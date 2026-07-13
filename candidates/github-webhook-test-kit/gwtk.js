#!/usr/bin/env node
"use strict";
/*
 * GitHub Webhook Test Kit (gwtk) — Node stdlib port of gwtk.py.
 *
 * Fire REAL-shape signed GitHub webhook deliveries at your local endpoint and
 * check your handler the way GitHub actually behaves. Stdlib only (crypto, fs,
 * path, http, https, url) — no npm install, no build step. Node 14+.
 *
 * Subcommands (mirror gwtk.py exactly):
 *   fire        --url --fixture [--secret-env] [--forge|--unsigned|--sha1-only|--replay]
 *               [--form] [--delivery GUID]
 *   check-event --fixture
 *   vector
 *   list
 *
 * The webhook secret is read from an environment variable (NAME only — the
 * value is never stored, logged, or echoed). Default: GWTK_WEBHOOK_SECRET.
 */
const crypto = require("crypto");
const fs = require("fs");
const path = require("path");
const http = require("http");
const https = require("https");
const { URL } = require("url");

const FIXTURES_DIR = path.join(__dirname, "fixtures");
const DEFAULT_SECRET_ENV = "GWTK_WEBHOOK_SECRET";

// GitHub's official known-answer test (docs source: github/docs
// validating-webhook-deliveries.md — see fixtures/PROVENANCE.md).
// Public documentation values, not a real secret.
const VECTOR_SECRET = "It's a Secret to Everybody";
const VECTOR_PAYLOAD = Buffer.from("Hello, World!", "utf-8");
const VECTOR_SIG_256 =
  "sha256=757107ea0eb2509fc211221cce984b8a37570b6d7586c22c46f4379c8b043e17";

// --------------------------------------------------------------------------- //
// Signatures — the real X-Hub-Signature-256 / legacy X-Hub-Signature schemes:
// HMAC hex digest of the RAW request body, keyed with the webhook secret.
// NO timestamp component exists (unlike Stripe) — see GOTCHAS.md #3.
// --------------------------------------------------------------------------- //
function hubSignature256(payload, secret) {
  const digest = crypto.createHmac("sha256", Buffer.from(secret, "utf-8")).update(payload).digest("hex");
  return `sha256=${digest}`;
}

function hubSignatureSha1(payload, secret) {
  const digest = crypto.createHmac("sha1", Buffer.from(secret, "utf-8")).update(payload).digest("hex");
  return `sha1=${digest}`;
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
    fail(`error: fixture not found: ${path.basename(p)}. Run \`gwtk list\` to see bundled fixtures.`);
  }
  return fs.readFileSync(p);
}

function loadEvents() {
  const events = JSON.parse(fs.readFileSync(path.join(FIXTURES_DIR, "EVENTS.json")).toString("utf-8"));
  delete events._comment;
  return events;
}

function eventForFixture(name) {
  const stem = name.endsWith(".json") ? name.slice(0, -5) : name;
  const events = loadEvents();
  if (!(stem in events)) {
    fail(
      `error: fixture '${stem}' has no X-GitHub-Event mapping in fixtures/EVENTS.json — ` +
        `add one (the event name travels only in the header, never in the payload).`
    );
  }
  return events[stem];
}

function listFixtures() {
  if (!fs.existsSync(FIXTURES_DIR)) return [];
  return fs
    .readdirSync(FIXTURES_DIR)
    .filter((n) => n.endsWith(".json") && n !== "EVENTS.json")
    .sort();
}

// --------------------------------------------------------------------------- //
// Request building + HTTP + verdicts (mirrors gwtk.py)
// --------------------------------------------------------------------------- //
function buildRequest(payload, event, delivery, secret, form, sha1Only) {
  let body, contentType;
  if (form) {
    // GitHub form deliveries: payload=<urlencoded json>; the signature covers
    // THESE raw form bytes, not the JSON inside.
    body = Buffer.from("payload=" + encodeURIComponent(payload.toString("utf-8")).replace(/%20/g, "+"), "utf-8");
    contentType = "application/x-www-form-urlencoded";
  } else {
    body = payload;
    contentType = "application/json";
  }
  const headers = {
    "Content-Type": contentType,
    "User-Agent": "GitHub-Hookshot/gwtk",
    "X-GitHub-Event": event,
    "X-GitHub-Delivery": delivery,
  };
  if (secret !== null && secret !== undefined) {
    if (!sha1Only) headers["X-Hub-Signature-256"] = hubSignature256(body, secret);
    headers["X-Hub-Signature"] = hubSignatureSha1(body, secret);
  }
  return [body, headers];
}

function postDelivery(urlStr, body, headers, timeoutMs = 10000) {
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
      headers: Object.assign({ "Content-Length": Buffer.byteLength(body) }, headers),
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
      `error: environment variable ${envName} is not set. Export your webhook ` +
        `secret token into it — the value is read from the env and never stored.`
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

function randomUuid() {
  if (crypto.randomUUID) return crypto.randomUUID();
  const b = crypto.randomBytes(16);
  b[6] = (b[6] & 0x0f) | 0x40;
  b[8] = (b[8] & 0x3f) | 0x80;
  const h = b.toString("hex");
  return `${h.slice(0, 8)}-${h.slice(8, 12)}-${h.slice(12, 16)}-${h.slice(16, 20)}-${h.slice(20)}`;
}

// --------------------------------------------------------------------------- //
// Commands
// --------------------------------------------------------------------------- //
async function cmdFire(argv) {
  const o = parseOpts(argv, {
    flags: new Set(["forge", "unsigned", "sha1-only", "replay", "form"]),
    opts: new Set(["url", "fixture", "secret-env", "delivery"]),
  });
  if (!o.url) fail("error: fire requires --url");
  if (!o.fixture) fail("error: fire requires --fixture");
  const modes = [o.forge, o.unsigned, o.sha1_only, o.replay].filter(Boolean);
  if (modes.length > 1) fail("error: --forge / --unsigned / --sha1-only / --replay are mutually exclusive.");
  const secretEnv = o.secret_env || DEFAULT_SECRET_ENV;
  const payload = loadFixture(o.fixture);
  const secret = requireSecret(secretEnv);
  const event = eventForFixture(o.fixture);
  const delivery = o.delivery || randomUuid();

  if (o.forge) {
    const [body, headers] = buildRequest(payload, event, delivery, secret + "__gwtk_forged__", o.form, false);
    const [status, resp] = await postDelivery(o.url, body, headers);
    console.log(`[forge]     POST ${o.url}  (${event})  ->  HTTP ${status}`);
    printBody(resp);
    if (rejectedFirePass(status)) {
      console.log("PASS: handler rejected the forged delivery (signature verification is working).");
      return 0;
    }
    console.log("FAIL: handler ACCEPTED a forged delivery (HTTP 2xx). It is not verifying");
    console.log("      X-Hub-Signature-256 — anyone who knows your endpoint URL can post fake events.");
    return 1;
  }

  if (o.unsigned) {
    const [body, headers] = buildRequest(payload, event, delivery, null, o.form, false);
    const [status, resp] = await postDelivery(o.url, body, headers);
    console.log(`[unsigned]  POST ${o.url}  (${event})  ->  HTTP ${status}`);
    printBody(resp);
    if (rejectedFirePass(status)) {
      console.log("PASS: handler rejected the unsigned delivery (missing signature fails closed).");
      return 0;
    }
    console.log("FAIL: handler ACCEPTED a delivery with NO signature header. If your webhook has a");
    console.log("      secret configured, a missing X-Hub-Signature-256 must be rejected, not skipped.");
    return 1;
  }

  if (o.sha1_only) {
    const [body, headers] = buildRequest(payload, event, delivery, secret, o.form, true);
    const [status, resp] = await postDelivery(o.url, body, headers);
    console.log(`[sha1-only] POST ${o.url}  (${event})  ->  HTTP ${status}`);
    printBody(resp);
    if (rejectedFirePass(status)) {
      console.log("PASS: handler rejected the SHA-1-only delivery (no downgrade path).");
      return 0;
    }
    console.log("FAIL: handler ACCEPTED a delivery carrying only the legacy X-Hub-Signature (SHA-1).");
    console.log("      GitHub always sends X-Hub-Signature-256 when a secret is set — an attacker who");
    console.log("      strips the sha256 header should not be able to route you onto the weaker check.");
    return 1;
  }

  if (o.replay) {
    const [body, headers] = buildRequest(payload, event, delivery, secret, o.form, false);
    const [status1, resp1] = await postDelivery(o.url, body, headers);
    const [status2, resp2] = await postDelivery(o.url, body, headers);
    console.log(`[replay]    POST ${o.url}  (${event})  delivery ${delivery}`);
    console.log(`        1st -> HTTP ${status1}`);
    printBody(resp1);
    console.log(`        2nd -> HTTP ${status2} (identical bytes, identical GUID)`);
    printBody(resp2);
    console.log("NOTE: GitHub's signature scheme has NO timestamp — a replayed delivery verifies");
    console.log("      forever. HTTP alone cannot show whether you PROCESSED it twice: dedupe on");
    console.log("      X-GitHub-Delivery (redeliveries reuse the original GUID) and check your own");
    console.log("      side effects. The bundled stub_handler.py shows the dedupe pattern.");
    if (normalFirePass(status1) && status2 < 500) {
      console.log("PASS (transport): both deliveries handled without a 5xx. Idempotency is on you.");
      return 0;
    }
    console.log(`FAIL: a correctly-signed (re)delivery crashed or was mis-rejected (HTTP ${status1} then ${status2}).`);
    return 1;
  }

  const [body, headers] = buildRequest(payload, event, delivery, secret, o.form, false);
  const [status, resp] = await postDelivery(o.url, body, headers);
  const mode = o.form ? "form" : "json";
  console.log(`[fire/${mode}] POST ${o.url}  (${event})  ->  HTTP ${status}`);
  printBody(resp);
  if (normalFirePass(status)) {
    console.log("PASS: handler accepted the correctly-signed delivery.");
    return 0;
  }
  console.log(`FAIL: handler did not accept a correctly-signed delivery (HTTP ${status}, expected 2xx).`);
  if (o.form) {
    console.log("      (--form signs the RAW urlencoded body, exactly as GitHub does. If you verify");
    console.log("      the decoded JSON instead of the raw request bytes, this is the failure you see.)");
  }
  return 1;
}

function cmdCheckEvent(argv) {
  const o = parseOpts(argv, { flags: new Set(), opts: new Set(["fixture"]) });
  if (!o.fixture) fail("error: check-event requires --fixture");
  const payload = JSON.parse(loadFixture(o.fixture).toString("utf-8"));
  const event = eventForFixture(o.fixture);
  const action = payload.action !== undefined ? payload.action : null;
  console.log(`fixture: ${o.fixture}`);
  console.log(`  X-GitHub-Event header (the ONLY place the event name travels) = '${event}'`);
  console.log(`  payload top-level "action"                                    = ${action === null ? "None" : `'${action}'`}`);
  if (event === "ping") {
    console.log(`  payload "zen"                                                 = '${payload.zen}'`);
    console.log("GOTCHA: ping is the FIRST delivery every new webhook receives (sent on creation).");
    console.log('  It has no "action" and no event-specific resource — a handler that assumes');
    console.log('  e.g. payload["pull_request"] exists will 500 before your webhook ever works.');
    console.log("  Return 2xx on ping.");
    return 0;
  }
  if (action === null) {
    console.log(`GOTCHA: '${event}' deliveries have NO "action" field at all. Routing on`);
    console.log('  payload["action"] alone breaks here — route on the X-GitHub-Event header first.');
    return 0;
  }
  console.log(`GOTCHA: "action": '${action}' is NOT unique to '${event}' — many event types share`);
  console.log("  action values (e.g. \"created\", \"completed\"). Route on the X-GitHub-Event header");
  console.log("  first, THEN on action; a handler switching on action alone conflates event types.");
  return 0;
}

function cmdVector() {
  const computed = hubSignature256(VECTOR_PAYLOAD, VECTOR_SECRET);
  console.log("GitHub's published test vector (validating-webhook-deliveries docs):");
  console.log(`  secret   = "${VECTOR_SECRET}"`);
  console.log(`  payload  = "${VECTOR_PAYLOAD.toString("utf-8")}"`);
  console.log(`  expected = ${VECTOR_SIG_256}`);
  console.log(`  computed = ${computed}`);
  if (crypto.timingSafeEqual(Buffer.from(computed, "utf-8"), Buffer.from(VECTOR_SIG_256, "utf-8"))) {
    console.log("PASS: this kit's HMAC-SHA256 implementation matches GitHub's own published constant.");
    return 0;
  }
  console.log("FAIL: computed signature does not match GitHub's published vector — do not trust");
  console.log("      this copy of the kit; re-download it.");
  return 1;
}

function cmdList() {
  const names = listFixtures();
  if (names.length === 0) {
    console.log("(no fixtures found)");
    return 1;
  }
  const events = loadEvents();
  console.log("bundled real-shape fixtures (vendored from GitHub's own example set —");
  console.log("see fixtures/PROVENANCE.md):");
  for (const n of names) {
    const stem = n.slice(0, -5);
    try {
      const payload = JSON.parse(fs.readFileSync(path.join(FIXTURES_DIR, n)).toString("utf-8"));
      const suffix = payload.action !== undefined ? ` action=${payload.action}` : " (no action field)";
      console.log(`  ${n.padEnd(36)}  X-GitHub-Event=${events[stem] || "?"}${suffix}`);
    } catch (e) {
      console.log(`  ${n}`);
    }
  }
  return 0;
}

function usage() {
  console.log("usage: gwtk <fire|check-event|vector|list> [options]");
  console.log("  fire        --url URL --fixture NAME [--secret-env NAME]");
  console.log("              [--forge|--unsigned|--sha1-only|--replay] [--form] [--delivery GUID]");
  console.log("  check-event --fixture NAME");
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
    case "check-event":
      code = cmdCheckEvent(rest);
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
  hubSignature256,
  hubSignatureSha1,
  buildRequest,
  postDelivery,
  normalFirePass,
  rejectedFirePass,
  listFixtures,
  loadEvents,
  VECTOR_SECRET,
  VECTOR_PAYLOAD,
  VECTOR_SIG_256,
};

if (require.main === module) {
  main();
}
