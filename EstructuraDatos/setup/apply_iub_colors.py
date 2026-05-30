#!/usr/bin/env python3
"""
apply_iub_colors.py
Aplica la paleta oficial IUB (DG-TSI-09-V4) a todos los archivos HTML del proyecto TGA05.

Paleta IUB:
  Primario oscuro:  #1E2843  (azul marino institucional)
  Primario amarillo:#FFDF2D  (amarillo institucional)
  Gris claro:       #E9EAED
  Gris borde:       #DEDFE4
  Fondo blanco:     #FAFAFA

Tipografía IUB: Open Sans (con fallback Arial, sans-serif)
"""

import os, re

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ── Archivos objetivo ──────────────────────────────────────────────────────────
TARGET_FILES = []
for i in range(1, 15):
    for f in ["index.html", "notas_profesor.html"]:
        p = os.path.join(BASE, f"semana{i}", f)
        if os.path.exists(p):
            TARGET_FILES.append(p)

for f in [
    os.path.join(BASE, "dashboard", "index.html"),
    os.path.join(BASE, "dashboard", "profesor.html"),
    os.path.join(BASE, "index.html"),
]:
    if os.path.exists(f):
        TARGET_FILES.append(f)

print(f"Archivos objetivo: {len(TARGET_FILES)}")

# ── Mapa de sustituciones de colores ──────────────────────────────────────────
# Orden importa: más específico primero
COLOR_MAP = [
    # Gradientes completos con dos colores (reemplazar por IUB)
    (r"linear-gradient\(135deg,\s*#1a237e,\s*#283593,\s*#3949ab\)",
     "linear-gradient(135deg, #1E2843, #2d3a5e)"),
    (r"linear-gradient\(135deg,\s*#1a237e,\s*#3949ab\)",
     "linear-gradient(135deg, #1E2843, #2d3a5e)"),
    (r"linear-gradient\(135deg,\s*var\(--primary\)\s*0%,\s*var\(--accent\)\s*100%\)",
     "linear-gradient(135deg, var(--primary) 0%, var(--accent) 100%)"),

    # Variables CSS :root  — reemplazar valores
    (r"--primary:\s*#1a237e", "--primary:   #1E2843"),
    (r"--accent:\s*#3949ab",  "--accent:    #2d3a5e"),
    (r"--gold:\s*#f9a825",    "--gold:      #FFDF2D"),
    (r"--gold:\s*#f0c040",    "--gold:      #FFDF2D"),
    (r"--light-bg:\s*#f5f7ff","--light-bg:  #FAFAFA"),
    (r"--light:\s*#f5f7ff",   "--light:     #FAFAFA"),
    (r"--border:\s*#c5cae9",  "--border:    #DEDFE4"),

    # Colores hardcodeados estructurales (NO gamificación)
    (r"#1a237e",  "#1E2843"),
    (r"#3949ab",  "#2d3a5e"),
    (r"#283593",  "#1E2843"),
    (r"#1e1e2e",  "#1E2843"),   # widget dark background → IUB navy (casi idéntico)
    (r"#313244",  "#2d3a5e"),   # widget card bg
    (r"#f9a825",  "#FFDF2D"),   # gold/XP bar → IUB amarillo
    (r"#f0c040",  "#FFDF2D"),
    (r"#ffd54f",  "#FFDF2D"),
    (r"#ffa000",  "#e6c800"),   # amber oscuro para hover sobre amarillo
    (r"#f5f7ff",  "#FAFAFA"),
    (r"#c5cae9",  "#DEDFE4"),
    (r"#e8eaf6",  "#E9EAED"),

    # Tipografía
    (r"font-family:\s*'Segoe UI',\s*system-ui,\s*sans-serif",
     "font-family: 'Open Sans', Arial, sans-serif"),
    (r"font-family:\s*'Segoe UI',system-ui,sans-serif",
     "font-family: 'Open Sans', Arial, sans-serif"),
    (r"font-family:\s*'Segoe UI',\s*Arial,\s*sans-serif",
     "font-family: 'Open Sans', Arial, sans-serif"),
]

# ── Google Fonts import para Open Sans ────────────────────────────────────────
GFONTS_MARKER  = "fonts.googleapis.com/css2?family=Open+Sans"
GFONTS_IMPORT  = '<link rel="preconnect" href="https://fonts.googleapis.com">\n' \
                 '  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n' \
                 '  <link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600;700;800&display=swap" rel="stylesheet">'
GFONTS_ANCHOR  = "<meta charset"  # insertar justo antes del <meta charset

# ── Procesamiento ─────────────────────────────────────────────────────────────
modified = 0
for path in TARGET_FILES:
    with open(path, "r", encoding="utf-8") as f:
        original = f.read()

    content = original

    # 1. Agregar Google Fonts import si no está
    if GFONTS_MARKER not in content and GFONTS_ANCHOR in content:
        content = content.replace(
            GFONTS_ANCHOR,
            f"{GFONTS_IMPORT}\n  {GFONTS_ANCHOR}",
            1
        )

    # 2. Aplicar sustituciones de colores/tipografía
    for pattern, replacement in COLOR_MAP:
        content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)

    if content != original:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        rel = os.path.relpath(path, BASE)
        print(f"  ✅  {rel}")
        modified += 1
    else:
        rel = os.path.relpath(path, BASE)
        print(f"  ──  {rel}  (sin cambios)")

print(f"\nTotal modificados: {modified}/{len(TARGET_FILES)}")
