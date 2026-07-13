# Session — Night run: The False-Green Test Trap to the owner gate (ORDER 008, PRODUCT #8)

> **Status:** `complete`

- **📊 Model:** fable-5 · worker slice · ORDER 008 night-run product lane
- **session:** PRODUCT #8 of the 2026-07-13 night run — drove
  `candidates/false-green-test-trap/` (sweep verdict: needs-build medium)
  from INTAKE-only to publish-READY per `docs/products/TEMPLATE.md`,
  floor 6/6 executed. Guide assembled ONLY from committed repo material,
  every chapter with a provenance footer citing file@sha; the runnable
  stdlib-only offline `vendor_fixture.py` authored AND executed
  end-to-end against SWTK's committed sample payload. **Honest size
  verdict:** the material supports ~3,600 words (~8 pages), not the
  intake's ~15-page estimate — scoped down, said so in the bundle README,
  listing FAQ, and packet verdict, rather than padding.
- **started (date -u):** Sun Jul 13 02:51:04 UTC 2026
- **closed (date -u):** Sun Jul 13 03:04 UTC 2026

## ⟲ Previous-session review

Previous session (`.sessions/2026-07-13-night-queue-killcheck.md`,
PR #128, merged `53f6b65`): the ⏲/KILL-CHECK slice closed THE
three-card-streak backlog debt exactly as scoped — packet-level token,
tolerant parser, earliest-first rendering — and its strongest move, the
both-sides byte-identity regen proof (baseline at HEAD AND post-change on
the untouched tree), is the reason this slice could trust the generator
blindly: my regen came back 19/19 clean with the delta being exactly one
D-group + one click sequence + renumbering. Its 💡 (`check_kill_clocks.py`
DUE/OVERDUE advisory) did not apply to this product slice and remains the
named next infra debt; its own KILL-CHECK line for SWTK rendered correctly
in tonight's regen stdout (`⏲ … next checkpoint 2026-07-19`), which is
live confirmation its feature works on a packet set it never saw.

## 💡 Session idea

This guide's credibility mechanic — every chapter ends with a provenance
footer citing committed file@sha, in a public repo the buyer can audit —
is itself a reusable product pattern: "auditable non-fiction." The
candidate-sweep card proposed a `source-material:` intake field; this
slice suggests its buyer-facing twin: a `PROVENANCE-FOOTER` convention in
TEMPLATE.md's listing-copy stage for any guide-shaped product ("claims
verified by citation" as a listed, checkable feature — the FAQ's
"auditably no invented stories" line converted into a floor row). It
would make honesty a visible differentiator against the free-content
competition every methodology product faces, at near-zero marginal cost
since the citations must exist anyway to pass the TRUTH bar.

## Scope

- `candidates/false-green-test-trap/` — NEW build: `guide/` (7 chapters,
  each citing its committed sources), `vendor_fixture.py` (stdlib-only,
  offline, fail-closed on secrets, nulls enumerated, `--redact-emails`),
  `test_vendor_fixture.py` (8 tests), `examples/` (SWTK-provenance
  sample + README), buyer README/QUICKSTART/INCLUDED, LISTING.md pointer,
  allow-list `package.sh`, committed dist.
- `docs/launch/false-green-test-trap/` — listing-copy.md +
  owner-actions.md (six-field, ARTIFACT sha line, $15 precedent chain).
- `docs/publishing/vetting/false-green-test-trap.md` — §7 packet (8th
  product packet); `docs/publishing/OWNER-QUEUE.md` regenerated;
  launch/publishing indexes linked.
- `docs/current-state.md` — sweep line flipped needs-build →
  click-queued (PRODUCT #8); catalog count 4 → 5 click-queued.

## Executed evidence (all 2026-07-13, 02:51–03:04Z)

1. **Source-material map (chapter → committed file@sha):** ch.1 war story
   ← `control/inbox.md` ORDER 003 @ `c99caa4` +
   `.sessions/2026-07-13-order-003-stripe-path.md` @ `d058c4d` (PR #16
   `912da3e`) + `candidates/membership-kit/server/app.py` @ `dfe3332`;
   ch.2 ← `docs/products/TEMPLATE.md` stage-3 @ `53f6b65`; ch.3–4 ← both
   kits' `fixtures/PROVENANCE.md` @ `dfe3332`; ch.5 ← both
   `test_http_realpath.py` @ `dfe3332`; ch.6 ← distilled from the above +
   Q-0120 verify-before-claiming lore
   (`.sessions/2026-07-12-heartbeat-2026-07-12b.md` @ `d7896f0` — present
   in-repo only as heartbeat discipline, cited as exactly that); ch.7 ←
   the tool's own executed run.
2. **vendor_fixture.py executed end-to-end** on
   `candidates/stripe-webhook-test-kit/fixtures/checkout_session_completed.json`
   @ `dfe3332` as the pasted sample: exit 0; fixture (1,157 B, sha256
   `4f4b3be1…bb2c55`) + PROVENANCE stub written; **7 null fields
   enumerated incl. `data.object.customer_email`** (the war-story field);
   6 volatile fields flagged; the sample's one email-shaped value flagged
   with the `--redact-emails` hint. Verbatim output shipped in guide
   ch.7. Repeated from the extracted bundle: identical result.
3. **Tests:** `python3 -m unittest test_vendor_fixture` → `Ran 8 tests …
   OK` in the repo dir AND from the extracted bundle in a clean dir.
4. **Package floor:** double rebuild via allow-list `package.sh` →
   identical sha256
   `1d83702b7259191a88e16ae6238758c7fb46cf0c9c4884dfb6514c01487017b4`
   (25,825 B, 14 content files) — committed dist IS that build.
5. **Clean-dir checkout verification:** unzip → inventory 14/14 vs
   INCLUDED.md; all files valid UTF-8 non-empty; all 11 markdown files
   H1-headed, balanced fences; sample JSON parses; secret-pattern scan
   **0 hits** (a first-pass scan caught the test suite's literal fake
   `whsec_` string — fixed by assembling it at runtime, bundle rebuilt,
   all proofs re-run on the final artifact).
6. **Queue regen (baseline-then-delta):** baseline at HEAD packet-set
   byte-identical (18/18 clean); with the new packet `parsed 19 of 19
   inputs clean … 13 decisions, 100 owner clicks across 17 click-run
   sequences … manual-review — none`; delta vs baseline = the new
   false-green D2 group + its 6-click §7 sequence + mechanical
   renumbering (12→13 decisions, 94→100 clicks). Never hand-edited.
7. **Price:** $15 one-time — set at the candidate's own INTAKE.md,
   recorded identically in listing copy + click-script + packet; chain:
   $15 (tied w/ kill-rule-intake-kit) < $19 PWYW < $29 SWTK live < $39 <
   $49.

## Honest caveats

- The prose chapters are verified by **citation to committed material**,
  not by execution; the tool is verified by execution (8/8 + end-to-end).
  The listing FAQ states this split in buyer terms.
- ~8 pages, not the intake's ~15 — the committed material honestly
  supports no more, and the FAQ tells already-disciplined practitioners
  to buy nothing.
- No publish action performed; the product parks at §7 owner clicks.
  Conservative expectation per intake: 0–4 sales / $0–$60 first-90-day,
  $0 absent distribution.
