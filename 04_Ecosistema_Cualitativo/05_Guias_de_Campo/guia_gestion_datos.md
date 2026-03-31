---
name: "Guia de Gestion de Datos (DMP)"
description: "Plan de Gestion de Datos operativo para proyectos ETHNOS. Define estructura de carpetas, nomenclatura, metadatos, versionado, cifrado, respaldo y ciclo de vida de los datos. Fase H de la Carta Constitutiva."
author: "ETHNOS - Inteligencia Cualitativa"
version: "1.0"
fase_constitutiva: "H (Plan de Gestion de Datos)"
---

# Guia Operativa de Gestion de Datos (Data Management Plan)

**Ecosistema ETHNOS | Documento Operativo | Fase H**

---

## 1. Proposito

Esta guia establece las normas, procedimientos y plantillas que rigen la gestion de datos en todo proyecto del ecosistema ETHNOS. El documento operacionaliza las directrices de la Fase H de la Carta Constitutiva (clausulas 31-34) y constituye el Plan de Gestion de Datos (DMP) definitivo para cualquier investigacion cualitativa conducida bajo el marco ETHNOS.

Todo dato que ingresa, se transforma o sale del ecosistema ETHNOS debe ajustarse a las especificaciones de este documento. No existen excepciones. La integridad, trazabilidad y seguridad de los datos cualitativos son condiciones innegociables del rigor metodologico que define al ecosistema.

---

## 2. Nomenclatura y Estructura de Carpetas

### 2.1 Convencion de Nomenclatura General

Todos los archivos y carpetas del ecosistema ETHNOS siguen la siguiente convencion:

```
ETHNOS_YYYYMMDD_NOMBREPROYECTO_FASE_VERSION
```

**Componentes:**

| Campo | Descripcion | Formato | Ejemplo |
|-------|-------------|---------|---------|
| ETHNOS | Prefijo constante del ecosistema | Texto fijo | ETHNOS |
| YYYYMMDD | Fecha de creacion o ultima modificacion significativa | 8 digitos numericos | 20260331 |
| NOMBREPROYECTO | Identificador corto del proyecto, sin espacios ni caracteres especiales | CamelCase o guiones_bajos | ComunidadBribri, FOCIAS_FA |
| FASE | Fase del proyecto o tipo de documento | Texto estandarizado | FaseC, Corpus, Analisis, Informe |
| VERSION | Numero de version | vX.Y | v0.1, v1.0, v2.3 |

**Ejemplos completos:**
```
ETHNOS_20260331_ComunidadBribri_Corpus_v1.0
ETHNOS_20260415_FOCIAS_FA_Analisis_v0.3
ETHNOS_20260501_MigracionCR_Informe_v2.0
ETHNOS_20260331_ComunidadBribri_Consentimiento_v1.0
```

### 2.2 Estructura de Carpetas por Proyecto

Cada proyecto genera una estructura de carpetas estandarizada al momento de su inicializacion (conforme al Workflow de Inicio de Proyecto):

```
04_Ecosistema_Cualitativo/
  00_Proyectos/
    [NOMBRE_DEL_PROYECTO]/
      01_Corpus_RAW/
        audio/
        transcripciones/
        fotografias/
        mapas/
        documentos_secundarios/
        metadatos/
      02_Contexto_Local/
        bibliografia/
        demografia/
        marcos_normativos/
        antecedentes/
      03_Reportes_Finales/
        borradores/
        versiones_aprobadas/
        anexos_metodologicos/
      04_Bitacora/
        bitacora_campo/
        bitacora_metacognitiva/
        registro_decisiones/
      05_Consentimientos/
        formularios_aprobados/
        registros_firmados/
        tabla_correspondencia/    [CIFRADO OBLIGATORIO]
      06_Analisis/
        codificacion/
        categorias/
        matrices/
        triangulacion/
      07_Instrumentos/
        guias_entrevista/
        protocolos_observacion/
        formatos_campo/
      08_Respaldos/
        respaldo_YYYYMMDD/
```

### 2.3 Reglas de Nomenclatura para Archivos Individuales

**Transcripciones:**
```
ETHNOS_[YYYYMMDD]_[PROYECTO]_TRANS_[TECNICA]_[CODIGO_PARTICIPANTE]_v[X.Y].[ext]
Ejemplo: ETHNOS_20260401_ComunidadBribri_TRANS_EP_P07_v1.0.txt
```

Donde TECNICA puede ser:
- EP = Entrevista a profundidad
- ESE = Entrevista semiestructurada
- GF = Grupo focal
- HV = Historia de vida
- OBS = Observacion
- FE = Foto-elicitacion
- RC = Recorrido comentado

**Fotografias:**
```
ETHNOS_[YYYYMMDD]_[PROYECTO]_FOTO_[SECUENCIA]_[DESCRIPCION_BREVE].[ext]
Ejemplo: ETHNOS_20260402_ComunidadBribri_FOTO_001_mercado_central.jpg
```

**Notas de campo:**
```
ETHNOS_[YYYYMMDD]_[PROYECTO]_NOTA_[TIPO]_[SECUENCIA]_v[X.Y].[ext]
Ejemplo: ETHNOS_20260401_ComunidadBribri_NOTA_CAMPO_003_v1.0.txt
```

Donde TIPO puede ser:
- CAMPO = Nota de campo
- META = Nota metacognitiva
- DECISION = Registro de decision

**Informes:**
```
ETHNOS_[YYYYMMDD]_[PROYECTO]_INFORME_[TIPO]_v[X.Y].[ext]
Ejemplo: ETHNOS_20260501_ComunidadBribri_INFORME_FINAL_v2.0.docx
```

---

## 3. Estandares de Metadatos

### 3.1 Ficha de Metadatos por Archivo

Todo archivo que ingresa al corpus debe acompanarse de una ficha de metadatos. La ficha puede estar embebida en el encabezado del documento (para archivos de texto) o como archivo separado con el sufijo `_META` (para fotografias, audios y otros formatos binarios).

```
============================================================
FICHA DE METADATOS - ECOSISTEMA ETHNOS
============================================================

IDENTIFICADOR: [Codigo segun nomenclatura]
PROYECTO: [Nombre del proyecto]
TIPO DE ARCHIVO: [Transcripcion / Fotografia / Audio / Nota / Mapa / Documento]

FECHA DE REGISTRO: [DD/MM/YYYY]
HORA DE REGISTRO: [HH:MM]
LUGAR: [Localidad, region, pais]
COORDENADAS GPS: [Si aplica y no compromete anonimato]

TECNICA EMPLEADA: [Entrevista / Grupo focal / Observacion / etc.]
PARTICIPANTES: [Codigos, nunca nombres reales]
INVESTIGADOR/FACILITADOR: [Nombre o codigo del miembro del equipo]

DURACION: [HH:MM, para audios y sesiones]
IDIOMA: [Idioma principal del registro]
CONDICIONES DEL REGISTRO: [Descripcion breve: ambiente, interrupciones, calidad tecnica]

NIVEL DE SENSIBILIDAD: [Bajo / Medio / Alto / Critico]
NIVEL DE DESIDENTIFICACION: [1: Pseudonimizado / 2: Anonimizado parcial / 3: Anonimizado completo]

FECHA DE INGRESO AL SISTEMA: [DD/MM/YYYY]
VERSION ACTUAL: [vX.Y]
RESPONSABLE DE INGRESO: [Nombre]

OBSERVACIONES: [Notas adicionales relevantes]
============================================================
```

### 3.2 Niveles de Sensibilidad

| Nivel | Descripcion | Tratamiento |
|-------|-------------|-------------|
| Bajo | Datos generales sin informacion personal identificable | Almacenamiento estandar |
| Medio | Datos con informacion indirectamente identificable | Cifrado en reposo, acceso restringido al equipo del proyecto |
| Alto | Datos con informacion directamente identificable (nombres, ubicaciones exactas) | Cifrado en reposo y en transito, acceso solo PI, tabla de correspondencia separada |
| Critico | Datos sobre violencia, persecucion, abuso, estatus migratorio | Cifrado obligatorio, acceso exclusivo PI, destruccion programada, coordinacion con Justitia |

---

## 4. Protocolo de Versionado

### 4.1 Sistema de Numeracion

ETHNOS utiliza un sistema de versionado semantico simplificado:

```
vX.Y

X = Version mayor (cambio sustantivo en el contenido)
Y = Version menor (correcciones, adiciones parciales, ajustes de formato)
```

**Reglas:**
- Todo archivo inicia en `v0.1` (borrador inicial).
- Correcciones menores incrementan Y: v0.1 -> v0.2 -> v0.3.
- La primera version aprobada por el PI se marca como `v1.0`.
- Modificaciones sustantivas posteriores a la aprobacion incrementan X: v1.0 -> v2.0.
- Nunca se sobrescribe un archivo existente. Cada version es un archivo nuevo con su numero correspondiente.

### 4.2 Registro de Versiones

Cada archivo con multiples versiones debe tener un registro de cambios, ya sea al inicio del documento o como archivo separado:

```
============================================================
REGISTRO DE VERSIONES
============================================================
ARCHIVO: [Nombre base]

| Version | Fecha      | Autor    | Descripcion del cambio                    |
|---------|------------|----------|-------------------------------------------|
| v0.1    | DD/MM/YYYY | [Nombre] | Borrador inicial                          |
| v0.2    | DD/MM/YYYY | [Nombre] | Correccion de errores de transcripcion    |
| v1.0    | DD/MM/YYYY | [PI]     | Version aprobada por el PI                |
| v2.0    | DD/MM/YYYY | [Nombre] | Incorporacion de analisis complementario  |
============================================================
```

### 4.3 Politica de Retencion de Versiones

- Todas las versiones se conservan durante la vida activa del proyecto.
- Al cierre del proyecto, se retienen: la version final aprobada (vX.0), la version inmediatamente anterior y la version original (v0.1).
- Las versiones intermedias pueden eliminarse conforme a la politica de destruccion programada, salvo indicacion contraria del PI.

---

## 5. Cifrado y Control de Acceso

### 5.1 Cifrado en Reposo

| Elemento | Cifrado Requerido | Estandar Minimo |
|----------|-------------------|-----------------|
| Tabla de correspondencia (pseudonimos-identidades) | Obligatorio | AES-256 o equivalente |
| Transcripciones con datos identificables (Nivel 3 no aplicado) | Obligatorio | AES-256 o equivalente |
| Consentimientos firmados | Obligatorio | AES-256 o equivalente |
| Corpus desidentificado | Recomendado | Cifrado de disco completo |
| Informes finales (Nivel 3 aplicado) | Opcional | Depende de la sensibilidad residual |

### 5.2 Cifrado en Transito

- Toda transferencia de archivos entre miembros del equipo debe realizarse por canales cifrados.
- No se envian transcripciones, consentimientos ni datos identificables por correo electronico no cifrado.
- Para transferencias de archivos grandes, utilizar servicios con cifrado de extremo a extremo.
- Las conexiones a repositorios de almacenamiento deben utilizar protocolos seguros (HTTPS, SFTP, SSH).

### 5.3 Control de Acceso

ETHNOS opera con un modelo de acceso basado en roles:

| Rol | Acceso a Corpus RAW | Acceso a Tabla de Correspondencia | Acceso a Informes | Acceso a Bitacora |
|-----|---------------------|----------------------------------|-------------------|-------------------|
| Investigador Principal (PI) | Completo | Completo | Completo | Completo |
| ETHNOS (sistema) | Completo (para procesamiento) | No (trabaja con datos pseudonimizados) | Completo | Completo |
| Equipo de campo | Limitado (sus propios registros) | No | Borradores | Su propia bitacora |
| Comite de etica | Solo muestras desidentificadas | No | Informes finales | Registro de decisiones eticas |
| Beneficiarios / Comunidad | No | No | Version de devolucion | No |

### 5.4 Protocolo ante Perdida o Robo de Dispositivos

1. Notificacion inmediata al PI.
2. Si el dispositivo contenia datos cifrados: evaluar riesgo residual.
3. Si el dispositivo contenia datos no cifrados: activar protocolo de brecha de seguridad.
4. Cambio inmediato de contrasenas de acceso a repositorios compartidos.
5. Notificacion al comite de etica si hay riesgo de exposicion de datos identificables.
6. Registro del incidente en bitacora con clasificacion de severidad.

---

## 6. Ciclo de Vida de los Datos

### 6.1 Fases del Ciclo de Vida

```
+-------------+     +-------------+     +-------------+
|  CREACION/  | --> | PROCESAMIENTO| --> |  ANALISIS   |
|  RECOLECCION|     | Y LIMPIEZA  |     | Y CODIFICAC.|
+-------------+     +-------------+     +-------------+
                                              |
                                              v
+-------------+     +-------------+     +-------------+
| DESTRUCCION | <-- | ARCHIVADO/  | <-- |  PUBLICACION|
| PROGRAMADA  |     | RETENCION   |     | /ENTREGA    |
+-------------+     +-------------+     +-------------+
```

### 6.2 Descripcion de cada Fase

**Fase 1: Creacion y Recoleccion**
- Registro en campo (grabacion, fotografia, notas).
- Asignacion inmediata de nomenclatura ETHNOS.
- Llenado de ficha de metadatos.
- Respaldo diario (ver seccion 7).
- Inicio de pseudonimizacion (Nivel 1).

**Fase 2: Procesamiento y Limpieza**
- Transcripcion de audios.
- Verificacion de calidad de transcripciones (audibilidad, completitud).
- Desidentificacion progresiva (Niveles 1-2).
- Eliminacion de ruido y datos no pertinentes (conforme al Motor de Triage Masivo).
- Control de calidad: cada archivo procesado se verifica contra la ficha de metadatos.

**Fase 3: Analisis y Codificacion**
- Ingreso al flujo analitico de ETHNOS (Grounded Theory, 12 Dimensiones, fenomenologia, etc.).
- Generacion de categorias, matrices y patrones.
- Toda codificacion se registra con trazabilidad: codigo -> cita -> fuente -> metadato.
- Versionado de los documentos de analisis conforme al protocolo (seccion 4).

**Fase 4: Publicacion y Entrega**
- Aplicacion de desidentificacion Nivel 3 a todos los entregables.
- Verificacion cruzada: ningun dato identificable en informes finales.
- Entrega conforme al formato y calendario acordado con el PI.
- Devolucion a comunidad (si aplica) en version adaptada.

**Fase 5: Archivado y Retencion**
- Archivado de la version final, la version anterior y la version original.
- Almacenamiento en repositorio seguro conforme a las politicas de acceso.
- Periodo de retencion definido por el PI y el comite de etica (minimo: hasta el cierre formal del proyecto; maximo: segun legislacion aplicable y acuerdos con participantes).

**Fase 6: Destruccion Programada**
- Al vencer el periodo de retencion, se destruyen:
  - Tabla de correspondencia (pseudonimos-identidades).
  - Consentimientos firmados (originales digitalizados).
  - Corpus RAW con datos identificables.
  - Versiones intermedias no retenidas.
- Metodo de destruccion: borrado seguro (multiples pasadas) para archivos digitales. Trituracion para documentos fisicos.
- Registro de destruccion: fecha, archivos destruidos, metodo, responsable.
- Notificacion al comite de etica del cumplimiento.

---

## 7. Respaldo y Recuperacion

### 7.1 Politica de Respaldo

| Tipo de Respaldo | Frecuencia | Ubicacion | Responsable |
|------------------|-----------|-----------|-------------|
| Respaldo de campo (durante F2) | Diario, al cierre de cada jornada | Dispositivo secundario cifrado + nube segura | Coordinador de campo |
| Respaldo del corpus procesado | Semanal o tras cada modificacion significativa | Repositorio institucional cifrado | ETHNOS / PI |
| Respaldo de la bitacora | Diario durante campo; semanal durante analisis | Misma ubicacion que el corpus | ETHNOS |
| Respaldo completo del proyecto | Mensual y al cierre de cada fase | Disco externo cifrado + nube segura (doble soporte) | PI |

### 7.2 Procedimiento de Respaldo Diario en Campo

1. Al cierre de cada jornada de campo, el coordinador verifica que todos los archivos generados (audios, fotos, notas) estan nombrados conforme a la nomenclatura ETHNOS.
2. Copia de archivos a dispositivo secundario cifrado (disco externo, memoria USB cifrada).
3. Si hay conectividad: carga a repositorio en nube segura.
4. Verificacion de integridad: comparar numero de archivos y tamano entre original y copia.
5. Registro en bitacora: "Respaldo diario completado. [N] archivos. Sin incidentes / Con incidentes: [descripcion]."

### 7.3 Procedimiento de Recuperacion

En caso de perdida de datos:

1. Identificar el alcance de la perdida (archivos especificos, carpeta completa, proyecto completo).
2. Localizar el respaldo mas reciente que contenga los datos perdidos.
3. Restaurar desde el respaldo verificando la integridad de los archivos.
4. Registrar el incidente en bitacora: fecha, causa de la perdida, archivos afectados, fuente de recuperacion, estado post-recuperacion.
5. Si la perdida afecta datos identificables: activar protocolo de brecha de seguridad (seccion 5.4).
6. Evaluar y reforzar las medidas preventivas para evitar recurrencia.

### 7.4 Regla 3-2-1

ETHNOS recomienda la regla 3-2-1 como estandar minimo para proyectos con datos sensibles:
- **3** copias de cada dato critico.
- **2** tipos de medio de almacenamiento diferentes (disco local + nube, o disco local + disco externo).
- **1** copia fuera del sitio (nube segura o ubicacion fisica distinta).

---

## 8. Formatos Maestros Aceptados

### 8.1 Formatos de Archivo

| Tipo de Dato | Formato Primario | Formato Secundario | Notas |
|-------------|-----------------|-------------------|-------|
| Transcripciones | .txt (UTF-8) | .docx | UTF-8 obligatorio para preservar caracteres especiales y diacriticos |
| Notas de campo | .txt (UTF-8) | .md | Formato plano preferido para maxima portabilidad |
| Fotografias | .jpg | .png | EXIF debe limpiarse antes de ingreso al corpus si contiene datos de ubicacion |
| Mapas y diagramas | .png | .svg | Vectorial preferido para diagramas que requieran escalabilidad |
| Audio | .wav | .mp3 | WAV para archivo maestro; MP3 para copias de trabajo |
| Matrices y tablas | .csv (UTF-8) | .xlsx | CSV para maxima interoperabilidad; XLSX cuando se requiera formato enriquecido |
| Informes | .docx | .pdf | PDF solo para versiones finales aprobadas (no editables) |
| Metadatos | .txt (UTF-8) | .yaml | YAML para metadatos estructurados que requieran procesamiento automatizado |

### 8.2 Codificacion de Texto

- Todos los archivos de texto deben utilizar codificacion **UTF-8** sin BOM.
- Los saltos de linea deben ser consistentes dentro de cada archivo (LF preferido).
- Los nombres de archivo no deben contener caracteres especiales mas alla de guiones bajos, guiones medios y puntos.

---

## 9. Licencias y Politicas de Comparticion

### 9.1 Principio General

El control primario de acceso y distribucion corresponde siempre al Investigador Principal (PI). ETHNOS no publica, comparte ni distribuye datos ni informes sin autorizacion explicita del PI.

### 9.2 Opciones de Licenciamiento

| Opcion | Descripcion | Cuando Aplicar |
|--------|-------------|----------------|
| Acceso abierto | Datos desidentificados disponibles para reutilizacion | Proyectos academicos con aprobacion etica y de participantes |
| Acceso restringido | Datos disponibles solo bajo solicitud y acuerdo de uso | Proyectos institucionales, datos con sensibilidad media |
| Embargo temporal | Datos no disponibles hasta una fecha determinada | Proyectos con publicacion pendiente o clausulas contractuales |
| Confidencialidad absoluta | Datos accesibles unicamente al PI y equipo autorizado | Proyectos con datos criticos, poblaciones vulnerables, riesgo de re-identificacion |

### 9.3 Acuerdos de Uso de Datos

Cuando se comparten datos con terceros (con autorizacion del PI), ETHNOS recomienda un acuerdo de uso que incluya:

- Proposito especifico del acceso.
- Prohibicion de re-identificacion.
- Prohibicion de redistribucion sin autorizacion.
- Obligacion de destruccion al concluir el uso autorizado.
- Clausula de notificacion en caso de brecha de seguridad.

---

## 10. Auditoria y Trazabilidad

### 10.1 Registro de Acceso

ETHNOS mantiene un registro de acceso para todo archivo con nivel de sensibilidad Medio o superior:

```
============================================================
REGISTRO DE ACCESO
============================================================
ARCHIVO: [Nombre]
PROYECTO: [Nombre del proyecto]

| Fecha      | Hora  | Usuario    | Accion                | Justificacion         |
|------------|-------|------------|----------------------|-----------------------|
| DD/MM/YYYY | HH:MM | [Nombre]  | Lectura / Edicion    | [Motivo breve]        |
============================================================
```

### 10.2 Auditoria de Integridad

Trimestralmente (o al cierre de cada fase del proyecto), ETHNOS recomienda una verificacion de integridad que incluya:

1. Conteo de archivos vs. inventario registrado.
2. Verificacion de nomenclatura conforme al estandar.
3. Verificacion de completitud de fichas de metadatos.
4. Estado de cifrado de archivos sensibles.
5. Estado de respaldos (fecha del ultimo respaldo, ubicacion, integridad).
6. Revision de tabla de correspondencia (acceso restringido, cifrado vigente).

---

## 11. Checklist DMP por Fase del Proyecto

### 11.1 Al Inicio del Proyecto

| Num | Accion | Estado |
|-----|--------|--------|
| 11.01 | Estructura de carpetas creada conforme a seccion 2.2 | [ ] |
| 11.02 | Nomenclatura definida y comunicada al equipo | [ ] |
| 11.03 | Nivel de sensibilidad preliminar establecido | [ ] |
| 11.04 | Politica de cifrado definida | [ ] |
| 11.05 | Roles de acceso asignados | [ ] |
| 11.06 | Politica de respaldo acordada | [ ] |
| 11.07 | Formato de consentimiento aprobado y almacenado | [ ] |
| 11.08 | Periodo de retencion definido con PI y comite de etica | [ ] |

### 11.2 Durante el Trabajo de Campo

| Num | Accion | Estado |
|-----|--------|--------|
| 11.09 | Respaldo diario ejecutado | [ ] |
| 11.10 | Nomenclatura correcta en todos los archivos nuevos | [ ] |
| 11.11 | Fichas de metadatos completadas para cada registro | [ ] |
| 11.12 | Pseudonimizacion aplicada desde la transcripcion | [ ] |
| 11.13 | EXIF limpiado en fotografias | [ ] |
| 11.14 | Control de calidad post-sesion ejecutado | [ ] |

### 11.3 Durante el Analisis

| Num | Accion | Estado |
|-----|--------|--------|
| 11.15 | Versionado correcto en documentos de analisis | [ ] |
| 11.16 | Trazabilidad verificable: codigo -> cita -> fuente | [ ] |
| 11.17 | Respaldo semanal ejecutado | [ ] |
| 11.18 | Desidentificacion Nivel 2 aplicada en borradores | [ ] |

### 11.4 Al Cierre del Proyecto

| Num | Accion | Estado |
|-----|--------|--------|
| 11.19 | Desidentificacion Nivel 3 verificada en todos los entregables | [ ] |
| 11.20 | Auditoria final de integridad ejecutada | [ ] |
| 11.21 | Respaldo completo en doble soporte realizado | [ ] |
| 11.22 | Versiones intermedias no retenidas eliminadas de forma segura | [ ] |
| 11.23 | Periodo de retencion registrado y calendarizado | [ ] |
| 11.24 | Destruccion programada calendarizada en la bitacora | [ ] |
| 11.25 | Notificacion al comite de etica sobre cierre de datos | [ ] |

---

## 12. Articulacion con Otros Documentos del Ecosistema

| Documento | Relacion |
|-----------|----------|
| Guia de Planificacion de Campo | Define la base instrumental minima que genera archivos conforme a este DMP |
| Guia de Consentimiento Informado | Los consentimientos se almacenan en 05_Consentimientos conforme a este DMP |
| Workflow de Inicio de Proyecto | Genera automaticamente la estructura de carpetas definida en seccion 2.2 |
| Motor de Triage Masivo | Opera sobre el corpus almacenado en 01_Corpus_RAW conforme a esta nomenclatura |
| Carta Constitutiva ETHNOS | Fase H (clausulas 31-34) es la directriz fundacional de esta guia |

---

## 13. Registro de Version

| Version | Fecha | Autor | Descripcion |
|---------|-------|-------|-------------|
| 1.0 | 2026-03-31 | ETHNOS | Version inicial del Plan de Gestion de Datos |

---

> **Directiva operativa:** La gestion de datos no es un acto burocratico sino una condicion del rigor cientifico. Un dato mal nombrado, no respaldado o sin metadatos es un dato en riesgo de perdida, malinterpretacion o violacion etica. ETHNOS debe mantener la disciplina de gestion de datos como habito permanente, no como tarea de cierre. Todo archivo que ingresa al ecosistema debe cumplir con este DMP desde el instante de su creacion.
