# S13 — Taller

## Programa NeuroBiz Final: Encuentra y Corrige los Errores

**Curso:** TGA04 — Fundamentos de Computación para los Negocios  
**Semana:** 13  
**Lenguaje:** Python 3.x en Thonny

## Propósito
Detectar y corregir errores reales de un programa integrador en Python. Debes identificar:
- **2 SyntaxError**
- **2 errores de ejecución (runtime)**
- **3 errores lógicos**

## Instrucciones
1. Lee el código completo antes de corregir.
2. Marca la **línea**, el **tipo de error**, la **descripción** y la **corrección**.
3. Si deseas copiarlo a Thonny, **omite la numeración de líneas**.
4. Corrige primero sintaxis, luego ejecución y al final lógica.

## Código “roto”
```python
01 terapeutas = [
02     {"id": "T01", "nombre": "Ana Ramos", "realizadas": 68, "disponibles": 80, "canceladas": 9, "satisfaccion": 4.7},
03     {"id": "T02", "nombre": "Carlos Mejía", "realizadas": 71, "disponibles": 72, "canceladas": 2, "satisfaccion": 4.9},
04     {"id": "T03", "nombre": "Luz Torres", "realizadas": 54, "disponibles": 72, "canceladas": 14, "satisfaccion": 4.2},
05     {"id": "T04", "nombre": "Mario Suárez", "realizadas": 77, "disponibles": 80, "canceladas": 4, "satisfaccion": 4.8},
06     {"id": "T05", "nombre": "Paula Vega", "realizadas": 58, "disponibles": 60, "canceladas": 1, "satisfaccion": 5.0},
07     {"id": "T06", "nombre": "Diego Ríos", "realizadas": 43, "disponibles": 72, "canceladas": 22, "satisfaccion": 3.9},
08     {"id": "T07", "nombre": "Sandra Ospina", "realizadas": 69, "disponibles": 72, "canceladas": 5, "satisfaccion": 4.6},
09     {"id": "T08", "nombre": "Héctor Niño", "realizadas": 60, "disponibles": 60, "canceladas": 0, "satisfaccion": 4.8}
10 ]
11 
12 alertas = []
13 suma_satisfaccion = 0
14 sesiones_disponibles = 0
15 
16 for terapeuta-item in terapeutas:
17     n1 = terapeuta["realizadas"] / terapeuta["realizadas"] * 100
18     n4 = terapeuta["canceladas"] / sesiones_disponibles * 100
19 
20     if n1 >= 75 and n4 <= 15
21         estado = "Verde"
22     elif n1 < 75 and n4 > 15:
23         estado = "Rojo"
24     else:
25         estado = "Amarillo"
26 
27     if n1 > 75:
28         alertas.append(terapeuta["nombre"])
29 
30     suma_satisfaccion += terapeuta["satisfaccion"]
31     print(terapeuta["nombre"], "->", estado, "N1:", round(n1, 2), "N4:", round(n4, 2))
32 
33 promedio_satisfaccion = suma_satisfaccion / 9
34 print("Promedio de satisfacción:", round(promedio_satisfaccion, 2))
35 print("Terapeuta en alerta destacado:", alertas[10])
```

## Tabla para completar por el estudiante
| Línea | Tipo de error | Descripción | Corrección |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

---

## Código correcto y completo
```python
# Programa NeuroBiz Final - versión corregida
terapeutas = [
    {"id": "T01", "nombre": "Ana Ramos", "realizadas": 68, "disponibles": 80, "canceladas": 9, "satisfaccion": 4.7},
    {"id": "T02", "nombre": "Carlos Mejía", "realizadas": 71, "disponibles": 72, "canceladas": 2, "satisfaccion": 4.9},
    {"id": "T03", "nombre": "Luz Torres", "realizadas": 54, "disponibles": 72, "canceladas": 14, "satisfaccion": 4.2},
    {"id": "T04", "nombre": "Mario Suárez", "realizadas": 77, "disponibles": 80, "canceladas": 4, "satisfaccion": 4.8},
    {"id": "T05", "nombre": "Paula Vega", "realizadas": 58, "disponibles": 60, "canceladas": 1, "satisfaccion": 5.0},
    {"id": "T06", "nombre": "Diego Ríos", "realizadas": 43, "disponibles": 72, "canceladas": 22, "satisfaccion": 3.9},
    {"id": "T07", "nombre": "Sandra Ospina", "realizadas": 69, "disponibles": 72, "canceladas": 5, "satisfaccion": 4.6},
    {"id": "T08", "nombre": "Héctor Niño", "realizadas": 60, "disponibles": 60, "canceladas": 0, "satisfaccion": 4.8}
]

alertas = []
suma_satisfaccion = 0

for terapeuta in terapeutas:
    # Cálculo correcto de indicadores
    n1 = terapeuta["realizadas"] / terapeuta["disponibles"] * 100
    n4 = terapeuta["canceladas"] / terapeuta["disponibles"] * 100

    # Clasificación por semáforo
    if n1 >= 75 and n4 <= 15:
        estado = "Verde"
    elif n1 < 75 and n4 > 15:
        estado = "Rojo"
    else:
        estado = "Amarillo"

    # En alerta quedan los que no están en verde
    if estado != "Verde":
        alertas.append(terapeuta["nombre"])

    suma_satisfaccion += terapeuta["satisfaccion"]
    print(f"{terapeuta['nombre']} -> {estado} | N1: {n1:.2f}% | N4: {n4:.2f}%")

promedio_satisfaccion = suma_satisfaccion / len(terapeutas)
print(f"\nPromedio de satisfacción: {promedio_satisfaccion:.2f}")
print("Terapeutas en alerta:", ", ".join(alertas))
```

## Tabla de respuestas
| Línea | Tipo de error | Descripción | Corrección esperada |
|---|---|---|---|
| 16 | SyntaxError | `terapeuta-item` usa un guion; no es un identificador válido en Python. | `for terapeuta in terapeutas:` |
| 17 | Error lógico | N1 se divide por `realizadas` en vez de `disponibles`. | `n1 = terapeuta["realizadas"] / terapeuta["disponibles"] * 100` |
| 18 | RuntimeError | División por cero porque `sesiones_disponibles = 0`. | Dividir entre `terapeuta["disponibles"]`. |
| 20 | SyntaxError | Falta `:` al final del `if`. | `if n1 >= 75 and n4 <= 15:` |
| 27 | Error lógico | La alerta se activa con `>` en vez de usar una condición de incumplimiento. | `if estado != "Verde":` o `if n1 < 75 or n4 > 15:` |
| 33 | Error lógico | El promedio se divide entre 9, pero hay 8 terapeutas. | `promedio_satisfaccion = suma_satisfaccion / len(terapeutas)` |
| 35 | RuntimeError | `alertas[10]` intenta acceder a una posición inexistente. | Mostrar toda la lista o verificar longitud antes de acceder. |

## Resultado esperado al corregir
- **Verdes:** Ana Ramos, Carlos Mejía, Mario Suárez, Paula Vega, Sandra Ospina, Héctor Niño.
- **Amarillo:** Luz Torres.
- **Rojo:** Diego Ríos.
- **Promedio de satisfacción:** **4.61**.
- **Terapeutas en alerta:** Luz Torres y Diego Ríos.
