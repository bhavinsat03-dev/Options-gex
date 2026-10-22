# SPCX gamma exposure report

As of 2026-10-22T19:00:50+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 145.10 | The underlying price used for every calculation in this run. |
| Net GEX | -$112.9M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 150.00, 146.00, 145.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 140.00, 150.00, 145.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 150.00: 2026-11-20 40%, 2026-10-23 30%, 2026-10-30 16%; 146.00: 2026-10-23 92%, 2026-11-06 2%, 2026-10-30 2%; 145.00: 2026-10-23 47%, 2026-11-20 35%, 2026-10-26 7% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 140.00: 2026-10-23 53%, 2026-11-20 21%, 2026-10-30 14%; 150.00: 2026-10-23 41%, 2026-10-30 26%, 2026-11-20 20%; 145.00: 2026-10-23 59%, 2026-11-20 16%, 2026-10-30 13% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 150.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 156.95 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $4.94B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $9.0M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$31.4M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±4.71 (3.2%) -> 140.39 to 149.82, exp 2026-10-23 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 755,348 calls / 780,998 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 170.00 (66,439); puts 140.00 (57,330) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 150 calls, 31,338 OI: 2026-11-20 58% (18,138), 2026-10-23 16% (4,889), 2026-10-30 13% (4,037); put wall 140 puts, 57,330 OI: 2026-11-20 36% (20,468), 2026-10-23 35% (19,896), 2026-10-30 14% (8,003); max call OI 170 calls, 66,439 OI: 2026-10-23 43% (28,600), 2026-11-20 25% (16,492), 2026-10-30 19% (12,325); max put OI 140 puts, 57,330 OI: 2026-11-20 36% (20,468), 2026-10-23 35% (19,896), 2026-10-30 14% (8,003) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 150.00: 31,338 calls; put wall 140.00: 57,330 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.03 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 2.02 vol pts (put 55.4%, call 53.4%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 41.4% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 26.2% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 32.4% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$986.0K net, 0.9% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-22T16:30:29+00:00)

- Call wall: 150.00 -> 150.00 (+0.00)
- Put wall: 150.00 -> 140.00 (-10.00)
- Zero gamma: 153.37 -> 156.95 (+3.58)
- Abs gamma strike: 150.00 -> 150.00 (+0.00)
- Net GEX: -$76.7M -> -$112.9M (-$36.2M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
