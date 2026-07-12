# Session — Auto-merge guards reference doc + branch-naming convention

> **Status:** `complete`

- **📊 Model:** opus-4.8 · high · auto-merge-guards-doc
- **session:** write venture-lab's OWN `docs/operations/auto-merge-guards.md` —
  what the enabler does, its two guards (refuse-to-arm on zero required
  contexts; `do-not-automerge` carve-out with a fresh re-read race guard), the
  `claude/*` head filter, the VERIFIED-LIVE state (both repo settings ON, proven
  by PR #59 self-landing), and the structural-refusal fallback — plus one
  prominent branch-naming line so sessions cut `claude/`-prefixed heads.
- **started (date -u):** Sun Jul 12 00:17 UTC 2026 (born-red first commit)

## ⟲ Previous-session review

Previous-session review: the last landed work on `main` is PR #59 (squash
`305646f`, "Install auto-merge enabler (canonical landing path)"), which wired
the kit-owned enabler into `.github/workflows/auto-merge-enabler.yml` and shipped
the six-field OWNER-ACTION doc `docs/operations/owner-action-auto-merge.md`. That
install left the enabler's own warning message pointing at
`docs/operations/auto-merge-guards.md` — a doc that does not yet exist on `main`.
This slice fills that dangling reference with venture-lab's own guards reference
and records the now-verified-live repo-settings state (the owner-action doc still
describes the pre-settings INERT state). No prior guards doc exists to regress.

## 💡 Session idea

Do NOT copy the trading-strategy sibling doc verbatim — that lane's version
documents the still-INERT, settings-not-yet-flipped state, whereas venture-lab's
settings are already ON and PROVEN live by PR #59 self-landing. venture-lab's doc
must therefore lead with VERIFIED-LIVE state, not owner-guidance. The
branch-naming convention line lands in `docs/conventions.md` (project-owned,
`Status: binding`, already the home of the "PR state and merge authority
(self-merge grant)" rules) — NOT in `.substrate/claude/CLAUDE.md`, which is
kit-owned and regenerated on `bootstrap.py upgrade` (a hand edit there is
overwritten). Secret NAMES only (`ROUTINE_PAT`), never a value; never arm or
merge my own PR.

## Scope

- Add `docs/operations/auto-merge-guards.md` (venture-lab's own voice, VERIFIED-
  LIVE state, two guards + `claude/*` filter + structural-refusal fallback).
- Add one prominent branch-naming line to `docs/conventions.md`, cross-linking
  the new guards doc.
- Born-red card first; flip to `complete` before opening the PR;
  `python3 bootstrap.py check --strict` green before push.
- Do NOT touch `control/`, `candidates/`, launch docs, PRs #57/#58/#51.

## Work log

- (born-red) card committed first; branch `claude/auto-merge-guards-doc` cut from
  `origin/main` at `305646f`.
- Wrote `docs/operations/auto-merge-guards.md` in venture-lab's own voice —
  `verified-live` status (NOT the sibling lane's INERT `owner-guidance` state):
  what the enabler does, the two guards (refuse-to-arm on zero required contexts;
  `do-not-automerge` carve-out with the fresh ~15s API re-read race guard), the
  `claude/*`-only head filter, the VERIFIED-LIVE repo-settings state proven by
  PR #59 self-landing 24s after open (armed by the enabler, merged by
  `github-actions[bot]`), and the structural-refusal fallback (park READY+green;
  owner/non-author merges; never self-merge). Secret NAME `ROUTINE_PAT` only.
- Placed the branch-naming convention line at the TOP of `docs/conventions.md`
  § "PR state and merge authority (the self-merge grant)" — the binding,
  project-owned home of the self-merge rules — cross-linking the guards doc.
  Chose `conventions.md` over `.substrate/claude/CLAUDE.md` because the latter is
  kit-owned and regenerated on `bootstrap.py upgrade` (a hand edit is lost).
- Flipped this card `complete` as the deliberate last step before the PR;
  `python3 bootstrap.py check --strict --session-log <this card>` green at flip.
