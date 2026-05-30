# NeuroBiz S.A.S. — Contexto del Caso Estudio
## Módulo TGA04 · Fundamentos de Computación para los Negocios
### Institución Universitaria de Barranquilla (UIB) · 2026

---

## 1. ¿QUIÉN ES NEUROBIZ S.A.S.?

**NeuroBiz S.A.S.** es una empresa colombiana de servicios especializados en neurodivergencia, con sede en Barranquilla (Atlántico). Fundada en 2019, ofrece:

| Servicio | Descripción | Duración estándar | Costo por sesión |
|----------|-------------|-------------------|------------------|
| Evaluación diagnóstica | Proceso de evaluación neuropsicológica | 4 sesiones de 60 min | $180.000 COP |
| Terapia individual | Sesiones personalizadas (fonoaudiología, TO, psicología) | 45 min | $95.000 COP |
| Terapia grupal | Sesiones de 4-6 personas con condición similar | 60 min | $55.000 COP |
| Psicoeducación familias | Talleres para padres/cuidadores | 90 min | $70.000 COP |
| Coaching laboral | Apoyo a adultos en entorno laboral | 60 min | $110.000 COP |
| Sensibilización empresarial | Talleres para empleadores/instituciones | 120 min | $350.000 COP (grupo) |

**Equipo:** 8 terapeutas (3 psicólogos, 2 fonoaudiólogos, 2 terapeutas ocupacionales, 1 neuropsicólogo).

**Condiciones que atiende:**
- TEA — Trastorno del Espectro Autista
- TDAH — Trastorno por Déficit de Atención e Hiperactividad
- TDA — Déficit de Atención sin hiperactividad
- Dislexia
- Discalculia
- ACCC — Altas Capacidades Cognitivas y Creativas
- Dispraxia / Trastorno del Desarrollo de la Coordinación

---

## 2. EL CONTRATO UIB–NEUROBIZ

### 2.1 Contexto del convenio

La **Institución Universitaria de Barranquilla (UIB)** firmó en enero de 2026 un contrato de prestación de servicios con NeuroBiz S.A.S. El contrato surge tras identificar que un porcentaje significativo del estudiantado de UIB presenta condiciones de neurodivergencia no diagnosticadas o sin acompañamiento, lo que impacta su rendimiento académico y bienestar.

> **Tipo de contrato:** Prestación de servicios · **Vigencia:** Enero–Diciembre 2026  
> **Valor mensual:** $12.500.000 COP (hasta 150 sesiones mensuales)  
> **Costo por sesión contratada:** $83.333 COP promedio

### 2.2 Servicios incluidos en el contrato

| Servicio | Sesiones/mes contratadas | Costo unitario |
|----------|--------------------------|----------------|
| Evaluación diagnóstica | 10 procesos (40 sesiones) | $180.000/sesión |
| Terapia individual | 80 sesiones | $95.000/sesión |
| Psicoeducación | 8 talleres | $70.000/taller |
| Sensibilización docente | 2 talleres | $350.000/taller |
| Coaching laboral (personal UIB) | 8 sesiones | $110.000/sesión |

### 2.3 Dos perspectivas: PROVEEDOR vs CLIENTE

Esta dualidad será la base de los ejercicios algorítmicos del módulo:

---

#### 🏢 PERSPECTIVA NEUROBIZ (PROVEEDOR de servicios)

NeuroBiz debe responder preguntas como:
- ¿Cuántas sesiones realicé este mes para UIB?
- ¿Cuál es la tasa de ocupación de cada terapeuta?
- ¿El costo por sesión se mantiene dentro del rango contratado?
- ¿Qué terapeuta tiene mayor índice de satisfacción de estudiantes UIB?
- ¿Se están cumpliendo los indicadores de calidad del servicio?

**Indicadores internos de NeuroBiz:**

| # | Indicador | Fórmula | Umbral aceptable |
|---|-----------|---------|-----------------|
| N1 | Tasa de ocupación del terapeuta | (Sesiones realizadas / Sesiones disponibles) × 100 | ≥ 75% |
| N2 | Índice de satisfacción del paciente | (Encuestas "satisfecho" o "muy satisfecho" / Total encuestas) × 100 | ≥ 85% |
| N3 | Tiempo promedio de sesión | Σ(tiempo real de sesión) / n° sesiones | 40–65 min |
| N4 | Tasa de ausentismo | (Sesiones canceladas por paciente / Sesiones programadas) × 100 | ≤ 15% |
| N5 | Tasa de cancelación tardía | (Cancelaciones < 24h / Total sesiones programadas) × 100 | ≤ 10% |
| N6 | Costo por sesión ejecutado | Costos operativos del mes / n° sesiones realizadas | ≤ $95.000 |
| N7 | Índice de retención | (Pacientes activos mes actual / Pacientes iniciales del mes) × 100 | ≥ 80% |
| N8 | Eficiencia diagnóstica | (Diagnósticos entregados en tiempo / Total diagnósticos iniciados) × 100 | ≥ 90% |

---

#### 🎓 PERSPECTIVA UIB (CLIENTE de servicios)

UIB debe responder preguntas como:
- ¿Cuántos estudiantes recibieron atención este mes?
- ¿Cuánto costó el servicio por estudiante?
- ¿Se están usando las 150 sesiones contratadas?
- ¿Hay mejora académica en los estudiantes atendidos?
- ¿El contrato está siendo rentable para UIB?

**Indicadores de seguimiento de UIB:**

| # | Indicador | Fórmula | Umbral aceptable |
|---|-----------|---------|-----------------|
| U1 | Tasa de uso del contrato | (Sesiones usadas / Sesiones contratadas) × 100 | ≥ 80% |
| U2 | Costo por estudiante atendido | Total pagado a NeuroBiz / n° estudiantes únicos atendidos | Monitoreo |
| U3 | Tasa de mejora académica | (Estudiantes con mejora de nota ≥ 0.5 / Total estudiantes atendidos) × 100 | ≥ 60% |
| U4 | Porcentaje de diagnósticos nuevos | (Diagnósticos nuevos / Total estudiantes evaluados) × 100 | Monitoreo |
| U5 | Sesiones ejecutadas vs contratadas | Sesiones reales / Sesiones contratadas | ≥ 0.80 |
| U6 | Índice de satisfacción UIB | (Estudiantes satisfechos con NeuroBiz / Total encuestados UIB) × 100 | ≥ 85% |
| U7 | Tasa de deserción post-intervención | (Estudiantes que abandonaron carrera / Total intervenidos) × 100 | ≤ 5% |

---

## 3. DATOS SIMULADOS DEL MES DE FEBRERO 2026 (Referencia para talleres)

### 3.1 Terapeutas NeuroBiz

| ID | Nombre | Especialidad | Sesiones disponibles/mes | Sesiones realizadas | Canceladas | Satisfacción (1-5) |
|----|--------|-------------|--------------------------|---------------------|------------|--------------------|
| T01 | Ana Ramos | Psicología | 80 | 68 | 9 | 4.7 |
| T02 | Carlos Mejía | Fonoaudiología | 72 | 71 | 2 | 4.9 |
| T03 | Luz Torres | Terapia Ocupacional | 72 | 54 | 14 | 4.2 |
| T04 | Mario Suárez | Psicología | 80 | 77 | 4 | 4.8 |
| T05 | Paula Vega | Neuropsicología | 60 | 58 | 1 | 5.0 |
| T06 | Diego Ríos | Fonoaudiología | 72 | 43 | 22 | 3.9 |
| T07 | Sandra Ospina | Terapia Ocupacional | 72 | 69 | 5 | 4.6 |
| T08 | Héctor Niño | Psicología | 80 | 80 | 0 | 4.8 |

### 3.2 Estudiantes UIB atendidos en Febrero 2026

| ID | Programa | Condición | Sesiones en Feb | Tipo servicio | Promedio académico antes | Promedio académico después |
|----|----------|-----------|-----------------|---------------|--------------------------|---------------------------|
| E001 | TGA | TDAH | 4 | Terapia individual | 3.1 | 3.7 |
| E002 | Contaduría | Dislexia | 3 | Terapia individual | 2.9 | 3.2 |
| E003 | TGA | TEA-L1 | 6 | Terapia individual | 3.8 | 4.1 |
| E004 | Administración | TDA | 2 | Coaching | 2.7 | 2.9 |
| E005 | Sistemas | ACCC | 4 | Coaching | 4.2 | 4.5 |
| E006 | TGA | TDAH | 5 | Terapia individual | 2.5 | 3.0 |
| E007 | Derecho | Discalculia | 3 | Terapia individual | 3.0 | 3.0 |
| E008 | Psicología | Dislexia | 4 | Terapia individual | 3.4 | 3.8 |
| E009 | Ingeniería | TDAH | 3 | Terapia individual | 3.2 | 3.6 |
| E010 | TGA | TEA-L1 | 2 | Evaluación | 3.9 | 3.9 |
| E011 | Contaduría | TDA | 4 | Terapia grupal | 2.8 | 3.1 |
| E012 | Administración | ACCC | 3 | Coaching | 4.0 | 4.3 |

**Costo total facturado a UIB en Febrero 2026:** $11.840.000 COP  
**Sesiones contratadas:** 150 | **Sesiones ejecutadas:** 142

---

## 4. ACTIVIDADES DEL MÓDULO CON DOBLE PERSPECTIVA

| Semana | Contenido | Ejercicio desde NeuroBiz | Ejercicio desde UIB |
|--------|-----------|--------------------------|---------------------|
| 2 | Variables y operadores | Calcular N1, N6 para T01 | Calcular U1, U2 del mes |
| 3 | Diagramas de flujo | Flujo de cálculo de N2 | Flujo de cálculo de U3 |
| 4 | Operadores estadísticos | Promedio, máximo N1 de todos los terapeutas | Costo promedio por estudiante |
| 6-7 | Selectivas | Si N4 > 15%, generar alerta | Si U3 < 60%, notificar a rectoría |
| 8 | Decisión múltiple | Según condición del paciente, asignar terapeuta | Según programa académico, determinar tipo de intervención |
| 9-10 | Ciclos | Procesar todos los terapeutas del mes | Procesar todos los estudiantes UIB del mes |
| 12-13 | Python IDE | Sistema completo NeuroBiz en Python | Reporte mensual UIB en Python |

---

## 5. GLOSARIO ORGANIZACIONAL

| Término | Definición |
|---------|-----------|
| **Sesión** | Una cita de terapia/coaching entre un terapeuta y un paciente/estudiante |
| **Sesión disponible** | Espacio en la agenda del terapeuta, con o sin paciente asignado |
| **Cancelación tardía** | Cancelada con menos de 24 horas de anticipación |
| **Terapia individual** | Una persona + un terapeuta |
| **Terapia grupal** | 4 a 6 personas + un terapeuta |
| **Contrato UIB** | El convenio de prestación de servicios entre UIB y NeuroBiz |
| **Sesión contratada** | Sesión incluida en el cupo mensual pagado por UIB |
| **Mejora académica** | Incremento de 0.5 o más en el promedio del estudiante entre semestres |
| **PROVEEDOR** | NeuroBiz (quien presta el servicio) |
| **CLIENTE** | UIB (quien paga y recibe el servicio para sus estudiantes) |

---

*Archivo base para el módulo TGA04 · Fundamentos de Computación para los Negocios · UIB 2026*
