# IWM gamma exposure report

As of 2026-10-21T15:30:48+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 276.92 | The underlying price used for every calculation in this run. |
| Net GEX | -$537.0M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 277.00, 280.00, 278.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 270.00, 275.00, 265.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 277.00: 2026-10-21 86%, 2026-10-23 7%, 2026-10-22 4%; 280.00: 2026-10-23 29%, 2026-10-29 20%, 2026-10-22 17%; 278.00: 2026-10-30 40%, 2026-10-23 34%, 2026-10-21 8% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 270.00: 2026-11-20 64%, 2026-10-30 23%, 2026-10-23 4%; 275.00: 2026-11-20 46%, 2026-10-23 24%, 2026-10-30 12%; 265.00: 2026-11-20 69%, 2026-10-30 20%, 2026-11-06 5% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 277.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 278.89 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $17.31B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $594.3M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$635.1M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±1.03 (0.4%) -> 275.89 to 277.95, exp 2026-10-21 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 1,103,603 calls / 2,212,842 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 280.00 (80,286); puts 260.00 (208,512) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 277 calls, 20,328 OI: 2026-10-21 40% (8,129), 2026-10-23 22% (4,447), 2026-11-20 9% (1,777); put wall 270 puts, 203,996 OI: 2026-11-20 69% (141,536), 2026-10-30 18% (36,409), 2026-10-23 4% (8,911); max call OI 280 calls, 80,286 OI: 2026-11-20 22% (17,380), 2026-10-29 19% (15,156), 2026-10-23 18% (14,199); max put OI 260 puts, 208,512 OI: 2026-11-20 48% (99,359), 2026-10-30 38% (78,241), 2026-11-06 6% (11,697) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 277.00: 20,328 calls; put wall 270.00: 203,996 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 2.01 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 2.34 vol pts (put 20.1%, call 17.7%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 12.4% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 20.7% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 26.6% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 40.3% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $20.5M net, 0.8% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-21T13:48:32+00:00)

- Call wall: 277.00 -> 277.00 (+0.00)
- Put wall: 270.00 -> 270.00 (+0.00)
- Zero gamma: 279.15 -> 278.89 (-0.26)
- Abs gamma strike: 277.00 -> 277.00 (+0.00)
- Net GEX: -$577.6M -> -$537.0M (+$40.6M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
