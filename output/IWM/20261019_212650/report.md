# IWM gamma exposure report

As of 2026-10-20T01:26:50+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 271.28 | The underlying price used for every calculation in this run. |
| Net GEX | -$2.37B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 275.00, 278.00, 272.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 270.00, 265.00, 260.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 275.00: 2026-10-23 23%, 2026-10-21 17%, 2026-10-22 13%; 278.00: 2026-10-30 69%, 2026-10-23 12%, 2026-10-26 7%; 272.00: 2026-10-20 36%, 2026-11-20 25%, 2026-10-23 15% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 270.00: 2026-11-20 56%, 2026-10-30 22%, 2026-10-23 7%; 265.00: 2026-11-20 57%, 2026-10-30 31%, 2026-10-23 5%; 260.00: 2026-11-20 45%, 2026-10-30 44%, 2026-11-06 5% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 270.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 283.22 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $19.79B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $388.1M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$341.5M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±2.14 (0.8%) -> 269.13 to 273.42, exp 2026-10-20 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 923,888 calls / 1,979,050 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 290.00 (62,109); puts 270.00 (204,092) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 275 calls, 29,593 OI: 2026-10-23 18% (5,281), 2026-11-20 16% (4,700), 2026-10-21 12% (3,681); put wall 270 puts, 204,092 OI: 2026-11-20 71% (144,999), 2026-10-30 17% (34,440), 2026-10-23 3% (7,076); max call OI 290 calls, 62,109 OI: 2026-11-20 70% (43,596), 2026-10-30 19% (11,511), 2026-10-23 5% (3,081); max put OI 270 puts, 204,092 OI: 2026-11-20 71% (144,999), 2026-10-30 17% (34,440), 2026-10-23 3% (7,076) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 275.00: 29,593 calls; put wall 270.00: 204,092 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 2.14 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 2.90 vol pts (put 21.6%, call 18.7%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 23.0% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 27.4% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 49.6% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$1.7M net, 0.4% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-20T01:21:36+00:00)

- Call wall: 275.00 -> 275.00 (+0.00)
- Put wall: 270.00 -> 270.00 (+0.00)
- Zero gamma: 283.22 -> 283.22 (+0.00)
- Abs gamma strike: 270.00 -> 270.00 (+0.00)
- Net GEX: -$2.37B -> -$2.37B (-$381.5K)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
