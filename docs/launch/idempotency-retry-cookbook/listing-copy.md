# The Idempotency & Retry Cookbook — listing copy

> **Status:** `reference`

Ready-to-paste copy for a Gumroad / Lemon Squeezy digital-product page.

## Title
```
The Idempotency & Retry Cookbook — retry API calls without double-charging anyone
```

## Short description (≤ 200 chars)
```
Eight chapters + four self-tested stdlib recipes for safe API retries: idempotency keys, backoff+jitter, retry budgets, circuit breakers, Retry-After, consumer dedup. Every claim cited to an RFC or the source.
```

## Long description
```
A network call failed, so you retry it. That single instinct — applied without guard rails — is how a payment gets charged twice, how a queue silently duplicates every message under load, and how a brief blip on one dependency becomes a self-inflicted outage that the retries themselves keep alive. The root cause is one fact most retry code ignores: a failed RESPONSE is not a failed OPERATION. When a POST times out you cannot tell whether the side effect ran, so retrying safely is a small stack of cooperating decisions — not a loop on error.

This cookbook teaches that stack, one chapter per layer, with a runnable recipe for each. Eight compact chapters (~12 pages): why naive retries are dangerous (the double charge, the thundering-herd retry storm, wasted work on 4xx); idempotency keys done right (fingerprint the request + store the response, the four rules, 409/422-on-mismatch, the in-flight lock, TTL expiry); which errors are actually retryable (429/408/425 + 5xx + transport failures — never any other 4xx — and why the request METHOD decides whether a POST is safe to retry at all); exponential backoff and jitter with the full/equal/decorrelated formulas AND the math for why jitter breaks the herd; retry budgets and circuit breakers to cap the blast radius so an outage can't turn your fleet into the load that sustains it; honoring Retry-After in both its RFC forms (delay-seconds and HTTP-date) as a floor over your backoff; and at-least-once vs exactly-once delivery with consumer-side dedup (because exactly-once DELIVERY is a fiction, but effectively-once PROCESSING is achievable).

Four stdlib-only recipes ship in recipes/, small enough to read and lift: backoff.py (exponential + full/equal/decorrelated jitter, pure functions), idempotency_store.py (a server-side idempotency-key store sketch enforcing all four rules), and retry.py (retryable classification, a Retry-After parser for both forms, a gRPC-style retry-budget token bucket, a three-state circuit breaker, and a call_with_retry that ties them together). They are not just parseable — they ship a 26-test unittest self-test that runs offline in milliseconds and in the publisher's CI, so you can PROVE the snippets behave before you trust them.

Provenance is the product. Every chapter ends with a Sources footer citing the exact reference — RFC 9110 (idempotent methods, Retry-After), RFC 6585 (429), the IETF Idempotency-Key and RateLimit drafts, the AWS "Exponential Backoff And Jitter" blog, Google's SRE book (retry budgets, cascading failures), the gRPC retry design, Nygard's Circuit Breaker, and Stripe's idempotency docs as the reference implementation. No fabricated quotes; audit every claim yourself. And the honesty ledger is explicit about the limits: the recipes are reference patterns (the idempotency store is a labeled in-memory sketch, not a distributed store), the self-test proves the snippets and not your production system, and the two header specs are still IETF drafts.
```

## Bullets
```
- The one idea most retry code misses: a failed RESPONSE is not a failed OPERATION — so retrying a write safely means making it idempotent first, then retrying only what's retryable
- Idempotency keys done right: fingerprint the request + store the response, replay on match, 409/422 on mismatch, an in-flight lock for concurrent retries, and a documented TTL — the four rules, with a runnable server-side sketch
- Which errors to retry, settled: 429/408/425 + 5xx + transport failures, NEVER any other 4xx — plus why a bare POST isn't retry-safe but a POST with an idempotency key is
- Backoff + jitter with the actual formulas (full / equal / decorrelated) AND the math for why jitter breaks the thundering herd — proven in the shipped test by two clients that collide zero times in a thousand draws
- Retry budgets + circuit breakers: a gRPC-style token bucket that caps retries to ~10% of traffic, and a CLOSED/OPEN/HALF-OPEN breaker that fails fast on a dead dependency and probes once on recovery
- Honor Retry-After in BOTH RFC forms (delay-seconds and HTTP-date) as a floor over your backoff — never retry sooner than the server told you, never strip the jitter that de-synchronizes the herd
- Four stdlib recipes with a 26-test self-test (offline, deterministic, also run in CI) — every chapter cites an RFC / draft / named engineering source you can audit
```

## FAQ
```
Q: Is this a library I install, or a book I read?
A: A book with runnable, tested reference recipes — not a packaged library. The four recipes/ files are stdlib-only Python you read, understand, and lift into your own client/server, adapting the defaults to your stack. They ship a 26-test self-test so you can prove they behave (python3 -m unittest test_recipes), but they're deliberately small and readable — the patterns, correct and cited, not a framework.

Q: How is this different from the Idempotency Key Test Kit and the Rate-Limit Test Kit?
A: Teach vs test. Those two kits TEST an endpoint you own over real HTTP and report PASS/FAIL on the exactly-once and 429/Retry-After contracts. THIS cookbook TEACHES the patterns behind those contracts — idempotency keys, backoff+jitter, retry budgets, circuit breakers, Retry-After, consumer dedup — and ships reference recipes. They pair naturally: read here, verify your implementation there. A client that retries on 429 is exactly the client that needs idempotent writes.

Q: Are the claims real, or hand-waved?
A: Cited, per chapter. Every chapter ends with a Sources footer naming the exact reference: RFC 9110, RFC 6585, the IETF Idempotency-Key and RateLimit drafts, the AWS backoff-and-jitter blog, Google's SRE book, the gRPC retry design, Nygard's Circuit Breaker, and Stripe's idempotency docs. Nothing is quoted falsely — sources are paraphrased and cited by stable identifier so you can audit each one. The recipes are proven by the shipped 26-test suite.

Q: Will the recipes work in production as-is?
A: The patterns are correct and tested; the code is a reference, not a hardened library. In particular idempotency_store.py is a labeled in-memory, single-process SKETCH — the four rules are right, but a real distributed store needs an atomic shared backend (Redis SET NX / a DB unique constraint) for the reserve step to be a true lock. The file and the guide say so. Treat the recipes as correct starting points to adapt and load-test, not drop-in infrastructure.

Q: Is this tied to one language or vendor?
A: The recipes are Python stdlib for readability, but the patterns are language-agnostic — the formulas, the state machines, and the rules port directly. The behaviours follow widely-deployed models (the Stripe-style idempotency contract, the AWS jitter formulas, the gRPC budget) and stable HTTP standards (429, Retry-After), all cited so you can match your own platform's documented codes.

Q: What was NOT machine-verified?
A: The prose chapters are verified by citation to public specs and engineering sources, not by a runtime test (they're explanatory). The recipes ARE machine-verified: the 26-test suite runs offline and in CI. But that suite proves the SNIPPETS behave as documented — not that your real distributed store, your real backoff-under-load, or your real breaker thresholds are correct. Load-test those, and test your endpoint with the companion kits. Both header specs (Idempotency-Key, RateLimit-*) are IETF drafts and can move.

Q: Who should NOT buy this?
A: If you already run idempotent writes with keys, classify retryable errors correctly, back off with jitter under a retry budget and a circuit breaker, and honor Retry-After — you own this discipline; buy nothing. If you're happy reading the AWS blog, the SRE book, and the RFCs yourself and assembling the stack, this cookbook's value is the curation, the tested recipes, and the auditable citations — decide if that's worth $19 to you.

Q: License?
A: Single-user license; use the recipes in as many of your own projects as you like. v0.1 — free updates to the v0.x line.

Q: Support?
A: Best-effort, community-level. It's a cookbook, not a managed service.
```

## What this does NOT do (honesty section — keep in the listing)

- It does **not** ship a production-grade retry library or a distributed
  idempotency store. The recipes are reference patterns — tested, correct, and
  minimal; `idempotency_store.py` is an explicitly in-memory sketch.
- It does **not** TEST your endpoint. That's the companion Idempotency Key Test
  Kit and Rate-Limit Test Kit; this book teaches the patterns those kits verify.
- The self-test proves the **snippets**, not your production system — your real
  distributed store, backoff-under-load, and breaker thresholds still need load
  testing.
- The `Idempotency-Key` and `RateLimit-*` headers are IETF **drafts**; the stable
  RFC-backed pieces are method idempotency (RFC 9110), `429` (RFC 6585), and
  `Retry-After` (RFC 9110). Re-verify current drafts before betting on exact
  semantics.

---

**PROVENANCE-FOOTER** — every claim above traces to the buyer bundle + cited
public sources: IETF `draft-ietf-httpapi-idempotency-key-header` · RFC 9110
§9.2.2/§10.2.3/§15.5 · RFC 6585 §4 · RFC 8470 · IETF
`draft-ietf-httpapi-ratelimit-headers` · AWS *Exponential Backoff And Jitter*
(Brooker) · Google *SRE* (Handling Overload / Addressing Cascading Failures) ·
gRPC A6 retry throttling · Nygard *Release It!* Circuit Breaker · Stripe
idempotent-requests docs · companion kits
`candidates/idempotency-key-test-kit/README.md` @ `c1bf40a` and
`candidates/rate-limit-test-kit/README.md` @ `dfec52e` · recipes proven by
`recipes/test_recipes.py` (26 tests, CI job `idempotency-retry-cookbook-tests`) ·
buyer bundle
`candidates/idempotency-retry-cookbook/dist/idempotency-retry-cookbook-v0.1.zip`
@ sha256 `9579f98ae0ffbb5e670e03aa48673ad45d070632ac657aef98dde4bbfc8a8981`
(43,177 bytes, 16 content files) · repo `menno420/venture-lab` @ `f28465e`.
