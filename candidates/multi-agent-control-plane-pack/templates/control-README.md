# control/ — manager ↔ lane coordination protocol

> **One writer per file.** Violating writer-ownership is the only way
> this protocol merge-conflicts.

## Writer table

| File | Writer | Semantics |
|---|---|---|
| [`inbox.md`](inbox.md) | **MANAGER ONLY** | Append-only orders. The lane NEVER edits this file — not to ack, not to mark done, not to fix typos. |
| [`status.md`](status.md) | **LANE ONLY** | Overwritten by the lane each session. |
| [`outbox.md`](outbox.md) | **LANE ONLY** | Append-only dated sections, newest last: asks and reports UP. |
| [`claims/`](claims/README.md) | creating session | One file per in-flight work claim; deleted at session close. |

## Inbox semantics — `status: new` stays `new`

Orders keep `status: new` in the inbox forever — nobody flips them.
To see what is unexecuted, **diff the inbox against `status.md`**: any
order number not listed there as acked/done is new work.

## The standing ritual (every session, every wake)

1. **FIRST:** fetch; read `control/inbox.md` **AT HEAD**. Diff against
   your status. Claim before building.
2. **HEARTBEAT BEFORE WORK:** first commit is the session card / a
   status WIP line. A silent session is indistinguishable from a dead
   one.
3. Act on orders; ambiguous orders become ⚑ asks in your status — then
   do the rest, don't stall.
4. **LAST:** overwrite `control/status.md` — timestamp (`date -u`),
   phase, health, last-shipped PR, blockers, orders acked/done, ⚑
   asks. **Re-read the inbox at HEAD immediately before this final
   write** and ack anything new.

## Rules that ride the protocol

- Report progress ONLY in committed files — never only in chat.
- All timestamps from `date -u`, never the model's sense of time.
- A no-op wake costs at most a heartbeat line — never a full PR round.
