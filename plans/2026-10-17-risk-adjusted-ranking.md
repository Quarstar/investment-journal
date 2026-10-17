# Risk-adjusted ranking · the plan names as buys · 17 Oct 2026

Which names give the most upside per unit of risk? Four measures, each ranked, then the average rank. Script: [`analysis/risk_adjusted_ranking.py`](../analysis/risk_adjusted_ranking.py); refreshed with the Wednesday review.

> Personal record, not financial advice.

**The measures**
- **Sharpe:** (expected return − 5% cash rate) ÷ volatility. Penalises all movement, up and down.
- **Sortino:** the same, but divided by downside deviation only (weeks below zero). Closer to what "risk" means to a holder.
- **Reward ÷ risk:** expected upside ÷ the 5th-percentile 26-week return from the block bootstrap (the bad half-year). A trader's "3-to-1".
- **PEG:** forward P/E ÷ net-income growth. Growth per unit of price, not per unit of risk. Below 1 reads as cheap for the growth. Loss-makers and negative growth: n/a.

**Expected return** is the consensus 12-month target against the price, so it carries the analysts' optimism; the bias is the same for every name, so the ranking survives it, the absolute numbers don't. Prices: 15 Oct closes. Volatility and downside deviation: 50 weekly returns to 9 Oct. PEG uses trailing net-income growth because forward growth isn't in the data yet.

## Ranking (15 Oct 2026 closes)

| # | Name | Price | Upside to target | Vol | Downside dev. | Sharpe | Sortino | Reward÷risk (5th pct 26w) | Fwd P/E | PEG | Avg rank |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | NVDA | 217.23 | +51% | 33% | 21% | 1.41 (1) | 2.22 (1) | 2.11 (1) | 18.71 | 0.15 (2) | 1.2 |
| 2 | AVGO | 346.25 | +53% | 45% | 30% | 1.08 (3) | 1.64 (3) | 1.65 (2) | 20.47 | 0.20 (3) | 2.8 |
| 3 | TSM | 422.25 | +37% | 28% | 18% | 1.12 (2) | 1.82 (2) | 1.48 (3) | 19.61 | 0.37 (7) | 3.5 |
| 4 | MU | 931.24 | +68% | 71% | 39% | 0.88 (6) | 1.59 (4) | 1.28 (5) | 5.61 | 0.01 (1) | 4.0 |
| 5 | NEE | 78.96 | +23% | 18% | 14% | 0.98 (4) | 1.28 (5) | 1.23 (6) | 19.17 | 0.34 (6) | 5.2 |
| 6 | VST | 154.17 | +36% | 43% | 30% | 0.73 (7) | 1.05 (7) | 1.37 (4) | 15.89 | n/a | 6.0 |
| 7 | MCD | 242.50 | +20% | 16% | 14% | 0.94 (5) | 1.10 (6) | 1.14 (7) | 17.84 | 3.80 (11) | 7.2 |
| 8 | GOOGL | 349.22 | +23% | 33% | 20% | 0.55 (9) | 0.93 (8) | 0.77 (10) | 26.18 | 0.24 (4) | 7.8 |
| 9 | NU | 14.73 | +27% | 41% | 28% | 0.55 (8) | 0.80 (9) | 0.79 (9) | 16.44 | 0.29 (5) | 7.8 |
| 10 | TLN | 358.42 | +29% | 53% | 36% | 0.45 (10) | 0.65 (11) | 0.80 (8) | 12.91 | n/a | 9.7 |
| 11 | UNP | 288.71 | +14% | 21% | 13% | 0.41 (11) | 0.65 (10) | 0.64 (12) | 20.69 | 3.63 (10) | 10.8 |
| 12 | CEG | 279.54 | +22% | 47% | 34% | 0.37 (12) | 0.50 (12) | 0.66 (11) | 24.01 | 1.58 (9) | 11.0 |
| 13 | AMD | 570.82 | +11% | 62% | 37% | 0.10 (13) | 0.18 (13) | 0.22 (13) | 53.51 | 0.42 (8) | 11.8 |

Ranks in brackets. NBIS isn't scored: no earnings, and its target spread ($84–$399) makes "upside" meaningless. After Friday's falls (NVDA $214, AVGO ~$329) the top two move slightly closer together; the order holds.

## Reading it

1. **NVDA is first on every risk-adjusted measure**, and second on PEG only because Micron's cyclical-peak earnings make its PEG look like 0.01. That's the battles' chips verdict from another angle.
2. **AVGO is a clear second**, ahead of TSM on three of four, behind on PEG. Its ratio improved this week because the price fell faster than the targets. It is the best buy *not yet in the book*, which is what the January gate is for.
3. **TSM is the steadiest of the top three**: the lowest volatility and downside deviation of any chip name, so its Sharpe beats AVGO's even with less upside. Growth-per-price (PEG 0.37) is its weak spot.
4. **MU looks cheap on every price measure and is fourth** only because its downside is the worst of the group after AMD. The PEG of 0.01 is the cycle, not a bargain (see the capture-zone page).
5. **NEE beats VST on risk-adjusted terms** (less upside, far less risk) even though VST has the bigger target. Together they're why the power pair is built as merchant first, regulated second.
6. **The anchors (MCD, UNP, NU) score low here by design**: anchors are bought for what they do in bad weeks, not for upside. UNP's PEG of 3.6 and MCD's 3.8 are the price of durability. This table is a buy ranking, not a build.
7. **CEG and AMD are last.** CEG's 24× forward P/E and 47% volatility for 22% upside is exactly why it's being swapped for NEE; AMD at 54× with 11% upside has the worst ratio in the set.

**What this does and doesn't change:** nothing in the targets. The gates and the shield floor still decide *when*; this table decides *which first* when two buys are ready at the same time: NVDA/AVGO over TSM over MU for chip money, NEE over VST for power money, and it argues for keeping AVGO's January gate rather than skipping it.

## Caveats
- Analyst targets lag: after a 20% fall the "upside" inflates before the targets are cut, which flatters whatever fell last. AVGO had two target cuts this week (TD Cowen, Morgan Stanley) that aren't in the 13 Oct snapshot.
- One year of weekly data, a strong year for chips: volatility is understated for the next bear market, equally for all names.
- Trailing earnings growth is used for PEG; forward growth would move MU, NVDA and AVGO down the growth scale as comparisons get harder.
