"""
convert_to_futureinternet.py
============================
Converts any .docx file into a document formatted according to the
MDPI Future Internet journal template (futureinternet-template.dot).

Usage
-----
    python convert_to_futureinternet.py input.docx [output.docx]

If output.docx is omitted the result is saved as <input>_futureinternet.docx
in the same directory.

Dependencies
------------
    pip install python-docx

Notes
-----
The script analyses paragraph roles heuristically (title, authors,
affiliations, abstract, keywords, section headings, body, references,
figures, tables, captions) and re-styles every paragraph to match the
MDPI Future Internet Word template.  All existing text, tables, and
inline images are preserved.

Author  : GitHub Copilot  (academic-editing mode)
Date    : 2026-08-19
"""

import sys
import os
import re
import copy
from docx import Document
from docx.shared import Pt, Cm, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

# ---------------------------------------------------------------------------
# ── MDPI Future Internet style definitions ──────────────────────────────────
# ---------------------------------------------------------------------------

FONT_NAME = "Arial"

STYLES = {
    # name                : (font_pt, bold, italic, align,         space_before, space_after, first_indent_cm, line_rule,            line_val)
    "FI_Title"           : (14, True,  False, WD_ALIGN_PARAGRAPH.CENTER,  0,  12,  0,     WD_LINE_SPACING.SINGLE,      1.0),
    "FI_Authors"         : (11, False, False, WD_ALIGN_PARAGRAPH.CENTER,  6,   6,  0,     WD_LINE_SPACING.SINGLE,      1.0),
    "FI_Affiliations"    : (10, False, True,  WD_ALIGN_PARAGRAPH.CENTER,  3,   3,  0,     WD_LINE_SPACING.SINGLE,      1.0),
    "FI_Abstract_Heading": (10, True,  False, WD_ALIGN_PARAGRAPH.JUSTIFY, 12,  2,  0,     WD_LINE_SPACING.SINGLE,      1.0),
    "FI_Abstract"        : (10, False, False, WD_ALIGN_PARAGRAPH.JUSTIFY,  2,  6,  0,     WD_LINE_SPACING.SINGLE,      1.0),
    "FI_Keywords_Heading": (10, False, True,  WD_ALIGN_PARAGRAPH.JUSTIFY,  6,  0,  0,     WD_LINE_SPACING.SINGLE,      1.0),
    "FI_Keywords"        : (10, False, False, WD_ALIGN_PARAGRAPH.JUSTIFY,  0,  12, 0,     WD_LINE_SPACING.SINGLE,      1.0),
    "FI_Heading1"        : (12, True,  False, WD_ALIGN_PARAGRAPH.LEFT,    12,  6,  0,     WD_LINE_SPACING.SINGLE,      1.0),
    "FI_Heading2"        : (11, True,  False, WD_ALIGN_PARAGRAPH.LEFT,     6,  3,  0,     WD_LINE_SPACING.SINGLE,      1.0),
    "FI_Heading3"        : (10, True,  True,  WD_ALIGN_PARAGRAPH.LEFT,     6,  3,  0,     WD_LINE_SPACING.SINGLE,      1.0),
    "FI_Body"            : (10, False, False, WD_ALIGN_PARAGRAPH.JUSTIFY,  0,  6,  0.5,   WD_LINE_SPACING.SINGLE,      1.0),
    "FI_Body_NoIndent"   : (10, False, False, WD_ALIGN_PARAGRAPH.JUSTIFY,  0,  6,  0,     WD_LINE_SPACING.SINGLE,      1.0),
    "FI_Caption"         : (10, False, True,  WD_ALIGN_PARAGRAPH.CENTER,   4,  4,  0,     WD_LINE_SPACING.SINGLE,      1.0),
    "FI_References_Head" : (10, True,  False, WD_ALIGN_PARAGRAPH.LEFT,    12,  4,  0,     WD_LINE_SPACING.SINGLE,      1.0),
    "FI_References"      : (10, False, False, WD_ALIGN_PARAGRAPH.JUSTIFY,  2,  2,  -0.5,  WD_LINE_SPACING.SINGLE,      1.0),
    "FI_TableHeader"     : (10, True,  False, WD_ALIGN_PARAGRAPH.CENTER,   2,  2,  0,     WD_LINE_SPACING.SINGLE,      1.0),
    "FI_TableBody"       : (10, False, False, WD_ALIGN_PARAGRAPH.LEFT,     2,  2,  0,     WD_LINE_SPACING.SINGLE,      1.0),
}

# Page margins (cm) – MDPI single-column manuscript format
PAGE_MARGIN_TOP    = 2.5
PAGE_MARGIN_BOTTOM = 2.5
PAGE_MARGIN_LEFT   = 2.5
PAGE_MARGIN_RIGHT  = 2.5


# ---------------------------------------------------------------------------
# ── Helpers ──────────────────────────────────────────────────────────────────
# ---------------------------------------------------------------------------

def _set_page_margins(doc: Document) -> None:
    """Apply MDPI page margins to every section."""
    for section in doc.sections:
        section.top_margin    = Cm(PAGE_MARGIN_TOP)
        section.bottom_margin = Cm(PAGE_MARGIN_BOTTOM)
        section.left_margin   = Cm(PAGE_MARGIN_LEFT)
        section.right_margin  = Cm(PAGE_MARGIN_RIGHT)


def _define_styles(doc: Document) -> None:
    """Create (or overwrite) all FI_* styles in the document."""
    for style_name, props in STYLES.items():
        font_pt, bold, italic, align, sp_bef, sp_aft, fi_cm, line_rule, line_val = props

        if style_name in doc.styles:
            style = doc.styles[style_name]
        else:
            style = doc.styles.add_style(style_name, WD_STYLE_TYPE.PARAGRAPH)

        # Font
        style.font.name  = FONT_NAME
        style.font.size  = Pt(font_pt)
        style.font.bold  = bold
        style.font.italic = italic

        # Paragraph format
        pf = style.paragraph_format
        pf.alignment       = align
        pf.space_before    = Pt(sp_bef)
        pf.space_after     = Pt(sp_aft)
        pf.first_line_indent = Cm(fi_cm) if fi_cm != 0 else None
        pf.line_spacing_rule = line_rule


def _apply_style_to_paragraph(para, style_name: str, doc: Document) -> None:
    """Apply a named style and re-run all runs through the same font settings."""
    para.style = doc.styles[style_name]
    props = STYLES[style_name]
    font_pt, bold, italic = props[0], props[1], props[2]
    for run in para.runs:
        run.font.name   = FONT_NAME
        run.font.size   = Pt(font_pt)
        run.font.bold   = bold   if run.font.bold   is not None else None
        run.font.italic = italic if run.font.italic is not None else None
        # Clear any hard-coded colors (let style drive)
        run.font.color.rgb = None


def _full_text(para) -> str:
    return para.text.strip()


# ---------------------------------------------------------------------------
# ── Paragraph-role detection ─────────────────────────────────────────────────
# ---------------------------------------------------------------------------

_RE_HEADING1 = re.compile(
    r"^(\d+\.?\s|[IVX]+\.\s|Introduction|Background|Related|Methodology|Method|"
    r"Experiment|Results?|Discussion|Conclusion|Future|Acknowledgment|Appendix|"
    r"Material)", re.IGNORECASE
)
_RE_HEADING2 = re.compile(r"^(\d+\.\d+\.?\s)", re.IGNORECASE)
_RE_HEADING3 = re.compile(r"^(\d+\.\d+\.\d+\.?\s)", re.IGNORECASE)
_RE_FIGURE   = re.compile(r"^(figure|fig\.?)\s*\d+", re.IGNORECASE)
_RE_TABLE    = re.compile(r"^table\s*\d+", re.IGNORECASE)
_RE_REF_HEAD = re.compile(r"^references?$", re.IGNORECASE)
_RE_REF_ITEM = re.compile(r"^\[?\d+[\]\.]")
_RE_ABSTRACT = re.compile(r"^abstract[:.]?\s*$", re.IGNORECASE)
_RE_KEYWORDS = re.compile(r"^keywords?[:.]?\s*$", re.IGNORECASE)
_RE_AUTHOR_EMAIL = re.compile(r"@")
_RE_SUPERSCRIPT_AFFIL = re.compile(r"^\d[\d,;]*\s+\w")  # "1 Department..."


class RoleDetector:
    """
    Finite-state machine that walks paragraphs top-to-bottom and assigns
    a semantic role to each one.
    """

    TITLE        = "title"
    AUTHORS      = "authors"
    AFFILIATIONS = "affiliations"
    ABSTRACT_H   = "abstract_heading"
    ABSTRACT     = "abstract"
    KEYWORDS_H   = "keywords_heading"
    KEYWORDS     = "keywords"
    HEADING1     = "heading1"
    HEADING2     = "heading2"
    HEADING3     = "heading3"
    BODY         = "body"
    CAPTION      = "caption"
    REF_HEAD     = "ref_heading"
    REF_ITEM     = "ref_item"
    BLANK        = "blank"

    def __init__(self, paragraphs):
        self.paragraphs = paragraphs
        self.roles: list[str] = []
        self._run()

    # ── state machine ───────────────────────────────────────────────────────
    def _run(self):
        state = "front_matter"
        front_count = 0  # paragraphs seen in front matter

        for i, para in enumerate(self.paragraphs):
            txt  = _full_text(para)
            low  = txt.lower()

            # Skip blank paragraphs
            if not txt:
                self.roles.append(self.BLANK)
                continue

            # ── front matter (title / authors / affiliations / abstract / keywords)
            if state == "front_matter":
                if front_count == 0:
                    self.roles.append(self.TITLE); front_count += 1; continue

                if front_count == 1:
                    self.roles.append(self.AUTHORS); front_count += 1; continue

                if _RE_ABSTRACT.match(txt) or low.startswith("abstract"):
                    if _RE_ABSTRACT.match(txt):
                        self.roles.append(self.ABSTRACT_H)
                    else:
                        # abstract heading fused with text
                        self.roles.append(self.ABSTRACT_H)
                    state = "abstract"; continue

                # affiliation lines (email, numbered affiliation, short lines)
                if (_RE_AUTHOR_EMAIL.search(txt) or
                        _RE_SUPERSCRIPT_AFFIL.match(txt) or
                        len(txt) < 120):
                    self.roles.append(self.AFFILIATIONS); front_count += 1; continue

                self.roles.append(self.AFFILIATIONS); front_count += 1; continue

            if state == "abstract":
                if _RE_KEYWORDS.match(txt) or low.startswith("keyword"):
                    if _RE_KEYWORDS.match(txt):
                        self.roles.append(self.KEYWORDS_H)
                        state = "keywords"
                    else:
                        self.roles.append(self.KEYWORDS_H)
                        state = "body"
                    continue
                self.roles.append(self.ABSTRACT); continue

            if state == "keywords":
                # keywords text (may be on next line after heading)
                self.roles.append(self.KEYWORDS)
                state = "body"; continue

            # ── body / references
            if _RE_REF_HEAD.match(txt):
                self.roles.append(self.REF_HEAD)
                state = "references"; continue

            if _RE_REF_ITEM.match(txt):
                self.roles.append(self.REF_ITEM)
                state = "references"; continue

            if _RE_FIGURE.match(txt) or _RE_TABLE.match(txt):
                self.roles.append(self.CAPTION); continue

            if state == "references":
                if _RE_REF_ITEM.match(txt):
                    self.roles.append(self.REF_ITEM)
                else:
                    self.roles.append(self.REF_ITEM)   # continuation
                continue

            # Detect headings by style name first
            style_name = para.style.name if para.style else ""
            if "Heading 1" in style_name or _RE_HEADING1.match(txt) and len(txt.split()) <= 12:
                self.roles.append(self.HEADING1); continue
            if "Heading 2" in style_name or _RE_HEADING2.match(txt):
                self.roles.append(self.HEADING2); continue
            if "Heading 3" in style_name or _RE_HEADING3.match(txt):
                self.roles.append(self.HEADING3); continue

            self.roles.append(self.BODY)


# ---------------------------------------------------------------------------
# ── Style-map from role to FI style name ─────────────────────────────────────
# ---------------------------------------------------------------------------

ROLE_TO_STYLE = {
    RoleDetector.TITLE        : "FI_Title",
    RoleDetector.AUTHORS      : "FI_Authors",
    RoleDetector.AFFILIATIONS : "FI_Affiliations",
    RoleDetector.ABSTRACT_H   : "FI_Abstract_Heading",
    RoleDetector.ABSTRACT     : "FI_Abstract",
    RoleDetector.KEYWORDS_H   : "FI_Keywords_Heading",
    RoleDetector.KEYWORDS     : "FI_Keywords",
    RoleDetector.HEADING1     : "FI_Heading1",
    RoleDetector.HEADING2     : "FI_Heading2",
    RoleDetector.HEADING3     : "FI_Heading3",
    RoleDetector.BODY         : "FI_Body",
    RoleDetector.CAPTION      : "FI_Caption",
    RoleDetector.REF_HEAD     : "FI_References_Head",
    RoleDetector.REF_ITEM     : "FI_References",
    RoleDetector.BLANK        : "FI_Body_NoIndent",
}


# ---------------------------------------------------------------------------
# ── Table styling ─────────────────────────────────────────────────────────────
# ---------------------------------------------------------------------------

def _style_table(table, doc: Document) -> None:
    """Apply FI table styles: no color fills, clean borders, Arial fonts."""
    for i, row in enumerate(table.rows):
        for cell in row.cells:
            # Remove cell shading
            tc = cell._tc
            tcPr = tc.get_or_add_tcPr()
            shd = tcPr.find(qn("w:shd"))
            if shd is not None:
                tcPr.remove(shd)

            for para in cell.paragraphs:
                style = "FI_TableHeader" if i == 0 else "FI_TableBody"
                _apply_style_to_paragraph(para, style, doc)


# ---------------------------------------------------------------------------
# ── Separator line below title block ─────────────────────────────────────────
# ---------------------------------------------------------------------------

def _add_horizontal_rule(para) -> None:
    """Add a bottom border (thin rule) below a paragraph via XML."""
    pPr = para._p.get_or_add_pPr()
    pBdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"),   "single")
    bottom.set(qn("w:sz"),    "4")
    bottom.set(qn("w:space"), "1")
    bottom.set(qn("w:color"), "auto")
    pBdr.append(bottom)
    pPr.append(pBdr)


# ---------------------------------------------------------------------------
# ── Main conversion function ─────────────────────────────────────────────────
# ---------------------------------------------------------------------------

def convert(input_path: str, output_path: str | None = None) -> str:
    """
    Read *input_path*, apply MDPI Future Internet formatting, write *output_path*.
    Returns the path of the created file.
    """
    if output_path is None:
        base, _ = os.path.splitext(input_path)
        output_path = base + "_futureinternet.docx"

    print(f"[INFO] Loading: {input_path}")
    doc = Document(input_path)

    # 1. Page setup
    _set_page_margins(doc)

    # 2. Register all custom styles
    _define_styles(doc)

    # 3. Detect roles
    paragraphs = doc.paragraphs
    detector   = RoleDetector(paragraphs)

    # 4. Restyle every paragraph
    last_front_role = None
    for para, role in zip(paragraphs, detector.roles):
        style_name = ROLE_TO_STYLE.get(role, "FI_Body")
        _apply_style_to_paragraph(para, style_name, doc)

        # Draw a horizontal rule under the keywords block (end of front matter)
        if role in (RoleDetector.KEYWORDS, RoleDetector.KEYWORDS_H):
            last_front_role = role
        if last_front_role == RoleDetector.KEYWORDS and role == RoleDetector.HEADING1:
            # Put the rule on the keywords paragraph (already processed — find it)
            # We look back for the last keywords paragraph
            pass   # handled below

    # Add separator rule after the last keywords paragraph
    for para, role in zip(paragraphs, detector.roles):
        if role == RoleDetector.KEYWORDS:
            _add_horizontal_rule(para)
            break

    # 5. Style tables
    for table in doc.tables:
        _style_table(table, doc)

    # 6. Report detection summary
    from collections import Counter
    cnt = Counter(detector.roles)
    print("[INFO] Paragraph roles detected:")
    for role, n in sorted(cnt.items(), key=lambda x: -x[1]):
        print(f"       {role:<22} {n:>4} paragraph(s)")

    # 7. Save
    doc.save(output_path)
    print(f"[OK]  Saved: {output_path}")
    return output_path


# ---------------------------------------------------------------------------
# ── CLI entry point ──────────────────────────────────────────────────────────
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python convert_to_futureinternet.py input.docx [output.docx]")
        sys.exit(1)

    input_file  = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) >= 3 else None

    if not os.path.isfile(input_file):
        print(f"[ERROR] File not found: {input_file}")
        sys.exit(1)

    if not input_file.lower().endswith(".docx"):
        print("[ERROR] Input must be a .docx file.")
        sys.exit(1)

    convert(input_file, output_file)
