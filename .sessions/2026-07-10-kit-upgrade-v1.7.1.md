# Session — substrate-kit upgrade v1.7.0 → v1.7.1

> **Status:** `in-progress`

- **📊 Model:** claude-fable-5 · kit-upgrade distribution wave
- **session:** kit-upgrade v1.7.1 (distribution worker, kit wave)
- **started (date -u):** Fri Jul 10 22:00:26 UTC 2026

## Purpose

Upgrade the vendored substrate-kit from v1.7.0 to the published v1.7.1 release
(tag `1cbd666`, release asset sha256
`2aa4feddf7de7e20b00f46866826985ca8fd11f40bc51ebe261bbdef3118486d`): place the
pinned release assets, run `bootstrap.py.new upgrade`, verify the v1.7.1
payload (live + staged gate regen, carve-out report, single-dist backup,
`--inbox-base` wiring), verify `python3 bootstrap.py check --strict` green,
and land only kit-owned changes. Scope is the kit upgrade only — no domain
work, no `control/inbox.md` / `control/status.md` writes (the lane's own next
heartbeat updates the `kit:` line).
