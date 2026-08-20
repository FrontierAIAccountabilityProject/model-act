#!/usr/bin/env python3
"""
build_reviewers_copy.py — deterministic line-numbered reviewer's copy of the Model Act.

    python3 tools/build_reviewers_copy.py model_act_v3_4.txt archive/model_act_v3_4_reviewers_copy.pdf

Reads the authoritative statutory text and emits a print-and-annotate PDF: one source line
per numbered line, 1.5 spacing, wide right margin, page/line citable, no typography beyond
a monospaced face. Nothing is reflowed, reordered, or reworded; the PDF's line numbers are
the source file's line numbers, so "p. 9, l. 236" and "model_act_v3_4.txt#L236" name the
same text.

Reproducibility: dates are pinned to the v3.4 tag date and the PDF's document ID is derived
from the source text's own sha256, so nothing in the output depends on the build clock or the
machine. Two builds of the same source are byte-identical — verify by building twice and
comparing sha256sums.

Public domain (CC0), like everything else here.
"""
import sys, hashlib
from reportlab.lib.pagesizes import letter, landscape
from reportlab.pdfgen import canvas

FIXED_DATE = "D:20260819000000+00'00'"   # the v3.4 tag date; keeps builds byte-identical

def build(src_path, out_path):
    src = open(src_path, encoding="utf-8").read()
    digest = hashlib.sha256(src.encode("utf-8")).hexdigest()
    lines = src.split("\n")

    W, H = landscape(letter)                            # 792 x 612
    LEFT, RIGHT_MARGIN, TOP, BOTTOM = 54, 200, 60, 48    # 200pt (2.8in) margin to write in
    LEADING, SIZE, NUM_SIZE = 13, 7.6, 6                 # ~1.5 spacing; fits 171-char lines
    NUMCOL, TEXTCOL = LEFT, LEFT + 30
    CHARW = SIZE * 0.6                                   # Courier is monospaced
    MAXCH = int((W - RIGHT_MARGIN - TEXTCOL) / CHARW)

    c = canvas.Canvas(out_path, pagesize=landscape(letter), invariant=1)
    c.setTitle("Model Act — Frontier AI Public Welfare Offenses (v3.4, reviewer's copy)")
    c.setAuthor("llmaolaw")
    c.setSubject("Line-numbered reviewer's copy. Research draft; never enacted. CC0.")
    c.setKeywords("model legislation; responsible corporate officer doctrine; frontier AI")
    c.setCreator("tools/build_reviewers_copy.py")

    page_ref = [1]
    y = H - TOP

    def header():
        c.setFont("Helvetica", 7)
        c.setFillGray(0.35)
        c.drawString(LEFT, H - 40,
                     "MODEL ACT — FRONTIER AI PUBLIC WELFARE OFFENSES · v3.4 · "
                     "REVIEWER'S COPY · RESEARCH DRAFT, NEVER ENACTED")
        c.setFillGray(0)

    def footer(n):
        c.setFont("Helvetica", 7)
        c.setFillGray(0.35)
        c.drawString(LEFT, 30, f"page {n}")
        c.drawRightString(W - RIGHT_MARGIN + 140, 40,
                          "cite as: Model Act § __ (v3.4) · p. __, l. __ · "
                          "sha256 " + digest[:12])
        c.setFillGray(0)

    header()
    for n, line in enumerate(lines, 1):
        if y < BOTTOM + LEADING:
            footer(page_ref[0]); c.showPage(); page_ref[0] += 1; header(); y = H - TOP
        c.setFont("Helvetica", NUM_SIZE); c.setFillGray(0.55)
        c.drawRightString(NUMCOL + 26, y, str(n))
        c.setFillGray(0); c.setFont("Courier", SIZE)
        if len(line) <= MAXCH:
            c.drawString(TEXTCOL, y, line)
            y -= LEADING
        else:
            # never lose text: overflow continues on the next printed row, unnumbered,
            # indented, so the source-line correspondence stays visible
            c.drawString(TEXTCOL, y, line[:MAXCH]); y -= LEADING
            rest = line[MAXCH:]
            while rest:
                if y < BOTTOM + LEADING:
                    footer(page_ref[0]); c.showPage(); page_ref[0] += 1; header(); y = H - TOP
                c.drawString(TEXTCOL + 12, y, rest[:MAXCH - 2]); y -= LEADING
                rest = rest[MAXCH - 2:]
    footer(page_ref[0])

    c.setPageCompression(1)
    c._doc.info.creationDate = FIXED_DATE
    c._doc.info.modDate = FIXED_DATE
    # deterministic document ID: derived from the source text, never from the clock
    c._doc._ID = b"[<%s><%s>]" % (digest[:32].encode(), digest[:32].encode())
    c.save()

    print(f"source sha256: {digest}")
    print(f"pages: {page_ref[0]} · lines: {len(lines)} · out: {out_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    build(sys.argv[1], sys.argv[2])
