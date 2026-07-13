# Session — PRODUCTS build: GitHub Webhook Test Kit (GWTK, $29) to publish-READY

> **Status:** `complete`

- **📊 Model:** Claude Fable (fable-5) · worker · PRODUCTS lane, build slice
- **session:** build the GitHub Webhook Test Kit — the #1 BUILD verdict (3.60)
  from `docs/products/ideas-2026-07-13.md` (PR #142, squash `49fcf1e`) — to
  the ORDER 008 publish-READY quality floor per `docs/products/TEMPLATE.md`:
  built + tested (real-path HTTP suite, wired into CI like SWTK's) + priced
  $29 + listing drafted + checkout/format verified (double rebuild, unzip,
  tests from the extracted zip) + sha256 pinned + ⚑ owner click queued in a
  §7-parseable packet + OWNER-QUEUE regenerated + INTAKE kill-rule fields
  bound. No spend, no accounts, no external publish — the path ends at a
  queued owner click.
- **started (date -u):** Mon Jul 13 09:39:15 UTC 2026
- **completed (date -u):** Mon Jul 13 09:56:30 UTC 2026

## Scope

- `candidates/github-webhook-test-kit/` — the pack: harness (`gwtk.py` +
  `gwtk.js`), example correct handler, vendored real GitHub payload fixtures
  + `fixtures/PROVENANCE.md`, real-path HTTP test suite, `GOTCHAS.md`,
  `INTAKE.md`, allow-list `package.sh`, `dist/` zip.
- `docs/launch/github-webhook-test-kit/` — `listing-copy.md` +
  `owner-actions.md` (six-field click-script).
- `docs/publishing/vetting/github-webhook-test-kit.md` — §7-parseable packet
  (+ index row in `docs/publishing/README.md` for docs-gate reachability).
- `docs/publishing/OWNER-QUEUE.md` — regenerated (never hand-edited).
- `.github/workflows/kit-tests.yml` — one added job running the pack's
  real-path suite (same convention as the SWTK job).
- `control/claims/2026-07-13-gwtk-build.md` — claim (deleted in this ender).
- This card (born-red first commit `5d7d14c`; flipped `complete` last).
- Does NOT touch `control/inbox.md`, `control/status.md`,
  `control/outbox.md`, any trigger, or the auto-merge enabler. Never arms or
  merges its own PR.

## Work log

- Hard-synced `main` to `origin/main` (HEAD `58cdb14`, PR #144 merge);
  pre-sync dirt (one appended `.substrate/guard-fires.jsonl` line) preserved
  on local rescue branch `rescue/2026-07-13-gwtk-presync`.
- Inbox read at HEAD: ORDERs 001–009, nothing newer than 009, nothing
  pre-empting the products lane — ORDER 008's products clause drives this
  slice. Claims scan: only the night-report claim (disjoint scope) →
  claimed `control/claims/2026-07-13-gwtk-build.md` (commit `b5227a8`).
- Studied the LIVE exemplar end-to-end: `candidates/stripe-webhook-test-kit/`
  (harness/stub/tests/package.sh), its vetting packet + click-script +
  LISTING, `docs/products/TEMPLATE.md`, `scripts/derive_owner_queue.py`
  grammar, the merge-wall packet (most recent queued-§7 form).
- **Sourced the GitHub facts in-session, never from memory** (SWTK's
  vendored-fixture discipline): 5 payloads fetched verbatim from
  `octokit/webhooks @ main` `payload-examples/api.github.com/` (per-file
  sha256 pinned in PROVENANCE.md); signature scheme + official test vector
  from `github/docs @ main`
  `content/webhooks/using-webhooks/validating-webhook-deliveries.md`;
  delivery headers from `webhook-events-and-payloads.md`; replay/GUID
  guidance from `best-practices-for-using-webhooks.md`; form content type
  from `data/reusables/webhooks/content_type_and_secret.md` (all fetched
  2026-07-13, `docs.github.com` itself not proxy-fetchable).
- Built the pack (commit `813ca09`): `gwtk.py` (fire with
  forge/unsigned/sha1-only/form/replay modes + check-event + vector + list),
  `gwtk.js` Node port (same commands), `stub_handler.py` (constant-time
  sha256, fail-closed missing/downgrade, raw-form-body verify, ping, GUID
  dedupe), `GOTCHAS.md` (6 sourced failure modes), `INTAKE.md` (kill-rule
  fields bound: ≥1 sale OR ≥50 reads in 30 days; T+7/T+30 checkpoints;
  ≤70k budget), fixtures + EVENTS.json + PROVENANCE.md, `package.sh`.
- **Executed evidence (all 2026-07-13):** suite `Ran 18 tests in 4.552s /
  OK` from source (09:44:21Z); every fire mode PASS live against the stub on
  127.0.0.1:18742, BOTH ports (09:45:59Z — forge/unsigned/sha1-only
  rejected 400 with the right reasons, form accepted, replay flagged
  `duplicate: true` on the 2nd delivery); `vector` PASS in Python and Node
  against GitHub's published `sha256=757107ea…` constant; double rebuild
  09:47:54Z → identical sha256
  `e17b08bac25b047942281c00eb0047ae592d6bda790284aade7b6cf58dcbf6a9`
  (36,214 B, 13 files); clean-dir unzip 09:48:06Z → inventory 13/13, suite
  `Ran 18 tests in 4.547s / OK` from the extracted zip, secret-shape scan
  0 hits.
- Launch assets + packet + queue (commit `ba5de3b`): listing-copy.md
  (Short 183 chars measured), owner-actions.md (six-field, ARTIFACT sha
  pinned, price chain at the live-SWTK $29 rung), vetting packet §7 with 5
  ⚑ owner rows + post-click KILL-CHECK arming step, publishing README index
  row, `kit-tests.yml` job, OWNER-QUEUE regen: `parsed 25 of 25 inputs
  clean … 16 decisions, 135 owner clicks across 23 click-run sequences`,
  GWTK = D3 default **Gumroad**, manual-review none.
- Verification: `python3 bootstrap.py check --strict` pre-flip — only red
  was the designed born-red HOLD on this card; clean at flip. All three
  kit-tests suites green locally the exact CI way (membership-kit 36 OK,
  SWTK 14 OK, GWTK 18 OK); workflow YAML parses with the new job.
- Opened PR #147 READY (non-draft), base `main`; the enabler lands it on
  green — this lane never arms or merges its own PRs.

## Status / outcome

**Complete.** The products lane's tenth packet is queued: GWTK v0.1 is
publish-READY to the full TEMPLATE.md floor — the SWTK template genuinely
made product N+1 cheaper (one session, ideation-to-queued-click, vs the
multi-session SWTK path). Every floor item is executed evidence, not
assertion: vendored fixtures with per-file shas, GitHub's own published
HMAC vector as an offline known-answer test in the product itself, an
18-test real-path suite green from source AND from the artifact, a
byte-reproducible dist, and a §7 click-run the derive script parses clean.
Honest ceiling: same concentrated channel where SWTK has 0 organic sales —
conservative $0 absent distribution, kill clock armed at T+30.

## 💡 Session idea

💡 **Ship the known-answer vector as a product feature, not just a test.**
The single highest-trust-per-token move in this build was promoting
GitHub's published HMAC test vector from a hidden unit test into a
buyer-facing `vector` command ("prove this kit against GitHub's own docs
constant, offline, before you trust it") — it converts the TRUTH-bar work
the lane does anyway into a listed, checkable differentiator, exactly like
the PROVENANCE-FOOTER convention did for guides. Generalizable rule for
every future protocol/format kit (webhook kits, JWT kit, SAML kit, sitemap
lint…): if the upstream vendor publishes ANY known-answer test, ship a
one-command self-proof against it and name it in the listing. Candidate
for a TEMPLATE.md stage-3 note next time it's touched.

## ⟲ Previous-session review

⟲ previous-session review: `.sessions/2026-07-13-product-ideation.md` — the
scoring discipline held up under build pressure: GWTK's ideation entry
(3.60, provisional kill-rule fields, ≤70k budget) translated 1:1 into this
INTAKE with zero re-derivation, which is the rubric doing its job. Two
honest nits: (1) its buildability-4.5 rationale flagged "GitHub's
delivery/redelivery semantics" as the one learnable unknown — correct call,
that's exactly where the new product surface came from (no-timestamp
replay + GUID dedupe became a fire mode, a stub pattern, and two tests);
(2) its 💡 (machine-readable catalog manifest for collision checks) is now
the third consecutive unbuilt 💡 that card's own review pattern complains
about — this card's collision scan §2 again hand-re-read packet summaries
to check the SWTK/false-green boundary, so the manifest idea has now cost
three sessions the same grep it proposes to eliminate.

## Deliverable summary

`candidates/github-webhook-test-kit/` v0.1 (13-file buyer bundle, sha256
`e17b08ba…8dcbf6a9`, byte-reproducible) + `docs/launch/github-webhook-test-kit/`
(listing + six-field click-script) + vetting packet #10 with a 5-click §7
run (D3 default Gumroad) + OWNER-QUEUE regenerated (25/25 clean) +
`github-webhook-test-kit-tests` CI job. Landing: READY PR #147, born-red
card first commit (`5d7d14c`), claim `b5227a8` released in this ender, pack
`813ca09`, launch assets `ba5de3b`.
