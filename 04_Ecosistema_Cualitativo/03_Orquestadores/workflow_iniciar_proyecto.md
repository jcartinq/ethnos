---
description: Flujo de trabajo para inicializar un nuevo proyecto de consultoría/investigación y generar su arquitectura aislada.
---

# Orquestador: Iniciar Nuevo Proyecto ETHNOS

**Activación:** El usuario invoca "ETHNOS, inicia el proyecto [NOMBRE DEL PROYECTO]".

## 1. Misión
Este workflow tiene como objetivo crear un entorno de trabajo hermético ("sandbox") para cada nueva investigación de laboratorio. Al crear el entorno, ETHNOS se asegurará de que durante la fase de análisis, los modelos teóricos solo tengan acceso al contexto geográfico y cultural de ese cliente/proyecto, evitando alucinaciones o mezcla ("contaminación") con otros proyectos pasados.

## 2. Puesta en Operación (Ejecución del Agente LLM):

- **Acción LLM**: Cuando el usuario ordene iniciar un proyecto, el Sistema AI usará sus herramientas de sistema (Terminal/PowerShell) para generar la siguiente estructura de carpetas de forma autónoma dentro de `00_Proyectos\`:

   ```
   00_Proyectos\[NOMBRE_DEL_PROYECTO]\
   ├── 00_Admin\                    (documentos administrativos, contratos, consentimientos)
   ├── 01_Corpus_RAW\               (transcripciones brutas, notas de campo)
   ├── 02_Corpus_Visual\            (fotografías, mapas para análisis semiótico)
   ├── 03_Contexto_Local\           (bibliografía, demografía, contexto geográfico)
   ├── 04_Codificacion\             (salidas de codificación, libros de códigos)
   ├── 05_Analisis\                 (análisis intermedios, matrices de cruce)
   ├── 06_Decisiones\               (bitácora de decisiones, elecciones metodológicas)
   ├── 07_Reportes_Finales\         (entregables finales al cliente/academia)
   ├── 08_Devolucion\               (materiales de devolución a la comunidad)
   └── README_PROYECTO.md           (ficha técnica del proyecto, auto-generada)
   ```

- **Auto-generación de README_PROYECTO.md**: Inmediatamente después de crear la estructura de carpetas, el LLM generará automáticamente un archivo `README_PROYECTO.md` dentro de la raíz del proyecto con la siguiente ficha técnica:

   ```markdown
   # [NOMBRE DEL PROYECTO]

   ## Ficha Técnica
   - **Investigador(a) Principal (PI):** [Nombre del PI]
   - **Fecha de inicio:** [Fecha]
   - **Alcance:** [Descripción breve del alcance de la investigación]
   - **Población o unidad de análisis:** [Descripción de la población objetivo]
   - **Consideraciones éticas:** [Consentimiento informado, anonimización, comité de ética, etc.]
   - **Lente teórico elegido:** [Marco teórico o enfoque epistemológico principal]

   ## Notas
   [Espacio para observaciones iniciales del equipo investigador]
   ```

   El LLM solicitará al usuario los datos necesarios para completar la ficha. Si el usuario no proporciona algún campo, se dejará marcado como `[Pendiente]` para llenado posterior.

- **Instrucción al Usuario final**: Tras crear las carpetas y el README exitosamente, el LLM notificará al usuario:
  *¡Proyecto [NOMBRE] Creado Estructuralmente!*
  *Se han generado 9 subcarpetas según el Acta de Inicio Operativa y una ficha técnica en README_PROYECTO.md.*
  *Por favor, deposita tus transcripciones en `01_Corpus_RAW`, la bibliografía o demografía específica del cliente en `03_Contexto_Local`, y cualquier documento administrativo (contratos, consentimientos) en `00_Admin` antes de iniciar el orquestador principal de análisis.*
