# Predictions log

Calls I make about prices or events, written down **before** the outcome, so I can check my own judgment later. Each one has a deadline and a test that can only come out yes or no. Git timestamps every entry, so none of them can be edited after the fact.

Alongside each call: a **base rate**, i.e. how often a coin-flip market with the stock's own volatility would produce the same outcome. Beating the base rate over many calls is the evidence that my read adds something; matching it means it's luck either way.

## Scoreboard

| # | Made | Call | Deadline | Result |
|---|---|---|---|---|
| 1 | 14 Oct 2026 | NBIS holds (no close below $175) and is back at $230 | Wed 4 Nov 2026 | open |

---

## 1 · NBIS: the floor holds, back to $230 in 2–3 weeks
**Made:** Wed 14 Oct 2026, 15:01 UK. NBIS trading around **$189** after falling ~9% on the day (sector-wide: neocloud funding worries, oil near $105, CPI day; no company news). I bought ~0.9% of the book at $189 at 14:40.

**My words:** "I think 186 is the floor right now for Nebius, I think that point is where it will hold. I believe that in 2–3 weeks' time we will be back at $230."

**How it's scored (fixed 15:03 on 14 Oct, before the close):**
- **Floor:** no daily **close** below **$175.00** from 14 Oct to the deadline. My read is $186; I set the test at $175 because a floor is an area, not a line, and $186 sits less than one normal day's move below the price.
- **Target:** at least one daily **close** at or above **$230.00** by **Wed 4 Nov 2026** (3 weeks; before the 10 Nov results).
- **Full hit** = both. **Half** = target reached but the floor broke first, or the floor held but no $230 close. **Miss** = neither.

**Base rate** (simulation from NBIS's own past-year volatility, 94% annualised, no drift, 15 trading days from $189): no close below $175 **34%** · a $230 close **28%** · both **23%**. (At a $186 floor the same numbers were 17% / 28% / 14%.) Method: 200,000 simulated 15-day paths of daily closes, volatility taken from the weekly closes in `data/weekly_closes_battles_2025-10-24_to_2026-10-09.csv`.

**What I'll do whatever happens:** no more NBIS buys until $160 with the four deep-value checks ([drawdown plan](plans/2026-10-10-drawdown-plan.md)); the first-half sale stays at a $215 limit to Fri 23 Oct, market Mon 26 Oct. The prediction doesn't change the orders.

**Result (fill on 4 Nov or when decided):** ____
