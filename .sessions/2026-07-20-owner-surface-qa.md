# Session — Owner-surface QA fix slice

> **Status:** `complete`

- **📊 Model:** opus-4.8 · medium · docs-only (owner-surface QA)

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
- 2026-07-20 — Landed all six fixes in logical commits:
  - **A1** (`fdbc…`): OWNER-START-HERE Step-8 "five"→"seven" (only stale "five" in
    the file; section is titled "The seven new book sequels").
  - **A2**: TRANSITION-DOSSIER restamped to live HEAD `d2d49ec` / #281. Confirmed
    HAND-WRITTEN (no `scripts/` reference, no generated marker), so corrected every
    stale figure: 5→7 new sequels (added Bk6 #279 + Ultramarine Bk3 #278 table
    rows), Night Kiln 5→6-book series, Ultramarine 2-book→complete 3-book trilogy,
    asset-map + resume-path package lists (5→7 paths), footer HEAD. Counts
    cross-checked against `docs/current-state.md` L151/154–157 and the `candidates/`
    tree. Rewrote the "Known drift" section (current-state.md has since caught up to
    the 2026-07-20 wave).
  - **B1+B2**: normalized owner-fill placeholders across all 7
    `kdp-ready/*/MANUSCRIPT-KDP.md` to the canonical `⟨owner: …⟩` tokens per the map
    above (before: 42 divergent placeholder lines, 0 canonical tokens; after: 0
    old-style, 63 canonical tokens — proven by grep). Added the review/store-link
    CTA back-matter to the 4 books missing it (Night Kiln bk4, Ultramarine bk2/bk3,
    Lull bk2); all 7 now carry exactly one CTA + one `⟨owner: store link⟩`.
  - **B3**: re-scoped `keyword-map.md` §3 "Lull" row from "Quiet/literary novella"
    to "Middle-grade portal-fantasy trilogy (COMPLETE, Books 1–3)"; reconciled the
    bk2/bk3 `KDP-METADATA.md` §3 flags to past-tense. Left owner-gated: the §1
    per-title keyword reservation and the separate "Lull" title-collision check
    (`DECISIONS.md` D-001).
  - **C-advisory**: added a `> ⚑ EDITORIAL NOTE` atop
    `api-robustness--reddit.md` on the r/webdev self-promo removal risk + honest
    alternatives. File kept intact; the `⟨owner: your Gumroad link⟩` marker untouched.
  - Validation: `bootstrap.py check --strict` red on the **born-red HOLD only**
    (in-progress Status — the designed hold); no other guard fired (no catalog/dref,
    no parity, no docs-links). Advisories pre-existing/non-gating (2 seat-digest,
    7 model-line on OTHER cards; my card trips none once this line is set to a valid
    PL-004 class). Docs+manuscript-only diff — no code touched, so pytest skipped per
    convention. `.substrate/guard-fires.jsonl` left UNSTAGED to keep the diff scoped
    (matches the ultramarine-book3 / -book2 precedent).
- 2026-07-20 — Flip to `complete` (this commit): Status badge flipped, Model line
  set to a valid PL-004 form, 💡 idea + prev-session review added, all auto-draft
  slots resolved. This flip is the last commit and releases the landing workflow.

## Out-of-scope follow-ups surfaced (NOT fixed — suggested for the owner/next slice)

- **Night Kiln Bk5 back-matter is stale**: its "A note to readers" still says
  *"There is no sixth book waiting at the end of this one: the five-book cycle is
  complete"* and *"grow line by line to the fifth"* — but Book 6 (*The Summer Ember*)
  now exists. Not in this slice's defect scope (B-defects were placeholders + CTA
  consistency), so left untouched; flag for a content-refresh slice.
- **KDP `⟨owner: author bio⟩` vs `⟨owner: author name⟩` About-the-author shape**
  still varies by book (some sign with a name, some with a bio blurb). Normalizing
  the *field-TYPE* was in scope (done); unifying *which* field each book's
  About-the-author uses is an editorial call left to the owner.

## 💡 Session idea

💡 **A `kdp-owner-token` guard that fails CI when a `kdp-ready/*/MANUSCRIPT-KDP.md`
carries an owner-fill placeholder in any shape other than the canonical
`⟨owner: …⟩` token set.** This slice's B1 fix (collapsing ~a dozen ad-hoc
`[… — owner to set]` / `owner to finalise` / `*(Placeholder …)*` strings into eight
canonical tokens) restores the "one scripted find-replace clears one field across
the whole catalog" property — but nothing keeps it restored: the next book drafted
from an older template re-introduces a bespoke bracket and silently breaks the
invariant again (exactly how three extra variants slipped past the first grep here).
Recipe: a tiny stdlib checker (advisory first, then gating) that greps each KDP
manuscript for bracketed/parenthetical owner-fill hints (`owner to \w+`,
`placeholder`, `TBD`) and passes only if every owner-fill uses a token from a small
allowlist (`author name | author bio | year | cover credit | publisher | ISBN |
edition and copyright | store link`) — the same allowlist the eventual owner
find-replace script consumes, so the guard and the clearing tool agree by
construction. Complements the submissions pack's existing `⟨owner: …⟩` convention,
extending one owner-fill grammar across both the distribution and KDP lanes.

## previous-session review

previous-session review: the immediately-prior 2026-07-20 card,
`2026-07-20-ultramarine-book3.md`, modelled the exact landing discipline I reused —
born-red card + claim committed FIRST to arm the substrate-gate HOLD, content
second, the `complete` flip LAST as the single releasing commit, family-level model
attribution, and a deliberately scoped diff that left `control/status.md`, the SKU
registry, `OWNER-QUEUE.md`, and `.substrate/guard-fires.jsonl` untouched. I mirrored
its guard-fires-unstaged choice here. One thing to carry forward: its model-line
task-class ("Ultramarine Book 3 manuscript") trips the PL-004 `model-line-class`
advisory — a good reminder to pin my own line to a real PL-004 class
(`docs-only`) rather than a free-text label, which is why this card does.
