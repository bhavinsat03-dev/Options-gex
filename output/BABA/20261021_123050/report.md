# BABA gamma exposure report

As of 2026-10-21T16:30:50+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 104.53 | The underlying price used for every calculation in this run. |
| Net GEX | -$21.7M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 110.00, 120.00, 115.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 104.00, 105.00, 100.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 110.00: 2026-11-20 57%, 2026-10-30 21%, 2026-10-23 18%; 120.00: 2026-11-20 82%, 2026-10-30 9%, 2026-11-27 5%; 115.00: 2026-11-20 56%, 2026-10-23 18%, 2026-10-30 17% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 104.00: 2026-10-23 91%, 2026-10-30 8%, 2026-11-13 1%; 105.00: 2026-10-23 44%, 2026-11-20 34%, 2026-10-30 16%; 100.00: 2026-11-20 60%, 2026-10-23 19%, 2026-10-30 10% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 110.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 107.50 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $694.8M | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $4.6M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$8.5M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±2.78 (2.7%) -> 101.74 to 107.31, exp 2026-10-23 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 258,939 calls / 117,102 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 120.00 (30,611); puts 100.00 (14,909) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 110 calls, 15,168 OI: 2026-11-20 62% (9,473), 2026-10-23 19% (2,864), 2026-10-30 15% (2,264); put wall 104 puts, 7,408 OI: 2026-10-23 82% (6,106), 2026-10-30 15% (1,099), 2026-11-13 2% (113); max call OI 120 calls, 30,611 OI: 2026-11-20 66% (20,077), 2026-10-30 14% (4,360), 2026-10-23 12% (3,745); max put OI 100 puts, 14,909 OI: 2026-11-20 67% (10,061), 2026-10-23 15% (2,246), 2026-10-30 7% (1,093) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 110.00: 15,168 calls; put wall 104.00: 7,408 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 0.45 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | -2.34 vol pts (put 40.4%, call 42.8%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 39.1% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 19.0% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 41.9% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$60.9K net, 1.2% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-21T15:30:48+00:00)

- Call wall: 110.00 -> 110.00 (+0.00)
- Put wall: 104.00 -> 104.00 (+0.00)
- Zero gamma: 107.15 -> 107.50 (+0.35)
- Abs gamma strike: 110.00 -> 110.00 (+0.00)
- Net GEX: -$18.2M -> -$21.7M (-$3.5M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
