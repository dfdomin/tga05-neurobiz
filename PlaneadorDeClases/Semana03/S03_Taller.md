# S03 — Taller de Semana 3
## Diagramas de flujo y pseudocódigo formal
### TGA04 Fundamentos de Computación para los Negocios · Caso NeuroBiz + UIB

**Nombre del estudiante:** ____________________________  
**Grupo:** ____________________________  
**Fecha:** ____________________________

---

## Instrucciones generales
- Trabaje con letra legible.
- En Semana 3 use solo **secuencia**.
- Si describe un diagrama en texto, escriba cada símbolo en orden y use flechas `→`.
- Cuando haga pseudocódigo, use sintaxis básica de PSeInt.
- Puede usar los datos del caso NeuroBiz + UIB incluidos por el docente.

---

# PARTE 1. Reconocimiento de símbolos

## Ejercicio 1. ¿Qué símbolo corresponde?
Indique qué símbolo de diagrama de flujo usaría en cada caso: **óvalo (inicio/fin), rectángulo (proceso), paralelogramo (entrada/salida), rombo (decisión), conector, flecha**.

| Ítem | Acción del proceso NeuroBiz/UIB | Símbolo correcto |
|---|---|---|
| 1 | Comenzar el cálculo de N1 para T01 | __________ |
| 2 | Leer el número de sesiones disponibles del terapeuta | __________ |
| 3 | Calcular `n1 <- (realizadas / disponibles) * 100` | __________ |
| 4 | Mostrar en pantalla `N1 = 85%` | __________ |
| 5 | Continuar el diagrama en otra parte de la hoja sin cruzar líneas | __________ |
| 6 | Indicar el sentido de ejecución entre dos pasos | __________ |
| 7 | Finalizar el cálculo de U1 | __________ |
| 8 | Leer el total pagado por UIB en febrero | __________ |
| 9 | Preguntar `¿el estudiante mejoró académicamente?` | __________ |
| 10 | Calcular `u2 <- totalPagado / estudiantesUnicos` | __________ |

---

## Ejercicio 2. Flujo de N1 con errores
El siguiente diagrama textual tiene **4 errores**. Encuéntrelos y corríjalos.

```text
[rectangle: Inicio]
   ↓
[oval: Leer sesionesDisponibles y sesionesRealizadas]
   ↓
[parallelogram: n1 <- (sesionesRealizadas / sesionesDisponibles) * 100]
   ↓
[rectangle: Escribir "N1 = ", n1, "%"]
   ↓
[oval: Fin]
```

### Responda:
1. Error 1: ____________________________________________
2. Error 2: ____________________________________________
3. Error 3: ____________________________________________
4. Error 4: ____________________________________________

---

# PARTE 2. Construcción de diagramas de flujo

## Ejercicio 3. Construya el flujo para N4
Diseñe un diagrama de flujo para calcular la **tasa de ausentismo N4** de **un terapeuta**.

**Fórmula:** `N4 = (Canceladas / Programadas) × 100`

> Si no le dan el dato de programadas, puede usar:  
> `Programadas = Realizadas + Canceladas`

### Respuesta (describa su diagrama en texto)
```text
(Inicio) →

→

→

→

(Fin)
```

---

## Ejercicio 4. Construya el flujo para U1
Diseñe un diagrama de flujo para calcular la **tasa de uso del contrato U1** desde la perspectiva UIB.

**Fórmula:** `U1 = (Sesiones usadas / Sesiones contratadas) × 100`

### Respuesta (describa su diagrama en texto)
```text
(Inicio) →

→

→

→

(Fin)
```

---

## Ejercicio 5. Flujo combinado N1 + N4
Diseñe un diagrama de flujo que calcule **N1 y N4 en secuencia** para un terapeuta. Debe tener **dos salidas** al final.

### Respuesta (describa su diagrama en texto)
```text
(Inicio) →

→

→

→

→

→

(Fin)
```

---

# PARTE 3. Pseudocódigo en PSeInt

## Ejercicio 6. Pase el flujo del ejercicio 3 a pseudocódigo
Escriba el pseudocódigo en PSeInt para calcular N4.

```pseint
Proceso __________________________





FinProceso
```

---

## Ejercicio 7. Pase el flujo del ejercicio 4 a pseudocódigo
Escriba el pseudocódigo en PSeInt para calcular U1.

```pseint
Proceso __________________________





FinProceso
```

---

## Ejercicio 8. RETO
Escriba pseudocódigo que lea datos de **un estudiante UIB** y calcule:
1. número de sesiones asistidas,
2. costo total para UIB,
3. si el estudiante mostró mejora académica comparando nota antes y nota después.

**Sugerencia:** puede usar una variable lógica o una expresión relacional sin necesidad de `Si`.

### Respuesta
```pseint
Proceso __________________________







FinProceso
```

---

# CLAVE DE RESPUESTAS

## Respuesta Ejercicio 1
| Ítem | Símbolo correcto |
|---|---|
| 1 | Óvalo |
| 2 | Paralelogramo |
| 3 | Rectángulo |
| 4 | Paralelogramo |
| 5 | Conector |
| 6 | Flecha |
| 7 | Óvalo |
| 8 | Paralelogramo |
| 9 | Rombo |
| 10 | Rectángulo |

---

## Respuesta Ejercicio 2
Los 4 errores son:
1. **Inicio** no va en rectángulo; debe ir en **óvalo**.
2. **Leer sesionesDisponibles y sesionesRealizadas** no va en óvalo; debe ir en **paralelogramo**.
3. El cálculo de `n1 <- ...` no va en paralelogramo; debe ir en **rectángulo**.
4. **Escribir "N1 = ..."** no va en rectángulo; debe ir en **paralelogramo**.

Versión corregida:
```text
[oval: Inicio]
   ↓
[parallelogram: Leer sesionesDisponibles y sesionesRealizadas]
   ↓
[rectangle: n1 <- (sesionesRealizadas / sesionesDisponibles) * 100]
   ↓
[parallelogram: Escribir "N1 = ", n1, "%"]
   ↓
[oval: Fin]
```

---

## Respuesta Ejercicio 3
Una respuesta correcta puede escribirse así:
```text
(Inicio)
   ↓
/ Leer realizadas, canceladas /
   ↓
[ programadas <- realizadas + canceladas ]
   ↓
[ n4 <- (canceladas / programadas) * 100 ]
   ↓
/ Escribir "N4 = ", n4, "%" /
   ↓
(Fin)
```

---

## Respuesta Ejercicio 4
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

---

## Respuesta Ejercicio 5
```text
(Inicio)
   ↓
/ Leer disponibles, realizadas, canceladas /
   ↓
[ programadas <- realizadas + canceladas ]
   ↓
[ n1 <- (realizadas / disponibles) * 100 ]
   ↓
[ n4 <- (canceladas / programadas) * 100 ]
   ↓
/ Escribir "N1 = ", n1, "%" /
   ↓
/ Escribir "N4 = ", n4, "%" /
   ↓
(Fin)
```

---

## Respuesta Ejercicio 6
```pseint
Proceso Calcular_N4
    Definir realizadas, canceladas, programadas, n4 Como Real
    Escribir "Sesiones realizadas:"
    Leer realizadas
    Escribir "Sesiones canceladas:"
    Leer canceladas
    programadas <- realizadas + canceladas
    n4 <- (canceladas / programadas) * 100
    Escribir "N4 = ", n4, "%"
FinProceso
```

---

## Respuesta Ejercicio 7
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

---

## Respuesta Ejercicio 8
Una opción correcta, sin usar condicional explícito, es:

```pseint
Proceso Estudiante_UIB
    Definir sesionesAsistidas, costoPorSesion, costoTotal, notaAntes, notaDespues Como Real
    Definir mejoraAcademica Como Logico
    Escribir "Sesiones asistidas:"
    Leer sesionesAsistidas
    Escribir "Costo por sesión para UIB:"
    Leer costoPorSesion
    Escribir "Nota antes:"
    Leer notaAntes
    Escribir "Nota después:"
    Leer notaDespues
    costoTotal <- sesionesAsistidas * costoPorSesion
    mejoraAcademica <- (notaDespues - notaAntes) >= 0.5
    Escribir "Sesiones asistidas = ", sesionesAsistidas
    Escribir "Costo total = $", costoTotal
    Escribir "¿Mejora académica? ", mejoraAcademica
FinProceso
```

**Observación didáctica:** aquí la comparación produce un valor lógico (`Verdadero` o `Falso`) sin necesidad de usar todavía `Si`.
