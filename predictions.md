# Predictions log

Calls I make about prices or events, written down **before** the outcome, so I can check my own judgment later. Each one has a deadline and a test that can only come out yes or no. Git timestamps every entry, so none of them can be edited after the fact.

Alongside each call: a **base rate**, i.e. how often a coin-flip market with the stock's own volatility would produce the same outcome. Beating the base rate over many calls is the evidence that my read adds something; matching it means it's luck either way.

## Scoreboard

| # | Made | Call | Deadline | Result |
|---|---|---|---|---|
| 1 | 14 Oct 2026 | NBIS holds (no close below $175) and is back at $230 | Wed 4 Nov 2026 | open |
| 2 | 15 Oct 2026 | My ten picks beat the real book by a big margin by 6 months | Wed 14 Apr 2027 | open |
| 3 | 15 Oct 2026 | Today's lows are the bottom: no close below $167 (NBIS) or $26 (IREN) | Wed 13 Jan 2027 | open |
| 4 | 15 Oct 2026 | CELH trades at $60 within a year | Fri 15 Oct 2027 | open |

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

**Tracking:** 15 Oct close **$188.41** (day low $163.36, then a ~15% reversal off the low). Floor ($175) intact so far.

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

---

## 3 · NBIS $167 and IREN $26 are the bottom
**Made:** Thu 15 Oct 2026, 18:43 UK, mid-session, on the day of the neocloud debt sell-off (CoreWeave bonds repriced, chips' eighth straight loss). At the time: NBIS $179.44 (day low $163.36), IREN $28.98 (day low $26.60).

**My words:** "I think $167 for Nebius and $26 for IREN is the base price they're going to hit. I don't believe that they're going to go below that from now."

**How it's scored (fixed 18:45 on 15 Oct, before the close):**
- **NBIS:** no daily **close** below **$167.00** from the 15 Oct close to the deadline. (It already traded at $163.36 intraday today; like Prediction 1, closes count, intraday spikes don't.)
- **IREN:** no daily **close** below **$26.00** over the same window.
- **Deadline: Wed 13 Jan 2027** (three months, the paper race's first checkpoint). "From now" has no end date, and a floor call with no deadline can't be scored, so three months was set as the default; an interim note is written at the 4 Nov review.
- **Full hit** = both hold. **Half** = one holds. **Miss** = neither.

**Base rate** (200,000 simulated paths of daily closes, no drift, from the prices at the time; NBIS volatility 94% from its past-year weekly closes, IREN 100% assumed, as its weekly history isn't in the journal yet; the joint figure assumes the two move together with 0.6 correlation):

| Window | NBIS holds $167 | IREN holds $26 | Both hold |
|---|---|---|---|
| to 4 Nov (interim) | 33% | 42% | 23% |
| **to 13 Jan 2027** | **14%** | **18%** | **7%** |

The numbers are low because both stocks swing so much that a level 7–10% below the price usually gets tested at some point within three months. Beating a 7% base rate would be strong evidence that the read on where buyers step in adds something.

**Tracking:** 15 Oct closes NBIS **$188.41**, IREN **$30.39**. Both floors intact on the first close.

**Personal note, 18:46 (not scored):** "When IREN hit $27, that was the best price I could buy." IREN's low on the day was $26.60, and it bounced ~9% from there within hours.

**What I'll do whatever happens:** no NBIS buys before ~22 Nov (dilution rule) and none in the 27 Oct–10 Nov results window; no IREN adds (sandbox, no averaging down). The prediction doesn't change the orders.

**Result:** ____

---

## 4 · CELH reaches $60 within a year
**Made:** Thu 15 Oct 2026, 19:27 UK, the day I sold the whole position (T212 lot $27.00, Revolut lot $27.88) under the concentration plan. CELH was green that afternoon while the Nasdaq fell, as money rotated out of chips and AI debt.

**My words:** "I was holding Celsius for months with genuine conviction that it could hit $60 in the next year. Honestly the move from money in AI to other sectors could be the catalyst for that."

**How it's scored (fixed 19:30 on 15 Oct):**
- **Full hit:** CELH **trades** at or above **$60.00** (intraday counts) at any point up to **Fri 15 Oct 2027**.
- **Half:** it gets to **$45** (+61% from the $27.88 sale) but not $60.
- **Miss:** neither.
- Whatever happens, the exit's cost or saving is written in a post-mortem: the sale price against CELH's price on 15 Oct 2027, so the decision to sell is scored as well as the call.

**Base rate** (100,000 simulated one-year paths from $27.88, no drift): CELH touches $60 in **10%** of paths at 55% volatility and **17%** at 70% (its volatility isn't in the journal's data yet, so both are shown); it ends the year at or above $60 in 5–7%.

**What I'll do whatever happens:** no buy-back before the [re-entry gate](plans/watch-items.md) (the 5 Nov results) passes. The prediction doesn't change the orders.

**Result:** ____
