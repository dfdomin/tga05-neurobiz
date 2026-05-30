# S04 — Material de Estudio
## Operadores estadísticos y consolidación RA1
### TGA04 Fundamentos de Computación para los Negocios · UIB · Semana 4

**Caso transversal:** NeuroBiz S.A.S. (proveedor) + UIB (cliente)  
**Foco de aprendizaje:** suma acumulada, promedio, máximo, mínimo, conteo, pseudocódigo secuencial e introducción breve a Python.

---

## 1. Idea central de la semana
En la Semana 4 el estudiante ya no se queda en un solo indicador aislado. Ahora debe ser capaz de **leer varios valores, acumularlos, resumirlos y sacar conclusiones**. Eso es exactamente lo que hacen los reportes de gestión de una empresa.

En este curso usaremos los datos de **NeuroBiz** para leer el servicio desde dos puntos de vista:
- **Proveedor:** ¿cómo les fue a los terapeutas?
- **Cliente (UIB):** ¿el contrato está siendo usado y está generando mejora académica?

---

## 2. Definiciones formales de operadores estadísticos

Según Joyanes Aguilar (2008), en programación básica es frecuente trabajar con **acumuladores, contadores y comparaciones** para resumir conjuntos de datos. Cairó y Guardati (2006) subrayan que en pseudocódigo estas operaciones deben expresarse con secuencia clara: entrada, proceso y salida.

| Operador estadístico | Definición formal | Fórmula / regla | Notación típica en pseudocódigo | Ejemplo breve |
|---|---|---|---|---|
| **Suma acumulada** | Variable que guarda la suma progresiva de varios datos. | `Σ valores` | `suma <- suma + valor` | `sumaN1 <- sumaN1 + n1_3` |
| **Promedio** | Cociente entre la suma total y el número de datos. | `promedio = Σ valores / n` | `promedio <- suma / cantidad` | `promedioN1 <- sumaN1 / 8` |
| **Máximo** | Mayor valor de un conjunto. | `max(x1, x2, ..., xn)` | `Si valor > maximo Entonces maximo <- valor` | `Si n1_5 > maxN1 Entonces maxN1 <- n1_5` |
| **Mínimo** | Menor valor de un conjunto. | `min(x1, x2, ..., xn)` | `Si valor < minimo Entonces minimo <- valor` | `Si n1_6 < minN1 Entonces minN1 <- n1_6` |
| **Conteo** | Número de elementos o de casos que cumplen una condición. | `n` o `cantidad de casos` | `contador <- contador + 1` | `contadorCumplen <- contadorCumplen + 1` |

### 2.1 Notación matemática y notación de pseudocódigo

| Idea | Matemática | Pseudocódigo |
|---|---|---|
| Acumular | `Σ x` | `suma <- suma + x` |
| Promediar | `Σ x / n` | `promedio <- suma / cantidad` |
| Buscar máximo | `max(x)` | `Si x > maximo Entonces` |
| Buscar mínimo | `min(x)` | `Si x < minimo Entonces` |
| Contar | `n` | `contador <- contador + 1` |

> **Nota didáctica:** en esta semana no trabajamos ciclos formales; la lectura de varios datos se hace de forma **secuencial y manual**. Eso significa repetir los `Leer` uno a uno.

---

## 3. Datos del caso para Semana 4

### 3.1 Tabla completa de terapeutas
| ID  | Nombre         | Especialidad      | Disp | Real | Cancel | Costo/ses | Satisf |
|-----|----------------|-------------------|------|------|--------|-----------|--------|
| T01 | Ana Ramos      | Psicología        | 80   | 68   | 9      | $87.000   | 4.7    |
| T02 | Carlos Mejía   | Fonoaudiología    | 72   | 71   | 2      | $91.000   | 4.9    |
| T03 | Luz Torres     | T. Ocupacional    | 72   | 54   | 14     | $78.000   | 4.2    |
| T04 | Mario Suárez   | Psicología        | 80   | 77   | 4      | $89.000   | 4.8    |
| T05 | Paula Vega     | Neuropsicología   | 60   | 58   | 1      | $105.000  | 5.0    |
| T06 | Diego Ríos     | Fonoaudiología    | 72   | 43   | 22     | $72.000   | 3.9    |
| T07 | Sandra Ospina  | T. Ocupacional    | 72   | 69   | 5      | $85.000   | 4.6    |
| T08 | Héctor Niño    | Psicología        | 80   | 80   | 0      | $93.000   | 4.8    |

### 3.2 Valores estadísticos ya calculados para trabajar en Semana 4
> Para concentrarnos en los **operadores estadísticos**, en esta guía tomamos los valores N1 y N4 ya calculados en la ficha del caso.

| ID | N1 | N4 |
|---|---:|---:|
| T01 | 85.0% | 11.25% |
| T02 | 98.6% | 2.78% |
| T03 | 75.0% | 19.44% |
| T04 | 96.3% | 5.00% |
| T05 | 96.7% | 1.67% |
| T06 | 59.7% | 30.56% |
| T07 | 95.8% | 6.94% |
| T08 | 100.0% | 0.00% |

### 3.3 Resumen UIB febrero 2026
- **Sesiones usadas:** 142 de 150 contratadas  
- **Total pagado:** $11.840.000 COP  
- **Estudiantes atendidos:** 12  
- **Estudiantes con mejora ≥ 0.5:** E001 y E006  
- **E005 (ACCC):** pasó de 4.2 a 4.5 con coaching  

### 3.4 Fórmulas clave del caso
- `N1 = (Sesiones realizadas / Sesiones disponibles) * 100`
- `N4 = (Sesiones canceladas / Sesiones programadas) * 100`
- `N6 = Costos operativos / Número de sesiones realizadas`
- `U1 = (Sesiones usadas / Sesiones contratadas) * 100`
- `U2 = Total pagado / Número de estudiantes únicos`
- `U3 = (Estudiantes con mejora >= 0.5 / Total estudiantes) * 100`

---

## 4. Ejemplos resueltos paso a paso

### Ejemplo 1. Promedio de N1 de todos los terapeutas

**Paso 1.** Escribir todos los N1.
```text
85.0, 98.6, 75.0, 96.3, 96.7, 59.7, 95.8, 100.0
```

**Paso 2.** Hacer la suma acumulada.
```text
sumaN1 = 85.0 + 98.6 + 75.0 + 96.3 + 96.7 + 59.7 + 95.8 + 100.0
       = 707.1
```

**Paso 3.** Dividir entre la cantidad de terapeutas.
```text
promedioN1 = 707.1 / 8
           = 88.3875 ≈ 88.4%
```

**Resultado:** el **promedio N1 = 88.4%**.

---

### Ejemplo 2. Máximo N1
Comparación rápida:
```text
85.0, 98.6, 75.0, 96.3, 96.7, 59.7, 95.8, 100.0
```
El valor más alto es **100.0%**, correspondiente a **T08 Héctor Niño**.

**Resultado:** **Max N1 = T08 (100%)**.

---

### Ejemplo 3. Mínimo N1
El valor más bajo de la lista es **59.7%**, correspondiente a **T06 Diego Ríos**.

**Resultado:** **Min N1 = T06 (59.7%)**.

---

### Ejemplo 4. Conteo de terapeutas con N1 ≥ 75%
Revisamos cada caso:
- T01 = 85.0 ✅
- T02 = 98.6 ✅
- T03 = 75.0 ✅
- T04 = 96.3 ✅
- T05 = 96.7 ✅
- T06 = 59.7 ❌
- T07 = 95.8 ✅
- T08 = 100.0 ✅

**Conteo final:** **7 de 8 terapeutas** cumplen `N1 >= 75%`.  
El único que no cumple es **T06**.

---

### Ejemplo 5. Promedio de N4

**Paso 1.** Sumar los N4 ya calculados.
```text
sumaN4 = 11.25 + 2.78 + 19.44 + 5.00 + 1.67 + 30.56 + 6.94 + 0.00
       = 77.64
```

**Paso 2.** Dividir entre 8.
```text
promedioN4 = 77.64 / 8
           = 9.705 ≈ 9.7%
```

**Resultado:** el **promedio N4 = 9.7%**.

**Lectura adicional:** aunque el promedio general es aceptable, **T03** y **T06** superan el umbral de 15%.

---

### Ejemplo 6. Cálculo de U3

**Datos:**
- Total de estudiantes atendidos = 12
- Estudiantes con mejora ≥ 0.5 = 2

**Cálculo:**
```text
U3 = (2 / 12) * 100
   = 16.666... ≈ 16.7%
```

**Resultado:** **U3 = 16.7%**, por debajo del umbral deseable de **60%**.

**Implicación para UIB:** el contrato se está usando bastante (`U1 = 94.7%`), pero la mejora académica fuerte todavía es baja. Eso obliga a preguntar por calidad, focalización y seguimiento.

---

## 5. Pseudocódigo completo de integración RA1

> **Nota:** este ejemplo integra lectura secuencial, acumulación, promedio, máximo, mínimo, conteo y evaluación dual NeuroBiz–UIB. No usa ciclos; por eso las lecturas aparecen una por una.

```pseint
Proceso Integracion_RA1_Semana4
    Definir n1_1, n1_2, n1_3, n1_4, n1_5, n1_6, n1_7, n1_8 Como Real
    Definir n4_1, n4_2, n4_3, n4_4, n4_5, n4_6, n4_7, n4_8 Como Real
    Definir sumaN1, sumaN4, promedioN1, promedioN4 Como Real
    Definir maxN1, minN1 Como Real
    Definir contadorCumplenN1, contadorRiesgo Como Entero
    Definir sesionesUsadas, sesionesContratadas, totalPagado, estudiantes, mejoran Como Real
    Definir u1, u2, u3 Como Real

    sumaN1 <- 0
    sumaN4 <- 0
    contadorCumplenN1 <- 0
    contadorRiesgo <- 0

    Escribir "Ingrese N1 de T01:"; Leer n1_1
    Escribir "Ingrese N4 de T01:"; Leer n4_1
    Escribir "Ingrese N1 de T02:"; Leer n1_2
    Escribir "Ingrese N4 de T02:"; Leer n4_2
    Escribir "Ingrese N1 de T03:"; Leer n1_3
    Escribir "Ingrese N4 de T03:"; Leer n4_3
    Escribir "Ingrese N1 de T04:"; Leer n1_4
    Escribir "Ingrese N4 de T04:"; Leer n4_4
    Escribir "Ingrese N1 de T05:"; Leer n1_5
    Escribir "Ingrese N4 de T05:"; Leer n4_5
    Escribir "Ingrese N1 de T06:"; Leer n1_6
    Escribir "Ingrese N4 de T06:"; Leer n4_6
    Escribir "Ingrese N1 de T07:"; Leer n1_7
    Escribir "Ingrese N4 de T07:"; Leer n4_7
    Escribir "Ingrese N1 de T08:"; Leer n1_8
    Escribir "Ingrese N4 de T08:"; Leer n4_8

    sumaN1 <- sumaN1 + n1_1 + n1_2 + n1_3 + n1_4 + n1_5 + n1_6 + n1_7 + n1_8
    sumaN4 <- sumaN4 + n4_1 + n4_2 + n4_3 + n4_4 + n4_5 + n4_6 + n4_7 + n4_8
    promedioN1 <- sumaN1 / 8
    promedioN4 <- sumaN4 / 8

    maxN1 <- n1_1
    minN1 <- n1_1

    Si n1_2 > maxN1 Entonces maxN1 <- n1_2 FinSi
    Si n1_3 > maxN1 Entonces maxN1 <- n1_3 FinSi
    Si n1_4 > maxN1 Entonces maxN1 <- n1_4 FinSi
    Si n1_5 > maxN1 Entonces maxN1 <- n1_5 FinSi
    Si n1_6 > maxN1 Entonces maxN1 <- n1_6 FinSi
    Si n1_7 > maxN1 Entonces maxN1 <- n1_7 FinSi
    Si n1_8 > maxN1 Entonces maxN1 <- n1_8 FinSi

    Si n1_2 < minN1 Entonces minN1 <- n1_2 FinSi
    Si n1_3 < minN1 Entonces minN1 <- n1_3 FinSi
    Si n1_4 < minN1 Entonces minN1 <- n1_4 FinSi
    Si n1_5 < minN1 Entonces minN1 <- n1_5 FinSi
    Si n1_6 < minN1 Entonces minN1 <- n1_6 FinSi
    Si n1_7 < minN1 Entonces minN1 <- n1_7 FinSi
    Si n1_8 < minN1 Entonces minN1 <- n1_8 FinSi

    Si n1_1 >= 75 Entonces contadorCumplenN1 <- contadorCumplenN1 + 1 FinSi
    Si n1_2 >= 75 Entonces contadorCumplenN1 <- contadorCumplenN1 + 1 FinSi
    Si n1_3 >= 75 Entonces contadorCumplenN1 <- contadorCumplenN1 + 1 FinSi
    Si n1_4 >= 75 Entonces contadorCumplenN1 <- contadorCumplenN1 + 1 FinSi
    Si n1_5 >= 75 Entonces contadorCumplenN1 <- contadorCumplenN1 + 1 FinSi
    Si n1_6 >= 75 Entonces contadorCumplenN1 <- contadorCumplenN1 + 1 FinSi
    Si n1_7 >= 75 Entonces contadorCumplenN1 <- contadorCumplenN1 + 1 FinSi
    Si n1_8 >= 75 Entonces contadorCumplenN1 <- contadorCumplenN1 + 1 FinSi

    Si n1_1 < 75 O n4_1 > 15 Entonces contadorRiesgo <- contadorRiesgo + 1 FinSi
    Si n1_2 < 75 O n4_2 > 15 Entonces contadorRiesgo <- contadorRiesgo + 1 FinSi
    Si n1_3 < 75 O n4_3 > 15 Entonces contadorRiesgo <- contadorRiesgo + 1 FinSi
    Si n1_4 < 75 O n4_4 > 15 Entonces contadorRiesgo <- contadorRiesgo + 1 FinSi
    Si n1_5 < 75 O n4_5 > 15 Entonces contadorRiesgo <- contadorRiesgo + 1 FinSi
    Si n1_6 < 75 O n4_6 > 15 Entonces contadorRiesgo <- contadorRiesgo + 1 FinSi
    Si n1_7 < 75 O n4_7 > 15 Entonces contadorRiesgo <- contadorRiesgo + 1 FinSi
    Si n1_8 < 75 O n4_8 > 15 Entonces contadorRiesgo <- contadorRiesgo + 1 FinSi

    Escribir "Sesiones usadas UIB:"; Leer sesionesUsadas
    Escribir "Sesiones contratadas UIB:"; Leer sesionesContratadas
    Escribir "Total pagado UIB:"; Leer totalPagado
    Escribir "Estudiantes atendidos:"; Leer estudiantes
    Escribir "Estudiantes con mejora >= 0.5:"; Leer mejoran

    u1 <- (sesionesUsadas / sesionesContratadas) * 100
    u2 <- totalPagado / estudiantes
    u3 <- (mejoran / estudiantes) * 100

    Escribir "--- REPORTE RA1 ---"
    Escribir "Promedio N1: ", promedioN1, "%"
    Escribir "Promedio N4: ", promedioN4, "%"
    Escribir "Maximo N1: ", maxN1, "%"
    Escribir "Minimo N1: ", minN1, "%"
    Escribir "Cumplen N1>=75: ", contadorCumplenN1
    Escribir "Terapeutas en riesgo: ", contadorRiesgo
    Escribir "U1: ", u1, "%"
    Escribir "U2: $", u2
    Escribir "U3: ", u3, "%"
FinProceso
```

---

## 6. Así se escribe esto en Python

```python
terapeutas = ["T01", "T02", "T03", "T04", "T05", "T06", "T07", "T08"]
n1 = [85.0, 98.6, 75.0, 96.3, 96.7, 59.7, 95.8, 100.0]
n4 = [11.25, 2.78, 19.44, 5.00, 1.67, 30.56, 6.94, 0.00]

promedio_n1 = sum(n1) / len(n1)      # suma y promedio
promedio_n4 = sum(n4) / len(n4)
max_n1 = max(n1)                     # valor máximo
min_n1 = min(n1)                     # valor mínimo
conteo_cumplen = sum(1 for valor in n1 if valor >= 75)

indice_max = n1.index(max_n1)
terapeuta_max = terapeutas[indice_max]

print(f"Promedio N1: {promedio_n1:.1f}%")
print(f"Promedio N4: {promedio_n4:.1f}%")
print(f"Máximo N1: {terapeuta_max} con {max_n1:.1f}%")
print(f"Mínimo N1: {min_n1:.1f}%")
print(f"Cumplen N1 >= 75: {conteo_cumplen}")
```

### Lo importante del paralelo PSeInt–Python
- En PSeInt declaramos y leemos paso a paso.
- En Python podemos usar **listas** para agrupar muchos valores del mismo tipo.
- `sum()`, `max()`, `min()` y `len()` son atajos muy útiles, pero la lógica matemática es la misma.

---

## 7. ACCC — Altas Capacidades Cognitivas y Creativas

### 7.1 Definición
Las **ACCC** son un perfil de funcionamiento cognitivo en el que una persona presenta desempeño significativamente superior al promedio en una o varias áreas: razonamiento, creatividad, lenguaje, matemática, pensamiento abstracto o solución de problemas. No es un trastorno; es una **condición diferencial** que exige apoyos educativos adecuados.

### 7.2 Marco colombiano
En Colombia, el **Decreto 1421 de 2017** reconoce la necesidad de ajustes razonables e inclusión educativa. Aunque suele citarse más en discapacidad, también se conecta con el deber institucional de atender perfiles diferenciales. El **Decreto 366 de 2009** y la normativa asociada a capacidades o talentos excepcionales respaldan la atención a estudiantes con altas capacidades.

### 7.3 Rasgos frecuentes en estudiantes universitarios con ACCC
- Aprenden muy rápido y pueden frustrarse con explicaciones imprecisas.
- Necesitan comprender el **por qué** de la actividad, no solo el paso mecánico.
- Detectan inconsistencias en los datos o en el método con rapidez.
- Pueden aburrirse si todo el reto es repetitivo.
- En algunos casos presentan perfeccionismo, hipersensibilidad o desregulación ante cambios inesperados.

### 7.4 Relación con NeuroBiz y con el aula
NeuroBiz también acompaña a estudiantes con ACCC. El caso visible de esta guía es **E005**, estudiante con ACCC en UIB que pasó de **4.2** a **4.5** después de coaching. Esa mejora no significa que “antes estaba mal”; significa que el acompañamiento pudo ayudarle a organizar mejor su potencial.

### 7.5 Qué datos extra debería pedir NeuroBiz para evaluar impacto real en ACCC
- nivel de reto percibido en las clases,
- grado de aburrimiento o desenganche,
- avance en autorregulación y planificación,
- satisfacción con coaching,
- permanencia y bienestar, no solo promedio académico.

### 7.6 Pregunta de reflexión sugerida
> “NeuroBiz también atiende a estudiantes como E005 que tienen altas capacidades — su promedio ya era 4.2 y subió a 4.5. ¿Qué datos extra necesitaría NeuroBiz para evaluar el impacto del coaching para este perfil?”

---

## 8. Guía de preparación para el primer parcial

### 8.1 Temas que debe dominar
- Diferencia entre **dato** e **información**.
- Tipos de variables: numérica entera, numérica real, alfanumérica, lógica.
- Operadores: matemáticos, relacionales, lógicos y estadísticos.
- Fórmulas N1, N4, U1, U2, U3.
- Pseudocódigo secuencial en sintaxis básica de PSeInt.
- Lectura de varios datos **sin ciclos**, usando secuencia manual.
- Interpretación desde proveedor y cliente.

### 8.2 Tipos de preguntas probables
1. Clasificar variables de un caso empresarial.
2. Identificar qué operador se necesita para resolver un problema.
3. Calcular manualmente un indicador o un promedio.
4. Diseñar pseudocódigo secuencial para uno o varios indicadores.
5. Interpretar un resultado y decir si está sobre o bajo un umbral.

### 8.3 Consejos de manejo del tiempo
- **Min 0–15:** lea todo el examen y marque lo que ya sabe hacer.
- **Min 15–45:** resuelva teoría y cálculos cortos.
- **Min 45–80:** haga el pseudocódigo con títulos claros y procedimientos visibles.
- **Últimos 10 min:** revise etiquetas, signos `%`, nombres de variables y división entre la cantidad correcta.

### 8.4 Errores frecuentes que bajan nota
- Promediar sin dividir por la cantidad de datos.
- Confundir máximo con mínimo.
- No declarar variables antes de usarlas en pseudocódigo.
- Imprimir resultados sin rótulo descriptivo.
- Mezclar proveedor con cliente sin decir desde qué perspectiva se habla.

### 8.5 Resumen de rúbrica institucional (RA3)
| Criterio | Peso | Qué espera el docente |
|---|---:|---|
| Identifica variables significativas | 25% | Nombra y tipifica correctamente datos del problema |
| Formula problemas con variables medibles y alcanzables | 35% | Organiza los cálculos con lógica, umbrales y propósito claro |
| Diseña la solución con estructura y pertinencia | 40% | Presenta pseudocódigo ordenado, funcional y coherente con el caso |

---

## 9. Referencias (APA 7.ª edición)
Cairó Battistutti, O., & Guardati Bueno, S. I. (2006). *Metodología de la programación: Algoritmos, diagramas de flujo y programas* (3.ª ed.). Alfaomega.

Joyanes Aguilar, L. (2008). *Fundamentos de programación: Algoritmos, estructura de datos y objetos* (3.ª ed.). McGraw-Hill Interamericana.

Ministerio de Educación Nacional. (2017). *Decreto 1421 de 2017: Por el cual se reglamenta en el marco de la educación inclusiva la atención educativa a la población con discapacidad*. https://www.mineducacion.gov.co
