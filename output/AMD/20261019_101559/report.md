# AMD gamma exposure report

As of 2026-10-19T14:15:59+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 544.77 | The underlying price used for every calculation in this run. |
| Net GEX | $17.6M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | positive gamma | Dealer hedging tends to offset price moves, a condition historically associated with lower realized volatility. |
| Call walls (top 3) | 550.00, 535.00, 540.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 550.00, 540.00, 545.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 550.00: 2026-10-19 41%, 2026-10-23 26%, 2026-11-20 11%; 535.00: 2026-10-19 68%, 2026-10-23 26%, 2026-10-21 3%; 540.00: 2026-10-19 55%, 2026-10-23 22%, 2026-11-20 9% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 550.00: 2026-10-19 23%, 2026-11-20 22%, 2026-10-23 21%; 540.00: 2026-10-19 47%, 2026-10-23 17%, 2026-10-30 10%; 545.00: 2026-10-19 54%, 2026-10-23 17%, 2026-10-21 15% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 550.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 541.37 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $9.61B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $37.0M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$75.7M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±8.70 (1.6%) -> 536.07 to 553.47, exp 2026-10-19 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Put/call OI ratio | 1.03 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 1.37 vol pts (put 58.4%, call 57.1%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 23.2% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 33.3% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 12.1% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 31.4% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $1.2M net, 8.5% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-19T13:56:52+00:00)

- Call wall: 550.00 -> 550.00 (+0.00)
- Put wall: 550.00 -> 550.00 (+0.00)
- Zero gamma: 546.48 -> 541.37 (-5.11)
- Abs gamma strike: 550.00 -> 550.00 (+0.00)
- Net GEX: $4.4M -> $17.6M (+$13.2M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
