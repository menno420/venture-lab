# Quick start

## 0. Run the self-test (one minute, no network, no dependencies)

The recipes are stdlib-only Python. Prove they behave on your machine:

```sh
cd recipes
python3 -m unittest test_recipes -v
```

Expect `Ran 26 tests ... OK`. That verifies the backoff windows, all four
idempotency-store rules, the `Retry-After` floor, the retry-budget starvation, and
the circuit-breaker transitions — offline, deterministically, in well under a
second.

Want just a smoke check without the test runner? Confirm the three modules import
and expose their API:

```sh
cd recipes
python3 -c "import backoff, idempotency_store, retry; print('ok:', retry.RETRYABLE_STATUS)"
```

## 1. Read the guide in order

The chapters build on each other:

1. `guide/01-why-naive-retries-are-dangerous.md` — the threat model (double
   charges, retry storms, wasted work).
2. `guide/02-idempotency-keys.md` — make the write a no-op on retry (server side).
3. `guide/03-retryable-vs-non-retryable.md` — retry 429/408/425 + 5xx + transport;
   never another 4xx; method matters.
4. `guide/04-backoff-and-jitter.md` — the formulas, and why jitter breaks the herd.
5. `guide/05-retry-budgets-and-circuit-breakers.md` — cap the total blast radius.
6. `guide/06-honoring-retry-after.md` — parse both forms; use it as a floor.
7. `guide/07-at-least-once-vs-exactly-once.md` — dedup at the consumer.
8. `guide/08-recipes.md` — the install guide, the honesty ledger, and further
   reading.

Each chapter ends with a **Sources footer** naming the exact RFC / draft /
engineering source behind its claims. That is the product's honesty mechanic:
every assertion is auditable.

## 2. Lift the recipes into your client

The three modules compose (full example in chapter 8):

- `backoff.py` — pick a jitter variant (`full_jitter` is the safe default) for the
  delay between attempts.
- `retry.py` — `call_with_retry(fn, budget=..., breaker=...)` wraps your call with
  classification + backoff + budget + breaker + `Retry-After` floor. Your `fn`
  raises `RetryableError` (transient) or `FatalError` (don't retry) per chapter 3.
- `idempotency_store.py` — the server-side reserve-and-replay logic that makes a
  retried `POST` safe; also the consumer-side dedup pattern (chapter 7).

All three take injectable `rng` / `sleep` / `clock` so your own tests run without
real waits — copy the pattern from `test_recipes.py`.

## 3. Adapt the honest defaults

- **Status codes:** `retry.RETRYABLE_STATUS` is the Stripe/RFC-aligned default
  (`408, 425, 429, 500, 502, 503, 504`). If your API documents different retryable
  codes, edit the set.
- **Idempotency codes:** the store returns 409/422-style mismatches per the
  Stripe-style model. Match your own API's documented codes where they differ
  (chapter 2 explains why the IETF draft leaves this open).
- **Budget / breaker thresholds:** `token_ratio=0.1` (≤~10% retries) and
  `fail_threshold`/`cooldown` are starting points — tune to your traffic and load
  tests.

## 4. Verify your endpoint with the companion kits

This cookbook teaches the patterns; it does not test *your* endpoint. To prove
your implementation over real HTTP (stdlib-only, no vendor account):

- **Idempotency Key Test Kit** — the exactly-once contract from chapter 2.
- **Rate-Limit Test Kit** — the 429 + `Retry-After` behaviour from chapter 6.

See the "pairs with" note in `README.md`.
