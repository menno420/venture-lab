# 2026-07-12 — Market State Dashboard: anchor-rotation primary use case + rotation cost math + Intel context

> **Status:** `complete`

## 💡 Session idea
Extend the existing `candidates/market-state-dashboard/` spec with the owner's PRIMARY
Phase-1 use case: an **anchor holding** (default INTC — the owner holds ~€5–6K of Intel at
DEGIRO, default = HOLD). Spec (A) the anchor's own descriptive state panel + a mechanical,
ex-ante **rotation trigger** that surfaces DESCRIPTIVE-strength rotation candidates from a
watchlist (Phase-1 ranks by descriptive strength ONLY — no predictive ranking, since no
strategy has cleared the forward test); (B) a prominent, honest **rotation cost / breakeven**
block (4-leg cycle: sell INTC → buy OTHER → sell OTHER → rebuy INTC), with real DEGIRO US-stock
fees + slippage + gap-risk + an NL box-3 tax note; and (C) a NEW `intel-context-2026-07.md`
file — current, fully-cited web research on Intel, headed **CONTEXT — NOT A RECOMMENDATION**.
RAILS: research/spec only — no accounts, no trades, no financial recommendations. Cross-repo
READS of menno420/trading-strategy only; the PR touches venture-lab ONLY; control/ untouched.

## Previous-session review
The prior slice (`2026-07-12-candidate-market-state-dashboard.md`) wrote
`candidates/market-state-dashboard/INTAKE.md` — a spec-only intake for a $0-hosted static
DECISION-SUPPORT SCREENER for the owner's MANUAL DEGIRO trading (no bot, no advice), with
PHASED HONESTY (Phase 1 descriptive-only; Phase 2 signal overlays ship EMPTY, gated on a passed
forward test). That card also recorded the correct standing result from the trading-strategy
lane: the one-shot holdout was SPENT and cleared **no strategy for deployment** — of 13
candidates, 1 CONFIRMED (AAPL-donchian, t=0.02, "deep inside noise"), 2 HOLDOUT-BEAT, 10
HOLDOUT-MISS, verdict **"No candidate holds a finding label"**. This slice extends the SAME
candidate with the anchor-rotation use case; it touches only files under
`candidates/market-state-dashboard/` plus this card. It does NOT touch `control/`,
`.github/workflows/`, other candidates, or the ledger (spec-only candidate → INTAKE-standalone
per repo convention).

## Model
- **📊 Model:** opus-4.8 · worker · venture/intake

## Deliverables
- candidates/market-state-dashboard/INTAKE.md — new §G anchor-rotation use case + §H rotation
  cost/breakeven math (edit of existing spec)
- candidates/market-state-dashboard/intel-context-2026-07.md — NEW cited research file
  (CONTEXT — NOT A RECOMMENDATION)

## Outcome
Extended `candidates/market-state-dashboard/INTAKE.md` with **§G (anchor-rotation PRIMARY
Phase-1 use case)** and **§H (rotation cost/breakeven math)**, and added a NEW
`intel-context-2026-07.md` research file.

**§G** specs a configurable anchor (default INTC) with its OWN descriptive-state panel (regime,
band position daily/4h/1h, ATR% range, reversal-relevant descriptive facts — gap, distance-to-band,
band re-entry, NO predictions); a mechanical **ex-ante rotation trigger** (anchor below lower daily
band OR downtrend regime); **descriptive-only** candidate ranking (predictive ranking withheld —
0/13 cleared the holdout); an **always-displayed rotation hurdle** next to every candidate; a
**reversal-watch panel** (descriptive facts only); and the two owner situations — (a) rotate ~€5K
out of a mechanically-weak Intel and rebuy later, (b) trade Intel itself on a flagged reversal.

**§H** computes the full **4-leg cycle** (sell INTC→buy OTHER→sell OTHER→rebuy INTC) on €5K with
**verified DEGIRO US fees** (€1 commission + €1 handling = €2/leg → €8/cycle = 0.16%; 0.25% FX
conditional), a conservative **5 bps/leg slippage floor** (0.20%, ~€10), giving a **base cycle cost
~€18 = ~0.36%** (up to ~1.36% if auto-FX hits all 4 legs). **Breakeven stated plainly:** the switch
must beat holding Intel by MORE than ~0.36% (a multiple of it in practice). **Gap risk** quantified
off INTC's **~5% ATR%** (out-of-Intel timing risk dwarfs friction; Q2 earnings 2026-07-23 is a
binary event in-window). **NL box-3 note:** taxes wealth not per-trade gains → churn no direct tax
penalty; pending werkelijk-rendement reform flagged — general info, not tax advice.

**intel-context-2026-07.md** — fully cited (every claim + URL + accessed 2026-07-12), headed
**CONTEXT — NOT A RECOMMENDATION**, and opening with the standing program result (0/13 cleared;
active signals lost to buy-and-hold after costs). Covers price ~$109.60 / 52-wk $18.97–$142.35;
Q1 FY2026 (rev $13.6B +7%, foundry loss $2.4B, GM 39.4%, GAAP net loss $4.28B); analyst band
~$85–$102 (HSBC $200 outlier); Q2 earnings 2026-07-23 + Panther Lake/18A catalysts; ATR% ~5%.
**Marked unverified:** the exact ±1–2%-day frequency count (no citable histogram) — gave the
defensible ATR-grounded inference instead; **no figure fabricated.**

RAILS honoured: research/spec only, no accounts/trades/recommendations, Intel material clearly
labelled CONTEXT. Cross-repo READS of trading-strategy only; PR touches venture-lab ONLY; `control/`
untouched. First commit = born-red card; this final commit flips it complete.
`python3 bootstrap.py check --strict` green.
