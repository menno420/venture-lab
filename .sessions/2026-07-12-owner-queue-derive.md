# 2026-07-12 — Derive owner queue from vetting packet §7 blocks (PR #91 card idea)

> **Status:** complete

One-line summary: built `scripts/derive_owner_queue.py` (stdlib-only,
always-exit-0, tolerant parser) + the generated
`docs/publishing/OWNER-QUEUE.md` (4 decisions with bolded defaults, 22 owner
clicks across 4 sequences, 5 of 5 inputs parsed clean) + the README index
row — PR #101.

⚑ Self-initiated: this slice was self-generated from PR #91's session-card
💡 idea (`.sessions/2026-07-12-slow-word-vetting.md`) — derive the ⚑ owner
queue from packet §7 state instead of hand-maintaining it.

## Scope

One work increment: parse the §7 / ⚑ OWNER-GATE blocks across
`docs/publishing/vetting/*.md` plus ⚑ OWNER-flagged conflicts in
`docs/publishing/keyword-map.md`, and regenerate
`docs/publishing/OWNER-QUEUE.md` deterministically (decisions first — each
with a bolded default so "agree" is a one-word owner reply — then the
paste-ready click-run sequences; unparseable inputs listed under Manual
review, never normalized or edited). No packet was edited; no publish,
spend, account, or external action; `control/status.md`,
`control/outbox.md`, and triggers untouched.

## Outcome

- `scripts/derive_owner_queue.py` — mirrors `check_ledger_drift.py`
  conventions (stdlib-only, graceful skips, ALWAYS exit 0, clear stdout).
  Decision = a §7 OWNER-ACTION numbered step carrying an inline ⚑; click =
  a `- [ ] ⚑ **Owner:**` checkbox; map conflict = a `### C<N>` section
  whose body carries `⚑ OWNER`. No titles hardcoded.
- `docs/publishing/OWNER-QUEUE.md` regenerated: D1 Painted Stones
  illustration gate (default **Park (C)**), D2 Weigh House subtitle
  (default **"An Amsterdam Crime Novel"**), D3 Ultramarine rename (default
  **The Widow's Blue — "A Novel of Delft, 1654"**), D4 keyword-map C1
  category swap (default **Women's Fiction → Domestic Life**); then the
  Slow Word / Weigh House / Ultramarine click-runs with Painted Stones
  hard-gated last. Output verified byte-identical across re-runs.
- Parse coverage: 5 of 5 inputs clean; Manual-review section empty.
- Index row added to `docs/publishing/README.md`.

## 💡 Session idea
💡 **Owner-decision log + queue consumption.** OWNER-QUEUE.md now states the
asks, but the owner's ANSWERS arrive in chat and evaporate — nothing durable
records "D3: agreed, The Widow's Blue" or feeds it back. Add a tiny
append-only `docs/publishing/DECISIONS-LOG.md` convention (one line per
owner ruling: D-id · choice · date · where the owner said it) that
`derive_owner_queue.py` reads on its next run to move decided items out of
the open queue into a "Decided" section — closing the loop so the queue
shrinks as the owner rules, instead of re-asking forever.

## Previous-session review
previous-session review: `.sessions/2026-07-12-keyword-allocation-map.md`
(PR #100) — genuine strength: it turned packet-isolation into a claims
discipline (28 keywords + 8 categories reproduced verbatim, conflicts
adjudicated C1–C3 with the disputed one honestly ⚑-parked rather than
retro-editing a shipped packet); one honest nit: its ⚑ C1 ask lived only
inside the map's §2 where an owner skimming for "what do I decide?" may
never look — exactly the scatter this slice's derived queue now sweeps into
one list (C1 parses out as D4).

## Model
- **📊 Model:** Fable 5 · worker · venture/publishing
