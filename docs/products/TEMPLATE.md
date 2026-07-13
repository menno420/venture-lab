# Product path template — idea → publish-READY

> **Status:** `reference`
>
> The repeatable path a digital product travels from idea to a queued owner
> publish click, distilled from the two worked instances: the Stripe Webhook
> Test Kit ($29, `docs/launch/stripe-webhook-test-kit/`) and the
> Membership-Site Boilerplate Kit ($49, `candidates/membership-kit/` +
> `docs/launch/membership-kit/` + `docs/publishing/vetting/membership-kit.md`).
> Copy this checklist per new product so product N+1 gets cheaper (ORDER 008
> quality floor: built + priced + listing drafted + checkout/format verified +
> sha recorded + click queued). No agent ever publishes, spends, or creates
> accounts — the path ENDS at a queued ⚑ owner click.

## The stages

| # | Stage | Output lives at | Evidence required (executed, not asserted) |
|---|-------|-----------------|--------------------------------------------|
| 1 | **Idea** | `candidates/<product>/` README stub or `docs/ideas/` | One-paragraph thesis: who pays, for what pain, why an agent can build it in sessions. Conservative revenue line (Q-0259.4: expect 0–low sales absent distribution — write that down). |
| 2 | **Build** | `candidates/<product>/` (code, README, QUICKSTART) | Runs with zero accounts (mock/demo mode with a LOUD banner — a buyer without keys must never see silent success); stdlib-only or a pinned, minimal dependency list; `.env.example` with placeholders, never values. |
| 3 | **Tests** | `candidates/<product>/…/test_*.py` (shipped IN the bundle) | Real-path tests, not only synthetic: exercise the money-touching route at the HTTP layer against **vendored, source-verified fixtures** (+ `PROVENANCE.md`), signature/auth verification, and fail-closed misconfiguration cases. Verbatim `Ran N tests … OK` captured in the session card / PR. The "13 green tests trap": green synthetic tests cannot catch a wrong belief about what the real service sends. **Zero-runtime products** (pure content: markdown packs, templates, manuscripts) record an explicit honest null instead — see "Honest-null clause" below. **Products whose subject matter IS the repo's own live infrastructure** may use the third evidence class, **verified-by-production** — see "Verified-by-production clause" below. |
| 4 | **Price** | The listing copy + owner click-script | One number with a cited precedent or comparable ($29 SWTK, $49 membership-kit); one-time unless there's a reason; recorded identically everywhere it appears. |
| 5 | **Listing copy** | `docs/launch/<product>/` (`listing-copy.md` or `LISTING.md`, one-pager) | Storefront-field-shaped blocks (Title / Short ≤200 chars / Long / Bullets / FAQ) copyable as-is; claims match what the tests actually prove — including an explicit "what it does NOT do / not live-tested" honesty section; refund/license/support lines present (placeholder ok, marked owner-to-set). **PROVENANCE-FOOTER convention (guide-shaped products):** every listing/guide chapter ends with a Sources footer citing the committed `file@sha` sources it was assembled from, and the listing names "claims verified by citation — audit the footers yourself" as a listed, checkable feature. The citations must exist anyway to pass the TRUTH bar, so the footer is near-zero marginal cost and converts honesty into a visible differentiator against free content (validated by two products: The False-Green Test Trap, PRODUCT #8, and The Agent Merge-Wall Cookbook, PRODUCT #9, which both hand-rolled the same footer before it was named here). |
| 6 | **Package + sha** | `candidates/<product>/dist/<name>-vX.Y.zip` + `package.sh` | Allow-list packaging script (never a blanket copy: exclude seller copy, runtime data, build cruft, the dist itself); **byte-reproducible** (fixed mtimes, sorted entries, `zip -X`) proven by an **unconditional double rebuild pre-click**: run `package.sh` twice, `sha256sum` both outputs, and paste the matching pair verbatim before the click is queued — no product skips this, even a "trivial" one; full **sha256 recorded** in the launch doc (owner uploads exactly that artifact). **Checkout/format verification:** unzip into a clean dir, inspect (README, QUICKSTART with the mock-mode warning, no secrets/junk), and re-run the packaged tests from the extracted copy. **Buyer-side self-rebuild proof (gold standard for products that ship build tooling, from PR #110's field-manual lesson):** if the bundle ships its own build tooling or its README says "rebuild it yourself", prove that claim buyer-side — extract the zip into a clean dir, run the shipped build tooling from inside the extracted copy, and show the regenerated artifact is **byte-identical** (same sha256) to the shipped one. This catches the defect class PR #110 actually hit: tooling the in-zip README invokes but the packaging allow-list excluded. |
| 7 | **§7 click block** | `docs/publishing/vetting/<product>.md` | A packet whose `## 7. ⚑ OWNER-GATE` section matches `scripts/derive_owner_queue.py`'s grammar: H1 `# Title Vetting — <Name>`; numbered OWNER-ACTION steps (inline ⚑ + `**X** (default …)` for each open decision); `- [ ] ⚑ **Owner:** …` checkboxes for the clicks; a post-click seat step (record launch URL/price/timestamp à la the SWTK `LAUNCH-LOG.md`). Detail HOW in `docs/launch/<product>/owner-actions.md` (six-field WHAT/WHERE/HOW/WHY/UNBLOCKS/VERIFIED-WHEN grammar); the packet is the queue-parseable pointer. |
| 8 | **OWNER-QUEUE regen** | `docs/publishing/OWNER-QUEUE.md` (GENERATED) | Run `python3 scripts/derive_owner_queue.py`; confirm stdout reports the packet parsed clean (never edit the generated file by hand). **Parallel branches:** regenerate from YOUR branch's packet set only; when two open PRs both regenerate this file they WILL conflict — whoever lands second merges `origin/main` into their branch and re-runs `derive_owner_queue.py` on the merged tree (the script derives from the union packet set, so the conflict resolves mechanically; never hand-merge the generated hunks). **Post-click DONE flip:** once the owner has executed a click and it is durably recorded (launch log), flip that §7 row to the checked live disposition — `- [x] ⚑ **Owner:** … — DONE <ISO date>` — and regenerate: the row moves to the queue's read-only "Live / completed" section instead of re-queueing, so the owner queue shows the products actually earning, not just the ones awaiting clicks (never flip a row that lacks its durable record; never flip a DONE row back). **Post-click kill-clock (⏲):** once the click is DONE-flipped and the launch doc has armed its kill-rule dates, record them in the same §7 block as a packet-level line — `KILL-CHECK: ⏲ <ISO date> <label> [· ⏲ <ISO date> <label> …]` (one line per packet, product-level: one kill clock per launch, never one per DONE row; indent wrapped continuations) — and regenerate: the queue's Live/completed entry then shows `⏲ Next checkpoint: <date> — <label>` earliest-first, so the owner sees which live product needs a look today. A malformed date is skipped with a manual-review note (tolerant-parser contract), so check stdout after regen. |

## Honest-null clause (zero-runtime products)

Some products have no executable surface — template packs, checklists,
manuscripts, image packs. For these, stage 3's "run the tests" floor item is
an **honest null**, recorded explicitly, never silently skipped and never
faked with make-work tests:

- The floor tally carries an explicit row: `- [x] Honest null — zero-runtime
  product; no test suite exists or is warranted. Substitute executed instead
  (below).`
- The **artifact-side execution substitute** replaces the test run: unzip the
  packaged artifact into a clean dir, enumerate its contents against the
  listing's promised inventory (counts must match, verbatim `ls`/`find`
  output captured), and render/lint every content file in whatever way its
  format allows (e.g. a markdown syntax pass, a link check, a UTF-8 decode of
  every file). The substitute must be an executed command with captured
  output, held to the same TRUTH bar as a test run.
- The listing's honesty section states the null in buyer-facing terms (what
  was NOT machine-verified).

## Verified-by-production clause (third evidence class)

For products whose subject matter IS this repo's own live infrastructure
(workflow cookbooks, the substrate kit itself), stage 3 admits a third
evidence class alongside real-path tests and the honest null:
**verified-by-production** — the shipped artifact is a distillation of a
live in-repo implementation, cited @ sha, together with **at least one real
event ID that implementation produced** (e.g. PR merge events with
`merged_at`/`merged_by`, read via the API in-session). "This exact workflow
landed PRs #104/#128, merged_by github-actions[bot] — verify it with one API
call" is a stronger truth-claim than any in-slice lint or synthetic run, and
usually cheaper than authoring a CI harness (origin: PRODUCT #9's session
card, `.sessions/2026-07-13-night-merge-wall.md`; second validation:
PRODUCT #8's citation-footer mechanic).

Built-in honesty rule: **any shipped artifact NOT covered by a production
citation carries an explicit not-production-run label** — in the artifact
itself, the listing FAQ, and the guide's honesty ledger, never silently
omitted. Exemplar: merge-wall-cookbook Recipe 2 (`merge-on-green.yml`) has
no production run anywhere, and every surface that mentions it says
"parse-verified-only". The class never dilutes stage 3: production evidence
is a citation to executed reality (real event IDs), not an assertion, and
the per-stage evidence bar below applies unchanged.

## Freeze / gate discipline

- A publish click may carry a **freeze**: a named gate condition (e.g. ORDER
  003's "real-path tests green IN CI") recorded in the click-script. Queue
  nothing while frozen; the unfreeze is its own evidenced change (membership
  kit: PR #16 landed the gate, PR #22 verified CI actually ran the suites and
  flipped the script to UNFROZEN).
- Honest caveats survive the unfreeze: "UNFROZEN" means the owner MAY click,
  not that the untested remainder (e.g. a live purchase, ⚑A) is proven.

## Landing procedure (how a product slice reaches `main`)

`main` is PR-only; never merge, never arm auto-merge (the enabler workflow
arms green `claude/*` PRs on its own). Strict commit order on a
`claude/<slice-name>` branch cut from a hard-synced `origin/main`:

1. **Born-red session card** `.sessions/<date>-<slice>.md`
   (`> **Status:** in-progress`, `📊 Model:` family-level) — first commit,
   before any work.
2. **Claim file** `control/claims/<date>-<slice>.md` (branch · scope · date)
   — second commit; check the directory for collisions BEFORE claiming.
3. **Work commits** — each floor item with its evidence in the message.
4. `python3 bootstrap.py check --strict` — fix every flag (docs-gate: Status
   badge in first 12 lines + reachable via an index link).
5. **Ender commit** — card flipped `complete` (💡 idea, 📊 family-level model,
   previous-session review; no fill placeholders) + claim file deleted.
6. Push; open the PR READY (Before/After body, cite the driving ORDER);
   ≤2 CI polls; leave it OPEN regardless of outcome.

## Per-stage evidence bar (the TRUTH rule applied)

Every stage claim in the PR/card cites `file@sha`, a PR number, or a CI run,
with `date -u` timestamps for executed commands. "READY" is never asserted
without having executed the verification in that same session: rebuild, test
runs, unzip inspection, queue regen. If a stage cannot be executed (wall),
quote the failure verbatim and park the product honestly rather than
asserting the floor.
