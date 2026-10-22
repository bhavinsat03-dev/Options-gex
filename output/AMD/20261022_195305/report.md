# AMD gamma exposure report

As of 2026-10-22T23:53:05+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 507.93 | The underlying price used for every calculation in this run. |
| Net GEX | -$284.5M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 520.00, 600.00, 550.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 500.00, 510.00, 520.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 520.00: 2026-10-23 69%, 2026-11-20 13%, 2026-12-18 8%; 600.00: 2026-11-20 39%, 2026-12-18 33%, 2026-10-30 11%; 550.00: 2026-11-20 41%, 2026-12-18 24%, 2026-10-30 16% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 500.00: 2026-10-23 57%, 2026-11-20 14%, 2026-10-30 11%; 510.00: 2026-10-23 65%, 2026-10-30 10%, 2026-11-13 8%; 520.00: 2026-10-23 61%, 2026-10-30 13%, 2026-11-20 11% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 500.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 547.11 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $8.96B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $12.3M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$21.8M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±16.30 (3.2%) -> 491.63 to 524.23, exp 2026-10-23 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 580,279 calls / 598,443 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 600.00 (24,284); puts 440.00 (23,851) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 520 calls, 6,762 OI: 2026-10-23 33% (2,214), 2026-11-20 29% (1,975), 2026-12-18 24% (1,593); put wall 500 puts, 20,947 OI: 2026-11-20 29% (6,098), 2026-10-23 22% (4,606), 2026-12-18 19% (4,001); max call OI 600 calls, 24,284 OI: 2026-11-20 25% (6,130), 2026-10-23 24% (5,898), 2026-12-18 23% (5,664); max put OI 440 puts, 23,851 OI: 2026-11-20 82% (19,471), 2026-12-18 11% (2,628), 2026-10-23 2% (549) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 520.00: 6,762 calls; put wall 500.00: 20,947 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.03 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 1.23 vol pts (put 62.5%, call 61.3%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 35.6% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 20.9% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 43.5% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$12.9M net, 12.0% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-22T21:56:03+00:00)

- Call wall: 520.00 -> 520.00 (+0.00)
- Put wall: 500.00 -> 500.00 (+0.00)
- Zero gamma: 546.30 -> 547.11 (+0.81)
- Abs gamma strike: 500.00 -> 500.00 (+0.00)
- Net GEX: -$272.3M -> -$284.5M (-$12.1M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
