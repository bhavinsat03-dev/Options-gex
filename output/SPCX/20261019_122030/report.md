# SPCX gamma exposure report

As of 2026-10-19T16:20:30+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 149.87 | The underlying price used for every calculation in this run. |
| Net GEX | $21.8M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | positive gamma | Dealer hedging tends to offset price moves, a condition historically associated with lower realized volatility. |
| Call walls (top 3) | 150.00, 149.00, 155.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 150.00, 140.00, 145.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 150.00: 2026-10-19 74%, 2026-11-20 9%, 2026-12-18 7%; 149.00: 2026-10-19 85%, 2026-10-23 8%, 2026-10-21 4%; 155.00: 2026-10-23 28%, 2026-12-18 19%, 2026-11-20 19% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 150.00: 2026-10-19 44%, 2026-11-20 16%, 2026-12-18 13%; 140.00: 2026-11-20 25%, 2026-12-18 25%, 2026-10-23 23%; 145.00: 2026-10-23 26%, 2026-11-20 22%, 2026-12-18 17% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 150.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 149.18 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $5.63B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $18.2M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$33.6M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±1.42 (0.9%) -> 148.46 to 151.29, exp 2026-10-19 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 931,825 calls / 995,503 puts | Open contracts across all fetched expirations and strikes. |
| OI at main walls | call wall 150.00: 55,090 calls; put wall 150.00: 54,982 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.07 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | -0.75 vol pts (put 56.4%, call 57.1%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 24.2% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 25.1% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 13.0% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 37.6% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$14.2M net, 13.3% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-19T16:05:44+00:00)

- Call wall: 150.00 -> 150.00 (+0.00)
- Put wall: 150.00 -> 150.00 (+0.00)
- Zero gamma: 150.67 -> 149.18 (-1.49)
- Abs gamma strike: 150.00 -> 150.00 (+0.00)
- Net GEX: $17.4M -> $21.8M (+$4.4M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
