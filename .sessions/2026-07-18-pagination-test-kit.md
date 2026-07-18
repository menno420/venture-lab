# Session — Pagination Test Kit $29 (new sellable → owner-click-ready)

> **Status:** `in-progress`

- **📊 Model:** [[fill:model]]
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

[[fill:idea]]

## previous-session review

[[fill:prev-review]]
