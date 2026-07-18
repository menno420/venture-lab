# Session — Rate-Limit Test Kit $29 (new sellable → owner-click-ready)

> **Status:** `in-progress`

- **📊 Model:** [[fill:model]]
- **started (date -u):** Sat Jul 18 17:48 UTC 2026
- **branch:** `claude/rate-limit-test-kit-2026-07-18`
- **base:** `main@c728933`
- **purpose:** build the **Rate-Limit Test Kit ($29)** to owner-click-ready and
  land it as ONE PR — a NEW sellable in the API-robustness kit family, a
  DIFFERENT problem class from the webhook signature kits and the idempotency
  kit. Where the webhook kits verify an inbound provider *signature* and the
  idempotency kit verifies a *safe-retry / exactly-once* dedup contract, this
  kit verifies a buyer's OWN endpoint's **throttling correctness**: that
  requests under the limit return 2xx; that at/over the limit within the window
  the endpoint returns **429 Too Many Requests** with a valid, positive,
  sane `Retry-After` (delay-seconds or HTTP-date); that the optional standard
  `RateLimit-Limit`/`RateLimit-Remaining`/`RateLimit-Reset` (or legacy
  `X-RateLimit-*`) headers, when present, are consistent (Remaining decrements,
  hits 0 exactly at the 429 boundary, Reset is in the future); that after the
  advertised `Retry-After`/reset window elapses, requests succeed again; and
  that the advertised delay matches when the service actually resumes. Stdlib-
  only, account-free, runs with a loud DEMO banner against bundled reference
  stubs. Ships: a CORRECT reference stub (a real fixed-window limiter with a
  short configurable window), a deliberately NAIVE/broken stub (off-by-one +
  missing/invalid Retry-After) so the suite can PROVE it catches the bug, an
  `rltk.py` harness (+ `rltk.js` Node parity) a buyer points at their own
  endpoint, an HTTP-layer real-path test suite with a request-counter and a
  short window, real docs-derived fixtures + PROVENANCE (cited to the IETF draft
  "RateLimit header fields for HTTP", RFC 6585 §4, RFC 9110), a byte-reproducible
  buyer bundle, and a §7 owner-gate publish packet. The build ENDS at a queued
  owner ⚑ publish click (rail 13 / CONSTITUTION §13) — no publish, no spend, no
  accounts by the seat.
- **session:** Mirrors the proven idempotency-key-test-kit scaffold (the closest
  template — same correct-stub + naive-stub evidence pattern) but is a genuinely
  DIFFERENT product: rate-limiting / throttling correctness, not dedup or
  signature verification. The value proof is built in — the CORRECT stub passes
  every property while the NAIVE stub is FLAGGED on the limit-boundary /
  Retry-After / RateLimit-header properties, so the kit demonstrably
  distinguishes a correct limiter from a broken one. Honest caveat carried in
  PROVENANCE + the listing: the standard `RateLimit-*` header fields are an
  IETF DRAFT (not yet an RFC), so the kit tests the draft/legacy `X-RateLimit-*`
  model and says so; the 429 + Retry-After semantics are stable RFC 6585 / RFC
  9110. Born-red card holds the substrate-gate red until the deliberate
  completion flip.

## 💡 Session idea

[[fill:idea]]

## previous-session review

[[fill:prev-review]]

## Work log

- 2026-07-18T17:48Z — Branch `claude/rate-limit-test-kit-2026-07-18` from
  origin/main (`c728933`); collision check clean (no `control/claims/`
  rate-limit claim, no `candidates/rate-limit-test-kit/`, no open PR covering
  it). Born-red card committed (first commit), pushed. Build begins.
