# IWM gamma exposure report

As of 2026-10-23T13:51:27+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 274.92 | The underlying price used for every calculation in this run. |
| Net GEX | -$2.41B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 275.00, 280.00, 276.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 270.00, 275.00, 260.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 275.00: 2026-10-23 63%, 2026-12-18 13%, 2026-10-28 5%; 280.00: 2026-10-29 26%, 2026-12-18 25%, 2026-11-20 16%; 276.00: 2026-10-23 77%, 2026-10-26 6%, 2026-10-27 4% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 270.00: 2026-11-20 49%, 2026-10-30 20%, 2026-12-18 17%; 275.00: 2026-10-23 48%, 2026-11-20 22%, 2026-12-18 15%; 260.00: 2026-12-18 34%, 2026-11-20 32%, 2026-10-30 26% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 275.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 279.85 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $33.70B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $666.9M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$381.4M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±2.14 (0.8%) -> 272.78 to 277.06, exp 2026-10-23 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 1,911,188 calls / 4,059,260 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 290.00 (127,159); puts 260.00 (346,166) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 275 calls, 49,977 OI: 2026-12-18 52% (25,822), 2026-10-23 11% (5,434), 2026-11-06 9% (4,627); put wall 270 puts, 329,005 OI: 2026-11-20 50% (164,329), 2026-12-18 24% (79,849), 2026-10-30 13% (42,454); max call OI 290 calls, 127,159 OI: 2026-12-18 42% (53,668), 2026-11-20 42% (52,841), 2026-10-30 10% (12,211); max put OI 260 puts, 346,166 OI: 2026-12-18 36% (123,855), 2026-11-20 29% (99,553), 2026-10-30 25% (86,466) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 275.00: 49,977 calls; put wall 270.00: 329,005 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 2.12 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 4.23 vol pts (put 23.6%, call 19.3%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 19.8% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 0.0% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 24.5% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 55.7% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$381.2M net, 20.1% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-22T23:53:05+00:00)

- Call wall: 280.00 -> 275.00 (-5.00)
- Put wall: 270.00 -> 270.00 (+0.00)
- Zero gamma: 280.52 -> 279.85 (-0.67)
- Abs gamma strike: 270.00 -> 275.00 (+5.00)
- Net GEX: -$1.90B -> -$2.41B (-$513.8M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
