# What's in this bundle (v0.1)

16 files:

```
idempotency-retry-cookbook-v0.1/
├── README.md                                 — what this is + honesty box + "pairs with" + "what it does NOT do"
├── QUICKSTART.md                             — run the self-test, read order, adapt defaults
├── INCLUDED.md                               — this manifest
├── PROVENANCE.md                             — spec/engineering citations + the honesty ledger
├── guide/
│   ├── 01-why-naive-retries-are-dangerous.md — the threat model: double charges, retry storms
│   ├── 02-idempotency-keys.md                — make the write a no-op on retry (server side)
│   ├── 03-retryable-vs-non-retryable.md      — which errors to retry; method matters
│   ├── 04-backoff-and-jitter.md              — the formulas + why jitter breaks the herd
│   ├── 05-retry-budgets-and-circuit-breakers.md — cap the blast radius
│   ├── 06-honoring-retry-after.md            — parse both RFC forms; use it as a floor
│   ├── 07-at-least-once-vs-exactly-once.md   — dedup at the consumer
│   └── 08-recipes.md                         — install guide + honesty ledger + further reading
└── recipes/
    ├── backoff.py                            — exponential backoff + full/equal/decorrelated jitter
    ├── idempotency_store.py                  — server-side idempotency-key store sketch (four rules)
    ├── retry.py                              — classification + Retry-After + budget + breaker + call_with_retry
    └── test_recipes.py                       — 26-test stdlib unittest self-test (offline, deterministic)
```

Guide length: ~5,000 words (~12 pages) across 8 chapters, each with a Sources
footer citing the exact RFC / IETF draft / engineering source (RFC 9110, RFC
6585, the IETF Idempotency-Key + RateLimit drafts, the AWS backoff-and-jitter
blog, Google SRE, the gRPC retry design, Nygard's Circuit Breaker). Plus ~1,500
words of README/QUICKSTART/PROVENANCE and 4 stdlib Python files (~700 lines,
including the 26-test self-test).

Evidence class: **hybrid — runnable-and-self-tested recipes + verified-by-citation
prose.** The four `recipes/` files carry a real `unittest` suite (26 tests) that
runs offline from source, from the extracted bundle, and in CI
(`idempotency-retry-cookbook-tests`); the prose chapters are verified by citation
to public specs and engineering sources (the honest-null substitute for the
zero-runtime chapters — see PROVENANCE.md). Nothing is asserted as
production-hardened that isn't: `idempotency_store.py` is a labeled in-memory
sketch, and every borrowed model is cited to its source.
