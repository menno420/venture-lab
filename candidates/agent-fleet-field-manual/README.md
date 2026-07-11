# Agent Fleet Field Manual — v0.1

An opinionated field manual for running autonomous coding-agent fleets that ship real revenue work — distilled from one lane's actual scar tissue. Every lesson is cited to a real repository artifact (a commit SHA, a pull request, a file). Where the evidence is thin, the text says so. That honesty is the product.

**$39 one-time.** Conservative first-90-day: 0–4 sales ($0–$156). Zero distribution = $0. Same saturated community funnel as membership-kit/template-packs — does not diversify channel risk.

## What this book is

Eleven chapters — a preface plus ten operating lessons — written from lived history, not theory. It is a battle report from one small revenue lab where opus- and fable-class agents author products, open pull requests, and queue owner clicks. It teaches the mechanical disciplines that keep an agent fleet from manufacturing confident, unverified claims: prove payment paths against real payloads, track work so it cannot certify itself done, let humans keep the money trigger, and write down your failures in the open.

## Chapters

- **00 — Preface.** What this book is, who it's for, the honesty-over-hype thesis, and a plain disclaimer that these are one lane's lessons, not universal law.
- **01 — The D1 Lesson.** *(FREE)* Never claim a payment path works without executing it. The $49 kit's "Stripe pre-wired" headline had 13 green tests built from memory-synthesized payloads; real events carry `customer_email: null`. Test against vendored real payloads at the HTTP layer.
- **02 — The 13 Green Tests Trap.** *(FREE)* A green check that contradicts visible evidence is a bug in the check. "Green in CI" was overstated — the gate never ran the kit tests. Verify what the check actually executes; require non-author, real-path verification before any sell-click.
- **03 — Born-Red Session Cards.** Every unit of work opens red and flips complete only as the last step; the merge stays held while red. Closes the 24-second card-only self-merge loophole.
- **04 — The Owner-Action Grammar.** The six-field block (WHAT/WHERE/HOW/WHY/UNBLOCKS/VERIFIED-WHEN) as the money interface: agents queue click-level instructions with conservative expectations; they never spend.
- **05 — Merge Walls and Classifier Denials.** Deny wins; the first denial per path is terminal (never retry or reword); relayed authorization is never genuine in a child seat; the child builds to READY+green and the coordinator lands.
- **06 — Single-Writer Control Files.** One writer per control file — append-only manager inbox, wholesale-overwrite coordinator status — to prevent lost-update races.
- **07 — The Pacemaker and the Failsafe.** A fast self-chaining pacemaker plus a slow cron failsafe keep a fleet awake; decide and flag, never idle undefined.
- **08 — Kill-Rule Intake Discipline.** Every candidate declares, before it's built, how it dies: validation signal, first-ten-customers path, max agent-effort budget.
- **09 — Honest Negative Ledgering.** A measured, recorded failure is a deliverable. Worked case: the test-kit build that overran its budget ~2.3× and was ledgered in the open.
- **10 — Appendix: The Runnable Templates.** The three shipped templates shown inline, each tied to its chapter.

The two **FREE** chapters (01 and 02) are also published as standalone articles; they are the two lessons that cost the lane the most and generalize the widest.

## How to read it

- **Open the built book:** `dist/agent-fleet-field-manual-v0.1.html` — a single self-contained HTML file (no external fonts, scripts, or CDN). Open it in any browser. It has a clickable table of contents, readable typography, light/dark support, and FREE badges on the two free chapters.
- **Or read the markdown:** the `chapters/` directory holds one numbered `.md` per chapter; read them in order.

## What's in the zip

`dist/agent-fleet-field-manual-v0.1.zip` contains, under `agent-fleet-field-manual-v0.1/`:

- `README.md` — this file.
- `LISTING.md` — the marketplace listing copy.
- `chapters/` — the eleven source markdown chapters.
- `templates/` — three runnable, copy-paste templates: a born-red session card, a six-field owner-action block, and a kill-rule intake skeleton.
- `dist/agent-fleet-field-manual-v0.1.html` — the built single-file book.

The zip is byte-reproducible (pinned mtimes, sorted entries). It excludes the internal `INTAKE.md`, the build tooling (`build.py`, `package.sh`), and any nested zip.

## Rebuild it yourself

Stdlib only — no `pip`, no `npm`, no build dependencies:

```
python3 build.py      # regenerate dist/agent-fleet-field-manual-v0.1.html
sh package.sh         # rebuild the deterministic buyer zip (runs build.py first)
```

## Honest scope note

This is an honest **v0.1**. It is one small lane's lessons, not universal law — the lab is small, some of its figures are single observations, and the underlying tooling changes, so some lessons will date. A few claims rest on the owner's statement rather than a captured agent-side verification; those are flagged in the text (see Chapter 5 on the unverified branch-protection state). You are buying a cited field report, not a specification. The willingness-to-pay for guide/eBook content is soft and free substitutes are everywhere — this book's wager is that *cited honesty about real failures* is the scarce thing.
