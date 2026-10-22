# BABA gamma exposure report

As of 2026-10-22T21:56:03+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 101.82 | The underlying price used for every calculation in this run. |
| Net GEX | -$26.9M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 110.00, 120.00, 105.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 104.00, 100.00, 105.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 110.00: 2026-11-20 57%, 2026-10-30 32%, 2026-11-06 7%; 120.00: 2026-11-20 83%, 2026-10-30 8%, 2026-11-27 5%; 105.00: 2026-10-23 36%, 2026-11-06 25%, 2026-10-30 24% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 104.00: 2026-10-23 90%, 2026-10-30 9%, 2026-11-13 1%; 100.00: 2026-10-23 40%, 2026-11-20 37%, 2026-10-30 15%; 105.00: 2026-11-20 38%, 2026-10-23 37%, 2026-10-30 19% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 104.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 105.78 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $757.4M | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $2.9M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | $5.9M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±2.04 (2.0%) -> 99.78 to 103.85, exp 2026-10-23 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 281,918 calls / 122,256 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 120.00 (32,405); puts 100.00 (15,987) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 110 calls, 19,771 OI: 2026-11-20 47% (9,258), 2026-10-30 24% (4,708), 2026-10-23 22% (4,389); put wall 104 puts, 8,054 OI: 2026-10-23 82% (6,587), 2026-10-30 15% (1,202), 2026-11-13 1% (112); max call OI 120 calls, 32,405 OI: 2026-11-20 63% (20,304), 2026-10-30 18% (5,907), 2026-10-23 11% (3,704); max put OI 100 puts, 15,987 OI: 2026-11-20 61% (9,701), 2026-10-23 16% (2,527), 2026-10-30 12% (1,988) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 110.00: 19,771 calls; put wall 104.00: 8,054 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 0.43 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | -2.11 vol pts (put 42.4%, call 44.5%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 37.6% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 25.7% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 36.7% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$22.0K net, 1.4% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-22T19:00:50+00:00)

- Call wall: 110.00 -> 110.00 (+0.00)
- Put wall: 100.00 -> 104.00 (+4.00)
- Zero gamma: 105.01 -> 105.78 (+0.77)
- Abs gamma strike: 100.00 -> 104.00 (+4.00)
- Net GEX: -$18.9M -> -$26.9M (-$8.0M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
