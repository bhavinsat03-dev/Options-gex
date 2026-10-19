# AMD gamma exposure report

As of 2026-10-19T15:31:23+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 551.31 | The underlying price used for every calculation in this run. |
| Net GEX | $63.1M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | positive gamma | Dealer hedging tends to offset price moves, a condition historically associated with lower realized volatility. |
| Call walls (top 3) | 550.00, 552.50, 620.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 550.00, 560.00, 545.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 550.00: 2026-10-19 65%, 2026-10-23 16%, 2026-11-20 6%; 552.50: 2026-10-19 94%, 2026-10-23 3%, 2026-10-21 3%; 620.00: 2026-11-20 45%, 2026-10-30 29%, 2026-10-23 9% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 550.00: 2026-10-19 40%, 2026-10-23 17%, 2026-11-20 17%; 560.00: 2026-11-20 35%, 2026-10-23 21%, 2026-10-19 14%; 545.00: 2026-10-19 30%, 2026-10-23 26%, 2026-10-21 22% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 550.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 541.37 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $9.86B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $35.5M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$75.6M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±6.26 (1.1%) -> 545.04 to 557.57, exp 2026-10-19 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 565,327 calls / 582,418 puts | Open contracts across all fetched expirations and strikes. |
| OI at main walls | call wall 550.00: 11,610 calls; put wall 550.00: 14,957 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.03 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 1.03 vol pts (put 57.1%, call 56.1%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 20.3% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 35.6% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 12.9% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 31.2% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $4.6M net, 8.6% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-19T14:20:13+00:00)

- Call wall: 550.00 -> 550.00 (+0.00)
- Put wall: 550.00 -> 550.00 (+0.00)
- Zero gamma: 543.34 -> 541.37 (-1.97)
- Abs gamma strike: 550.00 -> 550.00 (+0.00)
- Net GEX: $11.2M -> $63.1M (+$51.9M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
