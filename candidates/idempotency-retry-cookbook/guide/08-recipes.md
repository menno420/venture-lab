# 8 · The recipes, the honesty ledger, and further reading

Four files ship in `recipes/`: three small, correct, stdlib-only reference
snippets and one self-test that proves they behave. This chapter is the install
guide, the per-file honesty statement, and where to read next. Nothing here needs
a network, an account, or a dependency.

## What's in `recipes/`

| File | What it is | How to trust it |
|------|-----------|-----------------|
| `backoff.py` | Exponential backoff + full / equal / decorrelated jitter (ch.4). Pure functions returning a delay in seconds; injectable RNG; they don't sleep. | Unit-tested for window bounds + herd de-synchronization. |
| `idempotency_store.py` | Server-side idempotency-key store sketch (ch.2): `fingerprint` + the four rules (replay / mismatch / in-flight / expiry). In-memory reference; a real backend swaps in an atomic store. | Unit-tested for all four rules + fingerprint order-insensitivity + abort. |
| `retry.py` | The client-side executor (ch.3, 5, 6): retryable classification, `parse_retry_after` (both RFC forms), `RetryBudget`, `CircuitBreaker`, and `call_with_retry` tying them together. Injectable rng/sleep/clock. | Unit-tested for classification, the `Retry-After` floor, budget starvation, breaker transitions, and the retry loop. |
| `test_recipes.py` | The self-test. Stdlib `unittest`, offline, deterministic (seeded RNG, injected clock, recording fake sleeper — no wall-clock waits). | It *is* the proof; run it (below). |

## Run the self-test (one command, no network)

From the `recipes/` directory:

```sh
python3 -m unittest test_recipes -v
```

You should see `Ran 26 tests ... OK`. That is the evidence the snippets are
correct, not merely parseable — the backoff windows hold, the idempotency store
enforces all four rules, `Retry-After` floors the delay, the budget starves under
sustained failure, and the breaker opens/probes/recovers. The same suite runs in
this repo's CI (the `idempotency-retry-cookbook-tests` job), so a regression reds
the check.

## Using them together

The three recipes compose into one safe call:

```python
from retry import call_with_retry, RetryBudget, CircuitBreaker, RetryableError, FatalError

budget  = RetryBudget(max_tokens=100, token_ratio=0.1)   # <= ~10% of reqs retried
breaker = CircuitBreaker(fail_threshold=5, cooldown=30)  # stop hammering a dead dep

def do_charge(attempt):
    status, headers, body = http_post("/charges", idempotency_key=key, json=payload)
    if status in (200, 201):
        return body
    if status in (408, 425, 429, 500, 502, 503, 504):
        raise RetryableError(f"HTTP {status}", retry_after=parse_retry_after(headers.get("Retry-After")))
    raise FatalError(f"HTTP {status}")   # any other 4xx: do not retry

result = call_with_retry(do_charge, max_attempts=4, base=0.1, cap=20.0,
                         budget=budget, breaker=breaker)
```

The `idempotency_key` is what makes retrying a `POST` safe (ch.2); the
classification decides what's retryable (ch.3); the executor applies backoff +
jitter (ch.4), the budget + breaker (ch.5), and the `Retry-After` floor (ch.6).
Server-side, `idempotency_store.py` is what makes that key mean "at most once".

## The honesty ledger (read before shipping any of this)

- **These are reference recipes, not a library.** They are deliberately small and
  readable — the *patterns*, correct and tested, meant to be lifted and adapted.
  `idempotency_store.py` is explicitly an in-memory, single-process **sketch**:
  it models the four rules, but production needs an atomic shared backend (Redis
  `SET NX` / a DB unique constraint) for the reserve step to be a real
  distributed lock. The file says so at the top; don't ship the in-memory version
  as a multi-node store.
- **Behaviour follows a documented model, cited — not invented.** The idempotency
  status codes (409/422 on mismatch, 409 in-flight, 24h expiry) follow the
  widely-deployed Stripe-style model, which the IETF `Idempotency-Key` draft
  standardizes at the header/intent level but not down to every status code. Where
  your API documents different codes, adjust. The jitter formulas are the AWS
  blog's; the budget is the gRPC token-bucket; the breaker is the Nygard pattern.
  Every chapter carries a Sources footer so you can audit each claim.
- **The tests prove the *snippets*, not your production system.** `Ran 26 tests
  ... OK` means these functions behave as documented under a seeded, offline
  harness. It does **not** mean your real backoff-under-load, your real
  distributed idempotency store, or your real breaker thresholds are right — those
  need load testing and the companion kits' HTTP-level checks against your own
  endpoint.
- **Standards move; drafts move faster.** `429`/`Retry-After` are stable RFCs;
  the `RateLimit-*` header fields and the `Idempotency-Key` header are IETF
  drafts. Re-check the current draft before betting on exact semantics.

## Pairs with (cross-sell) + further reading

This cookbook TEACHES the patterns. To *verify your implementation*, pair it with
the two companion products in this catalog — they TEST an endpoint you own over
real HTTP, stdlib-only, no vendor account:

- **Idempotency Key Test Kit ($29)** — fires real-shape requests at your endpoint
  and reports PASS/FAIL on the exactly-once contract from chapter 2 (replay,
  mismatch, distinct-keys, concurrent, missing-key).
- **Rate-Limit Test Kit ($29)** — fires a burst and checks the 429 + `Retry-After`
  + `RateLimit-*` behaviour from chapter 6 (the client side of which this book
  covers).

Chapter 6 is the client that consumes what the Rate-Limit kit proves; chapter 2
is the client of what the Idempotency kit proves. Read here, prove it there.

**Further reading (all public):** the IETF draft *The Idempotency-Key HTTP Header
Field*; RFC 9110 §9.2.2 (idempotent methods) and §10.2.3 (`Retry-After`); RFC
6585 §4 (`429`); the AWS Architecture Blog *Exponential Backoff And Jitter* (Marc
Brooker); Google's *Site Reliability Engineering* chapters "Handling Overload" and
"Addressing Cascading Failures" (free at sre.google/books); the gRPC retry design
(A6, retry throttling); Michael Nygard's *Release It!* (Circuit Breaker); Stripe's
idempotent-requests documentation as the reference concrete implementation.

**Sources.** Shipped recipes `recipes/backoff.py`, `recipes/idempotency_store.py`,
`recipes/retry.py`, and the self-test `recipes/test_recipes.py` (26 tests, run in
CI as `idempotency-retry-cookbook-tests`); the spec + engineering sources named
per chapter above; companion products
`candidates/idempotency-key-test-kit/README.md` @ `c1bf40a` and
`candidates/rate-limit-test-kit/README.md` @ `dfec52e` in `menno420/venture-lab`.
