# Pending citations

Citations named in the outline that have not been verified against a
primary source and must be confirmed before they enter
`paper/bibliography/references.bib`. Do not add a citation to the
bibliography from memory; add it only after checking the bibliographic
record (year, publisher/series, edition, DOI or report number) against the
original publication.

See `paper/bibliography/references.bib`'s header comment for why these are
listed here in prose rather than as commented-out BibTeX stubs: a
commented `@techreport{...}` placeholder previously broke this outline's
first render, because BibTeX scans for the `@` entry marker even inside a
`%`-comment line.

## 1. UKMOD/EUROMOD country report

Referenced in-notebook (`docs/book/validation/validation.ipynb` in
`policyengine-uk`) as "the 2020-26 UKMOD country report." ISER publishes
UKMOD/EUROMOD country reports annually. Before citing it in the
manuscript:

1. Identify the exact edition/year this notebook's figures were
   transcribed from (the notebook's own citation comment should say, or
   the commit history around policyengine-uk#724 -- "Update validation
   page for new UKMOD country report" -- should identify the edition it
   updated to).
2. Confirm publisher, series name, edition number, and any DOI or report
   number via ISER's publication page.
3. Add the verified entry to `paper/bibliography/references.bib` and cite
   it with `\citep{...}` in `paper/sections/validation.tex`, replacing the
   current inline "2020-26 UKMOD country report" prose reference.

## 2. DWP Households Below Average Income (HBAI) statistics release

Cited in `docs/book/validation/hbai.md` in `policyengine-uk`, which links
to the "Households Below Average Income for Financial Years Ending 1995 to
2024" statistics release and its accompanying quality-and-methodology
report. Before citing it in the manuscript:

1. Confirm the exact release edition/year in use (HBAI is republished
   annually with an updated financial-year range in its title).
2. Add a formal citation (DWP as author/publisher, release title, year,
   URL) to `paper/bibliography/references.bib`.
3. This citation becomes load-bearing only if Section 5's "Validation not
   yet assembled" HBAI-distributional-statistics gap is closed for v1 (see
   `paper/sections/validation.tex`'s final `\todo{}`); if that comparison
   is instead deferred to a later version, this citation may remain
   unused in v1's rendered text.

## 3. HMRC Survey of Personal Incomes (SPI) statistics release, 2020/21

Cited in `docs/book/validation/spi-validation.ipynb` in `policyengine-uk`
as the 2020/21 tax-year vintage. Before citing it in the manuscript:

1. Confirm the exact HMRC SPI statistics release title, year, and URL for
   the 2020/21 vintage.
2. Confirm whether a newer SPI vintage has since been published; if so,
   decide (per `paper/sections/validation.tex`'s existing `\todo{}`)
   whether to note that this validation predates it or to rerun the
   notebook against the newer vintage before submission.
3. Add the verified entry to `paper/bibliography/references.bib`.
