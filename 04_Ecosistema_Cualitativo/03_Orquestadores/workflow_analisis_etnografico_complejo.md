---
description: Pipeline y Orquestador del Análisis Etnográfico (Desde RAW data a Descripción Densa con validación teórica).
---

# Orquestador: Análisis Etnográfico Complejo

## 1. Misión
Este workflow dirige secuencialmente a los LLMs para que analicen corpus cualitativos complejos sin perderse en resúmenes anodinos, aplicando rigurosamente los Motores (Grounded/Geertz/Fenomenología/Hermenéutica) y Lentes (Bourdieu, Giddens, Turner, Levi-Strauss).

## 2. Puesta en Operación (Entrada de Datos RAW y Contexto)
   **Usuario**: "Invoco el `workflow_analisis_etnografico_complejo`. El [Nombre del Proyecto] es el Proyecto X. El lente teórico a utilizar será [Bourdieu / Levi-Strauss / Giddens / etc.]. La salida debe usar la [Plantilla Consultoría / Ensayo Académico / Crónica]."

## 3. Fase a Fase - Ejecución Secuencial (Agente LLM):

### FASE -1: Triage Visual (Píxel a Texto)
- **Acción LLM**: Revisa si el usuario adjuntó hasta 3 mapas o fotografías (idealmente en `01_Corpus_Visual`). Si es así, ejecuta `02_Motores_Metodologicos\skill_semiotica_visual.md`.
- **Tarea**: Extrae la semiótica visual de la región (poder espacial, fracturas territoriales) usando visión artificial *solo una vez*, convirtiendo el análisis profundo en un archivo `.md`. Envía este texto a las Fases de Texto puro.

### FASE 0: Triage y Mapeo Masivo (Opcional para Macro-corpus)
- **Acción LLM**: Ejecuta `02_Motores_Metodologicos\skill_triage_masivo.md` si el volumen de datos excede las capacidades inmediatas.
- **Tarea**: Fragmenta miles de páginas en macro-clústers temáticos filtrando el ruido conversacional, preparando raciones digeribles para las siguientes fases.

### FASE 1: Motor de Inducción - GROUNDED THEORY + CONTEXTO LOCAL
- **Acción LLM**: Toma el texto bruto suministrado dentro de `00_Proyectos\[NOMBRE_DEL_PROYECTO]\01_Corpus_RAW`. Inmediatamente lee obligatoriamente los archivos de pre-requisito en `\02_Contexto_Local` (ej. Reportes geográficos o de clientes). Invoca lógicamente los parámetros de `skill_grounded_theory.md`.
- **Tarea**: Extrae primero los 10 códigos crudos (con la cita en el corpus), ponderados e influenciados por el Contexto Local. Luego, agrúpalos en "Categorías Centrales".

### FASE 1.5: Auditoría Estructural - MOTOR 12 DIMENSIONES (Opcional pero Recomendado)
- **Acción LLM**: Ejecuta `02_Motores_Metodologicos\skill_auditoria_discursiva_12D.md`.
- **Tarea**: Somete las transcripciones al escrutinio del Eje Contextual y Discursivo. Mapea polifonías, estrategias retóricas y los Silencios y Omisiones del corpus a la luz de la Bibliografía Local.

### FASE 2: Traducción Teórica - LENTE ELEGIDO
- **Acción LLM**: Toma las "Categorías Centrales" y hallazgos 12D. Olvida las restricciones de inducción para abrazar radicalmente el determinismo o el postulado del "Lente" seleccionado por el investigador de manera predeterminada (`01_Lentes_Teoricos\lente_[seleccionado].md`).
- **Tarea**: Interroga frontalmente a los códigos de la Fase 1 utilizando **solo** las matrices de ese teórico. ¿Cómo un antropólogo o un sociólogo usarían estos códigos para diagnosticar, ver la patología, o explicar este comportamiento micro-político? 

### FASE 2.5: Escalado Cuantitativo Transversal - Q-SQUARE
- **Acción LLM**: Ejecuta `02_Motores_Metodologicos\skill_protocolo_QSquare.md`.
- **Tarea**: Congela temporalmente la narrativa textual. Transforma todos los hallazgos previos en matrices de frecuencia booleana, escalas Likert de dolor doxástico y cuadros de disonancias discursivas (Renderizando obligatoriamente solo Tablas Markdown en crudo).

### FASE 2.8: Destilación Pragmática - PERFILADOR MULTIDIMENSIONAL
- **Acción LLM**: Ejecuta `02_Motores_Metodologicos\skill_perfilador_multidimensional.md`.
- **Tarea**: Ingiere los números de Q-Square y la estructura de Giddens, cruzándolos con antropología y psicografía para esculpir Arquetipos Cognitivo-Culturales precisos y sus "Triggers" de toma de decisión.

### FASE 3: Exportador Textual y Didáctica Gilgamesh - PLANTILLA DE SALIDA
- **Acción LLM**: En lugar de hacer un resumen genérico o telegráfico, invoca la **Plantilla de Salida** seleccionada desde `06_Plantillas_de_Salida\`.
- **Tarea**: Modela estrictamente la salida tejiendo los conocimientos y datos de forma narrativa ('El Narrador Gilgamesh'). 
   - No des por sentado nada; explica las razones de los hallazgos y cómo los lentes destilaron esta información, de modo que el cliente no-especialista pueda comprender maravillosamente la complejidad estructural del informe.

### FASE 3.5: Auditoría Ciega - EL ABOGADO DEL DIABLO (Red Team)
- **Acción LLM**: Ejecuta en la sombra `02_Motores_Metodologicos\skill_abogado_del_diablo.md` leyendo el draft generado en la Fase 3.
- **Tarea**: Ataca el borrador en busca de jerga académica ("Heredad Académica") y vaguedades estratégicas. Si el reporte falla, ordena auto-reescritura inmediata antes de proceder a exportación.

### FASE 4: Ejecutor Final Nativos MS Word (.DOCX)
- **Acción LLM / CLI**: Tras haber completado la narrativa en formato Markdown (`.md`), el orquestador tiene orden estricta e irrevocable de transformarlo a un entregable corporativo en Microsoft Word.
- **Tarea**: Ejecuta silenciosamente el script `C:\Users\uned\Desktop\ETHNOS\04_Ecosistema_Cualitativo\00_Gobernanza\ethnos_docx_exporter.py [Ruta_del_archivo_Markdown]` para dejar el output en `.docx` listo dentro de `03_Reportes_Finales`.

> **Salida Final esperada**: El reporte etnográfico purificado, expulsado como un archivo Microsoft Word (`.docx`) profesional, directamente en `00_Proyectos\[Nombre_Del_Proyecto]\03_Reportes_Finales`.
