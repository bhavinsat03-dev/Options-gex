# TSLA gamma exposure report

As of 2026-10-22T13:50:59+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 383.88 | The underlying price used for every calculation in this run. |
| Net GEX | $476.6M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | positive gamma | Dealer hedging tends to offset price moves, a condition historically associated with lower realized volatility. |
| Call walls (top 3) | 385.00, 380.00, 400.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 380.00, 375.00, 370.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 385.00: 2026-10-23 79%, 2026-10-30 6%, 2026-10-26 5%; 380.00: 2026-10-23 71%, 2026-10-30 10%, 2026-11-20 7%; 400.00: 2026-10-23 36%, 2026-11-20 25%, 2026-10-30 23% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 380.00: 2026-10-23 49%, 2026-11-20 24%, 2026-10-30 19%; 375.00: 2026-10-23 64%, 2026-11-20 11%, 2026-10-30 9%; 370.00: 2026-10-23 52%, 2026-11-20 18%, 2026-10-30 16% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 385.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 373.12 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $6.94B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $52.4M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$378.8M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±13.62 (3.5%) -> 370.26 to 397.49, exp 2026-10-23 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 714,518 calls / 660,202 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 400.00 (51,456); puts 350.00 (28,643) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 385 calls, 25,717 OI: 2026-10-23 55% (14,201), 2026-11-20 16% (4,213), 2026-10-30 10% (2,537); put wall 380 puts, 19,111 OI: 2026-11-20 40% (7,681), 2026-10-23 30% (5,644), 2026-10-30 21% (3,952); max call OI 400 calls, 51,456 OI: 2026-10-23 38% (19,583), 2026-11-20 29% (15,090), 2026-10-30 18% (9,189); max put OI 350 puts, 28,643 OI: 2026-11-20 38% (10,753), 2026-10-23 31% (8,927), 2026-10-30 9% (2,588) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 385.00: 25,717 calls; put wall 380.00: 19,111 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 0.92 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 9.65 vol pts (put 44.0%, call 34.4%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 50.4% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 21.4% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 28.2% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $3.9M net, 1.4% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-21T19:00:04+00:00)

- Call wall: 400.00 -> 385.00 (-15.00)
- Put wall: 380.00 -> 380.00 (+0.00)
- Zero gamma: 355.05 -> 373.12 (+18.07)
- Abs gamma strike: 400.00 -> 385.00 (-15.00)
- Net GEX: $353.2M -> $476.6M (+$123.4M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
