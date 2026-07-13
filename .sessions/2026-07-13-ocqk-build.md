# Session — PRODUCTS build: Owner-Click Queue Kit (OCQK, $19) to publish-READY

> **Status:** `in-progress`

- **📊 Model:** Claude Fable (fable-5) · worker · PRODUCTS lane, build slice
- **session:** build the Owner-Click Queue Kit — the #2 BUILD verdict (3.60)
  from `docs/products/ideas-2026-07-13.md` §2 — to the ORDER 008
  publish-READY quality floor per `docs/products/TEMPLATE.md`: built +
  tested (parse/derive/lint suite incl. hostile inputs, wired into CI) +
  priced $19 + listing drafted + checkout/format verified (double rebuild,
  clean-dir unzip, tests from the extracted zip) + sha256 pinned + ⚑ owner
  click queued in a §7-parseable packet + OWNER-QUEUE regenerated + INTAKE
  kill-rule fields bound. No spend, no accounts, no external publish — the
  path ends at a queued owner click.
- **started (date -u):** Mon Jul 13 10:08:29 UTC 2026
- **completed (date -u):** in progress

## Scope

- `candidates/owner-click-queue-kit/` — the pack: `GRAMMAR.md` (generic
  owner-gate block grammar + six-field action-detail grammar), `ocq.py`
  (stdlib derive + strict lint), worked examples (agent-fleet + solo-repo,
  with committed expected outputs), test suite, `GOTCHAS.md` (production
  lessons), `INTAKE.md` (internal), allow-list `package.sh`, `dist/` zip.
- `docs/launch/owner-click-queue-kit/` — `listing-copy.md` +
  `owner-actions.md` (six-field click-script).
- `docs/publishing/vetting/owner-click-queue-kit.md` — §7-parseable packet
  (+ index row in `docs/publishing/README.md` for docs-gate reachability).
- `docs/publishing/OWNER-QUEUE.md` — regenerated (never hand-edited).
- `.github/workflows/kit-tests.yml` — one added job running the pack's
  suite (same convention as the GWTK job).
- `control/claims/2026-07-13-ocqk-build.md` — claim (deleted in the ender).
- This card (born-red first commit; flipped `complete` last).
- Does NOT touch `control/inbox.md`, `control/status.md`,
  `control/outbox.md`, any trigger, or the auto-merge enabler. Never arms
  or merges its own PR.

## Work log

- (in progress)
