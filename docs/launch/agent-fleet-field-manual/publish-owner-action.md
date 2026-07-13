**STATUS: QUEUED (2026-07-11)**

> **Status:** `owner-guidance`

This publish click is **queued to the owner.** The coordinator seat reviewed
the build + merge + verification evidence below (2026-07-11) and flipped this
from NOT-QUEUED. No agent publishes, spends, or creates accounts — the owner
performs the click.

Note on the payment-path gate: this is a **Gumroad-hosted book** — the
marketplace hosts checkout and delivery, there is **no custom payment path in
this product**, so the lane's D1/Stripe real-path verification gate does not
apply to this publish (it gates products that ship their own payment code).

## Queue evidence (reviewed 2026-07-11, coordinator seat)

- **Merged to main:** PR #41 squash-merged as **`9226e22`** (head `c77ce0d`) under the owner's standing instruction (2026-07-11, event b92aab44).
- **CI green on the merged head `c77ce0d` (all three checks success):** substrate-gate ([run 29161813966 / job 86568058722](https://github.com/menno420/venture-lab/actions/runs/29161813966/job/86568058722)) · membership-kit-tests ([run 29161813941 / job 86568058704](https://github.com/menno420/venture-lab/actions/runs/29161813941/job/86568058704)) · stripe-webhook-test-kit-tests ([job 86568058678](https://github.com/menno420/venture-lab/actions/runs/29161813941/job/86568058678)).
- **NON-AUTHOR spot-review (2026-07-11, this queue slice; card `.sessions/2026-07-11-queue-f-field-manual-publish.md`)** of the two free chapters on merged main — all verdicts **CONFIRMED**, none refuted: ch01 D1 claims match `docs/NEXT-SESSION.md` + PR #16; ch02 claims match PR #22 `6fea90b` / PR #28 `fc7f39c` / `kit-tests.yml` (swtk suite is exactly 14 tests); no invented numbers, no proven-revenue claims; honest-negatives figures match PR #29 `74894e5` (~284k vs 120k, ~2.3×).
- **Zip verified on main:** `candidates/agent-fleet-field-manual/dist/agent-fleet-field-manual-v0.1.zip`, sha256 recomputed = `7eff9235024619a632020c06f7c47da24667f8134c828715694eaa8755a29176` (exact match to the PR claim); extracted HTML's 22 anchor links all resolve, 0 external asset refs.
- **Budget honesty (ledgered):** the build overran its 90k intake cap (~200k, ≈2.2×) — headlined as a NEGATIVE in `control/status.md`; the overrun does not change what the buyer receives, and is disclosed per the lane's own honest-negative rule.

## Evidence (what is built + what CI proved)

1. **The book is built.** Eleven chapters (`candidates/agent-fleet-field-manual/chapters/00-preface.md` … `10-appendix-templates.md`), each lesson cited to a real repository artifact (SHA / PR / file); the two free chapters (01, 02) are also exported as standalone articles in this directory.
2. **The HTML build is verified.** `python3 build.py` produces the single self-contained `dist/agent-fleet-field-manual-v0.1.html` (stdlib only, no external assets); all 11 table-of-contents links resolve to their chapter sections and the "back to contents" links resolve to `#top` — verified from inside the extracted zip.
3. **The zip is byte-reproducible.** `sh package.sh` builds `dist/agent-fleet-field-manual-v0.1.zip` deterministically (pinned mtimes, sorted entries); two consecutive builds produce an identical sha256. It contains README, LISTING, chapters, templates, and the built HTML, and excludes the internal INTAKE and the build tooling.
4. **CI leg — CONFIRMED (2026-07-11):** all three checks (substrate-gate, membership-kit-tests, stripe-webhook-test-kit-tests) ran green on the built head SHA `c77ce0d` with the session card flipped to `complete`; run links in the Queue evidence block above. This is a docs/prose product — there is no runtime test suite to run; verification is the build determinism + the TOC-resolution check above, and the citation map in the PR body (each lesson → its repo artifact).

Honest caveat: this is guide/eBook content in the softest willingness-to-pay
category on the board; the value proposition is *cited honesty about real
failures*, not code utility. Conservative revenue is $0–$156 and $0 without
distribution.

## Owner-action row (six-field grammar)

- **WHAT:** publish Agent Fleet Field Manual v0.1 at **$39** (one-time) on a digital marketplace.
- **WHERE:** Gumroad (gumroad.com → New product → Digital product) or Lemon Squeezy (Products → New), signed into your own account.
- **HOW:** 1) Sign in. 2) New product → Digital product. 3) Name = "Agent Fleet Field Manual". 4) Price = $39, one-time. 5) Upload `candidates/agent-fleet-field-manual/dist/agent-fleet-field-manual-v0.1.zip`. 6) Paste Title / Tagline / Description / Bullets / Who-it's-for / FAQ from `docs/launch/agent-fleet-field-manual/LISTING.md`. 7) Publish. 8) Copy the public product URL.
- **WHY:** revenue-lane candidate #4 (eval-001, score 3.55), un-deferred by owner steer 2026-07-11 (event 4df864d6). Conservative expectation: 0–4 sales / 90 days ($0–$156); $0 without distribution.
- **UNBLOCKS:** the free-chapter validation funnel — once the listing is live and ≥2 free chapters are posted, the 14-day validation clock starts (signal: ≥100 organic reads on a chapter OR ≥5 signups OR first sale).
- **VERIFIED-WHEN:** the live listing URL returns HTTP 200 on a purchasable $39 page **AND** ≥2 free chapters are live (which together start the 14-day validation clock).
- **ARTIFACT (verified 2026-07-13):** upload exactly `candidates/agent-fleet-field-manual/dist/agent-fleet-field-manual-v0.1.zip` @ sha256 `63e71b30d1a194b42f92d8c9197148ec89244cba82688e6c097d5727e6ccee23` (65,283 bytes; byte-reproducible via `package.sh` — double rebuild identical, both `date -u` 2026-07-13 ~01:28Z). This supersedes the earlier sha `7eff9235…a29176` in the queue-evidence block above: the 2026-07-13 night slice fixed a bundle defect — the in-zip README's "rebuild it yourself" instructions referenced `build.py`/`package.sh`, which the old bundle excluded; the refreshed bundle ships both (stdlib-only), and the fix is proven buyer-side: extracting the zip and running `python3 build.py && sh package.sh` from the extracted copy regenerates the byte-identical zip (same sha256). Chapter/template/HTML content is unchanged from the non-author-reviewed v0.1 text; the refresh adds the 2 tooling files and updates the bundle README/LISTING inventory + a stale NOT-QUEUED cross-ref only. Zero-runtime product (prose + stdlib build tooling — no test suite by design); executed verification from the extracted bundle: 19/19 files non-empty valid UTF-8; HTML has 0 external src/href refs, 0 script tags, all 12 in-page anchors resolve, FREE badges present on chapters 01/02; secret-pattern scan zero hits; no junk entries.

No secret values are involved in this action — nothing in this product reads or
stores a secret; environment-variable *names* only appear in the book's
templates as guidance. The owner performs the click; the coordinator queues this
only after reviewing the evidence above.
