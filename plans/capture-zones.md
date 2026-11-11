# Capture zones · per-stock buy levels · first mapped 15 Oct 2026, re-mapped every Wednesday (latest: 11 Nov, 10 Nov closes)

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

## The map (10 Nov 2026 closes, re-mapped on the 6 Nov weekly closes; first map 14 Oct)

| | Last | Vol | Testing now | **Zone 1** · first capture | Fwd P/E | P(touch) | **Zone 2** · capitulation | Fwd P/E | P(touch) | Ceiling | Next ceiling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **Power** | | | | | | | | | | | |
| VST | 131.18 | 43% | 124–131 | **115–122** (-7.0%, -41.2% off high) | 11.6 | 71% | **106–112** (-14.6%, -45.9%) | 10.7 | 46% | 136–141 | 146–150 |
| NEE | 86.27 | 19% | 81.9–82.1 | **79.2–80.6** (-6.6%, -17.6% off high) | 19.5 | 44% | **75.4–76.7** (-11.1%, -21.6%) | 18.6 | 19% | 84–84.4 | 87.6 |
| **Chips** | | | | | | | | | | | |
| NVDA | 168.89 | 34% | 165–173 | **152–162** (-4.1%, -35.5% off high) | 12.9 | 77% | **137–146** (-13.6%, -41.9%) | 11.6 | 38% | 173–179 | 192–199 |
| TSM | 396.48 | 31% | 393–404 | **373–387** (-2.4%, -22.0% off high) | 16.8 | 83% | **342–360** (-9.2%, -28.0%) | 15.5 | 51% | 406–417 | 422–428 |
| **Adopter** | | | | | | | | | | | |
| GOOGL | 287.38 | 36% | 271–280 | **255–265** (-7.8%, -35.1% off high) | 19.3 | 62% | **227–237** (-17.5%, -42.1%) | 17.2 | 28% | 301–310 | 319–328 |
| **Anchors** | | | | | | | | | | | |
| UNP | 300.62 | 22% | 285–286 | **272–278** (-7.5%, -11.3% off high) | 20.2 | 45% | **262–270** (-10.2%, -14.2%) | 19.5 | 30% | 289–293 | 306–314 |
| V | 423.0 | 20% | 397–402 | **375.3–382.7** (-9.5%, -8.6% off high) | 26.0 | 30% | **356.1–363.5** (-14.1%, -13.2%) | 24.7 | 12% | 407–410 | 414.6 |
| MCD | 282.17 | 18% | 234–235 | **229–233** (-17.4%, -32.3% off high) | 17.4 | 4% | **218–222** (-21.3%, -35.5%) | 16.6 | 1% | 242–250 | 286–287 |
| NU | 12.08 | 48% | – | **10.9–11.7** (-3.1%, -37.4% off high) | 11.8 | 86% | **9.5–10.3** (-14.7%, -45.1%) | 10.4 | 51% | 14.2–14.4 | 15.6–16.2 |
| **Weapons** | | | | | | | | | | | |
| NBIS | 134.0 | 97% | 125–135 | **105–115** (-14.2%, -63.3% off high) | n/m | 76% | **80–90** (-32.8%, -71.7%) | n/m | 46% | 148–160 | 168–175 |
| SOFI | 16.37 | 53% | 15.67–16.02 | **15.25–15.84** (-3.2%, -52.5% off high) | n/m | 86% | **13.86–14.6** (-10.8%, -56.5%) | n/m | 65% | 16.55–17.14 | 18.3–18.4 |
| **Deep-value list** | | | | | | | | | | | |
| AMD | 515.21 | 64% | – | **451–488** (-5.3%, -28.7% off high) | 42.0 | 84% | **383–408** (-20.8%, -39.9%) | 35.4 | 48% | 606–620 | 648–658.5 |
| CEG | 267.76 | 47% | 250–256 | **242–250** (-6.6%, -36.8% off high) | 19.9 | 74% | **206–222** (-17.1%, -45.0%) | 17.3 | 42% | 264–271 | 286–301 |
| MU | 725.11 | 76% | 800–845 | **734–784** (8.1%, -33.1% off high) | 4.5 | 100% | **564–615** (-15.2%, -48.0%) | 3.5 | 67% | 888–903 | 978–1003 |
| TLN | 361.18 | 52% | 334–344 | **302–321** (-11.1%, -28.6% off high) | 10.4 | 64% | **283–297** (-17.8%, -33.5%) | 9.7 | 45% | 349–356 | 374–391 |
| **January gate** | | | | | | | | | | | |
| AVGO | 331.98 | 46% | – | **314–325** (-2.1%, -28.5% off high) | 18.3 | 88% | **295–306** (-7.8%, -32.7%) | 17.2 | 70% | 336–343 | 357–368 |
| **Sandbox / watch** | | | | | | | | | | | |
| IREN | 19.73 | 90% | 20–22.5 | **15–17.5** (-11.3%, -78.9% off high) | n/m | 79% | **9.7–12.6** (-36.1%, -85.5%) | n/m | 35% | 23.7–24.5 | 25.6–27 |
| APLD | 16.68 | 68% | 17.6–18.4 | **15.5–17.2** (3.1%, -47.6% off high) | n/m | 100% | **11.5–13.3** (-20.3%, -60.3%) | n/m | 51% | 20.1–20.4 | 26.9–27 |
| **Index** | | | | | | | | | | | |
| QQQ | 674.76 | 20% | 645–665 | **604–622** (-7.8%, -19.6% off high) | n/m | 38% | **562–596** (-11.7%, -24.1%) | n/m | 19% | 680–690 | 700–709 |

Percentages in brackets: distance of the zone's top from the 27 Oct close, then of its middle from the 52-week high. Forward P/E at each zone uses the 13 Oct earnings snapshot (TSM's is therefore too high after the 15 Oct beat-and-raise). Percentages from the 10 Nov close. Re-mapped this week: VST, NVDA, TSM, NBIS, IREN, QQQ. **Not re-mapped (ranking or watch only, flags stand):** MU, AMD, AVGO, CEG, APLD; next run.

**Changes on 11 Nov (re-mapped on the 6 Nov weekly closes, prices to 10 Nov).** Same rule as 4 Nov: the broken band becomes the first ceiling, the band the price sits in becomes "testing".
- **VST** 136–141 broke (124.80, a new 52-week closing low) → ceiling. Testing 124–131. Zone 1 115–122 (11.6×), Zone 2 106–112 (the 110.89 swing, 10.7×). After results (6 Nov) it closed back at 131.18, the top of testing.
- **NVDA** 204–210 and 192–199 broke (186.64), and the 10 Nov close (168.89) sat under the old Zone 2 → 173–179 is now the first ceiling. Testing 165–173: the 52-week lows (164.27 intraday, 167.52 close). **No structure below**: Zone 1 152–162 (12.9×) and Zone 2 137–146 (11.6×) are volatility bands. For reference only, one analyst's "CEO leaves" scenario is ~$118–127.
- **TSM** 406–417 broke (375.44, inside the old Zone 2, which held) → ceiling. Testing 393–404 (the 40-week average, 402.2). Zone 1 373–387 (16.8×), Zone 2 342–360 (the 351.19 swing, 15.5×).
- **NBIS** 148–160 broke (129.49) → ceiling. Testing 125–135. Zone 1 105–115 (the 107.06 cluster), Zone 2 80–90 unchanged.
- **IREN** 23.7–24.5 broke (21.64) → ceiling. Testing 20–22.5 (10 Nov close 19.73, the 52-week closing low, just under it). Zone 1 15–17.5, Zone 2 9.7–12.6 (volatility bands).
- **QQQ** 680–690 broke (656.10) → ceiling. Testing 645–665 holds the 5 Nov close (647.05) and the −15% line ($645.71, highest-close measure). Zone 1 604–622 (weekly swing closes, ~−19%). Zone 2 562–596: the 52-week low, and it contains the −25% line ($569.75).
- **Second Friday above (13 Nov) would step up:** NEE, MCD, V.

**Changes on 4 Nov (re-mapped on the 30 Oct weekly closes, prices to 3 Nov).** The AI leg down broke nine testing bands on one Friday close. Rule applied the same way to each: the broken band becomes the first ceiling, the band the price now sits in becomes "testing", and the zones below are re-drawn from the script's levels (where it finds no structure, a volatility band, said so).
- **VST** 146–150 broke (138.37) → ceiling. Testing 136–141: the 52-week closing low (136.21) with seven sources agreeing, the strongest level on the map. Nothing structural below, so Zone 1 is a volatility band, 124–131 (12.5×); Zone 2 115–122 unchanged.
- **NVDA** 212–218 broke (204.64) → ceiling. Testing 204–210 (the 40-week average, 204.15). Zone 1 192–199 (16.1×) and Zone 2 173–179 (14.5×): weekly swing-close clusters.
- **TSM** 422–428 broke (406.13) → ceiling. Testing 406–417. Zone 1 393–404 (17.6×; the 40-week average 401.1 and the 399.75 swing), Zone 2 373–387 (a volatility band).
- **GOOGL** 319–328 and 301–310 both broke (279.84) → ceilings. Testing 271–280 (last week's Zone 2). Zone 1 255–265 (19.3×; the 52-week closing low 259.92), Zone 2 227–237 (17.2×, a volatility band).
- **NBIS** 168–175 broke (154.14) → ceiling. Testing 148–160 (the 2 Nov close of 141.39 sat under it; not a weekly close). Zone 1 105–118 (last week's Zone 2), Zone 2 80–90 (the 85.2 cluster).
- **QQQ** 714–718 and 700–709 broke (690.49) → ceilings. Testing 680–690 (the 40-week average 680.4; the −10% line 686.57 sits inside). Zone 1 648–665 starts at the −15% drawdown line ($648.43). Zone 2 606–621 (weekly swing closes, ~−20%).
- **IREN** 25.6–27 broke (23.95, the 52-week closing low) → ceiling. Testing 23.7–24.5 (the 52-week lows). Zones unchanged; the 2 Nov close (22.02) was inside Zone 1.
- **MU** 888–903 broke (884.74) → ceiling; testing 800–845; Zone 1 734–784 (the 40-week average); Zone 2 564–615. **TLN** 349–356 broke (343.12) → ceiling; testing 334–344; Zone 1 302–321; Zone 2 283–297. Ranking names only.
- **Not stepped up yet:** UNP (304.00), MCD (258.12) and V (413.59) closed above their first ceilings on 30 Oct for the first time; a second Friday close above steps each map up. NEE closed inside its first ceiling (83.71 vs 84.0–84.4).

**Changes on 28 Oct (re-mapped on the 23 Oct weekly closes, prices to 27 Oct):** **GOOGL** 334–342 broke (weekly close 320.21) → ceiling; the price is inside 319–328, which becomes "testing"; Zone 1 is now 301–310 (22.6×), Zone 2 271–280 (20.4×, the 40-week-low cluster). **NEE** rallied off the old Zone 1 after its results (82.42): new shelf 81.9–82.1 (the 22–26 Oct closes), Zone 1 79.2–80.6, the old Zone 1 75.4–76.7 becomes Zone 2. **NBIS** closed below the 160–168 demand zone on 23 Oct (158.74), tested Zone 1 on 26 Oct (low 149.48, $1.48 above the $148 buy) and reclaimed it on 27 Oct (170.47, +11%); a Friday close above 168 restores 160–168 as support. **IREN** closed below 25.6–27 on 23 Oct (24.91), set a new 52-week low (23.72) on 26 Oct and reclaimed the band on 27 Oct; bands unchanged. **NU** gapped through both zones on the Brazil runoff (26 Oct, −17%); volatility bands only, watch only since V replaced it. **Added: SOFI** (weapon; results gap 14.46 → 16.40 on 160M shares on 27 Oct): testing 15.67–16.02 (the gap's top), Zone 1 15.25–15.84 (the early-October shelf), Zone 2 13.86–14.60 (gap filled, the 52-week low). Forward P/E isn't in the 13 Oct snapshot; on the company's ~$0.90 2027 EPS outlook, Zone 1 is ~17× and Zone 2 ~16×. Volatility is the 50-session daily figure (53%), since only ten weekly closes are on file. **Added: V** (financial anchor): testing 397–402, Zone 1 375.3–382.7 (26.0×, the September swing lows and the volume shelf), Zone 2 356.1–363.5 (24.7×, the 40-week-average cluster), ceiling the 22 Oct record 414.60. **Not yet stepped up:** UNP (299.88) and MCD (249.47) both closed inside their first ceilings on 23 Oct (292.87, 248.46); one more Friday close above 293 / 250 steps the map up. AVGO (342.33) is inside its 336–343 ceiling. Everything else unchanged.

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
