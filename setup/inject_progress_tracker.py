#!/usr/bin/env python3
"""
inject_progress_tracker.py
──────────────────────────
Inyecta el sistema de persistencia de progreso en todos los index.html
del módulo TGA05 — Estructura de Datos para los Negocios.

Uso:
    python3 inject_progress_tracker.py

El script modifica cada semanaX/index.html añadiendo:
  • Widget de progreso (nombre del estudiante, XP, barra)
  • localStorage para persistencia local (sobrevive cierre de Moodle)
  • Sincronización con Google Sheets vía Apps Script (opcional)
  • Botón "Guardar en la nube" y "Exportar código"
  • Quiz interactivo con registro de respuestas (reemplaza el CSS-hover)
"""

import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT     = os.path.join(BASE_DIR, "..")  # EstructuraDatos/

# ── CSS DEL WIDGET ────────────────────────────────────────────────
WIDGET_CSS = """
<style id="progress-tracker-css">
/* ── Progress Tracker Widget ── */
#pt-widget{
  position:fixed; bottom:20px; right:20px; z-index:9999;
  background:linear-gradient(135deg,#1a237e,#283593);
  color:#fff; border-radius:16px; padding:14px 18px;
  min-width:240px; max-width:280px;
  box-shadow:0 8px 32px rgba(0,0,0,.35);
  font-family:'Segoe UI',system-ui,sans-serif;
  font-size:.85rem; transition:transform .3s;
}
#pt-widget.collapsed { transform:translateY(calc(100% - 42px)); }
#pt-header{ display:flex; justify-content:space-between; align-items:center; cursor:pointer; }
#pt-header strong{ font-size:.92rem; }
#pt-toggle{ background:none; border:none; color:#fff; font-size:1.1rem; cursor:pointer; line-height:1; }
#pt-body{ margin-top:10px; }
#pt-nombre{ width:100%; background:rgba(255,255,255,.12); border:1px solid rgba(255,255,255,.3);
  border-radius:8px; color:#fff; padding:5px 10px; font-size:.82rem; margin-bottom:8px; }
#pt-nombre::placeholder{ color:rgba(255,255,255,.5); }
#pt-xp-bar-wrap{ background:rgba(255,255,255,.2); border-radius:20px; height:10px; overflow:hidden; }
#pt-xp-bar{ height:100%; background:linear-gradient(90deg,#f9a825,#fff176); border-radius:20px;
  transition:width .8s ease; }
#pt-xp-label{ display:flex; justify-content:space-between; font-size:.75rem; opacity:.8; margin-top:4px; }
#pt-btns{ display:flex; gap:6px; margin-top:10px; flex-wrap:wrap; }
.pt-btn{ flex:1; padding:5px 8px; border:none; border-radius:8px; font-size:.75rem;
  font-weight:700; cursor:pointer; transition:opacity .2s; }
.pt-btn:hover{ opacity:.85; }
#pt-btn-save  { background:#43a047; color:#fff; }
#pt-btn-export{ background:#f9a825; color:#1a237e; }
#pt-btn-load  { background:rgba(255,255,255,.15); color:#fff; border:1px solid rgba(255,255,255,.3); }
#pt-msg{ font-size:.72rem; margin-top:6px; min-height:16px; opacity:.85; text-align:center; }
#pt-quiz-panel{ margin-top:1rem; }
#pt-quiz-panel .pq{ margin-bottom:.8rem; }
#pt-quiz-panel .pq p{ font-weight:600; font-size:.88rem; margin-bottom:.4rem; }
#pt-quiz-panel .pq button{ display:block; width:100%; text-align:left; margin-bottom:3px;
  padding:5px 10px; border-radius:6px; border:1px solid rgba(255,255,255,.2);
  background:rgba(255,255,255,.08); color:#fff; cursor:pointer; font-size:.8rem;
  transition:background .2s; }
#pt-quiz-panel .pq button:hover  { background:rgba(255,255,255,.18); }
#pt-quiz-panel .pq button.correct{ background:#2e7d32; border-color:#43a047; }
#pt-quiz-panel .pq button.wrong  { background:#c62828; border-color:#e57373; }
#pt-quiz-panel .pq button:disabled{ opacity:.7; cursor:default; }
</style>
"""

# ── HTML DEL WIDGET ───────────────────────────────────────────────
WIDGET_HTML = """
<!-- ── PROGRESS TRACKER WIDGET ── -->
<div id="pt-widget">
  <div id="pt-header" onclick="ptToggle()">
    <strong>📊 Mi Progreso TGA05</strong>
    <button id="pt-toggle">▲</button>
  </div>
  <div id="pt-body">
    <input id="pt-nombre" type="text" placeholder="Tu nombre completo…" oninput="ptSaveLocal()" />
    <div id="pt-xp-bar-wrap"><div id="pt-xp-bar" style="width:0%"></div></div>
    <div id="pt-xp-label"><span id="pt-semana-label">Semana —</span><span id="pt-xp-count">0 XP</span></div>
    <div id="pt-btns">
      <button class="pt-btn" id="pt-btn-save"   onclick="ptSyncCloud()">☁️ Guardar</button>
      <button class="pt-btn" id="pt-btn-export" onclick="ptExportCode()">📋 Código</button>
      <button class="pt-btn" id="pt-btn-load"   onclick="ptImportCode()">📥 Cargar</button>
    </div>
    <div id="pt-msg"></div>
  </div>
</div>
"""

# ── JAVASCRIPT DEL TRACKER ────────────────────────────────────────
def build_tracker_js(semana_num):
    return f"""
<script id="progress-tracker-js">
// ════════════════════════════════════════════════════
//  NeuroBiz Progress Tracker · Semana {semana_num}
// ════════════════════════════════════════════════════

const PT = (function() {{
  const SEMANA       = {semana_num};
  const XP_BASE      = {semana_num * 5};          // XP base por abrir el material
  const XP_MAX       = 100;
  const LS_KEY       = `tga05_s{semana_num}`;
  const LS_GLOBAL    = "tga05_global";

  // URL del Apps Script — reemplaza con tu URL al configurar
  // Ver: EstructuraDatos/setup/CONFIGURAR_PROGRESO.html
  const SHEETS_URL = localStorage.getItem("tga05_sheets_url") || "";

  let state = {{
    nombre          : "",
    id_estudiante   : "",
    semana          : SEMANA,
    xp              : XP_BASE,
    quiz_respuestas : {{}},
    quiz_puntaje    : 0,
    hti_entregado   : false,
    actividad_completada: false,
    dispositivo     : navigator.userAgent.substring(0, 80)
  }};

  // ── Cargar desde localStorage ──────────────────────
  function load() {{
    try {{
      const raw = localStorage.getItem(LS_KEY);
      if (raw) Object.assign(state, JSON.parse(raw));

      // Cargar nombre/id del perfil global si no está en esta semana
      const global = JSON.parse(localStorage.getItem(LS_GLOBAL) || "{{}}");
      if (!state.nombre       && global.nombre)        state.nombre        = global.nombre;
      if (!state.id_estudiante && global.id_estudiante) state.id_estudiante = global.id_estudiante;
    }} catch(e) {{ console.warn("PT load error:", e); }}
  }}

  // ── Guardar en localStorage ────────────────────────
  function save() {{
    // Capturar nombre del input
    const inp = document.getElementById("pt-nombre");
    if (inp && inp.value.trim()) {{
      state.nombre = inp.value.trim();
      // Generar ID si no existe
      if (!state.id_estudiante) {{
        state.id_estudiante = state.nombre.toLowerCase()
          .replace(/\\s+/g,"_").replace(/[^a-z0-9_]/g,"")
          .substring(0,20) + "_" + Math.random().toString(36).substr(2,4);
      }}
      // Guardar perfil global
      const global = JSON.parse(localStorage.getItem(LS_GLOBAL) || "{{}}");
      global.nombre = state.nombre;
      global.id_estudiante = state.id_estudiante;
      localStorage.setItem(LS_GLOBAL, JSON.stringify(global));
    }}
    localStorage.setItem(LS_KEY, JSON.stringify(state));
    render();
  }}

  // ── Renderizar widget ──────────────────────────────
  function render() {{
    const xpBar   = document.getElementById("pt-xp-bar");
    const xpCount = document.getElementById("pt-xp-count");
    const semLbl  = document.getElementById("pt-semana-label");
    const inp     = document.getElementById("pt-nombre");

    if (xpBar)   xpBar.style.width   = Math.min(state.xp, XP_MAX) + "%";
    if (xpCount) xpCount.textContent = state.xp + " XP";
    if (semLbl)  semLbl.textContent  = "Semana " + SEMANA;
    if (inp && !inp.value && state.nombre) inp.value = state.nombre;

    // Sync original XP bars in the page
    document.querySelectorAll(".xp-fill,[data-target]").forEach(el => {{
      el.style.width = Math.min(state.xp, XP_MAX) + "%";
    }});
    const xpCounters = document.querySelectorAll("#xpCount,.xp-row strong");
    xpCounters.forEach(el => {{ el.textContent = state.xp + " XP"; }});
  }}

  // ── Sumar XP ──────────────────────────────────────
  function addXP(pts, motivo) {{
    state.xp = Math.min(state.xp + pts, XP_MAX);
    msg("✨ +" + pts + " XP — " + motivo, "lime");
    save();
  }}

  // ── Sincronizar con Google Sheets ─────────────────
  async function syncCloud() {{
    const url = localStorage.getItem("tga05_sheets_url") || "";
    if (!url) {{
      msg("⚠️ No configurado. Ver CONFIGURAR_PROGRESO.html", "orange");
      return;
    }}
    save();
    try {{
      msg("⏳ Sincronizando…", "#fff9c4");
      const resp = await fetch(url, {{
        method : "POST",
        headers: {{ "Content-Type": "text/plain" }},
        body   : JSON.stringify(state)
      }});
      const json = await resp.json();
      if (json.ok) msg("✅ Guardado en Google Sheets", "lightgreen");
      else         msg("❌ " + (json.error || "Error"), "salmon");
    }} catch(e) {{
      msg("❌ Sin conexión. Guardado solo localmente.", "salmon");
    }}
  }}

  // ── Exportar código de progreso ────────────────────
  function exportCode() {{
    save();
    const code = btoa(unescape(encodeURIComponent(JSON.stringify(state))));
    const ta = document.createElement("textarea");
    ta.value = code;
    document.body.appendChild(ta); ta.select(); document.execCommand("copy");
    document.body.removeChild(ta);
    msg("📋 ¡Código copiado! Guárdalo en Google Drive o OneDrive.", "#fff9c4");
    // También abrir como descarga
    const a = document.createElement("a");
    a.href     = "data:text/plain;charset=utf-8," + encodeURIComponent(code);
    a.download = "progreso_tga05_s{semana_num}_" + (state.id_estudiante || "estudiante") + ".txt";
    a.click();
  }}

  // ── Importar desde código ──────────────────────────
  function importCode() {{
    const code = prompt("Pega tu código de progreso:");
    if (!code) return;
    try {{
      const decoded = JSON.parse(decodeURIComponent(escape(atob(code.trim()))));
      Object.assign(state, decoded);
      save();
      msg("✅ Progreso restaurado correctamente.", "lightgreen");
    }} catch(e) {{
      msg("❌ Código inválido.", "salmon");
    }}
  }}

  // ── Toggle widget ──────────────────────────────────
  function toggle() {{
    const w = document.getElementById("pt-widget");
    const t = document.getElementById("pt-toggle");
    if (w) w.classList.toggle("collapsed");
    if (t) t.textContent = w && w.classList.contains("collapsed") ? "▼" : "▲";
  }}

  // ── Mensaje en widget ──────────────────────────────
  function msg(text, color) {{
    const el = document.getElementById("pt-msg");
    if (!el) return;
    el.textContent = text;
    el.style.color = color || "#fff";
    setTimeout(() => {{ if (el.textContent === text) el.textContent = ""; }}, 4000);
  }}

  // ── Init ───────────────────────────────────────────
  function init() {{
    load();
    render();

    // XP por visitar la semana (solo una vez por semana)
    const visitKey = `tga05_visited_s{semana_num}`;
    if (!localStorage.getItem(visitKey)) {{
      localStorage.setItem(visitKey, "1");
      addXP(15, "Material de Semana {semana_num} abierto");
    }}

    // Hacer quiz interactivo si hay preguntas con clase .quiz-q
    document.querySelectorAll(".quiz-q").forEach((qEl, qi) => {{
      const answers = qEl.querySelectorAll("li");
      // Buscar la respuesta oculta (.quiz-answer)
      const answerEl = qEl.querySelector(".quiz-answer");
      const correctText = answerEl ? answerEl.textContent : "";
      const correctLetter = correctText.match(/^✅\\s*([a-d])/i);
      const correctIdx = correctLetter
        ? ["a","b","c","d"].indexOf(correctLetter[1].toLowerCase())
        : -1;

      answers.forEach((li, ai) => {{
        li.style.cursor = "pointer";
        li.style.borderRadius = "6px";
        li.style.padding = "3px 8px";
        li.style.transition = "background .2s";
        li.addEventListener("mouseenter", () => {{
          if (!li.dataset.answered) li.style.background = "rgba(25,118,210,.15)";
        }});
        li.addEventListener("mouseleave", () => {{
          if (!li.dataset.answered) li.style.background = "";
        }});
        li.addEventListener("click", () => {{
          const key = "q" + qi;
          if (state.quiz_respuestas[key] !== undefined) return; // ya respondida
          answers.forEach(a => {{ a.dataset.answered = "1"; }});
          if (ai === correctIdx) {{
            li.style.background = "#2e7d32";
            li.style.color = "#fff";
            addXP(10, "Respuesta correcta en quiz");
            state.quiz_puntaje = (state.quiz_puntaje || 0) + 1;
          }} else {{
            li.style.background = "#c62828";
            li.style.color = "#fff";
            if (correctIdx >= 0) {{
              answers[correctIdx].style.background = "#2e7d32";
              answers[correctIdx].style.color = "#fff";
            }}
          }}
          state.quiz_respuestas[key] = ai;
          if (answerEl) answerEl.style.display = "block";
          save();
        }});
      }});

      // Restaurar estado previo
      const prevKey = "q" + qi;
      if (state.quiz_respuestas[prevKey] !== undefined) {{
        const prev = state.quiz_respuestas[prevKey];
        answers.forEach(a => {{ a.dataset.answered = "1"; }});
        if (prev === correctIdx && correctIdx >= 0) {{
          answers[prev].style.background = "#2e7d32";
          answers[prev].style.color = "#fff";
        }} else {{
          if (prev < answers.length) {{
            answers[prev].style.background = "#c62828";
            answers[prev].style.color = "#fff";
          }}
          if (correctIdx >= 0) {{
            answers[correctIdx].style.background = "#2e7d32";
            answers[correctIdx].style.color = "#fff";
          }}
        }}
        if (answerEl) answerEl.style.display = "block";
      }}
    }});

    // XP por configurar nombre
    const nombreInp = document.getElementById("pt-nombre");
    if (nombreInp) {{
      nombreInp.addEventListener("blur", () => {{
        if (nombreInp.value.trim() && !state._nombre_xp) {{
          state._nombre_xp = true;
          addXP(5, "Perfil configurado");
        }}
      }});
    }}
  }}

  return {{
    init,
    addXP,
    save  : save,
    sync  : syncCloud,
    export: exportCode,
    import: importCode,
    toggle,
    state : () => state
  }};
}})();

// ── Exponer funciones para botones HTML ────────────────────
function ptSaveLocal()  {{ PT.save(); }}
function ptSyncCloud()  {{ PT.sync(); }}
function ptExportCode() {{ PT.export(); }}
function ptImportCode() {{ PT.import(); }}
function ptToggle()     {{ PT.toggle(); }}

// ── Inicializar cuando cargue el DOM ───────────────────────
if (document.readyState === "loading") {{
  document.addEventListener("DOMContentLoaded", PT.init);
}} else {{
  PT.init();
}}
</script>
"""

def inject_into_html(filepath, semana_num):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Skip if already injected
    if "progress-tracker-js" in content:
        print(f"  ⏭  Ya inyectado: {filepath}")
        return False

    # Inject CSS before </head>
    if "</head>" in content:
        content = content.replace("</head>", WIDGET_CSS + "\n</head>", 1)
    else:
        content = WIDGET_CSS + content

    # Inject Widget HTML right after <main> or after <body>
    if "<main>" in content:
        content = content.replace("<main>", "<main>\n" + WIDGET_HTML, 1)
    elif "<body>" in content:
        content = content.replace("<body>", "<body>\n" + WIDGET_HTML, 1)
    else:
        content += WIDGET_HTML

    # Inject JS before </body>
    tracker_js = build_tracker_js(semana_num)
    if "</body>" in content:
        content = content.replace("</body>", tracker_js + "\n</body>", 1)
    else:
        content += tracker_js

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    return True

def main():
    print("🚀 NeuroBiz Progress Tracker — Inyección en TGA05")
    print("=" * 50)

    modified = 0
    skipped  = 0
    errors   = 0

    for semana in range(1, 15):
        folder = os.path.join(ROOT, f"semana{semana}")
        index  = os.path.join(folder, "index.html")

        if not os.path.exists(index):
            print(f"  ❌ No encontrado: {index}")
            errors += 1
            continue

        try:
            changed = inject_into_html(index, semana)
            size    = os.path.getsize(index) // 1024
            if changed:
                print(f"  ✅ Semana {semana:2d} → {size}K")
                modified += 1
            else:
                skipped += 1
        except Exception as e:
            print(f"  ❌ Error en semana {semana}: {e}")
            errors += 1

    print("=" * 50)
    print(f"✅ Modificados : {modified}")
    print(f"⏭  Ya inyectados: {skipped}")
    print(f"❌ Errores     : {errors}")
    print()
    print("Próximo paso: Configura la URL de Google Sheets")
    print("→ Abre: EstructuraDatos/setup/CONFIGURAR_PROGRESO.html")

if __name__ == "__main__":
    main()
