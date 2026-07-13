# Session — Night run: The Pepper Ledger, first complete manuscript (ORDER 008, BOOKS lane)

> **Status:** `complete`

- **📊 Model:** fable-5 · worker slice · ORDER 008 night-run books lane
- **session:** Run under ORDER 008 (control/inbox.md, BOOKS clause: "multiple new book ideas AND multiple versions of each (different angles, audiences, lengths) — versions are cheap once the research exists"). This slice wrote the FIRST COMPLETE MANUSCRIPT for *The Pepper Ledger* (YA age-of-sail adventure), the concept vetted in `docs/publishing/vetting/the-pepper-ledger.md` — the wave's designated cheap-research-reuse title (17th-century research vein of Ultramarine, different genre lane and audience, zero Netherlands-branded keyword stems per keyword-map C3).
- **started (date -u):** Mon Jul 13 01:32:44 UTC 2026
- **closed (date -u):** Mon Jul 13 01:48:15 UTC 2026

## ⟲ Previous-session review

Previous session (`.sessions/2026-07-13-ultramarine-serial-edition.md`, BOOKS lane of this same night run): a clean versions-slice whose two best properties carried directly into this one. (1) Its zero-shared-surface construction — net-new files under one candidate dir plus own card/claim only — is copied here verbatim: this slice touches nothing outside `candidates/ya-novels/the-pepper-ledger/**` and its own card/claim, so siblings (the-slow-word, the-weigh-house, the-night-kiln) cannot conflict with it by construction. (2) Its honest-`wc -w` discipline is applied at the harder end: the vetted packet planned ~30k–45k, this manuscript landed 16,548 — DECISIONS D-004 states the gap plainly and re-derives the price consequence ($2.99, not $3.99) instead of quietly inheriting the packet's length-conditioned recommendation. Its 💡 (additions-only derivation checking for versions) is noted as not applicable here — this is a base manuscript, the thing versions will later derive FROM — which is itself the review point: that checker's value depends on base manuscripts landing first.

## 💡 Session idea

The packet-to-manuscript step exposed a reusable pattern worth writing into the vetting checklist: the **premise-departure register**. This manuscript kept the packet's premise but deliberately restructured one element (outbound Indies voyage → short false "condemned-cargo" run) so a novella could carry a complete arc — and the only place that departure is recorded is this candidate's DECISIONS.md, where a future cover/blurb writer may not look. A one-line "departures from packet" row in the vetting doc's §6 (filled at manuscript-landing time, owner-visible at the §7 publish gate) would keep listing copy and manuscript from drifting apart — cheap to add, and it turns the packet into a live contract instead of a snapshot. Follow-up-sized; not done this slice because docs/publishing/** is out of this slice's write scope.

## Scope

- Premise check at HEAD (1eb4fe4): `candidates/ya-novels/the-pepper-ledger/` did not exist; no claim in `control/claims/` covered it. Claim filed born-red first commit (40c5f7c).
- Delivered `candidates/ya-novels/the-pepper-ledger/en/the-pepper-ledger.md`: complete 14-chapter YA adventure novella, honest `wc -w` **16,548** (target 15k–20k). Arc: counting-house setup and the second ledger → father seized as "security" → stowaway in the pepper hold → discovery and clerk's berth → gale and the Combs (dead-reckoning save) → false course, sack-count, keystone schedule copied → cove rendezvous → fo'c'sle "mutiny arithmetic" audit scene → fire/reckoning → earned landing (fraud deposited with underwriters, father cleared, Sana signed as captain's clerk; sequel runway = the real Indies voyage).
- YA contract kept: teen protagonist with real agency (every turn driven by Sana's ledger-craft), chapter end-hooks throughout, age-appropriate peril (no on-page deaths, no graphic content), father-daughter emotional throughline ("numbers never lie / carried forward"). Period texture from the Ultramarine bible research vein (double-entry waste-book/journal/ledger, weigh-house sampling, garbled pepper, traverse board/log-line/lead, barratry and underwriters) woven into scenes, not info-dumped.
- C3 discipline verified by grep: no `dutch|golden age|delft|amsterdam|netherlands` hits anywhere in the manuscript; invented port "Marren", generic "the Company".
- `DECISIONS.md`: premise fidelity + one flagged departure (D-001), C3 verification (D-002), POV/tense third-limited past close on Sana (D-003), honest count + $2.99 consequence (D-004), sequel line (D-005), ⚑ publishing owner-gated via packet §7 with YA band $2.99–$3.99 (D-006), token-cost line.
- ⚑ Publishing remains fully owner-gated: all clicks stay queued in `docs/publishing/vetting/the-pepper-ledger.md` §7 (KDP account, required title recheck, cover, price, publish + KU) — none performed.
- `python3 bootstrap.py check --strict` pre-flip: only the by-design born-red hold on this card (flipped by this commit); no findings from the content diff. Claim file deleted this same commit.
