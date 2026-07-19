#!/usr/bin/env python3
"""check_owner_queue_staleness.py — guard the OWNER-QUEUE against STALENESS drift (ENG-7).

Why this exists
---------------
`docs/publishing/OWNER-QUEUE.md` is a GENERATED file: `scripts/derive_owner_queue.py`
derives it from the §7 ⚑ OWNER-GATE blocks of `docs/publishing/vetting/*.md` plus the
⚑ OWNER conflicts in `docs/publishing/keyword-map.md`.

ENG-6 (`check_owner_queue_idempotent.py`, #261) pins one property: the committed queue
is byte-identical to a fresh regeneration over its current inputs (idempotence). That
catches a hand-edit or an un-regenerated input drift. It does NOT — and by design
cannot — catch content that is internally INCONSISTENT even when it is perfectly
idempotent: a regenerated-and-therefore-idempotent queue can still carry a stale
cross-reference, a self-contradictory dated checkpoint, or a proofread-gated row that
lost its hard-gate. That orthogonal class is what "staleness" means here, and it is
this guard's job — the roadmap's ENG-7 / PUB-9 "OWNER-QUEUE staleness / proofread-gate
drift checker" (docs/ideas/2026-07-19-execution-roadmap.md line 82).

Three deterministic, OFFLINE consistency invariants
---------------------------------------------------
INV-1 — COMPANION CROSS-REF RESOLUTION (staleness / renumber-drift).
    The curated one-sitting companion `docs/publishing/OWNER-START-HERE.md` (#260)
    hand-cites into the generated queue: "OWNER-QUEUE.md §1 / §2" and specific
    decision IDs ("GitHub D6 → Slack D20 → Shopify D19", "D22–D25"). Those D-IDs are
    RENUMBERED whenever a packet adds/removes a ⚑ decision and the queue is
    regenerated — the exact #244/#245 renumber-mispoint class, one level UP from
    ENG-2's queue→packet D-ref guard (this is companion→queue). This invariant
    asserts every `§N` and `D<n>` the companion points at still resolves to a real
    `## N.` section / `### D<n> —` decision header in the committed queue, so a regen
    that renumbers decisions can't silently leave the digest pointing at a moved or
    vanished row.

INV-2 — DATED-CHECKPOINT CONSISTENCY (staleness / time, made STRUCTURAL).
    The §4 "Live / completed" section renders a live product's kill-clock checkpoints
    (e.g. the Stripe kit's ⏲ T+7 2026-07-19 / ⏲ T+14 2026-07-26). This invariant
    asserts each checkpoint date is a well-formed ISO CALENDAR date, and that any
    `T+<n>` day-offset labels that share an anchor are arithmetically consistent —
    T+7 followed by T+14 must be exactly +7 calendar days apart. It is deliberately a
    STRUCTURE / CONSISTENCY assertion, NOT a "has the date elapsed?" check: it never
    reads the wall clock, so the guard (and its test) are fully deterministic —
    wall-clock-dependent checks are banned in this repo. A packet edit that bumps one
    checkpoint date but not the paired one produces an idempotent-but-contradictory
    queue that ENG-6 passes and this invariant reds.

INV-3 — PROOFREAD-GATE INTEGRITY (proofread-gate DRIFT).
    A native-speaker-proofread pass is an inherently blocking owner quality gate — an
    NL/DE edition must never render as click-ready to publish un-proofread. Every §2
    click-run that carries such a row MUST be HARD-GATED. This invariant reuses the
    generator's OWN `PROOFREAD_GATE_RE` + `is_blocking_box`/`blocked` logic (so it can
    never drift from the render it guards) to assert exactly that, catching the
    #210/#213 owner-misleading class where a proofread-gated row is mis-rendered as an
    unblocked publish click.

Reuse, so the guard can never drift from the generator
------------------------------------------------------
Like ENG-6, this guard imports `derive_owner_queue` and drives its OWN parser
(`parse_packet`, `PROOFREAD_GATE_RE`) for INV-2/INV-3, and regexes the two committed
docs for INV-1 — no re-implementation of the queue format.

Exit 0 when every applicable invariant holds (or there is nothing to check); exit
non-zero with an itemized, per-invariant finding list when a staleness drift is
present. Stdlib-only. No network, no wall clock. Never writes the tree.
"""

from __future__ import annotations

import argparse
import datetime
import os
import re
import sys
from pathlib import Path

import derive_owner_queue as gen

# Resolve paths relative to the repo root (this file lives in scripts/), so the guard
# works regardless of the current working directory. Tests override the root with
# --root to point at a temp fixture tree.
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# The generated queue, its inputs, and the curated companion — as repo-relative paths.
# The derive script's own defaults ARE the ground truth for the queue + inputs, so
# reusing its constants keeps the guard and the generator pointed at the same files by
# construction.
VETTING_DIR_REL = gen.DEFAULT_VETTING_DIR       # docs/publishing/vetting
OWNER_QUEUE_REL = gen.DEFAULT_OUTPUT            # docs/publishing/OWNER-QUEUE.md
COMPANION_REL = "docs/publishing/OWNER-START-HERE.md"  # the #260 curated companion

# Committed-queue anchor headers.
QUEUE_SECTION_RE = re.compile(r"^##\s+(\d+)\.", re.MULTILINE)      # "## 4. Live / …"
QUEUE_DECISION_RE = re.compile(r"^###\s+D(\d+)\s*[—–-]", re.MULTILINE)  # "### D7 — …"

# Companion cross-references INTO the queue. A `D<n>` decision-ID is queue-specific, so
# it is collected anywhere; a bare `§N` is only treated as a queue section reference
# when it co-occurs on a line that names OWNER-QUEUE (how the companion actually writes
# them: "`OWNER-QUEUE.md` §1", "[OWNER-QUEUE.md](OWNER-QUEUE.md) §2"), so a future §ref
# to some OTHER doc can never false-red this guard.
COMPANION_DREF_RE = re.compile(r"\bD(\d+)(?:\s*[–-]\s*D(\d+))?\b")   # D7 or D22–D25
COMPANION_SREF_RE = re.compile(r"§\s*(\d+)")

# A `T+<n>` day-offset token inside a checkpoint label (T+7, T+14).
TPLUS_RE = re.compile(r"\bT\+(\d+)\b")


def _read(path: Path):
    """File text, or None when the file is absent/unreadable (tolerant)."""
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return None


def parse_tree(root=REPO_ROOT):
    """Parse the vetting packets into `derive_owner_queue`'s ParseResult.

    Mirrors the generator's own parse sequence (sorted traversal, same parser) so the
    structured live groups + checkpoints + click groups this guard reasons over are
    exactly what the generator would render — no re-implementation of the queue model.
    Returns (result, n_packets); n_packets == 0 means there is nothing to derive.
    """
    result = gen.ParseResult()
    vdir = Path(root) / VETTING_DIR_REL
    packets = sorted(vdir.glob("*.md")) if vdir.is_dir() else []
    for packet in packets:
        gen.parse_packet(packet, result)
    return result, len(packets)


def check_companion_crossrefs(root=REPO_ROOT):
    """INV-1 — every companion cross-ref resolves to a real queue anchor.

    Returns (applicable, findings). `applicable` is False when either the queue or the
    companion is absent (nothing to cross-check); `findings` is a list of dangling-ref
    strings.
    """
    queue_text = _read(Path(root) / OWNER_QUEUE_REL)
    companion_text = _read(Path(root) / COMPANION_REL)
    if queue_text is None or companion_text is None:
        return False, []

    sections = {int(m.group(1)) for m in QUEUE_SECTION_RE.finditer(queue_text)}
    decisions = {int(m.group(1)) for m in QUEUE_DECISION_RE.finditer(queue_text)}

    findings = []
    # D-refs (including inclusive ranges "D22–D25").
    for match in COMPANION_DREF_RE.finditer(companion_text):
        lo = int(match.group(1))
        hi = int(match.group(2)) if match.group(2) else lo
        for n in range(lo, hi + 1):
            if n not in decisions:
                findings.append(
                    "INV-1 DANGLING-DREF: {c} cites decision D{n} (in '{ref}'), but "
                    "{q} has no `### D{n} —` decision header (renumber drift after a "
                    "regen?)".format(
                        c=COMPANION_REL, n=n, ref=match.group(0), q=OWNER_QUEUE_REL
                    )
                )
    # §-refs, scoped to lines that name OWNER-QUEUE.
    for line in companion_text.splitlines():
        if "OWNER-QUEUE" not in line:
            continue
        for match in COMPANION_SREF_RE.finditer(line):
            n = int(match.group(1))
            if n not in sections:
                findings.append(
                    "INV-1 DANGLING-SECTION: {c} cites {q} §{n}, but the queue has no "
                    "`## {n}.` section header".format(
                        c=COMPANION_REL, q=OWNER_QUEUE_REL, n=n
                    )
                )
    # De-dup while preserving order (a range/section can recur across the doc).
    seen, unique = set(), []
    for f in findings:
        if f not in seen:
            seen.add(f)
            unique.append(f)
    return True, unique


def check_checkpoint_consistency(result):
    """INV-2 — dated checkpoints are well-formed and internally arithmetic-consistent.

    Structure/consistency only — never compares against "today". Returns (applicable,
    findings): applicable is False when no live product carries any checkpoint.
    """
    checkpointed = [g for g in result.live if g.checkpoints]
    if not checkpointed:
        return False, []

    findings = []
    for group in checkpointed:
        parsed = []  # (checkpoint dict, date | None)
        for cp in group.checkpoints:
            try:
                d = datetime.date.fromisoformat(cp["date"])
            except ValueError:
                findings.append(
                    "INV-2 BAD-CHECKPOINT-DATE: [{t}] checkpoint date '{d}' is not a "
                    "well-formed ISO calendar date".format(t=group.title, d=cp["date"])
                )
                d = None
            parsed.append((cp, d))

        # T+<n> arithmetic: for every ordered pair of T+n-labelled checkpoints with
        # valid dates, the calendar-day delta must equal the ordinal (day-offset)
        # delta — a shared-anchor invariant (T+7 → T+14 == +7 days).
        tpoints = []
        for cp, d in parsed:
            m = TPLUS_RE.search(cp["label"])
            if m and d is not None:
                tpoints.append((int(m.group(1)), d, cp["label"]))
        tpoints.sort(key=lambda x: x[0])
        for (n1, d1, l1), (n2, d2, l2) in zip(tpoints, tpoints[1:]):
            day_delta = (d2 - d1).days
            ordinal_delta = n2 - n1
            if day_delta != ordinal_delta:
                findings.append(
                    "INV-2 CHECKPOINT-ARITHMETIC: [{t}] T+{n1} ({d1}) → T+{n2} ({d2}) "
                    "is {dd} calendar day(s) apart, but the T+n offsets differ by {od} "
                    "— a self-contradictory kill clock".format(
                        t=group.title, n1=n1, d1=d1, n2=n2, d2=d2,
                        dd=day_delta, od=ordinal_delta,
                    )
                )
    return True, findings


def check_proofread_gate_integrity(result):
    """INV-3 — every click-run carrying a native-speaker-proofread row is HARD-GATED.

    Reuses the generator's own PROOFREAD_GATE_RE + per-group `blocked` flag. Returns
    (applicable, findings): applicable is False when no click-run carries a proofread
    row.
    """
    gated_groups = [
        g
        for g in result.groups
        if any(gen.PROOFREAD_GATE_RE.search(c["what"]) for c in g.clicks)
    ]
    if not gated_groups:
        return False, []

    findings = []
    for group in gated_groups:
        if not group.blocked:
            findings.append(
                "INV-3 PROOFREAD-GATE-DRIFT: click-run '{t}' carries a "
                "native-speaker-proofread owner row but is NOT rendered HARD-GATED — "
                "it reads as click-ready to publish un-proofread".format(t=group.title)
            )
    return True, findings


def check(root=REPO_ROOT):
    """Run all applicable staleness invariants over the tree at `root`.

    Returns (status, findings):
      * ("ok", [])     — every applicable invariant holds;
      * ("skip", why)  — nothing to check (no packets AND no companion cross-refs);
      * ("stale", [..])— a list of human-readable per-invariant findings.
    """
    result, n_packets = parse_tree(root)

    applicable_any = False
    findings = []

    inv1_applicable, inv1 = check_companion_crossrefs(root)
    applicable_any |= inv1_applicable
    findings.extend(inv1)

    if n_packets:
        inv2_applicable, inv2 = check_checkpoint_consistency(result)
        applicable_any |= inv2_applicable
        findings.extend(inv2)

        inv3_applicable, inv3 = check_proofread_gate_integrity(result)
        applicable_any |= inv3_applicable
        findings.extend(inv3)

    if not applicable_any:
        return "skip", (
            "no packets under {v} and no resolvable companion cross-refs — nothing to "
            "check for staleness".format(v=VETTING_DIR_REL)
        )
    if findings:
        return "stale", findings
    return "ok", []


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        default=REPO_ROOT,
        help="repo root to check (default: the repo this script lives in)",
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="suppress the OK/skip banner on success",
    )
    args = parser.parse_args(argv)

    status, detail = check(args.root)

    if status == "stale":
        print("STALE: docs/publishing/OWNER-QUEUE.md carries a staleness drift.")
        print(
            "One or more staleness invariants failed. These are consistency checks the\n"
            "idempotence guard (ENG-6) cannot catch — a dangling companion cross-ref, a\n"
            "self-contradictory dated checkpoint, or a proofread-gated row that lost its\n"
            "hard-gate. Fix the underlying packet / companion (never hand-edit the\n"
            "generated queue), regenerate with `python3 scripts/derive_owner_queue.py`,\n"
            "and re-run.\n"
        )
        print("--- {n} finding(s) ---".format(n=len(detail)))
        for line in detail:
            print("  * " + line)
        print("FAIL: OWNER-QUEUE.md is stale (an internal consistency invariant broke).")
        return 1

    if status == "skip":
        if not args.quiet:
            print("SKIP: {why}".format(why=detail))
        return 0

    if not args.quiet:
        print(
            "OK: OWNER-QUEUE.md is consistent — companion cross-refs resolve, dated "
            "checkpoints are\nwell-formed and arithmetic-consistent, and every "
            "proofread-gated click-run is hard-gated."
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
