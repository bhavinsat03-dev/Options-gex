# AMD gamma exposure report

As of 2026-10-23T19:22:31+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 516.49 | The underlying price used for every calculation in this run. |
| Net GEX | -$157.9M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 600.00, 550.00, 540.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 500.00, 550.00, 440.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 600.00: 2026-11-20 37%, 2026-12-18 33%, 2026-11-06 10%; 550.00: 2026-10-30 32%, 2026-11-20 32%, 2026-12-18 18%; 540.00: 2026-10-30 50%, 2026-11-20 22%, 2026-10-26 11% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 500.00: 2026-11-20 27%, 2026-10-30 24%, 2026-10-26 15%; 550.00: 2026-11-20 49%, 2026-10-30 21%, 2026-12-18 14%; 440.00: 2026-11-20 84%, 2026-12-18 10%, 2026-11-06 2% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 517.50 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 518.70 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $8.87B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $21.1M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$143.6M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±16.32 (3.2%) -> 500.16 to 532.81, exp 2026-10-26 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 628,523 calls / 612,122 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 600.00 (27,264); puts 440.00 (24,856) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 600 calls, 27,264 OI: 2026-11-20 23% (6,346), 2026-12-18 23% (6,181), 2026-10-23 20% (5,442); put wall 500 puts, 22,100 OI: 2026-11-20 28% (6,122), 2026-10-23 21% (4,628), 2026-12-18 18% (4,077); max call OI 600 calls, 27,264 OI: 2026-11-20 23% (6,346), 2026-12-18 23% (6,181), 2026-10-23 20% (5,442); max put OI 440 puts, 24,856 OI: 2026-11-20 79% (19,685), 2026-12-18 11% (2,665), 2026-10-23 3% (864) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 600.00: 27,264 calls; put wall 500.00: 22,100 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 0.97 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 1.46 vol pts (put 61.9%, call 60.4%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 29.1% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 0.0% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 30.2% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 40.7% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$10.0M net, 11.2% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-23T19:01:06+00:00)

- Call wall: 517.50 -> 600.00 (+82.50)
- Put wall: 517.50 -> 500.00 (-17.50)
- Zero gamma: 518.15 -> 518.70 (+0.55)
- Abs gamma strike: 517.50 -> 517.50 (+0.00)
- Net GEX: -$125.4M -> -$157.9M (-$32.5M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
