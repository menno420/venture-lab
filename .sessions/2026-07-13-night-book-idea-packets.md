# 2026-07-13 — Night run: 6 new book-idea vetting packets (BOOKS lane)

> **Status:** `complete`

Started 2026-07-13T00:53:22Z · closed 2026-07-13T01:01:51Z (`date -u`).
**Run under ORDER 008** (control/inbox.md, 2026-07-13T00:46:54Z, landed via
PR #103 — owner night-run DIRECT ORDER; seat clause 1: "BOOKS: multiple new
book ideas AND multiple versions of each"): this slice delivers the
multiple-new-ideas half — six NEW concepts as concept-stage vetting packets
tiling adjacent, non-overlapping niches against the 14-title catalog.
Versions-of-each is queued as the natural next slice (each packet records
its series/variant shape so versioning starts warm).

## Outcome

- Six concept-stage packets under `docs/publishing/vetting/`, each per
  CHECKLIST §1–§7 with a REAL web collision scan quoted + "accessed
  2026-07-13", price band from the plan's verified §1 table, and a
  `derive_owner_queue.py`-parseable §7 ⚑ OWNER-GATE block:
  - `the-paper-orange.md` — adult, Hunger Winter Amsterdam 1944–45
    literary-historical novella (collision Low; third Netherlands
    era-register beside C3's two; reuses Weigh House/Ultramarine research).
  - `the-night-kiln.md` — adult cozy fantasy novella, kiln-witch fires
    memories into pottery (collision Low; cited demand signal).
  - `the-pepper-ledger.md` — YA age-of-sail spice-route adventure
    (collision None/inconclusive; reuses Ultramarine's 17th-c research with
    ZERO Netherlands-branded keywords per the C3 rule — the designated
    cheap-research-reuse concept).
  - `the-marginalia-society.md` — YA dark academia boarding-school mystery
    (collision Low, non-book namesakes only; PW 2025 trend citation).
  - `the-windmill-mouse.md` — kids picture book, miller-mouse little-helper
    (collision Moderate via the 1965 "Windmill in Old Amsterdam" song
    adjacency — differentiator written: no "old Amsterdam" phrasing).
  - `the-puddle-museum.md` — kids picture book, rainy-day curation-of-wonder
    (collision Low; AI-art reflection-failure risk flagged for the §5
    decision).
- `docs/publishing/keyword-map.md` §3: six NAME-LEVEL reservation rows
  (reservations only — no vetted-ownership rows; those come at graduation
  when manuscripts exist). Zero overlap with owned/reserved phrases;
  C1–C3 respected by construction.
- `docs/publishing/OWNER-QUEUE.md` regenerated: 11/11 inputs parsed clean,
  6 decisions (both new kids packets surface their ⚑ illustration gates,
  default Park), 56 owner clicks across 10 sequences, manual-review empty.
- Honest nulls: no manuscript exists for any concept (each packet parks at
  "no manuscript" explicitly); no spend, no accounts, no publishing; base
  case ≈ $0 stated in every §3.

## 💡 Session idea
💡 **Concept-packet graduation checker.** The map now holds two row species
(vetted ownership vs concept reservations) and nothing machine-checks that
a packet claiming ownership rows actually has a manuscript path on disk.
A ~30-line advisory script (pattern: `check_ledger_drift.py`) that
cross-references `docs/publishing/vetting/*.md` front-matter
("concept-stage" marker) against `candidates/**` manuscript dirs would
catch a packet graduating on paper only — same tolerant/exit-0 contract as
`derive_owner_queue.py`.

## Previous-session review
previous-session review: `.sessions/2026-07-12-owner-queue-derive.md`
(PR #101) — genuinely strong: the tolerant-parser + always-exit-0 contract
meant tonight's six new packets dropped straight into a regenerated queue
with zero script changes (11/11 clean parse proves the abstraction held);
honest nit: its DECISIONS-LOG 💡 idea (owner answers evaporate in chat) is
still unbuilt, and tonight added two more Park-default decisions to a queue
that can only grow until that loop closes.

## Model
- **📊 Model:** fable-5 · worker · BOOKS lane, night run
