# 2026-07-13 — Ultramarine: Dutch (NL) edition

> **Status:** `complete`

One-line summary: complete literary Dutch translation of *Ultramarine* —
*Weduwenblauw*, all 12 chapters in three parts, honest `wc -w` 28,439 (EN
source 27,865, +2.1%) — plus mandatory NOTES.md, NL vetting packet,
keyword-map C4 rows, and OWNER-QUEUE regen, landed as one READY PR (#135)
per the one-PR pattern proven by #134.

Started: Mon Jul 13 04:05 UTC 2026 (born-red first commit `dce257b`).
Closed: Mon Jul 13 04:32 UTC 2026. PR #135.

## Intent

Run under ORDER 008 (owner night run 2026-07-13, BOOKS clause: "multiple
new book ideas AND multiple versions of each (different angles, audiences,
lengths) — versions are cheap once the research exists"). This slice adds
the different-**language** audience version for the catalog's most
Dutch-native title of all: a novella set in Delft, 1654, around the
historical Delft Thunderclap — the EN text glosses Dutch Golden Age
realities that the NL edition simply speaks. Backlog check at HEAD
(`2c039e3`): ultramarine/versions/ held only serial-edition + large-print
spec; the NL edition was OPEN; control/claims/ carried no collision (only
the coordinator's inbox-scope night-run claim).

## Scope

One work increment: NL manuscript
(`candidates/adult-novels/ultramarine/versions/nl/weduwenblauw.md`, all 12
chapters, every line finished prose, committed in 2-chapter chunks) +
`NOTES.md` (source pinning, title decision with dated collision scan +
rejected alternatives, glossary incl. gloss reversions, honest `wc -w`,
⚑ owner gates) + the NL vetting packet
(`docs/publishing/vetting/weduwenblauw.md`, dated 2026-07-13 collision
scan) + 7 keyword-map rows under the C4 Dutch-namespace / C3
Golden-Age-register rules + the derived owner queue regenerated. Walls
held: no edits to the EN master, `control/status.md`, `control/outbox.md`,
`control/inbox.md`, workflows, or triggers; no publish, spend, or external
action.

## Outcome

- `versions/nl/weduwenblauw.md` — title ***Weduwenblauw*** (subtitle *Een
  roman over Delft, 1654*): the Ch. 11 title made the book's title, and
  the natural Dutch form of the EN packet's pending ⚑ default *The
  Widow's Blue*, so the NL pick stays compatible with the live owner
  decision. Collision scan 2026-07-13: **clean** (nearest: van der
  Vlugt's *Nachtblauw* — Delft/17th-century ADJACENCY, logged as comp
  evidence); the direct translation ***Ultramarijn* is head-on blocked**
  by Henk van Woerden's Gouden Uil-winning 2005 novel — which
  independently reinforces the EN rename recommendation. Alternatives
  (*Het blauw van de weduwe*, *Het geheim van Holland*, *Het blauwe
  uur*) recorded and rejected with cites in NOTES.
- Netherlands literary-historical register throughout; real domain
  vocabulary (loper/wrijfsteen, verfmaalster, vijzel, loodwit, loodglit,
  gebeurnis, keur, weduwenverlof, plateelbakker, het Secreet van
  Holland); motif systems carried whole (the wash-and-settle law "het
  beste is het traagst / het dierbaarste het laatst", het goud dat geen
  goud was, de blauwste handen van Delft, een blauw dat je ademen kunt,
  "het wit", the chained puttertje "stilhoudend om gezien te worden").
- **Gloss reversions** — where the EN glossed Dutch realities (a
  goldfinch "a *puttertje*", "the Secret of Holland", *verfmaalster*
  "(colour-grinder)", the fullers' bridge), the NL speaks plainly again;
  full list in NOTES per the paper-orange convention.
- Honest `wc -w`: **28,439** NL vs **27,865** EN source (+2.1%, inside
  the catalog's measured +1.5%…+2.5% NL band; measured, not targeted).
- EN-source seam found during translation (Ch. 5 puts Grietje's treasures
  on the shop-window sill that morning; Ch. 8/9 have her carrying all
  four "out of the ruin in her fist" with no retrieval line) — carried
  over unfixed per fixes-propagate-EN→NL, flagged in NOTES for an
  EN-side one-line patch.
- Vetting packet `plan`, publish-ready up to the §7 owner gate,
  sequenced behind the EN edition and **coupled to the EN ⚑ title pick**
  (§7 step 2 ratifies the EN+NL pair in one click; parseable default —
  derive_owner_queue manual-review none, D14 default Weduwenblauw).
  Honest gaps (NL comps not formally pulled, €4.99 band inherited,
  native proofread pending) are explicit §7 rows. Keyword map: +7 Dutch
  rows (C4 namespace, C3 Golden-Age register); `weduwe rouw literaire
  roman` completes the C2 grief-vs-crime mirror De Waag's row
  anticipated.
- `bootstrap.py check --strict`: only the designed born-red HOLD
  pre-flip. PR #135 opened READY, not draft; per tonight's owner rule
  the seat leaves it OPEN if auto-merge does not arm.

## 💡 Session idea
💡 **A per-market blocked-titles ledger, so collision scans stop
evaporating.** Every vetting packet spends fresh WebSearch discovering
incumbent titles and then buries the findings in its own §2 prose:
tonight's scan re-established that *Ultramarijn* (van Woerden), *Het
blauwe uur* (Hawkins NL), and the *Oorlogswinter* etiquette all block or
constrain phrases — facts earlier packets partially knew and future
packets (the DE editions, Night Kiln NL, comet-biscuit sequels) will pay
to rediscover. Add a small table to `docs/publishing/keyword-map.md` —
one row per KNOWN incumbent per market (title · market · why it blocks ·
discovered-by packet + date) — that CHECKLIST §2 requires consulting
before any new scan, so each packet's search spend compounds into a
reusable asset instead of a footnote. Distinct from the landed
shared-click hoisting idea (#131, owner-queue mechanics), the FINDINGS.md
continuity channel (#134, EN-master defects), and the gloss-reversion /
shelf-glossary ideas (translation tooling) — this one is scan-evidence
reuse across packets.

## Previous-session review
previous-session review: `.sessions/2026-07-13-weigh-house-nl.md`
(PR #134) — genuine strength: its one-PR shape and its NOTES/packet
formats made tonight's slice pure assembly (manuscript + packet + rows in
one branch, no convention invented), and its explicit "manual-review
none" bar caught this slice's one real defect immediately — the §7
title-coupling step first shipped without a parseable default and the
derive script flagged it before the PR did; honest nit: its keyword-map
row hard-coded a prediction inside a table cell ("crime intent vs any
future Ultramarine NL grief-literary phrase") that this slice only found
by grepping the map — predictions that bind future packets should live in
the C2/C3 rule text where the next packet is told to look, not in one
row's parenthetical.

## Model
- **📊 Model:** fable-5 · worker slice · ORDER 008 night-run books lane
