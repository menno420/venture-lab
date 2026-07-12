# Market State Dashboard — intake (owner-directed candidate, spec only)

> A live, **$0-hosted** static website that is a **decision-support screener** for the
> owner's **MANUAL** trading on his existing DEGIRO account. Per watchlist stock it
> surfaces current market **state** (ranging / uptrend / downtrend), an ATR-based
> **expected daily % move**, and — only once earned — whether any lane-vetted strategy
> currently signals. **NOT a bot. NOT automated execution. NOT financial advice.** This
> file is the SPEC only — no site is built in this slice.

## A. What it is (one-liner)

A GitHub-Pages-hosted static screener that reads free/delayed market data on a cron,
computes a small set of **mechanical, descriptive** market-state numbers for a
configurable watchlist of ~20–50 liquid US names, and renders them so the **owner reads
the board and clicks his own trades on DEGIRO**. DEGIRO has no bot API (confirmed —
trading-strategy `docs/research/broker-bot-options-nl-2026-07-12.md`: *"No official API
and no support for automated/bot trading"*), so the only honest model is: **the site
describes state, the human executes**. The site never places an order, never gives
advice, and never claims to predict price.

## B. Phased honesty (CORE DESIGN)

The whole credibility of this tool is that it **never shows a number it cannot defend at
the moment it shows it.** Two hard-separated phases:

### Phase 1 — DESCRIPTIVE screener ONLY (defensible NOW, ships first)

Every Phase-1 field is a **mechanical description of past/observed price**, with **zero
predictive claim**:

- **Regime classification** — ranging vs uptrend vs downtrend, from mechanical inputs
  only: **Bollinger band-width percentile** (band width vs its own trailing history →
  squeeze/expansion) and/or **ADX** (trend strength). No opinion, just the classifier's
  label + the raw inputs behind it.
- **Bollinger band position per timeframe** — where price sits inside its bands on **1h /
  4h / daily** (upper/mid/lower, %B), computed from free data. Purely positional.
- **ATR-based expected daily range, expressed in %** — `ATR(daily) / price` as a
  **typical daily range**, labelled explicitly as *"this is how much it has recently
  moved in a day,"* NOT *"it will move X% today."* It is a volatility descriptor, not a
  forecast.
- **Days-in-current-state** — how many sessions the current regime label has persisted.

All four are backward-looking, reproducible from the raw bars, and survive an honest
"where did this number come from?" audit. **This is the entire product at launch.**

### Phase 2 — SIGNAL overlays (ships EMPTY; each slot must be EARNED)

Phase 2 would overlay *"strategy X currently signals BUY/flat on this ticker."* It is
wired to **exactly one thing**: strategies that have **passed the trading-strategy lane's
pre-registered forward test / one-shot holdout.** No signal is ever shown that isn't
backed by a passed forward test.

**Current status: NONE qualify. Phase 2 ships EMPTY.** As of the 2026-07-12 read of the
trading-strategy lane, the one-shot holdout has been **spent** (its protocol is explicitly
single-use — `docs/p5-holdout-protocol.md`: *"One shot, then final … The holdout is spent
the moment it is read."*) and the result cleared **no strategy for deployment**:

- Of 13 candidates evaluated, the final report records **1 CONFIRMED** (AAPL-donchian),
  **2 HOLDOUT-BEAT** secondaries, and **10 HOLDOUT-MISS** — but the verdict is
  unambiguous: **"No candidate holds a finding label"** (`docs/final-report.md` §Holdout).
  Even the one confirmation is *"a modest, drawdown-shaped, instrument-specific,
  statistically insignificant result"* (t = 0.02, "deep inside noise"). **Zero strategies
  are deployment-ready → zero signal slots exist.**
- **Honest correction to the intake brief:** there is **no landed "Bollinger multi-TF in
  dev" document** in trading-strategy as of this read (the named
  `bollinger-mtf-dev-2026-07-12.md` returns 404 and does not exist in `docs/research/`).
  The only Bollinger evidence on record is negative: the final report states *"The whole
  Bollinger sub-family went 0 for 8"* in the mean-reversion phase. So Phase 2 must **not**
  presuppose a Bollinger multi-TF signal is coming; it ships empty and stays empty until
  some strategy — Bollinger or otherwise — actually clears a fresh, pre-registered forward
  test. If/when a new holdout is opened and a strategy passes, THAT is the trigger to add
  its slot, citing the passing run.

Phase 2 shipping empty is a **feature**: a screener that admits it has no edge yet is more
useful — and far more honest — than one that manufactures signals to fill space.

## C. Architecture ($0 hosting)

```
GitHub Actions cron (hourly, US market hours)
  → fetch delayed/EOD bars for a config watchlist (~20–50 liquid, high-vol US names)
  → compute Phase-1 states (regime, BB positions 1h/4h/daily, ATR% range, days-in-state)
  → emit static JSON + static HTML
  → publish to GitHub Pages
```

- **No server, no database, no runtime backend.** The Action is the only compute; the site
  is static files. Cost = $0 (GitHub Actions + Pages free tiers).
- **No secrets beyond OPTIONAL data-API key NAMES.** The pipeline is designed to run with
  **zero keys** on the primary source. If an optional keyed source is wired, only the env
  var **NAME** is referenced in config/CI (e.g. `FINNHUB_API_KEY`) — **never a value**, and
  the value is an owner-managed GitHub Actions secret, never committed.
- **Watchlist** is a checked-in config file (tickers + timeframe params) the owner edits.

### Data source investigation (honest tradeoffs)

Requirement: cover ~50 tickers **hourly** during US market hours, including enough history
to compute daily Bollinger/ATR/ADX and (ideally) 1h/4h bands.

| Source | Key? | Limits | Covers ~50 tickers hourly? | ToS / notes |
|---|---|---|---|---|
| **yfinance** (Yahoo, unofficial) | No | Unpublished, IP-rate-limited; can throttle/break without notice | **Yes** — one batched call pulls daily + intraday (1h) for the whole list; 4h is resampled from 1h | **Unofficial, ToS grey-area.** Fine-risk for *personal, hourly, non-redistributed* use; do NOT redistribute/sell its data |
| **Stooq** | No | EOD/CSV, generous; intraday coverage thin/unreliable | **Daily: yes.** Intraday 1h/4h: **no** (degrades to daily-only) | Free EOD CSV, no key — rock-solid **daily** fallback |
| **Alpha Vantage** (free) | Yes | **25 requests/day HARD cap** | **No** — 25/day can't cover 50 tickers even once, let alone hourly | Disqualified for this shape |
| **Finnhub** (free) | Yes | 60 req/min; **delayed**; candle/history restricted on free tier | Last-price quotes: yes. Historical candles for BB/ATR: restricted | Optional last-price secondary only (env var NAME `FINNHUB_API_KEY`) |

**RECOMMENDED: PRIMARY = yfinance, FALLBACK = Stooq.**
- **yfinance (primary):** the only free, keyless source that returns **multi-timeframe
  intraday + daily** for all ~50 tickers in a batched pull, which Phase-1's 1h/4h/daily
  Bollinger positions require. Risk owned honestly: unofficial + rate-limited + ToS
  grey-area — acceptable **only** because usage is hourly, personal, and never
  redistributed.
- **Stooq (fallback):** free, keyless, reliable **daily** CSV. If Yahoo throttles/breaks,
  the board **degrades gracefully to daily-only** (regime + daily BB + ATR% + days-in-state
  still compute; the 1h/4h band rows show "intraday unavailable" rather than going stale or
  fabricating). A visibly-degraded board beats a silently-wrong one.
- **Finnhub (optional secondary):** delayed last-price sanity check only, keyed, off by
  default.

**Refresh cadence:** GitHub Actions `cron` **hourly during US market hours**
(~13:30–20:00 UTC ≈ 09:30–16:00 ET) **plus one post-close EOD run** to lock the day's
daily bar. Note GitHub-hosted cron can be delayed several minutes under load — fine for a
decision-support board, and the page must stamp its **last-updated time** so a stale board
is obvious.

**Licensing flag (load-bearing):** 15-min-delayed / EOD data is **fine for personal
decision support** but is **NOT licensed for redistribution or resale.** A **sellable**
version of this dashboard needs a **licensed real-time feed** — a real recurring cost line
(e.g. Polygon or Tiingo paid tiers, roughly tens of USD/month and up). That is an
owner-funded, out-of-scope decision, not a Phase-1 build step.

## D. DEGIRO manual-execution fit (the cost math)

DEGIRO offers no bot API (see §A), so execution is **manual by design** — and at the
owner's account size that is fine, because **costs are not the enemy here:**

- Owner capital: **€5–6K**; typical position **€4–5K**.
- US-stock trade cost: **~€4 total round trip** (per-order fixed fee both ways).
- On a €4–5K position, €4 ≈ **0.08–0.10%** round-trip cost.
- A reliably captured **1–2% move** on €4–5K nets ≈ **€40–100 per trade**, against ~€4 of
  cost — i.e. cost is **~5–10% of a good trade's gross**, not a dealbreaker.
- (Note: DEGIRO's fixed fee makes *small* trades expensive — trading-strategy's broker
  research shows *"single-stock round trips at €100 cost ~4.5% (US)"*. At €4–5K the same
  fixed fee amortizes to ~0.1%. The owner's scale is exactly where the fixed fee stops
  mattering.)

**The edge bar a Phase-2 signal must clear before real use:** a signal is only worth
acting on if its **net expectancy materially exceeds total friction** — round-trip cost
(~0.1%) **+ slippage + a safety margin**. A rule of thumb for this account: a signal must
demonstrate expectancy **well above ~0.1% net per trade** (realistically a multiple of it,
to survive slippage and variance) before it earns a slot on the board. This is exactly why
Phase 2 ships empty: **nothing in the trading-strategy lane has demonstrated even a
statistically significant edge, let alone one that clears costs.**

**Sizing discipline (cited).** Position sizing follows the trading-strategy lane's
allocation discipline, not gut feel. That lane's hybrid allocator
(`docs/hybrid-allocator.md`) fixes a **conservative, non-optimized 70/20/10 split**
(*"B&H core 70% | Rule sleeve 20% | Cash buffer 10%"*, *"chosen conservative, not
optimized"*), and critically **"The sleeve share never grows on paper performance"** — no
adaptive up-sizing off backtest results. The holdout protocol (`docs/p5-holdout-protocol.md`)
further constrains any rule sleeve to **long/flat, no leverage, no shorts**, costed at
**5 bps slippage + 1 bps commission per side.** The dashboard **inherits** this discipline:
any Phase-2 signal maps to the small **rule-sleeve** allocation only, never the core, and
never scales up on a hot streak.

## E. Owner actions + effort

### Owner-action row (six-field grammar) — NOT queued for revenue; one enablement click

> This is the **only** owner action, and it is an **enablement** step (make the future
> site hostable), not a spend or a publish. It is queued only when Phase 1 is actually
> built; at spec stage it is documented, not requested.

#### ⚑ — Enable GitHub Pages for the dashboard (RECOMMENDED host: the trading-strategy repo)

- **WHAT:** Turn on GitHub Pages for the repository that will host the built dashboard.
  **Recommendation: host it on the `menno420/trading-strategy` repo**, not venture-lab.
- **WHERE:** GitHub → the host repo → Settings → Pages → Source = GitHub Actions (or the
  `gh-pages` branch the build Action publishes to).
- **HOW:** One UI toggle: Settings → Pages → set Source; the build Action then publishes the
  static JSON+HTML on each cron run. No custom domain needed (the default
  `menno420.github.io/<repo>` URL is fine).
- **WHY:** GitHub Pages is **per-repository** (each repo can have its own project site), so
  this is **not** about a scarce shared "allotment" — the honest reasons to put it on
  trading-strategy are **cohesion and ownership**: the market data pipeline, the strategy
  definitions, and the forward-test / holdout gating that Phase 2 depends on **all live in
  trading-strategy**, so the dashboard is that repo's natural public face. Keeping
  venture-lab as the **intake/eval lane** (not a hosting surface for a live trading tool)
  keeps its Pages site free for a customer-facing product like **Bababoefoe**, and avoids
  cross-repo data plumbing. (Both repos *could* technically host independently — this is a
  clean-separation recommendation, not a technical constraint.)
- **UNBLOCKS:** A live, auto-refreshing public URL for the Phase-1 board — the entire point
  of "$0-hosted live website."
- **VERIFIED-WHEN:** The Pages URL resolves, shows the watchlist board, and updates after a
  scheduled Action run (last-updated stamp advances).

### Phase 1 build effort / token cap (intake cap — ONE honest number)

**≈ 120k tokens to Phase 1 v0.1, including CI wiring.** Scope inside the cap: the
multi-source fetch module (yfinance primary + Stooq fallback + graceful degrade), the four
descriptive computations (BB-width-percentile/ADX regime, multi-TF %B, ATR% range,
days-in-state), the static JSON+HTML emitter, the GitHub Actions cron workflow, the
watchlist config, a small deterministic test suite over the math, and the CI wiring to keep
it green. Expressed as **complexity/token budget, not wall-clock time.** Over the cap
without a working descriptive board = ledgered negative and re-scoped. (Reference points in
this lane: cc-cost-lens 70k single-file; bababoefoe 150k multi-artifact — this sits between
them.)

### Kill criteria (binding)

- **Owner disuse:** owner stops opening the board for **2 weeks** → **park** it (stop the
  cron, keep the code). A screener nobody reads is pure cost.
- **Data ToS break:** the primary source (yfinance) starts blocking, or its use crosses a
  clear ToS line → **pull** the offending source, fall back to Stooq (daily-only), and if
  no keyless source remains, **park** rather than pay for a feed on spec.
- **No edge ever clears the bar:** if **no** strategy ever passes a fresh forward test at an
  expectancy that clears costs (§D), then **Phase 2 never opens** and the tool stays
  **descriptive-only forever — and that is a fine, honest end state.** A permanently
  Phase-1 screener that correctly describes market state is a legitimate terminal product,
  not a failure.

## F. Ranking / ledger note

**No ranking or ledger update in this slice — by convention.** `docs/research/venture-ledger.md`
tracks **built** candidates (currently only #1 membership-kit and #2 template-packs); other
spec-stage candidates with an INTAKE (cc-cost-lens, bababoefoe) are **not** ledger entries.
This candidate is **spec-only** (nothing built), so it is INTAKE-standalone like them. It
earns a ledger entry (and a six-field ⚑ owner action promoted to `venture-ledger.md`) only
if/when Phase 1 is actually built and the Pages enablement becomes a live ask.

## Why this might fail

The honest downside: the owner may not sustain the manual-read-and-click habit (kill
criterion #1); the free data sources are unofficial/fragile and could force a park (kill
criterion #2); and — most importantly — **the value ceiling of Phase 1 is "a tidy
description of market state," which does not by itself make money.** The money would come
from Phase 2 signals, and **no strategy in the connected lane has earned one** — the
one-shot holdout cleared nothing deployment-ready (§B). So a realistic read is: this ships
as an honest, defensible **descriptive utility** for the owner's own decisions, with real
revenue **gated behind a forward-test win that has not happened yet and may never.** Scored
that way on purpose — no overstatement.
