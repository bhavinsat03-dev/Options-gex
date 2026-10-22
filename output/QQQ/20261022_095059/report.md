# QQQ gamma exposure report

As of 2026-10-22T13:50:59+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 712.15 | The underlying price used for every calculation in this run. |
| Net GEX | -$10.08B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 720.00, 740.00, 750.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 710.00, 700.00, 711.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 720.00: 2026-11-20 40%, 2026-10-23 28%, 2026-10-30 15%; 740.00: 2026-10-30 46%, 2026-11-20 22%, 2026-10-27 16%; 750.00: 2026-11-20 48%, 2026-10-30 20%, 2026-11-30 19% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 710.00: 2026-10-23 55%, 2026-10-22 21%, 2026-10-30 10%; 700.00: 2026-10-30 48%, 2026-11-20 21%, 2026-10-23 16%; 711.00: 2026-10-23 87%, 2026-10-22 10%, 2026-11-20 1% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 710.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 724.87 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $71.70B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $1.05B | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$1.78B | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±5.85 (0.8%) -> 706.30 to 718.00, exp 2026-10-22 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 1,782,261 calls / 2,920,255 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 760.00 (99,249); puts 700.00 (196,305) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 720 calls, 48,056 OI: 2026-11-20 58% (27,965), 2026-10-30 13% (6,106), 2026-10-23 11% (5,419); put wall 710 puts, 124,813 OI: 2026-10-23 37% (46,596), 2026-10-30 20% (24,488), 2026-11-06 18% (22,596); max call OI 760 calls, 99,249 OI: 2026-11-20 37% (37,168), 2026-11-06 26% (25,523), 2026-10-30 17% (17,357); max put OI 700 puts, 196,305 OI: 2026-10-30 42% (82,493), 2026-11-20 30% (58,043), 2026-10-23 10% (20,161) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 720.00: 48,056 calls; put wall 710.00: 124,813 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.64 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 3.02 vol pts (put 24.7%, call 21.7%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 9.4% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 26.4% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 29.7% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 34.5% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$128.1M net, 2.9% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-21T19:00:04+00:00)

- Call wall: 725.00 -> 720.00 (-5.00)
- Put wall: 720.00 -> 710.00 (-10.00)
- Zero gamma: 728.10 -> 724.87 (-3.23)
- Abs gamma strike: 725.00 -> 710.00 (-15.00)
- Net GEX: -$2.15B -> -$10.08B (-$7.93B)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
