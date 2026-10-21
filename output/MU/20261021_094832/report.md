# MU gamma exposure report

As of 2026-10-21T13:48:32+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 904.28 | The underlying price used for every calculation in this run. |
| Net GEX | -$101.6M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 900.00, 910.00, 950.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 900.00, 905.00, 895.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 900.00: 2026-10-21 49%, 2026-10-23 18%, 2026-11-20 15%; 910.00: 2026-10-21 46%, 2026-11-20 31%, 2026-10-23 14%; 950.00: 2026-10-23 51%, 2026-10-30 19%, 2026-11-20 13% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 900.00: 2026-10-23 39%, 2026-10-21 30%, 2026-11-20 12%; 905.00: 2026-10-21 77%, 2026-10-23 10%, 2026-10-30 7%; 895.00: 2026-10-21 47%, 2026-10-23 35%, 2026-10-30 12% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 900.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 907.93 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $11.88B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $70.5M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$699.0M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±22.10 (2.4%) -> 882.18 to 926.38, exp 2026-10-21 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 493,042 calls / 523,017 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 1,000.00 (23,637); puts 850.00 (20,962) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 900 calls, 11,912 OI: 2026-11-20 38% (4,508), 2026-10-21 20% (2,334), 2026-10-23 17% (1,999); put wall 900 puts, 18,074 OI: 2026-11-20 34% (6,117), 2026-10-23 26% (4,777), 2026-11-27 12% (2,108); max call OI 1000 calls, 23,637 OI: 2026-10-23 29% (6,972), 2026-11-20 25% (5,967), 2026-10-30 20% (4,758); max put OI 850 puts, 20,962 OI: 2026-11-20 33% (6,994), 2026-10-23 25% (5,180), 2026-10-21 14% (2,842) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 900.00: 11,912 calls; put wall 900.00: 18,074 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.06 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | -9.72 vol pts (put 46.1%, call 55.9%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 22.4% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 26.8% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 20.8% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 30.0% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$19.4M net, 2.8% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-21T01:10:11+00:00)

- Call wall: 900.00 -> 900.00 (+0.00)
- Put wall: 900.00 -> 900.00 (+0.00)
- Zero gamma: 915.22 -> 907.93 (-7.29)
- Abs gamma strike: 900.00 -> 900.00 (+0.00)
- Net GEX: -$167.1M -> -$101.6M (+$65.5M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
