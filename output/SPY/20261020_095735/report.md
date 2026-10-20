# SPY gamma exposure report

As of 2026-10-20T13:57:35+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 767.21 | The underlying price used for every calculation in this run. |
| Net GEX | -$6.95B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 767.00, 768.00, 770.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 760.00, 765.00, 750.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 767.00: 2026-10-20 80%, 2026-10-21 5%, 2026-10-22 4%; 768.00: 2026-10-20 74%, 2026-10-23 7%, 2026-10-21 7%; 770.00: 2026-10-23 32%, 2026-10-30 16%, 2026-10-21 15% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 760.00: 2026-10-30 63%, 2026-10-23 12%, 2026-11-20 10%; 765.00: 2026-10-20 32%, 2026-10-30 31%, 2026-10-23 14%; 750.00: 2026-10-30 40%, 2026-11-20 32%, 2026-10-23 9% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 767.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 770.48 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $79.09B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $3.12B | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$3.72B | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±3.87 (0.5%) -> 763.34 to 771.08, exp 2026-10-20 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 2,090,639 calls / 6,079,224 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 800.00 (135,595); puts 745.00 (228,702) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 767 calls, 18,580 OI: 2026-10-20 23% (4,247), 2026-10-30 16% (2,880), 2026-11-20 15% (2,829); put wall 760 puts, 214,367 OI: 2026-10-30 61% (130,192), 2026-11-20 14% (30,725), 2026-10-23 8% (17,116); max call OI 800 calls, 135,595 OI: 2026-11-20 40% (53,605), 2026-10-30 36% (49,272), 2026-10-23 7% (9,483); max put OI 745 puts, 228,702 OI: 2026-10-30 55% (124,939), 2026-10-23 16% (37,711), 2026-11-20 14% (32,440) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 767.00: 18,580 calls; put wall 760.00: 214,367 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 2.91 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 5.19 vol pts (put 17.1%, call 11.9%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 16.5% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 27.7% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 28.5% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 27.3% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$194.3M net, 4.0% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-20T13:50:37+00:00)

- Call wall: 766.00 -> 767.00 (+1.00)
- Put wall: 760.00 -> 760.00 (+0.00)
- Zero gamma: 771.68 -> 770.48 (-1.20)
- Abs gamma strike: 765.00 -> 767.00 (+2.00)
- Net GEX: -$11.12B -> -$6.95B (+$4.17B)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
