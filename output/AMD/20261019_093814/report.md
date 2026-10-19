# AMD gamma exposure report

As of 2026-10-19T13:38:14+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 547.45 | The underlying price used for every calculation in this run. |
| Net GEX | $8.0M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | positive gamma | Dealer hedging tends to offset price moves, a condition historically associated with lower realized volatility. |
| Call walls (top 3) | 550.00, 620.00, 535.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 550.00, 540.00, 545.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 550.00: 2026-10-19 42%, 2026-10-23 25%, 2026-11-20 12%; 620.00: 2026-11-20 43%, 2026-10-30 29%, 2026-10-23 11%; 535.00: 2026-10-19 69%, 2026-10-23 25%, 2026-10-21 2% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 550.00: 2026-10-23 22%, 2026-11-20 22%, 2026-10-19 21%; 540.00: 2026-10-19 38%, 2026-10-23 20%, 2026-10-30 12%; 545.00: 2026-10-19 42%, 2026-10-23 21%, 2026-10-21 18% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 550.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 546.41 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $10.01B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $38.2M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$163.6M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±13.30 (2.4%) -> 534.15 to 560.75, exp 2026-10-19 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Put/call OI ratio | 1.03 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | -0.82 vol pts (put 57.9%, call 58.7%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 22.1% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 34.0% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 12.6% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 31.3% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $547.2K net, 8.4% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-18T00:44:03+00:00)

- Call wall: 620.00 -> 550.00 (-70.00)
- Put wall: 550.00 -> 550.00 (+0.00)
- Zero gamma: 579.56 -> 546.41 (-33.15)
- Abs gamma strike: 550.00 -> 550.00 (+0.00)
- Net GEX: -$139.5M -> $8.0M (+$147.5M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
