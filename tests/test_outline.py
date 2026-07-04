"""Structural checks on the paper outline.

No experiment code exists yet (v1 is outline + evidence mapping only), so
these tests do not check any numeric claim. They guard the two things a
careless edit could silently break: that every section file the top-level
document \\input{}s actually exists, and that every \\todo{} marker is
well-formed (balanced braces), so a malformed edit fails fast in CI rather
than surfacing as a confusing LaTeX compile error.
"""

import re
from pathlib import Path

PAPER_DIR = Path(__file__).resolve().parent.parent / "paper"
INDEX_QMD = PAPER_DIR / "index.qmd"


def _referenced_sections() -> list[str]:
    text = INDEX_QMD.read_text()
    return re.findall(r"\\input\{(sections/[^}]+)\}", text)


def test_index_qmd_exists():
    assert INDEX_QMD.is_file()


def test_every_input_section_exists():
    sections = _referenced_sections()
    assert sections, "index.qmd should \\input{} at least one section"
    for rel_path in sections:
        section_file = PAPER_DIR / f"{rel_path}.tex"
        assert section_file.is_file(), f"missing section file: {section_file}"


def test_no_orphan_section_files():
    """Every .tex file under sections/ should be \\input{} somewhere.

    Catches the opposite mistake: a section file added but never wired into
    index.qmd, which would silently exclude it from every rendered format.
    """
    referenced = {f"{s}.tex" for s in _referenced_sections()}
    on_disk = {f"sections/{f.name}" for f in (PAPER_DIR / "sections").glob("*.tex")}
    assert on_disk <= referenced, f"orphaned section files: {on_disk - referenced}"


def test_todo_markers_have_balanced_braces():
    """A \\todo{...} marker with unbalanced braces breaks the LaTeX build.

    This does not require compiling LaTeX (that is CI's render job); it
    just checks the source text directly so the failure is fast and the
    error message points at the exact file.
    """
    for tex_file in (PAPER_DIR / "sections").glob("*.tex"):
        text = tex_file.read_text()
        depth = 0
        for i, ch in enumerate(text):
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
            assert depth >= 0, f"{tex_file}: unbalanced closing brace at character {i}"
        assert depth == 0, f"{tex_file}: unbalanced braces (net {depth} open)"


def test_bibliography_has_no_at_sign_outside_entries():
    """An '@' character in a comment still starts a new entry for BibTeX.

    This regression is exactly what broke the initial render of this
    outline (a commented-out '@techreport{...}' placeholder desynced
    BibTeX's parser even though it followed a '%'). Guard against it
    recurring: every non-comment, non-blank line containing '@' must be
    the start of a real entry.
    """
    bib_file = PAPER_DIR / "bibliography" / "references.bib"
    for lineno, line in enumerate(bib_file.read_text().splitlines(), start=1):
        stripped = line.lstrip()
        if stripped.startswith("%"):
            assert "@" not in line, (
                f"{bib_file}:{lineno}: '@' inside a comment line breaks "
                "BibTeX's parser even after '%' -- rephrase without '@'"
            )
