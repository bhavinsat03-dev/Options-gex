# QQQ gamma exposure report

As of 2026-10-23T16:30:16+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 706.80 | The underlying price used for every calculation in this run. |
| Net GEX | -$7.13B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 710.00, 708.00, 706.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 700.00, 705.00, 690.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 710.00: 2026-10-23 63%, 2026-10-30 14%, 2026-11-20 6%; 708.00: 2026-10-23 92%, 2026-10-26 2%, 2026-11-06 2%; 706.00: 2026-10-23 94%, 2026-10-26 2%, 2026-12-18 1% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 700.00: 2026-10-30 47%, 2026-12-18 18%, 2026-11-20 17%; 705.00: 2026-10-23 62%, 2026-10-30 15%, 2026-11-20 11%; 690.00: 2026-10-30 44%, 2026-12-18 18%, 2026-11-20 18% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 705.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 724.18 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $116.35B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $1.51B | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$2.26B | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±3.65 (0.5%) -> 703.15 to 710.45, exp 2026-10-23 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 2,928,122 calls / 4,506,795 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 760.00 (143,569); puts 700.00 (278,527) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 710 calls, 44,662 OI: 2026-10-23 28% (12,480), 2026-10-30 22% (9,627), 2026-12-18 18% (8,061); put wall 700 puts, 278,527 OI: 2026-10-30 32% (88,330), 2026-12-18 28% (78,043), 2026-11-20 20% (56,875); max call OI 760 calls, 143,569 OI: 2026-11-20 27% (38,766), 2026-12-18 18% (25,670), 2026-11-06 17% (24,636); max put OI 700 puts, 278,527 OI: 2026-10-30 32% (88,330), 2026-12-18 28% (78,043), 2026-11-20 20% (56,875) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 710.00: 44,662 calls; put wall 700.00: 278,527 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.54 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 5.04 vol pts (put 27.1%, call 22.1%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 20.9% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 0.0% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 30.8% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 48.3% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$867.0M net, 18.9% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-23T16:12:39+00:00)

- Call wall: 710.00 -> 710.00 (+0.00)
- Put wall: 710.00 -> 700.00 (-10.00)
- Zero gamma: 725.43 -> 724.18 (-1.25)
- Abs gamma strike: 710.00 -> 705.00 (-5.00)
- Net GEX: -$8.33B -> -$7.13B (+$1.20B)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
