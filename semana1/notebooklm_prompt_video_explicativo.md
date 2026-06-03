# NotebookLM Prompt — Video Explicativo Semana 1 TGA05

## Instrucciones para el docente

1. Ve a https://notebooklm.google.com
2. Crea un nuevo notebook llamado "TGA05 - Semana 1 Explicativa"
3. Sube como fuentes:
   - El archivo `semana1/index.html` (arrastra el archivo completo)
   - El texto de CONTEXTO ADICIONAL de abajo (cópialo en un .txt y súbelo también)
4. Ve a "Audio Overview" → "Customize" (Personalizar)
5. Pega el PROMPT DE PERSONALIZACIÓN de abajo
6. Genera. Duración sugerida: 12-15 minutos.

---

## CONTEXTO ADICIONAL (crear archivo semana1_contexto.txt y subir)

```
TGA05 - ESTRUCTURA DE DATOS PARA LOS NEGOCIOS
Semana 1: Estructuras de Datos Elementales
Institución Universitaria de Barranquilla (IUB)
Caso transversal: NeuroBiz S.A.S. — clínica de terapia con 1.200 sesiones mensuales

ESTRUCTURA DE LA SEMANA 1 — 10 ACTIVIDADES DE DESARROLLO:

1. 📊 MINI COLAB: KPIs NeuroBiz (Bloque 1)
   Objetivo: Que el estudiante declare variables con los tipos correctos en Python.
   Los KPIs de NeuroBiz vienen mal tipados (números como texto). El estudiante debe
   declarar sesiones_asistidas=847 (int), tasa_retencion=0.78 (float), etc.
   Bloom: Recordar → Aplicar. XP: +2.

2. 📅 MINI COLAB: Arreglo de sesiones mensuales (Bloque 2)
   Objetivo: Crear una lista con las sesiones de 4 semanas y calcular total, promedio,
   semana máxima. Introduce el concepto de arreglo como estructura indexada.
   Bloom: Aplicar. XP: +2.

3. 🕵️ AUDITORÍA DE DATOS — Paso 1: Diagnóstico Interactivo
   Objetivo: Corregir 5 variables mal tipadas del caso NeuroBiz. El estudiante
   selecciona el tipo correcto (int/float/str/bool) en un dropdown y escribe el valor
   corregido. Sistema de verificación inmediata con ✅/❌ por variable.
   Variables: sesiones_asistidas, tasa_retencion, sede, contrato_activo, nivel_hiperfoco.
   Bloom: Analizar → Evaluar. XP: +10 al completar 5/5.

4. 📝 AUDITORÍA DE DATOS — Paso 2: Código Corregido
   Objetivo: El sistema genera automáticamente el código Python corregido al completar
   el Paso 1. El estudiante ve la versión correcta como referencia.
   Bloom: Comprender. XP: incluido en Paso 1.

5. 🐍 GOOGLE COLAB EN VIVO (5 celdas)
   Objetivo: Ejecutar Python real en el navegador con Pyodide (WebAssembly).
   Celda 1: Código sucio original para inspeccionar.
   Celda 2: Espacio para escribir la versión corregida.
   Celda 3: Cálculo del reporte de eficiencia.
   Celda 4: Declaración de KPIs (Bloque 1 interactivo).
   Celda 5: Arreglo de sesiones con operaciones (Bloque 2 interactivo).
   Cada celda tiene botón ▶ Run que ejecuta Python real.
   Bloom: Aplicar → Crear. XP: +2 por celda ejecutada.

6. ✍️ CODECADEMY — Fill-in-the-Blank (3 ejercicios)
   Ejercicio 1: "Corrige los tipos de datos" — completar `sesiones_asistidas = ____`
   con el valor correcto.
   Ejercicio 2: "Completa el cálculo" — escribir operador/fórmula de eficiencia.
   Ejercicio 3: "Declara la variable correcta" — escribir `contrato_activo = True`.
   Validación inmediata con feedback ✅/❌.
   Bloom: Aplicar. XP: +5 por cada ejercicio completado.

7. 🖱️ DRAG & DROP — Arrastrar tipos de datos
   Objetivo: Asociar 6 valores ("847", "78%", "True", "Ana Ramos", "6.4", "[68,72,80]")
   con su tipo Python correcto (int, float, str, bool, list). 
   Usa HTML5 drag & drop nativo. Feedback visual verde/rojo.
   Bloom: Comprender → Analizar. XP: +3 al completar 6/6.

8. 🎮 QUIZ DE VERIFICACIÓN (5 preguntas)
   Objetivo: Evaluar comprensión de tipos de datos, memoria y arreglos.
   P1: TypeError al sumar str + int.
   P2: Acceso O(1) por índice en arreglo.
   P3: float para porcentajes decimales.
   P4: bool para datos sí/no.
   P5: Ventaja de arreglos sobre variables sueltas.
   Respuestas clickeables con botón "Verificar". Scoring: +10 XP si 5/5, +5 XP si 3+/5.
   Bloom: Evaluar.

9. 📊 HTI A — "Ampliando el Dashboard NeuroBiz" (Escenario avanzado)
   Objetivo: Extender el código a 3 sedes usando listas. Code editor con Run integrado.
   El estudiante crea arreglos por sede, calcula totales, identifica la sede más eficiente.
   Botón "Marcar como Entregado" para reportar finalización (+5 XP).
   Bloom: Analizar → Crear. XP: +5.

10. 🗂️ HTI B — "Ficha de Tipos de Datos NeuroBiz" (Escenario básico)
    Objetivo: Tabla fillable para estudiantes con carga académica alta. Completan:
    variable, tipo Python, valor inventado, justificación. Opcional, no bloquea.
    Bloom: Comprender. XP: +2.

PEDAGOGÍA DETRÁS DEL DISEÑO:
- Framework GAME: Generar interés (narrativa NeuroBiz), Activar conocimiento previo
  (diagnóstico), Mediar aprendizaje (teoría + práctica), Evaluar (quiz + auditoría).
- Taxonomía de Bloom: progresión Recordar → Comprender → Aplicar → Analizar → Evaluar → Crear.
- Neurodiversidad: texto en bloques cortos, feedback inmediato, múltiples formatos
  (visual, táctil/drag-drop, textual), sin castigo por error, sin rankings públicos.
- Gamificación: XP por cada actividad, insignias por competencia, barra de progreso
  visible, sin competencia individual.
- Andamiaje: de lo simple (declarar una variable) a lo complejo (dashboard multi-sede).
- Evaluación formativa: cada actividad da feedback inmediato, no solo al final.

CONTEXTO DEL CASO NEUROBIZ:
NeuroBiz S.A.S. es una clínica con 1.200 sesiones mensuales en Barranquilla, Bogotá y
Medellín. Atiende pacientes con neurodivergencias (TDAH, AACC, TEA). Sus datos están
en hojas de cálculo desorganizadas. Los estudiantes son "Analistas de Datos" contratados
para modernizar el sistema. Los KPIs reales son: 847 sesiones asistidas, 112 fallidas,
78% tasa de retención, 6.4/10 índice de progreso.

TECNOLOGÍA:
- Google Colab integrado en la página con Pyodide (Python en WebAssembly)
- Progress Tracker con localStorage + Supabase + Google Sheets
- XP animation, barras de progreso, insignias
- Drag & drop nativo HTML5
- Quiz interactivo con scoring
```

---

## PROMPT DE PERSONALIZACIÓN (pegar en "Customize" de NotebookLM)

```
Genera una conversación en español entre dos personas que sea EL MEJOR VIDEO EXPLICATIVO 
DEL MUNDO sobre la Semana 1 del módulo TGA05 - Estructura de Datos para los Negocios.

PERSONAJES:
- "Valentina": Directora de Innovación Pedagógica de IUB. Experta en diseño instruccional, 
  neurodiversidad y gamificación. Habla con precisión, calidez y entusiasmo contagioso. 
  Conoce cada actividad al detalle y explica POR QUÉ funciona pedagógicamente.
- "Samuel": Docente nuevo de TGA05 que está preparando su primera clase de Estructura de 
  Datos. Viene de la industria (fue ingeniero de datos en una empresa de logística). Es 
  curioso, hace preguntas prácticas, y a veces se sorprende con lo que la pedagogía moderna 
  puede lograr.

ESTRUCTURA DE LA CONVERSACIÓN (12-15 minutos):

PARTE 1 — APERTURA (2 min): El caso que engancha
- Valentina le cuenta a Samuel sobre NeuroBiz S.A.S.: 1.200 sesiones, datos en papel, 
  KPIs que no cuadran. "Samuel, tus estudiantes no vienen a aprender tipos de datos. 
  Vienen a salvar una empresa."
- Samuel: "Espera, ¿me estás diciendo que la semana 1 ya tiene un caso empresarial real?"
- Valentina explica el framework GAME y por qué la narrativa no es decoración: es el motor.

PARTE 2 — LAS 10 ACTIVIDADES, UNA POR UNA (8 min)
Para cada actividad, Valentina explica y Samuel reacciona:

Actividad 1-2 (Mini Colab KPIs y Arreglo):
- V: "Empezamos con lo más simple: declarar variables. Pero no declaras x=5. Declaras 
  sesiones_asistidas=847. El contexto empresarial desde el minuto cero."
- S: "En mi época era 'escribe un programa que sume dos números'. Esto es otra cosa."

Actividad 3-4 (Auditoría de Datos interactiva):
- V: "Aquí está la magia. Les damos datos MAL tipados. Un número guardado como texto. 
  Una sede guardada como 1 en vez de 'Barranquilla'. Ellos hacen de auditores."
- S: "O sea que aprenden tipos de datos detectando errores, no memorizando definiciones."
- V: "Exacto. Y el sistema les dice ✅ o ❌ al instante. Sin esperar a que el profesor 
  corrija 40 trabajos."

Actividad 5 (Google Colab en vivo):
- V: "Python real, en el navegador, sin instalar nada. Ejecutan, ven el output, corrigen."
- S: "¿Sin instalar Python? ¿Cómo?"
- V: "Pyodide. Python compilado a WebAssembly. Tarda 3 segundos en cargar y ya está."

Actividad 6-7 (Codecademy fill-in-the-blank + Drag & Drop):
- V: "Aquí atendemos a la neurodiversidad. Unos estudiantes aprenden escribiendo código. 
  Otros necesitan manipular objetos. El drag & drop es para cerebros cinestésicos."
- S: "Nunca había pensado en que arrastrar un '847' a una caja de 'int' fuera aprendizaje."
- V: "Es evaluación formativa disfrazada de juego. El estudiante no se siente examinado."

Actividad 8 (Quiz):
- V: "5 preguntas. Pero no es un quiz tradicional: eligen opciones, verifican, y si sacan 
  5/5 ganan +10 XP. Si sacan 3/5, +5 XP. Siempre hay recompensa por intentar."
- S: "¿Y el que saca 2/5?"
- V: "No pierde nada. Simplemente no gana XP extra. Pero aprendió. El feedback le muestra 
  la respuesta correcta."

Actividad 9-10 (HTI A y B):
- V: "Dos caminos. El estudiante motivado toma el Escenario A: programa un dashboard para 
  3 sedes. El que viene cansado de trabajar toma el B: completa una tabla en 20 minutos."
- S: "Esto es diseño universal para el aprendizaje."
- V: "Sí. Mismo objetivo, distinta profundidad. Nadie se queda atrás."

PARTE 3 — LA PEDAGOGÍA DETRÁS (3 min)
- V: "¿Sabes cuál es el secreto de esta semana? No es la tecnología. Es que cada 
  actividad responde a una pregunta: ¿qué necesita el cerebro del estudiante AHORA?"
- V explica la progresión de Bloom: de Recordar (tipos de datos) a Crear (dashboard).
- V: "Y todo con feedback inmediato. El cerebro humano aprende cuando recibe respuesta 
  en segundos, no en semanas."
- S: "O sea que eliminaron la espera del 'el profe me corregirá la próxima clase'."
- V: "Exacto. Cada actividad es un ciclo completo: exploro → intento → recibo feedback → 
  corrijo → avanzo. En 10 minutos, no en 7 días."
- V habla de neurodiversidad: "El TDAH necesita bloques cortos y recompensa inmediata. 
  El TEA necesita estructura clara y sin ambigüedad. Las AACC necesitan profundidad 
  sin castigo por ir más rápido. Esta semana cubre los tres."

PARTE 4 — CIERRE INSPIRADOR (2 min)
- S: "Valentina, esto no es una clase de programación. Es una experiencia de aprendizaje."
- V: "Ese es el punto, Samuel. En 2030, el docente no transmite información — eso lo hace 
  Google. El docente diseña experiencias. Y esta semana 1 es una experiencia que atrapa, 
  enseña y no suelta."
- S: "¿Qué le dirías a un docente que está asustado de tanta tecnología?"
- V: "Que empiece por una actividad. Solo una. La Auditoría de Datos. Son 5 dropdowns y 
  un botón. Si eso funciona, la próxima semana agregas otra. No necesitas tragarte el 
  elefante entero."
- Cierre: "Semana 1 de TGA05. Donde los estudiantes dejan de memorizar tipos de datos y 
  empiezan a salvar empresas con Python. Porque aprender no debería doler."

TONO GENERAL:
- Energía positiva, casi de podcast premium (piensa en TED en español, o Radio Ambulante)
- Valentina debe sonar como alguien que YA implementó esto y vio resultados
- Samuel debe ser el espejo del oyente: escéptico al inicio, convencido al final
- Incluir 2-3 momentos de humor ligero (Samuel: "¿Y si el estudiante arrastra 'True' a 
  la caja de 'int'?" Valentina: "La caja se pone roja y le dice que no. Como Tinder, pero 
  con tipos de datos.")
- Sin tecnicismos innecesarios. Si se menciona Pyodide o WebAssembly, explicarlo en una frase.
- El mensaje central: LA TECNOLOGÍA SIRVE A LA PEDAGOGÍA, NO AL REVÉS.
```
