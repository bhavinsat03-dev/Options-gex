# TSLA gamma exposure report

As of 2026-10-22T19:00:50+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 375.48 | The underlying price used for every calculation in this run. |
| Net GEX | $216.1M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | positive gamma | Dealer hedging tends to offset price moves, a condition historically associated with lower realized volatility. |
| Call walls (top 3) | 380.00, 385.00, 370.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 375.00, 380.00, 370.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 380.00: 2026-10-23 72%, 2026-10-30 9%, 2026-11-20 7%; 385.00: 2026-10-23 71%, 2026-10-30 8%, 2026-11-20 7%; 370.00: 2026-10-23 70%, 2026-11-20 12%, 2026-10-30 6% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 375.00: 2026-10-23 76%, 2026-10-30 6%, 2026-11-20 6%; 380.00: 2026-10-23 60%, 2026-11-20 17%, 2026-10-30 16%; 370.00: 2026-10-23 65%, 2026-10-30 12%, 2026-11-20 12% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 380.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 366.12 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $8.46B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $46.4M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$185.5M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±8.55 (2.3%) -> 366.93 to 384.03, exp 2026-10-23 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 714,518 calls / 660,202 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 400.00 (51,456); puts 350.00 (28,643) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 380 calls, 25,009 OI: 2026-10-23 44% (11,041), 2026-11-20 21% (5,343), 2026-10-30 14% (3,480); put wall 375 puts, 13,888 OI: 2026-10-23 47% (6,585), 2026-11-20 21% (2,848), 2026-10-30 12% (1,625); max call OI 400 calls, 51,456 OI: 2026-10-23 38% (19,583), 2026-11-20 29% (15,090), 2026-10-30 18% (9,189); max put OI 350 puts, 28,643 OI: 2026-11-20 38% (10,753), 2026-10-23 31% (8,927), 2026-10-30 9% (2,588) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 380.00: 25,009 calls; put wall 375.00: 13,888 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 0.92 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | -0.20 vol pts (put 40.3%, call 40.5%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 52.0% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 21.6% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 26.4% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $1.1M net, 1.3% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-22T16:30:29+00:00)

- Call wall: 385.00 -> 380.00 (-5.00)
- Put wall: 380.00 -> 375.00 (-5.00)
- Zero gamma: 367.72 -> 366.12 (-1.60)
- Abs gamma strike: 380.00 -> 380.00 (+0.00)
- Net GEX: $295.9M -> $216.1M (-$79.8M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
