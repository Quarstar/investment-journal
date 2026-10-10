# Trade history: Revolut general account, May 2024 – Oct 2026

← Back to the [combined track record](track-record.md)

> **Backfilled from broker records on 9 Oct 2026.** These trades happened before this journal existed, so the git timestamps show when they were *uploaded*, not when they were *made*. The source is my official Revolut Trading account statement (kept private). From October 2026 onward, trades are logged in [`swing-log.md`](swing-log.md) **before** entry.
>
> Covers my Revolut **general** (non-ISA) trading account. See the [combined track record](track-record.md) for all three accounts.

## Method
- 486 orders parsed from the statement, grouped into **87 round trips**. A round trip opens when a position goes from zero to a holding and closes when it's back to zero, including adds and partial sells in between.
- **Return after fees** = cash received from sells ÷ cash spent on buys − 1, with all commissions and fees included.
- Code: [`analysis/parse_revolut_statement.py`](../analysis/parse_revolut_statement.py) → [`analysis/roundtrips.py`](../analysis/roundtrips.py). Full table as CSV: [`revolut-general_roundtrips.csv`](revolut-general_roundtrips.csv).
- Returns only, no £/$ amounts, by design.

## Headline numbers

| Metric | Result |
|---|---|
| Closed round trips | 87 (46 wins, 41 losses) |
| Win rate | 53% |
| Average return per trade (after fees) | +1.8% (median +0.7%) |
| Average win / average loss | +14.0% / −11.9% |
| Profit factor (total won ÷ total lost) | **6.7** |
| Share of total profit from the top 5 trades | 72% |
| Median holding period | 17 days |

## By year

| Year opened | Trades | Win rate | Avg return / trade | Share of net profit |
|---|---|---|---|---|
| 2024 | 30 | 23% | −7.4% | 12% |
| 2025 | 47 | 72% | +8.2% | 93% |
| 2026 | 10 | 50% | −0.6% | −6% |

## By holding period

| Held | Trades | Win rate | Avg return / trade | Share of net profit |
|---|---|---|---|---|
| ≤ 1 week | 25 | 40% | −0.3% | 5% |
| 1 week – 1 month | 28 | 54% | +3.1% | 14% |
| 1 – 3 months | 23 | 57% | −1.6% | 54% |
| > 3 months | 11 | 73% | +10.5% | 27% |

## What the data says (honest read)
1. **My profit came from a few big conviction trades in AI leaders, not from quick swings.** NBIS (+53%), two AMD runs (+22%, +25%), NVDA (+15%) and DLO (+29%) produced 72% of all profit. Those were built and trimmed over weeks with many orders.
2. **Short trades were roughly break-even.** Trades held a week or less won 40% of the time and averaged −0.3%. Simple trades with six orders or fewer averaged −0.3% too. My edge isn't in fast in-and-out trades.
3. **2025 was the year everything worked.** A 72% win rate in a strong AI bull market. 2026 so far is 50/50 and slightly negative. I can't yet separate skill from the tide, so the logged-in-advance record from here matters.
4. **Losses are kept small, which is what makes the record work.** Average loss −11.9% vs average win +14.0%, and total wins are 6.7× total losses.
5. **Fees destroyed tiny trades.** In 2024 I placed many ~$10–$100 orders with a ~$1.27 commission each. Trades under $100 averaged −12.4% after fees versus −6.6% before. Lesson: no more small orders.
6. **My worst trade broke my own rules.** IONQ (Jan → Mar 2026): bought at $45, averaged down twice to $31, then sold almost everything at the March low for about −30%, weeks before the stock rebounded. See [the post-mortem](../post-mortems/2026-IONQ.md). This is why the swing sleeve now has a hard stop placed at entry and no averaging down.

*Note: a few "days held" figures are inflated by leftover fractional shares that couldn't be limit-sold. IONQ's leftover 0.84 shares sat until June, for example. Returns are unaffected.*

## What changes because of this
- The swing sleeve stays **sandbox-sized** until the forward log proves an edge. History says my edge is in conviction position trades, not fast swings.
- **Stop placed at entry, no averaging down** (lesson from IONQ).
- **Time stop is non-negotiable.**
- **Minimum order size** so commission stays under ~0.5% of the trade.

## Full history
| # | Ticker | Opened | Closed | Days | Orders | Return after fees | Result |
|---|---|---|---|---|---|---|---|
| 1 | SAIC | 2024-05-28 | 2024-06-03 | 6 | 2 | -36.9% | ❌ |
| 2 | TM | 2024-05-28 | 2024-08-23 | 87 | 2 | -28.9% | ❌ |
| 3 | NIO | 2024-05-28 | 2024-09-06 | 101 | 9 | -9.2% | ❌ |
| 4 | MSFT | 2024-05-31 | 2024-07-22 | 51 | 3 | -9.4% | ❌ |
| 5 | BABA | 2024-06-21 | 2024-09-30 | 100 | 7 | +8.7% | ✅ |
| 6 | CRWD | 2024-07-22 | 2024-07-22 | 0 | 2 | -8.6% | ❌ |
| 7 | CRWD | 2024-07-23 | 2024-09-03 | 41 | 2 | -1.5% | ❌ |
| 8 | RIOT | 2024-07-26 | 2024-11-11 | 108 | 5 | +87.5% | ✅ |
| 9 | TWOUQ | 2024-07-31 | 2024-10-01 | 61 | 2 | -100.0% | ❌ |
| 10 | NVDA | 2024-09-09 | 2025-06-25 | 289 | 47 | +15.1% | ✅ |
| 11 | ASML | 2024-09-09 | 2024-10-14 | 34 | 3 | +4.1% | ✅ |
| 12 | ASML | 2024-10-25 | 2024-11-15 | 21 | 2 | -9.8% | ❌ |
| 13 | MSFT | 2024-11-01 | 2024-11-13 | 11 | 3 | -1.6% | ❌ |
| 14 | UBER | 2024-11-01 | 2024-11-25 | 24 | 3 | -1.7% | ❌ |
| 15 | LRCX | 2024-11-01 | 2024-12-02 | 30 | 2 | -4.1% | ❌ |
| 16 | SMCI | 2024-11-04 | 2024-11-14 | 10 | 3 | -27.5% | ❌ |
| 17 | IGMS | 2024-11-08 | 2024-11-11 | 2 | 2 | -1.2% | ❌ |
| 18 | ABCL | 2024-11-11 | 2024-11-22 | 10 | 3 | -10.6% | ❌ |
| 19 | AMD | 2024-11-13 | 2024-12-03 | 19 | 2 | -2.1% | ❌ |
| 20 | RIOT | 2024-11-14 | 2024-11-21 | 6 | 2 | -4.6% | ❌ |
| 21 | RIO | 2024-11-15 | 2024-11-26 | 11 | 2 | -1.4% | ❌ |
| 22 | KRRO | 2024-11-21 | 2024-11-21 | 0 | 2 | -5.8% | ❌ |
| 23 | IGMS | 2024-11-21 | 2024-11-21 | 0 | 2 | -9.6% | ❌ |
| 24 | IONQ | 2024-11-21 | 2024-11-22 | 0 | 2 | +5.6% | ✅ |
| 25 | IONQ | 2024-11-22 | 2024-12-02 | 9 | 4 | +16.5% | ✅ |
| 26 | NIO | 2024-11-25 | 2024-12-04 | 8 | 2 | -3.7% | ❌ |
| 27 | RIOT | 2024-11-26 | 2024-11-26 | 0 | 2 | -4.9% | ❌ |
| 28 | FLNA | 2024-11-29 | 2025-03-14 | 105 | 2 | -32.7% | ❌ |
| 29 | IGMS | 2024-12-03 | 2025-02-25 | 83 | 3 | -63.8% | ❌ |
| 30 | IONQ | 2024-12-11 | 2024-12-20 | 8 | 2 | +20.8% | ✅ |
| 31 | IONQ | 2025-01-08 | 2025-03-17 | 68 | 8 | +22.6% | ✅ |
| 32 | FDX | 2025-01-10 | 2025-01-27 | 17 | 2 | -0.6% | ❌ |
| 33 | PCAR | 2025-01-10 | 2025-01-27 | 17 | 2 | +0.9% | ✅ |
| 34 | AMD | 2025-01-22 | 2025-09-04 | 225 | 22 | +25.1% | ✅ |
| 35 | RIOT | 2025-01-27 | 2025-02-18 | 21 | 2 | -0.1% | ❌ |
| 36 | HIMS | 2025-03-12 | 2025-03-14 | 2 | 2 | -11.7% | ❌ |
| 37 | TSLA | 2025-03-12 | 2025-03-21 | 9 | 3 | +0.7% | ✅ |
| 38 | TSM | 2025-03-12 | 2025-05-12 | 61 | 3 | +5.7% | ✅ |
| 39 | AMZN | 2025-03-12 | 2025-06-13 | 93 | 8 | +2.2% | ✅ |
| 40 | MSTR | 2025-03-14 | 2025-03-26 | 12 | 4 | +19.3% | ✅ |
| 41 | RIOT | 2025-03-17 | 2025-04-25 | 38 | 4 | +0.2% | ✅ |
| 42 | IONQ | 2025-03-21 | 2025-03-26 | 5 | 5 | +26.3% | ✅ |
| 43 | BABA | 2025-03-24 | 2025-08-20 | 149 | 22 | +4.8% | ✅ |
| 44 | MU | 2025-03-26 | 2025-03-26 | 0 | 2 | -4.7% | ❌ |
| 45 | GOOGL | 2025-03-31 | 2025-07-07 | 98 | 5 | +14.3% | ✅ |
| 46 | IONQ | 2025-03-31 | 2025-04-03 | 2 | 4 | +4.2% | ✅ |
| 47 | MSTR | 2025-03-31 | 2025-04-03 | 2 | 2 | -1.3% | ❌ |
| 48 | YUMC | 2025-05-02 | 2025-06-13 | 42 | 3 | -0.2% | ❌ |
| 49 | DLO | 2025-05-12 | 2025-06-02 | 21 | 4 | +11.4% | ✅ |
| 50 | UNH | 2025-05-21 | 2025-05-22 | 0 | 2 | -3.1% | ❌ |
| 51 | NIO | 2025-05-21 | 2025-07-14 | 53 | 5 | +7.1% | ✅ |
| 52 | SMCI | 2025-05-23 | 2025-05-29 | 5 | 2 | +8.4% | ✅ |
| 53 | DLO | 2025-06-09 | 2025-10-14 | 126 | 10 | +28.9% | ✅ |
| 54 | PYPL | 2025-06-13 | 2025-08-28 | 75 | 11 | +2.1% | ✅ |
| 55 | ABCL | 2025-08-11 | 2025-10-07 | 56 | 2 | +29.6% | ✅ |
| 56 | NBIS | 2025-08-14 | 2025-10-29 | 75 | 18 | +53.4% | ✅ |
| 57 | IONQ | 2025-08-20 | 2025-09-02 | 12 | 4 | +16.4% | ✅ |
| 58 | DUOL | 2025-08-28 | 2025-10-06 | 38 | 6 | +7.1% | ✅ |
| 59 | LULU | 2025-09-05 | 2025-09-23 | 18 | 2 | +1.3% | ✅ |
| 60 | ORCL | 2025-09-30 | 2025-10-08 | 8 | 3 | +0.7% | ✅ |
| 61 | MSTR | 2025-09-30 | 2025-10-07 | 7 | 3 | +11.9% | ✅ |
| 62 | AMD | 2025-09-30 | 2025-11-13 | 44 | 28 | +21.7% | ✅ |
| 63 | WING | 2025-09-30 | 2025-10-09 | 9 | 4 | -0.3% | ❌ |
| 64 | RIVN | 2025-10-03 | 2025-10-06 | 3 | 2 | +0.4% | ✅ |
| 65 | IREN | 2025-10-07 | 2025-10-10 | 3 | 2 | +16.4% | ✅ |
| 66 | NVDA | 2025-10-08 | 2025-12-30 | 83 | 37 | +3.7% | ✅ |
| 67 | AMZN | 2025-10-24 | 2025-11-06 | 13 | 11 | +7.8% | ✅ |
| 68 | META | 2025-11-03 | 2025-11-13 | 9 | 3 | -4.3% | ❌ |
| 69 | NBIS | 2025-11-11 | 2026-01-12 | 61 | 27 | -2.2% | ❌ |
| 70 | META | 2025-11-14 | 2025-11-20 | 5 | 2 | -0.2% | ❌ |
| 71 | IONQ | 2025-11-14 | 2025-12-01 | 17 | 5 | +3.1% | ✅ |
| 72 | AMZN | 2025-11-20 | 2025-11-21 | 0 | 3 | -5.1% | ❌ |
| 73 | AMD | 2025-11-20 | 2025-12-30 | 39 | 7 | -2.1% | ❌ |
| 74 | RBRK | 2025-12-01 | 2025-12-05 | 4 | 5 | +21.6% | ✅ |
| 75 | IREN | 2025-12-05 | 2026-01-30 | 55 | 4 | +17.4% | ✅ |
| 76 | RIOT | 2025-12-30 | 2026-01-30 | 30 | 6 | +20.2% | ✅ |
| 77 | IONQ | 2025-12-30 | 2026-01-12 | 12 | 4 | +4.2% | ✅ |
| 78 | MSTR | 2026-01-06 | 2026-02-26 | 50 | 3 | -17.1% | ❌ |
| 79 | VLN | 2026-01-12 | 2026-01-14 | 2 | 2 | -11.6% | ❌ |
| 80 | MREO | 2026-01-12 | 2026-01-12 | 0 | 2 | +2.6% | ✅ |
| 81 | RBRK | 2026-01-15 | 2026-03-04 | 48 | 5 | -13.6% | ❌ |
| 82 | IONQ | 2026-01-26 | 2026-06-22 | 146 | 5 | -29.1% | ❌ |
| 83 | NBIS | 2026-01-30 | 2026-02-13 | 13 | 2 | +8.9% | ✅ |
| 84 | NOK | 2026-02-10 | 2026-02-12 | 2 | 3 | -1.8% | ❌ |
| 85 | NVDA | 2026-03-30 | 2026-06-05 | 66 | 2 | +27.9% | ✅ |
| 86 | GDC | 2026-05-11 | 2026-05-13 | 2 | 2 | +6.1% | ✅ |
| 87 | USAR | 2026-06-09 | 2026-06-22 | 12 | 2 | +21.6% | ✅ |