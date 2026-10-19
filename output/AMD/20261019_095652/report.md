# AMD gamma exposure report

As of 2026-10-19T13:56:52+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 547.26 | The underlying price used for every calculation in this run. |
| Net GEX | $4.4M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | positive gamma | Dealer hedging tends to offset price moves, a condition historically associated with lower realized volatility. |
| Call walls (top 3) | 550.00, 620.00, 535.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 550.00, 540.00, 545.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 550.00: 2026-10-19 46%, 2026-10-23 24%, 2026-11-20 11%; 620.00: 2026-11-20 45%, 2026-10-30 29%, 2026-10-23 9%; 535.00: 2026-10-19 65%, 2026-10-23 28%, 2026-10-21 3% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 550.00: 2026-10-19 30%, 2026-10-23 20%, 2026-11-20 20%; 540.00: 2026-10-19 37%, 2026-10-23 20%, 2026-10-30 12%; 545.00: 2026-10-19 51%, 2026-10-23 18%, 2026-10-21 16% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 550.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 546.48 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $9.89B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $36.6M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$72.0M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±10.25 (1.9%) -> 537.02 to 557.52, exp 2026-10-19 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Put/call OI ratio | 1.03 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 0.19 vol pts (put 58.0%, call 57.8%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 21.5% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 34.0% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 12.7% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 31.8% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $832.2K net, 8.6% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-19T13:44:22+00:00)

- Call wall: 560.00 -> 550.00 (-10.00)
- Put wall: 540.00 -> 550.00 (+10.00)
- Zero gamma: 550.34 -> 546.48 (-3.86)
- Abs gamma strike: 560.00 -> 550.00 (-10.00)
- Net GEX: $84.7M -> $4.4M (-$80.2M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
