# Session — ENG-6: owner-queue idempotence guard

> **Status:** `in-progress`

- **started (date -u):** Sun Jul 19 08:28 UTC 2026
- **branch:** `claude/eng6-owner-queue-idempotence-guard`
- **base:** `main@8a1e728`
- **purpose:** implement roadmap item **ENG-6** — a REQUIRED guard that pins the
  idempotence of `docs/publishing/OWNER-QUEUE.md` under its generator
  `scripts/derive_owner_queue.py`. The queue is a GENERATED file (derived from
  the §7 ⚑ OWNER-GATE blocks of `docs/publishing/vetting/*.md` plus ⚑ OWNER
  conflicts in `docs/publishing/keyword-map.md`) whose determinism the whole
  D-ref safety story depends on. ENG-2 (#248, `check_catalog_drefs.py`) catches
  a mispoint *after* a regen introduces it; nothing yet catches the class that
  *causes* the mispoint — a hand-edit to the generated file, or an input packet
  drifting without a regen. This slice closes that: re-run the generator's pure
  render over the current inputs and assert the output byte-matches the committed
  queue; a mismatch (someone hand-edited the generated file, or a packet changed
  without regenerating) reds with a unified-diff summary.
- **mechanism (not hand-fabricated):** the guard imports `derive_owner_queue`
  and calls its own `parse_packet` / `parse_keyword_map` / `render` against the
  live tree — no re-implementation of the queue format, so it can never drift
  from the generator. Determinism is already a documented property of the derive
  script (sorted traversal, no timestamps → byte-identical re-runs), so on a
  correctly-regenerated tree the guard is silently green.
- **scope (files):** NEW `scripts/check_owner_queue_idempotent.py` (the guard,
  stdlib-only, exit 0 clean / non-zero on drift, `--root` for fixtures),
  NEW `scripts/test_check_owner_queue_idempotent.py` (unittest: green on the live
  tree + hand-edit catch-case + input-drift catch-case), CI wiring in
  `.github/workflows/kit-tests.yml` (new REQUIRED job mirroring the
  `catalog-dref-guard` job), plus the claim and this card. No regen of
  OWNER-QUEUE.md was needed — the committed file is already byte-idempotent under
  the generator (verified: `derive_owner_queue.py --output <tmp>` diffs clean).
- **verify:** `python3 scripts/check_owner_queue_idempotent.py` (exit 0 on the
  live tree) · `cd scripts && python3 -m unittest test_check_owner_queue_idempotent -v`
  · `python3 bootstrap.py check --strict` (exit 0, advisories only).

## 💡 Session idea

[[fill: one genuine idea at close-out]]

## previous-session review

[[fill: one-line review of the previous session card at close-out]]

## Work log

- 2026-07-19T08:28Z — Branch `claude/eng6-owner-queue-idempotence-guard` from
  origin/main (`8a1e728`); collision check clean (no prior
  `control/claims/eng6-owner-queue-idempotence-guard` entry, no open PR covering
  ENG-6). Confirmed the committed OWNER-QUEUE.md is already idempotent under
  `derive_owner_queue.py` (regen dry-run to a temp file diffs byte-clean, 28
  decisions, 58/58 inputs). Claim + this born-red card committed (first commit).
  Build begins.
