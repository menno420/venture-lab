# ⚑ Owner queue — every decision and click, in one list

> GENERATED FILE — regenerate with `ocq.py derive`; edit the
> gate files, never this file. A stale copy of this file is a
> bug in the workflow, never in the gate files.

The agents performed NONE of the actions below — every item is an owner click or an owner choice, queued and pre-chewed. Decisions come first (each with a bolded default so “agree” is a one-word reply); the pure click-run sequences follow.

## 1. Decisions — pick the default or override

### D1 — CLI v2.0 Release — Version pick

- **WHAT:** ⚑ Version pick: publish as 2.0.0 stable (default — the breaking changes are documented and the migration guide shipped) or as 2.0.0-rc.1 first — maintainer's call.
- **WHERE:** `RELEASE-GATE.md` @ OWNER-GATE step 1
- **DEFAULT:** **2.0.0 stable**
- **UNBLOCKS:** the “CLI v2.0 Release” click-run continuing past this pick

## 2. Click-run — mechanical owner clicks, paste-ready

### CLI v2.0 Release — `RELEASE-GATE.md` @ OWNER-GATE checklist

- [ ] **WHAT:** version pick confirmed (2.0.0 stable (default)). · **DEFAULT:** **2.0.0 stable** (executes its D-item above) · **UNBLOCKS:** the next click in this sequence
- [ ] **WHAT:** package published to the registry with YOUR token. · **UNBLOCKS:** the next click in this sequence
- [ ] **WHAT:** release notes pasted + release published on the repo host (VERIFIED-WHEN: the release URL loads and npm info shows 2.0.0). · **UNBLOCKS:** the next click in this sequence

## 3. Manual review — gate files the parser could not read reliably

*(none — every input parsed clean)*
