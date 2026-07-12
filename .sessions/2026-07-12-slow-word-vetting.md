# Session — The Slow Word vetting packet (Tier-1 title #1 → owner-click-ready)

> **Status:** `complete`

- **📊 Model:** Claude (Fable family) · slow-word-vetting
- **session:** advance the book-catalog second revenue line by ONE non-gated
  increment: run the one-pass title-vetting checklist
  (`docs/publishing/CHECKLIST.md`, PR #90) top-to-bottom for **The Slow
  Word** — the publishing plan's Tier-1 title #1 (PR #87, §2) — producing
  `docs/publishing/vetting/the-slow-word.md`: collision re-check, market/price
  verification, packaging gate, drafted listing copy (blurb, categories,
  keywords, KU call), a cover design brief, and the queued ⚑ OWNER-ACTION
  block. Nothing is published; no account, spend, or click is performed.
- **started (date -u):** Sun Jul 12 21:32:48 UTC 2026
- **completed (date -u):** Sun Jul 12 21:35:36 UTC 2026

## Scope

- `docs/publishing/vetting/the-slow-word.md` — new worked vetting packet
  (the checklist template's first per-title instance).
- `docs/publishing/README.md` — index row so the packet is reachable.
- `control/claims/2026-07-12-slow-word-vetting.md` — claim (born-red first
  commit, deleted at close per `control/claims/README.md`).
- This card (born-red first commit; flipped `complete` last commit).
- Does NOT touch `control/inbox.md`, `control/status.md`,
  `control/outbox.md`, or any trigger. No publish/spend/account action —
  §7 of the checklist stays a queued owner block.

## Work log

- Synced `main` fresh; HEAD `67c7066` == `git ls-remote origin main`.
- Inbox check both repos: venture max ORDER 007 (acked ≤007), trading max
  ORDER 011 (acked ≤011) — no unexecuted orders; standing default applies.
- Grounding reads: `docs/current-state.md` @ 67c7066 (SWTK in
  coordinator-owned measurement mode — no buildable pre-click increment;
  book catalog is the sanctioned next lane), `docs/publishing/PUBLISHING-PLAN.md`
  (PR #87), `docs/publishing/CHECKLIST.md` (PR #90),
  `candidates/adult-novels/the-slow-word/` READMEs + DECISIONS.
- Fresh web collision re-check for the exact title (2026-07-12): no
  same-named book surfaced — plan §7 verdict "None — phrase genuinely open"
  holds.
- Measured the manuscript mechanically: 29,662 words across
  `en/01…12-*.md` — novella band confirmed, so the checklist's length step
  rests on a measurement, not a guess.
- Wrote `docs/publishing/vetting/the-slow-word.md` (badge `plan`; linked
  from `docs/publishing/README.md` for reachability): all non-gated
  checklist steps completed with citations; §7 stays a queued six-field
  ⚑ OWNER-ACTION block. Drafted listing blurb v1, 2 categories, 7 keywords,
  content note, KU=yes rationale, and a §6a cover design brief.
- Opened PR #91 READY (non-draft), base `main`; the enabler lands it on
  green — this lane never arms or merges.
- `python3 bootstrap.py check --strict` pre-flip: only red was the designed
  born-red hold on this card; clean at flip.

## Status / outcome

**Complete.** The Slow Word — the plan's Tier-1 title #1 — moved from
"planned" to **publish-ready up to the owner gate**: every non-gated
checklist step done and cited; what remains is exclusively the §7 owner
clicks (KDP account, cover approval, price, publish, KU enrollment). No
publish, spend, account, or external action was performed by the seat.

## 💡 Session idea

💡 The vetting packet is machine-checkable owner-readiness: a title is
"owner-click-ready" exactly when its `docs/publishing/vetting/<slug>.md`
has zero unchecked boxes *outside* §7. The ⚑ owner queue could therefore be
*generated* — parse the §7 OWNER-ACTION blocks across `vetting/*.md` and
emit the queue — instead of hand-maintained on the heartbeat, making
"what can the owner click right now?" a derived fact that can never silently
drift from the packets. (Distinct from the prior card's ledger-drift checker,
which watches PR numbers; this derives the owner queue from checklist state.)

## ⟲ Previous-session review

⟲ previous-session review: `.sessions/2026-07-12-current-state-refresh.md`
(PR #90) did exactly what a ledger refresh should — merged-PRs-only, badge
discipline kept, and its CHECKLIST.md turned this session into a fill-in
exercise instead of a re-derivation, which is compounding working as
intended. One honest nit it half-predicts itself: its refreshed "Recently
shipped" tops out at PR #87, so at the instant #90 merged the ledger was
already 3 PRs behind (#88–#90) — the exact silent gap its own 💡
drift-checker idea would flag. The idea is worth building before the gap
grows teeth.

## Deliverable summary

`docs/publishing/vetting/the-slow-word.md` (+ index row in
`docs/publishing/README.md`): the first worked instance of the title-vetting
checklist. Collision "None" double-confirmed same-day; length measured
(29,662 words); $4.99 at the verified 70% band (≈$3.49/sale, base case
$0); listing copy + cover brief drafted in-repo; queued ⚑ OWNER-ACTION
publish block. Landing: READY `claude/`-headed PR #91, born-red card first
commit, claim released at close.
