# venture-lab conventions

> **Status:** `binding` — seeded 2026-07-09 from the gen-2 blueprint
> (`menno420/fleet-manager` `docs/gen2-blueprint.md` §1/§2) + the fleet
> merge-authority policy (fleet-manager PR #10). **Repo conventions OVERRIDE
> harness defaults.** When a harness rule ("create PRs as draft", "wait for
> review", "only open a PR when asked") conflicts with this file, this file wins.

## PR state and merge authority (owner-merges model)

> **Merge is an OWNER action.** An agent seat opens the PR READY on a `claude/*`
> head and leaves it green; **the owner merges it.** Agent-side auto-merge
> arming and direct self-merge are classifier-DENIED from agent seats
> (**[Self-Approval]** / **[Merge Without Review]**) — never attempt either. The
> `auto-merge-enabler` workflow is slated for retirement in the wind-down; do
> not depend on any "it lands itself" automation. (`claude/*` is still the
> branch convention.)

1. **READY, never draft.** The harness "create as draft" default cost gen-1
   lanes hours of drafts sitting unmerged. Never open a draft PR.
2. **Open ready + green; the owner merges — never arm or self-merge.**
   Agent-side arming and direct self-merge are classifier-DENIED from agent
   seats (**[Self-Approval]** / **[Merge Without Review]** — denials on PRs
   #9/#15/#55; ledger wall in [`CAPABILITIES.md`](CAPABILITIES.md) append
   log, verbatims archived in [`PLATFORM-LIMITS.md`](PLATFORM-LIMITS.md)). The
   old fleet guidance ("arm at creation, in the checks-pending window", R5/R12;
   REST merge-on-green fallback, R8) is SUPERSEDED — both paths hit the wall.
   Do NOT arm auto-merge or merge from an agent seat: open the PR READY on a
   `claude/*` head, leave it green, and the owner merges it. Lanes never arm or
   merge their own PRs ([`current-state.md`](current-state.md)).
3. **Nothing waits for a review gate. Review is post-merge; veto = revert.**
   The owner merges on green (owner direction IS the review), then flag: add a
   row to [`review-queue.md`](review-queue.md) for anything a reviewer should
   re-check. A PR parked indefinitely "awaiting review" is a convention
   violation, not caution.
4. **Done-when for the agent is:** "PR open, READY, CI green" — a state the
   agent can reach on its own; the owner-merge that follows is the owner's step,
   not a blocker on the agent's turn.

## Git discipline

5. **Forward-only git:** no force-push, no history rewrites, no amending
   pushed commits.
6. **Claim before build:** one file per claim in [`../claims/`](../claims/)
   (see its README). First-declared + claim-filed wins shared-surface
   conflicts (fleet R10).

## Session discipline

7. **Heartbeat-before-work:** the first act of any session is a status/WIP
   commit (session card or `control/status.md` WIP line). A silent session is
   indistinguishable from a dead one, and the platform WILL sometimes make
   you silent for an hour.
8. **Walking skeleton first (session 1):** within the first 20 minutes of the
   lane's life, drive one trivial change through the merge path —
   branch → PR → CI green → **owner merges** — before any real work.
9. **Kit adoption is a session-1 duty:** substrate-kit adopted and `python3
   bootstrap.py check --strict` green **before any domain work**, and before
   every push thereafter.
10. **Session cards carry identity from card #1:** a `📊 Model:` line and a
    time line on every card — identity not written at the moment of work is
    unrecoverable (proven independently by 3 gen-1 lanes). Born-red
    `in-progress` as the FIRST commit, flipped `complete` as the deliberate
    LAST step.
11. **Timestamps from `date -u`**, never the model's sense of time — commit
    history is the clock of record.
12. **Standing ritual every session:** inbox at HEAD first → act → status
    last, with a final inbox re-read at HEAD before the closing status write.
    Full protocol: [`../control/README.md`](../control/README.md).

## Hard rails (mission-specific, non-negotiable)

13. **NO spend, NO account creation, NO publishing, NO payment flows without
    an explicit owner go.** Queue every such step click-level under
    ⚑ needs-owner (WHAT/WHERE/HOW/WHY/UNBLOCKS) — never perform it.
14. **Token-cost accounting per candidate** — every venture candidate carries
    a running cost line so return-on-agent-labor is measurable, not vibes.
15. **Distribution-first scoring** — every candidate names its
    first-ten-customers path or scores down automatically.
