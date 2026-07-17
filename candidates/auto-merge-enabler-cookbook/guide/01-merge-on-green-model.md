# 1 · The merge-on-green model (who does the merging, and why it isn't your agent)

You have agents that open pull requests. You want those PRs to land on
`main` the moment they are green — no human clicking merge at 3am, no
queue of finished-but-unlanded work. The obvious approach is to have the
agent merge its own PR. That approach is wrong, and this chapter is about
the model that is right.

## The one idea

**The agent never merges. The agent never even arms auto-merge. A
repo-owned workflow does both, on the server, under its own token, gated
by a required check you control.**

That single sentence is the whole architecture. Everything else in this
cookbook is a consequence of it: how the workflow arms (chapter 2), what
"green" is allowed to mean (chapters 3-4), how a PR opts out (chapter 5),
why the agent is structurally barred from doing this itself (chapter 6),
and what breaks (chapter 7).

## Why not just let the agent merge?

Because in any serious agent stack it can't, and shouldn't. An agent that
approves and lands its own work defeats two-party review, and mature
policy layers deny exactly that — the source repo this cookbook is
distilled from records the denial as a hard classifier wall (chapter 6).
Retrying the merge through a different API path is denied again; arming
auto-merge *from the agent's own seat* is recognized as the same act and
denied too. The lesson the source fleet learned and wrote into its own
status doc:

> Agent seats are DENIED from arming auto-merge or self-merging their own
> (or a sibling's) PR (**[Self-Approval]** / **[Merge Without Review]**).
> … the sanctioned merger is the workflow, never the seat.

So the merging identity has to be something that is *not* the agent. There
are two such identities, and this cookbook is built around the first:

1. **GitHub's own native auto-merge**, armed by a repo-owned workflow —
   the primary path, the one running in production, the one this cookbook
   teaches. GitHub performs the squash; the workflow only *armed* it.
2. A repo-owned workflow that performs the merge itself via the REST API
   (a `GITHUB_TOKEN` merge-on-green job) — the fallback for repo shapes
   where the native arm is structurally refused. This cookbook points at
   it but does not center it, because the source repo lands via path 1.

## What "on green" actually means here

"Merge on green" is not "merge when CI passes and hope the PR was
finished." Green has to encode *finished*, or a pre-armed auto-merge lands
half-done work the instant CI reports. This cookbook's green is two things
at once:

- **The required check passes** — the gate is a *required* status context,
  so GitHub has something to wait for (chapter 3). Miss this and auto-merge
  either refuses to arm or merges instantly with no gate at all.
- **The session declares itself done** — the PR's own session journal has
  flipped from `in-progress` to `complete`, and the required gate holds the
  PR red until it does (chapter 4, the born-red HOLD).

When both are true the pre-armed auto-merge fires and the workflow's token
squash-merges the PR. In this repo, on the night this cookbook was written,
that is exactly what happened five times in a row.

## The proof this model runs

This is not a whiteboard model. On 2026-07-17 this repo's own
`auto-merge-enabler.yml` squash-merged five agent PRs on `main`, each
`merged_by: github-actions[bot]` (the workflow's token, not a human, not
the agent):

| PR | merge commit | merged_by |
|----|--------------|-----------|
| #219 | `389ab6e` | github-actions[bot] |
| #220 | `4e0a37c` | github-actions[bot] |
| #221 | `12498f4` | github-actions[bot] |
| #222 | `37cf9fd` | github-actions[bot] |
| #223 | `f0511ae` | github-actions[bot] |

PR #223 was **created 23:05:38Z and merged 23:06:26Z** — 48 seconds,
opened READY, auto-merged on green, no human in the loop. `merged_by:
github-actions[bot]` is the whole model made visible in the merge record:
the merging identity is the workflow's token, never the agent's seat.

The rest of this cookbook is how those five merges were made possible, one
mechanism at a time.

**Sources** (public repo `menno420/venture-lab`):
`docs/current-state.md` @ `4e0a37c` (the merge-classifier change; "the
sanctioned merger is the workflow, never the seat"; enabler currently
active, not retired); `.github/workflows/auto-merge-enabler.yml` @
`aa04700` (the live enabler); merge events verified via the GitHub API on
2026-07-17: PRs #219 (`389ab6e`), #220 (`4e0a37c`), #221 (`12498f4`),
#222 (`37cf9fd`), #223 (`f0511ae`), all `merged_by github-actions[bot]`;
PR #223 created 23:05:38Z, merged 23:06:26Z.
