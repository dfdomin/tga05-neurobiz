# S13 — Material de estudio

**TGA04 — Fundamentos de Computación para los Negocios**  
**Semana 13:** Depuración en Python + cierre integrador del módulo  
**Lenguaje:** Python 3.x en Thonny

---

## 1) Idea fuerza de la última clase
En esta última clase cerramos el recorrido completo del módulo: pasamos de entender **datos** y **algoritmos** a construir, probar, depurar y explicar un programa funcional. El caso **NeuroBiz** nos permitió conectar indicadores, decisiones y atención a personas con necesidades distintas.

### Recordatorio de fórmulas del caso
- **N1 = realizadas / disponibles × 100**  
- **N4 = canceladas / disponibles × 100**  
- **U1 = realizadas del contrato / contratadas × 100**  
- **U3 = personas con mejora / total de usuarios × 100**

### Datos NeuroBiz para practicar en materiales
| ID | Nombre | N1 | N4 | Satisfacción |
|---|---|---:|---:|---:|
| T01 | Ana Ramos | 85% | 11.25% | 4.7 |
| T02 | Carlos Mejía | 98.6% | 2.78% | 4.9 |
| T03 | Luz Torres | 75% | 19.44% | 4.2 |
| T04 | Mario Suárez | 96.3% | 5% | 4.8 |
| T05 | Paula Vega | 96.7% | 1.67% | 5.0 |
| T06 | Diego Ríos | 59.7% | 30.56% | 3.9 |
| T07 | Sandra Ospina | 95.8% | 6.94% | 4.6 |
| T08 | Héctor Niño | 100% | 0% | 4.8 |

### Indicadores institucionales UIB asociados al caso
- **150** sesiones contratadas
- **142** sesiones realizadas
- **$11.840.000** de pago
- **12** estudiantes
- **U3 = 16.7%** 🔴
- **U1 = 94.7%** ✅

---

## 2) Los 3 tipos de errores en Python

### A. SyntaxError
Ocurre cuando la **forma** del código es inválida. Python ni siquiera puede empezar a ejecutar.

#### Ejemplo 1 — falta `:`
```python
n1 = 85
n4 = 11.25
if n1 >= 75 and n4 <= 15
    print("Desempeño verde")
```
**Qué pasa:** falta `:` al final del `if`.  
**Corrección:**
```python
if n1 >= 75 and n4 <= 15:
    print("Desempeño verde")
```

#### Ejemplo 2 — falta `)`
```python
print("Promedio de satisfacción:", 4.61
```
**Qué pasa:** el paréntesis no se cerró.  
**Pista en Thonny:** normalmente subraya la línea o marca el punto donde dejó de entender el código.

---

### B. Error de ejecución (runtime)
El programa **sí arranca**, pero falla cuando intenta hacer algo imposible o incorrecto durante la ejecución.

#### Ejemplo 1 — NameError
```python
promedio = suma_satisfaccion / total_terapeutas
print(promedio_final)
```
**Qué pasa:** `promedio_final` no existe. La variable correcta era `promedio`.

#### Ejemplo 2 — ZeroDivisionError
```python
sesiones_disponibles = 0
n4 = canceladas / sesiones_disponibles * 100
```
**Qué pasa:** no se puede dividir entre cero.

#### Ejemplo 3 — TypeError
```python
satisfaccion = "4.8"
promedio = satisfaccion + 1
```
**Qué pasa:** Python no puede sumar directamente texto con número.

---

### C. Error lógico
El programa corre, pero el resultado es **incorrecto** porque la fórmula o la condición no representan bien el problema.

#### Ejemplo 1 — denominador equivocado en N1
```python
n1 = realizadas / realizadas * 100
```
**Problema:** siempre da 100% si `realizadas` no es cero.  
**Correcto:**
```python
n1 = realizadas / disponibles * 100
```

#### Ejemplo 2 — condición invertida
```python
if n1 > 75:
    alertas.append(nombre)
```
**Problema:** está marcando alerta a quien sí cumple.  
**Correcto:**
```python
if n1 < 75:
    alertas.append(nombre)
```

#### Ejemplo 3 — promedio mal dividido
```python
promedio = suma_satisfaccion / 9
```
**Problema:** en NeuroBiz hay 8 terapeutas, no 9.  
**Correcto:**
```python
promedio = suma_satisfaccion / 8
```

---

## 3) Cómo usar el debugger de Thonny paso a paso

### ¿Para qué sirve?
El debugger permite mirar el programa **por dentro**: línea por línea, variable por variable, antes de que el error se esconda.

### Paso 1 — Abrir el archivo y ubicar una hipótesis
Antes de depurar, pregúntate:
- ¿Dónde sospecho que empieza el problema?
- ¿Qué variable debería cambiar y no está cambiando?
- ¿Qué fórmula quiero verificar?

**Captura 1 descrita en texto:** en la ventana principal de Thonny, el código aparece en el editor. A la izquierda se ve el número de línea. En una línea crítica del `for` aparece un punto rojo: ese es el **breakpoint**.

### Paso 2 — Colocar breakpoints
Haz clic a la izquierda del número de línea para poner un punto rojo.

**Úsalos en:**
- el inicio del `for`
- la línea donde calculas `N1`
- la línea donde decides `verde/amarillo/rojo`

### Paso 3 — Ejecutar en modo debug
En Thonny, selecciona la opción de depuración y no la ejecución normal. El programa se detendrá en cada breakpoint.

**Captura 2 descrita en texto:** el código resalta una línea en color. Abajo aparece la consola y a un lado el panel de variables con nombres como `n1`, `n4`, `estado`, `suma_satisfaccion`.

### Paso 4 — Usar `Step over`
`Step over` ejecuta la línea actual y pasa a la siguiente sin entrar a detalles internos.

**Úsalo para:**
- ver cómo cambian `n1` y `n4`
- comprobar si `estado` toma el valor esperado
- revisar cuándo se agrega alguien a `alertas`

### Paso 5 — Usar `Run to cursor`
Coloca el cursor en una línea posterior y ejecuta hasta allí. Es útil cuando no quieres avanzar una por una durante muchas líneas repetitivas.

### Paso 6 — Leer el panel de variables
Verifica:
- si el valor de `disponibles` es correcto
- si `n1` y `n4` coinciden con el cálculo manual
- si `estado` realmente corresponde a la condición evaluada
- si la lista `alertas` crece cuando debe crecer

**Captura 3 descrita en texto:** en el panel lateral aparece una lista expandida con datos de un terapeuta y variables numéricas redondeadas. El estudiante puede comparar el valor actual con el que esperaba en papel.

### Paso 7 — Corregir y volver a probar
Depurar no termina al encontrar el error; termina cuando vuelves a ejecutar y confirmas que la corrección funcionó.

---

## 4) Buenas prácticas de código Python

### snake_case
Usa nombres como:
```python
sesiones_disponibles
promedio_satisfaccion
terapeutas_en_alerta
```
Evita mezclar mayúsculas, abreviaturas confusas o nombres como `x`, `dato1`, `var2`.

### Comentarios útiles
Comenta lo que ayude a entender el propósito, no lo obvio.
```python
# Calcula el porcentaje de sesiones realizadas sobre la disponibilidad del terapeuta
n1 = realizadas / disponibles * 100
```

### `print()` informativos
Un buen `print` le habla a una persona, no solo a la máquina.
```python
print(f"{nombre}: N1={n1:.2f}% | N4={n4:.2f}% | Estado={estado}")
```

### Constantes en mayúsculas
Si un valor no cambia, decláralo como constante.
```python
UMBRAL_N1 = 75
UMBRAL_N4 = 15
```

### Verificación simple antes de entregar
- ¿el programa corre?
- ¿los porcentajes coinciden con la calculadora?
- ¿los nombres de variables existen?
- ¿las condiciones representan lo que quiere el problema?

---

## 5) Checklist pre-entrega del programa final
Marca cada punto antes de guardar el `.py`:

- [ ] El archivo abre y ejecuta en Thonny sin errores.
- [ ] Se calculan correctamente **N1** y **N4**.
- [ ] El programa usa al menos un `for`.
- [ ] El programa usa `if/elif/else` para clasificar.
- [ ] El promedio de satisfacción está bien calculado.
- [ ] La lista de alertas muestra solo los casos necesarios.
- [ ] Los `print()` son claros y legibles.
- [ ] El archivo está guardado con nombre del grupo.
- [ ] Todos los integrantes pueden explicar una parte del código.
- [ ] Se revisó al menos un caso manualmente con calculadora.

---

## 6) Resumen completo del módulo TGA04 — RA1 a RA5

| RA | Enfoque | Pregunta guía | Producto típico | Herramienta central |
|---|---|---|---|---|
| **RA1** | Pensamiento computacional | ¿Qué datos tengo y qué problema quiero resolver? | Identificación de datos, información y necesidad | Análisis manual + tablas |
| **RA2** | Diseño de algoritmo | ¿Qué pasos debe seguir la solución? | Algoritmos secuenciales, decisiones y ciclos | PSeInt |
| **RA3** | Representación lógica | ¿Cómo comunico la solución de forma clara? | Pseudocódigo y diagrama de flujo | PSeInt + draw.io |
| **RA4** | Codificación | ¿Cómo llevo el algoritmo a Python? | Programa funcional en Python | Thonny |
| **RA5** | Depuración y mejora | ¿Cómo detecto, explico y corrijo fallas? | Programa corregido, probado y explicado | Thonny debugger |

### Conceptos clave del semestre
- dato vs. información
- variables y tipos de datos
- operadores aritméticos, relacionales y lógicos
- secuencia, decisión e iteración
- pseudocódigo y diagrama de flujo
- `if`, `elif`, `else`
- `for` y `while`
- listas y acumuladores básicos
- pruebas, depuración y mejora iterativa

### Herramientas usadas
- **PSeInt:** para pensar y expresar algoritmos antes del código.
- **draw.io:** para visualizar decisiones, entradas y salidas.
- **Thonny:** para programar en Python, ejecutar, depurar y observar variables.

---

## 7) Neurodivergencia: cierre integrador del semestre
El caso NeuroBiz nos ayuda a recordar que los sistemas de información no son neutrales: organizan recursos para personas reales.

| Tema trabajado | Qué aprendimos | Cómo lo atiende NeuroBiz |
|---|---|---|
| **TEA** | La estructura y la anticipación reducen carga e incertidumbre. | Agenda clara de sesiones, seguimiento estable y ambientes previsibles. |
| **TDAH** | El tiempo, los recordatorios y la fragmentación importan. | Recordatorios, metas cortas, seguimiento de asistencia y cancelaciones. |
| **Dislexia** | La forma de presentar información cambia la comprensión. | Reportes claros, apoyos visuales y comunicación multimodal. |
| **ACCC** | La agenda exacta y las transiciones anunciadas disminuyen fricción. | Protocolos claros, bloques visibles y contingencias previstas. |
| **Discalculia** | Los porcentajes y fórmulas necesitan apoyos visuales y paso a paso. | Indicadores simples, semáforos y validación de cálculos con ejemplos. |

### Reflexión final sugerida
**¿Qué aprendimos sobre datos, algoritmos y personas?**  
Aprendimos que un dato aislado no basta; necesita contexto. Aprendimos que un algoritmo no es solo una serie de pasos, sino una forma de tomar decisiones con lógica. Y aprendimos que programar bien también implica pensar en accesibilidad, comprensión y bienestar.

---

## 8) Mini resumen operativo para examen final y vida real
1. **Lee el problema antes de programar.**  
2. **Escribe la fórmula completa.**  
3. **Prueba un dato manualmente.**  
4. **Revisa nombres de variables.**  
5. **Usa el debugger si algo “parece raro”.**  
6. **No entregues hasta ejecutar una vez más.**

---

## 9) Referencias finales
- Xu, D., & Frydenberg, M. (2021). *An introductory computational thinking curriculum for business students*. ISEDJ, EJ1310052.
- De Santo, M., et al. (2022). *Teaching and learning programming with visual and adaptive supports*. IEEE Transactions on Learning Technologies.
- ACM/IEEE-CS/AAAI. (2020). *Computing Curricula 2020 (CC2020).* Association for Computing Machinery.
- World Health Organization. (2024). *Autism: key facts / factsheet*.
- Centers for Disease Control and Prevention. (2024). *ADHD: data and statistics / overview*.
- Colombia. Decreto 1421 de 2017. *Atención educativa a población con discapacidad en el marco de la educación inclusiva*.

**Cierre del módulo:** depurar no es “arreglar por intuición”; es pensar con método.
