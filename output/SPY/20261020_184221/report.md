# SPY gamma exposure report

As of 2026-10-20T22:42:21+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 769.05 | The underlying price used for every calculation in this run. |
| Net GEX | -$8.36B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 770.00, 780.00, 775.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 760.00, 769.00, 765.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 770.00: 2026-10-23 34%, 2026-10-21 21%, 2026-10-30 17%; 780.00: 2026-10-30 32%, 2026-10-23 27%, 2026-11-20 14%; 775.00: 2026-10-23 26%, 2026-10-30 18%, 2026-10-22 17% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 760.00: 2026-10-30 67%, 2026-10-23 12%, 2026-11-20 10%; 769.00: 2026-10-23 71%, 2026-10-21 13%, 2026-10-30 5%; 765.00: 2026-10-30 44%, 2026-10-23 24%, 2026-11-20 12% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 760.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 774.88 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $70.71B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $3.16B | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$2.33B | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±4.38 (0.6%) -> 764.67 to 773.42, exp 2026-10-21 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 2,090,634 calls / 6,079,224 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 800.00 (133,580); puts 745.00 (213,923) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 770 calls, 53,570 OI: 2026-11-20 27% (14,622), 2026-10-23 23% (12,495), 2026-10-30 23% (12,363); put wall 760 puts, 207,043 OI: 2026-10-30 63% (130,192), 2026-11-20 15% (30,725), 2026-10-23 8% (17,116); max call OI 800 calls, 133,580 OI: 2026-11-20 40% (53,605), 2026-10-30 37% (49,272), 2026-10-23 7% (9,483); max put OI 745 puts, 213,923 OI: 2026-10-30 58% (124,939), 2026-10-23 18% (37,711), 2026-11-20 15% (32,440) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 770.00: 53,570 calls; put wall 760.00: 207,043 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 2.91 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 1.90 vol pts (put 14.5%, call 12.6%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 34.8% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 33.5% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 31.7% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$222.9M net, 4.6% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-20T22:32:22+00:00)

- Call wall: 770.00 -> 770.00 (+0.00)
- Put wall: 760.00 -> 760.00 (+0.00)
- Zero gamma: 774.88 -> 774.88 (+0.00)
- Abs gamma strike: 760.00 -> 760.00 (+0.00)
- Net GEX: -$8.36B -> -$8.36B (-$1.3M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
