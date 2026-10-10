# Track record: all accounts, May 2024 – Oct 2026

> **Backfilled from official broker statements on 9 Oct 2026.** Git timestamps show when these trades were *uploaded*, not when they were *made*. From October 2026, every trade is logged in [`swing-log.md`](swing-log.md) **before** entry. Returns only, no £/$ amounts, by design. Raw statements stay private.

**127 closed round trips across three accounts:**

| Account | Period covered | Round trips | Win rate | Avg return / trade | Avg win / avg loss | Profit factor | Detail |
|---|---|---|---|---|---|---|---|
| Revolut general | May 2024 – Oct 2026 | 87 | 53% | +1.8% | +14.0% / −11.9% | 6.7 | [table](history-revolut-general.md) |
| Revolut Stocks & Shares ISA | Nov 2025 – Oct 2026 | 26 | 62% | +10.6% | +21.1% / −6.1% | 4.5 | [table](history-revolut-isa.md) |
| Trading 212 Stocks ISA | Jun – Oct 2026* | 14 | 50% | +2.4% | +13.0% / −8.2% | 1.1 | [table](history-t212-isa.md) |
| **All accounts** | | **127** | **54%** | **+3.7%** | **+15.6% / −10.5%** | | |

*Trading 212 statement period. Positions still open (e.g. CEG, MP, NBIS, TSM) aren't counted until they're closed. Profit factor = total won ÷ total lost, calculated per account because the accounts are in different currencies.

## The pattern that matters: holding period

| Held | Trades | Win rate | Avg return | Median return |
|---|---|---|---|---|
| ≤ 1 week | 33 | 33% | −0.7% | −3.1% |
| 1 week – 1 month | 42 | 55% | +2.9% | +0.7% |
| 1 – 3 months | 35 | 66% | +3.1% | +5.3% |
| > 3 months | 17 | 71% | **+15.3%** | +8.7% |

**The longer I held, the better I did, at every step.** My quick trades lose money on average. My multi-month conviction positions are where nearly all the edge is.

## By year

| Year opened | Trades | Win rate | Avg return |
|---|---|---|---|
| 2024 | 30 | 23% | −7.4% |
| 2025 | 53 | 75% | +9.9% |
| 2026 | 44 | 50% | +3.7% |

2024 was the learning year: tiny orders, fees, random names. 2025 was a strong AI bull market, so I can't separate skill from tide there. 2026 is the most honest test so far, positive but modest.

## Biggest results
- **Best:** NBIS +84.5% (ISA, Mar → Oct 2026), RIOT +87.5% (2024), NBIS +53.4% (Aug → Oct 2025), NOW +49.9% (Jul → Sep 2026), IREN +47.7% (Dec 2025 → Jan 2026).
- **Worst:** a −100% micro-cap in 2024 (2U, bankruptcy), IGMS −63.8% (2024), IONQ −29.1% (2026, see below).

## Lessons that changed my rules
1. **My edge is conviction position trades in AI leaders, not fast swings.** The swing sleeve stays sandbox-sized until a pre-logged record proves otherwise.
2. **Same stock, same crash, opposite results.** In early 2026 IONQ fell roughly 40%. In my ISA I kept most of the position and sold into the May–June rebound for +38% overall. In my general account I sold almost everything at the March low for −29%. The difference was process, not the stock: see the [IONQ post-mortem](../post-mortems/2026-IONQ.md).
3. **Fees kill tiny orders.** 2024 trades under $100 lost ~12% each after fees vs ~7% before. Minimum order size from now on.
4. **Losses are kept smaller than wins** in every account. That asymmetry, not the win rate, is what made the record profitable.

## Method
- **Revolut general:** every order grouped into round trips (position goes from zero → held → zero). [Code](../analysis/roundtrips.py)
- **Revolut ISA:** the statement reports each sold tax lot with its buy date and price. Lots whose holding periods overlap are grouped into one trade. This counts *realised* sales, including partial trims of positions I still hold.
- **Trading 212 ISA:** every order grouped into round trips, same as the general account.
- Return after fees = cash received ÷ cash spent − 1, with commissions, FX fees and dividend tax included.
