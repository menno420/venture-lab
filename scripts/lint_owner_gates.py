#!/usr/bin/env python3
"""scripts/lint_owner_gates.py — STRICT lint of the ⚑ owner-gate data.

Validates the same inputs `derive_owner_queue.py` compiles — the §7
⚑ OWNER-GATE blocks of every vetting packet under
docs/publishing/vetting/*.md, plus ⚑ OWNER-flagged conflict sections in
docs/publishing/keyword-map.md — and exits 1 with per-file errors on any
malformed gate. This is the OCQK `lint` mode ported back into production
(dogfood-gap backport; origin: PR #153's session-card 💡 idea): the
derive script is deliberately TOLERANT (a malformed packet degrades to a
"Manual review" row and the run still exits 0), so nothing in CI ever
NAGGED when a packet's §7 stopped parsing — malformed gates were only
caught by eyeballing derive stdout.

Strict checks (each one a per-file error line on stdout):

  - unreadable input file;
  - missing `# Title Vetting — <name>` H1 (the queue title);
  - missing `## 7. … OWNER-GATE` section;
  - §7 present but no OWNER-ACTION steps and no ⚑ Owner checkboxes;
  - ⚑ decision step without a machine-findable bolded default;
  - half-flipped DONE disposition — a checked ⚑ Owner box without the
    `— DONE <ISO date>` marker, or an unchecked box carrying it (derive
    fail-safes both to PENDING; lint says flip both marks or neither);
  - a DONE date that is date-SHAPED but not a real calendar date (the
    derive regex alone accepts impossible dates like 2026-13-45);
  - a KILL-CHECK line with no ⏲ token, or a ⏲ token whose leading
    ISO date is missing or not a real calendar date;
  - a ⚑ OWNER-flagged keyword-map conflict with no parseable proposed
    resolution.

Contract: exit 0 only when every input parses clean (and at least one
packet exists — zero inputs is a FAIL: a lint that can't find its data
must never report success). Read-only: never writes or edits any file.
Wired into `.github/workflows/kit-tests.yml` as an ADVISORY step
(`continue-on-error: true`, the ledger-drift precedent) — it flags,
it never blocks unrelated work.

Grammar source of truth: this linter IMPORTS the regexes and parsing
helpers from `derive_owner_queue.py` (same module, same constants), so
lint and derive can never disagree about what a gate IS — the same
pinning discipline the OCQK kit uses (`grammar.py` shared by derive and
check). Stdlib only. No network.

Run: python3 scripts/lint_owner_gates.py
"""

from __future__ import annotations

import argparse
import datetime
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import derive_owner_queue as doq  # noqa: E402  (the grammar source of truth)

# Unchecked owner boxes — derive never needs to tell these apart from the
# generic CHECKBOX_RE, but the half-flipped-DONE check does.
UNCHECKED_RE = re.compile(r"^- \[ \]\s+(.*)$")


def valid_iso_date(token: str) -> bool:
    """True when token is a real calendar date, not just date-shaped.

    The derive regexes match `\\d{4}-\\d{2}-\\d{2}`, which accepts
    impossible dates (month 13, day 32); `datetime.date.fromisoformat`
    is the calendar truth.
    """
    try:
        datetime.date.fromisoformat(token)
    except ValueError:
        return False
    return True


def is_owner_row(text: str) -> bool:
    """A §7 checkbox that is an ⚑ **Owner:** row (the queueable kind)."""
    return text.lstrip().startswith(doq.FLAG) and "**Owner:**" in text


def clip(text: str, limit: int = 60) -> str:
    """A short, markup-stripped quote of the offending row."""
    clean = doq.strip_markup(text)
    return clean[:limit] + ("…" if len(clean) > limit else "")


def lint_packet(path: Path, errors: list[tuple[str, str]]) -> None:
    """One vetting packet → strict per-file findings appended to errors."""
    name = path.name
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeDecodeError) as error:
        errors.append((name, f"unreadable ({error})"))
        return

    if not any(doq.TITLE_RE.match(line) for line in lines[:5]):
        errors.append(
            (name, "no `# Title Vetting — <name>` H1 in the first 5 lines "
                   "(the queue title)")
        )

    body = doq.section7(lines)
    if body is None:
        errors.append((name, "no `## 7. … OWNER-GATE` section found"))
        return

    steps = doq.collect_items(body, doq.STEP_RE)
    boxes = doq.collect_items(body, doq.CHECKBOX_RE)
    checked = doq.collect_items(body, doq.CHECKED_RE)
    checked_set = set(checked)
    unchecked = [b for b in doq.collect_items(body, UNCHECKED_RE) if b not in checked_set]
    owner_boxes = [b for b in boxes if is_owner_row(b)]

    if not steps and not owner_boxes:
        errors.append(
            (name, "§7 present but no OWNER-ACTION steps and no ⚑ Owner "
                   "checkboxes parsed")
        )
        return

    # Half-flipped DONE dispositions. Derive fail-safes BOTH shapes to a
    # pending click (never silently drops an owner action) — lint makes
    # the inconsistency loud: flip both marks or neither.
    for box in checked:
        if not is_owner_row(box):
            continue
        match = doq.DONE_RE.search(box)
        if not match:
            errors.append(
                (name, f"checked {doq.FLAG} Owner box without `— DONE "
                       f"<ISO date>`: “{clip(box)}” — flip both marks or neither")
            )
        elif not valid_iso_date(match.group(1)):
            errors.append(
                (name, f"DONE date `{match.group(1)}` is not a real calendar date")
            )
    for box in unchecked:
        if is_owner_row(box) and doq.DONE_RE.search(box):
            errors.append(
                (name, f"`— DONE` marker on an UNCHECKED {doq.FLAG} Owner box: "
                       f"“{clip(box)}” — flip both marks or neither")
            )

    # ⚑ decision steps need a machine-findable bolded default — a
    # defaultless decision derives as a placeholder the owner can't
    # one-word-agree to.
    for index, step in enumerate(steps, start=1):
        if doq.FLAG not in step:
            continue
        if not doq.extract_default(step):
            lead = doq.decision_lead(step)
            errors.append(
                (name, f"decision step {index} (“{lead}”) has no parseable "
                       f"default — mark it `**<pick>** (default …)`")
            )

    # KILL-CHECK checkpoint lines (packet-level kill clock).
    for payload in doq.collect_items(body, doq.KILLCHECK_RE):
        chunks = payload.split(doq.TIMER)
        if len(chunks) == 1:
            errors.append(
                (name, f"KILL-CHECK line carries no {doq.TIMER} <ISO date> token")
            )
            continue
        for chunk in chunks[1:]:
            chunk = doq.strip_markup(chunk.replace("\ufe0f", "")).strip(" ·")
            match = doq.CHECKPOINT_DATE_RE.match(chunk)
            if not match or not valid_iso_date(match.group(1)):
                errors.append(
                    (name, f"KILL-CHECK {doq.TIMER} token has no leading valid "
                           f"ISO date (YYYY-MM-DD): “{chunk[:60]}”")
                )


def lint_keyword_map(path: Path, errors: list[tuple[str, str]]) -> None:
    """⚑ OWNER-flagged conflict sections must carry a parseable default."""
    name = path.name
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeDecodeError) as error:
        errors.append((name, f"unreadable ({error})"))
        return

    sections: list[tuple[str, list[str]]] = []
    current: tuple[str, list[str]] | None = None
    for line in lines:
        match = doq.CONFLICT_RE.match(line)
        if match:
            if current:
                sections.append(current)
            current = (match.group(1), [])
            continue
        if line.startswith("## ") and current:
            sections.append(current)
            current = None
            continue
        if current:
            current[1].append(line)
    if current:
        sections.append(current)

    if not sections:
        errors.append((name, "no `### C<N> —` conflict sections parsed"))
        return

    for cid, body in sections:
        text = "\n".join(body)
        if f"{doq.FLAG} OWNER" not in text:
            continue  # resolved/watched conflicts need no owner click
        resolution = re.search(
            r"\*\*Proposed resolution:\*\*(.*?)(?:\n\n|\Z)", text, re.DOTALL
        )
        scope = resolution.group(1) if resolution else text
        has_default = bool(
            re.search(r"proposed\s+\*\*(.+?)\*\*", scope, re.DOTALL)
            or doq.BOLD_RE.search(scope)
        )
        if not has_default:
            errors.append(
                (name, f"{cid} is {doq.FLAG} OWNER-flagged but no proposed "
                       f"resolution parsed")
            )


def run(vetting_dir: str, keyword_map: str) -> int:
    errors: list[tuple[str, str]] = []

    vdir = Path(vetting_dir)
    packets = sorted(vdir.glob("*.md")) if vdir.is_dir() else []
    if not packets:
        print(f"owner-gate-lint: FAIL — no packets found under {vetting_dir}")
        return 1
    for packet in packets:
        lint_packet(packet, errors)

    kmap = Path(keyword_map)
    total_inputs = len(packets)
    if kmap.is_file():
        lint_keyword_map(kmap, errors)
        total_inputs += 1
    else:
        print(f"owner-gate-lint: note — {keyword_map} missing; conflict scan skipped")

    if errors:
        for fname, why in errors:
            print(f"owner-gate-lint: {fname}: {why}")
        print(
            f"owner-gate-lint: FAIL — {len(errors)} problem(s) in "
            f"{total_inputs} input(s)"
        )
        return 1
    print(f"owner-gate-lint: OK — {total_inputs} input(s) clean")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="lint_owner_gates",
        description="STRICT lint of packet §7 OWNER-GATE blocks — exit 1 on any "
        "malformed gate.",
    )
    parser.add_argument("--vetting-dir", default=doq.DEFAULT_VETTING_DIR)
    parser.add_argument("--keyword-map", default=doq.DEFAULT_KEYWORD_MAP)
    args = parser.parse_args(argv)
    return run(args.vetting_dir, args.keyword_map)


if __name__ == "__main__":
    sys.exit(main())
