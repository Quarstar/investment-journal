#!/usr/bin/env python3
"""
Slot battles, 13 Oct 2026.

Every slot in the planned core and anchor sleeve is contested: the name I own (or plan to own)
against the best alternatives in the same sector. Same data, same rules for everyone.

Inputs (both in data/):
  weekly_closes_battles_2025-10-24_to_2026-10-09.csv   51 Friday closes for 35 names + QQQ + US 10-year yield
  fundamentals_2026-10-13.csv                           quote-page snapshot taken 13 Oct 2026

Per name, on 50 weekly log returns:
  vol        annualised volatility, %
  beta       beta to QQQ
  corrQ/corrN  correlation with QQQ / NVDA
  worst10    average simple return in QQQ's 10 worst weeks of the window, %
  maxdd      worst peak-to-trough fall inside the window, %
  rate       % move per +1.00 point rise in the 10-year yield, after controlling for QQQ (t-stat alongside)
  fit        average correlation with the *other* roles in the planned core (lower = better diversifier)
  p_dd20     probability of a 20%+ drawdown inside 26 weeks, from a stationary block bootstrap
             (mean block 4 weeks, 20,000 paths) of the name's weekly returns with the average return
             REMOVED. Last year's average return is the thing least likely to repeat; what is left is
             the size and clustering of the moves.
  q05_26w    5th-percentile 26-week return from the same bootstrap, %

Then:
  1. a rank-based rubric per slot (best in the group = 10, worst = 0, linear in between), weighted,
     shown with and without the manual judgment criterion;
  2. a robustness run: 1,000 block-bootstrap resamples of the year (so every statistic is recomputed on
     a slightly different history) combined with random perturbation of the rubric weights
     (each weight x exp(N(0, 0.4))). The share of runs each name wins its slot is its win probability.
     Fundamentals are facts as of 13 Oct and are not resampled;
  3. a joint block bootstrap of the January-stage book (same weeks drawn for every name, so the
     correlations survive) for Option D versus the battle winners versus my recommendation.

Run:  python3 analysis/slot_battles.py     (about two minutes; most of it is the robustness run)
"""
import csv, json, sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
PX = ROOT / 'data' / 'weekly_closes_battles_2025-10-24_to_2026-10-09.csv'
FU = ROOT / 'data' / 'fundamentals_2026-10-13.csv'
rng = np.random.default_rng(20261013)
QUICK = '--quick' in sys.argv

# ---------- data ----------
rows = list(csv.DictReader(open(PX)))
dates = [r['week_ending'] for r in rows]
tickers = [c for c in rows[0] if c not in ('week_ending', 'US10Y')]
P = {t: np.array([float(r[t]) for r in rows]) for t in tickers}
Y = np.array([float(r['US10Y']) for r in rows])
R = {t: np.diff(np.log(P[t])) for t in tickers}
DY = np.diff(Y)
n = len(R['QQQ'])

F = {}
for r in csv.DictReader(open(FU)):
    f = {k: (float(v) if v not in ('', None) and k not in ('ticker', 'role', 'next_results') else v) for k, v in r.items()}
    f['net_margin'] = 100 * f['net_income_ttm_bn'] / f['revenue_ttm_bn']
    F[r['ticker']] = f
NAMES = list(F)

# ---------- block bootstrap ----------
def sbb_indices(n, H, npaths, L):
    """Stationary block bootstrap (Politis & Romano): blocks of random length, mean L, wrapping round."""
    idx = np.empty((npaths, H), dtype=int)
    idx[:, 0] = rng.integers(0, n, npaths)
    cont = rng.random((npaths, H)) >= 1.0 / L
    new = rng.integers(0, n, (npaths, H))
    for h in range(1, H):
        idx[:, h] = np.where(cont[:, h], (idx[:, h - 1] + 1) % n, new[:, h])
    return idx

H, NPATHS, L = 26, 20000, 4
IDX = sbb_indices(n, H, NPATHS, L)          # one set of draws, reused for every name and every team
IDX_SMALL = sbb_indices(n, H, 2000, L)      # for the robustness run

def path_stats(weekly_log):
    """weekly_log: (npaths, H) log returns -> drawdown probabilities and 26-week return percentiles."""
    cum = np.cumsum(weekly_log, axis=1)
    run = np.maximum.accumulate(np.concatenate([np.zeros((cum.shape[0], 1)), cum], axis=1), axis=1)[:, 1:]
    mdd = (1 - np.exp(cum - run)).max(axis=1)
    tot = np.exp(cum[:, -1]) - 1
    return dict(p_dd20=100 * (mdd >= 0.20).mean(), p_dd15=100 * (mdd >= 0.15).mean(),
                p_dd10=100 * (mdd >= 0.10).mean(), q05=100 * np.percentile(tot, 5), med=100 * np.median(tot))

# ---------- per-name statistics ----------
ROLE_OTHERS = {   # "fit": the other roles in the planned core
    'chips': ['VST', 'CEG', 'GOOGL'],
    'power': ['NVDA', 'TSM', 'GOOGL'],
    'adopter': ['NVDA', 'TSM', 'VST', 'CEG'],
    'anchor': ['NVDA', 'TSM', 'VST', 'CEG', 'GOOGL'],
}

def stats(t, role, Rd, dy, idx_paths, prices=None):
    r = Rd[t]; q = Rd['QQQ']
    w10 = np.argsort(q)[:10]
    s = {}
    p = prices if prices is not None else np.exp(np.concatenate([[0], np.cumsum(r)]))
    s['ret1y'] = 100 * (p[-1] / p[0] - 1)
    s['vol'] = 100 * r.std(ddof=1) * np.sqrt(52)
    s['beta'] = np.cov(r, q, ddof=1)[0, 1] / q.var(ddof=1)
    s['corrQ'] = np.corrcoef(r, q)[0, 1]
    s['corrN'] = np.corrcoef(r, Rd['NVDA'])[0, 1] if t != 'NVDA' else 1.0
    s['worst10'] = 100 * (np.exp(r[w10]) - 1).mean()
    s['qqq_worst10'] = 100 * (np.exp(q[w10]) - 1).mean()
    s['maxdd'] = 100 * (p / np.maximum.accumulate(p) - 1).min()
    X = np.column_stack([np.ones(len(r)), q, dy])
    b = np.linalg.lstsq(X, r, rcond=None)[0]
    resid = r - X @ b
    cov = (resid @ resid / (len(r) - 3)) * np.linalg.inv(X.T @ X)
    s['rate'] = 100 * b[2]; s['rate_t'] = b[2] / np.sqrt(cov[2, 2]); s['b_mkt'] = b[1]
    others = [o for o in ROLE_OTHERS[role.split('-')[0]] if o != t]
    s['fit'] = float(np.mean([np.corrcoef(r, Rd[o])[0, 1] for o in others]))
    bs = path_stats((r - r.mean())[idx_paths])
    s['p_dd20'] = bs['p_dd20']; s['q05_26w'] = bs['q05']
    return s

ST = {t: stats(t, F[t]['role'], R, DY, IDX, P[t]) for t in NAMES}
ST['QQQ'] = stats('QQQ', 'anchor', R, DY, IDX, P['QQQ'])

# ---------- rubric ----------
def rank_scores(values, higher_better=True):
    """Rank-based 0-10: best = 10, worst = 0, ties share the average rank."""
    v = np.array(values, float)
    order = v if higher_better else -v
    srt = np.argsort(-order, kind='stable')
    ranks = np.empty(len(v))
    i = 0
    while i < len(v):
        j = i
        while j + 1 < len(v) and order[srt[j + 1]] == order[srt[i]]:
            j += 1
        ranks[srt[i:j + 1]] = (i + j) / 2
        i = j + 1
    k = len(v) - 1
    return 10 * (k - ranks) / k if k else np.full(len(v), 10.0)

# criteria: (label, weight, source, key, higher_better); source 'F' = fundamentals, 'S' = statistics
BATTLES = {
    'chips': dict(
        names=['NVDA', 'TSM', 'AVGO', 'AMD', 'ASML', 'MU'], slots=2,
        criteria=[('growth', 20, 'F', 'rev_growth_ttm_pct', True),
                  ('valuation', 25, 'F', 'fwd_pe', False),
                  ('quality', 10, 'F', 'net_margin', True),
                  ('risk', 20, 'S', 'p_dd20', False),
                  ('worst10', 10, 'S', 'worst10', True),
                  ('fit', 15, 'S', 'fit', False)],
        manual=('durability', 10, {'NVDA': 8, 'TSM': 10, 'AVGO': 8, 'AMD': 6, 'ASML': 10, 'MU': 3}),
    ),
    'power': dict(
        names=['VST', 'CEG', 'TLN', 'NRG', 'GEV', 'NEE'], slots=2,
        criteria=[('valuation', 20, 'F', 'fwd_pe', False),
                  ('growth', 10, 'F', 'rev_growth_ttm_pct', True),
                  ('profitability', 10, 'F', 'net_margin', True),
                  ('rates', 15, 'S', 'rate', True),
                  ('risk', 15, 'S', 'p_dd20', False),
                  ('worst10', 10, 'S', 'worst10', True),
                  ('fit', 10, 'S', 'fit', False)],
        manual=('contracts', 10, {'VST': 8, 'CEG': 10, 'TLN': 9, 'NRG': 5, 'GEV': 6, 'NEE': 5}),
    ),
    'adopter': dict(
        names=['GOOGL', 'META', 'MSFT', 'AMZN', 'NOW'], slots=1,
        criteria=[('growth', 20, 'F', 'rev_growth_ttm_pct', True),
                  ('valuation', 20, 'F', 'fwd_pe', False),
                  ('quality', 10, 'F', 'net_margin', True),
                  ('risk', 15, 'S', 'p_dd20', False),
                  ('worst10', 10, 'S', 'worst10', True),
                  ('fit', 15, 'S', 'fit', False)],
        manual=('purity', 10, {'GOOGL': 7, 'META': 10, 'MSFT': 5, 'AMZN': 4, 'NOW': 9}),
    ),
}
ANCHOR_CRITERIA = [('worst10', 25, 'S', 'worst10', True),
                   ('risk', 15, 'S', 'p_dd20', False),
                   ('maxdd', 10, 'S', 'maxdd', True),
                   ('valuation', 15, 'F', 'fwd_pe', False),
                   ('growth', 15, 'F', 'rev_growth_ttm_pct', True),
                   ('quality', 10, 'F', 'net_margin', True),
                   ('dividend', 5, 'F', 'div_yield_pct', True),
                   ('corrN', 5, 'S', 'corrN', False)]
for sub, names in {'transport': ['UBER', 'DASH', 'UNP'], 'financials': ['NU', 'NDAQ', 'JPM', 'V'],
                   'consumer': ['MCD', 'WMT', 'COST', 'CMG'], 'defence': ['BWXT', 'AVAV', 'LMT', 'KTOS']}.items():
    BATTLES['anchor-' + sub] = dict(names=names, slots=1, criteria=ANCHOR_CRITERIA, manual=None)

def anchor_test(t, S):
    s = S[t]
    return dict(beta=s['beta'] < 0.8, corrN=s['corrN'] < 0.5, worst10=s['worst10'] > s['qqq_worst10'])

def value(t, src, key, S):
    return F[t][key] if src == 'F' else S[t][key]

def score_battle(name, S, weights=None, manual_on=True):
    """Returns (table, totals, passes). weights: optional dict label->weight override."""
    b = BATTLES[name]; names = b['names']
    table = {t: {} for t in names}; tot = {t: 0.0 for t in names}
    for label, w, src, key, hb in b['criteria']:
        w = weights[label] if weights else w
        vals = [value(t, src, key, S) for t in names]
        sc = rank_scores(vals, hb)
        for t, v, s in zip(names, vals, sc):
            table[t][label] = (v, s * w / 10); tot[t] += s * w / 10
    if b['manual'] and manual_on:
        label, w, scores = b['manual']
        w = weights[label] if weights else w
        for t in names:
            table[t][label] = (scores[t], scores[t] * w / 10); tot[t] += scores[t] * w / 10
    passes = {t: all(anchor_test(t, S).values()) for t in names} if name.startswith('anchor') else {t: True for t in names}
    return table, tot, passes

def winners(name, tot, passes):
    ranked = sorted([t for t in BATTLES[name]['names'] if passes[t]], key=lambda t: -tot[t])
    return ranked[:BATTLES[name]['slots']]

RESULTS = {}
for name in BATTLES:
    table, full, passes = score_battle(name, ST)
    _, num, _ = score_battle(name, ST, manual_on=False)
    RESULTS[name] = (table, num, full, passes)

# ---------- robustness: resample the year, perturb the weights ----------
B = 60 if QUICK else 1000
WIN = {name: {t: 0 for t in BATTLES[name]['names']} for name in BATTLES}
PASS = {t: 0 for t in NAMES}
for bi in range(B):
    idx = sbb_indices(n, n, 1, L)[0]
    Rb = {t: R[t][idx] for t in tickers}; dyb = DY[idx]
    Sb = {t: stats(t, F[t]['role'], Rb, dyb, IDX_SMALL) for t in NAMES}
    for t in NAMES:
        PASS[t] += all(anchor_test(t, Sb).values())
    for name, b in BATTLES.items():
        labels = [c[0] for c in b['criteria']] + ([b['manual'][0]] if b['manual'] else [])
        base = [c[1] for c in b['criteria']] + ([b['manual'][1]] if b['manual'] else [])
        wts = {l: w * np.exp(rng.normal(0, 0.4)) for l, w in zip(labels, base)}
        _, tot, passes = score_battle(name, Sb, wts)
        for t in winners(name, tot, passes):
            WIN[name][t] += 1

# ---------- team Monte Carlo ----------
ETF = {'XLVP': 12, 'VUKG': 6}       # January-stage defensive layer; cash 25% and sandbox 1% treated as cash

def team_sim(wts, demean=True):
    simple = np.zeros((NPATHS, H))
    for t, w in wts.items():
        r = R[t] - (R[t].mean() if demean else 0.0)
        simple += w / 100 * (np.exp(r[IDX]) - 1)
    return path_stats(np.log1p(simple))

def team_desc(wts):
    q = R['QQQ']; w10 = np.argsort(q)[:10]
    simple = sum(w / 100 * (np.exp(R[t]) - 1) for t, w in wts.items())
    r = np.log1p(simple); p = np.exp(np.concatenate([[0], np.cumsum(r)]))
    beta = np.cov(r, q, ddof=1)[0, 1] / q.var(ddof=1)
    X = np.column_stack([np.ones(n), q, DY]); b = np.linalg.lstsq(X, r, rcond=None)[0]
    nb = {t: np.cov(R[t], R['NVDA'], ddof=1)[0, 1] / R['NVDA'].var(ddof=1) for t in wts}
    return dict(vol=100 * r.std(ddof=1) * np.sqrt(52), beta=beta,
                worst10=100 * (np.exp(r[w10]) - 1).mean(), maxdd=100 * (p / np.maximum.accumulate(p) - 1).min(),
                ret1y=100 * (p[-1] - 1), rate=100 * b[2],
                qqq_m25=beta * -25, qqq_p20=beta * 20,
                nvda_m40=sum(w / 100 * nb[t] * -40 for t, w in wts.items()),
                rate_shock=b[1] * -5 + b[2] * 0.5)

def pick(name, use_manual=True):
    table, num, full, passes = RESULTS[name]
    return winners(name, full if use_manual else num, passes)

pw, ch, ad = pick('power'), pick('chips'), pick('adopter')
an = [pick('anchor-' + s)[0] for s in ('transport', 'financials', 'consumer', 'defence')]
TEAMS = {
    'Option D (13 Oct plan)': ({'VST': 12, 'CEG': 9, 'NVDA': 9, 'TSM': 9, 'GOOGL': 8}, {'UBER': 5, 'NU': 4}),
    'Battle winners, literal': ({pw[0]: 12, pw[1]: 9, ch[0]: 9, ch[1]: 9, ad[0]: 8}, {an[0]: 5, an[1]: 4}),
    'Recommended (see the write-up)': ({'VST': 12, 'NEE': 9, 'NVDA': 9, 'TSM': 9, 'GOOGL': 8}, {'UNP': 5, 'V': 4}),
    'Recommended + MU instead of TSM': ({'VST': 12, 'NEE': 9, 'NVDA': 9, 'MU': 9, 'GOOGL': 8}, {'UNP': 5, 'V': 4}),
    'Option D core + new anchors': ({'VST': 12, 'CEG': 9, 'NVDA': 9, 'TSM': 9, 'GOOGL': 8}, {'UNP': 5, 'V': 4}),
    'Recommended core + old anchors': ({'VST': 12, 'NEE': 9, 'NVDA': 9, 'TSM': 9, 'GOOGL': 8}, {'UBER': 5, 'NU': 4}),
}

# ---------- output ----------
def fmt(x, d=1):
    return '–' if x is None or (isinstance(x, float) and np.isnan(x)) else f'{x:.{d}f}'

print(f'Window: {dates[0]} .. {dates[-1]} ({n} weekly returns). QQQ worst-10 average {ST["QQQ"]["worst10"]:.1f}%, '
      f'QQQ P(DD>=20% in 26w, demeaned) {ST["QQQ"]["p_dd20"]:.1f}%, QQQ vol {ST["QQQ"]["vol"]:.0f}%\n')
print('## Per-name statistics')
print('| Name | 1y ret | Vol | Beta | Corr NVDA | Worst-10 | Max DD | Rate %/pt (t) | Fit | P(DD≥20%, 26w) | 5th pct 26w | Fwd P/E | Rev growth | Net margin |')
print('|---|---|---|---|---|---|---|---|---|---|---|---|---|---|')
for t in NAMES:
    s = ST[t]; f = F[t]
    print(f"| {t} | {fmt(s['ret1y'])} | {fmt(s['vol'],0)} | {fmt(s['beta'],2)} | {fmt(s['corrN'],2)} | {fmt(s['worst10'])} | {fmt(s['maxdd'])} | "
          f"{fmt(s['rate'])} ({fmt(s['rate_t'])}) | {fmt(s['fit'],2)} | {fmt(s['p_dd20'],0)}% | {fmt(s['q05_26w'])} | "
          f"{fmt(f['fwd_pe'])} | {fmt(f['rev_growth_ttm_pct'])} | {fmt(f['net_margin'])} |")

print('\n## Pairwise correlations of interest')
for a, b2 in [('VST', 'CEG'), ('VST', 'NEE'), ('CEG', 'NEE'), ('VST', 'TLN'), ('VST', 'NRG'), ('NVDA', 'TSM'), ('NVDA', 'MU'), ('TSM', 'MU'),
              ('NVDA', 'AVGO'), ('GOOGL', 'META'), ('UNP', 'UBER'), ('JPM', 'V'), ('COST', 'MCD'), ('LMT', 'BWXT'), ('BWXT', 'VST')]:
    print(f'{a}-{b2}: {np.corrcoef(R[a], R[b2])[0, 1]:.2f}', end='   ')
print()

for name, b in BATTLES.items():
    table, num, full, passes = RESULTS[name]
    labels = [c[0] for c in b['criteria']] + ([b['manual'][0]] if b['manual'] else [])
    weights = [c[1] for c in b['criteria']] + ([b['manual'][1]] if b['manual'] else [])
    print(f'\n## Battle: {name}  (slots: {b["slots"]})')
    print('| Name | ' + ' | '.join(f'{l} ({w})' for l, w in zip(labels, weights)) + ' | Numbers only | Total | Anchor test | P(wins slot) |')
    print('|---|' + '---|' * (len(labels) + 4))
    for t in sorted(b['names'], key=lambda t: -full[t]):
        cells = []
        for l in labels:
            v, s = table[t][l]
            cells.append(f'{fmt(v, 2 if abs(v) < 10 else 1)} → {s:.1f}')
        at = anchor_test(t, ST) if name.startswith('anchor') else None
        at_s = '' if at is None else ('pass' if all(at.values()) else 'FAIL (' + ', '.join(k for k, v in at.items() if not v) + ')')
        if at is not None:
            at_s += f' · passes in {100 * PASS[t] / B:.0f}% of resamples'
        print(f'| {t} | ' + ' | '.join(cells) + f' | {num[t]:.1f} | **{full[t]:.1f}** | {at_s} | {100 * WIN[name][t] / B:.0f}% |')
    print('Winners (numbers + judgment):', pick(name, True), ' numbers only:', pick(name, False))

print('\n## Teams (January-stage book: core 47% + anchors 9% + XLVP 12 + VUKG 6 + cash 26)')
print('| Team | Core | Anchors | Vol | Beta | Worst-10 | Max DD | 1y ret | Rate %/pt | QQQ −25% | NVDA −40% | +50bp & QQQ −5% | QQQ +20% | P(DD≥10%) | P(DD≥15%) | 5th pct 26w |')
print('|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|')
TEAM_OUT = {}
for label, (core, anchors) in TEAMS.items():
    wts = dict(core); wts.update(anchors); wts.update(ETF)
    d = team_desc(wts); mc = team_sim(wts, True); mcd = team_sim(wts, False)
    TEAM_OUT[label] = dict(core=core, anchors=anchors, desc=d, mc=mc, mc_with_drift=mcd)
    cs = ', '.join(f'{t} {w}' for t, w in core.items()); As = ', '.join(f'{t} {w}' for t, w in anchors.items())
    print(f"| {label} | {cs} | {As} | {d['vol']:.1f} | {d['beta']:.2f} | {d['worst10']:.1f} | {d['maxdd']:.1f} | {d['ret1y']:+.1f} | {d['rate']:.1f} | "
          f"{d['qqq_m25']:+.1f} | {d['nvda_m40']:+.1f} | {d['rate_shock']:+.1f} | {d['qqq_p20']:+.1f} | "
          f"{mc['p_dd10']:.0f}% | {mc['p_dd15']:.0f}% | {mc['q05']:+.1f} |")
print("\nWith last year's drift left in (NOT a forecast; shown only to make the point that it flatters last year's winners):")
for label, o in TEAM_OUT.items():
    m = o['mc_with_drift']
    print(f"  {label}: P(DD>=15%) {m['p_dd15']:.0f}%, 5th pct {m['q05']:+.1f}%, median {m['med']:+.1f}%")

json.dump({'stats': ST, 'battles': {k: {'num': v[1], 'full': v[2], 'passes': v[3], 'win_prob': {t: WIN[k][t] / B for t in WIN[k]}}
                                     for k, v in RESULTS.items()},
           'anchor_test_pass_rate': {t: PASS[t] / B for t in NAMES}, 'teams': TEAM_OUT, 'resamples': B},
          open(ROOT / 'analysis' / 'slot_battles_output.json', 'w'), default=float, indent=1)
