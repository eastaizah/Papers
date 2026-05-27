# 10. Conclusiones, Glosario y Referencias

---

## 10.1 Conclusiones y recapitulación

### 10.1.1 Resumen del recorrido tutorial

A lo largo de este tutorial, hemos emprendido un viaje que conecta dos disciplinas que, durante décadas, evolucionaron de manera independiente: la **inteligencia artificial** y las **comunicaciones**. Partimos desde los fundamentos más elementales —la neurona artificial y el perceptrón— y construimos, paso a paso, un edificio conceptual que culmina en los **sistemas de comunicación semántica**, una de las áreas de investigación más prometedoras para las redes de sexta generación (6G) y más allá.

El recorrido puede resumirse en las siguientes etapas fundamentales:

**Etapa 1: El perceptrón como unidad fundamental.** En las secciones iniciales, estudiamos cómo una única neurona artificial puede realizar clasificación binaria mediante la combinación lineal de entradas ponderadas por pesos, seguida de una función de activación:

$$y = f\left(\sum_{i=1}^{n} w_i x_i + b\right)$$

Este modelo, propuesto originalmente por Rosenblatt (1958), constituye el bloque de construcción elemental de todas las arquitecturas de aprendizaje profundo que vendrían después. Comprendimos sus limitaciones —la incapacidad de resolver problemas no linealmente separables como la función XOR— y cómo esta limitación motivó el desarrollo de redes más complejas.

**Etapa 2: Redes multicapa y retropropagación.** Exploramos cómo al apilar múltiples capas de neuronas —formando el perceptrón multicapa (MLP)— se obtiene la capacidad de aproximar cualquier función continua, un resultado formalizado por el **teorema de aproximación universal** (Hornik, 1991). El algoritmo de retropropagación (Rumelhart *et al.*, 1986), basado en la regla de la cadena del cálculo diferencial, proporcionó el mecanismo para entrenar estas redes de manera eficiente:

$$\frac{\partial \mathcal{L}}{\partial w_{ij}^{(l)}} = \frac{\partial \mathcal{L}}{\partial a_j^{(l)}} \cdot \frac{\partial a_j^{(l)}}{\partial z_j^{(l)}} \cdot \frac{\partial z_j^{(l)}}{\partial w_{ij}^{(l)}}$$

Aprendimos que el descenso del gradiente, en sus diversas variantes (SGD, Adam, RMSProp), permite navegar paisajes de pérdida de alta dimensionalidad para encontrar configuraciones de pesos que minimizan la función de costo.

**Etapa 3: Redes convolucionales y la explotación de la estructura espacial.** Las redes neuronales convolucionales (CNN), inspiradas en el trabajo seminal de LeCun *et al.* (1998), introdujeron el concepto de **compartición de pesos** y **conectividad local**, lo que las hace especialmente adecuadas para datos con estructura espacial como imágenes, señales y espectrogramas. La operación de convolución:

$$(\mathbf{X} * \mathbf{K})[i,j] = \sum_m \sum_n \mathbf{X}[i+m, j+n] \cdot \mathbf{K}[m,n]$$

permite detectar patrones locales de forma invariante a la posición, reduciendo drásticamente el número de parámetros respecto a una red completamente conectada. Estas arquitecturas encontraron aplicaciones directas en comunicaciones: estimación de canal, detección de señales y, crucialmente, como codificadores/decodificadores en sistemas de comunicación semántica para imágenes.

**Etapa 4: Redes recurrentes y el modelado de secuencias.** Las RNN y, en particular, las celdas LSTM (Hochreiter y Schmidhuber, 1997) abordaron el desafío de modelar dependencias temporales en datos secuenciales. El mecanismo de compuertas de la LSTM:

$$\mathbf{f}_t = \sigma(\mathbf{W}_f [\mathbf{h}_{t-1}, \mathbf{x}_t] + \mathbf{b}_f)$$
$$\mathbf{i}_t = \sigma(\mathbf{W}_i [\mathbf{h}_{t-1}, \mathbf{x}_t] + \mathbf{b}_i)$$
$$\mathbf{o}_t = \sigma(\mathbf{W}_o [\mathbf{h}_{t-1}, \mathbf{x}_t] + \mathbf{b}_o)$$

permite la preservación selectiva de información a lo largo de secuencias extensas, mitigando los problemas de desvanecimiento y explosión del gradiente. No obstante, la naturaleza inherentemente secuencial de estas redes limita su capacidad de paralelización y, por tanto, su escalabilidad.

**Etapa 5: Mecanismos de atención y la revolución del Transformer.** El mecanismo de atención (Bahdanau *et al.*, 2015) representó un cambio de paradigma al permitir que los modelos aprendan a **focalizar su procesamiento** en las partes más relevantes de la entrada. La auto-atención escalada:

$$\text{Attention}(\mathbf{Q}, \mathbf{K}, \mathbf{V}) = \text{softmax}\left(\frac{\mathbf{Q}\mathbf{K}^T}{\sqrt{d_k}}\right)\mathbf{V}$$

y su extensión multi-cabeza en la arquitectura Transformer (Vaswani *et al.*, 2017) eliminaron la dependencia del procesamiento secuencial, habilitando un entrenamiento masivamente paralelo. El Transformer no solo revolucionó el procesamiento de lenguaje natural —dando lugar a modelos como BERT y GPT— sino que se ha convertido en la arquitectura dominante en múltiples dominios, incluyendo las comunicaciones.

**Etapa 6: Comunicaciones semánticas.** En la culminación del tutorial, convergieron todas las herramientas previamente desarrolladas. Los sistemas de comunicación semántica (Xie *et al.*, 2021) redefinen el objetivo de un sistema de comunicación: en lugar de garantizar la reproducción exacta de bits transmitidos, buscan preservar el **significado** de la información. La arquitectura codificador-canal-decodificador:

$$\hat{s} = D_\phi(C(E_\theta(s)))$$

donde $E_\theta$ es el codificador semántico, $C$ representa el canal de comunicación y $D_\phi$ es el decodificador semántico, se entrena de extremo a extremo (E2E) optimizando una función de pérdida semántica. Este enfoque, conocido como **codificación conjunta fuente-canal** (JSCC), supera la separación clásica fuente-canal de Shannon en regímenes de latencia finita y ofrece una degradación graceful (gradual) del rendimiento con la relación señal a ruido (SNR), eliminando el **efecto acantilado** (*cliff effect*) de los sistemas digitales tradicionales.

### 10.1.2 Lecciones clave del tutorial

Las principales lecciones que emergen de este recorrido son:

1. **El perceptrón es el bloque fundamental.** Toda la complejidad del aprendizaje profundo se construye a partir de la operación elemental de una neurona: una combinación lineal seguida de una no linealidad. Esta simplicidad es poderosa porque permite composición jerárquica.

2. **Los MLP aprenden mediante retropropagación.** El algoritmo de retropropagación, combinado con el descenso del gradiente, proporciona un mecanismo general y escalable para ajustar millones (o miles de millones) de parámetros a partir de datos. El gradiente $\nabla_{\mathbf{w}} \mathcal{L}$ guía la optimización en espacios de muy alta dimensionalidad.

3. **Las CNN explotan la estructura espacial.** Al incorporar **sesgos inductivos** como la invariancia traslacional y la localidad, las CNN logran eficiencia y rendimiento superiores en tareas que involucran datos con estructura espacial: imágenes, señales de comunicación, mapas de canal, etc.

4. **Las RNN/LSTM manejan datos secuenciales, pero tienen limitaciones.** Aunque las RNN y LSTM son capaces de capturar dependencias temporales, su procesamiento secuencial intrínseco limita la paralelización y el manejo de dependencias de muy largo alcance. Estas limitaciones motivaron la búsqueda de alternativas.

5. **Los mecanismos de atención permiten focalizar en lo relevante.** La atención proporciona un mecanismo diferenciable para ponderar dinámicamente la importancia de diferentes partes de la entrada, y puede interpretarse como una forma suave de recuperación de información basada en similitud.

6. **Los Transformers combinan atención con procesamiento paralelo.** Al reemplazar la recurrencia por auto-atención y codificación posicional, los Transformers logran modelar dependencias de rango arbitrario con complejidad computacional $O(n^2 d)$ pero total paralelización. Esto ha permitido escalar los modelos a tamaños sin precedentes y alcanzar rendimiento estado del arte en prácticamente todos los dominios.

7. **Las comunicaciones semánticas aprovechan el aprendizaje profundo para transmitir significado.** Al integrar codificación de fuente y de canal en una sola red neuronal entrenada E2E, los sistemas de comunicación semántica superan las limitaciones del paradigma de Shannon para escenarios prácticos con longitud de bloque finita, recursos limitados y requisitos de baja latencia.

8. **El entrenamiento E2E a través de canales diferenciables habilita la optimización conjunta.** La modelización del canal como una capa diferenciable (ya sea mediante modelos analíticos o redes generativas adversarias) permite que el gradiente fluya desde el decodificador hasta el codificador, optimizando todo el sistema de comunicación como una única red neuronal.

### 10.1.3 El camino hacia adelante: 6G y más allá

El futuro de las comunicaciones semánticas está intrínsecamente ligado a la evolución de las redes móviles hacia la sexta generación (6G), cuyo despliegue se anticipa para la década de 2030. Las principales direcciones de investigación y desarrollo incluyen:

**Comunicación semántica multimodal.** Los sistemas actuales se han centrado predominantemente en modalidades individuales (texto, imagen, voz). El futuro demanda sistemas que integren múltiples modalidades simultáneamente, transmitiendo la semántica de escenas complejas que combinan audio, video, texto y datos sensoriales. Esto requerirá avances en modelos de fusión multimodal y representaciones semánticas unificadas.

**Comunicación orientada a tareas.** Más allá de la reconstrucción fiel de la fuente, los sistemas futuros se orientarán hacia la **efectividad**: transmitir solo la información necesaria para que el receptor complete una tarea específica (clasificación, control, toma de decisiones). Esto implica funciones de pérdida diseñadas en torno al rendimiento de la tarea, no a la fidelidad de reconstrucción.

**Bases de conocimiento compartidas.** Los sistemas de comunicación semántica del futuro podrán aprovechar **bases de conocimiento** compartidas entre transmisor y receptor, permitiendo una compresión aún mayor al transmitir solo las diferencias respecto al conocimiento común. Esto introduce desafíos relacionados con la sincronización del conocimiento y la detección de **deriva semántica** (*semantic drift*).

**Integración con ISAC (Integrated Sensing and Communications).** La convergencia de percepción (radar, localización) y comunicaciones en una sola infraestructura se potenciará con la comunicación semántica, donde los datos sensoriales se comprimen y transmiten preservando su significado relevante para la tarea de percepción.

**Robustez y seguridad.** Los sistemas basados en redes neuronales son vulnerables a ataques adversariales. Garantizar la robustez y seguridad de las comunicaciones semánticas frente a perturbaciones intencionales y condiciones de canal extremas es un desafío abierto crítico.

**Escalabilidad y eficiencia.** La implementación de Transformers de gran escala en dispositivos con recursos limitados (IoT, sensores, dispositivos móviles) requiere técnicas de compresión de modelos, cuantización, poda y destilación de conocimiento.

**Métricas semánticas estandarizadas.** A diferencia de la tasa de error de bit (BER) o la tasa de error de bloque (BLER), no existe aún un consenso sobre métricas universales para evaluar la calidad semántica. El desarrollo de métricas estandarizadas que capturen fielmente la preservación del significado es fundamental para la adopción práctica de estos sistemas.

### 10.1.4 Reflexión final: la convergencia de la IA y las comunicaciones

La historia de las telecomunicaciones ha estado marcada por una separación conceptual clara entre la **fuente de información**, el **canal de transmisión** y el **destino**, siguiendo el modelo propuesto por Shannon en 1948. Esta separación, que demostró ser óptima en el límite asintótico de longitud de bloque infinita, ha sido la piedra angular del diseño de sistemas de comunicación durante más de siete décadas.

Sin embargo, los avances en aprendizaje profundo han revelado que, en condiciones prácticas con restricciones de latencia, ancho de banda y complejidad computacional, la **optimización conjunta** de todos los componentes del sistema de comunicación puede superar significativamente a los diseños modulares tradicionales. Esta convergencia entre IA y comunicaciones no es simplemente una mejora incremental; representa un **cambio de paradigma** en la forma en que concebimos la transmisión de información.

El modelo clásico de Shannon se centra en el **nivel técnico** de la comunicación: ¿con qué precisión pueden transmitirse los símbolos? Las comunicaciones semánticas, apoyadas por las capacidades representacionales del aprendizaje profundo, abordan el **nivel semántico**: ¿con qué precisión los símbolos transmitidos comunican el significado deseado? Y, en última instancia, el **nivel de efectividad**: ¿con qué eficacia el significado recibido afecta la conducta deseada?

Esta visión, articulada por Weaver y Shannon en 1949 pero imposible de realizar con las herramientas de la época, se está materializando ahora gracias a la convergencia de:

- **Potencia computacional** sin precedentes (GPUs, TPUs, aceleradores de IA).
- **Volúmenes masivos de datos** para el entrenamiento de modelos.
- **Arquitecturas neuronales** poderosas y flexibles (especialmente el Transformer).
- **Técnicas de entrenamiento** sofisticadas (E2E, aprendizaje por transferencia, aprendizaje auto-supervisado).

El futuro de las comunicaciones no reside únicamente en transmitir más bits por segundo, sino en transmitir **significado** de manera más eficiente, robusta e inteligente. Los ingenieros y científicos que dominen tanto los fundamentos del aprendizaje profundo como los principios de las comunicaciones estarán en una posición privilegiada para diseñar los sistemas que definirán la próxima era de las telecomunicaciones.

Como reflexión final, cabe señalar que el viaje desde el perceptrón de Rosenblatt hasta los sistemas de comunicación semántica basados en Transformers no es simplemente una progresión tecnológica: es un testimonio de cómo ideas aparentemente simples —una neurona que suma entradas ponderadas, un mecanismo que puntúa la relevancia de diferentes partes de una secuencia, un canal ruidoso modelado como una capa diferenciable— pueden combinarse para crear sistemas de una complejidad y capacidad extraordinarias. Esta es, en esencia, la belleza del aprendizaje profundo aplicado a las comunicaciones: la emergencia de comportamiento inteligente a partir de componentes simples, entrenados de extremo a extremo para un objetivo común.

---

## 10.2 Apéndice matemático

Este apéndice recopila las herramientas matemáticas fundamentales utilizadas a lo largo del tutorial. Su propósito es servir como referencia rápida para el lector que necesite refrescar conceptos específicos, así como proporcionar una visión unificada del aparato matemático que sustenta el aprendizaje profundo y las comunicaciones semánticas.

### 10.2.1 Álgebra lineal

El álgebra lineal constituye el lenguaje fundamental del aprendizaje profundo. Las operaciones sobre vectores y matrices son el núcleo computacional de todas las redes neuronales.

**Vectores.** Un vector $\mathbf{x} \in \mathbb{R}^n$ es una colección ordenada de $n$ números reales:

$$\mathbf{x} = \begin{bmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{bmatrix}$$

**Producto escalar (dot product).** Dados dos vectores $\mathbf{a}, \mathbf{b} \in \mathbb{R}^n$, su producto escalar se define como:

$$\mathbf{a} \cdot \mathbf{b} = \sum_{i=1}^{n} a_i b_i = ||\mathbf{a}||\,||\mathbf{b}||\cos\theta$$

donde $\theta$ es el ángulo entre ambos vectores y $||\mathbf{a}|| = \sqrt{\sum_i a_i^2}$ es la norma euclidiana. Esta relación es fundamental en los mecanismos de atención, donde la similitud entre vectores *query* y *key* se calcula mediante el producto escalar.

**Matrices.** Una matriz $\mathbf{A} \in \mathbb{R}^{m \times n}$ es un arreglo rectangular de números con $m$ filas y $n$ columnas. Las operaciones fundamentales incluyen:

- **Transposición:** $(\mathbf{A}^T)_{ij} = \mathbf{A}_{ji}$, que intercambia filas por columnas.
- **Multiplicación matricial:** Dadas $\mathbf{A} \in \mathbb{R}^{m \times p}$ y $\mathbf{B} \in \mathbb{R}^{p \times n}$:

$$(\mathbf{A}\mathbf{B})_{ij} = \sum_{k=1}^{p} A_{ik} B_{kj}$$

La operación fundamental de una capa neuronal se expresa como $\mathbf{z} = \mathbf{W}\mathbf{x} + \mathbf{b}$, que es una transformación afín donde $\mathbf{W} \in \mathbb{R}^{m \times n}$ es la matriz de pesos y $\mathbf{b} \in \mathbb{R}^m$ es el vector de sesgo.

**Valores y vectores propios.** Una matriz cuadrada $\mathbf{A}$ tiene un valor propio $\lambda$ y un vector propio $\mathbf{v}$ si:

$$\mathbf{A}\mathbf{v} = \lambda\mathbf{v}$$

Estos conceptos son relevantes en el análisis de la convergencia del entrenamiento, en la descomposición de la matriz de covarianza (PCA) y en la comprensión de la dinámica del gradiente.

### 10.2.2 Cálculo diferencial

El cálculo diferencial es esencial para la optimización de redes neuronales, pues el entrenamiento se basa fundamentalmente en el cómputo de gradientes.

**Derivada parcial.** La derivada parcial de una función $f(x_1, x_2, \ldots, x_n)$ respecto a la variable $x_i$ mide la tasa de cambio de $f$ cuando solo $x_i$ varía:

$$\frac{\partial f}{\partial x_i} = \lim_{\Delta x_i \to 0} \frac{f(\ldots, x_i + \Delta x_i, \ldots) - f(\ldots, x_i, \ldots)}{\Delta x_i}$$

**Gradiente.** El vector gradiente agrupa todas las derivadas parciales y apunta en la dirección de máximo crecimiento de la función:

$$\nabla f = \left[\frac{\partial f}{\partial x_1}, \frac{\partial f}{\partial x_2}, \ldots, \frac{\partial f}{\partial x_n}\right]^T$$

En el descenso del gradiente, los parámetros se actualizan en la dirección opuesta al gradiente:

$$\mathbf{w}_{t+1} = \mathbf{w}_t - \eta \nabla_{\mathbf{w}} \mathcal{L}(\mathbf{w}_t)$$

donde $\eta > 0$ es la tasa de aprendizaje.

**Regla de la cadena.** Para funciones compuestas $f(g(x))$, la regla de la cadena establece:

$$\frac{d f}{d x} = \frac{d f}{d g} \cdot \frac{d g}{d x}$$

En su versión multivariable, para $\mathbf{y} = g(\mathbf{x})$ y $z = f(\mathbf{y})$:

$$\frac{\partial z}{\partial x_i} = \sum_j \frac{\partial z}{\partial y_j} \cdot \frac{\partial y_j}{\partial x_i}$$

Esta es la base matemática del algoritmo de retropropagación: el gradiente de la pérdida respecto a los pesos de cada capa se calcula propagando las derivadas parciales desde la salida hacia la entrada, capa por capa.

### 10.2.3 Probabilidad y estadística

Los conceptos probabilísticos permean el aprendizaje profundo, desde la modelización de datos hasta la interpretación de las salidas de los modelos.

**Esperanza matemática.** El valor esperado de una variable aleatoria $X$ con función de densidad $p(x)$ es:

$$\mathbb{E}[X] = \int_{-\infty}^{\infty} x \, p(x) \, dx \quad \text{(caso continuo)}$$

$$\mathbb{E}[X] = \sum_x x \, p(x) \quad \text{(caso discreto)}$$

**Varianza.** La varianza mide la dispersión de $X$ respecto a su media $\mu = \mathbb{E}[X]$:

$$\text{Var}(X) = \mathbb{E}[(X - \mu)^2] = \mathbb{E}[X^2] - (\mathbb{E}[X])^2$$

**Distribución Gaussiana.** La distribución normal $\mathcal{N}(\mu, \sigma^2)$ tiene función de densidad:

$$p(x) = \frac{1}{\sqrt{2\pi\sigma^2}}\exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)$$

Esta distribución es omnipresente en comunicaciones (modelo de ruido AWGN) y en aprendizaje profundo (inicialización de pesos, regularización, modelos generativos). En el caso multivariado, la distribución Gaussiana con vector de medias $\boldsymbol{\mu}$ y matriz de covarianza $\boldsymbol{\Sigma}$ se expresa como:

$$p(\mathbf{x}) = \frac{1}{(2\pi)^{d/2}|\boldsymbol{\Sigma}|^{1/2}}\exp\left(-\frac{1}{2}(\mathbf{x}-\boldsymbol{\mu})^T\boldsymbol{\Sigma}^{-1}(\mathbf{x}-\boldsymbol{\mu})\right)$$

### 10.2.4 Teoría de la información

La teoría de la información, fundada por Shannon (1948), proporciona el marco teórico para las comunicaciones y establece los límites fundamentales que los sistemas de comunicación semántica buscan abordar de manera más eficiente.

**Entropía.** La entropía de una variable aleatoria discreta $X$ cuantifica la incertidumbre promedio asociada a sus posibles valores:

$$H(X) = -\sum_{x \in \mathcal{X}} p(x)\log_2 p(x)$$

Se mide en bits (cuando se usa $\log_2$) y alcanza su máximo para la distribución uniforme: $H(X) \leq \log_2 |\mathcal{X}|$.

**Entropía conjunta y condicional.** La entropía conjunta de dos variables $X$ e $Y$ es:

$$H(X, Y) = -\sum_{x,y} p(x,y) \log_2 p(x,y)$$

La entropía condicional, que mide la incertidumbre restante sobre $X$ dado el conocimiento de $Y$, se define como:

$$H(X|Y) = -\sum_{x,y} p(x,y) \log_2 p(x|y) = H(X,Y) - H(Y)$$

**Información mutua.** La información mutua entre $X$ e $Y$ cuantifica la reducción de incertidumbre sobre una variable al observar la otra:

$$I(X;Y) = H(X) - H(X|Y) = H(Y) - H(Y|X) = H(X) + H(Y) - H(X,Y)$$

La información mutua es simétrica, no negativa, y es igual a cero si y solo si $X$ e $Y$ son estadísticamente independientes. Es la cantidad fundamental que los sistemas de comunicación buscan maximizar.

**Capacidad del canal.** La capacidad de un canal de comunicación es la tasa máxima de información que puede transmitirse de manera fiable:

$$C = \max_{p(x)} I(X;Y)$$

Para el canal AWGN con potencia de señal $P$ y potencia de ruido $N$, la capacidad es:

$$C = \frac{1}{2}\log_2\left(1 + \frac{P}{N}\right) \quad \text{bits por uso del canal}$$

El teorema de codificación de canal de Shannon establece que es posible comunicarse con probabilidad de error arbitrariamente pequeña a cualquier tasa $R < C$, pero no para $R > C$. Los sistemas de comunicación semántica reinterpretan este resultado al operar sobre representaciones de significado en lugar de secuencias de bits.

### 10.2.5 La función Softmax: propiedades y estabilidad numérica

La función softmax transforma un vector de valores reales en una distribución de probabilidad:

$$\text{softmax}(\mathbf{z})_i = \frac{e^{z_i}}{\sum_{j=1}^{K} e^{z_j}}, \quad i = 1, \ldots, K$$

**Propiedades:**

1. **Normalización:** $\sum_{i=1}^{K} \text{softmax}(\mathbf{z})_i = 1$ y $\text{softmax}(\mathbf{z})_i > 0$ para todo $i$.
2. **Invariancia a traslación:** $\text{softmax}(\mathbf{z} + c\mathbf{1}) = \text{softmax}(\mathbf{z})$ para cualquier constante $c$.
3. **Comportamiento límite:** Cuando una componente $z_k \gg z_j$ para todo $j \neq k$, la softmax se aproxima a un vector one-hot.
4. **Temperatura:** La variante con temperatura $\tau > 0$:

$$\text{softmax}(\mathbf{z}/\tau)_i = \frac{e^{z_i/\tau}}{\sum_{j} e^{z_j/\tau}}$$

controla la "suavidad" de la distribución: $\tau \to 0$ produce una distribución concentrada (argmax suave); $\tau \to \infty$ produce una distribución uniforme.

**Estabilidad numérica.** En la práctica, los valores $e^{z_i}$ pueden causar desbordamiento numérico (*overflow*) cuando $z_i$ es grande, o subdesbordamiento (*underflow*) cuando $z_i$ es muy negativo. La solución estándar explota la propiedad de invariancia a traslación:

$$\text{softmax}(\mathbf{z})_i = \frac{e^{z_i - z_{\max}}}{\sum_{j} e^{z_j - z_{\max}}}, \quad z_{\max} = \max_j z_j$$

Al restar el valor máximo, se garantiza que el exponente mayor es $0$, evitando desbordamientos sin alterar el resultado.

### 10.2.6 Cálculo matricial: Jacobianos en la retropropagación

En la retropropagación a través de redes neuronales, las derivadas entre cantidades vectoriales se representan mediante **matrices jacobianas**.

**Matriz Jacobiana.** Dada una función vectorial $\mathbf{f}: \mathbb{R}^n \to \mathbb{R}^m$, la matriz Jacobiana $\mathbf{J} \in \mathbb{R}^{m \times n}$ se define como:

$$\mathbf{J} = \frac{\partial \mathbf{f}}{\partial \mathbf{x}} = \begin{bmatrix}
\frac{\partial f_1}{\partial x_1} & \cdots & \frac{\partial f_1}{\partial x_n} \\
\vdots & \ddots & \vdots \\
\frac{\partial f_m}{\partial x_1} & \cdots & \frac{\partial f_m}{\partial x_n}
\end{bmatrix}$$

**Aplicación en la retropropagación.** Si la capa $l$ computa $\mathbf{z}^{(l)} = \mathbf{W}^{(l)}\mathbf{a}^{(l-1)} + \mathbf{b}^{(l)}$ y $\mathbf{a}^{(l)} = \sigma(\mathbf{z}^{(l)})$, entonces:

$$\frac{\partial \mathcal{L}}{\partial \mathbf{z}^{(l)}} = \frac{\partial \mathcal{L}}{\partial \mathbf{a}^{(l)}} \odot \sigma'(\mathbf{z}^{(l)})$$

$$\frac{\partial \mathcal{L}}{\partial \mathbf{W}^{(l)}} = \frac{\partial \mathcal{L}}{\partial \mathbf{z}^{(l)}} \cdot (\mathbf{a}^{(l-1)})^T$$

$$\frac{\partial \mathcal{L}}{\partial \mathbf{a}^{(l-1)}} = (\mathbf{W}^{(l)})^T \cdot \frac{\partial \mathcal{L}}{\partial \mathbf{z}^{(l)}}$$

donde $\odot$ denota el producto elemento a elemento (producto de Hadamard). Estas ecuaciones forman el núcleo del algoritmo de retropropagación y permiten el cómputo eficiente de gradientes en redes de profundidad arbitraria.

**Jacobiano de la softmax.** Un caso particularmente importante es el Jacobiano de la función softmax. Si $\mathbf{p} = \text{softmax}(\mathbf{z})$, entonces:

$$\frac{\partial p_i}{\partial z_j} = p_i(\delta_{ij} - p_j)$$

donde $\delta_{ij}$ es la delta de Kronecker. Esta expresión se utiliza frecuentemente en la retropropagación a través de capas de atención y clasificación.

---

## 10.3 Glosario de términos

A continuación se presenta un glosario completo de los términos técnicos más relevantes utilizados a lo largo de este tutorial. Cada entrada incluye el término en inglés (cuando difiere) y su definición en español.

1. **Aprendizaje automático** (*Machine Learning*): Rama de la inteligencia artificial que desarrolla algoritmos capaces de aprender patrones a partir de datos sin ser programados explícitamente para cada tarea.

2. **Aprendizaje profundo** (*Deep Learning*): Subconjunto del aprendizaje automático que utiliza redes neuronales con múltiples capas ocultas para aprender representaciones jerárquicas de los datos.

3. **Atención** (*Attention*): Mecanismo que permite a un modelo ponderar dinámicamente la importancia de diferentes partes de la entrada al generar cada elemento de la salida, basándose en una función de similitud entre consultas y claves.

4. **Auto-atención** (*Self-Attention*): Variante del mecanismo de atención donde las consultas, claves y valores provienen de la misma secuencia de entrada, permitiendo que cada posición atienda a todas las demás posiciones de la misma secuencia.

5. **Autoencoder**: Arquitectura de red neuronal que aprende a comprimir (codificar) la entrada en una representación de menor dimensión y luego reconstruirla (decodificar), utilizada para aprendizaje de representaciones y reducción de dimensionalidad.

6. **AWGN** (*Additive White Gaussian Noise*): Modelo de ruido aditivo blanco gaussiano, ampliamente utilizado en comunicaciones para modelar el ruido térmico del canal. Se caracteriza por tener densidad espectral de potencia constante y distribución gaussiana.

7. **Batch Normalization**: Técnica de normalización que estandariza las activaciones de cada capa utilizando la media y varianza del mini-lote actual durante el entrenamiento, acelerando la convergencia y estabilizando el proceso de entrenamiento.

8. **BERT** (*Bidirectional Encoder Representations from Transformers*): Modelo de lenguaje basado en el codificador del Transformer, pre-entrenado bidireccionalmente mediante tareas de modelado de lenguaje enmascarado y predicción de la siguiente oración.

9. **Capacidad del canal** (*Channel Capacity*): Tasa máxima de información (en bits por uso del canal) que puede transmitirse de manera fiable a través de un canal de comunicación, definida como $C = \max_{p(x)} I(X;Y)$.

10. **Capa oculta** (*Hidden Layer*): Capa intermedia de una red neuronal situada entre la capa de entrada y la capa de salida. Las capas ocultas realizan transformaciones no lineales sucesivas que permiten a la red aprender representaciones complejas.

11. **CNN** (*Convolutional Neural Network* / Red Neuronal Convolucional): Tipo de red neuronal que emplea capas de convolución con filtros de pesos compartidos para extraer características locales, especialmente efectiva en datos con estructura espacial como imágenes y señales.

12. **Codificación conjunta fuente-canal** (*JSCC – Joint Source-Channel Coding*): Paradigma de codificación que integra la compresión de fuente y la protección contra errores del canal en un único proceso, en contraste con la separación clásica de Shannon. En el contexto de comunicaciones semánticas, se implementa mediante redes neuronales entrenadas de extremo a extremo.

13. **Codificador** (*Encoder*): Componente de una arquitectura que transforma la entrada en una representación intermedia (latente o codificada). En comunicaciones semánticas, el codificador extrae las características semánticas de la fuente y las mapea a símbolos adecuados para la transmisión por el canal.

14. **Cross-Entropy** (Entropía cruzada): Función de pérdida que mide la discrepancia entre la distribución de probabilidad predicha $\hat{p}$ y la distribución verdadera $p$: $H(p, \hat{p}) = -\sum_x p(x)\log \hat{p}(x)$. Es la función de pérdida estándar para tareas de clasificación.

15. **Decodificador** (*Decoder*): Componente de una arquitectura que transforma la representación intermedia en la salida deseada. En comunicaciones semánticas, el decodificador reconstruye la información semántica a partir de la señal recibida a través del canal.

16. **Descenso del gradiente** (*Gradient Descent*): Algoritmo de optimización iterativo que actualiza los parámetros en la dirección opuesta al gradiente de la función de pérdida: $\mathbf{w}_{t+1} = \mathbf{w}_t - \eta \nabla \mathcal{L}(\mathbf{w}_t)$.

17. **Dropout**: Técnica de regularización que, durante el entrenamiento, desactiva aleatoriamente una fracción $p$ de las neuronas de una capa en cada iteración, forzando a la red a aprender representaciones más robustas y reduciendo el sobreajuste.

18. **E2E** (*End-to-End* / Extremo a extremo): Enfoque de diseño en el que todo el sistema (desde la entrada hasta la salida) se entrena conjuntamente como una sola red neuronal diferenciable, optimizando directamente la métrica de rendimiento final.

19. **Efecto acantilado** (*Cliff Effect*): Fenómeno observado en sistemas de comunicación digital tradicionales donde el rendimiento se degrada abrupta y catastróficamente cuando la SNR cae por debajo de un umbral crítico, en contraste con la degradación gradual de los sistemas analógicos o los sistemas basados en JSCC.

20. **Embedding**: Representación vectorial densa y de baja dimensionalidad de entidades discretas (palabras, tokens, categorías) en un espacio continuo, donde la proximidad geométrica refleja similitud semántica o funcional.

21. **Entropía** (*Entropy*): Medida de la incertidumbre promedio asociada a una variable aleatoria: $H(X) = -\sum_x p(x)\log p(x)$. En teoría de la información, representa el número mínimo de bits necesarios, en promedio, para codificar los resultados de la variable.

22. **Época** (*Epoch*): Una pasada completa por todo el conjunto de datos de entrenamiento. El entrenamiento típicamente requiere múltiples épocas para que los pesos converjan a valores adecuados.

23. **Filtro / Kernel**: Matriz de pesos pequeña (por ejemplo, $3 \times 3$ o $5 \times 5$) que se desliza sobre la entrada en una capa convolucional para detectar patrones locales como bordes, texturas o formas.

24. **Función de activación** (*Activation Function*): Función no lineal aplicada a la salida de una neurona, como ReLU ($f(x) = \max(0,x)$), sigmoide ($\sigma(x) = 1/(1+e^{-x})$) o tanh. Introduce no linealidad en la red, permitiéndole aprender relaciones complejas.

25. **Función de pérdida** (*Loss Function*): Función escalar que cuantifica la discrepancia entre la predicción del modelo y la salida deseada. Su gradiente respecto a los parámetros guía el proceso de entrenamiento. Ejemplos comunes: error cuadrático medio (MSE), entropía cruzada, pérdida semántica.

26. **GPT** (*Generative Pre-trained Transformer*): Familia de modelos de lenguaje basados en el decodificador del Transformer, entrenados de forma auto-regresiva para predecir el siguiente token en una secuencia.

27. **GRU** (*Gated Recurrent Unit*): Variante simplificada de la LSTM que combina las compuertas de olvido y de entrada en una sola compuerta de actualización, reduciendo el número de parámetros mientras mantiene la capacidad de capturar dependencias a largo plazo.

28. **Información mutua** (*Mutual Information*): Medida de la dependencia estadística entre dos variables aleatorias: $I(X;Y) = H(X) - H(X|Y)$. Cuantifica la cantidad de información que una variable proporciona sobre la otra.

29. **ISAC** (*Integrated Sensing and Communications*): Paradigma que integra las funciones de percepción (radar, localización) y comunicación en una sola infraestructura, compartiendo recursos de hardware, espectro y procesamiento de señales.

30. **Layer Normalization** (Normalización de capa): Técnica de normalización que estandariza las activaciones a lo largo de la dimensión de características para cada muestra individual, independientemente del tamaño del lote. Es la normalización predominante en arquitecturas Transformer.

31. **LSTM** (*Long Short-Term Memory*): Tipo de celda de red neuronal recurrente diseñada para capturar dependencias a largo plazo en secuencias, mediante un mecanismo de compuertas (entrada, olvido, salida) que regula el flujo de información a través del estado de celda.

32. **Mapa de características** (*Feature Map*): Salida de una capa convolucional que representa la respuesta de un filtro aplicado sobre la entrada. Cada filtro genera un mapa de características que destaca un patrón específico detectado en la entrada.

33. **MIMO** (*Multiple-Input Multiple-Output*): Tecnología de comunicaciones inalámbricas que utiliza múltiples antenas en el transmisor y el receptor para mejorar la capacidad, la fiabilidad y la eficiencia espectral del enlace.

34. **MLP** (*Multilayer Perceptron* / Perceptrón multicapa): Red neuronal totalmente conectada con una o más capas ocultas, capaz de aproximar funciones continuas arbitrarias según el teorema de aproximación universal.

35. **Multi-Head Attention** (Atención multi-cabeza): Extensión del mecanismo de atención que ejecuta múltiples funciones de atención en paralelo con diferentes proyecciones lineales aprendidas, permitiendo que el modelo atienda simultáneamente a información de diferentes subespacios de representación:
$$\text{MultiHead}(\mathbf{Q}, \mathbf{K}, \mathbf{V}) = \text{Concat}(\text{head}_1, \ldots, \text{head}_h)\mathbf{W}^O$$

36. **OFDM** (*Orthogonal Frequency-Division Multiplexing*): Técnica de modulación multiportadora que divide el espectro disponible en múltiples subportadoras ortogonales de banda estrecha, proporcionando robustez frente al desvanecimiento selectivo en frecuencia y eficiencia espectral.

37. **OTFS** (*Orthogonal Time Frequency Space*): Esquema de modulación que opera en el dominio retardo-Doppler, ofreciendo ventajas sobre OFDM en canales con alta movilidad al representar el canal como una función quasi-estática en el dominio retardo-Doppler.

38. **Overfitting** (Sobreajuste): Fenómeno en el que un modelo se ajusta excesivamente a los datos de entrenamiento, memorizando ruido y particularidades específicas del conjunto de entrenamiento, lo que resulta en un rendimiento pobre sobre datos no vistos.

39. **Perceptrón** (*Perceptron*): Modelo de neurona artificial propuesto por Rosenblatt (1958) que calcula una combinación lineal ponderada de las entradas, le suma un sesgo y aplica una función de activación escalón para producir una salida binaria. Es el bloque de construcción fundamental de las redes neuronales.

40. **Peso** (*Weight*): Parámetro numérico ajustable de una red neuronal que pondera la importancia de cada conexión entre neuronas. Los pesos se ajustan durante el entrenamiento mediante algoritmos de optimización basados en gradientes.

41. **Pooling**: Operación de reducción espacial que reduce las dimensiones de los mapas de características al resumir regiones locales mediante operaciones como el máximo (*max pooling*) o el promedio (*average pooling*), proporcionando cierta invariancia a pequeñas traslaciones y reduciendo la carga computacional.

42. **Positional Encoding** (Codificación posicional): Mecanismo que inyecta información sobre la posición de cada token en una secuencia, necesario en arquitecturas como el Transformer que carecen de recurrencia inherente. Típicamente se implementa mediante funciones sinusoidales:
$$PE_{(pos,2i)} = \sin(pos / 10000^{2i/d_{\text{model}}})$$
$$PE_{(pos,2i+1)} = \cos(pos / 10000^{2i/d_{\text{model}}})$$

43. **Query, Key, Value (Q, K, V)** (Consulta, Clave, Valor): Las tres proyecciones lineales utilizadas en el mecanismo de atención. La *query* representa la consulta de información, la *key* representa las claves contra las que se compara la consulta, y el *value* contiene la información que se agrega ponderadamente según las puntuaciones de atención.

44. **Regularización** (*Regularization*): Conjunto de técnicas para prevenir el sobreajuste, incluyendo regularización L1 ($\lambda\sum|w_i|$), L2 ($\lambda\sum w_i^2$), dropout, data augmentation y early stopping.

45. **Residual Connection** (Conexión residual): Conexión de atajo que suma la entrada de un bloque directamente a su salida ($\mathbf{y} = F(\mathbf{x}) + \mathbf{x}$), facilitando el flujo del gradiente en redes profundas y mitigando el problema de degradación. Introducida por He *et al.* (2016).

46. **Retropropagación** (*Backpropagation*): Algoritmo eficiente para calcular el gradiente de la función de pérdida respecto a todos los pesos de la red, basado en la aplicación recursiva de la regla de la cadena desde la capa de salida hacia la capa de entrada.

47. **RNN** (*Recurrent Neural Network* / Red Neuronal Recurrente): Red neuronal diseñada para procesar datos secuenciales, donde la salida en cada paso temporal depende de la entrada actual y del estado oculto del paso anterior: $\mathbf{h}_t = f(\mathbf{W}_h\mathbf{h}_{t-1} + \mathbf{W}_x\mathbf{x}_t + \mathbf{b})$.

48. **Semantic Communication** (Comunicación semántica): Paradigma de comunicación que busca transmitir el significado o la información semántica del mensaje en lugar de reproducir exactamente la secuencia de bits original, aprovechando técnicas de aprendizaje profundo para lograr mayor eficiencia y robustez.

49. **Semantic Drift** (Deriva semántica): Fenómeno que ocurre cuando las bases de conocimiento o los modelos del transmisor y receptor divergen con el tiempo, causando errores de interpretación semántica. Es un desafío clave en la implementación práctica de sistemas de comunicación semántica.

50. **Sesgo** (*Bias*): (1) En redes neuronales: parámetro aditivo $b$ en la combinación lineal $z = \mathbf{w}^T\mathbf{x} + b$ que permite desplazar la función de activación. (2) En aprendizaje automático: suposiciones implícitas del modelo (*sesgo inductivo*) que facilitan la generalización.

51. **Sigmoide** (*Sigmoid*): Función de activación que mapea valores reales al intervalo $(0,1)$: $\sigma(x) = \frac{1}{1+e^{-x}}$. Históricamente utilizada en redes neuronales, ha sido mayormente reemplazada por ReLU en capas ocultas pero sigue siendo fundamental en compuertas de LSTM/GRU y en la capa de salida para clasificación binaria.

52. **SNR** (*Signal-to-Noise Ratio* / Relación señal a ruido): Métrica que cuantifica la potencia de la señal respecto a la potencia del ruido, típicamente expresada en decibelios: $\text{SNR}_{\text{dB}} = 10\log_{10}(P_s/P_n)$.

53. **Softmax**: Función que transforma un vector de valores reales en una distribución de probabilidad: $\text{softmax}(z_i) = e^{z_i}/\sum_j e^{z_j}$. Se utiliza en la capa de salida para clasificación multiclase y en el mecanismo de atención para obtener pesos de atención normalizados.

54. **Stride** (Paso): Número de posiciones que el filtro se desplaza en cada paso durante la operación de convolución o pooling. Un stride mayor que 1 reduce las dimensiones espaciales de la salida.

55. **Tasa de aprendizaje** (*Learning Rate*): Hiperparámetro $\eta > 0$ que controla el tamaño del paso en la actualización de los pesos durante el descenso del gradiente. Una tasa demasiado alta puede causar divergencia; una demasiado baja, convergencia lenta.

56. **Transformer**: Arquitectura de red neuronal basada enteramente en mecanismos de auto-atención y redes feed-forward, sin recurrencia ni convoluciones. Propuesta por Vaswani *et al.* (2017), permite procesamiento paralelo y captura de dependencias de largo alcance, convirtiéndose en la arquitectura dominante en procesamiento de lenguaje natural, visión por computador y comunicaciones semánticas.

57. **Feed-Forward Network** (Red de propagación hacia adelante): Red neuronal en la que la información fluye exclusivamente desde la entrada hacia la salida, sin conexiones recurrentes ni retroalimentación. En el contexto del Transformer, se refiere a la subred de dos capas lineales con activación no lineal intermedia que se aplica posición por posición tras la capa de atención.

58. **Red generativa adversarial** (*GAN – Generative Adversarial Network*): Arquitectura compuesta por un generador y un discriminador que se entrenan de forma adversarial. En comunicaciones semánticas, los GAN se utilizan para modelar canales complejos y para mejorar la calidad de la reconstrucción semántica.

59. **Desvanecimiento del gradiente** (*Vanishing Gradient*): Problema que ocurre en redes profundas cuando los gradientes se hacen exponencialmente pequeños al propagarse hacia las capas iniciales, dificultando el aprendizaje de las primeras capas. Es especialmente pronunciado con funciones de activación saturantes como la sigmoide y la tangente hiperbólica.

60. **Explosión del gradiente** (*Exploding Gradient*): Problema opuesto al desvanecimiento, donde los gradientes crecen exponencialmente durante la retropropagación, causando inestabilidad numérica y actualizaciones de pesos excesivamente grandes. Se mitiga mediante técnicas como el recorte de gradiente (*gradient clipping*).

61. **Cuantización** (*Quantization*): Técnica de compresión de modelos que reduce la precisión numérica de los pesos y activaciones (por ejemplo, de punto flotante de 32 bits a enteros de 8 bits), reduciendo el tamaño del modelo y acelerando la inferencia con una pérdida mínima de rendimiento.

62. **Destilación de conocimiento** (*Knowledge Distillation*): Técnica en la que un modelo pequeño (estudiante) se entrena para replicar el comportamiento de un modelo grande (profesor), transfiriendo el conocimiento aprendido a una arquitectura más eficiente.

---

## 10.4 Referencias bibliográficas

Las siguientes referencias se organizan por área temática y han sido verificadas con sus respectivos identificadores DOI o de publicación.

### Fundamentos de redes neuronales

[1] F. Rosenblatt, "The Perceptron: A Probabilistic Model for Information Storage and Organization in the Brain," *Psychological Review*, vol. 65, no. 6, pp. 386–408, 1958. DOI: [10.1037/h0042519](https://doi.org/10.1037/h0042519)

[2] D. E. Rumelhart, G. E. Hinton, y R. J. Williams, "Learning representations by back-propagating errors," *Nature*, vol. 323, pp. 533–536, 1986. DOI: [10.1038/323533a0](https://doi.org/10.1038/323533a0)

[3] K. Hornik, "Approximation capabilities of multilayer feedforward networks," *Neural Networks*, vol. 4, no. 2, pp. 251–257, 1991. DOI: [10.1016/0893-6080(91)90009-T](https://doi.org/10.1016/0893-6080(91)90009-T)

[4] Y. LeCun, L. Bottou, Y. Bengio, y P. Haffner, "Gradient-based learning applied to document recognition," *Proceedings of the IEEE*, vol. 86, no. 11, pp. 2278–2324, 1998. DOI: [10.1109/5.726791](https://doi.org/10.1109/5.726791)

[5] S. Hochreiter y J. Schmidhuber, "Long Short-Term Memory," *Neural Computation*, vol. 9, no. 8, pp. 1735–1780, 1997. DOI: [10.1162/neco.1997.9.8.1735](https://doi.org/10.1162/neco.1997.9.8.1735)

### Mecanismos de atención y Transformers

[6] D. Bahdanau, K. Cho, y Y. Bengio, "Neural Machine Translation by Jointly Learning to Align and Translate," en *Proc. International Conference on Learning Representations (ICLR)*, 2015. arXiv: [1409.0473](https://arxiv.org/abs/1409.0473)

[7] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, Ł. Kaiser, e I. Polosukhin, "Attention Is All You Need," en *Advances in Neural Information Processing Systems (NeurIPS)*, vol. 30, 2017. DOI: [10.48550/arXiv.1706.03762](https://doi.org/10.48550/arXiv.1706.03762)

[8] J. Devlin, M.-W. Chang, K. Lee, y K. Toutanova, "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding," en *Proc. North American Chapter of the Association for Computational Linguistics (NAACL)*, 2019. DOI: [10.18653/v1/N19-1423](https://doi.org/10.18653/v1/N19-1423)

### Comunicaciones semánticas

[9] C. E. Shannon, "A Mathematical Theory of Communication," *Bell System Technical Journal*, vol. 27, pp. 379–423, 623–656, 1948. DOI: [10.1002/j.1538-7305.1948.tb01338.x](https://doi.org/10.1002/j.1538-7305.1948.tb01338.x)

[10] H. Xie, Z. Qin, G. Y. Li, y B.-H. Juang, "Deep Learning Enabled Semantic Communication Systems," *IEEE Transactions on Signal Processing*, vol. 69, pp. 2663–2675, 2021. DOI: [10.1109/TSP.2021.3071082](https://doi.org/10.1109/TSP.2021.3071082)

[11] E. Bourtsoulatze, D. Burth Kurka, y D. Gündüz, "Deep Joint Source-Channel Coding for Wireless Image Transmission," *IEEE Transactions on Cognitive Communications and Networking*, vol. 5, no. 3, pp. 567–579, 2019. DOI: [10.1109/TCCN.2019.2919300](https://doi.org/10.1109/TCCN.2019.2919300)

[12] X. Luo, H.-H. Chen, y Q. Guo, "Semantic Communications: Overview, Open Issues, and Future Research Directions," *IEEE Wireless Communications*, vol. 29, no. 1, pp. 210–219, 2022. DOI: [10.1109/MWC.101.2100269](https://doi.org/10.1109/MWC.101.2100269)

### Aprendizaje profundo para comunicaciones

[13] T. O'Shea y J. Hoydis, "An Introduction to Deep Learning for the Physical Layer," *IEEE Transactions on Cognitive Communications and Networking*, vol. 3, no. 4, pp. 563–575, 2017. DOI: [10.1109/TCCN.2017.2758370](https://doi.org/10.1109/TCCN.2017.2758370)

[14] K. He, X. Zhang, S. Ren, y J. Sun, "Deep Residual Learning for Image Recognition," en *Proc. IEEE Conference on Computer Vision and Pattern Recognition (CVPR)*, pp. 770–778, 2016. DOI: [10.1109/CVPR.2016.90](https://doi.org/10.1109/CVPR.2016.90)

### Teoría de la información y comunicaciones

[15] C. E. Shannon y W. Weaver, *The Mathematical Theory of Communication*. Urbana, IL: University of Illinois Press, 1949. ISBN: 978-0252725463

[16] T. M. Cover y J. A. Thomas, *Elements of Information Theory*, 2.ª ed. Hoboken, NJ: Wiley-Interscience, 2006. DOI: [10.1002/047174882X](https://doi.org/10.1002/047174882X)

### Aprendizaje profundo — textos generales

[17] I. Goodfellow, Y. Bengio, y A. Courville, *Deep Learning*. Cambridge, MA: MIT Press, 2016. ISBN: 978-0262035613. Disponible en: [https://www.deeplearningbook.org](https://www.deeplearningbook.org)

[18] Y. LeCun, Y. Bengio, y G. Hinton, "Deep learning," *Nature*, vol. 521, pp. 436–444, 2015. DOI: [10.1038/nature14539](https://doi.org/10.1038/nature14539)

---

*Fin del tutorial.*

*Este tutorial ha proporcionado una introducción integral a las herramientas de inteligencia artificial —desde el perceptrón hasta los Transformers— y su aplicación en los sistemas de comunicación semántica. Esperamos que sirva como punto de partida sólido para investigadores, estudiantes e ingenieros interesados en esta fascinante intersección entre la inteligencia artificial y las telecomunicaciones.*
