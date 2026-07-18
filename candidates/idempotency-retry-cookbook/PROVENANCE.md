# Provenance

Every factual claim in this cookbook traces to a **public specification or a
named public engineering source**, cited in the Sources footer of the chapter
that uses it. This is a *teaching* product, so its evidence class is
**verified-by-citation** for the prose, plus a **runnable, self-tested** proof for
the recipes: the four `recipes/` files carry a 26-test stdlib `unittest` suite
that runs offline and in CI. No fabricated quotes appear anywhere — sources are
paraphrased and cited by stable identifier so a buyer can audit each one.

Repo state at assembly: `main` HEAD `f28465e`, 2026-07-18 (UTC).

## Specifications cited (stable public identifiers)

| Source | Where used | What it backs |
|--------|-----------|---------------|
| **IETF draft — *The Idempotency-Key HTTP Header Field*** (`draft-ietf-httpapi-idempotency-key-header`, IETF HTTP APIs WG) | ch.1, 2, 8 | the `Idempotency-Key` header name + the at-most-once safe-retry intent; explicitly light on exact status codes |
| **RFC 9110 — *HTTP Semantics*** §9.2.2 | ch.1, 3, 7 | idempotent methods (GET/HEAD/PUT/DELETE/OPTIONS/TRACE), why repeats are safe |
| **RFC 9110** §10.2.3 | ch.6 | `Retry-After` — delay-seconds OR HTTP-date |
| **RFC 9110** §15.5 / §15.6 | ch.1, 3 | 4xx client-error vs 5xx server-error meaning; 409/422 |
| **RFC 6585** §4 | ch.3, 6 | `429 Too Many Requests` and its `Retry-After` |
| **RFC 8470** | ch.3 | `425 Too Early` (HTTP early data) |
| **IETF draft — *RateLimit header fields for HTTP*** (`draft-ietf-httpapi-ratelimit-headers`) | ch.6 | `RateLimit-*` fields — explicitly a DRAFT, not an RFC |
| **AWS Architecture Blog — *Exponential Backoff And Jitter*** (Marc Brooker) | ch.4 | full / equal / decorrelated jitter formulas; the simulation result that decorrelated jitter minimizes total calls |
| **Google — *Site Reliability Engineering*** ("Handling Overload", "Addressing Cascading Failures") — free at sre.google/books | ch.1, 5, 7 | retry amplification across layers; per-client retry budgets (~10%); avoid retrying at multiple layers |
| **gRPC retry design** (`grpc/proposal` A6, "retry throttling") | ch.5 | the request-deposit / retry-withdraw token-bucket budget model |
| **Michael Nygard — *Release It!*** / Martin Fowler — "CircuitBreaker" | ch.5 | the Circuit Breaker pattern + CLOSED/OPEN/HALF-OPEN states |
| **Stripe idempotency documentation** (`https://docs.stripe.com/api/idempotent_requests`) | ch.2, 8 | the reference concrete implementation: fingerprint, 409-in-progress, 24h expiry |

Honest note on the two headers that are **drafts, not RFCs**: the
`Idempotency-Key` header and the `RateLimit-*` fields are both IETF drafts. The
stable, RFC-backed pieces are the *methods'* idempotency (RFC 9110), `429` (RFC
6585), and `Retry-After` (RFC 9110). Where this cookbook asserts a specific status
code for an idempotency edge (409/422 on mismatch, 409 in-flight, 24h expiry) it
follows the widely-deployed **Stripe-style model** and says so — a buyer whose API
documents different codes should adjust.

## Repo material cited (file @ commit, `menno420/venture-lab`)

The two companion kits are cross-referenced (not copied) as the "prove-it"
partners to this "teach-it" guide:

| File | Commit | Used in |
|------|--------|---------|
| `candidates/idempotency-key-test-kit/README.md` | `c1bf40a` | ch.1, 2, 8 — the exactly-once HTTP test kit this cookbook points at |
| `candidates/idempotency-key-test-kit/fixtures/PROVENANCE.md` | `c1bf40a` | ch.2 — the honest Stripe-vs-IETF scope framing this cookbook mirrors |
| `candidates/rate-limit-test-kit/README.md` | `dfec52e` | ch.1, 6 — the 429 + `Retry-After` HTTP test kit this cookbook points at |
| `candidates/rate-limit-test-kit/fixtures/PROVENANCE.md` | `dfec52e` | ch.6 — the RateLimit-draft honesty framing this cookbook mirrors |

## The recipes' evidence (runnable, self-tested)

The four `recipes/` files are not prose — they are code with a test. Verify:

```sh
cd recipes && python3 -m unittest test_recipes -v   # -> Ran 26 tests ... OK
```

The suite is stdlib-only, offline, and deterministic (a seeded RNG, an injected
clock, and a recording fake sleeper — no wall-clock waits). It asserts: backoff
window bounds + herd de-synchronization; all four idempotency-store rules +
fingerprint order-insensitivity + abort; retryable-status classification + the
idempotent-method gate; `Retry-After` parsing (both forms, past-clamped,
garbage→None); budget starvation under sustained failure; and the circuit
breaker's open/half-open/close transitions. The same job runs in this repo's CI
(`.github/workflows/kit-tests.yml`, job `idempotency-retry-cookbook-tests`).

## What is NOT claimed

- **Not a production library / not a distributed store.** `idempotency_store.py`
  is an in-memory single-process sketch (labeled so at the top of the file and in
  ch.2/ch.8); production needs an atomic shared backend.
- **The self-test proves the snippets, not your system.** `Ran 26 tests ... OK`
  is a correctness proof for these functions offline — not for your real
  backoff-under-load, distributed store, or breaker thresholds. Load-test those,
  and verify your endpoint with the companion kits.
- **This does not TEST your endpoint.** It teaches the patterns; the Idempotency
  Key Test Kit and Rate-Limit Test Kit are the HTTP-level checks.
- **Drafts move.** Re-verify the IETF `Idempotency-Key` and `RateLimit-*` drafts
  before betting on exact semantics.

---

**PROVENANCE-FOOTER** — claims trace to public specs + named engineering sources
(IETF `draft-ietf-httpapi-idempotency-key-header` · RFC 9110 §9.2.2/§10.2.3/§15.5
· RFC 6585 §4 · RFC 8470 · IETF `draft-ietf-httpapi-ratelimit-headers` · AWS
*Exponential Backoff And Jitter* (Brooker) · Google *SRE* Overload/Cascading ·
gRPC A6 retry throttling · Nygard *Release It!* Circuit Breaker · Stripe
idempotent-requests docs) and to companion repo material
`candidates/idempotency-key-test-kit/README.md` @ `c1bf40a` ·
`candidates/idempotency-key-test-kit/fixtures/PROVENANCE.md` @ `c1bf40a` ·
`candidates/rate-limit-test-kit/README.md` @ `dfec52e` ·
`candidates/rate-limit-test-kit/fixtures/PROVENANCE.md` @ `dfec52e`; recipes
proven by `recipes/test_recipes.py` (26 tests, CI job
`idempotency-retry-cookbook-tests`); repo `menno420/venture-lab` @ `f28465e`.
