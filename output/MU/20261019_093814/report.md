# MU gamma exposure report

As of 2026-10-19T13:38:14+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 910.28 | The underlying price used for every calculation in this run. |
| Net GEX | -$1.9M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 900.00, 910.00, 920.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 900.00, 920.00, 850.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 900.00: 2026-10-19 50%, 2026-10-23 12%, 2026-11-20 11%; 910.00: 2026-10-19 46%, 2026-11-20 31%, 2026-10-23 6%; 920.00: 2026-10-19 74%, 2026-12-18 8%, 2026-10-23 6% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 900.00: 2026-10-23 35%, 2026-11-20 17%, 2026-10-19 15%; 920.00: 2026-10-19 48%, 2026-11-20 15%, 2026-10-23 13%; 850.00: 2026-11-20 36%, 2026-10-23 26%, 2026-12-18 12% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 900.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 910.47 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $18.88B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $62.7M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$561.7M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±18.80 (2.1%) -> 891.48 to 929.08, exp 2026-10-19 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Put/call OI ratio | 1.13 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 3.37 vol pts (put 54.6%, call 51.2%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 23.9% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 26.5% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 14.7% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 34.9% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$27.9M net, 11.5% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-18T00:44:03+00:00)

- Call wall: 900.00 -> 900.00 (+0.00)
- Put wall: 900.00 -> 900.00 (+0.00)
- Zero gamma: 936.72 -> 910.47 (-26.25)
- Abs gamma strike: 900.00 -> 900.00 (+0.00)
- Net GEX: -$220.9M -> -$1.9M (+$219.0M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
