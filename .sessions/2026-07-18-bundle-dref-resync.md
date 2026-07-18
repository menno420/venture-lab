# Session — Resync stale bundle D-refs + fix lint_owner_gates DONE marker

> **Status:** `complete`

- **📊 Model:** opus-4.8 · high · docs-only
- **started (date -u):** Sat Jul 18 22:11 UTC 2026
- **branch:** `claude/bundle-dref-resync`
- **base:** `main@1809c7e`
- **purpose:** PR #244 folded the CORS SKU into `docs/publishing/OWNER-QUEUE.md`
  as new **D4**, shifting every alphabetically-later decision ID +1. Two
  sellable-bundle doc families still carry STALE decision-ID (D-ref)
  cross-references from an older numbering (last touched by PRs #231/#239), so
  after the #244 renumber they now MISPOINT to the wrong SKUs' owner-queue rows.
  `bootstrap --strict` does not catch this (it is a semantic cross-ref, not a
  syntax error), but an owner who follows a bundle's owner-actions would land on
  the wrong queue row. This slice resyncs every mispointed bundle D-ref to the
  LIVE OWNER-QUEUE numbering and fixes a half-flipped `— DONE` marker on an
  UNCHECKED ⚑ Owner box that makes `scripts/lint_owner_gates.py` FAIL.
- **source of truth:** `docs/publishing/OWNER-QUEUE.md` (D1–D28, generated) —
  the live map was derived from its `### D<n> — <Title>` headings:
  D6=GitHub Webhook, D7=Idempotency Key, D9=JWT Auth, D15=Pagination,
  D18=Rate-Limit, D19=Shopify Webhook, D20=Slack Webhook.
- **scope (files):** api-robustness-bundle family (owner-actions.md,
  listing-copy.md, vetting packet, MANIFEST.json — and the sibling candidates
  README.md/PROVENANCE.md that carry the same live `queued (OWNER-QUEUE D<n>)`
  pointer) + webhook-verifier-bundle family (same set). Plus the lint DONE-marker
  fix in `docs/publishing/vetting/webhook-verifier-bundle.md`. OWNER-QUEUE.md is
  NOT touched (it is the authority; confirmed byte-identical). No point-in-time
  snapshots (`.sessions/*`, `control/inbox.md`/`outbox.md`, `docs/NEXT-*.md`,
  `docs/current-state.md`) touched. The binary `dist/*.zip` build snapshots are
  left alone (no test compares them to live docs). Plus claim + this born-red
  card + a `control/status.md` heartbeat. Born-red card holds substrate-gate red
  until the completion flip.

## 💡 Session idea

💡 **A `scripts/check_bundle_drefs.py` advisory that proves every
`OWNER-QUEUE D<n>` pointer in the sellable-bundle doc families resolves to the
correct SKU in `OWNER-QUEUE.md`.** This slice's bug was invisible to every gate:
`bootstrap --strict` is semantic-blind to cross-refs, `lint_owner_gates.py`
validates a packet's OWN §7 grammar but never checks that a cited `D<n>` points
at the intended SKU, and `test_bundle.py` only checks pricing + zip presence. So
when PR #244's CORS fold renumbered the shared decision IDs, the bundle families
(`docs/launch/*-bundle/`, `docs/publishing/vetting/*-bundle.md`,
`candidates/*-bundle/{MANIFEST.json,README.md,PROVENANCE.md}`) silently kept
pointing at the wrong queue rows — an owner following them would land on the
wrong decision, with nothing red. The prior card (owner-queue-cors-fold, PR #244)
already proposed a `check_catalog_drefs.py` for CATALOG↔OWNER-QUEUE drift and
named the bundle `PROVENANCE.md` rows as the stretch target; this is that stretch
made concrete for the whole bundle family. The fix is a tiny stdlib checker that
parses OWNER-QUEUE's `### D<n> — <Title>` headings into a D→SKU map, then for each
bundle-family occurrence of `queued (OWNER-QUEUE D<n>)` / `OWNER-QUEUE **D<n>**` /
`(D<n>)` sitting next to a kit-name token, asserts the cited `D<n>`'s title
contains that SKU's token — emitting a `bundle-dref-drift` advisory (never
exit-affecting, same class as `lint_owner_gates.py`) on any mismatch. That turns
the manual "grep every D-ref and eyeball the SKU" pass I ran this slice into a
standing greppable signal, and it composes with the proposed `check_catalog_drefs`
into one D-ref-integrity family. Guard recipe: new `scripts/check_bundle_drefs.py`
(map regex `^### D(\d+) — (.+)$` over `docs/publishing/OWNER-QUEUE.md`; per-family
scan of the six doc kinds; per-SKU kit-name→token table: idempotency/jwt/pagination/
rate-limit and github/slack/shopify/stripe), wired as an advisory into
`bootstrap.py check` alongside the existing linters; test target a fixture bundle
doc with one shifted D-ref asserting the one advisory fires and a clean fixture
staying silent.

## previous-session review

previous-session review: `.sessions/2026-07-18-owner-queue-cors-fold.md`
(PR #244, `1809c7e`) — the CORS-into-OWNER-QUEUE fold that caused (and correctly
predicted) this slice's bug. #244 was a clean, disciplined regen: it added CORS
as **D4** via the derive script, shifted every later decision +1, and hand-resynced
all 38 CATALOG D-refs — the right restraint being that it deliberately scoped the
bundle-family `candidates/*/PROVENANCE.md` staleness OUT and flagged it (plus the
missing cross-ref gate) as an explicit follow-up rather than ballooning the PR.
That follow-up is exactly this slice, and #244's clean CATALOG resync + unchanged
§1 numbering gave me a trustworthy source-of-truth map to fix the bundles against.
Its 💡 even named the `candidates/*/PROVENANCE.md` drift as live-proof-unguarded —
which this slice both fixes and turns into the standing checker proposed above.

## Work log

- 2026-07-18T22:11Z — Branch `claude/bundle-dref-resync` from origin/main
  (`1809c7e`); collision check clean. Derived the live D-ref → SKU map from
  OWNER-QUEUE and confirmed the expected corrections. Claim + born-red card
  committed (first commit), pushed. Build begins.
- 2026-07-18T22:12Z — PR #245 opened READY (non-draft) with the plain
  Before/After, the per-file before→after D-ref table, and the verification plan.
- 2026-07-18T22:15Z — **Conflict surfaced + resolved.** Discovered OWNER-QUEUE.md
  is a GENERATED file whose §2 bundle click-run rows derive from the bundle
  vetting packets' §7 blocks — so fixing those §7 cross-refs (explicit targets)
  regenerates OWNER-QUEUE, contradicting the "byte-identical" verify bullet.
  Reported to the coordinator with the finding + facts (no CI gate enforces
  derive-drift; repo header requires re-running derive after any packet change).
  Coordinator ruled **OPTION A**: regenerate via the script (the byte-identical
  bullet was superseded — the packets ARE the queue's source), keep the
  candidates README/PROVENANCE fixes, keep the lint reword, leave dist zips alone.
- 2026-07-18T22:18Z — **Build.** Applied all D-ref corrections
  (context-verified against kit names + packet filenames): api-robustness
  Idempotency D6→D7 / JWT D7→D9 / Pagination D13→D15 / Rate-Limit D16→D18;
  webhook-verifier GitHub D5→D6 / Slack D14→D20 / Shopify D13→D19; across
  owner-actions, listing-copy, vetting packet, MANIFEST.json, README.md,
  PROVENANCE.md in both families. Regenerated OWNER-QUEUE via
  `scripts/derive_owner_queue.py` (only the 7 §2 bundle rows changed; §1 numbering
  unchanged, CORS still D4). Removed the stray `— DONE 2026-07-12` on the UNCHECKED
  Shopify owner box (reworded to "already live since 2026-07-12"; no false
  done-mark). Committed + pushed; PR body updated to record the regen.
- 2026-07-18T22:20Z — **Verification.** Bundle D-ref grep: api family = {D7, D9,
  D15, D18} only, webhook family = {D6, D19, D20} only — each resolves to the
  intended SKU. `derive_owner_queue.py` idempotent (re-run byte-identical). §1 map
  = 28 decisions; all 19 CATALOG positioning headers + table rows still resolve
  (CATALOG untouched). `lint_owner_gates.py` OK — 58 inputs clean (was 1 FAIL).
  `test_derive_owner_queue.py` 13/13 OK. `test_bundle` 8/8 OK in both bundle dirs.
- 2026-07-18T22:22Z — Heartbeat to `control/status.md` (neutral in-flight note,
  others' sections intact), committed + pushed.
- 2026-07-18T22:2xZ — Flip to `complete` (this commit): Status badge, 📊 Model
  line, one 💡 idea, previous-session review, every auto-draft slot resolved.
  `python3 bootstrap.py check --strict` EXIT 0 (advisories only). Born-red HOLD
  clears.
