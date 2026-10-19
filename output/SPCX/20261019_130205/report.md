# SPCX gamma exposure report

As of 2026-10-19T17:02:05+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 148.70 | The underlying price used for every calculation in this run. |
| Net GEX | -$35.3M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 149.00, 150.00, 155.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 148.00, 140.00, 150.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 149.00: 2026-10-19 92%, 2026-10-23 4%, 2026-10-21 2%; 150.00: 2026-10-19 31%, 2026-11-20 23%, 2026-12-18 18%; 155.00: 2026-10-23 27%, 2026-12-18 20%, 2026-11-20 19% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 148.00: 2026-10-19 91%, 2026-10-28 4%, 2026-10-23 2%; 140.00: 2026-11-20 25%, 2026-12-18 24%, 2026-10-23 24%; 150.00: 2026-11-20 29%, 2026-12-18 24%, 2026-10-30 19% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 148.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 148.93 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $5.53B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $19.3M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$149.5M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±1.23 (0.8%) -> 147.47 to 149.94, exp 2026-10-19 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 931,825 calls / 995,503 puts | Open contracts across all fetched expirations and strikes. |
| OI at main walls | call wall 149.00: 9,408 calls; put wall 148.00: 16,935 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.07 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | -0.31 vol pts (put 56.9%, call 57.2%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 28.7% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 23.6% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 12.2% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 35.6% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$14.9M net, 12.7% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-19T16:33:15+00:00)

- Call wall: 150.00 -> 149.00 (-1.00)
- Put wall: 140.00 -> 148.00 (+8.00)
- Zero gamma: 149.20 -> 148.93 (-0.27)
- Abs gamma strike: 150.00 -> 148.00 (-2.00)
- Net GEX: $6.0M -> -$35.3M (-$41.4M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
