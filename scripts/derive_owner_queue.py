#!/usr/bin/env python3
"""scripts/derive_owner_queue.py — derive the ⚑ owner queue from packets.

Parses the §7 ⚑ OWNER-GATE blocks of every vetting packet under
docs/publishing/vetting/*.md, plus ⚑ OWNER-flagged conflict sections in
docs/publishing/keyword-map.md, and deterministically regenerates
docs/publishing/OWNER-QUEUE.md — one consolidated, paste-ready owner
list: DECISIONS first (each with a bolded default), then the pure
click-run publish sequences. "What can the owner click right now?" is a
derived fact that can never silently drift from the packets (origin:
PR #91's session-card 💡 idea).

TOLERANT parser + ADVISORY contract, mirroring check_ledger_drift.py:
this script exits 0 on EVERY path. A packet whose §7 can't be parsed
reliably is never normalized or edited — it is listed in the generated
file's "Manual review" section and on stdout, and the run still
succeeds. Determinism: output depends only on input file content
(sorted traversal, no timestamps), so re-runs on the same tree are
byte-identical.

Stdlib only. No network. Never edits the packets it reads.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

DEFAULT_VETTING_DIR = "docs/publishing/vetting"
DEFAULT_KEYWORD_MAP = "docs/publishing/keyword-map.md"
DEFAULT_OUTPUT = "docs/publishing/OWNER-QUEUE.md"

FLAG = "\N{BLACK FLAG}"  # ⚑ — the repo's owner-gate marker

# §7 heading: "## 7. ⚑ OWNER-GATE — ..." (tolerate spacing/wording drift
# as long as the section number and OWNER-GATE both appear).
SECTION7_RE = re.compile(r"^##\s*7\..*OWNER-GATE", re.IGNORECASE)
HEADING_RE = re.compile(r"^##\s")
TITLE_RE = re.compile(r"^#\s*Title Vetting\s*[—-]\s*(.+?)\s*$")
STEP_RE = re.compile(r"^(\d+)\.\s+(.*)$")
CHECKBOX_RE = re.compile(r"^- \[[ xX]\]\s+(.*)$")
# DONE disposition: a CHECKED owner box whose text carries "— DONE <ISO date>"
# is an already-executed click (product live), rendered read-only in the
# "Live / completed" section and NEVER counted as a pending click. Both marks
# are required — a checked box without DONE still queues (legacy tolerance),
# and an unchecked box with DONE text still queues (the click isn't done).
CHECKED_RE = re.compile(r"^- \[[xX]\]\s+(.*)$")
DONE_RE = re.compile(r"[—–-]\s*DONE\s+(\d{4}-\d{2}-\d{2})")
BOLD_RE = re.compile(r"\*\*(.+?)\*\*")
# Conflict sections in the keyword map: "### C1 — ..."
CONFLICT_RE = re.compile(r"^###\s*(C\d+)\s*[—-]\s*(.+?)\s*$")


@dataclass
class Decision:
    label: str  # heading, e.g. "The Weigh House — Title + subtitle"
    what: str
    where: str
    default: str  # already-bolded markdown, or "" when unparsed
    unblocks: str
    source: str  # short file token, e.g. "the-weigh-house.md"


@dataclass
class ClickGroup:
    title: str
    where: str
    blocked: bool
    clicks: list[dict] = field(default_factory=list)
    done: list[dict] = field(default_factory=list)  # {"what", "date"} rows


@dataclass
class ParseResult:
    decisions: list[Decision] = field(default_factory=list)
    groups: list[ClickGroup] = field(default_factory=list)
    live: list[ClickGroup] = field(default_factory=list)  # groups with DONE rows
    manual: list[tuple[str, str]] = field(default_factory=list)  # (file, why)
    parsed_files: list[str] = field(default_factory=list)


def strip_markup(text: str) -> str:
    """Markdown bold/italic/backticks removed; whitespace collapsed."""
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text, flags=re.DOTALL)
    text = re.sub(r"\*(.+?)\*", r"\1", text, flags=re.DOTALL)
    text = text.replace("`", "")
    return re.sub(r"\s+", " ", text).strip()


def section7(lines: list[str]) -> list[str] | None:
    """The §7 block's lines (heading excluded), or None when absent."""
    start = None
    for i, line in enumerate(lines):
        if SECTION7_RE.match(line):
            start = i + 1
            break
    if start is None:
        return None
    body: list[str] = []
    for line in lines[start:]:
        if HEADING_RE.match(line):
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


def extract_default(step: str) -> str:
    """The step's recommended default as a bolded markdown span, or ''.

    Priority: (1) the **bold** span immediately followed by
    "(default" / "(recommended default" — the packets' convention for
    marking the default pick; (2) a **bold** span that itself says
    "recommend"; (3) a parenthetical containing "recommend".
    """
    marked = re.search(
        r"\*\*([^*]+?)\*\*\s*\((?:recommended\s+)?default", step, re.IGNORECASE
    )
    if marked:
        return f"**{marked.group(1)}**"
    for match in BOLD_RE.finditer(step):
        if "recommend" in match.group(1).lower():
            return f"**{match.group(1)}**"
    paren = re.search(r"\(([^()]*recommend[^()]*)\)", step, re.IGNORECASE)
    if paren:
        return f"**{strip_markup(paren.group(1))}**"
    return ""


def decision_lead(step: str) -> str:
    """The step's bold lead ("Title + subtitle (...)") minus flag/parens."""
    match = BOLD_RE.match(step.strip())
    lead = match.group(1) if match else step
    lead = lead.replace(FLAG, "")
    lead = re.sub(r"\([^)]*\)", "", lead)
    return strip_markup(lead).rstrip(":").strip()


def lead_keywords(lead: str) -> set[str]:
    """Distinctive lowercase words of a decision lead (stopwords out)."""
    stop = {"the", "and", "owner", "kdp", "decision", "gate", "choice", "pick"}
    return {w for w in re.findall(r"[a-z]+", lead.lower()) if len(w) > 3 and w not in stop}


def parse_packet(path: Path, result: ParseResult) -> None:
    """One vetting packet → decisions + a click group, tolerantly."""
    name = path.name
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeDecodeError) as error:
        result.manual.append((name, f"unreadable ({error})"))
        return

    title = name
    for line in lines[:5]:
        match = TITLE_RE.match(line)
        if match:
            title = strip_markup(match.group(1))
            break

    body = section7(lines)
    if body is None:
        result.manual.append((name, "no `## 7. … OWNER-GATE` section found"))
        return

    steps = collect_items(body, STEP_RE)
    boxes = collect_items(body, CHECKBOX_RE)
    # DONE rows: checked (- [x]) owner boxes carrying the "— DONE <date>"
    # marker. Everything else — including checked boxes WITHOUT the marker —
    # keeps the legacy pending-click behavior, byte-for-byte.
    checked = collect_items(body, CHECKED_RE)
    done_rows = [
        b
        for b in checked
        if b.lstrip().startswith(FLAG) and "**Owner:**" in b and DONE_RE.search(b)
    ]
    done_set = set(done_rows)
    owner_boxes = [
        b
        for b in boxes
        if b.lstrip().startswith(FLAG) and "**Owner:**" in b and b not in done_set
    ]
    if not steps and not owner_boxes and not done_rows:
        result.manual.append(
            (name, "§7 present but no OWNER-ACTION steps and no ⚑ Owner checkboxes parsed")
        )
        return

    blocked = any("blocking" in b.lower() for b in owner_boxes)

    # DECISIONS: numbered OWNER-ACTION steps that carry an inline ⚑ —
    # the packets' own convention for "this step is an open owner choice".
    decision_keys: set[str] = set()
    for index, step in enumerate(steps, start=1):
        if FLAG not in step:
            continue
        lead = decision_lead(step)
        default = extract_default(step)
        if not default:
            result.manual.append(
                (name, f"decision step {index} (“{lead}”) parsed but no default/recommendation found")
            )
            default = "*(no default parsed — see the packet)*"
        unblocks = (
            f"the entire remaining “{title}” click-run — hard gate, nothing below it proceeds"
            if blocked
            else f"the “{title}” publish sequence continuing past this pick"
        )
        step_text = strip_markup(step)
        if len(step_text) > 300:
            step_text = step_text[:300] + "…"
        result.decisions.append(
            Decision(
                label=f"{title} — {lead}",
                what=step_text,
                where=f"`{DEFAULT_VETTING_DIR}/{name}` @ §7, OWNER-ACTION step {index}",
                default=default,
                unblocks=unblocks,
                source=name,
            )
        )
        decision_keys |= lead_keywords(lead)

    group = ClickGroup(
        title=title,
        where=f"`{DEFAULT_VETTING_DIR}/{name}` @ §7 checklist",
        blocked=blocked,
    )
    for box in owner_boxes:
        text = box.lstrip()
        text = text[len(FLAG) :].lstrip()
        text = text.replace("**Owner:**", "", 1).strip()
        clean = strip_markup(text)
        linked = bool(decision_keys & lead_keywords(clean))
        default = extract_default(box) or ""
        group.clicks.append({"what": clean, "default": default, "linked": linked})
    for box in done_rows:
        text = box.lstrip()
        text = text[len(FLAG) :].lstrip()
        text = text.replace("**Owner:**", "", 1).strip()
        match = DONE_RE.search(text)
        what = strip_markup(text[: match.start()] + " " + text[match.end() :])
        group.done.append({"what": what, "date": match.group(1)})
    if group.clicks:
        result.groups.append(group)
    if group.done:
        result.live.append(group)
    result.parsed_files.append(name)


def parse_keyword_map(path: Path, result: ParseResult) -> None:
    """⚑ OWNER-flagged conflict sections (C1-style) → decisions."""
    name = path.name
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeDecodeError) as error:
        result.manual.append((name, f"unreadable ({error})"))
        return

    sections: list[tuple[str, str, list[str]]] = []
    current: tuple[str, str, list[str]] | None = None
    for line in lines:
        match = CONFLICT_RE.match(line)
        if match:
            if current:
                sections.append(current)
            current = (match.group(1), strip_markup(match.group(2)), [])
            continue
        if line.startswith("## ") and current:
            sections.append(current)
            current = None
            continue
        if current:
            current[2].append(line)
    if current:
        sections.append(current)

    if not sections:
        result.manual.append((name, "no `### C<N> —` conflict sections parsed"))
        return

    found_flagged = False
    for cid, heading, body in sections:
        text = "\n".join(body)
        if f"{FLAG} OWNER" not in text:
            continue  # resolved/watched conflicts need no owner click
        found_flagged = True
        # Default: the bold span following "proposed" in the resolution
        # paragraph, else the first bold span after "Proposed resolution".
        default = ""
        resolution = re.search(
            r"\*\*Proposed resolution:\*\*(.*?)(?:\n\n|\Z)", text, re.DOTALL
        )
        scope = resolution.group(1) if resolution else text
        prop = re.search(r"proposed\s+\*\*(.+?)\*\*", scope, re.DOTALL)
        if prop:
            default = f"**accept the proposed resolution — {strip_markup(prop.group(1))}**"
        else:
            bold = BOLD_RE.search(scope)
            if bold:
                default = f"**accept the proposed resolution — {strip_markup(bold.group(1))}**"
        if not default:
            result.manual.append(
                (name, f"{cid} is ⚑ OWNER-flagged but no proposed resolution parsed")
            )
            default = "*(no default parsed — see the map)*"
        summary = strip_markup(scope)
        summary = summary[:300] + "…" if len(summary) > 300 else summary
        result.decisions.append(
            Decision(
                label=f"Keyword map {cid} — {heading.split(':', 1)[0]}",
                what=f"{heading} — proposed resolution: {summary}",
                where=f"`{DEFAULT_KEYWORD_MAP}` @ §2 {cid}",
                default=default,
                unblocks=(
                    "applying the resolution to the affected packet's §6 and the map's "
                    "ownership rows (packets are edited only on this approval)"
                ),
                source=name,
            )
        )
    result.parsed_files.append(name)
    if not found_flagged:
        # Informational only — a map with zero flagged conflicts is healthy.
        pass


def render(result: ParseResult, vetting_dir: str) -> str:
    """The generated OWNER-QUEUE.md content (deterministic)."""
    out: list[str] = []
    out.append(f"# {FLAG} Owner queue — every decision and click, in one list")
    out.append("")
    out.append("> **Status:** `owner-guidance`")
    out.append(">")
    out.append(
        "> GENERATED FILE — generated by `scripts/derive_owner_queue.py` — "
        "edit packets, not this file."
    )
    out.append(
        f"> Derived from the §7 {FLAG} OWNER-GATE blocks of "
        f"`{vetting_dir}/*.md` plus {FLAG} OWNER-flagged conflicts in "
        f"`{DEFAULT_KEYWORD_MAP}`. Re-run the script after any packet "
        "change; a stale copy of this file is a bug in the workflow, "
        "never in the packets."
    )
    out.append("")
    out.append(
        "The seat performed NONE of the actions below — every item is an "
        "owner click or an owner choice, queued and pre-chewed. Decisions "
        "come first (each with a bolded default so “agree” is a one-word "
        "reply); the pure click-run publish sequences follow."
    )
    out.append("")

    out.append("## 1. Decisions — pick the default or override")
    out.append("")
    if not result.decisions:
        out.append("*(none parsed — every packet is pure click-run)*")
        out.append("")
    for i, d in enumerate(result.decisions, start=1):
        out.append(f"### D{i} — {d.label}")
        out.append("")
        out.append(f"- **WHAT:** {d.what}")
        out.append(f"- **WHERE:** {d.where}")
        out.append(f"- **DEFAULT:** {d.default}")
        out.append(f"- **UNBLOCKS:** {d.unblocks}")
        out.append("")

    out.append("## 2. Click-run — mechanical publish clicks, paste-ready")
    out.append("")
    if not result.groups:
        out.append("*(none parsed)*")
        out.append("")
    # Unblocked sequences first, hard-gated ones last; alphabetical within.
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

    out.append("## 3. Manual review — packets the parser could not read reliably")
    out.append("")
    if result.manual:
        out.append(
            "These files were NOT normalized or edited (tolerant-parser "
            "contract); a human or a later slice should look at them:"
        )
        out.append("")
        for fname, why in result.manual:
            out.append(f"- `{fname}` — {why}")
    else:
        out.append("*(none — every input parsed clean)*")
    out.append("")

    # Live / completed — rendered ONLY when a packet carries DONE rows, so
    # trees without the disposition regenerate byte-identically to before.
    if result.live:
        out.append("## 4. Live / completed — already published, read-only")
        out.append("")
        out.append(
            f"Derived from checked `- [x] {FLAG} **Owner:** … — DONE <date>` "
            "rows: owner actions ALREADY executed (product live). Nothing "
            "here is queued, and nothing here counts toward the pending "
            "decision/click totals above."
        )
        out.append("")
        for group in sorted(result.live, key=lambda g: g.title.lower()):
            out.append(f"### {group.title} — {group.where}")
            out.append("")
            for row in group.done:
                out.append(f"- [x] {row['what']} · **DONE:** {row['date']}")
            out.append("")
    return "\n".join(out)


def run(vetting_dir: str, keyword_map: str, output: str) -> int:
    result = ParseResult()

    vdir = Path(vetting_dir)
    packets = sorted(vdir.glob("*.md")) if vdir.is_dir() else []
    if not packets:
        print(f"owner-queue: skipped — no packets found under {vetting_dir}")
        return 0
    for packet in packets:
        parse_packet(packet, result)

    kmap = Path(keyword_map)
    if kmap.is_file():
        parse_keyword_map(kmap, result)
    else:
        print(f"owner-queue: note — {keyword_map} missing; conflict scan skipped")

    try:
        Path(output).write_text(render(result, vetting_dir), encoding="utf-8")
    except OSError as error:
        print(f"owner-queue: FAILED to write {output} ({error})")
        return 0  # advisory contract: report, never fail the caller

    total_inputs = len(packets) + (1 if kmap.is_file() else 0)
    clean = len(result.parsed_files) - len({f for f, _ in result.manual} & set(result.parsed_files))
    clicks = sum(len(g.clicks) for g in result.groups)
    print(f"owner-queue: regenerated {output}")
    print(
        f"owner-queue: parsed {clean} of {total_inputs} inputs clean "
        f"({len(packets)} packets + keyword map); "
        f"{len(result.decisions)} decisions, {clicks} owner clicks "
        f"across {len(result.groups)} click-run sequences"
    )
    if result.live:
        done_rows = sum(len(g.done) for g in result.live)
        print(
            f"owner-queue: live/completed {done_rows} DONE rows across "
            f"{len(result.live)} products (read-only; excluded from pending totals)"
        )
    for d_index, decision in enumerate(result.decisions, start=1):
        print(f"owner-queue:   D{d_index} [{decision.source}] default {strip_markup(decision.default)}")
    if result.manual:
        for fname, why in result.manual:
            print(f"owner-queue: manual-review {fname} — {why}")
    else:
        print("owner-queue: manual-review — none")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="derive_owner_queue",
        description="Regenerate OWNER-QUEUE.md from packet §7 blocks — always exits 0.",
    )
    parser.add_argument("--vetting-dir", default=DEFAULT_VETTING_DIR)
    parser.add_argument("--keyword-map", default=DEFAULT_KEYWORD_MAP)
    parser.add_argument("--output", default=DEFAULT_OUTPUT)
    args = parser.parse_args(argv)
    try:
        return run(args.vetting_dir, args.keyword_map, args.output)
    except Exception as error:  # advisory contract: NEVER a nonzero exit
        print(f"owner-queue: skipped — unexpected parser failure ({error})")
        return 0


if __name__ == "__main__":
    sys.exit(main())
