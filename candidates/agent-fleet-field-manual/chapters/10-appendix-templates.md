# Chapter 10 — Appendix: The Runnable Templates

The disciplines in this book are only as good as the friction of applying them. To lower that friction, the book ships three copy-paste templates in the `templates/` directory of the zip. This appendix shows each one inline and says which chapter it operationalizes. The files in the zip are the authoritative versions; the skeletons below are reproduced so you can read them without unzipping.

## 1. Born-red session card

Operationalizes **Chapter 3**. Copy this into `.sessions/<date>-<slug>.md` as the FIRST commit on a new branch, alone, before any product code. It is born red — `Status` starts at `in-progress` — and flips to `complete` only as the deliberate last step. Four markers must be present in exact byte-form; resolve every `[[fill: ...]]` slot before flipping.

```
# Session — <title>

> **Status:** `in-progress`

- **📊 Model:** <family-level model, e.g. opus-4.8> · <effort> · <task-class>
- **session:** <one line: what this session ships>
- **started (date -u):** <paste `date -u`> (born-red first commit)

## ⟲ Previous-session review

Previous-session review: <one line — what landed just before this; cite a PR/SHA>

## 💡 Session idea

<2-4 lines: why this work exists>

## Scope

- <bullets: the concrete artifacts>

## Work log

- <commits + evidence, filled as you go>

## Status / outcome

<close-out: verification, check result, PR#, honest budget line. Flip Status to complete only when this is real.>
```

The full file (`templates/session-card.md`) keeps this skeleton inside a code fence deliberately: the born-red checker strips fenced blocks before scanning, so shipping the skeleton in a repo does not trip the gate on a half-written card. That is the same subtlety Chapter 3 noted about the checker stripping inline code and fences before counting `[[fill:]]` slots.

## 2. Six-field owner-action block

Operationalizes **Chapter 4**. The agent fills all six fields; a human performs the click. The block stays inert (`STATUS: NOT-QUEUED`) until the gate conditions are met and a coordinator reviews the evidence.

```
**STATUS: NOT-QUEUED**

> **Status:** `owner-guidance`

## Evidence
- <what is built>
- <what CI/verification proved — real path, non-author>

### ⚑ <short action label>
- **WHAT:** <the single decision, e.g. publish <product> at $<price>>
- **WHERE:** <exact surface, e.g. Gumroad → New product → Digital product>
- **HOW:** <click-level steps — sign in; upload <file>; paste <copy>; set price; publish; copy URL>
- **WHY:** <candidate + provenance + conservative expectation>
- **UNBLOCKS:** <what becomes possible once the owner acts>
- **VERIFIED-WHEN:** <observable success condition, e.g. public URL returns HTTP 200>

No secret values — <which secret is read from which env-var NAME>.
The owner performs the click; no agent publishes, spends, or creates accounts.
```

Two rules the skeleton enforces by shape: WHY carries a conservative number so the block never manufactures consent, and there are no secret values anywhere — only environment-variable names.

## 3. Candidate intake with kill-rule fields

Operationalizes **Chapter 8**. Every candidate gets one of these BEFORE it is built. The three kill-rule fields are binding — they define, in advance, how the candidate dies.

```
# <Candidate name> — intake (candidate #<n>)

> <one-line pitch>

## What it is
<3-5 sentences: the artifact, how delivered, in/out of scope for v0.1>

## Scoring (rubric, weighted 0–5)
| Axis | Weight | Score | Rationale |
(distribution 35% / agent-buildability 20% / owner-click cost 15% /
 speed-to-first-dollar 15% / WTP-moat 15% → weighted total, show the arithmetic)

## Kill-rule fields (binding)
- Validation signal: within <N> days of <trigger>, ≥1 of <threshold> / <threshold> / <first sale>. Else ledgered negative.
- First-ten-customers path (⚑ = owner-gated): <the actual channels>. NOTE: <does it diversify or concentrate channel risk?>
- Max agent-effort budget: <N>k tokens to v0.1. Over budget without the signal = ledgered negative.
- Conservative revenue: $<price> one-time; first-90-day <0–N sales ($0–$X)>; zero distribution = $0.

## Why this might fail
<name the softest axes honestly>

## Owner actions — NOT queued yet
<publish click earned only after v0.1 is built and verified>
```

This book's own intake (`candidates/agent-fleet-field-manual/INTAKE.md`) is a filled instance of exactly this skeleton — candidate #4, scored 3.55, with its weakest axes (distribution, willingness-to-pay) named in the open and a "Why this might fail" section that admits the saturated-funnel problem. Chapter 8 walks through it.

## Closing

That is the whole toolkit: a way to track work so it cannot certify itself done (the card), a way to request money actions without performing them (the owner-action block), and a way to decide in advance how a candidate dies (the intake). Three skeletons, three disciplines, each earned by a failure this lane actually lived and cited back to a real artifact. Copy them, adapt the numbers to your own economics, and keep the one thing that is not adjustable: the honesty about what you have and have not proven.
