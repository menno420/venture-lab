# Auto-merge enabler — owner action (turn the canonical landing path live)

> **Status:** `historical`
>
> ⚠️ **RETIRING — the auto-merge apparatus is being wound down.** Agent seats no
> longer arm/self-merge (classifier-denied ~2026-07-15); the owner merges green
> PRs. Kept for reference only; the enabler workflow is slated for retirement at
> relaunch. See [`../conventions.md`](../conventions.md) /
> [`../current-state.md`](../current-state.md).

The substrate-kit auto-merge enabler workflow is now wired at
`.github/workflows/auto-merge-enabler.yml` (byte-identical to the kit-owned
staged copy `.substrate/ci/auto-merge-enabler.yml`). It arms GitHub-native
auto-merge on agent PRs so a born-red session PR **merges itself** the moment
the required check goes green — no per-PR merge click.

**The workflow is INERT until the owner sets two one-time repo settings below.**
A workflow cannot flip repo settings, so these are owner-only clicks. This is a
click-script for the owner, not a request to any agent — no agent performs the
settings changes, and no agent auto-publishes or force-merges.

## Owner-action row (six-field grammar)

- **WHAT:** turn on GitHub-native auto-merge for this repo and make
  `substrate-gate` a required status check on `main`, so the already-wired
  enabler workflow can arm agent PRs to self-land on green.
- **WHERE:** GitHub repo `menno420/venture-lab` → Settings (owner UI). Two
  panes: *General → Pull Requests*, and *Rules* (rulesets / branch protection).
- **HOW (steps):**
  1. Settings → **General** → *Pull Requests* → check **"Allow auto-merge"** = ON.
  2. Settings → **Rules** → add/edit a ruleset targeting the default branch
     `main` → **Require status checks to pass** → add the check named
     **`substrate-gate`** as a required context. (If a required check exists
     under a different name, pin the real name via
     `substrate.config.json → automerge.required_context` so the enabler logs
     and this checklist name the same context.)
  3. (Optional, recommended) Settings → General → **"Automatically delete head
     branches"** = ON, plus auto-update of PR branches — closes merged-branch
     clutter and the green-behind stall.
- **WHY:** green agent PRs self-land, removing the per-PR merge click from the
  loop; the required `substrate-gate` check stays the enforcement, so nothing
  merges red. This is the canonical landing path the fleet's born-red session
  PRs depend on.
- **UNBLOCKS:** every future green `claude/*` session PR merges itself with no
  owner click; removes the manual-merge bottleneck for the whole lane.
- **VERIFIED-WHEN:** the next green `claude/*` PR merges itself with no manual
  merge click — the enabler's "Enable native auto-merge (squash)" step logs
  `Auto-merge enabled for PR #N`, and the PR squash-merges automatically once
  `substrate-gate` reports green.

## Head convention — only `claude/*` branches get armed

The enabler's job filter arms **only** PR heads whose branch name starts with
`claude/` (`startsWith(github.head_ref, 'claude/')`). A PR from a differently
named branch installs no arm and must be merged by hand. Agent sessions must cut
their branches with the `claude/` prefix to get the self-landing behavior.

## Safety guards (why arming is safe)

The kit-owned workflow ships two guards, both live in
`.github/workflows/auto-merge-enabler.yml`:

1. **Refuse-to-arm on zero required contexts.** The first step counts the base
   branch's required status-check *contexts* and refuses to arm when the count
   is `0` (it emits a `::warning::` and every downstream step is gated on
   `steps.rules.outputs.required != '0'`). With no required check, arming would
   merge a PR *instantly* — this guard is why the two owner settings above must
   both be done; the required-check setting is not optional.
2. **`do-not-automerge` carve-out.** A PR labeled `do-not-automerge` is never
   armed — enforced both at the job `if:` (`!contains(... 'do-not-automerge')`)
   and by a fresh API re-read of the labels 15s after open (defeats the
   stale-payload label race). Add the label to any PR you want to hold for a
   manual merge.

## Secrets / env (NAMES only — never values)

- **`ROUTINE_PAT`** — *optional*. A user PAT (Contents + Pull requests write).
  When present the eventual merge attributes to a real user; otherwise the
  workflow falls back to the built-in `GITHUB_TOKEN`. Store as an Actions
  secret if you want real-user attribution. **Do not paste any token value into
  this repo or this doc.**
- **`GITHUB_TOKEN`** — the built-in Actions token, the automatic fallback. No
  setup required.
