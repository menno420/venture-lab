# Marketplace listing copy — Multi-Agent Control-Plane Pack v0.1

> **Status:** `reference`

**Title:** Multi-Agent Control-Plane Pack — run 2+ agent sessions on one repo without chaos

**Short description (≤200 chars, 196):** The coordination layer for
concurrent coding agents: one-writer inbox/status/outbox files, a
one-file-per-claim work ledger, and born-red session cards — with the
production WHY behind every rule.

**Price:** $29 (one-time)

## Description

The moment you run a SECOND agent session on the same codebase, a new
failure class appears: both sessions pick up the same task, both append
to the same status file (merge conflict), and the instruction you gave
one of them evaporates with its chat window. Single-session discipline
doesn't fix any of that — you need the layer above it.

This pack is that layer, distilled from a repository where multiple
concurrent agent sessions have coordinated 150+ merged pull requests
through exactly these files:

- **One law everything derives from:** one writer per file. The manager
  writes the inbox; the lane writes its status and outbox; claims and
  session cards are one-file-per-thing. Violating writer-ownership is
  the only way the protocol can merge-conflict — so it doesn't.
- **An append-only inbox with a parseable ORDER grammar** (id ·
  priority · do · why · done-when) — and the counter-intuitive rule
  that makes it work: `status: new` never flips in the file; done-state
  lives in the lane's heartbeat, and the diff between the two files IS
  the work queue.
- **A status heartbeat convention** — heartbeat-before-work (a silent
  agent is indistinguishable from a dead one), re-stamp-LAST with a
  final inbox re-read (the measured miss: an order landing 15 minutes
  before a heartbeat that never saw it).
- **A one-file-per-claim work ledger** — because the shared "active
  work" list you'd write instead was measured at ~98% merge-conflict
  rate under concurrency vs 0% for one-file-per-claim. Grammar,
  arbitration (first claim merged wins), ~72h expiry.
- **An outbox for asks routed UP** — SIM-REQUEST / idea / INFO markers,
  and the ask-then-continue discipline that keeps a waiting lane from
  becoming a stalled lane.
- **Session cards with a born-red CI gate** — every session's first
  commit declares itself unfinished; CI holds the PR until the card is
  deliberately flipped complete. A session that dies mid-flight leaves
  a resumable record instead of a mystery.

Six chapters explain each surface and — the part you can't get from
reading a template — WHY each rule exists, with the production scars
that made it a rule. Seven blank-slate templates install in ~15
minutes. Every chapter ends in a Sources footer citing the committed
production files it was distilled from — claims verified by citation;
audit the footers yourself.

## What's inside

- `QUICKSTART.md` — the ~15-minute install: copy 5 files, fill one
  writer table, add 4 lines to your agent's standing instructions.
- `guide/` — 6 chapters: the control plane and the one-writer law ·
  the inbox + ORDER grammar · the status heartbeat · the claims ledger
  · the outbox · session cards + the born-red gate.
- `templates/` — 7 starters: `control/README.md` (writer table +
  standing ritual), `inbox.md`, `status.md`, `outbox.md`,
  `claims/README.md`, a claim file, a session card.
- `README.md` + `INCLUDED.md` — orientation + full inventory
  (17 content files).

## Requirements

- A git repo and a markdown editor. No runtime, no dependencies, no
  accounts, no network. Agent-harness-agnostic: the conventions only
  assume your agents can read files and commit.

## What it does NOT do (so you know what you're buying)

- **It ships no software.** There is nothing to execute: the pack is
  conventions + rationale + templates. The born-red chapter shows the
  CI gate's shape, but you wire your own CI.
- It is not single-repo session discipline (PR habits, checklists) —
  that's the layer below, covered by the seller's Agent-Workflow
  Template Pack. This pack only earns its price once you run 2+
  concurrent sessions.
- It is not an owner-approval/spend-gating queue — that is the
  seller's Owner-Click Queue Kit; the boundary is stated in both
  listings. This pack is agent-to-agent coordination.
- The production evidence is the seller's own repository (cited
  file@sha in every chapter footer, with real PR events); no external
  fleet has run these exact files. The claims-ledger conflict
  measurement is cited to its external simulator, not re-run in-pack.
- Nothing in this pack was machine-verified beyond format checks
  (UTF-8/markdown/inventory) — it is a document pack; there is no test
  suite because there is nothing to test.

## FAQ

**Can't I just read a public repo that runs this and copy it?**
Yes — that is honestly the free substitute, and the README says so.
What you're paying for: the extraction is done (repo-specific noise
stripped, blank-slate templates), and each rule carries the WHY and
the failure it prevents — the part that stops the next contributor
from "simplifying" the inbox into a shared TODO list again.

**Does this work with [my agent framework]?**
If your agents can read repo files and make commits, yes. Nothing here
calls any API. The conventions have run in production under scheduled
wakes, parallel worker sessions, and human-in-the-loop sessions alike.

**How is this different from the seller's field manual?**
The Agent Fleet Field Manual ($39) teaches fleet operations broadly in
prose, including a chapter on this territory; this pack is the
narrow, working version of the coordination layer — installable files
+ per-rule rationale. Disclosed cross-sell, both directions.

**Refunds / support / license:** [owner-to-set — storefront defaults;
suggested: 14-day no-questions refund, single-team license, email
support best-effort.]
