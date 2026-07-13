# DECISIONS — The Pepper Ledger

> **Status:** `draft`

Provisional, retroactively owner-vetoable decisions taken under ORDER 008 (2026-07-13 night run, BOOKS clause). All creative decisions this session's call; decide-and-flag.

## D-001 · Premise fidelity to the vetted packet (2026-07-13)
- **Decision:** the manuscript delivers the concept exactly as vetted in `docs/publishing/vetting/the-pepper-ledger.md`: 1620s spice route; a merchant clerk's daughter (Sana, 15) who keeps her father's books; a second, secret ledger found under the counting-house floor; father taken aboard an East Indiaman as "security" for a debt he never made; Sana stows away with a stolen quill; navigation and ledger-craft as a girl's weapon; mutiny arithmetic (the fo'c'sle scene where she reads the crew their own names in the loss column); and the packet's title question answered on the page — why a cargo of pepper is worth more than the crew sailing it (the pepper is sold twice: condemned by a bought survey, then resold prime, with the over-insured hull and the crew's wage-book written off against it).
- **Departure from packet, flagged honestly:** the packet's blurb (§6, explicitly marked "draft v0") has the father taken aboard a ship bound outward; the manuscript makes the voyage a short false "condemned-cargo" run (weeks, not a 20-month Indies round trip) so a complete novella can carry a full voyage arc with the pepper cargo aboard throughout. The Indies voyage proper becomes the earned ending / sequel runway. Title, heroine, ledger mechanism, register, and all seven keyword registers are untouched.
- **Owner veto:** open — retitle or redirect on request.

## D-002 · C3 keyword discipline verified (2026-07-13)
- **Decision:** zero Netherlands-branded stems anywhere in the manuscript, title, or front matter — verified by grep at commit time (`dutch|golden age|delft|amsterdam|netherlands`: no hits). Home port is the invented harbor city "Marren"; currency is generic florins/stivers; the trading company is only ever "the Company." Period texture (double-entry bookkeeping, weigh-house tallies, garbled pepper, East Indiaman working, dead reckoning, barratry/insurance law) draws on the Ultramarine 17th-c research vein (`candidates/adult-novels/ultramarine/bible/`) without touching Ultramarine's claimed register.
- **Owner veto:** open.

## D-003 · POV / tense / register (2026-07-13)
- **Decision:** third-person limited, past tense, close on Sana Brandt. YA adventure register (propulsive chapters, each with an end-hook), NOT the literary-historical register of Ultramarine — keeps the two 17th-c properties clearly separate in voice as the packet requires.
- **Peril calibration:** age-appropriate throughout — storm, fire, one bound-forearm wound in the ladder-head fight, no deaths on the page, no graphic content; the mortal stakes are carried by arithmetic (boats that hold 26 for a company of 28) rather than gore.
- **Owner veto:** open.

## D-004 · Length and honest count (2026-07-13)
- **Decision:** complete 14-chapter novella. Honest count at final commit: `wc -w` = **16,548** on `en/the-pepper-ledger.md` (includes title/front matter and chapter headings; body prose ~16.4k).
- **Note vs packet:** packet §3 planned ~30k–45k; this first complete manuscript lands at the coordinator-directed 15k–20k slice target. Per packet §4 that puts the price at the **$2.99** point of the $2.99–$3.99 band (the $3.99 recommendation was conditioned on ≥35k words). A future expansion pass (or the sequel) can revisit.
- **Owner veto:** open.

## D-005 · Sequel potential (2026-07-13)
- **Decision:** ending is closed (fraud exposed, father cleared, Corver taken, Sana signed as captain's clerk) but built to the packet's series shape — "one voyage per book, one commodity per ledger": Book 2 is the real 20-month Indies run on the refitted *Petrel* under Captain Bakker, next commodity's ledger ready-made.
- **Owner veto:** open.

## D-006 · ⚑ Publishing owner-gated (2026-07-13)
- **Decision:** NOTHING published, listed, priced live, or spent. All publish clicks stay queued exactly as written in the packet's §7 OWNER-GATE block (`docs/publishing/vetting/the-pepper-ledger.md` §7): KDP account/tax interview, title-availability recheck (required — §2 collision verdict inconclusive), cover approval, price set, publish click + KDP Select enrollment — every one an owner click, none performed or scheduled by this session.
- **Price band restated:** YA novella ebook **$2.99–$3.99** (70% tier); at this manuscript's true length, **$2.99** per D-004.
- **Owner veto:** n/a — this is the standing rail (conventions.md #13), not a delegated decision.

## Cost line (token-cost accounting, conventions.md #14)
- One worker session, 2026-07-13 night run: premise check, full packet/bible read-in, 14 chapters (~16.5k words) written and committed in 5 content chunks, this DECISIONS file, bootstrap check, PR. No external spend; no owner clicks consumed.
