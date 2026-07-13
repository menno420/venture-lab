# 2026-07-13 — The Paper Orange: first complete manuscript

> **Status:** `complete`

- **📊 Model:** fable-5 · worker slice · BOOKS lane, 2026-07-13 night run
- **Started:** 2026-07-13T02:01:32Z (`date -u`)
- **Closed:** 2026-07-13T02:15:48Z (`date -u`)
- **⚑ Order basis:** run under **ORDER 008** (owner night-run DIRECT ORDER, landed verbatim in `control/inbox.md`; re-verified present at origin/main `a46ee4b` before this flip) — BOOKS clause: "multiple new book ideas AND multiple versions of each (different angles, audiences, lengths) — versions are cheap once the research exists." Not self-initiated.

**What landed:** the FIRST COMPLETE MANUSCRIPT for *The Paper Orange* (adult literary-historical novella; Hunger Winter, Amsterdam 1944–45), the write-slice that the concept packet `docs/publishing/vetting/the-paper-orange.md` (PR #105 wave) parks on:

1. `candidates/adult-novels/the-paper-orange/en/the-paper-orange.md` — complete novella, 12 chapters, full arc (printer's widow recruited into coupon forgery for people in hiding → the working winter → house search, liberation, the paper orange out of the wallpaper and into the window). Honest `wc -w`: **15811** (includes front matter and chapter headings), inside the 13k–17k brief. Every line finished prose, no placeholders. House formatting matched to the-weigh-house/the-night-kiln conventions (`# TITLE` front matter, content note, `# Chapter One — Name` headings, `---` breaks, THE END + ⁂).
2. `candidates/adult-novels/the-paper-orange/DECISIONS.md` — premise fidelity to the packet, POV/tense, verified-vs-invented historical-accuracy ledger (verified spine: railway strike/embargo, tulip-bulb rations, hongertochten, Landwacht confiscations, Swedish white bread, Manna drops, May 4/5/7/8 sequence; marked inventions: all named characters, the network name, the mill, non-facsimile coupon details), keyword-discipline note on the watched `Amsterdam occupation 1944 story` / `Amsterdam crime novel` adjacency, ⚑ publishing owner-gated via packet §7, price band $3.99–$5.99 (rec. $4.99), NL-translation follow-up flag (*De papieren sinaasappel* — flagged, not done).

**Publishing remains owner-gated** via the packet §7 OWNER-GATE block — this slice adds shelf inventory, not a publish click. No real persons in speaking roles; sensitive-history handling documented in DECISIONS.

## previous-session review

Previous BOOKS slice (`.sessions/2026-07-13-slow-word-novella-cut.md`): its 💡 was budget-first abridgment — compute per-chapter word budgets BEFORE writing and `wc -w` after every chapter so deviation is caught one chapter deep. This session applied it to original drafting: counted at every 3-chapter commit (4,847 → 8,829 → 12,561 → 15,811), and the mid-run pace correction those counts allowed is why the manuscript landed inside 13k–17k with no trim pass at the end.

## 💡 Session idea

Vetting-packet-as-outline pays compound interest: because the concept packet already fixed the protagonist's name, the blurb beats, the era registers NOT to touch (Weigh House/Ultramarine adjacency), and the §6 keyword phrases, the manuscript could be drafted in one pass with zero naming/positioning decisions left open — the packet's §6 draft blurb even doubled as the chapter-1 scene list. Cheap generalization for the catalog: when a write-slice is ordered, always write the vetting packet FIRST in the same night-run wave (concept packet ≈ 1/20th the tokens of the manuscript), so every manuscript slice starts with its decisions pre-paid.

## Work log

1. Premise check at HEAD: no `candidates/adult-novels/the-paper-orange/`, no live claim covering it. Born-red card + claim (`1fc297a`), pushed before content work.
2. Read the vetting packet in full; matched formatting to `the-weigh-house/en/` and `the-night-kiln/en/`.
3. Chapters 1–3 + front matter (`72bc078`), 4–6 (`0176317`), 7–9 (`21e02e2`), 10–12 + end matter (`152254f`), DECISIONS.md (see flip commit's parent). Two continuity fixes caught mid-run (Fien's age, an orange-age date-math slip) — fixed before their chunks were committed where possible, else in the same session.
4. `python3 bootstrap.py check --strict`: only findings were this card's designed born-red hold + its missing close-out markers — both resolved by this flip commit. Claim file `control/claims/claude-paper-orange-manuscript.md` deleted in this same commit.
