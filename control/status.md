# Venture Lab — status log (neutral snapshot)
updated: 2026-07-19T21:50:53Z

> The `control/*` manager↔lane message-bus remains **retired**. This file is a
> neutral status pointer, not a source of truth or an order. The successor reads
> [`../docs/current-state.md`](../docs/current-state.md),
> [`../docs/publishing/OWNER-START-HERE.md`](../docs/publishing/OWNER-START-HERE.md),
> [`../docs/publishing/TRANSITION-DOSSIER.md`](../docs/publishing/TRANSITION-DOSSIER.md),
> and [`../docs/launch/CATALOG.md`](../docs/launch/CATALOG.md).

**Where the tree is (neutral facts):**
- `main` HEAD is `d776fd7` — "KDP-ready packages for the 5 new book sequels
  (#274)". Latest-numbered merged PR is #275 (the transition dossier).
- `python3 bootstrap.py check --strict` is **green (exit 0)** at that HEAD
  (advisories only, pre-existing).

**What this consolidation pass landed (2026-07-19):**
- **5 KDP-ready book packages (#274)** — each of the five new sequels now has an
  upload-ready `MANUSCRIPT-KDP.md`, a paste-ready `KDP-METADATA.md`, and a
  `SELF-EDIT-PASS.md` self-edit log under `candidates/.../kdp-ready/`.
- **Transition dossier (#275)** — `docs/publishing/TRANSITION-DOSSIER.md`: one
  neutral read of the whole venture state at the 2026-07-21 read-only cutoff.
- **Owner-steps + current-state refresh (this PR)** — the five ready sequels are
  written up as owner publish steps in `docs/publishing/OWNER-START-HERE.md` §4,
  and `docs/current-state.md` is restamped to HEAD `d776fd7` with the complete
  5-book Night Kiln series, the complete Lull trilogy, and the new KDP/dossier
  artifacts.

**Read-path pointers (neutral):**
- Living ledger: [`../docs/current-state.md`](../docs/current-state.md).
- Owner publish/proofread click-path:
  [`../docs/publishing/OWNER-START-HERE.md`](../docs/publishing/OWNER-START-HERE.md).
- Full cutover state:
  [`../docs/publishing/TRANSITION-DOSSIER.md`](../docs/publishing/TRANSITION-DOSSIER.md).

**Backlog (honest):**
- Publishing stays **owner-gated**: the native-speaker proofread plus the
  KDP/Gumroad clicks remain owner-only. No SKU, generated-file, or publish-surface
  edits rode this pass.

kit: v1.17.0
