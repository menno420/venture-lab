# Session — check_catalog_drefs.py guard + test: machine-catch OWNER-QUEUE renumber mispointing (the #245 class)

> **Status:** `in-progress`

- **📊 Model:** [[fill: family-level model · effort · task-class at flip]]
- **started (date -u):** Sat Jul 18 23:07 UTC 2026
- **branch:** `claude/dref-regression-guard`
- **base:** `main@cde8f6d`
- **purpose:** tonight PR #244 folded the CORS Preflight Test Kit into
  `docs/publishing/OWNER-QUEUE.md` as a new **D4**, renumbering every
  alphabetically-later decision +1 (D4→D5 … D27→D28). That silently MISPOINTED
  the D-ref cross-references in the sellable-bundle + catalog docs (owner would
  land on the wrong queue row); PR #245 hand-resynced them. The green checker
  (`bootstrap.py check --strict`) did NOT catch it — a D-ref is a SEMANTIC
  cross-reference, not a syntax error — so the regression shipped green. This
  slice adds a GUARD so the class is caught automatically the next time
  OWNER-QUEUE renumbers. (Directly builds the 💡 logged on the #245
  bundle-dref-resync card and the #244 owner-queue-cors-fold card.)
- **deliverable:** `scripts/check_catalog_drefs.py` — builds the live
  decision-ID → SKU map from OWNER-QUEUE.md §1 `### D<n> — <SKU>` headers (the
  source of truth), then scans an ALLOWLIST of live-cross-ref files and asserts
  each `D<n>` (a) resolves to an EXISTING decision and (b) points at the SKU the
  surrounding context names. Exit non-zero with a per-ref message on any
  dangling / mispointed ref, exit 0 clean. Stdlib-only.
  `scripts/test_check_catalog_drefs.py` — pass-case on the current clean tree +
  catch-case on a temp fixture with a deliberately-wrong D-ref (proves the guard
  fires, not just that it is green) + dangling-case + historical-exclusion case.
  Wired into `.github/workflows/kit-tests.yml`.
- **scope + exclusions (allowlist-based, not deny-all):** the allowlist = the
  files carrying LIVE cross-refs — `docs/launch/CATALOG.md`, the two bundle
  families (`docs/launch/{api-robustness,webhook-verifier}-bundle/*.md`,
  `docs/publishing/vetting/{api-robustness,webhook-verifier}-bundle.md`,
  `candidates/{api-robustness,webhook-verifier}-bundle/*.{md,json}`). Frozen
  point-in-time snapshots are HISTORY and deliberately NOT in the allowlist
  (`.sessions/*`, `control/inbox.md`/`outbox.md`, `docs/NEXT-TASKS.md`,
  `docs/NEXT-SESSION.md`, `docs/current-state.md`'s "N decisions D1-Dn" line);
  plus in-file renumber-arrow (`D4→D5`) and decision-range (`D1–D28`) lines are
  skipped as migration/summary prose, not per-SKU cross-refs.
- **guardrails:** no packet/queue edited (OWNER-QUEUE is the authority — read
  only). Diff is scripts/ + test + the one kit-tests CI job + claim + this card +
  a control/status.md heartbeat only. No publish/spend/account action. Born-red
  card holds substrate-gate red until the completion flip.

## 💡 Session idea

[[fill: one 💡 idea at flip]]

## previous-session review

[[fill: one-line prev-session review remark at flip]]

## Work log

- 2026-07-18 — Branch `claude/dref-regression-guard` from `origin/main`
  (`cde8f6d`); collision check clean (no `control/claims/` entry for a D-ref
  guard; the #245 card only PROPOSED it as a 💡, never built it). Claim +
  born-red card committed (first commit), pushed. Build begins.
