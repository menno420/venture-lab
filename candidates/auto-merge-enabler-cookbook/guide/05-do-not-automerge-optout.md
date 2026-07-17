# 5 · The `do-not-automerge` opt-out (and where auto-merge is turned on)

A landing strip that lands *everything* is a hazard. Some PRs must wait for
a human: a risky migration, a doctrine change, a PR the owner wants to read
before it lands. The enabler's opt-out is a single label —
`do-not-automerge` — and this chapter is about how it works and the one
repo setting that makes any of this live.

## The label, and the PR that proves it works

The enabler honors `do-not-automerge` in two places (chapter 2): the
event-payload `if:` and a fresh API re-read. A PR carrying the label is
never armed, so it sits green and waits for an explicit human merge.

This is not hypothetical. On 2026-07-17, PR #218 — a docs-and-doctrine
"fresh-start cleanup" the author wanted a human to land — was opened with
the label and its body said so:

> Labeled `do-not-automerge` so it waits for the owner's explicit merge
> (this seat does not self-merge).

The result, from the merge record: PR #218 was `merged_by: menno420` — the
**human owner**, by hand — while the five auto-merge-eligible PRs that same
day were `merged_by: github-actions[bot]`. The label did exactly its job:
it took one PR off the auto-merge path and left it for a person, while the
enabler kept landing everything else. One label is the entire manual-review
escape hatch.

## The label is advisory routing; the required check is enforcement

Read this carefully, because it is the part people get backwards. The
`do-not-automerge` label is **routing**, not a security boundary. It tells
the enabler "don't arm this one." It does **not** make the PR unmergeable —
a human can still merge a labeled PR (that's the point). The thing that
*enforces* — that actually holds a PR red and unmergeable — is the required
check (chapters 3-4). The enabler's own comment draws the line:

> The label is advisory routing; the required check going red is the
> enforcement.

So: use the label to keep the robot's hands off a PR you want to land
yourself. Use the required gate (born-red HOLD, real tests) to keep
*anything* unfinished or broken from landing at all. They are different
tools for different jobs; don't reach for the label when you needed a red
check.

## The two one-time settings that make it live

The enabler is **inert** until an owner/admin flips two things in the
repo UI. No workflow can do this for you (chapter 6 explains why the agent
can't, and why that's correct):

1. **Settings → General → Pull Requests → "Allow auto-merge" = ON.**
   Without this, `gh pr merge --auto` has nothing to enable; the arm fails.
2. **A ruleset on the default branch REQUIRING your gate's context name**
   (this repo: `substrate-gate`). Without a required context, arming merges
   instantly — the refuse-to-arm guard (chapter 3) is what stops that from
   being a disaster, but you still have no gate. Add the required check.

Verify both from the API, not the settings page (chapter 3's checklist). A
green settings screen is a claim; a fresh PR showing `blocked` with your
gate in its check runs is proof.

## A note on scope as a second opt-out

The label is the *per-PR* opt-out. The enabler's `if:` branch-namespace
filter (`claude/*`) is the *standing* opt-out: any PR outside your agent
namespace is never armed at all. A human's own topic branch, a Dependabot
PR, a fork — none of them match, so none of them auto-merge. If you want a
whole class of PRs to always wait for a human, put them on a branch prefix
the enabler doesn't match, and you never need the label.

**Sources** (public repo `menno420/venture-lab`):
`.github/workflows/auto-merge-enabler.yml` @ `aa04700` (the label carve-out
in the `if:` + the fresh re-read; "the label is advisory routing; the
required check going red is the enforcement"; the two one-time settings in
the header); PR #218 verified via the GitHub API on 2026-07-17 — labels
`["do-not-automerge"]`, `merged_by: menno420` (human), contrasted with the
same day's five `github-actions[bot]` auto-merges (chapter 1).
