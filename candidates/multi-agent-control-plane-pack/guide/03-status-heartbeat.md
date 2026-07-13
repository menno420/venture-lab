# 3. The status heartbeat

## The contract

`control/status.md` is **lane-written, overwritten each session**. It
is not a log (git history is the log); it is the current answer to
"if this agent died right now, what would its successor need to know?"

A useful heartbeat carries, every time:

- `updated: <ISO8601 from date -u>` — the freshness stamp, first line.
- Phase / health — what the lane is doing and whether it's blocked.
- Last-shipped PR (number + squash SHA) — the resume pointer.
- Orders acked/done by number — the inbox's done-ledger (chapter 2).
- ⚑ needs-owner / needs-manager asks — decisions parked, not stalled.
- Next 1–3 — the baton for the successor session.

## Heartbeat BEFORE work

The first act of any session is a committed heartbeat — the session
card or a status WIP line — before any real work:

> A silent session is indistinguishable from a dead one, and the
> platform WILL sometimes make you silent for an hour.

Without this rule, the manager cannot tell "session working on
something long" from "session crashed at boot", and the recovery
action for those two states is opposite (wait vs restart). The
heartbeat makes the distinction observable for the cost of one commit.

## Re-stamp LAST

The mirror rule: the status overwrite is the **last** act of the
session, and immediately before it the lane re-reads the inbox at HEAD
and acks anything new. A session that heartbeats first and last brackets
its work: everything between the two commits is attributable to it.

Two production-measured reasons for the LAST discipline:

- The stale-heartbeat poison: a session that dies after doing work but
  before re-stamping leaves a status file describing the PREVIOUS
  state. A successor booting from it re-plans work that already shipped.
  (Production scar: a lane's status said "PR awaiting merge" for a PR
  that had merged hours earlier; the fix order — re-stamp before
  archive — is what turned re-stamp-last into a standing rule.)
- The close-out race: an order can land while you work. Re-reading the
  inbox at HEAD immediately before the final write is what catches it
  (the fleet's measured miss: a heartbeat written 15 minutes after an
  order landed, without seeing it).

## Cheap wakes

A scheduled wake that finds no new orders costs at most one heartbeat
line — never a full PR round. This keeps "check in every hour"
affordable, which is what makes the heartbeat trustworthy: a
convention that is expensive on empty wakes gets skipped, and a
sometimes-skipped heartbeat is worse than none (silence stops meaning
anything).

## Amendments, not rewrites, for terminal facts

When a fact in the last heartbeat changes after the session closed
(e.g. a PR it reported as dead later merged), the successor amends the
heartbeat with the terminal state rather than leaving the stale claim
standing — the heartbeat is a living ledger, and its credibility is
the fleet's shared asset.

---

**Sources:** `control/status.md@e252b46` (a live production heartbeat:
updated-stamp, applied-order ack with citations, open-PR and claims
state, ⚑ owner asks, next-2 baton) · `control/README.md@35e5597`
(§ "The standing ritual" steps 2 and 4) · `docs/conventions.md@35e5597`
(#7 heartbeat-before-work, #11 `date -u`) · production events: PR #144
(squash `58cdb14`) — an ordered night report delivered status-side;
PR #160 (squash `765e1f8`) — a terminal-state amendment recording that
a session reported dead at 0 words had been resumed and merged.
