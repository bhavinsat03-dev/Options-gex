# TSLA gamma exposure report

As of 2026-10-18T00:44:03+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 354.72 | The underlying price used for every calculation in this run. |
| Net GEX | -$20.5M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 400.00, 350.00, 380.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 350.00, 360.00, 355.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 400.00: 2026-11-20 40%, 2026-10-30 28%, 2026-10-23 18%; 350.00: 2026-11-20 73%, 2026-10-19 7%, 2026-10-23 6%; 380.00: 2026-11-20 26%, 2026-10-23 23%, 2026-10-30 16% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 350.00: 2026-11-20 34%, 2026-10-19 25%, 2026-10-23 18%; 360.00: 2026-10-19 37%, 2026-10-23 23%, 2026-10-30 17%; 355.00: 2026-10-19 44%, 2026-11-20 21%, 2026-10-23 15% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 350.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 357.30 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $6.37B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $31.7M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$120.5M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±8.85 (2.5%) -> 345.87 to 363.57, exp 2026-10-19 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Put/call OI ratio | 0.80 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 0.86 vol pts (put 49.9%, call 49.1%, exp 2026-11-13) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 0.0% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 60.9% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 39.1% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $1.3M net, 1.0% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-18T00:36:34+00:00)

- Call wall: 400.00 -> 400.00 (+0.00)
- Put wall: 350.00 -> 350.00 (+0.00)
- Zero gamma: 357.29 -> 357.30 (+0.01)
- Abs gamma strike: 350.00 -> 350.00 (+0.00)
- Net GEX: -$20.4M -> -$20.5M (-$99.1K)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
