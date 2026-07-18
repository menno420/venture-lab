#!/usr/bin/env python3
"""check_catalog_drefs.py — guard the LIVE decision-ID (D-ref) cross-references.

Why this exists
---------------
`docs/publishing/OWNER-QUEUE.md` §1 is the SOURCE OF TRUTH for decision IDs:
its `### D<n> — <SKU> — <topic>` headers map each decision number to a SKU.
That queue is a GENERATED file (`scripts/derive_owner_queue.py`) and it
RENUMBERS whenever a packet is inserted — e.g. PR #244 folded the CORS
Preflight Test Kit in as a new D4, shifting every alphabetically-later
decision +1 (D4→D5 … D27→D28). When that happens, every `D<n>`
cross-reference in the catalog/bundle docs that was written against the OLD
numbering silently MISPOINTS at the wrong SKU's queue row. `bootstrap.py
check --strict` does NOT catch this — it is a semantic cross-reference, not a
syntax error — so PR #244 shipped green with the bundle docs mispointed, and
PR #245 had to hand-resync them.

This checker makes that regression class MACHINE-CATCHABLE:

  1. Build the live decision-ID -> SKU map from OWNER-QUEUE.md §1 headers.
  2. Scan a well-defined ALLOWLIST of files that carry LIVE cross-references
     and, for each `D<n>` cross-ref, assert:
       - it resolves to an EXISTING decision (else: DANGLING), and
       - when the surrounding context names a SKU, `D<n>` points at THAT
         SKU (else: MISPOINTED).

Scoping is ALLOWLIST-BASED, not deny-all. Frozen point-in-time snapshots
(`.sessions/*` logs, `control/inbox.md` / `control/outbox.md`,
`docs/NEXT-TASKS.md`, `docs/NEXT-SESSION.md`, `docs/current-state.md`'s
"N decisions D1-Dn" line, etc.) are HISTORY — they are deliberately NOT in
the allowlist and must never be flagged. In addition, individual lines that
carry RENUMBER notation (`D4→D5`) or a decision RANGE span (`D1–D28`) are
skipped inside allowlisted files, because those are migration/summary prose,
not per-SKU cross-references.

Exit 0 clean (prints the map + "all N refs resolve"); exit non-zero with a
clear per-ref message on any dangling or mispointed reference. Stdlib-only.
"""

from __future__ import annotations

import argparse
import glob
import os
import re
import sys

# --- repo location -----------------------------------------------------------
# Resolve paths relative to the repo root (this file lives in scripts/), so the
# checker works regardless of the current working directory. Tests override the
# root with --root to point at an in-memory/temp fixture tree.
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

OWNER_QUEUE_REL = "docs/publishing/OWNER-QUEUE.md"

# --- allowlist ---------------------------------------------------------------
# The files that carry LIVE decision-ID cross-references. Glob patterns are
# resolved relative to the repo root. This is the ONLY set of files scanned;
# everything else (history/snapshots) is out of scope by construction.
ALLOWLIST_GLOBS = [
    "docs/launch/CATALOG.md",
    "docs/launch/api-robustness-bundle/*.md",
    "docs/launch/webhook-verifier-bundle/*.md",
    "docs/publishing/vetting/api-robustness-bundle.md",
    "docs/publishing/vetting/webhook-verifier-bundle.md",
    "candidates/api-robustness-bundle/*.md",
    "candidates/api-robustness-bundle/*.json",
    "candidates/webhook-verifier-bundle/*.md",
    "candidates/webhook-verifier-bundle/*.json",
]

# --- keyword derivation ------------------------------------------------------
# Generic product-type / decision-type words carry no SKU identity; dropping
# them leaves each decision with at least one DISTINCTIVE keyword. (Shared
# words like "webhook" or "agent" are fine to keep — a shared keyword only
# WIDENS a ref's candidate set, which can never turn a correct ref into a false
# positive; it can only make a mispoint harder to catch, and the sharp
# per-SKU carriers, e.g. table rows / manifest objects, catch it anyway.)
STOPWORDS = {
    "the", "a", "an", "and", "of", "for", "to", "in", "at", "by", "with",
    "ai", "kit", "kits", "test", "pack", "packs", "cookbook", "guide",
    "site", "boilerplate", "production", "field", "manual", "intake",
    "storefront", "pick", "decision", "title", "subtitle", "coupling",
    "price", "illustration", "category", "map", "new", "component",
}

# A decision-ID token that is a genuine cross-reference. Requires an uppercase
# D not glued to a preceding alphanumeric (so lowercase hex shas like
# "d772b26e" never match) and captures the whole number.
DREF_RE = re.compile(r"(?<![A-Za-z0-9])D(\d+)(?![0-9])")

# Header form in OWNER-QUEUE.md §1: "### D<n> — <SKU> — <topic>"
HEADER_RE = re.compile(r"^###\s+D(\d+)\s+—\s+(.+)$")

# Historical / non-cross-ref line notation to skip inside allowlisted files:
#   renumber arrows  (D4→D5, D15/D16→D16/D17, D21–D27→D22–D28)
#   decision ranges  (D1–D28, "decisions D1-Dn")
RENUMBER_RE = re.compile(r"D\d+\s*(?:→|-+>|=>)\s*D\d+")
RANGE_RE = re.compile(r"D\d+\s*[–—-]\s*D\d+")


def _norm_words(text):
    """Lowercase, collapse every non-alphanumeric run to a space, split.

    Hyphens/punctuation become boundaries, so 'Rate-Limit' -> {rate, limit}
    and 'idempotency-key-test-kit.md' -> {idempotency, key, test, kit, md}.
    """
    return set(re.sub(r"[^a-z0-9]+", " ", text.lower()).split())


def build_decision_map(root=REPO_ROOT):
    """Parse OWNER-QUEUE.md §1 into {id: sku_title}. Source of truth."""
    path = os.path.join(root, OWNER_QUEUE_REL)
    id_to_sku = {}
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            m = HEADER_RE.match(line.rstrip("\n"))
            if not m:
                continue
            num = int(m.group(1))
            # SKU is the segment between the first and second " — ".
            sku = m.group(2).split(" — ", 1)[0].strip()
            id_to_sku[num] = sku
    if not id_to_sku:
        raise SystemExit(
            "check_catalog_drefs: no '### D<n> — <SKU>' headers found in "
            + path
            + " — cannot build the decision map"
        )
    return id_to_sku


def build_keyword_index(id_to_sku):
    """{id: set(distinctive keyword words)} derived from each SKU title."""
    idx = {}
    for num, sku in id_to_sku.items():
        words = {w for w in _norm_words(sku) if len(w) >= 3 and w not in STOPWORDS}
        idx[num] = words
    return idx


def decisions_named_in(context, keyword_index):
    """The set of decision IDs whose SKU keywords appear in `context`."""
    ctx_words = _norm_words(context)
    return {num for num, kws in keyword_index.items() if kws & ctx_words}


def _is_continuation(line):
    """A wrapped continuation line starts with whitespace (indent)."""
    return bool(line) and line[0] in " \t"


def _bq_content(line):
    """A non-empty blockquote line: starts with '>' and has text after it.

    An empty blockquote separator ('>' or '> ') is NOT content, so it ends a
    blockquote paragraph rather than merging two paragraphs together.
    """
    s = line.strip()
    return s.startswith(">") and s.lstrip(">").strip() != ""


def prose_block(lines, i):
    """Logical block for a prose ref: the ref's line plus the continuation
    lines above it. A line absorbs the line above it when the ref line (or the
    current topmost line) is an INDENTED wrap of it, or when both are non-empty
    blockquote lines of the same paragraph (markdown soft-wraps a long
    blockquote/bullet sentence across physical lines, which can split a kit
    name from its `D<n>`). Stops at a non-indented block start, an empty
    blockquote separator, a blank line, or a heading — so it never bleeds
    across a sibling bullet/paragraph. Widening context only adds candidate
    SKUs; it can never turn a correct ref into a false positive."""
    start = i
    steps = 0
    while start > 0 and steps < 8:
        cur = lines[start]
        prev = lines[start - 1]
        if _is_continuation(cur):
            extend = True
        elif _bq_content(cur) and _bq_content(prev):
            extend = True
        else:
            extend = False
        if not extend:
            break
        start -= 1
        steps += 1
    return "\n".join(lines[start : i + 1])


def json_object_context(lines, i):
    """For a JSON ref, the enclosing object: walk back to the nearest '{'."""
    start = i
    steps = 0
    while start > 0 and "{" not in lines[start] and steps < 15:
        start -= 1
        steps += 1
    return "\n".join(lines[start : i + 1])


def context_for_ref(lines, i, is_json):
    line = lines[i]
    if is_json:
        return json_object_context(lines, i)
    if line.lstrip().startswith("|"):
        # Markdown table row: self-contained, single-line context.
        return line
    return prose_block(lines, i)


def iter_allowlisted_files(root=REPO_ROOT):
    seen = set()
    files = []
    for pattern in ALLOWLIST_GLOBS:
        for path in sorted(glob.glob(os.path.join(root, pattern))):
            if path not in seen and os.path.isfile(path):
                seen.add(path)
                files.append(path)
    return files


def scan(root=REPO_ROOT):
    """Scan the allowlist. Returns (errors, ref_count, files_scanned).

    `errors` is a list of human-readable strings; empty means clean.
    """
    id_to_sku = build_decision_map(root)
    keyword_index = build_keyword_index(id_to_sku)

    errors = []
    ref_count = 0
    files = iter_allowlisted_files(root)

    for path in files:
        rel = os.path.relpath(path, root)
        is_json = path.endswith(".json")
        with open(path, encoding="utf-8") as fh:
            lines = fh.read().split("\n")
        for i, line in enumerate(lines):
            # Skip historical / non-cross-ref notation lines.
            if RENUMBER_RE.search(line) or RANGE_RE.search(line):
                continue
            for m in DREF_RE.finditer(line):
                num = int(m.group(1))
                ref_count += 1
                if num not in id_to_sku:
                    errors.append(
                        "DANGLING  {rel}:{ln}  D{n} does not exist in "
                        "OWNER-QUEUE.md (queue has D1..D{max}) -- line: {txt}".format(
                            rel=rel,
                            ln=i + 1,
                            n=num,
                            max=max(id_to_sku),
                            txt=line.strip(),
                        )
                    )
                    continue
                ctx = context_for_ref(lines, i, is_json)
                named = decisions_named_in(ctx, keyword_index)
                if named and num not in named:
                    named_desc = ", ".join(
                        'D{k} "{s}"'.format(k=k, s=id_to_sku[k])
                        for k in sorted(named)
                    )
                    errors.append(
                        'MISPOINTED  {rel}:{ln}  D{n} resolves to "{sku}", but '
                        "the surrounding context names {named} -- line: {txt}".format(
                            rel=rel,
                            ln=i + 1,
                            n=num,
                            sku=id_to_sku[num],
                            named=named_desc,
                            txt=line.strip(),
                        )
                    )
    return errors, ref_count, files


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        default=REPO_ROOT,
        help="repo root to scan (default: the repo this script lives in)",
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="suppress the decision-map printout on success",
    )
    args = parser.parse_args(argv)

    id_to_sku = build_decision_map(args.root)
    if not args.quiet:
        print(
            "OWNER-QUEUE decision -> SKU map ({n} decisions):".format(
                n=len(id_to_sku)
            )
        )
        for num in sorted(id_to_sku):
            print("  D{n:<3} -> {sku}".format(n=num, sku=id_to_sku[num]))
        print("")

    errors, ref_count, files = scan(args.root)

    print("Scanned {n} allowlisted file(s).".format(n=len(files)))
    if errors:
        print("")
        for err in errors:
            print("  " + err)
        dangling = sum(1 for e in errors if e.startswith("DANGLING"))
        mispointed = sum(1 for e in errors if e.startswith("MISPOINTED"))
        print("")
        print(
            "FAIL: {d} dangling, {m} mispointed of {r} cross-ref D-ref(s).".format(
                d=dangling, m=mispointed, r=ref_count
            )
        )
        return 1

    print(
        "all {r} cross-ref D-ref(s) resolve (0 dangling, 0 mispointed).".format(
            r=ref_count
        )
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
