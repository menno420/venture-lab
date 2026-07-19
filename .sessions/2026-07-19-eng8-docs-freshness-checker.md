# Session — ENG-8: docs-freshness + link/orphan checker

> **Status:** `complete`

![status](https://img.shields.io/badge/status-complete-brightgreen)

- **📊 Model:** Claude Opus (4.x family) · high · test writing
- **started (date -u):** Sun Jul 19 09:15 UTC 2026
- **branch:** `claude/eng8-docs-freshness-checker`
- **base:** `main@82059bf` (post #261 ENG-6 / #262 ENG-5 / #263 ENG-4 / #264 ENG-7)
- **purpose:** implement roadmap item **ENG-8** — the docs-freshness + link/orphan
  checker (= OPS-5 + OPS-6, `docs/ideas/2026-07-19-execution-roadmap.md` line 83 +
  veto-menu §ENG-8 line 456). This is the FINAL slice of the ENG-4→ENG-8
  pipeline-safety lane. The roadmap frames it as "cheap `docs/` hygiene; keeps the
  ledger honest for a fresh seat."
- **what the existing gate ALREADY covers (so this does NOT duplicate it):**
  `bootstrap.py` ships a generic doc-hygiene gate (`engine/checks/check_docs.py`, run
  by `python3 bootstrap.py check --strict`) that, **over `docs/` only**, enforces
  three checks: **badge** (every non-ADR `docs/**/*.md` carries a `> **Status:**`
  token), **link** (every relative markdown link resolves to an existing file — but
  it `.split("#", 1)[0]`s the fragment, so it **never verifies `#anchor`s**), and
  **reachable** (orphan: every live doc reachable from a read-path root / README).
  OPS-6's dead-link + orphan idea is therefore ALREADY GATED for `docs/`; OPS-5's
  "stamped docs lagging main HEAD" freshness rule was **intentionally left out** of
  the port (it needs git/wall-clock, which is banned here as non-deterministic).
- **the GAP this guard fills (two invariants — deterministic, offline, stdlib-only):**
  - **INV-1 dead-link in the UN-GATED living-doc set:** every relative markdown link
    in the repo-doc surface the docs-gate never sees — repo-root `*.md`
    (`README.md`, `CONSTITUTION.md`, `.session-journal.md`) + `control/**/*.md` —
    resolves to an existing file. These are exactly the control-plane / fresh-seat
    boot docs, and today NOTHING link-checks them.
  - **INV-2 anchor-fragment resolution (the dimension the docs-gate strips):** for
    every markdown link carrying a `#anchor` into an existing markdown file — across
    root + `control/` **and** `docs/` — the fragment must resolve to a real heading
    (GitHub-style slug, with duplicate `-N` disambiguation and fenced-code skipping).
    The docs-gate drops every `#anchor`, so a link that points at the right FILE but
    a MOVED/renamed heading passes it silently; INV-2 catches that. `docs/` is in
    scope for anchors ONLY — its link-existence + orphan checks stay owned by the
    bootstrap gate (no duplication).
- **scope / exclusions (documented):** in-scope = tracked `*.md` under repo-root +
  `control/` + `docs/`. EXCLUDED, each with reason: `.sessions/` (immutable
  point-in-time session cards — append-only history, they legitimately cite files
  later moved/renamed, e.g. two dangling refs to `capabilities.md`), `candidates/`
  (generated kit/template packs whose relative links resolve in the GENERATED kit
  layout, not this repo — e.g. a template's `claims/README.md`), `.substrate/`
  (machine-generated telemetry JSONL, not prose). ORPHAN/reachability is deliberately
  NOT re-implemented: it is already gated for `docs/`, and root/`control/` have no
  README-graph reachability convention to gate — extending orphan there would invent
  policy, so it is out of scope (reported, not papered over).
- **known-current-state (reported + FIXED, not papered over):** the tree was almost
  clean. INV-1 — **0** broken relative links in root/`control/`. INV-2 — **1** genuine
  broken anchor: `docs/launch/DISTRIBUTION-PLAYBOOK.md:72` the `[§2]` self-link
  pointed at `#2-copy-paste-skeleton-for-a-new-cluster-lead-magnetmd`, but the real
  heading `## 2. Copy-paste skeleton for a new \`docs/launch/<cluster>-lead-magnet.md\``
  slugs to `#2-copy-paste-skeleton-for-a-new-docslaunchcluster-lead-magnetmd` (the
  hand-written link dropped the `docs/launch/` code-span text). FIXED reversibly by
  correcting the link fragment to the real heading slug — the owner's own `§2`
  cross-reference now actually jumps to section 2. This is precisely the class the
  docs-gate can never catch (it strips fragments). No target file/heading was
  invented; nothing deleted.
- **scope (files):** NEW `scripts/check_docs_links.py` (guard, stdlib-only, exit 0
  clean / non-zero with an itemized per-finding list, `--root` for fixtures), NEW
  `scripts/test_check_docs_links.py` (unittest: live-tree green + non-vacuity +
  synthetic broken-link / broken-anchor / duplicate-heading / fenced-code / exclusion
  / skip cases), CI wiring in `.github/workflows/kit-tests.yml` (new REQUIRED
  `docs-links-guard` job mirroring `owner-queue-staleness-guard`), the one
  `DISTRIBUTION-PLAYBOOK.md` anchor fix, plus the claim and this card.
- **verify:** `python3 scripts/check_docs_links.py` (exit 0 on the live tree, after
  the one fix) · `cd scripts && python3 -m unittest test_check_docs_links -v` ·
  `python3 bootstrap.py check --strict` (exit 0, advisories only).

## Work log

- 2026-07-19T09:15Z — Branch `claude/eng8-docs-freshness-checker` from origin/main
  (`82059bf`, post #261/#262/#263/#264). Read the ENG-8 spec of record (roadmap line
  83 + veto-menu §ENG-8), the bootstrap docs-gate (`engine/checks/check_docs.py` —
  badge/link/reachable, and confirmed it strips `#anchor`s), the docs/ structure +
  index READMEs, and the ENG-4/5/6/7 guards + their CI jobs this mirrors. Measured
  the tree offline: `docs/` (gated) is link/orphan-clean, and the only breakage
  repo-wide is 2 dangling refs in `.sessions/` cards, 1 in a `candidates/` template
  (both excluded with reason), and 1 genuine broken anchor in `docs/launch/`. Claim +
  this born-red card committed. Build begins.
- 2026-07-19T09:2xZ — **Build.** Added `scripts/check_docs_links.py` (INV-1 dead-link
  over root/`control/`; INV-2 `#anchor` resolution across root + `control/` + `docs/`
  via a GitHub-style slug with duplicate `-N` disambiguation + fenced-code skipping;
  exit 0 clean / 1 with an itemized finding list; `--root` for fixtures;
  `stats` counts so the test proves non-vacuity) + `scripts/test_check_docs_links.py`
  (20 tests: live-tree-green + non-vacuity + INV-1 catch/pass, docs/-not-relink-checked,
  external-skipped, INV-2 same-file/cross-file catch/pass, anchor-checked-inside-docs,
  duplicate-heading, fenced-code, exclusion of `.sessions`/`candidates`/`.substrate`,
  skip, end-to-end nonzero, and a slugify unit). Fixed the one genuine finding —
  `docs/launch/DISTRIBUTION-PLAYBOOK.md:72` `[§2]` anchor now points at the real
  heading slug. Wired a new REQUIRED `docs-links-guard` job into
  `.github/workflows/kit-tests.yml` (checker on the live tree + unittest), mirroring
  `owner-queue-staleness-guard` (#264). YAML validated (23 jobs).
- 2026-07-19T09:2xZ — **Verification.** Checker EXIT 0 on the live tree (200 in-scope
  docs, 27 links + 32 anchors checked — non-vacuous). `python3 -m unittest
  test_check_docs_links -v` 20/20 OK. `python3 bootstrap.py check --strict` EXIT 1
  ONLY on the born-red HOLD (card in-progress) — no finding from this slice; reverted
  the local `.substrate/guard-fires.jsonl` telemetry append. No target file/heading
  invented; nothing deleted.
- 2026-07-19T09:2xZ — Flip to `complete` (this commit): Status badge, 📊 Model line
  (family-level, task-class `test writing`), one 💡 idea, previous-session review, all
  `[[fill:]]` slots resolved. Born-red HOLD clears → `check --strict` returns EXIT 0.
  This is the FINAL slice of the ENG-4→ENG-8 pipeline-safety lane.

## 💡 Session idea

💡 **The ENG-4→ENG-8 pipeline-safety lane is now complete — promote the four disjoint
per-guard SCOPE constants into ONE declared `repo-consistency manifest` so the next
guard registers into a contract instead of hard-coding its own file set.** ENG-8 closes
the lane (ENG-6 idempotence, ENG-5 built-vs-registered, ENG-4 funnel-assets, ENG-7
queue-staleness, ENG-8 doc links/anchors). But each guard now owns a private,
script-local answer to "which files am I responsible for": ENG-8 hard-codes
`EXCLUDED_TOP = {.sessions, candidates, .substrate}` and `DOCS_GATE_ROOT = "docs"`;
ENG-7 hard-codes `COMPANION_REL`; ENG-4/ENG-5 hard-code their SKU roots. The seams that
divide "gated by bootstrap" from "gated by scripts/" from "deliberately un-gated" are
invisible until a reader greps five files — and the moment a NEW top-level doc dir
appears (say `playbooks/`), it silently falls into NO guard's scope, exactly the
orphan-class ENG-8 exists to prevent, one level up. Guard recipe: add
`control/repo-consistency-manifest.md` (or a `consistency:` block in the SKU-REGISTRY
the ENG-4/5/7 💡s already propose) declaring, per guard, its in-scope roots + documented
exclusions; have `check_docs_links.py::scope_files` read `EXCLUDED_TOP`/`DOCS_GATE_ROOT`
from it, and add a meta-guard test asserting every tracked top-level dir is claimed by
exactly one guard OR listed as a reasoned exclusion — so "what is unguarded" becomes a
declared, reviewable fact rather than an emergent gap. Natural next backlog pick after
the lane: **MISC-1 fresh-seat boot hardening** (roadmap Tier A2) — it wants the repo
"clean enough that a fresh seat boots from the repo alone", and this manifest is the
artifact that makes that literally checkable.

## previous-session review

previous-session review: `.sessions/2026-07-19-eng7-owner-queue-staleness-checker.md`
(PR #264, `82059bf`) — added the REQUIRED `owner-queue-staleness-guard` asserting three
deterministic, OFFLINE consistency invariants over the generated `OWNER-QUEUE.md` and
its #260 companion (companion cross-ref resolution, dated-checkpoint structure/arithmetic,
proofread-gate integrity), the internal-inconsistency class ENG-6's idempotence guard
cannot catch. Exemplary, honestly-scoped work, and I followed its three best habits
directly: (1) **reuse the upstream so the guard can't drift** — ENG-7 imported
`derive_owner_queue`'s own parser + `PROOFREAD_GATE_RE`; I mirrored the bootstrap gate's
OWN `_link_target`/`_split_target` normalisation and slug convention so my guard reasons
about links the same way the substrate does, and I explicitly deferred `docs/`
link-existence back to that gate rather than re-deriving it; (2) **prove non-vacuity** —
ENG-7 added an `actually_applicable` test per invariant; I return `stats` counts and
assert the live run checked >0 links AND >0 anchors, so a future tree that quietly stops
exercising a dimension can't pass as a silent skip; (3) **report + fix known-current-state
truthfully** — ENG-7 found no staleness and manufactured none; I found exactly one real
broken anchor, FIXED it reversibly (corrected the link to the real heading), and reported
the excluded `.sessions`/`candidates` dangling refs with reasons rather than silently
scoping them away. ENG-7's own 💡 asked for a declared queue-consistency manifest to
replace its script-local constants; my 💡 above is the same shape generalised across all
five lane guards — they should converge into one repo-consistency manifest, not five
parallel per-guard ones. That convergence is the lane's natural capstone.
