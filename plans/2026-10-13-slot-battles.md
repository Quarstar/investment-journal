# Slot battles: every planned holding against the best alternatives in its sector · 13 Oct 2026

Written the day before the 14 Oct review, after the [A/B/C/D comparison](2026-10-13-abcd-comparison.md). That comparison chose a shape for the core (Option D, power-led). This page asks the next question: **is each name in the plan the best name for its slot?** Every slot is contested by the alternatives in the same sector, with the same data and the same rules, and the result is the best list I can build from statistics and probability rather than from attachment to what I already own.

Script: [`analysis/slot_battles.py`](../analysis/slot_battles.py). Data: [`data/weekly_closes_battles_2025-10-24_to_2026-10-09.csv`](../data/weekly_closes_battles_2025-10-24_to_2026-10-09.csv) and [`data/fundamentals_2026-10-13.csv`](../data/fundamentals_2026-10-13.csv). Every number below comes from that script; anyone can re-run it.

> Personal record, not financial advice. RTX was meant to be in the defence battle; its price-history page could not be read (rate-limited), so it is left out rather than guessed.

---

## 1. The short answer

| Slot | Plan (Option D) | Battle winner | Win probability* | My pick | Change? |
|---|---|---|---|---|---|
| Power 1 (12%) | VST | DUK (regulated utilities added 21:40; see §5) | 94% (NEE 51%, SO 43%) | **VST** (thesis leader; wins the merchant-generator sub-battle) | No |
| Power 2 (9%) | CEG | NEE / DUK | NEE 51% on the base rubric, 47% on the growth tilt (DUK 94% / 13%) | **NEE** replaces CEG; DUK is the alternate | **Yes** |
| Chips 1 (9%) | NVDA | NVDA | 99% | **NVDA** | No |
| Chips 2 (9%) | TSM | MU | 69% (TSM 31%) | **TSM** (MU to the sandbox only; see §4) | No |
| Adopter (8%) | GOOGL | GOOGL | 86% | **GOOGL** | No |
| Anchor: transport | UBER | UNP | 99% | **UNP** replaces UBER | **Yes** |
| Anchor: financials | NU | V | 64% (JPM 33%) | **V** replaces NU (NU wins the growth tilt; see §11) | **Yes** |
| Anchor: consumer | MCD | COST | 48% (MCD 42%) | **MCD** (tie-break: cheaper; see §7) | No |
| Anchor: defence | BWXT | LMT | 83% | **LMT** replaces BWXT, which **fails the anchor test** | **Yes** |

\* Share of 1,000 runs in which the name wins the slot, where each run resamples the past year's weeks (so every statistic moves) **and** randomly perturbs the rubric weights (so the result doesn't depend on my exact weighting). Method in §3. Monte Carlo figures move by a point or two between runs; the script's seed reproduces these exactly.

A growth-tilted version of every battle, run the same evening after the question "is this the most optimised for growth?", is in §11. It changes one slot (NU for V) and otherwise confirms the list.

**The battle list (Option E):**

| Layer | Holding | Weight (Jan 2027) | End state | Gate before buying |
|---|---|---|---|---|
| Core power | VST | 12% | 12% | held |
| Core power | **NEE** | 9% | 9% | Q3 results 21 Oct; buy as CEG is sold, one out, one in |
| Core chips | NVDA | 9% | 9% | held |
| Core chips | TSM | 9% | 9% | Q3 results 15 Oct (top-up gate) |
| Core adopter | GOOGL | 8% | 8% | Q3 results 28 Oct |
| Anchor | **UNP** | 5% | 6% | Q3 results 22 Oct |
| Anchor | **V** | 4% | 5% | Q4 FY results 27 Oct |
| Anchor | MCD | – | 4% | Q3 results 4 Nov; third anchor |
| Anchor | **LMT** | – | 4% | Q3 results 22 Oct; fourth anchor, once the switch triggers |
| Defensive | Cash shield | 25% | 15% | – |
| Defensive | XLVP | 12% | 12% | – |
| Defensive | VUKG | 6% | 6% | – |
| Sandbox | swing trades (IREN now) | 1% | 1% | ≤ 2% if MU or TLN is added as a cycle trade |

Four of nine slots change. The core keeps its power-led shape (VST + NEE = 21%, the largest sleeve) and its three other names. The anchor sleeve changes the most, because the rubric for anchors rewards exactly one thing: holding up when the Nasdaq doesn't, and UBER, NU and BWXT are growth stocks sitting in defensive seats.

**What it does to the book (January-stage weights, same simulation for every team):**

| Team | Vol | Beta | Worst-10 | QQQ −25% | NVDA −40% | +50bp & QQQ −5% | QQQ +20% | P(10%+ fall in 26 wks) | 5th-pct 26-wk return |
|---|---|---|---|---|---|---|---|---|---|
| Option D (VST 12, CEG 9, NVDA 9, TSM 9, GOOGL 8 · UBER 5, NU 4) | 12.0% | 0.38 | −1.4% | −9.5% | −5.8% | −1.7% | +7.6% | 12% | −8.6% |
| **Option E, the battle list** (VST 12, NEE 9, NVDA 9, TSM 9, GOOGL 8 · UNP 5, V 4) | **8.7%** | **0.25** | **−0.8%** | **−6.2%** | **−4.4%** | **−1.1%** | +4.9% | **6%** | **−7.1%** |
| Literal rubric winners (NEE 12, VST 9, NVDA 9, MU 9, GOOGL 8 · UNP 5, JPM 4) | 10.7% | 0.37 | −0.9% | −9.3% | −6.2% | −1.7% | +7.5% | 11% | −8.5% |
| Option E with MU instead of TSM | 11.1% | 0.39 | −1.0% | −9.7% | −6.0% | −1.8% | +7.7% | 12% | −8.6% |
| Option D core + the new anchors | 10.8% | 0.32 | −1.0% | −7.9% | −5.0% | −1.4% | +6.3% | 10% | −8.1% |
| Option E core + the old anchors | 9.7% | 0.31 | −1.1% | −7.8% | −5.3% | −1.4% | +6.2% | 7% | −7.5% |
| Literal rubric winners after the utilities were added (DUK 12, NEE 9, NVDA 9, MU 9, GOOGL 8 · UNP 5, JPM 4) | 9.3% | 0.32 | −0.7% | −8.1% | −5.7% | −1.5% | +6.4% | 7% | −8.0% |
| Growth tilt, literal winners (NRG 12, NEE 9, NVDA 9, MU 9, GOOGL 8 · UBER 5, NU 4) | 12.8% | 0.41 | −1.3% | −10.3% | −6.6% | −1.9% | +8.2% | 19% | −9.2% |
| **Option G** = E with NU for V (§11) | 9.4% | 0.26 | −0.8% | −6.6% | −4.7% | −1.2% | +5.3% | 8% | −7.5% |
| **Option G+** = G with cash at the 15% floor and the core at 55% (after a job; §11) | 10.8% | 0.33 | −1.1% | −8.3% | −6.0% | −1.5% | +6.6% | 13% | −8.7% |

Option E cuts the book's risk by a quarter to a third on every measure (volatility 12.0% → 8.7%, a Nasdaq −25% costs 6.2% instead of 9.5%, the chance of a 10%+ fall inside six months halves) and gives up about a third of the upside in a +20% Nasdaq year (+4.9% vs +7.6%). Most of that comes from one swap, NEE for CEG; the anchors add the rest. For a book with no wage behind it until January, that is the trade I want.

---

## 2. Rules of the battle

1. **Same data for everyone.** 51 Friday closes (24 Oct 2025 → 9 Oct 2026) from stockanalysis.com for 35 stocks, QQQ and the 10-year Treasury yield; the current (unfinished) week is excluded. Fundamentals are one snapshot of the stockanalysis.com quote pages, taken 13 Oct 2026 during US hours.
2. **Same statistics for everyone**, on 50 weekly log returns: annualised volatility; beta and correlation to QQQ; correlation with NVDA; the average return in QQQ's 10 worst weeks of the window ("worst-10"; QQQ itself averaged −3.1%); the deepest fall inside the window; sensitivity to the 10-year yield (% move per +1.00 point, after controlling for QQQ, with its t-statistic); "fit", the average correlation with the *other* roles in the core (lower = better diversifier); and two bootstrap numbers explained in §3.
3. **A rubric per slot, written before the numbers were run.** Each criterion is scored by rank inside the group (best 10, worst 0, linear in between), weighted, and summed to 100. Criteria and weights are in each battle's table. Three slots have one *judgment* criterion (10 points) that I scored by hand before running anything: chips "durability", power "contracts", adopter "purity". Every table shows the total with and without it, so the judgment can be stripped out.
4. **Anchors must pass the anchor test first** (1-year weekly: beta to QQQ < 0.8, correlation with NVDA < 0.5, worst-10 better than QQQ's −3.1%). A name that fails cannot win, whatever its score.
5. **Fundamentals are facts, not forecasts.** Revenue growth and net income are trailing twelve months; forward P/E is the consensus next-twelve-months multiple on the quote page. Where that misleads (memory chips at a cycle peak, see §4) I say so instead of fixing the rubric after the fact.

## 3. Where the probabilities come from

- **P(20%+ drawdown in 26 weeks)**, per name: a stationary block bootstrap (random blocks of weeks, average length 4, 20,000 paths) of the name's own weekly returns **with the past year's average return removed**. Last year's average return is the one thing least likely to repeat; what's left is the size and clustering of the moves. The number says how often a name of that volatility and clustering falls 20% from a high inside six months. QQQ scores 7%.
- **Win probability**, per slot: 1,000 runs. Each run block-bootstraps the year (so beta, worst-10, drawdown, rate sensitivity and fit are all recomputed on a slightly different history) and multiplies every rubric weight by a random factor (log-normal, σ = 0.4, so a weight of 20 usually lands between 13 and 30). The share of runs a name wins is its win probability. A name that wins 98% of runs is a robust winner; 48% vs 44% is a coin flip and I say so.
- **Book-level Monte Carlo**: the same block bootstrap, but one set of draws applied to every holding at once, so correlations survive. Average returns removed. 26-week horizon. Reported as the probability of a 10% or 15% fall from a high, and the 5th-percentile 26-week return.

**The limits.** One year of data. The window had no crash (QQQ's worst fall inside it was about −10%), so the bootstrap cannot produce a 2022 or a 2008; treat every probability as a ranking, not a forecast. Trailing fundamentals flatter cyclicals at the top and punish them at the bottom. The judgment scores are mine and are shown separately for that reason.

---

## 4. Chips: NVDA and TSM vs AVGO, AMD, ASML, MU (two slots)

| Name | Rev growth (20) | Fwd P/E (25) | Net margin (10) | P(DD≥20%) (20) | Worst-10 (10) | Fit (15) | Durability (10, judgment) | Numbers only | **Total** | Win prob |
|---|---|---|---|---|---|---|---|---|---|---|
| NVDA | 83% → 16 | 18.7 → 20 | 64% → 8 | 34% → 16 | −4.7% → 6 | 0.09 → 15 | 8 → 8 | 81 | **89** | 99% |
| MU | 256% → 20 | 5.6 → 25 | 64% → 10 | 93% → 0 | −5.4% → 4 | 0.18 → 9 | 3 → 3 | 68 | **71** | 69% |
| TSM | 31% → 4 | 19.6 → 15 | 50% → 6 | 32% → 20 | −2.4% → 10 | 0.23 → 3 | 10 → 10 | 58 | **68** | 31% |
| AVGO | 49% → 12 | 20.5 → 10 | 43% → 4 | 63% → 8 | −5.9% → 2 | 0.32 → 0 | 8 → 8 | 36 | **44** | 1% |
| ASML | 10% → 0 | 31.7 → 5 | 30% → 2 | 54% → 12 | −2.6% → 8 | 0.18 → 6 | 10 → 10 | 33 | **43** | 0% |
| AMD | 40% → 8 | 53.5 → 0 | 16% → 0 | 90% → 4 | −6.9% → 0 | 0.16 → 12 | 6 → 6 | 24 | **30** | 0% |

**NVDA is the safest slot in the book:** wins 99% of runs. 18.7× forward earnings for 83% growth and a 64% net margin is the cheapest growth in the group; its one weakness is that it *is* the Nasdaq's bad weeks (−4.7%).

**The second slot is MU vs TSM, and the rubric says MU, 69/31.** I'm not taking it, and the reason is written down so it can be judged later. MU's win comes entirely from two numbers, a 5.6× forward P/E and +256% trailing revenue growth, and both are what memory looks like at the top of its cycle: a surge in memory prices makes trailing growth enormous, and the market pays a single-digit multiple precisely because it expects those earnings to fall. The durability score (3/10) was my pre-written correction for that and it wasn't enough to flip the ranking. The other side of the ledger is unambiguous: MU is the riskiest name in the whole study (71% volatility, 93% chance of a 20% drawdown inside six months, 5th-percentile six-month return −53%, deepest fall in the window −27%). Putting 9% of a book with no income behind it into that is a sandbox decision, not a core one. TSM is the opposite: the lowest drawdown probability in the group (32%), the best bad-week behaviour (−2.4%), 31% growth at 19.6×, and the toll gate for NVDA, AMD and AVGO alike. **TSM keeps the slot; MU is the designated challenger, allowed into the sandbox at up to 2% as a cycle trade if I want the exposure, never into the core.**

AVGO and ASML finish mid-table. AVGO is the most correlated with the rest of the core (fit 0.32) and the second-worst in bad weeks, which is the wrong profile for a fourth chip name; it stays on the January watchlist as written. ASML is the best-quality business in the group (EUV monopoly, durability 10) but 10% growth at 31.7× is the worst growth-for-price combination here; it reports tomorrow (14 Oct), worth reading, not buying. AMD scores last on every fundamental criterion.

**What would flip it:** TSM failing its 15 Oct gate (a cut to the 2026 capex plan or a gross-margin miss) would hand the slot to MU on the numbers. MU falling 40% from here with its forward P/E rising above 10× would mean the cycle has turned and the risk/reward is at last honest; that is when a memory trade belongs in the sandbox.

## 5. Electricity: VST and CEG vs TLN, NRG, GEV, NEE, then DUK, SO and AEP (two slots)

First run (six names, 19:30):

| Name | Fwd P/E (20) | Rev growth (10) | Net margin (10) | Rate %/pt (15) | P(DD≥20%) (15) | Worst-10 (10) | Fit (10) | Contracts (10, judgment) | Numbers only | **Total** |
|---|---|---|---|---|---|---|---|---|---|---|
| NEE | 19.2 → 8 | 11% → 2 | 32% → 10 | −9.5 → 12 | 9% → 15 | −0.0% → 10 | −0.02 → 10 | 5 → 5 | 67 | **72** |
| VST | 15.9 → 12 | 4% → 0 | 11% → 4 | −25.9 → 6 | 48% → 12 | −2.5% → 4 | 0.00 → 8 | 8 → 8 | 46 | **54** |
| GEV | 47.4 → 0 | 13% → 6 | 23% → 8 | 0.0 → 15 | 65% → 9 | −0.8% → 8 | 0.32 → 0 | 6 → 6 | 46 | **52** |
| NRG | 10.2 → 20 | 13% → 4 | 2% → 2 | −28.1 → 3 | 69% → 3 | −1.9% → 6 | 0.02 → 6 | 5 → 5 | 44 | **49** |
| CEG | 24.0 → 4 | 26% → 8 | 11% → 6 | −25.6 → 9 | 66% → 6 | −3.2% → 0 | 0.04 → 4 | 10 → 10 | 37 | **47** |
| TLN | 12.9 → 16 | 76% → 10 | −5% → 0 | −31.3 → 0 | 76% → 0 | −2.9% → 2 | 0.21 → 2 | 9 → 9 | 30 | **39** |

Second run (21:40), after the question "why NEE over anything else?": three more regulated utilities added, Duke (DUK), Southern (SO) and AEP. Dominion's price page could not be read (rate-limited) and is left out.

| Name | Fwd P/E (20) | Rev growth (10) | Net margin (10) | Rate %/pt (15) | P(DD≥20%) (15) | Worst-10 (10) | Fit (10) | Contracts (10) | Numbers only | **Total** | Win prob (2 slots) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| DUK | 17.4 → 12.5 | 6% → 1.2 | 16% → 7.5 | −11.6 → 9.4 | 3% → 15 | −0.2% → 7.5 | −0.20 → 10 | 4 → 4 | 63 | **67** | 94% |
| NEE | 19.2 → 5 | 11% → 5 | 32% → 10 | −9.5 → 13.1 | 9% → 11.2 | −0.0% → 8.8 | −0.02 → 6.2 | 5 → 5 | 59 | **64** | 51% |
| SO | 18.6 → 10 | 6% → 2.5 | 15% → 6.2 | −9.5 → 11.2 | 6% → 13.1 | −0.8% → 6.2 | −0.14 → 8.8 | 4 → 4 | 58 | **62** | 43% |
| AEP | 18.7 → 7.5 | 10% → 3.8 | 14% → 5 | −14.4 → 7.5 | 12% → 9.4 | +0.1% → 10 | −0.10 → 7.5 | 4 → 4 | 51 | **55** | 1% |
| GEV | 47.4 → 0 | 13% → 7.5 | 23% → 8.8 | 0.0 → 15 | 65% → 5.6 | −0.8% → 5 | 0.32 → 0 | 6 → 6 | 42 | **48** | 2% |
| VST | 15.9 → 15 | 4% → 0 | 11% → 2.5 | −25.9 → 3.8 | 48% → 7.5 | −2.5% → 2.5 | 0.00 → 5 | 8 → 8 | 36 | **44** | 1% |
| NRG | 10.2 → 20 | 13% → 6.2 | 2% → 1.2 | −28.1 → 1.9 | 69% → 1.9 | −1.9% → 3.8 | 0.02 → 3.8 | 5 → 5 | 39 | **44** | 4% |
| TLN | 12.9 → 17.5 | 76% → 10 | −5% → 0 | −31.3 → 0 | 76% → 0 | −2.9% → 1.2 | 0.21 → 1.2 | 9 → 9 | 30 | **39** | 2% |
| CEG | 24.0 → 2.5 | 26% → 8.8 | 11% → 3.8 | −25.6 → 5.6 | 66% → 3.8 | −3.2% → 0 | 0.04 → 2.5 | 10 → 10 | 27 | **37** | 0% |

Pairwise correlations: VST–CEG 0.74, VST–TLN 0.76, VST–NRG 0.76, **VST–NEE 0.38**, CEG–NEE 0.11.

**What the second run exposed.** Add three regulated utilities and the rubric hands both slots to utilities (DUK and NEE) and drops VST to a 1% win probability. That is not because VST got worse; it is because the rubric pays 50 of its 100 points for low risk, mild bad weeks and low rate sensitivity, and a regulated utility has all three by construction: its returns are set by a regulator and do not depend on the price of power. Rank-based scoring makes it worse, since every utility added pushes the merchant generators down a rank on every risk criterion. Taken literally, the "energy thesis" sleeve would become a utility fund with no exposure to the thing the thesis is about, which is the scarcity value of firm power. So I am adding a structural rule, after the fact and flagged as such: **the first power slot must be a merchant generator** (VST, CEG, TLN or NRG, the only group with leverage to power prices and data-centre contracts), **and the second slot is the best different bet**, judged by the rubric.

**Slot 1, the merchant sub-battle: VST.** Six-name table: VST 54, NRG 49, CEG 47, TLN 39. Nine-name table: VST 44, NRG 44, TLN 39, CEG 37. VST wins both, narrowly over NRG, which is the same trade (0.76 correlated) with a 2% margin and a 47% fall inside the window. CEG has the best contracts in the group (Microsoft at Crane, Meta at Clinton, Google's ~890 MW deal announced 6 Oct; contracts 10) and the best growth (26%), but is the dearest IPP (24×), the worst in bad weeks (−3.2%), the deepest faller of the three (−38.5%), and 0.74 correlated with VST, so holding both is one bet held twice. TLN is the purest nuclear-to-data-centre story (AWS at Susquehanna, 76% growth, 12.9×) and the riskiest: losses, the worst rate sensitivity in the study, 76% drawdown probability, which is above the 75% core-eligibility line in §8. Sandbox only. One more thing the rubric cannot see: VST's 3.8% trailing revenue growth is the retail book and last year's power prices, while the gap between its trailing P/E (27.7×) and forward P/E (15.9×) says consensus expects earnings to rise roughly 70% over the next twelve months as the Meta (2,609 MW nuclear) and AWS (1,200 MW) contracts and higher prices arrive. (Rough: trailing and forward multiples mix reported and adjusted earnings.) Its other facts: the conditional $4.2B DOE loan for nuclear upgrades, integrated retail that hedges prices, and the best bad-week number of the IPPs (−2.5%). Contracts 8.

**Slot 2, the different bet: NEE, with DUK the alternate.** DUK edges NEE on the base rubric, 67 to 64 (94% vs 51% of runs), because it is the lowest-risk power stock tested (3% drawdown probability, −0.2% in bad weeks, 17.4× with a 3.7% yield) and owns the largest regulated nuclear fleet in the US. NEE edges DUK on everything that grows: 10.8% revenue growth vs 6.3%, a 32% margin vs 16%, less rate sensitivity (−9.5 vs −11.6% per point), and the growth tilt in §11 has it 58 to 52 (47% vs 13%). For a core slot the tie-break is the growth tilt, because the core's job is growth and the anchors already carry the defence. NEE also has the one thing in this group that reads as the thesis: in September 2026 it closed a $1.9B DOE loan to restart the 615 MW Duane Arnold plant under a 25-year contract with Google, targeting the end of 2028, on top of Seabrook and Point Beach and the largest renewables build in the country. Its contracts score is 5 because the regulated Florida utility and the renewables developer are most of the company. SO (Vogtle 3 and 4, Georgia data-centre load) and AEP (the largest contracted data-centre load pipeline of the three, but the highest rate sensitivity and a −14% earnings year) are the next two; GEV sells turbines into the build-out, which makes it a supplier (the exposure cut on 12 Oct) that moves with the chip names (fit 0.32) at 47×.

**Pick: VST 12%, NEE 9%.** NEE replaces CEG. The power pair's rate sensitivity drops from −25.8% per point (VST + CEG) to −18.9% (VST + NEE), and the two are only 0.38 correlated, so the 21% sleeve is two bets instead of one. CEG goes to the watchlist as first back in if its forward P/E gap to VST closes to under 4 points or the 10-year falls back below 4.5%. DUK is the alternate for the second slot if NEE's 21 Oct results disappoint. The rate rule from the A/B/C/D page (10-year above 5.50% two Wednesdays running → the power pair to 16%) stays, now trimming VST first since NEE carries less rate risk.

**What would flip it:** NEE's 21 Oct results are the gate. A cut to the 2026–27 earnings growth guide, a dividend-growth cut, or a large equity raise beyond plan would send the slot to DUK (results 5 Nov). If the 10-year yield turns down decisively (below 4.5%), the IPPs' rate penalty shrinks and CEG's contracts matter more.

## 6. Adopter: GOOGL vs META, MSFT, AMZN, NOW (one slot)

| Name | Rev growth (20) | Fwd P/E (20) | Net margin (10) | P(DD≥20%) (15) | Worst-10 (10) | Fit (15) | Purity (10, judgment) | Numbers only | **Total** | Win prob |
|---|---|---|---|---|---|---|---|---|---|---|
| GOOGL | 20% → 10 | 26.2 → 15 | 55% → 10 | 50% → 15 | −2.5% → 10 | 0.01 → 11 | 7 → 7 | 71 | **78** | 86% |
| META | 28% → 20 | 23.1 → 20 | 30% → 5 | 74% → 4 | −5.5% → 0 | 0.23 → 0 | 10 → 10 | 49 | **59** | 11% |
| MSFT | 18% → 5 | 27.4 → 10 | 40% → 8 | 50% → 11 | −3.9% → 5 | 0.05 → 8 | 5 → 5 | 46 | **51** | 3% |
| NOW | 22% → 15 | 30.9 → 0 | 11% → 0 | 88% → 0 | −4.3% → 3 | −0.05 → 15 | 9 → 9 | 33 | **42** | 0% |
| AMZN | 16% → 0 | 27.6 → 5 | 17% → 3 | 53% → 8 | −3.8% → 8 | 0.14 → 4 | 4 → 4 | 26 | **30** | 0% |

**GOOGL keeps the slot, 86%.** It is the only adopter that is both uncorrelated with the rest of the core (fit 0.01, the best of any core name) and well-behaved in bad weeks (−2.5%), with the highest margin (55%; the trailing net income includes unrealised gains on its investments, so the 17.7× trailing P/E flatters it, which is why the rubric uses the 26.2× forward figure). META wins the two fundamental criteria (28% growth at 23×, purity 10) and loses everything about risk: −5.5% in bad weeks, the worst of the five, a 74% drawdown probability and 0.23 correlation with the chip names. It is the challenger if GOOGL's 28 Oct results break, and reports a week earlier (21 Oct). MSFT is a fine company that is half a supplier (Azure). AMZN is the biggest supplier of all (AWS). **NOW scores zero in the robustness run**: 31× forward for 11% margins, a −55% fall inside the window and an 88% drawdown probability; it was already a Phase 2 name and the battle settles it, so it goes on the sell list (see the [limit orders](../trades/limit-orders-2026-10-14.md)).

**What would flip it:** a GOOGL cloud-growth or capex shock on 28 Oct, with META having already printed clean on the 21st.

## 7. Anchors: four sub-battles (one slot each), hard filter first

The anchor sleeve exists to hold up when the AI names don't, so the rubric weights defence heavily: worst-10 (25), drawdown probability (15), deepest fall (10), then forward P/E (15), revenue growth (15), net margin (10), dividend yield (5), correlation with NVDA (5). A name must pass the anchor test to be eligible; the "passes" column shows how often it passes when the year is resampled.

### Transport: UBER vs DASH, UNP

| Name | Worst-10 | P(DD≥20%) | Max fall | Fwd P/E | Rev growth | Net margin | Dividend | Corr NVDA | **Total** | Anchor test | Win prob |
|---|---|---|---|---|---|---|---|---|---|---|---|
| UNP | +2.8% | 19% | −11.7% | 20.7 | 4% | 29% | 2.0% | −0.07 | **77.5** | pass (100% of resamples) | 99% |
| UBER | −2.4% | 36% | −31.7% | 17.7 | 17% | 17% | 0% | 0.23 | **56.2** | pass (54%) | 1% |
| DASH | −4.4% | 82% | −43.2% | 28.8 | 34% | 5% | 0% | 0.26 | **16.2** | FAIL: beta 1.26, worst-10 (passes 8%) | 0% |

**UNP, 99%.** It has the best bad-week record in the whole study: *up* 2.8% on average in the Nasdaq's ten worst weeks (the next best, JPM and V, managed +0.9%), with a beta of −0.24, 21% volatility and an 11.7% worst fall. UBER passes the anchor test today but only in 54% of resampled years (its beta of 0.68 sits close to the 0.8 line), and it fell 32% inside the window. The railroad is the anchor; the ride-hailing company is a growth stock. One thing to know before buying: UNP is mid-way through acquiring Norfolk Southern, and the STB's schedule runs to final briefs on 28 May 2027 with a decision 0–90 days after the record closes, so merger headlines will move the stock through 2027. Gate: Q3 results 22 Oct.

### Financials: NU vs NDAQ, JPM, V

| Name | Worst-10 | P(DD≥20%) | Max fall | Fwd P/E | Rev growth | Net margin | Dividend | Corr NVDA | **Total** | Anchor test | Win prob |
|---|---|---|---|---|---|---|---|---|---|---|---|
| V | +0.9% | 10% | −16.8% | 26.9 | 14% | 50% | 0.7% | −0.19 | **65.0** | pass (100%) | 64% |
| JPM | +0.9% | 13% | −14.1% | 13.4 | 14% | 34% | 2.0% | 0.11 | **65.0** | pass (100%) | 33% |
| NU | −1.5% | 60% | −33.6% | 16.4 | 44% | 43% | 0% | 0.07 | **43.3** | pass (83%) | 1% |
| NDAQ | −1.6% | 42% | −22.2% | 21.6 | 14% | 35% | 1.3% | 0.08 | **26.7** | pass (80%) | 2% |

**V, 64%, with JPM the co-winner at 33%.** They tie on the point estimate (65–65) and V wins more of the perturbed runs because its risk numbers are the best in the sleeve (10% drawdown probability, beta 0.09, −0.19 correlation with NVDA) and its margin is 50%. JPM is half the price (13.4× vs 26.9×) with a 2% yield, and it reported Q3 today, so the trade-off is quality against price; either is a real anchor. NU, the name in the plan, is not: 41% volatility, a 34% fall inside the window, a 60% drawdown probability and no dividend. It passes the anchor test, but it's a growth stock, and the sleeve already has enough growth in the core. Gate for V: results 27 Oct.

### Consumer: MCD vs WMT, COST, CMG

| Name | Worst-10 | P(DD≥20%) | Max fall | Fwd P/E | Rev growth | Net margin | Dividend | Corr NVDA | **Total** | Anchor test | Win prob |
|---|---|---|---|---|---|---|---|---|---|---|---|
| COST | +0.5% | 5% | −14.6% | 42.1 | 10% | 3% | 0.6% | −0.16 | **65.0** | pass (100%) | 48% |
| MCD | −0.6% | 8% | −32.0% | 17.8 | 6% | 32% | 3.3% | −0.12 | **46.7** | pass (100%) | 42% |
| WMT | +0.5% | 25% | −23.0% | 37.7 | 6% | 3% | 0.9% | −0.06 | **45.0** | pass (98%) | 3% |
| CMG | +0.2% | 66% | −28.8% | 24.0 | 7% | 11% | 0% | −0.23 | **43.3** | pass (90%) | 6% |

**A coin flip: COST 48%, MCD 42%.** COST is the lowest-risk stock in the study (5% drawdown probability, 20% volatility, 14.6% worst fall) and the point-estimate winner by 18 points; MCD gives back most of that on its own 32% slide inside the window, which has nothing to do with the Nasdaq and everything to do with McDonald's having a bad year. Where they differ is price: COST at 42× earnings for 10% growth and 3% margins is paying for safety at a level where a de-rating to 30× would cost 29% with nothing going wrong at the company; MCD at 17.8× with a 3.3% yield and 32% margins has already had its de-rating. **Tie-break rule, stated now: when two anchors are within 10 points of win probability, the cheaper one on forward P/E takes the slot.** MCD keeps it. COST is the alternate if MCD's 4 Nov results show a second quarter of falling US comparable sales.

### Defence: BWXT vs AVAV, LMT, KTOS

| Name | Worst-10 | P(DD≥20%) | Max fall | Fwd P/E | Rev growth | Net margin | Dividend | Corr NVDA | **Total** | Anchor test | Win prob |
|---|---|---|---|---|---|---|---|---|---|---|---|
| LMT | −2.0% | 50% | −24.8% | 16.5 | 7% | 8% | 2.9% | −0.02 | **81.7** | pass (87%) | 83% |
| BWXT | −4.2% | 56% | −42.8% | 28.0 | 23% | 10% | 0.8% | 0.32 | **61.7** | **FAIL: worst-10** (passes 27%) | 6% |
| KTOS | −8.4% | 98% | −67.6% | 44.1 | 26% | 2% | 0% | 0.18 | **29.2** | FAIL: beta, worst-10 (0%) | 0% |
| AVAV | −9.8% | 99% | −65.1% | 38.9 | 84% | −10% | 0% | 0.17 | **27.5** | FAIL: beta, worst-10 (0%) | 0% |

**BWXT fails the anchor test.** This is the 14 Oct check the checklist asked for, and the answer is no: in the Nasdaq's ten worst weeks it fell 4.2% on average, worse than the index's 3.1%, and it passes the test in only 27% of resampled years. Its correlation with VST (0.44) scrapes under the 0.5 rule, but its fit of 0.33 is the highest of any anchor candidate, which says what it is: a nuclear stock that trades with the AI-power complex. That makes it a possible *core* energy candidate one day, not an anchor. It drops off the anchor list; its 2 Nov results stay on the calendar as a watchlist item only. **LMT takes the slot, 83%:** beta −0.07, 16.5× with a 2.9% yield, −2.0% in bad weeks. It is not a perfect anchor (33% volatility this year and a 24.8% fall inside the window, hence a 50% drawdown probability), but it is the only defence name that passes. AVAV and KTOS fail in 100% of resamples: 86% and 75% volatility, falls of 65% and 68%. AVAV therefore goes on the sell list without waiting for a thesis page. Gate for LMT: Q3 results 22 Oct.

---

## 8. Three rules this page adds

1. **Core eligibility: a name with a bootstrap P(20%+ drawdown in 26 weeks) above 75% is a sandbox name, not a core name,** however good its fundamentals. On today's numbers that excludes MU (93%), AMD (90%), NOW (88%), TLN (76%), DASH, AVAV and KTOS, and keeps every current core name (NVDA 34, TSM 32, VST 48, GOOGL 50, CEG 66, NEE 9). I am adding this after seeing MU's result, so it is fair to call it a reaction; I think it is the right rule regardless, because it formalises what the sandbox was always for.
2. **Anchor tie-break:** within 10 points of win probability, the cheaper name on forward P/E wins (§7, consumer).
3. **Power pair structure:** the first slot is a merchant generator, the second is the best different bet; for a core slot, a tie goes to the growth tilt (§5, §11). Added after the utilities run showed the rubric would otherwise hold two regulated utilities and no merchant power at all.

All three go into the [adaptive rules](adaptive-rules.md) change log if adopted on 14 Oct.

## 9. What changes if I adopt the battle list (Option E)

- **Decision page:** Option E added alongside A–D; it is Option D with NEE in CEG's slot (DUK the alternate) and the anchor sleeve rebuilt as UNP, V, MCD, LMT. Same three conditions as D (rate rule, VST beta check, GOOGL gate) plus the gates above. Option G (E with NU for V) and G+ (the re-risk after a job) are the growth versions in §11.
- **Sells:** CEG in two halves as NEE is bought (one out, one in), both before CEG's 9 Nov results; NOW and AVAV join the Phase 2 sell list now rather than waiting for thesis pages; MP had no battle to enter (rare earths are not in any slot) and sells with them. All drafted in [`trades/limit-orders-2026-10-14.md`](../trades/limit-orders-2026-10-14.md).
- **Anchor gates:** UNP 22 Oct, LMT 22 Oct, V 27 Oct, MCD 4 Nov. UBER's 4 Nov gate and NU's 12 Nov gate are removed; BWXT's 2 Nov gate becomes a watchlist note.
- **Order of anchor entry:** UNP and V first (January: 5% + 4%), MCD third, LMT fourth when the switch triggers. The sleeve's 15% cap and 20% switch rule are unchanged.
- **AI-linked share of the book** falls from ~47% to ~38% (VST, NVDA, TSM, GOOGL), with NEE's 9% as power-adjacent. The target-portfolio and checklist lines get updated after the review, not before.

## 10. What I'd want to re-run

- The whole study after each gate (15, 21, 22, 27, 28 Oct, 4 Nov): the fundamentals snapshot is a day old and the results season will move it.
- The same battles on a 3-year window once I have the data, so the bootstrap has seen 2022.
- RTX in the defence battle and Dominion (D) in the power battle, when their pages can be read.

## 11. The growth tilt (added 21:40, after "is this the most optimised for growth?")

Option E was built for robustness: the rubrics pay heavily for bad weeks and drawdowns because the book has no wage behind it until January. The question deserved a straight test, so every battle was re-run with a growth-tilted weight set: more for revenue growth and price, a new 10-point "upside" criterion (consensus analyst target vs price, an optimistic measure by nature, used only here), nothing for bad weeks, and the same 1,000-run robustness. The anchor test still applies to anchors.

| Slot | Growth-tilt weights | Winner (win prob) | Runner-up | What I take from it |
|---|---|---|---|---|
| Chips | growth 25, value 25, quality 10, risk 10, fit 10, upside 10, durability 10 | NVDA 80 (100%), MU 79 (100%) | TSM 52 (0%) | MU's case is peak-cycle numbers plus a +66% consensus upside; it stays sandbox-only under the 75% rule |
| Power | value 25, growth 20, margin 10, rates 10, risk 10, fit 5, upside 10, contracts 10 | NRG 58 (70%), NEE 58 (47%) | TLN 56 (57%), DUK 52 (13%), VST 48 (2%) | NRG's win is a 10× multiple and a +75% "upside" that is analysts not yet cutting targets after a −37% year; TLN fails the 75% rule; NEE is the co-winner either way |
| Adopter | growth 25, value 25, quality 10, risk 10, fit 10, upside 10, purity 10 | GOOGL 73 (61%) | META 68 (39%) | GOOGL holds |
| Transport | growth 25, value 20, quality 15, worst-10 15, risk 10, upside 10, corr 5 | UNP (54%) | UBER 65 pts (46%) | UBER scores more points, UNP wins more runs; UNP holds |
| Financials | same | **NU 67 (60%)** | V 57 (32%) | the one slot the tilt changes: NU's 44% growth and 43% margin at 16× beat V's safety once bad weeks stop counting |
| Consumer | same | MCD (58%) | CMG 60 pts (29%) | MCD holds |
| Defence | same | LMT 60 (72%) | BWXT 57 (17%) | LMT holds; BWXT still fails the anchor test |

**Taken literally**, the growth tilt gives NRG 12, NEE 9, NVDA 9, MU 9, GOOGL 8 with UBER and NU as anchors. The Monte Carlo puts that book at 12.8% volatility, a 19% chance of a 10%+ fall inside six months and −10.3% in a Nasdaq −25%, which is Option D's risk with a different set of names, and three of its five changes rest on the least trustworthy numbers in the study (memory-cycle growth, stale analyst targets, a trailing growth figure that misreads VST).

**Taken with judgment, the growth version is Option G: Option E with NU in V's slot.** Everything else survives the tilt. NU is the only change where the growth case is made by durable numbers (44% revenue growth, 43% margin, 16× earnings, passes the anchor test in 83% of resampled years) rather than by cycle or by target lag. Cost: the book's six-month 10%-fall probability goes from 6% to 8% and volatility from 8.7% to 9.4%.

**The bigger lever is weight, not names.** In the January-stage book, 52% sits in cash, the two ETFs and the anchors; the four growth engines (NVDA, TSM, GOOGL, VST) are 38%. The expected return of cash is zero, so every 10 points of cash costs roughly 10% of whatever the invested book earns. That cash is there for a reason written in the plan (no income until January; the drawdown plan, which is how cash turns into growth by buying falls), and the [adaptive rules](adaptive-rules.md) already say the risk-down targets are revisited at the first review after a new job. **Option G+** is what that revisit should produce: cash to the 15% floor, the core to 55% (VST 14, NVDA 11, TSM 11, GOOGL 10, NEE 9), same anchors. Monte Carlo: 10.8% volatility, 13% chance of a 10% fall, −8.3% in a Nasdaq −25%, +6.6% in a +20% year. More growth bought with weight in names that already won their battles, not with riskier names.

**Why I'd still run E (or G) now and not G+:** the risk that destroys long-term growth is not volatility, it is being forced to sell at the bottom, and a book with no income and a 25% cash buffer can sit through a 30% fall without selling anything. Your own track record says the same thing from the other side: trades held over three months won 71% of the time and the short ones lost. Volatility you can hold through is a cost; volatility that forces a sale is a loss.

## Sources
- Prices and fundamentals: stockanalysis.com quote and history pages for each ticker, 13 Oct 2026 (weekly closes via its history API; the US 10-year from the Treasury's daily yield-curve file).
- NEE / Duane Arnold: [The Next Web, 10 Sep 2026, "US closes $1.9bn loan to restart the Iowa nuclear plant powering Google"](https://thenextweb.com/news/duane-arnold-nuclear-restart-1-9bn-doe-loan-google); [S&P Global, Oct 2025, NextEra plans Duane Arnold restart as soon as 2028](https://www.spglobal.com/market-intelligence/en/news-insights/articles/2025/10/nextera-plans-duane-arnold-restart-as-soon-as-2028-q3-results-top-estimates-94343987).
- UNP–NSC merger schedule: [Railway Age, "STB advances UP-NS merger proceeding to merits evaluation phase"](https://www.railwayage.com/regulatory/stb-advances-up-ns-merger-proceeding-to-merits-evaluation-phase/).
- LMT Q3 date: [Lockheed Martin, 1 Oct 2026, Q3 2026 earnings webcast notice](https://news.lockheedmartin.com/2026-10-01-Lockheed-Martin-Announces-Third-Quarter-2026-Earnings-Results-Webcast).
- CEG/VST contract facts: the [A/B/C/D comparison](2026-10-13-abcd-comparison.md) and the [7 Oct review](../weekly-reviews/2026-10-07.md).
- Method: Politis & Romano (1994), the stationary bootstrap.
