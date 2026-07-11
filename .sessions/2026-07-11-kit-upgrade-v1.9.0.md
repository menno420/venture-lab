# Session — substrate-kit upgrade v1.8.0 → v1.9.0

> **Status:** `complete`

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
- Verify v1.9.0 payload; `check --strict` + kit-tests suites green.
- NOT running `upgrade --apply-docs` (known kit bug: rewrites
  upgrade-report.md without the carve-out section — websites wave finding).

## Work log

- Branch `claude/kit-upgrade-v1.9.0` cut from origin/main `0ad0ea4`
  (tree-verified kit_version 1.8.0 in substrate.config.json).
- Born-red card + `control/claims/` claim = FIRST commit `242d2aa`; PR #32
  opened immediately (in-flight signal).
- Asset re-verified sha256 `55181082…` before staging; engine printed
  `verified: sha256 + version against release.json` and self-cleaned inputs.
- Payload commit `3f6ab80`: bootstrap.py 1.8.0 → 1.9.0; exactly ONE new
  backup bank `bootstrap-1.8.0.py` (sha256 `28c5dcb6…`), all 3 pre-existing
  banks byte-identical (hash-verified before/after); `.ignore` +
  `.gitattributes` fresh plants (both absent pre-upgrade, 2 entries each
  under the append-only provenance marker); SessionStart handoff-push
  verified live (`hook sessionstart` prints the Handoff section + newest
  card + status); explicit carve-out section in `.substrate/
  upgrade-report.md` (`carve-out scan: .github/workflows/substrate-gate.yml
  — ran, 0 found`; no pre-regen bank — correct, conditional on carve-outs);
  live gate regen delta = exactly the v1.9.0 `--added-card` grammar-lint
  lane.
- `.sessions/README.md` was `kept:` by the engine (consumer-owned); diff vs
  the v1.9.0 compose showed the sole delta was the template's own stale
  paragraph 1 (old marker list, no doctrine), paragraphs 2–3 byte-identical
  → zero host-only content → ⚑ self-initiated: regenerated from the v1.9.0
  compose so the model-attribution doctrine + byte-form needles are present.
- kit-tests suites green locally: membership-kit server 35 tests OK,
  stripe-webhook-test-kit real-path 14 tests OK.
- First exercise: live gate printed the #156 locked-door line + the v1.9.0
  `HOLD (by design)` notice + the Actions `##[notice]` annotation on the
  payload commit (run 29141148135, job 86514481872) — designed hold, PR
  adds a card AND touches the gate file. No `automerge.required_context`
  advisory — correct silence, this repo's gate job IS named
  `substrate-gate`.
- `--apply-docs` NOT run; staged template-improved docs remain lane-owed
  (`.substrate/claude/CLAUDE.md` among the staged copies). Guard recipe for
  whoever runs it: `upgrade --apply-docs` rewrites
  `.substrate/upgrade-report.md` WITHOUT the carve-out section (websites
  wave, kit-lane bug) — hand-restore the section after running, verify with
  `grep -n "Carve-out scan" .substrate/upgrade-report.md`.

## 💡 Session idea

The added-card grammar-lint lane this upgrade ships can never be observed
live by the PR that ships it (the locked door routes the added card through
the full gate instead — gba-homebrew + venture-lab both hit this). Kit
idea: a `check --strict --simulate-added-card <card>` local mode that runs
exactly the advisory-sentinel lane, so a distribution session can verify
the lint it just installed without waiting for the next unrelated PR.

## ⟲ Previous-session review

Previous-session review: PR #31 (order-005 model-attribution close-out) did
its one job cleanly — a single-line family-level Model addition where the
template was already present — and merged green. What it left: the
`.sessions/README.md` paragraph it relied on was still the pre-doctrine
template output (no byte-form needles), so the convention it recorded lived
only in the card, not the README cold sessions actually read; this upgrade
closes that gap by regenerating the README from the v1.9.0 compose.
Workflow improvement carried: order close-outs that touch attribution
should also check the doctrine surface (.sessions/README.md) they depend
on, not just the card.

- **non-kit follow-ups (noted, not touched):** `control/status.md` `kit:`
  heartbeat line bump is lane-owed; legacy root `claims/` dir still
  coexists with `control/claims/` (claims-legacy-location nudge class).
