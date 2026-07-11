# Session — kit upgrade v1.10.0 → v1.10.1

> **Status:** `in-progress`

- 📊 Model: fable-5
- **started (date -u):** 2026-07-11 09:34:14 UTC
- **scope:** kit-owned files only — vendored `bootstrap.py`, regenerated
  `.github/workflows/substrate-gate.yml`, `.substrate/` state, this card, and
  the `control/status.md` kit-heartbeat line in the flip commit.

## Purpose

Upgrade substrate-kit v1.10.0 → v1.10.1 (distribution wave, owner directive
Q-0261.3). v1.10.1 ships the session-gate `tail -1` multi-card shadowing fix —
the bug this repo's own PR #33 reopening demonstrated — plus the
emphasis-blind model-doctrine presence check. This repo therefore gets the
most explicit local verification of the tail-1 fix (per-added-card grading,
in-progress HOLD demonstrated with the regenerated checker).

## Log

- Born-red heartbeat: this card is the session's first commit; PR opens
  immediately after (in-flight signal). Flip to `complete` is the deliberate
  last step. This PR touches the gate workflow, so this ADDED card rides the
  FULL locked door (mid-PR gate-regen invariant).
