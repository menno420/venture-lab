# Session — ENG-8: docs-freshness + link/orphan checker

> **Status:** `in-progress`

- **📊 Model:** [[fill: model line at flip]]
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

## 💡 Session idea

[[fill: one genuine idea at flip]]

## previous-session review

[[fill: previous-session review at flip]]
