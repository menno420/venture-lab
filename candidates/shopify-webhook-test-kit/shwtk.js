#!/usr/bin/env node
"use strict";
/*
 * Shopify Webhook Test Kit (shwtk) — Node stdlib port of shwtk.py.
 *
 * Fire REAL-shape signed Shopify webhooks at your local endpoint and check your
 * handler the way Shopify actually behaves. Stdlib only (crypto, fs, path, http,
 * https, url) — no npm install, no build step. Node 14+.
 *
 * Subcommands (mirror shwtk.py exactly):
 *   fire   --url --fixture [--secret-env] [--forge|--unsigned|--tamper|--malformed]
 *   vector
 *   list
 *
 * The Shopify webhook secret is read from an environment variable (NAME only —
 * the value is never stored, logged, or echoed). Default: SHOPIFY_WEBHOOK_SECRET.
 *
 * Shopify signs DIFFERENTLY from Slack/Stripe: X-Shopify-Hmac-Sha256 is the
 * BASE64 (not hex) HMAC-SHA256 of the RAW body DIRECTLY — no timestamp
 * basestring, no replay window (so no --stale mode, no challenge handshake).
 */
const crypto = require("crypto");
const fs = require("fs");
const path = require("path");
const http = require("http");
const https = require("https");
const { URL } = require("url");

const FIXTURES_DIR = path.join(__dirname, "fixtures");
const DEFAULT_SECRET_ENV = "SHOPIFY_WEBHOOK_SECRET";

const HMAC_HEADER = "X-Shopify-Hmac-Sha256";
const TOPIC_HEADER = "X-Shopify-Topic";
const SHOP_DOMAIN_HEADER = "X-Shopify-Shop-Domain";
const WEBHOOK_ID_HEADER = "X-Shopify-Webhook-Id";
const API_VERSION_HEADER = "X-Shopify-Api-Version";

const DEMO_SHOP_DOMAIN = "example-store.myshopify.com";
const DEMO_WEBHOOK_ID = "b54557e4-bcc0-4f8b-a1f0-6f0b3a1d2c3e";
const DEMO_API_VERSION = "2026-07";

// Kit-internal known-answer vector (Shopify publishes no fixed constant — see
// fixtures/PROVENANCE.md). Byte-identical to shwtk.py's constants.
const VECTOR_SECRET = "shwtk_test_client_secret_v0_1_not_a_real_secret";
const VECTOR_BODY = Buffer.from(
  '{"id":123456789,"topic":"orders/create","note":"shwtk known-answer vector"}',
  "utf-8"
);
const VECTOR_HMAC = "uhRiDuW3C3+o+mLcijsFK2jv0FwIloa+C4O5MQzK6w0=";

// --------------------------------------------------------------------------- //
// Signature — the real X-Shopify-Hmac-Sha256 scheme.
// header = base64( HMAC-SHA256(secret, RAW body) )  -- base64, NOT hex; no ts.
// --------------------------------------------------------------------------- //
function shopifyHmac(rawBody, secret) {
  return crypto.createHmac("sha256", Buffer.from(secret, "utf-8")).update(rawBody).digest("base64");
}

// --------------------------------------------------------------------------- //
// Fixtures
// --------------------------------------------------------------------------- //
function loadManifest() {
  const m = JSON.parse(fs.readFileSync(path.join(FIXTURES_DIR, "MANIFEST.json"), "utf-8"));
  delete m._comment;
  return m;
}

function stemOf(name) {
  return name.replace(/\.json$/, "");
}

function entryFor(stem) {
  const m = loadManifest();
  stem = stemOf(stem);
  if (!(stem in m)) {
    fail(`error: fixture '${stem}' has no entry in fixtures/MANIFEST.json.`);
  }
  return m[stem];
}

function fixtureFile(stem) {
  stem = stemOf(stem);
  const p = path.join(FIXTURES_DIR, stem + ".json");
  if (fs.existsSync(p)) return p;
  fail(`error: fixture not found: ${stem}. Run \`shwtk list\` to see bundled fixtures.`);
}

function loadFixture(stem) {
  return fs.readFileSync(fixtureFile(stem));
}

function contentTypeFor(stem) {
  return entryFor(stem).content_type;
}

function topicFor(stem) {
  return entryFor(stem).topic;
}

function listFixtures() {
  return Object.keys(loadManifest()).sort();
}

// --------------------------------------------------------------------------- //
// HTTP + verdicts
// --------------------------------------------------------------------------- //
function buildRequest(rawBody, contentType, topic, opts = {}) {
  // opts: { secret, signBody, forge, malformed }
  const headers = {
    "Content-Type": contentType,
    [TOPIC_HEADER]: topic,
    [SHOP_DOMAIN_HEADER]: DEMO_SHOP_DOMAIN,
    [WEBHOOK_ID_HEADER]: DEMO_WEBHOOK_ID,
    [API_VERSION_HEADER]: DEMO_API_VERSION,
  };
  if (opts.malformed) {
    headers[HMAC_HEADER] = "!!!not-valid-base64!!!";
  } else if (opts.secret !== undefined && opts.secret !== null) {
    const signingSecret = opts.forge ? opts.secret + "__shwtk_forged__" : opts.secret;
    const toSign = opts.signBody !== undefined && opts.signBody !== null ? opts.signBody : rawBody;
    headers[HMAC_HEADER] = shopifyHmac(toSign, signingSecret);
  }
  return [rawBody, headers];
}

function postRequest(urlStr, body, headers, timeoutMs = 10000) {
  return new Promise((resolve, reject) => {
    let u;
    try {
      u = new URL(urlStr);
    } catch (e) {
      reject(new Error(`invalid url: ${urlStr}`));
      return;
    }
    const lib = u.protocol === "https:" ? https : http;
    const h = Object.assign({ "Content-Length": Buffer.byteLength(body) }, headers);
    const options = {
      method: "POST",
      hostname: u.hostname,
      port: u.port || (u.protocol === "https:" ? 443 : 80),
      path: u.pathname + u.search,
      headers: h,
    };
    const req = lib.request(options, (res) => {
      const chunks = [];
      res.on("data", (c) => chunks.push(c));
      res.on("end", () => resolve([res.statusCode, Buffer.concat(chunks).toString("utf-8")]));
    });
    // A handler that drops the connection yields status 0 — treated as neither
    // a 2xx accept nor a clean 4xx reject, so both verdicts mark it a FAIL.
    req.on("error", (e) => resolve([0, `<no HTTP response: ${e.message}>`]));
    req.setTimeout(timeoutMs, () => req.destroy(new Error("request timed out")));
    req.write(body);
    req.end();
  });
}

function normalFirePass(status) {
  return status >= 200 && status < 300;
}
function rejectedFirePass(status) {
  return status >= 400 && status < 500;
}

// --------------------------------------------------------------------------- //
// CLI helpers
// --------------------------------------------------------------------------- //
function fail(msg) {
  process.stderr.write(msg + "\n");
  process.exit(2);
}

function requireSecret(envName) {
  const secret = process.env[envName];
  if (!secret) {
    fail(
      `error: environment variable ${envName} is not set. Export your Shopify webhook ` +
        `secret into it — the value is read from the env and never stored.`
    );
  }
  return secret;
}

function printBody(body) {
  body = body.trim();
  if (!body) return;
  if (body.length > 600) body = body.slice(0, 600) + " …(truncated)";
  console.log("        response:", body);
}

function parseOpts(argv, spec) {
  const out = { _: [] };
  for (let i = 0; i < argv.length; i++) {
    let a = argv[i];
    if (a.startsWith("--")) {
      let key = a.slice(2);
      let val = null;
      const eq = key.indexOf("=");
      if (eq !== -1) {
        val = key.slice(eq + 1);
        key = key.slice(0, eq);
      }
      const norm = key.replace(/-/g, "_");
      if (spec.flags && spec.flags.has(key)) {
        out[norm] = true;
      } else if (spec.opts && spec.opts.has(key)) {
        if (val === null) {
          val = argv[++i];
          if (val === undefined) fail(`error: --${key} requires a value`);
        }
        out[norm] = val;
      } else {
        fail(`error: unknown option --${key}`);
      }
    } else {
      out._.push(a);
    }
  }
  return out;
}

// --------------------------------------------------------------------------- //
// Commands
// --------------------------------------------------------------------------- //
async function cmdFire(argv) {
  const o = parseOpts(argv, {
    flags: new Set(["forge", "unsigned", "tamper", "malformed"]),
    opts: new Set(["url", "fixture", "secret-env"]),
  });
  if (!o.url) fail("error: fire requires --url");
  if (!o.fixture) fail("error: fire requires --fixture");
  const modes = [o.forge, o.unsigned, o.tamper, o.malformed].filter(Boolean);
  if (modes.length > 1) fail("error: --forge / --unsigned / --tamper / --malformed are mutually exclusive.");
  const secretEnv = o.secret_env || DEFAULT_SECRET_ENV;
  const payload = loadFixture(o.fixture);
  const contentType = contentTypeFor(o.fixture);
  const topic = topicFor(o.fixture);

  if (o.unsigned) {
    const [body, headers] = buildRequest(payload, contentType, topic, {});
    const [status, resp] = await postRequest(o.url, body, headers);
    console.log(`[unsigned]  POST ${o.url}  (${o.fixture})  ->  HTTP ${status}`);
    printBody(resp);
    if (rejectedFirePass(status)) {
      console.log("PASS: handler rejected the unsigned webhook (missing signature fails closed).");
      return 0;
    }
    console.log("FAIL: handler ACCEPTED a webhook with NO X-Shopify-Hmac-Sha256 header.");
    return 1;
  }

  if (o.malformed) {
    const [body, headers] = buildRequest(payload, contentType, topic, { malformed: true });
    const [status, resp] = await postRequest(o.url, body, headers);
    console.log(`[malformed] POST ${o.url}  (${o.fixture})  ->  HTTP ${status}`);
    printBody(resp);
    if (rejectedFirePass(status)) {
      console.log("PASS: handler rejected the malformed-base64 signature cleanly (4xx, no crash).");
      return 0;
    }
    if (status === 0 || (status >= 500 && status < 600)) {
      console.log(`FAIL: handler CRASHED (HTTP ${status || "connection dropped"}) on a non-base64 signature`);
      console.log("      header. Decode it defensively and return 401/400 — never let bad input 500 you.");
    } else {
      console.log("FAIL: handler ACCEPTED a webhook whose X-Shopify-Hmac-Sha256 is not valid base64.");
    }
    return 1;
  }

  const secret = requireSecret(secretEnv);

  if (o.forge) {
    const [body, headers] = buildRequest(payload, contentType, topic, { secret, forge: true });
    const [status, resp] = await postRequest(o.url, body, headers);
    console.log(`[forge]     POST ${o.url}  (${o.fixture})  ->  HTTP ${status}`);
    printBody(resp);
    if (rejectedFirePass(status)) {
      console.log("PASS: handler rejected the wrong-secret webhook (signature verification is working).");
      return 0;
    }
    console.log("FAIL: handler ACCEPTED a webhook signed with the wrong secret (HTTP 2xx). It is not");
    console.log("      verifying X-Shopify-Hmac-Sha256 — anyone who knows your URL can post fake webhooks.");
    return 1;
  }

  if (o.tamper) {
    const tampered = Buffer.concat([payload, Buffer.from(" ", "utf-8")]);
    const [body, headers] = buildRequest(tampered, contentType, topic, { secret, signBody: payload });
    const [status, resp] = await postRequest(o.url, body, headers);
    console.log(`[tamper]    POST ${o.url}  (${o.fixture})  ->  HTTP ${status}`);
    printBody(resp);
    if (rejectedFirePass(status)) {
      console.log("PASS: handler rejected the tampered body (it hashes the RAW bytes it received).");
      return 0;
    }
    console.log("FAIL: handler ACCEPTED a body that differs from the one the signature covers.");
    return 1;
  }

  const [body, headers] = buildRequest(payload, contentType, topic, { secret });
  const [status, resp] = await postRequest(o.url, body, headers);
  console.log(`[fire]      POST ${o.url}  (${o.fixture}, topic=${topic})  ->  HTTP ${status}`);
  printBody(resp);
  if (normalFirePass(status)) {
    console.log("PASS: handler accepted the correctly-signed webhook.");
    return 0;
  }
  console.log(`FAIL: handler did not accept a correctly-signed webhook (HTTP ${status}, expected 2xx).`);
  return 1;
}

function cmdVector() {
  const computed = shopifyHmac(VECTOR_BODY, VECTOR_SECRET);
  console.log("Kit-internal known-answer vector (see fixtures/PROVENANCE.md — Shopify");
  console.log("publishes the verification METHOD but NOT a fixed known-answer constant,");
  console.log("so this vector is the kit's own, honestly labelled):");
  console.log(`  secret   = '${VECTOR_SECRET}'`);
  console.log(`  body     = '${VECTOR_BODY.toString("utf-8")}'`);
  console.log(`  expected = ${VECTOR_HMAC}`);
  console.log(`  computed = ${computed}`);
  const a = Buffer.from(computed);
  const b = Buffer.from(VECTOR_HMAC);
  if (a.length === b.length && crypto.timingSafeEqual(a, b)) {
    console.log("PASS: this kit's HMAC-SHA256 + base64 implementation matches the pinned known-answer");
    console.log("      (byte-identical to shwtk.py — cross-language parity).");
    return 0;
  }
  console.log("FAIL: computed signature does not match the pinned known-answer — re-download the kit.");
  return 1;
}

function cmdList() {
  const manifest = loadManifest();
  const stems = Object.keys(manifest).sort();
  if (stems.length === 0) {
    console.log("(no fixtures found)");
    return 1;
  }
  console.log("bundled real-shape fixtures (reconstructed from Shopify's docs —");
  console.log("see fixtures/PROVENANCE.md):");
  for (const stem of stems) {
    const entry = manifest[stem];
    const ct = entry.content_type || "?";
    const topic = entry.topic || "?";
    console.log(`  ${stem.padEnd(20)}  topic=${String(topic).padEnd(20)}  ${ct}`);
  }
  return 0;
}

function usage() {
  console.log("usage: shwtk <fire|vector|list> [options]");
  console.log("  fire   --url URL --fixture NAME [--secret-env NAME] [--forge|--unsigned|--tamper|--malformed]");
  console.log("  vector");
  console.log("  list");
}

async function main() {
  const argv = process.argv.slice(2);
  const cmd = argv[0];
  const rest = argv.slice(1);
  let code;
  switch (cmd) {
    case "fire":
      code = await cmdFire(rest);
      break;
    case "vector":
      code = cmdVector();
      break;
    case "list":
      code = cmdList();
      break;
    case undefined:
    case "-h":
    case "--help":
      usage();
      code = cmd === undefined ? 2 : 0;
      break;
    default:
      fail(`error: unknown command '${cmd}'`);
  }
  process.exit(code);
}

module.exports = {
  shopifyHmac,
  buildRequest,
  postRequest,
  normalFirePass,
  rejectedFirePass,
  listFixtures,
  loadManifest,
  VECTOR_SECRET,
  VECTOR_BODY,
  VECTOR_HMAC,
};

if (require.main === module) {
  main();
}
