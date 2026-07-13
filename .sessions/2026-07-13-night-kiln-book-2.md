# Session — The Night Kiln, Book 2 (adult cozy-fantasy novella, EN)

> **Status:** `complete`

- **📊 Model:** fable-5 · BOOKS-lane worker · day run 2026-07-13
- **session:** ORDER 009-adjacent BOOKS day slice — first series continuation for a delivered manuscript
- **applied:** candidates/adult-novels/the-night-kiln/{en/the-morning-door.md,DECISIONS.md}, docs/publishing/keyword-map.md §3 (one line)
- **verify:** `python3 bootstrap.py check --strict`
- **started:** 2026-07-13T09:31Z

## ⟲ Previous-session review
Book 1 landed complete last night (`.sessions/2026-07-13-night-kiln-manuscript.md`,
15,999 words, honest `wc -w`, keystone arc, book-2 hook planted in the closing
pages: the Stonebeck letter about Widow Sorrel's jar and "a strange thing
about a door"). Its card flagged the length conflict honestly (packet §3
~20k–30k vs delivered 12k–16k slice) — this session records the standing
call in DECISIONS.md (⚑ OWNER, reversible) rather than re-litigating it. A
sibling worker is adding vetting packets under `docs/publishing/` on another
branch today: this session created nothing under `docs/publishing/vetting/`
and kept its keyword-map edit to one §3 line.

## 💡 Session idea
💡 **Series canon sheet per multi-book title.** Writing book 2 required
rereading book 1's 15,999 words end-to-end to recover the load-bearing canon
(the kiln's law byte-exact, the Sorrel tale's every detail, cast names,
planted hooks) — and the one internal timeline slip this session had to
repair (jar age vs. character ages) is exactly the drift class that reread
almost missed. A one-page `CANON.md` in the title dir (names/ages, laws
verbatim, artifacts, open hooks with the chapter that planted them), updated
in the same PR as each book lands, turns book N+1's canon recovery from an
O(series-words) reread into an O(1) lookup and gives continuity errors a
diffable home. Distinct from the refrain-consistency ledger idea (byte-parity
across format versions of ONE text); this is cross-book fact continuity.

## Work log
- 2026-07-13T09:31Z — Branch `claude/night-kiln-book-2` from origin/main
  (374e8d1); book 1 reread in full for canon (kiln's law, Sorrel tale,
  cast, hooks). Born-red card + claim file committed (first commit),
  pushed; PR #145 opened READY (repo convention; no auto-merge armed).
- 2026-07-13T09:40Z — All 12 chapters drafted in 3-chapter chunks (commits
  606f936, d0500d0, c8e4c15, 4cfb568): complete standalone three-act arc —
  the Stonebeck letter, the un-firing of Widow Sorrel's jar as the spine,
  the Hessa proving-cup, Perrin's first received telling, the Short Night
  opening fire, the morning told, homegoing; book-3 hook planted (the
  dunted race-dish, "a harvest story").
- 2026-07-13T09:55Z — Continuity pass (b806249): jar age reconciled to
  seventy years against Mercy's and Edda's ages, the letter's promised
  cart-remark paid off on the page, lime-yard kitchen slip fixed. Honest
  `wc -w` = **15,995** (book-1 parity; light trim from 16,202). DECISIONS.md
  gained the dated ⚑ OWNER length-call entry; keyword-map.md gained ONE §3
  name-level line (The Morning Door, Night Kiln series register). Card
  flipped complete, claim file deleted same commit, strict check green,
  branch pushed; PR #145 left OPEN on green.
