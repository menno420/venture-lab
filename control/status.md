# Venture Lab — status log (neutral snapshot)
updated: 2026-07-21T20:04:35Z

SEAT CLOSED — Tue Jul 21 20:04:35 UTC 2026

> The `control/*` manager↔lane message-bus remains **retired**. This file is a
> neutral status pointer, not a source of truth or an order. This is the final
> closeout heartbeat before the 2026-07-21 read-only cutoff.

**Cutover read (start here):**
- Project closeout — the single durable read of what shipped, the true current
  state, continuation threads, and the owner walkthrough:
  [`../docs/PROJECT-CLOSEOUT.md`](../docs/PROJECT-CLOSEOUT.md).
- Living ledger: [`../docs/current-state.md`](../docs/current-state.md).
- Owner start page: [`../docs/publishing/OWNER-START-HERE.md`](../docs/publishing/OWNER-START-HERE.md).
- Cutover dossier: [`../docs/publishing/TRANSITION-DOSSIER.md`](../docs/publishing/TRANSITION-DOSSIER.md).

**Where the tree is (neutral facts, verified live):**
- `main` HEAD is `83faa9c` — the substrate-kit vendored-dist upgrade
  v1.17.0 → v1.20.1 (#282), with its follow-up substrate-gate fix #286.
- `python3 bootstrap.py check --strict` is **green (exit 0)** at that HEAD
  (advisories only, pre-existing: model-line notes on older cards).
- Kit version: `v1.20.1` (`../substrate.config.json`).

**PR list — terminal states (recent, newest first):**
- #287 — final project closeout (closeout doc + records true-up + this
  heartbeat) — the PR carrying this snapshot; lands on green via the landing
  workflow once its born-red session card flips to complete.
- #286 `5172bd9` — substrate-gate fix for the v1.20.1 upgrade — MERGED.
- #282 `83faa9c` — substrate-kit v1.20.1 upgrade — MERGED (current HEAD).
- #281 `d2d49ec` — end-of-day owner-list + heartbeat + current-state refresh — MERGED.
- #279 `3bb962b` — Night Kiln Book 6 — MERGED.
- #278 `a2ab822` — Ultramarine Book 3 — MERGED.
- #277 `c689783` — distribution submission pack — MERGED.
- (Full shipped history with cites: `../docs/PROJECT-CLOSEOUT.md` §1.)

**Catalog (unchanged this pass — neutral counts):**
- Sellables: **1 LIVE SKU** (Stripe Webhook Test Kit $29, 0 organic sales;
  T+14 keep/iterate/delist call 2026-07-26) **+ 19 publish-READY + 3 hard-gated
  bundles** (`../docs/launch/CATALOG.md`).
- Books: **two complete adult trilogies** (Ultramarine Bk 1–3 · Lull/DREAMLINE
  Bk 1–3) **+ a six-book Night Kiln cozy series** (Bk 1–6; Bk 7 planted but
  unwritten); **7 KDP-ready packages**, all still owner-gated on the
  native-speaker proofread.

**Backlog (honest — all owner-gated):**
- Publishing stays owner-gated: the native-speaker proofread plus the KDP/Gumroad
  clicks remain owner-only, and posting the lead magnets is an owner
  paste-and-post. No SKU, generated-file, or publish-surface edits rode this pass.
- Continuation threads in priority order are enumerated in
  [`../docs/PROJECT-CLOSEOUT.md`](../docs/PROJECT-CLOSEOUT.md) §3.

**Automation:**
- routine wipe executed by the coordinator session; see closeout. No live
  autonomous schedules remain; re-arming is a deliberate owner action
  post-relaunch, not an in-repo fact.

kit: v1.20.1
