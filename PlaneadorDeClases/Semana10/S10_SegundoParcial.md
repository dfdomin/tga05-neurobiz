# S10 — Segundo Parcial
## TGA04 Fundamentos de Computación para los Negocios · UIB
### Caso: **ApoyaNov S.A.S.** + **Cementos Norte S.A.**

**Nombre:** ________________________________________  
**ID:** ____________________________________________  
**Fecha:** _________________________________________  
**Programa:** ______________________________________  
**Sección:** _______________________________________  
**Grupo:** _________________________________________  

**Duración:** 90 minutos  
**Modalidad:** individual  
**Material permitido:** lápiz, lapicero, borrador, calculadora básica no programable  
**Indicaciones generales:** muestre procedimiento, escriba pseudocódigo en estilo **PSeInt**, rotule bien sus resultados y lea con cuidado los umbrales. **No necesita materiales previos:** este enunciado trae fórmulas, datos y criterios necesarios.

---

## 1. Caso de estudio

**ApoyaNov S.A.S.** es una empresa que presta servicios psicopedagógicos y de acompañamiento a trabajadores de compañías industriales. Uno de sus clientes es **Cementos Norte S.A.**, empresa que contrató atención mensual para sus empleados.

En este parcial usted analizará dos niveles:
- **Nivel proveedor (ApoyaNov):** desempeño individual de los terapeutas.
- **Nivel cliente (Cementos Norte):** uso y efectividad general del contrato.

### Tabla del equipo de terapeutas de ApoyaNov
| Terapeuta | Disponibles/mes | Realizadas | Canceladas | Costo/sesión | Satisfacción |
|---|---:|---:|---:|---:|---:|
| Laura Campos | 65 | 58 | 6 | $88.000 | 4.6 |
| Andrés Peñaloza | 50 | 48 | 1 | $95.000 | 4.9 |
| Marcela Suárez | 65 | 44 | 18 | $79.000 | 3.7 |
| Óscar Villanueva | 55 | 54 | 1 | $91.000 | 4.8 |
| Daniela Ríos | 45 | 45 | 0 | $102.000 | 5.0 |
| Javier Montoya | 60 | 39 | 17 | $76.000 | 3.5 |

### Datos del contrato con Cementos Norte
- Sesiones contratadas por mes: **120**
- Empleados cubiertos: **15**
- Pago mensual del contrato: **$10.200.000 COP**
- Sesiones usadas por los empleados este mes: **15 empleados × 8 sesiones promedio = 120 sesiones**
- Empleados con mejora documentada: **7 de 15**

> **Nota importante para evitar confusión:** la **tabla de terapeutas** se usa para analizar el desempeño del equipo de ApoyaNov (Partes 2 y 3). Para los indicadores del **contrato** use solo los datos del bloque “Datos del contrato con Cementos Norte”.

---

## 2. Indicadores y umbrales que debe usar en este examen

### Indicadores del proveedor
- `N1 = (realizadas / disponibles) × 100`  → cumple si **N1 ≥ 75%**
- `N4 = (canceladas / disponibles) × 100` → cumple si **N4 ≤ 15%**

### Indicadores del cliente
- `U1 = (sesiones usadas / sesiones contratadas) × 100` → cumple si **U1 ≥ 80%**
- `U3 = (empleados con mejora / total empleados) × 100` → cumple si **U3 ≥ 60%**

### Interpretación para la Parte 2
Use esta clasificación del estado del terapeuta:
- **VERDE:** cumple ambos umbrales (`N1 ≥ 75` y `N4 ≤ 15`)
- **AMARILLO:** cumple solo uno de los dos umbrales
- **ROJO:** no cumple ninguno de los dos umbrales

> Ejemplo de AMARILLO: un terapeuta con `N1 = 82%` y `N4 = 18%` cumple solo un umbral.

---

# PARTE 1 — Teoría y clasificación (25 puntos)

## Ejercicio 1 (9 pts)
Clasifique cada ítem como **Dato / Información / No corresponde**. Justifique brevemente.

| Ítem | Clasificación | Justificación breve |
|---|---|---|
| 1. “Laura Campos” | __________ | ______________________________ |
| 2. “65 sesiones disponibles” | __________ | ______________________________ |
| 3. “Marcela presenta riesgo operativo porque su N1 está por debajo de 75%” | __________ | ______________________________ |
| 4. “$10.200.000 COP de pago mensual” | __________ | ______________________________ |
| 5. “U3 = 46.7%, por tanto el contrato no alcanza el umbral de mejora” | __________ | ______________________________ |
| 6. “El color favorito de Javier Montoya es azul” | __________ | ______________________________ |
| 7. “120 sesiones usadas por empleados” | __________ | ______________________________ |
| 8. “Daniela cumple completamente los dos umbrales del proveedor” | __________ | ______________________________ |
| 9. “La oficina principal de ApoyaNov queda cerca a un parque” | __________ | ______________________________ |

---

## Ejercicio 2 (10 pts)
Complete la tabla con el **tipo de variable** y los **operadores que aplican principalmente**.

| Variable | Tipo (entera / real / alfanumérica / lógica) | Operadores que aplican |
|---|---|---|
| nombreTerapeuta | __________ | __________ |
| sesionesRealizadas | __________ | __________ |
| costoSesion | __________ | __________ |
| u3 | __________ | __________ |
| estadoTerapeuta | __________ | __________ |

---

## Ejercicio 3 (6 pts)
Responda:

1. En las fórmulas de `N1` y `U3`, ¿qué **operadores matemáticos** aparecen?  
   **Respuesta:** __________________________________________
2. ¿Qué **símbolos de agrupación** aparecen en esas fórmulas?  
   **Respuesta:** __________________________________________
3. Escriba una **expresión relacional** para verificar si un terapeuta cumple `N1`.  
   **Respuesta:** __________________________________________
4. Escriba una **expresión lógica compuesta** para verificar si un terapeuta está en **VERDE**.  
   **Respuesta:** __________________________________________

---

# PARTE 2 — Pseudocódigo selectivo (35 puntos)

## Ejercicio 4 (35 pts)
Escriba pseudocódigo en notación **PSeInt** que:
1. Lea `nombre`, `disponibles`, `realizadas` y `canceladas` de **un terapeuta**.
2. Calcule `N1` y `N4`.
3. Clasifique el estado del terapeuta como **VERDE**, **AMARILLO** o **ROJO** usando **SI-SINO-FSI**.
4. Imprima:
   - nombre del terapeuta,
   - valor de `N1`,
   - valor de `N4`,
   - estado final,
   - y un mensaje apropiado.

Use estos mensajes:
- **VERDE:** `"Operación estable"`
- **AMARILLO:** `"Revisar uno de los indicadores"`
- **ROJO:** `"Alerta: revisar ocupación y cancelaciones"`

```pseint
Proceso Ejercicio4






FinProceso
```

---

# PARTE 3 — Pseudocódigo repetitivo (40 puntos)

## Ejercicio 5 (40 pts)
Escriba un pseudocódigo que procese los **6 terapeutas** de la tabla usando una estructura repetitiva.

Puede usar **PARA-FPARA** o **MQ-FMQ**. Como la cantidad de terapeutas ya es conocida (6), la opción más directa suele ser **PARA-FPARA**.

Su algoritmo debe:
1. Leer en cada iteración: `nombre`, `disponibles`, `realizadas` y `canceladas`.
2. Calcular `N1` de cada terapeuta.
3. Acumular la **suma total de sesiones realizadas**.
4. Acumular la suma de `N1` para luego calcular el **promedio N1** del equipo.
5. Identificar el **terapeuta con menor N1**.
6. Imprimir al final:
   - total de sesiones realizadas,
   - promedio N1,
   - nombre del terapeuta con menor N1,
   - y el valor de ese menor N1.

**No se requieren arreglos o vectores.** Puede leer los datos uno por uno dentro del ciclo.

```pseint
Proceso Ejercicio5







FinProceso
```

---

## Rúbrica de calificación (alineada a RA3 institucional)

| Criterio RA3 | Evidencia en este parcial | Peso |
|---|---|---:|
| **Criterio 1**: Identifica variables significativas | Parte 1 + identificación inicial de variables en Parte 2 | 25% |
| **Criterio 2**: Formula problemas complejos con variables medibles | Parte 2: clasificación del estado del terapeuta con umbrales | 35% |
| **Criterio 3**: Diseña la solución a través de modelos | Parte 3: ciclo, acumulación, promedio y mínimo | 40% |

---

# CLAVE DOCENTE — RETIRAR EN LA COPIA DEL ESTUDIANTE

## 1. Valores correctos del caso

### Indicadores del proveedor (ApoyaNov)
- **Laura Campos:** `N1 = (58 / 65) × 100 = 89.2%` ✅ · `N4 = (6 / 65) × 100 = 9.2%` ✅ · **Estado: VERDE**
- **Andrés Peñaloza:** `N1 = (48 / 50) × 100 = 96.0%` ✅ · `N4 = (1 / 50) × 100 = 2.0%` ✅ · **Estado: VERDE**
- **Marcela Suárez:** `N1 = (44 / 65) × 100 = 67.7%` 🔴 · `N4 = (18 / 65) × 100 = 27.7%` 🔴 · **Estado: ROJO**
- **Óscar Villanueva:** `N1 = (54 / 55) × 100 = 98.2%` ✅ · `N4 = (1 / 55) × 100 = 1.8%` ✅ · **Estado: VERDE**
- **Daniela Ríos:** `N1 = (45 / 45) × 100 = 100.0%` ✅ · `N4 = (0 / 45) × 100 = 0.0%` ✅ · **Estado: VERDE**
- **Javier Montoya:** `N1 = (39 / 60) × 100 = 65.0%` 🔴 · `N4 = (17 / 60) × 100 = 28.3%` 🔴 · **Estado: ROJO**

### Totales del equipo
- **Total sesiones realizadas:** `58 + 48 + 44 + 54 + 45 + 39 = 288`
- **Promedio N1 del equipo:** `(89.2 + 96.0 + 67.7 + 98.2 + 100.0 + 65.0) / 6 = 86.0%` (aprox.)
- **Menor N1:** **Javier Montoya = 65.0%**

### Indicadores del cliente (Cementos Norte)
- **U1:** `(120 / 120) × 100 = 100.0%` ✅
- **U3:** `(7 / 15) × 100 = 46.7%` 🔴

**Nota docente de consistencia:** para `U1` use únicamente las **120 sesiones usadas por empleados del contrato**. La suma `288` corresponde al volumen mensual del equipo de ApoyaNov y no debe mezclarse con el uso contractual de Cementos Norte.

---

## 2. Clave Parte 1

### Ejercicio 1
| Ítem | Clasificación esperada | Justificación breve |
|---|---|---|
| 1 | Dato | Es un nombre aislado del caso. |
| 2 | Dato | Es un valor puntual de entrada. |
| 3 | Información | Ya interpreta un indicador frente a un umbral. |
| 4 | Dato | Es un valor bruto del contrato. |
| 5 | Información | Es un cálculo interpretado del contrato. |
| 6 | No corresponde | No aporta al análisis del problema ni a los indicadores. |
| 7 | Dato | Es una cantidad puntual usada en el contrato. |
| 8 | Información | Resume el cumplimiento de dos umbrales. |
| 9 | No corresponde | No aporta al análisis solicitado. |

### Ejercicio 2
| Variable | Tipo esperado | Operadores que aplican principalmente |
|---|---|---|
| nombreTerapeuta | Alfanumérica | asignación, entrada/salida |
| sesionesRealizadas | Entera | matemáticos, relacionales, estadísticos |
| costoSesion | Real | matemáticos, relacionales, estadísticos |
| u3 | Real | matemáticos, relacionales |
| estadoTerapeuta | Alfanumérica | asignación, comparación, salida |

### Ejercicio 3
1. **Operadores matemáticos:** división (`/`) y multiplicación (`*` o `×`).
2. **Símbolos de agrupación:** paréntesis `(` `)`.
3. **Expresión relacional válida:** `n1 >= 75`
4. **Expresión lógica compuesta válida:** `n1 >= 75 Y n4 <= 15`

---

## 3. Solución esperada Parte 2 (selectiva)

### Pseudocódigo modelo
```pseint
Proceso Ejercicio4
    Definir nombre, estado, mensaje Como Cadena
    Definir disponibles, realizadas, canceladas, n1, n4 Como Real

    Escribir "Nombre del terapeuta:"
    Leer nombre
    Escribir "Sesiones disponibles:"
    Leer disponibles
    Escribir "Sesiones realizadas:"
    Leer realizadas
    Escribir "Sesiones canceladas:"
    Leer canceladas

    n1 <- (realizadas / disponibles) * 100
    n4 <- (canceladas / disponibles) * 100

    Si n1 >= 75 Y n4 <= 15 Entonces
        estado <- "VERDE"
        mensaje <- "Operación estable"
    SiNo
        Si (n1 >= 75 Y n4 > 15) O (n1 < 75 Y n4 <= 15) Entonces
            estado <- "AMARILLO"
            mensaje <- "Revisar uno de los indicadores"
        SiNo
            estado <- "ROJO"
            mensaje <- "Alerta: revisar ocupación y cancelaciones"
        FinSi
    FinSi

    Escribir "Terapeuta: ", nombre
    Escribir "N1 = ", n1, "%"
    Escribir "N4 = ", n4, "%"
    Escribir "Estado = ", estado
    Escribir mensaje
FinProceso
```

### Criterios de calificación del Ejercicio 4 (35 pts)
| Aspecto | Puntos |
|---|---:|
| Variables y entradas correctas | 5 |
| Fórmulas correctas de `N1` y `N4` | 8 |
| Lógica correcta de VERDE / AMARILLO / ROJO | 12 |
| Salidas rotuladas y mensaje final | 5 |
| Orden, sintaxis legible y estructura SI-SINO-FSI | 5 |

---

## 4. Solución esperada Parte 3 (repetitiva)

### Pseudocódigo modelo con PARA-FPARA
```pseint
Proceso Ejercicio5
    Definir i Como Entero
    Definir nombre, nombreMenorN1 Como Cadena
    Definir disponibles, realizadas, canceladas, n1 Como Real
    Definir sumaRealizadas, sumaN1, promedioN1, menorN1 Como Real

    sumaRealizadas <- 0
    sumaN1 <- 0
    menorN1 <- 999
    nombreMenorN1 <- ""

    Para i <- 1 Hasta 6 Hacer
        Escribir "Nombre del terapeuta:"
        Leer nombre
        Escribir "Sesiones disponibles:"
        Leer disponibles
        Escribir "Sesiones realizadas:"
        Leer realizadas
        Escribir "Sesiones canceladas:"
        Leer canceladas

        n1 <- (realizadas / disponibles) * 100
        sumaRealizadas <- sumaRealizadas + realizadas
        sumaN1 <- sumaN1 + n1

        Si n1 < menorN1 Entonces
            menorN1 <- n1
            nombreMenorN1 <- nombre
        FinSi
    FinPara

    promedioN1 <- sumaN1 / 6

    Escribir "Total realizadas = ", sumaRealizadas
    Escribir "Promedio N1 = ", promedioN1, "%"
    Escribir "Menor N1 = ", nombreMenorN1
    Escribir "Valor menor N1 = ", menorN1, "%"
FinProceso
```

### Resultados esperados al usar la tabla dada
- `Total realizadas = 288`
- `Promedio N1 ≈ 86.0%`
- `Menor N1 = Javier Montoya`
- `Valor menor N1 = 65.0%`

### Criterios de calificación del Ejercicio 5 (40 pts)
| Aspecto | Puntos |
|---|---:|
| Inicialización correcta de acumuladores y mínimo | 6 |
| Uso correcto de estructura repetitiva | 10 |
| Cálculo y acumulación de total realizadas | 8 |
| Cálculo de promedio N1 | 8 |
| Identificación correcta del terapeuta con menor N1 | 8 |

---

## 5. Síntesis de evaluación por RA3

| Criterio institucional | Evidencia concreta | Puntos / peso |
|---|---|---:|
| **Criterio 1**: identifica variables significativas | Clasificación de datos, tipificación de variables, operadores y entradas de la Parte 2 | 25 pts / 25% |
| **Criterio 2**: formula problemas complejos con variables medibles | Construcción del algoritmo selectivo con umbrales y estados | 35 pts / 35% |
| **Criterio 3**: diseña la solución a través de modelos | Construcción del algoritmo repetitivo con suma, promedio y mínimo | 40 pts / 40% |

**Observación docente:** se aceptan soluciones equivalentes en PSeInt si conservan la lógica correcta, aunque cambie el nombre de las variables o el orden de algunas instrucciones.
