# Session — substrate-kit upgrade v1.9.0 → v1.10.0

> **Status:** `complete`

- **📊 Model:** fable-5 · kit-upgrade distribution seat
- **session:** distribution-wave kit seat (Q-0261.3): upgrade substrate-kit
  1.9.0 → 1.10.0 via the sha256-verified release asset (tag v1.10.0 @
  1b5db16, release run 29142780212). Kit-owned files only — no domain
  work, no control/ edits beyond this card + claim.
- **started (date -u):** Sat Jul 11 2026 (born-red first commit)

## Scope

- Stage verified asset (`sha256 ba69fc5c…b5a4`) as `bootstrap.py.new` +
  `release.json` → single-invocation `python3 bootstrap.py.new upgrade
  --apply-docs` (v1.10.0 fixed the carve-out-section rewrite bug, so
  --apply-docs rides the upgrade directly this wave).
- Verify: (a) regenerated LIVE gate carries the `session-card-hold`
  locked-door lane for PR-added cards (old lane here was advisory —
  superbot-games #40 loophole class); (b) model-doctrine append to
  .sessions/README.md idempotent; (c) exactly one new backup bank
  bootstrap-1.9.0.py; (d) carve-out section intact after --apply-docs.
- `check --strict` + `check --simulate-added-card` exercised; kit-tests
  suites run locally.

## Work log

- Branch `claude/kit-upgrade-v1.10.0` cut from origin/main `9b504e8`
  (tree-verified: bootstrap.py:90 KIT_VERSION 1.9.0, state.json + config
  1.9.0, bootstrap.py sha256 `55181082…` == v1.9.0 dist bytes).
- Born-red card + `control/claims/` claim = FIRST commit `1e6e040`; PR #33
  opened immediately (in-flight signal).
- Asset re-downloaded + sha256-verified `ba69fc5c…b5a4` (== release.json ==
  wave 3-way value). Single-invocation `python3 bootstrap.py.new upgrade
  --apply-docs`: engine printed `verified: sha256 + version against
  release.json`, self-cleaned inputs. Payload commit `95a21bd`.
- Verifications: (a) LIVE gate regenerated — added-card lane flipped from
  the v1.9.0 "advisory sentinel gate" to "in-progress HOLDs until the card
  flips complete" (`session-card-hold`, engine ~13094/13110/13387, appended
  after the allowlist pass — never allowlistable); locked-door branch now
  runs `--simulate-added-card`; staged .substrate/ci/ copy byte-identical
  to live. (b) model-doctrine NO-OP: .sessions/README.md byte-identical
  (`cae82297…`, doctrine already embedded by the v1.9.0 regen). (c) exactly
  ONE new bank `bootstrap-1.9.0.py` (sha256 `55181082…` == pre-upgrade
  bootstrap.py); all four pre-existing banks byte-identical (hash-diffed).
  (d) carve-out section intact after --apply-docs: "carve-out scan:
  .github/workflows/substrate-gate.yml — ran, 0 found"; zero carve-outs →
  no pre-regen gate bank (correct).
- FIRST-EXERCISE (venture-lab = second live-gate repo this wave): HOLD DID
  engage — head `60e91f8` gate run 29144777017 / job 86524329059 FAILURE
  with the "HOLD (by design)" banner + `##[notice]` + the live
  `simulate-added-card … would HOLD (born-red …)` advisory line. Card-only
  first head `1e6e040` ran the OLD v1.9.0 gate → advisory lane → GREEN
  (run 29144666243): the superbot-games #40 loophole was open pre-regen.
- NEGATIVE FINDING (new, kit-side): the gate's single-card picker
  (`tail -1` over the diff) let head `798a3d0` go GREEN (run 29144734514)
  while the ADDED card was in-progress — the diff also modified
  `.sessions/session-001.md` (grammar backfill), which sorts last, so the
  gate graded the compliant sibling and the added card's hold was
  SHADOWED. Multi-card diffs grade only one card. Reproduced + evidenced
  in the run log ("session gate card: .sessions/session-001.md"). Kit idea
  below.
- Mtime-lottery sweep: all sibling cards grade exit 0 after a
  provenance-marked grammar backfill on `session-001.md` (missing 💡 +
  review needles; pre-doctrine card, no content fabricated).
- Tests: membership-kit server suites 35 OK; stripe-webhook-test-kit 14 OK
  (the two kit-tests.yml CI jobs, run locally). `check --strict` exit 0 at
  close-out; `check --simulate-added-card` exercised locally (advisory
  "would HOLD", exit 0).

## 💡 Session idea

Kit gate: grade EVERY session card in the PR diff, not `tail -1`. This
session proved a live shadowing loophole — an ADDED in-progress card
escapes the session-card-hold whenever the same PR also modifies an
alphabetically-later sibling card (here: a grammar backfill). The hold that
kit #176 shipped to close the superbot-games #40 class reopens through any
multi-card diff. Cheapest fix: loop the card list (added cards through the
added-card/locked-door lane, modified cards through the full gate) instead
of picking one.

## ⟲ Previous-session review

Previous-session review: the v1.9.0 upgrade session (PR #32) was clean and
its card is a model of citation density — this session reused its recipe
verbatim. What it could have done better: it recorded the
`--simulate-added-card` kit idea but could not exercise the added-card lane
it shipped; this session closed that observability gap live (first
venture-lab CI exercise of both the hold and the simulate line). Workflow
improvement surfaced by this session: sibling-card backfills must land
either before the PR opens or in the same commit that flips the own card
complete — landing one mid-PR shadows the added-card hold (see negative
finding above).

- **non-kit follow-ups (noted, not touched):** `control/status.md` `kit:`
  heartbeat line bump is lane-owed (one-writer rule); legacy root `claims/`
  dir still coexists with `control/claims/`; `session-001.md`'s 📊 Model
  value is a full-ish id (`claude-opus-4-8[1m]`) predating the family-level
  doctrine — left as-is (attribution ground truth, not mine to rewrite).
