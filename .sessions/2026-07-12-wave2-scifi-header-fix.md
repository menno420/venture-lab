# Session — The Slow Word: chapter-header numeral fix

> **Status:** `in-progress`

- **📊 Model:** opus-4.8 · high · revenue-lane creative polish
- **session:** Normalize spelled-out chapter numerals (Five/Six → 5/6) in The Slow Word EN master for header consistency.
- **started (date -u):** Sun Jul 12 15:37:30 UTC 2026  (born-red first commit)

## ⟲ Previous-session review

Previous-session review: PR #79 landed "The Slow Word" (adult SF novella, 12 EN chapters, ~29,400 words) under candidates/adult-novels/. Two chapter files (05, 06) shipped with spelled-out H1 numerals while the other ten used digits; this session normalizes them.

## 💡 Session idea

Product polish: a sellable manuscript should have consistent chapter headers. Cheap one-line-per-file fix; flagged from the landing report rather than left in the shipped text.

## Scope

- Normalize `en/05-*.md` and `en/06-*.md` H1 numerals to digits.
- Born-red card; strict gate green before push.

## Work log

- Born-red session card opened (first commit).

## Status / outcome

Pending — session in progress.
