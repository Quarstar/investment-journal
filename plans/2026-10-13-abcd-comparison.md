# A vs B vs C vs D: the comparison, written before the 14 Oct review

> Written 13 Oct 2026, evening, with prices and news verified that afternoon (US market open). This is the analysis. The decision itself is recorded on the [decision page](2026-10-14-decision-googl.md) at the review. The number-crunching script is [`analysis/options_abcd.py`](../analysis/options_abcd.py).

## The four options

All four keep the core at **47% of the book**, the risk-down level set on 12 Oct.

| Weight in the book | **A** Keep | **B** GOOGL for VST | **C** GOOGL for CEG | **D** Power-led |
|---|---|---|---|---|
| NVDA | 10.5 | 10.5 | 10.5 | 9 |
| TSM | 10.5 | 10.5 | 10.5 | 9 |
| VST | 10 | – | 10 | **12** |
| CEG | 10 | 10 | – | **9** |
| GOOGL | – | 10 | 10 | 8 |
| NBIS | 6 | 6 | 6 | **0** |
| Electricity in the core | 20 | 10 | 10 | 21 |
| Chips | 21 | 21 | 21 | 18 |
| Adopter | 0 | 10 | 10 | 8 |

## What I verified on 13 Oct

| | Price | Forward P/E | Beta, 1 yr weekly vs Nasdaq-100 | Beta, 5 yr (StockAnalysis) | Off 52-week high | Next results |
|---|---|---|---|---|---|---|
| NVDA | $229.28 (9 Oct close) | 19.0× | 1.17 | 2.22 | −6% | ~18 Nov |
| TSM | $453.31 (9 Oct close) | 20.3× | 0.87 | 1.25 | −7% | **15 Oct** |
| VST | $162.23 | **15.9×** | **0.30** | 1.38 | −25% | 6 Nov |
| CEG | $297.25 | 24.0× | 0.59 | 1.13 | −28% | 9 Nov |
| GOOGL | $354.76 | 26.2× | 0.99 | 1.21 | −13% | **28 Oct** |
| NBIS | $207.00 | n/a (P/E ~1,259; ~42× sales) | **2.27** | 1.46 | −31% | 10 Nov |

News that matters for the choice:
- **CEG:** 6 Oct, 20-year deal with Google for 890 MW of nuclear uprates at 11 PJM units, worth over $4.3B, first power by 2028. Stock rose 12–14% that day. Cleared 18,875 MW in July's PJM capacity auction, about $2.2B of capacity revenue for 2028/29. 2026 EPS guidance of $11–12 was below the $12.11 consensus when given.
- **VST:** 3–5 Oct, US government to lend $4.2B to upgrade its nuclear plants. Cleared 10,924 MW in the auction, about $1.3B. 2025 revenue grew only 3% and EPS fell 69% on one-off hedge and acquisition accounting; analysts expect 2026 EPS to more than quadruple, then 2027 EPS growth of about 8%. The 15.9× forward multiple sits on that rebound year.
- **GOOGL:** Q2 (22 Jul) revenue +24% to $119.8B, Google Cloud +82% to $24.8B, cloud backlog $514B. Capex $44.9B in the quarter and 2026 capex guidance **raised to $195–205B**, which pushed free cash flow to −$5.9B. The stock fell 5–6% on the capex, not the revenue. Gemini 4 launched today. Results 28 Oct.
- **NBIS:** revenue +507% to $1.36B trailing. COO sold 500,000 shares (~$118M) on 5 Oct under a pre-set plan. Down ~5.8% on 12 Oct with the neocloud sector after the OpenAI revenue report. Results 10 Nov.
- **Rates:** the US 10-year yield was **5.24%** on 9 Oct against 4.05% a year earlier, a rise of about 120 basis points, most of it since May and 50bp of it in September alone. The Fed raised rates in September. Brent crude is above $106.

## 1. What each core did over the past year

Weekly closes, 10 Oct 2025 to 9 Oct 2026, at the weights above and rebalanced weekly. Rate sensitivity is from a regression of each week's return on the Nasdaq-100's return and the change in the 10-year yield, so it's the move *after* the market effect is removed.

| Core | Volatility | Beta vs Nasdaq-100 | Corr. with NVDA | Nasdaq's 10 worst weeks (index −3.1%) | Max drawdown | Avg correlation between the 5 names | Rate sensitivity (per +1.00pt on the 10-year) | Past-year return (hindsight) |
|---|---|---|---|---|---|---|---|---|
| **A** | 29% | 0.93 | 0.51 | −4.0% | −14.1% | 0.29 | −5.7% | +23.8% |
| **B** | 26% | 1.08 | 0.65 | −4.0% | −12.0% | 0.21 | +0.5% | +40.7% |
| **C** | 26% | 1.02 | 0.62 | −3.8% | −11.4% | 0.21 | +0.4% | +40.6% |
| **D** | **23%** | **0.75** | **0.44** | **−3.0%** | **−10.3%** | **0.19** | **−9.6%** | +16.9% |

Nasdaq-100 over the same year: +27.4%.

**What the table says.** D is the least volatile, least market-sensitive, least NVDA-sensitive and least internally correlated of the four, and it had the smallest drawdown. It is also the only one with a meaningful **rate** sensitivity, and it would have earned the least over a year in which the Nasdaq rose 27% and the power names fell. Those two facts are the whole trade-off.

The last column is hindsight. It mostly measures that VST and CEG had a bad year and GOOGL a good one. It is not a reason to pick B or C, but it is a reminder that D's low beta came partly from the power names *falling while the market rose*, which is not the same as holding value.

## 2. Stress tests

Beta-implied, for the whole book at the January weights (core 47%, cash 25%, XLVP 12%, VUKG 6%, UBER 5%, NU 4%, sandbox 1%). Betas are the past year's weekly betas, so these are rough.

| Scenario | A | B | C | D |
|---|---|---|---|---|
| Nasdaq-100 −15% (drawdown trigger 1) | −7.4% | −8.4% | −8.0% | **−6.1%** |
| Nasdaq-100 −25% (trigger 2) | −12.3% | −14.0% | −13.3% | **−10.1%** |
| Nasdaq-100 −35% (trigger 3) | −17.2% | −19.6% | −18.6% | **−14.2%** |
| AI-specific bust: NVDA −40%, every other name moves by its past-year beta to NVDA | −8.5% | −9.7% | −9.2% | **−5.6%** |
| Rate shock: 10-year +50bp and Nasdaq-100 −5% | −3.8% | −2.7% | **−2.6%** | −4.3% |
| Boom continues: Nasdaq-100 +20% | +9.8% | **+11.2%** | +10.7% | +8.1% |

In the AI-specific bust, NBIS alone costs options A, B and C about 2.8% of the book (6% weight × a 1.18 beta to NVDA × −40%).

## 3. The rates problem

This is the one place D is clearly worse, so it needs the most honest treatment.

- Over the past year, after removing the market's effect, **VST moved about −26% for every +1.00pt on the 10-year yield, and CEG about −26%** too. Both estimates are statistically meaningful (t-statistics of −2.8 and −2.5 on 52 weekly observations). NVDA, TSM and GOOGL show no reliable rate sensitivity.
- The 10-year rose 1.19 points over the year. The regression attributes essentially the **whole** of VST's and CEG's decline to that rise. Put differently: for the past year, VST and CEG traded like long-dated bonds with a nuclear plant attached.
- In D, the core's rate sensitivity is −9.6% per +1.00pt, about −4.5% of the book. In C it is roughly zero.
- The backdrop is the wrong way: a hike in September, another signalled, oil above $106 feeding inflation worries, and the 10-year at its highest since 2002.

Two caveats cut the other way. First, yields rose and power stocks fell steadily through the same months, so some of this is two trends overlapping rather than week-by-week cause and effect; it also coincided with the PJM price cap and the "AI premium" leaving the sector. Second, the 5-year betas (VST 1.38, CEG 1.13) say these were high-beta stocks in 2023–25. The past-year numbers describe a stock that has already de-rated, not a permanently defensive one.

## 4. The electricity thesis: what's true and what's capped

**True, and getting stronger**
- EIA (6 Oct 2026) expects record US electricity consumption in both 2026 and 2027: 4,195 billion kWh in 2025 to 4,356 in 2027, +3.8% in two years, after two decades of roughly flat demand. Drivers: data centres, reshored manufacturing, electrified transport and heating.
- A 2026 DOE study puts data centres at about 192 TWh in 2024, 4.7% of US electricity, rising to 9.5–15.3% by 2030.
- PJM, the grid VST and CEG mostly sell into, is about 6.8 GW short of its reserve target and only 525 MW of new supply cleared in July's auction. Scarcity is real.
- The contracts are real: CEG with Google (890 MW uprates, $4.3B+) and Amazon; VST with AWS (1,200 MW), Meta (2,609 MW), the Helix venture (Nvidia, KKR, KIA), New Era, plus the $4.2B DoE loan.

**Capped, and politically exposed**
- PJM's capacity price is capped at **$325/MW-day** by a collar agreed with the states. July's auction hit the cap; without it the price would have been about **$555** (and $777 in Chicago). The collar has been extended through the 2029/30 auction, so the scarcity *windfall* is off the table for several years. VST and CEG get a good price, not the full price.
- The House passed the **Ratepayer Protection Act 417–3** on 16 Sep, pushing states to make large loads pay for new generation. New York has paused data-centre permits partly over bills. PJM's market monitor estimates data centres added $29.4B to capacity costs over four auctions. The political direction is to shift costs onto data centres and limit windfalls to generators.
- FERC on 9 Oct rejected most of PJM's large-load plan on jurisdiction grounds (5–0). Jefferies read that as keeping capacity prices "higher for longer", which helps existing generators, but it also means the rules for selling directly to co-located data centres are still unwritten.
- VST and CEG have already lost their "AI premium" once: VST went from ~23× earnings at its September 2025 peak to ~15×; CEG from ~40× to ~24×. That's why they're cheaper. It is also what happens to a power stock when the market stops treating it as an AI stock.

**Net:** the demand side of the thesis is as strong as it looks. The *pricing* side is politically capped. That argues for owning the power names on contracted revenue and a fair multiple, not on scarcity pricing, which is exactly where VST (15.9×) sits and where CEG (24×) partly doesn't.

## 5. Option by option

**A. Keep NVDA, TSM, VST, CEG, NBIS.** Middle of the pack on every risk measure and the worst fit with the rules written on 12 Oct: no adopter in the core, and the only name it keeps that isn't a supplier is none. It was the default if nothing else could be decided. It shouldn't win on its merits.

**B. GOOGL replaces VST.** Sells the cheapest, lowest-beta, best-contracted name in the core and keeps the pricier of the two power names. Highest beta of the four (1.08). Highest return in hindsight, which is the only thing going for it. Reject.

**C. GOOGL replaces CEG.** The sensible middle option. No rate bet, full chip weight, the adopter at 10%, VST kept, NBIS small. It also has the second-highest beta (1.02) and keeps NBIS, which is the single largest risk in the book: 93% volatility, a 2.27 beta, ~42× sales, and insiders selling. And it sells CEG a week after CEG signed the most direct hyperscaler nuclear contracts in the market. If the thesis is electricity, C leaves 10% of the book in it.

**D. Power-led, NBIS out.** Lowest equity risk by every measure, best in both crash scenarios, best fit with the 12 Oct rule that cuts come from suppliers (NBIS is the purest build-out supplier in the book), and the only option that matches the thesis as now stated. Its costs: a concentrated rate bet (21% in two names that moved −26% per point of yield), two names that are 0.75 correlated, a capped upside, and the lowest payoff if the AI build-out simply keeps going. It also gives up NBIS, the best-performing position in the track record, and re-entry would need a core slot.

## 6. Scorecard

Scored 1 (worst) to 5 (best) on what the numbers above show. Equal weights, because I don't have a good reason to weight them otherwise.

| | A | B | C | D |
|---|---|---|---|---|
| Loss in a general crash | 3 | 1 | 2 | 5 |
| Loss in an AI-specific bust | 3 | 1 | 2 | 5 |
| Rate risk | 3 | 5 | 5 | 1 |
| Gain if the boom continues | 3 | 5 | 4 | 2 |
| One-bet risk inside the core | 2 | 3 | 4 | 3 |
| Valuation of what's held | 3 | 2 | 3 | 4 |
| Fit with the written rules (adopter, supplier cut, caps) | 1 | 3 | 4 | 5 |
| Execution (trades, tax, timing) | 5 | 2 | 3 | 3 |
| **Total** | **23** | **22** | **27** | **28** |

Close between C and D. The scorecard is there to make the reasoning visible, not to decide; a different weighting on rates would flip it. What decides it is section 7.

## 7. My pick: D, with three conditions

**Why D over C.** The portfolio was cut to 47% core on 12 Oct because there is no income coming in and the book should take less risk. D takes the most risk out of the thing most likely to hurt it, an AI-driven sell-off: about 3 points of the book less damage than C at trigger 2, and about 3.5 points less in an AI-specific bust. The risk D adds instead, rates, is real but it is **one** risk, it is visible every week in one number, and it can be bounded with a rule written now. The NBIS exit is most of D's benefit, and it stands on its own: a 2.27-beta, 42×-sales stock with insiders selling doesn't belong in a book that just chose to carry less risk. And on the thesis: the demand side of electricity is the best-evidenced idea in the whole book, and D is the only option that owns it at a weight that matters.

**Why not C.** C is a good portfolio. It loses because it keeps NBIS, sells the name that just signed Google, and leaves the stated thesis at 10% of the book.

**Condition 1: the GOOGL gate stays.** Buy GOOGL only after its 28 Oct results, and only if Cloud growth stays strong (Q2 was +82%) and the capex guidance isn't raised *again* without matching revenue. Until then the 8% waits in cash.

**Condition 2: NBIS leaves in two halves.** Half on the first green day after the review, half by the 4 Nov review, so the position is closed before its 10 Nov results. That keeps within the adaptive rules' 5%-per-review limit. No averaging into a red day, no waiting for a bounce.

**Condition 3: a rate rule, written before it's needed.**
- The power pair (VST + CEG) is capped at **21%** of the book.
- If the 10-year yield closes **above 5.50% on two consecutive Wednesdays**, the pair's target drops to **16%** (VST 10, CEG 6). New money goes elsewhere first; if a trim is needed, trim CEG first (the pricier one). The freed weight goes to the cash shield or XLVP.
- If VST's rolling one-year beta to the Nasdaq-100 goes above **0.8**, it has started trading as an AI stock again and no longer does the diversification job at 12%; revisit its weight at the next review.
- Sell triggers in the [VST](../theses/VST.md) and CEG thesis pages still apply, including guidance cuts at the 6 Nov and 9 Nov results.

**Housekeeping if D is chosen:** the README's core thesis line changes from "AI bottlenecks" to "electricity is the bottleneck, for AI and for everything else; chips second; one adopter"; the drawdown plan's buy list drops NBIS and adds GOOGL; the target portfolio and factsheet are updated; NOW's path into the core now runs through NVDA or TSM, not NBIS.

## 8. What I'm not sure about
- **One year of weekly data is thin.** 52 observations. The betas and correlations will move; the 5-year betas say VST and CEG can be high-beta stocks.
- **GOOGL is only half an adopter.** It is also the biggest builder, with $195–205B of 2026 capex and negative free cash flow. If AI spending disappoints, its stock will be punished for the spending even if Search and YouTube are fine.
- **Regulation is the open variable** for the power names, and it is moving against windfalls. The thesis survives that; the upside is smaller than the 2024–25 run suggested.
- **The hindsight gap is large.** D would have made 17% last year against 41% for C. If the next year looks like the last one, D is the wrong call. The reason to choose it is that the next year is less likely to look like the last one, and that the book cannot currently afford it if it doesn't.

## Sources
- [StockAnalysis: VST](https://stockanalysis.com/stocks/vst/), [CEG](https://stockanalysis.com/stocks/ceg/), [GOOGL](https://stockanalysis.com/stocks/googl/), [NBIS](https://stockanalysis.com/stocks/nbis/), [NVDA](https://stockanalysis.com/stocks/nvda/), [TSM](https://stockanalysis.com/stocks/tsm/) (prices, multiples, 5-year betas, results dates)
- [US Treasury daily yield curve, 2025 and 2026](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/2026/all?type=daily_treasury_yield_curve&field_tdr_date_value=2026&page&_format=csv) (10-year yields)
- [Utility Dive: PJM capacity auction hits price cap, reserve shortfall grows (15 Jul 2026)](https://www.utilitydive.com/news/pjm-capacity-auction-price-cap-reserve-shortfall/825282/)
- [Energy News Beat: FERC rejects most of PJM's data-centre plan (Oct 2026)](https://energynewsbeat.co/ai/ferc-rejects-most-of-pjms-data-center-plan-and-the-29-4-billion-question-of-who-pays-is-still-open/)
- [Utility Dive: PJM colocation plan takes fire from Vistra, Constellation (2026)](https://www.utilitydive.com/news/pjm-data-center-colocation-ferc-vistra-constellation/815941/)
- [CBS News: House passes bill to shield Americans from data-centre energy costs (16 Sep 2026)](https://www.cbsnews.com/news/house-bill-data-center-energy-costs/)
- [AI Weekly: Alphabet Q2 2026, Cloud +82%, capex $44.9B](https://aiweekly.co/alerts/alphabet-q2-cloud-jumps-82-to-248b-capex-hits-449b)
- [EIA via roic.ai: US power demand to hit record highs (6 Oct 2026)](https://www.roic.ai/news/us-power-demand-to-hit-record-highs-on-ai-boom-eia-says-10-06-2026)
- [Motley Fool: Vistra is down 30% from its high (8 Sep 2026)](https://www.fool.com/investing/2026/09/08/vistra-is-down-30-from-its-high-heres-what-id-do/)
- [Motley Fool via Yahoo: Constellation down 28% (16 Apr 2026)](https://finance.yahoo.com/markets/stocks/articles/constellation-energy-down-28-52-124000776.html)
- [Investing.com: Why is Nebius sliding (12 Oct 2026)](https://www.investing.com/news/stock-market-news/why-is-nebius-stock-sliding-today-93CH-4944863)
