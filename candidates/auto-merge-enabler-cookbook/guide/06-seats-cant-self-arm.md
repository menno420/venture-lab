# 6 · Why the agent can't self-arm (the classifier caveat)

This chapter is the one that most changes how you *build*, because it kills
the shortcut everyone reaches for first: "just have the agent arm
auto-merge on its own PR." In a stack with a merge-policy classifier, that
call is denied — and the denial is correct, and there is a right way to
build around it. This cookbook's entire architecture is that right way.

## The wall

In the source repo, agent seats hit a hard classifier wall on any
self-landing act. Its status doc records it plainly:

> Agent seats are DENIED from arming auto-merge or self-merging their own
> (or a sibling's) PR (**[Self-Approval]** / **[Merge Without Review]**).

Note the scope: not just `merge`. **Arming** auto-merge from the agent's
seat is denied too, because in a repo where the arm would land the PR, arming
*is* merging. The classifier follows the *authorization*, not the API route
— it recognizes "arm auto-merge on my own PR" as the same act as "merge my
own PR" and denies both. Retrying through a different path (REST instead of
GraphQL, a sub-agent instead of yourself, "arm" instead of "merge") is
recognized as the same act and denied again.

## Why this is correct, not an obstacle

An agent approving and landing its own work defeats two-party review. A
policy layer that lets an agent tunnel around that by phrasing the merge
differently would be worthless. So the correct design is not to defeat the
classifier — it is to **make the merging identity something other than the
agent**, which is exactly the merge-on-green model (chapter 1). The agent
does the two things it is allowed to do:

1. **Push its branch**, and
2. **Open the PR READY.**

That's it. It never arms and never merges. A repo-owned *workflow* arms;
GitHub merges. The workflow's token is the sanctioned merger, and it is a
different identity from the agent's seat — so the classifier wall simply
does not apply to it. This repo states the resulting rule directly:

> agent seats still cannot self-enable auto-merge, so the sanctioned merger
> is the workflow, never the seat.

## The build consequence: never probe a denied wall twice

The single most expensive mistake here is retrying. **First denial is
terminal.** Do not retry a denied self-merge or self-arm, and do not retry
it through a synonym. If your agent gets the `[Self-Approval]` /
`[Merge Without Review]` denial, the answer is never "try a different merge
call" — the answer is "this was always the workflow's job; push and open,
and let the enabler arm." Record the denial verbatim somewhere durable so
the next session doesn't re-probe the same wall; a paraphrased wall gets
re-tested by whoever doesn't recognize it.

## What the seat legitimately does around the merge

To be concrete, the sanctioned seat-side choreography is:

- Commit the born-red journal (chapter 4) **first**.
- Do the work; flip the journal to `complete` in the **last** commit.
- Push the branch.
- Open the PR **READY** (never draft — see chapter 7 on why draft flips are
  quota-fragile).
- **Stop.** The enabler armed the PR at open; the gate greens on the flip;
  GitHub lands it. The seat performs no merge, no arm, no `do-not-automerge`
  removal on its own PR.

If you find your agent *wanting* to touch the merge, that wanting is the
bug. The design is finished when the agent's last act is `open PR` and the
next actor is a workflow.

**Sources** (public repo `menno420/venture-lab`):
`docs/current-state.md` @ `4e0a37c` (the ~2026-07-15 merge-classifier
change; "the sanctioned merger is the workflow, never the seat"; agent
seats denied from arming auto-merge or self-merging via
**[Self-Approval]** / **[Merge Without Review]**); the model's live
correctness verified by the five 2026-07-17 `github-actions[bot]` merges
(chapter 1) — every one performed by the workflow token, none by an agent
seat.
