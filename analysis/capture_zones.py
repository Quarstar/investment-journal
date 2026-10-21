"""Capture zones: per-stock support, capitulation and ceiling levels.

Re-run every Wednesday after appending the week's rows to data/daily_2026-10-14/ (daily OHLCV per
name from stockanalysis.com history pages; the last 50 sessions are used) and the weekly closes file.

Method (all mechanical; the judgment overlay lives on plans/capture-zones.md):
  1. Candidate support levels below the last close, from five sources:
       - daily swing lows (a low lower than the 3 sessions either side)
       - weekly swing closes over the past year (a close lower than the 2 weeks either side)
       - the 40-week moving average (~200-day)
       - the 52-week closing low
       - volume shelves: price bins (1 ATR wide) holding the most traded volume in the 50 sessions
  2. Candidates within 0.75 ATR of each other are merged into one level; its strength is the
     number of distinct sources/touches that agree.
  3. Zone 1 (first capture) = the strongest level at least 1 ATR below the last close and within
     2 weekly standard deviations; Zone 2 (capitulation) = the strongest level at least one weekly
     standard deviation below Zone 1, falling back to the 52-week low or a 40%-from-high level.
  4. Ceiling = the nearest daily swing-high cluster above the last close; the 52-week high is
     the major ceiling.
  5. Each zone is a band (level +/- 0.5 ATR). Forward P/E at the zone uses forward EPS implied by
     the 13 Oct snapshot (price / forward P/E). Touch probability: share of 20,000 simulated
     13-week daily paths (no drift, the stock's own volatility from the weekly closes) whose
     low reaches the zone's upper edge.
"""
import csv, json, math, os, sys
import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DAILY = os.path.join(ROOT, "data", "daily_2026-10-14")
WEEKLY = os.path.join(ROOT, "data", "weekly_closes_battles_2025-10-24_to_2026-10-09.csv")
FUND = os.path.join(ROOT, "data", "fundamentals_2026-10-13.csv")
NAMES = ["VST", "NEE", "NVDA", "TSM", "GOOGL", "UNP", "NU", "MCD",
         "NBIS", "AMD", "CEG", "MU", "TLN", "AVGO", "QQQ", "IREN", "APLD"]
rng = np.random.default_rng(20261015)


def load_daily(t, n=50):
    """The last n sessions in the file (files grow each week; the method uses 50)."""
    rows = list(csv.DictReader(open(os.path.join(DAILY, f"{t}.csv"))))
    rows.sort(key=lambda r: r["date"])
    rows = rows[-n:]
    return [{k: (r[k] if k == "date" else float(r[k])) for k in r} for r in rows]


def load_weekly():
    rows = list(csv.DictReader(open(WEEKLY)))
    return rows


def load_fund():
    return {r["ticker"]: r for r in csv.DictReader(open(FUND))}


def _is_friday(date):
    import datetime
    return datetime.date.fromisoformat(date).weekday() == 4


def atr(d, n=14):
    trs = []
    for i in range(1, len(d)):
        h, l, pc = d[i]["high"], d[i]["low"], d[i - 1]["close"]
        trs.append(max(h - l, abs(h - pc), abs(l - pc)))
    return float(np.mean(trs[-n:]))


def pivots(vals, k, kind):
    out = []
    for i in range(k, len(vals) - k):
        w = vals[i - k:i + k + 1]
        if kind == "low" and vals[i] == min(w):
            out.append((i, vals[i]))
        if kind == "high" and vals[i] == max(w):
            out.append((i, vals[i]))
    return out


def volume_nodes(d, width, top=3):
    lo = min(r["low"] for r in d)
    hi = max(r["high"] for r in d)
    nb = max(1, int(math.ceil((hi - lo) / width)))
    vol = np.zeros(nb)
    for r in d:
        tp = (r["high"] + r["low"] + r["close"]) / 3
        vol[min(nb - 1, int((tp - lo) / width))] += r["volume"]
    idx = np.argsort(vol)[::-1][:top]
    return [lo + (i + 0.5) * width for i in idx]


def cluster(cands, tol):
    """cands: list of (price, source). Merge within tol; strength = distinct sources + extra touches."""
    cands = sorted(cands)
    groups = []
    for p, s in cands:
        if groups and p - groups[-1]["px"][0] <= tol:
            g = groups[-1]
            g["px"].append(p); g["src"].append(s); g["hi"] = p
        else:
            groups.append({"px": [p], "src": [s], "hi": p})
    out = []
    for g in groups:
        out.append({"level": float(np.median(g["px"])), "strength": len(g["src"]),
                    "sources": sorted(set(g["src"])), "lo": min(g["px"]), "hi": max(g["px"])})
    return out


def touch_prob(last, level, vol_annual, days=63, n=20000):
    if level >= last:
        return 1.0
    sd = vol_annual / math.sqrt(252)
    z = rng.standard_normal((n, days)) * sd - 0.5 * sd * sd
    paths = last * np.exp(np.cumsum(z, axis=1))
    return float((paths.min(axis=1) <= level).mean())


def analyse(t, weekly, fund):
    d = load_daily(t)
    last = d[-1]["close"]
    wk = [float(r[t]) for r in weekly if r.get(t)]
    wdates = [r["week_ending"] for r in weekly if r.get(t)]
    if len(wk) < 20:  # no year of weekly closes in the file (IREN, APLD): use the daily file's Friday closes
        wk = [r["close"] for r in load_daily(t, 400) if r["date"] and _is_friday(r["date"])]
        wdates = [r["date"] for r in load_daily(t, 400) if _is_friday(r["date"])]
    closes_1y = wk + [last]
    a = atr(d)
    wr = np.diff(np.log(np.array(wk)))
    vol = float(wr.std(ddof=1) * math.sqrt(52))
    wk_sd = last * float(wr.std(ddof=1))
    ma40 = float(np.mean(wk[-40:]))
    hi52 = max(max(closes_1y), max(r["high"] for r in d))
    lo52 = min(min(closes_1y), min(r["low"] for r in d))
    lo52_close = min(closes_1y)

    cands = []
    for i, p in pivots([r["low"] for r in d], 3, "low"):
        cands.append((p, f"daily swing low {d[i]['date']}"))
    for i, p in pivots(wk, 2, "low"):
        cands.append((p, f"weekly swing close {wdates[i]}"))
    cands.append((ma40, "40-week average"))
    cands.append((lo52_close, "52-week closing low"))
    for p in volume_nodes(d, a):
        cands.append((p, "volume shelf"))
    below = [c for c in cands if c[0] < last]
    levels = [l for l in cluster(below, a)]
    levels.sort(key=lambda l: -l["level"])

    def pick(maxp, minp):
        pool = [l for l in levels if minp <= l["level"] <= maxp]
        if not pool:
            return None
        return max(pool, key=lambda l: (l["strength"], l["level"]))

    z1 = pick(last - a, last - 2 * wk_sd)
    if z1 is None:  # nothing structural in the window: take the nearest level below, else a volatility band
        near = [l for l in levels if last - 3 * wk_sd <= l["level"] <= last - a]
        z1 = near[0] if near else {"level": last - 1.5 * wk_sd, "strength": 0, "sources": ["volatility band (no structural support)"]}
    z2 = pick(z1["level"] - wk_sd, z1["level"] - 3 * wk_sd)
    if z2 is None:
        z2 = {"level": z1["level"] - 2 * wk_sd, "strength": 0, "sources": ["volatility band (no structural support)"]}

    highs = [(p, f"daily swing high {d[i]['date']}") for i, p in pivots([r["high"] for r in d], 3, "high") if p > last]
    ceil = cluster(highs, a)
    ceil = min(ceil, key=lambda l: l["level"]) if ceil else {"level": hi52, "strength": 1, "sources": ["52-week high"]}

    f = fund.get(t, {})
    try:
        eps = float(f["price_usd"]) / float(f["fwd_pe"])
    except (KeyError, ValueError, ZeroDivisionError):
        eps = None

    def band(l):
        lv = l["level"]
        return {"level": round(lv, 2), "top": round(lv + 0.5 * a, 2), "bottom": round(lv - 0.5 * a, 2),
                "strength": l["strength"], "sources": l["sources"],
                "pct_from_last": round(100 * (lv / last - 1), 1),
                "pct_from_high": round(100 * (lv / hi52 - 1), 1),
                "fwd_pe": round(lv / eps, 1) if eps else None,
                "p_touch_13w": round(touch_prob(last, lv + 0.5 * a, vol), 2)}

    testing = [l for l in levels if last - a < l["level"] < last]
    testing = max(testing, key=lambda l: l["strength"]) if testing else None
    return {"ticker": t, "testing_now": ({"level": round(testing["level"], 2), "strength": testing["strength"],
                                          "sources": testing["sources"]} if testing else None), "last_close": last, "last_date": d[-1]["date"], "atr14": round(a, 2), "vol_annual": round(vol, 3),
            "weekly_sd_usd": round(wk_sd, 2), "ma40w": round(ma40, 2), "high_52w": round(hi52, 2),
            "low_52w_close": round(lo52_close, 2), "fwd_pe_now": round(last / eps, 1) if eps else None,
            "zone1": band(z1) if z1 else None, "zone2": band(z2),
            "ceiling": {"level": round(ceil["level"], 2), "pct_from_last": round(100 * (ceil["level"] / last - 1), 1),
                        "sources": ceil["sources"]},
            "all_levels_below": [{"level": round(l["level"], 2), "strength": l["strength"], "sources": l["sources"]} for l in levels]}


def main():
    weekly = load_weekly()
    fund = load_fund()
    out = {t: analyse(t, weekly, fund) for t in NAMES}
    json.dump(out, open(os.path.join(ROOT, "analysis", "capture_zones_output.json"), "w"), indent=1)
    print("| Ticker | Last | ATR | Vol | 40w avg | 52w high | Zone 1 | Z1 str | Z1 fwd P/E | P(Z1) 13w | Zone 2 | Z2 str | Z2 fwd P/E | P(Z2) 13w | Ceiling |")
    print("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for t, r in out.items():
        z1, z2 = r["zone1"], r["zone2"]
        f = lambda z: f"{z['bottom']}–{z['top']} ({z['pct_from_last']}%)" if z else "–"
        print(f"| {t} | {r['last_close']} | {r['atr14']} | {r['vol_annual']:.0%} | {r['ma40w']} | {r['high_52w']} | "
              f"{f(z1)} | {z1['strength'] if z1 else ''} | {z1['fwd_pe'] if z1 else ''} | {z1['p_touch_13w'] if z1 else ''} | "
              f"{f(z2)} | {z2['strength']} | {z2['fwd_pe']} | {z2['p_touch_13w']} | {r['ceiling']['level']} ({r['ceiling']['pct_from_last']}%) |")


if __name__ == "__main__":
    main()
