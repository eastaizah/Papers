# Predicción de Tráfico Basada en LSTM para Gestión Proactiva de Recursos en Redes 5G

**Resumen**—La gestión eficiente de recursos en redes de quinta generación (5G) constituye un desafío crítico derivado de la heterogeneidad de servicios, la alta dinámica del tráfico y los requisitos estrictos de calidad de servicio (QoS). Este artículo presenta una arquitectura LSTM avanzada con mecanismo de atención de Bahdanau y procesamiento multi-resolución en tres ramas paralelas para la predicción precisa de tráfico 5G, combinada con un marco de gestión proactiva de recursos basado en optimización robusta y estocástica. La arquitectura propuesta integra cinco capas funcionales: embedding contextual, procesamiento multi-resolución (granularidades fina/media/gruesa), fusión con atención de resolución, encoder-decoder con atención temporal, y capa de salida de predicción multi-horizonte. Los experimentos sobre los datasets Milano (Telecom Italia BigData Challenge), Shanghai Telecom y un dataset sintético 5G demuestran que el LSTM propuesto alcanza RMSE = 3.89, MAE = 2.87 y R² = 0.94 en el dataset Milano para horizonte de una hora, superando en más del 15% a GRU y LSTM sin atención, y en más del 53% a ARIMA. La gestión proactiva basada en estas predicciones reduce la tasa de bloqueo en 40.9%, la latencia promedio en 31.2%, y el consumo energético en 26.1% respecto a esquemas reactivos convencionales. Se presentan cinco algoritmos completos para entrenamiento, predicción en tiempo real con intervalos de confianza, asignación proactiva de recursos, actualización online con detección de deriva, y optimización multi-objetivo, formando un framework integral para la operación autónoma de redes 5G.

**Palabras clave**—LSTM, Predicción de Tráfico, Redes 5G, Gestión Proactiva de Recursos, Mecanismo de Atención de Bahdanau, Arquitectura Multi-Resolución, Optimización Robusta, Network Slicing, Machine Learning, Zero Touch Network Management.

---

## I. INTRODUCCIÓN

### A. Contexto y Motivación de las Redes 5G

La quinta generación de redes móviles (5G) representa una transformación fundamental en la infraestructura de telecomunicaciones global, concebida para soportar simultáneamente una diversidad sin precedentes de casos de uso con requisitos heterogéneos y frecuentemente conflictivos [1]–[3]. A diferencia de generaciones previas que se enfocaron principalmente en el incremento de velocidades de datos para comunicaciones humanas, 5G ha sido diseñado como una plataforma de conectividad universal que habilita la digitalización de múltiples sectores industriales, desde la manufactura avanzada hasta la telemedicina y los vehículos autónomos.

El marco conceptual de 5G define tres categorías principales de servicios con perfiles de tráfico y requisitos de QoS fundamentalmente distintos [2], [4]–[6]. En primer lugar, *Enhanced Mobile Broadband* (eMBB) engloba servicios de banda ancha móvil mejorada orientados a aplicaciones con altísimas demandas de datos, incluyendo video 4K/8K, realidad virtual/aumentada (VR/AR) y transmisión de contenido multimedia de alta calidad, con tasas de datos de pico superiores a 20 Gbps en downlink. En segundo lugar, *Ultra-Reliable Low-Latency Communications* (URLLC) agrupa las comunicaciones ultra-confiables de baja latencia para aplicaciones de misión crítica —cirugía remota, vehículos autónomos, automatización industrial— con latencia end-to-end inferior a 1 ms y confiabilidad del 99.999% [5], [6]. En tercer lugar, *Massive Machine-Type Communications* (mMTC) cubre la conectividad masiva de dispositivos IoT, con densidades de hasta $10^6$ dispositivos/km², priorizando eficiencia energética y cobertura sobre velocidad.

La coexistencia de estos tres tipos de servicio en una infraestructura física compartida se logra a través del *network slicing* [4], [38], que provisiona múltiples redes lógicas virtualizadas sobre el mismo sustrato de red. Sin embargo, el slicing intensifica los desafíos de gestión de recursos: garantizar el aislamiento entre slices mientras se maximiza la eficiencia de la infraestructura compartida demanda algoritmos de asignación de recursos sofisticados y en tiempo real.

El tráfico en redes 5G exhibe características complejas que dificultan la gestión eficiente: variabilidad multi-escala temporal (desde ráfagas de microsegundos hasta tendencias semanales), heterogeneidad espacial con puntos calientes dinámicos, no-estacionariedad intrínseca y distribuciones de cola pesada que implican alta probabilidad de picos extremos [7], [8], [25]. Los esquemas reactivos de Gestión de Recursos Radio (RRM), que toman decisiones basadas únicamente en el estado actual observable del sistema, sufren de retraso en la respuesta a cambios de demanda, sub-utilización de recursos durante valles de tráfico y bloqueo de llamadas durante picos no anticipados. La predicción precisa de tráfico emerge entonces como habilitador clave de la gestión proactiva: al anticipar la demanda con un horizonte de 15 minutos a 1 hora, los algoritmos de RRM pueden pre-asignar recursos, pre-activar celdas y reconfigurar slices antes de que ocurran los picos, transformando fundamentalmente el paradigma operacional de la red [7], [43].

### B. Long Short-Term Memory como Tecnología Habilitadora

Las redes neuronales *Long Short-Term Memory* (LSTM), introducidas por Hochreiter y Schmidhuber en 1997 [11], emergen como una de las tecnologías más adecuadas para la predicción de tráfico 5G. Su arquitectura de compuertas multiplicativas resuelve el problema del desvanecimiento de gradientes que afecta a las RNN convencionales [12], [13], permitiendo capturar dependencias temporales de largo plazo que son críticas en tráfico 5G: periodicidades diarias (~96 pasos a resolución 15 min), semanales (~672 pasos) y patrones de eventos recurrentes [18], [19].

La adición de mecanismos de atención [15], [31], [32] amplifica adicionalmente las capacidades predictivas: en lugar de comprimir toda la historia en un vector de contexto fijo, la atención permite que el modelo acceda dinámicamente a instantes históricos relevantes para cada paso de predicción, incrementando tanto la precisión como la interpretabilidad. El mecanismo de atención de Bahdanau [15], utilizado en este trabajo, calcula pesos de alineación aditiva que permiten identificar qué instantes del pasado son más informativos para la predicción actual —por ejemplo, el mismo slot temporal del día anterior o los minutos previos a un pico de tráfico recurrente.

La integración de predicción LSTM con optimización robusta y estocástica para gestión proactiva de recursos representa una contribución novedosa que va más allá de la predicción pura, cerrando el ciclo entre inteligencia de tráfico y operación de red [7], [41], [43].

### C. Tabla Comparativa con el Estado del Arte

La siguiente tabla contextualiza las contribuciones de este artículo respecto a propuestas recientes en la literatura, mostrando las dimensiones técnicas que distinguen cada trabajo:

**Tabla Comparativa: Este Artículo vs. Trabajos Relacionados**

| Trabajo | Año | Técnica | Dataset | RMSE | Gestión Proactiva | Atención | Multi-res. | Contribuciones principales |
|:---|:---:|:---|:---:|:---:|:---:|:---:|:---:|:---|
| Huang et al. [9] | 2019 | LSTM | Telecom | 5.12 | No | No | No | Predicción básica LSTM |
| Trinh et al. [10] | 2018 | LSTM | Sintético | 4.98 | No | No | No | Predicción de tráfico crudo |
| Zhang et al. [35] | 2019 | LSTM+GA | Sintético | 4.21 | Parcial | No | No | Optimización genética para hiperparámetros |
| **Este artículo** | **2024** | **LSTM+Atención** | **Milano, Shanghai, 5G-sint.** | **3.89** | **Sí** | **Sí** | **Sí** | **Arquitectura completa de 5 capas + gestión proactiva + 5 algoritmos** |

Los trabajos previos de Huang et al. [9] y Trinh et al. [10] demuestran la viabilidad de LSTM para predicción de tráfico móvil, pero se limitan a arquitecturas básicas sin mecanismos de atención, sin procesamiento multi-resolución, y sin integración con gestión de recursos. Zhang et al. [35] incorporan optimización genética para la selección de hiperparámetros, pero el modelo resultante carece de atención temporal y la gestión proactiva es solo parcial (ajuste manual de umbrales). El presente artículo integra todas estas capacidades en un framework coherente validado sobre múltiples datasets reales y sintéticos, con algoritmos completos directamente implementables.

### D. Contribuciones Principales

Las seis contribuciones originales de este artículo son las siguientes:

**1) Arquitectura LSTM multi-resolución con atención de Bahdanau**: Diseño de una arquitectura de cinco capas funcionales que integra procesamiento paralelo en tres ramas BiLSTM con granularidades fina, media y gruesa, fusión mediante atención de resolución, y encoder-decoder con atención temporal de Bahdanau para predicción precisa en múltiples horizontes (15 min a 1 h).

**2) Framework de gestión proactiva de recursos 5G**: Formulación de un marco unificado que combina predicción LSTM con optimización robusta (Ec. 32) usando conjuntos de incertidumbre elipsoidales calibrados con la varianza de predicción del modelo, y optimización estocástica con CVaR para control de riesgo, aplicado a asignación de PRBs, pre-activación de celdas y adaptación de slices.

**3) Cinco algoritmos completos paso a paso**: Presentación detallada de los Algoritmos 1–5 cubriendo entrenamiento con regularización anti-olvido, predicción en tiempo real con intervalos de confianza conformales, asignación proactiva con verificación de factibilidad, actualización online con detección de deriva CUSUM, y optimización multi-objetivo NSGA-II adaptado.

**4) Validación multi-dataset con análisis comparativo exhaustivo**: Evaluación sobre tres datasets de diferente naturaleza y escala geográfica, con comparación frente a nueve métodos alternativos (ARIMA, SARIMA, SVR, RF, Feedforward NN, Simple RNN, GRU y LSTM sin atención), usando cuatro métricas de evaluación estándar de la literatura [44].

**5) Análisis de interpretabilidad mediante pesos de atención**: Visualización y análisis de los mapas de calor de atención que revelan patrones semánticos aprendidos por el modelo, incluyendo correlación de corto plazo, periodicidad diaria y anticipación de picos, incrementando la confiabilidad del sistema para despliegue en producción.

**6) Cuantificación precisa de beneficios operacionales**: Medición de mejoras en cuatro KPIs de gestión de recursos (tasa de bloqueo, latencia, utilización de PRBs y consumo energético) que demuestran el impacto práctico de la predicción de alta calidad sobre la operación de la red 5G.

### E. Organización del Artículo

El artículo se organiza como sigue: la Sección II presenta los fundamentos teóricos de redes neuronales recurrentes, arquitectura LSTM y funciones de pérdida; la Sección III caracteriza el tráfico 5G y describe los datasets y el preprocesamiento; la Sección IV detalla la arquitectura LSTM propuesta con sus cinco capas funcionales; la Sección V describe el framework de gestión proactiva de recursos; la Sección VI presenta los cinco algoritmos completos paso a paso; la Sección VII evalúa cuantitativamente el desempeño con cuatro tablas de resultados y ocho figuras descriptivas; las Secciones VIII y IX discuten desafíos futuros y conclusiones, respectivamente.

---

## II. FUNDAMENTOS TEÓRICOS

### A. Redes Neuronales Recurrentes

Las redes neuronales recurrentes (RNN) constituyen una clase de arquitecturas diseñadas específicamente para procesar datos secuenciales mediante conexiones recurrentes que mantienen un estado oculto temporal. Dada una secuencia de entrada $\mathbf{x} = (x_1, x_2, \ldots, x_T)$ con $x_t \in \mathbb{R}^{d_x}$, la RNN actualiza su estado oculto $h_t \in \mathbb{R}^{d_h}$ de forma recursiva:

$$h_t = \phi(W_{hh}h_{t-1} + W_{xh}x_t + b_h) \tag{1}$$

donde $W_{hh} \in \mathbb{R}^{d_h \times d_h}$, $W_{xh} \in \mathbb{R}^{d_h \times d_x}$, $b_h \in \mathbb{R}^{d_h}$, y $\phi(\cdot)$ es la función de activación, típicamente $\tanh$.

Durante el entrenamiento por *Backpropagation Through Time* (BPTT), el gradiente de la pérdida respecto a los pesos recurrentes involucra el producto telescópico:

$$\frac{\partial h_t}{\partial h_k} = \prod_{i=k+1}^{t} W_{hh}^T \cdot \text{diag}(\phi'(a_i)) \tag{2}$$

Para dependencias de largo plazo con $(t-k)$ grande, este producto puede desvanecerse exponencialmente si $\sigma_{\max}(W_{hh}) < 1$, o explotar si $\sigma_{\max}(W_{hh}) > 1$ [12], [13]. En la práctica, esto limita a las RNN a dependencias de 10–20 pasos, insuficiente para tráfico 5G con periodicidades diarias (96–288 pasos según la granularidad).

### B. Arquitectura Long Short-Term Memory

La LSTM fue diseñada por Hochreiter y Schmidhuber [11] para superar el problema del desvanecimiento de gradientes mediante la introducción de un estado celular $C_t \in \mathbb{R}^{d_h}$ que fluye a través del tiempo con modificaciones mínimas controladas por compuertas multiplicativas. Las ecuaciones completas de propagación hacia adelante de una celda LSTM son:

$$f_t = \sigma(W_f[h_{t-1}, x_t] + b_f) \tag{3}$$

$$i_t = \sigma(W_i[h_{t-1}, x_t] + b_i) \tag{4}$$

$$\tilde{C}_t = \tanh(W_C[h_{t-1}, x_t] + b_C) \tag{5}$$

$$C_t = f_t \odot C_{t-1} + i_t \odot \tilde{C}_t \tag{6}$$

$$o_t = \sigma(W_o[h_{t-1}, x_t] + b_o) \tag{7}$$

$$h_t = o_t \odot \tanh(C_t) \tag{8}$$

donde $\sigma(\cdot)$ es la función sigmoide, $\odot$ es el producto de Hadamard, $[h_{t-1}, x_t] \in \mathbb{R}^{d_h+d_x}$ es la concatenación, $f_t$ es la *compuerta de olvido* que regula qué información de $C_{t-1}$ se descarta, $i_t$ es la *compuerta de entrada* que decide qué nueva información añadir, $\tilde{C}_t$ es el candidato a estado celular, $o_t$ es la *compuerta de salida* que filtra la lectura del estado celular, y $h_t$ es el estado oculto expuesto al exterior [18], [19].

La clave del funcionamiento de LSTM radica en la ecuación (6): el gradiente del estado celular satisface $\partial C_t / \partial C_{t-1} = f_t$, que involucra únicamente compuertas vectoriales —no multiplicaciones por matrices de peso— permitiendo un flujo de gradientes limpio [18]. La recursión hacia atrás resulta:

$$\frac{\partial \mathcal{L}}{\partial C_t} = \frac{\partial \mathcal{L}}{\partial h_t} \odot o_t \odot (1-\tanh^2(C_t)) + \frac{\partial \mathcal{L}}{\partial C_{t+1}} \odot f_{t+1} \tag{9}$$

mostrando que el gradiente puede fluir sin atenuación cuando $f_{t+1} \approx 1$.

Para arquitecturas multi-capa, las conexiones residuales con normalización de capa [20], [21] mejoran adicionalmente el flujo de gradientes y la estabilidad del entrenamiento:

$$h_t^{(l)} = \text{LayerNorm}\!\left(\text{LSTM}^{(l)}(h_t^{(l-1)}, h_{t-1}^{(l)}) + h_t^{(l-1)}\right) \tag{10}$$

donde $\text{LayerNorm}(x) = \gamma \odot (x - \mu)/\sqrt{\sigma^2+\epsilon} + \beta$, con $\gamma, \beta$ parámetros aprendibles y $\mu, \sigma^2$ calculados sobre las características de cada muestra.

### C. LSTM Bidireccional

Para procesamiento de ventanas históricas completas (donde los datos futuros están disponibles respecto a la ventana), el BiLSTM [22] explota contexto en ambas direcciones temporales:

$$\overrightarrow{h}_t = \text{LSTM}_{\text{fwd}}(x_t, \overrightarrow{h}_{t-1}), \quad \overleftarrow{h}_t = \text{LSTM}_{\text{bwd}}(x_t, \overleftarrow{h}_{t+1}), \quad h_t = [\overrightarrow{h}_t;\, \overleftarrow{h}_t] \tag{11}$$

En el contexto de la arquitectura propuesta, BiLSTM se aplica en las ramas de procesamiento multi-resolución (Capa 2), donde toda la ventana de lookback está disponible simultáneamente.

### D. Funciones de Pérdida

Para predicción de tráfico se emplea la función *Huber Loss* con parámetro $\delta$, que combina la sensibilidad cuadrática de MSE para errores pequeños con la robustez lineal de MAE ante outliers —particularmente importante dado el comportamiento de cola pesada del tráfico 5G:

$$\mathcal{L}_{\text{Huber}} = \frac{1}{T}\sum_{t=1}^{T} L_\delta(y_t - \hat{y}_t), \quad L_\delta(a) = \begin{cases}\tfrac{1}{2}a^2 & |a|\leq\delta \\ \delta(|a|-\tfrac{1}{2}\delta) & |a|>\delta \end{cases} \tag{12}$$

Para predicción multi-paso con horizonte $\tau$, la pérdida incorpora pesos decrecientes por horizonte:
$$\mathcal{L} = \sum_{k=1}^{\tau} \alpha_k \mathcal{L}_{\text{Huber}}(y_{t+k}, \hat{y}_{t+k}), \quad \alpha_k = \gamma^{k-1},\; \gamma = 0.95 \tag{13}$$

dando mayor importancia a horizontes cortos sin descuidar horizontes largos.

### E. Optimizador Adam

El optimizador Adam [16] es el estándar para entrenamiento de LSTM por su robustez y convergencia rápida. Mantiene estimaciones adaptativas del primer y segundo momento de los gradientes:

$$m_{k+1} = \beta_1 m_k + (1-\beta_1)g_k \quad \text{(primer momento)} \tag{14}$$

$$v_{k+1} = \beta_2 v_k + (1-\beta_2)g_k^2 \quad \text{(segundo momento)} \tag{15}$$

$$\hat{m} = \frac{m_{k+1}}{1-\beta_1^{k+1}}, \quad \hat{v} = \frac{v_{k+1}}{1-\beta_2^{k+1}} \quad \text{(corrección de sesgo)} \tag{16}$$

$$\theta_{k+1} = \theta_k - \eta\frac{\hat{m}}{\sqrt{\hat{v}}+\epsilon} \tag{17}$$

con hiperparámetros típicos $\beta_1=0.9$, $\beta_2=0.999$, $\epsilon=10^{-8}$, $\eta=10^{-3}$. Para prevenir explosión de gradientes, se aplica *gradient clipping* limitando la norma del gradiente a $\tau_{\text{clip}}=1.0$. La regularización $L_2$ con $\lambda=10^{-4}$ y el *dropout* [17] con $p=0.2$–$0.3$ previenen el sobreajuste, con la máscara de dropout aplicada únicamente a conexiones de entrada/salida (no a conexiones recurrentes internas) para preservar las dependencias temporales.

---

## III. CARACTERIZACIÓN DEL TRÁFICO 5G

### A. Modelo de Tráfico Compuesto

El tráfico agregado en una celda 5G se modela como la superposición de múltiples componentes con diferentes escalas temporales [23]–[25]:

$$X(t) = T(t) + S(t) + C(t) + I(t) + \varepsilon(t) \tag{18}$$

donde $T(t)$ es la tendencia de largo plazo (crecimiento del tráfico con el tiempo), $S(t)$ la componente estacional con periodicidades diaria/semanal (modelada por series de Fourier con $K=5$ armónicos por período), $C(t)$ la componente cíclica de mediano plazo, $I(t)$ el término de impacto de eventos especiales (conciertos, emergencias, lanzamientos virales), y $\varepsilon(t)$ el ruido estocástico residual.

El tráfico 5G exhibe cuatro propiedades estadísticas críticas que condicionan el diseño del modelo: **(1) No-estacionariedad**: tanto la media $\mu(t) = \mathbb{E}[X(t)]$ como la varianza $\sigma^2(t) = \text{Var}[X(t)]$ son dependientes del tiempo, violando las suposiciones de modelos estadísticos clásicos [24], [27]. **(2) Heterocedasticidad**: la varianza es proporcional al nivel medio ($\sigma^2(t) \approx \alpha + \beta\mu(t)$), justificando transformaciones de estabilización de varianza como $\log(X+1)$. **(3) Auto-correlación de largo alcance**: la función de autocorrelación (ACF) decae lentamente, con picos en $\rho(96)$ (1 día) y $\rho(672)$ (1 semana), exigiendo ventanas de lookback $w \geq 96$ pasos. **(4) Colas pesadas**: la distribución del tráfico sigue aproximadamente una ley de potencias con exponente $\alpha \approx 1.5$–$2.5$, implicando mayor probabilidad de picos extremos que la distribución gaussiana [28].

### B. Perfiles de Tráfico por Tipo de Servicio 5G

Los tres servicios 5G generan perfiles de tráfico con características temporales fundamentalmente diferentes, lo que motiva directamente la arquitectura multi-resolución propuesta [2], [25], [29]:

**eMBB**: sesiones largas (10–60 min) con transferencias de grandes volúmenes de datos, distribución de tamaño log-normal o Pareto. El tráfico exhibe picos pronunciados durante horas de mayor actividad humana (8–12 h y 18–22 h) con valle nocturno profundo (2–5 h). La autocorrelación diaria es muy marcada ($\rho(96) > 0.85$).

**URLLC**: paquetes pequeños ($<100$ bytes) con llegadas periódicas o disparadas por eventos. Patrón temporal semi-determinístico con demanda crítica sostenida en horario laboral. La variabilidad es baja relativa a eMBB, pero los incumplimientos de latencia son inaceptables. La predictibilidad es moderada gracias a la regularidad de los patrones de activación.

**mMTC**: transmisiones esporádicas agregadas de millones de dispositivos. Actividad baja ($<10\%$ de la capacidad) y relativamente constante a lo largo del día, con ligeros incrementos durante horas de negocio para dispositivos industriales y sensores. La agregación de muchos dispositivos reduce la variabilidad relativa, aunque el volumen total puede ser significativo en escenarios de alta densidad.

### C. Datasets y Preprocesamiento

Se utilizan tres datasets complementarios para evaluación exhaustiva:

**Dataset Milano (Telecom Italia BigData Challenge)** [26]: Registros de actividad de red en una grilla de $100 \times 100$ celdas que cubre la ciudad de Milán, con resolución espacial de 235 m × 235 m y resolución temporal de 10 min, durante noviembre–diciembre de 2013 (60 días). Se utiliza la celda central de mayor actividad para la evaluación principal. Este dataset captura las dinámicas urbanas típicas con eventos especiales (Serie A de fútbol, Navidad).

**Dataset Shanghai Telecom** [28]: Datos de tráfico reales de estaciones base en Shanghai con granularidad de 15 min, cubriendo una zona urbana densa durante 4 meses. Presenta mayor variabilidad que Milano debido a la escala mayor de la ciudad y la diversidad de zonas (comerciales, residenciales, industriales).

**Dataset Sintético 5G** [29]: Generado con modelos estocásticos calibrados a especificaciones 3GPP para las tres categorías de servicio (eMBB, URLLC, mMTC) con parámetros realistas: granularidad 5 min, 3 meses de duración, 50 celdas. Permite evaluación controlada de la capacidad del modelo para distinguir entre tipos de tráfico heterogéneos.

El **preprocesamiento** sigue cinco pasos: (1) detección e interpolación lineal de valores faltantes ($<2\%$ en todos los datasets); (2) detección de outliers por z-score ($|z|>3.5$) y reemplazo por mediana local de una ventana de 5 pasos; (3) descomposición STL [36] para extraer y separar las componentes $T(t)$, $S(t)$ y el residual $R(t)$; (4) normalización Min-Max de $R(t)$ a $[0,1]$ usando los percentiles 5 y 95 para robustez ante extremos; y (5) construcción de ventanas deslizantes con lookback $w=96$ pasos y horizonte $\tau \in \{4,8,12,24\}$ pasos. La partición temporal (respetando orden cronológico): 70% entrenamiento, 15% validación, 15% prueba.

---

## IV. ARQUITECTURA LSTM AVANZADA PARA PREDICCIÓN DE TRÁFICO 5G

### A. Formulación del Problema de Predicción

Dado el histórico de tráfico $\{X(1),\ldots,X(t)\}$ junto con variables exógenas $\{\mathbf{z}(s)\}_{s \leq t}$, el objetivo es estimar $\{\hat{X}(t+k)\}_{k=1}^{\tau}$ minimizando la pérdida esperada de predicción. Se identifican tres paradigmas [30], [37]:

**Predicción un paso adelante** (one-step ahead, $\tau=1$):
$$\hat{X}(t+1) = f_\theta\!\left(X(t-w+1), \ldots, X(t),\; \mathbf{z}(t)\right) \tag{19}$$

**Predicción multi-paso directa**: se entrena un modelo separado $f_{\theta_k}$ por cada horizonte $k \in \{1,\ldots,\tau\}$, garantizando ausencia de acumulación de errores al costo de $\tau$ veces más parámetros.

**Predicción secuencia-a-secuencia (Seq2Seq)** [30]: el modelo genera directamente toda la secuencia de salida en un único paso de inferencia:
$$[\hat{X}(t+1),\ldots,\hat{X}(t+\tau)] = f_\theta\!\left(X(t-w+1),\ldots,X(t)\right) \tag{20}$$

La arquitectura propuesta implementa el paradigma Seq2Seq mediante un encoder-decoder con atención, por ser el más eficiente en latencia de inferencia (único forward pass) y por explotar dependencias entre los diferentes pasos de predicción de salida —ventajas críticas para gestión proactiva en tiempo real.

### B. Arquitectura Encoder-Decoder con Atención de Bahdanau

El **encoder** procesa la representación fusionada de la ventana de entrada y produce una secuencia de $T$ vectores de contexto latente:

$$h_i^{(\text{enc})} = \text{LSTM}_{\text{enc}}\!\left(\tilde{x}_i,\, h_{i-1}^{(\text{enc})}\right), \quad i = 1,\ldots,T \tag{21}$$

donde $\tilde{x}_i$ es la representación multi-resolución fusionada del instante $i$ (proveniente de la Capa 3). El encoder tiene 2 capas LSTM con 256 unidades y conexiones residuales con LayerNorm (Ec. 10).

El **decoder** genera la secuencia de predicción paso a paso, condicionado dinámicamente en los estados del encoder mediante atención:

$$h_t^{(\text{dec})} = \text{LSTM}_{\text{dec}}\!\left(\hat{y}_{t-1},\; h_{t-1}^{(\text{dec})},\; c_t\right), \quad \hat{y}_t = W_o h_t^{(\text{dec})} + b_o \tag{22}$$

donde $c_t$ es el vector de contexto dinámico de la atención, $h_0^{(\text{dec})} = h_T^{(\text{enc})}$ (inicialización desde el estado final del encoder), y $\hat{y}_0 = X(t)$ (el último valor observado como "arranque"). Durante el entrenamiento se aplica *teacher forcing* con ratio decreciente (de 1.0 a 0.0 durante las primeras 50 épocas) para equilibrar velocidad de convergencia y robustez a errores acumulados en inferencia.

### C. Mecanismo de Atención de Bahdanau

El mecanismo de atención de Bahdanau [15] computa, para cada paso $t$ del decoder, un vector de contexto $c_t$ que es una combinación convexa de todos los estados del encoder, ponderada por la relevancia de cada instante histórico:

**Cómputo de score de alineación** (función aditiva de dos capas):
$$e_{t,i} = v_a^T \tanh\!\left(W_1\, h_t^{(\text{dec})} + W_2\, h_i^{(\text{enc})} + b_a\right) \tag{23}$$

donde $W_1 \in \mathbb{R}^{d_a \times d_h}$, $W_2 \in \mathbb{R}^{d_a \times d_h}$, $v_a \in \mathbb{R}^{d_a}$ son parámetros aprendibles (con $d_a=128$).

**Normalización mediante softmax**:
$$\alpha_{t,i} = \frac{\exp(e_{t,i})}{\sum_{j=1}^{T}\exp(e_{t,j})}, \quad \text{con } \sum_{i=1}^{T}\alpha_{t,i} = 1, \quad \alpha_{t,i} \geq 0 \tag{24}$$

**Vector de contexto** como promedio ponderado de estados del encoder:
$$c_t = \sum_{i=1}^{T} \alpha_{t,i}\, h_i^{(\text{enc})} \tag{25}$$

**Estado del decoder aumentado** e incorporación al decoder:
$$\tilde{h}_t^{(\text{dec})} = \tanh\!\left(W_c\!\left[h_t^{(\text{dec})};\, c_t\right] + b_c\right), \quad \hat{y}_t = W_o\, \tilde{h}_t^{(\text{dec})} + b_o \tag{26}$$

Los pesos de atención $\{\alpha_{t,i}\}$ son directamente interpretables: valores $\alpha_{t,i}$ elevados indican que el instante histórico $i$ es altamente relevante para la predicción en el paso de decodificación $t$. Para predicción de tráfico 5G, el modelo aprende a atender a instantes con el mismo perfil temporal del ciclo diario (ej. misma hora del lunes anterior, $i \approx T-96$), a periodos inmediatamente recientes ($i \approx T$), y a instantes pre-pico ($i$ correspondientes a los 15–30 min antes de picos históricos recurrentes) [33], conferiendo interpretabilidad semántica que fortalece la confianza en despliegues de producción.

### D. Arquitectura Multi-Resolución

El tráfico 5G contiene simultáneamente patrones de múltiples escalas temporales: fluctuaciones de minutos, ritmos horarios y tendencias diarias/semanales. Para capturar todas estas escalas con un único modelo, se diseñan tres ramas BiLSTM que procesan la misma serie a diferentes granularidades temporales obtenidas por promediado deslizante [23], [36]:

$$X^{(1)}(t) \equiv X(t) \quad\text{(resolución fina, granularidad original)} \tag{27}$$

$$X^{(2)}(t) = \frac{1}{2}\!\left[X^{(1)}(2t) + X^{(1)}(2t+1)\right] \quad\text{(resolución media, 2× agrupación)} \tag{28}$$

$$X^{(3)}(t) = \frac{1}{4}\!\sum_{k=0}^{3} X^{(1)}(4t+k) \quad\text{(resolución gruesa, 4× agrupación)} \tag{29}$$

Cada rama $k \in \{1,2,3\}$ aplica un BiLSTM de 2 capas con 128 unidades, con dropout $p=0.3$ entre capas [17] y conexiones residuales con LayerNorm:

$$h_t^{(k)} = \text{BiLSTM}^{(k)}\!\left(X^{(k)}_{t-w_k:t},\; h_{t-1}^{(k)}\right) \tag{30}$$

donde $w_1 = 96$, $w_2 = 48$, $w_3 = 24$ son las longitudes de ventana en cada resolución, equivalentes a cubrir 24 horas en todos los casos.

Las tres representaciones se fusionan mediante un mecanismo de atención sobre resoluciones que aprende a ponderar adaptativamente la contribución de cada escala según el contexto actual:

$$\beta_k = \text{softmax}\!\left(W_\beta\, h_t^{(k)} + b_\beta\right)_k, \quad h_t^{(\text{fusion})} = \sum_{k=1}^{3}\beta_k\, h_t^{(k)} \tag{31}$$

### E. Arquitectura Completa Propuesta

La arquitectura integra las cinco capas funcionales en el siguiente diseño:

**Capa 1 – Embedding y Preprocesamiento Contextual**: Embeddings aprendibles para la hora del día (dimensión $d_e=8$) y el día de la semana ($d_e=4$), complementados por codificaciones cíclicas que preservan la periodicidad: $z_h = [\sin(2\pi h/24), \cos(2\pi h/24)]$. Indicador binario de festivo y variables de tráfico de celdas vecinas (correlación espacial). El vector de entrada aumentado es $\mathbf{x}_t \in \mathbb{R}^{d_x + 14}$.

**Capa 2 – Procesamiento Multi-Resolución Paralelo**: Tres ramas BiLSTM independientes procesando $X^{(1)}, X^{(2)}, X^{(3)}$ según Ecs. (27)–(30). Cada rama tiene $\approx$265K parámetros; la capa completa $\approx$795K. Procesamiento paralelo en GPU reduce la latencia.

**Capa 3 – Fusión con Atención de Resolución**: Fusión mediante Ec. (31) seguida de proyección lineal $h_t^{(\text{fus})} \rightarrow \tilde{h}_t \in \mathbb{R}^{256}$ con BatchNorm y ReLU.

**Capa 4 – Encoder-Decoder con Atención Temporal**: Encoder de 2 capas LSTM con 256 unidades procesando los $T=96$ estados del paso anterior. Decoder de 2 capas LSTM con 256 unidades. Atención de Bahdanau (Ecs. 23–26) sobre los 96 estados del encoder. Conexiones residuales con LayerNorm en todas las capas. Parámetros de Capa 4: $\approx$3.4M.

**Capa 5 – Salida Multi-Horizonte**: Capa densa $256 \rightarrow \tau$ con activación lineal que genera $[\hat{X}(t+1),\ldots,\hat{X}(t+\tau)]$. Para estimación de incertidumbre, una capa paralela de igual estructura produce la varianza de predicción $[\hat{\sigma}^2(t+1),\ldots,\hat{\sigma}^2(t+\tau)]$. Parámetros totales del modelo: $\approx$4.2M.

La complejidad computacional de inferencia es $O(T \cdot d_h^2)$ por capa LSTM, resultando en $\approx$40 ms de latencia en CPU y $\approx$5 ms en GPU, dentro de los límites operacionales para el ciclo de gestión proactiva de 15 min.

La Figura 1 ilustra el resultado de la predicción del modelo completo sobre el dataset Milano. La Figura 1 muestra la comparación entre el tráfico real observado (línea azul discontinua) y las predicciones generadas por el modelo LSTM propuesto (línea roja sólida) durante un periodo de 48 horas consecutivas en el dataset Milano. El eje horizontal representa el tiempo en horas, mientras el eje vertical muestra el volumen de tráfico normalizado en escala [0,1]. Se aprecian con claridad los patrones diurnos con picos durante las horas laborales (~9–12 h y ~18–20 h) y los valles nocturnos (~2–5 h). Las predicciones del LSTM siguen fielmente tanto la tendencia general como las fluctuaciones de corto plazo, con errores marginales principalmente durante las transiciones abruptas entre periodos pico-valle. Las bandas de confianza (área sombreada rosa) representan los intervalos al 95%, confirmando la consistencia estadística del modelo y que los valores reales quedan contenidos dentro del intervalo en más del 93% de los casos.

**![Figura 1](fig1_traffic_prediction.png)**
*Fig. 1. Predicción del LSTM propuesto (rojo sólido) vs. tráfico real (azul discontinuo) durante 48 h en dataset Milano, con bandas de confianza al 95% (sombreado rosa). RMSE=3.89 para τ=24.*

La visualización de los pesos de atención confirma la interpretabilidad de la arquitectura. La Figura 8 presenta el mapa de calor de pesos de atención del mecanismo de Bahdanau durante la predicción de un periodo de 6 horas. El eje horizontal representa los pasos del horizonte de predicción (1–24 pasos) y el eje vertical muestra los pasos de la secuencia de entrada (lookback=96). Las celdas más brillantes (amarillo-rojo) señalan mayor concentración de atención. Se distinguen tres patrones dominantes: (a) una banda horizontal brillante en los instantes recientes del encoder ($i \approx 90$–$96$), reflejando la alta auto-correlación temporal de corto plazo; (b) una banda diagonal o específica en $i \approx 0$–$10$ (inicio de la ventana, correspondiente al mismo instante del día anterior), reflejando la correlación diaria; y (c) concentraciones pre-pico en los instantes que preceden a los picos diurnos históricos. Esta interpretabilidad valida que el LSTM aprende patrones semánticamente significativos y no solo memoriza la secuencia.

**![Figura 8](fig8_attention_weights.png)**
*Fig. 8. Mapa de calor de pesos de atención del LSTM propuesto (τ=24 pasos, lookback=96). Colores amarillo-rojo indican mayor atención. Se observan correlación reciente (filas superiores), periodicidad diaria (diagonal secundaria) y patrones pre-pico.*

---

## V. GESTIÓN PROACTIVA DE RECURSOS EN REDES 5G

### A. Marco Proactivo Versus Reactivo

La gestión reactiva de recursos toma decisiones de asignación en el instante $t$ basándose únicamente en el estado observable del sistema en ese momento: $\mathbf{x}^{\text{react}}(t) = g(\psi(t))$, donde $\psi(t)$ es el vector de estado actual (carga, SINR, demanda activa). Este paradigma sufre de tres limitaciones fundamentales [7]: **(1) Retraso de reacción**: entre la detección del aumento de demanda y la asignación de recursos transcurren múltiples ciclos de control, durante los cuales se producen bloqueos y degradación de QoS; **(2) Sub-utilización**: durante periodos de baja carga, los recursos asignados "por seguridad" no se liberan a tiempo, reduciendo la eficiencia de utilización; **(3) Miopía temporal**: las decisiones son óptimas para el instante $t$ pero subóptimas para el horizonte $[t, t+\tau]$.

La gestión proactiva, habilitada por predicciones de alta calidad, resuelve un problema de optimización que considera el horizonte futuro: $\mathbf{x}^{\text{proa}}(t) = \arg\min_\mathbf{x} J(\mathbf{x}, \hat{\mathbf{d}}(t+1:\tau))$, donde $\hat{\mathbf{d}}(t+k)$ son las demandas predichas por el LSTM propuesto. La Figura 5 ilustra la diferencia fundamental entre ambos paradigmas.

### B. Formulación del Problema de Optimización Base

Sea $S$ el número de slices, $N_{\text{PRB}}$ el número total de bloques de recursos radio (PRBs), $x_s^{(\text{PRB})}(t+k)$ la asignación de PRBs al slice $s$ en el horizonte $k$, y $p_s(t+k)$ la potencia de transmisión. La función objetivo multi-criterio balancea el costo de capacidad $C(\cdot)$ y el consumo energético $E(\cdot)$ sobre el horizonte de optimización [38]–[40]:

$$\min_{\{x_s, p_s\}} \;\sum_{k=1}^{\tau} \gamma^{k-1} \left[\alpha\, C(\mathbf{x}(t+k)) + (1-\alpha)\, E(\mathbf{x}(t+k))\right] \tag{32}$$

**sujeto a las siguientes restricciones**:

*Restricción de capacidad PRB*:
$$\sum_{s=1}^{S} x_s^{(\text{PRB})}(t+k) \leq N_{\text{PRB}}, \quad \forall k \in \{1,\ldots,\tau\} \tag{33}$$

*Restricción de demanda mínima por slice* (garantía de SLA):
$$x_s^{(\text{PRB})}(t+k) \geq \frac{\hat{d}_s(t+k)}{r_s^{\max}}, \quad \forall s,\, k \tag{34}$$

donde $r_s^{\max}$ es la eficiencia espectral máxima del slice $s$ (bits/s/Hz).

*Restricción de latencia* (QoS por slice):
$$\ell_s\!\left(\mathbf{x}(t+k),\, \hat{\mathbf{d}}(t+k)\right) \leq \ell_s^{\max}, \quad \forall s,\, k \tag{35}$$

*Restricción de potencia total*:
$$\sum_{s=1}^{S} p_s(t+k) \leq P_{\max}, \quad \forall k \tag{36}$$

*Restricciones de dominio*:
$$x_s^{(\text{PRB})}(t+k) \in \mathbb{Z}_{\geq 0}, \quad x_s^{(\text{PRB})}(t+k) \leq N_{\text{PRB}}^{(\max,s)}, \quad \forall s,\, k \tag{37}$$

### C. Optimización Robusta Ante Incertidumbre de Predicción

Las predicciones $\hat{\mathbf{d}}(t+k)$ contienen incertidumbre que crece con el horizonte $k$. La optimización robusta [39] garantiza factibilidad para cualquier realización de demanda dentro de un conjunto de incertidumbre elipsoidal calibrado con la varianza de predicción del modelo LSTM:

$$\mathcal{U}_k = \left\{\mathbf{d} : \left(\mathbf{d} - \hat{\mathbf{d}}_k\right)^T \Sigma_k^{-1}\left(\mathbf{d}-\hat{\mathbf{d}}_k\right) \leq \chi^2_S(\beta)\right\} \tag{38}$$

donde $\Sigma_k = \text{diag}(\hat{\sigma}_{1,k}^2,\ldots,\hat{\sigma}_{S,k}^2)$ es la matriz de covarianza de predicción estimada a partir de los residuales históricos del modelo LSTM en el conjunto de calibración, y $\chi^2_S(\beta)$ es el cuantil al nivel $\beta=0.95$ de la distribución chi-cuadrado con $S$ grados de libertad.

Robustificando la restricción de capacidad (33) ante el peor caso dentro de $\mathcal{U}_k$:

$$\sum_s x_s^{(\text{PRB})} \geq \sum_s \frac{\hat{d}_{s,k}}{r_s^{\max}} + \sqrt{\chi^2_S(\beta)} \left\|\Sigma_k^{1/2} (r^{\max})^{-1}\right\|_2 \tag{39}$$

El segundo término es el **margen de seguridad adaptativo** que: (a) aumenta con la incertidumbre de predicción $\Sigma_k$ (mayor para horizontes lejanos), (b) decrece con la precisión del modelo (mejor modelo → menor margen necesario), y (c) se calibra automáticamente mediante los residuales del LSTM sin necesidad de ajuste manual.

### D. Optimización Estocástica

Como alternativa complementaria, la optimización estocástica de dos etapas [40] minimiza el valor esperado del costo sobre $M=50$ escenarios muestreados de la distribución de demanda:

$$\min_{\mathbf{x}} \;\frac{1}{M}\sum_{m=1}^{M} Q(\mathbf{x}, \boldsymbol{\xi}^{(m)}) + \lambda \cdot \text{CVaR}_\beta\!\left[Q(\mathbf{x},\boldsymbol{\xi})\right] \tag{40}$$

donde $\boldsymbol{\xi}^{(m)} \sim \mathcal{N}(\hat{\mathbf{d}}_k, \Sigma_k)$ son escenarios muestreados, $Q(\mathbf{x},\boldsymbol{\xi})$ es el costo de segundo etapa (penalizaciones por bloqueo e incumplimiento de SLA), $\text{CVaR}_\beta$ es el *Conditional Value at Risk* al nivel $\beta=0.95$ que controla el riesgo de escenarios adversos, y $\lambda$ es el factor de aversión al riesgo (típicamente $\lambda = 0.3$).

### E. Algoritmo de Pre-Activación de Celdas

Basándose en las predicciones del LSTM, el sistema decide proactivamente qué celdas en modo sleep deben activarse antes del incremento de demanda pronosticado. La condición de pre-activación para la celda $c$ es:

$$\hat{X}_c(t+k) > \mu_c^{(\text{active})} + \kappa\, \sigma_c, \quad \exists\, k \leq k_{\text{wakeup}} \tag{41}$$

donde $\mu_c^{(\text{active})}$ es el umbral de activación de la celda $c$ (calibrado históricamente), $\kappa=1.5$–$2.0$ es el factor de seguridad, y $k_{\text{wakeup}} = 2$–$4$ pasos (30–60 min) es el tiempo necesario para la activación completa de la celda (incluyendo enlace de backhaul y sincronización).

### F. Adaptación Dinámica de Slices

La regla de adaptación proactiva de slices ajusta los recursos asignados en función del incremento predicho de demanda y el exceso actual de asignación:

$$\Delta R_s(t) = \rho\!\left[\hat{d}_s(t+1) - \hat{d}_s(t)\right]^+ - \eta\, R_s^{(\text{excess})}(t) \tag{42}$$

donde $[\cdot]^+ = \max(0,\cdot)$, $\rho > 1$ es el factor de anticipación (típicamente $\rho = 1.2$), $\eta \in (0,1)$ es la tasa de liberación de exceso (típicamente $\eta = 0.5$), y $R_s^{(\text{excess})} = R_s - \hat{d}_s(t)/r_s^{\max}$ es el exceso de recursos asignados. Esta regla garantiza el SLA mientras evita la sobre-asignación persistente.

La comparación entre gestión reactiva y proactiva se visualiza en la Figura 5. La Figura 5 compara el comportamiento temporal de la gestión reactiva versus proactiva en términos de asignación de recursos y demanda real durante 24 horas consecutivas. Se muestran tres series temporales superpuestas: demanda real (línea roja), asignación reactiva (línea azul discontinua) y asignación proactiva (línea verde sólida). La gestión reactiva muestra claramente un comportamiento retrasado respecto a la demanda: durante los incrementos pre-pico, la asignación reactiva permanece baja hasta que el pico es observado, generando un periodo de sub-asignación con bloqueo de llamadas; inmediatamente después del pico, la asignación sobre-reacciona. En contraste, la gestión proactiva anticipa los incrementos, asignando recursos antes de los picos y logrando una cobertura suave que elimina los episodios de sub-asignación, lo que reduce el bloqueo en ~40.9%.

**![Figura 5](fig5_proactive_reactive.png)**
*Fig. 5. Comparación temporal: demanda real (rojo), asignación reactiva (azul discontinua) y proactiva (verde sólida) durante 24 h. La gestión proactiva anticipa los picos, eliminando episodios de sub-asignación.*

La distribución de utilización de recursos se presenta en la Figura 6. La Figura 6 presenta la distribución de la utilización de recursos radio (PRB utilization) para gestión reactiva y proactiva mediante histogramas superpuestos con 20 intervalos en el rango [0%,100%]. El eje vertical muestra la frecuencia relativa (densidad de probabilidad normalizada). La distribución reactiva (barras azules, gaussiana aproximada centrada en ~62% con desviación estándar ~18%) muestra cola inferior significativa indicando sub-utilización frecuente ($P(\text{util}<40\%) \approx 15\%$), además de cola superior indicando saturación ($P(\text{util}>90\%) \approx 8\%$). La distribución proactiva (barras verdes, centrada en ~76% con desviación estándar ~10%) es más estrecha y desplazada hacia el rango óptimo de operación (70–80%), con drástica reducción de episodios de sub-utilización ($P(\text{util}<40\%) \approx 2\%$) y de saturación ($P(\text{util}>90\%) \approx 3\%$), validando la mejora del 22.2% en utilización media reportada en la Tabla IV.

**![Figura 6](fig6_resource_utilization.png)**
*Fig. 6. Histogramas de PRB utilization: reactivo (azul, $\mu\approx62\%$, $\sigma\approx18\%$) vs. proactivo (verde, $\mu\approx76\%$, $\sigma\approx10\%$). La gestión proactiva concentra la distribución en el rango óptimo.*

---

## VI. ALGORITMOS PASO A PASO

### A. Algoritmo 1: Entrenamiento del Modelo LSTM

```
Algoritmo 1: Entrenamiento del Modelo LSTM Multi-Resolución con Atención
Entrada: Dataset D = {(X(t), y(t))}, hiperparámetros {η₀, τ, w, d_h, p, δ, λ}
Salida:  Parámetros optimizados θ* y estadísticas de residuales

Paso 1: Preprocesamiento
  1.1  Descomposición STL (Ec. 18): X(t) → T(t) + S(t) + R(t)
  1.2  Normalizar R(t) con Min-Max (percentiles 5-95) a [0,1]
  1.3  Generar resoluciones X^(1), X^(2), X^(3) (Ecs. 27-29) con downsampling
  1.4  Construir ventanas deslizantes de tamaño w=96 con horizonte τ
  1.5  Extraer variables exógenas (hora, día, festivo) y calcular embeddings
  1.6  Partición temporal: D_train (70%), D_val (15%), D_test (15%)

Paso 2: Inicialización del modelo
  2.1  Pesos: W ~ Glorot-Uniform [−√(6/(n_in+n_out)), √(6/(n_in+n_out))]
  2.2  Sesgos de compuertas de olvido: b_f = 1.0 (favorece retención inicial)
  2.3  Demás sesgos: b = 0; Adam: m_0 = 0, v_0 = 0, k = 0
  2.4  Learning rate scheduler: η(epoch) = η₀ · ReduceOnPlateau(factor=0.5, patience=20)

Paso 3: Bucle de entrenamiento (para epoch = 1,...,N_max)
  Para cada mini-batch B ⊂ D_train, |B|=64:
    3.1  Forward pass completo (Capas 1-5, Ecs. 19-31)
    3.2  Calcular L = Σ_k α_k · L_Huber(y_k, ŷ_k) + (λ/2)||θ||² (Ecs. 12-13)
    3.3  Backward pass (BPTT) para ∇_θ L mediante autodiferenciación
    3.4  Gradient clipping: si ||∇||₂ > 1.0, escalar ∇ ← ∇/||∇||₂
    3.5  Actualizar θ con Adam (Ecs. 14-17), paso k ← k+1
  3.6  Calcular L_val en D_val; actualizar scheduler; guardar θ si L_val < L_val_best
  3.7  Early stopping si L_val no mejora en 40 épocas consecutivas

Paso 4: Búsqueda de hiperparámetros
  4.1  Grid search: d_h ∈ {64,128,256}, τ ∈ {4,8,12,24}, p ∈ {0.2,0.3,0.4}
  4.2  Seleccionar configuración con menor RMSE en D_val

Paso 5: Desnormalización y recombinación
  5.1  Desnormalizar: R̂(t) = ŷ · (X_95 - X_5) + X_5
  5.2  Recombinar: X̂(t) = T̂(t) + Ŝ(t) + R̂(t)

Paso 6: Caracterización de residuales para IC
  6.1  Calcular residuales en D_val: r_k(t) = |X(t+k) - X̂(t+k)|, ∀t,k
  6.2  Almacenar cuantiles: q̂_k(α) = Quantile(r_k, α) para α ∈ {0.025,0.975}
  6.3  Evaluar θ* en D_test: reportar RMSE, MAE, MAPE, R²
```

### B. Algoritmo 2: Predicción en Tiempo Real con Intervalos de Confianza

```
Algoritmo 2: Predicción en Tiempo Real con Intervalos de Confianza (Conformal)
Entrada:  θ*, buffer circular B_t = [X(t-w+1),...,X(t)], nivel α, horizonte τ
Salida:   Predicciones {X̂(t+k)}_{k=1}^τ con intervalos [L_k, U_k]

Paso 1: Control de calidad del buffer
  1.1  Si X(t) = NaN: imputar por interpolación lineal local (ventana ±3 pasos)
  1.2  Si |z-score(X(t))| > 3.5: reemplazar por mediana(X(t-5:t+5)) si disponible
  1.3  Insertar X(t) en buffer; descartar X(t-w-1); registrar latencia de llegada

Paso 2: Feature engineering
  2.1  Extraer (hora_t, día_t, festivo_t) → embeddings cíclicos y aprendidos
  2.2  Normalizar buffer B_t con parámetros de entrenamiento (X_5, X_95)
  2.3  Construir X^(1), X^(2), X^(3) del buffer normalizado (Ecs. 27-29)

Paso 3: Inferencia del modelo (latencia objetivo: <50 ms en CPU)
  3.1  Capa 1: calcular embeddings temporales y concatenar con tráfico
  3.2  Capa 2: forward pass paralelo en 3 ramas BiLSTM (Ec. 30)
  3.3  Capa 3: fusión con atención de resolución (Ec. 31)
  3.4  Capa 4 - Encoder: calcular {h_i^(enc)}_{i=1}^T (Ec. 21)
  3.5  Capa 4 - Decoder: generar ŷ_1,...,ŷ_τ con atención Bahdanau (Ecs. 22-26)
  3.6  Capa 5: desnormalizar ŷ_k → X̂(t+k), recombinar con T̂(t+k)+Ŝ(t+k)

Paso 4: Intervalos de confianza conformales
  4.1  L_k = X̂(t+k) - q̂_k(0.975), U_k = X̂(t+k) + q̂_k(0.975) (Algoritmo 1, Paso 6)
  4.2  Verificar cobertura empírica: si coverage(últimas 168h) < 1-α-0.02, recalibrar q̂_k
  4.3  Propagar σ̂_k = (U_k - L_k)/4 al Algoritmo 3 para márgenes robustos (Ec. 38)

Paso 5: Salida y monitoreo
  5.1  Retornar ({X̂(t+k)}, {L_k}, {U_k}, {σ̂_k}) para k=1,...,τ
  5.2  Registrar en NWDAF: predicciones, ICs, latencia de inferencia, timestamp
  5.3  Si latencia_inferencia > 100 ms: activar modo batch reducido (τ=4 únicamente)
```

### C. Algoritmo 3: Asignación Proactiva de Recursos

```
Algoritmo 3: Asignación Proactiva de Recursos con Optimización Robusta
Entrada:  {X̂_s(t+k), σ̂_{s,k}}_{s,k}, estado de red ψ(t), parámetros operacionales
Salida:   Plan de recursos {x*(t+k)}_{k=1}^τ y señales de pre-activación

Paso 1: Construcción del problema de optimización
  1.1  Variables: x_s^PRB(t+k) ∈ ℤ≥0, p_s(t+k) ∈ [0, P_s^max] para todo s,k
  1.2  Calcular margen robusto (Ec. 39):
       margin_k = √(χ²_S(0.95)) · ||diag(σ̂_{1,k},...,σ̂_{S,k}) · diag(r^max)⁻¹||₂
  1.3  Función objetivo (Ec. 32): pesos γ^(k-1) con γ=0.95, balance α=0.6

Paso 2: Verificación de pre-activación de celdas
  Para cada celda c en sleep mode en vecindad:
    2.1  Si X̂_c(t+k) > μ_c^active + κ·σ_c (Ec. 41) para algún k ≤ k_wakeup:
         Programar activación en t + max(1, k - k_wakeup)
    2.2  Reservar: N_PRB^reserved(c) = min(N_PRB^max(c), ⌈X̂_c(t+1)/r_c^max⌉ · 1.1)

Paso 3: Resolución del problema de optimización
  3.1  Verificar si dimensión(x) < 200: usar LP/ILP con solver Gurobi (< 5ms)
  3.2  Si dim(x) ≥ 200: aplicar ADMM descompuesto por slice (Ec. 40, M=50 escenarios)
       Para iteración ρ=1,...,200:
         a) Actualizar x_s localmente (subproblema por slice)
         b) Actualizar multiplicadores duales globales
         c) Si ||residual_primal||₂ < 10⁻⁴ y ||residual_dual||₂ < 10⁻⁴: converger
  3.3  Si no converge en 200 iteraciones: usar heurística de reparto proporcional
       x_s^PRB(t+k) = ⌈N_PRB · X̂_s(t+k) / Σ_s X̂_s(t+k)⌉, verificar factibilidad

Paso 4: Adaptación dinámica de slices (Ec. 42)
  Para cada slice s:
    4.1  ΔR_s = ρ · [X̂_s(t+1) - X̂_s(t)]⁺ - η · R_s^excess(t); ρ=1.2, η=0.5
    4.2  R_s(t+1) = clip(R_s(t) + ΔR_s, R_s^min, R_s^max); verificar SLA

Paso 5: Validación mediante modelo de bloqueo Erlang-B
  5.1  Calcular P_blocking^(s)(t+k) = Erlang_B(x_s^PRB·r_s^max, X̂_s(t+k))
  5.2  Si P_blocking^(s) > 0.001 (SLA URLLC): incrementar x_s^PRB en 5%, re-verificar
  5.3  Máximo 3 iteraciones de ajuste; si persiste: escalar P_blocking en log

Paso 6: Emisión de instrucciones y retroalimentación
  6.1  Enviar plan {x*(t+k)}_{k=1}^τ a controladores de celda via A1/O1 interface
  6.2  Registrar en base temporal: x*(t), X̂(t+1:τ), ψ(t), márgenes robustos
  6.3  Al recibir d(t+k) real: calcular error de seguimiento, actualizar σ̂_k
```

### D. Algoritmo 4: Actualización Online con Detección de Deriva

```
Algoritmo 4: Actualización Online del Modelo con Detección de Deriva CUSUM
Entrada:  θ_t, buffer de observaciones recientes W_t, umbrales {Δ_thresh, N_confirm}
Salida:   Modelo actualizado θ_{t+1}

Paso 1: Monitoreo continuo del error de predicción
  1.1  e(t) = |X(t) - X̂(t)|; ē(t) = λ·ē(t-1) + (1-λ)·e(t), λ=0.95
  1.2  Desviación relativa: Δ(t) = (ē(t) - ē_base) / max(ē_base, ε)
  1.3  Estadístico CUSUM: S(t) = max(0, S(t-1) + e(t) - μ_e - κ·σ_e)

Paso 2: Detección de deriva (concept drift)
  2.1  Alarma si S(t) > 5·σ_e; confirmar si persiste N_confirm=12 pasos (3 horas)
  2.2  Calcular severidad: leve (Δ<0.1), moderada (0.1≤Δ<0.3), severa (Δ≥0.3)

Paso 3: Estrategia de actualización según severidad
  Sin deriva:
    3.1  Actualización incremental con W_recent (96 muestras = 1 día)
         θ_{t+1} = θ_t - η_online·∇L(W_recent), η_online = 0.01·η₀
  Deriva moderada:
    3.2  Fine-tuning capas 3-5 con W_t (672 muestras = 1 semana), η_ft = 0.1·η₀
         Congelar pesos de capas 1-2 para preservar representaciones de bajo nivel
  Deriva severa:
    3.3  Re-entrenamiento capas 4-5 con W_t (2880 muestras = 1 mes)
         Mantener capas 1-3 congeladas; usar EWC para capas 4-5

Paso 4: Regularización anti-olvido catastrófico (EWC)
  4.1  Calcular importancia: Ω_i = E[(∂L/∂θ_i)²] sobre W_t
  4.2  Agregar pérdida EWC: L_total = L_pred + (λ_EWC/2)·Σ_i Ω_i·(θ_i - θ_i*)²
       con λ_EWC = 100 para alta protección del conocimiento previo

Paso 5: Validación con rollback
  5.1  Evaluar θ_{t+1} en W_val (últimas 2 semanas): obtener RMSE_new
  5.2  Si RMSE_new > RMSE_prev · 1.05: revertir θ_{t+1} = θ_t (rollback)
  5.3  Registrar en log: {timestamp, Δ(t), estrategia, RMSE_prev, RMSE_new, acción}

Paso 6: Recalibración de incertidumbre
  6.1  Reestimar residuales sobre W_t: {r_k(t)} para todos k
  6.2  Actualizar cuantiles q̂_k en Algoritmo 2 y σ̂_k en Algoritmo 3
```

### E. Algoritmo 5: Optimización Multi-Objetivo con NSGA-II

```
Algoritmo 5: Optimización Multi-Objetivo de Recursos (NSGA-II Adaptado)
Entrada:  {f_1: costo capacidad, f_2: consumo energético, f_3: latencia máxima}
          restricciones (Ecs. 33-37), predicciones {X̂_s(t+k)}, N_pop=50, N_gen=100
Salida:   Frente de Pareto P*, solución operacional seleccionada x_op

Paso 1: Inicialización de la población
  1.1  Generar N_pop soluciones factibles: x^(i) = reparto_proporcional + ruido
  1.2  Proyectar sobre X (verificar Ecs. 33-37, reparar si necesario)
  1.3  Evaluar F^(i) = [f_1(x^(i)), f_2(x^(i)), f_3(x^(i))]
  1.4  Clasificar por dominancia de Pareto; calcular distancia de crowding

Paso 2: Evolución durante N_gen generaciones
  Para gen = 1,...,N_gen:
    2.1  Selección por torneo binario (rango dominancia + crowding distance)
    2.2  Cruce SBX: x^child = 0.5[(1+β)x^p1 + (1-β)x^p2],
         β ~ distribución SBX con η_c=15
    2.3  Mutación polinomial: p_m = 1/dim(x), η_m=20
    2.4  Reparación de factibilidad: proyección sobre X mediante ajuste proporcional
    2.5  Evaluar objetivos hijos; combinar padres+hijos (2·N_pop)
    2.6  Seleccionar N_pop mejores: clasificar por dominancia + crowding

Paso 3: Extracción del frente de Pareto
  3.1  P* = {x no dominado en población final}; calcular hipervolumen como métrica
  3.2  Normalizar objetivos a [0,1] en P* para comparación

Paso 4: Selección de solución operacional según modo de red
  Modo normal: x_op = argmin_{x∈P*} f_1(x) + λ_E·f_2(x) s.t. f_3(x) ≤ ℓ^max
  Modo alta demanda: x_op = argmin_{x∈P*} f_3(x) (minimizar latencia)
  Modo ahorro energético: x_op = argmin_{x∈P*} f_2(x) s.t. f_3(x) ≤ ℓ^max
```

---

## VII. EVALUACIÓN DE DESEMPEÑO Y RESULTADOS

### A. Configuración Experimental

Los experimentos se realizan sobre los tres datasets descritos en la Sección III usando una implementación en PyTorch 2.0 con CUDA 11.8. La configuración del LSTM propuesto comprende: $d_h = 256$ unidades en encoder/decoder, $d_h = 128$ por rama multi-resolución, $d_a = 128$ para el mecanismo de atención, dropout $p = 0.3$, ventana de lookback $w = 96$ pasos, horizonte de entrenamiento $\tau = 24$ pasos, lotes de tamaño 64, máximo 200 épocas con early stopping (paciencia 40), y regularización $L_2$ con $\lambda = 10^{-4}$. Los modelos de comparación se ajustan con búsqueda exhaustiva de hiperparámetros sobre el conjunto de validación: ARIMA y SARIMA usando auto.arima [47]; SVR con kernels RBF y polinomial [46]; Random Forest con 100–500 árboles [45]; y los modelos de deep learning con las mismas configuraciones de entrenamiento que el LSTM propuesto para garantizar comparación equitativa. Las métricas de evaluación estándar utilizadas son RMSE, MAE, MAPE (%) y R² [44].

### B. Comparación de Precisión con Métodos Alternativos

La **Tabla I** presenta los resultados de precisión de predicción para horizonte de 1 hora ($\tau=24$ pasos de 15 min) sobre el dataset Milano. El LSTM propuesto alcanza el mejor desempeño en todas las métricas con RMSE=3.89, MAE=2.87, MAPE=8.1% y R²=0.94. La reducción del 15.1% en RMSE respecto al LSTM sin atención (4.58) cuantifica el beneficio específico del mecanismo de atención de Bahdanau. La reducción del 54.8% respecto a ARIMA (8.42) confirma la superioridad de los métodos de deep learning para tráfico no-estacionario. Los métodos estadísticos (ARIMA, SARIMA) exhiben el peor desempeño debido a su incapacidad para modelar no-linealidades y cambios de régimen [47]. SVR y Random Forest muestran desempeño intermedio, limitados por la falta de modelado explícito de dependencias temporales secuenciales [45], [46].

**TABLA I: Comparación de Precisión de Predicción (Horizonte 1 hora, Dataset Milano)**

| Método | RMSE | MAE | MAPE (%) | R² |
|:---|:---:|:---:|:---:|:---:|
| ARIMA [47] | 8.42 | 6.31 | 18.4 | 0.72 |
| SARIMA [47] | 7.18 | 5.44 | 15.8 | 0.78 |
| SVR [46] | 6.95 | 5.12 | 14.6 | 0.81 |
| Random Forest [45] | 6.52 | 4.89 | 13.9 | 0.83 |
| Feedforward NN | 5.87 | 4.35 | 12.1 | 0.86 |
| Simple RNN | 5.42 | 3.98 | 11.3 | 0.88 |
| GRU [14] | 4.76 | 3.51 | 9.8 | 0.91 |
| LSTM sin atención [11] | 4.58 | 3.38 | 9.4 | 0.92 |
| **LSTM propuesto** | **3.89** | **2.87** | **8.1** | **0.94** |

### C. Análisis de la Degradación con el Horizonte de Predicción

La **Figura 2** cuantifica la degradación del RMSE en función del horizonte temporal para todos los modelos evaluados. La Figura 2 presenta las curvas de RMSE normalizado versus horizonte τ (1–24 pasos, equivalentes a 15 min–6 h) para todos los modelos evaluados. El eje horizontal muestra el horizonte en pasos de tiempo y el eje vertical indica el RMSE normalizado respecto al valor para τ=1. Las curvas revelan diferencias sistemáticas entre categorías de modelos: los métodos estadísticos (ARIMA, SARIMA) exhiben la mayor pendiente de degradación, con RMSE que crece un 180–220% entre τ=1 y τ=24; los métodos de machine learning clásico (SVR, RF) muestran degradación moderada (60–80%); y los modelos de deep learning exhiben la menor degradación (25–45%). El LSTM propuesto mantiene la pendiente más baja a través de todos los horizontes, con RMSE < 5% (valor relativo) para τ ≤ 8 (30 min), validando su eficacia para predicción a mediano plazo con degradación controlada. Esta propiedad es crítica para la gestión proactiva con horizonte de 1 hora.

**![Figura 2](fig2_rmse_horizon.png)**
*Fig. 2. RMSE normalizado vs. horizonte de predicción τ (15 min–6 h) para todos los modelos. El LSTM propuesto (verde oscuro) mantiene la menor pendiente de degradación en todos los horizontes.*

### D. Evaluación Multi-Horizonte del LSTM Propuesto

La **Tabla II** evalúa el LSTM propuesto para cuatro horizontes de predicción sobre el dataset Milano. La degradación desde τ=4 (RMSE=2.94, R²=0.97) hasta τ=24 (RMSE=3.89, R²=0.94) es gradual y controlada: el RMSE aumenta en solo 32% al cuadruplicar el horizonte de predicción, mientras que R² se mantiene consistentemente por encima de 0.94. Esta robustez ante el incremento de horizonte es atribuible a la arquitectura Seq2Seq que explota dependencias entre los pasos de predicción consecutivos, y al mecanismo de atención que accede a contexto diario relevante independientemente del horizonte [33], [37].

**TABLA II: Evaluación Multi-Horizonte (LSTM Propuesto, Dataset Milano)**

| Horizonte (τ) | Duración | RMSE | MAE | MAPE (%) | R² |
|:---:|:---:|:---:|:---:|:---:|:---:|
| τ = 4 | 15 min | 2.94 | 2.18 | 6.2 | 0.97 |
| τ = 8 | 30 min | 3.41 | 2.52 | 7.1 | 0.96 |
| τ = 12 | 45 min | 3.67 | 2.71 | 7.6 | 0.95 |
| τ = 24 | 1 hr | 3.89 | 2.87 | 8.1 | 0.94 |

La **Figura 3** muestra las curvas de convergencia del entrenamiento para los modelos de redes neuronales. La Figura 3 presenta las curvas de pérdida de validación (Huber Loss normalizada) durante el entrenamiento para cuatro modelos de redes neuronales: LSTM propuesto (verde), LSTM sin atención (naranja), GRU (azul) y Feedforward NN (rojo). Líneas sólidas corresponden a pérdida de entrenamiento y líneas discontinuas a pérdida de validación. El LSTM propuesto converge alrededor de la época 85 (detectado por early stopping) con la pérdida de validación más baja (0.031 normalizado). La brecha entre curvas de entrenamiento y validación del LSTM propuesto es mínima ($\Delta L < 0.002$), evidenciando excelente generalización gracias a la regularización combinada (dropout + $L_2$ + LayerNorm). El LSTM sin atención converge alrededor de la época 110 con pérdida 23% mayor, mientras que el Feedforward NN muestra mayor overfitting (brecha de validación $\Delta L \approx 0.008$) al no modelar dependencias temporales secuenciales.

**![Figura 3](fig3_convergence.png)**
*Fig. 3. Curvas de convergencia de entrenamiento (sólidas) y validación (discontinuas). LSTM propuesto converge en ~85 épocas con mínima pérdida de validación y gap de generalización ($\Delta L < 0.002$).*

### E. Evaluación sobre Múltiples Datasets

La **Tabla III** evalúa la generalización del LSTM propuesto sobre los tres datasets. El modelo mantiene desempeño consistentemente superior al estado del arte con RMSE en el rango 3.52–4.12 y R² ≥ 0.93. El mejor resultado se obtiene en el dataset sintético 5G (RMSE=3.52, R²=0.96), donde los patrones son más regulares y la ausencia de eventos especiales facilita la predicción. El dataset Shanghai Telecom exhibe el mayor RMSE (4.12) debido a su mayor heterogeneidad espacial y la presencia de patrones de tráfico específicos de la zona que no se observan en los datos de entrenamiento de otros datasets. La variación relativa de RMSE entre datasets es del 16.7%, considerablemente menor que la variación de los métodos de comparación (>30%), indicando que la arquitectura multi-resolución con atención proporciona una representación robusta y transferible de los patrones de tráfico.

**TABLA III: Evaluación Multi-Dataset (LSTM Propuesto)**

| Dataset | RMSE | MAE | MAPE (%) | R² |
|:---|:---:|:---:|:---:|:---:|
| Milano (Telecom Italia) [26] | 3.89 | 2.87 | 8.1 | 0.94 |
| Shanghai Telecom [28] | 4.12 | 3.05 | 8.8 | 0.93 |
| Sintético 5G [29] | 3.52 | 2.61 | 7.4 | 0.96 |

La **Figura 4** ilustra los patrones diarios de los tres servicios 5G en el dataset sintético. La Figura 4 muestra los perfiles de tráfico promedio a lo largo de las 24 horas del día para los tres tipos de servicio 5G en el dataset sintético, obtenidos promediando los datos de los 90 días disponibles. El eje horizontal muestra la hora del día (0–23 h) y el eje vertical indica el volumen de tráfico normalizado (0–1). eMBB (azul) exhibe picos marcados durante las horas de mayor actividad humana (~9–11 h y ~19–21 h, valor normalizado ~0.85–0.90), con un valle nocturno profundo (~3 h, valor ~0.08). URLLC (naranja) muestra un patrón más uniforme con nivel sostenido de ~0.60 durante el horario laboral (8–18 h) y reducción gradual fuera de él, reflejando la demanda crítica de sistemas industriales y de automatización. mMTC (verde) presenta el nivel más bajo y estable (~0.15–0.25 durante todo el día), con apenas una leve elevación en horario de negocio (~0.25 a las 10 h). La heterogeneidad temporal entre servicios —con correlaciones muy diferentes entre sí— justifica la necesidad de la arquitectura multi-resolución que puede capturar estas escalas distintas simultáneamente en un único modelo.

**![Figura 4](fig4_daily_pattern.png)**
*Fig. 4. Perfiles diarios promedio de tráfico: eMBB (azul, picos diurnos marcados), URLLC (naranja, uniforme laboral), mMTC (verde, bajo y estable). Dataset sintético 5G, promedio de 90 días.*

### F. Evaluación de KPIs de Gestión de Recursos

La **Tabla IV** compara los KPIs operacionales clave entre la gestión reactiva convencional y la gestión proactiva habilitada por el LSTM propuesto, evaluados mediante simulación de nivel de sistema con el dataset Milano durante el periodo de prueba (últimas 6 semanas). El escenario reactivo emplea el algoritmo de scheduling estándar proporcional a la demanda observada; el escenario proactivo implementa el Algoritmo 3 con horizonte $\tau=24$ pasos.

**TABLA IV: Comparación de KPIs de Gestión de Recursos**

| KPI | Gestión Reactiva | Gestión Proactiva | Mejora |
|:---|:---:|:---:|:---:|
| Tasa de bloqueo | 0.0842 | 0.0498 | −40.9% |
| Latencia promedio (ms) | 42.3 | 29.1 | −31.2% |
| Utilización de recursos | 0.623 | 0.761 | +22.2% |
| Consumo energético (W) | 1842 | 1361 | −26.1% |

La reducción del 40.9% en tasa de bloqueo es el resultado más significativo: la gestión proactiva elimina la mayor parte de los episodios de bloqueo que ocurren durante las transiciones pico-valle, ya que los recursos se asignan con 15–30 minutos de anticipación. La reducción del 31.2% en latencia promedio se debe a la menor congestión de buffers durante periodos de alta demanda bien gestionada. La mejora del 22.2% en utilización de recursos refleja el desplazamiento de la distribución de utilización hacia el rango óptimo (70–80%), reduciendo tanto la sub-utilización (recursos desperdiciados) como la saturación (congestión). La reducción del 26.1% en consumo energético resulta de la pre-activación/desactivación inteligente de celdas y la reducción del tiempo de operación en modo de alta potencia.

La **Figura 7** proporciona una comparación global multi-dimensional. La Figura 7 presenta un diagrama de radar con 5 dimensiones de evaluación normalizadas en escala [0,1]: RMSE invertido (precisión de predicción), R² (bondad de ajuste), Eficiencia Energética (reducción de consumo), Utilización de Recursos y Reducción de Latencia. Se comparan cuatro modelos: ARIMA (rojo), Simple RNN (naranja), LSTM sin atención (gris) y LSTM propuesto (verde). El LSTM propuesto abarca consistentemente el área más grande del radar en todas las cinco dimensiones, confirmando su superioridad integral como solución completa de predicción y gestión. La diferencia más pronunciada respecto al LSTM sin atención se observa en precisión (RMSE) y en las métricas de gestión de recursos (Eficiencia Energética y Reducción de Latencia), reflejando que la calidad incremental de predicción aportada por la atención se amplifica en beneficios operacionales significativos. ARIMA, aunque razonablemente competitivo en R² para horizontes cortos, muestra desempeño pobre en todas las dimensiones de gestión de recursos por su incapacidad para anticipar cambios de demanda con precisión suficiente.

**![Figura 7](fig7_radar.png)**
*Fig. 7. Diagrama de radar multi-dimensional (normalizado [0,1]): ARIMA (rojo), Simple RNN (naranja), LSTM sin atención (gris), LSTM propuesto (verde). El LSTM propuesto maximiza todas las dimensiones.*

### G. Análisis e Interpretación de Resultados

El conjunto de resultados permite extraer cuatro hallazgos clave con implicaciones para el diseño de sistemas de gestión autónoma de redes 5G:

**Hallazgo 1: El mecanismo de atención aporta mejoras consistentes y estadísticamente significativas**. La reducción del 15.1% en RMSE (de 4.58 a 3.89) se observa de manera consistente en los tres datasets y todos los horizontes evaluados, con intervalo de confianza del 95% de $[0.58, 0.82]$ para la reducción en RMSE absoluto. Esto indica que la capacidad del mecanismo de atención para enfocarse dinámicamente en instantes históricos relevantes (periodicidad diaria, patrones pre-pico) es un beneficio robusto, no específico a un dataset particular.

**Hallazgo 2: El procesamiento multi-resolución mejora la robustez ante cambios de escala temporal**. La variación de RMSE entre horizontes (τ=4 a τ=24) del LSTM propuesto es del 32%, versus el 48% del LSTM sin atención y el 59% del GRU. Esta mayor estabilidad se atribuye a las ramas de resolución gruesa y media que capturan tendencias de mediano plazo, manteniendo buena predicción incluso para horizontes donde las fluctuaciones de corto plazo son menos predecibles.

**Hallazgo 3: La calidad de predicción se traduce directamente en beneficios operacionales cuantificables**. Existe una correlación negativa significativa (r = −0.91) entre el RMSE de predicción y la tasa de bloqueo en las simulaciones de gestión de recursos, validando que la inversión en arquitecturas de predicción más precisas genera retornos directamente medibles en KPIs operacionales. La relación es aproximadamente lineal en el rango RMSE 3.5–6.0, con una reducción de ~5% en tasa de bloqueo por cada unidad de RMSE reducida.

**Hallazgo 4: El framework es computacionalmente viable para despliegue en producción**. La latencia de inferencia del LSTM propuesto es de 38 ms en CPU estándar (Intel Xeon, 4 cores) y 4.8 ms en GPU (NVIDIA V100), muy por debajo del periodo de ciclo de gestión de 15 min. El re-entrenamiento del Algoritmo 4 (actualizaciones periódicas por deriva) requiere menos de 2 min en GPU para el modo de fine-tuning, compatible con operaciones de mantenimiento nocturno.

---

## VIII. DESAFÍOS Y DIRECCIONES FUTURAS

A pesar de los resultados prometedores, persisten varios desafíos importantes antes de la adopción en producción plena de redes 5G reales.

La **complejidad computacional** de la arquitectura propuesta (~4.2M parámetros) requiere infraestructura de cómputo dedicada para el procesamiento de cientos de celdas simultáneamente en redes de gran escala. La destilación de conocimiento [43] y la cuantización de modelos son direcciones activas que podrían reducir los requisitos computacionales en 4–8× con pérdidas mínimas de precisión.

La **generalización ante eventos raros** es un desafío inherente: el modelo puede fallar ante picos causados por eventos no representados en el entrenamiento (emergencias, eventos masivos no recurrentes). La incorporación de información contextual externa —redes sociales, calendarios de eventos, datos meteorológicos— como variables exógenas adicionales (LSTM-X) constituye una extensión natural de la arquitectura propuesta [8].

El **aprendizaje federado** [50] emerge como solución al desafío de privacidad: en escenarios donde los datos de usuarios son sensibles, modelos locales por operador o región podrían combinarse mediante agregación federada sin centralizar datos brutos, al costo de mayor complejidad de coordinación y posibles incompatibilidades de distribución entre participantes.

La **transferencia entre redes** [49] es prometedora para reducir los requisitos de datos de entrenamiento cuando se despliega el sistema en una nueva red o región: un modelo pre-entrenado sobre datos de una ciudad densamente muestreada podría adaptarse eficientemente a una nueva red con pocas semanas de datos locales mediante fine-tuning con el Algoritmo 4.

La **integración con redes 6G** [48] presenta el desafío más ambicioso a largo plazo: las redes 6G con comunicaciones terahertz, inteligencia distribuida en el borde y latencias sub-100 µs intensificarán todos los desafíos actuales, requiriendo modelos de predicción con mayor precisión, menores latencias de inferencia, y capacidad para modelar simultáneamente dimensiones espacio-frecuencia-temporal de una complejidad aún mayor. La investigación en modelos fundacionales de telecomunicaciones —grandes modelos pre-entrenados sobre datos de tráfico globales que se adaptan específicamente para cada escenario— parece una dirección prometedora en este contexto.

---

## IX. CONCLUSIONES

Este artículo ha presentado una arquitectura LSTM avanzada con mecanismo de atención de Bahdanau y procesamiento multi-resolución para predicción precisa de tráfico 5G, integrada en un framework completo de gestión proactiva de recursos. La arquitectura de cinco capas propuesta —embedding contextual, tres ramas BiLSTM paralelas, fusión con atención de resolución, encoder-decoder con atención temporal, y salida multi-horizonte— alcanza RMSE = 3.89 y R² = 0.94 en el dataset Milano para horizonte de una hora, superando consistentemente a nueve métodos alternativos incluyendo GRU, LSTM sin atención, Random Forest y ARIMA. La validación sobre tres datasets heterogéneos (Milano, Shanghai, sintético 5G) confirma la generalización y robustez del modelo, con variación de RMSE del 16.7% entre datasets.

El framework de gestión proactiva, que incorpora optimización robusta con conjuntos de incertidumbre elipsoidales calibrados automáticamente y optimización estocástica con CVaR, reduce la tasa de bloqueo en 40.9%, la latencia promedio en 31.2%, la utilización de recursos mejora en 22.2% y el consumo energético disminuye en 26.1% frente a la gestión reactiva convencional. Los cinco algoritmos completos presentados —con sus condiciones de parada, estrategias de fallback y mecanismos de retroalimentación— forman un sistema directamente implementable en el contexto de Zero Touch Network Management [43].

La interpretabilidad de los pesos de atención, que revela patrones semánticamente significativos como correlación diaria y anticipación de picos, incrementa la confiabilidad del sistema y facilita la auditoría de decisiones autónomas de gestión, un aspecto crítico para la adopción en entornos operacionales regulados. Las contribuciones de este trabajo establecen una base sólida para la extensión hacia redes 6G, aprendizaje federado y sistemas de gestión autónoma de mayor escala.

---

## REFERENCIAS

[1] M. Shafi et al., "5G: A Tutorial Overview of Standards, Trials, Challenges, Deployment, and Practice," *IEEE J. Sel. Areas Commun.*, vol. 35, no. 6, pp. 1201–1221, Jun. 2017, doi: 10.1109/JSAC.2017.2692307.

[2] P. Popovski et al., "5G Wireless Network Slicing for eMBB, URLLC, and mMTC: A Communication-Theoretic View," *IEEE Access*, vol. 6, pp. 55765–55779, 2018, doi: 10.1109/ACCESS.2018.2872781.

[3] J. G. Andrews et al., "What Will 5G Be?," *IEEE J. Sel. Areas Commun.*, vol. 32, no. 6, pp. 1065–1082, Jun. 2014, doi: 10.1109/JSAC.2014.2328098.

[4] X. Foukas et al., "Network Slicing in 5G: Survey and Challenges," *IEEE Commun. Mag.*, vol. 55, no. 5, pp. 94–100, May 2017, doi: 10.1109/MCOM.2017.1600951.

[5] G. Durisi et al., "Toward Massive, Ultrareliable, and Low-Latency Wireless Communication With Short Packets," *Proc. IEEE*, vol. 104, no. 9, pp. 1711–1726, Sep. 2016, doi: 10.1109/JPROC.2016.2537298.

[6] M. Bennis et al., "Ultrareliable and Low-Latency Wireless Communication: Tail, Risk, and Scale," *Proc. IEEE*, vol. 106, no. 10, pp. 1834–1853, Oct. 2018, doi: 10.1109/JPROC.2018.2867029.

[7] C. Zhang et al., "Data-Driven Proactive Resource Allocation for 5G Networks," *IEEE Access*, vol. 7, pp. 147723–147738, 2019, doi: 10.1109/ACCESS.2019.2946491.

[8] N. Jiang et al., "Deep Learning for Traffic Prediction and Resource Allocation in 5G Networks," *IEEE Trans. Veh. Technol.*, vol. 69, no. 11, pp. 13530–13544, Nov. 2020, doi: 10.1109/TVT.2020.3025604.

[9] Y. Huang et al., "Mobile Traffic Prediction Using LSTM with Attention Mechanism," in *Proc. IEEE WCSP*, 2019, pp. 1–6.

[10] R. Trinh et al., "Mobile Traffic Prediction from Raw Data Using LSTM Networks," in *Proc. IEEE PIMRC*, 2018, pp. 1827–1832.

[11] S. Hochreiter and J. Schmidhuber, "Long Short-Term Memory," *Neural Comput.*, vol. 9, no. 8, pp. 1735–1780, Nov. 1997, doi: 10.1162/neco.1997.9.8.1735.

[12] Y. Bengio et al., "Learning Long-Term Dependencies with Gradient Descent is Difficult," *IEEE Trans. Neural Netw.*, vol. 5, no. 2, pp. 157–166, Mar. 1994, doi: 10.1109/72.279181.

[13] R. Pascanu et al., "On the difficulty of training recurrent neural networks," in *Proc. ICML*, 2013, pp. 1310–1318.

[14] K. Cho et al., "Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation," in *Proc. EMNLP*, 2014, pp. 1724–1734.

[15] D. Bahdanau et al., "Neural Machine Translation by Jointly Learning to Align and Translate," in *Proc. ICLR*, 2015.

[16] D. P. Kingma and J. Ba, "Adam: A Method for Stochastic Optimization," in *Proc. ICLR*, 2015.

[17] N. Srivastava et al., "Dropout: A simple way to prevent neural networks from overfitting," *J. Mach. Learn. Res.*, vol. 15, no. 1, pp. 1929–1958, 2014.

[18] K. Greff et al., "LSTM: A Search Space Odyssey," *IEEE Trans. Neural Netw. Learn. Syst.*, vol. 28, no. 10, pp. 2222–2232, Oct. 2017, doi: 10.1109/TNNLS.2016.2582924.

[19] F. A. Gers et al., "Learning to Forget: Continual Prediction with LSTM," *Neural Comput.*, vol. 12, no. 10, pp. 2451–2471, Oct. 2000, doi: 10.1162/089976600300015015.

[20] K. He et al., "Deep Residual Learning for Image Recognition," in *Proc. IEEE CVPR*, 2016, pp. 770–778, doi: 10.1109/CVPR.2016.90.

[21] J. L. Ba et al., "Layer Normalization," *arXiv:1607.06450*, 2016.

[22] M. Schuster and K. K. Paliwal, "Bidirectional Recurrent Neural Networks," *IEEE Trans. Signal Process.*, vol. 45, no. 11, pp. 2673–2681, Nov. 1997, doi: 10.1109/78.650093.

[23] R. J. Hyndman and G. Athanasopoulos, *Forecasting: Principles and Practice*, 2nd ed. OTexts, 2018.

[24] G. E. P. Box et al., *Time Series Analysis: Forecasting and Control*, 5th ed. Wiley, 2015.

[25] J. Navarro-Ortiz et al., "A Survey on 5G Usage Scenarios and Traffic Models," *IEEE Commun. Surveys Tuts.*, vol. 22, no. 2, pp. 905–929, Second Quarter 2020, doi: 10.1109/COMST.2019.2963698.

[26] G. Barlacchi et al., "A multi-source dataset of urban life in the city of Milan and the Province of Trentino," *Sci. Data*, vol. 2, no. 1, pp. 1–15, Oct. 2015, doi: 10.1038/sdata.2015.55.

[27] H. Abou-zeid et al., "Cellular Traffic Prediction and Classification: A Comparative Evaluation of LSTM and ARIMA," in *Proc. IEEE CAMAD*, 2020, pp. 1–6.

[28] F. Xu et al., "Big Data Driven Mobile Traffic Understanding and Forecasting: A Time Series Approach," *IEEE Trans. Services Comput.*, vol. 9, no. 5, pp. 796–805, Sep.–Oct. 2016, doi: 10.1109/TSC.2016.2599503.

[29] 3GPP TS 23.288, "Architecture enhancements for 5G System (5GS) to support network data analytics services," Release 16, Dec. 2019.

[30] I. Sutskever et al., "Sequence to Sequence Learning with Neural Networks," in *Proc. NIPS*, 2014, pp. 3104–3112.

[31] A. Vaswani et al., "Attention is all you need," in *Proc. NIPS*, 2017, pp. 5998–6008.

[32] M.-T. Luong et al., "Effective Approaches to Attention-based Neural Machine Translation," in *Proc. EMNLP*, 2015, pp. 1412–1421.

[33] Y. Qin et al., "A Dual-Stage Attention-Based Recurrent Neural Network for Time Series Prediction," in *Proc. IJCAI*, 2017, pp. 2627–2633.

[34] X. Shi et al., "Convolutional LSTM Network: A Machine Learning Approach for Precipitation Nowcasting," in *Proc. NIPS*, 2015, pp. 802–810.

[35] Y. Zhang et al., "Network Traffic Prediction Based on LSTM Networks with Genetic Algorithm," in *Proc. IEEE TrustCom*, 2019, pp. 643–648.

[36] R. B. Cleveland et al., "STL: A Seasonal-Trend Decomposition Procedure Based on Loess," *J. Off. Stat.*, vol. 6, no. 1, pp. 3–73, 1990.

[37] S. Ben Taieb et al., "A review and comparison of strategies for multi-step ahead time series forecasting," *Expert Syst. Appl.*, vol. 39, no. 8, pp. 7067–7083, Jun. 2012, doi: 10.1016/j.eswa.2012.01.039.

[38] P. Rost et al., "Network Slicing to Enable Scalability and Flexibility in 5G Mobile Networks," *IEEE Commun. Mag.*, vol. 55, no. 5, pp. 72–79, May 2017, doi: 10.1109/MCOM.2017.1600920.

[39] A. Ben-Tal et al., *Robust Optimization*. Princeton Univ. Press, 2009.

[40] J. R. Birge and F. Louveaux, *Introduction to Stochastic Programming*, 2nd ed. Springer, 2011.

[41] R. Li et al., "Deep Reinforcement Learning for Resource Management in Network Slicing," *IEEE Access*, vol. 6, pp. 74429–74441, 2018, doi: 10.1109/ACCESS.2018.2885583.

[42] V. Mnih et al., "Human-level control through deep reinforcement learning," *Nature*, vol. 518, no. 7540, pp. 529–533, Feb. 2015, doi: 10.1038/nature14236.

[43] C. Benzaid and T. Taleb, "AI-Driven Zero Touch Network and Service Management in 5G and Beyond: Challenges and Research Directions," *IEEE Netw.*, vol. 34, no. 2, pp. 186–194, Mar./Apr. 2020, doi: 10.1109/MNET.001.1900252.

[44] R. J. Hyndman and A. B. Koehler, "Another look at measures of forecast accuracy," *Int. J. Forecasting*, vol. 22, no. 4, pp. 679–688, Oct.–Dec. 2006, doi: 10.1016/j.ijforecast.2006.03.001.

[45] L. Breiman, "Random Forests," *Mach. Learn.*, vol. 45, no. 1, pp. 5–32, Oct. 2001, doi: 10.1023/A:1010933404324.

[46] A. J. Smola and B. Schölkopf, "A tutorial on support vector regression," *Stat. Comput.*, vol. 14, no. 3, pp. 199–222, Aug. 2004, doi: 10.1023/B:STCO.0000035301.49549.88.

[47] R. J. Hyndman and Y. Khandakar, "Automatic Time Series Forecasting: The forecast Package for R," *J. Stat. Softw.*, vol. 27, no. 3, pp. 1–22, 2008, doi: 10.18637/jss.v027.i03.

[48] M. Giordani et al., "Toward 6G Networks: Use Cases and Technologies," *IEEE Commun. Mag.*, vol. 58, no. 3, pp. 55–61, Mar. 2020, doi: 10.1109/MCOM.001.1900411.

[49] S. J. Pan and Q. Yang, "A Survey on Transfer Learning," *IEEE Trans. Knowl. Data Eng.*, vol. 22, no. 10, pp. 1345–1359, Oct. 2010, doi: 10.1109/TKDE.2009.191.

[50] J. Konečný et al., "Federated Learning: Strategies for Improving Communication Efficiency," *arXiv:1610.05492*, 2016.
