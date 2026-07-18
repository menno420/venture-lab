# Session — Idempotency Key Test Kit $29 (new sellable → owner-click-ready)

> **Status:** `complete`

- **📊 Model:** claude-opus-4-8 family · high effort · new-sellable build
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

💡 **An "API Robustness Bundle" + a shared `candidates/_api-hardening-core/`.**
This kit and the webhook line now split cleanly into a coherent product family:
the four webhook kits verify the INBOUND edge (a provider's signature on requests
coming in), and this kit verifies the OUTBOUND edge (safe retries on the writes
your service sends out). The obvious next SKU is a **rate-limit / retry-backoff
test kit** — does your client honour `Retry-After` / `429` with exponential
backoff + jitter, and does your server emit correct `429` + `RateLimit-*` headers
(the IETF `RateLimit` header draft) — which pairs with this idempotency kit into
an **API Robustness Bundle** ($29 + $29 → a $49 anchor, the same higher-AOV move
the Webhook Verifier Bundle makes for the signature four-pack; a client that
retries on 429 is EXACTLY the client that needs idempotency, so the cross-sell is
native). The mechanical enabler is the consolidation both the Shopify card (#227
💡) and the bundle card (#231 💡) already flagged: the webhook kits + this kit now
share ~70% of their scaffold by copy — the byte-reproducible allow-list
`package.sh`, the `_insecure_handler`/reference-stub HTTP test scaffold, the
`is_2xx`/verdict pair, the `post`/`get`/`build_request` HTTP shape, the
side-effect-counter demo pattern, and the PROVENANCE discipline (pinned per-fixture
sha256 + a cited source per fact). Extract a `candidates/_api-hardening-core/`
the kits inherit — plus a `provenance_lint.py` that FAILS a kit whose fixture
lacks a pinned sha256 or a cited source — so kit N+1 (rate-limit? pagination-
cursor? optimistic-concurrency/ETag?) is a scheme-and-fixtures diff, not a
re-implementation, and the honesty bar is machine-enforced. This kit already
proved the template stretches from signature-verification to stateful
multi-request dedup without breaking the shared shape — the strongest signal yet
that the core is worth extracting before it drifts five ways.

## previous-session review

previous-session review: `.sessions/2026-07-18-storefront-catalog.md` (PR #232,
slice-2 of the continued ORDER 016 run — the cross-SKU **Storefront Catalog**
launch asset) — a disciplined conversion asset that did the honest things right:
it COMPLEMENTED the per-SKU listing copy rather than duplicating it, derived
every price/status/D-number from the authoritative generated OWNER-QUEUE (not
from memory), marked the two hard-gated bundles honestly, added NO §7 packet and
regenerated NO queue (an asset is not a publish surface), and reconciled the
current-state "10 READY" drift against the queue in an explicit sourcing note.
Its 💡 — a `scripts/derive_catalog.py` that machine-emits the comparison table
from the packets/queue so the one drift-prone artifact can't fall out of sync —
landed as prophecy THIS session: adding the Idempotency kit at D6 shifted eight
of that hand-maintained table's D-numbers, and I had to reconcile them by hand
(table + bundle gates + publish order + provenance). That hand-reconcile is
exactly the toil the 💡 predicted; three cards now independently converging on
"machine-derive the one drift-prone table" (its own, the #231 bundle MANIFEST,
the night-kiln runtime table) is the strongest signal that the derive-catalog
script is the next high-leverage hygiene slice — and this session is its first
concrete cost receipt.

## Work log

- 2026-07-18T17:00Z — Branch `claude/idempotency-key-test-kit-2026-07-18` from
  origin/main (`8c60cfc`); collision check clean (no `control/claims/`
  idempotency claim, no `candidates/idempotency-key-test-kit/`, no open PR
  covering it). Born-red card committed (first commit), pushed. Build begins.
- 2026-07-18T17:2xZ — Built the full kit as a NEW problem class (idempotency /
  safe-retry, not signature verification): `ikt.py` + `ikt.js` harness, CORRECT
  `stub_handler.py` (per-`(method,path,key)` store + fingerprint + stored
  response + per-key in-flight lock + side-effect counter), NAIVE
  `stub_handler_naive.py` (no dedup, the value proof), 20-test real-path suite,
  docs-derived fixtures + PROVENANCE (Stripe model + IETF header draft, honest).
  20 tests green from source AND from the extracted zip; `ikt demo` both ports:
  correct all-5-pass (counter 5 = exactly-once) + naive flagged on 4 (counter
  9 = over-executed); `package.sh` double-rebuild byte-identical (sha256
  `8607803d5fd7286e9f86f1515981ea1ca6052ae06d7a8d417526dd85a796f6e1`, 32,925
  bytes, 14 content files); secret-shape scan 0 hits. Wired the
  `idempotency-key-test-kit-tests` CI job. Landed the launch dir, the §7 vetting
  packet (backticked filenames in §7 checkboxes so the derive script emits no
  broken links), and the regenerated OWNER-QUEUE (52/52 clean; +1 decision D6 +
  a 5-click publish sequence; later product D-numbers shifted +1). Reconciled
  the hand-maintained `docs/launch/CATALOG.md` (new row + every shifted
  D-number). `bootstrap.py check --strict`: 0 dead-links, only the born-red HOLD
  red (by design). PR #233 opened READY. Card flipped `complete` (this commit).
