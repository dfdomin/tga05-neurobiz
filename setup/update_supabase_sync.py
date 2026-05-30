#!/usr/bin/env python3
"""
update_supabase_sync.py
Actualiza la función syncCloud en todos los index.html de TGA05
para soportar Supabase, Google Sheets (existente) y OneDrive/GDrive (exportación mejorada).
"""
import os, re

ROOT = os.path.join(os.path.dirname(__file__), "..")

OLD_SYNC = '''// ── Sincronizar con Google Sheets ─────────────────
  async function syncCloud() {
    const url = localStorage.getItem("tga05_sheets_url") || "";
    if (!url) {
      msg("⚠️ No configurado. Ver CONFIGURAR_PROGRESO.html", "orange");
      return;
    }
    save();
    try {
      msg("⏳ Sincronizando…", "#fff9c4");
      const resp = await fetch(url, {
        method : "POST",
        headers: { "Content-Type": "text/plain" },
        body   : JSON.stringify(state)
      });
      const json = await resp.json();
      if (json.ok) msg("✅ Guardado en Google Sheets", "lightgreen");
      else         msg("❌ " + (json.error || "Error"), "salmon");
    } catch(e) {
      msg("❌ Sin conexión. Guardado solo localmente.", "salmon");
    }
  }'''

NEW_SYNC = '''// ── Sincronizar con Supabase + Google Sheets ──────
  async function syncCloud() {
    save();
    const sheetsUrl = localStorage.getItem("tga05_sheets_url") || "";
    const sbUrl     = localStorage.getItem("tga05_supabase_url") || "";
    const sbKey     = localStorage.getItem("tga05_supabase_key") || "";

    if (!sheetsUrl && !sbUrl) {
      msg("⚠️ Sin destino configurado. Ver CONFIGURAR_SUPABASE.html", "orange");
      return;
    }

    msg("⏳ Sincronizando…", "#fff9c4");
    let synced = false;

    // ── Supabase (recomendado) ─────────────────────
    if (sbUrl && sbKey) {
      try {
        const res = await fetch(sbUrl + "/rest/v1/student_progress", {
          method : "POST",
          headers: {
            "apikey"       : sbKey,
            "Authorization": "Bearer " + sbKey,
            "Content-Type" : "application/json",
            "Prefer"       : "resolution=merge-duplicates"
          },
          body: JSON.stringify({
            student_name    : state.nombre         || "Anónimo",
            student_id      : state.id_estudiante  || "desconocido",
            semana          : state.semana,
            xp              : state.xp             || 0,
            quiz_answers    : state.quiz_respuestas || {},
            quiz_score      : state.quiz_puntaje    || 0,
            hti_done        : !!state.hti_entregado,
            activity_done   : !!state.actividad_completada,
            updated_at      : new Date().toISOString()
          })
        });
        if (res.ok || res.status === 201) {
          synced = true;
          msg("✅ Guardado en Supabase ☁️", "lightgreen");
        } else {
          msg("❌ Supabase: error " + res.status, "salmon");
        }
      } catch(e) {
        msg("❌ Sin conexión (Supabase). Local guardado.", "salmon");
      }
    }

    // ── Google Sheets (opcional adicional) ─────────
    if (sheetsUrl) {
      try {
        const resp = await fetch(sheetsUrl, {
          method : "POST",
          headers: { "Content-Type": "text/plain" },
          body   : JSON.stringify(state)
        });
        const json = await resp.json();
        if (json.ok) {
          synced = true;
          msg(sbUrl ? "✅ Guardado en Supabase + Sheets" : "✅ Guardado en Google Sheets", "lightgreen");
        } else {
          if (!synced) msg("❌ Sheets: " + (json.error || "Error"), "salmon");
        }
      } catch(e) {
        if (!synced) msg("❌ Sin conexión. Solo guardado local.", "salmon");
      }
    }
  }'''


def update_file(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    if OLD_SYNC not in content:
        return False, "texto no encontrado (ya actualizado o diferente)"

    updated = content.replace(OLD_SYNC, NEW_SYNC, 1)

    with open(path, "w", encoding="utf-8") as f:
        f.write(updated)
    return True, "OK"


def main():
    updated = 0
    skipped = 0
    for i in range(1, 15):
        path = os.path.join(ROOT, f"semana{i}", "index.html")
        if not os.path.exists(path):
            print(f"  S{i:02d}: ❌ FALTA {path}")
            continue
        ok, reason = update_file(path)
        if ok:
            updated += 1
            print(f"  S{i:02d}: ✅ actualizado")
        else:
            skipped += 1
            print(f"  S{i:02d}: ⏭  {reason}")
    print(f"\n{'─'*40}")
    print(f"  Actualizados: {updated}/14")
    print(f"  Omitidos:     {skipped}/14")


if __name__ == "__main__":
    main()
