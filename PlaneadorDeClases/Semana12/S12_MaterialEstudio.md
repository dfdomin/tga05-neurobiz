# S12 — Material de Estudio
## TGA04 · UIB

**Semana 12:** RA4 — Python en Thonny: condicionales y bucles  
**Lenguaje:** Python 3.x  
**IDE:** Thonny

## 1. Meta de la semana
En esta semana ya no basta con imprimir variables. Ahora debemos **tomar decisiones y repetir procesos** en Python para analizar datos reales de NeuroBiz.

## 2. Datos exactos del caso NeuroBiz
| ID | Nombre | N1 | N4 | Satisfacción |
|---|---|---:|---:|---:|
| T01 | Ana Ramos | 85.0 | 11.25 | 4.7 |
| T02 | Carlos Mejía | 98.6 | 2.78 | 4.9 |
| T03 | Luz Torres | 75.0 | 19.44 | 4.2 |
| T04 | Mario Suárez | 96.3 | 5.0 | 4.8 |
| T05 | Paula Vega | 96.7 | 1.67 | 5.0 |
| T06 | Diego Ríos | 59.7 | 30.56 | 3.9 |
| T07 | Sandra Ospina | 95.8 | 6.94 | 4.6 |
| T08 | Héctor Niño | 100.0 | 0.0 | 4.8 |

Datos UIB para usar en ejemplos:
- `sesiones_contratadas = 150`
- `sesiones_realizadas = 142`
- `valor_pagado = 11840000`
- `u3 = 16.7`
- `u1 = 94.7`

## 3. Nota neurodivergencia: TDAH y automatización
Esta semana se conversa sobre **TDAH en población universitaria/adulta** y la utilidad de automatizar tareas. Cita breve para contextualizar:
- **Vélez Van Meerbeke et al. (2008):** 5.7% reportado en Bogotá.
- **Cornejo et al. (2005):** reportan presencia relevante de TDAH en población colombiana.

Relación con el curso:
- hacer a mano la misma clasificación 8 veces puede agobiar,
- un `for` o un `if` automatiza la repetición,
- así queda más energía mental para interpretar el resultado.

**Idea clave:** Python no reemplaza el análisis; libera atención para analizar mejor.

## 4. `if`, `elif`, `else`
Sirven para tomar decisiones.

### 4.1 Sintaxis básica
```python
if condicion_1:
    print("Opción 1")
elif condicion_2:
    print("Opción 2")
else:
    print("Opción 3")
```

### 4.2 Regla de clasificación del curso
Para esta semana usaremos esta regla simple con N1 y N4:
- **Verde:** `n1 >= 75` y `n4 <= 15`
- **Amarillo:** `n1 >= 75` y `n4 > 15`
- **Rojo:** `n1 < 75`

### 4.3 Ejemplo con un terapeuta
```python
nombre = "Luz Torres"
n1 = 75.0
n4 = 19.44

if n1 >= 75 and n4 <= 15:
    color = "VERDE"
elif n1 >= 75 and n4 > 15:
    color = "AMARILLO"
else:
    color = "ROJO"

print(f"{nombre} queda clasificada en {color}.")
```

Resultado esperado: **AMARILLO**.

## 5. `for` con listas
Un `for` recorre elementos uno por uno.

### 5.1 Lista simple
```python
satisfacciones = [4.7, 4.9, 4.2, 4.8, 5.0, 3.9, 4.6, 4.8]

suma = 0
for dato in satisfacciones:
    suma = suma + dato

promedio = suma / len(satisfacciones)
print(f"Promedio de satisfacción: {promedio}")
```

### 5.2 `for` con `range()`
```python
for i in range(5):
    print(i)
```

Salida:
- 0
- 1
- 2
- 3
- 4

### 5.3 Ejemplo con N1
```python
n1_valores = [85.0, 98.6, 75.0, 96.3, 96.7, 59.7, 95.8, 100.0]
suma_n1 = 0

for valor in n1_valores:
    suma_n1 = suma_n1 + valor

promedio_n1 = suma_n1 / len(n1_valores)
print(f"Promedio N1: {promedio_n1:.2f}%")
```

## 6. `while`
Un `while` repite mientras la condición sea verdadera.

### 6.1 Ejemplo base
```python
sesiones_realizadas = 142
meta = 150
dias_extra = 0

while sesiones_realizadas < meta:
    sesiones_realizadas = sesiones_realizadas + 1
    dias_extra = dias_extra + 1

print(f"Meta alcanzada: {sesiones_realizadas} sesiones en {dias_extra} pasos.")
```

### 6.2 `break` y `continue`
```python
numero = 0
while numero < 10:
    numero = numero + 1

    if numero == 3:
        continue

    if numero == 8:
        break

    print(numero)
```

- `continue` salta a la siguiente vuelta.
- `break` rompe el ciclo.

> En esta semana no abusaremos de `break` y `continue`; primero importa dominar el `while` básico.

## 7. Listas (intro)
Una lista guarda varios datos del mismo tipo o de tipos compatibles.

```python
nombres = ["Ana Ramos", "Carlos Mejía", "Luz Torres"]
n4_valores = [11.25, 2.78, 19.44]
```

Ventajas:
- permiten recorrer varios datos con `for`,
- reducen repetición de código,
- ayudan a construir reportes.

## 8. `f-strings`
```python
nombre = "Diego Ríos"
n4 = 30.56
print(f"{nombre} tiene N4 de {n4}%")
```

Con formato decimal:
```python
promedio = 4.6125
print(f"Promedio: {promedio:.2f}")
```

## 9. Comentarios y nombres claros
### 9.1 Comentarios
```python
# Este bloque calcula el promedio de satisfacción
```

### 9.2 Buenas prácticas de nombres (`snake_case`)
Correcto:
```python
sesiones_realizadas = 142
promedio_satisfaccion = 4.61
```

Evitar:
```python
sr = 142
ps = 4.61
```

## 10. Ejemplos progresivos con NeuroBiz
### 10.1 Clasificar un terapeuta
```python
nombre = "Diego Ríos"
n1 = 59.7
n4 = 30.56

if n1 >= 75 and n4 <= 15:
    color = "VERDE"
elif n1 >= 75 and n4 > 15:
    color = "AMARILLO"
else:
    color = "ROJO"

print(f"{nombre}: {color}")
```

### 10.2 Calcular promedio de satisfacción
```python
satisfacciones = [4.7, 4.9, 4.2, 4.8, 5.0, 3.9, 4.6, 4.8]
suma = 0

for nota in satisfacciones:
    suma = suma + nota

promedio = suma / len(satisfacciones)
print(f"Promedio satisfacción: {promedio:.2f}")
```

### 10.3 Simular alcance de meta UIB
```python
sesiones_realizadas = 142
meta = 150

while sesiones_realizadas < meta:
    sesiones_realizadas = sesiones_realizadas + 1
    print(f"Sesiones acumuladas: {sesiones_realizadas}")
```

### 10.4 Mini reporte NeuroBiz
```python
nombres = [
    "Ana Ramos", "Carlos Mejía", "Luz Torres", "Mario Suárez",
    "Paula Vega", "Diego Ríos", "Sandra Ospina", "Héctor Niño"
]
n1_valores = [85.0, 98.6, 75.0, 96.3, 96.7, 59.7, 95.8, 100.0]
n4_valores = [11.25, 2.78, 19.44, 5.0, 1.67, 30.56, 6.94, 0.0]

for i in range(len(nombres)):
    if n1_valores[i] >= 75 and n4_valores[i] <= 15:
        color = "VERDE"
    elif n1_valores[i] >= 75 and n4_valores[i] > 15:
        color = "AMARILLO"
    else:
        color = "ROJO"

    print(f"{nombres[i]} -> {color}")
```

## 11. Cómo guardar y ejecutar en Thonny
1. Abrir Thonny.
2. Escribir el programa en el editor.
3. Ir a **File > Save**.
4. Guardar con nombre claro, por ejemplo: `reporte_neurobiz.py`.
5. Pulsar **Run** o presionar `F5`.
6. Leer la salida en la Shell.

## 12. Errores comunes de esta semana
- olvidar `:` después de `if`, `elif`, `else`, `for` o `while`;
- romper la sangría;
- dividir mal el nombre de una variable;
- intentar usar `=` dentro de una condición cuando se quería `==`;
- calcular el promedio fuera de lugar o antes de terminar el ciclo.

## 13. Referencias sugeridas
- De Santo et al. (2022). IEEE Transactions on Learning Technologies. Referencia útil para enseñanza de programación y apoyo tecnológico.
- Vélez Van Meerbeke et al. (2008). Referencia colombiana usada para contextualizar TDAH.
- Cornejo et al. (2005). Referencia colombiana de apoyo para discusión de TDAH.
- Material institucional del módulo TGA04.
