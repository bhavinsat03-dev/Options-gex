# SPY gamma exposure report

As of 2026-10-21T19:01:20+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 771.62 | The underlying price used for every calculation in this run. |
| Net GEX | $2.62B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | positive gamma | Dealer hedging tends to offset price moves, a condition historically associated with lower realized volatility. |
| Call walls (top 3) | 773.00, 770.00, 772.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 769.00, 770.00, 766.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 773.00: 2026-10-21 79%, 2026-10-23 10%, 2026-10-22 8%; 770.00: 2026-10-21 60%, 2026-10-23 25%, 2026-10-22 11%; 772.00: 2026-10-21 77%, 2026-10-23 13%, 2026-10-22 5% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 769.00: 2026-10-23 88%, 2026-10-22 6%, 2026-10-26 3%; 770.00: 2026-10-23 60%, 2026-10-22 19%, 2026-10-26 11%; 766.00: 2026-10-26 78%, 2026-10-23 11%, 2026-10-22 4% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 769.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 771.10 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $15.19B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $636.5M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | $1.19B | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±3.23 (0.4%) -> 768.39 to 774.85, exp 2026-10-21 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 736,626 calls / 1,162,793 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 790.00 (45,816); puts 745.00 (48,110) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 773 calls, 22,110 OI: 2026-10-21 51% (11,351), 2026-10-23 23% (5,065), 2026-10-22 13% (2,917); put wall 769 puts, 40,820 OI: 2026-10-23 76% (30,902), 2026-10-21 12% (5,101), 2026-10-22 4% (1,709); max call OI 790 calls, 45,816 OI: 2026-10-23 79% (36,043), 2026-10-22 5% (2,336), 2026-10-26 5% (2,112); max put OI 745 puts, 48,110 OI: 2026-10-23 79% (38,052), 2026-10-21 7% (3,265), 2026-10-22 6% (2,993) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 773.00: 22,110 calls; put wall 769.00: 40,820 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.58 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | -2.31 vol pts (put 10.7%, call 13.0%, exp 2026-10-28) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 25.7% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 55.6% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 18.6% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 0.0% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $0 net, 0.0% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
