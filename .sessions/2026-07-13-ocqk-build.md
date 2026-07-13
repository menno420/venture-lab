# Session — PRODUCTS build: Owner-Click Queue Kit (OCQK, $19) to publish-READY

> **Status:** `complete`

- **📊 Model:** Claude Fable (fable-5) · worker · PRODUCTS lane, build slice
- **session:** build the Owner-Click Queue Kit — the #2 BUILD verdict (3.60)
  from `docs/products/ideas-2026-07-13.md` §2 (PR #142) — to the ORDER 008
  publish-READY quality floor per `docs/products/TEMPLATE.md`: built +
  tested (38-test parse/derive/lint/hostile suite, wired into CI) + priced
  $19 + listing drafted + checkout/format verified (double rebuild,
  clean-dir unzip, tests from the extracted zip) + sha256 pinned + ⚑ owner
  clicks queued in a §7-parseable packet + OWNER-QUEUE regenerated + INTAKE
  kill-rule fields bound. No spend, no accounts, no external publish — the
  path ends at a queued owner click.
- **started (date -u):** Mon Jul 13 10:08:29 UTC 2026
- **completed (date -u):** Mon Jul 13 10:26:30 UTC 2026

## Scope

- `candidates/owner-click-queue-kit/` — the pack: `ocq.py` (stdlib derive
  tolerant/advisory + lint strict), `GRAMMAR.md` (gate-block grammar +
  six-field detail convention), `GOTCHAS.md` (10 production lessons),
  worked examples (agent-fleet + solo-repo, committed EXPECTED outputs),
  `test_ocq.py` (38 tests), `INTAKE.md` (internal), allow-list
  `package.sh`, `dist/` zip.
- `docs/launch/owner-click-queue-kit/` — `listing-copy.md` +
  `owner-actions.md` (six-field click-script).
- `docs/publishing/vetting/owner-click-queue-kit.md` — §7-parseable packet
  (+ index row in `docs/publishing/README.md` for docs-gate reachability).
- `docs/publishing/OWNER-QUEUE.md` — regenerated (never hand-edited).
- `.github/workflows/kit-tests.yml` — one added job running the pack's
  suite (same convention as the GWTK job).
- `control/claims/2026-07-13-ocqk-build.md` — claim (deleted in this ender).
- This card (born-red first commit `bc8937f`; flipped `complete` last).
- Does NOT touch `control/inbox.md`, `control/status.md`,
  `control/outbox.md`, any trigger, or the auto-merge enabler. Never arms
  or merges its own PR.

## Work log

- Hard-synced `main` to `origin/main` (HEAD `6ecc460`, PR #150 merge);
  tree was clean, no rescue branch needed. Inbox read at HEAD: ORDERs
  001–009, nothing newer than 009, nothing pre-empting the products lane —
  ORDER 008's products clause drives this slice. Claims scan: night-report
  + round2-idea-packets claims only, both disjoint scopes → claimed
  `control/claims/2026-07-13-ocqk-build.md` (commit `16e0aca`).
- Studied the exemplars end-to-end: the two newest packs (GWTK PR
  #147/#150, SWTK), `docs/products/TEMPLATE.md`, and — since it IS the
  subject matter — `scripts/derive_owner_queue.py` + the live OWNER-QUEUE
  + the GWTK packet's §7 form.
- Built the pack (commit `453302e`) as a **generalization, not a copy**:
  `ocq.py` drops the repo couplings (keyword-map conflict scan, "Title
  Vetting —" H1 prefix, fixed vetting dir) and adds what a buyer needs
  that the repo script never had — a strict `lint` mode (exit 1, per-file
  errors: defaultless decisions, half-flipped DONE rows, calendar-invalid
  dates), output-file self-skip, EXPECTED-file hygiene, repeatable
  `--gates`. GRAMMAR.md documents both layers (parseable gate block +
  six-field convention); GOTCHAS.md ships 10 lessons this repo actually
  hit (incl. the #150 generated-file merge race and the
  proposal-not-authorization rule).
- **Executed evidence (all 2026-07-13):** suite `Ran 38 tests in 0.028s /
  OK` from source (10:17:14Z) and `38 passed` under pytest; both worked
  examples derive byte-identical to their committed EXPECTED outputs and
  lint OK; double rebuild 10:18:35Z → identical sha256
  `f81f1b4eb39194ef96551b24bb20ffbd6f15aac07543fba2f894c670734564e7`
  (28,712 B, 12 content files); clean-dir unzip 10:18:50Z → inventory
  12/12, suite `Ran 38 tests in 0.023s / OK` from the extracted zip,
  example re-derived from the extracted copy byte-identical,
  real-secret-shape scan 0 hits.
- Launch assets + packet + queue (commit `471307a`): listing-copy.md
  (Short 189 chars measured), owner-actions.md (six-field, ARTIFACT sha
  pinned, price chain at the merge-wall $19 rung), vetting packet §7 with
  5 ⚑ owner rows + post-click KILL-CHECK arming step
  (verified-by-production citations: PR #147 squash `44d2a5e`, PR #150
  squash `6ecc460`), publishing README index row, `kit-tests.yml` job
  (YAML parse-checked), OWNER-QUEUE regen: `parsed 32 of 32 inputs clean
  … 17 decisions, 171 owner clicks across 30 click-run sequences`, OCQK =
  D7 default **Gumroad**, manual-review none (10:22:54Z).
- Verification: `python3 bootstrap.py check --strict` pre-flip — only red
  was the designed born-red HOLD on this card; clean at flip. All four
  kit-tests suites green locally the exact CI way (membership-kit 36 OK,
  SWTK 14 OK, GWTK 18 OK, OCQK 38 OK — 10:23:50Z).
- main moved under the branch mid-slice (`6ecc460` → `f15e9f1`, PRs
  #148/#149) — manuscripts only, zero packet/queue overlap, no re-derive
  needed at open time. Opened PR #153 READY (non-draft), base `main`; the
  enabler lands it on green — this lane never arms or merges its own PRs.

## Status / outcome

**Complete.** The products lane's eleventh packet is queued: OCQK v0.1 is
publish-READY to the full TEMPLATE.md floor, and the product is the
lane's own control surface made sellable — its publish click rides the
exact mechanism it ships (the §7 block of its packet parsed clean by the
production deriver, D7 in the regenerated queue). Every floor item is
executed evidence: byte-identical determinism pinned against committed
EXPECTED outputs, a strict lint contract the repo's own script never had,
a reproducible dist verified from the artifact side, and hostile-input
tests proving queue entries stay data. Honest ceiling: it's
conventions-plus-one-script in a small-population channel — conservative
$0 absent distribution, kill clock arms at T+30.

## 💡 Session idea

💡 **Dogfood-gap mining: diff the productized copy against the production
original and ship the deltas back.** Generalizing
`derive_owner_queue.py` for sale forced a list of things the production
script lacks that the KIT now has: a strict lint mode (the repo has no
CI check that a packet's §7 stays parseable — malformed packets are only
caught by eyeballing derive stdout), real-calendar-date validation (the
repo regex accepts 2026-13-45), and output-file self-skip. That diff is
a ready-made, pre-scoped upgrade PR for the production system — and the
pattern generalizes: every time the lane packages an internal system for
sale, the "what would a buyer need that we never built" list is ALSO the
production system's gap list. Candidate follow-up: port `lint` back as
`scripts/lint_owner_gates.py` + a kit-tests advisory step.

## ⟲ Previous-session review

⟲ previous-session review: `.sessions/2026-07-13-gwtk-build.md` — the
template-reuse thesis it proved (SWTK → GWTK in one session) held again
on a DIFFERENT product shape: this slice reused its ritual skeleton
(born-red → claim → pack → launch assets → regen → READY PR) 1:1 and
landed in ~18 minutes of wall clock, so the cost curve is the ritual,
not the product type. Two nits: (1) its card's "25 of 25 inputs clean"
queue line was stale within hours (round-2 book packets landed; this
regen parsed 32) — queue-size claims in cards should be read as
at-that-HEAD, which the card did say but only implicitly; (2) its 💡
(ship the vendor's known-answer test as a product feature) didn't apply
here — OCQK has no upstream vendor constant — but its GOTCHAS-from-
production discipline transferred as the kit's main moat, which supports
the 💡's underlying rule: convert TRUTH-bar work into listed features.

## Deliverable summary

`candidates/owner-click-queue-kit/` v0.1 (12-file buyer bundle, sha256
`f81f1b4e…734564e7`, byte-reproducible) + `docs/launch/owner-click-queue-kit/`
(listing + six-field click-script) + vetting packet #11 with a 5-click §7
run (D7 default Gumroad) + OWNER-QUEUE regenerated (32/32 clean) +
`owner-click-queue-kit-tests` CI job. Landing: READY PR #153, born-red
card first commit (`bc8937f`), claim `16e0aca` released in this ender,
pack `453302e`, launch assets `471307a`.
