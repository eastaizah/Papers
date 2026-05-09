# SECCIÓN III: ARQUITECTURAS NEURONALES ADAPTATIVAS PARA RECEPTORES 6G

## A. Codificación Conjunta Fuente-Canal Neural (JSCC)

La codificación conjunta fuente-canal neural (Neural Joint Source-Channel Coding, JSCC) representa un cambio paradigmático en el diseño de sistemas de comunicación 6G, abandonando el enfoque tradicional de separación entre codificación de fuente y canal establecido por el teorema de Shannon [90]. En el contexto de comunicaciones masivas inalámbricas con restricciones de latencia ultrabaja, las arquitecturas JSCC neuronales ofrecen ventajas significativas al optimizar de manera end-to-end la cadena de transmisión completa [91].

El marco fundamental de JSCC neural puede formularse como un problema de optimización de distorsión-tasa, donde el objetivo es minimizar la función de pérdida:

$$\mathcal{L}_{JSCC} = \mathbb{E}[d(S, \hat{S})] + \lambda \cdot I(X; Y) \tag{1}$$

donde $S$ representa la señal fuente, $\hat{S}$ la señal reconstruida, $d(\cdot,\cdot)$ es una métrica de distorsión (típicamente MSE o pérdidas perceptuales), $X$ e $Y$ son las señales transmitida y recibida respectivamente, $I(\cdot;\cdot)$ denota la información mutua, y $\lambda$ es un parámetro de control de tasa [92].

La arquitectura neuronal para JSCC se compone típicamente de dos redes neuronales profundas: un codificador $E_\theta$ y un decodificador $D_\varphi$, parametrizados por $\theta$ y $\varphi$ respectivamente:

$$X = E_\theta(S) \tag{2}$$

$$\hat{S} = D_\varphi(Y) \tag{3}$$

El modelo de canal puede incorporarse de manera diferenciable mediante:

$$Y = h(X, H, N) \tag{4}$$

donde $H$ representa la respuesta del canal y $N$ el ruido aditivo. Para canales AWGN (Additive White Gaussian Noise), esta función se simplifica a:

$$Y = X + N, \quad N \sim \mathcal{N}(0, \sigma^2 \mathbf{I}) \tag{5}$$

Sin embargo, para canales más realistas con desvanecimiento Rayleigh o MIMO masivo, se requiere modelar:

$$Y = \mathbf{H} \cdot X + N, \quad \mathbf{H} \sim \mathcal{CN}(0, K_H) \tag{6}$$

donde $K_H$ es la matriz de covarianza del canal [93].

Una arquitectura JSCC avanzada para comunicaciones semánticas incorpora capas de atención y normalización por lotes. El codificador puede diseñarse como:

$$\begin{aligned}
h^{(0)} &= \text{Embedding}(S) \\
h^{(l)} &= \text{LayerNorm}(h^{(l-1)} + \text{MultiHeadAttention}(h^{(l-1)})) \\
h^{(l)} &= \text{LayerNorm}(h^{(l)} + \text{FFN}(h^{(l)})) \\
X &= \text{PowerNorm}(\text{Linear}(h^{(L)}))
\end{aligned} \tag{7}$$

donde $l = 1,\ldots,L$ son las capas de la red, $\text{FFN}$ denota una red feed-forward, y $\text{PowerNorm}$ asegura restricciones de potencia transmitida [94].

La normalización de potencia es crítica y se implementa como:

$$X_{norm} = \sqrt{n \cdot P} \cdot \frac{X}{\|X\|_2} \tag{8}$$

donde $n$ es la dimensión del espacio de señal y $P$ la potencia promedio permitida.

Para entrenamiento, se emplea una función de pérdida multiobjetivo que combina fidelidad de reconstrucción, eficiencia espectral y robustez:

$$\mathcal{L}_{total} = \alpha \cdot \mathcal{L}_{MSE} + \beta \cdot \mathcal{L}_{perceptual} + \gamma \cdot \mathcal{L}_{adversarial} + \delta \cdot \mathcal{L}_{rate} \tag{9}$$

donde:

$$\mathcal{L}_{MSE} = \mathbb{E}[\|S - \hat{S}\|^2] \tag{10}$$

$$\mathcal{L}_{perceptual} = \mathbb{E}[\|\Phi(S) - \Phi(\hat{S})\|^2] \tag{11}$$

$$\mathcal{L}_{adversarial} = \mathbb{E}[\log D(S)] + \mathbb{E}[\log(1 - D(\hat{S}))] \tag{12}$$

$$\mathcal{L}_{rate} = H(X) = -\mathbb{E}[\log p(X)] \tag{13}$$

$\Phi(\cdot)$ representa características extraídas por una red preentrenada (e.g., VGG o ResNet) para pérdidas perceptuales, y $D$ es un discriminador para entrenamiento adversarial [95].

Un aspecto innovador en JSCC neural para 6G es la incorporación de información semántica. Se puede formular un codificador semántico que extrae características de alto nivel:

$$\begin{aligned}
Z_{sem} &= \text{Encoder}_{semantic}(S) \\
Z_{importance} &= \text{Attention\_mask}(Z_{sem}) \\
X &= \text{Encoder}_{channel}(Z_{sem} \odot Z_{importance})
\end{aligned} \tag{14}$$

donde $\odot$ denota multiplicación elemento a elemento, y $Z_{importance}$ asigna pesos según la relevancia semántica [96].

Para canales con realimentación limitada, se puede incorporar un módulo de estimación de canal integrado:

$$\begin{aligned}
\hat{H} &= \text{EstimatorNet}(Y_{pilot}) \\
\hat{S} &= \text{Decoder}(Y, \hat{H})
\end{aligned} \tag{15}$$

El estimador de canal puede entrenarse conjuntamente mediante:

$$\mathcal{L}_{channel} = \mathbb{E}[\|H - \hat{H}\|^2] + \mathbb{E}[\|S - \hat{S}(Y, \hat{H})\|^2] \tag{16}$$

Esta formulación conjunta permite al sistema aprender representaciones óptimas del canal que son directamente útiles para la decodificación [97].

Para escenarios MIMO masivo, el codificador debe generar matrices de precodificación:

$$X = \mathbf{F} \cdot S, \quad \mathbf{F} \in \mathbb{C}^{N_t \times K} \tag{17}$$

donde $N_t$ es el número de antenas transmisoras y $K$ el rango de transmisión. La red neuronal puede aprender $\mathbf{F}$ adaptándose a las estadísticas del canal:

$$\mathbf{F} = \text{Precoder\_Net}(S, H_{CSI}) \tag{18}$$

donde $H_{CSI}$ es información de estado de canal disponible [98].

Finalmente, para garantizar robustez ante variaciones de SNR, se emplea entrenamiento multi-SNR:

$$\mathcal{L}_{robust} = \mathbb{E}_{SNR}[\mathbb{E}[d(S, \hat{S}_{SNR})]] \tag{19}$$

Este enfoque permite que la arquitectura JSCC neural se adapte dinámicamente a condiciones de canal variables, esencial para la confiabilidad ultra-alta requerida en aplicaciones 6G críticas [99].

## B. Redes de Atención Temporal para Estimación de Canal

La estimación precisa de canal es fundamental para receptores 6G operando en entornos de alta movilidad y con frecuencias milimétricas o terahercios. Las redes de atención temporal ofrecen capacidades superiores para capturar dependencias temporales complejas y variaciones no estacionarias del canal [100].

El problema de estimación de canal puede formularse como la estimación de la matriz de respuesta de canal $H(t)$ a partir de señales piloto y datos recibidos. En sistemas MIMO masivo, la dimensionalidad del problema escala con el número de antenas:

$$Y_{pilot}(t) = H(t) \cdot X_{pilot} + N(t) \tag{20}$$

donde $H(t) \in \mathbb{C}^{N_r \times N_t}$, con $N_r$ y $N_t$ siendo el número de antenas receptoras y transmisoras respectivamente [101].

Una arquitectura de red de atención temporal para estimación de canal consta de múltiples componentes. Primero, un embedding temporal de las observaciones:

$$E(t) = \text{Linear}(\text{concat}([\text{Re}(Y(t)), \text{Im}(Y(t))])) \tag{21}$$

Posteriormente, se aplica codificación posicional para mantener información temporal:

$$\begin{aligned}
PE(t,2i) &= \sin(t / 10000^{2i/d_{model}}) \\
PE(t,2i+1) &= \cos(t / 10000^{2i/d_{model}}) \\
E_{pos}(t) &= E(t) + PE(t)
\end{aligned} \tag{22}$$

donde $d_{model}$ es la dimensión del modelo y $i$ indexa las dimensiones del embedding [102].

El mecanismo de auto-atención temporal permite que la red pondere diferentes instantes temporales según su relevancia:

$$Q = E_{pos} \cdot W_Q, \quad K = E_{pos} \cdot W_K, \quad V = E_{pos} \cdot W_V \tag{23}$$

donde $W_Q$, $W_K$, $W_V \in \mathbb{R}^{d_{model} \times d_k}$ son matrices de proyección aprendibles.

Los scores de atención se calculan mediante:

$$\text{Attention}(Q,K,V) = \text{softmax}\!\left(\frac{Q \cdot K^T}{\sqrt{d_k}}\right) \cdot V \tag{24}$$

La normalización por $\sqrt{d_k}$ estabiliza los gradientes durante el entrenamiento [103].

Para capturar dependencias multi-escala, se emplea atención multi-cabeza:

$$\begin{aligned}
\text{head}_i &= \text{Attention}(Q \cdot W_Q^i, K \cdot W_K^i, V \cdot W_V^i) \\
\text{MultiHead}(Q,K,V) &= \text{concat}(\text{head}_1, \ldots, \text{head}_h) \cdot W_O
\end{aligned} \tag{25}$$

donde $h$ es el número de cabezas de atención y $W_O$ es una matriz de proyección de salida.

Una innovación clave para estimación de canal es la atención causal temporal, que evita fugas de información futuras:

$$\text{Attention}_{causal}(Q,K,V) = \text{softmax}\!\left(\text{Mask}\!\left(\frac{Q \cdot K^T}{\sqrt{d_k}}\right)\right) \cdot V \tag{26}$$

donde la matriz de máscara $\text{Mask}$ se define como:

$$\text{Mask}[i,j] = \begin{cases} 0 & \text{if } j \leq i \\ -\infty & \text{if } j > i \end{cases} \tag{27}$$

Esta formulación es crucial para estimación en tiempo real en receptores 6G [104].

Para modelar la evolución temporal del canal, se incorpora una capa LSTM bidireccional antes de la atención:

$$\begin{aligned}
\vec{h}_t &= \overrightarrow{\text{LSTM}}(E_{pos}(t), \vec{h}_{t-1}) \\
\overleftarrow{h}_t &= \overleftarrow{\text{LSTM}}(E_{pos}(t), \overleftarrow{h}_{t+1}) \\
h_t^{bi} &= \text{concat}([\vec{h}_t, \overleftarrow{h}_t])
\end{aligned} \tag{28}$$

La combinación de LSTM y atención permite capturar tanto dependencias secuenciales como relaciones de largo alcance [105].

Para canales con desvanecimiento selectivo en frecuencia, se extiende la arquitectura a atención espacio-temporal:

$$\hat{H}(t,f) = \text{Decoder}(\text{Attention}_{spatial}(\text{Attention}_{temporal}(E(t,f)))) \tag{29}$$

donde la dimensión frecuencial se modela mediante transformaciones adicionales.

La función de pérdida para entrenamiento combina error cuadrático medio y coherencia temporal:

$$\mathcal{L}_{estimation} = \mathbb{E}[\|H - \hat{H}\|_F^2] + \lambda \cdot \mathbb{E}[\|\Delta H - \Delta\hat{H}\|_F^2] \tag{30}$$

donde $\Delta H(t) = H(t) - H(t-1)$ captura la dinámica temporal y $\|\cdot\|_F$ denota la norma de Frobenius [106].

Para mejorar la robustez ante desvanecimientos profundos, se incorpora un mecanismo de atención consciente de incertidumbre:

$$\begin{aligned}
\alpha_t &= \text{softmax}(\text{Uncertainty\_Net}(E(t))) \\
\hat{H} &= \sum_t \alpha_t \cdot \hat{H}_t
\end{aligned} \tag{31}$$

donde $\text{Uncertainty\_Net}$ estima la confiabilidad de cada estimación temporal.

En escenarios de movilidad ultra-alta (e.g., comunicaciones vehiculares 6G a >500 km/h), el canal varía rápidamente según el modelo de Doppler:

$$H(t) = \sum_l \alpha_l \cdot \exp(j 2\pi f_{d,l} \cdot t) \cdot \mathbf{a}(\theta_l) \cdot \mathbf{a}^H(\phi_l) \tag{32}$$

donde $f_{d,l}$ son las frecuencias Doppler, $\alpha_l$ las ganancias de path, y $\mathbf{a}(\cdot)$ los vectores de dirección [107].

La red de atención puede especializarse para rastrear estos patrones mediante una capa de extracción Doppler:

$$\begin{aligned}
F_{doppler} &= \text{FFT}(\hat{H}(t)) \\
\text{Doppler\_features} &= \text{Conv1D}(|F_{doppler}|)
\end{aligned} \tag{33}$$

Finalmente, para reducir la complejidad computacional en despliegues edge, se emplea compresión de atención mediante núcleos lineales:

$$\text{Attention}_{linear}(Q,K,V) \approx \phi(Q) \cdot (\phi(K)^T \cdot V) \tag{34}$$

donde $\phi: \mathbb{R}^d \rightarrow \mathbb{R}^m$ es una transformación a un espacio de menor dimensión (típicamente $m \ll d$), permitiendo complejidad $O(m)$ en lugar de $O(d^2)$ [108][109].

## C. Autoencoders Variacionales para Compresión Semántica

Los autoencoders variacionales (VAE) representan una herramienta fundamental para compresión semántica en comunicaciones 6G, permitiendo la transmisión eficiente de información significativa en lugar de bits sin procesar. Esta aproximación es particularmente relevante para aplicaciones de realidad extendida (XR), hologramas móviles y gemelos digitales [110].

El framework probabilístico de los VAE se fundamenta en la maximización de la cota inferior de evidencia (ELBO, Evidence Lower Bound):

$$\log p_\theta(x) \geq \mathbb{E}_{q_\varphi(z|x)}[\log p_\theta(x|z)] - KL(q_\varphi(z|x) \| p(z)) \tag{35}$$

donde $x$ son los datos de entrada (e.g., imagen, video, señal), $z$ es la representación latente, $q_\varphi(z|x)$ es el codificador (distribución de inferencia aproximada), $p_\theta(x|z)$ es el decodificador (distribución generativa), y $p(z)$ es la distribución prior (típicamente $\mathcal{N}(0,\mathbf{I})$) [111].

El codificador VAE mapea los datos de entrada a parámetros de una distribución Gaussiana en el espacio latente:

$$\begin{aligned}
\mu(x), \log \sigma^2(x) &= \text{Encoder}_\varphi(x) \\
z &\sim \mathcal{N}(\mu(x), \sigma^2(x) \cdot \mathbf{I})
\end{aligned} \tag{36}$$

El truco de reparametrización permite el backpropagation a través del muestreo estocástico:

$$z = \mu(x) + \sigma(x) \odot \varepsilon, \quad \varepsilon \sim \mathcal{N}(0, \mathbf{I}) \tag{37}$$

Esta formulación es diferenciable y permite optimización end-to-end [112].

Para compresión semántica en comunicaciones 6G, se extiende el VAE estándar incorporando información de canal y restricciones de tasa. La función objetivo modificada es:

$$\begin{aligned}
\mathcal{L}_{semantic\text{-}VAE} = &\; \mathbb{E}[\|x - \hat{x}\|^2] + \beta \cdot KL(q_\varphi(z|x) \| p(z)) \\
&+ \gamma \cdot \mathbb{E}_H[\|x - \hat{x}_{channel}\|^2] + \lambda \cdot H(z)
\end{aligned} \tag{38}$$

donde:
- El primer término asegura fidelidad de reconstrucción
- El segundo término (con parámetro $\beta$) regulariza el espacio latente
- El tercer término considera degradación por canal de comunicación
- El cuarto término controla la tasa de compresión mediante entropía $H(z)$ [113]

Para transmisión sobre canales ruidosos, el modelo incorpora un canal diferenciable:

$$\begin{aligned}
z_{transmitted} &= z + n, \quad n \sim \mathcal{N}(0, \sigma_{channel}^2 \cdot \mathbf{I}) \\
\hat{x}_{channel} &= \text{Decoder}_\theta(z_{transmitted})
\end{aligned} \tag{39}$$

Un VAE jerárquico permite capturar estructuras semánticas multi-escala:

$$p_\theta(x, z_1, \ldots, z_L) = p_\theta(x|z_1) \cdot \prod_{l=1}^{L-1} p_\theta(z_l|z_{l+1}) \cdot p(z_L) \tag{40}$$

donde $z_1,\ldots,z_L$ son variables latentes en diferentes niveles de abstracción [114].

El codificador jerárquico se define recursivamente:

$$q_\varphi(z_1, \ldots, z_L|x) = q_\varphi(z_1|x) \cdot \prod_{l=2}^{L} q_\varphi(z_l|z_{l-1}) \tag{41}$$

Esta arquitectura permite representaciones semánticas desde características de bajo nivel (texturas, bordes) hasta conceptos de alto nivel (objetos, escenas).

Para aplicaciones de comunicación visual 6G, se incorpora un modelo de atención semántica que identifica regiones de interés:

$$\begin{aligned}
A(x) &= \text{softmax}(W_a \cdot \tanh(W_x \cdot x)) \\
z_{weighted} &= A(x) \odot \text{Encoder}_\varphi(x)
\end{aligned} \tag{42}$$

donde $W_a$ y $W_x$ son matrices de peso aprendibles, y $A(x)$ es un mapa de atención [115].

La cuantización de la representación latente es crítica para transmisión digital. Se emplea cuantización vectorial aprendida:

$$\begin{aligned}
z_q &= \arg\min_{e_k \in \mathcal{C}} \|z - e_k\|^2 \\
\mathcal{L}_{vq} &= \|\text{sg}[z] - e\|^2 + \beta \cdot \|z - \text{sg}[e]\|^2
\end{aligned} \tag{43}$$

donde $\text{sg}[\cdot]$ denota stop-gradient, $\mathcal{C} = \{e_1,\ldots,e_K\}$ es un conjunto de vectores prototipo aprendibles, y el segundo término evita colapso del espacio latente [116].

Para comunicaciones semánticas orientadas a tareas específicas, se incorpora un clasificador o detector en el espacio latente:

$$\begin{aligned}
\mathcal{L}_{task} &= \text{CrossEntropy}(f_{task}(z), y_{true}) \\
\mathcal{L}_{total} &= \mathcal{L}_{semantic\text{-}VAE} + \alpha \cdot \mathcal{L}_{task}
\end{aligned} \tag{44}$$

Esta formulación permite que el VAE aprenda representaciones optimizadas para la tarea downstream, reduciendo drásticamente los requisitos de ancho de banda [117].

En escenarios multimodales (e.g., transmisión conjunta de video, audio, datos sensoriales), se emplea un VAE multi-modal:

$$\begin{aligned}
p(x_v, x_a|z) &= p(x_v|z) \cdot p(x_a|z) \\
q(z|x_v, x_a) &= \text{ProductOfExperts}(q(z|x_v), q(z|x_a))
\end{aligned} \tag{45}$$

donde $x_v$ y $x_a$ representan modalidades visuales y auditivas respectivamente [118].

Para adaptación a condiciones de canal variables, se propone un VAE consciente de SNR:

$$\begin{aligned}
z_\mu(x, SNR), z_\sigma(x, SNR) &= \text{Encoder}_\varphi(x, SNR) \\
\mathcal{L} &= \mathbb{E}_{SNR}[\mathcal{L}_{semantic\text{-}VAE}(x, SNR)]
\end{aligned} \tag{46}$$

El modelo aprende a ajustar el nivel de compresión y redundancia según las condiciones del canal, maximizando la calidad percibida bajo restricciones de tasa variables [119].

## D. Arquitecturas Híbridas CNN-Transformer

Las arquitecturas híbridas que combinan redes neuronales convolucionales (CNN) con mecanismos Transformer han emergido como soluciones potentes para procesamiento de señales en receptores 6G, aprovechando las fortalezas complementarias de ambos paradigmas: las CNN para extracción de características locales y los Transformers para modelado de dependencias globales [120].

La arquitectura básica híbrida CNN-Transformer puede formalizarse como una composición de operaciones:

$$\begin{aligned}
h_{CNN} &= f_{CNN}(x; \theta_{CNN}) \\
h_{Transformer} &= f_{Transformer}(h_{CNN}; \theta_{Transformer}) \\
\hat{y} &= g_{output}(h_{Transformer}; \theta_{output})
\end{aligned} \tag{47}$$

donde $x$ es la entrada (e.g., señal IQ en el dominio tiempo-frecuencia), $f_{CNN}$ extrae características espaciales/espectrales, $f_{Transformer}$ modela dependencias globales, y $g_{output}$ genera la salida final [121].

Las capas convolucionales operan mediante:

$$h_l^{(i,j)} = \sigma\!\left(\sum_m \sum_n W_l^{(m,n)} \cdot h_{l-1}^{(i+m,j+n)} + b_l\right) \tag{48}$$

donde $W_l$ son filtros convolucionales, $b_l$ son sesgos, y $\sigma(\cdot)$ es una función de activación no lineal (típicamente ReLU o GELU).

Para señales de comunicación, se emplean convoluciones en el dominio tiempo-frecuencia:

$$\begin{aligned}
S_{TF} &= \text{STFT}(s(t)) \\
h_{TF} &= \text{Conv2D}(S_{TF})
\end{aligned} \tag{49}$$

donde STFT denota la transformada de Fourier de tiempo corto, generando una representación espectrograma [122].

El módulo Transformer subsecuente procesa los parches de características CNN:

$$\begin{aligned}
\text{Patches} &= \text{Reshape}(h_{CNN}) \rightarrow \{p_1, p_2, \ldots, p_N\} \\
E_i &= \text{Linear}(p_i) + PE_i
\end{aligned} \tag{50}$$

donde cada parche $p_i$ se proyecta linealmente y se le añade codificación posicional $PE_i$.

La auto-atención en el Transformer se formula como:

$$\begin{aligned}
Q &= E \cdot W_Q, \quad K = E \cdot W_K, \quad V = E \cdot W_V \\
\text{Attention}(Q,K,V) &= \text{softmax}\!\left(\frac{Q \cdot K^T}{\sqrt{d_k}}\right) \cdot V
\end{aligned} \tag{51}$$

Para receptores 6G procesando señales de banda ultra-ancha, se introduce una variante con atención factorizada espacio-frecuencial:

$$\text{Attention}_{hybrid} = \text{Attention}_{spatial} \circ \text{Attention}_{spectral} \tag{52}$$

donde cada componente opera en su dominio respectivo, reduciendo complejidad de $O(N^2)$ a $O(2N\sqrt{N})$ [123].

Una innovación arquitectónica es el uso de convoluciones depthwise separables antes del Transformer:

$$\begin{aligned}
h_{depthwise} &= \text{DWConv}(h_{l-1}) \\
h_{pointwise} &= \text{PWConv}(h_{depthwise}) \\
h_l &= \text{LayerNorm}(h_{pointwise})
\end{aligned} \tag{53}$$

donde $\text{DWConv}$ aplica filtros independientes por canal y $\text{PWConv}$ mezcla información entre canales, reduciendo parámetros significativamente [124].

Para ecualización de canal en MIMO masivo, la arquitectura híbrida procesa la matriz de señal recibida:

$$\begin{aligned}
Y &\in \mathbb{C}^{N_r \times T} \xrightarrow{\text{CNN}} \text{Features} \in \mathbb{R}^{d \times T'} \\
\text{Features} &\xrightarrow{\text{Transformer}} \text{Context} \in \mathbb{R}^{d \times T'} \\
\text{Context} &\xrightarrow{\text{Decoder}} \hat{S} \in \mathbb{C}^{N_t \times T}
\end{aligned} \tag{54}$$

donde $N_r$ y $N_t$ son antenas RX/TX, $T$ es la duración temporal, y $d$ es la dimensión de características.

El Transformer emplea atención multi-cabeza con cabezas especializadas:

$$\begin{aligned}
&\text{head}_1: \text{Attention}_{temporal}(Q,K,V) \quad \rightarrow \text{ modela evolución temporal} \\
&\text{head}_2: \text{Attention}_{spatial}(Q,K,V) \quad \rightarrow \text{ modela correlaciones entre antenas} \\
&\text{head}_3: \text{Attention}_{cross}(Q,K,V) \quad \rightarrow \text{ modela interdependencias cruzadas} \\
&\text{Output} = \text{Concat}(\text{head}_1, \text{head}_2, \text{head}_3) \cdot W_O
\end{aligned} \tag{55}$$

Para eficiencia computacional en hardware edge, se implementa atención dispersa (sparse attention):

$$\text{Attention}_{sparse}(Q,K,V) = \text{softmax}\!\left(\text{Mask}_{sparse} \odot \frac{Q \cdot K^T}{\sqrt{d_k}}\right) \cdot V \tag{56}$$

donde $\text{Mask}_{sparse}$ restringe la atención a patrones específicos (e.g., local, estriado, global) [125].

En detección de símbolos para modulaciones de orden alto (e.g., 1024-QAM en 6G), el decoder híbrido se formula:

$$P(s_k|Y) = \text{softmax}(\text{MLP}(\text{Transformer}(\text{CNN}(Y)))) \tag{57}$$

Esta arquitectura aprende a detectar símbolos considerando interferencia inter-símbolo, distorsión de canal y patrones temporales complejos.

Una formulación avanzada incorpora conexiones residuales densas entre CNN y Transformer:

$$\begin{aligned}
h_T^{(0)} &= h_{CNN} \\
h_T^{(l)} &= \text{Transformer\_layer}(h_T^{(l-1)} + \alpha \cdot h_{CNN})
\end{aligned} \tag{58}$$

donde $\alpha$ es un parámetro aprendible que controla la influencia de características CNN en cada capa Transformer [126].

Para sincronización temporal fina en receptores 6G, se emplea una arquitectura de regresión temporal:

$$\hat{\tau}, \hat{f}_o = \text{RegressorHead}(h_{Transformer}) \tag{59}$$

donde $\hat{\tau}$ es el offset temporal estimado y $\hat{f}_o$ el offset de frecuencia, permitiendo sincronización sub-muestra con precisión superior a métodos clásicos [127].

La función de pérdida para entrenamiento end-to-end combina múltiples objetivos:

$$\begin{aligned}
\mathcal{L}_{total} &= \mathcal{L}_{reconstruction} + \lambda_1 \cdot \mathcal{L}_{attention} + \lambda_2 \cdot \mathcal{L}_{diversity} \\
\mathcal{L}_{attention} &= -\sum_i H(A_i) \quad \text{(maximiza entropía de atención)} \\
\mathcal{L}_{diversity} &= \sum_{i \neq j} \langle \text{head}_i, \text{head}_j \rangle \quad \text{(minimiza correlación entre cabezas)}
\end{aligned} \tag{60}$$

Esta formulación promueve atención difusa y cabezas especializadas diversas [128][129].

## E. Mecanismos de Adaptación en Tiempo Real

La adaptación en tiempo real es un requisito crítico para receptores 6G que deben operar en entornos dinámicos con variaciones rápidas de canal, movilidad extrema, interferencias impredecibles y requisitos heterogéneos de QoS. Los mecanismos de adaptación neuronal permiten ajuste continuo de parámetros del receptor sin reentrenamiento offline costoso [130].

El marco fundamental para adaptación online se basa en meta-aprendizaje (learning to learn), donde el sistema aprende estrategias de adaptación que generalizan a nuevas condiciones:

$$\begin{aligned}
\theta^* &= \arg\min_\theta \mathbb{E}_{\mathcal{T} \sim p(\mathcal{T})}[\mathcal{L}_\mathcal{T}(f_{\theta'})] \\
\theta' &= \theta - \alpha \nabla_\theta \mathcal{L}_\mathcal{T}^{support}(f_\theta)
\end{aligned} \tag{61}$$

donde $\mathcal{T}$ representa una tarea (e.g., un canal específico), $\mathcal{L}_\mathcal{T}^{support}$ es la pérdida en datos de soporte, y $\alpha$ es la tasa de adaptación [131].

El algoritmo Model-Agnostic Meta-Learning (MAML) aplicado a receptores 6G se implementa como:

1. Inicialización: $\theta_0$
2. Para cada episodio:
   - a. Muestrear canal $H_i \sim p(H)$
   - b. Recopilar datos de piloto: $\mathcal{D}_i^{support}$
   - c. Adaptación rápida: $\theta_i' = \theta - \alpha \nabla_\theta \mathcal{L}(f_\theta, \mathcal{D}_i^{support})$
   - d. Evaluar en datos de consulta: $\mathcal{L}_i^{query} = \mathcal{L}(f_{\theta_i'}, \mathcal{D}_i^{query})$
3. Meta-actualización: $\theta \leftarrow \theta - \beta \nabla_\theta \sum_i \mathcal{L}_i^{query}$ $\tag{62}$

Este procedimiento permite adaptación con pocos ejemplos (few-shot adaptation) [132].

Para adaptación continua sin catastrofic forgetting, se emplea Elastic Weight Consolidation (EWC):

$$\mathcal{L}_{EWC}(\theta) = \mathcal{L}_{current}(\theta) + \sum_i \frac{\lambda}{2} \cdot F_i \cdot (\theta_i - \theta_i^*)^2 \tag{63}$$

donde $F_i$ es la información de Fisher para el parámetro $i$, $\theta_i^*$ son parámetros previamente aprendidos, y $\lambda$ controla la importancia de preservar conocimiento previo [133].

La matriz de Fisher se aproxima mediante:

$$F_i = \mathbb{E}_x\!\left[\left(\frac{\partial \log p(x|\theta)}{\partial \theta_i}\right)^2\right] \tag{64}$$

Para receptores adaptativos basados en gradientes online, se implementa adaptación de tasa de aprendizaje mediante Adam optimizador con momento adaptativo:

$$\begin{aligned}
m_t &= \beta_1 \cdot m_{t-1} + (1 - \beta_1) \cdot g_t \\
v_t &= \beta_2 \cdot v_{t-1} + (1 - \beta_2) \cdot g_t^2 \\
\theta_t &= \theta_{t-1} - \eta \cdot \frac{m_t}{\sqrt{v_t} + \varepsilon}
\end{aligned} \tag{65}$$

donde $g_t = \nabla_\theta \mathcal{L}_t$ es el gradiente en tiempo $t$, $m_t$ y $v_t$ son estimaciones de primer y segundo momento, y $\eta$ es la tasa de aprendizaje base [134].

Un enfoque innovador para adaptación en receptores 6G es la red neuronal auto-modificante (self-modifying neural network):

$$\begin{aligned}
\theta_{t+1} &= \theta_t + \Delta\theta_t \\
\Delta\theta_t &= \text{HyperNetwork}(state_t, \theta_t)
\end{aligned} \tag{66}$$

donde una hiperred genera actualizaciones de parámetros basándose en el estado actual del sistema (SNR, velocidad Doppler, nivel de interferencia) [135].

Para estimación de canal adaptativa, se formula un filtro de Kalman neuronal:

$$\begin{aligned}
\hat{H}_{t|t-1} &= f_{transition}(\hat{H}_{t-1|t-1}) & &\text{(predicción)} \\
K_t &= P_{t|t-1} \cdot H_{obs}^T \cdot (H_{obs} \cdot P_{t|t-1} \cdot H_{obs}^T + R)^{-1} & &\text{(ganancia)} \\
\hat{H}_{t|t} &= \hat{H}_{t|t-1} + K_t \cdot (y_t - H_{obs} \cdot \hat{H}_{t|t-1}) & &\text{(actualización)}
\end{aligned} \tag{67}$$

donde $f_{transition}$ es una red neuronal que aprende la dinámica del canal, reemplazando modelos paramétricos rígidos [136].

La covarianza del error de estimación se actualiza mediante:

$$P_{t|t} = (\mathbf{I} - K_t \cdot H_{obs}) \cdot P_{t|t-1} \tag{68}$$

Para módems cognitivos 6G que deben seleccionar dinámicamente esquemas de modulación y codificación, se emplea aprendizaje por refuerzo profundo con Deep Q-Network (DQN):

$$\begin{aligned}
Q(s,a; \theta) &\approx Q^*(s,a) \\
\mathcal{L}(\theta) &= \mathbb{E}\!\left[\left(r + \gamma \cdot \max_{a'} Q(s',a'; \theta^-) - Q(s,a; \theta)\right)^2\right]
\end{aligned} \tag{69}$$

donde $s$ es el estado (condiciones de canal), $a$ es la acción (MCS seleccionado), $r$ es la recompensa (throughput, latencia), $\gamma$ es el factor de descuento, y $\theta^-$ son parámetros de red objetivo [137].

Una extensión para acciones continuas (e.g., ajuste de potencia, beamforming) emplea Actor-Critic:

$$\begin{aligned}
&\text{Actor: } \pi(a|s; \theta_\pi) \\
&\text{Critic: } V(s; \theta_V) \\
&\nabla_{\theta_\pi} J(\theta_\pi) \approx \mathbb{E}[\nabla_{\theta_\pi} \log \pi(a|s) \cdot A(s,a)] \\
&A(s,a) = r + \gamma \cdot V(s'; \theta_V) - V(s; \theta_V)
\end{aligned} \tag{70}$$

donde $A(s,a)$ es la función de ventaja que indica cuánto mejor es la acción $a$ respecto al valor esperado [138].

Para adaptación ultra-rápida en escenarios de alta movilidad (V2X), se propone una arquitectura de memoria externa diferenciable:

$$\begin{aligned}
read_t &= \sum_i w_t^r(i) \cdot M_t(i) \\
M_t(i) &= M_{t-1}(i) + w_t^w(i) \cdot k_t \\
w_t^r &= \text{softmax}(\mathcal{K}(k_t, M_{t-1}))
\end{aligned} \tag{71}$$

donde $M_t$ es una matriz de memoria, $k_t$ es un vector de consulta, y $\mathcal{K}(\cdot,\cdot)$ es una función de similitud (e.g., coseno) [139].

Esta memoria permite al receptor recordar y recuperar rápidamente configuraciones óptimas para canales previamente encontrados.

Finalmente, para garantizar estabilidad en adaptación continua, se implementa un mecanismo de control proporcional-integral (PI):

$$\begin{aligned}
\eta_t &= \eta_{base} + K_p \cdot e_t + K_i \cdot \sum_{\tau=1}^{t} e_\tau \\
e_t &= \mathcal{L}_{target} - \mathcal{L}_t
\end{aligned} \tag{72}$$

donde $\eta_t$ es la tasa de aprendizaje adaptativa, $e_t$ es el error respecto a una pérdida objetivo, y $K_p$, $K_i$ son ganancias proporcional e integral. Este control evita oscilaciones y divergencia durante la adaptación online [140].

La integración de todos estos mecanismos permite a los receptores 6G neuronales adaptarse continuamente a entornos dinámicos mientras mantienen rendimiento óptimo, robustez y eficiencia energética.
