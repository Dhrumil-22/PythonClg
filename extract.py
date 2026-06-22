import json
import os

files = [
    r"c:\Users\91940\Downloads\@ COLLAGE\LJIET\SEM4\PYTHON\T3 PYTHON\LEC(3).ipynb",
    r"c:\Users\91940\Downloads\@ COLLAGE\LJIET\SEM4\PYTHON\T3 PYTHON\LEC1.ipynb",
    r"c:\Users\91940\Downloads\@ COLLAGE\LJIET\SEM4\PYTHON\T3 PYTHON\LEC2.IPYNB",
    r"c:\Users\91940\Downloads\@ COLLAGE\LJIET\SEM4\PYTHON\T3 PYTHON\LEC3(1).ipynb",
    r"c:\Users\91940\Downloads\@ COLLAGE\LJIET\SEM4\PYTHON\T3 PYTHON\LEC3(2).ipynb",
    r"c:\Users\91940\Downloads\@ COLLAGE\LJIET\SEM4\PYTHON\T3 PYTHON\LEC4.ipynb",
    r"c:\Users\91940\Downloads\@ COLLAGE\LJIET\SEM4\PYTHON\T3 PYTHON\LEC5.ipynb"
]

out_lines = []

for f in files:
    out_lines.append(f"--- File: {os.path.basename(f)} ---")
    try:
        with open(f, 'r', encoding='utf-8') as fh:
            data = json.load(fh)
            for cell in data.get('cells', []):
                ctype = cell.get('cell_type')
                source = "".join(cell.get('source', []))
                if ctype in ['code', 'markdown']:
                    out_lines.append(f"[{ctype.upper()}]:\n{source}\n")
    except Exception as e:
        out_lines.append(f"Error reading file: {e}")

with open('extracted_notes.txt', 'w', encoding='utf-8') as out_f:
    out_f.write("\n".join(out_lines))
