"""Step 1 of the weekly run: fetch daily bars, cross-check them, and append them to the repo's CSVs.

Deterministic on purpose: prices come from data feeds, not from the language model.
  primary     Yahoo Finance chart API (no key)
  cross-check Twelve Data (free key, optional: set the TWELVEDATA_API_KEY secret). Without it every close is
              marked "single source" and the agent spot-checks the holdings' closes on the web instead.
              (Nasdaq.com times out and Stooq returns nothing from GitHub's runners, so neither is used.)
A close is "verified" when both sources agree within config.prices.max_source_gap_pct, "single source"
when only one answered, and "unverified" when they disagree (the draft flags it; nothing is guessed).

Usage:
  python agent/prices.py                 # fetch, cross-check, append, write agent/out/prices.json
  python agent/prices.py --offline       # no network: summarise what's already in the CSVs (for testing)
"""
from __future__ import annotations

import csv
import datetime as dt
import io
import json
import os
import sys
import time
import tomllib
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG = tomllib.loads((ROOT / "agent" / "config.toml").read_text())
DAILY = ROOT / CONFIG["prices"]["daily_dir"]
OUT = ROOT / "agent" / "out"
FIELDS = ["date", "open", "high", "low", "close", "volume"]
UA = {"User-Agent": "Mozilla/5.0 (investment-journal weekly agent; github.com/Quarstar)"}


def _get(url: str, timeout: int = 20) -> bytes:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()

# ---------- parsers (pure; tested with fixtures) ----------

def _rnd(x: float) -> str:
    return f"{x:.2f}" if abs(x) >= 1 else f"{x:.4f}"


def parse_yahoo(payload: bytes) -> tuple[list[dict], dict]:
    """Yahoo v8 chart JSON -> (rows oldest first, meta). Skips bars with a missing close."""
    res = json.loads(payload)["chart"]["result"][0]
    meta = res.get("meta", {})
    off = int(meta.get("gmtoffset", 0))
    q = res["indicators"]["quote"][0]
    rows = []
    for i, ts in enumerate(res.get("timestamp", []) or []):
        c = q["close"][i]
        if c is None:
            continue
        day = dt.datetime.fromtimestamp(ts + off, dt.timezone.utc).date().isoformat()
        rows.append({"date": day, "open": _rnd(q["open"][i] or c), "high": _rnd(q["high"][i] or c),
                     "low": _rnd(q["low"][i] or c), "close": _rnd(c),
                     "volume": str(int(q["volume"][i])) if q["volume"][i] is not None else ""})
    return rows, {"currency": meta.get("currency"), "exchange": meta.get("exchangeName")}


def merge(existing: list[dict], new: list[dict]) -> tuple[list[dict], list[str]]:
    """Add rows for dates not already in the file. Existing rows are never overwritten. Newest first."""
    have = {r["date"] for r in existing}
    added = [r for r in new if r["date"] not in have]
    rows = sorted(existing + added, key=lambda r: r["date"], reverse=True)
    return rows, sorted(r["date"] for r in added)


def cross_check(primary_close: float, check_close: float | None, max_gap_pct: float) -> tuple[str, float | None]:
    if check_close is None:
        return "single source", None
    gap = 100 * abs(primary_close / check_close - 1)
    return ("verified" if gap <= max_gap_pct else "unverified"), round(gap, 3)

# ---------- fetch ----------

def fetch_yahoo(symbol: str, rng: str) -> tuple[list[dict], dict]:
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?range={rng}&interval=1d&includePrePost=false"
    return parse_yahoo(_get(url))


def parse_twelvedata(payload: bytes) -> list[dict]:
    """Twelve Data time_series JSON -> rows oldest first (date and close only)."""
    try:
        d = json.loads(payload)
    except ValueError:
        return []
    if d.get("status") != "ok":
        return []
    rows = []
    for v in d.get("values", []):
        try:
            rows.append({"date": v["datetime"][:10], "close": _rnd(float(v["close"]))})
        except (KeyError, ValueError):
            continue
    return sorted(rows, key=lambda r: r["date"])


def fetch_twelvedata(symbol: str, key: str) -> list[dict]:
    url = (f"https://api.twelvedata.com/time_series?symbol={symbol}&interval=1day&outputsize=10"
           f"&apikey={key}")
    return parse_twelvedata(_get(url, timeout=15))


def read_csv(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return list(csv.DictReader(open(path)))


def write_csv(path: Path, rows: list[dict]) -> None:
    with open(path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(rows)


def run(offline: bool = False) -> dict:
    gap_limit = CONFIG["prices"]["max_source_gap_pct"]
    report = {"generated_utc": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"), "tickers": {}}
    failures = 0
    for t in CONFIG["prices"]["us"] + CONFIG["prices"]["london"]:
        london = t.endswith(".L")
        path = DAILY / f"{t}.csv"
        existing = [] if london else read_csv(path)
        entry = {"source": None, "status": "missing", "added_dates": []}
        try:
            if offline:
                rows, meta = sorted(existing, key=lambda r: r["date"]), {}
            else:
                rows, meta = fetch_yahoo(t, "1mo" if existing else "6mo")
                today = dt.datetime.now(dt.timezone.utc).date().isoformat()
                rows = [r for r in rows if r["date"] < today]  # today's bar may still be trading
                entry["source"] = "yahoo"
                entry["currency"] = meta.get("currency")
            if not rows:
                raise ValueError("no rows")
            last = rows[-1]
            check_close = None
            td_key = os.environ.get("TWELVEDATA_API_KEY")
            if not offline and not london and td_key and failures < 3:
                try:
                    ref = {r["date"]: float(r["close"]) for r in fetch_twelvedata(t, td_key)}
                    check_close = ref.get(last["date"])
                    if check_close is not None:
                        entry["cross_check_source"] = "twelvedata"
                except Exception as e:  # the cross-check is best effort
                    entry["cross_check_error"] = type(e).__name__
                    failures += 1
                time.sleep(8)  # the free tier allows 8 requests a minute
            status, gap = cross_check(float(last["close"]), check_close, gap_limit)
            entry.update({"last_date": last["date"], "close": float(last["close"]),
                          "status": "from file" if offline else status, "gap_pct": gap})
            if not london and not offline:
                merged, added = merge(existing, rows)
                write_csv(path, merged)
                entry["added_dates"] = added
            if london:
                entry["last_rows"] = rows[-5:]
        except Exception as e:
            entry["error"] = f"{type(e).__name__}: {e}"[:200]
        report["tickers"][t] = entry

    # the ranking's price file, named for the close it uses
    closes = {t: e for t, e in report["tickers"].items() if e.get("close") is not None}
    if closes:
        last_dates = sorted({e["last_date"] for t, e in closes.items() if not t.endswith(".L")})
        tag = last_dates[-1]
        out = ROOT / "data" / f"prices_{tag}.csv"
        with open(out, "w") as fh:
            fh.write("ticker,price\n")
            for t in CONFIG["prices"]["ranking"]:
                if t in closes:
                    fh.write(f"{t},{closes[t]['close']}\n")
        report["ranking_prices_file"] = str(out.relative_to(ROOT))
        report["price_date"] = tag
    OUT.mkdir(exist_ok=True)
    (OUT / "prices.json").write_text(json.dumps(report, indent=1))
    return report


if __name__ == "__main__":
    rep = run(offline="--offline" in sys.argv)
    bad = {t: e.get("error") or e["status"] for t, e in rep["tickers"].items()
           if e.get("error") or e["status"] in ("unverified", "missing")}
    print(f"prices: {len(rep['tickers'])} tickers, last date {rep.get('price_date')}; problems: {bad or 'none'}")
