# META gamma exposure report

As of 2026-10-23T13:51:27+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 643.44 | The underlying price used for every calculation in this run. |
| Net GEX | -$285.5M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 650.00, 700.00, 645.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 650.00, 640.00, 630.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 650.00: 2026-10-23 29%, 2026-11-20 20%, 2026-10-30 20%; 700.00: 2026-11-20 59%, 2026-12-18 20%, 2026-11-27 6%; 645.00: 2026-10-23 84%, 2026-11-20 5%, 2026-10-30 4% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 650.00: 2026-10-23 69%, 2026-11-20 10%, 2026-10-30 6%; 640.00: 2026-10-23 61%, 2026-12-18 13%, 2026-11-20 12%; 630.00: 2026-10-23 63%, 2026-11-20 11%, 2026-12-18 9% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 650.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 653.27 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $16.00B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $73.7M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | $420.4M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±13.39 (2.1%) -> 630.05 to 656.84, exp 2026-10-23 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 849,072 calls / 514,441 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 700.00 (47,947); puts 600.00 (26,231) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 650 calls, 17,163 OI: 2026-11-20 32% (5,577), 2026-12-18 31% (5,271), 2026-10-30 16% (2,689); put wall 650 puts, 22,042 OI: 2026-10-23 38% (8,457), 2026-11-20 23% (5,038), 2026-12-18 18% (3,895); max call OI 700 calls, 47,947 OI: 2026-11-20 44% (21,334), 2026-12-18 18% (8,714), 2026-10-23 17% (8,129); max put OI 600 puts, 26,231 OI: 2026-10-23 32% (8,392), 2026-12-18 22% (5,862), 2026-11-20 20% (5,183) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 650.00: 17,163 calls; put wall 650.00: 22,042 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 0.61 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 6.20 vol pts (put 40.7%, call 34.5%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 32.8% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 0.0% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 17.1% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 50.0% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $10.6M net, 18.2% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-22T23:53:05+00:00)

- Call wall: 700.00 -> 650.00 (-50.00)
- Put wall: 650.00 -> 650.00 (+0.00)
- Zero gamma: 695.78 -> 653.27 (-42.51)
- Abs gamma strike: 650.00 -> 650.00 (+0.00)
- Net GEX: -$426.2M -> -$285.5M (+$140.7M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
