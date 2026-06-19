from __future__ import annotations

import datetime as dt
import re
import zipfile
from pathlib import Path
from xml.sax.saxutils import escape


ROOT = Path(__file__).resolve().parents[1]
PLAN = ROOT / "blog-image-batch-plan.md"
OUT_DIR = ROOT / "5_BATCH_EXPORT"
OUT_FILE = OUT_DIR / "cars24-batch-processing-template.xlsx"


HEADERS = [
    "Item id",
    "Date",
    "Blog title",
    "Blog description",
    "URL",
    "Number of slides",
    "Image width px",
    "Image height px",
    "Image theme",
    "Visible image text",
    "Custom visible text",
    "Logo",
    "Hero type",
    "Image direction",
    "Description context",
    "Layout archetype",
    "Prompt priority",
    "Specific guardrail",
    "Batch",
    "Approved references / asset links",
    "Status",
    "Notes",
    "Validation warnings",
]

REQUIRED = {"Blog title", "URL", "Image width px", "Image height px", "Image theme", "Hero type", "Image direction", "Status"}

LISTS = {
    "Themes": ["Dark", "Light", "Custom"],
    "VisibleText": ["Blog title only", "Custom", "None"],
    "Logo": ["None by default", "Cars24 logo", "Third-party logo", "Approved supplied logo"],
    "HeroType": ["Abstract illustration", "Photo illustration", "Photo-based", "Infographic", "Portrait illustration"],
    "Priority": ["Balanced", "Hero-led", "Headline-led"],
    "Status": ["Ready", "Needs review", "Skip", "Generated"],
    "Layout": [
        "Headline-left + system-right",
        "Headline-left + flow-right",
        "Centre workflow",
        "Headline-left + hero-right",
        "Centre lockup",
        "Data-led split",
        "Three-figure hero",
        "Product-builder scene",
        "Dashboard-to-action",
        "Restrained centre",
        "Bold hero-right",
        "Map/chain layout",
        "Roadmap arc",
        "Showroom hero",
        "Metaphor-led",
        "Portrait-right",
        "Car cutaway",
        "People-led hero",
        "Product promise",
        "Metaphor portrait",
        "Minimal title-led",
        "Flowing system",
        "Timeline",
        "Architecture diagram",
        "Confusion-to-clarity path",
        "Waveform guardrail",
        "Headline-dominant",
        "Ownership system",
        "Centre horizon",
        "Reflective split",
        "Calm checklist",
        "Patterned life/work rhythm",
        "Process path",
        "Loop-to-output",
        "Minimal repeated form",
        "Road-risk scene",
        "Rating hierarchy",
        "Portrait + trail",
        "Workflow system",
        "Product-tech card",
        "Recommendation paths",
        "Calm people hero",
        "Docs-to-data",
        "Signal stream",
        "Voice intelligence",
        "Timeline portrait",
        "Motion interface",
        "Circular system",
    ],
    "SlideCounts": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
}


def col_name(n: int) -> str:
    out = ""
    while n:
        n, rem = divmod(n - 1, 26)
        out = chr(65 + rem) + out
    return out


def cell_ref(row: int, col: int) -> str:
    return f"{col_name(col)}{row}"


def split_md_row(line: str) -> list[str]:
    body = line.strip().strip("|")
    return [part.strip().replace("\\|", "|") for part in body.split("|")]


def parse_batch_rows() -> list[list[object]]:
    rows: list[list[object]] = []
    in_table = False
    for line in PLAN.read_text(encoding="utf-8").splitlines():
        if line.startswith("| # | Date | Blog title |"):
            in_table = True
            continue
        if in_table and line.startswith("|---"):
            continue
        if in_table:
            if not line.startswith("|"):
                break
            parts = split_md_row(line)
            if len(parts) < 17:
                continue
            dim = parts[5].lower().replace("px", "").strip()
            match = re.match(r"(\d+)\s*x\s*(\d+)", dim)
            width, height = (1000, 650)
            if match:
                width, height = int(match.group(1)), int(match.group(2))
            rows.append(
                [
                    parts[0],
                    parts[1],
                    parts[2],
                    parts[3],
                    parts[4],
                    1,
                    width,
                    height,
                    parts[6],
                    parts[7],
                    "",
                    parts[8],
                    parts[9],
                    parts[10],
                    parts[11],
                    parts[12],
                    parts[13],
                    parts[14],
                    parts[15],
                    "",
                    "Ready" if parts[16] == "Planned" else parts[16],
                    "",
                    "",
                ]
            )
    return rows


def date_to_serial(value: dt.date) -> int:
    return (value - dt.date(1899, 12, 30)).days


def sheet_xml(
    rows: list[list[object]],
    *,
    merges: list[str] | None = None,
    cols: list[tuple[int, int, float]] | None = None,
    validations: list[str] | None = None,
    freeze: str | None = None,
    autofilter: str | None = None,
    hidden: bool = False,
) -> str:
    parts = [
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
        '<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" '
        'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">',
    ]
    if cols:
        parts.append("<cols>")
        for min_col, max_col, width in cols:
            parts.append(f'<col min="{min_col}" max="{max_col}" width="{width}" customWidth="1"/>')
        parts.append("</cols>")
    if freeze:
        x_split = re.match(r"([A-Z]+)(\d+)", freeze)
        if x_split:
            col_letters, row_s = x_split.groups()
            col_idx = sum((ord(c) - 64) * (26 ** i) for i, c in enumerate(reversed(col_letters)))
            row_idx = int(row_s)
            parts.append(
                "<sheetViews><sheetView workbookViewId=\"0\"><pane "
                f'xSplit="{col_idx - 1}" ySplit="{row_idx - 1}" topLeftCell="{freeze}" '
                'activePane="bottomRight" state="frozen"/></sheetView></sheetViews>'
            )
    parts.append("<sheetData>")
    for r_idx, row in enumerate(rows, start=1):
        parts.append(f'<row r="{r_idx}">')
        for c_idx, value in enumerate(row, start=1):
            ref = cell_ref(r_idx, c_idx)
            style = 1 if r_idx == 1 else 0
            if isinstance(value, tuple) and value[0] == "formula":
                parts.append(f'<c r="{ref}" s="{style}"><f>{escape(value[1])}</f></c>')
            elif isinstance(value, (int, float)) and not isinstance(value, bool):
                parts.append(f'<c r="{ref}" s="{style}"><v>{value}</v></c>')
            elif isinstance(value, dt.date):
                parts.append(f'<c r="{ref}" s="2"><v>{date_to_serial(value)}</v></c>')
            elif value is None or value == "":
                parts.append(f'<c r="{ref}" s="{style}"/>')
            else:
                text = escape(str(value))
                parts.append(f'<c r="{ref}" s="{style}" t="inlineStr"><is><t>{text}</t></is></c>')
        parts.append("</row>")
    parts.append("</sheetData>")
    if autofilter:
        parts.append(f'<autoFilter ref="{autofilter}"/>')
    if merges:
        parts.append(f'<mergeCells count="{len(merges)}">')
        for ref in merges:
            parts.append(f'<mergeCell ref="{ref}"/>')
        parts.append("</mergeCells>")
    if validations:
        parts.append(f'<dataValidations count="{len(validations)}">')
        parts.extend(validations)
        parts.append("</dataValidations>")
    if hidden:
        parts.append("<sheetProtection sheet=\"1\" objects=\"1\" scenarios=\"1\"/>")
    parts.append("</worksheet>")
    return "".join(parts)


def validation(range_ref: str, list_formula: str, prompt: str) -> str:
    return (
        f'<dataValidation type="list" allowBlank="1" showInputMessage="1" sqref="{range_ref}">'
        f'<formula1>{escape(list_formula)}</formula1>'
        f'<promptTitle>Choose a value</promptTitle><prompt>{escape(prompt)}</prompt></dataValidation>'
    )


def workbook_xml(sheet_names: list[str]) -> str:
    sheets = []
    for idx, name in enumerate(sheet_names, start=1):
        state = ' state="hidden"' if name == "Lists" else ""
        sheets.append(f'<sheet name="{escape(name)}" sheetId="{idx}" r:id="rId{idx}"{state}/>')
    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" '
        'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
        "<sheets>"
        + "".join(sheets)
        + "</sheets></workbook>"
    )


def workbook_rels(sheet_count: int) -> str:
    rels = [
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">',
    ]
    for idx in range(1, sheet_count + 1):
        rels.append(
            f'<Relationship Id="rId{idx}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" '
            f'Target="worksheets/sheet{idx}.xml"/>'
        )
    rels.append(
        f'<Relationship Id="rId{sheet_count + 1}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>'
    )
    rels.append("</Relationships>")
    return "".join(rels)


def content_types(sheet_count: int) -> str:
    overrides = [
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
        '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">',
        '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>',
        '<Default Extension="xml" ContentType="application/xml"/>',
        '<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>',
        '<Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/>',
    ]
    for idx in range(1, sheet_count + 1):
        overrides.append(
            f'<Override PartName="/xl/worksheets/sheet{idx}.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>'
        )
    overrides.append("</Types>")
    return "".join(overrides)


def styles_xml() -> str:
    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<styleSheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">'
        '<fonts count="2"><font><sz val="11"/><name val="Aptos"/></font>'
        '<font><b/><color rgb="FFFFFFFF"/><sz val="11"/><name val="Aptos"/></font></fonts>'
        '<fills count="3"><fill><patternFill patternType="none"/></fill><fill><patternFill patternType="gray125"/></fill>'
        '<fill><patternFill patternType="solid"><fgColor rgb="FF4736FE"/><bgColor indexed="64"/></patternFill></fill></fills>'
        '<borders count="1"><border><left/><right/><top/><bottom/><diagonal/></border></borders>'
        '<cellStyleXfs count="1"><xf numFmtId="0" fontId="0" fillId="0" borderId="0"/></cellStyleXfs>'
        '<cellXfs count="3"><xf numFmtId="0" fontId="0" fillId="0" borderId="0" xfId="0"/>'
        '<xf numFmtId="0" fontId="1" fillId="2" borderId="0" xfId="0" applyFont="1" applyFill="1"/>'
        '<xf numFmtId="14" fontId="0" fillId="0" borderId="0" xfId="0" applyNumberFormat="1"/></cellXfs>'
        '<cellStyles count="1"><cellStyle name="Normal" xfId="0" builtinId="0"/></cellStyles>'
        '</styleSheet>'
    )


def rels_root() -> str:
    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/>'
        "</Relationships>"
    )


def build() -> None:
    examples = parse_batch_rows()
    blank_rows = [HEADERS]
    for idx in range(1, 101):
        formula = (
            f'TEXTJOIN("; ",TRUE,IF(C{idx+1}="","Missing blog title",""),'
            f'IF(E{idx+1}="","Missing URL",""),IF(F{idx+1}="","Missing number of slides",""),'
            f'IF(OR(F{idx+1}<1,F{idx+1}>10),"Number of slides must be 1-10",""),'
            f'IF(G{idx+1}="","Missing width",""),IF(H{idx+1}="","Missing height",""),'
            f'IF(I{idx+1}="","Missing theme",""),IF(M{idx+1}="","Missing hero type",""),'
            f'IF(N{idx+1}="","Missing image direction",""),IF(U{idx+1}="","Missing status",""),'
            f'IF(AND(J{idx+1}="Custom",K{idx+1}=""),"Custom visible text missing",""))'
        )
        blank_rows.append([idx, "", "", "", "", 1, 1000, 650, "Dark", "Blog title only", "", "None by default", "", "", "", "", "Balanced", "", "", "", "Needs review", "", ("formula", formula)])

    readme = [
        ["Cars24 batch processing template", "", ""],
        ["Use this workbook to upload repeatable batch image jobs.", "", ""],
        ["Step", "Action", "Notes"],
        ["1", "Fill the Batch upload sheet", "One row equals one generated output request. Number of slides defaults to 1; use a higher value for carousel rows."],
        ["2", "Keep required fields complete", "Validation warnings should be blank before upload; slide counts must be between 1 and 10."],
        ["3", "Use dropdowns where present", "Dropdown values map to Maker Agent batch-processing rules."],
        ["4", "Attach references by path or URL", "Only use approved assets; do not fabricate third-party logos."],
        ["5", "Upload the workbook", "Rows marked Ready can be processed; Skip rows are ignored."],
        ["Default dimensions", "1000 x 650 px", "Matches the current Autonauts blog-cover batch."],
        ["Default theme", "Dark Cars24 brand blue", "Can be changed row by row."],
        ["Default visible text", "Blog title only", "Description remains prompt context only."],
    ]

    guide = [["Field", "Required", "How to use"]]
    descriptions = {
        "Item id": "Unique row identifier. Can be numeric or a stable external ID.",
        "Date": "Publish or target date. Optional but useful for scheduling.",
        "Blog title": "Primary visible headline unless Visible image text is Custom or None.",
        "Blog description": "Planning and prompt context. Not visible by default.",
        "URL": "Canonical article or destination URL.",
        "Number of slides": "Defaults to 1. Use 2-5 for carousel rows; above 5 should be intentionally confirmed before generation.",
        "Image width px": "Output width in pixels. Default is 1000.",
        "Image height px": "Output height in pixels. Default is 650.",
        "Image theme": "Cars24 theme to apply: Dark, Light, or Custom.",
        "Visible image text": "Controls whether the title, custom text, or no text appears in the output.",
        "Custom visible text": "Use only when Visible image text is Custom.",
        "Logo": "Logo handling. Use approved logo references only.",
        "Hero type": "Primary visual treatment for the generated image.",
        "Image direction": "Short scene/metaphor direction for the image prompt.",
        "Description context": "Key facts, product names, people, risks, and constraints for prompt context.",
        "Layout archetype": "Composition direction. Optional but helps consistency.",
        "Prompt priority": "Whether headline, hero, or balance leads the composition.",
        "Specific guardrail": "Anything the generator must avoid.",
        "Batch": "Operational grouping for chunked processing.",
        "Approved references / asset links": "Approved local paths or URLs for logos, people, products, or style references.",
        "Status": "Ready rows are processable; Needs review rows should be checked first.",
        "Notes": "Internal production notes.",
        "Validation warnings": "Formula-generated checks. Keep blank before upload.",
    }
    for header in HEADERS:
        guide.append([header, "Yes" if header in REQUIRED else "No", descriptions[header]])

    list_rows = []
    max_len = max(len(v) for v in LISTS.values())
    list_rows.append(list(LISTS.keys()))
    for i in range(max_len):
        list_rows.append([values[i] if i < len(values) else "" for values in LISTS.values()])

    example_rows = [HEADERS] + examples
    sheets = ["README", "Batch upload", "Example rows", "Field guide", "Lists"]
    validations = [
        validation("F2:F101", "Lists!$H$2:$H$11", "Choose number of slides. Defaults to 1."),
        validation("I2:I101", "Lists!$A$2:$A$4", "Dark, Light, or Custom."),
        validation("J2:J101", "Lists!$B$2:$B$4", "Choose what text appears in the image."),
        validation("L2:L101", "Lists!$C$2:$C$5", "Choose logo handling."),
        validation("M2:M101", "Lists!$D$2:$D$6", "Choose the hero treatment."),
        validation("P2:P101", "Lists!$G$2:$G$51", "Choose a layout archetype when known."),
        validation("Q2:Q101", "Lists!$E$2:$E$4", "Choose composition priority."),
        validation("U2:U101", "Lists!$F$2:$F$5", "Choose processing status."),
    ]

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(OUT_FILE, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("[Content_Types].xml", content_types(len(sheets)))
        zf.writestr("_rels/.rels", rels_root())
        zf.writestr("xl/workbook.xml", workbook_xml(sheets))
        zf.writestr("xl/_rels/workbook.xml.rels", workbook_rels(len(sheets)))
        zf.writestr("xl/styles.xml", styles_xml())
        zf.writestr("xl/worksheets/sheet1.xml", sheet_xml(readme, merges=["A1:C1"], cols=[(1, 1, 24), (2, 2, 38), (3, 3, 80)]))
        zf.writestr(
            "xl/worksheets/sheet2.xml",
            sheet_xml(
                blank_rows,
                cols=[
                    (1, 1, 10),
                    (2, 2, 14),
                    (3, 4, 36),
                    (5, 5, 52),
                    (6, 6, 17),
                    (7, 8, 14),
                    (9, 13, 20),
                    (14, 18, 34),
                    (19, 19, 10),
                    (20, 23, 34),
                ],
                validations=validations,
                freeze="A2",
                autofilter=f"A1:{cell_ref(101, len(HEADERS))}",
            ),
        )
        zf.writestr(
            "xl/worksheets/sheet3.xml",
            sheet_xml(
                example_rows,
                cols=[(1, 1, 8), (2, 2, 14), (3, 4, 42), (5, 5, 52), (6, 23, 24)],
                freeze="A2",
                autofilter=f"A1:{cell_ref(len(example_rows), len(HEADERS))}",
            ),
        )
        zf.writestr("xl/worksheets/sheet4.xml", sheet_xml(guide, cols=[(1, 1, 28), (2, 2, 12), (3, 3, 90)], freeze="A2", autofilter=f"A1:C{len(guide)}"))
        zf.writestr("xl/worksheets/sheet5.xml", sheet_xml(list_rows, cols=[(1, len(LISTS), 28)], hidden=True))


if __name__ == "__main__":
    build()
    print(OUT_FILE)
