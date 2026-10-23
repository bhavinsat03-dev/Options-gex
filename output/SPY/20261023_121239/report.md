# SPY gamma exposure report

As of 2026-10-23T16:12:39+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 762.91 | The underlying price used for every calculation in this run. |
| Net GEX | -$13.46B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 763.00, 765.00, 762.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 760.00, 750.00, 762.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 763.00: 2026-10-23 86%, 2026-10-26 5%, 2026-10-30 3%; 765.00: 2026-10-23 63%, 2026-10-26 13%, 2026-12-18 6%; 762.00: 2026-10-23 81%, 2026-10-30 8%, 2026-10-26 3% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 760.00: 2026-10-30 45%, 2026-10-23 19%, 2026-11-20 11%; 750.00: 2026-10-26 32%, 2026-11-20 23%, 2026-10-30 23%; 762.00: 2026-10-23 64%, 2026-10-26 19%, 2026-10-27 6% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 762.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 771.02 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $113.26B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $3.66B | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$3.70B | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±2.91 (0.4%) -> 760.00 to 765.82, exp 2026-10-23 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 3,057,693 calls / 8,152,062 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 800.00 (222,046); puts 750.00 (325,623) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 763 calls, 17,254 OI: 2026-10-23 37% (6,447), 2026-10-30 16% (2,747), 2026-10-26 11% (1,909); put wall 760 puts, 190,984 OI: 2026-10-30 41% (78,081), 2026-11-20 18% (34,688), 2026-12-18 12% (22,942); max call OI 800 calls, 222,046 OI: 2026-11-20 39% (85,806), 2026-12-18 25% (55,090), 2026-10-30 22% (49,075); max put OI 750 puts, 325,623 OI: 2026-11-20 27% (87,966), 2026-10-26 27% (86,808), 2026-10-30 17% (55,649) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 763.00: 17,254 calls; put wall 760.00: 190,984 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 2.67 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 3.63 vol pts (put 16.9%, call 13.3%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 22.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 0.0% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 39.7% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 38.3% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $44.8M net, 14.8% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-23T13:51:27+00:00)

- Call wall: 762.00 -> 763.00 (+1.00)
- Put wall: 760.00 -> 760.00 (+0.00)
- Zero gamma: 770.14 -> 771.02 (+0.88)
- Abs gamma strike: 760.00 -> 762.00 (+2.00)
- Net GEX: -$15.94B -> -$13.46B (+$2.49B)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
