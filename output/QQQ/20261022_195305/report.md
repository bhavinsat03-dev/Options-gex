# QQQ gamma exposure report

As of 2026-10-22T23:53:05+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 704.47 | The underlying price used for every calculation in this run. |
| Net GEX | -$9.62B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 720.00, 750.00, 760.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 700.00, 710.00, 690.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 720.00: 2026-11-20 43%, 2026-12-18 19%, 2026-10-30 15%; 750.00: 2026-11-20 39%, 2026-12-18 23%, 2026-11-30 16%; 760.00: 2026-11-20 39%, 2026-12-18 28%, 2026-11-06 21% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 700.00: 2026-10-30 34%, 2026-10-23 26%, 2026-12-18 15%; 710.00: 2026-10-23 65%, 2026-10-30 12%, 2026-11-06 8%; 690.00: 2026-10-30 33%, 2026-11-20 23%, 2026-12-18 21% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 700.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 731.89 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $119.67B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $1.16B | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$137.2M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±10.14 (1.4%) -> 694.32 to 714.61, exp 2026-10-23 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 2,789,473 calls / 4,374,713 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 760.00 (124,348); puts 700.00 (268,898) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 720 calls, 63,524 OI: 2026-11-20 44% (27,965), 2026-12-18 27% (16,899), 2026-10-30 10% (6,106); put wall 700 puts, 268,898 OI: 2026-10-30 31% (82,493), 2026-12-18 29% (77,447), 2026-11-20 22% (58,043); max call OI 760 calls, 124,348 OI: 2026-11-20 30% (37,168), 2026-12-18 21% (25,728), 2026-11-06 21% (25,523); max put OI 700 puts, 268,898 OI: 2026-10-30 31% (82,493), 2026-12-18 29% (77,447), 2026-11-20 22% (58,043) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 720.00: 63,524 calls; put wall 700.00: 268,898 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.57 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 5.08 vol pts (put 28.0%, call 22.9%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 22.2% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 27.6% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 50.2% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$900.3M net, 20.7% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-22T21:56:03+00:00)

- Call wall: 720.00 -> 720.00 (+0.00)
- Put wall: 710.00 -> 700.00 (-10.00)
- Zero gamma: 731.48 -> 731.89 (+0.41)
- Abs gamma strike: 710.00 -> 700.00 (-10.00)
- Net GEX: -$8.81B -> -$9.62B (-$814.2M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
