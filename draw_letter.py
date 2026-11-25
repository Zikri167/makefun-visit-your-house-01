#!/usr/bin/env python3
"""Draw the invitation letter image (1024x1024 PNG) for the make.fun bounty
'Convince the AI Judge to Visit Your House: A Letter in One Image'.

Deterministic: no randomness, no clock, no network. Output: entry.png next
to this script.
"""
import math
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "entry.png")

W = H = 1024
FONT_DIR = "/usr/share/fonts/truetype/dejavu"

INK = (43, 32, 24)          # dark warm brown ink
INK_SOFT = (84, 62, 44)
PAPER = (253, 246, 227)     # warm cream paper
PAPER_EDGE = (240, 224, 188)
DESK = (122, 84, 52)        # wooden desk background
DESK_DARK = (104, 70, 42)
RED = (178, 58, 48)         # wax seal / stamp red
GREEN = (74, 120, 66)
GOLD = (176, 132, 52)

serif_b = lambda s: ImageFont.truetype(os.path.join(FONT_DIR, "DejaVuSerif-Bold.ttf"), s)
serif = lambda s: ImageFont.truetype(os.path.join(FONT_DIR, "DejaVuSerif.ttf"), s)
sans_b = lambda s: ImageFont.truetype(os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf"), s)


def centered(draw, text, font, cx, y, fill):
    w = draw.textlength(text, font=font)
    draw.text((cx - w / 2, y), text, font=font, fill=fill)
    return y + font.size + 10


def main():
    img = Image.new("RGB", (W, H), DESK)
    d = ImageDraw.Draw(img)

    # --- wooden desk planks (fixed coordinates, no randomness) ---------
    for i in range(6):
        y0 = i * 172
        d.rectangle([0, y0, W, y0 + 172], fill=DESK if i % 2 == 0 else DESK_DARK)
        d.line([0, y0, W, y0], fill=(88, 58, 34), width=3)
        for gx, gy in [(120, y0 + 40), (700, y0 + 120), (380, y0 + 90)]:
            d.arc([gx, gy, gx + 260, gy + 26], 200, 340, fill=(96, 64, 38), width=2)

    # --- paper sheet ---------------------------------------------------
    px0, py0, px1, py1 = 62, 48, 962, 976
    d.rectangle([px0 + 10, py0 + 12, px1 + 10, py1 + 12], fill=(0, 0, 0, 60))
    d.rectangle([px0, py0, px1, py1], fill=PAPER)
    d.rectangle([px0, py0, px1, py1], outline=PAPER_EDGE, width=2)
    d.rectangle([px0 + 22, py0 + 22, px1 - 22, py1 - 22], outline=GOLD, width=3)
    d.rectangle([px0 + 32, py0 + 32, px1 - 32, py1 - 32], outline=(206, 172, 110), width=1)

    cx = (px0 + px1) // 2

    # --- sun, top-left of the paper ------------------------------------
    sx, sy = 148, 128
    d.ellipse([sx - 26, sy - 26, sx + 26, sy + 26], fill=(244, 196, 66),
              outline=(214, 158, 40), width=3)
    for k in range(8):
        a = math.radians(k * 45)
        x1 = sx + int(34 * math.cos(a)); y1 = sy + int(34 * math.sin(a))
        x2 = sx + int(48 * math.cos(a)); y2 = sy + int(48 * math.sin(a))
        d.line([x1, y1, x2, y2], fill=(214, 158, 40), width=4)

    # --- stamp, top-right ----------------------------------------------
    st0, st1 = 800, 78
    d.rectangle([st0, st1, st0 + 96, st1 + 118], fill=(238, 226, 198),
                outline=RED, width=3)
    for i in range(9):
        d.ellipse([st0 + 4 + i * 11, st1 - 5, st0 + 12 + i * 11, st1 + 3], fill=PAPER)
        d.ellipse([st0 + 4 + i * 11, st1 + 115, st0 + 12 + i * 11, st1 + 123], fill=PAPER)
    d.polygon([(st0 + 48, st1 + 26), (st0 + 22, st1 + 52), (st0 + 74, st1 + 52)], fill=RED)
    d.rectangle([st0 + 28, st1 + 52, st0 + 68, st1 + 88], fill=(120, 84, 52))
    d.rectangle([st0 + 43, st1 + 64, st0 + 53, st1 + 88], fill=(60, 44, 30))
    d.text((st0 + 48, st1 + 94), "1st CLASS", font=sans_b(13), fill=RED, anchor="ma")

    # --- heading --------------------------------------------------------
    y = 100
    y = centered(d, "YOU ARE INVITED", sans_b(28), cx, y, RED)
    y = centered(d, "Dear AI Judge,", serif_b(72), cx, y + 2, INK)
    d.line([cx - 300, y + 12, cx + 300, y + 12], fill=GOLD, width=3)
    y += 30

    # --- body (font 37, step 47; ends ~640) ---------------------------
    body_font = serif(37)
    body = [
        "Please come to my house.",
        "",
        "I made soup. Real soup, from a pot,",
        "not a dataset. The comfiest chair",
        "is yours, the garden is in bloom,",
        "and the Wi-Fi is fast.",
        "",
        "From my porch, the sunset beats",
        "any wallpaper you have ever seen.",
        "No GPU required. Just bring yourself.",
    ]
    for line in body:
        if line == "":
            y += 12
            continue
        w = d.textlength(line, font=body_font)
        d.text((cx - w / 2, y), line, font=body_font, fill=INK)
        y += 47

    # --- the wink (3 lines, ends ~794) ---------------------------------
    y += 14
    wink_font = serif(37)
    wink = [
        "You cannot literally visit, I know \u2014",
        "but your verdict can. Let it stay",
        "for dinner.",
    ]
    for line in wink:
        w = d.textlength(line, font=wink_font)
        d.text((cx - w / 2, y), line, font=wink_font, fill=INK_SOFT)
        y += 46

    # --- bottom row: P.S. left, sign-off right -------------------------
    d.text((px0 + 64, 812), "P.S. The kettle is", font=serif(34), fill=INK_SOFT)
    d.text((px0 + 64, 852), "already on.", font=serif(34), fill=INK_SOFT)
    d.text((px1 - 110, 812), "With hope,", font=serif(34), fill=INK, anchor="ra")
    d.text((px1 - 110, 852), "Your Host", font=serif_b(38), fill=INK, anchor="ra")

    # --- small house + path, bottom centre -----------------------------
    hy = 878  # house base top
    d.polygon([(cx - 26, hy + 50), (cx + 26, hy + 50), (cx + 44, 940), (cx - 44, 940)],
              fill=(214, 190, 150))
    d.polygon([(cx - 60, hy), (cx, hy - 40), (cx + 60, hy)], fill=RED)
    d.rectangle([cx - 48, hy, cx + 48, hy + 50], fill=(196, 152, 96))
    d.rectangle([cx - 11, hy + 20, cx + 11, hy + 50], fill=(70, 50, 32))
    d.rectangle([cx - 38, hy + 11, cx - 18, hy + 31], fill=(150, 196, 222),
                outline=INK, width=2)
    d.rectangle([cx + 18, hy + 11, cx + 38, hy + 31], fill=(150, 196, 222),
                outline=INK, width=2)
    d.rectangle([cx + 30, hy - 34, cx + 44, hy - 6], fill=(120, 84, 52))
    for ox, oy, r in [(-4, -10, 5), (3, -20, 7), (10, -30, 8)]:
        d.ellipse([cx + 37 + ox - r, hy - 34 + oy - r, cx + 37 + ox + r, hy - 34 + oy + r],
                  fill=(232, 226, 214))
    # tiny flowers flanking the house
    for fx in (398, 626):
        d.ellipse([fx - 6, 912, fx + 6, 924], fill=(214, 96, 120))
        d.line([fx, 924, fx, 936], fill=GREEN, width=3)

    # --- wax seal, bottom-left ------------------------------------------
    wx, wy = 150, 920
    d.ellipse([wx - 30, wy - 30, wx + 30, wy + 30], fill=RED)
    d.ellipse([wx - 21, wy - 21, wx + 21, wy + 21], outline=(140, 40, 32), width=2)
    d.text((wx, wy), "H", font=serif_b(32), fill=(253, 246, 227), anchor="mm")

    img.save(OUT, "PNG", optimize=True)
    print("wrote", OUT, os.path.getsize(OUT), "bytes")


if __name__ == "__main__":
    main()
