# TSLA gamma exposure report

As of 2026-10-19T13:38:14+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 356.92 | The underlying price used for every calculation in this run. |
| Net GEX | $61.4M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | positive gamma | Dealer hedging tends to offset price moves, a condition historically associated with lower realized volatility. |
| Call walls (top 3) | 360.00, 380.00, 400.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 350.00, 360.00, 355.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 360.00: 2026-10-19 67%, 2026-10-23 10%, 2026-11-20 8%; 380.00: 2026-10-23 35%, 2026-10-19 17%, 2026-12-18 13%; 400.00: 2026-11-20 29%, 2026-12-18 21%, 2026-10-23 20% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 350.00: 2026-10-19 45%, 2026-12-18 15%, 2026-11-20 14%; 360.00: 2026-10-19 57%, 2026-10-23 13%, 2026-10-30 8%; 355.00: 2026-10-19 55%, 2026-11-20 13%, 2026-10-23 12% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 360.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 354.43 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $11.24B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $42.9M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$688.6M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±8.10 (2.3%) -> 348.82 to 365.02, exp 2026-10-19 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Put/call OI ratio | 0.81 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | -2.03 vol pts (put 61.9%, call 64.0%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 30.1% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 21.7% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 12.5% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 35.7% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$16.6M net, 14.1% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-18T00:44:03+00:00)

- Call wall: 400.00 -> 360.00 (-40.00)
- Put wall: 350.00 -> 350.00 (+0.00)
- Zero gamma: 357.30 -> 354.43 (-2.87)
- Abs gamma strike: 350.00 -> 360.00 (+10.00)
- Net GEX: -$20.5M -> $61.4M (+$81.9M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
