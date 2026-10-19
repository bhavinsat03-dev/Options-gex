# SPY gamma exposure report

As of 2026-10-19T21:59:34+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 766.48 | The underlying price used for every calculation in this run. |
| Net GEX | -$6.46B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 770.00, 780.00, 775.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 760.00, 750.00, 765.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 770.00: 2026-10-23 34%, 2026-10-20 23%, 2026-10-30 18%; 780.00: 2026-10-30 41%, 2026-10-23 36%, 2026-10-22 6%; 775.00: 2026-10-23 26%, 2026-10-30 25%, 2026-10-22 16% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 760.00: 2026-10-30 63%, 2026-10-23 18%, 2026-11-06 4%; 750.00: 2026-10-30 76%, 2026-11-06 9%, 2026-10-23 8%; 765.00: 2026-10-30 53%, 2026-10-23 22%, 2026-10-20 8% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 770.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 772.21 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $41.82B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $1.70B | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$2.02B | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±4.40 (0.6%) -> 762.08 to 770.88, exp 2026-10-20 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 1,514,940 calls / 3,235,545 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 790.00 (77,604); puts 750.00 (160,796) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| OI at main walls | call wall 770.00: 40,600 calls; put wall 760.00: 105,893 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 2.14 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 2.92 vol pts (put 15.5%, call 12.6%, exp 2026-11-13) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 49.5% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 41.0% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 9.4% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $0 net, 0.0% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-19T19:21:22+00:00)

- Call wall: 768.00 -> 770.00 (+2.00)
- Put wall: 768.00 -> 760.00 (-8.00)
- Zero gamma: 767.94 -> 772.21 (+4.27)
- Abs gamma strike: 768.00 -> 770.00 (+2.00)
- Net GEX: $743.5M -> -$6.46B (-$7.20B)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
