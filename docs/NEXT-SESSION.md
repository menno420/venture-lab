# NEXT SESSION — venture-lab resume brief

> **Status:** `reference`

> Rewritten 2026-07-13; counts re-derived at HEAD `5944109` (PR #165;
> catalog last changed by PR #164, Multi-Agent Control-Plane Pack).
> Cold-start brief for the next coordinator session. Read this
> first, then [`current-state.md`](current-state.md) (the living ledger) and
> [`retro/2026-07-13-coordinator-session.md`](retro/2026-07-13-coordinator-session.md)
> (latest retro: the 2026-07-13 night+day coordinator run).

## Boot ritual

1. Land on `origin/main` HEAD (`git fetch origin main && git reset --hard origin/main`).
2. Read `control/inbox.md` at HEAD — MANAGER-written, append-only, **never
   edit it**. Orders stay `status: new` in that file by protocol; done-state
   lives in `control/status.md` — diff the inbox against status acks to see
   what is unexecuted. As of `5944109`: ORDERs 001–010 on file; ORDER 010
   (sim-lab pricing verdicts) is APPLIED + ACKed (PR #163).
3. Read `control/status.md` — the 2026-07-13T13:44Z boot-refresh heartbeat is
   the source of truth for triggers and live ⚑ owner asks (copied below).
4. Scan `control/claims/` AND open PRs before building (claim before build,
   one file per claim — `control/claims/README.md`).
5. `python3 bootstrap.py check --strict` must be **exit 0** before any push.
6. Session card born-red as the FIRST commit; status/heartbeat writes last;
   timestamps from `date -u` (full rules: [`conventions.md`](conventions.md)).

## Catalog snapshot (derived at HEAD `5944109`)

**Products — 1 live + 9 publish-READY + 2 hard-gated:**

- **LIVE: Stripe Webhook Test Kit $29** on Gumroad (launched 2026-07-12,
  measurement mode; buyer path verified end to end). Kill clocks armed:
  **T+7 funnel checkpoint 2026-07-19 · T+14 kill-rule 2026-07-26** (≥1
  organic sale OR ≥1 qualified inbound, else ledger ⚑E NEGATIVE +
  pause/delist). Durable record:
  [`launch/stripe-webhook-test-kit/LAUNCH-LOG.md`](launch/stripe-webhook-test-kit/LAUNCH-LOG.md).
- **Publish-READY** (built + priced + listing drafted + verified + sha
  recorded; publish clicks owner-gated in the queue): Membership-Site
  Boilerplate Kit $49 · Agent-Workflow Template Pack $19 PWYW · Agent Fleet
  Field Manual $39 · Kill-Rule Intake Kit $15 · The False-Green Test Trap
  $15 · The Agent Merge-Wall Cookbook $19 · GitHub Webhook Test Kit $29 ·
  Owner-Click Queue Kit $19 · Multi-Agent Control-Plane Pack $29 (PR #164,
  INTAKE-gated build).
- **Hard-gated (not publish-ready):** Photo Packs — full-res originals are
  owner-held off-repo, the sellable zips are agent-unbuildable until handoff;
  Ship-It Bundle $59 — gated on its ⚑B/⚑D component publish clicks landing
  first.

**Books** (all publish clicks owner-gated; details + tree counts in
[`current-state.md`](current-state.md)): 10 adult titles / 11 complete EN
manuscripts · 5 YA · 1 middle-grade (The Halfway Ferry) · 9 trilingual
picture-book title-lines · editions (27 board-book texts, 4 adult NL
editions, 2 EN novella cuts, Ultramarine serial ×3, 5 large-print specs) ·
31 vetting packets in [`publishing/vetting/`](publishing/vetting/).

**Trading:** R3 (3,468 configs) and R4 (6 pre-registered experiments) both
complete with **0 promotions** — honest zeros; Friday grading is the
scoreboard.

## Owner queue (derived, at HEAD)

[`publishing/OWNER-QUEUE.md`](publishing/OWNER-QUEUE.md) — GENERATED file
(re-run `scripts/derive_owner_queue.py` after any packet change; never
hand-edit). At `5944109` it queues **18 decisions (D1–D18, each with a
bolded default — "go with defaults" works) and 31 click-run publish
sequences totalling 177 unchecked owner clicks** (6 sequences HARD-GATED
behind a blocking D-item); §3 manual-review is empty; §4 lists the SWTK rows
already DONE plus its ⏲ kill-clock checkpoints. These counts move with
every queue regen — when in doubt, the generated file at HEAD wins over any
prose copy (including this one).

## Triggers / wake (verbatim from the 2026-07-13T13:44Z heartbeat — never trust older docs for ids)

- Failsafe wake: `trig_01SbFnHdb1bvUzDnKrDdRb6t` (cron `45 1-23/2 * * *`),
  bound to the coordinator seat.
- Friday grading cron: `trig_01UsNU4JRps4b7jiAMdEfXNi` (`0 9 * * 5`, next
  fire 2026-07-17T09:05Z) — the grading executor is LIVE.
- SWTK T+7 one-shot: `trig_01V9DZrTtDU81Sm7vektX9fa` (fires 2026-07-19T16:37Z).
- SWTK T+14 kill-rule one-shot: `trig_01SNkNWfSXoAdz1ALf4YNbC6` (fires
  2026-07-26T16:37Z).
- FOREIGN, untouched: `trig_01YXNmgqYeYQ1LuepsLmbNCG` — send_later firing
  2026-07-17T09:00Z into a non-seat session; potential duplicate grading
  fire on 07-17, recorded only.
- The pre-cutover id set (old failsafe/grading/T+7/T+14) is **DELETED** —
  any doc citing other trig_ ids is stale. Pacemaker chain: ~15-min
  send_later links on the coordinator seat.

## ⚑ Owner asks (live set, per the heartbeat)

1. **OWNER-QUEUE decisions + clicks** — `docs/publishing/OWNER-QUEUE.md`,
   defaults bolded, "go with defaults" works (counts above).
2. **Branch-delete credential** — `git push --delete` hits a hard 403 wall
   (see `docs/PLATFORM-LIMITS.md`, 2026-07-13 entry); the ~94-branch stale
   list waits on an owner-side credential or manual sweep.
3. **Night Kiln 2 length band** — 16k parity with Book 1 as written vs the
   packet's 20–30k plan; owner's call.

## Landing path (proven, unchanged)

Born-red session card + claim → READY (non-draft) `claude/*`-headed PR → CI
green (kit-tests + substrate-gate) → **the auto-merge enabler self-lands
it**. Seats never arm auto-merge or merge their own PRs. substrate-gate red
while a card is still `in-progress` is designed (born-red HOLD) — it goes
green when the flip commit lands. Hard rails: NO spend, NO account creation,
NO publishing, NO payment flows without an explicit owner go
([`conventions.md`](conventions.md) §13).

## Next 2 (baton, from the heartbeat)

1. Friday 2026-07-17 grading pass — FLAT expected; executor cron is live on
   the coordinator seat.
2. OWNER-QUEUE click-runs — pending owner rulings; no publish click is
   agent-executable.

## Orientation pointers

- [`current-state.md`](current-state.md) — living status ledger; read it
  right after this brief; keep it current as work lands.
- `control/inbox.md` — ORDER protocol: orders stay `status: new` there;
  done-state lives in `control/status.md`.
- [`retro/2026-07-13-coordinator-session.md`](retro/2026-07-13-coordinator-session.md)
  — what worked and what hurt in the latest run (walls, baked lessons).
- [`products/TEMPLATE.md`](products/TEMPLATE.md) — the repeatable idea →
  publish-READY path; copy it per new product so N+1 gets cheaper.
- [`SKILLS.md`](SKILLS.md) — kit skill index; check it before improvising a
  workflow.
- Historical (superseded by this rewrite, kept for archaeology):
  [`retro/2026-07-11-coordinator-retro.md`](retro/2026-07-11-coordinator-retro.md)
  and [`retro/archive-ready-2026-07-11.md`](retro/archive-ready-2026-07-11.md)
  — the 2026-07-11 archive close-out records this brief previously led with.
