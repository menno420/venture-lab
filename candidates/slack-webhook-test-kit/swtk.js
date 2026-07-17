#!/usr/bin/env node
"use strict";
/*
 * Slack Webhook Test Kit (swtk) — Node stdlib port of swtk.py.
 *
 * Fire REAL-shape signed Slack requests at your local endpoint and check your
 * handler the way Slack actually behaves. Stdlib only (crypto, fs, path, http,
 * https, url) — no npm install, no build step. Node 14+.
 *
 * Subcommands (mirror swtk.py exactly):
 *   fire            --url --fixture [--secret-env] [--forge|--unsigned|--stale|--tamper]
 *   check-challenge [--url] [--secret-env]
 *   vector
 *   list
 *
 * The Slack signing secret is read from an environment variable (NAME only —
 * the value is never stored, logged, or echoed). Default: SLACK_SIGNING_SECRET.
 */
const crypto = require("crypto");
const fs = require("fs");
const path = require("path");
const http = require("http");
const https = require("https");
const { URL } = require("url");

const FIXTURES_DIR = path.join(__dirname, "fixtures");
const DEFAULT_SECRET_ENV = "SLACK_SIGNING_SECRET";
const REPLAY_WINDOW_SECONDS = 300;
const SLACK_UA = "Slackbot 1.0 (+https://api.slack.com/robots)";

// Slack's OWN published worked example (api.slack.com "Verifying requests from
// Slack"). Public documentation values — NOT a real secret.
const VECTOR_SECRET = "8f742231b10e8888abcd99yyyzzz85a5";
const VECTOR_TIMESTAMP = 1531420618;
const VECTOR_BODY = Buffer.from(
  "token=xyzz0WbapA4vBCDEFasx0q6G&team_id=T1DC2JH3J&team_domain=testteamnow" +
    "&channel_id=G8PSS9T3V&channel_name=foobar&user_id=U2CERLKJA&user_name=roadrunner" +
    "&command=%2Fwebhook-collect&text=&response_url=https%3A%2F%2Fhooks.slack.com%2Fcommands" +
    "%2FT1DC2JH3J%2F397700885554%2F96rGlfmibIGlgcZRskXaIFfN" +
    "&trigger_id=398738663015.47445629121.803a0bc887a14d10d2c447fce8b6703c",
  "utf-8"
);
const VECTOR_SIGNATURE = "v0=a2114d57b48eac39b9ad189dd8316235a7b4a8d21a10bd27519666489c69b503";

// --------------------------------------------------------------------------- //
// Signature — the real X-Slack-Signature v0 scheme.
// basestring = "v0:" + timestamp + ":" + RAW body ; sig = "v0=" + hex hmac-sha256
// --------------------------------------------------------------------------- //
function slackSignature(rawBody, secret, timestamp) {
  const ts = Math.trunc(timestamp);
  const basestring = Buffer.concat([Buffer.from(`v0:${ts}:`, "utf-8"), rawBody]);
  const digest = crypto.createHmac("sha256", Buffer.from(secret, "utf-8")).update(basestring).digest("hex");
  return "v0=" + digest;
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
  return name.replace(/\.(json|txt)$/, "");
}

function fixtureFile(stem) {
  stem = stemOf(stem);
  for (const ext of [".json", ".txt"]) {
    const p = path.join(FIXTURES_DIR, stem + ext);
    if (fs.existsSync(p)) return p;
  }
  fail(`error: fixture not found: ${stem}. Run \`swtk list\` to see bundled fixtures.`);
}

function loadFixture(stem) {
  return fs.readFileSync(fixtureFile(stem));
}

function contentTypeFor(stem) {
  const m = loadManifest();
  stem = stemOf(stem);
  if (!(stem in m)) {
    fail(`error: fixture '${stem}' has no Content-Type in fixtures/MANIFEST.json.`);
  }
  return m[stem];
}

function listFixtures() {
  return Object.keys(loadManifest()).sort();
}

// --------------------------------------------------------------------------- //
// HTTP + verdicts
// --------------------------------------------------------------------------- //
function buildRequest(rawBody, contentType, opts = {}) {
  // opts: { secret, timestamp, signBody, forge }
  const ts = opts.timestamp !== undefined && opts.timestamp !== null
    ? Math.trunc(opts.timestamp)
    : Math.floor(Date.now() / 1000);
  const headers = { "Content-Type": contentType, "User-Agent": SLACK_UA };
  if (opts.secret !== undefined && opts.secret !== null) {
    const signingSecret = opts.forge ? opts.secret + "__swtk_forged__" : opts.secret;
    const toSign = opts.signBody !== undefined && opts.signBody !== null ? opts.signBody : rawBody;
    headers["X-Slack-Request-Timestamp"] = String(ts);
    headers["X-Slack-Signature"] = slackSignature(toSign, signingSecret, ts);
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
    req.on("error", reject);
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
      `error: environment variable ${envName} is not set. Export your Slack signing ` +
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
    flags: new Set(["forge", "unsigned", "stale", "tamper"]),
    opts: new Set(["url", "fixture", "secret-env"]),
  });
  if (!o.url) fail("error: fire requires --url");
  if (!o.fixture) fail("error: fire requires --fixture");
  const modes = [o.forge, o.unsigned, o.stale, o.tamper].filter(Boolean);
  if (modes.length > 1) fail("error: --forge / --unsigned / --stale / --tamper are mutually exclusive.");
  const secretEnv = o.secret_env || DEFAULT_SECRET_ENV;
  const payload = loadFixture(o.fixture);
  const contentType = contentTypeFor(o.fixture);
  const secret = requireSecret(secretEnv);

  if (o.forge) {
    const [body, headers] = buildRequest(payload, contentType, { secret, forge: true });
    const [status, resp] = await postRequest(o.url, body, headers);
    console.log(`[forge]    POST ${o.url}  (${o.fixture})  ->  HTTP ${status}`);
    printBody(resp);
    if (rejectedFirePass(status)) {
      console.log("PASS: handler rejected the wrong-secret request (signature verification is working).");
      return 0;
    }
    console.log("FAIL: handler ACCEPTED a request signed with the wrong secret (HTTP 2xx). It is not");
    console.log("      verifying X-Slack-Signature — anyone who knows your URL can post fake requests.");
    return 1;
  }

  if (o.unsigned) {
    const [body, headers] = buildRequest(payload, contentType, {});
    const [status, resp] = await postRequest(o.url, body, headers);
    console.log(`[unsigned] POST ${o.url}  (${o.fixture})  ->  HTTP ${status}`);
    printBody(resp);
    if (rejectedFirePass(status)) {
      console.log("PASS: handler rejected the unsigned request (missing signature fails closed).");
      return 0;
    }
    console.log("FAIL: handler ACCEPTED a request with NO X-Slack-Signature header.");
    return 1;
  }

  if (o.stale) {
    const oldTs = Math.floor(Date.now() / 1000) - (REPLAY_WINDOW_SECONDS + 300);
    const [body, headers] = buildRequest(payload, contentType, { secret, timestamp: oldTs });
    const [status, resp] = await postRequest(o.url, body, headers);
    console.log(`[stale]    POST ${o.url}  (${o.fixture})  ts=${oldTs}  ->  HTTP ${status}`);
    printBody(resp);
    if (rejectedFirePass(status)) {
      console.log("PASS: handler rejected the stale-timestamp request (replay window is enforced).");
      return 0;
    }
    console.log(`FAIL: handler ACCEPTED a request outside the ±${REPLAY_WINDOW_SECONDS}s window — a captured`);
    console.log("      request replays forever. Reject anything older than 5 minutes first.");
    return 1;
  }

  if (o.tamper) {
    const tampered = Buffer.concat([payload, Buffer.from(" ", "utf-8")]);
    const [body, headers] = buildRequest(tampered, contentType, { secret, signBody: payload });
    const [status, resp] = await postRequest(o.url, body, headers);
    console.log(`[tamper]   POST ${o.url}  (${o.fixture})  ->  HTTP ${status}`);
    printBody(resp);
    if (rejectedFirePass(status)) {
      console.log("PASS: handler rejected the tampered body (it hashes the RAW bytes it received).");
      return 0;
    }
    console.log("FAIL: handler ACCEPTED a body that differs from the one the signature covers.");
    return 1;
  }

  const [body, headers] = buildRequest(payload, contentType, { secret });
  const [status, resp] = await postRequest(o.url, body, headers);
  console.log(`[fire]     POST ${o.url}  (${o.fixture}, ${contentType})  ->  HTTP ${status}`);
  printBody(resp);
  if (normalFirePass(status)) {
    console.log("PASS: handler accepted the correctly-signed request.");
    return 0;
  }
  console.log(`FAIL: handler did not accept a correctly-signed request (HTTP ${status}, expected 2xx).`);
  return 1;
}

async function cmdCheckChallenge(argv) {
  const o = parseOpts(argv, { flags: new Set(), opts: new Set(["url", "secret-env"]) });
  const secretEnv = o.secret_env || DEFAULT_SECRET_ENV;
  const payload = JSON.parse(loadFixture("url_verification").toString("utf-8"));
  const challenge = payload.challenge;
  console.log("fixture: url_verification");
  console.log(`  payload "type"      = ${repr(payload.type)}`);
  console.log(`  payload "challenge" = ${repr(challenge)}`);
  console.log("GOTCHA: when you save an Events API Request URL, Slack immediately POSTs a");
  console.log("  url_verification request. Your endpoint MUST answer 200 and echo the");
  console.log('  `challenge` value back (as text/plain, or as JSON {"challenge": ...}).');
  console.log("  If you don't, Slack marks the URL unverified and NO events are ever delivered.");
  if (o.url) {
    const secret = requireSecret(secretEnv);
    const [body, headers] = buildRequest(loadFixture("url_verification"),
      contentTypeFor("url_verification"), { secret });
    const [status, resp] = await postRequest(o.url, body, headers);
    console.log(`\n[challenge] POST ${o.url}  ->  HTTP ${status}`);
    printBody(resp);
    const echoed = challenge != null && resp.indexOf(challenge) !== -1;
    if (normalFirePass(status) && echoed) {
      console.log("PASS: handler answered 2xx AND echoed the challenge value.");
      return 0;
    }
    if (!normalFirePass(status)) console.log(`FAIL: handler did not answer 2xx (HTTP ${status}).`);
    else console.log("FAIL: handler answered 2xx but did NOT echo the challenge — Slack will not verify the URL.");
    return 1;
  }
  return 0;
}

function cmdVector() {
  const computed = slackSignature(VECTOR_BODY, VECTOR_SECRET, VECTOR_TIMESTAMP);
  console.log("Slack's published worked example (Verifying requests from Slack docs):");
  console.log(`  signing secret = ${repr(VECTOR_SECRET)}`);
  console.log(`  timestamp      = ${VECTOR_TIMESTAMP}`);
  console.log(`  body           = ${repr(VECTOR_BODY.slice(0, 48).toString("utf-8"))}…`);
  console.log(`  expected       = ${VECTOR_SIGNATURE}`);
  console.log(`  computed       = ${computed}`);
  const a = Buffer.from(computed);
  const b = Buffer.from(VECTOR_SIGNATURE);
  if (a.length === b.length && crypto.timingSafeEqual(a, b)) {
    console.log("PASS: this kit's HMAC-SHA256 implementation matches Slack's own published example.");
    return 0;
  }
  console.log("FAIL: computed signature does not match Slack's published example — re-download the kit.");
  return 1;
}

function cmdList() {
  const manifest = loadManifest();
  const stems = Object.keys(manifest).sort();
  if (stems.length === 0) {
    console.log("(no fixtures found)");
    return 1;
  }
  console.log("bundled real-shape fixtures (reconstructed from Slack's docs —");
  console.log("see fixtures/PROVENANCE.md):");
  for (const stem of stems) {
    const ct = manifest[stem];
    let hint = "";
    try {
      const raw = loadFixture(stem);
      if (ct === "application/json") {
        hint = `type=${JSON.parse(raw.toString("utf-8")).type}`;
      } else if (raw.slice(0, 8).toString("utf-8") === "payload=") {
        hint = "interactivity (payload=<json>)";
      } else {
        hint = "slash command (form fields)";
      }
    } catch (e) {
      hint = "";
    }
    console.log(`  ${stem.padEnd(32)}  ${ct.padEnd(35)}  ${hint}`);
  }
  return 0;
}

function repr(v) {
  if (v === null || v === undefined) return "None";
  return `'${v}'`;
}

function usage() {
  console.log("usage: swtk <fire|check-challenge|vector|list> [options]");
  console.log("  fire            --url URL --fixture NAME [--secret-env NAME] [--forge|--unsigned|--stale|--tamper]");
  console.log("  check-challenge [--url URL] [--secret-env NAME]");
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
    case "check-challenge":
      code = await cmdCheckChallenge(rest);
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
  slackSignature,
  buildRequest,
  postRequest,
  normalFirePass,
  rejectedFirePass,
  listFixtures,
  loadManifest,
  REPLAY_WINDOW_SECONDS,
  VECTOR_SECRET,
  VECTOR_TIMESTAMP,
  VECTOR_BODY,
  VECTOR_SIGNATURE,
};

if (require.main === module) {
  main();
}
