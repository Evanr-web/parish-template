#!/usr/bin/env python3
"""Extract Byzantine pattern bands from source plates for parish template."""
from PIL import Image
import os

SRC = os.path.dirname(os.path.abspath(__file__)) + "/source"
OUT = os.path.dirname(os.path.abspath(__file__)) + "/extracted"
os.makedirs(OUT, exist_ok=True)

# Byzantine Doors palette for reference
BYZ_PALETTE = {
    "blue": "#1B2A4A",
    "gold": "#C6A032",
    "cream": "#FAF8F0",
    "red": "#8B2500",
    "teal": "#1A6B5C",
}

def crop_and_save(src_file, name, box, description=""):
    """Crop a region and save it. box = (left, upper, right, lower)"""
    img = Image.open(os.path.join(SRC, src_file))
    cropped = img.crop(box)
    out_path = os.path.join(OUT, f"{name}.png")
    cropped.save(out_path, "PNG")
    w, h = cropped.size
    print(f"  ✓ {name}.png ({w}x{h}) — {description}")
    return out_path

print("=" * 60)
print("Extracting Byzantine pattern bands")
print("=" * 60)

# ── Jones Byzantine Plate 30 (3244x5000) ──
print("\n▸ Jones Byzantine No. 3 (Plate 30)")

# Band 1: Top geometric strip (5 small panels)
crop_and_save("jones-byzantine-3.jpg", "jones30-geometric-strip",
    (180, 280, 3060, 560),
    "Top row geometric panels — stars, interlace, rosettes")

# Band 5: Red spiral guilloche (Panel 33)
crop_and_save("jones-byzantine-3.jpg", "jones30-guilloche-red",
    (620, 3380, 1520, 3800),
    "Red running spiral guilloche on cream — strongest divider")

# Band 6: Green vine scroll with rosettes (Panel 34/35)
crop_and_save("jones-byzantine-3.jpg", "jones30-vine-rosette",
    (1500, 3380, 2440, 3800),
    "Green vine-scroll medallions with rosettes")

# Band 3: Chain/ring guilloche (Panel 23)
crop_and_save("jones-byzantine-3.jpg", "jones30-chain-guilloche",
    (1540, 1830, 2440, 2070),
    "Interlocking circle chain band")

# Band 4: Palmette frieze (Panel 24)
crop_and_save("jones-byzantine-3.jpg", "jones30-palmette",
    (2080, 1700, 2900, 2080),
    "Repeating palmette/anthemion frieze")

# Band 7: Bottom row narrow friezes (Panels 39-42)
crop_and_save("jones-byzantine-3.jpg", "jones30-bottom-friezes",
    (180, 4600, 3080, 4940),
    "Four narrow bands — scroll, leaf, anthemion, interlace")

# Panel 41: Dark anthemion (isolated)
crop_and_save("jones-byzantine-3.jpg", "jones30-dark-anthemion",
    (1620, 4620, 2300, 4900),
    "Dark ground palmette buds — subtle elegant divider")

# Panel 42: Interlace knotwork
crop_and_save("jones-byzantine-3.jpg", "jones30-interlace-knot",
    (2300, 4600, 3080, 4920),
    "Red-white strapwork interlace with green rosettes")

# Wave scroll (Panel 22)
crop_and_save("jones-byzantine-3.jpg", "jones30-wave-scroll",
    (640, 1700, 1540, 2080),
    "Wave-scroll with leaf tips and chain-link band")

# ── Jones Byzantine Plate 29 (3332x5000) ──
print("\n▸ Jones Byzantine No. 2 (Plate 29)")

# Blue vine scroll on brown (Figure 15)
crop_and_save("jones-byzantine-2.jpg", "jones29-vine-blue",
    (1150, 4050, 2200, 4800),
    "Blue vine scroll on brown — striking lapis motif")

# Horizontal vine scroll band (Figure 14)
crop_and_save("jones-byzantine-2.jpg", "jones29-vine-band",
    (180, 4050, 1130, 4800),
    "Blue vine scroll band on brown — primary header ribbon")

# Greek cross repeat (Figures 10-11)
crop_and_save("jones-byzantine-2.jpg", "jones29-cross-band",
    (1100, 3050, 2200, 3900),
    "Greek cross repeating band in red/blue/white")

# Pearled/quatrefoil border (Figure 4)
crop_and_save("jones-byzantine-2.jpg", "jones29-pearled-border",
    (180, 2050, 680, 2900),
    "Pearled border with quatrefoils")

# Tiered horizontal bands with rosettes (Figure 16)
crop_and_save("jones-byzantine-2.jpg", "jones29-tiered-bands",
    (2250, 4050, 3200, 4800),
    "Tiered bands with rosettes and jeweled cabochons")

# Rosettes in circles (Figure 12)
crop_and_save("jones-byzantine-2.jpg", "jones29-rosette-circles",
    (2350, 3050, 3200, 3900),
    "Blue rosettes in circles — tileable band")

# ── Jones Byzantine Plate 29* (3326x5000) ──
print("\n▸ Jones Byzantine No. 2* (Plate 29*)")

# Gold-ground manuscript scrolls with roundels
crop_and_save("jones-byzantine-2b.jpg", "jones29b-gold-scroll",
    (200, 2000, 1600, 2800),
    "Gold-ground inhabited scroll with roundels — manuscript feel")

# Arched palmette frieze
crop_and_save("jones-byzantine-2b.jpg", "jones29b-palmette-arch",
    (200, 3600, 1600, 4200),
    "Arched palmette frieze — sanctuary screen style")

# ── Dolmetsch Table 32 (3511x5178) ──
print("\n▸ Dolmetsch Table 32")

# Lily/trefoil band (element 4 area — middle section)
crop_and_save("dolmetsch-table32.jpg", "dolmetsch-lily-band",
    (200, 2400, 3300, 2700),
    "Lily/trefoil band on dark ground — primary hr replacement")

# Cross-in-circle repeat (element 7 area)
crop_and_save("dolmetsch-table32.jpg", "dolmetsch-cross-circles",
    (200, 3200, 1700, 3600),
    "Cross-in-circle opus alexandrinum — liturgical borders")

# Vine scroll inhabited (element 2 area)
crop_and_save("dolmetsch-table32.jpg", "dolmetsch-vine-inhabited",
    (200, 1400, 1200, 2300),
    "Inhabited vine scroll in mandorla compartments")

# Interlaced roundel field (element 1 — bottom)
crop_and_save("dolmetsch-table32.jpg", "dolmetsch-roundel-field",
    (1200, 3800, 2800, 4600),
    "Interlaced roundel field — hero background texture")

print("\n" + "=" * 60)
print(f"Done! {len(os.listdir(OUT))} patterns extracted to {OUT}")
print("=" * 60)
