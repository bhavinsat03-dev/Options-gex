# MU gamma exposure report

As of 2026-10-20T16:21:59+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 910.13 | The underlying price used for every calculation in this run. |
| Net GEX | -$82.8M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 900.00, 950.00, 1,000.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 900.00, 950.00, 850.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 900.00: 2026-10-21 29%, 2026-10-23 23%, 2026-11-20 19%; 950.00: 2026-10-23 39%, 2026-10-21 16%, 2026-10-30 16%; 1,000.00: 2026-11-20 25%, 2026-12-18 22%, 2026-10-30 21% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 900.00: 2026-10-23 37%, 2026-10-21 17%, 2026-11-20 16%; 950.00: 2026-10-23 30%, 2026-10-30 28%, 2026-11-20 22%; 850.00: 2026-11-20 36%, 2026-10-23 29%, 2026-12-18 13% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 900.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 918.53 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $18.00B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $71.2M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$325.2M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±24.45 (2.7%) -> 885.68 to 934.58, exp 2026-10-21 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 662,730 calls / 754,917 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 1,000.00 (27,558); puts 900.00 (23,044) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 900 calls, 14,260 OI: 2026-11-20 31% (4,445), 2026-12-18 26% (3,651), 2026-10-23 14% (1,926); put wall 900 puts, 23,044 OI: 2026-11-20 27% (6,297), 2026-10-23 21% (4,893), 2026-12-18 19% (4,477); max call OI 1000 calls, 27,558 OI: 2026-10-23 24% (6,523), 2026-12-18 23% (6,366), 2026-11-20 21% (5,722); max put OI 900 puts, 23,044 OI: 2026-11-20 27% (6,297), 2026-10-23 21% (4,893), 2026-12-18 19% (4,477) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 900.00: 14,260 calls; put wall 900.00: 23,044 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.14 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | -0.95 vol pts (put 49.2%, call 50.2%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 41.0% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 18.7% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 40.3% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$35.2M net, 13.4% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
