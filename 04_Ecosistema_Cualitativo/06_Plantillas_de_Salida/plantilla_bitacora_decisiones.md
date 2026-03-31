---
name: Plantilla de Bitácora de Decisiones Metodológicas (El Libro Negro)
description: Registro vivo de cada decisión metodológica significativa tomada durante un proyecto ETHNOS. Cadena de custodia epistémica. Exigido por la Carta Constitucional de Gobernanza.
author: ETHNOS - Inteligencia Cualitativa
---

# Bitácora de Decisiones Metodológicas (El Libro Negro)

**Misión:** Este documento es el registro forense de cada decisión que alteró el curso del análisis. No es un diario. No es un adorno de rigor. Es la cadena de custodia epistémica del proyecto. Cuando alguien pregunte "¿por qué usaron Bourdieu y no Giddens?", "¿por qué eliminaron ese código?", "¿por qué suprimieron esa sección del informe?" — la respuesta DEBE estar aquí, con fecha, autor y justificación. Si no está en la Bitácora, no existió como decisión consciente. Y una decisión inconsciente en investigación cualitativa es una negligencia.

> **Principio rector:** La reflexividad no es un lujo postmoderno. Es la diferencia entre investigación y opinión. Cada decisión que tomaste pudo haber sido otra. Este documento registra cuál tomaste, cuáles descartaste, y por qué.

## Ubicación del Archivo

```
00_Proyectos/[NOMBRE_DEL_PROYECTO]/06_Decisiones/bitacora_decisiones.md
```

Este es un **DOCUMENTO VIVO.** Se actualiza después de cada fase analítica, cada reunión de equipo, cada punto de inflexión metodológico. No se escribe al final del proyecto como reconstrucción post-hoc. Se escribe EN CALIENTE.

---

## Formato de Entrada

Cada decisión registrada sigue este esquema sin excepción:

```
### DEC-[PROYECTO]-[###]

| Campo | Contenido |
| :--- | :--- |
| **ID** | DEC-[PROYECTO]-[###] |
| **Fecha** | YYYY-MM-DD |
| **Fase del Pipeline** | [Fase -0.5: Preprocesamiento / Fase 0: Triage / Fase 1: Grounded Theory / Fase 1.5: Auditoría 12D / Fase 2: Lente Teórico / Fase 2.5: Q-Square / Fase 2.8: Perfilador / Fase 3: Exportación / Fase 3.5: Red Team] |
| **Decisión** | Declaración clara e inequívoca de lo que se decidió |
| **Alternativas Consideradas** | Qué otras opciones existían (mínimo 1 alternativa) |
| **Justificación** | Por qué se eligió esta opción. DEBE referenciar evidencia: códigos, turnos, frecuencias, criterios teóricos. "Nos pareció mejor" NO es justificación |
| **Implicaciones** | Qué abre y qué cierra esta decisión para el análisis subsiguiente |
| **Riesgo Asumido** | Qué podría salir mal con esta elección. Qué punto ciego acepta el equipo |
| **Decidido por** | PI / ETHNOS (sistema) / Consenso del equipo |
| **Estado** | VIGENTE / REVERTIDA (ver DEC-XXX) / SUPERADA (por DEC-XXX) |
```

---

## Ejemplo de Entrada

```
### DEC-BARRIO_NORTE-007

| Campo | Contenido |
| :--- | :--- |
| **ID** | DEC-BARRIO_NORTE-007 |
| **Fecha** | 2026-03-15 |
| **Fase del Pipeline** | Fase 2: Lente Teórico |
| **Decisión** | Se selecciona Bourdieu (Campos y Habitus) como lente primario y Giddens (Estructuración) como lente complementario |
| **Alternativas Consideradas** | Turner (Liminalidad) fue evaluado pero contraindicado por baja pertinencia contextual (Score 6/20). Foucault (Biopoder) tenía resonancia conceptual alta pero potencia explicativa redundante con Bourdieu para estos datos |
| **Justificación** | Los códigos C04 (acumulación desigual de contactos institucionales) y C07 (autopercepción de "no pertenecer" al espacio urbano formal) mapean directamente sobre capital social y habitus de clase. Giddens complementa iluminando la agencia táctica visible en C11 (estrategias de sobrevivencia que modifican la estructura barrial). Ver Matriz de Pertinencia completa |
| **Implicaciones** | Abre: análisis de reproducción social, capital simbólico en el territorio, disposiciones incorporadas. Cierra: análisis de rituales de paso (Turner), tecnologías de gobierno (Foucault) |
| **Riesgo Asumido** | Bourdieu tiende al determinismo estructural — podría invisibilizar las líneas de fuga creativas de los participantes. Giddens mitiga parcialmente este riesgo |
| **Decidido por** | PI, tras recomendación del Selector de Lentes |
| **Estado** | VIGENTE |
```

---

## Categorías de Decisiones que DEBEN Registrarse

No toda micro-decisión merece una entrada. Pero las siguientes son **obligatorias**:

### Decisiones de Encuadre Teórico
- Selección de lente(s) teórico(s) y justificación contra la Matriz de Pertinencia.
- Rechazo de lentes contraindicados (breve: el detalle está en el output del Selector).

### Decisiones de Codificación
- Fusión de dos o más códigos en uno (qué se fusionó, por qué, qué se perdió).
- División de un código en dos o más (qué se separó, qué ambigüedad motivó la ruptura).
- Eliminación de un código (por qué dejó de ser analíticamente productivo).
- Renombramiento o reconceptualización de una categoría (nombre viejo → nombre nuevo, razón).

### Decisiones de Motor y Pipeline
- Motor omitido y justificación (ej. "Se omitió Q-Square porque el corpus tiene menos de 5 entrevistas y la cuantificación sería espuria").
- Orden alterado del pipeline (ej. "Se ejecutó 12D antes de Grounded Theory por solicitud del PI").
- Repetición de una fase (ej. "Se repitió Grounded Theory tras incorporar 3 entrevistas adicionales").

### Decisiones sobre los Datos
- Exclusión de datos del corpus y justificación (ej. "Se excluyó entrevista_P8 porque el participante solicitó retiro del estudio").
- Inclusión de datos no previstos (ej. "Se incorporó documento de WhatsApp proporcionado espontáneamente por P3").
- Nivel de anonimización elegido y razón.

### Decisiones Interpretativas
- Disputas de interpretación dentro del equipo y cómo se resolvieron.
- Momentos donde ETHNOS y el PI discreparon y qué prevaleció.
- Reinterpretaciones: cuando un hallazgo posterior obligó a releer uno anterior.

### Decisiones de Salida
- Plantilla seleccionada para el reporte final y por qué.
- Secciones suprimidas del informe y justificación (ej. "Se suprimió el hallazgo sobre violencia doméstica por riesgo de identificación de la participante P5").
- Cambios de alcance (ej. "Se redujo el scope del informe de 'comunidad completa' a 'jefas de hogar' por saturación desigual del corpus").

### Decisiones Éticas
- Toda decisión que implique proteger, suprimir, o alterar datos por razones éticas.
- Decisiones de anonimización más allá del estándar.
- Supresión de hallazgos que podrían causar daño a participantes.

---

## Protocolo de Registro Automático (Instrucciones para ETHNOS)

ETHNOS debe **solicitar proactivamente** al Investigador Principal el registro de decisiones en los siguientes momentos del pipeline:

| Momento del Pipeline | Prompt de ETHNOS al PI |
| :--- | :--- |
| Al finalizar Preprocesamiento (Fase -0.5) | "Se completó el preprocesamiento. ¿Se excluyó algún archivo? ¿Se tomaron decisiones sobre anomalías? Registre en Bitácora." |
| Al finalizar Triage Masivo (Fase 0) | "Los macro-clústers están definidos. ¿Acepta esta partición o desea modificarla? Registre la decisión." |
| Al finalizar Grounded Theory (Fase 1) | "Los códigos y categorías emergentes están listos. ¿Hubo fusiones, eliminaciones o renombramientos durante la codificación? Registre cada uno." |
| Al finalizar Auditoría 12D (Fase 1.5) | "La auditoría discursiva está completa. ¿Alguna dimensión fue desestimada? ¿Algún silencio requiere decisión ética? Registre." |
| Al elegir Lente Teórico (Fase 2) | "OBLIGATORIO: Registre la selección del lente, las alternativas evaluadas y la justificación. Use el formato DEC-[PROYECTO]-[###]." |
| Al finalizar Q-Square (Fase 2.5) | "Las matrices cuantitativas están generadas. ¿Se descartó alguna variable? ¿Se modificó algún umbral? Registre." |
| Al finalizar Perfilador (Fase 2.8) | "Los arquetipos están construidos. ¿Se fusionaron o eliminaron perfiles? Registre las decisiones de agrupación." |
| Antes de exportar (Fase 3) | "Antes de generar el reporte final: ¿Hay hallazgos que deban suprimirse? ¿Se cambió el alcance? ¿Se eligió plantilla? Registre TODO." |
| Tras Red Team (Fase 3.5) | "El Abogado del Diablo detectó problemas. ¿Qué se corrigió y qué se mantuvo pese a la objeción? Registre cada resolución." |

> **Instrucción a los motores ETHNOS:** Al finalizar cada fase, antes de pasar a la siguiente, verificar si existen decisiones pendientes de registro. Si las hay, DETENER el pipeline y solicitar al PI que complete la Bitácora. No se avanza con decisiones sin registrar.

---

## Estados de una Decisión

| Estado | Significado |
| :--- | :--- |
| **VIGENTE** | La decisión está activa y gobierna el análisis actual |
| **REVERTIDA** | La decisión fue anulada. DEBE referenciarse la nueva decisión que la reemplaza (ej. "REVERTIDA — ver DEC-BARRIO_NORTE-012") |
| **SUPERADA** | La decisión ya no es relevante porque el análisis avanzó más allá de su alcance, pero no fue "incorrecta" en su momento |

> **Regla de oro:** Una decisión REVERTIDA nunca se borra. Se marca y se vincula a su reemplazo. La Bitácora es un registro cronológico inmutable, no un documento editable.

---

## Notas Finales

- La Bitácora se revisa íntegramente antes de la exportación final (Fase 3) como control de calidad reflexivo.
- En caso de auditoría externa o revisión por pares, la Bitácora es el primer documento que se entrega. Es la prueba de que las decisiones fueron conscientes, documentadas y justificadas.
- Si un proyecto ETHNOS no tiene Bitácora de Decisiones, su rigor metodológico es cuestionable por definición. No hay excepciones.

> **Directiva Final:** "Cada decisión que tomaste pudo haber sido otra. Este documento demuestra que lo sabías, que evaluaste las alternativas, y que elegiste con fundamento. Eso es reflexividad. Eso es rigor. Eso es lo mínimo que se le exige a quien pretende interpretar la vida de otros."
