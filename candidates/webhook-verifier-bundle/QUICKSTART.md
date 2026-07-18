# Quickstart — Webhook Verifier Bundle

You downloaded `webhook-verifier-bundle-v0.1.zip`. It contains the four
component kits' own buyer bundles plus this documentation. Nothing here needs an
account, an API key, or a network connection — every kit is stdlib-only Python
(with a JS parity port alongside).

## 1. Unzip the bundle

```sh
unzip webhook-verifier-bundle-v0.1.zip
cd webhook-verifier-bundle-v0.1
ls kits/
# github-webhook-test-kit-v0.1.zip
# shopify-webhook-test-kit-v0.1.zip
# slack-webhook-test-kit-v0.1.zip
# stripe-webhook-test-kit-v0.1.zip
```

## 2. Pick the provider you're wiring up and unzip that kit

```sh
cd kits
unzip stripe-webhook-test-kit-v0.1.zip      # or github / slack / shopify
cd stripe-webhook-test-kit-v0.1
cat README.md          # provider-specific: header, signed bytes, encoding
```

## 3. Run that kit's test suite (one command, no accounts)

Each kit ships an HTTP real-path test suite that starts the real handler over
loopback and drives signed fixture payloads through it — true-pass plus the
tamper / wrong-secret / (replay or malformed) rejection cases:

```sh
python3 -m unittest test_http_realpath -v
```

## 4. Use the kit against your own endpoint

Each kit's README shows the correct verification for that provider and points at
the example handler (`stub_handler.py` / equivalent) you can copy the check
from. The GOTCHAS.md in each kit lists the specific mistakes that silently pass
a naive verifier (wrong signed bytes, hex-vs-base64, missing constant-time
compare, no replay window).

## Verify what you got (optional)

Every artifact is pinned by sha256 in `MANIFEST.json`. To confirm the four kit
zips are exactly the published ones:

```sh
cd kits
sha256sum *.zip
# compare against MANIFEST.json's per-component sha256 values
```

That's it — no build step, no dependencies, no signup.
