# META gamma exposure report

As of 2026-10-19T13:42:08+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 701.27 | The underlying price used for every calculation in this run. |
| Net GEX | -$57.6M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 750.00, 800.00, 760.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 705.00, 700.00, 650.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 750.00: 2026-11-20 50%, 2026-10-23 37%, 2026-10-30 8%; 800.00: 2026-12-18 77%, 2026-10-30 23%, 2026-11-13 0%; 760.00: 2026-11-20 63%, 2026-12-18 31%, 2026-11-06 7% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 705.00: 2026-10-19 59%, 2026-10-23 23%, 2026-10-30 13%; 700.00: 2026-12-18 48%, 2026-10-23 44%, 2026-10-26 5%; 650.00: 2026-10-23 57%, 2026-12-18 23%, 2026-10-30 11% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 750.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 704.90 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $8.10B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $48.8M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$258.1M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±14.50 (2.1%) -> 686.77 to 715.77, exp 2026-10-19 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Put/call OI ratio | 0.66 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | -7.15 vol pts (put 48.1%, call 55.2%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 13.9% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 19.2% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 10.1% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 56.8% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $2.7M net, 22.5% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-19T13:38:14+00:00)

- Call wall: 800.00 -> 750.00 (-50.00)
- Put wall: 700.00 -> 705.00 (+5.00)
- Zero gamma: 700.48 -> 704.90 (+4.42)
- Abs gamma strike: 700.00 -> 750.00 (+50.00)
- Net GEX: $10.3M -> -$57.6M (-$67.9M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
