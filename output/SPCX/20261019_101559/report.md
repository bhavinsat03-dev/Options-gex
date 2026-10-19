# SPCX gamma exposure report

As of 2026-10-19T14:15:59+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 149.99 | The underlying price used for every calculation in this run. |
| Net GEX | $42.4M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | positive gamma | Dealer hedging tends to offset price moves, a condition historically associated with lower realized volatility. |
| Call walls (top 3) | 150.00, 155.00, 160.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 148.00, 150.00, 140.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 150.00: 2026-10-19 80%, 2026-11-20 7%, 2026-12-18 5%; 155.00: 2026-10-23 28%, 2026-11-20 18%, 2026-12-18 18%; 160.00: 2026-11-20 31%, 2026-10-23 23%, 2026-10-30 18% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 148.00: 2026-10-19 85%, 2026-10-28 7%, 2026-10-23 3%; 150.00: 2026-11-20 25%, 2026-12-18 21%, 2026-10-19 17%; 140.00: 2026-11-20 25%, 2026-12-18 25%, 2026-10-23 23% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 150.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 149.54 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $5.45B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $18.6M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$117.2M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±2.92 (2.0%) -> 147.07 to 152.92, exp 2026-10-19 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Put/call OI ratio | 1.07 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 9.59 vol pts (put 61.9%, call 52.3%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 28.1% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 24.3% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 12.0% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 35.5% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$10.3M net, 12.6% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-19T13:56:52+00:00)

- Call wall: 150.00 -> 150.00 (+0.00)
- Put wall: 148.00 -> 148.00 (+0.00)
- Zero gamma: 150.93 -> 149.54 (-1.39)
- Abs gamma strike: 148.00 -> 150.00 (+2.00)
- Net GEX: -$130.7M -> $42.4M (+$173.1M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
