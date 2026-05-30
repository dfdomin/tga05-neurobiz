# Semana 1 — Material de Estudio
## TGA04 Fundamentos de Computación para los Negocios
**UIB · Tecnología en Gestión Administrativa**  
**Caso transversal:** NeuroBiz S.A.S. + contrato con UIB  
**RA trabajado:** RA1 — Identificar variables y operaciones para solución de problemas organizacionales

---

## 1. ¿Qué debe lograr el estudiante esta semana?
Al finalizar la semana 1, el estudiante debe poder:
- distinguir **dato** e **información**;
- reconocer ejemplos de **hardware, software** y **sistema de información**;
- explicar qué es un **algoritmo**;
- identificar algoritmos de la vida cotidiana y de la vida organizacional;
- comprender el contexto general del caso **NeuroBiz–UIB**.

---

## 2. Dato e información

### 2.1 ¿Qué es un dato?
Un **dato** es un valor o registro aislado que, por sí solo, todavía no explica completamente una situación. Puede ser un número, una palabra, una fecha, un código o una categoría.

### 2.2 ¿Qué es información?
La **información** es el resultado de **organizar, relacionar e interpretar** datos para que sirvan en la toma de decisiones.

### 2.3 Regla práctica para no confundirlos
- Si está **solo** y no permite decidir casi nada, probablemente es **dato**.
- Si ya está **contextualizado**, comparado o interpretado, probablemente es **información**.

### 2.4 Ejemplos desde NeuroBiz
| Elemento | ¿Dato o información? | Explicación |
|---|---|---|
| `68` | Dato | Es solo una cifra aislada. |
| `Ana Ramos` | Dato | Es un nombre sin contexto operativo. |
| `Febrero 2026` | Dato | Es una referencia temporal aislada. |
| `68 sesiones realizadas por Ana Ramos en febrero` | Información | Ya une cantidad, persona y periodo. |
| `Ana Ramos realizó 68 de 80 sesiones y alcanzó 85% de ocupación` | Información | Hay relación entre varios datos y un resultado útil. |
| `Costo total facturado a UIB: $11.840.000 COP` | Información | Permite seguimiento financiero del contrato. |

### 2.5 Del dato a la información
**Ejemplo 1 — NeuroBiz**
- Datos: 68 sesiones realizadas, 80 sesiones disponibles.
- Proceso: calcular `(68/80) × 100`.
- Información: **la terapeuta tuvo una tasa de ocupación del 85%**.

**Ejemplo 2 — UIB**
- Datos: 142 sesiones ejecutadas, 150 contratadas.
- Proceso: calcular `(142/150) × 100`.
- Información: **UIB usó el 94,67% del contrato en febrero**.

---

## 3. Hardware, software y sistema de información

### 3.1 Hardware
El **hardware** es la parte física del sistema computacional: lo que se puede tocar.

**Ejemplos en NeuroBiz y UIB:**
- computador de recepción;
- impresora para consentimientos y reportes;
- video beam del aula;
- teclado, mouse y monitor;
- servidor o equipo donde se almacenan archivos administrativos.

### 3.2 Software
El **software** es el conjunto de programas e instrucciones que le dicen al hardware qué hacer.

**Ejemplos en el curso o en el caso:**
- **PSeInt** para escribir pseudocódigo;
- **draw.io** para diagramas de flujo;
- **Python** como lenguaje de alto nivel que veremos después;
- **ClassDojo** para seguimiento de participación;
- **Quizizz** para evaluación formativa gamificada.

### 3.3 Sistema de información
Un **sistema de información** integra **personas, datos, procesos, reglas, hardware y software** para capturar, almacenar, procesar y comunicar información útil.

### 3.4 Ejemplo de sistema de información en NeuroBiz
| Componente | Ejemplo en NeuroBiz |
|---|---|
| Personas | Recepcionista, terapeuta, coordinador, analista de calidad |
| Datos | nombre del estudiante, sesiones realizadas, cancelaciones, satisfacción |
| Procesos | registro, asignación, agenda, facturación, seguimiento |
| Hardware | computadores, tablets, impresora |
| Software | agenda digital, hojas de cálculo, sistema de historias, correo |
| Información generada | ocupación, ausentismo, costo por sesión, satisfacción |

**Idea clave:** una empresa no mejora por “tener datos”; mejora cuando esos datos circulan dentro de un **sistema de información** y se convierten en decisiones.

---

## 4. Introducción a los algoritmos

### 4.1 Definiciones académicas
A continuación se presentan tres formulaciones académicas útiles. Están **parafraseadas** para facilitar su comprensión en semana 1.

| Fuente | Definición/paráfrasis | Idea clave |
|---|---|---|
| **Cairó Battistutti y Guardati Bueno (2006)** | Un algoritmo es una secuencia **ordenada, precisa y finita** de pasos para resolver un problema. | Orden + precisión + finitud |
| **Joyanes Aguilar (2008)** | Un algoritmo es un conjunto de instrucciones que permite transformar unos **datos de entrada** en un **resultado de salida**. | Entradas → proceso → salidas |
| **Moreno Pérez (2011)** | Un algoritmo es un procedimiento definido que describe cómo ejecutar una tarea para que luego pueda expresarse en un lenguaje formal o de programación. | Procedimiento formalizable |

### 4.2 Síntesis operativa para esta asignatura
En este curso, diremos que un **algoritmo** es:

> **Una secuencia finita, ordenada y clara de pasos que usa datos para producir un resultado útil.**

### 4.3 Características de un buen algoritmo
Un algoritmo de calidad debería ser:
- **Finito:** debe terminar.
- **Preciso:** cada paso debe ser claro y no ambiguo.
- **Ordenado:** el resultado depende del orden correcto.
- **Definido:** mismas entradas, mismo procedimiento.
- **Comprensible:** otra persona debe poder seguirlo.
- **Pertinente al problema:** no debe incluir pasos irrelevantes.
- **Verificable:** se puede revisar si funciona o no.

### 4.4 Estructura básica de un algoritmo
1. **Entrada:** datos que necesito.
2. **Proceso:** operaciones o decisiones.
3. **Salida:** resultado obtenido.

---

## 5. Algoritmos de la vida organizacional: ejemplos específicos
> En esta asignatura no nos interesan solo algoritmos de “hacer café”; nos interesan procesos que una organización realmente necesita.

### 5.1 NeuroBiz (proveedor)
#### Ejemplo A — Calcular N1: tasa de ocupación del terapeuta
- **Entrada:** sesiones realizadas, sesiones disponibles.
- **Proceso:** dividir realizadas entre disponibles y multiplicar por 100.
- **Salida:** porcentaje de ocupación.

#### Ejemplo B — Registrar una nueva sesión
- Recibir nombre del estudiante.
- Verificar si pertenece al contrato UIB.
- Revisar disponibilidad del terapeuta.
- Agendar la sesión.
- Guardar fecha, hora y tipo de atención.
- Emitir confirmación.

#### Ejemplo C — Medir satisfacción del servicio
- Reunir encuestas del mes.
- Contar respuestas “satisfecho” y “muy satisfecho”.
- Dividir ese total entre el total de encuestas.
- Multiplicar por 100.
- Reportar si se cumple o no la meta.

### 5.2 UIB (cliente)
#### Ejemplo D — Controlar uso del contrato
- Tomar sesiones ejecutadas y contratadas.
- Calcular el porcentaje de uso del contrato.
- Comparar con la meta institucional.
- Informar si hay subutilización o buen aprovechamiento.

#### Ejemplo E — Estimar costo por estudiante atendido
- Tomar total pagado a NeuroBiz.
- Contar estudiantes únicos atendidos.
- Dividir el valor pagado entre el número de estudiantes.
- Generar reporte para bienestar universitario.

#### Ejemplo F — Seguimiento académico posterior
- Identificar estudiantes atendidos.
- Registrar promedio académico antes y después.
- Comparar resultados.
- Contar cuántos mejoraron al menos 0,5.
- Generar información de impacto del contrato.

---

## 6. Representación de algoritmos (visión general)
En las próximas semanas representaremos algoritmos de tres maneras:

| Forma | ¿Qué permite? | Herramienta |
|---|---|---|
| Lenguaje natural | Pensar la lógica sin sintaxis compleja | Cuaderno / taller |
| Pseudocódigo | Escribir pasos de forma estructurada | **PSeInt** |
| Diagrama de flujo | Visualizar la secuencia de acciones y decisiones | **draw.io** o PSeInt |

**Preview motivacional:** más adelante, algunos algoritmos pasarán a **Python**, pero en la semana 1 solo se muestra una vista breve, por ejemplo:

```python
print("¡Hola NeuroBiz!")
```

---

## 7. Introducción breve a la neurodivergencia
> **Extensión intencionalmente breve:** esta sección busca dar contexto humano al caso, no reemplazar una clase clínica.

La **neurodivergencia** es una manera de nombrar diferencias en el funcionamiento neurológico y cognitivo de las personas. No significa automáticamente enfermedad ni incapacidad; significa que no todos procesamos la atención, el lenguaje, la socialización, la lectura, los números o la sensibilidad de la misma forma.

### 7.1 Conceptos clave
| Término | Definición breve |
|---|---|
| **TEA** | Trastorno del Espectro Autista: diferencias en comunicación social, flexibilidad conductual y procesamiento sensorial. Para fines introductorios del curso se usa la referencia divulgativa de la **OMS (2023): 1 de cada 100 personas/niños a nivel global**. |
| **TDAH** | Trastorno por Déficit de Atención e Hiperactividad: patrón de inatención, impulsividad y/o hiperactividad que afecta el funcionamiento diario. Como referencia breve de curso se usa la cifra ampliamente difundida por **CDC: 9,4% de niños en EE. UU.** |
| **TDA** | Presentación predominantemente inatenta del TDAH; suele observarse más en olvidos, distracción y dificultad para sostener instrucciones largas. |
| **Dislexia** | Dificultad específica del aprendizaje vinculada con lectura, decodificación y ortografía. |
| **Discalculia** | Dificultad específica en el procesamiento numérico y el razonamiento matemático. |
| **ACCC** | Altas Capacidades Cognitivas y Creativas: desempeño intelectual y/o creativo significativamente superior al promedio; no es trastorno, pero sí puede requerir ajustes educativos. |

### 7.2 ¿Por qué importa esto en NeuroBiz y en UIB?
- Porque NeuroBiz presta servicios justamente a personas con estos perfiles o necesidades.
- Porque UIB, como cliente del contrato, necesita saber si el servicio mejora bienestar, permanencia y desempeño académico.
- Porque trabajar con datos sin contexto humano puede llevar a decisiones pobres o poco sensibles.
- Porque en el aula también puede haber estudiantes con estos perfiles; por eso son valiosas las instrucciones claras, los tiempos definidos y las actividades variadas.

### 7.3 Idea ética central
Cuando una organización registra datos sobre personas, no solo administra números: administra **trayectorias humanas, apoyos, tiempos, costos y oportunidades**.

---

## 8. Preguntas de autorreflexión personal (no calificadas)
> No es necesario compartir estas respuestas en público.

1. ¿Te identificas con alguna de estas formas de aprendizaje o procesamiento?
2. ¿Conoces a alguien con TEA, TDAH, TDA, dislexia, discalculia o ACCC?
3. ¿Qué tipo de explicación te ayuda más a aprender: visual, paso a paso, práctica o escrita?
4. ¿Por qué crees que un curso de computación para negocios debería tratar estos temas con respeto?

---

## 9. Resumen express de la semana
- **Dato** = registro aislado.
- **Información** = dato con contexto y utilidad.
- **Hardware** = parte física.
- **Software** = programas.
- **Sistema de información** = personas + procesos + datos + tecnología.
- **Algoritmo** = secuencia ordenada y finita de pasos para resolver un problema.
- **NeuroBiz** y **UIB** observan el mismo contrato, pero desde perspectivas distintas.

---

## 10. Referencias (formato APA 7.ª ed.)
Cairó Battistutti, O., & Guardati Bueno, S. I. (2006). *Metodología de la programación: Algoritmos, diagramas de flujo y programas* (3.ª ed.). Alfaomega.

Centers for Disease Control and Prevention. (s. f.). *Data and statistics on ADHD*. https://www.cdc.gov/adhd/data/index.html

Joyanes Aguilar, L. (2008). *Fundamentos de programación: algoritmos, estructura de datos y objetos* (3.ª ed.). McGraw-Hill Interamericana.

Ministerio de Educación Nacional. (2017). *Decreto 1421 de 2017: Por el cual se reglamenta en el marco de la educación inclusiva la atención educativa a la población con discapacidad*. https://www.mineducacion.gov.co

Moreno Pérez, J. C., & Raya Cabrera, J. L. (2011). *Programación*. RA-MA Editorial.

World Health Organization. (2023). *Autism spectrum disorders*. https://www.who.int/news-room/fact-sheets/detail/autism-spectrum-disorders

---

## 11. Nota para estudiar mejor esta semana
Recomendación práctica: al leer este material, intenta convertir cada definición en un ejemplo propio. Si puedes inventar un ejemplo de NeuroBiz o de tu vida diaria, ya no estás memorizando: estás comprendiendo.
