# Chapter 7 — The Pacemaker and the Failsafe: Keeping a Fleet Awake Without Letting It Idle

An autonomous fleet has to keep running when no human is watching — but "keep running" is a deceptively hard requirement. An agent that finishes a task and simply stops leaves the lane dead until someone pokes it. An agent that loops without direction burns tokens on nothing. This lane threads that needle with two mechanisms working together: a self-chaining **pacemaker** and a cron **failsafe**, governed by one behavioral rule — *decide and flag, never idle undefined.*

## The pacemaker

The primary heartbeat is a self-chaining wake. When the coordinator seat finishes a slice of work, it schedules its own next wake a short interval out — this lane uses a `send_later` chain in roughly the fifteen-to-forty-five-minute range — and that next wake, when it fires, does the same. The chain is self-perpetuating: each beat is responsible for scheduling the beat after it. As long as the chain is unbroken, the lane wakes on its own cadence, works a slice, and re-arms.

The routine is recorded in the succession brief (`docs/NEXT-SESSION.md`, the Routines section) and its exact create-arguments live in `control/status.md` under the ORDER-002 section. That placement matters: the operational parameters — the precise interval, the trigger IDs — are kept in the live status file, not scattered, so that a fresh session can find and re-arm the chain from one authoritative place.

## The failsafe

A self-chaining pacemaker has one obvious flaw: if any beat fails to schedule the next — a crash, a stopped worker, a missed wake — the chain is broken and the lane goes silent, with nothing to restart it. So the pacemaker is backstopped by a **cron failsafe**: an independent, roughly two-hourly scheduled wake (in this lane, a cron of `0 */2 * * *`) that fires regardless of the pacemaker's state. If the fast chain is alive, the failsafe finds recent work and does little. If the chain has broken, the failsafe is what notices and revives it.

The two mechanisms have deliberately different characters. The pacemaker is fast, self-referential, and fragile-by-design — it gives responsive cadence but depends on every beat succeeding. The failsafe is slow, external, and robust — it gives a guarantee of eventual wake but at coarse resolution. Neither alone is sufficient: the pacemaker alone can die silently; the failsafe alone is too slow to run a lane. Together they give a responsive cadence with a floor under it.

## Decide and flag, never idle undefined

The mechanisms keep the lane awake; a behavioral rule keeps it from wasting the wakes. The standing default, from the brief, is: between orders, *deepen the current top candidate* — advance its smallest real artifact, validate an assumption, keep its cost line honest — and **never idle undefined.** A wake that finds no explicit order does not spin or no-op; it falls back to a defined default action. And when a wake makes a judgment call in the absence of instruction, it *decides and flags*: it takes the reasonable action and records the decision where the coordinator's sweep will collect it for retroactive review, rather than either blocking on a missing instruction or acting silently.

This is the same "leave a reviewable trail" instinct as the owner-action grammar (Chapter 4) and the born-red card (Chapter 3): the agent is allowed to act under uncertainty, but never allowed to act invisibly.

## Honest note: this is operational detail, not universal law

Be clear about what generalizes here and what does not. The *pattern* — a fast self-chaining heartbeat plus a slow independent failsafe, governed by a never-idle-undefined default — is the transferable lesson. The specific numbers are **not** a recommendation. The exact cadence (which interval, which cron expression) and the trigger IDs are operational details tuned to this lane's token budget, task granularity, and platform; they are recorded for *this* lane's continuity, not offered as the correct values for yours. A fleet with different economics would pick different intervals, and should. Treat the two-mechanism structure as the lesson and the numbers as one lane's instantiation of it.

## The rule you take away

Keep a fleet alive with two mechanisms of different character: a fast, self-chaining pacemaker for responsive cadence, and a slow, independent cron failsafe as the floor that revives a broken chain. Keep the operational parameters in one authoritative place so a fresh session can re-arm them. And govern every wake with *decide and flag, never idle undefined* — a wake without an order runs the defined default and leaves a reviewable trail, rather than spinning or silently stopping. The structure is the lesson; the exact cadence is just this lane's dial setting.
