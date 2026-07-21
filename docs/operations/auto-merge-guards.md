# Auto-merge enabler — guards & the self-landing path

> **Status:** `historical`
>
> ⚠️ **RETIRING — reference only.** The owner is winding down the autonomy
> apparatus and the `auto-merge-enabler.yml` workflow is slated for retirement.
> **Correction:** merging is normal agent work — agents merge their own green
> PRs directly (MCP/REST) or via the enabler; the old "classifier-DENIED /
> the owner merges" framing was a false standing wall (superseded, proven by
> direct agent merges 2026-07-18). See [`../conventions.md`](../conventions.md) §
> "PR state and merge authority" and [`../current-state.md`](../current-state.md).
>
> This doc explains what the enabler did, the guards that made arming safe,
> which branches it armed, and the fallback for when GitHub refused the arm.

> **Branch-naming rule (read this first):** agent PR branches **MUST** use the
> `claude/` prefix to self-land. The enabler arms **only** heads matching
> `claude/*`; a PR from any other branch name (e.g. `money-seat-heartbeat`,
> `owner-launch-hour`) is never armed and must park READY + green for a
> non-author merge. See `docs/conventions.md` § "PR state and merge authority"
> for the binding form of this rule.

## What the enabler does

The substrate-kit auto-merge enabler lives at
`.github/workflows/auto-merge-enabler.yml` (KIT-OWNED — wired byte-identical
from `.substrate/ci/auto-merge-enabler.yml`; `bootstrap.py upgrade` regenerates
it in place, so hand edits are overwritten — put host customizations in a
separate workflow). It was installed by **PR #59** (merged
2026-07-11T23:55Z, squash `305646f`).

On `pull_request` events (`opened`, `reopened`, `ready_for_review`,
`synchronize`) it arms **GitHub-native squash auto-merge** on a READY agent PR,
server-side, at open. The PR then **self-lands the moment the required
`substrate-gate` check goes green** — no per-PR merge click. `synchronize`
re-arms on every push to the head, so a fix-push or a `git merge origin/main`
re-arms on the up-to-date head (arming is idempotent and never merges anything
itself — the required check stays the gate).

## The two guards (why arming is safe)

Both guards live in `.github/workflows/auto-merge-enabler.yml`:

1. **Refuse-to-arm on zero required contexts.** The first step counts the base
   branch's required status-check *contexts* (not rules — a
   `required_status_checks` rule with an empty context list still lets an armed
   PR merge with nothing to wait for) and **refuses to arm when the count is
   `0`**: it emits a `::warning::` and every downstream step is gated on
   `steps.rules.outputs.required != '0'`. With no required check, arming would
   merge a PR *instantly* — this guard inverts that failure mode into a safe
   no-op, and is why the required-check repo setting is not optional.

2. **`do-not-automerge` carve-out WITH a fresh re-read race guard.** A PR
   labeled `do-not-automerge` is never armed. This is enforced twice: at the
   job `if:` (`!contains(... 'do-not-automerge')`, which reads the *event
   payload* labels snapshotted at open), **and** by a second step that sleeps a
   grace beat (~15s) and **re-reads the PR's labels fresh from the API at HEAD**
   right before arming. The re-read defeats the stale-payload race: a label
   added in a second call just after PR-open (as an MCP-created PR does) is
   absent from the open-time payload but present on the fresh re-read, so it
   still blocks the arm. Add the label to hold any PR for a manual merge.

## Head-branch filter — `claude/*` only

The enabler's job `if:` includes `startsWith(github.head_ref, 'claude/')`, and
it also requires the PR to be from this repo (not a fork) and not a draft. The
practical consequence:

- **`claude/*` heads self-land** — armed at open, merged on green.
- **Any other head does NOT self-land.** Sessions cutting branches like
  `money-seat-heartbeat` or `owner-launch-hour` install no arm; their PRs must
  park **READY + green** and be merged by a manual / non-author action.

This is why every agent session must cut its branch with the `claude/` prefix.

## Verified-live state in venture-lab

Both repo settings the enabler depends on are **ON and verified live**:

- **"Allow auto-merge"** (Settings → General → Pull Requests) = ON.
- **`substrate-gate` required** as a status-check context on `main`
  (Settings → Rules).

**Proof:** PR #59 self-landed **24s after open** — armed by the enabler and
squash-merged by `github-actions[bot]`, with no human or agent merge click. That
is the `VERIFIED-WHEN` bar from `owner-action-auto-merge.md` met by a real
merge. This is the only claim stated as verified here; nothing beyond the
repo-settings-ON + one-PR-self-land fact is asserted.

## Fallback — when GitHub structurally refuses the arm

On some repo shapes GitHub will structurally refuse to arm native auto-merge
(e.g. a required check with no pending window, or a PR-required-but-no-CI
configuration). When that happens the enabler's arm step logs a `::warning::`
rather than merging. The landing path in that case:

- **Merge it directly on green.** REST/MCP squash-merge (`merge_pull_request`)
  is the standard path — merging your own green PR is normal agent work.
- **Or let a non-author session / the enabler land it.** Any of these is fine;
  never route a mergeable green PR to the owner.

## Secrets / env (NAMES only — never values)

- **`ROUTINE_PAT`** — *optional*. When present as an Actions secret, the merge
  attributes to a real user; otherwise the workflow falls back to the built-in
  `GITHUB_TOKEN`. Store a value only in GitHub Actions secrets — never paste any
  token value into this repo or this doc.

## See also

- `docs/operations/owner-action-auto-merge.md` — the six-field OWNER-ACTION
  click-script that turned the two repo settings on (written from the pre-
  settings INERT state; this doc records the now-verified-live outcome).
- `docs/conventions.md` § "PR state and merge authority" — the binding
  self-merge-grant + `claude/`-prefix rule.
