# TSLA gamma exposure report

As of 2026-10-21T00:49:04+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 373.71 | The underlying price used for every calculation in this run. |
| Net GEX | $201.9M | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | positive gamma | Dealer hedging tends to offset price moves, a condition historically associated with lower realized volatility. |
| Call walls (top 3) | 400.00, 380.00, 385.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 350.00, 360.00, 370.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 400.00: 2026-10-23 35%, 2026-11-20 30%, 2026-10-30 22%; 380.00: 2026-10-23 54%, 2026-11-20 15%, 2026-10-30 14%; 385.00: 2026-10-23 64%, 2026-11-20 13%, 2026-10-30 10% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 350.00: 2026-11-20 41%, 2026-10-23 24%, 2026-10-30 16%; 360.00: 2026-10-23 41%, 2026-10-30 21%, 2026-11-20 21%; 370.00: 2026-10-23 38%, 2026-11-20 29%, 2026-10-30 21% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 400.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 348.12 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $8.30B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $41.5M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$237.6M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±24.23 (6.5%) -> 349.48 to 397.94, exp 2026-10-23 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 599,773 calls / 528,234 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 400.00 (45,627); puts 350.00 (23,041) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 400 calls, 45,627 OI: 2026-11-20 35% (16,103), 2026-10-23 31% (14,018), 2026-10-30 21% (9,468); put wall 350 puts, 23,041 OI: 2026-11-20 47% (10,758), 2026-10-23 20% (4,599), 2026-10-30 15% (3,366); max call OI 400 calls, 45,627 OI: 2026-11-20 35% (16,103), 2026-10-23 31% (14,018), 2026-10-30 21% (9,468); max put OI 350 puts, 23,041 OI: 2026-11-20 47% (10,758), 2026-10-23 20% (4,599), 2026-10-30 15% (3,366) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 400.00: 45,627 calls; put wall 350.00: 23,041 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 0.88 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 0.00 vol pts (put 45.9%, call 45.9%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 42.2% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 21.0% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 36.8% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $3.3M net, 1.4% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-21T00:32:46+00:00)

- Call wall: 400.00 -> 400.00 (+0.00)
- Put wall: 350.00 -> 350.00 (+0.00)
- Zero gamma: 348.09 -> 348.12 (+0.03)
- Abs gamma strike: 400.00 -> 400.00 (+0.00)
- Net GEX: $201.7M -> $201.9M (+$174.7K)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
