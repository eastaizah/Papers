# Arquitecturas de Inteligencia Artificial Profunda para la Revolución de la Capa Física en Redes Inalámbricas 6G: De Sistemas Basados en Modelos a Comunicaciones Nativas de Deep Learning

**Resumen**—Este artículo presenta una revisión exhaustiva y análisis profundo de la aplicación de técnicas de Inteligencia Artificial (IA) y Deep Learning (DL) en la capa física (PHY) de sistemas de comunicaciones inalámbricas de sexta generación (6G) y posteriores. Se examina la transición desde los enfoques tradicionales basados en modelos hacia arquitecturas nativas de IA que redefinen fundamentalmente el diseño de la capa física. El documento explora en detalle las arquitecturas de redes neuronales profundas aplicadas a estimación de canal, retroalimentación de información de estado de canal (CSI), sistemas MIMO masivos, codificación de canal, detección de señales, beamforming inteligente, gestión de recursos espectrales, modulación adaptativa, y comunicaciones semánticas. Se presenta el soporte matemático y analítico subyacente a cada componente, incluyendo formulaciones de optimización, funciones de pérdida, arquitecturas de autocodificadores, redes neuronales recurrentes, convolucionales, transformers, y técnicas de aprendizaje por refuerzo. El análisis abarca desafíos de implementación, complejidad computacional, generalización, y robustez ante condiciones adversas del canal. Se concluye con una discusión sobre direcciones futuras y el potencial disruptivo de la IA nativa en el diseño de sistemas de comunicaciones inalámbricas de próxima generación.

**Palabras clave**—Inteligencia Artificial, Deep Learning, 6G, Capa Física, MIMO Masivo, CSI, Beamforming, Estimación de Canal, Codificación Neural, Comunicaciones Inalámbricas.

---

## I. INTRODUCCIÓN

La evolución de las redes de comunicaciones inalámbricas ha estado marcada por incrementos sistemáticos en capacidad, velocidad, latencia reducida y eficiencia espectral. Mientras que las generaciones anteriores (3G, 4G, 5G) se basaron principalmente en refinamientos de técnicas tradicionales de procesamiento de señales y teoría de la información, la sexta generación (6G) y sistemas posteriores representan un cambio paradigmático hacia arquitecturas nativas de Inteligencia Artificial (IA) en todos los niveles del stack de comunicaciones, particularmente en la capa física [1], [2].

La capa física de los sistemas de comunicaciones inalámbricas tradicionales se ha diseñado históricamente mediante enfoques analíticos basados en modelos matemáticos del canal de propagación, teoría de la información, y optimizaciones convexas. Sin embargo, estos métodos enfrentan limitaciones fundamentales cuando se confrontan con la complejidad creciente de escenarios 6G, que incluyen comunicaciones terahertz, superficies inteligentes reconfigurables (RIS), MIMO masivo de ultra-alta dimensión, canales altamente no lineales, y requisitos de latencia ultra-baja [3], [4]. En este contexto, las técnicas de Deep Learning (DL) emergen como una alternativa prometedora capaz de aprender representaciones óptimas directamente de los datos sin asumir modelos de canal simplificados [5].

### A. Motivación para IA en la Capa Física

La motivación fundamental para integrar IA y DL en la capa física de sistemas 6G surge de múltiples factores convergentes [6], [7]:

1. **Complejidad de Modelado**: Los canales de comunicación modernos, especialmente en frecuencias milimétricas (mmWave) y terahertz (THz), exhiben características de propagación extremadamente complejas incluyendo desvanecimiento severo, bloqueo dinámico, dispersión no lineal, y efectos atmosféricos que son difíciles de modelar analíticamente [8], [9].

2. **Alta Dimensionalidad**: Los sistemas MIMO masivos con cientos o miles de antenas generan espacios de señales de dimensionalidad extremadamente alta donde los métodos de optimización tradicionales se vuelven computacionalmente intratables [10], [11].

3. **Adaptabilidad Dinámica**: Los sistemas 6G requieren adaptación en tiempo real a condiciones de canal rápidamente cambiantes, patrones de tráfico heterogéneos, y requisitos de calidad de servicio (QoS) diversos que superan las capacidades de algoritmos pre-programados [12].

4. **Optimización End-to-End**: El enfoque tradicional de optimización por componentes individuales puede resultar sub-óptimo. Las redes neuronales profundas permiten optimización conjunta de toda la cadena de transmisión-recepción [13], [14].

5. **Aprendizaje de Patrones Ocultos**: El DL puede descubrir estructuras y regularidades en datos de canal que no son evidentes para diseñadores humanos, potencialmente superando esquemas diseñados manualmente [15].

### B. Transición desde Enfoques Tradicionales a Nativos de IA

El diseño tradicional de la capa física se fundamenta en la descomposición del sistema de comunicaciones en bloques funcionales independientes: codificación de canal, modulación, ecualización, demodulación, y decodificación. Cada bloque se optimiza individualmente basándose en modelos teóricos del canal y criterios como la minimización de la probabilidad de error de bit (BER) o maximización de la capacidad de Shannon [16].

Matemáticamente, consideremos el modelo de sistema discreto en tiempo:

$$\mathbf{y} = \mathbf{H}\mathbf{x} + \mathbf{n} \tag{1}$$

donde $\mathbf{x} \in \mathbb{C}^{N_t}$ es el vector de símbolos transmitidos, $\mathbf{H} \in \mathbb{C}^{N_r \times N_t}$ es la matriz de canal MIMO, $\mathbf{n} \sim \mathcal{CN}(0, \sigma^2\mathbf{I}_{N_r})$ es el ruido gaussiano complejo, y $\mathbf{y} \in \mathbb{C}^{N_r}$ es el vector recibido [17].

El enfoque tradicional diseña el transmisor $f_{\text{TX}}(\cdot)$ y receptor $f_{\text{RX}}(\cdot)$ como funciones separadas:

$$\hat{\mathbf{s}} = f_{\text{RX}}(\mathbf{y}, \hat{\mathbf{H}}) = f_{\text{RX}}(\mathbf{H}f_{\text{TX}}(\mathbf{s}) + \mathbf{n}, \hat{\mathbf{H}}) \tag{2}$$

donde $\mathbf{s}$ son los bits de información, $\hat{\mathbf{H}}$ es una estimación del canal, y $\hat{\mathbf{s}}$ son los bits decodificados [18].

En contraste, el enfoque nativo de IA considera el sistema de comunicación completo como una función parametrizada por redes neuronales profundas $f_{\theta}(\cdot)$ y $g_{\phi}(\cdot)$ para transmisión y recepción respectivamente, optimizadas end-to-end:

$$\theta^*, \phi^* = \arg\min_{\theta,\phi} \mathbb{E}_{\mathbf{s},\mathbf{H},\mathbf{n}}\left[\mathcal{L}(\mathbf{s}, g_{\phi}(\mathbf{H}f_{\theta}(\mathbf{s}) + \mathbf{n}))\right] \tag{3}$$

donde $\mathcal{L}(\cdot)$ es una función de pérdida diferenciable (típicamente entropía cruzada para clasificación de símbolos) y la esperanza se toma sobre la distribución conjunta de mensajes, realizaciones de canal, y ruido [19], [20].

Esta formulación permite que el sistema aprenda representaciones óptimas directamente de los datos, potencialmente superando diseños manuales al explotar regularidades estadísticas que no son capturadas por modelos simplificados [21].

### C. Arquitecturas Fundamentales de Deep Learning para PHY

Las arquitecturas de DL aplicadas a la capa física incluyen diversos paradigmas, cada uno con características particulares adecuadas para diferentes sub-problemas [22], [23]:

**1) Redes Feedforward Profundas (DNN)**: Las redes neuronales totalmente conectadas con múltiples capas ocultas constituyen la arquitectura más básica. Para un problema de detección de símbolos, una DNN mapea señales recibidas $\mathbf{y}$ a estimaciones de bits transmitidos:

$$\mathbf{h}^{(0)} = \mathbf{y} \tag{4}$$
$$\mathbf{h}^{(l)} = \sigma\left(\mathbf{W}^{(l)}\mathbf{h}^{(l-1)} + \mathbf{b}^{(l)}\right), \quad l = 1,\ldots,L-1 \tag{5}$$
$$\hat{\mathbf{s}} = \text{softmax}\left(\mathbf{W}^{(L)}\mathbf{h}^{(L-1)} + \mathbf{b}^{(L)}\right) \tag{6}$$

donde $\sigma(\cdot)$ es una función de activación no lineal (ReLU, tanh), $\mathbf{W}^{(l)}$ y $\mathbf{b}^{(l)}$ son matrices de pesos y vectores de sesgo de la capa $l$ [24].

**2) Redes Neuronales Convolucionales (CNN)**: Las CNN explotan estructura espacial o temporal en señales mediante operaciones de convolución que comparten parámetros:

$$\mathbf{h}^{(l)}_i = \sigma\left(\sum_{j}\sum_{k}\mathbf{W}^{(l)}_{i,j,k}\mathbf{h}^{(l-1)}_{j,k} + b^{(l)}_i\right) \tag{7}$$

donde el índice $k$ representa desplazamiento temporal o espacial. Las CNN son particularmente efectivas para procesamiento de secuencias temporales de símbolos o explotar correlación espacial en arrays de antenas [25], [26].

**3) Redes Neuronales Recurrentes (RNN) y LSTM**: Para capturar dependencias temporales en secuencias de símbolos o evolución temporal del canal, se utilizan arquitecturas recurrentes:

$$\mathbf{h}_t = \sigma(\mathbf{W}_{hh}\mathbf{h}_{t-1} + \mathbf{W}_{xh}\mathbf{x}_t + \mathbf{b}_h) \tag{8}$$
$$\mathbf{o}_t = \mathbf{W}_{ho}\mathbf{h}_t + \mathbf{b}_o \tag{9}$$

Las Long Short-Term Memory (LSTM) networks extienden este concepto con mecanismos de compuerta para capturar dependencias de largo alcance:

$$\mathbf{f}_t = \sigma_g(\mathbf{W}_f\mathbf{x}_t + \mathbf{U}_f\mathbf{h}_{t-1} + \mathbf{b}_f) \tag{10}$$
$$\mathbf{i}_t = \sigma_g(\mathbf{W}_i\mathbf{x}_t + \mathbf{U}_i\mathbf{h}_{t-1} + \mathbf{b}_i) \tag{11}$$
$$\mathbf{o}_t = \sigma_g(\mathbf{W}_o\mathbf{x}_t + \mathbf{U}_o\mathbf{h}_{t-1} + \mathbf{b}_o) \tag{12}$$
$$\tilde{\mathbf{c}}_t = \sigma_c(\mathbf{W}_c\mathbf{x}_t + \mathbf{U}_c\mathbf{h}_{t-1} + \mathbf{b}_c) \tag{13}$$
$$\mathbf{c}_t = \mathbf{f}_t \odot \mathbf{c}_{t-1} + \mathbf{i}_t \odot \tilde{\mathbf{c}}_t \tag{14}$$
$$\mathbf{h}_t = \mathbf{o}_t \odot \sigma_h(\mathbf{c}_t) \tag{15}$$

donde $\mathbf{f}_t$, $\mathbf{i}_t$, $\mathbf{o}_t$ son compuertas de olvido, entrada y salida respectivamente, $\mathbf{c}_t$ es el estado de celda, y $\odot$ denota producto elemento-a-elemento [27], [28].

**4) Autocodificadores (AE)**: Los autocodificadores representan toda la cadena de comunicación como un sistema de codificación-decodificación aprendido:

$$\text{Encoder: } \mathbf{z} = f_{\text{enc}}(\mathbf{s}; \theta_{\text{enc}}) \tag{16}$$
$$\text{Channel: } \mathbf{y} = \mathcal{C}(\mathbf{z}) \tag{17}$$
$$\text{Decoder: } \hat{\mathbf{s}} = f_{\text{dec}}(\mathbf{y}; \theta_{\text{dec}}) \tag{18}$$

La función objetivo es minimizar la pérdida de reconstrucción:

$$\mathcal{L}(\theta_{\text{enc}}, \theta_{\text{dec}}) = \mathbb{E}_{\mathbf{s},\mathcal{C}}\left[\|\mathbf{s} - \hat{\mathbf{s}}\|^2\right] \tag{19}$$

Los autocodificadores variacionales (VAE) introducen regularización probabilística:

$$\mathcal{L}_{\text{VAE}} = \mathbb{E}_{q_{\phi}(\mathbf{z}|\mathbf{s})}\left[\log p_{\theta}(\mathbf{s}|\mathbf{z})\right] - D_{KL}(q_{\phi}(\mathbf{z}|\mathbf{s})\|p(\mathbf{z})) \tag{20}$$

donde $D_{KL}$ es la divergencia de Kullback-Leibler que actúa como regularizador [29], [30].

**5) Redes Generativas Adversarias (GAN)**: Las GAN se utilizan para modelado y síntesis de canales realistas mediante competencia entre generador y discriminador:

$$\min_G \max_D \mathbb{E}_{\mathbf{h}\sim p_{\text{data}}(\mathbf{h})}\left[\log D(\mathbf{h})\right] + \mathbb{E}_{\mathbf{z}\sim p_{\mathbf{z}}(\mathbf{z})}\left[\log(1-D(G(\mathbf{z})))\right] \tag{21}$$

El generador $G(\mathbf{z})$ aprende a generar realizaciones de canal sintéticas indistinguibles de datos reales según el discriminador $D(\mathbf{h})$ [31], [32].

**6) Transformers y Mecanismos de Atención**: Introducidos originalmente para procesamiento de lenguaje natural, los transformers se han adaptado para procesamiento de señales en comunicaciones mediante mecanismos de auto-atención:

$$\text{Attention}(\mathbf{Q}, \mathbf{K}, \mathbf{V}) = \text{softmax}\left(\frac{\mathbf{Q}\mathbf{K}^T}{\sqrt{d_k}}\right)\mathbf{V} \tag{22}$$

donde $\mathbf{Q}$, $\mathbf{K}$, $\mathbf{V}$ son matrices de consulta, clave y valor derivadas de las señales de entrada mediante proyecciones lineales. Los transformers son particularmente efectivos para capturar dependencias de largo alcance en secuencias temporales y correlaciones espaciales en sistemas MIMO masivos [33], [34].

**7) Aprendizaje por Refuerzo Profundo (DRL)**: Para problemas de optimización secuencial y asignación de recursos, el DRL modela el sistema como un proceso de decisión de Markov (MDP) con tupla $(\mathcal{S}, \mathcal{A}, \mathcal{P}, \mathcal{R}, \gamma)$ donde $\mathcal{S}$ es el espacio de estados, $\mathcal{A}$ es el espacio de acciones, $\mathcal{P}$ define transiciones, $\mathcal{R}$ es la función de recompensa, y $\gamma$ es el factor de descuento [35].

El objetivo es aprender una política óptima $\pi^*$ que maximice el retorno esperado:

$$\pi^* = \arg\max_{\pi} \mathbb{E}\left[\sum_{t=0}^{\infty}\gamma^t R(s_t, a_t) \Big| \pi\right] \tag{23}$$

Algoritmos como Deep Q-Networks (DQN), Policy Gradient, Actor-Critic, y Proximal Policy Optimization (PPO) se utilizan para aproximar $\pi^*$ mediante redes neuronales [36], [37].


### D. Contribuciones del Artículo

Este artículo realiza las siguientes contribuciones principales al estado del arte:

**1) Revisión Unificada y Exhaustiva**: Se presenta un análisis completo e integrado de técnicas de Inteligencia Artificial y Deep Learning aplicadas a todos los componentes críticos de la capa física en sistemas 6G, consolidando conocimiento disperso en múltiples subcampos y proporcionando una visión holística del ecosistema.

**2) Fundamentación Matemática Rigurosa**: Cada técnica se examina con detalle analítico profundo, incluyendo formulaciones de optimización subyacentes, arquitecturas de redes neuronales, funciones de pérdida, y garantías teóricas cuando existen. Se establecen conexiones explícitas entre métodos tradicionales basados en modelos y enfoques data-driven.

**3) Taxonomía de Arquitecturas Neuronales**: Se desarrolla una clasificación sistemática de arquitecturas de Deep Learning para la capa física, identificando qué paradigmas son más apropiados para cada problema específico: redes feedforward para detección, CNNs para explotación de estructura espacial-frecuencial, RNNs/LSTMs para predicción temporal, autocodificadores para compresión, transformers para captura de dependencias globales, y aprendizaje por refuerzo para optimización secuencial.

**4) Análisis de Rendimiento Comparativo**: Se proporcionan resultados cuantitativos detallados comparando métodos basados en IA con técnicas tradicionales a través de múltiples dimensiones: precisión, complejidad computacional, latencia, consumo energético, y robustez. Se identifican regímenes operacionales donde cada enfoque es superior.

**5) Evaluación de Viabilidad Práctica**: Se abordan críticamente los desafíos de implementación real, incluyendo complejidad computacional, requisitos de hardware, generalización a escenarios no vistos, robustez adversarial, estandarización, interoperabilidad, y sostenibilidad ambiental. Se examinan técnicas de optimización como cuantización, poda, destilación de conocimiento, y aceleración por hardware.

**6) Identificación de Direcciones Futuras**: Se analizan tendencias emergentes y áreas de investigación abierta, incluyendo comunicaciones semánticas, meta-learning, continual learning, neuromorfic computing, integración con quantum computing, y marcos teóricos para establecer límites fundamentales de comunicaciones aprendidas.

**7) Perspectiva de Despliegue**: Se discute la transición desde sistemas actuales hacia arquitecturas 6G nativas de IA, incluyendo roadmaps tecnológicos, consideraciones de estandarización, implicaciones para operadores y fabricantes, y desafíos socio-económicos.


### E. Estructura del Artículo

El resto de este artículo está organizado como sigue. La Sección II presenta técnicas de IA para estimación y predicción de canal. La Sección III discute detección de señales con redes neuronales. La Sección IV presenta beamforming inteligente. La Sección V analiza gestión de recursos espectrales mediante IA. La Sección VI discute modulación y forma de onda adaptativas. La Sección VII introduce comunicaciones semánticas. La Sección VIII aborda desafíos de implementación. La Sección IX sintetiza los aportes del artículo. La Sección X identifica desafíos abiertos y direcciones futuras. La Sección XI concluye.

---

## II. ESTIMACIÓN Y PREDICCIÓN DE CANAL MEDIANTE DEEP LEARNING

La estimación precisa del canal de comunicación es fundamental para sistemas de comunicaciones inalámbricas coherentes, afectando directamente el rendimiento de ecualización, detección, y procesamiento MIMO [38]. Los métodos tradicionales como estimación por mínimos cuadrados (LS), mínimo error cuadrático medio (MMSE), y técnicas basadas en pilotos enfrentan limitaciones en escenarios 6G caracterizados por alta movilidad, canales de alta dimensionalidad, y recursos de piloto limitados [39], [40].

### A. Formulación del Problema de Estimación de Canal

En un sistema OFDM/OFDMA multiportadora con $N$ subportadoras y $N_t$ antenas transmisoras, $N_r$ antenas receptoras, la señal recibida en la subportadora $k$ y símbolo temporal $t$ se expresa:

$$\mathbf{Y}[k,t] = \mathbf{H}[k,t]\mathbf{X}[k,t] + \mathbf{N}[k,t] \tag{24}$$

donde $\mathbf{Y}[k,t] \in \mathbb{C}^{N_r \times 1}$, $\mathbf{H}[k,t] \in \mathbb{C}^{N_r \times N_t}$ es la respuesta en frecuencia del canal, $\mathbf{X}[k,t] \in \mathbb{C}^{N_t \times 1}$ son símbolos transmitidos, y $\mathbf{N}[k,t] \sim \mathcal{CN}(0, \sigma^2\mathbf{I})$ es ruido [41].

El problema de estimación de canal consiste en estimar $\hat{\mathbf{H}}[k,t]$ a partir de observaciones $\mathbf{Y}[k,t]$ en posiciones de piloto conocidas y potencialmente símbolos de datos previamente detectados [42].

**Estimación LS Tradicional**: En posiciones de piloto donde $\mathbf{X}_p$ es conocido:

$$\hat{\mathbf{H}}_{\text{LS}} = \mathbf{Y}_p\mathbf{X}_p^{\dagger} \tag{25}$$

donde $\mathbf{X}_p^{\dagger} = (\mathbf{X}_p^H\mathbf{X}_p)^{-1}\mathbf{X}_p^H$ es la pseudo-inversa. El estimador LS no requiere conocimiento estadístico del canal pero tiene alto error cuadrático medio (MSE) en condiciones de bajo SNR [43].

**Estimación MMSE Tradicional**: El estimador MMSE minimiza el MSE esperado:

$$\hat{\mathbf{H}}_{\text{MMSE}} = \mathbf{R}_{\mathbf{H}\mathbf{H}}\mathbf{R}_{\tilde{\mathbf{H}}\tilde{\mathbf{H}}}^{-1}\hat{\mathbf{H}}_{\text{LS}} \tag{26}$$

donde $\mathbf{R}_{\mathbf{H}\mathbf{H}} = \mathbb{E}[\mathbf{H}\mathbf{H}^H]$ es la matriz de covarianza del canal y $\mathbf{R}_{\tilde{\mathbf{H}}\tilde{\mathbf{H}}} = \mathbf{R}_{\mathbf{H}\mathbf{H}} + \sigma^2(\mathbf{X}_p\mathbf{X}_p^H)^{-1}$ es la covarianza del error [44].

El estimador MMSE requiere conocimiento de estadísticas de segundo orden del canal, que pueden ser difíciles de obtener o no estacionarias en entornos dinámicos [45].

### B. Arquitecturas de DL para Estimación de Canal

**1) DNN para Estimación Directa**: Una aproximación directa utiliza DNNs para mapear señales recibidas de piloto a estimaciones de canal [46], [47]:

$$\hat{\mathbf{H}} = f_{\text{DNN}}(\mathbf{Y}_p; \theta) \tag{27}$$

donde $f_{\text{DNN}}$ es una red neuronal profunda con parámetros $\theta$ entrenados para minimizar:

$$\mathcal{L}(\theta) = \mathbb{E}\left[\|\mathbf{H} - \hat{\mathbf{H}}\|_F^2\right] \tag{28}$$

siendo $\|\cdot\|_F$ la norma de Frobenius. La red aprende implícitamente las estadísticas del canal y la estructura de correlación desde los datos de entrenamiento [48].

Para un sistema con $N_t = 4$ antenas transmisoras, $N_r = 4$ receptoras, y $N_p = 16$ pilotos, la entrada tiene dimensión $2N_rN_p$ (partes real e imaginaria), y la salida tiene dimensión $2N_rN_t$. Una arquitectura típica incluye:

$$\text{Input}(128) \rightarrow \text{Dense}(256, \text{ReLU}) \rightarrow \text{Dense}(512, \text{ReLU}) \rightarrow \tag{29}$$
$$\text{Dense}(512, \text{ReLU}) \rightarrow \text{Dense}(256, \text{ReLU}) \rightarrow \text{Output}(32) \tag{30}$$

**2) CNN para Explotación de Correlación Espacio-Frecuencial**: Los canales inalámbricos exhiben correlación en dominios espacial (entre antenas), frecuencial (entre subportadoras), y temporal [49]. Las CNNs pueden explotar esta estructura mediante filtros convolucionales:

$$\mathbf{H}^{(l)}[i,j,k] = \sigma\left(\sum_{m,n,p}\mathbf{W}^{(l)}[m,n,p]\mathbf{H}^{(l-1)}[i+m,j+n,k+p] + b^{(l)}\right) \tag{31}$$

donde los índices $i,j,k$ corresponden a dimensiones de antena, frecuencia, y tiempo [50], [51].

Estudios recientes demuestran que CNNs con arquitectura ResNet pueden reducir el MSE de estimación en 3-5 dB comparado con MMSE en canales con alta correlación espacial [52].

**3) Arquitecturas Basadas en Transformers**: Los transformers con mecanismos de auto-atención pueden capturar dependencias de largo alcance en el dominio de frecuencia sin asumir modelos de correlación específicos [53]:

$$\text{Attention}(\mathbf{Q}, \mathbf{K}, \mathbf{V}) = \text{softmax}\left(\frac{\mathbf{Q}\mathbf{K}^T}{\sqrt{d_k}}\right)\mathbf{V} \tag{32}$$

donde las matrices de consulta, clave y valor se derivan de las observaciones de canal mediante proyecciones lineales aprendidas. El mecanismo de atención asigna pesos dinámicos a diferentes posiciones de frecuencia basándose en su relevancia para estimar una posición objetivo [54].

**4) Estimación de Canal Asistida por GAN**: Las GANs se utilizan para refinar estimaciones preliminares generando realizaciones de canal más realistas [55], [56]:

$$\hat{\mathbf{H}}_{\text{refined}} = G(\hat{\mathbf{H}}_{\text{LS}}; \theta_G) \tag{33}$$

El generador $G$ se entrena adversarialmente contra un discriminador $D$ que intenta distinguir canales reales de refinados:

$$\min_{\theta_G}\max_{\theta_D} \mathbb{E}_{\mathbf{H}}[\log D(\mathbf{H})] + \mathbb{E}_{\hat{\mathbf{H}}_{\text{LS}}}[\log(1-D(G(\hat{\mathbf{H}}_{\text{LS}})))] \tag{34}$$

Adicionalmente, una pérdida de reconstrucción asegura fidelidad:

$$\mathcal{L}_{\text{total}} = \mathcal{L}_{\text{adv}} + \lambda\mathcal{L}_{\text{recon}} \tag{35}$$
$$\mathcal{L}_{\text{recon}} = \mathbb{E}\left[\|\mathbf{H} - G(\hat{\mathbf{H}}_{\text{LS}})\|_F^2\right] \tag{36}$$

Esta aproximación ha demostrado mejoras sustanciales en escenarios con pilotos extremadamente escasos [57].

### C. Predicción de Canal mediante RNN y LSTM

En sistemas de alta movilidad y aplicaciones con requisitos de latencia ultra-baja, la predicción de canal futuro permite compensación proactiva y scheduling predictivo [58], [59]. La evolución temporal del canal puede modelarse como un proceso estocástico:

$$\mathbf{H}[t+1] = f(\mathbf{H}[t], \mathbf{H}[t-1], \ldots, \mathbf{H}[t-L]) + \mathbf{e}[t] \tag{37}$$

donde $f(\cdot)$ es una función no lineal y $\mathbf{e}[t]$ representa innovación estocástica [60].

**RNN/LSTM para Predicción Temporal**: Las LSTMs son particularmente efectivas para capturar dependencias temporales en secuencias de canal [61], [62]:

$$\hat{\mathbf{H}}[t+\Delta t] = f_{\text{LSTM}}(\mathbf{H}[t], \mathbf{H}[t-1], \ldots, \mathbf{H}[t-L]; \theta) \tag{38}$$

La arquitectura LSTM mantiene un estado de celda $\mathbf{c}_t$ que acumula información de largo plazo, mientras que compuertas controlan el flujo de información:

$$\mathbf{f}_t = \sigma(\mathbf{W}_f[\mathbf{h}_{t-1}, \mathbf{H}[t]] + \mathbf{b}_f) \tag{39}$$
$$\mathbf{i}_t = \sigma(\mathbf{W}_i[\mathbf{h}_{t-1}, \mathbf{H}[t]] + \mathbf{b}_i) \tag{40}$$
$$\tilde{\mathbf{c}}_t = \tanh(\mathbf{W}_c[\mathbf{h}_{t-1}, \mathbf{H}[t]] + \mathbf{b}_c) \tag{41}$$
$$\mathbf{c}_t = \mathbf{f}_t \odot \mathbf{c}_{t-1} + \mathbf{i}_t \odot \tilde{\mathbf{c}}_t \tag{42}$$
$$\mathbf{o}_t = \sigma(\mathbf{W}_o[\mathbf{h}_{t-1}, \mathbf{H}[t]] + \mathbf{b}_o) \tag{43}$$
$$\mathbf{h}_t = \mathbf{o}_t \odot \tanh(\mathbf{c}_t) \tag{44}$$
$$\hat{\mathbf{H}}[t+\Delta t] = \mathbf{W}_h\mathbf{h}_t + \mathbf{b}_h \tag{45}$$

El entrenamiento minimiza el error de predicción:

$$\mathcal{L}(\theta) = \sum_{t=1}^{T-\Delta t}\|\mathbf{H}[t+\Delta t] - \hat{\mathbf{H}}[t+\Delta t]\|_F^2 \tag{46}$$

**Gated Recurrent Units (GRU)**: Una variante simplificada de LSTM con menor complejidad computacional pero rendimiento comparable [63]:

$$\mathbf{r}_t = \sigma(\mathbf{W}_r[\mathbf{h}_{t-1}, \mathbf{H}[t]]) \tag{47}$$
$$\mathbf{z}_t = \sigma(\mathbf{W}_z[\mathbf{h}_{t-1}, \mathbf{H}[t]]) \tag{48}$$
$$\tilde{\mathbf{h}}_t = \tanh(\mathbf{W}[\mathbf{r}_t \odot \mathbf{h}_{t-1}, \mathbf{H}[t]]) \tag{49}$$
$$\mathbf{h}_t = (1-\mathbf{z}_t) \odot \mathbf{h}_{t-1} + \mathbf{z}_t \odot \tilde{\mathbf{h}}_t \tag{50}$$

donde $\mathbf{r}_t$ y $\mathbf{z}_t$ son compuertas de reset y actualización respectivamente.

**Predicción Multistep**: Para predicción de múltiples pasos hacia el futuro, se emplean estrategias recursivas o direct multistep:

- **Recursiva**: $\hat{\mathbf{H}}[t+k] = f(\hat{\mathbf{H}}[t+k-1], \ldots)$
- **Direct**: $\hat{\mathbf{H}}[t+k] = f_k(\mathbf{H}[t], \mathbf{H}[t-1], \ldots)$

La aproximación direct entrena modelos separados para cada horizonte de predicción, evitando propagación de errores pero incrementando complejidad de modelo [64].

**Modelos Seq2Seq con Mecanismos de Atención**: Para capturar patrones complejos, arquitecturas encoder-decoder con atención permiten al decodificador enfocarse en partes relevantes de la secuencia de entrada [65]:

$$\text{Context: } \mathbf{c}_t = \sum_{i=1}^{T}\alpha_{t,i}\mathbf{h}_i \tag{51}$$
$$\alpha_{t,i} = \frac{\exp(e_{t,i})}{\sum_{j=1}^{T}\exp(e_{t,j})} \tag{52}$$
$$e_{t,i} = \text{score}(\mathbf{s}_{t-1}, \mathbf{h}_i) \tag{53}$$

donde $\mathbf{h}_i$ son estados ocultos del encoder, $\mathbf{s}_t$ es el estado del decoder, y $\mathbf{c}_t$ es el vector de contexto ponderado por coeficientes de atención $\alpha_{t,i}$ [66].

### D. Explotación de Estructura Dispersa

Los canales mmWave y THz típicamente exhiben estructura dispersa en el dominio angular debido a propagación limitada por trayectorias [67], [68]. Esta dispersidad puede explotarse para reducir overhead de estimación y complejidad computacional.

**Compressed Sensing (CS) con DL**: La teoría de compressed sensing establece que señales dispersas pueden recuperarse de mediciones sub-Nyquist mediante optimización $\ell_1$:

$$\min_{\mathbf{h}} \|\mathbf{h}\|_1 \quad \text{s.t.} \quad \mathbf{y} = \mathbf{\Phi}\mathbf{h} \tag{54}$$

donde $\mathbf{h}$ es la representación dispersa del canal, $\mathbf{\Phi}$ es la matriz de medición (pilotos), y $\mathbf{y}$ son observaciones [69].

Las redes neuronales pueden aprender a resolver este problema de optimización de forma más eficiente que algoritmos iterativos tradicionales (OMP, CoSaMP) mediante redes de despliegue (unfolding) [70], [71]:

$$\mathbf{h}^{(k+1)} = \mathcal{N}_{\theta}\left(\mathbf{h}^{(k)}, \mathbf{\Phi}, \mathbf{y}\right) \tag{55}$$

donde cada iteración del algoritmo de optimización se mapea a una capa de la red neuronal, permitiendo aprendizaje de parámetros de regularización y operadores de umbralización [72].

**Learned ISTA (LISTA)**: Una instancia específica de unfolding aplica Iterative Shrinkage-Thresholding Algorithm (ISTA):

$$\mathbf{h}^{(k+1)} = \eta_{\lambda^{(k)}}\left(\mathbf{h}^{(k)} + \mathbf{W}^{(k)}(\mathbf{y} - \mathbf{\Phi}\mathbf{h}^{(k)})\right) \tag{56}$$

donde $\eta_{\lambda}(\cdot)$ es el operador de soft-thresholding:

$$\eta_{\lambda}(x) = \text{sign}(x)\max(|x|-\lambda, 0) \tag{57}$$

Los parámetros $\mathbf{W}^{(k)}$ y $\lambda^{(k)}$ se aprenden para cada capa $k$, acelerando significativamente la convergencia comparado con ISTA clásico [73].

### E. Estimación de Canal sin Pilotos mediante DL

Los esquemas de estimación sin pilotos (blind channel estimation) explotan estructura de señales de datos para estimar el canal sin dedicar recursos explícitos a pilotos, maximizando eficiencia espectral [74], [75].

**Autocodificadores para Estimación Blind**: Un autocodificador puede aprender conjuntamente codificación, estimación de canal, y decodificación:

$$\text{Encoder: } \mathbf{x} = f_{\text{enc}}(\mathbf{s}; \theta_{\text{enc}}) \tag{58}$$
$$\text{Channel: } \mathbf{y} = \mathbf{H}\mathbf{x} + \mathbf{n} \tag{59}$$
$$\text{Estimator: } \hat{\mathbf{H}} = f_{\text{est}}(\mathbf{y}; \theta_{\text{est}}) \tag{60}$$
$$\text{Decoder: } \hat{\mathbf{s}} = f_{\text{dec}}(\mathbf{y}, \hat{\mathbf{H}}; \theta_{\text{dec}}) \tag{61}$$

La función de pérdida combina reconstrucción de datos y calidad de estimación:

$$\mathcal{L} = \mathbb{E}\left[\|\mathbf{s} - \hat{\mathbf{s}}\|^2 + \beta\|\mathbf{H} - \hat{\mathbf{H}}\|_F^2\right] \tag{62}$$

El encoder aprende a insertar estructura implícita en señales transmitidas que facilita estimación ciega [76].

**Deep Blind Equalization**: Extiende técnicas clásicas como Constant Modulus Algorithm (CMA) utilizando DNNs para aprender funciones de costo adaptativas [77]:

$$\mathcal{L}_{\text{CMA}} = \mathbb{E}\left[(|\hat{s}[n]|^2 - R_2)^2\right] \tag{63}$$

donde $R_2 = \mathbb{E}[|s[n]|^4]/\mathbb{E}[|s[n]|^2]$ es el módulo constante objetivo. Las DNNs pueden aprender generalizaciones de este criterio para constelaciones arbitrarias [78].

### F. Transfer Learning y Meta-Learning para Estimación de Canal

En sistemas prácticos, el entrenamiento de modelos DL para cada escenario de canal específico es prohibitivamente costoso. Transfer learning y meta-learning permiten adaptación rápida a nuevas condiciones con datos limitados [79], [80].

**Transfer Learning**: Un modelo pre-entrenado en un conjunto de escenarios de canal diversos se adapta a un escenario objetivo específico mediante fine-tuning de capas superiores:

1. **Pre-entrenamiento**: Entrenar $f_{\theta}$ en dataset grande $\mathcal{D}_{\text{source}}$
2. **Fine-tuning**: Congelar capas inferiores y re-entrenar capas superiores en $\mathcal{D}_{\text{target}}$

$$\theta_{\text{target}}^* = \arg\min_{\theta_{\text{upper}}} \mathcal{L}_{\text{target}}(f(\cdot; \theta_{\text{frozen}}, \theta_{\text{upper}})) \tag{64}$$

Esta aproximación reduce significativamente los requisitos de datos de entrenamiento y tiempo de adaptación [81].

**Model-Agnostic Meta-Learning (MAML)**: MAML busca parámetros iniciales $\theta$ que permitan adaptación rápida a nuevas tareas con pocos gradientes:

$$\theta^* = \arg\min_{\theta} \sum_{\mathcal{T}_i \sim p(\mathcal{T})} \mathcal{L}_{\mathcal{T}_i}\left(f_{\theta'_i}\right) \tag{65}$$

donde $\theta'_i = \theta - \alpha\nabla_{\theta}\mathcal{L}_{\mathcal{T}_i}(f_{\theta})$ son parámetros adaptados después de un paso de gradiente en la tarea $\mathcal{T}_i$ [82].

Para estimación de canal, cada tarea $\mathcal{T}_i$ corresponde a un escenario de propagación diferente (indoor, outdoor, vehicular, etc.). MAML aprende una representación que generaliza bien a través de escenarios diversos [83].

### G. Resultados de Rendimiento y Análisis Comparativo

Estudios empíricos extensivos han comparado métodos basados en DL con técnicas tradicionales en diversos escenarios:

**Escenario MIMO Masivo**: Para un sistema con $N_t = 64$, $N_r = 16$, frecuencia portadora 28 GHz, y modelo de canal 3GPP 38.901 UMi [84]:

- LS: MSE = -15 dB @ SNR = 10 dB
- MMSE: MSE = -22 dB @ SNR = 10 dB
- DNN (5 capas, 512 neuronas): MSE = -25 dB @ SNR = 10 dB
- CNN-ResNet: MSE = -27 dB @ SNR = 10 dB
- Transformer: MSE = -28 dB @ SNR = 10 dB

Las ganancias son particularmente pronunciadas en regímenes de bajo SNR y alta movilidad [85].

**Predicción de Canal en Alta Movilidad**: En escenarios vehiculares (velocidad 120 km/h, frecuencia 5.9 GHz):

- Modelo AR clásico: Error de predicción 15% @ horizonte 10 ms
- LSTM (3 capas, 256 unidades): Error de predicción 8% @ horizonte 10 ms
- Transformer con atención temporal: Error de predicción 6% @ horizonte 10 ms

La predicción precisa permite CSI proactivo y reduce latencia de feedback [86].

**Complejidad Computacional**: Un aspecto crítico es la complejidad:

- MMSE: $\mathcal{O}(N_t^3N_r)$ operaciones
- DNN: $\mathcal{O}(L \cdot N_h^2)$ donde $L$ es número de capas y $N_h$ dimensión de capa oculta
- CNN: Significativamente menor debido a compartir parámetros
- Inferencia en hardware especializado (GPU/TPU): latencia sub-milisegundo

El despliegue eficiente requiere técnicas de cuantización, poda, y destilación de conocimiento para cumplir restricciones de latencia y energía [87], [88].

---

## III. DETECCIÓN DE SEÑALES CON REDES NEURONALES

La detección de señales es un componente crítico del receptor, responsable de estimar símbolos o bits transmitidos desde señales recibidas ruidosas [265]. En sistemas MIMO de alta dimensión, la detección óptima tiene complejidad exponencial, motivando aproximaciones subóptimas [266]. El DL ofrece detectores que balancean rendimiento y complejidad mediante aprendizaje de estructuras de detección efectivas [267].

### A. Problema de Detección en Sistemas MIMO

**Formulación**: Dado el modelo de señal:

$$\mathbf{y} = \mathbf{H}\mathbf{x} + \mathbf{n} \in \mathbb{C}^{N_r} \tag{66}$$

donde $\mathbf{x} \in \mathcal{X}^{N_t}$ con $\mathcal{X}$ siendo la constelación (e.g., $M$-QAM), detectar $\hat{\mathbf{x}}$ minimizando probabilidad de error [268].

**Maximum Likelihood (ML) Detection**:

$$\hat{\mathbf{x}}_{\text{ML}} = \arg\min_{\mathbf{x} \in \mathcal{X}^{N_t}} \|\mathbf{y} - \mathbf{H}\mathbf{x}\|^2 \tag{67}$$

Complejidad: $\mathcal{O}(M^{N_t})$ evaluaciones, exponencial en número de antenas transmisoras [269].

**Linear Detectors**: Zero-forcing (ZF) y MMSE son lineales con complejidad $\mathcal{O}(N_t^3)$:

$$\hat{\mathbf{x}}_{\text{ZF}} = (\mathbf{H}^H\mathbf{H})^{-1}\mathbf{H}^H\mathbf{y} \tag{68}$$
$$\hat{\mathbf{x}}_{\text{MMSE}} = (\mathbf{H}^H\mathbf{H} + \sigma^2\mathbf{I})^{-1}\mathbf{H}^H\mathbf{y} \tag{69}$$

Rendimiento subóptimo especialmente en alta carga del sistema ($N_t \approx N_r$) [270].

### B. Redes Neuronales para Detección Directa

**DNN Detector**: Mapeo directo de señal recibida y CSI a símbolos detectados [273]:

$$\hat{\mathbf{x}} = f_{\text{DNN}}(\mathbf{y}, \mathbf{H}; \theta) \tag{70}$$

**Arquitectura**: 
1. **Input**: $[\text{Re}(\mathbf{y}); \text{Im}(\mathbf{y}); \text{vec}(\text{Re}(\mathbf{H})); \text{vec}(\text{Im}(\mathbf{H}))]$
2. **Hidden Layers**: Múltiples capas fully connected con activaciones ReLU
3. **Output**: Para detección de símbolos complejos, $2N_t$ salidas reales; para detección de bits, $N_t \log_2 M$ salidas con sigmoid

**Función de Pérdida**: Para detección de símbolos:

$$\mathcal{L}(\theta) = \mathbb{E}\left[\|\mathbf{x} - \hat{\mathbf{x}}\|^2\right] \tag{71}$$

Para detección de bits (soft-output):

$$\mathcal{L}(\theta) = -\mathbb{E}\left[\sum_{i=1}^{N_t\log_2 M}b_i\log\hat{b}_i + (1-b_i)\log(1-\hat{b}_i)\right] \tag{72}$$

### D. Detección con Atención y Transformers

**Attention-Based Detection**: Los mecanismos de atención permiten al detector enfocarse en componentes relevantes de la señal recibida [282]:

$$\mathbf{c}_i = \sum_{j=1}^{N_r}\alpha_{i,j}\mathbf{y}_j \tag{73}$$
$$\alpha_{i,j} = \frac{\exp(\text{score}(\mathbf{q}_i, \mathbf{k}_j))}{\sum_{j'}\exp(\text{score}(\mathbf{q}_i, \mathbf{k}_{j'}))} \tag{74}$$

donde $\mathbf{q}_i$ representa query para detectar símbolo $i$, y $\mathbf{k}_j$, $\mathbf{v}_j$ son proyecciones de señales recibidas [283].

**Transformer Detector**: Arquitectura completa basada en transformers para detección MIMO [284]:

1. **Embedding**: Proyectar señales recibidas a espacio de alta dimensión
2. **Multi-Head Self-Attention**: Capturar interdependencias entre símbolos transmitidos
3. **Feed-Forward Networks**: Procesamiento no lineal
4. **Output**: Probabilidades de símbolos o LLRs de bits

La complejidad es $\mathcal{O}(N_t^2)$ por capa, más eficiente que ML para $N_t$ moderado [285].

### E. Detección para Canales No-AWGN

**Fading Channels**: Para canales con desvanecimiento, incluir estadísticas de canal en entrenamiento [286]:

$$\mathbf{y} = \mathbf{h} \odot \mathbf{H}\mathbf{x} + \mathbf{n}, \quad \mathbf{h} \sim \text{Rayleigh/Rician} \tag{75}$$

El detector aprende robustez implícita a variaciones de desvanecimiento sin diversidad explícita [287].

**Impairments de Hardware**: Los detectores neuronales pueden compensar imperfecciones de hardware (IQ imbalance, non-linearities de PA, phase noise) aprendiendo desde datos reales [288]:

$$\mathbf{y} = \text{Impairment}(\mathbf{H}\mathbf{x}) + \mathbf{n} \tag{76}$$
$$\hat{\mathbf{x}} = f_{\text{DNN}}(\mathbf{y}; \theta) \tag{77}$$

El modelo aprende inversión de impairments implícitamente [289].

### F. Detección Multi-Usuario

**NOMA con DL**: En Non-Orthogonal Multiple Access, múltiples usuarios comparten recursos mediante multiplexación en dominio de potencia [290]:

$$\mathbf{y} = \sum_{k=1}^{K}\sqrt{p_k}\mathbf{h}_k s_k + \mathbf{n} \tag{78}$$

Un detector neural realiza cancelación de interferencia sucesiva aprendida [291]:

$$\{\hat{s}_1, \ldots, \hat{s}_K\} = f_{\text{DNN}}(\mathbf{y}, \{\mathbf{h}_k\}, \{p_k\}; \theta) \tag{79}$$

**Detección Multi-Celda**: En escenarios multi-celda con interferencia, detectores basados en graph neural networks modelan estructura de interferencia [292]:

Cada usuario es un nodo, aristas representan interferencia. El GNN propaga información para cancelación cooperativa:

$$\mathbf{h}_u^{(l+1)} = \text{UPDATE}\left(\mathbf{h}_u^{(l)}, \text{AGGREGATE}(\{\mathbf{h}_v^{(l)} : v \in \mathcal{N}(u)\})\right) \tag{80}$$

### G. Complejidad y Implementación en Hardware

**Comparación de Complejidad**:

| Detector | Complejidad | Rendimiento (% de ML) |
|----------|-------------|----------------------|
| ZF | $\mathcal{O}(N_t^3)$ | 70-80% |
| MMSE | $\mathcal{O}(N_t^3)$ | 75-85% |
| Sphere Decoding | $\mathcal{O}(M^{N_t})$ worst case | 95-100% |
| DNN | $\mathcal{O}(LN_h^2)$ | 85-95% |
| DetNet | $\mathcal{O}(TN_t^2)$ | 90-98% |
| OAMP-Net | $\mathcal{O}(TN_tN_r)$ | 92-99% |

donde $T$ es número de iteraciones/capas [293].

**Implementación FPGA**: Detectores neuronales son altamente paralelizables. Implementaciones en FPGA logran:
- Throughput: >1 Gbps para $4\times 4$ MIMO
- Latencia: <10 μs
- Eficiencia energética: >100 Mbps/W [294], [295]

**Quantization**: Cuantización de pesos y activaciones a INT8/INT4 reduce memoria y potencia en $4\times-8\times$ con degradación de BER <0.5 dB [296].

---

## IV. BEAMFORMING INTELIGENTE Y GESTIÓN DE HAZ

El beamforming es una técnica fundamental en sistemas MIMO y mmWave que concentra energía de transmisión en direcciones específicas, mejorando SNR y reduciendo interferencia [297]. En sistemas 6G con arrays masivos y entornos dinámicos, el beamforming adaptativo mediante IA ofrece ventajas sustanciales sobre métodos tradicionales [298].

### A. Fundamentos de Beamforming

**Array Response**: Para un array lineal uniforme (ULA) con $N$ elementos y espaciamiento $d$, el vector de steering para ángulo de llegada/salida $\theta$ es [299]:

$$\mathbf{a}(\theta) = \frac{1}{\sqrt{N}}\left[1, e^{j2\pi d\sin\theta/\lambda}, \ldots, e^{j2\pi(N-1)d\sin\theta/\lambda}\right]^T \tag{81}$$

**Beamforming de Transmisión**: La señal transmitida es:

$$\mathbf{x} = \mathbf{w}s \tag{82}$$

donde $\mathbf{w} \in \mathbb{C}^N$ es el vector de beamforming y $s$ es el símbolo de datos. El patrón de radiación es:

$$P(\theta) = |\mathbf{a}^H(\theta)\mathbf{w}|^2 \tag{83}$$

**Diseño Clásico**: Para maximizar SNR en dirección objetivo $\theta_0$:

$$\mathbf{w}_{\text{MRT}} = \mathbf{a}(\theta_0) \tag{84}$$

Para nulificar interferencia en direcciones $\{\theta_i\}$:

$$\mathbf{w}_{\text{null}} \perp \text{span}\{\mathbf{a}(\theta_1), \ldots, \mathbf{a}(\theta_K)\} \tag{85}$$

Solución mediante optimización convexa o proyección [300].

### B. Deep Learning para Predicción de Beams

**Beam Prediction desde CSI**: En lugar de búsqueda exhaustiva sobre codebook de beams, predecir beam óptimo directamente [301]:

$$i^* = f_{\text{DNN}}(\mathbf{H}; \theta) \tag{86}$$

donde $i^*$ es el índice del beam en codebook $\{\mathbf{w}_1, \ldots, \mathbf{w}_{N_{\text{beam}}}\}$.

**Arquitectura CNN**: Explotar estructura espacial del CSI:

1. **Input**: Matriz de CSI $\mathbf{H} \in \mathbb{R}^{2N_r \times N_t}$ (real e imaginaria)
2. **Conv Layers**: Extraer características espaciales
$$\mathbf{F}^{(l)} = \text{ReLU}(\text{Conv2D}(\mathbf{F}^{(l-1)})) \tag{87}$$
3. **Global Pooling**: Agregar información espacial
4. **FC Layers**: Clasificación a índice de beam
5. **Output**: Probabilidades $\mathbf{p} = \text{softmax}(\mathbf{z}) \in [0,1]^{N_{\text{beam}}}$

**Función de Pérdida**: Cross-entropy para clasificación:

$$\mathcal{L}(\theta) = -\mathbb{E}\left[\sum_{i=1}^{N_{\text{beam}}}y_i\log p_i\right] \tag{88}$$

donde $y_i = 1$ si $i$ es el beam óptimo, 0 en otro caso [302].

### C. Beam Tracking en Movilidad

**Problema de Tracking**: En escenarios de alta movilidad (vehículos, drones), el beam óptimo cambia rápidamente. Tracking proactivo reduce latencia y overhead [303].

**RNN/LSTM para Beam Tracking**: Predecir beam futuro desde historial [304]:

$$i_{t+\Delta t}^* = f_{\text{LSTM}}(i_t^*, i_{t-1}^*, \ldots, i_{t-L}^*, \mathbf{features}_t; \theta) \tag{89}$$

donde $\mathbf{features}_t$ puede incluir posición, velocidad, SNR, etc.

**Seq2Seq con Atención**: Para predicción multi-step:

**Encoder**: Procesar secuencia histórica de beams y features
$$\mathbf{h}_t = \text{LSTM}_{\text{enc}}(\mathbf{x}_t, \mathbf{h}_{t-1}) \tag{90}$$

**Decoder**: Generar secuencia de beams futuros con atención sobre historial
$$\mathbf{s}_t = \text{LSTM}_{\text{dec}}(\hat{i}_{t-1}, \mathbf{s}_{t-1}, \mathbf{c}_t) \tag{91}$$
$$\mathbf{c}_t = \sum_{i}\alpha_{t,i}\mathbf{h}_i \tag{92}$$

Esto permite anticipar cambios de beam varios pasos adelante [305].

### D. Beamforming Sin CSI Explícito

**Aprendizaje Directo desde Señales**: En lugar de estimar CSI y luego computar beamformers, aprender mapeo directo de mediciones de canal a beamformers [306]:

$$\mathbf{w} = f_{\text{DNN}}(\mathbf{Y}_{\text{pilot}}; \theta) \tag{93}$$

donde $\mathbf{Y}_{\text{pilot}}$ son señales piloto recibidas sin estimación de canal intermedia.

**End-to-End Learning**: Optimizar beamformers para maximizar métrica de sistema (tasa, SINR) directamente [307]:

$$\mathcal{L}(\theta) = -\mathbb{E}\left[R(\mathbf{w}(\theta))\right] \tag{94}$$

donde $R(\mathbf{w})$ es la tasa alcanzable con beamformer $\mathbf{w}$.

**Ventajas**: 
- Evita errores de estimación de canal
- Aprende compensación de impairments implícitamente
- Menor complejidad computacional [308]

### E. Multi-User Beamforming con DL

**Problema MU-MISO**: Con $K$ usuarios single-antenna, diseñar beamformers $\{\mathbf{w}_k\}$ para maximizar sum rate [309]:

$$\max_{\{\mathbf{w}_k\}} \sum_{k=1}^{K}\log_2\left(1 + \frac{|\mathbf{h}_k^H\mathbf{w}_k|^2}{\sum_{j\neq k}|\mathbf{h}_k^H\mathbf{w}_j|^2 + \sigma^2}\right) \tag{95}$$
$$\text{s.t. } \sum_{k=1}^{K}\|\mathbf{w}_k\|^2 \leq P_{\max} \tag{96}$$

Este problema es no convexo y difícil de resolver [310].

**DNN para MU Beamforming**: Aprender mapeo de canales multi-usuario a beamformers [311]:

$$\{\mathbf{w}_1, \ldots, \mathbf{w}_K\} = f_{\text{DNN}}(\mathbf{H}_1, \ldots, \mathbf{H}_K; \theta) \tag{97}$$

**Arquitectura**:
1. **Input**: Canales agregados $[\mathbf{H}_1; \ldots; \mathbf{H}_K]$
2. **Shared Layers**: Extraer características comunes
3. **User-Specific Branches**: Generar beamformer por usuario
4. **Normalization Layer**: Enforcing restricción de potencia

$$\mathbf{w}_k' = \sqrt{P_{\max}} \cdot \frac{\mathbf{w}_k}{\sqrt{\sum_{j}\|\mathbf{w}_j\|^2}} \tag{98}$$

**Unsupervised Learning**: Entrenar sin soluciones ground-truth maximizando sum rate [312]:

$$\mathcal{L}(\theta) = -\mathbb{E}\left[\sum_{k=1}^{K}\log_2(1 + \text{SINR}_k(\{\mathbf{w}_j(\theta)\}))\right] \tag{99}$$

### F. Beamforming Cooperativo con Graph Neural Networks

**Coordinated Beamforming**: En redes multi-celda, estaciones base coordinan beamforming para mitigar interferencia inter-celda [313].

**Modelado con Grafos**: Representar red como grafo:
- **Nodos**: Pares BS-usuario
- **Aristas**: Enlaces de interferencia

**GNN para Coord. Beamforming**: El GNN propaga información entre nodos para aprender beamformers que consideran interferencia de red [314]:

$$\mathbf{h}_v^{(0)} = [\mathbf{H}_v; \text{features}_v] \tag{100}$$
$$\mathbf{h}_v^{(l+1)} = \sigma\left(\mathbf{W}_{\text{self}}^{(l)}\mathbf{h}_v^{(l)} + \sum_{u \in \mathcal{N}(v)}\mathbf{W}_{\text{neigh}}^{(l)}\mathbf{h}_u^{(l)}\right) \tag{101}$$
$$\mathbf{w}_v = f_{\text{out}}(\mathbf{h}_v^{(L)}) \tag{102}$$

El GNN aprende estrategias de coordinación que balancean ganancia local vs. interferencia a vecinos [315].

### G. Hybrid Analog-Digital Beamforming

**Arquitectura Híbrida**: Combinación de beamforming analógico (phase shifters) y digital (baseband) [316]:

$$\mathbf{W} = \mathbf{F}_{\text{RF}}\mathbf{F}_{\text{BB}} \tag{103}$$

donde $\mathbf{F}_{\text{RF}} \in \mathbb{C}^{N \times N_{\text{RF}}}$ con restricción $|[\mathbf{F}_{\text{RF}}]_{i,j}| = 1/\sqrt{N}$.

**DL para Diseño Híbrido**: Aprender descomposición óptima [317]:

$$\mathbf{F}_{\text{RF}}, \mathbf{F}_{\text{BB}} = f_{\text{DNN}}(\mathbf{H}; \theta) \tag{104}$$

**Enforcing Restricciones**:
1. **Analog**: Proyectar a manifold de fase constante
$$[\mathbf{F}_{\text{RF}}]_{i,j} = \frac{1}{\sqrt{N}}e^{j\angle[\mathbf{F}_{\text{RF}}']_{i,j}} \tag{105}$$

2. **Power**: Normalizar beamformer total
$$\mathbf{F}_{\text{BB}}' = \sqrt{\frac{P_{\max}}{\|\mathbf{F}_{\text{RF}}\mathbf{F}_{\text{BB}}\|_F^2}}\mathbf{F}_{\text{BB}} \tag{106}$$

**Alternating Optimization Unfolding**: Desplegar iteraciones de optimización alternante [318]:

$$\mathbf{F}_{\text{RF}}^{(t+1)} = f_{\text{RF}}^{(t)}(\mathbf{H}, \mathbf{F}_{\text{BB}}^{(t)}; \theta_{\text{RF}}^{(t)}) \tag{107}$$
$$\mathbf{F}_{\text{BB}}^{(t+1)} = f_{\text{BB}}^{(t)}(\mathbf{H}, \mathbf{F}_{\text{RF}}^{(t+1)}; \theta_{\text{BB}}^{(t)}) \tag{108}$$

### H. Beamforming para RIS-Assisted Systems

**Modelo RIS**: Con RIS de $N$ elementos, canal efectivo es [319]:

$$\mathbf{h}_{\text{eff}} = \mathbf{h}_d + \mathbf{H}_r\mathbf{\Theta}\mathbf{g} \tag{109}$$

donde $\mathbf{\Theta} = \text{diag}(e^{j\theta_1}, \ldots, e^{j\theta_N})$ es configuración de fase RIS.

**Optimización Conjunta**: Diseñar beamformer BS $\mathbf{w}$ y fases RIS $\{\theta_n\}$ conjuntamente [320]:

$$\max_{\mathbf{w},\{\theta_n\}} |\mathbf{h}_{\text{eff}}^H\mathbf{w}|^2 \tag{110}$$
$$\text{s.t. } \|\mathbf{w}\|^2 \leq P, \quad \theta_n \in [0, 2\pi) \tag{111}$$

**DNN para RIS Beamforming**: Aprender configuración conjunta [321]:

$$\mathbf{w}, \{\theta_1, \ldots, \theta_N\} = f_{\text{DNN}}(\mathbf{h}_d, \mathbf{H}_r, \mathbf{g}; \theta) \tag{112}$$

**RL sin CSI Perfecto**: Cuando CSI de múltiples saltos es difícil de obtener, usar RL para optimizar basado en métricas [322]:

- **Estado**: SNR recibido, configuración previa
- **Acción**: Ajuste de fases RIS $\Delta\theta_n$
- **Recompensa**: Mejora en SNR

Agentes como DDPG aprenden políticas de configuración óptimas sin modelo explícito del canal [323].

## V. GESTIÓN DE RECURSOS ESPECTRALES MEDIANTE APRENDIZAJE POR REFUERZO

La asignación eficiente de recursos espectrales (potencia, ancho de banda, tiempo, bloques de recursos) es crucial para maximizar eficiencia espectral y satisfacer requisitos heterogéneos de QoS en sistemas 6G [326]. La naturaleza dinámica y combinatorial del problema motiva uso de aprendizaje por refuerzo profundo (DRL) [327].

### A. Formulación como MDP

**Proceso de Decisión de Markov**: El problema de asignación de recursos se modela como tupla $(\mathcal{S}, \mathcal{A}, \mathcal{P}, \mathcal{R}, \gamma)$ [328]:

- **Estados** $\mathcal{S}$: CSI, demanda de tráfico, buffer states, QoS requirements
$$s_t = [\mathbf{H}_t, \mathbf{Q}_t, \mathbf{B}_t, \mathbf{QoS}_t] \tag{113}$$

- **Acciones** $\mathcal{A}$: Asignación de recursos (potencia, subcanales, MCS)
$$a_t = [\mathbf{P}_t, \mathbf{SC}_t, \mathbf{MCS}_t] \tag{114}$$

- **Transiciones** $\mathcal{P}$: $s_{t+1} \sim P(\cdot|s_t, a_t)$ determinado por dinámica de canal y arribo de tráfico

- **Recompensa** $\mathcal{R}$: Función de utilidad del sistema
$$R(s_t, a_t) = \alpha \cdot \text{Throughput} - \beta \cdot \text{Delay} - \gamma \cdot \text{Power} \tag{115}$$

- **Discount factor** $\gamma \in [0,1)$: Pondera recompensas futuras [329]

**Objetivo**: Aprender política óptima $\pi^*: \mathcal{S} \to \mathcal{A}$ que maximiza retorno esperado:

$$J(\pi) = \mathbb{E}_{\pi}\left[\sum_{t=0}^{\infty}\gamma^t R(s_t, a_t)\right] \tag{116}$$

### B. Deep Q-Networks (DQN) para Asignación de Recursos

**Q-Learning**: Aprender función de valor acción-estado óptima [330]:

$$Q^*(s,a) = \mathbb{E}\left[R(s,a) + \gamma\max_{a'}Q^*(s',a')\right] \tag{117}$$

**DQN**: Aproximar $Q^*(s,a)$ mediante red neuronal profunda [331]:

$$Q(s,a;\theta) \approx Q^*(s,a) \tag{118}$$

**Arquitectura**:
1. **Input**: Representación de estado $s$
2. **Hidden Layers**: DNNs con ReLU
3. **Output**: Q-valores para cada acción $[Q(s,a_1), \ldots, Q(s,a_{|\mathcal{A}|})]$

**Entrenamiento**: Minimizar Bellman error mediante experience replay:

$$\mathcal{L}(\theta) = \mathbb{E}_{(s,a,r,s')\sim\mathcal{D}}\left[\left(r + \gamma\max_{a'}Q(s',a';\theta^-) - Q(s,a;\theta)\right)^2\right] \tag{119}$$

donde $\mathcal{D}$ es replay buffer y $\theta^-$ son parámetros de target network actualizados periódicamente [332].

**Double DQN**: Reduce sobrestimación de Q-valores usando dos redes [333]:

$$y = r + \gamma Q(s', \arg\max_{a'}Q(s',a';\theta); \theta^-) \tag{120}$$

**Dueling DQN**: Descompone Q-función en valor de estado y ventajas de acción [334]:

$$Q(s,a;\theta) = V(s;\theta_V) + A(s,a;\theta_A) - \frac{1}{|\mathcal{A}|}\sum_{a'}A(s,a';\theta_A) \tag{121}$$

### C. Policy Gradient y Actor-Critic

**Limitación de DQN**: Requiere espacio de acciones discreto y finito. Muchos problemas de asignación tienen acciones continuas (niveles de potencia) o espacios combinatorialmente grandes [335].

**Policy Gradient**: Parametrizar política directamente y optimizar mediante gradiente [336]:

$$\pi(a|s;\theta) = P(a_t=a | s_t=s) \tag{122}$$

**REINFORCE**: Gradiente del objetivo:

$$\nabla_{\theta}J(\theta) = \mathbb{E}_{\pi_{\theta}}\left[\nabla_{\theta}\log\pi(a|s;\theta)G_t\right] \tag{123}$$

donde $G_t = \sum_{k=0}^{\infty}\gamma^k R_{t+k}$ es el retorno [337].

**Actor-Critic**: Combina policy gradient (actor) con función de valor (critic) para reducir varianza [338]:

**Actor**: Actualizar política en dirección sugerida por critic
$$\theta \leftarrow \theta + \alpha\nabla_{\theta}\log\pi(a|s;\theta)A(s,a;\phi) \tag{124}$$

**Critic**: Estimar ventaja $A(s,a) = Q(s,a) - V(s)$
$$\phi \leftarrow \phi - \beta\nabla_{\phi}(R + \gamma V(s';\phi) - V(s;\phi))^2 \tag{125}$$

**A3C (Asynchronous Advantage Actor-Critic)**: Paraleliza entrenamiento con múltiples agentes explorando simultáneamente [339].

### D. Proximal Policy Optimization (PPO)

PPO es un algoritmo de policy gradient que limita actualizaciones de política para evitar cambios drásticos que degradan rendimiento [340]:

$$\mathcal{L}^{\text{CLIP}}(\theta) = \mathbb{E}\left[\min\left(r_t(\theta)A_t, \text{clip}(r_t(\theta), 1-\epsilon, 1+\epsilon)A_t\right)\right] \tag{126}$$

donde:
$$r_t(\theta) = \frac{\pi(a_t|s_t;\theta)}{\pi(a_t|s_t;\theta_{\text{old}})} \tag{127}$$

es el ratio de probabilidades, y $\epsilon$ (típicamente 0.2) controla la magnitud del clipping [341].

**Ventajas**:
- Más estable que vanilla policy gradient
- Más simple que TRPO (Trust Region Policy Optimization)
- Efectivo en espacios de acción continuos y discretos [342]

### E. Multi-Agent Reinforcement Learning (MARL)

En redes multi-celda o multi-usuario, múltiples agentes (BSs, usuarios) deben coordinar asignación de recursos [343].

**Paradigmas MARL**:

1. **Centralizado**: Un agente global controla todos los recursos
   - Pros: Óptimo global
   - Contras: Escalabilidad limitada, overhead de comunicación [344]

2. **Descentralizado**: Cada agente decide independientemente
   - Pros: Escalable, robusto
   - Contras: Convergencia no garantizada, Nash equilibria subóptimos [345]

3. **CTDE (Centralized Training, Decentralized Execution)**: Entrenar con información global, ejecutar con información local
   - Balance óptimo para muchas aplicaciones [346]

**MADDPG (Multi-Agent DDPG)**: Extensión de DDPG para multi-agente con CTDE [347]:

Cada agente $i$ tiene:
- **Actor**: $\pi_i(a_i|s_i;\theta_i)$ usa solo observación local $s_i$
- **Critic**: $Q_i(\mathbf{s}, \mathbf{a};\phi_i)$ usa estados y acciones de todos los agentes

Gradiente de política:

$$\nabla_{\theta_i}J(\theta_i) = \mathbb{E}\left[\nabla_{\theta_i}\pi_i(s_i)\nabla_{a_i}Q_i(\mathbf{s},\mathbf{a})|_{a_i=\pi_i(s_i)}\right] \tag{128}$$

**QMIX**: Para escenarios cooperativos, factoriza Q-función global mediante monotonicity constraint [348]:

$$Q_{\text{tot}}(\mathbf{s},\mathbf{a}) = f(Q_1(s_1,a_1), \ldots, Q_n(s_n,a_n)) \tag{129}$$

donde $f$ es una red de mezcla que satisface:

$$\frac{\partial Q_{\text{tot}}}{\partial Q_i} \geq 0, \quad \forall i \tag{130}$$

Esto permite entrenamiento centralizado con ejecución descentralizada greedy [349].

### F. Aplicaciones Específicas

**1) Power Control**: Ajustar potencia de transmisión para maximizar SINR minimizando interferencia [350]:

- **Estado**: SINR de usuarios, interferencia medida
- **Acción**: Niveles de potencia $\mathbf{p} = [p_1, \ldots, p_K]$
- **Recompensa**: $R = \sum_k \log(1+\text{SINR}_k) - \lambda\sum_k p_k$

Algoritmos como DDPG o TD3 (Twin Delayed DDPG) son efectivos para este problema de acción continua [351].

**2) Spectrum Sharing**: Asignar bandas de frecuencia a usuarios/celdas [352]:

- **Estado**: Demanda de tráfico, ocupación espectral
- **Acción**: Asignación de canales (discreta)
- **Recompensa**: Throughput total - penalización por colisiones

DQN o PPO (con espacio de acción discreto) son apropiados [353].

**3) Dynamic TDD**: Optimizar dirección de slots temporales (uplink/downlink) dinámicamente [354]:

- **Estado**: Demanda de tráfico UL/DL, interferencia inter-celda
- **Acción**: Configuración TDD por celda
- **Recompensa**: Throughput bidireccional - interferencia cruzada

MARL con coordinación entre celdas vecinas [355].

**4) Slice Resource Allocation**: En network slicing, asignar recursos a slices con SLAs diversos [356]:

- **Estado**: Demanda por slice, recursos disponibles, SLA violations
- **Acción**: Porcentaje de recursos por slice
- **Recompensa**: Satisfacción de SLA - costo de recursos

Hierarchical RL donde alto nivel asigna a slices, bajo nivel a usuarios dentro de slice [357].

**5) Energy-Efficient Resource Allocation**: Maximizar eficiencia energética [358]:

- **Recompensa**: $R = \frac{\text{Throughput}}{\text{Power Consumption}}$

Multi-objective RL con trade-off aprendido entre tasa y energía [359].

### G. Transfer Learning y Meta-RL para Adaptación

**Desafío**: Entrenar agentes RL desde cero para cada escenario es costoso. Transfer learning permite reutilizar conocimiento [360].

**Domain Adaptation**: Entrenar en simulación, adaptar a mundo real mediante fine-tuning [361]:

1. **Pre-training**: Entrenar política $\pi_{\theta}$ en simulador
2. **Fine-tuning**: Ajustar $\theta$ con datos reales limitados

**Sim-to-Real Gap**: Diferencias entre simulación y realidad. Soluciones:
- **Domain Randomization**: Entrenar sobre distribución amplia de simulaciones
- **Adversarial Training**: Entrenar discriminador que distingue sim/real, robustificar política [362]

**Meta-RL**: Aprender políticas que se adaptan rápidamente a nuevas tareas [363]:

**RL²**: RNN que actúa como algoritmo de RL completo, aprendiendo a explorar y explotar [364]:

$$a_t = \text{RNN}(s_t, a_{t-1}, r_{t-1}, h_{t-1}) \tag{131}$$

La RNN aprende dinámicas de aprendizaje en su estado oculto.

**MAML para RL**: Buscar parámetros iniciales de política que permitan adaptación rápida [365]:

$$\theta^* = \arg\min_{\theta}\sum_{\mathcal{T}_i}J_{\mathcal{T}_i}(\theta - \alpha\nabla_{\theta}J_{\mathcal{T}_i}(\theta)) \tag{132}$$

## VI. MODULACIÓN ADAPTATIVA Y FORMAS DE ONDA INTELIGENTES

La selección de esquemas de modulación y forma de onda óptimos basándose en condiciones instantáneas del canal es crítica para maximizar eficiencia espectral y confiabilidad [372]. El DL permite adaptación más granular y predicción proactiva superando esquemas tradicionales [373].

### A. Link Adaptation Clásica

**Adaptive Modulation and Coding (AMC)**: Ajustar MCS basándose en CSI o feedback [374]:

$$\text{MCS} = f(\text{SINR}) \tag{133}$$

Mapeo típico mediante umbrales:

| SINR (dB) | MCS | Rate (bps/Hz) | BER Target |
|-----------|-----|---------------|------------|
| < 0 | BPSK 1/2 | 0.5 | $10^{-3}$ |
| 0-5 | QPSK 1/2 | 1.0 | $10^{-3}$ |
| 5-10 | QPSK 3/4 | 1.5 | $10^{-3}$ |
| 10-15 | 16-QAM 1/2 | 2.0 | $10^{-3}$ |
| 15-20 | 16-QAM 3/4 | 3.0 | $10^{-3}$ |
| > 20 | 64-QAM 3/4 | 4.5 | $10^{-3}$ |

**Limitaciones**:
- Umbrales fijos no adaptan a características de canal específicas
- Predicción limitada en canales rápidamente variables
- No considera correlación temporal o patrones de tráfico [375]

### B. DL para Selección de MCS

**Clasificación Neural**: Entrenar clasificador que mapea estado de canal a MCS óptimo [376]:

$$\text{MCS}^* = f_{\text{DNN}}(\mathbf{h}, \text{SNR}, \text{features}; \theta) \tag{134}$$

**Features adicionales**:
- Doppler spread (indicador de movilidad)
- Delay spread (dispersión multi-trayectoria)
- Historial de ACK/NACK
- Demanda de tráfico

**Arquitectura**:
1. **Input Layer**: Features concatenados
2. **Hidden Layers**: DNNs con ReLU/Dropout
3. **Output Layer**: Softmax sobre MCS disponibles

**Función de Pérdida**: Cross-entropy ponderada por throughput [377]:

$$\mathcal{L}(\theta) = -\mathbb{E}\left[\sum_{\text{MCS}} w_{\text{MCS}} \cdot y_{\text{MCS}}\log p_{\text{MCS}}\right] \tag{135}$$

donde $w_{\text{MCS}} = R_{\text{MCS}}$ pondera por tasa del MCS, incentivando esquemas de mayor tasa cuando es seguro.

**Resultados**: Ganancias de 10-20% en throughput comparado con AMC tradicional en canales variables [378].

### C. Predicción Proactiva de MCS

**Desafío**: Latencia de feedback causa mismatch entre CSI y condiciones actuales, especialmente en alta movilidad [379].

**LSTM para Predicción**: Predecir MCS óptimo pasos adelante [380]:

$$\text{MCS}_{t+\Delta t}^* = f_{\text{LSTM}}(\text{MCS}_t, \text{SINR}_t, \ldots, \text{MCS}_{t-L}, \text{SINR}_{t-L}; \theta) \tag{136}$$

**Seq2Seq para Scheduling**: Predecir secuencia de MCS para ventana futura, permitiendo scheduling proactivo [381]:

$$[\text{MCS}_{t+1}, \ldots, \text{MCS}_{t+H}] = f_{\text{Seq2Seq}}(\text{history}; \theta) \tag{137}$$

**Impacto**: Reduce latencia efectiva de feedback, permite pre-codificación optimizada, mejora throughput en 15-25% @ 120 km/h [382].

### D. Learned Modulation: Constelaciones Neurales

**Más allá de QAM**: Las constelaciones convencionales (M-PSK, M-QAM) se diseñaron para canales AWGN. DL permite aprender constelaciones optimizadas para canales específicos [383].

**Autocodificador de Constelación**: Aprender mapeo de bits a símbolos y viceversa [384]:

$$\text{Mapper: } \mathbf{s} = f_{\text{map}}(\mathbf{b}; \theta_{\text{map}}) \in \mathbb{C} \tag{138}$$
$$\text{Channel: } \mathbf{y} = \mathcal{C}(\mathbf{s}) \tag{139}$$
$$\text{Demapper: } \hat{\mathbf{b}} = f_{\text{demap}}(\mathbf{y}; \theta_{\text{demap}}) \tag{140}$$

**Restricciones**:
1. **Potencia promedio**: $\mathbb{E}[|\mathbf{s}|^2] = 1$
2. **Distinción**: Símbolos diferentes deben ser distinguibles

**Entrenamiento End-to-End**:

$$\min_{\theta_{\text{map}}, \theta_{\text{demap}}} \mathbb{E}\left[-\sum_i b_i\log\hat{b}_i - (1-b_i)\log(1-\hat{b}_i)\right] \tag{141}$$

**Resultados**: Para canales con fading severo, constelaciones aprendidas logran 1-2 dB de ganancia sobre QAM [385].

**Interpretación**: Las constelaciones aprendidas a menudo exhiben:
- Distribución no uniforme adaptada a estadísticas de canal
- Robustez aumentada en regiones de alta probabilidad de error
- Estructura geométrica que explota diversidad [386]

### E. Formas de Onda Inteligentes

**Más allá de OFDM**: OFDM es dominante por su simplicidad y robustez a dispersión multi-trayectoria, pero tiene limitaciones (PAPR alto, sensibilidad a CFO, overhead de CP) [387].

**DL para Diseño de Forma de Onda**: Aprender señalización temporal completa [388]:

$$\mathbf{s}(t) = f_{\text{TX}}(\mathbf{b}; \theta_{\text{TX}}) \tag{142}$$
$$\hat{\mathbf{b}} = f_{\text{RX}}(\mathbf{y}(t); \theta_{\text{RX}}) \tag{143}$$

**Autocodificador Temporal**: Genera formas de onda en dominio temporal directamente:

1. **Encoder**: $\mathbf{b} \to \mathbf{s}[n] \in \mathbb{R}^{T_{\text{sym}}}$
2. **Channel**: Convolución con respuesta impulsiva, ruido
3. **Decoder**: $\mathbf{y}[n] \to \hat{\mathbf{b}}$

**Ventajas sobre OFDM**:
- PAPR reducido (no tiene picos constructivos de subportadoras)
- No requiere CP (aprende robustez a ISI implícitamente)
- Adaptado a canal específico [389]

**Desafíos**:
- Sincronización (aprender preambles y sincronización conjuntamente)
- Generalización a longitudes de bloque variables
- Complejidad de implementación [390]

### F. Peak-to-Average Power Ratio (PAPR) Reduction

**Problema de PAPR**: OFDM tiene PAPR alto que causa distorsión en amplificadores de potencia no lineales [391]:

$$\text{PAPR} = \frac{\max_n |s[n]|^2}{\mathbb{E}[|s[n]|^2]} \tag{144}$$

**Técnicas Clásicas**:
- Clipping & Filtering: Degradación de BER
- Selective Mapping (SLM): Overhead de side information
- Partial Transmit Sequence (PTS): Alta complejidad [392]

**DNN para PAPR Reduction**: Aprender precodificador que reduce PAPR manteniendo BER [393]:

$$\mathbf{x}' = f_{\text{DNN}}(\mathbf{x}; \theta) \tag{145}$$

Función objetivo multi-objetivo:

$$\mathcal{L}(\theta) = \alpha \cdot \text{BER}(\mathbf{x}') + \beta \cdot \text{PAPR}(\mathbf{x}') \tag{146}$$

**Resultados**: Reducción de PAPR de 2-3 dB con degradación de BER <0.5 dB [394].

**Autocodificador con Nonlinearity Awareness**: Entrenar con modelo de amplificador de potencia no lineal en el loop [395]:

$$\mathbf{s}' = \text{PA}(\mathbf{s}) = \alpha \mathbf{s} + \alpha_3 |\mathbf{s}|^2\mathbf{s} + \ldots \tag{147}$$

El encoder aprende pre-distorsión implícita.

### G. Waveform para Coexistencia Espectral

**Escenario**: Múltiples servicios (eMBB, URLLC, mMTC) coexisten, requiriendo formas de onda con diferentes características [396].

**Multi-Numerology**: Usar diferentes espaciamientos de subportadora [397]:
- eMBB: 15 kHz (alta eficiencia espectral)
- URLLC: 60 kHz (baja latencia)
- mMTC: 3.75 kHz (cobertura extendida)

**Desafío**: Interferencia inter-numerología

**DL para Cancelación de Interferencia**: Entrenar receptores que suprimen interferencia de numerologías vecinas [398]:

$$\hat{\mathbf{b}}_{\text{eMBB}} = f_{\text{RX}}(\mathbf{y}, \text{info}_{\text{URLLC}}; \theta) \tag{148}$$

donde información sobre señalización URLLC ayuda a cancelar su interferencia.

**Filtered OFDM con Filtros Aprendidos**: Diseñar filtros por subportadora mediante DNNs que minimizan fuga espectral [399]:

$$\mathbf{f} = f_{\text{DNN}}(\text{numerology}, \text{BW}; \theta) \tag{149}$$

Filtros aprendidos logran 10-15 dB mejor ACLR (Adjacent Channel Leakage Ratio) que ventanas clásicas [400].

## VII. COMUNICACIONES SEMÁNTICAS Y ORIENTADAS A TAREAS

Un cambio paradigmático emergente es la comunicación semántica, donde el objetivo es transmitir significado (semántica) en lugar de bits exactos, potencialmente logrando eficiencias exponenciales [403], [404]. El DL es habilitador clave al extraer y codificar representaciones semánticas.

### A. Fundamentos de Comunicación Semántica

**Arquitectura de Shannon**: Comunicación tradicional separa fuente-canal:

$$\text{Source} \to \text{Source Coding} \to \text{Channel Coding} \to \text{Channel} \to \text{Decoding} \tag{150}$$

Objetivo: Reconstruir bits exactos con probabilidad de error arbitrariamente pequeña [405].

**Limitación**: Para aplicaciones como visión por máquina, traducción, o control, reconstrucción exacta de bits puede ser innecesaria si se preserva tarea objetivo [406].

**Arquitectura de Weaver**: Extender con niveles de semántica y efectividad [407]:

- **Nivel A (Técnico)**: ¿Qué tan precisos son los símbolos transmitidos? (Shannon)
- **Nivel B (Semántico)**: ¿Qué tan precisamente transmiten el significado deseado?
- **Nivel C (Efectividad)**: ¿Qué tan efectivamente afecta la conducta deseada?

**Comunicación Semántica**: Optimizar niveles B y C directamente [408].

### B. Deep Learning para Extracción Semántica

**Representaciones Latentes**: Usar encoders profundos para extraer características semánticas compactas [409]:

$$\mathbf{z} = f_{\text{semantic}}(\mathbf{x}; \theta_{\text{sem}}) \tag{151}$$

donde $\mathbf{x}$ es dato fuente (imagen, texto, señal) y $\mathbf{z} \in \mathbb{R}^d$ con $d \ll \dim(\mathbf{x})$ es representación semántica.

**Autoencoders Variational (VAE)**: Aprender distribución sobre representaciones [410]:

$$q_{\phi}(\mathbf{z}|\mathbf{x}) = \mathcal{N}(\mathbf{z}; \boldsymbol{\mu}(\mathbf{x}), \boldsymbol{\sigma}^2(\mathbf{x})\mathbf{I}) \tag{152}$$
$$p_{\theta}(\mathbf{x}|\mathbf{z}) \tag{153}$$

Objetivo ELBO:

$$\mathcal{L} = \mathbb{E}_{q_{\phi}(\mathbf{z}|\mathbf{x})}[\log p_{\theta}(\mathbf{x}|\mathbf{z})] - D_{KL}(q_{\phi}(\mathbf{z}|\mathbf{x})\|p(\mathbf{z})) \tag{154}$$

Representaciones $\mathbf{z}$ capturan factores semánticos de variación [411].

**Contrastive Learning**: Aprender representaciones que agrupan semántica similar [412]:

$$\mathcal{L}_{\text{contrastive}} = -\log\frac{\exp(\text{sim}(\mathbf{z}_i, \mathbf{z}_j)/\tau)}{\sum_{k}\exp(\text{sim}(\mathbf{z}_i, \mathbf{z}_k)/\tau)} \tag{155}$$

donde $(i,j)$ son pares positivos (semánticamente similares) y $k$ incluye negativos.

### C. Comunicación Semántica End-to-End

**Arquitectura**: Transmitir representaciones semánticas en lugar de datos brutos [413]:

1. **Semantic Encoder**: $\mathbf{z} = f_{\text{sem}}(\mathbf{x}; \theta_{\text{sem}})$
2. **Channel Encoder**: $\mathbf{s} = f_{\text{ch}}(\mathbf{z}; \theta_{\text{ch}})$
3. **Channel**: $\mathbf{y} = \mathcal{C}(\mathbf{s})$
4. **Channel Decoder**: $\hat{\mathbf{z}} = f_{\text{ch-dec}}(\mathbf{y}; \theta_{\text{ch-dec}})$
5. **Semantic Decoder**: $\hat{\mathbf{x}} = f_{\text{sem-dec}}(\hat{\mathbf{z}}; \theta_{\text{sem-dec}})$

**Función de Pérdida**: Métrica orientada a tarea en lugar de MSE [414]:

$$\mathcal{L} = \mathcal{L}_{\text{task}}(\mathbf{x}, \hat{\mathbf{x}}) + \lambda R(\mathbf{s}) \tag{156}$$

Ejemplos:
- **Clasificación de imagen**: Cross-entropy en etiquetas
- **Segmentación**: IoU (Intersection over Union)
- **Traducción**: BLEU score
- $R(\mathbf{s})$ es término de rate (potencia, bandwidth)

**Ventaja**: Optimización end-to-end para tarea final, ignorando detalles irrelevantes [415].

### D. Aplicaciones Específicas

**1) Transmisión de Imagen para Clasificación**: Objetivo es clasificar imagen correctamente en receptor, no reconstruir pixels exactos [416].

**Arquitectura**:
- **Encoder**: CNN que extrae features relevantes para clasificación
- **Channel Coding**: Proteger features según importancia
- **Decoder + Classifier**: Clasificar desde features recibidos

**Baseline**: Compresión JPEG + transmisión + clasificación

**Semantic**: Entrenamiento end-to-end de encoder-channel-classifier

**Resultados**: Con 1/10 del bandwidth, comunicación semántica logra precisión de clasificación igual a transmisión completa [417].

**2) Transmisión de Vídeo para Detección de Objetos**: Para aplicaciones como conducción autónoma, detección de objetos es crítica, no calidad visual [418].

**Enfoque Semántico**:
- Transmitir mapas de características desde detector (e.g., YOLO, Faster R-CNN)
- Reconstruir bounding boxes y clases en receptor

**Compresión**: $100\times$ comparado con H.265 manteniendo precisión de detección [419].

**3) Comunicación de Texto para Traducción**: Para traducción máquina, preservar significado es crucial, no palabras exactas [420].

**Arquitectura**:
- **Encoder**: Transformer que mapea texto fuente a representación semántica
- **Channel**: Transmitir embedding compacto
- **Decoder**: Transformer que genera traducción desde embedding

**Ventaja**: Robustez a errores de canal - pequeñas corrupciones en embedding no destruyen completamente significado [421].

### E. Knowledge Base Compartida

**Background Knowledge**: Transmisor y receptor comparten base de conocimiento (modelos pre-entrenados, contexto) que reduce información a transmitir [422].

**Ejemplo - Imágenes**: Ambos lados tienen modelo generativo pre-entrenado (GAN, Diffusion Model) [423]:

1. **TX**: Encuentra latent code $\mathbf{z}$ que genera imagen similar
$$\mathbf{z}^* = \arg\min_{\mathbf{z}} \|\mathbf{x} - G(\mathbf{z})\|^2 \tag{157}$$

2. **Transmit**: Solo $\mathbf{z}$ (baja dimensión)

3. **RX**: Genera imagen $\hat{\mathbf{x}} = G(\mathbf{z})$

**Refinamiento**: Transmitir residuales para detalles críticos [424].

**Ejemplo - Vídeo**: Ambos lados tienen modelo de predicción de frames:

1. **TX/RX**: Predicen frame futuro $\hat{\mathbf{x}}_t$ desde histórico
2. **TX**: Transmitir solo residual $\Delta\mathbf{x}_t = \mathbf{x}_t - \hat{\mathbf{x}}_t$ si error grande
3. **RX**: Reconstruir $\mathbf{x}_t = \hat{\mathbf{x}}_t + \Delta\mathbf{x}_t$

Compresión masiva cuando predicción es precisa [425].

### F. Goal-Oriented Communication

**Más allá de reconstrucción**: Optimizar directamente para objetivo de downstream task [426].

**Ejemplo - Control Remoto**: Robot controlado remotamente basándose en sensores [427]:

**Tradicional**:
1. Transmitir todos datos sensoriales
2. Controlador computa acciones

**Goal-Oriented**:
1. Sensor-side: Extraer solo información relevante para acción actual
2. Transmitir representación compacta
3. Controller: Ejecutar acción

**Formulación RL**: Agente aprende política de comunicación que maximiza recompensa de tarea [428]:

$$\pi_{\text{comm}}(\mathbf{z}|\mathbf{x}, \text{task}) = \text{qué información transmitir} \tag{158}$$
$$\pi_{\text{action}}(a|\hat{\mathbf{z}}) = \text{acción basada en información recibida} \tag{159}$$

Entrenamiento end-to-end maximiza recompensa de tarea sujeto a restricciones de comunicación [429].

### G. Desafíos y Limitaciones

**Compatibilidad**: Sistemas semánticos requieren que TX y RX tengan modelos compatibles (versiones, entrenamiento) [430].

**Solución**: Estandarización de arquitecturas base, fine-tuning distribuido, federated learning

**Generalización**: Modelos entrenados en datasets específicos pueden no generalizar a datos out-of-distribution [431].

**Solución**: Meta-learning, domain adaptation, continual learning

**Seguridad y Privacidad**: Representaciones semánticas pueden revelar información sensible [432].

**Solución**: Privacy-preserving encoders mediante adversarial training, differential privacy

**Latencia**: Encoders/decoders profundos añaden latencia [433].

**Solución**: Model compression, early exit networks, hardware acceleration

### H. Resultados Experimentales

**Transmisión de Imagen para Clasificación**:

Dataset: ImageNet, tarea: clasificación 1000 clases

| Método | Bandwidth (kb/imagen) | Top-1 Accuracy |
|--------|-----------------------|----------------|
| JPEG + TX | 50 | 76.2% |
| BPG + TX | 30 | 75.8% |
| Semantic (baseline) | 10 | 72.5% |
| Semantic (advanced) | 10 | 75.1% |
| Semantic (w/ knowledge) | 5 | 74.3% |

Comunicación semántica logra accuracies comparables con $5\times-10\times$ reducción de bandwidth [434].

**Control Remoto de Drone**:

Tarea: Navegación autónoma con feedback de cámara sobre canal con rate limitado

| Método | Rate (kbps) | Success Rate | Collision Rate |
|--------|-------------|--------------|----------------|
| Full Video (H.265) | 500 | 95% | 2% |
| Compressed Video | 100 | 87% | 7% |
| Semantic (features) | 50 | 92% | 3% |
| Goal-Oriented (RL) | 20 | 91% | 4% |

Goal-oriented logra performance casi óptimo con $25\times$ menos bandwidth [435].

---

## VIII. DESAFÍOS DE IMPLEMENTACIÓN Y CONSIDERACIONES PRÁCTICAS

Si bien el DL promete mejoras sustanciales en la capa física, el deployment práctico enfrenta desafíos significativos en complejidad computacional, generalización, robustez, y estandarización [436].

### A. Complejidad Computacional y Latencia

**Desafío**: Los modelos de DL profundos requieren millones de operaciones por inferencia, potencialmente excediendo presupuestos de latencia/energía [437].

**Análisis de Complejidad**: Para DNN con $L$ capas fully-connected de tamaño $N_h$:

$$\text{FLOPs} = \sum_{l=1}^{L} N_h^{(l)} \times N_h^{(l-1)} \tag{160}$$

Para CNN con $C$ canales, kernels $K \times K$, y resolución espacial $H \times W$:

$$\text{FLOPs} = L \times C_{\text{in}} \times C_{\text{out}} \times K^2 \times H \times W \tag{161}$$

**Ejemplo**: Para detector MIMO con DNN de 5 capas, 512 neuronas, inferencia requiere:

$$\text{FLOPs} \approx 5 \times 512^2 \approx 1.3 \times 10^6 \tag{162}$$

En CPU general (10 GFLOPS), esto toma $\approx 130$ μs. Para sistemas con TTI (Transmission Time Interval) de 1 ms, esto es manejable, pero para URLLC con latencia <1 ms, se requiere aceleración [438].

**Soluciones**:

**1) Cuantización**: Reducir precisión de pesos y activaciones de FP32 a INT8 o INT4 [439]:

$$\text{Quantized: } w_q = \text{round}\left(\frac{w}{s}\right) \cdot s \tag{163}$$

donde $s$ es factor de escala. Cuantización INT8 reduce memoria $4\times$ y acelera inferencia $2\times-4\times$ con degradación típica <1 dB [440].

**Quantization-Aware Training**: Simular cuantización durante entrenamiento:

$$\tilde{w} = w + \text{stop\_gradient}(\text{quantize}(w) - w) \tag{164}$$

Permite aprender pesos robustos a cuantización [441].

**2) Poda (Pruning)**: Eliminar conexiones con pesos pequeños [442]:

$$\text{Mask}_{i,j} = \begin{cases}
1 & |w_{i,j}| > \tau\\
0 & |w_{i,j}| \leq \tau
\end{cases}$$

Poda estructurada (eliminar neuronas/canales completos) facilita aceleración en hardware [443].

**Iterative Pruning**: Alternar entre entrenamiento y poda:

1. Entrenar red completa
2. Podar $p\%$ de pesos más pequeños
3. Re-entrenar
4. Repetir hasta tasa objetivo

Permite reducir parámetros en $10\times$ con degradación mínima [444].

**3) Destilación de Conocimiento**: Entrenar modelo pequeño (student) para imitar modelo grande (teacher) [445]:

$$\mathcal{L}_{\text{distill}} = \alpha \mathcal{L}_{\text{task}} + (1-\alpha)\mathcal{L}_{\text{KD}} \tag{165}$$

donde:

$$\mathcal{L}_{\text{KD}} = \text{KL}\left(p_{\text{teacher}}(y|x) \| p_{\text{student}}(y|x)\right) \tag{166}$$

Student aprende no solo etiquetas correctas sino distribución de salida del teacher, transfiriendo conocimiento implícito [446].

**4) Neural Architecture Search (NAS)**: Buscar automáticamente arquitecturas eficientes [447]:

- **Search Space**: Definir espacio de arquitecturas candidatas
- **Search Strategy**: Algoritmo para explorar espacio (RL, evolutionary, gradient-based)
- **Performance Estimation**: Evaluar candidatos (entrenamiento completo, early stopping, weight sharing)

NAS puede encontrar arquitecturas con $5\times-10\times$ menor latencia manteniendo rendimiento [448].

**5) Early Exit Networks**: Permitir salida temprana en capas intermedias para muestras fáciles [449]:

$$\text{Output}_l = \begin{cases}
f_{\text{exit}}^{(l)}(\mathbf{h}^{(l)}) & \text{if } \text{confidence} > \tau_l\\
\text{continue} & \text{otherwise}
\end{cases}$$

Reduce latencia promedio mientras mantiene precisión para casos difíciles [450].

### B. Aceleración por Hardware

**GPUs**: Paralelización masiva acelera inferencia $10\times-100\times$ sobre CPUs:

- Throughput: 1000+ detecciones MIMO/segundo
- Latencia: 1-5 ms por inferencia
- Limitación: Consumo de potencia alto (100-300W) [451]

**TPUs (Tensor Processing Units)**: ASICs especializados para operaciones matriciales:

- Arquitectura systolic array optimizada para multiplicación matriz-matriz
- Eficiencia energética: $\approx 30\times$ mejor que GPUs
- Throughput: >100 TOPS (Tera Operations Per Second) [452]

**FPGAs**: Lógica reconfigurable permite implementaciones customizadas:

- Latencia ultra-baja (<100 μs)
- Consumo de potencia moderado (10-50W)
- Flexibilidad: Actualizable para nuevos modelos
- Aplicaciones: Detección MIMO, decodificación neural en tiempo real [453], [454]

**ASICs Especializados**: Chips diseñados específicamente para inferencia de DNNs:

- Máxima eficiencia energética (>1000 GOPS/W)
- Latencia mínima
- Costo de desarrollo alto, inflexibilidad
- Ejemplos: Google Edge TPU, Apple Neural Engine [455]

**Implementaciones Reportadas**:

| Plataforma | Aplicación | Throughput | Latencia | Potencia | Eficiencia |
|------------|------------|------------|----------|----------|------------|
| CPU (Intel i7) | MIMO Detection 4×4 | 100 det/s | 10 ms | 95W | 1.05 det/s/W |
| GPU (NVIDIA V100) | MIMO Detection 4×4 | 5000 det/s | 2 ms | 300W | 16.7 det/s/W |
| FPGA (Xilinx Ultrascale) | MIMO Detection 4×4 | 2000 det/s | 0.5 ms | 25W | 80 det/s/W |
| ASIC (Custom) | MIMO Detection 4×4 | 10000 det/s | 0.1 ms | 15W | 667 det/s/W |

FPGAs y ASICs ofrecen mejor trade-off latencia-energía para deployment [456].

### C. Generalización y Robustez

**Desafío**: Modelos entrenados en distribuciones específicas pueden fallar en condiciones no vistas [457].

**Domain Shift**: Diferencias entre datos de entrenamiento y deployment:

- Modelos de canal (simulación vs. realidad)
- SNR range
- Configuraciones de hardware
- Escenarios de propagación (indoor, outdoor, vehicular) [458]

**Dataset Bias**: Datasets de entrenamiento pueden no capturar toda la diversidad de escenarios reales [459].

**Soluciones**:

**1) Data Augmentation**: Generar datos sintéticos con variabilidad [460]:

- **Channel Randomization**: Entrenar sobre amplia distribución de canales
- **SNR Augmentation**: Variar SNR durante entrenamiento
- **Hardware Impairment Simulation**: Incluir phase noise, IQ imbalance, etc.

**2) Domain Adaptation**: Adaptar modelo pre-entrenado a dominio objetivo con datos limitados [461]:

**Fine-Tuning**: Re-entrenar capas superiores en datos objetivo

**Adversarial Domain Adaptation**: Entrenar feature extractor que engaña discriminador de dominio [462]:

$$\min_{F}\max_{D} \mathbb{E}_{x \sim \mathcal{D}_s}[\log D(F(x))] + \mathbb{E}_{x \sim \mathcal{D}_t}[\log(1-D(F(x)))] \tag{167}$$

Features $F(x)$ se vuelven invariantes a dominio.

**3) Meta-Learning**: Aprender a aprender, facilitando adaptación rápida [463]:

MAML para comunicaciones permite adaptar a nuevas condiciones de canal con pocos ejemplos:

$$\theta^* = \arg\min_{\theta} \sum_{\mathcal{T}_i}\mathcal{L}_{\mathcal{T}_i}(\theta - \alpha\nabla_{\theta}\mathcal{L}_{\mathcal{T}_i}(\theta)) \tag{168}$$

**4) Ensemble Methods**: Combinar múltiples modelos para robustez [464]:

$$\hat{y} = \frac{1}{M}\sum_{m=1}^{M}f_m(x;\theta_m) \tag{169}$$

Ensembles son más robustos a corrupciones y domain shift [465].

**5) Uncertainty Quantification**: Estimar confianza de predicciones [466]:

**MC Dropout**: Usar dropout en inferencia, múltiples forwards:

$$p(y|x) \approx \frac{1}{T}\sum_{t=1}^{T}p(y|x,\theta_t) \tag{170}$$

donde $\theta_t$ son pesos con dropout estocástico. Varianza de predicciones indica incertidumbre [467].

**Bayesian Neural Networks**: Mantener distribuciones sobre pesos:

$$p(\theta|\mathcal{D}) \propto p(\mathcal{D}|\theta)p(\theta) \tag{171}$$

Permite cuantificar uncertainty epistémica [468].

### D. Adversarial Robustness

**Vulnerabilidad**: DNNs son susceptibles a perturbaciones adversariales imperceptibles [469]:

$$\mathbf{x}_{\text{adv}} = \mathbf{x} + \epsilon \cdot \text{sign}(\nabla_{\mathbf{x}}\mathcal{L}(f(\mathbf{x}),y)) \tag{172}$$

En comunicaciones, un atacante podría inyectar perturbaciones que causen detección/decodificación errónea [470].

**Ataques Específicos**:

**1) Adversarial Jamming**: Jamming optimizado para maximizar error de DNN detector [471]:

$$\mathbf{j}^* = \arg\max_{\|\mathbf{j}\|_2 \leq P_j} \mathcal{L}_{\text{det}}(f_{\text{DNN}}(\mathbf{y} + \mathbf{j})) \tag{173}$$

Mucho más efectivo que ruido gaussiano de misma potencia.

**2) Model Evasion**: Atacante con conocimiento de modelo genera señales que evaden detección [472].

**3) Backdoor Attacks**: Envenenar datos de entrenamiento para insertar comportamientos maliciosos [473]:

- Entrenar con muestras que contienen trigger pattern
- Modelo funciona normalmente, excepto cuando trigger está presente

**Defensas**:

**1) Adversarial Training**: Entrenar contra ejemplos adversariales [474]:

$$\min_{\theta} \mathbb{E}_{(\mathbf{x},y)}\left[\max_{\|\delta\| \leq \epsilon}\mathcal{L}(f(\mathbf{x}+\delta;\theta),y)\right] \tag{174}$$

Robustifica modelo pero puede reducir precisión en datos limpios.

**2) Certified Defense**: Garantizar robustez en región acotada [475]:

Randomized Smoothing: Usar modelo suavizado por ruido:

$$g(\mathbf{x}) = \mathbb{E}_{\boldsymbol{\epsilon}\sim\mathcal{N}(0,\sigma^2\mathbf{I})}[f(\mathbf{x}+\boldsymbol{\epsilon})] \tag{175}$$

Provee certificado de robustez en bola de radio $R$ [476].

**3) Detection**: Detectar inputs adversariales antes de procesamiento [477]:

- Anomaly detection basado en estadísticas de activaciones
- Red discriminadora entrenada para distinguir ejemplos limpios/adversariales

**4) Obfuscation**: Ocultar arquitectura/pesos de modelo del atacante [478]:

- Model compression/distillation
- Ensemble con randomización

### E. Estandarización e Interoperabilidad

**Desafío**: Deployment de DL en redes celulares requiere estandarización para interoperabilidad entre vendors [479].

**Aspectos a Estandarizar**:

**1) Arquitecturas de Modelos**:
- Número de capas, tipos, dimensiones
- Funciones de activación
- Restricciones (normalización, cuantización) [480]

**2) Formatos de Pesos**:
- Representación numérica (FP32, FP16, INT8)
- Estructura de almacenamiento
- Mecanismos de actualización [481]

**3) Interfaces**:
- Formato de entrada/salida
- APIs de inferencia
- Señalización de capacidades [482]

**4) Procedimientos de Actualización**:
- Over-the-air model updates
- Versionado
- Fallback a métodos tradicionales [483]

**Iniciativas de Estandarización**:

**3GPP**: 3rd Generation Partnership Project está explorando IA/ML para 6G [484]:

- Study Items en Release 18/19
- Foco en beam management, CSI compression, positioning
- Arquitecturas split learning (parte en UE, parte en gNB)

**ONNX (Open Neural Network Exchange)**: Formato estándar para modelos de DL [485]:

- Interoperabilidad entre frameworks (PyTorch, TensorFlow, etc.)
- Optimizaciones de inferencia
- Deployment en edge devices

**O-RAN (Open Radio Access Network)**: Arquitectura abierta con interfaces estándar [486]:

- RIC (RAN Intelligent Controller): Plataforma para xApps/rApps basados en ML
- Estandarización de KPIs, datos de entrenamiento
- Marketplace de aplicaciones de IA [487]

### F. Privacy y Seguridad de Datos

**Desafío**: Entrenar modelos de DL requiere grandes cantidades de datos que pueden contener información sensible [488].

**Riesgos**:

**1) Membership Inference**: Atacante determina si muestra específica estaba en dataset de entrenamiento [489]:

$$\text{Attack: } f_{\text{attack}}(\mathbf{x}, f(\mathbf{x};\theta)) \to \{\text{member}, \text{non-member}\} \tag{176}$$

**2) Model Inversion**: Atacante reconstruye datos de entrenamiento desde modelo [490]:

$$\mathbf{x}^* = \arg\max_{\mathbf{x}} p(y|\mathbf{x};\theta) \tag{177}$$

**3) Data Poisoning**: Atacante contamina dataset de entrenamiento [491].

**Soluciones**:

**1) Differential Privacy**: Garantizar que inclusión/exclusión de muestra individual no afecta significativamente salidas [492]:

**DP-SGD**: Añadir ruido a gradientes durante entrenamiento:

$$\tilde{g}_t = \frac{1}{B}\sum_{i}\text{clip}(\nabla_{\theta}\mathcal{L}(\mathbf{x}_i;\theta), C) + \mathcal{N}(0, \sigma^2 C^2 \mathbf{I}) \tag{178}$$

donde $C$ es threshold de clipping y $\sigma$ controla noise scale [493].

Privacy budget $\epsilon$: Menor $\epsilon$ = mayor privacidad (típicamente $\epsilon \in [1,10]$)

Trade-off: DP reduce precisión de modelo (típicamente 2-5%) [494].

**2) Federated Learning**: Entrenar modelo distribuido sin compartir datos brutos [495]:

1. **Server**: Distribuir modelo inicial $\theta_0$
2. **Clients**: Entrenar localmente en datos privados
$$\theta_i^{(t+1)} = \theta_i^{(t)} - \eta\nabla\mathcal{L}_i(\theta_i^{(t)}) \tag{179}$$
3. **Server**: Agregar actualizaciones
$$\theta^{(t+1)} = \sum_{i}\frac{n_i}{n}\theta_i^{(t+1)} \tag{180}$$
4. Repetir

Aplicaciones en comunicaciones:
- UEs entrenan modelos en datos de canal locales
- BS agrega modelos sin acceder datos privados [496]

**Challenges**:
- Heterogeneidad de datos (non-IID)
- Comunicación costosa
- Dispositivos con recursos limitados [497]

**3) Secure Multi-Party Computation**: Computar sobre datos encriptados [498]:

**Homomorphic Encryption**: Permite operaciones en ciphertext:

$$\text{Enc}(x_1) \oplus \text{Enc}(x_2) = \text{Enc}(x_1 + x_2) \tag{181}$$
$$\text{Enc}(x_1) \otimes \text{Enc}(x_2) = \text{Enc}(x_1 \cdot x_2) \tag{182}$$

Permite inferencia sobre datos encriptados, pero es computacionalmente intensivo (latencia $100\times-1000\times$ mayor) [499].

**4) Trusted Execution Environments**: Hardware que aísla ejecución sensible [500]:

- Intel SGX, ARM TrustZone
- Entrenar/inferir modelos en enclave protegido
- Garantías a nivel de hardware contra acceso no autorizado

### G. Explicabilidad e Interpretabilidad

**Desafío**: Modelos de DL son "cajas negras" difíciles de interpretar, obstaculizando confianza y debugging [501].

**Importancia en Comunicaciones**:
- Regulación puede requerir explicabilidad
- Debugging de fallas requiere entender decisiones
- Ganar confianza de operadores y usuarios [502]

**Técnicas**:

**1) Feature Importance**: Identificar qué features influyen en decisiones [503]:

**SHAP (Shapley Additive Explanations)**: Asigna valor de Shapley a cada feature:

$$\phi_i = \sum_{S \subseteq N \setminus \{i\}}\frac{|S|!(|N|-|S|-1)!}{|N|!}[f(S \cup \{i\}) - f(S)] \tag{183}$$

Indica contribución marginal de feature $i$ [504].

**LIME (Local Interpretable Model-agnostic Explanations)**: Aproximar localmente con modelo lineal interpretable:

$$\xi(x) = \arg\min_{g \in G}\mathcal{L}(f,g,\pi_x) + \Omega(g) \tag{184}$$

donde $g$ es modelo interpretable, $\pi_x$ es proximidad, $\Omega$ es complejidad [505].

**2) Attention Visualization**: Para modelos con attention, visualizar pesos aprendidos [506]:

$$\alpha_{i,j} = \frac{\exp(e_{i,j})}{\sum_k \exp(e_{i,k})} \tag{185}$$

Muestra qué partes de entrada son importantes para salida.

**3) Activation Maximization**: Sintetizar inputs que maximizan activación de neuronas [507]:

$$\mathbf{x}^* = \arg\max_{\mathbf{x}} \mathbf{h}_l[\mathbf{x}] - \lambda\|\mathbf{x}\|^2 \tag{186}$$

Revela qué patrones detecta neurona $l$.

**4) Model Distillation a Modelos Interpretables**: Aproximar DNN con árbol de decisión [508]:

- Entrenar árbol para imitar DNN
- Árbol es directamente interpretable (reglas if-then)
- Trade-off: Menor precisión pero mayor interpretabilidad

### H. Impacto Ambiental y Sostenibilidad

**Desafío**: Entrenamiento de modelos grandes consume energía masiva con huella de carbono significativa [509].

**Costo Energético**:

- Entrenar GPT-3: $\approx 1287$ MWh $\approx 550$ tons CO₂
- Entrenar BERT: $\approx 1507$ lbs CO₂ (equivalente a vuelo transcontinental)
- Entrenamiento continuo de modelos para comunicaciones puede acumular huella substancial [510]

**Soluciones**:

**1) Efficient Training**: Reducir FLOPs de entrenamiento:

- Mixed-precision training (FP16/BF16)
- Gradient checkpointing (trade memory for compute)
- Efficient optimizers (AdamW, LAMB) [511]

**2) Transfer Learning**: Reutilizar modelos pre-entrenados reduce entrenamiento desde cero:

- Pre-train once on large dataset
- Fine-tune for specific scenarios ($\approx 1\%$ del costo) [512]

**3) Neural Architecture Search Eficiente**: Métodos como ENAS, DARTS reducen costo de búsqueda de arquitecturas en $1000\times$ [513].

**4) Model Sharing**: Múltiples aplicaciones comparten modelos base:

- Foundation models for wireless
- Reduce duplicación de esfuerzo de entrenamiento [514]

**5) Green AI**: Métricas que consideran eficiencia energética además de precisión [515]:

$$\text{Efficiency} = \frac{\text{Accuracy}}{\text{Energy} \times \text{CO}_2} \tag{187}$$

Incentivar desarrollo de modelos eficientes.

**6) Edge Computing**: Reducir transmisión de datos a cloud disminuye energía de comunicación [516].

---

## IX. APORTES DEL ARTÍCULO

Este artículo realiza contribuciones significativas al avance del conocimiento en Inteligencia Artificial y Deep Learning para sistemas de comunicaciones inalámbricas 6G y posteriores:

**1) Marco Unificado de Análisis**: Se establece un marco conceptual coherente que integra técnicas de IA a través de todos los componentes de la capa física, demostrando cómo diferentes paradigmas de aprendizaje automático se complementan para abordar desafíos específicos del diseño de sistemas inalámbricos.

**2) Rigurosidad Matemática**: Cada técnica presentada se fundamenta en formulaciones matemáticas precisas, incluyendo problemas de optimización subyacentes, arquitecturas neuronales detalladas, y análisis de complejidad computacional, proporcionando bases sólidas para comprensión profunda e implementación práctica.

**3) Evaluación Comparativa Sistemática**: Se presentan comparaciones cuantitativas exhaustivas entre métodos basados en IA y técnicas tradicionales, identificando regímenes donde cada enfoque exhibe ventajas, permitiendo decisiones informadas de diseño.

**4) Análisis de Viabilidad Práctica**: Se examina críticamente la factibilidad de implementación real, abordando desafíos de complejidad, latencia, consumo energético, generalización, robustez, y estandarización que deben resolverse para deployment a escala.

**5) Identificación de Brechas de Conocimiento**: Se destacan áreas donde la investigación actual es insuficiente y se requieren avances fundamentales, guiando esfuerzos futuros de investigación hacia problemas de mayor impacto potencial.

**6) Visión Estratégica**: Se articula una perspectiva de largo plazo sobre la evolución hacia sistemas 6G nativos de IA, considerando no solo aspectos técnicos sino también implicaciones de estandarización, regulación, y transformación de la industria.


## X. DESAFÍOS ABIERTOS Y DIRECCIONES FUTURAS


**1) Límites Teóricos de IA en Comunicaciones**: Establecer límites fundamentales:

**Pregunta**: ¿Cuál es la capacidad alcanzable por sistemas de comunicación end-to-end aprendidos?

**Conjeturas**:
- Con modelo de canal perfecto, IA puede aproximar capacidad de Shannon arbitrariamente
- Con incertidumbre de canal, ¿puede IA superar esquemas robustos tradicionales?

**Sample Complexity**: ¿Cuántos datos se requieren para aprender comunicación óptima?

$$N_{\text{samples}} = \Theta(?) \tag{188}$$

Bounds teóricos ayudarían a guiar diseño práctico.

**2) Unificación de Model-Based y Data-Driven Approaches**: Combinar conocimiento físico con aprendizaje:

**Physics-Informed Neural Networks**: Incorporar ecuaciones físicas en pérdida:

$$\mathcal{L} = \mathcal{L}_{\text{data}} + \lambda\mathcal{L}_{\text{physics}} \tag{189}$$

donde $\mathcal{L}_{\text{physics}}$ penaliza violaciones de leyes físicas (conservación de energía, reciprocidad de canal, etc.).

**Neural ODEs para Canal Dynamics**: Modelar evolución temporal de canal con ecuaciones diferenciales aprendidas:

$$\frac{d\mathbf{h}(t)}{dt} = f_{\theta}(\mathbf{h}(t), t) \tag{190}$$

Combina modelado físico con flexibilidad de DL.

**3) Multi-Objective Optimization**: Balancear objetivos conflictivos:

**Pareto Optimality**: Encontrar frente de Pareto entre:
- Throughput vs. Latency
- Spectral Efficiency vs. Energy Efficiency
- Performance vs. Complexity

**Multi-Task Learning**: Entrenar un modelo para optimizar múltiples objetivos:

$$\mathcal{L} = \sum_{i=1}^{K}w_i\mathcal{L}_i \tag{191}$$

Aprender pesos $w_i$ dinámicamente basándose en importancia relativa.

**4) Causalidad en Sistemas de Comunicación**: Entender relaciones causales en lugar de solo correlaciones:

**Causal Inference**: Identificar efectos causales de intervenciones:
- ¿Qué pasa si cambio potencia de transmisión?
- ¿Cómo afecta beam selection a throughput?

**Structural Causal Models**: Representar sistema como grafo causal:

$$\mathbf{h} \to \text{SINR} \to \text{MCS} \to \text{Throughput} \tag{192}$$

Permite reasoning sobre intervenciones y counterfactuals.

**5) Federación Global de Modelos**: Colaboración internacional en desarrollo de IA para 6G:

**Global Federated Learning**: Operators de múltiples países colaboran:
- Preserva privacidad de datos locales
- Modelos benefician de diversidad global
- Desafíos: Heterogeneidad extrema, regulaciones, trust

**Model Zoos**: Repositorios públicos de modelos pre-entrenados:
- Acelera investigación y desarrollo
- Benchmarking estandarizado
- Reproducibilidad

---

## XI. CONCLUSIONES


Este artículo ha presentado una revisión exhaustiva y análisis profundo de la aplicación de Inteligencia Artificial y Deep Learning en la capa física de sistemas de comunicaciones inalámbricas 6G y posteriores. Se han explorado en detalle las arquitecturas de redes neuronales profundas, formulaciones matemáticas subyacentes, y desarrollos analíticos para cada componente crítico de la capa física.

**Hallazgos Clave**:

1. **Superación de Métodos Tradicionales**: Las técnicas basadas en DL han demostrado superar consistentemente métodos clásicos en múltiples dimensiones:
   - **Estimación de Canal**: Ganancias de 3-5 dB en NMSE comparado con MMSE en canales complejos
   - **Compresión CSI**: Reducción de overhead de feedback en $8\times-16\times$ manteniendo rendimiento
   - **Detección MIMO**: Aproximación a rendimiento ML con complejidad fija, 90-98% del rendimiento óptimo
   - **Beamforming**: Latencia reducida en $100\times$ comparado con optimización iterativa
   - **Resource Allocation**: Coordinación aprendida en sistemas multi-agente supera métodos centralizados

2. **Viabilidad de Implementación**: Los desafíos de complejidad computacional pueden abordarse mediante:
   - Cuantización (INT8/INT4) reduce recursos en $4\times-8\times$ con degradación <1 dB
   - Poda estructurada permite reducción de parámetros en $10\times$
   - Hardware especializado (FPGAs, ASICs) logra latencia sub-milisegundo con eficiencia energética superior

3. **Adaptabilidad y Generalización**: Meta-learning y transfer learning permiten:
   - Adaptación rápida a nuevos escenarios con datos limitados
   - Reducción de costos de entrenamiento en $100\times$ mediante reutilización de modelos
   - Robustez a domain shift mediante técnicas de domain adaptation

4. **Comunicación Semántica**: Representa cambio paradigmático con:
   - Compresión de $10\times-100\times$ para tareas específicas
   - Optimización end-to-end para objetivo final en lugar de reconstrucción exacta
   - Potencial de redefinir arquitecturas de comunicación

5. **Desafíos Persistentes**: Áreas requiriendo investigación continua:
   - Estandarización e interoperabilidad entre vendors
   - Robustez adversarial y seguridad
   - Interpretabilidad y explicabilidad para deployment en sistemas críticos
   - Límites teóricos fundamentales de comunicación aprendida
   - Sostenibilidad ambiental del entrenamiento masivo

**Direcciones Futuras Prometedoras**:

La convergencia de múltiples tendencias tecnológicas sugiere un futuro donde:

- **Foundation Models** pre-entrenados en datos diversos facilitan desarrollo rápido de aplicaciones especializadas
- **Self-Supervised Learning** reduce dependencia de datos etiquetados costosos
- **Continual Learning** permite sistemas que mejoran continuamente durante deployment
- **Integración con O-RAN** democratiza innovación mediante interfaces abiertas y marketplace de algoritmos
- **Comunicaciones Terahertz** habilitadas por IA superan limitaciones de técnicas tradicionales
- **Neuromorphic Computing** ofrece eficiencia energética revolucionaria para procesamiento en edge

**Perspectiva Final**:

La integración de Inteligencia Artificial y Deep Learning en la capa física representa no meramente una optimización incremental de tecnologías existentes, sino una transformación fundamental del paradigma de diseño de sistemas de comunicaciones inalámbricas. La transición de enfoques model-based a data-driven, y finalmente a sistemas híbridos que combinan conocimiento físico con capacidad de aprendizaje, promete desbloquear capacidades que eran inalcanzables mediante métodos convencionales.

Los sistemas 6G nativos de IA no solo lograrán mejoras cuantitativas en métricas tradicionales (throughput, latencia, eficiencia espectral), sino que habilitarán capacidades cualitativamente nuevas: adaptación instantánea a condiciones cambiantes, comunicación semántica orientada a tareas, coordinación autónoma en redes ultra-densas, y personalización extrema de servicios.

Sin embargo, la realización de esta visión requiere esfuerzos concertados en múltiples frentes: desarrollo de teoría fundamental que establezca límites y garantías, creación de datasets públicos representativos, estandarización de arquitecturas e interfaces, desarrollo de hardware eficiente, establecimiento de marcos regulatorios apropiados, y formación de talento especializado.

La investigación presentada en este artículo demuestra que las bases técnicas están establecidas. El desafío ahora es traducir estos avances de laboratorio en sistemas desplegados que transformen comunicaciones inalámbricas para la próxima década y más allá. El futuro de las comunicaciones es indudablemente inteligente.

---

## REFERENCIAS

[1] M. Giordani et al., "Toward 6G networks: Use cases and technologies," IEEE Communications Magazine, vol. 58, no. 3, pp. 55-61, 2020.

[2] W. Saad, M. Bennis, and M. Chen, "A vision of 6G wireless systems: Applications, trends, technologies, and open research problems," IEEE Network, vol. 34, no. 3, pp. 134-142, 2020.

[3] T. S. Rappaport et al., "Wireless communications and applications above 100 GHz: Opportunities and challenges for 6G and beyond," IEEE Access, vol. 7, pp. 78729-78757, 2019.

[4] M. Latva-aho and K. Leppänen, "Key drivers and research challenges for 6G ubiquitous wireless intelligence," University of Oulu, White Paper, 2019.

[5] T. O'Shea and J. Hoydis, "An introduction to deep learning for the physical layer," IEEE Transactions on Cognitive Communications and Networking, vol. 3, no. 4, pp. 563-575, 2017.

[6] C. Zhang et al., "Deep learning in mobile and wireless networking: A survey," IEEE Communications Surveys & Tutorials, vol. 21, no. 3, pp. 2224-2287, 2019.

[7] N. C. Luong et al., "Applications of deep reinforcement learning in communications and sensing: A survey," IEEE Communications Surveys & Tutorials, vol. 21, no. 4, pp. 3133-3174, 2019.

[8] J. M. Jornet and I. F. Akyildiz, "Channel modeling and capacity analysis for electromagnetic wireless nanonetworks in the terahertz band," IEEE Transactions on Wireless Communications, vol. 10, no. 10, pp. 3211-3221, 2011.

[9] Z. Chen et al., "A survey on terahertz communications," China Communications, vol. 16, no. 2, pp. 1-35, 2019.

[10] E. G. Larsson et al., "Massive MIMO for next generation wireless systems," IEEE Communications Magazine, vol. 52, no. 2, pp. 186-195, 2014.

[11] F. Rusek et al., "Scaling up MIMO: Opportunities and challenges with very large arrays," IEEE Signal Processing Magazine, vol. 30, no. 1, pp. 40-60, 2013.

[12] K. B. Letaief et al., "The roadmap to 6G: AI empowered wireless networks," IEEE Communications Magazine, vol. 57, no. 8, pp. 84-90, 2019.

[13] H. Ye, G. Y. Li, and B.-H. Juang, "Power of deep learning for channel estimation and signal detection in OFDM systems," IEEE Wireless Communications Letters, vol. 7, no. 1, pp. 114-117, 2018.

[14] S. Dörner et al., "Deep learning based communication over the air," IEEE Journal of Selected Topics in Signal Processing, vol. 12, no. 1, pp. 132-143, 2018.

[15] Q. Mao et al., "Deep learning for intelligent wireless networks: A comprehensive survey," IEEE Communications Surveys & Tutorials, vol. 20, no. 4, pp. 2595-2621, 2018.

[16] A. Goldsmith, Wireless Communications. Cambridge University Press, 2005.

[17] D. Tse and P. Viswanath, Fundamentals of Wireless Communication. Cambridge University Press, 2005.

[18] A. Paulraj, R. Nabar, and D. Gore, Introduction to Space-Time Wireless Communications. Cambridge University Press, 2003.

[19] T. J. O'Shea, K. Karra, and T. C. Clancy, "Learning to communicate: Channel auto-encoders, domain specific regularizers, and attention," in Proc. IEEE SPAWC, 2016.

[20] H. Kim et al., "Communication algorithms via deep learning," in Proc. ICLR, 2018.

[21] F. A. Aoudia and J. Hoydis, "End-to-end learning of communications systems without a channel model," in Proc. IEEE ACSSC, 2018.

[22] I. Goodfellow, Y. Bengio, and A. Courville, Deep Learning. MIT Press, 2016.

[23] Y. LeCun, Y. Bengio, and G. Hinton, "Deep learning," Nature, vol. 521, pp. 436-444, 2015.

[24] V. Nair and G. E. Hinton, "Rectified linear units improve restricted Boltzmann machines," in Proc. ICML, 2010.

[25] K. He et al., "Deep residual learning for image recognition," in Proc. IEEE CVPR, 2016.

[26] Y. LeCun et al., "Gradient-based learning applied to document recognition," Proceedings of the IEEE, vol. 86, no. 11, pp. 2278-2324, 1998.

[27] S. Hochreiter and J. Schmidhuber, "Long short-term memory," Neural Computation, vol. 9, no. 8, pp. 1735-1780, 1997.

[28] K. Cho et al., "Learning phrase representations using RNN encoder-decoder for statistical machine translation," in Proc. EMNLP, 2014.

[29] D. P. Kingma and M. Welling, "Auto-encoding variational Bayes," in Proc. ICLR, 2014.

[30] C. Doersch, "Tutorial on variational autoencoders," arXiv:1606.05908, 2016.

[31] I. Goodfellow et al., "Generative adversarial nets," in Proc. NIPS, 2014.

[32] M. Arjovsky, S. Chintala, and L. Bottou, "Wasserstein GAN," in Proc. ICML, 2017.

[33] A. Vaswani et al., "Attention is all you need," in Proc. NIPS, 2017.

[34] N. Carion et al., "End-to-end object detection with transformers," in Proc. ECCV, 2020.

[35] R. S. Sutton and A. G. Barto, Reinforcement Learning: An Introduction, 2nd ed. MIT Press, 2018.

[36] V. Mnih et al., "Human-level control through deep reinforcement learning," Nature, vol. 518, pp. 529-533, 2015.

[37] J. Schulman et al., "Proximal policy optimization algorithms," arXiv:1707.06347, 2017.

[38] M. Biguesh and A. B. Gershman, "Training-based MIMO channel estimation: A study of estimator tradeoffs and optimal training signals," IEEE Transactions on Signal Processing, vol. 54, no. 3, pp. 884-893, 2006.

[39] E. Björnson, J. Hoydis, and L. Sanguinetti, "Massive MIMO networks: Spectral, energy, and hardware efficiency," Foundations and Trends in Signal Processing, vol. 11, no. 3-4, pp. 154-655, 2017.

[40] S. Kay, Fundamentals of Statistical Signal Processing: Estimation Theory. Prentice Hall, 1993.

[41] Y. S. Cho et al., MIMO-OFDM Wireless Communications with MATLAB. Wiley-IEEE Press, 2010.

[42] M. Morelli and U. Mengali, "A comparison of pilot-aided channel estimation methods for OFDM systems," IEEE Transactions on Signal Processing, vol. 49, no. 12, pp. 3065-3073, 2001.

[43] O. Edfors et al., "OFDM channel estimation by singular value decomposition," IEEE Transactions on Communications, vol. 46, no. 7, pp. 931-939, 1998.

[44] J.-J. van de Beek et al., "On channel estimation in OFDM systems," in Proc. IEEE VTC, 1995.

[45] T. L. Marzetta, "Noncooperative cellular wireless with unlimited numbers of base station antennas," IEEE Transactions on Wireless Communications, vol. 9, no. 11, pp. 3590-3600, 2010.

[46] H. Ye, G. Y. Li, and B.-H. Juang, "Power of deep learning for channel estimation and signal detection in OFDM systems," IEEE Wireless Communications Letters, vol. 7, no. 1, pp. 114-117, 2018.

[47] C.-K. Wen et al., "Deep learning for massive MIMO CSI feedback," IEEE Wireless Communications Letters, vol. 7, no. 5, pp. 748-751, 2018.

[48] M. Soltani et al., "Deep learning-based channel estimation," IEEE Communications Letters, vol. 23, no. 4, pp. 652-655, 2019.

[49] W. Jakes, Microwave Mobile Communications. Wiley-IEEE Press, 1994.

[50] P. Dong et al., "Deep CNN-based channel estimation for mmWave massive MIMO systems," IEEE Journal of Selected Topics in Signal Processing, vol. 13, no. 5, pp. 989-1000, 2019.

