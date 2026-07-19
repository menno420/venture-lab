# Session — ENG-3: check_funnel_coverage.py — per-cluster funnel-top checker

> **Status:** `complete`

- **📊 Model:** opus-4.8 · high · feature build
- **started (date -u):** Sun Jul 19 00:19 UTC 2026
- **branch:** `claude/eng-3-funnel-coverage-checker`
- **base:** `main@aaa3f26`
- **purpose:** land ENG-3 from the veto-ready menu (#247) — a stdlib checker
  that reads `docs/launch/CATALOG.md` §"Cross-sell clusters" and **advisory-warns**
  on any cross-sell cluster that carries a singles/bundle list but has NO linked
  `*-lead-magnet.md` funnel-top. Today "which cluster still needs a lead magnet"
  is a manual CATALOG read (the exact question the LM-1/LM-2 membership +
  AI-Novella magnets, #250/#251, were built to answer); this turns it into a
  standing greppable signal. Builds the 💡 logged on the PR #246 agent-ops
  card and the sibling per-KIT ENG-4 idea; natural sibling of the D-ref guard
  (#248, `catalog-dref-guard`) — that checks cross-ref *resolution*, this checks
  funnel *coverage*.
- **deliverable:** `scripts/check_funnel_coverage.py` — parses the Cross-sell
  clusters section into `**<Name> cluster:**` bullets that carry a singles/bundle
  list (arrow-joined SKUs), derives distinctive keywords per cluster, and marks a
  cluster COVERED when its keywords overlap a coverage source: either a Cross-sell
  bullet that **links** a `*-lead-magnet.md` funnel-top, or an existing
  `docs/launch/*-lead-magnet.md` file (slug + H1). Advisory-only: prints one line
  per cluster and ALWAYS exits 0 (like `check_ledger_drift.py`).
  `scripts/test_check_funnel_coverage.py` — pass-case on the live tree (all
  clusters covered → no warning) + catch-case on a temp fixture with an uncovered
  cluster (warning fires) + a covered-cluster fixture (no warning). Wired into
  `.github/workflows/kit-tests.yml` as an ADVISORY-ONLY `continue-on-error` job
  (the `ledger-drift-advisory` shape), NEVER a required gate — it must never
  exit-fail another in-flight PR's substrate/kit gate.
- **scope (files):** NEW `scripts/check_funnel_coverage.py`,
  `scripts/test_check_funnel_coverage.py`; EDIT `.github/workflows/kit-tests.yml`
  (one new advisory job). No CATALOG / packet / OWNER-QUEUE edit — the checker is
  read-only over the launch docs. Diff is scripts/ + test + the one advisory CI
  job + this card + a `control/status.md` heartbeat only. No SKU, no publish
  surface, no OWNER-QUEUE row; the seat performs no publish/spend/account action.
- **guardrails:** ADVISORY-ONLY by contract — exits 0 on every path AND wired
  `continue-on-error`, so it can never red another PR's gate. Cluster list is
  grounded in the ACTUAL CATALOG content (no hardcoded clusters). Born-red card
  holds substrate-gate red until the completion flip.

## 💡 Session idea

💡 **Fold ENG-3 (per-cluster) and ENG-4 (per-KIT) into one
`check_funnel_coverage.py` with two advisories, and add a THIRD advisory that
flags a `*-lead-magnet.md` file with NO cluster to serve — the reverse gap.**
This checker answers "which cluster lacks a magnet"; the sibling ENG-4 idea (PR
#243 card) answers "which shipped KIT's intake names no funnel-top". Both read
the same launch docs and share the keyword-overlap machinery already here, so
one module with `--per-cluster` / `--per-kit` (default: both) avoids a second
CATALOG parser drifting out of sync with this one. The reverse gap is worth a
line too: today the coverage relation is checked one direction only — a cluster
without a magnet warns, but an ORPHAN magnet (a `docs/launch/foo-lead-magnet.md`
whose keywords overlap NO cross-sell cluster — e.g. a magnet written for a
cluster later renamed or dropped from CATALOG) is silent, so a funnel-top can
rot pointing at nothing. Recipe: reuse `coverage_sources()` and `find_clusters()`
and emit `orphan-magnet: foo-lead-magnet.md — no cross-sell cluster it serves`
when a magnet file's keyword set intersects zero cluster keyword sets. Same
advisory-only contract (exit 0, `continue-on-error`); it composes with the D-ref
guard (#248, resolution) and the DIST-9 bundle-unlock-order 💡 (#255, ordering)
into a launch-doc integrity family — resolution · ordering · coverage.

## previous-session review

previous-session review: this slice mechanizes the exact coverage question the
distribution-first #249–#255 baton answered by hand. #249's
`DISTRIBUTION-PLAYBOOK.md` templated the funnel-top recipe; #250 (membership) and
#251 (AI-Novella) filled the last two uncovered clusters one at a time — each PR
had to MANUALLY read CATALOG to decide which cluster was next. #252/#253 pre-chewed
the live-SKU T+7/T+14 call and #254/#255 refreshed the ledger and pre-EAP plan.
ENG-3 turns "which cluster still needs a magnet" from that recurring manual read
into a standing signal, and it CONFIRMS the baton's work landed: run on the live
tree, all four cross-sell clusters (Webhook, API-robustness, Membership,
Agent-ops) resolve to a linked funnel-top → zero warnings, so the membership +
AI-Novella gaps #250/#251 closed genuinely read as closed, not just as claimed.
The one thing I'd flag forward: this checks the cluster→magnet direction only —
an orphan magnet is still silent (the 💡 above is the reverse-gap fix).

## Work log

- 2026-07-19 — Branch `claude/eng-3-funnel-coverage-checker` from `origin/main`
  (`aaa3f26`, #255 HEAD); clean base confirmed. Born-red card committed (first
  commit `aa5bcc6`), pushed. PR #256 opened READY. Build begins.
- 2026-07-19 — Built the checker: `scripts/check_funnel_coverage.py` (stdlib-only;
  parses CATALOG §"Cross-sell clusters" → `**<Name> cluster:**` bullets with a
  SKU list; keyword-overlap coverage against section funnel-top rows that link a
  magnet + the `docs/launch/*-lead-magnet.md` files; advisory — exits 0 on every
  path) + `scripts/test_check_funnel_coverage.py` (live-tree green case +
  uncovered-fixture catch-case + covered-via-file case, 5 tests) + an
  advisory-only `funnel-coverage-advisory` `continue-on-error` job in
  `.github/workflows/kit-tests.yml`. Checker on the clean tree: EXIT 0, 4/4
  clusters (Webhook, API-robustness, Membership, Agent-ops) COVERED, 0 uncovered.
  Committed (`0a4a455`), pushed. Diff verified to carry only scripts/ + test + the
  one advisory CI job.
- 2026-07-19 — Heartbeat: neutral in-flight pointer for PR #256 added to
  `control/status.md` (other sections + `control/inbox.md` untouched). Committed
  (`d1c87ab`), pushed.
- 2026-07-19 — `python3 bootstrap.py check --strict` pre-flip = the born-red HOLD
  only (in-progress Status + 3 unresolved `[[fill:]]` slots); all non-hold checks
  pass, advisories (seat-digest, model-line payload, guard-fire telemetry) are
  non-gating and pre-existing. `python3 -m unittest test_check_funnel_coverage -v`
  = 5 tests OK.
- 2026-07-19 — Flip to `complete` (this commit): Status badge, 📊 Model line
  (family-level `opus-4.8`), one 💡 idea, previous-session review acknowledging
  the #249–#255 baton, all `[[fill:]]` slots resolved, guard-fire ledger delta
  committed. Re-ran `bootstrap.py check --strict` EXIT 0 (advisories only). Born-red
  HOLD clears; last commit releases auto-merge.
