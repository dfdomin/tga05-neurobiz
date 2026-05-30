# Semana 2 · Material de estudio
## TGA04 Fundamentos de Computación para los Negocios · UIB
### RA1: Variables y Operadores

**Caso de estudio:** NeuroBiz S.A.S. + contrato UIB  
**Objetivo del material:** comprender qué tipos de variables y qué operadores aparecen en indicadores organizacionales reales, y cómo traducirlos a pseudocódigo.

---

## 1. Idea central de la semana

En esta semana no se busca “programar mucho”, sino **pensar con precisión**:
1. **Identificar variables** según el tipo de dato que almacenan.
2. **Reconocer operadores** según la operación que realizan.
3. **Traducir una fórmula** a una secuencia de pasos en pseudocódigo.
4. **Mirar un preview de Python** para motivar lo que vendrá después.

El caso NeuroBiz/UIB es útil porque obliga a pensar desde dos miradas:
- **NeuroBiz (proveedor):** controla terapeutas, sesiones, cancelaciones, satisfacción y costos.
- **UIB (cliente):** controla uso del contrato, costo por estudiante y mejora académica.

---

## 2. ¿Qué es una variable?

### Definición base según Cairó & Guardati (2006)
Cairó y Guardati explican la variable como un **espacio identificado por un nombre**, cuyo contenido puede cambiar durante la ejecución de un algoritmo. En otras palabras, el algoritmo guarda allí un dato para usarlo, modificarlo o mostrarlo después.

### Definición base según Joyanes Aguilar (2008)
Joyanes define la variable como un **identificador asociado a una posición de memoria** que almacena un valor de un tipo determinado. Por eso, antes de resolver un problema, se debe reconocer **qué dato se guarda** y **de qué naturaleza es**.

### Idea práctica para este curso
Una variable es cualquier dato que el negocio necesita leer, guardar, calcular, comparar o mostrar.  
Ejemplos del caso:
- `nombre_terapeuta`
- `sesiones_realizadas`
- `satisfaccion`
- `programa_academico`
- `mejora_mayor_igual_0_5`

---

## 3. Tipos de variables

Cairó y Guardati (2006) y Joyanes Aguilar (2008) coinciden en que, para la resolución algorítmica básica, conviene clasificar las variables por la **naturaleza del dato** que almacenan. En este curso usaremos la clasificación más operativa para el caso NeuroBiz/UIB: **numéricas (enteras y reales), alfanuméricas y lógicas**.

### 3.1 Variables numéricas enteras
**Definición:** almacenan números sin parte decimal. Se usan para conteos, cantidades o registros completos.

**Ejemplos NeuroBiz/UIB**
- Sesiones disponibles = 80
- Sesiones realizadas = 68
- Sesiones canceladas = 9
- Estudiantes únicos atendidos = 12
- Sesiones contratadas = 150

**¿Cuándo conviene pensar “entera”?**
Cuando el dato representa una cantidad contable: 1 terapeuta, 12 estudiantes, 72 sesiones.

### 3.2 Variables numéricas reales
**Definición:** almacenan números con parte decimal. Se usan en promedios, porcentajes, costos y mediciones.

**Ejemplos NeuroBiz/UIB**
- Satisfacción = 4.7
- Promedio antes = 3.1
- Promedio después = 3.7
- U1 = 94.7%
- U2 = 986666.67 COP

**¿Cuándo conviene pensar “real”?**
Cuando el dato puede llevar decimales: 4.2, 20.6%, 3.8, 95.4.

### 3.3 Variables alfanuméricas (cadenas)
**Definición:** almacenan texto, códigos o combinaciones de letras y números tratadas como texto.

**Ejemplos NeuroBiz/UIB**
- ID terapeuta = `T03`
- Nombre = `Luz Torres`
- Programa = `TGA`
- Condición = `TDAH`
- Tipo de servicio = `Terapia grupal`

**Importante:** aunque `T03` tiene números, se trata como texto porque es un código, no una cantidad para sumar o dividir.

### 3.4 Variables lógicas o booleanas
**Definición:** almacenan solo dos posibilidades: **Verdadero/Falso**, **Sí/No**, **Cumple/No cumple**.

**Ejemplos NeuroBiz/UIB**
- `cumple_meta_n1` = Verdadero
- `ausentismo_alto` = Falso
- `mejora_mayor_igual_0_5` = Verdadero
- `satisface_contrato` = Sí / No

**Se construyen a partir de comparaciones**, por ejemplo:
- `N1 >= 75`
- `N4 <= 15`
- `promedio_despues > promedio_antes`

---

## 4. Tabla rápida de ejemplos del caso

| Dato del caso | Tipo de variable | Justificación |
|---|---|---|
| Ana Ramos | Alfanumérica | Es texto, no se calcula. |
| T08 | Alfanumérica | Es un código. |
| 80 sesiones disponibles | Numérica entera | Es una cantidad completa. |
| 4.8 de satisfacción | Numérica real | Tiene decimal. |
| 11.840.000 COP | Numérica real | Es un valor monetario. |
| TDAH | Alfanumérica | Es una etiqueta/condición. |
| ¿N1 >= 75? | Lógica | Responde verdadero o falso. |
| 3.7 de promedio después | Numérica real | Tiene decimal. |
| 12 estudiantes únicos | Numérica entera | Es un conteo. |
| ¿mejora >= 0.5? | Lógica | Es una condición. |

---

## 5. Indicadores y tipos de variables que intervienen

| Indicador | Fórmula | Variables principales | Tipos de variables involucrados |
|---|---|---|---|
| N1 Tasa de ocupación | (Sesiones realizadas / Sesiones disponibles) × 100 | realizadas, disponibles, n1 | Enteras + real |
| N2 Índice de satisfacción | (Encuestas satisfecho o muy satisfecho / total encuestas) × 100 | satisfechos, total_encuestas, n2 | Enteras + real |
| N3 Tiempo promedio de sesión | Total horas sesión / número de sesiones | total_horas, numero_sesiones, n3 | Reales + enteras |
| N4 Tasa de ausentismo | (Sesiones canceladas / sesiones programadas) × 100 | canceladas, programadas, n4 | Enteras + real |
| N5 Cancelación tardía | (Cancelaciones < 24h / total programadas) × 100 | cancelaciones_tardias, total_programadas, n5 | Enteras + real |
| N6 Costo por sesión | Costos operativos / número de sesiones realizadas | costos, realizadas, n6 | Real + enteras |
| N7 Retención de pacientes | (Pacientes activos mes actual / pacientes iniciales) × 100 | activos, iniciales, n7 | Enteras + real |
| N8 Eficiencia diagnóstica | (Diagnósticos entregados en tiempo / total diagnósticos iniciados) × 100 | diagnosticos_tiempo, total_diagnosticos, n8 | Enteras + real |
| U1 Uso del contrato | (Sesiones usadas / sesiones contratadas) × 100 | usadas, contratadas, u1 | Enteras + real |
| U2 Costo por estudiante | Total pagado / estudiantes únicos | total_pagado, estudiantes_unicos, u2 | Real + enteras |
| U3 Mejora académica | (Estudiantes con mejora >= 0.5 / total) × 100 | mejora, total, u3 | Enteras + lógica + real |
| U4 Diagnósticos nuevos | (Diagnósticos nuevos / total evaluados) × 100 | nuevos, evaluados, u4 | Enteras + real |
| U5 Sesiones ejecutadas vs contratadas | Sesiones reales / sesiones contratadas | reales, contratadas, u5 | Enteras + real |
| U6 Satisfacción UIB | (Estudiantes satisfechos / total encuestados) × 100 | satisfechos, encuestados, u6 | Enteras + real |
| U7 Deserción post-intervención | (Estudiantes que desertaron / total intervenidos) × 100 | desertaron, intervenidos, u7 | Enteras + real |

---

## 6. Operadores: qué son y cómo se usan

### 6.1 Operadores matemáticos
**Definición:** permiten efectuar cálculos aritméticos con variables numéricas.

| Operador | Significado | Ejemplo NeuroBiz |
|---|---|---|
| `+` | suma | `programadas <- realizadas + canceladas` |
| `-` | resta | `mejora <- promedio_despues - promedio_antes` |
| `*` | multiplicación | `u1 <- (usadas / contratadas) * 100` |
| `/` | división | `n1 <- realizadas / disponibles` |
| `%` o módulo | residuo de una división | útil si se quisiera saber si un número de sesiones es par o impar |

### 6.2 Operadores relacionales
**Definición:** comparan dos valores y producen un resultado lógico.

| Operador | Significado | Ejemplo del caso | Resultado |
|---|---|---|---|
| `>` | mayor que | `n4 > 15` | verdadero si el ausentismo supera el umbral |
| `<` | menor que | `satisfaccion < 4.5` | verdadero si está por debajo del objetivo |
| `>=` | mayor o igual que | `n1 >= 75` | verdadero si cumple ocupación mínima |
| `<=` | menor o igual que | `n4 <= 15` | verdadero si cumple meta de ausentismo |
| `==` | igual a | `programa == "TGA"` | verdadero si el estudiante es de TGA |
| `!=` | diferente de | `condicion != "TDAH"` | verdadero si la condición es otra |

### 6.3 Operadores lógicos
**Definición:** combinan o invierten condiciones lógicas.

| Operador | Significado | Ejemplo NeuroBiz/UIB |
|---|---|---|
| `Y` / `AND` | ambas condiciones deben cumplirse | `n1 >= 75 Y n4 <= 15` |
| `O` / `OR` | basta con una condición verdadera | `programa == "TGA" O programa == "Contaduría"` |
| `NO` / `NOT` | invierte el valor lógico | `NO(cumple_meta)` |

### 6.4 Operadores estadísticos
**Definición:** resumen conjuntos de datos para apoyar decisiones.

| Operador | Qué hace | Ejemplo con el caso |
|---|---|---|
| Suma | acumula cantidades | total de sesiones realizadas por todos los terapeutas |
| Promedio | calcula valor medio | promedio de satisfacción de T01–T08 |
| Máximo | identifica el valor más alto | mayor N1 entre terapeutas |
| Mínimo | identifica el valor más bajo | menor N4 del mes |
| Conteo | cuenta elementos | número de estudiantes únicos atendidos |

---

## 7. Guía de sintaxis de pseudocódigo

### 7.1 Palabras y símbolos básicos

| Elemento | Función | Ejemplo |
|---|---|---|
| `INICIO` / `FIN` | marcan el comienzo y el cierre del algoritmo | `Inicio` ... `Fin` |
| `LEER` | captura datos de entrada | `Leer realizadas` |
| `ESCRIBIR` | muestra un resultado o mensaje | `Escribir n1` |
| `<-` | asignación | `n1 <- (realizadas / disponibles) * 100` |
| `+ - * /` | operadores matemáticos | `mejora <- despues - antes` |
| `> < >= <= == !=` | operadores relacionales | `n1 >= 75` |
| `Y O NO` | operadores lógicos | `n1 >= 75 Y n4 <= 15` |

> **Nota de curso:** en algunos textos se usa `:=` para asignación. En PSeInt y en la mayoría de ejemplos del curso usaremos `<-`.

### 7.2 Estructura mínima

```text
Proceso NombreDelAlgoritmo
    Definir variable1, variable2, resultado Como Real
    Leer variable1
    Leer variable2
    resultado <- operacion
    Escribir resultado
FinProceso
```

---

## 8. Ejemplos resueltos en pseudocódigo

### 8.1 Calcular N1 para Ana Ramos (T01)
**Datos:** sesiones realizadas = 68, sesiones disponibles = 80

**Fórmula:**
`N1 = (sesiones realizadas / sesiones disponibles) * 100`

**Sustitución:**
`N1 = (68 / 80) * 100 = 85.0%`

**Pseudocódigo:**

```text
Proceso Calcular_N1_Ana_Ramos
    Definir realizadas, disponibles, n1 Como Real
    realizadas <- 68
    disponibles <- 80
    n1 <- (realizadas / disponibles) * 100
    Escribir "N1 Ana Ramos = ", n1, "%"
FinProceso
```

### 8.2 Calcular N4 para Luz Torres (T03)
**Datos:** sesiones realizadas = 54, canceladas = 14  
**Paso previo:** sesiones programadas = 54 + 14 = 68

**Fórmula:**
`N4 = (sesiones canceladas / sesiones programadas) * 100`

**Sustitución:**
`N4 = (14 / 68) * 100 = 20.6% aprox.`

**Pseudocódigo:**

```text
Proceso Calcular_N4_Luz_Torres
    Definir realizadas, canceladas, programadas, n4 Como Real
    realizadas <- 54
    canceladas <- 14
    programadas <- realizadas + canceladas
    n4 <- (canceladas / programadas) * 100
    Escribir "N4 Luz Torres = ", n4, "%"
FinProceso
```

### 8.3 Calcular U1 para UIB (febrero)
**Datos:** sesiones usadas = 142, sesiones contratadas = 150

**Fórmula:**
`U1 = (sesiones usadas / sesiones contratadas) * 100`

**Sustitución:**
`U1 = (142 / 150) * 100 = 94.7% aprox.`

**Pseudocódigo:**

```text
Proceso Calcular_U1_UIB
    Definir usadas, contratadas, u1 Como Real
    usadas <- 142
    contratadas <- 150
    u1 <- (usadas / contratadas) * 100
    Escribir "U1 UIB = ", u1, "%"
FinProceso
```

### 8.4 Calcular U2 para UIB (febrero)
**Datos:** total pagado = 11840000, estudiantes únicos = 12

**Fórmula:**
`U2 = total pagado / estudiantes unicos`

**Sustitución:**
`U2 = 11840000 / 12 = 986666.67 COP aprox.`

**Pseudocódigo:**

```text
Proceso Calcular_U2_UIB
    Definir total_pagado, estudiantes_unicos, u2 Como Real
    total_pagado <- 11840000
    estudiantes_unicos <- 12
    u2 <- total_pagado / estudiantes_unicos
    Escribir "U2 UIB = ", u2, " COP"
FinProceso
```

---

## 9. Python preview: así se ve esto en Python

> **Importante:** este fragmento es solo de observación y motivación. En esta semana la meta formal sigue siendo pseudocódigo.

```python
# N1 = (sesiones_realizadas / sesiones_disponibles) * 100
sesiones_realizadas = float(input("Ingrese sesiones realizadas: "))
sesiones_disponibles = float(input("Ingrese sesiones disponibles: "))

n1 = (sesiones_realizadas / sesiones_disponibles) * 100
print("La tasa de ocupación es:", n1, "%")
```

### Anotación línea por línea
- `sesiones_realizadas = ...` crea una variable y guarda lo que el usuario escribe.
- `float(...)` indica que el valor se leerá como número decimal.
- `n1 = ...` hace la misma operación del pseudocódigo.
- `print(...)` muestra el resultado en pantalla.

### Equivalencia conceptual
| Pseudocódigo | Python |
|---|---|
| `Leer sesiones_realizadas` | `sesiones_realizadas = float(input(...))` |
| `n1 <- ...` | `n1 = ...` |
| `Escribir n1` | `print(n1)` |

---

## 10. ¿Por qué la tasa de ausentismo importa? (TDAH / TDA y N4)

La fórmula **N4 = (sesiones canceladas / sesiones programadas) × 100** parece solo matemática, pero en realidad tiene un sentido humano y organizacional importante. En un servicio como NeuroBiz, una tasa de ausentismo alta puede afectar:
- la continuidad de la intervención,
- la disponibilidad del terapeuta,
- el costo del contrato,
- y la posibilidad de que el estudiante reciba apoyo sostenido.

### Conexión con TDAH y TDA
El **TDAH** y el **TDA** (presentación predominantemente inatenta) son condiciones del neurodesarrollo asociadas con dificultades en atención sostenida, organización, manejo del tiempo, seguimiento de rutinas y memoria de trabajo. El CDC explica que los síntomas pueden causar dificultades en la escuela, en casa o con los amigos, y que pueden cambiar con el tiempo según aumentan las demandas de la vida diaria (CDC, 2025).

En términos prácticos, esto significa que algunas personas con TDAH/TDA pueden necesitar más apoyo para:
- recordar horarios,
- sostener una rutina semanal,
- preparar con tiempo la salida hacia una cita,
- reorganizarse si hubo cambios inesperados.

Por eso, cuando NeuroBiz calcula **N4**, no está “culpando” a nadie. Está detectando un patrón operativo que puede requerir acciones de apoyo, por ejemplo:
- recordatorios automáticos,
- confirmación previa de asistencia,
- horarios más predecibles,
- seguimiento coordinado con bienestar universitario,
- ajustes razonables para sostener la adherencia al proceso.

### Dato útil del CDC para contextualizar
Según datos del CDC publicados en 2024 con base en la encuesta nacional de 2022:
- aproximadamente **7.1 millones** de niños y adolescentes en EE. UU. (11.4%) habían recibido un diagnóstico de TDAH;
- **58.1%** de quienes tenían TDAH actual presentaban nivel moderado o severo;
- **77.9%** tenía al menos una condición concurrente;
- cerca de **30.1%** no recibió tratamiento específico para TDAH en ese periodo.

Estos datos no dicen que toda inasistencia sea causada por TDAH, pero sí muestran que se trata de una condición frecuente y relevante para el seguimiento educativo y terapéutico. En el contexto UIB–NeuroBiz, monitorear N4 ayuda a detectar si el servicio necesita estrategias de acompañamiento más consistentes.

### Idea ética clave
- **N4 es un indicador organizacional, no un diagnóstico clínico.**
- Un porcentaje no explica por sí solo la historia de una persona.
- El análisis correcto combina **datos + contexto + criterio humano**.

---

## 11. Autoevaluación rápida (con respuestas)

### 1) ¿Qué tipo de variable es `T05`?
**Respuesta:** alfanumérica, porque es un código.

### 2) ¿Qué operadores aparecen en `U1 = (142 / 150) * 100`?
**Respuesta:** división y multiplicación.

### 3) ¿Qué tipo de variable es `cumple_meta` si se construye con `N1 >= 75`?
**Respuesta:** lógica o booleana.

### 4) Si una variable guarda `4.9`, ¿es entera o real?
**Respuesta:** real, porque tiene decimal.

### 5) ¿Qué hace la línea `programadas <- realizadas + canceladas`?
**Respuesta:** suma dos variables y asigna el resultado a una nueva variable llamada `programadas`.

---

## 12. Referencias (APA 7.ª ed.)

Cairó Battistutti, O., & Guardati Bueno, S. I. (2006). *Metodología de la programación: algoritmos, diagramas de flujo y programas* (3.ª ed.). Alfaomega.

Centers for Disease Control and Prevention. (2024, November 18). *Data and statistics on ADHD*. https://www.cdc.gov/adhd/data/index.html

Centers for Disease Control and Prevention. (2025, November 25). *About ADHD*. https://www.cdc.gov/adhd/about/index.html

Danielson, M. L., Claussen, A. H., Bitsko, R. H., et al. (2024). ADHD prevalence among U.S. children and adolescents in 2022: Diagnosis, severity, co-occurring disorders, and treatment. *Journal of Clinical Child & Adolescent Psychology*. Advance online publication. https://pubmed.ncbi.nlm.nih.gov/38778436/

Joyanes Aguilar, L. (2008). *Fundamentos de programación: algoritmos, estructura de datos y objetos* (3.ª ed.). McGraw-Hill Interamericana.
