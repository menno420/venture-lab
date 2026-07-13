# Marketplace listing copy — AI Novella Production Kit v0.1

> **Status:** `reference`

**Title:** AI Novella Production Kit — finish the book your AI keeps starting

**Short description (≤200 chars, 199):** The production method behind
16 finished AI-assisted manuscripts: length bands, series-bible CANON
files, promise-manifest checks, dead-session recovery, and the gate
between written and publishable.

**Price:** $29 (one-time)

## Description

AI assistants are spectacular at starting novels. The graveyard is the
middle: 2,000 promising words, then drift, then a new project. The gap
is not prose quality — it is production structure: nothing declares
what "finished" means, nothing holds continuity across sessions,
nothing survives a crashed run, and nothing separates "a draft exists"
from "this can be listed."

This kit is that structure, distilled from a repository whose fiction
lane shipped **16 complete manuscripts** (10 adult titles, 5 YA, 1
middle-grade — every one committed, every word count an honest `wc -w`
measurement cited to a merged pull request):

- **The one-session method** — a declared length band (the production
  default: 15,000–16,000 words, 12 chapters), chapter briefs, one
  aimed repair pass, and a written decisions record; "finished" is
  checkable, not a feeling.
- **The promise manifest** — two grep-able lists extracted from your
  own blurb before drafting: promised phrases that MUST appear, and
  register fences that must hit zero. Mechanical, cheap, and it
  caught real defects in production that human rereads missed.
- **The series bible (CANON.md)** — laws quoted byte-exact, cast
  constraints, and open hooks with the coordinates where they were
  planted, updated in the same sitting each book lands — so book N+1
  starts from an O(1) lookup, not a reread.
- **Length bands and editions** — deriving novella cuts, serial
  editions, translations, and large-print specs from ONE base
  manuscript, with the conventions that keep derived editions from
  breeding continuity errors.
- **Dead-session recovery** — the forward-only protocol from a real
  production death: a drafting run that died with zero words pushed,
  resumed to a merged 15,995-word manuscript because the state was
  recoverable by design.
- **The publish gate** — the 7-section vetting packet (title,
  collision scan, market, price band, packaging, listing copy, click
  checklist) that 31 committed packets ran, separating *written* from
  *publishable*.
- **Kill rules for fiction** — validation signals, T+7/T+30 kill
  clocks, and the negative ledger, so you stop writing book five for
  an audience that never bought book one.

Seven chapters carry the method and the WHY behind each rule, each
ending in a Sources footer citing the committed production files it
was distilled from — claims verified by citation, audit them yourself.
Five blank-slate templates (CANON bible, chapter plan, vetting packet,
recovery checklist, edition matrix) install the method in ~20 minutes.

## What's inside

- `QUICKSTART.md` — the ~20-minute setup: copy 5 templates, declare a
  band, write the promise manifest, draft.
- `guide/` — 7 chapters: the one-session method · the series bible ·
  length bands + editions · the publish gate · dead-session recovery ·
  pricing + listing · kill rules for fiction.
- `templates/` — 5 starters: `CANON-template.md`, `chapter-plan.md`,
  `vetting-packet.md`, `recovery-checklist.md`,
  `edition-variant-matrix.md` (+ a copy-map README).
- `README.md` + `INCLUDED.md` — orientation + full inventory (16
  content files).

## Requirements

- Any AI writing assistant that can hold a chapter brief — the method
  is tool-agnostic — plus a plain-text editor and any word counter
  (`wc -w` or equivalent). Git recommended (the recovery chapter
  assumes some form of versioned sync) but only required by chapter 5.

## What it does NOT do (so you know what you're buying)

- **It contains no fiction.** The 16 manuscripts are separate
  products; nothing of their text ships here beyond one-or-two-line
  cited examples of artifact *shape*. You are buying method +
  templates, not books.
- **It is not a novel generator and ships no software.** Nothing
  executes; there are no prompts that "do it for you." The method was
  run in production by coordinated coding-agent sessions with a CI
  gate — a solo writer with one chat window gets the full structure
  but not the automated enforcement, and chapter 1 says so plainly.
- The production evidence is the seller's own repository (cited
  file@sha in every chapter footer, word counts cited to merged PRs);
  no external writing team has run these exact templates.
- The catalog behind the pricing chapter has zero verified book sales
  — its pricing discipline is verified-by-citation (real comps, real
  tier arithmetic), not verified-by-revenue, and the chapter says so.
- Nothing here was machine-verified beyond format checks
  (UTF-8/markdown/inventory) — it is a document kit; there is no test
  suite because there is nothing to test.

## FAQ

**Can't I get writing advice like this free?**
Yes — endless amounts, and this listing says so. What you're paying
for is different in kind: a *production system* that demonstrably
finished 16 manuscripts, with the receipts cited (file@sha, merged-PR
word counts) rather than asserted, plus the templates that install it
in minutes instead of an afternoon of transcription.

**Does this work with ChatGPT / Claude / my tool?**
If your assistant can follow a chapter brief and you can save files,
yes. Nothing in the kit calls any API or assumes any vendor.

**Will this make my book sell?**
No — and chapter 7 exists precisely for that honesty. The kit gets
you from "starts" to "a publishable, gated, priced manuscript" and
then puts a kill clock on the launch so the market's answer gets
recorded instead of rationalized.

**Is this the seller's agent-fleet material rebranded?**
No. The seller's agent-ops products (template packs, field manual,
control-plane pack) serve developers running coding-agent fleets;
this kit is the fiction lane's method for writers. Where a convention
originated fleet-side (the recovery protocol), the chapter says so
and translates it.

**Refunds / support / license:** [owner-to-set — storefront defaults;
suggested: 14-day no-questions refund, single-writer license, email
support best-effort.]
