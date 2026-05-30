# S06 — Taller
## Primitivas selectivas: SI-FSI en PSeInt y primer `if` en Python
### TGA04 Fundamentos de Computación para los Negocios · UIB

**Nombre:** ________________________________________  
**ID:** ____________________________________________  
**Fecha:** _________________________________________  
**Programa:** ______________________________________  
**Sección:** _______________________________________  

---

## Instrucciones generales
- Use únicamente los datos exactos del caso NeuroBiz y del contrato UIB.
- En pseudocódigo, escriba sintaxis tipo PSeInt.
- En Python, asuma trabajo en **Thonny** con Python 3.x.
- En esta semana use **solo selectiva simple**: no use `sino`, `elif`, `else` ni ciclos.
- Cuando una condición sea falsa, deje claro que la acción no se ejecuta.

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

### Contrato UIB — datos exactos para el taller
- Sesiones contratadas: **150**
- Sesiones realizadas: **142**
- Pago mensual: **$11.840.000 COP**
- Estudiantes atendidos: **12**
- Estudiantes con mejora ≥ 0.5: **2**
- **U1 = 94.7%**
- **U3 = 16.7%**

## Ejercicio 1. Verdadero o falso antes de programar
Indique si cada condición es **verdadera** o **falsa** usando la tabla del caso.

1. `T06_N4 > 15`  
2. `T03_N4 > 15`  
3. `T01_N4 > 15`  
4. `T06_N1 < 75`  
5. `T03_N1 < 75`  
6. `U3 < 60`  

**Espacio de respuesta**
```text
1.
2.
3.
4.
5.
6.
```

## Ejercicio 2. Pseudocódigo mínimo de alerta por ausentismo
Escriba un algoritmo en PSeInt que:
- lea `n4`,
- muestre `"ALERTA DE AUSENTISMO"` solo si `n4 > 15`.

```pseint
Proceso Ejercicio2



FinProceso
```

## Ejercicio 3. Pseudocódigo con dato exacto de T06
Escriba un pseudocódigo sin `Leer` que cargue directamente `n1 <- 59.7` y muestre `"BAJA OCUPACION"` si `n1 < 75`.

```pseint
Proceso Ejercicio3



FinProceso
```

## Ejercicio 4. Python en Thonny — primer `if`
Complete el siguiente programa para que muestre una alerta cuando `n4 > 15`.

```python
n4 = 19.44

if __________________:
    print("__________________")
```

Luego cambie el valor por `0.00` y describa qué ocurre.

**Respuesta breve:** ________________________________________________

## Ejercicio 5. Dos `if` independientes en PSeInt
Escriba un programa que lea `n1` y `n4` y evalúe dos condiciones independientes:
- Si `n1 < 75`, escribir `"BAJA OCUPACION"`.
- Si `n4 > 15`, escribir `"ALERTA DE AUSENTISMO"`.

> No use `sino`; son dos selectivas simples separadas.

```pseint
Proceso Ejercicio5




FinProceso
```

## Ejercicio 6. Python con el cliente UIB
Escriba un programa en Python que use `u3 = 16.7` y muestre `"REVISAR IMPACTO DEL CONTRATO"` si `u3 < 60`.

```python
u3 = 16.7


```

## Ejercicio 7. Análisis corto del caso
Responda en una o dos líneas:
1. ¿Qué terapeutas quedan en alerta por `N4 > 15`?  
2. ¿Qué terapeuta queda en alerta por `N1 < 75`?  
3. ¿Qué dice esto desde la perspectiva de NeuroBiz y qué dice desde la perspectiva de UIB?  

```text
1.
2.
3.
```

---

# Clave docente
## Ejercicio 1
1. `T06_N4 > 15` → **Verdadera**  
2. `T03_N4 > 15` → **Verdadera**  
3. `T01_N4 > 15` → **Falsa**  
4. `T06_N1 < 75` → **Verdadera**  
5. `T03_N1 < 75` → **Falsa** (75.0 no es menor que 75)  
6. `U3 < 60` → **Verdadera**

## Ejercicio 2
```pseint
Proceso Ejercicio2
    Definir n4 Como Real
    Escribir "Ingrese N4:"
    Leer n4

    Si n4 > 15 Entonces
        Escribir "ALERTA DE AUSENTISMO"
    FinSi
FinProceso
```

## Ejercicio 3
```pseint
Proceso Ejercicio3
    Definir n1 Como Real
    n1 <- 59.7

    Si n1 < 75 Entonces
        Escribir "BAJA OCUPACION"
    FinSi
FinProceso
```

## Ejercicio 4
```python
n4 = 19.44

if n4 > 15:
    print("ALERTA DE AUSENTISMO")
```
Con `n4 = 0.00`, la condición es falsa y el programa no imprime la alerta.

## Ejercicio 5
```pseint
Proceso Ejercicio5
    Definir n1, n4 Como Real
    Escribir "Ingrese N1:"
    Leer n1
    Escribir "Ingrese N4:"
    Leer n4

    Si n1 < 75 Entonces
        Escribir "BAJA OCUPACION"
    FinSi

    Si n4 > 15 Entonces
        Escribir "ALERTA DE AUSENTISMO"
    FinSi
FinProceso
```

## Ejercicio 6
```python
u3 = 16.7

if u3 < 60:
    print("REVISAR IMPACTO DEL CONTRATO")
```

## Ejercicio 7
1. Alertas por `N4 > 15`: **T03 y T06**.  
2. Alerta por `N1 < 75`: **T06**.  
3. **NeuroBiz** observa desempeño interno y seguimiento a terapeutas; **UIB** observa si el contrato genera valor, por eso `U3 = 16.7%` obliga a revisar impacto aunque `U1 = 94.7%` sea alto.
