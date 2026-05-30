# S06 HAD — Plan de Sesión
## TGA04 Fundamentos de Computación para los Negocios · UIB

**Semana:** 6  
**Modalidad:** HAD · Bloque 1 de 2 (mismo día; descanso 10 min antes de HP)  
**Duración:** 120 minutos  
**RA:** RA2 — Formular soluciones algorítmicas  
**Tema:** Primitivas selectivas: SI-FSI en PSeInt e introducción conceptual al `if` de Python

## 1. Propósito observable (3-5 bullets)
- Reconocer que una estructura selectiva simple ejecuta una acción solo cuando la condición es verdadera.
- Escribir correctamente la forma `Si ... Entonces ... FinSi` en pseudocódigo tipo PSeInt.
- Traducir reglas del caso NeuroBiz, por ejemplo `si N4 > 15 entonces mostrar alerta`, a lenguaje algorítmico.
- Identificar en la tabla qué terapeutas están en alerta por `N1 < 75%` o `N4 > 15%`.
- Preparar el puente entre la lógica en PSeInt y la codificación posterior en Thonny con Python 3.x.

## 2. Checklist preclase (con checkboxes, 24h antes y 15 min antes)
### 24 horas antes
- [ ] Dejar proyectada la agenda exacta de los 8 bloques de trabajo de HAD.
- [ ] Tener lista la diapositiva con la tabla completa de terapeutas y los indicadores N1/N4 pre-calculados.
- [ ] Configurar Quizizz/Wayground en modo Playground con 6 preguntas, 20-25 segundos por pregunta, orden aleatorio y retroalimentación inmediata.
- [ ] Verificar que ClassDojo tenga creadas las categorías fijas del curso.
- [ ] Llevar listo el tablero con las palabras guía: **condición**, **verdadero**, **falso**, **alerta**, **umbral**.

### 15 minutos antes
- [ ] Abrir proyector, temporizador visible y presentación en la diapositiva de agenda.
- [ ] Confirmar conexión a internet y dejar copiado el código/enlace del Quizizz.
- [ ] Abrir PSeInt solo como apoyo visual para mostrar la sintaxis, aunque el bloque sea HAD.
- [ ] Tener agua a la vista y ubicar pausas de voz ya marcadas en la agenda.
- [ ] Escribir en el tablero la frase fija de transición: **"Cerramos bloque, abrimos bloque, cambien solo el recurso."**

## 3. Protocolo de predictibilidad ACCC
- La agenda exacta debe permanecer proyectada desde el minuto 0 hasta el minuto 120.
- El temporizador visible no se oculta en ningún momento; solo cambia de conteo según el bloque.
- Ningún tramo de explicación continua puede superar 20-25 minutos; después se cambia a **MONITOREA**, **DESCANSA VOZ** o **SILENCIO**.
- Toda transición se anuncia con la misma frase: **"Cerramos bloque, abrimos bloque, cambien solo el recurso."**
- Si aparece una contingencia, se aplica la ruta escrita en la sección 8 sin improvisar una nueva.
- Agenda visible del bloque: 1) apertura, 2) repaso, 3) condición lógica, 4) Quizizz, 5) sintaxis SI-FSI, 6) pausa activa, 7) análisis NeuroBiz, 8) cierre.

## 4. ClassDojo: tabla con momento → categoría → acción observable
| Momento | Categoría | Puntos | Acción observable |
|---|---|---:|---|
| Minutos 0-2 | Puntualidad | +1 | Entra listo antes del minuto 2, con cuaderno y equipo abiertos. |
| Respuesta oral o análisis válido | Participación | +1 a +2 | Responde con dato correcto, interpreta un indicador o justifica una condición. |
| Evidencia en cuaderno o digital | Entregó actividad | +2 | Muestra pseudocódigo, captura de Thonny o desarrollo completo del ejercicio. |
| Trabajo cooperativo | Trabajo en equipo | +1 | Colabora, explica a un compañero y no distrae el trabajo del grupo. |
| Pregunta de valor o patrón detectado | Curiosidad | +1 | Hace una pregunta útil o detecta una relación entre N1, N4 y la decisión. |

## 5. Quizizz/Wayground: configuración y preguntas sugeridas (mínimo 6)
**Configuración sugerida**
- Modo: Playground.
- Activación: en el **primer descanso de voz** del docente.
- Cantidad: 6 preguntas.
- Tiempo: 20-25 segundos por pregunta.
- Retroalimentación: inmediata.
- Orden: aleatorio activado.
- Código/enlace: listo antes de clase y copiado en una nota aparte.
- Si no conecta: sustituir por preguntas orales de mano alzada con ClassDojo en tiempo real.

**Preguntas sugeridas**
1. La estructura `Si condición Entonces acción FinSi` se ejecuta cuando la condición es: verdadera / falsa / vacía / numérica.  
2. Si `N4 > 15`, el caso de NeuroBiz dice que debe mostrarse una: alerta / suma / entrada / repetición.  
3. El terapeuta con `N4 = 30.56%` es: T06 / T04 / T02 / T08.  
4. El terapeuta con `N1 = 59.7%` es: T06 / T01 / T03 / T07.  
5. En una selectiva simple, si la condición es falsa, el algoritmo: no ejecuta la acción / repite / suma / se detiene siempre.  
6. `if` en Python corresponde en esta semana a: `SI-FSI` / `MQ-FMQ` / `PARA-FPARA` / `Inicio-Fin`.  

**Clave:** 1 verdadera, 2 alerta, 3 T06, 4 T06, 5 no ejecuta la acción, 6 SI-FSI.

## 6. Cronograma minuto a minuto (tabla: Tiempo | Actividad | Modo docente | Herramienta | ClassDojo)

| Tiempo | Actividad | Modo docente | Herramienta | ClassDojo |
|---|---|---|---|---|
| 00-02 | Recibe en puerta, señala agenda proyectada y exige cuaderno/equipo listos antes del minuto 2. | SILENCIO | Proyector + temporizador | Puntualidad |
| 02-05 | Presenta propósito, reglas de voz y recuerda que HAD y HP ocurren el mismo día. | HABLA | Diapositiva inicial | — |
| 05-10 | Revisa idea previa de algoritmo y pregunta qué significa “cumplir una condición”. | HABLA | Tablero | Participación |
| 10-18 | Explica condición lógica, verdadero/falso y el sentido de un umbral de negocio. | HABLA | Tablero + diapositiva | — |
| 18-22 | Modela dos lecturas del caso: `N1 < 75` y `N4 > 15`. | HABLA | Tabla NeuroBiz proyectada | Participación |
| 22-25 | Pausa de copia guiada; el docente camina, escucha y bebe agua. | MONITOREA | Cuaderno | Entregó actividad |
| 25-27 | Activa Quizizz y dicta instrucciones cortas. | HABLA | Quizizz/Wayground | — |
| 27-40 | Desarrollo del Quizizz en el primer descanso de voz; el docente solo resuelve bloqueos técnicos. | DESCANSA VOZ | Celulares + proyector | Entregó actividad / Participación |
| 40-46 | Cierra Quizizz: aclara por qué T03 y T06 aparecen en zona de alerta por N4. | HABLA | Resultados Quizizz | Curiosidad |
| 46-55 | Presenta la sintaxis PSeInt de SI-FSI y la escribe completa sin borrar la tabla del caso. | HABLA | Tablero + PSeInt proyectado | — |
| 55-60 | Construye con el grupo un primer pseudocódigo: `si N4 > 15 entonces mostrar alerta`. | HABLA | PSeInt | Participación |
| 60-63 | PAUSA ACTIVA de 3 minutos: ponerse de pie, respirar, agua, estiramiento breve. | SILENCIO | Temporizador visible | — |
| 63-72 | Reinicia con la frase fija de transición y plantea análisis por parejas de T01-T08. | HABLA | Tabla impresa/proyectada | Trabajo en equipo |
| 72-82 | Las parejas marcan qué condiciones son verdaderas para cada terapeuta; docente recorre mesas. | MONITOREA | Hoja guía o cuaderno | Trabajo en equipo / Entregó actividad |
| 82-88 | Socializa solo cuatro casos: T03, T06, T08 y T01. | HABLA | Tablero | Participación |
| 88-94 | Introduce el caso UIB: `U1 = 94.7%` y `U3 = 16.7%`; muestra que un if simple también sirve para clientes. | HABLA | Diapositiva | Curiosidad |
| 94-98 | Pausa de voz y copia: estudiantes redactan una regla propia usando “si... entonces...”. | DESCANSA VOZ | Cuaderno | Entregó actividad |
| 98-106 | Muestra el paralelo inicial entre PSeInt y Python: `Si` ↔ `if`, `Escribir` ↔ `print`. | HABLA | Diapositiva comparativa | — |
| 106-114 | Mini cierre conceptual: errores frecuentes al escribir condiciones y al olvidar `FinSi`. | HABLA | Tablero | Participación |
| 114-118 | Ticket de salida: cada estudiante escribe una condición válida con datos de NeuroBiz. | SILENCIO | Papel/cuaderno | Entregó actividad |
| 118-120 | Cierre del bloque y anuncio del HP con la frase fija de transición. | HABLA | Proyector + ClassDojo | Participación |

**Nota operativa:** si alguna actividad se altera por contingencia, se conserva el objetivo del bloque y se activa la tabla de rutas de la sección 8.

## 7. Nota de conexión neurodivergencia (1-2 párrafos)
En Semana 6 se retoma **TDAH** de forma breve y respetuosa. La selectiva simple ayuda a mostrar que una intervención clínica no se decide “por intuición”, sino por un criterio explícito. En el caso de NeuroBiz, el ejemplo guía es claro: **si el ausentismo de T06 supera 15%, entonces requiere plan de mejora**. La regla no juzga a la persona; organiza la acción de seguimiento.

Didácticamente esto también apoya a estudiantes con TDAH, porque la clase reduce ambigüedad: una condición bien escrita produce una sola decisión observable. En vez de sostener largos discursos, el bloque alterna explicación corta, copia guiada, juego y análisis por parejas para mantener foco atencional y previsibilidad.

## 8. Contingencias (tabla: Situación | Ruta A | Ruta B)
| Situación | Ruta A | Ruta B |
|---|---|---|
| Falla el proyector | Pasar la agenda exacta al tablero y mantener el temporizador en celular visible sobre el escritorio. | Trabajar con hojas impresas de la tabla NeuroBiz y escribir solo la sintaxis clave en el tablero. |
| Quizizz/Wayground no conecta | Convertir las 6 preguntas en reto oral con mano alzada y puntos ClassDojo. | Usar Kahoot alternativo si ya está cargado y el acceso es inmediato. |
| Se va la luz | Continuar con cuaderno y tablero si hay iluminación natural suficiente. | Si el aula queda inoperable, convertir el bloque en análisis manual de condiciones con la tabla impresa. |
| Llegan tarde varios estudiantes | Mantener apertura, Quizizz y análisis central; reducir socialización final. | Si el retraso supera 10 minutos, pasar el Quizizz a formato oral y conservar sintaxis SI-FSI + ticket de salida. |
| Internet inestable | Mostrar la tabla ya descargada y hacer preguntas dirigidas sin plataforma. | Pedir captura o evidencia manual en cuaderno y continuar sin gamificación. |
