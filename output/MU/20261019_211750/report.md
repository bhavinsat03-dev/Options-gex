# MU gamma exposure report

As of 2026-10-20T01:17:50+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 904.90 | The underlying price used for every calculation in this run. |
| Net GEX | -$143.2M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 900.00, 1,000.00, 950.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 900.00, 850.00, 950.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 900.00: 2026-10-23 25%, 2026-10-21 23%, 2026-11-20 21%; 1,000.00: 2026-11-20 25%, 2026-12-18 24%, 2026-10-23 19%; 950.00: 2026-10-23 39%, 2026-11-20 17%, 2026-10-30 14% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 900.00: 2026-10-23 40%, 2026-11-20 20%, 2026-12-18 11%; 850.00: 2026-11-20 36%, 2026-10-23 27%, 2026-12-18 12%; 950.00: 2026-10-23 29%, 2026-10-30 25%, 2026-11-20 23% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 900.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 936.85 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $17.38B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $54.6M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$163.8M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±30.65 (3.4%) -> 874.25 to 935.55, exp 2026-10-21 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 604,090 calls / 713,549 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 1,000.00 (24,463); puts 900.00 (20,627) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 900 calls, 14,320 OI: 2026-11-20 31% (4,501), 2026-12-18 25% (3,620), 2026-10-23 15% (2,182); put wall 900 puts, 20,627 OI: 2026-11-20 29% (6,006), 2026-10-23 23% (4,717), 2026-12-18 22% (4,441); max call OI 1000 calls, 24,463 OI: 2026-12-18 26% (6,446), 2026-10-23 22% (5,453), 2026-11-20 22% (5,401); max put OI 900 puts, 20,627 OI: 2026-11-20 29% (6,006), 2026-10-23 23% (4,717), 2026-12-18 22% (4,441) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 900.00: 14,320 calls; put wall 900.00: 20,627 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.18 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 0.33 vol pts (put 50.4%, call 50.1%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 34.0% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 19.2% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 46.8% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$28.1M net, 15.5% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-19T21:59:34+00:00)

- Call wall: 900.00 -> 900.00 (+0.00)
- Put wall: 900.00 -> 900.00 (+0.00)
- Zero gamma: 935.49 -> 936.85 (+1.36)
- Abs gamma strike: 900.00 -> 900.00 (+0.00)
- Net GEX: -$150.4M -> -$143.2M (+$7.2M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
