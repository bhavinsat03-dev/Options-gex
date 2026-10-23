# SPCX gamma exposure report

As of 2026-10-23T19:22:31+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 146.75 | The underlying price used for every calculation in this run. |
| Net GEX | -$69.3M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 150.00, 155.00, 160.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 150.00, 140.00, 145.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 150.00: 2026-11-20 31%, 2026-10-30 23%, 2026-12-18 22%; 155.00: 2026-10-30 29%, 2026-11-20 21%, 2026-12-18 20%; 160.00: 2026-11-20 38%, 2026-10-30 25%, 2026-12-18 13% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 150.00: 2026-10-30 33%, 2026-11-20 24%, 2026-12-18 20%; 140.00: 2026-11-20 26%, 2026-10-26 21%, 2026-12-18 19%; 145.00: 2026-11-20 24%, 2026-10-26 22%, 2026-10-30 20% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 147.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 146.81 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $6.25B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $22.6M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$89.4M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±4.58 (3.1%) -> 142.16 to 151.34, exp 2026-10-26 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 1,166,881 calls / 1,143,710 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 160.00 (76,187); puts 140.00 (87,476) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 150 calls, 64,840 OI: 2026-12-18 31% (19,855), 2026-11-20 30% (19,535), 2026-10-23 18% (11,629); put wall 150 puts, 79,671 OI: 2026-12-18 29% (22,947), 2026-11-20 25% (20,140), 2026-10-30 18% (14,599); max call OI 160 calls, 76,187 OI: 2026-10-23 34% (25,723), 2026-11-20 23% (17,361), 2026-10-30 13% (10,278); max put OI 140 puts, 87,476 OI: 2026-11-20 24% (21,138), 2026-12-18 23% (20,401), 2026-10-23 22% (18,829) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 150.00: 64,840 calls; put wall 150.00: 79,671 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 0.98 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 2.99 vol pts (put 54.0%, call 51.0%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 29.9% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 0.0% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 30.3% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 39.9% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$16.6M net, 12.8% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-23T19:01:06+00:00)

- Call wall: 146.00 -> 150.00 (+4.00)
- Put wall: 146.00 -> 150.00 (+4.00)
- Zero gamma: 146.28 -> 146.81 (+0.53)
- Abs gamma strike: 146.00 -> 147.00 (+1.00)
- Net GEX: -$12.5M -> -$69.3M (-$56.8M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
