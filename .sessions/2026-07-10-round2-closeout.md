# Session — round 2 close-out (ledger + capabilities + status)

> **Status:** `complete`

- **📊 Model:** claude-opus-4-8[1m] · high · round2-closeout
- **session:** venture-lab session 1 round 2 — verify the round-2 landed state
  authoritatively, consolidate the venture ledger + capability manifest, and run
  the close ritual in one PR
- **started (date -u):** Fri Jul 10 03:26:55 UTC 2026
- **completed (date -u):** Fri Jul 10 03:28:55 UTC 2026

## Purpose

Round 2 shipped two builds under a single PR (#7) because of a shared-tree git
race. This session establishes ground truth (both candidate trees present +
correct, both session cards present, 13/13 kit tests green, `check --strict`
exit 0), then brings the durable records current: candidate #1 → v0.2
(persistence), candidate #2 → publish-ready v0.1, plus the worktree-race recipe
that the shared-tree collision earned. No owner-gated action performed.

## ⟲ Previous-session review

⟲ previous-session review: PR #7 (6b4ad52) landed BOTH candidate #1 v0.2
(pluggable `MembershipStore` ABC + `JsonFileStore` that survives restart +
`SupabaseStore` skeleton + 13 tests) AND candidate #2 v0.1 (drop-in pack + $19
PWYW listing), because candidate-02's `git add -A` swept candidate-01's
uncommitted v0.2 files into its commit in a shared clone. Content is
byte-identical/correct and verified on main; the cost was per-workstream PR
attribution. This close-out records that lesson as a capability recipe and
re-anchors the ledger + status heartbeat to the real landed state.

## 💡 Session idea

💡 Attribution is a property of the *tooling boundary*, not of discipline. Both
builders followed the protocol perfectly — claim-before-build, born-red card,
close ritual — and still collided, because `git add -A` in a shared working tree
is a wider blast radius than any convention can fence. The durable fix is
mechanical isolation (a worktree per mutating worker), not more rules. When two
correct agents produce a wrong *outcome*, suspect the substrate they share, not
their behavior.

## Log

- Synced to `origin/main` @ 6b4ad52; hard-reset; captured NOW_UTC 03:26:55Z.
- Verified ground truth: `MembershipStore` ABC + `JsonFileStore` +
  `SupabaseStore` present in `server/app.py`; `python3 -m unittest
  test_membership -v` → 13 tests OK; `python3 bootstrap.py check --strict` →
  exit 0; both candidate trees + both session cards
  (`candidate-01-v02.md`, `candidate-02.md`) present.
- Re-read `control/inbox.md` at HEAD: holds ONLY ORDER 001 (`status: new`); no
  new order.
- Branched `venture-lab/session-1-round2-closeout`.
- Updated `docs/research/venture-ledger.md`: candidate #1 → v0.2 entry
  (persistence, 13 tests, honest token-cost) + new candidate #2 entry
  (publish-ready v0.1) + added ⚑D (publish template-packs listing).
- Appended the parallel-workers / isolated-worktree recipe to
  `docs/capabilities.md` under CAN.
- Overwrote `control/status.md`: round-2-complete heartbeat, refreshed ⚑A–⚑D +
  the advisory kit-token NOTE + attribution note.

## Deliverable summary

One PR consolidating round 2: the venture ledger now reflects candidate #1 at
v0.2 (pluggable, restart-surviving persistence, 13 passing tests) and candidate
#2 at publish-ready v0.1 (real drop-in pack + $19 PWYW cross-selling listing);
the capability manifest carries a new worktree-isolation recipe earned by the
shared-tree race behind PR #7; and the status heartbeat is green with owner
actions ⚑A–⚑D structured and current. Nothing owner-gated was performed.
