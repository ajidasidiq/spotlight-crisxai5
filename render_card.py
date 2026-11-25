#!/usr/bin/env python3
"""Render the @crisxai5 spotlight card, 1200x675, drawn at 2x and downscaled
for crisp text. Original artwork, drawn with PIL in this session."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math, random

S = 2                      # supersample factor
W, H = 1200 * S, 675 * S
BOLD = "/usr/share/fonts/truetype/noto/NotoSans-ExtraBold.ttf"
BOLD2 = "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf"
MED = "/usr/share/fonts/truetype/noto/NotoSans-Medium.ttf"

def font(path, px):
    return ImageFont.truetype(path, px * S)

img = Image.new("RGB", (W, H), (7, 10, 26))
d = ImageDraw.Draw(img, "RGBA")

# --- background: vertical gradient navy -> deep indigo ---
top, bot = (8, 12, 32), (16, 20, 58)
for y in range(H):
    t = y / H
    d.line([(0, y), (W, y)],
           fill=tuple(int(top[i] + (bot[i] - top[i]) * t) for i in range(3)))

# --- glow orbs (blurred circles) ---
glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
g = ImageDraw.Draw(glow)
g.ellipse([W * 0.62, -H * 0.45, W * 1.15, H * 0.55], fill=(34, 211, 238, 70))
g.ellipse([W * 0.72, H * 0.45, W * 1.25, H * 1.25], fill=(139, 92, 246, 60))
g.ellipse([-W * 0.15, H * 0.75, W * 0.25, H * 1.3], fill=(34, 211, 238, 36))
glow = glow.filter(ImageFilter.GaussianBlur(90 * S))
img.paste(Image.alpha_composite(img.convert("RGBA"), glow).convert("RGB"), (0, 0))
d = ImageDraw.Draw(img, "RGBA")

# --- faint dot grid on the right half ---
for gx in range(int(W * 0.60), W, 34 * S):
    for gy in range(20 * S, H, 34 * S):
        d.ellipse([gx, gy, gx + 3 * S, gy + 3 * S], fill=(148, 163, 184, 28))

# --- rising sparkline (crypto chart motif), bottom right ---
random.seed(7)
pts = []
x = W * 0.58
y = H * 0.82
for i in range(14):
    pts.append((x, y))
    x += (W * 0.40) / 13
    y -= random.randint(6, 26) * S
    y = max(y, H * 0.42)
# fill under the line
poly = pts + [(pts[-1][0], H), (pts[0][0], H)]
d.polygon(poly, fill=(34, 211, 238, 22))
d.line(pts, fill=(34, 211, 238, 220), width=5 * S, joint="curve")
d.ellipse([pts[-1][0] - 8 * S, pts[-1][1] - 8 * S,
           pts[-1][0] + 8 * S, pts[-1][1] + 8 * S], fill=(34, 211, 238, 255))
d.ellipse([pts[-1][0] - 4 * S, pts[-1][1] - 4 * S,
           pts[-1][0] + 4 * S, pts[-1][1] + 4 * S], fill=(255, 255, 255, 255))

# --- glowing ring emblem, top right ---
cx, cy, r = int(W * 0.86), int(H * 0.26), 78 * S
ring = Image.new("RGBA", (W, H), (0, 0, 0, 0))
rd = ImageDraw.Draw(ring)
rd.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(34, 211, 238, 255), width=6 * S)
rd.ellipse([cx - r + 14 * S, cy - r + 14 * S, cx + r - 14 * S, cy + r - 14 * S],
           outline=(139, 92, 246, 160), width=3 * S)
ring = ring.filter(ImageFilter.GaussianBlur(2 * S))
img.paste(Image.alpha_composite(img.convert("RGBA"), ring).convert("RGB"), (0, 0))
d = ImageDraw.Draw(img, "RGBA")
d.ellipse([cx - r + 22 * S, cy - r + 22 * S, cx + r - 22 * S, cy + r - 22 * S],
          fill=(13, 20, 48, 255), outline=(34, 211, 238, 90), width=2 * S)
f_ai = font(BOLD, 58)
d.text((cx, cy), "AI", font=f_ai, fill=(255, 255, 255, 255), anchor="mm")
f_x = font(BOLD2, 20)
d.text((cx, cy + 52 * S), "× CRYPTO", font=f_x, fill=(34, 211, 238, 255), anchor="mm")

# --- left column text ---
LX = 64 * S
CYAN = (34, 211, 238, 255)
VIOLET = (167, 139, 250, 255)
WHITE = (255, 255, 255, 255)
MUTE = (203, 213, 225, 255)

# badge pill (drawn star: the font has no ★ glyph)
import math as _m
badge = "MUST-FOLLOW"
f_badge = font(BOLD2, 21)
bw = d.textlength(badge, font=f_badge) + 36 * S + 26 * S
by0, by1 = 52 * S, 52 * S + 44 * S
d.rounded_rectangle([LX, by0, LX + bw, by1], radius=22 * S,
                    outline=CYAN, width=2 * S)
_scx, _scy, _sr = LX + 24 * S, (by0 + by1) // 2, 10 * S
_star = []
for _i in range(10):
    _ang = -_m.pi / 2 + _i * _m.pi / 5
    _rr = _sr if _i % 2 == 0 else _sr * 0.45
    _star.append((_scx + _rr * _m.cos(_ang), _scy + _rr * _m.sin(_ang)))
d.polygon(_star, fill=CYAN)
d.text((LX + 44 * S, (by0 + by1) // 2), badge, font=f_badge, fill=CYAN, anchor="lm")

# kicker
f_kick = font(BOLD2, 26)
d.text((LX, 128 * S), "AI & CRYPTO EXPERT ON X", font=f_kick, fill=VIOLET)

# headline
f_head = font(BOLD, 92)
d.text((LX, 158 * S), "@crisxai5", font=f_head, fill=WHITE)
# cyan underline
hw = d.textlength("@crisxai5", font=f_head)
d.rounded_rectangle([LX, 268 * S, LX + hw, 276 * S], radius=4 * S, fill=CYAN)

# subline
f_sub = font(REG, 27)
d.text((LX, 296 * S), "Sharp takes on the tech eating the future —",
       font=f_sub, fill=MUTE)
d.text((LX, 330 * S), "no noise, no shilling, just signal.",
       font=f_sub, fill=MUTE)

# four value rows
rows = [
    ("AI agents", "decoded, not hyped"),
    ("Crypto alpha", "without the noise"),
    ("Web3 tooling", "that actually ships"),
    ("On-chain automation", "explained simply"),
]
f_row_b = font(BOLD2, 26)
f_row_r = font(REG, 26)
ry = 392 * S
for title, rest in rows:
    d.ellipse([LX, ry + 8 * S, LX + 14 * S, ry + 22 * S], fill=CYAN)
    d.text((LX + 28 * S, ry), title, font=f_row_b, fill=WHITE)
    tw = d.textlength(title + " ", font=f_row_b)
    d.text((LX + 28 * S + tw, ry), rest, font=f_row_r, fill=MUTE)
    ry += 46 * S

# footer
d.line([(LX, 606 * S), (LX + 560 * S, 606 * S)], fill=(148, 163, 184, 90), width=2 * S)
f_foot = font(BOLD2, 24)
d.text((LX, 620 * S), "x.com/crisxai5", font=f_foot, fill=CYAN)
f_foot2 = font(MED, 24)
d.text((LX + d.textlength("x.com/crisxai5  ", font=f_foot), 620 * S),
       "— follow the signal.", font=f_foot2, fill=MUTE)

img = img.resize((1200, 675), Image.LANCZOS)
img.save("/home/hatch/workspace/makefun/spotlight-crisxai5/crisxai5-spotlight.png",
         optimize=True)
print("saved 1200x675")
