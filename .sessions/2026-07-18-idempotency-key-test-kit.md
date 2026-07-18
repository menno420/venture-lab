# Session — Idempotency Key Test Kit $29 (new sellable → owner-click-ready)

> **Status:** `in-progress`

- **📊 Model:** [[fill:model]]
- **started (date -u):** Sat Jul 18 17:00:18 UTC 2026
- **branch:** `claude/idempotency-key-test-kit-2026-07-18`
- **base:** `main@8c60cfc`
- **purpose:** build the **Idempotency Key Test Kit ($29)** to owner-click-ready
  and land it as ONE PR — a NEW, NON-webhook sellable in a DIFFERENT problem
  class from the webhook signature kits. Where the webhook kits verify a
  provider's *signature* on an inbound request, this kit verifies a buyer's OWN
  API's `Idempotency-Key` handling: that a safe retry with the same key + same
  body triggers the side effect **exactly once** and replays the STORED original
  response; that the same key with a DIFFERENT body is rejected (409/422); that a
  missing key follows a documented policy; that two concurrent same-key requests
  produce ONE side effect (in-flight lock); and that keys are scoped per
  endpoint. Stdlib-only, account-free, runs with a loud DEMO banner against
  bundled reference stubs. Ships: a CORRECT reference stub, a deliberately NAIVE
  (no-dedup) stub so the suite can PROVE it catches the double-charge bug, a
  `ikt.py` harness (+ `ikt.js` Node parity) a buyer points at their own
  endpoint, an HTTP-layer real-path test suite with a side-effect counter, real
  docs-derived fixtures + PROVENANCE (cited to Stripe's idempotency docs + the
  IETF `Idempotency-Key` header draft), a byte-reproducible buyer bundle, and a
  §7 owner-gate publish packet. The build ENDS at a queued owner ⚑ publish click
  (rail 13 / CONSTITUTION §13) — no publish, no spend, no accounts by the seat.
- **session:** Mirrors the proven Stripe/Slack/Shopify webhook-kit scaffold (file
  set, evidence bar, packaging, listing/vetting grammar) but is a genuinely
  DIFFERENT product: dedup / safe-retry semantics, not signature verification.
  The value proof is built in — the CORRECT stub passes every property while the
  NAIVE stub is FLAGGED on the exactly-once / mismatch / concurrency / missing-key
  properties, so the kit demonstrably distinguishes correct idempotency from
  broken. Honest caveat carried in PROVENANCE + the listing: behaviour specifics
  follow Stripe's widely-used model (the IETF header draft standardises the
  header, not the exact status codes), and the fixtures are docs-derived, not
  wire-captured. Born-red card holds the substrate-gate red until the deliberate
  completion flip.

## 💡 Session idea

[[fill:idea]]

## previous-session review

[[fill:prev-review]]

## Work log

- 2026-07-18T17:00Z — Branch `claude/idempotency-key-test-kit-2026-07-18` from
  origin/main (`8c60cfc`); collision check clean (no `control/claims/`
  idempotency claim, no `candidates/idempotency-key-test-kit/`, no open PR
  covering it). Born-red card committed (first commit), pushed. Build begins.
