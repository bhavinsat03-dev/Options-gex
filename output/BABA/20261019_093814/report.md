# BABA gamma exposure report

As of 2026-10-19T13:38:14+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 109.58 | The underlying price used for every calculation in this run. |
| Net GEX | $6.2M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | positive gamma | Dealer hedging tends to offset price moves, a condition historically associated with lower realized volatility. |
| Call walls (top 3) | 120.00, 115.00, 130.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 100.00, 110.00, 105.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 120.00: 2026-11-20 46%, 2026-12-18 29%, 2026-10-30 13%; 115.00: 2026-10-23 60%, 2026-11-20 15%, 2026-12-18 14%; 130.00: 2026-11-20 48%, 2026-12-18 41%, 2026-10-30 4% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 100.00: 2026-12-18 66%, 2026-11-20 21%, 2026-10-23 6%; 110.00: 2026-12-18 51%, 2026-11-20 32%, 2026-10-23 8%; 105.00: 2026-12-18 38%, 2026-11-20 30%, 2026-10-23 21% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 100.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 107.37 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $1.79B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $6.6M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$19.3M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±4.38 (4.0%) -> 105.20 to 113.97, exp 2026-10-23 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Put/call OI ratio | 0.56 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | -3.39 vol pts (put 59.4%, call 62.8%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 29.3% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 9.6% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 61.0% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$5.5M net, 34.4% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-18T00:44:03+00:00)

- Call wall: 120.00 -> 120.00 (+0.00)
- Put wall: 110.00 -> 100.00 (-10.00)
- Zero gamma: 105.65 -> 107.37 (+1.72)
- Abs gamma strike: 110.00 -> 100.00 (-10.00)
- Net GEX: $11.4M -> $6.2M (-$5.3M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
