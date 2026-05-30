# S08 — Material de Estudio
## MQ-FMQ: ciclo MIENTRAS QUE en PSeInt y `while` en Python 3.x
### TGA04 Fundamentos de Computación para los Negocios · UIB · Semana 8

**RA2:** Formular soluciones algorítmicas con primitivas repetitivas.  
**Herramientas:** PSeInt para pseudocódigo, Thonny para Python 3.x.  
**Caso transversal:** NeuroBiz (proveedor: eficiencia) y UIB (cliente: valor).

---

## 1. Idea central de la semana
Un ciclo repetitivo sirve para **hacer varias veces la misma acción mientras una condición siga siendo verdadera**. En esta semana esa idea se formaliza con **MQ-FMQ** en pseudocódigo y con `while` en Python.

La pregunta base es siempre la misma:

> **¿Qué condición se revisa antes de entrar al ciclo y qué variable cambia dentro del ciclo para que este termine?**

Si el estudiante sabe responder eso, ya puede leer, escribir y depurar un `while`.

---

## 2. Datos exactos del caso NeuroBiz + UIB

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

**Umbrales:** `N1 >= 75%` y `N4 <= 15%`  
**Contrato UIB:** 150 sesiones/mes, 142 realizadas, $11.840.000 COP, 12 estudiantes, `U3 = 16.7%` 🔴, `U1 = 94.7%` ✅.

---

## 3. ¿Qué es MQ-FMQ?
**MQ-FMQ** significa **Mientras Que ... Fin Mientras Que**. Su lógica es:
1. Revisar una condición al inicio.
2. Si la condición es verdadera, ejecutar el cuerpo del ciclo.
3. Cambiar la variable de control.
4. Volver a evaluar la condición.
5. Salir cuando la condición se vuelva falsa.

### 3.1 Plantilla en pseudocódigo PSeInt
```pseint
Mientras Que condicion Hacer
    // instrucciones
    // actualización necesaria
FinMientras
```

### 3.2 Traducción a Python
```python
while condicion:
    # instrucciones
    # actualización necesaria
```

**Diferencia clave:** la condición se evalúa **antes** de entrar. Si arranca falsa, el cuerpo no se ejecuta ni una sola vez.

---

## 4. Anatomía mínima de un `while`

| Pieza | Pregunta guía | Ejemplo |
|---|---|---|
| Inicialización | ¿Con qué valor empieza la variable de control? | `indice <- 0` |
| Condición | ¿Qué debe ser verdadero para repetir? | `indice < 8` |
| Cuerpo | ¿Qué trabajo hace cada vuelta? | sumar, contar, imprimir |
| Actualización | ¿Qué cambia para acercarse al final? | `indice <- indice + 1` |

Si falta una de esas cuatro partes, el ciclo normalmente queda mal diseñado.

---

## 5. Ejemplo 1 — `while` con contador simple

### PSeInt
```pseint
Proceso ContarDel1Al5
    Definir contador Como Entero
    contador <- 1

    Mientras Que contador <= 5 Hacer
        Escribir contador
        contador <- contador + 1
    FinMientras
FinProceso
```

### Python (Thonny)
```python
contador = 1
while contador <= 5:
    print(contador)
    contador = contador + 1
```

**Salida esperada:** `1 2 3 4 5`

---

## 6. Ejemplo 2 — Acumular N1 del equipo NeuroBiz con `while`
Este ejemplo usa exactamente los N1 ya calculados del caso:

```text
[85.0, 98.6, 75.0, 96.3, 96.7, 59.7, 95.8, 100.0]
```

### Python
```python
n1 = [85.0, 98.6, 75.0, 96.3, 96.7, 59.7, 95.8, 100.0]
indice = 0
suma = 0

while indice < len(n1):
    suma = suma + n1[indice]
    indice = indice + 1

promedio = suma / len(n1)
print("Suma N1:", suma)
print("Promedio N1:", round(promedio, 1))
```

### PSeInt
```pseint
Proceso PromedioN1ConMientras
    Dimension n1[8]
    Definir indice Como Entero
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

    Mientras Que indice <= 8 Hacer
        suma <- suma + n1[indice]
        indice <- indice + 1
    FinMientras

    promedio <- suma / 8
    Escribir "Suma N1: ", suma
    Escribir "Promedio N1: ", promedio
FinProceso
```

**Resultado correcto:**
- `Suma N1 = 707.1`
- `Promedio N1 = 88.4%` aproximadamente

---

## 7. Ejemplo 3 — Acumular sesiones realizadas y comparar con la suma manual
El parcial anterior sumó manualmente las realizadas:

```text
68 + 71 + 54 + 77 + 58 + 43 + 69 + 80 = 520
```

Ahora el `while` debe llegar al mismo total.

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

**Salida esperada:** `Total realizadas: 520`

**Lectura del caso:**
- **Proveedor (NeuroBiz):** 520 realizadas muestran volumen operativo del equipo.
- **Cliente (UIB):** aun con alto uso contractual (`U1 = 94.7%`), el valor final debe revisarse porque `U3 = 16.7%` sigue bajo.

---

## 8. Ejemplo 4 — `while` con condición de negocio
En intervención terapéutica la repetición no se explica solo con números. En la semana 8 se usa este puente:

> **Mientras no mejore la lectura, continuar sesiones de apoyo.**

Eso se puede modelar así:

### PSeInt
```pseint
Proceso ApoyoLecturaDislexia
    Definir lecturaAdecuada Como Logico
    Definir sesiones Como Entero

    lecturaAdecuada <- Falso
    sesiones <- 0

    Mientras Que lecturaAdecuada = Falso Y sesiones < 20 Hacer
        Escribir "Continuar apoyo lector"
        sesiones <- sesiones + 1
        // Aquí el equipo terapéutico reevalúa si ya hubo mejora
    FinMientras
FinProceso
```

### Python
```python
lectura_adecuada = False
sesiones = 0

while lectura_adecuada == False and sesiones < 20:
    print("Continuar apoyo lector")
    sesiones = sesiones + 1
    # aquí se volvería a evaluar el progreso
```

**Conexión humana:** T03 (Luz Torres) atiende dislexia. Las **14 canceladas** muestran que un ciclo de apoyo puede interrumpirse en la realidad, aunque el objetivo terapéutico siga vigente.

---

## 9. Ciclo infinito: qué es y cómo evitarlo
Un **ciclo infinito** ocurre cuando la condición nunca llega a ser falsa. No es un error “mágico”; casi siempre aparece por uno de estos motivos:

| Causa | Ejemplo malo | Corrección |
|---|---|---|
| No actualizar variable de control | `while contador <= 5: print(contador)` | agregar `contador = contador + 1` |
| Condición imposible de romper | `while indice >= 0:` sin cambiar `indice` | definir límite real |
| Inicialización incorrecta | `contador = 10` y `while contador <= 5:` | iniciar en valor coherente |
| Actualizar variable equivocada | cambia `suma`, pero no `indice` | actualizar la variable que controla la condición |

### Regla práctica de depuración
Antes de ejecutar, el estudiante debe revisar esta lista:
- ¿Con qué valor inicia el contador o índice?
- ¿Qué línea cambia ese valor?
- ¿La condición puede volverse falsa en algún momento?
- ¿Puedo hacer un trazado de 3 iteraciones en cuaderno?

---

## 10. Trazado rápido del ejemplo de realizadas

| Iteración | indice | valor leído | total acumulado |
|---|---:|---:|---:|
| Inicio | 0 | — | 0 |
| 1 | 0 | 68 | 68 |
| 2 | 1 | 71 | 139 |
| 3 | 2 | 54 | 193 |
| 4 | 3 | 77 | 270 |
| 5 | 4 | 58 | 328 |
| 6 | 5 | 43 | 371 |
| 7 | 6 | 69 | 440 |
| 8 | 7 | 80 | 520 |

El trazado hace visible por qué el `while` funciona: el índice avanza, la condición se acerca al final y el total se acumula correctamente.

---

## 11. `while` con contador vs `while` con condición de negocio

| Tipo | Cuándo usarlo | Ejemplo |
|---|---|---|
| `while` con contador | Cuando se recorre una lista o una cantidad que controlamos con índice | recorrer T01–T08 |
| `while` con condición de negocio | Cuando repetimos hasta que se cumpla una meta o deje de existir una necesidad | continuar apoyo lector hasta mejorar |

**Puente a la Semana 9:** si ya sabemos desde el inicio cuántas veces se repetirá, normalmente conviene un **`for`**.

---

## 12. Ideas clave para recordar
- `while` evalúa la condición al inicio.
- Puede ejecutarse **cero veces**.
- Siempre debe existir una **actualización** clara.
- Sirve para acumuladores, contadores y validaciones de negocio.
- En Thonny se prueba rápido con listas y `print()`; en PSeInt se afianza la lógica.

---

## 13. Referencias de la semana
- **Xu & Frydenberg (2021).** Referencia orientadora para práctica incremental de programación en Python y control de flujo.
- **ACM/IEEE Computing Curricula 2020 (CC2020).** Marco de referencia para fundamentos de algoritmia, estructuras de control e iteración.
- **Programa del módulo TGA04 UIB.** RA2: primitivas repetitivas MQ-FMQ, HH-FHH y PARA-FPARA.
