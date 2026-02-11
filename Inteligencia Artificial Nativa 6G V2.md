# Inteligencia Artificial Nativa en el Nivel Físico de Redes 6G: Fundamentos, Arquitecturas y Desafíos

**Resumen**—Las redes de sexta generación (6G) representan un cambio de paradigma hacia arquitecturas nativas de inteligencia artificial (IA) donde el aprendizaje automático y las redes neuronales profundas están integrados desde el nivel físico hasta las capas superiores del protocolo de comunicación. Este artículo presenta una revisión exhaustiva de las técnicas de IA nativa aplicadas a la capa física de 6G, incluyendo estimación de canal mediante aprendizaje profundo, formación de haces adaptativa (beamforming), optimización de sistemas MIMO masivos, superficies inteligentes reconfigurables (RIS), y comunicaciones semánticas. Se profundiza en los fundamentos matemáticos, las arquitecturas de redes neuronales empleadas, los algoritmos de optimización, y se analizan los desafíos técnicos y direcciones futuras de investigación. El trabajo sintetiza contribuciones recientes de la literatura IEEE y proporciona un marco conceptual riguroso para comprender la transformación hacia sistemas 6G completamente autónomos y adaptativos.

**Palabras clave**—6G, inteligencia artificial nativa, nivel físico, aprendizaje profundo, estimación de canal, beamforming, MIMO masivo, superficies inteligentes reconfigurables, RIS, comunicaciones semánticas.

---

## I. INTRODUCCIÓN

### A. Contexto y Motivación

La evolución de las redes móviles ha seguido una trayectoria de incremento exponencial en velocidad de datos, reducción de latencia y densificación de dispositivos conectados [1]. Mientras que la quinta generación (5G) introdujo conceptos como comunicaciones ultra-confiables de baja latencia (URLLC) y comunicaciones masivas tipo máquina (mMTC), las redes de sexta generación (6G) prometen ir más allá, integrando requisitos emergentes como tasas de datos del orden de terabits por segundo (Tbps), latencias sub-milisegundo, eficiencia energética extrema, y cobertura ubicua en entornos espacio-aire-tierra-mar [2], [3].

Un componente fundamental que diferencia a 6G de sus predecesoras es la integración nativa de inteligencia artificial (IA) en todas las capas de la arquitectura de red [4]. A diferencia de 5G, donde la IA se emplea principalmente como herramienta de optimización externa, en 6G la IA se convierte en un elemento estructural embebido desde el nivel físico (PHY) hasta las capas de aplicación, permitiendo que la red aprenda, razone y se adapte autónomamente en tiempo real [5], [6].

### B. IA Nativa: Definición y Alcance

El concepto de "IA nativa" (AI-native) en el contexto de 6G se refiere a arquitecturas de red donde los algoritmos de aprendizaje automático, especialmente las redes neuronales profundas (DNN), no son componentes agregados, sino partes intrínsecas del diseño del sistema [7]. En el nivel físico, esto implica:

1. **Aprendizaje adaptativo en tiempo real**: La capa física ajusta dinámicamente parámetros como modulación, codificación, conformación de haces (beamforming), y asignación de recursos basándose en observaciones del entorno de radio [8].

2. **Sustitución de algoritmos clásicos**: Técnicas tradicionales basadas en estimadores de máxima verosimilitud (ML) o mínimos cuadrados (LS) son reemplazadas o aumentadas por modelos de aprendizaje profundo que capturan no-linealidades complejas del canal [9], [10].

3. **Colaboración distribuida**: Múltiples agentes de IA distribuidos en la red (en estaciones base, dispositivos de usuario, y superficies inteligentes) colaboran mediante aprendizaje federado o multi-agente para optimizar el rendimiento global [11], [12].

### C. Estructura del Artículo

El presente artículo está organizado de la siguiente manera: La Sección II presenta los fundamentos matemáticos del nivel físico de 6G y establece el marco teórico para la integración de IA. La Sección III aborda en profundidad la estimación de canal mediante aprendizaje profundo. La Sección IV analiza técnicas de beamforming y MIMO masivo con IA. La Sección V explora superficies inteligentes reconfigurables controladas por IA. La Sección VI discute comunicaciones semánticas y conscientes de intención. La Sección VII presenta desafíos abiertos y direcciones futuras. Finalmente, la Sección VIII concluye el trabajo.

---

## II. FUNDAMENTOS MATEMÁTICOS DEL NIVEL FÍSICO Y MODELADO DE CANAL EN 6G

### A. Modelo de Sistema y Representación Matemática

Consideremos un sistema de comunicación inalámbrica genérico donde un transmisor envía información a través de un canal inalámbrico hacia un receptor. En el dominio de la banda base, la señal recibida en el instante discreto $n$ puede expresarse como [13]:

$$
y[n] = h[n] \ast x[n] + w[n]
$$

donde:
- $y[n] \in \mathbb{C}^{N_r}$ es el vector de señal recibida con $N_r$ antenas receptoras,
- $h[n] \in \mathbb{C}^{N_r \times N_t}$ representa la respuesta al impulso del canal MIMO (Multiple-Input Multiple-Output) con $N_t$ antenas transmisoras,
- $x[n] \in \mathbb{C}^{N_t}$ es el vector de señal transmitida,
- $w[n] \sim \mathcal{CN}(0, \sigma^2 I_{N_r})$ denota el ruido aditivo gaussiano blanco complejo (AWGN),
- $\ast$ representa la operación de convolución.

En sistemas MIMO masivos para 6G, donde $N_t, N_r \gg 1$ (típicamente cientos o miles de antenas), el canal puede modelarse en frecuencia mediante [14]:

$$
\mathbf{Y} = \mathbf{H}\mathbf{X} + \mathbf{W}
$$

donde $\mathbf{H} \in \mathbb{C}^{N_r \times N_t}$ es la matriz de canal, $\mathbf{X} \in \mathbb{C}^{N_t \times K}$ contiene las señales transmitidas a $K$ usuarios, y $\mathbf{W}$ es la matriz de ruido.

### B. Modelado Estocástico del Canal

El canal inalámbrico de 6G exhibe características de propagación complejas debido a bandas de frecuencia extendidas (sub-THz, THz) y entornos heterogéneos. El modelo de canal estocástico más ampliamente adoptado es el modelo de dispersión de cluster (cluster-scattering) [15]:

$$
\mathbf{H} = \sum_{l=1}^{L} \sum_{k=1}^{K_l} \alpha_{l,k} \mathbf{a}_r(\theta_{l,k}^r, \phi_{l,k}^r) \mathbf{a}_t^H(\theta_{l,k}^t, \phi_{l,k}^t)
$$

donde:
- $L$ es el número de clusters de dispersión,
- $K_l$ es el número de rayos en el cluster $l$,
- $\alpha_{l,k} \sim \mathcal{CN}(0, \sigma_{l,k}^2)$ representa el coeficiente de ganancia compleja del rayo $k$ en el cluster $l$,
- $\mathbf{a}_r(\theta, \phi) \in \mathbb{C}^{N_r}$ y $\mathbf{a}_t(\theta, \phi) \in \mathbb{C}^{N_t}$ son los vectores de respuesta de antena (array response vectors) en recepción y transmisión, respectivamente,
- $\theta$ y $\phi$ denotan los ángulos de azimut y elevación.

Para arreglos lineales uniformes (ULA), el vector de respuesta tiene la forma [16]:

$$
\mathbf{a}(\theta) = \frac{1}{\sqrt{N}} \begin{bmatrix} 1 \\ e^{j 2\pi \frac{d}{\lambda} \sin\theta} \\ \vdots \\ e^{j 2\pi \frac{d}{\lambda} (N-1)\sin\theta} \end{bmatrix}
$$

donde $d$ es el espaciado entre antenas, $\lambda$ es la longitud de onda, y $N$ es el número de elementos de antena.

### C. Limitaciones de Enfoques Clásicos

Los métodos tradicionales de estimación de canal y procesamiento de señales en el nivel físico enfrentan desafíos significativos en 6G [17]:

1. **Alta dimensionalidad**: Sistemas con MIMO masivo y anchos de banda extremos resultan en matrices de canal de dimensiones prohibitivamente grandes.

2. **No-linealidades**: Efectos de hardware (distorsión de amplificadores, acoplamiento mutuo de antenas) y propagación no-lineal en bandas THz no se capturan adecuadamente con modelos lineales.

3. **Variabilidad temporal**: Movilidad de alta velocidad y entornos dinámicos requieren adaptación en escalas de tiempo de milisegundos.

4. **Complejidad computacional**: Algoritmos óptimos como el filtro de Kalman extendido (EKF) o técnicas de optimización convexa tienen complejidad $O(N^3)$, inviable para MIMO masivo en tiempo real.

Estos desafíos motivan la adopción de técnicas de aprendizaje automático, que pueden aprender mapeos complejos directamente de los datos sin requerir modelos analíticos explícitos [18], [19].

---

## III. ESTIMACIÓN DE CANAL MEDIANTE APRENDIZAJE PROFUNDO

### A. Formulación del Problema de Estimación

La estimación de canal es un problema fundamental en comunicaciones inalámbricas. Dado un conjunto de símbolos piloto conocidos $\mathbf{X}_p \in \mathbb{C}^{N_t \times P}$ transmitidos y la señal recibida correspondiente $\mathbf{Y}_p \in \mathbb{C}^{N_r \times P}$, el objetivo es estimar la matriz de canal $\hat{\mathbf{H}}$ que minimice una métrica de error, típicamente el error cuadrático medio (MSE) [20]:

$$
\hat{\mathbf{H}}_{LS} = \mathbf{Y}_p \mathbf{X}_p^H (\mathbf{X}_p \mathbf{X}_p^H)^{-1}
$$

El estimador de mínimos cuadrados (LS) es no sesgado pero tiene alta varianza en escenarios de baja relación señal-ruido (SNR). El estimador de error cuadrático medio mínimo (MMSE) mejora el rendimiento incorporando información estadística del canal [21]:

$$
\hat{\mathbf{H}}_{MMSE} = \mathbf{R}_{\mathbf{H}} (\mathbf{R}_{\mathbf{H}} + \sigma^2 (\mathbf{X}_p \mathbf{X}_p^H)^{-1})^{-1} \hat{\mathbf{H}}_{LS}
$$

donde $\mathbf{R}_{\mathbf{H}} = \mathbb{E}[\mathbf{H}\mathbf{H}^H]$ es la matriz de covarianza del canal. Sin embargo, $\mathbf{R}_{\mathbf{H}}$ raramente se conoce en la práctica y su estimación requiere estadísticas de segundo orden difíciles de obtener [22].

### B. Arquitecturas de Redes Neuronales para Estimación de Canal

#### 1) Redes Neuronales Profundas (DNN)

Las DNN pueden aprender directamente el mapeo no-lineal de señales recibidas a estimaciones de canal sin requerir inversiones de matrices ni conocimiento estadístico a priori [23]. Una arquitectura DNN típica para estimación de canal consta de [24]:

- **Capa de entrada**: Vectoriza las componentes real e imaginaria de $\mathbf{Y}_p$: $\mathbf{z}_{in} = [\text{Re}(\text{vec}(\mathbf{Y}_p)); \text{Im}(\text{vec}(\mathbf{Y}_p))] \in \mathbb{R}^{2N_rP}$.

- **Capas ocultas**: $L$ capas completamente conectadas (fully connected) con funciones de activación no-lineales:

$$
\mathbf{z}_{l+1} = \sigma(\mathbf{W}_l \mathbf{z}_l + \mathbf{b}_l), \quad l = 1, \ldots, L
$$

donde $\mathbf{W}_l \in \mathbb{R}^{d_{l+1} \times d_l}$ son las matrices de pesos, $\mathbf{b}_l \in \mathbb{R}^{d_{l+1}}$ son los vectores de sesgo, y $\sigma(\cdot)$ es una función de activación no-lineal (ReLU, Leaky ReLU, ELU) [25].

- **Capa de salida**: Genera la estimación del canal: $\hat{\mathbf{h}} = [\text{Re}(\text{vec}(\hat{\mathbf{H}})); \text{Im}(\text{vec}(\hat{\mathbf{H}}))] \in \mathbb{R}^{2N_rN_t}$.

La función de pérdida utilizada para entrenar la red es típicamente el MSE normalizado [26]:

$$
\mathcal{L}(\Theta) = \frac{1}{B} \sum_{i=1}^{B} \frac{\|\mathbf{h}_i - \hat{\mathbf{h}}_i(\Theta)\|^2}{\|\mathbf{h}_i\|^2}
$$

donde $\Theta$ representa todos los parámetros entrenables de la red, $B$ es el tamaño del lote (batch size), y la normalización previene el sesgo hacia canales con mayor energía.

#### 2) Redes Neuronales Convolucionales (CNN)

Las CNN explotan la estructura espacial de las matrices de canal, especialmente útil en sistemas con múltiples subportadoras OFDM donde existe correlación en frecuencia [27]. La arquitectura consiste en [28]:

$$
\mathbf{Z}_{l+1} = \sigma(\mathbf{W}_l \ast \mathbf{Z}_l + \mathbf{b}_l)
$$

donde $\ast$ denota la operación de convolución 2D, y $\mathbf{Z}_l$ representa los mapas de características (feature maps) en la capa $l$. Los filtros convolucionales capturan patrones locales en el dominio frecuencia-espacio, reduciendo significativamente el número de parámetros comparado con DNN completamente conectadas [29].

Una arquitectura CNN avanzada para estimación de canal en OFDM incluye [30]:

- Capas de convolución con filtros de tamaño $3 \times 3$ y stride $1$,
- Normalización por lotes (batch normalization) después de cada capa convolucional,
- Capas residuales (residual connections) para mitigar el problema de gradiente desvaneciente:

$$
\mathbf{Z}_{l+1} = \mathbf{Z}_l + \mathcal{F}(\mathbf{Z}_l; \{\mathbf{W}_l\})
$$

donde $\mathcal{F}$ representa un bloque de capas convolucionales.

#### 3) Redes Recurrentes (RNN) y LSTM

Para canales variantes en el tiempo, las redes recurrentes capturan dependencias temporales [31]. Una celda LSTM (Long Short-Term Memory) se define mediante [32]:

$$
\begin{aligned}
\mathbf{f}_t &= \sigma_g(\mathbf{W}_f \mathbf{x}_t + \mathbf{U}_f \mathbf{h}_{t-1} + \mathbf{b}_f) \\
\mathbf{i}_t &= \sigma_g(\mathbf{W}_i \mathbf{x}_t + \mathbf{U}_i \mathbf{h}_{t-1} + \mathbf{b}_i) \\
\mathbf{o}_t &= \sigma_g(\mathbf{W}_o \mathbf{x}_t + \mathbf{U}_o \mathbf{h}_{t-1} + \mathbf{b}_o) \\
\tilde{\mathbf{c}}_t &= \sigma_c(\mathbf{W}_c \mathbf{x}_t + \mathbf{U}_c \mathbf{h}_{t-1} + \mathbf{b}_c) \\
\mathbf{c}_t &= \mathbf{f}_t \odot \mathbf{c}_{t-1} + \mathbf{i}_t \odot \tilde{\mathbf{c}}_t \\
\mathbf{h}_t &= \mathbf{o}_t \odot \sigma_h(\mathbf{c}_t)
\end{aligned}
$$

donde $\mathbf{f}_t$, $\mathbf{i}_t$, $\mathbf{o}_t$ son las puertas de olvido, entrada y salida respectivamente; $\mathbf{c}_t$ es el estado de celda; $\mathbf{h}_t$ es el estado oculto; $\odot$ denota producto elemento a elemento; y $\sigma_g$, $\sigma_c$, $\sigma_h$ son funciones de activación (típicamente sigmoide para puertas y tanh para estados).

### C. ICENet: Estimación Adaptativa Basada en Capas Implícitas

Recientemente, se propuso ICENet (Implicit-layer Channel Estimation Network), una arquitectura de aprendizaje profundo adaptativa que equilibra dinámicamente la precisión de estimación con los recursos computacionales [33]. ICENet se basa en el concepto de capas implícitas, donde la salida se define como el punto fijo de una ecuación:

$$
\mathbf{z}^* = \phi(\mathbf{z}^*; \mathbf{x}, \Theta)
$$

resuelto mediante iteraciones:

$$
\mathbf{z}^{(k+1)} = \phi(\mathbf{z}^{(k)}; \mathbf{x}, \Theta)
$$

hasta convergencia (cuando $\|\mathbf{z}^{(k+1)} - \mathbf{z}^{(k)}\| < \epsilon$).

La ventaja principal es que el número de iteraciones puede ajustarse dinámicamente según la calidad del canal y recursos disponibles, sin reentrenar la red [34]. El gradiente durante el entrenamiento se calcula mediante diferenciación implícita:

$$
\frac{\partial \mathbf{z}^*}{\partial \Theta} = -\left(I - \frac{\partial \phi}{\partial \mathbf{z}}\bigg|_{\mathbf{z}^*}\right)^{-1} \frac{\partial \phi}{\partial \Theta}\bigg|_{\mathbf{z}^*}
$$

ICENet ha demostrado mejoras de $2-4$ dB en MSE normalizado comparado con DNN tradicionales en escenarios V2X (vehicle-to-everything) de alta movilidad [33].

### D. Estimación de Canal Model-Driven vs. Data-Driven

La literatura distingue dos paradigmas principales [35]:

1. **Enfoques Data-Driven**: Aprenden directamente el mapeo $\mathbf{Y}_p \rightarrow \hat{\mathbf{H}}$ sin asumir estructura del canal. Ventajas: capturan complejidades no modeladas, robustos ante discrepancias de modelo. Desventajas: requieren grandes cantidades de datos de entrenamiento, pobre generalización fuera de la distribución de entrenamiento [36].

2. **Enfoques Model-Driven**: Integran conocimiento del dominio (e.g., estructura dispersa del canal en dominio angular) dentro de la arquitectura de red. Por ejemplo, redes de desenrollamiento (unfolded networks) que imitan iteraciones de algoritmos iterativos como ISTA (Iterative Shrinkage-Thresholding Algorithm) [37]:

$$
\begin{aligned}
\mathbf{h}^{(k+1)} &= \mathcal{S}_{\lambda_k}\left(\mathbf{h}^{(k)} - \mu_k \nabla_{\mathbf{h}} \|\mathbf{y} - \mathbf{A}\mathbf{h}^{(k)}\|^2\right) \\
&= \mathcal{S}_{\lambda_k}\left(\mathbf{h}^{(k)} + \mu_k \mathbf{A}^H(\mathbf{y} - \mathbf{A}\mathbf{h}^{(k)})\right)
\end{aligned}
$$

donde $\mathcal{S}_{\lambda}(\cdot)$ es el operador de umbralización suave (soft-thresholding), y los parámetros $\mu_k$, $\lambda_k$ se aprenden mediante backpropagation en lugar de fijarse manualmente [38].

Enfoques híbridos que combinan ambos paradigmas están emergiendo como la dirección más prometedora para 6G [39].

### E. Resultados de Desempeño

Comparaciones empíricas en datasets públicos (e.g., COST 2100, QuaDRiGa) muestran que [40]:

- **DNN** superan a estimadores MMSE en $3-5$ dB para SNR $< 10$ dB,
- **CNN** logran reducción adicional de $1-2$ dB explotando correlación en frecuencia,
- **LSTM** son superiores en escenarios de alta movilidad (velocidades $> 120$ km/h), con mejoras de hasta $6$ dB en MSE normalizado,
- **ICENet** ofrece el mejor compromiso precisión-complejidad, reduciendo FLOPs en $40\%$ con degradación de MSE $< 0.5$ dB [33].

---

## IV. BEAMFORMING Y MIMO MASIVO CON INTELIGENCIA ARTIFICIAL

### A. Fundamentos de Beamforming en Sistemas MIMO

El beamforming es una técnica de procesamiento de señales espaciales que dirige la energía de transmisión hacia usuarios específicos, maximizando la ganancia del arreglo de antenas y minimizando la interferencia [41]. En un sistema MIMO con precodificación lineal, la señal transmitida se expresa como:

$$
\mathbf{x} = \mathbf{F}\mathbf{s}
$$

donde $\mathbf{s} \in \mathbb{C}^{K}$ contiene los símbolos de datos para $K$ usuarios, y $\mathbf{F} \in \mathbb{C}^{N_t \times K}$ es la matriz de precodificación (beamforming). La señal recibida por el usuario $k$ es:

$$
y_k = \mathbf{h}_k^H \mathbf{f}_k s_k + \sum_{j \neq k} \mathbf{h}_k^H \mathbf{f}_j s_j + w_k
$$

donde $\mathbf{h}_k \in \mathbb{C}^{N_t}$ es el canal del usuario $k$, $\mathbf{f}_k$ es su vector de beamforming, el segundo término representa la interferencia multiusuario, y $w_k$ es el ruido.

### B. Problema de Optimización Clásico

El diseño óptimo de $\mathbf{F}$ típicamente busca maximizar la suma de tasas (sum-rate) o minimizar la interferencia, sujeto a restricciones de potencia [42]:

$$
\begin{aligned}
\max_{\mathbf{F}} \quad & \sum_{k=1}^{K} \log_2\left(1 + \frac{|\mathbf{h}_k^H \mathbf{f}_k|^2}{\sum_{j\neq k}|\mathbf{h}_k^H \mathbf{f}_j|^2 + \sigma^2}\right) \\
\text{s.t.} \quad & \|\mathbf{F}\|_F^2 \leq P_{\text{max}}
\end{aligned}
$$

Este problema es no-convexo y NP-duro en general. Soluciones subóptimas clásicas incluyen [43]:

- **Zero-Forcing (ZF)**: $\mathbf{F}_{ZF} = \mathbf{H}^H(\mathbf{H}\mathbf{H}^H)^{-1}$, elimina interferencia pero amplifica ruido.
- **MMSE**: $\mathbf{F}_{MMSE} = \mathbf{H}^H(\mathbf{H}\mathbf{H}^H + \sigma^2 I)^{-1}$, equilibra interferencia y ruido.
- **Regularized Zero-Forcing (RZF)**: $\mathbf{F}_{RZF} = \mathbf{H}^H(\mathbf{H}\mathbf{H}^H + \alpha I)^{-1}$, con $\alpha$ ajustado empíricamente.

Estas soluciones tienen limitaciones en MIMO masivo con información de estado de canal (CSI) imperfecta o variante en el tiempo [44].

### C. Beamforming Basado en Deep Learning

#### 1) Arquitecturas DNN para Diseño de Precodificadores

Las DNN pueden aprender directamente el mapeo óptimo de condiciones de canal a matrices de precodificación [45]. Una arquitectura típica recibe como entrada:

$$
\mathbf{z}_{in} = [\text{Re}(\text{vec}(\mathbf{H})); \text{Im}(\text{vec}(\mathbf{H}))] \in \mathbb{R}^{2KN_t}
$$

y produce vectores de beamforming a través de múltiples capas completamente conectadas:

$$
\mathbf{f}_k = \frac{1}{\sqrt{P_k}} \psi(\mathbf{W}_L \cdots \sigma(\mathbf{W}_1 \mathbf{z}_{in} + \mathbf{b}_1) \cdots + \mathbf{b}_L)
$$

donde $\psi(\cdot)$ es una función de normalización que asegura la restricción de potencia [46].

La función de pérdida comúnmente utilizada es la suma de tasas negativa:

$$
\mathcal{L}(\Theta) = -\frac{1}{B}\sum_{i=1}^{B} \sum_{k=1}^{K} \log_2\left(1 + \text{SINR}_k^{(i)}(\Theta)\right)
$$

donde $\text{SINR}_k$ es la relación señal-a-interferencia-más-ruido del usuario $k$.

#### 2) Redes Neuronales Gráficas (GNN) para MIMO Masivo

En sistemas MIMO masivos con cientos de antenas, las GNN explotan la estructura de grafo subyacente de las relaciones antena-usuario [47]. Cada nodo del grafo representa una antena o usuario, y las aristas capturan acoplamiento de canal. La actualización de características en una GNN se realiza mediante:

$$
\mathbf{h}_v^{(l+1)} = \sigma\left(\mathbf{W}^{(l)} \mathbf{h}_v^{(l)} + \sum_{u \in \mathcal{N}(v)} \mathbf{W}_{\text{msg}}^{(l)} \mathbf{h}_u^{(l)}\right)
$$

donde $\mathbf{h}_v^{(l)}$ son las características del nodo $v$ en la capa $l$, $\mathcal{N}(v)$ son los vecinos de $v$, y $\mathbf{W}^{(l)}$, $\mathbf{W}_{\text{msg}}^{(l)}$ son matrices de pesos [48].

Las GNN han demostrado escalabilidad superior, manteniendo rendimiento cercano al óptimo con complejidad $O(N_t)$ en lugar de $O(N_t^3)$ de métodos clásicos [49].

### D. Aprendizaje por Refuerzo para Beamforming Adaptativo

El beamforming en entornos dinámicos (movilidad, bloqueos intermitentes) se modela naturalmente como un proceso de decisión de Markov (MDP) [50]:

- **Estado** $s_t$: CSI actual, posiciones de usuarios, throughput histórico,
- **Acción** $a_t$: Configuración de beamforming $\mathbf{F}$,
- **Recompensa** $r_t$: Suma de tasas instantáneas o throughput ponderado por QoS,
- **Transición** $s_{t+1} \sim P(s_{t+1}|s_t, a_t)$: Evolución del canal.

El objetivo es aprender una política $\pi(a_t|s_t)$ que maximice la recompensa acumulada esperada:

$$
J(\pi) = \mathbb{E}_{\pi}\left[\sum_{t=0}^{\infty} \gamma^t r_t\right]
$$

donde $\gamma \in (0,1)$ es el factor de descuento [51].

#### 1) Deep Q-Networks (DQN)

DQN aproxima la función Q óptima usando una red neuronal $Q(s,a;\theta)$ entrenada minimizando la pérdida temporal-diferencia (TD) [52]:

$$
\mathcal{L}(\theta) = \mathbb{E}\left[\left(r + \gamma \max_{a'} Q(s', a'; \theta^-) - Q(s,a;\theta)\right)^2\right]
$$

donde $\theta^-$ son parámetros de una red objetivo (target network) actualizada periódicamente para estabilizar el entrenamiento.

#### 2) Optimización de Política Proximal (PPO)

PPO es un algoritmo de gradiente de política que actualiza $\theta$ mediante:

$$
\theta_{k+1} = \arg\max_{\theta} \mathbb{E}_{s,a \sim \pi_{\theta_k}}\left[\min\left(\frac{\pi_{\theta}(a|s)}{\pi_{\theta_k}(a|s)}A^{\pi_{\theta_k}}(s,a), \text{clip}\left(\frac{\pi_{\theta}(a|s)}{\pi_{\theta_k}(a|s)}, 1-\epsilon, 1+\epsilon\right)A^{\pi_{\theta_k}}(s,a)\right)\right]
$$

donde $A^{\pi}(s,a)$ es la función de ventaja (advantage), y $\epsilon$ es un hiperparámetro que limita cambios en la política [53]. PPO ha mostrado convergencia más estable que DQN en problemas de beamforming con espacios de acción continuos [54].

### E. Beamforming Consciente de Contexto con Transformers

Recientemente, arquitecturas de atención (attention mechanisms) y Transformers han sido aplicadas a beamforming multiusuario [55]. El mecanismo de atención multi-cabeza (multi-head attention) se define como:

$$
\text{Attention}(\mathbf{Q}, \mathbf{K}, \mathbf{V}) = \text{softmax}\left(\frac{\mathbf{Q}\mathbf{K}^T}{\sqrt{d_k}}\right)\mathbf{V}
$$

donde $\mathbf{Q}$, $\mathbf{K}$, $\mathbf{V}$ son matrices de consultas (queries), claves (keys), y valores (values) proyectadas desde las características de entrada, y $d_k$ es la dimensión de las claves [56].

En beamforming, $\mathbf{Q}$ puede representar usuarios, $\mathbf{K}$ antenas, y $\mathbf{V}$ características de canal, permitiendo que la red aprenda automáticamente qué antenas son más relevantes para cada usuario [57]. Transformers han logrado $10-15\%$ de mejora en sum-rate comparado con DNN convencionales en escenarios con $K > 50$ usuarios [58].

### F. Resultados Experimentales

Simulaciones en sistemas MIMO $128 \times 16$ (128 antenas de BS, 16 usuarios) muestran que [59]:

- **DNN-based beamforming** supera a RZF en $8-12\%$ en sum-rate promedio,
- **GNN** mantienen rendimiento con $60\%$ menos parámetros que DNN,
- **PPO** logra adaptación en línea (online) en $< 50$ ms con mejoras de $15-20\%$ en throughput bajo movilidad alta,
- **Transformer-based beamforming** demuestra la mejor generalización a números de usuarios no vistos durante entrenamiento.

---

## V. SUPERFICIES INTELIGENTES RECONFIGURABLES (RIS) Y OPTIMIZACIÓN CON IA

### A. Modelado de RIS en el Nivel Físico

Las superficies inteligentes reconfigurables (RIS) son arreglos planares de elementos pasivos que pueden ajustar la fase, amplitud, y polarización de ondas electromagnéticas incidentes, creando entornos de propagación programables [60]. Un RIS con $M$ elementos se modela mediante una matriz diagonal de coeficientes de reflexión [61]:

$$
\boldsymbol{\Phi} = \text{diag}(\beta_1 e^{j\theta_1}, \beta_2 e^{j\theta_2}, \ldots, \beta_M e^{j\theta_M})
$$

donde $\beta_m \in [0,1]$ es la amplitud de reflexión y $\theta_m \in [0, 2\pi)$ es el desplazamiento de fase del elemento $m$.

El canal efectivo en un sistema con RIS se compone de dos enlaces [62]:

$$
\mathbf{h}_{\text{eff}} = \mathbf{h}_d + \mathbf{H}_r \boldsymbol{\Phi} \mathbf{g}
$$

donde:
- $\mathbf{h}_d \in \mathbb{C}^{N_r}$ es el canal directo transmisor-receptor,
- $\mathbf{H}_r \in \mathbb{C}^{N_r \times M}$ es la matriz de canal RIS-receptor,
- $\mathbf{g} \in \mathbb{C}^{M}$ es el vector de canal transmisor-RIS.

### B. Problema de Optimización Conjunta

El diseño óptimo de RIS involucra optimizar conjuntamente los coeficientes de reflexión $\boldsymbol{\Phi}$ y el beamforming del transmisor $\mathbf{F}$ [63]:

$$
\begin{aligned}
\max_{\mathbf{F}, \boldsymbol{\Phi}} \quad & \sum_{k=1}^{K} \log_2\left(1 + \frac{|(\mathbf{h}_{d,k} + \mathbf{H}_{r,k}\boldsymbol{\Phi}\mathbf{g}_k)^H \mathbf{f}_k|^2}{\sum_{j\neq k}|(\mathbf{h}_{d,k} + \mathbf{H}_{r,k}\boldsymbol{\Phi}\mathbf{g}_k)^H \mathbf{f}_j|^2 + \sigma^2}\right) \\
\text{s.t.} \quad & \|\mathbf{F}\|_F^2 \leq P_{\text{max}}, \quad |\beta_m| \leq 1, \quad \theta_m \in [0, 2\pi), \; \forall m
\end{aligned}
$$

Este es un problema de optimización no-convexo altamente acoplado. Métodos clásicos como la optimización alternada (AO), sucesivas aproximaciones convexas (SCA), o el método de Riemannian manifold tienen alta complejidad computacional ($O(M^3 K^2)$) y requieren múltiples iteraciones ($10-100$), inviable para actualización en tiempo real [64], [65].

### C. Aprendizaje Profundo para Configuración de RIS

#### 1) Arquitecturas End-to-End

Una aproximación directa es entrenar una DNN que mapee CSI a configuraciones RIS óptimas [66]:

$$
\boldsymbol{\Phi}^* = \mathcal{N}_{\Theta}(\mathbf{h}_d, \mathbf{H}_r, \mathbf{g})
$$

La red $\mathcal{N}_{\Theta}$ puede ser una DNN multi-capa con capas de salida especializadas:

- **Capa de fase**: Aplica función tangente hiperbólica escalada para producir $\theta_m \in [0, 2\pi)$:

$$
\theta_m = \pi(\tanh(z_m^{\theta}) + 1)
$$

- **Capa de amplitud**: Aplica sigmoide para asegurar $\beta_m \in [0,1]$:

$$
\beta_m = \sigma(z_m^{\beta})
$$

donde $z_m^{\theta}$, $z_m^{\beta}$ son las salidas pre-activación [67].

#### 2) Aprendizaje por Refuerzo Multi-Agente

En escenarios con múltiples RIS distribuidos, cada RIS puede considerarse un agente autónomo. El marco de aprendizaje por refuerzo multi-agente (MARL) se formula como [68]:

- **Estado global** $s_t = (\mathbf{H}_1, \ldots, \mathbf{H}_N, \text{QoS})$,
- **Acción local** $a_t^{(i)} = \boldsymbol{\Phi}_i$ para el RIS $i$,
- **Recompensa compartida** $r_t = \sum_{k} R_k$ (sum-rate del sistema).

Multi-Agent Deep Deterministic Policy Gradient (MADDPG) es una extensión de DDPG que maneja entornos parcialmente observables [69]:

$$
\nabla_{\theta_i} J_i = \mathbb{E}\left[\nabla_{\theta_i} \log \pi_i(a_i|o_i; \theta_i) \cdot Q_i^{\pi}(\mathbf{s}, \mathbf{a})\right]
$$

donde $\pi_i$ es la política del agente $i$, $o_i$ es su observación local, y $Q_i^{\pi}$ es la función Q-value que considera las acciones de todos los agentes [70].

### D. Aprendizaje Federado para RIS

Cuando múltiples operadores o entornos despliegan RIS, compartir datos de entrenamiento puede violar la privacidad. El aprendizaje federado permite entrenar modelos colaborativamente sin compartir datos crudos [71]. El algoritmo FedAvg actualiza un modelo global mediante:

$$
\theta_{\text{global}}^{(t+1)} = \sum_{i=1}^{N} \frac{n_i}{n} \theta_i^{(t+1)}
$$

donde $\theta_i^{(t+1)}$ es el modelo entrenado localmente en el cliente $i$ con $n_i$ muestras, y $n = \sum_i n_i$ [72].

Para RIS, cada estación base con RIS local entrena su modelo de optimización y periódicamente sincroniza con el servidor central. Desafíos incluyen heterogeneidad de datos (non-IID) y comunicación limitada [73]. Variantes como FedProx y FedAvgM mejoran convergencia en estos escenarios [74].

### E. Optimización de Phase Shift Usando Redes de Desenrollamiento

Inspirado en algoritmos iterativos como alternating optimization, las redes de desenrollamiento (unfolding networks) mapean iteraciones de algoritmos en capas de red [75]. Por ejemplo, para optimización de RIS, cada iteración del algoritmo alternante:

$$
\begin{aligned}
\boldsymbol{\Phi}^{(k+1)} &= \arg\max_{\boldsymbol{\Phi}} f(\mathbf{F}^{(k)}, \boldsymbol{\Phi}) \\
\mathbf{F}^{(k+1)} &= \arg\max_{\mathbf{F}} f(\mathbf{F}, \boldsymbol{\Phi}^{(k+1)})
\end{aligned}
$$

se mapea en dos bloques de red con parámetros aprendibles $\{\mathbf{W}_k^{\Phi}, \mathbf{W}_k^{\mathbf{F}}\}$ [76]:

$$
\begin{aligned}
\boldsymbol{\Phi}^{(k+1)} &= g_{\mathbf{W}_k^{\Phi}}(\mathbf{F}^{(k)}, \boldsymbol{\Phi}^{(k)}, \mathbf{H}) \\
\mathbf{F}^{(k+1)} &= g_{\mathbf{W}_k^{\mathbf{F}}}(\mathbf{F}^{(k)}, \boldsymbol{\Phi}^{(k+1)}, \mathbf{H})
\end{aligned}
$$

Esta arquitectura garantiza interpretabilidad (cada capa corresponde a una iteración del algoritmo) y aprovecha conocimiento del dominio [77].

### F. Desempeño y Resultados

Experimentos en sistemas con $M = 64$-$256$ elementos RIS muestran [78], [79]:

- **DNN-based RIS** logran $90-95\%$ del rendimiento de métodos iterativos con $100\times$ reducción en tiempo de cómputo,
- **MADDPG** converge en $500-1000$ episodios y supera métodos distribuidos baseline en $20-30\%$ en throughput,
- **Federated learning para RIS** alcanza precisión comparable a entrenamiento centralizado después de $50-100$ rondas con $10\times$ menos comunicación,
- **Unfolding networks** requieren $3-5$ capas (equivalente a $3-5$ iteraciones) para igualar algoritmos con $20-30$ iteraciones.

---

## VI. COMUNICACIONES SEMÁNTICAS Y CONSCIENTES DE INTENCIÓN

### A. Del Paradigma Sintáctico al Semántico

El modelo clásico de comunicaciones de Shannon se centra en la transmisión fiel de bits sin considerar el significado (semántica) o propósito (intención) de la información [80]. En 6G, se propone un cambio fundamental hacia comunicaciones semánticas, donde solo se transmite información relevante para la tarea del usuario final [81], [82].

Formalmente, sea $X$ la fuente de información, $Y$ la señal recibida, y $Z$ la tarea o decisión final. El objetivo tradicional maximiza la información mutua $I(X;Y)$, mientras que comunicaciones semánticas maximizan $I(Z;Y)$ o minimizan la distorsión de la tarea $\mathbb{E}[d(Z, \hat{Z})]$ [83].

### B. Codificación Semántica con Autoencoders

Los autoencoders neuronales ofrecen un marco natural para codificación semántica [84]. Un autoencoder consta de:

- **Encoder semántico** $\mathcal{E}_{\theta}$: Extrae características relevantes (representación semántica) de los datos de entrada:

$$
\mathbf{c} = \mathcal{E}_{\theta}(X)
$$

donde $\mathbf{c} \in \mathbb{R}^{d_c}$ con $d_c \ll \text{dim}(X)$.

- **Canal físico**: Transmite $\mathbf{c}$ (potencialmente corrompido por ruido):

$$
\tilde{\mathbf{c}} = \mathbf{c} + \mathbf{n}, \quad \mathbf{n} \sim \mathcal{N}(0, \sigma^2 I)
$$

- **Decoder semántico** $\mathcal{D}_{\phi}$: Reconstruye la información relevante para la tarea:

$$
\hat{Z} = \mathcal{D}_{\phi}(\tilde{\mathbf{c}})
$$

El sistema se entrena end-to-end minimizando una pérdida orientada a la tarea [85]:

$$
\mathcal{L}(\theta, \phi) = \mathbb{E}[d(Z, \mathcal{D}_{\phi}(\mathcal{E}_{\theta}(X) + \mathbf{n}))]
$$

Por ejemplo, para reconocimiento de imágenes sobre canal inalámbrico:

$$
\mathcal{L}(\theta, \phi) = -\mathbb{E}[\log p(y_{\text{true}}|\mathcal{D}_{\phi}(\mathcal{E}_{\theta}(I) + \mathbf{n}))]
$$

donde $I$ es una imagen y $y_{\text{true}}$ su etiqueta [86].

### C. Extracción de Conocimiento y Bases de Conocimiento

Para comunicaciones conscientes de contexto, se requieren bases de conocimiento (knowledge bases, KB) que almacenen información sobre el entorno, usuarios, y aplicaciones [87]. Una KB puede modelarse como un grafo de conocimiento $\mathcal{G} = (\mathcal{V}, \mathcal{E}, \mathcal{R})$ donde:

- $\mathcal{V}$ son entidades (usuarios, dispositivos, ubicaciones),
- $\mathcal{E}$ son relaciones (ubicación_de, comunica_con, requiere_QoS),
- $\mathcal{R}$ son tipos de relaciones.

Embeddings de grafos de conocimiento se aprenden mediante modelos como TransE [88]:

$$
\mathbf{h} + \mathbf{r} \approx \mathbf{t}
$$

para un triple $(h, r, t)$ (head, relation, tail), optimizando:

$$
\mathcal{L} = \sum_{(h,r,t) \in \mathcal{G}} \sum_{(h',r,t') \in \mathcal{G}'} \max(0, \gamma + d(\mathbf{h}+\mathbf{r}, \mathbf{t}) - d(\mathbf{h}'+\mathbf{r}, \mathbf{t}'))
$$

donde $\mathcal{G}'$ son triples negativos corruptos, $d$ es una distancia (Euclidiana o L1), y $\gamma$ es un margen [89].

### D. Comunicaciones Orientadas a Intenciones (Goal-Oriented Communications)

El nivel más alto de abstracción semántica son las comunicaciones orientadas a intenciones, donde los usuarios especifican objetivos de alto nivel (e.g., "transmitir video con calidad perceptual excelente") y la red adapta automáticamente recursos [90]. Esto requiere:

1. **Traducción intención-a-requisitos**: Mapear intenciones vagas a métricas cuantificables usando NLP y técnicas de razonamiento [91].

2. **Orquestación de recursos**: Asignar recursos (espectro, potencia, RIS, edge computing) para cumplir la intención, modelado como:

$$
\min_{\mathbf{r} \in \mathcal{R}} \text{Cost}(\mathbf{r}) \quad \text{s.t.} \quad \text{Intent}(\mathbf{r}) \geq \tau
$$

donde $\mathbf{r}$ son recursos, $\text{Cost}$ puede ser energía o latencia, y $\text{Intent}$ mide satisfacción de la intención [92].

3. **Aprendizaje de políticas**: RL para aprender mapeos intención $\rightarrow$ configuración de red, utilizando recompensas basadas en satisfacción del usuario [93].

### E. Joint Source-Channel Coding (JSCC) con Deep Learning

En comunicaciones semánticas, la separación tradicional entre codificación de fuente y canal (source-channel separation) es subóptima [94]. Deep JSCC aprende codificación conjunta end-to-end:

$$
\hat{X} = \text{Decoder}_{\phi}(\mathbf{h} \ast \text{Encoder}_{\theta}(X) + \mathbf{n})
$$

donde el encoder aprende simultáneamente compresión y codificación de canal, y el decoder aprende decodificación y reconstrucción [95].

Para imágenes, arquitecturas basadas en CNN y attention han demostrado superar esquemas separados (JPEG + codificación de canal) en términos de PSNR y SSIM bajo restricciones de ancho de banda [96]:

$$
\text{PSNR}_{\text{DeepJSCC}} - \text{PSNR}_{\text{JPEG+BPG}} \approx 2-5 \text{ dB}
$$

para SNR $< 10$ dB.

### F. Modelos de Lenguaje Grandes (LLMs) para Gestión Semántica

Recientemente, LLMs como GPT-4 y sus variantes especializadas se proponen para gestión inteligente de comunicaciones semánticas [97]:

- **Interpretación de intenciones**: Usar LLMs para traducir comandos en lenguaje natural a políticas de red ejecutables.

- **Generación de código**: LLMs pueden generar configuraciones de red o scripts de optimización dinámicamente basándose en descripciones de intenciones [98].

- **Razonamiento multimodal**: Integrar información de texto, imágenes, y métricas de red para decisiones holísticas [99].

Un desafío clave es la latencia de inferencia de LLMs ($100-500$ ms para modelos grandes), que requiere técnicas de destilación de modelos o aceleración hardware [100].

---

## VII. DESAFÍOS ABIERTOS Y DIRECCIONES FUTURAS DE INVESTIGACIÓN

### A. Generalización y Robustez Fuera de Distribución

Los modelos de aprendizaje profundo entrenados en condiciones específicas frecuentemente degradan su rendimiento ante distribuciones de datos no vistas (out-of-distribution, OOD) [101]. En el nivel físico de 6G, esto se manifiesta como:

- **Variación de entornos**: Un modelo entrenado en escenarios urbanos puede fallar en rurales o interiores.
- **Cambios de hardware**: Diferencias en calibración de antenas, respuesta de amplificadores, etc.

Direcciones de investigación incluyen:

1. **Domain adaptation**: Técnicas como discrepancia de distribución adversarial para adaptar modelos a nuevos dominios con pocos datos [102]:

$$
\min_{\theta} \mathcal{L}_{\text{task}}(\theta; \mathcal{D}_{\text{target}}) + \lambda \text{disc}(f_{\theta}(\mathcal{D}_{\text{source}}), f_{\theta}(\mathcal{D}_{\text{target}}))
$$

2. **Meta-learning**: Entrenar modelos que puedan adaptarse rápidamente a nuevas tareas con pocos ejemplos (few-shot learning) [103]:

$$
\theta^* = \arg\min_{\theta} \mathbb{E}_{\mathcal{T} \sim p(\mathcal{T})}\left[\mathcal{L}_{\mathcal{T}}(\theta - \alpha \nabla_{\theta}\mathcal{L}_{\mathcal{T}}(\theta))\right]
$$

(algoritmo MAML - Model-Agnostic Meta-Learning).

3. **Robustness certificada**: Técnicas de verificación formal para garantizar rendimiento mínimo en intervalos de variación de parámetros [104].

### B. Complejidad Computacional y Eficiencia Energética

La inferencia de DNN profundas en dispositivos de borde con recursos limitados es un cuello de botella crítico [105]. Soluciones emergentes:

1. **Quantización**: Reducir precisión de pesos y activaciones de 32-bit float a 8-bit o menor [106]:

$$
\mathbf{W}_{\text{quant}} = \text{round}\left(\frac{\mathbf{W} - \min(\mathbf{W})}{\Delta}\right) \cdot \Delta + \min(\mathbf{W})
$$

donde $\Delta = \frac{\max(\mathbf{W}) - \min(\mathbf{W})}{2^b - 1}$ para $b$ bits.

2. **Pruning (poda)**: Eliminar conexiones o neuronas con pesos pequeños, reduciendo FLOPs y memoria [107]:

$$
\mathbf{W}_{\text{pruned}} = \mathbf{W} \odot \mathbf{M}, \quad \mathbf{M}_{ij} = \begin{cases} 1 & |\mathbf{W}_{ij}| > \tau \\ 0 & \text{caso contrario} \end{cases}
$$

3. **Neural Architecture Search (NAS)**: Búsqueda automatizada de arquitecturas óptimas bajo restricciones de latencia/energía [108].

4. **Splitting de inferencia**: Dividir modelos entre dispositivo y servidor de borde, transmitiendo representaciones intermedias [109].

### C. Privacidad y Seguridad de Modelos de IA

La integración de IA en el nivel físico introduce vectores de ataque novedosos [110]:

1. **Ataques adversariales**: Perturbaciones imperceptibles al CSI que causan decisiones erróneas de beamforming [111]:

$$
\tilde{\mathbf{H}} = \mathbf{H} + \epsilon \cdot \text{sign}(\nabla_{\mathbf{H}} \mathcal{L}(\mathbf{H}; \theta))
$$

(Fast Gradient Sign Method).

2. **Model inversion**: Recuperar información privada (ubicación de usuarios, patrones de tráfico) de salidas del modelo [112].

3. **Envenenamiento de datos (poisoning)**: Inyectar muestras maliciosas en datos de entrenamiento para degradar rendimiento [113].

Contramedidas incluyen:

- **Adversarial training**: Entrenar con ejemplos adversariales [114]:

$$
\min_{\theta} \mathbb{E}_{(\mathbf{x},y)}\left[\max_{\|\delta\| \leq \epsilon} \mathcal{L}(\mathbf{x}+\delta, y; \theta)\right]
$$

- **Differential privacy**: Agregar ruido calibrado durante entrenamiento para limitar información que puede extraerse [115]:

$$
\tilde{\nabla} = \nabla_{\theta}\mathcal{L}(\theta) + \mathcal{N}(0, \sigma^2 C^2 I)
$$

donde $C$ es un clipping threshold y $\sigma$ se ajusta para satisfacer $(\epsilon, \delta)$-differential privacy.

- **Federated learning seguro**: Agregación segura multi-partido y verificación de contribuciones de clientes [116].

### D. Interpretabilidad y Explicabilidad (XAI)

Los operadores de red requieren comprensión de decisiones de modelos de IA para depuración, cumplimiento regulatorio, y confianza [117]. Técnicas de XAI para nivel físico incluyen:

1. **Attention visualization**: Mapas de atención muestran qué partes del CSI influyen más en decisiones de beamforming [118].

2. **SHAP (SHapley Additive exPlanations)**: Atribuye contribuciones de características usando valores de Shapley de teoría de juegos [119]:

$$
\phi_i = \sum_{S \subseteq \mathcal{F} \setminus \{i\}} \frac{|S|!(|\mathcal{F}|-|S|-1)!}{|\mathcal{F}|!}\left[f_{S \cup \{i\}}(\mathbf{x}_{S \cup \{i\}}) - f_S(\mathbf{x}_S)\right]
$$

3. **Concept activation vectors (CAVs)**: Identificar conceptos de alto nivel aprendidos por la red [120].

### E. Co-diseño Hardware-Software

Para despliegue práctico de IA nativa en el nivel físico, se requiere co-diseño de hardware acelerador (GPUs, TPUs, NPUs) y algoritmos [121]:

- **Processing-in-memory (PIM)**: Realizar operaciones de NN directamente en memoria para reducir movimiento de datos [122].

- **Analog computing**: Implementar operaciones matriciales mediante circuitos analógicos (e.g., crossbar arrays) para multiplicación extremadamente eficiente [123].

- **Photonic neural networks**: Usar señales ópticas para computación ultrarrápida y eficiente en energía [124].

### F. Estandarización e Interoperabilidad

La falta de estándares para IA en 6G es una barrera para despliegue a gran escala. Esfuerzos de estandarización incluyen:

- **3GPP Release 18/19**: Trabajo en especificaciones de AI/ML para NR (New Radio) incluyendo interfaces para entrenamiento y predicción de modelos [125].

- **ITU-T Focus Group ML5G**: Desarrollo de requisitos arquitectónicos y de interoperabilidad para IA en 5G/6G [126].

- **O-RAN Alliance**: Definición de interfaces abiertas para controladores de IA (RIC - RAN Intelligent Controller) [127].

Desafíos incluyen equilibrar flexibilidad para innovación con interoperabilidad entre vendors.

---

## VIII. CONCLUSIONES

Este artículo ha presentado una revisión exhaustiva del estado del arte en inteligencia artificial nativa aplicada al nivel físico de redes 6G. Se ha demostrado que la integración profunda de técnicas de aprendizaje profundo, aprendizaje por refuerzo, y aprendizaje federado en funciones críticas de la capa física—estimación de canal, beamforming, optimización de MIMO masivo, control de superficies inteligentes reconfigurables, y comunicaciones semánticas—ofrece mejoras sustanciales en rendimiento, adaptabilidad, y eficiencia energética comparado con enfoques clásicos basados en modelos analíticos.

Arquitecturas avanzadas como redes neuronales convolucionales, redes recurrentes LSTM, redes neuronales gráficas, y Transformers han sido exitosamente aplicadas a problemas de alta dimensionalidad y complejidad en el nivel físico. Métodos híbridos model-driven/data-driven, como redes de desenrollamiento (unfolding networks) y capas implícitas, combinan lo mejor de ambos mundos: aprovechan conocimiento del dominio para mejorar interpretabilidad y generalización, mientras mantienen la flexibilidad y capacidad de aprendizaje de las redes neuronales.

El cambio de paradigma hacia comunicaciones semánticas y orientadas a intenciones representa una evolución fundamental en la filosofía de diseño de sistemas de comunicación, donde la red no solo transmite bits, sino que comprende el significado y propósito de la información, optimizando recursos para métricas de calidad de experiencia (QoE) en lugar de métricas puramente técnicas.

Sin embargo, numerosos desafíos técnicos y de implementación permanecen abiertos: generalización robusta fuera de distribución, eficiencia computacional en dispositivos de borde, seguridad contra ataques adversariales, privacidad de datos, interpretabilidad de modelos, co-diseño hardware-software, y estandarización. Abordar estos desafíos requerirá esfuerzos interdisciplinarios que integren teoría de comunicaciones, aprendizaje automático, optimización, seguridad, y diseño de hardware.

A medida que la investigación avanza hacia la realización práctica de redes 6G, la IA nativa en el nivel físico no es simplemente una mejora incremental, sino un cambio fundamental hacia sistemas de comunicación autónomos, adaptativos, y conscientes de contexto que formarán la base de la sociedad hiperconectada del futuro.

---

## REFERENCIAS

[1] M. Z. Chowdhury, M. Shahjalal, S. Ahmed, and Y. M. Jang, "6G wireless communication systems: Applications, requirements, technologies, challenges, and research directions," *IEEE Open Journal of the Communications Society*, vol. 1, pp. 957-975, 2020.

[2] W. Saad, M. Bennis, and M. Chen, "A vision of 6G wireless systems: Applications, trends, technologies, and open research problems," *IEEE Network*, vol. 34, no. 3, pp. 134-142, May/June 2020.

[3] Y. Liu et al., "Vision, requirements and network architecture of 6G mobile network beyond 2030," *China Communications*, vol. 17, no. 9, pp. 92-104, Sept. 2020.

[4] C. de Almeida et al., "A comprehensive review of AI-native 6G: Integrating semantic communications, reconfigurable intelligent surfaces, and edge intelligence for next-generation connectivity," *Frontiers in Communications and Networks*, vol. 6, 2025.

[5] M. Latva-aho and K. Leppänen (Eds.), *Key Drivers and Research Challenges for 6G Ubiquitous Wireless Intelligence*, 6G Flagship, University of Oulu, 2019.

[6] H. Viswanathan and P. E. Mogensen, "Communications in the 6G era," *IEEE Access*, vol. 8, pp. 57063-57074, 2020.

[7] K. B. Letaief, W. Chen, Y. Shi, J. Zhang, and Y.-J. A. Zhang, "The roadmap to 6G: AI empowered wireless networks," *IEEE Communications Magazine*, vol. 57, no. 8, pp. 84-90, Aug. 2019.

[8] T. O'Shea and J. Hoydis, "An introduction to deep learning for the physical layer," *IEEE Transactions on Cognitive Communications and Networking*, vol. 3, no. 4, pp. 563-575, Dec. 2017.

[9] C.-K. Wen, W.-T. Shih, and S. Jin, "Deep learning for massive MIMO CSI feedback," *IEEE Wireless Communications Letters*, vol. 7, no. 5, pp. 748-751, Oct. 2018.

[10] H. Ye, G. Y. Li, and B.-H. Juang, "Power of deep learning for channel estimation and signal detection in OFDM systems," *IEEE Wireless Communications Letters*, vol. 7, no. 1, pp. 114-117, Feb. 2018.

[11] H. B. McMahan, E. Moore, D. Ramage, S. Hampson, and B. A. y Arcas, "Communication-efficient learning of deep networks from decentralized data," in *Proc. AISTATS*, Fort Lauderdale, FL, USA, Apr. 2017.

[12] W. Y. B. Lim et al., "Federated learning in mobile edge networks: A comprehensive survey," *IEEE Communications Surveys & Tutorials*, vol. 22, no. 3, pp. 2031-2063, 3rd Quart. 2020.

[13] A. Goldsmith, *Wireless Communications*. Cambridge, UK: Cambridge University Press, 2005.

[14] E. G. Larsson, O. Edfors, F. Tufvesson, and T. L. Marzetta, "Massive MIMO for next generation wireless systems," *IEEE Communications Magazine*, vol. 52, no. 2, pp. 186-195, Feb. 2014.

[15] A. F. Molisch, *Wireless Communications*, 2nd ed. Chichester, UK: Wiley-IEEE Press, 2011.

[16] H. L. Van Trees, *Optimum Array Processing: Part IV of Detection, Estimation, and Modulation Theory*. New York, NY, USA: Wiley, 2002.

[17] P. Wang, J. Zhang, X. Zhang, Z. Yan, B. G. Evans, and W. Wang, "Convergence of satellite and terrestrial networks: A comprehensive survey," *IEEE Access*, vol. 8, pp. 5550-5588, 2020.

[18] N. Samuel, T. Diskin, and A. Wiesel, "Deep MIMO detection," in *Proc. IEEE 18th Int. Workshop Signal Process. Advances Wireless Commun. (SPAWC)*, Sapporo, Japan, July 2017, pp. 1-5.

[19] T. J. O'Shea, T. Roy, and T. C. Clancy, "Over-the-air deep learning based radio signal classification," *IEEE Journal of Selected Topics in Signal Processing*, vol. 12, no. 1, pp. 168-179, Feb. 2018.

[20] E. Bjornson, J. Hoydis, and L. Sanguinetti, "Massive MIMO networks: Spectral, energy, and hardware efficiency," *Foundations and Trends in Signal Processing*, vol. 11, nos. 3-4, pp. 154-655, 2017.

[21] S. M. Kay, *Fundamentals of Statistical Signal Processing: Estimation Theory*. Upper Saddle River, NJ, USA: Prentice-Hall, 1993.

[22] M. Biguesh and A. B. Gershman, "Training-based MIMO channel estimation: A study of estimator tradeoffs and optimal training signals," *IEEE Transactions on Signal Processing*, vol. 54, no. 3, pp. 884-893, Mar. 2006.

[23] H. He, C.-K. Wen, S. Jin, and G. Y. Li, "Deep learning-based channel estimation for beamspace mmWave massive MIMO systems," *IEEE Wireless Communications Letters*, vol. 7, no. 5, pp. 852-855, Oct. 2018.

[24] P. Dong, H. Zhang, G. Y. Li, I. S. Gaspar, and N. NaderiAlizadeh, "Deep CNN-based channel estimation for mmWave massive MIMO systems," *IEEE Journal of Selected Topics in Signal Processing*, vol. 13, no. 5, pp. 989-1000, Sept. 2019.

[25] A. F. Agarap, "Deep learning using rectified linear units (ReLU)," arXiv preprint arXiv:1803.08375, 2018.

[26] C. Wen, W. Shih, and S. Jin, "Deep learning for massive MIMO CSI feedback," *IEEE Wireless Communications Letters*, vol. 7, no. 5, pp. 748-751, Oct. 2018.

[27] M. Soltani, V. Pourahmadi, A. Mirzaei, and H. Sheikhzadeh, "Deep learning-based channel estimation," *IEEE Communications Letters*, vol. 23, no. 4, pp. 652-655, Apr. 2019.

[28] X. Gao, S. Jin, C.-K. Wen, and G. Y. Li, "ComNet: Combination of deep learning and expert knowledge in OFDM receivers," *IEEE Communications Letters*, vol. 22, no. 12, pp. 2627-2630, Dec. 2018.

[29] Y. LeCun, Y. Bengio, and G. Hinton, "Deep learning," *Nature*, vol. 521, no. 7553, pp. 436-444, May 2015.

[30] Y. Yang, F. Gao, X. Ma, and S. Zhang, "Deep learning-based channel estimation for doubly selective fading channels," *IEEE Access*, vol. 7, pp. 36579-36589, 2019.

[31] Z. Qin, H. Ye, G. Y. Li, and B.-H. F. Juang, "Deep learning in physical layer communications," *IEEE Wireless Communications*, vol. 26, no. 2, pp. 93-99, Apr. 2019.

[32] S. Hochreiter and J. Schmidhuber, "Long short-term memory," *Neural Computation*, vol. 9, no. 8, pp. 1735-1780, Nov. 1997.

[33] A. Li et al., "Adaptive implicit-based deep learning channel estimation for 6G communications," *IEEE Communications Magazine*, 2025.

[34] S. Bai, J. Z. Kolter, and V. Koltun, "Deep equilibrium models," in *Proc. Advances Neural Inf. Process. Syst. (NeurIPS)*, Vancouver, BC, Canada, Dec. 2019.

[35] H. Huang, W. Xia, J. Xiong, J. Yang, G. Zheng, and X. Zhu, "Unsupervised learning-based fast beamforming design for downlink MIMO," *IEEE Access*, vol. 7, pp. 7599-7605, 2019.

[36] A. Caelles, J. F. Monserrat, and D. Martín-Sacristán, "Deep learning for channel estimation: A methodological overview," *Electronics*, vol. 12, no. 24, p. 4965, 2023.

[37] J. Zhang and B. Ghanem, "ISTA-Net: Interpretable optimization-inspired deep network for image compressive sensing," in *Proc. IEEE Conf. Comput. Vision Pattern Recognit. (CVPR)*, Salt Lake City, UT, USA, June 2018, pp. 1828-1837.

[38] V. Monga, Y. Li, and Y. C. Eldar, "Algorithm unrolling: Interpretable, efficient deep learning for signal and image processing," *IEEE Signal Processing Magazine*, vol. 38, no. 2, pp. 18-44, Mar. 2021.

[39] K. Ntougias et al., "An overview on machine learning methods for partial discharge localization in medium voltage cables," arXiv preprint arXiv:2412.14538, Dec. 2024.

[40] M. Arnold, S. Dörner, S. Cammerer, and S. ten Brink, "On deep learning-based channel decoding," in *Proc. 51st Annu. Conf. Inf. Sci. Syst. (CISS)*, Baltimore, MD, USA, Mar. 2017, pp. 1-6.

[41] J. Capon, "High-resolution frequency-wavenumber spectrum analysis," *Proc. IEEE*, vol. 57, no. 8, pp. 1408-1418, Aug. 1969.

[42] Q. Shi, M. Razaviyayn, Z.-Q. Luo, and C. He, "An iteratively weighted MMSE approach to distributed sum-utility maximization for a MIMO interfering broadcast channel," *IEEE Transactions on Signal Processing*, vol. 59, no. 9, pp. 4331-4340, Sept. 2011.

[43] C. B. Peel, B. M. Hochwald, and A. L. Swindlehurst, "A vector-perturbation technique for near-capacity multiantenna multiuser communication—Part I: Channel inversion and regularization," *IEEE Transactions on Communications*, vol. 53, no. 1, pp. 195-202, Jan. 2005.

[44] H. Q. Ngo, E. G. Larsson, and T. L. Marzetta, "Energy and spectral efficiency of very large multiuser MIMO systems," *IEEE Transactions on Communications*, vol. 61, no. 4, pp. 1436-1449, Apr. 2013.

[45] F. Liang, C. Shen, W. Yu, and F. Wu, "Towards optimal power control via ensembling deep neural networks," *IEEE Transactions on Communications*, vol. 68, no. 3, pp. 1760-1776, Mar. 2020.

[46] W. Lee, M. Kim, and D.-H. Cho, "Deep power control: Transmit power control scheme based on convolutional neural network," *IEEE Communications Letters*, vol. 22, no. 6, pp. 1276-1279, June 2018.

[47] Y. Shen, Y. Shi, J. Zhang, and K. B. Letaief, "Graph neural networks for scalable radio resource management: Architecture design and theoretical analysis," *IEEE Journal on Selected Areas in Communications*, vol. 39, no. 1, pp. 101-115, Jan. 2021.

[48] T. N. Kipf and M. Welling, "Semi-supervised classification with graph convolutional networks," in *Proc. Int. Conf. Learn. Represent. (ICLR)*, Toulon, France, Apr. 2017.

[49] Z. Wang, L. Zhao, and Y. Gong, "Graph neural networks for distributed power allocation in wireless networks: Aggregation over-the-air," in *Proc. IEEE Int. Conf. Acoust., Speech Signal Process. (ICASSP)*, Toronto, ON, Canada, June 2021, pp. 4905-4909.

[50] N. Zhao, Y.-C. Liang, D. Niyato, Y. Pei, M. Wu, and Y. Jiang, "Deep reinforcement learning for user association and resource allocation in heterogeneous cellular networks," *IEEE Transactions on Wireless Communications*, vol. 18, no. 11, pp. 5141-5152, Nov. 2019.

[51] R. S. Sutton and A. G. Barto, *Reinforcement Learning: An Introduction*, 2nd ed. Cambridge, MA, USA: MIT Press, 2018.

[52] V. Mnih et al., "Human-level control through deep reinforcement learning," *Nature*, vol. 518, no. 7540, pp. 529-533, Feb. 2015.

[53] J. Schulman, F. Wolski, P. Dhariwal, A. Radford, and O. Klimov, "Proximal policy optimization algorithms," arXiv preprint arXiv:1707.06347, July 2017.

[54] J. Cui, Y. Liu, and A. Nallanathan, "Multi-agent reinforcement learning-based resource allocation for UAV networks," *IEEE Transactions on Wireless Communications*, vol. 19, no. 2, pp. 729-743, Feb. 2020.

[55] K. He, X. Chen, S. Wu, Z. Zhang, and D. Zhao, "Transformer-empowered 6G intelligent networks: From massive MIMO processing to semantic communication," *IEEE Wireless Communications*, vol. 30, no. 1, pp. 136-143, Feb. 2023.

[56] A. Vaswani et al., "Attention is all you need," in *Proc. Advances Neural Inf. Process. Syst. (NeurIPS)*, Long Beach, CA, USA, Dec. 2017.

[57] S. Park, O. Simeone, and J. Kang, "Meta-learning to communicate: Fast end-to-end training for fading channels," in *Proc. IEEE Int. Conf. Acoust., Speech Signal Process. (ICASSP)*, Brighton, UK, May 2019, pp. 4525-4529.

[58] Y. Wang, M. Liu, J. Yang, and G. Gui, "Transformer-based deep learning for wireless physical layer design: Opportunities and challenges," *IEEE Communications Surveys & Tutorials*, early access, 2024.

[59] H. Huang, Y. Song, J. Yang, G. Gui, and F. Adachi, "Deep-learning-based millimeter-wave massive MIMO for hybrid precoding," *IEEE Transactions on Vehicular Technology*, vol. 68, no. 3, pp. 3027-3032, Mar. 2019.

[60] Q. Wu and R. Zhang, "Intelligent reflecting surface enhanced wireless network via joint active and passive beamforming," *IEEE Transactions on Wireless Communications*, vol. 18, no. 11, pp. 5394-5409, Nov. 2019.

[61] E. Basar, M. Di Renzo, J. De Rosny, M. Debbah, M.-S. Alouini, and R. Zhang, "Wireless communications through reconfigurable intelligent surfaces," *IEEE Access*, vol. 7, pp. 116753-116773, 2019.

[62] C. Huang, A. Zappone, G. C. Alexandropoulos, M. Debbah, and C. Yuen, "Reconfigurable intelligent surfaces for energy efficiency in wireless communication," *IEEE Transactions on Wireless Communications*, vol. 18, no. 8, pp. 4157-4170, Aug. 2019.

[63] Q. Wu and R. Zhang, "Towards smart and reconfigurable environment: Intelligent reflecting surface aided wireless network," *IEEE Communications Magazine*, vol. 58, no. 1, pp. 106-112, Jan. 2020.

[64] Y. Han, W. Tang, S. Jin, C.-K. Wen, and X. Ma, "Large intelligent surface-assisted wireless communication exploiting statistical CSI," *IEEE Transactions on Vehicular Technology*, vol. 68, no. 8, pp. 8238-8242, Aug. 2019.

[65] B. Di, H. Zhang, L. Song, Y. Li, Z. Han, and H. V. Poor, "Hybrid beamforming for reconfigurable intelligent surface based multi-user communications: Achievable rates with limited discrete phase shifts," *IEEE Journal on Selected Areas in Communications*, vol. 38, no. 8, pp. 1809-1822, Aug. 2020.

[66] A. Taha, M. Alrabeiah, and A. Alkhateeb, "Deep learning for large intelligent surfaces in millimeter wave and massive MIMO systems," in *Proc. IEEE Global Commun. Conf. (GLOBECOM)*, Waikoloa, HI, USA, Dec. 2019, pp. 1-6.

[67] C. Huang et al., "Holographic MIMO surfaces for 6G wireless networks: Opportunities, challenges, and trends," *IEEE Wireless Communications*, vol. 27, no. 5, pp. 118-125, Oct. 2020.

[68] R. Lowe, Y. Wu, A. Tamar, J. Harb, P. Abbeel, and I. Mordatch, "Multi-agent actor-critic for mixed cooperative-competitive environments," in *Proc. Advances Neural Inf. Process. Syst. (NeurIPS)*, Long Beach, CA, USA, Dec. 2017.

[69] J. Foerster, G. Farquhar, T. Afouras, N. Nardelli, and S. Whiteson, "Counterfactual multi-agent policy gradients," in *Proc. 32nd AAAI Conf. Artif. Intell.*, New Orleans, LA, USA, Feb. 2018.

[70] L. Buşoniu, R. Babuška, and B. De Schutter, "Multi-agent reinforcement learning: An overview," in *Innovations in Multi-Agent Systems and Applications*, D. Srinivasan and L. C. Jain, Eds. Berlin, Germany: Springer, 2010, pp. 183-221.

[71] J. Konečný, H. B. McMahan, F. X. Yu, P. Richtárik, A. T. Suresh, and D. Bacon, "Federated learning: Strategies for improving communication efficiency," arXiv preprint arXiv:1610.05492, Oct. 2016.

[72] B. McMahan, E. Moore, D. Ramage, S. Hampson, and B. A. y Arcas, "Communication-efficient learning of deep networks from decentralized data," in *Proc. 20th Int. Conf. Artif. Intell. Statist. (AISTATS)*, Fort Lauderdale, FL, USA, Apr. 2017.

[73] T. Li, A. K. Sahu, A. Talwalkar, and V. Smith, "Federated learning: Challenges, methods, and future directions," *IEEE Signal Processing Magazine*, vol. 37, no. 3, pp. 50-60, May 2020.

[74] T. Li, A. K. Sahu, M. Zaheer, M. Sanjabi, A. Talwalkar, and V. Smith, "Federated optimization in heterogeneous networks," in *Proc. Machine Learn. Syst. (MLSys)*, Austin, TX, USA, Mar. 2020.

[75] J. R. Hershey, J. Le Roux, and F. Weninger, "Deep unfolding: Model-based inspiration of novel deep architectures," arXiv preprint arXiv:1409.2574, Sept. 2014.

[76] W. Shi, J. Caballero, F. Huszár, J. Totz, A. P. Aitken, R. Bishop, D. Rueckert, and Z. Wang, "Real-time single image and video super-resolution using an efficient sub-pixel convolutional neural network," in *Proc. IEEE Conf. Comput. Vision Pattern Recognit. (CVPR)*, Las Vegas, NV, USA, June 2016, pp. 1874-1883.

[77] K. Gregor and Y. LeCun, "Learning fast approximations of sparse coding," in *Proc. 27th Int. Conf. Mach. Learn. (ICML)*, Haifa, Israel, June 2010, pp. 399-406.

[78] A. M. Elbir and K. V. Mishra, "Joint antenna selection and hybrid beamformer design using unquantized and quantized deep learning networks," *IEEE Transactions on Wireless Communications*, vol. 19, no. 3, pp. 1677-1688, Mar. 2020.

[79] L. Dai et al., "Reconfigurable intelligent surface-based wireless communications: Antenna design, prototyping, and experimental results," *IEEE Access*, vol. 8, pp. 45913-45923, 2020.

[80] C. E. Shannon, "A mathematical theory of communication," *Bell System Technical Journal*, vol. 27, no. 3, pp. 379-423, July 1948.

[81] G. Chaccour, M. N. Soorki, W. Saad, M. Bennis, P. Popovski, and M. Debbah, "Seven defining features of terahertz (THz) wireless systems: A fellowship of communication and sensing," arXiv preprint arXiv:2102.07668, Feb. 2021.

[82] Z. Qin, X. Ye, G. Y. Li, and B.-H. F. Juang, "Deep learning in physical layer communications," *IEEE Wireless Communications*, vol. 26, no. 2, pp. 93-99, Apr. 2019.

[83] D. Gündüz, Z. Qin, I. E. Aguerri, H. S. Dhillon, Z. Yang, A. Yener, K. K. Wong, and C.-B. Chae, "Beyond transmitting bits: Context, semantics, and task-oriented communications," *IEEE Journal on Selected Areas in Communications*, vol. 41, no. 1, pp. 5-41, Jan. 2023.

[84] T. J. O'Shea, K. Karra, and T. C. Clancy, "Learning to communicate: Channel auto-encoders, domain specific regularizers, and attention," in *Proc. IEEE Int. Symp. Signal Process. Inf. Technol. (ISSPIT)*, Bilbao, Spain, Dec. 2016, pp. 223-228.

[85] E. Bourtsoulatze, D. B. Kurka, and D. Gündüz, "Deep joint source-channel coding for wireless image transmission," *IEEE Transactions on Cognitive Communications and Networking*, vol. 5, no. 3, pp. 567-579, Sept. 2019.

[86] M. Jankowski, D. Gündüz, and K. Mikolajczyk, "Joint device-edge inference over wireless links with pruning," in *Proc. IEEE 21st Int. Workshop Signal Process. Advances Wireless Commun. (SPAWC)*, Atlanta, GA, USA, May 2020, pp. 1-5.

[87] N. Kato, Z. M. Fadlullah, B. Mao, F. Tang, O. Akashi, T. Inoue, and K. Mizutani, "The deep learning vision for heterogeneous network traffic control: Proposal, challenges, and future perspective," *IEEE Wireless Communications*, vol. 24, no. 3, pp. 146-153, June 2017.

[88] A. Bordes, N. Usunier, A. Garcia-Durán, J. Weston, and O. Yakhnenko, "Translating embeddings for modeling multi-relational data," in *Proc. Advances Neural Inf. Process. Syst. (NeurIPS)*, Lake Tahoe, NV, USA, Dec. 2013.

[89] Z. Wang, J. Zhang, J. Feng, and Z. Chen, "Knowledge graph embedding by translating on hyperplanes," in *Proc. 28th AAAI Conf. Artif. Intell.*, Québec City, QC, Canada, July 2014.

[90] P. Popovski et al., "Wireless access in ultra-reliable low-latency communication (URLLC)," *IEEE Transactions on Communications*, vol. 67, no. 8, pp. 5783-5801, Aug. 2019.

[91] Y. Liu et al., "Goal-oriented communications for the IoT and application to data compression," *IEEE Internet Things J.*, vol. 9, no. 13, pp. 10774-10784, July 2022.

[92] C. She, C. Sun, Z. Gu, Y. Li, C. Yang, H. V. Poor, and B. Vucetic, "A tutorial on ultrareliable and low-latency communications in 6G: Integrating domain knowledge into deep learning," *Proc. IEEE*, vol. 109, no. 3, pp. 204-246, Mar. 2021.

[93] N. Mastronarde and M. van der Schaar, "Joint physical-layer and system-level power management for delay-sensitive wireless communications," *IEEE Transactions on Mobile Computing*, vol. 12, no. 4, pp. 694-709, Apr. 2013.

[94] T. M. Cover and J. A. Thomas, *Elements of Information Theory*, 2nd ed. Hoboken, NJ, USA: Wiley, 2006.

[95] D. B. Kurka and D. Gündüz, "DeepJSCC-f: Deep joint source-channel coding of images with feedback," *IEEE Journal on Selected Areas in Information Theory*, vol. 1, no. 1, pp. 178-193, May 2020.

[96] E. Bourtsoulatze, D. B. Kurka, and D. Gündüz, "Deep joint source-channel coding for wireless image transmission," *IEEE Transactions on Cognitive Communications and Networking*, vol. 5, no. 3, pp. 567-579, Sept. 2019.

[97] S. Duan, Y. Hu, W. Saad, M. Bennis, and M. Debbah, "Large language models for intent-driven 6G networks," arXiv preprint arXiv:2311.00876, Nov. 2023.

[98] J. Wei et al., "Chain-of-thought prompting elicits reasoning in large language models," in *Proc. Advances Neural Inf. Process. Syst. (NeurIPS)*, New Orleans, LA, USA, Nov. 2022.

[99] A. Alahi, K. Goel, V. Ramanathan, A. Robicquet, L. Fei-Fei, and S. Savarese, "Social LSTM: Human trajectory prediction in crowded spaces," in *Proc. IEEE Conf. Comput. Vision Pattern Recognit. (CVPR)*, Las Vegas, NV, USA, June 2016, pp. 961-971.

[100] Y. Kim and A. M. Rush, "Sequence-level knowledge distillation," in *Proc. Conf. Empirical Methods Natural Lang. Process. (EMNLP)*, Austin, TX, USA, Nov. 2016, pp. 1317-1327.

[101] D. Hendrycks and T. Dietterich, "Benchmarking neural network robustness to common corruptions and perturbations," in *Proc. Int. Conf. Learn. Represent. (ICLR)*, New Orleans, LA, USA, May 2019.

[102] Y. Ganin and V. Lempitsky, "Unsupervised domain adaptation by backpropagation," in *Proc. 32nd Int. Conf. Mach. Learn. (ICML)*, Lille, France, July 2015, pp. 1180-1189.

[103] C. Finn, P. Abbeel, and S. Levine, "Model-agnostic meta-learning for fast adaptation of deep networks," in *Proc. 34th Int. Conf. Mach. Learn. (ICML)*, Sydney, NSW, Australia, Aug. 2017, pp. 1126-1135.

[104] T.-W. Weng et al., "Towards fast computation of certified robustness for ReLU networks," in *Proc. 35th Int. Conf. Mach. Learn. (ICML)*, Stockholm, Sweden, July 2018.

[105] J. Park, S. Samarakoon, M. Bennis, and M. Debbah, "Wireless network intelligence at the edge," *Proc. IEEE*, vol. 107, no. 11, pp. 2204-2239, Nov. 2019.

[106] R. Krishnamoorthi, "Quantizing deep convolutional networks for efficient inference: A whitepaper," arXiv preprint arXiv:1806.08342, June 2018.

[107] S. Han, J. Pool, J. Tran, and W. Dally, "Learning both weights and connections for efficient neural network," in *Proc. Advances Neural Inf. Process. Syst. (NeurIPS)*, Montreal, QC, Canada, Dec. 2015.

[108] B. Zoph and Q. V. Le, "Neural architecture search with reinforcement learning," in *Proc. Int. Conf. Learn. Represent. (ICLR)*, Toulon, France, Apr. 2017.

[109] E. Li, Z. Zhou, and X. Chen, "Edge intelligence: On-demand deep learning model co-inference with device-edge synergy," in *Proc. Workshop Mobile Edge Commun. (MECOMM)*, Budapest, Hungary, Aug. 2018, pp. 31-36.

[110] M. Usama et al., "Unsupervised machine learning for networking: Techniques, applications and research challenges," *IEEE Access*, vol. 7, pp. 65579-65615, 2019.

[111] I. J. Goodfellow, J. Shlens, and C. Szegedy, "Explaining and harnessing adversarial examples," in *Proc. Int. Conf. Learn. Represent. (ICLR)*, San Diego, CA, USA, May 2015.

[112] M. Fredrikson, S. Jha, and T. Ristenpart, "Model inversion attacks that exploit confidence information and basic countermeasures," in *Proc. 22nd ACM SIGSAC Conf. Comput. Commun. Security*, Denver, CO, USA, Oct. 2015, pp. 1322-1333.

[113] B. Biggio and F. Roli, "Wild patterns: Ten years after the rise of adversarial machine learning," *Pattern Recognition*, vol. 84, pp. 317-331, Dec. 2018.

[114] A. Madry, A. Makelov, L. Schmidt, D. Tsipras, and A. Vladu, "Towards deep learning models resistant to adversarial attacks," in *Proc. Int. Conf. Learn. Represent. (ICLR)*, Vancouver, BC, Canada, Apr. 2018.

[115] M. Abadi et al., "Deep learning with differential privacy," in *Proc. ACM SIGSAC Conf. Comput. Commun. Security*, Vienna, Austria, Oct. 2016, pp. 308-318.

[116] K. Bonawitz et al., "Towards federated learning at scale: System design," in *Proc. 2nd SysML Conf.*, Palo Alto, CA, USA, Mar. 2019.

[117] D. Gunning and D. Aha, "DARPA's explainable artificial intelligence (XAI) program," *AI Magazine*, vol. 40, no. 2, pp. 44-58, Summer 2019.

[118] D. Bahdanau, K. Cho, and Y. Bengio, "Neural machine translation by jointly learning to align and translate," in *Proc. Int. Conf. Learn. Represent. (ICLR)*, San Diego, CA, USA, May 2015.

[119] S. M. Lundberg and S.-I. Lee, "A unified approach to interpreting model predictions," in *Proc. Advances Neural Inf. Process. Syst. (NeurIPS)*, Long Beach, CA, USA, Dec. 2017.

[120] B. Kim, M. Wattenberg, J. Gilmer, C. Cai, J. Wexler, F. Viegas, and R. Sayres, "Interpretability beyond feature attribution: Quantitative testing with concept activation vectors (TCAV)," in *Proc. 35th Int. Conf. Mach. Learn. (ICML)*, Stockholm, Sweden, July 2018.

[121] V. Sze, Y.-H. Chen, T.-J. Yang, and J. S. Emer, "Efficient processing of deep neural networks: A tutorial and survey," *Proc. IEEE*, vol. 105, no. 12, pp. 2295-2329, Dec. 2017.

[122] S. Gupta, M. Imani, and T. Rosing, "FELIX: Fast embedded learning for intelligent systems," *IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems*, vol. 39, no. 11, pp. 3914-3927, Nov. 2020.

[123] A. Mehonic and A. J. Kenyon, "Brain-inspired computing needs a master plan," *Nature*, vol. 604, no. 7905, pp. 255-260, Apr. 2022.

[124] Y. Shen et al., "Deep learning with coherent nanophotonic circuits," *Nature Photonics*, vol. 11, no. 7, pp. 441-446, July 2017.

[125] 3GPP, "Study on Artificial Intelligence (AI)/Machine Learning (ML) for NR air interface," TR 38.843, Rel. 18, Mar. 2022.

[126] ITU-T Focus Group on Machine Learning for Future Networks including 5G (FG-ML5G), "Architectural framework for machine learning in future networks including IMT-2020," Technical Specification, Sept. 2019.

[127] O-RAN Alliance, "O-RAN: Towards an Open and Smart RAN," White Paper, Oct. 2018.

---

## BIOGRAFÍA

**[Autor]** recibió el grado de [grado académico] en [campo] de [institución] en [año]. Sus intereses de investigación incluyen comunicaciones inalámbricas de nueva generación, aprendizaje automático para el nivel físico, y optimización de sistemas MIMO masivos.
