# Wednesday review checklist

Run every Wednesday. Verify; don't estimate. Commit the review as `weekly-reviews/YYYY-MM-DD.md`.

## 1. Money in
**Income from 28 Oct 2026: Outlier (remote AI-training work) only** (Gracey's ended 24 Oct; Greggs' final pay 29 Oct). Pay is variable and is **counted only once it has landed**, never forecast. **From 4 Nov (my money update): new contributions to the book are paused** until my cash priorities outside the book are met (the buffer first), then a small weekly amount while the driving fund fills (theory certificate expires 2 Dec 2026; a retake is expected), then the full goals amount. Living costs, the tax pot and bills come out of every payment first. **January's student finance** is the next real money: it goes into the book (after a one-month living-costs reserve) **only if the previous four weeks of Outlier pay hit my weekly target**; if not, it stays as reserve. Figures are in private records. Any new job is a situation trigger (adaptive rules, trigger 1), reviewed at the next Wednesday.
- [ ] Is this the first review after the 25th? If yes: pay received, living costs moved out first, the rest per the rules below. If no: skip to 2.
- [ ] Emergency fund (kept outside the portfolio) at its target? If not, refill it first.
- [ ] Cash shield at 15%+? If not, top it up before any buying.
- [ ] Any buy this week that wasn't in the queue? (24-hour rule, [adaptive rules](../plans/adaptive-rules.md)) Log it and say why

## 2. Verify every holding (core + defensive + sandbox)
For each one: price, % change since last review, news, valuation, dilution, next earnings date.
- [ ] Recompute weights from live prices across **all** accounts (Revolut general, Revolut ISA, Trading 212 ISA).
- [ ] Total exposure per stock across accounts, not per account.

## 3. Limits
- [ ] Core: 5 AI names max · Anchor sleeve: 3 names / 15% max (one in, one out), rising to 4 / 20% only when the switch triggers
- [ ] Each anchor still passes the diversification test (beta < 0.8, corr. NVDA < 0.5, falls less than the Nasdaq in bad weeks). Proposed 28 Oct, not adopted: worst single week no worse than −10% (NU passed all three and fell 17% in a day)
- [ ] Single stock ≤ 20%
- [ ] Energy/nuclear ≤ 35% · Neocloud ≤ 15%
- [ ] Sandbox ≤ 5%
- [ ] Cash shield ≥ 15%
- [ ] AI-linked share of the book: ____% (target ~41% under F, ~47% under G+)
- [ ] Income still Outlier only? Keep the 12 Oct risk-down targets. New job started? Review them (see the [target portfolio](../plans/target-portfolio.md))

## 4. Plans committed in advance
- [ ] Drawdown plan: QQQ vs its 52-week high ($762.86, the 6 Oct intraday high; highest close $759.66). Any trigger hit (−10% G+ half / −15 / −25 / −35%)? → [plan](../plans/2026-10-10-drawdown-plan.md)
- [ ] Concentration plan: phase status → [plan](../plans/2026-10-10-concentration-plan.md)
- [ ] Option F in progress (G decided 14 Oct, TSM raised to 12% on 15 Oct): exits and gates per the [limit-order sheet](../trades/limit-orders-2026-10-14.md); G+ cash held for a dip: QQQ −10% (~$687) → half into G+ names, deepest into their capture zones first; −15% ($648) → drawdown plan; time stop at the first review after the January student finance; nothing before the first full pay unless a dip trigger fires
- [ ] NBIS carry: kill line measured from the share count in the **12 Nov** release (re-based 4 Nov) · weight inside 3–7%? Price in Zone 1 (re-mapped weekly: 105–118 from 4 Nov; 148–160 is now "testing") with all four checks passed (not before ~22 Nov) → buy towards 7%; at $205+ → trim to 5%; any kill criterion hit (share count +15% yoy, backlog shrinking, a major customer cutting) → slot to 0
- [ ] VST/CEG ratio (while CEG is still held): above ~0.62 favours CEG, below ~0.48 favours VST

## 5. Watchlist and gates
- [ ] Gates (Option G, from 14 Oct; V and SOFI added 27 Oct): V 27 Oct **passed** (adj. EPS $3.48 vs $3.44, FY27 guide low double digits) · TSM 15 Oct **passed** (top-up in two halves, see the [order sheet](../trades/limit-orders-2026-10-14.md)) · NEE 21 Oct **passed** (adj. EPS $1.24 vs $1.19; 2026 high end and 8%+ reaffirmed; backlog 36.7 GW): CEG first half on a $266 limit to 6 Nov, NEE bought the day it fills · UNP 22 Oct **passed** (adj. EPS $3.53 vs $3.47, revenue +15%, guidance held; buy after the shield ≥15%, behind GOOGL) · GOOGL 28 Oct **passed** (two flags: dilution, role drift) · NOW sold 28 Oct before its print · MCD 4 Nov (to score) · ARM 4 Nov (watch list; bar in the 4 Nov review §5) · MP 5 Nov ([thesis](../theses/MP.md)) · IREN 5 Nov ([neocloud page](../theses/NEOCLOUD.md)) · IONQ 5 Nov (no gate; [thesis](../theses/IONQ.md)) · DUK 5 Nov (NEE's alternate) · VST 6 Nov · **NBIS Thu 12 Nov before the open (confirmed)** · NU 12 Nov · NVDA Tue 17 Nov · AVGO (January)
- [ ] BWXT fails the anchor test (13 Oct: bad weeks −4.2% vs the index's −3.1%); watchlist only. UBER passes in only 54% of resampled years; not an anchor
- [ ] Third anchor MCD (4 Nov); fourth slot stays open until the switch, re-battled then with RTX, Rolls-Royce, Dominion and any new sectors
- [ ] [Capture zones](../plans/capture-zones.md): refresh the daily data, re-run `capture_zones.py` and `capture_zones_final.py`. Any weekly close below a zone (re-map: broken zone → ceiling) or above a ceiling twice (step up)? Any name inside a zone → act per its role (entry limit / G+ cash / deep-value capture / watch)
- [ ] Deep-value list ([drawdown plan](../plans/2026-10-10-drawdown-plan.md)): any name inside its capture zone (the first zone ≥30% off its high)? All four checks written down before any order
- [ ] The switch (anchors 15% → 20%, funded from the AI shave, VUKG stays ~6%): sleeve full, two good quarters each, every anchor still passing the test? Only then.
- [ ] Anything new must replace a core name, or go in the sandbox
- [ ] [Watch items](../plans/watch-items.md): any Terafab milestone hit? RBLX gate (29 Oct): bookings bottoming, Q4 guide back to growth, FCF margin holding?
- [ ] VST edge check: forward P/E gap to CEG, and VST's correlation with NVDA
- [ ] Re-run the [risk-adjusted ranking](../plans/2026-10-17-risk-adjusted-ranking.md) with the week's prices (`analysis/risk_adjusted_ranking.py --prices <file>`); when two buys are ready at once, the higher-ranked goes first

## 5b. Build-out → adopter transition (added 12 Oct 2026)
History says the handover from AI suppliers to AI adopters usually comes through a crash. Track these each week:
- [ ] **Hyperscaler capex growth slowing** for two quarters in a row (the growth rate, not the total)
- [ ] **GPU rental prices falling** steadily (a sign of overbuilt capacity)
- [ ] **Neocloud or AI-lab funding pulled, delayed or repriced** (e.g. Firmus scrapped its IPO, Oct 2026)
- [ ] **AI-lab revenue missing what was signalled** (e.g. OpenAI ~$50B vs ~$70B signalled)

**Rule:** if **2 of the 4** have flipped, move one more core supplier slot to a profitable adopter at the next review, one in, one out, with the reason written down. Status on 12 Oct: early cracks in funding and lab revenue, demand still strong; 0 confirmed, 2 to watch. **21 Oct: 1 confirmed (funding repriced: CoreWeave bonds ~15%, Firmus IPO pulled), 1 to watch (OpenAI run-rate vs signal); GPU rental prices rising (signal 2 off); capex signal tested by Meta 21 Oct (**not flipped**: 2026 narrowed up to $135–145B, 2027 "aggressive", no number; FCF negative), MSFT/GOOGL 28 Oct, AMZN 29 Oct — decision point 4 Nov.** **4 Nov: unchanged, 1 confirmed, 1 to watch.** Capex not cut by any of the four (AMZN ~$220bn held; Alphabet 2027 "increase significantly"; MSFT trimmed 2026 on supply delays, not demand). Hyperscaler self-funding (Meta, Alphabet share sales) is recorded under signal 3, not as a fifth signal.

## 5b2. Rotation gauge (added 15 Oct 2026)
Is money leaving AI/tech for the rest of the market? Checked weekly, as **4-week relative performance** at Tuesday's close:
- [ ] **RSP vs QQQ** (equal-weight S&P 500 vs Nasdaq-100): is the average stock beating the tech giants?
- [ ] **XLP vs XLK** (consumer staples vs tech) and **XLY vs XLK** (consumer discretionary vs tech)
- [ ] **Breadth:** NYSE new 52-week highs vs new lows that week

**Rule:** if RSP and at least one of XLP/XLY beat their comparison over 4 weeks at **three reviews running**, the rotation is confirmed. Then: MCD moves up the buy queue (still only after its results gate), and the fourth anchor slot is re-battled with consumer names first (COST, the preferred candidate, plus whichever consumer names lead). Staples leading means the rate-proof half is winning; discretionary leading means consumers are spending, so it matters which one. Status on 15 Oct: one day of rotation (Dow up, Nasdaq down); 0 of 3. **21 Oct: 1 of 3** (4 weeks to 20 Oct: RSP +1.4% vs QQQ −4.0%; XLP +6.1% and XLY +2.8% vs XLK −5.5%; staples leading). **28 Oct: 2 of 3** (4 weeks to 27 Oct: RSP +3.8% vs QQQ −2.3%; XLP +6.5%, XLY +5.8% vs XLK −2.6%). **4 Nov: 3 of 3, confirmed** (4 weeks to 3 Nov: RSP +3.3% vs QQQ −9.8%; XLP +8.7%, XLY +5.0% vs XLK −12.6%). Consequences: MCD up the queue after its gate; the fourth-anchor re-battle (consumer names first, COST preferred) runs at the first review after the January student finance.

## 5c. Predictions
- [ ] Any call in the [predictions log](../predictions.md) past its deadline? Score it (full / half / miss) and update the scoreboard
- [ ] [My picks vs the plan](../shadow-portfolio.md): add the week's row (both books, QQQ, worst falls) at Tuesday's close. Verdicts only at 13 Jan, 14 Apr and 13 Oct 2027

## 6. Swing trades
- [ ] Open trades: stop still placed as a real order? Time stop or earnings date within the next week?
- [ ] Close and log any finished trade in [`swing-log.md`](../trades/swing-log.md)

## 6b. Adaptive rules ([rules](../plans/adaptive-rules.md))
- [ ] Did any of the five triggers fire this week? (situation, 2-of-4 signals, drawdown, gate, drift beyond 3 points)
- [ ] If yes: change the target, within the 5%-per-review limit, and add a row to the change log
- [ ] If no: targets stay the same, whatever the news says

## 7. Write it down
- [ ] Decisions and the reason for each
- [ ] Commit
