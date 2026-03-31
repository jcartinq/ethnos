---
description: Pipeline Maestro del Analisis Etnografico Complejo — 19 Fases desde RAW data hasta Devolucion a Participantes con validacion epistemica total.
---

# Orquestador: Analisis Etnografico Complejo (Pipeline Completo 19 Fases)

## 1. Mision

Este workflow es el cerebro operativo de ETHNOS. Dirige secuencialmente a los LLMs para que trituren corpus cualitativos complejos sin rendirse ante la tentacion del resumen anodino, aplicando con brutalidad metodologica los 17 Motores, 20 Lentes Teoricos, 4 Protocolos Avanzados, 4 Guias de Campo y 4 Plantillas de Salida del ecosistema. Cada fase alimenta a la siguiente en una cadena de custodia analitica ininterrumpida. Saltarse una fase obligatoria es traicion epistemica.

**Investigador Principal (PI):** Johnny Cartin.

---

## 2. Puesta en Operacion (Entrada de Datos RAW y Contexto)

**Usuario**: "Invoco el `workflow_analisis_etnografico_complejo`. El proyecto es **[NOMBRE_PROYECTO]**. El lente teorico sera **[AUTOR / auto-seleccion]**. La salida debe usar la **[Plantilla Consultoria / Ensayo Academico / Cronica / Bitacora]**."

**Prerequisitos obligatorios:**
- Corpus RAW depositado en `00_Proyectos\[NOMBRE_PROYECTO]\01_Corpus_RAW\`
- Contexto local en `00_Proyectos\[NOMBRE_PROYECTO]\02_Contexto_Local\`
- Protocolo etico verificado (`05_Guias_de_Campo\guia_consentimiento_informado.md`)

**Parametros opcionales del usuario:**
- Imagenes/mapas en `00_Proyectos\[NOMBRE_PROYECTO]\01_Corpus_Visual\` (activa Fase -1)
- Solicitud de auto-seleccion de lente (activa Fase 1.2)
- Indicacion de corpus con focus groups (activa Fase 2.6)
- Multiples codificadores (activa Fase 3.9)

---

## 3. Mapa del Pipeline Completo (19 Fases)

```
FASE -1 .... Semiotica Visual ............... [OPCIONAL]    Pixel a Texto
FASE -0.5 .. Preprocesamiento Corpus ........ [OBLIGATORIA] Limpieza y normalizacion
FASE  0 .... Triaje Masivo .................. [CONDICIONAL] Solo macro-corpus
FASE  1 .... Grounded Theory ................ [OBLIGATORIA] Induccion pura
FASE  1.2 .. Selector de Lentes ............. [OPCIONAL]    Recomendacion post-induccion
FASE  1.5 .. Auditoria Discursiva 12D ....... [OBLIGATORIA] Escrutinio discursivo
FASE  2 .... Lente Teorico .................. [OBLIGATORIA] Traduccion teorica
FASE  2.3 .. Analisis Narrativo ............. [OPCIONAL]    Temporalidad y trama
FASE  2.4 .. ACD ............................ [OPCIONAL]    Critica del discurso
FASE  2.5 .. Q-Square ....................... [OBLIGATORIA] Puente cuali-cuanti
FASE  2.6 .. Etnometodologia ................ [CONDICIONAL] Solo focus groups
FASE  2.8 .. Perfilador Multidimensional .... [OBLIGATORIA] Arquetipos
FASE  3 .... Plantilla de Salida ............ [OBLIGATORIA] Narrativa final
FASE  3.5 .. Abogado del Diablo ............. [OBLIGATORIA] Red Team
FASE  3.7 .. Auditoria Epistemica ........... [OBLIGATORIA] Rigor
FASE  3.8 .. Triangulacion .................. [OBLIGATORIA] Validacion cruzada
FASE  3.9 .. Fiabilidad Inter-codificador ... [CONDICIONAL] Solo multi-codificador
FASE  4 .... Exportacion DOCX ............... [OBLIGATORIA] Entregable corporativo
FASE  5 .... Devolucion Participantes ........ [OBLIGATORIA] Member checking
```

---

## 4. Fase a Fase — Ejecucion Secuencial (Agente LLM)

---

### FASE -1: Semiotica Visual — Pixel a Texto

| Campo | Valor |
|-------|-------|
| **Motor/Skill** | `02_Motores_Metodologicos\skill_semiotica_visual.md` |
| **Obligatoria** | NO — Solo si el usuario adjunta imagenes, mapas o fotografias |
| **Condicion de activacion** | Existen archivos en `00_Proyectos\[PROYECTO]\01_Corpus_Visual\` |
| **Input** | Hasta 3 imagenes/mapas (PNG, JPG) del corpus visual |
| **Output** | Archivo `.md` con decodificacion semiotica: poder espacial, fracturas territoriales, signos visuales codificados |

**Accion LLM**: Revisa si el usuario deposito imagenes en `01_Corpus_Visual`. Si existen, ejecuta el motor de semiotica visual sin piedad. Extrae la semiotica de la region — poder espacial, fracturas territoriales, signos iconicos — usando vision artificial *una sola vez*. Convierte el analisis profundo en texto plano `.md` que se inyecta como contexto en las fases textuales posteriores. Si no hay imagenes, salta esta fase sin remordimiento.

> **BITACORA**: Registrar decision de incluir/excluir corpus visual y justificacion.

---

### FASE -0.5: Preprocesamiento de Corpus — Limpieza y Normalizacion

| Campo | Valor |
|-------|-------|
| **Motor/Skill** | `02_Motores_Metodologicos\skill_preprocesamiento_corpus.md` |
| **Obligatoria** | SI — Todo corpus pasa por aqui antes de tocar un solo motor analitico |
| **Condicion de activacion** | Siempre. Sin excepciones. |
| **Input** | Corpus RAW de `00_Proyectos\[PROYECTO]\01_Corpus_RAW\` |
| **Output** | Corpus limpio y normalizado: sin ruido tipografico, con turnos de habla identificados, segmentado y listo para triaje o induccion directa |

**Accion LLM**: Antes de que cualquier motor analitico toque una sola linea del corpus, este pasa obligatoriamente por el preprocesador. Limpieza de artefactos de transcripcion, normalizacion ortografica, identificacion de turnos de habla, segmentacion de unidades analiticas. Un corpus sucio produce codigos basura — esta fase es el filtro de entrada que protege la integridad de todo el pipeline. El output normalizado reemplaza al corpus RAW como fuente para todas las fases subsiguientes.

> **BITACORA**: Documentar decisiones de limpieza, criterios de segmentacion, elementos eliminados y su justificacion.

---

### FASE 0: Triaje Masivo — Clasificacion Demografica Inicial

| Campo | Valor |
|-------|-------|
| **Motor/Skill** | `02_Motores_Metodologicos\skill_triage_masivo.md` |
| **Obligatoria** | CONDICIONAL — Solo para macro-corpus que excedan capacidad de procesamiento inmediato |
| **Condicion de activacion** | Volumen de datos > umbral manejable (multiples documentos extensos, cientos de paginas) |
| **Input** | Corpus limpio de Fase -0.5 |
| **Output** | Macro-clusters tematicos, clasificacion demografica, raciones digeribles para Fase 1 |

**Accion LLM**: Si el volumen de datos amenaza con desbordar las capacidades inmediatas del agente, ejecuta el triaje masivo. Fragmenta miles de paginas en macro-clusters tematicos filtrando el ruido conversacional, preparando raciones digeribles para la induccion. Para corpus pequenos o medianos, esta fase se salta — el corpus limpio de Fase -0.5 pasa directo a Fase 1.

> **BITACORA**: Si se activa, registrar criterios de fragmentacion y distribucion de clusters. Si se salta, registrar justificacion.

---

### FASE 1: Grounded Theory — Motor de Induccion Pura

| Campo | Valor |
|-------|-------|
| **Motor/Skill** | `02_Motores_Metodologicos\skill_grounded_theory.md` |
| **Obligatoria** | SI — Columna vertebral del pipeline |
| **Condicion de activacion** | Siempre |
| **Input** | Corpus limpio (de Fase -0.5 o clusters de Fase 0) + Contexto Local de `02_Contexto_Local\` + Output de Fase -1 si existe |
| **Output** | Codigos crudos con citas, categorias emergentes, categorias centrales, memo teorico inicial |

**Accion LLM**: Toma el corpus normalizado. Lee OBLIGATORIAMENTE los archivos de contexto local (reportes geograficos, perfiles de clientes, documentos de referencia). Invoca los parametros de `skill_grounded_theory.md` con la ferocidad que exige la codificacion abierta. Extrae los codigos crudos (minimo 10, con cita textual del corpus para cada uno), ponderados e influenciados por el Contexto Local. Agrupa en categorias axiales. Destila las Categorias Centrales. Esta es la columna vertebral inductiva — si aqui se falla, todo el pipeline colapsa.

> **BITACORA**: Registrar codigos emergentes mas significativos, decisiones de agrupacion axial, y categoria(s) central(es) seleccionada(s).

---

### FASE 1.2: Selector de Lentes — Recomendacion Teorica Post-Induccion

| Campo | Valor |
|-------|-------|
| **Motor/Skill** | `03_Orquestadores\workflow_selector_lentes.md` |
| **Obligatoria** | NO — Solo si el usuario solicita auto-seleccion de lente o no pre-selecciono uno |
| **Condicion de activacion** | Usuario indica "auto-seleccion" o no especifica lente teorico en la invocacion |
| **Input** | Categorias centrales y codigos de Fase 1 |
| **Output** | Ranking de 3-5 lentes teoricos recomendados con justificacion, seleccion final del PI |

**Accion LLM**: Si el investigador no pre-selecciono un lente teorico, o solicito recomendacion automatica, ejecuta el selector de lentes. Analiza las categorias centrales emergentes de la Fase 1 y las cruza contra los 20 lentes disponibles en `01_Lentes_Teoricos\`. Presenta un ranking justificado de los 3-5 lentes mas pertinentes. El PI toma la decision final — el selector recomienda, no impone.

> **BITACORA**: Registrar lentes recomendados, justificacion de cada uno, y decision final del PI.

---

### FASE 1.5: Auditoria Discursiva 12D — Escrutinio Multidimensional

| Campo | Valor |
|-------|-------|
| **Motor/Skill** | `02_Motores_Metodologicos\skill_auditoria_discursiva_12D.md` |
| **Obligatoria** | SI — Recomendada con fuerza. Omitirla empobrece brutalmente el analisis |
| **Condicion de activacion** | Siempre (puede omitirse solo bajo instruccion explicita del PI con justificacion) |
| **Input** | Corpus limpio + Codigos y categorias de Fase 1 + Contexto Local |
| **Output** | Mapa de 12 dimensiones discursivas: polifonias, estrategias retoricas, silencios y omisiones, ejes contextual y discursivo |

**Accion LLM**: Somete las transcripciones al escrutinio implacable del Eje Contextual y Discursivo en 12 dimensiones. Mapea polifonias, estrategias retoricas, los Silencios y Omisiones del corpus (que frecuentemente son mas reveladores que lo dicho), todo a la luz de la Bibliografia Local. Los hallazgos 12D enriquecen la Fase 2 con capas que la induccion pura no alcanza.

> **BITACORA**: Registrar dimensiones mas criticas, silencios detectados, y hallazgos discursivos que contradicen o enriquecen la Fase 1.

---

### FASE 2: Lente Teorico — Traduccion Teorica Radical

| Campo | Valor |
|-------|-------|
| **Motor/Skill** | `01_Lentes_Teoricos\lente_[AUTOR_SELECCIONADO].md` (1 de 20 disponibles) |
| **Obligatoria** | SI — Sin lente no hay interpretacion, solo descripcion |
| **Condicion de activacion** | Siempre. El lente fue pre-seleccionado por el usuario o recomendado en Fase 1.2 |
| **Input** | Categorias centrales de Fase 1 + Hallazgos 12D de Fase 1.5 |
| **Output** | Re-lectura teorica completa de los codigos, diagnostico estructural, patologias micro-politicas detectadas |

**Accion LLM**: Toma las Categorias Centrales y los hallazgos 12D. Olvida las restricciones de la induccion para abrazar radicalmente el determinismo o el postulado del Lente seleccionado (`01_Lentes_Teoricos\lente_[seleccionado].md`). Interroga frontalmente a los codigos de la Fase 1 utilizando **solo** las matrices de ese teorico. Como un antropologo o sociologo diagnosticarian la patologia, el comportamiento micro-politico, la violencia simbolica o la estructura de poder que subyace a estos datos? El lente no decora — disecciona.

**Lentes disponibles (20):** Bourdieu, Butler, Chomsky, Crenshaw, Dennett, Derrida, Fanon/Said, Foucault, Giddens, Gramsci, Habermas, Latour, Levi-Strauss, Margaret Mead, Pinker, Radcliffe-Brown, Ruth Benedict, Sapir-Whorf, Turner, Wittgenstein.

> **BITACORA**: Registrar lente aplicado, hallazgos teoricos principales, y donde el lente ilumino vs. donde dejo puntos ciegos.

---

### FASE 2.3: Analisis Narrativo — Temporalidad, Trama y Modelo Actancial

| Campo | Valor |
|-------|-------|
| **Motor/Skill** | `02_Motores_Metodologicos\skill_analisis_narrativo.md` |
| **Obligatoria** | NO — Opcional pero recomendada para corpus con fuerte componente narrativo |
| **Condicion de activacion** | El corpus contiene testimonios extensos, historias de vida, relatos, cronologias experienciales |
| **Input** | Corpus limpio + Categorias de Fase 1 + Hallazgos de Fase 2 |
| **Output** | Estructura narrativa: temporalidad, configuracion de trama, modelo actancial de Greimas, funciones narrativas |

**Accion LLM**: Si el corpus tiene carne narrativa — testimonios, historias de vida, relatos extendidos — esta fase extrae la arquitectura temporal y actancial que la codificacion por categorias no captura. Aplica el modelo actancial de Greimas, identifica la configuracion de trama (comedia, tragedia, romance, satira), mapea la temporalidad vivida de los participantes. La narrativa no es adorno: es estructura profunda de sentido.

> **BITACORA**: Registrar decision de activar/omitir, tipo de estructura narrativa dominante, actantes identificados.

---

### FASE 2.4: Analisis Critico del Discurso (ACD) — Poder en el Lenguaje

| Campo | Valor |
|-------|-------|
| **Motor/Skill** | `02_Motores_Metodologicos\skill_analisis_critico_discurso.md` |
| **Obligatoria** | NO — Opcional pero recomendada cuando el corpus involucra relaciones de poder explicitas |
| **Condicion de activacion** | El corpus involucra discursos institucionales, politicos, mediaticos, o relaciones de poder asimetricas |
| **Input** | Corpus limpio + Hallazgos de Fases 1, 1.5, 2 |
| **Output** | Analisis tri-dimensional Fairclough (texto, practica discursiva, practica social), ideologias identificadas, estrategias de legitimacion/Van Dijk |

**Accion LLM**: Cuando el corpus transpira relaciones de poder — discursos institucionales, narrativas hegemonicas, comunicaciones entre actores asimetricos — el ACD destripa las estrategias discursivas de dominacion, legitimacion y resistencia. Aplica el modelo tri-dimensional de Fairclough y las categorias de Van Dijk. Esta fase complementa al lente teorico (Fase 2) con un bisturi especificamente disenado para el poder inscrito en el lenguaje.

> **BITACORA**: Registrar decision de activar/omitir, estrategias discursivas dominantes, ideologias detectadas.

---

### FASE 2.5: Q-Square — Puente Cualitativo-Cuantitativo

| Campo | Valor |
|-------|-------|
| **Motor/Skill** | `02_Motores_Metodologicos\skill_protocolo_QSquare.md` |
| **Obligatoria** | SI — Ancla cuantitativa del analisis |
| **Condicion de activacion** | Siempre |
| **Input** | Todos los hallazgos previos: codigos (Fase 1), 12D (Fase 1.5), lente teorico (Fase 2), narrativo (Fase 2.3 si aplica), ACD (Fase 2.4 si aplica) |
| **Output** | Matrices de frecuencia booleana, escalas Likert de dolor doxastico, cuadros de disonancias discursivas (solo tablas Markdown crudas) |

**Accion LLM**: Congela temporalmente la narrativa textual. Transforma todos los hallazgos previos en matrices de frecuencia booleana, escalas Likert de dolor doxastico y cuadros de disonancias discursivas. Renderiza obligatoriamente **solo Tablas Markdown en crudo** — nada de prosa decorativa. Este es el momento cuantitativo del pipeline: los numeros no mienten, pero tampoco explican solos. Por eso Q-Square alimenta al Perfilador, no al revez.

> **BITACORA**: Registrar metricas clave, disonancias mas criticas, decisiones sobre escalas utilizadas.

---

### FASE 2.6: Etnometodologia — Analisis Conversacional

| Campo | Valor |
|-------|-------|
| **Motor/Skill** | `02_Motores_Metodologicos\skill_etnometodologia.md` |
| **Obligatoria** | CONDICIONAL — Solo para corpus que contengan focus groups o interacciones grupales |
| **Condicion de activacion** | El corpus incluye transcripciones de focus groups, grupos de discusion, o interacciones conversacionales entre multiples participantes |
| **Input** | Corpus limpio (especificamente transcripciones de focus groups) + Hallazgos previos |
| **Output** | Analisis conversacional Garfinkel/Sacks: turnos de habla, secuencias de adyacencia, reparaciones, construccion colaborativa de sentido, etnometodos |

**Accion LLM**: Si el corpus contiene focus groups o interacciones grupales, esta fase es imprescindible. La etnometodologia de Garfinkel y el analisis conversacional de Sacks revelan lo que los participantes hacen *con* el lenguaje en interaccion — turnos de habla, secuencias de adyacencia, reparaciones, la construccion colaborativa del sentido comun. Lo que la Grounded Theory codifica como contenido, la etnometodologia lo analiza como practica social in situ. Si no hay focus groups, esta fase no se activa.

> **BITACORA**: Registrar decision de activar/omitir, patrones conversacionales dominantes, etnometodos identificados.

---

### FASE 2.8: Perfilador Multidimensional — Arquetipos Cognitivo-Culturales

| Campo | Valor |
|-------|-------|
| **Motor/Skill** | `02_Motores_Metodologicos\skill_perfilador_multidimensional.md` |
| **Obligatoria** | SI — Destilacion final pre-narrativa |
| **Condicion de activacion** | Siempre |
| **Input** | Matrices Q-Square (Fase 2.5) + Hallazgos teoricos (Fase 2) + Todas las fases opcionales ejecutadas (2.3, 2.4, 2.6) |
| **Output** | Arquetipos cognitivo-culturales con perfiles psicograficos, triggers de toma de decision, mapas de tension identitaria |

**Accion LLM**: Ingiere los numeros de Q-Square y la estructura del lente teorico, cruzandolos con antropologia y psicografia para esculpir Arquetipos Cognitivo-Culturales precisos y sus "Triggers" de toma de decision. Cada arquetipo debe ser una criatura viva con tensiones internas, no una caricatura de segmentacion de mercado. Los hallazgos narrativos (Fase 2.3), de ACD (Fase 2.4) y etnometodologicos (Fase 2.6) enriquecen los perfiles cuando estan disponibles.

> **BITACORA**: Registrar arquetipos generados, criterios de diferenciacion, y triggers principales.

---

### FASE 3: Plantilla de Salida — Narrativa Final "Gilgamesh"

| Campo | Valor |
|-------|-------|
| **Motor/Skill** | `06_Plantillas_de_Salida\plantilla_[SELECCIONADA].md` |
| **Obligatoria** | SI — Sin salida formateada no hay entregable |
| **Condicion de activacion** | Siempre |
| **Input** | Todo el acervo acumulado: codigos, 12D, lente, Q-Square, arquetipos, narrativo/ACD/etnometodologia si aplica |
| **Output** | Documento narrativo completo en formato Markdown segun plantilla seleccionada |

**Plantillas disponibles:**
- `plantilla_cronica_etnografica.md` — Cronica inmersiva
- `plantilla_ensayo_interpretativo.md` — Ensayo academico
- `plantilla_informe_consultoria.md` — Informe de consultoria pragmatico
- `plantilla_bitacora_decisiones.md` — Bitacora de decisiones metodologicas

**Accion LLM**: En lugar de hacer un resumen generico o telegrafico, invoca la Plantilla de Salida seleccionada por el usuario. Modela estrictamente la salida tejiendo los conocimientos y datos de forma narrativa ('El Narrador Gilgamesh'). No des por sentado nada; explica las razones de los hallazgos y como los lentes destilaron esta informacion, de modo que el cliente no-especialista pueda comprender maravillosamente la complejidad estructural del informe. Si la narrativa es plana, es que el analisis fue cobarde.

> **BITACORA**: Registrar plantilla seleccionada, decisiones editoriales, secciones donde la evidencia fue mas solida vs. mas debil.

---

### FASE 3.5: Abogado del Diablo — Auditoria Red Team

| Campo | Valor |
|-------|-------|
| **Motor/Skill** | `02_Motores_Metodologicos\skill_abogado_del_diablo.md` |
| **Obligatoria** | SI — Ningun reporte sale sin pasar por el Red Team |
| **Condicion de activacion** | Siempre |
| **Input** | Draft completo generado en Fase 3 |
| **Output** | Reporte de vulnerabilidades: jerga academica ("Heredad Academica"), vaguedades estrategicas, falacias, puntos ciegos, dictamen de aprobacion/rechazo |

**Accion LLM**: Ejecuta en la sombra el motor del Abogado del Diablo. Lee el borrador de la Fase 3 con intencion destructiva. Ataca en busca de jerga academica impenetrable, vaguedades estrategicas que disfrazan falta de evidencia, falacias logicas, y puntos ciegos teoricos. Si el reporte falla la auditoria, ordena **auto-reescritura inmediata** de las secciones debiles antes de proceder. No se avanza hasta que el Red Team apruebe o el PI decida aceptar los riesgos explicitamente.

> **BITACORA**: Registrar vulnerabilidades detectadas, secciones reescritas, decision final de aprobacion.

---

### FASE 3.7: Auditoria Epistemica — Validacion de Rigor

| Campo | Valor |
|-------|-------|
| **Motor/Skill** | `04_Protocolos_Avanzados\skill_auditoria_epistemica.md` |
| **Obligatoria** | SI — Sello de calidad epistemologica |
| **Condicion de activacion** | Siempre |
| **Input** | Draft revisado post-Red Team (Fase 3.5) + Toda la trazabilidad del pipeline |
| **Output** | Dictamen de rigor epistemologico: criterios de credibilidad, transferibilidad, dependabilidad, confirmabilidad (Lincoln & Guba), recomendaciones |

**Accion LLM**: Ejecuta la auditoria epistemica sobre el draft post-Red Team. Evalua si el analisis cumple los criterios de rigor cualitativo: credibilidad, transferibilidad, dependabilidad, confirmabilidad. Verifica la trazabilidad completa desde el dato bruto hasta la interpretacion final. Si hay brechas de rigor, se documentan y se decide con el PI si corregir o aceptar con nota de limitacion.

> **BITACORA**: Registrar dictamen de rigor, criterios cumplidos/incumplidos, brechas detectadas.

---

### FASE 3.8: Triangulacion — Validacion Cruzada de Datos (Denzin)

| Campo | Valor |
|-------|-------|
| **Motor/Skill** | `04_Protocolos_Avanzados\skill_triangulacion.md` |
| **Obligatoria** | SI — Pilar de validez cualitativa |
| **Condicion de activacion** | Siempre |
| **Input** | Todos los outputs acumulados del pipeline + Fuentes de datos multiples si existen |
| **Output** | Matriz de triangulacion (de datos, de investigador, teorica, metodologica), convergencias y divergencias, indice de confianza |

**Accion LLM**: Ejecuta la triangulacion segun el modelo de Denzin. Cruza las cuatro dimensiones: triangulacion de datos (fuentes distintas), de investigador (perspectivas multiples), teorica (lentes aplicados), y metodologica (motores utilizados). El pipeline de ETHNOS, al usar multiples motores y lentes, genera triangulacion metodologica y teorica de forma intrinseca — esta fase la hace explicita y cuantificable. Las divergencias son tan valiosas como las convergencias: senalan donde la realidad resiste la simplificacion.

> **BITACORA**: Registrar tipos de triangulacion aplicados, convergencias principales, divergencias criticas.

---

### FASE 3.9: Fiabilidad Inter-codificador — Cohen's Kappa

| Campo | Valor |
|-------|-------|
| **Motor/Skill** | `04_Protocolos_Avanzados\skill_fiabilidad_intercodificador.md` |
| **Obligatoria** | CONDICIONAL — Solo cuando hay multiples codificadores |
| **Condicion de activacion** | El proyecto involucra mas de un codificador humano o la combinacion de codificacion humana + IA |
| **Input** | Codificaciones paralelas de multiples codificadores sobre los mismos segmentos |
| **Output** | Coeficiente Kappa de Cohen, porcentaje de acuerdo, tabla de discrepancias, informe de reconciliacion |

**Accion LLM**: Si el proyecto tiene multiples codificadores (incluyendo la combinacion humano + IA), calcula la fiabilidad inter-codificador usando el coeficiente Kappa de Cohen. Identifica las discrepancias sistematicas, no las aleatorias. Un Kappa < 0.60 exige reunion de reconciliacion antes de continuar. Esta fase es la garantia de que la codificacion no es el delirio interpretativo de un solo analista.

> **BITACORA**: Registrar Kappa obtenido, categorias con mayor discrepancia, decisiones de reconciliacion.

---

### FASE 4: Exportacion DOCX — Entregable Corporativo Final

| Campo | Valor |
|-------|-------|
| **Motor/Skill** | `00_Gobernanza\ethnos_docx_exporter.py` |
| **Obligatoria** | SI — Sin DOCX no hay entrega formal |
| **Condicion de activacion** | Siempre |
| **Input** | Documento Markdown final validado (post-Fases 3.5, 3.7, 3.8) |
| **Output** | Archivo `.docx` profesional en `00_Proyectos\[PROYECTO]\03_Reportes_Finales\` |

**Accion LLM / CLI**: Tras haber completado y validado la narrativa en formato Markdown, el orquestador tiene orden estricta e irrevocable de transformarlo a un entregable corporativo en Microsoft Word. Ejecuta silenciosamente:

```
python C:\Users\uned\Desktop\ETHNOS\04_Ecosistema_Cualitativo\00_Gobernanza\ethnos_docx_exporter.py [Ruta_del_archivo_Markdown]
```

El output queda depositado como `.docx` listo dentro de `03_Reportes_Finales`.

> **BITACORA**: Registrar ruta del archivo exportado, formato de plantilla usado.

---

### FASE 5: Devolucion a Participantes — Member Checking

| Campo | Valor |
|-------|-------|
| **Motor/Skill** | `05_Guias_de_Campo\guia_devolucion_participantes.md` |
| **Obligatoria** | SI — Compromiso etico ineludible |
| **Condicion de activacion** | Siempre. Es la fase de cierre etico del pipeline |
| **Input** | Reporte final exportado + Hallazgos principales del pipeline completo |
| **Output** | Documento de devolucion adaptado a participantes, protocolo de member checking, guia de sesion de devolucion |

**Accion LLM**: El pipeline no termina con el DOCX. Genera el documento de devolucion a participantes siguiendo `guia_devolucion_participantes.md`. Prepara una version accesible de los hallazgos principales (despojada de jerga academica), un protocolo de member checking para verificar interpretaciones con los propios participantes, y una guia de sesion de devolucion. La voz de los participantes tiene la ultima palabra sobre la validez de las interpretaciones. Esto no es cortesia — es obligacion etica y epistemologica.

> **BITACORA**: Registrar formato de devolucion seleccionado, adaptaciones realizadas para accesibilidad, plan de member checking.

---

## 5. Bitacora de Decisiones Metodologicas

### Protocolo Obligatorio

ETHNOS exige que despues de **cada fase mayor** del pipeline, el agente LLM solicite y registre una entrada en la Bitacora de Decisiones Metodologicas. Esta bitacora es la espina dorsal de la trazabilidad analitica y la reflexividad del investigador.

### Formato de Entrada (plantilla: `06_Plantillas_de_Salida\plantilla_bitacora_decisiones.md`)

```markdown
## Fase [NUMERO]: [NOMBRE]
- **Fecha**: [YYYY-MM-DD]
- **Decision tomada**: [Descripcion concisa]
- **Alternativas consideradas**: [Que mas se pudo hacer]
- **Justificacion**: [Por que esta opcion y no las otras]
- **Riesgos asumidos**: [Que se pierde con esta decision]
- **Implicaciones para fases posteriores**: [Como afecta al pipeline]
- **Nota reflexiva del PI**: [Espacio para la voz del investigador]
```

### Reglas de la Bitacora

1. **Despues de cada fase obligatoria**: El agente DEBE preguntar al PI si desea agregar una nota a la bitacora antes de avanzar.
2. **Despues de cada fase condicional/opcional activada o saltada**: Se registra automaticamente la decision de activar u omitir, con justificacion.
3. **En decisiones criticas intra-fase**: Cuando el agente toma una decision analitica significativa dentro de una fase (ej: fusionar dos codigos, descartar un outlier, elegir una interpretacion sobre otra), lo documenta en la bitacora sin esperar a que termine la fase.
4. **Acumulacion**: La bitacora se acumula como archivo `.md` dentro de `00_Proyectos\[PROYECTO]\04_Bitacora\bitacora_decisiones.md`.
5. **Exportacion**: La bitacora se exporta a DOCX junto con el reporte final en Fase 4, como documento adjunto.

### Por que es irrenunciable

Sin bitacora, el analisis cualitativo es una caja negra. La trazabilidad de decisiones es lo que distingue un analisis riguroso de una opinion informada. Cada decision metodologica tiene consecuencias epistemicas — la bitacora las hace visibles, auditables y criticables. El investigador que no documenta sus decisiones no puede reclamar rigor.

---

## 6. Flujo de Dependencias

```
                    [Corpus Visual?]
                          |
                     FASE -1 (opt)
                          |
                          v
                    FASE -0.5 (oblig) ---- Preprocesamiento
                          |
                     [Macro-corpus?]
                      /         \
                   SI             NO
                    |              |
               FASE 0 (cond)      |
                    \             /
                     v           v
                    FASE 1 (oblig) ---- Grounded Theory
                     |          \
                     |      [Sin lente?]
                     |           |
                     |      FASE 1.2 (opt) ---- Selector Lentes
                     |          /
                     v         v
                    FASE 1.5 (oblig) ---- Auditoria 12D
                          |
                          v
                    FASE 2 (oblig) ---- Lente Teorico
                     |    |    |
         [Narrativo?] [Poder?] [Focus?]
              |          |        |
         FASE 2.3    FASE 2.4  FASE 2.6
           (opt)      (opt)    (cond)
              \         |        /
               v        v       v
                    FASE 2.5 (oblig) ---- Q-Square
                          |
                          v
                    FASE 2.8 (oblig) ---- Perfilador
                          |
                          v
                    FASE 3 (oblig) ---- Plantilla Salida
                          |
                          v
                    FASE 3.5 (oblig) ---- Red Team
                          |
                          v
                    FASE 3.7 (oblig) ---- Auditoria Epistemica
                          |
                          v
                    FASE 3.8 (oblig) ---- Triangulacion
                          |
                     [Multi-cod?]
                          |
                    FASE 3.9 (cond) ---- Fiabilidad Kappa
                          |
                          v
                    FASE 4 (oblig) ---- Exportacion DOCX
                          |
                          v
                    FASE 5 (oblig) ---- Devolucion Participantes
```

---

## 7. Invocacion Rapida

| Comando | Efecto |
|---------|--------|
| `ETHNOS, ejecuta pipeline completo` | Ejecuta las 19 fases en secuencia, preguntando en cada punto de decision |
| `ETHNOS, ejecuta analisis etnografico complejo` | Sinonimo del anterior |
| `ETHNOS, ejecuta desde Fase [N]` | Reanuda el pipeline desde una fase especifica (requiere outputs previos) |
| `ETHNOS, ejecuta solo Fase [N]` | Ejecuta una fase aislada (el usuario provee inputs manualmente) |
| `ETHNOS, estado del pipeline` | Muestra que fases se han completado y cuales faltan |

---

## 8. Restricciones Inamovibles

1. **Ningun dato se procesa sin verificacion de consentimiento etico** (ver `guia_consentimiento_informado.md`).
2. **Toda salida elimina identificadores personales** antes de circulacion.
3. **La bitacora de decisiones se mantiene actualizada** en todo momento.
4. **El PI tiene poder de veto** sobre cualquier decision automatica del pipeline.
5. **Fases obligatorias no se saltan** salvo instruccion explicita del PI con justificacion registrada en bitacora.
6. **El Red Team (Fase 3.5) es innegociable** — ningun borrador sale sin auditoria adversarial.
7. **La devolucion a participantes (Fase 5) no es opcional** — es cierre etico del proceso investigativo.

> **Salida Final esperada**: El reporte etnografico purificado, expulsado como archivo Microsoft Word (`.docx`) profesional en `00_Proyectos\[PROYECTO]\03_Reportes_Finales\`, acompanado de la Bitacora de Decisiones y el Documento de Devolucion a Participantes.
