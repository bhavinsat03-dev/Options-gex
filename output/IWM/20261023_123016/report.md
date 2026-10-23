# IWM gamma exposure report

As of 2026-10-23T16:30:16+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 275.79 | The underlying price used for every calculation in this run. |
| Net GEX | -$2.26B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 276.00, 275.00, 280.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 276.00, 270.00, 275.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 276.00: 2026-10-23 90%, 2026-10-26 3%, 2026-10-27 2%; 275.00: 2026-10-23 58%, 2026-12-18 15%, 2026-10-28 6%; 280.00: 2026-10-29 27%, 2026-12-18 23%, 2026-11-20 15% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 276.00: 2026-10-23 94%, 2026-10-26 2%, 2026-10-30 1%; 270.00: 2026-11-20 50%, 2026-10-30 20%, 2026-12-18 18%; 275.00: 2026-10-23 44%, 2026-11-20 23%, 2026-12-18 15% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 276.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 279.23 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $31.51B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $699.4M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$410.0M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±1.11 (0.4%) -> 274.68 to 276.90, exp 2026-10-23 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 1,911,188 calls / 4,059,260 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 290.00 (127,159); puts 260.00 (346,166) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 276 calls, 20,396 OI: 2026-10-23 42% (8,598), 2026-11-20 15% (3,109), 2026-10-30 10% (2,072); put wall 276 puts, 20,026 OI: 2026-10-23 51% (10,234), 2026-11-20 11% (2,294), 2026-10-30 9% (1,745); max call OI 290 calls, 127,159 OI: 2026-12-18 42% (53,668), 2026-11-20 42% (52,841), 2026-10-30 10% (12,211); max put OI 260 puts, 346,166 OI: 2026-12-18 36% (123,855), 2026-11-20 29% (99,553), 2026-10-30 25% (86,466) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 276.00: 20,396 calls; put wall 276.00: 20,026 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 2.12 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 2.40 vol pts (put 22.0%, call 19.6%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 21.1% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 0.0% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 24.3% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 54.6% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$390.5M net, 19.7% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-23T16:12:39+00:00)

- Call wall: 276.00 -> 276.00 (+0.00)
- Put wall: 270.00 -> 276.00 (+6.00)
- Zero gamma: 279.34 -> 279.23 (-0.11)
- Abs gamma strike: 276.00 -> 276.00 (+0.00)
- Net GEX: -$2.29B -> -$2.26B (+$31.4M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
