# AMD gamma exposure report

As of 2026-10-23T16:12:39+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 519.49 | The underlying price used for every calculation in this run. |
| Net GEX | -$47.2M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 520.00, 517.50, 522.50 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 520.00, 517.50, 500.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 520.00: 2026-10-23 93%, 2026-10-30 2%, 2026-11-20 2%; 517.50: 2026-10-23 95%, 2026-10-26 5%; 522.50: 2026-10-23 94%, 2026-10-26 6% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 520.00: 2026-10-23 88%, 2026-10-30 4%, 2026-11-20 3%; 517.50: 2026-10-23 96%, 2026-10-26 4%, 2026-10-28 0%; 500.00: 2026-11-20 28%, 2026-10-30 23%, 2026-12-18 15% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 520.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 527.16 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $9.12B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $25.1M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$78.1M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±5.62 (1.1%) -> 513.87 to 525.10, exp 2026-10-23 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 628,523 calls / 612,122 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 620.00 (29,735); puts 440.00 (24,856) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 520 calls, 11,628 OI: 2026-10-23 43% (4,960), 2026-11-20 19% (2,253), 2026-12-18 15% (1,732); put wall 520 puts, 9,663 OI: 2026-11-20 25% (2,405), 2026-10-23 22% (2,107), 2026-12-18 19% (1,856); max call OI 620 calls, 29,735 OI: 2026-11-20 39% (11,516), 2026-10-30 25% (7,573), 2026-10-23 17% (5,171); max put OI 440 puts, 24,856 OI: 2026-11-20 79% (19,685), 2026-12-18 11% (2,665), 2026-10-23 3% (864) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 520.00: 11,628 calls; put wall 520.00: 9,663 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 0.97 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 0.58 vol pts (put 60.7%, call 60.2%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 44.6% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 0.0% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 23.2% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 32.2% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$9.1M net, 8.7% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-23T13:51:27+00:00)

- Call wall: 520.00 -> 520.00 (+0.00)
- Put wall: 510.00 -> 520.00 (+10.00)
- Zero gamma: 531.03 -> 527.16 (-3.87)
- Abs gamma strike: 520.00 -> 520.00 (+0.00)
- Net GEX: -$150.7M -> -$47.2M (+$103.5M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
