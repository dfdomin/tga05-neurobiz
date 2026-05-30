# S11 — Material de Estudio
## TGA04 · UIB

**Semana 11:** RA3 (prueba de escritorio) + introducción a RA4 (Python en Thonny)  
**Lenguaje:** Python 3.x en Thonny IDE  
**Pseudocódigo:** PSeInt

## 1. Panorama de la semana
Esta semana une dos ideas clave:
1. **Verificar un algoritmo antes de programarlo** con una prueba de escritorio.
2. **Traducir esa lógica a Python** en un IDE real: Thonny.

La idea central es simple: **si puedes seguir el estado de las variables en papel, podrás escribir mejor el programa en pantalla.**

## 2. Datos base del caso NeuroBiz
### 2.1 Terapeutas
| ID | Nombre | N1 | N4 | Satisfacción |
|---|---|---:|---:|---:|
| T01 | Ana Ramos | 85%✅ | 11.25%✅ | 4.7 |
| T02 | Carlos Mejía | 98.6%✅ | 2.78%✅ | 4.9 |
| T03 | Luz Torres | 75%✅ | 19.44%🔴 | 4.2 |
| T04 | Mario Suárez | 96.3%✅ | 5%✅ | 4.8 |
| T05 | Paula Vega | 96.7%✅ | 1.67%✅ | 5.0 |
| T06 | Diego Ríos | 59.7%🔴 | 30.56%🔴🔴 | 3.9 |
| T07 | Sandra Ospina | 95.8%✅ | 6.94%✅ | 4.6 |
| T08 | Héctor Niño | 100%✅ | 0%✅ | 4.8 |

### 2.2 UIB (cliente)
- 150 sesiones contratadas
- 142 sesiones realizadas
- $11.840.000 pagados
- 12 estudiantes cubiertos
- U3 = 16.7% 🔴
- U1 = 94.7% ✅

### 2.3 Doble perspectiva
- **NeuroBiz (proveedor):** mira desempeño por terapeuta.
- **UIB (cliente):** mira uso del contrato y efecto del servicio.

## 3. ¿Qué es una prueba de escritorio?
Una **prueba de escritorio** es una revisión manual, paso a paso, de un algoritmo. En cada instrucción se registra:
- qué variable cambia,
- cuál es su nuevo valor,
- qué condición fue verdadera o falsa,
- qué salida debería aparecer.

No se “adivina” el resultado final. Se sigue el algoritmo **instrucción por instrucción**.

## 4. ¿Qué es un trace table?
El **trace table** es la tabla donde se registran los cambios del algoritmo.

Formato recomendado en este curso:

| Variable / salida | Paso 0 | Paso 1 | Paso 2 | Paso 3 | Paso 4 |
|---|---|---|---|---|---|
| variable_1 | | | | | |
| variable_2 | | | | | |
| salida | | | | | |

**Regla de oro:** cada columna representa un momento claro del algoritmo. Puede ser:
- una instrucción,
- una decisión,
- o una vuelta completa del ciclo,

pero el criterio debe mantenerse constante dentro de la misma tabla.

## 5. ¿Cómo hacer una prueba de escritorio?
1. Leer el algoritmo completo una vez.
2. Identificar entradas, variables de proceso y salidas.
3. Escribir los valores iniciales.
4. Ejecutar mentalmente **solo la primera instrucción** y registrar cambios.
5. Evaluar la condición del `Si` o del `Mientras`.
6. Continuar paso a paso hasta el final.
7. Verificar si la salida coincide con el objetivo del algoritmo.

## 6. Inclusión y neurodivergencia: discalculia
Esta semana se aborda la **discalculia**, una dificultad que puede afectar cálculos secuenciales, seguimiento numérico y memoria de trabajo matemática.

En el caso NeuroBiz, se menciona que **T03 atiende pacientes con discalculia**. Por eso el trace table se presenta también como una **herramienta inclusiva**:
- hace visible el estado de cada variable,
- reduce la carga de cálculo mental,
- permite detectar errores antes de programar,
- baja la ansiedad de “perderse” dentro del algoritmo.

**Idea clave para recordar:** el trace table no es solo control de calidad; también es una ayuda cognitiva.

## 7. Ejemplo resuelto 1 — algoritmo selectivo en PSeInt
### 7.1 Pseudocódigo
```
Algoritmo AlertaAusentismoT03
    Definir n4 Como Real
    Definir mensaje Como Cadena
    n4 <- 19.44

    Si n4 > 15 Entonces
        mensaje <- "Alerta roja"
    SiNo
        mensaje <- "En rango"
    FinSi

    Escribir mensaje
FinAlgoritmo
```

### 7.2 Trace table resuelto
| Variable / salida | Paso 0 | Paso 1 `n4 <- 19.44` | Paso 2 `n4 > 15` | Paso 3 `mensaje <- "Alerta roja"` | Paso 4 `Escribir mensaje` |
|---|---|---|---|---|---|
| n4 | — | 19.44 | 19.44 | 19.44 | 19.44 |
| mensaje | — | — | — | Alerta roja | Alerta roja |
| salida | — | — | Verdadero | — | Alerta roja |

**Lectura:** como `19.44 > 15` es verdadero, el mensaje final es **Alerta roja**.

## 8. Ejemplo resuelto 2 — algoritmo con while + condicional
### 8.1 Pseudocódigo
```
Algoritmo CierreContratoUIB
    Definir realizadas, meta, iteracion Como Entero
    Definir estado Como Cadena

    realizadas <- 142
    meta <- 150
    iteracion <- 0
    estado <- "Seguimiento"

    Mientras realizadas < meta Hacer
        realizadas <- realizadas + 2
        iteracion <- iteracion + 1

        Si realizadas >= 148 Entonces
            estado <- "Cierre cercano"
        FinSi
    FinMientras

    Escribir realizadas, iteracion, estado
FinAlgoritmo
```

### 8.2 Trace table por vueltas del ciclo
| Variable / salida | Inicio | Vuelta 1 | Vuelta 2 | Vuelta 3 | Vuelta 4 | Salida |
|---|---|---|---|---|---|---|
| realizadas | 142 | 144 | 146 | 148 | 150 | 150 |
| meta | 150 | 150 | 150 | 150 | 150 | 150 |
| iteracion | 0 | 1 | 2 | 3 | 4 | 4 |
| estado | Seguimiento | Seguimiento | Seguimiento | Cierre cercano | Cierre cercano | Cierre cercano |
| condición `realizadas < meta` | Verdadero | Verdadero | Verdadero | Verdadero | Falso | — |

**Lectura:** el ciclo termina cuando `realizadas` llega a 150. Se necesitaron 4 vueltas si cada vuelta suma 2 sesiones.

## 9. Señales de error comunes en prueba de escritorio
- Saltarse una asignación.
- Actualizar una variable dos veces en la misma columna sin registrarlo.
- Escribir el resultado “esperado” en vez del resultado real del algoritmo.
- No registrar si una condición fue verdadera o falsa.
- Olvidar que un `while` vuelve a evaluar la condición en cada vuelta.

## 10. Puente entre PSeInt y Python
### 10.1 Mismo problema, distinta sintaxis
| Idea | PSeInt | Python |
|---|---|---|
| Asignar valor | `n4 <- 19.44` | `n4 = 19.44` |
| Imprimir | `Escribir mensaje` | `print(mensaje)` |
| Condición | `Si n4 > 15 Entonces` | `if n4 > 15:` |
| Si no | `SiNo` | `else:` |
| Ciclo mientras | `Mientras x < y Hacer` | `while x < y:` |
| Fin de bloque | `FinSi`, `FinMientras` | sangría (indentación) |
| Comentario | `// comentario` | `# comentario` |

### 10.2 Diferencias visibles que debes mencionar
1. Python usa `:` al iniciar bloques.
2. Python no usa `FinSi`; usa sangría.
3. `print()` reemplaza a `Escribir`.
4. La asignación en Python es con `=`.

## 11. Thonny IDE: ¿qué es y para qué sirve?
**Thonny** es un entorno de desarrollo pensado para principiantes. Permite:
- escribir código,
- guardarlo como archivo `.py`,
- ejecutarlo,
- ver errores de forma clara,
- y explorar variables de manera amigable.

### 11.1 Instalación / apertura básica
1. Abrir el navegador.
2. Ir a `https://thonny.org` si se necesita instalar.
3. Descargar la versión para el sistema operativo.
4. Instalar con opciones por defecto.
5. Abrir Thonny desde el acceso directo.

> En sala de cómputo, lo usual es que Thonny ya esté instalado. Si ya está listo, se omiten los pasos 2–4.

### 11.2 Ventanas principales de Thonny
- **Editor:** donde se escribe el programa.
- **Shell:** donde aparece la salida o se prueban instrucciones.
- **Barra Run/Stop:** ejecutar o detener.
- **Archivo / Save:** guardar el `.py`.

## 12. Primer archivo Python
### 12.1 Programa mínimo
```python
print("Hola NeuroBiz")
```

### 12.2 Guardado sugerido
- Nombre del archivo: `hola_neurobiz.py`
- Ubicación: carpeta del curso o carpeta personal del estudiante.

## 13. Variables en Python
```python
empresa = "NeuroBiz S.A.S."
sesiones_realizadas = 142
valor_pagado = 11840000
uso_uib = 94.7
alerta = True
```

### 13.1 Tipos básicos
| Tipo | Ejemplo | Significado |
|---|---|---|
| `int` | `142` | número entero |
| `float` | `94.7` | número decimal |
| `str` | `"Ana Ramos"` | texto |
| `bool` | `True` | verdadero/falso |

## 14. `print()` y `f-string`
```python
empresa = "NeuroBiz S.A.S."
sesiones_realizadas = 142
valor_pagado = 11840000

print(f"{empresa} registró {sesiones_realizadas} sesiones y recibió ${valor_pagado}.")
```

**Ventaja de la `f-string`:** permite mezclar texto y variables de forma legible.

## 15. `input()` básico
```python
nombre_estudiante = input("Escribe tu nombre: ")
print(f"Hola, {nombre_estudiante}. Bienvenido a NeuroBiz en Python.")
```

Si se necesita leer un número:
```python
n1 = float(input("Escribe el N1 del terapeuta: "))
print(f"El N1 digitado fue {n1}%")
```

## 16. Ejemplos NeuroBiz en Python
### 16.1 Cálculo simple
```python
sesiones_contratadas = 150
sesiones_realizadas = 142
faltantes = sesiones_contratadas - sesiones_realizadas
print(f"Faltan {faltantes} sesiones para completar la meta mensual.")
```

### 16.2 Variables de un terapeuta
```python
terapeuta = "Diego Ríos"
n1 = 59.7
n4 = 30.56
satisfaccion = 3.9

print(f"{terapeuta}: N1={n1}%, N4={n4}%, satisfacción={satisfaccion}")
```

## 17. Buenas prácticas mínimas desde el inicio
- Guardar el archivo antes de ejecutar.
- Usar nombres claros: `sesiones_realizadas`, no `sr`.
- Probar una idea a la vez.
- Leer el mensaje de error completo antes de pedir ayuda.
- Comparar la lógica con el pseudocódigo si algo falla.

## 18. Referencias sugeridas
- Xu, D. & Frydenberg, M. (2021). Material sobre aprendizaje inicial de programación y uso de estrategias paso a paso para seguir la ejecución.
- De Santo et al. (2022). IEEE Transactions on Learning Technologies. Referencia sobre apoyo tecnológico para la enseñanza/aprendizaje de programación.
- Material base del módulo TGA04 y prácticas en PSeInt/Thonny.
