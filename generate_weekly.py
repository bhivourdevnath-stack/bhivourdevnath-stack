import urllib.request
from pathlib import Path

GIST_URL = "https://gist.githubusercontent.com/bhivourdevnath-stack/91c3056618c155283c7c86c1a41cf36c/raw/a997a3018d11fd59fe25e9462fbd450c8b4f4c4b/%25F0%259F%2593%258A%2520Weekly%2520development%2520breakdown"

data = urllib.request.urlopen(GIST_URL).read().decode("utf-8")

lines = data.splitlines()

rows = []

for line in lines:
    if line.strip():
        rows.append(line.strip())

svg_lines = []

for i, line in enumerate(rows):
    y = 70 + i * 28

    # Escape XML characters
    line = (
        line.replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
    )

    svg_lines.append(
        f'<text x="30" y="{y}" '
        f'font-family="monospace" font-size="16" '
        f'fill="white">{line}</text>'
    )

height = max(120, 90 + len(rows) * 28)

svg = f'''<svg xmlns="http://www.w3.org/2000/svg"
width="900"
height="{height}"
viewBox="0 0 900 {height}">

<rect width="100%" height="100%" rx="15" fill="#0d1117"/>

<text x="30" y="40"
font-family="monospace"
font-size="20"
font-weight="bold"
fill="white">
📊 Weekly Development Breakdown
</text>

{"".join(svg_lines)}

</svg>
'''

Path("assets/weekly.svg").write_text(svg, encoding="utf-8")

print("weekly.svg generated successfully!")
