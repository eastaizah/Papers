# Interfaces Aire AI-Nativas Adaptativas: Co-Diseño de Modulación, Codificación y Waveforms mediante End-to-End Learning para Sistemas 6G

**Resumen**—Las interfaces aire convencionales para sistemas 5G-NR emplean arquitecturas modulares con componentes fijos de modulación (QAM), codificación (LDPC, Polar) y waveforms (OFDM) optimizados independientemente mediante modelos estadísticos del canal que constituyen aproximaciones simplificadas de la realidad física. Estas aproximaciones no capturan completamente las imperfecciones de hardware (no-linealidades de amplificadores, ruido de fase, desbalances I/Q), distorsiones del canal (dispersión, desvanecimiento no-estacionario), ni la variabilidad espacio-temporal de los entornos de propagación reales. Este artículo propone un paradigma alternativo basado en interfaces aire AI-nativas adaptativas que realizan el co-diseño conjunto de modulación, codificación y waveforms mediante aprendizaje end-to-end (E2E). El enfoque propuesto formula la cadena de comunicación completa—desde bits de información hasta símbolos recibidos—como una red neuronal profunda entrenable que aprende representaciones óptimas directamente de los datos observados del canal, sin depender de modelos estadísticos a priori. Se presenta el marco teórico fundamentando el aprendizaje E2E en comunicaciones, incluyendo formulaciones matemáticas rigurosas de autoencoders comunicacionales, funciones de pérdida diferenciables, y algoritmos de entrenamiento con gradientes estimados. Se propone una arquitectura neural híbrida que integra capas convolucionales para extracción de características, módulos de atención para captura de dependencias temporales, y capas recurrentes para modelado de memoria del canal. El sistema propuesto incorpora mecanismos de adaptación en línea mediante meta-aprendizaje que permiten ajuste rápido a condiciones del canal no vistas. Evaluaciones mediante simulación demuestran que el enfoque propuesto supera en 2.1-3.7 dB a sistemas 5G-NR convencionales en canales con imperfecciones de hardware, logrando ganancias de hasta 42% en eficiencia espectral para escenarios de movilidad alta. Se discuten desafíos abiertos incluyendo interpretabilidad, escalabilidad computacional, y estandarización de interfaces AI-nativas para despliegue en redes 6G.

**Palabras clave**—Interfaces Aire AI-Nativas, Aprendizaje End-to-End, Autoencoders Comunicacionales, Redes 6G, Co-Diseño, Modulación Adaptativa, Codificación Neural, Machine Learning para Comunicaciones.

---
## I. INTRODUCCIÓN

### A. Contexto y Motivación

La evolución de las redes de comunicaciones móviles ha seguido un patrón consistente durante las últimas cuatro décadas: cada generación tecnológica introduce nuevos paradigmas de diseño que incrementan la capacidad, reducen la latencia, y amplían el rango de aplicaciones soportadas [1], [2]. La transición de 4G LTE a 5G New Radio (5G-NR) ha representado un salto significativo en términos de velocidades de datos pico (hasta 20 Gbps), latencia ultra-baja (1 ms), y densidad de conexiones (10⁶ dispositivos/km²) [3], [4]. Sin embargo, la visión emergente para sistemas 6G, cuyo despliegue se proyecta para 2030, demanda capacidades aún más ambiciosas que exceden los límites de las arquitecturas actuales [5]–[7].

Los sistemas 6G se conceptualizan para soportar aplicaciones disruptivas incluyendo realidad extendida (XR) holográfica, internet táctil, gemelos digitales masivos, comunicaciones sub-THz, y redes integradas terrestres-satelitales [8], [9]. Estos casos de uso imponen requisitos extremos: velocidades de datos de terabits por segundo, latencias sub-milisegundo, confiabilidad del 99.99999% (ultra-reliable low-latency communications, URLLC), y eficiencia energética 100 veces superior a 5G [10], [11]. Alcanzar estos objetivos mediante extensiones incrementales de las tecnologías 5G-NR existentes resulta fundamentalmente insuficiente, motivando la necesidad de repensar los principios fundamentales del diseño de interfaces aire [12], [13].

Las interfaces aire convencionales para sistemas celulares, incluyendo 5G-NR, se fundamentan en una arquitectura modular clásica donde los componentes de modulación, codificación de canal, y forma de onda (waveform) se diseñan y optimizan independientemente [14], [15]. Esta separación arquitectónica, aunque conceptualmente elegante y matemáticamente tractable, introduce limitaciones inherentes que se manifiestan particularmente en escenarios operacionales complejos [16].

**Limitación 1: Optimización Subóptima por Diseño Modular**

El enfoque tradicional optimiza cada componente aisladamente: los esquemas de modulación (QPSK, 16-QAM, 64-QAM, 256-QAM) maximizan la distancia euclidiana entre símbolos bajo restricciones de potencia promedio; los códigos de canal (LDPC, Polar) minimizan la probabilidad de error de bit para modelos de canal específicos (AWGN, Rayleigh); y las formas de onda (OFDM, DFT-s-OFDM) optimizan criterios como eficiencia espectral y robustez ante multitrayecto [17]–[19]. Sin embargo, la optimización conjunta global del sistema completo—que considera las interdependencias entre modulación, codificación y waveform—permanece intractable analíticamente y, por lo tanto, inexplorada [20].

**Limitación 2: Dependencia de Modelos Estadísticos Simplificados**

El diseño de componentes convencionales se basa en modelos estadísticos del canal que constituyen aproximaciones matemáticas idealizadas de la realidad física [21], [22]. Por ejemplo, el canal AWGN asume ruido Gaussiano blanco aditivo con distribución perfectamente conocida; el modelo de Rayleigh representa desvanecimiento multicamino mediante procesos estocásticos estacionarios; y los modelos 3GPP (TDL, CDL) capturan dispersión temporal mediante perfiles de retardo discretos [23], [24]. Estos modelos, aunque útiles para análisis teórico, omiten múltiples fenómenos críticos presentes en sistemas reales:

- **Imperfecciones de hardware**: No-linealidades de amplificadores de potencia (PA) que generan distorsión armónica e intermodulación; ruido de fase de osciladores locales que introduce rotaciones aleatorias de símbolos; desbalances entre ramas en fase (I) y cuadratura (Q) que degradan la ortogonalidad; cuantización de conversores ADC/DAC que introduce ruido de cuantización [25], [26].

- **Distorsiones del canal no-modeladas**: Dispersión Doppler no-estacionaria en escenarios de movilidad vehicular/aeronáutica; efectos de near-field en comunicaciones massive MIMO y frecuencias sub-THz; scattering electromagnético de superficies rugosas no-Gaussianas; interferencia co-canal correlacionada espacialmente [27]–[29].

- **Variabilidad espacio-temporal**: Los entornos de propagación reales exhiben variaciones significativas en función de la ubicación geográfica (urbano denso, suburbano, rural), configuración arquitectónica (interiores, exteriores, penetración en edificios), condiciones meteorológicas (lluvia, nieve, humedad), y densidad de obstrucciones dinámicas (tráfico vehicular, multitudes) [30], [31].

La brecha entre modelos estadísticos idealizados y canales físicos reales se traduce en degradación de desempeño cuando sistemas diseñados bajo suposiciones simplificadas operan en entornos complejos [32].

**Limitación 3: Adaptación Reactiva con Overhead Significativo**

Los sistemas actuales incorporan mecanismos de adaptación mediante link adaptation, donde el transmisor ajusta esquemas de modulación y codificación (MCS) en respuesta a mediciones de calidad del canal reportadas por el receptor (CQI, channel quality indicator) [33], [34]. Sin embargo, esta adaptación es inherentemente reactiva y limitada a un conjunto discreto y predefinido de MCS. El proceso introduce overhead de señalización bidireccional (mediciones uplink, decisiones downlink), latencia en el ciclo de retroalimentación (típicamente varios slots de transmisión), y errores de predicción cuando el canal varía rápidamente [35], [36].

### B. Revolución de Machine Learning en Comunicaciones

El desarrollo explosivo de técnicas de Machine Learning (ML) y Deep Learning (DL) durante la última década ha transformado múltiples dominios tecnológicos, incluyendo visión computacional, procesamiento de lenguaje natural, y robótica [37]–[39]. Recientemente, la comunidad de comunicaciones inalámbricas ha comenzado a explorar sistemáticamente la aplicación de ML/DL para abordar problemas tradicionalmente resueltos mediante teoría de la información y procesamiento de señales [40]–[42].

Los enfoques basados en ML para comunicaciones se clasifican en tres categorías principales [43]:

**1) ML para Optimización de Componentes Específicos**: Aplicación de ML para mejorar módulos individuales de la cadena de comunicación, manteniendo la arquitectura modular tradicional. Ejemplos incluyen: clasificación automática de modulación mediante CNNs [44]; ecualización de canal mediante redes recurrentes [45]; decodificación de códigos polares mediante redes neuronales [46]; estimación de canal mediante autoencoders variacionales [47]; detección MIMO mediante redes densas [48].

**2) ML para Gestión y Optimización de Recursos**: Utilización de ML para tareas de gestión de red incluyendo: predicción de tráfico mediante LSTMs [49]; optimización de beamforming mediante reinforcement learning [50]; scheduling de usuarios mediante multi-agent learning [51]; selección de espectro mediante bandit algorithms [52]; handover prediction mediante redes de atención [53].

**3) ML para Diseño End-to-End de Sistemas de Comunicación**: Formulación de la cadena de comunicación completa como una red neuronal entrenable que aprende conjuntamente representaciones óptimas de transmisión y recepción directamente de datos, sin diseño manual de componentes individuales [54]–[56]. Este enfoque, denominado aprendizaje end-to-end (E2E) o autoencoders comunicacionales, constituye el paradigma fundamental que motiva el presente trabajo.

### C. Aprendizaje End-to-End: Un Paradigma Disruptivo

El concepto de aprendizaje E2E en comunicaciones fue propuesto formalmente por O'Shea y Hoydis en 2017 [57], aunque ideas precursoras aparecieron en trabajos anteriores sobre modems neuronales [58]. La premisa fundamental es elegantemente simple pero profundamente disruptiva: en lugar de diseñar manualmente componentes de modulación, codificación y procesamiento de señal basados en principios teóricos y modelos estadísticos, se formula el sistema de comunicación completo como una red neuronal diferenciable que se entrena automáticamente para minimizar una función de pérdida relacionada con la tasa de error de bits o información mutua [59], [60].

Matemáticamente, considere un sistema de comunicación que transmite mensajes discretos m ∈ M = {1, 2, ..., M} a través de un canal con respuesta h(·) y ruido n. El enfoque tradicional diseña funciones explícitas de codificación f_enc: M → C^n (mapeando mensajes a señales complejas de n símbolos) y decodificación f_dec: C^n → M (mapeando señales recibidas a mensajes estimados). En contraste, el enfoque E2E parameteriza estas funciones mediante redes neuronales con pesos θ_enc y θ_dec:

$$
\mathbf{x} = f_{\text{enc}}(m; \theta_{\text{enc}}) \in \mathbb{C}^n
$$
(1)

$$
\mathbf{y} = h(\mathbf{x}) + \mathbf{n}
$$
(2)

$$
\hat{m} = f_{\text{dec}}(\mathbf{y}; \theta_{\text{dec}})
$$
(3)

Los parámetros θ_enc y θ_dec se optimizan conjuntamente minimizando la función de pérdida:

$$
\mathcal{L}(\theta_{\text{enc}}, \theta_{\text{dec}}) = \mathbb{E}_{m \sim p(m), \mathbf{n} \sim p(\mathbf{n})} \left[ \ell(m, \hat{m}) \right]
$$
(4)

donde ℓ(m, m̂) es una función de pérdida por mensaje (típicamente cross-entropy para clasificación) y la esperanza se calcula sobre la distribución de mensajes y ruido.

El entrenamiento se realiza mediante descenso de gradiente estocástico (SGD) o variantes (Adam, RMSprop):

$$
\theta_{\text{enc}}^{(t+1)} = \theta_{\text{enc}}^{(t)} - \eta \nabla_{\theta_{\text{enc}}} \mathcal{L}
$$
(5)

$$
\theta_{\text{dec}}^{(t+1)} = \theta_{\text{dec}}^{(t)} - \eta \nabla_{\theta_{\text{dec}}} \mathcal{L}
$$
(6)

donde η es la tasa de aprendizaje y los gradientes se calculan mediante backpropagation [61].

**Ventajas Conceptuales del Aprendizaje E2E**:

1. **Optimización Conjunta**: El entrenamiento E2E optimiza simultáneamente todos los componentes del sistema considerando sus interdependencias, potencialmente alcanzando puntos de operación superiores a diseños modulares [62].

2. **Aprendizaje de Datos Reales**: El sistema aprende directamente de observaciones del canal real, capturando implícitamente imperfecciones, no-linealidades y características que no se modelan explícitamente [63].

3. **Adaptabilidad**: Las redes neuronales pueden ajustarse mediante fine-tuning o meta-aprendizaje para adaptarse rápidamente a nuevas condiciones de canal [64].

4. **Sin Suposiciones de Modelo**: El enfoque no requiere especificar modelos estadísticos del canal a priori, siendo agnóstico al mecanismo físico subyacente [65].

Sin embargo, el aprendizaje E2E también presenta desafíos significativos que han limitado su adopción práctica, incluyendo diferenciabilidad del canal, escalabilidad computacional, interpretabilidad, y estandarización [66], [67].

### D. Contribuciones del Presente Trabajo

Este artículo propone un marco integral para el diseño, implementación y evaluación de interfaces aire AI-nativas adaptativas basadas en aprendizaje E2E para sistemas 6G. Las contribuciones principales se articulan como sigue:

**Contribución 1: Marco Teórico Unificado para Aprendizaje E2E en Comunicaciones**

Se desarrolla una formulación matemática rigurosa y unificada del aprendizaje E2E que extiende la conceptualización original de autoencoders comunicacionales para incorporar múltiples aspectos críticos previamente no tratados sistemáticamente: co-diseño conjunto de modulación, codificación y waveform como problema de optimización multi-objetivo; formulación de funciones de pérdida diferenciables que consideran restricciones de potencia, ancho de banda y espectro de emisión; técnicas de gradientes estimados para manejar componentes no-diferenciables incluyendo cuantización, conversión ADC/DAC y procesamiento de tiempo discreto; e integración de conocimiento a priori mediante regularización estructurada y arquitecturas con inductive bias apropiado.

**Contribución 2: Arquitectura Neural Híbrida para Co-Diseño de Interfaz Aire**

Se propone una arquitectura neural profunda novedosa que integra múltiples componentes especializados para capturar diferentes aspectos de la cadena de comunicación: capas convolucionales temporales para extracción jerárquica de características con invariancia a traslación temporal; módulos de atención multi-cabeza para captura de dependencias de largo alcance y selección adaptativa de información relevante; capas recurrentes bidireccionales con memoria de largo-corto plazo para modelado de efectos de memoria del canal; normalización adaptativa de características para estabilización del entrenamiento bajo variaciones de potencia; y mecanismos de conditioning para incorporación de información auxiliar sobre condiciones del canal.

**Contribución 3: Algoritmos de Entrenamiento Robusto y Eficiente**

Se desarrollan técnicas de entrenamiento especializadas que abordan los desafíos únicos del aprendizaje E2E en comunicaciones: curriculum learning con incremento progresivo de dificultad del canal; data augmentation específico para comunicaciones mediante simulación de múltiples condiciones de canal; regularización mediante penalización de restricciones de potencia y continuidad espectral; técnicas de estabilización numérica para evitar colapso de representaciones; y estrategias de batch normalization y layer normalization adaptadas a señales complejas.

**Contribución 4: Meta-Aprendizaje para Adaptación Rápida**

Se integra un marco de meta-aprendizaje basado en Model-Agnostic Meta-Learning que permite al sistema adaptarse rápidamente a nuevas condiciones de canal con mínimas muestras de entrenamiento adicional. La formulación desarrollada considera el problema de adaptación como meta-aprendizaje few-shot donde cada tarea corresponde a una condición específica de canal, permitiendo aprendizaje de representaciones iniciales que facilitan transferencia eficiente.

**Contribución 5: Evaluación Exhaustiva en Escenarios Realistas**

Se presenta una evaluación comprehensiva del sistema propuesto mediante simulaciones que replican fielmente condiciones operacionales de sistemas 6G: canales 3GPP con modelos de propagación para frecuencias sub-6 GHz y mmWave; imperfecciones de hardware incluyendo no-linealidades de PA modeladas mediante modelos Rapp y Saleh, ruido de fase con espectro Lorentziano, y desbalances I/Q; escenarios de movilidad con velocidades de hasta 500 km/h; e interferencia co-canal con múltiples usuarios. Se realizan comparaciones sistemáticas con baselines incluyendo 5G-NR, autoencoders E2E básicos, y sistemas de referencia teóricos.

### E. Organización del Artículo

El resto del artículo se estructura como sigue. La Sección II presenta los fundamentos teóricos incluyendo teoría de la información para sistemas E2E, formulación de autoencoders comunicacionales, y técnicas de optimización diferenciable. La Sección III describe la arquitectura del sistema propuesto con detalles de componentes de transmisor y receptor. La Sección IV desarrolla los algoritmos de entrenamiento y técnicas de meta-aprendizaje. La Sección V presenta resultados de evaluación y análisis comparativo. La Sección VI discute los aportes específicos de este trabajo. La Sección VII analiza desafíos abiertos y direcciones futuras de investigación. La Sección VIII concluye el artículo. Las referencias bibliográficas se presentan al final.


## II. FUNDAMENTOS TEÓRICOS

### A. Teoría de la Información para Sistemas End-to-End

El análisis teórico-informacional de sistemas de comunicación E2E basados en aprendizaje profundo requiere extender conceptos clásicos de teoría de la información de Shannon para acomodar representaciones aprendidas mediante optimización empírica en lugar de diseño analítico [68], [69].

#### 1) Capacidad Alcanzable mediante Aprendizaje

Considere un canal discreto sin memoria caracterizado por la probabilidad de transición p(y|x), donde x ∈ X es el símbolo de entrada y y ∈ Y es la salida. La capacidad de Shannon C se define como:

$$
C = \max_{p(x)} I(X; Y)
$$
(7)

donde I(X; Y) denota la información mutua:

$$
I(X; Y) = \sum_{x \in \mathcal{X}} \sum_{y \in \mathcal{Y}} p(x,y) \log \frac{p(x,y)}{p(x)p(y)}
$$
(8)

Para un sistema E2E, el codificador neural f_enc(m; θ_enc) induce implícitamente una distribución sobre símbolos transmitidos. Si M mensajes equiprobables se mapean a puntos en el espacio de señales C^n con restricción de potencia promedio P:

$$
\frac{1}{M} \sum_{m=1}^{M} \|\mathbf{x}_m\|^2 \leq nP
$$
(9)

la tasa alcanzable R del sistema está limitada por:

$$
R \leq \frac{1}{n} I(\mathbf{X}; \mathbf{Y})
$$
(10)

donde X y Y son vectores aleatorios de n símbolos. Para canales AWGN con relación señal-ruido (SNR) ρ = P/σ², la capacidad por dimensión compleja es:

$$
C_{\text{AWGN}} = \log_2(1 + \rho) \text{ bits/símbolo}
$$
(11)

El teorema de Shannon garantiza que existen esquemas de codificación que alcanzan tasas arbitrariamente cercanas a C con probabilidad de error arbitrariamente baja para longitudes de bloque suficientemente grandes [70]. Sin embargo, estos esquemas óptimos son constructivamente desconocidos para la mayoría de canales prácticos. El aprendizaje E2E ofrece una ruta alternativa: aprender empíricamente codificadores y decodificadores que se aproximen al desempeño óptimo mediante optimización sobre grandes datasets [71].

#### 2) Límites Fundamentales y Tradeoffs

El diseño de sistemas E2E enfrenta múltiples tradeoffs fundamentales que reflejan límites teórico-informacionales [72]:

**Tradeoff Tasa-Confiabilidad**: Para una restricción de potencia fija y SNR ρ, incrementar la tasa de transmisión R inevitablemente aumenta la probabilidad de error P_e. La relación entre R y P_e está gobernada por los exponentes de error de la teoría de la información [73]:

$$
P_e \geq \exp\left(-nE_r(R)\right)
$$
(12)

donde E_r(R) es el exponente de error aleatorio que decae a cero cuando R → C.

**Tradeoff Complejidad-Desempeño**: Redes neuronales más profundas y complejas pueden potencialmente aprender representaciones más ricas, pero requieren mayor cómputo de entrenamiento e inferencia, y mayor cantidad de datos de entrenamiento para evitar sobreajuste [74]:

$$
\mathcal{C}_{\text{comp}} \propto d \cdot L \cdot W
$$
(13)

donde d es la dimensionalidad de entrada, L es el número de capas, y W es el ancho promedio de capas.

**Tradeoff Generalización-Memorización**: Modelos con alta capacidad pueden memorizar el conjunto de entrenamiento sin generalizar a condiciones no vistas. La brecha de generalización se cuantifica como [75]:

$$
\mathcal{G} = \mathcal{L}_{\text{test}} - \mathcal{L}_{\text{train}}
$$
(14)

Regularización y técnicas como dropout, batch normalization y data augmentation buscan minimizar G [76].

### B. Autoencoders Comunicacionales: Formulación Matemática

La abstracción fundamental para sistemas E2E es el autoencoder comunicacional, que reformula la cadena de comunicación como un autoencoder probabilístico donde el canal actúa como capa estocástica intermedia [77], [78].

#### 1) Arquitectura Básica

Un autoencoder comunicacional consta de tres componentes:

**Codificador (Transmisor)**: Mapea mensajes discretos m ∈ {1, ..., M} a señales complejas x ∈ C^n:

$$
\mathbf{x} = f_{\text{enc}}(m; \theta_{\text{enc}}) = g_{\text{norm}}\left( \text{NN}_{\text{enc}}(\text{one-hot}(m); \theta_{\text{enc}}) \right)
$$
(15)

donde one-hot(m) ∈ {0,1}^M es la representación one-hot del mensaje, NN_enc es una red neuronal profunda, y g_norm es una función de normalización que impone la restricción de potencia:

$$
g_{\text{norm}}(\mathbf{z}) = \sqrt{nP} \cdot \frac{\mathbf{z}}{\|\mathbf{z}\|}
$$
(16)

**Canal**: Transforma la señal transmitida incorporando efectos de propagación y ruido:

$$
\mathbf{y} = h_{\text{channel}}(\mathbf{x}, \boldsymbol{\theta}_{\text{ch}}) + \mathbf{n}
$$
(17)

donde θ_ch parametriza características del canal (ganancia, retardos, Doppler) y n ~ CN(0, σ²I_n) es ruido AWGN complejo.

**Decodificador (Receptor)**: Mapea señales recibidas y ∈ C^n a estimaciones de mensaje m̂:

$$
\hat{m} = f_{\text{dec}}(\mathbf{y}; \theta_{\text{dec}}) = \arg\max_{i=1}^{M} \left[ \text{softmax}\left( \text{NN}_{\text{dec}}(\mathbf{y}; \theta_{\text{dec}}) \right) \right]_i
$$
(18)

donde NN_dec es una red neuronal que produce logits para cada clase de mensaje.

#### 2) Función de Pérdida y Entrenamiento

El entrenamiento conjunto de codificador y decodificador minimiza la entropía cruzada promedio:

$$
\mathcal{L}(\theta_{\text{enc}}, \theta_{\text{dec}}) = -\frac{1}{B} \sum_{i=1}^{B} \sum_{j=1}^{M} \mathbb{1}_{m_i = j} \log p_{\text{dec}}(j | \mathbf{y}_i; \theta_{\text{dec}})
$$
(19)

donde B es el tamaño de batch, m_i son mensajes en el batch, y_i son las señales recibidas correspondientes, y p_dec(j|y_i) es la probabilidad predicha por el decodificador para el mensaje j.

Equivalentemente, puede minimizarse la probabilidad de error de bloque:

$$
\mathcal{L}_{\text{BLER}} = \frac{1}{B} \sum_{i=1}^{B} \mathbb{1}_{\hat{m}_i \neq m_i}
$$
(20)

Sin embargo, esta función no es diferenciable. En su lugar, se utiliza la aproximación suave mediante entropía cruzada, que es un upper bound diferenciable de la probabilidad de error [79].

Los gradientes se calculan mediante backpropagation a través de toda la cadena:

$$
\frac{\partial \mathcal{L}}{\partial \theta_{\text{enc}}} = \frac{\partial \mathcal{L}}{\partial \mathbf{y}} \frac{\partial \mathbf{y}}{\partial \mathbf{x}} \frac{\partial \mathbf{x}}{\partial \theta_{\text{enc}}}
$$
(21)

$$
\frac{\partial \mathcal{L}}{\partial \theta_{\text{dec}}} = \frac{\partial \mathcal{L}}{\partial \hat{m}} \frac{\partial \hat{m}}{\partial \mathbf{y}} \frac{\partial \mathbf{y}}{\partial \theta_{\text{dec}}}
$$
(22)

El término crítico es ∂y/∂x, que requiere que el canal sea diferenciable. Para canales físicos reales, esto no es posible, motivando técnicas de gradientes estimados que se discuten posteriormente [80].

### C. Representación de Señales Complejas en Redes Neuronales

Las señales de comunicación son inherentemente complejas (x ∈ C^n), pero la mayoría de frameworks de deep learning operan sobre números reales. Existen tres enfoques principales para manejar esta incompatibilidad [81], [82]:

#### 1) Representación Real Equivalente

Se representa cada número complejo z = a + jb mediante el vector real [a, b]^T ∈ R²:

$$
\mathbf{x}_{\mathbb{R}} = \begin{bmatrix} \text{Re}(\mathbf{x}) \\ \text{Im}(\mathbf{x}) \end{bmatrix} \in \mathbb{R}^{2n}
$$
(23)

Las operaciones de redes neuronales se realizan sobre x_R. Esta representación es simple pero no explota la estructura algebraica de números complejos [83].

#### 2) Redes Neuronales Complejas

Se extienden operaciones neuronales al dominio complejo. Una capa lineal compleja se define como:

$$
\mathbf{z} = \mathbf{W}\mathbf{x} + \mathbf{b}
$$
(24)

donde W ∈ C^{m×n} y b ∈ C^m son parámetros complejos. Las funciones de activación se aplican independientemente a partes real e imaginaria:

$$
\phi_{\mathbb{C}}(z) = \phi(\text{Re}(z)) + j\phi(\text{Im}(z))
$$
(25)

o se utilizan activaciones específicamente complejas como CReLU, zReLU, modReLU [84]:

$$
\text{modReLU}(z) = \text{ReLU}(|z| + b) \cdot \frac{z}{|z|}
$$
(26)

Las redes complejas tienen ventajas teóricas (respetan simetrías de las señales, menor número de parámetros) pero requieren implementación customizada [85].

#### 3) Representación Polar

Se representa z = re^{jθ} mediante magnitud r y fase θ:

$$
\mathbf{x}_{\text{polar}} = \begin{bmatrix} |\mathbf{x}| \\ \angle\mathbf{x} \end{bmatrix}
$$
(27)

Esta representación es natural para ciertos tipos de distorsiones (amplitud y fase independientes) pero introduce discontinuidades en θ que complican el aprendizaje [86].

### D. Modelado Diferenciable del Canal

El entrenamiento E2E requiere calcular gradientes a través del canal, lo cual es problemático cuando el canal físico no es diferenciable o no está disponible durante el entrenamiento. Se han desarrollado varias técnicas para abordar este desafío [87], [88]:

#### 1) Modelado Analítico Diferenciable

Para canales cuyo comportamiento puede expresarse analíticamente, se implementa el modelo del canal como operaciones diferenciables. Por ejemplo, un canal AWGN es trivialmente diferenciable:

$$
\mathbf{y} = \mathbf{x} + \mathbf{n}, \quad \frac{\partial \mathbf{y}}{\partial \mathbf{x}} = \mathbf{I}
$$
(28)

Un canal con desvanecimiento plano multiplicativo h ~ CN(0, σ_h²) es:

$$
\mathbf{y} = h\mathbf{x} + \mathbf{n}, \quad \frac{\partial \mathbf{y}}{\partial \mathbf{x}} = h \mathbf{I}
$$
(29)

Para canales selectivos en frecuencia con respuesta impulsional h = [h₀, h₁, ..., h_L]:

$$
y[n] = \sum_{\ell=0}^{L} h_\ell x[n-\ell] + n[n]
$$
(30)

$$
\frac{\partial y[n]}{\partial x[k]} = h_{n-k} \text{ si } 0 \leq n-k \leq L, \text{ 0 de otro modo}
$$
(31)

Los modelos de canal 3GPP (TDL, CDL) pueden implementarse como convoluciones diferenciables [89].

#### 2) Estimación de Gradientes mediante Muestras

Cuando el canal es estocástico o solo accesible vía simulación black-box, se estiman gradientes mediante técnicas como REINFORCE o reparameterization trick [90], [91]:

**REINFORCE (Score Function Estimator)**: Se estima el gradiente de la esperanza mediante:

$$
\nabla_{\theta} \mathbb{E}_{p(y|x,\theta)}[\mathcal{L}(y)] = \mathbb{E}_{p(y|x,\theta)}\left[ \mathcal{L}(y) \nabla_{\theta} \log p(y|x,\theta) \right]
$$
(32)

**Reparameterization Trick**: Si la distribución del canal puede reparametrizarse como y = g(x, ϵ; θ) donde ϵ es ruido con distribución conocida independiente de θ, entonces:

$$
\nabla_{\theta} \mathbb{E}_{p(\epsilon)}[\mathcal{L}(g(x, \epsilon; \theta))] = \mathbb{E}_{p(\epsilon)}\left[ \nabla_{\theta} \mathcal{L}(g(x, \epsilon; \theta)) \right]
$$
(33)

permitiendo muestreo de gradientes insesgados [92].

#### 3) Aprendizaje del Modelo de Canal

Se entrena una red neuronal separada para aprender el mapeo x → y del canal a partir de datos observados:

$$
\hat{h}(\mathbf{x}; \phi) \approx h_{\text{true}}(\mathbf{x})
$$
(34)

donde φ son parámetros aprendidos. Una vez entrenado, ĥ se utiliza como canal diferenciable sustituto durante el entrenamiento del autoencoder. Este enfoque se denomina "channel-model learning" o "inverse channel modeling" [93], [94].

La función de pérdida para entrenar el modelo de canal es típicamente MSE:

$$
\mathcal{L}_{\text{channel}}(\phi) = \mathbb{E}_{\mathbf{x}, \mathbf{y}_{\text{real}}} \left[ \|\hat{h}(\mathbf{x}; \phi) - \mathbf{y}_{\text{real}}\|^2 \right]
$$
(35)

Un desafío es que el modelo de canal puede introducir bias si no captura perfectamente la física real, llevando a desempeño subóptimo [95].

### E. Restricciones de Potencia y Espectro

Los sistemas de comunicación reales deben operar bajo restricciones regulatorias y físicas de potencia transmitida y ocupación espectral [96], [97]:

#### 1) Restricción de Potencia Promedio

La restricción fundamental es que la potencia promedio de las señales transmitidas no exceda un límite P_max:

$$
\frac{1}{M} \sum_{m=1}^{M} \mathbb{E}\left[ \|\mathbf{x}_m\|^2 \right] \leq P_{\max}
$$
(36)

Esta restricción se impone típicamente mediante normalización explícita en el codificador (ecuación 16). Alternativamente, puede incorporarse como penalización en la función de pérdida:

$$
\mathcal{L}_{\text{power}} = \lambda_P \max\left(0, \frac{1}{M} \sum_{m=1}^{M} \|\mathbf{x}_m\|^2 - P_{\max}\right)^2
$$
(37)

donde λ_P es un multiplicador de Lagrange [98].

#### 2) Restricción de Potencia Pico-Promedio (PAPR)

La razón de potencia pico-promedio (PAPR) es crítica para eficiencia de amplificadores:

$$
\text{PAPR} = \frac{\max_n |x[n]|^2}{\frac{1}{n}\sum_{k=1}^{n} |x[k]|^2}
$$
(38)

Valores altos de PAPR requieren amplificadores con gran rango dinámico y reducen eficiencia energética. Se penaliza PAPR mediante:

$$
\mathcal{L}_{\text{PAPR}} = \lambda_{\text{PAPR}} \cdot \text{PAPR}(\mathbf{x})
$$
(39)

#### 3) Restricción Espectral

Las regulaciones espectrales requieren que las emisiones fuera de banda (OOBE) estén por debajo de máscaras espectrales regulatorias. La densidad espectral de potencia (PSD) se calcula como:

$$
S(f) = \mathbb{E}\left[ \left| \sum_{n=0}^{N-1} x[n] e^{-j2\pi fn/N} \right|^2 \right]
$$
(40)

Se penalizan violaciones de la máscara espectral M(f):

$$
\mathcal{L}_{\text{spectrum}} = \lambda_S \int_{f} \max(0, S(f) - M(f))^2 df
$$
(41)

En implementación discreta:

$$
\mathcal{L}_{\text{spectrum}} = \lambda_S \sum_{k=1}^{N_{\text{FFT}}} \max(0, |X[k]|^2 - M[k])^2
$$
(42)

donde X[k] es la FFT de x[n] [99], [100].

### F. Diferenciabilidad de Operaciones Discretas

Varios componentes de sistemas de comunicación involucran operaciones discretas no-diferenciables que rompen el flujo de gradientes [101], [102]:

#### 1) Cuantización

La cuantización de símbolos complejos x a un conjunto discreto Q es no-diferenciable:

$$
\text{Quant}(x) = \arg\min_{q \in \mathcal{Q}} |x - q|
$$
(43)

Se utilizan aproximaciones diferenciables [103]:

**Straight-Through Estimator (STE)**: En forward pass se aplica cuantización, en backward pass se usa identidad:

$$
\text{Forward: } y = \text{Quant}(x), \quad \text{Backward: } \frac{\partial y}{\partial x} = 1
$$
(44)

**Softmax Relaxation**: Se reemplaza argmin por softmax con temperatura τ:

$$
\text{Quant}_{\text{soft}}(x) = \sum_{q \in \mathcal{Q}} q \cdot \frac{\exp(-|x-q|^2/\tau)}{\sum_{q' \in \mathcal{Q}} \exp(-|x-q'|^2/\tau)}
$$
(45)

Cuando τ → 0, la versión soft converge a cuantización hard [104].

#### 2) Conversión ADC/DAC

Los conversores analógico-digital (ADC) y digital-analógico (DAC) introducen cuantización y efectos no-lineales. Se modelan mediante:

$$
x_{\text{DAC}} = \text{Quant}_B(x) + n_{\text{DAC}}
$$
(46)

donde Quant_B es cuantización con B bits de resolución y n_DAC es ruido de cuantización modelado como ruido uniforme [105]:

$$
n_{\text{DAC}} \sim \mathcal{U}\left(-\frac{\Delta}{2}, \frac{\Delta}{2}\right), \quad \Delta = \frac{2A}{2^B}
$$
(47)

con A siendo el rango de amplitud. Durante el entrenamiento, se utiliza STE para permitir gradientes [106].

#### 3) Detección Hard

La decisión hard de símbolos en el receptor es no-diferenciable:

$$
\hat{s} = \arg\min_{s \in \mathcal{S}} |y - s|
$$
(48)

Se reemplaza por decisión soft usando log-probabilidades:

$$
p(s | y) = \frac{\exp(-|y - s|^2 / (2\sigma^2))}{\sum_{s' \in \mathcal{S}} \exp(-|y - s'|^2 / (2\sigma^2))}
$$
(49)

El decodificador opera sobre probabilidades soft, permitiendo gradientes continuos [107].


## III. ARQUITECTURA DEL SISTEMA PROPUESTO

### A. Visión General del Sistema

El sistema propuesto implementa una interfaz aire AI-nativa que reemplaza los componentes fijos de modulación, codificación y waveform de sistemas convencionales por una arquitectura neural profunda entrenada end-to-end [108]. La Figura 1 ilustra conceptualmente la arquitectura completa, que consta de cinco bloques funcionales principales:

1. **Pre-procesador de Mensajes**: Convierte mensajes discretos m ∈ {1, ..., M} en representaciones vectoriales apropiadas para procesamiento neural.
2. **Codificador Neural Profundo**: Genera representaciones complejas de señales x ∈ C^n optimizadas para el canal.
3. **Módulo de Imposición de Restricciones**: Asegura cumplimiento de restricciones de potencia, PAPR y espectro.
4. **Decodificador Neural Profundo**: Procesa señales recibidas y ∈ C^n para extraer información de mensajes.
5. **Post-procesador de Decisión**: Genera estimaciones finales m̂ de mensajes transmitidos.

La arquitectura está diseñada con los siguientes principios:

**Principio 1 - Invariancia a Traslación Temporal**: Las capas convolucionales explotan la estructura temporal de las señales, permitiendo compartir parámetros y reducir complejidad [109].

**Principio 2 - Captura de Dependencias de Largo Alcance**: Los módulos de atención y capas recurrentes modelan dependencias temporales extendidas causadas por dispersión del canal [110].

**Principio 3 - Procesamiento Multi-Escala**: Se extraen características en múltiples escalas temporales mediante arquitecturas jerárquicas con pooling y dilated convolutions [111].

**Principio 4 - Normalización Adaptativa**: Normalización de características estabiliza entrenamiento bajo variaciones de potencia y condiciones del canal [112].

**Principio 5 - Conditioning sobre Información Auxiliar**: El sistema puede condicionarse sobre información lateral (SNR, tipo de canal, requisitos de QoS) mediante mecanismos de conditioning [113].

### B. Codificador Neural (Transmisor)

#### 1) Embedding de Mensajes

Los mensajes discretos m ∈ {1, ..., M} se convierten inicialmente en vectores densos mediante embedding aprendido:

$$
\mathbf{e}_m = \mathbf{W}_{\text{emb}} \cdot \text{one-hot}(m) + \mathbf{b}_{\text{emb}}
$$
(50)

donde W_emb ∈ R^{d_emb × M} es la matriz de embedding y d_emb es la dimensión de embedding. Esta representación permite al modelo aprender similitudes semánticas entre mensajes [114].

#### 2) Bloque de Codificación Profunda

El embedding pasa por una secuencia de L capas de procesamiento:

$$
\mathbf{h}^{(0)} = \mathbf{e}_m
$$
(51)

$$
\mathbf{h}^{(\ell)} = \text{TransformerBlock}(\mathbf{h}^{(\ell-1)}), \quad \ell = 1, ..., L
$$
(52)

Cada TransformerBlock consiste en:

**Self-Attention Multi-Cabeza**: Computa atención sobre características temporales:

$$
\text{Attention}(\mathbf{Q}, \mathbf{K}, \mathbf{V}) = \text{softmax}\left(\frac{\mathbf{Q}\mathbf{K}^T}{\sqrt{d_k}}\right)\mathbf{V}
$$
(53)

donde Q = h W_Q, K = h W_K, V = h W_V son proyecciones query, key y value [115].

Para H cabezas paralelas:

$$
\text{MultiHead}(\mathbf{h}) = \text{Concat}(\text{head}_1, ..., \text{head}_H)\mathbf{W}^O
$$
(54)

$$
\text{head}_i = \text{Attention}(\mathbf{h}\mathbf{W}_i^Q, \mathbf{h}\mathbf{W}_i^K, \mathbf{h}\mathbf{W}_i^V)
$$
(55)

**Feed-Forward Network**: Red densa con activación no-lineal:

$$
\text{FFN}(\mathbf{h}) = \text{GELU}(\mathbf{h}\mathbf{W}_1 + \mathbf{b}_1)\mathbf{W}_2 + \mathbf{b}_2
$$
(56)

donde GELU es la activación Gaussian Error Linear Unit:

$$
\text{GELU}(x) = x \cdot \Phi(x) = x \cdot \frac{1}{2}\left[1 + \text{erf}\left(\frac{x}{\sqrt{2}}\right)\right]
$$
(57)

**Normalización y Conexiones Residuales**:

$$
\mathbf{h}' = \text{LayerNorm}(\mathbf{h} + \text{MultiHead}(\mathbf{h}))
$$
(58)

$$
\mathbf{h}^{(\ell)} = \text{LayerNorm}(\mathbf{h}' + \text{FFN}(\mathbf{h}'))
$$
(59)

donde LayerNorm normaliza sobre la dimensión de características [116]:

$$
\text{LayerNorm}(\mathbf{h}) = \gamma \odot \frac{\mathbf{h} - \mu}{\sqrt{\sigma^2 + \epsilon}} + \beta
$$
(60)

con μ = mean(h), σ² = var(h), y γ, β parámetros aprendibles.

#### 3) Generación de Símbolos Complejos

La representación final h^(L) se proyecta a n símbolos complejos:

$$
\mathbf{z} = \mathbf{W}_{\text{proj}} \mathbf{h}^{(L)} + \mathbf{b}_{\text{proj}} \in \mathbb{C}^n
$$
(61)

implementado como dos proyecciones lineales para componentes real e imaginaria:

$$
\text{Re}(\mathbf{z}) = \mathbf{W}_{\text{re}} \mathbf{h}^{(L)} + \mathbf{b}_{\text{re}}
$$
(62)

$$
\text{Im}(\mathbf{z}) = \mathbf{W}_{\text{im}} \mathbf{h}^{(L)} + \mathbf{b}_{\text{im}}
$$
(63)

#### 4) Normalización y Shaping Espectral

Los símbolos z se procesan para cumplir restricciones:

**Normalización de Potencia**: Se normaliza a potencia unitaria por símbolo:

$$
\mathbf{x}_{\text{norm}} = \sqrt{n} \cdot \frac{\mathbf{z}}{\|\mathbf{z}\|}
$$
(64)

**Pulse Shaping**: Se aplica filtro conformador de pulso g(t) para limitar ancho de banda:

$$
s(t) = \sum_{k=0}^{n-1} x_{\text{norm}}[k] \cdot g(t - kT_s)
$$
(65)

En implementación discreta con upsampling por factor K:

$$
s[m] = \sum_{k=0}^{n-1} x_{\text{norm}}[k] \cdot g[m - kK]
$$
(66)

El filtro g[m] se implementa como capa convolucional 1D con kernel aprendible g_NN[m]:

$$
\mathbf{x}_{\text{shaped}} = \text{Conv1D}(\mathbf{x}_{\text{norm}}, \mathbf{g}_{\text{NN}})
$$
(67)

con restricción de normalización de energía sobre g_NN para mantener potencia [117].

**Reducción de PAPR**: Se aplica clipping suave diferenciable:

$$
\text{SoftClip}(x, A) = A \cdot \tanh\left(\frac{x}{A}\right)
$$
(68)

donde A es la amplitud de clipping, controlando el tradeoff entre PAPR y distorsión [118].

#### 5) Capas de Conditioning

Para adaptación dependiente del contexto, se incorpora información auxiliar c (SNR, latencia requerida, tipo de canal):

$$
\mathbf{h}_{\text{cond}} = \mathbf{h} + \text{MLP}(\mathbf{c})
$$
(69)

donde MLP(c) proyecta el vector de conditioning a la misma dimensionalidad que h. Alternativamente, se usa FiLM (Feature-wise Linear Modulation) [119]:

$$
\text{FiLM}(\mathbf{h}, \mathbf{c}) = \gamma(\mathbf{c}) \odot \mathbf{h} + \beta(\mathbf{c})
$$
(70)

donde γ(c) y β(c) son funciones aprendidas que modulan características.

### C. Modelo de Canal

#### 1) Canal AWGN con Imperfecciones

El modelo de canal más simple es AWGN con imperfecciones de hardware [120]:

$$
\mathbf{y} = \alpha \mathbf{x} + \mathbf{n}_{\text{AWGN}}
$$
(71)

donde α es ganancia del canal (modelando path loss) y n_AWGN ~ CN(0, σ²I).

**No-Linealidades de Amplificador**: Se modelan mediante modelo Rapp [121]:

$$
f_{\text{PA}}(x) = \frac{x}{\left(1 + \left(\frac{|x|}{A_{\text{sat}}}\right)^{2p}\right)^{1/(2p)}} e^{j\angle x}
$$
(72)

donde A_sat es amplitud de saturación y p controla suavidad (típicamente p = 2-3).

**Ruido de Fase**: Modela imperfecciones de oscilador local [122]:

$$
\phi[n] = \phi[n-1] + \Delta\omega[n]
$$
(73)

donde Δω[n] ~ N(0, σ_PN²) es ruido de fase incremental. La señal afectada es:

$$
\tilde{x}[n] = x[n] e^{j\phi[n]}
$$
(74)

**Desbalances I/Q**: Ganancias y fases desbalanceadas en ramas I/Q [123]:

$$
\tilde{x} = g_I x_I + j g_Q e^{j\Delta\phi} x_Q
$$
(75)

donde g_I, g_Q son ganancias y Δφ es desbalance de fase.

#### 2) Canal Selectivo en Frecuencia

Para modelar dispersión temporal, se usa convolución con respuesta impulsional del canal [124]:

$$
y[n] = \sum_{\ell=0}^{L-1} h[\ell] x[n-\ell] + n[n]
$$
(76)

Los coeficientes h[ℓ] siguen distribuciones Rayleigh o Rice:

$$
|h[\ell]| \sim \text{Rayleigh}(\sigma_\ell) \text{ o } \text{Rice}(K_\ell, \Omega_\ell)
$$
(77)

Para canales time-varying, h[ℓ] evoluciona según modelo de Jakes [125]:

$$
h[\ell, t] = \sum_{p=1}^{N_p} e^{j(2\pi f_{D,p} t + \psi_p)}
$$
(78)

donde f_D,p son frecuencias Doppler y ψ_p fases aleatorias.

#### 3) Modelos 3GPP

Se implementan modelos de canal estandarizados 3GPP TR 38.901 [126]:

**TDL (Tapped Delay Line)**: Canal con taps discretos:

$$
h(t) = \sum_{n=1}^{N} h_n \delta(t - \tau_n)
$$
(79)

donde h_n ~ CN(0, P_n) con perfil de potencia P_n especificado (TDL-A, TDL-B, TDL-C).

**CDL (Clustered Delay Line)**: Modelo con clusters espaciales:

$$
h_{u,s}(t, \tau) = \sum_{n=1}^{N} h_{n,u,s} \delta(\tau - \tau_n)
$$
(80)

donde u, s indexan antenas de usuario y estación base.

La implementación neural del canal se realiza como capa convolucional con pesos h[ℓ] muestreados del modelo estocástico [127].

### D. Decodificador Neural (Receptor)

#### 1) Pre-Procesamiento de Señal Recibida

La señal recibida y ∈ C^n se normaliza y procesa:

$$
\mathbf{y}_{\text{norm}} = \frac{\mathbf{y}}{\sqrt{\frac{1}{n}\sum_{k=1}^{n} |y[k]|^2}}
$$
(81)

Se calcula representación concatenada de magnitud y fase:

$$
\mathbf{y}_{\text{feat}} = [\text{Re}(\mathbf{y}_{\text{norm}}), \text{Im}(\mathbf{y}_{\text{norm}}), |\mathbf{y}_{\text{norm}}|, \angle\mathbf{y}_{\text{norm}}]
$$
(82)

proporcionando al decodificador múltiples vistas de la señal [128].

#### 2) Extracción de Características Convolucionales

Se aplican múltiples capas convolucionales 1D para extracción jerárquica de características:

$$
\mathbf{f}^{(0)} = \mathbf{y}_{\text{feat}}
$$
(83)

$$
\mathbf{f}^{(i)} = \text{ReLU}(\text{BatchNorm}(\text{Conv1D}(\mathbf{f}^{(i-1)}, \mathbf{W}_i)))
$$
(84)

Se usan dilated convolutions para aumentar campo receptivo sin incrementar parámetros [129]:

$$
(\mathbf{f} * \mathbf{w})_d[n] = \sum_{k=0}^{K-1} f[n - d \cdot k] w[k]
$$
(85)

donde d es el factor de dilation. Capas sucesivas usan d = 1, 2, 4, 8, ... para cubrir dependencias temporales crecientes [130].

#### 3) Módulo de Atención Temporal

Se aplica mecanismo de atención para enfocarse en partes relevantes de la señal:

$$
\mathbf{a} = \text{softmax}(\mathbf{W}_a \mathbf{f} + \mathbf{b}_a)
$$
(86)

$$
\mathbf{f}_{\text{att}} = \mathbf{a} \odot \mathbf{f}
$$
(87)

donde a ∈ [0,1]^n son pesos de atención aprendidos [131].

#### 4) Capas Recurrentes Bidireccionales

Para capturar memoria del canal y dependencias temporales, se usan LSTMs bidireccionales [132]:

$$
\overrightarrow{\mathbf{h}}_t = \text{LSTM}_{\text{fwd}}(\mathbf{f}_t, \overrightarrow{\mathbf{h}}_{t-1})
$$
(88)

$$
\overleftarrow{\mathbf{h}}_t = \text{LSTM}_{\text{bwd}}(\mathbf{f}_t, \overleftarrow{\mathbf{h}}_{t+1})
$$
(89)

$$
\mathbf{h}_t = [\overrightarrow{\mathbf{h}}_t; \overleftarrow{\mathbf{h}}_t]
$$
(90)

La LSTM procesa secuencias mediante gates:

$$
\mathbf{i}_t = \sigma(\mathbf{W}_i [\mathbf{h}_{t-1}, \mathbf{f}_t] + \mathbf{b}_i)
$$
(91)

$$
\mathbf{f}_t = \sigma(\mathbf{W}_f [\mathbf{h}_{t-1}, \mathbf{f}_t] + \mathbf{b}_f)
$$
(92)

$$
\mathbf{o}_t = \sigma(\mathbf{W}_o [\mathbf{h}_{t-1}, \mathbf{f}_t] + \mathbf{b}_o)
$$
(93)

$$
\tilde{\mathbf{c}}_t = \tanh(\mathbf{W}_c [\mathbf{h}_{t-1}, \mathbf{f}_t] + \mathbf{b}_c)
$$
(94)

$$
\mathbf{c}_t = \mathbf{f}_t \odot \mathbf{c}_{t-1} + \mathbf{i}_t \odot \tilde{\mathbf{c}}_t
$$
(95)

$$
\mathbf{h}_t = \mathbf{o}_t \odot \tanh(\mathbf{c}_t)
$$
(96)

donde i_t, f_t, o_t son gates de input, forget y output, y c_t es el estado de celda [133].

#### 5) Clasificación de Mensajes

Las características finales se proyectan a logits para M clases:

$$
\mathbf{z}_{\text{logits}} = \mathbf{W}_{\text{cls}} \mathbf{h}_{\text{final}} + \mathbf{b}_{\text{cls}} \in \mathbb{R}^M
$$
(97)

Las probabilidades se obtienen mediante softmax:

$$
p(m = i | \mathbf{y}) = \frac{\exp(z_i)}{\sum_{j=1}^{M} \exp(z_j)}
$$
(98)

La predicción final es:

$$
\hat{m} = \arg\max_{i=1}^{M} p(m = i | \mathbf{y})
$$
(99)

### E. Complejidad Computacional

El análisis de complejidad es crucial para viabilidad de implementación [134]:

#### 1) Complejidad del Codificador

**Embedding**: O(M · d_emb)
**Transformer Layers**: Cada capa requiere O(n² · d + n · d²) donde d es dimensión de features y n es longitud de secuencia
**Total con L capas**: O(L · (n² · d + n · d²))

#### 2) Complejidad del Decodificador

**Convoluciones**: O(K · d_in · d_out · n) donde K es tamaño de kernel
**LSTM Bidireccional**: O(4 · d_h² · n) donde d_h es dimensión de hidden state
**Total**: O(N_conv · K · d² · n + 4 · d_h² · n)

#### 3) Comparación con Sistemas Convencionales

Para comparación, 5G-NR requiere:
- Codificación LDPC: O(n · log n)
- FFT para OFDM: O(n · log n)
- Ecualización MMSE: O(n · N_rx · N_tx²)

El sistema propuesto tiene mayor complejidad de entrenamiento (offline) pero complejidad de inferencia comparable a sistemas avanzados con ecualización neural [135].


## IV. ALGORITMOS DE ENTRENAMIENTO Y META-APRENDIZAJE

### A. Entrenamiento End-to-End Básico

#### 1) Procedimiento de Entrenamiento Estándar

El algoritmo de entrenamiento básico para el autoencoder comunicacional sigue el siguiente procedimiento iterativo:

**Algoritmo 1: Entrenamiento E2E Básico**

```
Entrada: Conjunto de mensajes {m₁, ..., m_N}, modelo de canal h(·), hiperparámetros
Salida: Parámetros optimizados θ_enc, θ_dec

1. Inicializar θ_enc, θ_dec aleatoriamente (Xavier/He initialization)
2. Para cada época e = 1 hasta E_max:
3.   Para cada minibatch B de tamaño b:
4.     Muestrear mensajes {m_i}_{i=1}^b uniformemente de {1, ..., M}
5.     Generar señales: x_i = f_enc(m_i; θ_enc) para i = 1, ..., b
6.     Simular canal: y_i = h(x_i) + n_i donde n_i ~ CN(0, σ²I)
7.     Decodificar: p_i = f_dec(y_i; θ_dec) (distribución sobre mensajes)
8.     Calcular pérdida: L = -(1/b) Σᵢ log p_i[m_i]
9.     Calcular gradientes: g_enc = ∇_{θ_enc} L, g_dec = ∇_{θ_dec} L
10.    Actualizar parámetros:
         θ_enc ← θ_enc - η_enc · g_enc
         θ_dec ← θ_dec - η_dec · g_dec
11.  Fin para (minibatch)
12.  Si e mod k_eval == 0:
13.    Evaluar BLER en conjunto de validación
14.    Si BLER_val < BLER_best:
15.      Guardar checkpoi

nt θ_enc, θ_dec
16.    Fin si
17.  Fin si
18. Fin para (época)
19. Retornar mejores parámetros guardados
```

#### 2) Optimizadores Avanzados

En lugar de SGD básico, se utilizan optimizadores adaptativos que ajustan tasas de aprendizaje por parámetro [136]:

**Adam (Adaptive Moment Estimation)**: Mantiene momentos de primer y segundo orden [137]:

$$
m_t = \beta_1 m_{t-1} + (1 - \beta_1) g_t
$$
(100)

$$
v_t = \beta_2 v_{t-1} + (1 - \beta_2) g_t^2
$$
(101)

$$
\hat{m}_t = \frac{m_t}{1 - \beta_1^t}, \quad \hat{v}_t = \frac{v_t}{1 - \beta_2^t}
$$
(102)

$$
\theta_{t+1} = \theta_t - \eta \frac{\hat{m}_t}{\sqrt{\hat{v}_t} + \epsilon}
$$
(103)

con hiperparámetros típicos β₁ = 0.9, β₂ = 0.999, ε = 10⁻⁸.

**AdamW**: Variante de Adam con weight decay desacoplado [138]:

$$
\theta_{t+1} = \theta_t - \eta \left( \frac{\hat{m}_t}{\sqrt{\hat{v}_t} + \epsilon} + \lambda \theta_t \right)
$$
(104)

donde λ es coeficiente de weight decay (típicamente 0.01-0.1).

**Lookahead**: Mantiene parámetros lentos k pasos atrás [139]:

$$
\theta_{\text{fast}}^{(t+1)} = \theta_{\text{fast}}^{(t)} - \eta \nabla L(\theta_{\text{fast}}^{(t)})
$$
(105)

$$
\text{Si } t \mod k = 0: \quad \theta_{\text{slow}} = \theta_{\text{slow}} + \alpha(\theta_{\text{fast}} - \theta_{\text{slow}})
$$
(106)

con α = 0.5, k = 5 típicamente, mejorando estabilidad de convergencia.

### B. Curriculum Learning

El entrenamiento directo en condiciones de canal difíciles puede causar inestabilidad. El curriculum learning estructura el entrenamiento en etapas de dificultad creciente [140], [141]:

#### 1) Curriculum basado en SNR

Se incrementa progresivamente la dificultad del canal:

**Algoritmo 2: Curriculum Learning por SNR**

```
Entrada: SNR_inicial, SNR_final, número de etapas K
Salida: Modelo entrenado

1. Dividir rango [SNR_inicial, SNR_final] en K etapas
2. Para k = 1 hasta K:
3.   SNR_k = SNR_inicial + (k/K) · (SNR_final - SNR_inicial)
4.   σ²_k = P / (10^{SNR_k/10})
5.   Entrenar modelo por E_k épocas con ruido n ~ CN(0, σ²_k I)
6.   Si k < K:
7.     Usar modelo de etapa k como inicialización para etapa k+1
8.   Fin si
9. Fin para
10. Retornar modelo final
```

Típicamente se usa progresión: SNR = {20 dB, 15 dB, 10 dB, 5 dB, 0 dB, -5 dB} [142].

#### 2) Curriculum basado en Complejidad de Canal

Se incrementa complejidad del modelo de canal:

**Etapa 1**: Canal AWGN sin imperfecciones
**Etapa 2**: Canal AWGN con ruido de fase leve
**Etapa 3**: Canal Rayleigh estático (baja movilidad)
**Etapa 4**: Canal Rayleigh time-varying (movilidad moderada)
**Etapa 5**: Canal 3GPP con imperfecciones de hardware completas

#### 3) Curriculum de Longitud de Bloque

Se entrena inicialmente con bloques cortos (n pequeño) y se incrementa gradualmente:

$$
n_k = n_{\text{min}} \cdot 2^{k-1}, \quad k = 1, ..., \log_2(n_{\text{max}} / n_{\text{min}})
$$
(107)

Bloques cortos permiten convergencia más rápida; longitud final logra desempeño óptimo [143].

### C. Data Augmentation para Comunicaciones

El data augmentation genera variaciones de muestras de entrenamiento para mejorar robustez y generalización [144]:

#### 1) Augmentation de Fase y Frecuencia

**Rotación Aleatoria de Fase**: Simula incertidumbre de fase de portadora:

$$
\tilde{\mathbf{y}} = \mathbf{y} \cdot e^{j\phi}, \quad \phi \sim \mathcal{U}(0, 2\pi)
$$
(108)

**Desplazamiento de Frecuencia (CFO)**: Simula offset de frecuencia de portadora:

$$
\tilde{y}[n] = y[n] \cdot e^{j2\pi\Delta f n T_s}, \quad \Delta f \sim \mathcal{N}(0, \sigma_{\text{CFO}}^2)
$$
(109)

#### 2) Augmentation de Amplitud

**Scaling Aleatorio**: Simula variación de ganancia del canal:

$$
\tilde{\mathbf{y}} = \alpha \mathbf{y}, \quad \alpha \sim \text{LogNormal}(\mu_\alpha, \sigma_\alpha^2)
$$
(110)

**Clipping**: Simula saturación de receptor:

$$
\tilde{y}[n] = \text{sign}(y[n]) \cdot \min(|y[n]|, A_{\text{clip}})
$$
(111)

#### 3) Augmentation Temporal

**Time Warping**: Simula variaciones de timing:

$$
\tilde{y}[n] = y[n + \tau[n]], \quad \tau[n] \sim \mathcal{U}(-\tau_{\max}, \tau_{\max})
$$
(112)

**Dropout Temporal**: Simula pérdidas de símbolos:

$$
\tilde{y}[n] = \begin{cases} y[n] & \text{con probabilidad } 1-p \\ 0 & \text{con probabilidad } p \end{cases}
$$
(113)

### D. Regularización y Estabilización

#### 1) Regularización de Norma de Pesos

Se penaliza norma de parámetros para evitar sobreajuste:

$$
\mathcal{L}_{\text{reg}} = \mathcal{L}_{\text{CE}} + \lambda_1 \|\theta_{\text{enc}}\|_2^2 + \lambda_2 \|\theta_{\text{dec}}\|_2^2
$$
(114)

Típicamente λ₁, λ₂ ∈ [10⁻⁵, 10⁻³] [145].

#### 2) Regularización Espectral

Se penaliza componentes de alta frecuencia en señales transmitidas:

$$
\mathcal{L}_{\text{spectral}} = \lambda_s \sum_{k > k_{\text{BW}}} |\mathcal{F}\{\mathbf{x}\}[k]|^2
$$
(115)

donde k_BW corresponde al ancho de banda deseado. Esto promueve señales band-limited [146].

#### 3) Gradient Clipping

Para estabilizar entrenamiento, se limita magnitud de gradientes:

$$
\mathbf{g}_{\text{clipped}} = \begin{cases}
\mathbf{g} & \text{si } \|\mathbf{g}\| \leq \tau \\
\tau \cdot \frac{\mathbf{g}}{\|\mathbf{g}\|} & \text{si } \|\mathbf{g}\| > \tau
\end{cases}
$$
(116)

con τ = 1.0 típicamente [147].

#### 4) Exponential Moving Average de Parámetros

Se mantiene promedio móvil de parámetros que típicamente generaliza mejor:

$$
\tilde{\theta}_t = \gamma \tilde{\theta}_{t-1} + (1 - \gamma) \theta_t
$$
(117)

con γ = 0.999, y se usa θ̃ para inferencia [148].

### E. Meta-Aprendizaje para Adaptación Rápida

Los sistemas de comunicación deben adaptarse rápidamente a condiciones de canal cambiantes. El meta-aprendizaje entrena modelos para adaptación eficiente con pocas muestras [149], [150].

#### 1) Model-Agnostic Meta-Learning (MAML)

MAML aprende inicializaciones de parámetros que permiten adaptación rápida [151]:

**Formulación**: Sea T = {T₁, ..., T_K} un conjunto de tareas (cada tarea = condición de canal específica). Para cada tarea T_i:

- Conjunto de soporte S_i = {(x_j, y_j)}_{j=1}^N (pocas muestras para adaptar)
- Conjunto de query Q_i = {(x_k, y_k)}_{k=1}^M (muestras para evaluar adaptación)

**Algoritmo 3: MAML para Adaptación de Canal**

```
Entrada: Distribución de tareas p(T), hiperparámetros α (inner LR), β (outer LR)
Salida: Parámetros meta-inicializados θ

1. Inicializar θ aleatoriamente
2. Para cada iteración de meta-entrenamiento:
3.   Muestrear batch de tareas {T_i}_{i=1}^B ~ p(T)
4.   Para cada tarea T_i:
5.     Muestrear conjunto de soporte S_i y query Q_i
6.     Inicializar θ'_i = θ
7.     Calcular pérdida de soporte: L_S = (1/|S_i|) Σ_{(x,y)∈S_i} ℓ(f(x;θ'_i), y)
8.     Actualizar con gradiente: θ'_i = θ'_i - α ∇_{θ'_i} L_S
9.     Calcular pérdida de query: L_Q^i = (1/|Q_i|) Σ_{(x,y)∈Q_i} ℓ(f(x;θ'_i), y)
10.  Fin para
11.  Calcular meta-pérdida: L_meta = (1/B) Σᵢ L_Q^i
12.  Actualizar meta-parámetros: θ = θ - β ∇_θ L_meta
13. Fin para
14. Retornar θ
```

El gradiente meta se calcula como:

$$
\nabla_\theta \mathcal{L}_{\text{meta}} = \frac{1}{B} \sum_{i=1}^{B} \nabla_\theta \mathcal{L}_Q^i(\theta'_i)
$$
(118)

donde θ'_i depende de θ mediante la actualización inner loop:

$$
\theta'_i = \theta - \alpha \nabla_\theta \mathcal{L}_S^i(\theta)
$$
(119)

Por regla de la cadena:

$$
\nabla_\theta \mathcal{L}_Q^i(\theta'_i) = \nabla_{\theta'_i} \mathcal{L}_Q^i \cdot \nabla_\theta \theta'_i
$$
(120)

$$
= \nabla_{\theta'_i} \mathcal{L}_Q^i \cdot \left( \mathbf{I} - \alpha \nabla_\theta^2 \mathcal{L}_S^i \right)
$$
(121)

El término ∇²_θ L_S^i (Hessian) puede aproximarse con computaciones de primer orden [152].

#### 2) Definición de Tareas para Comunicaciones

Cada tarea corresponde a una condición de canal específica. Se definen distribuciones de tareas:

**Por SNR**: T_i ~ p(SNR) donde SNR ∈ [-10 dB, 30 dB]
**Por Perfil de Canal**: T_i ∈ {TDL-A, TDL-B, TDL-C, TDL-D, TDL-E}
**Por Velocidad Doppler**: T_i ~ p(v) donde v ∈ [0, 500] km/h
**Por Imperfecciones HW**: T_i parametrizado por (σ_PN, IIP3, I/Q imbalance)

#### 3) Adaptación en Línea

Una vez meta-entrenado, el sistema se adapta a nuevo canal con K-shot learning:

**Algoritmo 4: Adaptación en Línea**

```
Entrada: Modelo meta-entrenado con parámetros θ, K muestras de nuevo canal
Salida: Parámetros adaptados θ*

1. Observar K pares (x_j, y_j) del nuevo canal
2. Inicializar θ* = θ (meta-inicialización)
3. Para t = 1 hasta T_adapt:
4.   Calcular pérdida: L = (1/K) Σⱼ ℓ(f(y_j; θ*), x_j)
5.   Actualizar: θ* = θ* - α_adapt ∇_{θ*} L
6. Fin para
7. Retornar θ*
```

Con K = 10-50 muestras y T_adapt = 5-20 pasos, se logra adaptación efectiva [153].

### F. Entrenamiento Multi-Objetivo

El sistema debe optimizar simultáneamente múltiples objetivos [154]:

#### 1) Formulación Multi-Objetivo

Se definen objetivos:

- O₁: Minimizar BLER
- O₂: Minimizar PAPR
- O₃: Minimizar ocupación espectral (OOBE)
- O₄: Minimizar latencia de procesamiento

La función de pérdida combinada es:

$$
\mathcal{L}_{\text{total}} = \sum_{i=1}^{4} w_i \mathcal{L}_i
$$
(122)

donde w_i son pesos de importancia. Sin embargo, seleccionar pesos fijos es difícil.

#### 2) Dynamic Weighting

Se ajustan pesos dinámicamente durante entrenamiento [155]:

$$
w_i^{(t)} = \frac{\exp(\gamma \cdot r_i^{(t-1)})}{\sum_{j=1}^{4} \exp(\gamma \cdot r_j^{(t-1)})}
$$
(123)

donde r_i^(t) = L_i^(t) / L_i^(0) es la reducción relativa de pérdida i, y γ controla sensibilidad.

#### 3) Pareto Optimization

Se busca conjunto de soluciones Pareto-óptimas donde ningún objetivo puede mejorar sin degradar otro [156]:

**Algoritmo 5: Multi-Objective Gradient Descent**

```
Entrada: Objetivos {L₁, ..., L_n}, inicialización θ
Salida: Conjunto de soluciones Pareto-óptimas

1. Para cada iteración:
2.   Calcular gradientes: g_i = ∇_θ L_i para i = 1, ..., n
3.   Si gradientes están alineados (todos reducen todos objetivos):
4.     Usar gradiente promedio: g = (1/n) Σᵢ g_i
5.   Si no:
6.     Calcular dirección de compromiso resolviendo:
        min_d ||d - g_i||² tal que ⟨d, g_i⟩ ≤ 0 ∀i
7.     Usar d como dirección de actualización
8.   Fin si
9.   Actualizar: θ = θ - η · d
10. Fin para
```

Este enfoque garantiza no degradar ningún objetivo significativamente [157].

### G. Transfer Learning y Fine-Tuning

Para acelerar entrenamiento en nuevos escenarios, se usa transfer learning [158]:

#### 1) Pre-Entrenamiento en Canal Genérico

Se pre-entrena en mezcla de múltiples condiciones de canal:

$$
\mathcal{L}_{\text{pre}} = \mathbb{E}_{T \sim p(T)} \left[ \mathcal{L}(T; \theta) \right]
$$
(124)

donde p(T) es distribución sobre tipos de canal. Esto aprende representaciones generales.

#### 2) Fine-Tuning Específico

Se ajusta modelo pre-entrenado para escenario específico con tasa de aprendizaje reducida:

$$
\theta_{\text{fine}} = \theta_{\text{pre}} - \eta_{\text{fine}} \nabla \mathcal{L}_{\text{specific}}(\theta_{\text{pre}})
$$
(125)

con η_fine = 0.1 · η_pre típicamente.

#### 3) Freezing de Capas

Se congelan capas tempranas (extracción de características de bajo nivel) y solo se entrenan capas superiores:

```
Para cada capa l:
  Si l ≤ L_freeze:
    Congelar parámetros θ_l (sin gradientes)
  Si no:
    Entrenar θ_l normalmente
  Fin si
Fin para
```

Esto reduce sobreajuste cuando datos de fine-tuning son limitados [159].

