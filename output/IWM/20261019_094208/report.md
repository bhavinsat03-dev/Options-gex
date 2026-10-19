# IWM gamma exposure report

As of 2026-10-19T13:42:08+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 271.61 | The underlying price used for every calculation in this run. |
| Net GEX | -$1.33B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 274.00, 272.00, 275.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 272.00, 270.00, 273.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 274.00: 2026-10-19 62%, 2026-10-23 12%, 2026-10-21 11%; 272.00: 2026-10-19 59%, 2026-10-20 18%, 2026-10-23 9%; 275.00: 2026-10-23 23%, 2026-10-21 19%, 2026-10-19 17% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 272.00: 2026-10-19 66%, 2026-10-30 21%, 2026-10-23 7%; 270.00: 2026-10-19 60%, 2026-10-23 14%, 2026-10-20 9%; 273.00: 2026-10-19 76%, 2026-10-21 6%, 2026-10-23 6% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 272.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 274.58 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $7.81B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $128.4M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$419.0M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±1.98 (0.7%) -> 269.63 to 273.59, exp 2026-10-19 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Put/call OI ratio | 1.63 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 2.27 vol pts (put 21.4%, call 19.1%, exp 2026-11-13) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 32.9% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 30.3% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 27.0% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 9.9% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $0 net, 0.0% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-19T13:38:14+00:00)

- Call wall: 274.00 -> 274.00 (+0.00)
- Put wall: 272.00 -> 272.00 (+0.00)
- Zero gamma: 275.18 -> 274.58 (-0.60)
- Abs gamma strike: 272.00 -> 272.00 (+0.00)
- Net GEX: -$1.37B -> -$1.33B (+$41.3M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
