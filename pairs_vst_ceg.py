"""
Long-only pairs tilt: VST vs CEG
================================

Question: both stocks sell the same thing (nuclear/firm power to AI data
centres). When one runs ahead of the other, does tilting a 2-stock nuclear
sleeve toward the laggard beat simply holding 50/50?

This is NOT classic stat arb (no shorting -- I invest through an ISA).
It is a *relative value* rule for deciding which of two similar holdings
gets the weight.

Rule
----
* Signal = z-score of log(VST / CEG) against its own rolling window.
* z > +ENTRY  -> VST is rich vs CEG  -> hold 25% VST / 75% CEG
* z < -ENTRY  -> VST is cheap vs CEG -> hold 75% VST / 25% CEG
* |z| < EXIT  -> relationship back to normal -> 50 / 50
* Otherwise keep the current tilt (hysteresis, avoids flip-flopping).
* Signal is computed on day t's close and traded on day t+1's close
  (no look-ahead).
* Every trade pays FEE on the amount traded (my broker's FX fee on
  US shares is ~0.15% per side).

Benchmark: 50/50 bought on the first test day and held.

Run:  python backtests/pairs_vst_ceg.py
"""

from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT_PNG = Path(__file__).with_name("pairs_vst_ceg.png")

WINDOW = 60     # trading days in the rolling z-score
ENTRY = 1.5     # |z| to start a tilt
EXIT = 0.5      # |z| to go back to 50/50
TILT = 0.25     # 25/75 when tilted
FEE = 0.0015    # 0.15% per side on traded value


def load() -> pd.DataFrame:
    vst = pd.read_csv(DATA / "VST.csv", parse_dates=["date"]).rename(columns={"close": "VST"})
    ceg = pd.read_csv(DATA / "CEG.csv", parse_dates=["date"]).rename(columns={"close": "CEG"})
    df = vst.merge(ceg, on="date", how="inner").set_index("date").sort_index()
    assert len(df) == len(vst) == len(ceg), "date mismatch between VST and CEG files"
    return df


def describe(df: pd.DataFrame) -> dict:
    ratio = df.VST / df.CEG
    log_r = np.log(ratio)
    rets = df.pct_change().dropna()
    # AR(1) on the log ratio -> half-life of mean reversion
    y, x = log_r.diff().dropna(), log_r.shift(1).dropna()
    x = x.loc[y.index]
    beta = np.polyfit(x, y, 1)[0]
    half_life = -np.log(2) / beta if beta < 0 else np.inf
    return {
        "days": len(df),
        "start": df.index[0].date(),
        "end": df.index[-1].date(),
        "ratio_now": ratio.iloc[-1],
        "ratio_mean": ratio.mean(),
        "ratio_min": ratio.min(),
        "ratio_min_date": ratio.idxmin().date(),
        "ratio_max": ratio.max(),
        "ratio_max_date": ratio.idxmax().date(),
        "z_full_period": (log_r.iloc[-1] - log_r.mean()) / log_r.std(),
        "return_corr": rets.VST.corr(rets.CEG),
        "half_life_days": half_life,
        "vst_change": df.VST.iloc[-1] / df.VST.iloc[0] - 1,
        "ceg_change": df.CEG.iloc[-1] / df.CEG.iloc[0] - 1,
    }


def backtest(df, window=WINDOW, entry=ENTRY, exit_=EXIT, tilt=TILT, fee=FEE):
    log_r = np.log(df.VST / df.CEG)
    mu = log_r.rolling(window).mean()
    sd = log_r.rolling(window).std()
    z = (log_r - mu) / sd

    # target VST weight decided on each close (state machine with hysteresis)
    target = pd.Series(np.nan, index=df.index)
    state = 0.5
    for t, zt in z.items():
        if np.isnan(zt):
            continue
        if zt > entry:
            state = tilt            # VST rich -> underweight VST
        elif zt < -entry:
            state = 1 - tilt        # VST cheap -> overweight VST
        elif abs(zt) < exit_:
            state = 0.5
        target[t] = state

    test = df.loc[target.dropna().index]
    trade_w = target.dropna().shift(1)          # trade the day after the signal
    trade_w.iloc[0] = 0.5
    rets = test.pct_change().fillna(0)

    # strategy: holdings drift between trades, rebalance (and pay fees) only when target changes
    value, w_vst = 1.0, 0.5
    curve, trades = [], 0
    for i, t in enumerate(test.index):
        if i > 0:
            gross = w_vst * (1 + rets.VST[t]) + (1 - w_vst) * (1 + rets.CEG[t])
            w_vst = w_vst * (1 + rets.VST[t]) / gross
            value *= gross
        tgt = trade_w[t]
        if abs(tgt - w_vst) > 0.05:              # only act on a real signal change
            traded = abs(tgt - w_vst) * 2         # sell one leg, buy the other
            value *= 1 - traded * fee
            w_vst = tgt
            trades += 1
        curve.append(value)
    strat = pd.Series(curve, index=test.index)

    bench = 0.5 * test.VST / test.VST.iloc[0] + 0.5 * test.CEG / test.CEG.iloc[0]

    def max_dd(s):
        return (s / s.cummax() - 1).min()

    return {
        "z": z,
        "mu": mu,
        "sd": sd,
        "strat": strat,
        "bench": bench,
        "strat_ret": strat.iloc[-1] - 1,
        "bench_ret": bench.iloc[-1] - 1,
        "strat_dd": max_dd(strat),
        "bench_dd": max_dd(bench),
        "rebalances": trades,
        "days_tilted": int((trade_w.round(2) != 0.5).sum()),
        "test_days": len(test),
    }


def main():
    df = load()
    d = describe(df)
    r = backtest(df)

    print("=== Relationship ===")
    print(f"Period:            {d['start']} -> {d['end']}  ({d['days']} trading days)")
    print(f"VST change:        {d['vst_change']:+.1%}")
    print(f"CEG change:        {d['ceg_change']:+.1%}")
    print(f"Daily return corr: {d['return_corr']:.2f}")
    print(f"VST/CEG now:       {d['ratio_now']:.3f}  (1y mean {d['ratio_mean']:.3f}, "
          f"range {d['ratio_min']:.3f} on {d['ratio_min_date']} to {d['ratio_max']:.3f} on {d['ratio_max_date']})")
    print(f"z vs full year:    {d['z_full_period']:+.2f}")
    print(f"z vs last {WINDOW}d:    {r['z'].iloc[-1]:+.2f}")
    print(f"Mean-reversion half-life: {d['half_life_days']:.0f} trading days")

    print(f"\n=== Backtest (window {WINDOW}, entry {ENTRY}, exit {EXIT}, fee {FEE:.2%}/side) ===")
    print(f"Test days:         {r['test_days']}  (first {WINDOW} days used to warm up)")
    print(f"Tilt strategy:     {r['strat_ret']:+.1%}   max drawdown {r['strat_dd']:.1%}")
    print(f"50/50 buy & hold:  {r['bench_ret']:+.1%}   max drawdown {r['bench_dd']:.1%}")
    print(f"Edge vs benchmark: {r['strat_ret'] - r['bench_ret']:+.1%}")
    print(f"Rebalances:        {r['rebalances']}   days spent tilted: {r['days_tilted']}")

    print("\n=== Sensitivity: edge vs 50/50 (percentage points) ===")
    print("window  entry=1.0  entry=1.5  entry=2.0")
    for w in (40, 60, 90):
        row = []
        for e in (1.0, 1.5, 2.0):
            s = backtest(df, window=w, entry=e)
            row.append(f"{(s['strat_ret'] - s['bench_ret']) * 100:+8.1f}")
        print(f"{w:>6}  " + "   ".join(row))

    # chart
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 7), sharex=True)
    ratio = df.VST / df.CEG
    ax1.plot(ratio.index, ratio, color="#2a6f97", lw=1.4, label="VST / CEG")
    band_mid = np.exp(r["mu"])
    ax1.plot(band_mid.index, band_mid, color="#999", lw=1, ls="--", label=f"{WINDOW}-day mean")
    ax1.fill_between(band_mid.index, np.exp(r["mu"] - ENTRY * r["sd"]), np.exp(r["mu"] + ENTRY * r["sd"]),
                     color="#2a6f97", alpha=0.08, label=f"±{ENTRY} sd entry band")
    ax1.set_ylabel("Price ratio")
    ax1.set_title("VST vs CEG: price ratio and tilt-rule bands")
    ax1.legend(loc="upper left", frameon=False)
    ax2.plot(r["strat"].index, r["strat"], color="#c44e52", lw=1.4, label="Tilt rule (after fees)")
    ax2.plot(r["bench"].index, r["bench"], color="#555", lw=1.2, label="50/50 buy & hold")
    ax2.set_ylabel("Growth of 1")
    ax2.legend(loc="upper left", frameon=False)
    for ax in (ax1, ax2):
        ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=150)
    print(f"\nChart saved to {OUT_PNG.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
