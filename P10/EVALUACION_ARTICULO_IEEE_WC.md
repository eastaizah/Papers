# INFORME DE EVALUACIÓN ACADÉMICA

## "Predicción de Tráfico Basada en LSTM para Gestión Proactiva de Recursos en Redes 5G"

**Revista objetivo:** IEEE Wireless Communications (Q1)
**Evaluador:** Agente especializado en edición académica y en IA/Telecomunicaciones
**Fecha de evaluación:** Mayo 2026
**Idioma del informe:** Español

---

## RESUMEN EJECUTIVO

El artículo presenta una arquitectura LSTM con mecanismo de atención de Bahdanau y procesamiento multi-resolución para predicción de tráfico en redes 5G, integrada con un framework de gestión proactiva de recursos. A pesar de la solidez técnica general y la ambición del trabajo, el manuscrito presenta **deficiencias críticas** que impiden su aceptación en el estado actual, siendo la más grave que el artículo está redactado íntegramente en español, lo cual es un requisito de rechazo inmediato para IEEE Wireless Communications, que solo acepta manuscritos en inglés. Adicionalmente, se identifican inconsistencias significativas entre el artículo y los scripts de simulación, ecuaciones sin formato LaTeX adecuado, y aspectos de novedad que requieren mayor justificación frente al estado del arte citado. Se recomienda **revisión mayor** antes de una nueva sumisión.

---

## I. EVALUACIÓN DESDE LA PERSPECTIVA DEL EDITOR DE LA REVISTA

### I.1 Idoneidad para IEEE Wireless Communications

IEEE Wireless Communications es una revista de alto impacto (Q1, IF ≈ 12) orientada a artículos de revisión y originales sobre tecnologías de comunicaciones inalámbricas emergentes, con énfasis en aplicaciones prácticas para redes 5G y más allá. El tema del artículo —predicción de tráfico con LSTM para gestión proactiva de recursos en 5G— está directamente alineado con los temas de interés de la revista.

**Adecuación temática:** ✅ Alta  
**Idioma:** ❌ RECHAZO INMEDIATO — El artículo está escrito en español. IEEE Wireless Communications requiere manuscritos en inglés.

Esta deficiencia es bloqueante y debe corregirse como primer paso antes de cualquier otra revisión.

### I.2 Impacto, Originalidad y Potencial de Citación

**Impacto potencial:** El artículo propone un framework integral que combina predicción LSTM avanzada con gestión proactiva de recursos, lo cual es relevante para la comunidad 5G/6G. Los resultados cuantitativos (reducción de 40.9% en tasa de bloqueo, 31.2% en latencia) son atractivos para operadores y la comunidad investigadora.

**Originalidad:** La combinación específica de procesamiento multi-resolución con atención de Bahdanau y su integración en un pipeline completo de gestión proactiva es novedosa en su conjunto. Sin embargo, la novedad de los componentes individuales debe justificarse mejor frente a trabajos previos, especialmente la referencia [9] (Huang et al., "Mobile Traffic Prediction Using LSTM with Attention Mechanism"), que ya combinó LSTM con atención para tráfico móvil. El artículo afirma que estos autores se limitan a "arquitecturas básicas sin mecanismos de atención", pero el propio título de [9] indica lo contrario. Esta contradicción debe resolverse.

**Potencial de citación:** Alto, dado el interés creciente en Zero Touch Network Management (ZTN) y la gestión autónoma de redes 5G. Sin embargo, el potencial se reduce si la novedad no se justifica adecuadamente frente a [7] (Zhang et al., que ya propone asignación proactiva de recursos basada en datos).

**Presentación profesional:** El artículo es técnicamente denso y bien estructurado, pero la redacción en español limita inmediatamente su audiencia internacional.

---

## II. EVALUACIÓN DESDE LA PERSPECTIVA DEL REVISOR EXPERTO

### II.1 Solidez y Reproducibilidad de los Métodos

**Arquitectura propuesta — Inconsistencia crítica:**

La arquitectura de cinco capas descrita en la Sección IV.E (con BiLSTM multi-resolución + encoder-decoder con atención de Bahdanau, 4.2M parámetros) **no está implementada como una clase unificada** en los scripts de simulación. Los archivos `models.py` implementan `MultiResolutionLSTM` y `AttentionLSTM` como clases separadas. Los modelos guardados en `results/` (checkpoints) corresponden a `BaseLSTM`, `FeedforwardNN` y `AttentionLSTM`, pero **no** a la arquitectura de 5 capas completa descrita. Esto significa que los resultados reportados en las Tablas I–III no necesariamente corresponden a la arquitectura descrita en el artículo. Esta inconsistencia compromete gravemente la reproducibilidad.

**Corrección requerida:** El artículo debe aclarar si el modelo evaluado en las tablas es `AttentionLSTM` (encoder-decoder con atención, sin la capa multi-resolución de BiLSTM paralelas) o la arquitectura de 5 capas completa. Si es la segunda, debe proporcionarse el código correspondiente y verificarse que los resultados numéricos son consistentes.

### II.2 Inconsistencias entre el Artículo y los Scripts de Simulación

Se identifican las siguientes inconsistencias concretas entre el manuscrito y el código fuente:

#### Inconsistencia 1: Dataset Sintético 5G (Crítica)

| Parámetro | Artículo (Sección III.C) | `generate_datasets.py` |
|-----------|--------------------------|------------------------|
| Granularidad | 5 min | 1 min (`LOOKBACK_5G = 60` para 1 h) |
| Duración | 3 meses | 2 semanas |
| Número de celdas | 50 celdas | 20 celdas |

Estas tres discrepancias simultáneas sugieren que el dataset descrito en el artículo y el dataset generado por el código son sustancialmente diferentes.

#### Inconsistencia 2: Dataset Shanghai Telecom

| Parámetro | Artículo (Sección III.C) | `generate_datasets.py` |
|-----------|--------------------------|------------------------|
| Duración | 4 meses | 6 meses (según docstring) |

#### Inconsistencia 3: Paciencia del Early Stopping

| Fuente | Valor |
|--------|-------|
| Artículo (Sección VII.A) | paciencia = 40 épocas |
| `train.py` (docstring) | paciencia = 20 épocas |

#### Inconsistencia 4: Método de Cuantificación de Incertidumbre

El artículo describe el Algoritmo 2 (Sección VI.B) como basado en "intervalos de confianza conformales" (conformal prediction). Sin embargo, `predict.py` implementa **Monte Carlo Dropout** (MC Dropout con 30 pases hacia adelante). Conformal prediction y MC Dropout son metodologías fundamentalmente distintas con garantías estadísticas diferentes. Debe usarse un método consistente y justificado teóricamente en el artículo.

#### Inconsistencia 5: Referencia para el Dataset Sintético

La Sección III.C cita [29] (3GPP TS 23.288) como fuente del dataset sintético 5G. Sin embargo, 3GPP TS 23.288 es un documento de estándares sobre arquitectura de servicios de análisis de datos para 5GS, no una descripción de dataset. El dataset es generado internamente por `generate_datasets.py`, por lo que la cita es incorrecta. La referencia apropiada debería ser al proceso de generación estocástica descrito en el propio artículo, complementada con citas a modelos de tráfico 3GPP relevantes.

### II.3 Análisis de Ecuaciones Matemáticas y Formato LaTeX

**Problema grave detectado:** La extracción del texto del archivo DOCX revela que múltiples ecuaciones y expresiones matemáticas tienen **variables ausentes** o representadas como espacios en blanco. Por ejemplo:

- Sección II.A: "donde , , , y " (todas las variables son espacios vacíos)
- Sección II.B: "donde  es la función sigmoide,  es el producto de Hadamard"  
- Sección III.A: "con hasta  dispositivos/km²"
- Sección IV.B: "donde  es el vector de contexto"

Esto indica que las ecuaciones están en formato Word (Equation Editor de Microsoft Word u OfficeMath) y **no en LaTeX**, lo cual es un requisito explícito de IEEE para la sumisión. Todas las ecuaciones deben convertirse a formato LaTeX puro en el archivo .tex de sumisión.

**Corrección requerida:** Convertir todas las expresiones matemáticas del formato Word Equation al formato LaTeX estándar IEEE. A continuación se indican las ecuaciones clave que deben revisarse:

- Ecuación de estado oculto de RNN (Sección II.A): debe ser $h_t = f(W_h h_{t-1} + W_x x_t + b)$
- Ecuaciones LSTM completas (1)–(9) (Sección II.B): compuertas de olvido, entrada, candidato y salida
- Ecuación de gradiente BPTT (Sección II.A): producto telescópico $\prod_{k=t}^{T}$
- Modelo de tráfico compuesto (Ec. 15) (Sección III.A): $X(t) = T(t) + S(t) + C(t) + I(t) + \epsilon(t)$
- Función de pérdida Huber (Sección II.D)
- Ecuaciones de atención de Bahdanau (23)–(26)
- Formulación del problema de optimización robusto (Ec. 32)

### II.4 Análisis de las Figuras

El artículo referencia 8 figuras (Figs. 1–8). A continuación se evalúa cada una:

**Figura 1 (fig1_traffic_prediction):** Descripción clara en el texto. El archivo existe en `figures/fig1_traffic_prediction.pdf/.png`. ✅

**Figura 2 (fig2_rmse_horizon):** Curvas de RMSE vs horizonte. Descripción adecuada. El archivo existe. ✅

**Figura 3 (fig3_convergence):** Curvas de convergencia de entrenamiento/validación. El archivo existe. ✅

**Figura 4 (fig4_daily_pattern):** Perfiles diarios por tipo de servicio 5G. El archivo existe. ✅

**Figura 5 (fig5_proactive_reactive):** Comparación temporal reactivo vs proactivo. El archivo existe. ✅

**Figura 6 (fig6_resource_utilization):** Histograma de utilización de PRBs. El archivo existe, pero en la descripción textual del artículo (Sección VII.F) se mencionan valores estadísticos de las distribuciones (media, desviación estándar, percentiles) que **no se especifican numéricamente** en el texto principal de la sección de resultados, solo en la leyenda de la figura. Estos valores deben incorporarse en el cuerpo del texto.

**Figura 7 (fig7_radar):** Diagrama de radar multi-dimensional. El archivo existe. ✅

**Figura 8 (fig8_attention_weights):** Mapa de calor de pesos de atención. El archivo existe. ✅

**Figura faltante — Diagrama de Arquitectura (CRÍTICO):**

El artículo describe una arquitectura de cinco capas funcionales (Sección IV.E) pero **no incluye ninguna figura que ilustre la arquitectura completa del modelo propuesto**. Esta omisión es inaceptable para una publicación en revista IEEE. La ausencia de un diagrama arquitectural es una de las deficiencias más graves del artículo desde la perspectiva de la presentación.

**Corrección requerida — Figura 0 (nueva):**

> **Figura 0. Arquitectura completa del modelo LSTM multi-resolución con atención de Bahdanau propuesto.**
>
> Se debe incorporar una figura de arquitectura completa titulada: **"Fig. 0. Arquitectura de cinco capas del modelo LSTM propuesto para predicción de tráfico 5G"** (o renumerada como Fig. 1 desplazando las actuales). La figura debe presentarse como un diagrama de flujo vertical (top-to-bottom) o de izquierda a derecha, con los siguientes elementos en orden:
>
> **Capa 1 – Embedding Contextual:** Un bloque rectangular etiquetado "Capa 1: Embedding" que recibe el vector de entrada aumentado $x'_t$ compuesto por las variables de tráfico de celdas vecinas, la codificación cíclica de la hora del día (seno/coseno con dimensión $d_h=16$), la codificación del día de la semana ($d_w=8$) y el indicador binario de festivo. Las operaciones de codificación cíclica $\sin(2\pi h/24)$ y $\cos(2\pi h/24)$ se muestran como nodos de transformación.
>
> **Capa 2 – Procesamiento Multi-Resolución Paralelo:** Tres bloques paralelos etiquetados "Rama 1 (resolución fina, factor=1)", "Rama 2 (resolución media, factor=2)" y "Rama 3 (resolución gruesa, factor=4)", cada uno conteniendo un BiLSTM de 2 capas con 128 unidades (→256 unidades bidireccionales). Las ramas reciben el mismo input $x'_t$ pero con diferentes niveles de promediado temporal. Cada rama produce un vector de estado $\mathbf{r}_k \in \mathbb{R}^{256}$.
>
> **Capa 3 – Fusión con Atención de Resolución:** Un bloque de "Atención sobre Resoluciones" que recibe los tres vectores $\mathbf{r}_1, \mathbf{r}_2, \mathbf{r}_3$ y calcula pesos $\beta_k = \text{softmax}(W_\beta [\mathbf{r}_1, \mathbf{r}_2, \mathbf{r}_3])$ para producir el vector fusionado $\tilde{\mathbf{r}} = \sum_k \beta_k \mathbf{r}_k$, seguido de proyección lineal con BatchNorm y ReLU.
>
> **Capa 4 – Encoder-Decoder con Atención Temporal de Bahdanau:** Dos sub-bloques: (a) "Encoder LSTM (2 capas, 256 unidades)" que procesa la secuencia de entrada de $T=96$ pasos y produce $T$ estados $\{h_t^{enc}\}_{t=1}^{T}$; (b) "Decoder LSTM (2 capas, 256 unidades)" que genera predicciones paso a paso, con el mecanismo de "Atención de Bahdanau" representado como un módulo separado que calcula el vector de contexto $c_\tau$ a partir de una combinación convexa de los estados del encoder, con flechas que representan los pesos de atención $\alpha_{t,\tau}$.
>
> **Capa 5 – Salida Multi-Horizonte:** Un bloque "FC + Linear" que produce $\hat{y}(t+1), \ldots, \hat{y}(t+\tau)$ para horizontes de 15 min a 1 h, con una rama paralela etiquetada "FC + Linear (varianza $\sigma^2$)" para la estimación de incertidumbre mediante MC Dropout.
>
> Las conexiones residuales con LayerNorm se representan mediante flechas de bypass con el símbolo "+" y la etiqueta "LayerNorm". El número de parámetros de cada capa se indica en un cuadro anotado: Capa 1: ~10K, Capa 2: ~795K, Capa 3: ~5K, Capa 4: ~3.4M, Capa 5: ~5K, Total: ~4.2M. La figura debe seguir el estilo IEEE (fuente Times New Roman, líneas negras sobre fondo blanco, sin colores de fondo en los bloques, solo bordes).

Esta figura debe ser citada en la Sección IV.E inmediatamente después de describir la arquitectura completa.

### II.5 Análisis de Tablas y Resultados Numéricos

**Tabla I – Comparación de Precisión:**
Los resultados del LSTM propuesto (RMSE=3.89, MAE=2.87, MAPE=8.1%, R²=0.94) son coherentes internamente y están en línea con lo reportado en la literatura. Sin embargo, **no se reportan desviaciones estándar ni intervalos de confianza** para ninguno de los valores. Dado que los resultados se obtienen sobre series temporales (no sobre muestras i.i.d.), la comparación estadística requiere pruebas de significancia apropiadas (p.ej., Diebold-Mariano test para comparación de precisión de pronóstico). La ausencia de pruebas estadísticas formales reduce la solidez del paper.

**Tabla II – Multi-Horizonte:**
La variación de RMSE de 2.94 (τ=4) a 3.89 (τ=24) se describe como "gradual y controlada" con un incremento del 32%. Sin embargo, no queda claro si los modelos de cada horizonte son entrenados por separado (lo que implicaría 6 modelos distintos) o si se usa un único modelo Seq2Seq que genera todos los horizontes simultáneamente. La sección de configuración experimental no lo especifica con suficiente claridad.

**Tabla III – Multi-Dataset:**
Los resultados muestran que el dataset sintético 5G produce el mejor RMSE (3.52), lo cual es esperable dado que los datos sintéticos tienen patrones más regulares. Sin embargo, dado que el sintético es generado con el propio código de los autores (`generate_datasets.py`), existe un riesgo de sesgo de evaluación. Los parámetros del generador podrían haber sido ajustados para favorecer el modelo propuesto. Se recomienda incluir una descripción explícita de la separación entre los parámetros del generador y el proceso de optimización del modelo.

**Tabla IV – KPIs de Gestión de Recursos:**
La reducción del 40.9% en tasa de bloqueo es el resultado más relevante. Sin embargo, la simulación de nivel de sistema descrita no está suficientemente detallada: no se especifica el número de usuarios simulados, la distribución de llegada de tráfico, el algoritmo de scheduling reactivo baseline, ni los parámetros de la red simulada (número de celdas, capacidad por celda, número de slices). Esta falta de detalle impide la reproducibilidad de los resultados de gestión de recursos.

**Corrección requerida — Figura adicional (nueva):**

> **Figura nueva: Esquema de la simulación de nivel de sistema para evaluación de KPIs de gestión de recursos.**
>
> Se debe incorporar una figura titulada: **"Fig. X. Arquitectura de la simulación de nivel de sistema para evaluación comparativa de gestión reactiva vs. proactiva de recursos en redes 5G"**. Esta figura debe mostrar un diagrama de bloques que represente: (a) el generador de demanda de tráfico que utiliza el dataset Milano durante las últimas 6 semanas del periodo de test; (b) el bloque de predicción LSTM propuesto con horizonte τ pasos; (c) el bloque de optimización robusta (Algoritmo 3) que consume las predicciones y produce la asignación de PRBs; (d) el simulador de red con parámetros explícitos (número de celdas, PRBs disponibles, slices eMBB/URLLC/mMTC, modelo de canal); (e) el bloque de medición de KPIs (tasa de bloqueo, latencia, utilización de PRBs, consumo energético); y (f) la rama paralela del algoritmo reactivo de referencia (scheduling proporcional a la demanda observada). Las flechas de flujo de datos deben diferenciarse de las flechas de control. El diagrama debe usar la convención de la figura IEEE con líneas sólidas para flujo principal y líneas discontinuas para retroalimentación.

### II.6 Evaluación de los Algoritmos

Los cinco algoritmos presentados en la Sección VI son una fortaleza del artículo. La presentación paso a paso con condiciones de parada, estrategias de fallback y mecanismos de retroalimentación es apropiada para la reproducibilidad. Sin embargo, se identifican las siguientes deficiencias:

**Algoritmo 2 (Predicción en Tiempo Real con Intervalos de Confianza):**
Como se indicó en la inconsistencia 4, el artículo describe conformal prediction pero el código implementa MC Dropout. Se recomienda:
- Opción A: Actualizar el artículo para describir MC Dropout con la formulación teórica correspondiente y citar [Gal & Ghahramani, 2016] para la justificación bayesiana.
- Opción B: Actualizar el código para implementar conformal prediction (split conformal con calibration set) y reportar cobertura empírica de los intervalos producidos.

**Algoritmo 5 (NSGA-II Multi-objetivo):**
La formulación del problema multi-objetivo en la Sección V.D menciona tres objetivos: minimizar consumo energético, minimizar latencia, maximizar utilización. Sin embargo, la Tabla IV solo reporta métricas de una solución del frente de Pareto (no queda claro cuál). Se debe especificar qué punto del frente de Pareto se selecciona para la comparación y justificar la elección.

---

## III. ANÁLISIS DE CITAS Y REFERENCIAS

### III.1 Referencias con DOI Ausente o Incompleto

Las siguientes referencias listadas en el artículo carecen de DOI, lo cual dificulta la verificación y acceso:

| Ref | Autores | Fuente | DOI |
|-----|---------|--------|-----|
| [9] | Huang et al. | IEEE WCSP 2019 | Ausente |
| [10] | Trinh et al. | IEEE PIMRC 2018 | Ausente |
| [13] | Pascanu et al. | ICML 2013 | Ausente (disponible: 10.5555/3042817.3043083) |
| [14] | Cho et al. | EMNLP 2014 | Ausente (disponible: 10.3115/v1/D14-1179) |
| [15] | Bahdanau et al. | ICLR 2015 | Ausente (arXiv: 1409.0473) |
| [16] | Kingma & Ba | ICLR 2015 | Ausente (arXiv: 1412.6980) |
| [17] | Srivastava et al. | JMLR 2014 | Ausente (disponible: acceso abierto) |
| [21] | Ba et al. | arXiv 2016 | Ausente (arXiv: 1607.06450) |
| [23] | Hyndman & Athanasopoulos | Libro OTexts | Sin DOI (acceso libre en otexts.com) |
| [24] | Box et al. | Libro Wiley | Sin DOI (libro) |
| [27] | Abou-zeid et al. | IEEE CAMAD 2020 | Ausente |
| [29] | 3GPP TS 23.288 | Estándar 3GPP | Sin DOI (referencia de estándar técnico) |
| [30] | Sutskever et al. | NIPS 2014 | Ausente |
| [31] | Vaswani et al. | NIPS 2017 | Ausente (disponible: 10.5555/3295222.3295349) |
| [32] | Luong et al. | EMNLP 2015 | Ausente (disponible: 10.18653/v1/D15-1166) |
| [33] | Qin et al. | IJCAI 2017 | Ausente (disponible: 10.24963/ijcai.2017/366) |
| [34] | Shi et al. | NIPS 2015 | Ausente |
| [35] | Zhang et al. | IEEE TrustCom 2019 | Ausente |
| [36] | Cleveland et al. | J. Off. Stat. 1990 | Sin DOI (artículo de 1990, sin DOI electrónico) |
| [39] | Ben-Tal et al. | Libro Princeton | Sin DOI (libro) |
| [40] | Birge & Louveaux | Libro Springer | Sin DOI (libro) |
| [50] | Konečný et al. | arXiv 2016 | Ausente (arXiv: 1610.05492) |

**Corrección requerida:** Para todas las referencias de artículos de conferencia y revistas con DOI disponible, debe añadirse el DOI. Para libros, es aceptable omitir el DOI pero debe incluirse ISBN o editorial completa. Para preprints arXiv, debe indicarse el número arXiv. Para estándares 3GPP, el formato correcto es citar el número de especificación técnica, versión y organismo.

### III.2 Inconsistencia en el Citado de [9]

El artículo afirma explícitamente en la Sección I.C: "Los trabajos previos de Huang et al. [9] [...] se limitan a arquitecturas básicas sin mecanismos de atención". Sin embargo, el título completo de [9] es "Mobile Traffic Prediction Using LSTM **with Attention Mechanism**". Esta contradicción directa puede interpretarse como deshonestidad académica involuntaria o como un error de caracterización. El artículo debe reconocer que [9] también usa atención y justificar en qué difiere la arquitectura propuesta (p.ej., atención de Bahdanau específicamente, procesamiento multi-resolución, integración con gestión de recursos).

### III.3 Referencia [29] Incorrecta para Dataset Sintético

Como se indicó, 3GPP TS 23.288 no es una referencia de dataset. El formato de citación de estándares en IEEE debe seguir el formato:
> "3rd Generation Partnership Project (3GPP), "Architecture enhancements for 5G System (5GS) to support network data analytics services," Technical Specification 3GPP TS 23.288, Rel. 16, Dec. 2019."

Adicionalmente, se debe citar el trabajo original del generador de datasets (si existe en la literatura) o describir en detalle el modelo de generación, que actualmente solo está en el código Python y no en el artículo.

### III.4 Referencias de Trabajos Relevantes No Citados

La revisión del estado del arte identifica trabajos relevantes que deberían considerarse:

1. **Transformers para predicción de tráfico:** [Vaswani et al., 2017] es citado ([31]), pero trabajos específicos de Transformers para tráfico de redes móviles (p.ej., Temporal Fusion Transformer, PatchTST) no se consideran. Dado que los Transformers han superado a las LSTMs en múltiples benchmarks de series temporales desde 2021, su omisión como baseline es una debilidad.

2. **TCN (Temporal Convolutional Networks):** Bai et al. [An Empirical Evaluation of Generic Convolutional and Recurrent Networks for Sequence Modeling, 2018] demostraron que las TCN superan a las LSTMs en muchas tareas de series temporales con menor costo computacional. No se incluyen como baseline ni se discuten.

3. **Graph Neural Networks para correlación espacial:** El artículo menciona correlación espacial entre celdas (Sección I.E, Capa 1) pero no considera modelos basados en GNN (p.ej., STGCN, DCRNN) que explotan explícitamente la topología de la red. Estos son trabajos directamente relevantes.

4. **Foundation Models para telecomunicaciones:** La Sección VIII menciona "modelos fundacionales de telecomunicaciones" como dirección futura pero no cita trabajos específicos recientes (p.ej., Telco-LLM, NetLLM).

5. **Online learning para tráfico no-estacionario:** El Algoritmo 4 (detección de deriva CUSUM) es relevante pero debería relacionarse con la literatura de concept drift y online learning más amplia.

---

## IV. ANÁLISIS DEL ESTADO DEL ARTE Y SUGERENCIAS DE EXPLORACIÓN

### IV.1 Estado del Arte Cubierto

El artículo cubre adecuadamente los siguientes aspectos del estado del arte:
- Modelos estadísticos clásicos: ARIMA/SARIMA ✅
- Métodos de ML clásico: SVR, Random Forest ✅
- Arquitecturas de deep learning para series temporales: RNN, LSTM, GRU ✅
- Mecanismos de atención: Bahdanau, Luong, Vaswani ✅
- Optimización robusta y estocástica para redes ✅
- Network slicing y gestión de recursos ✅
- Zero Touch Network Management ✅

### IV.2 Gaps en el Estado del Arte — Temas a Incorporar

Se sugiere explorar e incorporar los siguientes temas que son directamente relevantes al trabajo:

**Temas recomendados para exploración y posible simulación:**

1. **Temporal Fusion Transformer (TFT) como baseline adicional:** El TFT [Lim et al., 2021, doi:10.1016/j.ijforecast.2021.03.012] es actualmente el método de referencia para predicción multi-horizonte de series temporales. Su omisión como baseline debilita la comparación. Se recomienda incluirlo como baseline adicional o justificar explícitamente por qué no se considera.

2. **Redes Neuronales Convolucionales-LSTM (ConvLSTM) para correlación espacio-temporal:** [34] (Shi et al.) es citado pero no se incluye como baseline en las simulaciones. ConvLSTM es particularmente relevante dado que el artículo menciona correlación espacial entre celdas vecinas en la arquitectura.

3. **Predicción de tráfico en escenarios de red O-RAN:** La arquitectura O-RAN (Open Radio Access Network) es el contexto operacional natural para los algoritmos de gestión proactiva propuestos. Explorar cómo el framework se integra con el rApps y xApps de O-RAN añadiría relevancia práctica significativa.

4. **Cuantificación de incertidumbre bayesiana:** El artículo usa MC Dropout (o conformal prediction, según la versión) pero no compara la calibración de los intervalos de confianza resultantes. Incluir métricas de calibración (p.ej., PICP - Prediction Interval Coverage Probability, PINAW - Prediction Interval Normalized Average Width) fortalecería la contribución.

5. **Análisis de equidad entre slices (network slicing fairness):** La gestión proactiva de recursos entre slices eMBB, URLLC y mMTC plantea problemas de equidad que no se abordan. Métricas como el índice de Jain para asignación de recursos añadirían perspectiva práctica.

6. **Detección de anomalías de tráfico:** El modelo de tráfico compuesto (Ec. 15) incluye una componente de impacto de eventos especiales $C(t)$. La capacidad del modelo para detectar y predecir estos eventos anómalos podría explorarse mediante un análisis dedicado.

---

## V. EVALUACIÓN TÉCNICA DE LOS SCRIPTS DE SIMULACIÓN

### V.1 Calidad General del Código

El código es de buena calidad técnica general:
- Documentación: docstrings detallados en todos los módulos ✅
- Estructura modular: separación clara de responsabilidades ✅
- Reproducibilidad: semilla aleatoria fija (SEED=42) ✅
- Type hints: uso de anotaciones de tipo Python ✅
- Self-tests: modo `--self-test` en todos los scripts ✅

### V.2 Problemas Técnicos Identificados en el Código

#### Problema 1: Arquitectura Propuesta No Implementada como Clase Unificada

Como se indicó, la arquitectura de 5 capas descrita en el artículo no tiene un equivalente directo en `models.py`. `MultiResolutionLSTM` implementa solo las capas 2-3, y `AttentionLSTM` implementa solo la capa 4. La capa 1 (embedding contextual) y la capa 5 (salida con estimación de varianza) no están implementadas en ninguna clase de `models.py`.

**Corrección:** Crear una clase `ProposedLSTM` (o `TrafficLSTM5Layer`) en `models.py` que integre las cinco capas funcionales descritas en la Sección IV.E, con los parámetros especificados (4.2M total).

#### Problema 2: Inconsistencia en Parámetros de la Capa 2

El artículo indica "Cada rama tiene 265K parámetros". El valor correcto para una BiLSTM de 2 capas con 128 unidades (256 bidireccional) y `input_size` variable sería aproximadamente 264K–270K dependiendo del `input_size`. El valor "265K" podría ser un error tipográfico por "256K" (valor más limpio) o puede ser correcto dado un `input_size` específico que no se especifica.

#### Problema 3: Mezcla de NumPy Random y Python Random en `models.py`

En la clase `AttentionLSTM`, el teacher forcing usa `np.random.random()` (línea 277) en lugar del generador de PyTorch. Esto puede causar inconsistencias en la reproducibilidad cuando se fija la semilla con `torch.manual_seed()` pero no con `np.random.seed()`.

**Corrección:** Reemplazar `np.random.random() < teacher_forcing_ratio` por `torch.rand(1).item() < teacher_forcing_ratio`.

#### Problema 4: Implementación de XGBoostBaseline

`models.py` importa y define `XGBoostBaseline` pero `run_benchmarks.py` no lo incluye en la evaluación comparativa, y el artículo tampoco lo menciona en las comparaciones. O bien se incluye en la comparación (requiere añadir XGBoost a `requirements.txt`) o se elimina del código para evitar confusión.

#### Problema 5: Lookback Inconsistente con el Artículo

El artículo especifica lookback = 96 pasos para el dataset Milano (10 min → 16 horas de lookback, no 24 horas como indica el código). Verificar: `LOOKBACK_MILANO = 144` en `generate_datasets.py` corresponde a 144 × 10 min = 24 horas ✅. Sin embargo, el artículo en la Sección IV.E (Capa 4) dice "procesando los 96 estados del encoder" para lookback=96, pero en otras secciones el lookback para Milano es 144. Esta ambigüedad debe resolverse.

### V.3 Requisitos de Reproducibilidad

Para que los resultados sean plenamente reproducibles se necesita:

1. Especificar la versión exacta de CUDA usada (el código menciona "CUDA 11.8")
2. Incluir un archivo `environment.yml` con todas las versiones exactas de dependencias (no solo las restricciones mínimas en `requirements.txt`)
3. Proporcionar el código de la semilla aleatoria completa para todas las librerías (PyTorch, NumPy, CUDA)
4. Incluir los scripts de generación de datasets con los parámetros exactos usados para generar los datasets almacenados en `results/*.npz`

---

## VI. EVALUACIÓN GLOBAL Y RECOMENDACIONES PRIORITARIAS

### VI.1 Fortalezas del Artículo

1. **Ambición y completitud:** El framework cubre todo el pipeline desde la predicción hasta la gestión de recursos, con cinco algoritmos detallados.
2. **Resultados cuantitativos sólidos:** Las mejoras reportadas (>40% en tasa de bloqueo, >25% en eficiencia energética) son significativas.
3. **Validación multi-dataset:** Evaluar sobre tres datasets de naturaleza distinta incrementa la credibilidad de los resultados.
4. **Interpretabilidad:** El análisis de pesos de atención es una contribución de alto valor práctico para despliegue en producción.
5. **Código disponible:** La disponibilidad de scripts de simulación bien documentados es una ventaja importante para la reproducibilidad.

### VI.2 Debilidades Críticas (Corrección Obligatoria)

| Prioridad | Deficiencia | Tipo |
|-----------|-------------|------|
| 🔴 CRÍTICA | Artículo en español (idioma incorrecto para la revista) | Formato |
| 🔴 CRÍTICA | Inconsistencias dataset sintético (granularidad, duración, celdas) | Metodología |
| 🔴 CRÍTICA | Arquitectura propuesta no implementada como clase unificada | Reproducibilidad |
| 🔴 CRÍTICA | Ecuaciones sin formato LaTeX (Word Equation format) | Formato |
| 🟡 MAYOR | Falta de figura de arquitectura del modelo | Presentación |
| 🟡 MAYOR | Contradicción en caracterización de [9] (Huang et al.) | Citas |
| 🟡 MAYOR | Conformal prediction vs MC Dropout (Algoritmo 2) | Metodología |
| 🟡 MAYOR | Ausencia de pruebas estadísticas de significancia en comparaciones | Estadística |
| 🟡 MAYOR | Parámetros del simulador de nivel de sistema no especificados | Metodología |
| 🟡 MAYOR | Falta de Transformers y TCN como baselines adicionales | Estado del arte |
| 🟠 MENOR | DOIs ausentes en múltiples referencias de conferencias | Formato |
| 🟠 MENOR | Discrepancia en paciencia de early stopping (40 vs 20) | Código |
| 🟠 MENOR | np.random.random() en teacher forcing (reproducibilidad) | Código |
| 🟠 MENOR | XGBoostBaseline definido pero no evaluado | Consistencia |

### VI.3 Sugerencias Adicionales de Mejora

1. **Ampliar el abstract en inglés** (al traducir el artículo) para incluir una frase sobre la arquitectura de 5 capas, los tres datasets usados, y los cinco algoritmos presentados, manteniendo el límite de 150 palabras de IEEE Wireless Communications.

2. **Añadir una subsección de Limitaciones** en la Sección VIII, discutiendo: (a) el uso de datos reales vs. sintéticos; (b) la hipótesis de que el tráfico predicho es el tráfico total y no el desglose por slice; (c) la suposición de que la demanda predicha se puede satisfacer instantáneamente con la asignación calculada.

3. **Incluir análisis de complejidad temporal y espacial** de la arquitectura propuesta de forma más rigurosa, comparando con los modelos baseline en términos de FLOPs por inferencia y memoria en GPU, no solo latencia en ms.

4. **Incluir el código fuente en un repositorio público** (GitHub, Zenodo) y proporcionar el DOI del repositorio en el artículo, siguiendo las mejores prácticas de reproducibilidad en ciencia abierta.

5. **Revisar las magnitudes de RMSE reportadas:** Los valores RMSE=3.89, MAE=2.87 no tienen unidades indicadas explícitamente. ¿Están en escala normalizada [0,1]? ¿En unidades de tráfico original? Esto debe aclararse en las tablas de resultados.

---

## VII. DECISIÓN EDITORIAL RECOMENDADA

**Decisión:** Rechazo con invitación a resubmisión (Major Revision)

**Justificación:** El artículo aborda un problema relevante con un enfoque técnicamente ambicioso y presenta resultados que podrían ser de interés para la comunidad IEEE Wireless Communications. Sin embargo, las deficiencias identificadas son demasiado numerosas y significativas para una revisión menor. El idioma del manuscrito (español en lugar de inglés) impide la evaluación formal por revisores internacionales y debe corregirse como primer paso. Las inconsistencias entre el artículo y los scripts de simulación (especialmente el dataset sintético y la arquitectura del modelo) comprometen la reproducibilidad y la integridad científica del trabajo. Una vez corregidas estas deficiencias, el trabajo podría tener un impacto significativo en la comunidad y merece una resubmisión rigurosa.

---

*Informe generado mediante análisis automatizado del manuscrito DOCX y los scripts de simulación Python. Las evaluaciones técnicas se basan en la lectura directa del texto del artículo y el código fuente. Los DOIs indicados como "disponibles" deben verificarse manualmente antes de incorporarlos al manuscrito.*
