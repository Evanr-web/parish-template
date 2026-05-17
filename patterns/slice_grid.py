#!/usr/bin/env python3
"""Slice source plates into horizontal strips for visual inspection."""
from PIL import Image
import os

SRC = os.path.dirname(os.path.abspath(__file__)) + "/source"
OUT = os.path.dirname(os.path.abspath(__file__)) + "/grid"
os.makedirs(OUT, exist_ok=True)

def slice_plate(filename, num_slices=10):
    """Slice a plate into horizontal strips."""
    img = Image.open(os.path.join(SRC, filename))
    w, h = img.size
    strip_h = h // num_slices
    base = filename.replace('.jpg', '')
    
    for i in range(num_slices):
        top = i * strip_h
        bottom = min((i + 1) * strip_h, h)
        strip = img.crop((0, top, w, bottom))
        # Scale down for inspection
        scale = 800 / w
        strip = strip.resize((800, int((bottom - top) * scale)), Image.LANCZOS)
        out_path = os.path.join(OUT, f"{base}_strip{i:02d}_y{top}-{bottom}.png")
        strip.save(out_path, "PNG")
    print(f"  ✓ {filename}: {num_slices} strips ({w}x{strip_h} each)")

print("Slicing plates into horizontal strips...")
for f in ["jones-byzantine-3.jpg", "jones-byzantine-2.jpg", "dolmetsch-table32.jpg"]:
    slice_plate(f, 10)
print("Done!")
