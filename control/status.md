# Venture Lab — status log (neutral snapshot)
updated: 2026-07-20T07:36:15Z

> The `control/*` manager↔lane message-bus remains **retired**. This file is a
> neutral status pointer, not a source of truth or an order. The successor reads
> [`../docs/current-state.md`](../docs/current-state.md),
> [`../docs/publishing/OWNER-START-HERE.md`](../docs/publishing/OWNER-START-HERE.md),
> [`../docs/publishing/TRANSITION-DOSSIER.md`](../docs/publishing/TRANSITION-DOSSIER.md),
> and [`../docs/launch/CATALOG.md`](../docs/launch/CATALOG.md).

**Where the tree is (neutral facts):**
- `main` HEAD is `d2d49ec` — the 2026-07-20 end-of-day owner-list + heartbeat +
  current-state refresh (#281), which rode on top of #279 (Night Kiln Book 6).
  This pass's two PRs ride on top of that base.
- `python3 bootstrap.py check --strict` is **green (exit 0)** at that HEAD
  (advisories only, pre-existing: seat-digest stale/over-budget + model-line
  notes).
- Kit version: `v1.17.0` (an upgrade to `v1.20.1` is proposed on a separate open
  PR, not part of this pass).

**What this pass did (2026-07-20):**
- **QA'd the owner click-surface.** A read-only sweep of the owner-facing surface
  (OWNER-START-HERE, the transition dossier, the 7 KDP-ready packages, the
  submission-pack channel files, the catalog counts) — links resolve, manuscripts
  are un-truncated, metadata is complete, no fabricated stats. The content-staleness
  and consistency fixes it surfaced are **in flight on a companion QA PR** (branch
  `claude/owner-surface-qa`).
- **Added the season-2 plan.** `docs/ideas/2026-07-20-season-2-plan.md` — a
  prioritized, contingency-shaped build plan for the world after the 2026-07-21
  write-cutoff, organised as ordered branches keyed to which owner action fires
  first (lead magnets posted · vetoes arrive · a book sells · trading data
  provisioned) plus a standing upkeep cadence. Planning-only, decide-and-flagged,
  owner-gated items marked. Linked from `docs/ideas/README.md`.
- **This heartbeat + a current-state restamp** — `control/status.md` overwritten
  LAST as neutral prose pointers; `docs/current-state.md` restamped to the current
  HEAD/date noting the plan doc now exists. No SKU, no publish surface, no
  generated file touched.

**Catalog (unchanged this pass — neutral counts):**
- Sellables: **1 LIVE SKU** (Stripe Webhook Test Kit $29) **+ 19 publish-READY +
  3 hard-gated bundles** (`../docs/launch/CATALOG.md`).
- Books: **two complete adult trilogies** (Ultramarine Bk 1–3 · Lull/DREAMLINE
  Bk 1–3) **+ a six-book Night Kiln cozy series** (Bk 1–6; Bk 7 planted but
  unwritten); **7 KDP-ready packages**, all still owner-gated on the
  native-speaker proofread.

**Read-path pointers (neutral):**
- Living ledger: [`../docs/current-state.md`](../docs/current-state.md).
- Season-2 plan: [`../docs/ideas/2026-07-20-season-2-plan.md`](../docs/ideas/2026-07-20-season-2-plan.md).
- Owner publish/proofread click-path:
  [`../docs/publishing/OWNER-START-HERE.md`](../docs/publishing/OWNER-START-HERE.md).

**Backlog (honest):**
- Publishing stays **owner-gated**: the native-speaker proofread plus the
  KDP/Gumroad clicks remain owner-only, and posting the lead magnets is an owner
  paste-and-post. No SKU, generated-file, or publish-surface edits rode this pass.
- **Nothing is due before Friday's grading (2026-07-24)** — the SWTK T+14
  keep/iterate/delist read follows on **2026-07-26** with its inputs already
  written (`../docs/launch/funnel-diagnostic.md`, `../docs/launch/kill-clock-decision-packet.md`).

kit: v1.17.0
