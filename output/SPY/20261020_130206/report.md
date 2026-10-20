# SPY gamma exposure report

As of 2026-10-20T17:02:06+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 768.44 | The underlying price used for every calculation in this run. |
| Net GEX | -$7.22B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 770.00, 769.00, 768.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 760.00, 769.00, 768.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 770.00: 2026-10-20 47%, 2026-10-23 19%, 2026-10-21 10%; 769.00: 2026-10-20 77%, 2026-10-21 11%, 2026-10-23 4%; 768.00: 2026-10-20 78%, 2026-10-23 6%, 2026-10-21 5% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 760.00: 2026-10-30 66%, 2026-10-23 12%, 2026-11-20 10%; 769.00: 2026-10-23 46%, 2026-10-20 36%, 2026-10-21 7%; 768.00: 2026-10-20 73%, 2026-10-21 10%, 2026-10-23 6% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 769.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 771.22 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $75.26B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $3.21B | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$2.77B | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±2.23 (0.3%) -> 766.21 to 770.67, exp 2026-10-20 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 2,090,639 calls / 6,079,224 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 800.00 (135,595); puts 745.00 (228,702) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 770 calls, 63,413 OI: 2026-11-20 23% (14,622), 2026-10-23 20% (12,495), 2026-10-30 19% (12,363); put wall 760 puts, 214,367 OI: 2026-10-30 61% (130,192), 2026-11-20 14% (30,725), 2026-10-23 8% (17,116); max call OI 800 calls, 135,595 OI: 2026-11-20 40% (53,605), 2026-10-30 36% (49,272), 2026-10-23 7% (9,483); max put OI 745 puts, 228,702 OI: 2026-10-30 55% (124,939), 2026-10-23 16% (37,711), 2026-11-20 14% (32,440) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 770.00: 63,413 calls; put wall 760.00: 214,367 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 2.91 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 2.19 vol pts (put 14.9%, call 12.7%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 16.8% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 28.7% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 28.1% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 26.4% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$235.3M net, 3.8% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-20T13:57:35+00:00)

- Call wall: 767.00 -> 770.00 (+3.00)
- Put wall: 760.00 -> 760.00 (+0.00)
- Zero gamma: 770.48 -> 771.22 (+0.74)
- Abs gamma strike: 767.00 -> 769.00 (+2.00)
- Net GEX: -$6.95B -> -$7.22B (-$269.2M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
