# IWM gamma exposure report

As of 2026-10-23T20:32:43+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 275.75 | The underlying price used for every calculation in this run. |
| Net GEX | -$1.95B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 280.00, 290.00, 278.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 270.00, 265.00, 260.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 280.00: 2026-10-29 28%, 2026-12-18 23%, 2026-11-20 16%; 290.00: 2026-11-20 48%, 2026-12-18 42%, 2026-10-30 5%; 278.00: 2026-10-30 70%, 2026-10-26 19%, 2026-11-20 4% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 270.00: 2026-11-20 50%, 2026-10-30 21%, 2026-12-18 18%; 265.00: 2026-11-20 55%, 2026-12-18 19%, 2026-10-30 18%; 260.00: 2026-12-18 37%, 2026-11-20 33%, 2026-10-30 21% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 270.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 283.52 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $30.49B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $698.6M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$431.3M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±2.72 (1.0%) -> 273.03 to 278.47, exp 2026-10-26 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 1,911,188 calls / 4,059,260 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 290.00 (123,809); puts 260.00 (339,216) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 280 calls, 90,186 OI: 2026-12-18 40% (36,309), 2026-11-20 19% (17,236), 2026-10-29 17% (15,273); put wall 270 puts, 318,212 OI: 2026-11-20 52% (164,329), 2026-12-18 25% (79,849), 2026-10-30 13% (42,454); max call OI 290 calls, 123,809 OI: 2026-12-18 43% (53,668), 2026-11-20 43% (52,841), 2026-10-30 10% (12,211); max put OI 260 puts, 339,216 OI: 2026-12-18 37% (123,855), 2026-11-20 29% (99,553), 2026-10-30 25% (86,466) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 280.00: 90,186 calls; put wall 270.00: 318,212 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 2.12 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 2.64 vol pts (put 22.0%, call 19.3%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 0.0% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 30.7% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 69.3% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$390.5M net, 24.9% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-23T19:22:31+00:00)

- Call wall: 280.00 -> 280.00 (+0.00)
- Put wall: 270.00 -> 270.00 (+0.00)
- Zero gamma: 279.45 -> 283.52 (+4.07)
- Abs gamma strike: 276.00 -> 270.00 (-6.00)
- Net GEX: -$2.32B -> -$1.95B (+$368.8M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
