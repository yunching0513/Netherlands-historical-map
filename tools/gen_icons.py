#!/usr/bin/env python3
"""Generate language-specific PWA icons for the Netherlands historical map app.

Renders the existing SVG base icon, then composites a language-specific text
band at the bottom of each icon variant. Outputs:
  icons/icon-192-nl.png   icons/icon-512-nl.png
  icons/icon-192-en.png   icons/icon-512-en.png
  icons/icon-192-zh.png   icons/icon-512-zh.png
  icons/icon-maskable-512.png  (language-neutral, large safe-zone padding)

Also writes a shared fallback:
  icons/icon-192.png  icons/icon-512.png  (English, for manifest fallback)
"""
import io, os
import cairosvg
from PIL import Image, ImageDraw, ImageFont

PAPER   = (241, 239, 233)   # #F1EFE9
VERMILION = (193, 95, 60)   # #C15F3C
ASH     = (128, 124, 115)   # #807C73

SERIF_FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf'
CJK_FONT   = '/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc'

LANGS = {
    'nl': {'label': 'WANDELING',   'font': SERIF_FONT, 'spacing': 5},
    'en': {'label': 'OLD-MAP',     'font': SERIF_FONT, 'spacing': 4},
    'zh': {'label': '古地圖散策',  'font': CJK_FONT,   'spacing': 2},
}

SVG_PATH = os.path.join(os.path.dirname(__file__), '..', 'icons', 'icon.svg')
OUT_DIR  = os.path.join(os.path.dirname(__file__), '..', 'icons')


def render_svg(size):
    svg = open(SVG_PATH, 'rb').read()
    png = cairosvg.svg2png(bytestring=svg, output_width=size, output_height=size)
    return Image.open(io.BytesIO(png)).convert('RGBA')


def add_label(base_img, label, font_path, spacing, size):
    """Overlay a small text label at the bottom of the icon."""
    img = base_img.copy()
    draw = ImageDraw.Draw(img)
    # Font size scales with icon size: ~8% of icon width, min 10px
    font_size = max(10, int(size * 0.082))
    font = ImageFont.truetype(font_path, font_size)
    # Measure text
    bbox = draw.textbbox((0, 0), label, font=font, spacing=spacing)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    # Position: centered horizontally, near bottom (leaving ~5% margin)
    margin = int(size * 0.05)
    x = (size - text_w) // 2 - bbox[0]
    y = size - margin - text_h - bbox[1]
    # Semi-transparent paper background behind text
    pad = int(size * 0.02)
    bg_box = (x + bbox[0] - pad, y + bbox[1] - pad,
              x + bbox[2] + pad, y + bbox[3] + pad)
    overlay = Image.new('RGBA', img.size, (0, 0, 0, 0))
    ov_draw = ImageDraw.Draw(overlay)
    ov_draw.rectangle(bg_box, fill=(*PAPER, 210))
    img = Image.alpha_composite(img, overlay)
    draw = ImageDraw.Draw(img)
    draw.text((x, y), label, fill=(*ASH, 230), font=font)
    return img


def make_maskable(base_img, size):
    """Maskable icon: shrink the graphic to 80% to respect the safe zone."""
    inner = int(size * 0.8)
    pad = (size - inner) // 2
    bg = Image.new('RGBA', (size, size), (*PAPER, 255))
    shrunk = base_img.resize((inner, inner), Image.LANCZOS)
    bg.paste(shrunk, (pad, pad), shrunk)
    return bg


def save(img, path):
    rgb = Image.new('RGB', img.size, PAPER)
    rgb.paste(img, mask=img.split()[3])
    rgb.save(path, 'PNG', optimize=True)
    print(f'  {path}  ({os.path.getsize(path)//1024} KB)')


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    print('Rendering base SVGs ...')
    base192 = render_svg(192)
    base512 = render_svg(512)

    for lang, cfg in LANGS.items():
        print(f'\n[{lang}]')
        for size, base in [(192, base192), (512, base512)]:
            img = add_label(base, cfg['label'], cfg['font'], cfg['spacing'], size)
            save(img, os.path.join(OUT_DIR, f'icon-{size}-{lang}.png'))

    # Shared fallback (EN)
    print('\n[fallback EN]')
    for size, base in [(192, base192), (512, base512)]:
        img = add_label(base, 'OLD-MAP', SERIF_FONT, 4, size)
        save(img, os.path.join(OUT_DIR, f'icon-{size}.png'))

    # Maskable (language-neutral, safe-zone padding)
    print('\n[maskable]')
    save(make_maskable(base512, 512),
         os.path.join(OUT_DIR, 'icon-maskable-512.png'))

    print('\nDone.')


if __name__ == '__main__':
    main()
