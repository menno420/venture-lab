# Session — Owner-surface QA fix slice

> **Status:** `in-progress`

- **📊 Model:** [[fill: family-level model line resolved at flip]]

- **started (date -u):** Mon Jul 20 07:34 UTC 2026
- **branch:** `claude/owner-surface-qa`
- **base:** `main@d2d49ec`
- **purpose:** land the owner-surface QA fixes surfaced by the read-only scan
  (`vl-qa-scan.md`) as ONE READY PR under the born-red landing protocol. Fix the
  owner-facing content-staleness and consistency defects on the publishing docs
  and the 7 upload-ready KDP manuscript packages, without touching any generated
  file, SKU registry, or owner-gated publish surface. Pure repo content + doc
  correctness; **publish/spend/proofread stay owner-only**.
- **scope (files):**
  - A1 — `docs/publishing/OWNER-START-HERE.md` (five→seven).
  - A2 — `docs/publishing/TRANSITION-DOSSIER.md` (HAND-WRITTEN, not
    script-generated — confirmed no `scripts/` reference and no generated
    marker; corrected every stale figure + restamped HEAD).
  - B1 — placeholder normalization across the 7 `kdp-ready/*/MANUSCRIPT-KDP.md`.
  - B2 — review/store-link CTA back-matter added to the 4 books missing it.
  - B3 — `dream-series` bk2/bk3 `KDP-METADATA.md` keyword-map §3 scope note.
  - C-advisory — editorial note atop
    `docs/launch/submissions/api-robustness--reddit.md`.
  - This card + `control/claims/owner-surface-qa.md`. No generated file
    (`OWNER-QUEUE.md`, `.substrate/*`), no SKU, no `control/status.md`.

## B1 — placeholder normalization map (auditable)

Canonical `⟨owner: …⟩` tokens (U+27E8/U+27E9), one identical token per semantic
field-TYPE across all 7 manuscripts, matching the `docs/launch/submissions/`
angle-bracket convention:

| Semantic field | Old bracket variants collapsed | Canonical token |
|---|---|---|
| Author name (byline · copyright holder · about-author signature) | `[Author name — owner to set]`, `[Author name — owner to set.]`, `[author / rights-holder — owner to set]` | `⟨owner: author name⟩` |
| Author bio / biography / about-the-author blurb | `[Author biography — owner to set.]`, `[Author bio — owner to set. …]`, `[About the author — placeholder; owner to set …]`, `*(Author bio to be supplied …)*` | `⟨owner: author bio⟩` |
| Copyright year / first-edition year/date | `[year]`, `[Year]`, `[year — owner to set]`, `[date — owner to set]` | `⟨owner: year⟩` |
| Cover art / design credit / commission | `[credit — owner to set]`, `[owner to set]` (cover), `[owner to commission — see cover brief]` | `⟨owner: cover credit⟩` |
| Publisher / imprint | `[publisher / imprint — owner to set]`, `[Publisher / imprint — owner to set]`, `[Owner to set imprint / year.]` | `⟨owner: publisher⟩` |
| ISBN / ASIN | `[ISBN / ASIN — owner to set]`, `[ISBN — owner to set.]`, `[owner to set]` (ISBN) | `⟨owner: ISBN⟩` |
| Edition-and-copyright combined note | `[Edition and copyright — owner to set before publication.]` | `⟨owner: edition and copyright⟩` |
| Review / store link (CTA) | `[… Review / store link — placeholder; owner to set …]`, `*(Placeholder — owner to finalize wording and store links …)*` | `⟨owner: store link⟩` |

Rule applied: same field → identical token in every one of the 7 books, so a
single scripted find-replace clears one field across the whole catalog. The
submissions-pack `⟨owner: Gumroad⟩` markers were NOT touched.

## Work log

- 2026-07-20 — Synced to `origin/main` (`d2d49ec`, PR #281), branched
  `claude/owner-surface-qa`. Baseline `bootstrap.py check --strict` EXIT 0
  (pre-existing advisories only, non-gating). Read the read-only scan for exact
  locations. Born-red card + claim committed first (this commit) to establish
  the substrate-gate HOLD before any fix lands.
- [[fill: fixes work-log entry added before flip]]

## 💡 Session idea

[[fill: one genuine idea resolved at flip]]

## previous-session review

[[fill: one-line prev-session review resolved at flip]]
