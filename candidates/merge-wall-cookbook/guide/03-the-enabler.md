# 3 · Recipe 1: the auto-merge enabler (the production landing path)

`recipes/auto-merge-enabler.yml` is the primary pattern: a repo-owned
workflow that **arms** native auto-merge on every eligible agent PR at
open, so the PR merges itself the moment the required gate goes green. The
agent never merges; the agent never even arms. It just pushes and opens.

## This one is not a hypothetical

The recipe is adapted (near-verbatim; the gate name and secret name are
generalized) from the workflow live in the source repo at
`.github/workflows/auto-merge-enabler.yml` @ `305646f`. On the night this
cookbook was assembled — 2026-07-13, one night — that workflow landed 13
agent PRs on `main`. Two you can verify from the public API in one call
each:

- **PR #104** — merged `2026-07-13T00:56:20Z`, `merged_by:
  github-actions[bot]`, head branch `claude/order-003-stripe-path`.
- **PR #128** — merged `2026-07-13T02:46:46Z`, `merged_by:
  github-actions[bot]`, head branch `claude/night-queue-killcheck` —
  23 seconds after the PR was created, which is what a pre-armed merge
  looks like when the gate rides its fast lane (chapter 5).

`merged_by: github-actions[bot]` is the whole trick, visible in the merge
record: the merging identity is the workflow's token, not the agent.

## Why each guard exists

**Arm on `synchronize` too.** Arming is idempotent and never merges
anything itself, so the enabler re-arms on every push to the PR head. This
narrows the green-behind stall: a fix-push after a red run re-arms on the
up-to-date head without anyone remembering to.

**Refuse to arm on zero required contexts.** Chapter 2's trap, inverted
into a guard: with no required check, arming merges instantly, so the
enabler counts required contexts and refuses on zero rather than becoming
the hole in its own gate.

**Label carve-out, re-read fresh.** `do-not-automerge` on the PR means
never armed — but the event payload snapshots labels at open time, and
API-driven agents typically add labels in a second call right after
create. The production workflow waits a grace beat and re-reads the labels
from the API before arming; its comment records the incident class that
taught it ("the kit #22 incident class" — a stale payload arming an
opted-out PR).

**Scope the arm.** Same-repo heads only, non-draft only, agent branch
namespace only (`claude/*` in production — change it to yours). You are
building a landing strip for your fleet, not for every fork on the
internet.

**Prefer a PAT, fall back to `GITHUB_TOKEN`.** The production file's
comment states the reason: a PAT attributes the eventual merge to a real
user. The fallback works — the #104/#128 merges above are
`github-actions[bot]` doing exactly that.

## Failure mode it cannot fix

If the arm itself is structurally refused — a required check already red
at arm time with no pending window (chapter 4's born-red gate creates
exactly that shape on card-only PRs), or a PR-required-but-no-CI repo —
the enabler's own failure message points at the fallback: REST
merge-on-green, chapter 7.

**Sources** (public repo `menno420/venture-lab`):
`.github/workflows/auto-merge-enabler.yml` @ `305646f` (the live workflow,
all guards + comments cited above); merge events verified via the GitHub
API on 2026-07-13: PR #104 (`merged_at 2026-07-13T00:56:20Z`) and PR #128
(`merged_at 2026-07-13T02:46:46Z`), both `merged_by github-actions[bot]`.
