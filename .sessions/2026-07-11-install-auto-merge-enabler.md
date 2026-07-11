# Session — Install the substrate-kit auto-merge enabler (canonical landing path)

> **Status:** `complete`

- **📊 Model:** opus-4.8 · high · install-auto-merge-enabler
- **session:** wire the staged, kit-owned auto-merge enabler workflow
  (`.substrate/ci/auto-merge-enabler.yml`) into `.github/workflows/` byte-identical
  and ship the six-field OWNER-ACTION doc that turns it live, so a green agent PR
  self-lands instead of waiting on a per-PR merge click.
- **started (date -u):** Sat Jul 11 23:45 UTC 2026 (born-red first commit)

## ⟲ Previous-session review

Previous-session review: the last landed work on `main` was the substrate-kit
v1.12.1 upgrade (PR #56, squash `296a1a9`), which is where this branch is cut
from. That upgrade staged the enabler at `.substrate/ci/auto-merge-enabler.yml`
but did NOT wire it into `.github/workflows/` — the workflows dir still holds only
`kit-tests.yml` + `substrate-gate.yml`, so agent PRs still require a manual merge
click. No prior enabler install exists to regress; this slice is the first wire.

## 💡 Session idea

The enabler is kit-owned and regenerated on every `bootstrap.py upgrade`, so the
install must copy it BYTE-IDENTICAL (verify by `diff` + matching `sha256sum`) and
never hand-edit the workflow. The enabler's job filter only arms heads matching
`claude/*` — hence this branch uses the `claude/` prefix (a differently-named head
would install the file but never exercise the arm). The workflow ships two safety
guards (refuse-to-arm when the base requires zero status-check contexts; skip PRs
labeled `do-not-automerge`), so it is INERT until the owner performs two one-time
repo settings — documented in the accompanying six-field OWNER-ACTION doc.

## Scope

- Wire `.substrate/ci/auto-merge-enabler.yml` → `.github/workflows/auto-merge-enabler.yml`
  byte-identical (kit-owned content untouched).
- Add `docs/operations/owner-action-auto-merge.md` (six-field grammar, secret
  NAMES only — never values).
- Born-red card first; `python3 bootstrap.py check --strict` green before push.
- Do NOT touch `control/`, `candidates/`, launch docs, or open PRs (#57/#58/#51).

## Work log

- Branch `claude/install-auto-merge-enabler` cut from `origin/main` at `296a1a9`.
- Tried `python3 bootstrap.py adopt --wire-enforcement` first; it did MORE than
  wire the enabler (planted `.claude/CLAUDE.md` + `.claude/settings.json`,
  re-staged the `.substrate/` skill/agent/hook packs, wrote
  `.substrate/backup/bootstrap-1.12.1.py`, bumped `.substrate/state.json`).
  Reverted every extra change and wired the enabler MANUALLY instead:
  `cp .substrate/ci/auto-merge-enabler.yml .github/workflows/auto-merge-enabler.yml`
  — keeps this a single enabler-wire PR with zero kit-owned collateral.
- Verified byte-identical: `diff` empty; both files sha256
  `64f9db4122c69631ab01d097a4f46ff49eac5d5d42728429e27543c45fc64c84`.
- Confirmed both safety guards live in the workflow: (a) the "Refuse to arm
  unless the base branch requires status CONTEXTS" step refuses on a `0`
  context count (downstream steps gated on `steps.rules.outputs.required != '0'`);
  (b) `do-not-automerge` carve-out at the job `if:` plus a fresh-API label
  re-read. Referenced secret NAME: `ROUTINE_PAT` (optional; `GITHUB_TOKEN`
  fallback) — name only, no value anywhere.
- Wrote `docs/operations/owner-action-auto-merge.md` (six-field grammar); linked
  it from the read-path root `docs/current-state.md` so it is not an orphan.
- `python3 bootstrap.py check --strict --session-log <this card>` green at flip.

