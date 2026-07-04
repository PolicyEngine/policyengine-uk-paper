# Contributing

## Review tiers

Work in this repository routes by issue label, following the portfolio-wide
doctrine (PolicyEngine/populace#305): `tier:fable` (frontier-model review:
claim-bearing prose, statistical semantics, framing that could read as
advocacy) versus `tier:standard` (spec-complete assembly; acceptance tests
judge the output). Issue #1 (this outline) is `tier:standard`: the
acceptance test is that every claim maps to an existing evidence artifact
or is marked `TODO(evidence needed)` -- not that the prose itself has been
reviewed for framing.

## The evidence rule

Every claim in `paper/sections/*.tex` must resolve to one of:

1. An inline citation to a specific file path, notebook, or URL that
   already contains the claimed fact, checked during drafting (this paper
   cites sources directly in prose -- e.g. `\texttt{policyengine\_uk/programs.yaml}`
   -- rather than through a separate annotation macro).
2. A `\citep{...}` to a verified bibliography entry in
   `paper/bibliography/references.bib` (see that file's header comment: an
   entry may only be added after its bibliographic record is confirmed
   against a primary source).
3. A `\todo{...}` explicitly marking the claim as pending -- either
   `TODO(evidence needed)` for a claim with no known existing source, or a
   more specific instruction (e.g. "re-run this notebook before citing its
   numbers") for a claim whose evidence exists but has not been
   re-verified at manuscript-drafting time.

Do not write a number, a citation, or a named comparison from memory. If a
number was true in a prior release, a prior conversation, or a prior paper,
it must be re-verified against a current artifact before entering this
manuscript -- models and calibrated data change version to version, and
this paper's whole purpose is to be the citable, versioned source of truth
rather than another number that drifts silently out of date.

## Guardian claims

Claim types that have already caused near-misses during outline drafting
and review, and deserve extra scrutiny regardless of green CI:

- **Registry counts drift between surveys.** Program-coverage counts
  (`policyengine_uk/programs.yaml`) are not static -- a program can move
  from absent to `partial` to `complete` between one contributor's survey
  and another's PR. The v1 outline itself shipped with a stale count (45
  programs / 7 partial) that a same-PR re-verification against the live
  file found to be out of date by one program (46 / 8 partial,
  `council_tax_reduction` added in policyengine-uk#1769). Re-verify
  registry-derived counts against the live file immediately before each
  push that touches Section 3 (Model), not just at outline-drafting time.
- **A program's `notes` field must be matched to its own `id`, not skimmed
  from a nearby entry.** The same review found a case of a childcare-hours
  note being attributed in prose to `business_rates` -- both entries exist
  in the same file, but the note belonged to a different program
  (`targeted_childcare_entitlement`) entirely. Quote a program's note only
  after confirming the `id`/`notes` pair directly in the source file.
- **The "Official" series in the UKMOD/administrative validation
  (Section 5.1) is PolicyEngine's own calibration target, not an
  independent third figure.** Do not describe the three-way UKMOD
  comparison as PolicyEngine vs. two independent externals -- only the
  UKMOD column is genuinely external; the "Official" column is what
  PolicyEngine is calibrated to match.
- **UKMOD/EUROMOD framing must stay strictly validation-comparative and
  collegial** (per issue #1's scope). Report where figures agree or differ
  from a cited source; do not characterize either model as "more correct"
  beyond stated distance from an official figure, and do not introduce new
  comparative claims about UKMOD/EUROMOD's own methodology that are not
  already public.
- **A document's title or file path does not guarantee its content
  describes PolicyEngine's own methodology.** `docs/book/assumptions/rf-nowcasting-methodology.md`
  in `policyengine-uk` is a summary of the Resolution Foundation's
  (external, third-party) nowcasting approach, kept as a paired reference
  next to PolicyEngine's own `growthfactors.md` -- not a description of
  PolicyEngine's own method. Read a cited document in full before
  characterizing what it says.

## Build

```bash
uv sync
uv run quarto render          # builds the manuscript (PDF + HTML)
uv run pytest                 # structural checks (section wiring, balanced \todo{} braces, bib comment safety)
uv run ruff check .
```

Requires `quarto` and a TeX distribution with `pdflatex` on `PATH`
(TeX Live via TinyTeX or a system install; the `ijm.sty` style shim avoids
`mathptmx`'s missing-font issue on TinyTeX installs).

## Layout

- `paper/` -- Quarto + LaTeX manuscript (International Journal of
  Microsimulation style), sections under `paper/sections/`.
- `paper/bibliography/references.bib` -- only bibliographic entries
  verified against a primary source; see its header comment (including the
  BibTeX `@`-inside-a-comment parsing hazard that broke this outline's
  first render attempt).
- `docs/pending-citations.md` -- citations named in the outline but not
  yet verified against a primary source; do not add them to
  `references.bib` until verified.
- `tests/test_outline.py` -- structural guards (no numeric/statistical
  checks; v1 is outline + evidence mapping, not new results).
- `PLAN.md` -- the section-by-section evidence map referenced from the
  README.
