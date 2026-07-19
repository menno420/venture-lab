# Session — ENG-3: check_funnel_coverage.py — per-cluster funnel-top checker

> **Status:** `in-progress`

- **📊 Model:** [[fill: model · effort · task-class at flip]]
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

[[fill: one genuine 💡 idea at flip]]

## previous-session review

[[fill: one-line prev-session review acknowledging the #249–#255 baton at flip]]

## Work log

- 2026-07-19 — Branch `claude/eng-3-funnel-coverage-checker` from `origin/main`
  (`aaa3f26`, #255 HEAD); clean base confirmed. Born-red card committed (first
  commit), pushed. PR opened READY. Build begins.
