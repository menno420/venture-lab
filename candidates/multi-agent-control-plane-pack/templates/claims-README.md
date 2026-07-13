# control/claims/ — claim before build, one file per claim

> One file per claim is structurally conflict-free (a shared-append
> claim list measured ~98% merge-conflict under concurrency; per-file
> measured 0%). The rule that preserves the 0%: **no hand-edited
> shared index** — discover claims with `ls control/claims/`; this
> README never lists them.

## How to use it

1. **Before starting work**, scan this directory AND the open PRs.
   Already claimed or in flight → coordinate or pick something else.
2. **Create one claim file** — `control/claims/<branch-or-scope>.md` —
   with a single bullet:
   `` - `branch-or-scope` · **scope** — one-line detail · expected files/area · YYYY-MM-DD ``
   (Keep the backticks around the branch/scope token and the ISO date —
   they are the anchors any checker parses.)
3. **Land the claim fast**, then re-read this directory at HEAD before
   you build: if both lanes do this, the second claimer always sees
   the first.
4. **Delete your own claim file at session close.** The durable record
   is the PR — a claim is a whiteboard note, not an audit trail.

## Arbitration + expiry

- **First claim merged wins** a collision; the loser deletes its file
  and stands down.
- **Claims expire:** older than ~72h with no visible build activity =
  abandoned — prune on sight.

## Not for orders

An inbox ORDER is claimed on your OWN heartbeat's `orders:` line,
never here. This directory is for **work** — anything two parallel
sessions could both pick up that isn't an ORDER id.
