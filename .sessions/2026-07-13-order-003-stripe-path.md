# Session — ORDER 003 re-verification (real Stripe path) + ORDER 007 terminal ack

> **Status:** `complete`

- **📊 Model:** fable-5 · worker slice · ORDER 003 audit + ORDER 007 close
- **session:** dispatched to execute ORDER 003 (P0 real-Stripe-path fix); found it ALREADY LANDED (PR #16, squash `912da3e`, 2026-07-11) — this slice re-verifies every D-item live at HEAD instead of re-implementing, and records ORDER 007 as satisfied (both PRs terminal, live-verified via GitHub MCP)
- **started (date -u):** Sun Jul 13 00:51:19 UTC 2026
- **closed (date -u):** Sun Jul 13 00:53:30 UTC 2026

## ⟲ Previous-session review

Previous-session review: PR #16 (`912da3e`) fixed the real Stripe path per ORDER 003 (D1a `customer_details.email`, D1b `{CHECKOUT_SESSION_ID}`, D3 loud MOCK banner, D2 README v0.2, vendored-fixture HTTP tests, both zips rebuilt); PR #22 unfroze ⚑B/⚑D on that gate; PR #103 (`c99caa4`) landed owner ORDER 008 (night-run) minutes before this slice branched. No regressions found — every PR #16 fix is still present and green at HEAD `c99caa4` (evidence below). Note: the coordinator relay of 2026-07-13 states the ⚑B publish-click freeze STANDS; this slice adds no §7 publish-click blocks.

## 💡 Session idea

An ORDER can be re-dispatched after it already shipped — the cheap, honest response is a verification slice, not a re-implementation: re-prove each done-when item live at HEAD (code markers, test runs, artifacts) and cite the original landing, so the dispatcher gets evidence instead of duplicate work. Follow-up worth extracting: a tiny `scripts/verify_order.py` that maps ORDER ids to their done-when evidence commands.

## Scope

- Re-verify ORDER 003 D1a/D1b/D2/D3 + HTTP-layer real-path tests + rebuilt zips are present and green at HEAD (`c99caa4`), with file-level evidence — no re-implementation of already-merged work.
- ORDER 007: live-confirm PR #51 / PR #57 terminal state; append the satisfied-note to the ORDER 007 thread in `control/inbox.md` (coordinator-directed, append-only).

## Work log — ORDER 003 verified ALREADY DONE at HEAD `c99caa4`

Original landing: PR #16 squash `912da3e` (2026-07-11); CI kit-tests run 29135371209 job `membership-kit-tests` green; adversarial verification 9/9 (see `docs/launch/membership-kit/owner-actions.md`).

Live re-verification this slice (2026-07-13, HEAD `c99caa4`):

- **D1a** — `candidates/membership-kit/server/app.py`: grant path prefers `customer_details.email` with legacy `customer_email` fallback (lines ~404–414); buyer email passed into Checkout Session creation as `customer_email` (~595, ~624). PRESENT.
- **D1b** — success_url uses `{CHECKOUT_SESSION_ID}` only (~619–620); no `{CHECKOUT_EMAIL}` anywhere in the kit. PRESENT.
- **Real-path HTTP tests** — vendored fixtures `server/fixtures/checkout_session_completed.json` (+ legacy-email variant, PROVENANCE.md); `python3 -m unittest test_http_realpath -v` → `Ran 9 tests in 4.541s` / `OK`; `test_membership` → `Ran 15 tests in 0.008s` / `OK`; `test_supabase_store` → `Ran 12 tests in 6.049s` / `OK`. GREEN.
- **D2** — `candidates/membership-kit/README.md` headline is v0.2 with the HTTP-layer verification note. PRESENT.
- **D3** — loud MOCK banner: `MOCK_WARNING` + `_loud_banner` in `app.py` (~56–79), QUICKSTART leads with the MOCK-MODE warning. PRESENT.
- **Zips** — `dist/membership-kit-v0.2.zip` (39,955 B) and `template-packs/dist/template-packs-v0.1.zip` (12,989 B) committed. PRESENT.
- `python3 bootstrap.py check --strict` at HEAD before this branch: `check: all checks passed.`

Verdict: nothing to re-implement; all six ORDER 003 task items evidenced done. The ⚑B/⚑D click state is the coordinator's call (relay 2026-07-13: freeze STANDS) — untouched here.

## Work log — ORDER 007 satisfied (ack recorded HERE; inbox write structurally impossible)

Live via GitHub MCP 2026-07-13T00:49Z: PR #51 `state: closed`, `merged: false` (closed 2026-07-12T09:39:15Z); PR #57 `state: closed`, `merged: true` (2026-07-12T09:40:17Z, merged_by menno420, label `do-not-automerge`). done-when "both PRs terminal" MET.

The coordinator-directed one-line satisfied-note on the ORDER 007 inbox thread was attempted twice and is FORBIDDEN by the substrate gate, which allows inbox appends to be well-formed `## ORDER` blocks ONLY:
- mid-thread insert → `[inbox-not-append] control/inbox.md changed non-append vs the merge-base — the one-writer/append-only law (control/README.md) allows only additions at the end` (run 29216242073);
- EOF note → `[inbox-order-grammar] malformed ORDER header '## ORDER 007 update · 2026-07-13T00:55Z · ACKED/SATISFIED' — expected `## ORDER <nnn> · <ISO8601> · status: <state>`` (run 29216279657), and non-ORDER appended content is likewise a finding (`bootstrap.py` ~2985–3040).

Both attempts reverted forward — `control/inbox.md` in this PR is byte-identical to `origin/main`. Minting a pseudo-ORDER block to pass the grammar would be lane-authored manager content; declined. Per protocol (`control/README.md`, ORDER 005's own text) done-state lives in `control/status.md`, which is coordinator-owned and out of this slice's write scope — the ack rides THIS card + the worker report for the coordinator to fold into the next heartbeat.

## Guard recipe

If ORDER 003 gets dispatched a third time: the done-when evidence is `candidates/membership-kit/server/app.py` (grep `customer_details` + `CHECKOUT_SESSION_ID`), `server/test_http_realpath.py` (run via `python3 -m unittest test_http_realpath`), and PR #16 `912da3e` — verify, don't rebuild.
