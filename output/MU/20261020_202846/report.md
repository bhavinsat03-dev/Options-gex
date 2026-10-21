# MU gamma exposure report

As of 2026-10-21T00:28:46+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 896.07 | The underlying price used for every calculation in this run. |
| Net GEX | -$166.0M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 900.00, 910.00, 950.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 900.00, 850.00, 880.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 900.00: 2026-10-21 33%, 2026-10-23 25%, 2026-11-20 20%; 910.00: 2026-11-20 41%, 2026-10-21 40%, 2026-10-23 9%; 950.00: 2026-10-23 39%, 2026-10-30 19%, 2026-11-20 17% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 900.00: 2026-10-23 40%, 2026-11-20 18%, 2026-10-21 18%; 850.00: 2026-10-23 37%, 2026-11-20 33%, 2026-10-21 12%; 880.00: 2026-10-23 31%, 2026-11-20 24%, 2026-10-21 21% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 900.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 915.19 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $14.00B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $53.3M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$375.4M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±23.50 (2.6%) -> 872.57 to 919.57, exp 2026-10-21 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 452,244 calls / 494,866 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 1,000.00 (21,192); puts 900.00 (18,567) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 900 calls, 10,609 OI: 2026-11-20 42% (4,445), 2026-10-23 18% (1,926), 2026-10-30 16% (1,725); put wall 900 puts, 18,567 OI: 2026-11-20 34% (6,297), 2026-10-23 26% (4,893), 2026-11-27 11% (2,099); max call OI 1000 calls, 21,192 OI: 2026-10-23 31% (6,523), 2026-11-20 27% (5,722), 2026-10-30 20% (4,151); max put OI 900 puts, 18,567 OI: 2026-11-20 34% (6,297), 2026-10-23 26% (4,893), 2026-11-27 11% (2,099) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 900.00: 10,609 calls; put wall 900.00: 18,567 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.09 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | -0.17 vol pts (put 51.2%, call 51.4%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 45.7% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 20.8% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 33.5% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$13.7M net, 2.5% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-20T22:42:21+00:00)

- Call wall: 900.00 -> 900.00 (+0.00)
- Put wall: 900.00 -> 900.00 (+0.00)
- Zero gamma: 915.53 -> 915.19 (-0.34)
- Abs gamma strike: 900.00 -> 900.00 (+0.00)
- Net GEX: -$186.4M -> -$166.0M (+$20.4M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
