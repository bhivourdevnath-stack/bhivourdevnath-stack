import urllib.request
from pathlib import Path
from html import escape

GIST_URL = "https://gist.githubusercontent.com/bhivourdevnath-stack/91c3056618c155283c7c86c1a41cf36c/raw/"

try:
    data = urllib.request.urlopen(GIST_URL).read().decode("utf-8")
except Exception as e:
    print("Failed to fetch Gist:", e)
    raise

print("Gist content:")
print(data)

lines = [line.strip() for line in data.splitlines() if line.strip()]

rows = []

for line in lines:
    rows.append(
        f"""
        <text x="30"
              y="{80 + len(rows) * 28}"
              font-family="Arial, sans-serif"
              font-size="16"
              fill="#ffffff">
            {escape(line)}
        </text>
        """
    )

height = max(140, 100 + len(lines) * 28)

svg = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg"
     width="900"
     height="{height}"
     viewBox="0 0 900 {height}">

    <rect width="900"
          height="{height}"
          rx="16"
          fill="#0d1117"/>

    <text x="30"
          y="45"
          font-family="Arial, sans-serif"
          font-size="22"
          font-weight="bold"
          fill="#ffffff">
        Weekly Development Breakdown
    </text>

    {''.join(rows)}

</svg>
"""

Path("assets").mkdir(exist_ok=True)

Path("assets/weekly.svg").write_text(
    svg,
    encoding="utf-8"
)

print("✅ assets/weekly.svg generated successfully!")
