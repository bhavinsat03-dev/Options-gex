# SPCX gamma exposure report

As of 2026-10-23T20:32:43+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 147.49 | The underlying price used for every calculation in this run. |
| Net GEX | -$87.7M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 150.00, 155.00, 160.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 140.00, 145.00, 135.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 150.00: 2026-11-20 31%, 2026-10-30 23%, 2026-12-18 22%; 155.00: 2026-10-30 29%, 2026-11-20 19%, 2026-12-18 19%; 160.00: 2026-11-20 36%, 2026-10-30 26%, 2026-12-18 12% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 140.00: 2026-11-20 28%, 2026-12-18 20%, 2026-10-30 19%; 145.00: 2026-11-20 24%, 2026-10-26 22%, 2026-10-30 21%; 135.00: 2026-11-20 46%, 2026-12-18 27%, 2026-11-06 11% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 150.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 155.46 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $5.34B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $22.1M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$42.9M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±4.39 (3.0%) -> 143.10 to 151.88, exp 2026-10-26 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 1,166,881 calls / 1,143,710 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 150.00 (53,211); puts 130.00 (75,261) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 150 calls, 53,211 OI: 2026-12-18 37% (19,855), 2026-11-20 37% (19,535), 2026-10-30 13% (6,891); put wall 140 puts, 68,647 OI: 2026-11-20 31% (21,138), 2026-12-18 30% (20,401), 2026-10-26 13% (8,613); max call OI 150 calls, 53,211 OI: 2026-12-18 37% (19,855), 2026-11-20 37% (19,535), 2026-10-30 13% (6,891); max put OI 130 puts, 75,261 OI: 2026-11-20 46% (34,492), 2026-12-18 34% (25,513), 2026-10-30 13% (9,484) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 150.00: 53,211 calls; put wall 140.00: 68,647 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 0.98 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 0.54 vol pts (put 53.0%, call 52.4%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 0.0% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 43.7% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 56.3% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$17.2M net, 18.0% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-23T19:22:31+00:00)

- Call wall: 150.00 -> 150.00 (+0.00)
- Put wall: 150.00 -> 140.00 (-10.00)
- Zero gamma: 146.81 -> 155.46 (+8.65)
- Abs gamma strike: 147.00 -> 150.00 (+3.00)
- Net GEX: -$69.3M -> -$87.7M (-$18.4M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
