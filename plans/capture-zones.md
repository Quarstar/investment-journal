# Capture zones · per-stock buy levels · mapped 15 Oct 2026 (14 Oct closes)

Each name in the plan and on the deep-value list gets its own map: the support it's testing now, a **first capture zone**, a **capitulation zone**, and the **ceilings** above. The point is not to miss a name that falls on its own story while the index barely moves. NBIS fell 27% from its 6 Oct high in seven sessions while QQQ fell 4%, and an index-only trigger would never have fired. The zones are refreshed every Wednesday from the latest closes.

> Personal record, not financial advice.

## How the levels are found

A level is where buyers have shown up before. The script ([`analysis/capture_zones.py`](../analysis/capture_zones.py)) collects candidate levels below the last close from five sources, then merges any that sit within one day's average range (ATR) of each other. The more sources agree, the stronger the level:

| Source | What it means |
|---|---|
| **Daily swing lows** (last 50 sessions) | A low that held for 3 sessions either side: the recent floors |
| **Weekly swing closes** (past year) | A weekly close lower than the 2 weeks either side: the bigger floors |
| **40-week average** (≈ 200-day) | The trend line that big funds watch |
| **52-week closing low** | The year's floor |
| **Volume shelves** | Price bands where the most shares changed hands in the 50 sessions: lots of holders with a cost basis there |

The mechanical output is the starting point. The zones below are my read of it, an analyst's overlay: I merged neighbouring levels, used the official 52-week high for NBIS ($299.86, older than the 50-session window), and where the script found no structure, I said so and used a volatility band instead of inventing a level. [`analysis/capture_zones_final.py`](../analysis/capture_zones_final.py) holds the final bands and computes the numbers in the table.

**Columns:** *Fwd P/E* = the price at the middle of the zone divided by forward earnings from the 13 Oct snapshot, a check that the zone is also cheaper on earnings and not just on the chart. *P(touch)* = how often a stock with its own volatility and no trend reaches the zone's upper edge within 13 weeks (20,000 simulated paths). It's a base rate, not a forecast: a high number means the zone is close, not that it's likely to hold.

## The map (14 Oct 2026 closes)

| | Last | Vol | Testing now | **Zone 1** · first capture | Fwd P/E | P(touch) | **Zone 2** · capitulation | Fwd P/E | P(touch) | Ceiling | Next ceiling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **Power** | | | | | | | | | | | |
| VST | 151.79 | 43% | 146–150 | **132–141** (−7%, −32% off high) | 13.3 | 71% | **115–122** (−20%, −41%) | 11.6 | 32% | 154–155 | 164–169 |
| NEE | 78.37 | 18% | 77.3–77.7 | **75.4–76.7** (−2%, −22%) | 18.6 | 77% | **71.5–72.8** (−7%, −26%) | 17.6 | 39% | 84.0–84.4 | 87.6 |
| **Chips** | | | | | | | | | | | |
| NVDA | 221.30 | 33% | 219.6–221.1 | **212–218** (−2%, −12%) | 17.7 | 88% | **198–204** (−8%, −17%) | 16.5 | 59% | 230–234 | 243 |
| TSM | 430.00 | 28% | 422–428 | **406–417** (−3%, −16%) | 18.2* | 78% | **393–404** (−6%, −18%) | 17.6* | 63% | 440–446 | 487 |
| **Adopter** | | | | | | | | | | | |
| GOOGL | 347.64 | 33% | 341–342 (just above Zone 1) | **334–342** (−2%, −16%) | 25.1 | 88% | **298–307** (−12%, −25%) | 22.4 | 45% | 352–359 | 401 |
| **Anchors** | | | | | | | | | | | |
| UNP | 286.43 | 21% | 285–286 | **272–278** (−3%, −13%) | 20.2 | 74% | **262–270** (−6%, −15%) | 19.5 | 55% | 289–293 | 306–314 |
| NU | 14.93 | 41% | 14.2–14.4 | **13.3–13.9** (−7%, −25%) | 14.2 | 71% | **11.7–12.4** (−17%, −33%) | 12.6 | 35% | 15.6–16.2 | 18.0 |
| MCD | 238.31 | 16% | 234–235 | **229–233** (−2%, −32%) | 17.4 | 75% | **218–222** (−7%, −36%) | 16.6 | 36% | 242–250 | 287 |
| **Deep-value list** | | | | | | | | | | | |
| NBIS | 186.01 | 94% | 175–183 | **148–160** (−14%, −49%) | n/m | 76% | **105–118** (−37%, −63%) | n/m | 37% | 209–221 | 228–237 |
| AMD | 570.82 | 62% | – | **451–488** (−15%, −29%) | 42.0 | 61% | **383–408** (−29%, −40%) | 35.4 | 30% | 606–620 | 648–659 |
| CEG | 279.54 | 47% | 264–271 | **242–256** (−8%, −36%) | 20.1 | 68% | **206–222** (−21%, −45%) | 17.3 | 32% | 286–301 | 310 |
| MU | 914.13 | 71% | 888–903 | **800–845** (−8%, −28%) | 4.9 | 81% | **698–743** (−19%, −37%) | 4.3 | 58% | 978–1,003 | 1,088–1,108 |
| TLN | 358.42 | 53% | 349–356 | **324–344** (−4%, −23%) | 11.2 | 84% | **283–302** (−16%, −33%) | 9.8 | 51% | 374–391 | 436 |
| **January gate** | | | | | | | | | | | |
| AVGO | 346.25 | 45% | 336–343 | **314–325** (−6%, −29%) | 18.3 | 75% | **295–306** (−12%, −33%) | 17.2 | 57% | 357–368 | 447 |
| **Index** | | | | | | | | | | | |
| QQQ | 728.95 | 18% | 722 | **700–709** (−3%, −8%) | | 72% | **684–688** (−6%, −10%) = the G+ half trigger | | 50% | 744–752 | 760–763 |

Percentages in brackets: distance of the zone's top from the 14 Oct close, then of its middle from the 52-week high. *TSM's forward P/E uses pre-results earnings; after the 15 Oct beat-and-raise, forward EPS is higher, so the true multiple at each zone is lower.

## What each zone is built on, and the read

**VST.** Testing $146–150 now: a volume shelf plus four weekly swing closes (Feb, Mar, Jun, Jul). Zone 1 is the strongest level on the map (8 sources): the 52-week closing low of $136.21 and three daily lows at $133–135 (24 Aug, 1 Sep, 30 Sep), a triple bottom. Below $136 there is **no price structure in the past year**, so Zone 2 is a volatility band that lines up with 40% off the high ($121). At Zone 2 VST would be 11.6× forward earnings for the merchant generator with the Nvidia-linked contracts. *Rate rule wins:* if the 10-year is above 5.50% at two reviews running, VST is being trimmed, and no VST capture is made until the rule switches off.

**NEE.** The low-volatility name, so the zones are tight. Zone 1 is the 52-week closing low ($76.08, 25 Sep) with a volume shelf. The 1 Oct low ($74.41) sits between the zones. Zone 2 has no structure in the year, so it's a volatility band. NEE is 22% off its high on rates, not on earnings. It is a −9.5%-per-point rate name, so a 10-year breakout pushes it straight through these zones.

**NVDA.** Testing the 24 Sep low now. Zone 1 is a three-source level (11 Aug and 1 Sep lows, 21 Aug weekly close). Zone 2 is the **40-week average ($202)** with the May and July swing closes: the level where the 2026 uptrend would be tested. Below that, the 52-week closing low ($167.5) and the Dec/Feb closes ($176) would make a third zone around 14× forward earnings. At 11.4% of the book against a 9% target, NVDA isn't bought at Zone 1. A fall there brings the weight back toward target by itself.

**TSM.** Testing a volume shelf at $422–428, and pre-market on 15 Oct put it at ~$421, right on it. Zone 1 is a four-source floor (3 and 15 Sep lows, 28 Aug close). Zone 2 is the **40-week average ($395)** with the 24 Aug low and 17 Jul close. Below that, the next structure is the Jan/Mar weekly closes around $329. A beat-and-raise sold off is the textbook case for buying the gate on weakness.

**GOOGL.** The most-tested level on the map: $334–342 has 8 sources, including the 40-week average ($340.8) and four daily lows (20 Aug, 2 Sep, 24 Sep, 1 Oct). It's sitting 1.6% above it. If that breaks, there's a minor level at $324 (10 Sep low, 24 Jul close), then the Dec–Mar closes at $298–307. GOOGL's forward P/E (25×) is the highest of the core, and only Zone 2 brings it near 22×.

**UNP.** Zone 1: the 8 Oct low, the 25 Sep weekly close and a volume shelf. Zone 2: the 40-week average ($267.7), the 21 Sep and 1 Oct lows, and the May weekly closes. The early-September breakdown area ($289–293) is the first ceiling. A 21%-volatility anchor, so these zones are small moves.

**NU.** Testing the 40-week average ($14.55) and the August lows now (5 sources). Zone 1 has 6 sources (11 Aug and 16 Sep lows, Mar/Jul/Aug closes). Zone 2 is the 52-week closing low ($11.97) with the 30 Sep low: the panic low before the 5 Oct gap up on 180M shares. A 41%-volatility name, so it moves to its zones quickly.

**MCD.** At its 52-week closing low already, 32% off the high after the Investor Day sell-off. Zone 1 is that low ($231.89) with the 5 Oct low. **Below it there's no structure in the past year**, so Zone 2 is a volatility band. The 23 Sep gap ($242–250) is the ceiling. The dividend yield rises as the price falls, which is the valuation floor the chart can't show.

**NBIS.** Testing $175–183: the 40-week average ($174.6), the 7 Aug low ($180.6) and the 17 Jul close. That's your floor call, and the prediction's $175 test line sits at the bottom of it. **Zone 1 ($148–160) is the April–May 2026 weekly base** ($145–157 closes before the breakout to $220): the origin of the move, your $160, and 49% off the high. Zone 2 is the March–April base ($109–118). Loss-making, so no P/E check; the dilution check does that job. Ceilings: the 9–12 Oct range ($209–221, where your $215 sell limit sits), then $228–237 (your $230).

**AMD.** No support close by: the nearest level is $501 (a volume shelf), then Zone 1 ($451–488: the 14 Sep low and the Jun–Aug weekly closes, five sources). Zone 2 is the 40-week average ($395), which is also exactly 40% off the high. **Still 35× forward earnings at Zone 2**: a beaten-down AMD is not a cheap AMD.

**CEG.** Testing a six-source level ($264–271) now. Zone 1 is seven sources ($242–256: 21 and 30 Sep lows, the 52-week closing low area, three weekly closes). Zone 2 has no structure, so it's a volatility band at 45% off the high. CEG is being sold under the plan, so these zones only matter as a buy-back map after the exit, and only below the 25%-under-last-sale line.

**MU.** A double bottom at $888–903 (24 Aug and 14 Sep lows). Zone 1 has the 31 Jul close and the 6 and 11 Aug lows. Zone 2 is the 40-week average ($720). **The 4–5× forward P/E is a warning, not a bargain:** memory makers look cheapest at the top of their cycle, when forward earnings are at their peak. A low P/E on MU means "the market expects earnings to fall", the opposite of what it means on MCD.

**TLN.** Testing the 40-week average ($351). Zone 1: a volume shelf and the Feb/May/Jul weekly closes. Zone 2: the 52-week closing low ($292.3) with the 1 and 15 Sep lows and two weekly closes (five sources). Cheapest of the power names on earnings at every level.

**AVGO.** A floor tested four times at $336–343 (3 Sep, 16 Sep, 1 Oct and 14 Oct). A weekly close below $336 breaks it, and that is technically significant: the next stop is Zone 1 at the Jan–Feb closes (~$320). Zone 2 is the 52-week closing low ($300.7). January gate, so no buying before then whatever the price.

**QQQ.** Support at $700–709 (five sources: three daily lows in Aug–Sep, two June closes). Below that, **$684–688 is where the G+ half-trigger ($687) sits, on the 24 Jul weekly close**, so the rule and the chart agree. The 40-week average is $674.5 and the drawdown plan's −15% is $648.

## How the zones are used

The same zone means different things depending on the name's role:

| Role | Names | Zone 1 | Zone 2 |
|---|---|---|---|
| **Planned buys, below target** | TSM, NEE, GOOGL, UNP, NU, MCD | Sets the **entry limit** once the results gate has passed: a limit at the zone's top for 5 trading days, then market (the execution rule: no open-ended waiting). If the price is already inside or below the zone when the gate passes, buy at market | Can **pull the next planned tranche forward** (e.g. TSM's second half before 2 Nov), but **never ahead of a results gate** |
| **At or over target** | VST, NVDA | Nothing; a fall here brings the weight back to target by itself | Deploys **G+ cash only** (VST to 14%, NVDA to 11%) under the G+ rule. The −10% QQQ half-tranche goes to whichever G+ name is deepest into its zones |
| **Deep-value list** | NBIS, AMD, CEG (after the exit), MU, TLN | **Alert**: write the four checks. Capture only if the zone is ≥30% below the 52-week high (true for NBIS and CEG) | **Capture**: first tranche once the four checks pass (≤⅓ of the shield per name, shield ≥10% after, max two open). Second tranche two weeks later if the zone held on a weekly close |
| **January gate** | AVGO | Watch only | Watch only; the zones set the limit price once the January gate passes |

**Which zone captures for the deep-value list:** the first zone that is at least 30% below the 52-week high. NBIS → Zone 1 ($148–160, −49%; your $160 rule). CEG → Zone 1 (−36%). AMD → Zone 2 ($383–408, −40%). MU → Zone 2 ($698–743, −37%). TLN → Zone 2 ($283–302, −33%). This replaces the drawdown plan's flat "40% below the 52-week high" with each name's own level. The 30% floor is still there because zones only 7–15% below the price get touched most quarters (P(touch) 60–85% above), and a deep-value buy that fires every quarter isn't deep value, it's more AI exposure.

**Order of precedence:** results gate → rate rule (no captures in VST, CEG or NEE while the 10-year rule is active) → the drawdown plan's index tranches → G+ dip cash → zone captures.

## Weekly re-mapping (every Wednesday, at the review)

1. Refresh the daily data (50 sessions) and the weekly closes, and re-run both scripts.
2. **A zone breaks only on a weekly close** below its bottom edge, never on an intraday move. When it breaks:
   - the broken zone becomes the new **ceiling** (old support becomes resistance);
   - Zone 2 moves up to become Zone 1;
   - a new Zone 2 is drawn from the structure below, or a volatility band (−2 weekly standard deviations) if there's none.
3. **A ceiling breaks** after two weekly closes above it. It becomes the new Testing-now level, and the zones step up.
4. **A broken zone is a price event, not a thesis event.** Buying stops only if one of the four checks fails (thesis, dilution, results window, depth). Price alone never cancels a capture; a failed check always does.
5. Log every break and every capture in the week's review, with the zone it came from.

## Limits of this map

- **Support is where buyers showed up before, not a floor.** In a real 2018 or 2022, zones break one after another. That's why Zone 2 is two tranches, not one, and why the shield floor stays at 10%.
- **The data window is short:** 50 daily sessions (5 Aug–14 Oct) and one year of weekly closes. Older structure (multi-year highs and lows) isn't in it; where that matters (VST, NEE, MCD below their 52-week lows), the zones say "no structure" rather than pretend.
- **Weekly closes, not weekly lows,** for the year-long levels: intraday spikes below them aren't counted, so the real support may be a little lower.
- The zones come from the 14 Oct close. The 15 Oct moves (TSMC, CPI) aren't in them; the first refresh is Wed 21 Oct.

## Sources
Daily prices: stockanalysis.com history pages for each ticker (e.g. [NBIS](https://stockanalysis.com/stocks/nbis/history/), [NVDA](https://stockanalysis.com/stocks/nvda/history/), [TSM](https://stockanalysis.com/stocks/tsm/history/), [QQQ](https://stockanalysis.com/etf/qqq/history/)), saved in [`data/daily_2026-10-14/`](../data/daily_2026-10-14/). Weekly closes and forward P/E: [`data/weekly_closes_battles_2025-10-24_to_2026-10-09.csv`](../data/weekly_closes_battles_2025-10-24_to_2026-10-09.csv) and [`data/fundamentals_2026-10-13.csv`](../data/fundamentals_2026-10-13.csv).
