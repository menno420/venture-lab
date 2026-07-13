# Session — Night run: ⏲/KILL-CHECK column in the derived owner queue (ORDER 008)

> **Status:** `in-progress`

- **📊 Model:** fable-5 · worker slice · ORDER 008 night-run product-infra lane
- **session:** pay down THE top backlog debt (named by three consecutive
  cards): the derived owner queue's "Live / completed" section cannot show
  kill-clock checkpoints, so the owner can't see "which live product needs
  a look today". Slice: extend `scripts/derive_owner_queue.py` with an
  optional packet-level `KILL-CHECK:` line carrying `⏲ <ISO date> <label>`
  tokens, rendered earliest-first as a next-checkpoint indication in the
  Live section; byte-identical backward-compat proof on the untouched
  tree; tests; SWTK packet updated with the real 2026-07-19 (T+7) /
  2026-07-26 (T+14) checkpoints from its LAUNCH-LOG; TEMPLATE stage-8 doc.
- **started (date -u):** Sun Jul 13 02:38:59 UTC 2026
- **closed (date -u):** (in progress)

## ⟲ Previous-session review

(pending — filled at close)

## 💡 Session idea

(pending — filled at close)

## Scope

- `scripts/derive_owner_queue.py` — KILL-CHECK grammar + Live-section
  rendering + stdout line.
- `scripts/test_derive_owner_queue.py` — token parsed / earliest-first /
  absent-token unchanged / malformed-date tests.
- `docs/publishing/vetting/stripe-webhook-test-kit.md` — real checkpoints.
- `docs/publishing/OWNER-QUEUE.md` — regenerated.
- `docs/products/TEMPLATE.md` — stage-8 token documentation.
