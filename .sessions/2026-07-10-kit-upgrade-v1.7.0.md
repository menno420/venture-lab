# Session — substrate-kit upgrade v1.6.0 → v1.7.0

> **Status:** `complete`

- **📊 Model:** claude-fable-5 · kit-upgrade distribution wave
- **session:** kit-upgrade v1.7.0 (distribution worker, kit wave)
- **started (date -u):** Fri Jul 10 20:24:14 UTC 2026
- **completed (date -u):** Fri Jul 10 20:26:52 UTC 2026
- Delivered: substrate-kit v1.6.0 → v1.7.0 (pinned release asset,
  sha256-verified); `check --strict` green on the upgraded tree.

## Purpose

Upgrade the vendored substrate-kit from v1.6.0 to the published v1.7.0 release
(tag `93c7bdb`, release asset sha256
`00f4f4cd39351b17389b9abab3be88fcb0c9f4dee9ad8f1639ad1fc67fdb5238`): download
the pinned release assets, run `bootstrap.py.new upgrade` (without
`--apply-docs` — no prior upgrade precedent in this repo; template-improved doc
rows are the lane's decision to take later), verify `python3 bootstrap.py check
--strict` green, and land only kit-owned changes. Scope is the kit upgrade
only — no domain work, no `control/inbox.md` / `control/status.md` writes (the
lane's own next heartbeat updates the `kit:` line).

## Log

- Synced to `origin/main` @ `af11bdb`; vendored header confirmed v1.6.0.
- Downloaded both v1.7.0 release assets; `bootstrap.py.new` sha256 matched the
  pin `00f4f4cd39351b17389b9abab3be88fcb0c9f4dee9ad8f1639ad1fc67fdb5238`;
  engine self-verified against `release.json` before archiving.
- `python3 bootstrap.py.new upgrade` (no `--apply-docs`): planted docs
  classified consumer-edited 3 · diverged 1 · unchanged 15 ·
  template-improved 0 — nothing `--apply-docs` would have applied this
  release. The one `diverged` doc is `control/README.md` (template gained the
  `adopt --lane <name>` shared-repo paragraph); manual-merge note is in
  `.substrate/upgrade-report.md`, left for the lane (never auto-applied).
- Vendored `bootstrap.py` now v1.7.0; `substrate.config.json` pin `1.7.0`;
  staged `.substrate/` artifacts regenerated; rollback banked under
  `.substrate/backup/` (`last-upgrade.json` → `bootstrap-1.6.0.py`).
- Known/expected: v1.7.0 does NOT regenerate the installed
  `.github/workflows/substrate-gate.yml` (kit PR #130 ships next release);
  only the staged copy `.substrate/ci/substrate-gate.yml` refreshed.
- `python3 bootstrap.py check --strict` → exit 0 (with this card complete).
- Out of scope, untouched: `control/inbox.md`, `control/status.md` (ORDER 004
  status re-stamp + the `kit: v1.7.0` heartbeat line belong to the lane's own
  next boot session).

## 💡 Session idea

💡 The upgrade engine names the banked rollback dist by *from*-version
(`bootstrap-1.6.0.py`) but also writes a `bootstrap-1.7.0.py` copy next to it.
A one-line `README.md` in `.substrate/backup/` explaining which file
`--rollback` restores (it's whatever `last-upgrade.json` points at) would stop
a future session from "cleaning up" the wrong archive — cheap guard, kit-side
template candidate.

## ⟲ Previous-session review

⟲ previous-session review: the kit-adoption session (2026-07-10) left an
exemplary trail — its card recorded the exact vendored-source path, the
`check --strict` CI-mode invocation, and the control-file preservation
verification, which made this upgrade's precedent check (no `--apply-docs`
history, gate shape, born-red flow) a two-minute read instead of PR
archaeology. Improvement it surfaces: the adoption card pinned the kit
*version* but not the dist *sha256*; recording the hash at adopt time would
have let this upgrade verify the outgoing artifact too, not just the incoming
one.
