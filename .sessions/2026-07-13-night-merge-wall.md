# Session — Night run: The Agent Merge-Wall Cookbook to the owner gate (ORDER 008, PRODUCT #9)

> **Status:** `complete`

- **📊 Model:** fable-5 · worker slice · ORDER 008 night-run product lane
- **session:** PRODUCT #9 of the 2026-07-13 night run — drove
  `candidates/merge-wall-cookbook/` (sweep verdict: needs-build
  medium-heavy) from INTAKE-only to publish-READY per
  `docs/products/TEMPLATE.md`, floor 6/6 executed. The honesty unlock: the
  sweep said the intake's "CI-verified YAML" claim couldn't be fully
  executed in-slice — closed by citing this repo's own LIVE
  `auto-merge-enabler.yml` (@ `305646f`) as the production evidence for
  the primary recipe (real merge events: PR #104 `2026-07-13T00:56:20Z`,
  PR #128 `2026-07-13T02:46:46Z`, both `merged_by github-actions[bot]`,
  read via the API this session), while the one recipe with NO production
  run (`merge-on-green.yml`) is labeled parse-verified-only in its
  header, the listing FAQ, and guide ch.7's per-recipe honesty ledger.
- **started (date -u):** Sun Jul 13 03:09:13 UTC 2026
- **closed (date -u):** Sun Jul 13 03:24 UTC 2026

## ⟲ Previous-session review

Previous session (`.sessions/2026-07-13-night-false-green.md`, PRODUCT #8,
merged `2d972ed`-adjacent wave): its strongest export was the provenance
mechanic — every chapter cites committed file@sha — and this slice reused
it wholesale plus one step further: where false-green's chapters were
citation-verified prose around ONE executed tool, this cookbook's central
recipe is cited to a production system that ran 13 times tonight, which is
a stronger evidence class than any in-slice execution could be. Its 💡
(a PROVENANCE-FOOTER convention in TEMPLATE.md's listing stage) remains
un-adopted and is now two products' worth of validated pattern — both #8
and #9 hand-rolled the same footer; that idea is ripe. Its honest-size
discipline (~8 pages, said so) repeated here almost exactly (~3,500 words,
~8 pages + YAML) — the second consecutive intake whose page estimate
exceeded what committed material supports, which suggests intake page
estimates should be written as ceilings, not targets.

## 💡 Session idea

Production-evidence citations beat in-slice execution for infra products:
"this exact workflow landed PRs #104/#128, merged_by github-actions[bot],
verify it yourself with one API call" is a stronger truth-claim than any
lint run — and it was CHEAPER than authoring a CI harness would have been.
Proposal: TEMPLATE.md stage-3 gains a third evidence class alongside
real-path tests and the honest null — **verified-by-production** (cite the
live in-repo implementation @ sha + at least one real event id it
produced), for products whose subject matter IS the repo's own
infrastructure. The catalog has at least one more candidate shaped like
this (the substrate kit itself), and the class comes with a built-in
honesty rule: anything NOT covered by a production citation must carry an
explicit not-production-run label (this slice's Recipe 2).

## Scope

- `candidates/merge-wall-cookbook/` — NEW build: `guide/` (7 chapters,
  each with a Sources footer citing file@sha), `recipes/` (4 runnable
  GitHub Actions YAMLs: auto-merge-enabler, merge-on-green,
  born-red-hold-gate, advisory-check), buyer README/QUICKSTART/INCLUDED,
  LISTING.md pointer, allow-list `package.sh`, committed dist.
- `docs/launch/merge-wall-cookbook/` — listing-copy.md + owner-actions.md
  (six-field, ARTIFACT sha line, $19 precedent chain).
- `docs/publishing/vetting/merge-wall-cookbook.md` — §7 packet (9th
  product packet); `docs/publishing/OWNER-QUEUE.md` regenerated;
  launch/publishing indexes linked.
- `docs/current-state.md` — sweep line flipped needs-build →
  click-queued (PRODUCT #9); catalog count 5 → 6 click-queued.

## Executed evidence (all 2026-07-13, 03:09–03:24Z)

1. **Source-material map (chapter → committed file@sha):** ch.1 walls
   verbatim ← `docs/PLATFORM-LIMITS.md` @ `2044dc6`; ch.2
   zero-required-checks trap ← same @ `2044dc6` + enabler refuse-to-arm
   guard @ `305646f`; ch.3 enabler ← `auto-merge-enabler.yml` @ `305646f`
   + API-verified merges #104/#128; ch.4 born-red HOLD ← `bootstrap.py` @
   `6c46941` (`BORN_RED_HOLD_MESSAGE`, `IN_PROGRESS_TOKENS`,
   `check_added_card`) + `substrate-gate.yml` @ `4776045`; ch.5 fast lane
   ← `substrate-gate.yml` @ `4776045`; ch.6 advisory ← `kit-tests.yml` @
   `838b46e`; ch.7 REST fallback ← `PLATFORM-LIMITS.md` @ `2044dc6` +
   enabler fallback message @ `305646f`.
2. **Per-recipe parse execution:** all 4 recipes through PyYAML
   `yaml.safe_load` (03:19:20Z) — each a dict with name+jobs
   (enable-auto-merge / merge / required-gate / drift-advisory). Repeated
   from the extracted bundle via the QUICKSTART's own shipped commands
   (PyYAML pass + stdlib structural pass): identical.
3. **Package floor:** double rebuild via allow-list `package.sh` →
   identical sha256
   `8d12a4371850689ed7f1be5b7f13fa0017db98bfa163bc6570edca1306a3c2b0`
   (25,629 B, 14 content files) — committed dist IS that build.
4. **Clean-dir checkout verification:** unzip → inventory 14/14 vs
   INCLUDED.md; all files valid UTF-8 non-empty; 10 markdown files
   H1-headed, balanced fences; **real-secret-shape scan 0 hits** with the
   9 `${{ secrets.GITHUB_TOKEN|MERGE_PAT }}` occurrences documented as
   allowlisted template-variable REFERENCES (GitHub Actions syntax naming
   which secret to read — no values present), not scanned around.
5. **Queue regen (baseline-then-delta):** baseline at HEAD byte-identical
   (19/19 clean, 13 decisions, 100 clicks); with the new packet `parsed
   20 of 20 inputs clean … 14 decisions, 106 owner clicks across 18
   click-run sequences … manual-review — none`; delta vs baseline =
   exactly the new merge-wall D5 group + its 6-click §7 sequence +
   mechanical renumbering (D5→D6…D13→D14). Never hand-edited.
6. **Price:** $19 one-time — set at the candidate's own INTAKE.md,
   recorded identically in listing copy + click-script + packet; chain:
   $15 (kill-rule, false-green) < **$19** = template-packs $19 PWYW
   (PR #108) < $29 SWTK live < $39 < $49.
7. **Honest size verdict:** guide measured 3,531 words (~8 pages) + 4
   recipes (~330 lines commented YAML) + ~950 words README/QUICKSTART —
   the committed material fully supports six chapters; the REST-fallback
   chapter is doctrine-not-production and says so.

## Honest caveats

- No recipe was executed on a GitHub runner in this slice. The enabler's
  evidence class is production citation (live file + real merge events);
  recipes 3–4 are distillations of live production jobs; Recipe 2 has NO
  production evidence anywhere and every surface that mentions it says
  so. The intake's "CI-verified" VERIFIED-WHEN clause was superseded
  honestly in the click-script, not silently met.
- The prose chapters are verified by citation to committed material, not
  by execution; the listing FAQ states this split in buyer terms.
- Platform workarounds rot (the source ledger's own re-verify notes);
  the README honesty box says so.
- No publish action performed; the product parks at §7 owner clicks.
  Conservative expectation per intake: 0–3 sales / $0–$57 first-90-day,
  $0 absent distribution.
