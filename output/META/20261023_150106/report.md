# META gamma exposure report

As of 2026-10-23T19:01:06+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 644.77 | The underlying price used for every calculation in this run. |
| Net GEX | -$622.4M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 645.00, 700.00, 650.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 645.00, 650.00, 700.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 645.00: 2026-10-23 97%, 2026-11-20 1%, 2026-10-30 1%; 700.00: 2026-11-20 60%, 2026-12-18 20%, 2026-11-27 6%; 650.00: 2026-11-20 28%, 2026-10-30 27%, 2026-10-26 22% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 645.00: 2026-10-23 98%, 2026-11-20 1%, 2026-10-30 0%; 650.00: 2026-11-20 27%, 2026-10-26 25%, 2026-10-30 20%; 700.00: 2026-11-20 44%, 2026-12-18 36%, 2026-10-30 11% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 645.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 651.46 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $16.14B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $61.8M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | $183.3M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±3.22 (0.5%) -> 641.55 to 647.99, exp 2026-10-23 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 849,071 calls / 514,195 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 700.00 (47,947); puts 600.00 (26,231) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 645 calls, 2,772 OI: 2026-10-23 29% (791), 2026-12-18 23% (628), 2026-11-20 23% (625); put wall 645 puts, 8,203 OI: 2026-10-23 38% (3,121), 2026-11-20 30% (2,462), 2026-12-18 14% (1,159); max call OI 700 calls, 47,947 OI: 2026-11-20 44% (21,334), 2026-12-18 18% (8,714), 2026-10-23 17% (8,129); max put OI 600 puts, 26,231 OI: 2026-10-23 32% (8,392), 2026-12-18 22% (5,862), 2026-11-20 20% (5,183) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 645.00: 2,772 calls; put wall 645.00: 8,203 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 0.61 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | -0.24 vol pts (put 37.1%, call 37.4%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 44.3% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 0.0% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 14.8% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 41.0% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$7.0M net, 14.7% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-23T16:30:16+00:00)

- Call wall: 700.00 -> 645.00 (-55.00)
- Put wall: 640.00 -> 645.00 (+5.00)
- Zero gamma: 646.83 -> 651.46 (+4.63)
- Abs gamma strike: 640.00 -> 645.00 (+5.00)
- Net GEX: -$169.9M -> -$622.4M (-$452.5M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
