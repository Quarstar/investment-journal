# Capture zones · per-stock buy levels · first mapped 15 Oct 2026, re-mapped every Wednesday (latest: 21 Oct, 20 Oct closes)

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

## The map (20 Oct 2026 closes; first map 14 Oct)

| | Last | Vol | Testing now | **Zone 1** · first capture | Fwd P/E | P(touch) | **Zone 2** · capitulation | Fwd P/E | P(touch) | Ceiling | Next ceiling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **Power** | | | | | | | | | | | |
| VST | 150.32 | 43% | 146–150 | **132–141** (-6%, -32% off high) | 13.3 | 74% | **115–122** (-19%, -41%) | 11.6 | 34% | 154–155 | 164–169 |
| NEE | 78.86 | 18% | 77.3–77.7 | **75.4–76.7** (-3%, -22% off high) | 18.6 | 72% | **71.5–72.8** (-8%, -26%) | 17.6 | 36% | 84–84.4 | 87.6–87.6 |
| **Chips** | | | | | | | | | | | |
| NVDA | 216.47 | 33% | 212–218 | **204–210** (-3%, -15% off high) | 17.0 | 81% | **190–196** (-10%, -21%) | 15.9 | 53% | 219.6–221.1 | 230–234 |
| TSM | 425.08 | 28% | 422–428 | **406–417** (-2%, -16% off high) | 18.2 | 85% | **393–404** (-5%, -18%) | 17.6 | 69% | 440–446 | 486–487.5 |
| **Adopter** | | | | | | | | | | | |
| GOOGL | 340.28 | 33% | 334–342 | **319–328** (-4%, -19% off high) | 24.0 | 79% | **301–310** (-9%, -24%) | 22.6 | 56% | 352–359 | 400–401 |
| **Anchors** | | | | | | | | | | | |
| UNP | 287.61 | 21% | 285–286 | **272–278** (-3%, -12% off high) | 20.2 | 71% | **262–270** (-6%, -15%) | 19.5 | 52% | 289–293 | 306–314 |
| NU | 15.09 | 41% | 14.2–14.4 | **13.3–13.9** (-8%, -25% off high) | 14.2 | 67% | **11.7–12.4** (-18%, -33%) | 12.6 | 33% | 15.6–16.2 | 18–18 |
| MCD | 246.52 | 16% | 234–235 | **229–233** (-6%, -32% off high) | 17.4 | 46% | **218–222** (-10%, -36%) | 16.6 | 19% | 242–250 | 286–287 |
| **Deep-value list** | | | | | | | | | | | |
| NBIS | 171.45 | 94% | 160–168 | **148–160** (-7%, -49% off high) | n/m | 87% | **105–118** (-31%, -63%) | n/m | 47% | 175–183 | 209–221 |
| AMD | 534.74 | 62% | – | **451–488** (-9%, -29% off high) | 42.0 | 75% | **383–408** (-24%, -40%) | 35.4 | 40% | 606–620 | 648–658.5 |
| CEG | 258.84 | 47% | 250–256 | **242–250** (-3%, -37% off high) | 19.9 | 84% | **206–222** (-14%, -45%) | 17.3 | 51% | 264–271 | 286–301 |
| MU | 896.07 | 71% | 888–903 | **800–845** (-6%, -28% off high) | 4.9 | 85% | **698–743** (-17%, -36%) | 4.3 | 61% | 978–1003 | 1088–1108 |
| TLN | 349.43 | 53% | 349–356 | **324–344** (-2%, -23% off high) | 11.2 | 91% | **283–302** (-14%, -33%) | 9.8 | 57% | 374–391 | 436–436 |
| **January gate** | | | | | | | | | | | |
| AVGO | 334.37 | 45% | – | **314–325** (-3%, -28% off high) | 18.3 | 86% | **295–306** (-8%, -33%) | 17.2 | 67% | 336–343 | 357–368 |
| **Sandbox / watch** | | | | | | | | | | | |
| IREN | 26.62 | 102% | 25.6–27 | **20–22.5** (-16%, -72% off high) | n/m | 76% | **12–15** (-44%, -82%) | n/m | 31% | 28.8–30.5 | 34.8–36 |
| APLD | 19.33 | 74% | 17.6–18.4 | **15.5–17.2** (-11%, -50% off high) | n/m | 75% | **11.5–13.3** (-31%, -62%) | n/m | 34% | 20.1–20.4 | 26.9–27 |
| **Index** | | | | | | | | | | | |
| QQQ | 717.63 | 18% | 714–718 | **700–709** (-1%, -8% off high) | n/m | 84% | **684–688** (-4%, -10%) = the G+ half trigger | n/m | 61% | 722–723 | 744–752 |

Percentages in brackets: distance of the zone's top from the 20 Oct close, then of its middle from the 52-week high. Forward P/E at each zone uses the 13 Oct earnings snapshot (TSM's is therefore too high after the 15 Oct beat-and-raise). Names whose price is *inside* a band on 20 Oct: NVDA (testing 212–218), GOOGL (testing 334–342), MCD (ceiling 242–250), TLN (testing 349–356), IREN (testing 25.6–27.0); NBIS closed 3% above its new 160–168 demand zone, CEG 1% above its 250–256 test.

**Changes on 21 Oct (re-mapped on the 16 Oct weekly closes):** NVDA 219.6–221.1 broke → ceiling, zones step down a rung (Zone 1 204–210, Zone 2 190–196). GOOGL closed inside its old Zone 1 → that band is now "testing", Zone 1 319–328, Zone 2 301–310. NBIS 175–183 broke → ceiling; a new demand zone 160–168 from three successive session lows (163.36 / 163.27 / 160.25); Zone 1 148–160 unchanged. CEG 264–271 broke → ceiling; testing 250–256 (the 52-week closing low 250.55), Zone 1 242–250. AVGO 336–343 broke → ceiling; Zone 1 314–325. QQQ 722–723 broke → ceiling; Zone 1 700–709 was touched on 16 Oct (low 707.23) and held on the close (709.80). IREN and APLD added: both sit at or near 52-week lows with no structure beneath, so their lower zones are volatility bands, not support. Everything else unchanged.

## What each zone is built on, and the read (written 15 Oct on the 14 Oct closes; the levels that moved on 21 Oct are listed above)

**VST.** Testing $146–150 now: a volume shelf plus four weekly swing closes (Feb, Mar, Jun, Jul). Zone 1 is the strongest level on the map (8 sources): the 52-week closing low of $136.21 and three daily lows at $133–135 (24 Aug, 1 Sep, 30 Sep), a triple bottom. Below $136 there is **no price structure in the past year**, so Zone 2 is a volatility band that lines up with 40% off the high ($121). At Zone 2 VST would be 11.6× forward earnings for the merchant generator with the Nvidia-linked contracts. *Rate rule wins:* if the 10-year is above 5.50% at two reviews running, VST is being trimmed, and no VST capture is made until the rule switches off.

**NEE.** The low-volatility name, so the zones are tight. Zone 1 is the 52-week closing low ($76.08, 25 Sep) with a volume shelf. The 1 Oct low ($74.41) sits between the zones. Zone 2 has no structure in the year, so it's a volatility band. NEE is 22% off its high on rates, not on earnings. It is a −9.5%-per-point rate name, so a 10-year breakout pushes it straight through these zones.

**NVDA.** Testing the 24 Sep low now. Zone 1 is a three-source level (11 Aug and 1 Sep lows, 21 Aug weekly close). Zone 2 is the **40-week average ($202)** with the May and July swing closes: the level where the 2026 uptrend would be tested. Below that, the 52-week closing low ($167.5) and the Dec/Feb closes ($176) would make a third zone around 14× forward earnings. At 11.4% of the book against a 9% target, NVDA isn't bought at Zone 1. A fall there brings the weight back toward target by itself.

**TSM.** Testing a volume shelf at $422–428, and pre-market on 15 Oct put it at ~$421, right on it. Zone 1 is a four-source floor (3 and 15 Sep lows, 28 Aug close). Zone 2 is the **40-week average ($395)** with the 24 Aug low and 17 Jul close. Below that, the next structure is the Jan/Mar weekly closes around $329. A beat-and-raise sold off is the textbook case for buying the gate on weakness.

**GOOGL.** The most-tested level on the map: $334–342 has 8 sources, including the 40-week average ($340.8) and four daily lows (20 Aug, 2 Sep, 24 Sep, 1 Oct). It's sitting 1.6% above it. If that breaks, there's a minor level at $324 (10 Sep low, 24 Jul close), then the Dec–Mar closes at $298–307. GOOGL's forward P/E (25×) is the highest of the core, and only Zone 2 brings it near 22×.

**UNP.** Zone 1: the 8 Oct low, the 25 Sep weekly close and a volume shelf. Zone 2: the 40-week average ($267.7), the 21 Sep and 1 Oct lows, and the May weekly closes. The early-September breakdown area ($289–293) is the first ceiling. A 21%-volatility anchor, so these zones are small moves.

**NU.** Testing the 40-week average ($14.55) and the August lows now (5 sources). Zone 1 has 6 sources (11 Aug and 16 Sep lows, Mar/Jul/Aug closes). Zone 2 is the 52-week closing low ($11.97) with the 30 Sep low: the panic low before the 5 Oct gap up on 180M shares. A 41%-volatility name, so it moves to its zones quickly.

**MCD.** At its 52-week closing low already, 32% off the high after the Investor Day sell-off. Zone 1 is that low ($231.89) with the 5 Oct low. **Below it there's no structure in the past year**, so Zone 2 is a volatility band. The 23 Sep gap ($242–250) is the ceiling. The dividend yield rises as the price falls, which is the valuation floor the chart can't show.

**NBIS.** Testing $175–183: the 40-week average ($174.6), the 7 Aug low ($180.6) and the 17 Jul close. That's your floor call, and the prediction's $175 test line sits at the bottom of it. **Zone 1 ($148–160) is the April–May 2026 weekly base** ($145–157 closes before the breakout to $220): the origin of the move, your $160, and 49% off the high. Zone 2 is the March–April base ($109–118). Loss-making, so no P/E check; the dilution check does that job, and **it fails until ~22 Nov**: a $5.75B convertible closed on 24 Aug 2026, so the 90-day line rules out any NBIS capture before then, even inside Zone 1. Ceilings: the 9–12 Oct range ($209–221, where your $215 sell limit sits), then $228–237 (your $230).

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
