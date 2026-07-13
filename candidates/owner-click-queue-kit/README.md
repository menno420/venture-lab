# Owner-Click Queue Kit v0.1

Let your agents run all night without letting them spend, publish, or
create accounts — and stop losing the actions only YOU can take in chat
scrollback.

The kit is the "agent proposes, human clicks" control surface, packaged:
a parseable **OWNER-GATE** grammar your agents write into ordinary
markdown files, and a stdlib Python tool (`ocq.py`) that compiles every
gated action across your repo into ONE prioritized owner queue — open
decisions first, each with a **bolded default** so "agree" is a one-word
reply, then the mechanical click-runs, then a read-only record of what
already went live. Plus a strict `lint` mode you can gate pull requests
on, so the grammar stays parseable as your fleet grows.

This is not a thought experiment: the pattern is distilled from a repo
where multiple concurrent agent sessions run it in production — every
publish, price, and account action their owner has ever taken was queued
this way first. `GOTCHAS.md` is the list of ways it actually broke.

## Quickstart

1. Copy `ocq.py` into your repo and create a `gates/` directory (or
   point `--gates` anywhere).

2. Have your agents (or you) write gate files — see `GRAMMAR.md`, or
   start from the worked examples:

   ```
   examples/agent-fleet/   three gate files from a simulated fleet
                           (a decision + click-run, a hard-gated run,
                           a live product with a kill clock)
   examples/solo-repo/     one RELEASE-GATE.md embedded in a normal repo
   ```

3. Derive the queue:

   ```
   python3 ocq.py derive --gates gates --output OWNER-QUEUE.md
   ```

   Re-run after any gate change; the output is deterministic, so the
   diff is exactly what changed in the gates.

4. Try it on the shipped examples right now:

   ```
   cd examples/agent-fleet
   python3 ../../ocq.py derive --gates gates --output /tmp/queue.md
   diff /tmp/queue.md EXPECTED-OWNER-QUEUE.md && echo "byte-identical"
   ```

5. Gate your PRs on the grammar (strict mode, exit 1 on any malformed
   gate):

   ```
   python3 ocq.py lint --gates gates
   ```

6. When the owner executes a click, record it durably, then flip the
   row to `- [x] ⚑ **Owner:** … — DONE 2026-07-12` and re-derive: the
   action moves to the queue's read-only "Live / completed" section.
   Arm follow-up checkpoints with a `KILL-CHECK: ⏲ <date> <label>`
   line — the queue shows the earliest as "Next checkpoint".

## What's in the queue it generates

1. **Decisions** — every `⚑`-marked open choice, as
   WHAT / WHERE / DEFAULT / UNBLOCKS, defaults bolded.
2. **Click-run** — the mechanical `- [ ] ⚑ **Owner:** …` checklists,
   unblocked sequences first, `blocking`-marked ones labeled
   HARD-GATED and sorted last.
3. **Manual review** — gate files the tolerant parser could not read
   reliably (it never edits or normalizes them).
4. **Live / completed** — DONE-flipped rows plus ⏲ kill-clock
   checkpoints, read-only.

## Run the kit's own tests

```
python3 -m unittest test_ocq -v
```

(The suite is plain `unittest`, so `pytest test_ocq.py` collects and
runs it too — no dependency either way.) 38 tests cover the parser, the
derive output (including byte-identical determinism and the committed
example outputs), the strict lint contract, and hostile inputs:
binary junk, half-flipped DONE rows, malformed dates, defaultless
decisions, injection-shaped gate text.

## What it does NOT do

Be clear about what you're buying:

- It does **not** execute anything. No clicking, no spending, no
  posting, no notifications, no scheduling. The output is a markdown
  file for a human. That is the entire point.
- It does **not** integrate with GitHub/Slack/email out of the box —
  it reads markdown and writes markdown. Wire the derive command into
  whatever hook or CI step you already have.
- It does **not** stop a misbehaving agent from acting outside the
  queue. It is a convention plus a compiler for it; enforcement is
  social + `lint` in CI, not a sandbox. If your agent has credentials
  to spend money, this kit does not take them away.
- It is **not** a general markdown TODO parser — it parses exactly the
  OWNER-GATE grammar in `GRAMMAR.md`, deliberately, so the queue never
  guesses.
- The six-field WHAT/WHERE/HOW/WHY/UNBLOCKS/VERIFIED-WHEN detail layer
  (GRAMMAR.md §7) is a documented convention, not parsed structure —
  the queue links the human to it.
- The production system it distills runs on one specific repo's
  conventions; this kit is the generalized version, and your naming
  (gates directory, file layout) will differ. That's supported —
  `--gates` takes any files or directories.

## Requirements

- Python 3.9+ (stdlib only — no `pip install`).
- No account, no network, no build step. `ocq.py` reads your gate
  files and writes only the `--output` file.

## Files

| File | What |
|---|---|
| `ocq.py` | derive (tolerant) + lint (strict), one stdlib file |
| `GRAMMAR.md` | the complete gate grammar + the six-field detail convention |
| `GOTCHAS.md` | how this pattern actually breaks in production, and the rules that fix it |
| `examples/agent-fleet/` | 3 gate files + committed expected queue |
| `examples/solo-repo/` | 1 embedded gate file + committed expected queue |
| `test_ocq.py` | 38-test suite (unittest; pytest-compatible) |
