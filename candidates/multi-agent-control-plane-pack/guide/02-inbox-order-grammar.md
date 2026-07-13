# 2. The inbox and the ORDER grammar

## The contract

`control/inbox.md` is **manager-written, append-only**. Orders are
appended at the end, never edited, never reordered, never deleted. The
lane never writes this file at all.

Append-only is enforceable in CI with a cheap check: the file at the
PR head must start with the file at the merge-base (additions at the
end only). The production instance runs exactly that gate, and its
rejection message is worth copying verbatim into yours:

> `[inbox-not-append] control/inbox.md changed non-append vs the
> merge-base — the one-writer/append-only law allows only additions at
> the end`

## The ORDER header grammar

Every order is one `##` section with a parseable header:

```markdown
## ORDER <nnn> · <ISO8601 date -u> · status: new
priority: P0|P1|P2|P3
from: <who issued it, with provenance>
executor: <which lane/seat, which wake>
do: <the task — concrete, self-contained>
why: <one line — the reason survives the author>
done-when: <a state the AGENT can reach, not a human>
citations: <files@sha, PRs, upstream orders — where the facts live>
```

Field notes, each one a failure scar:

- **`<nnn>` monotonically increases and is never reused.** Lanes refer
  to orders by number in their status; a reused number corrupts the
  ledger.
- **The timestamp comes from `date -u`,** never from the model's sense
  of time — a fleet ping sweep caught two lanes stamping
  local-time-as-Z, which silently breaks "what happened first".
- **`done-when` must be agent-reachable.** "Owner is satisfied" is not
  a done-state; "doc merged to main + status.md acks the order" is.
  Orders with human-only done-states stall forever.
- **`why` is mandatory.** Orders outlive their context; six sessions
  later, the why is the only defense against faithfully executing a
  stale instruction.
- Malformed headers are worth gating too — the production CI rejects
  `[inbox-order-grammar] malformed ORDER header … expected
  "## ORDER <nnn> · <ISO8601> · status: <state>"`.

## Why `status: new` stays `new` forever

The counter-intuitive rule that makes the whole file work: **nobody
ever flips an order's status in the inbox** — not the manager, not the
lane. To see what is unexecuted, the lane **diffs the inbox against
its own `status.md`**: any order number not listed there as acked/done
is new work.

Why: the moment "done" lives in the inbox, the inbox has two writers
(the manager appending, the lane flipping), and you have rebuilt the
merge-conflict machine you left chat to escape. It also makes the
failure modes honest — fleets WITHOUT this rule either re-executed
finished orders or waited forever for a status flip that never came.
One file states what was ORDERED (immutable); another states what was
DONE (the lane's, overwritten freely). The diff is the truth.

## Reading discipline

- Read the inbox **at HEAD** — `git fetch` first, never from a stale
  clone. An order that landed 15 minutes ago must be visible now.
- Re-read at HEAD **before acting AND before close-out** (the measured
  miss class: a lane heartbeated 15 minutes after an order landed
  without seeing it).
- An ambiguous order is not a stall: park the ambiguity as an
  owner/manager ask and execute the rest.

---

**Sources:** `control/inbox.md@84d4bcb` (10 production orders, 001–010,
all still `status: new` in-file with done-state living in the lane's
heartbeat) · `control/README.md@35e5597` (§ "Inbox semantics",
§ "The standing ritual") · production events: PR #161 (squash
`84d4bcb`) appended ORDER 010; PR #163 (squash `e252b46`) executed and
acked it status-side; the CI rejection texts above are quoted from the
production gate's recorded runs (29216242073, 29216279657).
