# IWM gamma exposure report

As of 2026-10-23T16:12:39+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 276.18 | The underlying price used for every calculation in this run. |
| Net GEX | -$2.29B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 276.00, 280.00, 290.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 270.00, 277.00, 276.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 276.00: 2026-10-23 91%, 2026-10-26 3%, 2026-10-27 2%; 280.00: 2026-10-29 28%, 2026-12-18 23%, 2026-11-20 15%; 290.00: 2026-11-20 48%, 2026-12-18 42%, 2026-10-30 6% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 270.00: 2026-11-20 50%, 2026-10-30 20%, 2026-12-18 18%; 277.00: 2026-10-23 91%, 2026-11-20 3%, 2026-10-26 3%; 276.00: 2026-10-23 93%, 2026-10-26 2%, 2026-10-30 1% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 276.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 279.34 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $32.08B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $704.6M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$184.4M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±1.18 (0.4%) -> 275.00 to 277.36, exp 2026-10-23 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 1,911,188 calls / 4,059,260 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 290.00 (127,159); puts 260.00 (346,166) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 276 calls, 20,396 OI: 2026-10-23 42% (8,598), 2026-11-20 15% (3,109), 2026-10-30 10% (2,072); put wall 270 puts, 329,005 OI: 2026-11-20 50% (164,329), 2026-12-18 24% (79,849), 2026-10-30 13% (42,454); max call OI 290 calls, 127,159 OI: 2026-12-18 42% (53,668), 2026-11-20 42% (52,841), 2026-10-30 10% (12,211); max put OI 260 puts, 346,166 OI: 2026-12-18 36% (123,855), 2026-11-20 29% (99,553), 2026-10-30 25% (86,466) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 276.00: 20,396 calls; put wall 270.00: 329,005 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 2.12 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 2.83 vol pts (put 21.9%, call 19.0%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 23.4% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 0.0% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 23.6% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 53.0% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$373.1M net, 19.1% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-23T13:51:27+00:00)

- Call wall: 275.00 -> 276.00 (+1.00)
- Put wall: 270.00 -> 270.00 (+0.00)
- Zero gamma: 279.85 -> 279.34 (-0.51)
- Abs gamma strike: 275.00 -> 276.00 (+1.00)
- Net GEX: -$2.41B -> -$2.29B (+$118.3M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
