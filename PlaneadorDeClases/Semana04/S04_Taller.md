# S04 — Taller de Semana 4
## Consolidación RA1: operadores estadísticos, pseudocódigo secuencial y lectura dual NeuroBiz–UIB
### TGA04 Fundamentos de Computación para los Negocios · UIB

**Nombre:** ________________________________________  
**ID:** ____________________________________________  
**Fecha:** _________________________________________  
**Programa:** ______________________________________  
**Sección:** _______________________________________  

---

## Instrucciones generales
- Muestre el procedimiento de todos los cálculos.
- Use porcentajes con **1 o 2 decimales** según convenga.
- En pseudocódigo, use sintaxis tipo **PSeInt**.
- En esta semana la lectura de varios datos se hace **sin ciclos**; si necesita varios datos, léalos secuencialmente.
- Cuando use N4 en las preguntas estadísticas, tome los valores **precalculados de la tabla guía**.

---

## Tabla guía del caso

### A. Terapeutas NeuroBiz
| ID  | Nombre         | Especialidad      | Disp | Real | Cancel | Costo/ses | Satisf | N1 | N4 |
|-----|----------------|-------------------|------|------|--------|-----------|--------|----|----|
| T01 | Ana Ramos      | Psicología        | 80   | 68   | 9      | $87.000   | 4.7    | 85.0% | 11.25% |
| T02 | Carlos Mejía   | Fonoaudiología    | 72   | 71   | 2      | $91.000   | 4.9    | 98.6% | 2.78% |
| T03 | Luz Torres     | T. Ocupacional    | 72   | 54   | 14     | $78.000   | 4.2    | 75.0% | 19.44% |
| T04 | Mario Suárez   | Psicología        | 80   | 77   | 4      | $89.000   | 4.8    | 96.3% | 5.00% |
| T05 | Paula Vega     | Neuropsicología   | 60   | 58   | 1      | $105.000  | 5.0    | 96.7% | 1.67% |
| T06 | Diego Ríos     | Fonoaudiología    | 72   | 43   | 22     | $72.000   | 3.9    | 59.7% | 30.56% |
| T07 | Sandra Ospina  | T. Ocupacional    | 72   | 69   | 5      | $85.000   | 4.6    | 95.8% | 6.94% |
| T08 | Héctor Niño    | Psicología        | 80   | 80   | 0      | $93.000   | 4.8    | 100.0% | 0.00% |

### B. UIB febrero 2026
- Sesiones usadas: **142** de **150** contratadas.
- Total pagado: **$11.840.000 COP**.
- Estudiantes atendidos: **12**.

| ID estudiante | Antes | Después | ¿Mejora ≥ 0.5? |
|---|---:|---:|---|
| E001 | 3.1 | 3.7 | ______ |
| E002 | 2.9 | 3.2 | ______ |
| E003 | 3.8 | 4.1 | ______ |
| E004 | 2.7 | 2.9 | ______ |
| E005 | 4.2 | 4.5 | ______ |
| E006 | 2.5 | 3.0 | ______ |
| E007 | 3.0 | 3.0 | ______ |
| E008 | 3.4 | 3.8 | ______ |
| E009 | 3.2 | 3.6 | ______ |
| E010 | 3.9 | 3.9 | ______ |
| E011 | 2.8 | 3.1 | ______ |
| E012 | 4.0 | 4.3 | ______ |

---

# PARTE 1. Cálculos estadísticos manuales

## Ejercicio 1. Análisis completo de terapeutas
Usando la tabla completa de terapeutas:

a) Calcule **N1 para cada terapeuta**. Muestre para cada uno: fórmula + sustitución + resultado.  
b) Calcule el **promedio de N1** del grupo.  
c) Identifique: **¿cuántos terapeutas tienen N1 ≥ 75%? ¿Cuáles son?**  
d) ¿Quién tiene la **satisfacción más alta** y quién la **más baja**?  
e) Calcule el **promedio de N4** y diga **qué terapeutas superan el umbral del 15%**.

**Espacio de trabajo:**

```text
T01:
T02:
T03:
T04:
T05:
T06:
T07:
T08:

Promedio N1:

Conteo N1 >= 75%:

Satisfacción máxima / mínima:

Promedio N4 y terapeutas sobre 15%:
```

---

## Ejercicio 2. Perspectiva UIB

a) Calcule **U1**.  
b) Calcule **U2**.  
c) Para cada uno de los 12 estudiantes, verifique si la mejora fue **≥ 0.5** y liste quiénes califican.  
d) Calcule **U3**. ¿Está por encima o por debajo del umbral del 60%?  
e) Con base en **U3 = 16.7%**, ¿qué recomendación le haría a la rectoría de UIB?

**Espacio de trabajo:**
```text
U1:
U2:
Estudiantes que califican:
U3:
Recomendación:
```

---

# PARTE 2. Programas en pseudocódigo

## Ejercicio 3. Programa para 4 terapeutas
Escriba pseudocódigo que lea **N1, N4 y satisfacción** para **4 terapeutas** de forma secuencial. El programa debe:
- calcular **suma** y **promedio** de N1,
- contar cuántos tienen **N4 > 15%**,
- imprimir un reporte final.

```pseint
Proceso Ejercicio3






FinProceso
```

---

## Ejercicio 4. Programa UIB para 6 estudiantes
Escriba pseudocódigo que lea la nota **antes** y **después** de **6 estudiantes**. Debe:
- calcular la mejora de cada estudiante,
- contar cuántos tienen mejora **≥ 0.5**,
- calcular **U3**,
- imprimir si el contrato está o no cumpliendo la meta del **60%**.

```pseint
Proceso Ejercicio4






FinProceso
```

---

# PARTE 3. Diagrama de flujo + pseudocódigo

## Ejercicio 5. Satisfacción promedio de 3 terapeutas
Dibuje el **diagrama de flujo** y escriba el **pseudocódigo** para el siguiente problema:
- leer **3** puntuaciones de satisfacción,
- calcular el promedio,
- identificar si el promedio está **por encima de 4.5**,
- imprimir la conclusión.

### Diagrama (descríbalo en texto)
```text
(Inicio) →

→

→

→

(Fin)
```

### Pseudocódigo
```pseint
Proceso Ejercicio5





FinProceso
```

---

# RETO

## Ejercicio 6. Generador de reporte mensual completo
Escriba pseudocódigo para un **generador de reporte mensual de NeuroBiz** que maneje los datos completos de **8 terapeutas**. El reporte debe mostrar:
- promedio de todos los indicadores N usados,
- cantidad de terapeutas en riesgo,
- resumen del contrato UIB,
- recomendación final **CONTINUAR / REVISAR** con base en:

```text
U1 >= 80%  Y  U3 >= 60%  Y  promedio_N1 >= 75%
```

> Este reto se parece al formato del **segundo parcial (semana 10)**: misma lógica de caso organizacional, más variables y más integración.

```pseint
Proceso Ejercicio6_Reto






FinProceso
```

---

# CLAVE DE RESPUESTAS

## Respuesta Ejercicio 1
a) **Cálculo de N1 por terapeuta**
- **T01:** `N1 = (68 / 80) * 100 = 85.0%`
- **T02:** `N1 = (71 / 72) * 100 = 98.6%`
- **T03:** `N1 = (54 / 72) * 100 = 75.0%`
- **T04:** `N1 = (77 / 80) * 100 = 96.3%`
- **T05:** `N1 = (58 / 60) * 100 = 96.7%`
- **T06:** `N1 = (43 / 72) * 100 = 59.7%`
- **T07:** `N1 = (69 / 72) * 100 = 95.8%`
- **T08:** `N1 = (80 / 80) * 100 = 100.0%`

b) **Promedio N1**
```text
(85.0 + 98.6 + 75.0 + 96.3 + 96.7 + 59.7 + 95.8 + 100.0) / 8 = 88.4%
```

c) **N1 ≥ 75%**
- Cantidad: **7 de 8**
- Cumplen: **T01, T02, T03, T04, T05, T07 y T08**

d) **Satisfacción extrema**
- Más alta: **T05 = 5.0**
- Más baja: **T06 = 3.9**

e) **Promedio N4 y umbral**
```text
(11.25 + 2.78 + 19.44 + 5.00 + 1.67 + 30.56 + 6.94 + 0.00) / 8 = 9.7%
```
- Superan 15%: **T03 y T06**

---

## Respuesta Ejercicio 2
- **U1:** `(142 / 150) * 100 = 94.7%`
- **U2:** `$11.840.000 / 12 = $986.667 COP` por estudiante (aprox.)
- **Mejora ≥ 0.5:** solo **E001 (+0.6)** y **E006 (+0.5)**
- **U3:** `(2 / 12) * 100 = 16.7%` → **por debajo** del 60%
- **Recomendación posible:** mantener el contrato porque se usa mucho (U1 alto), pero **revisar la estrategia de intervención académica**, segmentar por perfiles y exigir más seguimiento de resultados a NeuroBiz.

---

## Respuesta Ejercicio 3
```pseint
Proceso Ejercicio3
    Definir n1_1, n1_2, n1_3, n1_4 Como Real
    Definir n4_1, n4_2, n4_3, n4_4 Como Real
    Definir sat_1, sat_2, sat_3, sat_4 Como Real
    Definir sumaN1, promedioN1 Como Real
    Definir contadorN4Alto Como Entero

    sumaN1 <- 0
    contadorN4Alto <- 0

    Leer n1_1, n4_1, sat_1
    Leer n1_2, n4_2, sat_2
    Leer n1_3, n4_3, sat_3
    Leer n1_4, n4_4, sat_4

    sumaN1 <- n1_1 + n1_2 + n1_3 + n1_4
    promedioN1 <- sumaN1 / 4

    Si n4_1 > 15 Entonces contadorN4Alto <- contadorN4Alto + 1 FinSi
    Si n4_2 > 15 Entonces contadorN4Alto <- contadorN4Alto + 1 FinSi
    Si n4_3 > 15 Entonces contadorN4Alto <- contadorN4Alto + 1 FinSi
    Si n4_4 > 15 Entonces contadorN4Alto <- contadorN4Alto + 1 FinSi

    Escribir "Suma N1 = ", sumaN1
    Escribir "Promedio N1 = ", promedioN1
    Escribir "Cantidad con N4 > 15 = ", contadorN4Alto
FinProceso
```

---

## Respuesta Ejercicio 4
```pseint
Proceso Ejercicio4
    Definir a1, a2, a3, a4, a5, a6 Como Real
    Definir d1, d2, d3, d4, d5, d6 Como Real
    Definir m1, m2, m3, m4, m5, m6 Como Real
    Definir mejoran Como Entero
    Definir u3 Como Real

    mejoran <- 0
    Leer a1, d1
    Leer a2, d2
    Leer a3, d3
    Leer a4, d4
    Leer a5, d5
    Leer a6, d6

    m1 <- d1 - a1
    m2 <- d2 - a2
    m3 <- d3 - a3
    m4 <- d4 - a4
    m5 <- d5 - a5
    m6 <- d6 - a6

    Si m1 >= 0.5 Entonces mejoran <- mejoran + 1 FinSi
    Si m2 >= 0.5 Entonces mejoran <- mejoran + 1 FinSi
    Si m3 >= 0.5 Entonces mejoran <- mejoran + 1 FinSi
    Si m4 >= 0.5 Entonces mejoran <- mejoran + 1 FinSi
    Si m5 >= 0.5 Entonces mejoran <- mejoran + 1 FinSi
    Si m6 >= 0.5 Entonces mejoran <- mejoran + 1 FinSi

    u3 <- (mejoran / 6) * 100
    Escribir "U3 = ", u3, "%"
    Escribir "¿Cumple meta del 60%?: ", u3 >= 60
FinProceso
```

---

## Respuesta Ejercicio 5
**Diagrama textual posible:**
```text
(Inicio)
    ↓
/ Leer s1, s2, s3 /
    ↓
[ promedio <- (s1 + s2 + s3) / 3 ]
    ↓
/ Escribir promedio /
    ↓
[ conclusion <- promedio > 4.5 ]
    ↓
/ Escribir conclusion /
    ↓
(Fin)
```

**Pseudocódigo posible:**
```pseint
Proceso Ejercicio5
    Definir s1, s2, s3, promedio Como Real
    Definir conclusion Como Logico
    Leer s1, s2, s3
    promedio <- (s1 + s2 + s3) / 3
    conclusion <- promedio > 4.5
    Escribir "Promedio = ", promedio
    Escribir "¿Promedio superior a 4.5?: ", conclusion
FinProceso
```

---

## Respuesta Ejercicio 6 (una solución posible)
```pseint
Proceso Ejercicio6_Reto
    Definir promedioN1, promedioN4, u1, u2, u3 Como Real
    Definir riesgo Como Entero
    Definir recomendacion Como Cadena
    // Leer N1 y N4 de 8 terapeutas, acumular, calcular promedios y contar riesgo
    // Leer datos UIB: sesiones usadas, contratadas, total pagado, estudiantes, mejoran
    u1 <- (sesionesUsadas / sesionesContratadas) * 100
    u2 <- totalPagado / estudiantes
    u3 <- (mejoran / estudiantes) * 100

    Si u1 >= 80 Y u3 >= 60 Y promedioN1 >= 75 Entonces
        recomendacion <- "CONTINUAR"
    SiNo
        recomendacion <- "REVISAR"
    FinSi

    Escribir "Promedio N1: ", promedioN1
    Escribir "Promedio N4: ", promedioN4
    Escribir "Terapeutas en riesgo: ", riesgo
    Escribir "U1: ", u1
    Escribir "U2: ", u2
    Escribir "U3: ", u3
    Escribir "Recomendacion: ", recomendacion
FinProceso
```

**Criterios mínimos para darla por correcta:**
- integra proveedor y cliente,
- usa promedios y conteos,
- emite una recomendación final sustentada,
- mantiene estructura clara de entrada → proceso → salida.
