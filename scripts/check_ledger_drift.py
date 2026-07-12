#!/usr/bin/env python3
"""scripts/check_ledger_drift.py — ADVISORY ledger-drift checker.

Compares the highest PR number cited in the living ledger's
"Recently shipped" section (docs/current-state.md) against the newest
MERGED pull request on GitHub, and prints ONE advisory line:

    ledger-drift: in-sync (ledger cites #N, newest merged #N)
    ledger-drift: trailing by K — missing PRs: #a, #b, ...
    ledger-drift: skipped — <reason>

ADVISORY ONLY — this script exits 0 on EVERY path (in-sync, trailing,
skip, parse failure). It must never be wired as a required gate; the
same contract as the kit's `claims-stale` advisory. Rationale + usage:
docs/ledger-drift-checker.md (origin: PR #90's session-card 💡 idea —
the ledger trailed 3 merged PRs at #90's own merge and nothing nagged).

Stdlib only. Auth: GITHUB_TOKEN or GH_TOKEN from the environment if
present (CI provides one); with no token or an unreachable API the
check degrades to a graceful skip line, never an error.
"""

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request

DEFAULT_LEDGER = "docs/current-state.md"
DEFAULT_REPO = "menno420/venture-lab"
SECTION_HEADING = "recently shipped"
API_TIMEOUT_SECONDS = 15
# One page of the most recent closed PRs is plenty for an advisory
# gap check; a gap deeper than this is loud long before it matters.
API_PAGE_SIZE = 100


def advisory(line: str) -> int:
    """Print the single advisory line. ALWAYS returns exit code 0."""
    print(line)
    return 0


def parse_cited_max(ledger_text: str) -> int | None:
    """Highest PR number cited in the "Recently shipped" section.

    The section runs from its `## ` heading to the next `## ` heading
    (or EOF). Any `#123` token inside counts as a citation — this also
    catches range spellings like `#67–#82` and `PRs #79/#80` at both
    endpoints. Returns None when the section or a citation is missing.
    """
    lines = ledger_text.splitlines()
    start = None
    for i, line in enumerate(lines):
        if line.startswith("## ") and SECTION_HEADING in line.lower():
            start = i + 1
            break
    if start is None:
        return None
    section: list[str] = []
    for line in lines[start:]:
        if line.startswith("## "):
            break
        section.append(line)
    cited = [int(m) for m in re.findall(r"#(\d+)\b", "\n".join(section))]
    return max(cited) if cited else None


def fetch_merged_prs(repo: str, token: str) -> list[int]:
    """Merged-PR numbers from the newest page of closed PRs (desc)."""
    url = (
        f"https://api.github.com/repos/{repo}/pulls"
        f"?state=closed&sort=created&direction=desc&per_page={API_PAGE_SIZE}"
    )
    request = urllib.request.Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "User-Agent": "venture-lab-ledger-drift-checker",
            "X-GitHub-Api-Version": "2022-11-28",
        },
    )
    with urllib.request.urlopen(request, timeout=API_TIMEOUT_SECONDS) as response:
        pulls = json.load(response)
    # merged_at is the merge truth; the `merged` bool is absent on list
    # payloads and some proxies mangle it.
    return [pr["number"] for pr in pulls if pr.get("merged_at")]


def run(ledger_path: str, repo: str) -> int:
    try:
        with open(ledger_path, encoding="utf-8") as handle:
            ledger_text = handle.read()
    except OSError as error:
        return advisory(f"ledger-drift: skipped — cannot read {ledger_path} ({error})")

    cited = parse_cited_max(ledger_text)
    if cited is None:
        return advisory(
            f"ledger-drift: skipped — no PR citation found in the"
            f' "Recently shipped" section of {ledger_path}'
        )

    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if not token:
        return advisory(
            "ledger-drift: skipped — no GITHUB_TOKEN/GH_TOKEN in the environment"
            f" (ledger cites #{cited}; API check needs a token)"
        )

    try:
        merged = fetch_merged_prs(repo, token)
    except Exception as error:  # advisory: ANY API failure degrades to a skip
        return advisory(
            f"ledger-drift: skipped — GitHub API unavailable ({error});"
            f" ledger cites #{cited}"
        )
    if not merged:
        return advisory(
            f"ledger-drift: skipped — no merged PRs visible via the API"
            f" (ledger cites #{cited})"
        )

    newest = max(merged)
    missing = sorted(n for n in merged if n > cited)
    if not missing:
        return advisory(
            f"ledger-drift: in-sync (ledger cites #{cited}, newest merged #{newest})"
        )
    listed = ", ".join(f"#{n}" for n in missing)
    return advisory(f"ledger-drift: trailing by {len(missing)} — missing PRs: {listed}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="check_ledger_drift",
        description="ADVISORY ledger-drift check — always exits 0.",
    )
    parser.add_argument(
        "--ledger",
        default=DEFAULT_LEDGER,
        help=f"path to the living ledger (default: {DEFAULT_LEDGER})",
    )
    parser.add_argument(
        "--repo",
        default=os.environ.get("GITHUB_REPOSITORY") or DEFAULT_REPO,
        help="owner/repo to query (default: $GITHUB_REPOSITORY or "
        f"{DEFAULT_REPO})",
    )
    args = parser.parse_args(argv)
    return run(args.ledger, args.repo)


if __name__ == "__main__":
    sys.exit(main())
