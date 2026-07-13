# Session — counts sync: NEXT-SESSION + current-state vs OWNER-QUEUE at HEAD (2026-07-13)

> **Status:** `in-progress`

- 📊 Model: Claude Fable 5
- **session:** coordinator-specified follow-up to PR #165 — that brief merged
  carrying pre-#164 numbers (PR #164 landed while the slice was in flight and
  the enabler merged #165 before the re-derive could push). This slice syncs
  the prose counts in `docs/NEXT-SESSION.md` AND `docs/current-state.md` to
  the generated OWNER-QUEUE at HEAD `5944109`, every number grep-counted, not
  remembered.
- **applied:** docs/NEXT-SESSION.md (count/derivation fixes) ·
  docs/current-state.md (stale count lines only) ·
  control/claims/2026-07-13-counts-sync.md (deleted at flip) · this card.
  Nothing else touched.
- **verify:** `python3 bootstrap.py check --strict`
- **started (date -u):** Mon Jul 13 14:38 UTC 2026 (born-red first commit)
