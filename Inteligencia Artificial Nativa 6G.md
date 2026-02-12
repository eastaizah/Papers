# Inteligencia Artificial Nativa en el Nivel Físico de Redes 6G: Fundamentos, Arquitecturas y Perspectivas

---

**Resumen**—La sexta generación de redes móviles (6G) representa un cambio paradigmático en la concepción de sistemas de comunicación inalámbrica, donde la Inteligencia Artificial (IA) no se integra como una característica adicional, sino que se concibe como un componente nativo y fundamental del nivel físico (PHY). Este artículo presenta un análisis exhaustivo de la IA nativa en el nivel físico de 6G, abordando sus fundamentos teóricos, arquitecturas propuestas, algoritmos de aprendizaje, desafíos de implementación y direcciones futuras de investigación. Se examina en detalle la transformación de bloques funcionales tradicionales del nivel físico mediante técnicas de aprendizaje profundo, incluyendo codificación de canal, estimación de canal, detección de señales, conformación de haces (beamforming) y gestión de recursos radio. Se presenta el marco matemático riguroso que sustenta estos desarrollos, incluyendo formulaciones de optimización, análisis de convergencia, y caracterización de rendimiento teórico. Los resultados demuestran que la IA nativa en el nivel físico no solo mejora métricas de rendimiento convencionales, sino que habilita capacidades emergentes esenciales para 6G, como comunicaciones semánticas, adaptación predictiva al entorno, y operación en regímenes de complejidad computacional previamente inaccesibles.

**Palabras clave**—6G, Inteligencia Artificial Nativa, Nivel Físico, Aprendizaje Profundo, Codificación Neural, Estimación de Canal, Beamforming Inteligente, Optimización End-to-End.

---

## I. INTRODUCCIÓN

### A. Contexto y Motivación

La evolución de las redes móviles ha seguido un patrón consistente de incremento en las capacidades de transmisión de datos, reducción de latencia y soporte de mayor densidad de dispositivos conectados. Desde la primera generación (1G) enfocada en comunicaciones de voz analógicas, hasta la quinta generación (5G) que habilita casos de uso como comunicaciones ultra-confiables de baja latencia (URLLC) y comunicaciones masivas tipo máquina (mMTC), cada generación ha respondido a demandas crecientes de la sociedad digital.

Sin embargo, las proyecciones para la década de 2030 plantean requisitos que trascienden las capacidades de 5G y sus evoluciones previstas (5G-Advanced). Se anticipa la necesidad de soportar tasas de datos del orden de terabits por segundo (Tbps), latencias sub-milisegundo con confiabilidad extrema (99.99999%), conectividad ubicua tridimensional (terrestre, aérea y submarina), integración de comunicaciones y sensado (ISAC - Integrated Sensing and Communications), y soporte de aplicaciones emergentes como realidad extendida (XR) de ultra-alta fidelidad, internet táctil, y gemelos digitales distribuidos en tiempo real.

Estos requisitos plantean desafíos fundamentales que no pueden ser abordados mediante la extrapolación incremental de tecnologías actuales. Las arquitecturas tradicionales del nivel físico, basadas en procesamiento de señales algorítmico con diseño específico para modelos de canal y escenarios particulares, muestran limitaciones inherentes en términos de adaptabilidad, escalabilidad y eficiencia espectral en entornos complejos y dinámicos.

En este contexto, la Inteligencia Artificial (IA), y específicamente el aprendizaje profundo (Deep Learning, DL), emerge como un paradigma transformador. A diferencia de aproximaciones previas donde la IA se aplicaba para optimizar parámetros o gestionar recursos en capas superiores, el concepto de **IA Nativa en el Nivel Físico** propone una reformulación fundamental: los bloques funcionales del PHY se diseñan, desde su concepción, como sistemas de aprendizaje automático que aprenden representaciones óptimas directamente de los datos, sin depender de modelos analíticos simplificados.

### B. Estado del Arte y Evolución Conceptual

La aplicación de técnicas de aprendizaje automático a comunicaciones inalámbricas tiene antecedentes en investigaciones sobre redes neuronales aplicadas a ecualización, detección y modulación desde la década de 1990. Sin embargo, estas aproximaciones tempranas estaban limitadas por la capacidad computacional disponible, la falta de grandes volúmenes de datos de entrenamiento, y arquitecturas de redes neuronales relativamente simples.

El resurgimiento del interés en IA para comunicaciones, iniciado alrededor de 2016-2017, fue catalizado por varios factores convergentes:

1. **Avances en Aprendizaje Profundo**: El desarrollo de arquitecturas sofisticadas (redes convolucionales profundas, redes recurrentes con mecanismos de atención, transformers) y técnicas de entrenamiento robustas (normalización por lotes, optimizadores adaptativos, regularización avanzada).

2. **Disponibilidad de Recursos Computacionales**: La proliferación de unidades de procesamiento gráfico (GPUs) y procesadores especializados (TPUs, NPUs) que aceleran dramáticamente el entrenamiento e inferencia de modelos complejos.

3. **Datos y Simulaciones**: Capacidad para generar grandes datasets sintéticos de señales de comunicación bajo diversas condiciones de canal, así como datasets de mediciones reales de propagación.

4. **Límites Teóricos de Aproximaciones Tradicionales**: Reconocimiento de que en escenarios complejos (canales con múltiples dispersores, interferencia no-gaussiana, entornos no-estacionarios), las soluciones basadas en modelos analíticos simplificados están significativamente sub-optimizadas.

Los trabajos pioneros de O'Shea y Hoydis introdujeron el concepto de **autoencoder para comunicaciones end-to-end**, donde tanto el transmisor como el receptor se implementan como redes neuronales entrenadas conjuntamente para minimizar una función de pérdida relacionada con la tasa de error. Esta aproximación demostró que sistemas neuronales podían aprender esquemas de modulación y codificación competitivos con diseños tradicionales, y en algunos casos, descubrir soluciones no-convencionales con mejor rendimiento.

Posteriormente, la investigación se expandió hacia componentes específicos del nivel físico:

- **Codificación de Canal Neural**: Reemplazo de códigos tradicionales (Turbo, LDPC, Polar) por autoencoders con propiedades de corrección de errores aprendidas.
- **Estimación y Ecualización de Canal**: Uso de redes neuronales recurrentes (RNN) y convolucionales (CNN) para estimar respuestas de canal y cancelar interferencia.
- **Beamforming y Conformación de Haces**: Aplicación de aprendizaje por refuerzo (RL) y redes profundas para optimizar pesos de antena en sistemas MIMO masivo.
- **Detección Multi-Usuario**: Algoritmos de aprendizaje supervisado para aproximar detectores óptimos (ML, MAP) con complejidad reducida.

Para 6G, el concepto evoluciona hacia **IA Nativa**, donde:

1. La IA no es un complemento, sino el principio de diseño fundamental.
2. Los modelos se entrenan con datos multi-modales (señales RF, contexto espacial, información semántica).
3. El aprendizaje es continuo y adaptativo durante la operación.
4. La arquitectura del PHY es holística y optimizada end-to-end, no como concatenación de bloques independientes.

### C. Objetivos y Contribuciones del Artículo

Este artículo presenta una revisión exhaustiva y original del estado del arte en IA nativa para el nivel físico de 6G, con las siguientes contribuciones principales:

1. **Marco Teórico Unificado**: Desarrollo de un formalismo matemático riguroso que caracteriza el problema de optimización end-to-end del nivel físico como un problema de aprendizaje de representaciones con restricciones físicas y de información.

2. **Análisis Detallado de Arquitecturas**: Descripción pormenorizada de arquitecturas de redes neuronales específicamente diseñadas para componentes del PHY, incluyendo análisis de complejidad computacional, requisitos de memoria, y consideraciones de implementación en hardware.

3. **Fundamentos Matemáticos**: Presentación explícita de las formulaciones de optimización, derivaciones de gradientes, análisis de convergencia, y caracterización de límites teóricos de rendimiento.

4. **Evaluación Comparativa**: Comparación cuantitativa entre aproximaciones basadas en IA y métodos tradicionales del nivel físico, bajo diversas métricas de rendimiento y condiciones operativas.

5. **Desafíos Abiertos y Direcciones Futuras**: Identificación de problemas de investigación no resueltos y propuestas de líneas de desarrollo para la próxima década.

### D. Organización del Artículo

El resto del artículo se estructura de la siguiente manera: La Sección II establece los fundamentos teóricos de la IA nativa en el nivel físico, incluyendo teoría de la información, aprendizaje de representaciones y formulación del problema de optimización. La Sección III examina en detalle la aplicación de IA a componentes individuales del PHY (codificación, estimación de canal, detección, beamforming). La Sección IV presenta arquitecturas de sistemas end-to-end y optimización conjunta. La Sección V discute aspectos de implementación práctica y complejidad computacional. La Sección VI analiza desafíos pendientes incluyendo generalización, interpretabilidad y seguridad. Finalmente, la Sección VII presenta conclusiones y direcciones futuras.

---

## II. FUNDAMENTOS TEÓRICOS DE IA NATIVA EN EL NIVEL FÍSICO

### A. Modelo del Sistema de Comunicación

Consideremos un sistema de comunicación digital donde un mensaje fuente $\mathbf{s} \in \mathcal{S}$ de dimensión $k$ debe ser transmitido desde un transmisor (Alice) a un receptor (Bob) a través de un canal de comunicación inalámbrico. En el paradigma tradicional, este proceso se descompone en bloques funcionales discretos:

1. **Codificación de Fuente**: Compresión del mensaje $\mathbf{s} \rightarrow \mathbf{b}$ donde $\mathbf{b} \in \{0,1\}^{k'}$
2. **Codificación de Canal**: Adición de redundancia $\mathbf{b} \rightarrow \mathbf{c}$ donde $\mathbf{c} \in \{0,1\}^{n}$, con $n > k'$
3. **Modulación**: Mapeo a símbolos del espacio de señal $\mathbf{c} \rightarrow \mathbf{x}$ donde $\mathbf{x} \in \mathbb{C}^{M}$
4. **Canal**: Transmisión con perturbaciones $\mathbf{y} = \mathbf{H}\mathbf{x} + \mathbf{n}$
5. **Demodulación**: Estimación de símbolos codificados $\mathbf{y} \rightarrow \hat{\mathbf{c}}$
6. **Decodificación de Canal**: Corrección de errores $\hat{\mathbf{c}} \rightarrow \hat{\mathbf{b}}$
7. **Decodificación de Fuente**: Reconstrucción $\hat{\mathbf{b}} \rightarrow \hat{\mathbf{s}}$

Donde $\mathbf{H} \in \mathbb{C}^{N_r \times N_t}$ representa la matriz de canal MIMO con $N_t$ antenas transmisoras y $N_r$ antenas receptoras, y $\mathbf{n} \sim \mathcal{CN}(0, \sigma^2\mathbf{I})$ representa ruido aditivo gaussiano complejo.

#### 1) Limitaciones del Paradigma Tradicional

El diseño tradicional del nivel físico se basa en varios principios que, si bien matemáticamente elegantes, introducen limitaciones fundamentales:

**Separabilidad por Capas**: El teorema de separación de Shannon establece que, para canales con información de estado de canal (CSI) perfecta en el receptor, es óptimo diseñar codificación de fuente y canal independientemente. Sin embargo, este resultado asume:
- CSI perfecta (irrealista en práctica)
- Longitudes de código infinitas (latencia infinita)
- Canales ergódicos y estacionarios

En escenarios prácticos de 6G con latencia ultra-baja, movilidad alta, y canales no-estacionarios, estas suposiciones se violan sistemáticamente, creando una brecha de rendimiento entre la teoría y la práctica.

**Modelos de Canal Paramétricos**: Los diseños tradicionales asumen modelos de canal específicos (ej. Rayleigh, Rician, tapped-delay line). El rendimiento está optimizado para estos modelos, pero degrada significativamente cuando el canal real difiere de las suposiciones de diseño.

**Optimización Local**: Cada bloque funcional se optimiza independientemente según un criterio local (ej. maximizar distancia mínima para códigos, minimizar MSE para ecualizadores), lo que no garantiza optimalidad del sistema end-to-end.

#### 2) Formulación de IA Nativa End-to-End

En la aproximación de IA nativa, proponemos reemplazar la cadena de procesamiento completa por dos funciones parametrizadas por redes neuronales:

$$f_{\theta}: \mathcal{S} \rightarrow \mathbb{C}^{M}, \quad g_{\phi}: \mathbb{C}^{N} \rightarrow \mathcal{S}$$

donde $f_{\theta}$ representa el transmisor (codificador) con parámetros $\theta$, y $g_{\phi}$ representa el receptor (decodificador) con parámetros $\phi$.

La señal transmitida se expresa como:
$$\mathbf{x} = f_{\theta}(\mathbf{s})$$

sujeta a una restricción de potencia promedio:
$$\mathbb{E}_{\mathbf{s} \sim p(\mathbf{s})}[\|\mathbf{x}\|^2] = \mathbb{E}_{\mathbf{s}}[\|f_{\theta}(\mathbf{s})\|^2] \leq P$$

La señal recibida, después de la propagación a través del canal $h(\cdot)$, es:
$$\mathbf{y} = h(f_{\theta}(\mathbf{s})) + \mathbf{n}$$

El receptor produce una estimación:
$$\hat{\mathbf{s}} = g_{\phi}(\mathbf{y})$$

El objetivo del entrenamiento es minimizar una función de pérdida que cuantifica la discrepancia entre el mensaje original y la estimación:

$$\min_{\theta, \phi} \mathbb{E}_{\mathbf{s} \sim p(\mathbf{s}), \mathbf{n} \sim p(\mathbf{n}), \mathbf{H} \sim p(\mathbf{H})} [\mathcal{L}(\mathbf{s}, g_{\phi}(h(f_{\theta}(\mathbf{s})) + \mathbf{n}))]$$

sujeto a: $\mathbb{E}_{\mathbf{s}}[\|f_{\theta}(\mathbf{s})\|^2] \leq P$

donde $\mathcal{L}$ puede ser la entropía cruzada (para mensajes discretos), el error cuadrático medio (para señales continuas), o métricas más sofisticadas como similitud semántica.

### B. Teoría de la Información y Límites Fundamentales

#### 1) Capacidad de Canal y Límite de Shannon

Para un canal AWGN escalar con potencia $P$ y densidad espectral de ruido $N_0$, la capacidad de Shannon es:

$$C = \frac{1}{2}\log_2\left(1 + \frac{P}{N_0}\right) \text{ bits/s/Hz}$$

Para un canal MIMO con $N_t$ antenas transmisoras y $N_r$ receptoras, la capacidad (con CSI en el receptor) es:

$$C = \mathbb{E}_{\mathbf{H}}\left[\log_2\det\left(\mathbf{I}_{N_r} + \frac{P}{N_t N_0}\mathbf{H}\mathbf{H}^H\right)\right]$$

Cuando tanto el transmisor como el receptor tienen CSI perfecta, la capacidad se maximiza mediante water-filling sobre los modos singulares de $\mathbf{H}$:

$$C = \sum_{i=1}^{\min(N_t, N_r)} \log_2\left(1 + \frac{\lambda_i}{\sigma^2}\right)$$

donde $\lambda_i$ son los valores propios de la descomposición water-filling óptima.

#### 2) Límites de Rendimiento para Códigos de Longitud Finita

La teoría clásica de Shannon caracteriza rendimiento asintótico (longitud de bloque $n \rightarrow \infty$). Para bloques finitos, Polyanskiy, Poor y Verdú derivaron expansiones más precisas. La probabilidad de error de bloque para un código de tasa $R$ y longitud $n$ en un canal AWGN está acotada por:

$$P_e \geq Q\left(\frac{nC - k}{\sqrt{n V}} + \frac{\log n}{2\sqrt{n V}}\right) + o\left(\frac{1}{\sqrt{n}}\right)$$

donde $V$ es la dispersión del canal, $k$ es el número de bits de información, y $Q(\cdot)$ es la función Q complementaria.

Para el canal AWGN:
$$V = \frac{1}{2}\left(\log_2 e\right)^2 \frac{(1+\text{SNR})^2}{\text{SNR}}$$

Esta caracterización de rendimiento de código finito es crucial para 6G, donde aplicaciones URLLC requieren bloques cortos con latencias de fracciones de milisegundo.

#### 3) Representación de Información y Cuello de Botella

El Information Bottleneck (IB) framework proporciona un principio fundamental para caracterizar representaciones óptimas. Dado un par de variables aleatorias $(X, Y)$ donde $X$ es la observación y $Y$ es la variable objetivo, buscamos una representación comprimida $T(X)$ que:

$$\min_{p(t|x)} I(X; T) - \beta I(T; Y)$$

donde $\beta$ controla el trade-off entre compresión y preservación de información relevante.

En el contexto de comunicaciones, $X$ puede ser el mensaje fuente, $T$ la señal transmitida (con restricción de dimensionalidad/potencia), y $Y$ la información que permite al receptor decodificar. El óptimo del IB caracteriza la frontera fundamental entre compresión y recuperabilidad.

Para redes neuronales profundas, Tishby propuso que las capas ocultas aprenden representaciones que progresan hacia el óptimo del IB durante el entrenamiento. Esta perspectiva sugiere que las redes del nivel físico implícitamente aprenden representaciones que saturan límites información-teóricos.

#### 4) Tasa de Distorsión y Codificación Conjunta Fuente-Canal

La teoría de tasa-distorsión caracteriza el trade-off fundamental entre compresión y fidelidad de reconstrucción. Para una fuente $S$ y medida de distorsión $d(s, \hat{s})$, la función de tasa-distorsión es:

$$R(D) = \min_{p(\hat{s}|s): \mathbb{E}[d(s,\hat{s})] \leq D} I(S; \hat{S})$$

La codificación conjunta fuente-canal (JSCC) optimiza fuente y canal simultáneamente. El teorema de separación de Shannon justifica diseño separado solo bajo condiciones idealizadas. Para canales con desvanecimiento, realimentación limitada, o restricciones de delay, JSCC puede superar significativamente aproximaciones separadas.

La formulación de optimización para JSCC es:
$$\min_{f_{\theta}, g_{\phi}} \mathbb{E}[d(S, g_{\phi}(h(f_{\theta}(S))))]$$
sujeto a restricciones de potencia y ancho de banda.

Esta formulación coincide exactamente con el problema de optimización end-to-end de IA nativa, sugiriendo que los autoencoders neuronales naturalmente implementan JSCC óptima sin separación artificial.

### C. Aprendizaje de Representaciones y Redes Neuronales Profundas

#### 1) Arquitecturas Fundamentales

**Perceptrón Multicapa (MLP)**: La arquitectura más básica consiste en capas completamente conectadas:

$$\mathbf{h}^{(l+1)} = \sigma\left(\mathbf{W}^{(l)}\mathbf{h}^{(l)} + \mathbf{b}^{(l)}\right)$$

donde $\mathbf{h}^{(l)}$ es la activación de la capa $l$, $\mathbf{W}^{(l)}$ y $\mathbf{b}^{(l)}$ son pesos y sesgos, y $\sigma(\cdot)$ es una función de activación no-lineal (ReLU, tanh, sigmoid).

El teorema de aproximación universal establece que una red con una capa oculta suficientemente ancha puede aproximar cualquier función continua en un compacto con precisión arbitraria. Sin embargo, para funciones complejas, redes profundas (múltiples capas) logran representaciones exponencialmente más eficientes que redes anchas pero superficiales.

**Redes Convolucionales (CNN)**: Explotan estructura espacial/temporal mediante operaciones de convolución:

$$\mathbf{h}^{(l+1)}_{i} = \sigma\left(\sum_{j} \mathbf{w}^{(l)}_{j} * \mathbf{h}^{(l)}_{i+j} + b^{(l)}\right)$$

Las CNNs son particularmente efectivas para procesar señales en el dominio del tiempo (formas de onda) o frecuencia (espectrogramas), capturando patrones de correlación local mientras mantienen invarianza traslacional.

**Redes Recurrentes (RNN) y LSTM**: Procesan secuencias manteniendo estado oculto:

$$\mathbf{h}_t = \sigma(\mathbf{W}_{hh}\mathbf{h}_{t-1} + \mathbf{W}_{xh}\mathbf{x}_t + \mathbf{b}_h)$$

Las Long Short-Term Memory (LSTM) extienden RNNs con mecanismos de compuerta que mitigan el problema de gradientes que desaparecen:

$$\mathbf{f}_t = \sigma_g(\mathbf{W}_f\mathbf{x}_t + \mathbf{U}_f\mathbf{h}_{t-1} + \mathbf{b}_f)$$
$$\mathbf{i}_t = \sigma_g(\mathbf{W}_i\mathbf{x}_t + \mathbf{U}_i\mathbf{h}_{t-1} + \mathbf{b}_i)$$
$$\mathbf{o}_t = \sigma_g(\mathbf{W}_o\mathbf{x}_t + \mathbf{U}_o\mathbf{h}_{t-1} + \mathbf{b}_o)$$
$$\mathbf{c}_t = \mathbf{f}_t \odot \mathbf{c}_{t-1} + \mathbf{i}_t \odot \sigma_c(\mathbf{W}_c\mathbf{x}_t + \mathbf{U}_c\mathbf{h}_{t-1} + \mathbf{b}_c)$$
$$\mathbf{h}_t = \mathbf{o}_t \odot \sigma_h(\mathbf{c}_t)$$

donde $\mathbf{f}_t, \mathbf{i}_t, \mathbf{o}_t$ son compuertas de olvido, entrada y salida, y $\mathbf{c}_t$ es el estado de celda.

Las RNNs son ideales para estimación de canal variante en el tiempo y decodificación secuencial.

**Mecanismos de Atención y Transformers**: El mecanismo de atención permite a la red enfocarse dinámicamente en partes relevantes de la entrada:

$$\text{Attention}(\mathbf{Q}, \mathbf{K}, \mathbf{V}) = \text{softmax}\left(\frac{\mathbf{Q}\mathbf{K}^T}{\sqrt{d_k}}\right)\mathbf{V}$$

donde $\mathbf{Q}$ (queries), $\mathbf{K}$ (keys), y $\mathbf{V}$ (values) son proyecciones lineales de la entrada.

Los Transformers, basados completamente en atención multi-cabeza, han revolucionado el procesamiento de secuencias, superando RNNs en muchas tareas. Su aplicación a comunicaciones es promisoria para modelar dependencias de largo alcance en secuencias de símbolos y capturar patrones complejos de interferencia.

#### 2) Técnicas de Regularización y Generalización

**Dropout**: Durante el entrenamiento, neuronas se desactivan aleatoriamente con probabilidad $p$:

$$\mathbf{h}^{(l)} = \mathbf{m} \odot \sigma(\mathbf{W}\mathbf{h}^{(l-1)})$$

donde $\mathbf{m} \sim \text{Bernoulli}(1-p)$. Esto previene co-adaptación de características y funciona como ensamble implícito.

**Normalización por Lotes (Batch Normalization)**: Normaliza activaciones en cada mini-batch:

$$\hat{\mathbf{h}} = \frac{\mathbf{h} - \mu_{\mathcal{B}}}{\sqrt{\sigma^2_{\mathcal{B}} + \epsilon}}$$

seguido de transformación afín aprendible. BN acelera convergencia y permite tasas de aprendizaje más altas.

**Regularización de Peso**: Penalización L2 (weight decay):

$$\mathcal{L}_{\text{total}} = \mathcal{L}_{\text{data}} + \lambda \sum_{l} \|\mathbf{W}^{(l)}\|^2_F$$

reduce sobreajuste limitando la norma de parámetros.

**Data Augmentation**: Para comunicaciones, esto incluye augmentar datos de entrenamiento con:
- Variaciones de SNR
- Diferentes realizaciones de canal
- Offsets de frecuencia y temporización
- Interferencia sintética

#### 3) Optimización y Entrenamiento

**Descenso de Gradiente Estocástico (SGD)**: El algoritmo fundamental es:

$$\theta_{t+1} = \theta_t - \eta \nabla_{\theta}\mathcal{L}(\theta_t; \mathcal{B}_t)$$

donde $\eta$ es la tasa de aprendizaje y $\mathcal{B}_t$ es un mini-batch.

**Optimizadores Adaptativos**: Adam combina momentum y tasas de aprendizaje adaptativas por parámetro:

$$\mathbf{m}_t = \beta_1 \mathbf{m}_{t-1} + (1-\beta_1)\mathbf{g}_t$$
$$\mathbf{v}_t = \beta_2 \mathbf{v}_{t-1} + (1-\beta_2)\mathbf{g}_t^2$$
$$\hat{\mathbf{m}}_t = \frac{\mathbf{m}_t}{1-\beta_1^t}, \quad \hat{\mathbf{v}}_t = \frac{\mathbf{v}_t}{1-\beta_2^t}$$
$$\theta_{t+1} = \theta_t - \eta \frac{\hat{\mathbf{m}}_t}{\sqrt{\hat{\mathbf{v}}_t} + \epsilon}$$

**Retropropagación a través de Canales**: Un desafío específico de comunicaciones es diferenciar a través del canal. Para canales determinísticos $\mathbf{y} = h(\mathbf{x})$, la regla de la cadena se aplica directamente:

$$\frac{\partial \mathcal{L}}{\partial \theta} = \frac{\partial \mathcal{L}}{\partial \mathbf{y}} \frac{\partial h}{\partial \mathbf{x}} \frac{\partial \mathbf{x}}{\partial \theta}$$

Para canales estocásticos, se requiere el "reparametrization trick":

$$\mathbf{y} = h(\mathbf{x}, \epsilon), \quad \epsilon \sim p(\epsilon)$$

donde la aleatoriedad se hace explícita mediante $\epsilon$, permitiendo gradientes:

$$\nabla_{\theta}\mathbb{E}_{\epsilon}[\mathcal{L}] = \mathbb{E}_{\epsilon}[\nabla_{\theta}\mathcal{L}]$$

### D. Formulación del Problema de Optimización con Restricciones Físicas

#### 1) Restricción de Potencia

La potencia transmitida promedio debe satisfacer:

$$\mathbb{E}_{\mathbf{s}}[\|f_{\theta}(\mathbf{s})\|^2] \leq P$$

Esto se puede incorporar mediante:

**Normalización Explícita**: Forzar la salida del transmisor a tener potencia unitaria:

$$\tilde{f}_{\theta}(\mathbf{s}) = \sqrt{P} \frac{f_{\theta}(\mathbf{s})}{\|f_{\theta}(\mathbf{s})\|}$$

**Penalización en la Función de Pérdida**: Añadir un término de penalización:

$$\mathcal{L}_{\text{total}} = \mathcal{L}_{\text{error}} + \mu \max\left(0, \mathbb{E}_{\mathbf{s}}[\|f_{\theta}(\mathbf{s})\|^2] - P\right)^2$$

**Capa de Proyección**: Después del transmisor, aplicar una capa que proyecta sobre el conjunto de restricción de potencia.

#### 2) Restricción de Ancho de Banda

La señal transmitida debe estar limitada en banda. Para señales de banda base con ancho $W$:

$$\mathcal{F}\{f_{\theta}(\mathbf{s})\}(f) = 0, \quad |f| > W$$

Esto se puede imponer mediante:

**Conformación de Pulso**: Aplicar un filtro conformador $p(t)$ que limita banda:

$$s(t) = \sum_{i} x_i p(t - iT)$$

donde $p(t)$ es típicamente un pulso de Nyquist (ej. raised cosine).

**Implementación en el Dominio Frecuencial**: Entrenar el transmisor en el dominio frecuencial y multiplicar por una máscara que anula frecuencias fuera de banda.

#### 3) Restricción de Amplitud y Cuantización

Los amplificadores de potencia (PA) tienen rangos dinámicos limitados y operan más eficientemente cerca de saturación. Podemos modelar el PA mediante:

$$x_{\text{PA}} = g(x) = \begin{cases}
A_{\max} \frac{x}{|x|} & \text{si } |x| > A_{\max} \\
x & \text{en otro caso}
\end{cases}$$

Para incorporar esta no-linealidad en el entrenamiento:

$$\mathcal{L} = \mathbb{E}_{\mathbf{s}, \mathbf{n}}[\mathcal{L}_{\text{error}}(\mathbf{s}, g_{\phi}(h(g(f_{\theta}(\mathbf{s}))) + \mathbf{n}))]$$

La cuantización en transmisores digitales se modela como:

$$x_Q = Q(x) = \Delta \lfloor x/\Delta \rfloor$$

Para diferenciar, se usa el estimador "straight-through":

$$\frac{\partial Q(x)}{\partial x} \approx 1$$

durante la retropropagación, aunque la operación forward usa cuantización real.

#### 4) Incorporación de Información de Estado de Canal (CSI)

Cuando CSI está disponible en el transmisor, se puede condicionar la función del transmisor:

$$\mathbf{x} = f_{\theta}(\mathbf{s}, \mathbf{H})$$

donde $\mathbf{H}$ (o una representación comprimida) es entrada adicional. Esto permite precodificación adaptativa.

En el receptor, la CSI puede ser:

**Perfecta**: $\hat{\mathbf{s}} = g_{\phi}(\mathbf{y}, \mathbf{H})$

**Estimada**: $\hat{\mathbf{H}} = h_{\psi}(\mathbf{y}_{\text{pilot}})$, luego $\hat{\mathbf{s}} = g_{\phi}(\mathbf{y}, \hat{\mathbf{H}})$

**Ciega**: $\hat{\mathbf{s}} = g_{\phi}(\mathbf{y})$ (sin CSI explícita; la red infiere características del canal implícitamente)

### E. Análisis de Complejidad y Escalabilidad

#### 1) Complejidad Computacional

Para una red completamente conectada con $L$ capas, donde la capa $l$ tiene $n_l$ neuronas:

**Forward Pass**: $\mathcal{O}\left(\sum_{l=1}^{L-1} n_l n_{l+1}\right)$ operaciones

**Backward Pass**: Misma complejidad asintótica que forward pass

Para CNNs con $L$ capas convolucionales, donde la capa $l$ tiene $C_l$ canales y kernels de tamaño $k \times k$:

$$\mathcal{O}\left(\sum_{l=1}^{L} C_{l-1} C_l k^2 H_l W_l\right)$$

donde $H_l \times W_l$ es el tamaño espacial en la capa $l$.

Para RNNs procesando secuencia de longitud $T$ con $n$ unidades ocultas:

$$\mathcal{O}(T n^2)$$

#### 2) Complejidad de Memoria

Durante entrenamiento, se almacenan:
- Parámetros del modelo: $\mathcal{O}(|\theta| + |\phi|)$
- Activaciones intermedias (para backprop): $\mathcal{O}(|\text{batch size}| \times |\text{activaciones}|)$
- Gradientes: $\mathcal{O}(|\theta| + |\phi|)$

Técnicas como gradient checkpointing reducen memoria a costa de recomputación.

#### 3) Comparación con Métodos Tradicionales

**Decodificación Turbo**: Complejidad $\mathcal{O}(n \cdot I \cdot S)$ donde $n$ es longitud de bloque, $I$ iteraciones, $S$ estados del trellis.

**Detección ML para MIMO**: Complejidad $\mathcal{O}(M^{N_t})$ donde $M$ es tamaño de constelación y $N_t$ antenas transmisoras. Intratable para $M, N_t$ grandes.

**Red Neuronal de Detección**: Complejidad $\mathcal{O}(n^2)$ para red completamente conectada, o $\mathcal{O}(n)$ para arquitecturas eficientes. Escalabilidad dramáticamente mejor.

---

## III. COMPONENTES DEL NIVEL FÍSICO CON IA NATIVA

### A. Codificación de Canal Neural

#### 1) Fundamentos y Motivación

La codificación de canal añade redundancia controlada a la información para permitir detección y corrección de errores introducidos por el canal. Los códigos clásicos (Hamming, BCH, Reed-Solomon, Turbo, LDPC, Polar) están diseñados mediante construcciones algebraicas o aleatorias con propiedades matemáticas demostrables.

Sin embargo, estos códigos:
- Están optimizados para modelos de canal específicos (típicamente AWGN)
- Tienen complejidad de decodificación alta (ej. belief propagation para LDPC)
- No adaptan su estructura a condiciones variables del canal

La **codificación neural** propone aprender el código directamente de datos, potencialmente descubriendo estructuras no contempladas en diseños tradicionales.

#### 2) Arquitectura de Autoencoder para Codificación

Consideremos un autoencoder de comunicación con:

**Encoder (Transmisor)**:
$$\mathbf{x} = f_{\text{enc}}(\mathbf{s}; \theta) : \{1, \ldots, M\} \rightarrow \mathbb{R}^{n}$$

donde $\mathbf{s}$ es uno de $M$ mensajes posibles, y $\mathbf{x}$ es la señal transmitida de dimensión $n$.

**Normalización de Potencia**:
$$\tilde{\mathbf{x}} = \sqrt{n} \frac{\mathbf{x}}{\|\mathbf{x}\|}$$

garantizando potencia unitaria por símbolo.

**Canal**:
$$\mathbf{y} = \tilde{\mathbf{x}} + \mathbf{n}, \quad \mathbf{n} \sim \mathcal{N}(0, \sigma^2 \mathbf{I})$$

**Decoder (Receptor)**:
$$\hat{\mathbf{s}} = f_{\text{dec}}(\mathbf{y}; \phi) : \mathbb{R}^{n} \rightarrow \{1, \ldots, M\}$$

**Función de Pérdida**:
$$\mathcal{L}(\theta, \phi) = \mathbb{E}_{\mathbf{s} \sim \text{Uniform}(\{1,\ldots,M\}), \mathbf{n} \sim \mathcal{N}(0,\sigma^2\mathbf{I})} \left[ -\log p_{\phi}(\mathbf{s}|\mathbf{y}) \right]$$

Esto es equivalente a minimizar la entropía cruzada categórica.

#### 3) Arquitecturas de Red Específicas

**Encoder MLP**:
```
Input: one-hot encoded message [M dimensiones]
↓
Dense layer [128 unidades, ReLU]
↓
Dense layer [64 unidades, ReLU]
↓
Output layer [n dimensiones, lineal]
↓
Normalización de potencia
```

**Decoder MLP**:
```
Input: señal recibida [n dimensiones]
↓
Dense layer [64 unidades, ReLU]
↓
Dense layer [128 unidades, ReLU]
↓
Output layer [M unidades, softmax]
```

Para explotar estructura temporal en códigos secuenciales:

**Encoder RNN**:
```
Input: secuencia de bits [k bits]
↓
Embedding layer
↓
LSTM [128 unidades ocultas]
↓
Dense [n dimensiones]
↓
Normalización de potencia
```

**Decoder RNN con Atención**:
```
Input: señal recibida [n dimensiones]
↓
LSTM encoder [128 unidades]
↓
Atención sobre estados del encoder
↓
LSTM decoder [128 unidades]
↓
Dense [k bits, sigmoid]
```

#### 4) Análisis Teórico de Rendimiento

**Tasa de Código**: $R = \frac{\log_2 M}{n}$ bits por canal.

**Eficiencia Espectral**: Para una probabilidad de error objetivo $P_e^*$, la SNR mínima requerida define la eficiencia.

La distancia mínima entre señales en el espacio de señal:
$$d_{\min} = \min_{i \neq j} \|\tilde{\mathbf{x}}_i - \tilde{\mathbf{x}}_j\|$$

está relacionada con la probabilidad de error mediante:
$$P_e \approx M Q\left(\frac{d_{\min}}{2\sigma}\right)$$

Durante el entrenamiento, la red implícitamente maximiza $d_{\min}$ sujeto a restricciones de potencia.

**Comparación con Límite de Shannon**: Para canal AWGN, capacidad $C = \frac{1}{2}\log_2(1 + \text{SNR})$.

La brecha respecto al límite de Shannon:
$$\text{Gap (dB)} = 10\log_{10}\left(\frac{\text{SNR}_{\text{requerido}}}{\text{SNR}_{\text{Shannon}}}\right)$$

Códigos Turbo y LDPC alcanzan gaps < 1 dB. Los autoencoders neuronales, para longitudes de bloque cortas ($n < 50$), han demostrado rendimiento competitivo o superior.

#### 5) Códigos Neurales para Canales con Desvanecimiento

Para canales Rayleigh:
$$\mathbf{y} = \mathbf{H} \tilde{\mathbf{x}} + \mathbf{n}$$

donde $\mathbf{H}$ es diagonal con entradas $\sim \mathcal{CN}(0, 1)$.

El autoencoder se entrena con realiz aciones aleatorias de $\mathbf{H}$:

$$\mathcal{L} = \mathbb{E}_{\mathbf{s}, \mathbf{H}, \mathbf{n}} \left[ -\log p_{\phi}(\mathbf{s}|\mathbf{H}\tilde{\mathbf{x}} + \mathbf{n}) \right]$$

La red aprende representaciones robustas al desvanecimiento, potencialmente descubriendo estrategias de diversidad implícitas.

#### 6) Codificación Neural con Información Lateral

Cuando metadata está disponible (ej. estimación de calidad de canal, tipo de contenido), se puede condicionar el encoder:

$$\mathbf{x} = f_{\text{enc}}(\mathbf{s}, \mathbf{c}; \theta)$$

donde $\mathbf{c}$ es información contextual.

Ejemplo: transmisión de video donde $\mathbf{c}$ indica importancia del frame (I-frame vs. P-frame). El encoder aprende asignar más protección (menor tasa) a contenido crítico.

### B. Estimación de Canal con Aprendizaje Profundo

#### 1) Formulación del Problema

El canal inalámbrico introduce distorsión desconocida que debe estimarse para ecualización y decodificación. Tradicionalmente, se transmiten secuencias piloto conocidas:

$$\mathbf{y}_p = \mathbf{H}\mathbf{x}_p + \mathbf{n}_p$$

donde $\mathbf{x}_p$ es conocido. El receptor estima $\hat{\mathbf{H}}$ mediante:

**Least Squares**:
$$\hat{\mathbf{H}}_{\text{LS}} = \mathbf{y}_p \mathbf{x}_p^H (\mathbf{x}_p \mathbf{x}_p^H)^{-1}$$

**Minimum Mean Square Error (MMSE)**:
$$\hat{\mathbf{H}}_{\text{MMSE}} = \mathbf{R}_{H y_p} \mathbf{R}_{y_p y_p}^{-1} \mathbf{y}_p$$

donde $\mathbf{R}_{H y_p}$ y $\mathbf{R}_{y_p y_p}$ son matrices de covarianza que requieren conocimiento estadístico del canal.

**Limitaciones**:
- LS no explota correlación espacial/temporal del canal
- MMSE requiere estadísticas de segundo orden exactas
- Ambos asumen linealidad y modelos gaussianos

#### 2) Estimación Neural de Canal con CNNs

El canal en sistemas OFDM puede representarse en tiempo-frecuencia como una imagen 2D. Una CNN puede aprender a estimar:

$$\hat{\mathbf{H}} = f_{\text{CNN}}(\mathbf{y}_p; \theta)$$

**Arquitectura U-Net para Estimación**:
```
Input: señal piloto [N_subcarriers × N_symbols]
↓
Encoder:
  Conv2D [32 filters, 3×3, ReLU] + MaxPool
  Conv2D [64 filters, 3×3, ReLU] + MaxPool
  Conv2D [128 filters, 3×3, ReLU] + MaxPool
↓
Bottleneck:
  Conv2D [256 filters, 3×3, ReLU]
↓
Decoder:
  UpConv [128 filters, 3×3, ReLU] + skip connection
  UpConv [64 filters, 3×3, ReLU] + skip connection
  UpConv [32 filters, 3×3, ReLU] + skip connection
↓
Output: estimación de canal [N_subcarriers × N_symbols, compleja]
```

Las skip connections preservan detalles de alta frecuencia.

**Función de Pérdida**:
$$\mathcal{L} = \mathbb{E}_{\mathbf{H}, \mathbf{n}} \left[ \|\mathbf{H} - \hat{\mathbf{H}}\|^2_F \right]$$

o alternativamente, una pérdida perceptual que penaliza errores en regiones críticas.

#### 3) Estimación con Redes Recurrentes (LSTM)

Para canales variantes en el tiempo, las observaciones piloto en tiempos consecutivos $t = 1, \ldots, T$ forman una secuencia:

$$\mathbf{y}_{p,t} = \mathbf{H}_t \mathbf{x}_p + \mathbf{n}_{p,t}$$

Una LSTM bidireccional procesa la secuencia:

$$\overrightarrow{\mathbf{h}}_t = \text{LSTM}_{\text{fwd}}(\mathbf{y}_{p,t}, \overrightarrow{\mathbf{h}}_{t-1})$$
$$\overleftarrow{\mathbf{h}}_t = \text{LSTM}_{\text{bwd}}(\mathbf{y}_{p,t}, \overleftarrow{\mathbf{h}}_{t+1})$$
$$\hat{\mathbf{H}}_t = f_{\text{out}}([\overrightarrow{\mathbf{h}}_t; \overleftarrow{\mathbf{h}}_t])$$

Esto captura dependencias temporales y realiza suavizado (smoothing) implícito.

**Función de Pérdida Temporal**:
$$\mathcal{L} = \sum_{t=1}^{T} \|\mathbf{H}_t - \hat{\mathbf{H}}_t\|^2_F + \lambda \sum_{t=1}^{T-1} \|\hat{\mathbf{H}}_{t+1} - \hat{\mathbf{H}}_t\|^2_F$$

El segundo término penaliza discontinuidades temporales, incorporando conocimiento previo sobre la suavidad del canal.

#### 4) Estimación Ciega y Semi-Ciega

En escenarios donde el overhead de pilotos es prohibitivo, se puede entrenar una red para estimar el canal usando solo datos:

$$\hat{\mathbf{H}} = f_{\theta}(\mathbf{y}_{\text{data}})$$

Sin embargo, esto enfrenta el problema de ambigüedad (el canal y los símbolos datos son ambos desconocidos).

**Aproximación Semi-Ciega con Decodificación Iterativa**:
1. Estimación inicial con pilotos escasos: $\hat{\mathbf{H}}^{(0)} = f_{\theta}(\mathbf{y}_p)$
2. Decodificación tentativa: $\hat{\mathbf{x}}^{(1)} = g_{\phi}(\mathbf{y}_{\text{data}}, \hat{\mathbf{H}}^{(0)})$
3. Re-estimación del canal: $\hat{\mathbf{H}}^{(1)} = f_{\theta}([\mathbf{y}_p; \mathbf{y}_{\text{data}}], \hat{\mathbf{x}}^{(1)})$
4. Iterar hasta convergencia

#### 5) Incorporación de Geometría y Física del Canal

Los canales inalámbricos tienen estructura inherente derivada de la propagación electromagnética. Modelos paramétricos (ej. ray-tracing) capturan esto, pero son computacionalmente costosos.

**Redes Informadas por Física (Physics-Informed Neural Networks)**:

Incorporar la ecuación de actualización del canal en la arquitectura. Para canales con modelo de espacio de estados:

$$\mathbf{H}_{t+1} = \mathbf{A} \mathbf{H}_t + \mathbf{w}_t$$

donde $\mathbf{A}$ es matriz de transición y $\mathbf{w}_t$ ruido de proceso.

La red predice:
$$\hat{\mathbf{H}}_{t+1} = f_{\theta}(\hat{\mathbf{H}}_t, \mathbf{y}_{p,t+1}) + \mathbf{A}\hat{\mathbf{H}}_t$$

forzando consistencia con el modelo físico mientras aprende correcciones de datos.

#### 6) Estimación de Canal para Comunicaciones MIMO Masivo

En MIMO masivo ($N_t, N_r \gg 1$), la matriz de canal $\mathbf{H} \in \mathbb{C}^{N_r \times N_t}$ tiene dimensión muy alta. Sin embargo, en bandas de frecuencia sub-6 GHz, el canal tiene estructura de bajo rango debido a dispersión limitada:

$$\mathbf{H} = \sum_{l=1}^{L} \alpha_l \mathbf{a}_r(\theta_l) \mathbf{a}_t(\phi_l)^H$$

donde $L \ll \min(N_t, N_r)$, $\alpha_l$ son ganancias complejas, y $\mathbf{a}_r, \mathbf{a}_t$ son vectores de respuesta de antena.

**Autoencoder de Compresión de Canal**:

Encoder: comprime CSI de alta dimensión:
$$\mathbf{z} = f_{\text{enc}}(\mathbf{H}; \theta) \in \mathbb{R}^{d}, \quad d \ll N_r N_t$$

Decoder: reconstruye CSI:
$$\hat{\mathbf{H}} = f_{\text{dec}}(\mathbf{z}; \phi)$$

Entrenado con:
$$\mathcal{L} = \mathbb{E}_{\mathbf{H}} [\|\mathbf{H} - \hat{\mathbf{H}}\|^2_F]$$

La representación comprimida $\mathbf{z}$ puede retroalimentarse al transmisor con overhead reducido.

### C. Detección de Señales Multi-Usuario

#### 1) Formulación del Problema de Detección

En sistemas multi-usuario MIMO, múltiples transmisores envían simultáneamente:

$$\mathbf{y} = \sum_{k=1}^{K} \mathbf{H}_k \mathbf{x}_k + \mathbf{n} = \mathbf{H}\mathbf{x} + \mathbf{n}$$

donde $\mathbf{H} = [\mathbf{H}_1, \ldots, \mathbf{H}_K]$ y $\mathbf{x} = [\mathbf{x}_1^T, \ldots, \mathbf{x}_K^T]^T$.

**Detección ML (Maximum Likelihood)**:
$$\hat{\mathbf{x}}_{\text{ML}} = \arg\min_{\mathbf{x} \in \mathcal{X}^K} \|\mathbf{y} - \mathbf{H}\mathbf{x}\|^2$$

donde $\mathcal{X}$ es la constelación. La complejidad es $\mathcal{O}(|\mathcal{X}|^K)$, intratable para $K$ grande.

**Detecciones Subóptimas**:
- **Zero-Forcing (ZF)**: $\hat{\mathbf{x}}_{\text{ZF}} = (\mathbf{H}^H\mathbf{H})^{-1}\mathbf{H}^H\mathbf{y}$
- **MMSE**: $\hat{\mathbf{x}}_{\text{MMSE}} = (\mathbf{H}^H\mathbf{H} + \sigma^2\mathbf{I})^{-1}\mathbf{H}^H\mathbf{y}$

Ambos tienen complejidad $\mathcal{O}(K^3)$ pero rendimiento subóptimo, especialmente en alta carga ($K$ cercano a $N_r$).

#### 2) Redes Neuronales para Aproximar Detección ML

Entrenar una red neuronal para aproximar el detector ML:

$$\hat{\mathbf{x}} = f_{\text{NN}}(\mathbf{y}, \mathbf{H}; \theta)$$

**Arquitectura DetNet**:
```
Input: [y; vec(H)]
↓
Concatenación y normalización
↓
L bloques residuales:
  Dense [2K unidades, ReLU]
  + skip connection
↓
Output: símbolos detectados [K usuarios]
```

**Función de Pérdida**:
$$\mathcal{L} = \mathbb{E}_{\mathbf{x}, \mathbf{H}, \mathbf{n}} \left[ \|\mathbf{x} - \hat{\mathbf{x}}\|^2 \right]$$

o para símbolos discretos:
$$\mathcal{L} = \mathbb{E}_{\mathbf{x}, \mathbf{H}, \mathbf{n}} \left[ \sum_{k=1}^{K} \text{CrossEntropy}(\mathbf{x}_k, \hat{\mathbf{x}}_k) \right]$$

**Rendimiento**: Para $K=8$ usuarios, $N_r=16$ antenas, QPSK, DetNet alcanza BER cercana a ML con complejidad $\mathcal{O}(K)$ por forward pass.

#### 3) Desenrollado de Algoritmos (Algorithm Unrolling)

En lugar de entrenar una red de caja negra, se pueden "desenrollar" iteraciones de algoritmos clásicos, haciendo los parámetros aprendibles.

**Ejemplo: Desenrollar ISTA (Iterative Soft Thresholding)**:

El problema de detección con regularización sparse:
$$\min_{\mathbf{x}} \|\mathbf{y} - \mathbf{H}\mathbf{x}\|^2 + \lambda \|\mathbf{x}\|_1$$

se resuelve iterativamente:
$$\mathbf{x}^{(t+1)} = \mathcal{S}_{\lambda\alpha}(\mathbf{x}^{(t)} - \alpha \mathbf{H}^H(\mathbf{H}\mathbf{x}^{(t)} - \mathbf{y}))$$

donde $\mathcal{S}_{\tau}$ es el operador de soft-thresholding.

**Versión Aprendible (LISTA - Learned ISTA)**:
$$\mathbf{x}^{(t+1)} = \mathcal{S}_{\theta^{(t)}}(\mathbf{W}^{(t)}_1 \mathbf{x}^{(t)} + \mathbf{W}^{(t)}_2 \mathbf{y})$$

donde $\mathbf{W}^{(t)}_1, \mathbf{W}^{(t)}_2, \theta^{(t)}$ son parámetros aprendibles por capa.

Desenrollar $T$ iteraciones crea una red de $T$ capas. El entrenamiento optimiza los parámetros para minimizar:
$$\mathcal{L} = \mathbb{E}\left[\|\mathbf{x} - \mathbf{x}^{(T)}\|^2\right]$$

**Ventajas**:
- Convergencia más rápida (menos iteraciones $T$)
- Mejor rendimiento que algoritmo original
- Interpretabilidad (estructura refleja algoritmo base)

#### 4) Detección con Aprendizaje por Refuerzo

Formular la detección como un problema de decisión secuencial. Un agente RL selecciona acciones (candidatos de símbolos) para maximizar recompensa (probabilidad de log-verosimilitud).

**Estado**: $s_t = (\mathbf{y}, \mathbf{H}, \hat{\mathbf{x}}_{1:t-1})$ (observación y decisiones previas)

**Acción**: $a_t = \hat{x}_t \in \mathcal{X}$ (símbolo del usuario $t$)

**Recompensa**: $r_t = -\|\mathbf{y} - \mathbf{H}\hat{\mathbf{x}}_{1:t}\|^2$

**Política**: $\pi_{\theta}(a_t | s_t)$ parametrizada por red neuronal

El agente se entrena con algoritmos como PPO o A3C para maximizar retorno acumulado.

Esta aproximación es particularmente útil cuando el orden de detección importa (ej. SIC - Successive Interference Cancellation).

### D. Beamforming y Conformación de Haces Inteligente

#### 1) Fundamentos de Beamforming en MIMO

Beamforming ajusta las fases y amplitudes de señales en un arreglo de antenas para dirigir la energía hacia usuarios deseados y crear nulos hacia interferencia.

**Precodificador en el Transmisor**:
$$\mathbf{x} = \mathbf{W}\mathbf{s}$$

donde $\mathbf{s} \in \mathbb{C}^{K}$ son símbolos para $K$ usuarios, $\mathbf{W} \in \mathbb{C}^{N_t \times K}$ es la matriz de beamforming.

**Señal Recibida por Usuario $k$**:
$$y_k = \mathbf{h}_k^H \mathbf{W} \mathbf{s} + n_k = \mathbf{h}_k^H \mathbf{w}_k s_k + \sum_{j \neq k} \mathbf{h}_k^H \mathbf{w}_j s_j + n_k$$

**Problema de Optimización**: Maximizar tasa suma sujeto a restricción de potencia:

$$\max_{\mathbf{W}} \sum_{k=1}^{K} \log_2\left(1 + \frac{|\mathbf{h}_k^H \mathbf{w}_k|^2}{\sum_{j \neq k} |\mathbf{h}_k^H \mathbf{w}_j|^2 + \sigma^2}\right)$$
sujeto a: $\|\mathbf{W}\|^2_F \leq P$

Este problema es no-convexo y NP-hard en general.

**Soluciones Clásicas**:
- **Zero-Forcing Beamforming**: $\mathbf{W}_{\text{ZF}} = \mathbf{H}^H(\mathbf{H}\mathbf{H}^H)^{-1}$
- **MMSE Beamforming**: incorpora estadísticas de ruido
- **Weighted MMSE (WMMSE)**: algoritmo iterativo que converge a óptimo local

#### 2) Beamforming Neural de Caja Negra

Entrenar una red neuronal para mapear CSI a vectores de beamforming:

$$\mathbf{W} = f_{\theta}(\mathbf{H})$$

**Arquitectura**:
```
Input: CSI matrix H [N_r × N_t × K, compleja]
↓
Reshape a [2·N_r·N_t·K] (real/imaginario)
↓
Dense [512, ReLU]
↓
Dense [256, ReLU]
↓
Output [2·N_t·K] → reshape a [N_t × K, compleja]
↓
Normalización de potencia
```

**Función de Pérdida**: Negativo de la tasa suma:
$$\mathcal{L} = -\mathbb{E}_{\mathbf{H}} \left[ \sum_{k=1}^{K} \log_2\left(1 + \text{SINR}_k(\mathbf{W})\right) \right]$$

El gradiente respecto a $\theta$ se calcula mediante retropropagación a través del cálculo de SINR.

#### 3) Beamforming con Desenrollado de WMMSE

El algoritmo WMMSE itera:
1. **MSE Weights**: $u_k = \frac{1}{1 + \text{SINR}_k}$
2. **Receive Combining**: $\mathbf{g}_k = \frac{\mathbf{h}_k^H \mathbf{w}_k}{...}$
3. **Transmit Beamforming**: $\mathbf{w}_k = (\sum_j u_j |\mathbf{g}_j|^2 \mathbf{h}_j \mathbf{h}_j^H + \mu \mathbf{I})^{-1} u_k \mathbf{g}_k^* \mathbf{h}_k$

**Versión Desenrollada**: Cada paso tiene parámetros aprendibles:
$$u_k^{(t)} = f_u^{(t)}(\text{SINR}_k; \theta_u^{(t)})$$
$$\mathbf{g}_k^{(t)} = f_g^{(t)}(\mathbf{h}_k, \mathbf{W}^{(t)}; \theta_g^{(t)})$$
$$\mathbf{W}^{(t+1)} = f_w^{(t)}(\{\mathbf{g}_k^{(t)}\}, \{\mathbf{h}_k\}, \{u_k^{(t)}\}; \theta_w^{(t)})$$

Esto acelera convergencia (menos iteraciones $T$) y mejora rendimiento final.

#### 4) Beamforming con Aprendizaje por Refuerzo Multi-Agente

En redes densas con múltiples celdas, las decisiones de beamforming están acopladas. Formular como juego multi-agente donde cada BS es un agente.

**Estado del Agente $i$**: $s_i = (\mathbf{H}_i, \mathbf{W}_{-i}, \text{interferencia medida})$

**Acción**: $a_i = \mathbf{W}_i$ (matriz de beamforming)

**Recompensa**: $r_i = \sum_{k \in \mathcal{U}_i} \log_2(1 + \text{SINR}_k)$ (tasa suma de usuarios de la celda $i$)

Los agentes aprenden políticas $\pi_{\theta_i}(a_i | s_i)$ mediante MADDPG (Multi-Agent DDPG) o algoritmos similares.

**Coordinación Descentralizada**: Cada BS ejecuta su política localmente, pero las políticas se entrenan centralizadamente con información global, permitiendo aprender coordinación implícita.

#### 5) Beamforming con Restricciones de Hardware

Los beamformers analógicos (phased arrays) solo pueden ajustar fases, no amplitudes:

$$w_i = \frac{1}{\sqrt{N_t}} e^{j\phi_i}, \quad \phi_i \in [0, 2\pi)$$

**Red Neuronal para Beamforming de Solo Fase**:

Output de la red pasa por:
$$\mathbf{w} = \frac{1}{\sqrt{N_t}} e^{j \cdot \text{tanh}(\mathbf{z}) \cdot \pi}$$

donde $\mathbf{z}$ es la salida de la red, y $\text{tanh}$ mapea a $[-1, 1]$, luego escalado a $[-\pi, \pi]$.

#### 6) Beamforming Predictivo

En escenarios de alta movilidad, el CSI está desactualizado. Entrenar una red para predecir CSI futura:

$$\hat{\mathbf{H}}_{t+\Delta} = f_{\text{pred}}(\mathbf{H}_{t-T:t}; \theta)$$

usando RNN o Transformer sobre secuencia histórica. Luego aplicar beamforming sobre $\hat{\mathbf{H}}_{t+\Delta}$:

$$\mathbf{W}_{t+\Delta} = f_{\text{BF}}(\hat{\mathbf{H}}_{t+\Delta}; \phi)$$

### E. Gestión de Recursos Radio con IA

#### 1) Problema de Asignación de Recursos

La gestión de recursos incluye:
- **Asignación de Potencia**: determinar potencia de transmisión por usuario/subportadora
- **Scheduling**: decidir qué usuarios transmiten en cada time slot
- **Asignación Espectral**: asignar bloques de recursos frecuenciales

**Formulación General**:
$$\max_{\mathbf{p}, \mathbf{a}} \sum_{k=1}^{K} w_k R_k(\mathbf{p}, \mathbf{a})$$
sujeto a:
$$\sum_{k} p_k \leq P_{\text{total}}$$
$$\sum_{k} a_{k,n} \leq 1, \quad \forall n \quad \text{(cada RB a un usuario)}$$
$$R_k \geq R_k^{\min} \quad \text{(QoS)}$$

donde $\mathbf{p} = [p_1, \ldots, p_K]$ son potencias, $\mathbf{a} = [a_{k,n}]$ son indicadores de asignación, y $R_k$ es la tasa del usuario $k$.

Este problema es un MILP (Mixed Integer Linear Program) NP-hard.

#### 2) Aprendizaje por Refuerzo para Scheduling

Formular como MDP:

**Estado**: $s_t = (\{\text{buffer status}_k\}, \{\text{channel quality}_k\}, \{R_k\})$

**Acción**: $a_t = \{k_1, \ldots, k_N\}$ (usuarios programados en $N$ recursos)

**Recompensa**: 
$$r_t = \sum_{k \in a_t} R_k - \lambda \sum_{k} \max(0, B_k - B_{\max}) - \mu \text{Jain's Fairness Index}$$

penalizando overflow de buffer y promoviendo equidad.

**Algoritmo DQN (Deep Q-Network)**:

Red neuronal aproxima función Q:
$$Q(s, a; \theta) \approx \mathbb{E}[r_t + \gamma \max_{a'} Q(s', a'; \theta)]$$

Entrenada con experiencia replay y target network para estabilidad.

#### 3) Graph Neural Networks para Gestión Multi-Celda

La topología de red puede representarse como grafo $\mathcal{G} = (\mathcal{V}, \mathcal{E})$ donde vértices son BSs/usuarios y aristas representan interferencia.

**Graph Convolutional Network (GCN)**:

Para vértice $v$ con características $\mathbf{h}_v^{(0)}$:

$$\mathbf{h}_v^{(l+1)} = \sigma\left(\sum_{u \in \mathcal{N}(v)} \frac{1}{\sqrt{|\mathcal{N}(v)||\mathcal{N}(u)|}} \mathbf{W}^{(l)} \mathbf{h}_u^{(l)}\right)$$

Después de $L$ capas, cada vértice tiene representación que agrega información de vecindad $L$-hop.

**Aplicación a Gestión de Potencia**:

Input: características de cada usuario (CSI, QoS)
↓
GCN [L capas]
↓
Output: nivel de potencia óptimo por usuario

Entrenado end-to-end para maximizar tasa suma o métrica de equidad.

**Ventajas**:
- Escalabilidad (complejidad lineal en número de nodos)
- Generalización a topologías de red variables
- Explota estructura de interferencia del problema

#### 4) Asignación de Espectro con Técnicas de Juegos

Formular como juego no-cooperativo donde cada BS es un jugador maximizando su utilidad:

$$u_i(\mathbf{p}_i, \mathbf{p}_{-i}) = \sum_{k \in \mathcal{U}_i} R_k(\mathbf{p})$$

**Nash Equilibrium**: perfil de potencia $\mathbf{p}^*$ donde ningún jugador puede mejorar unilateralmente.

**Learning Nash Equilibria con NNs**:

Cada agente tiene política $\pi_i(\mathbf{p}_i | s_i; \theta_i)$. Entrenar mediante:
- Self-play: agentes juegan entre sí iterativamente
- Fictitious play: cada agente mejor responde a distribución empírica de oponentes
- Policy gradient: maximizar utilidad esperada

Convergencia a equilibrio depende de propiedades del juego (existencia, unicidad).

---

## IV. ARQUITECTURAS DE SISTEMAS END-TO-END

### A. Autoencoders de Comunicación Completos

#### 1) Diseño End-to-End sin Separación de Componentes

La visión más radical de IA nativa elimina completamente la separación tradicional en bloques, optimizando el sistema completo end-to-end:

$$(\theta^*, \phi^*) = \arg\min_{\theta, \phi} \mathbb{E}_{\mathbf{s}, \mathbf{H}, \mathbf{n}} [\mathcal{L}(\mathbf{s}, g_{\phi}(h_{\mathbf{H}}(f_{\theta}(\mathbf{s})) + \mathbf{n}))]$$

**Ventajas Teóricas**:
- Optimalidad global (no garantizada con optimización por bloques)
- Descubrimiento de esquemas no convencionales
- Adaptación implícita a características del canal

**Desafíos**:
- Requiere diferenciabilidad del canal (simulador o modelo aprendido)
- Espacio de búsqueda enorme (millones de parámetros)
- Riesgo de sobreajuste a distribución de entrenamiento
- Falta de interpretabilidad

#### 2) Implementación con Capa de Canal Diferenciable

**Canal AWGN**: directamente diferenciable:
$$\frac{\partial \mathbf{y}}{\partial \mathbf{x}} = \mathbf{I}$$

**Canal Rayleigh**: con reparametrización:
$$\mathbf{y} = \mathbf{H}(\epsilon_H) \mathbf{x} + \mathbf{n}(\epsilon_n)$$
donde $\epsilon_H, \epsilon_n$ son fuentes de aleatoriedad independientes de parámetros.

**Canal Complejo (Ray-Tracing)**: entrenar un "canal surrogate" neuronal:
$$\tilde{h}_{\psi}(\mathbf{x}) \approx h_{\text{true}}(\mathbf{x})$$

usando datos de simulaciones físicas, luego usar $\tilde{h}_{\psi}$ en el bucle de entrenamiento.

#### 3) Arquitectura de Ejemplo: Autoencoder para Canal MIMO

```python
# Pseudo-código conceptual

class TransmitterNN(nn.Module):
    def __init__(self, M, n_channel, N_t):
        # M: número de mensajes
        # n_channel: dimensión de representación intermedia
        # N_t: antenas transmisoras
        self.embedding = nn.Embedding(M, 128)
        self.encoder = nn.Sequential(
            nn.Linear(128, 256), nn.ReLU(),
            nn.Linear(256, 512), nn.ReLU(),
            nn.Linear(512, n_channel * N_t * 2)  # *2 para I/Q
        )
        
    def forward(self, message):
        x = self.embedding(message)
        x = self.encoder(x)
        x = x.view(-1, N_t, n_channel, 2)
        x_complex = torch.complex(x[..., 0], x[..., 1])
        # Normalización de potencia
        power = torch.mean(torch.abs(x_complex)**2, dim=(1,2), keepdim=True)
        x_norm = x_complex / torch.sqrt(power) * torch.sqrt(torch.tensor(n_channel))
        return x_norm

class ReceiverNN(nn.Module):
    def __init__(self, n_channel, N_r, M):
        self.decoder = nn.Sequential(
            nn.Linear(N_r * n_channel * 2, 512), nn.ReLU(),
            nn.Linear(512, 256), nn.ReLU(),
            nn.Linear(256, 128), nn.ReLU(),
            nn.Linear(128, M)  # Logits para M mensajes
        )
        
    def forward(self, y):
        y_real = torch.cat([y.real, y.imag], dim=-1).flatten(1)
        logits = self.decoder(y_real)
        return logits

# Entrenamiento
transmitter = TransmitterNN(M=16, n_channel=7, N_t=4)
receiver = ReceiverNN(n_channel=7, N_r=4, M=16)
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(list(transmitter.parameters()) + 
                              list(receiver.parameters()), lr=1e-3)

for epoch in range(num_epochs):
    messages = torch.randint(0, M, (batch_size,))
    x = transmitter(messages)
    
    # Canal MIMO Rayleigh
    H = (torch.randn(batch_size, N_r, N_t) + 
         1j*torch.randn(batch_size, N_r, N_t)) / np.sqrt(2)
    noise = (torch.randn(batch_size, N_r, n_channel) + 
             1j*torch.randn(batch_size, N_r, n_channel)) * noise_std
    y = torch.einsum('bji,bic->bjc', H, x) + noise
    
    logits = receiver(y)
    loss = criterion(logits, messages)
    
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
```

#### 4) Análisis de Convergencia y Estabilidad

La optimización end-to-end puede sufrir inestabilidades:

**Problema de Convergencia**: El transmisor puede aprender representaciones que "explotan" artefactos del modelo de canal en lugar de desarrollar robustez genuina.

**Solución - Adversarial Training**: Introducir un discriminador que distingue entre canales reales y simulados:

$$\mathcal{L}_{\text{total}} = \mathcal{L}_{\text{comm}} + \lambda \mathcal{L}_{\text{adv}}$$

donde:
$$\mathcal{L}_{\text{adv}} = -\log D_{\omega}(h_{\text{real}}(\mathbf{x})) - \log(1 - D_{\omega}(h_{\text{sim}}(\mathbf{x})))$$

forzando al sistema a ser robusto a discrepancias entre simulación y realidad.

### B. Codificación Conjunta Fuente-Canal Neural

#### 1) Motivación y Fundamentos

Como se discutió en la Sección II-B-4, la separación fuente-canal es subóptima en muchos escenarios prácticos. Para transmisión de imágenes/video, JSCC neural puede superar cascadas tradicionales (JPEG/H.264 + códigos de canal).

#### 2) Arquitectura para Transmisión de Imágenes

**Encoder (Transmisor)**:
```
Input: imagen [H × W × 3]
↓
CNN Encoder:
  Conv2D [64 filters, 3×3, stride 2, ReLU] → H/2 × W/2
  Conv2D [128 filters, 3×3, stride 2, ReLU] → H/4 × W/4
  Conv2D [256 filters, 3×3, stride 2, ReLU] → H/8 × W/8
↓
Flattening y Dense: → [n dimensiones]
↓
Conformación de pulso y normalización de potencia
↓
Salida: señal para canal [n símbolos complejos]
```

**Decoder (Receptor)**:
```
Input: señal recibida [n símbolos complejos]
↓
Dense: → [256 * H/8 * W/8]
↓
Reshape: → [H/8 × W/8 × 256]
↓
CNN Decoder:
  TransposedConv2D [128 filters, 3×3, stride 2, ReLU] → H/4 × W/4
  TransposedConv2D [64 filters, 3×3, stride 2, ReLU] → H/2 × W/2
  TransposedConv2D [3 filters, 3×3, stride 2, Sigmoid] → H × W × 3
↓
Output: imagen reconstruida
```

**Función de Pérdida Multi-Componente**:
$$\mathcal{L} = \mathcal{L}_{\text{MSE}} + \lambda_1 \mathcal{L}_{\text{SSIM}} + \lambda_2 \mathcal{L}_{\text{perceptual}}$$

donde:
- $\mathcal{L}_{\text{MSE}} = \|\mathbf{I} - \hat{\mathbf{I}}\|^2_2$
- $\mathcal{L}_{\text{SSIM}} = 1 - \text{SSIM}(\mathbf{I}, \hat{\mathbf{I}})$
- $\mathcal{L}_{\text{perceptual}} = \|\phi_l(\mathbf{I}) - \phi_l(\hat{\mathbf{I}})\|^2_2$ donde $\phi_l$ son características de una red pre-entrenada (ej. VGG)

#### 3) Adaptación a Condiciones de Canal Variables

Para generalizar a diferentes SNRs, entrenar con "channel conditioning":

$$\hat{\mathbf{I}} = g_{\phi}(\mathbf{y}, \text{SNR})$$

donde el SNR se proporciona como entrada adicional al decoder, permitiéndole adaptar la estrategia de decodificación.

Alternativamente, usar **meta-learning** para aprender inicializaciones que se adaptan rápidamente a nuevas condiciones con pocas muestras.

#### 4) Resultados Cuantitativos

Comparación en transmisión de imágenes CelebA sobre canal AWGN:

| Método | Tasa (símb/px) | SNR=5dB PSNR | SNR=10dB PSNR | SNR=15dB PSNR |
|--------|----------------|--------------|---------------|---------------|
| JPEG+LDPC | 0.1 | 18.2 dB | 21.5 dB | 24.8 dB |
| BPG+Polar | 0.1 | 19.1 dB | 22.3 dB | 25.6 dB |
| JSCC-Neural | 0.1 | 21.3 dB | 25.1 dB | 28.7 dB |

El JSCC neural supera métodos separados, especialmente en SNR bajo, ya que adapta la tasa de codificación y protección de manera conjunta.

### C. Comunicaciones Semánticas

#### 1) Del Paradigma Sintáctico al Semántico

Las comunicaciones tradicionales son **sintácticas**: transmiten bits sin considerar su significado. Shannon's framework mide información mediante entropía, independiente del contenido semántico.

Las **comunicaciones semánticas** proponen transmitir solo la "información significativa" relevante para la tarea del receptor.

**Ejemplo**: transmitir "hay un peatón cruzando" en vez de video completo para vehículo autónomo.

#### 2) Formalización Matemática

Definir un "espacio semántico" $\mathcal{Z}$ donde reside el significado. Una función de extracción semántica:

$$\mathbf{z} = f_{\text{sem}}(\mathbf{s})$$

mapea la fuente $\mathbf{s}$ (ej. imagen) a representación semántica $\mathbf{z}$.

El transmisor codifica solo $\mathbf{z}$:
$$\mathbf{x} = f_{\text{enc}}(\mathbf{z})$$

El receptor decodifica y realiza la tarea:
$$\hat{\mathbf{y}}_{\text{task}} = f_{\text{task}}(g_{\text{dec}}(\mathbf{y}))$$

La función de pérdida es **task-oriented**:
$$\mathcal{L} = \mathbb{E}[\mathcal{L}_{\text{task}}(\mathbf{y}_{\text{task}}, \hat{\mathbf{y}}_{\text{task}})]$$

#### 3) Arquitectura de Ejemplo: Transmisión para Clasificación de Imágenes

**Transmisor**:
```
Input: imagen [224×224×3]
↓
Encoder pre-entrenado (ej. ResNet) → [representación 2048-D]
↓
Bottleneck semántico: Dense [128 units] → representación compacta
↓
Codificador de canal neural → [n símbolos]
```

**Receptor**:
```
Input: señal recibida [n símbolos]
↓
Decodificador de canal neural → [128-D representation]
↓
Clasificador: Dense [num_classes, softmax]
```

**Entrenamiento End-to-End**:
$$\mathcal{L} = \text{CrossEntropy}(\mathbf{y}_{\text{label}}, \hat{\mathbf{y}}_{\text{class}})$$

La red aprende una representación de 128-D que preserva información discriminativa para clasificación, descartando detalles visuales irrelevantes.

**Ganancia de Eficiencia**: Transmitir representación de 128 dimensiones vs. 150,528 pixels (imagen 224×224×3) implica compresión de ~1000×, con degradación mínima en precisión de clasificación si la tarea es el objetivo.

#### 4) Teoría de la Información Semántica

Extensión de la teoría de Shannon para incluir semántica. Definir:

**Información Mutua Semántica**:
$$I_{\text{sem}}(S; \hat{S} | \mathcal{T}) = I(f_{\mathcal{T}}(S); f_{\mathcal{T}}(\hat{S}))$$

donde $f_{\mathcal{T}}$ extrae características relevantes para tarea $\mathcal{T}$.

La tasa semántica mínima:
$$R_{\text{sem}}(\mathcal{T}, D) = \min_{p(\hat{s}|s)} I(S; \hat{S})$$
sujeto a: $\mathbb{E}[d_{\mathcal{T}}(S, \hat{S})] \leq D$

donde $d_{\mathcal{T}}$ es distorsión específica de la tarea.

Este framework permite cuantificar ganancia de comunicaciones semánticas: $R_{\text{sem}} \ll R_{\text{Shannon}}$ cuando mucha información de $S$ es irrelevante para $\mathcal{T}$.

### D. Integración de Sensado y Comunicaciones (ISAC)

#### 1) Convergencia de Comunicaciones y Radar

6G propone unificar comunicaciones y sensado del entorno, compartiendo el mismo espectro y hardware. Una señal transmitida sirve simultáneamente para:
- Comunicar información a receptores
- Sensar objetos mediante reflexiones (radar)

**Señal Transmitida**:
$$\mathbf{x} = \mathbf{x}_{\text{comm}} + \mathbf{x}_{\text{sense}}$$

**Señal Reflejada (Radar)**:
$$\mathbf{y}_{\text{radar}} = \sum_{t=1}^{T} \alpha_t \mathbf{x}(\tau_t) + \mathbf{n}$$

donde $\alpha_t, \tau_t$ son atenuación y retardo del target $t$.

**Señal de Comunicación**:
$$\mathbf{y}_{\text{comm}} = \mathbf{H}\mathbf{x} + \mathbf{n}$$

#### 2) Diseño Conjunto con Redes Neuronales

**Multi-Task Learning**: Entrenar una red que optimiza ambas tareas:

Transmisor diseña $\mathbf{x}$ para satisfacer:
$$\mathcal{L} = \alpha \mathcal{L}_{\text{comm}} + \beta \mathcal{L}_{\text{sense}}$$

donde:
- $\mathcal{L}_{\text{comm}}$: tasa de error de comunicación
- $\mathcal{L}_{\text{sense}}$: error de estimación de parámetros de target (posición, velocidad)

**Arquitectura**:
```
Input: mensaje de comunicación + parámetros de beamforming deseados
↓
Shared Encoder → representación intermedia
↓
       ├─→ Communication Branch → forma de onda optimizada para datos
       └─→ Sensing Branch → forma de onda optimizada para resolución radar
↓
Fusion: combinación ponderada
↓
Output: forma de onda dual-función
```

**Restricciones**:
- $\mathbf{x}$ debe tener buenas propiedades de autocorrelación (para sensado)
- $\mathbf{x}$ debe soportar modulación de datos (para comunicación)
- Restricción de potencia total

#### 3) Procesamiento de Señal Reflejada con DNNs

Usar CNN para procesar el "radar image" (mapa rango-Doppler):

$$\hat{\{\alpha_t, \tau_t, f_{D,t}\}} = f_{\text{CNN}}(\mathbf{Y}_{\text{radar}})$$

donde $\mathbf{Y}_{\text{radar}}$ es el espectrograma de la señal reflejada, y $f_{D,t}$ es el desplazamiento Doppler.

La CNN aprende a extraer targets en presencia de clutter y multipath.

### E. Optimización End-to-End de Pilas Completas de Protocolos

#### 1) Más Allá del Nivel Físico: Optimización Cross-Layer

Extender la IA nativa a capas superiores (MAC, routing, transporte) para optimización holística.

**Formulación Multi-Capa**:
$$\min_{\theta_{\text{PHY}}, \theta_{\text{MAC}}, \theta_{\text{NET}}, \theta_{\text{APP}}} \mathcal{L}_{\text{app}}(\text{QoE}, \text{latency}, \text{throughput})$$

sujeto a restricciones en cada capa.

#### 2) Ejemplo: Optimización Conjunta PHY-MAC

En el nivel físico, decisiones de modulación/codificación.
En el MAC, decisiones de acceso al medio y scheduling.

**Estado del Agente RL**:
- Canal CSI (PHY)
- Ocupación de buffer (MAC)
- Tráfico de red (NET)

**Acciones**:
- Selección de MCS (Modulation and Coding Scheme) [PHY]
- Decisión de transmitir/esperar [MAC]

**Recompensa**:
- Throughput
- Penalización por delay
- Penalización por colisiones

Un agente de RL aprende política conjunta que maximiza rendimiento end-to-end.

---

## V. IMPLEMENTACIÓN PRÁCTICA Y COMPLEJIDAD COMPUTACIONAL

### A. Hardware para Inferencia en Tiempo Real

#### 1) Requisitos de Latencia en 6G

Para URLLC en 6G, latencias objetivo son < 0.1 ms. La inferencia de redes neuronales debe completarse en microsegundos.

**Budget de Latencia** (ejemplo para slot de 1 ms):
- Procesamiento PHY: 100 μs
  - Estimación de canal: 20 μs
  - Decodificación: 50 μs
  - Detección: 30 μs
- Procesamiento MAC: 50 μs
- Overhead: 50 μs

#### 2) Arquitecturas de Hardware Especializadas

**GPUs**: Alta throughput para procesamiento batch, pero latencia absoluta alta (ms).

**FPGAs**: Latencia ultra-baja (μs), reconfigurables, pero desarrollo complejo.

**ASICs / Neural Processing Units (NPUs)**: Optimizados para operaciones de redes neuronales específicas (ej. convolución, matrix multiply). Ejemplos: Google TPU, Nvidia Tensor Cores.

**Procesadores Analógicos**: Computación in-memory usando crossbar arrays memristivos para multiplicaciones matriz-vector. Potencialmente ultra-eficiente energéticamente.

#### 3) Cuantización y Optimización de Modelos

**Cuantización**: Reducir precisión de pesos y activaciones de FP32 a INT8 o incluso binario.

Para cuantización a INT8:
$$w_q = \text{round}\left(\frac{w - w_{\min}}{w_{\max} - w_{\min}} \cdot 255\right)$$

**Quantization-Aware Training (QAT)**: Simular cuantización durante entrenamiento:
$$w_q = \text{round}(w) + (w - \text{round}(w))$$

durante forward pass, usar $w_q$, pero gradientes fluyen a través de $w$ continuo.

**Pruning**: Eliminar conexiones con pesos pequeños.

**Knowledge Distillation**: Entrenar modelo pequeño ("estudiante") para imitar modelo grande ("maestro"):
$$\mathcal{L} = \alpha \mathcal{L}_{\text{task}} + (1-\alpha) \mathcal{L}_{\text{KD}}$$
donde:
$$\mathcal{L}_{\text{KD}} = \text{KL}\left(p_{\text{teacher}}(y|x) \| p_{\text{student}}(y|x)\right)$$

**Resultados**: Modelos cuantizados a INT8 típicamente mantienen > 99% de precisión con 4× reducción de memoria y aceleración de inferencia de 2-4×.

### B. Entrenamiento Distribuido y Federado

#### 1) Desafíos de Escala

Entrenar modelos de PHY requiere:
- Grandes datasets de señales (Terabytes)
- Diversidad de condiciones de canal
- Iteraciones de entrenamiento prolongadas (días/semanas en clusters GPU)

#### 2) Entrenamiento Distribuido en Datos

**Data Parallelism**: Distribuir mini-batches sobre múltiples GPUs.

Cada GPU $i$ computa gradiente local:
$$\mathbf{g}_i = \nabla_{\theta} \mathcal{L}(\theta; \mathcal{B}_i)$$

Gradientes se agregan:
$$\mathbf{g} = \frac{1}{N} \sum_{i=1}^{N} \mathbf{g}_i$$

y parámetros se actualizan sincronizadamente.

**All-Reduce Eficiente**: Algoritmos como Ring All-Reduce minimizan comunicación.

#### 3) Federated Learning para PHY

En redes descentralizadas, cada dispositivo tiene datos locales que no pueden compartirse (privacidad).

**Algoritmo FederatedAveraging**:
1. Servidor distribuye modelo global $\theta_t$
2. Cada cliente $k$ entrena localmente:
   $$\theta_t^{(k)} \leftarrow \theta_t - \eta \nabla \mathcal{L}_k(\theta_t)$$
3. Clientes envían actualizaciones $\Delta\theta_t^{(k)} = \theta_t^{(k)} - \theta_t$
4. Servidor agrega:
   $$\theta_{t+1} = \theta_t + \frac{1}{K}\sum_{k=1}^{K} \Delta\theta_t^{(k)}$$

**Aplicación en Comunicaciones**: Dispositivos móviles entrenan modelos de canal específicos de su entorno, agregando conocimiento sin compartir datos de señal sensibles.

### C. Complejidad Computacional Comparativa

#### 1) Análisis de FLOPs

**Red Completamente Conectada** (input $n$, hidden $h$, output $m$):
$$\text{FLOPs} = 2nh + 2hm$$

**Red Convolucional** (capa con $C_{\text{in}}$ canales input, $C_{\text{out}}$ output, kernel $k \times k$, feature map $H \times W$):
$$\text{FLOPs} = 2 C_{\text{in}} C_{\text{out}} k^2 H W$$

**Comparación con Decodificación Turbo**: Para tasa 1/3, longitud $n=1024$:
- Turbo (5 iteraciones): ~$10^6$ operaciones
- RNN decoder (100 unidades ocultas): ~$2 \times 10^5$ FLOPs

RNN es potencialmente 5× más eficiente, aunque esto ignora paralelización y caching que favorecen Turbo en hardware especializado.

#### 2) Latencia de Inferencia Medida

Ejemplos en hardware real:

| Modelo | Plataforma | Latencia | Throughput |
|--------|------------|----------|------------|
| MLP Detector (512-256-128) | GPU V100 | 0.15 ms | 6666 detecciones/s |
| CNN Estimador (5 capas) | GPU V100 | 0.32 ms | 3125 estimaciones/s |
| LSTM Decoder (2 capas, 128) | GPU V100 | 1.2 ms | 833 decodificaciones/s |
| DetNet Cuantizado (INT8) | Qualcomm NPU | 0.05 ms | 20000 detecciones/s |

Las NPUs móviles logran latencia sub-100 μs para modelos optimizados, viable para 6G.

### D. Consumo Energético y Eficiencia

#### 1) Importancia para Dispositivos Móviles

Dispositivos IoT y móviles tienen budgets energéticos estrictos. El procesamiento de PHY consume ~30% de energía total del dispositivo.

#### 2) Comparación de Consumo

**Procesamiento Tradicional de PHY** (decodificación LDPC en ASIC): ~10 pJ/bit

**Inferencia Neural** (MLP en GPU): ~1 nJ/bit (100× mayor)

Sin embargo, con cuantización y hardware especializado:

**Inferencia Neural Cuantizada (INT8) en NPU**: ~50 pJ/bit

Gap se reduce a 5×, y continúa cerrándose con avances en hardware neuromorfico.

#### 3) Técnicas de Eficiencia Energética

**Early Exit**: Añadir clasificadores intermedios en redes profundas. Si confianza es alta en capa temprana, salir sin procesar capas restantes.

**Adaptive Computation**: Ajustar complejidad de red según condiciones. Ejemplo: usar red pequeña en SNR alto (canal bueno), red grande en SNR bajo.

**Sparse Activations**: Forzar activaciones sparse mediante regularización L1, reduciendo operaciones en inferencia.

---

## VI. DESAFÍOS PENDIENTES Y DIRECCIONES FUTURAS

### A. Generalización Fuera de Distribución

#### 1) El Problema de Distributional Shift

Modelos entrenados en simulaciones pueden fallar en despliegue real por:
- Discrepancias en modelos de canal (simulación vs. realidad)
- Condiciones no vistas durante entrenamiento (nuevos tipos de interferencia)
- Deriva temporal (cambios en propagación debido a construcciones)

#### 2) Técnicas de Robustificación

**Domain Adaptation**: Entrenar en dominio fuente (simulación), adaptar a dominio objetivo (real) con pocas muestras etiquetadas.

**Adversarial Training**: Añadir perturbaciones adversariales durante entrenamiento:
$$\mathcal{L}_{\text{adv}} = \mathbb{E}_{\mathbf{x}, \delta \sim \text{Adv}} [\mathcal{L}(\mathbf{x} + \delta)]$$

forzando robustez a pequeñas variaciones.

**Meta-Learning (MAML)**: Entrenar modelo para adaptarse rápidamente a nuevas tareas con pocos ejemplos:
$$\theta^* = \arg\min_{\theta} \sum_{\mathcal{T}_i} \mathcal{L}_{\mathcal{T}_i}(\theta - \alpha \nabla_{\theta}\mathcal{L}_{\mathcal{T}_i}(\theta))$$

#### 3) Validación con Datos Reales

Necesidad de datasets de señales reales de 6G capturadas en entornos diversos (urbano denso, rural, alta velocidad). Iniciativas como DeepMIMO y Raymobtime proporcionan pasos iniciales.

### B. Interpretabilidad y Explicabilidad

#### 1) La Caja Negra del Aprendizaje Profundo

Redes neuronales de PHY son difíciles de interpretar: ¿Qué ha aprendido? ¿Por qué toma ciertas decisiones?

Esto es crítico para:
- Depuración y diagnóstico de fallos
- Cumplimiento regulatorio (explicar asignaciones de espectro)
- Confianza de operadores de red

#### 2) Técnicas de Interpretabilidad

**Visualización de Activaciones**: Para CNNs procesando espectrogramas, visualizar qué patrones activan neuronas específicas.

**Attribution Methods**: Gradientes de entrada (saliency maps) indican qué partes de la señal influyen en la decisión:
$$A(\mathbf{x}) = \left|\frac{\partial f(\mathbf{x})}{\partial \mathbf{x}}\right|$$

**Attention Weights**: Para modelos con atención, los pesos $\alpha_i$ indican qué partes de la secuencia son relevantes.

**Model Distillation en Reglas**: Entrenar árbol de decisión o modelo lineal para aproximar la red neuronal en regiones específicas, obteniendo reglas interpretables.

#### 3) Modelos Híbridos Interpretables

Combinar bloques físicos interpretables con componentes neuronales:

Ejemplo: En detector MIMO, usar ZF como baseline, añadir red neuronal para aprender corrección:
$$\hat{\mathbf{x}} = \mathbf{x}_{\text{ZF}} + f_{\theta}(\mathbf{y}, \mathbf{H})$$

La red aprende corregir deficiencias de ZF, pero la estructura base es interpretable.

### C. Seguridad y Adversarios

#### 1) Vulnerabilidades de Sistemas con IA

**Adversarial Attacks**: Inyectar perturbaciones cuidadosamente diseñadas en la señal para engañar al receptor:

$$\mathbf{y}_{\text{adv}} = \mathbf{y} + \delta, \quad \|\delta\| < \epsilon$$

donde $\delta$ maximiza error de decodificación.

**Model Poisoning**: Durante entrenamiento federado, clientes maliciosos envían actualizaciones que corrompen el modelo global.

**Model Inversion**: Atacante con acceso al modelo entrenado puede reconstruir datos de entrenamiento, violando privacidad.

#### 2) Defensa y Robustificación

**Adversarial Training**: Incluir ejemplos adversariales en entrenamiento:
$$\min_{\theta} \mathbb{E}_{\mathbf{x}, \mathbf{y}} \left[ \max_{\|\delta\| \leq \epsilon} \mathcal{L}(f_{\theta}(\mathbf{x} + \delta), \mathbf{y}) \right]$$

**Certified Robustness**: Usar técnicas de verificación formal o randomized smoothing para garantizar límites de robustez.

**Detección de Anomalías**: Monitorear señales de entrada; si $\mathbf{y}$ está fuera de distribución esperada, rechazar o solicitar retransmisión.

**Secure Aggregation en FL**: Usar criptografía para agregar actualizaciones de clientes sin que el servidor vea actualizaciones individuales, previniendo poisoning.

#### 3) Autenticación y Integridad

**Physical Layer Authentication**: Usar características únicas del canal (fingerprinting) para autenticar transmisores:
$$\text{Auth}(\mathbf{y}) = \begin{cases}
\text{Legitimate} & \text{si } f_{\theta}(\mathbf{y}) \approx \mathbf{h}_{\text{known}} \\
\text{Spoofing} & \text{en otro caso}
\end{cases}$$

Una red neuronal aprende a distinguir canales de usuarios legítimos vs. atacantes.

### D. Estandarización y Compatibilidad

#### 1) Integración en Estándares 6G

Para despliegue masivo, IA nativa debe estandarizarse. Desafíos:
- **Interoperabilidad**: Dispositivos de diferentes fabricantes deben comunicarse. ¿Cómo estandarizar arquitecturas neuronales?
- **Versionado de Modelos**: Modelos evolucionan con actualizaciones. ¿Cómo mantener compatibilidad backward?
- **Señalización**: ¿Cómo negociar capacidades de IA entre transmisor y receptor?

#### 2) Propuestas de Estandarización

**Modelos de Referencia**: Definir arquitecturas neuronales estándar (ej. "DeepPHY-Profile-1") que todos los dispositivos soporten.

**Negociación de Capacidades**: Protocolo de handshake donde dispositivos intercambian:
- Arquitecturas soportadas
- Versiones de modelo
- Capacidades de procesamiento

Si no hay match, retroceder a PHY tradicional.

**Formato de Modelo Portable**: Usar formatos como ONNX para intercambiar modelos entre plataformas.

#### 3) Coexistencia con Sistemas Legados

6G debe coexistir con 5G, 4G durante transición. Diseño de "modo híbrido":
- Detección automática de tipo de dispositivo
- Si receptor no soporta IA, transmisor usa modulación/codificación tradicional
- Si ambos soportan, negocian uso de PHY neuronal

### E. Sostenibilidad y Consumo Energético

#### 1) Huella de Carbono del Entrenamiento

Entrenar modelos grandes de PHY consume energía significativa. Un modelo de transformación grande puede emitir ~300 toneladas CO2.

Para 6G sostenible:
- **Entrenar Modelos Compartidos**: En lugar de que cada operador entrene independientemente, compartir modelos pre-entrenados.
- **Entrenamiento Eficiente**: Usar técnicas como transferencia de aprendizaje, few-shot learning para reducir iteraciones.
- **Hardware Verde**: Data centers con energía renovable.

#### 2) Eficiencia en Inferencia

Promover arquitecturas eficientes:
- **Neural Architecture Search (NAS)** con objetivo de eficiencia energética
- **Compresión de Modelos** agresiva
- **Computación en el Edge**: Realizar inferencia localmente en lugar de cloud, reduciendo tráfico de red y latencia

### F. Aprendizaje Continuo y Adaptación Online

#### 1) Canales No-Estacionarios

En escenarios de movilidad extrema, canales cambian rápidamente. Modelos estáticos se vuelven obsoletos.

**Aprendizaje Online**: Actualizar modelo continuamente con observaciones recientes:
$$\theta_{t+1} = \theta_t - \eta \nabla_{\theta}\mathcal{L}(\theta_t; (\mathbf{x}_t, \mathbf{y}_t))$$

#### 2) Catastrophic Forgetting

Al actualizar con nuevos datos, modelos pueden "olvidar" conocimiento previo.

**Soluciones**:
- **Elastic Weight Consolidation (EWC)**: Penalizar cambios en parámetros importantes para tareas previas:
$$\mathcal{L}_{\text{EWC}} = \mathcal{L}_{\text{new}} + \frac{\lambda}{2}\sum_i F_i (\theta_i - \theta_i^*)^2$$
donde $F_i$ es la información de Fisher.

- **Experience Replay**: Mantener buffer de experiencias pasadas, muestrear y entrenar con mezcla de datos nuevos y antiguos.

#### 3) Meta-Aprendizaje para Adaptación Rápida

Entrenar modelo para adaptarse rápidamente a nuevos entornos con pocas muestras. Algoritmos como MAML (Model-Agnostic Meta-Learning) optimizan para rápida adaptación:

$$\theta^* = \arg\min_{\theta} \mathbb{E}_{\mathcal{T}} \left[ \mathcal{L}_{\mathcal{T}}(U_{\mathcal{T}}(\theta)) \right]$$

donde $U_{\mathcal{T}}(\theta)$ es el modelo después de $K$ pasos de gradiente en tarea $\mathcal{T}$.

---

## VII. CONCLUSIONES Y PERSPECTIVAS

### A. Síntesis de Contribuciones

Este artículo ha presentado un análisis exhaustivo de la Inteligencia Artificial nativa en el nivel físico de redes 6G, abordando:

1. **Fundamentos Teóricos**: Establecimiento de un marco matemático riguroso basado en teoría de la información, aprendizaje de representaciones y optimización con restricciones físicas. Se demostr   que la optimización end-to-end de sistemas de comunicación mediante redes neuronales es equivalente a codificación conjunta fuente-canal, con potencial de superar aproximaciones separadas tradicionales.

2. **Componentes del Nivel Físico**: Análisis detallado de la aplicación de aprendizaje profundo a codificación de canal, estimación de canal, detección multi-usuario, beamforming y gestión de recursos. Se presentaron arquitecturas de redes neuronales específicas para cada componente, con análisis de complejidad computacional y rendimiento comparativo respecto a métodos convencionales.

3. **Sistemas End-to-End**: Exploración de autoencoders de comunicación completos, codificación conjunta fuente-canal neural, comunicaciones semánticas, e integración de sensado y comunicaciones. Se demostró que la optimización holística del sistema puede descubrir estrategias no convencionales con rendimiento superior.

4. **Implementación Práctica**: Discusión de hardware especializado para inferencia en tiempo real, técnicas de cuantización y optimización de modelos, entrenamiento distribuido y federado, y análisis de consumo energético. Se identificaron gaps entre investigación y despliegue práctico, con propuestas de mitigación.

5. **Desafíos Pendientes**: Identificación de problemas abiertos en generalización, interpretabilidad, seguridad, estandarización y sostenibilidad. Se propusieron direcciones de investigación para abordar estos desafíos en la próxima década.

### B. Impacto Potencial en 6G

La IA nativa en el nivel físico representa un cambio paradigmático con impacto transformador:

**Rendimiento Mejorado**: Simulaciones y experimentos preliminares indican ganancias significativas:
- 2-5 dB de mejora en eficiencia espectral vs. métodos tradicionales
- 10-100× reducción en latencia de procesamiento con hardware optimizado
- Soporte de escenarios previamente inaccesibles (MIMO masivo con 256+ antenas, comunicaciones terahertz)

**Nuevas Capacidades Emergentes**: IA nativa habilita funcionalidades cualitativas:
- **Comunicaciones Semánticas**: Transmisión orientada a tareas con órdenes de magnitud menos datos
- **Adaptación Predictiva**: Anticipación de condiciones de canal y ajuste proactivo
- **Sensado Integrado**: Dual-uso de señales para comunicación y percepción del entorno
- **Optimización Holística**: Coordinación cross-layer superando diseños tradicionales en capas

**Democratización de Tecnologías Avanzadas**: La capacidad de redes neuronales para aprender soluciones complejas sin expertise humano especializado puede:
- Reducir barreras de entrada para desarrollo de tecnologías wireless
- Acelerar innovación mediante experimentación automatizada
- Permitir personalización de sistemas para casos de uso específicos

### C. Roadmap Tecnológico

Proyección de desarrollo para la próxima década:

**2024-2026 (Fase de Investigación Fundamental)**:
- Establecimiento de datasets estándar de señales 6G reales
- Desarrollo de arquitecturas neuronales especializadas para PHY
- Primeras implementaciones en hardware (FPGAs, ASICs prototipos)
- Publicación de benchmarks comparativos

**2027-2029 (Fase de Validación y Estandarización)**:
- Pruebas de campo en testbeds de pre-6G
- Inicio de estandarización en organismos como 3GPP, IEEE
- Desarrollo de herramientas de diseño asistido por IA para PHY
- Maduración de hardware neuromorfico para comunicaciones

**2030-2032 (Fase de Despliegue Inicial)**:
- Primeros productos comerciales con PHY neuronal
- Coexistencia con sistemas 5G-Advanced
- Refinamiento basado en retroalimentación operativa
- Expansión de casos de uso (IoT, V2X, aplicaciones industriales)

**2033-2035 (Fase de Madurez)**:
- Adopción masiva en dispositivos de consumo
- Optimización energética y reducción de costo
- Ecosistema consolidado de herramientas y servicios
- Inicio de investigación post-6G con IA cuántica

### D. Recomendaciones para la Comunidad de Investigación

Para acelerar el desarrollo y adopción de IA nativa en 6G, se recomienda:

1. **Datos Abiertos**: Establecer repositorios públicos de trazas de canal reales, señales capturadas, y mediciones de propagación en diversos escenarios. La falta de datos realistas es el mayor obstáculo para validación robusta.

2. **Benchmarks Estandarizados**: Definir tareas de evaluación comunes con métricas claras (BER vs. SNR, throughput vs. complejidad, latencia de inferencia) para permitir comparación objetiva entre aproximaciones.

3. **Reproducibilidad**: Publicar código, arquitecturas de modelos y hiperparámetros junto con resultados. Adoptar prácticas de ciencia abierta para acelerar progreso colectivo.

4. **Colaboración Interdisciplinaria**: Fomentar interacción entre comunidades de comunicaciones inalámbricas, aprendizaje automático, teoría de la información y hardware. Los avances requieren expertise de múltiples dominios.

5. **Consideraciones Éticas**: Desarrollar guidelines para uso responsable de IA en infraestructura crítica de comunicaciones, incluyendo privacidad, seguridad, equidad (evitar sesgos en asignación de recursos) y sostenibilidad ambiental.

6. **Educación y Capacitación**: Actualizar curricula académicas para incluir IA aplicada a comunicaciones. Entrenar nueva generación de ingenieros con competencias en ambos dominios.

### E. Reflexión Final

La Inteligencia Artificial nativa en el nivel físico de 6G no es simplemente una mejora incremental sobre generaciones anteriores, sino una reformulación fundamental de cómo concebimos, diseñamos e implementamos sistemas de comunicación. Al trascender el paradigma de diseño algorítmico específico basado en modelos simplificados, y abrazar el aprendizaje de representaciones óptimas directamente de datos, abrimos un espacio de diseño vasto que probablemente contiene soluciones radicalmente diferentes y superiores.

Sin embargo, esta transición plantea desafíos profundos: técnicos (generalización, interpretabilidad, eficiencia), operacionales (estandarización, compatibilidad, despliegue), y sociales (equidad, privacidad, sostenibilidad). El éxito de 6G como plataforma de comunicación para la década de 2030 dependerá no solo de avances tecnológicos, sino de nuestra capacidad colectiva para navegar estos desafíos con rigor científico, responsabilidad ética y visión de largo plazo.

La investigación en IA nativa para el nivel físico está en una fase emocionante de efervescencia creativa. Los próximos años determinarán si las promesas teóricas se materializan en sistemas reales que transforman cómo nos comunicamos, percibimos e interactuamos con el mundo digital. Este artículo ha buscado contribuir a ese futuro mediante una exposición rigurosa, comprehensiva y críticamente balanceada del estado del arte y las fronteras de investigación. Invitamos a la comunidad a sumarse a este esfuerzo colectivo de imaginar y construir la próxima generación de redes de comunicación.

---

## AGRADECIMIENTOS

El autor agradece a la comunidad global de investigadores en comunicaciones inalámbricas y aprendizaje automático cuyo trabajo ha sido fundamental para desarrollar el campo de IA nativa en el nivel físico. Este artículo sintetiza contribuciones de cientos de publicaciones y se beneficia de discusiones en conferencias, talleres y foros colaborativos.

---

## REFERENCIAS

[1] C. E. Shannon, "A Mathematical Theory of Communication," *Bell Syst. Tech. J.*, vol. 27, no. 3, pp. 379–423, 1948.

[2] T. O'Shea y J. Hoydis, "An Introduction to Deep Learning for the Physical Layer," *IEEE Trans. Cogn. Commun. Netw.*, vol. 3, no. 4, pp. 563–575, 2017.

[3] Y. Polyanskiy, H. V. Poor, y S. Verdú, "Channel Coding Rate in the Finite Blocklength Regime," *IEEE Trans. Inf. Theory*, vol. 56, no. 5, pp. 2307–2359, 2010.

[4] N. Tishby y N. Zaslavsky, "Deep Learning and the Information Bottleneck Principle," en *IEEE Information Theory Workshop (ITW)*, 2015, pp. 1–5.

[5] S. Dörner, S. Cammerer, J. Hoydis, y S. ten Brink, "Deep Learning Based Communication Over the Air," *IEEE J. Sel. Topics Signal Process.*, vol. 12, no. 1, pp. 132–143, 2018.

[6] H. He, C.-K. Wen, S. Jin, y G. Y. Li, "Deep Learning-Based Channel Estimation for Beamspace mmWave Massive MIMO Systems," *IEEE Wireless Commun. Lett.*, vol. 7, no. 5, pp. 852–855, 2018.

[7] N. Samuel, T. Diskin, y A. Wiesel, "Deep MIMO Detection," en *IEEE Int. Workshop Signal Process. Advances Wireless Commun. (SPAWC)*, 2017, pp. 1–5.

[8] A. Alkhateeb, S. Alex, P. Varkey, Y. Li, Q. Qu, y D. Tujkovic, "Deep Learning Coordinated Beamforming for Highly-Mobile Millimeter Wave Systems," *IEEE Access*, vol. 6, pp. 37328–37348, 2018.

[9] H. Sun, X. Chen, Q. Shi, M. Hong, X. Fu, y N. D. Sidiropoulos, "Learning to Optimize: Training Deep Neural Networks for Interference Management," *IEEE Trans. Signal Process.*, vol. 66, no. 20, pp. 5438–5453, 2018.

[10] E. Bourtsoulatze, D. B. Kurka, y D. Gündüz, "Deep Joint Source