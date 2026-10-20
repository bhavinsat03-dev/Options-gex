# IWM gamma exposure report

As of 2026-10-20T13:50:37+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 273.46 | The underlying price used for every calculation in this run. |
| Net GEX | -$1.38B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 275.00, 274.00, 278.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 270.00, 265.00, 260.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 275.00: 2026-10-21 44%, 2026-10-23 19%, 2026-10-22 9%; 274.00: 2026-10-20 51%, 2026-10-21 16%, 2026-10-23 16%; 278.00: 2026-10-30 72%, 2026-10-23 13%, 2026-11-20 4% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 270.00: 2026-11-20 59%, 2026-10-30 22%, 2026-10-23 7%; 265.00: 2026-11-20 61%, 2026-10-30 24%, 2026-10-23 7%; 260.00: 2026-11-20 46%, 2026-10-30 43%, 2026-11-06 6% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 275.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 280.43 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $18.62B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $495.0M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$553.8M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±2.10 (0.8%) -> 271.36 to 275.56, exp 2026-10-20 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 1,017,047 calls / 2,103,722 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 290.00 (62,953); puts 270.00 (204,752) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 275 calls, 44,607 OI: 2026-10-21 24% (10,614), 2026-10-23 16% (7,280), 2026-11-06 12% (5,229); put wall 270 puts, 204,752 OI: 2026-11-20 69% (142,217), 2026-10-30 17% (34,707), 2026-10-23 4% (7,540); max call OI 290 calls, 62,953 OI: 2026-11-20 70% (43,985), 2026-10-30 18% (11,541), 2026-10-23 5% (3,083); max put OI 270 puts, 204,752 OI: 2026-11-20 69% (142,217), 2026-10-30 17% (34,707), 2026-10-23 4% (7,540) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 275.00: 44,607 calls; put wall 270.00: 204,752 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 2.07 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 5.37 vol pts (put 22.7%, call 17.4%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 4.2% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 24.0% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 27.2% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 44.7% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $375.5K net, 0.4% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-20T01:26:50+00:00)

- Call wall: 275.00 -> 275.00 (+0.00)
- Put wall: 270.00 -> 270.00 (+0.00)
- Zero gamma: 283.22 -> 280.43 (-2.79)
- Abs gamma strike: 270.00 -> 275.00 (+5.00)
- Net GEX: -$2.37B -> -$1.38B (+$983.5M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
