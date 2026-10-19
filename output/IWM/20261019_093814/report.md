# IWM gamma exposure report

As of 2026-10-19T13:38:14+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 271.87 | The underlying price used for every calculation in this run. |
| Net GEX | -$1.37B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 274.00, 275.00, 272.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 272.00, 270.00, 273.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 274.00: 2026-10-19 61%, 2026-10-23 11%, 2026-10-21 10%; 275.00: 2026-10-23 20%, 2026-10-21 17%, 2026-10-19 16%; 272.00: 2026-10-19 61%, 2026-10-20 18%, 2026-10-23 9% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 272.00: 2026-10-19 64%, 2026-10-30 21%, 2026-10-23 7%; 270.00: 2026-10-30 35%, 2026-10-19 33%, 2026-10-23 11%; 273.00: 2026-10-19 79%, 2026-10-23 5%, 2026-10-21 5% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 272.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 275.18 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $9.03B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $200.8M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$533.4M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±1.95 (0.7%) -> 269.92 to 273.82, exp 2026-10-19 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Put/call OI ratio | 1.63 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 2.99 vol pts (put 21.7%, call 18.7%, exp 2026-11-13) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 27.4% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 28.9% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 34.2% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 9.5% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $0 net, 0.0% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-18T00:44:03+00:00)

- Call wall: 278.00 -> 274.00 (-4.00)
- Put wall: 270.00 -> 272.00 (+2.00)
- Zero gamma: 283.88 -> 275.18 (-8.70)
- Abs gamma strike: 270.00 -> 272.00 (+2.00)
- Net GEX: -$2.17B -> -$1.37B (+$802.1M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
