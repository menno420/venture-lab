# Quickstart — Agent-Workflow Template Pack

Give a repo the session discipline a coding agent needs in about ten minutes.
No dependencies, no build step, no runtime — you're copying in a few short text
files and three tiny shell scripts.

## Install (four steps)

1. **Constitution.** Copy `pack/CLAUDE.md.template` to your repo root as
   `CLAUDE.md`. Resolve every `<FILL: ...>` — your stack, your single
   quality-floor command (the one thing that must pass before every push), your
   PR/merge convention. Keep it short.

2. **Playbook.** Copy `pack/session-discipline.md` next to it and read it once.
   It's the one page behind the templates: heartbeat-before-work,
   claim-before-build, the close ritual, `date -u` timestamps, forward-only git
   — each rule paired with the failure it prevents.

3. **Hooks (advisory, fail-open).** Copy `pack/hooks/scripts/` into your repo and
   make them executable:

   ```bash
   mkdir -p .claude/scripts
   cp pack/hooks/scripts/*.sh .claude/scripts/
   chmod +x .claude/scripts/*.sh
   ```

   Then fill the paths in `pack/hooks/settings.template.json` and merge its
   `hooks` block into `.claude/settings.json`. Full contract in
   `pack/hooks/README.md`. Every hook prints a reminder and exits `0` — a broken
   hook degrades to silence, it never wedges a session.

4. **Session card.** Copy `pack/session-card.template.md` into your session-log
   directory. Open each session with it (born red, `in-progress`) and close each
   session by flipping it to `complete`.

That's the whole install.

## What's in this bundle

- `README.md` — what the pack is, who it's for, honest scope.
- `QUICKSTART.md` — this file.
- `INCLUDED.md` — per-file manifest of everything in `pack/`.
- `pack/` — the drop-in payload (constitution, playbook, session card, hooks).

## Verify it's working

- Start a session: the `SessionStart` hook prints your reading list + heartbeat
  reminder.
- Edit a file: the `PostToolUse` hook reminds you to run the quality floor
  before pushing.
- Stop: the `Stop` hook nudges if today's session card is missing or still
  `in-progress`.

If a hook is misconfigured it stays silent — nothing blocks. Fill the `<FILL>`
slots at your own pace; the pack ships the *shape*, you supply the specifics.
