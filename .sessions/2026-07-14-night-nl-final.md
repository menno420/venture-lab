# Session — Night run: NL-final — the last two NL editions (Harvest Rows + Sweetwater Sea) + packets/keywords/regen (ORDER 011 item 2 tail, owner 2026-07-14 night directive)

> **Status:** `in-progress`

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

(born-red — filled at the flip; this card flips `complete` as the
deliberate LAST step once the close-out is written)

## ⟲ Previous-session review

(owed at flip; previous-session review target:
`.sessions/2026-07-14-night-nl-completion.md`)

## 💡 Session idea

(owed at flip — 💡 required, deduped against `.sessions/2026-07-1*.md`)

## Verification

(owed at flip: `python3 scripts/derive_owner_queue.py` exit 0 + counts,
`python3 bootstrap.py check --strict` green, claim
`control/claims/2026-07-14-night-nl-final.md` removed in the flip commit
per convention)
