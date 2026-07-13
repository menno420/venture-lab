#!/usr/bin/env python3
"""ocq.py — Owner-Click Queue: derive one owner queue from gate files.

The control surface for agent fleets that must NEVER spend, publish, or
create accounts: agents queue owner-only actions as parseable OWNER-GATE
blocks in ordinary markdown files ("gate files"); this tool compiles
every gate across the repo into ONE prioritized owner queue with bolded
defaults (so "agree" is a one-word reply). Agents propose; only the
human clicks. The queue is a proposal surface, never an authorization
surface.

Two commands, two contracts:

  ocq.py derive [--gates PATH ...] [--output FILE]
      Regenerate the queue. TOLERANT + ADVISORY: exits 0 on EVERY path.
      A gate file that cannot be parsed reliably is never edited or
      normalized — it is listed in the generated file's "Manual review"
      section and on stdout, and the run still succeeds. Safe to run
      from hooks/CI without ever blocking unrelated work.

  ocq.py lint [--gates PATH ...]
      STRICT validation of the same grammar: exit 1 with per-file
      errors on any malformed gate (missing title, defaultless
      decision, half-flipped DONE row, bad date, ...). This is the mode
      you gate a pull request on.

Determinism: derive output depends only on input file content (sorted
traversal, no timestamps), so re-runs on the same tree are
byte-identical — regen diffs stay reviewable.

Grammar: see GRAMMAR.md in this kit. Stdlib only. No network. Reads
gate files, writes only --output, never edits an input.
"""

from __future__ import annotations

import argparse
import datetime
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

DEFAULT_GATES = "gates"
DEFAULT_OUTPUT = "OWNER-QUEUE.md"

FLAG = "\N{BLACK FLAG}"  # ⚑ — the owner-gate marker
TIMER = "\N{TIMER CLOCK}"  # ⏲ — the kill-clock checkpoint marker

# The gate section: any h2 whose text contains OWNER-GATE ("## ⚑
# OWNER-GATE", "## 7. ⚑ OWNER-GATE — publish clicks", ...). The section
# runs to the next h2 or end of file.
GATE_HEADING_RE = re.compile(r"^##\s.*OWNER-GATE", re.IGNORECASE)
H2_RE = re.compile(r"^##\s")
H1_RE = re.compile(r"^#\s+(.+?)\s*$")
STEP_RE = re.compile(r"^(\d+)\.\s+(.*)$")
CHECKBOX_RE = re.compile(r"^- \[[ xX]\]\s+(.*)$")
CHECKED_RE = re.compile(r"^- \[[xX]\]\s+(.*)$")
UNCHECKED_RE = re.compile(r"^- \[ \]\s+(.*)$")
# DONE disposition: "— DONE <ISO date>" (em/en dash or hyphen). BOTH
# marks are required — a checked box without DONE still queues, and an
# unchecked box carrying DONE text still queues. See GOTCHAS.md #4.
DONE_RE = re.compile(r"[—–-]\s*DONE\s+(\d{4}-\d{2}-\d{2})")
KILLCHECK_RE = re.compile(r"^KILL-CHECK:\s*(.*)$")
CHECKPOINT_DATE_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})\b\s*(.*)$")
BOLD_RE = re.compile(r"\*\*(.+?)\*\*")


@dataclass
class Decision:
    label: str  # "<file title> — <decision lead>"
    what: str
    where: str
    default: str  # already-bolded markdown, or a manual-review placeholder
    unblocks: str
    source: str  # display path of the gate file


@dataclass
class ClickGroup:
    title: str
    where: str
    blocked: bool
    clicks: list[dict] = field(default_factory=list)  # {"what", "default", "linked"}
    done: list[dict] = field(default_factory=list)  # {"what", "date"}
    checkpoints: list[dict] = field(default_factory=list)  # {"date", "label"}


@dataclass
class ParseResult:
    decisions: list[Decision] = field(default_factory=list)
    groups: list[ClickGroup] = field(default_factory=list)
    live: list[ClickGroup] = field(default_factory=list)
    manual: list[tuple[str, str]] = field(default_factory=list)  # (file, why)
    errors: list[tuple[str, str]] = field(default_factory=list)  # lint-grade (file, why)
    parsed_files: list[str] = field(default_factory=list)


def strip_markup(text: str) -> str:
    """Markdown bold/italic/backticks removed; whitespace collapsed."""
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text, flags=re.DOTALL)
    text = re.sub(r"\*(.+?)\*", r"\1", text, flags=re.DOTALL)
    text = text.replace("`", "")
    return re.sub(r"\s+", " ", text).strip()


def gate_section(lines: list[str]) -> list[str] | None:
    """The OWNER-GATE section's lines (heading excluded), or None."""
    start = None
    for i, line in enumerate(lines):
        if GATE_HEADING_RE.match(line):
            start = i + 1
            break
    if start is None:
        return None
    body: list[str] = []
    for line in lines[start:]:
        if H2_RE.match(line):
            break
        body.append(line)
    return body


def collect_items(body: list[str], head_re: re.Pattern) -> list[str]:
    """Match head_re at line starts; fold indented continuations in."""
    items: list[str] = []
    current: list[str] | None = None
    for line in body:
        match = head_re.match(line)
        if match:
            if current is not None:
                items.append(" ".join(current))
            current = [match.group(len(match.groups()))]
            continue
        if current is not None and line.startswith(" ") and line.strip():
            current.append(line.strip())
            continue
        if current is not None:
            items.append(" ".join(current))
            current = None
    if current is not None:
        items.append(" ".join(current))
    return items


def extract_default(text: str) -> str:
    """The recommended default as a bolded markdown span, or ''.

    Priority: (1) a **bold** span immediately followed by "(default" /
    "(recommended default" — the grammar's marker for the default pick;
    (2) a **bold** span that itself says "recommend"; (3) a
    parenthetical containing "recommend".
    """
    marked = re.search(
        r"\*\*([^*]+?)\*\*\s*\((?:recommended\s+)?default", text, re.IGNORECASE
    )
    if marked:
        return f"**{marked.group(1)}**"
    for match in BOLD_RE.finditer(text):
        if "recommend" in match.group(1).lower():
            return f"**{match.group(1)}**"
    paren = re.search(r"\(([^()]*recommend[^()]*)\)", text, re.IGNORECASE)
    if paren:
        return f"**{strip_markup(paren.group(1))}**"
    return ""


def decision_lead(step: str) -> str:
    """The step's bold lead, minus the flag marker and parentheticals."""
    match = BOLD_RE.match(step.strip())
    lead = match.group(1) if match else step
    lead = lead.replace(FLAG, "")
    lead = re.sub(r"\([^)]*\)", "", lead)
    return strip_markup(lead).rstrip(":").strip()


def lead_keywords(lead: str) -> set[str]:
    """Distinctive lowercase words of a decision lead (stopwords out)."""
    stop = {"the", "and", "owner", "decision", "gate", "choice", "pick", "with"}
    return {w for w in re.findall(r"[a-z]+", lead.lower()) if len(w) > 3 and w not in stop}


def valid_iso_date(token: str) -> bool:
    """True when token is a real calendar date, not just date-shaped."""
    try:
        datetime.date.fromisoformat(token)
    except ValueError:
        return False
    return True


def parse_gate_file(path: Path, display: str, result: ParseResult) -> None:
    """One gate file → decisions + a click group + lint findings.

    Tolerant: every problem is recorded (manual for derive, errors for
    lint), never raised. The file is never modified.
    """
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeDecodeError) as error:
        result.manual.append((display, f"unreadable ({error})"))
        result.errors.append((display, f"unreadable ({error})"))
        return

    title = ""
    for line in lines:
        match = H1_RE.match(line)
        if match:
            title = strip_markup(match.group(1))
            break
    if not title:
        result.errors.append((display, "no `# <title>` H1 found (the queue title)"))
        title = display

    body = gate_section(lines)
    if body is None:
        result.manual.append((display, "no `## … OWNER-GATE` section found"))
        result.errors.append((display, "no `## … OWNER-GATE` section found"))
        return

    steps = collect_items(body, STEP_RE)
    boxes = collect_items(body, CHECKBOX_RE)
    checked = collect_items(body, CHECKED_RE)
    unchecked = collect_items(body, UNCHECKED_RE)

    def is_owner_row(text: str) -> bool:
        return text.lstrip().startswith(FLAG) and "**Owner:**" in text

    done_rows = [b for b in checked if is_owner_row(b) and DONE_RE.search(b)]
    done_set = set(done_rows)
    owner_boxes = [b for b in boxes if is_owner_row(b) and b not in done_set]

    # Lint: half-flipped dispositions. A checked owner box without the
    # DONE marker, or an unchecked one carrying it, still QUEUES in
    # derive (fail-safe: never silently drop an owner action) but is an
    # error in lint — flip both marks or neither.
    for b in checked:
        if is_owner_row(b) and not DONE_RE.search(b):
            result.errors.append(
                (display, f"checked {FLAG} Owner box without `— DONE <ISO date>`: "
                          f"“{strip_markup(b)[:60]}” — flip both marks or neither")
            )
    for b in unchecked:
        if is_owner_row(b) and DONE_RE.search(b):
            result.errors.append(
                (display, f"`— DONE` marker on an UNCHECKED {FLAG} Owner box: "
                          f"“{strip_markup(b)[:60]}” — flip both marks or neither")
            )
    for b in done_rows:
        date_token = DONE_RE.search(b).group(1)
        if not valid_iso_date(date_token):
            result.errors.append(
                (display, f"DONE date `{date_token}` is not a real calendar date")
            )

    # KILL-CHECK checkpoints (packet-level kill clock, live products).
    checkpoints: list[dict] = []
    for payload in collect_items(body, KILLCHECK_RE):
        chunks = payload.split(TIMER)
        if len(chunks) == 1:
            note = f"KILL-CHECK line carries no {TIMER} <ISO date> token"
            result.manual.append((display, note))
            result.errors.append((display, note))
            continue
        for chunk in chunks[1:]:
            chunk = strip_markup(chunk.replace("\ufe0f", "")).strip(" ·")
            match = CHECKPOINT_DATE_RE.match(chunk)
            if not match or not valid_iso_date(match.group(1)):
                note = (
                    f"KILL-CHECK {TIMER} token skipped — no leading valid ISO date "
                    f"(YYYY-MM-DD): “{chunk[:60]}”"
                )
                result.manual.append((display, note))
                result.errors.append((display, note))
                continue
            checkpoints.append(
                {"date": match.group(1), "label": match.group(2).strip(" ·—–-")}
            )
    checkpoints.sort(key=lambda c: (c["date"], c["label"]))

    if not steps and not owner_boxes and not done_rows:
        note = f"OWNER-GATE section present but no steps and no {FLAG} Owner rows parsed"
        result.manual.append((display, note))
        result.errors.append((display, note))
        return

    blocked = any("blocking" in b.lower() for b in owner_boxes)

    # DECISIONS: numbered steps carrying an inline ⚑ — "this step is an
    # open owner choice". Each needs a machine-findable bolded default.
    decision_keys: set[str] = set()
    for index, step in enumerate(steps, start=1):
        if FLAG not in step:
            continue
        lead = decision_lead(step)
        default = extract_default(step)
        if not default:
            note = (
                f"decision step {index} (“{lead}”) has no parseable default — "
                f"mark it `**<pick>** (default …)`"
            )
            result.manual.append((display, note))
            result.errors.append((display, note))
            default = "*(no default parsed — see the gate file)*"
        unblocks = (
            f"the entire remaining “{title}” click-run — hard gate, nothing below it proceeds"
            if blocked
            else f"the “{title}” click-run continuing past this pick"
        )
        step_text = strip_markup(step)
        if len(step_text) > 300:
            step_text = step_text[:300] + "…"
        result.decisions.append(
            Decision(
                label=f"{title} — {lead}",
                what=step_text,
                where=f"`{display}` @ OWNER-GATE step {index}",
                default=default,
                unblocks=unblocks,
                source=display,
            )
        )
        decision_keys |= lead_keywords(lead)

    group = ClickGroup(
        title=title,
        where=f"`{display}` @ OWNER-GATE checklist",
        blocked=blocked,
        checkpoints=checkpoints,
    )
    for box in owner_boxes:
        text = box.lstrip()[len(FLAG):].lstrip().replace("**Owner:**", "", 1).strip()
        clean = strip_markup(text)
        linked = bool(decision_keys & lead_keywords(clean))
        group.clicks.append(
            {"what": clean, "default": extract_default(box) or "", "linked": linked}
        )
    for box in done_rows:
        text = box.lstrip()[len(FLAG):].lstrip().replace("**Owner:**", "", 1).strip()
        match = DONE_RE.search(text)
        what = strip_markup(text[: match.start()] + " " + text[match.end():])
        group.done.append({"what": what, "date": match.group(1)})
    if group.clicks:
        result.groups.append(group)
    if group.done:
        result.live.append(group)
    result.parsed_files.append(display)


def discover(gates: list[str], output: str) -> list[tuple[Path, str]]:
    """(path, display) pairs, deterministic order; the output file and
    any EXPECTED-* comparison files are never treated as inputs."""
    out_resolved = Path(output).resolve()
    seen: dict[str, Path] = {}
    for entry in gates:
        p = Path(entry)
        if p.is_dir():
            candidates = sorted(p.rglob("*.md"))
        elif p.is_file():
            candidates = [p]
        else:
            continue  # missing path → zero inputs (derive skips, lint FAILs)
        for c in candidates:
            try:
                resolved = c.resolve()
            except OSError:
                continue
            if resolved == out_resolved:
                continue  # never parse our own output
            if c.name.startswith("EXPECTED-"):
                continue  # committed comparison outputs, not gates
            display = c.as_posix()
            if display not in seen:
                seen[display] = c
    return [(seen[d], d) for d in sorted(seen)]


def render(result: ParseResult) -> str:
    """The generated queue content (deterministic — no timestamps)."""
    out: list[str] = []
    out.append(f"# {FLAG} Owner queue — every decision and click, in one list")
    out.append("")
    out.append("> GENERATED FILE — regenerate with `ocq.py derive`; edit the")
    out.append("> gate files, never this file. A stale copy of this file is a")
    out.append("> bug in the workflow, never in the gate files.")
    out.append("")
    out.append(
        "The agents performed NONE of the actions below — every item is an "
        "owner click or an owner choice, queued and pre-chewed. Decisions "
        "come first (each with a bolded default so “agree” is a one-word "
        "reply); the pure click-run sequences follow."
    )
    out.append("")

    out.append("## 1. Decisions — pick the default or override")
    out.append("")
    if not result.decisions:
        out.append("*(none parsed — every gate is pure click-run)*")
        out.append("")
    for i, d in enumerate(result.decisions, start=1):
        out.append(f"### D{i} — {d.label}")
        out.append("")
        out.append(f"- **WHAT:** {d.what}")
        out.append(f"- **WHERE:** {d.where}")
        out.append(f"- **DEFAULT:** {d.default}")
        out.append(f"- **UNBLOCKS:** {d.unblocks}")
        out.append("")

    out.append("## 2. Click-run — mechanical owner clicks, paste-ready")
    out.append("")
    if not result.groups:
        out.append("*(none parsed)*")
        out.append("")
    ordered = sorted(result.groups, key=lambda g: (g.blocked, g.title.lower()))
    for group in ordered:
        gate = " — **HARD-GATED** (a D-item above blocks this sequence)" if group.blocked else ""
        out.append(f"### {group.title} — {group.where}{gate}")
        out.append("")
        for click in group.clicks:
            parts = [f"**WHAT:** {click['what']}"]
            if click["linked"] and click["default"]:
                parts.append(f"**DEFAULT:** {click['default']} (executes its D-item above)")
            elif click["linked"]:
                parts.append("**DEFAULT:** executes its D-item above")
            elif click["default"]:
                parts.append(f"**DEFAULT:** {click['default']}")
            parts.append("**UNBLOCKS:** the next click in this sequence")
            out.append("- [ ] " + " · ".join(parts))
        out.append("")

    out.append("## 3. Manual review — gate files the parser could not read reliably")
    out.append("")
    if result.manual:
        out.append(
            "These files were NOT normalized or edited (tolerant-parser "
            "contract); a human or a later session should look at them:"
        )
        out.append("")
        for fname, why in result.manual:
            out.append(f"- `{fname}` — {why}")
    else:
        out.append("*(none — every input parsed clean)*")
    out.append("")

    if result.live:
        out.append("## 4. Live / completed — already executed, read-only")
        out.append("")
        out.append(
            f"Derived from checked `- [x] {FLAG} **Owner:** … — DONE <date>` "
            "rows: owner actions ALREADY executed. Nothing here is queued, "
            "and nothing here counts toward the pending totals above."
        )
        out.append("")
        for group in sorted(result.live, key=lambda g: g.title.lower()):
            out.append(f"### {group.title} — {group.where}")
            out.append("")
            for row in group.done:
                out.append(f"- [x] {row['what']} · **DONE:** {row['date']}")
            for i, cp in enumerate(group.checkpoints):
                head = "**Next checkpoint:**" if i == 0 else "then:"
                label = f" — {cp['label']}" if cp["label"] else ""
                out.append(f"- {TIMER} {head} {cp['date']}{label}")
            out.append("")
    return "\n".join(out)


def parse_all(gates: list[str], output: str) -> tuple[ParseResult, int]:
    result = ParseResult()
    files = discover(gates, output)
    for path, display in files:
        parse_gate_file(path, display, result)
    return result, len(files)


def cmd_derive(gates: list[str], output: str) -> int:
    """Advisory contract: exits 0 on EVERY path."""
    result, total = parse_all(gates, output)
    if total == 0:
        print(f"ocq: skipped — no gate files found under {', '.join(gates)}")
        return 0
    try:
        Path(output).write_text(render(result), encoding="utf-8")
    except OSError as error:
        print(f"ocq: FAILED to write {output} ({error})")
        return 0  # advisory: report, never fail the caller
    clean = len(result.parsed_files) - len(
        {f for f, _ in result.manual} & set(result.parsed_files)
    )
    clicks = sum(len(g.clicks) for g in result.groups)
    print(f"ocq: regenerated {output}")
    print(
        f"ocq: parsed {clean} of {total} gate files clean; "
        f"{len(result.decisions)} decisions, {clicks} owner clicks "
        f"across {len(result.groups)} click-run sequences"
    )
    if result.live:
        done_rows = sum(len(g.done) for g in result.live)
        print(
            f"ocq: live/completed {done_rows} DONE rows across "
            f"{len(result.live)} gates (read-only; excluded from pending totals)"
        )
        for group in sorted(result.live, key=lambda g: g.title.lower()):
            if group.checkpoints:
                nxt = group.checkpoints[0]
                label = f" — {nxt['label']}" if nxt["label"] else ""
                print(
                    f"ocq:   {TIMER} [{group.title}] next checkpoint "
                    f"{nxt['date']}{label} ({len(group.checkpoints)} armed)"
                )
    for i, decision in enumerate(result.decisions, start=1):
        print(f"ocq:   D{i} [{decision.source}] default {strip_markup(decision.default)}")
    if result.manual:
        for fname, why in result.manual:
            print(f"ocq: manual-review {fname} — {why}")
    else:
        print("ocq: manual-review — none")
    return 0


def cmd_lint(gates: list[str], output: str) -> int:
    """Strict contract: exit 1 on any malformed gate (or zero inputs)."""
    result, total = parse_all(gates, output)
    if total == 0:
        print(f"ocq lint: FAIL — no gate files found under {', '.join(gates)}")
        return 1
    if result.errors:
        for fname, why in result.errors:
            print(f"ocq lint: {fname}: {why}")
        print(f"ocq lint: FAIL — {len(result.errors)} problem(s) in {total} gate file(s)")
        return 1
    clicks = sum(len(g.clicks) for g in result.groups)
    done_rows = sum(len(g.done) for g in result.live)
    print(
        f"ocq lint: OK — {total} gate file(s) clean; "
        f"{len(result.decisions)} decisions, {clicks} pending clicks, "
        f"{done_rows} DONE rows"
    )
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="ocq",
        description="Derive (tolerant) or lint (strict) the owner click-queue from OWNER-GATE files.",
    )
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("derive", "lint"):
        p = sub.add_parser(name)
        p.add_argument(
            "--gates",
            action="append",
            default=None,
            help=f"gate file or directory (repeatable; default: {DEFAULT_GATES}/)",
        )
        p.add_argument("--output", default=DEFAULT_OUTPUT)
    args = parser.parse_args(argv)
    gates = args.gates if args.gates else [DEFAULT_GATES]
    if args.command == "derive":
        try:
            return cmd_derive(gates, args.output)
        except Exception as error:  # advisory contract: NEVER a nonzero exit
            print(f"ocq: skipped — unexpected parser failure ({error})")
            return 0
    return cmd_lint(gates, args.output)


if __name__ == "__main__":
    sys.exit(main())
