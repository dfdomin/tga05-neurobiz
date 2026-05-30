# S03 HP — Plan de Sesión de Laboratorio
## TGA04 Fundamentos de Computación para los Negocios · UIB

**Semana:** 3  
**Modalidad:** HP (laboratorio) · Bloque 2 de 2 · mismo día que HAD  
**Duración:** 120 minutos  
**Herramientas obligatorias:** draw.io / app.diagrams.net, PSeInt, navegador, proyector  
**Productos esperados:** 1 archivo draw.io, 1 PNG exportado, 1 archivo `.psc` y evidencia de ejecución

---

## 1. Meta de laboratorio
Al finalizar el laboratorio, cada estudiante debe haber producido:
1. Un diagrama de flujo en draw.io para **N1**.
2. Un diagrama de flujo integrado para **N1 + N4** de un terapeuta.
3. Un pseudocódigo PSeInt equivalente al flujo integrado.
4. Un flujo y pseudocódigo para **U1 + U2** desde la perspectiva UIB.
5. Una captura mental clara de la equivalencia con Python.

---

## 2. Checklist técnico preclase

### 25–15 min antes
- [ ] Encender equipos y verificar acceso a internet.
- [ ] Abrir en el computador docente: `https://app.diagrams.net/`.
- [ ] Confirmar que PSeInt abre correctamente en al menos 3 equipos de muestra.
- [ ] Tener un archivo modelo mínimo con 5 símbolos básicos.
- [ ] Dejar visible una carpeta de entrega o instrucción de entrega por aula virtual.

### 15–5 min antes
- [ ] Escribir en tablero los nombres de archivo obligatorios:
  - `ApellidoNombre_S03_N1.drawio`
  - `ApellidoNombre_S03_N1N4.drawio`
  - `ApellidoNombre_S03_N1N4.psc`
  - `ApellidoNombre_S03_U1U2.png`
- [ ] Abrir una diapositiva con fórmulas N1, N4, U1 y U2.
- [ ] Dejar lista una imagen del flujo terminado para usarla solo si el grupo se bloquea.

### 5–0 min antes
- [ ] Tener agua disponible para pausas de voz.
- [ ] Preparar ruta B sin internet: papel + PSeInt + tablero.
- [ ] Verificar zoom legible del proyector (125% o 150%).

---

## 3. Reglas operativas para el grupo
- Trabajar siempre con nombre de archivo estandarizado.
- Guardar cada 10 minutos.
- Si el estudiante termina antes, apoya a un compañero sin tomar su teclado.
- En esta semana solo se permiten estructuras **secuenciales**.
- Cuando el docente diga **“manos fuera del mouse”**, todos detienen la edición y miran pantalla.

---

## 4. Cronograma minuto a minuto

| Minutos | Estado | Acción exacta del docente | Acción esperada del estudiante | Herramienta | Contingencia / evidencia |
|---|---|---|---|---|---|
| 00–02 | SILENCIO | Recibe grupo con instrucciones ya proyectadas. | Entra y prende equipo. | Proyector | — |
| 02–05 | HABLA | Presenta meta del laboratorio y productos a entregar. | Toma nota. | Proyector | — |
| 05–08 | HABLA | Da rutina de nombres de archivo y criterio de guardado. | Crea carpeta o identifica ubicación. | Equipo | Si no puede guardar localmente, usar escritorio temporal del equipo. |
| 08–10 | HABLA | Indica apertura de draw.io / app.diagrams.net. | Abre sitio. | Navegador | Si falla el sitio, usar papel cuadriculado o herramienta de formas disponible. |
| 10–15 | HABLA | Demuestra desde cero el flujo de N1: óvalo, entrada, proceso, salida, fin. | Replica visualmente. | draw.io | Mantener explicación breve para no exceder voz continua. |
| 15–20 | DESCANSA VOZ | Circula y corrige postura de símbolos, alineación y flechas. | Ajusta su flujo N1. | draw.io | Evidencia mínima: flujo N1 guardado. |
| 20–25 | MONITOREA | Verifica que todos tengan archivo guardado como `..._S03_N1.drawio`. | Guarda archivo. | draw.io | Si alguien va tarde, darle archivo base. |
| 25–30 | DESCANSA VOZ | Pide exportar mentalmente el recorrido del algoritmo y cerrar actividad 1. | Revisa flujo completo. | draw.io | — |
| 30–33 | HABLA | Introduce actividad 2: combinar N1 y N4 en un único flujo secuencial. | Atiende. | Proyector | — |
| 33–37 | HABLA | Explica que N4 requiere `canceladas` y `programadas`; si no hay `programadas`, usar `realizadas + canceladas`. | Copia regla. | Tablero | — |
| 37–40 | HABLA | Muestra layout sugerido del flujo combinado: entradas arriba, procesos al centro, dos salidas al final. | Observa organización. | draw.io | — |
| 40–45 | DESCANSA VOZ | Circula mientras el grupo construye la sección de entradas. | Dibuja entradas y cálculo de N1. | draw.io | +1 ClassDojo opcional por organización impecable si se desea usar en laboratorio. |
| 45–50 | MONITOREA | Revisa secuencia lógica, flechas y separación visual entre procesos. | Agrega cálculo de N4. | draw.io | — |
| 50–55 | DESCANSA VOZ | Apoya a estudiantes rezagados en voz baja. | Añade dos salidas finales. | draw.io | Evidencia: flujo combinado terminado. |
| 55–60 | MONITOREA | Hace checkpoint visual: todos levantan mano si ya tienen dos salidas. | Autoevalúa avance. | draw.io | Si menos del 70% terminó, mostrar ejemplo parcial 2 minutos. |
| 60–63 | SILENCIO | Pausa breve de estiramiento sentado y descanso ocular. | Se estira y descansa la vista. | Aula | Voz en reposo. |
| 63–67 | HABLA | Abre PSeInt y muestra plantilla base del pseudocódigo integrado. | Abre PSeInt. | PSeInt | — |
| 67–72 | HABLA | Traduce en vivo la primera mitad del flujo: lecturas y cálculo de N1. | Copia estructura. | PSeInt | — |
| 72–75 | HABLA | Añade cálculo de N4 y dos instrucciones `Escribir`. | Completa plantilla. | PSeInt | Aquí termina la ráfaga de voz continua (<15 min). |
| 75–80 | DESCANSA VOZ | Circula mientras los estudiantes escriben su versión propia. | Digita pseudocódigo. | PSeInt | Si PSeInt no abre, escribir pseudocódigo en Bloc de notas o cuaderno. |
| 80–85 | MONITOREA | Verifica sintaxis básica: `Proceso`, `Leer`, `<-`, `Escribir`, `FinProceso`. | Corrige errores. | PSeInt | — |
| 85–88 | DESCANSA VOZ | Pide ejecutar o hacer prueba manual con T01. | Ejecuta y verifica resultado. | PSeInt | Evidencia: resultado visible o comprobación manual. |
| 88–90 | MONITOREA | Cierra actividad 3 y pide guardar `..._S03_N1N4.psc`. | Guarda archivo. | PSeInt | — |
| 90–93 | HABLA | Introduce actividad 4 desde perspectiva UIB: U1 y U2. | Atiende. | Tablero | — |
| 93–97 | HABLA | Repite estructura visual recomendada: mismas etapas, datos distintos. | Observa. | Proyector | — |
| 97–100 | HABLA | Muestra fórmulas: U1 = 142/150 × 100; U2 = 11.840.000 / 12. | Copia. | Tablero | — |
| 100–105 | DESCANSA VOZ | Circula mientras el grupo dibuja el flujo U1+U2. | Construye flujo. | draw.io o cuaderno | Si no alcanza el tiempo, permitir solo descripción textual ordenada. |
| 105–110 | MONITOREA | Revisa si hay dos procesos y dos salidas bien diferenciados. | Ajusta flujo y/o pseudocódigo. | draw.io + PSeInt | Evidencia: U1 y U2 presentes. |
| 110–113 | HABLA | Muestra el equivalente en Python del programa N1+N4. | Compara con PSeInt. | Proyector | No profundizar en sintaxis avanzada. |
| 113–115 | HABLA | Resume: “flowchart = vista espacial; pseudocódigo = vista textual; Python = implementación”. | Escucha. | Proyector | — |
| 115–118 | MONITOREA | Indica exportar PNG del diagrama final y verificar nombres. | Exporta PNG. | draw.io | Si exportación falla, tomar captura de pantalla. |
| 118–120 | HABLA | Explica entrega final y checklist de salida. | Entrega o deja listo para entregar. | Aula virtual / carpeta | Cerrar con recordatorio de HTI si aplica. |

---

## 5. Modelos mínimos que el docente debe mostrar

### 5.1 Flujo N1 en draw.io
`(Inicio) → /Leer disponibles, realizadas/ → [n1 ← (realizadas/disponibles)*100] → /Escribir n1/ → (Fin)`

### 5.2 Flujo combinado N1 + N4
`(Inicio) → /Leer disponibles, realizadas, canceladas/ → [programadas ← realizadas + canceladas] → [n1 ← (realizadas/disponibles)*100] → [n4 ← (canceladas/programadas)*100] → /Escribir n1/ → /Escribir n4/ → (Fin)`

### 5.3 PSeInt combinado
```pseint
Proceso N1_N4_Terapeuta
    Definir disponibles, realizadas, canceladas, programadas, n1, n4 Como Real
    Escribir "Sesiones disponibles:"
    Leer disponibles
    Escribir "Sesiones realizadas:"
    Leer realizadas
    Escribir "Sesiones canceladas:"
    Leer canceladas
    programadas <- realizadas + canceladas
    n1 <- (realizadas / disponibles) * 100
    n4 <- (canceladas / programadas) * 100
    Escribir "N1 = ", n1, "%"
    Escribir "N4 = ", n4, "%"
FinProceso
```

### 5.4 Python preview
```python
disponibles = float(input("Sesiones disponibles: "))
realizadas = float(input("Sesiones realizadas: "))
canceladas = float(input("Sesiones canceladas: "))
programadas = realizadas + canceladas
n1 = (realizadas / disponibles) * 100
n4 = (canceladas / programadas) * 100
print(f"N1 = {n1:.1f}%")
print(f"N4 = {n4:.1f}%")
```

---

## 6. Checklist de salida del estudiante
- [ ] Guardó `ApellidoNombre_S03_N1.drawio`.
- [ ] Guardó `ApellidoNombre_S03_N1N4.drawio`.
- [ ] Guardó `ApellidoNombre_S03_N1N4.psc`.
- [ ] Exportó `ApellidoNombre_S03_U1U2.png` o tomó captura equivalente.
- [ ] Verificó que cada algoritmo tenga: inicio, entrada, proceso, salida y fin.

---

## 7. Contingencias del laboratorio

### Si draw.io no abre
- Trabajar el flujo en papel con regla.
- Luego tomar foto o transcribirlo en la próxima sesión.

### Si PSeInt no está disponible
- Escribir pseudocódigo limpio en editor de texto o cuaderno.
- Hacer prueba manual con los datos de T01 y UIB febrero 2026.

### Si internet cae a mitad del laboratorio
- Mantener actividad con papel + tablero.
- Priorizar el flujo combinado N1+N4 y dejar U1+U2 como extensión.

### Si el grupo avanza más rápido de lo previsto
- Reto: agregar nombre del terapeuta como dato de entrada y mostrarlo junto al resultado.
- Reto 2: probar T08 y explicar por qué N1 = 100% y N4 = 0%.

---

## 8. Criterio de logro
El laboratorio queda logrado si el estudiante entrega al menos un flujo combinado N1+N4 y su pseudocódigo equivalente con secuencia correcta y sintaxis comprensible.
