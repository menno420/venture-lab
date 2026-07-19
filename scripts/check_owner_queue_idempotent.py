#!/usr/bin/env python3
"""check_owner_queue_idempotent.py — guard the generated OWNER-QUEUE's idempotence.

Why this exists
---------------
`docs/publishing/OWNER-QUEUE.md` is a GENERATED file: `scripts/derive_owner_queue.py`
derives it from the §7 ⚑ OWNER-GATE blocks of `docs/publishing/vetting/*.md` plus
the ⚑ OWNER-flagged conflicts in `docs/publishing/keyword-map.md`. The derive
script is deterministic — sorted traversal, no timestamps — so a correct tree is
IDEMPOTENT: regenerating the queue produces byte-identical output.

Two regression classes break that idempotence, and neither is caught elsewhere:

  1. A HAND-EDIT to the generated file. The queue header says "edit packets, not
     this file", but nothing enforces it — a hand-edit to a `### D<n> — <SKU>`
     header silently rewrites the decision-ID → SKU map that `check_catalog_drefs.py`
     (ENG-2, #248) treats as SOURCE OF TRUTH, so the D-ref guard would then
     validate every cross-reference against a hand-corrupted map.
  2. An INPUT DRIFT without a regen. A vetting packet or the keyword map changes
     (a title, a default, a new ⚑ decision) but OWNER-QUEUE.md is not regenerated,
     so the committed queue no longer reflects its own inputs — a stale copy,
     which the derive script's own docstring calls "a bug in the workflow".

ENG-2 (#248) catches a mispoint AFTER a regen introduces it. This guard catches
the class that CAUSES the mispoint — it prevents a regen (or a hand-edit) from
silently reintroducing the #244/#245 renumber-mispoint by pinning the invariant
the whole D-ref safety story rests on:

    the committed OWNER-QUEUE.md == derive_owner_queue.render(current inputs)

The guard imports `derive_owner_queue` and drives its OWN parser + `render`
against the live tree — no re-implementation of the queue format, so the check
can never drift from the generator it guards. Exit 0 when the committed file is
byte-identical to a fresh regeneration; exit non-zero with a unified-diff summary
when it is not (someone hand-edited the generated file, or an input drifted
without regenerating). Stdlib-only. Never writes the tree.
"""

from __future__ import annotations

import argparse
import difflib
import os
import sys
from pathlib import Path

import derive_owner_queue as gen

# Resolve paths relative to the repo root (this file lives in scripts/), so the
# guard works regardless of the current working directory. Tests override the
# root with --root to point at a temp fixture tree.
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# The generated file and its inputs, as repo-relative paths. The derive script's
# defaults ARE the ground truth here — reusing its constants keeps the guard and
# the generator pointed at the same files by construction.
VETTING_DIR_REL = gen.DEFAULT_VETTING_DIR       # docs/publishing/vetting
KEYWORD_MAP_REL = gen.DEFAULT_KEYWORD_MAP       # docs/publishing/keyword-map.md
OWNER_QUEUE_REL = gen.DEFAULT_OUTPUT            # docs/publishing/OWNER-QUEUE.md


def regenerate(root=REPO_ROOT):
    """The queue content the generator WOULD write for the tree under `root`.

    Mirrors `derive_owner_queue.run()`'s parse sequence exactly, but calls
    `render()` in-memory instead of writing the file, and passes the
    repo-relative vetting-dir STRING to `render` (not the on-disk path) so the
    rendered header matches what a real `derive_owner_queue.py` run on a checkout
    produces. Returns (content, n_packets); n_packets == 0 means the generator
    would have skipped (no packets), in which case there is nothing to compare.
    """
    result = gen.ParseResult()
    vdir = Path(root) / VETTING_DIR_REL
    packets = sorted(vdir.glob("*.md")) if vdir.is_dir() else []
    for packet in packets:
        gen.parse_packet(packet, result)
    kmap = Path(root) / KEYWORD_MAP_REL
    if kmap.is_file():
        gen.parse_keyword_map(kmap, result)
    return gen.render(result, VETTING_DIR_REL), len(packets)


def check(root=REPO_ROOT):
    """Compare committed OWNER-QUEUE.md to a fresh regeneration.

    Returns (status, detail):
      * ("ok", <n refs summary>)     — byte-identical (idempotent), or
      * ("skip", <why>)              — no packets / queue absent (nothing to pin), or
      * ("drift", <unified diff>)    — the committed file is not idempotent.
    """
    expected, n_packets = regenerate(root)
    if n_packets == 0:
        return "skip", (
            "no vetting packets under {d} — the generator would skip, so there "
            "is nothing to pin".format(d=VETTING_DIR_REL)
        )
    queue_path = Path(root) / OWNER_QUEUE_REL
    if not queue_path.is_file():
        return "skip", "{f} does not exist — nothing to compare".format(f=OWNER_QUEUE_REL)
    committed = queue_path.read_text(encoding="utf-8")
    if committed == expected:
        return "ok", None
    diff = "".join(
        difflib.unified_diff(
            committed.splitlines(keepends=True),
            expected.splitlines(keepends=True),
            fromfile="committed  " + OWNER_QUEUE_REL,
            tofile="regenerated (derive_owner_queue.py over current inputs)",
        )
    )
    return "drift", diff


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

    if status == "drift":
        print(
            "DRIFT: {f} is NOT idempotent under scripts/derive_owner_queue.py.".format(
                f=OWNER_QUEUE_REL
            )
        )
        print(
            "The committed generated file differs from a fresh regeneration over "
            "the current inputs\n(docs/publishing/vetting/*.md + keyword-map.md). "
            "Either the generated file was hand-edited,\nor an input packet drifted "
            "without regenerating. Fix by running:\n"
            "    python3 scripts/derive_owner_queue.py\n"
            "and committing the regenerated {f} (edit packets, never this file).\n".format(
                f=OWNER_QUEUE_REL
            )
        )
        print("--- committed vs. regenerated (unified diff) ---")
        print(detail if detail.strip() else "(no textual diff — check trailing bytes)")
        print("FAIL: OWNER-QUEUE.md is stale / hand-edited (not idempotent).")
        return 1

    if status == "skip":
        if not args.quiet:
            print("SKIP: {why}".format(why=detail))
        return 0

    if not args.quiet:
        print(
            "OK: {f} is byte-identical to a fresh regeneration — idempotent under "
            "scripts/derive_owner_queue.py.".format(f=OWNER_QUEUE_REL)
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
