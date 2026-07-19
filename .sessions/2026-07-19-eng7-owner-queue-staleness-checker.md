# Session — ENG-7: owner-queue staleness checker

> **Status:** `complete`

![status](https://img.shields.io/badge/status-complete-brightgreen)

- **📊 Model:** Claude Opus (4.x family) · high · test writing
- **started (date -u):** Sun Jul 19 08:57 UTC 2026
- **branch:** `claude/eng7-owner-queue-staleness-checker`
- **base:** `main@f1ab8dc` (post #261 ENG-6 / #262 ENG-5 / #263 ENG-4)
- **purpose:** implement roadmap item **ENG-7** — the OWNER-QUEUE **staleness /
  proofread-gate drift** checker (= PUB-9,
  `docs/ideas/2026-07-19-execution-roadmap.md` line 82 + veto-menu §ENG-7 line 449).
  ENG-6 (#261) pins that the committed `docs/publishing/OWNER-QUEUE.md` is
  byte-identical to a fresh regeneration (idempotence). That leaves an ORTHOGONAL
  class untouched: content that is internally INCONSISTENT even when perfectly
  idempotent — a stale cross-ref, a self-contradictory dated checkpoint, or a
  proofread-gated row that lost its hard-gate. ENG-7 is the required guard for that
  class: it asserts three deterministic, OFFLINE consistency invariants over the
  generated queue and its curated companion.
- **the three staleness invariants (deterministic, offline — no network, no
  wall-clock):**
  - **INV-1 companion cross-ref resolution (staleness / renumber-drift):** every
    `§N` section and `D<n>` decision the curated companion
    `docs/publishing/OWNER-START-HERE.md` (#260) cites into `OWNER-QUEUE.md` must
    still resolve to a real `## N.` / `### D<n> —` header in the committed queue.
    This is the #244/#245 renumber-mispoint class one level UP (companion→queue,
    where ENG-2's D-ref guard is queue→packet): after a regen renumbers decisions,
    a hand-written digest can dangle.
  - **INV-2 dated-checkpoint consistency (staleness / time, made STRUCTURAL):** for
    each live product's §4 kill-clock checkpoints, every date is a well-formed ISO
    calendar date, and any `T+<n>` day-offset labels sharing an anchor are
    arithmetically consistent (T+7 → T+14 must be exactly +7 days). This is the
    time-relative check the roadmap implies, but implemented as a
    structure/consistency assertion — it NEVER compares against "today", so it is
    fully deterministic (wall-clock tests are banned in this repo).
  - **INV-3 proofread-gate integrity (proofread-gate DRIFT):** every §2 click-run
    that contains a native-speaker-proofread owner row MUST render HARD-GATED. This
    reuses the generator's own `PROOFREAD_GATE_RE` / `is_blocking_box`, so it can
    never drift from the render it guards; it catches the #210/#213 class where a
    proofread-gated NL edition is mis-rendered as click-ready to publish
    un-proofread.
- **reuse (can't drift from the generator):** like ENG-6, the checker imports
  `derive_owner_queue` and drives its OWN parser (`parse_packet`, `PROOFREAD_GATE_RE`)
  for INV-2/INV-3, and regexes the two committed docs for INV-1 — no
  re-implementation of the queue format.
- **scope (files):** NEW `scripts/check_owner_queue_staleness.py` (guard, stdlib-only,
  exit 0 clean / non-zero with an itemized per-invariant finding list, `--root` for
  fixtures), NEW `scripts/test_check_owner_queue_staleness.py` (unittest: live-tree
  green + synthetic staleness-catch cases per invariant + skip/edge), CI wiring in
  `.github/workflows/kit-tests.yml` (new REQUIRED `owner-queue-staleness-guard` job
  mirroring `funnel-assets-guard`), plus the claim and this card.
- **known-current-state (reported, not papered over):** NO staleness finding on the
  live tree. INV-1 — all 11 companion cross-refs (§1, §2, D6, D7, D9, D15, D18, D19,
  D20, D22–D25) resolve. INV-2 — the one live product (Stripe Webhook Test Kit) has
  two well-formed checkpoints, T+7 2026-07-19 and T+14 2026-07-26, and 26−19 = 7 days
  matches the 14−7 = 7 ordinal delta. INV-3 — all 13 click-runs carrying a
  native-speaker-proofread row are correctly HARD-GATED. No queue content was
  invented to force a green; the guard reflects the real tree and reds only a FUTURE
  drift.
- **verify:** `python3 scripts/check_owner_queue_staleness.py` (exit 0 on the live
  tree) · `cd scripts && python3 -m unittest test_check_owner_queue_staleness -v` ·
  `python3 bootstrap.py check --strict` (exit 0, advisories only).

## Work log

- 2026-07-19T08:57Z — Branch `claude/eng7-owner-queue-staleness-checker` from
  origin/main (`f1ab8dc`, post #261/#262/#263). Read the ENG-7 spec of record
  (roadmap line 82 + veto-menu §ENG-7), `OWNER-QUEUE.md` end-to-end (esp. §4
  Live/completed + the Stripe T+7/T+14 checkpoints), `derive_owner_queue.py` (the
  generator), `OWNER-START-HERE.md` (the #260 companion), and the ENG-4/5/6 guards +
  their CI jobs it mirrors. Confirmed all three planned invariants hold on the live
  tree before writing the guard. Claim + this born-red card committed. Build begins.
- 2026-07-19T09:0xZ — **Build.** Added `scripts/check_owner_queue_staleness.py` (imports
  `derive_owner_queue`, drives its parser for INV-2/INV-3, regexes the two committed
  docs for INV-1; exit 0 clean / 1 with an itemized per-invariant finding list;
  `--root` for fixtures) + `scripts/test_check_owner_queue_staleness.py` (20 tests:
  live-tree-green + each-invariant-actually-applicable (non-vacuous) + per-invariant
  synthetic catch-cases (dangling D-ref, dangling §, range-upper-bound dangle,
  other-doc §-ref not-false-red, contradictory T+n arithmetic, malformed date,
  proofread-row-lost-hard-gate) + skip + end-to-end nonzero-exit). Wired a new REQUIRED
  `owner-queue-staleness-guard` job into `.github/workflows/kit-tests.yml` (checker on
  the live tree + unittest), mirroring `funnel-assets-guard` (#263). YAML validated.
- 2026-07-19T09:0xZ — **Verification.** Checker EXIT 0 on the live tree (no staleness
  finding). `python3 -m unittest test_check_owner_queue_staleness -v` 20/20 OK.
  `python3 bootstrap.py check --strict` EXIT 0 (pre-existing seat-digest + model-line
  advisories on OTHER cards only — none from this slice; this card's model line is the
  taught three-field form). Reverted the local `.substrate/guard-fires.jsonl` telemetry
  append to keep the PR scoped. No queue content invented.
- 2026-07-19T09:0xZ — Flip to `complete` (this commit): Status badge, 📊 Model line
  (family-level, task-class `test writing`), one 💡 idea, previous-session review, all
  `[[fill:]]` slots resolved. Born-red HOLD clears.

## 💡 Session idea

💡 **The three staleness invariants are hand-picked structural checks; promote the
"what is a stale-able cross-ref / dated token" set to a declared queue-consistency
MANIFEST so a fourth staleness class (or a new dated-token convention) is registered,
not silently unguarded.** INV-1 hard-codes that the companion cites `§N`/`D<n>` into
`OWNER-QUEUE.md`; INV-2 hard-codes the `T+<n>` day-offset convention as the only
dated-token shape it reconciles. Both are correct for today's two artifacts, but the
moment a THIRD owner-facing doc starts citing the queue (a launch-hour sequencer, a
storefront hub), or a checkpoint adopts a `D+<n>`/`W+<n>` offset, the new refs/tokens
pass unchecked — the guard silently narrows rather than reds. Guard recipe: add a
`docs/publishing/QUEUE-CONSISTENCY-MANIFEST.md` (or a `consistency:` block in the
SKU-REGISTRY the ENG-4/ENG-5 cards propose) declaring (a) which docs are "queue
companions" whose `§`/`D` refs must resolve, and (b) the recognised dated-offset token
grammars and their anchor rules; have
`check_owner_queue_staleness.py::check_companion_crossrefs` iterate the declared
companion list instead of the single `COMPANION_REL` constant, and
`check_checkpoint_consistency` load the offset grammars from the manifest; add a
`test_*` catch-case (manifest names a companion whose ref dangles → guard fires; a
companion NOT in the manifest → advisory, not red). That converts "which cross-refs and
dated tokens can go stale" from three script-local constants into a declared,
scaffold-visible contract the next artifact registers into.

## previous-session review

previous-session review: `.sessions/2026-07-19-eng4-funnel-asset-checker.md`
(PR #263, `f1ab8dc`) — added the REQUIRED `funnel-assets-guard` asserting every
shippable kit's `docs/launch/<sku>/` folder carries the full required funnel-asset set
(landing/sales copy + owner publish action), one level DOWN from ENG-5's
built-registered guard. Solid, honestly-scoped work: it inferred the required asset set
from the live tree (two naming conventions, role-satisfied-by-any-filename) rather than
assuming one, refused to invent launch copy to force a green (reported "no
missing-asset finding" plainly), and mirrored #262's job shape. I followed its three
best habits here: (1) reuse the upstream signal rather than re-derive it — ENG-4 reused
ENG-5's `dist/` BUILD_MARKER; I reused `derive_owner_queue`'s parser + `PROOFREAD_GATE_RE`
so this guard can never disagree with the generator it guards; (2) prove non-vacuity —
ENG-4's `test_live_tree_actually_saw_built_skus`; I added an `actually_applicable` test
per invariant so a future tree that quietly stops exercising one can't pass as a silent
skip; (3) report known-current-state truthfully — no staleness was found and none was
manufactured. One thing I'd carry forward from ENG-4's own 💡: it wanted a declared
funnel-asset manifest to replace hand-maintained filename lists; my 💡 above is the
same shape applied to cross-ref/dated-token conventions — the two should converge into
one repo-consistency manifest rather than three parallel per-guard ones.
