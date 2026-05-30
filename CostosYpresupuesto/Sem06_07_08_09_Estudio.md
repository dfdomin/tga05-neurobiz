# 📖 Semana 6 — Sistemas de Producción y Tipos de Costeo
**UBA | GOL06 Costos y Presupuestos | RA2**
**Caso:** LOGÍSATL S.A.S.

---

## 🎯 Objetivo de la semana
Identificar los principales sistemas de producción, relacionarlos con el tipo de costeo apropiado, y determinar cuál aplica para LOGÍSATL.

---

## 🧩 Analogía: Fábrica de camisas vs. pastelería custom

**Fábrica de camisas:** Produce 5.000 camisas talla M azules estándar todos los días. El proceso es idéntico para todas. El costo de una camisa = costo total del lote / 5.000.
→ **Sistema por procesos** (producción masiva y homogénea)

**Pastelería custom:** Cada torta es diferente: diferente tamaño, sabor, decoración, para un cliente diferente. El costo de cada torta se calcula por separado.
→ **Sistema por órdenes** (producción bajo pedido, cada unidad o lote es único)

> ¿Y LOGÍSATL? Cada cliente tiene una necesidad diferente: distinta carga, distinta ruta, distinta cantidad de embalaje. El costo no puede ser el mismo para todos.
> **LOGÍSATL usa costeo por órdenes de servicio.**

---

## 📚 Contenido teórico

### Sistemas de producción

| Sistema | Características | Tipo de empresa | Sistema de costeo que usa |
|---|---|---|---|
| **Por órdenes** | Producción bajo pedido específico, cada unidad o lote es diferente | Talleres, constructoras, empresas logísticas, agencias, imprentas | **Costeo por órdenes** |
| **Por procesos** | Producción continua y homogénea en masa | Cementeras, refinerías, empresas de alimentos masivos | **Costeo por procesos** |
| **Mixto** | Combinación de los dos anteriores | Automotriz, textiles semi-personalizados | Híbrido |

### Tipos de costeo según el tratamiento de los CIF

| Tipo | ¿Qué incluye en el costo? | Ventaja | Limitación |
|---|---|---|---|
| **Costeo Absorbente** (total) | MP + MOD + CIF fijos + CIF variables | Base para estados financieros NIIF | Los fijos "se esconden" en el inventario |
| **Costeo Variable** (directo) | Solo MP + MOD + CIF variables | Mejor para decisiones gerenciales | No acepta NIIF para informes externos |

### Costeo histórico vs. predeterminado

| Tipo | Cuándo se calcula el costo | Uso |
|---|---|---|
| **Histórico (real)** | Después de terminada la producción | Control post-operación |
| **Predeterminado** | Antes de la producción (estándar o estimado) | Planeación y control presupuestal |

---

## 🔢 Diagnóstico de LOGÍSATL

```
DIAGNÓSTICO DEL SISTEMA DE COSTEO — LOGÍSATL S.A.S.

¿La producción es homogénea?           NO → cada orden es diferente
¿Cada cliente tiene necesidades únicas? SÍ
¿Se pueden identificar MP, MO por orden? SÍ

CONCLUSIÓN: LOGÍSATL usa COSTEO POR ÓRDENES DE SERVICIO (COS)

Documento central: HOJA DE COSTOS por orden
Una hoja de costos = un cliente/pedido = un acumulador de MP + MO + CIF
```

---

## ✅ Puntos clave para recordar

1. El sistema de costeo debe ser coherente con el **tipo de producción**
2. **Por órdenes:** producción bajo pedido → cada orden tiene su propia hoja de costos
3. **Por procesos:** producción masiva → el costo se promedia por período y unidades
4. **Costeo absorbente:** incluye CIF fijos → requerido por NIIF
5. **Costeo variable:** excluye CIF fijos → mejor para decisiones internas

---

## 🧠 Pregunta de reflexión

> Imagina que LOGÍSATL decide ofrecer un nuevo servicio: "almacenamiento mensual estándar" a $800.000/mes fijo para cualquier cliente con hasta 20 paletas.
> ¿Cambia el sistema de costeo apropiado?
> ¿Qué pasa con la hoja de costos individual en ese caso?

---

*Material UBA | GOL06 | Semana 6 de 13*

---
---

# 📖 Semana 7 — Costeo por Órdenes de Servicio (Producción)
**UBA | GOL06 Costos y Presupuestos | RA2**
**Caso:** LOGÍSATL S.A.S.

---

## 🎯 Objetivo de la semana
Construir una hoja de costos completa para una orden de servicio logístico, acumulando MP, MO y CIF según los documentos de soporte.

---

## 🧩 Analogía: El restaurante a la carta

En un restaurante de carta, cada mesa pide algo diferente. El mesero abre una **comanda** cuando la mesa llega, y cada cosa que pide la mesa se va anotando en esa comanda: la entrada, el plato fuerte, el postre, las bebidas. Al final, la comanda tiene el total exacto de esa mesa.

> La **Hoja de Costos** es la comanda de LOGÍSATL. Se abre cuando llega la orden del cliente, y en ella se acumulan todos los costos: los materiales pedidos por esa orden, las horas de los trabajadores asignados, y la parte proporcional de los CIF.

---

## 📚 Contenido teórico

### La Hoja de Costos — documento central del sistema por órdenes

```
ESTRUCTURA DE LA HOJA DE COSTOS

Encabezado:
  Número de orden, cliente, descripción del servicio,
  fecha de inicio, fecha de entrega prometida.

Cuerpo — tres secciones:
  ┌─────────────────┬──────────────────┬──────────────────┐
  │ MATERIALES      │ MANO DE OBRA     │ CIF APLICADOS    │
  │ DIRECTOS        │ DIRECTA          │                  │
  ├─────────────────┼──────────────────┼──────────────────┤
  │ Requisición #   │ Tarjeta tiempo   │ Tasa × base      │
  │ Material/cant.  │ Empleado/horas   │                  │
  │ Valor unitario  │ Costo/hora       │                  │
  │ Total           │ Total            │ Total            │
  └─────────────────┴──────────────────┴──────────────────┘

Resumen:
  Total MP + Total MOD + Total CIF = COSTO TOTAL DE LA ORDEN
```

### Flujo de documentos que alimentan la Hoja de Costos

```
Requisición de materiales → MP de la Hoja de Costos
Tarjeta de tiempo → MO de la Hoja de Costos
Tasa predeterminada × horas usadas → CIF de la Hoja de Costos
```

---

## 🔢 Ejercicio completo — Orden #048 LOGÍSATL

**Cliente:** Distribuidora Caribe S.A.S.
**Servicio:** Recepción, almacenamiento (10 días) y distribución de 800 cajas de producto.

**Documentos de soporte:**

*Requisición #R-055:*
- Stretch film: 35 rollos × $8.545 = $299.075
- Estibas nuevas: 6 × $12.000 = $72.000
- Zuncho y cinta: $28.000

*Tarjeta de tiempo:*
- Operadora Ana Torres: 18 h MOD × $14.416 = $259.488
- Operador Pedro Manjarrez: 16 h MOD × $14.416 = $230.656
- Conductor Ramiro Salas: 12 h MOD × $14.416 = $172.992

*CIF:*
- Horas MOD totales: 46 horas × $16.667 = $766.682

```
HOJA DE COSTOS — ORDEN #048
Cliente: Distribuidora Caribe S.A.S.
Período: 5–15 febrero 2024

MATERIALES DIRECTOS:
  Stretch film (R-055):                $299.075
  Estibas (R-055):                      $72.000
  Zuncho y cinta (R-055):               $28.000
  SUBTOTAL MP:                         $399.075

MANO DE OBRA DIRECTA:
  Ana Torres — 18h × $14.416:         $259.488
  Pedro Manjarrez — 16h × $14.416:    $230.656
  Ramiro Salas — 12h × $14.416:       $172.992
  SUBTOTAL MOD:                        $663.136

CIF APLICADOS:
  46 horas MOD × $16.667/h:           $766.682

═══════════════════════════════════════════════
COSTO TOTAL ORDEN #048:              $1.828.893
Precio facturado al cliente:         $2.600.000
Utilidad bruta:                        $771.107
Margen bruto:                             29.7%
```

---

## ✅ Puntos clave para recordar

1. Una **Hoja de Costos** = una orden = un acumulador de los tres elementos
2. La HdC se **abre al iniciar** la orden y se **cierra al terminarla**
3. Los documentos fuente son: Requisición (MP), Tarjeta de tiempo (MO), Tasa predeterminada (CIF)
4. El costo total permite calcular la **rentabilidad por cliente**
5. Al acumular todas las HdC del período se obtiene el **Estado de Costos**

---

## 🧠 Pregunta de reflexión

> LOGÍSATL tiene dos clientes recurrentes:
> Cliente A: órdenes de alto volumen (muchos materiales, pocas horas de MO)
> Cliente B: órdenes de alto servicio (pocos materiales, muchas horas de MO especializado)
>
> Si la tasa de CIF se calcula sobre horas MOD, ¿cuál cliente carga más CIF?
> ¿Es eso justo? ¿Qué base de aplicación diferente podría ser más equitativa?

---

*Material UBA | GOL06 | Semana 7 de 13*

---
---

# 📖 Semana 8 — Costeo por Procesos
**UBA | GOL06 Costos y Presupuestos | RA2**
**Caso:** LOGÍSATL S.A.S. + empresa comparativa

---

## 🎯 Objetivo de la semana
Aplicar el costeo por procesos para calcular el costo unitario por período y reconocer cuándo este sistema es apropiado vs. el costeo por órdenes.

---

## 🧩 Analogía: La línea de ensamblaje de un carro

En una planta de Toyota, cada carro pasa por las mismas estaciones: carrocería → motor → electricidad → pintura → acabados. Al final del día, salieron 400 carros exactamente iguales. El costo de UN carro = costo total de la planta ese día / 400.

> Nadie pregunta "¿cuánto costó exactamente el carro #227?". Todos costaron lo mismo.

**¿Cuándo LOGÍSATL usaría costeo por procesos?** Si ofreciera un servicio estándar (ej. "servicio de entrega exprés urbana — siempre lo mismo") a miles de usuarios. En ese caso, el costo por entrega = total del mes / número de entregas.

---

## 📚 Contenido teórico

### Características del costeo por procesos

| Característica | Descripción |
|---|---|
| Producción continua | El proceso no para entre unidades |
| Unidades homogéneas | Todas las unidades son iguales |
| Acumulación por departamento/proceso | Los costos se acumulan por etapa, no por pedido |
| Costo unitario | Se calcula al dividir el costo total por las unidades producidas |

### Unidades equivalentes — el concepto clave

Al final del período, algunas unidades están terminadas y otras están en proceso (incompletas). Las unidades **en proceso** se convierten a **unidades equivalentes** según su grado de avance.

```
Fórmula:
Unidades equivalentes = Unidades terminadas + (Unidades en proceso × % de avance)

Ejemplo:
  100 unidades terminadas + 40 unidades en proceso al 50%:
  = 100 + (40 × 0.50) = 120 unidades equivalentes

Costo unitario = Costo total / Unidades equivalentes
```

### Comparación: órdenes vs. procesos en el contexto logístico

| Criterio | Por Órdenes (LOGÍSATL) | Por Procesos (hipotético) |
|---|---|---|
| Unidad de costeo | Una orden = un cliente | Un período = todas las unidades |
| Documento clave | Hoja de costos | Informe de producción del departamento |
| Cuándo se usa | Servicios personalizados | Servicios masivos y estándar |
| Costo unitario | Diferente por cada orden | Igual para todas las unidades del período |

---

## 🔢 Ejercicio por procesos — servicio estándar hipotético

**Situación:** LOGÍSATL lanza un nuevo servicio: "Entrega Urbana Estándar" — distribución de paquetes iguales en Barranquilla. En enero:

```
Unidades al inicio del período: 0
Unidades ingresadas al proceso: 1.200 entregas
Unidades terminadas y entregadas: 1.000
Unidades en proceso al final: 200 (al 60% de avance)

Costos del mes:
  MP (embalajes estándar): $2.400.000
  MOD: $3.600.000
  CIF: $2.000.000
  TOTAL: $8.000.000

Unidades equivalentes:
  1.000 + (200 × 60%) = 1.000 + 120 = 1.120

Costo unitario por entrega:
  $8.000.000 / 1.120 = $7.143/entrega

Costo del servicio completado:
  1.000 × $7.143 = $7.143.000

Inventario en proceso al cierre:
  120 eq. × $7.143 = $857.160
```

---

## ✅ Puntos clave para recordar

1. **Por procesos:** producción masiva, todas las unidades son iguales
2. Las **unidades equivalentes** corrigen el problema de las unidades incompletas
3. El **costo unitario** se calcula dividiendo el total por las unidades equivalentes
4. LOGÍSATL **normalmente usa órdenes**, pero podría usar procesos para servicios estándar
5. La diferencia entre sistemas no es de dificultad sino de **adecuación al tipo de producción**

---

*Material UBA | GOL06 | Semana 8 de 13*

---
---

# 📖 Semana 9 — Estado de Costos de Producción y Ventas: el resumen final
**UBA | GOL06 Costos y Presupuestos | RA2**
**Caso:** LOGÍSATL S.A.S.

---

## 🎯 Objetivo de la semana
Construir el Estado de Costos de Producción y Ventas completo de LOGÍSATL, integrando todos los elementos del costo del período.

---

## 🧩 Analogía: El resumen de una temporada deportiva

Al final de la temporada, el director técnico hace el balance: ¿cuántos partidos se jugaron, cuántos goles se metieron, qué jugadores más rindieron, cuánto costó la plantilla? El **Estado de Costos** es ese balance — un resumen de todo lo que costó producir y vender los servicios del período.

---

## 📚 Estructura del Estado de Costos de Producción y Ventas

```
ESTADO DE COSTOS DE PRODUCCIÓN Y VENTAS
(Empresa manufacturera — se adapta a servicios)

MATERIA PRIMA:
  Inventario inicial de MP                    XXX
  + Compras netas de MP                       XXX
  = MP disponible para uso                    XXX
  - Inventario final de MP                   (XXX)
  = MATERIA PRIMA USADA                       XXX

MANO DE OBRA DIRECTA:                         XXX

CIF:                                          XXX
  MOI, depreciación, arriendo, etc.
  ────────────────────────────────────────────────
= COSTO DE PRODUCCIÓN DEL PERÍODO             XXX

+ Inventario inicial de producción en proceso XXX
= COSTO DE PRODUCCIÓN EN PROCESO              XXX
- Inventario final de producción en proceso  (XXX)
  ────────────────────────────────────────────────
= COSTO DE SERVICIOS/PRODUCTOS TERMINADOS     XXX

+ Inventario inicial de terminados            XXX
= COSTO DISPONIBLE PARA VENTA                 XXX
- Inventario final de terminados             (XXX)
  ════════════════════════════════════════════════
= COSTO DE SERVICIOS/PRODUCTOS VENDIDOS       XXX
```

---

## 🔢 Estado de Costos de LOGÍSATL — Enero 2024

```
LOGÍSATL S.A.S.
ESTADO DE COSTOS DE SERVICIOS PRESTADOS
Mes de enero de 2024
(Cifras en pesos colombianos)

MATERIALES DIRECTOS:
  Inventario inicial (01-ene):           $1.840.000
  + Compras del mes:                     $3.005.000
  = MP disponible:                       $4.845.000
  − Inventario final (31-ene):          ($2.093.525)
  = MATERIALES DIRECTOS USADOS:         $2.751.475

MANO DE OBRA DIRECTA:
  Total MOD del mes (ver nómina):        $4.120.480

COSTOS INDIRECTOS DE FABRICACIÓN:
  CIF aplicados en el mes (órdenes):     $5.833.450
  Ajuste CIF sub-aplicado:                 $166.550
  = CIF REALES DEL MES:                 $6.000.000
  ──────────────────────────────────────────────────
COSTO DE SERVICIOS DEL PERÍODO:        $12.871.955

+ Servicios en proceso inicio mes:               $0
= COSTO EN PROCESO:                    $12.871.955
− Servicios en proceso fin mes:                  $0 *
  ══════════════════════════════════════════════════
COSTO TOTAL DE SERVICIOS PRESTADOS:   $12.871.955

*En servicios logísticos, generalmente no hay WIP (servicio se completa en el período)

VERIFICACIÓN CON EL ERI:
Ingresos del mes:                      $18.500.000
− Costo de servicios prestados:       ($12.871.955)
= UTILIDAD BRUTA:                       $5.628.045  (30.4% margen bruto)
− Gastos operacionales:                ($2.400.000)
= UTILIDAD OPERACIONAL:                 $3.228.045
```

---

## ✅ Puntos clave para recordar

1. El Estado de Costos integra **MP + MO + CIF** del período completo
2. Mueve el costo a través de las tres etapas: **materiales → en proceso → terminados → vendidos**
3. El **inventario final de MP** reduce el costo del período (lo que no se usó, no se gasta)
4. El ajuste de CIF (sub/sobre aplicado) corrige la diferencia entre tasa predeterminada y CIF real
5. El costo de servicios prestados es el **primer gran componente del ERI** → conecta con contabilidad financiera

---

## 🧠 Pregunta de reflexión (REPASO PARA PARCIAL 2)

> Si LOGÍSATL compra $4.000.000 en materiales en febrero pero solo usa $3.200.000,
> ¿cuánto va al Estado de Costos como MP?
> ¿Qué pasa con los $800.000 restantes?
> ¿Dónde aparecen en el balance?

---

*Material UBA | GOL06 | Semana 9 de 13 — ÚLTIMA ANTES DEL PARCIAL 2*
