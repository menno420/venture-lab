#!/usr/bin/env node
"use strict";
/*
 * JWT Auth Test Kit (jatk) — Node stdlib port of jatk.py.
 *
 * Point it at your own JWT-protected endpoint and prove your token verification
 * is SECURE: it ACCEPTS a valid, correctly-signed, unexpired token with correct
 * claims, and REJECTS the critical auth-bypass classes — alg:none, a
 * tampered/wrong-key token, the RS256->HS256 algorithm-confusion attack, an
 * expired token, a not-yet-valid token, a wrong/missing aud, a wrong/missing iss,
 * and a structurally-malformed token. Stdlib only (http, crypto, fs, path, url) —
 * no npm install, no build step. Node 14+.
 *
 * NOT a webhook signature kit, NOT the idempotency/rate-limit/pagination kit — it
 * tests JWT VERIFIER SECURITY. Grounded in RFC 7519 (JWT), RFC 7515 (JWS), and
 * RFC 8725 ("JWT BCP") + the alg:none and RS256->HS256 confusion attacks. See
 * fixtures/PROVENANCE.md. Honest scope: HS256 + the attack classes above, stdlib
 * only; real RS256/ES256 signature-math verify is out of scope (the confusion
 * check needs no RSA verify — it forges an HS256 token over the public-key bytes).
 *
 * Subcommands (mirror jatk.py exactly):
 *   check                    --url [--fixture] [--secret] [--pubkey] [--path] [--aud] [--iss] [--now]
 *   <property>               same flags, run a single property (names below)
 *   demo                     bundled reference stubs, zero accounts, loud banner
 *   list
 * Property names: valid-accepted, alg-none-rejected, signature-rejected,
 *   alg-confusion-rejected, expired-rejected, not-yet-valid-rejected,
 *   audience-enforced, issuer-enforced, malformed-rejected.
 */
const http = require("http");
const crypto = require("crypto");
const fs = require("fs");
const path = require("path");
const { URL } = require("url");

const FIXTURES_DIR = path.join(__dirname, "fixtures");
const DEFAULT_FIXTURE = "hs256_bearer";
const DEFAULT_SECRET = Buffer.from("jatk-demo-hs256-secret-not-a-real-secret");
const WRONG_KEY = Buffer.from("jatk-attacker-guessed-wrong-key");

function fail(msg) {
  process.stderr.write(msg + "\n");
  process.exit(2);
}

// --------------------------------------------------------------------------- //
// Fixtures
// --------------------------------------------------------------------------- //
function loadManifest() {
  const m = JSON.parse(fs.readFileSync(path.join(FIXTURES_DIR, "MANIFEST.json"), "utf-8"));
  delete m._comment;
  return m;
}
function entryFor(stem) {
  const m = loadManifest();
  stem = stem.replace(/\.json$/, "");
  if (!(stem in m)) fail(`error: fixture '${stem}' has no entry in fixtures/MANIFEST.json. Run \`jatk list\`.`);
  return m[stem];
}
function listFixtures() {
  return Object.keys(loadManifest()).sort();
}
function specFrom(stem) {
  const e = entryFor(stem);
  return {
    path: e.path || "/protected",
    authHeader: e.auth_header || "Authorization",
    authScheme: e.auth_scheme || "Bearer",
    expectedAud: e.expected_aud || null,
    expectedIss: e.expected_iss || null,
    subject: e.subject || "jatk-demo-user-001",
  };
}
function loadPubkey() {
  const p = path.join(FIXTURES_DIR, "test_public_key.pem");
  return fs.existsSync(p) ? fs.readFileSync(p) : Buffer.alloc(0);
}

// --------------------------------------------------------------------------- //
// JWT primitives — mint the valid token and every attack token
// --------------------------------------------------------------------------- //
function b64url(buf) {
  return Buffer.from(buf).toString("base64").replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, "");
}
function unb64url(s) {
  return Buffer.from(s.replace(/-/g, "+").replace(/_/g, "/"), "base64");
}
function seg(obj) {
  return b64url(Buffer.from(JSON.stringify(sortKeys(obj))));
}
function sortKeys(obj) {
  if (Array.isArray(obj) || obj === null || typeof obj !== "object") return obj;
  const out = {};
  for (const k of Object.keys(obj).sort()) out[k] = obj[k];
  return out;
}
function mint(claims, key, alg = "HS256", typ = "JWT") {
  const h = seg({ alg, typ });
  const p = seg(claims);
  const signingInput = Buffer.from(h + "." + p);
  let sig = "";
  if (alg !== "none") sig = b64url(crypto.createHmac("sha256", key).update(signingInput).digest());
  return `${h}.${p}.${sig}`;
}
function baseClaims(spec, now) {
  const c = { sub: spec.subject, iat: Math.floor(now - 60), nbf: Math.floor(now - 60), exp: Math.floor(now + 3600) };
  if (spec.expectedAud) c.aud = spec.expectedAud;
  if (spec.expectedIss) c.iss = spec.expectedIss;
  return c;
}
function attackTokens(spec, secret, pubkey, now) {
  const valid = baseClaims(spec, now);
  const v = mint(valid, secret);
  const [h, p, s] = v.split(".");
  const pTampered = p.slice(0, -1) + (p.slice(-1) !== "A" ? "A" : "B");
  const tampered = `${h}.${pTampered}.${s}`;

  const expired = Object.assign({}, valid, { iat: Math.floor(now - 7200), nbf: Math.floor(now - 7200), exp: Math.floor(now - 3600) });
  const future = Object.assign({}, valid, { iat: Math.floor(now + 3600), nbf: Math.floor(now + 3600), exp: Math.floor(now + 7200) });
  const wrongAud = Object.assign({}, valid, { aud: "jatk-attacker-different-audience" });
  const missingAud = Object.assign({}, valid); delete missingAud.aud;
  const wrongIss = Object.assign({}, valid, { iss: "https://attacker.example/" });
  const missingIss = Object.assign({}, valid); delete missingIss.iss;

  const twoSeg = mint(valid, secret).split(".").slice(0, 2).join(".");
  const fourSeg = mint(valid, secret) + ".extra";
  const badB64 = "@@@bad@@@." + p + "." + s;

  return {
    valid: mint(valid, secret),
    alg_none: mint(valid, Buffer.alloc(0), "none"),
    tampered,
    wrong_key: mint(valid, WRONG_KEY),
    confusion: mint(valid, pubkey),
    expired: mint(expired, secret),
    not_yet_valid: mint(future, secret),
    wrong_aud: mint(wrongAud, secret),
    missing_aud: mint(missingAud, secret),
    wrong_iss: mint(wrongIss, secret),
    missing_iss: mint(missingIss, secret),
    malformed_notjwt: "this-is-not-a-jwt",
    malformed_twoseg: twoSeg,
    malformed_fourseg: fourSeg,
    malformed_badb64: badB64,
  };
}

// --------------------------------------------------------------------------- //
// HTTP
// --------------------------------------------------------------------------- //
function fire(baseUrl, method, p, headers, timeoutMs = 10000) {
  return new Promise((resolve) => {
    let u;
    try {
      u = new URL(baseUrl.replace(/\/$/, "") + p);
    } catch (e) {
      resolve([0, "<invalid url>"]);
      return;
    }
    const opts = { method, hostname: u.hostname, port: u.port, path: u.pathname + u.search, headers: headers || {} };
    const req = http.request(opts, (res) => {
      const chunks = [];
      res.on("data", (c) => chunks.push(c));
      res.on("end", () => resolve([res.statusCode, Buffer.concat(chunks).toString("utf-8")]));
    });
    req.on("error", (e) => resolve([0, `<no HTTP response: ${e.message}>`]));
    req.setTimeout(timeoutMs, () => { req.destroy(); resolve([0, "<no HTTP response: timeout>"]); });
    req.end();
  });
}
function is2xx(s) {
  return s >= 200 && s < 300;
}
async function fireToken(baseUrl, spec, token) {
  const headers = {};
  headers[spec.authHeader] = `${spec.authScheme} ${token}`;
  return fire(baseUrl, "GET", spec.path, headers);
}

// --------------------------------------------------------------------------- //
// Suite plumbing
// --------------------------------------------------------------------------- //
function mkTokens(spec, secret, pubkey, now) {
  return attackTokens(spec, secret, pubkey, now == null ? Date.now() / 1000 : now);
}
async function rejectCheck(baseUrl, spec, tokens, keys, okMsg, bypassWord) {
  const accepted = [];
  for (const k of keys) {
    const [status] = await fireToken(baseUrl, spec, tokens[k]);
    if (is2xx(status)) accepted.push(`${k} (HTTP ${status})`);
  }
  if (accepted.length) {
    return [false, `the endpoint ACCEPTED ${bypassWord}: ${accepted.join(", ")} — it must reject these with 401/403, not serve the protected resource.`];
  }
  return [true, okMsg];
}

// Properties — each returns [passed(bool|null), detail]. null == SKIP.
async function checkValidAccepted(baseUrl, spec, secret, pubkey, now) {
  const tokens = mkTokens(spec, secret, pubkey, now);
  const [status, body] = await fireToken(baseUrl, spec, tokens.valid);
  if (!is2xx(status)) return [false, `the endpoint REJECTED a valid, correctly-signed, unexpired token (HTTP ${status}) — check --secret matches your server's HS256 key and --aud/--iss match. Body: ${body.slice(0, 160)}`];
  return [true, `a valid HS256 token with correct claims was accepted (HTTP ${status})`];
}
async function checkAlgNone(baseUrl, spec, secret, pubkey, now) {
  return rejectCheck(baseUrl, spec, mkTokens(spec, secret, pubkey, now), ["alg_none"],
    "an `alg:none` unsigned token was rejected — the classic bypass is closed", "an `alg:none` unsigned token");
}
async function checkSignature(baseUrl, spec, secret, pubkey, now) {
  return rejectCheck(baseUrl, spec, mkTokens(spec, secret, pubkey, now), ["tampered", "wrong_key"],
    "a tampered token and a wrong-key token were both rejected — the signature is actually verified", "a token with an invalid signature");
}
async function checkConfusion(baseUrl, spec, secret, pubkey, now) {
  if (!pubkey || !pubkey.length) return [null, "SKIP: no public-key blob available to craft the confusion token (pass --pubkey <file>)."];
  return rejectCheck(baseUrl, spec, mkTokens(spec, secret, pubkey, now), ["confusion"],
    "an HS256 token signed with the public-key bytes was rejected — the verifier pins its algorithm and key (no RS256->HS256 confusion)",
    "an algorithm-confusion token (HS256 signed with the RSA/EC public key)");
}
async function checkExpired(baseUrl, spec, secret, pubkey, now) {
  return rejectCheck(baseUrl, spec, mkTokens(spec, secret, pubkey, now), ["expired"],
    "an expired token (exp in the past) was rejected", "an expired token (exp in the past)");
}
async function checkNotYetValid(baseUrl, spec, secret, pubkey, now) {
  return rejectCheck(baseUrl, spec, mkTokens(spec, secret, pubkey, now), ["not_yet_valid"],
    "a not-yet-valid token (nbf/iat in the future) was rejected", "a not-yet-valid token (nbf/iat in the future)");
}
async function checkAudience(baseUrl, spec, secret, pubkey, now) {
  if (!spec.expectedAud) return [null, "SKIP: no expected audience configured (fixture `expected_aud` empty / --aud unset)."];
  return rejectCheck(baseUrl, spec, mkTokens(spec, secret, pubkey, now), ["wrong_aud", "missing_aud"],
    `a wrong \`aud\` and a missing \`aud\` were both rejected — the audience '${spec.expectedAud}' is enforced`, "a token with the wrong/missing audience");
}
async function checkIssuer(baseUrl, spec, secret, pubkey, now) {
  if (!spec.expectedIss) return [null, "SKIP: no expected issuer configured (fixture `expected_iss` empty / --iss unset)."];
  return rejectCheck(baseUrl, spec, mkTokens(spec, secret, pubkey, now), ["wrong_iss", "missing_iss"],
    `a wrong \`iss\` and a missing \`iss\` were both rejected — the issuer '${spec.expectedIss}' is enforced`, "a token with the wrong/missing issuer");
}
async function checkMalformed(baseUrl, spec, secret, pubkey, now) {
  const tokens = mkTokens(spec, secret, pubkey, now);
  const keys = Object.keys(tokens).filter((k) => k.startsWith("malformed_"));
  return rejectCheck(baseUrl, spec, tokens, keys,
    `all ${keys.length} structurally-malformed tokens (bad base64url, wrong segment count) were rejected — the parser fails closed`, "a structurally-malformed token");
}

const CHECKS = [
  ["valid-accepted", checkValidAccepted],
  ["alg-none-rejected", checkAlgNone],
  ["signature-rejected", checkSignature],
  ["alg-confusion-rejected", checkConfusion],
  ["expired-rejected", checkExpired],
  ["not-yet-valid-rejected", checkNotYetValid],
  ["audience-enforced", checkAudience],
  ["issuer-enforced", checkIssuer],
  ["malformed-rejected", checkMalformed],
];
const CHECKS_BY_NAME = Object.fromEntries(CHECKS);

function label(passed) {
  return passed === null ? "SKIP" : passed ? "PASS" : "FAIL";
}
function printResult(name, passed, detail) {
  console.log(`[${label(passed)}] ${name.padEnd(24)} ${detail}`);
}
async function runSuite(baseUrl, spec, secret, pubkey, now) {
  let failures = 0;
  for (const [name, fn] of CHECKS) {
    const [passed, detail] = await fn(baseUrl, spec, secret, pubkey, now);
    printResult(name, passed, detail);
    if (passed === false) failures++;
  }
  return failures;
}

// --------------------------------------------------------------------------- //
// Reference stubs (Node) for the demo — mirror stub_handler*.py
// --------------------------------------------------------------------------- //
const DEMO_AUD = "jatk-demo-api";
const DEMO_ISS = "jatk-demo-issuer";
const LEEWAY = 60;

function bearer(req) {
  const raw = req.headers["authorization"] || "";
  const parts = raw.split(" ");
  if (parts.length !== 2 || parts[0].toLowerCase() !== "bearer" || !parts[1].trim()) return null;
  return parts[1].trim();
}
function sendJSON(res, code, obj) {
  const data = Buffer.from(JSON.stringify(obj));
  res.writeHead(code, { "Content-Type": "application/json", "Content-Length": data.length });
  res.end(data);
}
function correctStub(secret, pubkey, expectedAud, expectedIss) {
  return http.createServer((req, res) => {
    const u = new URL(req.url, "http://x");
    if (req.method !== "GET" || u.pathname !== "/protected") return sendJSON(res, 404, { error: "not found" });
    const token = bearer(req);
    if (token === null) return sendJSON(res, 401, { error: "missing bearer token" });
    try {
      const parts = token.split(".");
      if (parts.length !== 3) throw new Error("malformed: not 3 segments");
      const header = JSON.parse(unb64url(parts[0]).toString("utf-8"));
      const alg = header.alg;
      if (alg === "none" || alg == null) throw new Error("alg_none");
      if (alg !== "HS256") throw new Error("alg_not_allowed");
      const signingInput = Buffer.from(parts[0] + "." + parts[1]);
      const sig = unb64url(parts[2]);
      const expected = crypto.createHmac("sha256", secret).update(signingInput).digest();
      if (sig.length !== expected.length || !crypto.timingSafeEqual(sig, expected)) throw new Error("bad_signature");
      const claims = JSON.parse(unb64url(parts[1]).toString("utf-8"));
      const now = Date.now() / 1000;
      if (claims.exp != null && now > Number(claims.exp) + LEEWAY) throw new Error("expired");
      if (claims.nbf != null && now + LEEWAY < Number(claims.nbf)) throw new Error("not_yet_valid");
      if (claims.iat != null && now + LEEWAY < Number(claims.iat)) throw new Error("not_yet_valid");
      if (expectedAud) {
        const aud = claims.aud;
        const ok = aud === expectedAud || (Array.isArray(aud) && aud.includes(expectedAud));
        if (!ok) throw new Error("bad_audience");
      }
      if (expectedIss && claims.iss !== expectedIss) throw new Error("bad_issuer");
      return sendJSON(res, 200, { ok: true, sub: claims.sub });
    } catch (e) {
      return sendJSON(res, 401, { error: "invalid token", reason: String(e.message) });
    }
  });
}
function naiveStub(secret, pubkey) {
  return http.createServer((req, res) => {
    const u = new URL(req.url, "http://x");
    if (req.method !== "GET" || u.pathname !== "/protected") return sendJSON(res, 404, { error: "not found" });
    const token = bearer(req);
    if (token === null) return sendJSON(res, 401, { error: "missing bearer token" });
    try {
      const parts = token.split(".");
      if (parts.length !== 3) throw new Error("not three segments");
      const header = JSON.parse(unb64url(parts[0]).toString("utf-8"));
      const claims = JSON.parse(unb64url(parts[1]).toString("utf-8"));
      const alg = header.alg;
      if (alg === "none" || alg == null) return sendJSON(res, 200, { ok: true, sub: claims.sub }); // BUG 1
      const signingInput = Buffer.from(parts[0] + "." + parts[1]);
      const sig = unb64url(parts[2]);
      for (const key of [secret, pubkey]) {                                                        // BUG 2 (confusion)
        if (key && key.length) {
          const expected = crypto.createHmac("sha256", key).update(signingInput).digest();
          if (sig.length === expected.length && crypto.timingSafeEqual(sig, expected)) {
            return sendJSON(res, 200, { ok: true, sub: claims.sub });                               // BUG 3+4: no time/aud/iss
          }
        }
      }
      throw new Error("signature did not match secret or public key");
    } catch (e) {
      return sendJSON(res, 401, { error: "invalid token", detail: String(e.message) });
    }
  });
}
function listen(server) {
  return new Promise((resolve) => server.listen(0, "127.0.0.1", () => resolve(server.address().port)));
}

// --------------------------------------------------------------------------- //
// CLI
// --------------------------------------------------------------------------- //
function parseArgs(argv) {
  const args = { _: [] };
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a.startsWith("--")) {
      const k = a.slice(2);
      const next = argv[i + 1];
      if (next === undefined || next.startsWith("--")) args[k] = "";
      else { args[k] = next; i++; }
    } else args._.push(a);
  }
  return args;
}
function requireUrl(a) {
  if (!a.url) fail("error: --url is required (your endpoint base, e.g. http://localhost:8000)");
  return a.url;
}
function resolveSpec(a) {
  const spec = specFrom(a.fixture || DEFAULT_FIXTURE);
  if (a.path) spec.path = a.path;
  if (a.aud !== undefined) spec.expectedAud = a.aud || null;
  if (a.iss !== undefined) spec.expectedIss = a.iss || null;
  const secret = a.secret ? Buffer.from(a.secret) : DEFAULT_SECRET;
  const pubkey = a.pubkey ? fs.readFileSync(a.pubkey) : loadPubkey();
  const now = a.now ? parseFloat(a.now) : null;
  return { spec, secret, pubkey, now };
}
async function cmdCheck(a) {
  const url = requireUrl(a);
  const { spec, secret, pubkey, now } = resolveSpec(a);
  console.log(`JWT Auth Test Kit — checking ${url}`);
  console.log(`  ${spec.authScheme} token at GET ${spec.path}   aud=${JSON.stringify(spec.expectedAud)} iss=${JSON.stringify(spec.expectedIss)}`);
  console.log(`  (set --secret to your server's HS256 key so the kit can mint tokens; --aud/--iss to what your server enforces)\n`);
  const failures = await runSuite(url, spec, secret, pubkey, now);
  console.log("");
  if (failures === 0) { console.log("ALL PROPERTIES PASS/SKIP — this endpoint accepts a valid token and rejects the attack classes tested."); return 0; }
  console.log(`${failures} PROPERTY(IES) FAILED — see the FAIL lines above and GOTCHAS.md.`);
  return 1;
}
async function cmdSingle(a, name) {
  const url = requireUrl(a);
  const { spec, secret, pubkey, now } = resolveSpec(a);
  const [passed, detail] = await CHECKS_BY_NAME[name](url, spec, secret, pubkey, now);
  printResult(name, passed, detail);
  return passed === false ? 1 : 0;
}
function cmdList() {
  const m = loadManifest();
  console.log("bundled fixtures (endpoint/claim templates — see fixtures/PROVENANCE.md):");
  for (const stem of listFixtures()) {
    const e = m[stem];
    console.log(`  ${stem.padEnd(16)}  ${(e.auth_scheme || "Bearer")} @ GET ${(e.path || "/protected").padEnd(12)}  aud=${e.expected_aud || "-"} iss=${e.expected_iss || "-"}  — ${e.note || ""}`);
  }
  return 0;
}
async function cmdDemo() {
  console.log("=".repeat(74));
  console.log("  JATK DEMO MODE — bundled REFERENCE stubs, in-process, on localhost.");
  console.log("  NO real endpoint, NO accounts, NO money. This proves the kit works");
  console.log("  before you point `jatk check --url` at your own app.");
  console.log("=".repeat(74));
  const spec = specFrom(DEFAULT_FIXTURE);
  const secret = DEFAULT_SECRET;
  const pubkey = loadPubkey();
  const correct = correctStub(secret, pubkey, spec.expectedAud, spec.expectedIss);
  const naive = naiveStub(secret, pubkey);
  const cport = await listen(correct);
  const nport = await listen(naive);
  let cf, nf;
  try {
    console.log(`\n--- CORRECT stub (alg allowlist [HS256], exp/nbf/aud/iss enforced) — expect ALL PASS ---`);
    cf = await runSuite(`http://127.0.0.1:${cport}`, spec, secret, pubkey);
    console.log(`\n--- NAIVE stub (accepts alg:none, confusion, expired, future, wrong aud/iss) — expect the kit to FLAG it ---`);
    nf = await runSuite(`http://127.0.0.1:${nport}`, spec, secret, pubkey);
  } finally {
    correct.close();
    naive.close();
  }
  console.log("\n" + "=".repeat(74));
  if (cf === 0 && nf > 0) {
    console.log(`  DEMO OK: correct stub passed all properties; naive stub flagged on ${nf} property(ies).`);
    console.log("  The kit distinguishes a secure JWT verifier from a bypassable one.");
    console.log("=".repeat(74));
    return 0;
  }
  console.log(`  DEMO UNEXPECTED: correct failures=${cf}, naive failures=${nf} (expected 0 and >0).`);
  console.log("=".repeat(74));
  return 1;
}
async function main() {
  const argv = process.argv.slice(2);
  const cmd = argv[0];
  const a = parseArgs(argv.slice(1));
  let rc = 0;
  if (cmd === "check") rc = await cmdCheck(a);
  else if (cmd === "demo") rc = await cmdDemo();
  else if (cmd === "list") rc = cmdList();
  else if (CHECKS_BY_NAME[cmd]) rc = await cmdSingle(a, cmd);
  else fail("usage: jatk {check|valid-accepted|alg-none-rejected|signature-rejected|alg-confusion-rejected|expired-rejected|not-yet-valid-rejected|audience-enforced|issuer-enforced|malformed-rejected|demo|list} [--url ...] [--secret ...] [--pubkey ...] [--aud ...] [--iss ...]");
  process.exit(rc);
}

main();
