# Session — Night run: NL-catalog completion — the last three NL editions (ORDER 011 item 2 remainder, owner 2026-07-14 night directive)

> **Status:** `complete`

- **📊 Model:** Claude Fable · worker slices · ORDER 011 item 2 remainder (NL completion, night run)
- **started (date -u):** Tue Jul 14 UTC 2026 (night slice)
- **closed (date -u):** Tue Jul 14 02:40 UTC 2026 (finalizer flip)
- **branch:** `claude/night-nl-completion` — anchor branch of the slice;
  translation work landed on sibling branches of this card, per the
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
  follow-throughs against the merged union, ONE regen): NL vetting packets
  in `docs/publishing/vetting/`, keyword-map C4 rows (full-map V057
  first-claim-wins collision scan first), ONE `derive_owner_queue.py` regen,
  and counts-sync to `docs/current-state.md` + `docs/NEXT-SESSION.md` +
  heartbeat. **Coordinator scope-add at the finalizer slice:** a sibling
  session's PR #182 (merged `beffdf0`) added a new EN title *The Sweetwater
  Sea* whose DECISIONS.md records its vetting packet as an owed follow-up —
  that packet + its keyword rows were added to this session's batch, making
  it 4 packets, not 3.
- **walls:** no edits to EN manuscripts (fixes propagate EN → NL, never the
  reverse), `control/inbox.md`, workflows, or triggers; no publish, spend,
  or external action — every publish click stays ⚑ owner-gated in the
  packets' §7. The Night Kiln Book-2 length-band owner question is
  referenced, never altered.

## Results (as landed)

- **3 complete NL editions** (each all chapters/parts in finished prose,
  own NOTES.md with source pin, honest `wc -w`, title decision with
  collision scan, glossary, gloss reversions, market note, ⚑ gates):
  - *Liefde in de kantlijn* (The Seed-Catalogue Courtship) — **15,633w**
    (+3.3% over the 15,133w EN source), all 4 Parts / 52 document blocks,
    **PR #183 MERGED** (`24a17d3`), branch `claude/night-nl-completion-2`.
  - *De Morgendeur* (The Morning Door, Night Kiln Book Two) — **16,730w**
    (+4.6% over the 15,995w EN source, translated AS WRITTEN; length-band
    ⚑ untouched), series glossary inherited from De Nachtoven's NL NOTES,
    **PR #185 MERGED** (`3af3a95`), branch `claude/night-nl-completion-3`.
  - *De geborgen boomgaard* (The Salvage Orchard) — **15,750w** (+4.7%
    over the 15,045w EN source; hen/hen/hun pronoun strategy documented in
    NOTES.md), **anchor PR #184** (this branch, commit `b66252c`) — open
    with the enabler's auto-merge armed; lands on this card's flip.
  All counts re-verified by `wc -w` on the working tree at the finalizer
  merge of `origin/main` (commit `5c2be57`).
- **4 vetting packets** in `docs/publishing/vetting/` (7-section
  de-nachtoven form; §7 `OWNER-GATE` heading parseable; all owner clicks
  queued, none performed): `de-geborgen-boomgaard.md` (collision Low),
  `liefde-in-de-kantlijn.md` (collision Low; first Romance-storefront
  claim), `de-morgendeur.md` (collision Low; pre-named title; Book-2
  length-band ⚑ carried forward untouched as the sequence's blocking row),
  and `the-sweetwater-sea.md` (the scope-add: manuscript-first EN packet,
  15,243w re-measured; collision recorded honestly as Low exact-title with
  **Moderate search-intent drift** — "Sweetwater Sea" is the standing
  Great Lakes / Lake Huron epithet (Champlain's *La Mer Douce*, a Parker
  shipwreck history, a documentary) — subtitle *"A novella of the
  Zuiderzee"* made mandatory as the mitigation).
- **Keyword-map rows** (`docs/publishing/keyword-map.md`): full-map V057
  first-claim-wins scan run FIRST — no existing claim touched, no reroutes
  needed. Added: 2×3 browse-node first-claims per C4 (Climate Fiction +
  Urban Life → De geborgen boomgaard; Clean & Wholesome + Later in Life →
  Liefde in de kantlijn; Sea Stories + Small Town & Rural → The Sweetwater
  Sea), the map's **first series node-share** (De Morgendeur rides De
  Nachtoven's two nodes per the §3 series rule — separate listing, no
  duplicate row), 28 keyword ownership rows (7 NL each for the three NL
  editions in the C4 namespace — De Morgendeur's seven all NEW phrases,
  none of Book One's re-claimed — plus 7 EN rows for Sweetwater), C3
  extended with the **fourth Netherlands era-register** (interwar
  Zuiderzee-closure → The Sweetwater Sea), §3 rows annotated. Watched
  adjacencies recorded in the C2 pattern (sciencefiction / feelgood /
  gezellige / zonder-geweld / Netherlands / Holland stems) — full phrases
  all distinct.
- **ONE owner-queue regen** (`python3 scripts/derive_owner_queue.py`,
  exit 0): **19 decisions / 41 click-run sequences / 241 owner clicks
  (14 hard-gated), 43/43 inputs parsed clean** — from the PR #180 baseline
  of 19 / 37 / 213 (11 hard-gated), 39/39. (One parse-grammar lesson: an
  inline ⚑ in a §7 numbered step is decision grammar — the Morgendeur
  length-band step was rephrased as sequencing prose so the standing owner
  question isn't double-queued as a defaultless D-item.)
- **Counts-sync** (re-derived by grep, not memory): `docs/current-state.md`
  — adult novels 10 titles/12 EN manuscripts → **11 titles/13 EN
  manuscripts** (Sweetwater added); the stale "4 adult NL editions" bullet
  → **11 adult NL editions** with per-title counts; vetting packets 38 →
  **42** (28 book + 13 product + 1 probe); large-print specs 5 → **13**
  (the stale line predated PR #172's 8-spec bundle); owner-queue paragraph
  to the new counts. `docs/NEXT-SESSION.md` — same four corrections in its
  catalog snapshot + owner-queue paragraph.
- **Heartbeat:** one dated night-progress line appended to
  `control/status.md` (2026-07-14T02:40Z), stating only what this slice
  did, with the Sweetwater scope-add and the honest collision verdict
  named.

## ⟲ Previous-session review

previous-session review: `.sessions/2026-07-13-night-book-variants.md`
(ORDER 011 item 2, anchor PR #172 + sibling NL PRs #175–#178) — its
anchor/sibling shape is exactly what this session reused: born-red anchor
card holding the gate red while card-less sibling translation PRs merge
green, and its 💡 (batch the owed NL follow-throughs into ONE session
against the merged union, ONE regen) was consumed once by PR #180 and
deliberately re-applied here for the remainder batch — the shape held both
times, drift-free by construction. Honest nit: its deferral prose named
the owed artifacts but recorded no durable owed-LIST location, and its
"NL coverage 8 of 11" numerator/denominator was already out of step with
the same night's heartbeat ("12 EN adult manuscripts on file") — this
session's scout had to re-derive the remainder by grep because no ranked
remainder list existed anywhere, and tonight's counts-sync had to restate
both counts from the tree. Deferrals should name the file that carries the
owed list, not just the debt.

## 💡 Session idea

💡 **Pre-name the NL title in every new EN adult title's DECISIONS.md at
write time.** Tonight's cheapest title decision was the one made a day
early: *De Morgendeur* was pre-named by Book One's NL NOTES + packet §7,
so the Book Two slice inherited a scanned, series-consistent title for
free — while *De geborgen boomgaard* and *Liefde in de kantlijn* each cost
a full alternatives-considered, three-query collision pass in the night
slice. The Sweetwater Sea's DECISIONS.md already does this ad hoc (*De
zoete zee*, with the zoet/sweetwater pun reasoning recorded). Make it one
convention line in the adult-novels lane README/template: every new EN
title's DECISIONS.md records its natural NL title + a one-query scan, so
translation slices start from a scanned candidate instead of re-deriving
one at 2 a.m. Deduped against `.sessions/2026-07-1*.md` 💡 lines:
night-book-variants batched owed follow-through (consumed); night-nl-packets
batches the EN concept-packet graduations; night-new-title wants
per-concept outcome rows in ideas docs; night-v020-probe fixes HARD-GATED
rendering; nl-editions-vetting hoists shared clicks — no card proposes
pre-naming translations at EN DECISIONS time.

## Verification

- `python3 scripts/derive_owner_queue.py` exit 0, 43/43 inputs clean
  (output quoted in Results).
- `python3 bootstrap.py check --strict` green at flip (run after the flip
  commit was staged; output in the session report).
- Claim `control/claims/2026-07-14-night-nl-completion.md` removed in the
  flip commit per convention.
