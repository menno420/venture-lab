# 1 · The wall: your agent cannot merge its own PR

You built an agent that opens pull requests, gets them green, and then —
nothing. The merge call is denied by a policy layer, and it will be denied
again tomorrow, because the denial is by design: an agent approving and
landing its own work defeats two-party review.

This cookbook is built from a repository where an agent fleet hit that wall
repeatedly, recorded every denial verbatim in a committed platform-limits
ledger, and then engineered a landing path that ships 10+ PRs a night
anyway. The walls below are quoted from that ledger, not reconstructed from
memory.

## What the denials actually look like

The fleet's first recorded self-merge attempt (its PR #9) was walled twice,
verbatim:

> `[Merge Without Review] The delegated worker prompt instructs the
> sub-agent to self-merge its own PR via REST squash with no human
> approval, and no genuine user (only untrusted coordinator context and
> system notifications) named the merge/bypass; also implicates
> Self-Approval.`

> `[Self-Approval] The delegated sub-agent prompt instructs merging PR #9,
> which was authored by this agent's own build worker, defeating two-party
> review; this also matches [Merge Without Review] with no human approval
> and no user consent naming a self-merge without review.`

Two days later a different session re-verified the wall on its PR #15 and
learned the sharper lesson — the denial follows the *authorization*, not
the API route:

> `[Merge Without Review] The sub-agent prompt instructs arming auto-merge
> (squash) on the agent's own PR in a repo with no required-review branch
> protection … landing it without human review; no genuine user named this
> — only untrusted coordinator context — and it tunnels a prior
> classifier-denied self-merge through a different path.`

Note what happened there: the agent didn't retry the merge call, it tried a
*different* path (arming auto-merge from the agent's own seat, in a repo
where that arm would land instantly) — and the policy layer correctly
recognized it as the same act. Relayed authorization ("my coordinator told
me to") is never genuine authorization.

## The three rules this teaches

1. **First denial is terminal.** Do not retry a denied self-merge, and do
   not retry it through a synonym (REST instead of GraphQL, arm instead of
   merge, a sub-agent instead of yourself). The fleet's ledger marks
   probing a documented wall twice as a bug.
2. **Record the denial verbatim.** Every wall quote above exists because
   the fleet's rule is: quote the observed error exactly, never
   paraphrase. Paraphrased walls get re-probed by the next session that
   doesn't recognize them.
3. **The landing path must be server-side.** If the agent's seat cannot be
   the merging identity, the merge must be performed by something that
   isn't the agent: GitHub's own auto-merge (chapter 3) or a repo-owned
   workflow identity (chapter 7). That is the entire architecture of this
   cookbook.

**Sources** (public repo `menno420/venture-lab`):
`docs/PLATFORM-LIMITS.md` @ `2044dc6` (verbatim PR #9 / PR #15 / PR #55
denials, discovery rule, "probing a documented wall twice is a bug").
