# QQQ gamma exposure report

As of 2026-10-22T21:56:03+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 704.47 | The underlying price used for every calculation in this run. |
| Net GEX | -$8.81B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 720.00, 750.00, 740.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 710.00, 700.00, 690.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 720.00: 2026-11-20 53%, 2026-10-30 18%, 2026-10-23 11%; 750.00: 2026-11-20 50%, 2026-11-30 21%, 2026-10-30 17%; 740.00: 2026-10-30 47%, 2026-11-20 27%, 2026-10-27 12% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 710.00: 2026-10-23 69%, 2026-10-30 13%, 2026-11-06 9%; 700.00: 2026-10-30 40%, 2026-10-23 29%, 2026-11-20 17%; 690.00: 2026-10-30 42%, 2026-11-20 29%, 2026-10-23 10% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 710.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 731.48 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $84.61B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $649.8M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$99.7M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±10.14 (1.4%) -> 694.32 to 714.61, exp 2026-10-23 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 1,782,261 calls / 2,920,255 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 760.00 (98,620); puts 700.00 (191,451) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 720 calls, 46,625 OI: 2026-11-20 60% (27,965), 2026-10-30 13% (6,106), 2026-10-23 12% (5,419); put wall 710 puts, 116,903 OI: 2026-10-23 40% (46,596), 2026-10-30 21% (24,488), 2026-11-06 19% (22,596); max call OI 760 calls, 98,620 OI: 2026-11-20 38% (37,168), 2026-11-06 26% (25,523), 2026-10-30 18% (17,357); max put OI 700 puts, 191,451 OI: 2026-10-30 43% (82,493), 2026-11-20 30% (58,043), 2026-10-23 11% (20,161) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 720.00: 46,625 calls; put wall 710.00: 116,903 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.64 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 5.09 vol pts (put 28.0%, call 22.9%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 27.0% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 33.6% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 39.4% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$144.9M net, 3.4% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-22T19:00:50+00:00)

- Call wall: 720.00 -> 720.00 (+0.00)
- Put wall: 700.00 -> 710.00 (+10.00)
- Zero gamma: 724.21 -> 731.48 (+7.27)
- Abs gamma strike: 700.00 -> 710.00 (+10.00)
- Net GEX: -$8.42B -> -$8.81B (-$388.6M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
