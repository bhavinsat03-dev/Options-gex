# TSLA gamma exposure report

As of 2026-10-19T16:20:30+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 368.14 | The underlying price used for every calculation in this run. |
| Net GEX | $386.9M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | positive gamma | Dealer hedging tends to offset price moves, a condition historically associated with lower realized volatility. |
| Call walls (top 3) | 370.00, 367.50, 400.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 370.00, 350.00, 367.50 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 370.00: 2026-10-19 81%, 2026-10-23 9%, 2026-11-20 4%; 367.50: 2026-10-19 96%, 2026-10-23 3%, 2026-10-30 0%; 400.00: 2026-11-20 29%, 2026-10-23 22%, 2026-10-30 20% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 370.00: 2026-10-19 48%, 2026-11-20 14%, 2026-10-23 14%; 350.00: 2026-12-18 30%, 2026-11-20 29%, 2026-10-23 16%; 367.50: 2026-10-19 91%, 2026-10-23 5%, 2026-10-26 2% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 370.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 355.51 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $12.00B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $53.4M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$238.3M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±2.96 (0.8%) -> 365.18 to 371.10, exp 2026-10-19 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 1,071,838 calls / 864,444 puts | Open contracts across all fetched expirations and strikes. |
| OI at main walls | call wall 370.00: 33,825 calls; put wall 370.00: 17,280 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 0.81 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | -0.31 vol pts (put 44.8%, call 45.1%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 33.4% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 20.2% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 11.2% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 35.1% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$10.1M net, 14.1% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-19T16:05:44+00:00)

- Call wall: 370.00 -> 370.00 (+0.00)
- Put wall: 350.00 -> 370.00 (+20.00)
- Zero gamma: 355.19 -> 355.51 (+0.32)
- Abs gamma strike: 370.00 -> 370.00 (+0.00)
- Net GEX: $375.4M -> $386.9M (+$11.5M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
