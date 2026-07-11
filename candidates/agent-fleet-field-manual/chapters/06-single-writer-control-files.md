# Chapter 6 — Single-Writer Control Files: One Author Per Bus, or You Lose Writes

When several agents run at once, the files they use to coordinate become a shared mutable resource — and shared mutable state is where concurrent systems go to die. This lane's answer is not locking or merging; it is an ownership rule so simple it fits in a sentence: **every control file has exactly one writer.** This chapter is about which file that writer is, and why the discipline prevents the lost-update race that would otherwise corrupt the fleet's shared memory.

## The control bus

The lane coordinates through a small `control/` directory. Two files carry the traffic:

- **`control/inbox.md`** — the orders the manager issues to the fleet.
- **`control/status.md`** — the coordinator's live report of lane state.

If any agent could write either file, two agents finishing work at the same time would both read the current status, both edit it, and both write it back — and whichever wrote second would silently erase the first's update. That is the lost-update race, and in a fleet it is not a rare edge case; it is the *normal* outcome of concurrency without an ownership rule.

## The two rules

**`inbox.md` is manager-written, append-only. Workers never edit it.** Orders arrive from the manager and stay in their as-issued state (`status: new`) until acted on. A worker discovers what is unexecuted not by editing the inbox but by *diffing* it against the status file — comparing the orders in the inbox against the "done" lines in status to find the gap. The succession brief (`docs/NEXT-SESSION.md`) states the rule directly: *"You NEVER edit `control/inbox.md` (manager-written)."* A worker that edited the inbox would be rewriting its own instructions — the exact circularity Chapter 3's born-red rule guards against, in a different file.

**`status.md` is coordinator-written, overwritten wholesale as the deliberate last step.** The coordinator does not surgically patch status while work is in flight. It does the work, and then — as the final action — re-reads the inbox at HEAD one more time and overwrites the status file whole. The brief again: *"You overwrite `control/status.md` wholesale as the deliberate LAST step, after a final inbox re-read at HEAD."* The wholesale overwrite is deliberate: a full rewrite from a fresh read cannot half-apply, and the final inbox re-read ensures the status reflects the latest orders rather than a stale snapshot taken before the work began.

**Workers never touch `control/` at all.** A worker's outputs go into product directories, session cards, and launch docs — never the control bus. The control files are the coordinator's and manager's instruments; a worker reads them for orientation and writes elsewhere.

## Why one writer beats clever merging

You could imagine solving the race with locks, or with a merge strategy that reconciles concurrent edits. Both are more machinery and more failure modes. The single-writer rule dissolves the problem instead of managing it: if only one process ever writes a file, there is no concurrent write to lose, no lock to deadlock, no merge to botch. The cost is a constraint on *who* may write — and in a fleet with clear manager/coordinator/worker roles, that constraint is nearly free, because the roles already differ in what they are responsible for.

The read side stays unconstrained. Any agent may *read* any control file for orientation — indeed the boot ritual requires it: land on HEAD, read the inbox, diff against status. Reading never races. Only writing does, and writing is what the ownership rule pins down.

## The honest limit

This is a discipline enforced by convention and role, not by a filesystem-level guarantee. Nothing physically prevents a misbehaving worker from writing `status.md`; the rule holds because the workers are instructed not to, and because the boot ritual and succession brief repeat the rule at every entry point. In a larger or less-trusted fleet you would want to back the convention with a mechanical check. Here it is a stated protocol that the sessions follow — effective in this lane's scale, and named as convention rather than dressed up as an enforced invariant.

## The rule you take away

Give every coordination file exactly one writer, and make the write pattern match the failure you fear. Manager-written, append-only for the order stream, so instructions are never rewritten by their recipients. Coordinator-written, wholesale-overwrite-as-last-step for the status, so a report can never half-apply and always reflects a fresh read of the latest orders. Workers write their own artifacts and never the bus. Everyone reads freely; exactly one role writes each file. Concurrency stops being a hazard the moment there is nothing to concurrently write.
