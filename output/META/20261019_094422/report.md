# META gamma exposure report

As of 2026-10-19T13:44:22+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 700.72 | The underlying price used for every calculation in this run. |
| Net GEX | -$62.2M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 750.00, 800.00, 760.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 705.00, 700.00, 650.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 750.00: 2026-11-20 50%, 2026-10-23 37%, 2026-10-30 8%; 800.00: 2026-12-18 77%, 2026-10-30 23%, 2026-11-13 0%; 760.00: 2026-11-20 63%, 2026-12-18 31%, 2026-11-06 7% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 705.00: 2026-10-19 59%, 2026-10-23 23%, 2026-10-30 13%; 700.00: 2026-12-18 48%, 2026-10-23 44%, 2026-10-26 5%; 650.00: 2026-10-23 57%, 2026-12-18 23%, 2026-10-30 11% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 750.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 702.20 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $8.09B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $48.1M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$255.9M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±14.50 (2.1%) -> 686.22 to 715.22, exp 2026-10-19 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Put/call OI ratio | 0.66 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | -7.47 vol pts (put 48.0%, call 55.4%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 14.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 19.1% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 10.1% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 56.8% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $1.8M net, 22.4% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-19T13:42:08+00:00)

- Call wall: 750.00 -> 750.00 (+0.00)
- Put wall: 705.00 -> 705.00 (+0.00)
- Zero gamma: 704.90 -> 702.20 (-2.70)
- Abs gamma strike: 750.00 -> 750.00 (+0.00)
- Net GEX: -$57.6M -> -$62.2M (-$4.6M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
