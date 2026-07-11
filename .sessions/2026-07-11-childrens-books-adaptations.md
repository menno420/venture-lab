# Session — Children's book adaptation track

> **Status:** `complete`

- **📊 Model:** opus-4.8 · high · revenue-lane creative ideation
- **session:** ships candidates/childrens-books/adaptations/ — 3–4 adaptation concepts (public-domain classics + our own IP) retold with animal casts in a short, fun, childish voice, plus a copyright-guardrail README.
- **started (date -u):** Sat Jul 11 17:57:02 UTC 2026 (born-red first commit)

## ⟲ Previous-session review

Previous-session review: this lane just landed the first children's-books portfolio (6 original concepts) in PR #45, now merged to main. This slice adds an adaptation track alongside it.

## 💡 Session idea

Owner addition (2026-07-11): successful/known books can inspire small children's books by turning characters into animals and telling the story short and fun. Guardrail: adapt ONLY public-domain works (verify per work) or the lane's own IP; contemporary/copyrighted books are inspiration for ORIGINAL stories only, never adaptation sources. Creative portfolio; publish paths owner-gated.

## Scope

- candidates/childrens-books/adaptations/README.md — copyright guardrail (allowed: public-domain + own-IP; not allowed: contemporary/copyrighted retellings) + index + ranking.
- candidates/childrens-books/adaptations/ — 3–4 adaptation concept files (mix of public-domain and own-IP), each with logline, age band, sample opening (~150–300w, short fun childish voice), animal-cast mapping, 2–3 scene premises, visuals direction + illustration prompt sheet; public-domain picks name the source work + its PD status.
- This slice ALSO adds one new original concept — #7 Star Pirates (middle grade) — under candidates/childrens-books/concepts/, and updates the main childrens-books/README.md ranking + language table + counts to SEVEN concepts.

## Work log

- Born-red session card committed (b76305b) to open the slice.
- Wrote 4 adaptation concept files under `candidates/childrens-books/adaptations/`: A1 Kit in Wonderland (Carroll 1865, PD), A2 Mika's Long Way Home (Homer's Odyssey, PD), A3 Around the World in 80 Naps (Verne 1873, PD), B1 The Dormouse Who Dreams Awake (DREAMLINE, own IP / Source B).
- Wrote `adaptations/README.md` with the copyright guardrail stated up front (allowed: public-domain + own-IP; not allowed: any contemporary/copyrighted retelling), an index table, loglines, and a 4-way ranking (B1 first).
- Added one new original concept, #7 Star Pirates (middle grade ~8–12), under `concepts/07-star-pirates.md`.
- Updated the main `childrens-books/README.md`: concept list now 7, ranking reworked (Star Pirates top pick, Comet Biscuit second, Tummel lead old-fashioned), Dutch-first table + counts updated, adaptations pointer added.
- Ran `bootstrap.py check --strict` against this card — GREEN (see outcome).

## Status / outcome

Shipped the adaptation track (4 retellings, all rights-clear: 3 public-domain + 1 own-IP) plus original concept #7 Star Pirates, taking the portfolio to 7 concepts. The main index and the new guardrail README both merge cleanly with the merged 6-concept base (PR #45). `check --strict` passes GREEN. This is a creative portfolio — no spend, no accounts, no images generated or published; every publish path stays owner-gated, and no borrowed IP is used beyond verified public-domain works and the lane's own DREAMLINE IP. Committed and pushed on branch claude/childrens-books-adaptations; PR opened READY into main.
