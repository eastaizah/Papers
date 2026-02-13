# Inteligencia Artificial Nativa en el Nivel Físico de Redes 6G: Fundamentos, Arquitecturas y Perspectivas

---

**Abstract**—La sexta generación de redes móviles (6G) representa un cambio paradigmático en la concepción de sistemas de comunicación inalámbrica, donde la Inteligencia Artificial (IA) no se integra como una característica adicional, sino que se concibe como un componente nativo y fundamental del nivel físico (PHY). Este artículo presenta un análisis exhaustivo de la IA nativa en el nivel físico de 6G, abordando sus fundamentos teóricos, arquitecturas propuestas, algoritmos de aprendizaje, desafíos de implementación y direcciones futuras de investigación [1], [2]. Se examina en detalle la transformación de bloques funcionales tradicionales del nivel físico mediante técnicas de aprendizaje profundo, incluyendo codificación de canal, estimación de canal, detección de señales, conformación de haces (beamforming) y gestión de recursos radio [3], [4]. Se presenta el marco matemático riguroso que sustenta estos desarrollos, incluyendo formulaciones de optimización, análisis de convergencia, y caracterización de rendimiento teórico. Los resultados demuestran que la IA nativa en el nivel físico no solo mejora métricas de rendimiento convencionales, sino que habilita capacidades emergentes esenciales para 6G, como comunicaciones semánticas, adaptación predictiva al entorno, y operación en regímenes de complejidad computacional previamente inaccesibles [5], [6].

**Index Terms**—6G, Inteligencia Artificial Nativa, Nivel Físico, Aprendizaje Profundo, Codificación Neural, Estimación de Canal, Beamforming Inteligente, Optimización End-to-End, Redes Neuronales Profundas.

---

## I. INTRODUCCIÓN

### A. Contexto y Motivación

La evolución de las redes móviles ha seguido un patrón consistente de incremento en las capacidades de transmisión de datos, reducción de latencia y soporte de mayor densidad de dispositivos conectados [1]. Desde la primera generación (1G) enfocada en comunicaciones de voz analógicas, hasta la quinta generación (5G) que habilita casos de uso como comunicaciones ultra-confiables de baja latencia (URLLC) y comunicaciones masivas tipo máquina (mMTC), cada generación ha respondido a demandas crecientes de la sociedad digital [2].

Sin embargo, las proyecciones para la década de 2030 plantean requisitos que trascienden las capacidades de 5G y sus evoluciones previstas (5G-Advanced) [3]. Se anticipa la necesidad de soportar tasas de datos del orden de terabits por segundo (Tbps), latencias sub-milisegundo con confiabilidad extrema (99.99999%), conectividad ubicua tridimensional (terrestre, aérea y submarina), integración de comunicaciones y sensado (ISAC - Integrated Sensing and Communications), y soporte de aplicaciones emergentes como realidad extendida (XR) de ultra-alta fidelidad, internet táctil, y gemelos digitales distribuidos en tiempo real [4], [5].

Estos requisitos plantean desafíos fundamentales que no pueden ser abordados mediante la extrapolación incremental de tecnologías actuales [6]. Las arquitecturas tradicionales del nivel físico, basadas en procesamiento de señales algorítmico con diseño específico para modelos de canal y escenarios particulares, muestran limitaciones inherentes en términos de adaptabilidad, escalabilidad y eficiencia espectral en entornos complejos y dinámicos [7].

En este contexto, la Inteligencia Artificial (IA), y específicamente el aprendizaje profundo (Deep Learning, DL), emerge como un paradigma transformador [8]. A diferencia de aproximaciones previas donde la IA se aplicaba para optimizar parámetros o gestionar recursos en capas superiores, el concepto de **IA Nativa en el Nivel Físico** propone una reformulación fundamental: los bloques funcionales del PHY se diseñan, desde su concepción, como sistemas de aprendizaje automático que aprenden representaciones óptimas directamente de los datos, sin depender de modelos analíticos simplificados [9], [10].

### B. Estado del Arte y Evolución Conceptual

La aplicación de técnicas de aprendizaje automático a comunicaciones inalámbricas tiene antecedentes en investigaciones sobre redes neuronales aplicadas a ecualización, detección y modulación desde la década de 1990 [11]. Sin embargo, estas aproximaciones tempranas estaban limitadas por la capacidad computacional disponible, la falta de grandes volúmenes de datos de entrenamiento, y arquitecturas de redes neuronales relativamente simples.

El resurgimiento del interés en IA para comunicaciones, iniciado alrededor de 2016-2017, fue catalizado por varios factores convergentes [12], [13]:

1. **Avances en Aprendizaje Profundo**: El desarrollo de arquitecturas sofisticadas (redes convolucionales profundas, redes recurrentes con mecanismos de atención, transformers) y técnicas de entrenamiento robustas (normalización por lotes, optimizadores adaptativos, regularización avanzada) [14].

2. **Disponibilidad de Recursos Computacionales**: La proliferación de unidades de procesamiento gráfico (GPUs) y procesadores especializados (TPUs, NPUs) que aceleran dramáticamente el entrenamiento e inferencia de modelos complejos [15].

3. **Datos y Simulaciones**: Capacidad para generar grandes datasets sintéticos de señales de comunicación bajo diversas condiciones de canal, así como datasets de mediciones reales de propagación [16].

4. **Límites Teóricos de Aproximaciones Tradicionales**: Reconocimiento de que en escenarios complejos (canales con múltiples dispersores, interferencia no-gaussiana, entornos no-estacionarios), las soluciones basadas en modelos analíticos simplificados están significativamente sub-optimizadas [17].

Los trabajos pioneros de O'Shea y Hoydis introdujeron el concepto de **autoencoder para comunicaciones end-to-end**, donde tanto el transmisor como el receptor se implementan como redes neuronales entrenadas conjuntamente para minimizar una función de pérdida relacionada con la tasa de error [18], [19]. Esta aproximación demostró que sistemas neuronales podían aprender esquemas de modulación y codificación competitivos con diseños tradicionales, y en algunos casos, descubrir soluciones no-convencionales con mejor rendimiento.

Posteriormente, la investigación se expandió hacia componentes específicos del nivel físico [20]:

- **Codificación de Canal Neural**: Reemplazo de códigos tradicionales (Turbo, LDPC, Polar) por autoencoders con propiedades de corrección de errores aprendidas [21].
- **Estimación y Ecualización de Canal**: Uso de redes neuronales recurrentes (RNN) y convolucionales (CNN) para estimar respuestas de canal y cancelar interferencia [22].
- **Beamforming y Conformación de Haces**: Aplicación de aprendizaje por refuerzo (RL) y redes profundas para optimizar pesos de antena en sistemas MIMO masivo [23].
- **Detección Multi-Usuario**: Algoritmos de aprendizaje supervisado para aproximar detectores óptimos (ML, MAP) con complejidad reducida [24].

Para 6G, el concepto evoluciona hacia **IA Nativa**, donde [25], [26]:

1. La IA no es un complemento, sino el principio de diseño fundamental.
2. Los modelos se entrenan con datos multi-modales (señales RF, contexto espacial, información semántica).
3. El aprendizaje es continuo y adaptativo durante la operación.
4. La arquitectura del PHY es holística y optimizada end-to-end, no como concatenación de bloques independientes.

### C. Objetivos y Contribuciones del Artículo

Este artículo presenta una revisión exhaustiva y original del estado del arte en IA nativa para el nivel físico de 6G, con las siguientes contribuciones principales [27]:

1. **Marco Teórico Unificado**: Desarrollo de un formalismo matemático riguroso que caracteriza el problema de optimización end-to-end del nivel físico como un problema de aprendizaje de representaciones con restricciones físicas y de información [28].

2. **Análisis Detallado de Arquitecturas**: Descripción pormenorizada de arquitecturas de redes neuronales específicamente diseñadas para componentes del PHY, incluyendo análisis de complejidad computacional, requisitos de memoria, y consideraciones de implementación en hardware [29].

3. **Fundamentos Matemáticos**: Presentación explícita de las formulaciones de optimización, derivaciones de gradientes, análisis de convergencia, y caracterización de límites teóricos de rendimiento [30].

4. **Evaluación Comparativa**: Comparación cuantitativa entre aproximaciones basadas en IA y métodos tradicionales del nivel físico, bajo diversas métricas de rendimiento y condiciones operativas [31].

5. **Desafíos Abiertos y Direcciones Futuras**: Identificación de problemas de investigación no resueltos y propuestas de líneas de desarrollo para la próxima década [32].

### D. Organización del Artículo

El resto del artículo se estructura de la siguiente manera: La Sección II establece los fundamentos teóricos de la IA nativa en el nivel físico, incluyendo teoría de la información, aprendizaje de representaciones y formulación del problema de optimización. La Sección III examina en detalle la aplicación de IA a componentes individuales del PHY (codificación, estimación de canal, detección, beamforming). La Sección IV presenta arquitecturas de sistemas end-to-end y optimización conjunta. La Sección V discute aspectos de implementación práctica y complejidad computacional. La Sección VI analiza desafíos pendientes incluyendo generalización, interpretabilidad y seguridad. Finalmente, la Sección VII presenta conclusiones y direcciones futuras.

---

## II. FUNDAMENTOS TEÓRICOS DE IA NATIVA EN EL NIVEL FÍSICO

### A. Modelo del Sistema de Comunicación

Consideremos un sistema de comunicación digital donde un mensaje fuente $\mathbf{s} \in \mathcal{S}$ de dimensión $k$ debe ser transmitido desde un transmisor (Alice) a un receptor (Bob) a través de un canal de comunicación inalámbrico [33]. En el paradigma tradicional, este proceso se descompone en bloques funcionales discretos que operan de manera secuencial y independiente.

#### 1) Cadena de Procesamiento Convencional

La arquitectura tradicional del nivel físico comprende las siguientes etapas de procesamiento [34]:

1. **Codificación de Fuente**: Compresión del mensaje original mediante una transformación $\mathbf{s} \rightarrow \mathbf{b}$ donde $\mathbf{b} \in \{0,1\}^{k'}$. Esta operación elimina redundancia inherente en la fuente para reducir la tasa de transmisión requerida.

2. **Codificación de Canal**: Introducción de redundancia estructurada $\mathbf{b} \rightarrow \mathbf{c}$ donde $\mathbf{c} \in \{0,1\}^{n}$ con $n > k'$. La redundancia añadida permite la detección y corrección de errores introducidos por el canal de comunicación.

3. **Modulación**: Mapeo de bits codificados a símbolos complejos del espacio de señal $\mathbf{c} \rightarrow \mathbf{x}$ donde $\mathbf{x} \in \mathbb{C}^{M}$. Esta transformación prepara la señal digital para transmisión analógica sobre el medio físico.

4. **Propagación por Canal**: La señal transmitida experimenta distorsión lineal y adición de ruido modelada como:
$$\mathbf{y} = \mathbf{H}\mathbf{x} + \mathbf{n}$$
donde $\mathbf{H} \in \mathbb{C}^{N_r \times N_t}$ representa la matriz de canal MIMO (Multiple-Input Multiple-Output) que caracteriza la respuesta entre $N_t$ antenas transmisoras y $N_r$ antenas receptoras, y $\mathbf{n} \sim \mathcal{CN}(0, \sigma^2\mathbf{I})$ denota el ruido aditivo gaussiano complejo circularmente simétrico con varianza $\sigma^2$ por dimensión [35].

5. **Demodulación**: Estimación de símbolos codificados a partir de la señal recibida $\mathbf{y} \rightarrow \hat{\mathbf{c}}$. Esta operación invierte el mapeo de modulación, produciendo estimaciones blandas (log-likelihood ratios) o duras (bits decididos).

6. **Decodificación de Canal**: Corrección de errores mediante algoritmos específicos del código utilizado $\hat{\mathbf{c}} \rightarrow \hat{\mathbf{b}}$. Ejemplos incluyen el algoritmo de Viterbi para códigos convolucionales, belief propagation para códigos LDPC, o decodificación sucesiva de cancelación para códigos Polar.

7. **Decodificación de Fuente**: Reconstrucción del mensaje original $\hat{\mathbf{b}} \rightarrow \hat{\mathbf{s}}$ mediante reversión de la compresión aplicada en el transmisor.

#### 2) Limitaciones del Paradigma Tradicional

El diseño modular del nivel físico, si bien matemáticamente elegante, introduce varias limitaciones fundamentales [36]:

**Teorema de Separación y Sus Restricciones**: El teorema de separación de Shannon establece que, bajo condiciones idealizadas, la codificación de fuente y canal pueden diseñarse independientemente sin pérdida de optimalidad. Formalmente, para una fuente con entropía $H(S)$ y un canal con capacidad $C$, es posible transmitir confiablemente si y solo si $H(S) < C$, y este resultado es alcanzable mediante diseño separado [37]. Sin embargo, este resultado fundamental asume:

- Información de estado de canal (CSI) perfecta y completa en el receptor
- Longitudes de código arbitrariamente largas (equivalente a latencia infinita)
- Canales ergódicos, estacionarios y sin memoria
- Ausencia de restricciones de complejidad computacional

En escenarios reales de 6G, particularmente en aplicaciones de comunicaciones ultra-confiables de baja latencia (URLLC), estas suposiciones se violan sistemáticamente. La latencia objetivo de fracciones de milisegundo impone longitudes de código cortas, donde la brecha entre rendimiento teórico y práctico se amplifica significativamente.

**Modelos Paramétricos de Canal**: Los diseños tradicionales optimizan el rendimiento bajo modelos de canal específicos como desvanecimiento Rayleigh (dispersión rica sin línea de vista), Rician (componente especular dominante), o modelos tapped-delay line con perfiles de retardo exponenciales. El rendimiento degrada considerablemente cuando las características reales del canal difieren de las suposiciones de diseño, situación común en entornos dinámicos y heterogéneos de 6G [38].

**Optimización por Componentes**: Cada bloque funcional se optimiza según un criterio local. Por ejemplo, los códigos de canal maximizan la distancia mínima de Hamming, los ecualizadores minimizan el error cuadrático medio (MSE), y los detectores maximizan la probabilidad a posteriori. Esta optimización local no garantiza optimalidad del sistema end-to-end en presencia de restricciones de recursos compartidos y objetivos de rendimiento multidimensionales [39].

#### 3) Formulación de IA Nativa End-to-End

La aproximación de IA nativa propone un cambio paradigmático radical: reemplazar la cadena de procesamiento completa por dos funciones universales parametrizadas por redes neuronales profundas [40]:

$$f_{\theta}: \mathcal{S} \rightarrow \mathbb{C}^{M}, \quad g_{\phi}: \mathbb{C}^{N} \rightarrow \mathcal{S}$$

donde $f_{\theta}$ representa el transmisor (codificador neuronal) con parámetros $\theta \in \mathbb{R}^{p}$, y $g_{\phi}$ representa el receptor (decodificador neuronal) con parámetros $\phi \in \mathbb{R}^{q}$.

La señal transmitida se genera como una función no-lineal aprendida del mensaje:
$$\mathbf{x} = f_{\theta}(\mathbf{s})$$

Esta señal debe satisfacer una restricción de potencia promedio que refleja limitaciones físicas del transmisor:
$$\mathbb{E}_{\mathbf{s} \sim p(\mathbf{s})}[\|\mathbf{x}\|^2] = \mathbb{E}_{\mathbf{s}}[\|f_{\theta}(\mathbf{s})\|^2] \leq P$$
donde $P$ representa la potencia disponible y la esperanza se toma sobre la distribución de mensajes fuente $p(\mathbf{s})$.

La señal recibida, después de la propagación a través del canal físico $h(\cdot)$, se expresa como:
$$\mathbf{y} = h(f_{\theta}(\mathbf{s})) + \mathbf{n}$$

El receptor neuronal produce una estimación del mensaje original mediante:
$$\hat{\mathbf{s}} = g_{\phi}(\mathbf{y})$$

El entrenamiento conjunto de transmisor y receptor se formula como un problema de optimización end-to-end que minimiza una función de pérdida diferenciable [41]:

$$\min_{\theta, \phi} \mathbb{E}_{\mathbf{s} \sim p(\mathbf{s}), \mathbf{n} \sim p(\mathbf{n}), \mathbf{H} \sim p(\mathbf{H})} [\mathcal{L}(\mathbf{s}, g_{\phi}(h(f_{\theta}(\mathbf{s})) + \mathbf{n}))]$$

sujeto a: $\mathbb{E}_{\mathbf{s}}[\|f_{\theta}(\mathbf{s})\|^2] \leq P$

La función de pérdida $\mathcal{L}(\mathbf{s}, \hat{\mathbf{s}})$ cuantifica la discrepancia entre mensaje original y estimación. Para mensajes discretos, típicamente se emplea la entropía cruzada categórica:
$$\mathcal{L}_{\text{CE}}(\mathbf{s}, \hat{\mathbf{s}}) = -\sum_{i=1}^{|\mathcal{S}|} s_i \log(\hat{s}_i)$$

Para señales continuas, el error cuadrático medio es apropiado:
$$\mathcal{L}_{\text{MSE}}(\mathbf{s}, \hat{\mathbf{s}}) = \|\mathbf{s} - \hat{\mathbf{s}}\|^2$$

Esta formulación unificada elimina las fronteras artificiales entre bloques funcionales, permitiendo que el sistema aprenda representaciones y transformaciones óptimas para el objetivo de comunicación completo.

### B. Teoría de la Información y Límites Fundamentales

#### 1) Capacidad de Canal y Límite de Shannon

La teoría de la información establece límites fundamentales sobre las tasas de comunicación confiable alcanzables [42]. Para un canal AWGN escalar con potencia de transmisión $P$ y densidad espectral de potencia de ruido $N_0$ (en W/Hz), la capacidad de Shannon se expresa como:

$$C_{\text{AWGN}} = \frac{1}{2}\log_2\left(1 + \frac{P}{N_0 W}\right) \text{ bits/s}$$

donde $W$ es el ancho de banda en Hz. Alternativamente, en términos de eficiencia espectral (bits/s/Hz):

$$C_{\text{AWGN}} = \frac{1}{2}\log_2\left(1 + \text{SNR}\right) \text{ bits/s/Hz}$$

donde $\text{SNR} = P/(N_0 W)$ es la relación señal-ruido. Este resultado establece que para cualquier tasa $R < C$, existen códigos que permiten comunicación con probabilidad de error arbitrariamente pequeña conforme la longitud del código aumenta.

Para sistemas MIMO con $N_t$ antenas transmisoras y $N_r$ receptoras, cuando el receptor posee conocimiento perfecto de la matriz de canal $\mathbf{H}$ pero el transmisor no, la capacidad promedio (ergódica) sobre realizaciones de canal se expresa como [43]:

$$C_{\text{MIMO}} = \mathbb{E}_{\mathbf{H}}\left[\log_2\det\left(\mathbf{I}_{N_r} + \frac{P}{N_t \sigma^2}\mathbf{H}\mathbf{H}^H\right)\right]$$

donde $\mathbf{I}_{N_r}$ es la matriz identidad de dimensión $N_r$, $\sigma^2$ es la varianza del ruido por antena receptora, y la esperanza se toma sobre la distribución estadística del canal. El término $\det(\cdot)$ representa el determinante de la matriz, y la expresión refleja que la capacidad es la suma de las capacidades de los modos espaciales paralelos del canal MIMO.

Cuando tanto transmisor como receptor poseen CSI perfecta, la capacidad se maximiza mediante la técnica de water-filling sobre los valores singulares de $\mathbf{H}$. Descomponiendo $\mathbf{H} = \mathbf{U}\boldsymbol{\Sigma}\mathbf{V}^H$ mediante descomposición en valores singulares (SVD), donde $\boldsymbol{\Sigma} = \text{diag}(\sigma_1, \ldots, \sigma_r)$ con $r = \min(N_t, N_r)$, la capacidad con CSI bilateral es:

$$C_{\text{MIMO-CSIT}} = \sum_{i=1}^{r} \log_2\left(1 + \frac{\lambda_i \sigma_i^2}{\sigma^2}\right)$$

donde $\lambda_i$ son los coeficientes óptimos de asignación de potencia determinados por el algoritmo de water-filling:
$$\lambda_i = \left[\mu - \frac{\sigma^2}{\sigma_i^2}\right]^+$$
con $[\cdot]^+ = \max(0, \cdot)$ y $\mu$ escogido para satisfacer $\sum_{i=1}^{r}\lambda_i = P$.

#### 2) Límites de Rendimiento para Códigos de Longitud Finita

La teoría clásica de Shannon caracteriza el rendimiento asintótico cuando la longitud de bloque $n \rightarrow \infty$. Sin embargo, para aplicaciones URLLC en 6G con latencias sub-milisegundo, se requieren bloques cortos (típicamente $n < 200$ símbolos). Polyanskiy, Poor y Verdú derivaron caracterizaciones precisas del rendimiento no-asintótico [44].

Para un canal AWGN con SNR dado, la probabilidad de error de bloque $P_e$ para un código óptimo de tasa $R = k/n$ (transmitiendo $k$ bits en $n$ usos de canal) está acotada inferiormente por:

$$P_e \geq Q\left(\frac{nC - k}{\sqrt{n V}} + \frac{\log n}{2\sqrt{n V}}\right) + o\left(\frac{1}{\sqrt{n}}\right)$$

donde $Q(x) = \frac{1}{\sqrt{2\pi}}\int_x^{\infty}e^{-t^2/2}dt$ es la función Q complementaria (cola de la distribución normal estándar), $C$ es la capacidad del canal, y $V$ es la **dispersión del canal**, una cantidad que caracteriza las fluctuaciones de segundo orden en la información mutua.

Para el canal AWGN, la dispersión se calcula como:
$$V_{\text{AWGN}} = \frac{1}{2}\left(\log_2 e\right)^2 \left(\frac{(1+\text{SNR})^2}{\text{SNR}}\right)$$

Esta expresión revela que para bloques cortos, existe una penalización en la tasa alcanzable que escala como $\mathcal{O}(1/\sqrt{n})$. Para mantener una probabilidad de error objetivo $\epsilon$, la tasa máxima alcanzable es aproximadamente:

$$R^*(n, \epsilon) \approx C - \sqrt{\frac{V}{n}}Q^{-1}(\epsilon)$$

Esta caracterización de rendimiento de código finito es crítica para el diseño de sistemas 6G-URLLC, donde se debe operar en el régimen de bloques cortos con alta confiabilidad ($\epsilon \sim 10^{-6}$ o menor) [45].

#### 3) Representación de Información y Cuello de Botella (Information Bottleneck)

El principio del Information Bottleneck (IB) proporciona un marco teórico fundamental para caracterizar representaciones óptimas en presencia de limitaciones de dimensionalidad [46]. Consideremos un par de variables aleatorias $(X, Y)$ donde $X$ representa la observación (entrada) y $Y$ la variable objetivo (salida relevante). Buscamos construir una representación comprimida $T = f(X)$ que satisface dos objetivos en conflicto:

1. Minimizar la información mutua $I(X; T)$ (maximizar compresión)
2. Maximizar la información mutua $I(T; Y)$ (preservar información relevante)

El problema de optimización del IB se formula como:

$$\min_{p(t|x)} \mathcal{F}(p(t|x)) = I(X; T) - \beta I(T; Y)$$

donde $\beta > 0$ es un parámetro de Lagrange que controla el trade-off entre compresión y preservación de información relevante. La solución óptima caracteriza la **frontera de información** del sistema, análoga a la frontera de Pareto en optimización multi-objetivo.

Mediante cálculo variacional, la distribución óptima $p^*(t|x)$ satisface:

$$p^*(t|x) = \frac{p(t)}{Z(x, \beta)}\exp\left(\beta \sum_y p(y|x)\log\frac{p(y|t)}{p(y)}\right)$$

donde $Z(x, \beta) = \sum_t p(t)\exp(\beta D_{\text{KL}}[p(y|x) \| p(y|t)])$ es la función de partición normalizadora, y $D_{\text{KL}}$ denota la divergencia de Kullback-Leibler.

En el contexto de comunicaciones inalámbricas, el IB proporciona un principio fundamental para el diseño de transceptores neuronales [47]:

- $X$: Mensaje fuente $\mathbf{s}$
- $T$: Señal transmitida $\mathbf{x} = f_{\theta}(\mathbf{s})$ (con restricciones de potencia/dimensionalidad)
- $Y$: Variable que representa la información necesaria para decodificación en el receptor

El óptimo del IB caracteriza la frontera fundamental entre compresión (limitaciones de recursos físicos) y recuperabilidad (capacidad de decodificación confiable). Tishby y colaboradores propusieron que las redes neuronales profundas, durante el entrenamiento, progresan naturalmente hacia representaciones que aproximan el óptimo del IB: las primeras capas comprimen la entrada eliminando información irrelevante, mientras las últimas capas refinan características relevantes para la tarea objetivo.

#### 4) Tasa de Distorsión y Codificación Conjunta Fuente-Canal

La teoría de tasa-distorsión cuantifica el trade-off fundamental entre compresión y fidelidad de reconstrucción [48]. Para una fuente aleatoria $S$ con distribución $p(s)$ y una medida de distorsión $d(s, \hat{s})$ que cuantifica el error de reconstrucción, la función de tasa-distorsión $R(D)$ se define como:

$$R(D) = \min_{p(\hat{s}|s): \mathbb{E}[d(S,\hat{S})] \leq D} I(S; \hat{S})$$

Esta función caracteriza la mínima tasa de información (en bits) requerida para representar la fuente tal que la distorsión promedio esperada no exceda $D$. Para fuentes gaussianas con distorsión cuadrática, la función de tasa-distorsión tiene forma cerrada:

$$R(D) = \begin{cases}
\frac{1}{2}\log_2\frac{\sigma_S^2}{D} & \text{si } D \leq \sigma_S^2 \\
0 & \text{si } D > \sigma_S^2
\end{cases}$$

donde $\sigma_S^2$ es la varianza de la fuente gaussiana.

El teorema de separación de Shannon justifica el diseño independiente de codificación de fuente (compresión) y codificación de canal (protección contra errores) bajo condiciones idealizadas. Sin embargo, para canales con desvanecimiento, retroalimentación limitada, o restricciones estrictas de latencia, la **codificación conjunta fuente-canal (JSCC)** puede superar significativamente las aproximaciones separadas [49].

La formulación de optimización para JSCC es:
$$\min_{f, g} \mathbb{E}[d(S, g(h(f(S))))]$$
sujeto a restricciones de potencia, ancho de banda y complejidad.

Notablemente, esta formulación coincide estructuralmente con el problema de optimización end-to-end para transceptores neuronales. Los autoencoders profundos implementan naturalmente JSCC óptima: el encoder aprende a comprimir la fuente mientras añade redundancia adaptada al canal, y el decoder realiza descompresión y corrección de errores de manera conjunta. Esta conexión fundamental sugiere que la IA nativa en el nivel físico no solo es una aproximación práctica, sino que está alineada con principios teóricos fundamentales de comunicación óptima [50].

### C. Aprendizaje de Representaciones y Redes Neuronales Profundas

#### 1) Arquitecturas Fundamentales para el Nivel Físico

**Perceptrón Multicapa (MLP)**: La arquitectura neuronal más básica consiste en capas completamente conectadas (fully-connected) donde cada neurona en la capa $l$ está conectada a todas las neuronas en la capa $l+1$ [51]. La transformación de activaciones entre capas se expresa como:

$$\mathbf{h}^{(l+1)} = \sigma\left(\mathbf{W}^{(l)}\mathbf{h}^{(l)} + \mathbf{b}^{(l)}\right)$$

donde:
- $\mathbf{h}^{(l)} \in \mathbb{R}^{n_l}$ representa el vector de activaciones de la capa $l$
- $\mathbf{W}^{(l)} \in \mathbb{R}^{n_{l+1} \times n_l}$ es la matriz de pesos sinápticos
- $\mathbf{b}^{(l)} \in \mathbb{R}^{n_{l+1}}$ es el vector de sesgos
- $\sigma(\cdot)$ es una función de activación no-lineal aplicada elemento a elemento

Las funciones de activación comunes incluyen:
- ReLU (Rectified Linear Unit): $\sigma(z) = \max(0, z)$
- Tanh: $\sigma(z) = \tanh(z) = \frac{e^z - e^{-z}}{e^z + e^{-z}}$
- Sigmoid: $\sigma(z) = \frac{1}{1 + e^{-z}}$

El teorema de aproximación universal de Cybenko (1989) y Hornik (1991) establece que una red neuronal con una sola capa oculta suficientemente ancha puede aproximar cualquier función continua en un compacto con precisión arbitraria. Formalmente, para cualquier función continua $f: \mathbb{R}^n \rightarrow \mathbb{R}$ y $\epsilon > 0$, existe una red con activaciones sigmoidales y suficientes neuronas ocultas tal que $\|f(x) - \hat{f}(x)\| < \epsilon$ para todo $x$ en un dominio compacto.

Sin embargo, para funciones complejas de alta dimensionalidad, las redes profundas (múltiples capas ocultas) son exponencialmente más eficientes en términos de número de parámetros requeridos que redes superficiales anchas [52].

**Redes Convolucionales (CNN)**: Las CNNs explotan estructura espacial o temporal mediante operaciones de convolución que comparten pesos sobre la dimensión espacial/temporal [53]. Para señales unidimensionales (relevante para formas de onda en el tiempo):

$$\mathbf{h}^{(l+1)}_{i} = \sigma\left(\sum_{j=-k}^{k} \mathbf{w}^{(l)}_{j} \cdot \mathbf{h}^{(l)}_{i+j} + b^{(l)}\right)$$

donde $\mathbf{w}^{(l)}_j$ son los pesos del filtro convolucional (kernel) de tamaño $2k+1$, y $\cdot$ denota producto escalar cuando las activaciones son vectoriales (múltiples canales).

Las ventajas de las CNNs para procesamiento de señales incluyen:
- **Invarianza traslacional**: Detectan patrones independientemente de su posición en la señal
- **Jerarquía de características**: Capas iniciales aprenden características locales (bordes, transiciones), capas profundas combinan estas en patrones complejos
- **Eficiencia paramétrica**: Compartir pesos reduce dramáticamente el número de parámetros comparado con capas completamente conectadas

Para procesamiento de formas de onda I/Q complejas, espectrogramas o matrices de canal espacio-temporales, las CNNs bidimensionales son apropiadas con kernels $\mathbf{W}^{(l)} \in \mathbb{R}^{C_{out} \times C_{in} \times k_h \times k_w}$ donde $C_{in}, C_{out}$ son números de canales de entrada y salida, y $k_h, k_w$ son dimensiones del kernel.

**Redes Recurrentes (RNN) y LSTM**: Las RNNs procesan secuencias manteniendo un estado oculto que se actualiza recursivamente [54]:

$$\mathbf{h}_t = \sigma_h(\mathbf{W}_{hh}\mathbf{h}_{t-1} + \mathbf{W}_{xh}\mathbf{x}_t + \mathbf{b}_h)$$
$$\mathbf{y}_t = \sigma_y(\mathbf{W}_{hy}\mathbf{h}_t + \mathbf{b}_y)$$

donde $\mathbf{x}_t$ es la entrada en el instante $t$, $\mathbf{h}_t$ el estado oculto, $\mathbf{y}_t$ la salida, $\mathbf{W}_{hh}, \mathbf{W}_{xh}, \mathbf{W}_{hy}$ son matrices de pesos, y $\sigma_h, \sigma_y$ funciones de activación.

Las RNNs básicas sufren del problema de **gradientes que desaparecen** durante el entrenamiento con backpropagation through time (BPTT), limitando su capacidad de capturar dependencias de largo plazo. Las redes Long Short-Term Memory (LSTM) mitigan este problema mediante una arquitectura con compuertas (gates) que controlan el flujo de información [55]:

$$\mathbf{f}_t = \sigma_g(\mathbf{W}_f\mathbf{x}_t + \mathbf{U}_f\mathbf{h}_{t-1} + \mathbf{b}_f)$$
$$\mathbf{i}_t = \sigma_g(\mathbf{W}_i\mathbf{x}_t + \mathbf{U}_i\mathbf{h}_{t-1} + \mathbf{b}_i)$$
$$\mathbf{o}_t = \sigma_g(\mathbf{W}_o\mathbf{x}_t + \mathbf{U}_o\mathbf{h}_{t-1} + \mathbf{b}_o)$$
$$\tilde{\mathbf{c}}_t = \sigma_c(\mathbf{W}_c\mathbf{x}_t + \mathbf{U}_c\mathbf{h}_{t-1} + \mathbf{b}_c)$$
$$\mathbf{c}_t = \mathbf{f}_t \odot \mathbf{c}_{t-1} + \mathbf{i}_t \odot \tilde{\mathbf{c}}_t$$
$$\mathbf{h}_t = \mathbf{o}_t \odot \sigma_h(\mathbf{c}_t)$$

donde:
- $\mathbf{f}_t$: Compuerta de olvido (forget gate) - controla qué información del estado de celda previo se retiene
- $\mathbf{i}_t$: Compuerta de entrada (input gate) - controla qué nueva información se añade al estado de celda
- $\mathbf{o}_t$: Compuerta de salida (output gate) - controla qué parte del estado de celda se expone como salida
- $\mathbf{c}_t$: Estado de celda (cell state) - memoria interna de largo plazo
- $\odot$: Producto de Hadamard (elemento a elemento)
- $\sigma_g$: Típicamente sigmoid (salidas en [0,1])
- $\sigma_c, \sigma_h$: Típicamente tanh (salidas en [-1,1])

Las LSTMs son particularmente adecuadas para:
- Estimación de canal variante en el tiempo, donde el estado oculto puede rastrear evolución temporal del canal
- Decodificación secuencial de códigos, analizando dependencias entre bits/símbolos
- Predicción de tráfico y asignación dinámica de recursos

**Mecanismos de Atención y Transformers**: El mecanismo de atención permite a una red neuronal enfocarse dinámicamente en partes relevantes de la entrada, ponderando adaptativamente diferentes elementos según su importancia contextual [56]. La operación fundamental de atención escalada por producto punto (scaled dot-product attention) se define como:

$$\text{Attention}(\mathbf{Q}, \mathbf{K}, \mathbf{V}) = \text{softmax}\left(\frac{\mathbf{Q}\mathbf{K}^T}{\sqrt{d_k}}\right)\mathbf{V}$$

donde:
- $\mathbf{Q} \in \mathbb{R}^{n_q \times d_k}$: Matriz de consultas (queries) - representan "qué información se busca"
- $\mathbf{K} \in \mathbb{R}^{n_k \times d_k}$: Matriz de claves (keys) - representan "qué información está disponible"
- $\mathbf{V} \in \mathbb{R}^{n_k \times d_v}$: Matriz de valores (values) - contienen la información actual
- $d_k$: Dimensión de consultas y claves
- $\sqrt{d_k}$: Factor de escalado que estabiliza gradientes

La operación $\mathbf{Q}\mathbf{K}^T$ calcula similitudes entre consultas y claves, la softmax normaliza estas en una distribución de probabilidad, y la multiplicación por $\mathbf{V}$ produce una combinación ponderada de valores.

Los Transformers, basados completamente en mecanismos de atención multi-cabeza (multi-head attention), han revolucionado el procesamiento de secuencias, superando RNNs y LSTMs en numerosas tareas de procesamiento de lenguaje natural y, recientemente, procesamiento de series temporales [14]. La atención multi-cabeza ejecuta múltiples operaciones de atención en paralelo:

$$\text{MultiHead}(\mathbf{Q}, \mathbf{K}, \mathbf{V}) = \text{Concat}(\mathbf{head}_1, \ldots, \mathbf{head}_h)\mathbf{W}^O$$

donde:
$$\mathbf{head}_i = \text{Attention}(\mathbf{Q}\mathbf{W}_i^Q, \mathbf{K}\mathbf{W}_i^K, \mathbf{V}\mathbf{W}_i^V)$$

y $\mathbf{W}_i^Q, \mathbf{W}_i^K, \mathbf{W}_i^V, \mathbf{W}^O$ son matrices de proyección aprendibles.

Para comunicaciones inalámbricas, los Transformers son prometedores para:
- Modelar dependencias de largo alcance en secuencias de símbolos
- Capturar patrones complejos de interferencia multi-usuario
- Procesar información contextual heterogénea (canal, tráfico, QoS) para decisiones de asignación de recursos

#### 2) Técnicas de Regularización y Generalización

La generalización - capacidad de un modelo de rendir bien en datos no vistos durante entrenamiento - es crítica para sistemas de comunicación que deben operar en condiciones variables [57]. Varias técnicas de regularización mejoran la generalización:

**Dropout**: Durante el entrenamiento, neuronas individuales se desactivan aleatoriamente con probabilidad $p$ [58]:

$$\mathbf{h}^{(l)} = \mathbf{m}^{(l)} \odot \sigma(\mathbf{W}^{(l)}\mathbf{h}^{(l-1)} + \mathbf{b}^{(l)})$$

donde $\mathbf{m}^{(l)} \sim \text{Bernoulli}(1-p)$ es un vector de máscara binaria. Durante inferencia, se usan todas las neuronas pero las activaciones se escalan por $(1-p)$ para mantener la magnitud esperada. Dropout previene co-adaptación de características (donde neuronas se especializan excesivamente en presencia de otras específicas) y funciona como un ensamble implícito de redes más pequeñas.

**Normalización por Lotes (Batch Normalization)**: Normaliza activaciones en cada mini-batch para tener media cero y varianza unitaria [58]:

$$\hat{\mathbf{h}} = \frac{\mathbf{h} - \mu_{\mathcal{B}}}{\sqrt{\sigma^2_{\mathcal{B}} + \epsilon}}$$

donde $\mu_{\mathcal{B}} = \frac{1}{|\mathcal{B}|}\sum_{i \in \mathcal{B}}\mathbf{h}_i$ y $\sigma^2_{\mathcal{B}} = \frac{1}{|\mathcal{B}|}\sum_{i \in \mathcal{B}}(\mathbf{h}_i - \mu_{\mathcal{B}})^2$ son estadísticas del mini-batch $\mathcal{B}$, y $\epsilon$ es una constante pequeña para estabilidad numérica. Posteriormente se aplica una transformación afín aprendible:

$$\mathbf{z} = \gamma \odot \hat{\mathbf{h}} + \beta$$

donde $\gamma$ y $\beta$ son parámetros entrenables. Batch Normalization acelera convergencia (permitiendo tasas de aprendizaje más altas), reduce sensibilidad a inicialización de pesos, y proporciona un efecto regularizador implícito.

**Regularización de Peso**: Penalización L2 (weight decay) añade un término a la función de pérdida:

$$\mathcal{L}_{\text{total}} = \mathcal{L}_{\text{data}} + \lambda \sum_{l=1}^{L} \|\mathbf{W}^{(l)}\|^2_F$$

donde $\|\mathbf{W}\|_F = \sqrt{\sum_{ij}W_{ij}^2}$ es la norma de Frobenius, y $\lambda > 0$ controla la intensidad de regularización. Esto favorece soluciones con pesos de magnitud pequeña, mejorando generalización al reducir complejidad efectiva del modelo.

**Aumento de Datos (Data Augmentation)**: Para sistemas de comunicación, esto incluye entrenar con variaciones sintéticas que emulan diversidad operacional [59]:

- Variaciones de SNR: Entrenar en un rango amplio de condiciones de ruido
- Realizaciones de canal: Múltiples instancias de desvanecimiento con diferentes perfiles
- Offsets de frecuencia portadora y temporización: Simular imperfecciones de sincronización
- Interferencia sintética: Añadir interferencia co-canal, adyacente, o impulsiva
- Distorsiones no-lineales: Modelar efectos de amplificadores de potencia

El aumento de datos mejora robustez y reduce el riesgo de sobreajuste a condiciones específicas de entrenamiento.

#### 3) Optimización y Entrenamiento

**Descenso de Gradiente Estocástico (SGD)**: El algoritmo fundamental para entrenar redes neuronales es la actualización iterativa de parámetros en dirección opuesta al gradiente de la función de pérdida [61]:

$$\theta_{t+1} = \theta_t - \eta \nabla_{\theta}\mathcal{L}(\theta_t; \mathcal{B}_t)$$

donde:
- $\theta_t$: Parámetros en la iteración $t$
- $\eta > 0$: Tasa de aprendizaje (learning rate)
- $\nabla_{\theta}\mathcal{L}$: Gradiente de la pérdida respecto a parámetros
- $\mathcal{B}_t$: Mini-batch de muestras de entrenamiento

El gradiente se calcula mediante el algoritmo de retropropagación (backpropagation), aplicación eficiente de la regla de la cadena a grafos computacionales.

**Optimizadores Adaptativos**: Adam (Adaptive Moment Estimation) combina momentum (término de inercia que acelera convergencia) y tasas de aprendizaje adaptativas por parámetro [62]:

$$\mathbf{m}_t = \beta_1 \mathbf{m}_{t-1} + (1-\beta_1)\mathbf{g}_t$$
$$\mathbf{v}_t = \beta_2 \mathbf{v}_{t-1} + (1-\beta_2)\mathbf{g}_t^2$$

donde $\mathbf{g}_t = \nabla_{\theta}\mathcal{L}(\theta_t; \mathcal{B}_t)$ es el gradiente, $\mathbf{m}_t$ es el estimado de primer momento (media), $\mathbf{v}_t$ el estimado de segundo momento (varianza no-centrada), y $\beta_1, \beta_2 \in [0,1)$ son tasas de decaimiento exponencial (típicamente $\beta_1=0.9, \beta_2=0.999$).

Los estimados se corrigen para compensar sesgo hacia cero en iteraciones iniciales:

$$\hat{\mathbf{m}}_t = \frac{\mathbf{m}_t}{1-\beta_1^t}, \quad \hat{\mathbf{v}}_t = \frac{\mathbf{v}_t}{1-\beta_2^t}$$

La actualización de parámetros se realiza mediante:

$$\theta_{t+1} = \theta_t - \eta \frac{\hat{\mathbf{m}}_t}{\sqrt{\hat{\mathbf{v}}_t} + \epsilon}$$

donde $\epsilon$ (típicamente $10^{-8}$) previene división por cero. Adam adapta efectivamente la tasa de aprendizaje para cada parámetro, acelerando convergencia y mejorando estabilidad.

**Retropropagación a través de Canales**: Un desafío específico de comunicaciones neuronales es diferenciar a través del canal físico para entrenar transmisor y receptor conjuntamente. Para canales determinísticos donde $\mathbf{y} = h(\mathbf{x})$ es una función diferenciable, la regla de la cadena se aplica directamente:

$$\frac{\partial \mathcal{L}}{\partial \theta} = \frac{\partial \mathcal{L}}{\partial \mathbf{y}} \frac{\partial h(\mathbf{x})}{\partial \mathbf{x}} \frac{\partial f_{\theta}(\mathbf{s})}{\partial \theta}$$

Para un canal lineal AWGN MIMO $\mathbf{y} = \mathbf{H}\mathbf{x} + \mathbf{n}$, el término medio es simplemente $\partial h/\partial \mathbf{x} = \mathbf{H}$.

Para canales estocásticos (con desvanecimiento aleatorio o ruido), se requiere el **reparametrization trick** para obtener estimados insesgados de gradientes [63]. La aleatoriedad se hace explícita mediante variables auxiliares:

$$\mathbf{y} = h(\mathbf{x}, \epsilon), \quad \epsilon \sim p(\epsilon)$$

donde $\epsilon$ representa la fuente de estocasticidad (ej. realización de desvanecimiento, muestra de ruido). El gradiente de la pérdida esperada se expresa como:

$$\nabla_{\theta}\mathbb{E}_{\epsilon}[\mathcal{L}(g_{\phi}(h(f_{\theta}(\mathbf{s}), \epsilon)))] = \mathbb{E}_{\epsilon}[\nabla_{\theta}\mathcal{L}(g_{\phi}(h(f_{\theta}(\mathbf{s}), \epsilon)))]$$

permitiendo intercambiar gradiente y esperanza, de modo que el gradiente se estima mediante muestras de $\epsilon$.

### D. Formulación del Problema de Optimización con Restricciones Físicas

La implementación práctica de sistemas de comunicación neuronal requiere incorporar restricciones impuestas por limitaciones físicas de hardware y regulaciones espectrales [64].

#### 1) Restricción de Potencia

La potencia promedio transmitida debe satisfacer límites regulatorios y capacidades de amplificadores:

$$\mathbb{E}_{\mathbf{s} \sim p(\mathbf{s})}[\|f_{\theta}(\mathbf{s})\|^2] \leq P$$

Esta restricción se puede incorporar mediante tres aproximaciones principales:

**Normalización Explícita**: Forzar la salida del transmisor neuronal a tener norma controlada:

$$\tilde{f}_{\theta}(\mathbf{s}) = \sqrt{P} \frac{f_{\theta}(\mathbf{s})}{\|f_{\theta}(\mathbf{s})\|}$$

Esta transformación proyecta cada señal transmitida sobre una esfera de radio $\sqrt{P}$ en $\mathbb{C}^M$. La operación de normalización es diferenciable (excepto en el origen), permitiendo retropropagación de gradientes. Una variante emplea normalización promedio por mini-batch:

$$\tilde{f}_{\theta}(\mathbf{s}) = \sqrt{P} \frac{f_{\theta}(\mathbf{s})}{\sqrt{\frac{1}{|\mathcal{B}|}\sum_{i \in \mathcal{B}}\|f_{\theta}(\mathbf{s}_i)\|^2}}$$

**Penalización en la Función de Pérdida**: Añadir un término de penalización cuadrática que penaliza violaciones de la restricción:

$$\mathcal{L}_{\text{total}} = \mathcal{L}_{\text{error}} + \mu \max\left(0, \frac{1}{|\mathcal{B}|}\sum_{i \in \mathcal{B}}\|f_{\theta}(\mathbf{s}_i)\|^2 - P\right)^2$$

donde $\mu > 0$ es un hiperparámetro de penalización. Esta aproximación es más flexible, permitiendo potencias menores a $P$, pero requiere ajuste cuidadoso de $\mu$ para balancear satisfacción de restricción y minimización de error.

**Capa de Proyección**: Implementar una capa final que proyecta la salida del transmisor sobre el conjunto factible de señales con potencia $\leq P$ [65]. Para restricción de potencia promedio, esto se reduce a escalado adaptativo.

#### 2) Restricción de Ancho de Banda

La señal transmitida debe estar limitada espectralmente al ancho de banda asignado $W$ Hz. Para señales de banda base complejas, esto se expresa en el dominio de Fourier como:

$$\mathcal{F}\{f_{\theta}(\mathbf{s})\}(f) = 0, \quad |f| > W/2$$

donde $\mathcal{F}\{\cdot\}$ denota la transformada de Fourier.

**Conformación de Pulso (Pulse Shaping)**: Aplicar un filtro conformador de pulso $p(t)$ que limita el espectro:

$$s(t) = \sum_{i=0}^{M-1} x_i p(t - iT)$$

donde $\{x_i\}$ son los símbolos complejos de salida del transmisor neuronal, $T$ es el período de símbolo, y $p(t)$ es típicamente un pulso de Nyquist (ej. raised cosine, root raised cosine) con ancho de banda controlado. El filtro de pulso puede implementarse como una capa convolucional con pesos fijos o parcialmente entrenables [66].

**Implementación en Dominio Frecuencial**: Entrenar el transmisor en el dominio frecuencial y aplicar una máscara binaria $M(f)$ que anula componentes espectrales fuera de banda:

$$\tilde{X}(f) = M(f) \cdot X(f)$$

donde $M(f) = \mathbb{1}_{|f| \leq W/2}$ y $X(f) = \mathcal{F}\{f_{\theta}(\mathbf{s})\}$.

#### 3) Restricción de Amplitud y Cuantización

Los amplificadores de potencia (PA) operan con rangos dinámicos limitados y exhiben no-linealidades, especialmente cerca de saturación. Un modelo simplificado de clipping es:

$$x_{\text{PA}}(t) = g(x(t)) = \begin{cases}
A_{\max} \frac{x(t)}{|x(t)|} & \text{si } |x(t)| > A_{\max} \\
x(t) & \text{si } |x(t)| \leq A_{\max}
\end{cases}$$

donde $A_{\max}$ es la amplitud máxima del PA. Para incorporar esta no-linealidad en el entrenamiento end-to-end:

$$\mathcal{L} = \mathbb{E}_{\mathbf{s}, \mathbf{n}}[\mathcal{L}_{\text{error}}(\mathbf{s}, g_{\phi}(h(g(f_{\theta}(\mathbf{s}))) + \mathbf{n}))]$$

La función $g(\cdot)$ es casi-en-todas-partes diferenciable, permitiendo gradientes aproximados. Modelos más sofisticados de PA (ej. Rapp model, Saleh model) capturan conversión AM-AM y AM-PM [67].

La **cuantización** en conversores digital-analógico (DAC) se modela como:

$$x_Q = Q(x) = \Delta \left\lfloor \frac{x}{\Delta} + \frac{1}{2}\right\rfloor$$

donde $\Delta = \frac{x_{\max} - x_{\min}}{2^b}$ es el paso de cuantización para $b$ bits. La función $Q(\cdot)$ no es diferenciable. Durante entrenamiento, se emplea el estimador **straight-through** [68]:

$$\frac{\partial Q(x)}{\partial x} \approx 1$$

en la retropropagación (backward pass), mientras que el pase forward usa cuantización real. Este estimador sesgado funciona sorprendentemente bien en práctica.

#### 4) Incorporación de Información de Estado de Canal (CSI)

Cuando el transmisor posee información sobre el estado del canal (ej. mediante retroalimentación o reciprocidad en TDD), se puede condicionar la transmisión en $\mathbf{H}$ [69]:

$$\mathbf{x} = f_{\theta}(\mathbf{s}, \mathbf{H})$$

Esto habilita precodificación adaptativa que optimiza la transmisión según condiciones instantáneas del canal. En sistemas MIMO, el transmisor puede aprender estrategias de beamforming implícitas.

En el receptor, el tratamiento de CSI varía:

**CSI Perfecta**: El receptor tiene conocimiento exacto de $\mathbf{H}$:
$$\hat{\mathbf{s}} = g_{\phi}(\mathbf{y}, \mathbf{H})$$

**CSI Estimada**: El receptor estima el canal a partir de señales piloto y usa la estimación:
$$\hat{\mathbf{H}} = h_{\psi}(\mathbf{y}_{\text{pilot}})$$
$$\hat{\mathbf{s}} = g_{\phi}(\mathbf{y}, \hat{\mathbf{H}})$$

La red de estimación $h_{\psi}$ puede entrenarse conjuntamente con el receptor o separadamente.

**Operación Ciega (Blind)**: El receptor no usa CSI explícita:
$$\hat{\mathbf{s}} = g_{\phi}(\mathbf{y})$$

La red neuronal debe inferir implícitamente características del canal a partir de la señal recibida. Esta aproximación es robusta a errores de estimación de canal, pero típicamente requiere arquitecturas más complejas [70].

### E. Análisis de Complejidad y Escalabilidad

La viabilidad práctica de sistemas neuronales para el nivel físico depende críticamente de su complejidad computacional y de memoria, especialmente para implementación en tiempo real en dispositivos con recursos limitados [71].

#### 1) Complejidad Computacional

**Redes Completamente Conectadas**: Para una red feedforward con $L$ capas, donde la capa $l$ tiene $n_l$ neuronas:

**Forward Pass**: La complejidad para evaluar la red es:
$$\mathcal{C}_{\text{forward}} = \mathcal{O}\left(\sum_{l=1}^{L-1} n_l n_{l+1}\right)$$

operaciones (multiplicaciones-acumulaciones, MACs). Para matrices de pesos densas, esto equivale aproximadamente al número total de pesos sinápticos.

**Backward Pass**: Durante entrenamiento, el cálculo de gradientes mediante backpropagation tiene complejidad asintótica similar:
$$\mathcal{C}_{\text{backward}} = \mathcal{O}\left(\sum_{l=1}^{L-1} n_l n_{l+1}\right)$$

**Redes Convolucionales**: Para CNNs con $L$ capas convolucionales, donde la capa $l$ tiene $C_l$ canales de salida, kernels de tamaño $k_l \times k_l$, y mapas de características de tamaño espacial $H_l \times W_l$:

$$\mathcal{C}_{\text{CNN}} = \mathcal{O}\left(\sum_{l=1}^{L} C_{l-1} C_l k_l^2 H_l W_l\right)$$

Las CNNs son típicamente mucho más eficientes que capas completamente conectadas para procesamiento de señales con estructura espacial/temporal, debido al número reducido de parámetros por compartición de pesos.

**Redes Recurrentes**: Para RNNs/LSTMs procesando secuencias de longitud $T$ con $n$ unidades ocultas:

$$\mathcal{C}_{\text{RNN}} = \mathcal{O}(T n^2)$$

La complejidad escala cuadráticamente con el tamaño del estado oculto y linealmente con la longitud de secuencia. Para secuencias muy largas, esto puede ser prohibitivo.

**Transformers**: La atención escalada tiene complejidad:
$$\mathcal{C}_{\text{attention}} = \mathcal{O}(n^2 d)$$

donde $n$ es la longitud de secuencia y $d$ la dimensión de embeddings. La complejidad cuadrática en $n$ es una limitación para secuencias extensas, motivando variantes eficientes como Linformer, Performer, o attention local [72].

#### 2) Complejidad de Memoria

Durante **entrenamiento**, los requisitos de memoria incluyen:

- **Parámetros del modelo**: $\mathcal{O}(|\theta| + |\phi|)$ donde $|\theta|, |\phi|$ son los números de parámetros del transmisor y receptor
- **Activaciones intermedias**: $\mathcal{O}(B \cdot A)$ donde $B$ es el tamaño de mini-batch y $A$ es el número total de activaciones en todas las capas. Estas deben almacenarse durante el forward pass para el backward pass.
- **Gradientes**: $\mathcal{O}(|\theta| + |\phi|)$
- **Momentos del optimizador** (para Adam): $\mathcal{O}(2(|\theta| + |\phi|))$

Para redes muy profundas, el almacenamiento de activaciones domina. **Gradient checkpointing** reduce memoria reteniendo solo activaciones de algunas capas seleccionadas y recomputando las demás durante backpropagation, con un trade-off de $\sim$30-40% más tiempo de cómputo [73].

Durante **inferencia**, solo se requiere almacenar parámetros y activaciones de la capa actual (para procesamiento secuencial), resultando en requisitos de memoria significativamente menores.

#### 3) Comparación con Métodos Tradicionales

**Decodificación Turbo**: Los códigos Turbo emplean decodificación iterativa con dos decodificadores SISO (Soft-Input Soft-Output) que intercambian información. La complejidad por iteración es aproximadamente:
$$\mathcal{C}_{\text{Turbo}} = \mathcal{O}(n \cdot I \cdot S)$$

donde $n$ es la longitud de bloque, $I$ el número de iteraciones (típicamente 4-8), y $S$ el número de estados del trellis del código convolucional constituyente (típicamente $S=8$ o $16$). Para bloques largos ($n \sim 1000$), esto puede alcanzar decenas de miles de operaciones.

**Decodificación de Códigos LDPC**: La decodificación belief propagation tiene complejidad:
$$\mathcal{C}_{\text{LDPC}} = \mathcal{O}(E \cdot I)$$

donde $E$ es el número de aristas en el grafo de Tanner (proporcional a $n \cdot d_v$ con $d_v$ grado promedio de nodos variables), e $I$ iteraciones (típicamente 10-50).

**Detección ML para MIMO**: La detección de máxima verosimilitud evaluando todas las posibles secuencias transmitidas tiene complejidad:
$$\mathcal{C}_{\text{ML}} = \mathcal{O}(M^{N_t})$$

donde $M$ es el tamaño de la constelación (ej. $M=16$ para 16-QAM) y $N_t$ el número de antenas transmisoras. Para configuraciones típicas ($M=64, N_t=8$), esto es $64^8 \approx 2.8 \times 10^{14}$ evaluaciones - completamente intratable. Métodos sphere decoding reducen la complejidad promedio pero no la peor.

**Detección MIMO Neuronal**: Una red neuronal con arquitectura eficiente (ej. capas completamente conectadas con $L=5$ capas, $n_l \sim 256$ neuronas) tiene complejidad aproximada:
$$\mathcal{C}_{\text{NN}} = \mathcal{O}(L \cdot n^2) \sim \mathcal{O}(10^5)$$

operaciones - múltiples órdenes de magnitud menor que ML, con rendimiento cercano a óptimo para SNR moderado-alto [74].

**Estimación de Canal**: Métodos tradicionales como Least Squares (LS) o Minimum Mean Square Error (MMSE) tienen complejidad $\mathcal{O}(N_p^3)$ para $N_p$ pilotos (por inversión de matrices). Redes neuronales con arquitecturas CNN o RNN procesan pilotos con complejidad lineal o cuadrática, escalando mejor para sistemas masivos.

En resumen, las arquitecturas neuronales cuidadosamente diseñadas pueden alcanzar complejidad computacional comparable o incluso inferior a métodos tradicionales, mientras ofrecen rendimiento superior en escenarios complejos y no-ideales [75].

---

## REFERENCIAS

[1] M. Giordani, M. Polese, M. Mezzavilla, S. Rangan, and M. Zorzi, "Toward 6G networks: Use cases and technologies," *IEEE Communications Magazine*, vol. 58, no. 3, pp. 55-61, Mar. 2020.

[2] W. Saad, M. Bennis, and M. Chen, "A vision of 6G wireless systems: Applications, trends, technologies, and open research problems," *IEEE Network*, vol. 34, no. 3, pp. 134-142, May 2020.

[3] ITU-R, "IMT Vision - Framework and overall objectives of the future development of IMT for 2030 and beyond," Recommendation ITU-R M.2160-0, Nov. 2023.

[4] K. B. Letaief, W. Chen, Y. Shi, J. Zhang, and Y.-J. A. Zhang, "The roadmap to 6G: AI empowered wireless networks," *IEEE Communications Magazine*, vol. 57, no. 8, pp. 84-90, Aug. 2019.

[5] C. De Alwis et al., "Survey on 6G frontiers: Trends, applications, requirements, technologies and future research," *IEEE Open Journal of the Communications Society*, vol. 2, pp. 836-886, 2021.

[6] Z. Zhang et al., "6G wireless networks: Vision, requirements, architecture, and key technologies," *IEEE Vehicular Technology Magazine*, vol. 14, no. 3, pp. 28-41, Sep. 2019.

[7] T. S. Rappaport et al., "Wireless communications and applications above 100 GHz: Opportunities and challenges for 6G and beyond," *IEEE Access*, vol. 7, pp. 78729-78757, 2019.

[8] C. Jiang, H. Zhang, Y. Ren, Z. Han, K.-C. Chen, and L. Hanzo, "Machine learning paradigms for next-generation wireless networks," *IEEE Wireless Communications*, vol. 24, no. 2, pp. 98-105, Apr. 2017.

[9] T. O'Shea and J. Hoydis, "An introduction to deep learning for the physical layer," *IEEE Transactions on Cognitive Communications and Networking*, vol. 3, no. 4, pp. 563-575, Dec. 2017.

[10] H. Ye, G. Y. Li, and B.-H. Juang, "Power of deep learning for channel estimation and signal detection in OFDM systems," *IEEE Wireless Communications Letters*, vol. 7, no. 1, pp. 114-117, Feb. 2018.

[11] B. Mulgrew, "Applying radial basis functions," *IEEE Signal Processing Magazine*, vol. 13, no. 2, pp. 50-65, Mar. 1996.

[12] Y. LeCun, Y. Bengio, and G. Hinton, "Deep learning," *Nature*, vol. 521, no. 7553, pp. 436-444, May 2015.

[13] I. Goodfellow, Y. Bengio, and A. Courville, *Deep Learning*. Cambridge, MA: MIT Press, 2016.

[14] A. Vaswani et al., "Attention is all you need," in *Proc. Advances in Neural Information Processing Systems (NeurIPS)*, Long Beach, CA, USA, Dec. 2017, pp. 5998-6008.

[15] N. P. Jouppi et al., "In-datacenter performance analysis of a tensor processing unit," in *Proc. ACM/IEEE 44th Annual International Symposium on Computer Architecture (ISCA)*, Toronto, ON, Canada, Jun. 2017, pp. 1-12.

[16] M. K. Samimi and T. S. Rappaport, "3-D millimeter-wave statistical channel model for 5G wireless system design," *IEEE Transactions on Microwave Theory and Techniques*, vol. 64, no. 7, pp. 2207-2225, Jul. 2016.

[17] N. Shlezinger, N. Farsad, Y. C. Eldar, and A. J. Goldsmith, "ViterbiNet: A deep learning based Viterbi algorithm for symbol detection," *IEEE Transactions on Wireless Communications*, vol. 19, no. 5, pp. 3319-3331, May 2020.

[18] T. O'Shea and K. Karra, "Learning to communicate: Channel auto-encoders, domain specific regularizers, and attention," in *Proc. IEEE International Symposium on Signal Processing and Information Technology (ISSPIT)*, Bilbao, Spain, Dec. 2016, pp. 223-228.

[19] S. Dörner, S. Cammerer, J. Hoydis, and S. ten Brink, "Deep learning based communication over the air," *IEEE Journal of Selected Topics in Signal Processing*, vol. 12, no. 1, pp. 132-143, Feb. 2018.

[20] F. A. Aoudia and J. Hoydis, "End-to-end learning of communications systems without a channel model," in *Proc. 52nd Asilomar Conference on Signals, Systems, and Computers*, Pacific Grove, CA, USA, Oct. 2018, pp. 298-303.

[21] H. Kim, Y. Jiang, R. Rana, S. Kannan, S. Oh, and P. Viswanath, "Communication algorithms via deep learning," in *Proc. International Conference on Learning Representations (ICLR)*, Vancouver, BC, Canada, Apr. 2018.

[22] H. Ye, L. Liang, G. Y. Li, and B.-H. Juang, "Deep learning-based end-to-end wireless communication systems with conditional GANs as unknown channel," *IEEE Transactions on Wireless Communications*, vol. 19, no. 5, pp. 3133-3143, May 2020.

[23] C. Huang, G. C. Alexandropoulos, A. Zappone, M. Debbah, and C. Yuen, "Deep learning for UL/DL channel calibration in generic massive MIMO systems," in *Proc. IEEE International Conference on Communications (ICC)*, Shanghai, China, May 2019, pp. 1-6.

[24] N. Samuel, T. Diskin, and A. Wiesel, "Deep MIMO detection," in *Proc. IEEE 18th International Workshop on Signal Processing Advances in Wireless Communications (SPAWC)*, Sapporo, Japan, Jul. 2017, pp. 1-5.

[25] M. Chen et al., "Artificial neural networks-based machine learning for wireless networks: A tutorial," *IEEE Communications Surveys & Tutorials*, vol. 21, no. 4, pp. 3039-3071, 4th Quart. 2019.

[26] Q. Mao, F. Hu, and Q. Hao, "Deep learning for intelligent wireless networks: A comprehensive survey," *IEEE Communications Surveys & Tutorials*, vol. 20, no. 4, pp. 2595-2621, 4th Quart. 2018.

[27] J. Park, S. Samarakoon, M. Bennis, and M. Debbah, "Wireless network intelligence at the edge," *Proceedings of the IEEE*, vol. 107, no. 11, pp. 2204-2239, Nov. 2019.

[28] N. Farsad and A. Goldsmith, "Neural network detection of data sequences in communication systems," *IEEE Transactions on Signal Processing*, vol. 66, no. 21, pp. 5663-5678, Nov. 2018.

[29] S. Cammerer, T. Gruber, J. Hoydis, and S. ten Brink, "Scaling deep learning-based decoding of polar codes via partitioning," in *Proc. IEEE Global Communications Conference (GLOBECOM)*, Abu Dhabi, United Arab Emirates, Dec. 2018, pp. 1-6.

[30] N. Shlezinger, Y. C. Eldar, and M. R. D. Rodrigues, "Hardware-limited task-based quantization," *IEEE Transactions on Signal Processing*, vol. 67, no. 20, pp. 5223-5238, Oct. 2019.

[31] M. Eisen, C. Zhang, L. F. O. Chamon, D. D. Lee, and A. Ribeiro, "Learning optimal resource allocations in wireless systems," *IEEE Transactions on Signal Processing*, vol. 67, no. 10, pp. 2775-2790, May 2019.

[32] Y. Shi, K. Yang, T. Jiang, J. Zhang, and K. B. Letaief, "Communication-efficient edge AI: Algorithms and systems," *IEEE Communications Surveys & Tutorials*, vol. 22, no. 4, pp. 2167-2191, 4th Quart. 2020.

[33] C. E. Shannon, "A mathematical theory of communication," *Bell System Technical Journal*, vol. 27, no. 3, pp. 379-423, Jul. 1948.

[34] J. G. Proakis and M. Salehi, *Digital Communications*, 5th ed. New York, NY: McGraw-Hill, 2008.

[35] A. Paulraj, R. Nabar, and D. Gore, *Introduction to Space-Time Wireless Communications*. Cambridge, UK: Cambridge University Press, 2003.

[36] F. Ait Aoudia and J. Hoydis, "Model-free training of end-to-end communication systems," *IEEE Journal on Selected Areas in Communications*, vol. 37, no. 11, pp. 2503-2516, Nov. 2019.

[37] T. M. Cover and J. A. Thomas, *Elements of Information Theory*, 2nd ed. Hoboken, NJ: Wiley-Interscience, 2006.

[38] M. K. Samimi, G. R. MacCartney, S. Sun, and T. S. Rappaport, "28 GHz millimeter-wave ultrawideband small-scale fading models in wireless channels," in *Proc. IEEE 83rd Vehicular Technology Conference (VTC Spring)*, Nanjing, China, May 2016, pp. 1-6.

[39] A. Goldsmith, *Wireless Communications*. New York, NY: Cambridge University Press, 2005.

[40] T. J. O'Shea, K. Karra, and T. C. Clancy, "Learning to communicate: Channel auto-encoders, domain specific regularizers, and attention," in *Proc. IEEE International Symposium on Signal Processing and Information Technology (ISSPIT)*, Limassol, Cyprus, Dec. 2016, pp. 223-228.

[41] S. Dörner, S. Cammerer, J. Hoydis, and S. ten Brink, "Deep learning based communication over the air," *IEEE Journal of Selected Topics in Signal Processing*, vol. 12, no. 1, pp. 132-143, Feb. 2018.

[42] R. G. Gallager, *Information Theory and Reliable Communication*. New York, NY: John Wiley & Sons, 1968.

[43] E. Telatar, "Capacity of multi-antenna Gaussian channels," *European Transactions on Telecommunications*, vol. 10, no. 6, pp. 585-595, Nov. 1999.

[44] Y. Polyanskiy, H. V. Poor, and S. Verdú, "Channel coding rate in the finite blocklength regime," *IEEE Transactions on Information Theory*, vol. 56, no. 5, pp. 2307-2359, May 2010.

[45] G. Durisi, T. Koch, and P. Popovski, "Toward massive, ultrareliable, and low-latency wireless communication with short packets," *Proceedings of the IEEE*, vol. 104, no. 9, pp. 1711-1726, Sep. 2016.

[46] N. Tishby, F. C. Pereira, and W. Bialek, "The information bottleneck method," in *Proc. 37th Annual Allerton Conference on Communication, Control, and Computing*, Monticello, IL, USA, Sep. 1999, pp. 368-377.

[47] N. Tishby and N. Zaslavsky, "Deep learning and the information bottleneck principle," in *Proc. IEEE Information Theory Workshop (ITW)*, Jerusalem, Israel, Apr. 2015, pp. 1-5.

[48] T. Berger, *Rate Distortion Theory: A Mathematical Basis for Data Compression*. Englewood Cliffs, NJ: Prentice-Hall, 1971.

[49] M. Gastpar, B. Rimoldi, and M. Vetterli, "To code, or not to code: Lossy source-channel communication revisited," *IEEE Transactions on Information Theory*, vol. 49, no. 5, pp. 1147-1158, May 2003.

[50] E. Bourtsoulatze, D. B. Kurka, and D. Gündüz, "Deep joint source-channel coding for wireless image transmission," *IEEE Transactions on Cognitive Communications and Networking*, vol. 5, no. 3, pp. 567-579, Sep. 2019.

[51] G. Cybenko, "Approximation by superpositions of a sigmoidal function," *Mathematics of Control, Signals, and Systems*, vol. 2, no. 4, pp. 303-314, Dec. 1989.

[52] M. Telgarsky, "Benefits of depth in neural networks," in *Proc. 29th Annual Conference on Learning Theory (COLT)*, New York, NY, USA, Jun. 2016, pp. 1517-1539.

[53] Y. LeCun, L. Bottou, Y. Bengio, and P. Haffner, "Gradient-based learning applied to document recognition," *Proceedings of the IEEE*, vol. 86, no. 11, pp. 2278-2324, Nov. 1998.

[54] D. E. Rumelhart, G. E. Hinton, and R. J. Williams, "Learning representations by back-propagating errors," *Nature*, vol. 323, no. 6088, pp. 533-536, Oct. 1986.

[55] S. Hochreiter and J. Schmidhuber, "Long short-term memory," *Neural Computation*, vol. 9, no. 8, pp. 1735-1780, Nov. 1997.

[56] D. Bahdanau, K. Cho, and Y. Bengio, "Neural machine translation by jointly learning to align and translate," in *Proc. International Conference on Learning Representations (ICLR)*, San Diego, CA, USA, May 2015.

[57] Y. Bengio, A. Courville, and P. Vincent, "Representation learning: A review and new perspectives," *IEEE Transactions on Pattern Analysis and Machine Intelligence*, vol. 35, no. 8, pp. 1798-1828, Aug. 2013.

[58] N. Srivastava, G. Hinton, A. Krizhevsky, I. Sutskever, and R. Salakhutdinov, "Dropout: A simple way to prevent neural networks from overfitting," *Journal of Machine Learning Research*, vol. 15, no. 1, pp. 1929-1958, Jun. 2014.

[59] S. Ioffe and C. Szegedy, "Batch normalization: Accelerating deep network training by reducing internal covariate shift," in *Proc. International Conference on Machine Learning (ICML)*, Lille, France, Jul. 2015, pp. 448-456.

[60] C. Shorten and T. M. Khoshgoftaar, "A survey on image data augmentation for deep learning," *Journal of Big Data*, vol. 6, no. 1, pp. 1-48, Jul. 2019.

[61] L. Bottou, "Large-scale machine learning with stochastic gradient descent," in *Proc. COMPSTAT'2010*, Paris, France, Aug. 2010, pp. 177-186.

[62] D. P. Kingma and J. Ba, "Adam: A method for stochastic optimization," in *Proc. International Conference on Learning Representations (ICLR)*, San Diego, CA, USA, May 2015.

[63] D. P. Kingma and M. Welling, "Auto-encoding variational Bayes," in *Proc. International Conference on Learning Representations (ICLR)*, Banff, AB, Canada, Apr. 2014.

[64] R. Fritschek, R. F. Schaefer, and G. Wunder, "Deep learning for the Gaussian wiretap channel," in *Proc. IEEE International Conference on Communications (ICC)*, Kansas City, MO, USA, May 2018, pp. 1-6.

[65] M. Kim, W. Lee, and D.-H. Cho, "A novel PAPR reduction scheme for OFDM system based on deep learning," *IEEE Communications Letters*, vol. 22, no. 3, pp. 510-513, Mar. 2018.

[66] S. Cammerer, F. Aït Aoudia, S. Dörner, M. Stark, J. Hoydis, and S. ten Brink, "Trainable communication systems: Concepts and prototype," *IEEE Transactions on Communications*, vol. 68, no. 9, pp. 5489-5503, Sep. 2020.

[67] S. C. Cripps, *RF Power Amplifiers for Wireless Communications*, 2nd ed. Norwood, MA: Artech House, 2006.

[68] Y. Bengio, N. Léonard, and A. Courville, "Estimating or propagating gradients through stochastic neurons for conditional computation," *arXiv preprint arXiv:1308.3432*, Aug. 2013.

[69] H. Huang, W. Xia, J. Xiong, J. Yang, G. Zheng, and X. Zhu, "Unsupervised learning-based fast beamforming design for downlink MIMO," *IEEE Access*, vol. 7, pp. 7599-7605, Jan. 2019.

[70] H. Ye, G. Y. Li, B.-H. Juang, and K. Sivanesan, "Channel agnostic end-to-end learning based communication systems with conditional GAN," in *Proc. IEEE Global Communications Conference (GLOBECOM)*, Waikoloa, HI, USA, Dec. 2018, pp. 1-5.

[71] Y. Wang, M. Liu, J. Yang, and G. Gui, "Data-driven deep learning for automatic modulation recognition in cognitive radios," *IEEE Transactions on Vehicular Technology*, vol. 68, no. 4, pp. 4074-4077, Apr. 2019.

[72] A. Katharopoulos, A. Vyas, N. Pappas, and F. Fleuret, "Transformers are RNNs: Fast autoregressive transformers with linear attention," in *Proc. International Conference on Machine Learning (ICML)*, Virtual, Jul. 2020, pp. 5156-5165.

[73] T. Chen, B. Xu, C. Zhang, and C. Guestrin, "Training deep nets with sublinear memory cost," *arXiv preprint arXiv:1604.06174*, Apr. 2016.

[74] N. Samuel, T. Diskin, and A. Wiesel, "Learning to detect," *IEEE Transactions on Signal Processing*, vol. 67, no. 10, pp. 2554-2564, May 2019.

[75] Q. Hu, F. Gao, H. Zhang, S. Jin, and G. Y. Li, "Deep learning for channel estimation: Interpretation, performance, and comparison," *IEEE Transactions on Wireless Communications*, vol. 20, no. 4, pp. 2398-2412, Apr. 2021.
