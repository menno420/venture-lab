# Session — kit upgrade v1.11.0 → v1.12.0

> **Status:** `complete`

- 📊 Model: fable-5
- **started (date -u):** 2026-07-11 17:34:08 UTC
- **scope:** kit-owned files only — vendored `bootstrap.py`, `.substrate/`
  state, kit-owned planted docs, and this card. No `control/inbox.md` /
  `control/status.md` writes this session (hard scope, owner directive
  Q-0261.3; heartbeat bump is lane-owed, not this PR).

## Purpose

Upgrade substrate-kit v1.11.0 → v1.12.0 (distribution wave, owner directive
Q-0261.3). v1.12.0 ships: substantive auto-draft arrival (reflog evidence +
pointer carry-forward), planted-orientation boot-set trim (CLAUDE.md /
AGENT_ORIENTATION / CONSTITUTION template changes — regen diffs expected),
untouched-auto-draft advisory in the bare strict lane only (born-red HOLD
lanes byte-unchanged), and the carve-out scanner three-way compare (kit
#210 — first live exercise this wave; expect NO phantom carve-out on this
repo's live gate). This ADDED card rides the `--added-card` locked door
(born-red HOLD until the deliberate final flip).

## Log

- Born-red heartbeat: card + claim were the session's first commit
  (`cf47dcd`); PR #42 opened immediately after. Flip to `complete` is the
  deliberate last step.
- Preflight: origin/main had advanced past the wave-briefing snapshot
  (`a447f1a` → `c22922d`, routine PRs #39/#40) — re-verified all three tree
  stamps at 1.11.0 and pre-upgrade dist sha256 `c339bd6a…a29` at `c22922d`
  before branching.
- Upgrade commit `26c04ab`: canonical `bootstrap.py.new upgrade` with
  adjacent release.json; asset sha256 `77c00b81…e1f8` (689,586 bytes) and
  release.json own digest `617dca35…600` (449 bytes) verified before use;
  engine self-verified ("verified: sha256 + version against release.json")
  and self-cleaned both inputs. Then `upgrade --apply-docs` for the 2
  template-improved consumer-untouched docs.
- Claim-format fix mid-session: initial claim bullet lacked the backticked
  branch token / grammar shape; `check --strict` claims-format advisory
  caught it — rewritten per control/claims/README.md and re-verified clean.

## Verification record

- **Carve-out scan (three-way compare, kit #210 — first live-gate exercise
  on THIS repo, which carried a v1.11.0 phantom bank) — VERDICT: CLEAN.**
  Engine stdout verbatim:
  `upgrade: carve-out scan: .github/workflows/substrate-gate.yml — ran, 0 found`
  `upgrade: kept: .github/workflows/substrate-gate.yml (kit-owned, already current)`
  Report line verbatim: `- carve-out scan: .github/workflows/substrate-gate.yml — ran, 0 found`
  NO phantom carve-outs, NO new pre-regen bank (backup dir before/after:
  only the historical `substrate-gate.pre-regen-4f50eb4d.yml`, hash-identical
  `4f50eb4d…09b1c`). No `kit-updated N step(s)` line — the v1.12.0 gate
  template is unchanged from v1.11.0's regen, live gate byte-identical to
  the NEW staged `.substrate/ci/substrate-gate.yml` (diff empty), so the
  zero-flags/no-bank shape is correct. Same shape as gba-homebrew #49.
- **Live-gate regen diff:** NONE — `git diff` on
  `.github/workflows/substrate-gate.yml` empty; PR does not touch the gate.
- **Backup bank:** exactly one new archive
  `.substrate/backup/bootstrap-1.11.0.py`, sha256
  `c339bd6a2eb3a139dd0106d5fd3873eb2d067f79723fccb5781d4e72a74a8d29`
  == pre-upgrade dist == v1.11.0 release asset. All 7 pre-existing
  bootstrap banks + the pre-regen yml byte-identical before/after
  (`sha256sum -c` against pre-branch baseline); only
  `backup/last-upgrade.json` + `backup/state.json` rewritten by the engine
  as designed — PASS.
- **Version stamps:** bootstrap.py `KIT_VERSION = "1.12.0"`,
  `.substrate/state.json` 1.12.0, `substrate.config.json` 1.12.0; vendored
  dist sha256 `77c00b81…e1f8` == release asset — PASS.
- **Planted docs:** 2 template-improved + consumer-untouched
  (CONSTITUTION.md, docs/AGENT_ORIENTATION.md) applied via
  `upgrade --apply-docs` (boot-set trim / condensed program-law register);
  5 consumer-edited "template unchanged — consumer-owned, nothing to apply"
  (incl. control/inbox.md + control/status.md — untouched); 14 unchanged.
  Staged `.substrate/claude/CLAUDE.md` regen (three-surface boot set).
  Consumer-owned `.substrate/check-exceptions.yml` untouched. Carve-out
  section survived the `--apply-docs` report rewrite (kit #176 fix) — PASS.
- **Exact-pin grep:** zero functional `1.11.0` pins in tests/config
  (repo-wide grep excluding bootstrap.py/.substrate/.git/.sessions/control/
  → no hits) — nothing to bump — PASS.
- **Host CI suites local:** membership-kit server 35/35 OK
  (test_membership + test_http_realpath + test_supabase_store);
  stripe-webhook-test-kit 14/14 OK (test_http_realpath) — PASS.
- **HANDOFF discipline:** no HANDOFF.md present, none fabricated or
  committed — PASS.
- **Mid-session `check --strict`:** reported only the designed born-red
  HOLD (verbatim "HOLD (by design) … nothing to investigate") after the
  claims-format fix; final run after this flip must exit 0.
- **⚠ Kit follow-up (same finding as gba-homebrew #49, second repo this
  wave):** the new `docs/AGENT_ORIENTATION.md` template points its boot set
  (line 10) and verify block (line 34) at `.claude/CLAUDE.md` § sections —
  but venture-lab has NO live `.claude/CLAUDE.md` (staged
  `.substrate/claude/CLAUDE.md` only), so both pointers dangle. Not
  hand-patched (would diverge a kit-owned doc); reported to the wave
  coordinator for a kit-side fix.

## ⟲ Previous-session review

Previous-session review: the v1.11.0 upgrade session (PR #37) executed a
model wave pass and — critically — its manual byte-diff proof that the two
flagged "carve-outs" were the old template's own pins (banked
`pre-regen-4f50eb4d.yml` byte-identical to the pre-upgrade gate) is exactly
the evidence that fed kit #210's three-way compare, which this session
exercised live and confirmed fixed (0 found, no bank). Its 💡 idea became
shipped kit behavior within one release — the idea loop works. Workflow
improvement this session surfaces: the born-red card template's claim
bullet grammar isn't stated anywhere agent-visible at write time — I wrote
an unparseable claim and only the advisory caught it; the claims README
grammar line (backticked token + ISO date) belongs in the card/claim
skeleton the kit auto-drafts, so the bullet is born parseable instead of
advisory-corrected.

## 💡 Session idea

💡 Session idea: make the upgrade engine emit a one-line
`orientation-pointer check` after planting/applying docs — for each
`§`-style cross-reference a kit template writes (e.g.
`docs/AGENT_ORIENTATION.md` → `.claude/CLAUDE.md`), verify the target file
exists live in the adopter tree and print `pointer ok` /
`pointer dangling: <path> (staged-only)`. Two repos in this wave
(gba-homebrew, venture-lab) shipped kit-owned orientation docs whose boot
and verify pointers dangle because the repo has only the staged
`.substrate/claude/CLAUDE.md`; the engine already knows both the render
targets and the tree, so it can flag the dangle at plant time instead of
each adopter rediscovering it downstream.
