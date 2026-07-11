# Template — Born-Red Session Card

Copy the fenced block below into `.sessions/<date>-<slug>.md` as your FIRST
commit on a new branch, committed **alone**, before any product code. It is
born red: the `Status` badge starts at `in-progress`. Flip it to `complete`
only as the deliberate LAST step, once the close-out is actually written.

Four markers must be present in their exact byte-form for the card to count
complete: the `**Status:**` badge (a blockquote line, backticked
lowercase-hyphen value), the `📊 Model:` line (family-level model name — e.g.
`opus-4.8`, never a dated ID), the exact string `Previous-session review`, and
a `💡` character. Resolve every `[[fill: ...]]` slot before flipping — an
unresolved slot keeps the card counting incomplete.

(The template lives inside the code fence below on purpose: the born-red
checker strips fenced blocks before it scans, so shipping this skeleton in the
repo does not trip the gate on a half-written card.)

```markdown
# Session — [[fill: title]]

> **Status:** `in-progress`

- **📊 Model:** [[fill: family-level model, e.g. opus-4.8]] · [[fill: effort]] · [[fill: task-class]]
- **session:** [[fill: one-line statement of what this session ships]]
- **started (date -u):** [[fill: paste `date -u` output]] (born-red first commit)

## ⟲ Previous-session review

Previous-session review: [[fill: one line — what landed just before this session, per the status file; cite a PR/SHA]]

## 💡 Session idea

[[fill: 2-4 lines — why this work exists and what makes it worth doing]]

## Scope

- [[fill: bullets — the concrete artifacts this session will produce]]

## Work log

- [[fill: commits + evidence, filled as you go]]

## Status / outcome

[[fill: close-out — verification results, check --strict result, PR#, honest budget line. Flip Status to `complete` only when this is real.]]
```
