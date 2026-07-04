# policyengine-uk-paper

The canonical, versioned model paper for PolicyEngine UK: description and
validation of the full tax-benefit microsimulation model — rules coverage,
data (the populace stack), and validation against administrative outturns
and incumbent models (UKMOD/EUROMOD, and against HMRC/DWP ready reckoners and outturns where comparable).

EUROMOD (Sutherland–Figari 2013) and TAXSIM (Feenberg–Coutts 1993) each
have a standard citable methods paper; PolicyEngine UK does not yet. The
paper is *versioned*: v1 documents the model as deployed in 2026; engine
migrations later produce a v2 rather than invalidating v1.

Validation assets assembled from: the policyengine-uk test suite, docs, and
validation notebooks (`docs/book/validation/`), and the populace UK build
pipeline (`packages/populace-build/src/populace/build/uk_runtime/` in the
[populace](https://github.com/PolicyEngine/populace) monorepo — there is no
standalone `populace-uk` or `uk-data` repo; both are folded into that
monorepo's UK build shard as of this outline). See [PLAN.md](PLAN.md) for
the section-by-section evidence map.

Target venue: International Journal of Microsimulation (diamond open
access); arXiv preprint on completion.

## Building

```bash
uv sync
uv run quarto render
```

Requires [Quarto](https://quarto.org) and a LaTeX distribution (TinyTeX is
sufficient) for the PDF format; the HTML format has no LaTeX dependency.

## Status

v1 outline (PolicyEngine/policyengine-uk-paper#1): section stubs with
evidence mapped to existing sources, or marked `\todo{evidence needed}`
where no such evidence was found. No results, figures, or numbers are
fabricated — everything cites a specific, checkable file or publication.
Full prose drafting is the next milestone.

## Layout

- `paper/` — Quarto + LaTeX manuscript (IJM style), sections under
  `paper/sections/`.
- `paper/bibliography/references.bib` — only bibliographic entries
  verified against a primary source; see its header comment.
- `docs/pending-citations.md` — citations named in the outline but not yet
  verified against a primary source.
- `CONTRIBUTING.md` — the evidence rule, review-tier doctrine, and
  guardian-claims this repository follows.
- `PLAN.md` — the section-by-section evidence map.
- `tests/` — structural checks (section wiring, `\todo{}` brace balance,
  bibliography comment safety); run via `uv run pytest`.
