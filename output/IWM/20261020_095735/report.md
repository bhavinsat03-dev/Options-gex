# IWM gamma exposure report

As of 2026-10-20T13:57:35+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 273.95 | The underlying price used for every calculation in this run. |
| Net GEX | -$893.4M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 274.00, 275.00, 278.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 270.00, 265.00, 260.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 274.00: 2026-10-20 75%, 2026-10-21 9%, 2026-10-23 8%; 275.00: 2026-10-21 47%, 2026-10-23 17%, 2026-10-22 9%; 278.00: 2026-10-30 70%, 2026-10-23 15%, 2026-11-20 4% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 270.00: 2026-11-20 60%, 2026-10-30 22%, 2026-10-23 7%; 265.00: 2026-11-20 62%, 2026-10-30 24%, 2026-10-23 6%; 260.00: 2026-11-20 46%, 2026-10-30 43%, 2026-11-06 6% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 274.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 280.60 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $18.50B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $497.2M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$539.1M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±2.00 (0.7%) -> 271.96 to 275.95, exp 2026-10-20 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 1,017,047 calls / 2,103,722 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 290.00 (62,953); puts 270.00 (204,752) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 274 calls, 18,998 OI: 2026-10-23 24% (4,608), 2026-10-20 19% (3,593), 2026-10-30 11% (2,132); put wall 270 puts, 204,752 OI: 2026-11-20 69% (142,217), 2026-10-30 17% (34,707), 2026-10-23 4% (7,540); max call OI 290 calls, 62,953 OI: 2026-11-20 70% (43,985), 2026-10-30 18% (11,541), 2026-10-23 5% (3,083); max put OI 270 puts, 204,752 OI: 2026-11-20 69% (142,217), 2026-10-30 17% (34,707), 2026-10-23 4% (7,540) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 274.00: 18,998 calls; put wall 270.00: 204,752 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 2.07 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 5.82 vol pts (put 22.9%, call 17.1%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 9.1% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 23.9% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 25.5% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 41.5% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $780.8K net, 0.4% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-20T13:50:37+00:00)

- Call wall: 275.00 -> 274.00 (-1.00)
- Put wall: 270.00 -> 270.00 (+0.00)
- Zero gamma: 280.43 -> 280.60 (+0.17)
- Abs gamma strike: 275.00 -> 274.00 (-1.00)
- Net GEX: -$1.38B -> -$893.4M (+$489.7M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
