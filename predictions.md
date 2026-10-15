# Predictions log

Calls I make about prices or events, written down **before** the outcome, so I can check my own judgment later. Each one has a deadline and a test that can only come out yes or no. Git timestamps every entry, so none of them can be edited after the fact.

Alongside each call: a **base rate**, i.e. how often a coin-flip market with the stock's own volatility would produce the same outcome. Beating the base rate over many calls is the evidence that my read adds something; matching it means it's luck either way.

## Scoreboard

| # | Made | Call | Deadline | Result |
|---|---|---|---|---|
| 1 | 14 Oct 2026 | NBIS holds (no close below $175) and is back at $230 | Wed 4 Nov 2026 | open |
| 2 | 15 Oct 2026 | My ten picks beat the real book by a big margin by 6 months | Wed 14 Apr 2027 | open |

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

---

## 2 · My picks beat the real book, by a big margin, by 6 months
**Made:** Thu 15 Oct 2026, 15:43 UK, on a day the Nasdaq was down ~1.4% (chips' eighth straight loss, AI-debt worries), after I wanted to spend the shield on dips and held back.

**My words:** "I really do think it will outperform this portfolio, especially by 6 months' time. If I'm right and it's by a big margin I expect you to start respecting my reads. It's just my genuine intention that's against the numbers."

**The books:** my ten picks, 10% each, fully invested ([paper race](shadow-portfolio.md)) vs the real book across all four accounts (cash, exits and gate buys as they actually happen, time-weighted so deposits don't count). Both indexed to 100 at the 15 Oct 2026 close.

**How it's scored (fixed 15:45 on 15 Oct, before the close):**
- **Full hit:** my picks ahead of the real book by **10 percentage points or more** on total return at the Wed 14 Apr 2027 review (prices at Tue 13 Apr close).
- **Half:** ahead by less than 10 points.
- **Miss:** level or behind.
- Written alongside, not part of the score: each book's worst fall from a high over the six months, and return divided by worst fall.

**Base rate:** to be added at the Wed 21 Oct review, before any meaningful move, from a joint bootstrap of the eleven names' weekly returns (the data for IREN, IONQ, NFLX, SOFI and LLY isn't in the journal yet). Expectation stated now so it can't move later: a fully invested book of high-volatility names beats one holding ~18% cash in most six-month windows when the market rises and loses in most when it falls, so the base rate will sit near the odds of the market being up over six months.

**What changes if it's a full hit:** at the 14 Apr 2027 review, a sleeve inside the real book for my own picks is proposed (size decided then, with the evidence in front of me), and from then on my reads get tested as entries rather than overridden by default. If it's a miss, the rules-first process stays as it is.

**Result:** ____
