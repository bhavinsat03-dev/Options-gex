# AMD gamma exposure report

As of 2026-10-23T20:32:43+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 516.79 | The underlying price used for every calculation in this run. |
| Net GEX | -$110.9M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 600.00, 550.00, 620.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 500.00, 440.00, 510.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 600.00: 2026-11-20 38%, 2026-12-18 33%, 2026-11-06 11%; 550.00: 2026-10-30 33%, 2026-11-20 32%, 2026-12-18 18%; 620.00: 2026-11-20 64%, 2026-12-18 11%, 2026-10-30 10% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 500.00: 2026-11-20 27%, 2026-10-30 24%, 2026-10-26 15%; 440.00: 2026-11-20 84%, 2026-12-18 10%, 2026-11-06 2%; 510.00: 2026-10-26 31%, 2026-10-30 22%, 2026-11-13 14% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 500.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 547.55 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $7.95B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $24.5M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$54.6M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±15.32 (3.0%) -> 501.46 to 532.11, exp 2026-10-26 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 628,523 calls / 612,122 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 620.00 (24,564); puts 440.00 (23,992) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 600 calls, 21,822 OI: 2026-11-20 29% (6,346), 2026-12-18 28% (6,181), 2026-10-30 16% (3,450); put wall 500 puts, 17,472 OI: 2026-11-20 35% (6,122), 2026-12-18 23% (4,077), 2026-10-30 15% (2,693); max call OI 620 calls, 24,564 OI: 2026-11-20 47% (11,516), 2026-10-30 31% (7,573), 2026-12-18 8% (2,050); max put OI 440 puts, 23,992 OI: 2026-11-20 82% (19,685), 2026-12-18 11% (2,665), 2026-10-30 3% (620) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 600.00: 21,822 calls; put wall 500.00: 17,472 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 0.97 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 2.51 vol pts (put 61.8%, call 59.3%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 0.0% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 41.7% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 58.3% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$8.6M net, 15.7% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-23T19:22:31+00:00)

- Call wall: 600.00 -> 600.00 (+0.00)
- Put wall: 500.00 -> 500.00 (+0.00)
- Zero gamma: 518.70 -> 547.55 (+28.85)
- Abs gamma strike: 517.50 -> 500.00 (-17.50)
- Net GEX: -$157.9M -> -$110.9M (+$47.0M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
