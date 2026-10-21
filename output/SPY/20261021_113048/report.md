# SPY gamma exposure report

As of 2026-10-21T15:30:48+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 772.08 | The underlying price used for every calculation in this run. |
| Net GEX | -$1.73B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 773.00, 772.00, 780.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 760.00, 769.00, 765.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 773.00: 2026-10-21 79%, 2026-10-23 8%, 2026-10-22 7%; 772.00: 2026-10-21 71%, 2026-10-23 13%, 2026-10-22 6%; 780.00: 2026-10-23 32%, 2026-10-30 29%, 2026-11-20 12% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 760.00: 2026-10-30 68%, 2026-11-20 12%, 2026-10-23 9%; 769.00: 2026-10-23 69%, 2026-10-21 9%, 2026-10-30 6%; 765.00: 2026-10-30 48%, 2026-10-23 24%, 2026-11-20 14% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 773.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 772.74 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $71.25B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $3.33B | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$3.32B | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±2.41 (0.3%) -> 769.67 to 774.49, exp 2026-10-21 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 2,114,648 calls / 6,026,536 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 800.00 (136,648); puts 760.00 (219,963) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 773 calls, 29,293 OI: 2026-10-21 39% (11,351), 2026-10-23 17% (5,065), 2026-10-22 10% (2,917); put wall 760 puts, 219,963 OI: 2026-10-30 59% (130,435), 2026-11-20 15% (33,002), 2026-10-23 8% (18,427); max call OI 800 calls, 136,648 OI: 2026-11-20 39% (53,958), 2026-10-30 36% (49,829), 2026-10-23 7% (9,627); max put OI 760 puts, 219,963 OI: 2026-10-30 59% (130,435), 2026-11-20 15% (33,002), 2026-10-23 8% (18,427) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 773.00: 29,293 calls; put wall 760.00: 219,963 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 2.85 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 2.38 vol pts (put 14.5%, call 12.1%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 16.1% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 25.5% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 30.7% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 27.7% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$131.1M net, 4.0% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-21T13:48:32+00:00)

- Call wall: 770.00 -> 773.00 (+3.00)
- Put wall: 760.00 -> 760.00 (+0.00)
- Zero gamma: 772.77 -> 772.74 (-0.03)
- Abs gamma strike: 770.00 -> 773.00 (+3.00)
- Net GEX: -$3.11B -> -$1.73B (+$1.38B)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
