#!/usr/bin/env python3
"""Final precision extraction of the best Byzantine patterns."""
from PIL import Image
import os

SRC = os.path.dirname(os.path.abspath(__file__)) + "/source"
OUT = os.path.dirname(os.path.abspath(__file__)) + "/final"
os.makedirs(OUT, exist_ok=True)

def crop(src, name, box, desc):
    img = Image.open(os.path.join(SRC, src))
    c = img.crop(box)
    path = os.path.join(OUT, f"{name}.png")
    c.save(path, "PNG")
    print(f"  ✓ {name}.png ({c.size[0]}x{c.size[1]}) — {desc}")

print("Final Byzantine Pattern Extraction")
print("=" * 60)

# ── JONES PLATE 30 (3244x5000) ──
print("\n▸ Jones Plate 30")

# Band 41 — green wave/anthemion on dark ground (the 9/10 winner)
crop("jones-byzantine-3.jpg", "wave-anthemion",
    (1540, 4580, 2220, 4770), "★ Green wave/anthemion on black — best divider")

# Band 42 — interlace star lattice (8/10 runner-up)
crop("jones-byzantine-3.jpg", "interlace-stars",
    (2230, 4580, 3000, 4770), "Red/green star lattice interlace")

# Band 40 — green leaf scales (needs top trim)
crop("jones-byzantine-3.jpg", "leaf-scales",
    (750, 4630, 1530, 4770), "Green leaf petal scales on dark — trimmed")

# Band 3 — triangular geometric (4/5 from first pass)
crop("jones-byzantine-3.jpg", "triangle-geo",
    (280, 2340, 3000, 2480), "Triangular geometric border strip")

# ── JONES PLATE 29 (3332x5000) ──
print("\n▸ Jones Plate 29")

# The full left panel — has the best horizontal bands inside it
# Extract just the tulip/vine band from the top of the left panel
crop("jones-byzantine-2.jpg", "tulip-vine-band",
    (100, 4050, 1150, 4250), "Tulip & vine band — ornate header ribbon")

# The stripe dividers from the left panel
crop("jones-byzantine-2.jpg", "stripe-divider",
    (100, 4240, 1150, 4310), "Red-white-blue stripe divider — thin separator")

# Lower vine medallion band from left panel
crop("jones-byzantine-2.jpg", "vine-medallion",
    (100, 4310, 1150, 4600), "Circular vine medallions — footer ribbon")

# Bottom band from right panel — circular tulips
crop("jones-byzantine-2.jpg", "circular-tulips",
    (2300, 4500, 3300, 4700), "Circular tulip medallion band")

# ── DOLMETSCH TABLE 32 (3511x5178) ──
# Section offsets: top=200, mid=1200, lower=2600, bottom=4000
print("\n▸ Dolmetsch Table 32")

# Vitruvian wave band — Section 4 y~540-700 → absolute y=4540-4700
crop("dolmetsch-table32.jpg", "vitruvian-wave",
    (100, 4540, 3400, 4720), "★ Vitruvian wave scroll — best Dolmetsch divider")

# Green vine architrave — Section 2 y~230-290 → absolute y=1430-1490
crop("dolmetsch-table32.jpg", "vine-architrave",
    (100, 1400, 3400, 1520), "Green/gold vine scroll architrave")

# Byzantine cross — Section 2 y~550-850 → absolute y=1750-2050
crop("dolmetsch-table32.jpg", "byzantine-cross",
    (1200, 1700, 2300, 2100), "Byzantine cross with roundels — centerpiece")

# Confronted birds — Section 1 y~150-450 → absolute y=350-650
crop("dolmetsch-table32.jpg", "confronted-birds",
    (800, 350, 2700, 700), "Confronted roosters — Byzantine paradise motif")

# Trefoil vine band — Section 3 y~540-640 → absolute y=3140-3240
crop("dolmetsch-table32.jpg", "trefoil-vine",
    (100, 3100, 3400, 3280), "Trefoil vine band with striped borders")

# Blue wave scroll — Section 3 y~280-360 → absolute y=2880-2960
crop("dolmetsch-table32.jpg", "blue-wave",
    (100, 2860, 3400, 2980), "Blue wave/vine scroll band")

# Thin top rule bands — Section 1 y~80-130 → absolute y=280-330
crop("dolmetsch-table32.jpg", "thin-rules",
    (100, 270, 3400, 340), "Thin horizontal rule bands — minimal divider")

# Large rosette medallions from bottom section
crop("dolmetsch-table32.jpg", "rosette-medallions",
    (200, 4050, 2200, 4500), "Rosette/sunburst medallions — standalone roundels")

print(f"\nTotal: {len(os.listdir(OUT))} final patterns")
