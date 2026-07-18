# Session — The Paper Orange back-matter & sellability package (additive, gate-free)

> **Status:** `complete`

- **📊 Model:** claude-opus-4-8 family · high effort · book apparatus (content)
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

💡 **A reusable `apparatus/` template trio — `HISTORICAL-NOTE`,
`BOOK-CLUB-GUIDE`, `MARKETING-COPY` — every catalog title inherits, plus an
educator/library one-page sales sheet as the fourth asset.** This slice proved
the shape is title-agnostic in the same way the audio EDITION-SPEC card proved
its scaffold was: the *structure* of all three files is fixed (historical note =
setting → record-vs-fiction → further reading; book-club guide = thematic
overview → chapter-anchored questions → topics-to-research; marketing copy =
hook → short/long blurb → comps → keywords/BISAC → book-club/educator pitch),
and only the per-title *content* changes — and most of that content already
exists, structured, in each title's `DECISIONS.md` (vetted spine, marked
inventions) and vetting packet §6 (blurb/keywords/categories). Lift the
scaffolding into `apparatus/*.template.md` (or a `scripts/new_apparatus.py`
that stubs the three files, pre-filling the marketing block straight from the
packet §4/§6 and the historical block's record-vs-fiction table from
`DECISIONS.md`'s "marked inventions" bullet), and every EN title gets a
book-club/educator discovery surface — the single strongest *gate-free* demand
lever a standalone novella by an unknown author has — for the cost of one
grep-and-fill. Pairs with the existing large-print + audio spec tiers to make a
complete gate-free catalog layer: two accessibility formats, three back-matter
assets, all spec/content only, all inheriting the one owner ⚑ publish gate.
The **educator/library sales sheet** (one page: logline, content-note, curriculum
fit, the free companion guide as the hook, ordering pointer) is the natural
fourth template — it turns the book-club/educator pitch in `MARKETING-COPY.md`
into a hand-out the owner can actually send to a librarian or teacher.

## previous-session review

previous-session review: `.sessions/2026-07-18-next-wave-roadmap.md` (PR #234,
slice-4 of the continued ORDER 016 run — the next-wave ranked candidate
pipeline). A disciplined planning slice that did the one thing a roadmap most
often fails to do: it grounded every ranked row in the real tree (confirmed the
five recently-built kits present, retired the already-BUILT menu items into
their own table) so a fresh seat can't read a "candidate" that already ships at
owner-click-ready — the false-not-dry twin of the false-dry it fixes. Its 💡 (a
`scripts/lint_roadmap.py` that auto-retires built rows against the tree) is the
fourth independent card now converging on "machine-check the drift-prone doc,"
which is a real signal that the derive/lint hygiene build is the next
high-leverage tooling slice. This back-matter slice is the natural companion on
the *content* axis: the roadmap ranks what to build next; this proves out a
gate-free content tier (back-matter apparatus) that any of those title
candidates can inherit cheaply — and its own 💡 above generalises exactly the
roadmap's "mechanize the drift-prone artifact" instinct to the apparatus layer.

## Work log

- 2026-07-18T17:37Z — Branch `claude/paper-orange-backmatter-2026-07-18` from
  origin/main (`0662542`). Read the full EN manuscript + conventions +
  vetting packet + existing EDITION-SPEC scaffolds. Born-red card committed
  (first commit), pushed. Build begins.
- 2026-07-18T17:4xZ — Built `apparatus/{HISTORICAL-NOTE,BOOK-CLUB-GUIDE,
  MARKETING-COPY}.md`, each grounded in the manuscript with chapter citations
  and a `file@sha` provenance footer; indexed from `versions/README.md`
  (backtick filenames). Verified `git diff --stat` touches **no `en/*.md`**
  manuscript byte. `bootstrap.py check --strict`: only the born-red HOLD red
  (by design); no `[reachable]`/dead-link finding (backtick index links pass);
  the seat-digest + model-line + claims-order-collision findings are
  pre-existing advisory-only (never exit-affecting, confirmed on clean
  origin/main by the slice-4 card). PR #235 opened READY. NO §7 packet, NO
  OWNER-QUEUE regen — apparatus is not a publish surface. Card flipped
  `complete` (this commit) to release the born-red HOLD.
