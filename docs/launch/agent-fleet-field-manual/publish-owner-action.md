**STATUS: NOT-QUEUED**

> **Status:** `owner-guidance`

This publish click is **not yet queued.** It is written so the shape is ready,
but the coordinator queues it to the owner only after reviewing the build
evidence below. No agent publishes, spends, or creates accounts.

## Evidence (what is built + what CI proved)

1. **The book is built.** Eleven chapters (`candidates/agent-fleet-field-manual/chapters/00-preface.md` … `10-appendix-templates.md`), each lesson cited to a real repository artifact (SHA / PR / file); the two free chapters (01, 02) are also exported as standalone articles in this directory.
2. **The HTML build is verified.** `python3 build.py` produces the single self-contained `dist/agent-fleet-field-manual-v0.1.html` (stdlib only, no external assets); all 11 table-of-contents links resolve to their chapter sections and the "back to contents" links resolve to `#top` — verified from inside the extracted zip.
3. **The zip is byte-reproducible.** `sh package.sh` builds `dist/agent-fleet-field-manual-v0.1.zip` deterministically (pinned mtimes, sorted entries); two consecutive builds produce an identical sha256. It contains README, LISTING, chapters, templates, and the built HTML, and excludes the internal INTAKE and the build tooling.
4. **CI leg (to be confirmed on the PR):** the substrate-gate `check --strict` must be green on the built head SHA with the session card flipped to `complete`. This is a docs/prose product — there is no runtime test suite to run; verification is the build determinism + the TOC-resolution check above, and the citation map in the PR body (each lesson → its repo artifact).

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

No secret values are involved in this action — nothing in this product reads or
stores a secret; environment-variable *names* only appear in the book's
templates as guidance. The owner performs the click; the coordinator queues this
only after reviewing the evidence above.
