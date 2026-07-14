# Session — Night run: NL-catalog completion — the last three NL editions (ORDER 011 item 2 remainder, owner 2026-07-14 night directive)

> **Status:** `in-progress`

- **📊 Model:** Claude Fable · worker slices · ORDER 011 item 2 remainder (NL completion, night run)
- **started (date -u):** Tue Jul 14 UTC 2026 (night slice)
- **branch:** `claude/night-nl-completion` — anchor branch of the slice;
  translation work may land on sibling branches of this card, per the
  `.sessions/2026-07-13-night-book-variants.md` anchor/sibling precedent.
- **session:** Continuation of ORDER 011 item 2 (control/inbox.md: "New book
  titles + edition variants — EN adult catalog (11 manuscripts) still has
  unexecuted variants; versions are cheap per ORDER 008 item 1") under the
  owner's 2026-07-14 night directive. Tonight's earlier slices took NL
  coverage to **8 of 11** EN adult manuscripts (PRs #175–#178 + packets
  batch #180). This slice completes the NL catalog: complete literary Dutch
  (Netherlands register) editions of the three remaining uncovered
  manuscripts —
  1. *The Salvage Orchard* (`candidates/adult-novels/the-salvage-orchard/en/`,
     15,045w measured) → `versions/nl/`;
  2. *The Seed-Catalogue Courtship*
     (`candidates/adult-novels/the-seed-catalogue-courtship/en/`, 15,133w
     measured) → `versions/nl/`;
  3. *The Morning Door* (Night Kiln Book Two,
     `candidates/adult-novels/the-night-kiln/en/the-morning-door.md`,
     15,995w measured, translated AS WRITTEN — the ⚑ owner length-band
     question in `the-night-kiln/DECISIONS.md` is not touched) →
     `versions/nl-book-2/` (Book Two dirs carry the `-book-2` suffix per the
     title's versions/README convention); NL title pre-named *De Morgendeur*
     by the de-nachtoven NOTES/packet; series terms inherit the de-nachtoven
     glossary unchanged (series-safe rule).
  Each edition ships per the de-papieren-sinaasappel / de-nachtoven
  precedent: one full manuscript file + `NOTES.md` (source pin, honest
  `wc -w`, title decision, glossary, gloss reversions, market note, ⚑ owner
  gates) + a `versions/README.md` row. Follow-through in the SAME batch, per
  the #166 remedy class and the night-book-variants 💡 (batch owed
  follow-throughs against the merged union, ONE regen): 3 NL vetting packets
  in `docs/publishing/vetting/`, keyword-map C4 rows (full-map V057
  first-claim-wins collision scan first), ONE `derive_owner_queue.py` regen,
  and counts-sync to `docs/current-state.md` + `docs/NEXT-SESSION.md` +
  heartbeat (NL coverage 8/11 → 11/11; queue counts move from 19 decisions /
  37 sequences / 213 clicks).
- **walls:** no edits to EN manuscripts (fixes propagate EN → NL, never the
  reverse), `control/inbox.md`, workflows, or triggers; no publish, spend,
  or external action — every publish click stays ⚑ owner-gated in the
  packets' §7. The Night Kiln Book-2 length-band owner question is
  referenced, never altered.

## Results (as landed)

(to be written at flip — manuscripts, measured counts, packet/queue/counts
follow-through, PR numbers)

## ⟲ Previous-session review

previous-session review: (to be written at flip; candidate:
`.sessions/2026-07-14-night-nl-packets.md`, PR #180 — its one-batch/one-regen
discipline is the shape this slice reuses for the three-title remainder.)

## 💡 Session idea

💡 (to be written at flip)

## Verification

(to be written at flip — `python3 bootstrap.py check --strict` + claim
removal per convention)
