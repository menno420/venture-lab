# Session — Owner-gate lint backport: OCQK `lint` ported to production CI

> **Status:** `in-progress`

- **📊 Model:** Claude Fable (fable-5) · worker · PRODUCTS lane, dogfood-gap
  backport slice
- **session:** execute the OCQK build card's 💡 follow-up
  (`.sessions/2026-07-13-ocqk-build.md`, PR #153): port the kit's strict
  `lint` mode back into production as `scripts/lint_owner_gates.py` (per-file
  errors, exit 1, REAL calendar-date validation — the production regex
  accepts impossible dates like month 13 / day 32), add a stdlib test suite,
  and wire it into `kit-tests.yml` as an ADVISORY step
  (`continue-on-error: true`, the ledger-drift precedent). Fix the lax date
  regex in `scripts/derive_owner_queue.py` ONLY if byte-identical
  regeneration is proven. No spend, no accounts, no external publish.
- **started (date -u):** Mon Jul 13 11:52:28 UTC 2026
- **completed (date -u):** in progress

## Scope

- `scripts/lint_owner_gates.py` — NEW strict linter over the production
  owner-gate data (packet §7 blocks + keyword-map ⚑ OWNER conflicts).
- `scripts/test_lint_owner_gates.py` — NEW stdlib unittest suite.
- `scripts/derive_owner_queue.py` — date-validation fix ONLY with
  byte-identical before/after OWNER-QUEUE regeneration proof; reverted
  otherwise.
- `.github/workflows/kit-tests.yml` — one ADVISORY step
  (`continue-on-error: true`), mirroring the ledger-drift advisory job.
- `control/claims/2026-07-13-owner-gate-lint.md` — claim (deleted in the
  ender).
- This card (born-red first commit; flipped `complete` last).
- Does NOT touch `control/inbox.md`, `control/status.md`,
  `control/outbox.md`, any packet, `docs/publishing/OWNER-QUEUE.md`
  content, any trigger, or the auto-merge enabler. Never arms or merges
  its own PR.

## Work log

- (in progress)
