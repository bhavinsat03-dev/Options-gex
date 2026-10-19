# IWM gamma exposure report

As of 2026-10-19T13:56:52+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 270.81 | The underlying price used for every calculation in this run. |
| Net GEX | -$1.53B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 272.00, 278.00, 275.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 270.00, 271.00, 272.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 272.00: 2026-10-19 57%, 2026-10-20 19%, 2026-10-23 10%; 278.00: 2026-10-30 71%, 2026-10-23 12%, 2026-10-26 7%; 275.00: 2026-10-23 24%, 2026-10-21 18%, 2026-10-22 13% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 270.00: 2026-10-19 56%, 2026-10-30 22%, 2026-10-23 8%; 271.00: 2026-10-19 39%, 2026-10-30 29%, 2026-10-23 16%; 272.00: 2026-10-30 56%, 2026-10-23 21%, 2026-10-22 6% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 270.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 274.04 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $7.53B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $192.4M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$527.9M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±1.49 (0.6%) -> 269.32 to 272.30, exp 2026-10-19 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Put/call OI ratio | 1.63 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 1.27 vol pts (put 20.4%, call 19.1%, exp 2026-11-13) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 19.4% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 29.4% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 39.9% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 11.3% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $0 net, 0.0% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-19T13:44:22+00:00)

- Call wall: 272.00 -> 272.00 (+0.00)
- Put wall: 273.00 -> 270.00 (-3.00)
- Zero gamma: 271.30 -> 274.04 (+2.74)
- Abs gamma strike: 273.00 -> 270.00 (-3.00)
- Net GEX: -$3.9M -> -$1.53B (-$1.53B)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
