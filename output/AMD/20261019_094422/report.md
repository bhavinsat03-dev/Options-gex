# AMD gamma exposure report

As of 2026-10-19T13:44:22+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 551.53 | The underlying price used for every calculation in this run. |
| Net GEX | $84.7M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | positive gamma | Dealer hedging tends to offset price moves, a condition historically associated with lower realized volatility. |
| Call walls (top 3) | 560.00, 570.00, 620.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 540.00, 545.00, 500.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 560.00: 2026-10-23 44%, 2026-10-19 39%, 2026-11-20 11%; 570.00: 2026-10-23 78%, 2026-10-21 10%, 2026-10-30 8%; 620.00: 2026-11-20 100%, 2026-10-23 0%, 2026-11-06 0% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 540.00: 2026-10-23 100%, 2026-10-30 0%, 2026-12-18 0%; 545.00: 2026-10-23 100%, 2026-11-06 0%, 2026-10-30 0%; 500.00: 2026-10-23 97%, 2026-10-28 2%, 2026-10-19 1% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 560.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 550.34 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $1.19B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $8.9M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$3.7M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±32.17 (5.8%) -> 519.36 to 583.71, exp 2026-10-19 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Put/call OI ratio | 1.03 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | -23.80 vol pts (put 32.9%, call 56.7%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 30.4% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 40.3% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 2.2% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 27.2% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $498.3K net, 6.3% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-19T13:42:08+00:00)

- Call wall: 550.00 -> 560.00 (+10.00)
- Put wall: 550.00 -> 540.00 (-10.00)
- Zero gamma: 550.97 -> 550.34 (-0.63)
- Abs gamma strike: 550.00 -> 560.00 (+10.00)
- Net GEX: -$11.5M -> $84.7M (+$96.1M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
