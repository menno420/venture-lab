#!/usr/bin/env python3
"""check_funnel_coverage.py — ADVISORY per-cluster funnel-top coverage checker.

Why this exists
---------------
`docs/launch/CATALOG.md` §"Cross-sell clusters" is where each product cluster
(Webhook / API-robustness / Membership / Agent-ops …) is listed as a
singles/bundle "you may also like" chain. A cluster converts best when it has a
top-of-funnel FREE discovery asset — a `docs/launch/<cluster>-lead-magnet.md`
article (the funnel-top) that teaches the shared pain and funnels into the
cluster's bundles/singles. Those magnets are what PRs #243 / #246 / #250 / #251
shipped one cluster at a time.

Until now, "which cross-sell cluster still needs a lead magnet?" was a MANUAL
CATALOG read: scan the section by eye, cross-check the `*-lead-magnet.md` files,
and notice the gap. `bootstrap.py check --strict` does not surface it — a
missing funnel-top is a coverage gap, not a syntax error. This checker turns
that question into a standing greppable signal: it parses the Cross-sell
clusters section, cross-references the `docs/launch/*-lead-magnet.md` files, and
warns on any cluster with a singles/bundle list but NO linked funnel-top.

Coverage model (grounded in the ACTUAL CATALOG content, no hardcoded clusters):

  * A CLUSTER is a `- **<Name> cluster:**` bullet in the section that carries a
    singles/bundle list (an arrow-joined SKU chain: → / ↔ / ->).
  * A cluster is COVERED when its distinctive keywords overlap a COVERAGE
    SOURCE, either of:
      - a Cross-sell bullet that LINKS a `*-lead-magnet.md` funnel-top (the
        section's own "Dev-cluster funnel-top" / "Agent-ops-cluster funnel-top"
        rows carry the link + the prose that names which clusters they serve),
        or
      - an existing `docs/launch/*-lead-magnet.md` FILE (its slug + H1) — so the
        membership + AI-Novella gaps that LM-1/LM-2 (#250/#251) filled read as
        covered the moment the file exists.
  * Keyword overlap mirrors the D-ref guard's (`check_catalog_drefs.py`) idiom:
    generic words are dropped so each cluster keeps a DISTINCTIVE carrier
    (webhook / api+robustness / membership / agent+ops). Overlap only ever
    WIDENS coverage, so it never false-warns a genuinely-covered cluster.

Posture: **ADVISORY ONLY — this script exits 0 on EVERY path** (covered,
uncovered, or a parse/skip). It must never be wired as a required gate; the same
contract as `check_ledger_drift.py` / `lint_owner_gates.py`. An uncovered
cluster is a nudge ("next magnet target"), never a locked door — it must not
exit-fail another in-flight PR's substrate/kit gate. Stdlib-only.
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
# root with --root to point at a temp fixture tree.
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CATALOG_REL = "docs/launch/CATALOG.md"
LEAD_MAGNET_GLOB = "docs/launch/*-lead-magnet.md"

# The bold paragraph label that opens the cross-sell clusters block. The section
# runs from this line to the next horizontal rule (`---`) or `## ` heading.
SECTION_MARKER = "cross-sell clusters"

# --- keyword derivation ------------------------------------------------------
# Generic cluster/funnel/product-type words carry no cluster IDENTITY; dropping
# them leaves each cluster with at least one DISTINCTIVE keyword (webhook,
# api+robustness, membership, agent+ops). Shared words only WIDEN a cluster's
# coverage candidates, which can never turn a covered cluster into a false warn.
STOPWORDS = {
    "the", "a", "an", "and", "of", "for", "to", "in", "at", "by", "with", "or",
    "its", "into", "you", "may", "also", "like", "any", "other", "all", "each",
    "cluster", "clusters", "funnel", "top", "free", "discovery", "asset",
    "assets", "lead", "magnet", "article", "storefront", "cross", "sell",
    "bundle", "bundles", "single", "singles", "kit", "kits", "test", "pack",
    "packs", "cookbook", "guide", "map", "pick", "first", "then", "new", "one",
    "two", "three", "four", "reinforce", "reinforces", "supporting", "trap",
    "false", "green", "md",
}

# A cluster bullet's bold label: "- **<Name> cluster:**" (case-insensitive on
# the word "cluster"). Requires a space before "cluster" so the funnel-top rows
# ("Dev-cluster funnel-top …", "Agent-ops-cluster funnel-top …") — where
# "cluster" is glued to the name and followed by "funnel-top", not ":" — are NOT
# picked up as clusters-to-check (they are coverage SOURCES instead).
CLUSTER_LABEL_RE = re.compile(r"\*\*\s*(.+?)\s+cluster:\*\*", re.IGNORECASE)

# A markdown/inline reference to a lead-magnet funnel-top file.
LEAD_MAGNET_REF_RE = re.compile(r"[A-Za-z0-9_-]*-lead-magnet\.md")

# An arrow-joined SKU chain marks a "singles/bundle list".
LIST_ARROW_RE = re.compile(r"→|↔|->|—>")

# H1 of a markdown file: the first "# " heading.
H1_RE = re.compile(r"^#\s+(.*)$")


def _norm_words(text):
    """Lowercase, collapse every non-alphanumeric run to a space, split."""
    return set(re.sub(r"[^a-z0-9]+", " ", text.lower()).split())


def _keywords(text):
    """Distinctive keyword set: len>=3, not a stopword."""
    return {w for w in _norm_words(text) if len(w) >= 3 and w not in STOPWORDS}


def _read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def extract_section(catalog_text):
    """Return the Cross-sell clusters section's lines (marker excluded).

    The section runs from the `**Cross-sell clusters …**` label to the next
    horizontal rule (`---`) or `## ` heading (or EOF). Returns [] if absent.
    """
    lines = catalog_text.split("\n")
    start = None
    for i, line in enumerate(lines):
        if SECTION_MARKER in line.lower() and line.lstrip().startswith("**"):
            start = i + 1
            break
    if start is None:
        return []
    out = []
    for line in lines[start:]:
        stripped = line.strip()
        if stripped == "---" or stripped.startswith("## "):
            break
        out.append(line)
    return out


def group_bullets(section_lines):
    """Group section lines into top-level bullets.

    A bullet starts at a `- ` line; following non-bullet lines (continuations,
    indented wraps) are folded into it. Returns a list of bullet text blocks.
    """
    bullets = []
    current = None
    for line in section_lines:
        if re.match(r"^\s*-\s", line):
            if current is not None:
                bullets.append("\n".join(current))
            current = [line]
        elif current is not None:
            if line.strip() == "":
                bullets.append("\n".join(current))
                current = None
            else:
                current.append(line)
    if current is not None:
        bullets.append("\n".join(current))
    return bullets


def coverage_sources(section_bullets, root=REPO_ROOT):
    """Build the list of coverage sources: (label, keyword_set).

    Two kinds:
      * every Cross-sell bullet that LINKS a `*-lead-magnet.md` (keywords from
        the whole bullet's prose — this is where the section declares which
        clusters a funnel-top serves), and
      * every `docs/launch/*-lead-magnet.md` FILE (keywords from its slug + H1).
    """
    sources = []

    for bullet in section_bullets:
        if LEAD_MAGNET_REF_RE.search(bullet):
            refs = ", ".join(sorted(set(LEAD_MAGNET_REF_RE.findall(bullet))))
            sources.append(("section funnel-top row → " + refs, _keywords(bullet)))

    for path in sorted(glob.glob(os.path.join(root, LEAD_MAGNET_GLOB))):
        if not os.path.isfile(path):
            continue
        base = os.path.basename(path)
        slug = base[: -len("-lead-magnet.md")]
        h1 = ""
        for line in _read(path).split("\n"):
            m = H1_RE.match(line)
            if m:
                h1 = m.group(1)
                break
        sources.append((base, _keywords(slug + " " + h1)))

    return sources


def find_clusters(section_bullets):
    """Return [(name, keyword_set)] for cluster bullets carrying a SKU list."""
    clusters = []
    for bullet in section_bullets:
        first_line = bullet.split("\n", 1)[0]
        m = CLUSTER_LABEL_RE.search(first_line)
        if not m:
            continue
        if not LIST_ARROW_RE.search(bullet):
            # A `**X cluster:**` label with no singles/bundle list is not a
            # coverage target — the pitch scopes this to clusters that list SKUs.
            continue
        name = m.group(1).strip()
        clusters.append((name, _keywords(name)))
    return clusters


def evaluate(root=REPO_ROOT):
    """Return (results, note).

    `results` is a list of (name, covered_by_or_None); `note` is a skip reason
    string when the CATALOG/section could not be read, else "".
    """
    path = os.path.join(root, CATALOG_REL)
    if not os.path.isfile(path):
        return [], "CATALOG.md not found at " + CATALOG_REL
    section_lines = extract_section(_read(path))
    if not section_lines:
        return [], "no '" + SECTION_MARKER + "' section found in " + CATALOG_REL
    bullets = group_bullets(section_lines)
    sources = coverage_sources(bullets, root)
    clusters = find_clusters(bullets)

    results = []
    for name, kws in clusters:
        covered_by = None
        for label, src_kws in sources:
            if kws & src_kws:
                covered_by = label
                break
        results.append((name, covered_by))
    return results, ""


def run(root=REPO_ROOT):
    """Print the advisory. ALWAYS returns exit code 0."""
    results, note = evaluate(root)

    if note:
        print("funnel-coverage: skipped — " + note)
        return 0

    if not results:
        print("funnel-coverage: no cross-sell clusters with a SKU list found")
        return 0

    covered = [(n, by) for (n, by) in results if by is not None]
    uncovered = [n for (n, by) in results if by is None]

    print(
        "funnel-coverage: {t} cross-sell cluster(s), {c} covered, {u} "
        "uncovered".format(t=len(results), c=len(covered), u=len(uncovered))
    )
    for name, by in results:
        if by is None:
            print(
                "  UNCOVERED  {name} cluster — no linked *-lead-magnet.md "
                "funnel-top (next magnet target)".format(name=name)
            )
        else:
            print(
                "  COVERED    {name} cluster — funnel-top: {by}".format(
                    name=name, by=by
                )
            )
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="check_funnel_coverage",
        description="ADVISORY per-cluster funnel-top coverage check — always "
        "exits 0.",
    )
    parser.add_argument(
        "--root",
        default=REPO_ROOT,
        help="repo root to scan (default: the repo this script lives in)",
    )
    args = parser.parse_args(argv)
    return run(args.root)


if __name__ == "__main__":
    sys.exit(main())
