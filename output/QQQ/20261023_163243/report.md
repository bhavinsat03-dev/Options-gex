# QQQ gamma exposure report

As of 2026-10-23T20:32:43+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 704.40 | The underlying price used for every calculation in this run. |
| Net GEX | -$7.14B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 720.00, 760.00, 730.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 700.00, 690.00, 680.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 720.00: 2026-11-20 44%, 2026-12-18 18%, 2026-10-30 16%; 760.00: 2026-11-20 35%, 2026-12-18 25%, 2026-11-30 19%; 730.00: 2026-10-30 35%, 2026-11-20 27%, 2026-12-18 22% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 700.00: 2026-10-30 48%, 2026-12-18 17%, 2026-11-20 17%; 690.00: 2026-10-30 46%, 2026-11-20 17%, 2026-12-18 17%; 680.00: 2026-11-20 30%, 2026-12-18 26%, 2026-10-30 14% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 700.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 731.72 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $109.76B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $1.38B | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$966.8M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±9.89 (1.4%) -> 694.51 to 714.29, exp 2026-10-26 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 2,928,122 calls / 4,506,795 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 760.00 (134,186); puts 690.00 (260,225) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 720 calls, 66,529 OI: 2026-11-20 47% (30,997), 2026-12-18 26% (17,337), 2026-10-30 10% (6,776); put wall 700 puts, 256,667 OI: 2026-10-30 34% (88,330), 2026-12-18 30% (78,043), 2026-11-20 22% (56,875); max call OI 760 calls, 134,186 OI: 2026-11-20 29% (38,766), 2026-12-18 19% (25,670), 2026-11-06 18% (24,636); max put OI 690 puts, 260,225 OI: 2026-10-30 33% (87,035), 2026-12-18 27% (70,909), 2026-11-20 21% (55,187) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 720.00: 66,529 calls; put wall 700.00: 256,667 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.54 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 5.03 vol pts (put 27.4%, call 22.3%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 0.0% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 38.9% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 61.1% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$941.3M net, 24.0% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-23T19:22:31+00:00)

- Call wall: 720.00 -> 720.00 (+0.00)
- Put wall: 700.00 -> 700.00 (+0.00)
- Zero gamma: 724.10 -> 731.72 (+7.62)
- Abs gamma strike: 705.00 -> 700.00 (-5.00)
- Net GEX: -$10.30B -> -$7.14B (+$3.17B)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
