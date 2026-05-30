#!/usr/bin/env python3
"""
update_widget_modal.py
──────────────────────
Para cada semana*/index.html:
  1. Inyecta <script src="../js/supabase-config.js"> en el <head>
  2. Reemplaza los botones del widget (simplificar: ⚙️ oculta Código/Cargar)
  3. Inyecta el modal de bienvenida (CSS + HTML + JS) antes de </body>

Idempotente: verifica marcadores antes de modificar.
"""

import os, re

ROOT = os.path.join(os.path.dirname(__file__), "..")

# ─────────────────────────────────────────────────────────────────
#  1. CONFIG SCRIPT TAG (inject in <head>)
# ─────────────────────────────────────────────────────────────────
CONFIG_SCRIPT_TAG = '  <script src="../js/supabase-config.js"></script>\n'
CONFIG_MARKER     = 'supabase-config.js'

# ─────────────────────────────────────────────────────────────────
#  2. WIDGET BUTTONS — OLD vs NEW
# ─────────────────────────────────────────────────────────────────
OLD_BTNS = '''    <div id="pt-btns">
      <button class="pt-btn" id="pt-btn-save"   onclick="ptSyncCloud()">☁️ Guardar</button>
      <button class="pt-btn" id="pt-btn-export" onclick="ptExportCode()">📋 Código</button>
      <button class="pt-btn" id="pt-btn-load"   onclick="ptImportCode()">📥 Cargar</button>
    </div>'''

NEW_BTNS = '''    <div id="pt-btns" style="display:flex;gap:5px;align-items:center">
      <button class="pt-btn" id="pt-btn-save" onclick="ptSyncCloud()" style="flex:1">☁️ Guardar</button>
      <button class="pt-btn" id="pt-btn-opts"
        title="Opciones de respaldo"
        onclick="(function(){var a=document.getElementById('pt-advanced');a.style.display=a.style.display==='block'?'none':'block';})()"
        style="width:32px;flex-shrink:0;padding:0;font-size:.8rem">⚙️</button>
    </div>
    <div id="pt-advanced" style="display:none;margin-top:5px">
      <button class="pt-btn" onclick="ptExportCode()" style="width:100%;margin-bottom:3px;font-size:.72rem">📋 Exportar código de respaldo</button>
      <button class="pt-btn" onclick="ptImportCode()" style="width:100%;font-size:.72rem">📥 Cargar desde código</button>
    </div>'''

# ─────────────────────────────────────────────────────────────────
#  3. WELCOME MODAL — injected before </body>
# ─────────────────────────────────────────────────────────────────
MODAL_MARKER = 'pt-welcome-modal'

MODAL_BLOCK = '''<!-- ── WELCOME MODAL ── -->
<style id="welcome-modal-css">
#pt-overlay{
  position:fixed;inset:0;background:rgba(0,0,0,.55);z-index:9999;
  display:flex;align-items:center;justify-content:center;
  animation:fadeIn .3s ease;
}
@keyframes fadeIn{from{opacity:0}to{opacity:1}}
#pt-modal-box{
  background:linear-gradient(160deg,#1a237e,#283593 70%,#3949ab);
  color:#fff;border-radius:20px;padding:2rem 2rem 1.5rem;
  width:min(94vw,400px);box-shadow:0 20px 60px rgba(0,0,0,.5);
  position:relative;animation:slideUp .35s cubic-bezier(.2,.8,.3,1);
}
@keyframes slideUp{from{transform:translateY(30px);opacity:0}to{transform:translateY(0);opacity:1}}
#pt-modal-box h2{font-size:1.25rem;font-weight:900;margin-bottom:.3rem}
#pt-modal-box .sub{opacity:.75;font-size:.85rem;margin-bottom:1.3rem}
#pt-modal-box .field{margin-bottom:.9rem}
#pt-modal-box label{display:block;font-size:.78rem;font-weight:700;
  opacity:.85;margin-bottom:.3rem;text-transform:uppercase;letter-spacing:.05em}
#pt-modal-box input{
  width:100%;background:rgba(255,255,255,.12);border:1.5px solid rgba(255,255,255,.35);
  border-radius:10px;padding:.6rem .9rem;color:#fff;font-size:.95rem;outline:none;
}
#pt-modal-box input::placeholder{color:rgba(255,255,255,.45)}
#pt-modal-box input:focus{border-color:rgba(249,168,37,.9)}
#pt-modal-btn{
  width:100%;padding:.7rem;border:none;border-radius:12px;
  background:linear-gradient(135deg,#f9a825,#ffd54f);
  color:#1a237e;font-weight:900;font-size:1rem;cursor:pointer;
  margin-top:.4rem;transition:opacity .15s;
}
#pt-modal-btn:hover{opacity:.9}
#pt-modal-error{color:#ff8a80;font-size:.8rem;margin-top:.5rem;min-height:1em}
#pt-modal-xp{
  text-align:center;font-size:.78rem;opacity:.7;margin-top:.7rem;
}
</style>

<div id="pt-overlay" style="display:none" role="dialog" aria-modal="true" aria-labelledby="pt-modal-title">
  <div id="pt-modal-box">
    <h2 id="pt-modal-title">👋 ¡Bienvenido a TGA05!</h2>
    <p class="sub">NeuroBiz S.A.S. · Estructura de Datos para los Negocios</p>
    <div class="field">
      <label for="pt-modal-nombre">Tu nombre completo *</label>
      <input id="pt-modal-nombre" type="text" placeholder="Ej: María García López"
        autocomplete="name" autofocus
        onkeydown="if(event.key==='Enter')ptModalSetup()" />
    </div>
    <div class="field">
      <label for="pt-modal-grupo">Grupo / Paralelo</label>
      <input id="pt-modal-grupo" type="text" placeholder="Ej: GA-01" />
    </div>
    <button id="pt-modal-btn" onclick="ptModalSetup()">¡Empezar! 🚀</button>
    <div id="pt-modal-error"></div>
    <p id="pt-modal-xp">⭐ Recibirás +5 XP por configurar tu perfil</p>
  </div>
</div>

<script id="welcome-modal-js">
(function () {
  function shouldShowModal() {
    try {
      var g = JSON.parse(localStorage.getItem("tga05_global") || "{}");
      return !g.nombre || g.nombre.trim().length < 2;
    } catch(e) { return true; }
  }

  function showModal() {
    var overlay = document.getElementById("pt-overlay");
    if (overlay) {
      overlay.style.display = "flex";
      var inp = document.getElementById("pt-modal-nombre");
      // Pre-fill if there's a partial name saved
      try {
        var g = JSON.parse(localStorage.getItem("tga05_global") || "{}");
        if (g.nombre && inp) inp.value = g.nombre;
        var gInp = document.getElementById("pt-modal-grupo");
        if (g.grupo && gInp) gInp.value = g.grupo;
      } catch(e) {}
      if (inp) setTimeout(function(){ inp.focus(); }, 100);
    }
  }

  window.ptModalSetup = function() {
    var nombreInp = document.getElementById("pt-modal-nombre");
    var grupoInp  = document.getElementById("pt-modal-grupo");
    var errEl     = document.getElementById("pt-modal-error");
    var nombre    = nombreInp ? nombreInp.value.trim() : "";
    var grupo     = grupoInp  ? grupoInp.value.trim()  : "";

    if (!nombre || nombre.length < 3) {
      if (errEl) errEl.textContent = "Por favor escribe tu nombre completo (mínimo 3 caracteres).";
      if (nombreInp) nombreInp.focus();
      return;
    }

    // Build / update global profile
    var profile = {};
    try { profile = JSON.parse(localStorage.getItem("tga05_global") || "{}"); } catch(e) {}

    profile.nombre = nombre;
    if (grupo) profile.grupo = grupo;
    if (!profile.id_estudiante) {
      profile.id_estudiante = nombre.toLowerCase()
        .replace(/\\s+/g, "_").replace(/[^a-z0-9_áéíóúñ]/g, "")
        .substring(0, 22) + "_" + Math.random().toString(36).substr(2, 4);
    }
    localStorage.setItem("tga05_global", JSON.stringify(profile));

    // Sync into the PT widget name input
    var ptInp = document.getElementById("pt-nombre");
    if (ptInp) { ptInp.value = nombre; ptInp.dispatchEvent(new Event("input")); }

    // XP reward
    if (typeof PT !== "undefined" && typeof PT.addXP === "function") {
      PT.addXP(5, "Perfil configurado ✨");
    }

    // Close modal
    var overlay = document.getElementById("pt-overlay");
    if (overlay) {
      overlay.style.opacity = "0";
      overlay.style.transition = "opacity .2s";
      setTimeout(function(){ overlay.style.display = "none"; overlay.style.opacity = ""; }, 200);
    }

    // Auto-sync to Supabase after a short delay
    setTimeout(function(){
      if (typeof PT !== "undefined" && typeof PT.sync === "function") PT.sync();
    }, 800);
  };

  // Show on load if no name
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", function(){
      if (shouldShowModal()) showModal();
    });
  } else {
    if (shouldShowModal()) showModal();
  }
})();
</script>
'''

# ─────────────────────────────────────────────────────────────────
def process_file(path, semana_num):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    changes = []

    # 1. Inject config.js in <head>
    if CONFIG_MARKER not in content:
        content = content.replace("</head>", CONFIG_SCRIPT_TAG + "</head>", 1)
        changes.append("config.js injected")

    # 2. Simplify widget buttons
    if OLD_BTNS in content:
        content = content.replace(OLD_BTNS, NEW_BTNS, 1)
        changes.append("widget simplified")
    elif NEW_BTNS in content:
        changes.append("widget already simplified")

    # 3. Inject welcome modal before </body>
    if MODAL_MARKER not in content:
        content = content.replace("</body>", MODAL_BLOCK + "\n</body>", 1)
        changes.append("welcome modal injected")

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

    return changes


def main():
    total_ok = 0
    for i in range(1, 15):
        path = os.path.join(ROOT, f"semana{i}", "index.html")
        if not os.path.exists(path):
            print(f"  S{i:02d}: ❌ FALTA")
            continue
        changes = process_file(path, i)
        total_ok += 1
        print(f"  S{i:02d}: ✅ {' | '.join(changes)}")

    print(f"\n{'─'*50}")
    print(f"  Procesados: {total_ok}/14")


if __name__ == "__main__":
    main()
