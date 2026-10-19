# MU gamma exposure report

As of 2026-10-19T16:33:15+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 910.62 | The underlying price used for every calculation in this run. |
| Net GEX | -$63.4M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 900.00, 910.00, 920.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 910.00, 900.00, 950.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 900.00: 2026-10-19 52%, 2026-10-23 12%, 2026-11-20 11%; 910.00: 2026-10-19 59%, 2026-11-20 23%, 2026-10-21 5%; 920.00: 2026-10-19 76%, 2026-12-18 7%, 2026-10-23 6% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 910.00: 2026-10-19 85%, 2026-10-23 4%, 2026-11-20 3%; 900.00: 2026-10-23 42%, 2026-11-20 20%, 2026-12-18 10%; 950.00: 2026-10-23 28%, 2026-10-30 27%, 2026-11-20 23% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 910.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 911.47 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $16.64B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $63.6M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$110.7M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±11.65 (1.3%) -> 898.96 to 922.27, exp 2026-10-19 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 655,186 calls / 742,386 puts | Open contracts across all fetched expirations and strikes. |
| OI at main walls | call wall 900.00: 16,872 calls; put wall 910.00: 5,862 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.13 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | -3.07 vol pts (put 48.4%, call 51.4%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 24.1% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 24.9% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 14.7% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 36.3% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$35.4M net, 12.0% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-19T16:20:30+00:00)

- Call wall: 920.00 -> 900.00 (-20.00)
- Put wall: 915.00 -> 910.00 (-5.00)
- Zero gamma: 914.62 -> 911.47 (-3.15)
- Abs gamma strike: 920.00 -> 910.00 (-10.00)
- Net GEX: $28.1M -> -$63.4M (-$91.5M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
