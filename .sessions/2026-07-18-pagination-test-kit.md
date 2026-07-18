# Session — Pagination Test Kit $29 (new sellable → owner-click-ready)

> **Status:** `complete`

- **📊 Model:** claude-opus-4-8 family · high effort · new-sellable build
- **started (date -u):** Sat Jul 18 18:17 UTC 2026
- **branch:** `claude/pagination-test-kit-2026-07-18`
- **base:** `main@dfec52e`
- **purpose:** build the **Pagination Test Kit ($29)** to owner-click-ready and
  land it as ONE PR — a NEW sellable in the API-robustness kit family, a
  DIFFERENT problem class from the webhook signature kits, the idempotency kit,
  and the rate-limit kit. Where the webhook kits verify an inbound provider
  *signature*, the idempotency kit verifies a *safe-retry / exactly-once* dedup
  contract, and the rate-limit kit verifies a *throttling* contract, this kit
  verifies a buyer's OWN paginated endpoint's **result-set integrity**: that
  following the next-cursor from page 1 yields every item with NO overlap and NO
  gap (concatenating all pages reproduces the full ordered set exactly once);
  that the traversal is **stable under mutation** — inserting and deleting rows
  BETWEEN page fetches must not skip or duplicate items present throughout (the
  headline property, where naive OFFSET pagination fails); that a consistent
  total order holds (stable sort key + unique tiebreaker); that the page-size
  limit is honored and an over-max limit is clamped to a documented maximum; that
  the last page signals the end (null/absent next-cursor) with no infinite loop;
  and that a malformed or forged/opaque cursor is rejected (400), not silently
  mishandled. Stdlib-only, account-free, runs with a loud DEMO banner against
  bundled reference stubs. Ships: a CORRECT reference stub (keyset/cursor
  pagination over a sortable dataset on `(sort_key, id)` with an opaque,
  HMAC-signed cursor), a deliberately NAIVE/broken stub (OFFSET/LIMIT pagination
  that skips items under mid-traversal mutation, no over-max clamp, accepts a
  forged cursor) so the suite can PROVE it catches the bug, a `pgtk.py` harness
  (+ `pgtk.js` Node parity) a buyer points at their own endpoint, an HTTP-layer
  real-path test suite that performs a controlled mid-traversal mutation, real
  docs-derived fixtures + PROVENANCE (cited to the common keyset/cursor
  pagination pattern and the Stripe/Slack/GitHub cursor-pagination docs + the
  keyset-vs-offset literature), a byte-reproducible buyer bundle, and a §7
  owner-gate publish packet. The build ENDS at a queued owner ⚑ publish click
  (rail 13 / CONSTITUTION §13) — no publish, no spend, no accounts by the seat.
- **session:** Mirrors the proven rate-limit-test-kit / idempotency-key-test-kit
  scaffold (the closest templates — same correct-stub + naive-stub evidence
  pattern) but is a genuinely DIFFERENT product: pagination / result-set
  integrity, not throttling, dedup, or signature verification. The value proof is
  built in — the CORRECT stub passes every property while the NAIVE stub is
  FLAGGED on the stability-under-mutation / page-size-clamp / cursor-tamper
  properties, so the kit demonstrably distinguishes correct keyset pagination
  from a broken offset one. Honest caveat carried in PROVENANCE + the listing:
  the kit tests the widely-deployed keyset/cursor model (opaque signed cursor
  over `(sort_key, id)`) and says so; there is no single RFC for cursor
  pagination, so the sources are the common pattern + named vendor docs, cited
  honestly. Born-red card holds the substrate-gate red until the deliberate
  completion flip.

## 💡 Session idea

💡 **The fourth leg is on — ship the "API Robustness Bundle" (Idempotency +
Rate-Limit + Pagination) and extract `candidates/_api-hardening-core/` before the
four kits calcify into four copies of the same code.** The catalog now has three
sibling dev-tool kits that test a buyer's OWN endpoint (idempotency = safe-retry,
rate-limit = throttling, pagination = result-set integrity) plus the four webhook
kits that test the INBOUND edge. Those three "own-endpoint" kits share ~70% of
their scaffold by literal copy: the byte-reproducible allow-list `package.sh`, the
correct-stub + naive-stub HTTP test scaffold, the `fire`/`is_2xx`/verdict pair, the
`/_debug/reset` + `/_debug/all` state/mutation demo pattern, the `PageSpec`/fixture
indirection, and the PROVENANCE discipline (a pinned per-fixture sha256 + a cited
source per fact). Two obvious moves: (1) an **API Robustness Bundle** at a ~$69
anchor (Idempotency $29 + Rate-Limit $29 + Pagination $29 → the same bundle-discount
play the Webhook Verifier four-pack makes) — a developer hardening one API needs all
three, and a client that retries on 429 with backoff is exactly the client that
needs idempotent writes AND correct pagination on the list it re-fetches, so the
cross-sell is native; (2) the mechanical enabler flagged now by four independent
cards (Shopify #227 💡, the bundle #231 💡, idempotency #233 💡, rate-limit #236 💡):
extract `candidates/_api-hardening-core/` the kits inherit, plus a
`provenance_lint.py` that FAILS any kit whose fixture lacks a pinned sha256 or a
cited source, so kit N+1 (optimistic-concurrency/ETag? conditional-request
`If-Match`/`304`?) is a scheme-and-fixtures diff, not a re-implementation, and the
honesty bar is machine-enforced. This build stretched the shared shape a fourth way
— from stateful dedup (idempotency) through timing/windows (rate-limit) to
ordered-set integrity under mutation (pagination, with a keyset cursor, an
HMAC-signed opaque token, and a controlled mid-traversal mutation) — without
breaking it, which is the strongest signal yet that the divergence is real and the
core should be pulled before it hardens into four copies of the same bugs.

## previous-session review

previous-session review: `.sessions/2026-07-18-rate-limit-test-kit.md` (PR #236, the
R1 Rate-Limit Test Kit — the third API-robustness kit, throttling correctness).
Strong, honest build and a clean template to mirror: the correct/naive stub pair is
the load-bearing value proof (correct passes all six; naive is flagged on
over-limit/retry-after/headers/retry-after-honored and honestly NOT on
under-limit/window-reset), and the card is exemplary about the softer half of its
own claims — it states up front that the `RateLimit-*` header fields are an IETF
DRAFT (not an RFC) whose newest revisions favour a combined field the kit does not
assert, while the 429 + Retry-After half rests on stable RFC 6585/9110. This
pagination kit deliberately inherited that same "name your sources honestly, mark
the non-distinguishing properties out loud" discipline (here: no single RFC for
cursor pagination at all, stated plainly). One nit worth carrying into the core
extraction: the rate-limit suite pays real wall-clock time for its windowed waits
(~11s) where this kit has none — a shared harness should keep timing-based checks
opt-in so the fast kits stay fast in CI.
