# 8. Sistemas de Comunicación Semántica de Extremo a Extremo (E2E)

Los capítulos anteriores han establecido los fundamentos teóricos del aprendizaje profundo, la teoría de la información semántica y las arquitecturas neuronales que constituyen los bloques de construcción de los sistemas modernos de comunicación. En esta sección, integramos todos estos componentes para presentar el diseño, entrenamiento y operación de **sistemas de comunicación semántica de extremo a extremo** (*End-to-End Semantic Communication Systems*, E2E SemCom). A diferencia de los sistemas de comunicación convencionales —donde la codificación de fuente, la codificación de canal y la modulación se diseñan y optimizan por separado—, los sistemas E2E proponen un paradigma radicalmente distinto: **todas las etapas del transmisor y receptor se entrenan conjuntamente como una única red neuronal**, optimizando directamente una métrica de fidelidad semántica a nivel de significado, en lugar de minimizar la tasa de error de bit.

Este enfoque, inspirado en los autoencoders profundos y catalizado por los avances en redes neuronales diferenciables, permite que el sistema aprenda representaciones intermedias que no corresponden necesariamente a símbolos discretos de una constelación clásica, sino a **vectores latentes semánticos** optimizados para sobrevivir las distorsiones del canal físico manteniendo el contenido semántico relevante. El resultado es un sistema que exhibe propiedades notablemente superiores a los sistemas convencionales, incluyendo degradación suave en lugar del efecto acantilado, compresión adaptativa del contenido semántico, y robustez intrínseca al ruido del canal.

A lo largo de esta sección, desarrollaremos cada componente con rigor matemático, proporcionaremos descripciones detalladas de las arquitecturas, analizaremos las funciones de pérdida apropiadas para distintas modalidades de datos, y culminaremos con una implementación completa en PyTorch que el lector podrá utilizar como punto de partida para sus propias investigaciones.

---

## 8.1 Arquitectura E2E: Encoder Semántico-Canal (Transmisor)

### 8.1.1 Visión general del transmisor semántico

El transmisor en un sistema de comunicación semántica E2E tiene una función fundamentalmente diferente a la de un transmisor convencional. En un sistema clásico, el transmisor realiza secuencialmente tres operaciones independientes: (1) la codificación de fuente, que comprime los datos eliminando redundancia estadística (por ejemplo, mediante algoritmos como Huffman, Lempel-Ziv o transformadas como la DCT en JPEG); (2) la codificación de canal, que añade redundancia controlada para proteger contra errores del canal (mediante códigos como Turbo, LDPC o Polar); y (3) la modulación, que mapea los bits codificados a símbolos de una constelación (como QAM o PSK) aptos para la transmisión por el medio físico. Cada una de estas etapas se diseña aplicando el teorema de separación fuente-canal de Shannon, que garantiza que la optimización independiente es óptima asintóticamente.

Sin embargo, el teorema de separación de Shannon se aplica bajo condiciones idealizadas: longitud de bloque infinita, distribuciones estacionarias y ergódicas, y sin restricciones de complejidad. En la práctica, con longitudes de bloque finitas, datos no estacionarios (como texto, imágenes o video) y requisitos de latencia estrictos, la separación es subóptima. Los sistemas E2E explotan esta observación al **fusionar todas las etapas del transmisor en una única red neuronal** que aprende simultáneamente a extraer significado, comprimir la información semántica relevante y codificarla de manera robusta para su transmisión por el canal.

### 8.1.2 El encoder semántico

El **encoder semántico** es la primera etapa del transmisor. Su función es transformar los datos de origen $\mathbf{s}$ en una representación latente semántica $\mathbf{h}$ que capture el significado esencial del mensaje, descartando la información irrelevante o redundante desde el punto de vista de la tarea comunicativa. Formalmente, el encoder semántico se define como una función parametrizada:

$$\mathbf{h} = f_{\theta_{se}}(\mathbf{s})$$

donde $\mathbf{s} \in \mathcal{S}$ es el dato de origen (que puede ser un texto, una imagen, una señal de audio, etc.), $f_{\theta_{se}}$ es la función de codificación semántica implementada por una red neuronal con parámetros $\theta_{se}$, y $\mathbf{h} \in \mathbb{R}^{k}$ es el vector de características semánticas de dimensión $k$.

La arquitectura del encoder semántico depende de la modalidad de los datos de entrada. Para **datos textuales**, la arquitectura dominante es el Transformer, que utiliza mecanismos de auto-atención (*self-attention*) para capturar dependencias a largo plazo entre las palabras de la oración. El texto de entrada se tokeniza primero en una secuencia de tokens $\mathbf{s} = (s_1, s_2, \ldots, s_L)$, donde $L$ es la longitud de la secuencia. Cada token $s_i$ se mapea a un vector de *embedding* $\mathbf{e}_i \in \mathbb{R}^{d_{model}}$ mediante una matriz de *embeddings* $\mathbf{E} \in \mathbb{R}^{|V| \times d_{model}}$, donde $|V|$ es el tamaño del vocabulario. A estos *embeddings* se les añade la codificación posicional:

$$\mathbf{e}_i' = \mathbf{e}_i + \mathbf{PE}(i)$$

donde $\mathbf{PE}(i)$ es el vector de codificación posicional para la posición $i$, típicamente definido mediante funciones sinusoidales:

$$\text{PE}(i, 2j) = \sin\left(\frac{i}{10000^{2j/d_{model}}}\right), \quad \text{PE}(i, 2j+1) = \cos\left(\frac{i}{10000^{2j/d_{model}}}\right)$$

La secuencia de *embeddings* con posición $(\mathbf{e}_1', \mathbf{e}_2', \ldots, \mathbf{e}_L')$ se procesa a través de $N_{se}$ capas de Transformer encoder, cada una de las cuales aplica:

$$\mathbf{H}^{(l)} = \text{TransformerLayer}^{(l)}(\mathbf{H}^{(l-1)})$$

donde cada capa consiste en auto-atención multi-cabeza seguida de una red *feed-forward* con conexiones residuales y normalización de capa. La salida final $\mathbf{H}^{(N_{se})}$ es una representación contextualizada de la secuencia completa.

Para **datos de imagen**, el encoder semántico típicamente emplea una arquitectura de red neuronal convolucional (CNN), como una ResNet o una red similar, que progresivamente reduce la resolución espacial mientras incrementa la profundidad de canales de características. La imagen de entrada $\mathbf{s} \in \mathbb{R}^{H \times W \times C}$ se transforma en un mapa de características $\mathbf{h} \in \mathbb{R}^{H' \times W' \times C'}$ donde $H' \ll H$, $W' \ll W$ y $C' \gg C$. Alternativamente, arquitecturas más recientes emplean Vision Transformers (ViT), que dividen la imagen en parches y los procesan con capas de Transformer.

### 8.1.3 El encoder de canal

El **encoder de canal** toma la representación semántica $\mathbf{h}$ producida por el encoder semántico y la transforma en un vector de símbolos de canal $\mathbf{z}$ adecuado para la transmisión por el medio físico. Formalmente:

$$\mathbf{z} = f_{\theta_{ce}}(\mathbf{h})$$

donde $f_{\theta_{ce}}$ es la función de codificación de canal implementada por una red neuronal con parámetros $\theta_{ce}$, y $\mathbf{z} \in \mathbb{R}^{2n}$ es el vector de símbolos de canal (donde el factor 2 aparece porque cada símbolo complejo se representa como dos valores reales: parte real e imaginaria, o bien I y Q en cuadratura).

La arquitectura del encoder de canal consiste típicamente en una o más **capas densas** (*fully connected layers*) que mapean el espacio semántico al espacio de símbolos de canal. Cada capa realiza la operación:

$$\mathbf{z}^{(l)} = \sigma\left(\mathbf{W}^{(l)} \mathbf{z}^{(l-1)} + \mathbf{b}^{(l)}\right)$$

donde $\mathbf{W}^{(l)}$ y $\mathbf{b}^{(l)}$ son los pesos y sesgos de la capa $l$, y $\sigma(\cdot)$ es una función de activación no lineal (típicamente ReLU o GELU para capas intermedias). La última capa no utiliza función de activación, permitiendo que los símbolos de salida tomen cualquier valor real.

### 8.1.4 Diseño conjunto y formulación compuesta

La operación completa del transmisor se expresa como la composición de ambos encoders:

$$\mathbf{z} = f_{\theta_{ce}}\left(f_{\theta_{se}}(\mathbf{s})\right)$$

Esta formulación enfatiza que el transmisor completo es una única función diferenciable parametrizada por $\theta_{tx} = \{\theta_{se}, \theta_{ce}\}$. La clave del diseño E2E es que **no existe una interfaz de bits entre el encoder semántico y el encoder de canal**: la representación intermedia $\mathbf{h}$ es un vector de valores reales continuos, no una secuencia de bits. Esto permite que la información fluya de manera más eficiente entre las etapas y que los gradientes se propaguen sin obstáculos durante el entrenamiento.

Esta ausencia de la interfaz binaria tradicional es, simultáneamente, una de las mayores fortalezas y uno de los desafíos más significativos de los sistemas E2E. La fortaleza radica en que elimina la pérdida de información inherente a la cuantización y permite una optimización verdaderamente conjunta. El desafío es que rompe la compatibilidad con los estándares de comunicación existentes y dificulta la interoperabilidad con otros sistemas.

### 8.1.5 Normalización de potencia

Para que los símbolos transmitidos $\mathbf{z}$ sean físicamente realizables, es necesario imponer una **restricción de potencia** que limite la energía promedio de la señal transmitida. Esta restricción se expresa como:

$$\mathbb{E}\left[||\mathbf{z}||^2\right] \leq P$$

donde $P$ es la potencia máxima permitida y $||\cdot||^2$ denota la norma euclidiana al cuadrado. En la práctica, esta restricción se implementa mediante una **capa de normalización de potencia** al final del encoder de canal. Las dos estrategias más comunes son:

**Normalización por lote** (*batch normalization*): Se normaliza cada símbolo para que el promedio sobre todo el lote de entrenamiento cumpla la restricción:

$$\mathbf{z}_{norm} = \sqrt{nP} \cdot \frac{\mathbf{z}}{||\mathbf{z}||_2}$$

donde $n$ es el número de usos del canal (dimensión de $\mathbf{z}$ dividida por 2 para canales complejos). Esta normalización garantiza que $||\mathbf{z}_{norm}||^2 = nP$ exactamente, lo cual es una restricción de potencia promedio por bloque.

**Normalización promedio** (*average power constraint*): Se normaliza para que la potencia promedio por símbolo sea igual a $P/n$:

$$\mathbf{z}_{norm} = \sqrt{P} \cdot \frac{\mathbf{z}}{\sqrt{\frac{1}{B}\sum_{b=1}^{B}||\mathbf{z}_b||^2}}$$

donde $B$ es el tamaño del lote. Esta normalización es más suave y permite variaciones en la potencia instantánea entre diferentes muestras, lo cual puede ser beneficioso para el aprendizaje de constelaciones adaptativas.

### 8.1.6 La razón de codificación $k/n$

Un parámetro fundamental del sistema es la **razón de codificación** o **tasa de compresión semántica**, definida como:

$$R = \frac{k}{n}$$

donde $k$ es la dimensión de la representación semántica (o equivalentemente, el número de valores reales que describen el significado del mensaje original) y $n$ es el número de usos del canal (o símbolos complejos transmitidos). Esta razón cuantifica el grado de compresión que el sistema aplica sobre la información semántica.

Cuando $R < 1$, el sistema está comprimiendo: transmite menos símbolos de los necesarios para representar completamente la información semántica. Esto es posible porque el encoder de canal aprende a codificar la información semántica de manera redundante solo donde es necesario para la protección contra errores. Cuando $R > 1$, el sistema está expandiendo, lo que corresponde a una codificación de canal fuerte que proporciona mayor protección.

La elección de $R$ implica un compromiso fundamental entre **eficiencia espectral** (valores bajos de $R$ permiten transmitir más información semántica por uso del canal) y **robustez** (valores altos de $R$ proporcionan mayor protección contra el ruido del canal a costa de utilizar más recursos de canal). En los sistemas E2E, este compromiso se aprende automáticamente durante el entrenamiento, en contraste con los sistemas convencionales donde debe diseñarse manualmente seleccionando tasas de codificación de fuente y canal específicas.

### 8.1.7 Diagrama del transmisor

> **Figura 8.1:** Arquitectura detallada del transmisor semántico E2E. El dato de origen $\mathbf{s}$ (por ejemplo, una oración de texto) ingresa al **Encoder Semántico**, compuesto por una capa de *embedding* seguida de $N_{se}$ capas de Transformer (cada una con auto-atención multi-cabeza, normalización de capa y red *feed-forward*). La salida del Transformer produce la representación semántica $\mathbf{h} \in \mathbb{R}^k$. Esta representación alimenta al **Encoder de Canal**, formado por una secuencia de capas densas con activaciones no lineales (Dense $\rightarrow$ ReLU $\rightarrow$ Dense $\rightarrow$ ReLU $\rightarrow$ Dense) que transforman progresivamente las dimensiones: $k \rightarrow 256 \rightarrow 128 \rightarrow 2n$. La salida pasa por una **capa de normalización de potencia** que asegura $\mathbb{E}[||\mathbf{z}||^2] \leq P$, produciendo el vector de símbolos de canal $\mathbf{z} \in \mathbb{R}^{2n}$ listo para la transmisión. Las flechas de gradiente (punteadas, en dirección opuesta) ilustran el flujo de retropropagación durante el entrenamiento.

---

## 8.2 El Canal Físico como Capa Diferenciable

### 8.2.1 Motivación: el canal como capa de la red neuronal

En el paradigma E2E, el canal de comunicación ocupa una posición central y a la vez paradójica. Por un lado, es un componente que **no se puede modificar ni optimizar**: el medio físico (aire, fibra óptica, cable) introduce distorsiones que son gobernadas por las leyes de la física electromagnética. Por otro lado, el entrenamiento E2E requiere que los gradientes de la función de pérdida fluyan **a través de todos los componentes del sistema**, incluyendo el canal, para actualizar los parámetros del transmisor. Esto exige que el canal se modele como una **capa diferenciable** dentro de la red neuronal completa.

La clave conceptual es la siguiente: aunque el canal real no tiene parámetros que optimizar, su modelo matemático puede incorporarse como una capa estocástica fija (sin parámetros entrenables) dentro del grafo computacional. Los gradientes no necesitan fluir *a través* del canal para actualizar parámetros del canal (que no existen), pero sí necesitan fluir *a través del modelo del canal* para llegar a los parámetros del transmisor. Esto es posible siempre que el modelo del canal sea diferenciable con respecto a su entrada $\mathbf{z}$.

### 8.2.2 Canal AWGN (Ruido Gaussiano Blanco Aditivo)

El modelo de canal más fundamental es el **canal AWGN** (*Additive White Gaussian Noise*), que modela un canal ideal con únicamente ruido térmico aditivo. La relación entrada-salida es:

$$\mathbf{y} = \mathbf{z} + \mathbf{n}$$

donde $\mathbf{z} \in \mathbb{R}^{2n}$ es el vector de símbolos transmitidos, $\mathbf{n} \sim \mathcal{N}(\mathbf{0}, \sigma^2\mathbf{I})$ es el vector de ruido gaussiano con media cero y varianza $\sigma^2$ por componente, y $\mathbf{y} \in \mathbb{R}^{2n}$ es el vector recibido. El término $\mathbf{I}$ denota la matriz identidad de dimensión apropiada, indicando que las componentes de ruido son independientes e idénticamente distribuidas (*i.i.d.*).

La diferenciabilidad de este canal con respecto a $\mathbf{z}$ es inmediata y elegante: puesto que la relación es lineal (una simple suma), el gradiente de $\mathbf{y}$ respecto a $\mathbf{z}$ es:

$$\frac{\partial \mathbf{y}}{\partial \mathbf{z}} = \mathbf{I}$$

Es decir, el gradiente pasa sin modificación a través del canal AWGN. La aleatoriedad del ruido no afecta la diferenciabilidad porque $\mathbf{n}$ no depende de $\mathbf{z}$. Esto convierte al canal AWGN en la capa diferenciable más sencilla posible: es equivalente a una capa de *dropout* que, en lugar de poner a cero aleatoriamente algunas activaciones, añade perturbaciones gaussianas a todas.

### 8.2.3 Canal con desvanecimiento Rayleigh

En entornos de comunicación inalámbrica, especialmente en escenarios urbanos o interiores donde no existe línea de vista directa entre transmisor y receptor, el canal experimenta **desvanecimiento Rayleigh** (*Rayleigh fading*). Este fenómeno se produce cuando la señal llega al receptor por múltiples trayectos, cada uno con diferente amplitud, fase y retardo, y ninguno de ellos es dominante. El modelo entrada-salida es:

$$\mathbf{y} = \mathbf{h} \odot \mathbf{z} + \mathbf{n}$$

donde $\odot$ denota el producto elemento a elemento (producto de Hadamard), $\mathbf{h} \sim \mathcal{CN}(\mathbf{0}, \mathbf{I})$ es el vector de coeficientes de desvanecimiento que sigue una distribución compleja gaussiana circular con media cero y varianza unitaria, y $\mathbf{n} \sim \mathcal{CN}(\mathbf{0}, \sigma^2\mathbf{I})$ es el ruido complejo gaussiano. El término $\mathcal{CN}$ denota la distribución gaussiana circular compleja.

En la representación en componentes reales (partes real e imaginaria separadas), cada coeficiente de canal $h_i = h_i^{(R)} + jh_i^{(I)}$ tiene partes real e imaginaria que son variables aleatorias gaussianas independientes: $h_i^{(R)}, h_i^{(I)} \sim \mathcal{N}(0, 1/2)$. La magnitud $|h_i|$ sigue una distribución Rayleigh con parámetro $\sigma_h = 1/\sqrt{2}$:

$$f_{|h_i|}(r) = 2r \cdot e^{-r^2}, \quad r \geq 0$$

La diferenciabilidad del canal Rayleigh con respecto a $\mathbf{z}$ se verifica fácilmente. Dado que la operación es un producto elemento a elemento, el gradiente es:

$$\frac{\partial y_i}{\partial z_i} = h_i$$

Es decir, el gradiente se escala por el coeficiente de canal correspondiente. En términos matriciales:

$$\frac{\partial \mathbf{y}}{\partial \mathbf{z}} = \text{diag}(\mathbf{h})$$

donde $\text{diag}(\mathbf{h})$ es la matriz diagonal cuyos elementos diagonales son las componentes de $\mathbf{h}$. Esto significa que durante la retropropagación, los gradientes que llegan al transmisor están modulados por la realización del canal, lo cual tiene una interpretación intuitiva: el sistema aprende a transmitir de manera que sea robusto frente a las variaciones de ganancia del canal.

### 8.2.4 Canal con desvanecimiento Riciano

Cuando existe una componente de **línea de vista** (*Line-of-Sight*, LoS) dominante entre transmisor y receptor, además de las componentes multitrayecto, el canal se modela mediante el **desvanecimiento Riciano** (*Rician fading*). El modelo entrada-salida tiene la misma estructura multiplicativa:

$$\mathbf{y} = \mathbf{h}_{Ric} \odot \mathbf{z} + \mathbf{n}$$

pero el vector de coeficientes de canal $\mathbf{h}_{Ric}$ se descompone en una componente determinista (LoS) y una componente aleatoria (dispersión):

$$\mathbf{h}_{Ric} = \sqrt{\frac{K}{K+1}} \mathbf{h}_{LoS} + \sqrt{\frac{1}{K+1}} \mathbf{h}_{NLoS}$$

donde $K$ es el **factor Riciano** (también llamado factor $K$), que cuantifica la razón de potencia entre la componente LoS y la componente dispersa. $\mathbf{h}_{LoS}$ es el vector de respuesta de la componente de línea de vista (típicamente un vector de fase $\mathbf{h}_{LoS} = e^{j\phi}\mathbf{1}$ para un canal de banda estrecha), y $\mathbf{h}_{NLoS} \sim \mathcal{CN}(\mathbf{0}, \mathbf{I})$ es la componente dispersa que sigue la distribución Rayleigh.

El factor $K$ controla la severidad del desvanecimiento:
- Cuando $K = 0$: no hay componente LoS, y el canal se reduce al modelo Rayleigh.
- Cuando $K \to \infty$: la componente LoS domina completamente y el canal se aproxima a un canal AWGN con ganancia fija.
- Para valores intermedios de $K$ (típicamente $K = 3$ a $K = 10$ dB en escenarios prácticos): coexisten ambas componentes.

La magnitud de cada coeficiente de canal $|h_{Ric,i}|$ sigue la distribución Rice:

$$f_{|h_{Ric,i}|}(r) = \frac{2r(K+1)}{1} \cdot e^{-K - (K+1)r^2} \cdot I_0\left(2r\sqrt{K(K+1)}\right), \quad r \geq 0$$

donde $I_0(\cdot)$ es la función de Bessel modificada de primera especie de orden cero. La diferenciabilidad del canal Riciano es idéntica a la del canal Rayleigh, ya que la estructura multiplicativa se mantiene.

### 8.2.5 Relación señal a ruido (SNR)

La **relación señal a ruido** (*Signal-to-Noise Ratio*, SNR) es el parámetro fundamental que caracteriza la calidad del canal. Se define como la razón entre la potencia de la señal transmitida y la potencia del ruido:

$$\text{SNR} = \frac{P}{\sigma^2}$$

donde $P = \mathbb{E}[||\mathbf{z}||^2]/n$ es la potencia promedio por símbolo (asumiendo $n$ símbolos complejos o $2n$ símbolos reales) y $\sigma^2$ es la varianza del ruido por componente. En decibelios (dB), la SNR se expresa como:

$$\text{SNR}_{\text{dB}} = 10\log_{10}\left(\frac{P}{\sigma^2}\right)$$

La escala logarítmica en decibelios es la convención estándar en telecomunicaciones porque permite expresar de manera compacta rangos muy amplios de SNR. Valores típicos en sistemas de comunicación prácticos van desde $\text{SNR}_{\text{dB}} \approx -5$ dB (canales muy ruidosos, como comunicaciones en el límite de cobertura celular) hasta $\text{SNR}_{\text{dB}} \approx 30$ dB (canales de alta calidad, como comunicaciones por fibra óptica o enlaces inalámbricos de corto alcance).

Durante el entrenamiento del sistema E2E, la varianza del ruido $\sigma^2$ se calcula a partir de la SNR deseada y la potencia de la señal (normalizada a $P = 1$ típicamente):

$$\sigma^2 = \frac{P}{10^{\text{SNR}_{\text{dB}}/10}} = 10^{-\text{SNR}_{\text{dB}}/10}$$

Esta relación permite simular diferentes condiciones de canal durante el entrenamiento simplemente ajustando el valor de $\sigma^2$ al generar el ruido gaussiano.

### 8.2.6 Requisito de diferenciabilidad para la retropropagación

El entrenamiento de redes neuronales mediante descenso de gradiente estocástico (SGD) requiere calcular las derivadas parciales de la función de pérdida $L$ con respecto a todos los parámetros del modelo. En un sistema E2E, los parámetros del transmisor $\theta_{tx}$ aparecen *antes* del canal en el grafo computacional. Para calcular $\frac{\partial L}{\partial \theta_{tx}}$ mediante la regla de la cadena, necesitamos:

$$\frac{\partial L}{\partial \theta_{tx}} = \frac{\partial L}{\partial \hat{\mathbf{s}}} \cdot \frac{\partial \hat{\mathbf{s}}}{\partial \mathbf{y}} \cdot \frac{\partial \mathbf{y}}{\partial \mathbf{z}} \cdot \frac{\partial \mathbf{z}}{\partial \theta_{tx}}$$

El factor crítico es $\frac{\partial \mathbf{y}}{\partial \mathbf{z}}$, que requiere que el canal sea diferenciable con respecto a su entrada. Como hemos visto, para los canales AWGN y con desvanecimiento, este gradiente existe y es sencillo de calcular. Sin embargo, hay situaciones donde la diferenciabilidad no es trivial, por ejemplo, cuando el canal incluye cuantización (conversión analógico-digital), detección de umbral, o cualquier operación discontinua.

### 8.2.7 El truco de reparametrización para canales estocásticos

Aunque los canales estudiados son diferenciables con respecto a $\mathbf{z}$, la presencia de variables aleatorias ($\mathbf{n}$, $\mathbf{h}$) introduce un desafío computacional. Al entrenar, necesitamos calcular el gradiente de la esperanza de la pérdida:

$$\nabla_{\theta_{tx}} \mathbb{E}_{\mathbf{n}, \mathbf{h}}\left[L\left(g_{\theta_{rx}}(\mathbf{h} \odot f_{\theta_{tx}}(\mathbf{s}) + \mathbf{n}), \mathbf{s}\right)\right]$$

El **truco de reparametrización** (*reparameterization trick*), popularizado por Kingma y Welling en el contexto de los autoencoders variacionales (VAE), permite mover el operador de gradiente dentro de la esperanza. La idea es expresar las variables aleatorias como transformaciones deterministas de una variable auxiliar con distribución fija. Para el canal AWGN:

$$\mathbf{y} = \mathbf{z} + \sigma \boldsymbol{\epsilon}, \quad \boldsymbol{\epsilon} \sim \mathcal{N}(\mathbf{0}, \mathbf{I})$$

Aquí, $\boldsymbol{\epsilon}$ es una variable aleatoria que no depende de los parámetros del modelo. La varianza del ruido $\sigma$ actúa como un factor de escala determinista. Esto permite escribir:

$$\nabla_{\theta_{tx}} \mathbb{E}_{\boldsymbol{\epsilon}}\left[L\left(g_{\theta_{rx}}(\mathbf{z} + \sigma\boldsymbol{\epsilon}), \mathbf{s}\right)\right] = \mathbb{E}_{\boldsymbol{\epsilon}}\left[\nabla_{\theta_{tx}} L\left(g_{\theta_{rx}}(\mathbf{z} + \sigma\boldsymbol{\epsilon}), \mathbf{s}\right)\right]$$

El intercambio del gradiente y la esperanza es válido bajo condiciones de regularidad suaves (que se cumplen para las distribuciones gaussianas y funciones de pérdida suaves). En la práctica, la esperanza se aproxima mediante Monte Carlo con una sola muestra por cada elemento del mini-lote:

$$\nabla_{\theta_{tx}} L \approx \frac{1}{B} \sum_{b=1}^{B} \nabla_{\theta_{tx}} L\left(g_{\theta_{rx}}(\mathbf{z}_b + \sigma\boldsymbol{\epsilon}_b), \mathbf{s}_b\right)$$

donde $\boldsymbol{\epsilon}_b \sim \mathcal{N}(\mathbf{0}, \mathbf{I})$ se muestrea de forma independiente para cada elemento del lote. Esta aproximación es no sesgada y tiene varianza controlable (que disminuye con $1/B$).

Para el canal Rayleigh, la reparametrización es análoga:

$$\mathbf{y} = (\boldsymbol{\epsilon}_h) \odot \mathbf{z} + \sigma\boldsymbol{\epsilon}_n$$

donde $\boldsymbol{\epsilon}_h \sim \mathcal{CN}(\mathbf{0}, \mathbf{I})$ y $\boldsymbol{\epsilon}_n \sim \mathcal{CN}(\mathbf{0}, \mathbf{I})$ son variables auxiliares independientes de los parámetros del modelo.

### 8.2.8 Visualización del efecto del canal

> **Figura 8.2:** Efecto de los modelos de canal sobre los símbolos transmitidos, visualizado en un diagrama de constelación (plano I-Q). Se muestran tres paneles: **(a) Canal AWGN:** los símbolos transmitidos (puntos azules) se dispersan isotrópicamente alrededor de sus posiciones originales, formando nubes gaussianas circulares. La dispersión es proporcional a $\sigma$. A SNR alta, las nubes son compactas y separables; a SNR baja, se solapan causando errores. **(b) Canal Rayleigh:** los símbolos experimentan rotaciones y escalados aleatorios (cada símbolo se multiplica por un coeficiente complejo aleatorio $h_i$), produciendo una dispersión no uniforme que incluye desvanecimiento profundo (símbolos que se atenúan casi a cero). La nube resultante tiene una envolvente Rayleigh que concentra energía cerca del origen. **(c) Canal Riciano ($K = 5$ dB):** el efecto es intermedio; la componente LoS mantiene una dirección preferencial mientras la componente dispersa añade variación, generando una distribución Rice en la magnitud de los símbolos recibidos. En los tres paneles, los puntos rojos representan los símbolos recibidos $\mathbf{y}$ y las flechas verdes ilustran la distorsión introducida por el canal.

---

## 8.3 El Decoder Semántico-Canal (Receptor)

### 8.3.1 Estructura general del receptor

El receptor en un sistema de comunicación semántica E2E tiene la tarea de reconstruir el dato original $\mathbf{s}$ (o una aproximación semánticamente fiel $\hat{\mathbf{s}}$) a partir de la señal recibida $\mathbf{y}$, que ha sido corrompida por el canal. Al igual que el transmisor se divide conceptualmente en encoder semántico y encoder de canal, el receptor se estructura en dos etapas complementarias: el **decoder de canal** y el **decoder semántico**.

### 8.3.2 El decoder de canal

El **decoder de canal** es la primera etapa del receptor. Recibe la señal ruidosa $\mathbf{y}$ y produce una estimación de la representación semántica $\hat{\mathbf{h}}$:

$$\hat{\mathbf{h}} = g_{\theta_{cd}}(\mathbf{y})$$

donde $g_{\theta_{cd}}$ es la función de decodificación de canal implementada por una red neuronal con parámetros $\theta_{cd}$. La función de este componente es *deshacer* las distorsiones del canal —ruido, desvanecimiento, interferencia— y recuperar la representación semántica latente que fue codificada por el transmisor.

Arquitectónicamente, el decoder de canal suele ser el espejo del encoder de canal: si el encoder de canal utilizó capas densas para reducir la dimensión desde $k$ (espacio semántico) hasta $2n$ (espacio de canal), el decoder de canal utiliza capas densas que transforman desde $2n$ de vuelta a $k$. Cada capa aplica:

$$\hat{\mathbf{h}}^{(l)} = \sigma\left(\mathbf{W}_{cd}^{(l)} \hat{\mathbf{h}}^{(l-1)} + \mathbf{b}_{cd}^{(l)}\right)$$

con la entrada inicial $\hat{\mathbf{h}}^{(0)} = \mathbf{y}$. Las dimensiones se expanden progresivamente: $2n \rightarrow 128 \rightarrow 256 \rightarrow k$, invirtiendo la compresión realizada por el encoder de canal.

En canales con desvanecimiento, cuando la información de estado del canal (CSI, *Channel State Information*) está disponible en el receptor, esta puede incorporarse como entrada adicional al decoder de canal:

$$\hat{\mathbf{h}} = g_{\theta_{cd}}(\mathbf{y}, \hat{\mathbf{h}}_{csi})$$

donde $\hat{\mathbf{h}}_{csi}$ representa la estimación de los coeficientes del canal. En la práctica, esto puede implementarse concatenando $\mathbf{y}$ y $\hat{\mathbf{h}}_{csi}$ como entrada a la primera capa densa, o utilizando capas de atención que ponderen la señal recibida en función de la calidad estimada del canal.

### 8.3.3 El decoder semántico

El **decoder semántico** toma la representación semántica recuperada $\hat{\mathbf{h}}$ y produce la reconstrucción final del dato original:

$$\hat{\mathbf{s}} = g_{\theta_{sd}}(\hat{\mathbf{h}})$$

donde $g_{\theta_{sd}}$ es la función de decodificación semántica con parámetros $\theta_{sd}$. La arquitectura de este componente depende críticamente de la modalidad de datos:

**Para texto:** El decoder semántico emplea un **Transformer decoder** con mecanismo de **atención cruzada** (*cross-attention*) que atiende a la representación semántica recuperada $\hat{\mathbf{h}}$. La generación de texto es **autoregresiva**: los tokens de salida se generan uno a uno, donde la predicción de cada token $\hat{s}_t$ depende de la representación semántica y de todos los tokens previamente generados:

$$p(\hat{s}_t | \hat{s}_{<t}, \hat{\mathbf{h}}) = \text{softmax}\left(\mathbf{W}_o \cdot \text{TransformerDecoder}(\hat{s}_{<t}, \hat{\mathbf{h}})\right)$$

donde $\hat{s}_{<t} = (\hat{s}_1, \hat{s}_2, \ldots, \hat{s}_{t-1})$ denota la secuencia de tokens generados hasta el paso $t-1$, y $\mathbf{W}_o \in \mathbb{R}^{|V| \times d_{model}}$ es la matriz de proyección de salida que mapea al espacio del vocabulario. El mecanismo de atención cruzada permite que el decoder semántico "consulte" selectivamente diferentes partes de la representación semántica al generar cada token, de manera análoga a como un traductor humano consulta repetidamente el texto fuente al redactar la traducción.

**Para imágenes:** El decoder semántico emplea una arquitectura de **red convolucional transpuesta** (también llamada deconvolucional) que progresivamente incrementa la resolución espacial y reduce la profundidad de canales. Si la representación semántica $\hat{\mathbf{h}} \in \mathbb{R}^{H' \times W' \times C'}$, el decoder aplica una secuencia de capas de sobremuestreo (*upsampling*):

$$\hat{\mathbf{s}}^{(l)} = \sigma\left(\text{ConvTranspose2d}\left(\hat{\mathbf{s}}^{(l-1)}\right)\right)$$

donde cada capa de convolución transpuesta duplica las dimensiones espaciales y reduce los canales: $H' \times W' \times C' \rightarrow 2H' \times 2W' \times C'/2 \rightarrow \cdots \rightarrow H \times W \times C$. La última capa utiliza una activación sigmoide o tangente hiperbólica para producir valores de píxeles en el rango apropiado ($[0,1]$ o $[-1,1]$).

### 8.3.4 Formulación completa del receptor

La operación completa del receptor se expresa como la composición de ambos decoders:

$$\hat{\mathbf{s}} = g_{\theta_{sd}}\left(g_{\theta_{cd}}(\mathbf{y})\right)$$

y el receptor completo está parametrizado por $\theta_{rx} = \{\theta_{cd}, \theta_{sd}\}$. Combinando con la expresión del transmisor, el sistema E2E completo se describe como:

$$\hat{\mathbf{s}} = g_{\theta_{sd}}\left(g_{\theta_{cd}}\left(\text{Canal}\left(f_{\theta_{ce}}\left(f_{\theta_{se}}(\mathbf{s})\right)\right)\right)\right)$$

Esta cadena de funciones compuestas constituye el grafo computacional completo del sistema, a través del cual fluyen los gradientes durante el entrenamiento. La simetría entre transmisor y receptor (encoder/decoder) no es accidental: el sistema E2E es esencialmente un **autoencoder** cuyo cuello de botella no es una capa de dimensión reducida, sino el canal de comunicación físico.

---

## 8.4 Funciones de Pérdida para Comunicaciones Semánticas

### 8.4.1 El papel central de la función de pérdida

La función de pérdida es, junto con la arquitectura de la red, el componente más crítico del diseño de un sistema de comunicación semántica E2E. Mientras que en los sistemas de comunicación convencionales la métrica de rendimiento es la tasa de error de bit (BER) o la tasa de error de bloque (BLER) —métricas puramente sintácticas que tratan todos los bits como igualmente importantes—, los sistemas semánticos requieren funciones de pérdida que capturen la **fidelidad del significado** transmitido. La elección de la función de pérdida determina qué aspectos del mensaje el sistema priorizará preservar.

### 8.4.2 Funciones de pérdida para transmisión de texto

La transmisión de texto presenta desafíos particulares porque el lenguaje natural es discreto (secuencias de tokens de un vocabulario finito), altamente estructurado (con sintaxis, semántica y pragmática) y ambiguo (diferentes secuencias de palabras pueden expresar el mismo significado).

**Pérdida de entropía cruzada (*Cross-Entropy Loss*):** La función de pérdida estándar para modelos generativos de texto es la entropía cruzada entre la distribución de probabilidad predicha y el token verdadero, sumada sobre todas las posiciones de la secuencia:

$$L_{CE} = -\sum_{t=1}^{T} \log p_{\theta}(\hat{s}_t = s_t \mid \hat{s}_{<t}, \mathbf{y})$$

donde $T$ es la longitud de la secuencia objetivo, $s_t$ es el token verdadero en la posición $t$, $\hat{s}_{<t}$ son los tokens generados en las posiciones anteriores (durante el entrenamiento, se usa *teacher forcing* con los tokens verdaderos), y $p_{\theta}(\cdot)$ es la distribución de probabilidad sobre el vocabulario predicha por el modelo.

La entropía cruzada tiene una interpretación profunda en teoría de la información: es equivalente a la log-verosimilitud negativa (*negative log-likelihood*) de la secuencia objetivo bajo el modelo, y su minimización es equivalente a minimizar la divergencia KL entre la distribución verdadera de los datos y la distribución del modelo:

$$L_{CE} = -\log p_{\theta}(s_1, s_2, \ldots, s_T \mid \mathbf{y}) = \text{KL}(p_{data} || p_{\theta}) + H(p_{data})$$

donde $H(p_{data})$ es la entropía de la distribución verdadera (una constante con respecto a $\theta$). Por tanto, minimizar $L_{CE}$ es equivalente a minimizar la divergencia KL.

Sin embargo, la entropía cruzada opera a nivel de **token individual** y no captura directamente la similitud semántica a nivel de oración. Dos oraciones pueden tener la misma semántica pero diferir significativamente token a token (por ejemplo, "El gato está sobre la alfombra" vs. "Encima del tapete se encuentra el felino"), lo que resultaría en una pérdida de entropía cruzada alta a pesar de la equivalencia semántica.

**Pérdida de similitud semántica basada en embeddings:** Para capturar la fidelidad semántica a nivel de oración, se puede emplear una pérdida basada en la similitud entre las representaciones vectoriales (*embeddings*) de las oraciones original y reconstruida. Utilizando un modelo de *embeddings* de oraciones pre-entrenado $\phi(\cdot)$ (como BERT o Sentence-BERT):

$$L_{sem} = 1 - \frac{\phi(\mathbf{s})^{\top} \phi(\hat{\mathbf{s}})}{||\phi(\mathbf{s})|| \cdot ||\phi(\hat{\mathbf{s}})||}$$

donde el cociente es la **similitud coseno** entre los embeddings de la oración original y la reconstruida. Esta pérdida vale 0 cuando las oraciones son semánticamente idénticas (embeddings paralelos) y 1 cuando son completamente disímiles (embeddings ortogonales). Un valor de 2 correspondería a significados opuestos (embeddings antiparalelos), aunque esto raramente ocurre en la práctica.

La ventaja de esta pérdida es que permite paráfrasis: el sistema puede reconstruir el significado del mensaje usando palabras diferentes sin ser penalizado, lo cual es deseable desde el punto de vista de la comunicación semántica. Su desventaja es que depende de la calidad del modelo de embeddings pre-entrenado y añade un costo computacional no despreciable al calcular los embeddings en cada paso de entrenamiento.

### 8.4.3 Funciones de pérdida para transmisión de imágenes

La transmisión de imágenes permite utilizar funciones de pérdida que operan en el dominio continuo de los valores de píxeles, pero la elección de la función tiene un impacto significativo en la calidad perceptual de las imágenes reconstruidas.

**Error cuadrático medio (*Mean Squared Error*, MSE):** La función de pérdida más fundamental para imágenes es el MSE, que mide la diferencia promedio al cuadrado entre cada píxel de la imagen original y la reconstruida:

$$L_{MSE} = \frac{1}{N}\sum_{i=1}^{N}(s_i - \hat{s}_i)^2 = \frac{1}{N}||\mathbf{s} - \hat{\mathbf{s}}||^2$$

donde $N = H \times W \times C$ es el número total de píxeles (alto × ancho × canales de color). El MSE es equivalente al PSNR (*Peak Signal-to-Noise Ratio*) a través de la relación:

$$\text{PSNR} = 10\log_{10}\left(\frac{\text{MAX}^2}{L_{MSE}}\right)$$

donde $\text{MAX}$ es el valor máximo del píxel (255 para imágenes de 8 bits o 1.0 para imágenes normalizadas).

El MSE es matemáticamente conveniente (es suave, convexo y fácil de optimizar), pero tiene una limitación fundamental: trata todos los errores de píxel como igualmente importantes, independientemente de su relevancia perceptual. Esto produce imágenes que, aunque tienen PSNR alto, pueden parecer borrosas porque el MSE favorece la predicción del promedio de posibles reconstrucciones en regiones de alta incertidumbre.

**Pérdida perceptual (*Perceptual Loss*):** Para superar las limitaciones del MSE, se emplea la pérdida perceptual, que compara las imágenes en el espacio de características de una red de clasificación pre-entrenada (típicamente VGG-16 o VGG-19 entrenada en ImageNet):

$$L_{perceptual} = \sum_{l \in \mathcal{L}} \frac{1}{N_l}||\Phi_l(\mathbf{s}) - \Phi_l(\hat{\mathbf{s}})||^2$$

donde $\Phi_l(\cdot)$ denota el mapa de activaciones de la capa $l$ de la red VGG, $N_l$ es el número de elementos en el mapa de activaciones de la capa $l$, y $\mathcal{L}$ es el conjunto de capas seleccionadas (típicamente capas de las primeras etapas del bloque convolucional).

La intuición detrás de la pérdida perceptual es que las capas internas de una red de clasificación de imágenes pre-entrenada han aprendido a extraer características perceptualmente relevantes: bordes, texturas, formas y estructuras. Comparar imágenes en este espacio de características, en lugar del espacio de píxeles, resulta en reconstrucciones que se parecen más a la imagen original desde el punto de vista humano, aunque puedan diferir en detalles de píxel.

**Pérdida basada en SSIM (*Structural Similarity Index Measure*):** El índice de similitud estructural SSIM compara las imágenes en términos de luminancia, contraste y estructura:

$$\text{SSIM}(\mathbf{s}, \hat{\mathbf{s}}) = \frac{(2\mu_s\mu_{\hat{s}} + c_1)(2\sigma_{s\hat{s}} + c_2)}{(\mu_s^2 + \mu_{\hat{s}}^2 + c_1)(\sigma_s^2 + \sigma_{\hat{s}}^2 + c_2)}$$

donde $\mu_s$, $\mu_{\hat{s}}$ son las medias locales, $\sigma_s^2$, $\sigma_{\hat{s}}^2$ son las varianzas locales, $\sigma_{s\hat{s}}$ es la covarianza local, y $c_1$, $c_2$ son constantes de estabilización. El SSIM se calcula localmente en ventanas deslizantes y se promedia sobre toda la imagen. La pérdida basada en SSIM se define como:

$$L_{SSIM} = 1 - \text{SSIM}(\mathbf{s}, \hat{\mathbf{s}})$$

El SSIM captura mejor la percepción humana de calidad que el MSE porque se basa en la comparación de estadísticas locales de luminancia, contraste y estructura, que son los elementos que el sistema visual humano utiliza para evaluar la calidad de las imágenes.

### 8.4.4 Función de pérdida combinada

En la práctica, los sistemas de comunicación semántica E2E suelen emplear una **función de pérdida combinada** que integra múltiples objetivos:

$$L = \alpha L_{task} + \beta L_{semantic} + \gamma L_{channel}$$

donde:
- $L_{task}$ es la pérdida específica de la tarea (por ejemplo, entropía cruzada para texto, MSE para imágenes).
- $L_{semantic}$ es una pérdida que mide la fidelidad semántica (por ejemplo, similitud coseno de embeddings, pérdida perceptual).
- $L_{channel}$ es un término de regularización que puede incluir restricciones sobre la distribución de los símbolos transmitidos (por ejemplo, penalización de potencia, suavidad de la constelación, o restricciones de forma de espectro).
- $\alpha, \beta, \gamma \geq 0$ son hiperparámetros que ponderan la contribución relativa de cada componente.

El diseño de estos pesos implica compromisos fundamentales. Un valor alto de $\alpha$ con $\beta \approx 0$ produce un sistema que replica fielmente la secuencia de símbolos originales pero puede no capturar la semántica subyacente. Un valor alto de $\beta$ con $\alpha \approx 0$ produce un sistema que preserva el significado global pero puede alterar los detalles superficiales del mensaje. El término $\gamma$ controla la regularización del espacio de señales de canal y puede mejorar la robustez del sistema frente a condiciones de canal no vistas durante el entrenamiento.

En la práctica, estos hiperparámetros se seleccionan mediante validación cruzada o búsqueda de hiperparámetros, y sus valores óptimos dependen de la modalidad de datos, la arquitectura del sistema, el rango de SNR operativo y los requisitos de la aplicación.

---

## 8.5 Proceso de Entrenamiento E2E Paso a Paso

### 8.5.1 Visión general del entrenamiento

El entrenamiento de un sistema de comunicación semántica E2E sigue el paradigma estándar de aprendizaje profundo —retropropagación con descenso de gradiente estocástico— pero con particularidades importantes derivadas de la presencia del canal estocástico en medio de la red. En esta subsección, desglosamos el proceso paso a paso con rigor matemático.

### 8.5.2 Paso 1: Propagación hacia adelante (*Forward Pass*)

Dado un mini-lote de $B$ muestras de entrenamiento $\{\mathbf{s}_1, \mathbf{s}_2, \ldots, \mathbf{s}_B\}$ extraídas del conjunto de datos de entrenamiento, la propagación hacia adelante recorre secuencialmente todos los componentes del sistema:

**Etapa 1 — Encoder semántico:** Para cada muestra $b$:
$$\mathbf{h}_b = f_{\theta_{se}}(\mathbf{s}_b), \quad b = 1, 2, \ldots, B$$

**Etapa 2 — Encoder de canal:**
$$\mathbf{z}_b = f_{\theta_{ce}}(\mathbf{h}_b)$$

**Etapa 3 — Normalización de potencia:**
$$\mathbf{z}_b^{norm} = \text{PowerNorm}(\mathbf{z}_b)$$

**Etapa 4 — Canal (con reparametrización):**
Se muestrea ruido $\boldsymbol{\epsilon}_b \sim \mathcal{N}(\mathbf{0}, \mathbf{I})$ y, opcionalmente, coeficientes de desvanecimiento $\boldsymbol{\epsilon}_{h,b} \sim \mathcal{CN}(\mathbf{0}, \mathbf{I})$. La señal recibida se calcula como:
$$\mathbf{y}_b = \mathbf{z}_b^{norm} + \sigma\boldsymbol{\epsilon}_b \quad \text{(AWGN)}$$
$$\mathbf{y}_b = \boldsymbol{\epsilon}_{h,b} \odot \mathbf{z}_b^{norm} + \sigma\boldsymbol{\epsilon}_b \quad \text{(Rayleigh)}$$

**Etapa 5 — Decoder de canal:**
$$\hat{\mathbf{h}}_b = g_{\theta_{cd}}(\mathbf{y}_b)$$

**Etapa 6 — Decoder semántico:**
$$\hat{\mathbf{s}}_b = g_{\theta_{sd}}(\hat{\mathbf{h}}_b)$$

Es fundamental observar que cada etapa mantiene el grafo computacional necesario para la retropropagación. Las variables aleatorias $\boldsymbol{\epsilon}_b$ y $\boldsymbol{\epsilon}_{h,b}$ se tratan como constantes durante la retropropagación (no tienen gradientes), pero la reparametrización asegura que $\mathbf{y}_b$ permanece diferenciable con respecto a $\mathbf{z}_b^{norm}$ y, por tanto, con respecto a todos los parámetros del transmisor.

### 8.5.3 Paso 2: Cálculo de la pérdida

Se computa la función de pérdida promediada sobre el mini-lote:

$$L = \frac{1}{B}\sum_{b=1}^{B} \ell(\mathbf{s}_b, \hat{\mathbf{s}}_b)$$

donde $\ell(\cdot, \cdot)$ es la función de pérdida por muestra (por ejemplo, entropía cruzada, MSE o una combinación ponderada). El valor escalar $L$ cuantifica qué tan bien el sistema completo —desde la entrada del transmisor hasta la salida del receptor, pasando por el canal ruidoso— preserva el contenido del mensaje.

### 8.5.4 Paso 3: Retropropagación (*Backpropagation*)

El cálculo de gradientes se realiza mediante la aplicación recursiva de la regla de la cadena, fluyendo desde la pérdida hacia atrás a través de todos los componentes del sistema:

**Gradientes del decoder semántico:**
$$\frac{\partial L}{\partial \theta_{sd}} = \frac{1}{B}\sum_{b=1}^{B} \frac{\partial \ell}{\partial \hat{\mathbf{s}}_b} \cdot \frac{\partial \hat{\mathbf{s}}_b}{\partial \theta_{sd}}$$

**Gradientes del decoder de canal:**
$$\frac{\partial L}{\partial \theta_{cd}} = \frac{1}{B}\sum_{b=1}^{B} \frac{\partial \ell}{\partial \hat{\mathbf{s}}_b} \cdot \frac{\partial \hat{\mathbf{s}}_b}{\partial \hat{\mathbf{h}}_b} \cdot \frac{\partial \hat{\mathbf{h}}_b}{\partial \theta_{cd}}$$

**Gradientes a través del canal:** Aquí es donde la reparametrización juega su papel crucial. Para AWGN:
$$\frac{\partial \mathbf{y}_b}{\partial \mathbf{z}_b^{norm}} = \mathbf{I}$$

Para Rayleigh:
$$\frac{\partial \mathbf{y}_b}{\partial \mathbf{z}_b^{norm}} = \text{diag}(\boldsymbol{\epsilon}_{h,b})$$

**Gradientes del encoder de canal:**
$$\frac{\partial L}{\partial \theta_{ce}} = \frac{1}{B}\sum_{b=1}^{B} \frac{\partial \ell}{\partial \hat{\mathbf{s}}_b} \cdot \frac{\partial \hat{\mathbf{s}}_b}{\partial \hat{\mathbf{h}}_b} \cdot \frac{\partial \hat{\mathbf{h}}_b}{\partial \mathbf{y}_b} \cdot \frac{\partial \mathbf{y}_b}{\partial \mathbf{z}_b^{norm}} \cdot \frac{\partial \mathbf{z}_b^{norm}}{\partial \theta_{ce}}$$

**Gradientes del encoder semántico:**
$$\frac{\partial L}{\partial \theta_{se}} = \frac{1}{B}\sum_{b=1}^{B} \frac{\partial \ell}{\partial \hat{\mathbf{s}}_b} \cdot \frac{\partial \hat{\mathbf{s}}_b}{\partial \hat{\mathbf{h}}_b} \cdot \frac{\partial \hat{\mathbf{h}}_b}{\partial \mathbf{y}_b} \cdot \frac{\partial \mathbf{y}_b}{\partial \mathbf{z}_b^{norm}} \cdot \frac{\partial \mathbf{z}_b^{norm}}{\partial \mathbf{h}_b} \cdot \frac{\partial \mathbf{h}_b}{\partial \theta_{se}}$$

Observe cómo los gradientes fluyen a través de toda la cadena, incluyendo el canal. La estocasticidad del canal introduce variabilidad en los gradientes (ya que $\boldsymbol{\epsilon}_{h,b}$ y $\boldsymbol{\epsilon}_b$ son diferentes para cada muestra y cada época), lo cual actúa como una forma adicional de regularización que mejora la generalización del modelo.

### 8.5.5 Paso 4: Actualización de parámetros

Todos los parámetros del sistema se actualizan **conjuntamente** utilizando un optimizador de descenso de gradiente. Con el optimizador Adam:

$$\theta \leftarrow \theta - \eta \cdot \text{Adam}(\nabla_\theta L)$$

donde $\theta = \{\theta_{se}, \theta_{ce}, \theta_{cd}, \theta_{sd}\}$ es el conjunto completo de parámetros y $\eta$ es la tasa de aprendizaje. El optimizador Adam adapta la tasa de aprendizaje para cada parámetro individualmente utilizando estimaciones de los momentos de primer y segundo orden de los gradientes:

$$m_t = \beta_1 m_{t-1} + (1-\beta_1)\nabla_\theta L$$
$$v_t = \beta_2 v_{t-1} + (1-\beta_2)(\nabla_\theta L)^2$$
$$\hat{m}_t = \frac{m_t}{1-\beta_1^t}, \quad \hat{v}_t = \frac{v_t}{1-\beta_2^t}$$
$$\theta_{t+1} = \theta_t - \eta \frac{\hat{m}_t}{\sqrt{\hat{v}_t} + \epsilon}$$

donde $\beta_1 = 0.9$ y $\beta_2 = 0.999$ son valores típicos de los hiperparámetros de Adam, y $\epsilon = 10^{-8}$ es un factor de estabilización numérica.

La actualización conjunta es esencial: permite que el transmisor y el receptor co-adapten sus estrategias. El transmisor aprende a codificar la información de una manera que el receptor pueda decodificar eficientemente dado el ruido del canal, y el receptor aprende a decodificar de una manera que explota las regularidades de la codificación del transmisor.

### 8.5.6 Entrenamiento con currículo de SNR

Una técnica crucial para el entrenamiento exitoso de sistemas E2E es el **entrenamiento con currículo de SNR** (*SNR curriculum training*). La idea es comenzar el entrenamiento con valores altos de SNR (canal menos ruidoso) y gradualmente reducir la SNR a lo largo del entrenamiento (incrementando el nivel de ruido).

La justificación pedagógica es análoga a la enseñanza humana: primero se aprenden los conceptos básicos en un entorno "fácil" (alto SNR, poco ruido) y después se desarrolla robustez frente a condiciones adversas (bajo SNR, mucho ruido). Formalmente, la varianza del ruido sigue un programa:

$$\sigma^2(e) = \frac{P}{10^{\text{SNR}(e)/10}}$$

donde $\text{SNR}(e)$ es la SNR programada para la época $e$. Un programa típico podría ser:

$$\text{SNR}(e) = \text{SNR}_{max} - \frac{e}{E}(\text{SNR}_{max} - \text{SNR}_{min})$$

donde $E$ es el número total de épocas, $\text{SNR}_{max}$ (por ejemplo, 20 dB) es la SNR inicial y $\text{SNR}_{min}$ (por ejemplo, 0 dB) es la SNR final.

**Entrenamiento con SNR mixto por lote:** Una alternativa al currículo temporal es entrenar cada mini-lote con **valores de SNR variados**. Para cada muestra $b$ del lote, se selecciona una SNR diferente $\text{SNR}_b \sim \mathcal{U}[\text{SNR}_{min}, \text{SNR}_{max}]$ muestreada uniformemente del rango operativo deseado:

$$\sigma_b^2 = 10^{-\text{SNR}_b/10}$$

Esta estrategia produce un modelo que funciona razonablemente bien en todo el rango de SNR, en lugar de estar optimizado para un único valor. El costo es que el rendimiento en cualquier SNR específica puede ser ligeramente inferior al de un modelo entrenado exclusivamente para esa SNR.

### 8.5.7 Diagrama del proceso de entrenamiento

> **Figura 8.3:** Diagrama completo del bucle de entrenamiento E2E. El flujo de datos comienza con un mini-lote de muestras $\{\mathbf{s}_b\}_{b=1}^B$ (izquierda). **Propagación hacia adelante** (flechas azules, de izquierda a derecha): los datos pasan secuencialmente por el Encoder Semántico ($f_{\theta_{se}}$), el Encoder de Canal ($f_{\theta_{ce}}$), la Normalización de Potencia, el Canal Estocástico (representado como una nube con ruido $\mathbf{n}$ y, opcionalmente, desvanecimiento $\mathbf{h}$), el Decoder de Canal ($g_{\theta_{cd}}$) y el Decoder Semántico ($g_{\theta_{sd}}$), produciendo las reconstrucciones $\{\hat{\mathbf{s}}_b\}$. El módulo de **Cálculo de Pérdida** (derecha) compara $\mathbf{s}_b$ con $\hat{\mathbf{s}}_b$ y produce el escalar $L$. **Retropropagación** (flechas rojas punteadas, de derecha a izquierda): los gradientes $\nabla L$ fluyen en dirección opuesta a través de todos los componentes, incluyendo a través del canal (gracias a la reparametrización). El **Optimizador Adam** (parte inferior) recibe todos los gradientes y actualiza conjuntamente los parámetros $\theta = \{\theta_{se}, \theta_{ce}, \theta_{cd}, \theta_{sd}\}$. Un módulo de **Programación de SNR** (esquina superior derecha) controla la varianza del ruido $\sigma^2$ que se inyecta en el canal, permitiendo el entrenamiento con currículo.

---

## 8.6 Conversión de Señales Multimedia a Representación Semántica

### 8.6.1 El desafío de la representación universal

Uno de los aspectos más fascinantes y técnicamente desafiantes de la comunicación semántica es la transformación de señales multimedia en su forma nativa —ondas sonoras, secuencias de fotogramas de video, secuencias de caracteres— en representaciones semánticas compactas que capturan el significado esencial. Esta transformación debe ser simultáneamente eficiente (comprimir la información drásticamente), informativa (preservar el contenido semántico) y robusta (las representaciones deben ser adecuadas para su transmisión por canales ruidosos). En esta subsección, examinamos en detalle cómo se realiza esta conversión para las principales modalidades multimedia.

### 8.6.2 Audio y voz: de la onda acústica a tokens semánticos

El procesamiento de señales de audio y voz para comunicación semántica sigue una cadena de transformaciones progresivas:

**Paso 1 — De la forma de onda al espectrograma:** La señal de audio cruda es una forma de onda unidimensional $x(t)$ muestreada típicamente a 16 kHz o 44.1 kHz. El primer paso es convertirla en una representación tiempo-frecuencia bidimensional mediante la **Transformada de Fourier de Tiempo Corto** (STFT):

$$X(t, f) = \sum_{\tau} x(\tau) w(\tau - t) e^{-j2\pi f \tau}$$

donde $w(\tau)$ es una función ventana (típicamente Hann o Hamming) de longitud 25 ms con desplazamiento de 10 ms. El resultado $|X(t, f)|^2$ es el espectrograma de potencia: una imagen 2D donde el eje horizontal representa el tiempo, el eje vertical representa la frecuencia, y la intensidad representa la potencia.

**Paso 2 — Del espectrograma al mel-espectrograma:** Para capturar la percepción auditiva humana (que es logarítmica en frecuencia), se aplica un banco de filtros mel al espectrograma:

$$M(t, m) = \sum_{f} |X(t, f)|^2 \cdot \Phi_m(f)$$

donde $\Phi_m(f)$ es el $m$-ésimo filtro triangular en la escala mel. Típicamente se utilizan 80 filtros mel, produciendo un mel-espectrograma $\mathbf{M} \in \mathbb{R}^{T' \times 80}$ donde $T'$ es el número de tramas temporales.

**Paso 3 — Del mel-espectrograma a tokens semánticos:** El mel-espectrograma se procesa mediante un encoder (CNN o Transformer) que extrae una secuencia de vectores semánticos. Modelos como wav2vec 2.0 o HuBERT aprenden representaciones semánticas del habla directamente de la forma de onda, capturando el contenido lingüístico (fonemas, palabras, significado) mientras descartan variaciones acústicas irrelevantes (ruido ambiental, reverberación). Alternativamente, se puede aplicar cuantización vectorial para obtener tokens discretos semánticos, lo que facilita la integración con modelos de lenguaje.

### 8.6.3 Video: de fotogramas a representación espacio-temporal

El video presenta un desafío adicional respecto a las imágenes estáticas: la dimensión temporal. Un video consiste en una secuencia de fotogramas $\mathbf{V} = (\mathbf{I}_1, \mathbf{I}_2, \ldots, \mathbf{I}_F)$ donde cada fotograma $\mathbf{I}_f \in \mathbb{R}^{H \times W \times 3}$ es una imagen en color. La cadena de conversión semántica para video procede en dos etapas:

**Etapa espacial — Extracción de características por fotograma:** Cada fotograma se procesa individualmente mediante una red convolucional (CNN) pre-entrenada (por ejemplo, ResNet-50 o EfficientNet):

$$\mathbf{f}_f = \text{CNN}(\mathbf{I}_f) \in \mathbb{R}^{d_{spatial}}$$

produciendo un vector de características espaciales $\mathbf{f}_f$ que describe el contenido visual de cada fotograma. Alternativamente, redes convolucionales 3D como C3D o SlowFast procesan conjuntamente bloques de fotogramas consecutivos para capturar el movimiento de manera implícita.

**Etapa temporal — Modelado de dependencias entre fotogramas:** La secuencia de características espaciales $(\mathbf{f}_1, \mathbf{f}_2, \ldots, \mathbf{f}_F)$ se procesa mediante un modelo de secuencia —un Transformer temporal o una red LSTM— que captura las dependencias temporales (movimiento de objetos, evolución de escenas, dinámica de acciones):

$$\mathbf{h}_{video} = \text{Transformer}(\mathbf{f}_1, \mathbf{f}_2, \ldots, \mathbf{f}_F) \in \mathbb{R}^{d_{semantic}}$$

El resultado es una representación semántica del video que captura tanto el contenido visual de cada fotograma como la estructura temporal de la secuencia. La redundancia temporal del video (fotogramas consecutivos son muy similares) se elimina automáticamente por el mecanismo de atención del Transformer, que aprende a focalizar la atención en los cambios significativos entre fotogramas.

### 8.6.4 Texto: tokenización y embeddings

Para el texto, la conversión a representación semántica sigue un proceso bien establecido en el procesamiento de lenguaje natural:

**Tokenización:** El texto crudo se segmenta en **tokens** (subpalabras) mediante algoritmos como:

- **BPE (*Byte Pair Encoding*):** Construye iterativamente un vocabulario fusionando los pares de caracteres más frecuentes. Produce un vocabulario de tamaño fijo (típicamente 30,000–50,000 tokens) que puede representar cualquier texto, incluyendo palabras fuera de vocabulario, mediante secuencias de subtokens.

- **WordPiece:** Similar a BPE pero utiliza un criterio de máxima verosimilitud para seleccionar las fusiones, optimizando la probabilidad del corpus de entrenamiento bajo un modelo unigram.

- **SentencePiece:** Una implementación que no asume pre-tokenización por espacios, permitiendo aplicar BPE o unigram directamente sobre texto crudo, lo que es esencial para idiomas sin separadores de palabras (como chino o japonés).

**Embedding:** Cada token $s_i$ del vocabulario se mapea a un vector denso de dimensión $d_{model}$ mediante una tabla de búsqueda (*lookup table*):

$$\mathbf{e}_i = \mathbf{E}[s_i] \in \mathbb{R}^{d_{model}}$$

donde $\mathbf{E} \in \mathbb{R}^{|V| \times d_{model}}$ es la matriz de embeddings, con $|V|$ el tamaño del vocabulario. Los embeddings se inicializan aleatoriamente y se ajustan durante el entrenamiento del sistema E2E.

**Codificación Transformer:** La secuencia de embeddings (con codificación posicional añadida) se procesa a través de las capas del Transformer para producir la representación semántica contextualizada:

$$\mathbf{h}_{text} = \text{TransformerEncoder}(\mathbf{e}_1 + \mathbf{PE}_1, \ldots, \mathbf{e}_L + \mathbf{PE}_L)$$

### 8.6.5 El puente de la tokenización: de señales continuas a unidades semánticas discretas

Un concepto unificador en todas las modalidades es el **puente de tokenización**: la conversión de señales continuas del mundo físico en unidades semánticas discretas o cuasi-discretas que pueden procesarse eficientemente por modelos neuronales. Este puente es un punto de diseño crítico que determina:

- **La granularidad de la representación:** Tokens más finos capturan más detalle pero requieren secuencias más largas; tokens más gruesos son más compactos pero pierden matices.
- **El balance entre compresión y fidelidad:** La cuantización inherente a la tokenización introduce una pérdida de información que debe balancearse con la eficiencia de la transmisión.
- **La adaptabilidad al contenido:** Los mejores sistemas aprenden tokenizaciones adaptativas que asignan más tokens a las partes informativas del contenido y menos a las partes redundantes o predecibles.

### 8.6.6 Superioridad sobre la codificación de fuente tradicional

Los métodos tradicionales de codificación de fuente —JPEG para imágenes, MP3/AAC para audio, H.264/H.265 para video— fueron diseñados con un objetivo fundamentalmente diferente al de la comunicación semántica. Estos códecs se optimizan para **minimizar la tasa de bits** sujeta a una **restricción de distorsión** (típicamente MSE o alguna métrica perceptual simple), operando bajo el paradigma de la teoría de tasa-distorsión de Shannon.

La comunicación semántica E2E supera este paradigma en varios aspectos fundamentales:

1. **Optimización conjunta fuente-canal:** Los códecs tradicionales producen un flujo de bits que luego debe protegerse con codificación de canal. Esta separación es subóptima para longitudes de bloque finitas. El sistema E2E elimina esta separación, optimizando directamente la calidad de la reconstrucción bajo las condiciones reales del canal.

2. **Adaptación al contenido semántico:** JPEG comprime todos los bloques de 8×8 de una imagen de la misma manera, independientemente de su importancia semántica. Un sistema semántico puede asignar más recursos de canal a las regiones semánticamente relevantes (por ejemplo, la cara de una persona en una videollamada) y menos a las regiones de fondo.

3. **Robustez frente a errores de canal:** Cuando un bit protegido por codificación de canal se decodifica erróneamente, el efecto puede ser catastrófico (pérdida de paquetes completos, artefactos de bloque). En un sistema semántico, los errores del canal se manifiestan como degradaciones suaves y distribuidas que preservan la interpretabilidad del contenido.

4. **Eliminación de la interfaz binaria:** Al no requerir la conversión de la representación intermedia a bits, el sistema E2E evita la pérdida de cuantización y puede explotar la naturaleza continua de las señales analógicas de manera más eficiente.

---

## 8.7 Degradación Suave vs. Efecto Acantilado

### 8.7.1 El efecto acantilado en los sistemas clásicos

Los sistemas de comunicación digital convencionales exhiben un comportamiento característico conocido como **efecto acantilado** (*cliff effect* o *threshold effect*). Este fenómeno se manifiesta de la siguiente manera: cuando la SNR del canal está por encima de un cierto umbral (determinado por la tasa de codificación del canal y el esquema de modulación seleccionados), el sistema funciona prácticamente sin errores, con una calidad de recepción excelente. Pero cuando la SNR cae por debajo de ese umbral, la calidad se degrada de manera **abrupta y catastrófica**, pasando de una operación casi perfecta a una falla total en un rango muy estrecho de SNR.

Matemáticamente, este comportamiento se puede entender analizando la probabilidad de error de bit (BER) de un sistema con modulación $M$-QAM y codificación de canal con tasa $R_c$:

$$\text{BER}(\text{SNR}) \approx \frac{4}{\log_2 M}\left(1 - \frac{1}{\sqrt{M}}\right) Q\left(\sqrt{\frac{3 R_c \cdot \text{SNR}}{M-1}}\right)$$

donde $Q(x) = \frac{1}{\sqrt{2\pi}}\int_x^{\infty}e^{-t^2/2}dt$ es la función Q gaussiana, que decae exponencialmente. La transición de BER alta a BER baja ocurre en un rango de SNR de apenas 2–3 dB, creando el "acantilado" en la curva de rendimiento. Con codificación de canal moderna (Turbo, LDPC, Polar) con longitudes de bloque largas, la caída es aún más pronunciada —de $10^{-1}$ a $10^{-6}$ en menos de 1 dB—, lo cual es deseable operativamente pero exacerba el efecto acantilado.

El problema se agrava cuando consideramos la capa de aplicación. Un video codificado con H.264 y transmitido con 16-QAM y código LDPC de tasa 3/4 se verá perfecto si la SNR > 15 dB, pero será completamente ilegible si la SNR < 12 dB. No hay un término medio: el sistema no puede degradar gracefully la calidad del video para adaptarse a la SNR disponible (a menos que se implementen mecanismos de adaptación de enlace, que son complejos e introducen latencia).

### 8.7.2 Degradación suave en los sistemas semánticos

Los sistemas de comunicación semántica E2E exhiben un comportamiento radicalmente diferente: la **degradación suave** (*graceful degradation*). A medida que la SNR disminuye, la calidad de la reconstrucción se degrada de manera **continua y gradual**, sin transiciones abruptas. Incluso a SNR muy bajas, el sistema produce reconstrucciones que, aunque imperfectas, preservan el significado esencial del mensaje original.

Este comportamiento emerge naturalmente de la arquitectura E2E y se puede explicar intuitivamente. En un sistema semántico, la información no se codifica como bits individuales (donde un error en un solo bit puede corromper un símbolo completo), sino como **vectores continuos en un espacio latente**. Cuando el ruido del canal perturba estos vectores, la perturbación se distribuye de manera suave sobre todas las dimensiones de la representación. El decoder, entrenado para reconstruir el significado a partir de representaciones ruidosas, produce una reconstrucción que refleja la *distancia* en el espacio semántico a la representación original, no una reconstrucción perfecta o nula.

### 8.7.3 Análisis matemático comparativo

Para formalizar la comparación, definamos una métrica de calidad semántica $Q(\text{SNR})$ que varía entre 0 (calidad nula, significado completamente perdido) y 1 (calidad perfecta, significado completamente preservado). Para un sistema clásico, esta métrica tiene la forma aproximada de una función escalón:

$$Q_{clasico}(\text{SNR}) \approx \begin{cases} 1 - \epsilon & \text{si } \text{SNR} > \text{SNR}_{th} + \delta \\ \text{transición abrupta} & \text{si } |\text{SNR} - \text{SNR}_{th}| \leq \delta \\ \epsilon' & \text{si } \text{SNR} < \text{SNR}_{th} - \delta \end{cases}$$

donde $\text{SNR}_{th}$ es el umbral del sistema, $\delta \approx 1\text{–}2$ dB es el ancho de la transición (muy estrecho), $\epsilon$ es el error residual a alta SNR (muy pequeño) y $\epsilon'$ es la calidad a baja SNR (esencialmente cero para aplicaciones prácticas).

Para un sistema semántico E2E, la métrica de calidad tiene una forma sigmoidal suave:

$$Q_{semantico}(\text{SNR}) \approx 1 - \frac{C_1}{1 + C_2 \cdot \text{SNR}^{\alpha}}$$

donde $C_1$, $C_2$ y $\alpha$ son constantes que dependen de la arquitectura, la razón de codificación y la distribución de los datos. Esta curva varía suavemente sobre todo el rango de SNR, sin discontinuidades.

Otra forma de analizar la comparación es mediante la **similitud semántica** (por ejemplo, la puntuación BLEU para texto o el SSIM para imágenes) como función de la SNR. Empíricamente, para el sistema DeepSC (Xie et al., 2021, DOI: 10.1109/TSP.2021.3071082), la similitud semántica del texto varía aproximadamente como:

$$\text{SemSim}(\text{SNR}) \approx \text{SemSim}_{max} \left(1 - e^{-\lambda(\text{SNR} - \text{SNR}_0)}\right)$$

para $\text{SNR} > \text{SNR}_0$, donde $\lambda$ controla la tasa de convergencia y $\text{SNR}_0$ es el punto de inflexión. Esta curva exponencial saturante produce una degradación suave.

### 8.7.4 Implicaciones prácticas

La degradación suave tiene implicaciones prácticas profundas:

1. **Robustez ante variaciones del canal:** En entornos inalámbricos donde la SNR fluctúa rápidamente (por ejemplo, comunicaciones vehiculares o IoT en entornos industriales), un sistema con degradación suave mantiene una calidad aceptable incluso durante caídas momentáneas de la SNR, mientras que un sistema clásico experimentaría interrupciones frecuentes.

2. **Simplificación del diseño del sistema:** Los sistemas clásicos requieren mecanismos complejos de **adaptación de enlace** (*link adaptation*) que seleccionan dinámicamente el esquema de modulación y codificación (MCS) óptimo para la SNR actual. Los sistemas semánticos eliminan esta necesidad, ya que un único modelo entrenado para un rango de SNR funciona adecuadamente en todo ese rango.

3. **Eficiencia en el uso del espectro:** Los sistemas clásicos deben diseñarse con márgenes de SNR conservadores para evitar el efecto acantilado, desperdiciando capacidad. Los sistemas semánticos pueden operar más cerca del límite de capacidad porque no hay un acantilado que evitar.

### 8.7.5 Diagrama comparativo

> **Figura 8.4:** Comparación del rendimiento de un sistema clásico y un sistema de comunicación semántica en función de la SNR. El eje horizontal representa la SNR en dB (de $-5$ a 25 dB) y el eje vertical representa la métrica de calidad normalizada $Q$ (de 0 a 1). **Curva azul (Sistema clásico):** muestra una transición abrupta tipo escalón alrededor de $\text{SNR}_{th} \approx 10$ dB. Por debajo de $\sim$8 dB, la calidad es prácticamente cero (efecto acantilado); por encima de $\sim$12 dB, la calidad es casi perfecta. La zona sombreada roja marca la región de falla catastrófica. **Curva roja (Sistema semántico E2E):** muestra una curva sigmoidal suave que mejora gradualmente con la SNR. A 0 dB, la calidad es aproximadamente 0.4 (parcialmente inteligible); a 10 dB, es aproximadamente 0.85; y satura cerca de 0.95 a SNR altas. No hay transición abrupta. La zona sombreada verde marca la región donde el sistema semántico supera al clásico (SNR baja). La zona sombreada azul marca la región donde el sistema clásico es ligeramente superior (SNR alta). Una anotación señala el "crossover point" donde ambas curvas se cruzan (aproximadamente a 11 dB), y otra anotación explica "Degradación suave: calidad proporcional a SNR" para la curva semántica.

---

## 8.8 Implementación Completa en PyTorch

### 8.8.1 Descripción del sistema implementado

A continuación, presentamos una implementación completa y funcional de un sistema de comunicación semántica E2E en PyTorch. El sistema implementa la transmisión de texto a través de un canal AWGN, siguiendo la arquitectura inspirada en DeepSC (Xie et al., 2021, DOI: 10.1109/TSP.2021.3071082). El código incluye todos los componentes discutidos en esta sección: encoder semántico basado en Transformer, encoder de canal con capas densas y normalización de potencia, canal AWGN diferenciable, decoder de canal y decoder semántico autoregresivo.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
import math
import numpy as np

# ===========================================================
# SISTEMA DE COMUNICACIÓN SEMÁNTICA E2E EN PYTORCH
# Basado en la arquitectura DeepSC para transmisión de texto
# ===========================================================

class PositionalEncoding(nn.Module):
    """
    Codificación posicional sinusoidal para el Transformer.
    Añade información de posición a los embeddings de entrada,
    permitiendo que el modelo distinga entre tokens en diferentes
    posiciones de la secuencia.
    """
    def __init__(self, d_model, max_len=512, dropout=0.1):
        super().__init__()
        self.dropout = nn.Dropout(p=dropout)

        # Crear la matriz de codificación posicional [max_len, d_model]
        pe = torch.zeros(max_len, d_model)
        position = torch.arange(0, max_len, dtype=torch.float).unsqueeze(1)
        # Factor de escala exponencial para las frecuencias
        div_term = torch.exp(
            torch.arange(0, d_model, 2).float()
            * (-math.log(10000.0) / d_model)
        )
        # Componentes seno (dimensiones pares) y coseno (impares)
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)
        pe = pe.unsqueeze(0)  # [1, max_len, d_model]
        self.register_buffer('pe', pe)

    def forward(self, x):
        # x: [batch_size, seq_len, d_model]
        x = x + self.pe[:, :x.size(1), :]
        return self.dropout(x)


class SemanticEncoder(nn.Module):
    """
    Encoder Semántico basado en Transformer.
    Transforma la secuencia de tokens de entrada en una
    representación semántica densa que captura el significado
    del mensaje completo.
    """
    def __init__(self, vocab_size, d_model=128, nhead=8,
                 num_layers=3, dim_feedforward=512, dropout=0.1):
        super().__init__()
        self.d_model = d_model

        # Capa de embedding: mapea índices de tokens a vectores densos
        self.embedding = nn.Embedding(vocab_size, d_model)
        self.pos_encoder = PositionalEncoding(d_model, dropout=dropout)

        # Capas del Transformer Encoder
        encoder_layer = nn.TransformerEncoderLayer(
            d_model=d_model,
            nhead=nhead,
            dim_feedforward=dim_feedforward,
            dropout=dropout,
            batch_first=True
        )
        self.transformer_encoder = nn.TransformerEncoder(
            encoder_layer, num_layers=num_layers
        )

        # Capa de proyección: reduce la representación del Transformer
        # a un vector semántico de dimensión fija
        self.fc_semantic = nn.Linear(d_model, d_model)

    def forward(self, src, src_mask=None, src_key_padding_mask=None):
        """
        Args:
            src: Tensor de tokens [batch_size, seq_len]
            src_mask: Máscara de atención opcional
            src_key_padding_mask: Máscara de padding [batch_size, seq_len]
        Returns:
            h: Representación semántica [batch_size, seq_len, d_model]
        """
        # Embedding con escalado por sqrt(d_model) para estabilizar
        x = self.embedding(src) * math.sqrt(self.d_model)
        x = self.pos_encoder(x)

        # Procesamiento por las capas de Transformer
        h = self.transformer_encoder(
            x, mask=src_mask,
            src_key_padding_mask=src_key_padding_mask
        )

        # Proyección semántica
        h = self.fc_semantic(h)
        return h


class ChannelEncoder(nn.Module):
    """
    Encoder de Canal: transforma la representación semántica
    en símbolos de canal con normalización de potencia.
    Mapea del espacio semántico (d_model dimensiones) al
    espacio de canal (channel_dim dimensiones = 2n para n
    símbolos complejos).
    """
    def __init__(self, d_model=128, channel_dim=32):
        super().__init__()
        self.channel_dim = channel_dim

        # Red de capas densas para la codificación de canal
        self.encoder = nn.Sequential(
            nn.Linear(d_model, 256),
            nn.ReLU(),
            nn.Linear(256, channel_dim)
        )

    def power_normalize(self, z):
        """
        Normalización de potencia: asegura E[||z||^2] = channel_dim.
        Cada vector de símbolos se normaliza para tener potencia
        unitaria por dimensión.
        """
        # Calcular la potencia promedio por muestra del lote
        batch_power = torch.mean(z ** 2, dim=-1, keepdim=True)
        # Normalizar para potencia unitaria por dimensión
        z_norm = z / torch.sqrt(batch_power + 1e-8)
        return z_norm

    def forward(self, h):
        """
        Args:
            h: Representación semántica [batch_size, seq_len, d_model]
        Returns:
            z: Símbolos de canal normalizados
               [batch_size, seq_len, channel_dim]
        """
        z = self.encoder(h)
        z = self.power_normalize(z)
        return z


class AWGNChannel(nn.Module):
    """
    Canal AWGN diferenciable.
    Implementa y = z + n, donde n ~ N(0, sigma^2 * I).
    Utiliza el truco de reparametrización: y = z + sigma * epsilon,
    con epsilon ~ N(0, I), para permitir la retropropagación
    de gradientes a través del canal.
    """
    def __init__(self):
        super().__init__()

    def forward(self, z, snr_db):
        """
        Args:
            z: Señal transmitida [batch_size, seq_len, channel_dim]
            snr_db: Relación señal a ruido en dB (escalar o tensor)
        Returns:
            y: Señal recibida con ruido [batch_size, seq_len, channel_dim]
        """
        if self.training:
            # Convertir SNR de dB a escala lineal
            snr_linear = 10.0 ** (snr_db / 10.0)
            # Calcular la potencia de la señal (ya normalizada a ~1)
            signal_power = torch.mean(z ** 2)
            # Calcular varianza del ruido: sigma^2 = P / SNR
            noise_std = torch.sqrt(signal_power / snr_linear)
            # Truco de reparametrización: muestrear epsilon ~ N(0, I)
            # y escalar por sigma
            epsilon = torch.randn_like(z)
            y = z + noise_std * epsilon
            return y
        else:
            # En modo evaluación, también añadir ruido para simular
            # condiciones reales del canal
            snr_linear = 10.0 ** (snr_db / 10.0)
            signal_power = torch.mean(z ** 2)
            noise_std = torch.sqrt(signal_power / snr_linear)
            epsilon = torch.randn_like(z)
            y = z + noise_std * epsilon
            return y


class RayleighChannel(nn.Module):
    """
    Canal con desvanecimiento Rayleigh diferenciable.
    Implementa y = h ⊙ z + n, donde h ~ CN(0, I) y n ~ N(0, σ²I).
    """
    def __init__(self):
        super().__init__()

    def forward(self, z, snr_db):
        """
        Args:
            z: Señal transmitida [batch_size, seq_len, channel_dim]
            snr_db: Relación señal a ruido en dB
        Returns:
            y: Señal recibida [batch_size, seq_len, channel_dim]
        """
        snr_linear = 10.0 ** (snr_db / 10.0)
        signal_power = torch.mean(z ** 2)
        noise_std = torch.sqrt(signal_power / snr_linear)

        # Coeficientes de desvanecimiento Rayleigh (reparametrizados)
        # Para canal real: |h| ~ Rayleigh, implementado como
        # h = h_real donde h_real ~ N(0, 1/sqrt(2))
        h = torch.randn_like(z) * (1.0 / math.sqrt(2.0))
        epsilon = torch.randn_like(z)

        # y = h ⊙ z + sigma * epsilon
        y = h * z + noise_std * epsilon
        return y


class ChannelDecoder(nn.Module):
    """
    Decoder de Canal: recupera la representación semántica
    a partir de la señal recibida ruidosa.
    Arquitectura espejo del encoder de canal.
    """
    def __init__(self, channel_dim=32, d_model=128):
        super().__init__()
        self.decoder = nn.Sequential(
            nn.Linear(channel_dim, 256),
            nn.ReLU(),
            nn.Linear(256, d_model)
        )

    def forward(self, y):
        """
        Args:
            y: Señal recibida [batch_size, seq_len, channel_dim]
        Returns:
            h_hat: Representación semántica estimada
                   [batch_size, seq_len, d_model]
        """
        h_hat = self.decoder(y)
        return h_hat


class SemanticDecoder(nn.Module):
    """
    Decoder Semántico basado en Transformer.
    Reconstruye la secuencia de tokens a partir de la
    representación semántica recuperada.
    """
    def __init__(self, vocab_size, d_model=128, nhead=8,
                 num_layers=3, dim_feedforward=512, dropout=0.1):
        super().__init__()
        self.d_model = d_model

        # Capas del Transformer Decoder
        decoder_layer = nn.TransformerDecoderLayer(
            d_model=d_model,
            nhead=nhead,
            dim_feedforward=dim_feedforward,
            dropout=dropout,
            batch_first=True
        )
        self.transformer_decoder = nn.TransformerDecoder(
            decoder_layer, num_layers=num_layers
        )

        # Proyección final al vocabulario
        self.fc_out = nn.Linear(d_model, vocab_size)

    def forward(self, h_hat, tgt_embedding,
                tgt_mask=None, tgt_key_padding_mask=None):
        """
        Args:
            h_hat: Representación semántica recuperada (memoria)
                   [batch_size, seq_len_src, d_model]
            tgt_embedding: Embeddings del objetivo (teacher forcing)
                           [batch_size, seq_len_tgt, d_model]
            tgt_mask: Máscara causal para generación autoregresiva
            tgt_key_padding_mask: Máscara de padding del objetivo
        Returns:
            logits: Distribución sobre vocabulario
                    [batch_size, seq_len_tgt, vocab_size]
        """
        decoded = self.transformer_decoder(
            tgt_embedding, h_hat,
            tgt_mask=tgt_mask,
            tgt_key_padding_mask=tgt_key_padding_mask
        )
        logits = self.fc_out(decoded)
        return logits


class E2ESemanticCommSystem(nn.Module):
    """
    Sistema de Comunicación Semántica E2E completo.
    Integra todos los componentes: encoder semántico, encoder de canal,
    canal físico (AWGN o Rayleigh), decoder de canal y decoder semántico.
    """
    def __init__(self, vocab_size, d_model=128, nhead=8,
                 num_encoder_layers=3, num_decoder_layers=3,
                 dim_feedforward=512, channel_dim=32,
                 channel_type='awgn', dropout=0.1):
        super().__init__()
        self.d_model = d_model
        self.vocab_size = vocab_size

        # Componentes del transmisor
        self.semantic_encoder = SemanticEncoder(
            vocab_size, d_model, nhead,
            num_encoder_layers, dim_feedforward, dropout
        )
        self.channel_encoder = ChannelEncoder(d_model, channel_dim)

        # Canal físico
        if channel_type == 'awgn':
            self.channel = AWGNChannel()
        elif channel_type == 'rayleigh':
            self.channel = RayleighChannel()
        else:
            raise ValueError(
                f"Tipo de canal '{channel_type}' no soportado. "
                f"Usar 'awgn' o 'rayleigh'."
            )

        # Componentes del receptor
        self.channel_decoder = ChannelDecoder(channel_dim, d_model)
        self.semantic_decoder = SemanticDecoder(
            vocab_size, d_model, nhead,
            num_decoder_layers, dim_feedforward, dropout
        )

        # Embedding compartido (opcional) para el decoder
        self.tgt_embedding = nn.Embedding(vocab_size, d_model)
        self.tgt_pos_encoder = PositionalEncoding(d_model, dropout=dropout)

    def generate_square_subsequent_mask(self, sz):
        """
        Genera máscara causal triangular superior para el decoder.
        Impide que la posición i atienda a posiciones j > i,
        forzando la generación autoregresiva.
        """
        mask = torch.triu(torch.ones(sz, sz), diagonal=1).bool()
        return mask

    def forward(self, src, tgt, snr_db,
                src_key_padding_mask=None,
                tgt_key_padding_mask=None):
        """
        Propagación hacia adelante completa del sistema E2E.

        Args:
            src: Tokens de entrada [batch_size, src_len]
            tgt: Tokens objetivo [batch_size, tgt_len]
            snr_db: SNR del canal en dB
            src_key_padding_mask: Máscara de padding de la fuente
            tgt_key_padding_mask: Máscara de padding del objetivo
        Returns:
            logits: Predicciones sobre el vocabulario
                    [batch_size, tgt_len, vocab_size]
        """
        # === TRANSMISOR ===
        # Paso 1: Codificación semántica
        h = self.semantic_encoder(
            src, src_key_padding_mask=src_key_padding_mask
        )

        # Paso 2: Codificación de canal + normalización de potencia
        z = self.channel_encoder(h)

        # === CANAL FÍSICO ===
        # Paso 3: Transmisión a través del canal ruidoso
        y = self.channel(z, snr_db)

        # === RECEPTOR ===
        # Paso 4: Decodificación de canal
        h_hat = self.channel_decoder(y)

        # Paso 5: Decodificación semántica (con teacher forcing)
        tgt_emb = self.tgt_embedding(tgt) * math.sqrt(self.d_model)
        tgt_emb = self.tgt_pos_encoder(tgt_emb)
        tgt_mask = self.generate_square_subsequent_mask(
            tgt.size(1)
        ).to(tgt.device)

        logits = self.semantic_decoder(
            h_hat, tgt_emb,
            tgt_mask=tgt_mask,
            tgt_key_padding_mask=tgt_key_padding_mask
        )

        return logits


# ===========================================================
# FUNCIONES DE ENTRENAMIENTO
# ===========================================================

class SNRScheduler:
    """
    Programador de SNR para entrenamiento con currículo.
    Comienza con SNR alta (canal fácil) y gradualmente
    reduce la SNR (canal más difícil).
    """
    def __init__(self, snr_max=20.0, snr_min=0.0,
                 total_epochs=100, mode='linear'):
        self.snr_max = snr_max
        self.snr_min = snr_min
        self.total_epochs = total_epochs
        self.mode = mode

    def get_snr(self, epoch):
        """Calcula la SNR para la época actual."""
        if self.mode == 'linear':
            progress = min(epoch / self.total_epochs, 1.0)
            return self.snr_max - progress * (self.snr_max - self.snr_min)
        elif self.mode == 'cosine':
            progress = min(epoch / self.total_epochs, 1.0)
            return self.snr_min + 0.5 * (self.snr_max - self.snr_min) \
                   * (1 + math.cos(math.pi * progress))
        elif self.mode == 'random':
            # SNR aleatoria uniforme en [snr_min, snr_max]
            return np.random.uniform(self.snr_min, self.snr_max)
        else:
            raise ValueError(f"Modo '{self.mode}' no reconocido.")


def train_epoch(model, dataloader, optimizer, snr_db,
                pad_idx, device):
    """
    Entrena el modelo durante una época completa.

    Args:
        model: Sistema E2E de comunicación semántica
        dataloader: DataLoader con pares (src, tgt) de texto
        optimizer: Optimizador (Adam recomendado)
        snr_db: SNR del canal para esta época
        pad_idx: Índice del token de padding en el vocabulario
        device: Dispositivo de cómputo (CPU o GPU)

    Returns:
        avg_loss: Pérdida promedio de la época
    """
    model.train()
    total_loss = 0
    num_batches = 0

    for batch_idx, (src, tgt) in enumerate(dataloader):
        src = src.to(device)     # [batch_size, src_len]
        tgt = tgt.to(device)     # [batch_size, tgt_len]

        # Preparar entrada y objetivo del decoder
        # (desplazamiento de un token para teacher forcing)
        tgt_input = tgt[:, :-1]  # Todos menos el último token
        tgt_label = tgt[:, 1:]   # Todos menos el primer token

        # Crear máscaras de padding
        src_pad_mask = (src == pad_idx)
        tgt_pad_mask = (tgt_input == pad_idx)

        # Paso 1: Forward pass completo
        optimizer.zero_grad()
        logits = model(
            src, tgt_input, snr_db,
            src_key_padding_mask=src_pad_mask,
            tgt_key_padding_mask=tgt_pad_mask
        )

        # Paso 2: Calcular pérdida de entropía cruzada
        # Reshape para compatibilidad con cross_entropy:
        # logits: [batch * tgt_len, vocab_size]
        # labels: [batch * tgt_len]
        loss = F.cross_entropy(
            logits.reshape(-1, logits.size(-1)),
            tgt_label.reshape(-1),
            ignore_index=pad_idx
        )

        # Paso 3: Retropropagación a través de todo el sistema,
        # incluyendo el canal (gracias a la reparametrización)
        loss.backward()

        # Gradient clipping para estabilidad
        torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)

        # Paso 4: Actualización conjunta de todos los parámetros
        optimizer.step()

        total_loss += loss.item()
        num_batches += 1

    avg_loss = total_loss / max(num_batches, 1)
    return avg_loss


@torch.no_grad()
def evaluate(model, dataloader, snr_db, pad_idx, device):
    """
    Evalúa el modelo en un conjunto de datos de validación.

    Args:
        model: Sistema E2E
        dataloader: DataLoader de validación
        snr_db: SNR del canal para evaluación
        pad_idx: Índice del token de padding
        device: Dispositivo de cómputo

    Returns:
        avg_loss: Pérdida promedio de validación
    """
    model.eval()
    total_loss = 0
    num_batches = 0

    for src, tgt in dataloader:
        src = src.to(device)
        tgt = tgt.to(device)

        tgt_input = tgt[:, :-1]
        tgt_label = tgt[:, 1:]

        src_pad_mask = (src == pad_idx)
        tgt_pad_mask = (tgt_input == pad_idx)

        logits = model(
            src, tgt_input, snr_db,
            src_key_padding_mask=src_pad_mask,
            tgt_key_padding_mask=tgt_pad_mask
        )

        loss = F.cross_entropy(
            logits.reshape(-1, logits.size(-1)),
            tgt_label.reshape(-1),
            ignore_index=pad_idx
        )

        total_loss += loss.item()
        num_batches += 1

    return total_loss / max(num_batches, 1)


def train_e2e_system(model, train_loader, val_loader,
                     num_epochs=100, lr=1e-4, pad_idx=0,
                     snr_max=20.0, snr_min=0.0,
                     snr_mode='linear', device='cpu'):
    """
    Bucle de entrenamiento completo con currículo de SNR.

    Args:
        model: Sistema E2E de comunicación semántica
        train_loader: DataLoader de entrenamiento
        val_loader: DataLoader de validación
        num_epochs: Número de épocas de entrenamiento
        lr: Tasa de aprendizaje inicial
        pad_idx: Índice del token de padding
        snr_max: SNR máxima (dB) al inicio del entrenamiento
        snr_min: SNR mínima (dB) al final del entrenamiento
        snr_mode: Modo del programador de SNR
        device: Dispositivo de cómputo
    """
    model = model.to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=lr, betas=(0.9, 0.999))

    # Programador de tasa de aprendizaje con calentamiento
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(
        optimizer, T_max=num_epochs, eta_min=lr * 0.01
    )

    # Programador de SNR con currículo
    snr_scheduler = SNRScheduler(
        snr_max=snr_max, snr_min=snr_min,
        total_epochs=num_epochs, mode=snr_mode
    )

    best_val_loss = float('inf')

    for epoch in range(num_epochs):
        # Obtener SNR para esta época (currículo)
        current_snr = snr_scheduler.get_snr(epoch)

        # Entrenamiento
        train_loss = train_epoch(
            model, train_loader, optimizer,
            current_snr, pad_idx, device
        )

        # Validación (evaluada a múltiples SNR)
        val_loss = evaluate(
            model, val_loader, current_snr, pad_idx, device
        )

        # Actualizar tasa de aprendizaje
        scheduler.step()

        # Guardar mejor modelo
        if val_loss < best_val_loss:
            best_val_loss = val_loss
            torch.save(model.state_dict(), 'best_semcom_model.pth')

        # Registro de progreso
        if (epoch + 1) % 10 == 0:
            print(
                f"Época [{epoch+1}/{num_epochs}] | "
                f"SNR: {current_snr:.1f} dB | "
                f"Pérdida Train: {train_loss:.4f} | "
                f"Pérdida Val: {val_loss:.4f} | "
                f"LR: {scheduler.get_last_lr()[0]:.6f}"
            )


# ===========================================================
# EJEMPLO DE USO
# ===========================================================

if __name__ == "__main__":
    # Hiperparámetros del sistema
    VOCAB_SIZE = 30000    # Tamaño del vocabulario (BPE tokens)
    D_MODEL = 128         # Dimensión del modelo Transformer
    NHEAD = 8             # Número de cabezas de atención
    NUM_ENC_LAYERS = 3    # Capas del encoder Transformer
    NUM_DEC_LAYERS = 3    # Capas del decoder Transformer
    DIM_FF = 512          # Dimensión de la red feed-forward
    CHANNEL_DIM = 16      # Dimensión del canal (2n para n símbolos)
    CHANNEL_TYPE = 'awgn' # Tipo de canal: 'awgn' o 'rayleigh'
    DROPOUT = 0.1         # Probabilidad de dropout

    # Crear el sistema E2E
    system = E2ESemanticCommSystem(
        vocab_size=VOCAB_SIZE,
        d_model=D_MODEL,
        nhead=NHEAD,
        num_encoder_layers=NUM_ENC_LAYERS,
        num_decoder_layers=NUM_DEC_LAYERS,
        dim_feedforward=DIM_FF,
        channel_dim=CHANNEL_DIM,
        channel_type=CHANNEL_TYPE,
        dropout=DROPOUT
    )

    # Contar parámetros totales del sistema
    total_params = sum(p.numel() for p in system.parameters())
    trainable_params = sum(
        p.numel() for p in system.parameters() if p.requires_grad
    )
    print(f"Parámetros totales: {total_params:,}")
    print(f"Parámetros entrenables: {trainable_params:,}")
    print(f"Razón de codificación k/n: "
          f"{D_MODEL}/{CHANNEL_DIM} = {D_MODEL/CHANNEL_DIM:.2f}")

    # Ejemplo de forward pass con datos sintéticos
    batch_size = 4
    src_len = 20
    tgt_len = 20
    snr_db = 10.0  # 10 dB

    src = torch.randint(1, VOCAB_SIZE, (batch_size, src_len))
    tgt = torch.randint(1, VOCAB_SIZE, (batch_size, tgt_len))

    # Forward pass
    logits = system(src, tgt[:, :-1], snr_db)
    print(f"\nForward pass exitoso:")
    print(f"  Entrada: {src.shape}")
    print(f"  Salida (logits): {logits.shape}")
    print(f"  SNR del canal: {snr_db} dB")
```

### 8.8.2 Explicación detallada de los componentes del código

El código anterior implementa cada componente del sistema E2E tal como se describió en las subsecciones anteriores. A continuación, detallamos los aspectos más relevantes de la implementación:

**Clase `PositionalEncoding`:** Implementa la codificación posicional sinusoidal estándar del Transformer. La matriz de codificaciones se pre-calcula para todas las posiciones hasta `max_len` y se almacena como un buffer (no como parámetro entrenable) mediante `register_buffer`. Esto es eficiente porque la codificación posicional no cambia durante el entrenamiento.

**Clase `SemanticEncoder`:** El encoder semántico utiliza `nn.TransformerEncoderLayer` de PyTorch, que internamente implementa la auto-atención multi-cabeza, las conexiones residuales, la normalización de capa y la red *feed-forward*. La capa de embedding incluye el escalado por $\sqrt{d_{model}}$, que es una práctica estándar para estabilizar los gradientes durante el entrenamiento (compensando el hecho de que los embeddings se inicializan con valores pequeños).

**Clase `ChannelEncoder`:** La codificación de canal se realiza mediante dos capas densas con activación ReLU intermedia. La función `power_normalize` implementa la normalización de potencia dividiendo cada vector de símbolos por su norma RMS (raíz cuadrada de la media de los cuadrados), lo que garantiza que la potencia promedio por dimensión sea unitaria.

**Clases `AWGNChannel` y `RayleighChannel`:** Estas clases implementan los canales diferenciables. Observe cómo la reparametrización se aplica explícitamente: primero se genera $\boldsymbol{\epsilon} \sim \mathcal{N}(\mathbf{0}, \mathbf{I})$ con `torch.randn_like(z)`, y luego se escala por $\sigma$ para obtener el ruido con la varianza deseada. Dado que `torch.randn_like` genera tensores que no forman parte del grafo computacional de los parámetros, pero $\mathbf{z}$ sí lo es, los gradientes pueden fluir a través de la suma $\mathbf{y} = \mathbf{z} + \sigma\boldsymbol{\epsilon}$ sin problemas.

**Clase `SemanticDecoder`:** El decoder semántico utiliza `nn.TransformerDecoderLayer`, que implementa la auto-atención enmascarada (causal), la atención cruzada con la representación del encoder, y la red *feed-forward*. La máscara causal, generada por `generate_square_subsequent_mask`, es una matriz triangular superior booleana que impide que la posición $i$ atienda a posiciones $j > i$, forzando la generación autoregresiva durante el entrenamiento.

**Función `train_epoch`:** Implementa el bucle de entrenamiento estándar con *teacher forcing*: al decoder se le proporciona la secuencia objetivo desplazada un token (`tgt[:, :-1]`) como entrada, y se le pide predecir la secuencia objetivo desplazada en la otra dirección (`tgt[:, 1:]`). El *gradient clipping* (limitación de la norma del gradiente a 1.0) es una técnica importante para la estabilidad del entrenamiento de Transformers, que son propensos a gradientes explosivos.

**Clase `SNRScheduler`:** Implementa tres estrategias de programación de SNR: lineal (decrecimiento uniforme), coseno (decrecimiento suave con inicio y final lentos) y aleatorio (SNR uniformemente distribuida en cada época). La estrategia coseno es generalmente preferida en la práctica, ya que proporciona una transición más suave y dedica más tiempo tanto a SNR altas (aprendizaje de representaciones) como a SNR bajas (aprendizaje de robustez).

---

## 8.9 Resumen y Conexiones

En esta sección hemos desarrollado de manera exhaustiva los sistemas de comunicación semántica de extremo a extremo, desde sus fundamentos arquitectónicos hasta su implementación práctica. Los puntos clave son:

1. **Diseño conjunto:** La fusión de la codificación de fuente, la codificación de canal y la modulación en una única red neuronal diferenciable permite una optimización global que supera el rendimiento de los sistemas diseñados por separado, especialmente en regímenes de longitud de bloque finita.

2. **Canal diferenciable:** El modelado del canal físico como una capa estocástica diferenciable, junto con el truco de reparametrización, permite que los gradientes fluyan a través de todo el sistema durante el entrenamiento.

3. **Funciones de pérdida semánticas:** La elección de funciones de pérdida que operan a nivel de significado —como la similitud coseno de embeddings o la pérdida perceptual— es fundamental para que el sistema optimice la fidelidad semántica en lugar de la fidelidad bit a bit.

4. **Degradación suave:** Una de las propiedades más valiosas de los sistemas E2E es la degradación gradual de la calidad con la SNR, en contraste con el efecto acantilado catastrófico de los sistemas convencionales.

Los sistemas aquí descritos constituyen la base sobre la cual se construyen las variantes más avanzadas que se explorarán en las secciones posteriores: sistemas adaptativos, sistemas multi-usuario, y sistemas con retroalimentación semántica.

---

### Referencias

- Xie, H., Qin, Z., Li, G. Y., & Juang, B.-H. (2021). Deep learning enabled semantic communication systems. *IEEE Transactions on Signal Processing*, 69, 2663–2675. DOI: [10.1109/TSP.2021.3071082](https://doi.org/10.1109/TSP.2021.3071082)

- Bourtsoulatze, E., Kurka, D. B., & Gündüz, D. (2019). Deep joint source-channel coding for wireless image transmission. *IEEE Transactions on Cognitive Communications and Networking*, 5(3), 567–579. DOI: [10.1109/TCCN.2019.2919300](https://doi.org/10.1109/TCCN.2019.2919300)

- Farsad, N., Rao, M., & Goldsmith, A. (2018). Deep learning for joint source-channel coding of text. *IEEE Transactions on Communications*, 66(11), 5765–5775. DOI: [10.1109/TCOMM.2018.2827020](https://doi.org/10.1109/TCOMM.2018.2827020)
