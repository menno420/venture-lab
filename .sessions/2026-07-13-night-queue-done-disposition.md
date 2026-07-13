# Session — Night run: DONE disposition for the derived owner queue (ORDER 008)

> **Status:** `in-progress`

- **📊 Model:** fable-5 · worker slice · ORDER 008 night-run product lane
- **session:** teach `scripts/derive_owner_queue.py` an already-live/DONE
  disposition (`- [x] ⚑ **Owner:** … — DONE <ISO date>` → read-only
  "Live / completed" section, zero pending clicks), write the SWTK §7 packet
  using it so the queue finally shows the one product actually earning, and
  upgrade `docs/products/TEMPLATE.md` stage 6 (buyer-side self-rebuild proof)
  + stage 8 (post-click DONE flip).
- **started (date -u):** Sun Jul 13 01:44 UTC 2026
- **closed (date -u):** (in progress)

## ⟲ Previous-session review

(filled at close)

## 💡 Session idea

(filled at close)

## Scope

- `scripts/derive_owner_queue.py` — DONE disposition, backward-compatible
  (all 13 existing packets must parse EXACTLY as before; proven by
  before/after regen diff).
- `scripts/test_derive_owner_queue.py` — new stdlib test: legacy packet
  unchanged, DONE row lands in Live section, mixed packet.
- `docs/publishing/vetting/stripe-webhook-test-kit.md` — SWTK packet, all
  rows DONE (live 2026-07-12), zero new pending clicks.
- `docs/publishing/OWNER-QUEUE.md` — regenerated.
- `docs/products/TEMPLATE.md` — stage-6 + stage-8 upgrades.
