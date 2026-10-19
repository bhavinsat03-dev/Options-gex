# META gamma exposure report

As of 2026-10-19T13:56:52+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 697.48 | The underlying price used for every calculation in this run. |
| Net GEX | -$91.4M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 700.00, 800.00, 750.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 700.00, 697.50, 750.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 700.00: 2026-11-20 59%, 2026-12-18 17%, 2026-10-19 14%; 800.00: 2026-11-20 50%, 2026-12-18 25%, 2026-10-23 10%; 750.00: 2026-11-20 41%, 2026-10-23 27%, 2026-12-18 20% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 700.00: 2026-10-19 74%, 2026-12-18 8%, 2026-10-23 7%; 697.50: 2026-10-19 99%, 2026-10-23 1%, 2026-10-26 0%; 750.00: 2026-10-23 69%, 2026-11-20 14%, 2026-12-18 11% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 700.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 703.72 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $19.10B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $87.2M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$191.0M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±10.16 (1.5%) -> 687.32 to 707.64, exp 2026-10-19 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Put/call OI ratio | 0.66 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | -4.65 vol pts (put 41.5%, call 46.2%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 17.5% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 20.6% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 9.8% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 52.1% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $53.0M net, 18.7% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-19T13:44:22+00:00)

- Call wall: 750.00 -> 700.00 (-50.00)
- Put wall: 705.00 -> 700.00 (-5.00)
- Zero gamma: 702.20 -> 703.72 (+1.52)
- Abs gamma strike: 750.00 -> 700.00 (-50.00)
- Net GEX: -$62.2M -> -$91.4M (-$29.3M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
