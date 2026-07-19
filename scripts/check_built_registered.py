#!/usr/bin/env python3
"""check_built_registered.py — guard against storefront inventory/registry drift (ENG-5).

Why this exists
---------------
A SKU in this repo lives in THREE independent places, and nothing yet asserts
they agree:

  1. BUILT on disk       — `candidates/<sku>/` packaged to a shippable artifact
                           (a `dist/` directory: the crisp "this candidate reached
                           a sellable, packaged state" marker that separates a real
                           product from a book-lane / WIP-intake / notes candidate
                           dir, none of which carry a `dist/`).
  2. LAUNCH-REGISTERED   — `docs/launch/<sku>/` exists (the per-SKU owner launch
                           registry: `listing-copy.md` + `owner-actions.md`, the
                           surface `OWNER-START-HERE` / OWNER-LAUNCH-HOUR turn into
                           owner publish clicks).
  3. QUEUE-REGISTERED    — `docs/publishing/vetting/<sku>.md` exists (the vetting
                           packet the OWNER-QUEUE is generated from) AND
                           the sku is referenced in `docs/launch/CATALOG.md`
                           (the storefront positioning / comparison view).

Two drift classes break the owner's click path, and neither is caught elsewhere:

  A. BUILT-BUT-UNREGISTERED — a kit is built and packaged (`candidates/<sku>/dist/`)
     but never registered for launch / never given a vetting packet / never added
     to the catalog. It is finished inventory that no owner step will ever surface
     — a strand. This is the headline case in the ENG-5 spec ("built a SKU but
     never registered it in the storefront").

  B. REGISTERED-BUT-MISSING-ARTIFACT — a `docs/launch/<sku>/` launch row (or a
     catalog row) exists but its build artifacts, vetting packet, or catalog row
     are missing. An owner who clicks that publish step would hit a dead link or
     ship an incomplete product.

ENG-2 (`check_catalog_drefs.py`, #248) and ENG-6 (`check_owner_queue_idempotent.py`,
#261) guard the *internal consistency of the generated queue*. This guard sits one
level up: it guards the *inventory-to-registry* correspondence, so a newly built
kit can't ship as invisible inventory and a newly registered launch row can't ship
without its product.

Known-current-state exemptions (deliberate, not drift)
------------------------------------------------------
Two launch rows do not carry a `candidates/<sku>/dist/` build, and this is
intentional per the repo's own docs — so the guard's baseline tolerates them
explicitly (a comment, not silent skipping) and reports FUTURE drift truthfully:

  * `bundle-starter` — a compositional bundle-listing scaffold, not a standalone
    product; it composes other SKUs and has no `candidates/` build dir of its own.
    (The two *shippable* bundles, `api-robustness-bundle` and
    `webhook-verifier-bundle`, DO carry `candidates/<sku>/dist/` and are checked
    normally.) See BUNDLE_TEMPLATES below.
  * `photo-packs` — an owner-gated lane deliberately EXCLUDED from the storefront
    catalog: `docs/launch/CATALOG.md` states "Out of scope here (separate lanes,
    each hard-gated on owner-only work): the Photo Packs and the KDP book catalog".
    It has a launch dir + vetting packet but is intentionally not packaged and not
    in the catalog. See OWNER_GATED_LANES below.

Adding a catalog row or a build dir for either would be inventing artifacts that
contradict the repo's own scoping — so they are allowlisted with the reason, not
papered over. The guard flags any OTHER built-but-unregistered or
registered-but-missing item.

Exit 0 when every built SKU is registered and every registered SKU has its
artifacts (or is a documented exemption); exit non-zero with an itemized report
otherwise. Stdlib-only. Never writes the tree.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

# Resolve paths relative to the repo root (this file lives in scripts/), so the
# guard works regardless of the current working directory. Tests override the
# root with --root to point at a temp fixture tree.
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Repo-relative registry locations.
CANDIDATES_DIR_REL = "candidates"                 # candidates/<sku>/ build dirs
LAUNCH_DIR_REL = "docs/launch"                    # docs/launch/<sku>/ launch registry
VETTING_DIR_REL = "docs/publishing/vetting"       # docs/publishing/vetting/<sku>.md packets
CATALOG_REL = "docs/launch/CATALOG.md"            # storefront positioning view

# A candidate counts as BUILT (packaged to a shippable artifact) when it carries
# this subdirectory. It is the marker that separates a real, packaged product from
# an idea/WIP/book-lane candidate dir (books, intake-only stubs → no dist/).
BUILD_MARKER = "dist"

# Compositional bundle scaffolds with NO standalone candidates/<sku>/ build dir.
# Exempt from the "registered launch row must have a built artifact" requirement
# ONLY (they still must have a vetting packet + catalog row). The shippable bundles
# that DO have a build dir are not listed here and are checked normally.
BUNDLE_TEMPLATES = frozenset({"bundle-starter"})

# Owner-gated lanes deliberately kept OUT of the storefront catalog and not
# packaged, per docs/launch/CATALOG.md's explicit "Out of scope here ... the Photo
# Packs and the KDP book catalog" note. Exempt from the catalog-row + built-artifact
# requirements (they legitimately carry a launch dir + vetting packet only).
OWNER_GATED_LANES = frozenset({"photo-packs"})


def _subdirs(path: Path):
    """Immediate subdirectory names under `path` (empty list if absent)."""
    if not path.is_dir():
        return []
    return sorted(p.name for p in path.iterdir() if p.is_dir())


def _catalog_refs(catalog_text: str):
    """The set of sku slugs referenced as link paths in CATALOG.md.

    A reference is the slug appearing as a whole path token — immediately
    followed by `/`, `.`, or `)` (i.e. `<slug>/…`, `<slug>.md`, or `<slug>)`),
    and not preceded by a word char or hyphen — so `membership-kit` matches
    `(membership-kit/LISTING.md)` but a longer slug that merely contains a
    shorter one as a substring does not false-match.
    """
    refs = set()
    # Candidate slugs are lowercase, digits, hyphens.
    for m in re.finditer(r"(?<![\w-])([a-z0-9][a-z0-9-]+)(?=[/.)])", catalog_text):
        refs.add(m.group(1))
    return refs


def collect(root=REPO_ROOT):
    """Gather the three registries for the tree under `root`.

    Returns a dict with the built set, launch set, vetting set, and catalog-ref
    set — pure inventory, no verdict.
    """
    root = Path(root)
    cand_dir = root / CANDIDATES_DIR_REL
    built = {
        name
        for name in _subdirs(cand_dir)
        if (cand_dir / name / BUILD_MARKER).is_dir()
    }
    launch = set(_subdirs(root / LAUNCH_DIR_REL))
    vdir = root / VETTING_DIR_REL
    vetting = (
        {p.stem for p in vdir.glob("*.md")} if vdir.is_dir() else set()
    )
    catalog_path = root / CATALOG_REL
    catalog_refs = (
        _catalog_refs(catalog_path.read_text(encoding="utf-8"))
        if catalog_path.is_file()
        else set()
    )
    candidates_all = set(_subdirs(cand_dir))
    return {
        "built": built,
        "launch": launch,
        "vetting": vetting,
        "catalog_refs": catalog_refs,
        "candidates_all": candidates_all,
    }


def check(root=REPO_ROOT):
    """Assert built↔registered correspondence for the tree under `root`.

    Returns (status, violations):
      * ("ok", [])      — every built SKU is registered and every registered SKU
                          has its artifacts (or is a documented exemption);
      * ("skip", why)   — nothing to check (no launch dirs and no built candidates);
      * ("drift", [..]) — a list of human-readable violation lines.
    """
    reg = collect(root)
    built = reg["built"]
    launch = reg["launch"]
    vetting = reg["vetting"]
    catalog_refs = reg["catalog_refs"]

    if not launch and not built:
        return "skip", (
            "no launch rows under {l} and no built candidates under {c} — nothing "
            "to correspond".format(l=LAUNCH_DIR_REL, c=CANDIDATES_DIR_REL)
        )

    violations = []

    # ---- Direction A: BUILT-BUT-UNREGISTERED ----------------------------------
    # Every packaged candidate must be registered for launch + queue + catalog.
    for sku in sorted(built):
        missing = []
        if sku not in launch:
            missing.append("no launch row (docs/launch/{s}/)".format(s=sku))
        if sku not in vetting:
            missing.append(
                "no vetting packet (docs/publishing/vetting/{s}.md)".format(s=sku)
            )
        if sku not in catalog_refs:
            missing.append("not referenced in docs/launch/CATALOG.md")
        if missing:
            violations.append(
                "BUILT-BUT-UNREGISTERED: candidates/{s}/{m}/ is packaged but {why}".format(
                    s=sku, m=BUILD_MARKER, why="; ".join(missing)
                )
            )

    # ---- Direction B: REGISTERED-BUT-MISSING-ARTIFACT -------------------------
    # Every launch row must have its vetting packet, catalog row, and (unless a
    # documented exemption) a built artifact.
    for sku in sorted(launch):
        missing = []
        if sku not in vetting:
            missing.append(
                "no vetting packet (docs/publishing/vetting/{s}.md)".format(s=sku)
            )
        if sku not in catalog_refs and sku not in OWNER_GATED_LANES:
            missing.append("not referenced in docs/launch/CATALOG.md")
        if (
            sku not in built
            and sku not in BUNDLE_TEMPLATES
            and sku not in OWNER_GATED_LANES
        ):
            missing.append(
                "no built artifact (candidates/{s}/{m}/)".format(s=sku, m=BUILD_MARKER)
            )
        if missing:
            violations.append(
                "REGISTERED-BUT-MISSING-ARTIFACT: docs/launch/{s}/ is a launch row but {why}".format(
                    s=sku, why="; ".join(missing)
                )
            )

    if violations:
        return "drift", violations
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

    if status == "drift":
        print("DRIFT: storefront inventory and registries disagree.")
        print(
            "Every packaged candidate (candidates/<sku>/{m}/) must be registered "
            "for launch (docs/launch/<sku>/),\nhave a vetting packet "
            "(docs/publishing/vetting/<sku>.md), and appear in "
            "docs/launch/CATALOG.md;\nand every launch row must have its artifacts. "
            "Fix by registering the built SKU (or building\nthe registered one) — "
            "do NOT hand-edit this guard's allowlists to hide real drift.\n".format(
                m=BUILD_MARKER
            )
        )
        print("--- {n} violation(s) ---".format(n=len(detail)))
        for line in detail:
            print("  * " + line)
        print("FAIL: built/registered correspondence is broken.")
        return 1

    if status == "skip":
        if not args.quiet:
            print("SKIP: {why}".format(why=detail))
        return 0

    if not args.quiet:
        reg = collect(args.root)
        print(
            "OK: {b} built SKU(s) all registered; {l} launch row(s) all have "
            "artifacts — built/registered correspondence holds.".format(
                b=len(reg["built"]), l=len(reg["launch"])
            )
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
