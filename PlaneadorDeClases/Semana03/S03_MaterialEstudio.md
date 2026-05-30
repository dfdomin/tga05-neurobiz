# S03 — Material de Estudio
## Representación algorítmica: diagramas de flujo y pseudocódigo formal
### TGA04 Fundamentos de Computación para los Negocios · UIB · Semana 3

**Caso transversal:** NeuroBiz S.A.S. + UIB  
**Tema central:** representar un algoritmo secuencial de dos maneras: visualmente (diagrama de flujo) y textualmente (pseudocódigo en PSeInt).

---

## 1. Idea central de la semana
Un algoritmo secuencial siempre sigue el mismo patrón:

**Inicio → entrada de datos → proceso → salida → fin**

En Semana 3 todavía **no usamos condicionales ni ciclos**. Por eso, todos los ejemplos de esta guía son **secuenciales**.

---

## 2. Datos guía del caso NeuroBiz + UIB

### 2.1 Terapeutas de NeuroBiz
| ID | Nombre | Especialidad | Disponibles | Realizadas | Canceladas | Satisfacción |
|---|---|---|---:|---:|---:|---:|
| T01 | Ana Ramos | Psicología | 80 | 68 | 9 | 4.7/5 |
| T02 | Carlos Mejía | Fonoaudiología | 72 | 71 | 2 | 4.9/5 |
| T03 | Luz Torres | TO | 72 | 54 | 14 | 4.2/5 |
| T04 | Mario Suárez | Psicología | 80 | 77 | 4 | 4.8/5 |
| T05 | Paula Vega | Neuropsicología | 60 | 58 | 1 | 5.0/5 |
| T06 | Diego Ríos | Fonoaudiología | 72 | 43 | 22 | 3.9/5 |
| T07 | Sandra Ospina | TO | 72 | 69 | 5 | 4.6/5 |
| T08 | Héctor Niño | Psicología | 80 | 80 | 0 | 4.8/5 |

### 2.2 Datos de UIB (febrero 2026)
- **Sesiones contratadas:** 150
- **Sesiones usadas:** 142
- **Total pagado:** $11.840.000 COP
- **Estudiantes únicos atendidos:** 12

### 2.3 Fórmulas clave
- **N1** = (Sesiones realizadas / Sesiones disponibles) × 100
- **N4** = (Canceladas / Programadas) × 100
- **U1** = (Sesiones usadas / Sesiones contratadas) × 100 = 94.7%
- **U2** = Total pagado / estudiantes únicos = $986.667 COP por estudiante (aprox.)

> **Nota didáctica:** cuando no se entrega explícitamente el dato de sesiones programadas, para esta semana trabajaremos con la simplificación:  
> **Programadas = realizadas + canceladas**.

---

## 3. Simbología básica de diagramas de flujo (ISO 5807)

Los diagramas de flujo usan símbolos estándar para representar las etapas de un algoritmo.

### 3.1 Inicio / Fin (óvalo)
**Uso:** marcar el comienzo o el cierre del algoritmo.

```text
  ( Inicio / Fin )
```

**Ejemplo en el caso:** iniciar el cálculo de N1 o finalizar la impresión del resultado.

### 3.2 Proceso (rectángulo)
**Uso:** realizar una operación, fórmula o asignación.

```text
+----------------------+
|       PROCESO        |
+----------------------+
```

**Ejemplo:** `n1 <- (realizadas / disponibles) * 100`

### 3.3 Entrada / Salida (paralelogramo)
**Uso:** leer datos o mostrar resultados.

```text
   /------------------/
  /  ENTRADA/SALIDA  /
 /------------------/
```

**Ejemplos:**
- Leer sesiones disponibles.
- Escribir “N1 = 85%”.

### 3.4 Decisión (rombo)
**Uso:** representar una pregunta con alternativas.

```text
     /-----------\
    /  DECISIÓN   \
    \           /
     \---------/
```

**Importante:** es parte de la simbología estándar, pero **no se usa todavía** en Semana 3 porque las decisiones se trabajan desde la Semana 6.

### 3.5 Conector (círculo)
**Uso:** unir partes del diagrama cuando no cabe todo en una sola línea o página.

```text
   ( A )
```

**Ejemplo:** continuar un diagrama largo sin cruzar flechas.

### 3.6 Flecha de dirección
**Uso:** indicar el orden en que se ejecutan los pasos.

```text
[ Paso 1 ] ---> [ Paso 2 ] ---> [ Paso 3 ]
```

**Idea clave:** si no hay flechas claras, el lector no sabe qué se ejecuta primero.

---

## 4. Reglas para dibujar un buen diagrama de flujo
1. **Un solo inicio y un solo fin** por algoritmo simple.
2. **Cada símbolo debe tener función clara.** No usar rectángulo para leer ni paralelogramo para calcular.
3. **Las flechas siempre indican dirección.**
4. **Evitar cruces de líneas.** Si hace falta, usar conectores.
5. **Seguir de arriba hacia abajo** o de izquierda a derecha de manera consistente.
6. **Una operación por bloque de proceso** cuando sea posible.
7. **Escribir textos cortos y precisos** dentro de cada símbolo.
8. **Mantener alineación visual** para facilitar lectura rápida.
9. **Verificar la secuencia completa:** inicio → entrada → proceso → salida → fin.
10. **No mezclar etapas.** Leer datos es diferente de calcular resultados.

---

## 5. Pseudocódigo formal con sintaxis PSeInt

### 5.1 Idea general
El pseudocódigo describe el algoritmo con palabras cercanas al lenguaje humano, pero en orden estricto y con sintaxis reconocible por PSeInt.

### 5.2 Estructura básica
```pseint
Proceso NombreDelAlgoritmo
    Definir variable1, variable2, resultado Como Real
    Escribir "Mensaje de entrada"
    Leer variable1
    Escribir "Otro mensaje"
    Leer variable2
    resultado <- formula
    Escribir "Resultado = ", resultado
FinProceso
```

### 5.3 Referencia rápida de palabras clave

| Función didáctica | Forma pedagógica | Sintaxis recomendada en PSeInt | Ejemplo |
|---|---|---|---|
| Comenzar algoritmo | INICIO | `Proceso` o `Algoritmo` | `Proceso CalcularN1` |
| Terminar algoritmo | FIN | `FinProceso` o `FinAlgoritmo` | `FinProceso` |
| Declarar variables | — | `Definir` | `Definir n1 Como Real` |
| Leer entrada | LEER | `Leer` | `Leer disponibles` |
| Mostrar salida | ESCRIBIR | `Escribir` | `Escribir "N1 = ", n1` |
| Asignar valor | ← | `<-` | `n1 <- 85` |
| Comentar | comentario | `//` | `// Calcular ocupación` |

### 5.4 Notas importantes
- En clase hablaremos de **INICIO** y **FIN** porque son conceptos intuitivos.
- En PSeInt, la forma formal más usada es **`Proceso ... FinProceso`**.
- El símbolo **`<-`** significa “asignar” o “guardar en”.
- Los comentarios con `//` no se ejecutan; sirven para explicar.

---

## 6. Tres ejemplos totalmente resueltos

## Ejemplo 1. Calcular N1 para un terapeuta (perspectiva NeuroBiz)

### Problema
Calcular la **tasa de ocupación** de un terapeuta usando sesiones disponibles y realizadas.

### Datos de prueba
- Terapeuta: T01 Ana Ramos
- Sesiones disponibles = 80
- Sesiones realizadas = 68

### Sustitución
**N1 = (68 / 80) × 100 = 85%**

### Diagrama de flujo descrito en texto
```text
(Inicio)
   ↓
/ Leer sesionesDisponibles, sesionesRealizadas /
   ↓
[ n1 <- (sesionesRealizadas / sesionesDisponibles) * 100 ]
   ↓
/ Escribir "N1 = ", n1, "%" /
   ↓
(Fin)
```

### Pseudocódigo PSeInt
```pseint
Proceso Calcular_N1
    Definir sesionesDisponibles, sesionesRealizadas, n1 Como Real
    Escribir "Sesiones disponibles:"
    Leer sesionesDisponibles
    Escribir "Sesiones realizadas:"
    Leer sesionesRealizadas
    n1 <- (sesionesRealizadas / sesionesDisponibles) * 100
    Escribir "N1 = ", n1, "%"
FinProceso
```

### Equivalente Python
```python
sesiones_disponibles = float(input("Sesiones disponibles: "))
sesiones_realizadas = float(input("Sesiones realizadas: "))
n1 = (sesiones_realizadas / sesiones_disponibles) * 100
print(f"N1 = {n1:.1f}%")
```

---

## Ejemplo 2. Calcular U1 para UIB (perspectiva cliente)

### Problema
Calcular la **tasa de uso del contrato** entre UIB y NeuroBiz.

### Datos de prueba
- Sesiones usadas = 142
- Sesiones contratadas = 150

### Sustitución
**U1 = (142 / 150) × 100 = 94.7%**

### Diagrama de flujo descrito en texto
```text
(Inicio)
   ↓
/ Leer sesionesUsadas, sesionesContratadas /
   ↓
[ u1 <- (sesionesUsadas / sesionesContratadas) * 100 ]
   ↓
/ Escribir "U1 = ", u1, "%" /
   ↓
(Fin)
```

### Pseudocódigo PSeInt
```pseint
Proceso Calcular_U1
    Definir sesionesUsadas, sesionesContratadas, u1 Como Real
    Escribir "Sesiones usadas:"
    Leer sesionesUsadas
    Escribir "Sesiones contratadas:"
    Leer sesionesContratadas
    u1 <- (sesionesUsadas / sesionesContratadas) * 100
    Escribir "U1 = ", u1, "%"
FinProceso
```

### Equivalente Python
```python
sesiones_usadas = float(input("Sesiones usadas: "))
sesiones_contratadas = float(input("Sesiones contratadas: "))
u1 = (sesiones_usadas / sesiones_contratadas) * 100
print(f"U1 = {u1:.1f}%")
```

---

## Ejemplo 3. Calcular U2 para UIB (costo por estudiante)

### Problema
Calcular cuánto costó, en promedio, la atención por estudiante atendido en febrero.

### Datos de prueba
- Total pagado = 11.840.000
- Estudiantes únicos = 12

### Sustitución
**U2 = 11.840.000 / 12 = 986.666,67 COP ≈ 986.667 COP**

### Diagrama de flujo descrito en texto
```text
(Inicio)
   ↓
/ Leer totalPagado, estudiantesUnicos /
   ↓
[ u2 <- totalPagado / estudiantesUnicos ]
   ↓
/ Escribir "U2 = $", u2, " COP" /
   ↓
(Fin)
```

### Pseudocódigo PSeInt
```pseint
Proceso Calcular_U2
    Definir totalPagado, estudiantesUnicos, u2 Como Real
    Escribir "Total pagado:"
    Leer totalPagado
    Escribir "Estudiantes únicos atendidos:"
    Leer estudiantesUnicos
    u2 <- totalPagado / estudiantesUnicos
    Escribir "U2 = $", u2, " COP"
FinProceso
```

### Equivalente Python
```python
total_pagado = float(input("Total pagado: "))
estudiantes_unicos = float(input("Estudiantes únicos atendidos: "))
u2 = total_pagado / estudiantes_unicos
print(f"U2 = ${u2:,.2f} COP")
```

---

## 7. Tabla de equivalencias: diagrama ↔ PSeInt ↔ Python

| Elemento del diagrama de flujo | Función | PSeInt | Python equivalente |
|---|---|---|---|
| Óvalo | Inicio / fin | `Proceso ...` / `FinProceso` | Inicio y final del script |
| Paralelogramo | Entrada de datos | `Leer` | `input()` |
| Rectángulo | Proceso / cálculo | `<-` + operación | `=` + operación |
| Paralelogramo | Salida | `Escribir` | `print()` |
| Flecha | Orden de ejecución | orden de líneas | orden de líneas |
| Conector | Continuidad visual | no tiene palabra fija | continuación lógica del código |
| Rombo | Decisión (vista previa) | `Si ... Entonces` | `if` |

**Observación:** aunque el rombo aparece en la tabla, su uso formal se trabajará en la Semana 6.

---

## 8. ¿Por qué los diagramas de flujo ayudan a los estudiantes con dislexia?

### 8.1 Punto científico de partida
La dislexia **no es un problema de inteligencia** y tampoco se explica, principalmente, por “ver letras al revés”. La evidencia sintetizada por **Shaywitz (2003)** muestra que la dislexia es, sobre todo, una dificultad de base **fonológica**: al estudiante le cuesta procesar con rapidez y precisión la relación entre sonidos y símbolos escritos.

Eso significa algo importante para esta asignatura: cuando una explicación depende exclusivamente de texto continuo, lectura lineal y decodificación rápida de instrucciones escritas, algunos estudiantes con dislexia pueden gastar mucha energía en “descifrar” la forma del texto antes de comprender el procedimiento.

### 8.2 Entonces, ¿por qué sí ayudan los diagramas de flujo?
Los diagramas de flujo no “curan” la dislexia ni reemplazan el trabajo con lenguaje. Lo que hacen es **reducir carga de decodificación** y **hacer visible la estructura del proceso**. Esto ayuda por varias razones:

1. **Externalizan la secuencia.**  
   El orden ya no depende solo de una cadena de frases; queda representado con flechas.

2. **Segmentan el problema en bloques cortos.**  
   En vez de leer un párrafo completo, el estudiante procesa un símbolo a la vez.

3. **Combinan lenguaje y apoyo visual.**  
   Un rectángulo con una operación y un paralelogramo con una entrada son pistas visuales inmediatas.

4. **Facilitan memoria de trabajo.**  
   El estudiante no necesita sostener todo el procedimiento “en la cabeza”; puede verlo desplegado.

5. **Favorecen autocorrección.**  
   Si falta una flecha o una salida aparece antes del proceso, el error salta a la vista.

### 8.3 Precisión pedagógica importante
Decir que “la dislexia es visual” sería inexacto. Lo correcto es decir:
- la dificultad central descrita por Shaywitz es fonológica;
- **los apoyos visuales** como diagramas, colores, flechas y bloques ayudan porque disminuyen la exigencia de lectura continua y permiten organizar mejor la información.

### 8.4 Aplicación a TGA04
En esta asignatura conviene ofrecer **doble representación**:
- **Diagrama de flujo** para ver el proceso;
- **Pseudocódigo** para leerlo y escribirlo en forma formal.

Esta doble vía beneficia a toda la clase, no solo a estudiantes con dislexia. También ayuda a estudiantes con TDAH, TDA o altas capacidades que necesitan estructura clara, variación o visión global del problema.

### 8.5 Cómo NeuroBiz usa apoyos visuales en terapia para estudiantes con dislexia
En el caso de NeuroBiz, los apoyos visuales pueden incluir:
- secuencias de pasos con pictogramas o íconos;
- agendas visuales de la sesión terapéutica;
- uso de color para diferenciar entrada, proceso y salida;
- tarjetas con una instrucción por bloque;
- modelos resueltos y luego semirrellenos;
- temporizadores visuales y rutinas previsibles;
- lectura acompañada de verbalización y señalamiento.

En el contexto UIB, esto se traduce en una práctica docente concreta: **mostrar primero el proceso con formas, luego con pseudocódigo y finalmente con Python**. Así se respetan diferentes perfiles de aprendizaje sin bajar el nivel académico.

---

## 9. Recomendaciones prácticas para estudiar esta semana
1. Dibujar primero el flujo en papel.
2. Revisar si tiene exactamente estas etapas: inicio, entrada, proceso, salida, fin.
3. Traducir cada bloque del flujo a una línea de PSeInt.
4. Probar con datos reales de NeuroBiz o UIB.
5. Comparar el resultado con una calculadora.
6. Solo después mirar la versión en Python como anticipo.

---

## 10. Autoevaluación rápida
1. ¿Qué símbolo se usa para **leer datos** en un diagrama de flujo?
2. ¿Qué instrucción de PSeInt corresponde a una **salida** de información?
3. Si UIB usó 142 de 150 sesiones contratadas, ¿cuál es el valor de U1?

---

## 11. Respuestas esperadas de la autoevaluación
1. El **paralelogramo**.
2. `Escribir`.
3. **94.7%**.

---

## 12. Referencias (APA 7.ª ed.)
Cairó Battistutti, O., & Guardati Bueno, S. I. (s. f.). *Metodología de la programación: algoritmos, diagramas de flujo y programas* (3.ª ed.). Alfaomega.

Institución Universitaria de Barranquilla. (2023). *TGA04 Fundamentos de Computación para los Negocios* [Microcurrículo institucional]. Documento interno.

International Organization for Standardization. (1985). *ISO 5807: Information processing—Documentation symbols and conventions for data, program and system flowcharts, program network charts and system resources charts*.

Novara, P. (s. f.). *PSeInt*. https://pseint.sourceforge.net/

Shaywitz, S. E. (2003). *Overcoming dyslexia: A new and complete science-based program for reading problems at any level*. Alfred A. Knopf.
