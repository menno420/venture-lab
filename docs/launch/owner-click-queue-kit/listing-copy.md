# Marketplace listing copy — Owner-Click Queue Kit v0.1

> **Status:** `reference`

**Title:** Owner-Click Queue Kit — let your agents run all night without letting them spend

**Short description (≤200 chars, 189):** The "agent proposes, human
clicks" control surface: a parseable OWNER-GATE grammar + a stdlib
derive tool that compiles every gated action into one owner queue.
Agents never spend or click.

**Price:** $19 (one-time)

## Description

If you run autonomous coding agents, you already have the rule: the
agent must NEVER spend money, publish, create accounts, or touch
production credentials. What you probably don't have is the other half —
so the actions only YOU can take pile up in chat scrollback, get asked
twice, or quietly never happen.

The Owner-Click Queue Kit packages the missing half, distilled from a
repo where multiple concurrent agent sessions run it in production:
agents write owner-only actions as parseable **OWNER-GATE** blocks in
ordinary markdown files, and one stdlib Python command compiles every
gate across your repo into a single prioritized owner queue:

- **Decisions first, each with a bolded default** — so clearing your
  queue starts with reading one file and replying "agree".
- **Click-runs second** — the mechanical checklists, unblocked
  sequences first, `blocking`-marked ones labeled HARD-GATED and
  sorted last.
- **A read-only "Live / completed" record** — DONE-flipped clicks plus
  a ⏲ kill-clock line per launch ("T+7: any traffic? T+30: kill rule"),
  earliest checkpoint surfaced.
- **A manual-review section** — anything the tolerant parser couldn't
  read reliably is listed, never edited, never silently dropped.

Two commands, two contracts: `derive` is tolerant and advisory (exits 0
on every path — safe in hooks and cron, a malformed gate never blocks
unrelated work), `lint` is strict (exit 1 with per-file errors — the
check you gate pull requests on, so the grammar survives your fleet).
The output is deterministic: no timestamps, sorted traversal,
byte-identical re-runs — regen diffs show exactly what changed.

The grammar has the fail-safes you'd otherwise learn the hard way: the
DONE flip needs BOTH marks (`[x]` AND `— DONE <date>`), so a stray
checkbox edit can only ever re-queue an owner action, never silently
drop one. Every decision must carry a machine-findable default or lint
fails. And the whole thing enforces the one rule that matters: **the
queue is a proposal surface, never an authorization surface** — agents
write entries, only the human executes.

## What's inside

- `ocq.py` — derive + lint in one stdlib Python file (3.9+, no
  `pip install`, no network; reads your gates, writes one output file).
- `GRAMMAR.md` — the complete gate grammar: decisions with defaults,
  ⚑ Owner click rows, the DONE flip, KILL-CHECK kill clocks, plus the
  six-field WHAT/WHERE/HOW/WHY/UNBLOCKS/VERIFIED-WHEN convention for
  writing actions a tired human can execute at midnight.
- `GOTCHAS.md` — 10 ways this pattern actually broke in production and
  the rules that fix them (generated-file merge races between parallel
  agents, advisory-vs-strict contract swaps, half-flipped DONE rows…).
- Two worked examples with committed expected outputs: `agent-fleet/`
  (three gate files: a decision + click-run, a HARD-GATED run with a
  real-spend block, a live launch with an armed kill clock) and
  `solo-repo/` (one gate section embedded in an ordinary doc).
- `test_ocq.py` — a 38-test suite (plain unittest; pytest collects it
  too) covering the parser, derive determinism (byte-identical against
  the committed example outputs), the strict lint contract, and
  hostile inputs: binary junk, malformed dates, defaultless decisions,
  injection-shaped gate text.

## Requirements

- Python 3.9+, standard library only.
- No account, no dependencies, no network, no build step.

## What it does NOT do (so you know what you're buying)

- It does not execute anything — no clicking, spending, posting,
  notifications, or scheduling. The output is a markdown file for a
  human. That is the point.
- It does not integrate with GitHub/Slack/email out of the box; it
  reads and writes markdown. Wire it into your own hooks/CI.
- It does not sandbox a misbehaving agent. It is a convention plus a
  compiler for it; if your agent holds credentials that can spend
  money, this kit does not take them away — lint in CI plus your
  agent instructions are the enforcement.
- It is not a general markdown TODO parser — it parses exactly the
  documented OWNER-GATE grammar, deliberately.
- The production evidence is the seller's own repo (the pattern this
  kit generalizes has carried every publish/price/account action
  across 150+ pull requests there); your fleet's conventions will
  differ, and the `--gates` flag is how you adapt.

## FAQ

**Can't I just tell my agent to ask before spending?**
That's the input, not the system. Asks in chat scroll away, repeat
across sessions, and die with the conversation. Gate files are
committed, reviewable, and compile to ONE queue that cannot drift from
them — plus a lint gate that keeps ten agents writing the same grammar.

**Why markdown and not a web dashboard?**
Because your agents already write markdown into your repo, your review
tooling already diffs it, and a derived file cannot go down, leak, or
need an account. The queue lives where the work lives.

**Refunds / support / license:** [owner-to-set — storefront defaults;
suggested: 14-day no-questions refund, single-developer license, email
support best-effort.]
