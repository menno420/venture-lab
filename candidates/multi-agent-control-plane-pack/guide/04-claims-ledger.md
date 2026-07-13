# 4. The claims ledger — one file per claim

*(This chapter is the "Parallel-Agent Claims Kit" that almost shipped
as a standalone product; it lives here because its audience is exactly
this pack's audience.)*

## The problem

Several sessions run at once; two of them picking up the same task is
pure waste. A PR is the LATE in-flight signal — by the time it exists,
the duplicate tokens are already spent. The claims ledger is the EARLY
signal: "is someone already on this?" answerable before any work.

## The measured design decision

The obvious design — one shared `ACTIVE-WORK.md` list every session
appends to and prunes — is a merge-conflict machine. A real-`git merge`
simulation (external to this pack: `tools/sim/claim_layout_sim.py` in
the seller's sibling repo `menno420/superbot`; not re-run in-kit)
measured it:

- shared-append list: **~98% conflict rate** under concurrent sessions;
- splitting the list by sector: only halved it;
- **one file per claim: 0% at every concurrency level** — two sessions
  never touch the same file.

The rule that preserves the 0%: **no hand-edited shared index.**
Discover claims with `ls control/claims/` — no README ever lists them.
The moment you add "and also add your claim to the table in the
README", you have rebuilt the shared-append list.

## The claim-bullet grammar

One file — `control/claims/<branch-or-scope>.md` — one bullet:

```markdown
- `branch-or-scope` · **scope** — one-line detail · expected files/area · YYYY-MM-DD
```

Keep the backticks around the branch/scope token and the ISO date: if
you later add an advisory checker, those two anchors are what it
parses; an unparseable claim is invisible to a duplicate scan.

## The lifecycle

1. **Before starting work:** scan `control/claims/` AND the open PRs.
   Already claimed or in flight → coordinate or pick something else.
2. **Create the claim file, land it fast** (control-plane traffic
   should ride your fastest CI lane), then **re-read the directory at
   HEAD before building** — if both lanes do this, the second claimer
   always sees the first.
3. Build.
4. **Delete your own claim file at session close.** The durable record
   is the PR; a claim is a whiteboard note, not an audit trail.

## Arbitration and expiry (decide these BEFORE the first race)

- **First claim merged wins** a collision. A deterministic tiebreak
  beats re-litigating every race; the loser deletes its file and
  stands down.
- **Claims expire:** older than ~72h with no visible build activity =
  abandoned; any session may prune it on sight. Without an expiry rule,
  a crashed session's claim fences off its task forever.
- Checks on this ledger should be **advisory, never blocking**
  (formats drift, sessions die mid-flight): nag on unparseable, stale,
  and duplicate claims, but never fail a build over them.

## What claims are NOT for

Inbox ORDERs are claimed on the lane's own heartbeat (an `orders:`
line in `status.md`), never here — the order lifecycle belongs to the
inbox/status pair (chapters 2–3), which preserves one-writer-per-file
for the ledger the manager reconciles. `control/claims/` is for
**work**: coordinator-assigned slices, self-initiated builds, anything
two parallel sessions could both pick up that isn't an ORDER id.

---

**Sources:** `control/claims/README.md@35e5597` (grammar, lifecycle,
arbitration, checker contract) · `control/README.md@35e5597`
(§ "Claiming work") · conflict-rate measurement cited as external:
`menno420/superbot` `tools/sim/claim_layout_sim.py` (a real-`git merge`
simulation; this pack cites, it does not re-run) · production event:
PR #154 (squash `557b744`) — a routine prune of two closed sessions'
claim files, the expiry rule executing as designed.
