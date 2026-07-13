#!/usr/bin/env python3
"""scripts/check_kill_clocks.py — ADVISORY kill-clock DUE/OVERDUE checker.

Reads the packet-level `KILL-CHECK: ⏲ <ISO date> <label> [· ⏲ …]` lines of
the vetting packets under docs/publishing/vetting/*.md and prints, per LIVE
product, whether each checkpoint is OVERDUE, DUE today, or upcoming relative
to a caller-supplied date:

    kill-clock: [<product>] OVERDUE 2026-07-19 — T+7 funnel checkpoint (3 days overdue)
    kill-clock: [<product>] DUE today 2026-07-19 — T+7 funnel checkpoint
    kill-clock: [<product>] upcoming 2026-07-26 — T+14 kill-rule deadline (in 7 days)
    kill-clock: checked N checkpoints across M live products — X overdue, Y due today, Z upcoming

PARSE REUSE, NOT A FORK: this script imports `parse_packet` (+ `ParseResult`)
from `derive_owner_queue.py` and reads the checkpoints that parser already
extracts — the KILL-CHECK grammar, tolerant-parser behavior, and the
"a kill clock only ticks once live" rule (checkpoints count only on packets
with DONE rows) live in ONE place. If the grammar evolves there, this
advisory follows automatically.

WHY `--today` IS REQUIRED (no default, deliberately): the owner-queue
generator family is deliberately timestamp-free — output depends only on
input file content, so re-runs on the same tree are byte-identical and
reviewable as plain diffs. Reading the wall clock would break that property,
so the impure "what day is it?" input is confined to this separate advisory
and made explicit: the caller must pass `--today YYYY-MM-DD` (e.g.
`--today "$(date -u +%F)"` in a wake ritual). The same invocation on the
same tree therefore always prints the same lines.

ADVISORY ONLY — exits 0 on EVERY path (upcoming, due, overdue, no tokens,
malformed input, unexpected failure), same contract as
`check_ledger_drift.py` and `derive_owner_queue.py`: it nags, never gates.
Malformed ⏲ dates are reported and skipped, never a hard error.

Stdlib only. No network. Never writes any file.

Run: python3 scripts/check_kill_clocks.py --today "$(date -u +%F)"

Origin: PR #128's session-card 💡 idea — the queue shows each live
product's next ⏲ checkpoint, but nothing computed "is it DUE?"; the owner
still had to compare dates against today by eye.
"""

from __future__ import annotations

import argparse
import datetime
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from derive_owner_queue import (  # noqa: E402
    DEFAULT_VETTING_DIR,
    TIMER,
    ParseResult,
    parse_packet,
)

PREFIX = "kill-clock:"


def parse_iso(text: str) -> datetime.date | None:
    """The date, or None when not a real calendar date (e.g. 2026-13-45)."""
    try:
        return datetime.date.fromisoformat(text)
    except ValueError:
        return None


def run(vetting_dir: str, today_text: str) -> int:
    today = parse_iso(today_text)
    if today is None:
        print(
            f"{PREFIX} skipped — --today is not a real ISO date "
            f"(YYYY-MM-DD): {today_text!r}"
        )
        return 0

    vdir = Path(vetting_dir)
    packets = sorted(vdir.glob("*.md")) if vdir.is_dir() else []
    if not packets:
        print(f"{PREFIX} skipped — no packets found under {vetting_dir}")
        return 0

    result = ParseResult()
    for packet in packets:
        parse_packet(packet, result)

    overdue = due = upcoming = skipped = 0
    live_with_clocks = 0
    # result.live: only packets with DONE rows (live products) — the kill
    # clock only ticks once live, same rule as the generator's Live section.
    for group in sorted(result.live, key=lambda g: g.title.lower()):
        if not group.checkpoints:
            continue
        live_with_clocks += 1
        for cp in group.checkpoints:  # already sorted earliest-first
            when = parse_iso(cp["date"])
            label = f" — {cp['label']}" if cp["label"] else ""
            if when is None:
                # ISO-shaped but not a real date; derive_owner_queue's regex
                # can't catch this, so report it here (and skip, never fail).
                skipped += 1
                print(
                    f"{PREFIX} [{group.title}] {TIMER} SKIPPED {cp['date']}"
                    f"{label} — ISO-shaped but not a real calendar date"
                )
                continue
            delta = (when - today).days
            if delta < 0:
                overdue += 1
                plural = "day" if delta == -1 else "days"
                print(
                    f"{PREFIX} [{group.title}] {TIMER} OVERDUE {cp['date']}"
                    f"{label} ({-delta} {plural} overdue)"
                )
            elif delta == 0:
                due += 1
                print(f"{PREFIX} [{group.title}] {TIMER} DUE today {cp['date']}{label}")
            else:
                upcoming += 1
                plural = "day" if delta == 1 else "days"
                print(
                    f"{PREFIX} [{group.title}] {TIMER} upcoming {cp['date']}"
                    f"{label} (in {delta} {plural})"
                )

    total = overdue + due + upcoming
    if total == 0 and skipped == 0:
        print(
            f"{PREFIX} no live kill-clock checkpoints found "
            f"({len(packets)} packets scanned under {vetting_dir})"
        )
        return 0
    print(
        f"{PREFIX} checked {total} checkpoints across {live_with_clocks} live "
        f"products — {overdue} overdue, {due} due today, {upcoming} upcoming"
        + (f", {skipped} skipped (malformed date)" if skipped else "")
    )
    if overdue or due:
        print(f"{PREFIX} ACTION — see the packet's §7 KILL-CHECK line and the launch log")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="check_kill_clocks",
        description=(
            "Advisory DUE/OVERDUE report for packet KILL-CHECK kill-clock "
            "checkpoints — always exits 0."
        ),
    )
    parser.add_argument(
        "--today",
        default=None,
        metavar="YYYY-MM-DD",
        help=(
            "the date to compare checkpoints against (REQUIRED — the "
            'generator family is timestamp-free by design; pass "$(date -u +%%F)")'
        ),
    )
    parser.add_argument("--vetting-dir", default=DEFAULT_VETTING_DIR)
    args = parser.parse_args(argv)
    if args.today is None:
        # Required-but-advisory: never a hard usage error (exit-0 contract),
        # but there is NO default — the impure "what day is it?" input must
        # be explicit (see the module docstring).
        print(
            f"{PREFIX} skipped — --today YYYY-MM-DD is required "
            '(no default by design; pass e.g. --today "$(date -u +%F)")'
        )
        return 0
    try:
        return run(args.vetting_dir, args.today)
    except Exception as error:  # advisory contract: NEVER a nonzero exit
        print(f"{PREFIX} skipped — unexpected failure ({error})")
        return 0


if __name__ == "__main__":
    sys.exit(main())
