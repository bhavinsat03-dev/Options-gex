# IWM gamma exposure report

As of 2026-10-21T00:28:46+00:00.

| Metric | Value | What it means |
|---|---|---|
| Spot | 275.78 | The underlying price used for every calculation in this run. |
| Net GEX | -$1.27B | Dollars of stock dealers would trade to re-hedge for a 1% move; positive means they trade against the move, negative means with it. |
| Regime | negative gamma | Dealer hedging tends to reinforce price moves, a condition historically associated with higher realized volatility. |
| Call walls (top 3) | 275.00, 277.00, 280.00 | Strikes holding the most dealer call gamma, where hedging flows have tended to slow rallies. |
| Put walls (top 3) | 270.00, 265.00, 275.00 | Strikes holding the most dealer put gamma, where hedging flows have tended to slow or, if broken, accelerate declines. |
| Call wall expiries | 275.00: 2026-10-21 49%, 2026-10-23 18%, 2026-10-22 9%; 277.00: 2026-10-21 79%, 2026-10-23 10%, 2026-10-22 3%; 280.00: 2026-10-29 31%, 2026-10-23 27%, 2026-11-20 18% | For each call wall, the expirations holding most of its gamma and their share; a wall made of near-dated options disappears when they expire. |
| Put wall expiries | 270.00: 2026-11-20 63%, 2026-10-30 22%, 2026-10-23 6%; 265.00: 2026-11-20 66%, 2026-10-30 22%, 2026-10-23 4%; 275.00: 2026-11-20 46%, 2026-10-23 19%, 2026-10-21 12% | For each put wall, the expirations holding most of its gamma and their share. |
| Absolute gamma strike | 275.00 | The single strike with the most total gamma (calls plus puts), often the strongest price magnet. |
| Zero-gamma flip | 281.99 | The price at which total dealer gamma would change sign; above it hedging tends to dampen moves, below it to amplify them. |
| Net DEX | $17.64B | Dollar delta dealers hold from these options; it is what their stock hedge must offset. |
| Net vanna | $521.9M | How much dealer dollar delta changes if implied volatility rises one point; a falling-vol environment flips the sign of the flow. |
| Net charm | -$451.3M | How much dealer dollar delta changes per day from time decay alone, with price and volatility unchanged. |
| Expected move | ±2.06 (0.7%) -> 273.72 to 277.84, exp 2026-10-21 | The nearest-expiry at-the-money straddle price, i.e. the size of move the options market is pricing by that expiry. |
| Total call / put OI | 990,135 calls / 2,067,734 puts | Open contracts across all fetched expirations and strikes. |
| Strongest OI strikes | calls 290.00 (62,408); puts 270.00 (201,025) | The strikes with the most open call and put contracts; these are often further from price and longer-dated than the gamma walls. |
| Wall OI by expiry | call wall 275 calls, 40,875 OI: 2026-10-21 26% (10,614), 2026-10-23 18% (7,280), 2026-11-06 13% (5,229); put wall 270 puts, 201,025 OI: 2026-11-20 71% (142,217), 2026-10-30 17% (34,707), 2026-10-23 4% (7,540); max call OI 290 calls, 62,408 OI: 2026-11-20 70% (43,985), 2026-10-30 18% (11,541), 2026-10-23 5% (3,083); max put OI 270 puts, 201,025 OI: 2026-11-20 71% (142,217), 2026-10-30 17% (34,707), 2026-10-23 4% (7,540) | Which expirations hold the open contracts at each key strike; positions expiring soon disappear after that date. |
| OI at main walls | call wall 275.00: 40,875 calls; put wall 270.00: 201,025 puts | Open contracts at the strongest call and put wall strikes, summed across expirations. |
| Put/call OI ratio | 2.09 | Put open interest divided by call open interest across the fetched expirations; above 1 means more puts outstanding. |
| 25-delta skew | 1.60 vol pts (put 20.1%, call 18.5%, exp 2026-11-20) | Implied vol of a 25-delta put minus a 25-delta call; higher means downside protection is priced richer than upside. |
| \|GEX\| from 0DTE | 0.0% | Share of total gamma expiring today, which disappears at today's close. |
| \|GEX\| from rest of this week | 26.7% | Share of total gamma expiring later this week. |
| \|GEX\| from rest of this month | 27.6% | Share of total gamma expiring after this week but within this calendar month. |
| \|GEX\| beyond this month | 45.7% | Share of total gamma expiring in later months, the most persistent part of positioning. |
| GEX after monthly expiry (2026-11-20) | $621.2K net, 0.4% of \|GEX\| | The gamma that will still be in place once the next standard monthly options expire. |

## Changes since previous run (2026-10-20T22:42:21+00:00)

- Call wall: 275.00 -> 275.00 (+0.00)
- Put wall: 270.00 -> 270.00 (+0.00)
- Zero gamma: 281.73 -> 281.99 (+0.26)
- Abs gamma strike: 275.00 -> 275.00 (+0.00)
- Net GEX: -$1.20B -> -$1.27B (-$72.2M)

_Positioning estimates assume dealers are long calls and short puts and use Yahoo open interest, which updates once per day. Descriptive only; not trading advice._
