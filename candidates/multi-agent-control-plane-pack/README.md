# Multi-Agent Control-Plane Pack

Run 2+ concurrent coding-agent sessions on one codebase without
duplicated work, clobbered status files, or lost orders.

This pack is the coordination layer above single-session discipline: a
small set of markdown conventions — an **inbox** (orders in), a
**status heartbeat** (state out), an **outbox** (asks up), a **claims
ledger** (who is on what), and **session cards** with a born-red gate
(what each session did, provably) — distilled from a repository where
multiple concurrent agent sessions have run it in production across
150+ merged pull requests. Every rule ships with the WHY that made it a
rule, because conventions without rationale get "improved" back into
the failure they prevent.

## What's inside

- `QUICKSTART.md` — install the plane in your repo in ~15 minutes.
- `INCLUDED.md` — full file inventory.
- `guide/` — six chapters, each ending in a Sources footer citing the
  committed production files it was distilled from:
  1. **The control plane** — the topology and the one law (one writer
     per file) everything else derives from.
  2. **The inbox and the ORDER grammar** — append-only orders with a
     parseable header; why `status: new` stays `new` forever.
  3. **The status heartbeat** — heartbeat-before-work, re-stamp-last,
     and the standing ritual that catches orders landing mid-session.
  4. **The claims ledger** — one file per claim; the measured ~98%
     merge-conflict rate of the shared-list alternative.
  5. **The outbox** — routing asks UP without breaking one-writer:
     SIM-REQUEST, WEBSITE-IDEA, INFO markers, ask-then-continue.
  6. **Session cards and the born-red gate** — identity, timestamps,
     and a CI hold that makes an unfinished session unmergeable.
- `templates/` — blank-slate starter files you copy into your own
  repo: `control/README.md`, `inbox.md`, `status.md`, `outbox.md`,
  `claims/README.md`, a claim file, and a session card.

## Requirements

- A git repo and a markdown editor. No runtime, no dependencies, no
  accounts, no network. The conventions are tool-agnostic — they work
  with any agent harness that can read files and commit.

## What this is NOT

- Not single-repo session discipline (checklists, PR habits) — that is
  the layer below this pack, and other products cover it. This is the
  layer that only matters once TWO OR MORE sessions run concurrently.
- Not an owner-approval queue — gating spend/publish actions on a
  human is a different (complementary) surface.
- Not software. There is nothing to execute in this pack; the born-red
  gate chapter shows the CI shape but your CI wiring is your own.

## Provenance

Distilled from committed, production-run files in the seller's own
multi-agent repository; every chapter's Sources footer cites them at
`file@sha`, and the claims-conflict measurement is cited to its
external simulator. Claims are verified by citation — audit the
footers yourself.
