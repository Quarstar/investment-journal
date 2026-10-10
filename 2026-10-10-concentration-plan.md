# Concentration plan · written 10 Oct 2026

> Decided on a Saturday, executed at the Wednesday review (14 Oct onward), so the trades follow the process instead of a mood.

## The problem
My profit has come from a few conviction positions held for months: NBIS, AMD, NVDA, NOW, IREN. My losses have mostly come from small, off-thesis positions I never sized up: 2024 micro-caps, XOS, TNON, IGMS, SGML. See the [track record](../trades/track-record.md).

As at 7 Oct 2026 the book looked like this:

| Group | Weight | Holdings |
|---|---|---|
| Core AI bottlenecks | ~51% | NVDA 11.6, CEG 11.7, VST 11.2, NBIS 10.1, TSM 6.4 |
| Defensive | ~26% | Cash 10.7, XLVP 8.3, VUKG 6.7 |
| Tail | ~22% | AVAV 5.9, MP 4.8, CELH 4.8, NOW 4.1, GRAB 2.5, other 1.2 |

The tail holds six names that are each too small to matter, yet each takes research time every week.

## Target structure

| Layer | Target | Holdings |
|---|---|---|
| Core | ~60% | Up to 5 AI names: NVDA, TSM, CEG, VST, NBIS. AVGO competes for a slot from January if its gate is met. |
| Anchor sleeve (non-AI) | ≤ 15% | Up to **3** stocks, one per sector, each outside the AI thesis and each passing the diversification test below: **UBER** (transport), **NU** (financials), **MCD** (consumer, candidate) |
| Defensive | ~25–30% | Cash shield (15% floor), XLVP, VUKG |
| Sandbox | ≤ 5% | Swing trades (logged in advance) and frenzy-bucket ideas |

Existing caps still apply: 20% single stock, 35% energy/nuclear, 15% neocloud.

**Two things I'm accepting knowingly:**
1. **Five AI names are one bet, not five.** They fall together if AI capex slows. VST and CEG especially (identical −25.6% over the year, 0.81 daily correlation). I hold both deliberately as a pair and use the ratio as a tie-breaker for new money.
2. **More AI exposure means a bigger hit in a crash.** Moving to this structure takes AI-linked holdings from ~55% to ~70% of the book. A 30% fall in those names would then cost ~21% instead of ~17%. The defensive layer and the [drawdown plan](2026-10-10-drawdown-plan.md) are what make that acceptable.

## Phase 1 · Wednesday 14 Oct review
Sell the names that don't fit the AI-bottleneck thesis:

| Sell | Weight | Reason |
|---|---|---|
| CELH | ~4.8% | Consumer energy drinks, outside the thesis; repeated growth misses |
| GRAB | ~2.5% | Southeast Asia super-app, outside the thesis |
| LVMH (MC) | ~0.1% | Reward share, no thesis |

Proceeds (~7.4%) go to the **cash shield**, taking it from ~10.7% to ~18%. That clears the 15% floor. The ~3% above 15% is reserved for the UBER anchor position after its 4 Nov results (below), or otherwise deployed only under the drawdown plan or the normal gates.

Execution: limit orders during US hours, sell into a green day where possible, and confirm fills before recomputing weights.

## Phase 2 · by Wednesday 4 Nov
NOW, MP and AVAV each keep their place only if I can write a one-page thesis for it using the [template](../theses/_template.md), with a clear sell trigger.

| Name | Weight | Question it has to answer |
|---|---|---|
| NOW | ~4.1% | Is enterprise AI software a bottleneck, or the app layer my thesis avoids? (Strongest case to keep: +49.9% and +47.5% trades.) |
| MP | ~4.8% | Are rare-earth magnets a real AI/robotics bottleneck, or a separate theme? |
| AVAV | ~5.9% | Does a defence sleeve still belong, or is it diluting the core? |

Any name without a finished thesis page by 4 Nov is sold into a green day.

## Watchlist clean-up
| Name | Decision |
|---|---|
| AVGO | **Keep.** Custom AI chips fit the thesis. Gate: January. |
| UBER | **Promoted to anchor sleeve.** See below. |
| NU | **Promoted to anchor sleeve.** See below. |
| MCD | **Added 10 Oct as the consumer anchor candidate.** See below. |
| GRAB top-up | Remove. Position being sold. |
| SOFI | Remove. Outside the thesis. |
| BWXT | Keep as an alert only. Nuclear fits the thesis, but a sixth core name would need one to leave. |

## Anchor sleeve (non-AI)
**Purpose:** reduce my dependence on AI spending with businesses that move differently from it. These are diversifiers, not safe havens: they're still volatile stocks (UBER 30%, NU 40% annualised volatility vs 18% for the Nasdaq-100). Protection in a crash comes from the defensive layer.

**Rules**
- Maximum **3 names**, one per sector, **15% of the book in total**.
- Health care and the UK are already covered by XLVP and VUKG, so no single stocks there.
- Every anchor must pass the **diversification test** on at least a year of weekly data:
  - beta to the Nasdaq-100 below 0.8
  - correlation with NVDA below 0.5
  - falls less than the Nasdaq-100 on average in its 10 worst weeks
- Plus the usual: a one-page thesis with sell triggers, and a buying gate written in advance.

| Anchor | Sector | Beta | Corr. NVDA | Nasdaq's 10 worst weeks (index −3.1%) | Passes |
|---|---|---|---|---|---|
| UBER | Transport | 0.69 | 0.24 | −2.4% | ✅ |
| NU | Financials | 0.57 | 0.07 | −1.5% | ✅ |
| MCD (candidate) | Consumer | 0.04 | −0.12 | −0.6% | ✅ |
| CELH (sold) | Consumer | 1.47 | – | −7.4% | ❌ |
| GRAB (sold) | Consumer tech | 1.34 | – | −4.1% | ❌ |

### UBER
**Why UBER and not CELH or GRAB:** over the past year of weekly data, UBER had a beta of 0.69 to the Nasdaq-100 and a 0.24 correlation with NVDA, and in the Nasdaq's 10 worst weeks it averaged −2.4% (index −3.1%). CELH (beta 1.47, −7.4%) and GRAB (beta 1.34, −4.1%) fell harder than the AI names they were meant to offset.

**Gate (written before the event):** Q3 results on **Wed 4 Nov 2026, before the US open**. Buy only after the print, and only if:
- [ ] Gross bookings growth stays in the high teens or better (Wells Fargo models ~20% ex-FX for Q4)
- [ ] Q4 guidance isn't cut
- [ ] No large new share issuance
- [ ] The stock holds above its 52-week low ($65.41) after the print

**Size:** start at ~3% (funded from the shield's excess above 15%), building to ~6% only on a second good quarter. Thesis page: [theses/UBER.md](../theses/UBER.md).

### NU
**Why NU:** Brazil-led digital bank with record Q2 2026 profit ($1.06B, +49%), revenue +39%, ROE 33%, ~17× forward earnings. Lowest correlation to my AI book of anything I've tested (0.07 with NVDA).

**Not buying the spike.** NU rose ~20% in the week of 5 Oct on a Brazilian election result. That's a political move, not a business one.

**Gate (written before the event):** buy only after its **Q3 2026 results** (date to confirm, likely mid-November; Q2 was reported 13 Aug), and only if:
- [ ] The 90+ day overdue-loan ratio is stable or improving (6.9% in Q2)
- [ ] Risk-adjusted net interest margin holds near Q2's 12.4%
- [ ] Customer growth continues (138.9M in Q2) with no large new share issuance
- [ ] Brazilian election uncertainty has passed

**Size:** start at ~3%, funded from wages once the shield is at 15%, or from the January student finance. Build to ~5% only on a second good quarter. Thesis page: [theses/NU.md](../theses/NU.md).

### MCD (candidate, added 10 Oct)
**Why MCD:** the consumer slot opens when CELH is sold, and MCD is the first consumer name to pass the test, by the widest margin yet: beta 0.04, correlation with NVDA −0.12, and −0.6% in the Nasdaq's 10 worst weeks (up in 5 of them). Lower volatility than the Nasdaq itself (17% vs 18%). ~17× forward earnings, ~3.3% yield, 50 straight years of dividend rises.

**The catch:** it fell ~32% from its high in a year the Nasdaq rose. US sales are weak (Q2 US comps +0.8% on price, visits down; management expects Q3 slightly negative), and Investor Day on 23 Sep added ~$8.5B of franchisee support costs. A low-correlation stock can still lose money on its own schedule.

**Not a reason to buy:** the "institutions are quietly buying before a crash" story. 13F holdings as of 30 Sep aren't public until mid-November, and the filings so far are small advisers trading both ways.

**Gate (written before the event):** Q3 results, **expected Wed 4 Nov 2026, before the US open** (confirm). Buy only after the print, and only if:
- [ ] US comparable sales are no worse than "slightly negative", as guided at Investor Day
- [ ] Management says October/Q4 traffic is improving as the value menu settles
- [ ] The operating-margin target (low-to-mid 50s% by 2030) and the dividend are both reaffirmed
- [ ] The stock holds above its 52-week low ($229.20) after the print

If Q3 misses the gate, wait for Q4 results (around February) rather than averaging down.

**Size:** start at ~3%, up to ~4% max. UBER (6%) + NU (5%) + MCD (4%) fills the 15% sleeve exactly. Funded only after UBER and NU, and only from new money once the shield is at 15%. Same results morning as UBER: decide each gate separately. Thesis page: [theses/MCD.md](../theses/MCD.md).

## Rule going forward
**One in, one out.** Core is capped at 5 AI names and the anchor sleeve at 3 names / 15%. A new name in either can only come in by removing one, at a Wednesday review, with the reason written down.
