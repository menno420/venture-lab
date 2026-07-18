# The Idempotency & Retry Cookbook

Retry API calls **without** double-charging a customer, duplicating a side
effect, or turning a brief blip into a self-inflicted outage. Eight compact
chapters plus four small, correct, **self-tested** stdlib recipes that teach the
safe-retry patterns end to end: idempotency keys, retryable-error
classification, exponential backoff + jitter (with the math), retry budgets,
circuit breakers, honoring `Retry-After`, and consumer-side dedup for
at-least-once delivery.

## What you get

- **`guide/`** — 8 chapters (~5,000 words): why naive retries are dangerous (the
  double charge, the retry storm); idempotency keys done right (fingerprint +
  stored response, the four rules, 409/422-on-mismatch, expiry); which errors are
  retryable (never a 4xx except 408/425/429); backoff & jitter with the
  full/equal/decorrelated formulas and *why* jitter breaks the thundering herd;
  retry budgets & circuit breakers to cap the blast radius; honoring
  `Retry-After` (both RFC forms) and the rate-limit headers; and at-least-once vs
  exactly-once with consumer dedup. Every chapter ends with a **Sources footer**
  citing the exact spec / engineering source — audit each claim yourself.
- **`recipes/`** — 4 files, stdlib-only, no dependencies:
  1. `backoff.py` — exponential backoff + full/equal/decorrelated jitter (pure
     functions, injectable RNG).
  2. `idempotency_store.py` — a server-side idempotency-key store sketch
     enforcing replay / mismatch / in-flight-lock / expiry.
  3. `retry.py` — the client executor: retryable classification, `Retry-After`
     parsing (delay-seconds *and* HTTP-date), a gRPC-style retry budget, a
     three-state circuit breaker, and `call_with_retry` tying them together.
  4. `test_recipes.py` — a **26-test** stdlib `unittest` self-test that proves the
     snippets are correct, not just parseable. Runs offline in <10ms; also runs
     in this repo's CI.

## The one idea

**A failed *response* is not a failed *operation*.** After an ambiguous failure
you cannot tell whether the side effect ran, so retrying safely means (1) making
the write idempotent so a retry can't double-execute, and (2) retrying only what's
retryable, spaced with jitter, capped by a budget and a breaker, honoring the
server's `Retry-After`. This cookbook is one chapter per layer, each with a
runnable, tested recipe.

## Honesty box (read first)

- **This TEACHES the patterns; it is not a library and not a test kit.** The
  recipes are deliberately small reference snippets meant to be lifted and
  adapted. `idempotency_store.py` is an in-memory single-process **sketch** — the
  four rules are correct, but production needs an atomic shared backend (Redis
  `SET NX` / a DB unique constraint); the file says so.
- **Behaviour is cited, not invented.** The idempotency status codes follow the
  widely-deployed Stripe-style model (which the IETF `Idempotency-Key` draft
  standardizes at the header/intent level, not every status code); the jitter
  formulas are the AWS blog's; the budget is the gRPC token-bucket; the breaker is
  the Nygard pattern. Each chapter's Sources footer names the reference.
- **The self-test proves the snippets, not your system.** `Ran 26 tests ... OK`
  means these functions behave as documented offline. Your real distributed store,
  your real backoff-under-load, and your real breaker thresholds still need load
  testing and the companion kits' HTTP checks against your own endpoint.
- **Standards move; drafts move faster.** `429`/`Retry-After` are stable RFCs; the
  `RateLimit-*` and `Idempotency-Key` headers are IETF drafts. Re-verify current
  drafts before betting on exact semantics.

## What this does NOT do

- It does **not** ship a production-grade retry library or a distributed
  idempotency store — the recipes are reference patterns, tested but minimal.
- It does **not** TEST your endpoint. That's the companion kits' job (below); this
  book teaches the patterns those kits verify.
- It is **not** the Idempotency Key Test Kit or the Rate-Limit Test Kit. Those
  fire real HTTP at an endpoint you own and report PASS/FAIL. This teaches the
  *why* and the *how*; they prove your implementation.

## Pairs with (cross-sell)

- **Idempotency Key Test Kit ($29)** — proves your endpoint's exactly-once
  contract (chapter 2's subject) over real HTTP, stdlib-only, no account.
- **Rate-Limit Test Kit ($29)** — proves your endpoint's 429 + `Retry-After`
  behaviour (chapter 6's subject) over real HTTP.

Read here, verify there. Same audience, non-overlapping scope — the cookbook is
the doctrine, the kits are the receipts.

## Quick start

See `QUICKSTART.md` — run the self-test, then read the guide install order.

## Who this is for

You call APIs that can charge money, create orders, send messages, or mutate
state, and you retry on failure. If you've ever worried a timeout double-charged
someone, or watched retries make an outage worse, this is the pattern set that
stops both.

## License

Single-user license; use the recipes in as many of your own projects as you like.
v0.1 — free updates to the v0.x line.
