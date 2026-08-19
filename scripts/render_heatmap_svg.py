import json
import os

# Paleta verde estilo GitHub
PALETTE = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353"]

def render_heatmap():
    json_path = "data/contributions.json"
    if not os.path.exists(json_path):
        print(f"Error: {json_path} no existe. Corre fetch_contributions.py primero.")
        return

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    days = data.get("days", [])
    total = data.get("total_contributions", 0)

    # Parametros de dibujo del calendario (53 semanas x 7 días)
    box_size = 11
    box_gap = 4
    start_x = 35
    start_y = 45
    width = 860
    height = 160

    svg_lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">',
        '  <style>',
        '    .title { font-family: "Courier New", Courier, monospace; font-size: 13px; font-weight: bold; fill: #58a6ff; }',
        '    .sub { font-family: "Courier New", Courier, monospace; font-size: 11px; fill: #8b949e; }',
        '    @keyframes popIn { 0% { opacity: 0; transform: scale(0.3); } 100% { opacity: 1; transform: scale(1); } }',
        '    .cell { animation: popIn 0.25s ease-out forwards; transform-origin: center; }',
        '  </style>',
        f'  <rect width="100%" height="100%" fill="#0d1117" rx="8" stroke="#30363d" stroke-width="1"/>',
        f'  <text x="20" y="25" class="title">tobias@fedora ~ $ ./contributions.sh</text>',
        f'  <text x="{width - 220}" y="25" class="sub">{total:,} contributions this year</text>'
    ]

    for idx, day in enumerate(days):
        col = idx // 7
        row = idx % 7
        x = start_x + (col * (box_size + box_gap))
        y = start_y + (row * (box_size + box_gap))
        
        level = min(day.get("level", 0), 4)
        color = PALETTE[level]
        
        # Animación diagonal escalonada
        delay = round((col * 0.015) + (row * 0.02), 3)
        svg_lines.append(
            f'  <rect x="{x}" y="{y}" width="{box_size}" height="{box_size}" rx="2" fill="{color}" opacity="0" class="cell" style="animation-delay: {delay}s;" />'
        )

    # Leyenda Less / More
    legend_y = height - 15
    svg_lines.append(f'  <text x="{width - 150}" y="{legend_y}" class="sub" font-size="10">Less</text>')
    for i, color in enumerate(PALETTE):
        lx = width - 120 + (i * 14)
        svg_lines.append(f'  <rect x="{lx}" y="{legend_y - 8}" width="10" height="10" rx="2" fill="{color}" />')
    svg_lines.append(f'  <text x="{width - 45}" y="{legend_y}" class="sub" font-size="10">More</text>')

    svg_lines.append('</svg>')

    with open("contrib-heatmap.svg", "w", encoding="utf-8") as f:
        f.write("\n".join(svg_lines))

    print("Listo! Heatmap generado con exito: contrib-heatmap.svg")

if __name__ == "__main__":
    render_heatmap()