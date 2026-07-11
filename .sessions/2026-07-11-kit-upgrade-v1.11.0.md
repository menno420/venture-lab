# Session — kit upgrade v1.10.1 → v1.11.0

> **Status:** `complete`

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

- Born-red heartbeat: this card is the session's first commit (`d99140c`);
  PR #37 opened immediately after. Flip to `complete` is the deliberate
  last step.
- Upgrade commit `c5d1293`: canonical `bootstrap.py.new upgrade` with
  adjacent release.json; asset sha256 `c339bd6a…` (673,937 bytes) and
  release.json sha256 `a8c7ddc1…` (449 bytes) verified before use.
  kit_version 1.10.1 → 1.11.0 in-tree; inputs self-cleaned.

## Verification record

- **HANDOFF plant:** `.substrate/claude/CLAUDE.md` line 16 carries the
  HANDOFF.md read-first line; no host-owned live `CLAUDE.md` /
  `.claude/CLAUDE.md` exists in this repo — PASS.
- **HANDOFF composer in dist:** `grep -c HANDOFF bootstrap.py` = 28;
  `HANDOFF_POINTER_FILENAME` / `HANDOFF_POINTER_MARKER` constants at
  ~bootstrap.py:4885; `git check-ignore HANDOFF.md` exits 1; no HANDOFF.md
  created or committed — PASS.
- **Backup bank:** exactly one new archive `.substrate/backup/bootstrap-1.10.1.py`
  (sha256 `fbe83ce35d1fb3b544ac58fc60ee2609eaa6c69c13d77883e9fdc5da6bbad158`);
  all six pre-existing banks byte-identical before/after — PASS.
- **Carve-outs:** scan flagged 2 "host-added" steps (`checkout@v4`,
  `setup-python@v5`) + banked `.substrate/backup/substrate-gate.pre-regen-4f50eb4d.yml`.
  This is the known false-positive class (gba-homebrew #44, same wave): the
  flagged steps are the OLD template's own pins, re-read as host additions
  because the new template bumps them. Verified: the banked file is
  byte-identical to both the pre-upgrade live gate and the pre-upgrade staged
  `.substrate/ci/substrate-gate.yml` (sha256 `4f50eb4d…`) — zero genuine host
  additions; bank committed for audit — PASS (false positive confirmed).
- **Regenerated gate:** live `.github/workflows/substrate-gate.yml` pins
  `actions/checkout@v5` (line 21) and `actions/setup-python@v6` (line 80);
  live file byte-identical to staged `.substrate/ci/substrate-gate.yml` — PASS.
- **guard-fires dedupe:** `check --strict` twice back-to-back mid-session:
  run 1 appended 1 line (12 → 13, the designed born-red HOLD), run 2
  appended 0 (13 → 13) — 10-min dedupe works — PASS.
- **Version stamp:** `substrate.config.json` kit_version `1.11.0`; vendored
  `bootstrap.py` sha256 == release asset `c339bd6a…` — PASS.
- **Host CI suites local:** membership-kit 35/35 OK; stripe-webhook-test-kit
  14/14 OK — PASS.
- **Final `check --strict`:** exit 0 after this flip (mid-session runs
  correctly reported the designed HOLD).

## ⟲ Previous-session review

Previous-session review: the v1.10.1 upgrade session (PR #34) was a model
wave execution — its local tail-1 shadowing demo (fixture cards vs old
picker emulation) was verification beyond the checklist, and its 💡 idea
(machine-check the `kit:` heartbeat line against KIT_VERSION) is exactly the
drift class this session had to tiptoe around again. Workflow improvement:
its card scoped the heartbeat bump into its own flip commit; this wave's
brief made the bump lane-owed instead — the split-writer rule should be
stated in the card scope line every wave (done here) so parallel sessions
never race on `control/status.md`.

## 💡 Session idea

💡 Session idea: teach the upgrade carve-out scanner to diff flagged
"host-added" steps against the OLD template's own step list before
reporting — when a flagged step exists verbatim in the previous template
(the pin-bump case seen here and in gba-homebrew #44), it is a template
delta, not a host addition, and should be reported as "pin bump (no action
needed)" instead of a ⚠️ carve-out demanding a host-ci.yml move. Two repos
in one wave paid a manual byte-diff verification for the same false
positive; the scanner has both templates in hand and could classify it
itself.
