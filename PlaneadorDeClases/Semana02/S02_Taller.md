# Semana 2 · Taller
## TGA04 Fundamentos de Computación para los Negocios · UIB
### RA1: Variables y Operadores con el caso NeuroBiz/UIB

**Nombre:** ____________________________  
**Programa:** ____________________________  
**Fecha:** ____________________________

**Instrucciones generales**
- Responde con orden y justifica cuando se te pida.
- En la parte de cálculo manual debes mostrar **fórmula, sustitución y resultado**.
- En pseudocódigo usa **INICIO/FIN, LEER, ESCRIBIR y `<-`**.
- Si trabajas en PSeInt, puedes usar **Proceso/FinProceso** como equivalente de **INICIO/FIN**.
- Puedes apoyar tus respuestas con la tabla de datos del caso.

---

## PARTE 1. Clasificación de variables

### Ejercicio 1. Clasifica cada dato
Marca cada elemento como: **numérica entera / numérica real / alfanumérica / lógica**.

| Ítem | Dato | Clasificación |
|---|---|---|
| 1 | `T03` | __________________ |
| 2 | `Luz Torres` | __________________ |
| 3 | `72 sesiones disponibles` | __________________ |
| 4 | `4.8 de satisfacción` | __________________ |
| 5 | `TDAH` | __________________ |
| 6 | `Cumple meta: Verdadero` | __________________ |
| 7 | `$11.840.000 COP` | __________________ |
| 8 | `Contaduría` | __________________ |
| 9 | `Promedio antes = 2.8` | __________________ |
| 10 | `22 sesiones canceladas` | __________________ |
| 11 | `Terapia grupal` | __________________ |
| 12 | `12 estudiantes únicos` | __________________ |
| 13 | `Mejora >= 0.5: Falso` | __________________ |
| 14 | `U1 = 94.7%` | __________________ |
| 15 | `9 diagnósticos en tiempo` | __________________ |

### Ejercicio 2. Indicadores, tipos de variables y operadores
Para cada indicador, identifica:
1. las variables principales,
2. el tipo de variable de sus componentes,
3. los operadores usados.

| Indicador | Fórmula | Variables principales | Tipos de variables | Operadores usados |
|---|---|---|---|---|
| N1 | (Sesiones realizadas / sesiones disponibles) × 100 | __________ | __________ | __________ |
| N2 | (Satisfechos / total encuestas) × 100 | __________ | __________ | __________ |
| N3 | Total horas sesión / número de sesiones | __________ | __________ | __________ |
| N4 | (Canceladas / programadas) × 100 | __________ | __________ | __________ |
| N5 | (Cancelaciones < 24h / total programadas) × 100 | __________ | __________ | __________ |
| N6 | Costos operativos / sesiones realizadas | __________ | __________ | __________ |
| N7 | (Pacientes activos / pacientes iniciales) × 100 | __________ | __________ | __________ |
| N8 | (Diagnósticos en tiempo / total diagnósticos) × 100 | __________ | __________ | __________ |
| U1 | (Sesiones usadas / contratadas) × 100 | __________ | __________ | __________ |
| U2 | Total pagado / estudiantes únicos | __________ | __________ | __________ |
| U3 | (Estudiantes con mejora >= 0.5 / total) × 100 | __________ | __________ | __________ |
| U4 | (Diagnósticos nuevos / total evaluados) × 100 | __________ | __________ | __________ |
| U5 | Sesiones reales / sesiones contratadas | __________ | __________ | __________ |
| U6 | (Estudiantes satisfechos / total encuestados) × 100 | __________ | __________ | __________ |
| U7 | (Estudiantes desertaron / total intervenidos) × 100 | __________ | __________ | __________ |

---

## PARTE 2. Aplicación de operadores

### Ejercicio 3. Cálculo manual con T01 (Ana Ramos)
**Datos T01:** sesiones disponibles = 80, sesiones realizadas = 68, canceladas = 9

#### a) Calcula N1
- Fórmula: ________________________________________________
- Sustitución: _____________________________________________
- Resultado: ______________________________________________

#### b) Calcula N4
> Recuerda: sesiones programadas = realizadas + canceladas
- Fórmula: ________________________________________________
- Sustitución: _____________________________________________
- Resultado: ______________________________________________

### Ejercicio 4. Cálculo manual con UIB (febrero)
**Datos:** sesiones usadas = 142, sesiones contratadas = 150, total pagado = 11.840.000, estudiantes únicos = 12

#### a) Calcula U1
- Fórmula: ________________________________________________
- Sustitución: _____________________________________________
- Resultado: ______________________________________________

#### b) Calcula U2
- Fórmula: ________________________________________________
- Sustitución: _____________________________________________
- Resultado: ______________________________________________

### Ejercicio 5. Operadores lógicos
Evalúa la condición:

**Condición:** `N1 >= 75% Y N4 <= 15%`

Completa la tabla para cada terapeuta.

| ID | Nombre | N1 | N4 | ¿Cumple la condición lógica? |
|---|---|---:|---:|---|
| T01 | Ana Ramos | ______ | ______ | ______ |
| T02 | Carlos Mejía | ______ | ______ | ______ |
| T03 | Luz Torres | ______ | ______ | ______ |
| T04 | Mario Suárez | ______ | ______ | ______ |
| T05 | Paula Vega | ______ | ______ | ______ |
| T06 | Diego Ríos | ______ | ______ | ______ |
| T07 | Sandra Ospina | ______ | ______ | ______ |
| T08 | Héctor Niño | ______ | ______ | ______ |

---

## PARTE 3. Escritura en pseudocódigo

### Ejercicio 6. Escribe el pseudocódigo

#### a) Leer sesiones realizadas y disponibles de un terapeuta, calcular e imprimir N1.

```text




```

#### b) Leer sesiones realizadas, disponibles y canceladas; calcular e imprimir N1 y N4.

```text






```

### Ejercicio 7. RETO (opcional)
Escribe un pseudocódigo que lea los datos de **dos terapeutas** y muestre cuál tiene el **mejor N1**.

```text






```

---

# CLAVE DE RESPUESTAS

## Respuestas de la Parte 1

### Ejercicio 1
| Ítem | Respuesta |
|---|---|
| 1 | Alfanumérica |
| 2 | Alfanumérica |
| 3 | Numérica entera |
| 4 | Numérica real |
| 5 | Alfanumérica |
| 6 | Lógica |
| 7 | Numérica real |
| 8 | Alfanumérica |
| 9 | Numérica real |
| 10 | Numérica entera |
| 11 | Alfanumérica |
| 12 | Numérica entera |
| 13 | Lógica |
| 14 | Numérica real |
| 15 | Numérica entera |

### Ejercicio 2
| Indicador | Variables principales (ejemplo) | Tipos de variables | Operadores usados |
|---|---|---|---|
| N1 | realizadas, disponibles, n1 | enteras + real | `/`, `*` |
| N2 | satisfechos, total_encuestas, n2 | enteras + real | `/`, `*` |
| N3 | total_horas, numero_sesiones, n3 | reales + enteras | `/` |
| N4 | canceladas, programadas, n4 | enteras + real | `/`, `*` |
| N5 | cancelaciones_tardias, total_programadas, n5 | enteras + real | `<`, `/`, `*` |
| N6 | costos, realizadas, n6 | real + enteras | `/` |
| N7 | activos, iniciales, n7 | enteras + real | `/`, `*` |
| N8 | diagnosticos_tiempo, total_diagnosticos, n8 | enteras + real | `/`, `*` |
| U1 | usadas, contratadas, u1 | enteras + real | `/`, `*` |
| U2 | total_pagado, estudiantes_unicos, u2 | real + enteras | `/` |
| U3 | mejora, total, u3 | lógica + enteras + real | `>=`, `/`, `*` |
| U4 | nuevos, evaluados, u4 | enteras + real | `/`, `*` |
| U5 | reales, contratadas, u5 | enteras + real | `/` |
| U6 | satisfechos, encuestados, u6 | enteras + real | `/`, `*` |
| U7 | desertaron, intervenidos, u7 | enteras + real | `/`, `*` |

## Respuestas de la Parte 2

### Ejercicio 3
#### a) N1 de T01
- Fórmula: `N1 = (sesiones realizadas / sesiones disponibles) * 100`
- Sustitución: `N1 = (68 / 80) * 100`
- Resultado: `N1 = 85.0%`

#### b) N4 de T01
- Sesiones programadas = `68 + 9 = 77`
- Fórmula: `N4 = (sesiones canceladas / sesiones programadas) * 100`
- Sustitución: `N4 = (9 / 77) * 100`
- Resultado: `N4 ≈ 11.7%`

### Ejercicio 4
#### a) U1
- Fórmula: `U1 = (sesiones usadas / sesiones contratadas) * 100`
- Sustitución: `U1 = (142 / 150) * 100`
- Resultado: `U1 ≈ 94.7%`

#### b) U2
- Fórmula: `U2 = total pagado / estudiantes unicos`
- Sustitución: `U2 = 11840000 / 12`
- Resultado: `U2 ≈ 986666.67 COP`

### Ejercicio 5
| ID | Nombre | N1 | N4 | ¿Cumple `N1 >= 75 Y N4 <= 15`? |
|---|---|---:|---:|---|
| T01 | Ana Ramos | 85.0% | 11.7% | VERDADERO |
| T02 | Carlos Mejía | 98.6% | 2.7% | VERDADERO |
| T03 | Luz Torres | 75.0% | 20.6% | FALSO |
| T04 | Mario Suárez | 96.2% | 4.9% | VERDADERO |
| T05 | Paula Vega | 96.7% | 1.7% | VERDADERO |
| T06 | Diego Ríos | 59.7% | 33.8% | FALSO |
| T07 | Sandra Ospina | 95.8% | 6.8% | VERDADERO |
| T08 | Héctor Niño | 100.0% | 0.0% | VERDADERO |

## Respuestas de la Parte 3

### Ejercicio 6a
```text
Proceso Calcular_N1
    Definir realizadas, disponibles, n1 Como Real
    Leer realizadas
    Leer disponibles
    n1 <- (realizadas / disponibles) * 100
    Escribir n1
FinProceso
```

### Ejercicio 6b
```text
Proceso Calcular_N1_y_N4
    Definir realizadas, disponibles, canceladas, programadas, n1, n4 Como Real
    Leer realizadas
    Leer disponibles
    Leer canceladas
    n1 <- (realizadas / disponibles) * 100
    programadas <- realizadas + canceladas
    n4 <- (canceladas / programadas) * 100
    Escribir n1
    Escribir n4
FinProceso
```

### Ejercicio 7 (una posible solución)
```text
Proceso Comparar_Dos_Terapeutas
    Definir r1, d1, r2, d2, n1_1, n1_2 Como Real
    Leer r1
    Leer d1
    Leer r2
    Leer d2

    n1_1 <- (r1 / d1) * 100
    n1_2 <- (r2 / d2) * 100

    Si n1_1 > n1_2 Entonces
        Escribir "El terapeuta 1 tiene mejor N1"
    SiNo
        Escribir "El terapeuta 2 tiene mejor N1"
    FinSi
FinProceso
```
