"""Step 2 of the weekly run: every number in the review that can be computed, computed in code.

Runs the repo's own scripts (capture zones, risk-adjusted ranking) on the fresh prices, then adds:
  - where each name sits on its capture-zone map, and which zones broke on the Friday close
    (the map is re-drawn by hand; the agent only flags it)
  - the rotation gauge (4-week relative performance)
  - the drawdown plan's distance from the QQQ high
  - the VST/CEG ratio
Writes agent/out/metrics.json for the agent to read. No judgment lives here.
"""
from __future__ import annotations

import csv
import datetime as dt
import json
import subprocess
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG = tomllib.loads((ROOT / "agent" / "config.toml").read_text())
DAILY = ROOT / CONFIG["prices"]["daily_dir"]
WEEKLY = ROOT / "data" / "weekly_closes_battles_2025-10-24_to_2026-10-09.csv"
OUT = ROOT / "agent" / "out"


def closes(t: str) -> dict[str, float]:
    p = DAILY / f"{t}.csv"
    if not p.exists():
        return {}
    return {r["date"]: float(r["close"]) for r in csv.DictReader(open(p)) if r.get("close")}


def on_or_before(series: dict[str, float], day: str) -> tuple[str, float] | None:
    ds = [d for d in series if d <= day]
    return (max(ds), series[max(ds)]) if ds else None


def fridays(series: dict[str, float]) -> list[str]:
    return sorted(d for d in series if dt.date.fromisoformat(d).weekday() == 4)


def add_weekly_row() -> str | None:
    """Append the latest Friday's closes to the weekly file if it isn't there yet (blank where no data)."""
    q = closes("QQQ")
    fr = fridays(q)
    if not fr:
        return None
    friday = fr[-1]
    rows = list(csv.DictReader(open(WEEKLY)))
    if any(r["week_ending"] == friday for r in rows):
        return None
    hdr = open(WEEKLY).readline().strip().split(",")
    row = {"week_ending": friday}
    for t in hdr[1:]:
        c = closes(t).get(friday)
        row[t] = f"{c:.2f}" if c is not None else ""
    with open(WEEKLY, "a", newline="") as fh:
        csv.DictWriter(fh, fieldnames=hdr).writerow(row)
    return friday


def run_script(args: list[str]) -> str:
    r = subprocess.run([sys.executable, *args], cwd=ROOT, capture_output=True, text=True, timeout=600)
    if r.returncode != 0:
        raise RuntimeError(f"{' '.join(args)} failed: {r.stderr[-500:]}")
    return r.stdout


def band_status(last: float, z: dict) -> str:
    """Where the last close sits on the map, from the top down."""
    c1, c2, z1, z2 = z["ceiling1"], z["ceiling2"], z["zone1"]["band"], z["zone2"]["band"]
    tn = z["testing_now"] if z["testing_now"] and z["testing_now"][0] is not None else None
    levels = [("above the second ceiling", c2[1], None), ("inside the second ceiling", c2[0], c2[1]),
              ("between the ceilings", c1[1], c2[0]), ("inside the first ceiling", c1[0], c1[1])]
    if tn:
        levels += [("between support and the first ceiling", tn[1], c1[0]), ("testing support", tn[0], tn[1]),
                   ("between Zone 1 and support", z1[1], tn[0])]
    else:
        levels += [("above Zone 1", z1[1], c1[0])]
    levels += [("inside Zone 1", z1[0], z1[1]), ("between Zone 1 and Zone 2", z2[1], z1[0]),
               ("inside Zone 2 (capitulation)", z2[0], z2[1])]
    for name, lo, hi in levels:
        if last >= lo and (hi is None or last <= hi):
            return name
    return "below Zone 2"


def zone_flags(t: str, z: dict) -> list[str]:
    """The map's mechanical rules on Friday closes after the last re-map (config zones.map_week):
    a close below a band breaks it (re-map by hand); two closes above the first ceiling step the map up."""
    s = closes(t)
    fr = [d for d in fridays(s) if d > CONFIG["zones"]["map_week"]]
    if not fr:
        return []
    f1 = s[fr[-1]]
    flags = []
    tn = z["testing_now"] if z["testing_now"] and z["testing_now"][0] is not None else None
    for name, b in (("testing band", tn), ("Zone 1", z["zone1"]["band"]), ("Zone 2", z["zone2"]["band"])):
        if b and f1 < b[0]:
            flags.append(f"{fr[-1]} close {f1} is below the {name} ({b[0]}–{b[1]}): re-map needed")
            break
    c1top = z["ceiling1"][1]
    above = [d for d in fr[-2:] if s[d] > c1top]
    if len(above) == 2:
        flags.append(f"two Friday closes above the first ceiling ({c1top}): step the map up")
    elif f1 > c1top:
        flags.append(f"{fr[-1]} close {f1} is above the first ceiling ({c1top}); a second Friday above steps the map up")
    return flags


def pct(a: float, b: float) -> float:
    return round(100 * (a / b - 1), 2)


def rotation(price_date: str) -> dict:
    start_day = (dt.date.fromisoformat(price_date) - dt.timedelta(days=28)).isoformat()
    out = {}
    for t in ("RSP", "QQQ", "XLP", "XLY", "XLK"):
        s = closes(t)
        a, b = on_or_before(s, start_day), on_or_before(s, price_date)
        out[t] = {"from": a, "to": b, "return_pct": pct(b[1], a[1]) if a and b else None}
    r = {k: v["return_pct"] for k, v in out.items()}
    if None in r.values():
        return {"legs": out, "reading": "incomplete data"}
    passes = r["RSP"] > r["QQQ"] and (r["XLP"] > r["XLK"] or r["XLY"] > r["XLK"])
    return {"legs": out, "rsp_minus_qqq": round(r["RSP"] - r["QQQ"], 2),
            "xlp_minus_xlk": round(r["XLP"] - r["XLK"], 2), "xly_minus_xlk": round(r["XLY"] - r["XLK"], 2),
            "this_week_passes": passes,
            "note": "the gauge confirms after three passing reviews in a row; the count lives in the checklist"}


def main() -> None:
    prices = json.loads((OUT / "prices.json").read_text())
    price_date = prices.get("price_date")
    metrics = {"price_date": price_date, "weekly_row_added": add_weekly_row()}

    run_script(["analysis/capture_zones.py"])
    run_script(["analysis/capture_zones_final.py"])
    zones = json.loads((ROOT / "analysis" / "capture_zones_final.json").read_text())
    metrics["zones"] = {t: {"last": z["last"], "status": band_status(z["last"], z), "flags": zone_flags(t, z),
                            "testing": z["testing_now"], "zone1": z["zone1"], "zone2": z["zone2"],
                            "ceiling1": z["ceiling1"], "ceiling2": z["ceiling2"], "fwd_pe_now": z["fwd_pe_now"]}
                        for t, z in zones.items()}
    if prices.get("ranking_prices_file"):
        metrics["ranking_table"] = run_script(["analysis/risk_adjusted_ranking.py", "--prices", prices["ranking_prices_file"]])

    q = closes("QQQ")
    if price_date in q:
        hi = CONFIG["market"]["qqq_high"]
        metrics["drawdown"] = {"qqq": q[price_date], "high": hi, "from_high_pct": pct(q[price_date], hi),
                               "lines": {f"{l}%": round(hi * (1 + l / 100), 2) for l in CONFIG["market"]["drawdown_lines"]}}
    v, c = closes("VST").get(price_date), closes("CEG").get(price_date)
    if v and c:
        metrics["vst_ceg_ratio"] = {"value": round(v / c, 3), "band": "above 0.62 favours CEG, below 0.48 favours VST"}
    metrics["rotation"] = rotation(price_date) if price_date else None
    metrics["week_change_pct"] = {}
    for t in CONFIG["prices"]["us"]:
        s = closes(t)
        if price_date in s:
            prev = on_or_before(s, (dt.date.fromisoformat(price_date) - dt.timedelta(days=7)).isoformat())
            if prev:
                metrics["week_change_pct"][t] = {"close": s[price_date], "prev": prev, "change_pct": pct(s[price_date], prev[1])}
    (OUT / "metrics.json").write_text(json.dumps(metrics, indent=1))
    print(f"metrics: price date {price_date}; zone flags: "
          f"{sum(bool(z['flags']) for z in metrics['zones'].values())}; rotation passes: "
          f"{(metrics['rotation'] or {}).get('this_week_passes')}")


if __name__ == "__main__":
    main()
