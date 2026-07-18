#!/bin/sh
# Build the buyer bundle for the API Robustness Bundle v0.1.
# Bundles: this directory's README / QUICKSTART / PROVENANCE / MANIFEST, plus the
# FOUR component kits' own published buyer zips (copied verbatim into kits/) —
# idempotency-key / rate-limit / pagination / jwt-auth -test-kit-v0.1.zip.
# EXCLUDES: package.sh (build tooling), test_bundle.py (assembly check, not a
# buyer artifact), dist/, .git, __pycache__.
# Allow-list copy + fixed mtimes + sorted entries + zip -X so the build is
# byte-reproducible (same convention as the four component kits and the Webhook
# Verifier Bundle). The component zips are themselves byte-reproducible, so
# copying them verbatim keeps the outer zip reproducible too.
set -eu

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
SRC="$SCRIPT_DIR"
REPO_ROOT=$(CDPATH= cd -- "$SRC/../.." && pwd)
BUNDLE_NAME="api-robustness-bundle-v0.1"
DIST_DIR="$SRC/dist"
ZIP_PATH="$DIST_DIR/$BUNDLE_NAME.zip"
SOURCE_DATE="200001010000.00"

STAGE=$(mktemp -d)
trap 'rm -rf "$STAGE"' EXIT
ROOT="$STAGE/$BUNDLE_NAME"
mkdir -p "$ROOT/kits"

cp "$SRC/README.md"      "$ROOT/README.md"
cp "$SRC/QUICKSTART.md"  "$ROOT/QUICKSTART.md"
cp "$SRC/PROVENANCE.md"  "$ROOT/PROVENANCE.md"
cp "$SRC/MANIFEST.json"  "$ROOT/MANIFEST.json"

cp "$REPO_ROOT/candidates/idempotency-key-test-kit/dist/idempotency-key-test-kit-v0.1.zip" "$ROOT/kits/"
cp "$REPO_ROOT/candidates/rate-limit-test-kit/dist/rate-limit-test-kit-v0.1.zip"           "$ROOT/kits/"
cp "$REPO_ROOT/candidates/pagination-test-kit/dist/pagination-test-kit-v0.1.zip"           "$ROOT/kits/"
cp "$REPO_ROOT/candidates/jwt-auth-test-kit/dist/jwt-auth-test-kit-v0.1.zip"               "$ROOT/kits/"

find "$ROOT" -exec touch -t "$SOURCE_DATE" {} +

mkdir -p "$DIST_DIR"
rm -f "$ZIP_PATH"
( cd "$STAGE" && find "$BUNDLE_NAME" -print | sort | zip -X -q "$ZIP_PATH" -@ )

echo "built: $ZIP_PATH"
unzip -l "$ZIP_PATH"
