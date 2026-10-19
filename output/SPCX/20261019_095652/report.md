# SPCX gamma exposure report

As of 2026-10-19T13:56:52+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 147.69 | The underlying price used for every calculation in this run. |
| Net GEX | -$130.7M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 150.00, 155.00, 160.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 148.00, 140.00, 150.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 150.00: 2026-10-19 37%, 2026-11-20 21%, 2026-12-18 17%; 155.00: 2026-10-23 26%, 2026-12-18 20%, 2026-11-20 19%; 160.00: 2026-11-20 31%, 2026-10-23 23%, 2026-10-30 17% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 148.00: 2026-10-19 95%, 2026-10-28 2%, 2026-10-23 1%; 140.00: 2026-11-20 25%, 2026-10-23 24%, 2026-12-18 24%; 150.00: 2026-11-20 29%, 2026-12-18 23%, 2026-10-30 19% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 148.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 150.93 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $5.56B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $16.6M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$98.1M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±3.08 (2.1%) -> 144.61 to 150.78, exp 2026-10-19 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Put/call OI ratio | 1.07 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | -4.57 vol pts (put 56.3%, call 60.9%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 31.6% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 22.2% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 11.8% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 34.4% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$17.1M net, 12.3% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-19T13:44:22+00:00)

- Call wall: 150.00 -> 150.00 (+0.00)
- Put wall: 140.00 -> 148.00 (+8.00)
- Zero gamma: 149.02 -> 150.93 (+1.91)
- Abs gamma strike: 150.00 -> 148.00 (-2.00)
- Net GEX: -$14.7M -> -$130.7M (-$116.0M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
