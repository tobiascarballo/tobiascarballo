import cv2
import numpy as np
import os

RAMP = " .`:-=+*cs#%@"  # Blanco/Espacio -> Oscuro/Denso

def generate_ascii_svg(image_path="data/source-prepped.png", output_svg="profile-ascii.svg", width_chars=80):
    if not os.path.exists(image_path):
        print(f"Error: {image_path} no existe. Ejecuta prep_photo.py primero.")
        return

    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    h, w = img.shape
    aspect_ratio = h / w
    height_chars = int(width_chars * aspect_ratio * 0.55)

    resized = cv2.resize(img, (width_chars, height_chars), interpolation=cv2.INTER_AREA)

    num_chars = len(RAMP)
    ascii_rows = []
    for row in resized:
        line = "".join([RAMP[int((pixel / 255.0) * (num_chars - 1))] for pixel in row])
        ascii_rows.append(line)

    char_w, char_h = 7.2, 12
    svg_w = int(width_chars * char_w) + 20
    svg_h = int(height_chars * char_h) + 20

    svg_lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_w} {svg_h}" width="{svg_w}" height="{svg_h}">',
        '  <style>',
        '    .ascii-text { font-family: "Courier New", Courier, monospace; font-size: 10px; fill: #58a6ff; white-space: pre; }',
        '    @keyframes typeRow { from { opacity: 0; transform: translateY(-2px); } to { opacity: 1; transform: translateY(0); } }',
        '    .row { opacity: 0; animation: typeRow 0.15s ease-out forwards; }',
        '  </style>',
        f'  <rect width="100%" height="100%" fill="#0d1117" rx="8" />'
    ]

    for idx, row_text in enumerate(ascii_rows):
        delay = round(idx * 0.035, 3)
        safe_text = row_text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        y_pos = 15 + (idx * char_h)
        svg_lines.append(f'  <text x="10" y="{y_pos}" class="ascii-text row" style="animation-delay: {delay}s;">{safe_text}</text>')

    svg_lines.append('</svg>')

    with open(output_svg, "w", encoding="utf-8") as f:
        f.write("\n".join(svg_lines))

    print(f"SVG generado con exito: {output_svg}")

if __name__ == "__main__":
    generate_ascii_svg()