# Session — Night run: NL-final — the last two NL editions (Harvest Rows + Sweetwater Sea) + packets/keywords/regen (ORDER 011 item 2 tail, owner 2026-07-14 night directive)

> **Status:** `complete`

- **📊 Model:** Claude Fable · worker slices · ORDER 011 item 2 tail (NL final, night run)
- **started (date -u):** Tue Jul 14 02:51 UTC 2026 (night slice)
- **branch:** `claude/night-nl-final` — anchor branch of the slice, per the
  `.sessions/2026-07-14-night-nl-completion.md` anchor/sibling precedent.
- **session:** Continuation of ORDER 011 item 2 (control/inbox.md: "New book
  titles + edition variants — EN adult catalog … versions are cheap per
  ORDER 008 item 1") under the owner's 2026-07-14 night directive. The
  NL-completion slice (PRs #183/#184/#185) took the NL catalog to 11 of 13
  EN adult manuscripts and named the EN-only remainders explicitly
  (`control/status.md` 2026-07-14T02:40Z night-progress line): *The Harvest
  Rows* (Night Kiln Book 3, `the-night-kiln/en/the-harvest-rows.md`,
  23,334w measured) and *The Sweetwater Sea*
  (`the-sweetwater-sea/en/the-sweetwater-sea.md`, 15,243w measured,
  PR #182). This slice finishes the line: complete literary Dutch
  (Netherlands register) editions of both —
  1. *The Harvest Rows* → `the-night-kiln/versions/nl-book-3/` (Book-N
     dirs carry the `-book-N` suffix per the title's versions/README
     convention); series terms inherit the De Nachtoven / De Morgendeur
     NL glossary unchanged (series-safe rule); translated AS WRITTEN —
     the ⚑ owner length-band question in `the-night-kiln/DECISIONS.md`
     is not touched; NL title to be derived series-consistently (no
     pre-name exists for Book 3 — the pre-naming 💡 from the
     nl-completion card postdates the Book-3 DECISIONS entry) with the
     full alternatives-considered, three-query collision scan.
  2. *The Sweetwater Sea* → `the-sweetwater-sea/versions/nl/`; NL title
     **pre-named *De zoete zee*** (subtitle *Een novelle van de
     Zuiderzee*) by the title's DECISIONS.md and its vetting packet §3;
     the packet's §2 mandatory-subtitle finding (Great Lakes epithet
     drift) carries into the NL listing posture.
  Each edition ships per the de-nachtoven / de-morgendeur precedent: one
  full manuscript file + `NOTES.md` (source pin, honest `wc -w`, title
  decision, glossary, gloss reversions, market note, ⚑ owner gates) + a
  `versions/README.md` row (creating `the-sweetwater-sea/versions/` where
  none exists). Follow-through in the SAME batch, per the #166 remedy
  class and the night-book-variants 💡 (batch owed follow-throughs
  against the merged union, ONE regen): NL vetting packets in
  `docs/publishing/vetting/`, keyword-map C4 rows (full-map V057
  first-claim-wins collision scan FIRST; De Morgendeur's series
  node-share precedent applies to Book 3; no inline ⚑ inside §7 numbered
  steps for the standing length-band question — sequencing prose only,
  per the nl-completion parse-grammar lesson), ONE
  `derive_owner_queue.py` regen (baseline 19 decisions / 41 sequences /
  241 clicks, 14 hard-gated, 43/43 clean), and counts-sync to
  `docs/current-state.md` + `docs/NEXT-SESSION.md` + heartbeat.
- **walls:** no edits to EN manuscripts (fixes propagate EN → NL, never
  the reverse), `control/inbox.md`, workflows, or triggers; no publish,
  spend, or external action — every publish click stays ⚑ owner-gated in
  the packets' §7. The Night Kiln length-band owner question is
  referenced, never altered.

## Results (as landed)

All on PR #186 (`claude/night-nl-final`, this anchor card born-red as its
first commit). **NL catalog 13/13 complete.**

- ***De zoete zee*** — complete Dutch edition of The Sweetwater Sea:
  `candidates/adult-novels/the-sweetwater-sea/versions/nl/de-zoete-zee.md`
  (honest `wc -w` **15,467**, 12 chapters, +1.5% over the 15,243w EN
  source) + `versions/nl/NOTES.md` + new `versions/README.md` (dir created
  where none existed). Title pre-named by DECISIONS.md (subtitle *Een
  novelle van de Zuiderzee*, mandatory per the EN packet's §2 ruling).
  Packet `docs/publishing/vetting/de-zoete-zee.md` — **collision-scan
  verdict: Moderate** (the catalog's first non-Low NL scan: Duyns's
  exact-title photo book + Kok's near-exact in-register novel, all
  disclosed; title kept, subtitle MANDATORY, ⚑ ratification queued as a
  genuine decision with the findings in view, bare `zoete zee` deliberately
  not keyword-drafted).
- ***De Oogstslag*** — complete Dutch edition of The Harvest Rows (Night
  Kiln Book 3):
  `candidates/adult-novels/the-night-kiln/versions/nl-book-3/de-oogstslag.md`
  (honest `wc -w` **24,655**, 12 chapters, +5.7% over the 23,334w EN
  source, translated AS WRITTEN — Book-2 length-band ⚑ untouched) +
  `nl-book-3/NOTES.md` + series `DECISIONS.md` entry (title derived
  decide-and-flag, no pre-name existed; alternatives + three-query scan
  recorded) + `versions/README.md` row. Packet
  `docs/publishing/vetting/de-oogstslag.md` — **collision-scan verdict:
  Low** (no same-named book; bare-*oogst* shelf noise only; subtitle
  settles the *slag*-as-battle misread).
- **Keyword map** (`docs/publishing/keyword-map.md`): 14 new NL C4 rows
  (7 + 7); full-map V057 first-claim scan run clean twice (worker proposal
  + re-run at apply), zero collisions, no spares used. De zoete zee shares
  The Sweetwater Sea's two browse nodes (straight C4); De Oogstslag rides
  De Nachtoven's two per the §3 series rule — the map's second series
  node-share. §3 Harvest Rows reservation row + edition-sharing note
  updated.
- **ONE `derive_owner_queue.py` regen + counts-sync**: **19 decisions /
  43 sequences / 256 clicks (16 hard-gated), 45/45 inputs clean** (from
  19/41/241, 14 hard-gated, 43/43). Synced `docs/current-state.md` +
  `docs/NEXT-SESSION.md` (NL editions 11 → 13, packets 42 → 44) and fixed
  the pre-existing night-kiln `versions/README.md` intro drift ("two
  complete EN novellas" → three EN + three NL). Heartbeat night-progress
  line appended to `control/status.md` (2026-07-14T03:40Z).

## ⟲ Previous-session review

Reviewed `.sessions/2026-07-14-night-nl-completion.md` (previous-session
review): its recorded regen baseline (19/41/241, 14 hard-gated, 43/43) and
its keyword/series precedents were exact and directly reusable — tonight's
scope needed zero discovery because that card named the two EN-only
remainders explicitly. Honest nit: its pre-naming 💡 was right but landed
one book too late — Book 3's DECISIONS entry predates it, so *De
Oogstslag* still cost this slice a full alternatives-considered title
derivation, exactly the cost the 💡 exists to remove; the convention line
it proposed is still not written into the lane template.

## 💡 Session idea

💡 **Promote the Night Kiln NL glossary to one series-canonical file.**
Tonight's Book 3 translation had to inherit series terms scattered across
two files — Book One's base table (`versions/nl/NOTES.md`) plus Book Two's
additions (`versions/nl-book-2/NOTES.md`) — and now adds a third additive
table in `nl-book-3/NOTES.md`; a Book 4 slice would reconcile three tables
before translating a line. One canonical `versions/nl/SERIES-GLOSSARY.md`
(per-book NOTES keep only their own coinages and point at it), appended in
the same commit as each new edition, makes series-safe rendering a
one-file lookup and turns glossary drift into a merge conflict instead of
a silent divergence.

## Verification

- `python3 scripts/lint_owner_gates.py` → `owner-gate-lint: OK — 45
  input(s) clean` (exit 0); zero inline ⚑ inside either packet's §7
  numbered steps (parse-grammar rule held).
- Both manuscripts: exactly 12 chapter headings each; honest `wc -w`
  15,467 / 24,655 re-measured at integration.
- `python3 scripts/derive_owner_queue.py` exit 0 — counts above, 45/45
  parsed clean, manual-review empty.
- `python3 bootstrap.py check --strict` green at flip (run post-flip,
  recorded in PR #186).
- Claim `control/claims/2026-07-14-night-nl-final.md` removed in this
  flip commit per convention.
