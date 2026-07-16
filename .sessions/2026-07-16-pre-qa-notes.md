# Session — mechanical pre-QA notes + length-band ruling prep (shrink the owner's cold NL proofread read to a guided checklist, without touching the owner gate)

> **Status:** `in-progress`

- **📊 Model:** Claude Opus · high · review/verify
- **started (date -u):** Thu Jul 16 16:58:12 UTC 2026
- **branch:** `claude/pre-qa-notes` (PR TBD)
- **session:** ⚑ Self-initiated slice, and the session's FINAL planned
  round. All inbox ORDERs 011–015 are terminal; nothing owner-queued asked
  for this. The binding constraint on ~13 ready NL editions is an
  OWNER-ONLY native-speaker proofread pass — an AI cannot clear it
  (confirmed by the #213 slice, which recognised it as HARD-GATED). This
  slice deliberately does **NOT** touch that gate. Instead it attacks the
  constraint sideways: it produces artifacts that SHRINK the owner's
  proofread work from a cold ~16k-word Dutch read per title down to a
  guided checklist — the native read stays the owner's, but it is no longer
  cold.
- **scope:** THREE parts, ONE PR.
  - **Part A** — a per-title MECHANICAL pre-QA note (`PRE-QA.md`, sibling to
    the version's `NOTES.md`) for the 3–5 NL titles closest to publishable.
    Each note carries ONLY what an agent can legitimately produce and an
    explicit disclaimer that it is machine pre-annotation, NOT a native
    proofread and NOT a gate clear: a coinage / craft-register inventory
    with a cross-manuscript CONSISTENCY check (variant spellings/inflections
    of a coined term, cited by location), the flagged word-count expansion
    seams isolated and quoted for the human to judge calque-padding, and
    mechanical nits (doubled words, quote/dialogue-punctuation
    inconsistencies) cited by location. hunspell nl_NL is NOT installed in
    this environment, so NO spellcheck pass is claimed — consistency-based
    checks only, stated as such in every note.
  - **Part B** — length-band ruling PREP for **De Morgendeur** (Book 2) and
    **De Oogstslag** (Book 3) of the Night-Kiln series: honest `wc -w`
    against the catalog band, the trade-off, and a clear RECOMMENDATION for
    a one-word owner ratify. The ruling itself stays the owner's — this
    slice does NOT rule.
  - **Part C** — tighten the D-item attribution in
    `scripts/derive_owner_queue.py` so a native-speaker proofread blocking
    row is never mis-classified as executing a D-item decision above (the
    Weduwenblauw "…for this title" ↔ "Title coupling" keyword-overlap bug
    the #213 slice flagged), + regression test, + OWNER-QUEUE regen. Same
    owner-misleading-wording class as #210/#213. Folded in only because it
    is small and self-contained.
- **walls:** no publish, spend, or external action; no edits to
  `control/inbox.md`; no merge or auto-merge from this seat; the generated
  OWNER-QUEUE.md is only ever written by the script; **no ⚑ Owner gate
  checkbox is ticked or altered** — the hard-gated count must stay 19;
  family-level model names only.
- **verify plan:** every pre-QA note cites real manuscript locations (no
  generic filler; a title that yields nothing meaningful says so rather
  than padding). Regenerate `docs/publishing/OWNER-QUEUE.md` via
  `python3 scripts/derive_owner_queue.py` and confirm hard-gated stays 19
  (Part C only changes Weduwenblauw's explanatory suffix, never gate state).
  `scripts/test_derive_owner_queue.py` + `scripts/lint_owner_gates.py` must
  pass; `python3 bootstrap.py check --strict` must exit 0 (its born-red HOLD
  on this card is the designed exception until the completion flip).
- **done-when:** the pre-QA notes + length-band prep + Part C fix land on a
  READY PR, CI green (kit-tests + substrate-gate), heartbeat re-stamped,
  and this card flipped `complete` as the last commit (clearing the
  born-red HOLD).

## Results (as landed)

[[fill: what actually landed — picked titles + note locations, Part B
counts + recommendation, Part C diff, PR #, gates, heartbeat SHA]]

## ⟲ Previous-session review

[[fill: one-line re-verification of the 2026-07-16 proofread-gate-detection
slice (PR #213, merge 9473e5f)]]

## 💡 Session idea

[[fill: one genuine idea surfaced by this slice]]

## DRY-BACKLOG

[[fill: net-new inventory paused; binding lever is the owner-only
native-speaker proofread pass; this was the session's final planned round]]
