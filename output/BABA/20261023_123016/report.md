# BABA gamma exposure report

As of 2026-10-23T16:30:16+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 99.98 | The underlying price used for every calculation in this run. |
| Net GEX | -$106.0M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 100.00, 110.00, 105.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 100.00, 110.00, 105.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 100.00: 2026-12-18 64%, 2026-10-23 26%, 2026-11-20 6%; 110.00: 2026-11-20 43%, 2026-12-18 33%, 2026-10-30 16%; 105.00: 2026-12-18 30%, 2026-10-30 26%, 2026-11-06 26% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 100.00: 2026-10-23 84%, 2026-12-18 9%, 2026-11-20 4%; 110.00: 2026-12-18 60%, 2026-11-20 37%, 2026-11-13 2%; 105.00: 2026-12-18 40%, 2026-11-20 37%, 2026-10-30 16% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 100.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 104.10 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $1.29B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $1.6M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | $2.1M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±0.57 (0.6%) -> 99.41 to 100.56, exp 2026-10-23 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 497,974 calls / 278,820 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 100.00 (31,509); puts 100.00 (52,845) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 100 calls, 31,509 OI: 2026-12-18 91% (28,767), 2026-11-20 6% (1,829), 2026-10-30 2% (587); put wall 100 puts, 52,845 OI: 2026-12-18 66% (34,855), 2026-11-20 18% (9,570), 2026-10-23 8% (4,302); max call OI 100 calls, 31,509 OI: 2026-12-18 91% (28,767), 2026-11-20 6% (1,829), 2026-10-30 2% (587); max put OI 100 puts, 52,845 OI: 2026-12-18 66% (34,855), 2026-11-20 18% (9,570), 2026-10-23 8% (4,302) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 100.00: 31,509 calls; put wall 100.00: 52,845 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 0.56 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | -3.36 vol pts (put 41.1%, call 44.5%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 50.9% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 0.0% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 14.7% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 34.4% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$11.7M net, 20.3% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-23T16:12:39+00:00)

- Call wall: 100.00 -> 100.00 (+0.00)
- Put wall: 100.00 -> 100.00 (+0.00)
- Zero gamma: 105.49 -> 104.10 (-1.39)
- Abs gamma strike: 100.00 -> 100.00 (+0.00)
- Net GEX: -$64.2M -> -$106.0M (-$41.8M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
