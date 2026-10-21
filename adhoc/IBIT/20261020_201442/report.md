# IBIT gamma exposure report

As of 2026-10-21T00:14:42+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 46.71 | The underlying price used for every calculation in this run. |
| Net GEX | $69.3M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | positive gamma | Dealer hedging tends to offset price moves, a condition historically associated with lower realized volatility. |
| Call walls (top 3) | 48.00, 47.00, 46.50 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 48.00, 46.00, 45.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 48.00: 2026-10-23 49%, 2026-10-30 29%, 2026-11-20 18%; 47.00: 2026-10-30 45%, 2026-10-23 34%, 2026-11-20 10%; 46.50: 2026-10-23 84%, 2026-10-30 5%, 2026-10-21 5% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 48.00: 2026-10-30 52%, 2026-11-20 27%, 2026-10-23 16%; 46.00: 2026-10-23 32%, 2026-10-30 24%, 2026-11-20 16%; 45.00: 2026-10-23 32%, 2026-11-20 29%, 2026-10-30 22% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 48.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 45.15 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $2.00B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $17.9M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$45.4M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±0.68 (1.5%) -> 46.03 to 47.39, exp 2026-10-21 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 972,108 calls / 783,759 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 48.00 (95,381); puts 40.00 (60,265) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 48 calls, 95,381 OI: 2026-10-23 34% (32,395), 2026-11-20 31% (29,800), 2026-10-30 28% (27,051); put wall 48 puts, 52,380 OI: 2026-10-30 44% (23,306), 2026-11-20 40% (20,884), 2026-10-23 11% (5,504); max call OI 48 calls, 95,381 OI: 2026-10-23 34% (32,395), 2026-11-20 31% (29,800), 2026-10-30 28% (27,051); max put OI 40 puts, 60,265 OI: 2026-11-20 72% (43,398), 2026-10-30 11% (6,592), 2026-11-30 8% (4,893) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 48.00: 95,381 calls; put wall 48.00: 52,380 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 0.81 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 0.99 vol pts (put 38.1%, call 37.1%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 38.0% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 25.2% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 36.9% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $8.0M net, 7.2% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
