# Session — Night run: Ultramarine serialized 3-part edition (ORDER 008, BOOKS lane)

> **Status:** `complete`

- **📊 Model:** fable-5 · worker slice · ORDER 008 night-run books lane
- **session:** Run under ORDER 008 (control/inbox.md, BOOKS clause: "multiple new book ideas AND multiple versions of each (different angles, audiences, lengths) — versions are cheap once the research exists"). This slice built the SERIALIZED 3-PART EDITION version of the adult historical novel *Ultramarine* (Delft 1654, base manuscript 27,865 words) under `candidates/adult-novels/ultramarine/versions/serial-edition/`.
- **started (date -u):** Mon Jul 13 01:23:24 UTC 2026
- **closed (date -u):** Mon Jul 13 01:28:35 UTC 2026

## ⟲ Previous-session review

Previous session (`.sessions/2026-07-13-night-template-packs.md`, PRODUCT #2 of this night run): a tight quality-floor slice whose double-rebuild sha check turned a freshness claim into evidence in under a minute — cheap in both outcomes, exactly the property a floor check needs. Two things carried into this session: (1) its "honest null" discipline (say explicitly what wasn't verifiable rather than leaving the row silently absent) is applied here to serialization economics — the NOTES.md revenue math is framed as unverified with an explicit SIM-REQUEST rather than presented as a projection; (2) its observed branch-conflict hazard (OWNER-QUEUE regenerated from different packet sets on parallel open branches) is the reason this slice touches ONLY net-new files under `versions/**` plus its own card/claim — zero shared-surface writes, so parallel BOOKS-lane siblings (the-slow-word, the-weigh-house versions) cannot conflict with it by construction.

## 💡 Session idea

The serial cut exposed a reusable invariant worth encoding in the versions convention: **additions-only derivation**. Every episode here is `full part text (byte-identical, via tail -n +5 of the committed part file) + written additions at the seams` — which means a one-line checker can verify canon integrity forever: strip the marked additions and diff against `manuscript/part-*.md`; any drift is a canon change hiding in a "version". Worth a small `tools/check_version_derivation.py` that NOTES.md can declare a `derived-from:` line for — versions that are pure supersets get continuity checking for free, and versions that genuinely rewrite (the board-book cuts) simply don't declare it.

## Scope

- Premise check at HEAD (d0ab1dd): `candidates/adult-novels/ultramarine/` had no `versions/` dir — clear to build.
- Created `versions/README.md` (convention: one subdir per version, manuscript + NOTES.md, honest `wc -w`, ⚑ gates carried) and `versions/serial-edition/` with three episode files + NOTES.md.
- Episodes: full part text unaltered + cold open (ep 1, ~200 w), episode-ending hooks (eps 1–2, ~140 w each), in-voice "The Story So Far" recaps (ep 2: 446 w; ep 3: 469 w), per-episode front matter with content note. No scene-boundary moves — the part breaks are clean act breaks.
- Honest `wc -w`: 9188 / 9849 / 10399 (total 29436; base parts 8809/9164/9850).
- Market position in NOTES.md: per-episode $2.99 (KDP 70% floor per docs/publishing/CHECKLIST.md §4) vs full novel $3.99–$5.99; serialization economics marked unverified with **SIM-REQUEST: serial vs single-volume pricing feasibility**.
- ⚑ Publishing stays owner-gated via `docs/publishing/vetting/ultramarine.md` §7; ⚑ pending D3 retitle ("The Widow's Blue — A Novel of Delft, 1654") NOT applied — working title kept, pointer recorded in versions/README.md and NOTES.md.
- `python3 bootstrap.py check --strict`: only the by-design born-red hold on this card (flipped by this commit) — no findings from the content diff.
