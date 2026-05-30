# S11 — Taller
## TGA04 · UIB

**Semana 11:** Prueba de escritorio + primer programa en Python  
**Entrega del estudiante:**
1. Trace tables completos en cuaderno o en esta guía.
2. Archivo `S11_NombreApellido.py` guardado y ejecutado en Thonny.

---

## Parte A. Trace tables (RA3)
**Instrucción general:** complete cada tabla paso a paso. No escriba solo la respuesta final.

### Ejercicio 1 — Alerta por ausentismo de T03
**PSeInt**
```
Algoritmo Ejercicio1
    Definir n4 Como Real
    Definir mensaje Como Cadena
    n4 <- 19.44

    Si n4 > 15 Entonces
        mensaje <- "Alerta roja"
    SiNo
        mensaje <- "En rango"
    FinSi

    Escribir mensaje
FinAlgoritmo
```

**Complete la tabla:**
| Variable / salida | Paso 0 | Paso 1 | Paso 2 | Paso 3 | Paso 4 |
|---|---|---|---|---|---|
| n4 | _____ | _____ | _____ | _____ | _____ |
| mensaje | _____ | _____ | _____ | _____ | _____ |
| salida / condición | _____ | _____ | _____ | _____ | _____ |

### Ejercicio 2 — Meta de sesiones UIB
**PSeInt**
```
Algoritmo Ejercicio2
    Definir realizadas, meta, vueltas Como Entero
    realizadas <- 142
    meta <- 150
    vueltas <- 0

    Mientras realizadas < meta Hacer
        realizadas <- realizadas + 1
        vueltas <- vueltas + 1
    FinMientras

    Escribir realizadas, vueltas
FinAlgoritmo
```

**Complete la tabla por vueltas:**
| Variable / salida | Inicio | V1 | V2 | V3 | V4 | V5 | V6 | V7 | V8 | Salida |
|---|---|---|---|---|---|---|---|---|---|---|
| realizadas | _____ | _____ | _____ | _____ | _____ | _____ | _____ | _____ | _____ | _____ |
| meta | _____ | _____ | _____ | _____ | _____ | _____ | _____ | _____ | _____ | _____ |
| vueltas | _____ | _____ | _____ | _____ | _____ | _____ | _____ | _____ | _____ | _____ |
| condición `realizadas < meta` | _____ | _____ | _____ | _____ | _____ | _____ | _____ | _____ | _____ | _____ |

### Ejercicio 3 — Conteo de alertas N4
**PSeInt**
```
Algoritmo Ejercicio3
    Definir contador, alertas Como Entero
    Definir n4_actual Como Real

    contador <- 1
    alertas <- 0

    Mientras contador <= 3 Hacer
        Si contador = 1 Entonces
            n4_actual <- 11.25
        FinSi

        Si contador = 2 Entonces
            n4_actual <- 19.44
        FinSi

        Si contador = 3 Entonces
            n4_actual <- 30.56
        FinSi

        Si n4_actual > 15 Entonces
            alertas <- alertas + 1
        FinSi

        contador <- contador + 1
    FinMientras

    Escribir alertas
FinAlgoritmo
```

**Complete la tabla por ciclo:**
| Variable / salida | Inicio | Ciclo 1 | Ciclo 2 | Ciclo 3 | Salida |
|---|---|---|---|---|---|
| contador | _____ | _____ | _____ | _____ | _____ |
| n4_actual | _____ | _____ | _____ | _____ | _____ |
| alertas | _____ | _____ | _____ | _____ | _____ |
| salida | _____ | _____ | _____ | _____ | _____ |

---

## Parte B. Python en Thonny (RA4)
**Instrucción general:** escriba cada ejercicio en Thonny, ejecútelo y guárdelo.

### Ejercicio 4 — Variables básicas
Escriba un programa que declare estas variables y luego las imprima:
- `empresa = "NeuroBiz S.A.S."`
- `sesiones_contratadas = 150`
- `sesiones_realizadas = 142`
- `valor_pagado = 11840000`

**Salida esperada:** una frase completa con esos cuatro datos.

### Ejercicio 5 — Operación simple
Agregue al ejercicio 4 una variable llamada `faltantes` y muestre el resultado con `f-string`.

Fórmula:
```python
faltantes = sesiones_contratadas - sesiones_realizadas
```

**Pregunta de control:** ¿cuántas sesiones faltan para llegar a 150?

### Ejercicio 6 — Saludo personalizado + datos de un terapeuta
Cree un programa que:
1. pida el nombre del estudiante con `input()`,
2. declare `terapeuta = "Ana Ramos"`,
3. declare `n1 = 85.0`,
4. imprima un saludo y una línea con el dato del terapeuta.

**Debe usar `f-string`.**

---

## Clave docente
> Usar esta sección solo al momento de retroalimentar o verificar.

### Solución Ejercicio 1
| Variable / salida | Paso 0 | Paso 1 | Paso 2 | Paso 3 | Paso 4 |
|---|---|---|---|---|---|
| n4 | — | 19.44 | 19.44 | 19.44 | 19.44 |
| mensaje | — | — | — | Alerta roja | Alerta roja |
| salida / condición | — | — | Verdadero | — | Alerta roja |

### Solución Ejercicio 2
| Variable / salida | Inicio | V1 | V2 | V3 | V4 | V5 | V6 | V7 | V8 | Salida |
|---|---|---|---|---|---|---|---|---|---|---|
| realizadas | 142 | 143 | 144 | 145 | 146 | 147 | 148 | 149 | 150 | 150 |
| meta | 150 | 150 | 150 | 150 | 150 | 150 | 150 | 150 | 150 | 150 |
| vueltas | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 8 |
| condición `realizadas < meta` | Verdadero | Verdadero | Verdadero | Verdadero | Verdadero | Verdadero | Verdadero | Verdadero | Falso | — |

### Solución Ejercicio 3
| Variable / salida | Inicio | Ciclo 1 | Ciclo 2 | Ciclo 3 | Salida |
|---|---|---|---|---|---|
| contador | 1 | 2 | 3 | 4 | 4 |
| n4_actual | — | 11.25 | 19.44 | 30.56 | 30.56 |
| alertas | 0 | 0 | 1 | 2 | 2 |
| salida | — | — | — | — | 2 |

### Solución Ejercicio 4
```python
empresa = "NeuroBiz S.A.S."
sesiones_contratadas = 150
sesiones_realizadas = 142
valor_pagado = 11840000

print(f"{empresa} contrató {sesiones_contratadas} sesiones, realizó {sesiones_realizadas} y pagó ${valor_pagado}.")
```

### Solución Ejercicio 5
```python
empresa = "NeuroBiz S.A.S."
sesiones_contratadas = 150
sesiones_realizadas = 142
valor_pagado = 11840000
faltantes = sesiones_contratadas - sesiones_realizadas

print(f"{empresa} contrató {sesiones_contratadas} sesiones, realizó {sesiones_realizadas} y pagó ${valor_pagado}.")
print(f"Faltan {faltantes} sesiones para completar la meta mensual.")
```

### Solución Ejercicio 6
```python
nombre_estudiante = input("Escribe tu nombre: ")
terapeuta = "Ana Ramos"
n1 = 85.0

print(f"Hola, {nombre_estudiante}.")
print(f"El terapeuta {terapeuta} tiene N1 de {n1}%.")
```
