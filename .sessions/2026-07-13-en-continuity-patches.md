# 2026-07-13 — EN continuity patches: The Weigh House + Ultramarine (from the NL translation passes)

> **Status:** `in-progress`

One-line summary: close the two EN-source continuity seams the NL
translation passes flagged (Weigh House Ch 2 flat vs Ch 7+ houseboat;
Ultramarine Ch 5 sill vs Ch 8/9 fist), propagate the fixes EN→NL into
*De Waag* and *Weduwenblauw*, and mark both NOTES seams RESOLVED.

Started: Sun Jul 13 2026 (born-red first commit).

## Intent

Run under ORDER 008 (owner night run 2026-07-13, BOOKS clause). The two
NL editions landed tonight (PR #134 De Waag, PR #135 Weduwenblauw) each
flagged one EN-source continuity wobble in their NOTES per the
fixes-propagate-EN→NL rule (carried, not silently repaired). This slice
is the EN-side patch both NOTES asked for, plus the EN→NL propagation so
the editions do not drift.

## Scope

- `candidates/adult-novels/the-weigh-house/en/the-weigh-house.md` —
  standardise Sanne's home on the houseboat on the Kloveniersburgwal
  (the resolution the novella cut already chose and documented in its
  NOTES "Continuity smoothing" section; the master itself puts her dark
  window over the Kloveniersburgwal from Ch 11 on).
- `candidates/adult-novels/the-weigh-house/versions/nl/de-waag.md` —
  same edits, NL register.
- `candidates/adult-novels/ultramarine/manuscript/ultramarine.md` (+ the
  identical paragraph in `manuscript/part-two.md`) — one retrieval line
  in Ch 5 so the treasures leave the shop-window sill in Grietje's fist.
- `candidates/adult-novels/ultramarine/versions/nl/weduwenblauw.md` —
  same line, NL register.
- Both `versions/nl/NOTES.md` — seam marked RESOLVED (2026-07-13),
  honest word counts re-measured.

Walls held: no edits to control/status.md, control/outbox.md,
control/inbox.md, workflows, or triggers; no publish, spend, or external
action; no rewriting beyond the seams.

## Outcome

(filled at flip)

## Model
- **📊 Model:** fable-5 · worker slice · ORDER 008 night-run books lane

Run under ORDER 008.
