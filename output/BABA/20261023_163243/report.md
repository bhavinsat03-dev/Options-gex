# BABA gamma exposure report

As of 2026-10-23T20:32:43+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 99.64 | The underlying price used for every calculation in this run. |
| Net GEX | -$29.1M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 100.00, 110.00, 105.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 100.00, 90.00, 95.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 100.00: 2026-12-18 86%, 2026-11-20 8%, 2026-10-30 6%; 110.00: 2026-11-20 44%, 2026-12-18 34%, 2026-10-30 14%; 105.00: 2026-12-18 31%, 2026-11-06 26%, 2026-10-30 25% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 100.00: 2026-12-18 59%, 2026-11-20 23%, 2026-10-30 13%; 90.00: 2026-12-18 70%, 2026-11-20 21%, 2026-10-30 6%; 95.00: 2026-12-18 42%, 2026-11-20 31%, 2026-10-30 14% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 100.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | n/a | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $1.27B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $1.5M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$2.6M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±4.24 (4.3%) -> 95.40 to 103.88, exp 2026-10-30 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 497,974 calls / 278,820 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 100.00 (31,259); puts 100.00 (48,543) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 100 calls, 31,259 OI: 2026-12-18 92% (28,767), 2026-11-20 6% (1,829), 2026-10-30 2% (587); put wall 100 puts, 48,543 OI: 2026-12-18 72% (34,855), 2026-11-20 20% (9,570), 2026-10-30 5% (2,360); max call OI 100 calls, 31,259 OI: 2026-12-18 92% (28,767), 2026-11-20 6% (1,829), 2026-10-30 2% (587); max put OI 100 puts, 48,543 OI: 2026-12-18 72% (34,855), 2026-11-20 20% (9,570), 2026-10-30 5% (2,360) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 100.00: 31,259 calls; put wall 100.00: 48,543 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 0.56 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | -2.40 vol pts (put 41.6%, call 44.0%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 0.0% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 30.2% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 69.8% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$11.2M net, 41.3% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-23T19:22:31+00:00)

- Call wall: 100.00 -> 100.00 (+0.00)
- Put wall: 100.00 -> 100.00 (+0.00)
- Abs gamma strike: 100.00 -> 100.00 (+0.00)
- Net GEX: -$64.4M -> -$29.1M (+$35.3M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
