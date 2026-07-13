# Session — The Seed Catalogue Courtship (adult epistolary romance, EN)

> **Status:** `complete`

- **📊 Model:** fable-5 · BOOKS-lane landing worker · day run 2026-07-13
- **session:** day-run BOOKS clause — first complete manuscript for a round-2 vetted concept
- **applied:** candidates/adult-novels/the-seed-catalogue-courtship/{en/the-seed-catalogue-courtship.md,DECISIONS.md}
- **verify:** `python3 bootstrap.py check --strict`
- **started:** 2026-07-13T10:21Z
- **closed:** 2026-07-13T10:52Z

## ⟲ Previous-session review
Concept lane state inherited clean: the seed-catalogue-courtship vetting
packet (`docs/publishing/vetting/the-seed-catalogue-courtship.md`, PR #143)
parks at "no manuscript" (§3/§5 flag the true length as unconfirmed) — this
session is that write-slice. Base was fresh origin/main (f15e9f1, includes
#143–#150); premise check clean: no
`candidates/adult-novels/the-seed-catalogue-courtship/` at HEAD, and the only
live claims (`round2-idea-packets`, `2026-07-13-night-report`) covered
disjoint surfaces. One sibling ran in parallel on
`claude/salvage-orchard-manuscript` (landed as #151 mid-run; merged in at
084192e — zero path overlap, by the zero-shared-surface construction). Direct
review of `.sessions/2026-07-13-marmalade-post-manuscript.md`: its length
discipline (book-parity 15k–16k wins over the packet's larger §3 plan, delta
stated in card + DECISIONS.md, never padded) was adopted here verbatim — this
packet plans ~30k–40k, and the same honest fork applied. Its under-floor
repair rule (inherited from marginalia: added words go where quality is
thinnest, not where padding is easiest) was executed structurally: the 9,071-
word first draft was expanded to 15,133 by ADDING fourteen documents where
the middle was thinnest (the Speed history, the daughter's inspection, the
harvest and lotting letters, the child's last order, the unsent draft,
Dilys's intervention), never by inflating existing ones. Honest nit on the
marmalade card: its Outcome cites deleting
`control/claims/marmalade-post-manuscript.md` but the file it actually
carried (and deleted) was the date-prefixed
`2026-07-13-marmalade-post-manuscript.md` — harmless, but claim filenames in
Outcome prose should match the ledger exactly, since the claims README makes
`ls` the only index. Formatting conventions (front-matter shape, ⁂ scene
breaks, DECISIONS.md) inherited from the weigh-house → night-kiln →
paper-orange → marmalade-post line, adapted to epistolary form (documents,
not chapters, carry the headings).

## 💡 Session idea
Run under the day-run BOOKS lane (owner day run 2026-07-13). Write the FIRST
COMPLETE MANUSCRIPT for **The Seed Catalogue Courtship** — the adult
epistolary-romance (clean & wholesome) concept vetted in
`docs/publishing/vetting/the-seed-catalogue-courtship.md` (landed via PR
#143, collision None→Low), which parks at "no manuscript"; this session is
the write-slice that unparks it. Honor the packet: title + subtitle *"A
Novel in Letters"* (§1), the Edith Prowse / walled-garden premise across one
full growing year (§3, pitch), and the §6 blurb promises on the page (order
No. 4,117, "What would you plant, if it were yours?", order forms + packet
instructions + letters, "more in the margin than on the line"). Epistolary
contract: told entirely in documents, two distinct voices, real arc
(connection, obstacle, rupture, earned resolution), warm, literate,
closed-door. Target 15,000–16,000 words (book-parity default; packet §3
plans ~30k–40k — delta flagged honestly here and in DECISIONS.md). One READY
PR, left OPEN on green.

## 💡 Idea (deduped vs all 2026-07-13 cards)
**A packet's pitch and blurb are a PROMISE MANIFEST — extract it at
write-slice start and grep it at flip, in both directions.** This packet hid
three binding textual constraints outside any checklist row: a hard NEGATIVE
one buried mid-pitch ("a late-life love story that **never once says the
word**" — an in-book banned-inflection rule), hard POSITIVES in §6 (the
margin question must appear *verbatim*, order "No. 4,117" must be the real
number on the page, "almost relieved" is a beat the reader was promised),
and a spelling regime in §1 (UK "Catalogue", zero "catalog"). The draft
genuinely violated the negative once — the word appeared in Edith's hand on
a seed packet, lampshaded — and only a pre-flip `grep -i "love"` caught that
"says it exactly once, knowingly" is still not "never once says it."
Cheap fix: write-slices open by extracting a 5-line manifest from packet
§1/pitch/§6 (required-verbatim strings; banned inflections; locked
spellings) and close by grepping both directions — required strings present,
banned strings absent. Deduped: distinct from salvage-orchard's
forbidden-stem checker (CROSS-book register disjointness, keyword stems in
prose), pepper-ledger's premise-departure register (recording deliberate
departures after the fact), paper-orange-graduation's length single-source
(numeric plan forking), glass-rectory's chronology ledger (internal dates),
and marginalia/marmalade's clue-audit rule (where to add words) — this is
the packet's own PROSE making testable promises about the manuscript's
text, positive and negative, currently enforced by nothing but close
reading of a pitch paragraph.

## Outcome
- Complete manuscript delivered:
  `candidates/adult-novels/the-seed-catalogue-courtship/en/the-seed-catalogue-courtship.md`
  — *A Novel in Letters*, four parts (Catalogue Weather / The Growing
  Season / Lifting Season / Winter Work), 50+ documents, full arc, THE END.
  Honest count: `wc -w` = **15,133** (includes front matter and part
  headings), inside the 15,000–16,000 brief band. Packet §3 plans ~30k–40k;
  the run's book-parity default won — flagged here, in DECISIONS.md, and in
  the PR body, not papered over.
- Epistolary contract kept: told entirely in order forms with marginalia,
  compliments slips, letters, annotated seed-packet instructions, a
  solicitor's letter, annotated estate agent's particulars, a measured
  garden plan, a child's last order, the sale catalogue, the auctioneer's
  settlement account (the rupture arrives as a business document), an
  unsent draft, a third-party letter (Dilys), a hand-sewn one-copy seed
  list (the proposal), an order form (the acceptance), and a printed trade
  leaflet (the closed-door coda). Two distinct voices throughout (Edith:
  catalogue-writer's prose behind firm formality, sign-off dial lampshaded;
  Henry: numbered engineer's reports, margin postscripts).
- Packet promises on the page: §6 blurb beats all delivered (order
  No. 4,117; the margin question verbatim; "almost relieved"; "more in the
  margin than on the line" echoed in-text); §1 subtitle + UK spelling kept
  (zero "catalog"); the pitch's "never once says the word" honored as a
  hard constraint — zero in-document occurrences of the word in any
  inflection (grep-verified; the sole file occurrence is the packet's own
  blurb quoted as front-matter teaser).
- Arc: connection (the redeemed 1940 order No. 812), obstacle (the
  winding-up, her geography), rupture (he buys the firm's mind at auction
  through an agent after she asked him not to come — the concealment, not
  the kindness, is the break), earned resolution (caretaker's reports,
  seed that cannot be returned, the First Seed List naming sweet pea
  'Edith Prowse', Order No. 1, the 12.40 met). Closed-door throughout.
- ⚑ Publishing untouched: all clicks stay queued in the packet §7
  OWNER-GATE block; keyword rows remain name-level reservations; no
  Netherlands stems (C3 untouched).
- Claim `control/claims/2026-07-13-seed-catalogue-manuscript.md` deleted in
  this flip commit per the claims README.

## Work log
- 2026-07-13T10:21Z — Branch `claude/seed-catalogue-manuscript` from
  origin/main (f15e9f1); premise check clean (no
  `candidates/adult-novels/the-seed-catalogue-courtship/` at HEAD, no
  covering claim in `control/claims/`). Born-red card + claim file committed
  (first commit, f965524) and pushed; READY PR #152 opened.
- 2026-07-13T10:35Z — Complete four-part first draft committed (62a71b1,
  9,071 words, full arc). Expansion + continuity pass committed (75f80e3):
  fourteen added documents where the middle was thinnest, six continuity
  fixes from a full read-through, the "never says the word" violation
  removed — honest 15,133.
- 2026-07-13T10:45Z — DECISIONS.md written (af3f5f1). origin/main
  re-fetched (b1eddbf: sibling's #151 + #153 merged); merged in (084192e),
  zero overlap with this slice's paths. Card flipped complete, claim file
  deleted same commit; `python3 bootstrap.py check --strict` green; branch
  pushed; PR #152 left OPEN on green — no auto-merge armed.
