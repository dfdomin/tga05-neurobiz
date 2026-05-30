# S05 — Primer Parcial
## TGA04 Fundamentos de Computación para los Negocios · UIB
### Caso: TerapiaSer S.A.S. + PlástiCor S.A.

**Nombre:** ________________________________________  
**ID:** ____________________________________________  
**Fecha:** _________________________________________  
**Programa:** ______________________________________  
**Sección:** _______________________________________  
**Grupo:** _________________________________________  

**Duración sugerida:** 90 minutos  
**Modalidad:** individual  
**Material permitido:** lapicero, lápiz, borrador, calculadora básica no programable  
**Indicaciones:** muestre procedimiento, use rótulos claros y escriba pseudocódigo en estilo PSeInt. No se requieren ciclos.

---

## CASO DE ESTUDIO

**TerapiaSer S.A.S.** presta servicios de terapia ocupacional y psicológica a empleados de **PlástiCor S.A.** mediante un contrato B2B. Debe analizarse el caso desde dos perspectivas:
- **Proveedor:** TerapiaSer
- **Cliente:** PlástiCor

### Tabla de terapeutas
| Terapeuta | Sesiones disponibles | Sesiones realizadas | Sesiones canceladas | Costo por sesión | Satisfacción |
|---|---:|---:|---:|---:|---:|
| Camila | 60 | 52 | 7 | $85.000 | 4.5 |
| Rodrigo | 48 | 47 | 1 | $92.000 | 4.8 |
| Natalia | 60 | 41 | 16 | $74.000 | 3.8 |
| Fernando | 48 | 45 | 3 | $88.000 | 4.7 |
| Valentina | 40 | 40 | 0 | $96.000 | 5.0 |

### Contrato PlástiCor
- Sesiones contratadas al mes: **100**
- Empleados atendidos este mes: **18**
- Pago mensual a TerapiaSer: **$8.500.000**
- Uso real del mes: **18 empleados × 3 sesiones promedio = 54 sesiones usadas**
- Empleados con mejora documentada: **10 de 18**

### Convención operativa para este parcial
Para evitar ambigüedad en el indicador de ausentismo, use en este examen:

```text
N4 = (Sesiones canceladas / Sesiones disponibles) × 100
```

---

# PARTE 1 — Teoría y clasificación (25 puntos)

## Ejercicio 1 (8 pts)
Clasifique cada ítem como **Dato / Información / No corresponde**. Justifique brevemente.

| Ítem | Clasificación | Justificación breve |
|---|---|---|
| 1. “Camila” | __________ | ______________________________ |
| 2. “60 sesiones disponibles” | __________ | ______________________________ |
| 3. “Rodrigo tuvo N1 = 97.9%” | __________ | ______________________________ |
| 4. “$8.500.000 pagados en el mes” | __________ | ______________________________ |
| 5. “Natalia presenta riesgo operativo” | __________ | ______________________________ |
| 6. “18 empleados fueron atendidos” | __________ | ______________________________ |
| 7. “La oficina de Fernando tiene una ventana grande” | __________ | ______________________________ |
| 8. “Valentina alcanzó 100% de ocupación” | __________ | ______________________________ |
| 9. “10 de 18 empleados mejoraron” | __________ | ______________________________ |
| 10. “El color favorito de Rodrigo es azul” | __________ | ______________________________ |
| 11. “El contrato está subutilizado porque U1 = 54%” | __________ | ______________________________ |
| 12. “Natalia canceló muchas sesiones frente al resto” | __________ | ______________________________ |

---

## Ejercicio 2 (10 pts)
Complete la tabla con el **nombre de la variable**, su **tipo** y los **operadores que aplican**.

| Variable | Tipo (entera / real / alfanumérica / lógica) | Operadores que aplican |
|---|---|---|
| nombreTerapeuta | __________ | __________ |
| sesionesDisponibles | __________ | __________ |
| sesionesRealizadas | __________ | __________ |
| sesionesCanceladas | __________ | __________ |
| costoSesion | __________ | __________ |
| satisfaccion | __________ | __________ |
| sesionesUsadas | __________ | __________ |
| contratoUsoAdecuado | __________ | __________ |

---

## Ejercicio 3 (7 pts)
Identifique todos los operadores (tipo y nombre) que aparecen en las fórmulas:

- `N1 = (Sesiones realizadas / Sesiones disponibles) × 100`
- `N4 = (Sesiones canceladas / Sesiones disponibles) × 100`
- `U1 = (Sesiones usadas / Sesiones contratadas) × 100`
- `U2 = Total pagado / Empleados atendidos`

**Respuesta:**
```text
Operadores matemáticos:

Operadores de agrupación:

¿Hay operadores relacionales o lógicos dentro de estas fórmulas base?:
```

---

# PARTE 2 — Diseño algorítmico: estructura secuencial (40 puntos)

## Ejercicio 4 (20 pts)
Con los datos de **Rodrigo** (`48 disponibles, 47 realizadas, 1 cancelada`):

a) **(12 pts)** Escriba pseudocódigo en notación **PSeInt** que lea los datos, calcule e imprima **N1** y **N4** con etiquetas descriptivas.  
b) **(8 pts)** Describa el diagrama de flujo del mismo programa usando símbolos estándar: **óvalo, paralelogramo, rectángulo y flechas**.

```pseint
Proceso Ejercicio4





FinProceso
```

**Diagrama textual:**
```text
(Inicio) →

→

→

→

(Fin)
```

---

## Ejercicio 5 (20 pts)
Desde la perspectiva de **PlástiCor**, escriba pseudocódigo que lea:
- sesiones contratadas,
- sesiones usadas,
- pago mensual total,
- número de empleados atendidos.

El programa debe calcular e imprimir:
- **U1**,
- **U2**,
- y una evaluación lógica: **¿el uso del contrato está por encima del 80%?** (imprima `VERDADERO` o `FALSO`).

```pseint
Proceso Ejercicio5





FinProceso
```

---

# PARTE 3 — Análisis estadístico (35 puntos)

## Ejercicio 6 (35 pts)
Usando la tabla completa de los **5 terapeutas** de TerapiaSer, escriba un programa completo en pseudocódigo que:

a) Lea los datos de los **5 terapeutas** de forma secuencial (**LEER** para cada uno; no se requieren ciclos).  
b) Calcule **N1** para cada terapeuta.  
c) Acumule la suma y calcule el **promedio N1**.  
d) Identifique, usando operadores relacionales y lógicos, qué terapeutas están en riesgo por cumplir:  

```text
N1 < 75%  O  N4 > 20%
```

e) Cuente cuántos terapeutas están en riesgo.  
f) Imprima un reporte completo con:
- todos los valores de N1,
- promedio N1,
- cantidad en riesgo,
- nombre del terapeuta con el **N1 más alto**.

```pseint
Proceso Ejercicio6






FinProceso
```

---

## Rúbrica de calificación (alineada a RA3)
- **25%**: identifica variables significativas y las describe con herramientas de mejora continua.
- **35%**: formula problemas complejos con variables medibles y alcanzables.
- **40%**: diseña la solución con estructura y pertinencia.

---

# CLAVE DE RESPUESTAS — VERSIÓN DOCENTE
> **Retire esta sección en la copia del estudiante.**

## Resultados numéricos base
- **N1 Camila:** `(52 / 60) * 100 = 86.7%`
- **N1 Rodrigo:** `(47 / 48) * 100 = 97.9%`
- **N1 Natalia:** `(41 / 60) * 100 = 68.3%`
- **N1 Fernando:** `(45 / 48) * 100 = 93.8%`
- **N1 Valentina:** `(40 / 40) * 100 = 100.0%`

- **N4 Camila:** `(7 / 60) * 100 = 11.67%`
- **N4 Rodrigo:** `(1 / 48) * 100 = 2.08%`
- **N4 Natalia:** `(16 / 60) * 100 = 26.67%`
- **N4 Fernando:** `(3 / 48) * 100 = 6.25%`
- **N4 Valentina:** `(0 / 40) * 100 = 0.00%`

- **Promedio N1:** `(86.7 + 97.9 + 68.3 + 93.8 + 100.0) / 5 = 89.3%` (aprox.)
- **En riesgo:** solo **Natalia**
- **Cantidad en riesgo:** **1**
- **Mayor N1:** **Valentina (100%)**
- **U1:** `(54 / 100) * 100 = 54%`
- **U2:** `$8.500.000 / 18 = $472.222` por empleado (aprox.)
- **U3:** `(10 / 18) * 100 = 55.6%`

---

## Clave Ejercicio 1

| Ítem | Clasificación esperada | Justificación breve |
|---|---|---|
| 1 | Dato | Es un nombre aislado, sin análisis. |
| 2 | Dato | Es un valor puntual del caso. |
| 3 | Información | Ya es un indicador calculado e interpretado. |
| 4 | Dato | Es un valor bruto de entrada. |
| 5 | Información | Es una conclusión sobre desempeño. |
| 6 | Dato | Cantidad observada del mes. |
| 7 | No corresponde | No aporta al análisis del contrato ni de los indicadores. |
| 8 | Información | Resume el cálculo de ocupación. |
| 9 | Información | Ya expresa un resultado agregado relevante. |
| 10 | No corresponde | No es útil para el problema planteado. |
| 11 | Información | Interpreta U1 frente a un umbral. |
| 12 | Información | Compara e interpreta la frecuencia de cancelaciones. |

---

## Clave Ejercicio 2

| Variable | Tipo | Operadores que aplican |
|---|---|---|
| nombreTerapeuta | Alfanumérica | asignación, salida |
| sesionesDisponibles | Entera | matemáticos, relacionales, estadísticos |
| sesionesRealizadas | Entera | matemáticos, relacionales, estadísticos |
| sesionesCanceladas | Entera | matemáticos, relacionales, estadísticos |
| costoSesion | Real | matemáticos, relacionales, estadísticos |
| satisfaccion | Real | matemáticos, relacionales, estadísticos |
| sesionesUsadas | Entera | matemáticos, relacionales, estadísticos |
| contratoUsoAdecuado | Lógica | lógicos, relacionales, asignación |

---

## Clave Ejercicio 3
- **Operadores matemáticos:** división (`/`) y multiplicación (`*` o `×`).
- **Operadores de agrupación:** paréntesis `(` `)`.
- **Operadores relacionales o lógicos en las fórmulas base:** **no**; aparecen cuando se comparan resultados con umbrales, no dentro de la fórmula original.

---

## Clave Ejercicio 4

### Pseudocódigo esperado
```pseint
Proceso Ejercicio4
    Definir disponibles, realizadas, canceladas, n1, n4 Como Real
    Escribir "Sesiones disponibles:"
    Leer disponibles
    Escribir "Sesiones realizadas:"
    Leer realizadas
    Escribir "Sesiones canceladas:"
    Leer canceladas
    n1 <- (realizadas / disponibles) * 100
    n4 <- (canceladas / disponibles) * 100
    Escribir "N1 de Rodrigo = ", n1, "%"
    Escribir "N4 de Rodrigo = ", n4, "%"
FinProceso
```

### Flujo textual esperado
```text
(Inicio)
    ↓
/ Leer disponibles, realizadas, canceladas /
    ↓
[ n1 <- (realizadas / disponibles) * 100 ]
    ↓
[ n4 <- (canceladas / disponibles) * 100 ]
    ↓
/ Escribir "N1..." y "N4..." /
    ↓
(Fin)
```

---

## Clave Ejercicio 5
```pseint
Proceso Ejercicio5
    Definir contratadas, usadas, pago, empleados, u1, u2 Como Real
    Definir usoAdecuado Como Logico
    Leer contratadas
    Leer usadas
    Leer pago
    Leer empleados
    u1 <- (usadas / contratadas) * 100
    u2 <- pago / empleados
    usoAdecuado <- u1 > 80
    Escribir "U1 = ", u1, "%"
    Escribir "U2 = $", u2
    Escribir "¿Uso del contrato > 80%?: ", usoAdecuado
FinProceso
```

---

## Clave Ejercicio 6
```pseint
Proceso Ejercicio6
    Definir nombre1, nombre2, nombre3, nombre4, nombre5 Como Cadena
    Definir disp1, disp2, disp3, disp4, disp5 Como Real
    Definir real1, real2, real3, real4, real5 Como Real
    Definir canc1, canc2, canc3, canc4, canc5 Como Real
    Definir n11, n12, n13, n14, n15 Como Real
    Definir n41, n42, n43, n44, n45 Como Real
    Definir sumaN1, promedioN1, maxN1 Como Real
    Definir contadorRiesgo Como Entero
    Definir nombreMax Como Cadena

    sumaN1 <- 0
    contadorRiesgo <- 0

    Leer nombre1, disp1, real1, canc1
    Leer nombre2, disp2, real2, canc2
    Leer nombre3, disp3, real3, canc3
    Leer nombre4, disp4, real4, canc4
    Leer nombre5, disp5, real5, canc5

    n11 <- (real1 / disp1) * 100
    n12 <- (real2 / disp2) * 100
    n13 <- (real3 / disp3) * 100
    n14 <- (real4 / disp4) * 100
    n15 <- (real5 / disp5) * 100

    n41 <- (canc1 / disp1) * 100
    n42 <- (canc2 / disp2) * 100
    n43 <- (canc3 / disp3) * 100
    n44 <- (canc4 / disp4) * 100
    n45 <- (canc5 / disp5) * 100

    sumaN1 <- n11 + n12 + n13 + n14 + n15
    promedioN1 <- sumaN1 / 5

    maxN1 <- n11
    nombreMax <- nombre1
    Si n12 > maxN1 Entonces
        maxN1 <- n12
        nombreMax <- nombre2
    FinSi
    Si n13 > maxN1 Entonces
        maxN1 <- n13
        nombreMax <- nombre3
    FinSi
    Si n14 > maxN1 Entonces
        maxN1 <- n14
        nombreMax <- nombre4
    FinSi
    Si n15 > maxN1 Entonces
        maxN1 <- n15
        nombreMax <- nombre5
    FinSi

    Si n11 < 75 O n41 > 20 Entonces contadorRiesgo <- contadorRiesgo + 1 FinSi
    Si n12 < 75 O n42 > 20 Entonces contadorRiesgo <- contadorRiesgo + 1 FinSi
    Si n13 < 75 O n43 > 20 Entonces contadorRiesgo <- contadorRiesgo + 1 FinSi
    Si n14 < 75 O n44 > 20 Entonces contadorRiesgo <- contadorRiesgo + 1 FinSi
    Si n15 < 75 O n45 > 20 Entonces contadorRiesgo <- contadorRiesgo + 1 FinSi

    Escribir "N1 Camila = ", n11
    Escribir "N1 Rodrigo = ", n12
    Escribir "N1 Natalia = ", n13
    Escribir "N1 Fernando = ", n14
    Escribir "N1 Valentina = ", n15
    Escribir "Promedio N1 = ", promedioN1
    Escribir "Cantidad en riesgo = ", contadorRiesgo
    Escribir "Mayor N1 = ", nombreMax, " con ", maxN1, "%"
FinProceso
```

**Se acepta cualquier variante equivalente** que:
- lea los 5 casos de forma secuencial,
- calcule N1 correctamente,
- identifique riesgo con `N1 < 75 O N4 > 20`,
- cuente los casos en riesgo,
- y nombre a **Valentina** como mayor N1.

---

## Aplicación de rúbrica por ejercicio

| Ejercicio | Criterio RA3 dominante | Evidencia esperada |
|---|---|---|
| 1 | Identifica variables significativas | Distingue dato, información y pertinencia |
| 2 | Identifica variables significativas | Tipifica y asocia operadores adecuados |
| 3 | Formula problemas con variables medibles | Reconoce qué operaciones componen cada indicador |
| 4 | Diseña solución con estructura | Presenta secuencia entrada–proceso–salida coherente |
| 5 | Diseña solución con estructura | Traduce la perspectiva cliente a pseudocódigo funcional |
| 6 | Formula y diseña solución completa | Integra cálculo, comparación, conteo y reporte final |
