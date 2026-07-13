# Quickstart — install the control plane in ~15 minutes

No build step, no dependencies. You are copying five markdown files and
adopting three habits.

## 1. Copy the templates

From `templates/` into your repo:

```
your-repo/
  control/
    README.md        <- templates/control-README.md
    inbox.md         <- templates/inbox.md
    status.md        <- templates/status.md
    outbox.md        <- templates/outbox.md
    claims/
      README.md      <- templates/claims-README.md
  .sessions/         <- create empty; cards accumulate here
```

## 2. Decide who writes what (the one law)

Fill in the writer table in `control/README.md`:

| File | Writer |
|---|---|
| `control/inbox.md` | the MANAGER only (you, or your orchestrator agent) |
| `control/status.md` | the LANE only (the working agent) |
| `control/outbox.md` | the lane only (append-only, dated sections) |
| `control/claims/<file>.md` | the session that created it |
| `.sessions/<date>-<slice>.md` | the session that created it |

One writer per file is the entire trick. Every convention in the guide
is a consequence of it. (Chapter 1.)

## 3. Put the ritual in your agent's standing instructions

Verbatim, adapted to your paths:

1. FIRST: fetch and read `control/inbox.md` AT HEAD. Diff it against
   your own `control/status.md` to find unexecuted orders.
2. HEARTBEAT BEFORE WORK: first commit is your session card (born-red,
   `Status: in-progress`) or a status WIP line.
3. Claim before build: one file in `control/claims/`, then re-read the
   directory at HEAD before building.
4. LAST: overwrite `control/status.md` (timestamp from `date -u`,
   phase, last-shipped PR, blockers, orders acked/done) — and re-read
   the inbox at HEAD immediately before this final write.

## 4. Issue your first ORDER

Append to `control/inbox.md` using the grammar (chapter 2):

```markdown
## ORDER 001 · 2026-07-13T14:00:00Z · status: new
priority: P1
do: <the task, concrete>
why: <one line>
done-when: <a state the AGENT can reach, not a human>
```

It stays `status: new` in the file forever; done-state lives in the
lane's `status.md`. Do not flip it — chapter 2 explains why.

## 5. Watch the first collision not happen

Start two sessions. Each claims before building (chapter 4); the
second one sees the first one's claim file at HEAD and picks other
work. That non-event is the product working.

## Optional hardening

- Wire the born-red hold into CI so a session card that still says
  `in-progress` blocks its own PR from merging (chapter 6).
- Add an advisory (never blocking) staleness pass over
  `control/claims/` — anything older than ~72h with no visible
  activity is prunable on sight (chapter 4).
