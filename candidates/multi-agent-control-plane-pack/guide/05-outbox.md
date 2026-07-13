# 5. The outbox — routing asks up without breaking one-writer

## The contract

`control/outbox.md` is **lane-written, append-only, dated sections
newest last**. It is the lane's channel UP — to the manager, the
owner, or sibling lanes via the manager — for anything that is not a
status fact:

- questions the lane cannot answer itself,
- work that belongs to a different lane,
- reports the manager asked for,
- ideas worth routing somewhere else.

Why not put these in `status.md`? Because status is overwritten every
session — an unanswered question would be erased by the next
heartbeat. The outbox is append-only precisely so asks SURVIVE until
answered. And the lane cannot write into anyone else's inbox (that
file has one writer, and it isn't you) — the outbox is where the
manager comes to collect.

## Typed markers

Prefix entries with an ALL-CAPS type token so a manager — human or
agent — can triage by grep:

- **`SIM-REQUEST:`** — a question for an analysis/simulation lane
  ("PWYW vs $5 fixed for X?"). The key discipline: **ask, then
  CONTINUE** — file the request and keep working on what doesn't
  depend on the answer. An asked-and-waiting lane is a stalled lane.
- **`WEBSITE-IDEA:`** (pattern: `<TOPIC>-IDEA:`) — work spotted that
  belongs to another lane; the marker makes it routable without the
  lane ever touching the other lane's files.
- **`INFO:`** — a fact the manager should know that fits no other
  slot ("this fulfillment channel doesn't support the format; owner
  decision pending").
- Ordered reports (e.g. a "night report" the manager requested) go in
  as their own dated section, and the answering entry cites the order
  number it serves.

Every entry names its source ("source: PR #NNN packet") — asks outlive
their context exactly like orders do.

## The round trip

The full loop, as it runs in production: the lane files `SIM-REQUEST:`
entries in its outbox → the manager routes them to the lane that can
answer → the answers come back as an ORDER **in the asking lane's
inbox**, with citations back to the answering lane's outbox → the lane
applies them and acks in its status. Four surfaces, each with one
writer, and the question-asker never blocked while waiting.

---

**Sources:** `control/outbox.md@58cdb14` (production entries: two
WEBSITE-IDEA batches, five SIM-REQUESTs, an INFO fulfillment note, and
two ordered reports — morning tally + night report — each citing the
order it serves) · round-trip production events: the outbox
SIM-REQUESTs of `58cdb14` (PR #144) were answered as inbox ORDER 010
(PR #161, squash `84d4bcb`) and applied + acked by PR #163 (squash
`e252b46`).
