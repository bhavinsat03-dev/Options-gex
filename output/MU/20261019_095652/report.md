# MU gamma exposure report

As of 2026-10-19T13:56:52+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 911.37 | The underlying price used for every calculation in this run. |
| Net GEX | -$10.9M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 900.00, 920.00, 910.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 900.00, 915.00, 920.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 900.00: 2026-10-19 48%, 2026-10-23 13%, 2026-10-21 11%; 920.00: 2026-10-19 78%, 2026-12-18 6%, 2026-10-23 6%; 910.00: 2026-10-19 51%, 2026-11-20 27%, 2026-10-21 6% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 900.00: 2026-10-23 35%, 2026-11-20 18%, 2026-10-19 14%; 915.00: 2026-10-19 85%, 2026-10-23 4%, 2026-10-30 4%; 920.00: 2026-10-19 50%, 2026-11-20 14%, 2026-10-23 13% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 900.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 912.42 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $18.76B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $61.2M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$287.6M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±17.42 (1.9%) -> 893.94 to 928.79, exp 2026-10-19 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Put/call OI ratio | 1.13 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 0.17 vol pts (put 50.3%, call 50.1%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 24.5% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 25.8% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 14.6% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 35.1% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$27.3M net, 11.6% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-19T13:44:22+00:00)

- Call wall: 1,000.00 -> 900.00 (-100.00)
- Put wall: 900.00 -> 900.00 (+0.00)
- Zero gamma: 911.12 -> 912.42 (+1.30)
- Abs gamma strike: 900.00 -> 900.00 (+0.00)
- Net GEX: $65.1M -> -$10.9M (-$76.1M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
