# SPCX gamma exposure report

As of 2026-10-22T23:53:05+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 144.75 | The underlying price used for every calculation in this run. |
| Net GEX | -$142.8M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 150.00, 146.00, 145.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 140.00, 145.00, 150.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 150.00: 2026-11-20 31%, 2026-12-18 24%, 2026-10-23 21%; 146.00: 2026-10-23 92%, 2026-11-06 2%, 2026-10-30 2%; 145.00: 2026-10-23 43%, 2026-11-20 31%, 2026-12-18 10% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 140.00: 2026-10-23 46%, 2026-11-20 18%, 2026-12-18 14%; 145.00: 2026-10-23 57%, 2026-11-20 14%, 2026-10-30 11%; 150.00: 2026-10-23 30%, 2026-10-30 24%, 2026-12-18 18% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 150.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 157.41 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $6.32B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $12.4M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$9.5M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±4.81 (3.3%) -> 139.94 to 149.56, exp 2026-10-23 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 1,049,510 calls / 1,096,987 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 170.00 (76,726); puts 130.00 (79,129) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 150 calls, 50,420 OI: 2026-12-18 38% (19,082), 2026-11-20 36% (18,138), 2026-10-23 10% (4,889); put wall 140 puts, 78,039 OI: 2026-12-18 27% (20,709), 2026-11-20 26% (20,468), 2026-10-23 25% (19,896); max call OI 170 calls, 76,726 OI: 2026-10-23 37% (28,600), 2026-11-20 21% (16,492), 2026-10-30 16% (12,325); max put OI 130 puts, 79,129 OI: 2026-11-20 32% (25,400), 2026-12-18 31% (24,923), 2026-10-23 16% (12,417) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 150.00: 50,420 calls; put wall 140.00: 78,039 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.05 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 0.66 vol pts (put 54.9%, call 54.3%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 35.5% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 22.9% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 41.5% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$19.8M net, 14.0% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-22T21:56:03+00:00)

- Call wall: 150.00 -> 150.00 (+0.00)
- Put wall: 145.00 -> 140.00 (-5.00)
- Zero gamma: 156.54 -> 157.41 (+0.87)
- Abs gamma strike: 145.00 -> 150.00 (+5.00)
- Net GEX: -$125.5M -> -$142.8M (-$17.3M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
