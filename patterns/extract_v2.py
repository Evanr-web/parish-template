#!/usr/bin/env python3
"""Precise Byzantine pattern extraction v2 — based on strip-by-strip analysis."""
from PIL import Image
import os

SRC = os.path.dirname(os.path.abspath(__file__)) + "/source"
OUT = os.path.dirname(os.path.abspath(__file__)) + "/extracted_v2"
os.makedirs(OUT, exist_ok=True)

def crop_and_save(src_file, name, box, desc=""):
    """box = (left, upper, right, lower)"""
    img = Image.open(os.path.join(SRC, src_file))
    cropped = img.crop(box)
    out = os.path.join(OUT, f"{name}.png")
    cropped.save(out, "PNG")
    w, h = cropped.size
    print(f"  ✓ {name}.png ({w}x{h}) — {desc}")

print("=" * 60)
print("Byzantine Pattern Extraction v2")
print("=" * 60)

# ── JONES PLATE 30 (3244x5000) ──
print("\n▸ Jones Plate 30 (Byzantine No. 3)")

# Strip 4 bands (y=2000-2500) — the horizontal ornamental bands
crop_and_save("jones-byzantine-3.jpg", "p30-wavy-band",
    (280, 2050, 3000, 2180), "Green wavy border strip")
crop_and_save("jones-byzantine-3.jpg", "p30-circle-band",
    (280, 2180, 3000, 2330), "Black/red circles ornamental band")
crop_and_save("jones-byzantine-3.jpg", "p30-dark-geo-band",
    (280, 2340, 3000, 2480), "Dark geometric band")

# Strip 7-8 bands (y=3500-4500) — red and green ornamental bands
crop_and_save("jones-byzantine-3.jpg", "p30-red-ornament",
    (280, 3750, 3000, 3920), "Red ornamental ribbon")
crop_and_save("jones-byzantine-3.jpg", "p30-circular-pattern",
    (280, 4020, 3000, 4180), "Red circular repeat pattern")
crop_and_save("jones-byzantine-3.jpg", "p30-lower-decor",
    (280, 4250, 3000, 4430), "Lower decorative band")

# Strip 9 — the four narrow bottom bands (y=4500-5000) — individually
crop_and_save("jones-byzantine-3.jpg", "p30-band39-floral",
    (300, 4580, 740, 4770), "Band 39: Red/green floral scroll")
crop_and_save("jones-byzantine-3.jpg", "p30-band40-tulip",
    (750, 4580, 1530, 4770), "Band 40: Green tulip/bud band")
crop_and_save("jones-byzantine-3.jpg", "p30-band41-wave",
    (1540, 4580, 2220, 4770), "Band 41: Green wave/anthemion")
crop_and_save("jones-byzantine-3.jpg", "p30-band42-interlace",
    (2230, 4580, 3000, 4770), "Band 42: Red/green interlace")

# All four bottom bands together
crop_and_save("jones-byzantine-3.jpg", "p30-all-bottom-bands",
    (280, 4560, 3020, 4790), "All 4 bottom narrow bands side by side")

# ── JONES PLATE 29 (3332x5000) ──
print("\n▸ Jones Plate 29 (Byzantine No. 2)")

# Vine scroll bands (strips 8-9, y=4000-4800)
# Left panel vine scroll
crop_and_save("jones-byzantine-2.jpg", "p29-vine-left",
    (100, 4050, 1150, 4800), "Left vine scroll panel on brown")
# Center vine scroll  
crop_and_save("jones-byzantine-2.jpg", "p29-vine-center",
    (1150, 4050, 2300, 4800), "Center vine scroll panel — lapis blue")
# Right panel (tiered bands)
crop_and_save("jones-byzantine-2.jpg", "p29-tiered-right",
    (2300, 4050, 3300, 4800), "Right tiered bands with rosettes")

# Cross/geometric band (strips 5-6, y=2500-3500)
crop_and_save("jones-byzantine-2.jpg", "p29-cross-geo",
    (900, 2800, 2200, 3300), "Cross and geometric repeat panels")

# Chevron/zigzag band (strip 3-4, y=1500-2500)
crop_and_save("jones-byzantine-2.jpg", "p29-chevron",
    (2200, 1700, 3300, 2200), "Rainbow chevron zigzag band")

# Quatrefoil section (strip 0-1, y=0-1000)
crop_and_save("jones-byzantine-2.jpg", "p29-quatrefoil",
    (150, 250, 1100, 700), "Quatrefoil repeat on blue ground")

# ── DOLMETSCH TABLE 32 (3511x5178) ──
print("\n▸ Dolmetsch Table 32")

# Let me try broader crops and let the vision model guide narrowing
# Top section with bird/cross motifs
crop_and_save("dolmetsch-table32.jpg", "dolm-top-section",
    (100, 200, 3400, 1200), "Top section — birds, cross, borders")
# Middle section — bands area
crop_and_save("dolmetsch-table32.jpg", "dolm-mid-section",
    (100, 1200, 3400, 2600), "Middle section — vine scrolls, bands")
# Lower section — geometric and cross patterns  
crop_and_save("dolmetsch-table32.jpg", "dolm-lower-section",
    (100, 2600, 3400, 4000), "Lower section — geometric, crosses")
# Bottom section — roundels, interlace
crop_and_save("dolmetsch-table32.jpg", "dolm-bottom-section",
    (100, 4000, 3400, 5100), "Bottom section — roundels, interlace")

print(f"\n✓ Total: {len(os.listdir(OUT))} patterns in {OUT}")
