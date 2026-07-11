# Session — kit upgrade v1.10.0 → v1.10.1

> **Status:** `complete`

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
- Regen commit `ab58488`: canonical `bootstrap.py.new upgrade` with adjacent
  release.json; asset sha256 `fbe83ce3…` verified before use. KIT_VERSION
  1.10.0 → 1.10.1 in-tree.

## Verification record

- **Backup bank:** exactly one new archive `.substrate/backup/bootstrap-1.10.0.py`
  (sha256 `ba69fc5cf21619cc85e4c733ebe3d9eda8803e678f810fcc39b94d60c2f3b5a4`);
  all five pre-existing banks byte-identical before/after — PASS.
- **Carve-outs:** scan ran, 0 found; host-owned `kit-tests.yml` untouched — PASS.
- **Doctrine:** `.sessions/README.md` byte-identical pre/post, doctrine phrase
  present exactly once (no duplicate append) — PASS.
- **Regenerated gate:** grades EVERY card in the diff — added cards loop with
  `|| fail=1` (any added in-progress card HOLDs), siblings modified alongside
  an added card are advisory-only, modified-only diffs keep the locked door
  per card, gate-touching PRs run the full locked door per added card — PASS.
- **Tail-1 shadowing demo (local, regenerated checker):** two fixture cards
  (never committed) — earlier-sorting `aa…` in-progress + tail-later `zz…`
  complete. Old `tail -1` emulation picked only the `zz…` card → exit 0
  (GREEN; the demonstrated PR #33 shadow). New per-card loop: `aa…` card →
  exit 1 `[session-card-hold] born-red HOLD`; `zz…` card → exit 0; overall
  verdict fail=1 → HOLD. Fixtures deleted after; guard-fires.jsonl retains
  the HOLD evidence — PASS.
- **Host CI suites local:** membership-kit 35/35 OK; stripe-webhook-test-kit
  14/14 OK — PASS.
- **Stale-pin grep:** no `1.10.0` references outside kit-owned/history files.

## ⟲ Previous-session review

Previous-session review: the v1.10.0 upgrade session (PR #33) executed the
canonical recipe cleanly and its sibling grammar backfill was properly
provenance-marked — but its reopening is where the tail-1 multi-card
shadowing was demonstrated, which this payload fixes. Workflow improvement:
that demonstration → kit fix → distribution loop worked exactly as designed;
the improvement this session adds is the local per-card demo pattern
(fixture cards + old-picker emulation vs new loop) as a cheap template for
verifying gate-semantics fixes in future waves.

## 💡 Session idea

💡 Session idea: venture-lab's `control/status.md` had no `kit:` heartbeat
line at all before this session (the wave brief assumes one exists to bump).
Worth adding a kit-side check — `check --strict` warning when
`control/status.md` lacks a `kit: v<version>` line matching the in-tree
KIT_VERSION — so heartbeat drift (6 repos owed bumps after the v1.10.0 wave)
becomes machine-visible instead of relying on distribution-session diligence.
