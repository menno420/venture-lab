# Session — Night run: Large-print edition specs, 4-title bundle (ORDER 008, BOOKS lane)

> **Status:** `complete`

- **📊 Model:** fable-5 · worker slice · ORDER 008 night-run books lane
- **session:** Run under ORDER 008 (control/inbox.md, BOOKS clause: "multiple new book ideas AND multiple versions of each (different angles, audiences, lengths) — versions are cheap once the research exists"). This slice wrote LARGE-PRINT EDITION SPECS (production spec docs only, no new manuscripts) for four titles — *Ultramarine* (adult), *Hollowtide*, *The Last Good Frequency*, *The Undertow* (YA) — as `versions/large-print/EDITION-SPEC.md` per title, mirroring the merged the-slow-word spec (PR #111). Explicitly excluded: the-weigh-house (sibling collision risk) and the-slow-word (done).
- **started (date -u):** Mon Jul 13 01:51:27 UTC 2026
- **closed (date -u):** Mon Jul 13 01:54:25 UTC 2026

## ⟲ Previous-session review

Previous session (`.sessions/2026-07-13-ultramarine-serial-edition.md`, BOOKS slice of this same night run): its zero-shared-surface discipline — touch only net-new files under `versions/**` plus own card/claim — is adopted wholesale here, extended one notch: this slice does NOT edit `ultramarine/versions/README.md` (which that session created) even to add a table row, because a parallel BOOKS sibling could plausibly do the same; the new subdir is discoverable by `ls` and the README row can be added by any later serializing pass. Its honest-`wc` convention (command shown, verbatim numbers) is applied to all four titles here, including the awkward cases it never hit: hollowtide's chapter-sum (28,595) vs assembled-file (28,610) discrepancy and the-undertow's non-story files (EXPANSION.md, README.md) that must be subtracted from the `en/*.md` total — both recorded explicitly rather than rounded away.

## 💡 Session idea

Writing four near-identical specs exposed that the spec's only title-varying inputs are: word count, opener count, content note, price band, and 2–3 title-specific flags — everything else (trim, typography, cost formula) is invariant boilerplate cited to the same two sources. A `docs/publishing/edition-spec-large-print.md` PARAMETER TABLE (one row per title, columns = the varying inputs) plus one shared boilerplate section would replace N whole-file specs, make the invariants updatable in one place when the KDP cost table changes, and shrink the marginal cost of title N+1 from ~a file to ~a row — the same template-extraction move ORDER 008 demands on the PRODUCTS lane, applied to BOOKS production specs.

## Scope

- Run under ORDER 008. Premise check at HEAD (35e5597): none of the four targets had `versions/large-print/`; only live claim was `claude/order-night-run` (inbox append — no overlap); the-weigh-house and the-slow-word untouched per exclusions.
- Real word counts (verbatim `wc -w`): ultramarine `27865` (manuscript/ultramarine.md); hollowtide chapters sum `28595` (ch01–ch16; assembled hollowtide-full.md `28610` incl. front matter); the-last-good-frequency `26390` (single .en.md file); the-undertow `27781` story text (en/*.md total `28653` − EXPANSION.md `410` − README.md `462`).
- Per title: 6×9 trim, 16pt+ large-print typography per the-slow-word spec (citations reused, marked "per the-slow-word spec" incl. its own unverified-APH caveat), page estimate at 160–200 wpp with math shown, KDP print cost ($1.00 + $0.012/page, kdp.amazon.com G201834340 accessed 2026-07-13) + royalty tables (60% × list − print cost) at 3 candidate prices, accessibility notes, content notes carried over.
- Title-specific: ultramarine — ⚑ pending D3 retitle pointer recorded, NOT applied; the-last-good-frequency — Tier-1 cover-only per PUBLISHING-PLAN §2 item 3; all three YA — large-print YA niche (low-vision teen + reluctant-reader crossover) with demand marked **not measured**. YA recommended list $12.99 (bottom of the only verified paperback band; no verified YA-paperback band exists — not measured).
- New versions/README.md created for the three YA titles (ultramarine's already existed from PR #109 — not recreated, not edited).
- ⚑ Publish/price clicks stay owner-gated (CHECKLIST §7) — every spec says so; nothing here authorizes a listing, price, or spend.
- `python3 bootstrap.py check --strict` after the content commit: only the by-design born-red hold on this card (flipped by this commit) — no findings from the content diff.
