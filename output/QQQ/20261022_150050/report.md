# QQQ gamma exposure report

As of 2026-10-22T19:00:50+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 703.06 | The underlying price used for every calculation in this run. |
| Net GEX | -$8.42B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 720.00, 750.00, 740.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 700.00, 710.00, 690.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 720.00: 2026-11-20 53%, 2026-10-30 18%, 2026-10-23 13%; 750.00: 2026-11-20 51%, 2026-11-30 21%, 2026-10-30 16%; 740.00: 2026-10-30 47%, 2026-11-20 28%, 2026-10-27 10% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 700.00: 2026-10-30 40%, 2026-10-23 30%, 2026-11-20 17%; 710.00: 2026-10-23 66%, 2026-10-30 14%, 2026-11-06 10%; 690.00: 2026-10-30 40%, 2026-11-20 28%, 2026-10-23 13% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 700.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 724.21 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $82.89B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $591.9M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$255.2M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±2.76 (0.4%) -> 700.30 to 705.82, exp 2026-10-22 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 1,782,261 calls / 2,920,255 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 760.00 (99,249); puts 700.00 (196,305) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 720 calls, 48,056 OI: 2026-11-20 58% (27,965), 2026-10-30 13% (6,106), 2026-10-23 11% (5,419); put wall 700 puts, 196,305 OI: 2026-10-30 42% (82,493), 2026-11-20 30% (58,043), 2026-10-23 10% (20,161); max call OI 760 calls, 99,249 OI: 2026-11-20 37% (37,168), 2026-11-06 26% (25,523), 2026-10-30 17% (17,357); max put OI 700 puts, 196,305 OI: 2026-10-30 42% (82,493), 2026-11-20 30% (58,043), 2026-10-23 10% (20,161) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 720.00: 48,056 calls; put wall 700.00: 196,305 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.64 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 5.39 vol pts (put 28.7%, call 23.3%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 25.3% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 34.2% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 40.5% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$148.7M net, 3.5% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-22T16:30:29+00:00)

- Call wall: 720.00 -> 720.00 (+0.00)
- Put wall: 710.00 -> 700.00 (-10.00)
- Zero gamma: 724.83 -> 724.21 (-0.62)
- Abs gamma strike: 710.00 -> 700.00 (-10.00)
- Net GEX: -$9.87B -> -$8.42B (+$1.45B)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
