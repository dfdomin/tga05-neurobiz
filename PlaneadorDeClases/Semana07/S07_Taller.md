# S07 — Taller
## SI-SINO-FSI, operadores lógicos y clasificación de terapeutas
### TGA04 Fundamentos de Computación para los Negocios · UIB

**Nombre:** ________________________________________  
**ID:** ____________________________________________  
**Fecha:** _________________________________________  
**Programa:** ______________________________________  
**Sección:** _______________________________________  

---

## Instrucciones generales
- Use los datos exactos del caso NeuroBiz.
- En pseudocódigo use sintaxis tipo PSeInt.
- En Python use formato compatible con Thonny y Python 3.x.
- En este taller sí puede usar `SI-SINO-FSI`, operadores lógicos y `if/elif/else`.
- Para decisión múltiple, puede usar `Segun` en PSeInt y `match-case` o `if/elif/else` en Python.

## Tabla guía del caso
| ID | Nombre | Especialidad | Disp/mes | Realizadas | Canceladas | Satisfacción | N1 | N4 |
|---|---|---|---:|---:|---:|---:|---:|---:|
| T01 | Ana Ramos | Psicología | 80 | 68 | 9 | 4.7 | 85.0% | 11.25% |
| T02 | Carlos Mejía | Fonoaudiología | 72 | 71 | 2 | 4.9 | 98.6% | 2.78% |
| T03 | Luz Torres | Terapia Ocupacional | 72 | 54 | 14 | 4.2 | 75.0% | 19.44% |
| T04 | Mario Suárez | Psicología | 80 | 77 | 4 | 4.8 | 96.3% | 5.00% |
| T05 | Paula Vega | Neuropsicología | 60 | 58 | 1 | 5.0 | 96.7% | 1.67% |
| T06 | Diego Ríos | Fonoaudiología | 72 | 43 | 22 | 3.9 | 59.7% | 30.56% |
| T07 | Sandra Ospina | Terapia Ocupacional | 72 | 69 | 5 | 4.6 | 95.8% | 6.94% |
| T08 | Héctor Niño | Psicología | 80 | 80 | 0 | 4.8 | 100.0% | 0.00% |

## Regla de clasificación obligatoria para el taller
- **Verde:** `N1 >= 95` y `N4 <= 10`
- **Amarillo:** `N1 >= 75` y `N4 <= 15`
- **Rojo:** cualquier otro caso

## Ejercicio 1. SI-SINO-FSI básico
Escriba un algoritmo en PSeInt que:
- lea `n4`,
- si `n4 > 15` muestre `"ALERTA"`,
- si no, muestre `"CONTROLADO"`.

```pseint
Proceso Ejercicio1



FinProceso
```

## Ejercicio 2. Operadores lógicos en papel
Clasifique como **verdadero** o **falso** las siguientes expresiones.

1. Para T08: `N1 >= 95 Y N4 <= 10`  
2. Para T01: `N1 >= 95 Y N4 <= 10`  
3. Para T01: `N1 >= 75 Y N4 <= 15`  
4. Para T03: `N1 < 75 O N4 > 15`  
5. Para T06: `N1 < 75 O N4 > 15`  
6. Para T05: `NO (N4 > 15)`  

```text
1.
2.
3.
4.
5.
6.
```

## Ejercicio 3. Clasificación completa de T01-T08
Con la regla de colores dada, complete la tabla.

| ID | Estado |
|---|---|
| T01 | |
| T02 | |
| T03 | |
| T04 | |
| T05 | |
| T06 | |
| T07 | |
| T08 | |

## Ejercicio 4. Python `if/elif/else`
Complete el programa para clasificar un terapeuta.

```python
n1 = 96.7
n4 = 1.67

if __________________________:
    estado = "VERDE"
elif ________________________:
    estado = "AMARILLO"
else:
    estado = "ROJO"

print(estado)
```

Luego cambie los valores por `n1 = 85.0` y `n4 = 11.25`. ¿Qué salida debe aparecer? __________________

## Ejercicio 5. Pseudocódigo con riesgo
Escriba un programa que lea `n1` y `n4` y muestre:
- `"RIESGO"` si `n1 < 75 O n4 > 15`
- `"ESTABLE"` en caso contrario

```pseint
Proceso Ejercicio5




FinProceso
```

## Ejercicio 6. Decisión múltiple por especialidad
Escriba una decisión múltiple que muestre un mensaje distinto según la especialidad:
- Psicología → `"Ruta emocional"`
- Fonoaudiología → `"Ruta de lenguaje"`
- Terapia Ocupacional → `"Ruta funcional"`
- Neuropsicología → `"Ruta cognitiva"`

Puede hacerlo en PSeInt o Python.

```text
Escriba aquí su solución:
```

## Ejercicio 7. Interpretación corta del caso
Responda en 2 o 3 líneas:
1. ¿Qué terapeutas quedan en rojo y por qué?  
2. ¿Qué terapeutas quedan en verde?  
3. ¿Cómo ayuda esta clasificación a NeuroBiz y cómo ayuda a UIB?  

```text
1.
2.
3.
```

---

# Clave docente
## Ejercicio 1
```pseint
Proceso Ejercicio1
    Definir n4 Como Real
    Escribir "Ingrese N4:"
    Leer n4

    Si n4 > 15 Entonces
        Escribir "ALERTA"
    SiNo
        Escribir "CONTROLADO"
    FinSi
FinProceso
```

## Ejercicio 2
1. **Verdadero**  
2. **Falso**  
3. **Verdadero**  
4. **Verdadero**  
5. **Verdadero**  
6. **Verdadero**

## Ejercicio 3
| ID | Estado correcto |
|---|---|
| T01 | Amarillo |
| T02 | Verde |
| T03 | Rojo |
| T04 | Verde |
| T05 | Verde |
| T06 | Rojo |
| T07 | Verde |
| T08 | Verde |

## Ejercicio 4
```python
n1 = 96.7
n4 = 1.67

if n1 >= 95 and n4 <= 10:
    estado = "VERDE"
elif n1 >= 75 and n4 <= 15:
    estado = "AMARILLO"
else:
    estado = "ROJO"

print(estado)
```
Con `n1 = 85.0` y `n4 = 11.25`, la salida correcta es **AMARILLO**.

## Ejercicio 5
```pseint
Proceso Ejercicio5
    Definir n1, n4 Como Real
    Escribir "Ingrese N1:"
    Leer n1
    Escribir "Ingrese N4:"
    Leer n4

    Si n1 < 75 O n4 > 15 Entonces
        Escribir "RIESGO"
    SiNo
        Escribir "ESTABLE"
    FinSi
FinProceso
```

## Ejercicio 6
### Opción PSeInt
```pseint
Segun especialidad Hacer
    "Psicología":
        Escribir "Ruta emocional"
    "Fonoaudiología":
        Escribir "Ruta de lenguaje"
    "Terapia Ocupacional":
        Escribir "Ruta funcional"
    "Neuropsicología":
        Escribir "Ruta cognitiva"
    De Otro Modo:
        Escribir "Especialidad no registrada"
FinSegun
```

### Opción Python
```python
match especialidad:
    case "Psicología":
        print("Ruta emocional")
    case "Fonoaudiología":
        print("Ruta de lenguaje")
    case "Terapia Ocupacional":
        print("Ruta funcional")
    case "Neuropsicología":
        print("Ruta cognitiva")
    case _:
        print("Especialidad no registrada")
```

## Ejercicio 7
1. En rojo quedan **T03** y **T06** porque incumplen la regla por ausentismo alto y, en el caso de T06, también por ocupación baja.  
2. En verde quedan **T02, T04, T05, T07 y T08**.  
3. A **NeuroBiz** le sirve para priorizar seguimiento interno; a **UIB** le ayuda a interpretar si el servicio contratado está generando una operación confiable y consistente para sus estudiantes.
