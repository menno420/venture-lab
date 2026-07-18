# Session — Fold CORS SKU into OWNER-QUEUE + resync CATALOG D-refs

> **Status:** `in-progress`

- **📊 Model:** [[fill: model · effort · task-class]]
- **started (date -u):** Sat Jul 18 21:52 UTC 2026
- **branch:** `claude/owner-queue-cors-fold`
- **base:** `main@bf8d5ec`
- **purpose:** the CORS Preflight Test Kit $29 (merged in PR #242, ORDER 016) is
  built, priced, listing-drafted, and already registered in
  `docs/launch/CATALOG.md` — but it is NOT in `docs/publishing/OWNER-QUEUE.md`.
  PR #242 deliberately did NOT regenerate the owner queue because
  `scripts/derive_owner_queue.py` renumbers shared decision IDs (D-refs) that
  CATALOG.md cites; it flagged the regen as an explicit owner/next-session
  follow-up. A sellable absent from the owner queue is not owner-click-ready, so
  #242's value is unbanked until it is folded in. This slice does that fold: add
  the CORS packet to the queue via the repo's real generation path (the derive
  script auto-picks up the on-main CORS vetting packet), regenerate OWNER-QUEUE,
  and resync every renumbered D-ref in CATALOG.md so no dangling or wrong D-ref
  remains.
- **mechanism (not hand-fabricated):** the CORS vetting packet
  `docs/publishing/vetting/cors-preflight-test-kit.md` is already on main with a
  §7 ⚑ OWNER-GATE storefront-pick decision. `derive_owner_queue.py` traverses
  the vetting dir in sorted-filename order; `cors-preflight-test-kit.md` sorts
  between `auto-merge-enabler-cookbook.md` (D3) and `false-green-test-trap.md`,
  so CORS derives as the new **D4** and every alphabetically-later decision
  shifts +1 (D4→D5 … D27→D28). OWNER-QUEUE is a GENERATED file — it is
  regenerated, never hand-edited.
- **scope (files):** EDIT `docs/publishing/OWNER-QUEUE.md` (regenerated),
  EDIT `docs/launch/CATALOG.md` (CORS row/positioning → D4; every renumbered
  D-ref resynced; sourcing + provenance notes updated to the CORS insert).
  No packet edit (the packet is the source of truth and already correct). Plus
  claim + this born-red card + a `control/status.md` heartbeat. Born-red card
  holds substrate-gate red until the completion flip.

## 💡 Session idea

[[fill: one idea]]

## previous-session review

[[fill: prev-session review remark]]

## Work log

- 2026-07-18T21:5xZ — Branch `claude/owner-queue-cors-fold` from origin/main
  (`bf8d5ec`); collision check clean (no prior `control/claims/owner-queue-cors-fold`
  entry, no open PR covering the CORS owner-queue fold). Investigated the derive
  path, captured the BEFORE D-ref → SKU map, and confirmed CORS derives at D4
  (regen dry-run: 28 decisions, 58/58 inputs clean). Claim + born-red card
  committed (first commit), pushed. Build begins.
