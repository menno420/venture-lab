# Session — substrate-kit upgrade v1.9.0 → v1.10.0

> **Status:** `in-progress`

- **📊 Model:** fable-5 · kit-upgrade distribution seat
- **session:** distribution-wave kit seat (Q-0261.3): upgrade substrate-kit
  1.9.0 → 1.10.0 via the sha256-verified release asset (tag v1.10.0 @
  1b5db16, release run 29142780212). Kit-owned files only — no domain
  work, no control/ edits beyond this card + claim.
- **started (date -u):** Sat Jul 11 2026 (born-red first commit)

## Scope

- Stage verified asset (`sha256 ba69fc5c…b5a4`) as `bootstrap.py.new` +
  `release.json` → single-invocation `python3 bootstrap.py.new upgrade
  --apply-docs` (v1.10.0 fixed the carve-out-section rewrite bug, so
  --apply-docs rides the upgrade directly this wave).
- Verify: (a) regenerated LIVE gate carries the `session-card-hold`
  locked-door lane for PR-added cards (old lane here was advisory —
  superbot-games #40 loophole class); (b) model-doctrine append to
  .sessions/README.md idempotent; (c) exactly one new backup bank
  bootstrap-1.9.0.py; (d) carve-out section intact after --apply-docs.
- `check --strict` + `check --simulate-added-card` exercised; kit-tests
  suites run locally.

## Work log

- (in progress)
