#!/usr/bin/env python3
"""vendor_fixture.py — turn a pasted provider sample payload into a vendored
test fixture + a PROVENANCE.md stub you are forced to fill in.

The discipline (the false-green lesson): NEVER test a webhook handler against
a payload you typed from memory. Paste a REAL sample payload — from your
provider's docs, SDK source, CLI (`stripe trigger`), or dashboard event log —
into a file, then run this script on it. You get:

  1. <name>.json          — the fixture, validated + pretty-printed
  2. <name>.PROVENANCE.md — a provenance stub with the fixture sha256, every
                            null field enumerated (null fields are where
                            false-green bugs hide), every volatile-looking
                            field flagged, and [[fill]] slots for the source
                            URL + field-name verification you still owe.

This script is OFFLINE by design: it fetches nothing, phones nowhere, and
imports only the Python standard library. It cannot vouch for where your
sample came from — that is what the PROVENANCE stub makes you write down.

Fail-closed rules:
  * not valid UTF-8 JSON with an object at top level  -> exit 2, no output
  * secret-looking material (sk_live_/sk_test_/whsec_/private keys/bearer
    tokens) anywhere in the payload                    -> exit 2, no output
    (a real sample payload never needs a real secret; re-paste without it)

Optional PII strip: --redact-emails rewrites every email-shaped string value
to a stable placeholder (redacted-1@example.com, ...) so a sample copied from
a real dashboard event does not vendor a real customer address into your repo.

Usage:
  python3 vendor_fixture.py SAMPLE.json [--name NAME] [--out DIR]
                            [--redact-emails] [--force]

Exit codes: 0 written · 2 refused (invalid/secret) · 1 usage/IO error.
"""

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

# --- detectors ------------------------------------------------------------- #

# Secret-looking values: refuse to write anything (fail closed).
SECRET_PATTERNS = [
    (re.compile(r"sk_(live|test)_[0-9a-zA-Z]{8,}"), "Stripe secret key"),
    (re.compile(r"rk_(live|test)_[0-9a-zA-Z]{8,}"), "Stripe restricted key"),
    (re.compile(r"whsec_[0-9a-zA-Z]{8,}"), "webhook signing secret"),
    (re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"), "PEM private key"),
    (re.compile(r"(?i)bearer\s+[0-9a-zA-Z._\-]{16,}"), "bearer token"),
    (re.compile(r"gh[pousr]_[0-9a-zA-Z]{16,}"), "GitHub token"),
    (re.compile(r"AKIA[0-9A-Z]{16}"), "AWS access key id"),
]

# Volatile-by-name: values that change per event/per capture. A fixture may
# keep them (shape matters, values are illustrative) but the provenance must
# say so, and tests must never assert their literal values.
VOLATILE_KEY_RE = re.compile(
    r"(?i)^(created|updated|timestamp|.*_at|expires.*|nonce|idempotency_key|"
    r"api_version|request_id|signature|livemode)$"
)
# Provider-id-shaped string values (evt_..., cs_test_..., pi_..., in_...).
PROVIDER_ID_RE = re.compile(r"^[a-z]{2,8}_(test_|live_)?[0-9a-zA-Z]{6,}$")
EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def walk(node, path=""):
    """Yield (json_path, key, value) for every key in the tree."""
    if isinstance(node, dict):
        for k, v in node.items():
            p = f"{path}.{k}" if path else k
            yield p, k, v
            yield from walk(v, p)
    elif isinstance(node, list):
        for i, v in enumerate(node):
            p = f"{path}[{i}]"
            yield p, None, v
            yield from walk(v, p)


def analyze(payload):
    nulls, volatile, ids, emails = [], [], [], []
    for p, k, v in walk(payload):
        if v is None:
            nulls.append(p)
        if k is not None and VOLATILE_KEY_RE.match(k):
            volatile.append(p)
        if isinstance(v, str):
            if PROVIDER_ID_RE.match(v):
                ids.append(p)
            if EMAIL_RE.match(v):
                emails.append(p)
    return nulls, volatile, ids, emails


def redact_emails(payload):
    """Replace email-shaped string values with stable placeholders."""
    mapping = {}

    def sub(node):
        if isinstance(node, dict):
            return {k: sub(v) for k, v in node.items()}
        if isinstance(node, list):
            return [sub(v) for v in node]
        if isinstance(node, str) and EMAIL_RE.match(node):
            if node not in mapping:
                mapping[node] = f"redacted-{len(mapping) + 1}@example.com"
            return mapping[node]
        return node

    return sub(payload), mapping


PROVENANCE_TEMPLATE = """# Fixture provenance — {name}.json

> Written by vendor_fixture.py on {date}. The [[fill]] slots below are YOUR
> homework — a fixture without a filled provenance is just a prettier payload
> you still cannot trust.

- **Fixture:** `{name}.json` · sha256 `{sha}` ({size} bytes)
- **Source (where this sample payload was copied from):** [[fill: exact URL —
  provider docs page, SDK source file, dashboard event log, or the CLI
  command (e.g. `stripe trigger checkout.session.completed`) that produced it]]
- **Copied on:** [[fill: date]] · **Provider API version (if shown):** [[fill]]

## Field-name verification (do this, then delete this sentence)

For each field your handler READS, cite where its name/type is defined in the
provider's SDK source or OpenAPI spec — not the prose docs, the source:

| field your handler reads | verified against (URL + struct/schema name) |
|---|---|
| [[fill]] | [[fill]] |

## Null fields in this sample ({n_null})

Null fields are where false-green bugs live (the `customer_email: null`
lesson). Your tests should ASSERT these are null, so a handler that reads
them gets caught:

{null_list}

## Volatile fields flagged ({n_volatile})

Per-event values (timestamps, versions, ids). Keeping them is fine — the
fixture's job is SHAPE — but never assert their literal values, and say here
whether they are captured-real or illustrative:

{volatile_list}

## Provider-id-shaped values ({n_ids})

{id_list}

## Email-shaped values ({n_emails})

{email_list}

## What is verified vs illustrative

- Field **names and types**: [[fill: verified against the sources above /
  NOT YET VERIFIED]]
- **Values** (ids, emails, amounts, timestamps): illustrative sample data
  unless stated otherwise above. No real customer data, no secrets — the
  vendoring script fails closed on secret-looking material.
"""


def bullet_list(paths, empty="- (none)"):
    return "\n".join(f"- `{p}`" for p in paths) if paths else empty


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="Vendor a pasted provider sample payload as a test "
        "fixture + PROVENANCE.md stub. Offline; stdlib-only; fails closed "
        "on secrets."
    )
    ap.add_argument("sample", help="file containing the pasted sample payload (JSON)")
    ap.add_argument("--name", help="fixture base name (default: sample file stem)")
    ap.add_argument("--out", default="fixtures", help="output directory (default: fixtures/)")
    ap.add_argument("--redact-emails", action="store_true",
                    help="replace email-shaped values with redacted-N@example.com")
    ap.add_argument("--force", action="store_true", help="overwrite existing outputs")
    args = ap.parse_args(argv)

    src = Path(args.sample)
    try:
        raw = src.read_bytes()
    except OSError as e:
        print(f"REFUSED: cannot read {src}: {e}", file=sys.stderr)
        return 1

    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as e:
        print(f"REFUSED: {src} is not UTF-8 ({e}) — paste the sample as plain text.",
              file=sys.stderr)
        return 2

    for rx, label in SECRET_PATTERNS:
        m = rx.search(text)
        if m:
            print(f"REFUSED: sample contains a {label}-looking value "
                  f"({m.group(0)[:12]}…). A sample payload never needs a real "
                  f"secret — remove it and re-run. Nothing was written.",
                  file=sys.stderr)
            return 2

    try:
        payload = json.loads(text)
    except json.JSONDecodeError as e:
        print(f"REFUSED: not valid JSON: {e}. Nothing was written.", file=sys.stderr)
        return 2
    if not isinstance(payload, dict):
        print("REFUSED: top level must be a JSON object (a provider event "
              "envelope), not a bare value/array. Nothing was written.",
              file=sys.stderr)
        return 2

    email_map = {}
    if args.redact_emails:
        payload, email_map = redact_emails(payload)

    nulls, volatile, ids, emails = analyze(payload)

    name = args.name or src.stem
    outdir = Path(args.out)
    fixture_path = outdir / f"{name}.json"
    prov_path = outdir / f"{name}.PROVENANCE.md"
    for p in (fixture_path, prov_path):
        if p.exists() and not args.force:
            print(f"REFUSED: {p} exists (use --force to overwrite). "
                  f"Nothing was written.", file=sys.stderr)
            return 2

    outdir.mkdir(parents=True, exist_ok=True)
    fixture_bytes = (json.dumps(payload, indent=2, ensure_ascii=False) + "\n").encode("utf-8")
    fixture_path.write_bytes(fixture_bytes)
    sha = hashlib.sha256(fixture_bytes).hexdigest()

    prov = PROVENANCE_TEMPLATE.format(
        name=name,
        date=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%SZ"),
        sha=sha,
        size=len(fixture_bytes),
        n_null=len(nulls), null_list=bullet_list(
            nulls, "- (none — unusual for a real provider event; double-check "
                   "your sample is complete, not hand-trimmed)"),
        n_volatile=len(volatile), volatile_list=bullet_list(volatile),
        n_ids=len(ids), id_list=bullet_list(ids),
        n_emails=len(emails), email_list=bullet_list(emails),
    )
    prov_path.write_text(prov, encoding="utf-8")

    print(f"vendored: {fixture_path} ({len(fixture_bytes)} bytes)")
    print(f"sha256:   {sha}")
    print(f"stub:     {prov_path}")
    print(f"null fields ({len(nulls)}):     " + (", ".join(nulls) or "(none)"))
    print(f"volatile fields ({len(volatile)}): " + (", ".join(volatile) or "(none)"))
    print(f"provider ids ({len(ids)}):    " + (", ".join(ids) or "(none)"))
    if args.redact_emails and email_map:
        print(f"emails redacted ({len(email_map)}): "
              + ", ".join(f"{v}" for v in email_map.values()))
    elif emails:
        print(f"email-shaped values ({len(emails)}): " + ", ".join(emails)
              + "  <- real address? re-run with --redact-emails")
    print("NEXT: open the PROVENANCE stub and fill every [[fill]] slot — "
          "source URL + field-name verification make it a fixture you can trust.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
