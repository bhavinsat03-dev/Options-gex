# MU gamma exposure report

As of 2026-10-19T17:11:29+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 907.76 | The underlying price used for every calculation in this run. |
| Net GEX | -$98.7M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 910.00, 900.00, 905.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 905.00, 900.00, 910.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 910.00: 2026-10-19 72%, 2026-11-20 15%, 2026-10-21 4%; 900.00: 2026-10-19 43%, 2026-10-23 15%, 2026-10-21 13%; 905.00: 2026-10-19 80%, 2026-10-23 9%, 2026-10-30 4% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 905.00: 2026-10-19 87%, 2026-10-23 6%, 2026-10-30 2%; 900.00: 2026-10-23 38%, 2026-11-20 19%, 2026-12-18 10%; 910.00: 2026-10-19 73%, 2026-10-23 8%, 2026-11-20 6% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 910.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 915.45 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $18.45B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $55.7M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$145.3M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±8.30 (0.9%) -> 899.46 to 916.06, exp 2026-10-19 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 655,183 calls / 742,320 puts | Open contracts across all fetched expirations and strikes. |
| OI at main walls | call wall 910.00: 12,128 calls; put wall 905.00: 3,580 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.13 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 0.82 vol pts (put 50.8%, call 50.0%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 22.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 26.7% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 15.0% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 36.3% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$28.1M net, 12.0% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-19T17:02:05+00:00)

- Call wall: 910.00 -> 910.00 (+0.00)
- Put wall: 905.00 -> 905.00 (+0.00)
- Zero gamma: 915.62 -> 915.45 (-0.17)
- Abs gamma strike: 910.00 -> 910.00 (+0.00)
- Net GEX: -$78.8M -> -$98.7M (-$20.0M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
