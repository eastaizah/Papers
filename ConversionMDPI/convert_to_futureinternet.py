from __future__ import annotations

import argparse
import copy
import os
import re
import shutil
import tempfile
from collections import Counter
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

import docx.api
from docx import Document
from docx.enum.style import WD_STYLE_TYPE
from docx.opc.constants import RELATIONSHIP_TYPE as RT
from docx.opc.part import PartFactory
from docx.parts.document import DocumentPart
from docx.oxml.ns import qn
from lxml import etree

W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
R_NS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
PR_NS = "http://schemas.openxmlformats.org/package/2006/relationships"
CT_NS = "http://schemas.openxmlformats.org/package/2006/content-types"
NS = {"w": W_NS, "r": R_NS, "pr": PR_NS, "ct": CT_NS}
TEMPLATE_CONTENT_TYPE = (
    "application/vnd.openxmlformats-officedocument.wordprocessingml.template.main+xml"
)
REL_HEADER = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/header"
REL_FOOTER = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/footer"
ROLE_STYLE_HINTS = {
    "title": ["title"],
    "authors": ["authornames", "author"],
    "affiliations": ["affiliation"],
    "abstract_heading": ["abstract"],
    "abstract": ["abstract"],
    "keywords_heading": ["keywords"],
    "keywords": ["keywords"],
    "heading1": ["heading1"],
    "heading2": ["heading2"],
    "heading3": ["heading3"],
    "body": ["text", "body text", "normal"],
    "body_no_indent": ["text_no_indent", "no_indent", "text"],
    "figure_caption": ["figure_caption", "figure caption", "caption"],
    "table_caption": ["table_caption", "one_table_caption", "caption"],
    "table_body": ["table_body", "table body"],
    "references_heading": ["heading1", "references"],
    "references": ["references"],
}
PARAGRAPH_DIRECT_FORMATTING_TAGS = {
    qn("w:jc"),
    qn("w:spacing"),
    qn("w:ind"),
    qn("w:contextualSpacing"),
    qn("w:mirrorIndents"),
    qn("w:pBdr"),
    qn("w:shd"),
    qn("w:tabs"),
    qn("w:suppressAutoHyphens"),
    qn("w:textAlignment"),
    qn("w:wordWrap"),
    qn("w:overflowPunct"),
    qn("w:topLinePunct"),
    qn("w:autoSpaceDE"),
    qn("w:autoSpaceDN"),
    qn("w:adjustRightInd"),
    qn("w:snapToGrid"),
    qn("w:bidi"),
}
RUN_DIRECT_FORMATTING_TAGS = {
    qn("w:rFonts"),
    qn("w:sz"),
    qn("w:szCs"),
    qn("w:color"),
}


def open_template_document(path: str | os.PathLike[str]):
    """Open a .dot/.dotx Word template via python-docx Document()."""
    PartFactory.part_type_for[TEMPLATE_CONTENT_TYPE] = DocumentPart
    original = docx.api.CT.WML_DOCUMENT_MAIN
    docx.api.CT.WML_DOCUMENT_MAIN = TEMPLATE_CONTENT_TYPE
    try:
        return docx.api.Document(str(path))
    finally:
        docx.api.CT.WML_DOCUMENT_MAIN = original


def _full_text(para) -> str:
    return para.text.strip()


_RE_HEADING1 = re.compile(
    r"^(\d+\.?\s|[IVX]+\.\s|Introduction|Background|Related|Methodology|Method|"
    r"Experiment|Results?|Discussion|Conclusion|Future|Acknowledg(?:e)?ments?|"
    r"Appendix|Material|Abbreviations|References)",
    re.IGNORECASE,
)
_RE_HEADING2 = re.compile(r"^(\d+\.\d+\.?\s)", re.IGNORECASE)
_RE_HEADING3 = re.compile(r"^(\d+\.\d+\.\d+\.?\s)", re.IGNORECASE)
_RE_FIGURE = re.compile(r"^(figure|fig\.?)\s*[A-Z0-9]+", re.IGNORECASE)
_RE_TABLE = re.compile(r"^table\s*[A-Z0-9]+", re.IGNORECASE)
_RE_TABLE_ONLY = re.compile(r"^table\s*[A-Z0-9]+\s*$", re.IGNORECASE)
_RE_REF_HEAD = re.compile(r"^references?$", re.IGNORECASE)
_RE_REF_ITEM = re.compile(r"^\[?\d+[\]\.\)]")
_RE_ABSTRACT = re.compile(r"^abstract[:.]?\s*$", re.IGNORECASE)
_RE_KEYWORDS = re.compile(r"^keywords?[:.]?\s*$", re.IGNORECASE)
_RE_AUTHOR_EMAIL = re.compile(r"@")
_RE_SUPERSCRIPT_AFFIL = re.compile(r"^\d[\d,;]*\s+\w")


class RoleDetector:
    TITLE = "title"
    AUTHORS = "authors"
    AFFILIATIONS = "affiliations"
    ABSTRACT_H = "abstract_heading"
    ABSTRACT = "abstract"
    KEYWORDS_H = "keywords_heading"
    KEYWORDS = "keywords"
    HEADING1 = "heading1"
    HEADING2 = "heading2"
    HEADING3 = "heading3"
    BODY = "body"
    CAPTION = "caption"
    REF_HEAD = "references_heading"
    REF_ITEM = "references"
    BLANK = "blank"

    def __init__(self, paragraphs):
        self.paragraphs = paragraphs
        self.roles: list[str] = []
        self._run()

    def _run(self):
        state = "front_matter"
        front_count = 0
        pending_table_caption = False
        for para in self.paragraphs:
            txt = _full_text(para)
            low = txt.lower()
            style_name = para.style.name if para.style else ""
            style_lower = style_name.lower()
            if not txt:
                self.roles.append(self.BLANK)
                continue

            if state == "front_matter":
                if front_count == 0:
                    self.roles.append(self.TITLE)
                    front_count += 1
                    continue
                if front_count == 1:
                    self.roles.append(self.AUTHORS)
                    front_count += 1
                    continue
                if _RE_ABSTRACT.match(txt) or low.startswith("abstract"):
                    self.roles.append(self.ABSTRACT_H if _RE_ABSTRACT.match(txt) else self.ABSTRACT)
                    state = "abstract"
                    continue
                if (
                    _RE_AUTHOR_EMAIL.search(txt)
                    or _RE_SUPERSCRIPT_AFFIL.match(txt)
                    or len(txt) < 160
                ):
                    self.roles.append(self.AFFILIATIONS)
                    front_count += 1
                    continue
                self.roles.append(self.AFFILIATIONS)
                front_count += 1
                continue

            if state == "abstract":
                if _RE_KEYWORDS.match(txt) or low.startswith("keyword"):
                    if _RE_KEYWORDS.match(txt):
                        self.roles.append(self.KEYWORDS_H)
                        state = "keywords"
                    else:
                        self.roles.append(self.KEYWORDS)
                        state = "body"
                    continue
                self.roles.append(self.ABSTRACT)
                continue

            if state == "keywords":
                self.roles.append(self.KEYWORDS)
                state = "body"
                continue

            if pending_table_caption:
                self.roles.append(self.CAPTION)
                pending_table_caption = False
                continue

            if _RE_REF_HEAD.match(txt):
                self.roles.append(self.REF_HEAD)
                state = "references"
                continue

            if "bibliography" in style_lower and _RE_REF_ITEM.match(txt):
                self.roles.append(self.REF_ITEM)
                state = "references"
                continue

            if _RE_TABLE_ONLY.match(txt):
                self.roles.append(self.CAPTION)
                pending_table_caption = True
                continue

            if _RE_FIGURE.match(txt) or _RE_TABLE.match(txt):
                self.roles.append(self.CAPTION)
                continue

            if state == "references":
                self.roles.append(self.REF_ITEM)
                continue

            if "Heading 3" in style_name or _RE_HEADING3.match(txt):
                self.roles.append(self.HEADING3)
                continue
            if "Heading 2" in style_name or _RE_HEADING2.match(txt):
                self.roles.append(self.HEADING2)
                continue
            if "Heading 1" in style_name or (_RE_HEADING1.match(txt) and len(txt.split()) <= 12):
                self.roles.append(self.HEADING1)
                continue
            self.roles.append(self.BODY)


class StyleResolver:
    def __init__(self, template_doc):
        self.style_names = [
            style.name
            for style in template_doc.styles
            if style.type == WD_STYLE_TYPE.PARAGRAPH
        ]
        self._cache: dict[tuple[str, tuple[str, ...]], str] = {}

    def resolve(self, role: str, *, text: str = "", fallback: str | None = None) -> str:
        if role == RoleDetector.CAPTION:
            role = "table_caption" if _RE_TABLE.match(text) else "figure_caption"
        elif role == RoleDetector.BLANK:
            role = "body_no_indent"
        hints = tuple(ROLE_STYLE_HINTS.get(role, ROLE_STYLE_HINTS["body"]))
        key = (role, hints)
        if key in self._cache:
            return self._cache[key]

        lowered = [(name, name.lower()) for name in self.style_names]
        for hint in hints:
            matches = [name for name, lower in lowered if hint.lower() in lower]
            if matches:
                best = sorted(
                    matches,
                    key=lambda name: (0 if name.upper().startswith("MDPI") else 1, len(name), name),
                )[0]
                self._cache[key] = best
                return best

        chosen = fallback or (self.style_names[0] if self.style_names else "Normal")
        self._cache[key] = chosen
        return chosen


class ComplianceTracker:
    def __init__(self):
        self.paragraph_style_usage: Counter[str] = Counter()
        self.role_to_style: dict[str, str] = {}


def clear_paragraph_direct_formatting(paragraph) -> None:
    pPr = paragraph._p.pPr
    if pPr is None:
        return
    for child in list(pPr):
        if child.tag in PARAGRAPH_DIRECT_FORMATTING_TAGS:
            pPr.remove(child)


def clear_run_direct_formatting(run) -> None:
    rPr = run._r.rPr
    if rPr is None:
        return
    for child in list(rPr):
        if child.tag in RUN_DIRECT_FORMATTING_TAGS:
            rPr.remove(child)


def apply_style_to_paragraph(paragraph, style_name: str, tracker: ComplianceTracker) -> None:
    clear_paragraph_direct_formatting(paragraph)
    paragraph.style = style_name
    tracker.paragraph_style_usage[style_name] += 1
    for run in paragraph.runs:
        clear_run_direct_formatting(run)
        run.font.name = None
        run.font.size = None
        run.font.color.rgb = None


def apply_table_styles(doc, resolver: StyleResolver, tracker: ComplianceTracker) -> None:
    header_style = resolver.resolve("table_body", fallback="Normal")
    body_style = resolver.resolve("table_body", fallback=header_style)
    table_header_style = resolver.resolve("table_caption", text="Table 1.", fallback=header_style)
    for table in doc.tables:
        for row_idx, row in enumerate(table.rows):
            for cell in row.cells:
                for paragraph in cell.paragraphs:
                    target = table_header_style if row_idx == 0 else body_style
                    apply_style_to_paragraph(paragraph, target, tracker)


def xml_texts(root: etree._Element) -> list[str]:
    return [" ".join(text.split()) for text in root.xpath(".//w:t/text()", namespaces=NS) if text.strip()]


def story_text(story) -> str:
    return " | ".join(" ".join(p.text.split()) for p in story.paragraphs if p.text.strip())


def load_xml(path: Path) -> etree._Element:
    return etree.parse(str(path)).getroot()


def save_xml(path: Path, root: etree._Element) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    etree.ElementTree(root).write(
        str(path),
        xml_declaration=True,
        encoding="UTF-8",
        standalone="yes",
    )


def next_rid(existing_ids: set[str]) -> str:
    nums = [int(match.group(1)) for rid in existing_ids if (match := re.fullmatch(r"rId(\d+)", rid))]
    candidate = max(nums, default=0) + 1
    rid = f"rId{candidate}"
    while rid in existing_ids:
        candidate += 1
        rid = f"rId{candidate}"
    existing_ids.add(rid)
    return rid


def unique_filename(path: str, used: set[str], prefix: str = "template_") -> str:
    candidate = path
    if candidate not in used:
        used.add(candidate)
        return candidate
    p = Path(path)
    stem = re.sub(r"[^A-Za-z0-9_.-]+", "_", p.stem)
    index = 1
    while True:
        renamed = str(p.with_name(f"{prefix}{stem}_{index}{p.suffix}"))
        if renamed not in used:
            used.add(renamed)
            return renamed
        index += 1


def ensure_content_type_override(content_types_root: etree._Element, part_name: str, content_type: str) -> None:
    xpath = f"./ct:Override[@PartName='/{part_name}']"
    override = content_types_root.xpath(xpath, namespaces=NS)
    if override:
        override[0].set("ContentType", content_type)
        return
    new = etree.Element(f"{{{CT_NS}}}Override")
    new.set("PartName", f"/{part_name}")
    new.set("ContentType", content_type)
    content_types_root.append(new)


def merge_template_structure(input_dir: Path, template_dir: Path) -> None:
    content_types_root = load_xml(input_dir / "[Content_Types].xml")
    template_content_types_root = load_xml(template_dir / "[Content_Types].xml")

    for relative in (
        "word/styles.xml",
        "word/settings.xml",
        "word/fontTable.xml",
        "word/webSettings.xml",
        "word/theme/theme1.xml",
    ):
        src = template_dir / relative
        if src.exists():
            dst = input_dir / relative
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
            match = template_content_types_root.xpath(
                f"./ct:Override[@PartName='/{relative}']",
                namespaces=NS,
            )
            if match:
                ensure_content_type_override(content_types_root, relative, match[0].get("ContentType"))

    input_doc_root = load_xml(input_dir / "word/document.xml")
    template_doc_root = load_xml(template_dir / "word/document.xml")
    input_rels_root = load_xml(input_dir / "word/_rels/document.xml.rels")
    template_rels_root = load_xml(template_dir / "word/_rels/document.xml.rels")
    used_rids = {rel.get("Id") for rel in input_rels_root}
    used_word_paths = {
        str(path.relative_to(input_dir)).replace(os.sep, "/")
        for path in (input_dir / "word").rglob("*")
        if path.is_file()
    }

    template_rel_id_map: dict[str, str] = {}
    for rel in template_rels_root:
        rel_type = rel.get("Type")
        if rel_type not in {REL_HEADER, REL_FOOTER}:
            continue
        old_target = f"word/{rel.get('Target')}"
        new_target = unique_filename(old_target, used_word_paths)
        src_part = template_dir / old_target
        dst_part = input_dir / new_target
        dst_part.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src_part, dst_part)

        header_rel_src = template_dir / "word/_rels" / f"{Path(old_target).name}.rels"
        if header_rel_src.exists():
            rels_root = load_xml(header_rel_src)
            for child_rel in rels_root:
                target_mode = child_rel.get("TargetMode")
                target = child_rel.get("Target")
                if target_mode == "External" or not target:
                    continue
                if not target.startswith("media/"):
                    continue
                src_media = template_dir / "word" / target
                new_media = unique_filename(f"word/{target}", used_word_paths, prefix=f"{Path(new_target).stem}_")
                dst_media = input_dir / new_media
                dst_media.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src_media, dst_media)
                child_rel.set("Target", new_media.removeprefix("word/"))
            copied_rels_path = input_dir / "word/_rels" / f"{Path(new_target).name}.rels"
            save_xml(copied_rels_path, rels_root)

        new_rid = next_rid(used_rids)
        template_rel_id_map[rel.get("Id")] = new_rid
        new_rel = copy.deepcopy(rel)
        new_rel.set("Id", new_rid)
        new_rel.set("Target", new_target.removeprefix("word/"))
        input_rels_root.append(new_rel)

        template_override = template_content_types_root.xpath(
            f"./ct:Override[@PartName='/{old_target}']", namespaces=NS
        )
        if template_override:
            ensure_content_type_override(
                content_types_root,
                new_target,
                template_override[0].get("ContentType"),
            )

    template_sect = template_doc_root.xpath(".//w:sectPr", namespaces=NS)[-1]
    replacement_children = []
    for child in template_sect:
        cloned = copy.deepcopy(child)
        rel_id = cloned.get(qn("r:id"))
        if rel_id and rel_id in template_rel_id_map:
            cloned.set(qn("r:id"), template_rel_id_map[rel_id])
        replacement_children.append(cloned)

    for sect in input_doc_root.xpath(".//w:sectPr", namespaces=NS):
        for child in list(sect):
            sect.remove(child)
        for child in replacement_children:
            sect.append(copy.deepcopy(child))

    save_xml(input_dir / "word/document.xml", input_doc_root)
    save_xml(input_dir / "word/_rels/document.xml.rels", input_rels_root)
    save_xml(input_dir / "[Content_Types].xml", content_types_root)


def rezip_directory(source_dir: Path, output_path: Path) -> None:
    with ZipFile(output_path, "w", ZIP_DEFLATED) as zf:
        for path in sorted(source_dir.rglob("*")):
            if path.is_file():
                zf.write(path, path.relative_to(source_dir).as_posix())


def copy_template_into_output(input_path: Path, template_path: Path, output_path: Path) -> None:
    with tempfile.TemporaryDirectory(prefix="futureinternet_") as temp_dir_name:
        temp_dir = Path(temp_dir_name)
        input_dir = temp_dir / "input"
        template_dir = temp_dir / "template"
        with ZipFile(input_path) as input_zip:
            input_zip.extractall(input_dir)
        with ZipFile(template_path) as template_zip:
            template_zip.extractall(template_dir)
        merge_template_structure(input_dir, template_dir)
        rezip_directory(input_dir, output_path)


def format_style_value(style) -> str:
    pf = style.paragraph_format
    font = style.font
    return (
        f"font={font.name or '-'} size={font.size.pt:.1f}pt "
        if font.size is not None
        else f"font={font.name or '-'} size=- "
    ) + (
        f"bold={font.bold} italic={font.italic} "
        f"space_before={pf.space_before.pt:.1f}pt "
        if pf.space_before is not None
        else f"bold={font.bold} italic={font.italic} space_before=- "
    ) + (
        f"space_after={pf.space_after.pt:.1f}pt "
        if pf.space_after is not None
        else "space_after=- "
    ) + (
        f"first_indent={pf.first_line_indent.cm:.3f}cm "
        if pf.first_line_indent is not None
        else "first_indent=- "
    ) + (
        f"alignment={pf.alignment}"
    )


def build_template_inventory(template_path: Path) -> tuple[object, list[str]]:
    template_doc = open_template_document(template_path)
    lines = [f"Template inventory: {template_path}", "Paragraph styles:"]
    for style in template_doc.styles:
        if style.type != WD_STYLE_TYPE.PARAGRAPH:
            continue
        lines.append(f"- {style.name}: {format_style_value(style)}")

    lines.append("Headers and footers:")
    for idx, section in enumerate(template_doc.sections, start=1):
        lines.append(
            f"- Section {idx}: header={section.header.is_linked_to_previous} footer={section.footer.is_linked_to_previous} "
            f"different_first_page={section.different_first_page_header_footer}"
        )
        lines.append(f"  default header: {story_text(section.header)!r}")
        lines.append(f"  even header: {story_text(section.even_page_header)!r}")
        lines.append(f"  first header: {story_text(section.first_page_header)!r}")
        lines.append(f"  default footer: {story_text(section.footer)!r}")
        lines.append(f"  even footer: {story_text(section.even_page_footer)!r}")
        lines.append(f"  first footer: {story_text(section.first_page_footer)!r}")
        lines.append(
            "  page setup: "
            f"top={section.top_margin.cm:.3f}cm bottom={section.bottom_margin.cm:.3f}cm "
            f"left={section.left_margin.cm:.3f}cm right={section.right_margin.cm:.3f}cm "
            f"width={section.page_width.cm:.3f}cm height={section.page_height.cm:.3f}cm orientation={section.orientation}"
        )

    with ZipFile(template_path) as zf:
        settings = etree.fromstring(zf.read("word/settings.xml"))
        document = etree.fromstring(zf.read("word/document.xml"))
        line_numbers = document.xpath(".//w:sectPr/w:lnNumType", namespaces=NS)
        lines.append(
            f"Line numbering active: {'yes' if line_numbers else 'no'}"
            + (f" ({etree.tostring(line_numbers[0], encoding='unicode')})" if line_numbers else "")
        )
        even_odd = settings.xpath(".//w:evenAndOddHeaders", namespaces=NS)
        lines.append(f"Odd/even different headers enabled: {'yes' if even_odd else 'no'}")
    return template_doc, lines


def compare_section_metrics(template_doc, generated_doc) -> list[str]:
    lines = []
    template_section = template_doc.sections[0]
    for idx, section in enumerate(generated_doc.sections, start=1):
        metrics = {
            "top_margin": (section.top_margin.cm, template_section.top_margin.cm),
            "bottom_margin": (section.bottom_margin.cm, template_section.bottom_margin.cm),
            "left_margin": (section.left_margin.cm, template_section.left_margin.cm),
            "right_margin": (section.right_margin.cm, template_section.right_margin.cm),
            "page_width": (section.page_width.cm, template_section.page_width.cm),
            "page_height": (section.page_height.cm, template_section.page_height.cm),
        }
        status = all(abs(actual - expected) < 0.01 for actual, expected in metrics.values())
        lines.append(f"- Section {idx} page setup: {'PASS' if status else 'FAIL'}")
        for key, (actual, expected) in metrics.items():
            lines.append(f"  {key}: generated={actual:.3f}cm template={expected:.3f}cm")
        lines.append(
            f"  different_first_page: generated={section.different_first_page_header_footer} template={template_section.different_first_page_header_footer}"
        )
    return lines


def has_line_numbering(path: Path) -> tuple[bool, list[dict[str, str]]]:
    with ZipFile(path) as zf:
        document = etree.fromstring(zf.read("word/document.xml"))
        sect_ln = document.xpath(".//w:sectPr/w:lnNumType", namespaces=NS)
    return bool(sect_ln), [dict(sorted(node.attrib.items())) for node in sect_ln]


def header_footer_summary(path: Path) -> dict[str, list[str]]:
    summary = {"headers": [], "footers": [], "header_parts": [], "footer_parts": []}
    with ZipFile(path) as zf:
        rels = etree.fromstring(zf.read("word/_rels/document.xml.rels"))
        for rel in rels:
            rel_type = rel.get("Type")
            if rel_type not in {REL_HEADER, REL_FOOTER}:
                continue
            target = f"word/{rel.get('Target')}"
            xml_root = etree.fromstring(zf.read(target))
            texts = xml_texts(xml_root)
            bucket = "headers" if rel_type == REL_HEADER else "footers"
            bucket_parts = "header_parts" if rel_type == REL_HEADER else "footer_parts"
            summary[bucket].extend(texts)
            summary[bucket_parts].append(target)
    return summary


def build_compliance_report(
    template_path: Path,
    output_path: Path,
    tracker: ComplianceTracker,
) -> list[str]:
    template_doc = open_template_document(template_path)
    generated_doc = Document(str(output_path))
    template_line_numbers, template_ln_xml = has_line_numbering(template_path)
    generated_line_numbers, generated_ln_xml = has_line_numbering(output_path)
    template_hf = header_footer_summary(template_path)
    generated_hf = header_footer_summary(output_path)

    lines = ["Compliance report", f"Template: {template_path}", f"Generated: {output_path}", ""]
    lines.append("Style mapping used:")
    for role, style_name in sorted(tracker.role_to_style.items()):
        lines.append(f"- {role}: {style_name}")

    lines.append("")
    lines.append("Paragraph styles applied:")
    for style_name, count in sorted(tracker.paragraph_style_usage.items()):
        in_template = any(s.name == style_name for s in template_doc.styles if s.type == WD_STYLE_TYPE.PARAGRAPH)
        lines.append(f"- {style_name}: {count} paragraph(s) ({'template style' if in_template else 'missing from template'})")

    lines.append("")
    lines.append("Page setup comparison:")
    lines.extend(compare_section_metrics(template_doc, generated_doc))

    lines.append("")
    template_ln_signature = template_ln_xml[0] if template_ln_xml else None
    generated_ln_match = all(xml == template_ln_signature for xml in generated_ln_xml) if template_ln_signature else not generated_ln_xml
    line_numbering_pass = template_line_numbers == generated_line_numbers and generated_ln_match
    lines.append(f"Line numbering: {'PASS' if line_numbering_pass else 'FAIL'}")
    lines.append(f"- template active={template_line_numbers} xml={template_ln_xml}")
    lines.append(f"- generated active={generated_line_numbers} xml={generated_ln_xml}")

    lines.append("")
    headers_match = len(template_hf["header_parts"]) == len(generated_hf["header_parts"]) and bool(generated_hf["headers"])
    footers_match = len(template_hf["footer_parts"]) == len(generated_hf["footer_parts"]) and bool(generated_hf["footers"])
    lines.append(f"Header presence: {'PASS' if headers_match else 'FAIL'}")
    lines.append(f"- template header parts={template_hf['header_parts']}")
    lines.append(f"- generated header parts={generated_hf['header_parts']}")
    lines.append(f"- generated header text={generated_hf['headers']}")
    lines.append(f"Footer presence: {'PASS' if footers_match else 'FAIL'}")
    lines.append(f"- template footer parts={template_hf['footer_parts']}")
    lines.append(f"- generated footer parts={generated_hf['footer_parts']}")
    lines.append(f"- generated footer text={generated_hf['footers']}")
    return lines


def convert(input_path: str, output_path: str | None = None, template_path: str | None = None) -> Path:
    input_file = Path(input_path).resolve()
    script_dir = Path(__file__).resolve().parent
    template_file = Path(template_path).resolve() if template_path else script_dir / "futureinternet-template.dot"
    if output_path is None:
        output_file = input_file.with_name(f"{input_file.stem}_futureinternet.docx")
    else:
        output_file = Path(output_path).resolve()

    template_doc, inventory_lines = build_template_inventory(template_file)
    print("\n".join(inventory_lines))

    source_doc = Document(str(input_file))
    source_detector = RoleDetector(source_doc.paragraphs)

    copy_template_into_output(input_file, template_file, output_file)
    doc = Document(str(output_file))
    resolver = StyleResolver(template_doc)
    tracker = ComplianceTracker()

    paragraphs = doc.paragraphs
    detector = source_detector
    if len(paragraphs) != len(detector.roles):
        raise RuntimeError(
            f"Paragraph count changed during template merge: source={len(detector.roles)} output={len(paragraphs)}"
        )
    for role in {
        RoleDetector.TITLE,
        RoleDetector.AUTHORS,
        RoleDetector.AFFILIATIONS,
        RoleDetector.ABSTRACT_H,
        RoleDetector.ABSTRACT,
        RoleDetector.KEYWORDS_H,
        RoleDetector.KEYWORDS,
        RoleDetector.HEADING1,
        RoleDetector.HEADING2,
        RoleDetector.HEADING3,
        RoleDetector.BODY,
        RoleDetector.REF_HEAD,
        RoleDetector.REF_ITEM,
        RoleDetector.BLANK,
    }:
        tracker.role_to_style[role] = resolver.resolve(role, fallback="Normal")
    tracker.role_to_style[RoleDetector.CAPTION] = "figure/table caption resolved by text"

    for paragraph, role in zip(paragraphs, detector.roles):
        style_name = resolver.resolve(role, text=_full_text(paragraph), fallback="Normal")
        apply_style_to_paragraph(paragraph, style_name, tracker)

    apply_table_styles(doc, resolver, tracker)
    doc.save(str(output_file))

    role_counts = Counter(detector.roles)
    print("Paragraph roles detected:")
    for role, count in sorted(role_counts.items()):
        print(f"- {role}: {count}")

    report_lines = build_compliance_report(template_file, output_file, tracker)
    report_path = script_dir / "compliance_report.txt"
    report_path.write_text("\n".join(report_lines) + "\n", encoding="utf-8")
    print("\n".join(report_lines))
    print(f"Saved: {output_file}")
    print(f"Compliance report: {report_path}")
    return output_file


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert a .docx manuscript to the Future Internet MDPI template.",
    )
    parser.add_argument("input_docx", help="Source .docx file")
    parser.add_argument("output_docx", nargs="?", help="Output .docx file")
    parser.add_argument(
        "--template",
        default=str(Path(__file__).resolve().parent / "futureinternet-template.dot"),
        help="Path to the Future Internet .dot template",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    convert(args.input_docx, args.output_docx, args.template)
