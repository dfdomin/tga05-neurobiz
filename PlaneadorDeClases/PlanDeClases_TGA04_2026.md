# PLANEADOR DE CLASES
## TGA04 — Fundamentos de Computación para los Negocios
**Programa:** Tecnología en Gestión Administrativa  
**Nivel:** Pregrado | **Créditos:** 2 | **Total horas:** 117 (2 HAD + 2 HP + 5 HTI semanales)  
**Docente:** __________________ | **Período:** 2026  
**Lenguaje de programación:** Python 3.x  
**Herramientas:** PSeInt (semanas 1–4, pseudocódigo), Python en Thonny IDE (semanas 5–13), draw.io (diagramas de flujo), ClassDojo (gamificación), Quizizz modo Playground/Wayground  
**Formato de sesión:** HAD (2h) + HP (2h) el **mismo día**, 4 horas continuas con pausa entre bloques de al menos 10 minutos. El docente tiene ACCC — requiere agenda exacta escrita visible, sin improvisaciones, pausas de voz cada 20–25 min.  
**RA evaluado (rúbrica institucional):** RA3 — Aplicar el pensamiento crítico y la habilidad para resolver problemas de la empresa, teniendo en cuenta las variables que hacen parte de los diferentes contextos, con el fin de lograr el mejoramiento continuo del proceso.

---

## CONTRATO NeuroBiz S.A.S. ↔ UIB: Marco de Doble Perspectiva

> 🏢 **NeuroBiz S.A.S.** (PROVEEDOR) firmó un contrato anual con la **Institución Universitaria de Barranquilla — UIB** (CLIENTE) para proveer servicios de acompañamiento terapéutico a estudiantes universitarios con condiciones de neurodivergencia.

### Datos del contrato (caso transversal del curso):
| Campo | Valor |
|-------|-------|
| Tipo de servicio | Terapia psicológica y psicopedagógica individualizada |
| Duración del contrato | Enero–Diciembre 2026 |
| Sesiones contratadas/mes | 150 sesiones (UIB paga anticipado por este bloque) |
| Costo por sesión | $83.380 COP |
| Valor mensual contrato | $12.507.000 COP |
| Pago real (febrero 2026) | $11.840.000 COP (142 sesiones usadas) |
| Estudiantes UIB cubiertos | 12 estudiantes activos (mes de análisis: febrero 2026) |
| Terapeutas asignados | 8 (T01–T08) |

### Las dos miradas sobre el mismo dato:
| Indicador | Vista PROVEEDOR (NeuroBiz) | Vista CLIENTE (UIB) |
|-----------|--------------------------|---------------------|
| 142 sesiones realizadas | N1-T06 = 59.7% → 🔴 bajo rendimiento del terapeuta | U1 = 94.7% → ✅ casi todas las sesiones fueron usadas |
| $11.840.000 pagados | Ingreso del mes | Costo total del servicio |
| 2 estudiantes mejoraron | NeuroBiz analiza eficacia por terapeuta | U3 = 16.7% → 🔴 baja mejora académica entre estudiantes |
| T06: 30.56% cancelación | N4-T06 → 🔴 muy por encima del límite (15%) | Riesgo de incumplimiento contractual |

> 💡 **Ejercicio permanente del curso:** ¿Quién tiene razón? ¿Cómo el mismo número cuenta historias distintas según quién lo analice? Esto es pensamiento crítico con datos reales.

---

## CASO ESTUDIO TRANSVERSAL: NeuroBiz S.A.S.

**NeuroBiz S.A.S.** es una empresa colombiana que ofrece servicios de diagnóstico, acompañamiento y entrenamiento para personas con condiciones de neurodivergencia (TEA, TDAH, dislexia, discalculia). Provee:
- Terapias individuales y grupales (psicología, fonoaudiología, terapia ocupacional)
- Programas de sensibilización para empleadores
- Talleres psicoeducativos para familias

### Indicadores de Gestión Organizacional de NeuroBiz S.A.S.

| # | Indicador | Fórmula | Tipo de Variable |
|---|-----------|---------|-----------------|
| 1 | Tasa de ocupación de terapeutas | (Sesiones realizadas / Sesiones disponibles) × 100 | Numérica |
| 2 | Índice de satisfacción del paciente | (Pacientes satisfechos / Total encuestados) × 100 | Numérica |
| 3 | Tiempo promedio de atención | Total horas sesión / Número de sesiones | Numérica |
| 4 | Tasa de ausentismo | (Sesiones canceladas / Sesiones programadas) × 100 | Numérica |
| 5 | Eficiencia diagnóstica | (Diagnósticos en tiempo / Total diagnósticos) × 100 | Numérica |
| 6 | Costo por sesión | Costos operativos / Número de sesiones | Numérica |
| 7 | Índice de retención de pacientes | (Pacientes activos mes actual / Pacientes iniciales) × 100 | Numérica |
| 8 | Nombre del terapeuta asignado | — | Alfanumérica |
| 9 | Tipo de condición atendida | TEA / TDAH / Dislexia / Discalculia / Otro | Alfanumérica |
| 10 | ¿Alcanzó meta mensual? | Sí / No | Lógica |

---

## ESTRUCTURA DE EVALUACIÓN

| Corte | Semanas | Peso | Evidencia principal |
|-------|---------|------|-------------------|
| Primer corte | 1–5 | 35% | Taller + Primer Parcial (Sem. 5) |
| Segundo corte | 6–10 | 35% | Talleres + Caso Estudio + Segundo Parcial (Sem. 10) |
| Tercer corte | 11–14 | 30% | Laboratorio + Evaluación Final (Sem. 14) |

---

## PLANEADOR SEMANAL

---

### ─── CORTE 1: SEMANAS 1–5 ───
**Objetivo del corte:** Identificar variables y operaciones para la solución de problemas organizacionales (RA1 del microcurrículo).

---

#### SEMANA 1 — Bienvenida, Diagnóstico y Contexto Empresarial

| Campo | Detalle |
|-------|---------|
| **RA microcurrículo** | RA1 |
| **Criterios evaluación (rúbrica RA3)** | Identifica las variables significativas del problema |
| **Contenidos** | Conceptos de Dato, Información, Software, Sistemas de Información. Introducción a los algoritmos. Algoritmos de la vida organizacional. |
| **Actividades HAD** | 1. Prueba diagnóstica (10 min). 2. Presentación del caso estudio NeuroBiz: contextualización del negocio, servicios y problemáticas reales. 3. Discusión guiada: ¿qué datos maneja una empresa de salud? |
| **Actividades HP** | Laboratorio en sala: exploración del entorno de trabajo (PSeInt o equivalente). Identificar datos de NeuroBiz: tipos de información que genera la empresa. |
| **Tareas HTI** | Investigar qué son los indicadores de gestión y traer 3 ejemplos de empresas de salud. |
| **Recursos** | Videoproyector, computadores, aula virtual, ficha diagnóstica impresa. |
| **Evaluación** | Participación oral y diagnóstica (formativa, no calificada). |

---

#### SEMANA 2 — Variables y Operadores con Indicadores de NeuroBiz

| Campo | Detalle |
|-------|---------|
| **RA microcurrículo** | RA1 |
| **Criterios evaluación (rúbrica RA3)** | Identifica las variables significativas del problema y las describe de manera estructurada |
| **Contenidos** | Tipos de variables: numéricas, alfanuméricas, lógicas. Operadores: matemáticos, relacionales, lógicos y estadísticos. Notación algorítmica: pseudocódigo básico. |
| **Actividades HAD** | 1. Clase magistral con ejemplos de variables tomados de los 10 indicadores de NeuroBiz. 2. Mesa redonda: ¿qué tipo de variable es cada indicador de NeuroBiz? Justificación grupal. |
| **Actividades HP** | Taller práctico: declarar variables y calcular los indicadores #1, #3 y #6 de NeuroBiz usando pseudocódigo (Inicio–Fin, entrada, operación, salida). |
| **Tareas HTI** | Completar el taller: calcular también los indicadores #2, #4 y #7 con datos ficticios de NeuroBiz. |
| **Recursos** | Guía de trabajo, computadores, aula virtual, software PSeInt. |
| **Evaluación** | Revisión del taller en clase siguiente (formativa). |

---

#### SEMANA 3 — Representación Algorítmica: Diagramas de Flujo

| Campo | Detalle |
|-------|---------|
| **RA microcurrículo** | RA1 |
| **Criterios evaluación (rúbrica RA3)** | Identifica de manera precisa y completa las variables; describe usando herramientas de mejora continua |
| **Contenidos** | Diagrama de flujo: símbolos estándar. Primitivas inicio-fin, entrada/salida. Representación de operaciones con variables numéricas. |
| **Actividades HAD** | 1. Presentación de simbología de diagramas de flujo. 2. Demostración: diagrama para calcular la "Tasa de ocupación de terapeutas" de NeuroBiz. 3. Preguntas intercaladas sobre el proceso de construcción. |
| **Actividades HP** | Taller: construir diagrama de flujo para calcular el "Índice de satisfacción" (#2) y la "Tasa de ausentismo" (#4) con datos que el docente suministra de NeuroBiz. |
| **Tareas HTI** | Crear diagrama de flujo para el indicador "Costo por sesión" (#6) e "Índice de retención" (#7). Subir al aula virtual. |
| **Recursos** | Software de diagramas (draw.io, PSeInt), guía de trabajo. |
| **Evaluación** | Taller entregado en aula virtual (formativa). |

---

#### SEMANA 4 — Operadores Estadísticos y Consolidación RA1

| Campo | Detalle |
|-------|---------|
| **RA microcurrículo** | RA1 |
| **Criterios evaluación (rúbrica RA3)** | Formula problemas complejos teniendo en cuenta variables y objetivos medibles |
| **Contenidos** | Operadores estadísticos (promedio, máximo, mínimo, conteo). Integración de operadores en pseudocódigo y diagramas de flujo. |
| **Actividades HAD** | 1. Exposición oral del docente: uso de estadísticos para analizar indicadores organizacionales. 2. Ejercicio en equipo: dado un reporte mensual de NeuroBiz (datos del docente), identificar qué operadores se necesitan para analizar los 10 indicadores. |
| **Actividades HP** | Laboratorio: elaborar algoritmo completo (pseudocódigo + diagrama) para calcular el promedio mensual de la "Tasa de ocupación" y determinar si NeuroBiz cumplió su meta (variable lógica). |
| **Tareas HTI** | Preparar para el parcial: resolver un caso de práctica completo publicado en el aula virtual (empresa diferente a NeuroBiz para calibrar comprensión). |
| **Recursos** | Aula virtual, computadores, ejercicio de práctica impreso. |
| **Evaluación** | Ejercicio de laboratorio (formativa); retroalimentación antes del parcial. |

---

#### SEMANA 5 — PRIMER PARCIAL ✏️

| Campo | Detalle |
|-------|---------|
| **Contenido evaluado** | RA1 completo: variables, operadores, pseudocódigo y diagramas de flujo aplicados a indicadores organizacionales. |
| **Instrumento** | Examen escrito/computador: análisis de un caso empresarial (empresa diferente a NeuroBiz) donde el estudiante debe: identificar tipos de variables, seleccionar operadores, construir pseudocódigo y/o diagrama de flujo. |
| **Criterios de evaluación (rúbrica RA3)** | • Identifica variables significativas (30%) • Formula el problema con variables y objetivos medibles (40%) • Diseña la solución algorítmica con estructura y pertinencia (30%) |
| **Peso** | 35% del corte 1 → 12.25% de la nota total |

---

### ─── CORTE 2: SEMANAS 6–10 ───
**Objetivo del corte:** Formular soluciones algorítmicas con estructuras de control aplicadas a indicadores de gestión de NeuroBiz (RA2 del microcurrículo). **El segundo parcial se diseña como un caso estudio alineado directamente a la rúbrica RA3 institucional.**

---

#### SEMANA 6 — Primitiva Selectiva: SI / FSI

| Campo | Detalle |
|-------|---------|
| **RA microcurrículo** | RA2 |
| **Criterios evaluación (rúbrica RA3)** | Identifica variables; formula problemas complejos con condicionales |
| **Contenidos** | Primitiva selectiva simple: SI–FSI. Primitiva Inicio–Fin. Primitivas de Entrada/Salida. Análisis de condición lógica. |
| **Actividades HAD** | 1. Introducción a primitivas selectivas con diagrama y pseudocódigo. 2. Problema motivador: NeuroBiz quiere saber si un terapeuta "cumplió meta" según su tasa de ocupación. Construcción en clase. |
| **Actividades HP** | Taller: algoritmo que lee la tasa de ausentismo semanal de NeuroBiz y emite un mensaje de alerta si supera el 20%. Representación en pseudocódigo y diagrama. |
| **Tareas HTI** | Diseñar algoritmo que evalúe si el "Índice de satisfacción" de NeuroBiz está por encima del umbral (85%) y genere recomendación. |
| **Recursos** | PSeInt, guía de trabajo, datos simulados de NeuroBiz. |
| **Evaluación** | Revisión de tarea (formativa). |

---

#### SEMANA 7 — Primitiva Selectiva Doble: SI–SINO–FSI

| Campo | Detalle |
|-------|---------|
| **RA microcurrículo** | RA2 |
| **Criterios evaluación (rúbrica RA3)** | Formula problemas complejos con pertinencia y rigurosidad |
| **Contenidos** | Primitiva selectiva doble: SI–SINO–FSI. Uso de operadores lógicos (Y, O, NO) en condiciones compuestas. |
| **Actividades HAD** | 1. Clase magistral: estructura SI-SINO-FSI, diferencias con SI-FSI. 2. Caso NeuroBiz: clasificar a un paciente como "prioritario", "regular" o "sin urgencia" según dos indicadores simultáneos (tiempo de espera + diagnóstico confirmado). |
| **Actividades HP** | Taller: algoritmo que recibe la tasa de ocupación y el costo por sesión; clasifica el estado operativo de un terapeuta como: "Eficiente", "En riesgo" o "Crítico". |
| **Tareas HTI** | Extender el algoritmo anterior para manejar 3 terapeutas e imprimir el resumen de cada uno. |
| **Recursos** | PSeInt, aula virtual. |
| **Evaluación** | Taller entregado al inicio de la siguiente clase (formativa). |

---

#### SEMANA 8 — Primitiva de Decisión Múltiple: DD–FDD

| Campo | Detalle |
|-------|---------|
| **RA microcurrículo** | RA2 |
| **Criterios evaluación (rúbrica RA3)** | Diseña la solución a través de modelos con estructura y pertinencia |
| **Contenidos** | Doble decisión / decisión múltiple (DD–FDD). Comparación con estructura SI–SINO anidada. Casos de uso en contexto empresarial. |
| **Actividades HAD** | 1. Presentación de la primitiva DD-FDD. 2. Caso NeuroBiz: según el tipo de condición del paciente (TEA / TDAH / Dislexia / Discalculia / Otro), el sistema asigna el tipo de terapeuta recomendado y la duración estándar de sesión. |
| **Actividades HP** | Laboratorio: construir el algoritmo anterior en PSeInt con menú interactivo. Ejecutar con al menos 5 casos de prueba de NeuroBiz. |
| **Tareas HTI** | Agregar al algoritmo que, según el diagnóstico, también calcule el costo mensual estimado del paciente. |
| **Recursos** | PSeInt, computadores. |
| **Evaluación** | Revisión de laboratorio (formativa). |

---

#### SEMANA 9 — Primitivas Repetitivas: MQ–FMQ y HH–FHH

| Campo | Detalle |
|-------|---------|
| **RA microcurrículo** | RA2 |
| **Criterios evaluación (rúbrica RA3)** | Formula y diseña soluciones algorítmicas para problemas organizacionales complejos |
| **Contenidos** | Primitiva repetitiva mientras-que (MQ–FMQ). Primitiva haga-hasta (HH–FHH). Diferencias y criterios de selección. |
| **Actividades HAD** | 1. Explicación con analogías del negocio: "procesar todas las sesiones del mes hasta que no haya más". 2. Caso NeuroBiz: calcular el total de sesiones realizadas en el mes y el promedio de satisfacción, usando un ciclo que lee sesión por sesión hasta que el usuario ingrese -1. |
| **Actividades HP** | Taller: usando HH–FHH, construir un algoritmo que acumule el ingreso total mensual de NeuroBiz sesión por sesión y al terminar muestre: total, promedio, sesión más costosa y si superó la meta mensual. |
| **Tareas HTI** | Preparar borrador del caso estudio para el parcial: identificar variables, indicadores involucrados y estructura del algoritmo. |
| **Recursos** | PSeInt, guía de trabajo. |
| **Evaluación** | Avance del caso estudio (retroalimentación docente antes del parcial). |

---

#### SEMANA 10 — SEGUNDO PARCIAL: CASO ESTUDIO NeuroBiz ✏️

| Campo | Detalle |
|-------|---------|
| **Descripción** | Evaluación tipo caso estudio alineada a la rúbrica RA3 institucional. El estudiante recibe el contexto completo de NeuroBiz para un mes de operación (datos de terapeutas, sesiones, costos, ausentismo) y debe resolver un problema organizacional usando todo lo aprendido. |
| **Enunciado síntesis** | *"NeuroBiz S.A.S. requiere un sistema algorítmico que procese la información mensual de sus terapeutas. Para cada terapeuta: calcule su tasa de ocupación, costo por sesión e índice de satisfacción; clasifique su desempeño como Sobresaliente / Bueno / En riesgo / Crítico según rangos definidos; y al final emita un reporte con el promedio general, el terapeuta con mejor desempeño y si la empresa en conjunto alcanzó su meta de satisfacción."* |
| **Criterios evaluación (rúbrica RA3)** | • **Identifica variables y herramientas de mejora continua** (25%) — Declara correctamente todas las variables, los indicadores y describe la lógica del proceso. • **Formula el problema con variables medibles y alcanzables** (35%) — El pseudocódigo/diagrama es claro, pertinente y riguroso. • **Diseña la solución con estructura y pertinencia** (40%) — Algoritmo completo, funcional, estructurado y pertinente al contexto. |
| **Formato** | Entrega escrita + archivo PSeInt. |
| **Peso** | 35% del corte 2 → 12.25% de la nota total |

---

### ─── CORTE 3: SEMANAS 11–14 ───
**Objetivo del corte:** Verificar soluciones mediante pruebas de escritorio y codificar algoritmos en lenguaje de alto nivel (RA3, RA4, RA5 del microcurrículo).

---

#### SEMANA 11 — Primitiva PARA–FPARA y Pruebas de Escritorio

| Campo | Detalle |
|-------|---------|
| **RA microcurrículo** | RA2 + RA3 |
| **Criterios evaluación (rúbrica RA3)** | Identifica el estado de variables en cada paso de la solución algorítmica |
| **Contenidos** | Primitiva PARA–FPARA (contador). Pruebas de escritorio: traza de variables, detectar errores lógicos. |
| **Actividades HAD** | 1. Introducción al PARA-FPARA con ejemplo de "procesar N terapeutas de NeuroBiz". 2. Demostración de prueba de escritorio paso a paso sobre el algoritmo del segundo parcial (feedback colectivo). |
| **Actividades HP** | Taller: dado un algoritmo de NeuroBiz con errores lógicos deliberados, realizar la prueba de escritorio y corregir los errores. |
| **Tareas HTI** | Trasladar el algoritmo corregido a pseudocódigo limpio listo para codificar la siguiente semana. |
| **Recursos** | Plantilla impresa de prueba de escritorio, PSeInt. |
| **Evaluación** | Entrega del taller de prueba de escritorio (calificado, 20% del corte 3). |

---

#### SEMANA 12 — Codificación en IDE: Variables y Selectivas

| Campo | Detalle |
|-------|---------|
| **RA microcurrículo** | RA4 |
| **Criterios evaluación (rúbrica RA3)** | Diseña la solución con estructura pertinente |
| **Contenidos** | Entornos Integrados de Desarrollo (IDE). Codificación de variables, entrada/salida. Codificación de estructuras selectivas en lenguaje de alto nivel (Python o Java, según decisión docente). |
| **Actividades HAD** | 1. Presentación del IDE (instalación, interfaz, primer programa "Hola NeuroBiz"). 2. Paralelo pseudocódigo–código: traducir un algoritmo de variables e indicadores de NeuroBiz al lenguaje de alto nivel seleccionado. |
| **Actividades HP** | Laboratorio: codificar el algoritmo de clasificación de terapeutas (semana 8) en el IDE. Ejecutar con datos reales de prueba. |
| **Tareas HTI** | Agregar los ciclos (PARA o equivalente) para procesar 5 terapeutas en el mismo programa. |
| **Recursos** | Computadores con IDE instalado (Python/Java), sala de cómputo. |
| **Evaluación** | Avance de laboratorio (formativa). |

---

#### SEMANA 13 — Codificación Completa y Depuración (Última Clase)

| Campo | Detalle |
|-------|---------|
| **RA microcurrículo** | RA4 + RA5 |
| **Criterios evaluación (rúbrica RA3)** | Diseña e implementa la solución completa; identifica y corrige fallas |
| **Contenidos** | Codificación de primitivas repetitivas en IDE. Depuración (debugging): identificar errores de sintaxis y lógica. Modo de ejecución paso a paso. |
| **Actividades HAD** | 1. Mesa redonda de cierre: ¿qué aprendimos con NeuroBiz?, ¿cómo la computación apoya la neurodivergencia? 2. Entrega y explicación del enunciado de la evaluación final. |
| **Actividades HP** | Laboratorio integrador: dado un programa de NeuroBiz con errores (sintaxis + lógica), depurarlo en el IDE, corregirlo y ejecutarlo satisfactoriamente. |
| **Tareas HTI** | Preparación evaluación final: repasar todos los algoritmos, pruebas de escritorio y codificación del caso NeuroBiz. |
| **Recursos** | IDE, computadores, lista de chequeo de depuración. |
| **Evaluación** | Entrega del laboratorio integrador (calificado, 30% del corte 3). |

---

#### SEMANA 14 — EVALUACIÓN FINAL 🎓

| Campo | Detalle |
|-------|---------|
| **Descripción** | Evaluación sumativa integradora del ciclo completo: algoritmo → prueba de escritorio → codificación → depuración, aplicado al caso NeuroBiz. |
| **Enunciado síntesis** | *"NeuroBiz S.A.S. requiere un programa funcional que procese la información de un trimestre de operación (3 meses, N terapeutas por mes). El programa debe: calcular todos los indicadores de gestión, clasificar el desempeño por terapeuta, identificar el mejor y peor mes de la empresa, y generar un reporte de alerta si algún indicador supera los umbrales críticos definidos."* |
| **Estructura de entrega** | 1. Pseudocódigo o diagrama de flujo (análisis del problema). 2. Prueba de escritorio con datos de ejemplo. 3. Programa codificado y funcional en IDE. |
| **Criterios evaluación (rúbrica RA3)** | • **Identifica variables y herramientas** (25%) • **Formula el problema** (35%) • **Diseña e implementa la solución** (40%) |
| **Peso** | 50% del corte 3 → 15% de la nota total |

---

## RESUMEN DE ACTIVIDADES EVALUATIVAS

| Semana | Actividad | Corte | % Corte | % Total |
|--------|-----------|-------|---------|---------|
| 1–4 | Talleres formativos + participación | 1 | 65% | 22.75% |
| 5 | Primer Parcial | 1 | 35% | 12.25% |
| 6–9 | Talleres + avance caso estudio | 2 | 65% | 22.75% |
| 10 | Segundo Parcial (Caso Estudio NeuroBiz) | 2 | 35% | 12.25% |
| 11 | Taller prueba de escritorio | 3 | 20% | 6% |
| 13 | Laboratorio integrador (depuración) | 3 | 30% | 9% |
| 14 | Evaluación Final | 3 | 50% | 15% |
| **TOTAL** | | | | **100%** |

---

## ALINEACIÓN: CONTENIDO → CASO ESTUDIO → RÚBRICA RA3

| Semana | Contenido | Aplicación NeuroBiz | Criterio rúbrica |
|--------|-----------|--------------------|--------------------|
| 1 | Datos e información | Identificar datos que genera NeuroBiz | Identifica variables significativas |
| 2–3 | Variables y operadores | Calcular indicadores de gestión (#1–#10) | Identifica y describe variables estructuradamente |
| 4 | Estadísticos + consolidación | Promedio, máximo, análisis mensual | Formula problemas con objetivos medibles |
| 6–7 | Selectivas simples y dobles | Alertas y clasificación de terapeutas | Formula y diseña con pertinencia y rigurosidad |
| 8 | Decisión múltiple | Asignación por tipo de condición atendida | Diseña solución estructurada |
| 9 | Ciclos MQ / HH | Procesamiento mensual acumulativo | Diseña solución integral |
| 10 | **Caso Estudio (parcial)** | **Problema complejo multivariable** | **Los 3 criterios rúbrica RA3** |
| 11 | Prueba de escritorio | Verificar algoritmos de NeuroBiz | Identifica estado de variables paso a paso |
| 12–13 | IDE + debugging | Codificar y depurar sistema NeuroBiz | Diseña e implementa solución funcional |
| 14 | **Evaluación Final** | **Sistema trimestral NeuroBiz** | **Los 3 criterios rúbrica RA3** |

---

## BIBLIOGRAFÍA

| Tipo | Referencia |
|------|-----------|
| Básica | Cairó Battistutti, O. & Guardati Bueno, S. *Metodología de la programación: algoritmos, diagramas de flujo y programas*. Alfaomega. 3ª ed. ISBN: 9789586827492 |
| Básica | Deitel, H. & Deitel, P. *Cómo programar en Java*. Pearson. 5ª ed. ISBN: 9789702605188 |
| Básica | Joyanes Aguilar, L. *Fundamentos de programación: algoritmos, estructura de datos y objetos*. McGraw-Hill. 3ª ed. ISBN: 9786071508188 |
| Complementaria | Moreno Pérez, J.C. *Programación*. RA-MA Editorial. ISBN: 9788499640884 |
| Web | Estructuras Algorítmicas: http://webdelprofesor.ula.ve/nucleotrujillo/frank_delgadillo/file/estructura_algoritmicas.pdf |

---

*Documento generado con GitHub Copilot CLI — Mayo 2026*
