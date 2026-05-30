-- ══════════════════════════════════════════════════════════
--  TGA05 · NeuroBiz S.A.S. — Supabase Schema
--  Ejecuta este script en el SQL Editor de Supabase
-- ══════════════════════════════════════════════════════════

-- 1. Tabla principal de progreso
CREATE TABLE IF NOT EXISTS student_progress (
  id            UUID        DEFAULT gen_random_uuid() PRIMARY KEY,
  created_at    TIMESTAMPTZ DEFAULT NOW(),
  updated_at    TIMESTAMPTZ DEFAULT NOW(),

  -- Identificación del estudiante
  student_name  TEXT        NOT NULL DEFAULT 'Anónimo',
  student_id    TEXT        NOT NULL DEFAULT 'desconocido',

  -- Datos de progreso
  semana        INTEGER     NOT NULL CHECK (semana BETWEEN 1 AND 14),
  xp            INTEGER     NOT NULL DEFAULT 0 CHECK (xp >= 0),
  quiz_answers  JSONB       DEFAULT '{}',
  quiz_score    INTEGER     DEFAULT 0,
  hti_done      BOOLEAN     DEFAULT FALSE,
  activity_done BOOLEAN     DEFAULT FALSE,

  -- Evitar duplicados: un estudiante tiene una sola fila por semana
  UNIQUE (student_id, semana)
);

-- 2. Índices para dashboard del docente
CREATE INDEX IF NOT EXISTS idx_sp_student_id ON student_progress(student_id);
CREATE INDEX IF NOT EXISTS idx_sp_semana     ON student_progress(semana);
CREATE INDEX IF NOT EXISTS idx_sp_updated    ON student_progress(updated_at DESC);

-- 3. Actualizar updated_at automáticamente
CREATE OR REPLACE FUNCTION update_updated_at()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = NOW();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS trg_updated_at ON student_progress;
CREATE TRIGGER trg_updated_at
  BEFORE UPDATE ON student_progress
  FOR EACH ROW EXECUTE FUNCTION update_updated_at();

-- ══════════════════════════════════════════════════════════
--  Row Level Security (RLS)
--  Los estudiantes pueden insertar/actualizar SUS propios datos.
--  El docente ve TODO desde el dashboard de Supabase.
-- ══════════════════════════════════════════════════════════

ALTER TABLE student_progress ENABLE ROW LEVEL SECURITY;

-- Política: cualquier anónimo puede insertar (estudiantes sin login)
CREATE POLICY "anon_insert"
  ON student_progress FOR INSERT
  TO anon
  WITH CHECK (true);

-- Política: cualquier anónimo puede actualizar (UPSERT)
CREATE POLICY "anon_update"
  ON student_progress FOR UPDATE
  TO anon
  USING (true);

-- Política: cualquier anónimo puede leer (para recuperar su progreso)
CREATE POLICY "anon_select"
  ON student_progress FOR SELECT
  TO anon
  USING (true);

-- ══════════════════════════════════════════════════════════
--  Vista de resumen para el docente
-- ══════════════════════════════════════════════════════════
CREATE OR REPLACE VIEW resumen_docente AS
SELECT
  student_name                              AS estudiante,
  student_id,
  COUNT(DISTINCT semana)                    AS semanas_visitadas,
  SUM(xp)                                  AS xp_total,
  ROUND(COUNT(DISTINCT semana)::NUMERIC / 14 * 100, 1) AS pct_avance,
  SUM(CASE WHEN hti_done       THEN 1 ELSE 0 END) AS htis_entregadas,
  SUM(CASE WHEN activity_done  THEN 1 ELSE 0 END) AS actividades_completadas,
  MAX(updated_at)                           AS ultima_actividad
FROM student_progress
GROUP BY student_name, student_id
ORDER BY xp_total DESC;

-- ══════════════════════════════════════════════════════════
--  Verificar instalación
-- ══════════════════════════════════════════════════════════
SELECT 'Tabla student_progress creada correctamente ✅' AS mensaje;
SELECT 'Vista resumen_docente lista ✅' AS mensaje;
