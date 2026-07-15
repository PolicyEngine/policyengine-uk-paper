# Evidence map (v1 outline)

This paper's v1 milestone (PolicyEngine/policyengine-uk-paper#1) is an
outline with every planned claim mapped to evidence that already exists, or
marked `\todo{evidence needed}` where it does not. This file is the
section-by-section index; the `\todo{}` markers in `paper/sections/*.tex`
are the authoritative, in-context list (`grep -rn 'todo{' paper/sections/`).

## What exists (evidence found during the 2026-07-04 survey)

| Section | Evidence | Source |
| --- | --- | --- |
| Model / program coverage | 45 programs (38 complete, 7 partial) across 9 agencies | `policyengine-uk` `policyengine_uk/programs.yaml` |
| Data / base survey | Family Resources Survey, `verified_start_year` as early as 2019 | `policyengine_uk/programs.yaml` |
| Data / enhancement | SPI-informed synthetic high-income FRS rows via QRF imputation, upweighted by calibration | `populace` `packages/populace-build/src/populace/build/uk_runtime/spi_support.py` |
| Data / calibration targets | Target definitions incl. `income_tax` in-simulation check | `populace` `packages/populace-build/src/populace/build/uk_runtime/local_targets.py` |
| Data / uprating | Per-variable OBR uprating index table (HBAI income concepts) | `policyengine-uk` `docs/book/validation/hbai.md` |
| Validation / aggregates | 3-way PolicyEngine vs. UKMOD vs. official comparison, income tax/NI/UC/Child Benefit/Tax Credits/Housing Benefit/Pension Credit, 2023-2025 | `policyengine-uk` `docs/book/validation/validation.ipynb` |
| Validation / aggregates, maintenance history | Notebook kept current against successive UKMOD country reports | `policyengine-uk` issues #724, #300, #212, #545 (confirmed via `gh api`) |
| Validation / individual income tax | SPI 2020/21 match-rate table: 92.7% of records within £10; 4 named discrepancy clusters | `policyengine-uk` `docs/book/validation/spi-validation.ipynb` |
| Validation / individual income tax, prior public writeup | "Autumn 2023 model calibration" | `https://policyengine.org/uk/research/uk-calibration-2023-q4` (confirmed live, HTTP 200) |
| Validation / student loans | FRS-reported vs. modelled repayments; aggregate "reasonably aligned," weaker individual correlation, 5 named factors | `policyengine-uk` `docs/book/validation/student-loan-repayments.ipynb` |
| Model / scope, open item | Indirect tax effects of reforms tracked as a documentation gap | `policyengine-uk` issues #1114, #1119 (confirmed via `gh api`) |

The rows below were added in a 2026-07-15 sweep of the populace UK lane's
July 2026 merged work (every PR/issue number re-verified against its live
title and state via `gh` at that date):

| Section | Evidence | Source |
| --- | --- | --- |
| Data / input-coverage contract | 145 required inputs / 0 reviewed exclusions; effective-mass (1 ppm) semantics; fail-closed gate classes; 143+2 launch state and the gate-forced charitable promotions | populace#420 ("UK release input-coverage contract: 145-required gate, effective-mass semantics, and the real-donor HMRC replay," MERGED 2026-07-13); `populace/UK_COVERAGE_PROGRESS.md` |
| Data / US contract comparison | 158 required inputs / 8 reviewed exclusions (US register) | `populace/COVERAGE_PROGRESS.md` (final checkpoint entry; verified 2026-07-15) |
| Data / local-area geography | OA-anchored ladder: 2021 OA anchor, 2024-boundary constituency within calibrated region, deterministic derived layers, vintage-refusal discipline, release-blocking gate; England & Wales at merge; build wire-up deferred to a follow-up | populace#354 ("UK output-area-anchored geography ladder (US block-ladder pattern)," MERGED 2026-07-09); design ratified in populace#349 (OPEN) |
| Data / promotion gate | `populace_uk_2023` certified as UK default on a matched-N holdout comparison (holdout loss 0.1239 vs. 0.3784; per-target wins 79–70; MARE 1.49%; worst miss 23.1% under a 25% gate) | policyengine.py#427 ("Certify UK Populace default dataset," MERGED 2026-06-19) |
| Validation / promotion adjudication | popdgp joint-distribution metrics (all 4 views intermediate) + out-of-sample backtests; head-to-head populace-uk 6 / incumbent 1 / tie 1; no decisive incumbent win; "unqualified superiority supported: False"; 4 named shared-gap metrics; in-sample context rows separated from adjudicated rows | policyengine.py#462 ("Promotion certification suite: pre-registered out-of-sample scorecard at default-flip time," OPEN), comment of 2026-07-08 |
| Validation / HMRC replay register | 208 facts (8 components × 13 total-income bands × 2 measures); result 0 exact / 0 directional / 208 evidence-fenced exclusions; 5-of-10 constituent fence (EPB, EXPS, TAXTERM, MOTHINC, OTHERINC absent; OSSBEN, SRP partial → named subsets); EXPS subtraction destroys directionality; NaN-not-proxy rule; deterministic TEI+TII=TI identity; no HMRC calibration | populace#420; per-constituent audit table in `populace/UK_COVERAGE_PROGRESS.md` |
| Data / licensing posture | UKDS-licensed row-level microdata never committed (version-control excluded); tracked artifacts aggregate-only, no row-level donor data; staging datasets untracked; licensed inputs pinned by checksum | populace#420; `populace/UK_COVERAGE_PROGRESS.md` |

## What does not exist yet (genuine gaps, not oversights)

- **HMRC/DWP ready reckoners**: no comparison of PolicyEngine's reform-costing
  output against a published ready-reckoner line item was found in either
  `policyengine-uk` or `populace`. Named explicitly in the issue scope;
  needs to be assembled or explicitly deferred with a stated reason.
- **HBAI distributional validation**: `hbai.md` establishes the variable
  mapping needed to compute HBAI-style poverty/income statistics. The six
  poverty rows of the promotion adjudication (policyengine.py#462, comment
  of 2026-07-08) are the first HBAI-benchmark poverty-rate comparisons on
  the public record, but a fuller distributional validation (income
  deciles, full distributions, against DWP's published HBAI release)
  remains unassembled.
- **UKMOD country report full citation**: the validation notebook cites "the
  2020-26 UKMOD country report" inline; this needs to resolve to a full,
  citable ISER/EUROMOD country-report reference before submission.
- **Re-running the two validation notebooks against the current model**: the
  `validation.ipynb` notebook imports
  `policyengine_uk.data.datasets.frs.calibration.loss`, which no longer
  resolves — calibration code has migrated to `populace.calibrate`. The
  notebook's *method and program coverage* are independently verifiable by
  reading its source (cited in `paper/sections/validation.tex`), but its
  *specific numeric outputs* need a re-run before they can be quoted in
  prose. Same caveat applies to `student-loan-repayments.ipynb`'s specific
  correlation/ratio figures, which are not transcribed in this outline.

## Non-goals for v1

- No new simulations. Every number that will appear in the drafted prose
  must trace to a committed, citable artifact (a notebook, a test, a YAML
  registry, or a published administrative statistic) — this outline PR
  itself introduces no new results.
- No comparative claims about UKMOD/EUROMOD beyond their own published
  figures (issue scope: "strictly validation-comparative and collegial").
