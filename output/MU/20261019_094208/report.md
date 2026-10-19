# MU gamma exposure report

As of 2026-10-19T13:42:08+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 913.47 | The underlying price used for every calculation in this run. |
| Net GEX | $125.9M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | positive gamma | Dealer hedging tends to offset price moves, a condition historically associated with lower realized volatility. |
| Call walls (top 3) | 900.00, 910.00, 925.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 900.00, 850.00, 800.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 900.00: 2026-10-19 62%, 2026-11-20 17%, 2026-12-18 10%; 910.00: 2026-10-19 57%, 2026-11-20 35%, 2026-10-23 7%; 925.00: 2026-10-19 92%, 2026-10-23 6%, 2026-10-30 2% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 900.00: 2026-11-20 38%, 2026-10-19 27%, 2026-10-21 10%; 850.00: 2026-11-20 47%, 2026-10-23 33%, 2026-10-21 7%; 800.00: 2026-11-20 43%, 2026-12-18 29%, 2026-10-23 8% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 900.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 910.70 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $10.21B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $59.5M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$474.3M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±45.80 (5.0%) -> 867.67 to 959.27, exp 2026-10-19 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Put/call OI ratio | 1.13 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 0.29 vol pts (put 50.6%, call 50.3%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 22.6% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 24.1% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 10.1% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 43.2% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$3.7M net, 9.3% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-19T13:38:14+00:00)

- Call wall: 900.00 -> 900.00 (+0.00)
- Put wall: 900.00 -> 900.00 (+0.00)
- Zero gamma: 910.47 -> 910.70 (+0.23)
- Abs gamma strike: 900.00 -> 900.00 (+0.00)
- Net GEX: -$1.9M -> $125.9M (+$127.8M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
