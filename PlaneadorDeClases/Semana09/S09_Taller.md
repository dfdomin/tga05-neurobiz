# S09 — Taller de Semana 9
## PARA-FPARA, `for` y HH-FHH
### TGA04 Fundamentos de Computación para los Negocios · UIB

**Nombre:** ______________________________  
**ID:** _________________________________  
**Fecha:** ______________________________  
**Programa:** ___________________________  
**Sección:** ____________________________

---

## Instrucciones generales
- Resuelva en **PSeInt** y luego en **Python 3.x con Thonny**.
- Identifique en cada ejercicio si la mejor estructura es `for`, `while` o HH-FHH.
- Use los datos exactos del caso cuando aparezcan en la guía.
- En Python, ejecute con **F5** y conserve la salida para revisión.
- En HH-FHH recuerde: el bloque debe ejecutarse **al menos una vez**.

---

## Tabla guía del caso
| ID | Nombre | Realizadas | Canceladas | Satisfacción | N1 | N4 |
|---|---|---:|---:|---:|---:|---:|
| T01 | Ana Ramos | 68 | 9 | 4.7 | 85.0 | 11.25 |
| T02 | Carlos Mejía | 71 | 2 | 4.9 | 98.6 | 2.78 |
| T03 | Luz Torres | 54 | 14 | 4.2 | 75.0 | 19.44 |
| T04 | Mario Suárez | 77 | 4 | 4.8 | 96.3 | 5.00 |
| T05 | Paula Vega | 58 | 1 | 5.0 | 96.7 | 1.67 |
| T06 | Diego Ríos | 43 | 22 | 3.9 | 59.7 | 30.56 |
| T07 | Sandra Ospina | 69 | 5 | 4.6 | 95.8 | 6.94 |
| T08 | Héctor Niño | 80 | 0 | 4.8 | 100.0 | 0.00 |

**Contrato UIB:** 150 sesiones/mes, 142 realizadas, $11.840.000 COP, 12 estudiantes, `U1 = 94.7%`, `U3 = 16.7%`.

---

## Ejercicio 1. `for` simple con contador
Imprima del 1 al 10 usando PARA-FPARA en PSeInt y `for` en Python.

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

## Ejercicio 2. Acumulador con `for`
Use la lista de canceladas y calcule el total mensual del equipo.

```text
canceladas = [9, 2, 14, 4, 1, 22, 5, 0]
```

Luego escriba una conclusión corta: ¿el total muestra un equipo sin problemas o con focos de riesgo?

### PSeInt
```pseint
Proceso Ejercicio2



FinProceso
```

### Python
```python
# Ejercicio 2
canceladas = [9, 2, 14, 4, 1, 22, 5, 0]


```

---

## Ejercicio 3. Promedio de satisfacción T01–T08
Calcule con `for` el promedio de satisfacción del equipo y determine si el resultado general es **mayor o igual a 4.5**.

```text
satisfacciones = [4.7, 4.9, 4.2, 4.8, 5.0, 3.9, 4.6, 4.8]
```

### PSeInt
```pseint
Proceso Ejercicio3



FinProceso
```

### Python
```python
# Ejercicio 3
satisfacciones = [4.7, 4.9, 4.2, 4.8, 5.0, 3.9, 4.6, 4.8]


```

---

## Ejercicio 4. HH-FHH / Hacer-Hasta
Diseñe un algoritmo que muestre un menú al menos una vez y termine solo cuando la persona escriba **2**.

### PSeInt
> Use la forma práctica de PSeInt: `Repetir ... Hasta Que`

```pseint
Proceso Ejercicio4



FinProceso
```

### Python
> Simule HH-FHH con `while True` y `break`.

```python
# Ejercicio 4


```

---

## Ejercicio 5. Análisis UIB con `for`
Use la lista de mejoras fuertes de 12 estudiantes. `1` significa que sí mejoró al menos 0.5; `0`, que no.

```text
mejoras = [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
```

a) Cuente cuántos estudiantes mejoraron.  
b) Calcule `U3`.  
c) Muestre también `U1` usando los datos del contrato.  
d) Escriba una conclusión breve desde doble perspectiva: **NeuroBiz vs UIB**.

### PSeInt
```pseint
Proceso Ejercicio5



FinProceso
```

### Python
```python
# Ejercicio 5
mejoras = [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]


```

---

## Ejercicio 6. ¿`for` o `while`?
Responda con una frase técnica cada caso:
1. Recorrer exactamente los 8 terapeutas del reporte.  
2. Repetir apoyo lector mientras no mejore la lectura.  
3. Mostrar un menú y validarlo al menos una vez.  

```text
1.
2.
3.
```

---

# CLAVE DOCENTE

## Respuesta Ejercicio 1
### PSeInt
```pseint
Proceso Ejercicio1
    Definir i Como Entero

    Para i <- 1 Hasta 10 Con Paso 1 Hacer
        Escribir i
    FinPara
FinProceso
```

### Python
```python
for i in range(1, 11):
    print(i)
```

---

## Respuesta Ejercicio 2
### PSeInt
```pseint
Proceso Ejercicio2
    Dimension canceladas[8]
    Definir i, total Como Entero

    canceladas[1] <- 9
    canceladas[2] <- 2
    canceladas[3] <- 14
    canceladas[4] <- 4
    canceladas[5] <- 1
    canceladas[6] <- 22
    canceladas[7] <- 5
    canceladas[8] <- 0

    total <- 0
    Para i <- 1 Hasta 8 Con Paso 1 Hacer
        total <- total + canceladas[i]
    FinPara

    Escribir "Total canceladas: ", total
FinProceso
```

### Python
```python
canceladas = [9, 2, 14, 4, 1, 22, 5, 0]
total = 0

for valor in canceladas:
    total = total + valor

print("Total canceladas:", total)
```

**Resultado correcto:** `57`  
**Conclusión esperada:** el total general no invalida todo el servicio, pero sí muestra focos de riesgo, sobre todo por T03 y T06.

---

## Respuesta Ejercicio 3
### PSeInt
```pseint
Proceso Ejercicio3
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
    Escribir "Promedio: ", promedio

    Si promedio >= 4.5 Entonces
        Escribir "Resultado general favorable"
    SiNo
        Escribir "Resultado general por revisar"
    FinSi
FinProceso
```

### Python
```python
satisfacciones = [4.7, 4.9, 4.2, 4.8, 5.0, 3.9, 4.6, 4.8]
suma = 0

for valor in satisfacciones:
    suma = suma + valor

promedio = suma / len(satisfacciones)
print("Promedio:", round(promedio, 2))
if promedio >= 4.5:
    print("Resultado general favorable")
else:
    print("Resultado general por revisar")
```

**Resultado correcto:** `4.61` y **sí es mayor o igual a 4.5**.

---

## Respuesta Ejercicio 4
### PSeInt
```pseint
Proceso Ejercicio4
    Definir opcion Como Entero

    Repetir
        Escribir "1. Continuar"
        Escribir "2. Salir"
        Leer opcion
    Hasta Que opcion = 2
FinProceso
```

### Python
```python
while True:
    opcion = int(input("1. Continuar / 2. Salir: "))
    if opcion == 2:
        break
```

**Comentario docente:** el menú aparece al menos una vez incluso si la persona decide salir de inmediato.

---

## Respuesta Ejercicio 5
### PSeInt
```pseint
Proceso Ejercicio5
    Dimension mejoras[12]
    Definir i, contador Como Entero
    Definir u1, u3 Como Real

    mejoras[1] <- 1
    mejoras[2] <- 0
    mejoras[3] <- 0
    mejoras[4] <- 0
    mejoras[5] <- 0
    mejoras[6] <- 1
    mejoras[7] <- 0
    mejoras[8] <- 0
    mejoras[9] <- 0
    mejoras[10] <- 0
    mejoras[11] <- 0
    mejoras[12] <- 0

    contador <- 0
    Para i <- 1 Hasta 12 Con Paso 1 Hacer
        Si mejoras[i] = 1 Entonces
            contador <- contador + 1
        FinSi
    FinPara

    u3 <- (contador / 12) * 100
    u1 <- (142 / 150) * 100

    Escribir "Mejoran: ", contador
    Escribir "U3: ", u3
    Escribir "U1: ", u1
FinProceso
```

### Python
```python
mejoras = [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
contador = 0

for valor in mejoras:
    if valor == 1:
        contador = contador + 1

u3 = (contador / len(mejoras)) * 100
u1 = (142 / 150) * 100

print("Mejoran:", contador)
print("U3:", round(u3, 1))
print("U1:", round(u1, 1))
```

**Resultados correctos:**
- `Mejoran = 2`
- `U3 = 16.7%`
- `U1 = 94.7%`

**Conclusión esperada:** NeuroBiz puede mostrar buena utilización del contrato, pero UIB debe cuestionar el valor final porque la mejora fuerte sigue baja.

---

## Respuesta Ejercicio 6
1. **`for`**, porque el número de terapeutas ya es conocido: 8.  
2. **`while`**, porque depende de una condición abierta de negocio: que mejore la lectura.  
3. **HH-FHH**, porque el menú debe mostrarse al menos una vez antes de validar la salida.
