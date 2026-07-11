#!/usr/bin/env node
"use strict";
/*
 * Stripe Webhook Test Kit (swtk) — Node stdlib port of swtk.py.
 *
 * Fire REAL-shape signed Stripe events at your local webhook endpoint and check
 * your handler the way Stripe actually behaves. Stdlib only (crypto, fs, path,
 * http, https, url) — no npm install, no build step. Node 14+.
 *
 * Subcommands (mirror swtk.py exactly):
 *   fire        --url --fixture [--secret-env] [--forge] [--timestamp]
 *   check-email --fixture
 *   lint-url    <url>
 *   list
 *
 * The webhook signing secret is read from an environment variable (NAME only —
 * the value is never stored, logged, or echoed). Default: SWTK_WEBHOOK_SECRET.
 */
const crypto = require("crypto");
const fs = require("fs");
const path = require("path");
const http = require("http");
const https = require("https");
const { URL } = require("url");

const FIXTURES_DIR = path.join(__dirname, "fixtures");
const DEFAULT_SECRET_ENV = "SWTK_WEBHOOK_SECRET";

// Stripe expands exactly one placeholder in success_url / cancel_url.
const VALID_URL_PLACEHOLDERS = new Set(["CHECKOUT_SESSION_ID"]);
const PLACEHOLDER_RE = /\{([A-Za-z0-9_]+)\}/g;

// stripe-go webhook/client.go: DefaultTolerance = 300 * time.Second
const DEFAULT_TOLERANCE = 300;

// --------------------------------------------------------------------------- //
// Signature — the real Stripe-Signature scheme (t=<ts>,v1=<hex hmac-sha256>).
// --------------------------------------------------------------------------- //
function stripeSignature(payload, secret, timestamp) {
  const ts = Math.trunc(timestamp);
  const signedPayload = Buffer.concat([Buffer.from(String(ts) + ".", "utf-8"), payload]);
  const v1 = crypto.createHmac("sha256", Buffer.from(secret, "utf-8")).update(signedPayload).digest("hex");
  return `t=${ts},v1=${v1}`;
}

// --------------------------------------------------------------------------- //
// Fixtures
// --------------------------------------------------------------------------- //
function fixturePath(name) {
  return path.join(FIXTURES_DIR, name.endsWith(".json") ? name : name + ".json");
}

function loadFixture(name) {
  const p = fixturePath(name);
  if (!fs.existsSync(p)) {
    fail(`error: fixture not found: ${path.basename(p)}. Run \`swtk list\` to see bundled fixtures.`);
  }
  return fs.readFileSync(p);
}

function listFixtures() {
  if (!fs.existsSync(FIXTURES_DIR)) return [];
  return fs.readdirSync(FIXTURES_DIR).filter((n) => n.endsWith(".json")).sort();
}

// --------------------------------------------------------------------------- //
// The two gotcha checks
// --------------------------------------------------------------------------- //
function resolveBuyerEmail(sessionObj) {
  const details = sessionObj.customer_details || {};
  if (details.email) return [details.email, "customer_details.email"];
  if (sessionObj.customer_email) return [sessionObj.customer_email, "customer_email"];
  return [null, null];
}

function lintSuccessUrl(url) {
  const issues = [];
  const found = [];
  let m;
  PLACEHOLDER_RE.lastIndex = 0;
  while ((m = PLACEHOLDER_RE.exec(url)) !== null) {
    found.push(m[1]);
  }
  for (const token of found) {
    if (!VALID_URL_PLACEHOLDERS.has(token)) {
      issues.push({
        level: "error",
        msg:
          `invalid placeholder {${token}} — Stripe never expands this; ` +
          `it reaches the buyer's browser verbatim. Only {CHECKOUT_SESSION_ID} is supported.`,
      });
    }
  }
  if (!found.includes("CHECKOUT_SESSION_ID")) {
    issues.push({
      level: "warning",
      msg:
        "no {CHECKOUT_SESSION_ID} placeholder — the success page will not receive the " +
        "session id, so it cannot resolve the buyer (the email is not on the URL).",
    });
  }
  return issues;
}

// --------------------------------------------------------------------------- //
// HTTP + verdicts
// --------------------------------------------------------------------------- //
function postEvent(urlStr, payload, sigHeader, timeoutMs = 10000) {
  return new Promise((resolve, reject) => {
    let u;
    try {
      u = new URL(urlStr);
    } catch (e) {
      reject(new Error(`invalid url: ${urlStr}`));
      return;
    }
    const lib = u.protocol === "https:" ? https : http;
    const options = {
      method: "POST",
      hostname: u.hostname,
      port: u.port || (u.protocol === "https:" ? 443 : 80),
      path: u.pathname + u.search,
      headers: {
        "Content-Type": "application/json",
        "Content-Length": Buffer.byteLength(payload),
        "Stripe-Signature": sigHeader,
      },
    };
    const req = lib.request(options, (res) => {
      const chunks = [];
      res.on("data", (c) => chunks.push(c));
      res.on("end", () => resolve([res.statusCode, Buffer.concat(chunks).toString("utf-8")]));
    });
    req.on("error", reject);
    req.setTimeout(timeoutMs, () => {
      req.destroy(new Error("request timed out"));
    });
    req.write(payload);
    req.end();
  });
}

function normalFirePass(status) {
  return status >= 200 && status < 300;
}

function forgedFirePass(status) {
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
      `error: environment variable ${envName} is not set. Export your Stripe webhook ` +
        `signing secret (whsec_...) into it — the value is read from the env and never stored.`
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

// Hand-rolled option parsing: collect --flag value / --flag=value / bare flags.
function parseOpts(argv, spec) {
  // spec: { flags: Set<string> (boolean), opts: Set<string> (take value) }
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
    flags: new Set(["forge"]),
    opts: new Set(["url", "fixture", "secret-env", "timestamp"]),
  });
  if (!o.url) fail("error: fire requires --url");
  if (!o.fixture) fail("error: fire requires --fixture");
  const secretEnv = o.secret_env || DEFAULT_SECRET_ENV;
  const payload = loadFixture(o.fixture);
  const secret = requireSecret(secretEnv);
  const ts = o.timestamp !== undefined ? parseInt(o.timestamp, 10) : Math.floor(Date.now() / 1000);

  if (o.forge) {
    const sig = stripeSignature(payload, secret + "__swtk_forged__", ts);
    const [status, body] = await postEvent(o.url, payload, sig);
    console.log(`[forge] POST ${o.url}  ->  HTTP ${status}`);
    printBody(body);
    if (forgedFirePass(status)) {
      console.log("PASS: handler rejected the forged event (signature verification is working).");
      return 0;
    }
    console.log("FAIL: handler ACCEPTED a forged event (HTTP 2xx). It is not verifying the");
    console.log("      Stripe-Signature — anyone who knows your endpoint URL can post fake events.");
    return 1;
  }

  const sig = stripeSignature(payload, secret, ts);
  const [status, body] = await postEvent(o.url, payload, sig);
  console.log(`[fire]  POST ${o.url}  ->  HTTP ${status}`);
  printBody(body);
  if (normalFirePass(status)) {
    console.log("PASS: handler accepted the correctly-signed event.");
    return 0;
  }
  console.log(`FAIL: handler did not accept a correctly-signed event (HTTP ${status}, expected 2xx).`);
  return 1;
}

function cmdCheckEmail(argv) {
  const o = parseOpts(argv, { flags: new Set(), opts: new Set(["fixture"]) });
  if (!o.fixture) fail("error: check-email requires --fixture");
  const event = JSON.parse(loadFixture(o.fixture).toString("utf-8"));
  const obj = (event.data && event.data.object) || {};
  const top = obj.customer_email !== undefined ? obj.customer_email : null;
  const detailsEmail = (obj.customer_details && obj.customer_details.email) || null;
  const [email, source] = resolveBuyerEmail(obj);

  console.log(`fixture: ${o.fixture}`);
  console.log(`  event.data.object.customer_email           = ${repr(top)}`);
  console.log(`  event.data.object.customer_details.email   = ${repr(detailsEmail)}`);
  if (email === null) {
    console.log("  resolved buyer email                       = <none>");
    console.log("FAIL: no buyer email resolvable from this event.");
    return 1;
  }
  console.log(`  resolved buyer email                       = ${repr(email)}  (from ${source})`);
  if (top === null && source === "customer_details.email") {
    console.log("GOTCHA CONFIRMED: top-level customer_email is null on this real completion.");
    console.log("  A handler that reads only event.data.object.customer_email gets None here");
    console.log("  and silently drops the sale. Read customer_details.email first.");
  }
  return 0;
}

function cmdLintUrl(argv) {
  const o = parseOpts(argv, { flags: new Set(), opts: new Set() });
  const url = o._[0];
  if (!url) fail("error: lint-url requires a url argument");
  const issues = lintSuccessUrl(url);
  const errors = issues.filter((i) => i.level === "error");
  console.log(`success_url: ${url}`);
  if (issues.length === 0) {
    console.log("OK: uses {CHECKOUT_SESSION_ID}, no invalid placeholders.");
    return 0;
  }
  for (const i of issues) {
    console.log(`  [${i.level}] ${i.msg}`);
  }
  if (errors.length) {
    console.log("FAIL: invalid placeholder(s) present.");
    return 1;
  }
  console.log("OK (with warnings): no invalid placeholders.");
  return 0;
}

function cmdList() {
  const names = listFixtures();
  if (names.length === 0) {
    console.log("(no fixtures found)");
    return 1;
  }
  console.log("bundled real-shape fixtures (see fixtures/PROVENANCE.md):");
  for (const n of names) {
    try {
      const ev = JSON.parse(fs.readFileSync(path.join(FIXTURES_DIR, n)).toString("utf-8"));
      console.log(`  ${n.padEnd(44)}  type=${ev.type}`);
    } catch (e) {
      console.log(`  ${n}`);
    }
  }
  return 0;
}

// Python-repr-ish for None/strings, to mirror swtk.py output.
function repr(v) {
  if (v === null || v === undefined) return "None";
  return `'${v}'`;
}

function usage() {
  console.log("usage: swtk <fire|check-email|lint-url|list> [options]");
  console.log("  fire        --url URL --fixture NAME [--secret-env NAME] [--forge] [--timestamp N]");
  console.log("  check-email --fixture NAME");
  console.log("  lint-url    URL");
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
    case "check-email":
      code = cmdCheckEmail(rest);
      break;
    case "lint-url":
      code = cmdLintUrl(rest);
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
  stripeSignature,
  resolveBuyerEmail,
  lintSuccessUrl,
  postEvent,
  normalFirePass,
  forgedFirePass,
  listFixtures,
  VALID_URL_PLACEHOLDERS,
  DEFAULT_TOLERANCE,
};

if (require.main === module) {
  main();
}
