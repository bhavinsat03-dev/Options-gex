# QQQ gamma exposure report

As of 2026-10-23T13:51:27+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 704.30 | The underlying price used for every calculation in this run. |
| Net GEX | -$8.45B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 710.00, 705.00, 720.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 700.00, 690.00, 710.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 710.00: 2026-10-23 53%, 2026-10-30 18%, 2026-11-20 8%; 705.00: 2026-10-23 57%, 2026-10-30 16%, 2026-11-06 6%; 720.00: 2026-11-20 44%, 2026-12-18 18%, 2026-10-30 15% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 700.00: 2026-10-23 32%, 2026-10-30 31%, 2026-12-18 13%; 690.00: 2026-10-30 43%, 2026-12-18 18%, 2026-11-20 17%; 710.00: 2026-10-23 45%, 2026-10-30 17%, 2026-11-06 13% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 700.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 724.02 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $122.94B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $1.43B | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$68.4K | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±7.67 (1.1%) -> 696.64 to 711.97, exp 2026-10-23 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 2,928,122 calls / 4,506,795 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 760.00 (143,569); puts 700.00 (278,527) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 710 calls, 44,662 OI: 2026-10-23 28% (12,480), 2026-10-30 22% (9,627), 2026-12-18 18% (8,061); put wall 700 puts, 278,527 OI: 2026-10-30 32% (88,330), 2026-12-18 28% (78,043), 2026-11-20 20% (56,875); max call OI 760 calls, 143,569 OI: 2026-11-20 27% (38,766), 2026-12-18 18% (25,670), 2026-11-06 17% (24,636); max put OI 700 puts, 278,527 OI: 2026-10-30 32% (88,330), 2026-12-18 28% (78,043), 2026-11-20 20% (56,875) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 710.00: 44,662 calls; put wall 700.00: 278,527 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.54 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 7.60 vol pts (put 29.8%, call 22.2%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 25.8% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 0.0% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 28.5% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 45.7% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$786.5M net, 18.3% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-22T23:53:05+00:00)

- Call wall: 720.00 -> 710.00 (-10.00)
- Put wall: 700.00 -> 700.00 (+0.00)
- Zero gamma: 731.89 -> 724.02 (-7.87)
- Abs gamma strike: 700.00 -> 700.00 (+0.00)
- Net GEX: -$9.62B -> -$8.45B (+$1.18B)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
