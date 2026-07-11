# venture-lab

> **Status:** `binding` — lane identity. Seeded 2026-07-09 by the fleet manager
> from the gen-2 blueprint (`menno420/fleet-manager` `docs/gen2-blueprint.md`).

**venture-lab is the fleet's first gen-2 "born-right" lane** — the pilot of the
seed standard that prevents the ~13 failure classes every gen-1 lane paid a tax
rediscovering. The conventions here are not aspirational: they were extracted
from the gen-1 fleet's own retros and are binding from commit #1.

## Mission

**Find and validate the cheapest credible path to first revenue.**

Agents build, the owner clicks. Systematically generate, score, and validate
candidate ventures; ship the smallest real artifact that can earn a first
dollar; keep an honest ledger of what each candidate actually costs and
returns. **Honest negative results are deliverables** — "candidate X cannot
reach revenue without spend Y" is a shipped finding, not a failure.

Scoring is **distribution-first** (every candidate names its
first-ten-customers path or scores down automatically) with **per-candidate
token-cost accounting** (every candidate carries a running cost line, so
return-on-agent-labor is measurable, not vibes).

## Hard rails (non-negotiable)

**NO spend, NO account creation, NO publishing, NO payment flows without an
explicit owner action** — every such step is queued click-level under
⚑ needs-owner, never performed.

## Where things live

| Path | What it is |
|---|---|
| [`control/`](control/) | Manager↔lane coordination — `inbox.md` (manager-written orders), `status.md` (lane-written state). Protocol: [`control/README.md`](control/README.md). |
| [`docs/conventions.md`](docs/conventions.md) | Repo conventions — **override harness defaults**. Read before any PR. |
| [`docs/CAPABILITIES.md`](docs/CAPABILITIES.md) | What sessions CAN do (recipes) — read before declaring anything impossible. |
| [`docs/PLATFORM-LIMITS.md`](docs/PLATFORM-LIMITS.md) | Verified walls with exact error text — probing a documented wall twice is a bug. |
| [`docs/corpus/`](docs/corpus/) | Input material seeded by the manager (opening corpus: the venture shortlist). |
| [`docs/research/`](docs/corpus/venture-shortlist-2026-07-09.md) | Lane-produced evaluations and venture ledgers (created by ORDER 001). |
| [`docs/review-queue.md`](docs/review-queue.md) | Post-merge review ledger — merge-then-flag, never wait-for-review. |
| [`docs/retro/QUESTIONS.md`](docs/retro/QUESTIONS.md) | Standing self-review questions, planted day 0. |
| [`claims/`](claims/) | Claim-before-build files, one per claim. |

## First session duties (in order)

1. Kit adoption: substrate-kit adopted and `python3 bootstrap.py check --strict`
   green **before any domain work**.
2. Walking skeleton: one trivial change through the FULL merge path
   (branch → PR → CI → auto-merge lands it) in the first 20 minutes.
3. ORDER 001 in [`control/inbox.md`](control/inbox.md).
