# Inteligencia Artificial Nativa en el Nivel Físico de Redes 6G: Fundamentos, Arquitecturas y Perspectivas

---

## Resumen

Las redes de sexta generación (6G) representan un paradigma disruptivo en las comunicaciones inalámbricas, donde la inteligencia artificial (IA) no se integra como una funcionalidad complementaria, sino que se establece como un componente nativo y fundamental de la arquitectura de red. En el nivel físico, esta integración nativa de IA trasciende los enfoques tradicionales basados en modelos matemáticos determinísticos, permitiendo la adaptación autónoma y el aprendizaje continuo de las características del canal, la optimización dinámica de recursos espectrales y energéticos, y la implementación de esquemas de modulación, codificación y detección adaptativos en tiempo real. Este artículo presenta una revisión exhaustiva de los fundamentos teóricos, arquitecturas emergentes y desafíos técnicos asociados con la implementación de IA nativa en el nivel físico de 6G, incluyendo el análisis de receptores neuronales end-to-end, esquemas de autocodificadores para comunicaciones semánticas, técnicas de estimación y ecualización de canal basadas en aprendizaje profundo, y mecanismos de optimización de forma de onda mediante redes neuronales. Se examinan las implicaciones de rendimiento, complejidad computacional, consumo energético y latencia, así como los requisitos de entrenamiento, generalización y robustez ante condiciones adversas del canal. El trabajo establece un marco conceptual integral que conecta los avances en aprendizaje automático con los requisitos específicos del nivel físico en sistemas 6G, identificando oportunidades de investigación y trayectorias tecnológicas hacia la implementación práctica de sistemas de comunicación verdaderamente inteligentes y autónomos.

**Palabras clave:** Inteligencia artificial nativa, redes 6G, nivel físico, aprendizaje profundo, receptores neuronales, autocodificadores, comunicaciones semánticas, optimización de canal, arquitecturas end-to-end, modulación adaptativa

---

## I. INTRODUCCIÓN

### A. Contexto y Motivación

La evolución de los sistemas de comunicaciones móviles ha seguido históricamente una trayectoria predecible de mejoras incrementales en velocidad de transmisión, latencia, eficiencia espectral y cobertura. Sin embargo, la transición hacia las redes de sexta generación (6G) representa un cambio paradigmático fundamentalmente diferente a las generaciones anteriores, donde la inteligencia artificial no se concibe como una tecnología habilitadora adicional, sino como un elemento constitutivo e indisociable de la arquitectura de red [1]. Esta transformación conceptual es especialmente relevante en el nivel físico (PHY), donde los métodos tradicionales basados en modelos matemáticos analíticos y procesamiento de señales diseñado manualmente enfrentan limitaciones crecientes ante la complejidad, heterogeneidad y dinamismo de los escenarios de comunicación previstos para 6G.

Los sistemas de quinta generación (5G) han demostrado las capacidades del aprendizaje automático (ML) aplicado a problemas específicos del nivel físico, tales como la estimación de canal, la predicción de tráfico, la gestión de interferencias y la optimización de recursos radio [2]. No obstante, estas aplicaciones mantienen una arquitectura fundamentalmente separada entre los componentes de procesamiento de señales tradicionales y los módulos de ML, que típicamente operan como optimizadores externos o predictores auxiliares. En contraste, la IA nativa en 6G propone una integración orgánica donde las funciones del nivel físico—modulación, codificación de canal, conformación de forma de onda, estimación de canal, ecualización, detección y decodificación—son reimplementadas mediante arquitecturas de aprendizaje profundo entrenadas de extremo a extremo (end-to-end) [3].

La motivación principal para esta transformación radical surge de múltiples factores convergentes. Primero, los escenarios de uso de 6G—incluyendo comunicaciones holográficas, gemelos digitales distribuidos, realidad extendida (XR) inmersiva, internet táctil de ultra-baja latencia, y conectividad masiva para internet de las cosas (IoT) a escala de billones de dispositivos—imponen requisitos de rendimiento que exceden los límites teóricos alcanzables con técnicas convencionales. Segundo, el espectro electromagnético disponible para 6G se extiende hacia bandas de ondas milimétricas (mmWave) superiores a 100 GHz, terahercios (THz) y comunicaciones ópticas inalámbricas, donde los modelos de canal tradicionales resultan inexactos o computacionalmente intratables. Tercero, la heterogeneidad extrema de dispositivos, desde sensores de ultra-bajo consumo hasta estaciones base masivas con arquitecturas de antenas inteligentes reconfigurables (RIS), demanda capacidades de adaptación y optimización que trascienden los algoritmos determinísticos [4].

La aplicación de IA nativa en el nivel físico no se limita a mejorar el rendimiento en condiciones nominales, sino que persigue objetivos más ambiciosos: la capacidad de operar eficientemente en escenarios para los cuales no existe modelo analítico preciso, la adaptación autónoma a condiciones de canal no estacionarias y altamente dinámicas, la optimización conjunta de múltiples objetivos conflictivos (velocidad, latencia, confiabilidad, consumo energético, seguridad), y la implementación de comunicaciones semánticas orientadas a la transmisión de significado en lugar de bits [5]. Estas capacidades emergentes posicionan a la IA nativa como el habilitador fundamental para alcanzar las ambiciosas metas de rendimiento de 6G: velocidades de transmisión de terabits por segundo, latencias inferiores a 100 microsegundos, confiabilidad del 99.99999%, eficiencia energética 100 veces superior a 5G, y densidad de conexión de 10^7 dispositivos por kilómetro cuadrado.

### B. Estado del Arte y Evolución Conceptual

La integración de técnicas de aprendizaje automático en el nivel físico de sistemas de comunicaciones tiene raíces que se remontan a las redes neuronales aplicadas a ecualización adaptativa y detección en los años 1990. Sin embargo, el advenimiento del aprendizaje profundo (deep learning) a partir de 2012, caracterizado por arquitecturas de redes neuronales con múltiples capas ocultas, funciones de activación no lineales sofisticadas, y algoritmos de entrenamiento eficientes basados en retropropagación estocástica, ha revolucionado las posibilidades de aplicación en comunicaciones [6].

El concepto seminal de autocodificadores para sistemas de comunicación, introducido formalmente en [7], establece el marco teórico fundamental para la IA nativa en el nivel físico. En esta aproximación, el transmisor se modela como una red neuronal codificadora que mapea mensajes de información a señales en el espacio de símbolos complejos, el canal se representa mediante un modelo diferenciable (determinístico, estocástico o basado en datos reales), y el receptor se implementa como una red neuronal decodificadora que recupera los mensajes transmitidos. El entrenamiento end-to-end de este sistema mediante descenso de gradiente optimiza conjuntamente las funciones de modulación, codificación y decodificación para maximizar la tasa de información mutua o minimizar la probabilidad de error, sin imponer restricciones estructurales basadas en esquemas convencionales predefinidos.

Los avances recientes han extendido esta arquitectura básica en múltiples direcciones. Los receptores neuronales basados en redes neuronales recurrentes (RNN) y redes de memoria a largo y corto plazo (LSTM) han demostrado capacidad superior para la detección de señales en canales con desvanecimiento selectivo en frecuencia y memoria temporal [8]. Las redes neuronales convolucionales (CNN) se han aplicado exitosamente a la estimación y seguimiento de canal en sistemas MIMO masivos, donde la estructura espacial de las matrices de canal puede explotarse mediante operaciones de convolución. Las arquitecturas transformer, originalmente desarrolladas para procesamiento de lenguaje natural, están siendo adaptadas para modelar dependencias temporales de largo plazo en secuencias de símbolos y predecir condiciones futuras del canal con precisión superior a métodos clásicos como filtros de Kalman.

La evolución conceptual hacia la IA nativa en 6G se caracteriza por tres transiciones fundamentales. Primera, el cambio de optimización basada en modelos (model-based) a optimización basada en datos (data-driven), donde las suposiciones analíticas sobre distribuciones de canal, estadísticas de ruido e interferencia se reemplazan por aprendizaje directo desde observaciones empíricas. Segunda, la transición de diseño separado por componentes a optimización conjunta end-to-end, eliminando las interfaces y abstracciones tradicionales entre capas de procesamiento que pueden resultar subóptimas globalmente. Tercera, la evolución de sistemas estáticos diseñados offline a sistemas adaptativos con capacidad de aprendizaje continuo online, que se ajustan dinámicamente a variaciones del entorno operativo [9].

Un área particularmente prometedora es la de comunicaciones semánticas, donde la IA nativa permite implementar sistemas que transmiten directamente la información relevante o el significado de los datos, en lugar de reproducir fielmente cada bit de la fuente. Esto se logra mediante codificadores neuronales que extraen representaciones compactas de alto nivel del contenido (embeddings semánticos) y decodificadores que reconstruyen la información semánticamente equivalente en el receptor, potencialmente con órdenes de magnitud de reducción en ancho de banda requerido [10].

### C. Objetivos y Contribuciones del Artículo

El presente artículo tiene como objetivo principal proporcionar una revisión integral, sistemática y crítica del estado del arte en inteligencia artificial nativa aplicada al nivel físico de redes 6G, estableciendo un marco conceptual unificado que articule los fundamentos teóricos, las arquitecturas prácticas, los desafíos técnicos y las perspectivas futuras de investigación en este campo emergente.

Las contribuciones específicas de este trabajo se estructuran en las siguientes dimensiones:

**Fundamentos Teóricos:** Se presenta un análisis riguroso de los principios matemáticos y teoría de la información que sustentan los sistemas de comunicación basados en IA nativa, incluyendo la formulación del problema de optimización end-to-end, las condiciones de diferenciabilidad del canal, las garantías de convergencia durante el entrenamiento, y los límites teóricos de rendimiento comparados con los límites de Shannon clásicos. Se examinan las relaciones entre capacidad de canal, complejidad del modelo neuronal, tamaño del conjunto de entrenamiento y desempeño de generalización.

**Arquitecturas y Diseños:** Se realiza una taxonomía exhaustiva de las arquitecturas de redes neuronales aplicadas al nivel físico, diferenciando entre receptores neuronales, autocodificadores de comunicación, estimadores y ecualizadores de canal basados en deep learning, optimizadores de forma de onda, y sistemas híbridos que combinan componentes tradicionales con módulos de IA. Para cada arquitectura se analizan las topologías de red más efectivas, las funciones de pérdida apropiadas, los métodos de regularización, y las estrategias de entrenamiento offline y online.

**Desafíos de Implementación:** Se identifican y analizan críticamente los obstáculos técnicos para la implementación práctica de IA nativa en el nivel físico de 6G, incluyendo: (i) la complejidad computacional y latencia de inferencia en dispositivos con recursos limitados, (ii) los requisitos de energía para el procesamiento neuronal en terminales móviles, (iii) las dificultades de entrenamiento con modelos de canal imperfectos o desajuste entre entrenamiento y despliegue, (iv) la falta de interpretabilidad y verificabilidad formal de soluciones basadas en cajas negras neuronales, y (v) las vulnerabilidades de seguridad ante ataques adversarios diseñados para engañar a los modelos de ML.

**Evaluación de Rendimiento:** Se sintetizan los resultados de rendimiento reportados en la literatura para diferentes técnicas de IA nativa, estableciendo comparaciones rigurosas con métodos convencionales bajo métricas estandarizadas: tasa de error de bit (BER), tasa de error de bloque (BLER), eficiencia espectral, eficiencia energética, latencia, robustez ante variaciones de canal, y capacidad de generalización a escenarios no vistos durante el entrenamiento.

**Perspectivas Futuras:** Se delinean las trayectorias tecnológicas y direcciones de investigación más prometedoras para el avance del campo, incluyendo el desarrollo de arquitecturas neuromórficas especializadas para procesamiento de señales, la integración de IA nativa con superficies inteligentes reconfigurables (RIS), la co-optimización de hardware y algoritmos (hardware-algorithm co-design), el aprendizaje federado para entrenamiento distribuido preservando privacidad, y la estandarización de interfaces y protocolos para sistemas de comunicación nativamente inteligentes.

Este trabajo se distingue de revisiones previas por su enfoque holístico que conecta rigurosamente los fundamentos teóricos con las implementaciones prácticas, su cobertura exhaustiva de todas las funciones del nivel físico susceptibles de implementación mediante IA nativa, y su perspectiva crítica que balancea el entusiasmo por las capacidades emergentes con el reconocimiento realista de limitaciones, desafíos pendientes y áreas que requieren investigación adicional.

### D. Organización del Artículo

El resto de este artículo se estructura de la siguiente manera:

La Sección II presenta los fundamentos teóricos de la inteligencia artificial nativa en el nivel físico, incluyendo la formulación matemática del problema de comunicación como optimización end-to-end, la teoría de aprendizaje profundo aplicada a procesamiento de señales, y los límites teóricos de información en sistemas basados en IA. Se establecen las conexiones con la teoría clásica de comunicaciones y se identifican las extensiones conceptuales necesarias para el nuevo paradigma.

La Sección III desarrolla una taxonomía detallada de arquitecturas de IA nativa para el nivel físico, organizadas por función: receptores neuronales y detectores basados en deep learning, autocodificadores para modulación y codificación de canal, estimadores y ecualizadores de canal mediante redes neuronales, optimización de forma de onda y gestión de recursos espectrales, y sistemas híbridos que combinan componentes convencionales con módulos de IA. Para cada categoría se describen las arquitecturas de red más relevantes, sus principios de operación, y sus características de rendimiento.

La Sección IV analiza los desafíos técnicos y limitaciones prácticas de la implementación de IA nativa en el nivel físico de 6G, cubriendo aspectos de complejidad computacional y latencia, consumo energético en dispositivos móviles, requisitos y metodologías de entrenamiento, generalización y robustez ante desajuste de canal, interpretabilidad y verificación formal, y consideraciones de seguridad ante ataques adversarios.

La Sección V presenta una evaluación comparativa de rendimiento de técnicas de IA nativa frente a métodos convencionales, sintetizando resultados de la literatura bajo escenarios estandarizados y métricas consistentes. Se incluyen análisis de eficiencia espectral, eficiencia energética, latencia, confiabilidad, y capacidad de adaptación.

La Sección VI discute las perspectivas futuras y direcciones de investigación, incluyendo tendencias tecnológicas emergentes como arquitecturas neuromórficas, integración con RIS y comunicaciones THz, aprendizaje federado y distribuido, co-diseño de hardware y software, y los caminos hacia la estandarización y adopción industrial de IA nativa en 6G.

Finalmente, la Sección VII concluye el artículo sintetizando los principales hallazgos, reiterando las contribuciones fundamentales, y estableciendo una visión prospectiva del rol transformador de la inteligencia artificial nativa en la definición del nivel físico de las redes de sexta generación.

---

## II. FUNDAMENTOS TEÓRICOS DE IA NATIVA EN EL NIVEL FÍSICO

La implementación efectiva de inteligencia artificial nativa en el nivel físico de sistemas de comunicación 6G requiere una fundamentación matemática rigurosa que conecte la teoría clásica de comunicaciones con los principios del aprendizaje profundo. Esta sección establece el marco teórico formal que sustenta el diseño, análisis y optimización de sistemas de comunicación basados en redes neuronales end-to-end. Se presenta el modelo matemático del sistema de comunicación, se derivan los límites fundamentales de información, se desarrollan los fundamentos del aprendizaje profundo aplicado al nivel físico, se formula el problema de optimización global, y se analizan las condiciones de convergencia y garantías teóricas de rendimiento.

### A. Modelo del Sistema de Comunicación

#### 1) Formulación Básica del Sistema de Comunicación Digital

Consideremos un sistema de comunicación digital que transmite información desde una fuente a un destino a través de un canal ruidoso. La formulación clásica se basa en la separación funcional entre codificación de fuente, codificación de canal, modulación digital y procesamiento en el receptor. En el paradigma de IA nativa, esta arquitectura modular se reemplaza por una función de mapeo end-to-end implementada mediante redes neuronales.

Sea $\mathcal{M} = \{1, 2, ..., M\}$ el conjunto de mensajes posibles que pueden ser transmitidos, donde $M = 2^k$ y $k$ representa el número de bits de información por mensaje. En el enfoque tradicional, el transmisor implementa una función de codificación $f_{\text{TX}}: \mathcal{M} \rightarrow \mathbb{C}^n$ que mapea cada mensaje $m \in \mathcal{M}$ a un vector de $n$ símbolos complejos:

$$\mathbf{x} = f_{\text{TX}}(m) = [x_1, x_2, ..., x_n]^T \in \mathbb{C}^n$$

donde cada símbolo complejo $x_i = x_i^{\text{I}} + j x_i^{\text{Q}}$ tiene componentes en fase (I) y en cuadratura (Q). La restricción de potencia promedio se expresa como:

$$\mathbb{E}[\|\mathbf{x}\|^2] = \mathbb{E}\left[\sum_{i=1}^{n}|x_i|^2\right] \leq nP$$

donde $P$ es la potencia promedio por símbolo transmitido. Esta restricción puede reformularse mediante una normalización que garantiza:

$$\|\mathbf{x}\|^2 = \sum_{i=1}^{n}|x_i|^2 = n$$

En el paradigma de IA nativa, el transmisor se implementa como una red neuronal profunda $f_{\text{TX}}(\cdot; \boldsymbol{\theta}_{\text{TX}})$ parametrizada por los pesos y sesgos $\boldsymbol{\theta}_{\text{TX}}$. La representación explícita de una red neuronal feedforward con $L$ capas ocultas es:

$$\mathbf{h}^{(0)} = \text{one-hot}(m) \in \{0,1\}^M$$

$$\mathbf{h}^{(l)} = \sigma\left(\mathbf{W}^{(l)}\mathbf{h}^{(l-1)} + \mathbf{b}^{(l)}\right), \quad l = 1, 2, ..., L$$

$$\mathbf{x} = g\left(\mathbf{W}^{(L+1)}\mathbf{h}^{(L)} + \mathbf{b}^{(L+1)}\right)$$

donde $\mathbf{W}^{(l)} \in \mathbb{R}^{n_l \times n_{l-1}}$ y $\mathbf{b}^{(l)} \in \mathbb{R}^{n_l}$ son las matrices de pesos y vectores de sesgo de la capa $l$, $\sigma(\cdot)$ es la función de activación no lineal (típicamente ReLU: $\sigma(z) = \max(0, z)$ o ELU: $\sigma(z) = z$ si $z > 0$, $\alpha(e^z - 1)$ si $z \leq 0$), y $g(\cdot)$ es una función de normalización que garantiza la restricción de potencia.

La función de normalización más común es la normalización de energía por lotes (batch energy normalization):

$$g(\mathbf{z}) = \sqrt{n} \cdot \frac{\mathbf{z}}{\|\mathbf{z}\|}$$

que garantiza que $\|\mathbf{x}\|^2 = n$ para cualquier salida de la red antes de normalizar.

#### 2) Modelo del Canal de Comunicación

El canal de comunicación introduce distorsión, ruido e interferencia durante la propagación de la señal transmitida. En el contexto de IA nativa, el modelo del canal debe ser diferenciable para permitir el entrenamiento end-to-end mediante retropropagación del gradiente.

Para un canal AWGN (Additive White Gaussian Noise) estándar, la señal recibida se modela como:

$$\mathbf{y} = \mathbf{x} + \mathbf{n}$$

donde $\mathbf{n} \sim \mathcal{CN}(\mathbf{0}, \sigma_n^2\mathbf{I}_n)$ es ruido complejo gaussiano con varianza $\sigma_n^2$ por dimensión. La relación señal-ruido (SNR) se define como:

$$\text{SNR} = \frac{P}{\sigma_n^2} = \frac{\mathbb{E}[\|\mathbf{x}\|^2]/n}{\sigma_n^2}$$

En decibelios: $\text{SNR}_{\text{dB}} = 10\log_{10}(\text{SNR})$.

Para canales con desvanecimiento (fading), el modelo se extiende a:

$$\mathbf{y} = \mathbf{H}\mathbf{x} + \mathbf{n}$$

donde $\mathbf{H} \in \mathbb{C}^{n \times n}$ es la matriz de canal que caracteriza los efectos de propagación multitrayecto, desvanecimiento selectivo en frecuencia y correlación espacial en sistemas MIMO. La matriz de canal se puede descomponer según el modelo de trayectorias discretas:

$$\mathbf{H} = \sum_{p=1}^{P} \alpha_p e^{j\phi_p} \mathbf{a}_{\text{RX}}(\theta_p, \varphi_p) \mathbf{a}_{\text{TX}}^H(\theta_p, \varphi_p)$$

donde $P$ es el número de trayectorias de propagación, $\alpha_p$ y $\phi_p$ son la amplitud y fase del $p$-ésimo camino, y $\mathbf{a}_{\text{RX}}, \mathbf{a}_{\text{TX}}$ son los vectores de respuesta de los arreglos de antenas en recepción y transmisión.

Para canales con memoria temporal, se utiliza el modelo de convolución discreta:

$$y[k] = \sum_{l=0}^{L-1} h[l] x[k-l] + n[k]$$

donde $h[l]$ es la respuesta al impulso del canal de longitud $L$ (número de taps), y $k$ es el índice temporal discreto.

#### 3) Arquitectura del Receptor Neuronal

El receptor implementa una función de decodificación $f_{\text{RX}}: \mathbb{C}^n \rightarrow \mathcal{M}$ que mapea la señal recibida $\mathbf{y}$ a una estimación del mensaje transmitido $\hat{m}$. En IA nativa, esta función se implementa mediante una red neuronal $f_{\text{RX}}(\cdot; \boldsymbol{\theta}_{\text{RX}})$:

$$\hat{m} = f_{\text{RX}}(\mathbf{y}; \boldsymbol{\theta}_{\text{RX}}) = \arg\max_{m \in \mathcal{M}} p(m|\mathbf{y}; \boldsymbol{\theta}_{\text{RX}})$$

La implementación explícita utiliza una arquitectura feedforward o recurrente:

$$\mathbf{z}^{(0)} = [\text{Re}(\mathbf{y})^T, \text{Im}(\mathbf{y})^T]^T \in \mathbb{R}^{2n}$$

$$\mathbf{z}^{(l)} = \sigma\left(\mathbf{V}^{(l)}\mathbf{z}^{(l-1)} + \mathbf{c}^{(l)}\right), \quad l = 1, 2, ..., L'$$

$$\mathbf{p} = \text{softmax}\left(\mathbf{V}^{(L'+1)}\mathbf{z}^{(L')} + \mathbf{c}^{(L'+1)}\right) \in [0,1]^M$$

donde $\mathbf{V}^{(l)}$ y $\mathbf{c}^{(l)}$ son los parámetros del receptor, y la función softmax se define como:

$$\text{softmax}(\mathbf{u})_i = \frac{e^{u_i}}{\sum_{j=1}^{M}e^{u_j}}$$

El vector de salida $\mathbf{p}$ representa la distribución de probabilidad estimada sobre los mensajes posibles, cumpliendo $\sum_{i=1}^M p_i = 1$ y $p_i \geq 0$ para todo $i$.

La decisión final se toma mediante:

$$\hat{m} = \arg\max_{i \in \{1,...,M\}} p_i$$

### B. Teoría de la Información y Límites Fundamentales

#### 1) Capacidad de Shannon y Límites Clásicos

La capacidad del canal define el límite superior de la tasa de transmisión confiable de información. Para un canal AWGN con entrada restringida en potencia, la capacidad de Shannon se expresa como:

$$C = \max_{p(\mathbf{x}): \mathbb{E}[\|\mathbf{x}\|^2] \leq nP} I(\mathbf{X}; \mathbf{Y})$$

donde $I(\mathbf{X}; \mathbf{Y})$ es la información mutua entre la entrada y salida del canal. Para un canal AWGN escalar real, la capacidad se alcanza con entrada gaussiana:

$$C_{\text{AWGN}} = \frac{1}{2}\log_2\left(1 + \frac{P}{\sigma_n^2}\right) \text{ bits por uso del canal}$$

Para símbolos complejos, la capacidad se duplica:

$$C_{\text{AWGN}}^{\mathbb{C}} = \log_2\left(1 + \frac{P}{\sigma_n^2}\right) = \log_2(1 + \text{SNR})$$

La información mutua para distribuciones arbitrarias se define como:

$$I(\mathbf{X}; \mathbf{Y}) = h(\mathbf{Y}) - h(\mathbf{Y}|\mathbf{X})$$

donde $h(\mathbf{Y}) = -\int p(\mathbf{y})\log_2 p(\mathbf{y}) d\mathbf{y}$ es la entropía diferencial de la salida y $h(\mathbf{Y}|\mathbf{X}) = -\iint p(\mathbf{x}, \mathbf{y})\log_2 p(\mathbf{y}|\mathbf{x}) d\mathbf{x}d\mathbf{y}$ es la entropía condicional.

Para el canal AWGN, donde $p(\mathbf{y}|\mathbf{x}) = \mathcal{CN}(\mathbf{x}, \sigma_n^2\mathbf{I})$, la entropía condicional es constante:

$$h(\mathbf{Y}|\mathbf{X}) = n\log_2(2\pi e \sigma_n^2)$$

Por lo tanto, maximizar la información mutua equivale a maximizar la entropía de la salida $h(\mathbf{Y})$.

Para canales con desvanecimiento de Rayleigh, donde $h \sim \mathcal{CN}(0, 1)$, la capacidad ergódica (promediada sobre realizaciones del desvanecimiento) es:

$$C_{\text{Rayleigh}} = \mathbb{E}_h\left[\log_2(1 + |h|^2\text{SNR})\right] = \int_0^{\infty} \log_2(1 + \gamma \cdot \text{SNR}) e^{-\gamma} d\gamma$$

que no tiene solución cerrada pero puede evaluarse numéricamente mediante la función exponencial integral.

#### 2) Información Mutua en Sistemas Basados en IA Nativa

En sistemas basados en autocodificadores neuronales, la información mutua empírica entre mensajes y señales recibidas se puede estimar mediante:

$$\hat{I}(\mathbf{X}; \mathbf{Y}) = H(M) - H(M|\mathbf{Y})$$

donde $H(M) = \log_2 M$ es la entropía del mensaje uniforme, y la entropía condicional se aproxima mediante muestreo Monte Carlo:

$$H(M|\mathbf{Y}) \approx -\frac{1}{N}\sum_{i=1}^{N}\log_2 p(m_i|\mathbf{y}_i; \boldsymbol{\theta}_{\text{RX}})$$

sobre un conjunto de $N$ muestras de entrenamiento $(m_i, \mathbf{y}_i)$.

La tasa de información alcanzable mediante el autocodificador neuronal está limitada por:

$$R = \frac{k}{n} = \frac{\log_2 M}{n} \leq \frac{I(\mathbf{X}; \mathbf{Y})}{n}$$

donde la igualdad se alcanza cuando la probabilidad de error de mensaje $P_e = P(\hat{m} \neq m) \rightarrow 0$ conforme $n \rightarrow \infty$ (régimen asintótico).

Para sistemas prácticos con longitud de bloque finita, el teorema de codificación de canal de segundo orden establece:

$$\log_2 M \leq nC - \sqrt{nV}Q^{-1}(\epsilon) + O(\log n)$$

donde $V$ es la dispersión del canal, $\epsilon$ es la probabilidad de error objetivo, y $Q^{-1}(\cdot)$ es la función cuantil de la distribución normal estándar. Esta expresión caracteriza el penalty de longitud de bloque finita.

#### 3) Distorsión y Tasa-Distorsión en Comunicaciones Semánticas

Para comunicaciones semánticas, donde el objetivo no es reproducir exactamente los bits sino preservar el significado o contenido relevante, la teoría de tasa-distorsión de Shannon establece el límite fundamental. Sea $D$ la distorsión promedio permisible medida por una métrica $d(\mathbf{s}, \hat{\mathbf{s}})$ entre la fuente original $\mathbf{s}$ y su reconstrucción $\hat{\mathbf{s}}$. La función de tasa-distorsión se define como:

$$R(D) = \min_{p(\hat{\mathbf{s}}|\mathbf{s}): \mathbb{E}[d(\mathbf{s}, \hat{\mathbf{s}})] \leq D} I(\mathbf{S}; \hat{\mathbf{S}})$$

Para una fuente gaussiana con distorsión cuadrática media, la función de tasa-distorsión es:

$$R(D) = \begin{cases}
\frac{1}{2}\log_2\left(\frac{\sigma_s^2}{D}\right) & \text{si } D \leq \sigma_s^2 \\
0 & \text{si } D > \sigma_s^2
\end{cases}$$

donde $\sigma_s^2$ es la varianza de la fuente.

En IA nativa, los autocodificadores variacionales (VAE) implementan esquemas de compresión semántica optimizando la cota inferior de la evidencia (ELBO):

$$\mathcal{L}_{\text{VAE}} = \mathbb{E}_{q(\mathbf{z}|\mathbf{s})}[\log p(\mathbf{s}|\mathbf{z})] - D_{\text{KL}}(q(\mathbf{z}|\mathbf{s}) || p(\mathbf{z}))$$

donde $\mathbf{z}$ es la representación latente compacta (embedding semántico), $q(\mathbf{z}|\mathbf{s})$ es el codificador probabilístico, $p(\mathbf{s}|\mathbf{z})$ es el decodificador probabilístico, y $D_{\text{KL}}$ es la divergencia de Kullback-Leibler que regulariza la complejidad de la representación.

### C. Fundamentos de Aprendizaje Profundo para PHY

#### 1) Arquitecturas de Redes Neuronales y Representación Universal

El teorema de aproximación universal establece que una red neuronal feedforward con una sola capa oculta de ancho suficiente puede aproximar cualquier función continua en un dominio compacto. Formalmente, dada una función continua $f: [0,1]^d \rightarrow \mathbb{R}$ y precisión $\epsilon > 0$, existe una red:

$$\hat{f}(\mathbf{x}) = \sum_{i=1}^{N_h} w_i \sigma(\mathbf{v}_i^T \mathbf{x} + b_i) + w_0$$

tal que $\sup_{\mathbf{x} \in [0,1]^d} |f(\mathbf{x}) - \hat{f}(\mathbf{x})| < \epsilon$, donde $N_h$ es el número de neuronas ocultas, $w_i, b_i$ son pesos y sesgos, y $\mathbf{v}_i \in \mathbb{R}^d$ son vectores de pesos de entrada.

Para funciones de procesamiento de señales en el nivel físico, esto implica que los receptores neuronales pueden aproximar arbitrariamente bien el receptor óptimo de máxima verosimilitud:

$$\hat{m}_{\text{ML}} = \arg\max_{m \in \mathcal{M}} p(\mathbf{y}|m)$$

siempre que la red tenga capacidad suficiente.

La teoría de aproximación para redes profundas establece que arquitecturas con múltiples capas pueden lograr la misma precisión con menos parámetros que redes shallow. Específicamente, para funciones con estructura compositiva (composición de funciones más simples), una red con profundidad $L$ puede requerir $O(\text{poly}(d))$ neuronas, mientras que una red shallow requeriría $O(\exp(d))$ neuronas.

La capacidad de representación de una red se cuantifica mediante su número de parámetros:

$$N_{\theta} = \sum_{l=1}^{L+1} n_l n_{l-1} + \sum_{l=1}^{L+1} n_l$$

donde el primer término corresponde a las matrices de pesos y el segundo a los vectores de sesgo.

#### 2) Funciones de Pérdida y Objetivos de Optimización

El entrenamiento de sistemas de comunicación end-to-end mediante IA nativa requiere definir una función de pérdida diferenciable que cuantifique el desempeño del sistema. Las funciones de pérdida más comunes son:

**Entropía Cruzada (Cross-Entropy):** Para clasificación de mensajes discretos, la función de pérdida estándar es:

$$\mathcal{L}_{\text{CE}}(\boldsymbol{\theta}) = -\frac{1}{N}\sum_{i=1}^{N}\log p(m_i|\mathbf{y}_i; \boldsymbol{\theta})$$

donde $\boldsymbol{\theta} = \{\boldsymbol{\theta}_{\text{TX}}, \boldsymbol{\theta}_{\text{RX}}\}$ son todos los parámetros del sistema end-to-end, y $N$ es el tamaño del lote de entrenamiento.

Expandiendo la probabilidad en términos de la salida softmax:

$$\mathcal{L}_{\text{CE}} = -\frac{1}{N}\sum_{i=1}^{N}\log\left(\frac{e^{z_{m_i}}}{\sum_{j=1}^{M}e^{z_j}}\right) = -\frac{1}{N}\sum_{i=1}^{N}\left(z_{m_i} - \log\sum_{j=1}^{M}e^{z_j}\right)$$

donde $z_j$ es el logit de la clase $j$ antes de la softmax.

**Error Cuadrático Medio (MSE):** Para comunicaciones analógicas o reconstrucción de señales:

$$\mathcal{L}_{\text{MSE}}(\boldsymbol{\theta}) = \frac{1}{N}\sum_{i=1}^{N}\|\mathbf{s}_i - \hat{\mathbf{s}}_i(\boldsymbol{\theta})\|^2$$

donde $\mathbf{s}_i$ es la señal original y $\hat{\mathbf{s}}_i$ es su reconstrucción.

**Información Mutua Negativa:** Para maximizar directamente la información mutua:

$$\mathcal{L}_{\text{MI}}(\boldsymbol{\theta}) = -\hat{I}(\mathbf{X}; \mathbf{Y}) = H(M|\mathbf{Y}) - H(M)$$

Esta función requiere estimar $H(M|\mathbf{Y})$ mediante técnicas de estimación de entropía como el estimador de k-vecinos más cercanos.

**Combinación con Regularización:** Para controlar la complejidad del modelo y evitar sobreajuste, se añaden términos de regularización:

$$\mathcal{L}_{\text{total}}(\boldsymbol{\theta}) = \mathcal{L}_{\text{CE}}(\boldsymbol{\theta}) + \lambda_1 \|\boldsymbol{\theta}\|_2^2 + \lambda_2 \|\boldsymbol{\theta}\|_1$$

donde el primer término de regularización es la norma L2 (weight decay) y el segundo es la norma L1 (promoción de esparsidad), con hiperparámetros $\lambda_1, \lambda_2 \geq 0$.

#### 3) Algoritmos de Optimización y Retropropagación

El entrenamiento de redes neuronales se realiza mediante descenso de gradiente estocástico (SGD) o sus variantes. El algoritmo básico actualiza los parámetros en dirección opuesta al gradiente de la función de pérdida:

$$\boldsymbol{\theta}^{(t+1)} = \boldsymbol{\theta}^{(t)} - \eta \nabla_{\boldsymbol{\theta}}\mathcal{L}(\boldsymbol{\theta}^{(t)})$$

donde $\eta > 0$ es la tasa de aprendizaje e iteración $t$.

El gradiente se calcula eficientemente mediante el algoritmo de retropropagación (backpropagation), que aplica la regla de la cadena para propagar derivadas desde la salida hacia las capas anteriores:

$$\frac{\partial \mathcal{L}}{\partial \mathbf{W}^{(l)}} = \frac{\partial \mathcal{L}}{\partial \mathbf{h}^{(l)}} \cdot \frac{\partial \mathbf{h}^{(l)}}{\partial \mathbf{z}^{(l)}} \cdot \frac{\partial \mathbf{z}^{(l)}}{\partial \mathbf{W}^{(l)}}$$

donde $\mathbf{z}^{(l)} = \mathbf{W}^{(l)}\mathbf{h}^{(l-1)} + \mathbf{b}^{(l)}$ es la activación pre-función no lineal.

Para la función de activación ReLU $\sigma(z) = \max(0, z)$, la derivada es:

$$\frac{\partial \sigma(z)}{\partial z} = \begin{cases}
1 & \text{si } z > 0 \\
0 & \text{si } z \leq 0
\end{cases}$$

**Optimizador Adam (Adaptive Moment Estimation):** Una variante avanzada que adapta la tasa de aprendizaje por parámetro utilizando estimaciones del primer y segundo momento del gradiente:

$$\mathbf{m}^{(t)} = \beta_1 \mathbf{m}^{(t-1)} + (1-\beta_1)\nabla_{\boldsymbol{\theta}}\mathcal{L}(\boldsymbol{\theta}^{(t-1)})$$

$$\mathbf{v}^{(t)} = \beta_2 \mathbf{v}^{(t-1)} + (1-\beta_2)[\nabla_{\boldsymbol{\theta}}\mathcal{L}(\boldsymbol{\theta}^{(t-1)})]^2$$

$$\hat{\mathbf{m}}^{(t)} = \frac{\mathbf{m}^{(t)}}{1-\beta_1^t}, \quad \hat{\mathbf{v}}^{(t)} = \frac{\mathbf{v}^{(t)}}{1-\beta_2^t}$$

$$\boldsymbol{\theta}^{(t)} = \boldsymbol{\theta}^{(t-1)} - \eta \frac{\hat{\mathbf{m}}^{(t)}}{\sqrt{\hat{\mathbf{v}}^{(t)}} + \epsilon}$$

donde $\beta_1 \approx 0.9$, $\beta_2 \approx 0.999$, y $\epsilon \approx 10^{-8}$ son hiperparámetros estándar.

**Complejidad Computacional del Entrenamiento:** Para una red con $L$ capas y $N_{\theta}$ parámetros totales, cada iteración de entrenamiento con un lote de tamaño $B$ requiere:

- Propagación hacia adelante: $O(BN_{\theta})$ operaciones
- Cálculo de pérdida y retropropagación: $O(BN_{\theta})$ operaciones
- Actualización de parámetros: $O(N_{\theta})$ operaciones

El costo total por época (paso completo sobre el conjunto de entrenamiento de tamaño $N_{\text{train}}$) es:

$$C_{\text{época}} = O\left(\frac{N_{\text{train}}}{B} \cdot BN_{\theta}\right) = O(N_{\text{train}}N_{\theta})$$

### D. Formulación del Problema de Optimización End-to-End

#### 1) Optimización Conjunta del Sistema de Comunicación

El problema fundamental en IA nativa para el nivel físico es la optimización conjunta del transmisor y receptor para maximizar el rendimiento del sistema bajo restricciones de potencia, ancho de banda y otros recursos. La formulación general es:

$$\min_{\boldsymbol{\theta}_{\text{TX}}, \boldsymbol{\theta}_{\text{RX}}} \mathbb{E}_{m \sim \mathcal{U}(\mathcal{M}), \mathbf{H}, \mathbf{n}}[\mathcal{L}(m, f_{\text{RX}}(f_{\text{CH}}(f_{\text{TX}}(m; \boldsymbol{\theta}_{\text{TX}}), \mathbf{H}, \mathbf{n}); \boldsymbol{\theta}_{\text{RX}}))]$$

$$\text{sujeto a: } \mathbb{E}[\|f_{\text{TX}}(m; \boldsymbol{\theta}_{\text{TX}})\|^2] \leq nP$$

donde $f_{\text{CH}}(\cdot, \mathbf{H}, \mathbf{n})$ modela el canal, y la expectativa se toma sobre mensajes uniformes, realizaciones del canal $\mathbf{H}$ y ruido $\mathbf{n}$.

Para el canal AWGN estacionario, la expectativa se simplifica a:

$$\min_{\boldsymbol{\theta}} \mathbb{E}_{m, \mathbf{n}}[\mathcal{L}(m, \hat{m})] = \min_{\boldsymbol{\theta}} \frac{1}{M}\sum_{m=1}^{M}\mathbb{E}_{\mathbf{n}}[\mathcal{L}(m, f_{\text{RX}}(\mathbf{x}_m + \mathbf{n}; \boldsymbol{\theta}_{\text{RX}}))]$$

donde $\mathbf{x}_m = f_{\text{TX}}(m; \boldsymbol{\theta}_{\text{TX}})$ es la señal transmitida para el mensaje $m$.

**Aproximación Empírica del Riesgo (ERM):** En la práctica, la expectativa sobre todas las distribuciones se reemplaza por promedio sobre un conjunto de entrenamiento finito:

$$\hat{\mathcal{L}}(\boldsymbol{\theta}) = \frac{1}{N}\sum_{i=1}^{N}\mathcal{L}(m_i, f_{\text{RX}}(\mathbf{y}_i; \boldsymbol{\theta}_{\text{RX}}))$$

donde $\{\mathbf{y}_i\}_{i=1}^{N}$ son muestras de señales recibidas generadas durante el entrenamiento mediante simulación del canal.

#### 2) Diferenciabilidad del Canal y Gradientes End-to-End

La clave para el entrenamiento end-to-end es la diferenciabilidad del modelo de canal, que permite calcular $\frac{\partial \mathcal{L}}{\partial \boldsymbol{\theta}_{\text{TX}}}$ propagando gradientes desde el receptor a través del canal hacia el transmisor.

Para el canal AWGN, la diferenciabilidad es directa pues es una transformación afín más ruido:

$$\frac{\partial \mathbf{y}}{\partial \mathbf{x}} = \mathbf{I}_n$$

$$\frac{\partial \mathcal{L}}{\partial \boldsymbol{\theta}_{\text{TX}}} = \frac{\partial \mathcal{L}}{\partial \hat{m}} \cdot \frac{\partial \hat{m}}{\partial \mathbf{y}} \cdot \frac{\partial \mathbf{y}}{\partial \mathbf{x}} \cdot \frac{\partial \mathbf{x}}{\partial \boldsymbol{\theta}_{\text{TX}}}$$

El término del ruido $\mathbf{n}$ no depende de $\mathbf{x}$, por lo que su gradiente es cero.

Para canales con desvanecimiento, donde $\mathbf{y} = \mathbf{H}\mathbf{x} + \mathbf{n}$:

$$\frac{\partial \mathbf{y}}{\partial \mathbf{x}} = \mathbf{H}$$

$$\frac{\partial y_i}{\partial x_j} = H_{ij}$$

El gradiente completo incorpora la matriz de canal en la retropropagación:

$$\frac{\partial \mathcal{L}}{\partial \mathbf{x}} = \mathbf{H}^T \frac{\partial \mathcal{L}}{\partial \mathbf{y}}$$

Para canales no lineales, como aquellos con efectos de amplificador de potencia, se requiere conocer o aprender el modelo no lineal $\mathbf{y} = g(\mathbf{x}) + \mathbf{n}$ y su jacobiano $\frac{\partial g}{\partial \mathbf{x}}$.

**Modelado Generativo del Canal:** Cuando el canal real no tiene modelo analítico, se puede entrenar una red neuronal generativa $f_{\text{CH}}(\mathbf{x}; \boldsymbol{\phi})$ utilizando datos capturados del canal real, y luego usarla durante el entrenamiento del autocodificador:

$$\min_{\boldsymbol{\phi}} \mathbb{E}_{\mathbf{x}, \mathbf{y}_{\text{real}}}[\|\mathbf{y}_{\text{real}} - f_{\text{CH}}(\mathbf{x}; \boldsymbol{\phi})\|^2]$$

Una vez entrenado, el modelo generativo $f_{\text{CH}}$ se fija y se utiliza para entrenar $\boldsymbol{\theta}_{\text{TX}}, \boldsymbol{\theta}_{\text{RX}}$ mediante retropropagación a través de $f_{\text{CH}}$.

#### 3) Restricciones y Métodos de Proyección

Las restricciones físicas del sistema (potencia, espectro, amplitud pico) deben incorporarse en la optimización. El método de Lagrange introduce multiplicadores $\boldsymbol{\lambda}$ para convertir restricciones en penalizaciones:

$$\mathcal{L}_{\text{aug}}(\boldsymbol{\theta}, \boldsymbol{\lambda}) = \mathcal{L}(\boldsymbol{\theta}) + \sum_i \lambda_i g_i(\boldsymbol{\theta})$$

donde $g_i(\boldsymbol{\theta})$ son las funciones de restricción.

**Restricción de Potencia Promedio:** Para garantizar $\mathbb{E}[\|\mathbf{x}\|^2] \leq nP$, se añade el término:

$$\mathcal{L}_{\text{power}}(\boldsymbol{\theta}_{\text{TX}}) = \lambda_P \max\left(0, \frac{1}{B}\sum_{i=1}^{B}\|\mathbf{x}_i\|^2 - nP\right)$$

Alternativamente, se aplica normalización por lotes después de cada generación de símbolo:

$$\mathbf{x}_{\text{norm}} = \sqrt{\frac{nP}{\frac{1}{B}\sum_{i=1}^{B}\|\mathbf{x}_i\|^2}} \cdot \mathbf{x}$$

**Restricción de PAPR (Peak-to-Average Power Ratio):** Para limitar la amplitud pico de las señales OFDM y evitar distorsión no lineal en amplificadores:

$$\text{PAPR} = \frac{\max_{i}|x_i|^2}{\frac{1}{n}\sum_{i=1}^{n}|x_i|^2}$$

Se penaliza PAPR alto mediante:

$$\mathcal{L}_{\text{PAPR}}(\boldsymbol{\theta}_{\text{TX}}) = \lambda_{\text{PAPR}} \cdot \mathbb{E}[\text{PAPR}(\mathbf{x})]$$

**Restricción Espectral:** Para limitar la ocupación espectral y cumplir máscaras regulatorias, se penaliza la potencia fuera de banda:

$$\mathcal{L}_{\text{spec}}(\boldsymbol{\theta}_{\text{TX}}) = \lambda_{\text{spec}} \sum_{f \notin B_{\text{allowed}}} |X(f)|^2$$

donde $X(f)$ es la transformada de Fourier de $\mathbf{x}$ y $B_{\text{allowed}}$ es el conjunto de frecuencias permitidas.

### E. Análisis de Convergencia y Garantías Teóricas

#### 1) Convergencia del Descenso de Gradiente

Para funciones de pérdida convexas y Lipschitz continuas, el descenso de gradiente con tasa de aprendizaje apropiada converge al óptimo global. Sin embargo, las redes neuronales profundas inducen funciones de pérdida no convexas con múltiples mínimos locales.

**Teorema de Convergencia para Funciones L-Smooth:** Una función $\mathcal{L}(\boldsymbol{\theta})$ es $L$-smooth si su gradiente es Lipschitz continuo:

$$\|\nabla\mathcal{L}(\boldsymbol{\theta}_1) - \nabla\mathcal{L}(\boldsymbol{\theta}_2)\| \leq L\|\boldsymbol{\theta}_1 - \boldsymbol{\theta}_2\|$$

Para funciones $L$-smooth, el descenso de gradiente con tasa $\eta < \frac{2}{L}$ satisface:

$$\mathcal{L}(\boldsymbol{\theta}^{(t)}) - \mathcal{L}(\boldsymbol{\theta}^*) \leq \frac{L\|\boldsymbol{\theta}^{(0)} - \boldsymbol{\theta}^*\|^2}{2t}$$

donde $\boldsymbol{\theta}^*$ es un punto crítico (no necesariamente global). Esta garantía indica convergencia con tasa $O(1/t)$.

**Análisis de Convergencia Estocástica:** Para SGD con lotes de tamaño $B$, el gradiente estimado es ruidoso:

$$\mathbf{g}^{(t)} = \frac{1}{B}\sum_{i=1}^{B}\nabla_{\boldsymbol{\theta}}\mathcal{L}_i(\boldsymbol{\theta}^{(t)})$$

Bajo la suposición de varianza acotada del gradiente estocástico:

$$\mathbb{E}[\|\mathbf{g}^{(t)} - \nabla\mathcal{L}(\boldsymbol{\theta}^{(t)})\|^2] \leq \frac{\sigma^2}{B}$$

el SGD converge con tasa:

$$\mathbb{E}[\mathcal{L}(\bar{\boldsymbol{\theta}}^{(T)})] - \mathcal{L}(\boldsymbol{\theta}^*) \leq O\left(\frac{1}{\sqrt{T}}\right) + O\left(\frac{\sigma^2}{B\sqrt{T}}\right)$$

donde $\bar{\boldsymbol{\theta}}^{(T)} = \frac{1}{T}\sum_{t=1}^{T}\boldsymbol{\theta}^{(t)}$ es el promedio de iteraciones.

#### 2) Teoría de Generalización y Bounds PAC

La capacidad de generalización de las redes neuronales entrenadas se analiza mediante la teoría PAC (Probably Approximately Correct). La cota de generalización establece que con probabilidad al menos $1-\delta$:

$$\mathcal{L}_{\text{test}}(\boldsymbol{\theta}) \leq \mathcal{L}_{\text{train}}(\boldsymbol{\theta}) + \sqrt{\frac{d\log(N_{\text{train}}/d) + \log(1/\delta)}{N_{\text{train}}}}$$

donde $d$ es la dimensión VC (Vapnik-Chervonenkis) de la clase de funciones, y $N_{\text{train}}$ es el tamaño del conjunto de entrenamiento.

Para redes neuronales feedforward con $N_{\theta}$ parámetros, la dimensión VC está acotada por:

$$d_{\text{VC}} \leq O(N_{\theta} \log N_{\theta})$$

lo que implica que el error de generalización decrece como $O\left(\sqrt{\frac{N_{\theta}\log N_{\theta}}{N_{\text{train}}}}\right)$.

**Bounds de Rademacher Complexity:** Una cota más ajustada utiliza la complejidad de Rademacher:

$$\mathcal{R}_N(\mathcal{F}) = \mathbb{E}_{\boldsymbol{\sigma}}\left[\sup_{f \in \mathcal{F}}\frac{1}{N}\sum_{i=1}^{N}\sigma_i f(\mathbf{x}_i)\right]$$

donde $\boldsymbol{\sigma} = (\sigma_1, ..., \sigma_N)$ son variables Rademacher independientes ($\sigma_i \in \{-1, +1\}$ con probabilidad 1/2 cada una). La cota de generalización es:

$$\mathbb{E}[\mathcal{L}_{\text{test}}] \leq \mathcal{L}_{\text{train}} + 2\mathcal{R}_N(\mathcal{F}) + 3\sqrt{\frac{\log(2/\delta)}{2N}}$$

Para redes con normas acotadas de los pesos, la complejidad de Rademacher se puede acotar por:

$$\mathcal{R}_N(\mathcal{F}_{\text{NN}}) \leq \frac{C}{\sqrt{N}}\prod_{l=1}^{L}\|\mathbf{W}^{(l)}\|_2$$

donde $C$ es una constante, mostrando que la regularización de norma de pesos mejora la generalización.

#### 3) Análisis de Estabilidad y Robustez

La robustez del sistema ante variaciones del canal y desajuste entre entrenamiento y despliegue es crítica. Se define la sensibilidad del sistema como:

$$S = \mathbb{E}_{\boldsymbol{\theta}, \Delta\mathbf{H}}\left[\frac{\|\mathcal{L}(\boldsymbol{\theta}; \mathbf{H} + \Delta\mathbf{H}) - \mathcal{L}(\boldsymbol{\theta}; \mathbf{H})\|}{\|\Delta\mathbf{H}\|}\right]$$

Idealmente, $S$ debe ser pequeña para garantizar operación robusta.

**Entrenamiento Adversario para Robustez:** Para mejorar la robustez, se entrena contra perturbaciones adversarias del canal:

$$\min_{\boldsymbol{\theta}} \max_{\|\Delta\mathbf{H}\| \leq \epsilon} \mathcal{L}(\boldsymbol{\theta}; \mathbf{H} + \Delta\mathbf{H})$$

Este problema minimax se resuelve mediante entrenamiento adversario iterativo:

1. Calcular la perturbación adversaria:
$$\Delta\mathbf{H}^* = \arg\max_{\|\Delta\mathbf{H}\| \leq \epsilon} \mathcal{L}(\boldsymbol{\theta}^{(t)}; \mathbf{H} + \Delta\mathbf{H})$$

2. Actualizar parámetros contra la perturbación:
$$\boldsymbol{\theta}^{(t+1)} = \boldsymbol{\theta}^{(t)} - \eta\nabla_{\boldsymbol{\theta}}\mathcal{L}(\boldsymbol{\theta}^{(t)}; \mathbf{H} + \Delta\mathbf{H}^*)$$

**Certificados de Robustez:** Para canales AWGN, se pueden derivar certificados probabilísticos de que el receptor clasificará correctamente incluso con perturbación:

$$P\left(\hat{m}(\mathbf{y} + \boldsymbol{\delta}) = m\right) \geq 1 - \epsilon$$

para cualquier perturbación $\|\boldsymbol{\delta}\| \leq r$, donde $r$ es el radio de robustez certificado que depende de la suavidad Lipschitz del clasificador.

#### 4) Límites de Rendimiento y Comparación con Óptimos

Para evaluar la optimalidad de los sistemas basados en IA nativa, se comparan con límites teóricos conocidos. Para comunicación sobre canal AWGN, el límite de Shannon proporciona la cota superior fundamental.

**Gap a Capacidad:** Se define el gap a capacidad como:

$$\Delta = C_{\text{Shannon}} - \frac{1}{n}I(\mathbf{X}; \mathbf{Y})$$

donde $I(\mathbf{X}; \mathbf{Y})$ es la información mutua alcanzada por el autocodificador neuronal. Idealmente, $\Delta \rightarrow 0$ conforme la capacidad de la red y cantidad de entrenamiento aumentan.

**Comparación con Decodificador ML:** El decodificador de máxima verosimilitud (ML) alcanza la mínima probabilidad de error para un codificador dado:

$$P_e^{\text{ML}} = P(\hat{m}_{\text{ML}} \neq m) = \min_{f_{\text{RX}}} P(f_{\text{RX}}(\mathbf{y}) \neq m)$$

Para modulación equiprobable con decisión ML:

$$P_e^{\text{ML}} = \frac{1}{M}\sum_{m=1}^{M}P(\mathbf{y} \notin \mathcal{D}_m | m)$$

donde $\mathcal{D}_m$ es la región de decisión óptima para el mensaje $m$.

El receptor neuronal debe aproximar esta decisión óptima:

$$P_e^{\text{NN}} - P_e^{\text{ML}} \leq \epsilon_{\text{approx}}$$

donde $\epsilon_{\text{approx}}$ depende de la capacidad de la red y converge a cero con arquitectura suficientemente expresiva.

**Análisis de Diversidad y Ganancia de Codificación:** Para canales con desvanecimiento, la probabilidad de error en alto SNR se comporta como:

$$P_e \approx (G_c \cdot \text{SNR})^{-G_d}$$

donde $G_d$ es el orden de diversidad y $G_c$ es la ganancia de codificación. Los autocodificadores neuronales pueden aprender esquemas que maximicen implícitamente estos parámetros:

$$\log P_e \approx -G_d \log(\text{SNR}) + \log G_c$$

La pendiente en escala logarítmica revela $G_d$, que idealmente iguala el número de caminos independientes en el canal MIMO o diversidad temporal disponible.

**Criterio de Optimalidad para Constelaciones:** Para canales AWGN, las constelaciones óptimas maximizan la distancia mínima entre puntos de señal:

$$d_{\min} = \min_{m \neq m'}\|\mathbf{x}_m - \mathbf{x}_{m'}\|$$

sujeto a la restricción de potencia promedio. Para $M=2^k$ mensajes con potencia unitaria, la probabilidad de error se puede acotar:

$$P_e \leq (M-1)Q\left(\frac{d_{\min}}{2\sigma_n}\right)$$

donde $Q(x) = \frac{1}{\sqrt{2\pi}}\int_x^{\infty}e^{-t^2/2}dt$ es la función Q.

Los autocodificadores neuronales aprenden implícitamente constelaciones que maximizan $d_{\min}$, convergiendo a configuraciones cercanas a las óptimas conocidas (e.g., PSK para potencia constante, QAM para potencia promedio) [11], [12].

**Bounds de Error para Códigos Neuronales:** La teoría de codificación de canal establece que para tasas $R < C$, existen códigos con probabilidad de error arbitrariamente pequeña. Para códigos neuronales con longitud de bloque $n$, el exponente de error aleatorio de Gallager proporciona:

$$P_e \leq 2^{-n[E_r(R) + o(1)]}$$

donde $E_r(R)$ es el exponente de error aleatorio:

$$E_r(R) = \max_{0 \leq \rho \leq 1}\left[E_0(\rho) - \rho R\right]$$

$$E_0(\rho) = -\log_2\int\left[\int p(y|x)^{1/(1+\rho)}p(x)dx\right]^{1+\rho}dy$$

Los autocodificadores neuronales que alcanzan $P_e$ cercana a este límite se consideran óptimos en sentido de exponente de error.

---

## Referencias

[1] M. Z. Chowdhury, M. Shahjalal, S. Ahmed, and Y. M. Jang, "6G wireless communication systems: Applications, requirements, technologies, challenges, and research directions," *IEEE Open Journal of the Communications Society*, vol. 1, pp. 957-975, 2020.

[11] M. Kim, N.-I. Kim, W. Lee, and D.-H. Cho, "Deep learning-aided SCMA," *IEEE Communications Letters*, vol. 22, no. 4, pp. 720-723, Apr. 2018.

[12] F. A. Aoudia and J. Hoydis, "End-to-end learning of communications systems without a channel model," in *Proc. 52nd Asilomar Conference on Signals, Systems, and Computers*, Pacific Grove, CA, USA, Oct. 2018, pp. 298-303.

[2] C. Zhang, P. Patras, and H. Haddadi, "Deep learning in mobile and wireless networking: A survey," *IEEE Communications Surveys & Tutorials*, vol. 21, no. 3, pp. 2224-2287, Third Quarter 2019.

[3] T. O'Shea and J. Hoydis, "An introduction to deep learning for the physical layer," *IEEE Transactions on Cognitive Communications and Networking*, vol. 3, no. 4, pp. 563-575, Dec. 2017.

[4] W. Saad, M. Bennis, and M. Chen, "A vision of 6G wireless systems: Applications, trends, technologies, and open research problems," *IEEE Network*, vol. 34, no. 3, pp. 134-142, May/June 2020.

[5] H. Xie, Z. Qin, G. Y. Li, and B.-H. Juang, "Deep learning enabled semantic communication systems," *IEEE Transactions on Signal Processing*, vol. 69, pp. 2663-2675, 2021.

[6] Y. LeCun, Y. Bengio, and G. Hinton, "Deep learning," *Nature*, vol. 521, no. 7553, pp. 436-444, May 2015.

[7] S. Dörner, S. Cammerer, J. Hoydis, and S. ten Brink, "Deep learning based communication over the air," *IEEE Journal of Selected Topics in Signal Processing*, vol. 12, no. 1, pp. 132-143, Feb. 2018.

[8] N. Samuel, T. Diskin, and A. Wiesel, "Deep MIMO detection," *IEEE Transactions on Wireless Communications*, vol. 18, no. 11, pp. 5559-5571, Nov. 2019.

[9] H. Sun, X. Chen, Q. Shi, M. Hong, X. Fu, and N. D. Sidiropoulos, "Learning to optimize: Training deep neural networks for interference management," *IEEE Transactions on Signal Processing*, vol. 66, no. 20, pp. 5438-5453, Oct. 2018.

[10] Z. Qin, X. Tao, J. Lu, W. Tong, and G. Y. Li, "Semantic communications: Principles and challenges," *arXiv preprint arXiv:2201.01389*, 2022.

