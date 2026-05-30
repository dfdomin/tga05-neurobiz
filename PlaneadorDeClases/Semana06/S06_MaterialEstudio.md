# S06 — Material de Estudio
## Primitivas selectivas: SI-FSI en PSeInt e introducción al `if` de Python
### TGA04 Fundamentos de Computación para los Negocios · UIB · Semana 6

**Caso transversal:** NeuroBiz S.A.S. (proveedor) + UIB (cliente)  
**RA de referencia:** RA2 — Formular soluciones algorítmicas con primitivas selectivas.  
**IDE para práctica:** Thonny con Python 3.x.  
**Pseudocodificación:** PSeInt.

---

## 1. Idea central de la semana
En la Semana 6 el estudiante deja de escribir algoritmos puramente secuenciales y aprende a **tomar una decisión**. La selectiva simple sirve cuando una acción solo debe ocurrir **si** se cumple una condición. No hay rama alternativa; simplemente se ejecuta el bloque o no se ejecuta.

Este cambio es clave en contextos de negocio. NeuroBiz no revisa a todos sus terapeutas del mismo modo: **si** el ausentismo supera el umbral, entonces se genera una alerta. UIB tampoco actúa igual en todos los contratos: **si** la mejora académica está por debajo de la meta, entonces se pide revisión del servicio. La selectiva simple convierte una regla de gestión en un procedimiento claro.

---

## 2. Datos exactos del caso para trabajar en Semana 6
### 2.1 Terapeutas NeuroBiz — febrero 2026
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

### 2.2 Indicadores y umbrales obligatorios
- **N1 (ocupación)** = realizadas / disponibles × 100. Umbral esperado: **N1 ≥ 75%**.
- **N4 (ausentismo)** = canceladas / disponibles × 100. Umbral esperado: **N4 ≤ 15%**.
- Casos de alerta confirmada por N4: **T03 = 19.44%** y **T06 = 30.56%**.
- Caso crítico por N1: **T06 = 59.7%**.
- **Contrato UIB:** 150 sesiones/mes, 142 realizadas, pago de **$11.840.000 COP**.
- **U1 = 94.7%** y **U3 = 16.7%**; solo **2 de 12 estudiantes** mejoraron al menos 0.5.

### 2.3 Doble perspectiva que debe mantenerse en clase
| Perspectiva | Pregunta guía |
|---|---|
| NeuroBiz (proveedor) | ¿Qué terapeuta necesita alerta o plan de mejora? |
| UIB (cliente) | ¿La inversión se usa y produce valor suficiente? |

---

## 3. ¿Qué es una primitiva selectiva simple?
Una **primitiva selectiva simple** es una estructura algorítmica que evalúa una condición y ejecuta una acción **solo si la condición es verdadera**. Si la condición es falsa, el algoritmo continúa con la siguiente instrucción sin ejecutar ese bloque.

### 3.1 Estructura mental mínima
1. Leer o tener un dato.
2. Compararlo con una regla.
3. Ejecutar una acción si la regla se cumple.
4. Continuar el algoritmo.

### 3.2 Ejemplos verbales antes de programar
- Si `N4 > 15`, mostrar “ALERTA DE AUSENTISMO”.
- Si `N1 < 75`, mostrar “BAJA OCUPACIÓN”.
- Si `U3 < 60`, mostrar “REVISAR IMPACTO DEL CONTRATO”.

---

## 4. Condición lógica, valor verdadero y valor falso
Una condición lógica es una expresión que solo puede producir dos resultados:
- **Verdadero**
- **Falso**

### 4.1 Operadores relacionales más usados en esta semana
| Símbolo | Significado | Ejemplo con el caso | Resultado esperado |
|---|---|---|---|
| `>` | mayor que | `30.56 > 15` | Verdadero |
| `<` | menor que | `59.7 < 75` | Verdadero |
| `>=` | mayor o igual que | `75 >= 75` | Verdadero |
| `<=` | menor o igual que | `11.25 <= 15` | Verdadero |
| `=` o `==` | igual a | `100 = 100` | Verdadero |
| `<>` o `!=` | diferente de | `4.7 != 5.0` | Verdadero |

### 4.2 Tabla de verdad mínima para SI-FSI
| Condición | Valor de la condición | ¿Se ejecuta la acción del SI? |
|---|---|---|
| `N4 > 15` con T06 = 30.56 | Verdadero | Sí |
| `N4 > 15` con T08 = 0.00 | Falso | No |
| `N1 < 75` con T06 = 59.7 | Verdadero | Sí |
| `N1 < 75` con T04 = 96.3 | Falso | No |

> **Regla pedagógica:** en Semana 6 no preguntamos todavía “¿qué pasa si es falso?” como segunda rama. Solo observamos que la acción **no ocurre**.

---

## 5. Sintaxis de SI-FSI en PSeInt
### 5.1 Forma general
```pseint
Si condicion Entonces
    accion
FinSi
```

### 5.2 Ejemplo 1 con el caso NeuroBiz
```pseint
Proceso AlertaAusentismo
    Definir n4 Como Real
    Escribir "Ingrese N4 del terapeuta:"
    Leer n4

    Si n4 > 15 Entonces
        Escribir "ALERTA: requiere plan de mejora"
    FinSi
FinProceso
```

### 5.3 Lectura paso a paso del ejemplo
- Se lee el valor de `n4`.
- El algoritmo compara ese valor con el umbral `15`.
- Si la comparación es verdadera, imprime la alerta.
- Si es falsa, no imprime la alerta y termina.

### 5.4 Error frecuente en PSeInt
- Escribir la condición sin `Entonces`.
- Olvidar `FinSi`.
- Confundir `>` con `<`.
- Redactar la acción fuera del bloque.

---

## 6. Sintaxis básica del `if` en Python 3.x
### 6.1 Forma general
```python
if condicion:
    accion()
```

### 6.2 Ejemplo equivalente en Thonny
```python
n4 = float(input("Ingrese N4 del terapeuta: "))

if n4 > 15:
    print("ALERTA: requiere plan de mejora")
```

### 6.3 Ideas claves para no confundirse
| PSeInt | Python |
|---|---|
| Usa `Entonces` y `FinSi` | Usa `:` e indentación |
| `Escribir` | `print()` |
| `Leer` | `input()` |
| `Si` | `if` |

### 6.4 Error frecuente en Python
- Olvidar los dos puntos `:` después de `if`.
- No indentar la línea del `print`.
- Leer texto cuando se necesita número; por eso usamos `float(...)`.

---

## 7. Traducción rápida PSeInt ↔ Python
### 7.1 Caso `N1 < 75`
```pseint
Si n1 < 75 Entonces
    Escribir "BAJA OCUPACION"
FinSi
```

```python
if n1 < 75:
    print("BAJA OCUPACION")
```

### 7.2 Caso `U3 < 60`
```pseint
Si u3 < 60 Entonces
    Escribir "REVISAR IMPACTO DEL CONTRATO"
FinSi
```

```python
if u3 < 60:
    print("REVISAR IMPACTO DEL CONTRATO")
```

---

## 8. Ejemplos con los datos exactos de NeuroBiz
### 8.1 ¿Qué terapeutas activan una alerta por N4?
- **T03**: `19.44 > 15` → verdadera → muestra alerta.
- **T06**: `30.56 > 15` → verdadera → muestra alerta.
- **T01**: `11.25 > 15` → falsa → no muestra alerta.
- **T08**: `0.00 > 15` → falsa → no muestra alerta.

### 8.2 ¿Qué terapeutas activan una alerta por N1?
- **T06**: `59.7 < 75` → verdadera.
- **T03**: `75.0 < 75` → falsa, porque es igual al umbral, no menor.
- **T02**: `98.6 < 75` → falsa.

### 8.3 ¿Qué sucede con UIB?
- `U1 = 94.7` → si la regla fuera `U1 < 80`, la condición sería falsa.
- `U3 = 16.7` → si la regla es `U3 < 60`, la condición es verdadera y sí debe mostrarse un mensaje de revisión.

---

## 9. Tres ejercicios resueltos con clave
### Ejercicio resuelto 1. Alertar ausentismo de T06
**Problema:** Mostrar una alerta si el terapeuta supera 15% de ausentismo.

**Dato exacto:** T06 tiene `N4 = 30.56%`.

**PSeInt**
```pseint
Proceso Caso_T06
    Definir n4 Como Real
    n4 <- 30.56

    Si n4 > 15 Entonces
        Escribir "ALERTA: T06 supera el umbral de ausentismo"
    FinSi
FinProceso
```

**Python**
```python
n4 = 30.56

if n4 > 15:
    print("ALERTA: T06 supera el umbral de ausentismo")
```

**Clave:** la condición es verdadera, por tanto sí se imprime la alerta.

### Ejercicio resuelto 2. Detectar baja ocupación de T06
**Problema:** Mostrar mensaje si `N1 < 75`.

**Dato exacto:** T06 tiene `N1 = 59.7%`.

**PSeInt**
```pseint
Proceso Baja_Ocupacion
    Definir n1 Como Real
    n1 <- 59.7

    Si n1 < 75 Entonces
        Escribir "BAJA OCUPACION"
    FinSi
FinProceso
```

**Python**
```python
n1 = 59.7

if n1 < 75:
    print("BAJA OCUPACION")
```

**Clave:** la condición también es verdadera. El caso T06 activa dos alertas distintas en la misma semana.

### Ejercicio resuelto 3. Revisar impacto del contrato UIB
**Problema:** Mostrar advertencia si la tasa de mejora académica es menor a 60%.

**Dato exacto:** `U3 = 16.7%`.

**PSeInt**
```pseint
Proceso Contrato_UIB
    Definir u3 Como Real
    u3 <- 16.7

    Si u3 < 60 Entonces
        Escribir "REVISAR IMPACTO DEL CONTRATO"
    FinSi
FinProceso
```

**Python**
```python
u3 = 16.7

if u3 < 60:
    print("REVISAR IMPACTO DEL CONTRATO")
```

**Clave:** como `16.7 < 60` es verdadero, la advertencia sí aparece.

### Ejercicio resuelto 4. Reconocimiento por satisfacción alta
**Problema:** Mostrar reconocimiento si la satisfacción es al menos 4.8.

**Dato exacto:** T02 tiene satisfacción `4.9`.

**PSeInt**
```pseint
Proceso Reconocimiento_Satisfaccion
    Definir satisfaccion Como Real
    satisfaccion <- 4.9

    Si satisfaccion >= 4.8 Entonces
        Escribir "RECONOCIMIENTO POR ALTA SATISFACCION"
    FinSi
FinProceso
```

**Python**
```python
satisfaccion = 4.9

if satisfaccion >= 4.8:
    print("RECONOCIMIENTO POR ALTA SATISFACCION")
```

**Clave:** la condición es verdadera para T02, T04, T05 y T08.

---

## 10. Errores comunes de esta semana
1. Escribir una condición sin comparar nada, por ejemplo solo `n4`.
2. Creer que si la condición es falsa el algoritmo “se daña”. No se daña; simplemente no entra al bloque.
3. Usar `if` como si fuera repetición.
4. Escribir el mensaje fuera del bloque condicional.
5. Olvidar que `75.0 < 75` es **falso** porque ambos son iguales.

---

## 11. Recomendaciones de práctica en Thonny
- Probar siempre al menos un caso **verdadero** y un caso **falso**.
- Guardar el archivo con nombre corto, por ejemplo `s06_alerta_n4.py`.
- Ejecutar primero con valores exactos del caso: 30.56, 19.44, 11.25 y 0.00.
- Comparar la misma lógica en PSeInt y Python para ver qué cambia y qué se mantiene.

---

## 12. Cierre conceptual
La selectiva simple representa la primera forma de decisión algorítmica. Todavía no ofrece caminos alternativos; solo permite decir: **si esto pasa, entonces hago esto**. En gestión de negocios esa lógica es suficiente para alertas, aprobaciones simples, reconocimientos o banderas de seguimiento. La próxima semana se ampliará a dos ramas y luego a múltiples casos.

---

## 13. Referencias académicas y técnicas
| Referencia | Aporte para la semana |
|---|---|
| Xu, J., & Frydenberg, M. (2021). *Python Programming in an IS Curriculum: Perceived Relevance and Outcomes*. *Information Systems Education Journal, 19*(4), 37-54. ERIC EJ1310052. https://files.eric.ed.gov/fulltext/EJ1310052.pdf | Sustenta el uso de Python como primer lenguaje en estudiantes de negocios y sistemas de información. |
| ACM, IEEE-CS, AAAI, AIS, AITP, CSTA, IFIP, & NDMU. (2020). *Computing Curricula 2020 (CC2020)*. https://www.acm.org/binaries/content/assets/education/curricula-recommendations/cc2020.pdf | Respalda pensamiento computacional, descomposición de problemas y alfabetización computacional para no especialistas. |
| PSeInt. Documentación oficial. https://pseint.sourceforge.net/ | Referencia práctica de la sintaxis SI-FSI, entrada/salida y pruebas en pseudocódigo. |
| Python Software Foundation. *Python 3 Documentation*. https://docs.python.org/3/tutorial/controlflow.html | Sintaxis oficial de `if` e indentación en Python 3.x. |
