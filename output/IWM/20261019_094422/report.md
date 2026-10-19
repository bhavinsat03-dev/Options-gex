# IWM gamma exposure report

As of 2026-10-19T13:44:22+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 271.28 | The underlying price used for every calculation in this run. |
| Net GEX | -$3.9M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 272.00, 271.00, 273.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 273.00, 271.00, 269.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 272.00: 2026-10-19 100%; 271.00: 2026-10-19 77%, 2026-10-21 20%, 2026-10-26 2%; 273.00: 2026-10-19 94%, 2026-10-26 2%, 2026-10-23 2% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 273.00: 2026-10-19 99%, 2026-10-28 1%; 271.00: 2026-10-19 100%; 269.00: 2026-10-30 60%, 2026-10-19 40%, 2026-10-21 0% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 273.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 271.30 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $676.1M | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $19.6M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$112.3M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±1.86 (0.7%) -> 269.42 to 273.14, exp 2026-10-19 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Put/call OI ratio | 1.63 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | -7.09 vol pts (put 13.8%, call 20.9%, exp 2026-11-13) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 68.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 15.7% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 9.6% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 6.7% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $0 net, 0.0% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-19T13:42:08+00:00)

- Call wall: 274.00 -> 272.00 (-2.00)
- Put wall: 272.00 -> 273.00 (+1.00)
- Zero gamma: 274.58 -> 271.30 (-3.28)
- Abs gamma strike: 272.00 -> 273.00 (+1.00)
- Net GEX: -$1.33B -> -$3.9M (+$1.32B)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
