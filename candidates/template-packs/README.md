# Agent-Workflow Template Pack — v0.1

A small, drop-in set of files that gives a repo the **session discipline** a
coding agent needs to work autonomously without going off the rails: an agent
constitution, advisory Claude Code hooks, a session-log card, and a one-page
discipline playbook.

> This is **v0.1** — a genuine, usable slice, honest about its scope. Every
> file is a *starter* you customize with `<FILL: ...>` placeholders; nothing
> here assumes a particular stack or CI. It is a workflow scaffold, not a
> framework you install.

## Who it's for

Solo devs and small teams running AI coding agents (Claude Code and similar)
who want their agent to orient itself, hold a quality floor, and leave a
recoverable trail — instead of starting cold every session and trailing off
without closing out.

## What's inside

```
pack/
├── CLAUDE.md.template        ← starter agent constitution (rails, done-when, quality floor)
├── session-card.template.md  ← session-log card carrying the discipline markers
├── session-discipline.md     ← 1-page playbook (heartbeat, claim, close ritual, timestamps, forward-only git)
└── hooks/
    ├── settings.template.json ← Claude Code hooks block (SessionStart / Stop / PostToolUse)
    ├── README.md              ← install contract (stage under .claude/, never auto-write)
    └── scripts/
        ├── agent-orient.sh       ← SessionStart orientation reminder
        ├── session-close-check.sh← Stop close-ritual nudge
        └── post-edit-reminder.sh ← PostToolUse quality-floor reminder
```

See [`INCLUDED.md`](INCLUDED.md) for a per-file manifest and
[`LISTING.md`](LISTING.md) for the marketplace copy.

## Quickstart

1. Copy `pack/CLAUDE.md.template` to your repo root as `CLAUDE.md` and resolve
   every `<FILL: ...>` — your stack, your one quality-floor command, your PR
   convention. Keep it short.
2. Copy `pack/session-discipline.md` next to it, and read it once.
3. Install the hooks: copy `pack/hooks/scripts/` into your repo, `chmod +x`
   them, fill the paths in `settings.template.json`, and merge its `hooks`
   block into `.claude/settings.json`. Full steps in `pack/hooks/README.md`.
4. Copy `pack/session-card.template.md` into your session-log directory and use
   it to open each session (born red) and close it (flipped to `complete`).

That's the whole install: no dependencies, no build step, no runtime. You are
adding four short text files and three tiny shell scripts.

## Honest scope

- These are **conventions and reminders**, not enforcement. The hooks are
  advisory (they print and exit `0`); they nudge, they don't block. That's a
  deliberate choice — a blocking hook that misfires wedges your session.
- Nothing here is stack-specific. The value is the *shape* of the discipline,
  proven in practice, that you fill in with your repo's specifics.
- It pairs with the membership-kit (a productized product starter); this pack
  is the *workflow* layer, that one is a *product* layer.
