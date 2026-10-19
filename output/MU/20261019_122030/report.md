# MU gamma exposure report

As of 2026-10-19T16:20:30+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 916.50 | The underlying price used for every calculation in this run. |
| Net GEX | $28.1M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | positive gamma | Dealer hedging tends to offset price moves, a condition historically associated with lower realized volatility. |
| Call walls (top 3) | 920.00, 915.00, 900.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 915.00, 900.00, 920.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 920.00: 2026-10-19 89%, 2026-12-18 3%, 2026-10-23 3%; 915.00: 2026-10-19 87%, 2026-10-23 8%, 2026-10-21 3%; 900.00: 2026-10-19 33%, 2026-10-23 17%, 2026-11-20 15% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 915.00: 2026-10-19 93%, 2026-10-23 2%, 2026-10-21 2%; 900.00: 2026-10-23 40%, 2026-11-20 20%, 2026-12-18 11%; 920.00: 2026-10-19 66%, 2026-10-23 9%, 2026-11-20 9% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 920.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 914.62 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $17.86B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $62.2M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$123.0M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±10.50 (1.1%) -> 906.00 to 927.01, exp 2026-10-19 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 655,183 calls / 742,320 puts | Open contracts across all fetched expirations and strikes. |
| OI at main walls | call wall 920.00: 7,361 calls; put wall 915.00: 2,521 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.13 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | -0.91 vol pts (put 49.5%, call 50.4%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 27.5% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 24.5% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 14.2% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 33.8% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$30.1M net, 11.1% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-19T16:05:44+00:00)

- Call wall: 920.00 -> 920.00 (+0.00)
- Put wall: 920.00 -> 915.00 (-5.00)
- Zero gamma: 914.85 -> 914.62 (-0.23)
- Abs gamma strike: 920.00 -> 920.00 (+0.00)
- Net GEX: $33.3M -> $28.1M (-$5.2M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
