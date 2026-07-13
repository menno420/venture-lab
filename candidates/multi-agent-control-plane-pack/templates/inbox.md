# control/inbox.md — MANAGER-WRITTEN, append-only

> One writer: the manager. The lane NEVER edits this file. Orders stay
> `status: new` here — the lane diffs this file against its own
> `control/status.md` to see what is unexecuted. Protocol:
> [`README.md`](README.md).

---

## ORDER 001 · <ISO8601 from date -u> · status: new
priority: P1
from: <who issued it, with provenance>
executor: <which lane, which wake>
do: <the task — concrete, self-contained>
why: <one line — the reason must survive the author>
done-when: <a state the AGENT can reach, not a human>
citations: <files@sha, PRs, upstream orders>

---

## Standing default (between orders)

When the inbox has no unexecuted orders: <your lane's default work —
never idle, never undefined>.
