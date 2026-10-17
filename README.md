# Investment Journal

A dated public record of how I invest: the framework, every thesis, every weekly review, every closed trade (wins **and** losses), and the code I use to test ideas.

I'm a BA (Hons) Esports International Business & Digital Media student and former retail duty manager. I run a concentrated long-only portfolio focused on the physical bottlenecks of AI (power, chips, compute) inside UK Stocks & Shares ISAs. This repo exists so my decisions can be checked against what actually happened. Git timestamps every commit, so nothing here can be quietly rewritten after the fact.

> **Not financial advice.** This is a personal journal of my own decisions. Nothing here is a recommendation to buy or sell anything.

**Connect:** [LinkedIn](https://www.linkedin.com/in/james-medeiros-uk)

---

## Repo map

| Folder | What's in it |
|---|---|
| [`theses/`](theses/) | One page per holding: why I own it, what would make me sell, target size |
| [`weekly-reviews/`](weekly-reviews/) | Every Wednesday: prices verified, weights, news, gates, decisions |
| [`trades/`](trades/) | Swing-trade log: entry reason, stop, target, exit, result |
| [`plans/`](plans/) | Decisions committed in advance, e.g. what I'll do in a market drawdown |
| [`post-mortems/`](post-mortems/) | What I got wrong and what changed in my process because of it |
| [`backtests/`](backtests/) | Python tests of trading rules, run on real price data with fees included |
| [`analysis/`](analysis/) | Scripts that turn broker statements into the trade history |
| [`data/`](data/) | Price data used by the backtests |

---

## The framework

### 1. Core thesis
AI needs **physical** inputs that can't be scaled overnight: electricity (especially firm nuclear power), leading-edge chips, and data-centre compute. I try to own the bottlenecks rather than guess which AI application wins.

### 2. Position limits

| Rule | Limit |
|---|---|
| Any single stock | 20% max |
| Energy / nuclear sleeve | 35% max |
| Neocloud sleeve | 15% max |
| Non-AI anchor sleeve | 15% max, 3 names (20% / 4 names once the anchors earn it) |
| Frenzy / speculative bucket | 10% max |
| **Cash shield** | **15% floor** — no new offensive buys until it's restored |

### 3. Defensive layer
- **Cash shield (15%)** is dry powder for drawdowns. It's triggered by index falls of 15%+ or core holdings down 30%+ with the thesis intact.
- **Uncorrelated sleeve:** a health-care ETF (XLVP) and a FTSE 100 tracker (VUKG), chosen for near-zero tech weight.
- **Emergency fund** is kept outside the portfolio, so life events never force a sale at the bottom.

### 4. Buying gates
A stock on the watchlist is only bought when its gate is met, usually a specific earnings print or price level, written down **before** the event.

### 5. Swing-trade sleeve
- Max ~1% of the book at risk per trade, with a hard stop placed as a real order.
- Pre-set take-profit target and a one-month time stop.
- No holding through earnings.
- Every trade logged in [`trades/`](trades/) before entry. The sleeve only scales up if 20+ logged trades show an edge **after fees**.

### 6. Weekly process (every Wednesday) · [checklist](weekly-reviews/_checklist.md)
1. Verify every price and recompute weights; no estimates.
2. Check news, valuation, dilution and gate status for each holding and watchlist name.
3. Check every limit in the table above.
4. Write the review and commit it.

---

## Current snapshot (weights only)

See the latest file in [`weekly-reviews/`](weekly-reviews/).

## Track record
- [**127 round trips across 3 accounts, May 2024 – Oct 2026**](trades/track-record.md): backfilled from official broker statements. 54% win rate, average win +15.6% vs average loss −10.5%. The clearest finding: **the longer I hold, the better I do.** Trades held over 3 months won 71% of the time and averaged +15.3%. Trades held a week or less averaged a loss.
- [**Risk-adjusted ranking**](plans/2026-10-17-risk-adjusted-ranking.md): the plan names ranked as buys by Sharpe, Sortino, reward-to-risk and PEG, refreshed weekly.
- [**Conviction slot: NBIS vs IREN**](plans/2026-10-16-conviction-slot-nbis-vs-iren.md): the two neoclouds tested head to head for the 5% conviction slot (contracts, purity, profitability, cost of debt, dilution, valuation, price).
- [**Capture zones**](plans/capture-zones.md): each name's own support, capitulation and ceiling levels from its price history, with forward P/E and touch odds at each level; re-mapped every Wednesday.
- [**Predictions log**](predictions.md): price calls written down before the outcome, each with a deadline and the base rate it has to beat.
- [**My picks vs the plan**](shadow-portfolio.md): a paper race from 15 Oct 2026 between ten stocks I picked on instinct and the rules-based plan, updated every Wednesday, judged at one year.
- [**Post-mortem: IONQ**](post-mortems/2026-IONQ.md): same stock, same crash, two accounts, opposite results, and the rules it created.

## Plans committed in advance
- [**Concentration plan (10 Oct 2026)**](plans/2026-10-10-concentration-plan.md): moving to 5 core AI-bottleneck names, a defensive layer and a small sandbox, and selling the off-thesis tail.
- [**Decision prepared for 14 Oct**](plans/2026-10-14-decision-googl.md): should Alphabet replace VST or CEG in the core, or should the core become power-led? Five options, a [full comparison with stress tests](plans/2026-10-13-abcd-comparison.md), and [**slot battles**](plans/2026-10-13-slot-battles.md): every planned holding against the best alternatives in its sector, scored by a written rubric with win probabilities from 1,000 resampled years, plus the [limit orders](trades/limit-orders-2026-10-14.md) drafted for the exits.
- [**Target portfolio**](plans/target-portfolio.md): where the book ends up once every plan is carried out.
- [**Adaptive rules**](plans/adaptive-rules.md): the five triggers that are allowed to change the targets, the speed limits, and a log of every change.
- [**Watch items**](plans/watch-items.md): Terafab and other developments that could change a thesis.
- [**Drawdown plan (10 Oct 2026)**](plans/2026-10-10-drawdown-plan.md): the triggers, tranches and buy list I'll follow if the Nasdaq-100 falls 15%, 25% or 35%, written before any fall.

## Projects
- [**Pairs tilt backtest: VST vs CEG**](backtests/) — can tilting between two near-identical nuclear stocks beat holding both 50/50? (Short answer so far: not reliably.)
