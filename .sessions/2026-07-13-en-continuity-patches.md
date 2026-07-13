# 2026-07-13 — EN continuity patches: The Weigh House + Ultramarine (from the NL translation passes)

> **Status:** `complete`

One-line summary: close the two EN-source continuity seams the NL
translation passes flagged (Weigh House Ch 2 flat vs Ch 7+ houseboat;
Ultramarine Ch 5 sill vs Ch 8/9 fist), propagate the fixes EN→NL into
*De Waag* and *Weduwenblauw*, and mark both NOTES seams RESOLVED.

Started: Sun Jul 13 2026 (born-red first commit `7ca7570`).
Closed: Sun Jul 13 2026. PR #136.

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

- **Weigh House seam — FIXED.** Verified real at HEAD `79e7752`: Ch 2 put
  Sanne in a present-day Prinsengracht flat while Ch 7/10/12/16 live on
  the houseboat (Joke a mooring neighbour; Slootweg's offer names "your
  houseboat, the mooring"; Ch 11 already has "her own dark window over
  the Kloveniersburgwal"). Standardised on the houseboat on the
  Kloveniersburgwal — the resolution the novella cut documented in its
  NOTES "Continuity smoothing" section — using the novella's own
  phrasing back-ported. Six sites in the EN master (Ch 2 x3, Ch 3, Ch 7,
  Ch 16), mirrored one-for-one in `versions/nl/de-waag.md` ("De woonboot
  lag aan de Kloveniersburgwal …"; kajuit / boot for the dark-flat and
  passing mentions; "een rompdikte boven het water" for "high and dry").
- **Ultramarine seam — FIXED.** Verified real at HEAD: Ch 5 left the
  treasures on the shop-window sill the morning of the donderslag; Ch
  8/9 carry them "out of the ruin in her fist" with no retrieval line.
  Added the one line the NL NOTES asked for — "Then she gathered them
  back into her fist, all four, the way she always carried them; the
  sill was for the counting, not the keeping." — in
  `manuscript/ultramarine.md` AND the identical paragraph in
  `manuscript/part-two.md`; NL mirror "Toen schoof ze ze terug in haar
  vuist, alle vier …" in `versions/nl/weduwenblauw.md`.
- Both `versions/nl/NOTES.md` seams marked **RESOLVED 2026-07-13**;
  honest word counts re-measured post-patch (EN 36,427 / 27,890; NL
  36,997 / 28,464).
- Follow-up flagged, not edited: the serial edition's
  `ultramarine-part-2.md` still carries the pre-patch Ch 5 paragraph
  verbatim (noted in the Ultramarine NL NOTES and the PR body).
- `bootstrap.py check --strict`: only the designed born-red HOLD
  pre-flip. PR #136 opened READY, not draft; per tonight's owner rule
  the seat leaves it OPEN if auto-merge does not arm.

## 💡 Session idea
💡 **Verbatim splits should be generated, not stored.** Tonight's
one-line Ultramarine fix had to be applied twice inside `manuscript/`
(ultramarine.md + part-two.md) and STILL left a third verbatim copy
stale (`versions/serial-edition/ultramarine-part-2.md`) — every
continuity patch now fans out over N hand-kept copies of the same
paragraph. Either derive the splits mechanically (a tiny
`build-editions.py` that cuts part files and serial parts from the
single master at known headings, run in CI), or add a drift check that
greps shared paragraphs across master/splits and goes red when they
diverge. Distinct from #134's FINDINGS.md idea (that routes *defect
reports* into the master; this keeps *verbatim derived copies* from
rotting after the master is patched) and from #131's shared-click
hoisting and #135's blocked-titles ledger.

## Previous-session review
previous-session review: `.sessions/2026-07-13-ultramarine-nl.md`
(PR #135) — genuine strength: its NOTES "Known EN-source wobbles"
section did not just flag the sill/fist seam, it pre-specified the fix
shape ("a one-line EN clarification would close the seam") with chapter
anchors and the workability analysis, so tonight's patch was a pure
apply with zero re-derivation; honest nit: having just CREATED the
serial edition the same night, it did not note that the seam paragraph
lives verbatim in `manuscript/part-two.md` and
`serial-edition/ultramarine-part-2.md` too — tonight's slice had to
rediscover the fan-out by grep, and the serial copy is now the one
stale holdout.

## Model
- **📊 Model:** fable-5 · worker slice · ORDER 008 night-run books lane

Run under ORDER 008.
