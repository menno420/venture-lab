# Session — kit upgrade v1.10.1 → v1.11.0

> **Status:** `in-progress`

- 📊 Model: fable-5
- **started (date -u):** 2026-07-11 13:25:09 UTC
- **scope:** kit-owned files only — vendored `bootstrap.py`, regenerated
  `.github/workflows/substrate-gate.yml`, `.substrate/` state, and this card.
  No `control/` writes this session (heartbeat bump is lane-owed, not this PR).

## Purpose

Upgrade substrate-kit v1.10.1 → v1.11.0 (distribution wave, owner directive
Q-0261.3). v1.11.0 ships the HANDOFF composer (planted `.substrate/claude/
CLAUDE.md` read-first line + HANDOFF.md generation machinery) and bumps the
regenerated gate workflow action pins to `actions/checkout@v5` +
`actions/setup-python@v6`. This PR touches the live gate workflow, so this
ADDED card rides the FULL locked door (born-red HOLD until flip).

## Log

- Born-red heartbeat: this card is the session's first commit; PR opens
  immediately after (in-flight signal). Flip to `complete` is the deliberate
  last step.
