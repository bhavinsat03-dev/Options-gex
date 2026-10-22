# META gamma exposure report

As of 2026-10-22T13:50:59+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 652.28 | The underlying price used for every calculation in this run. |
| Net GEX | -$309.4M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 700.00, 750.00, 650.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 650.00, 660.00, 670.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 700.00: 2026-11-20 74%, 2026-10-23 7%, 2026-10-30 7%; 750.00: 2026-11-20 75%, 2026-10-30 9%, 2026-11-06 5%; 650.00: 2026-11-20 66%, 2026-10-30 18%, 2026-10-23 13% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 650.00: 2026-10-23 74%, 2026-11-20 12%, 2026-10-30 5%; 660.00: 2026-10-23 59%, 2026-11-20 20%, 2026-10-30 12%; 670.00: 2026-10-23 39%, 2026-10-30 29%, 2026-11-20 18% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 650.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 676.61 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $8.79B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $53.7M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$226.8M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±20.67 (3.2%) -> 631.61 to 672.96, exp 2026-10-23 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 539,789 calls / 375,345 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 750.00 (28,741); puts 650.00 (17,255) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 700 calls, 28,625 OI: 2026-11-20 73% (20,787), 2026-10-23 10% (2,993), 2026-11-27 7% (1,888); put wall 650 puts, 17,255 OI: 2026-10-23 50% (8,676), 2026-11-20 29% (4,976), 2026-10-30 8% (1,407); max call OI 750 calls, 28,741 OI: 2026-11-20 44% (12,601), 2026-10-23 37% (10,670), 2026-10-30 9% (2,490); max put OI 650 puts, 17,255 OI: 2026-10-23 50% (8,676), 2026-11-20 29% (4,976), 2026-10-30 8% (1,407) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 700.00: 28,625 calls; put wall 650.00: 17,255 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 0.70 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | -7.53 vol pts (put 34.6%, call 42.1%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 34.4% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 17.4% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 48.2% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$1.2M net, 1.4% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-21T19:00:04+00:00)

- Call wall: 700.00 -> 700.00 (+0.00)
- Put wall: 750.00 -> 650.00 (-100.00)
- Zero gamma: 678.90 -> 676.61 (-2.29)
- Abs gamma strike: 750.00 -> 650.00 (-100.00)
- Net GEX: $135.7M -> -$309.4M (-$445.1M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
