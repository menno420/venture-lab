# Session — substrate-kit upgrade v1.6.0 → v1.7.0

> **Status:** `in-progress`

- **📊 Model:** claude-fable-5 · kit-upgrade distribution wave
- **session:** kit-upgrade v1.7.0 (distribution worker, kit wave)
- **started (date -u):** Fri Jul 10 20:24:14 UTC 2026

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
