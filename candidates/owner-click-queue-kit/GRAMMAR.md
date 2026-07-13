# The OWNER-GATE grammar — how agents queue actions only a human may take

This is the complete grammar `ocq.py` parses. It has two layers:

1. **The gate block** (this page, §1–§6) — the compact, machine-parseable
   form agents write into any markdown file. This is what `derive`
   compiles into the single owner queue and what `lint` validates.
2. **The six-field action detail** (§7) — the prose HOW that lives next
   to the gate block for anything non-obvious. Convention, not parsed:
   the queue links to it, the human reads it.

Design goal: the owner should be able to clear their whole queue by
reading ONE generated file top to bottom, replying "agree" to the
defaults, and clicking down the checklists. Agents propose; only the
human executes. **The queue is a proposal surface, never an
authorization surface** — no agent may treat a queued entry as
permission to act.

## 1. The gate file

Any markdown file that contains an OWNER-GATE section is a gate file.
Two rules:

- **Title:** the file's first H1 (`# Blog Relaunch`) names the
  click-run in the queue. Required (`lint` fails without it).
- **Gate section:** an h2 whose text contains `OWNER-GATE`, e.g.

  ```markdown
  ## ⚑ OWNER-GATE — actions queued for the owner
  ```

  Numbered forms (`## 7. ⚑ OWNER-GATE — publish clicks`) parse the
  same — the parser matches any `## … OWNER-GATE …` heading. The
  section runs to the next `## ` heading or end of file. One gate
  section per file (the first one wins).

Where gate files live is yours to choose: one `gates/` directory (the
kit's default), or gate sections embedded in existing per-task docs —
`derive --gates <dir-or-file>` accepts either, repeatably.

## 2. Decisions — `⚑` inside a numbered step

A numbered step inside the gate section that carries the `⚑` marker is
an **open owner decision**:

```markdown
1. **Storefront account:** sign into the storefront (no choice here —
   this step has no ⚑ because it is mechanical).
2. **⚑ Storefront pick:** **Gumroad** (default — payout already
   configured) or Lemon Squeezy — owner's call.
```

Rules:

- The step's **bold lead** (`⚑ Storefront pick`) becomes the decision's
  label.
- The recommended default MUST be machine-findable, in priority order:
  1. a `**bold**` span immediately followed by `(default` or
     `(recommended default` — the canonical form;
  2. a `**bold**` span whose own text contains "recommend";
  3. a parenthetical containing "recommend".
- A `⚑` step with no findable default still derives (with a
  *no default parsed* placeholder + a manual-review note) but **fails
  lint** — a defaultless decision costs the owner a full read instead
  of a one-word "agree", which defeats the queue.
- Steps WITHOUT `⚑` are context for the human; they are not queued.

## 3. Clicks — `- [ ] ⚑ **Owner:** …` checkboxes

Each mechanical owner action is one unchecked checkbox:

```markdown
- [ ] ⚑ **Owner:** upload `dist/kit-v0.1.zip` + sha256 spot-check.
- [ ] ⚑ **Owner:** price set (**$19 one-time** (default)).
- [ ] ⚑ **Owner:** the publish click + public URL copied.
```

Rules:

- The row must start with `⚑` and contain `**Owner:**` — anything else
  in the checklist (e.g. a `- [ ] Agent (post-click): …` follow-up
  step) is ignored by the parser and stays yours.
- A row may carry its own `**X** (default)` span; the queue renders it
  as that click's DEFAULT.
- A click whose text shares distinctive words with a decision's label
  is rendered as *executes its D-item above* — write the decision lead
  and its executing click with the same key noun ("storefront pick" /
  "storefront pick (**Gumroad** (default))") to link them.
- The word **`blocking`** in any pending click marks the whole file's
  click-run **HARD-GATED**: it sorts last in the queue and every
  decision in the file is labeled "nothing below it proceeds".
- Wrapped rows are fine — indent continuation lines and the parser
  folds them into one item:

  ```markdown
  - [ ] ⚑ **Owner:** rotate the deploy key in the hosting dashboard,
        then paste the new fingerprint into `docs/keys.md`.
  ```

## 4. The DONE flip — recording an executed click

Once the owner has executed a click AND the result is durably recorded
(launch log, URL, timestamp), flip the row — **both marks together**:

```markdown
- [x] ⚑ **Owner:** the publish click + public URL copied — DONE 2026-07-12
```

- `[x]` alone still queues. `— DONE <date>` on an unchecked box still
  queues. This is deliberate fail-safe asymmetry: a half-flip can only
  ever re-queue an owner action, never silently drop one. `lint` flags
  half-flips so they get fixed.
- The date is ISO `YYYY-MM-DD` and must be a real calendar date.
- DONE rows render in the queue's read-only **Live / completed**
  section and never count toward pending totals.
- Never flip a row without its durable record; never flip a DONE row
  back.

## 5. The kill clock — `KILL-CHECK:` (⏲)

A live launch needs scheduled follow-ups (did it get traffic? does the
kill rule fire?). Arm them as ONE line in the gate section — gate-level,
not per-click, because a kill clock is a fact about the launch, not
about any single click:

```markdown
KILL-CHECK: ⏲ 2026-07-19 T+7 funnel checkpoint · ⏲ 2026-08-11 T+30
      kill-rule deadline (≥1 sale or ≥50 reads, else delist)
```

- Each token is `⏲ <ISO date> <label>`; separate tokens with `·`;
  indent wrapped continuations.
- Checkpoints render earliest-first under the Live section as
  `⏲ Next checkpoint: <date> — <label>`.
- A malformed date token is skipped with a manual-review note (derive)
  and fails lint; valid sibling tokens still render.

## 6. Two contracts, one grammar

| | `derive` | `lint` |
|---|---|---|
| Contract | tolerant + advisory — **exits 0 on every path** | strict — exit 1 on any problem |
| Malformed gate | listed under "Manual review", never edited | named per-file error |
| Zero gate files | "skipped" note, exit 0 | FAIL, exit 1 |
| Use it in | hooks, cron, post-merge regen — must never block unrelated work | the PR check on gate-file changes |

The generated queue is deterministic: output depends only on input
content (sorted traversal, no timestamps), so re-running on the same
tree is byte-identical and regen diffs stay reviewable. Never hand-edit
the generated file.

## 7. The six-field action detail (convention layer, not parsed)

For any queued action whose HOW is non-obvious, write a companion block
near the gate (or in a linked doc) with exactly these six fields:

```markdown
### ⚑ — Publish "Owner-Click Queue Kit" at $19 (one-time)
- **WHAT:** the single action, one sentence, artifact paths inline.
- **WHERE:** the exact surface — URL, menu path, account.
- **HOW:** numbered micro-steps a tired human can follow verbatim.
- **WHY:** the justification + what evidence backs it (cited).
- **UNBLOCKS:** what becomes possible once this is done.
- **VERIFIED-WHEN:** the observable condition that proves it worked —
  never "when it's done"; a URL that loads, a hash that matches.
```

The gate block's checkbox is the queue-parseable pointer; the six-field
block is what the human reads before clicking. Keeping them separate is
what lets the queue stay one screen long.
