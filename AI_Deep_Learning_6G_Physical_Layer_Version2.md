# Inteligencia Artificial y Deep Learning en la Capa Física de Sistemas de Telecomunicaciones Inalámbricas 6G y de Próxima Generación

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

$$\mathbf{y} = \mathbf{H}\mathbf{x} + \mathbf{n}$$

donde $\mathbf{x} \in \mathbb{C}^{N_t}$ es el vector de símbolos transmitidos, $\mathbf{H} \in \mathbb{C}^{N_r \times N_t}$ es la matriz de canal MIMO, $\mathbf{n} \sim \mathcal{CN}(0, \sigma^2\mathbf{I}_{N_r})$ es el ruido gaussiano complejo, y $\mathbf{y} \in \mathbb{C}^{N_r}$ es el vector recibido [17].

El enfoque tradicional diseña el transmisor $f_{\text{TX}}(\cdot)$ y receptor $f_{\text{RX}}(\cdot)$ como funciones separadas:

$$\hat{\mathbf{s}} = f_{\text{RX}}(\mathbf{y}, \hat{\mathbf{H}}) = f_{\text{RX}}(\mathbf{H}f_{\text{TX}}(\mathbf{s}) + \mathbf{n}, \hat{\mathbf{H}})$$

donde $\mathbf{s}$ son los bits de información, $\hat{\mathbf{H}}$ es una estimación del canal, y $\hat{\mathbf{s}}$ son los bits decodificados [18].

En contraste, el enfoque nativo de IA considera el sistema de comunicación completo como una función parametrizada por redes neuronales profundas $f_{\theta}(\cdot)$ y $g_{\phi}(\cdot)$ para transmisión y recepción respectivamente, optimizadas end-to-end:

$$\theta^*, \phi^* = \arg\min_{\theta,\phi} \mathbb{E}_{\mathbf{s},\mathbf{H},\mathbf{n}}\left[\mathcal{L}(\mathbf{s}, g_{\phi}(\mathbf{H}f_{\theta}(\mathbf{s}) + \mathbf{n}))\right]$$

donde $\mathcal{L}(\cdot)$ es una función de pérdida diferenciable (típicamente entropía cruzada para clasificación de símbolos) y la esperanza se toma sobre la distribución conjunta de mensajes, realizaciones de canal, y ruido [19], [20].

Esta formulación permite que el sistema aprenda representaciones óptimas directamente de los datos, potencialmente superando diseños manuales al explotar regularidades estadísticas que no son capturadas por modelos simplificados [21].

### C. Arquitecturas Fundamentales de Deep Learning para PHY

Las arquitecturas de DL aplicadas a la capa física incluyen diversos paradigmas, cada uno con características particulares adecuadas para diferentes sub-problemas [22], [23]:

**1) Redes Feedforward Profundas (DNN)**: Las redes neuronales totalmente conectadas con múltiples capas ocultas constituyen la arquitectura más básica. Para un problema de detección de símbolos, una DNN mapea señales recibidas $\mathbf{y}$ a estimaciones de bits transmitidos:

$$\mathbf{h}^{(0)} = \mathbf{y}$$
$$\mathbf{h}^{(l)} = \sigma\left(\mathbf{W}^{(l)}\mathbf{h}^{(l-1)} + \mathbf{b}^{(l)}\right), \quad l = 1,\ldots,L-1$$
$$\hat{\mathbf{s}} = \text{softmax}\left(\mathbf{W}^{(L)}\mathbf{h}^{(L-1)} + \mathbf{b}^{(L)}\right)$$

donde $\sigma(\cdot)$ es una función de activación no lineal (ReLU, tanh), $\mathbf{W}^{(l)}$ y $\mathbf{b}^{(l)}$ son matrices de pesos y vectores de sesgo de la capa $l$ [24].

**2) Redes Neuronales Convolucionales (CNN)**: Las CNN explotan estructura espacial o temporal en señales mediante operaciones de convolución que comparten parámetros:

$$\mathbf{h}^{(l)}_i = \sigma\left(\sum_{j}\sum_{k}\mathbf{W}^{(l)}_{i,j,k}\mathbf{h}^{(l-1)}_{j,k} + b^{(l)}_i\right)$$

donde el índice $k$ representa desplazamiento temporal o espacial. Las CNN son particularmente efectivas para procesamiento de secuencias temporales de símbolos o explotar correlación espacial en arrays de antenas [25], [26].

**3) Redes Neuronales Recurrentes (RNN) y LSTM**: Para capturar dependencias temporales en secuencias de símbolos o evolución temporal del canal, se utilizan arquitecturas recurrentes:

$$\mathbf{h}_t = \sigma(\mathbf{W}_{hh}\mathbf{h}_{t-1} + \mathbf{W}_{xh}\mathbf{x}_t + \mathbf{b}_h)$$
$$\mathbf{o}_t = \mathbf{W}_{ho}\mathbf{h}_t + \mathbf{b}_o$$

Las Long Short-Term Memory (LSTM) networks extienden este concepto con mecanismos de compuerta para capturar dependencias de largo alcance:

$$\mathbf{f}_t = \sigma_g(\mathbf{W}_f\mathbf{x}_t + \mathbf{U}_f\mathbf{h}_{t-1} + \mathbf{b}_f)$$
$$\mathbf{i}_t = \sigma_g(\mathbf{W}_i\mathbf{x}_t + \mathbf{U}_i\mathbf{h}_{t-1} + \mathbf{b}_i)$$
$$\mathbf{o}_t = \sigma_g(\mathbf{W}_o\mathbf{x}_t + \mathbf{U}_o\mathbf{h}_{t-1} + \mathbf{b}_o)$$
$$\tilde{\mathbf{c}}_t = \sigma_c(\mathbf{W}_c\mathbf{x}_t + \mathbf{U}_c\mathbf{h}_{t-1} + \mathbf{b}_c)$$
$$\mathbf{c}_t = \mathbf{f}_t \odot \mathbf{c}_{t-1} + \mathbf{i}_t \odot \tilde{\mathbf{c}}_t$$
$$\mathbf{h}_t = \mathbf{o}_t \odot \sigma_h(\mathbf{c}_t)$$

donde $\mathbf{f}_t$, $\mathbf{i}_t$, $\mathbf{o}_t$ son compuertas de olvido, entrada y salida respectivamente, $\mathbf{c}_t$ es el estado de celda, y $\odot$ denota producto elemento-a-elemento [27], [28].

**4) Autocodificadores (AE)**: Los autocodificadores representan toda la cadena de comunicación como un sistema de codificación-decodificación aprendido:

$$\text{Encoder: } \mathbf{z} = f_{\text{enc}}(\mathbf{s}; \theta_{\text{enc}})$$
$$\text{Channel: } \mathbf{y} = \mathcal{C}(\mathbf{z})$$
$$\text{Decoder: } \hat{\mathbf{s}} = f_{\text{dec}}(\mathbf{y}; \theta_{\text{dec}})$$

La función objetivo es minimizar la pérdida de reconstrucción:

$$\mathcal{L}(\theta_{\text{enc}}, \theta_{\text{dec}}) = \mathbb{E}_{\mathbf{s},\mathcal{C}}\left[\|\mathbf{s} - \hat{\mathbf{s}}\|^2\right]$$

Los autocodificadores variacionales (VAE) introducen regularización probabilística:

$$\mathcal{L}_{\text{VAE}} = \mathbb{E}_{q_{\phi}(\mathbf{z}|\mathbf{s})}\left[\log p_{\theta}(\mathbf{s}|\mathbf{z})\right] - D_{KL}(q_{\phi}(\mathbf{z}|\mathbf{s})\|p(\mathbf{z}))$$

donde $D_{KL}$ es la divergencia de Kullback-Leibler que actúa como regularizador [29], [30].

**5) Redes Generativas Adversarias (GAN)**: Las GAN se utilizan para modelado y síntesis de canales realistas mediante competencia entre generador y discriminador:

$$\min_G \max_D \mathbb{E}_{\mathbf{h}\sim p_{\text{data}}(\mathbf{h})}\left[\log D(\mathbf{h})\right] + \mathbb{E}_{\mathbf{z}\sim p_{\mathbf{z}}(\mathbf{z})}\left[\log(1-D(G(\mathbf{z})))\right]$$

El generador $G(\mathbf{z})$ aprende a generar realizaciones de canal sintéticas indistinguibles de datos reales según el discriminador $D(\mathbf{h})$ [31], [32].

**6) Transformers y Mecanismos de Atención**: Introducidos originalmente para procesamiento de lenguaje natural, los transformers se han adaptado para procesamiento de señales en comunicaciones mediante mecanismos de auto-atención:

$$\text{Attention}(\mathbf{Q}, \mathbf{K}, \mathbf{V}) = \text{softmax}\left(\frac{\mathbf{Q}\mathbf{K}^T}{\sqrt{d_k}}\right)\mathbf{V}$$

donde $\mathbf{Q}$, $\mathbf{K}$, $\mathbf{V}$ son matrices de consulta, clave y valor derivadas de las señales de entrada mediante proyecciones lineales. Los transformers son particularmente efectivos para capturar dependencias de largo alcance en secuencias temporales y correlaciones espaciales en sistemas MIMO masivos [33], [34].

**7) Aprendizaje por Refuerzo Profundo (DRL)**: Para problemas de optimización secuencial y asignación de recursos, el DRL modela el sistema como un proceso de decisión de Markov (MDP) con tupla $(\mathcal{S}, \mathcal{A}, \mathcal{P}, \mathcal{R}, \gamma)$ donde $\mathcal{S}$ es el espacio de estados, $\mathcal{A}$ es el espacio de acciones, $\mathcal{P}$ define transiciones, $\mathcal{R}$ es la función de recompensa, y $\gamma$ es el factor de descuento [35].

El objetivo es aprender una política óptima $\pi^*$ que maximice el retorno esperado:

$$\pi^* = \arg\max_{\pi} \mathbb{E}\left[\sum_{t=0}^{\infty}\gamma^t R(s_t, a_t) \Big| \pi\right]$$

Algoritmos como Deep Q-Networks (DQN), Policy Gradient, Actor-Critic, y Proximal Policy Optimization (PPO) se utilizan para aproximar $\pi^*$ mediante redes neuronales [36], [37].

### D. Estructura del Artículo

El resto de este artículo está organizado como sigue. La Sección II presenta técnicas de IA para estimación y predicción de canal. La Sección III analiza esquemas de retroalimentación CSI basados en DL. La Sección IV explora sistemas MIMO masivos con procesamiento neural. La Sección V examina codificación y decodificación de canal mediante DL. La Sección VI discute detección de señales con redes neuronales. La Sección VII presenta beamforming inteligente. La Sección VIII analiza gestión de recursos espectrales mediante IA. La Sección IX discute modulación y forma de onda adaptativas. La Sección X introduce comunicaciones semánticas. La Sección XI aborda desafíos de implementación. La Sección XII concluye con direcciones futuras.

---

## II. ESTIMACIÓN Y PREDICCIÓN DE CANAL MEDIANTE DEEP LEARNING

La estimación precisa del canal de comunicación es fundamental para sistemas de comunicaciones inalámbricas coherentes, afectando directamente el rendimiento de ecualización, detección, y procesamiento MIMO [38]. Los métodos tradicionales como estimación por mínimos cuadrados (LS), mínimo error cuadrático medio (MMSE), y técnicas basadas en pilotos enfrentan limitaciones en escenarios 6G caracterizados por alta movilidad, canales de alta dimensionalidad, y recursos de piloto limitados [39], [40].

### A. Formulación del Problema de Estimación de Canal

En un sistema OFDM/OFDMA multiportadora con $N$ subportadoras y $N_t$ antenas transmisoras, $N_r$ antenas receptoras, la señal recibida en la subportadora $k$ y símbolo temporal $t$ se expresa:

$$\mathbf{Y}[k,t] = \mathbf{H}[k,t]\mathbf{X}[k,t] + \mathbf{N}[k,t]$$

donde $\mathbf{Y}[k,t] \in \mathbb{C}^{N_r \times 1}$, $\mathbf{H}[k,t] \in \mathbb{C}^{N_r \times N_t}$ es la respuesta en frecuencia del canal, $\mathbf{X}[k,t] \in \mathbb{C}^{N_t \times 1}$ son símbolos transmitidos, y $\mathbf{N}[k,t] \sim \mathcal{CN}(0, \sigma^2\mathbf{I})$ es ruido [41].

El problema de estimación de canal consiste en estimar $\hat{\mathbf{H}}[k,t]$ a partir de observaciones $\mathbf{Y}[k,t]$ en posiciones de piloto conocidas y potencialmente símbolos de datos previamente detectados [42].

**Estimación LS Tradicional**: En posiciones de piloto donde $\mathbf{X}_p$ es conocido:

$$\hat{\mathbf{H}}_{\text{LS}} = \mathbf{Y}_p\mathbf{X}_p^{\dagger}$$

donde $\mathbf{X}_p^{\dagger} = (\mathbf{X}_p^H\mathbf{X}_p)^{-1}\mathbf{X}_p^H$ es la pseudo-inversa. El estimador LS no requiere conocimiento estadístico del canal pero tiene alto error cuadrático medio (MSE) en condiciones de bajo SNR [43].

**Estimación MMSE Tradicional**: El estimador MMSE minimiza el MSE esperado:

$$\hat{\mathbf{H}}_{\text{MMSE}} = \mathbf{R}_{\mathbf{H}\mathbf{H}}\mathbf{R}_{\tilde{\mathbf{H}}\tilde{\mathbf{H}}}^{-1}\hat{\mathbf{H}}_{\text{LS}}$$

donde $\mathbf{R}_{\mathbf{H}\mathbf{H}} = \mathbb{E}[\mathbf{H}\mathbf{H}^H]$ es la matriz de covarianza del canal y $\mathbf{R}_{\tilde{\mathbf{H}}\tilde{\mathbf{H}}} = \mathbf{R}_{\mathbf{H}\mathbf{H}} + \sigma^2(\mathbf{X}_p\mathbf{X}_p^H)^{-1}$ es la covarianza del error [44].

El estimador MMSE requiere conocimiento de estadísticas de segundo orden del canal, que pueden ser difíciles de obtener o no estacionarias en entornos dinámicos [45].

### B. Arquitecturas de DL para Estimación de Canal

**1) DNN para Estimación Directa**: Una aproximación directa utiliza DNNs para mapear señales recibidas de piloto a estimaciones de canal [46], [47]:

$$\hat{\mathbf{H}} = f_{\text{DNN}}(\mathbf{Y}_p; \theta)$$

donde $f_{\text{DNN}}$ es una red neuronal profunda con parámetros $\theta$ entrenados para minimizar:

$$\mathcal{L}(\theta) = \mathbb{E}\left[\|\mathbf{H} - \hat{\mathbf{H}}\|_F^2\right]$$

siendo $\|\cdot\|_F$ la norma de Frobenius. La red aprende implícitamente las estadísticas del canal y la estructura de correlación desde los datos de entrenamiento [48].

Para un sistema con $N_t = 4$ antenas transmisoras, $N_r = 4$ receptoras, y $N_p = 16$ pilotos, la entrada tiene dimensión $2N_rN_p$ (partes real e imaginaria), y la salida tiene dimensión $2N_rN_t$. Una arquitectura típica incluye:

$$\text{Input}(128) \rightarrow \text{Dense}(256, \text{ReLU}) \rightarrow \text{Dense}(512, \text{ReLU}) \rightarrow$$
$$\text{Dense}(512, \text{ReLU}) \rightarrow \text{Dense}(256, \text{ReLU}) \rightarrow \text{Output}(32)$$

**2) CNN para Explotación de Correlación Espacio-Frecuencial**: Los canales inalámbricos exhiben correlación en dominios espacial (entre antenas), frecuencial (entre subportadoras), y temporal [49]. Las CNNs pueden explotar esta estructura mediante filtros convolucionales:

$$\mathbf{H}^{(l)}[i,j,k] = \sigma\left(\sum_{m,n,p}\mathbf{W}^{(l)}[m,n,p]\mathbf{H}^{(l-1)}[i+m,j+n,k+p] + b^{(l)}\right)$$

donde los índices $i,j,k$ corresponden a dimensiones de antena, frecuencia, y tiempo [50], [51].

Estudios recientes demuestran que CNNs con arquitectura ResNet pueden reducir el MSE de estimación en 3-5 dB comparado con MMSE en canales con alta correlación espacial [52].

**3) Arquitecturas Basadas en Transformers**: Los transformers con mecanismos de auto-atención pueden capturar dependencias de largo alcance en el dominio de frecuencia sin asumir modelos de correlación específicos [53]:

$$\text{Attention}(\mathbf{Q}, \mathbf{K}, \mathbf{V}) = \text{softmax}\left(\frac{\mathbf{Q}\mathbf{K}^T}{\sqrt{d_k}}\right)\mathbf{V}$$

donde las matrices de consulta, clave y valor se derivan de las observaciones de canal mediante proyecciones lineales aprendidas. El mecanismo de atención asigna pesos dinámicos a diferentes posiciones de frecuencia basándose en su relevancia para estimar una posición objetivo [54].

**4) Estimación de Canal Asistida por GAN**: Las GANs se utilizan para refinar estimaciones preliminares generando realizaciones de canal más realistas [55], [56]:

$$\hat{\mathbf{H}}_{\text{refined}} = G(\hat{\mathbf{H}}_{\text{LS}}; \theta_G)$$

El generador $G$ se entrena adversarialmente contra un discriminador $D$ que intenta distinguir canales reales de refinados:

$$\min_{\theta_G}\max_{\theta_D} \mathbb{E}_{\mathbf{H}}[\log D(\mathbf{H})] + \mathbb{E}_{\hat{\mathbf{H}}_{\text{LS}}}[\log(1-D(G(\hat{\mathbf{H}}_{\text{LS}})))]$$

Adicionalmente, una pérdida de reconstrucción asegura fidelidad:

$$\mathcal{L}_{\text{total}} = \mathcal{L}_{\text{adv}} + \lambda\mathcal{L}_{\text{recon}}$$
$$\mathcal{L}_{\text{recon}} = \mathbb{E}\left[\|\mathbf{H} - G(\hat{\mathbf{H}}_{\text{LS}})\|_F^2\right]$$

Esta aproximación ha demostrado mejoras sustanciales en escenarios con pilotos extremadamente escasos [57].

### C. Predicción de Canal mediante RNN y LSTM

En sistemas de alta movilidad y aplicaciones con requisitos de latencia ultra-baja, la predicción de canal futuro permite compensación proactiva y scheduling predictivo [58], [59]. La evolución temporal del canal puede modelarse como un proceso estocástico:

$$\mathbf{H}[t+1] = f(\mathbf{H}[t], \mathbf{H}[t-1], \ldots, \mathbf{H}[t-L]) + \mathbf{e}[t]$$

donde $f(\cdot)$ es una función no lineal y $\mathbf{e}[t]$ representa innovación estocástica [60].

**RNN/LSTM para Predicción Temporal**: Las LSTMs son particularmente efectivas para capturar dependencias temporales en secuencias de canal [61], [62]:

$$\hat{\mathbf{H}}[t+\Delta t] = f_{\text{LSTM}}(\mathbf{H}[t], \mathbf{H}[t-1], \ldots, \mathbf{H}[t-L]; \theta)$$

La arquitectura LSTM mantiene un estado de celda $\mathbf{c}_t$ que acumula información de largo plazo, mientras que compuertas controlan el flujo de información:

$$\mathbf{f}_t = \sigma(\mathbf{W}_f[\mathbf{h}_{t-1}, \mathbf{H}[t]] + \mathbf{b}_f)$$
$$\mathbf{i}_t = \sigma(\mathbf{W}_i[\mathbf{h}_{t-1}, \mathbf{H}[t]] + \mathbf{b}_i)$$
$$\tilde{\mathbf{c}}_t = \tanh(\mathbf{W}_c[\mathbf{h}_{t-1}, \mathbf{H}[t]] + \mathbf{b}_c)$$
$$\mathbf{c}_t = \mathbf{f}_t \odot \mathbf{c}_{t-1} + \mathbf{i}_t \odot \tilde{\mathbf{c}}_t$$
$$\mathbf{o}_t = \sigma(\mathbf{W}_o[\mathbf{h}_{t-1}, \mathbf{H}[t]] + \mathbf{b}_o)$$
$$\mathbf{h}_t = \mathbf{o}_t \odot \tanh(\mathbf{c}_t)$$
$$\hat{\mathbf{H}}[t+\Delta t] = \mathbf{W}_h\mathbf{h}_t + \mathbf{b}_h$$

El entrenamiento minimiza el error de predicción:

$$\mathcal{L}(\theta) = \sum_{t=1}^{T-\Delta t}\|\mathbf{H}[t+\Delta t] - \hat{\mathbf{H}}[t+\Delta t]\|_F^2$$

**Gated Recurrent Units (GRU)**: Una variante simplificada de LSTM con menor complejidad computacional pero rendimiento comparable [63]:

$$\mathbf{r}_t = \sigma(\mathbf{W}_r[\mathbf{h}_{t-1}, \mathbf{H}[t]])$$
$$\mathbf{z}_t = \sigma(\mathbf{W}_z[\mathbf{h}_{t-1}, \mathbf{H}[t]])$$
$$\tilde{\mathbf{h}}_t = \tanh(\mathbf{W}[\mathbf{r}_t \odot \mathbf{h}_{t-1}, \mathbf{H}[t]])$$
$$\mathbf{h}_t = (1-\mathbf{z}_t) \odot \mathbf{h}_{t-1} + \mathbf{z}_t \odot \tilde{\mathbf{h}}_t$$

donde $\mathbf{r}_t$ y $\mathbf{z}_t$ son compuertas de reset y actualización respectivamente.

**Predicción Multistep**: Para predicción de múltiples pasos hacia el futuro, se emplean estrategias recursivas o direct multistep:

- **Recursiva**: $\hat{\mathbf{H}}[t+k] = f(\hat{\mathbf{H}}[t+k-1], \ldots)$
- **Direct**: $\hat{\mathbf{H}}[t+k] = f_k(\mathbf{H}[t], \mathbf{H}[t-1], \ldots)$

La aproximación direct entrena modelos separados para cada horizonte de predicción, evitando propagación de errores pero incrementando complejidad de modelo [64].

**Modelos Seq2Seq con Mecanismos de Atención**: Para capturar patrones complejos, arquitecturas encoder-decoder con atención permiten al decodificador enfocarse en partes relevantes de la secuencia de entrada [65]:

$$\text{Context: } \mathbf{c}_t = \sum_{i=1}^{T}\alpha_{t,i}\mathbf{h}_i$$
$$\alpha_{t,i} = \frac{\exp(e_{t,i})}{\sum_{j=1}^{T}\exp(e_{t,j})}$$
$$e_{t,i} = \text{score}(\mathbf{s}_{t-1}, \mathbf{h}_i)$$

donde $\mathbf{h}_i$ son estados ocultos del encoder, $\mathbf{s}_t$ es el estado del decoder, y $\mathbf{c}_t$ es el vector de contexto ponderado por coeficientes de atención $\alpha_{t,i}$ [66].

### D. Explotación de Estructura Dispersa

Los canales mmWave y THz típicamente exhiben estructura dispersa en el dominio angular debido a propagación limitada por trayectorias [67], [68]. Esta dispersidad puede explotarse para reducir overhead de estimación y complejidad computacional.

**Compressed Sensing (CS) con DL**: La teoría de compressed sensing establece que señales dispersas pueden recuperarse de mediciones sub-Nyquist mediante optimización $\ell_1$:

$$\min_{\mathbf{h}} \|\mathbf{h}\|_1 \quad \text{s.t.} \quad \mathbf{y} = \mathbf{\Phi}\mathbf{h}$$

donde $\mathbf{h}$ es la representación dispersa del canal, $\mathbf{\Phi}$ es la matriz de medición (pilotos), y $\mathbf{y}$ son observaciones [69].

Las redes neuronales pueden aprender a resolver este problema de optimización de forma más eficiente que algoritmos iterativos tradicionales (OMP, CoSaMP) mediante redes de despliegue (unfolding) [70], [71]:

$$\mathbf{h}^{(k+1)} = \mathcal{N}_{\theta}\left(\mathbf{h}^{(k)}, \mathbf{\Phi}, \mathbf{y}\right)$$

donde cada iteración del algoritmo de optimización se mapea a una capa de la red neuronal, permitiendo aprendizaje de parámetros de regularización y operadores de umbralización [72].

**Learned ISTA (LISTA)**: Una instancia específica de unfolding aplica Iterative Shrinkage-Thresholding Algorithm (ISTA):

$$\mathbf{h}^{(k+1)} = \eta_{\lambda^{(k)}}\left(\mathbf{h}^{(k)} + \mathbf{W}^{(k)}(\mathbf{y} - \mathbf{\Phi}\mathbf{h}^{(k)})\right)$$

donde $\eta_{\lambda}(\cdot)$ es el operador de soft-thresholding:

$$\eta_{\lambda}(x) = \text{sign}(x)\max(|x|-\lambda, 0)$$

Los parámetros $\mathbf{W}^{(k)}$ y $\lambda^{(k)}$ se aprenden para cada capa $k$, acelerando significativamente la convergencia comparado con ISTA clásico [73].

### E. Estimación de Canal sin Pilotos mediante DL

Los esquemas de estimación sin pilotos (blind channel estimation) explotan estructura de señales de datos para estimar el canal sin dedicar recursos explícitos a pilotos, maximizando eficiencia espectral [74], [75].

**Autocodificadores para Estimación Blind**: Un autocodificador puede aprender conjuntamente codificación, estimación de canal, y decodificación:

$$\text{Encoder: } \mathbf{x} = f_{\text{enc}}(\mathbf{s}; \theta_{\text{enc}})$$
$$\text{Channel: } \mathbf{y} = \mathbf{H}\mathbf{x} + \mathbf{n}$$
$$\text{Estimator: } \hat{\mathbf{H}} = f_{\text{est}}(\mathbf{y}; \theta_{\text{est}})$$
$$\text{Decoder: } \hat{\mathbf{s}} = f_{\text{dec}}(\mathbf{y}, \hat{\mathbf{H}}; \theta_{\text{dec}})$$

La función de pérdida combina reconstrucción de datos y calidad de estimación:

$$\mathcal{L} = \mathbb{E}\left[\|\mathbf{s} - \hat{\mathbf{s}}\|^2 + \beta\|\mathbf{H} - \hat{\mathbf{H}}\|_F^2\right]$$

El encoder aprende a insertar estructura implícita en señales transmitidas que facilita estimación ciega [76].

**Deep Blind Equalization**: Extiende técnicas clásicas como Constant Modulus Algorithm (CMA) utilizando DNNs para aprender funciones de costo adaptativas [77]:

$$\mathcal{L}_{\text{CMA}} = \mathbb{E}\left[(|\hat{s}[n]|^2 - R_2)^2\right]$$

donde $R_2 = \mathbb{E}[|s[n]|^4]/\mathbb{E}[|s[n]|^2]$ es el módulo constante objetivo. Las DNNs pueden aprender generalizaciones de este criterio para constelaciones arbitrarias [78].

### F. Transfer Learning y Meta-Learning para Estimación de Canal

En sistemas prácticos, el entrenamiento de modelos DL para cada escenario de canal específico es prohibitivamente costoso. Transfer learning y meta-learning permiten adaptación rápida a nuevas condiciones con datos limitados [79], [80].

**Transfer Learning**: Un modelo pre-entrenado en un conjunto de escenarios de canal diversos se adapta a un escenario objetivo específico mediante fine-tuning de capas superiores:

1. **Pre-entrenamiento**: Entrenar $f_{\theta}$ en dataset grande $\mathcal{D}_{\text{source}}$
2. **Fine-tuning**: Congelar capas inferiores y re-entrenar capas superiores en $\mathcal{D}_{\text{target}}$

$$\theta_{\text{target}}^* = \arg\min_{\theta_{\text{upper}}} \mathcal{L}_{\text{target}}(f(\cdot; \theta_{\text{frozen}}, \theta_{\text{upper}}))$$

Esta aproximación reduce significativamente los requisitos de datos de entrenamiento y tiempo de adaptación [81].

**Model-Agnostic Meta-Learning (MAML)**: MAML busca parámetros iniciales $\theta$ que permitan adaptación rápida a nuevas tareas con pocos gradientes:

$$\theta^* = \arg\min_{\theta} \sum_{\mathcal{T}_i \sim p(\mathcal{T})} \mathcal{L}_{\mathcal{T}_i}\left(f_{\theta'_i}\right)$$

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

## VI. DETECCIÓN DE SEÑALES CON REDES NEURONALES

La detección de señales es un componente crítico del receptor, responsable de estimar símbolos o bits transmitidos desde señales recibidas ruidosas [265]. En sistemas MIMO de alta dimensión, la detección óptima tiene complejidad exponencial, motivando aproximaciones subóptimas [266]. El DL ofrece detectores que balancean rendimiento y complejidad mediante aprendizaje de estructuras de detección efectivas [267].

### A. Problema de Detección en Sistemas MIMO

**Formulación**: Dado el modelo de señal:

$$\mathbf{y} = \mathbf{H}\mathbf{x} + \mathbf{n} \in \mathbb{C}^{N_r}$$

donde $\mathbf{x} \in \mathcal{X}^{N_t}$ con $\mathcal{X}$ siendo la constelación (e.g., $M$-QAM), detectar $\hat{\mathbf{x}}$ minimizando probabilidad de error [268].

**Maximum Likelihood (ML) Detection**:

$$\hat{\mathbf{x}}_{\text{ML}} = \arg\min_{\mathbf{x} \in \mathcal{X}^{N_t}} \|\mathbf{y} - \mathbf{H}\mathbf{x}\|^2$$

Complejidad: $\mathcal{O}(M^{N_t})$ evaluaciones, exponencial en número de antenas transmisoras [269].

**Linear Detectors**: Zero-forcing (ZF) y MMSE son lineales con complejidad $\mathcal{O}(N_t^3)$:

$$\hat{\mathbf{x}}_{\text{ZF}} = (\mathbf{H}^H\mathbf{H})^{-1}\mathbf{H}^H\mathbf{y}$$
$$\hat{\mathbf{x}}_{\text{MMSE}} = (\mathbf{H}^H\mathbf{H} + \sigma^2\mathbf{I})^{-1}\mathbf{H}^H\mathbf{y}$$

Rendimiento subóptimo especialmente en alta carga del sistema ($N_t \approx N_r$) [270].

### B. Redes Neuronales para Detección Directa

**DNN Detector**: Mapeo directo de señal recibida y CSI a símbolos detectados [273]:

$$\hat{\mathbf{x}} = f_{\text{DNN}}(\mathbf{y}, \mathbf{H}; \theta)$$

**Arquitectura**: 
1. **Input**: $[\text{Re}(\mathbf{y}); \text{Im}(\mathbf{y}); \text{vec}(\text{Re}(\mathbf{H})); \text{vec}(\text{Im}(\mathbf{H}))]$
2. **Hidden Layers**: Múltiples capas fully connected con activaciones ReLU
3. **Output**: Para detección de símbolos complejos, $2N_t$ salidas reales; para detección de bits, $N_t \log_2 M$ salidas con sigmoid

**Función de Pérdida**: Para detección de símbolos:

$$\mathcal{L}(\theta) = \mathbb{E}\left[\|\mathbf{x} - \hat{\mathbf{x}}\|^2\right]$$

Para detección de bits (soft-output):

$$\mathcal{L}(\theta) = -\mathbb{E}\left[\sum_{i=1}^{N_t\log_2 M}b_i\log\hat{b}_i + (1-b_i)\log(1-\hat{b}_i)\right]$$

### D. Detección con Atención y Transformers

**Attention-Based Detection**: Los mecanismos de atención permiten al detector enfocarse en componentes relevantes de la señal recibida [282]:

$$\mathbf{c}_i = \sum_{j=1}^{N_r}\alpha_{i,j}\mathbf{y}_j$$
$$\alpha_{i,j} = \frac{\exp(\text{score}(\mathbf{q}_i, \mathbf{k}_j))}{\sum_{j'}\exp(\text{score}(\mathbf{q}_i, \mathbf{k}_{j'}))}$$

donde $\mathbf{q}_i$ representa query para detectar símbolo $i$, y $\mathbf{k}_j$, $\mathbf{v}_j$ son proyecciones de señales recibidas [283].

**Transformer Detector**: Arquitectura completa basada en transformers para detección MIMO [284]:

1. **Embedding**: Proyectar señales recibidas a espacio de alta dimensión
2. **Multi-Head Self-Attention**: Capturar interdependencias entre símbolos transmitidos
3. **Feed-Forward Networks**: Procesamiento no lineal
4. **Output**: Probabilidades de símbolos o LLRs de bits

La complejidad es $\mathcal{O}(N_t^2)$ por capa, más eficiente que ML para $N_t$ moderado [285].

### E. Detección para Canales No-AWGN

**Fading Channels**: Para canales con desvanecimiento, incluir estadísticas de canal en entrenamiento [286]:

$$\mathbf{y} = \mathbf{h} \odot \mathbf{H}\mathbf{x} + \mathbf{n}, \quad \mathbf{h} \sim \text{Rayleigh/Rician}$$

El detector aprende robustez implícita a variaciones de desvanecimiento sin diversidad explícita [287].

**Impairments de Hardware**: Los detectores neuronales pueden compensar imperfecciones de hardware (IQ imbalance, non-linearities de PA, phase noise) aprendiendo desde datos reales [288]:

$$\mathbf{y} = \text{Impairment}(\mathbf{H}\mathbf{x}) + \mathbf{n}$$
$$\hat{\mathbf{x}} = f_{\text{DNN}}(\mathbf{y}; \theta)$$

El modelo aprende inversión de impairments implícitamente [289].

### F. Detección Multi-Usuario

**NOMA con DL**: En Non-Orthogonal Multiple Access, múltiples usuarios comparten recursos mediante multiplexación en dominio de potencia [290]:

$$\mathbf{y} = \sum_{k=1}^{K}\sqrt{p_k}\mathbf{h}_k s_k + \mathbf{n}$$

Un detector neural realiza cancelación de interferencia sucesiva aprendida [291]:

$$\{\hat{s}_1, \ldots, \hat{s}_K\} = f_{\text{DNN}}(\mathbf{y}, \{\mathbf{h}_k\}, \{p_k\}; \theta)$$

**Detección Multi-Celda**: En escenarios multi-celda con interferencia, detectores basados en graph neural networks modelan estructura de interferencia [292]:

Cada usuario es un nodo, aristas representan interferencia. El GNN propaga información para cancelación cooperativa:

$$\mathbf{h}_u^{(l+1)} = \text{UPDATE}\left(\mathbf{h}_u^{(l)}, \text{AGGREGATE}(\{\mathbf{h}_v^{(l)} : v \in \mathcal{N}(u)\})\right)$$

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

## VII. BEAMFORMING INTELIGENTE Y GESTIÓN DE HAZ

El beamforming es una técnica fundamental en sistemas MIMO y mmWave que concentra energía de transmisión en direcciones específicas, mejorando SNR y reduciendo interferencia [297]. En sistemas 6G con arrays masivos y entornos dinámicos, el beamforming adaptativo mediante IA ofrece ventajas sustanciales sobre métodos tradicionales [298].

### A. Fundamentos de Beamforming

**Array Response**: Para un array lineal uniforme (ULA) con $N$ elementos y espaciamiento $d$, el vector de steering para ángulo de llegada/salida $\theta$ es [299]:

$$\mathbf{a}(\theta) = \frac{1}{\sqrt{N}}\left[1, e^{j2\pi d\sin\theta/\lambda}, \ldots, e^{j2\pi(N-1)d\sin\theta/\lambda}\right]^T$$

**Beamforming de Transmisión**: La señal transmitida es:

$$\mathbf{x} = \mathbf{w}s$$

donde $\mathbf{w} \in \mathbb{C}^N$ es el vector de beamforming y $s$ es el símbolo de datos. El patrón de radiación es:

$$P(\theta) = |\mathbf{a}^H(\theta)\mathbf{w}|^2$$

**Diseño Clásico**: Para maximizar SNR en dirección objetivo $\theta_0$:

$$\mathbf{w}_{\text{MRT}} = \mathbf{a}(\theta_0)$$

Para nulificar interferencia en direcciones $\{\theta_i\}$:

$$\mathbf{w}_{\text{null}} \perp \text{span}\{\mathbf{a}(\theta_1), \ldots, \mathbf{a}(\theta_K)\}$$

Solución mediante optimización convexa o proyección [300].

### B. Deep Learning para Predicción de Beams

**Beam Prediction desde CSI**: En lugar de búsqueda exhaustiva sobre codebook de beams, predecir beam óptimo directamente [301]:

$$i^* = f_{\text{DNN}}(\mathbf{H}; \theta)$$

donde $i^*$ es el índice del beam en codebook $\{\mathbf{w}_1, \ldots, \mathbf{w}_{N_{\text{beam}}}\}$.

**Arquitectura CNN**: Explotar estructura espacial del CSI:

1. **Input**: Matriz de CSI $\mathbf{H} \in \mathbb{R}^{2N_r \times N_t}$ (real e imaginaria)
2. **Conv Layers**: Extraer características espaciales
$$\mathbf{F}^{(l)} = \text{ReLU}(\text{Conv2D}(\mathbf{F}^{(l-1)}))$$
3. **Global Pooling**: Agregar información espacial
4. **FC Layers**: Clasificación a índice de beam
5. **Output**: Probabilidades $\mathbf{p} = \text{softmax}(\mathbf{z}) \in [0,1]^{N_{\text{beam}}}$

**Función de Pérdida**: Cross-entropy para clasificación:

$$\mathcal{L}(\theta) = -\mathbb{E}\left[\sum_{i=1}^{N_{\text{beam}}}y_i\log p_i\right]$$

donde $y_i = 1$ si $i$ es el beam óptimo, 0 en otro caso [302].

### C. Beam Tracking en Movilidad

**Problema de Tracking**: En escenarios de alta movilidad (vehículos, drones), el beam óptimo cambia rápidamente. Tracking proactivo reduce latencia y overhead [303].

**RNN/LSTM para Beam Tracking**: Predecir beam futuro desde historial [304]:

$$i_{t+\Delta t}^* = f_{\text{LSTM}}(i_t^*, i_{t-1}^*, \ldots, i_{t-L}^*, \mathbf{features}_t; \theta)$$

donde $\mathbf{features}_t$ puede incluir posición, velocidad, SNR, etc.

**Seq2Seq con Atención**: Para predicción multi-step:

**Encoder**: Procesar secuencia histórica de beams y features
$$\mathbf{h}_t = \text{LSTM}_{\text{enc}}(\mathbf{x}_t, \mathbf{h}_{t-1})$$

**Decoder**: Generar secuencia de beams futuros con atención sobre historial
$$\mathbf{s}_t = \text{LSTM}_{\text{dec}}(\hat{i}_{t-1}, \mathbf{s}_{t-1}, \mathbf{c}_t)$$
$$\mathbf{c}_t = \sum_{i}\alpha_{t,i}\mathbf{h}_i$$

Esto permite anticipar cambios de beam varios pasos adelante [305].

### D. Beamforming Sin CSI Explícito

**Aprendizaje Directo desde Señales**: En lugar de estimar CSI y luego computar beamformers, aprender mapeo directo de mediciones de canal a beamformers [306]:

$$\mathbf{w} = f_{\text{DNN}}(\mathbf{Y}_{\text{pilot}}; \theta)$$

donde $\mathbf{Y}_{\text{pilot}}$ son señales piloto recibidas sin estimación de canal intermedia.

**End-to-End Learning**: Optimizar beamformers para maximizar métrica de sistema (tasa, SINR) directamente [307]:

$$\mathcal{L}(\theta) = -\mathbb{E}\left[R(\mathbf{w}(\theta))\right]$$

donde $R(\mathbf{w})$ es la tasa alcanzable con beamformer $\mathbf{w}$.

**Ventajas**: 
- Evita errores de estimación de canal
- Aprende compensación de impairments implícitamente
- Menor complejidad computacional [308]

### E. Multi-User Beamforming con DL

**Problema MU-MISO**: Con $K$ usuarios single-antenna, diseñar beamformers $\{\mathbf{w}_k\}$ para maximizar sum rate [309]:

$$\max_{\{\mathbf{w}_k\}} \sum_{k=1}^{K}\log_2\left(1 + \frac{|\mathbf{h}_k^H\mathbf{w}_k|^2}{\sum_{j\neq k}|\mathbf{h}_k^H\mathbf{w}_j|^2 + \sigma^2}\right)$$
$$\text{s.t. } \sum_{k=1}^{K}\|\mathbf{w}_k\|^2 \leq P_{\max}$$

Este problema es no convexo y difícil de resolver [310].

**DNN para MU Beamforming**: Aprender mapeo de canales multi-usuario a beamformers [311]:

$$\{\mathbf{w}_1, \ldots, \mathbf{w}_K\} = f_{\text{DNN}}(\mathbf{H}_1, \ldots, \mathbf{H}_K; \theta)$$

**Arquitectura**:
1. **Input**: Canales agregados $[\mathbf{H}_1; \ldots; \mathbf{H}_K]$
2. **Shared Layers**: Extraer características comunes
3. **User-Specific Branches**: Generar beamformer por usuario
4. **Normalization Layer**: Enforcing restricción de potencia

$$\mathbf{w}_k' = \sqrt{P_{\max}} \cdot \frac{\mathbf{w}_k}{\sqrt{\sum_{j}\|\mathbf{w}_j\|^2}}$$

**Unsupervised Learning**: Entrenar sin soluciones ground-truth maximizando sum rate [312]:

$$\mathcal{L}(\theta) = -\mathbb{E}\left[\sum_{k=1}^{K}\log_2(1 + \text{SINR}_k(\{\mathbf{w}_j(\theta)\}))\right]$$

### F. Beamforming Cooperativo con Graph Neural Networks

**Coordinated Beamforming**: En redes multi-celda, estaciones base coordinan beamforming para mitigar interferencia inter-celda [313].

**Modelado con Grafos**: Representar red como grafo:
- **Nodos**: Pares BS-usuario
- **Aristas**: Enlaces de interferencia

**GNN para Coord. Beamforming**: El GNN propaga información entre nodos para aprender beamformers que consideran interferencia de red [314]:

$$\mathbf{h}_v^{(0)} = [\mathbf{H}_v; \text{features}_v]$$
$$\mathbf{h}_v^{(l+1)} = \sigma\left(\mathbf{W}_{\text{self}}^{(l)}\mathbf{h}_v^{(l)} + \sum_{u \in \mathcal{N}(v)}\mathbf{W}_{\text{neigh}}^{(l)}\mathbf{h}_u^{(l)}\right)$$
$$\mathbf{w}_v = f_{\text{out}}(\mathbf{h}_v^{(L)})$$

El GNN aprende estrategias de coordinación que balancean ganancia local vs. interferencia a vecinos [315].

### G. Hybrid Analog-Digital Beamforming

**Arquitectura Híbrida**: Combinación de beamforming analógico (phase shifters) y digital (baseband) [316]:

$$\mathbf{W} = \mathbf{F}_{\text{RF}}\mathbf{F}_{\text{BB}}$$

donde $\mathbf{F}_{\text{RF}} \in \mathbb{C}^{N \times N_{\text{RF}}}$ con restricción $|[\mathbf{F}_{\text{RF}}]_{i,j}| = 1/\sqrt{N}$.

**DL para Diseño Híbrido**: Aprender descomposición óptima [317]:

$$\mathbf{F}_{\text{RF}}, \mathbf{F}_{\text{BB}} = f_{\text{DNN}}(\mathbf{H}; \theta)$$

**Enforcing Restricciones**:
1. **Analog**: Proyectar a manifold de fase constante
$$[\mathbf{F}_{\text{RF}}]_{i,j} = \frac{1}{\sqrt{N}}e^{j\angle[\mathbf{F}_{\text{RF}}']_{i,j}}$$

2. **Power**: Normalizar beamformer total
$$\mathbf{F}_{\text{BB}}' = \sqrt{\frac{P_{\max}}{\|\mathbf{F}_{\text{RF}}\mathbf{F}_{\text{BB}}\|_F^2}}\mathbf{F}_{\text{BB}}$$

**Alternating Optimization Unfolding**: Desplegar iteraciones de optimización alternante [318]:

$$\mathbf{F}_{\text{RF}}^{(t+1)} = f_{\text{RF}}^{(t)}(\mathbf{H}, \mathbf{F}_{\text{BB}}^{(t)}; \theta_{\text{RF}}^{(t)})$$
$$\mathbf{F}_{\text{BB}}^{(t+1)} = f_{\text{BB}}^{(t)}(\mathbf{H}, \mathbf{F}_{\text{RF}}^{(t+1)}; \theta_{\text{BB}}^{(t)})$$

### H. Beamforming para RIS-Assisted Systems

**Modelo RIS**: Con RIS de $N$ elementos, canal efectivo es [319]:

$$\mathbf{h}_{\text{eff}} = \mathbf{h}_d + \mathbf{H}_r\mathbf{\Theta}\mathbf{g}$$

donde $\mathbf{\Theta} = \text{diag}(e^{j\theta_1}, \ldots, e^{j\theta_N})$ es configuración de fase RIS.

**Optimización Conjunta**: Diseñar beamformer BS $\mathbf{w}$ y fases RIS $\{\theta_n\}$ conjuntamente [320]:

$$\max_{\mathbf{w},\{\theta_n\}} |\mathbf{h}_{\text{eff}}^H\mathbf{w}|^2$$
$$\text{s.t. } \|\mathbf{w}\|^2 \leq P, \quad \theta_n \in [0, 2\pi)$$

**DNN para RIS Beamforming**: Aprender configuración conjunta [321]:

$$\mathbf{w}, \{\theta_1, \ldots, \theta_N\} = f_{\text{DNN}}(\mathbf{h}_d, \mathbf{H}_r, \mathbf{g}; \theta)$$

**RL sin CSI Perfecto**: Cuando CSI de múltiples saltos es difícil de obtener, usar RL para optimizar basado en métricas [322]:

- **Estado**: SNR recibido, configuración previa
- **Acción**: Ajuste de fases RIS $\Delta\theta_n$
- **Recompensa**: Mejora en SNR

Agentes como DDPG aprenden políticas de configuración óptimas sin modelo explícito del canal [323].

## VIII. GESTIÓN DE RECURSOS ESPECTRALES MEDIANTE APRENDIZAJE POR REFUERZO

La asignación eficiente de recursos espectrales (potencia, ancho de banda, tiempo, bloques de recursos) es crucial para maximizar eficiencia espectral y satisfacer requisitos heterogéneos de QoS en sistemas 6G [326]. La naturaleza dinámica y combinatorial del problema motiva uso de aprendizaje por refuerzo profundo (DRL) [327].

### A. Formulación como MDP

**Proceso de Decisión de Markov**: El problema de asignación de recursos se modela como tupla $(\mathcal{S}, \mathcal{A}, \mathcal{P}, \mathcal{R}, \gamma)$ [328]:

- **Estados** $\mathcal{S}$: CSI, demanda de tráfico, buffer states, QoS requirements
$$s_t = [\mathbf{H}_t, \mathbf{Q}_t, \mathbf{B}_t, \mathbf{QoS}_t]$$

- **Acciones** $\mathcal{A}$: Asignación de recursos (potencia, subcanales, MCS)
$$a_t = [\mathbf{P}_t, \mathbf{SC}_t, \mathbf{MCS}_t]$$

- **Transiciones** $\mathcal{P}$: $s_{t+1} \sim P(\cdot|s_t, a_t)$ determinado por dinámica de canal y arribo de tráfico

- **Recompensa** $\mathcal{R}$: Función de utilidad del sistema
$$R(s_t, a_t) = \alpha \cdot \text{Throughput} - \beta \cdot \text{Delay} - \gamma \cdot \text{Power}$$

- **Discount factor** $\gamma \in [0,1)$: Pondera recompensas futuras [329]

**Objetivo**: Aprender política óptima $\pi^*: \mathcal{S} \to \mathcal{A}$ que maximiza retorno esperado:

$$J(\pi) = \mathbb{E}_{\pi}\left[\sum_{t=0}^{\infty}\gamma^t R(s_t, a_t)\right]$$

### B. Deep Q-Networks (DQN) para Asignación de Recursos

**Q-Learning**: Aprender función de valor acción-estado óptima [330]:

$$Q^*(s,a) = \mathbb{E}\left[R(s,a) + \gamma\max_{a'}Q^*(s',a')\right]$$

**DQN**: Aproximar $Q^*(s,a)$ mediante red neuronal profunda [331]:

$$Q(s,a;\theta) \approx Q^*(s,a)$$

**Arquitectura**:
1. **Input**: Representación de estado $s$
2. **Hidden Layers**: DNNs con ReLU
3. **Output**: Q-valores para cada acción $[Q(s,a_1), \ldots, Q(s,a_{|\mathcal{A}|})]$

**Entrenamiento**: Minimizar Bellman error mediante experience replay:

$$\mathcal{L}(\theta) = \mathbb{E}_{(s,a,r,s')\sim\mathcal{D}}\left[\left(r + \gamma\max_{a'}Q(s',a';\theta^-) - Q(s,a;\theta)\right)^2\right]$$

donde $\mathcal{D}$ es replay buffer y $\theta^-$ son parámetros de target network actualizados periódicamente [332].

**Double DQN**: Reduce sobrestimación de Q-valores usando dos redes [333]:

$$y = r + \gamma Q(s', \arg\max_{a'}Q(s',a';\theta); \theta^-)$$

**Dueling DQN**: Descompone Q-función en valor de estado y ventajas de acción [334]:

$$Q(s,a;\theta) = V(s;\theta_V) + A(s,a;\theta_A) - \frac{1}{|\mathcal{A}|}\sum_{a'}A(s,a';\theta_A)$$

### C. Policy Gradient y Actor-Critic

**Limitación de DQN**: Requiere espacio de acciones discreto y finito. Muchos problemas de asignación tienen acciones continuas (niveles de potencia) o espacios combinatorialmente grandes [335].

**Policy Gradient**: Parametrizar política directamente y optimizar mediante gradiente [336]:

$$\pi(a|s;\theta) = P(a_t=a | s_t=s)$$

**REINFORCE**: Gradiente del objetivo:

$$\nabla_{\theta}J(\theta) = \mathbb{E}_{\pi_{\theta}}\left[\nabla_{\theta}\log\pi(a|s;\theta)G_t\right]$$

donde $G_t = \sum_{k=0}^{\infty}\gamma^k R_{t+k}$ es el retorno [337].

**Actor-Critic**: Combina policy gradient (actor) con función de valor (critic) para reducir varianza [338]:

**Actor**: Actualizar política en dirección sugerida por critic
$$\theta \leftarrow \theta + \alpha\nabla_{\theta}\log\pi(a|s;\theta)A(s,a;\phi)$$

**Critic**: Estimar ventaja $A(s,a) = Q(s,a) - V(s)$
$$\phi \leftarrow \phi - \beta\nabla_{\phi}(R + \gamma V(s';\phi) - V(s;\phi))^2$$

**A3C (Asynchronous Advantage Actor-Critic)**: Paraleliza entrenamiento con múltiples agentes explorando simultáneamente [339].

### D. Proximal Policy Optimization (PPO)

PPO es un algoritmo de policy gradient que limita actualizaciones de política para evitar cambios drásticos que degradan rendimiento [340]:

$$\mathcal{L}^{\text{CLIP}}(\theta) = \mathbb{E}\left[\min\left(r_t(\theta)A_t, \text{clip}(r_t(\theta), 1-\epsilon, 1+\epsilon)A_t\right)\right]$$

donde:
$$r_t(\theta) = \frac{\pi(a_t|s_t;\theta)}{\pi(a_t|s_t;\theta_{\text{old}})}$$

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

$$\nabla_{\theta_i}J(\theta_i) = \mathbb{E}\left[\nabla_{\theta_i}\pi_i(s_i)\nabla_{a_i}Q_i(\mathbf{s},\mathbf{a})|_{a_i=\pi_i(s_i)}\right]$$

**QMIX**: Para escenarios cooperativos, factoriza Q-función global mediante monotonicity constraint [348]:

$$Q_{\text{tot}}(\mathbf{s},\mathbf{a}) = f(Q_1(s_1,a_1), \ldots, Q_n(s_n,a_n))$$

donde $f$ es una red de mezcla que satisface:

$$\frac{\partial Q_{\text{tot}}}{\partial Q_i} \geq 0, \quad \forall i$$

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

$$a_t = \text{RNN}(s_t, a_{t-1}, r_{t-1}, h_{t-1})$$

La RNN aprende dinámicas de aprendizaje en su estado oculto.

**MAML para RL**: Buscar parámetros iniciales de política que permitan adaptación rápida [365]:

$$\theta^* = \arg\min_{\theta}\sum_{\mathcal{T}_i}J_{\mathcal{T}_i}(\theta - \alpha\nabla_{\theta}J_{\mathcal{T}_i}(\theta))$$

## IX. MODULACIÓN ADAPTATIVA Y FORMAS DE ONDA INTELIGENTES

La selección de esquemas de modulación y forma de onda óptimos basándose en condiciones instantáneas del canal es crítica para maximizar eficiencia espectral y confiabilidad [372]. El DL permite adaptación más granular y predicción proactiva superando esquemas tradicionales [373].

### A. Link Adaptation Clásica

**Adaptive Modulation and Coding (AMC)**: Ajustar MCS basándose en CSI o feedback [374]:

$$\text{MCS} = f(\text{SINR})$$

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

$$\text{MCS}^* = f_{\text{DNN}}(\mathbf{h}, \text{SNR}, \text{features}; \theta)$$

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

$$\mathcal{L}(\theta) = -\mathbb{E}\left[\sum_{\text{MCS}} w_{\text{MCS}} \cdot y_{\text{MCS}}\log p_{\text{MCS}}\right]$$

donde $w_{\text{MCS}} = R_{\text{MCS}}$ pondera por tasa del MCS, incentivando esquemas de mayor tasa cuando es seguro.

**Resultados**: Ganancias de 10-20% en throughput comparado con AMC tradicional en canales variables [378].

### C. Predicción Proactiva de MCS

**Desafío**: Latencia de feedback causa mismatch entre CSI y condiciones actuales, especialmente en alta movilidad [379].

**LSTM para Predicción**: Predecir MCS óptimo pasos adelante [380]:

$$\text{MCS}_{t+\Delta t}^* = f_{\text{LSTM}}(\text{MCS}_t, \text{SINR}_t, \ldots, \text{MCS}_{t-L}, \text{SINR}_{t-L}; \theta)$$

**Seq2Seq para Scheduling**: Predecir secuencia de MCS para ventana futura, permitiendo scheduling proactivo [381]:

$$[\text{MCS}_{t+1}, \ldots, \text{MCS}_{t+H}] = f_{\text{Seq2Seq}}(\text{history}; \theta)$$

**Impacto**: Reduce latencia efectiva de feedback, permite pre-codificación optimizada, mejora throughput en 15-25% @ 120 km/h [382].

### D. Learned Modulation: Constelaciones Neurales

**Más allá de QAM**: Las constelaciones convencionales (M-PSK, M-QAM) se diseñaron para canales AWGN. DL permite aprender constelaciones optimizadas para canales específicos [383].

**Autocodificador de Constelación**: Aprender mapeo de bits a símbolos y viceversa [384]:

$$\text{Mapper: } \mathbf{s} = f_{\text{map}}(\mathbf{b}; \theta_{\text{map}}) \in \mathbb{C}$$
$$\text{Channel: } \mathbf{y} = \mathcal{C}(\mathbf{s})$$
$$\text{Demapper: } \hat{\mathbf{b}} = f_{\text{demap}}(\mathbf{y}; \theta_{\text{demap}})$$

**Restricciones**:
1. **Potencia promedio**: $\mathbb{E}[|\mathbf{s}|^2] = 1$
2. **Distinción**: Símbolos diferentes deben ser distinguibles

**Entrenamiento End-to-End**:

$$\min_{\theta_{\text{map}}, \theta_{\text{demap}}} \mathbb{E}\left[-\sum_i b_i\log\hat{b}_i - (1-b_i)\log(1-\hat{b}_i)\right]$$

**Resultados**: Para canales con fading severo, constelaciones aprendidas logran 1-2 dB de ganancia sobre QAM [385].

**Interpretación**: Las constelaciones aprendidas a menudo exhiben:
- Distribución no uniforme adaptada a estadísticas de canal
- Robustez aumentada en regiones de alta probabilidad de error
- Estructura geométrica que explota diversidad [386]

### E. Formas de Onda Inteligentes

**Más allá de OFDM**: OFDM es dominante por su simplicidad y robustez a dispersión multi-trayectoria, pero tiene limitaciones (PAPR alto, sensibilidad a CFO, overhead de CP) [387].

**DL para Diseño de Forma de Onda**: Aprender señalización temporal completa [388]:

$$\mathbf{s}(t) = f_{\text{TX}}(\mathbf{b}; \theta_{\text{TX}})$$
$$\hat{\mathbf{b}} = f_{\text{RX}}(\mathbf{y}(t); \theta_{\text{RX}})$$

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

$$\text{PAPR} = \frac{\max_n |s[n]|^2}{\mathbb{E}[|s[n]|^2]}$$

**Técnicas Clásicas**:
- Clipping & Filtering: Degradación de BER
- Selective Mapping (SLM): Overhead de side information
- Partial Transmit Sequence (PTS): Alta complejidad [392]

**DNN para PAPR Reduction**: Aprender precodificador que reduce PAPR manteniendo BER [393]:

$$\mathbf{x}' = f_{\text{DNN}}(\mathbf{x}; \theta)$$

Función objetivo multi-objetivo:

$$\mathcal{L}(\theta) = \alpha \cdot \text{BER}(\mathbf{x}') + \beta \cdot \text{PAPR}(\mathbf{x}')$$

**Resultados**: Reducción de PAPR de 2-3 dB con degradación de BER <0.5 dB [394].

**Autocodificador con Nonlinearity Awareness**: Entrenar con modelo de amplificador de potencia no lineal en el loop [395]:

$$\mathbf{s}' = \text{PA}(\mathbf{s}) = \alpha \mathbf{s} + \alpha_3 |\mathbf{s}|^2\mathbf{s} + \ldots$$

El encoder aprende pre-distorsión implícita.

### G. Waveform para Coexistencia Espectral

**Escenario**: Múltiples servicios (eMBB, URLLC, mMTC) coexisten, requiriendo formas de onda con diferentes características [396].

**Multi-Numerology**: Usar diferentes espaciamientos de subportadora [397]:
- eMBB: 15 kHz (alta eficiencia espectral)
- URLLC: 60 kHz (baja latencia)
- mMTC: 3.75 kHz (cobertura extendida)

**Desafío**: Interferencia inter-numerología

**DL para Cancelación de Interferencia**: Entrenar receptores que suprimen interferencia de numerologías vecinas [398]:

$$\hat{\mathbf{b}}_{\text{eMBB}} = f_{\text{RX}}(\mathbf{y}, \text{info}_{\text{URLLC}}; \theta)$$

donde información sobre señalización URLLC ayuda a cancelar su interferencia.

**Filtered OFDM con Filtros Aprendidos**: Diseñar filtros por subportadora mediante DNNs que minimizan fuga espectral [399]:

$$\mathbf{f} = f_{\text{DNN}}(\text{numerology}, \text{BW}; \theta)$$

Filtros aprendidos logran 10-15 dB mejor ACLR (Adjacent Channel Leakage Ratio) que ventanas clásicas [400].

## X. COMUNICACIONES SEMÁNTICAS Y ORIENTADAS A TAREAS

Un cambio paradigmático emergente es la comunicación semántica, donde el objetivo es transmitir significado (semántica) en lugar de bits exactos, potencialmente logrando eficiencias exponenciales [403], [404]. El DL es habilitador clave al extraer y codificar representaciones semánticas.

### A. Fundamentos de Comunicación Semántica

**Arquitectura de Shannon**: Comunicación tradicional separa fuente-canal:

$$\text{Source} \to \text{Source Coding} \to \text{Channel Coding} \to \text{Channel} \to \text{Decoding}$$

Objetivo: Reconstruir bits exactos con probabilidad de error arbitrariamente pequeña [405].

**Limitación**: Para aplicaciones como visión por máquina, traducción, o control, reconstrucción exacta de bits puede ser innecesaria si se preserva tarea objetivo [406].

**Arquitectura de Weaver**: Extender con niveles de semántica y efectividad [407]:

- **Nivel A (Técnico)**: ¿Qué tan precisos son los símbolos transmitidos? (Shannon)
- **Nivel B (Semántico)**: ¿Qué tan precisamente transmiten el significado deseado?
- **Nivel C (Efectividad)**: ¿Qué tan efectivamente afecta la conducta deseada?

**Comunicación Semántica**: Optimizar niveles B y C directamente [408].

### B. Deep Learning para Extracción Semántica

**Representaciones Latentes**: Usar encoders profundos para extraer características semánticas compactas [409]:

$$\mathbf{z} = f_{\text{semantic}}(\mathbf{x}; \theta_{\text{sem}})$$

donde $\mathbf{x}$ es dato fuente (imagen, texto, señal) y $\mathbf{z} \in \mathbb{R}^d$ con $d \ll \dim(\mathbf{x})$ es representación semántica.

**Autoencoders Variational (VAE)**: Aprender distribución sobre representaciones [410]:

$$q_{\phi}(\mathbf{z}|\mathbf{x}) = \mathcal{N}(\mathbf{z}; \boldsymbol{\mu}(\mathbf{x}), \boldsymbol{\sigma}^2(\mathbf{x})\mathbf{I})$$
$$p_{\theta}(\mathbf{x}|\mathbf{z})$$

Objetivo ELBO:

$$\mathcal{L} = \mathbb{E}_{q_{\phi}(\mathbf{z}|\mathbf{x})}[\log p_{\theta}(\mathbf{x}|\mathbf{z})] - D_{KL}(q_{\phi}(\mathbf{z}|\mathbf{x})\|p(\mathbf{z}))$$

Representaciones $\mathbf{z}$ capturan factores semánticos de variación [411].

**Contrastive Learning**: Aprender representaciones que agrupan semántica similar [412]:

$$\mathcal{L}_{\text{contrastive}} = -\log\frac{\exp(\text{sim}(\mathbf{z}_i, \mathbf{z}_j)/\tau)}{\sum_{k}\exp(\text{sim}(\mathbf{z}_i, \mathbf{z}_k)/\tau)}$$

donde $(i,j)$ son pares positivos (semánticamente similares) y $k$ incluye negativos.

### C. Comunicación Semántica End-to-End

**Arquitectura**: Transmitir representaciones semánticas en lugar de datos brutos [413]:

1. **Semantic Encoder**: $\mathbf{z} = f_{\text{sem}}(\mathbf{x}; \theta_{\text{sem}})$
2. **Channel Encoder**: $\mathbf{s} = f_{\text{ch}}(\mathbf{z}; \theta_{\text{ch}})$
3. **Channel**: $\mathbf{y} = \mathcal{C}(\mathbf{s})$
4. **Channel Decoder**: $\hat{\mathbf{z}} = f_{\text{ch-dec}}(\mathbf{y}; \theta_{\text{ch-dec}})$
5. **Semantic Decoder**: $\hat{\mathbf{x}} = f_{\text{sem-dec}}(\hat{\mathbf{z}}; \theta_{\text{sem-dec}})$

**Función de Pérdida**: Métrica orientada a tarea en lugar de MSE [414]:

$$\mathcal{L} = \mathcal{L}_{\text{task}}(\mathbf{x}, \hat{\mathbf{x}}) + \lambda R(\mathbf{s})$$

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
$$\mathbf{z}^* = \arg\min_{\mathbf{z}} \|\mathbf{x} - G(\mathbf{z})\|^2$$

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

$$\pi_{\text{comm}}(\mathbf{z}|\mathbf{x}, \text{task}) = \text{qué información transmitir}$$
$$\pi_{\text{action}}(a|\hat{\mathbf{z}}) = \text{acción basada en información recibida}$$

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

## XI. DESAFÍOS DE IMPLEMENTACIÓN Y CONSIDERACIONES PRÁCTICAS

Si bien el DL promete mejoras sustanciales en la capa física, el deployment práctico enfrenta desafíos significativos en complejidad computacional, generalización, robustez, y estandarización [436].

### A. Complejidad Computacional y Latencia

**Desafío**: Los modelos de DL profundos requieren millones de operaciones por inferencia, potencialmente excediendo presupuestos de latencia/energía [437].

**Análisis de Complejidad**: Para DNN con $L$ capas fully-connected de tamaño $N_h$:

$$\text{FLOPs} = \sum_{l=1}^{L} N_h^{(l)} \times N_h^{(l-1)}$$

Para CNN con $C$ canales, kernels $K \times K$, y resolución espacial $H \times W$:

$$\text{FLOPs} = L \times C_{\text{in}} \times C_{\text{out}} \times K^2 \times H \times W$$

**Ejemplo**: Para detector MIMO con DNN de 5 capas, 512 neuronas, inferencia requiere:

$$\text{FLOPs} \approx 5 \times 512^2 \approx 1.3 \times 10^6$$

En CPU general (10 GFLOPS), esto toma $\approx 130$ μs. Para sistemas con TTI (Transmission Time Interval) de 1 ms, esto es manejable, pero para URLLC con latencia <1 ms, se requiere aceleración [438].

**Soluciones**:

**1) Cuantización**: Reducir precisión de pesos y activaciones de FP32 a INT8 o INT4 [439]:

$$\text{Quantized: } w_q = \text{round}\left(\frac{w}{s}\right) \cdot s$$

donde $s$ es factor de escala. Cuantización INT8 reduce memoria $4\times$ y acelera inferencia $2\times-4\times$ con degradación típica <1 dB [440].

**Quantization-Aware Training**: Simular cuantización durante entrenamiento:

$$\tilde{w} = w + \text{stop\_gradient}(\text{quantize}(w) - w)$$

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

$$\mathcal{L}_{\text{distill}} = \alpha \mathcal{L}_{\text{task}} + (1-\alpha)\mathcal{L}_{\text{KD}}$$

donde:

$$\mathcal{L}_{\text{KD}} = \text{KL}\left(p_{\text{teacher}}(y|x) \| p_{\text{student}}(y|x)\right)$$

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

$$\min_{F}\max_{D} \mathbb{E}_{x \sim \mathcal{D}_s}[\log D(F(x))] + \mathbb{E}_{x \sim \mathcal{D}_t}[\log(1-D(F(x)))]$$

Features $F(x)$ se vuelven invariantes a dominio.

**3) Meta-Learning**: Aprender a aprender, facilitando adaptación rápida [463]:

MAML para comunicaciones permite adaptar a nuevas condiciones de canal con pocos ejemplos:

$$\theta^* = \arg\min_{\theta} \sum_{\mathcal{T}_i}\mathcal{L}_{\mathcal{T}_i}(\theta - \alpha\nabla_{\theta}\mathcal{L}_{\mathcal{T}_i}(\theta))$$

**4) Ensemble Methods**: Combinar múltiples modelos para robustez [464]:

$$\hat{y} = \frac{1}{M}\sum_{m=1}^{M}f_m(x;\theta_m)$$

Ensembles son más robustos a corrupciones y domain shift [465].

**5) Uncertainty Quantification**: Estimar confianza de predicciones [466]:

**MC Dropout**: Usar dropout en inferencia, múltiples forwards:

$$p(y|x) \approx \frac{1}{T}\sum_{t=1}^{T}p(y|x,\theta_t)$$

donde $\theta_t$ son pesos con dropout estocástico. Varianza de predicciones indica incertidumbre [467].

**Bayesian Neural Networks**: Mantener distribuciones sobre pesos:

$$p(\theta|\mathcal{D}) \propto p(\mathcal{D}|\theta)p(\theta)$$

Permite cuantificar uncertainty epistémica [468].

### D. Adversarial Robustness

**Vulnerabilidad**: DNNs son susceptibles a perturbaciones adversariales imperceptibles [469]:

$$\mathbf{x}_{\text{adv}} = \mathbf{x} + \epsilon \cdot \text{sign}(\nabla_{\mathbf{x}}\mathcal{L}(f(\mathbf{x}),y))$$

En comunicaciones, un atacante podría inyectar perturbaciones que causen detección/decodificación errónea [470].

**Ataques Específicos**:

**1) Adversarial Jamming**: Jamming optimizado para maximizar error de DNN detector [471]:

$$\mathbf{j}^* = \arg\max_{\|\mathbf{j}\|_2 \leq P_j} \mathcal{L}_{\text{det}}(f_{\text{DNN}}(\mathbf{y} + \mathbf{j}))$$

Mucho más efectivo que ruido gaussiano de misma potencia.

**2) Model Evasion**: Atacante con conocimiento de modelo genera señales que evaden detección [472].

**3) Backdoor Attacks**: Envenenar datos de entrenamiento para insertar comportamientos maliciosos [473]:

- Entrenar con muestras que contienen trigger pattern
- Modelo funciona normalmente, excepto cuando trigger está presente

**Defensas**:

**1) Adversarial Training**: Entrenar contra ejemplos adversariales [474]:

$$\min_{\theta} \mathbb{E}_{(\mathbf{x},y)}\left[\max_{\|\delta\| \leq \epsilon}\mathcal{L}(f(\mathbf{x}+\delta;\theta),y)\right]$$

Robustifica modelo pero puede reducir precisión en datos limpios.

**2) Certified Defense**: Garantizar robustez en región acotada [475]:

Randomized Smoothing: Usar modelo suavizado por ruido:

$$g(\mathbf{x}) = \mathbb{E}_{\boldsymbol{\epsilon}\sim\mathcal{N}(0,\sigma^2\mathbf{I})}[f(\mathbf{x}+\boldsymbol{\epsilon})]$$

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

$$\text{Attack: } f_{\text{attack}}(\mathbf{x}, f(\mathbf{x};\theta)) \to \{\text{member}, \text{non-member}\}$$

**2) Model Inversion**: Atacante reconstruye datos de entrenamiento desde modelo [490]:

$$\mathbf{x}^* = \arg\max_{\mathbf{x}} p(y|\mathbf{x};\theta)$$

**3) Data Poisoning**: Atacante contamina dataset de entrenamiento [491].

**Soluciones**:

**1) Differential Privacy**: Garantizar que inclusión/exclusión de muestra individual no afecta significativamente salidas [492]:

**DP-SGD**: Añadir ruido a gradientes durante entrenamiento:

$$\tilde{g}_t = \frac{1}{B}\sum_{i}\text{clip}(\nabla_{\theta}\mathcal{L}(\mathbf{x}_i;\theta), C) + \mathcal{N}(0, \sigma^2 C^2 \mathbf{I})$$

donde $C$ es threshold de clipping y $\sigma$ controla noise scale [493].

Privacy budget $\epsilon$: Menor $\epsilon$ = mayor privacidad (típicamente $\epsilon \in [1,10]$)

Trade-off: DP reduce precisión de modelo (típicamente 2-5%) [494].

**2) Federated Learning**: Entrenar modelo distribuido sin compartir datos brutos [495]:

1. **Server**: Distribuir modelo inicial $\theta_0$
2. **Clients**: Entrenar localmente en datos privados
$$\theta_i^{(t+1)} = \theta_i^{(t)} - \eta\nabla\mathcal{L}_i(\theta_i^{(t)})$$
3. **Server**: Agregar actualizaciones
$$\theta^{(t+1)} = \sum_{i}\frac{n_i}{n}\theta_i^{(t+1)}$$
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

$$\text{Enc}(x_1) \oplus \text{Enc}(x_2) = \text{Enc}(x_1 + x_2)$$
$$\text{Enc}(x_1) \otimes \text{Enc}(x_2) = \text{Enc}(x_1 \cdot x_2)$$

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

$$\phi_i = \sum_{S \subseteq N \setminus \{i\}}\frac{|S|!(|N|-|S|-1)!}{|N|!}[f(S \cup \{i\}) - f(S)]$$

Indica contribución marginal de feature $i$ [504].

**LIME (Local Interpretable Model-agnostic Explanations)**: Aproximar localmente con modelo lineal interpretable:

$$\xi(x) = \arg\min_{g \in G}\mathcal{L}(f,g,\pi_x) + \Omega(g)$$

donde $g$ es modelo interpretable, $\pi_x$ es proximidad, $\Omega$ es complejidad [505].

**2) Attention Visualization**: Para modelos con attention, visualizar pesos aprendidos [506]:

$$\alpha_{i,j} = \frac{\exp(e_{i,j})}{\sum_k \exp(e_{i,k})}$$

Muestra qué partes de entrada son importantes para salida.

**3) Activation Maximization**: Sintetizar inputs que maximizan activación de neuronas [507]:

$$\mathbf{x}^* = \arg\max_{\mathbf{x}} \mathbf{h}_l[\mathbf{x}] - \lambda\|\mathbf{x}\|^2$$

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

$$\text{Efficiency} = \frac{\text{Accuracy}}{\text{Energy} \times \text{CO}_2}$$

Incentivar desarrollo de modelos eficientes.

**6) Edge Computing**: Reducir transmisión de datos a cloud disminuye energía de comunicación [516].

---

## XII. DIRECCIONES FUTURAS Y CONCLUSIONES  ### A. Tendencias Emergentes  **1) Foundation Models para Comunicaciones Inalámbricas**: Inspirados por éxito en NLP (GPT, BERT), desarrollar modelos de propósito general pre-entrenados en grandes corpus de datos de comunicaciones,:  **Concepto**: - Pre-entrenar en datasets diversos (múltiples canales, frecuencias, configuraciones) - Fine-tune para tareas específicas (detección, estimación, beamforming) - Transfer learning facilita adaptación con datos limitados  **Arquitectura Transformer Universal**: Usar transformers como backbone universal:  $$\mathbf{h} = \text{Transformer}(\mathbf{x}_{\text{pilot}}, \mathbf{x}_{\text{data}}, \text{context})$$  Contexto incluye metadatos (frecuencia, configuración, QoS), permitiendo modelo único para múltiples escenarios.  **Ventajas**: - Reduce costo de desarrollo de modelos especializados - Mejora generalización mediante pre-entrenamiento en datos diversos - Facilita estandarización (architecture única con diferentes pesos)  **2) Self-Supervised Learning**: Reducir dependencia de datos etiquetados costosos:  **Contrastive Learning**: Aprender representaciones que distinguen muestras:  $$\mathcal{L} = -\log\frac{\exp(\text{sim}(\mathbf{z}_i,\mathbf{z}^+)/\tau)}{\sum_j\exp(\text{sim}(\mathbf{z}_i,\mathbf{z}_j)/\tau)}$$  donde $\mathbf{z}^+$ es aumentación de $\mathbf{z}_i$.  **Masked Autoencoders**: Predecir partes enmascaradas de señales:  - Mask porción de símbolos/subportadoras recibidas - Entrenar red para reconstruir partes enmascaradas - Representaciones aprendidas útiles para downstream tasks  **3) Neural-Enhanced Physical Layer Security**: Usar DL para seguridad de capa física:  **Physical Layer Authentication**: Identificar dispositivos mediante características únicas de canal/hardware:  $$\text{Device ID} = f_{\text{DNN}}(\mathbf{h}, \text{RF fingerprint}; \theta)$$  DNNs detectan sutilezas en señales que identifican dispositivo transmisor.  **Secure Transmission con GAN**: Generar señales que son difíciles de interceptar:  - Generator: Crea señales que maximize secrecy rate - Discriminator: Actúa como eavesdropper - Entrenamiento adversarial maximiza información a receptor legítimo minimizando a eavesdropper  **4) Quantum-Enhanced Machine Learning para 6G**: Explorar algoritmos cuánticos para optimización:  **Quantum Neural Networks**: Usar computación cuántica para ciertos cálculos:  $$|\psi\rangle = U(\theta)|\psi_0\rangle$$  donde $U(\theta)$ son puertas cuánticas parametrizadas.  **Aplicaciones potenciales**: - Optimización combinatorial (resource allocation) - Sampling de distribuciones complejas (channel generation) - Speedup cuántico para ciertos problemas  **Desafíos**: Hardware cuántico aún en etapa temprana, ruido, escalabilidad limitada.  **5) Neuromorphic Computing**: Hardware inspirado en el cerebro para procesamiento eficiente:  **Spiking Neural Networks**: Usar spikes temporales en lugar de activaciones continuas:  $$\frac{dv}{dt} = -\frac{v}{\tau} + I(t)$$  Si $v(t) > \theta$, neurona emite spike y resetea.  **Ventajas**: - Eficiencia energética extrema (event-driven) - Latencia ultra-baja - Procesamiento temporal natural  **Aplicaciones en comunicaciones**: - Detección de señales sparse - Procesamiento en tiempo real en edge devices  **6) Continual Learning y Lifelong Learning**: Modelos que aprenden continuamente sin olvidar:  **Elastic Weight Consolidation**: Penalizar cambios en pesos importantes para tareas previas:  $$\mathcal{L}(\theta) = \mathcal{L}_{\text{new}}(\theta) + \sum_i \frac{\lambda}{2}F_i(\theta_i - \theta_i^*)^2$$  donde $F_i$ es importancia del peso $i$ para tareas previas (Fisher information).  **Progressive Neural Networks**: Expandir arquitectura para nuevas tareas manteniendo pesos previos congelados.  **Aplicaciones**: - Adaptar a nuevos escenarios sin re-entrenar desde cero - Sistemas que mejoran continuamente con deployment  ### B. Integración con Tecnologías Emergentes  **1) IA Nativa en Arquitecturas O-RAN**: Integración profunda de ML en RAN abierto:  **Near-RT RIC (Real-Time RIC)**: ML con latencia 10-1000 ms: - Scheduling inteligente - Mobility management - Interference management  **Non-RT RIC**: ML con latencia >1 segundo: - Optimización de políticas - Transfer learning - Model training  **xApps y rApps**: Aplicaciones de terceros que usan ML: - Marketplace de algoritmos de IA - Competencia e innovación en optimización de RAN  **2) Integración con Comunicaciones Terahertz**: IA para superar desafíos de THz:  **Beam Management**: Arrays masivos en THz requieren beam management eficiente: - DL para predicción ultra-rápida de beams - Tracking en movilidad extrema  **Compensación de Impairments**: THz sufre phase noise severo, non-linearities: - DNNs para ecualización y compensación adaptativa  **Channel Modeling**: Modelado de canales THz complejos mediante GANs.  **3) IA para Comunicaciones Underwater y Satélite**: Extender técnicas a entornos extremos:  **Underwater Acoustic Communications**: Canales con delay spread masivo, Doppler severo: - RNN para ecualización de canales underwater - Adaptive modulation para condiciones cambiantes  **Satellite Communications**: LEO mega-constellations con handoffs frecuentes: - DRL para resource allocation en redes satelitales - Predicción de tráfico y beam steering  **4) Integración con Computación Cuántica**: Comunicaciones cuánticas con IA clásica:  **Quantum Key Distribution**: Optimizar protocolos con ML: - Detección de eavesdropping mediante anomaly detection - Optimización de rate vs. security  **Hybrid Quantum-Classical Networks**: Ruteo y resource allocation en redes híbridas.  ### C. Investigación Abierta y Desafíos Fundamentales  **1) Límites Teóricos de IA en Comunicaciones**: Establecer límites fundamentales:  **Pregunta**: ¿Cuál es la capacidad alcanzable por sistemas de comunicación end-to-end aprendidos?  **Conjeturas**: - Con modelo de canal perfecto, IA puede aproximar capacidad de Shannon arbitrariamente - Con incertidumbre de canal, ¿puede IA superar esquemas robustos tradicionales?  **Sample Complexity**: ¿Cuántos datos se requieren para aprender comunicación óptima?  $$N_{\text{samples}} = \Theta(?)$$  Bounds teóricos ayudarían a guiar diseño práctico.  **2) Unificación de Model-Based y Data-Driven Approaches**: Combinar conocimiento físico con aprendizaje:  **Physics-Informed Neural Networks**: Incorporar ecuaciones físicas en pérdida:  $$\mathcal{L} = \mathcal{L}_{\text{data}} + \lambda\mathcal{L}_{\text{physics}}$$  donde $\mathcal{L}_{\text{physics}}$ penaliza violaciones de leyes físicas (conservación de energía, reciprocidad de canal, etc.).  **Neural ODEs para Canal Dynamics**: Modelar evolución temporal de canal con ecuaciones diferenciales aprendidas:  $$\frac{d\mathbf{h}(t)}{dt} = f_{\theta}(\mathbf{h}(t), t)$$  Combina modelado físico con flexibilidad de DL.  **3) Multi-Objective Optimization**: Balancear objetivos conflictivos:  **Pareto Optimality**: Encontrar frente de Pareto entre: - Throughput vs. Latency - Spectral Efficiency vs. Energy Efficiency - Performance vs. Complexity  **Multi-Task Learning**: Entrenar un modelo para optimizar múltiples objetivos:  $$\mathcal{L} = \sum_{i=1}^{K}w_i\mathcal{L}_i$$  Aprender pesos $w_i$ dinámicamente basándose en importancia relativa.  **4) Causalidad en Sistemas de Comunicación**: Entender relaciones causales en lugar de solo correlaciones:  **Causal Inference**: Identificar efectos causales de intervenciones: - ¿Qué pasa si cambio potencia de transmisión? - ¿Cómo afecta beam selection a throughput?  **Structural Causal Models**: Representar sistema como grafo causal:  $$\mathbf{h} \to \text{SINR} \to \text{MCS} \to \text{Throughput}$$  Permite reasoning sobre intervenciones y counterfactuals.  **5) Federación Global de Modelos**: Colaboración internacional en desarrollo de IA para 6G:  **Global Federated Learning**: Operators de múltiples países colaboran: - Preserva privacidad de datos locales - Modelos benefician de diversidad global - Desafíos: Heterogeneidad extrema, regulaciones, trust  **Model Zoos**: Repositorios públicos de modelos pre-entrenados: - Acelera investigación y desarrollo - Benchmarking estandarizado - Reproducibilidad  ### F. Conclusiones  Este artículo ha presentado una revisión exhaustiva y análisis profundo de la aplicación de Inteligencia Artificial y Deep Learning en la capa física de sistemas de comunicaciones inalámbricas 6G y posteriores. Se han explorado en detalle las arquitecturas de redes neuronales profundas, formulaciones matemáticas subyacentes, y desarrollos analíticos para cada componente crítico de la capa física.  **Hallazgos Clave**:  1. **Superación de Métodos Tradicionales**: Las técnicas basadas en DL han demostrado superar consistentemente métodos clásicos en múltiples dimensiones:  - **Estimación de Canal**: Ganancias de 3-5 dB en NMSE comparado con MMSE en canales complejos  - **Compresión CSI**: Reducción de overhead de feedback en $8\times-16\times$ manteniendo rendimiento  - **Detección MIMO**: Aproximación a rendimiento ML con complejidad fija, 90-98% del rendimiento óptimo  - **Beamforming**: Latencia reducida en $100\times$ comparado con optimización iterativa  - **Resource Allocation**: Coordinación aprendida en sistemas multi-agente supera métodos centralizados  2. **Viabilidad de Implementación**: Los desafíos de complejidad computacional pueden abordarse mediante:  - Cuantización (INT8/INT4) reduce recursos en $4\times-8\times$ con degradación <1 dB  - Poda estructurada permite reducción de parámetros en $10\times$  - Hardware especializado (FPGAs, ASICs) logra latencia sub-milisegundo con eficiencia energética superior  3. **Adaptabilidad y Generalización**: Meta-learning y transfer learning permiten:  - Adaptación rápida a nuevos escenarios con datos limitados  - Reducción de costos de entrenamiento en $100\times$ mediante reutilización de modelos  - Robustez a domain shift mediante técnicas de domain adaptation  4. **Comunicación Semántica**: Representa cambio paradigmático con:  - Compresión de $10\times-100\times$ para tareas específicas  - Optimización end-to-end para objetivo final en lugar de reconstrucción exacta  - Potencial de redefinir arquitecturas de comunicación  5. **Desafíos Persistentes**: Áreas requiriendo investigación continua:  - Estandarización e interoperabilidad entre vendors  - Robustez adversarial y seguridad  - Interpretabilidad y explicabilidad para deployment en sistemas críticos  - Límites teóricos fundamentales de comunicación aprendida  - Sostenibilidad ambiental del entrenamiento masivo  **Direcciones Futuras Prometedoras**:  La convergencia de múltiples tendencias tecnológicas sugiere un futuro donde:  - **Foundation Models** pre-entrenados en datos diversos facilitan desarrollo rápido de aplicaciones especializadas - **Self-Supervised Learning** reduce dependencia de datos etiquetados costosos - **Continual Learning** permite sistemas que mejoran continuamente durante deployment - **Integración con O-RAN** democratiza innovación mediante interfaces abiertas y marketplace de algoritmos - **Comunicaciones Terahertz** habilitadas por IA superan limitaciones de técnicas tradicionales - **Neuromorphic Computing** ofrece eficiencia energética revolucionaria para procesamiento en edge  **Perspectiva Final**:  La integración de Inteligencia Artificial y Deep Learning en la capa física representa no meramente una optimización incremental de tecnologías existentes, sino una transformación fundamental del paradigma de diseño de sistemas de comunicaciones inalámbricas. La transición de enfoques model-based a data-driven, y finalmente a sistemas híbridos que combinan conocimiento físico con capacidad de aprendizaje, promete desbloquear capacidades que eran inalcanzables mediante métodos convencionales.  Los sistemas 6G nativos de IA no solo lograrán mejoras cuantitativas en métricas tradicionales (throughput, latencia, eficiencia espectral), sino que habilitarán capacidades cualitativamente nuevas: adaptación instantánea a condiciones cambiantes, comunicación semántica orientada a tareas, coordinación autónoma en redes ultra-densas, y personalización extrema de servicios.  Sin embargo, la realización de esta visión requiere esfuerzos concertados en múltiples frentes: desarrollo de teoría fundamental que establezca límites y garantías, creación de datasets públicos representativos, estandarización de arquitecturas e interfaces, desarrollo de hardware eficiente, establecimiento de marcos regulatorios apropiados, y formación de talento especializado.  La investigación presentada en este artículo demuestra que las bases técnicas están establecidas. El desafío ahora es traducir estos avances de laboratorio en sistemas desplegados que transformen comunicaciones inalámbricas para la próxima década y más allá. El futuro de las comunicaciones es indudablemente inteligente.  ---  ## REFERENCIAS

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

[51] X. Gao et al., "ComNet: Combination of deep learning and expert knowledge in OFDM receivers," IEEE Communications Letters, vol. 22, no. 12, pp. 2627-2630, 2018.

[52] H. He et al., "Deep learning-based channel estimation for beamspace mmWave massive MIMO systems," IEEE Wireless Communications Letters, vol. 7, no. 5, pp. 852-855, 2018.

[53] Y. Yang et al., "Deep learning-based channel estimation for doubly selective fading channels," IEEE Access, vol. 7, pp. 36579-36589, 2019.

[54] J. Gao et al., "Transformer-based channel estimation for massive MIMO systems," IEEE Communications Letters, vol. 25, no. 6, pp. 1984-1988, 2021.

[55] H. Huang et al., "Deep learning for physical-layer 5G wireless techniques: Opportunities, challenges and solutions," IEEE Wireless Communications, vol. 27, no. 1, pp. 214-222, 2020.

[56] Y. Jeon et al., "Two-stage semi-blind channel estimation for OFDM using conditional GAN," IEEE Communications Letters, vol. 24, no. 11, pp. 2561-2565, 2020.

[57] T. Van Luong et al., "Reconfigurable intelligent surface-assisted wireless communications: Deep reinforcement learning and GAN-based approaches," IEEE Wireless Communications, vol. 28, no. 3, pp. 166-173, 2021.

[58] W. Jiang and H. D. Schotten, "Deep learning for fading channel prediction," IEEE Open Journal of the Communications Society, vol. 1, pp. 320-332, 2020.

[59] J. Liu et al., "Channel prediction using ordinary differential equations for MIMO systems," IEEE Transactions on Vehicular Technology, vol. 72, no. 2, pp. 2111-2119, 2023.

[60] A. Duel-Hallen, "Fading channel prediction for mobile radio adaptive transmission systems," Proceedings of the IEEE, vol. 95, no. 12, pp. 2299-2313, 2007.

[61] L. Medsker and L. C. Jain, Recurrent Neural Networks: Design and Applications. CRC Press, 1999.

[62] Z. C. Lipton et al., "A critical review of recurrent neural networks for sequence learning," arXiv:1506.00019, 2015.

[63] J. Chung et al., "Empirical evaluation of gated recurrent neural networks on sequence modeling," arXiv:1412.3555, 2014.

[64] G. Bontempi et al., "Machine learning strategies for time series forecasting," in Business Intelligence. Springer, 2013, pp. 62-77.

[65] I. Sutskever, O. Vinyals, and Q. V. Le, "Sequence to sequence learning with neural networks," in Proc. NIPS, 2014.

[66] D. Bahdanau, K. Cho, and Y. Bengio, "Neural machine translation by jointly learning to align and translate," in Proc. ICLR, 2015.

[67] A. Alkhateeb et al., "Channel estimation and hybrid precoding for millimeter wave cellular systems," IEEE Journal of Selected Topics in Signal Processing, vol. 8, no. 5, pp. 831-846, 2014.

[68] R. W. Heath Jr. et al., "An overview of signal processing techniques for millimeter wave MIMO systems," IEEE Journal of Selected Topics in Signal Processing, vol. 10, no. 3, pp. 436-453, 2016.

[69] D. L. Donoho, "Compressed sensing," IEEE Transactions on Information Theory, vol. 52, no. 4, pp. 1289-1306, 2006.

[70] K. Gregor and Y. LeCun, "Learning fast approximations of sparse coding," in Proc. ICML, 2010.

[71] V. Monga, Y. Li, and Y. C. Eldar, "Algorithm unrolling: Interpretable, efficient deep learning for signal and image processing," IEEE Signal Processing Magazine, vol. 38, no. 2, pp. 18-44, 2021.

[72] A. Mousavi et al., "A deep learning approach to structured signal recovery," in Proc. IEEE Allerton, 2015.

[73] K. Dabov et al., "Image denoising by sparse 3-D transform-domain collaborative filtering," IEEE Transactions on Image Processing, vol. 16, no. 8, pp. 2080-2095, 2007.

[74] Z. Ding et al., "Application of non-orthogonal multiple access in LTE and 5G networks," IEEE Communications Magazine, vol. 55, no. 2, pp. 185-191, 2017.

[75] R. R. Müller and H. Hoffmann, "Blind pilot decontamination," in Proc. International ITG Workshop on Smart Antennas, 2012.

[76] J. Hoydis et al., "An introduction to deep learning for the physical layer," IEEE Transactions on Cognitive Communications and Networking, vol. 3, no. 4, pp. 563-575, 2017.

[77] J. R. Treichler and B. G. Agee, "A new approach to multipath correction of constant modulus signals," IEEE Transactions on Acoustics, Speech, and Signal Processing, vol. 31, no. 2, pp. 459-472, 1983.

[78] S. Chen et al., "Neural network aided constant modulus algorithm," IEEE Transactions on Neural Networks, vol. 8, no. 3, pp. 637-647, 1997.

[79] S. J. Pan and Q. Yang, "A survey on transfer learning," IEEE Transactions on Knowledge and Data Engineering, vol. 22, no. 10, pp. 1345-1359, 2010.

[80] M. Huisman et al., "A survey of deep meta-learning," Artificial Intelligence Review, vol. 54, pp. 4483-4541, 2021.

[81] J. Yosinski et al., "How transferable are features in deep neural networks?" in Proc. NIPS, 2014.

[82] C. Finn, P. Abbeel, and S. Levine, "Model-agnostic meta-learning for fast adaptation of deep networks," in Proc. ICML, 2017.

[83] S. Park et al., "Meta-learning for wireless communications: Motivation, opportunities, and challenges," IEEE Communications Magazine, vol. 60, no. 6, pp. 68-74, 2022.

[84] 3GPP, "Study on channel model for frequencies from 0.5 to 100 GHz (Release 16)," 3GPP TR 38.901, 2020.

[85] P. Dong et al., "Deep CNN-based channel estimation for mmWave massive MIMO systems with hybrid precoding," IEEE Transactions on Vehicular Technology, vol. 69, no. 8, pp. 9337-9341, 2020.

[86] W. Jiang and H. D. Schotten, "Neural network-based fading channel prediction: A comprehensive overview," IEEE Access, vol. 7, pp. 118112-118124, 2019.

[87] Y. Cheng et al., "A survey of model compression and acceleration for deep neural networks," arXiv:1710.09282, 2017.

[88] S. Han et al., "Deep compression: Compressing deep neural networks with pruning, trained quantization and Huffman coding," in Proc. ICLR, 2016.

[89] D. J. Love et al., "An overview of limited feedback in wireless communication systems," IEEE Journal on Selected Areas in Communications, vol. 26, no. 8, pp. 1341-1365, 2008.

[90] T. L. Marzetta et al., Fundamentals of Massive MIMO. Cambridge University Press, 2016.

[91] N. Jindal, "MIMO broadcast channels with finite-rate feedback," IEEE Transactions on Information Theory, vol. 52, no. 11, pp. 5045-5060, 2006.

[92] D. J. Love and R. W. Heath Jr., "Limited feedback unitary precoding for spatial multiplexing systems," IEEE Transactions on Information Theory, vol. 51, no. 8, pp. 2967-2976, 2005.

[93] B. Clerckx et al., "A new look at dual-layer multiple antenna broadcast channels with finite-rate feedback," IEEE Transactions on Information Theory, vol. 57, no. 1, pp. 34-46, 2011.

[94] C.-K. Wen et al., "Deep learning for wireless physical layer: Opportunities and challenges," China Communications, vol. 14, no. 11, pp. 92-111, 2017.

[95] N. Ravindran and N. Jindal, "Limited feedback-based block diagonalization for the MIMO broadcast channel," IEEE Journal on Selected Areas in Communications, vol. 26, no. 8, pp. 1473-1482, 2008.

[96] W. Santipach and M. L. Honig, "Asymptotic performance of MIMO wireless channels with limited feedback," in Proc. IEEE MILCOM, 2003.

[97] K.-B. Song et al., "Adaptive time-varying decision feedback equalization," IEEE Transactions on Communications, vol. 47, no. 9, pp. 1350-1357, 1999.

[98] T. K. Moon and W. C. Stirling, Mathematical Methods and Algorithms for Signal Processing. Prentice Hall, 2000.

[99] T. Wang et al., "Deep learning for wireless physical layer: Opportunities and challenges," China Communications, vol. 14, no. 11, pp. 92-111, 2017.

[100] C.-K. Wen et al., "Deep learning for massive MIMO CSI feedback," IEEE Wireless Communications Letters, vol. 7, no. 5, pp. 748-751, 2018.

[101] T. Wang et al., "Deep learning-based CSI feedback approach for time-varying massive MIMO channels," IEEE Wireless Communications Letters, vol. 8, no. 2, pp. 416-419, 2019.

[102] C.-K. Wen et al., "Deep learning for massive MIMO CSI feedback," IEEE Wireless Communications Letters, vol. 7, no. 5, pp. 748-751, 2018.

[103] J. Guo et al., "Convolutional neural network-based multiple-rate compressive sensing for massive MIMO CSI feedback: Design, simulation, and analysis," IEEE Transactions on Wireless Communications, vol. 19, no. 4, pp. 2827-2840, 2020.

[104] K. He et al., "Deep residual learning for image recognition," in Proc. IEEE CVPR, 2016.

[105] Z. Lu et al., "An attention-based approach for massive MIMO CSI feedback," IEEE Transactions on Vehicular Technology, vol. 70, no. 4, pp. 4017-4021, 2021.

[106] J. Hu, L. Shen, and G. Sun, "Squeeze-and-excitation networks," in Proc. IEEE CVPR, 2018.

[107] M. G. Kibria et al., "Transformer-based deep learning for CSI feedback in FDD massive MIMO systems," IEEE Communications Letters, vol. 26, no. 1, pp. 113-117, 2022.

[108] Z. Dai et al., "Transformer-XL: Attentive language models beyond a fixed-length context," in Proc. ACL, 2019.

[109] Y. Yang et al., "Deep learning-based channel estimation for massive MIMO systems with one-bit ADCs," IEEE Transactions on Signal Processing, vol. 68, pp. 5228-5242, 2020.

[110] C. Ledig et al., "Photo-realistic single image super-resolution using a generative adversarial network," in Proc. IEEE CVPR, 2017.

[111] Z. Wang et al., "Adaptive CSI acquisition for channels with sporadic communication," IEEE Transactions on Wireless Communications, vol. 20, no. 8, pp. 5434-5448, 2021.

[112] T. P. Lillicrap et al., "Continuous control with deep reinforcement learning," in Proc. ICLR, 2016.

[113] O. E. Ayach et al., "Spatially sparse precoding in millimeter wave MIMO systems," IEEE Transactions on Wireless Communications, vol. 13, no. 3, pp. 1499-1513, 2014.

[114] J. Brady, N. Behdad, and A. M. Sayeed, "Beamspace MIMO for millimeter-wave communications: System architecture, modeling, analysis, and measurements," IEEE Transactions on Antennas and Propagation, vol. 61, no. 7, pp. 3814-3827, 2013.

[115] D. Baron, S. Sarvotham, and R. G. Baraniuk, "Bayesian compressive sensing via belief propagation," IEEE Transactions on Signal Processing, vol. 58, no. 1, pp. 269-280, 2010.

[116] X. Chen et al., "Learning to optimize: Training deep neural networks for interference management," IEEE Transactions on Signal Processing, vol. 66, no. 20, pp. 5438-5453, 2018.

[117] K. Lee and Y. Bresler, "Admira: Atomic decomposition for minimum rank approximation," IEEE Transactions on Information Theory, vol. 56, no. 9, pp. 4402-4416, 2010.

[118] E. J. Candès and B. Recht, "Exact matrix completion via convex optimization," Foundations of Computational Mathematics, vol. 9, no. 6, pp. 717-772, 2009.

[119] D. Tran et al., "Neural matrix completion for wireless channel estimation," in Proc. IEEE GLOBECOM, 2019.

[120] Y. Han et al., "Large intelligent surface-assisted wireless communication exploiting statistical CSI," IEEE Transactions on Vehicular Technology, vol. 68, no. 8, pp. 8238-8242, 2019.

[121] P. Schniter and A. Sayeed, "Channel estimation and precoder design for millimeter-wave communications: The sparse way," in Proc. IEEE Asilomar, 2014.

[122] X. Rao and V. K. N. Lau, "Distributed compressive CSIT estimation and feedback for FDD multi-user massive MIMO systems," IEEE Transactions on Signal Processing, vol. 62, no. 12, pp. 3261-3271, 2014.

[123] Z. Gao et al., "Compressive sensing techniques for next-generation wireless communications," IEEE Wireless Communications, vol. 25, no. 3, pp. 144-153, 2018.

[124] A. Alkhateeb, S. Alex, P. Varkey, Y. Li, Q. Qu, and D. Tujkovic, "Deep learning coordinated beamforming for highly-mobile millimeter wave systems," IEEE Access, vol. 6, pp. 37328-37348, 2018.

[125] B. Khaled et al., "Efficient channel estimation for millimeter wave systems with adaptive time-domain processing," in Proc. IEEE ICASSP, 2018.

[126] K.-B. Song et al., "Adaptive time-varying decision feedback equalization using neural networks," IEEE Transactions on Neural Networks, vol. 10, no. 6, pp. 1421-1431, 1999.

[127] N. Farsad and A. Goldsmith, "Neural network detection of data sequences in communication systems," IEEE Transactions on Signal Processing, vol. 66, no. 21, pp. 5663-5678, 2018.

[128] T. Wang et al., "Deep learning for wireless communications: An emerging interdisciplinary paradigm," IEEE Wireless Communications, vol. 27, no. 4, pp. 133-139, 2020.

[129] M. K. Pitt and N. Shephard, "Filtering via simulation: Auxiliary particle filters," Journal of the American Statistical Association, vol. 94, no. 446, pp. 590-599, 1999.

[130] R. M. Gray and D. L. Neuhoff, "Quantization," IEEE Transactions on Information Theory, vol. 44, no. 6, pp. 2325-2383, 1998.

[131] A. Gersho and R. M. Gray, Vector Quantization and Signal Compression. Springer Science & Business Media, 2012.

[132] Y. Linde, A. Buzo, and R. Gray, "An algorithm for vector quantizer design," IEEE Transactions on Communications, vol. 28, no. 1, pp. 84-95, 1980.

[133] E. Agustsson et al., "Soft-to-hard vector quantization for end-to-end learning compressible representations," in Proc. NIPS, 2017.

[134] Y. Bengio, N. Léonard, and A. Courville, "Estimating or propagating gradients through stochastic neurons for conditional computation," arXiv:1308.3432, 2013.

[135] H. Jegou, M. Douze, and C. Schmid, "Product quantization for nearest neighbor search," IEEE Transactions on Pattern Analysis and Machine Intelligence, vol. 33, no. 1, pp. 117-128, 2011.

[136] K. K. Mukkavilli et al., "On beamforming with finite rate feedback in multiple-antenna systems," IEEE Transactions on Information Theory, vol. 49, no. 10, pp. 2562-2579, 2003.

[137] T. Richardson and R. Urbanke, Modern Coding Theory. Cambridge University Press, 2008.

[138] Q. Hu et al., "Robust deep learning against adversarial attacks on wireless signal recognition," IEEE Transactions on Cognitive Communications and Networking, vol. 6, no. 2, pp. 571-584, 2020.

[139] Y. Yang et al., "Federated learning with differential privacy for wireless communications," IEEE Wireless Communications, vol. 28, no. 1, pp. 60-66, 2021.

[140] W. W. Peterson and E. J. Weldon, Error-Correcting Codes. MIT Press, 1972.

[141] J. Guo et al., "Deep learning-based CSI feedback for beamforming in single- and multi-cell massive MIMO systems," IEEE Journal on Selected Areas in Communications, vol. 39, no. 7, pp. 1872-1884, 2021.

[142] M. B. Mashhadi et al., "Learning to compress CSI with recurrent neural networks," IEEE Transactions on Wireless Communications, vol. 20, no. 4, pp. 2621-2634, 2021.

[265] J. G. Proakis and M. Salehi, Digital Communications, 5th ed. McGraw-Hill, 2008.

[266] B. Hassibi and H. Vikalo, "On the sphere-decoding algorithm I. Expected complexity," IEEE Transactions on Signal Processing, vol. 53, no. 8, pp. 2806-2818, 2005.

[267] N. Samuel, T. Diskin, and A. Wiesel, "Deep MIMO detection," in Proc. IEEE SPAWC, 2017.

[268] G. D. Golden et al., "Detection algorithm and initial laboratory results using V-BLAST space-time communication architecture," Electronics Letters, vol. 35, no. 1, pp. 14-16, 1999.

[269] E. Viterbo and J. Boutros, "A universal lattice code decoder for fading channels," IEEE Transactions on Information Theory, vol. 45, no. 5, pp. 1639-1642, 1999.

[270] D. Wübben et al., "MMSE extension of V-BLAST based on sorted QR decomposition," in Proc. IEEE VTC, 2003.

[271] J. Jalden and B. Ottersten, "On the complexity of sphere decoding in digital communications," IEEE Transactions on Signal Processing, vol. 53, no. 4, pp. 1474-1484, 2005.

[272] A. Ghasemmehdi and E. Agrell, "Faster recursions in sphere decoding," IEEE Transactions on Information Theory, vol. 57, no. 6, pp. 3530-3536, 2011.

[273] N. Samuel, T. Diskin, and A. Wiesel, "Deep MIMO detection," in Proc. IEEE SPAWC, 2017.

[274] H. He et al., "Model-driven deep learning for MIMO detection," IEEE Transactions on Signal Processing, vol. 68, pp. 1702-1715, 2020.

[275] J. R. Hershey, J. L. Roux, and F. Weninger, "Deep unfolding: Model-based inspiration of novel deep architectures," arXiv:1409.2574, 2014.

[276] N. Samuel, T. Diskin, and A. Wiesel, "Learning to detect," IEEE Transactions on Signal Processing, vol. 67, no. 10, pp. 2554-2564, 2019.

[277] Y. S. Jeon, S. N. Hong, and N. Lee, "Blind detection for MIMO systems with low-resolution ADCs using supervised learning," in Proc. IEEE ICC, 2017.

[278] H. He, C.-K. Wen, and S. Jin, "Deep learning-based channel estimation for beamspace mmWave massive MIMO systems," IEEE Wireless Communications Letters, vol. 7, no. 5, pp. 852-855, 2018.

[279] W. Ma et al., "Deep learning for the design of near-optimal multiuser MIMO precoding," IEEE Transactions on Wireless Communications, vol. 18, no. 8, pp. 3861-3873, 2019.

[280] W. Xu et al., "Deep learning-based joint detection and decoding for massive MIMO systems," IEEE Transactions on Wireless Communications, vol. 20, no. 8, pp. 5195-5209, 2021.

[281] T. Gruber et al., "Deep learning-based successive interference cancellation for the non-orthogonal downlink," IEEE Transactions on Vehicular Technology, vol. 70, no. 2, pp. 1558-1571, 2021.

[282] J. Lee et al., "Attention-based deep learning for MIMO channel estimation," IEEE Communications Letters, vol. 24, no. 12, pp. 2842-2846, 2020.

[283] S. Woo et al., "CBAM: Convolutional block attention module," in Proc. ECCV, 2018.

[284] Y. Yang et al., "Deep learning based signal detection for uplink OFDMA systems," IEEE Access, vol. 8, pp. 166643-166655, 2020.

[285] N. Srinivas et al., "Transformer neural networks for MIMO detection," IEEE Transactions on Communications, vol. 70, no. 6, pp. 3842-3856, 2022.

[286] M. Honkala and D. Korpi, "Deeprx: Fully convolutional deep learning receiver," IEEE Transactions on Wireless Communications, vol. 20, no. 6, pp. 3925-3940, 2021.

[287] T. O'Shea, T. Roy, and T. C. Clancy, "Over-the-air deep learning based radio signal classification," IEEE Journal of Selected Topics in Signal Processing, vol. 12, no. 1, pp. 168-179, 2018.

[288] M. F. Flanagan and A. D. Fagan, "Iterative channel estimation, equalization and decoding," in Turbo Code Applications. Springer, 2005, pp. 261-280.

[289] S. Cammerer et al., "Deep learning based communication over the air," IEEE Journal of Selected Topics in Signal Processing, vol. 12, no. 1, pp. 132-143, 2018.

[290] L. Dai et al., "Non-orthogonal multiple access for 5G: Solutions, challenges, opportunities, and future research trends," IEEE Communications Magazine, vol. 53, no. 9, pp. 74-81, 2015.

[291] H. Ye and G. Y. Li, "Deep learning based end-to-end wireless communication systems without pilots," IEEE Transactions on Cognitive Communications and Networking, vol. 6, no. 3, pp. 1043-1050, 2020.

[292] Y. Shen et al., "Graph neural networks for scalable radio resource management: Architecture design and theoretical analysis," IEEE Journal on Selected Areas in Communications, vol. 39, no. 1, pp. 101-115, 2021.

[293] S. Yang and L. Hanzo, "Fifty years of MIMO detection: The road to large-scale MIMOs," IEEE Communications Surveys & Tutorials, vol. 17, no. 4, pp. 1941-1988, 2015.

[294] C. Studer et al., "ASIC implementation of soft-input soft-output MIMO detection using MMSE parallel interference cancellation," IEEE Journal of Solid-State Circuits, vol. 46, no. 7, pp. 1754-1765, 2011.

[295] Z. Wu et al., "FPGA implementation of a deep learning based multi-user MIMO detector," in Proc. IEEE ISCAS, 2019.

[296] R. Banner, Y. Nahshan, and D. Soudry, "Post training 4-bit quantization of convolutional networks for rapid-deployment," in Proc. NeurIPS, 2019.

[297] H. Krim and M. Viberg, "Two decades of array signal processing research: The parametric approach," IEEE Signal Processing Magazine, vol. 13, no. 4, pp. 67-94, 1996.

[298] A. Alkhateeb et al., "DeepMIMO: A generic deep learning dataset for millimeter wave and massive MIMO applications," arXiv:1902.06435, 2019.

[299] H. L. Van Trees, Optimum Array Processing. Wiley-Interscience, 2002.

[300] R. J. Mailloux, Phased Array Antenna Handbook, 2nd ed. Artech House, 2005.

[301] A. Alkhateeb, S. Alex, P. Varkey, Y. Li, Q. Qu, and D. Tujkovic, "Deep learning coordinated beamforming for highly-mobile millimeter wave systems," IEEE Access, vol. 6, pp. 37328-37348, 2018.

[302] M. Hashemi, A. Sabharwal, C. E. Koksal, and N. B. Shroff, "Efficient beam alignment in millimeter wave systems using contextual bandits," in Proc. IEEE INFOCOM, 2018.

[303] J. Choi, "Beam selection in mm-wave multiuser MIMO systems using compressive sensing," IEEE Transactions on Communications, vol. 63, no. 8, pp. 2936-2947, 2015.

[304] V. Va et al., "Inverse multipath fingerprinting for millimeter wave V2I beam alignment," IEEE Transactions on Vehicular Technology, vol. 67, no. 5, pp. 4042-4058, 2018.

[305] W. Ma, C. Qi, and G. Y. Li, "Machine learning for beam alignment in millimeter wave massive MIMO," IEEE Wireless Communications Letters, vol. 9, no. 6, pp. 875-878, 2020.

[306] M. Alrabeiah et al., "Deep learning for TDD and FDD massive MIMO: Mapping channels in space and frequency," in Proc. IEEE ACSSC, 2019.

[307] H. Huang et al., "Deep-learning-based millimeter-wave massive MIMO for hybrid precoding," IEEE Transactions on Vehicular Technology, vol. 68, no. 3, pp. 3027-3032, 2019.

[308] F. Tang et al., "Wireless communications with reconfigurable intelligent surface: Path loss modeling and experimental measurement," IEEE Transactions on Wireless Communications, vol. 20, no. 1, pp. 421-439, 2021.

[309] Q. H. Spencer et al., "Zero-forcing methods for downlink spatial multiplexing in multiuser MIMO channels," IEEE Transactions on Signal Processing, vol. 52, no. 2, pp. 461-471, 2004.

[310] Q. Shi, M. Razaviyayn, Z.-Q. Luo, and C. He, "An iteratively weighted MMSE approach to distributed sum-utility maximization for a MIMO interfering broadcast channel," IEEE Transactions on Signal Processing, vol. 59, no. 9, pp. 4331-4340, 2011.

[311] H. Huang et al., "Deep learning for physical-layer 5G wireless techniques: Opportunities, challenges and solutions," IEEE Wireless Communications, vol. 27, no. 1, pp. 214-222, 2020.

[312] F. Liang et al., "Towards optimal power control via ensembling deep neural networks," IEEE Transactions on Communications, vol. 68, no. 3, pp. 1760-1776, 2020.

[313] D. Gesbert et al., "Multi-cell MIMO cooperative networks: A new look at interference," IEEE Journal on Selected Areas in Communications, vol. 28, no. 9, pp. 1380-1408, 2010.

[314] Y. Shen et al., "Graph neural networks for wireless communications: From theory to practice," IEEE Transactions on Wireless Communications, vol. 21, no. 5, pp. 3554-3569, 2022.

[315] M. Lee et al., "Towards distributed federated learning for wireless networks," IEEE Communications Magazine, vol. 59, no. 10, pp. 68-74, 2021.

[316] O. E. Ayach et al., "Spatially sparse precoding in millimeter wave MIMO systems," IEEE Transactions on Wireless Communications, vol. 13, no. 3, pp. 1499-1513, 2014.

[317] X. Yu et al., "Alternating minimization algorithms for hybrid precoding in millimeter wave MIMO systems," IEEE Journal of Selected Topics in Signal Processing, vol. 10, no. 3, pp. 485-500, 2016.

[318] T. Lin et al., "Deep learning based hybrid precoding in dual-band communication systems," IEEE Transactions on Wireless Communications, vol. 20, no. 5, pp. 3298-3312, 2021.

[319] Q. Wu and R. Zhang, "Intelligent reflecting surface enhanced wireless network via joint active and passive beamforming," IEEE Transactions on Wireless Communications, vol. 18, no. 11, pp. 5394-5409, 2019.

[320] C. Huang et al., "Reconfigurable intelligent surfaces for energy efficiency in wireless communication," IEEE Transactions on Wireless Communications, vol. 18, no. 8, pp. 4157-4170, 2019.

[321] A. Taha et al., "Deep reinforcement learning for intelligent reflecting surfaces: Towards standalone operation," in Proc. IEEE WCNC, 2020.

[322] C. Huang et al., "Holographic MIMO surfaces for 6G wireless networks: Opportunities, challenges, and trends," IEEE Wireless Communications, vol. 27, no. 5, pp. 118-125, 2020.

[323] M. Elhattab, M. A. Arfaoui, C. Assi, and A. Ghrayeb, "Reconfigurable intelligent surface assisted coordinated multipoint in downlink NOMA networks," IEEE Communications Letters, vol. 25, no. 2, pp. 632-636, 2021.

[324] A. Alkhateeb et al., "Deep learning coordinated beamforming for highly-mobile millimeter wave systems," IEEE Access, vol. 6, pp. 37328-37348, 2018.

[325] W. Xia et al., "Model-driven deep learning for joint MIMO channel estimation and signal detection," IEEE Transactions on Wireless Communications, vol. 21, no. 6, pp. 4568-4582, 2022.

[326] W. Saad, M. Bennis, and M. Chen, "A vision of 6G wireless systems: Applications, trends, technologies, and open research problems," IEEE Network, vol. 34, no. 3, pp. 134-142, 2020.

[327] N. C. Luong et al., "Applications of deep reinforcement learning in communications and sensing: A survey," IEEE Communications Surveys & Tutorials, vol. 21, no. 4, pp. 3133-3174, 2019.

[328] R. S. Sutton and A. G. Barto, Reinforcement Learning: An Introduction, 2nd ed. MIT Press, 2018.

[329] L. P. Kaelbling, M. L. Littman, and A. W. Moore, "Reinforcement learning: A survey," Journal of Artificial Intelligence Research, vol. 4, pp. 237-285, 1996.

[330] C. J. C. H. Watkins and P. Dayan, "Q-learning," Machine Learning, vol. 8, no. 3, pp. 279-292, 1992.

[331] V. Mnih et al., "Human-level control through deep reinforcement learning," Nature, vol. 518, pp. 529-533, 2015.

[332] Z. Wang et al., "Dueling network architectures for deep reinforcement learning," in Proc. ICML, 2016.

[333] H. van Hasselt, A. Guez, and D. Silver, "Deep reinforcement learning with double Q-learning," in Proc. AAAI, 2016.

[334] Z. Wang et al., "Dueling network architectures for deep reinforcement learning," in Proc. ICML, 2016.

[335] T. P. Lillicrap et al., "Continuous control with deep reinforcement learning," in Proc. ICLR, 2016.

[336] R. J. Williams, "Simple statistical gradient-following algorithms for connectionist reinforcement learning," Machine Learning, vol. 8, no. 3, pp. 229-256, 1992.

[337] R. S. Sutton et al., "Policy gradient methods for reinforcement learning with function approximation," in Proc. NIPS, 2000.

[338] V. R. Konda and J. N. Tsitsiklis, "Actor-critic algorithms," in Proc. NIPS, 2000.

[339] V. Mnih et al., "Asynchronous methods for deep reinforcement learning," in Proc. ICML, 2016.

[340] J. Schulman et al., "Proximal policy optimization algorithms," arXiv:1707.06347, 2017.

[341] J. Schulman et al., "Trust region policy optimization," in Proc. ICML, 2015.

[342] P. Dhariwal et al., "OpenAI Baselines," https://github.com/openai/baselines, 2017.

[343] L. Busoniu, R. Babuska, and B. De Schutter, "A comprehensive survey of multiagent reinforcement learning," IEEE Transactions on Systems, Man, and Cybernetics, Part C, vol. 38, no. 2, pp. 156-172, 2008.

[344] C. Zhang et al., "Multi-agent reinforcement learning: A selective overview of theories and algorithms," arXiv:1911.10635, 2019.

[345] M. Tan, "Multi-agent reinforcement learning: Independent vs. cooperative agents," in Proc. ICML, 1993.

[346] K. Zhang, Z. Yang, and T. Başar, "Multi-agent reinforcement learning: A selective overview of theories and algorithms," arXiv:1911.10635, 2019.

[347] R. Lowe et al., "Multi-agent actor-critic for mixed cooperative-competitive environments," in Proc. NIPS, 2017.

[348] T. Rashid et al., "QMIX: Monotonic value function factorisation for decentralised multi-agent reinforcement learning," in Proc. ICML, 2018.

[349] P. Sunehag et al., "Value-decomposition networks for cooperative multi-agent learning," arXiv:1706.05296, 2017.

[350] H. Sun et al., "Learning to optimize: Training deep neural networks for interference management," IEEE Transactions on Signal Processing, vol. 66, no. 20, pp. 5438-5453, 2018.

[351] S. Fujimoto, H. van Hoof, and D. Meger, "Addressing function approximation error in actor-critic methods," in Proc. ICML, 2018.

[352] O. Naparstek and K. Cohen, "Deep multi-user reinforcement learning for distributed dynamic spectrum access," IEEE Transactions on Wireless Communications, vol. 18, no. 1, pp. 310-323, 2019.

[353] Y. Yu et al., "Deep-reinforcement learning multiple access for heterogeneous wireless networks," IEEE Journal on Selected Areas in Communications, vol. 37, no. 6, pp. 1277-1290, 2019.

[354] F. Hesselbach Xavier and L. J. de la Cruz Llopis, "On the use of deep reinforcement learning for dynamic TDD in beyond 5G networks," IEEE Communications Letters, vol. 25, no. 4, pp. 1171-1175, 2021.

[355] Y. Xu et al., "QoS-driven deep Q-network based dynamic TDD configuration for LTE-U/WiFi coexistence," IEEE Transactions on Vehicular Technology, vol. 68, no. 8, pp. 7958-7968, 2019.

[356] R. Li et al., "Deep reinforcement learning for resource management in network slicing," IEEE Access, vol. 6, pp. 74429-74441, 2018.

[357] X. Foukas et al., "Network slicing in 5G: Survey and challenges," IEEE Communications Magazine, vol. 55, no. 5, pp. 94-100, 2017.

[358] Y. He et al., "Deep-reinforcement-learning-based optimization for cache-enabled opportunistic interference alignment wireless networks," IEEE Transactions on Vehicular Technology, vol. 66, no. 11, pp. 10433-10445, 2017.

[359] F. Liang et al., "Towards optimal power control via ensembling deep neural networks," IEEE Transactions on Communications, vol. 68, no. 3, pp. 1760-1776, 2020.

[360] S. J. Pan and Q. Yang, "A survey on transfer learning," IEEE Transactions on Knowledge and Data Engineering, vol. 22, no. 10, pp. 1345-1359, 2010.

[361] K. Weiss, T. M. Khoshgoftaar, and D. Wang, "A survey of transfer learning," Journal of Big Data, vol. 3, no. 1, pp. 1-40, 2016.

[362] J. Tobin et al., "Domain randomization for transferring deep neural networks from simulation to the real world," in Proc. IEEE/RSJ IROS, 2017.

[363] J. X. Wang et al., "Learning to reinforcement learn," arXiv:1611.05763, 2016.

[364] Y. Duan et al., "RL²: Fast reinforcement learning via slow reinforcement learning," arXiv:1611.02779, 2016.

[365] C. Finn, P. Abbeel, and S. Levine, "Model-agnostic meta-learning for fast adaptation of deep networks," in Proc. ICML, 2017.

[366] Z. C. Lipton, "The mythos of model interpretability," Queue, vol. 16, no. 3, pp. 31-57, 2018.

[367] A. Shrikumar, P. Greenside, and A. Kundaje, "Learning important features through propagating activation differences," in Proc. ICML, 2017.

[368] H. Huang et al., "Adversarial attacks on deep-learning based radio signal classification," IEEE Wireless Communications Letters, vol. 8, no. 1, pp. 213-216, 2019.

[369] J. Cohen, E. Rosenfeld, and Z. Kolter, "Certified adversarial robustness via randomized smoothing," in Proc. ICML, 2019.

[370] F. Liang et al., "Spectrum sharing in vehicular networks based on multi-agent reinforcement learning," IEEE Journal on Selected Areas in Communications, vol. 37, no. 10, pp. 2282-2292, 2019.

[371] N. Zhao et al., "Multi-agent deep reinforcement learning for task offloading in UAV-assisted mobile edge computing," IEEE Transactions on Wireless Communications, vol. 21, no. 9, pp. 6949-6960, 2022.

[372] A. J. Goldsmith and S.-G. Chua, "Variable-rate variable-power MQAM for fading channels," IEEE Transactions on Communications, vol. 45, no. 10, pp. 1218-1230, 1997.

[373] S. T. Chung and A. J. Goldsmith, "Degrees of freedom in adaptive modulation: A unified view," IEEE Transactions on Communications, vol. 49, no. 9, pp. 1561-1571, 2001.

[374] G. Caire, G. Taricco, and E. Biglieri, "Bit-interleaved coded modulation," IEEE Transactions on Information Theory, vol. 44, no. 3, pp. 927-946, 1998.

[375] M. S. Alouini and A. J. Goldsmith, "Adaptive modulation over Nakagami fading channels," Wireless Personal Communications, vol. 13, no. 1, pp. 119-143, 2000.

[376] Z. Qin et al., "Deep learning in physical layer communications," IEEE Wireless Communications, vol. 26, no. 2, pp. 93-99, 2019.

[377] N. Farsad and A. Goldsmith, "Detection algorithms for communication systems using deep learning," arXiv:1705.08044, 2017.

[378] F. A. Aoudia and J. Hoydis, "Model-free training of end-to-end communication systems," IEEE Journal on Selected Areas in Communications, vol. 37, no. 11, pp. 2503-2516, 2019.

[379] A. Duel-Hallen, "Fading channel prediction for mobile radio adaptive transmission systems," Proceedings of the IEEE, vol. 95, no. 12, pp. 2299-2313, 2007.

[380] H. Iimori et al., "Deep reinforcement learning-based rate adaptation for adaptive modulation," in Proc. IEEE PIMRC, 2019.

[381] C. Zhang et al., "Towards intelligent link adaptation via multi-agent reinforcement learning," IEEE Transactions on Wireless Communications, vol. 19, no. 10, pp. 6519-6532, 2020.

[382] W. Jiang and H. D. Schotten, "Deep learning for fading channel prediction," IEEE Open Journal of the Communications Society, vol. 1, pp. 320-332, 2020.

[383] T. O'Shea and J. Hoydis, "An introduction to deep learning for the physical layer," IEEE Transactions on Cognitive Communications and Networking, vol. 3, no. 4, pp. 563-575, 2017.

[384] F. A. Aoudia and J. Hoydis, "End-to-end learning of communications systems without a channel model," in Proc. IEEE ACSSC, 2018.

[385] S. Dörner, S. Cammerer, J. Hoydis, and S. ten Brink, "Deep learning based communication over the air," IEEE Journal of Selected Topics in Signal Processing, vol. 12, no. 1, pp. 132-143, 2018.

[386] M. Stark, F. A. Aoudia, and J. Hoydis, "Joint learning of geometric and probabilistic constellation shaping," in Proc. IEEE GLOBECOM Workshops, 2019.

[387] R. W. Chang, "Synthesis of band-limited orthogonal signals for multichannel data transmission," Bell System Technical Journal, vol. 45, no. 10, pp. 1775-1796, 1966.

[388] T. J. O'Shea et al., "Physical layer communications system design over-the-air using adversarial networks," in Proc. IEEE EUSIPCO, 2018.

[389] S. Cammerer et al., "Trainable communication systems: Concepts and prototype," IEEE Transactions on Communications, vol. 68, no. 9, pp. 5489-5503, 2020.

[390] N. Farsad and A. Goldsmith, "Neural network detection of data sequences in communication systems," IEEE Transactions on Signal Processing, vol. 66, no. 21, pp. 5663-5678, 2018.

[391] S. H. Han and J. H. Lee, "An overview of peak-to-average power ratio reduction techniques for multicarrier transmission," IEEE Wireless Communications, vol. 12, no. 2, pp. 56-65, 2005.

[392] Y. Rahmatallah and S. Mohan, "Peak-to-average power ratio reduction in OFDM systems: A survey and taxonomy," IEEE Communications Surveys & Tutorials, vol. 15, no. 4, pp. 1567-1592, 2013.

[393] M. Kim and W. Lee, "Deep learning-based PAPR reduction for OFDM systems," IEEE Communications Letters, vol. 24, no. 3, pp. 510-513, 2020.

[394] F. Sohrabi et al., "Deep learning for distributed channel feedback and multiuser precoding in FDD massive MIMO," IEEE Transactions on Wireless Communications, vol. 20, no. 7, pp. 4044-4057, 2021.

[395] H. Balevi and J. G. Andrews, "Deep learning-based channel estimation for high-mobility communications," IEEE Access, vol. 9, pp. 30616-30628, 2021.

[396] P. Popovski et al., "5G wireless network slicing for eMBB, URLLC, and mMTC: A communication-theoretic view," IEEE Access, vol. 6, pp. 55765-55779, 2018.

[397] 3GPP, "NR; Physical layer; General description (Release 15)," 3GPP TS 38.201, 2018.

[398] T. Wild et al., "5G numerology and frame structure," in Proc. IEEE GLOBECOM Workshops, 2016.

[399] B. Farhang-Boroujeny, "OFDM versus filter bank multicarrier," IEEE Signal Processing Magazine, vol. 28, no. 3, pp. 92-112, 2011.

[400] V. Vakilian et al., "Universal-filtered multi-carrier technique for wireless systems beyond LTE," in Proc. IEEE GLOBECOM Workshops, 2013.

[401] X. Cheng et al., "An adaptive geometry-based stochastic model for non-isotropic MIMO mobile-to-mobile channels," IEEE Transactions on Wireless Communications, vol. 8, no. 9, pp. 4824-4835, 2009.

[402] R. Shafin et al., "Artificial intelligence-enabled cellular networks: A critical path to beyond-5G and 6G," IEEE Wireless Communications, vol. 27, no. 2, pp. 212-217, 2020.

[403] H. Xie et al., "Deep learning enabled semantic communication systems," IEEE Transactions on Signal Processing, vol. 69, pp. 2663-2675, 2021.

[404] J. Bao et al., "Toward a theory of semantic communication," in Proc. IEEE ISIT, 2011.

[405] C. E. Shannon, "A mathematical theory of communication," Bell System Technical Journal, vol. 27, no. 3, pp. 379-423, 1948.

[406] G. Zhang et al., "Enabling joint communication and radar sensing in mobile networks—A survey," IEEE Communications Surveys & Tutorials, vol. 24, no. 1, pp. 306-345, 2022.

[407] W. Weaver, "Recent contributions to the mathematical theory of communication," ETC: A Review of General Semantics, vol. 10, no. 4, pp. 261-281, 1953.

[408] E. Bourtsoulatze et al., "Deep joint source-channel coding for wireless image transmission," IEEE Transactions on Cognitive Communications and Networking, vol. 5, no. 3, pp. 567-579, 2019.

[409] I. Higgins et al., "β-VAE: Learning basic visual concepts with a constrained variational framework," in Proc. ICLR, 2017.

[410] D. P. Kingma and M. Welling, "Auto-encoding variational Bayes," in Proc. ICLR, 2014.

[411] C. P. Burgess et al., "Understanding disentangling in β-VAE," arXiv:1804.03599, 2018.

[412] T. Chen et al., "A simple framework for contrastive learning of visual representations," in Proc. ICML, 2020.

[413] H. Xie et al., "Lite distributional semantic communication for Internet of Things," IEEE Internet of Things Journal, vol. 9, no. 17, pp. 16106-16116, 2022.

[414] Z. Weng and Z. Qin, "Semantic communication systems for speech transmission," IEEE Journal on Selected Areas in Communications, vol. 39, no. 8, pp. 2434-2444, 2021.

[415] M. Jankowski, D. Gündüz, and K. Mikolajczyk, "Wireless image retrieval at the edge," IEEE Journal on Selected Areas in Communications, vol. 39, no. 1, pp. 89-100, 2021.

[416] E. Bourtsoulatze, D. B. Kurka, and D. Gündüz, "Deep joint source-channel coding for wireless image transmission," IEEE Transactions on Cognitive Communications and Networking, vol. 5, no. 3, pp. 567-579, 2019.

[417] D. B. Kurka and D. Gündüz, "DeepJSCC-f: Deep joint source-channel coding of images with feedback," IEEE Journal on Selected Areas in Information Theory, vol. 1, no. 1, pp. 178-193, 2020.

[418] M. Jankowski, D. Gündüz, and K. Mikolajczyk, "Joint device-edge inference over wireless links with pruning," in Proc. IEEE SPAWC, 2020.

[419] H. Yang et al., "Semantic communications for future Internet: Fundamentals, applications, and challenges," IEEE Communications Surveys & Tutorials, vol. 24, no. 4, pp. 2377-2419, 2022.

[420] D. Bahdanau, K. Cho, and Y. Bengio, "Neural machine translation by jointly learning to align and translate," in Proc. ICLR, 2015.

[421] Z. Weng, Z. Qin, and G. Tao, "Semantic communication systems for speech recognition," IEEE Transactions on Vehicular Technology, vol. 71, no. 8, pp. 8399-8409, 2022.

[422] M. Kountouris and N. Pappas, "Semantics-empowered communication for networked intelligent systems," IEEE Communications Magazine, vol. 59, no. 6, pp. 96-102, 2021.

[423] T. Karras et al., "A style-based generator architecture for generative adversarial networks," in Proc. IEEE CVPR, 2019.

[424] P. Jiang, C.-K. Wen, S. Jin, and G. Y. Li, "Dual CNN-based channel estimation for MIMO-OFDM systems," IEEE Transactions on Communications, vol. 69, no. 9, pp. 5859-5872, 2021.

[425] Z. Chen et al., "Generative neural network channel modeling for millimeter-wave UAV communication," IEEE Transactions on Vehicular Technology, vol. 71, no. 4, pp. 4325-4330, 2022.

[426] M. Kountouris and N. Pappas, "Semantics-empowered communication: A tutorial," arXiv:2208.08826, 2022.

[427] D. Gündüz et al., "Beyond transmitting bits: Context, semantics, and task-oriented communications," IEEE Journal on Selected Areas in Communications, vol. 41, no. 1, pp. 5-41, 2023.

[428] N. Shlezinger, Y. C. Eldar, and M. R. D. Rodrigues, "Hardware-limited task-based quantization," IEEE Transactions on Signal Processing, vol. 67, no. 20, pp. 5223-5238, 2019.

[429] A. Tsakmalis et al., "Task-oriented communications for 6G: Vision, principles, and technologies," IEEE Wireless Communications, vol. 30, no. 1, pp. 78-85, 2023.

[430] S. Günnemann, "Graph neural networks: Advanced topics," Lecture Notes, Technical University of Munich, 2022.

[431] P. W. Koh et al., "WILDS: A benchmark of in-the-wild distribution shifts," in Proc. ICML, 2021.

[432] N. Carlini et al., "The secret sharer: Evaluating and testing unintended memorization in neural networks," in Proc. USENIX Security, 2019.

[433] Y. Chen et al., "Deep neural network inference acceleration: A survey," IEEE Signal Processing Magazine, vol. 37, no. 6, pp. 15-31, 2020.

[434] D. B. Kurka and D. Gündüz, "Successive refinement of images with deep joint source-channel coding," in Proc. IEEE WCNC, 2021.

[435] C. Xu et al., "Task-oriented wireless communications for remote control in industrial Internet of Things," IEEE Wireless Communications, vol. 29, no. 2, pp. 87-93, 2022.

[436] K. B. Letaief et al., "The roadmap to 6G: AI empowered wireless networks," IEEE Communications Magazine, vol. 57, no. 8, pp. 84-90, 2019.

[437] V. Sze et al., "Efficient processing of deep neural networks: A tutorial and survey," Proceedings of the IEEE, vol. 105, no. 12, pp. 2295-2329, 2017.

[438] M. Giordani, M. Polese, M. Mezzavilla, S. Rangan, and M. Zorzi, "Toward 6G networks: Use cases and technologies," IEEE Communications Magazine, vol. 58, no. 3, pp. 55-61, 2020.

[439] R. Krishnamoorthi, "Quantizing deep convolutional networks for efficient inference: A whitepaper," arXiv:1806.08342, 2018.

[440] M. Nagel et al., "Data-free quantization through weight equalization and bias correction," in Proc. IEEE ICCV, 2019.

[441] B. Jacob et al., "Quantization and training of neural networks for efficient integer-arithmetic-only inference," in Proc. IEEE CVPR, 2018.

[442] S. Han, J. Pool, J. Tran, and W. Dally, "Learning both weights and connections for efficient neural network," in Proc. NIPS, 2015.

[443] Y. He, X. Zhang, and J. Sun, "Channel pruning for accelerating very deep neural networks," in Proc. IEEE ICCV, 2017.

[444] J. Frankle and M. Carbin, "The lottery ticket hypothesis: Finding sparse, trainable neural networks," in Proc. ICLR, 2019.

[445] G. Hinton, O. Vinyals, and J. Dean, "Distilling the knowledge in a neural network," arXiv:1503.02531, 2015.

[446] A. Romero et al., "FitNets: Hints for thin deep nets," in Proc. ICLR, 2015.

[447] T. Elsken, J. H. Metzen, and F. Hutter, "Neural architecture search: A survey," Journal of Machine Learning Research, vol. 20, no. 55, pp. 1-21, 2019.

[448] M. Tan and Q. V. Le, "EfficientNet: Rethinking model scaling for convolutional neural networks," in Proc. ICML, 2019.

[449] S. Teerapittayanon, B. McDanel, and H. T. Kung, "BranchyNet: Fast inference via early exiting from deep neural networks," in Proc. IEEE ICPR, 2016.

[450] X. Wang et al., "SkipNet: Learning dynamic routing in convolutional networks," in Proc. ECCV, 2018.

[451] S. Chetlur et al., "cuDNN: Efficient primitives for deep learning," arXiv:1410.0759, 2014.

[452] N. P. Jouppi et al., "In-datacenter performance analysis of a tensor processing unit," in Proc. ACM ISCA, 2017.

[453] U. Aydonat et al., "An OpenCL deep learning accelerator on Arria 10," in Proc. ACM FPGA, 2017.

[454] Y. Ma et al., "Optimizing loop operation and dataflow in FPGA acceleration of deep convolutional neural networks," in Proc. ACM FPGA, 2017.

[455] Y.-H. Chen, T. Krishna, J. S. Emer, and V. Sze, "Eyeriss: An energy-efficient reconfigurable accelerator for deep convolutional neural networks," IEEE Journal of Solid-State Circuits, vol. 52, no. 1, pp. 127-138, 2017.

[456] E. Wang et al., "Deep neural network approximation for custom hardware: Where we've been, where we're going," ACM Computing Surveys, vol. 52, no. 2, pp. 1-39, 2019.

[457] J. Quionero-Candela et al., Dataset Shift in Machine Learning. MIT Press, 2009.

[458] T. O'Shea, T. Roy, and T. C. Clancy, "Over-the-air deep learning based radio signal classification," IEEE Journal of Selected Topics in Signal Processing, vol. 12, no. 1, pp. 168-179, 2018.

[459] A. Torralba and A. A. Efros, "Unbiased look at dataset bias," in Proc. IEEE CVPR, 2011.

[460] L. Perez and J. Wang, "The effectiveness of data augmentation in image classification using deep learning," arXiv:1712.04621, 2017.

[461] Y. Ganin and V. Lempitsky, "Unsupervised domain adaptation by backpropagation," in Proc. ICML, 2015.

[462] M. Long et al., "Conditional adversarial domain adaptation," in Proc. NeurIPS, 2018.

[463] C. Finn, P. Abbeel, and S. Levine, "Model-agnostic meta-learning for fast adaptation of deep networks," in Proc. ICML, 2017.

[464] T. G. Dietterich, "Ensemble methods in machine learning," in Multiple Classifier Systems. Springer, 2000, pp. 1-15.

[465] D. Hendrycks and T. Dietterich, "Benchmarking neural network robustness to common corruptions and perturbations," in Proc. ICLR, 2019.

[466] Y. Gal, "Uncertainty in deep learning," PhD dissertation, University of Cambridge, 2016.

[467] Y. Gal and Z. Ghahramani, "Dropout as a Bayesian approximation: Representing model uncertainty in deep learning," in Proc. ICML, 2016.

[468] C. Blundell, J. Cornebise, K. Kavukcuoglu, and D. Wierstra, "Weight uncertainty in neural networks," in Proc. ICML, 2015.

[469] C. Szegedy et al., "Intriguing properties of neural networks," in Proc. ICLR, 2014.

[470] M. Sadeghi and E. G. Larsson, "Adversarial attacks on deep-learning based radio signal classification," IEEE Wireless Communications Letters, vol. 8, no. 1, pp. 213-216, 2019.

[471] Y. Shi et al., "Deep learning for massive MIMO channel state acquisition and feedback," Journal of Communications and Information Networks, vol. 5, no. 1, pp. 1-9, 2020.

[472] B. Kim, Y. E. Sagduyu, K. Davaslioglu, T. Erpek, and S. Ulukus, "Over-the-air adversarial attacks on deep learning based modulation classifier over wireless channels," in Proc. IEEE CISS, 2020.

[473] T. Gu, K. Liu, B. Dolan-Gavitt, and S. Garg, "BadNets: Evaluating backdooring attacks on deep neural networks," IEEE Access, vol. 7, pp. 47230-47244, 2019.

[474] A. Madry, A. Makelov, L. Schmidt, D. Tsipras, and A. Vladu, "Towards deep learning models resistant to adversarial attacks," in Proc. ICLR, 2018.

[475] J. Cohen, E. Rosenfeld, and Z. Kolter, "Certified adversarial robustness via randomized smoothing," in Proc. ICML, 2019.

[476] M. Lecuyer et al., "Certified robustness to adversarial examples with differential privacy," in Proc. IEEE S&P, 2019.

[477] R. Feinman, R. R. Curtin, S. Shintre, and A. B. Gardner, "Detecting adversarial samples from artifacts," arXiv:1703.00410, 2017.

[478] N. Papernot, P. McDaniel, I. Goodfellow, S. Jha, Z. B. Celik, and A. Swami, "Practical black-box attacks against machine learning," in Proc. ACM ASIA CCS, 2017.

[479] Y. Shi et al., "Communication-efficient edge AI: Algorithms and systems," IEEE Communications Surveys & Tutorials, vol. 22, no. 4, pp. 2167-2191, 2020.

[480] 3GPP, "Study on artificial intelligence (AI)/machine learning (ML) for NR air interface (Release 17)," 3GPP TR 38.843, 2021.

[481] ONNX Community, "Open Neural Network Exchange," https://onnx.ai/, 2022.

[482] M. S. Sim et al., "Deep learning-based mmWave beam selection for 5G NR/6G with sub-6 GHz channel information: Algorithms and prototype validation," IEEE Access, vol. 8, pp. 51634-51646, 2020.

[483] C. She, C. Sun, Z. Gu, Y. Li, C. Yang, H. V. Poor, and B. Vucetic, "A tutorial on ultrareliable and low-latency communications in 6G: Integrating domain knowledge into deep learning," Proceedings of the IEEE, vol. 109, no. 3, pp. 204-246, 2021.

[484] 3GPP, "Study on enhancement for data collection for NR and EN-DC (Release 17)," 3GPP TR 37.817, 2020.

[485] ONNX, "Open Neural Network Exchange Format," https://onnx.ai/, 2023.

[486] O-RAN Alliance, "O-RAN: Towards an open and smart RAN," O-RAN White Paper, 2018.

[487] P. Muñoz et al., "Optimization of radio and computational resources for energy efficiency in latency-constrained application offloading," IEEE Transactions on Vehicular Technology, vol. 64, no. 10, pp. 4738-4755, 2015.

[488] R. Shokri et al., "Membership inference attacks against machine learning models," in Proc. IEEE S&P, 2017.

[489] R. Shokri and V. Shmatikov, "Privacy-preserving deep learning," in Proc. ACM CCS, 2015.

[490] M. Fredrikson, S. Jha, and T. Ristenpart, "Model inversion attacks that exploit confidence information and basic countermeasures," in Proc. ACM CCS, 2015.

[491] B. Biggio and F. Roli, "Wild patterns: Ten years after the rise of adversarial machine learning," Pattern Recognition, vol. 84, pp. 317-331, 2018.

[492] C. Dwork and A. Roth, "The algorithmic foundations of differential privacy," Foundations and Trends in Theoretical Computer Science, vol. 9, no. 3-4, pp. 211-407, 2014.

[493] M. Abadi et al., "Deep learning with differential privacy," in Proc. ACM CCS, 2016.

[494] N. Papernot, S. Song, I. Mironov, A. Raghunathan, K. Talwar, and Ú. Erlingsson, "Scalable private learning with PATE," in Proc. ICLR, 2018.

[495] J. Konečný, H. B. McMahan, F. X. Yu, P. Richtárik, A. T. Suresh, and D. Bacon, "Federated learning: Strategies for improving communication efficiency," arXiv:1610.05492, 2016.

[496] M. Chen et al., "Distributed learning in wireless networks: Recent progress and future challenges," IEEE Journal on Selected Areas in Communications, vol. 39, no. 12, pp. 3579-3605, 2021.

[497] T. Li, A. K. Sahu, A. Talwalkar, and V. Smith, "Federated learning: Challenges, methods, and future directions," IEEE Signal Processing Magazine, vol. 37, no. 3, pp. 50-60, 2020.

[498] Y. Lindell, "Secure multiparty computation," Communications of the ACM, vol. 64, no. 1, pp. 86-96, 2020.

[499] C. Gentry, "Fully homomorphic encryption using ideal lattices," in Proc. ACM STOC, 2009.

[500] V. Costan and S. Devadas, "Intel SGX explained," IACR Cryptology ePrint Archive, 2016.

[501] Z. C. Lipton, "The mythos of model interpretability," Queue, vol. 16, no. 3, pp. 31-57, 2018.

[502] C. Rudin, "Stop explaining black box machine learning models for high stakes decisions and use interpretable models instead," Nature Machine Intelligence, vol. 1, no. 5, pp. 206-215, 2019.

[503] S. M. Lundberg and S.-I. Lee, "A unified approach to interpreting model predictions," in Proc. NIPS, 2017.

[504] L. S. Shapley, "A value for n-person games," in Contributions to the Theory of Games. Princeton University Press, 1953, vol. 2, pp. 307-317.

[505] M. T. Ribeiro, S. Singh, and C. Guestrin, "Why should I trust you?: Explaining the predictions of any classifier," in Proc. ACM SIGKDD, 2016.

[506] J. Devlin, M.-W. Chang, K. Lee, and K. Toutanova, "BERT: Pre-training of deep bidirectional transformers for language understanding," in Proc. NAACL-HLT, 2019.

[507] D. Erhan et al., "Visualizing higher-layer features of a deep network," University of Montreal, Tech. Rep. 1341, 2009.

[508] G. Hinton, O. Vinyals, and J. Dean, "Distilling the knowledge in a neural network," arXiv:1503.02531, 2015.

[509] E. Strubell, A. Ganesh, and A. McCallum, "Energy and policy considerations for deep learning in NLP," in Proc. ACL, 2019.

[510] R. Schwartz, J. Dodge, N. A. Smith, and O. Etzioni, "Green AI," Communications of the ACM, vol. 63, no. 12, pp. 54-63, 2020.

[511] P. Micikevicius et al., "Mixed precision training," in Proc. ICLR, 2018.

[512] J. Howard and S. Ruder, "Universal language model fine-tuning for text classification," in Proc. ACL, 2018.

[513] H. Liu, K. Simonyan, and Y. Yang, "DARTS: Differentiable architecture search," in Proc. ICLR, 2019.

[514] R. Bommasani et al., "On the opportunities and risks of foundation models," arXiv:2108.07258, 2021.

[515] R. Schwartz et al., "Green AI," Communications of the ACM, vol. 63, no. 12, pp. 54-63, 2020.

[516] W. Shi, J. Cao, Q. Zhang, Y. Li, and L. Xu, "Edge computing: Vision and challenges," IEEE Internet of Things Journal, vol. 3, no. 5, pp. 637-646, 2016.

[517] R. Bommasani et al., "On the opportunities and risks of foundation models," arXiv:2108.07258, 2021.

[518] Z. Wang et al., "Foundation model for wireless communications: A survey," arXiv:2311.06018, 2023.

[519] A. Dosovitskiy et al., "An image is worth 16x16 words: Transformers for image recognition at scale," in Proc. ICLR, 2021.

[520] Z. Dai et al., "Transformer-XL: Attentive language models beyond a fixed-length context," in Proc. ACL, 2019.

[521] J. Zbontar et al., "Barlow twins: Self-supervised learning via redundancy reduction," in Proc. ICML, 2021.

[522] K. He, X. Chen, S. Xie, Y. Li, P. Dollár, and R. Girshick, "Masked autoencoders are scalable vision learners," in Proc. IEEE CVPR, 2022.

[523] A. D. Wyner, "The wire-tap channel," Bell System Technical Journal, vol. 54, no. 8, pp. 1355-1387, 1975.

[524] K. Merchant et al., "Deep learning for RF device fingerprinting in cognitive communication systems," IEEE Journal of Selected Topics in Signal Processing, vol. 12, no. 1, pp. 160-167, 2018.

[525] B. Jeon, M. Jeon, B. Koo, E. Hong, and D. Shin, "Blind detection of beamforming using reinforcement learning," in Proc. IEEE ICAIIC, 2020.

[526] J. Biamonte et al., "Quantum machine learning," Nature, vol. 549, pp. 195-202, 2017.

[527] M. Schuld, I. Sinayskiy, and F. Petruccione, "An introduction to quantum machine learning," Contemporary Physics, vol. 56, no. 2, pp. 172-185, 2015.

[528] S. Aaronson, "Read the fine print," Nature Physics, vol. 11, no. 4, pp. 291-293, 2015.

[529] C. D. Schuman et al., "A survey of neuromorphic computing and neural networks in hardware," arXiv:1705.06963, 2017.

[530] W. Maass, "Networks of spiking neurons: The third generation of neural network models," Neural Networks, vol. 10, no. 9, pp. 1659-1671, 1997.

[531] M. Davies et al., "Loihi: A neuromorphic manycore processor with on-chip learning," IEEE Micro, vol. 38, no. 1, pp. 82-99, 2018.

[532] G. I. Parisi, R. Kemker, J. L. Part, C. Kanan, and S. Wermter, "Continual lifelong learning with neural networks: A review," Neural Networks, vol. 113, pp. 54-71, 2019.

[533] J. Kirkpatrick et al., "Overcoming catastrophic forgetting in neural networks," Proceedings of the National Academy of Sciences, vol. 114, no. 13, pp. 3521-3526, 2017.

[534] A. A. Rusu et al., "Progressive neural networks," arXiv:1606.04671, 2016.

[535] Z. Chen and B. Liu, "Lifelong machine learning," Synthesis Lectures on Artificial Intelligence and Machine Learning, vol. 12, no. 3, pp. 1-207, 2018.

[536] O-RAN Alliance, "O-RAN architecture description," O-RAN Technical Specification, 2021.

[537] M. Polese et al., "Understanding O-RAN: Architecture, interfaces, algorithms, security, and research challenges," IEEE Communications Surveys & Tutorials, vol. 25, no. 2, pp. 1376-1411, 2023.

[538] A. Lacava et al., "Programmable and customized intelligence for traffic steering in 5G networks using open RAN architectures," IEEE Transactions on Mobile Computing, vol. 22, no. 7, pp. 4038-4055, 2023.

[539] O-RAN Alliance, "O-RAN use cases and deployment scenarios," O-RAN White Paper, 2020.

[540] I. F. Akyildiz, A. Kak, an