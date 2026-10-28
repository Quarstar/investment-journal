# Predictions log

Calls I make about prices or events, written down **before** the outcome, so I can check my own judgment later. Each one has a deadline and a test that can only come out yes or no. Git timestamps every entry, so none of them can be edited after the fact.

Alongside each call: a **base rate**, i.e. how often a coin-flip market with the stock's own volatility would produce the same outcome. Beating the base rate over many calls is the evidence that my read adds something; matching it means it's luck either way.

## Scoreboard

| # | Made | Call | Deadline | Result |
|---|---|---|---|---|
| 1 | 14 Oct 2026 | NBIS holds (no close below $175) and is back at $230 | Wed 4 Nov 2026 | open; **floor part broken** (16 Oct); 170.47 on 27 Oct, $230 needs +35% in 6 sessions → half at best |
| 2 | 15 Oct 2026 | My ten picks beat the real book by a big margin by 6 months | Wed 14 Apr 2027 | open; week 2: picks 96.4 vs real 98.8 (−2.4) |
| 3 | 15 Oct 2026 | Today's lows are the bottom: no close below $167 (NBIS) or $26 (IREN) | Wed 13 Jan 2027 | **Miss (decided 23 Oct).** NBIS closed below $167 on 16, 22, 23, 26 Oct (low close 153.27); IREN below $26 on 22, 23, 26 Oct (low close 24.91). Base rate for both holding: 7% |
| 4 | 15 Oct 2026 | CELH trades at $60 within a year | Fri 15 Oct 2027 | open; 29.96 on 20 Oct (+7–11% since the exits at 27.00 / 27.88) |
| 5 | 16 Oct 2026 | Bought at $165, NBIS trades back in the $200s within 3 months | Sat 16 Jan 2027 | open (filled 16 Oct); 170.47 on 27 Oct (low 149.48 on 26 Oct) |
| 6 | 17 Oct 2026 | NBIS does not close below $140 | Wed 13 Jan 2027 | open; low close 153.27 (26 Oct) |
| 7 | 22 Oct 2026 | NBIS's Q3 results confirm demand and the stock re-rates | price part: the review after results week; follow-through: 4 weeks after | open |

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

**Result: Miss**, decided 23 Oct, scored at the 28 Oct review. NBIS: closes 165.47 (16 Oct), 159.17 (22 Oct), 158.74 (23 Oct), 153.27 (26 Oct). IREN: 25.51 (22 Oct), 24.91 (23 Oct), 25.43 (26 Oct); new 52-week low 23.72 intraday on 26 Oct. Both legs broke inside eight sessions, in line with the 7% base rate for both holding. What it says about the read: the *areas* were close (NBIS bounced 11% from $153, IREN reclaimed $27 on 27 Oct), but a floor call scored on closes needs room below the level for one bad week, and these two names move 6–10% in a day. A future floor call on either should sit about one weekly standard deviation (~13% for NBIS) below the price, not 7–10%.

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

---

## 5 · NBIS bought at $165 is back in the $200s within 3 months
**Made:** Fri 16 Oct 2026, 16:18 UK. NBIS ~$188 after the 15 Oct reversal (low $163.36, close $188.41).

**My words:** "At $165 I'm going to put in [about 2.6% of the book]. I'm extremely confident that it will go back to the $200s within the next 3 months. If it gaps down below that, another [~1.3%] at $148, and that's all. I'll keep my limit sells."

**How it's scored (fixed 16:20 on 16 Oct):**
- **Started 16 Oct 2026:** the $165 buy filled that day (NBIS closed $165.47). Deadline **Sat 16 Jan 2027**. Size was ~3.2% of the book, more than the ~2.6% stated when the call was made; the overshoot is on the record in the 14 Oct review's addenda.
- **Full hit:** NBIS **trades** at or above **$200.00** (intraday counts) within 3 months of the fill date.
- **Miss:** it doesn't. Whatever happens, the buy's result is written up against the plan (which said no NBIS buys before ~22 Nov).

**Base rate** (200,000 simulated paths, 94% volatility, no drift): from $165, NBIS touches $200 within 3 months **56%** of the time. (From today's $188, the chance it dips to $165 at some point in the next 3 months is 78%.)

**Result:** ____

---

## 6 · NBIS doesn't close below $140
**Made:** Sat 17 Oct 2026, 10:28 UK. NBIS $165.47 (16 Oct close), after a −12% day; semis nine sessions down.

**My words:** "If Nebius reaches a price below $140 it is a seriously crazy price. People like Leopold and other investment firms were buying at mid-$200s thinking that was a good price. I think buyers will heavily defend those areas and the rally will be strong when the time comes."

**How it's scored (fixed 10:30 on 17 Oct):** no daily **close** below **$140.00** from 19 Oct to **Wed 13 Jan 2027** (same deadline as Prediction 3). Hit or miss; intraday spikes don't count.

**Base rate** (200,000 simulated paths, 94% volatility, no drift, from $165.47): the floor holds in **27%** of paths. For reference the same simulation gives the $205 sell a 25% chance of filling by 6 Nov and the $215 sell a 3% chance by 23 Oct.

**Noted against it, so it's judged fairly:** NBIS closed at $89–101 in March 2026 with the Microsoft and both Meta deals already signed, and the map's next demand zone below $148–160 is $105–118. The call is that the stock has re-rated since then and the new floor is higher.

**What I'll do whatever happens:** the orders as written (sells $215 → $205 → market by 6 Nov; the $148 buy is "that's all"). If it goes below $140, I don't add: the $205 sell is what has to come first, before any rebuy is considered.

**Result:** ____

---

## 7 · Nebius's Q3 results confirm demand and the stock re-rates
**Made:** Thu 22 Oct 2026, 23:39 UK. NBIS $171.57 (21 Oct close), ~$163 pre-market on 22 Oct; the day Jensen Huang said neocloud demand is "off the charts" but capital is scarce.

**My words:** "Once earnings are revealed and it's shown how much their demand actually is and how the company's revenue is booming, it will confirm a lot to the market … Nebius has done this repeatedly whenever doubt rises; just over the past year I've had nearly 4 moments like this."

**How it's scored (fixed 23:45 on 22 Oct, before the results date is confirmed):** two parts, each hit or miss.
- **Price, results week:** the close on the Friday of results week is **≥ 10% above** the close on the trading day before results, **and** beats QQQ over the same span.
- **Follow-through:** the close four weeks after that Friday is still above the pre-results close.
- **Thesis check (recorded, not scored as a hit):** from the release itself: ARR on track for the $7–9B year-end target; backlog above $37.5B; AI-cloud margin near 50%; a 2027 funding plan that doesn't lean on heavy new dilution. My view going in: the first three are largely priced; the fourth is what moves it.

**The record behind the call** (from the journal's weekly closes, Oct 2025 – Oct 2026): results weeks went **−25%** (Nov 2025, QQQ flat), **+14%** (Feb 2026), **+24%** (May 2026), **+48%** (Aug 2026), so three of the last four were up 14%+ while QQQ was flat or down. Every weekly swing low 22–38% off the prior high in the year bounced **+9% to +118%** within eight weeks. "Nearly four moments" is fair: Nov–Mar (three lows near $83–89), July ($178), late August ($209).

**Base rates:** the journal's own record says 3 of 4 (75%, a sample of four). A no-edge model (no drift, a results-week standard deviation of ~20%) says **~31%** for a +10% week. The truth for this print is probably between the two.

**Noted against it, so it's judged fairly:** the three good prints came while capital was easy and hyperscaler capex growth was accelerating (+86–97% in 2026). Going into this one, capex growth is guided to slow in 2027 (+35–60%), the CEO of Nvidia is saying capital is scarce, CoreWeave's bonds yield ~15%, and Nebius's own shares are up 22% in a year. Same company, different weather.

**What I'll do whatever happens:** the first-half sell as ordered (8 shares: $212 → $205 → market by 6 Nov, holding ~7%, the top of the band), the $148 buy as the last buy, and no rebuy until the 22 Nov dilution check and the 10 Nov share count.

**Result:** ____
