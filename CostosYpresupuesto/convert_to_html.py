#!/usr/bin/env python3
"""
Convierte los archivos .md del módulo GOL06 a HTML con identidad visual IUB.
Reemplaza referencias a Universidad de Buenas Aguas / UBA → IUB.
"""

import os
import re
import markdown
from pathlib import Path

# ─── Directorio de trabajo ───────────────────────────────────────────────────
BASE_DIR = Path("/Users/diegodomingueztapia/Library/CloudStorage/OneDrive-Unibarranquilla/DiegoIcloud/2026/copilot/CostosYpresupuesto")
HTML_DIR = BASE_DIR / "html"
HTML_DIR.mkdir(exist_ok=True)

# ─── Colores institucionales IUB ─────────────────────────────────────────────
# Azul institucional: #003087  |  Dorado: #F5A000  |  Blanco: #FFFFFF
# Azul claro: #0056B3           |  Fondo: #F0F5FF

CSS = """
    /* ── Reset y base ── */
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    :root {
      --iub-blue:       #003087;
      --iub-blue-mid:   #0056B3;
      --iub-blue-light: #E8F0FE;
      --iub-gold:       #F5A000;
      --iub-gold-light: #FFF3CD;
      --iub-white:      #FFFFFF;
      --iub-bg:         #F4F7FC;
      --iub-text:       #1A2744;
      --iub-muted:      #5A6A8A;
      --iub-border:     #C8D7F0;
      --iub-code-bg:    #0F1E3D;
      --iub-code-text:  #E8F0FE;
      --radius:         8px;
      --shadow:         0 2px 8px rgba(0,48,135,.12);
    }

    html { font-size: 16px; scroll-behavior: smooth; }
    body {
      font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
      background: var(--iub-bg);
      color: var(--iub-text);
      line-height: 1.7;
      padding-bottom: 3rem;
    }

    /* ── Header institucional ── */
    .iub-header {
      background: linear-gradient(135deg, var(--iub-blue) 0%, var(--iub-blue-mid) 100%);
      color: var(--iub-white);
      padding: 0;
      box-shadow: 0 4px 16px rgba(0,48,135,.3);
    }
    .iub-header-top {
      display: flex;
      align-items: center;
      gap: 1.25rem;
      padding: 1rem 2rem;
      border-bottom: 3px solid var(--iub-gold);
    }
    .iub-logo {
      width: 60px; height: 60px;
      background: var(--iub-white);
      border-radius: 50%;
      display: flex; align-items: center; justify-content: center;
      flex-shrink: 0;
      font-size: 1.1rem;
      font-weight: 900;
      color: var(--iub-blue);
      letter-spacing: -1px;
      box-shadow: 0 2px 8px rgba(0,0,0,.2);
    }
    .iub-institution { font-size: .8rem; opacity: .85; }
    .iub-institution strong { font-size: 1.05rem; display: block; opacity: 1; }
    .iub-header-meta {
      background: rgba(0,0,0,.18);
      padding: .55rem 2rem;
      font-size: .82rem;
      display: flex; flex-wrap: wrap; gap: .75rem 2rem;
      opacity: .9;
    }
    .iub-header-meta span::before { content: "● "; font-size: .65rem; }

    /* ── Barra de título del documento ── */
    .doc-title-bar {
      background: var(--iub-gold);
      color: var(--iub-blue);
      padding: .75rem 2rem;
      font-weight: 700;
      font-size: 1rem;
      letter-spacing: .02em;
    }

    /* ── Contenedor principal ── */
    .content-wrap {
      max-width: 900px;
      margin: 2rem auto;
      padding: 0 1.25rem;
    }

    /* ── Tarjeta de contenido ── */
    .content-card {
      background: var(--iub-white);
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      padding: 2.5rem 2.75rem;
      margin-bottom: 2rem;
    }

    /* ── Tipografía ── */
    h1 {
      font-size: 1.8rem;
      color: var(--iub-blue);
      border-bottom: 3px solid var(--iub-gold);
      padding-bottom: .5rem;
      margin-bottom: 1.5rem;
      line-height: 1.3;
    }
    h2 {
      font-size: 1.35rem;
      color: var(--iub-blue);
      margin: 2rem 0 .75rem;
      padding-left: .75rem;
      border-left: 4px solid var(--iub-gold);
    }
    h3 {
      font-size: 1.1rem;
      color: var(--iub-blue-mid);
      margin: 1.5rem 0 .5rem;
    }
    h4 {
      font-size: 1rem;
      color: var(--iub-muted);
      margin: 1.25rem 0 .4rem;
      text-transform: uppercase;
      letter-spacing: .05em;
    }
    p { margin-bottom: 1rem; }
    strong { color: var(--iub-blue); }
    em { color: var(--iub-muted); }

    /* ── Listas ── */
    ul, ol { margin: .5rem 0 1rem 1.5rem; }
    li { margin-bottom: .3rem; }
    ul li::marker { color: var(--iub-gold); }
    ol li::marker { color: var(--iub-blue); font-weight: 700; }

    /* ── Blockquote ── */
    blockquote {
      background: var(--iub-blue-light);
      border-left: 5px solid var(--iub-blue-mid);
      border-radius: 0 var(--radius) var(--radius) 0;
      padding: 1rem 1.25rem;
      margin: 1.25rem 0;
      color: var(--iub-text);
    }
    blockquote p { margin-bottom: .5rem; }
    blockquote p:last-child { margin-bottom: 0; }

    /* ── Código inline ── */
    code {
      background: var(--iub-blue-light);
      color: var(--iub-blue);
      padding: .15em .4em;
      border-radius: 4px;
      font-size: .88em;
      font-family: 'Cascadia Code', 'Fira Code', 'Courier New', monospace;
    }

    /* ── Bloque de código ── */
    pre {
      background: var(--iub-code-bg);
      color: var(--iub-code-text);
      border-radius: var(--radius);
      padding: 1.25rem 1.5rem;
      overflow-x: auto;
      margin: 1.25rem 0;
      font-size: .85rem;
      line-height: 1.6;
      border-left: 4px solid var(--iub-gold);
      box-shadow: inset 0 2px 8px rgba(0,0,0,.3);
    }
    pre code {
      background: transparent;
      color: var(--iub-code-text);
      padding: 0;
      font-size: inherit;
    }

    /* ── Tablas ── */
    .table-wrap { overflow-x: auto; margin: 1.25rem 0; }
    table {
      width: 100%;
      border-collapse: collapse;
      font-size: .9rem;
      min-width: 400px;
    }
    th {
      background: var(--iub-blue);
      color: var(--iub-white);
      padding: .65rem 1rem;
      text-align: left;
      font-weight: 600;
    }
    th:first-child { border-radius: var(--radius) 0 0 0; }
    th:last-child  { border-radius: 0 var(--radius) 0 0; }
    td {
      padding: .55rem 1rem;
      border-bottom: 1px solid var(--iub-border);
      vertical-align: top;
    }
    tr:nth-child(even) td { background: var(--iub-blue-light); }
    tr:hover td { background: var(--iub-gold-light); }

    /* ── Separador ── */
    hr {
      border: none;
      border-top: 2px solid var(--iub-border);
      margin: 2rem 0;
    }

    /* ── Alerta / aviso ── */
    .alert {
      background: var(--iub-gold-light);
      border-left: 5px solid var(--iub-gold);
      border-radius: 0 var(--radius) var(--radius) 0;
      padding: .85rem 1.1rem;
      margin: 1rem 0;
      font-size: .92rem;
    }

    /* ── Footer ── */
    .iub-footer {
      background: var(--iub-blue);
      color: rgba(255,255,255,.75);
      text-align: center;
      padding: 1rem 2rem;
      font-size: .8rem;
      margin-top: 3rem;
    }
    .iub-footer strong { color: var(--iub-gold); }

    /* ── Impresión ── */
    @media print {
      body { background: white; font-size: 11pt; }
      .content-card { box-shadow: none; padding: 1rem; }
      pre { background: #f0f0f0 !important; color: #000 !important;
            border-left-color: #999; }
      .iub-header { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
      .iub-footer { display: none; }
    }

    /* ── Responsive ── */
    @media (max-width: 640px) {
      .iub-header-top { padding: .75rem 1rem; }
      .content-card { padding: 1.25rem 1rem; }
      .iub-header-meta { padding: .4rem 1rem; }
      .doc-title-bar { padding: .6rem 1rem; }
    }
"""

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | IUB — GOL06</title>
  <style>{css}</style>
</head>
<body>

  <!-- ── Encabezado institucional ── -->
  <header class="iub-header">
    <div class="iub-header-top">
      <div class="iub-logo">IUB</div>
      <div>
        <div class="iub-institution">
          <strong>Institución Universitaria de Barranquilla</strong>
          Facultad · Tecnología en Gestión de Operaciones Logísticas
        </div>
      </div>
    </div>
    <div class="iub-header-meta">
      <span><strong>Módulo:</strong> GOL06 — Costos y Presupuestos</span>
      <span><strong>Créditos:</strong> 2 | HAD 2 + HP 2 + HTI 5</span>
      <span><strong>Período:</strong> 2024 – 2025</span>
      <span><strong>Caso hilo:</strong> LOGÍSATL S.A.S.</span>
    </div>
    <div class="doc-title-bar">{doc_label}</div>
  </header>

  <!-- ── Contenido ── -->
  <main class="content-wrap">
    <article class="content-card">
      {body}
    </article>
  </main>

  <footer class="iub-footer">
    <strong>Institución Universitaria de Barranquilla — IUB</strong> ·
    GOL06 Costos y Presupuestos · Material de apoyo académico · 2024–2025
  </footer>

</body>
</html>
"""

# ─── Metadatos para cada archivo ─────────────────────────────────────────────
FILE_META = {
    "00_PLANEADOR_MAESTRO.md":          ("Planeador Maestro del Módulo",   "📊 Planeador Maestro — GOL06 Costos y Presupuestos"),
    "Sem01_Estudio.md":                 ("Semana 1 — Material de Estudio", "📖 Semana 1 · Material de Estudio · RA1"),
    "Sem02_03_04_Estudio.md":           ("Semanas 2–4 — Material de Estudio", "📖 Semanas 2–4 · Material de Estudio · RA1"),
    "Sem01_02_03_04_Talleres.md":       ("Semanas 1–4 — Talleres",         "🛠️ Talleres · Semanas 1 – 4 · RA1"),
    "Sem06_07_08_09_Estudio.md":        ("Semanas 6–9 — Material de Estudio", "📖 Semanas 6–9 · Material de Estudio · RA2"),
    "Sem06_07_08_09_11_12_13_Talleres.md": ("Talleres Semanas 6–13",      "🛠️ Talleres · Semanas 6–9 y 11–13 · RA2 y RA3"),
    "Sem11_12_13_Estudio.md":           ("Semanas 11–13 — Material de Estudio", "📖 Semanas 11–13 · Material de Estudio · RA3"),
    "Parciales_Guia.md":                ("Guía de Parciales y Proyecto Final", "📝 Guía de Evaluaciones · Parcial 1, Parcial 2 y Proyecto Final"),
}

# ─── Sustituciones institucionales ───────────────────────────────────────────
def apply_iub_replacements(text: str) -> str:
    # Nombre completo + sigla
    text = re.sub(
        r"Universidad de Buenas Aguas\s*\(UBA\)",
        "Institución Universitaria de Barranquilla (IUB)",
        text, flags=re.IGNORECASE
    )
    # Solo el nombre largo sin sigla
    text = re.sub(
        r"Universidad de Buenas Aguas",
        "Institución Universitaria de Barranquilla",
        text, flags=re.IGNORECASE
    )
    # "UBA |" → "IUB |"  (encabezados de material)
    text = re.sub(r"\bUBA\s*\|", "IUB |", text)
    # "| UBA" → "| IUB"
    text = re.sub(r"\|\s*UBA\b", "| IUB", text)
    # "— UBA |" → "— IUB |"  (pie de página de materiales)
    text = re.sub(r"—\s*UBA\b", "— IUB", text)
    # "UBA-Tokens" → "IUB-Tokens"
    text = re.sub(r"\bUBA-Tokens?\b", "IUB-Tokens", text, flags=re.IGNORECASE)
    # "FinCoins UBA" → "FinCoins IUB"
    text = re.sub(r"FinCoins\s+UBA\b", "FinCoins IUB", text, flags=re.IGNORECASE)
    # "OPERACIONES UBA" → "OPERACIONES IUB"
    text = re.sub(r"OPERACIONES\s+UBA\b", "OPERACIONES IUB", text)
    # "Consultores de Operaciones UBA" → "Consultores de Operaciones IUB"
    text = re.sub(r"Consultores de Operaciones UBA\b", "Consultores de Operaciones IUB", text)
    # "Planeador Maestro — UBA" → "Planeador Maestro — IUB"
    text = re.sub(r"Planeador Maestro\s*—\s*UBA\b", "Planeador Maestro — IUB", text)
    # "Guía de Parciales — UBA" → "Guía de Parciales — IUB"
    text = re.sub(r"Guía de Parciales\s*—\s*UBA\b", "Guía de Parciales — IUB", text)
    # Standalone "UBA" que sea referencia institucional (no dentro de palabras)
    # Solo los que quedan sueltos como sigla institucional en footer/cabecera
    text = re.sub(r"(?<![A-Z])\bUBA\b(?!\s*[-–]?\s*(Tokens|[a-z]))", "IUB", text)
    return text

# ─── Post-procesamiento del HTML: wrappear tablas ────────────────────────────
def wrap_tables(html: str) -> str:
    """Envuelve cada <table> en un div.table-wrap para scroll horizontal."""
    html = re.sub(r"<table>", '<div class="table-wrap"><table>', html)
    html = re.sub(r"</table>", "</table></div>", html)
    return html

# ─── Extraer título del H1 ───────────────────────────────────────────────────
def extract_title(md_text: str) -> str:
    m = re.search(r"^#\s+(.+)$", md_text, re.MULTILINE)
    if m:
        # Limpiar emojis para el <title> del HTML
        return re.sub(r"[^\w\s\-–—áéíóúÁÉÍÓÚñÑüÜ,.:()]+", "", m.group(1)).strip()
    return "Documento"

# ─── Extensiones markdown ─────────────────────────────────────────────────────
MD_EXTENSIONS = [
    "tables",
    "fenced_code",
    "codehilite",
    "nl2br",
    "attr_list",
    "sane_lists",
]
MD_EXT_CONFIGS = {
    "codehilite": {"noclasses": True, "guess_lang": False}
}

# ─── Procesamiento principal ─────────────────────────────────────────────────
md_files = sorted(BASE_DIR.glob("*.md"))
generated = []

for md_path in md_files:
    raw = md_path.read_text(encoding="utf-8")

    # 1. Sustituciones institucionales
    raw = apply_iub_replacements(raw)

    # 2. Convertir markdown → HTML
    body_html = markdown.markdown(
        raw,
        extensions=MD_EXTENSIONS,
        extension_configs=MD_EXT_CONFIGS,
    )

    # 3. Wrappear tablas
    body_html = wrap_tables(body_html)

    # 4. Metadatos del archivo
    fname = md_path.name
    title, doc_label = FILE_META.get(fname, (extract_title(raw), fname.replace(".md", "")))

    # 5. Ensamblar HTML final
    html_out = HTML_TEMPLATE.format(
        title=title,
        doc_label=doc_label,
        css=CSS,
        body=body_html,
    )

    # 6. Escribir archivo
    out_path = HTML_DIR / (md_path.stem + ".html")
    out_path.write_text(html_out, encoding="utf-8")
    generated.append(out_path.name)
    print(f"  ✓  {out_path.name}")

print(f"\n✅  {len(generated)} archivos HTML generados en: {HTML_DIR}")
