# Progress log — v1 outline PR (issue #1)

Standing orders (2026-07-04): update this file with every push; delete it in
final cleanup before merge. Two prior fleets died mid-task today from process
exits, so treat every push as possibly the last action this session takes.

## Inherited state (at session start)

- Worktree: `~/PolicyEngine/_worktrees/uk-paper-outline`
- Branch: `v1-outline` @ `387a916` (pushed to origin)
- 1 substantive commit from a prior agent that finished content but died
  while opening the PR — apparently a scratchpad body-file name collision.
- Content present: `PLAN.md` (evidence map), `README.md` (repo description +
  status), `paper/sections/*.tex` (section stubs w/ `\todo{}` markers),
  `_quarto.yml`, `pyproject.toml`, `tests/`.

## This session's plan

1. [x] Create this PROGRESS.md
2. [x] `git diff origin/main...HEAD --stat` + read full inherited content
3. [x] Read `gh issue view 1 --repo PolicyEngine/policyengine-uk-paper` —
   compare scope against inherited content; STOP if mismatch (no mismatch
   found — proceeded)
4. [x] Verify build (`uv run quarto render` and `uv run pytest`/`ruff`) —
   verified locally after every substantive edit, not just once
5. [x] Verify every empirical claim maps to real evidence or is marked
   `\todo{evidence needed}` — cross-checked against a live re-fetch of
   policyengine-uk (programs.yaml, 4 validation docs, 6 issue numbers, 1
   external URL); found and fixed 5 real errors (see Log)
6. [x] Check UKMOD comparisons are strictly factual, no competitive
   framing — ran `3.23.0:shared:neutrality-reviewer` agent: PASS
7. [x] Check sentence case, policy-neutral language throughout — verified
   manually (all headings already sentence case) + neutrality agent
8. [x] Reference merged US sibling (PolicyEngine/policyengine-us-paper main)
   for structure + CONTRIBUTING guardian-claims pattern; mirrored where a
   UK analogue exists (added CONTRIBUTING.md + docs/pending-citations.md;
   deliberately did NOT add the `\evidence{}` macro — see Log for why)
9. [x] Fix anything that fails; note fixes here and in PR body
10. [x] Push (4 pushes total this session: PROGRESS.md checkpoint, then
    the fixes commit, plus this final update)
11. [x] Open PR (`gh pr create --body-file <fresh-name>`, no @-mentions) —
    https://github.com/PolicyEngine/policyengine-uk-paper/pull/2
12. [x] Confirm CI green (do NOT merge — lead reviews) — both `lint` and
    `render` pass, PR is MERGEABLE/CLEAN. Did NOT merge.
13. [ ] Final report to lead: PR URL, changes vs inherited, evidence-vs-TODO
    map, open questions (delivering now, in the same message that reports
    this checklist complete)
14. [ ] Delete this file before handoff/merge (per standing orders) — left
    in place for the lead's review; NOT yet deleted, since the lead
    reviews before merge and this file is useful context for that review

## Log

- 2026-07-04 (session start): Read PLAN.md + README.md. Both look
  substantive and well-scoped already. PLAN.md has an explicit evidence
  table and an honest "what does not exist yet" section (HMRC/DWP ready
  reckoners, HBAI distributional validation, UKMOD country-report full
  citation, stale notebook imports needing re-run before numbers are
  quoted). This is promising — inherited work looks careful. Proceeding to
  diff + issue comparison next.

- Issue #1 scope check: PASS. Issue text ("v1 scope: model description +
  validation vs UKMOD/HMRC outturns; outline mapped to existing evidence",
  labeled `tier:standard`) matches inherited PLAN.md/README.md/section
  content closely. No mismatch — proceeding without escalation.

- Compared against merged US sibling (policyengine-us-paper, PR #2,
  MERGED): same Quarto+LaTeX/IJM structure. Two real structural gaps found:
  1. US sibling has `CONTRIBUTING.md` (evidence rule, tier doctrine linking
     populace#305, guardian-claims section) + `docs/pending-citations.md`.
     UK repo has neither. **Decision: add both**, populated with UK-specific
     content (not copied verbatim) — this is a genuine mirroring gap the
     task explicitly asked me to check for.
  2. US sibling uses a separate `\evidence{}` macro (distinct from
     `\citep{}`/`\todo{}`) because its outline is skeletal claim-lists.
     UK repo's sections are already near-full draft prose with citations
     inline in text. **Decision: do NOT add `\evidence{}`** — the UK
     version is a further-along drafting style, not a deficient one;
     retrofitting a skeletal-outline macro onto complete prose would be a
     regression, not a fix. Confirmed via populace#305 (routing doctrine)
     that issue #1 here is `tier:standard`, matching the US sibling's tier
     — same acceptance bar, no framing-review escalation needed.

- Build verification (local, not just trusting CI): `uv run pytest` (5/5
  pass), `uv run ruff check .` (clean), `quarto render --to html` (clean,
  no warnings), `quarto render --to pdf` (clean, 14pp PDF, no LaTeX/BibTeX
  errors or undefined refs/citations in log). Build passes end to end,
  matching both CI jobs (render + lint).

- **Empirical claim verification against live policyengine-uk repo**
  (fetched `programs.yaml` via `gh api`, independently recomputed the
  agency x status crosstab): FOUND REAL ERRORS, all now fixed (see below):
  1. Program-coverage table (model.tex Table 1) said 45 total / 7 partial /
     Local: 1 program (complete only). Live file has 46 total / 8 partial /
     Local: 2 programs (`council_tax` complete + `council_tax_reduction`
     partial, added 2026-06-07 in policyengine-uk#1769, well before today
     — not a same-day race). **Fixed**: table and prose now say 46/38/8,
     Local row is 2/1/1, and the country-tax-reduction gap is folded into
     the DfE-partial-programs sentence pattern.
  2. model.tex's `business_rates` discussion quoted a childcare/nursery-
     hours note ("Free hours for disadvantaged 2-year-olds...") as if it
     were `business_rates`'s own note, flagging it as suspicious. Verified:
     `business_rates`'s real note is "Parameters need updating beyond
     2021" (sensible, unrelated to childcare) — verified_end_year: 2021.
     The childcare note actually belongs to `targeted_childcare_entitlement`
     (DfE, complete status), a different program entirely. **Fixed**:
     corrected the `business_rates` description to its real note and
     dropped the false "copied from elsewhere" suspicion (there was no
     copy-paste bug — the prior agent misattributed a real note to the
     wrong program id while surveying the file).
  3. model.tex's "known coverage gaps" cited both policyengine-uk#1114 and
     #1119 as tracking indirect-tax-effects. Verified via `gh issue view`:
     #1114 ("Model indirect tax effects of individual tax reforms") is
     correct; #1119 ("Add extended childcare hours usage fraction variable
     to fix caseload-spending mismatch") is unrelated — wrong issue number,
     not a second legitimate citation. Searched policyengine-uk issues for
     an on-point replacement; found none unambiguous. **Fixed**: dropped
     #1119, kept #1114 only.
  4. data.tex's "Nowcasting and uprating" subsection cited
     `docs/book/assumptions/rf-nowcasting-methodology.md` as containing
     "a more detailed rent- and council-tax-nowcasting methodology" for
     PolicyEngine's own model. Fetched and read the file: it is actually a
     summary of the **Resolution Foundation's** (third-party) nowcasting
     methodology, explicitly framed as a paired external reference to
     PolicyEngine's own `growthfactors.md`/`nowcasting-comparison.md`
     (both confirmed to exist via `gh api` directory listing). Citing it
     as PolicyEngine's own methodology would have been a real
     mischaracterization. **Fixed**: re-pointed the sentence to
     `growthfactors.md` (PolicyEngine's actual growth-rate assumptions doc)
     and added a sentence correctly describing `rf-nowcasting-methodology.md`
     as an external comparison reference, not PolicyEngine's own method.
  5. Cross-checked all 6 cited policyengine-uk issue numbers (#724, #300,
     #212, #545, #1114, #1119) via `gh issue view --json title,state`:
     titles match exactly as quoted in validation.tex/model.tex, except
     #1119 (see point 3). Confirmed the "Autumn 2023 model calibration"
     URL is genuinely live (307 apex->www redirect then 200, not a dead
     link — normal Vercel canonical-domain redirect, no fix needed).

## Fixes applied (final list, cross-ref PR body)

1. model.tex Table 1 + prose: corrected 45->46 total, 7->8 partial,
   Local row 1/0 -> 2/1/1 (added council_tax_reduction, partial,
   policyengine-uk#1769, 2026-06-07).
2. model.tex: corrected the business_rates note description to its real
   text ("Parameters need updating beyond 2021"); removed the false
   "looks copied from elsewhere" flag.
3. model.tex: dropped incorrect issue #1119 citation from the indirect-
   tax-effects gap sentence; kept #1114 only.
4. data.tex: corrected the rf-nowcasting-methodology.md citation to
   describe it accurately (external RF-methodology reference, not
   PolicyEngine's own), re-pointed the "PolicyEngine's own detailed
   methodology" claim to growthfactors.md.
5. data.tex: corrected a `\todo{}`'s guidance on the earliest
   verified_start_year (was 2019, actually 2013).
6. Added CONTRIBUTING.md (evidence rule + guardian-claims section,
   UK-specific content) mirroring the merged US sibling's structure.
7. Added docs/pending-citations.md (UKMOD/EUROMOD country report,
   HBAI statistics release, SPI statistics release -- the three
   pseudo-bibliography items already flagged in references.bib's comment).
8. README.md: neutrality-reviewer flag -- reworded an unbenchmarked
   "serious model" value judgment to a neutral factual statement.
9. introduction.tex: neutrality-reviewer flag -- tightened a `\todo{}` to
   warn against converting PolicyEngine's own publication timeline into an
   implicit UKMOD comparison during full-prose drafting.
10. README.md: added a Layout section (mirrors US sibling), pointing to
    CONTRIBUTING.md, docs/pending-citations.md, PLAN.md, tests/.

All fixes independently re-verified: `uv run pytest` (5/5), `uv run ruff
check .` (clean), `quarto render --to html` and `--to pdf` (both clean, no
LaTeX/BibTeX errors, 14pp PDF) after every substantive edit, not just once
at the end. Ran `3.23.0:shared:neutrality-reviewer` agent: **pass**, zero
violations (see above).

- Ran `3.23.0:shared:neutrality-reviewer` agent (sonnet) against all
  section files + new CONTRIBUTING.md + README.md + PLAN.md. **Verdict:
  pass** at the `tier:standard` bar. Zero real violations found (no
  unbenchmarked superlatives, no editorializing about UKMOD/EUROMOD's own
  methodology, no one-sided validation reporting -- every caveat set up in
  one place is honored elsewhere, e.g. the "Official" column not being
  independent is stated at first use in validation.tex AND repeated in
  discussion.tex, not diluted on second mention). Two low-cost improvements
  applied from its findings:
  1. README.md: reworded "Every serious model has this citation... does
     not yet" (an unbenchmarked "serious" value judgment) to the neutral
     "EUROMOD... and TAXSIM... each have a standard citable methods paper;
     PolicyEngine UK does not yet" -- same fact, no evaluative adjective.
  2. introduction.tex: tightened the `\todo{}` instructing the future
     drafter of the UKMOD-situating paragraph, explicitly warning against
     converting PolicyEngine's own citable-paper timeline into an implicit
     comparison with UKMOD's longer one (the reviewer's single
     highest-risk-during-full-drafting item).

- Additional independent verification beyond the four fixed errors above
  (all PASSED, no further errors found):
  - SPI validation.ipynb fetched and read in full: composite-records
    exclusion (1,770 records, ~0.2%), the four match-rate bands (92.7% /
    93.5% / 98.3% / 1.7%), and all four discrepancy-cluster figures
    (Marriage Allowance 4.8%/37,998 records; non-resident Personal
    Allowance 0.3%/2,054; Other Investment Income 0.2%/1,276; Gift Aid
    0.1%/738) all match validation.tex's Table 2 and prose exactly.
  - Confirmed validation.ipynb exists, is a real 2-cell notebook building
    a `policyengine_uk.Microsimulation` and a `UKMOD_CASELOADS` dict
    sourced to "the 2020-26 UKMOD country report" -- matches validation.tex's
    description of the notebook's method and citation.
  - Found (lower severity, inside a `\todo{}` instruction rather than
    asserted prose): data.tex's TODO said the earliest
    `verified_start_year` across programs.yaml is 2019 -- actual earliest
    is 2013 (`council_tax_reduction`, the same newly-added program behind
    the Table 1 fix). **Fixed**: corrected the TODO's guidance so whoever
    resolves it next isn't misled.

## Open questions for the lead (surfaced, not resolved by me)

- Whether v1 should assemble the HMRC/DWP ready-reckoner comparison and
  HBAI distributional validation before circulating, or explicitly scope
  them out for v1 with a stated reason (both currently open `\todo{}`s,
  per PLAN.md's own "non-goals for v1" framing -- I did not resolve this
  either way, since it is a scope decision, not a build/evidence-mapping
  one).
- Author list beyond Max Ghenis (disclosures.tex \todo{}) -- untouched,
  human decision.
- Funding statement -- untouched, human decision, per issue scope this is
  explicitly TODO.
