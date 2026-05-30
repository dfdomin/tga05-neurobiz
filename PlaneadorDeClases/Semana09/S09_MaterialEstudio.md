# S09 — Material de Estudio
## PARA-FPARA, HH-FHH y `for` en Python 3.x
### TGA04 Fundamentos de Computación para los Negocios · UIB · Semana 9

**RA2:** Formular soluciones algorítmicas con primitivas repetitivas.  
**Herramientas:** PSeInt y Thonny.  
**Caso transversal:** NeuroBiz (eficiencia operativa) y UIB (valor del servicio).

---

## 1. Idea central de la semana
La semana 8 abrió la iteración con `while`. La semana 9 afina la decisión:
- si el número de repeticiones ya se conoce, suele convenir **`for` / PARA-FPARA**;
- si se necesita ejecutar el bloque **al menos una vez** antes de evaluar, sirve **HH-FHH**.

En términos de negocio, esto evita programar “a ciegas”: primero se decide **qué tipo de repetición necesita el problema**.

---

## 2. Datos exactos del caso
| ID | Nombre | Disp | Realizadas | Canceladas | Satisfacción | N1 | N4 |
|---|---|---:|---:|---:|---:|---:|---:|
| T01 | Ana Ramos | 80 | 68 | 9 | 4.7 | 85%✅ | 11.25%✅ |
| T02 | Carlos Mejía | 72 | 71 | 2 | 4.9 | 98.6%✅ | 2.78%✅ |
| T03 | Luz Torres | 72 | 54 | 14 | 4.2 | 75%✅ | 19.44%🔴 |
| T04 | Mario Suárez | 80 | 77 | 4 | 4.8 | 96.3%✅ | 5%✅ |
| T05 | Paula Vega | 60 | 58 | 1 | 5.0 | 96.7%✅ | 1.67%✅ |
| T06 | Diego Ríos | 72 | 43 | 22 | 3.9 | 59.7%🔴 | 30.56%🔴🔴 |
| T07 | Sandra Ospina | 72 | 69 | 5 | 4.6 | 95.8%✅ | 6.94%✅ |
| T08 | Héctor Niño | 80 | 80 | 0 | 4.8 | 100%✅ | 0%✅ |

**Contrato UIB:** 150 sesiones/mes, 142 realizadas, $11.840.000 COP, 12 estudiantes, `U3 = 16.7%` 🔴, `U1 = 94.7%` ✅.

---

## 3. PARA-FPARA en pseudocódigo
PARA-FPARA es un ciclo contador. Se usa cuando sabemos desde el inicio cuántas vueltas habrá.

### Plantilla PSeInt
```pseint
Para contador <- inicio Hasta fin Con Paso incremento Hacer
    // instrucciones
FinPara
```

### Ejemplo básico
```pseint
Proceso ContarDel1Al5ConPara
    Definir i Como Entero

    Para i <- 1 Hasta 5 Con Paso 1 Hacer
        Escribir i
    FinPara
FinProceso
```

---

## 4. `for` en Python
En Python el equivalente más común es `for` con `range()` o con una lista.

### 4.1 `for` con `range()`
```python
for i in range(1, 6):
    print(i)
```

**Salida:** `1 2 3 4 5`

### 4.2 `for` con una lista
```python
satisfacciones = [4.7, 4.9, 4.2, 4.8, 5.0, 3.9, 4.6, 4.8]
for valor in satisfacciones:
    print(valor)
```

---

## 5. HH-FHH (Hacer-Hasta / do-while)
El rasgo clave es que **el bloque se ejecuta primero y la condición se revisa después**. Por eso siempre corre al menos una vez.

> En PSeInt la forma práctica equivalente suele escribirse como **`Repetir ... Hasta Que`**.

### PSeInt
```pseint
Proceso MenuConHHFHH
    Definir opcion Como Entero

    Repetir
        Escribir "1. Continuar"
        Escribir "2. Salir"
        Leer opcion
    Hasta Que opcion = 2
FinProceso
```

### Simulación en Python
Python no tiene `do-while` nativo, pero puede simularse así:

```python
while True:
    opcion = int(input("1. Continuar / 2. Salir: "))
    if opcion == 2:
        break
```

---

## 6. Ejemplo resuelto — Promedio de satisfacción con `for`
Lista exacta del caso:

```text
[4.7, 4.9, 4.2, 4.8, 5.0, 3.9, 4.6, 4.8]
```

### Python
```python
satisfacciones = [4.7, 4.9, 4.2, 4.8, 5.0, 3.9, 4.6, 4.8]
suma = 0

for valor in satisfacciones:
    suma = suma + valor

promedio = suma / len(satisfacciones)
print(round(promedio, 2))
```

### PSeInt
```pseint
Proceso PromedioSatisfaccionConPara
    Dimension satisf[8]
    Definir i Como Entero
    Definir suma, promedio Como Real

    satisf[1] <- 4.7
    satisf[2] <- 4.9
    satisf[3] <- 4.2
    satisf[4] <- 4.8
    satisf[5] <- 5.0
    satisf[6] <- 3.9
    satisf[7] <- 4.6
    satisf[8] <- 4.8

    suma <- 0
    Para i <- 1 Hasta 8 Con Paso 1 Hacer
        suma <- suma + satisf[i]
    FinPara

    promedio <- suma / 8
    Escribir "Promedio satisfacción: ", promedio
FinProceso
```

**Resultado correcto:** `4.61` aproximadamente.

---

## 7. Ejemplo resuelto — Análisis UIB con `for`
Si la mejora fuerte la lograron 2 de 12 estudiantes, una forma simple de representarlo es esta lista de banderas:

```text
mejoras = [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
```

### Python
```python
mejoras = [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
contador = 0

for valor in mejoras:
    if valor == 1:
        contador = contador + 1

u3 = (contador / len(mejoras)) * 100
print("U3:", round(u3, 1))
```

**Resultado:** `U3 = 16.7%`

**Lectura dual:**
- **NeuroBiz:** alta utilización del contrato (`U1 = 94.7%`).
- **UIB:** la mejora fuerte (`U3 = 16.7%`) sigue baja; el cliente mira valor, no solo uso.

---

## 8. For vs While vs HH-FHH
| Estructura | Pregunta que resuelve | Ventaja | Riesgo típico |
|---|---|---|---|
| `for` / PARA-FPARA | ¿Cuántas veces exactamente debo repetir? | Sintaxis más ordenada para conteos conocidos | rango mal definido |
| `while` / MQ-FMQ | ¿Debo repetir mientras una condición siga verdadera? | Flexible para negocio y validación | ciclo infinito |
| HH-FHH | ¿El bloque debe ejecutarse al menos una vez? | Útil para menús y validaciones de entrada | olvidar condición de salida |

### Regla de selección rápida
- Si ya conoces la cantidad de elementos (8 terapeutas, 12 estudiantes, 10 repeticiones): **usa `for`**.
- Si dependes de una condición que puede cambiar sin saber cuántas vueltas tomará: **usa `while`**.
- Si primero debes mostrar o ejecutar algo y luego validar la salida: **usa HH-FHH**.

---

## 9. Neurodivergencia y predictibilidad
En esta semana el enlace es **TEA**. Para muchas personas con TEA, las rutinas estables, las secuencias conocidas y el número de pasos definido pueden facilitar la anticipación. Un `for` se parece a eso porque desde el inicio deja claro:
- cuántas iteraciones habrá,
- cuándo empieza,
- cuándo termina,
- y qué paso sigue.

Ejemplo de analogía válida para clase:

```pseint
Para sesion <- 1 Hasta 12 Con Paso 1 Hacer
    Escribir "Realizar sesión programada número ", sesion
FinPara
```

La explicación debe ser respetuosa: se habla de **predictibilidad útil**, no de reducir a la persona a un algoritmo.

---

## 10. Ideas clave para recordar
- `for` conviene cuando el número de repeticiones es conocido.
- HH-FHH garantiza una primera ejecución.
- Python usa `range()` y listas; PSeInt usa `Para` y `Repetir ... Hasta Que`.
- El promedio de satisfacción de T01–T08 es **4.61**.
- El contrato UIB muestra una tensión útil para análisis: **U1 alto** y **U3 bajo**.

---

## 11. Referencias de la semana
- **Xu & Frydenberg (2021).** Referencia orientadora para práctica de Python y estructuras de control en programación inicial.
- **ACM/IEEE Computing Curricula 2020 (CC2020).** Referencia para control de flujo, iteración y fundamentos algorítmicos.
- **Programa del módulo TGA04 UIB.** RA2: MQ-FMQ, HH-FHH y PARA-FPARA.
