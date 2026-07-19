#!/usr/bin/env python3
"""check_docs_links.py — internal doc LINK + ANCHOR integrity guard (ENG-8).

Why this exists
---------------
`bootstrap.py` already ships a generic doc-hygiene gate (`engine/checks/check_docs.py`,
run by `python3 bootstrap.py check --strict`) that, **over `docs/` only**, enforces
three checks: **badge** (`> **Status:**` on every non-ADR doc), **link** (every
relative markdown link resolves to an existing file), and **reachable** (orphan: every
live doc reachable from a read-path root / README). That gate is the roadmap's OPS-6
"dead-link + orphan" idea for `docs/`, and it is green on this tree.

ENG-8 (= OPS-5 + OPS-6, `docs/ideas/2026-07-19-execution-roadmap.md` line 83) is scoped
to the GAP that gate leaves — deliberately, so this guard NEVER duplicates it:

INV-1 — DEAD LINK in the UN-GATED living-doc set.
    The bootstrap gate only walks `docs/`. The repo-root docs (`README.md`,
    `CONSTITUTION.md`, `.session-journal.md`) and the control-plane docs
    (`control/**/*.md`) — exactly the surface a fresh seat boots from — are
    link-checked by NOTHING today. INV-1 asserts every relative markdown link in that
    un-gated set resolves to an existing file (external `http(s)`/`mailto`/`tel` links
    and pure anchors are out of scope — INV-2 owns anchors). `docs/` is NOT re-checked
    for link existence here; that is the bootstrap gate's job.

INV-2 — ANCHOR-FRAGMENT resolution (the dimension the docs-gate STRIPS).
    The bootstrap gate normalises every link target with `.split("#", 1)[0]` — it
    throws the `#anchor` away and never verifies it. So a link that points at the
    right FILE but a since-moved/renamed heading passes the gate silently. INV-2
    closes that: for every markdown link carrying a `#anchor` into an existing
    markdown file — across repo-root + `control/` **and** `docs/` — the fragment must
    resolve to a real heading, matched by the GitHub-style slug convention
    (lowercase, punctuation dropped, spaces → hyphens, duplicate headings
    disambiguated with `-1`, `-2`, …, fenced-code blocks skipped). `docs/` is in scope
    for anchors ONLY; its link-existence + orphan checks stay owned by the bootstrap
    gate, so there is zero overlap.

OPS-5's other half — "flag stamped docs lagging main HEAD" (freshness by git/date) — is
intentionally NOT implemented: it needs the git log / wall clock, and wall-clock- and
network-dependent checks are banned in this repo for determinism. This guard is the
deterministic, offline slice of ENG-8.

Scope / exclusions (documented)
-------------------------------
In-scope markdown = tracked `*.md` under repo-root + `control/` + `docs/`. Excluded,
each for a stated reason:
  * `.sessions/`   — immutable point-in-time session cards (append-only history; they
                     legitimately cite files later moved/renamed).
  * `candidates/`  — generated kit / template packs whose relative links resolve in the
                     GENERATED kit layout, not this repo.
  * `.substrate/`  — machine-generated telemetry JSONL, not prose docs.
Orphan/reachability is deliberately NOT re-implemented: already gated for `docs/`, and
root/`control/` have no README-graph reachability convention to gate.

Exit 0 when every in-scope link + anchor resolves (or there is nothing to check); exit
non-zero with an itemized per-finding list otherwise. Stdlib-only. No network, no wall
clock. Never writes the tree.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

# Resolve paths relative to the repo root (this file lives in scripts/), so the guard
# works regardless of the current working directory. Tests override the root with
# --root to point at a temp fixture tree.
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Top-level directories whose markdown is NOT in scope (see the module docstring for
# the per-exclusion reasons). A file is excluded when its FIRST path component (relative
# to the repo root) is in this set.
EXCLUDED_TOP = frozenset({".sessions", "candidates", ".substrate"})

# The docs root the BOOTSTRAP gate already link-checks. Files under it are anchor-checked
# (INV-2 — the gate strips fragments) but NOT link-existence-checked here (INV-1), so the
# two guards never overlap.
DOCS_GATE_ROOT = "docs"

# Markdown inline link: [text](target).
_MD_LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
# ATX heading: one-to-six `#` then the heading text.
_HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")
# A fenced-code delimiter (``` or ~~~), possibly indented / with an info string.
_FENCE_RE = re.compile(r"^\s*(```+|~~~+)")
# Link schemes that are external / non-file — never a repo-relative target.
_EXTERNAL_PREFIXES = ("http://", "https://", "mailto:", "tel:", "ftp://")


def _split_target(raw: str) -> tuple[str, str]:
    """Split a raw markdown link target into (path, anchor).

    Mirrors the bootstrap gate's normalisation (drop ``<>`` wrappers and a trailing
    ``"title"``, keep the first whitespace-delimited token) but PRESERVES the
    ``#anchor`` fragment instead of discarding it, since anchor resolution is this
    guard's whole point. ``anchor`` is returned without its leading ``#`` (empty when
    absent).
    """
    target = raw.strip()
    if target.startswith("<") and ">" in target:
        target = target[1:].split(">", 1)[0]
    parts = target.split()
    target = parts[0] if parts else target
    path, _, anchor = target.partition("#")
    return path, anchor


def slugify(text: str) -> str:
    """Return the GitHub-style anchor slug for a heading's text.

    The convention GitHub's autolinker uses: lowercase, drop every character that is
    not a word char / whitespace / hyphen, then collapse whitespace runs to single
    hyphens. Duplicate-heading disambiguation (``-1``, ``-2``) is applied by the caller
    (`heading_slugs`), which sees the whole document.
    """
    text = text.strip().lower()
    text = re.sub(r"[^\w\s-]", "", text)
    return re.sub(r"\s+", "-", text).strip("-")


def heading_slugs(path: Path) -> set[str]:
    """Return the set of anchor slugs a markdown file exposes.

    Skips fenced-code blocks (a ``#`` inside a code fence is not a heading), and
    disambiguates repeated slugs the way GitHub does — the second ``## Notes`` becomes
    ``notes-1``, the third ``notes-2``. An unreadable / non-UTF-8 file exposes no slugs
    (its links are simply unverifiable, not a crash).
    """
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeDecodeError):
        return set()
    slugs: set[str] = set()
    counts: dict[str, int] = {}
    in_fence = False
    for line in lines:
        if _FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        match = _HEADING_RE.match(line)
        if not match:
            continue
        base = slugify(match.group(2))
        if not base:
            continue
        seen = counts.get(base, 0)
        slugs.add(base if seen == 0 else "{b}-{n}".format(b=base, n=seen))
        counts[base] = seen + 1
    return slugs


def _rel_top(path: Path, root: Path) -> str:
    """Return the first path component of ``path`` relative to ``root`` (``""`` if at
    the root itself)."""
    rel = path.relative_to(root).parts
    return rel[0] if len(rel) > 1 else ""


def scope_files(root: Path) -> list[Path]:
    """Every in-scope ``*.md`` under ``root`` (sorted, excluded tops removed)."""
    if not root.exists():
        return []
    out = []
    for path in sorted(root.rglob("*.md")):
        if _rel_top(path, root) in EXCLUDED_TOP:
            continue
        out.append(path)
    return out


def _is_under_docs_gate(path: Path, root: Path) -> bool:
    """True when ``path`` lives under the bootstrap-gated ``docs/`` root."""
    return _rel_top(path, root) == DOCS_GATE_ROOT


def check(root=REPO_ROOT):
    """Run INV-1 (dead link) + INV-2 (anchor) over the tree at ``root``.

    Returns ``(status, findings, stats)``:
      * ``("ok", [], stats)``     — every in-scope link + anchor resolves;
      * ``("skip", why, stats)``  — no in-scope markdown at all (nothing to check);
      * ``("broken", [..], stats)`` — an itemized list of per-finding strings.
    ``stats`` is ``{"files": n, "links_checked": n, "anchors_checked": n}`` — the test
    suite asserts the live run was non-vacuous (each dimension actually exercised).
    """
    root_path = Path(root)
    files = scope_files(root_path)
    stats = {"files": len(files), "links_checked": 0, "anchors_checked": 0}
    if not files:
        return "skip", "no in-scope markdown under {r} — nothing to check".format(r=root), stats

    # Cache each target file's slug set — a hub doc linked from many places is read once.
    slug_cache: dict[Path, set[str]] = {}

    def slugs_for(target: Path) -> set[str]:
        resolved = target.resolve()
        if resolved not in slug_cache:
            slug_cache[resolved] = heading_slugs(target)
        return slug_cache[resolved]

    findings: list[str] = []
    for path in files:
        under_docs = _is_under_docs_gate(path, root_path)
        rel = path.relative_to(root_path).as_posix()
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except (OSError, UnicodeDecodeError) as exc:
            findings.append("{r}: unreadable as UTF-8: {e}".format(r=rel, e=exc))
            continue
        for lineno, line in enumerate(lines, 1):
            for raw in _MD_LINK_RE.findall(line):
                stripped = raw.strip()
                if stripped.startswith(_EXTERNAL_PREFIXES):
                    continue
                link_path, anchor = _split_target(raw)

                if not link_path:
                    # Same-file anchor link, e.g. [§2](#section). Always in scope for
                    # INV-2 (the file itself is the target and always exists).
                    if not anchor:
                        continue
                    stats["anchors_checked"] += 1
                    if slugify(anchor) not in slugs_for(path):
                        findings.append(
                            "{r}:L{n}: INV-2 DEAD-ANCHOR -> {raw} (no heading in this "
                            "file slugs to `{a}`)".format(
                                r=rel, n=lineno, raw=raw, a=slugify(anchor)
                            )
                        )
                    continue

                if link_path.startswith(_EXTERNAL_PREFIXES):
                    continue
                target = (path.parent / link_path).resolve()
                exists = target.exists()

                # INV-1 — dead link, but ONLY for the un-gated set (docs/ link
                # existence is owned by the bootstrap gate — no duplication).
                if not under_docs:
                    stats["links_checked"] += 1
                    if not exists:
                        findings.append(
                            "{r}:L{n}: INV-1 DEAD-LINK -> {raw} (target does not "
                            "exist)".format(r=rel, n=lineno, raw=raw)
                        )
                        continue  # can't check an anchor into a missing file

                # INV-2 — anchor into an existing markdown file (any in-scope source,
                # including docs/). A missing docs/ target is left for the bootstrap
                # gate to red; we simply cannot verify its anchor.
                if anchor and exists and target.suffix == ".md":
                    stats["anchors_checked"] += 1
                    if slugify(anchor) not in slugs_for(target):
                        findings.append(
                            "{r}:L{n}: INV-2 DEAD-ANCHOR -> {raw} (target `{t}` has no "
                            "heading slugging to `{a}`)".format(
                                r=rel, n=lineno, raw=raw,
                                t=target.relative_to(root_path).as_posix()
                                if _is_within(target, root_path) else link_path,
                                a=slugify(anchor),
                            )
                        )

    if findings:
        return "broken", findings, stats
    return "ok", [], stats


def _is_within(path: Path, root: Path) -> bool:
    """True when ``path`` is inside ``root`` (for pretty relative reporting)."""
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


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

    status, detail, stats = check(args.root)

    if status == "broken":
        print("BROKEN: an internal doc link or anchor does not resolve.")
        print(
            "INV-1 (dead link in the un-gated root/control docs) and/or INV-2 (a\n"
            "`#anchor` pointing at a heading that no longer exists) failed. These are\n"
            "the gap the bootstrap docs-gate leaves — it link-checks only `docs/` and\n"
            "strips every `#anchor`. Fix the link to point at the real file / heading\n"
            "(never invent a target to satisfy it), then re-run.\n"
        )
        print("--- {n} finding(s) ---".format(n=len(detail)))
        for line in detail:
            print("  * " + line)
        print(
            "FAIL: {f} in-scope doc(s), {li} link(s) + {an} anchor(s) checked — see "
            "above.".format(f=stats["files"], li=stats["links_checked"], an=stats["anchors_checked"])
        )
        return 1

    if status == "skip":
        if not args.quiet:
            print("SKIP: {why}".format(why=detail))
        return 0

    if not args.quiet:
        print(
            "OK: every in-scope internal doc link + anchor resolves — {f} doc(s), "
            "{li} link(s) + {an} anchor(s) checked (root + control/ links, and "
            "anchors across root + control/ + docs/).".format(
                f=stats["files"], li=stats["links_checked"], an=stats["anchors_checked"]
            )
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
