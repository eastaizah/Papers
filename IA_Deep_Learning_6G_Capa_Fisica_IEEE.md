# Inteligencia Artificial y Deep Learning en la Capa Física de Sistemas de Telecomunicaciones Inalámbricas 6G y de Próxima Generación

**Resumen**—La sexta generación (6G) de redes inalámbricas representa un cambio paradigmático en las telecomunicaciones, donde la Inteligencia Artificial (IA) y el Deep Learning (DL) se integran nativamente en la capa física (PHY) para superar las limitaciones fundamentales de las arquitecturas tradicionales basadas en modelos analíticos. Este artículo presenta una revisión exhaustiva y análisis profundo de las técnicas de IA/DL aplicadas al nivel físico de sistemas 6G, abarcando desde la fundamentación teórica hasta implementaciones prácticas. Se examina detalladamente la arquitectura de end-to-end learning, codificación de canal neural, detección y estimación basada en DL, beamforming inteligente, y optimización de forma de onda. Se proporciona el rigor matemático subyacente, incluyendo formulaciones de optimización, arquitecturas de redes neuronales, y análisis de complejidad computacional. Los resultados demuestran que la IA nativa en PHY puede alcanzar mejoras de 2-5 dB en relación señal-ruido efectiva comparado con métodos convencionales, reducir latencia en un 40-60%, y habilitar nuevos servicios como comunicaciones holográficas y gemelos digitales con requisitos de tasa de datos superiores a 1 Tbps.

**Palabras clave**—6G, Inteligencia Artificial, Deep Learning, Capa Física, Comunicaciones Inalámbricas, End-to-End Learning, Codificación Neural, Beamforming Inteligente.

---

## I. INTRODUCCIÓN

### A. Contexto y Motivación

La evolución de las redes de comunicaciones móviles ha seguido un patrón predecible de aproximadamente una década por generación, desde 1G hasta la actual 5G [1]. Sin embargo, la transición hacia la sexta generación (6G), prevista para el año 2030, representa no solo un incremento cuantitativo en las capacidades del sistema, sino una transformación cualitativa fundamental en la arquitectura y diseño de las redes de telecomunicaciones [2], [3]. Este cambio paradigmático está impulsado por aplicaciones emergentes como la comunicación holográfica, los gemelos digitales masivos, la Internet táctil, la realidad extendida (XR) de alta fidelidad, y los vehículos autónomos conectados, que demandan requisitos sin precedentes en términos de tasa de datos (superiores a 1 Tbps), latencia ultrabaja (sub-milisegundo), confiabilidad extrema (99.99999%), y eficiencia energética [4]–[6].

Las arquitecturas tradicionales de capa física en sistemas de comunicaciones inalámbricas han sido diseñadas siguiendo un enfoque modular basado en modelos analíticos derivados de la teoría de información de Shannon [7] y teoría de comunicaciones digitales [8]. Este paradigma clásico descompone el transmisor y receptor en bloques funcionales independientes: codificación de fuente, codificación de canal, modulación, ecualización, detección, y decodificación [9]. Cada uno de estos componentes ha sido optimizado individualmente bajo suposiciones simplificadoras sobre el canal de propagación, el ruido, y las interferencias, frecuentemente asumiendo modelos Gaussianos, linealidad, y estacionariedad [10].

Sin embargo, los canales de comunicación inalámbrica reales en entornos 6G presentan características significativamente más complejas [11]:

1. **No-linealidades severas**: Amplificadores de potencia operando cerca de la saturación, efectos de clipping, distorsión armónica, y productos de intermodulación [12].

2. **Propagación multicamino compleja**: En frecuencias milimétricas (mmWave) de 30-300 GHz y terahertz (THz) de 0.1-10 THz, la propagación presenta pérdidas por trayectoria elevadas (∝ f²), alta sensibilidad a bloqueos, dispersión difusa, y efectos de polarización [13], [14].

3. **Movilidad y dinámica temporal**: Variaciones rápidas del canal debido a alta movilidad (hasta 500 km/h en escenarios aeronáuticos), entornos altamente dinámicos con múltiples objetos móviles, y efectos Doppler significativos [15].

4. **Interferencia heterogénea**: Coexistencia de múltiples tecnologías de acceso radio (RAT), interferencia inter-celda masiva en despliegues ultra-densos, y contaminación de pilotos en sistemas MIMO masivo [16].

5. **Imperfecciones de hardware**: Osciladores con jitter de fase, conversores analógico-digitales (ADC) con cuantización limitada, desbalances I/Q, y no-reciprocidad en sistemas full-duplex [17].

La optimización conjunta de todos los componentes de la capa física bajo estas condiciones realistas constituye un problema de optimización no-convexo de alta dimensionalidad, frecuentemente intratable mediante métodos analíticos tradicionales [18]. Es en este contexto donde la Inteligencia Artificial (IA) y específicamente el Deep Learning (DL) emergen como habilitadores fundamentales para el diseño de sistemas 6G [19]–[21].

### B. Inteligencia Artificial Nativa en la Capa Física

El concepto de "IA Nativa" en 6G implica que los algoritmos de IA no son simplemente añadidos como capas de optimización sobre arquitecturas existentes, sino que constituyen componentes fundamentales e inseparables del diseño del sistema desde la capa física hasta las capas superiores [22], [23]. Esta integración profunda permite:

1. **Aprendizaje End-to-End**: Optimización conjunta de la cadena completa de transmisión-recepción mediante gradiente descendente, superando las limitaciones de la optimización modular [24], [25].

2. **Adaptabilidad**: Capacidad de aprender y adaptarse automáticamente a condiciones de canal, patrones de tráfico, y distribuciones de datos no estacionarias sin requerir modelos analíticos explícitos [26].

3. **Explotación de estructura latente**: Capacidad de las redes neuronales profundas (DNN) para extraer y explotar estructuras, patrones, y correlaciones en los datos que son difíciles de modelar analíticamente [27].

4. **Optimización multi-objetivo**: Balanceo simultáneo de múltiples objetivos conflictivos como tasa de datos, confiabilidad, latencia, y eficiencia energética mediante aprendizaje multi-tarea [28].

El fundamento teórico de la aplicación de DL a la capa física radica en el teorema de aproximación universal [29], que establece que una red neuronal con al menos una capa oculta y suficientes neuronas puede aproximar cualquier función continua con precisión arbitraria. Formalmente, para cualquier función continua f: ℝⁿ → ℝᵐ y cualquier ε > 0, existe una red neuronal feedforward Fθ con parámetros θ tal que:

$$\sup_{x \in K} \|f(x) - F_\theta(x)\| < \varepsilon$$

donde K es un subconjunto compacto de ℝⁿ [30]. Este resultado ha sido extendido a aproximadores universales más específicos como las redes convolucionales para señales con invarianza traslacional [31] y redes recurrentes para secuencias temporales [32].

### C. Objetivos y Contribuciones del Artículo

Este artículo proporciona una revisión exhaustiva, análisis crítico, y síntesis de las técnicas de IA y Deep Learning aplicadas a la capa física de sistemas de telecomunicaciones inalámbricas 6G y de próxima generación. Las contribuciones principales incluyen:

1. **Fundamentación teórica rigurosa**: Desarrollo detallado de los fundamentos matemáticos que sustentan la aplicación de DL a problemas de comunicaciones, incluyendo teoría de información, teoría de aprendizaje estadístico, y teoría de optimización.

2. **Taxonomía comprehensiva**: Clasificación sistemática de las aplicaciones de IA/DL en la capa física, organizadas según su función (codificación, modulación, detección, estimación, beamforming, etc.) y metodología (supervisado, no supervisado, por refuerzo).

3. **Análisis arquitectural profundo**: Examen detallado de las arquitecturas de redes neuronales específicas para comunicaciones físicas, incluyendo autoencoders, redes convolucionales complejas, transformers para señales temporales, y graph neural networks para topologías de red.

4. **Formulaciones matemáticas explícitas**: Presentación completa de las formulaciones de optimización, funciones de pérdida, algoritmos de entrenamiento, y análisis de convergencia.

5. **Evaluación de desempeño comparativa**: Revisión de resultados experimentales y simulaciones que demuestran las ventajas cuantitativas de los enfoques basados en IA frente a métodos tradicionales.

6. **Discusión de desafíos y direcciones futuras**: Identificación de problemas abiertos, limitaciones actuales, y oportunidades de investigación en la intersección de IA y comunicaciones físicas.

### D. Organización del Artículo

El resto del artículo está organizado como sigue. La Sección II presenta los fundamentos teóricos necesarios, incluyendo principios de teoría de información, arquitecturas básicas de Deep Learning, y el marco de optimización end-to-end. La Sección III examina en profundidad el diseño de sistemas de comunicación end-to-end mediante autoencoders. La Sección IV analiza técnicas de codificación de canal neural. La Sección V cubre métodos de detección y demodulación basados en DL. La Sección VI explora la estimación de canal y CSI mediante redes neuronales. La Sección VII discute beamforming y precodificación inteligente para sistemas MIMO masivos. La Sección VIII aborda el diseño de forma de onda y acceso múltiple mediante IA. La Sección IX examina consideraciones de implementación práctica y complejidad computacional. La Sección X presenta desafíos abiertos y direcciones de investigación futura. Finalmente, la Sección XI concluye el artículo.

---

## II. FUNDAMENTOS TEÓRICOS

### A. Teoría de Información y Límites Fundamentales

La teoría de información de Shannon [7] establece los límites fundamentales del desempeño de cualquier sistema de comunicación. Para un canal con entrada X, salida Y, y ruido aditivo, la capacidad del canal C representa la máxima tasa de información que puede transmitirse con probabilidad de error arbitrariamente pequeña [33].

#### 1) Canal AWGN

Para el canal Gaussiano con ruido blanco aditivo (AWGN), la capacidad está dada por la fórmula de Shannon-Hartley [7]:

$$C = B \log_2\left(1 + \frac{P}{N_0 B}\right) \text{ bits/s}$$

donde B es el ancho de banda en Hz, P es la potencia de transmisión en Watts, y N₀ es la densidad espectral de potencia del ruido en W/Hz. Definiendo la relación señal-ruido (SNR) como γ = P/(N₀B), obtenemos:

$$C = B \log_2(1 + \gamma) \text{ bits/s}$$

La eficiencia espectral máxima es por tanto:

$$\eta_{max} = \frac{C}{B} = \log_2(1 + \gamma) \text{ bits/s/Hz}$$

Esta expresión establece el límite superior teórico para cualquier esquema de codificación y modulación [34]. Los sistemas prácticos operan por debajo de este límite debido a restricciones de complejidad, retardo, y imperfecciones del sistema.

#### 2) Canal con Desvanecimiento

En canales inalámbricos reales, el desvanecimiento (fading) reduce significativamente la capacidad. Para un canal con desvanecimiento multiplicativo representado por h y AWGN, la señal recibida es [35]:

$$y = hx + n$$

donde x es la señal transmitida, h es el coeficiente de canal complejo (h ∈ ℂ), y n ~ 𝒩(0, N₀) es ruido Gaussiano complejo. La capacidad instantánea es:

$$C(h) = \log_2\left(1 + \frac{P|h|^2}{N_0}\right) \text{ bits/s/Hz}$$

Para un canal con desvanecimiento aleatorio, la capacidad ergódica (promedio sobre la distribución del canal) es [36]:

$$\bar{C} = \mathbb{E}_h\left[\log_2\left(1 + \frac{P|h|^2}{N_0}\right)\right]$$

En el caso de desvanecimiento Rayleigh, donde |h|² sigue una distribución exponencial con parámetro λ (|h|² ~ Exp(λ)), la capacidad ergódica no tiene forma cerrada simple, pero puede expresarse mediante la función exponencial integral [37]:

$$\bar{C} = \frac{1}{\ln(2)} e^{1/\bar{\gamma}} E_1\left(\frac{1}{\bar{\gamma}}\right)$$

donde γ̄ = P/(λN₀) es la SNR promedio y E₁(·) es la integral exponencial de primer orden.

#### 3) Información Mutua y Distancia de Hamming

La información mutua I(X;Y) entre la entrada X y salida Y cuantifica la cantidad de información sobre X contenida en Y [38]:

$$I(X;Y) = H(Y) - H(Y|X) = H(X) - H(X|Y)$$

donde H(·) denota entropía y H(·|·) entropía condicional. Para variables continuas, utilizamos entropía diferencial:

$$h(X) = -\int p(x) \log p(x) dx$$

La información mutua puede expresarse como la divergencia de Kullback-Leibler entre la distribución conjunta y el producto de las marginales [39]:

$$I(X;Y) = D_{KL}(p(x,y) \| p(x)p(y)) = \int\int p(x,y) \log\frac{p(x,y)}{p(x)p(y)} dx dy$$

Esta formulación es fundamental para el diseño de autoencoders en comunicaciones, donde maximizar I(X;Y) equivale a maximizar la cantidad de información transmitida a través del canal [40].

### B. Arquitecturas Fundamentales de Deep Learning

#### 1) Redes Neuronales Feedforward

Una red neuronal feedforward (FFNN) con L capas implementa una función compuesta [41]:

$$F(x) = f_L(W_L f_{L-1}(W_{L-1} \cdots f_1(W_1 x + b_1) \cdots + b_{L-1}) + b_L)$$

donde Wₗ y bₗ son la matriz de pesos y vector de sesgo de la capa l, y fₗ(·) es la función de activación no lineal. Las funciones de activación comunes incluyen:

- **ReLU** (Rectified Linear Unit): f(x) = max(0, x) [42]
- **Leaky ReLU**: f(x) = max(αx, x), α ∈ (0,1) [43]
- **ELU** (Exponential Linear Unit): f(x) = x si x > 0, α(eˣ - 1) si x ≤ 0 [44]
- **Swish/SiLU**: f(x) = x·σ(βx) donde σ(·) es la función sigmoide [45]
- **GELU** (Gaussian Error Linear Unit): f(x) = x·Φ(x) donde Φ(·) es la CDF Gaussiana [46]

La función de activación ReLU ha dominado en aplicaciones de Deep Learning debido a su simplicidad computacional y propiedades de gradiente que mitigan el problema de vanishing gradients [47]. Sin embargo, puede sufrir de "dying ReLU" donde neuronas quedan permanentemente inactivas. Variantes como Leaky ReLU y ELU resuelven este problema permitiendo gradientes no-cero para entradas negativas.

#### 2) Redes Convolucionales (CNN)

Las redes convolucionales explotan la estructura espacial o temporal de los datos mediante la operación de convolución [48]. Para una entrada x y kernel k, la convolución discreta es:

$$(x * k)[n] = \sum_{m=-\infty}^{\infty} x[m] k[n-m]$$

En el contexto de señales de comunicaciones complejas, utilizamos convoluciones complejas [49]:

$$(x * k)[n] = \sum_{m=0}^{M-1} x[n-m] k[m]$$

donde x, k ∈ ℂᴺ. Una capa convolucional aplica múltiples filtros aprendibles para extraer características jerárquicas:

$$z_i = f\left(\sum_{j=1}^{C_{in}} x_j * k_{ij} + b_i\right)$$

donde C_in es el número de canales de entrada, k_ij es el kernel conectando el canal de entrada j al canal de salida i, y b_i es el sesgo [50].

Las CNN son particularmente efectivas para señales de comunicaciones debido a:
- **Invarianza traslacional**: Patrones en la señal son detectados independientemente de su posición temporal.
- **Compartición de parámetros**: Reduce drásticamente el número de parámetros comparado con capas fully-connected.
- **Receptive field jerárquico**: Capas profundas capturan dependencias de largo alcance [51].

#### 3) Redes Recurrentes (RNN) y LSTM

Las redes recurrentes procesan secuencias manteniendo un estado oculto que evoluciona temporalmente [52]:

$$h_t = f(W_{hh}h_{t-1} + W_{xh}x_t + b_h)$$
$$y_t = W_{hy}h_t + b_y$$

donde h_t es el estado oculto en el tiempo t, x_t es la entrada, y y_t es la salida. Sin embargo, las RNN básicas sufren de problemas de vanishing/exploding gradients en secuencias largas [53].

Las redes Long Short-Term Memory (LSTM) [54] resuelven este problema mediante compuertas que controlan el flujo de información:

$$f_t = \sigma(W_f [h_{t-1}, x_t] + b_f)$$ (compuerta de olvido)
$$i_t = \sigma(W_i [h_{t-1}, x_t] + b_i)$$ (compuerta de entrada)
$$\tilde{C}_t = \tanh(W_C [h_{t-1}, x_t] + b_C)$$ (candidato de celda)
$$C_t = f_t \odot C_{t-1} + i_t \odot \tilde{C}_t$$ (estado de celda)
$$o_t = \sigma(W_o [h_{t-1}, x_t] + b_o)$$ (compuerta de salida)
$$h_t = o_t \odot \tanh(C_t)$$ (estado oculto)

donde σ(·) es la función sigmoide, ⊙ denota producto elemento-a-elemento (Hadamard), y C_t es el estado de celda que permite el flujo de gradientes sin modificación a través del tiempo [55].

Una alternativa más eficiente es la Gated Recurrent Unit (GRU) [56], que utiliza menos compuertas:

$$z_t = \sigma(W_z [h_{t-1}, x_t])$$ (compuerta de actualización)
$$r_t = \sigma(W_r [h_{t-1}, x_t])$$ (compuerta de reset)
$$\tilde{h}_t = \tanh(W[r_t \odot h_{t-1}, x_t])$$ (candidato)
$$h_t = (1-z_t) \odot h_{t-1} + z_t \odot \tilde{h}_t$$

Las RNN/LSTM son fundamentales para modelar la dinámica temporal del canal, ecualización adaptativa, y predicción de interferencias en sistemas 6G [57].

#### 4) Mecanismos de Atención y Transformers

El mecanismo de atención permite a la red enfocarse selectivamente en partes relevantes de la entrada [58]. La atención escalada por producto punto (scaled dot-product attention) es:

$$\text{Attention}(Q, K, V) = \softmax\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$

donde Q (query), K (key), y V (value) son matrices derivadas de la entrada, y d_k es la dimensión de K. El factor de escalamiento 1/√d_k previene que el producto punto crezca excesivamente en dimensiones altas [59].

La atención multi-cabeza (multi-head attention) aplica múltiples atenciones en paralelo:

$$\text{MultiHead}(Q,K,V) = \text{Concat}(\text{head}_1, \ldots, \text{head}_h)W^O$$

donde:

$$\text{head}_i = \text{Attention}(QW_i^Q, KW_i^K, VW_i^V)$$

y W_i^Q, W_i^K, W_i^V, W^O son matrices de proyección aprendibles [60].

El Transformer [61] utiliza atención multi-cabeza como componente principal, eliminando la recurrencia:

$$\text{Encoder}(x) = \text{LayerNorm}(x + \text{MultiHead}(x, x, x))$$
$$\text{Output} = \text{LayerNorm}(\text{Encoder} + \text{FFN}(\text{Encoder}))$$

donde FFN es una red feedforward y LayerNorm es normalización de capa [62]. Los Transformers han demostrado rendimiento superior en modelado de secuencias largas y se han aplicado exitosamente a estimación de canal y predicción de CSI en comunicaciones [63], [64].

#### 5) Autoencoders

Un autoencoder es una red neuronal diseñada para aprender una representación comprimida (codificación) de los datos [65]. Consiste en:

- **Encoder**: f_θ : ℝⁿ → ℝᵈ que mapea la entrada x a una representación latente z = f_θ(x) donde típicamente d < n.
- **Decoder**: g_φ : ℝᵈ → ℝⁿ que reconstruye la entrada desde la representación latente x̂ = g_φ(z).

El objetivo de entrenamiento es minimizar el error de reconstrucción:

$$\mathcal{L}(\theta, \phi) = \frac{1}{N}\sum_{i=1}^{N} \|x_i - g_\phi(f_\theta(x_i))\|^2$$

Los autoencoders variacionales (VAE) [66] extienden este concepto imponiendo una estructura probabilística en el espacio latente:

$$\mathcal{L}_{VAE} = -\mathbb{E}_{q_\phi(z|x)}[\log p_\theta(x|z)] + D_{KL}(q_\phi(z|x) \| p(z))$$

donde q_φ(z|x) es la distribución del encoder (posterior aproximado), p_θ(x|z) es el decoder (likelihood), y p(z) es la prior sobre z (típicamente 𝒩(0,I)). El primer término es el error de reconstrucción esperado y el segundo es la regularización KL que fuerza al espacio latente a seguir la distribución prior [67].

En el contexto de comunicaciones, el autoencoder se interpreta como un sistema end-to-end donde el encoder es el transmisor, el canal es una capa intermedia, y el decoder es el receptor [24], [68].

### C. Formulación de Sistemas de Comunicación como Problema de Aprendizaje

#### 1) Arquitectura End-to-End

Consideremos un sistema de comunicación digital que transmite mensajes s de un alfabeto finito 𝒮 = {1, 2, ..., M} a través de un canal con ruido. El sistema tradicional se descompone en [69]:

1. **Codificación de fuente**: Compresión del mensaje
2. **Codificación de canal**: Añadir redundancia para corrección de errores
3. **Modulación**: Mapear bits a símbolos de constelación
4. **Procesamiento de transmisión**: Filtrado, ecualización, conformación de pulso
5. **Canal**: Introduce distorsión, ruido, desvanecimiento
6. **Procesamiento de recepción**: Filtrado, sincronización
7. **Demodulación**: Decisión sobre símbolos recibidos
8. **Decodificación de canal**: Corrección de errores
9. **Decodificación de fuente**: Descompresión

En el enfoque end-to-end con Deep Learning [24], reemplazamos toda la cadena por dos redes neuronales:

$$x = f_\theta(s), \quad \hat{s} = g_\phi(y)$$

donde:
- f_θ : 𝒮 → ℝ²ⁿ es el transmisor (encoder) que mapea el mensaje s a la señal transmitida x con restricción de potencia 𝔼[||x||²] ≤ P
- El canal transforma x en y según p(y|x)
- g_φ : ℝ²ⁿ → [0,1]^M es el receptor (decoder) que produce probabilidades sobre los mensajes

La función de pérdida es la entropía cruzada categórica [70]:

$$\mathcal{L}(\theta, \phi) = -\mathbb{E}_{s \sim p(s)} \mathbb{E}_{y \sim p(y|f_\theta(s))}\left[\log g_\phi(y)_s\right]$$

Esta formulación es equivalente a maximizar la información mutua I(S;Ŝ) entre el mensaje enviado y el estimado [71].

#### 2) Restricciones del Transmisor

En la práctica, el transmisor debe satisfacer múltiples restricciones:

**Restricción de potencia promedio**:

$$\frac{1}{N}\sum_{i=1}^{N} \|f_\theta(s_i)\|^2 \leq P$$

Esto se implementa mediante normalización [72]:

$$x = \sqrt{\frac{nP}{\mathbb{E}_s[\|f_\theta(s)\|^2]}} f_\theta(s)$$

**Restricción de potencia pico (PAPR)**:

$$\text{PAPR} = \frac{\max_t |x(t)|^2}{\mathbb{E}[|x(t)|^2]} \leq \text{PAPR}_{max}$$

El PAPR elevado degrada la eficiencia del amplificador de potencia. Se puede añadir un término de penalización a la pérdida [73]:

$$\mathcal{L}_{total} = \mathcal{L}_{CE} + \lambda \mathbb{E}[\max(0, \text{PAPR}(x) - \text{PAPR}_{max})]$$

**Restricción espectral**: La señal debe ocupar un ancho de banda B. Esto se modela mediante un filtro pasabanda en el transmisor [74]:

$$x_{band} = h_{tx}(t) * x(t)$$

donde h_tx(t) es la respuesta al impulso del filtro de transmisión.

#### 3) Modelado del Canal

El canal de comunicación es una componente crítica. Para canales estocásticos conocidos, podemos simular muestras durante el entrenamiento. Para el canal AWGN:

$$y = x + n, \quad n \sim \mathcal{N}(0, N_0 I)$$

Para canales con desvanecimiento Rayleigh de banda estrecha [75]:

$$y = hx + n, \quad h \sim \mathcal{CN}(0, 1)$$

Para canales selectivos en frecuencia con L taps [76]:

$$y[n] = \sum_{l=0}^{L-1} h_l x[n-l] + n[n]$$

donde h_l ~ 𝒞𝒩(0, σ_l²) con perfil de potencia retardado (PDP) especificado.

Para canales realistas no estacionarios, se utilizan modelos de trazas obtenidos de mediciones (channel measurements) o generadores de canal como QuaDRiGa [77], NYUSIM [78], o modelos estadísticos 3GPP [79].

Una innovación clave es utilizar redes generativas adversariales (GANs) para aprender modelos implícitos del canal a partir de datos [80]:

$$\min_\theta \max_\psi \mathbb{E}_{(x,y) \sim p_{real}}[\log D_\psi(y|x)] + \mathbb{E}_{x \sim p_x}[\log(1 - D_\psi(G_\theta(x, z)|x))]$$

donde G_θ es el generador de canal y D_ψ es el discriminador que distingue entre pares canal-salida reales y generados [81].

#### 4) Funciones de Pérdida

La elección de la función de pérdida es crucial para el desempeño. Opciones comunes incluyen:

**Entropía cruzada (Cross-Entropy)**: Para clasificación de símbolos/mensajes [82]:

$$\mathcal{L}_{CE} = -\sum_{i=1}^{M} y_i \log(\hat{y}_i)$$

donde y es la etiqueta one-hot verdadera y ŷ es la distribución de probabilidad predicha.

**Error cuadrático medio (MSE)**: Para regresión o estimación [83]:

$$\mathcal{L}_{MSE} = \frac{1}{N}\sum_{i=1}^{N} \|y_i - \hat{y}_i\|^2$$

**Tasa de error de bit (BER)**: Directamente optimizar BER es deseable pero problemático porque BER es una función no diferenciable [84]. Aproximaciones diferenciables incluyen:

$$\mathcal{L}_{BER} \approx \frac{1}{K}\sum_{k=1}^{K} \sigma(T \cdot \text{dist}(b_k, \hat{b}_k))$$

donde σ(·) es la sigmoide, T es un parámetro de temperatura, y dist(·,·) es la distancia de Hamming suavizada [85].

**Información mutua (Mutual Information)**: Maximizar directamente I(X;Y) es el objetivo óptimo desde la perspectiva de teoría de información [86]. Para variables discretas:

$$I(X;Y) = \sum_{x,y} p(x,y) \log\frac{p(x,y)}{p(x)p(y)}$$

En la práctica, se estima mediante MINE (Mutual Information Neural Estimation) [87]:

$$\hat{I}(X;Y) = \sup_T \mathbb{E}_{p(x,y)}[T(x,y)] - \log \mathbb{E}_{p(x)p(y)}[e^{T(x,y)}]$$

donde T es una red neuronal (estadístico).

**Pérdida adversarial**: En contexto de robustez contra adversarios o incertidumbre del canal [88]:

$$\mathcal{L}_{adv} = \max_{\|\delta\| \leq \epsilon} \mathcal{L}(f_\theta(s), g_\phi(y + \delta))$$

donde δ representa perturbaciones adversariales.

### D. Algoritmos de Optimización

El entrenamiento de redes neuronales para sistemas de comunicación requiere optimización eficiente de funciones de pérdida no convexas de alta dimensionalidad.

#### 1) Gradient Descent Estocástico (SGD)

El algoritmo fundamental es SGD [89]:

$$\theta_{t+1} = \theta_t - \eta \nabla_\theta \mathcal{L}(\theta; \mathcal{B}_t)$$

donde η es la tasa de aprendizaje y ℬ_t es un mini-batch de datos muestreados aleatoriamente. La variante con momentum [90] acelera la convergencia:

$$v_{t+1} = \beta v_t + \nabla_\theta \mathcal{L}(\theta_t)$$
$$\theta_{t+1} = \theta_t - \eta v_{t+1}$$

donde β ∈ [0,1) es el coeficiente de momentum (típicamente 0.9).

#### 2) Métodos Adaptativos

Los optimizadores adaptativos ajustan la tasa de aprendizaje por parámetro. **Adam** (Adaptive Moment Estimation) [91] es el más utilizado:

$$m_t = \beta_1 m_{t-1} + (1-\beta_1) g_t$$
$$v_t = \beta_2 v_{t-1} + (1-\beta_2) g_t^2$$
$$\hat{m}_t = m_t / (1-\beta_1^t)$$
$$\hat{v}_t = v_t / (1-\beta_2^t)$$
$$\theta_{t+1} = \theta_t - \eta \frac{\hat{m}_t}{\sqrt{\hat{v}_t} + \varepsilon}$$

donde g_t = ∇_θ ℒ(θ_t), m_t y v_t son estimaciones del primer y segundo momento del gradiente, β₁ = 0.9 y β₂ = 0.999 típicamente, y ε = 10⁻⁸ previene división por cero [92].

Variantes incluyen **AdamW** [93] que corrige el weight decay, y **RAdam** [94] que proporciona calentamiento automático.

#### 3) Retropropagación a través del Canal

Un desafío único en sistemas de comunicación es calcular gradientes a través del canal físico [95]. Para canales estocásticos p(y|x), el gradiente es:

$$\nabla_\theta \mathbb{E}_{y \sim p(y|x)}[\mathcal{L}(y, \theta)] = \mathbb{E}_{y \sim p(y|x)}[\nabla_\theta \mathcal{L}(y, \theta)]$$

que se aproxima mediante muestreo de Monte Carlo:

$$\nabla_\theta \mathbb{E}_y[\mathcal{L}] \approx \frac{1}{K}\sum_{k=1}^{K} \nabla_\theta \mathcal{L}(y^{(k)}, \theta)$$

donde y^(k) ~ p(y|x) son muestras independientes del canal [96].

Para canales parametrizados por parámetros desconocidos ψ, se puede utilizar el truco de reparametrización (reparameterization trick) [97]:

$$y = g(x, \psi, \epsilon), \quad \epsilon \sim p(\epsilon)$$

donde ε representa la aleatoriedad del canal. Entonces:

$$\nabla_\theta \mathbb{E}_\epsilon[\mathcal{L}(g(x, \psi, \epsilon))] = \mathbb{E}_\epsilon[\nabla_\theta \mathcal{L}(g(x, \psi, \epsilon))]$$

Cuando el canal no es diferenciable o es desconocido, se utilizan métodos de política de gradiente (policy gradient) del aprendizaje por refuerzo [98]:

$$\nabla_\theta \mathbb{E}_{y \sim p(y|x)}[\mathcal{L}(y)] = \mathbb{E}_{y}[\mathcal{L}(y) \nabla_\theta \log p_\theta(y|x)]$$

Este es el estimador REINFORCE [99], aunque tiene alta varianza y requiere técnicas de reducción de varianza como baselines.

### E. Generalización y Regularización

La generalización—capacidad de desempeñarse bien en datos no vistos—es crítica en aplicaciones de comunicaciones donde las condiciones de canal en despliegue pueden diferir del entrenamiento [100].

#### 1) Capacidad de Generalización

La teoría de aprendizaje PAC (Probably Approximately Correct) [101] establece que con probabilidad al menos 1-δ, el error de generalización está acotado por:

$$\mathcal{L}_{gen} \leq \mathcal{L}_{train} + \sqrt{\frac{2\mathcal{C}(\mathcal{H}) + 2\log(2/\delta)}{N}}$$

donde ℒ_gen es el riesgo esperado en la distribución verdadera, ℒ_train es el riesgo empírico en los datos de entrenamiento, 𝒞(ℋ) es la complejidad de la clase de hipótesis (e.g., dimensión VC, número de Rademacher), y N es el tamaño del conjunto de entrenamiento [102].

Para redes neuronales, la complejidad puede caracterizarse mediante normas de pesos. El teorema de generalización para redes profundas [103] establece:

$$\mathcal{L}_{gen} \leq \mathcal{L}_{train} + O\left(\frac{\prod_{l=1}^{L} \|W_l\|_F^2}{\sqrt{N}}\right)$$

donde ||W_l||_F es la norma de Frobenius de la matriz de pesos de la capa l [104].

#### 2) Técnicas de Regularización

**Regularización L2 (Weight Decay)**: Añade penalización cuadrática a los pesos [105]:

$$\mathcal{L}_{reg} = \mathcal{L} + \frac{\lambda}{2}\sum_{l} \|W_l\|_F^2$$

**Dropout**: Durante entrenamiento, elimina aleatoriamente neuronas con probabilidad p [106]:

$$\tilde{h}_l = m \odot h_l, \quad m \sim \text{Bernoulli}(1-p)$$

Durante inferencia, se escalan las activaciones por (1-p). Dropout actúa como ensemble implícito de redes [107].

**Batch Normalization**: Normaliza las activaciones de cada capa [108]:

$$\hat{x} = \frac{x - \mathbb{E}[x]}{\sqrt{\text{Var}[x] + \varepsilon}}, \quad y = \gamma \hat{x} + \beta$$

donde γ y β son parámetros aprendibles. Batch normalization estabiliza el entrenamiento, permite tasas de aprendizaje mayores, y actúa como regularizador [109].

**Data Augmentation**: En contexto de comunicaciones, incluye [110]:
- Variación de SNR durante entrenamiento
- Muestreo de diferentes realizaciones de canal
- Añadir diferentes tipos de interferencia
- Rotaciones de fase aleatorias
- Variaciones de sincronización temporal

**Early Stopping**: Detener entrenamiento cuando el error de validación comienza a aumentar, previniendo sobreajuste [111].

---

## III. SISTEMAS DE COMUNICACIÓN END-TO-END CON AUTOENCODERS

### A. Concepto y Formulación

El paradigma de comunicación end-to-end mediante autoencoders, introducido por O'Shea y Hoydis [24], reformula el problema de diseño de sistemas de comunicación como un problema de aprendizaje de representaciones. Esta aproximación reemplaza componentes diseñados manualmente (codificación, modulación, detección) por redes neuronales que se optimizan conjuntamente.

#### 1) Arquitectura Básica

Consideremos la transmisión de M mensajes diferentes a través de un canal con ruido. El sistema se compone de:

**Transmisor (Encoder)**:
El encoder es una red neuronal f_θ : {1,...,M} → ℂⁿ que mapea un mensaje discreto s ∈ {1,...,M} a un vector complejo x ∈ ℂⁿ de n símbolos de canal. Los parámetros θ son los pesos de la red. Típicamente, el encoder consiste en [112]:

1. **Capa de embedding**: Mapea el índice del mensaje s a un vector denso e ∈ ℝᵈ:
   $$e = E_s$$
   donde E ∈ ℝ^(d×M) es la matriz de embedding.

2. **Capas densas**: Varias capas fully-connected con activaciones no lineales:
   $$h^{(l)} = f(W^{(l)} h^{(l-1)} + b^{(l)})$$

3. **Capa de normalización de potencia**: Asegura que 𝔼[||x||²] = n (potencia promedio normalizada):
   $$x = \sqrt{n} \frac{\tilde{x}}{\|\tilde{x}\|}$$
   donde x̃ es la salida sin normalizar.

4. **Separación en componentes I/Q**: La salida real se separa en parte real (I) e imaginaria (Q):
   $$x = x_I + jx_Q$$

**Canal**:
El canal es una capa no entrenable que modela la transformación física. Para AWGN:

$$y = x + n, \quad n \sim \mathcal{CN}(0, N_0 I_n)$$

donde la SNR se define como:

$$\text{SNR} = \frac{\mathbb{E}[\|x\|^2]}{\mathbb{E}[\|n\|^2]} = \frac{n}{N_0 n} = \frac{1}{N_0}$$

Para desvanecimiento Rayleigh:

$$y = h \odot x + n, \quad h \sim \mathcal{CN}(0, I_n)$$

**Receptor (Decoder)**:
El decoder g_φ : ℂⁿ → Δ^(M-1) mapea la señal recibida y a una distribución de probabilidad sobre los M mensajes, donde Δ^(M-1) es el simplex (M-1)-dimensional [113]:

1. **Concatenación I/Q**: Trata las partes real e imaginaria como características separadas:
   $$r = [Re(y); Im(y)] ∈ ℝ^{2n}$$

2. **Capas densas**: Procesamiento no lineal:
   $$h^{(l)} = f(W^{(l)} h^{(l-1)} + b^{(l)})$$

3. **Capa softmax**: Produce probabilidades:
   $$\hat{p}(s|y) = \text{softmax}(W^{(out)} h^{(L)} + b^{(out)})$$
   $$\text{softmax}(z_i) = \frac{e^{z_i}}{\sum_{j=1}^{M} e^{z_j}}$$

#### 2) Función de Pérdida y Entrenamiento

La función de pérdida estándar es la entropía cruzada categórica [114]:

$$\mathcal{L}_{CE}(\theta, \phi) = -\frac{1}{B}\sum_{b=1}^{B} \log \hat{p}(s_b | y_b; \phi)$$

donde B es el tamaño del batch, s_b es el mensaje verdadero, y y_b es la señal recibida correspondiente.

Esta pérdida es equivalente a minimizar la divergencia KL entre la distribución verdadera (one-hot) y la predicha [115]:

$$\mathcal{L}_{CE} = D_{KL}(p_{true} \| \hat{p}) + H(p_{true}) = D_{KL}(p_{true} \| \hat{p})$$

ya que H(p_true) = 0 para distribuciones one-hot.

El procedimiento de entrenamiento es:

```
Para cada época:
    Para cada batch de mensajes {s₁,...,s_B}:
        1. x_b = f_θ(s_b) para cada b (forward pass encoder)
        2. y_b ~ p(y|x_b) para cada b (simulación del canal)
        3. p̂_b = g_φ(y_b) para cada b (forward pass decoder)
        4. Calcular ℒ_CE
        5. Retropropagar gradientes: ∇_θ ℒ, ∇_φ ℒ
        6. Actualizar parámetros: θ ← θ - η∇_θ ℒ, φ ← φ - η∇_φ ℒ
```

#### 3) Interpretación desde Teoría de Información

El autoencoder aprende implícitamente a maximizar la información mutua I(S;Ŝ) entre el mensaje transmitido S y el mensaje estimado Ŝ [116]. La entropía cruzada puede relacionarse con la información mutua como:

$$I(S;\hat{S}) = H(S) - H(S|\hat{S})$$

donde H(S|Ŝ) es la entropía condicional. Minimizar la entropía cruzada equivale a minimizar H(S|Ŝ), lo que maximiza I(S;Ŝ) dado que H(S) es constante para distribución uniforme sobre mensajes [117].

La tasa de información alcanzable es:

$$R = \frac{1}{n}\log_2 M \text{ bits por uso de canal}$$

donde n es el número de símbolos complejos transmitidos por mensaje. El objetivo es maximizar R sujeto a restricciones de potencia y ancho de banda, acercándose a la capacidad del canal [118].

### B. Ventajas sobre Sistemas Convencionales

#### 1) Optimización Conjunta

A diferencia del diseño modular tradicional donde cada componente se optimiza independientemente, el autoencoder realiza optimización end-to-end [119]. Esto permite:

- **Superación del óptimo local modular**: Los esquemas tradicionales como Turbo códigos + QAM están optimizados individualmente pero su combinación puede ser subóptima globalmente.

- **Adaptación implícita al canal**: La red aprende automáticamente la estructura óptima de señalización para el canal específico sin requerir modelos analíticos explícitos.

- **Explotación de estructura no lineal**: Las no linealidades en el encoder y decoder permiten constelaciones y mapeos no convencionales que pueden superar esquemas lineales [120].

#### 2) Flexibilidad Arquitectural

El framework de autoencoder es agnóstico al diseño específico y permite incorporar:

- **Conocimiento del dominio**: Capas de procesamiento de señal conocidas (FFT, convolución, filtrado) pueden integrarse como capas diferenciables [121].

- **Múltiples objetivos**: La función de pérdida puede combinar BER, throughput, latencia, PAPR, eficiencia espectral con pesos ajustables [122]:

$$\mathcal{L}_{multi} = \alpha \mathcal{L}_{BER} + \beta \mathcal{L}_{throughput} + \gamma \mathcal{L}_{PAPR}$$

- **Restricciones del sistema**: Limitaciones prácticas (potencia pico, ancho de banda, sincronización) se incorporan directamente en la arquitectura o pérdida [123].

#### 3) Resultados Experimentales

O'Shea y Hoydis [24] demostraron que para M=16 mensajes y n=7 símbolos complejos sobre canal AWGN, el autoencoder alcanza desempeño cercano al límite teórico de Shannon, superando sistemas convencionales basados en Hamming(7,4) + QPSK.

En [124], se muestra que para canales con desvanecimiento Rayleigh, el autoencoder aprende automáticamente una constelación adaptativa que explota la diversidad del canal, logrando ganancia de 2-3 dB en SNR comparado con 16-QAM convencional a BER = 10⁻³.

### C. Arquitecturas Avanzadas de Autoencoder

#### 1) Autoencoder Variacional para Comunicaciones

Los autoencoders variacionales (VAE) [66] pueden utilizarse para comunicación robusta aprendiendo distribuciones sobre el espacio latente [125].

**Encoder probabilístico**: En lugar de producir una señal determinística x, el encoder produce parámetros de una distribución:

$$\mu, \log \sigma^2 = \text{Encoder}_\theta(s)$$
$$z \sim \mathcal{N}(\mu, \sigma^2 I)$$
$$x = \text{Modulator}(z)$$

**Función de pérdida VAE**:

$$\mathcal{L}_{VAE} = \mathbb{E}_{z \sim q_\theta(z|s)}[\mathcal{L}_{recon}(s, \text{Decoder}_\phi(y))] + \beta D_{KL}(q_\theta(z|s) \| p(z))$$

donde el término KL regulariza el espacio latente y β es un hiperparámetro de balance [126].

**Ventajas**:
- Robustez a incertidumbre del canal
- Generación de múltiples señales válidas por mensaje (diversidad)
- Interpolación suave en el espacio de señales [127]

#### 2) Autoencoder con Atención

Incorporar mecanismos de atención permite al decoder enfocarse en partes relevantes de la señal recibida, especialmente útil en canales selectivos en frecuencia [128].

**Arquitectura**:

$$h = \text{CNN-Encoder}(y)$$
$$\alpha_i = \frac{\exp(e_i)}{\sum_j \exp(e_j)}, \quad e_i = a(h_i, c)$$
$$c = \sum_i \alpha_i h_i$$
$$\hat{s} = \text{Decoder}(c)$$

donde α_i son los pesos de atención que indican la relevancia de cada posición temporal/frecuencial h_i, y c es el vector de contexto ponderado [129].

#### 3) Autoencoder Condicionado

Para canales no estacionarios o con múltiples modos, condicionar el autoencoder en el estado del canal (CSI) mejora el desempeño [130].

**Transmisor condicionado**:

$$x = f_\theta(s, \text{CSI})$$

donde CSI puede incluir SNR estimada, perfil de retardo, velocidad Doppler, etc.

**Receptor condicionado**:

$$\hat{s} = g_\phi(y, \text{CSI})$$

El CSI puede obtenerse mediante secuencias piloto o estimación ciega [131].

**Meta-Learning**: Para generalizar a condiciones de canal no vistas, se utiliza meta-learning (learning to learn) donde el modelo aprende a adaptarse rápidamente con pocos ejemplos [132]:

$$\theta^* = \theta - \alpha \nabla_\theta \mathcal{L}_{\text{support}}(\theta)$$
$$\min_\theta \sum_{\text{tasks}} \mathcal{L}_{\text{query}}(\theta^*)$$

Algoritmos como MAML (Model-Agnostic Meta-Learning) [133] han sido aplicados exitosamente a comunicaciones adaptativas [134].

### D. Constelaciones Aprendidas

Un análisis fascinante del autoencoder es examinar las constelaciones que emerge automáticamente en el espacio de señales [135].

#### 1) Análisis Geométrico

Para n=2 símbolos complejos (4 dimensiones reales), podemos visualizar la constelación aprendida proyectándola en 2D. Los estudios muestran que:

- **Canal AWGN**: La constelación aprendida se aproxima a constelaciones de apilamiento esférico (sphere packing) óptimas, maximizando la distancia mínima d_min entre puntos [136]:

$$d_{min} = \min_{i \neq j} \|x_i - x_j\|$$

Para M=4, la constelación óptima es QPSK. Para M=8, se acerca a 8-PSK o configuraciones asimétricas que superan 8-QAM en bajo SNR [137].

- **Canal Rayleigh**: La constelación se expande para explotar diversidad, con puntos que no están uniformemente espaciados sino concentrados en regiones que maximizan la probabilidad de detección correcta bajo desvanecimiento [138].

- **Canales con no linealidad**: Para amplificadores no lineales modelados como:

$$y = A(|x|) e^{j(\angle x + \Phi(|x|))} + n$$

donde A(·) y Φ(·) son las características AM-AM y AM-PM, la constelación aprendida evita regiones de alta distorsión, resultando en formas asimétricas [139].

#### 2) Capacidad y Mutual Information

La información mutua alcanzada por la constelación aprendida puede estimarse como [140]:

$$I(X;Y) = \log_2 M - \mathbb{E}_{x,y}\left[\log_2 \sum_{s'} \frac{p(y|x_{s'})}{p(y|x_s)}\right]$$

Estudios empíricos [141] muestran que los autoencoders alcanzan información mutua dentro de 0.1-0.5 bits del límite teórico en canal AWGN, y exhiben mejor robustez que constelaciones convencionales en canales con imperfecciones.

### E. Extensiones Multi-Usuario

#### 1) Multiple Access mediante Autoencoder

En escenarios multi-usuario donde K usuarios transmiten simultáneamente, el autoencoder puede aprender esquemas de acceso múltiple [142].

**Formulación**:

- Cada usuario k tiene su propio encoder: x_k = f_θk(s_k)
- Señal recibida: y = ∑_k h_k x_k + n
- Decoder multi-usuario: {ŝ₁,...,ŝ_K} = g_φ(y)

**Función de pérdida**:

$$\mathcal{L} = \sum_{k=1}^{K} \mathcal{L}_{CE}(s_k, \hat{s}_k)$$

**Resultados**: Los autoencoders aprenden estrategias que se asemejan a TDMA, FDMA, CDMA, o NOMA dependiendo de las restricciones y condiciones del canal [143]. En particular, en canales con alta SNR, emerge comportamiento tipo TDMA (orthogonalización temporal), mientras en bajo SNR emerge superposición de señales similar a NOMA [144].

#### 2) Interference Mitigation

Para canales con interferencia de usuarios no cooperativos, el decoder puede incorporar capas especializadas en cancelación de interferencia [145]:

$$\hat{s}_k = g_\phi^{(k)}(y - \sum_{j \neq k} \hat{x}_j)$$

donde x̂_j es la reconstrucción de la señal del interferente j. Este proceso puede iterarse (iterative interference cancellation) [146].

Alternativamente, redes adversariales pueden entrenarse donde un discriminador intenta distinguir señales de usuarios legítimos de interferentes, forzando al encoder a ser robusto [147]:

$$\min_{\theta, \phi} \max_\psi \mathcal{L}_{comm}(\theta, \phi) - \lambda \mathcal{L}_{adv}(\psi)$$

### F. Limitaciones y Desafíos

A pesar de sus ventajas, los autoencoders para comunicación enfrentan varios desafíos [148]:

#### 1) Dependencia de los Datos de Entrenamiento

El autoencoder solo funcionará bien en canales similares a los del entrenamiento. Si las estadísticas del canal en despliegue difieren significativamente (distribución de desvanecimiento, tipo de interferencia, nivel de SNR), el desempeño degrada [149].

**Solución**: Entrenamiento con dominio ampliado (domain randomization) usando variedad de canales, meta-learning para adaptación rápida, o entrenamiento online en el despliegue [150].

#### 2) Complejidad Computacional

La inferencia de redes neuronales profundas requiere numerosas operaciones de punto flotante (FLOPs). Para receptor en dispositivos de bajo consumo, esto es prohibitivo [151].

**Solución**: Cuantización de pesos (int8/int4), pruning (poda de conexiones), knowledge distillation (destilación a redes más pequeñas), arquitecturas eficientes como MobileNets [152], [153].

#### 3) Sincronización y Estimación

Los autoencoders básicos asumen sincronización perfecta de tiempo y frecuencia, lo cual es irreal [154]. Desajustes en sincronización causan rotación de fase, desplazamiento temporal, y ensanchamiento espectral.

**Solución**: Incorporar capas de estimación y corrección de sincronización dentro del autoencoder, o utilizar estructuras de señal robustas como preámbulos, cyclic prefix, y windowing [155].

#### 4) Interpretabilidad

Las redes neuronales son cajas negras, dificultando la comprensión de qué características ha aprendido y cómo toma decisiones [156].

**Solución**: Análisis post-hoc mediante visualización de activaciones, saliency maps, técnicas de interpretabilidad como LIME/SHAP, o diseño de arquitecturas interpretables que incorporan estructura conocida [157].

---

## IV. CODIFICACIÓN DE CANAL NEURAL

La codificación de canal añade redundancia controlada a los datos para permitir detección y corrección de errores introducidos por el canal ruidoso [158]. Los códigos clásicos como Turbo códigos [159], LDPC [160], y Polar codes [161] se aproximan a la capacidad de Shannon pero requieren diseño manual complejo. La codificación neural aprende directamente mapeos óptimos mediante redes neuronales [162].

### A. Fundamentos de Codificación de Canal

#### 1) Definiciones Básicas

Un código de canal (n, k, d) mapea k bits de información a n bits codificados, con distancia mínima d entre palabras código [163]:

- **Tasa de código**: R = k/n ∈ (0,1]
- **Redundancia**: n - k bits añadidos
- **Distancia de Hamming**: d_H(c₁, c₂) = número de posiciones donde c₁ y c₂ difieren
- **Distancia mínima**: d = min_{c₁≠c₂} d_H(c₁, c₂)

El límite de Gilbert-Varshamov establece que existe un código binario lineal (n,k) con distancia mínima al menos d si [164]:

$$\sum_{i=0}^{d-2} \binom{n-1}{i} < 2^{n-k}$$

#### 2) Capacidad del Canal

Para un canal binario simétrico (BSC) con probabilidad de error p, la capacidad es [165]:

$$C_{BSC} = 1 - H(p) = 1 + p\log_2 p + (1-p)\log_2(1-p)$$

El teorema de codificación de Shannon garantiza que existen códigos con tasa R < C y probabilidad de error arbitrariamente pequeña para longitud de bloque n → ∞ [166].

Para canales AWGN, la capacidad considerando modulación BPSK es:

$$C_{AWGN} = \frac{1}{2}\log_2(1 + \text{SNR}) \text{ bits por dimensión}$$

El desafío es diseñar códigos prácticos (n finito) que se acerquen a estos límites [167].

### B. Autoencoders como Códigos de Canal

#### 1) Formulación

Un autoencoder puede interpretarse como un código de canal end-to-end [168]:

- **Encoder**: m ∈ {0,1}^k → x ∈ ℝⁿ (o ℂⁿ)
- **Canal**: y = C(x) donde C representa el canal estocástico
- **Decoder**: y → m̂ ∈ {0,1}^k

La tasa efectiva es R = k/n bits por uso de canal (o k/(2n) bits por dimensión real para símbolos complejos).

#### 2) Arquitectura del Encoder

El encoder neural típicamente consiste en [169]:

1. **Embedding**: Convierte el vector de bits en representación densa
   $$e = \text{Embedding}(m) \in \mathbb{R}^{d_e}$$

2. **Capas fully-connected o convolucionales**:
   $$h^{(l)} = f(W^{(l)}h^{(l-1)} + b^{(l)})$$

3. **Capa de salida con normalización**:
   $$\tilde{x} = W^{(out)}h^{(L)} + b^{(out)}$$
   $$x = \sqrt{n} \frac{\tilde{x}}{\|\tilde{x}\|}$$

Para modulación BPSK o PAM, la capa de salida usa activación tanh escalada:

$$x_i = A \cdot \tanh(z_i) \in [-A, A]$$

#### 3) Arquitectura del Decoder

El decoder recibe la señal ruidosa y estima el mensaje [170]:

1. **Normalización de entrada**: Estandarizar la señal recibida
   $$\tilde{y} = \frac{y - \mu_y}{\sigma_y}$$

2. **Capas de procesamiento**: CNN o fully-connected
   $$h^{(l)} = f(W^{(l)}h^{(l-1)} + b^{(l)})$$

3. **Capa de salida con sigmoide** (para bits):
   $$\hat{m}_i = \sigma(z_i) = \frac{1}{1 + e^{-z_i}} \in (0,1)$$

La decisión hard es: m̂_i = 1 si m̂_i ≥ 0.5, else 0.

#### 4) Función de Pérdida

La función de pérdida estándar es la entropía cruzada binaria (BCE) [171]:

$$\mathcal{L}_{BCE} = -\frac{1}{k}\sum_{i=1}^{k} [m_i \log \hat{m}_i + (1-m_i)\log(1-\hat{m}_i)]$$

Alternativamente, para enfatizar la minimización directa de BER, puede usarse:

$$\mathcal{L}_{BER} = \frac{1}{k}\sum_{i=1}^{k} |m_i - \text{round}(\hat{m}_i)|$$

Sin embargo, la función round(·) no es diferenciable. Una aproximación diferenciable es [172]:

$$\text{soft-round}(x) = \sigma(T(x - 0.5))$$

donde T es un parámetro de temperatura que se incrementa durante el entrenamiento (curriculum learning).

### C. Códigos Turbo Neuronales

Los códigos Turbo tradicionales [159] combinan dos codificadores convolucionales recursivos sistemáticos con un interleaver, y utilizan decodificación iterativa. Esta estructura puede neuralizarse [173].

#### 1) Arquitectura

**Encoder Turbo Neural**:

1. **Encoder sistemático**: Output = entrada + paridad
   $$p_1 = \text{CNN}_{\theta_1}(m)$$

2. **Interleaver**: Permutación π de los bits
   $$m_{\pi} = \pi(m)$$

3. **Segundo encoder**:
   $$p_2 = \text{CNN}_{\theta_2}(m_{\pi})$$

4. **Transmisión**: x = [m; p₁; p₂] (tasa R = k/(k + |p₁| + |p₂|))

**Decoder Turbo Neural Iterativo**: Utiliza múltiples iteraciones de decodificación [174]:

Para iteración t:
1. **Decoder 1**: Procesa [y_m; y_p1; L_ext2]
   $$L_1^{(t)} = \text{Decoder}_{\phi_1}([y_m; y_{p1}; L_{ext2}^{(t-1)}])$$
   $$L_{ext1}^{(t)} = L_1^{(t)} - y_m$$

2. **Interleaver**: L_ext1^π = π(L_ext1)

3. **Decoder 2**: Procesa [y_mπ; y_p2; L_ext1^π]
   $$L_2^{(t)} = \text{Decoder}_{\phi_2}([y_{m\pi}; y_{p2}; L_{ext1}^{\pi}])$$
   $$L_{ext2}^{(t)} = L_2^{(t)} - y_{m\pi}$$

4. **De-interleaver**: L_ext2 = π⁻¹(L_ext2)

Después de T iteraciones:
$$\hat{m} = \text{hard-decision}(L_1^{(T)})$$

donde L representa log-likelihood ratios (LLRs) [175].

#### 2) Resultados

En [176], se demuestra que códigos Turbo neuronales con k=100, tasa R=1/3, alcanzan BER comparables a Turbo códigos convencionales para n ≤ 200, pero con complejidad de decodificación potencialmente reducida mediante optimización de hardware neuromorfo. Para bloques más largos (n > 1000), los códigos Turbo clásicos aún superan debido a mejor estructuración de la interleaving.

### D. Códigos LDPC Neuronales

Los códigos Low-Density Parity-Check (LDPC) [160] se definen mediante una matriz de paridad dispersa H de dimensión (n-k) × n. El decoder clásico utiliza belief propagation (BP) en el grafo de Tanner [177].

#### 1) Belief Propagation Neural

El algoritmo BP puede expresarse como paso de mensajes en un grafo [178]:

**Mensajes variable-a-check**:
$$m_{v \to c}^{(t)} = \lambda_v + \sum_{c' \in N(v) \setminus c} m_{c' \to v}^{(t-1)}$$

**Mensajes check-a-variable**:
$$m_{c \to v}^{(t)} = 2 \tanh^{-1}\left(\prod_{v' \in N(c) \setminus v} \tanh\left(\frac{m_{v' \to c}^{(t)}}{2}\right)\right)$$

donde λ_v es el LLR del canal para el bit v, y N(·) denota vecinos en el grafo de Tanner [179].

**Neuralizaci ón**: Reemplazar las operaciones de BP por capas neuronales aprendibles [180]:

$$m_{v \to c}^{(t)} = f_\theta^{(v2c)}\left(\lambda_v, \{m_{c' \to v}^{(t-1)}\}_{c' \in N(v) \setminus c}\right)$$

$$m_{c \to v}^{(t)} = f_\theta^{(c2v)}\left(\{m_{v' \to c}^{(t)}\}_{v' \in N(c) \setminus v}\right)$$

donde f_θ^(v2c) y f_θ^(c2v) son redes neuronales pequeñas (típicamente MLPs de 2-3 capas) [181].

#### 2) Graph Neural Networks para LDPC

El grafo de Tanner es naturalmente representable como Graph Neural Network (GNN) [182]. Cada nodo (variable o check) tiene:
- **Estado**: h_i^(t) ∈ ℝ^d
- **Función de actualización**: h_i^(t+1) = UPDATE(h_i^(t), {h_j^(t)}_{j ∈ N(i)})

Para códigos LDPC, la arquitectura GNN es [183]:

1. **Inicialización**: h_v^(0) = MLP_init(λ_v), h_c^(0) = 0

2. **Paso de mensajes** (T iteraciones):
   $$m_{v \to c}^{(t)} = \text{MLP}_{v2c}([h_v^{(t-1)}; \sum_{c' \neq c} m_{c' \to v}^{(t-1)}])$$
   $$m_{c \to v}^{(t)} = \text{MLP}_{c2v}([\text{AGGREGATE}(\{m_{v' \to c}^{(t)}\}_{v' \neq v})])$$
   $$h_v^{(t)} = \text{MLP}_{update_v}([h_v^{(t-1)}; \sum_c m_{c \to v}^{(t)}])$$

3. **Decisión**: m̂_v = sign(MLP_out(h_v^(T)))

donde AGGREGATE puede ser suma, max, o atención [184].

#### 3) Desempeño

Estudios muestran que LDPC neuronales pueden superar BP convencional en:
- **Bloques cortos** (n < 1000): Ganancia de 0.2-0.5 dB [185]
- **Canales con errores de ráfaga**: Mejor adaptación a correlación temporal [186]
- **Desvanecimiento**: Explotación de estructura del canal [187]

Sin embargo, para bloques largos (n > 10000), BP con estructura diseñada sigue siendo superior en la waterfall region [188].

### E. Códigos Polares Neuronales

Los códigos Polares [161] son los primeros códigos probados de alcanzar la capacidad del canal con complejidad O(n log n). Se basan en el fenómeno de polarización de canal [189].

#### 1) Construcción Polar Clásica

La transformación polar para n = 2^m es [190]:

$$x = u G_n, \quad G_n = B_n F^{\otimes m}$$

donde F = [1 0; 1 1] es la matriz kernel, ⊗ denota producto Kronecker, y B_n es una matriz de permutación de bit-reversal. Los bits u se dividen en:
- **Frozen bits**: Indices ℱ con baja confiabilidad (fijados a 0)
- **Information bits**: Indices 𝒜 con alta confiabilidad (llevan datos)

#### 2) Neural Polar Decoder

El decoder SCL (Successive Cancellation List) [191] puede neuralizarse reemplazando las decisiones soft por redes neuronales [192]:

**SC Neural**:
Para cada bit i en orden:
$$p(u_i | y, \hat{u}_{1:i-1}) = \text{Neural-SC}_\theta(y, \hat{u}_{1:i-1}, i)$$
$$\hat{u}_i = \arg\max_{u_i \in \{0,1\}} p(u_i | y, \hat{u}_{1:i-1})$$

donde Neural-SC es una RNN o Transformer que procesa la secuencia [193].

**Attention-based Polar Decoder**:
Utilizar Transformer para capturar dependencias a largo alcance [194]:

$$H = \text{TransformerEncoder}([y_1, \ldots, y_n])$$
$$\hat{u}_i = \text{MLP}([H_i; \hat{u}_{1:i-1}])$$

#### 3) Resultados Experimentales

En [195], se muestra que decoders polares neuronales con n=256, R=1/2 alcanzan:
- BER = 10⁻⁵ a SNR de 1.8 dB (vs 2.1 dB para SC clásico)
- Complejidad reducida en 40% versus SCL con L=16

Para n > 1024, la brecha se cierra y SCL con CRC-aided permanece óptimo [196].

### F. Códigos Adaptativos y Rate-Compatible

En sistemas prácticos, la tasa de código debe adaptarse dinámicamente a las condiciones del canal (Hybrid ARQ, rate matching) [197].

#### 1) Neural Rate-Compatible Codes

Un encoder neural rate-compatible produce códigos con tasas variables desde una única arquitectura [198]:

$$x_{n'} = \text{Encoder}_\theta(m, n')$$

donde n' ∈ [n_min, n_max] es la longitud de código deseada. Implementaciones:

**Puncturing Neural**: Entrenar con longitud máxima n_max, luego eliminar sistemáticamente símbolos [199]:

$$x_{punctured} = \text{Puncture}(x_{n_{max}}, \text{pattern}(n'))$$

**Incremental Redundancy**: Transmitir incrementalmente símbolos adicionales [200]:

$$x^{(1)} = x_{1:n_1}, \quad x^{(2)} = x_{n_1+1:n_2}, \quad \ldots$$

El decoder procesa acumulativamente:

$$\hat{m}^{(i)} = \text{Decoder}_\phi([x^{(1)}, \ldots, x^{(i)}])$$

#### 2) Feedback-Enabled Codes

En canales con feedback, el encoder puede adaptar la codificación basado en ACK/NACK [201]:

**Estado**: s_t = (m, history_t)
**Acción**: x_t = π_θ(s_t) (política de codificación)
**Recompensa**: r_t = 𝟙(decodificación correcta) - αt (penalización por latencia)

Se entrena mediante aprendizaje por refuerzo (RL) [202]:

$$\max_\theta \mathbb{E}\left[\sum_t \gamma^t r_t\right]$$

usando algoritmos como PPO [203] o DDPG [204].

### G. Comparación con Códigos Clásicos

La Tabla I resume el desempeño comparativo de códigos neuronales versus clásicos.

**TABLA I: Comparación de Códigos de Canal**

| Código | Tasa | n | BER=10⁻³ SNR (dB) | Complejidad Decoder | Latencia (μs) |
|--------|------|---|-------------------|---------------------|---------------|
| Turbo Clásico | 1/3 | 1024 | 0.8 | O(n) | 50 |
| Turbo Neural | 1/3 | 1024 | 1.0 | O(n) | 35* |
| LDPC (IEEE 802.11) | 1/2 | 1944 | 2.5 | O(n log n) | 80 |
| LDPC Neural | 1/2 | 1944 | 2.3 | O(n) | 60* |
| Polar+SCL(L=8) | 1/2 | 512 | 2.1 | O(n log n L) | 45 |
| Polar Neural | 1/2 | 512 | 1.9 | O(n) | 30* |
| Convolutional (7,1/2) | 1/2 | 512 | 4.5 | O(n²) (Viterbi) | 40 |
| Neural Autoencoder | 1/2 | 512 | 3.2 | O(n) | 25* |

*Asume implementación en GPU/NPU optimizado. En CPU, latencia es 2-3× mayor.

**Observaciones clave** [205]:
1. Para n < 500, códigos neuronales compiten favorablemente en desempeño
2. Para n > 2000, códigos estructurados (Turbo/LDPC/Polar) dominan en waterfall
3. Códigos neuronales muestran mejor floor error (error residual a alto SNR)
4. Latencia de decoding neural es potencialmente menor con hardware especializado
5. Códigos neuronales se adaptan mejor a canales no Gaussianos

---

## V. DETECCIÓN Y DEMODULACIÓN BASADA EN DEEP LEARNING

La detección y demodulación transforman la señal recibida en estimaciones de los símbolos o bits transmitidos [206]. En sistemas MIMO, multi-usuario, y con interferencia severa, la detección óptima es exponencialmente compleja [207]. El Deep Learning ofrece alternativas sub-óptimas con excelente tradeoff complejidad-desempeño [208].

### A. Problema de Detección

#### 1) Formulación General

Dada la señal recibida:

$$y = Hx + n$$

donde:
- y ∈ ℂ^(n_r) es el vector recibido (n_r antenas receptoras)
- H ∈ ℂ^(n_r × n_t) es la matriz de canal (n_t antenas transmisoras)
- x ∈ ℂ^(n_t) es el vector transmitido, x_i ∈ 𝒳 donde 𝒳 es la constelación
- n ~ 𝒩(0, N₀I) es ruido Gaussiano

El problema de detección óptima (ML) es [209]:

$$\hat{x} = \arg\min_{x \in \mathcal{X}^{n_t}} \|y - Hx\|^2$$

Para constelaciones M-QAM, esto requiere evaluar M^(n_t) candidatos, exponencial en n_t [210].

#### 2) Detectores Lineales

Detectores sub-óptimos de complejidad lineal incluyen [211]:

**Zero-Forcing (ZF)**:
$$\hat{x}_{ZF} = (H^H H)^{-1} H^H y = H^\dagger y$$

donde H^† es la pseudoinversa. ZF invierte el canal pero amplifica el ruido [212].

**Minimum Mean Square Error (MMSE)**:
$$\hat{x}_{MMSE} = (H^H H + \frac{N_0}{P} I)^{-1} H^H y$$

MMSE balancea inversión de canal y amplificación de ruido [213].

**Complejidad**: O(n_t³) para inversión de matriz, O(n_t² n_r) para multiplicación.

#### 3) Detectores No Lineales

**Sphere Decoding**: Búsqueda eficiente del ML en espacio acotado [214]:

$$\min_{x} \|y - Hx\|^2 \text{ sujeto a } \|y - Hx\|^2 \leq r^2$$

Complejidad promedio O(n_t³) pero peor caso exponencial [215].

**Successive Interference Cancellation (SIC)**: Detectar símbolos secuencialmente [216]:

Para i = 1 a n_t:
$$\hat{x}_i = \text{detect}(y - \sum_{j=1}^{i-1} H_j \hat{x}_j)$$

Complejidad O(n_t²), desempeño depende del orden de detección [217].

### B. Redes Neuronales para Detección

#### 1) DetNet: Unfolding del Projected Gradient Descent

DetNet [218] unfolds el algoritmo iterativo projected gradient descent en una red neuronal con pesos entrenables.

**Algoritmo PGD** para minimizar ||y - Hx||²:

$$x^{(t+1)} = \mathcal{P}_\mathcal{X}\left(x^{(t)} - \mu \nabla_x \|y - Hx^{(t)}\|^2\right)$$
$$= \mathcal{P}_\mathcal{X}(x^{(t)} + \mu H^H(y - Hx^{(t)}))$$

donde 𝒫_𝒳 proyecta a la constelación (hard decision) y μ es el tamaño de paso.

**DetNet**: Reemplazar operaciones por capas aprendibles [219]:

$$z^{(t)} = x^{(t)} + W_1^{(t)} H^H(y - Hx^{(t)})$$
$$r^{(t)} = W_2^{(t)} z^{(t)} + b^{(t)}$$
$$x^{(t+1)} = \mathcal{P}_\mathcal{X}(r^{(t)})$$

donde W₁^(t), W₂^(t), b^(t) son parámetros entrenables por capa/iteración. La proyección se implementa como:

$$\mathcal{P}_\mathcal{X}(r_i) = \arg\min_{c \in \mathcal{X}} |r_i - c|$$

**Función de pérdida**:

$$\mathcal{L} = \frac{1}{n_t}\sum_{i=1}^{n_t} \|x_i - x_i^{(T)}\|^2 + \lambda \sum_{t=1}^{T} \|x - x^{(t)}\|^2$$

El segundo término supervisa las iteraciones intermedias (supervision profunda) [220].

**Resultados**: Para sistema 16×16 MIMO con 16-QAM, DetNet con T=10 iteraciones alcanza desempeño cercano a ML con complejidad O(Tn_t²) << O(M^(n_t)), logrando BER = 10⁻³ a 10 dB SNR versus 12 dB para MMSE [218].

#### 2) OAMP-Net: Approximate Message Passing Neural

Orthogonal AMP (OAMP) es un algoritmo iterativo basado en message passing [221]:

$$x^{(t)} = \eta_t(z^{(t)}, \tau_t)$$
$$z^{(t+1)} = y - Hx^{(t)} + \frac{z^{(t)}}{\tau_t} \langle \eta_t'(z^{(t)}, \tau_t) \rangle$$

donde η_t es una función de denoising, τ_t es la varianza del error estimado, y ⟨·⟩ denota promedio.

**OAMP-Net** [222] reemplaza el denoiser por una red neuronal:

$$\eta_t(z, \tau) = \text{CNN}_{\theta_t}([Re(z); Im(z); \tau])$$

La CNN típicamente tiene 5-10 capas convolucionales con kernels pequeños (3×1), batch normalization, y activaciones ReLU [223].

**Actualización de varianza aprendible**:

$$\tau_{t+1} = f_{\theta_t}(\tau_t, \|z^{(t)}\|)$$

donde f es una red pequeña (2 capas fully-connected).

**Resultados**: OAMP-Net supera DetNet en sistemas MIMO masivos (e.g., 128×32) y canales correlacionados, alcanzando BER = 10⁻⁴ a 8 dB SNR versus 10 dB para DetNet [222].

#### 3) Deep MIMO Detection con CNNs

Directamente utilizar CNN profundas para mapear y → x̂ [224]:

**Arquitectura**:

1. **Preprocesamiento**: Concatenar partes real e imaginaria y información del canal
   $$r = [Re(y); Im(y); Re(H(:)); Im(H(:))] \in \mathbb{R}^{2n_r + 2n_t n_r}$$

2. **CNN profunda**: 20-50 capas con conexiones residuales
   $$h^{(l+1)} = f(W^{(l)} * h^{(l)} + b^{(l)}) + h^{(l)}$$

3. **Capa de salida**: Para cada símbolo, clasificación soft
   $$\hat{p}(x_i = c) = \text{softmax}(W^{(out)}_i h^{(L)} + b^{(out)}_i)_c, \quad c \in \mathcal{X}$$

**Función de pérdida**: Entropía cruzada categórica para cada símbolo [225]:

$$\mathcal{L} = -\sum_{i=1}^{n_t} \log \hat{p}(x_i = x_i^{true})$$

**Ventajas**:
- No requiere despliegue iterativo explícito
- Puede aprender patrones complejos del canal
- Generaliza a canales con estructura no modelada [226]

**Desventajas**:
- Requiere muchos parámetros (millones)
- Entrenamiento costoso
- Sensible a desajuste de distribución del canal [227]

#### 4) Graph Neural Networks para Detección MIMO

Representar el sistema MIMO como un grafo donde nodos son antenas y aristas representan interferencia [228].

**Grafo MIMO**:
- Nodos transmisores: V_T = {1, ..., n_t}
- Nodos receptores: V_R = {1, ..., n_r}
- Aristas: E = {(i,j) : H_{ji} ≠ 0}

**GNN Detector** [229]:

1. **Inicialización**:
   $$h_i^{(0)} = \text{MLP}_{init}([y_i; H_{i,:}])$$

2. **Message Passing** (T iteraciones):
   $$m_{i \to j}^{(t)} = \text{MLP}_{msg}([h_i^{(t-1)}; h_j^{(t-1)}; H_{ji}])$$
   $$h_j^{(t)} = \text{MLP}_{update}\left(h_j^{(t-1)}, \sum_{i \in N(j)} m_{i \to j}^{(t)}\right)$$

3. **Decisión**:
   $$\hat{x}_i = \text{MLP}_{out}(h_i^{(T)})$$

**Resultados**: GNN-Detector muestra robustez superior en canales con estructura de sparsity o topología específica (e.g., cell-free massive MIMO) [230].

### C. Demodulación en Canales Selectivos en Frecuencia

En canales con dispersión temporal, la ISI (Inter-Symbol Interference) degrada el desempeño [231].

#### 1) Problema de Ecualización

El modelo de canal discreto es [232]:

$$y[n] = \sum_{l=0}^{L-1} h_l x[n-l] + w[n]$$

Objetivo: Estimar {x[n]} dado {y[n]} y {h_l}.

**Ecualizadores clásicos** [233]:
- **Linear Equalizer (LE)**: Filtro FIR inverso
- **Decision Feedback Equalizer (DFE)**: Feedforward + feedback de decisiones pasadas
- **MLSE (Maximum Likelihood Sequence Estimation)**: Algoritmo de Viterbi, óptimo pero complejidad O(M^L) [234]

#### 2) Neural Equalizers con RNNs

Las RNNs son naturales para ecualización debido a dependencias temporales [235].

**Arquitectura Bi-LSTM**:

$$\overrightarrow{h}_t = \text{LSTM}(y_t, \overrightarrow{h}_{t-1})$$
$$\overleftarrow{h}_t = \text{LSTM}(y_t, \overleftarrow{h}_{t+1})$$
$$h_t = [\overrightarrow{h}_t; \overleftarrow{h}_t]$$
$$\hat{x}_t = \text{softmax}(W h_t + b)$$

El Bi-LSTM procesa la secuencia en ambas direcciones, capturando contexto pasado y futuro [236].

**Función de pérdida**:

$$\mathcal{L} = -\sum_t \log p(\hat{x}_t = x_t | y_{1:T})$$

**Resultados**: En canales ITU Vehicular-A con L=6 taps y 16-QAM, Bi-LSTM supera DFE en 3 dB a BER = 10⁻³ [237].

#### 3) Temporal Convolutional Networks (TCN)

Las TCNs utilizan convoluciones causales dilatadas para capturar dependencias largas con menor complejidad que RNNs [238].

**Convolución causal dilatada**:

$$(x *_d k)[n] = \sum_{m=0}^{M-1} k[m] x[n - d \cdot m]$$

donde d es la tasa de dilatación. Apilando capas con dilataciones crecientes (d = 1, 2, 4, 8, ...), el receptive field crece exponencialmente [239].

**Arquitectura TCN para ecualización** [240]:

```
Input: y[n]
→ Causal Conv (d=1, filters=64)
→ Causal Conv (d=2, filters=64)
→ Causal Conv (d=4, filters=64)
→ ...
→ Causal Conv (d=2^K, filters=64)
→ FC layer → Softmax
Output: p(x[n])
```

**Ventajas sobre RNN**:
- Paralelizable (no secuencial)
- Training más estable
- Inferencia más rápida [241]

### D. Detección Multi-Usuario

En sistemas con múltiples usuarios transmitiendo simultáneamente (uplink MIMO, NOMA), el receptor debe separar las señales [242].

#### 1) Formulación Uplink Multi-Usuario

$$y = \sum_{k=1}^{K} H_k x_k + n$$

donde K es el número de usuarios, H_k ∈ ℂ^(n_r × n_k) es el canal del usuario k, y x_k ∈ ℂ^(n_k) es su señal.

**Detección óptima joint ML** [243]:

$$\{\hat{x}_1, \ldots, \hat{x}_K\} = \arg\min_{\{x_k\}} \left\|y - \sum_k H_k x_k\right\|^2$$

Complejidad: O(M^(∑_k n_k)), prohibitivo para K grande.

#### 2) DeepSIC: Deep Successive Interference Cancellation

DeepSIC [244] combina SIC con redes neuronales para detección robusta.

**Arquitectura**:

Para usuario k en orden k = 1, ..., K:

1. **Cancelación de interferencia**:
   $$\tilde{y}_k = y - \sum_{j=1}^{k-1} H_j \hat{x}_j$$

2. **Detección neural**:
   $$\hat{x}_k = \text{DetNet}_{\theta_k}(\tilde{y}_k, H_k)$$

donde DetNet_θk es una red especializada para el usuario k [245].

**Ordenamiento óptimo**: El orden de detección impacta el desempeño. Se aprende una política de ordenamiento mediante RL:

$$\pi(\text{order} | y, \{H_k\}) = \text{PolicyNet}_\psi(y, \{H_k\})$$

entrenada para maximizar suma de tasas o minimizar suma de BER [246].

**Resultados**: DeepSIC en sistema 32-antena BS con K=8 usuarios (4 antenas cada uno) y 64-QAM alcanza sum-rate 10% superior a MMSE-SIC a 15 dB SNR [244].

#### 3) Power-Domain NOMA con DL

En NOMA (Non-Orthogonal Multiple Access), usuarios con diferentes potencias se superponen [247]. El receptor usa SIC basado en diferencia de potencia.

**Modelo 2-usuario NOMA**:

$$y = h_1 \sqrt{P_1} x_1 + h_2 \sqrt{P_2} x_2 + n$$

con P₁ >> P₂ (usuario 1 es cercano, usuario 2 lejano).

**SIC convencional** [248]:
1. Decodificar usuario 1 (fuerte): x̂₁ = detect(y)
2. Cancelar: ỹ = y - h₁√P₁ x̂₁
3. Decodificar usuario 2: x̂₂ = detect(ỹ)

**Neural NOMA Detector** [249]: Red end-to-end que mapea y → {x̂₁, x̂₂}:

$$\{p(x_1), p(x_2)\} = \text{DNN}_\theta(y, h_1, h_2, P_1, P_2)$$

La red aprende implícitamente la estrategia de cancelación óptima, superando SIC cuando hay errores de propagación [250].

### E. Estimación de Símbolos en Fading Rápido

En canales con desvanecimiento rápido, el canal varía símbolo-a-símbolo [251].

#### 1) Modelo de Canal Variante en el Tiempo

$$y[n] = h[n] x[n] + w[n]$$

donde h[n] ~ 𝒞𝒩(0, σ²_h) evoluciona según modelo de Markov [252]:

$$h[n] = \rho h[n-1] + \sqrt{1-\rho^2} u[n], \quad u[n] \sim \mathcal{CN}(0, \sigma_h^2)$$

con ρ = J₀(2πf_D T_s), donde f_D es la frecuencia Doppler y T_s el periodo de símbolo (modelo de Jakes) [253].

#### 2) Joint Channel Estimation and Data Detection Neural Network

**Arquitectura JCEDD** [254]:

1. **Estimación de canal implícita**: RNN que trackea el canal
   $$\hat{h}[n], s[n] = \text{RNN}_{est}(y[n], s[n-1])$$
   donde s[n] es el estado oculto.

2. **Predicción de símbolos**:
   $$\hat{x}[n] = \text{MLP}_{det}(y[n], \hat{h}[n])$$

3. **Refinamiento**: Feedback de decisiones para mejorar estimación
   $$\hat{h}_{refined}[n] = \text{Update}(\hat{h}[n], \hat{x}[n-1])$$

**Entrenamiento conjunto**:

$$\mathcal{L} = \sum_n \|\hat{x}[n] - x[n]\|^2 + \lambda \|\hat{h}[n] - h[n]\|^2$$

donde el segundo término se incluye si se tienen pilotos (semi-supervised) [255].

**Resultados**: Para f_D T_s = 0.01 (movilidad 60 km/h a 2 GHz) y 16-QAM, JCEDD alcanza BER = 10⁻³ a 12 dB versus 14.5 dB para estimación LS + MMSE detection [254].

---

## VI. ESTIMACIÓN DE CANAL Y CSI CON REDES NEURONALES

La información del estado del canal (CSI - Channel State Information) es fundamental para beamforming, scheduling, control de potencia, y adaptación de enlace [256]. La estimación precisa de CSI es desafiante en sistemas MIMO masivos, canales de alta movilidad, y bandas milimétricas [257].

### A. Fundamentos de Estimación de Canal

#### 1) Modelo de Señal con Pilotos

En sistemas con pilotos, se transmiten secuencias conocidas [258]:

$$Y = XH + N$$

donde:
- Y ∈ ℂ^(n_r × τ) son las señales recibidas
- X ∈ ℂ^(n_t × τ) son los pilotos transmitidos (conocidos)
- H ∈ ℂ^(n_r × n_t) es la matriz de canal
- N ~ 𝒩(0, N₀I) es ruido
- τ es la longitud de la secuencia piloto

#### 2) Estimadores Clásicos

**Least Squares (LS)** [259]:

$$\hat{H}_{LS} = YX^H(XX^H)^{-1}$$

LS es unbiased pero no explota información a priori sobre H.

**MMSE (Minimum Mean Square Error)** [260]:

$$\hat{H}_{MMSE} = R_H X^H (XR_H X^H + N_0 I)^{-1} Y^H$$

donde R_H = 𝔼[H^H H] es la matriz de covarianza del canal. MMSE es óptimo bajo MSE pero requiere conocer R_H [261].

**Compressed Sensing**: Para canales sparse (e.g., mmWave, THz) [262]:

$$H = \Phi \alpha$$

donde Φ ∈ ℂ^(n_r n_t × L) es el diccionario (e.g., DFT, beamspace) y α es L-sparse. La estimación se formula como:

$$\min_\alpha \|Y - X\Phi\alpha\|_F^2 + \lambda \|\alpha\|_1$$

soluble mediante algoritmos como OMP (Orthogonal Matching Pursuit) o LASSO [263], [264].

### B. Channel Estimation mediante Deep Learning

#### 1) ChannelNet: CNN para Estimación

ChannelNet [265] utiliza CNN para aprender el mapeo Y → Ĥ.

**Arquitectura**:

1. **Preprocesamiento**: Concatenar componentes I/Q
   $$Z = [Re(Y); Im(Y); Re(X); Im(X)] \in \mathbb{R}^{2(n_r + n_t) \times \tau}$$

2. **CNN con residual blocks**:
   ```
   Conv(3×3, 64) → BN → ReLU
   → ResBlock × 5
   → Conv(3×3, 64) → BN → ReLU
   → Conv(3×3, 2n_r n_t)
   ```
   donde ResBlock implementa:
   $$h^{(l+1)} = f(W^{(l)} * h^{(l)}) + h^{(l)}$$

3. **Reshape**: Output se reordena a Ĥ ∈ ℂ^(n_r × n_t)

**Función de pérdida**:

$$\mathcal{L} = \frac{1}{n_r n_t} \|\hat{H} - H\|_F^2 = \frac{1}{n_r n_t} \sum_{i,j} |\hat{H}_{ij} - H_{ij}|^2$$

**Resultados**: Para sistema 32×32 MIMO en canal 3GPP Urban Micro con τ=8 pilotos, ChannelNet reduce NMSE (Normalized MSE) de -15 dB (LS) a -22 dB [265].

#### 2) ReEsNet: Residual Estimation Network

ReEsNet [266] descompone la estimación en componente de baja frecuencia (tendencia) y alta frecuencia (detalles).

**Arquitectura de dos ramas**:

**Rama Low-Frequency**:
$$H_{LF} = \text{CNN}_{LF}(Y, X)$$
CNN con kernels grandes (7×7, 5×5) para capturar variaciones suaves.

**Rama High-Frequency**:
$$R = Y - XH_{LF}$$
$$H_{HF} = \text{CNN}_{HF}(R, H_{LF})$$
CNN con kernels pequeños (3×3, 1×1) para detalles finos.

**Fusión**:
$$\hat{H} = H_{LF} + H_{HF}$$

**Ventaja**: Separación de escalas mejora generalización a diferentes SNR y longitudes de coherencia [267].

#### 3) Transformer-based Channel Estimation

Los Transformers capturan dependencias espaciales y temporales en canales MIMO [268].

**Arquitectura ChanFormer** [269]:

1. **Embedding espacial**: Cada par antena-tx/antena-rx es un token
   $$e_{ij} = \text{Linear}([Y_{i,:}; X_{j,:}]; pos(i,j))$$
   donde pos(i,j) es positional encoding espacial.

2. **Multi-Head Attention**: Captura correlación espacial
   $$E' = \text{MultiHeadAttention}(E, E, E)$$

3. **Feedforward**: Transformación no lineal
   $$E'' = \text{FFN}(E')$$

4. **Output**: Proyectar a estimación del canal
   $$\hat{H}_{ij} = \text{Linear}(E''_{ij})$$

**Ventajas**:
- Escalabilidad a sistemas MIMO ultra-masivos (>128 antenas)
- Captura correlaciones de largo alcance espacial
- Paralelizable para inferencia rápida [270]

### C. CSI Feedback Compression

En sistemas FDD (Frequency Division Duplex), el CSI debe retroalimentarse del receptor (UE) al transmisor (BS) a través de un canal de uplink de capacidad limitada [271].

#### 1) Problema de Feedback CSI

El canal downlink H ∈ ℂ^(n_r × n_t) requiere 2n_r n_t valores reales. Para n_r = 32, n_t = 4, con 16-bit quantization, esto es 4096 bits, excesivo [272].

Objetivo: Diseñar encoder-decoder para comprimir CSI:

- **Encoder (en UE)**: H → c donde c ∈ {0,1}^B con B << 2n_r n_t (tasa de compresión ρ = B/(2n_r n_t))
- **Decoder (en BS)**: c → Ĥ

#### 2) CsiNet: Autoencoder para CSI Feedback

CsiNet [273] utiliza CNN autoencoder para comprimir CSI.

**Encoder**:
```
Input: H ∈ ℂ^(n_r × n_t)
→ Concat([Re(H); Im(H)]) ∈ ℝ^{2n_r × n_t}
→ Conv(3×3, 64) → ReLU
→ Conv(3×3, 32) → ReLU
→ FC → c ∈ ℝ^B
→ Quantization → c_q ∈ {0,1}^B
```

**Decoder**:
```
Input: c_q ∈ {0,1}^B
→ FC → Reshape
→ ConvTranspose(3×3, 32) → ReLU
→ ConvTranspose(3×3, 64) → ReLU
→ Conv(3×3, 2) → Ĥ ∈ ℝ^{2n_r × n_t}
```

**Función de pérdida**:

$$\mathcal{L} = \|\hat{H} - H\|_F^2 + \lambda \|c\|_1$$

El término L1 promueve sparsity para quantization eficiente [274].

**Quantization-Aware Training**: Incluir quantization en el training mediante STE (Straight-Through Estimator) [275]:

$$c_q = \text{round}(c), \quad \frac{\partial c_q}{\partial c} \approx I$$

**Resultados**: Con compresión ρ = 1/32 (B=256 para H de 32×32), CsiNet alcanza NMSE = -20 dB versus -10 dB con quantization directa basada en DFT [273].

#### 3) CsiNet+: Attention y Multi-Resolution

CsiNet+ [276] mejora CsiNet incorporando:

**Multi-Resolution Processing**: Capturar características a múltiples escalas
```
H → [Path_1: Conv(3×3)] 
  → [Path_2: Conv(5×5)]
  → [Path_3: Conv(7×7)]
  → Concatenate → Feature Fusion
```

**Attention Module**: Ponderar selectivamente características importantes
$$A = \text{sigmoid}(W_2 \text{ReLU}(W_1 \text{GAP}(F)))$$
$$F' = A \odot F$$

donde GAP es Global Average Pooling y ⊙ es producto elemento-a-elemento [277].

**Mejora**: NMSE adicional de 2-3 dB sobre CsiNet [276].

#### 4) Transformer-based CSI Feedback

CSI-TransNet [278] usa Transformers para capturar correlación espacial y temporal (múltiples slots).

**Arquitectura**:

**Encoder**:
1. Patchify: Dividir H en patches p×p
2. Linear embedding: e_i = Linear(patch_i)
3. Positional encoding: e'_i = e_i + PE(i)
4. Transformer encoder: Z = TransformerEncoder(E')
5. Projection: c = Linear(Z_[CLS])

**Decoder**:
1. Expansion: Z = Linear(c)
2. Transformer decoder: Z' = TransformerDecoder(Z)
3. Unpatchify: Reconstruct Ĥ from patches

**Temporal Extension**: Para secuencia de H^(t-K+1), ..., H^(t), embeddings temporales se añaden:

$$e_i^{(t)} = \text{Linear}(\text{patch}_i^{(t)}) + PE_{space}(i) + PE_{time}(t)$$

**Ventaja**: Explotación de correlación temporal reduce dramáticamente feedback overhead [279].

### D. CSI Prediction

Predecir el CSI futuro permite proactive beamforming y scheduling, crítico para latencia ultrabaja [280].

#### 1) Modelo de Canal Temporal

El canal H[t] evoluciona según [281]:

$$H[t] = f(H[t-1], H[t-2], \ldots, H[t-K]) + U[t]$$

donde U[t] representa innovación estocástica. Para canales con movilidad, el modelo de Clarke/Jakes [282]:

$$h[t] = \sum_{l=1}^{L} a_l e^{j(2\pi f_{D,l} t + \theta_l)}$$

donde f_{D,l} = f_c v cos(φ_l)/c es el desplazamiento Doppler angular.

#### 2) LSTM para CSI Prediction

Las LSTMs son naturales para predicción de series temporales [283].

**Arquitectura**:

```
Input: {H[t-K+1], ..., H[t]} cada H ∈ ℂ^{n_r × n_t}
→ Reshape cada H a vector v[t] ∈ ℝ^{2n_r n_t}
→ LSTM(hidden_dim=256) × 3 layers
→ FC layer
→ Output: v̂[t+Δ]
→ Reshape a Ĥ[t+Δ]
```

**Función de pérdida**:

$$\mathcal{L} = \sum_{\Delta=1}^{\Delta_{max}} \alpha_\Delta \|H[t+\Delta] - \hat{H}[t+\Delta]\|_F^2$$

donde α_Δ pondera horizontes de predicción (típicamente α_Δ = λ^Δ con λ < 1) [284].

**Resultados**: Para canal Vehicular-A con velocidad 60 km/h y predicción Δ = 10 slots (10 ms), LSTM reduce NMSE de -8 dB (extrapolación lineal) a -15 dB [285].

#### 3) ConvLSTM y SpatioTemporal Prediction

Para canales MIMO, la correlación espacial debe preservarse. ConvLSTM [286] reemplaza multiplicaciones matriciales por convoluciones:

$$i_t = \sigma(W_{xi} * x_t + W_{hi} * h_{t-1} + b_i)$$
$$f_t = \sigma(W_{xf} * x_t + W_{hf} * h_{t-1} + b_f)$$
$$C_t = f_t \odot C_{t-1} + i_t \odot \tanh(W_{xC} * x_t + W_{hC} * h_{t-1} + b_C)$$
$$o_t = \sigma(W_{xo} * x_t + W_{ho} * h_{t-1} + b_o)$$
$$h_t = o_t \odot \tanh(C_t)$$

donde * denota convolución 2D, preservando la estructura espacial de H [287].

#### 4) GAN-based CSI Prediction

Las GANs pueden generar predicciones de CSI realistas capturando la distribución compleja [288].

**Arquitectura**:

**Generator**: H[t-K:t] → Ĥ[t+1:t+Δ]
- Encoder: ConvLSTM que procesa secuencia histórica
- Decoder: ConvLSTM que genera secuencia futura

**Discriminator**: Distingue entre secuencias reales H[·] y generadas Ĥ[·]
- 3D CNN que procesa (espacio × espacio × tiempo)
- Output: p(real) ∈ [0,1]

**Función de pérdida**:

$$\mathcal{L}_G = \mathbb{E}[\log(1 - D(\hat{H}))] + \lambda \|\hat{H} - H\|_F^2$$
$$\mathcal{L}_D = \mathbb{E}[\log D(H)] + \mathbb{E}[\log(1 - D(\hat{H}))]$$

El término de reconstrucción estabiliza el entrenamiento y asegura precisión [289].

**Ventaja**: Las predicciones de GAN capturan mejor la distribución de incertidumbre, útil para robust beamforming [290].

### E. Blind Channel Estimation

En algunos escenarios (comunicación de backhaul, D2D, sistemas sin pilotos), la estimación debe ser ciega [291].

#### 1) Formulación

Dadas solo las señales recibidas Y sin conocimiento de X:

$$Y = XH + N$$

Objetivo: Estimar H (y posiblemente X).

Este es un problema mal-puesto requiriendo suposiciones adicionales [292]:
- Estructura de X (e.g., constante modulus, finito alfabeto)
- Estructura de H (e.g., sparse, low-rank)
- Estadísticas (e.g., X independiente de H)

#### 2) ICA-based Neural Network

Independent Component Analysis (ICA) asume que las fuentes X son estadísticamente independientes [293]. Deep ICA [294] utiliza redes neuronales:

**Arquitectura**:

$$\hat{X} = W Y$$

donde W es implementado como una red neuronal (unfolded ICA iterations).

**Función de pérdida**: Maximizar no-Gaussianity de X̂ medida por negentropía [295]:

$$\mathcal{L} = -\sum_i \text{NeGent}(\hat{X}_i)$$

donde:

$$\text{NeGent}(X_i) = H(\mathcal{N}(0, \sigma_i^2)) - H(\hat{X}_i)$$

Aproximado mediante:

$$\text{NeGent}(\hat{X}_i) \approx [(\mathbb{E}[G(\hat{X}_i)] - \mathbb{E}[G(\mathcal{N})])^2$$

con G(·) una función no cuadrática (e.g., G(x) = log cosh(x)) [296].

#### 3) CycloStationary Neural Estimation

Para señales con estadísticas cicloestacionarias (e.g., OFDM), explotarlas mejora la estimación [297].

**Cyclic Correlation Function**:

$$R_x^\alpha(\tau) = \mathbb{E}[x(t) x^*(t-\tau) e^{-j2\pi\alpha t}]$$

donde α es la frecuencia cíclica [298].

**Neural Cyclo-Estimator** [299]: CNN que procesa el cyclic spectrum:

$$S_x^\alpha(f) = \mathcal{F}\{R_x^\alpha(\tau)\}$$

Input: S_y^α(f) para múltiples α
Output: Ĥ(f)

La red aprende implícitamente a extraer características cicloestacionarias discriminativas [300].

---

## VII. BEAMFORMING Y PRECODIFICACIÓN INTELIGENTE

En sistemas MIMO masivos y mmWave/THz 6G, el beamforming direccional es esencial para superar pérdidas de propagación severas y gestionar interferencias [301].

### A. Fundamentos de Beamforming

#### 1) Modelo de Sistema MIMO

Downlink multi-usuario:

$$y_k = H_k W s_k + \sum_{j \neq k} H_k W_j s_j + n_k$$

donde:
- y_k ∈ ℂ^(n_k): señal recibida por usuario k
- H_k ∈ ℂ^(n_k × n_t): canal de BS a usuario k
- W_k ∈ ℂ^(n_t × d_k): precodificador para usuario k
- s_k ∈ ℂ^(d_k): símbolo de datos (𝔼[||s_k||²] = P_k)
- n_k ~ 𝒩(0, N₀I): ruido [302]

#### 2) Precodificación Lineal Clásica

**Zero-Forcing (ZF)**: Cancelar interferencia inter-usuario [303]

$$W_{ZF} = H^H (H H^H)^{-1}$$

donde H = [H₁^H; ...; H_K^H]^H ∈ ℂ^(∑_k n_k × n_t). ZF fuerza H_k W_j = 0 para j ≠ k, pero amplifica ruido cuando el canal está mal condicionado.

**Regularized ZF (RZF)**: Balancea interferencia y ruido [304]

$$W_{RZF} = H^H (HH^H + \alpha I)^{-1}$$

donde α > 0 es el parámetro de regularización (típicamente α ∝ 1/SNR).

**Maximum Ratio Transmission (MRT)**: Maximiza SNR por usuario sin considerar interferencia [305]

$$W_{MRT,k} = H_k^H$$

MRT es óptimo para usuario único pero subóptimo en multi-usuario.

**Complejidad**: O(K³) para inversión matricial, prohibitivo para K grande o computación en tiempo real [306].

### B. Deep Learning para Hybrid Beamforming

En sistemas mmWave, el costo y consumo de cadenas RF impide full-digital beamforming [307]. El hybrid beamforming combina procesamiento analógico (phase shifters) y digital (baseband) [308].

#### 1) Arquitectura Hybrid

$$W = W_{RF} W_{BB}$$

donde:
- W_RF ∈ ℂ^(n_t × n_{RF}): precodificador analógico RF (phase shifters)
- W_BB ∈ ℂ^(n_{RF} × d): precodificador digital baseband
- n_{RF} << n_t: número de cadenas RF

**Restricciones**:
- Constant modulus: |[W_RF]_{ij}| = 1/√n_t (phase shifters)
- Potencia: ||W_RF W_BB||_F² ≤ P [309]

#### 2) Neural Hybrid Beamformer

El problema de optimización:

$$\max_{W_{RF}, W_{BB}} R = \sum_k \log_2 \det(I + H_k W_{RF} W_{BB} W_{BB}^H W_{RF}^H H_k^H R_k^{-1})$$

donde R_k = N₀I + ∑_{j≠k} H_k W_RF W_{BB,j} W_{BB,j}^H W_RF^H H_k^H es la covarianza de interferencia+ruido. Este problema es no-convexo y difícil [310].

**Solución Neural** [311]:

**Red para W_RF**: Mapea H → W_RF

1. Extracción de características del canal:
   $$F = \text{CNN}([Re(H); Im(H)])$$

2. Generación de fases:
   $$\phi = \text{MLP}(F) \in \mathbb{R}^{n_t \times n_{RF}}$$

3. Normalización constant-modulus:
   $$[W_{RF}]_{ij} = \frac{1}{\sqrt{n_t}} e^{j\phi_{ij}}$$

**Red para W_BB**: Dado W_RF y H, optimizar W_BB

$$W_{BB} = \text{MLP}([W_{RF}; H])$$

normalizado para satisfacer restricción de potencia.

**Entrenamiento end-to-end**:

$$\mathcal{L} = -\sum_k R_k + \lambda(\|W_{RF} W_{BB}\|_F^2 - P)^2$$

**Resultados**: Para sistema 256×16 MIMO en canal mmWave con n_RF = 8, hybrid beamformer neural alcanza 95% de la capacidad full-digital versus 80% para soluciones basadas en codebook [311].

### C. Beamforming Distribuido con Federated Learning

En sistemas cell-free massive MIMO, múltiples APs cooperan para servir usuarios [312]. El beamforming distribuido requiere coordinar precoding sin compartir CSI completo por overhead [313].

#### 1) Problema de Optimización Distribuido

Cada AP m diseña su precodificador W_m basado en CSI local H_m:

$$\max_{\{W_m\}} \sum_k R_k \quad \text{sujeto a} \quad \|W_m\|_F^2 \leq P_m \, \forall m$$

con limitada cooperación (backhaul de capacidad restringida) [314].

#### 2) Federated Learning para Beamforming

**Arquitectura Federada** [315]:

1. **Entrenamiento local** en cada AP m:
   - Datos locales: {H_m^(i), y^(i)}
   - Entrenar modelo local θ_m minimizando pérdida local:
     $$\mathcal{L}_m(\theta_m) = -\sum_i R(W_m = f_{\theta_m}(H_m^{(i)}))$$

2. **Agregación en servidor central**:
   - Recolectar gradientes ∇_θm ℒ_m o pesos θ_m (no CSI cruda)
   - Agregar: θ_global = ∑_m (N_m/N) θ_m donde N_m = |datos en AP m|

3. **Distribución**: Enviar θ_global a