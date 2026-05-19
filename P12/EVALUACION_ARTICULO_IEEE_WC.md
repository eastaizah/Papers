# INFORME DE EVALUACIÓN INTEGRAL
## Artículo Científico: "Massive AI Model Orchestration para 6G"
### Revista Objetivo: IEEE Wireless Communications

---

**Tipo de Informe:** Evaluación Editorial y Técnica Completa  
**Nivel de Evaluación:** Revisor Senior / Editor Asociado  
**Fecha:** 2025  
**Clasificación:** CONFIDENCIAL – USO INTERNO  

---

## ÍNDICE

1. [Datos del Artículo](#1-datos-del-artículo)
2. [Evaluación Editorial](#2-evaluación-editorial-perspectiva-editor-ieee-wireless-communications)
3. [Evaluación Técnica](#3-evaluación-técnica-perspectiva-investigador-experto)
4. [Análisis de Referencias y Citas](#4-análisis-de-referencias-y-citas)
5. [Análisis de Expresiones Matemáticas (LaTeX)](#5-análisis-de-expresiones-matemáticas-latex)
6. [Análisis de Figuras y Simulaciones](#6-análisis-de-figuras-y-simulaciones)
7. [Inconsistencias Detectadas](#7-inconsistencias-detectadas)
8. [Correcciones Requeridas](#8-correcciones-requeridas)
9. [Sugerencias para Investigación Adicional](#9-sugerencias-para-investigación-adicional)
10. [Veredicto Final y Recomendación](#10-veredicto-final-y-recomendación)

---

## 1. DATOS DEL ARTÍCULO

| Campo | Valor |
|-------|-------|
| **Título** | "Massive AI Model Orchestration para 6G: Arquitectura Federada para Gestión Dinámica de Foundation Models en Capa Física mediante Cloud-Edge-Device Collaboration" |
| **Idioma** | **ESPAÑOL** (problema crítico — ver Sección 2) |
| **Revista Objetivo** | IEEE Wireless Communications |
| **Formato Declarado** | Artículo de revista / Survey |
| **Número de Líneas** | 4.013 líneas |
| **Tamaño del Archivo** | ≈ 237 KB (texto Markdown) |
| **Longitud Estimada** | >60 páginas equivalentes en formato IEEE doble columna |
| **Número de Referencias** | 118 referencias (con duplicados identificados) |
| **Número de Secciones** | VIII secciones principales + RESUMEN, REFERENCIAS |
| **Scripts de Simulación** | 8 scripts Python (scripts 01–08) |
| **Figuras Generadas** | >35 figuras PNG en directorio `simulations/` |
| **Número de Manuscrito IEEE** | **No asignado** (no enviado al sistema) |
| **Afiliaciones de Autores** | **Ausentes** |
| **Biografías de Autores** | **Ausentes** |

### Estructura del Artículo

| Sección | Título | Líneas Aprox. |
|---------|--------|---------------|
| — | RESUMEN / PALABRAS CLAVE | 1–22 |
| I | INTRODUCCIÓN | 25–226 |
| II | FUNDAMENTOS TEÓRICOS | 228–951 |
| III | ARQUITECTURA DE TRES CAPAS | 953–1493 |
| IV | MARCO DE ORQUESTACIÓN INTELIGENTE | 1494–2212 |
| V | CONSIDERACIONES ENERGÉTICAS Y HUELLA DE CARBONO | 2214–2806 |
| VI | APORTES Y CONTRIBUCIONES | 2808–3316 |
| VII | DESAFÍOS ABIERTOS Y DIRECCIONES FUTURAS | 3318–3650 |
| VIII | CONCLUSIONES | 3652–3773 |
| — | REFERENCIAS COMPLETAS | 3775–4013 |

---

## 2. EVALUACIÓN EDITORIAL (Perspectiva Editor IEEE Wireless Communications)

### 2.1 ⛔ PROBLEMA CRÍTICO BLOQUEANTE: IDIOMA DEL ARTÍCULO

**El artículo COMPLETO está redactado en ESPAÑOL.** IEEE Wireless Communications, al igual que todas las publicaciones del IEEE, exige que los manuscritos sean redactados **exclusivamente en inglés**. Esta condición está explícitamente establecida en las normas de publicación del IEEE:

> *"All manuscripts submitted to IEEE publications must be written in English."*  
> — IEEE Publication Services and Products Board Operations Manual, Section 8.1

Este es un **impedimento absoluto (show-stopper)** para la revisión editorial. El artículo sería rechazado sin revisión técnica por cualquier editor asociado de IEEE Wireless Communications. **Todos los elementos del artículo deben ser traducidos:**

- El resumen (actualmente "RESUMEN" → debe ser "ABSTRACT")
- Las palabras clave (actualmente "PALABRAS CLAVE" → deben ser "INDEX TERMS" o "KEYWORDS")
- Todos los títulos de secciones (e.g., "INTRODUCCIÓN" → "INTRODUCTION", "CONCLUSIONES" → "CONCLUSIONS")
- Todo el texto de cuerpo, incluyendo ecuaciones contextuales, leyendas de figuras y pies de tabla
- Todos los algoritmos (actualmente en pseudocódigo en español)
- Los nombres de variables y comentarios en pseudocódigo

**Antes de cualquier otra corrección, la traducción integral al inglés es condición sine qua non.**

### 2.2 Adecuación al Perfil de la Revista

IEEE Wireless Communications es una revista de impacto premium (JCR Q1, IF ≈ 11–12) orientada a artículos de *survey*, *tutorial* y de visión tecnológica. El tema central del manuscrito —orquestación de modelos de IA a gran escala en redes 6G mediante colaboración cloud-edge-device— es altamente pertinente y se alinea con líneas editoriales recientes de la revista.

**Puntos positivos de adecuación:**
- Temática en la intersección de IA/ML y comunicaciones 6G, área de máximo interés actual
- Enfoque de survey con análisis comparativo extenso
- Inclusión de análisis de sostenibilidad energética, alineado con tendencias editoriales post-2022

**Problemas de adecuación:**
- La extensión es **excesivamente larga** para IEEE Wireless Communications. Los artículos regulares se limitan a 8 páginas en doble columna (~6.000–8.000 palabras de texto); los artículos de revista/survey pueden extenderse a 12–15 páginas. Este manuscrito, en su extensión actual, equivale a 60+ páginas, lo que es completamente inapropiado incluso para un survey exhaustivo.
- No se especifica el tipo de contribución (Regular Paper, Magazine Article, Invited Survey), lo que complica la evaluación del cumplimiento de normas de formato.

### 2.3 Originalidad e Impacto Potencial

El artículo propone un marco arquitectónico denominado **Massive AI Model Orchestration (MAIMO)** para la gestión dinámica de foundation models en la capa física de 6G. La contribución declarada es de alcance amplio:

- Arquitectura de tres capas (Cloud-Edge-Device) con interfaces estandarizadas
- Mecanismos de early-exit adaptativos, cascaded model ensembles y split inference
- Algoritmos de orquestación basados en DRL con análisis de convergencia
- Análisis cuantitativo de sostenibilidad y carbon-aware scheduling

**Evaluación de originalidad:** MEDIA-ALTA en concepción, MEDIA en ejecución. Si bien la síntesis propuesta es conceptualmente valiosa, varios componentes individuales (split inference, early-exit networks, knowledge distillation para redes móviles, carbon-aware scheduling) han sido estudiados por separado en trabajos previos. La contribución principal del artículo es la **integración sistemática** de estos componentes en un framework unificado con análisis teórico formal. Esta integración es original, pero debe diferenciarse más claramente de trabajos existentes.

**Impacto potencial:** ALTO, condicionado a que se subsanen las inconsistencias técnicas identificadas en este informe. El tema es de máxima relevancia para la comunidad de 6G y AI-native networks.

### 2.4 Potencial de Citación

Dado el tema (foundation models + 6G + orquestación federada), el artículo tiene un potencial de citación elevado. Sin embargo, este potencial se verá mermado si:
1. Las inconsistencias numéricas no se corrigen (los lectores perderán confianza en los resultados)
2. Las pruebas matemáticas permanecen como "bosquejos"
3. Las referencias duplicadas y cuestionables dañan la credibilidad

Un artículo de survey en IEEE Wireless Communications sobre este tema, bien ejecutado, podría razonablemente aspirar a 200–500+ citas en 5 años.

### 2.5 Presentación Profesional

La presentación tiene graves carencias formales:

| Elemento | Estado | Requerimiento IEEE |
|----------|--------|-------------------|
| Idioma | ESPAÑOL | Inglés obligatorio |
| Afiliaciones de autores | AUSENTES | Obligatorias |
| Biografías de autores (revista) | AUSENTES | Obligatorias para revista |
| Número de manuscrito | AUSENTE | Asignado por sistema editorial |
| Formato de encabezado | No IEEE | Doble columna, Times New Roman |
| Abstract | En español | Máx. 250 palabras en inglés |
| Keywords/Index Terms | En español | Terminología IEEE Thesaurus |
| Figuras | PNG independientes | Deben integrarse al texto con captions |
| Leyendas de figuras | Sin formato IEEE | Formato "Fig. N. Caption." requerido |
| Tablas | Sin formato IEEE | Tabla numerada con título sobre la tabla |

### 2.6 Veredicto Editorial

> **RECHAZO SIN REVISIÓN TÉCNICA** en el estado actual, por incumplimiento del requisito fundamental de idioma (inglés). Una vez traducido al inglés, el artículo podría ser considerado para **revisión mayor** con condicionantes técnicas específicas detalladas en este informe.

---

## 3. EVALUACIÓN TÉCNICA (Perspectiva Investigador Experto)

### 3.1 Solidez y Reproducibilidad de Métodos

#### 3.1.1 Modelos de Simulación

Los 8 scripts de simulación (`script_01` a `script_08`) han sido revisados en detalle. Se identifica una **discrepancia fundamental** entre lo que el artículo afirma sobre su metodología experimental y lo que los scripts realmente implementan.

**El artículo afirma (línea 11, RESUMEN):**
> *"La validación experimental sobre datasets realistas (channel traces 3GPP, movilidad NYC, tráfico 6G sintético)"*

**Lo que los scripts realmente implementan (`script_01_main_comparison.py`, comentarios explícitos):**
```
LATENCY MODEL:
  latency = base_processing + queueing_delay(n_users) + Gaussian_noise

ENERGY MODEL:
  total_energy = base_energy × (n_users / 1000) × (1 + noise)

ACCURACY MODEL:
  accuracy = base_acc − SNR_drop − mobility_drop + noise
```

Estos son **modelos paramétricos sintéticos** basados en fórmulas analíticas simples con perturbación gaussiana. **No son simulaciones de deep learning ni utilizan channel traces 3GPP reales.** La afirmación de "validación experimental sobre datasets realistas" es por tanto **incorrecta o fuertemente exagerada**.

**Análisis detallado por script:**

| Script | Descripción | Tipo de Simulación | Realismo |
|--------|-------------|-------------------|---------|
| `script_01` | Comparación principal | Modelo paramétrico + Monte Carlo | MUY BAJO |
| `script_02` | LSTM handover | NumPy puro (sin PyTorch/TF) → LSTM sintética | BAJO-MEDIO |
| `script_03` | ViT channel estimation | PyTorch con canal CDL-C simplificado (4×4 MIMO) | MEDIO |
| `script_04` | Pareto optimization | NSGA-II sobre funciones analíticas | BAJO-MEDIO |
| `script_05` | Carbon scheduling | Datos estáticos de intensidad de carbono | MEDIO |
| `script_06` | Early-exit networks | Modelo analítico de accuracy-latency | MUY BAJO |
| `script_07` | Split computing | Programación dinámica sobre modelo analítico | BAJO |
| `script_08` | KPI summary | Agregación de resultados de scripts anteriores | N/A |

**Problema crítico en `script_03`:** El único script con implementación de red neuronal real utiliza un sistema MIMO 4×4 con 64 subportadoras OFDM —escala de laboratorio mínima—, mientras que el artículo habla de "Massive MIMO" (tipicamente 64–256 antenas en 6G). Esto hace que los resultados de estimación de canal no sean directamente aplicables al escenario 6G descrito en el texto.

#### 3.1.2 Reproducibilidad

**Aspectos positivos:**
- Todos los scripts fijan `numpy.random.seed(42)` para reproducibilidad
- Los scripts incluyen comentarios detallados con valores esperados y tolerancias de verificación (±5%)
- Se incluye función de verificación PASS/FAIL automática en `script_01`

**Aspectos negativos:**
- El script `script_02` implementa una LSTM en NumPy puro sin autodiferenciación, lo que resulta en un entrenamiento de red neuronal poco realista para la arquitectura bidireccional descrita en el artículo
- Los parámetros del modelo LSTM (embedding_dim=32, hidden_dim=128) son extremadamente pequeños comparados con arquitecturas reales de producción
- No se proporcionan instrucciones para instalar dependencias (no hay `requirements.txt`)

### 3.2 Robustez de Datos y Validación Experimental

#### 3.2.1 Ausencia de Datos Reales

El artículo menciona tres tipos de datos "realistas":
1. **Channel traces 3GPP**: Los scripts usan modelos CDL-C con parámetros simplificados, no trazas reales de canal
2. **Movilidad NYC**: El modelo de movilidad implementado es "Random Waypoint" genérico, sin datos de trayectorias reales de Nueva York
3. **Tráfico 6G sintético**: Efectivamente sintético, pero no validado contra estándares 3GPP o mediciones de campo

#### 3.2.2 Tamaño de las Simulaciones

- `script_01`: 100 episodios Monte Carlo, 1.000 usuarios por episodio → metodología estadísticamente válida
- `script_02`: 10.000 trazas de movilidad de 60 segundos → razonable para predicción de handover
- `script_03`: Escala MIMO 4×4 cuando el artículo describe Massive MIMO

#### 3.2.3 Comparadores (Baselines)

Se comparan cuatro estrategias: Cloud-Only, Edge-Static, Device-Local, Hybrid-Adaptive (propuesta). La elección de baselines es razonable, pero se echa en falta:
- Comparación con algoritmos de referencia estándar de la literatura (e.g., el sistema de Liu et al. [18], citado en el propio artículo)
- Un baseline de offloading tradicional sin IA

### 3.3 Corrección de Resultados y Análisis Estadístico

#### 3.3.1 Valores Numéricos en el Artículo

Los valores principales del artículo son internamente **inconsistentes** (ver Sección 7 para análisis detallado). Se identifican al menos dos conjuntos de valores de latencia contradictorios en el mismo artículo:

- **RESUMEN (línea 11)**: "46% reducción de latencia (17 ms vs. 31 ms)"
- **Sección VI (línea 3236)**: "Propuesta (Hybrid): **12 ms** (46% reducción vs. Edge-Static de 22 ms)"
- **Script `script_01`**: Edge-Static = 22 ms, Hybrid = 12 ms → 45.5% reducción ✓ consistente con sección VI

**El RESUMEN y la Sección VII usan 17 ms vs. 31 ms, mientras que la Sección V usa 12 ms vs. 22 ms y los scripts verifican 12 ms vs. 22 ms.** Esta es una inconsistencia interna grave.

#### 3.3.2 Análisis Estadístico

El análisis estadístico es limitado:
- Se reportan medias sin intervalos de confianza explícitos en el texto principal
- Los percentiles de latencia (P95, P99) relevantes para URLLC se mencionan solo marginalmente
- No se realizan pruebas de hipótesis estadísticas (t-test, Mann-Whitney) para validar la superioridad de la propuesta

### 3.4 Consistencia entre Resultados y Conclusiones

Las conclusiones del artículo declaran (línea 11):
> *"La arquitectura propuesta alcanza KPIs críticos de 6G: latencia <1 ms para URLLC"*

Sin embargo, el caso de estudio URLLC (líneas 3121, 3167) muestra:
> *"Latencia: Reducción de 95% (de 45 ms cloud a **2.1 ms** edge)"*

**2.1 ms ≠ <1 ms.** El objetivo URLLC de 1 ms del estándar 6G (3GPP TR 38.913) no se alcanza. La afirmación del RESUMEN y las Conclusiones es **falsa** según los propios datos del artículo.

Adicionalmente, el artículo afirma "reliability six-nines (99.9999%)" sin proporcionar ninguna metodología ni dato de simulación que sustente esta cifra excepcional.

### 3.5 Calidad de Redacción y Flujo Lógico

El artículo está bien estructurado en términos de secciones. El flujo lógico general es coherente: motivación → fundamentos → arquitectura → orquestación → energía → contribuciones → desafíos → conclusiones. Sin embargo:

**Problemas de coherencia narrativa:**
- La arquitectura de tres capas (Sección III) se introduce conceptualmente pero la validación experimental de sus ventajas específicas aparece solo en la Sección VI, lo que obliga al lector a mantener muchos conceptos en suspenso durante demasiadas páginas
- El artículo define "Massive AI Model Orchestration" (MAIMO) pero este acrónimo no se usa consistentemente a lo largo del texto
- La Sección VI ("Aportes y Contribuciones") repite información ya presente en la Introducción y las Conclusiones, creando redundancias innecesarias

**Anglicismos sin definición:** El texto (en español) usa extensivamente términos técnicos en inglés sin paréntesis explicativos ni primera-definición. Aunque muchos son terminología estándar del campo, algunos casos son evitables (e.g., "feedback", "scheduling", "offloading" aparecen sin traducción).

---

## 4. ANÁLISIS DE REFERENCIAS Y CITAS

### 4.1 Referencias Duplicadas (Verificadas)

Se han identificado **6 grupos de duplicados** en las 118 referencias. Esto es inaceptable en cualquier publicación académica IEEE e indica falta de rigor en la gestión bibliográfica.

| Grupo | Referencias Duplicadas | Referencia Canónica | Impacto |
|-------|----------------------|--------------------|----|
| **D1** | [3] y [32] | Bommasani et al., "On the opportunities and risks of foundation models," *arXiv:2108.07258*, 2021 | Alto — referencia clave del artículo |
| **D2** | [13] y [42] | T. O'Shea & J. Hoydis, "An introduction to deep learning for the physical layer," *IEEE Trans. Cogn. Commun. Netw.*, 2017 | Alto — referencia fundacional del área |
| **D3** | [25], [48] y [75] | Y. Mao et al., "A survey on mobile edge computing: The communication perspective," *IEEE Commun. Surveys Tuts.*, 2017 | **Muy alto** — triplicado, además con formato de nombre de revista diferente en cada instancia |
| **D4** | [55] y [94] | M. Abadi et al., "Deep learning with differential privacy," *ACM CCS*, 2016 | Medio |
| **D5** | [41] y [88] | C. Finn, P. Abbeel, S. Levine, "Model-agnostic meta-learning," *ICML*, 2017 | Medio |
| **D6** | [1] y [78] | ITU-R M.2160-0, Nov. 2023 | Alto — la referencia normativa central de 6G aparece con títulos diferentes |

**Nota sobre D3:** La referencia de Mao et al. aparece con tres variantes de nombre de revista:
- [25]: "*IEEE Commun. Surveys Tuts.*"
- [48]: "*IEEE Commun. Surv. Tutorials*"
- [75]: "*IEEE Commun. Surveys Tut.*"

El nombre oficial es *IEEE Communications Surveys & Tutorials*. Ninguna de las tres variantes es completamente correcta.

**Nota sobre D6:** La referencia [1] cita el título completo con "IMT Vision – Framework and overall objectives..." mientras [78] cita un título diferente "IMT towards 2030 and beyond". Si bien pueden corresponder a documentos ligeramente distintos de la ITU-R, el identificador M.2160-0 y fecha Nov. 2023 son idénticos, confirmando la duplicación.

**Acción requerida:** Consolidar cada grupo duplicado en una única referencia canónica y actualizar todas las citas en el texto.

### 4.2 Referencias Cuestionables o Potencialmente Incorrectas

#### 4.2.1 Referencia [69] — Autor "D. Organic" (ALTA PROBABILIDAD DE ALUCINACIÓN)

```
[69] D. Organic, M. Keutzer, and T. Darrell, "POET: Training neural networks 
     on tiny devices with integrated rematerialization and paging," 
     in Proc. ICML, virtual, Jul. 2021, pp. 6081-6092.
```

**Análisis:** El apellido "D. Organic" es sospechoso y no corresponde a ningún investigador conocido del área. El artículo POET (ICML 2021, páginas 6081-6092) existe realmente pero sus autores son **Shishir G. Patil, Paras Jain, Prabal Datta, Ion Stoica, Joseph E. Gonzalez** — ninguno con apellido "Organic". Los autores de referencia M. Keutzer y T. Darrell son investigadores reales de UC Berkeley pero **no figuran como autores del artículo POET en ICML 2021**.

Esta referencia presenta todas las características de una **referencia alucinada por un LLM**: datos parcialmente correctos (título, venue, páginas) combinados con autores inventados o incorrectos.

**Acción requerida:** Verificar la referencia en Google Scholar/DBLP y corregir los autores. La cita correcta probable es:
> S. G. Patil, P. Jain, P. Datta, I. Stoica, and J. E. Gonzalez, "POET: Training neural networks on tiny devices with integrated rematerialization and paging," in *Proc. ICML*, 2021, pp. 6081-6092.

#### 4.2.2 Referencia [71] — "B. Yan et al., Spatially sparse CNNs, CVPR 2015" (INCORRECTA)

```
[71] B. Yan et al., "Spatially sparse convolutional neural networks," 
     in Proc. IEEE CVPR, Boston, MA, USA, Jun. 2015, pp. 2510-2518.
```

**Análisis:** El paper clásico sobre redes neuronales convolucionales espacialmente dispersas (*Spatially-sparse convolutional neural networks*) publicado en 2015 fue escrito por **Benjamin Graham** de la Universidad de Warwick. No existe un paper con este título en CVPR 2015 con el autor "B. Yan". Además, CVPR 2015 tuvo lugar en Boston pero las páginas 2510-2518 corresponden a un paper diferente. Esta referencia combina elementos de papers distintos de manera incorrecta.

**Acción requerida:** Identificar el paper correcto que se desea citar. Si se refiere al trabajo de Graham:
> B. Graham, "Spatially-sparse convolutional neural networks," *arXiv:1409.6070*, 2014.

#### 4.2.3 Referencias [29] y [31] — "Early Access 2024" sin DOI verificado

```
[29] Y. Hu et al., "Large language models for next generation wireless networks," 
     IEEE Wireless Commun., early access, 2024.
[31] S. Zhang et al., "CLIP-based multimodal semantic communication," 
     IEEE Trans. Wireless Commun., early access, 2024.
```

**Análisis:** Las referencias "early access" sin DOI o fecha de acceso online son aceptables provisionalmente, pero deben actualizarse con el volumen, número y páginas definitivos antes de publicación. Al momento de la evaluación, no ha sido posible verificar que estos artículos existan en estado publicado final en las revistas indicadas. Se recomienda verificar con la herramienta de búsqueda IEEEXplore.

#### 4.2.4 Otras Observaciones sobre Referencias

- **[19]** (Singh et al., arXiv:1909.09145): Es un preprint no peer-reviewed que se cita como si fuera una publicación definitiva
- **[36]** (Kaplan et al., arXiv:2001.08361): Preprint de OpenAI, ampliamente citado; aceptable aunque no publicado en revista peer-reviewed formal
- **[66]** (Google Sustainability Report, 2022): Fuente corporativa, no académica; no es apropiada para sustento de afirmaciones técnicas cuantitativas
- La sección de referencias incluye 118 entradas para un artículo que, en su versión final publicada en IEEE Wireless Communications, debería reducirse significativamente (estándar: 30-50 para artículos de survey; hasta 80 para surveys muy exhaustivos)

### 4.3 DOIs Faltantes

IEEE requiere DOIs en todas las referencias donde estén disponibles. En el manuscrito actual:
- Los DOIs están completamente ausentes en todas las 118 referencias
- Para publicaciones en revistas IEEE (Transactions, Letters, etc.), los DOIs siempre existen y son obligatorios
- Preprints de arXiv deben citarse con su identificador arXiv en lugar de DOI

### 4.4 Cobertura del Estado del Arte

El artículo omite referencias importantes y recientes (2022-2024) en las siguientes áreas:

#### 4.4.1 Foundation Models Específicos para Redes Inalámbricas (2023-2024)

No se citan desarrollos recientes específicamente diseñados para telecomunicaciones:
- **WirelessLLM** (2024): Framework para adaptar LLMs a tareas de redes móviles
- **TelecomGPT** (2024): Modelo de lenguaje especializado en dominio de telecomunicaciones
- **LLM4CP** (2024): LLMs para predicción de canal
- **NetGPT** (2024): Modelos generativos para gestión de redes

La omisión de estos trabajos recientes es significativa, ya que constituyen el estado del arte más directo en foundation models para comunicaciones.

#### 4.4.2 Especificaciones 3GPP Rel-17/18 para IA/ML

El artículo cita 3GPP TR 38.913 [12] pero omite especificaciones más recientes y directamente relevantes:
- **3GPP TR 38.843**: "Study on AI/ML for NR air interface" (Release 18, 2023)
- **3GPP TR 23.700-80**: "Study on architecture for enablement of AI/ML-based services"
- **3GPP TS 38.331**: Extensiones para capacidades de IA de UE en señalización RRC

#### 4.4.3 ETSI ENI (Experiential Networked Intelligence)

No se menciona el grupo de especificación ETSI ENI que trabaja directamente en IA para gestión de redes, incluyendo:
- ETSI GS ENI 001-006: Arquitectura de referencia para redes cognitivas
- ETSI GS ENI 007: "Proof of Concept"

#### 4.4.4 O-RAN Alliance (Cobertura Parcial)

Las referencias [102] y [103] son de 2018 y 2021 respectivamente. Los desarrollos de O-RAN Alliance para IA/ML han avanzado significativamente:
- O-RAN.WG2.AIML-v02.00 y posteriores (2022-2024)
- O-RAN.WG1.OAD especificaciones de arquitectura abierta con xApps de IA

#### 4.4.5 Digital Twins para Redes

La Sección VII menciona digital twins como dirección futura pero omite trabajos publicados sobre digital twins para gestión de redes móviles (2022-2024), área que ya tiene publicaciones sustanciales en IEEE JSAC, TWC y Communications Magazine.

---

## 5. ANÁLISIS DE EXPRESIONES MATEMÁTICAS (LaTeX)

### 5.1 Corrección Formal de Expresiones Matemáticas

En general, la notación matemática del artículo es consistente y correcta. Sin embargo, se identifican los siguientes problemas:

#### 5.1.1 Inconsistencias de Notación

**Problema 1:** La función objetivo principal (líneas 113-117) usa $L_{\text{lat}}$ para latencia pero en otras secciones se usa $\tau_{\text{total}}$ para el mismo concepto. Se recomienda unificar la notación en todo el artículo.

**Problema 2:** El Teorema 2 aparece definido en tres instancias diferentes en el artículo (líneas 927, 2124, 2873) con nombres y contenidos distintos:
- Línea 927: "Teorema 2 (Bound de Complejidad de Muestra para Fine-tuning)"
- Línea 2124: "Teorema 2 (Convergencia de DQN)"
- Línea 2873: "Teorema 2 (Estabilidad de Política RL)"

Esta reutilización del mismo número de teorema para tres resultados distintos es un error grave de numeración matemática.

**Problema 3:** La notación de conjuntos no es consistente. En algunas ecuaciones se usa $\mathcal{M}$ para el conjunto de modelos y en otras se usa $\{M_1, ..., M_K\}$. Similarmente, $\mathcal{N}$ se usa tanto para el conjunto de nodos de red como para la distribución normal gaussiana en partes del texto.

#### 5.1.2 Análisis del Cálculo de Energía (Sección V)

El cálculo de energía en la línea 2395 es:
$$E_{\text{total}}^{\text{hybrid}} = 0.25 \times 16.6 + 0.5 \times 30.8 + 0.25 \times 25.4 \approx 25.1 \text{ Wh}$$

**Verificación:** $0.25 \times 16.6 = 4.15$; $0.5 \times 30.8 = 15.4$; $0.25 \times 25.4 = 6.35$; suma = **25.9 Wh**, **no 25.1 Wh** como afirma el artículo. La diferencia es ≈3%, posiblemente por redondeo intermedio no documentado.

#### 5.1.3 Análisis del Teorema 1 (Existencia de Frontera Pareto)

```
Teorema 1 (Existencia de Frontera Pareto): ...
Demostración (bosquejo): El espacio de decisión es finito... 
```

**Problema:** La demostración está explícitamente etiquetada como "bosquejo" (*sketch*). Para una publicación en revista IEEE, las demostraciones de teoremas deben ser completas o bien remitir formalmente a una prueba en un apéndice o en una referencia anterior. Un "bosquejo" sin demostración rigurosa no es apropiado para ser presentado como "Teorema".

Adicionalmente, la afirmación "la frontera Pareto es convexa por la linealidad de las funciones objetivo" es incorrecta en general. La frontera de Pareto es convexa solo cuando las funciones objetivo son cóncavas (o convexas, dependiendo del sentido de optimización). La linealidad en las variables de decisión no garantiza convexidad de la frontera Pareto cuando el espacio de decisión tiene estructura combinatoria.

#### 5.1.4 Análisis del Teorema 2/DQN (línea 2124)

```
Demostración (Sketch): La convergencia de Q-learning tabular a Q* está bien establecida [60]. 
La extensión a DQN requiere manejar aproximación de función...
```

**Problema:** La convergencia de DQN (con redes neuronales) al Q-óptimo es un resultado conocido pero **no trivial**. La referencia [60] (Mnih et al., *Nature*, 2015) demuestra empíricamente el rendimiento superior de DQN pero **no prueba convergencia teórica**. Los resultados teóricos de convergencia de DQN con aproximación de función requieren condiciones restrictivas que no son trivialmente satisfechas en sistemas no-lineales como las redes neuronales. La demostración presentada es incompleta.

#### 5.1.5 NP-Hardness (Teorema 3, línea 2887)

```
Teorema 3 (NP-Hardness): El problema de asignación óptima es NP-hard 
mediante reducción desde el problema de bin-packing multi-dimensional.
```

**Problema:** La reducción se afirma pero **no se construye formalmente**. Una prueba de NP-hardness requiere:
1. Definir formalmente el problema de decisión
2. Mostrar que el problema de decisión está en NP (verificabilidad en tiempo polinomial)
3. Construir una reducción polinomial desde un problema NP-hard conocido
4. Demostrar que la reducción preserva las instancias YES/NO

Nada de esto se presenta en el artículo. Adicionalmente, el texto es inconsistente: en la Sección I (línea 512) se afirma reducción desde "Multiple Knapsack Problem" pero el Teorema 3 (línea 2887) afirma reducción desde "bin-packing multi-dimensional". Son dos reducciones distintas y ninguna se completa formalmente.

#### 5.1.6 Teorema 2 — Estabilidad de Política RL (línea 2873)

La demostración de convergencia del algoritmo Policy Gradient no aparece en el artículo. Se presenta el teorema y el gradiente de la función de valor, pero la demostración de convergencia hacia $\pi^*$ con probabilidad 1 (una afirmación muy fuerte) requiere un análisis de Lyapunov o martingala que no se proporciona.

#### 5.1.7 Correcciones de LaTeX Recomendadas

| Ubicación | Expresión actual | Problema | Corrección sugerida |
|-----------|-----------------|----------|-------------------|
| Línea ~2395 | `E_{\text{total}}^{\text{hybrid}} \approx 25.1` | Resultado incorrecto (25.9 Wh) | Recalcular o documentar redondeos |
| Líneas ~1534-1540 | Ecuaciones LSTM bidireccional | Usan $\overrightarrow{\mathbf{h}}_t$ y $\overleftarrow{\mathbf{h}}_t$ pero la dimensión concatenada $\mathbf{h}_t^{\text{bi}}$ no se define explícitamente | Añadir: $\mathbf{h}_t^{\text{bi}} = [\overrightarrow{\mathbf{h}}_t; \overleftarrow{\mathbf{h}}_t] \in \mathbb{R}^{2d_h}$ |
| Varias | Mezcla de `\mathcal{N}` para nodos y distribución normal | Notación ambigua | Usar $\mathcal{V}$ para vértices/nodos de red |
| Línea ~114 | Función de utilidad multi-objetivo | Los pesos $\alpha_i$ no se definen como pertenecientes al simplex | Añadir restricción $\sum_i \alpha_i = 1, \alpha_i \geq 0$ |

---

## 6. ANÁLISIS DE FIGURAS Y SIMULACIONES

### 6.1 Consistencia entre Scripts y Valores del Artículo

#### 6.1.1 Script 01 — Comparación Principal

Los scripts generan 4 figuras principales:
- `fig1_baseline_comparison.png`: Comparación de las 4 estrategias
- `fig2_scalability_users.png`: Latencia vs. número de usuarios
- `fig3_pareto_frontier.png`: Frontera Pareto 2D
- `fig4_sensitivity_analysis.png`: Análisis de sensibilidad

**Valores esperados en los scripts vs. valores en el artículo:**

| Métrica | Script (esperado) | Artículo (Sec. V) | Artículo (Resumen) | Estado |
|---------|-------------------|------------------|--------------------|--------|
| Latencia Cloud-Only | 78 ms | 78 ms | — | ✅ Consistente |
| Latencia Edge-Static | 22 ms | 22 ms | 31 ms | ❌ **Inconsistente** |
| Latencia Hybrid | 12 ms | 12 ms | 17 ms | ❌ **Inconsistente** |
| Accuracy Hybrid | 0.89 | 0.89 | 0.89 | ✅ Consistente |
| Energía Cloud-Only | 45 kWh | 45 kWh | — | ✅ Consistente |
| Energía Hybrid | 23 kWh | 23 kWh | 23 kWh | ✅ Consistente |
| SLA Violations Hybrid | 4% | 4% | 4% | ✅ Consistente |

#### 6.1.2 Script 05 — Carbon-Aware Scheduling

Los cálculos de carbono son consistentes internamente. El script verifica:
- $E_\text{cloud}$ = 25.4 Wh por inferencia GPT-3 ✅ (consistente con Sección V)
- Noruega: ≈0.61 gCO₂eq ✅ 
- China: ≈14.1 gCO₂eq ✅

### 6.2 Figuras Faltantes o Mal Referenciadas

El artículo hace referencia textual a figuras que no están formalmente incorporadas al texto con numeración IEEE estándar. El formato correcto es "Fig. 1.", "Fig. 2.", etc., con leyendas explicativas bajo cada figura.

Se identifican los siguientes problemas:
1. Las figuras se generan en el directorio `simulations/` pero **no están integradas en el documento Markdown del artículo**
2. Las referencias a figuras en el texto son descriptivas ("como se muestra en la siguiente figura") en lugar de numéricas ("as shown in Fig. 3")
3. "Figura VI-1" se menciona textualmente en la Sección VI sin numeración estándar IEEE

### 6.3 Descripción de Figuras Requeridas

A continuación se describen detalladamente las figuras que deben incorporarse en el artículo con sus títulos, numeración y contenido preciso para su generación definitiva en formato IEEE.

---

#### FIGURA 1: Arquitectura del Sistema de Tres Capas

**Número IEEE:** Fig. 1  
**Título propuesto:** "Proposed three-layer Massive AI Model Orchestration (MAIMO) architecture for 6G networks, showing cloud, edge, and device intelligence layers with foundation model size hierarchy and inter-layer communication interfaces."

**Descripción para generación:** La figura debe ser un diagrama arquitectónico vertical con tres capas claramente diferenciadas mediante colores distintos (recomendado: azul oscuro para cloud, azul claro para edge, verde para device). La **capa cloud** (parte superior) debe mostrar servidores de datacenter con el texto "Foundation Models: 100M–1000B parameters" y representar modelos Transformer completos con múltiples bloques de atención. La **capa edge** (parte media) debe representar estaciones base MEC (Multi-access Edge Computing) gNB con indicación "Specialized Models: 10M–100M parameters" y símbolos de antenas 5G/6G. La **capa device** (parte inferior) debe representar smartphones, dispositivos IoT y drones con "Compressed Models: <10M parameters" y etiquetas de técnicas de compresión (INT8, pruning, distillation). Las interfaces entre capas deben mostrar flechas bidireccionales etiquetadas con: (1) "Model distillation / KD" entre Cloud→Edge, (2) "Split inference / LoRA adapters" entre Edge→Device, y (3) "Gradient aggregation (FL)" en sentido ascendente. En la parte derecha de cada capa, incluir un cuadro con KPIs: Cloud (latencia 50–200 ms, PUE 1.3–1.6), Edge (10–50 ms, PUE 1.8–2.2), Device (<5 ms, batería 15 Wh). El fondo debe incluir ondas de radio estilizadas para indicar el entorno inalámbrico 6G.

---

#### FIGURA 2: Frontera Pareto 3D Latencia-Accuracy-Energía

**Número IEEE:** Fig. 2  
**Título propuesto:** "3D Pareto frontier in the latency-accuracy-energy space for the four orchestration strategies. The Hybrid-Adaptive strategy (red star) achieves near-Pareto-optimal performance, outperforming all baseline strategies simultaneously."

**Descripción para generación:** La figura es un gráfico 3D con tres ejes: eje X = Latencia (ms, escala 0–100), eje Y = Accuracy (F1-score, escala 0.6–1.0), eje Z = Energía (kWh/1000 usuarios, escala 15–50). Se deben plotear cuatro marcadores con distintos símbolos y colores: (1) Cloud-Only: círculo azul en (78 ms, 0.95, 45 kWh); (2) Edge-Static: triángulo naranja en (22 ms, 0.82, 28 kWh); (3) Device-Local: cuadrado verde en (8 ms, 0.68, 18 kWh); (4) Hybrid-Adaptive: estrella roja en (12 ms, 0.89, 23 kWh). La superficie de Pareto debe representarse como una malla semitransparente que envuelve los puntos no-dominados. El punto Hybrid-Adaptive debe estar anotado con una flecha indicando "Proposed: Pareto-near-optimal". Incluir leyenda con los cuatro marcadores. La orientación del eje Y debe ser creciente hacia atrás (mayor accuracy = mejor) mientras latencia y energía son ejes que crecen hacia afuera (menor = mejor), de modo que el punto "ideal" esté en la esquina inferior-izquierda-trasera. Tamaño recomendado: 8×6 pulgadas, con vista de elevación 25° y azimut 45°.

---

#### FIGURA 3: Arquitectura LSTM Bidireccional para Predicción de Handover

**Número IEEE:** Fig. 3  
**Título propuesto:** "Bidirectional LSTM architecture for proactive handover prediction in 6G mobile networks, enabling model pre-loading with prediction accuracy >85% at a 5-second horizon."

**Descripción para generación:** La figura es un diagrama de flujo de la arquitectura de red neuronal, dispuesto horizontalmente. En el extremo izquierdo, el vector de entrada debe mostrar los componentes de la secuencia temporal: RSRP mediciones de $N_{BS}$ celdas, velocidad del UE, dirección de movimiento y métricas de QoS. Una flecha apunta a un bloque "Embedding Layer (Dense, ReLU, dim=32)". A continuación, el bloque central muestra la arquitectura LSTM bidireccional: dos filas de celdas LSTM (fila superior con flechas de izquierda a derecha para $\overrightarrow{LSTM}$, fila inferior con flechas de derecha a izquierda para $\overleftarrow{LSTM}$) con la nomenclatura $\overrightarrow{\mathbf{h}}_t$ y $\overleftarrow{\mathbf{h}}_t$. Sobre las celdas, un bloque "Temporal Attention" que combina ambas representaciones y produce $\mathbf{h}_t^{att}$ mediante pesos de atención $\alpha_t$ ilustrados como una barra de calor (heatmap) sobre la secuencia temporal. A la derecha, múltiples cabezas de predicción paralelas etiquetadas $\Delta t = 1s$, $\Delta t = 2s$, $\Delta t = 5s$, $\Delta t = 10s$, cada una con una capa Softmax que produce distribuciones de probabilidad sobre las $N_{BS}$ celdas candidatas. Debajo del diagrama, un pequeño gráfico de barras horizontales mostrando la precisión por horizonte: 95% (1s), 92% (2s), 87% (5s), 74% (10s). Color scheme: azul para capas LSTM forward, naranja para backward, verde para atención, morado para cabezas de predicción.

---

#### FIGURA 4: Comparativa de KPIs — Mejoras de la Propuesta vs. Baselines

**Número IEEE:** Fig. 4  
**Título propuesto:** "KPI improvement summary of the Hybrid-Adaptive MAIMO architecture versus best baseline (Edge-Static), across latency, accuracy, energy consumption, and SLA violation rate metrics."

**Descripción para generación:** La figura consiste en un panel de 4 gráficos de barras dispuestos en una cuadrícula 2×2. Cada subgráfico compara la propuesta (barra roja) contra Edge-Static (barra azul) y, donde aplica, Cloud-Only (barra gris punteada). **Subgráfico (a) — Latencia:** Barras verticales con valores: Cloud-Only=78 ms, Edge-Static=22 ms, Hybrid=12 ms. Línea de referencia discontinua a 20 ms (umbral eMBB). Leyenda con flecha y "46% reduction". **Subgráfico (b) — Accuracy (F1-score):** Cloud-Only=0.95, Edge-Static=0.82, Device-Local=0.68, Hybrid=0.89. Eje Y: 0.5–1.0. **Subgráfico (c) — Energía (kWh/1000 usuarios/hora):** Cloud-Only=45, Edge-Static=28, Device-Local=18, Hybrid=23. Flecha indicando "18% reduction vs. Edge-Static". **Subgráfico (d) — Violaciones de SLA (%):** Cloud-Only=12%, Edge-Static=18%, Device-Local=35%, Hybrid=4%. Barra roja para Hybrid claramente menor. Título de cada subgráfico con el KPI correspondiente. Fuente mínima: 10pt para etiquetas de ejes. El conjunto debe caber en el ancho de una columna doble IEEE (~17 cm).

---

#### FIGURA 5: Análisis de Escalabilidad — Latencia vs. Número de Usuarios

**Número IEEE:** Fig. 5  
**Título propuesto:** "Latency scalability analysis for the four orchestration strategies as a function of concurrent mobile users (10–2000). The Hybrid-Adaptive strategy maintains sub-20 ms latency up to 1500 concurrent users, providing 3× higher capacity than Edge-Static at the 20 ms threshold."

**Descripción para generación:** Gráfico de líneas con eje X = número de usuarios concurrentes (escala logarítmica 10–2000) y eje Y = latencia media (ms, escala 0–100). Cuatro curvas: Cloud-Only (azul, círculos), Edge-Static (naranja, triángulos), Device-Local (verde, cuadrados), Hybrid-Adaptive (rojo, estrellas). Línea discontinua horizontal a 20 ms (umbral de latencia eMBB). Anotación vertical indicando que Edge-Static supera el umbral a ~500 usuarios mientras Hybrid lo supera a ~1500 usuarios, con texto "3× capacity advantage". Región sombreada entre 1500 y 2000 usuarios indicando "SLA critical zone". Error bars representando ±1 desviación estándar de los 100 episodios Monte Carlo. Leyenda en la esquina superior izquierda. El script `script_01` ya genera `fig2_scalability_users.png`; adaptar al formato IEEE estándar con dimensiones 8.6×5.5 cm (una columna).

---

#### FIGURA 6: Análisis de Reducción de Carbono por Estrategia y Región

**Número IEEE:** Fig. 6  
**Título propuesto:** "Carbon footprint analysis of AI model inference orchestration strategies across geographic regions with varying carbon intensity, demonstrating up to 89% carbon reduction with carbon-aware scheduling."

**Descripción para generación:** La figura tiene dos partes. **Parte (a) — Barra de intensidad de carbono regional:** Gráfico de barras horizontales ordenadas de menor a mayor intensidad, con valores: Islandia (12), Noruega (24), Francia (57), California (215), China (555), India (708) gCO₂eq/kWh. Colores: degradado de verde (limpio) a rojo (sucio). **Parte (b) — Reducción de carbono apilada:** Gráfico de barras verticales agrupadas para tres escenarios: (1) Baseline (CA): 25.4 Wh × 215 gCO₂/kWh = 5.46 gCO₂eq; (2) Geographic shifting (Noruega): 0.61 gCO₂eq (89% reducción); (3) Temporal shifting dentro de CA: 3.6 gCO₂eq (34% reducción). Incluir línea de referencia con el objetivo "Net-Zero 2030" de la ITU a 10 gCO₂eq/hora/usuario. Colores: naranja para baseline, azul claro para geographic, verde para temporal. Leyenda clara. Valor objetivo de 34-89% de reducción resaltado con texto anotado. El script `script_05` genera las figuras base; combinar `fig5_carbon_geographic.png` y `fig5_carbon_reduction.png` en un panel dual.

---

### 6.4 Observaciones sobre Figuras Ya Generadas

Se han analizado las 35+ figuras generadas en `simulations/`. Observaciones:

| Figura | Contenido | Calidad | Problema identificado |
|--------|-----------|---------|----------------------|
| `fig1_baseline_comparison.png` | Comparación 4 estrategias | Adecuado | Falta formato IEEE (fuentes, DPI, captioning) |
| `fig3_pareto_frontier.png` | Frontera Pareto 2D | Adecuado | Solo 2D; se necesita versión 3D (Fig. 2 propuesta arriba) |
| `fig4_pareto_3d.png` | Pareto 3D (latencia-accuracy-energía) | Bueno | Verificar que los valores coincidan con la Sección V |
| `fig8_kpi_improvements.png` | Mejoras de KPI | Bueno | Verificar consistencia con valores del texto |
| `fig_training_curves.png` | Curvas de entrenamiento LSTM | Adecuado | Reportar hiperparámetros utilizados |

---

## 7. INCONSISTENCIAS DETECTADAS

### 7.1 Inconsistencia Crítica: Latencia URLLC

**Afirmación en RESUMEN (línea 11):**
> "La arquitectura propuesta alcanza KPIs críticos de 6G: **latencia <1 ms para URLLC**"

**Dato del caso de estudio URLLC (líneas 3121, 3167):**
> "Latencia: Reducción de 95% (de 45 ms cloud a **2.1 ms** edge)"
> "URLLC Teleoperation | Latencia E2E | 45 ms | **2.1 ms** | 21×"

**2.1 ms > 1 ms.** El sistema propuesto logra 2.1 ms end-to-end para el caso URLLC, lo que es una mejora impresionante (21×) pero **no cumple el requisito de <1 ms** establecido por 3GPP TR 38.913 para URLLC avanzado (cirugía remota, control industrial táctico). Esta inconsistencia invalida una de las afirmaciones principales del artículo.

**Resolución sugerida:** Modificar la afirmación del RESUMEN para reflejar el logro real: "the proposed architecture achieves **2.1 ms E2E latency for URLLC** scenarios, a 21× improvement over cloud-only approaches" y discutir que el requisito de <1 ms requiere técnicas adicionales (in-device processing, split inference más agresivo).

### 7.2 Inconsistencia Grave: Valores de Latencia del Baseline

**RESUMEN y Sección VII (líneas 11, 3693):**
> "46% reducción de latencia (**17 ms** vs. **31 ms**)"

**Sección V y scripts `script_01`:**
> "Propuesta (Hybrid): **12 ms** (46% reducción vs. Edge-Static de **22 ms**)"

Los scripts verifican: Edge-Static = 22 ms, Hybrid = 12 ms → reducción = (22-12)/22 = **45.5% ≈ 46%** ✓

La reducción porcentual es internamente consistente con los valores 12/22. Los valores 17/31 del resumen son **incorrectos** y pueden ser fruto de una revisión anterior del artículo que no se propagó uniformemente.

### 7.3 Inconsistencia Grave: Metodología de Validación Experimental

**Afirmación en artículo:**
> "Validación experimental sobre datasets realistas (channel traces 3GPP, movilidad NYC, tráfico 6G sintético)"

**Realidad de los scripts:**
> "latency = base_processing + queueing_delay(n_users) + Gaussian_noise" (comentario explícito en `script_01`)
> "accuracy = base_acc − SNR_drop − mobility_drop + noise" (comentario explícito en `script_01`)

Los scripts usan **modelos paramétricos analíticos** con ruido gaussiano, no simulaciones de deep learning sobre datasets reales. La única excepción parcial es `script_03` (PyTorch), pero usa un canal CDL-C simplificado (4×4 MIMO) y no channel traces reales de 3GPP.

**Resolución sugerida:** Cambiar la descripción metodológica para ser honesta: "we evaluate our framework via a parametric system-level simulation calibrated against 3GPP UMa path-loss models and random waypoint mobility traces" sin afirmar el uso de "datasets realistas" que no se emplean.

### 7.4 Inconsistencia en Escala de Energía (Factor 2000×)

**Sección V, cálculo por inferencia (línea 2386):**
> $E_{\text{total}}^{\text{cloud}} \approx 25.4 \text{ Wh}$ por inferencia de modelo GPT-3 scale

**Script `script_01`, resultados de simulación:**
> Cloud-Only = **45 kWh** por 1000 usuarios/hora

**Análisis de consistencia:**
- 45 kWh / 1000 usuarios = 0.045 kWh = **45 Wh por usuario por hora**
- Asumiendo ~1 inferencia cada 3.6 segundos por usuario (1000 inferencias/hora): 45 Wh / 1000 inferencias = **0.045 Wh = 45 mWh por inferencia**
- El artículo calcula 25.4 Wh por inferencia de GPT-3

**25.4 Wh ≠ 0.045 Wh. Discrepancia de ~560×.** Esta inconsistencia sugiere que los 45 kWh por 1000 usuarios/hora y los 25.4 Wh por inferencia corresponden a modelos de escala completamente diferentes, pero el artículo no hace esta distinción explícita. Los 25.4 Wh corresponden a una inferencia de un modelo GPT-3 completo (175B parámetros), mientras que los 45 kWh de la simulación corresponden a un modelo de escala razonable para edge/cloud en la simulación paramétrica. Esta distinción debe clarificarse.

### 7.5 Inconsistencia en Claim de Rango de Reducción de Carbono

**Afirmación:** "scheduling carbon-aware que reducen emisiones **34-89%**"

El rango 34-89% es extremadamente amplio (factor 2.6×). El artículo deriva estos valores de dos escenarios:
- **34%:** Shifting de California a Noruega con scheduling temporal (reducción de 215 a ~143 gCO₂/kWh efectivo)
- **89%:** Shifting de California a Noruega (de 215 a 24 gCO₂/kWh)

Sin embargo, mezcla dos estrategias distintas (geográfica vs. temporal) bajo el mismo término "carbon-aware scheduling", lo que es confuso. El rango debería separarse: "geographic shifting reduces carbon by up to 89%; temporal scheduling by 34%".

### 7.6 Inconsistencia: Claim de Reliability Six-Nines

**Afirmación en RESUMEN:**
> "reliability six-nines (99.9999%)"

No existe ninguna tabla, figura, ecuación ni simulación en el artículo que sustente este valor de reliability. Los scripts de simulación no reportan reliability. Esta afirmación parece insertada sin respaldo cuantitativo y debe eliminarse o sustentarse con datos.

### 7.7 Inconsistencia Aritmética: Cálculo de E_hybrid

**Cálculo en línea 2395:**
$$E_{\text{total}}^{\text{hybrid}} = 0.25 \times 16.6 + 0.5 \times 30.8 + 0.25 \times 25.4 \approx 25.1 \text{ Wh}$$

**Verificación independiente:**
- $0.25 \times 16.6 = 4.150$
- $0.5 \times 30.8 = 15.400$
- $0.25 \times 25.4 = 6.350$
- **Suma = 25.900 Wh**, no 25.1 Wh

La diferencia es de 0.8 Wh (≈3%). El artículo usa "≈" pero la diferencia es mayor a la esperada por redondeo de los dos dígitos significativos mostrados. Debe recalcularse explícitamente.

---

## 8. CORRECCIONES REQUERIDAS

### 8.1 Correcciones Críticas (Bloquean Publicación)

| ID | Sección | Descripción | Impacto |
|----|---------|-------------|---------|
| **C1** | Todo el artículo | **Traducción integral al inglés** — incluye título, abstract, keywords, secciones, texto, figuras, tablas, algoritmos y pseudocódigo | Bloqueante |
| **C2** | RESUMEN/Conclusiones | Corregir afirmación "<1 ms para URLLC": el sistema logra 2.1 ms, no <1 ms | Científico crítico |
| **C3** | Todo el artículo | Resolver inconsistencia de valores de latencia: RESUMEN dice 17/31 ms, Sección V dice 12/22 ms. Unificar con valores verificados por scripts | Científico crítico |
| **C4** | Ref. [69] | Verificar y corregir autores del paper POET-ICML2021 (eliminar "D. Organic") | Integridad académica |
| **C5** | Ref. [71] | Verificar y corregir paper "Spatially sparse CNNs" — autor y venue incorrectos | Integridad académica |
| **C6** | Sección V | Clarificar inconsistencia de escala de energía (25.4 Wh/inferencia vs. 45 kWh/1000 usuarios) — explicitar modelos de escala distintos | Científico crítico |
| **C7** | Teorema 1, 2, 3 | Completar demostraciones o convertir "Teoremas" en "Proposiciones/Conjeturas" con demostración parcial; resolver triple numeración del "Teorema 2" | Rigor matemático |

### 8.2 Correcciones Mayores (Requeridas para Aceptación)

| ID | Sección | Descripción |
|----|---------|-------------|
| **M1** | Referencias | Eliminar 6 grupos de referencias duplicadas: D1-D6 (ver Sección 4.1) |
| **M2** | Todo | Añadir DOIs a todas las referencias con publicación verificada |
| **M3** | Metodología | Corregir descripción de validación experimental: especificar que se usan modelos paramétricos, no datasets reales de 3GPP |
| **M4** | Intro/Conclusiones | Eliminar afirmación de "reliability six-nines" o sustentarla con datos |
| **M5** | Sección V | Corregir cálculo aritmético de $E_{\text{total}}^{\text{hybrid}}$ (resultado correcto: 25.9 Wh) |
| **M6** | Sección V | Separar y clarificar los dos tipos de carbon scheduling (geográfico 89% vs. temporal 34%) |
| **M7** | Todo | Reducir extensión del artículo: de ~60 páginas a máx. 15 para IEEE Wireless Communications (survey) |
| **M8** | Todo | Unificar notación matemática: resolver conflictos de $\mathcal{N}$, $L$, $\tau$ entre secciones |
| **M9** | Todo | Añadir afiliaciones de autores, biografías y número de manuscrito IEEE |
| **M10** | Sección V | Corregir afirmación de convexidad de frontera Pareto en Teorema 1 |

### 8.3 Correcciones Menores

| ID | Sección | Descripción |
|----|---------|-------------|
| **m1** | Sección III-IV | Definir explícitamente $\mathbf{h}_t^{\text{bi}} = [\overrightarrow{\mathbf{h}}_t; \overleftarrow{\mathbf{h}}_t]$ en arquitectura LSTM |
| **m2** | Sección I | Definir la dimensión concatenada del estado del sistema $\mathcal{S}$ formalmente |
| **m3** | Función objetivo | Añadir restricción de simplex para pesos $\alpha_i$ en la función de utilidad multi-objetivo |
| **m4** | Sección VI | Eliminar o consolidar la Sección VI ("Aportes y Contribuciones") que en gran parte repite la Introducción y las Conclusiones |
| **m5** | Referencias | Actualizar refs. [29] y [31] con volumen/número/páginas definitivos si ya están publicadas |
| **m6** | Algoritmos | Traducir pseudocódigo (variables, comentarios) al inglés junto con el texto |
| **m7** | Figuras | Integrar todas las figuras en el documento con numeración IEEE estándar "Fig. N." y captions en inglés |
| **m8** | Sección II | Definir explícitamente la distinción entre "foundation model" y "large language model" en el contexto PHY de 6G |
| **m9** | Sección V | Documentar los pesos de mezcla (0.25, 0.5, 0.25) del hybrid energy model con justificación explícita |
| **m10** | Palabras clave | Revisar términos contra IEEE Thesaurus para asegurar terminología estándar; "six-nines" no es término normalizado IEEE |

---

## 9. SUGERENCIAS PARA INVESTIGACIÓN ADICIONAL

### 9.1 Estado del Arte a Cubrir

Para posicionar adecuadamente el trabajo, se recomienda explorar y citar las siguientes líneas de investigación activas (2022-2024):

#### 9.1.1 Foundation Models Específicos para Redes Inalámbricas

La literatura reciente incluye trabajos específicamente orientados a adaptar LLMs para telecomunicaciones que el artículo debería conocer y referenciar:

- **WirelessLLM / TelecomGPT / LLM4CP**: Modelos de lenguaje o de canal para predicción y optimización de redes móviles, publicados en IEEE Communications Magazine, JSAC y Trans. Wireless Commun. 2023-2024
- **Foundation models para beam management**: Uso de modelos preentrenados para selección de beams en mmWave/sub-THz sin reentrenamiento específico por celda
- **Channel Transformers**: Arquitecturas Transformer aplicadas a estimación de canal masivo MIMO con benchmarks en datasets CDL completos de 3GPP

#### 9.1.2 Especificaciones de Estándares Relevantes

El artículo debería integrar el estado actual de la normalización de IA en redes móviles:

- **3GPP TR 38.843** (Release 18): "Study on Artificial Intelligence (AI)/Machine Learning (ML) for NR Air Interface" — define casos de uso, métricas de evaluación y arquitectura de referencia para IA en la interfaz radio 6G
- **3GPP TR 23.700-80** y TS 23.288: Arquitectura de red core para servicios habilitados por IA/ML
- **ETSI GS ENI series**: Arquitectura de referencia para redes cognitivas con IA, especialmente relevante para la capa de orquestación propuesta
- **O-RAN Alliance WG2 AI/ML** (versiones 2022-2024): Especificaciones actualizadas de workflows de IA/ML en O-RAN, near-RT RIC y xApps

#### 9.1.3 Temas de Investigación con Alto Potencial

Las siguientes áreas emergentes se relacionan directamente con la propuesta y merecen mayor desarrollo en el artículo:

**a) Semantic Communications para 6G:**
El artículo menciona "semantic communications" superficialmente. La integración profunda de foundation models con semantic coding (e.g., trabajos de Qin, Bourtsoulatze, Deniz Gündüz) representa una oportunidad de diferenciación significativa para el framework propuesto.

**b) Digital Twins para Orquestación de IA:**
El artículo propone digital twins como "trabajo futuro" pero en 2023-2024 ya existen múltiples implementaciones reportadas. Incorporar la comparación con estos sistemas fortalecería la sección de validación.

**c) In-Context Learning para Adaptación Sin Reentrenamiento:**
Una limitación del artículo es que la adaptación cross-domain requiere fine-tuning. El uso de in-context learning (ICL) y prompt engineering podría eliminar este overhead para ciertos escenarios de PHY-layer, y este aspecto no se discute.

**d) Privacidad y Seguridad en Split Inference Distribuida:**
Las implicaciones de privacidad del split inference (i.e., qué información semántica se expone al nodo edge) merecen análisis más formal, especialmente con referencia al GDPR y a los requisitos de privacidad de aplicaciones médicas (cirugía remota, mencionada en el artículo).

**e) Escalado a Bandas sub-THz y Canales con No-Estacionariedad:**
La validación actual usa canales CDL-C en bandas sub-6 GHz. Para 6G, las bandas mmWave (26-60 GHz) y sub-THz (90-300 GHz) tienen características fundamentalmente distintas (bloqueo severo, clustering espacial) que afectarían los modelos de latencia y energía del framework.

**f) Hardware AI Dedicado para Inferencia en Edge/Device:**
El artículo asume hardware genérico (GPU, CPU). El análisis de ASICs de inferencia de IA (NVIDIA Jetson, Qualcomm AI100, Apple Neural Engine) cambiaría significativamente los modelos de energía y latencia, especialmente para la capa device.

### 9.2 Extensiones Metodológicas

Para fortalecer la validación experimental:

1. **Simulación ns-O-RAN**: Usar el simulador ns-O-RAN (basado en ns-3) para validar el framework en un entorno de simulación con stack protocolar 3GPP completo
2. **Datasets Públicos**: Utilizar datasets públicos verificados como los del proyecto DeepMIMO, los channel traces de la ITU-R IMT-2020 evaluation o el dataset de movilidad NYC TAXI para sustentar las afirmaciones sobre "datos realistas"
3. **Implementación en Testbed**: Una validación en testbed de laboratorio (e.g., OpenAirInterface + USRP + GPU edge) elevaría sustancialmente la credibilidad de los resultados

---

## 10. VEREDICTO FINAL Y RECOMENDACIÓN

### 10.1 Resumen Ejecutivo de Evaluación

| Categoría | Puntuación (1-5) | Comentario |
|-----------|-----------------|-----------|
| **Relevancia temática** | 5/5 | Tema de máxima actualidad; perfectamente alineado con IEEE WC |
| **Originalidad conceptual** | 4/5 | Framework integrador valioso; componentes individuales previos |
| **Rigor matemático** | 2/5 | Teoremas sin demostración completa; inconsistencias de notación |
| **Calidad experimental** | 2/5 | Modelos paramétricos, no simulación realista; inconsistencias numéricas |
| **Gestión bibliográfica** | 1/5 | 6 grupos de duplicados; 2 referencias incorrectas; sin DOIs |
| **Presentación/formato** | 1/5 | Idioma incorrecto; sin afiliaciones; excesivamente largo |
| **Consistencia interna** | 2/5 | Múltiples contradicciones entre secciones y entre texto y scripts |
| **Contribución científica** | 3/5 | Aportación real pero no suficientemente demostrada |

### 10.2 Decisión de Revisión

**DECISIÓN:** ⛔ **RECHAZO CON INVITACIÓN A REENVÍO MAYOR**

*(Equivalent IEEE decision: "Major Revision" or "Reject and Resubmit")*

El artículo aborda un tema de alta relevancia para la comunidad y contiene ideas arquitectónicas genuinamente valiosas. Sin embargo, en su estado actual presenta impedimentos fundamentales que van más allá de lo corregible mediante una revisión menor:

1. **Idioma (bloqueante absoluto):** El artículo entero debe ser re-escrito en inglés
2. **Inconsistencias numéricas graves** que socavan la credibilidad de los resultados
3. **Afirmaciones no sustentadas** (<1 ms URLLC, six-nines reliability)
4. **Referencias incorrectas/alucinadas** que comprometen la integridad académica
5. **Validación experimental insuficiente** (modelos paramétricos presentados como "datasets realistas")

### 10.3 Condiciones para Resubmisión

Para considerar el manuscrito en una revisión posterior, **todas las correcciones críticas (C1–C7)** de la Sección 8.1 deben ser resueltas, junto con un mínimo de **8 de las 10 correcciones mayores (M1–M10)** de la Sección 8.2. Específicamente:

**Condiciones sine qua non:**
- [ ] Traducción completa al inglés (C1)
- [ ] Corrección de afirmaciones falsas sobre latencia URLLC (C2) y reliability (M4)
- [ ] Unificación de todos los valores numéricos (latencia 17/31 ms → 12/22 ms) (C3)
- [ ] Corrección/eliminación de referencias alucinadas [69] y [71] (C4, C5)
- [ ] Resolución de inconsistencia de escala energética (C6)
- [ ] Completar o reformular demostraciones de Teoremas (C7)
- [ ] Eliminar duplicados de referencias (M1)
- [ ] Descripción honesta de la metodología de simulación (M3)
- [ ] Reducir extensión a máx. 15 páginas IEEE para survey (M7)

### 10.4 Potencial del Artículo Revisado

Si el artículo se revisa exhaustivamente incorporando las correcciones señaladas, especialmente si se enriquece la validación experimental con simulaciones más realistas (ns-O-RAN, DeepMIMO dataset) y se completan las demostraciones matemáticas, el manuscrito resultante tendría un **alto potencial de aceptación en IEEE Wireless Communications** y un **impacto significativo** en la comunidad de AI-native 6G.

Los autores han demostrado un dominio conceptual amplio del campo y la visión arquitectónica propuesta es coherente y técnicamente plausible. Con el rigor científico y la presentación formal adecuados, este trabajo puede convertirse en una referencia importante en la literatura de orquestación de IA para redes 6G.

---

## ANEXO A: TABLA RESUMEN DE ERRORES CRÍTICOS

| # | Tipo | Ubicación | Descripción | Severidad |
|---|------|-----------|-------------|-----------|
| 1 | Idioma | Todo | Artículo en español (IEEE requiere inglés) | ⛔ Crítico |
| 2 | Factual | Resumen, Conclusiones | "<1 ms URLLC" vs. 2.1 ms real | ⛔ Crítico |
| 3 | Numérico | Resumen vs. Sección V | 17/31 ms vs. 12/22 ms | 🔴 Grave |
| 4 | Metodológico | Resumen, Sec. I | "datasets realistas" vs. modelos paramétricos | 🔴 Grave |
| 5 | Bibliográfico | Ref. [69] | Autor "D. Organic" (alucinado) | 🔴 Grave |
| 6 | Bibliográfico | Ref. [71] | Autor "B. Yan" y venue incorrectos | 🔴 Grave |
| 7 | Bibliográfico | [3]=[32], [13]=[42], [25]=[48]=[75], [55]=[94], [41]=[88], [1]≈[78] | 6 grupos de referencias duplicadas | 🔴 Grave |
| 8 | Matemático | Sec. V | $E_{\text{hybrid}}$ = 25.9 Wh (calculado) ≠ 25.1 Wh (artículo) | 🟡 Menor |
| 9 | Energía | Sec. V vs. scripts | 25.4 Wh/inferencia vs. 45 mWh efectivo en simulación | 🔴 Grave |
| 10 | Sin sustento | Resumen | "reliability six-nines" sin datos de respaldo | 🟠 Mayor |
| 11 | Matemático | Teoremas 1-3 | Demostraciones como "bosquejo" o ausentes | 🟠 Mayor |
| 12 | Numeración | Todo | "Teorema 2" aparece con tres contenidos distintos | 🟠 Mayor |
| 13 | Formato | Todo | Sin afiliaciones, biografías, DOIs | 🟠 Mayor |
| 14 | Extensión | Todo | ~60 páginas vs. máx. 15 para IEEE WC survey | 🟠 Mayor |

---

## ANEXO B: MAPA DE DUPLICADOS EN REFERENCIAS

```
[3]  ═══════════════════ [32]   (Bommasani et al., arXiv:2108.07258)
[13] ═══════════════════ [42]   (O'Shea & Hoydis, IEEE TCCsN, 2017)
[25] ═══════════════ [48]═[75]  (Mao et al., IEEE Comm. Surveys, 2017)
[55] ═══════════════════ [94]   (Abadi et al., ACM CCS, 2016)
[41] ═══════════════════ [88]   (Finn, Abbeel & Levine, ICML, 2017)
[1]  ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈ [78]   (ITU-R M.2160-0, Nov. 2023)
```

---

*Fin del Informe de Evaluación*

---
**Evaluación preparada como ejercicio académico de revisión científica.**  
**Revisor:** Evaluación Integral Automatizada  
**Basado en análisis de:** Manuscript file `Massive_AI_Model_Orchestration_6G.md` (4013 líneas, 8 scripts de simulación Python)
