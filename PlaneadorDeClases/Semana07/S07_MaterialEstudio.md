# S07 — Material de Estudio
## SI-SINO-FSI, decisión múltiple y operadores lógicos en PSeInt y Python
### TGA04 Fundamentos de Computación para los Negocios · UIB · Semana 7

**Caso transversal:** NeuroBiz S.A.S. + UIB  
**RA de referencia:** RA2 — Formular soluciones algorítmicas con primitivas selectivas.  
**IDE:** Thonny con Python 3.x.  
**Pseudocodificación:** PSeInt.

---

## 1. Idea central de la semana
En Semana 6 la decisión tenía una sola rama activa. En Semana 7 el estudiante aprende a elegir entre **dos** o **más** caminos. Esto permite responder mejor a problemas reales, donde una organización no solo pregunta si existe alerta o no, sino **qué tipo de estado** tiene cada caso.

En NeuroBiz no basta con decir “hay problema” o “no hay problema”. Conviene clasificar: algunos terapeutas están en **verde**, otros en **amarillo** y otros en **rojo**. Además, cuando una variable es categórica, como la **especialidad**, se vuelve útil una decisión múltiple que seleccione entre varios casos exactos.

---

## 2. Datos exactos del caso para esta semana
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

### 2.1 Indicadores y datos de cliente
- **N1 ≥ 75%** es el umbral mínimo aceptable.
- **N4 ≤ 15%** es el umbral máximo aceptable.
- **U1 = 94.7%** indica buen uso del contrato.
- **U3 = 16.7%** indica mejora académica baja frente al umbral deseable de 60%.
- Solo **2 de 12 estudiantes** mejoraron al menos 0.5.
- En la semana se menciona a **E005** como ejemplo de posible ACCC para discutir diferenciación educativa, sin usar datos distintos a los ya declarados.

---

## 3. SI-SINO-FSI: dos ramas posibles
La estructura `SI-SINO-FSI` se usa cuando hay dos caminos excluyentes:
- uno si la condición es verdadera,
- otro si la condición es falsa.

### 3.1 Forma general en PSeInt
```pseint
Si condicion Entonces
    accion_si_verdadera
SiNo
    accion_si_falsa
FinSi
```

### 3.2 Forma general en Python
```python
if condicion:
    accion_si_verdadera()
else:
    accion_si_falsa()
```

### 3.3 Ejemplo básico con NeuroBiz
**Regla:** si `N4 > 15`, mostrar `ALERTA`; si no, mostrar `CONTROLADO`.

```pseint
Proceso Estado_Ausentismo
    Definir n4 Como Real
    Leer n4

    Si n4 > 15 Entonces
        Escribir "ALERTA"
    SiNo
        Escribir "CONTROLADO"
    FinSi
FinProceso
```

```python
n4 = float(input("Ingrese N4: "))

if n4 > 15:
    print("ALERTA")
else:
    print("CONTROLADO")
```

---

## 4. Operadores lógicos: Y, O, NO / and, or, not
Los operadores lógicos permiten construir condiciones compuestas.

### 4.1 Significado
| En español | En Python | Significado |
|---|---|---|
| `Y` | `and` | Ambas condiciones deben ser verdaderas. |
| `O` | `or` | Basta con que una condición sea verdadera. |
| `NO` | `not` | Niega el valor lógico de la condición. |

### 4.2 Tablas de verdad
#### Operador Y / and
| A | B | A Y B |
|---|---|---|
| V | V | V |
| V | F | F |
| F | V | F |
| F | F | F |

#### Operador O / or
| A | B | A O B |
|---|---|---|
| V | V | V |
| V | F | V |
| F | V | V |
| F | F | F |

#### Operador NO / not
| A | NO A |
|---|---|
| V | F |
| F | V |

### 4.3 Ejemplos con el caso
- `N1 >= 95 Y N4 <= 10` identifica desempeño muy sólido.
- `N1 < 75 O N4 > 15` identifica riesgo.
- `NO (N4 > 15)` equivale a decir que el ausentismo **no** supera el umbral.

---

## 5. Regla de clasificación de la semana
Para trabajar con una salida de tres colores, se usará la siguiente regla didáctica:
- **Verde:** `N1 >= 95` **y** `N4 <= 10`
- **Amarillo:** `N1 >= 75` **y** `N4 <= 15`
- **Rojo:** cualquier otro caso

### 5.1 ¿Por qué esta regla funciona didácticamente?
- Usa dos indicadores reales del caso.
- Obliga a combinar comparaciones y operadores lógicos.
- Produce tres resultados útiles para gestión.
- Permite ver que el mismo dato puede leerse como “cumple mínimo” o como “excelente”.

### 5.2 Resultado esperado para T01-T08
| ID | N1 | N4 | Estado esperado |
|---|---:|---:|---|
| T01 | 85.0% | 11.25% | Amarillo |
| T02 | 98.6% | 2.78% | Verde |
| T03 | 75.0% | 19.44% | Rojo |
| T04 | 96.3% | 5.00% | Verde |
| T05 | 96.7% | 1.67% | Verde |
| T06 | 59.7% | 30.56% | Rojo |
| T07 | 95.8% | 6.94% | Verde |
| T08 | 100.0% | 0.00% | Verde |

---

## 6. `if/elif/else` para más de dos resultados
Cuando la salida tiene tres o más posibilidades, la forma más práctica en Python suele ser `if/elif/else`.

```python
if n1 >= 95 and n4 <= 10:
    estado = "VERDE"
elif n1 >= 75 and n4 <= 15:
    estado = "AMARILLO"
else:
    estado = "ROJO"
```

### 6.1 Equivalente en PSeInt
```pseint
Si n1 >= 95 Y n4 <= 10 Entonces
    estado <- "VERDE"
SiNo
    Si n1 >= 75 Y n4 <= 15 Entonces
        estado <- "AMARILLO"
    SiNo
        estado <- "ROJO"
    FinSi
FinSi
```

> **Observación didáctica:** en PSeInt la forma visual suele verse como un `Si` anidado dentro del `SiNo`. En Python la cadena `if/elif/else` deja más clara la lectura secuencial de casos.

---

## 7. DD-FDD / decisión múltiple
En el microcurrículo aparece como **DD-FDD**. En la práctica, cuando hay varios casos exactos y mutuamente excluyentes, en PSeInt suele representarse con `Segun` y en Python puede modelarse con `match-case`.

### 7.1 Ejemplo por especialidad en PSeInt
```pseint
Segun especialidad Hacer
    "Psicología":
        Escribir "Ruta de seguimiento emocional"
    "Fonoaudiología":
        Escribir "Ruta de lenguaje y comunicación"
    "Terapia Ocupacional":
        Escribir "Ruta de funcionalidad y hábitos"
    "Neuropsicología":
        Escribir "Ruta de evaluación cognitiva"
    De Otro Modo:
        Escribir "Especialidad no registrada"
FinSegun
```

### 7.2 Ejemplo equivalente en Python 3.x con `match-case`
```python
match especialidad:
    case "Psicología":
        print("Ruta de seguimiento emocional")
    case "Fonoaudiología":
        print("Ruta de lenguaje y comunicación")
    case "Terapia Ocupacional":
        print("Ruta de funcionalidad y hábitos")
    case "Neuropsicología":
        print("Ruta de evaluación cognitiva")
    case _:
        print("Especialidad no registrada")
```

### 7.3 Nota práctica para Thonny
Si la versión de Python del laboratorio no soporta `match-case`, la decisión múltiple se puede resolver con `if/elif/else` sin cambiar la lógica.

---

## 8. Cuatro ejercicios resueltos con clave
### Ejercicio resuelto 1. SI-SINO-FSI con T03
**Problema:** si `N4 > 15` mostrar `ALERTA`; si no, mostrar `CONTROLADO`.

**Dato:** T03 tiene `N4 = 19.44`.

```pseint
Proceso Caso_T03
    Definir n4 Como Real
    n4 <- 19.44

    Si n4 > 15 Entonces
        Escribir "ALERTA"
    SiNo
        Escribir "CONTROLADO"
    FinSi
FinProceso
```

```python
n4 = 19.44

if n4 > 15:
    print("ALERTA")
else:
    print("CONTROLADO")
```

**Clave:** la salida correcta es `ALERTA`.

### Ejercicio resuelto 2. Clasificación verde/amarillo/rojo de T01
**Dato:** `N1 = 85.0`, `N4 = 11.25`.

```python
n1 = 85.0
n4 = 11.25

if n1 >= 95 and n4 <= 10:
    estado = "VERDE"
elif n1 >= 75 and n4 <= 15:
    estado = "AMARILLO"
else:
    estado = "ROJO"

print(estado)
```

**Clave:** T01 queda en `AMARILLO`.

### Ejercicio resuelto 3. Riesgo con operador O
**Regla:** si `N1 < 75` o `N4 > 15`, mostrar `RIESGO`.

**Dato:** T06 tiene `N1 = 59.7` y `N4 = 30.56`.

```pseint
Proceso Riesgo_T06
    Definir n1, n4 Como Real
    n1 <- 59.7
    n4 <- 30.56

    Si n1 < 75 O n4 > 15 Entonces
        Escribir "RIESGO"
    SiNo
        Escribir "ESTABLE"
    FinSi
FinProceso
```

**Clave:** T06 queda en `RIESGO`.

### Ejercicio resuelto 4. Decisión múltiple por especialidad
**Dato:** T05 tiene especialidad `Neuropsicología`.

```python
especialidad = "Neuropsicología"

match especialidad:
    case "Psicología":
        mensaje = "Ruta de seguimiento emocional"
    case "Fonoaudiología":
        mensaje = "Ruta de lenguaje y comunicación"
    case "Terapia Ocupacional":
        mensaje = "Ruta de funcionalidad y hábitos"
    case "Neuropsicología":
        mensaje = "Ruta de evaluación cognitiva"
    case _:
        mensaje = "Especialidad no registrada"

print(mensaje)
```

**Clave:** la salida correcta es `Ruta de evaluación cognitiva`.

---

## 9. Errores comunes de esta semana
1. Usar `if` simple cuando el problema realmente exige dos salidas.
2. Confundir `and` con `or`.
3. Creer que `T03` es amarillo solo porque `N1 = 75`; se olvida revisar `N4 = 19.44`.
4. Escribir una decisión múltiple para rangos numéricos exactos donde conviene más `if/elif/else`.
5. No probar el algoritmo con casos de cada color.

---

## 10. Mini guía para pruebas en Thonny
Pruebe mínimo estos cuatro casos:
- **T08** para verificar `VERDE`.
- **T01** para verificar `AMARILLO`.
- **T03** para verificar `ROJO` por ausentismo.
- **T06** para verificar `ROJO` por ocupación y ausentismo.

Si el programa no distingue correctamente esos cuatro casos, la lógica necesita revisión.

---

## 11. Cierre conceptual
`SI-SINO-FSI` permite decidir entre dos caminos; `if/elif/else` permite ampliar la clasificación; y la decisión múltiple organiza varios casos exactos. Juntas, estas estructuras convierten datos organizacionales en respuestas diferenciadas, que es justo lo que se necesita al analizar desempeño, alertas o rutas de atención en contextos de negocio.

---

## 12. Referencias académicas y técnicas
| Referencia | Aporte para la semana |
|---|---|
| Xu, J., & Frydenberg, M. (2021). *Python Programming in an IS Curriculum: Perceived Relevance and Outcomes*. *Information Systems Education Journal, 19*(4), 37-54. ERIC EJ1310052. https://files.eric.ed.gov/fulltext/EJ1310052.pdf | Justifica usar ejemplos de negocio reales y Python para desarrollar decisiones algorítmicas significativas. |
| ACM, IEEE-CS, AAAI, AIS, AITP, CSTA, IFIP, & NDMU. (2020). *Computing Curricula 2020 (CC2020)*. https://www.acm.org/binaries/content/assets/education/curricula-recommendations/cc2020.pdf | Relaciona la toma de decisiones con pensamiento computacional y resolución de problemas organizacionales. |
| PSeInt. Documentación oficial. https://pseint.sourceforge.net/ | Base para las estructuras SI-SINO-FSI y decisión múltiple tipo `Segun`. |
| Python Software Foundation. *Python 3 Documentation*. https://docs.python.org/3/tutorial/controlflow.html | Referencia de `if`, `elif`, `else`, operadores lógicos y `match` en Python 3.x. |
