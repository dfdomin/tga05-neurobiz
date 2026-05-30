// ══════════════════════════════════════════════════════════════════
//  NeuroBiz Progress Tracker — Google Apps Script
//  Módulo TGA05 · Estructura de Datos para los Negocios · UIB
//
//  INSTRUCCIONES DE DESPLIEGUE (ver CONFIGURAR_PROGRESO.html):
//  1. Crear un Google Sheet nuevo
//  2. Ir a Extensiones → Apps Script
//  3. Pegar TODO este código (reemplazar lo que hay)
//  4. Guardar → Implementar → Nueva implementación
//  5. Tipo: Aplicación web | Acceso: Cualquier persona
//  6. Copiar la URL y pegarla en CONFIGURAR_PROGRESO.html
// ══════════════════════════════════════════════════════════════════

const SHEET_NAME    = "Progreso_TGA05";
const SEMANAS_TOTAL = 14;

// ── Encabezados de columnas ───────────────────────────────────────
const HEADERS = [
  "Timestamp", "Estudiante", "ID_Estudiante", "Semana",
  "XP", "Quiz_Respuestas", "Quiz_Puntaje",
  "HTI_Entregado", "Actividad_Completada", "Dispositivo"
];

// ── Obtener o crear la hoja ───────────────────────────────────────
function getSheet() {
  const ss    = SpreadsheetApp.getActiveSpreadsheet();
  let   sheet = ss.getSheetByName(SHEET_NAME);
  if (!sheet) {
    sheet = ss.insertSheet(SHEET_NAME);
    sheet.appendRow(HEADERS);
    sheet.getRange(1, 1, 1, HEADERS.length)
         .setBackground("#1a237e")
         .setFontColor("#ffffff")
         .setFontWeight("bold");
    sheet.setFrozenRows(1);
  }
  return sheet;
}

// ── CORS helper ───────────────────────────────────────────────────
function corsOutput(data) {
  return ContentService
    .createTextOutput(JSON.stringify(data))
    .setMimeType(ContentService.MimeType.JSON);
}

// ── POST: guardar progreso ────────────────────────────────────────
function doPost(e) {
  try {
    const data    = JSON.parse(e.postData.contents);
    const sheet   = getSheet();
    const now     = new Date().toLocaleString("es-CO", { timeZone: "America/Bogota" });

    sheet.appendRow([
      now,
      data.nombre        || "Sin nombre",
      data.id_estudiante || "sin-id",
      data.semana        || 0,
      data.xp            || 0,
      JSON.stringify(data.quiz_respuestas || {}),
      data.quiz_puntaje  || 0,
      data.hti_entregado ? "SI" : "NO",
      data.actividad_completada ? "SI" : "NO",
      data.dispositivo   || "desconocido"
    ]);

    // Actualizar fila existente si el estudiante ya tenía registro para esa semana
    actualizarOAgregar(sheet, data, now);

    return corsOutput({ ok: true, mensaje: "Progreso guardado correctamente." });
  } catch (err) {
    return corsOutput({ ok: false, error: err.toString() });
  }
}

// ── Actualizar en lugar de duplicar ──────────────────────────────
function actualizarOAgregar(sheet, data, now) {
  const rows    = sheet.getDataRange().getValues();
  const idCol   = HEADERS.indexOf("ID_Estudiante") + 1;  // 1-based
  const semCol  = HEADERS.indexOf("Semana") + 1;

  for (let i = 1; i < rows.length; i++) {  // skip header
    if (rows[i][idCol - 1] === data.id_estudiante &&
        rows[i][semCol - 1] === data.semana) {
      // Actualizar fila existente
      sheet.getRange(i + 1, 1, 1, HEADERS.length).setValues([[
        now,
        data.nombre        || "Sin nombre",
        data.id_estudiante || "sin-id",
        data.semana        || 0,
        data.xp            || 0,
        JSON.stringify(data.quiz_respuestas || {}),
        data.quiz_puntaje  || 0,
        data.hti_entregado ? "SI" : "NO",
        data.actividad_completada ? "SI" : "NO",
        data.dispositivo   || "desconocido"
      ]]);
      // Eliminar la última fila (que se agregó con appendRow)
      sheet.deleteRow(sheet.getLastRow());
      return;
    }
  }
  // Si no se encontró, la fila ya quedó con appendRow — no hacer nada más
}

// ── GET: cargar progreso de un estudiante ─────────────────────────
function doGet(e) {
  try {
    const idEstudiante = e.parameter.id_estudiante;
    const semana       = parseInt(e.parameter.semana) || null;

    if (!idEstudiante) {
      return corsOutput({ ok: false, error: "Se requiere id_estudiante." });
    }

    const sheet = getSheet();
    const rows  = sheet.getDataRange().getValues();
    const result = [];

    for (let i = 1; i < rows.length; i++) {
      const row = rows[i];
      if (row[HEADERS.indexOf("ID_Estudiante")] === idEstudiante) {
        if (semana === null || row[HEADERS.indexOf("Semana")] === semana) {
          result.push({
            timestamp           : row[HEADERS.indexOf("Timestamp")],
            nombre              : row[HEADERS.indexOf("Estudiante")],
            semana              : row[HEADERS.indexOf("Semana")],
            xp                  : row[HEADERS.indexOf("XP")],
            quiz_respuestas     : row[HEADERS.indexOf("Quiz_Respuestas")],
            quiz_puntaje        : row[HEADERS.indexOf("Quiz_Puntaje")],
            hti_entregado       : row[HEADERS.indexOf("HTI_Entregado")] === "SI",
            actividad_completada: row[HEADERS.indexOf("Actividad_Completada")] === "SI"
          });
        }
      }
    }

    return corsOutput({ ok: true, data: result });
  } catch (err) {
    return corsOutput({ ok: false, error: err.toString() });
  }
}

// ── Dashboard resumen del profesor (opcional) ─────────────────────
function generarResumen() {
  const sheet    = getSheet();
  const ss       = SpreadsheetApp.getActiveSpreadsheet();
  let   resumen  = ss.getSheetByName("Resumen_Docente");
  if (!resumen) resumen = ss.insertSheet("Resumen_Docente");
  resumen.clearContents();

  const rows  = sheet.getDataRange().getValues().slice(1); // sin header
  const mapa  = {};  // id_estudiante → { nombre, xp_total, semanas_vistas }

  rows.forEach(row => {
    const id     = row[HEADERS.indexOf("ID_Estudiante")];
    const nombre = row[HEADERS.indexOf("Estudiante")];
    const xp     = parseInt(row[HEADERS.indexOf("XP")]) || 0;
    const sem    = row[HEADERS.indexOf("Semana")];
    if (!mapa[id]) mapa[id] = { nombre, xp_total: 0, semanas: new Set() };
    mapa[id].xp_total += xp;
    mapa[id].semanas.add(sem);
  });

  resumen.appendRow(["ID", "Nombre", "XP Total", "Semanas Visitadas", "% Avance"]);
  Object.entries(mapa).forEach(([id, d]) => {
    resumen.appendRow([
      id, d.nombre, d.xp_total,
      d.semanas.size,
      `${Math.round(d.semanas.size / SEMANAS_TOTAL * 100)}%`
    ]);
  });

  resumen.getRange(1, 1, 1, 5).setBackground("#2e7d32").setFontColor("#fff").setFontWeight("bold");
  SpreadsheetApp.getUi().alert("✅ Resumen del docente generado en la hoja 'Resumen_Docente'.");
}

// ── Menú personalizado en el Sheet ───────────────────────────────
function onOpen() {
  SpreadsheetApp.getUi()
    .createMenu("📊 TGA05 NeuroBiz")
    .addItem("Generar resumen docente", "generarResumen")
    .addToUi();
}
