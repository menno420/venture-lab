# Session discipline — the 1-page playbook

The habits that keep a coding-agent session recoverable, parallel-safe, and
honest. Extracted from a real autonomous agent fleet's retros. Five rules; read
them once, then let the hooks remind you.

## 1. Heartbeat-before-work

The **first act** of any session is a status commit — a session card (born red,
`Status: in-progress`) or a one-line WIP note. Do this *before* the real work.

> A silent session is indistinguishable from a dead one. Platforms will
> sometimes make you silent for an hour; the heartbeat is how a parallel
> session (or a human) knows you're alive and what you're touching.

## 2. Claim-before-build

Before editing a shared surface, **declare it**: a claim file, an issue
assignment, a WIP note naming the paths you own this session. First-declared
wins a conflict. Two agents editing the same file with no claim is the most
expensive failure mode there is — it's a merge conflict you find out about
after both of you did the work.

## 3. Close ritual

A session isn't done until you run the close ritual, in order:

1. **Verify** — run the change end-to-end (not just read the diff) and the
   quality floor. Paste the result into the card.
2. **Write the close-out** — Deliverable summary + Log on the session card.
3. **Flip the badge** — `in-progress` → `complete` as the deliberate last edit.

Completion is a state you produce on purpose, never one that happens by
drifting away from the keyboard.

## 4. Timestamps from `date -u`

Every timestamp comes from `date -u`, never the model's sense of time — a model
has no clock and will confidently invent one. Commit history is the record of
when things happened; make the card agree with it.

## 5. Forward-only git

No force-push, no history rewrites, no amending pushed commits. If something
landed wrong, fix it forward with a new commit. History is append-only evidence;
rewriting it destroys the one audit trail a parallel session can trust.

---

### Why these five

Each rule fixes a failure that *only* shows up with autonomous or parallel
agents and is invisible in a solo human workflow: silent-death (1),
double-build collisions (2), sessions that trail off unfinished (3),
hallucinated timelines (4), and destroyed audit trails (5). Wire the hooks
(see `hooks/`) so the discipline is enforced by the harness, not by willpower.
