# 📖 Semana 2 — Materiales: Materia Prima, valoración y control
**UBA | GOL06 Costos y Presupuestos | RA1**
**Caso:** LOGÍSATL S.A.S.

---

## 🎯 Objetivo de la semana
Clasificar los materiales en directos e indirectos, aplicar métodos de valoración de inventarios (PEPS, UEPS, Promedio Ponderado) y reconocer los documentos de control de materiales.

---

## 🧩 Analogía: El almacén de una tienda de barrio

Una tienda de barrio en Barranquilla tiene en su trastienda arroz, aceite, azúcar, jabón. El dueño sabe exactamente cuántas libras entran, cuántas se venden y cuántas quedan. Si no lleva ese control, nunca sabe si le están robando o si está agotando productos.

> La bodega de LOGÍSATL es exactamente esa trastienda — pero más grande y con más gente pasando. **El control de materiales evita pérdidas, robos y desperdicios.**

---

## 📚 Contenido teórico

### Tipos de materiales

| Tipo | Definición | Ejemplo LOGÍSATL |
|---|---|---|
| **Materiales Directos (MD)** | Se incorporan físicamente al servicio y son medibles por orden | Cinta de embalaje por paleta, zuncho, stretch film, estibas asignadas |
| **Materiales Indirectos (MI)** | Necesarios para la operación pero no asignables a una orden específica | Aceite para montacargas, guantes de seguridad, marcadores para rotulación |

### Documentos de control de materiales

| Documento | Para qué sirve | En LOGÍSATL |
|---|---|---|
| **Orden de Compra** | Solicitar materiales al proveedor | Pedir 500 rollos de stretch film |
| **Nota de Entrada** | Registrar ingreso de materiales a bodega | 500 rollos recibidos del proveedor |
| **Requisición de Materiales** | Solicitar materiales para una orden específica | "Para la orden 045 (cliente Pinturas Costa) necesito 12 rollos" |
| **Tarjeta de Kárdex** | Control permanente de entradas, salidas y saldo | Hoja donde se registra cada movimiento del stretch film |

### Métodos de valoración de inventarios

Cuando entra material a diferentes precios, ¿a cuál precio se "saca" cuando se usa?

**PEPS (Primero en Entrar, Primero en Salir)**
> Lo que llegó primero es lo primero que se consume. El inventario final queda valorado a los precios más recientes.

**UEPS (Último en Entrar, Primero en Salir)**
> Lo último que llegó es lo primero que se consume. El inventario final queda a precios más antiguos (menos usada en NIIF).

**Promedio Ponderado**
> Se calcula un precio promedio cada vez que entra material nuevo. Es el más usado en Colombia.

---

## 🔢 Ejercicio numérico resuelto: Kárdex del Stretch Film en LOGÍSATL

**Método: Promedio Ponderado**

```
KÁRDEX — STRETCH FILM (rollos)
LOGÍSATL S.A.S. — Enero 2024

Fecha   | Concepto          | Entradas        | Salidas         | Saldo
        |                   | Cant. PU  Total | Cant. PU  Total | Cant. PU   Total
────────────────────────────────────────────────────────────────────────────────────
01-ene  | Saldo inicial     |                 |                 | 80  $8.200  $656.000
05-ene  | Compra OC-001     | 200  $8.500  $1.700.000 |        | 280  $8.414* $2.356.000
        | *Nuevo promedio: (656.000+1.700.000)/280 = $8.414
10-ene  | Req. Orden #041   |                 | 45  $8.414  $378.630 | 235 $8.414 $1.977.290
15-ene  | Req. Orden #042   |                 | 60  $8.414  $504.840 | 175 $8.414 $1.472.450
20-ene  | Compra OC-002     | 150  $8.700  $1.305.000 |        | 325  $8.545* $2.777.125
        | *Nuevo promedio: (1.472.450+1.305.000)/325 = $8.545
28-ene  | Req. Orden #043   |                 | 80  $8.545  $683.600 | 245 $8.545 $2.093.525

RESUMEN ENERO:
  Total comprado:   350 rollos   $3.005.000
  Total usado:      185 rollos   $1.567.070
  Inventario final: 245 rollos   $2.093.525 (queda valorado al promedio actual)
```

### Diferencia entre métodos (mismo ejemplo simplificado)

| Método | Costo de lo vendido/usado | Inventario final |
|---|---|---|
| PEPS | Más bajo (precios viejos) | Más alto (precios nuevos) |
| UEPS | Más alto (precios nuevos) | Más bajo (precios viejos) |
| **Promedio** | **Intermedio** | **Intermedio** |

---

## ✅ Puntos clave para recordar

1. **MD vs. MI:** ¿Se puede asignar a una orden específica? Sí → directo. No → indirecto
2. La **requisición** es el documento que "saca" materiales de bodega para una orden
3. El **promedio ponderado** se recalcula cada vez que entra material nuevo
4. El método de valoración afecta el **costo del servicio** y por tanto la utilidad reportada
5. Un **Kárdex** bien llevado evita robos, desperdicios y errores de costeo

---

## 🧠 Pregunta de reflexión

> LOGÍSATL tiene en bodega 100 rollos de zuncho valorados a $3.200 c/u (compra de diciembre).
> En enero compra 200 rollos más a $3.500 c/u.
> En febrero usa 150 rollos para el pedido del cliente Cervecería Norte.
>
> ¿A qué valor sale esa materia prima del kárdex bajo promedio ponderado?
> ¿Cambiaría el costo de ese servicio si usáramos PEPS?

---

*Material UBA | GOL06 | Semana 2 de 13*

---
---

# 📖 Semana 3 — Mano de Obra: directa, indirecta, liquidación y control
**UBA | GOL06 Costos y Presupuestos | RA1**
**Caso:** LOGÍSATL S.A.S.

---

## 🎯 Objetivo de la semana
Clasificar la mano de obra en directa e indirecta, calcular el costo real de un trabajador incluyendo prestaciones sociales, y asignar la MO a las órdenes de servicio correspondientes.

---

## 🧩 Analogía: El equipo de fútbol

En un equipo de fútbol profesional:
- Los **11 titulares en la cancha** → producen directamente el juego → **Mano de Obra Directa**
- El **DT, el preparador físico, el médico, el utilero** → apoyan la producción pero no están en la cancha → **Mano de Obra Indirecta**

> Si el equipo gana, ¿quién produjo el resultado? Todos contribuyeron, pero el costo de los titulares es más fácil de asignar a cada partido.

**En LOGÍSATL:** Los operadores de bodega y conductores que trabajan en órdenes específicas = MOD. El supervisor de turno, el jefe de bodega, la recepcionista = MOI.

---

## 📚 Contenido teórico

### Clasificación de la Mano de Obra

| Tipo | Definición | Ejemplo LOGÍSATL |
|---|---|---|
| **MOD** (Mano de Obra Directa) | Trabajadores que participan directamente en cada orden de servicio, identificables y medibles | Operadores de bodega, conductores de flota asignados a rutas específicas |
| **MOI** (Mano de Obra Indirecta) | Personal de apoyo no asignable a órdenes específicas | Supervisor de bodega, jefe de logística, personal de limpieza |

### El costo real del trabajador (carga prestacional)

⚠️ El salario básico NO es el costo real. En Colombia, un empleado cuesta entre **1.5 y 1.7 veces** su salario por las prestaciones y aportes.

```
COSTO REAL DE UN OPERADOR EN LOGÍSATL
(Salario base: $1.800.000/mes)

SALARIO BÁSICO:                     $1.800.000

PRESTACIONES SOCIALES:
  Cesantías (8.33%):                  $150.000
  Intereses cesantías (1%):            $18.000
  Prima de servicios (8.33%):         $150.000
  Vacaciones (4.17%):                  $75.000

SEGURIDAD SOCIAL (cargo empresa):
  Salud (8.5%):                       $153.000
  Pensión (12%):                      $216.000
  ARL (riesgo III: 2.436%):            $43.848

PARAFISCALES:
  SENA (2%):                           $36.000
  ICBF (3%):                           $54.000
  Caja de Compensación (4%):           $72.000
  ────────────────────────────────────────────
COSTO TOTAL MENSUAL:                $2.767.848
FACTOR PRESTACIONAL: 2.767.848 / 1.800.000 = 1.538
```

> Por cada $1.000.000 de salario, LOGÍSATL paga $1.538.000 en costo real.

### Control de la Mano de Obra: tarjeta de tiempo

```
TARJETA DE TIEMPO — Operador: Carlos Pérez
Semana: 15–19 enero 2024

Día     | Orden asignada | Horas trabajadas | Tipo
────────────────────────────────────────────────────
Lunes   | Orden #041     | 8 horas          | MOD
Martes  | Orden #041     | 6 horas          | MOD
        | Mantenimiento  | 2 horas          | MOI
Miércoles | Orden #042   | 8 horas          | MOD
Jueves  | Orden #042     | 8 horas          | MOD
Viernes | Capacitación   | 8 horas          | MOI
────────────────────────────────────────────────────
TOTAL:  MOD = 30 horas  |  MOI = 10 horas
```

### Costo de la MO por hora

```
Costo hora normal = Costo mensual / Horas trabajadas normales
= $2.767.848 / 192 horas (24 días × 8 horas) = $14.416/hora

Costo hora extra (diurna): $14.416 × 1.25 = $18.020/hora
Costo hora extra (nocturna): $14.416 × 1.75 = $25.228/hora
```

---

## 🔢 Ejercicio numérico resuelto

**Orden #041** requirió los siguientes recursos de MO:

```
Operador Carlos Pérez: 14 horas MOD × $14.416/hora =    $201.824
Operador María López:  12 horas MOD × $14.416/hora =    $172.992
Conductor Jhon Reyes:   8 horas MOD × $14.416/hora =    $115.328
                                                       ───────────
COSTO TOTAL MO DIRECTA ORDEN #041:                     $490.144
```

---

## ✅ Puntos clave para recordar

1. **MOD:** asignable a una orden específica | **MOI:** va a los CIF
2. El costo real del trabajador incluye **prestaciones + seguridad social + parafiscales**
3. En Colombia el factor prestacional es aproximadamente **1.5 × el salario base**
4. La **tarjeta de tiempo** es el documento que distribuye las horas entre órdenes
5. Las **horas extras** incrementan el costo-hora y deben monitorearse

---

## 🧠 Pregunta de reflexión

> LOGÍSATL tiene un supervisor de bodega con salario de $3.200.000.
> Trabaja 192 horas al mes. El 70% de su tiempo lo dedica a supervisar operaciones
> directas y el 30% a tareas administrativas.
>
> ¿Cuánto de su costo (incluyendo factor prestacional 1.538) es MOD?
> ¿Cuánto es MOI?
> ¿Cómo lo clasificarías en el costeo de una orden específica?

---

*Material UBA | GOL06 | Semana 3 de 13*

---
---

# 📖 Semana 4 — Costos Indirectos de Fabricación (CIF): naturaleza y tasas de aplicación
**UBA | GOL06 Costos y Presupuestos | RA1**
**Caso:** LOGÍSATL S.A.S.

---

## 🎯 Objetivo de la semana
Identificar y clasificar los CIF, presupuestarlos para el período y calcular tasas de aplicación para asignarlos a las órdenes de servicio.

---

## 🧩 Analogía: El "costo invisible" de la oficina

Cuando contratas a un empleado, no solo pagas su salario. También necesitas: un escritorio, energía eléctrica para la computadora, internet, papel, impresora, seguridad del edificio. Ninguno de esos costos "aparece" en un producto específico, pero todos son necesarios para que el trabajo ocurra.

> Los **CIF son exactamente esos costos invisibles** de la producción — nadie los ve en el producto final, pero sin ellos la producción no existiría.

---

## 📚 Contenido teórico

### ¿Qué son los CIF?

Los Costos Indirectos de Fabricación (o de Operación, en servicios) incluyen **todo lo necesario para producir excepto la MP directa y la MOD**.

### CIF en LOGÍSATL S.A.S.

| Categoría | Ejemplos concretos | Comportamiento |
|---|---|---|
| **MO Indirecta** | Supervisor bodega, jefe de logística, seguridad | Fijo |
| **Depreciación** | Montacargas, camiones (parte no asignada directamente), instalaciones | Fijo |
| **Arrendamientos** | Bodega 4.200 m² en Zona Industrial Vía 40 | Fijo |
| **Servicios públicos** | Energía eléctrica, agua, gas | Semivariable |
| **Mantenimiento** | Revisiones programadas flota, mantenimiento bodega | Semivariable |
| **Seguros** | Seguro de carga, SOAT flota | Fijo |
| **Materiales indirectos** | Guantes, aceite montacargas, herramientas | Variable |
| **Otros** | Impuestos de industria y comercio, vigilancia | Fijo |

### El problema de los CIF: no se pueden asignar directamente

Aquí está el reto: la bodega arrendada cuesta $5.500.000/mes. ¿Cuánto le corresponde a la Orden #041 del cliente Textiles Mar? ¿Y a la Orden #042 del cliente Cervecería Norte?

**Solución: Tasa de Aplicación de CIF**

```
Tasa Predeterminada = CIF Presupuestado Total / Base de Aplicación Elegida

BASES DE APLICACIÓN POSIBLES:
  • Horas de MOD (más usada en servicios)
  • Costo de MOD
  • Horas-máquina (montacargas, camiones)
  • Unidades de servicio
  • Metros cuadrados ocupados
```

### Ejemplo: Cálculo de tasa para LOGÍSATL

**Presupuesto CIF mensual LOGÍSATL:**

```
MOI (supervisor, jefe logística, seguridad):   $4.200.000
Arrendamiento bodega:                          $5.500.000
Depreciación flota y equipo:                   $2.800.000
Servicios públicos:                            $1.200.000
Seguros:                                         $850.000
Mantenimiento:                                   $650.000
Materiales indirectos:                           $380.000
Otros:                                           $420.000
──────────────────────────────────────────────────────────
TOTAL CIF PRESUPUESTADO:                      $16.000.000

Base elegida: Horas de MOD presupuestadas: 960 horas/mes
(8 operadores × 24 días × 5 horas promedio asignadas a órdenes)

TASA CIF = $16.000.000 / 960 horas = $16.667 por hora de MOD
```

### Aplicación a órdenes

```
Orden #041 consumió 30 horas MOD:
CIF aplicado = 30 h × $16.667 = $500.010

Orden #042 consumió 22 horas MOD:
CIF aplicado = 22 h × $16.667 = $366.674
```

### ¿Qué pasa si el CIF real ≠ CIF aplicado?

Al final del período puede haber:
- **Sub-aplicación:** CIF real > CIF aplicado → se sub-distribuyó → ajuste al costo de ventas
- **Sobre-aplicación:** CIF real < CIF aplicado → se sobre-distribuyó → ajuste al costo de ventas

---

## 🔢 Costo total de la Orden #041 — LOGÍSATL

```
HOJA DE COSTOS — ORDEN #041
Cliente: Textiles Mar S.A.S. | Fecha: 10–12 enero 2024

MP  Directos:
    Stretch film (45 rollos × $8.414):        $378.630
    Estibas (8 × $12.000):                    $96.000
    Zuncho y cinta:                            $35.000
    SUBTOTAL MP:                              $509.630

MO  Directa:
    Operador Carlos Pérez (14h × $14.416):    $201.824
    Operador María López (12h × $14.416):     $172.992
    Conductor Jhon Reyes (8h × $14.416):      $115.328
    SUBTOTAL MO:                              $490.144

CIF Aplicados:
    30 horas MOD × $16.667/h:                 $500.010

═══════════════════════════════════════════════════════
COSTO TOTAL ORDEN #041:                     $1.499.784
Precio cobrado al cliente:                  $2.100.000
Utilidad bruta:                               $600.216  (28.6%)
```

---

## ✅ Puntos clave para recordar

1. **CIF = todo lo que no es MP directa ni MOD**, pero es necesario para producir/servir
2. Los CIF **no se pueden asignar directamente** → se necesita una tasa de aplicación
3. **Tasa = CIF Presupuestado / Base de aplicación**
4. La **base más común** en servicios es las horas de MOD
5. Al final del período, la diferencia entre CIF real y CIF aplicado requiere **ajuste**

---

## 🧠 Pregunta de reflexión (REPASO PARA PARCIAL 1)

> Con todos los datos que tienes de LOGÍSATL, completa mentalmente:
>
> Si la Orden #042 (cliente Cervecería Norte) consumió:
> - MP directos: $620.000
> - 22 horas de MOD a $14.416/hora
> - Tasa CIF: $16.667/hora
>
> ¿Cuál es el costo total de esa orden?
> Si se cobró $1.800.000, ¿cuál es el margen bruto?
> ¿Es rentable ese cliente para LOGÍSATL?

---

*Material UBA | GOL06 | Semana 4 de 13 — ÚLTIMA ANTES DEL PARCIAL 1*
