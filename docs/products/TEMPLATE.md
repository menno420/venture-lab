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
| 3 | **Tests** | `candidates/<product>/…/test_*.py` (shipped IN the bundle) | Real-path tests, not only synthetic: exercise the money-touching route at the HTTP layer against **vendored, source-verified fixtures** (+ `PROVENANCE.md`), signature/auth verification, and fail-closed misconfiguration cases. Verbatim `Ran N tests … OK` captured in the session card / PR. The "13 green tests trap": green synthetic tests cannot catch a wrong belief about what the real service sends. |
| 4 | **Price** | The listing copy + owner click-script | One number with a cited precedent or comparable ($29 SWTK, $49 membership-kit); one-time unless there's a reason; recorded identically everywhere it appears. |
| 5 | **Listing copy** | `docs/launch/<product>/` (`listing-copy.md` or `LISTING.md`, one-pager) | Storefront-field-shaped blocks (Title / Short ≤200 chars / Long / Bullets / FAQ) copyable as-is; claims match what the tests actually prove — including an explicit "what it does NOT do / not live-tested" honesty section; refund/license/support lines present (placeholder ok, marked owner-to-set). |
| 6 | **Package + sha** | `candidates/<product>/dist/<name>-vX.Y.zip` + `package.sh` | Allow-list packaging script (never a blanket copy: exclude seller copy, runtime data, build cruft, the dist itself); **byte-reproducible** (fixed mtimes, sorted entries, `zip -X`) proven by double rebuild; full **sha256 recorded** in the launch doc (owner uploads exactly that artifact). **Checkout/format verification:** unzip into a clean dir, inspect (README, QUICKSTART with the mock-mode warning, no secrets/junk), and re-run the packaged tests from the extracted copy. |
| 7 | **§7 click block** | `docs/publishing/vetting/<product>.md` | A packet whose `## 7. ⚑ OWNER-GATE` section matches `scripts/derive_owner_queue.py`'s grammar: H1 `# Title Vetting — <Name>`; numbered OWNER-ACTION steps (inline ⚑ + `**X** (default …)` for each open decision); `- [ ] ⚑ **Owner:** …` checkboxes for the clicks; a post-click seat step (record launch URL/price/timestamp à la the SWTK `LAUNCH-LOG.md`). Detail HOW in `docs/launch/<product>/owner-actions.md` (six-field WHAT/WHERE/HOW/WHY/UNBLOCKS/VERIFIED-WHEN grammar); the packet is the queue-parseable pointer. |
| 8 | **OWNER-QUEUE regen** | `docs/publishing/OWNER-QUEUE.md` (GENERATED) | Run `python3 scripts/derive_owner_queue.py`; confirm stdout reports the packet parsed clean (never edit the generated file by hand). |

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
