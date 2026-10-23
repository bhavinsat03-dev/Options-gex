# QQQ gamma exposure report

As of 2026-10-23T16:12:39+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 708.25 | The underlying price used for every calculation in this run. |
| Net GEX | -$8.33B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 710.00, 708.00, 709.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 710.00, 711.00, 700.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 710.00: 2026-10-23 82%, 2026-10-30 7%, 2026-11-20 3%; 708.00: 2026-10-23 94%, 2026-10-26 2%, 2026-11-06 2%; 709.00: 2026-10-23 91%, 2026-10-30 3%, 2026-10-26 2% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 710.00: 2026-10-23 69%, 2026-10-30 10%, 2026-11-06 7%; 711.00: 2026-10-23 97%, 2026-10-30 1%, 2026-11-20 1%; 700.00: 2026-10-30 47%, 2026-12-18 18%, 2026-11-20 18% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 710.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 725.43 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $119.13B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $1.51B | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | $164.6M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±3.75 (0.5%) -> 704.50 to 712.00, exp 2026-10-23 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 2,928,122 calls / 4,506,795 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 760.00 (143,569); puts 700.00 (278,527) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 710 calls, 44,662 OI: 2026-10-23 28% (12,480), 2026-10-30 22% (9,627), 2026-12-18 18% (8,061); put wall 710 puts, 125,513 OI: 2026-12-18 24% (30,407), 2026-10-30 20% (25,615), 2026-11-06 19% (23,244); max call OI 760 calls, 143,569 OI: 2026-11-20 27% (38,766), 2026-12-18 18% (25,670), 2026-11-06 17% (24,636); max put OI 700 puts, 278,527 OI: 2026-10-30 32% (88,330), 2026-12-18 28% (78,043), 2026-11-20 20% (56,875) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 710.00: 44,662 calls; put wall 710.00: 125,513 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 1.54 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 5.32 vol pts (put 26.9%, call 21.6%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 29.7% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 0.0% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 27.7% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 42.6% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | -$815.6M net, 16.6% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-23T13:51:27+00:00)

- Call wall: 710.00 -> 710.00 (+0.00)
- Put wall: 700.00 -> 710.00 (+10.00)
- Zero gamma: 724.02 -> 725.43 (+1.41)
- Abs gamma strike: 700.00 -> 710.00 (+10.00)
- Net GEX: -$8.45B -> -$8.33B (+$114.2M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
