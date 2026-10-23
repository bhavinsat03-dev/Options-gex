# MU gamma exposure report

As of 2026-10-23T20:32:43+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 877.55 | The underlying price used for every calculation in this run. |
| Net GEX | -$132.0M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 900.00, 950.00, 1,000.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 850.00, 800.00, 880.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 900.00: 2026-10-26 28%, 2026-10-30 26%, 2026-11-20 17%; 950.00: 2026-10-30 64%, 2026-11-20 17%, 2026-12-18 8%; 1,000.00: 2026-11-20 34%, 2026-12-18 28%, 2026-10-30 23% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 850.00: 2026-11-20 40%, 2026-10-30 18%, 2026-12-18 12%; 800.00: 2026-11-20 33%, 2026-12-18 25%, 2026-10-30 17%; 880.00: 2026-11-20 35%, 2026-10-30 22%, 2026-10-26 15% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 900.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 907.47 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $15.68B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $50.0M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$116.3M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±25.80 (2.9%) -> 851.75 to 903.35, exp 2026-10-26 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 744,363 calls / 812,736 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 1,000.00 (25,877); puts 800.00 (20,934) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 900 calls, 18,621 OI: 2026-11-20 24% (4,553), 2026-12-18 22% (4,178), 2026-10-30 20% (3,663); put wall 850 puts, 18,272 OI: 2026-11-20 45% (8,227), 2026-12-18 19% (3,402), 2026-11-27 14% (2,589); max call OI 1000 calls, 25,877 OI: 2026-10-30 27% (7,063), 2026-11-20 27% (6,917), 2026-12-18 26% (6,618); max put OI 800 puts, 20,934 OI: 2026-11-20 31% (6,532), 2026-12-18 30% (6,244), 2026-10-30 14% (2,968) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 900.00: 18,621 calls; put wall 850.00: 18,272 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.09 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 1.92 vol pts (put 54.1%, call 52.2%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 0.0% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 41.5% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 58.5% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$35.3M net, 20.1% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-23T19:22:31+00:00)

- Call wall: 900.00 -> 900.00 (+0.00)
- Put wall: 900.00 -> 850.00 (-50.00)
- Zero gamma: 875.93 -> 907.47 (+31.54)
- Abs gamma strike: 880.00 -> 900.00 (+20.00)
- Net GEX: -$309.9M -> -$132.0M (+$177.8M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
