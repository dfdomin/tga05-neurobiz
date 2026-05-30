# S12 — Taller
## TGA04 · UIB

**Semana 12:** Python en Thonny — condicionales y bucles  
**Producto:** programa integrador `reporte_neurobiz.py`

## Instrucción general
Construya un programa en Python que use los datos reales de NeuroBiz para:
1. declarar datos de los 8 terapeutas,
2. clasificar cada terapeuta con `if/elif/else`,
3. calcular el promedio de satisfacción con `for`,
4. simular con `while` la meta de sesiones UIB,
5. imprimir un reporte final.

## Regla de clasificación obligatoria
- **VERDE:** `n1 >= 75` y `n4 <= 15`
- **AMARILLO:** `n1 >= 75` y `n4 > 15`
- **ROJO:** `n1 < 75`

---

## Parte A. Declaración de datos
Escriba primero estas variables individuales:

```python
id_t01 = "T01"
nombre_t01 = "Ana Ramos"
n1_t01 = 85.0
n4_t01 = 11.25
satisfaccion_t01 = 4.7

id_t02 = "T02"
nombre_t02 = "Carlos Mejía"
n1_t02 = 98.6
n4_t02 = 2.78
satisfaccion_t02 = 4.9

id_t03 = "T03"
nombre_t03 = "Luz Torres"
n1_t03 = 75.0
n4_t03 = 19.44
satisfaccion_t03 = 4.2

id_t04 = "T04"
nombre_t04 = "Mario Suárez"
n1_t04 = 96.3
n4_t04 = 5.0
satisfaccion_t04 = 4.8

id_t05 = "T05"
nombre_t05 = "Paula Vega"
n1_t05 = 96.7
n4_t05 = 1.67
satisfaccion_t05 = 5.0

id_t06 = "T06"
nombre_t06 = "Diego Ríos"
n1_t06 = 59.7
n4_t06 = 30.56
satisfaccion_t06 = 3.9

id_t07 = "T07"
nombre_t07 = "Sandra Ospina"
n1_t07 = 95.8
n4_t07 = 6.94
satisfaccion_t07 = 4.6

id_t08 = "T08"
nombre_t08 = "Héctor Niño"
n1_t08 = 100.0
n4_t08 = 0.0
satisfaccion_t08 = 4.8
```

Ahora organice esos datos en listas para poder usar `for`:

```python
ids = [id_t01, id_t02, id_t03, id_t04, id_t05, id_t06, id_t07, id_t08]
nombres = [nombre_t01, nombre_t02, nombre_t03, nombre_t04, nombre_t05, nombre_t06, nombre_t07, nombre_t08]
n1_valores = [n1_t01, n1_t02, n1_t03, n1_t04, n1_t05, n1_t06, n1_t07, n1_t08]
n4_valores = [n4_t01, n4_t02, n4_t03, n4_t04, n4_t05, n4_t06, n4_t07, n4_t08]
satisfacciones = [satisfaccion_t01, satisfaccion_t02, satisfaccion_t03, satisfaccion_t04, satisfaccion_t05, satisfaccion_t06, satisfaccion_t07, satisfaccion_t08]
```

---

## Parte B. Clasificación con `if/elif/else`
Complete este bloque:

```python
verdes = 0
amarillos = 0
rojos = 0

for i in range(len(ids)):
    if ____________________________________________:
        color = "VERDE"
        verdes = verdes + 1
    elif __________________________________________:
        color = "AMARILLO"
        amarillos = amarillos + 1
    else:
        color = "ROJO"
        rojos = rojos + 1

    print(f"{ids[i]} - {nombres[i]}: N1={n1_valores[i]}%, N4={n4_valores[i]}%, Estado={color}")
```

**Meta:** el programa debe mostrar 8 líneas, una por terapeuta.

---

## Parte C. Promedio de satisfacción con `for`
Complete el cálculo:

```python
suma_satisfaccion = 0

for nota in satisfacciones:
    suma_satisfaccion = ___________________________

promedio_satisfaccion = __________________________
print(f"Promedio de satisfacción: {promedio_satisfaccion:.2f}")
```

---

## Parte D. `while` para meta UIB
Use los datos del cliente UIB:

```python
sesiones_contratadas = 150
sesiones_realizadas = 142
pasos = 0

while ____________________________________________:
    sesiones_realizadas = sesiones_realizadas + 1
    pasos = pasos + 1

print(f"Meta UIB completada con {sesiones_realizadas} sesiones en {pasos} pasos.")
```

---

## Parte E. Reporte final
Al final del programa imprima estas líneas:

```python
print("-" * 40)
print(f"Verdes: {verdes}")
print(f"Amarillos: {amarillos}")
print(f"Rojos: {rojos}")
print(f"Promedio de satisfacción: {promedio_satisfaccion:.2f}")
print(f"Sesiones UIB completadas: {sesiones_realizadas}")
```

**Pregunta de análisis:**
- ¿Qué terapeuta queda en amarillo?
- ¿Qué terapeuta queda en rojo?
- ¿Cuál es el promedio de satisfacción del equipo?

---

## Clave docente comentada
```python
# Datos de los 8 terapeutas
id_t01 = "T01"
nombre_t01 = "Ana Ramos"
n1_t01 = 85.0
n4_t01 = 11.25
satisfaccion_t01 = 4.7

id_t02 = "T02"
nombre_t02 = "Carlos Mejía"
n1_t02 = 98.6
n4_t02 = 2.78
satisfaccion_t02 = 4.9

id_t03 = "T03"
nombre_t03 = "Luz Torres"
n1_t03 = 75.0
n4_t03 = 19.44
satisfaccion_t03 = 4.2

id_t04 = "T04"
nombre_t04 = "Mario Suárez"
n1_t04 = 96.3
n4_t04 = 5.0
satisfaccion_t04 = 4.8

id_t05 = "T05"
nombre_t05 = "Paula Vega"
n1_t05 = 96.7
n4_t05 = 1.67
satisfaccion_t05 = 5.0

id_t06 = "T06"
nombre_t06 = "Diego Ríos"
n1_t06 = 59.7
n4_t06 = 30.56
satisfaccion_t06 = 3.9

id_t07 = "T07"
nombre_t07 = "Sandra Ospina"
n1_t07 = 95.8
n4_t07 = 6.94
satisfaccion_t07 = 4.6

id_t08 = "T08"
nombre_t08 = "Héctor Niño"
n1_t08 = 100.0
n4_t08 = 0.0
satisfaccion_t08 = 4.8

# Listas para recorrer con for
ids = [id_t01, id_t02, id_t03, id_t04, id_t05, id_t06, id_t07, id_t08]
nombres = [nombre_t01, nombre_t02, nombre_t03, nombre_t04, nombre_t05, nombre_t06, nombre_t07, nombre_t08]
n1_valores = [n1_t01, n1_t02, n1_t03, n1_t04, n1_t05, n1_t06, n1_t07, n1_t08]
n4_valores = [n4_t01, n4_t02, n4_t03, n4_t04, n4_t05, n4_t06, n4_t07, n4_t08]
satisfacciones = [satisfaccion_t01, satisfaccion_t02, satisfaccion_t03, satisfaccion_t04, satisfaccion_t05, satisfaccion_t06, satisfaccion_t07, satisfaccion_t08]

# Contadores por color
verdes = 0
amarillos = 0
rojos = 0

print("REPORTE NEUROBIZ")
print("-" * 40)

# Clasificación terapeuta por terapeuta
for i in range(len(ids)):
    if n1_valores[i] >= 75 and n4_valores[i] <= 15:
        color = "VERDE"
        verdes = verdes + 1
    elif n1_valores[i] >= 75 and n4_valores[i] > 15:
        color = "AMARILLO"
        amarillos = amarillos + 1
    else:
        color = "ROJO"
        rojos = rojos + 1

    print(f"{ids[i]} - {nombres[i]}: N1={n1_valores[i]}%, N4={n4_valores[i]}%, Estado={color}")

# Promedio de satisfacción
suma_satisfaccion = 0
for nota in satisfacciones:
    suma_satisfaccion = suma_satisfaccion + nota

promedio_satisfaccion = suma_satisfaccion / len(satisfacciones)

# While para completar meta UIB
sesiones_contratadas = 150
sesiones_realizadas = 142
pasos = 0

while sesiones_realizadas < sesiones_contratadas:
    sesiones_realizadas = sesiones_realizadas + 1
    pasos = pasos + 1

# Resumen final
print("-" * 40)
print(f"Verdes: {verdes}")
print(f"Amarillos: {amarillos}")
print(f"Rojos: {rojos}")
print(f"Promedio de satisfacción: {promedio_satisfaccion:.2f}")
print(f"Sesiones UIB completadas: {sesiones_realizadas}")
print(f"Pasos para completar la meta: {pasos}")
```

### Resultados esperados del docente
- **Verdes:** 6
- **Amarillos:** 1 (T03)
- **Rojos:** 1 (T06)
- **Promedio de satisfacción:** 4.61
- **Sesiones UIB completadas:** 150
- **Pasos para completar la meta:** 8
