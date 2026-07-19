# Session — ENG-6: owner-queue idempotence guard

> **Status:** `complete`

- **📊 Model:** Claude Opus (4.x family) · high · tooling
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

💡 **`OWNER-QUEUE.md` is not the only GENERATED file that can silently drift —
promote the same idempotence invariant to a reusable guard over EVERY derived
artifact, starting with `docs/seat-digest.md`.** While closing this slice
`bootstrap.py check --strict` emitted a `seat-digest-stale` advisory: the
committed `docs/seat-digest.md` "differs from a fresh render of its sources" —
i.e. the SAME hand-edit / un-regenerated-input class this ENG-6 guard now makes
REQUIRED for the owner queue, but for the seat digest it is only an ADVISORY
nudge (never exit-affecting), so a stale digest ships downstream to every
fresh-seat prompt. The generalization is small and mechanical: this guard's
shape is exactly `committed == generator.render(current inputs)`; lift
`regenerate()`/`check()` from a hard-coded (queue, derive_owner_queue) pair into
a tiny REGISTRY of `(generated_path, render_callable)` entries and run each as a
required byte-idempotence check. Guard recipe: generalize
`scripts/check_owner_queue_idempotent.py::check` to take a registry, register
`(docs/seat-digest.md, bootstrap.seat_digest render)` alongside the queue entry,
and add a `test_*` catch-case per registered artifact (hand-edit the committed
render → guard fires). That converts the seat-digest advisory — which is
green-but-stale right now — into the same born-required gate, closing the last
"generated file drifted and nobody's build turned red" hole in the repo.

## previous-session review

previous-session review: `.sessions/2026-07-19-owner-steps-refresh.md` (PR #260,
`8a1e728`) — added the curated plain-language `OWNER-START-HERE.md` companion and
deliberately did NOT hand-edit the GENERATED `OWNER-QUEUE.md`, linking back to it
instead ("must not be hand-edited"). That restraint was the correct human call;
this ENG-6 slice makes it a MACHINE call — the guard now reds any PR that edits
the generated queue directly or lets a packet drift without a regen, so the next
session can't accidentally do what #260 was careful to avoid by hand.

## Work log

- 2026-07-19T08:28Z — Branch `claude/eng6-owner-queue-idempotence-guard` from
  origin/main (`8a1e728`); collision check clean (no prior
  `control/claims/eng6-owner-queue-idempotence-guard` entry, no open PR covering
  ENG-6). Confirmed the committed OWNER-QUEUE.md is already idempotent under
  `derive_owner_queue.py` (regen dry-run to a temp file diffs byte-clean, 28
  decisions, 58/58 inputs). Claim + this born-red card committed (first commit
  `c7c3db1`). Build begins.
- 2026-07-19T08:3xZ — **Build.** Added `scripts/check_owner_queue_idempotent.py`
  (imports `derive_owner_queue`; drives its own `parse_packet` /
  `parse_keyword_map` / `render` over the live tree; asserts committed queue ==
  fresh regeneration; exit 0 clean / 1 on drift with a unified-diff summary) +
  `scripts/test_check_owner_queue_idempotent.py` (7 tests: live-tree-green,
  parsed-real-packets sanity, hand-edit catch, input-drift catch, no-packets
  skip). Wired a new REQUIRED `owner-queue-idempotence-guard` job into
  `.github/workflows/kit-tests.yml` (checker on the live tree + unittest),
  mirroring the `catalog-dref-guard` job. Committed `208df65`, pushed.
- 2026-07-19T08:3xZ — **Verification.** Guard EXIT 0 on the live tree
  ("byte-identical to a fresh regeneration — idempotent"); `python3 -m unittest
  test_check_owner_queue_idempotent -v` 7/7 OK; no real OWNER-QUEUE.md regen was
  needed (already idempotent). `bootstrap.py check --strict` reported only the
  born-red HOLD (by design) + pre-existing seat-digest / model-line advisories
  (non-exit-affecting) — no new failure. Reverted the local
  `.substrate/guard-fires.jsonl` telemetry append to keep the PR scoped.
- 2026-07-19T08:3xZ — Flip to `complete` (this commit): Status badge, 📊 Model
  line, one 💡 idea, previous-session review, all `[[fill:]]` slots resolved.
  Post-flip `bootstrap.py check --strict` EXIT 0 (advisories only). Born-red HOLD
  clears.
