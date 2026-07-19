# Session — ENG-7: owner-queue staleness checker

> **Status:** `in-progress`

- **📊 Model:** [[fill: model line at close-out]]
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

## 💡 Session idea

[[fill: one genuine session idea at close-out]]

## previous-session review

[[fill: previous-session review at close-out]]
