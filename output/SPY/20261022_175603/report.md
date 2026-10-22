# SPY gamma exposure report

As of 2026-10-22T21:56:03+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 763.96 | The underlying price used for every calculation in this run. |
| Net GEX | -$13.40B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 770.00, 780.00, 800.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 760.00, 765.00, 767.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 770.00: 2026-10-23 35%, 2026-10-30 26%, 2026-11-20 17%; 780.00: 2026-10-30 44%, 2026-11-20 25%, 2026-11-13 10%; 800.00: 2026-11-20 76%, 2026-10-30 9%, 2026-11-13 7% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 760.00: 2026-10-30 45%, 2026-10-23 26%, 2026-11-20 12%; 765.00: 2026-10-23 43%, 2026-10-30 35%, 2026-11-20 10%; 767.00: 2026-10-27 56%, 2026-10-23 27%, 2026-10-26 5% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 760.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 775.29 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $80.67B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $2.45B | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$1.67B | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±5.71 (0.7%) -> 758.25 to 769.67, exp 2026-10-23 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 2,152,484 calls / 5,927,332 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 800.00 (161,856); puts 750.00 (201,733) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 770 calls, 48,474 OI: 2026-11-20 32% (15,432), 2026-10-30 26% (12,381), 2026-10-23 20% (9,701); put wall 760 puts, 160,338 OI: 2026-10-30 47% (75,291), 2026-11-20 22% (34,886), 2026-10-23 10% (16,829); max call OI 800 calls, 161,856 OI: 2026-11-20 50% (81,279), 2026-10-30 30% (49,118), 2026-10-23 6% (9,453); max put OI 750 puts, 201,733 OI: 2026-11-20 40% (81,348), 2026-10-30 33% (67,250), 2026-11-06 9% (18,272) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 770.00: 48,474 calls; put wall 760.00: 160,338 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 2.75 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 3.21 vol pts (put 16.7%, call 13.5%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 21.5% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 42.0% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 36.4% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$337.2M net, 5.2% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-22T19:00:50+00:00)

- Call wall: 770.00 -> 770.00 (+0.00)
- Put wall: 762.00 -> 760.00 (-2.00)
- Zero gamma: 771.14 -> 775.29 (+4.15)
- Abs gamma strike: 762.00 -> 760.00 (-2.00)
- Net GEX: -$16.15B -> -$13.40B (+$2.75B)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
