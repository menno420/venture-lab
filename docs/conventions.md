# venture-lab conventions

> **Status:** `binding` — seeded 2026-07-09 from the gen-2 blueprint
> (`menno420/fleet-manager` `docs/gen2-blueprint.md` §1/§2) + the fleet
> merge-authority policy (fleet-manager PR #10). **Repo conventions OVERRIDE
> harness defaults.** When a harness rule ("create PRs as draft", "wait for
> review", "only open a PR when asked") conflicts with this file, this file wins.

## PR state and merge authority (the self-merge grant)

> **Branch naming — MUST `claude/`-prefix to self-land.** Agent PR branches
> MUST use the `claude/` prefix to self-land (see
> [`operations/auto-merge-guards.md`](operations/auto-merge-guards.md)). The
> auto-merge enabler arms **only** `claude/*` heads; a differently-named branch
> (e.g. `money-seat-heartbeat`) is never armed and must park READY + green for a
> non-author merge.

1. **READY, never draft.** The harness "create as draft" default cost gen-1
   lanes hours of drafts sitting unmerged. Never open a draft PR.
2. **This lane ALWAYS lands its own PRs — written grant, enabler-executed.**
   The `auto-merge-enabler` workflow
   (`.github/workflows/auto-merge-enabler.yml`, installed PR #59) arms squash
   auto-merge on every non-draft `claude/*` PR — that is THE self-merge path.
   Agent-side arming and direct self-merge are classifier-DENIED from agent
   seats (**[Self-Approval]** / **[Merge Without Review]** — denials on PRs
   #9/#15/#55; ledger wall in [`CAPABILITIES.md`](CAPABILITIES.md) append
   log, verbatims archived in [`PLATFORM-LIMITS.md`](PLATFORM-LIMITS.md)).
   The old fleet guidance ("arm at creation, in the checks-pending window",
   R5/R12; REST merge-on-green fallback, R8) is SUPERSEDED here — both paths
   hit the same wall. Do NOT arm auto-merge or merge from an agent seat:
   open the PR READY on a `claude/*` head, leave it green, and the enabler
   lands it. Lanes never arm or merge their own PRs
   ([`current-state.md`](current-state.md), stability baseline).
3. **Nothing waits for review. Review is post-merge; veto = revert.** PRs
   merge on green (the enabler lands them), then flag: add a row to
   [`review-queue.md`](review-queue.md) for anything a reviewer should
   re-check, and/or @-mention Codex on the PR for post-merge review. A PR
   parked "awaiting review" is a convention violation, not caution.
4. **Done-when is agent-reachable:** "PR open, READY, CI green — the enabler
   lands it" — never a state only a human can produce.

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
   lane's life, drive one trivial change through the FULL merge path —
   branch → PR → CI → auto-merge lands it — before any real work.
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
