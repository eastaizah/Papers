# Sección 1: Introducción y Fundamentos de las Neuronas Artificiales

---

## 1.1 Introducción al tutorial

Las comunicaciones semánticas representan un cambio de paradigma en la ingeniería de telecomunicaciones. Mientras que los sistemas de comunicación convencionales —desde los trabajos fundacionales de Claude Shannon en 1948— se han enfocado en transmitir bits de forma confiable a través de un canal ruidoso, las comunicaciones semánticas buscan transmitir el *significado* de la información, priorizando la relevancia y la interpretación del mensaje en el receptor por encima de la reproducción exacta de cada símbolo transmitido. Este enfoque, anticipado conceptualmente por Warren Weaver en su célebre artículo conjunto con Shannon, ha cobrado nueva relevancia gracias a los avances extraordinarios de la inteligencia artificial (IA), y en particular del aprendizaje profundo (*deep learning*), que proporcionan las herramientas matemáticas y computacionales necesarias para extraer, codificar y reconstruir el contenido semántico de señales complejas como texto, voz, imágenes y video.

El presente tutorial tiene como objetivo ofrecer una guía completa, rigurosa y autocontenida que permita al lector —ya sea estudiante de posgrado, investigador o ingeniero profesional en telecomunicaciones— comprender los fundamentos de la inteligencia artificial que sustentan las comunicaciones semánticas modernas. El recorrido comienza aquí, en esta primera sección, con los bloques de construcción más elementales: la neurona artificial y el perceptrón. A partir de estos conceptos básicos, las secciones posteriores del tutorial irán construyendo, de manera progresiva, las arquitecturas más sofisticadas que habilitan los sistemas de comunicación semántica de vanguardia: redes neuronales profundas, redes convolucionales (CNN), redes recurrentes (RNN y LSTM), mecanismos de atención, transformers, autoencoders variacionales (VAE), redes generativas adversarias (GAN) y, finalmente, su integración en esquemas de codificación y decodificación conjunta de fuente y canal (*Joint Source-Channel Coding*, JSCC).

La motivación de este tutorial es doble. Por un lado, existe una brecha significativa entre la literatura de aprendizaje automático —frecuentemente orientada a la visión por computadora o el procesamiento de lenguaje natural— y las necesidades específicas de la comunidad de telecomunicaciones. Muchos textos asumen familiaridad con conceptos de IA que no forman parte de la formación tradicional de un ingeniero de comunicaciones. Por otro lado, la literatura emergente sobre comunicaciones semánticas a menudo presupone un dominio de arquitecturas de aprendizaje profundo sin ofrecer las bases necesarias para comprenderlas. Este tutorial busca cerrar ambas brechas, proporcionando un camino pedagógico que parte desde los principios más básicos de las redes neuronales hasta su aplicación concreta en sistemas de comunicación semántica.

A lo largo de todo el tutorial se adoptará un enfoque formal pero accesible: cada concepto se introducirá con intuición geométrica o física, se formalizará mediante ecuaciones matemáticas expresadas con rigor y se ilustrará con ejemplos concretos. Se utilizará notación vectorial y matricial estándar, y todas las ecuaciones se presentarán en formato LaTeX para facilitar su reproducción. No se asumirán conocimientos previos de aprendizaje automático, aunque sí se espera familiaridad con álgebra lineal, cálculo multivariable y probabilidad a nivel de pregrado en ingeniería.

---

## 1.2 La neurona biológica y la neurona artificial

### 1.2.1 La neurona biológica

El cerebro humano está compuesto por aproximadamente $8.6 \times 10^{10}$ neuronas (86 mil millones), interconectadas a través de una red extraordinariamente compleja de conexiones sinápticas cuyo número se estima en el orden de $10^{14}$ a $10^{15}$. Cada neurona biológica es una célula especializada en el procesamiento y la transmisión de señales electroquímicas que, en su conjunto, dan lugar a la cognición, la percepción, el aprendizaje y la memoria. Comprender la estructura y el funcionamiento básico de la neurona biológica resulta fundamental, ya que la neurona artificial se concibió originalmente como una abstracción simplificada de su contraparte natural.

La estructura de una neurona biológica puede describirse mediante tres componentes funcionales principales:

1. **Dendritas:** Son las ramificaciones que se extienden desde el cuerpo celular y actúan como las "antenas receptoras" de la neurona. Las dendritas reciben señales electroquímicas provenientes de otras neuronas a través de las sinapsis. Una neurona típica puede tener miles de conexiones dendríticas, cada una de las cuales recibe una señal con una intensidad (o "peso") diferente, determinada por la eficacia sináptica de cada conexión. Es precisamente esta eficacia sináptica variable la que constituye el sustrato biológico del aprendizaje: cuando una conexión se refuerza (potenciación a largo plazo, LTP) o se debilita (depresión a largo plazo, LTD), la neurona modifica su respuesta ante determinados patrones de entrada.

2. **Soma (cuerpo celular):** El soma es el componente central de la neurona, donde se encuentra el núcleo celular. Desde la perspectiva del procesamiento de información, el soma realiza una función de integración: acumula las señales electroquímicas recibidas a través de las dendritas, sumando tanto las señales excitatorias (que tienden a activar la neurona) como las inhibitorias (que tienden a suprimirla). Si la suma neta de estas señales supera un cierto umbral de activación —conocido como potencial de umbral, típicamente alrededor de $-55$ mV en una neurona humana—, la neurona se "dispara", generando un potencial de acción.

3. **Axón:** Es la prolongación que se extiende desde el soma y se encarga de transmitir el potencial de acción hacia otras neuronas. El axón puede ramificarse en sus terminales (terminales axónicas o botones sinápticos), permitiendo que una sola neurona transmita su señal a miles de neuronas receptoras. La transmisión a lo largo del axón es de naturaleza binaria en cierto sentido: la neurona dispara o no dispara (principio de "todo o nada"), aunque la frecuencia de disparo puede variar, codificando así información de manera analógica a través de un mecanismo digital.

### 1.2.2 La neurona artificial: el modelo de McCulloch-Pitts y sus extensiones

En 1943, Warren McCulloch y Walter Pitts propusieron el primer modelo matemático de una neurona, estableciendo las bases de lo que hoy conocemos como redes neuronales artificiales. Su modelo, aunque extremadamente simplificado respecto a la complejidad biológica real, captura la esencia computacional de una neurona: recibir múltiples entradas, ponderarlas, sumarlas y producir una salida basada en si la suma supera un umbral.

La neurona artificial opera de la siguiente manera:

1. **Entradas ($x_1, x_2, \ldots, x_n$):** Análogas a las señales recibidas por las dendritas, representan los datos o características que alimentan a la neurona. Cada entrada $x_i$ es un valor numérico que puede provenir de los datos originales del problema o de la salida de otra neurona en una capa anterior.

2. **Pesos sinápticos ($w_1, w_2, \ldots, w_n$):** Cada conexión de entrada tiene asociado un peso $w_i \in \mathbb{R}$ que modula la importancia de la señal correspondiente. Los pesos son análogos a la eficacia sináptica en la neurona biológica: un peso grande (en valor absoluto) indica una conexión fuerte, mientras que un peso cercano a cero indica una conexión débil. Los pesos positivos modelan conexiones excitatorias y los pesos negativos, conexiones inhibitorias. El aprendizaje en una red neuronal artificial consiste, fundamentalmente, en ajustar estos pesos.

3. **Suma ponderada y sesgo (*bias*):** La neurona computa la suma ponderada de sus entradas más un término de sesgo $b$:

$$z = \sum_{i=1}^{n} w_i x_i + b = w_1 x_1 + w_2 x_2 + \cdots + w_n x_n + b$$

En notación vectorial, si definimos el vector de entradas $\mathbf{x} = [x_1, x_2, \ldots, x_n]^T \in \mathbb{R}^n$ y el vector de pesos $\mathbf{w} = [w_1, w_2, \ldots, w_n]^T \in \mathbb{R}^n$, la expresión anterior se escribe de forma compacta como:

$$z = \mathbf{w}^T \mathbf{x} + b$$

El término $z$ se denomina frecuentemente *pre-activación* o *logit*. El sesgo $b$ cumple una función análoga al umbral de activación de la neurona biológica (con signo invertido): permite desplazar la frontera de decisión de la neurona sin depender de los valores de entrada.

4. **Función de activación ($f$):** La salida final de la neurona se obtiene aplicando una función de activación $f(\cdot)$ a la pre-activación:

$$y = f(z) = f(\mathbf{w}^T \mathbf{x} + b)$$

La función de activación introduce no linealidad en el modelo. En la neurona biológica, esta no linealidad corresponde al mecanismo de disparo (todo o nada) del potencial de acción. En la neurona artificial, la elección de la función de activación es un aspecto de diseño fundamental que afecta profundamente la capacidad expresiva de la red y las propiedades de su entrenamiento, como se discutirá en detalle en la Sección 1.4.

5. **Salida ($y$):** El valor producido por la función de activación, análogo al potencial de acción transmitido por el axón. Esta salida puede servir como entrada a otras neuronas o como la predicción final del modelo.

**Figura 1.1:** *Diagrama comparativo entre la neurona biológica y la neurona artificial. En el lado izquierdo se ilustra una neurona biológica con sus tres componentes principales: (i) las dendritas, representadas como ramificaciones arbóreas que se extienden desde el cuerpo celular y que reciben señales electroquímicas de otras neuronas a través de las sinapsis; (ii) el soma o cuerpo celular, dibujado como una forma ovalada central que contiene el núcleo, donde se realiza la integración de todas las señales recibidas; y (iii) el axón, representado como una prolongación larga que parte del soma y se ramifica en su extremo terminal en múltiples botones sinápticos que transmiten la señal a las dendritas de neuronas subsiguientes. Las flechas indican el flujo de información desde las dendritas, pasando por el soma, hasta las terminales del axón. En el lado derecho se muestra el modelo matemático de la neurona artificial: las entradas $x_1, x_2, \ldots, x_n$ llegan por la izquierda, cada una multiplicada por su peso correspondiente $w_1, w_2, \ldots, w_n$ (representados como valores numéricos junto a cada conexión). Todas las señales ponderadas convergen en un nodo sumador circular marcado con el símbolo $\Sigma$, que calcula $z = \sum_{i} w_i x_i + b$, donde el sesgo $b$ entra como una entrada adicional con valor constante igual a 1. La salida del sumador alimenta un bloque rectangular etiquetado $f(\cdot)$ que representa la función de activación. Finalmente, la salida $y = f(z)$ emerge por la derecha. Líneas de correspondencia punteadas conectan las dendritas con las entradas ponderadas, el soma con el sumador y la función de activación, y el axón con la salida, evidenciando la analogía funcional entre ambos modelos.*

Es importante enfatizar que la neurona artificial es una simplificación drástica de la biología real. Las neuronas biológicas exhiben dinámicas temporales complejas, operan con pulsos (*spikes*) en lugar de valores continuos, poseen una geometría tridimensional intrincada y se comunican mediante mecanismos químicos y eléctricos sofisticados. No obstante, la abstracción de McCulloch-Pitts y sus extensiones posteriores han demostrado ser extraordinariamente poderosas para tareas de reconocimiento de patrones, clasificación, regresión y, como veremos en este tutorial, para el diseño de sistemas de comunicación semántica.

---

## 1.3 El Perceptrón simple

### 1.3.1 Definición y modelo matemático

El perceptrón, propuesto por Frank Rosenblatt en 1958, constituye el modelo más simple de neurona artificial con capacidad de aprendizaje. A diferencia del modelo estático de McCulloch-Pitts, donde los pesos debían ser determinados manualmente, Rosenblatt introdujo un algoritmo de aprendizaje que permite a la neurona ajustar automáticamente sus pesos a partir de ejemplos de entrenamiento. Este avance marcó el nacimiento del aprendizaje automático supervisado.

El perceptrón simple recibe un vector de entrada $\mathbf{x} = [x_1, x_2, \ldots, x_n]^T \in \mathbb{R}^n$ y produce una salida binaria $y \in \{0, 1\}$ (o equivalentemente $y \in \{-1, +1\}$ según la convención utilizada). Su operación se describe matemáticamente de la siguiente forma:

**Paso 1: Cómputo de la pre-activación.** Se calcula la suma ponderada de las entradas más el sesgo:

$$z = \sum_{i=1}^{n} w_i x_i + b = \mathbf{w}^T \mathbf{x} + b$$

donde $\mathbf{w} = [w_1, w_2, \ldots, w_n]^T \in \mathbb{R}^n$ es el vector de pesos y $b \in \mathbb{R}$ es el sesgo.

**Paso 2: Aplicación de la función de activación escalón.** La salida del perceptrón se determina mediante la función escalón unitario (función de Heaviside):

$$y = f(z) = \begin{cases} 1 & \text{si } z \geq 0 \\ 0 & \text{si } z < 0 \end{cases}$$

Es decir:

$$y = f\left(\sum_{i=1}^{n} w_i x_i + b\right) = f(\mathbf{w}^T \mathbf{x} + b)$$

El perceptrón, por tanto, implementa un clasificador binario: dado un punto $\mathbf{x}$ en el espacio $n$-dimensional, la salida es 1 si el punto cae en un lado de una frontera de decisión, y 0 si cae en el otro.

### 1.3.2 Interpretación geométrica: la frontera de decisión como un hiperplano

Una de las perspectivas más reveladoras para comprender el perceptrón es la interpretación geométrica. La condición de decisión del perceptrón es:

$$\mathbf{w}^T \mathbf{x} + b = 0$$

Esta ecuación define un **hiperplano** en el espacio $\mathbb{R}^n$. Un hiperplano es la generalización a $n$ dimensiones de los conceptos familiares de punto (0D), línea (1D) y plano (2D). Específicamente:

- En $\mathbb{R}^1$ (una sola entrada), la frontera de decisión es un punto en la recta real: $w_1 x_1 + b = 0 \Rightarrow x_1 = -b/w_1$.
- En $\mathbb{R}^2$ (dos entradas), la frontera de decisión es una línea recta: $w_1 x_1 + w_2 x_2 + b = 0$.
- En $\mathbb{R}^3$ (tres entradas), la frontera de decisión es un plano: $w_1 x_1 + w_2 x_2 + w_3 x_3 + b = 0$.
- En $\mathbb{R}^n$, es un hiperplano $(n-1)$-dimensional.

El vector de pesos $\mathbf{w}$ es **normal** (perpendicular) al hiperplano de decisión. Para verificar esto, consideremos dos puntos $\mathbf{x}_a$ y $\mathbf{x}_b$ que yacen sobre el hiperplano, de modo que $\mathbf{w}^T \mathbf{x}_a + b = 0$ y $\mathbf{w}^T \mathbf{x}_b + b = 0$. Restando ambas ecuaciones:

$$\mathbf{w}^T (\mathbf{x}_a - \mathbf{x}_b) = 0$$

Esto demuestra que $\mathbf{w}$ es ortogonal a cualquier vector contenido en el hiperplano, es decir, $\mathbf{w}$ es el vector normal del hiperplano. La dirección de $\mathbf{w}$ apunta hacia la región donde $y = 1$ (la clase positiva), y el sesgo $b$ determina la distancia del hiperplano al origen, que está dada por:

$$d = \frac{|b|}{\|\mathbf{w}\|}$$

donde $\|\mathbf{w}\| = \sqrt{w_1^2 + w_2^2 + \cdots + w_n^2}$ es la norma euclidiana del vector de pesos.

Esta interpretación geométrica tiene consecuencias fundamentales. El perceptrón solo puede resolver problemas de clasificación **linealmente separables**, es decir, aquellos en los que existe un hiperplano que separa perfectamente las dos clases. Como demostraron Minsky y Papert en su influyente libro de 1969, existen problemas aparentemente simples —como la función XOR— que no son linealmente separables y, por tanto, no pueden ser resueltos por un perceptrón simple.

### 1.3.3 Ejemplo: implementación de la compuerta OR

Para ilustrar concretamente el funcionamiento del perceptrón, consideremos la implementación de la función lógica OR. La tabla de verdad de la compuerta OR con dos entradas es:

| $x_1$ | $x_2$ | $y = x_1 \text{ OR } x_2$ |
|:------:|:------:|:--------------------------:|
|   0    |   0    |             0              |
|   0    |   1    |             1              |
|   1    |   0    |             1              |
|   1    |   1    |             1              |

Necesitamos encontrar valores de $w_1$, $w_2$ y $b$ tales que el perceptrón produzca las salidas correctas. La frontera de decisión debe separar el punto $(0,0)$ (clase 0) de los puntos $(0,1)$, $(1,0)$ y $(1,1)$ (clase 1).

Seleccionemos los siguientes parámetros: $w_1 = 1$, $w_2 = 1$ y $b = -0.5$. Verifiquemos cada caso:

1. **Entrada** $(0, 0)$: $z = 1 \cdot 0 + 1 \cdot 0 + (-0.5) = -0.5 < 0 \Rightarrow y = 0$ ✓
2. **Entrada** $(0, 1)$: $z = 1 \cdot 0 + 1 \cdot 1 + (-0.5) = 0.5 \geq 0 \Rightarrow y = 1$ ✓
3. **Entrada** $(1, 0)$: $z = 1 \cdot 1 + 1 \cdot 0 + (-0.5) = 0.5 \geq 0 \Rightarrow y = 1$ ✓
4. **Entrada** $(1, 1)$: $z = 1 \cdot 1 + 1 \cdot 1 + (-0.5) = 1.5 \geq 0 \Rightarrow y = 1$ ✓

La frontera de decisión está dada por la ecuación:

$$x_1 + x_2 - 0.5 = 0 \quad \Longrightarrow \quad x_2 = -x_1 + 0.5$$

Esta es una recta en el plano $x_1$-$x_2$ con pendiente $-1$ y ordenada al origen $0.5$. El vector normal a esta recta es $\mathbf{w} = [1, 1]^T$, que apunta hacia la región donde la salida es 1.

Observemos que la solución no es única. Por ejemplo, los parámetros $w_1 = 2$, $w_2 = 2$, $b = -1$ también funcionan, generando la frontera $2x_1 + 2x_2 - 1 = 0$, que es equivalente a $x_1 + x_2 = 0.5$. De hecho, cualquier hiperplano que separe correctamente el punto $(0,0)$ de los demás será una solución válida, lo que ilustra que en problemas linealmente separables la solución del perceptrón no es única.

**Figura 1.2:** *Visualización de la frontera de decisión del perceptrón para la compuerta OR en el plano $x_1$-$x_2$. Se representan los cuatro puntos de la tabla de verdad: el punto $(0,0)$ se marca con un símbolo circular vacío (○) indicando la clase 0, mientras que los puntos $(0,1)$, $(1,0)$ y $(1,1)$ se marcan con símbolos circulares rellenos (●) indicando la clase 1. La línea de decisión $x_1 + x_2 = 0.5$ se traza como una recta diagonal que va desde el punto $(0, 0.5)$ hasta el punto $(0.5, 0)$, separando perfectamente el punto de clase 0 del resto de puntos de clase 1. La región por encima y a la derecha de la recta (sombreada en azul claro) corresponde a la zona donde $z \geq 0$ y la salida es $y = 1$. La región por debajo y a la izquierda (sin sombrear) corresponde a $z < 0$ y salida $y = 0$. Una flecha etiquetada $\mathbf{w} = [1,1]^T$ parte perpendicular a la recta, apuntando hacia la región de clase positiva, indicando la dirección del vector normal al hiperplano de decisión. Los ejes están etiquetados como $x_1$ (horizontal) y $x_2$ (vertical), con marcas en $0$, $0.5$ y $1$.*

---

## 1.4 Funciones de activación

La función de activación es uno de los componentes más críticos de una neurona artificial. Su papel fundamental es introducir **no linealidad** en el modelo. Sin funciones de activación no lineales, una red neuronal de múltiples capas colapsaría matemáticamente en una sola transformación lineal, ya que la composición de funciones lineales es, a su vez, lineal:

$$f_2(f_1(\mathbf{x})) = \mathbf{W}_2(\mathbf{W}_1 \mathbf{x} + \mathbf{b}_1) + \mathbf{b}_2 = \mathbf{W}_2 \mathbf{W}_1 \mathbf{x} + \mathbf{W}_2 \mathbf{b}_1 + \mathbf{b}_2 = \tilde{\mathbf{W}} \mathbf{x} + \tilde{\mathbf{b}}$$

donde $\tilde{\mathbf{W}} = \mathbf{W}_2 \mathbf{W}_1$ y $\tilde{\mathbf{b}} = \mathbf{W}_2 \mathbf{b}_1 + \mathbf{b}_2$. Esto significa que sin no linealidad, agregar capas no incrementa la capacidad expresiva de la red.

A continuación se presentan las funciones de activación más importantes, organizadas desde la más simple hasta las más sofisticadas.

### 1.4.1 Función escalón (Heaviside)

La función escalón, también conocida como función de Heaviside, es la función de activación más simple y fue la utilizada en el perceptrón original de Rosenblatt:

$$f(z) = \theta(z) = \begin{cases} 1 & \text{si } z \geq 0 \\ 0 & \text{si } z < 0 \end{cases}$$

Alternativamente, usando la convención con salidas en $\{-1, +1\}$:

$$f(z) = \text{sgn}(z) = \begin{cases} +1 & \text{si } z \geq 0 \\ -1 & \text{si } z < 0 \end{cases}$$

La función escalón produce una salida binaria, lo que resulta natural para problemas de clasificación. Sin embargo, presenta una limitación fundamental para el entrenamiento mediante descenso de gradiente: su derivada es cero en todo punto excepto en $z = 0$, donde no está definida (o formalmente, es una distribución delta de Dirac):

$$\frac{d\theta}{dz} = \begin{cases} 0 & \text{si } z \neq 0 \\ \text{indefinida} & \text{si } z = 0 \end{cases}$$

Esta propiedad hace que los métodos de optimización basados en gradientes no puedan utilizarse con la función escalón, ya que el gradiente no proporciona información sobre la dirección en la que deben ajustarse los pesos. Por esta razón, la función escalón se utiliza en la actualidad casi exclusivamente con fines pedagógicos.

### 1.4.2 Función sigmoide (logística)

La función sigmoide, también llamada función logística, fue durante décadas la función de activación estándar en las redes neuronales:

$$\sigma(z) = \frac{1}{1 + e^{-z}}$$

La función sigmoide mapea cualquier valor real $z \in (-\infty, +\infty)$ al intervalo $(0, 1)$, lo que permite interpretarla como una probabilidad. Sus propiedades principales son:

- **Rango:** $(0, 1)$. Nótese que los valores 0 y 1 son límites asintóticos que nunca se alcanzan exactamente.
- **Monotonía:** Es estrictamente creciente para todo $z$.
- **Simetría:** Satisface la relación $\sigma(-z) = 1 - \sigma(z)$.
- **Punto de inflexión:** En $z = 0$, donde $\sigma(0) = 0.5$.
- **Comportamiento asintótico:** $\lim_{z \to -\infty} \sigma(z) = 0$ y $\lim_{z \to +\infty} \sigma(z) = 1$.

**Derivación de la derivada de la sigmoide.** Una propiedad matemática notable de la sigmoide es que su derivada puede expresarse de forma cerrada en términos de sí misma. Derivemos este resultado paso a paso:

$$\sigma(z) = \frac{1}{1 + e^{-z}} = (1 + e^{-z})^{-1}$$

Aplicando la regla de la cadena:

$$\sigma'(z) = \frac{d}{dz}\left[(1 + e^{-z})^{-1}\right] = -(1 + e^{-z})^{-2} \cdot \frac{d}{dz}(1 + e^{-z})$$

El término $\frac{d}{dz}(1 + e^{-z}) = -e^{-z}$, por lo que:

$$\sigma'(z) = -(1 + e^{-z})^{-2} \cdot (-e^{-z}) = \frac{e^{-z}}{(1 + e^{-z})^2}$$

Ahora, observemos que:

$$\sigma(z) \cdot (1 - \sigma(z)) = \frac{1}{1 + e^{-z}} \cdot \frac{e^{-z}}{1 + e^{-z}} = \frac{e^{-z}}{(1 + e^{-z})^2}$$

donde hemos utilizado que $1 - \sigma(z) = 1 - \frac{1}{1+e^{-z}} = \frac{e^{-z}}{1+e^{-z}}$. Comparando ambas expresiones, concluimos:

$$\boxed{\sigma'(z) = \sigma(z)(1 - \sigma(z))}$$

Este resultado es computacionalmente conveniente, ya que durante el entrenamiento de la red, si ya se ha calculado $\sigma(z)$, obtener su derivada requiere solo una multiplicación y una resta. El valor máximo de la derivada ocurre en $z = 0$, donde $\sigma'(0) = 0.5 \times 0.5 = 0.25$.

**Problema del desvanecimiento de gradientes (*vanishing gradients*).** A pesar de sus propiedades elegantes, la sigmoide sufre un problema importante cuando se utiliza en redes profundas: para valores de $|z|$ grandes, la derivada $\sigma'(z)$ tiende a cero. Esto significa que durante la retropropagación, los gradientes que se multiplican a través de muchas capas se vuelven exponencialmente pequeños, ralentizando o deteniendo completamente el aprendizaje en las capas más profundas. Dado que $\sigma'(z) \leq 0.25$ para todo $z$, al pasar por $L$ capas con activación sigmoide, el gradiente se escala por un factor del orden de $(0.25)^L$, que decrece rápidamente.

### 1.4.3 Tangente hiperbólica (tanh)

La tangente hiperbólica es otra función de activación suave y diferenciable, definida como:

$$\tanh(z) = \frac{e^z - e^{-z}}{e^z + e^{-z}}$$

Es posible demostrar que la tangente hiperbólica es, en realidad, una versión reescalada y desplazada de la sigmoide:

$$\tanh(z) = 2\sigma(2z) - 1$$

Esta relación puede verificarse directamente:

$$2\sigma(2z) - 1 = \frac{2}{1 + e^{-2z}} - 1 = \frac{2 - (1 + e^{-2z})}{1 + e^{-2z}} = \frac{1 - e^{-2z}}{1 + e^{-2z}}$$

Multiplicando numerador y denominador por $e^z$:

$$= \frac{e^z - e^{-z}}{e^z + e^{-z}} = \tanh(z) \quad \checkmark$$

Las propiedades principales de la tangente hiperbólica son:

- **Rango:** $(-1, 1)$. A diferencia de la sigmoide, la tanh está centrada en cero, lo que hace que sus salidas tengan media aproximadamente cero. Esta propiedad es beneficiosa para el entrenamiento, ya que las entradas a la siguiente capa no estarán sesgadas hacia valores positivos.
- **Simetría:** Es una función impar: $\tanh(-z) = -\tanh(z)$.
- **Derivada:** $\tanh'(z) = 1 - \tanh^2(z)$. En $z = 0$, $\tanh'(0) = 1$, lo cual es cuatro veces mayor que la derivada máxima de la sigmoide ($0.25$), lo que proporciona gradientes más fuertes.

A pesar de estas ventajas sobre la sigmoide, la tangente hiperbólica también sufre el problema de desvanecimiento de gradientes para valores grandes de $|z|$, ya que $\tanh'(z) \to 0$ cuando $|z| \to \infty$.

### 1.4.4 Unidad Lineal Rectificada (ReLU)

La función ReLU (*Rectified Linear Unit*), propuesta como función de activación para redes neuronales y popularizada a partir del trabajo de Nair y Hinton (2010) y del impacto práctico demostrado por Krizhevsky, Sutskever e Hinton en la arquitectura AlexNet (2012), representa un punto de inflexión en la historia del aprendizaje profundo:

$$f(z) = \text{ReLU}(z) = \max(0, z) = \begin{cases} z & \text{si } z > 0 \\ 0 & \text{si } z \leq 0 \end{cases}$$

Su derivada es:

$$f'(z) = \begin{cases} 1 & \text{si } z > 0 \\ 0 & \text{si } z < 0 \\ \text{indefinida} & \text{si } z = 0 \end{cases}$$

En la práctica, la derivada en $z = 0$ se define convencionalmente como 0 o 1.

Las ventajas de ReLU son significativas:

1. **Eficiencia computacional:** Su cómputo es extremadamente simple —solo una comparación y una asignación—, en contraste con las funciones exponenciales de la sigmoide y la tanh.
2. **Mitigación del desvanecimiento de gradientes:** Para $z > 0$, la derivada es exactamente 1, lo que permite que los gradientes fluyan sin atenuación a través de las capas de la red.
3. **Esparsidad:** ReLU produce exactamente cero para todas las entradas negativas, lo que genera representaciones esparsas (muchas neuronas con salida cero). Esta esparsidad ha demostrado ser beneficiosa para la generalización.

**El problema de las neuronas muertas (*dying ReLU*).** A pesar de sus ventajas, ReLU presenta un problema conocido: si durante el entrenamiento una neurona recibe consistentemente entradas negativas (es decir, $z < 0$), su gradiente será perpetuamente cero. Esto significa que los pesos de esa neurona nunca se actualizarán y la neurona quedará permanentemente "muerta" —produciendo siempre una salida de cero, independientemente de la entrada. Este fenómeno puede ocurrir si la tasa de aprendizaje es demasiado alta, causando que los pesos se actualicen de forma tan abrupta que la neurona se mueve a la región negativa y no puede regresar. En redes profundas con muchas neuronas ReLU, no es infrecuente que un porcentaje significativo de las neuronas (a veces hasta el 40% o más) estén "muertas" al final del entrenamiento.

### 1.4.5 Variantes de ReLU

Para abordar el problema de las neuronas muertas, se han propuesto diversas variantes de ReLU:

**Leaky ReLU (ReLU con fuga):** Introduce una pequeña pendiente $\alpha$ (típicamente $\alpha = 0.01$) para las entradas negativas:

$$f(z) = \begin{cases} z & \text{si } z > 0 \\ \alpha z & \text{si } z \leq 0 \end{cases} = \max(\alpha z, z)$$

De esta forma, la derivada para $z < 0$ es $\alpha \neq 0$, lo que evita que las neuronas mueran completamente. El hiperparámetro $\alpha$ controla la pendiente en la región negativa.

**Parametric ReLU (PReLU):** Es una generalización de Leaky ReLU en la que el parámetro $\alpha$ no se fija manualmente, sino que se aprende durante el entrenamiento como un parámetro más del modelo:

$$f(z) = \max(\alpha z, z), \quad \alpha \text{ aprendible}$$

**Exponential Linear Unit (ELU):** Propuesta por Clevert, Unterthiner y Hochreiter (2016), utiliza una función exponencial para la región negativa:

$$f(z) = \begin{cases} z & \text{si } z > 0 \\ \alpha(e^z - 1) & \text{si } z \leq 0 \end{cases}$$

donde $\alpha > 0$ es un hiperparámetro (comúnmente $\alpha = 1$). A diferencia de Leaky ReLU, la ELU se satura en $-\alpha$ para valores muy negativos, lo que proporciona robustez al ruido. Además, la ELU produce salidas con media más cercana a cero que ReLU, lo que puede acelerar el entrenamiento.

**GELU (Gaussian Error Linear Unit):** Propuesta por Hendrycks y Gimpel (2016), la GELU pondera la entrada por la probabilidad de que sea mayor que las demás entradas, bajo la suposición de una distribución normal:

$$\text{GELU}(z) = z \cdot \Phi(z) = z \cdot \frac{1}{2}\left[1 + \text{erf}\left(\frac{z}{\sqrt{2}}\right)\right]$$

donde $\Phi(z)$ es la función de distribución acumulada (CDF) de la distribución normal estándar y $\text{erf}$ es la función error. Una aproximación práctica frecuentemente utilizada es:

$$\text{GELU}(z) \approx 0.5 \, z \left[1 + \tanh\left(\sqrt{\frac{2}{\pi}}\left(z + 0.044715 \, z^3\right)\right)\right]$$

La GELU se ha convertido en la función de activación predominante en modelos de lenguaje basados en transformers, como BERT y GPT. A diferencia de ReLU, que aplica una "compuerta" determinista (pasa o no pasa), la GELU aplica una compuerta estocástica suave que depende del valor de la entrada, produciendo una transición gradual.

**Swish (SiLU):** Propuesta por Ramachandran, Zoph y Le (2017), y también conocida como SiLU (*Sigmoid Linear Unit*):

$$\text{Swish}(z) = z \cdot \sigma(\beta z) = \frac{z}{1 + e^{-\beta z}}$$

donde $\beta$ es un parámetro que controla la forma de la función. Cuando $\beta = 1$ (caso más común), se reduce a:

$$\text{Swish}(z) = \frac{z}{1 + e^{-z}}$$

La Swish es no monótona: para valores negativos cercanos a cero, la función puede tomar valores ligeramente negativos antes de saturarse a cero, lo que la diferencia fundamentalmente de ReLU. Se ha observado empíricamente que Swish iguala o supera a ReLU en una variedad de tareas, particularmente en redes profundas.

### 1.4.6 Función Softmax para clasificación multi-clase

Todas las funciones de activación discutidas hasta ahora operan elemento a elemento: cada neurona aplica la función de activación de manera independiente a su propia pre-activación. La función softmax, en cambio, opera sobre un **vector** completo de pre-activaciones y produce un vector de probabilidades. Se utiliza típicamente en la capa de salida de redes neuronales diseñadas para clasificación multi-clase.

Dado un vector de pre-activaciones $\mathbf{z} = [z_1, z_2, \ldots, z_K]^T$, donde $K$ es el número de clases, la función softmax se define como:

$$\text{softmax}(z_i) = \frac{e^{z_i}}{\sum_{j=1}^{K} e^{z_j}}, \quad \text{para } i = 1, 2, \ldots, K$$

Las propiedades de la softmax son:

1. **Positividad:** $\text{softmax}(z_i) > 0$ para todo $i$, ya que la función exponencial es siempre positiva.
2. **Normalización:** $\sum_{i=1}^{K} \text{softmax}(z_i) = 1$. Las salidas forman una distribución de probabilidad válida sobre las $K$ clases.
3. **Monotonía relativa:** Si $z_i > z_j$, entonces $\text{softmax}(z_i) > \text{softmax}(z_j)$. La clase con la mayor pre-activación tendrá la mayor probabilidad.
4. **Amplificación de diferencias:** La función exponencial amplifica las diferencias entre las pre-activaciones. Si una pre-activación es significativamente mayor que las demás, la probabilidad correspondiente se acercará a 1, mientras que las demás se acercarán a 0. Este efecto se puede controlar introduciendo un parámetro de temperatura $T$:

$$\text{softmax}(z_i; T) = \frac{e^{z_i / T}}{\sum_{j=1}^{K} e^{z_j / T}}$$

Con $T \to 0$, la softmax tiende a una función argmax determinista (one-hot); con $T \to \infty$, la distribución se acerca a la uniforme $1/K$.

**Estabilidad numérica.** En la implementación práctica, calcular $e^{z_i}$ directamente puede causar desbordamiento numérico (*overflow*) si $z_i$ es muy grande. Para evitar esto, se utiliza el truco de restar el valor máximo:

$$\text{softmax}(z_i) = \frac{e^{z_i - z_{\max}}}{\sum_{j=1}^{K} e^{z_j - z_{\max}}}, \quad \text{donde } z_{\max} = \max_j z_j$$

Esta modificación no altera el resultado matemático (las constantes se cancelan), pero garantiza que el mayor exponente sea $e^0 = 1$, previniendo el desbordamiento.

### 1.4.7 Descripción de figura: funciones de activación

**Figura 1.3:** *Gráficas comparativas de las principales funciones de activación utilizadas en redes neuronales. La figura se organiza en una cuadrícula de $3 \times 3$ subgráficas, cada una mostrando una función diferente junto con su derivada (en línea punteada). (a) Función escalón (Heaviside): una línea horizontal en $y=0$ para $z<0$ y una línea horizontal en $y=1$ para $z \geq 0$, con una discontinuidad de salto en $z=0$. (b) Sigmoide $\sigma(z) = 1/(1+e^{-z})$: una curva en forma de "S" suave que transita gradualmente de 0 a 1, con su derivada en forma de campana centrada en $z=0$ con un máximo de $0.25$. (c) Tangente hiperbólica $\tanh(z)$: similar a la sigmoide pero centrada en cero, transitando de $-1$ a $+1$, con su derivada en forma de campana con máximo en $1.0$ en $z=0$. (d) ReLU: una línea en $y=0$ para $z \leq 0$ y una línea con pendiente 1 para $z > 0$, formando un "codo" en el origen; su derivada es una función escalón (0 para $z<0$, 1 para $z>0$). (e) Leaky ReLU ($\alpha = 0.1$): similar a ReLU pero con una línea de pendiente suave $0.1$ para $z < 0$. (f) ELU ($\alpha = 1$): idéntica a ReLU para $z > 0$, pero con una curva exponencial suave que se satura en $-1$ para $z \ll 0$. (g) GELU: una curva suave similar a ReLU para $z > 0$ pero con una pequeña región negativa antes del origen, sin codo abrupto. (h) Swish ($\beta = 1$): similar a GELU, con una curva suave que presenta un mínimo negativo alrededor de $z \approx -1.28$ antes de saturarse a cero para $z \to -\infty$. (i) Softmax: se muestra un ejemplo con $K=3$ clases, graficando las tres probabilidades de salida como funciones de $z_1$ mientras se mantienen $z_2=0$ y $z_3=0$ fijos, mostrando cómo la probabilidad de la clase 1 crece sigmoidealmente mientras las otras decrecen simétricamente. Todos los ejes horizontales abarcan el rango $[-5, 5]$, y las funciones se dibujan en azul sólido con sus derivadas en rojo punteado.*

---

## 1.5 Aprendizaje y la regla de actualización de pesos

### 1.5.1 El concepto de aprendizaje en redes neuronales

En el contexto de las redes neuronales artificiales, **aprender** significa encontrar el conjunto de parámetros (pesos $\mathbf{w}$ y sesgos $b$) que minimiza una **función de pérdida** (*loss function*) $L$ que cuantifica la discrepancia entre las predicciones del modelo $\hat{y}$ y los valores verdaderos $y$ en un conjunto de datos de entrenamiento.

Formalmente, dado un conjunto de datos de entrenamiento $\mathcal{D} = \{(\mathbf{x}^{(1)}, y^{(1)}), (\mathbf{x}^{(2)}, y^{(2)}), \ldots, (\mathbf{x}^{(N)}, y^{(N)})\}$, donde $\mathbf{x}^{(k)} \in \mathbb{R}^n$ es el vector de entrada $k$-ésimo e $y^{(k)}$ es su etiqueta o valor objetivo correspondiente, el problema de aprendizaje se formula como un problema de **optimización**:

$$\min_{\mathbf{w}, b} \; L(\mathbf{w}, b) = \min_{\mathbf{w}, b} \; \frac{1}{N} \sum_{k=1}^{N} \ell\left(y^{(k)}, \hat{y}^{(k)}\right)$$

donde $\ell(y, \hat{y})$ es la función de pérdida evaluada en un solo ejemplo y $\hat{y}^{(k)} = f(\mathbf{w}^T \mathbf{x}^{(k)} + b)$ es la predicción del modelo para la entrada $\mathbf{x}^{(k)}$.

### 1.5.2 Descenso de gradiente: intuición geométrica

El **descenso de gradiente** (*gradient descent*) es el algoritmo fundamental para la optimización de redes neuronales. Su intuición geométrica es poderosa y sencilla: imaginemos la función de pérdida $L(\mathbf{w})$ como una superficie montañosa en un espacio de alta dimensión, donde cada eje corresponde a un peso de la red y la "altitud" representa el valor de la pérdida. El objetivo es encontrar el punto más bajo de esta superficie (el mínimo global, o al menos un buen mínimo local).

El gradiente de $L$ respecto a los pesos, denotado $\nabla_{\mathbf{w}} L$, es un vector que apunta en la **dirección de máximo crecimiento** de $L$. Matemáticamente:

$$\nabla_{\mathbf{w}} L = \left[\frac{\partial L}{\partial w_1}, \frac{\partial L}{\partial w_2}, \ldots, \frac{\partial L}{\partial w_n}\right]^T$$

Para descender por la superficie de la pérdida (es decir, reducir $L$), debemos movernos en la dirección **opuesta** al gradiente: $-\nabla_{\mathbf{w}} L$. Esta es la dirección de máximo decrecimiento local de la función de pérdida.

### 1.5.3 Tasa de aprendizaje y regla de actualización

La **tasa de aprendizaje** $\eta > 0$ (*learning rate*) es un hiperparámetro escalar que controla el tamaño del paso que damos en cada iteración del descenso de gradiente. La regla de actualización de pesos es:

$$w_i^{(t+1)} = w_i^{(t)} - \eta \frac{\partial L}{\partial w_i}$$

o en notación vectorial:

$$\mathbf{w}^{(t+1)} = \mathbf{w}^{(t)} - \eta \nabla_{\mathbf{w}} L$$

y de manera análoga para el sesgo:

$$b^{(t+1)} = b^{(t)} - \eta \frac{\partial L}{\partial b}$$

donde el superíndice $(t)$ indica la iteración actual y $(t+1)$ la siguiente.

La elección de la tasa de aprendizaje es crítica:

- **$\eta$ demasiado grande:** Los pasos de actualización son muy grandes, lo que puede causar que el algoritmo "salte" sobre el mínimo, oscile sin convergir o incluso diverja (la pérdida aumenta en lugar de disminuir).
- **$\eta$ demasiado pequeña:** Los pasos son muy pequeños, lo que hace que la convergencia sea extremadamente lenta. Además, el algoritmo tiene mayor riesgo de quedar atrapado en mínimos locales poco profundos o en puntos de silla (*saddle points*).
- **$\eta$ adecuada:** Los pasos son lo suficientemente grandes para avanzar con rapidez, pero lo suficientemente pequeños para no sobrepasar el mínimo.

En la práctica, los valores típicos iniciales de $\eta$ oscilan entre $10^{-4}$ y $10^{-1}$, dependiendo del problema, la arquitectura y el optimizador utilizado. Es frecuente emplear **programas de tasa de aprendizaje** (*learning rate schedules*) que reducen $\eta$ a medida que avanza el entrenamiento.

### 1.5.4 Funciones de pérdida

La elección de la función de pérdida $\ell(y, \hat{y})$ depende del tipo de problema:

**Error cuadrático medio (MSE, *Mean Squared Error*):*** Se utiliza principalmente en problemas de regresión, donde la salida es un valor continuo:

$$L_{\text{MSE}} = \frac{1}{N} \sum_{k=1}^{N} \left(y^{(k)} - \hat{y}^{(k)}\right)^2$$

La derivada de la pérdida MSE respecto a la predicción es:

$$\frac{\partial \ell}{\partial \hat{y}} = \frac{\partial}{\partial \hat{y}}\left(y - \hat{y}\right)^2 = -2(y - \hat{y})$$

El MSE penaliza cuadráticamente los errores grandes, lo que puede ser ventajoso (prioriza la corrección de errores grandes) o desventajoso (es sensible a valores atípicos u *outliers*).

**Entropía cruzada binaria (*Binary Cross-Entropy*):*** Se utiliza en problemas de clasificación binaria, donde $y \in \{0, 1\}$ y $\hat{y} = \sigma(z) \in (0, 1)$ representa la probabilidad estimada de que la entrada pertenezca a la clase 1:

$$L_{\text{BCE}} = -\frac{1}{N} \sum_{k=1}^{N} \left[y^{(k)} \log \hat{y}^{(k)} + (1 - y^{(k)}) \log(1 - \hat{y}^{(k)})\right]$$

La entropía cruzada tiene una interpretación profunda en teoría de la información: mide la divergencia entre la distribución verdadera $p = [y, 1-y]$ y la distribución estimada $q = [\hat{y}, 1-\hat{y}]$. Minimizar la entropía cruzada equivale a minimizar la divergencia de Kullback-Leibler $D_{\text{KL}}(p \| q)$, dado que la entropía de la distribución verdadera $H(p)$ es constante.

La derivada de la entropía cruzada binaria respecto a la pre-activación $z$ (cuando se usa activación sigmoide) tiene una forma particularmente elegante:

$$\frac{\partial L_{\text{BCE}}}{\partial z} = \hat{y} - y = \sigma(z) - y$$

Esta simplicidad es una de las razones por las que la combinación sigmoide + entropía cruzada es tan popular.

**Entropía cruzada categórica (*Categorical Cross-Entropy*):*** Generalización para clasificación multi-clase con $K$ clases, donde $y$ es un vector one-hot y $\hat{y}$ es la salida de la función softmax:

$$L_{\text{CCE}} = -\sum_{i=1}^{K} y_i \log \hat{y}_i$$

donde $y_i = 1$ solo para la clase correcta y $y_i = 0$ para las demás.

### 1.5.5 Ejemplo completo: entrenamiento de un perceptrón para la compuerta AND

Para solidificar la comprensión de los conceptos de aprendizaje, desarrollemos paso a paso el entrenamiento de un perceptrón para implementar la función lógica AND. Utilizaremos la regla de aprendizaje del perceptrón, que es un caso especial del descenso de gradiente para la función de activación escalón.

**Tabla de verdad de la compuerta AND:**

| $x_1$ | $x_2$ | $y = x_1 \text{ AND } x_2$ |
|:------:|:------:|:---------------------------:|
|   0    |   0    |              0              |
|   0    |   1    |              0              |
|   1    |   0    |              0              |
|   1    |   1    |              1              |

**Regla de actualización del perceptrón.** Para el perceptrón con activación escalón, la regla de actualización es:

$$w_i^{(t+1)} = w_i^{(t)} + \eta \left(y^{(k)} - \hat{y}^{(k)}\right) x_i^{(k)}$$

$$b^{(t+1)} = b^{(t)} + \eta \left(y^{(k)} - \hat{y}^{(k)}\right)$$

donde $y^{(k)}$ es la salida deseada para el ejemplo $k$, $\hat{y}^{(k)}$ es la salida predicha, y $\eta$ es la tasa de aprendizaje. Nótese que los pesos solo se actualizan cuando hay un error de clasificación ($y^{(k)} \neq \hat{y}^{(k)}$).

**Configuración inicial:**
- Tasa de aprendizaje: $\eta = 1$
- Pesos iniciales: $w_1 = 0$, $w_2 = 0$
- Sesgo inicial: $b = 0$

**Época 1** (una pasada completa por todos los datos de entrenamiento):

**Iteración 1** — Entrada: $(x_1, x_2) = (0, 0)$, Objetivo: $y = 0$

$$z = w_1 x_1 + w_2 x_2 + b = 0 \cdot 0 + 0 \cdot 0 + 0 = 0$$

$$\hat{y} = f(z) = f(0) = 1 \quad (\text{ya que } z \geq 0)$$

Error: $e = y - \hat{y} = 0 - 1 = -1 \neq 0 \Rightarrow$ actualizar pesos.

$$w_1 \leftarrow 0 + 1 \cdot (-1) \cdot 0 = 0$$

$$w_2 \leftarrow 0 + 1 \cdot (-1) \cdot 0 = 0$$

$$b \leftarrow 0 + 1 \cdot (-1) = -1$$

Estado actual: $w_1 = 0, \; w_2 = 0, \; b = -1$.

**Iteración 2** — Entrada: $(x_1, x_2) = (0, 1)$, Objetivo: $y = 0$

$$z = 0 \cdot 0 + 0 \cdot 1 + (-1) = -1$$

$$\hat{y} = f(-1) = 0 \quad (\text{ya que } z < 0)$$

Error: $e = 0 - 0 = 0 \Rightarrow$ no actualizar. ✓

Estado actual: $w_1 = 0, \; w_2 = 0, \; b = -1$.

**Iteración 3** — Entrada: $(x_1, x_2) = (1, 0)$, Objetivo: $y = 0$

$$z = 0 \cdot 1 + 0 \cdot 0 + (-1) = -1$$

$$\hat{y} = f(-1) = 0$$

Error: $e = 0 - 0 = 0 \Rightarrow$ no actualizar. ✓

Estado actual: $w_1 = 0, \; w_2 = 0, \; b = -1$.

**Iteración 4** — Entrada: $(x_1, x_2) = (1, 1)$, Objetivo: $y = 1$

$$z = 0 \cdot 1 + 0 \cdot 1 + (-1) = -1$$

$$\hat{y} = f(-1) = 0$$

Error: $e = 1 - 0 = 1 \neq 0 \Rightarrow$ actualizar pesos.

$$w_1 \leftarrow 0 + 1 \cdot 1 \cdot 1 = 1$$

$$w_2 \leftarrow 0 + 1 \cdot 1 \cdot 1 = 1$$

$$b \leftarrow -1 + 1 \cdot 1 = 0$$

Estado actual: $w_1 = 1, \; w_2 = 1, \; b = 0$.

**Fin de la Época 1.** Hubo errores, por lo que es necesario continuar el entrenamiento.

---

**Época 2:**

**Iteración 5** — Entrada: $(0, 0)$, Objetivo: $y = 0$

$$z = 1 \cdot 0 + 1 \cdot 0 + 0 = 0$$

$$\hat{y} = f(0) = 1$$

Error: $e = 0 - 1 = -1 \Rightarrow$ actualizar.

$$w_1 \leftarrow 1 + 1 \cdot (-1) \cdot 0 = 1$$

$$w_2 \leftarrow 1 + 1 \cdot (-1) \cdot 0 = 1$$

$$b \leftarrow 0 + 1 \cdot (-1) = -1$$

Estado actual: $w_1 = 1, \; w_2 = 1, \; b = -1$.

**Iteración 6** — Entrada: $(0, 1)$, Objetivo: $y = 0$

$$z = 1 \cdot 0 + 1 \cdot 1 + (-1) = 0$$

$$\hat{y} = f(0) = 1$$

Error: $e = 0 - 1 = -1 \Rightarrow$ actualizar.

$$w_1 \leftarrow 1 + 1 \cdot (-1) \cdot 0 = 1$$

$$w_2 \leftarrow 1 + 1 \cdot (-1) \cdot 1 = 0$$

$$b \leftarrow -1 + 1 \cdot (-1) = -2$$

Estado actual: $w_1 = 1, \; w_2 = 0, \; b = -2$.

**Iteración 7** — Entrada: $(1, 0)$, Objetivo: $y = 0$

$$z = 1 \cdot 1 + 0 \cdot 0 + (-2) = -1$$

$$\hat{y} = f(-1) = 0$$

Error: $e = 0 - 0 = 0 \Rightarrow$ no actualizar. ✓

Estado actual: $w_1 = 1, \; w_2 = 0, \; b = -2$.

**Iteración 8** — Entrada: $(1, 1)$, Objetivo: $y = 1$

$$z = 1 \cdot 1 + 0 \cdot 1 + (-2) = -1$$

$$\hat{y} = f(-1) = 0$$

Error: $e = 1 - 0 = 1 \Rightarrow$ actualizar.

$$w_1 \leftarrow 1 + 1 \cdot 1 \cdot 1 = 2$$

$$w_2 \leftarrow 0 + 1 \cdot 1 \cdot 1 = 1$$

$$b \leftarrow -2 + 1 \cdot 1 = -1$$

Estado actual: $w_1 = 2, \; w_2 = 1, \; b = -1$.

**Fin de la Época 2.** Hubo errores, continuar.

---

**Época 3:**

**Iteración 9** — Entrada: $(0, 0)$, Objetivo: $y = 0$

$$z = 2 \cdot 0 + 1 \cdot 0 + (-1) = -1$$

$$\hat{y} = f(-1) = 0$$

Error: $e = 0 - 0 = 0 \Rightarrow$ no actualizar. ✓

**Iteración 10** — Entrada: $(0, 1)$, Objetivo: $y = 0$

$$z = 2 \cdot 0 + 1 \cdot 1 + (-1) = 0$$

$$\hat{y} = f(0) = 1$$

Error: $e = 0 - 1 = -1 \Rightarrow$ actualizar.

$$w_1 \leftarrow 2 + 1 \cdot (-1) \cdot 0 = 2$$

$$w_2 \leftarrow 1 + 1 \cdot (-1) \cdot 1 = 0$$

$$b \leftarrow -1 + 1 \cdot (-1) = -2$$

Estado actual: $w_1 = 2, \; w_2 = 0, \; b = -2$.

**Iteración 11** — Entrada: $(1, 0)$, Objetivo: $y = 0$

$$z = 2 \cdot 1 + 0 \cdot 0 + (-2) = 0$$

$$\hat{y} = f(0) = 1$$

Error: $e = 0 - 1 = -1 \Rightarrow$ actualizar.

$$w_1 \leftarrow 2 + 1 \cdot (-1) \cdot 1 = 1$$

$$w_2 \leftarrow 0 + 1 \cdot (-1) \cdot 0 = 0$$

$$b \leftarrow -2 + 1 \cdot (-1) = -3$$

Estado actual: $w_1 = 1, \; w_2 = 0, \; b = -3$.

**Iteración 12** — Entrada: $(1, 1)$, Objetivo: $y = 1$

$$z = 1 \cdot 1 + 0 \cdot 1 + (-3) = -2$$

$$\hat{y} = f(-2) = 0$$

Error: $e = 1 - 0 = 1 \Rightarrow$ actualizar.

$$w_1 \leftarrow 1 + 1 \cdot 1 \cdot 1 = 2$$

$$w_2 \leftarrow 0 + 1 \cdot 1 \cdot 1 = 1$$

$$b \leftarrow -3 + 1 \cdot 1 = -2$$

Estado actual: $w_1 = 2, \; w_2 = 1, \; b = -2$.

**Fin de la Época 3.** Hubo errores, continuar.

---

**Época 4:**

**Iteración 13** — Entrada: $(0, 0)$, Objetivo: $y = 0$

$$z = 2 \cdot 0 + 1 \cdot 0 + (-2) = -2$$

$$\hat{y} = f(-2) = 0 \quad \checkmark$$

**Iteración 14** — Entrada: $(0, 1)$, Objetivo: $y = 0$

$$z = 2 \cdot 0 + 1 \cdot 1 + (-2) = -1$$

$$\hat{y} = f(-1) = 0 \quad \checkmark$$

**Iteración 15** — Entrada: $(1, 0)$, Objetivo: $y = 0$

$$z = 2 \cdot 1 + 1 \cdot 0 + (-2) = 0$$

$$\hat{y} = f(0) = 1$$

Error: $e = 0 - 1 = -1 \Rightarrow$ actualizar.

$$w_1 \leftarrow 2 + 1 \cdot (-1) \cdot 1 = 1$$

$$w_2 \leftarrow 1 + 1 \cdot (-1) \cdot 0 = 1$$

$$b \leftarrow -2 + 1 \cdot (-1) = -3$$

Estado actual: $w_1 = 1, \; w_2 = 1, \; b = -3$.

**Iteración 16** — Entrada: $(1, 1)$, Objetivo: $y = 1$

$$z = 1 \cdot 1 + 1 \cdot 1 + (-3) = -1$$

$$\hat{y} = f(-1) = 0$$

Error: $e = 1 - 0 = 1 \Rightarrow$ actualizar.

$$w_1 \leftarrow 1 + 1 \cdot 1 \cdot 1 = 2$$

$$w_2 \leftarrow 1 + 1 \cdot 1 \cdot 1 = 2$$

$$b \leftarrow -3 + 1 \cdot 1 = -2$$

Estado actual: $w_1 = 2, \; w_2 = 2, \; b = -2$.

**Fin de la Época 4.** Hubo errores, continuar.

---

**Época 5:**

**Iteración 17** — Entrada: $(0, 0)$, Objetivo: $y = 0$

$$z = 2 \cdot 0 + 2 \cdot 0 + (-2) = -2, \quad \hat{y} = 0 \quad \checkmark$$

**Iteración 18** — Entrada: $(0, 1)$, Objetivo: $y = 0$

$$z = 2 \cdot 0 + 2 \cdot 1 + (-2) = 0, \quad \hat{y} = f(0) = 1$$

Error: $e = -1 \Rightarrow$ actualizar.

$$w_1 \leftarrow 2, \quad w_2 \leftarrow 2 + (-1)(1) = 1, \quad b \leftarrow -2 + (-1) = -3$$

Estado: $w_1 = 2, \; w_2 = 1, \; b = -3$.

**Iteración 19** — Entrada: $(1, 0)$, Objetivo: $y = 0$

$$z = 2 \cdot 1 + 1 \cdot 0 + (-3) = -1, \quad \hat{y} = 0 \quad \checkmark$$

**Iteración 20** — Entrada: $(1, 1)$, Objetivo: $y = 1$

$$z = 2 \cdot 1 + 1 \cdot 1 + (-3) = 0, \quad \hat{y} = f(0) = 1 \quad \checkmark$$

**Fin de la Época 5.** Hubo un error. Continuar.

---

**Época 6:**

**Iteración 21** — $(0, 0)$, $y = 0$:

$$z = 2 \cdot 0 + 1 \cdot 0 - 3 = -3, \quad \hat{y} = 0 \quad \checkmark$$

**Iteración 22** — $(0, 1)$, $y = 0$:

$$z = 2 \cdot 0 + 1 \cdot 1 - 3 = -2, \quad \hat{y} = 0 \quad \checkmark$$

**Iteración 23** — $(1, 0)$, $y = 0$:

$$z = 2 \cdot 1 + 1 \cdot 0 - 3 = -1, \quad \hat{y} = 0 \quad \checkmark$$

**Iteración 24** — $(1, 1)$, $y = 1$:

$$z = 2 \cdot 1 + 1 \cdot 1 - 3 = 0, \quad \hat{y} = f(0) = 1 \quad \checkmark$$

**Fin de la Época 6.** ¡Ningún error! El perceptrón ha **convergido**.

---

**Resultado final:** Los parámetros aprendidos son $w_1 = 2$, $w_2 = 1$, $b = -3$. La frontera de decisión resultante es:

$$2x_1 + x_2 - 3 = 0 \quad \Longrightarrow \quad x_2 = -2x_1 + 3$$

Verifiquemos que esta solución clasifica correctamente todos los ejemplos:

| $(x_1, x_2)$ | $z = 2x_1 + x_2 - 3$ | $\hat{y}$ | $y$ | ¿Correcto? |
|:-------------:|:----------------------:|:---------:|:---:|:----------:|
| $(0, 0)$      | $-3$                   | $0$       | $0$ | ✓          |
| $(0, 1)$      | $-2$                   | $0$       | $0$ | ✓          |
| $(1, 0)$      | $-1$                   | $0$       | $0$ | ✓          |
| $(1, 1)$      | $0$                    | $1$       | $1$ | ✓          |

Este ejemplo ilustra varios aspectos fundamentales del aprendizaje del perceptrón:

1. **Convergencia garantizada:** El teorema de convergencia del perceptrón (Rosenblatt, 1962) establece que si los datos de entrenamiento son linealmente separables, el algoritmo del perceptrón convergerá en un número finito de iteraciones, sin importar la inicialización de los pesos. En nuestro ejemplo, la convergencia ocurrió después de 6 épocas (24 iteraciones individuales).

2. **Sensibilidad al orden de presentación:** El número de épocas necesarias para converger depende del orden en que se presentan los ejemplos y de la inicialización de los pesos. Un orden diferente o una inicialización diferente podrían llevar a una convergencia más rápida o más lenta.

3. **La solución no es única:** Diferentes inicializaciones y órdenes de presentación conducen a diferentes soluciones finales ($w_1 = 2, w_2 = 1, b = -3$ no es la única solución válida). Por ejemplo, $w_1 = 1, w_2 = 1, b = -1.5$ también clasifica correctamente todos los ejemplos de AND.

4. **Relación con la geometría:** El punto $(1,1)$ yace exactamente sobre la frontera de decisión ($z = 0$), lo que significa que el perceptrón clasifica este punto como 1 con margen cero. En la práctica, se prefieren soluciones con un margen más amplio, lo que motiva el uso de métodos como las máquinas de vectores de soporte (SVM) y técnicas de regularización.

### 1.5.6 Resumen y conexión con las secciones posteriores

En esta sección hemos establecido los cimientos sobre los cuales se construirá todo el tutorial. Los conceptos clave introducidos son:

- La **neurona artificial** como unidad computacional que calcula $y = f(\mathbf{w}^T \mathbf{x} + b)$.
- Las **funciones de activación** que introducen no linealidad, desde la función escalón hasta las modernas GELU y Swish.
- El **descenso de gradiente** como mecanismo de aprendizaje, que ajusta iterativamente los parámetros para minimizar una función de pérdida.
- Las **funciones de pérdida** (MSE, entropía cruzada) que cuantifican la discrepancia entre predicciones y valores verdaderos.

En la siguiente sección, extenderemos estos conceptos al **perceptrón multicapa** (*Multi-Layer Perceptron*, MLP), donde múltiples neuronas se organizan en capas sucesivas. Introduciremos el algoritmo de **retropropagación** (*backpropagation*), que permite calcular eficientemente los gradientes en redes de múltiples capas mediante la regla de la cadena del cálculo diferencial. Este paso es esencial para el entrenamiento de las arquitecturas profundas que sustentan los sistemas de comunicación semántica modernos, incluyendo los autoencoders que implementan la codificación conjunta de fuente y canal.

---

*Fin de la Sección 1.*
