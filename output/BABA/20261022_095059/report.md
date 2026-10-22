# BABA gamma exposure report

As of 2026-10-22T13:50:59+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 102.34 | The underlying price used for every calculation in this run. |
| Net GEX | -$19.5M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 110.00, 105.00, 120.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 104.00, 100.00, 105.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 110.00: 2026-11-20 47%, 2026-10-30 27%, 2026-10-23 18%; 105.00: 2026-10-23 47%, 2026-11-06 21%, 2026-10-30 20%; 120.00: 2026-11-20 85%, 2026-10-30 10%, 2026-11-06 4% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 104.00: 2026-10-23 91%, 2026-10-30 8%, 2026-11-06 0%; 100.00: 2026-11-20 42%, 2026-10-23 34%, 2026-10-30 15%; 105.00: 2026-10-23 43%, 2026-11-20 35%, 2026-10-30 16% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 105.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 104.99 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $689.8M | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $3.8M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$5.0M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±2.13 (2.1%) -> 100.22 to 104.48, exp 2026-10-23 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 281,918 calls / 122,256 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 120.00 (32,405); puts 100.00 (15,987) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 110 calls, 19,771 OI: 2026-11-20 47% (9,258), 2026-10-30 24% (4,708), 2026-10-23 22% (4,389); put wall 104 puts, 7,870 OI: 2026-10-23 84% (6,587), 2026-10-30 15% (1,202), 2026-11-06 1% (81); max call OI 120 calls, 32,405 OI: 2026-11-20 63% (20,304), 2026-10-30 18% (5,907), 2026-10-23 11% (3,704); max put OI 100 puts, 15,987 OI: 2026-11-20 61% (9,701), 2026-10-23 16% (2,527), 2026-10-30 12% (1,988) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 110.00: 19,771 calls; put wall 104.00: 7,870 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 0.43 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 0.10 vol pts (put 42.9%, call 42.8%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 39.9% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 25.7% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 34.4% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$282.0K net, 0.5% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-21T19:00:04+00:00)

- Call wall: 110.00 -> 110.00 (+0.00)
- Put wall: 104.00 -> 104.00 (+0.00)
- Zero gamma: 107.04 -> 104.99 (-2.05)
- Abs gamma strike: 104.00 -> 105.00 (+1.00)
- Net GEX: -$27.2M -> -$19.5M (+$7.7M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
