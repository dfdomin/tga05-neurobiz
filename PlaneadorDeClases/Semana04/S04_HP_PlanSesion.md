# S04 HP — Plan de Sesión de Laboratorio
## TGA04 Fundamentos de Computación para los Negocios · UIB

**Semana:** 4  
**Modalidad:** HP · Bloque 2 de 2 (mismo día que HAD; inicia después del descanso) (laboratorio)  
**Duración:** 120 minutos  
**Propósito central:** laboratorio integrador más importante antes del primer parcial  
**Herramientas:** PSeInt, proyector, tablero, ClassDojo, editor de texto como respaldo, calculadora básica  
**Restricción de voz:** alternar demostraciones cortas con trabajo autónomo; no sostener tramos largos de explicación continua.

---

## 1. Resultado esperado del laboratorio
Cada estudiante debe salir con:
1. Un pseudocódigo individual para **4 terapeutas** con N1 y N4.
2. Una versión extendida a **8 terapeutas** con máximos.
3. Un programa para **U3** con 5 estudiantes.
4. Un programa integrador **NeuroBiz + UIB** en una sola secuencia.
5. Una comparación clara entre pseudocódigo y Python.

---

## 2. Protocolo de predictibilidad docente (ACCC)
- Seguir exactamente el orden de actividades 1 → 2 → 3 → 4 → Python → cierre.
- Cada transición se anuncia con: **“Guarden, miren pantalla, cambiamos solo de problema.”**
- Cada actividad termina con un checkpoint visible antes de pasar a la siguiente.
- Si una herramienta falla, usar la contingencia correspondiente sin cambiar el objetivo académico.

---

## 3. Checklist técnico preclase
- [ ] Probar PSeInt en el equipo docente y en al menos 2 equipos del salón.
- [ ] Dejar abierto un archivo `.txt` de respaldo por si PSeInt falla.
- [ ] Escribir en tablero los nombres de los 4 productos del día.
- [ ] Abrir ClassDojo con énfasis en **Entregó actividad, Trabajo en equipo y Curiosidad**.
- [ ] Tener visible la tabla de terapeutas, los N1/N4 precalculados y el resumen UIB de febrero 2026.

---

## 4. Cronograma minuto a minuto

| Tiempo | Actividad | Modo docente | Herramienta | Producto / ClassDojo |
|---|---|---|---|---|
| 00–03 | Entrada, equipos encendidos, agenda proyectada y objetivos del laboratorio. | SILENCIO + HABLA | Proyector | **Puntualidad** a quien inicia sin ayuda. |
| 03–05 | Recordatorio: hoy no se evalúa creatividad del formato sino claridad de la secuencia. | HABLA | Tablero | — |
| 05–10 | **Actividad 1 — demostración (5 min):** mostrar cómo se declaran variables y cómo se lee N1/N4 de un terapeuta. | HABLA | PSeInt | — |
| 10–20 | Estudiantes construyen el programa para 4 terapeutas: lectura secuencial, suma de N1, promedio y reporte. | DESCANSA VOZ | PSeInt | **Entregó actividad** al primer checkpoint. |
| 20–25 | Revisión rápida individual: ejecutar o leer en voz baja cada pseudocódigo. | MONITOREA | PSeInt | **Curiosidad** por quien pregunta cómo verificar el promedio. |
| 25–30 | **Actividad 2 — transición:** explicar extensión a 8 terapeutas y la lógica de máximo N1 / máximo N4. | HABLA | PSeInt + tablero | — |
| 30–40 | Estudiantes agregan terapeutas 5–8 y completan acumuladores. | DESCANSA VOZ | PSeInt | **Entregó actividad** por avance real. |
| 40–50 | Se añade el nombre del terapeuta con mayor N1 y el de mayor N4. | MONITOREA | PSeInt | **Participación** por compartir una solución funcional. |
| 50–55 | **Actividad 3 — demostración corta:** antes/después de 5 estudiantes y fórmula de U3. | HABLA | Tablero + PSeInt | — |
| 55–65 | Trabajo individual: programa U3 con 5 estudiantes, sin ciclos, usando mejoras `despues - antes`. | DESCANSA VOZ | PSeInt | **Entregó actividad** a quien imprime U3. |
| 65–70 | Revisión en parejas: cada estudiante prueba el código del compañero con un caso distinto. | MONITOREA | PSeInt | **Trabajo en equipo** por retroalimentación útil. |
| 70–75 | **Actividad 4 — explicación:** cómo unir la lectura de terapeutas, contrato UIB y resumen ejecutivo en un solo algoritmo. | HABLA | Proyector | — |
| 75–85 | Construcción autónoma del integrador NeuroBiz + UIB. | DESCANSA VOZ | PSeInt | **Entregó actividad** por estructura completa. |
| 85–90 | Checkpoint docente: revisar que el resumen final imprima promedio N1, promedio N4, U1, U2, U3 y recomendación. | MONITOREA | PSeInt | **Curiosidad** a quien mejora el reporte. |
| 90–95 | **Python moment — parte 1:** mostrar lista `n1`, lista `n4` y variables de contrato. | HABLA | Python / proyector | — |
| 95–105 | **Python moment — parte 2:** mostrar `sum()`, `max()`, `min()`, `len()` y comentar similitudes con PSeInt. | HABLA | Python / proyector | **Participación** por identificar equivalencias. |
| 105–110 | Abrir espacio de dudas sobre el parcial: formato, tiempo, qué sí deben dominar. | HABLA | Tablero | — |
| 110–115 | Preguntas frecuentes: promedios, máximo/mínimo, diferencia entre proveedor y cliente. | HABLA | Tablero | **Curiosidad** por pregunta profunda. |
| 115–120 | Verificación final de productos y cierre con recordatorio de estudio. | MONITOREA + HABLA | ClassDojo + aula virtual | **Entregó actividad** y conteo final. |

---

## 5. Actividades con especificación precisa

### Actividad 1 (25 min) — Pseudocódigo individual para 4 terapeutas
**Debe hacer:**
- Leer de forma secuencial `n1_1, n4_1, n1_2, n4_2, n1_3, n4_3, n1_4, n4_4`.
- Acumular los 4 valores de N1.
- Calcular `promedioN1_4` y `promedioN4_4`.
- Imprimir un reporte con títulos claros.

**Demostración docente (solo 5 min):**
```pseint
Proceso Laboratorio_S04_Actividad1
    Definir n1_1, n1_2, n1_3, n1_4 Como Real
    Definir n4_1, n4_2, n4_3, n4_4 Como Real
    Definir sumaN1, sumaN4, promedioN1, promedioN4 Como Real
    sumaN1 <- 0
    sumaN4 <- 0
FinProceso
```

### Actividad 2 (25 min) — Extensión a 8 terapeutas
**Agregar:**
- Lectura secuencial de terapeutas 5 a 8.
- `maxN1`, `nombreMaxN1`.
- `maxN4`, `nombreMaxN4`.
- Reporte final con los máximos.

**Checkpoint obligatorio al minuto 50:** el programa debe mostrar al menos un valor de máximo correctamente.

### Actividad 3 (20 min) — Perspectiva UIB: cálculo de U3
**Leer:** antes y después de 5 estudiantes.  
**Calcular:** mejora individual y cantidad con mejora `>= 0.5`.  
**Imprimir:** `U3 = (mejoran / 5) * 100`.

### Actividad 4 (20 min) — Integrador NeuroBiz + UIB
**Entradas mínimas:**
- 8 valores N1.
- 8 valores N4.
- 150 sesiones contratadas.
- 142 sesiones usadas.
- `$11.840.000` pagados.
- 12 estudiantes atendidos.
- 2 estudiantes con mejora `>= 0.5`.

**Salidas mínimas:**
- Promedio N1.
- Promedio N4.
- U1.
- U2.
- U3.
- Resumen ejecutivo: “Fortaleza operativa” / “Alerta académica”.

### Python moment (15 min)
Mostrar, no exigir digitación completa. El objetivo es que el estudiante vea la equivalencia.

### Wrap-up (15 min)
Resolver dudas sobre:
- formato del parcial,
- duración sugerida de resolución,
- cómo presentar procedimientos,
- qué errores restan más puntos.

---

## 6. Modelo mínimo del integrador esperado
```pseint
Proceso Resumen_NeuroBiz_UIB
    Definir promedioN1, promedioN4, u1, u2, u3 Como Real
    Definir sesionesContratadas, sesionesUsadas, totalPagado, estudiantes, mejoran Como Real
    // Leer n1_1 ... n1_8 y n4_1 ... n4_8
    // Calcular promedios
    sesionesContratadas <- 150
    sesionesUsadas <- 142
    totalPagado <- 11840000
    estudiantes <- 12
    mejoran <- 2
    u1 <- (sesionesUsadas / sesionesContratadas) * 100
    u2 <- totalPagado / estudiantes
    u3 <- (mejoran / estudiantes) * 100
    Escribir "Promedio N1: ", promedioN1
    Escribir "Promedio N4: ", promedioN4
    Escribir "U1: ", u1, "%"
    Escribir "U2: $", u2
    Escribir "U3: ", u3, "%"
FinProceso
```

---

## 7. Contingencias permitidas
- **Si PSeInt falla:** continuar en editor de texto; se califica la lógica, no el ejecutable.
- **Si falla el proyector:** escribir la plantilla inicial en tablero y proyectar solo si vuelve el equipo.
- **Si el grupo se bloquea en la actividad 2:** entregar una plantilla con variables ya declaradas y concentrar el trabajo en máximos/reportes.
- **Si van tarde:** mantener actividades 1, 3 y 4; la extensión a 8 puede cerrarse con 6 terapeutas como mínimo y dejar 7–8 como HTI.
- **Si el compromiso baja:** activar reto por filas: primera fila que muestre promedio correcto gana **Trabajo en equipo** + **Entregó actividad**.

---

## 8. Criterio de éxito del laboratorio
El laboratorio se considera logrado si cada estudiante entrega al menos:
- un pseudocódigo funcional para 4 terapeutas,
- un avance real del integrador a 8 terapeutas,
- y un cálculo correcto de U3 o del resumen UIB.
