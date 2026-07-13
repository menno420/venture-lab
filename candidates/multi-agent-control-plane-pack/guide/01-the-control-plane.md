# 1. The control plane — one law, five surfaces

## The failure you are buying your way out of

Two agent sessions on one repo fail in exactly three ways:

1. **Duplicated work** — both pick up the same task, one PR wins, the
   other's tokens are waste.
2. **Clobbered coordination files** — both append to the same status
   or TODO list, and every merge is a conflict a human resolves.
3. **Lost orders** — an instruction lands in a chat window, the chat
   ends, the instruction is gone; or it lands in a file the agent read
   an hour ago and never re-reads.

All three have the same root cause: shared mutable surfaces with no
ownership rule. The fix is one law:

> **One writer per file.** Every coordination file has exactly one
> party allowed to write it. Violating writer-ownership is the only
> way this protocol merge-conflicts.

## The five surfaces

| Surface | Writer | Direction | Semantics |
|---|---|---|---|
| `control/inbox.md` | manager ONLY | manager → lane | Append-only orders. The lane never edits it — not to ack, not to mark done, not to fix typos. |
| `control/status.md` | lane ONLY | lane → manager | Overwritten each session: the heartbeat. |
| `control/outbox.md` | lane ONLY | lane → manager | Append-only dated sections: asks, reports, routed ideas. |
| `control/claims/*.md` | creating session | lane ↔ lane | One file per in-flight work claim; deleted at close. |
| `.sessions/*.md` | creating session | audit trail | One card per session, born-red, flipped complete last. |

Read the table columns as guarantees: because the inbox has one
writer, the lane can trust an order will never silently change under
it. Because the status has one writer, the manager can trust its
timestamp. Because claims and cards are one-file-per-thing, two
sessions structurally cannot conflict on them.

## Why files, not a dashboard or a message bus

- Your agents already read and write files, and git already gives you
  history, diffs, blame, and merge semantics for free. A dashboard is
  a second system that can drift from the repo; the control plane IS
  the repo.
- Chat is where coordination goes to die: it evaporates, it isn't
  diffable, and a new session can't read it. The rule that follows:
  **report progress only in committed files, never only in chat.**
- Every surface is human-legible. When your fleet does something
  strange at 3am, you read five small markdown files and know the
  state — no log-diving.

## The manager can be you

The topology is manager ↔ lanes, but "manager" is a role, not a
process: a human filling the inbox by hand, a coordinator agent, or a
cron-fired orchestrator all work identically, because the contract is
just "the inbox's single writer". Start as the manager yourself;
automate the role later without changing any file format.

---

**Sources** (the production instance this chapter distills — a
multi-agent repo where this plane has coordinated 150+ merged PRs):
`control/README.md@35e5597` (writer table, one-writer law, protocol) ·
`docs/conventions.md@35e5597` (session discipline #7–#12) · worked
end-to-end order lifecycle: PR #161 (manager appends ORDER 010 to the
inbox, squash `84d4bcb`) → PR #163 (lane executes and acks it in
`status.md`, squash `e252b46`) — the inbox row itself untouched by the
lane, as the law requires.
