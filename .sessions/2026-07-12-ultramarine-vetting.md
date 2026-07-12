# 2026-07-12 — Ultramarine vetting packet (Tier-1b title-fix worked, parks at the §7 owner gate)

> **Status:** complete

## 💡 Session idea
💡 Blurb-source concordance: every vetting packet quotes 2–3 short anchor
phrases from the manuscript with their chapter locations next to the blurb,
so a reviewer (or the owner) can verify in seconds that the listing copy was
written from the actual text and not invented — cheap to add, makes the
HONESTY check auditable instead of trusted.

## Previous-session review
Previous-session review: `2026-07-12-dashboard-monetization.md` — solid,
rails-honoring slice (feature-gated-not-advice-gated tiers, binding copy
rules with the MAR/MiFID rationale stated, six-field paid-euro gates); one
honest nit: its Outcome section substantially restates the shipped
MONETIZATION.md rather than summarizing it, which bloats the card without
adding audit value.

## Model
- **📊 Model:** Claude (Fable family) · worker · venture/vetting

## Scope

One work increment: the fourth worked instance of the one-pass title-vetting
checklist (`docs/publishing/CHECKLIST.md`), for the publishing plan's Tier-1b
candidate **Ultramarine** (`candidates/adult-novels/ultramarine/`, literary
novella of Delft 1654). Deliverable: `docs/publishing/vetting/ultramarine.md`
(structure mirrors `the-weigh-house.md`) + an index row in
`docs/publishing/README.md`. Pre-work verified this session: word count
measured mechanically (27,865 by `wc -w` on `manuscript/ultramarine.md` —
matches the plan §2 figure), story arc read and confirmed complete (opening,
middle, and a real resolved ending; no placeholder/TODO/fill markers), and the
plan's **Strong** title collision re-confirmed live (Navarro 2025, Lowry 1933,
Warhammer 40k *Ultramarines*) with two vetted rename alternatives. All
publish/money/account actions are ⚑ OWNER-gated in the packet's §7 — this
session takes none of them and does not retitle any manuscript file. Touches
only the packet, the README index row, the claim file, and this card;
`control/status.md`, `control/outbox.md`, and triggers untouched.

## Outcome
Packet landed at `docs/publishing/vetting/ultramarine.md` (@ `f2d8521`) +
index row in `docs/publishing/README.md`; PR #98 opened READY. Title-fix
worked: rename recommended to **The Widow's Blue — "A Novel of Delft,
1654"** (⚑ OWNER pick; *The Blue Hour* rejected on Paula Hawkins 2024);
$4.99 / KU-yes calls; blurb/categories/keywords/cover brief from the text;
§7 OWNER-ACTION block queued, nothing published. kit-tests green on the
packet commit; this final commit flips the born-red hold.
