# Session — Night run: candidate sweep + Kill-Rule Intake Kit to the owner gate (ORDER 008, PRODUCT #7)

> **Status:** `complete`

- **📊 Model:** fable-5 · worker slice · ORDER 008 night-run product lane
- **session:** PRODUCT #7 of the 2026-07-13 night run — swept the four
  unpacketed candidates (`cc-cost-lens`, `kill-rule-intake-kit`,
  `merge-wall-cookbook`, `false-green-test-trap`; all four were
  INTAKE.md-only), ranked by distance-to-READY, and drove the closest —
  the **Kill-Rule Intake Kit ($15)** — to publish-READY per
  `docs/products/TEMPLATE.md`, floor 6/6 all executed. Honesty note: the
  kit was NOT idea-only despite having no build yet, because its entire
  content genuinely pre-existed in-repo (venture-eval-001 rubric, the
  lane's real worked intakes, field-manual ch.8's discipline prose, the
  intake-skeleton template) — the build was curation into fillable form,
  the same move template-packs made. The other three stay honestly
  unbuilt with verdicts recorded in `docs/current-state.md`.
- **started (date -u):** Sun Jul 13 02:26:08 UTC 2026
- **closed (date -u):** Sun Jul 13 02:35 UTC 2026

## ⟲ Previous-session review

Previous session (`.sessions/2026-07-13-night-bundle-packet.md`, PR #123,
merged): the bundle slice held the HARD-GATED bar honestly (blocking rows
first, stage-6 N/A-with-reason) and its baseline-then-delta queue-regen
proof was reused here verbatim — baseline at HEAD byte-identical
(`2700b0cc…` unchanged), then delta = exactly one new D-group + mechanical
renumbering (11→12 decisions, 88→94 clicks, 17→18 inputs clean). Its 💡
(machine-readable `blocking[until: …]` gate types) did NOT apply here —
this packet is the catalog's first since SWTK with NO blocking rows and no
freeze lineage, which is itself evidence for that idea: the queue now
carries three blocker kinds plus a fourth "never gated" kind, all
distinguishable only by prose. One carry-forward it flagged twice
(photo-packs → bundle reviews) remains unbuilt after this slice too: the
⏲/KILL-CHECK column — SWTK's 2026-07-19 checkpoint is still invisible in
the derived queue. This slice chose driving a new product over the queue
upgrade because ORDER 008's seat thesis is product quantity; the column is
now THE top backlog debt (three consecutive cards name it).

## 💡 Session idea

The sweep found all four unpacketed candidates carry rich INTAKEs but
zero build, and the one that shipped tonight shipped precisely because
its content already existed as committed lane artifacts. Generalize that
into a sweep heuristic the intake grammar could carry: a one-line
`source-material:` field (committed paths the product would package, or
"none — must be authored") filled at intake time. Distance-to-READY then
becomes greppable — `source-material: none` candidates can never be
"driven tonight" and the night-run picker skips them without re-reading
four full intakes; it also makes fabrication structurally harder, since a
product claiming READY-in-one-slice must point at pre-existing content.

## Scope

- `candidates/kill-rule-intake-kit/` — NEW build: `pack/` (fillable
  INTAKE-TEMPLATE with 61 `[[fill]]` slots, SCORING-RUBRIC with anchors +
  anti-gaming rules, KILL-RULES one-pager, NEGATIVE-LEDGER-TEMPLATE, 2
  worked examples adapted/redacted from the lane's real merge-wall (3.55)
  and cc-cost-lens (3.10) intakes), README/QUICKSTART/INCLUDED buyer docs,
  LISTING.md pointer, allow-list `package.sh` (template-packs pattern),
  `dist/kill-rule-intake-kit-v0.1.zip`.
- `docs/launch/kill-rule-intake-kit/` — NEW: listing-copy.md (parity;
  honesty FAQ) + owner-actions.md (six-field, ARTIFACT sha, precedent
  chain).
- `docs/publishing/vetting/kill-rule-intake-kit.md` — NEW seventh product
  packet; `docs/publishing/OWNER-QUEUE.md` regenerated; index rows in
  `docs/publishing/README.md`, `docs/launch/README.md`;
  `docs/current-state.md` catalog row + sweep verdicts.

## Floor 6/6 evidence (all executed 2026-07-13, 02:29–02:33Z)

1. **Build/package:** `package.sh` double rebuild → identical
   sha256 `53a840fd6b4f0860accecff8d2bbc16abeab06e1d2bb38e03251ca8993a770e5`
   (15,875 bytes, 9 content files).
2. **Tests → honest null:** zero-runtime product; executed substitute from
   the extracted bundle in a clean dir: 9/9 files valid UTF-8, non-empty,
   H1-headed, balanced fences; example arithmetic recomputed in Python
   (3.55 ✓ / 3.10 ✓, weights sum 1.00 ✓).
3. **Price:** $15 one-time, set at intake, cited to the catalog chain
   ($15 < $19 PWYW #108 < $29 live #86 < $39 #110 < $49 #106).
4. **Listing:** short description 196 ≤ 200 chars; claims checked against
   the extracted bundle; explicit "what was NOT machine-verified" FAQ.
5. **Checkout/format:** clean-dir unzip, inventory matches INCLUDED.md
   9/9, secret-pattern scan 0 hits, no junk entries.
6. **§7 packet + queue:** derive_owner_queue.py — baseline at HEAD
   byte-identical first, then 18/18 inputs clean, delta = new D2 group
   only; no freeze applies (zero-runtime, no payment path).
