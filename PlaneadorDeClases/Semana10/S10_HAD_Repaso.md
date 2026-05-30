# S10 HAD — Repaso Pre-Segundo Parcial
## TGA04 Fundamentos de Computación para los Negocios · UIB

**Semana:** 10  
**Modalidad:** HAD  
**Duración:** 120 minutos  
**Secuencia del día:** **HAD repaso (120 min) → descanso (10–15 min) → Segundo Parcial (90 min)**. Esta semana **no hay taller ni material de estudio**; el parcial reemplaza el bloque HP.  
**Herramientas:** ClassDojo, Quizizz modo Playground, PSeInt, Thonny, proyector, tablero, temporizador visible, agua.  
**Propósito:** consolidar primitivas selectivas y repetitivas antes del Segundo Parcial, usando el caso NeuroBiz/UIB como referencia conocida y aclarando la logística del examen con empresa nueva.  
**Límite docente (ACCC):** no sostener más de 20–25 minutos seguidos en modo HABLA.

---

## 1. Protocolo ACCC de predictibilidad
- Mantener proyectada desde el minuto 0 la agenda completa de los bloques.
- Usar siempre los tres modos explícitos: **HABLA**, **MONITOREA** y **DESCANSA VOZ**.
- Anunciar cada transición con la misma frase: **“Cerramos este bloque; sigue el siguiente tal como está en pantalla.”**
- No improvisar nuevas dinámicas; si algo falla, usar solo las contingencias escritas al final.
- Tener visibles en tablero los 4 umbrales del corte: **N1 ≥ 75%, N4 ≤ 15%, U1 ≥ 80%, U3 ≥ 60%**.
- Cuando un estudiante pida “otro ejemplo”, responder con uno de estos tres recursos fijos: **T06**, **una pregunta del Quizizz** o **un mini-ejemplo en tablero**.
- Al cerrar cada bloque, indicar en una frase qué ya quedó hecho y qué sigue. Esto reduce ansiedad y evita ambigüedad.

---

## 2. Checklist preclase
- [ ] Abrir **ClassDojo** y dejar listas las categorías: Puntualidad, Participación, Trabajo en equipo, Entregó actividad.
- [ ] Abrir **Quizizz Playground** con las 10 preguntas de repaso de esta guía.
- [ ] Escribir en tablero las fórmulas base: `N1`, `N4`, `U1`, `U3`.
- [ ] Proyectar la secuencia del día: **Repaso → Descanso → Parcial**.
- [ ] Tener a mano el enunciado corto de la actividad grupal con **T06**.
- [ ] Confirmar que **Thonny** y **PSeInt** estén disponibles por si un estudiante pide ver la traducción de pseudocódigo a Python.
- [ ] Dejar visible el recordatorio logístico del parcial: **90 minutos, individual, calculadora básica no programable**.

---

## 3. Cronograma minuto a minuto (120 min)

| Tiempo | Actividad | Modo docente | Recurso | ClassDojo |
|---|---|---|---|---|
| 00–03 | Saludo breve, proyección de agenda completa y recordatorio: hoy no hay HP, porque el parcial reemplaza ese bloque. | HABLA | Proyector | **Puntualidad** a quien entra listo. |
| 03–08 | Explicar la ruta fija del día: repaso, pausa, descanso, parcial. Nombrar los modos HABLA / MONITOREA / DESCANSA VOZ. | HABLA | Diapositiva | — |
| 08–15 | Recordatorio guiado de fórmulas y umbrales: N1, N4, U1, U3. | HABLA | Tablero | **Participación** por responder umbrales. |
| 15–25 | Repaso de primitivas selectivas: **SI-FSI**, **SI-SINO-FSI**, **DD-FDD** con ejemplos rápidos del caso NeuroBiz/UIB. | HABLA | Tablero / PSeInt proyectado | **Participación** por clasificar bien la primitiva. |
| 25–35 | Micropráctica por parejas: para 3 situaciones dadas, decidir qué primitiva selectiva conviene usar y por qué. | MONITOREA | Cuaderno / tablero | **Trabajo en equipo**. |
| 35–45 | Repaso de primitivas repetitivas: **MQ-FMQ (while)**, **PARA-FPARA (for)**, **HH-FHH (do-while)**. | HABLA | Tablero / PSeInt | **Participación** por justificar cuándo se usa cada una. |
| 45–55 | **Quizizz Playground** de 10 preguntas de repaso. El docente circula y escucha; casi no reexplica. | DESCANSA VOZ | Quizizz | **Entregó actividad** + **Participación** al completar. |
| 55–60 | Retroalimentación corta del Quizizz: revisar solo errores más frecuentes y anunciar pausa activa. | HABLA | Quizizz / tablero | **Participación** por detectar error típico. |
| 60–65 | **Pausa activa**: ponerse de pie, mover cuello/hombros, mirar lejos, respirar 4-4-4. | DESCANSA VOZ | Aula | — |
| 65–70 | Reingreso y lectura de la actividad grupal sobre **T06**. | HABLA | Guía proyectada | — |
| 70–88 | Actividad grupal: construir diagrama de flujo + pseudocódigo que evalúe alertas de **N1** y **N4** para T06. | MONITOREA | Cuaderno / PSeInt | **Trabajo en equipo** y **Entregó actividad**. |
| 88–98 | Socialización rápida de 2 grupos: comparar mensajes y lógica condicional usada. | HABLA | Tablero | **Participación** a quien argumenta la condición. |
| 98–108 | **Anuncio formal del parcial**: qué se evalúa, duración, material permitido, empresa nueva y criterios RA3. | HABLA | Diapositiva | — |
| 108–115 | Preguntas logísticas cerradas. El docente responde solo sobre formato e instrucciones, no resuelve el examen. | MONITOREA + HABLA breve | Aula | **Curiosidad** por pregunta pertinente. |
| 115–120 | Cierre: conteo final de ClassDojo, frase de transición escrita, checklist antes del descanso. | HABLA | ClassDojo | Reconocimiento final. |

**Frases de transición ya preparadas**
1. “Cerramos este bloque; sigue el siguiente tal como está en pantalla.”
2. “Ahora no abrimos tema nuevo; solo consolidamos lo que ya está previsto.”
3. “La duda se responde con T06, con Quizizz o con la guía; no cambiamos de ruta.”

---

## 4. Repaso conceptual mínimo que debe quedar visible

### Selectivas
- **SI-FSI:** una sola decisión.
- **SI-SINO-FSI:** dos rutas excluyentes.
- **DD-FDD:** varias opciones según un valor o categoría.

### Repetitivas
- **MQ-FMQ (while):** repite mientras una condición sea verdadera.
- **PARA-FPARA (for):** repite una cantidad conocida de veces.
- **HH-FHH (do-while):** ejecuta al menos una vez y luego valida.

### Idea puente para el parcial
- Si analizo **un terapeuta**, normalmente uso **selectivas**.
- Si proceso **todos los terapeutas**, normalmente uso **repetitivas**.
- Si clasifico estado según umbrales, necesito **operadores relacionales y lógicos**.

---

## 5. Quizizz modo Playground — 10 preguntas de repaso

1. Si solo debo mostrar una alerta cuando `N4 > 15`, ¿qué estructura basta?  
   a) SI-FSI b) PARA-FPARA c) HH-FHH d) DD-FDD
2. Si debo mostrar un estado **VERDE o ROJO** según una condición, la estructura más directa es:  
   a) MQ-FMQ b) SI-SINO-FSI c) DD-FDD d) FPARA
3. Si tengo varias categorías posibles según el tipo de servicio, conviene usar:  
   a) DD-FDD b) MQ-FMQ c) SI-FSI d) HH-FHH
4. `N1 >= 75 Y N4 <= 15` es una condición:  
   a) alfanumérica b) lógica compuesta c) estadística d) secuencial
5. Si debo procesar exactamente **6 terapeutas**, la estructura más directa es:  
   a) PARA-FPARA b) HH-FHH c) DD-FDD d) SI-FSI
6. Si no sé cuántas veces se repetirá una acción y depende de una condición, puedo usar:  
   a) MQ-FMQ b) DD-FDD c) SI-SINO-FSI d) Ninguna
7. La estructura que **siempre ejecuta al menos una vez** es:  
   a) MQ-FMQ b) PARA-FPARA c) HH-FHH d) DD-FDD
8. Para el caso NeuroBiz, si T06 tiene `N1 = 59.7%` y `N4 = 30.56%`, el mensaje correcto sería:  
   a) sin alertas b) alerta en N1 solamente c) alerta en N4 solamente d) alerta doble en N1 y N4
9. En PSeInt, `contador <- contador + 1` se usa normalmente dentro de una estructura:  
   a) repetitiva b) solo selectiva c) de entrada d) de salida
10. Si un terapeuta cumple **solo uno** de los dos umbrales, en el parcial se clasifica como:  
   a) Verde b) Amarillo c) Rojo d) No corresponde

**Clave:** 1a, 2b, 3a, 4b, 5a, 6a, 7c, 8d, 9a, 10b.

---

## 6. Actividad grupal central — Caso T06 (NeuroBiz/UIB)

### Enunciado para proyectar
Dado el terapeuta **T06 — Diego Ríos** con estos datos:
- Sesiones disponibles: **72**
- Sesiones realizadas: **43**
- Sesiones canceladas: **22**

Construyan en grupos de 3:
1. Un **diagrama de flujo** que calcule `N1` y `N4`.
2. Un **pseudocódigo en estilo PSeInt** que evalúe si hay alertas en `N1` y `N4`.
3. Un mensaje final apropiado según el resultado:
   - **Sin alertas**
   - **Alerta en N1**
   - **Alerta en N4**
   - **Alerta doble en N1 y N4**

### Recordatorio de umbrales
- `N1 = (realizadas / disponibles) × 100` → cumple si **N1 ≥ 75%**
- `N4 = (canceladas / disponibles) × 100` → cumple si **N4 ≤ 15%**

### Resultado esperado por el docente
- `N1 = (43 / 72) × 100 = 59.7%`
- `N4 = (22 / 72) × 100 = 30.56%`
- **Conclusión:** T06 tiene **alerta doble**: falla en N1 y falla en N4.

### Pseudocódigo guía mínimo esperado
```pseint
Proceso AlertaT06
    Definir disponibles, realizadas, canceladas, n1, n4 Como Real
    disponibles <- 72
    realizadas <- 43
    canceladas <- 22
    n1 <- (realizadas / disponibles) * 100
    n4 <- (canceladas / disponibles) * 100

    Si n1 < 75 Y n4 > 15 Entonces
        Escribir "Alerta doble en N1 y N4"
    SiNo
        Si n1 < 75 Entonces
            Escribir "Alerta en N1"
        SiNo
            Si n4 > 15 Entonces
                Escribir "Alerta en N4"
            SiNo
                Escribir "Sin alertas"
            FinSi
        FinSi
    FinSi
FinProceso
```

---

## 7. Anuncio formal del Segundo Parcial

### Guion breve para leer al grupo
> “El Segundo Parcial evalúa lo trabajado en semanas 6 a 9: primitivas selectivas **SI-FSI, SI-SINO-FSI, DD-FDD** y primitivas repetitivas **MQ-FMQ, PARA-FPARA, HH-FHH**. También evalúa identificación de variables, operadores y lectura de indicadores. Dura **90 minutos**, es **individual** y solo permite **calculadora básica no programable**, lápiz, lapicero y borrador. La empresa del parcial será **ApoyaNov S.A.S.** y el cliente será **Cementos Norte S.A.**; es una empresa nueva, diferente a TerapiaSer y diferente al caso de repaso NeuroBiz.”

### Qué se evalúa
- Identificación de variables significativas.
- Clasificación de datos y uso de operadores.
- Construcción de pseudocódigo selectivo para clasificar estado de un terapeuta.
- Construcción de pseudocódigo repetitivo para procesar varios terapeutas.
- Lectura correcta de indicadores: **N1, N4, U1, U3**.

### Tiempo y materiales permitidos
- **Duración:** 90 minutos.
- **Modalidad:** individual.
- **Permitido:** calculadora básica no programable, lápiz, lapicero, borrador.
- **No permitido:** celular, IA, calculadora programable, compartir cuaderno durante la prueba.

### Mensaje logístico final
- Esta semana **solo hay repaso y parcial**.
- Después del repaso hay **descanso corto** y luego inicia el examen.
- El enunciado del parcial será **autocontenido**: trae fórmulas, umbrales y datos del caso.

---

## 8. Uso de ClassDojo durante el repaso

| Momento | Conducta observable | Categoría sugerida |
|---|---|---|
| Inicio | Llegó listo, con cuaderno y calculadora | Puntualidad |
| Repaso de fórmulas | Responde correctamente un umbral o identifica una estructura | Participación |
| Quizizz | Completa las 10 preguntas | Entregó actividad |
| Actividad T06 | Aporta en el diagrama o pseudocódigo del equipo | Trabajo en equipo |
| Cierre | Formula una pregunta logística clara y pertinente | Participación |

**Regla para el docente:** asignar puntos en los cambios de bloque, no interrumpiendo explicaciones largas.

---

## 9. Contingencias permitidas
- **Si falla Quizizz:** pasar las 10 preguntas a formato oral o proyectado y responder por filas; mantener el mismo banco y la misma clave.
- **Si falla internet:** usar tablero y cuaderno; el objetivo no cambia.
- **Si falla el proyector:** escribir agenda, fórmulas y T06 en tablero; conservar cronograma.
- **Si el grupo llega con ansiedad alta por el parcial:** no abrir temas nuevos; repetir solo fórmulas, umbrales y estructura del examen.
- **Si se van 10 minutos tarde:** conservar Quizizz, pausa activa, T06 y anuncio formal; reducir la socialización de grupos a 1 equipo.
- **Si el docente necesita descanso de voz antes de tiempo:** mover inmediatamente a MONITOREA con actividad escrita ya prevista; no improvisar conversación abierta.
- **Si un estudiante pregunta “¿esto viene en el parcial?”:** responder con la frase fija: **“Vienen estas mismas decisiones algorítmicas, pero con empresa nueva.”**

---

## 10. Cierre escrito que debe quedar visible antes del descanso
```text
YA REPASAMOS:
1. SI-FSI / SI-SINO-FSI / DD-FDD
2. MQ-FMQ / PARA-FPARA / HH-FHH
3. N1 / N4 / U1 / U3
4. Caso T06 con alertas

SIGUE:
Descanso corto → Segundo Parcial (90 min) → empresa nueva: ApoyaNov S.A.S.
```
