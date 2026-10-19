# IWM gamma exposure report

As of 2026-10-19T21:59:34+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 271.28 | The underlying price used for every calculation in this run. |
| Net GEX | -$1.22B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 278.00, 275.00, 272.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 270.00, 272.00, 265.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 278.00: 2026-10-30 73%, 2026-10-23 12%, 2026-10-26 7%; 275.00: 2026-10-23 27%, 2026-10-21 18%, 2026-10-22 15%; 272.00: 2026-10-20 51%, 2026-10-21 20%, 2026-10-23 19% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 270.00: 2026-10-30 49%, 2026-10-23 17%, 2026-10-20 14%; 272.00: 2026-10-30 57%, 2026-10-23 19%, 2026-10-22 6%; 265.00: 2026-10-30 74%, 2026-10-23 12%, 2026-11-13 5% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 272.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 278.12 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $8.23B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $168.9M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$226.2M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±2.14 (0.8%) -> 269.13 to 273.42, exp 2026-10-20 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 568,837 calls / 928,967 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 278.00 (39,276); puts 260.00 (102,019) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| OI at main walls | call wall 278.00: 39,276 calls; put wall 270.00: 57,968 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.63 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 3.05 vol pts (put 21.5%, call 18.5%, exp 2026-11-13) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 39.5% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 47.3% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 13.1% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $0 net, 0.0% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-19T19:21:22+00:00)

- Call wall: 278.00 -> 278.00 (+0.00)
- Put wall: 270.00 -> 270.00 (+0.00)
- Zero gamma: 273.77 -> 278.12 (+4.35)
- Abs gamma strike: 272.00 -> 272.00 (+0.00)
- Net GEX: -$1.25B -> -$1.22B (+$34.7M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
