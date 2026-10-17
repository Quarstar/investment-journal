"""Risk-adjusted ranking of the plan names: Sharpe, Sortino, reward-to-risk and PEG, each ranked, then a composite.
Expected return = consensus 12-month target vs price (optimistic by nature; the same bias for every name).
Risk from the past year of weekly closes (data/weekly_closes_battles_*.csv) and the block bootstrap in slot_battles_output.json.
Run: python3 analysis/risk_adjusted_ranking.py  [--prices file.csv with ticker,price to override the snapshot prices]
"""
import csv, json, sys
import numpy as np
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
rows = list(csv.DictReader(open(ROOT / 'data' / 'weekly_closes_battles_2025-10-24_to_2026-10-09.csv')))
F = {r['ticker']: r for r in csv.DictReader(open(ROOT / 'data' / 'fundamentals_2026-10-13.csv'))}
ST = json.load(open(ROOT / 'analysis' / 'slot_battles_output.json'))['stats']
RF = 0.05  # cash / 10-year, roughly
NAMES = ['NVDA', 'TSM', 'AVGO', 'GOOGL', 'VST', 'NEE', 'CEG', 'TLN', 'MU', 'AMD', 'UNP', 'NU', 'MCD']
# prices: 15 Oct 2026 closes where verified, else the 13 Oct snapshot
PX = {'NVDA': 217.23, 'TSM': 422.25, 'AVGO': 346.25, 'GOOGL': 349.22, 'VST': 154.17, 'NEE': 78.96, 'CEG': 279.54,
      'TLN': 358.42, 'MU': 931.24, 'AMD': 570.82, 'UNP': 288.71, 'NU': 14.73, 'MCD': 242.50, 'NBIS': 188.41}
if '--prices' in sys.argv:
    for r in csv.DictReader(open(sys.argv[sys.argv.index('--prices') + 1])):
        PX[r['ticker']] = float(r['price'])
out = []
for t in NAMES:
    f = F[t]; p = PX.get(t) or float(f['price_usd'])
    r = np.diff(np.log(np.array([float(x[t]) for x in rows])))
    vol = r.std(ddof=1) * np.sqrt(52)
    dn = r[r < 0]; ddev = np.sqrt((dn ** 2).sum() / len(r)) * np.sqrt(52)  # downside deviation (target 0)
    up = float(f['analyst_target']) / p - 1
    sharpe = (up - RF) / vol
    sortino = (up - RF) / ddev
    q05 = ST[t]['q05_26w'] / 100
    rr = up / abs(q05)
    fwd = float(f['fwd_pe']) if f['fwd_pe'] else None
    g = float(f['ni_growth_pct']) if f['ni_growth_pct'] else None
    peg = fwd / g if (fwd and g and g > 0) else None
    out.append(dict(t=t, p=p, up=up, vol=vol, ddev=ddev, q05=q05, sharpe=sharpe, sortino=sortino, rr=rr, fwd=fwd, peg=peg, pdd=ST[t]['p_dd20']))
def rank(key, higher_better=True, only=None):
    pool = [o for o in out if (o[key] is not None)]
    order = sorted(pool, key=lambda o: -o[key] if higher_better else o[key])
    for i, o in enumerate(order): o['r_' + key] = i + 1
    for o in out:
        if 'r_' + key not in o: o['r_' + key] = None
rank('sharpe'); rank('sortino'); rank('rr'); rank('peg', higher_better=False)
for o in out:
    rs = [o['r_sharpe'], o['r_sortino'], o['r_rr']] + ([o['r_peg']] if o['r_peg'] else [])
    o['comp'] = sum(rs) / len(rs)
out.sort(key=lambda o: o['comp'])
print('| # | Name | Price | Upside to target | Vol | Downside dev. | Sharpe | Sortino | Reward÷risk (5th pct 26w) | Fwd P/E | PEG | Avg rank |')
print('|---|---|---|---|---|---|---|---|---|---|---|---|')
for i, o in enumerate(out, 1):
    peg = f"{o['peg']:.2f} ({o['r_peg']})" if o['peg'] else 'n/a'
    print(f"| {i} | {o['t']} | {o['p']:.2f} | {o['up']*100:+.0f}% | {o['vol']*100:.0f}% | {o['ddev']*100:.0f}% | {o['sharpe']:.2f} ({o['r_sharpe']}) | {o['sortino']:.2f} ({o['r_sortino']}) | {o['rr']:.2f} ({o['r_rr']}) | {o['fwd'] or '-'} | {peg} | {o['comp']:.1f} |")
