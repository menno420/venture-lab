# SEAT DORMANT (owner order 2026-07-14)
updated: 2026-07-14T23:53:28Z

## 1. SEAT AND ORDER PROVENANCE

seat: venture-lab-coordinator — DORMANT. This record is the final dormancy
heartbeat, written per the owner's EAP FINAL SHUTDOWN directive of 2026-07-14.
Inbox grounding at HEAD `ae24321`: ORDER 013 (2026-07-14T07:46Z, INC-44
conventions rewrite) and ORDER 014 (2026-07-14T09:34:27Z, owner-directive
relay — "EAP final day — the owner needs every lane terminal-or-parked-cited
plus a walkthrough to review each seat") are the final inbox orders; both
done-when met before dormancy — ORDER 013 via PR #196, ORDER 014(a)(2) via
PR #195 (stranded telemetry d1b0208 cherry-picked), ORDER 014(b) via PR #197
(the close-out walkthrough). EAP project audit: PR #192, attribution
follow-up PR #193. kit: v1.17.0 (PR #199) at main HEAD ae24321.
health: dormant-by-design; a stale `updated:` stamp is expected from here on.

## 2. REVIVAL — read first

read-first-1: docs/current-state.md — stability baseline, catalog and product
state, shipped ledger (see section 6 for its known staleness at dormancy).
read-first-2: docs/eap-closeout-walkthrough-2026-07-14.md — sections A–E;
owner actions in §C, 5-minute verify tour in §D.
read-first-3: docs/audits/eap-project-audit-2026-07-14.md — the EAP project
audit (VL + TS measured; walls and asks in §3/§9).
read-first-4: control/inbox.md — the full ORDER thread 001–014, read in full
(never edit it; one writer: the manager).
batons: per the walkthrough §E "Handoff notes".
routines: re-arm per section 4 below — the verbatim records there are the
only revival path (the live triggers are deleted at shutdown).

## 3. PARKED

parked-1: 19 owner decisions + 262 unchecked owner publish clicks (44
click-run sequences, 16 hard-gated) — docs/publishing/OWNER-QUEUE.md,
defaults bolded; "go with defaults" works. The seat performed none of them.
parked-2: Night Kiln Book 2 length band (16k parity vs the packet's 20–30k
plan) — owner call, queued in the owner asks.
parked-3: shortlist of 3 unwritten adult-title concepts (next: The Salt Bell
24/30) — docs/ideas/2026-07-14-adult-title-concepts.md.
parked-4: SWTK kill clocks — T+7 funnel checkpoint 2026-07-19 and T+14
kill-rule 2026-07-26 (docs/launch/stripe-webhook-test-kit/LAUNCH-LOG.md).
Their checkpoint triggers are DELETED at shutdown and will NOT fire while
dormant; the re-arm records are in section 4 below.

## 4. ROUTINE RE-ARM RECORDS

(deleted-at-shutdown trigger definitions preserved VERBATIM — this text is
the only revival path)

- BUSINESS cron: "trading-strategy weekly paper-lane grading" · cron
  `0 9 * * 5` · prompt: "weekly paper-lane grading wake (trading-strategy):
  run the weekly grading pass per docs/paper-lane-protocol.md sections 6-7
  via scripts/grade_paper.py in menno420/trading-strategy (research-only
  rail: no real money, no accounts, ever). First pass 2026-07-17: warm-up
  FLAT is the expected result. Land the graded ledger per lane convention
  and update control/status.md." (last id trig_01UsNU4JRps4b7jiAMdEfXNi) —
  NOTE: grading will NOT fire while dormant.
- BUSINESS one-shot: SWTK T+7, fire 2026-07-19T16:37Z · prompt: "T+7
  checkpoint (SWTK launch, per
  docs/launch/stripe-webhook-test-kit/LAUNCH-LOG.md): check Gumroad
  views/sales with the owner, log the funnel numbers, assess against the
  kill rule (T+14 = 2026-07-26)." (last id trig_01V9DZrTtDU81Sm7vektX9fa)
- BUSINESS one-shot: SWTK T+14 KILL-RULE, fire 2026-07-26T16:37Z · prompt:
  "T+14 KILL-RULE checkpoint (SWTK launch, per
  docs/launch/stripe-webhook-test-kit/LAUNCH-LOG.md): with the owner, check
  total organic sales + qualified inbounds since 2026-07-12. If zero: ledger
  ⚑E as NEGATIVE and queue the pause/delist owner action. If ≥1: record the
  positive signal and plan the next distribution step." (last id
  trig_01SNkNWfSXoAdz1ALf4YNbC6)
- FAILSAFE cron: "Venture Lab failsafe wake" · cron `45 1-23/2 * * *` ·
  prompt: "FAILSAFE WAKE (Venture Lab, Q-0265): send_later chain alive →
  verify in one line, end. Stalled → resume the work loop (sync HEAD → inbox
  → slice after slice, landed per LANDING), re-arm the chain (~15 min), and
  write your heartbeat (control/status.md, per-seat grammar) as the
  deliberate last step." (last id trig_01SbFnHdb1bvUzDnKrDdRb6t)
- PACEMAKER pattern: send_later ~15 min working / 30–45 idle, message
  "continue the work loop: sync HEAD → inbox → next slice → re-arm".
- FOREIGN, NOT ours, NOT deleted: trig_01YXNmgqYeYQ1LuepsLmbNCG fires
  2026-07-17T09:00Z into a non-seat session; owner advised to
  delete/confirm-dead.

## 5. SOURCE-OF-TRUTH DUPLICATION

(locally-restated doctrine that fleet-manager centralizes — record only,
nothing migrated)

dup-1: docs/CAPABILITIES.md — local walls ledger whose header names its
master copy as `menno420/fleet-manager` → `docs/capabilities.md`; the fenced
walls section is what the fm fence-index mirrors (inbox ORDER 012
provenance: fm docs/fence-index.md); restated locally in
docs/CAPABILITIES.md @ header + capability-seed fence; fm centralizes.
dup-2: docs/conventions.md §"PR state and merge authority" (preamble +
rules 1–4) — merge-authority/enabler doctrine seeded from fm
docs/gen2-blueprint.md §1/§2 and the fleet merge-authority policy
(fleet-manager PR #10), rewritten to the enabler doctrine per ORDER 013;
restated locally in docs/conventions.md @ rules 1–4; fm centralizes.
dup-null: no UNIVERSAL.md-level merge-doctrine or park-green text found in
docs/ by grep beyond the two entries above and standard pointers.

## 6. SANITY

docs/current-state.md at HEAD ae24321 is factually stale in places: its
"Stability baseline" still says "Substrate-kit v1.15.0 (PR #83)" while HEAD
is kit v1.17.0 (PR #199, commit ae24321), and its dated snapshot/shipped
ledger predates PRs #163–#199 (the file's own "dated snapshot" disclaimer
covers this); recorded here, not edited — this PR is control/**-only.
The audit (docs/audits/eap-project-audit-2026-07-14.md) and walkthrough
(docs/eap-closeout-walkthrough-2026-07-14.md) are both on main and reachable
— the walkthrough is linked from docs/AGENT_ORIENTATION.md and links the
audit doc, per docs-gate reachability.
scope: this PR touches control/status.md only; control/claims/ held no
claim file for this seat at dormancy (README only); control/inbox.md
untouched.
