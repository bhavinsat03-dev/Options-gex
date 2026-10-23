# META gamma exposure report

As of 2026-10-23T20:32:43+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 642.62 | The underlying price used for every calculation in this run. |
| Net GEX | -$122.6M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 700.00, 650.00, 660.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 640.00, 600.00, 630.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 700.00: 2026-11-20 60%, 2026-12-18 20%, 2026-11-27 6%; 650.00: 2026-11-20 28%, 2026-10-30 27%, 2026-10-26 22%; 660.00: 2026-10-30 37%, 2026-11-20 31%, 2026-12-18 16% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 640.00: 2026-12-18 30%, 2026-11-20 28%, 2026-10-30 16%; 600.00: 2026-11-20 33%, 2026-12-18 30%, 2026-10-30 21%; 630.00: 2026-11-20 26%, 2026-12-18 22%, 2026-10-30 19% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 650.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 662.97 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $14.02B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $63.2M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$44.6M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±13.90 (2.2%) -> 628.72 to 656.52, exp 2026-10-26 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 849,072 calls / 514,441 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 700.00 (39,818); puts 600.00 (17,839) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 700 calls, 39,818 OI: 2026-11-20 54% (21,334), 2026-12-18 22% (8,714), 2026-10-30 7% (2,806); put wall 640 puts, 10,549 OI: 2026-12-18 46% (4,849), 2026-11-20 30% (3,190), 2026-10-30 9% (920); max call OI 700 calls, 39,818 OI: 2026-11-20 54% (21,334), 2026-12-18 22% (8,714), 2026-10-30 7% (2,806); max put OI 600 puts, 17,839 OI: 2026-12-18 33% (5,862), 2026-11-20 29% (5,183), 2026-10-30 17% (3,064) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 700.00: 39,818 calls; put wall 640.00: 10,549 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 0.61 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | -0.40 vol pts (put 37.4%, call 37.8%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 0.0% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 26.1% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 73.9% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$8.3M net, 26.5% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-23T19:22:31+00:00)

- Call wall: 700.00 -> 700.00 (+0.00)
- Put wall: 650.00 -> 640.00 (-10.00)
- Zero gamma: 653.77 -> 662.97 (+9.20)
- Abs gamma strike: 645.00 -> 650.00 (+5.00)
- Net GEX: -$431.7M -> -$122.6M (+$309.1M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
