# Evaluación Final — TGA04 — 2026

**Curso:** Fundamentos de Computación para los Negocios (TGA04)  
**Semana:** 14  
**Duración total:** 3 horas  
**Puntaje total:** 100 puntos  
**Lenguaje / entorno para la parte práctica:** Python 3.x en Thonny  
**Caso de estudio final:** **ConnectWell S.A.S.** y su cliente **TechLogic Colombia S.A.**

> **Instrucciones generales**
> - Diligencie con letra clara.
> - Puede usar calculadora básica no programable.
> - No se permite material impreso de apoyo.
> - Lea todo el caso antes de comenzar.
> - Justifique con orden cuando se le pida explicación.
> - En la parte de Python, el código debe ejecutar sin errores en Thonny.

## Encabezado del estudiante
- **Nombre completo:** __________________________________________
- **ID:** __________________________________________
- **Programa:** __________________________________________
- **Sección:** __________________________________________
- **Fecha:** __________________________________________

---

## Caso del examen

### Empresa prestadora: ConnectWell S.A.S.
*Proveedor de servicios de bienestar y salud mental laboral.*

| Terapeuta | Especialidad | Disp/mes | Realizadas | Canceladas | Costo/ses | Satisfacción |
|---|---|---:|---:|---:|---:|---:|
| Valeria Guzmán | Psicología | 70 | 65 | 4 | $92.000 | 4.8 |
| Eduardo Soto | Trabajo Social | 55 | 50 | 3 | $78.000 | 4.5 |
| Pilar Bermúdez | Fonoaudiología | 60 | 41 | 16 | $85.000 | 3.8 |
| Rafael Torres | Terapia Ocupacional | 65 | 64 | 1 | $98.000 | 4.9 |
| Nathalia Cruz | Neuropsicología | 50 | 50 | 0 | $105.000 | 5.0 |
| Sebastián Lima | Psicología | 60 | 38 | 19 | $80.000 | 3.4 |

### Cliente: TechLogic Colombia S.A.
- **Sesiones contratadas/mes:** 100
- **Empleados en plan:** 20
- **Pago mensual:** $8.800.000 COP
- **Sesiones efectivamente usadas por empleados:** 80
- **Empleados con reducción de ausentismo laboral ≥10%:** 11 de 20

### Indicadores a usar
- **N1 = realizadas / disponibles × 100**  *(umbral ≥75%)*
- **N4 = canceladas / disponibles × 100**  *(umbral ≤15%)*
- **U1 = sesiones_usadas_empleados / sesiones_contratadas × 100**  *(umbral ≥80%)*
- **U3 = empleados_mejorados / total_empleados × 100**  *(umbral ≥60%)*

---

# PARTE 1 — Fundamentos algorítmicos (20 pts)

## 1.1 Clasificación: Dato / Información / No corresponde (8 pts)
Clasifique cada enunciado del caso como **Dato**, **Información** o **No corresponde**.

| Ítem | Enunciado | Clasificación |
|---|---|---|
| a | “Valeria Guzmán tiene 70 sesiones disponibles al mes.” | |
| b | “Valeria cumple N1 porque 65/70 × 100 = 92.9%.” | |
| c | “ConnectWell es la empresa más importante del país.” | |
| d | “TechLogic tiene 20 empleados en el plan de bienestar.” | |
| e | “U3 = 55%, por tanto se requiere acción de mejora.” | |
| f | “El pago mensual del contrato es de $8.800.000.” | |
| g | “Nathalia Cruz atendió el 100% de su disponibilidad y no tuvo cancelaciones.” | |
| h | “Pilar Bermúdez presenta incumplimiento en N1 y en N4.” | |
| i | “El color favorito de Sebastián Lima es azul.” | |
| j | “Los empleados usaron 80 de 100 sesiones contratadas.” | |
| k | “Sebastián Lima canceló 19 sesiones.” | |
| l | “Como U1 quedó exactamente en 80%, el contrato supera ampliamente la meta.” | |

## 1.2 Variables y operadores (7 pts)
Indique el **tipo de variable** más adecuado y **dos operadores** que pueden aplicarse en el contexto del caso.

| Variable del caso | Tipo de variable | Dos operadores que aplican |
|---|---|---|
| `disponibles` | | |
| `satisfaccion` | | |
| `empleados_mejorados` | | |
| `nombre_terapeuta` | | |
| `u1` | | |
| `estado` | | |
| `pago_mensual` | | |

## 1.3 while vs for (5 pts)
Explique en **3 a 4 líneas** la diferencia entre `while` y `for`, usando un ejemplo del caso ConnectWell.

---

# PARTE 2 — Pseudocódigo completo (40 pts)

## 2.1 Clasificación de un terapeuta con SI-SINO-FSI (15 pts)
Redacte un pseudocódigo en **PSeInt** que clasifique el estado de **un terapeuta** según **N1** y **N4** al mismo tiempo.

### Requisitos
- Debe leer `realizadas`, `disponibles` y `canceladas`.
- Debe calcular `N1` y `N4`.
- Debe usar **operadores lógicos** (**Y**, **O**).
- Debe mostrar un estado: **Verde**, **Amarillo** o **Rojo**.
- Debe incluir un **diagrama de flujo simplificado**.

> Espacio de trabajo del estudiante:
>
> ```text
> 
> 
> 
> 
> 
> ```

## 2.2 Algoritmo completo con PARA-FPARA (25 pts)
Escriba un pseudocódigo formalmente correcto en **PSeInt** para procesar los **6 terapeutas** de ConnectWell.

### Su algoritmo debe:
- Declarar variables.
- Leer datos de cada terapeuta dentro de un ciclo **PARA-FPARA**.
- Calcular `N1` y `N4`.
- Clasificar el estado.
- Acumular sesiones realizadas.
- Calcular el promedio de satisfacción al final.
- Mostrar cuántos terapeutas quedaron en alerta.

> Espacio de trabajo del estudiante:
>
> ```text
> 
> 
> 
> 
> 
> ```

---

# PARTE 3 — Python en Thonny (40 pts)

## 3.1 Depuración de código (15 pts)
En el siguiente fragmento hay **3 errores**: **1 SyntaxError**, **1 NameError** y **1 error lógico**. Identifique la línea, el tipo de error, explique el problema y escriba la corrección.

```python
01 sesiones_contratadas = 100
02 sesiones_usadas = 80
03 empleados_mejorados = 11
04 total_empleados = 20
05 satisfacciones = [4.8, 4.5, 3.8, 4.9, 5.0, 3.4]
06 
07 u1 = sesiones_usadas / sesiones_contratadas * 100
08 u3 = empleados_mejorado / total_empleados * 100
09 
10 if u1 >= 80
11     print("U1 cumple")
12 elif u1 < 80:
13     print("U1 no cumple")
14 
15 if u3 > 60:
16     print("U3 cumple")
17 else:
18     print("U3 no cumple")
```

### Tabla de respuesta
| Línea | Tipo de error | Explicación | Corrección |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

## 3.2 Código Python completo y funcional (25 pts)
Escriba un programa en **Python 3.x** que:
1. Calcule **U1** y **U3** de TechLogic.
2. Use `if/elif/else` para mostrar el estado de cada indicador con un mensaje descriptivo.
3. Use un `for` para calcular el **promedio de satisfacción** de los 6 terapeutas.
4. Ejecute sin errores en Thonny.

### Datos obligatorios para usar en su código
- `sesiones_contratadas = 100`
- `sesiones_usadas_empleados = 80`
- `empleados_mejorados = 11`
- `total_empleados = 20`
- `satisfacciones = [4.8, 4.5, 3.8, 4.9, 5.0, 3.4]`

> Espacio para código del estudiante:
>
> ```python
> 
> 
> 
> 
> 
> ```

---

# CLAVE DOCENTE

## Valores clave del caso
- **Valeria:** N1 = 92.9% ✅ | N4 = 5.7% ✅
- **Eduardo:** N1 = 90.9% ✅ | N4 = 5.5% ✅
- **Pilar:** N1 = 68.3% 🔴 | N4 = 26.7% 🔴
- **Rafael:** N1 = 98.5% ✅ | N4 = 1.5% ✅
- **Nathalia:** N1 = 100% ✅ | N4 = 0% ✅
- **Sebastián:** N1 = 63.3% 🔴 | N4 = 31.7% 🔴
- **U1 = 80/100 × 100 = 80%** ✅
- **U3 = 11/20 × 100 = 55%** 🔴
- **Promedio de satisfacción = 26.4 / 6 = 4.4**

## Respuestas Parte 1

### 1.1 Clasificación correcta
| Ítem | Respuesta |
|---|---|
| a | Dato |
| b | Información |
| c | No corresponde |
| d | Dato |
| e | Información |
| f | Dato |
| g | Información |
| h | Información |
| i | No corresponde |
| j | Información |
| k | Dato |
| l | No corresponde |

### 1.2 Variables y operadores — posible solución
| Variable | Tipo de variable | Operadores posibles |
|---|---|---|
| `disponibles` | Entero | `/`, `>=` |
| `satisfaccion` | Real | `+`, `/` |
| `empleados_mejorados` | Entero | `+`, `/` |
| `nombre_terapeuta` | Cadena | `=`, `==` |
| `u1` | Real | `>=`, `<` |
| `estado` | Cadena | `=`, `==` |
| `pago_mensual` | Entero | `+`, `-` |

### 1.3 while vs for — respuesta esperada
`for` se usa cuando ya conocemos cuántas repeticiones habrá; por ejemplo, recorrer los 6 terapeutas de ConnectWell. `while` se usa cuando la repetición depende de una condición que puede cambiar, por ejemplo seguir pidiendo un dato mientras el usuario lo escriba mal. En este caso, `for` es más apropiado para procesar una lista fija de terapeutas.

## Respuestas Parte 2

### 2.1 Pseudocódigo correcto — un terapeuta
```text
Algoritmo ClasificarTerapeuta
    Definir realizadas, disponibles, canceladas Como Entero
    Definir n1, n4 Como Real
    Definir estado Como Cadena

    Escribir "Ingrese sesiones realizadas:"
    Leer realizadas
    Escribir "Ingrese sesiones disponibles:"
    Leer disponibles
    Escribir "Ingrese sesiones canceladas:"
    Leer canceladas

    n1 <- realizadas / disponibles * 100
    n4 <- canceladas / disponibles * 100

    Si n1 >= 75 Y n4 <= 15 Entonces
        estado <- "Verde"
    Sino
        Si (n1 < 75 Y n4 <= 15) O (n1 >= 75 Y n4 > 15) Entonces
            estado <- "Amarillo"
        Sino
            estado <- "Rojo"
        FinSi
    FinSi

    Escribir "N1: ", n1
    Escribir "N4: ", n4
    Escribir "Estado: ", estado
FinAlgoritmo
```

#### Diagrama de flujo simplificado
```text
Inicio
  ↓
Leer realizadas, disponibles, canceladas
  ↓
Calcular N1 y N4
  ↓
¿N1 >= 75 Y N4 <= 15?
  ├─ Sí → Estado = Verde
  └─ No → ¿(N1 < 75 Y N4 <= 15) O (N1 >= 75 Y N4 > 15)?
            ├─ Sí → Estado = Amarillo
            └─ No → Estado = Rojo
  ↓
Mostrar estado
  ↓
Fin
```

### 2.2 Pseudocódigo correcto — 6 terapeutas
```text
Algoritmo ProcesarConnectWell
    Definir i, disponibles, realizadas, canceladas, alertas, totalRealizadas Como Entero
    Definir satisfaccion, sumaSatisfaccion, promedioSatisfaccion, n1, n4 Como Real
    Definir nombre, estado Como Cadena

    alertas <- 0
    totalRealizadas <- 0
    sumaSatisfaccion <- 0

    Para i <- 1 Hasta 6 Con Paso 1 Hacer
        Escribir "Terapeuta ", i
        Leer nombre
        Leer disponibles
        Leer realizadas
        Leer canceladas
        Leer satisfaccion

        n1 <- realizadas / disponibles * 100
        n4 <- canceladas / disponibles * 100

        Si n1 >= 75 Y n4 <= 15 Entonces
            estado <- "Verde"
        Sino
            Si (n1 < 75 Y n4 <= 15) O (n1 >= 75 Y n4 > 15) Entonces
                estado <- "Amarillo"
            Sino
                estado <- "Rojo"
            FinSi
        FinSi

        Si estado <> "Verde" Entonces
            alertas <- alertas + 1
        FinSi

        totalRealizadas <- totalRealizadas + realizadas
        sumaSatisfaccion <- sumaSatisfaccion + satisfaccion

        Escribir nombre, " N1=", n1, " N4=", n4, " Estado=", estado
    FinPara

    promedioSatisfaccion <- sumaSatisfaccion / 6

    Escribir "Total de sesiones realizadas: ", totalRealizadas
    Escribir "Promedio de satisfacción: ", promedioSatisfaccion
    Escribir "Terapeutas en alerta: ", alertas
FinAlgoritmo
```

## Respuestas Parte 3

### 3.1 Depuración del fragmento
| Línea | Tipo de error | Explicación | Corrección |
|---|---|---|---|
| 08 | NameError | La variable `empleados_mejorado` no existe; falta la `s` final. | `u3 = empleados_mejorados / total_empleados * 100` |
| 10 | SyntaxError | Falta `:` al final del `if`. | `if u1 >= 80:` |
| 15 | Error lógico | El umbral es `>= 60`; con `>` dejaría por fuera el valor exacto de 60. | `if u3 >= 60:` |

### 3.2 Código Python correcto y comentado
```python
sesiones_contratadas = 100
sesiones_usadas_empleados = 80
empleados_mejorados = 11
total_empleados = 20
satisfacciones = [4.8, 4.5, 3.8, 4.9, 5.0, 3.4]

u1 = sesiones_usadas_empleados / sesiones_contratadas * 100
u3 = empleados_mejorados / total_empleados * 100

if u1 > 80:
    print(f"U1 = {u1:.1f}% -> Cumple y supera la meta de uso.")
elif u1 == 80:
    print(f"U1 = {u1:.1f}% -> Cumple exactamente la meta mínima.")
else:
    print(f"U1 = {u1:.1f}% -> No cumple la meta de uso.")

if u3 >= 60:
    print(f"U3 = {u3:.1f}% -> Cumple la meta de mejora.")
elif u3 >= 50:
    print(f"U3 = {u3:.1f}% -> Está cerca, pero requiere plan de mejora.")
else:
    print(f"U3 = {u3:.1f}% -> No cumple la meta y requiere acción inmediata.")

suma_satisfaccion = 0
for valor in satisfacciones:
    suma_satisfaccion += valor

promedio_satisfaccion = suma_satisfaccion / len(satisfacciones)
print(f"Promedio de satisfacción: {promedio_satisfaccion:.2f}")
```

## Rúbrica alineada a RA3
| Criterio | Peso | Evidencia en el examen |
|---|---:|---|
| **Criterio 1:** Identifica variables significativas | 25% | Parte 1 + inicio de Parte 2 |
| **Criterio 2:** Formula problemas complejos | 35% | Parte 2 completa |
| **Criterio 3:** Diseña la solución | 40% | Parte 3 |

## Nota de ajustes razonables (PIAR)
- **TDAH:** posibilidad de tiempo extra y fragmentación de instrucciones.
- **Dislexia:** lectura en voz alta de enunciados clave y tipografía/espaciado amigable.
- **TEA:** espacio tranquilo, agenda visible y anticipación de cambios.
- **ACCC:** evaluación oral alternativa o apoyo guiado en lectura de consignas cuando aplique.

**Observación docente:** este examen es autocontenido, usa un caso nuevo y todos los cálculos pueden realizarse a mano o verificarse en Thonny.
