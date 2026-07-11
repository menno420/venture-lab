# Session — substrate-kit upgrade v1.8.0 → v1.9.0

> **Status:** `in-progress`

- **📊 Model:** claude-fable-5 · high · kit-upgrade
- **session:** distribution-wave kit seat (Q-0261.3): upgrade substrate-kit
  1.8.0 → 1.9.0 via the sha256-verified release asset (tag v1.9.0, release
  run 29139623697). Kit-owned files only — no domain work, no control/
  edits beyond this card + claim.
- **started (date -u):** Sat Jul 11 2026 (born-red first commit)

## Scope

- Stage verified asset as `bootstrap.py.new` + `release.json` → `python3
  bootstrap.py.new upgrade` (engine self-verifies sha256+version,
  self-cleans inputs).
- Verify v1.9.0 payload: `.ignore` + `.gitattributes` plants, SessionStart
  handoff-push, model-attribution doctrine in `.sessions/README.md`,
  explicit carve-out section in `.substrate/upgrade-report.md`, exactly one
  new backup bank (`bootstrap-1.8.0.py`), live substrate-gate.yml regen.
- `python3 bootstrap.py check --strict` exit 0 + kit-tests suites green
  locally before push.
- NOT running `upgrade --apply-docs` (known kit bug: rewrites
  upgrade-report.md without the carve-out section — websites wave finding).

## Work log

- (in progress)
