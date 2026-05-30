# S08 — Taller de Semana 8
## MQ-FMQ: primeros `while` en PSeInt y Python
### TGA04 Fundamentos de Computación para los Negocios · UIB

**Nombre:** ______________________________  
**ID:** _________________________________  
**Fecha:** ______________________________  
**Programa:** ___________________________  
**Sección:** ____________________________

---

## Instrucciones generales
- Resuelva primero en **pseudocódigo PSeInt** y luego pase la misma lógica a **Python 3.x en Thonny**.
- Subraye en cada ejercicio tres cosas: **inicialización, condición y actualización**.
- Si el resultado no sale, haga un trazado de al menos **3 iteraciones** antes de pedir ayuda.
- Use los datos exactos del caso cuando la guía lo solicite.
- En los ejercicios con listas en Python, ejecute con **F5** en Thonny y guarde el archivo.

---

## Tabla guía del caso
| ID | Nombre | Disp | Realizadas | Canceladas | Satisfacción | N1 | N4 |
|---|---|---:|---:|---:|---:|---:|---:|
| T01 | Ana Ramos | 80 | 68 | 9 | 4.7 | 85.0 | 11.25 |
| T02 | Carlos Mejía | 72 | 71 | 2 | 4.9 | 98.6 | 2.78 |
| T03 | Luz Torres | 72 | 54 | 14 | 4.2 | 75.0 | 19.44 |
| T04 | Mario Suárez | 80 | 77 | 4 | 4.8 | 96.3 | 5.00 |
| T05 | Paula Vega | 60 | 58 | 1 | 5.0 | 96.7 | 1.67 |
| T06 | Diego Ríos | 72 | 43 | 22 | 3.9 | 59.7 | 30.56 |
| T07 | Sandra Ospina | 72 | 69 | 5 | 4.6 | 95.8 | 6.94 |
| T08 | Héctor Niño | 80 | 80 | 0 | 4.8 | 100.0 | 0.00 |

**Dato para comparar con el parcial anterior:**
```text
Total manual de realizadas = 520
```

---

## Ejercicio 1. `while` simple de 1 a 5
Escriba un algoritmo que imprima los números del 1 al 5 usando `while`.

### PSeInt
```pseint
Proceso Ejercicio1



FinProceso
```

### Python
```python
# Ejercicio 1


```

---

## Ejercicio 2. `while` con acumulador
Lea o simule los números del 1 al 5 y calcule la suma total con `while`.

**Preguntas de control:**
- ¿En qué variable guarda la suma?
- ¿Qué variable cambia en cada vuelta?

### PSeInt
```pseint
Proceso Ejercicio2



FinProceso
```

### Python
```python
# Ejercicio 2


```

---

## Ejercicio 3. Total de realizadas T01–T08 con `while`
Construya un programa que recorra la lista exacta de sesiones realizadas y calcule el total.

```text
realizadas = [68, 71, 54, 77, 58, 43, 69, 80]
```

a) Muestre el total final.  
b) Compare con el valor manual del parcial anterior.  
c) Escriba una conclusión: ¿el `while` confirmó el cálculo manual?

### PSeInt
```pseint
Proceso Ejercicio3



FinProceso
```

### Python
```python
# Ejercicio 3
realizadas = [68, 71, 54, 77, 58, 43, 69, 80]


```

---

## Ejercicio 4. Promedio N1 con `while`
Use la lista exacta de N1 para calcular el promedio del equipo.

```text
n1 = [85.0, 98.6, 75.0, 96.3, 96.7, 59.7, 95.8, 100.0]
```

Además, cuente cuántos terapeutas cumplen `N1 >= 75`.

### PSeInt
```pseint
Proceso Ejercicio4



FinProceso
```

### Python
```python
# Ejercicio 4
n1 = [85.0, 98.6, 75.0, 96.3, 96.7, 59.7, 95.8, 100.0]


```

---

## Ejercicio 5. `while` con condición de negocio
Modele en pseudocódigo y en Python esta situación:

> “Mientras no mejore la lectura, continuar sesiones de apoyo”.

Use estas reglas:
- `mejora_lectura` inicia en **Falso**.
- `sesiones_apoyo` inicia en **0**.
- El ciclo no debe superar **20 sesiones**.
- En cada repetición debe imprimirse: `Continuar apoyo lector`.

**Contexto humano:** T03 (Luz Torres) atiende dislexia y tiene **14 canceladas**; eso muestra que el apoyo puede interrumpirse si no hay seguimiento.

### PSeInt
```pseint
Proceso Ejercicio5



FinProceso
```

### Python
```python
# Ejercicio 5


```

---

## Ejercicio 6. Detectar el ciclo infinito
El siguiente código tiene un problema. Señálelo y corríjalo.

### PSeInt con error
```pseint
Proceso ErrorMientras
    Definir indice Como Entero
    indice <- 1

    Mientras Que indice <= 5 Hacer
        Escribir indice
    FinMientras
FinProceso
```

### Python con error
```python
indice = 1
while indice <= 5:
    print(indice)
```

**Explique en una frase:** ¿por qué nunca termina?

---

# CLAVE DOCENTE

## Respuesta Ejercicio 1
### PSeInt
```pseint
Proceso Ejercicio1
    Definir contador Como Entero
    contador <- 1

    Mientras Que contador <= 5 Hacer
        Escribir contador
        contador <- contador + 1
    FinMientras
FinProceso
```

### Python
```python
contador = 1
while contador <= 5:
    print(contador)
    contador = contador + 1
```

**Salida:** `1 2 3 4 5`

---

## Respuesta Ejercicio 2
### PSeInt
```pseint
Proceso Ejercicio2
    Definir numero, suma Como Entero
    numero <- 1
    suma <- 0

    Mientras Que numero <= 5 Hacer
        suma <- suma + numero
        numero <- numero + 1
    FinMientras

    Escribir "Suma: ", suma
FinProceso
```

### Python
```python
numero = 1
suma = 0

while numero <= 5:
    suma = suma + numero
    numero = numero + 1

print("Suma:", suma)
```

**Resultado:** `15`

---

## Respuesta Ejercicio 3
### PSeInt
```pseint
Proceso Ejercicio3
    Dimension realizadas[8]
    Definir indice, total Como Entero

    realizadas[1] <- 68
    realizadas[2] <- 71
    realizadas[3] <- 54
    realizadas[4] <- 77
    realizadas[5] <- 58
    realizadas[6] <- 43
    realizadas[7] <- 69
    realizadas[8] <- 80

    indice <- 1
    total <- 0

    Mientras Que indice <= 8 Hacer
        total <- total + realizadas[indice]
        indice <- indice + 1
    FinMientras

    Escribir "Total realizadas: ", total
FinProceso
```

### Python
```python
realizadas = [68, 71, 54, 77, 58, 43, 69, 80]
indice = 0
total = 0

while indice < len(realizadas):
    total = total + realizadas[indice]
    indice = indice + 1

print("Total realizadas:", total)
```

**Resultado correcto:** `520`  
**Conclusión:** sí, el `while` confirma el cálculo manual del parcial anterior.

---

## Respuesta Ejercicio 4
### PSeInt
```pseint
Proceso Ejercicio4
    Dimension n1[8]
    Definir indice, cumplen Como Entero
    Definir suma, promedio Como Real

    n1[1] <- 85.0
    n1[2] <- 98.6
    n1[3] <- 75.0
    n1[4] <- 96.3
    n1[5] <- 96.7
    n1[6] <- 59.7
    n1[7] <- 95.8
    n1[8] <- 100.0

    indice <- 1
    suma <- 0
    cumplen <- 0

    Mientras Que indice <= 8 Hacer
        suma <- suma + n1[indice]
        Si n1[indice] >= 75 Entonces
            cumplen <- cumplen + 1
        FinSi
        indice <- indice + 1
    FinMientras

    promedio <- suma / 8
    Escribir "Promedio N1: ", promedio
    Escribir "Cumplen N1 >= 75: ", cumplen
FinProceso
```

### Python
```python
n1 = [85.0, 98.6, 75.0, 96.3, 96.7, 59.7, 95.8, 100.0]
indice = 0
suma = 0
cumplen = 0

while indice < len(n1):
    suma = suma + n1[indice]
    if n1[indice] >= 75:
        cumplen = cumplen + 1
    indice = indice + 1

promedio = suma / len(n1)
print("Promedio N1:", round(promedio, 1))
print("Cumplen N1 >= 75:", cumplen)
```

**Resultados correctos:**
- `Promedio N1 = 88.4%`
- `Cumplen N1 >= 75 = 7`

---

## Respuesta Ejercicio 5
### PSeInt
```pseint
Proceso Ejercicio5
    Definir mejora_lectura Como Logico
    Definir sesiones_apoyo Como Entero

    mejora_lectura <- Falso
    sesiones_apoyo <- 0

    Mientras Que mejora_lectura = Falso Y sesiones_apoyo < 20 Hacer
        Escribir "Continuar apoyo lector"
        sesiones_apoyo <- sesiones_apoyo + 1
    FinMientras
FinProceso
```

### Python
```python
mejora_lectura = False
sesiones_apoyo = 0

while mejora_lectura == False and sesiones_apoyo < 20:
    print("Continuar apoyo lector")
    sesiones_apoyo = sesiones_apoyo + 1
```

**Comentario docente:** el límite de 20 evita un ciclo sin salida y obliga a pensar en criterios de reevaluación.

---

## Respuesta Ejercicio 6
**Problema:** la variable `indice` nunca cambia, por eso la condición `indice <= 5` permanece verdadera.

### Corrección PSeInt
```pseint
Proceso ErrorMientrasCorregido
    Definir indice Como Entero
    indice <- 1

    Mientras Que indice <= 5 Hacer
        Escribir indice
        indice <- indice + 1
    FinMientras
FinProceso
```

### Corrección Python
```python
indice = 1
while indice <= 5:
    print(indice)
    indice = indice + 1
```

**Frase esperada del estudiante:** “Nunca termina porque la variable de control no se actualiza”.
