# Session — The Paper Orange back-matter & sellability package (additive, gate-free)

> **Status:** `in-progress`

- **📊 Model:** [[fill:model]]
- **started (date -u):** Sat Jul 18 17:37:08 UTC 2026
- **branch:** `claude/paper-orange-backmatter-2026-07-18`
- **base:** `main@0662542`
- **purpose:** add a **purely additive** back-matter / sellability package to the
  flagship title *The Paper Orange*, landed as ONE PR. New dir
  `candidates/adult-novels/the-paper-orange/apparatus/` holding three reusable
  launch assets grounded in the actual manuscript —
  `HISTORICAL-NOTE.md` (reader's historical-context note on the 1944–45 Dutch
  Hunger Winter + Liberation, with a public-history further-reading pointer
  list), `BOOK-CLUB-GUIDE.md` (reading-group discussion guide: thematic
  overview + ~12 chapter-anchored questions + topics-to-research), and
  `MARKETING-COPY.md` (hook / short + long blurb / comp-positioning lines /
  keyword + BISAC suggestions / book-club-and-educator pitch angle). Each file
  carries a provenance footer citing the manuscript `file@sha`. The title's
  `versions/README.md` index gains an apparatus row.
- **hard constraint:** **NO author's-prose changes** — this slice ONLY ADDS
  supporting apparatus. `git diff --stat` must show only new apparatus files +
  the card / claim / index row. No `en/*.md` manuscript byte is touched.
- **in-conventions:** agents already author EDITION-SPECs
  (`versions/large-print/`, `versions/audio/`) and full listing copy
  (`docs/publishing/vetting/the-paper-orange.md` §6 — blurb, keywords,
  categories); additive marketing / back-matter apparatus is directly
  analogous. No convention forbids agent-authored book apparatus; the hard
  rails (`docs/conventions.md` §13) forbid only spend / accounts / publishing,
  none of which this slice touches.
- **queue note:** this is a launch/back-matter ASSET, not a publish surface —
  it adds **NO §7 vetting packet and NO OWNER-QUEUE row** (editions/apparatus
  don't; `scripts/derive_owner_queue.py` derives the queue only from vetting
  packets' §7 blocks). The ebook publish is already queued under the title's
  existing packet gate. No publish, no spend, no accounts by the seat.
- **session:** Continued autonomous run under ORDER 016 + the live owner turn
  2026-07-18T13:47Z. Everything is grounded in a full read of the EN master
  manuscript — the derived setting (Amsterdam, Hunger Winter Nov 1944 → May
  1945, Liberation) is the manuscript's own, not an assumed one. Born-red card
  holds the substrate-gate red until the deliberate completion flip.

## 💡 Session idea

[[fill:idea]]

## previous-session review

[[fill:prev-review]]

## Work log

- 2026-07-18T17:37Z — Branch `claude/paper-orange-backmatter-2026-07-18` from
  origin/main (`0662542`). Read the full EN manuscript + conventions +
  vetting packet + existing EDITION-SPEC scaffolds. Born-red card committed
  (first commit), pushed. Build begins.
