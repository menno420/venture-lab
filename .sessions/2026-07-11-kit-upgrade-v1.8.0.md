# Session — substrate-kit upgrade v1.7.1 → v1.8.0

> **Status:** `in-progress`

- **📊 Model:** claude-fable-5 · kit-upgrade distribution wave
- **session:** kit-upgrade v1.8.0 (distribution worker, kit wave)
- **started (date -u):** Sat Jul 11 01:19:26 UTC 2026

## Purpose

Upgrade the vendored substrate-kit from v1.7.1 to the published v1.8.0
release (tag `v1.8.0` @ `63c6b39`, release asset sha256
`28c5dcb64b713dde8d64a513a9a1aa860b4a07bf17d832686f0009932dc89b9b`): place
the pinned release assets, run `bootstrap.py.new upgrade`, verify the v1.8.0
payload (control/claims/ plant, scripts/env-setup.sh plant, staged
auto-merge enabler, gate regen + carve-out scan, single-dist backup),
perform the report-prescribed manual merge for the one `diverged` doc
(`control/README.md`), verify `python3 bootstrap.py check --strict` green,
and land only kit-owned changes. Scope is the kit upgrade only — no domain
work, no `control/inbox.md` / `control/status.md` writes (the lane's own
next heartbeat updates the `kit:` line).
