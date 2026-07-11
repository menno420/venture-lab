# Netherlands vs Philippines — Which Is Easier & More Beneficial to Run Online Monetization From?

> **Status:** `reference` — owner-directed research (2026-07-11)
>
> **Disclaimer:** Research summary compiled from public sources on 2026-07-11. This is **not legal or tax advice**. Rules change and individual circumstances vary — verify with a qualified accountant/tax advisor before acting. See [netherlands.md](./netherlands.md) and [philippines.md](./philippines.md) for the underlying cited detail.

## The decisive framing: "run from" is dominated by TAX RESIDENCY

You generally pay tax **where you (the person) live**, not where the platform, the buyer, or the bank sits. Choosing to "run from" a country is really choosing where you are **tax-resident** — and you cannot move that liability by merely registering a name or opening an account abroad while still living somewhere else. Both countries tax residents on income; NL additionally has **emigration/substance rules** that resist paper relocation. So the honest question is not "which flag looks better" but **"where does the owner genuinely live, and given that, what is the setup?"** Two scenarios follow.

## Side-by-side (small scale, first few thousand €/₱ of digital revenue)

| Dimension | Netherlands (resident) | Philippines (resident) |
|---|---|---|
| **Start friction** | Register eenmanszaak at KvK, **one-time €85.15**; VAT numbers auto-issued. | BIR registration (TIN, COR, books of accounts) + DTI trade-name if using a brand (₱230–₱2,030); **₱500 annual fee removed (RA 11976)**. More steps/paperwork. |
| **Tax at small scale** | Box 1 progressive; entrepreneur deductions (zelfstandigenaftrek €1,200/2026 phasing to €900, startersaftrek €2,123, MKB 12.70%) but gated by 1,225-hr criterion. **KOR** exempts BTW under €20,000 turnover. | **8% flat on gross above ₱250,000** in lieu of income + percentage tax — first ₱250,000 effectively tax-free; simple and often low. Below ₱3M no VAT. |
| **Payment-rail access** | **Easy** — Stripe, Mollie, PayPal, Gumroad SEPA all pay a euro IBAN directly. | **Hard** — **Stripe unavailable** to PH businesses; Gumroad direct-bank **excludes PH**, pays via **PayPal in USD**; extra hops (PayPal/Payoneer → GCash/bank) each add fees; Oct-2024 PayPal/Gumroad suspension shows platform-dependency risk. |
| **Compliance overhead** | VAT/OSS rules, 14-day digital-withdrawal waiver, DAC7 reporting (>€2,000 / >30 tx). Well-documented, digital-first (Mijn Belastingdienst). | Internet Transactions Act (RA 11967) merchant disclosure; RR 16-2023 withholding (0.5% above ₱500k on PH platforms); newer, still-settling rules; more manual filing. |
| **Scaling friction** | OSS handles EU-wide VAT cleanly; deductions taper as revenue grows; strong banking. | Cross ₱3M → mandatory 12% VAT + reversion from 8%; FX/USD-banking friction persists; rail access remains the bottleneck. |
| **Currency** | Earn/settle in **EUR** natively; minimal FX. | Earn in **USD** on foreign platforms, convert to **PHP** — recurring FX + transfer fees. |

## Bottom line (research, not legal advice)

- **If the owner is resident in the Netherlands:** **NL wins decisively for starting.** Rail access is frictionless (Stripe/Mollie/PayPal/Gumroad all direct to a euro account), setup is a single €85.15 registration, the **KOR** removes VAT hassle under €20,000, and everything is EUR-native. The real cost is only that NL is a higher-tax, higher-compliance environment as you scale — but at the "first dollar / first few thousand" stage that barely bites. **Recommendation: for an NL-resident owner, run from NL.**
- **If the owner is genuinely resident in the Philippines:** **PH is cheaper on tax at small scale** (the 8% flat with the first ₱250,000 effectively tax-free is very attractive, and the ₱500 annual fee is gone), **but payment rails are the binding constraint** — no direct Stripe, Gumroad pays PH only via PayPal in USD with real suspension-risk history, and every USD→PHP hop leaks fees. The tax saving can be outweighed by rail fragility and FX friction for a digital-download lane.
- **You cannot cherry-pick** "PH tax + NL rails" by paper alone: tax follows genuine residency, and NL rails/Stripe expect an NL/EU entity with local substance. A US-LLC-for-Stripe workaround exists but adds its own US filing/compliance layer and does not change where the owner is taxed.

**Overall, for the likely case (owner with NL ties, EUR-native, needing reliable digital-checkout rails now): the Netherlands is both easier and more beneficial to run from** — the payment-rail advantage is decisive for a Gumroad/Stripe digital-download business, and it outweighs the Philippines' lower small-scale tax. The Philippines only pulls ahead if the owner is *actually* living there, is comfortable with USD/PayPal-centric collection, and prioritizes minimizing tax on modest gross revenue over rail reliability.

## 3–5 questions to confirm with a professional (accountant / tax advisor)

1. **Residency:** Where is the owner tax-resident today, and would a move to PH actually shift NL tax liability (NL emigration/substance and any exit-tax exposure)?
2. **KOR vs OSS interaction (NL):** Can the owner use the €20,000 KOR domestically while making cross-border EU B2C digital sales, and at what point does the €10,000 OSS threshold force customer-country VAT? (flagged not-verified)
3. **PH rail reality:** Is Gumroad currently paying PH sellers reliably (direct bank vs PayPal-USD) post the Oct-2024 PayPal suspension, and what is the true net fee stack USD→PHP? (flagged not-verified)
4. **US-LLC-for-Stripe:** If a PH-resident owner forms a US LLC to access Stripe, what US (ECI/1040-NR, state) and PH filing obligations follow, and does it create any PH permanent-establishment/CFC issues?
5. **8% election (PH):** For a purely self-employed digital creator, is the 8% flat clearly better than graduated + percentage tax at the expected revenue, and how is foreign-platform income substantiated to the BIR?

## Key numbers — confirmed vs not-verified

**Confirmed (cited):** NL VAT 21%; KOR €20,000; OSS €10,000; KvK €85.15 (2026); zelfstandigenaftrek €1,200 (2026, phasing to €900/2027); startersaftrek €2,123; MKB 12.70%; urencriterium 1,225 hrs; DAC7 >€2,000/>30 tx. PH: ₱500 ARF removed (RA 11976); 8% flat above ₱250,000 (≤₱3M, non-VAT); percentage tax 3%; VAT 12% at ₱3M; RR 16-2023 = 0.5% effective above ₱500,000; DTI BN ₱200–₱2,000 +₱30 DST; **Stripe not available to PH**; Gumroad direct-bank excludes PH (pays via PayPal USD).

**Not verified (2026-07-11):** NL KOR/OSS interaction detail and exact KOR invoice wording; NL 2026 deduction figures rest on pages that could not be opened directly (corroborated across sources); PH — exact Gumroad PH payout minimum ($100 vs $10) and whether PH was added to Gumroad's post-2025 direct-bank list; whether RR 16-2023 withholding reaches foreign non-registered platforms like Gumroad; operational status of the DTI E-Commerce Bureau merchant-registration mechanics.
