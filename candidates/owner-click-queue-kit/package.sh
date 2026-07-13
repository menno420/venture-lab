#!/bin/sh
# Build the buyer bundle for Owner-Click Queue Kit v0.1.
# Bundles: the derive+lint tool, the grammar spec, the gotchas, the
# test suite, and both worked examples with their committed expected
# outputs.
# EXCLUDES: INTAKE.md (internal), package.sh (build tooling), dist/,
# .git, __pycache__. Explicit per-file allow-list copy (never a
# directory sweep) + fixed mtimes + sorted entries + zip -X so the
# build is byte-reproducible (same convention as the sibling kits).
set -eu

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
SRC="$SCRIPT_DIR"
BUNDLE_NAME="owner-click-queue-kit-v0.1"
DIST_DIR="$SRC/dist"
ZIP_PATH="$DIST_DIR/$BUNDLE_NAME.zip"
SOURCE_DATE="200001010000.00"

STAGE=$(mktemp -d)
trap 'rm -rf "$STAGE"' EXIT
ROOT="$STAGE/$BUNDLE_NAME"
mkdir -p "$ROOT/examples/agent-fleet/gates" "$ROOT/examples/solo-repo"

cp "$SRC/README.md"    "$ROOT/README.md"
cp "$SRC/GRAMMAR.md"   "$ROOT/GRAMMAR.md"
cp "$SRC/GOTCHAS.md"   "$ROOT/GOTCHAS.md"
cp "$SRC/ocq.py"       "$ROOT/ocq.py"
cp "$SRC/test_ocq.py"  "$ROOT/test_ocq.py"
cp "$SRC/examples/README.md" "$ROOT/examples/README.md"
cp "$SRC/examples/agent-fleet/gates/checkout-revamp.md" \
   "$ROOT/examples/agent-fleet/gates/checkout-revamp.md"
cp "$SRC/examples/agent-fleet/gates/newsletter-launch.md" \
   "$ROOT/examples/agent-fleet/gates/newsletter-launch.md"
cp "$SRC/examples/agent-fleet/gates/status-page.md" \
   "$ROOT/examples/agent-fleet/gates/status-page.md"
cp "$SRC/examples/agent-fleet/EXPECTED-OWNER-QUEUE.md" \
   "$ROOT/examples/agent-fleet/EXPECTED-OWNER-QUEUE.md"
cp "$SRC/examples/solo-repo/RELEASE-GATE.md" \
   "$ROOT/examples/solo-repo/RELEASE-GATE.md"
cp "$SRC/examples/solo-repo/EXPECTED-OWNER-QUEUE.md" \
   "$ROOT/examples/solo-repo/EXPECTED-OWNER-QUEUE.md"

find "$ROOT" -exec touch -t "$SOURCE_DATE" {} +

mkdir -p "$DIST_DIR"
rm -f "$ZIP_PATH"
( cd "$STAGE" && find "$BUNDLE_NAME" -print | sort | zip -X -q "$ZIP_PATH" -@ )

echo "built: $ZIP_PATH"
unzip -l "$ZIP_PATH"
