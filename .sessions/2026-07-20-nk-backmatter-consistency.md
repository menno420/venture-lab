# Session — Night Kiln back-matter consistency fix slice

> **Status:** `in-progress`

- **📊 Model:** opus-4.8 · medium · docs-only (owner-surface consistency)

- **started (date -u):** Mon Jul 20 07:54 UTC 2026
- **branch:** `claude/nk-backmatter-consistency`
- **base:** `main@4774d73`
- **purpose:** land the two owner-surface consistency defects surfaced by the
  2026-07-20 owner-surface QA pass (recorded as out-of-scope follow-ups on
  `2026-07-20-owner-surface-qa.md`) as ONE READY PR under the born-red landing
  protocol. Both are reversible content-only fixes on the upload-ready KDP
  manuscript packages; **publish/spend/proofread stay owner-only**.
- **scope (files):**
  - FIX 1 — Night Kiln Book 5 `kdp-ready/book-5/MANUSCRIPT-KDP.md` "About the
    series" back-matter: it still claims the cycle ends at five books ("fifth
    and final", "no sixth book waiting", "the five-book cycle is complete"),
    but Night Kiln is now a 6-book series (Book 6 *The Summer Ember*, #279,
    lives in `kdp-ready/book-6/`). Correct so it does NOT claim the series ends
    at five; point forward to Book Six, matching Bk6's own "About the series"
    framing. Series-accurate at 6 books, series-open, no invented Book 7.
  - FIX 2 — About-the-author back-matter slot made uniform across all 7
    `kdp-ready/*/MANUSCRIPT-KDP.md` (Night Kiln bk4/5/6, Ultramarine bk2/3,
    Dream bk2/3): one convention — a bio slot carrying the canonical
    `⟨owner: author bio⟩` token established in #284.
  - This card + `control/claims/nk-backmatter-consistency.md`. No generated
    file (`OWNER-QUEUE.md`, `.substrate/*`), no SKU, no `control/status.md`.

## FIX 2 — About-the-author slot audit (before → after)

Canonical token from #284: `⟨owner: author bio⟩` (U+27E8/U+27E9). Convention
chosen: every "About the author" slot is a **bio slot** carrying that token.
Book count cross-checked against `docs/current-state.md` (6-book Night Kiln,
Books 1–6) and the `candidates/*/kdp-ready/` tree (7 MANUSCRIPT-KDP.md files).

| Manuscript | Old About-the-author slot | Result |
|---|---|---|
| Night Kiln bk4 | `⟨owner: author name⟩` (name-only) | → `⟨owner: author bio⟩` |
| Night Kiln bk5 | `*⟨owner: author bio⟩*` (bio) | unchanged — already bio |
| Night Kiln bk6 | `*⟨owner: author bio⟩*` (bio) | unchanged — already bio |
| Ultramarine bk2 | `⟨owner: author bio⟩` (bio) | unchanged — already bio |
| Ultramarine bk3 | `⟨owner: author bio⟩` (bio) | unchanged — already bio |
| Dream bk2 | `⟨owner: author name⟩` + `⟨owner: author bio⟩` (both) | → `⟨owner: author bio⟩` |
| Dream bk3 | `⟨owner: author name⟩ *(⟨owner: author bio⟩)*` (both) | → `⟨owner: author bio⟩` |

Judgment call (noted): the Dream books previously carried a standalone author
NAME line above/around the bio. The name is already set on each title page
front-matter (`by ⟨owner: author name⟩`, line 7 of every book), so the
back-matter About-the-author does not *legitimately need* both — normalized to
the single canonical bio slot for true uniformity across all 7.

## Work log

- 2026-07-20 — Synced to `origin/main` (`4774d73`, PR #284), confirmed both
  prior fixes present (placeholder normalization + TRANSITION-DOSSIER restamp),
  branched `claude/nk-backmatter-consistency`. Born-red card + claim committed
  FIRST to arm the substrate-gate HOLD before any fix lands.
  Bootstrap result: [[fill: bootstrap check --strict exit code at close]].

## 💡 Session idea

_(to be filled at close)_

## previous-session review

_(to be filled at close)_
