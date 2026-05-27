# 4. Redes Neuronales Recurrentes (RNN) y LSTM

En las secciones anteriores de este tutorial hemos estudiado los perceptrones multicapa (MLP) y las redes neuronales convolucionales (CNN), dos arquitecturas fundamentales del aprendizaje profundo que han demostrado un rendimiento sobresaliente en tareas de clasificación, regresión y procesamiento de señales e imágenes. Sin embargo, estas arquitecturas presentan una limitación fundamental cuando se enfrentan a datos de naturaleza secuencial: carecen de un mecanismo intrínseco para capturar dependencias temporales. En el contexto de las comunicaciones semánticas, la información que se transmite frecuentemente adopta la forma de secuencias —texto, voz, series temporales de señales de canal, tramas de bits correlacionadas en el tiempo— lo que exige arquitecturas capaces de modelar la estructura temporal inherente a estos datos. Las redes neuronales recurrentes (RNN, *Recurrent Neural Networks*) y sus variantes avanzadas, particularmente las redes de memoria a largo-corto plazo (LSTM, *Long Short-Term Memory*), fueron diseñadas precisamente para abordar este desafío.

Esta sección presenta un tratamiento riguroso y pedagógico de las RNN, LSTM y sus variantes, comenzando desde la motivación fundamental, pasando por la formulación matemática completa, e incluyendo ejemplos numéricos detallados y una implementación práctica en PyTorch. Comprender estas arquitecturas es esencial no solo por su relevancia histórica, sino porque constituyen los cimientos sobre los cuales se han construido los sistemas modernos de comunicación semántica basados en codificación conjunta fuente-canal (*Joint Source-Channel Coding*, JSCC) para datos secuenciales.

---

## 4.1 Motivación: procesamiento de secuencias

### 4.1.1 Por qué los MLP y las CNN son insuficientes para datos secuenciales

Consideremos la tarea de predecir la siguiente palabra en una oración, estimar el estado futuro de un canal de comunicaciones inalámbricas, o decodificar una secuencia de símbolos transmitidos a través de un canal con memoria. En todos estos casos, el dato en el instante $t$ depende no solo de la entrada actual, sino de las entradas en instantes anteriores $t-1, t-2, \ldots, t-k$. Esta dependencia temporal es una característica fundamental de los datos secuenciales.

Un MLP estándar procesa cada entrada de forma independiente. Si deseamos que un MLP procese una secuencia de longitud $T$, podemos concatenar todos los elementos de la secuencia en un único vector de entrada $\mathbf{x} = [\mathbf{x}_1, \mathbf{x}_2, \ldots, \mathbf{x}_T]$. Sin embargo, este enfoque presenta múltiples problemas graves:

1. **Longitud fija de entrada**: El MLP requiere que el vector de entrada tenga una dimensión fija, lo que impide procesar secuencias de longitud variable sin técnicas de relleno (*padding*) o truncamiento que introducen artefactos.

2. **Explosión de parámetros**: Para una secuencia de longitud $T$ donde cada elemento tiene dimensión $d$, el vector de entrada tendría dimensión $Td$. Si la primera capa oculta tiene $H$ neuronas, la matriz de pesos $\mathbf{W}^{(1)} \in \mathbb{R}^{H \times Td}$ crece linealmente con la longitud de la secuencia, lo que resulta computacionalmente prohibitivo para secuencias largas.

3. **Ausencia de compartición de parámetros temporal**: En un MLP, los pesos que procesan la entrada en el instante $t=1$ son completamente distintos de los que procesan la entrada en $t=2$. Esto significa que el modelo no puede generalizar un patrón aprendido en una posición temporal a otra posición. Si el modelo aprende que la secuencia de símbolos "01" en la posición $t=5$ tiene cierto significado semántico, no puede transferir automáticamente ese conocimiento cuando la misma secuencia aparece en la posición $t=100$.

4. **No captura el orden**: Un MLP trata la concatenación $[\mathbf{x}_1, \mathbf{x}_2, \mathbf{x}_3]$ de manera fundamentalmente diferente a $[\mathbf{x}_3, \mathbf{x}_1, \mathbf{x}_2]$ solo porque los pesos son diferentes en cada posición, no porque tenga un mecanismo explícito para comprender la noción de orden o causalidad temporal.

Las CNN, por su parte, ofrecen una mejora parcial gracias a la compartición de parámetros a través de filtros convolucionales y la capacidad de capturar patrones locales. Una CNN 1D puede aplicar filtros a lo largo de la dimensión temporal, capturando dependencias dentro de una ventana receptiva local. Sin embargo, las CNN también presentan limitaciones significativas para el procesamiento secuencial:

- **Campo receptivo limitado**: Un filtro de tamaño $k$ solo puede capturar dependencias dentro de una ventana de $k$ pasos temporales. Para capturar dependencias a largo plazo, se requieren múltiples capas apiladas o filtros dilatados (*dilated convolutions*), lo que complica la arquitectura.

- **No mantienen estado**: Las CNN procesan toda la secuencia de una vez, sin mantener un estado interno que evolucione a medida que se procesan los elementos secuencialmente. Esto las hace menos naturales para tareas donde la predicción en el instante $t$ depende críticamente de toda la historia previa.

- **Causalidad**: Las CNN estándar aplican filtros que abarcan posiciones futuras y pasadas simultáneamente. Para aplicaciones causales (donde solo se dispone de información pasada), se requieren convoluciones causales (*causal convolutions*), que restringen el campo receptivo y complican el diseño.

### 4.1.2 Datos donde el orden importa

Los datos secuenciales son ubicuos tanto en las telecomunicaciones como en la inteligencia artificial en general. Algunos ejemplos representativos incluyen:

**Series temporales de canal**: En un sistema de comunicaciones inalámbricas, la respuesta del canal $h(t)$ varía en el tiempo debido al movimiento relativo entre transmisor y receptor, la dispersión por múltiples trayectos (*multipath*) y las variaciones del entorno. Predecir el estado futuro del canal a partir de sus valores pasados es un problema inherentemente secuencial. Los coeficientes de desvanecimiento (*fading*) en un canal Rayleigh exhiben correlación temporal que puede ser explotada por un modelo recurrente para mejorar la estimación y predicción de canal.

**Texto y lenguaje natural**: En comunicaciones semánticas, el transmisor puede necesar codificar texto en una representación semántica compacta para su transmisión. La comprensión del texto requiere modelar dependencias a larga distancia: en la oración "El ingeniero que diseñó el sistema de antenas MIMO para la estación base *terminó* el proyecto", el verbo "terminó" depende del sujeto "El ingeniero" a pesar de la distancia de múltiples palabras.

**Señales de voz y audio**: La señal de voz es intrínsecamente temporal, donde cada muestra depende de las anteriores. Los fonemas, las palabras y las oraciones se desarrollan a lo largo del tiempo, y su interpretación correcta requiere considerar el contexto temporal completo.

**Secuencias de símbolos codificados**: En sistemas de codificación de canal, las secuencias de bits codificadas tienen estructura temporal introducida por el codificador. Los códigos convolucionales, por ejemplo, producen símbolos de salida que dependen de los bits de entrada actuales y de un número finito de bits anteriores, almacenados en registros de desplazamiento. Un decodificador basado en redes neuronales recurrentes puede aprender a explotar esta estructura temporal.

### 4.1.3 El concepto de memoria en redes neuronales

La idea central que motiva las redes recurrentes es dotar a la red neuronal de **memoria**: la capacidad de mantener y actualizar un estado interno que resuma la información relevante de las entradas procesadas hasta el momento. Este concepto se puede formalizar de la siguiente manera.

Definimos una función de transición de estado $\phi$ que, dado el estado actual $\mathbf{h}_{t-1}$ y una nueva entrada $\mathbf{x}_t$, produce un nuevo estado $\mathbf{h}_t$:

$$\mathbf{h}_t = \phi(\mathbf{h}_{t-1}, \mathbf{x}_t)$$

y una función de salida $\psi$ que produce la salida $\mathbf{y}_t$ a partir del estado actual:

$$\mathbf{y}_t = \psi(\mathbf{h}_t)$$

El estado oculto $\mathbf{h}_t \in \mathbb{R}^{d_h}$ actúa como una memoria comprimida de toda la secuencia procesada hasta el instante $t$. Idealmente, $\mathbf{h}_t$ debería contener toda la información de $\mathbf{x}_1, \mathbf{x}_2, \ldots, \mathbf{x}_t$ que sea relevante para la tarea en cuestión.

Esta formulación tiene una analogía directa con los sistemas dinámicos en teoría de control y con los modelos ocultos de Markov (*Hidden Markov Models*, HMM) ampliamente utilizados en telecomunicaciones. La diferencia fundamental es que, en una RNN, las funciones $\phi$ y $\psi$ son parametrizadas por redes neuronales cuyos parámetros se aprenden a partir de los datos, en lugar de ser especificadas manualmente o estimadas mediante algoritmos como Baum-Welch.

La capacidad de mantener memoria es lo que distingue a las redes recurrentes de las redes *feedforward*. Mientras que un MLP implementa una función estática $\mathbf{y} = f(\mathbf{x})$ sin estado interno, una RNN implementa un sistema dinámico donde la salida depende tanto de la entrada actual como del historial acumulado en el estado oculto. Esta propiedad es fundamental para las comunicaciones semánticas, donde el significado de un símbolo o una palabra frecuentemente depende del contexto proporcionado por los elementos anteriores de la secuencia.

---

## 4.2 La Red Neuronal Recurrente (RNN) básica

### 4.2.1 Arquitectura: el estado oculto que se retroalimenta

La red neuronal recurrente (RNN) básica, también conocida como RNN de Elman (en honor a Jeffrey Elman, quien popularizó esta arquitectura en 1990), implementa las funciones de transición y salida mediante transformaciones afines seguidas de funciones de activación no lineales. La característica definitoria de la RNN es la presencia de una **conexión recurrente**: la salida de la capa oculta en el instante $t-1$ se retroalimenta como entrada adicional en el instante $t$.

La arquitectura de una celda RNN básica consta de tres componentes principales:

1. **Capa de entrada**: Recibe el vector de entrada $\mathbf{x}_t \in \mathbb{R}^{d_x}$ en cada paso temporal $t$.
2. **Capa oculta recurrente**: Mantiene un vector de estado oculto $\mathbf{h}_t \in \mathbb{R}^{d_h}$ que se actualiza en cada paso temporal incorporando tanto la entrada actual como el estado oculto anterior.
3. **Capa de salida**: Produce un vector de salida $\mathbf{y}_t \in \mathbb{R}^{d_y}$ a partir del estado oculto actual.

La conexión recurrente $\mathbf{h}_{t-1} \to \mathbf{h}_t$ es la que confiere a la red su capacidad de memoria. Sin esta conexión, la RNN se reduciría a un MLP aplicado independientemente en cada paso temporal.

### 4.2.2 Formulación matemática

La dinámica de una RNN básica se describe mediante las siguientes ecuaciones:

**Estado oculto:**

$$\mathbf{h}_t = f\!\left(\mathbf{W}_{hh}\mathbf{h}_{t-1} + \mathbf{W}_{xh}\mathbf{x}_t + \mathbf{b}_h\right)$$

**Salida:**

$$\mathbf{y}_t = g\!\left(\mathbf{W}_{hy}\mathbf{h}_t + \mathbf{b}_y\right)$$

donde:

- $\mathbf{x}_t \in \mathbb{R}^{d_x}$ es el vector de entrada en el paso temporal $t$.
- $\mathbf{h}_t \in \mathbb{R}^{d_h}$ es el vector de estado oculto en el paso temporal $t$.
- $\mathbf{h}_{t-1} \in \mathbb{R}^{d_h}$ es el vector de estado oculto en el paso temporal anterior $t-1$.
- $\mathbf{y}_t \in \mathbb{R}^{d_y}$ es el vector de salida en el paso temporal $t$.
- $\mathbf{W}_{xh} \in \mathbb{R}^{d_h \times d_x}$ es la matriz de pesos de entrada a oculta. Transforma la entrada $\mathbf{x}_t$ al espacio del estado oculto.
- $\mathbf{W}_{hh} \in \mathbb{R}^{d_h \times d_h}$ es la matriz de pesos de oculta a oculta, también llamada **matriz de recurrencia**. Es la responsable de la retroalimentación temporal y constituye el elemento diferenciador de la RNN respecto a una red *feedforward*.
- $\mathbf{W}_{hy} \in \mathbb{R}^{d_y \times d_h}$ es la matriz de pesos de oculta a salida.
- $\mathbf{b}_h \in \mathbb{R}^{d_h}$ es el vector de sesgo de la capa oculta.
- $\mathbf{b}_y \in \mathbb{R}^{d_y}$ es el vector de sesgo de la capa de salida.
- $f(\cdot)$ es la función de activación de la capa oculta, típicamente $\tanh$ o ReLU.
- $g(\cdot)$ es la función de activación de la capa de salida, que depende de la tarea (softmax para clasificación, lineal para regresión, sigmoide para probabilidades).

Es crucial observar que las matrices de pesos $\mathbf{W}_{xh}$, $\mathbf{W}_{hh}$ y $\mathbf{W}_{hy}$ son **compartidas a lo largo de todos los pasos temporales**. Esto significa que la misma transformación se aplica en cada instante $t$, independientemente de la longitud de la secuencia. Esta compartición de parámetros tiene dos consecuencias importantes:

1. **Eficiencia paramétrica**: El número total de parámetros entrenables de la RNN es independiente de la longitud de la secuencia. Específicamente, el número de parámetros es $d_h \times d_x + d_h \times d_h + d_h + d_y \times d_h + d_y = d_h(d_x + d_h + 1) + d_y(d_h + 1)$, que depende únicamente de las dimensiones de entrada, oculta y salida, no de $T$.

2. **Generalización temporal**: Un patrón aprendido en una posición temporal puede aplicarse automáticamente en cualquier otra posición, de manera análoga a como los filtros convolucionales generalizan a través del espacio.

El estado oculto $\mathbf{h}_t$ se inicializa típicamente como el vector cero $\mathbf{h}_0 = \mathbf{0}$, aunque en algunas aplicaciones puede inicializarse con un vector aprendido o proporcionado por otra red.

Analicemos con mayor detalle la ecuación del estado oculto. El argumento de la función de activación es:

$$\mathbf{a}_t = \mathbf{W}_{hh}\mathbf{h}_{t-1} + \mathbf{W}_{xh}\mathbf{x}_t + \mathbf{b}_h$$

Este vector $\mathbf{a}_t \in \mathbb{R}^{d_h}$, llamado **preactivación**, es la suma de tres componentes:

- $\mathbf{W}_{hh}\mathbf{h}_{t-1}$: la contribución del estado oculto anterior, que codifica la "memoria" de la secuencia procesada hasta $t-1$.
- $\mathbf{W}_{xh}\mathbf{x}_t$: la contribución de la entrada actual, que aporta información nueva.
- $\mathbf{b}_h$: el sesgo, que permite desplazar la preactivación independientemente de las entradas.

La función de activación $f$ aplica una transformación no lineal a $\mathbf{a}_t$ para obtener $\mathbf{h}_t = f(\mathbf{a}_t)$. La elección de $f = \tanh$ es particularmente común en las RNN porque produce valores en el rango $(-1, 1)$, lo que ayuda a mantener los valores del estado oculto acotados a lo largo de múltiples pasos temporales. Si se utilizara una activación sin saturación como ReLU, los valores del estado oculto podrían crecer sin límite a lo largo de la secuencia.

Una forma alternativa y compacta de escribir las ecuaciones de la RNN es concatenar $\mathbf{h}_{t-1}$ y $\mathbf{x}_t$ en un único vector y utilizar una sola matriz de pesos. Definimos:

$$\mathbf{W} = [\mathbf{W}_{hh} \mid \mathbf{W}_{xh}] \in \mathbb{R}^{d_h \times (d_h + d_x)}$$

y el vector concatenado:

$$[\mathbf{h}_{t-1}, \mathbf{x}_t] \in \mathbb{R}^{d_h + d_x}$$

Entonces la ecuación del estado oculto se puede reescribir como:

$$\mathbf{h}_t = f\!\left(\mathbf{W}[\mathbf{h}_{t-1}, \mathbf{x}_t] + \mathbf{b}_h\right)$$

Esta notación concatenada es la que se utiliza con mayor frecuencia en la literatura moderna y en las implementaciones de software como PyTorch y TensorFlow.

### 4.2.3 Despliegue de la RNN en el tiempo

Para comprender mejor cómo fluye la información a través de una RNN, resulta útil "desplegar" (*unroll*) la red en el tiempo. El despliegue consiste en representar explícitamente la RNN como una red *feedforward* profunda donde cada capa corresponde a un paso temporal.

Dado una secuencia de entrada $(\mathbf{x}_1, \mathbf{x}_2, \ldots, \mathbf{x}_T)$, el despliegue produce las siguientes ecuaciones:

$$\mathbf{h}_1 = f(\mathbf{W}_{hh}\mathbf{h}_0 + \mathbf{W}_{xh}\mathbf{x}_1 + \mathbf{b}_h)$$
$$\mathbf{h}_2 = f(\mathbf{W}_{hh}\mathbf{h}_1 + \mathbf{W}_{xh}\mathbf{x}_2 + \mathbf{b}_h)$$
$$\mathbf{h}_3 = f(\mathbf{W}_{hh}\mathbf{h}_2 + \mathbf{W}_{xh}\mathbf{x}_3 + \mathbf{b}_h)$$
$$\vdots$$
$$\mathbf{h}_T = f(\mathbf{W}_{hh}\mathbf{h}_{T-1} + \mathbf{W}_{xh}\mathbf{x}_T + \mathbf{b}_h)$$

Y las salidas correspondientes:

$$\mathbf{y}_t = g(\mathbf{W}_{hy}\mathbf{h}_t + \mathbf{b}_y), \quad t = 1, 2, \ldots, T$$

**Figura 4.1:** *Diagrama de una celda RNN y su versión desplegada en el tiempo. A la izquierda se muestra la representación compacta de una celda RNN con la conexión recurrente indicada por una flecha circular. La celda recibe la entrada $\mathbf{x}_t$ y el estado oculto anterior $\mathbf{h}_{t-1}$, produce el nuevo estado oculto $\mathbf{h}_t$ y la salida $\mathbf{y}_t$. A la derecha se muestra la misma red desplegada a lo largo de cuatro pasos temporales ($t=1, 2, 3, 4$). Cada copia de la celda comparte los mismos parámetros $\mathbf{W}_{xh}$, $\mathbf{W}_{hh}$, $\mathbf{W}_{hy}$, $\mathbf{b}_h$ y $\mathbf{b}_y$. Las entradas $\mathbf{x}_1, \mathbf{x}_2, \mathbf{x}_3, \mathbf{x}_4$ alimentan a la red desde abajo, los estados ocultos $\mathbf{h}_0 \to \mathbf{h}_1 \to \mathbf{h}_2 \to \mathbf{h}_3 \to \mathbf{h}_4$ fluyen horizontalmente de izquierda a derecha conectando las celdas, y las salidas $\mathbf{y}_1, \mathbf{y}_2, \mathbf{y}_3, \mathbf{y}_4$ se producen en la parte superior. El estado inicial $\mathbf{h}_0$ se inicializa típicamente como el vector cero.*

La vista desplegada revela que una RNN procesando una secuencia de longitud $T$ es equivalente a una red *feedforward* con $T$ capas, donde cada capa comparte los mismos pesos. Esta equivalencia es fundamental para el entrenamiento, ya que permite aplicar el algoritmo de retropropagación estándar a la red desplegada.

Es importante notar que existen diferentes configuraciones de entrada-salida para las RNN, dependiendo de la tarea:

- **Muchos a muchos** (*many-to-many*): Se produce una salida en cada paso temporal. Ejemplo: traducción automática, decodificación símbolo por símbolo.
- **Muchos a uno** (*many-to-one*): Se procesa toda la secuencia y se produce una única salida al final ($\mathbf{y}_T$). Ejemplo: clasificación de sentimiento, detección de tipo de modulación.
- **Uno a muchos** (*one-to-many*): Se proporciona una única entrada y se genera una secuencia de salida. Ejemplo: generación de texto a partir de un vector de contexto.

### 4.2.4 Retropropagación a través del tiempo (BPTT)

El entrenamiento de una RNN se realiza mediante el algoritmo de **retropropagación a través del tiempo** (BPTT, *Backpropagation Through Time*), que es simplemente la aplicación del algoritmo de retropropagación estándar a la RNN desplegada en el tiempo.

Supongamos que la función de pérdida total para una secuencia de longitud $T$ es la suma de las pérdidas en cada paso temporal:

$$\mathcal{L} = \sum_{t=1}^{T} \mathcal{L}_t(\mathbf{y}_t, \hat{\mathbf{y}}_t)$$

donde $\hat{\mathbf{y}}_t$ es la etiqueta verdadera en el paso $t$ y $\mathcal{L}_t$ es la función de pérdida en ese paso (por ejemplo, entropía cruzada para clasificación o error cuadrático medio para regresión).

Para actualizar los parámetros de la red, necesitamos calcular los gradientes de $\mathcal{L}$ con respecto a cada parámetro. Consideremos el gradiente con respecto a la matriz de recurrencia $\mathbf{W}_{hh}$. Dado que $\mathbf{W}_{hh}$ se utiliza en todos los pasos temporales, su gradiente total es la suma de las contribuciones de cada paso:

$$\frac{\partial \mathcal{L}}{\partial \mathbf{W}_{hh}} = \sum_{t=1}^{T} \frac{\partial \mathcal{L}_t}{\partial \mathbf{W}_{hh}}$$

Para calcular $\frac{\partial \mathcal{L}_t}{\partial \mathbf{W}_{hh}}$, debemos aplicar la regla de la cadena a través de todos los pasos temporales desde $t$ hasta $1$. La pérdida $\mathcal{L}_t$ depende de $\mathbf{y}_t$, que depende de $\mathbf{h}_t$, que a su vez depende de $\mathbf{h}_{t-1}$, y así sucesivamente hasta $\mathbf{h}_1$. Por lo tanto:

$$\frac{\partial \mathcal{L}_t}{\partial \mathbf{W}_{hh}} = \sum_{k=1}^{t} \frac{\partial \mathcal{L}_t}{\partial \mathbf{y}_t} \frac{\partial \mathbf{y}_t}{\partial \mathbf{h}_t} \left(\prod_{j=k+1}^{t} \frac{\partial \mathbf{h}_j}{\partial \mathbf{h}_{j-1}}\right) \frac{\partial \mathbf{h}_k}{\partial \mathbf{W}_{hh}}$$

El término $\frac{\partial \mathbf{h}_j}{\partial \mathbf{h}_{j-1}}$ es la Jacobiana de la transición de estado, que para la RNN básica con activación $f$ es:

$$\frac{\partial \mathbf{h}_j}{\partial \mathbf{h}_{j-1}} = \text{diag}\!\left(f'(\mathbf{a}_j)\right) \cdot \mathbf{W}_{hh}$$

donde $\mathbf{a}_j = \mathbf{W}_{hh}\mathbf{h}_{j-1} + \mathbf{W}_{xh}\mathbf{x}_j + \mathbf{b}_h$ y $\text{diag}(f'(\mathbf{a}_j))$ es la matriz diagonal con las derivadas de la función de activación evaluadas en las preactivaciones.

### 4.2.5 El problema del gradiente desvaneciente

El producto de Jacobianas que aparece en la expresión del gradiente es la fuente de uno de los problemas más fundamentales del entrenamiento de RNN: el **problema del gradiente desvaneciente** (*vanishing gradient problem*), identificado formalmente por Hochreiter (1991) y analizado en profundidad por Bengio, Simard y Frasconi (1994).

Consideremos el producto:

$$\prod_{j=k+1}^{t} \frac{\partial \mathbf{h}_j}{\partial \mathbf{h}_{j-1}} = \prod_{j=k+1}^{t} \text{diag}\!\left(f'(\mathbf{a}_j)\right) \cdot \mathbf{W}_{hh}$$

Para analizar el comportamiento de este producto, examinemos su norma. Utilizando la propiedad de submultiplicatividad de la norma matricial:

$$\left\|\prod_{j=k+1}^{t} \frac{\partial \mathbf{h}_j}{\partial \mathbf{h}_{j-1}}\right\| \leq \prod_{j=k+1}^{t} \left\|\text{diag}\!\left(f'(\mathbf{a}_j)\right)\right\| \cdot \left\|\mathbf{W}_{hh}\right\|$$

Si utilizamos la función de activación $\tanh$, su derivada satisface $0 < f'(a) = 1 - \tanh^2(a) \leq 1$ para todo $a$. Sea $\gamma = \max_j \|f'(\mathbf{a}_j)\|_\infty \leq 1$ y $\lambda_{\max}$ el mayor valor singular de $\mathbf{W}_{hh}$. Entonces:

$$\left\|\prod_{j=k+1}^{t} \frac{\partial \mathbf{h}_j}{\partial \mathbf{h}_{j-1}}\right\| \leq (\gamma \cdot \lambda_{\max})^{t-k}$$

Este resultado tiene consecuencias dramáticas:

- Si $\gamma \cdot \lambda_{\max} < 1$: El producto decrece exponencialmente con la distancia temporal $(t-k)$. Para dependencias a largo plazo donde $t - k$ es grande, el gradiente se vuelve exponencialmente pequeño — **se desvanece**. Esto significa que la red no puede aprender dependencias temporales a largo plazo porque el gradiente de la pérdida con respecto a las entradas antiguas es esencialmente cero.

- Si $\gamma \cdot \lambda_{\max} > 1$: El producto crece exponencialmente — **el gradiente explota**. Los gradientes se vuelven enormes, causando actualizaciones de parámetros inestables y divergencia del entrenamiento. Este caso es técnicamente más fácil de manejar (mediante *gradient clipping*), pero igualmente problemático.

- Si $\gamma \cdot \lambda_{\max} \approx 1$: El gradiente se mantiene estable, pero este régimen es difícil de mantener en la práctica.

Para ilustrar numéricamente la gravedad del problema, supongamos $\gamma \cdot \lambda_{\max} = 0.9$ y consideremos una secuencia de longitud $T = 100$. El gradiente de una dependencia que abarque 50 pasos temporales se atenuaría por un factor de $0.9^{50} \approx 0.0052$, y para 100 pasos: $0.9^{100} \approx 2.66 \times 10^{-5}$. En la práctica, con valores de $\gamma$ menores (la derivada de $\tanh$ es frecuentemente mucho menor que 1 para preactivaciones grandes), la atenuación puede ser aún más severa.

Este problema impone una **barrera fundamental** a las RNN básicas: en la práctica, solo pueden aprender dependencias temporales que abarquen unas pocas decenas de pasos temporales. Para secuencias más largas, la información de los pasos iniciales se pierde irrecuperablemente durante la retropropagación. Esta limitación motivó directamente el desarrollo de las redes LSTM, que abordaremos en la siguiente subsección.

La técnica de **recorte de gradientes** (*gradient clipping*), propuesta por Pascanu, Mikolov y Bengio (2013), mitiga parcialmente el problema de la explosión de gradientes al limitar la norma del vector de gradientes:

$$\text{Si } \|\nabla\mathcal{L}\| > \theta, \quad \nabla\mathcal{L} \leftarrow \frac{\theta}{\|\nabla\mathcal{L}\|} \nabla\mathcal{L}$$

donde $\theta$ es un umbral predefinido. Sin embargo, el recorte de gradientes no resuelve el problema del desvanecimiento, que requiere cambios arquitectónicos fundamentales.

---

## 4.3 Long Short-Term Memory (LSTM)

### 4.3.1 Motivación: resolver el problema del gradiente desvaneciente

La red de **memoria a largo-corto plazo** (LSTM, *Long Short-Term Memory*) fue propuesta por Hochreiter y Schmidhuber en 1997 como una solución arquitectónica al problema del gradiente desvaneciente. La idea fundamental de la LSTM es introducir un **camino de gradiente directo** a través del tiempo, de manera que los gradientes puedan fluir a lo largo de muchos pasos temporales sin atenuarse exponencialmente.

La innovación clave de la LSTM es la introducción del **estado de celda** (*cell state*) $\mathbf{C}_t$, un vector que actúa como una "cinta transportadora" de información a lo largo del tiempo. El estado de celda se actualiza mediante operaciones aditivas y multiplicativas controladas por **puertas** (*gates*) que aprenden a regular el flujo de información. Crucialmente, la actualización del estado de celda incluye un término aditivo que permite que los gradientes fluyan a través de él sin multiplicaciones matriciales repetidas, evitando así el desvanecimiento exponencial.

La LSTM fue posteriormente refinada por Gers, Schmidhuber y Cummins (2000), quienes añadieron la puerta de olvido (*forget gate*), y su formulación moderna se consolidó como el estándar de facto para el procesamiento de secuencias hasta la llegada de la arquitectura Transformer.

### 4.3.2 El estado de celda como "cinta transportadora"

El estado de celda $\mathbf{C}_t \in \mathbb{R}^{d_h}$ es un vector que atraviesa toda la cadena temporal de la red, sufriendo solo interacciones lineales menores (multiplicaciones punto a punto y sumas) en cada paso temporal. Esta propiedad es análoga a una cinta transportadora en una fábrica: la información puede viajar a lo largo de muchos pasos temporales con modificaciones mínimas, sin pasar por las transformaciones no lineales altamente compresivas que caracterizan a la RNN básica.

La ecuación de actualización del estado de celda tiene la forma:

$$\mathbf{C}_t = \mathbf{f}_t \odot \mathbf{C}_{t-1} + \mathbf{i}_t \odot \tilde{\mathbf{C}}_t$$

donde $\odot$ denota el producto de Hadamard (multiplicación elemento a elemento). Observemos que esta ecuación es **lineal en $\mathbf{C}_{t-1}$** (modulada por $\mathbf{f}_t$), lo que significa que el gradiente $\frac{\partial \mathbf{C}_t}{\partial \mathbf{C}_{t-1}} = \text{diag}(\mathbf{f}_t)$, que es simplemente una matriz diagonal cuyos elementos están en $[0, 1]$. Cuando la puerta de olvido está cerca de 1, el gradiente fluye sin atenuación, resolviendo el problema del gradiente desvaneciente para las dependencias codificadas en el estado de celda.

### 4.3.3 Las tres puertas: formulación matemática completa

La LSTM utiliza tres puertas (*gates*) —la puerta de olvido, la puerta de entrada y la puerta de salida— para controlar el flujo de información hacia, dentro de y desde el estado de celda. Cada puerta es un vector cuyos elementos están en el intervalo $[0, 1]$, producido por una función sigmoide aplicada a una transformación afín de las entradas.

A continuación, presentamos las ecuaciones completas de la LSTM, donde $\mathbf{x}_t \in \mathbb{R}^{d_x}$ es la entrada, $\mathbf{h}_{t-1} \in \mathbb{R}^{d_h}$ es el estado oculto anterior, y $\mathbf{C}_{t-1} \in \mathbb{R}^{d_h}$ es el estado de celda anterior.

#### Puerta de olvido (*Forget Gate*)

$$\mathbf{f}_t = \sigma\!\left(\mathbf{W}_f [\mathbf{h}_{t-1}, \mathbf{x}_t] + \mathbf{b}_f\right)$$

La puerta de olvido determina **qué información del estado de celda anterior debe descartarse**. El vector $\mathbf{f}_t \in \mathbb{R}^{d_h}$ tiene elementos en $[0, 1]$: un valor de 0 indica "olvidar completamente" y un valor de 1 indica "recordar completamente". La notación $[\mathbf{h}_{t-1}, \mathbf{x}_t]$ denota la concatenación de los vectores $\mathbf{h}_{t-1}$ y $\mathbf{x}_t$, resultando en un vector de dimensión $d_h + d_x$. La matriz de pesos $\mathbf{W}_f \in \mathbb{R}^{d_h \times (d_h + d_x)}$ y el vector de sesgo $\mathbf{b}_f \in \mathbb{R}^{d_h}$ son parámetros aprendidos durante el entrenamiento. La función sigmoide $\sigma(z) = \frac{1}{1+e^{-z}}$ asegura que los valores de la puerta estén en el rango $(0, 1)$.

Intuitivamente, la puerta de olvido actúa como un "filtro de relevancia temporal". Consideremos una analogía con las comunicaciones: si un codificador semántico está procesando una oración y encuentra un punto final, la puerta de olvido puede aprender a "reiniciar" partes del estado de celda que almacenaban información sobre la oración anterior, ya que esa información ya no es relevante para procesar la siguiente oración.

#### Puerta de entrada (*Input Gate*) y celda candidata

$$\mathbf{i}_t = \sigma\!\left(\mathbf{W}_i [\mathbf{h}_{t-1}, \mathbf{x}_t] + \mathbf{b}_i\right)$$

$$\tilde{\mathbf{C}}_t = \tanh\!\left(\mathbf{W}_C [\mathbf{h}_{t-1}, \mathbf{x}_t] + \mathbf{b}_C\right)$$

La puerta de entrada opera en dos pasos. Primero, el vector $\mathbf{i}_t \in \mathbb{R}^{d_h}$ determina **qué componentes del estado de celda se actualizarán** con nueva información. Segundo, el vector $\tilde{\mathbf{C}}_t \in \mathbb{R}^{d_h}$ es la **celda candidata**, que contiene los valores potenciales que podrían añadirse al estado de celda. La celda candidata se calcula mediante una transformación afín seguida de $\tanh$, que produce valores en $(-1, 1)$. Las matrices $\mathbf{W}_i \in \mathbb{R}^{d_h \times (d_h + d_x)}$, $\mathbf{W}_C \in \mathbb{R}^{d_h \times (d_h + d_x)}$ y los vectores de sesgo $\mathbf{b}_i, \mathbf{b}_C \in \mathbb{R}^{d_h}$ son parámetros aprendidos independientes de los de la puerta de olvido.

La analogía para la puerta de entrada es la de un "controlador de escritura" en una memoria. El vector $\mathbf{i}_t$ decide qué posiciones de la memoria se van a escribir, y $\tilde{\mathbf{C}}_t$ contiene los datos que se van a escribir. Solo donde $\mathbf{i}_t$ tiene valores altos se incorporará la información de $\tilde{\mathbf{C}}_t$ al estado de celda.

#### Actualización del estado de celda

$$\mathbf{C}_t = \mathbf{f}_t \odot \mathbf{C}_{t-1} + \mathbf{i}_t \odot \tilde{\mathbf{C}}_t$$

Esta ecuación combina las dos operaciones anteriores. El primer término $\mathbf{f}_t \odot \mathbf{C}_{t-1}$ retiene selectivamente la información del estado anterior (según lo que la puerta de olvido decida preservar), y el segundo término $\mathbf{i}_t \odot \tilde{\mathbf{C}}_t$ añade nueva información (filtrada por la puerta de entrada). La operación $\odot$ es el producto de Hadamard, que opera elemento a elemento:

$$[\mathbf{C}_t]_j = [\mathbf{f}_t]_j \cdot [\mathbf{C}_{t-1}]_j + [\mathbf{i}_t]_j \cdot [\tilde{\mathbf{C}}_t]_j, \quad j = 1, 2, \ldots, d_h$$

Cada componente $j$ del estado de celda se actualiza de forma independiente, lo que permite que diferentes "ranuras" de memoria almacenen y olviden información de manera independiente. Algunas componentes pueden mantener información durante cientos de pasos temporales (cuando $[\mathbf{f}_t]_j \approx 1$ consistentemente), mientras que otras se actualizan frecuentemente.

#### Puerta de salida (*Output Gate*) y estado oculto

$$\mathbf{o}_t = \sigma\!\left(\mathbf{W}_o [\mathbf{h}_{t-1}, \mathbf{x}_t] + \mathbf{b}_o\right)$$

$$\mathbf{h}_t = \mathbf{o}_t \odot \tanh(\mathbf{C}_t)$$

La puerta de salida $\mathbf{o}_t \in \mathbb{R}^{d_h}$ determina **qué partes del estado de celda se exponen como estado oculto**. El estado de celda $\mathbf{C}_t$ pasa primero por una función $\tanh$ para normalizar sus valores al rango $(-1, 1)$, y luego se filtra por la puerta de salida mediante el producto de Hadamard. El estado oculto resultante $\mathbf{h}_t$ es lo que se pasa a la siguiente celda LSTM y, opcionalmente, a la capa de salida para producir la predicción.

La puerta de salida implementa un "controlador de lectura": el estado de celda puede contener mucha información almacenada, pero solo una fracción de ella es relevante para la salida en el instante actual. Por ejemplo, en un sistema de comunicación semántica que procesa texto, el estado de celda puede almacenar información sobre el sujeto, el verbo y el objeto de una oración simultáneamente, pero en un momento dado solo necesita exponer la información relevante para predecir el siguiente token.

**Figura 4.2:** *Diagrama detallado de la arquitectura interna de una celda LSTM. La celda recibe tres entradas: la entrada actual $\mathbf{x}_t$ (desde abajo), el estado oculto anterior $\mathbf{h}_{t-1}$ (desde la izquierda) y el estado de celda anterior $\mathbf{C}_{t-1}$ (desde la izquierda, por la línea horizontal superior que representa la "cinta transportadora"). Dentro de la celda se muestran: (1) La puerta de olvido $\mathbf{f}_t$, representada por un nodo con el símbolo $\sigma$, que recibe $[\mathbf{h}_{t-1}, \mathbf{x}_t]$ y produce un vector que se multiplica punto a punto ($\odot$) con $\mathbf{C}_{t-1}$. (2) La puerta de entrada $\mathbf{i}_t$ (nodo $\sigma$) y la celda candidata $\tilde{\mathbf{C}}_t$ (nodo $\tanh$), ambas recibiendo $[\mathbf{h}_{t-1}, \mathbf{x}_t]$; sus salidas se multiplican punto a punto y el resultado se suma ($+$) al estado de celda filtrado, produciendo $\mathbf{C}_t$. (3) La puerta de salida $\mathbf{o}_t$ (nodo $\sigma$), que recibe $[\mathbf{h}_{t-1}, \mathbf{x}_t]$; su salida se multiplica punto a punto con $\tanh(\mathbf{C}_t)$ para producir el estado oculto $\mathbf{h}_t$. Las salidas de la celda son $\mathbf{C}_t$ (hacia la derecha por la cinta transportadora) y $\mathbf{h}_t$ (hacia la derecha y hacia arriba). Los nodos circulares representan operaciones punto a punto ($\odot$ para multiplicación, $+$ para suma), y los nodos rectangulares representan capas neuronales con la activación indicada ($\sigma$ o $\tanh$).*

### 4.3.4 Recuento de parámetros

Es instructivo calcular el número total de parámetros de una celda LSTM, ya que esto ilustra el costo computacional respecto a una RNN básica. La LSTM tiene cuatro conjuntos de parámetros (uno para cada una de las tres puertas y uno para la celda candidata):

- Puerta de olvido: $\mathbf{W}_f \in \mathbb{R}^{d_h \times (d_h + d_x)}$, $\mathbf{b}_f \in \mathbb{R}^{d_h}$ → $d_h(d_h + d_x) + d_h$ parámetros
- Puerta de entrada: $\mathbf{W}_i \in \mathbb{R}^{d_h \times (d_h + d_x)}$, $\mathbf{b}_i \in \mathbb{R}^{d_h}$ → $d_h(d_h + d_x) + d_h$ parámetros
- Celda candidata: $\mathbf{W}_C \in \mathbb{R}^{d_h \times (d_h + d_x)}$, $\mathbf{b}_C \in \mathbb{R}^{d_h}$ → $d_h(d_h + d_x) + d_h$ parámetros
- Puerta de salida: $\mathbf{W}_o \in \mathbb{R}^{d_h \times (d_h + d_x)}$, $\mathbf{b}_o \in \mathbb{R}^{d_h}$ → $d_h(d_h + d_x) + d_h$ parámetros

**Total**: $4 \cdot [d_h(d_h + d_x) + d_h] = 4d_h(d_h + d_x + 1)$

Comparado con una RNN básica que tiene $d_h(d_h + d_x) + d_h = d_h(d_h + d_x + 1)$ parámetros (excluyendo la capa de salida), la LSTM tiene exactamente **4 veces más parámetros**. Este incremento es el precio de la capacidad de mantener gradientes estables a lo largo del tiempo, y en la práctica es un compromiso altamente favorable dado el dramático mejoramiento en el aprendizaje de dependencias a largo plazo.

### 4.3.5 Ejemplo numérico detallado

Para consolidar la comprensión de las ecuaciones de la LSTM, trabajemos un ejemplo numérico completo con dimensiones pequeñas: $d_x = 2$ (dimensión de entrada) y $d_h = 2$ (dimensión del estado oculto). Procesaremos una secuencia de 3 pasos temporales.

**Inicialización de parámetros** (valores simplificados para facilitar el cálculo):

Para todas las matrices de pesos, usaremos la notación $\mathbf{W}_g \in \mathbb{R}^{2 \times 4}$ (ya que $d_h + d_x = 4$), y para los vectores de sesgo, $\mathbf{b}_g \in \mathbb{R}^2$.

$$\mathbf{W}_f = \begin{bmatrix} 0.5 & 0.1 & 0.2 & 0.3 \\ 0.4 & 0.6 & 0.1 & 0.2 \end{bmatrix}, \quad \mathbf{b}_f = \begin{bmatrix} 0.1 \\ 0.1 \end{bmatrix}$$

$$\mathbf{W}_i = \begin{bmatrix} 0.3 & 0.2 & 0.5 & 0.1 \\ 0.1 & 0.4 & 0.3 & 0.6 \end{bmatrix}, \quad \mathbf{b}_i = \begin{bmatrix} 0.0 \\ 0.0 \end{bmatrix}$$

$$\mathbf{W}_C = \begin{bmatrix} 0.2 & 0.3 & 0.4 & 0.1 \\ 0.5 & 0.1 & 0.2 & 0.3 \end{bmatrix}, \quad \mathbf{b}_C = \begin{bmatrix} 0.0 \\ 0.0 \end{bmatrix}$$

$$\mathbf{W}_o = \begin{bmatrix} 0.4 & 0.2 & 0.1 & 0.5 \\ 0.3 & 0.5 & 0.4 & 0.2 \end{bmatrix}, \quad \mathbf{b}_o = \begin{bmatrix} 0.1 \\ 0.1 \end{bmatrix}$$

**Estado inicial**: $\mathbf{h}_0 = [0, 0]^\top$, $\mathbf{C}_0 = [0, 0]^\top$.

**Secuencia de entrada**: $\mathbf{x}_1 = [1, 0]^\top$, $\mathbf{x}_2 = [0, 1]^\top$, $\mathbf{x}_3 = [1, 1]^\top$.

---

**Paso temporal $t = 1$:**

Vector concatenado: $[\mathbf{h}_0, \mathbf{x}_1] = [0, 0, 1, 0]^\top$

**Puerta de olvido:**

$$\mathbf{W}_f [\mathbf{h}_0, \mathbf{x}_1] + \mathbf{b}_f = \begin{bmatrix} 0.5 \cdot 0 + 0.1 \cdot 0 + 0.2 \cdot 1 + 0.3 \cdot 0 \\ 0.4 \cdot 0 + 0.6 \cdot 0 + 0.1 \cdot 1 + 0.2 \cdot 0 \end{bmatrix} + \begin{bmatrix} 0.1 \\ 0.1 \end{bmatrix} = \begin{bmatrix} 0.3 \\ 0.2 \end{bmatrix}$$

$$\mathbf{f}_1 = \sigma\!\left(\begin{bmatrix} 0.3 \\ 0.2 \end{bmatrix}\right) = \begin{bmatrix} 0.574 \\ 0.550 \end{bmatrix}$$

**Puerta de entrada:**

$$\mathbf{W}_i [\mathbf{h}_0, \mathbf{x}_1] + \mathbf{b}_i = \begin{bmatrix} 0.3 \cdot 0 + 0.2 \cdot 0 + 0.5 \cdot 1 + 0.1 \cdot 0 \\ 0.1 \cdot 0 + 0.4 \cdot 0 + 0.3 \cdot 1 + 0.6 \cdot 0 \end{bmatrix} = \begin{bmatrix} 0.5 \\ 0.3 \end{bmatrix}$$

$$\mathbf{i}_1 = \sigma\!\left(\begin{bmatrix} 0.5 \\ 0.3 \end{bmatrix}\right) = \begin{bmatrix} 0.622 \\ 0.574 \end{bmatrix}$$

**Celda candidata:**

$$\mathbf{W}_C [\mathbf{h}_0, \mathbf{x}_1] + \mathbf{b}_C = \begin{bmatrix} 0.2 \cdot 0 + 0.3 \cdot 0 + 0.4 \cdot 1 + 0.1 \cdot 0 \\ 0.5 \cdot 0 + 0.1 \cdot 0 + 0.2 \cdot 1 + 0.3 \cdot 0 \end{bmatrix} = \begin{bmatrix} 0.4 \\ 0.2 \end{bmatrix}$$

$$\tilde{\mathbf{C}}_1 = \tanh\!\left(\begin{bmatrix} 0.4 \\ 0.2 \end{bmatrix}\right) = \begin{bmatrix} 0.380 \\ 0.197 \end{bmatrix}$$

**Actualización del estado de celda:**

$$\mathbf{C}_1 = \mathbf{f}_1 \odot \mathbf{C}_0 + \mathbf{i}_1 \odot \tilde{\mathbf{C}}_1 = \begin{bmatrix} 0.574 \\ 0.550 \end{bmatrix} \odot \begin{bmatrix} 0 \\ 0 \end{bmatrix} + \begin{bmatrix} 0.622 \\ 0.574 \end{bmatrix} \odot \begin{bmatrix} 0.380 \\ 0.197 \end{bmatrix} = \begin{bmatrix} 0.236 \\ 0.113 \end{bmatrix}$$

Nótese que, dado que $\mathbf{C}_0 = \mathbf{0}$, el primer término es cero y el estado de celda se inicializa completamente a partir de la celda candidata filtrada por la puerta de entrada.

**Puerta de salida:**

$$\mathbf{W}_o [\mathbf{h}_0, \mathbf{x}_1] + \mathbf{b}_o = \begin{bmatrix} 0.4 \cdot 0 + 0.2 \cdot 0 + 0.1 \cdot 1 + 0.5 \cdot 0 \\ 0.3 \cdot 0 + 0.5 \cdot 0 + 0.4 \cdot 1 + 0.2 \cdot 0 \end{bmatrix} + \begin{bmatrix} 0.1 \\ 0.1 \end{bmatrix} = \begin{bmatrix} 0.2 \\ 0.5 \end{bmatrix}$$

$$\mathbf{o}_1 = \sigma\!\left(\begin{bmatrix} 0.2 \\ 0.5 \end{bmatrix}\right) = \begin{bmatrix} 0.550 \\ 0.622 \end{bmatrix}$$

**Estado oculto:**

$$\mathbf{h}_1 = \mathbf{o}_1 \odot \tanh(\mathbf{C}_1) = \begin{bmatrix} 0.550 \\ 0.622 \end{bmatrix} \odot \tanh\!\left(\begin{bmatrix} 0.236 \\ 0.113 \end{bmatrix}\right) = \begin{bmatrix} 0.550 \\ 0.622 \end{bmatrix} \odot \begin{bmatrix} 0.232 \\ 0.113 \end{bmatrix} = \begin{bmatrix} 0.128 \\ 0.070 \end{bmatrix}$$

---

**Paso temporal $t = 2$:**

Vector concatenado: $[\mathbf{h}_1, \mathbf{x}_2] = [0.128, 0.070, 0, 1]^\top$

**Puerta de olvido:**

$$\mathbf{W}_f [\mathbf{h}_1, \mathbf{x}_2] + \mathbf{b}_f = \begin{bmatrix} 0.5(0.128) + 0.1(0.070) + 0.2(0) + 0.3(1) \\ 0.4(0.128) + 0.6(0.070) + 0.1(0) + 0.2(1) \end{bmatrix} + \begin{bmatrix} 0.1 \\ 0.1 \end{bmatrix}$$

$$= \begin{bmatrix} 0.064 + 0.007 + 0 + 0.3 + 0.1 \\ 0.051 + 0.042 + 0 + 0.2 + 0.1 \end{bmatrix} = \begin{bmatrix} 0.471 \\ 0.393 \end{bmatrix}$$

$$\mathbf{f}_2 = \sigma\!\left(\begin{bmatrix} 0.471 \\ 0.393 \end{bmatrix}\right) = \begin{bmatrix} 0.616 \\ 0.597 \end{bmatrix}$$

**Puerta de entrada:**

$$\mathbf{W}_i [\mathbf{h}_1, \mathbf{x}_2] + \mathbf{b}_i = \begin{bmatrix} 0.3(0.128) + 0.2(0.070) + 0.5(0) + 0.1(1) \\ 0.1(0.128) + 0.4(0.070) + 0.3(0) + 0.6(1) \end{bmatrix} = \begin{bmatrix} 0.152 \\ 0.641 \end{bmatrix}$$

$$\mathbf{i}_2 = \sigma\!\left(\begin{bmatrix} 0.152 \\ 0.641 \end{bmatrix}\right) = \begin{bmatrix} 0.538 \\ 0.655 \end{bmatrix}$$

**Celda candidata:**

$$\mathbf{W}_C [\mathbf{h}_1, \mathbf{x}_2] + \mathbf{b}_C = \begin{bmatrix} 0.2(0.128) + 0.3(0.070) + 0.4(0) + 0.1(1) \\ 0.5(0.128) + 0.1(0.070) + 0.2(0) + 0.3(1) \end{bmatrix} = \begin{bmatrix} 0.147 \\ 0.371 \end{bmatrix}$$

$$\tilde{\mathbf{C}}_2 = \tanh\!\left(\begin{bmatrix} 0.147 \\ 0.371 \end{bmatrix}\right) = \begin{bmatrix} 0.146 \\ 0.355 \end{bmatrix}$$

**Actualización del estado de celda:**

$$\mathbf{C}_2 = \mathbf{f}_2 \odot \mathbf{C}_1 + \mathbf{i}_2 \odot \tilde{\mathbf{C}}_2 = \begin{bmatrix} 0.616 \\ 0.597 \end{bmatrix} \odot \begin{bmatrix} 0.236 \\ 0.113 \end{bmatrix} + \begin{bmatrix} 0.538 \\ 0.655 \end{bmatrix} \odot \begin{bmatrix} 0.146 \\ 0.355 \end{bmatrix} = \begin{bmatrix} 0.145 + 0.079 \\ 0.067 + 0.233 \end{bmatrix} = \begin{bmatrix} 0.224 \\ 0.300 \end{bmatrix}$$

Observemos cómo la puerta de olvido retiene parcialmente la información del paso anterior ($\mathbf{f}_2 \approx 0.6$), mientras que la puerta de entrada permite la incorporación de nueva información.

**Puerta de salida y estado oculto:**

$$\mathbf{o}_2 = \sigma\!\left(\mathbf{W}_o [\mathbf{h}_1, \mathbf{x}_2] + \mathbf{b}_o\right)$$

$$\mathbf{W}_o [\mathbf{h}_1, \mathbf{x}_2] + \mathbf{b}_o = \begin{bmatrix} 0.4(0.128) + 0.2(0.070) + 0.1(0) + 0.5(1) + 0.1 \\ 0.3(0.128) + 0.5(0.070) + 0.4(0) + 0.2(1) + 0.1 \end{bmatrix} = \begin{bmatrix} 0.665 \\ 0.373 \end{bmatrix}$$

$$\mathbf{o}_2 = \sigma\!\left(\begin{bmatrix} 0.665 \\ 0.373 \end{bmatrix}\right) = \begin{bmatrix} 0.660 \\ 0.592 \end{bmatrix}$$

$$\mathbf{h}_2 = \mathbf{o}_2 \odot \tanh(\mathbf{C}_2) = \begin{bmatrix} 0.660 \\ 0.592 \end{bmatrix} \odot \begin{bmatrix} 0.220 \\ 0.291 \end{bmatrix} = \begin{bmatrix} 0.145 \\ 0.172 \end{bmatrix}$$

---

**Paso temporal $t = 3$:**

Vector concatenado: $[\mathbf{h}_2, \mathbf{x}_3] = [0.145, 0.172, 1, 1]^\top$

**Puerta de olvido:**

$$\mathbf{W}_f [\mathbf{h}_2, \mathbf{x}_3] + \mathbf{b}_f = \begin{bmatrix} 0.5(0.145) + 0.1(0.172) + 0.2(1) + 0.3(1) + 0.1 \\ 0.4(0.145) + 0.6(0.172) + 0.1(1) + 0.2(1) + 0.1 \end{bmatrix} = \begin{bmatrix} 0.690 \\ 0.561 \end{bmatrix}$$

$$\mathbf{f}_3 = \sigma\!\left(\begin{bmatrix} 0.690 \\ 0.561 \end{bmatrix}\right) = \begin{bmatrix} 0.666 \\ 0.637 \end{bmatrix}$$

**Puerta de entrada:**

$$\mathbf{W}_i [\mathbf{h}_2, \mathbf{x}_3] + \mathbf{b}_i = \begin{bmatrix} 0.3(0.145) + 0.2(0.172) + 0.5(1) + 0.1(1) \\ 0.1(0.145) + 0.4(0.172) + 0.3(1) + 0.6(1) \end{bmatrix} = \begin{bmatrix} 0.678 \\ 0.983 \end{bmatrix}$$

$$\mathbf{i}_3 = \sigma\!\left(\begin{bmatrix} 0.678 \\ 0.983 \end{bmatrix}\right) = \begin{bmatrix} 0.663 \\ 0.728 \end{bmatrix}$$

**Celda candidata:**

$$\mathbf{W}_C [\mathbf{h}_2, \mathbf{x}_3] + \mathbf{b}_C = \begin{bmatrix} 0.2(0.145) + 0.3(0.172) + 0.4(1) + 0.1(1) \\ 0.5(0.145) + 0.1(0.172) + 0.2(1) + 0.3(1) \end{bmatrix} = \begin{bmatrix} 0.581 \\ 0.590 \end{bmatrix}$$

$$\tilde{\mathbf{C}}_3 = \tanh\!\left(\begin{bmatrix} 0.581 \\ 0.590 \end{bmatrix}\right) = \begin{bmatrix} 0.523 \\ 0.530 \end{bmatrix}$$

**Actualización del estado de celda:**

$$\mathbf{C}_3 = \mathbf{f}_3 \odot \mathbf{C}_2 + \mathbf{i}_3 \odot \tilde{\mathbf{C}}_3 = \begin{bmatrix} 0.666(0.224) + 0.663(0.523) \\ 0.637(0.300) + 0.728(0.530) \end{bmatrix} = \begin{bmatrix} 0.149 + 0.347 \\ 0.191 + 0.386 \end{bmatrix} = \begin{bmatrix} 0.496 \\ 0.577 \end{bmatrix}$$

**Puerta de salida y estado oculto:**

$$\mathbf{W}_o [\mathbf{h}_2, \mathbf{x}_3] + \mathbf{b}_o = \begin{bmatrix} 0.4(0.145) + 0.2(0.172) + 0.1(1) + 0.5(1) + 0.1 \\ 0.3(0.145) + 0.5(0.172) + 0.4(1) + 0.2(1) + 0.1 \end{bmatrix} = \begin{bmatrix} 0.792 \\ 0.830 \end{bmatrix}$$

$$\mathbf{o}_3 = \sigma\!\left(\begin{bmatrix} 0.792 \\ 0.830 \end{bmatrix}\right) = \begin{bmatrix} 0.688 \\ 0.696 \end{bmatrix}$$

$$\mathbf{h}_3 = \mathbf{o}_3 \odot \tanh(\mathbf{C}_3) = \begin{bmatrix} 0.688 \\ 0.696 \end{bmatrix} \odot \begin{bmatrix} 0.457 \\ 0.520 \end{bmatrix} = \begin{bmatrix} 0.314 \\ 0.362 \end{bmatrix}$$

---

**Resumen del ejemplo:**

| Paso $t$ | $\mathbf{f}_t$ | $\mathbf{i}_t$ | $\tilde{\mathbf{C}}_t$ | $\mathbf{C}_t$ | $\mathbf{o}_t$ | $\mathbf{h}_t$ |
|-----------|-----------|-----------|-------------|-----------|-----------|-----------|
| 1 | [0.574, 0.550] | [0.622, 0.574] | [0.380, 0.197] | [0.236, 0.113] | [0.550, 0.622] | [0.128, 0.070] |
| 2 | [0.616, 0.597] | [0.538, 0.655] | [0.146, 0.355] | [0.224, 0.300] | [0.660, 0.592] | [0.145, 0.172] |
| 3 | [0.666, 0.637] | [0.663, 0.728] | [0.523, 0.530] | [0.496, 0.577] | [0.688, 0.696] | [0.314, 0.362] |

Este ejemplo ilustra varios aspectos importantes. Primero, los valores de las puertas son moderados (en el rango 0.5-0.7) debido a que los pesos son pequeños y las entradas al sigmoide están cerca de cero. En la práctica, después del entrenamiento, las puertas tienden a producir valores más extremos (cercanos a 0 o 1), lo que resulta en decisiones más definidas de "olvidar" o "recordar". Segundo, el estado de celda $\mathbf{C}_t$ acumula gradualmente información a lo largo de la secuencia, creciendo de $[0.236, 0.113]$ a $[0.496, 0.577]$. Tercero, el estado oculto $\mathbf{h}_t$ es siempre más pequeño en magnitud que el estado de celda, debido al filtrado por la puerta de salida y la compresión de $\tanh$.

### 4.3.6 Análisis del flujo de gradientes en la LSTM

Para comprender formalmente por qué la LSTM resuelve el problema del gradiente desvaneciente, examinemos el gradiente del estado de celda. A partir de la ecuación de actualización:

$$\mathbf{C}_t = \mathbf{f}_t \odot \mathbf{C}_{t-1} + \mathbf{i}_t \odot \tilde{\mathbf{C}}_t$$

el gradiente del estado de celda futuro con respecto al estado de celda pasado es:

$$\frac{\partial \mathbf{C}_t}{\partial \mathbf{C}_{t-1}} = \text{diag}(\mathbf{f}_t) + \text{términos adicionales}$$

Los "términos adicionales" surgen porque $\mathbf{f}_t$, $\mathbf{i}_t$ y $\tilde{\mathbf{C}}_t$ también dependen (indirectamente) de $\mathbf{C}_{t-1}$ a través de $\mathbf{h}_{t-1}$, pero el término dominante es $\text{diag}(\mathbf{f}_t)$.

Para una cadena de múltiples pasos temporales:

$$\frac{\partial \mathbf{C}_T}{\partial \mathbf{C}_k} \approx \prod_{t=k+1}^{T} \text{diag}(\mathbf{f}_t)$$

Cada factor $\text{diag}(\mathbf{f}_t)$ es una matriz diagonal con elementos en $[0, 1]$. Si la puerta de olvido aprende a mantener $\mathbf{f}_t \approx 1$ (es decir, a no olvidar), entonces:

$$\prod_{t=k+1}^{T} \text{diag}(\mathbf{f}_t) \approx \mathbf{I}$$

y el gradiente fluye sin atenuación desde el paso $T$ hasta el paso $k$, sin importar cuán grande sea la distancia $T - k$. Esto contrasta dramáticamente con la RNN básica, donde el producto de matrices $\mathbf{W}_{hh}$ y derivadas de activaciones conduce inevitablemente a la atenuación exponencial.

La clave está en que **la red aprende cuándo olvidar y cuándo recordar** a través de la puerta de olvido. No se fuerza un valor fijo de retención; en cambio, la red adapta dinámicamente el flujo de gradientes según la tarea y los datos.

---

## 4.4 Gated Recurrent Unit (GRU)

### 4.4.1 Una versión simplificada de la LSTM

La **Unidad Recurrente con Puerta** (GRU, *Gated Recurrent Unit*), propuesta por Cho et al. en 2014, es una variante simplificada de la LSTM que combina las puertas de olvido y de entrada en una sola "puerta de actualización", y fusiona el estado de celda con el estado oculto. El resultado es una arquitectura con solo dos puertas (en lugar de tres) y un único vector de estado (en lugar de dos), lo que reduce significativamente el número de parámetros y el costo computacional, manteniendo un rendimiento comparable al de la LSTM en muchas tareas.

### 4.4.2 Formulación matemática

Las ecuaciones de la GRU son las siguientes:

**Puerta de reinicio (*Reset Gate*):**

$$\mathbf{r}_t = \sigma\!\left(\mathbf{W}_r [\mathbf{h}_{t-1}, \mathbf{x}_t]\right)$$

La puerta de reinicio $\mathbf{r}_t \in \mathbb{R}^{d_h}$ determina cuánto del estado oculto anterior debe ser "olvidado" al calcular el nuevo estado candidato. Cuando $\mathbf{r}_t \approx 0$, el estado candidato se calcula como si no hubiera historia previa, lo que permite que la red "reinicie" su estado. Cuando $\mathbf{r}_t \approx 1$, toda la información del estado anterior se utiliza para calcular el candidato. La matriz $\mathbf{W}_r \in \mathbb{R}^{d_h \times (d_h + d_x)}$ es un parámetro aprendido. Nótese que, a diferencia de la formulación de la LSTM presentada anteriormente, aquí se omite el sesgo por simplicidad (en la práctica, las implementaciones suelen incluirlo).

**Puerta de actualización (*Update Gate*):**

$$\mathbf{z}_t = \sigma\!\left(\mathbf{W}_z [\mathbf{h}_{t-1}, \mathbf{x}_t]\right)$$

La puerta de actualización $\mathbf{z}_t \in \mathbb{R}^{d_h}$ controla el equilibrio entre el estado anterior y el nuevo estado candidato. Esta puerta unifica las funciones de las puertas de olvido y de entrada de la LSTM: un valor $\mathbf{z}_t \approx 0$ significa "mantener el estado anterior" (equivalente a $\mathbf{f}_t \approx 1$, $\mathbf{i}_t \approx 0$ en la LSTM), mientras que $\mathbf{z}_t \approx 1$ significa "adoptar completamente el estado candidato" (equivalente a $\mathbf{f}_t \approx 0$, $\mathbf{i}_t \approx 1$).

**Estado oculto candidato:**

$$\tilde{\mathbf{h}}_t = \tanh\!\left(\mathbf{W} [\mathbf{r}_t \odot \mathbf{h}_{t-1}, \mathbf{x}_t]\right)$$

El estado candidato $\tilde{\mathbf{h}}_t$ se calcula de forma similar a la RNN básica, pero con una diferencia crucial: el estado oculto anterior se filtra por la puerta de reinicio antes de ser utilizado. El producto $\mathbf{r}_t \odot \mathbf{h}_{t-1}$ permite que la red borre selectivamente componentes del estado anterior que no son relevantes para el cálculo del nuevo candidato. La matriz $\mathbf{W} \in \mathbb{R}^{d_h \times (d_h + d_x)}$ transforma la concatenación del estado filtrado y la entrada actual.

**Estado oculto final:**

$$\mathbf{h}_t = (1 - \mathbf{z}_t) \odot \mathbf{h}_{t-1} + \mathbf{z}_t \odot \tilde{\mathbf{h}}_t$$

Esta ecuación es la interpolación lineal entre el estado anterior y el estado candidato, controlada por la puerta de actualización. Analicemos los casos extremos:

- Si $\mathbf{z}_t = \mathbf{0}$: $\mathbf{h}_t = \mathbf{h}_{t-1}$, el estado se copia sin modificación (la red "ignora" la entrada actual).
- Si $\mathbf{z}_t = \mathbf{1}$: $\mathbf{h}_t = \tilde{\mathbf{h}}_t$, el estado se reemplaza completamente por el candidato.
- En general, la puerta de actualización permite una mezcla suave entre mantener la memoria y actualizar con nueva información.

La relación entre la puerta de actualización de la GRU y las puertas de la LSTM se hace evidente al comparar la ecuación de actualización de la GRU con la del estado de celda de la LSTM. Definiendo $\mathbf{f}_t = 1 - \mathbf{z}_t$ y $\mathbf{i}_t = \mathbf{z}_t$, la ecuación de la GRU se puede reescribir como:

$$\mathbf{h}_t = \mathbf{f}_t \odot \mathbf{h}_{t-1} + \mathbf{i}_t \odot \tilde{\mathbf{h}}_t$$

que tiene la misma estructura que la actualización del estado de celda de la LSTM, con la restricción adicional de que $\mathbf{f}_t + \mathbf{i}_t = \mathbf{1}$ (las puertas están "acopladas"). En la LSTM, $\mathbf{f}_t$ e $\mathbf{i}_t$ son independientes, lo que le confiere mayor flexibilidad.

### 4.4.3 Comparación entre GRU y LSTM

La siguiente tabla resume las diferencias principales:

| Característica | LSTM | GRU |
|---|---|---|
| Vectores de estado | 2 ($\mathbf{C}_t$ y $\mathbf{h}_t$) | 1 ($\mathbf{h}_t$) |
| Puertas | 3 (olvido, entrada, salida) | 2 (reinicio, actualización) |
| Parámetros | $4d_h(d_h + d_x + 1)$ | $3d_h(d_h + d_x)$ |
| Puertas acopladas | No ($\mathbf{f}_t$ e $\mathbf{i}_t$ independientes) | Sí ($\mathbf{z}_t$ y $1-\mathbf{z}_t$) |
| Control de exposición | Sí (puerta de salida) | No |

En la práctica, múltiples estudios empíricos han mostrado que la LSTM y la GRU alcanzan rendimientos similares en una amplia variedad de tareas, incluyendo modelado de lenguaje, traducción automática y reconocimiento de voz. La GRU suele ser preferida cuando los recursos computacionales son limitados o cuando se trabaja con conjuntos de datos pequeños, ya que su menor número de parámetros reduce el riesgo de sobreajuste (*overfitting*). La LSTM, por su parte, tiende a ser preferida en tareas que requieren un control fino sobre la memoria y la exposición de información, o cuando se dispone de grandes volúmenes de datos.

En el contexto de las comunicaciones semánticas, la elección entre LSTM y GRU depende de la tarea específica. Para la codificación semántica de texto, donde las dependencias pueden ser muy largas y el control fino de la memoria es importante, la LSTM ha sido la elección predominante. Para tareas de estimación y predicción de canal en tiempo real, donde la eficiencia computacional es crítica y las dependencias temporales son más cortas, la GRU puede ser una alternativa atractiva.

---

## 4.5 Arquitecturas bidireccionales y apiladas

### 4.5.1 RNN/LSTM bidireccionales

En una RNN unidireccional estándar, la información fluye exclusivamente de izquierda a derecha: el estado oculto $\mathbf{h}_t$ en el instante $t$ captura información únicamente de las entradas pasadas $\mathbf{x}_1, \ldots, \mathbf{x}_t$. Sin embargo, en muchas aplicaciones es deseable que la representación en el instante $t$ capture información tanto del pasado como del futuro. Esto es particularmente relevante cuando se dispone de la secuencia completa antes de procesarla, como ocurre en tareas de clasificación de secuencias, traducción automática, o decodificación de canal con latencia permitida.

La **RNN bidireccional** (*Bidirectional RNN*, BiRNN), propuesta por Schuster y Paliwal en 1997, aborda esta limitación procesando la secuencia en ambas direcciones simultáneamente. La arquitectura consta de dos capas recurrentes independientes:

1. **Capa hacia adelante** (*forward*): Procesa la secuencia de izquierda a derecha, produciendo estados ocultos $\overrightarrow{\mathbf{h}}_t$:

$$\overrightarrow{\mathbf{h}}_t = f\!\left(\overrightarrow{\mathbf{W}}_{hh}\overrightarrow{\mathbf{h}}_{t-1} + \overrightarrow{\mathbf{W}}_{xh}\mathbf{x}_t + \overrightarrow{\mathbf{b}}_h\right)$$

2. **Capa hacia atrás** (*backward*): Procesa la secuencia de derecha a izquierda, produciendo estados ocultos $\overleftarrow{\mathbf{h}}_t$:

$$\overleftarrow{\mathbf{h}}_t = f\!\left(\overleftarrow{\mathbf{W}}_{hh}\overleftarrow{\mathbf{h}}_{t+1} + \overleftarrow{\mathbf{W}}_{xh}\mathbf{x}_t + \overleftarrow{\mathbf{b}}_h\right)$$

La representación final en cada paso temporal se obtiene concatenando ambos estados ocultos:

$$\mathbf{h}_t = [\overrightarrow{\mathbf{h}}_t, \overleftarrow{\mathbf{h}}_t] \in \mathbb{R}^{2d_h}$$

El estado $\overrightarrow{\mathbf{h}}_t$ codifica el contexto pasado (desde $\mathbf{x}_1$ hasta $\mathbf{x}_t$) y $\overleftarrow{\mathbf{h}}_t$ codifica el contexto futuro (desde $\mathbf{x}_T$ hasta $\mathbf{x}_t$). La concatenación $\mathbf{h}_t$ proporciona una representación rica que captura el contexto completo de la secuencia en cada posición.

Las capas hacia adelante y hacia atrás tienen parámetros completamente independientes (denotados con las flechas en las matrices de pesos), lo que duplica el número de parámetros respecto a una RNN unidireccional.

Es importante notar que las BiRNN solo son aplicables en situaciones donde la secuencia completa está disponible antes del procesamiento, lo que excluye aplicaciones estrictamente causales o en tiempo real. En comunicaciones, esto corresponde a escenarios de procesamiento por bloques: el receptor espera a recibir una trama completa antes de decodificarla. Para la transmisión en flujo continuo (*streaming*), se requieren arquitecturas unidireccionales.

La misma idea bidireccional se aplica directamente a las LSTM y GRU, resultando en las arquitecturas **BiLSTM** y **BiGRU**, que son ampliamente utilizadas en procesamiento de lenguaje natural y que han sido adoptadas en sistemas de comunicación semántica, particularmente para la codificación y decodificación semántica de texto.

### 4.5.2 Capas recurrentes apiladas (Deep RNN)

Así como las redes *feedforward* se benefician de múltiples capas para aprender representaciones jerárquicas, las RNN pueden apilarse en profundidad para crear **RNN profundas** (*Deep RNN* o *Stacked RNN*). En esta configuración, la salida de la capa recurrente $l$ en el paso temporal $t$ se utiliza como entrada de la capa $l+1$:

$$\mathbf{h}_t^{(l)} = f\!\left(\mathbf{W}_{hh}^{(l)}\mathbf{h}_{t-1}^{(l)} + \mathbf{W}_{xh}^{(l)}\mathbf{h}_t^{(l-1)} + \mathbf{b}_h^{(l)}\right)$$

donde $\mathbf{h}_t^{(0)} \equiv \mathbf{x}_t$ es la entrada original. Cada capa tiene sus propios parámetros $\mathbf{W}_{hh}^{(l)}$, $\mathbf{W}_{xh}^{(l)}$, $\mathbf{b}_h^{(l)}$, y captura patrones a diferentes niveles de abstracción: las capas inferiores tienden a capturar patrones locales y de bajo nivel, mientras que las capas superiores capturan patrones globales y de alto nivel.

La profundidad de las RNN apiladas suele ser más modesta que la de las CNN o los Transformers: típicamente se utilizan 2 a 4 capas recurrentes. Esto se debe a que cada capa recurrente ya es "profunda" en la dimensión temporal (desplegada a lo largo de $T$ pasos), y apilar demasiadas capas puede dificultar el entrenamiento y aumentar el riesgo de sobreajuste.

Las técnicas de regularización son especialmente importantes en las RNN profundas. El **dropout** se aplica típicamente entre capas (no entre pasos temporales dentro de la misma capa), ya que el dropout temporal destruye la información almacenada en el estado oculto. Gal y Ghahramani (2016) propusieron el **dropout variacional** para RNN, donde la máscara de dropout se mantiene constante a lo largo de los pasos temporales pero varía entre secuencias.

### 4.5.3 Aplicaciones en NLP y procesamiento de señales

Las arquitecturas bidireccionales y apiladas han encontrado aplicaciones extensas tanto en procesamiento de lenguaje natural como en procesamiento de señales para telecomunicaciones:

**Procesamiento de lenguaje natural (NLP)**: Las BiLSTM apiladas fueron la arquitectura dominante para muchas tareas de NLP antes de la era de los Transformers. En particular, fueron utilizadas exitosamente en:
- Etiquetado de secuencias (POS tagging, NER)
- Análisis de sentimiento
- Traducción automática (como componente del codificador en modelos *sequence-to-sequence*)
- Comprensión lectora

**Procesamiento de señales para telecomunicaciones**: Las RNN y LSTM han sido aplicadas en:
- Estimación y predicción de canal en sistemas OFDM
- Detección de señales en canales con memoria
- Decodificación de códigos convolucionales y turbo códigos
- Compresión de voz y audio para transmisión eficiente
- Codificación semántica conjunta fuente-canal para texto y voz

En el paradigma de comunicaciones semánticas, las LSTM bidireccionales son particularmente relevantes en el codificador semántico (*semantic encoder*), donde la secuencia completa (por ejemplo, una oración) está disponible y se desea generar una representación semántica que capture el contexto completo. El decodificador semántico, por su parte, puede utilizar una LSTM unidireccional en modo autoregresivo, generando la secuencia de salida token por token.

---

## 4.6 Limitaciones de las RNN/LSTM frente a los Transformers

A pesar de los avances significativos que las LSTM y GRU representan sobre las RNN básicas, estas arquitecturas recurrentes presentan limitaciones fundamentales que motivaron el desarrollo de la arquitectura Transformer, que estudiaremos en secciones posteriores de este tutorial.

### 4.6.1 Procesamiento secuencial: imposibilidad de paralelizar

La limitación más severa de las RNN/LSTM desde el punto de vista computacional es su naturaleza **inherentemente secuencial**. El cálculo del estado oculto $\mathbf{h}_t$ requiere el estado anterior $\mathbf{h}_{t-1}$, que a su vez requiere $\mathbf{h}_{t-2}$, y así sucesivamente. Esto crea una **cadena de dependencias** que impide la paralelización del cómputo a lo largo de la dimensión temporal.

En términos de complejidad computacional, procesar una secuencia de longitud $T$ con una RNN/LSTM requiere $\mathcal{O}(T)$ operaciones secuenciales. Cada operación individual tiene complejidad $\mathcal{O}(d_h^2)$ (dominada por la multiplicación matricial $\mathbf{W}_{hh}\mathbf{h}_{t-1}$), resultando en una complejidad total de $\mathcal{O}(T \cdot d_h^2)$. El problema no es la complejidad total, sino que las $T$ operaciones deben ejecutarse en serie: no es posible calcular $\mathbf{h}_{50}$ hasta que $\mathbf{h}_{49}$ esté disponible.

Esto contrasta fuertemente con las operaciones convolucionales y de atención del Transformer, que pueden paralelizarse a lo largo de la dimensión temporal, aprovechando las capacidades de las unidades de procesamiento gráfico (GPU) modernas. En la práctica, esta diferencia se traduce en tiempos de entrenamiento significativamente mayores para las RNN/LSTM, especialmente para secuencias largas.

### 4.6.2 Ventana de contexto limitada en la práctica

Aunque las LSTM resuelven teóricamente el problema del gradiente desvaneciente, en la práctica su capacidad para capturar dependencias a largo plazo sigue siendo limitada. El estado oculto $\mathbf{h}_t \in \mathbb{R}^{d_h}$ tiene una capacidad de información fija (determinada por $d_h$), y debe comprimir toda la información relevante de la secuencia procesada hasta el instante $t$ en este vector de dimensión fija. A medida que la secuencia se alarga, la información de los pasos iniciales inevitablemente se diluye o se pierde, un fenómeno conocido como el **cuello de botella de la información** (*information bottleneck*).

Estudios empíricos han mostrado que las LSTM estándar típicamente pueden capturar dependencias efectivas de hasta unos pocos cientos de pasos temporales, con un degradamiento gradual más allá de esa distancia. Para secuencias de miles o decenas de miles de elementos (como las que aparecen en la generación de textos largos o en el procesamiento de señales de alta resolución), las LSTM resultan insuficientes.

### 4.6.3 Dificultad con secuencias muy largas

Relacionado con el punto anterior, pero desde una perspectiva diferente, el procesamiento de secuencias muy largas con RNN/LSTM presenta desafíos tanto de memoria como de estabilidad numérica. Durante el entrenamiento con BPTT, la red desplegada tiene una profundidad igual a la longitud de la secuencia $T$, lo que requiere almacenar los $T$ estados intermedios para la retropropagación. El consumo de memoria es $\mathcal{O}(T \cdot d_h)$, lo que puede ser prohibitivo para secuencias muy largas.

La técnica de **BPTT truncado** (*Truncated BPTT*) mitiga este problema al limitar la retropropagación a una ventana de $k < T$ pasos temporales, pero introduce un sesgo en la estimación del gradiente que impide el aprendizaje de dependencias más largas que $k$.

### 4.6.4 Hacia la arquitectura Transformer

Estas limitaciones —procesamiento secuencial, ventana de contexto prácticamente limitada y dificultad con secuencias largas— motivaron la búsqueda de arquitecturas alternativas que pudieran:

1. **Paralelizar** el cómputo a lo largo de la secuencia para un entrenamiento más rápido.
2. Proporcionar **acceso directo** a cualquier posición de la secuencia, sin la necesidad de propagar información a través de una cadena de estados ocultos.
3. **Escalar** eficientemente a secuencias mucho más largas.

La arquitectura Transformer, propuesta por Vaswani et al. (2017), logra estos tres objetivos mediante el mecanismo de **autoatención** (*self-attention*), que calcula las relaciones entre todas las posiciones de la secuencia en paralelo. Esta arquitectura revolucionaria será el tema de las secciones siguientes de este tutorial, pero es esencial comprender las RNN/LSTM como sus predecesoras para apreciar las motivaciones y las innovaciones que el Transformer introduce.

---

## 4.7 Ejemplo práctico: Predicción de series temporales

### 4.7.1 Descripción del problema

Para ilustrar la implementación práctica de una LSTM, consideremos el problema de **predicción de series temporales**, que tiene aplicaciones directas en telecomunicaciones: predicción de tráfico de red, predicción de estado de canal, estimación de calidad de enlace, entre otros.

En este ejemplo, implementaremos una LSTM en PyTorch para predecir los valores futuros de una señal sinusoidal con ruido, que puede interpretarse como una simplificación de la predicción de variaciones de potencia de señal recibida en un canal inalámbrico.

### 4.7.2 Implementación en PyTorch

```python
import torch
import torch.nn as nn
import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# 1. Generación de datos sintéticos
# ============================================================
# Simulamos una señal que podría representar variaciones
# temporales de un canal inalámbrico: una combinación de
# sinusoides con ruido gaussiano aditivo.

np.random.seed(42)
torch.manual_seed(42)

T_total = 1000          # Longitud total de la serie temporal
frecuencia_1 = 0.02     # Frecuencia de la componente principal
frecuencia_2 = 0.05     # Frecuencia de la componente secundaria
sigma_ruido = 0.1       # Desviación estándar del ruido

t = np.arange(T_total)
# Señal compuesta: dos sinusoides + ruido
senal = (
    np.sin(2 * np.pi * frecuencia_1 * t)
    + 0.5 * np.sin(2 * np.pi * frecuencia_2 * t)
    + sigma_ruido * np.random.randn(T_total)
)

# Normalizar la señal al rango [-1, 1] para facilitar
# el entrenamiento con activaciones tanh
senal = senal / np.max(np.abs(senal))

# ============================================================
# 2. Preparación de datos: ventanas deslizantes
# ============================================================
# Creamos pares (entrada, objetivo) usando una ventana
# deslizante: la entrada son los L pasos anteriores y
# el objetivo es el siguiente valor.

longitud_ventana = 50   # Número de pasos de entrada (L)

def crear_secuencias(datos, L):
    """
    Crea pares (X, y) a partir de una serie temporal.
    X[i] = datos[i:i+L]    (secuencia de entrada)
    y[i] = datos[i+L]      (valor a predecir)
    """
    X, y = [], []
    for i in range(len(datos) - L):
        X.append(datos[i:i+L])
        y.append(datos[i+L])
    return np.array(X), np.array(y)

X, y = crear_secuencias(senal, longitud_ventana)

# División en conjuntos de entrenamiento y prueba (80/20)
N_train = int(0.8 * len(X))
X_train, X_test = X[:N_train], X[N_train:]
y_train, y_test = y[:N_train], y[N_train:]

# Convertir a tensores de PyTorch
# LSTM espera entrada con forma (batch, seq_len, input_size)
X_train_t = torch.FloatTensor(X_train).unsqueeze(-1)  # (N, L, 1)
y_train_t = torch.FloatTensor(y_train).unsqueeze(-1)  # (N, 1)
X_test_t  = torch.FloatTensor(X_test).unsqueeze(-1)
y_test_t  = torch.FloatTensor(y_test).unsqueeze(-1)

print(f"Forma de X_train: {X_train_t.shape}")
print(f"Forma de y_train: {y_train_t.shape}")
print(f"Muestras de entrenamiento: {N_train}")
print(f"Muestras de prueba: {len(X_test)}")

# ============================================================
# 3. Definición del modelo LSTM
# ============================================================

class PredictorLSTM(nn.Module):
    """
    Red LSTM para predicción de series temporales.

    Arquitectura:
    - Capa LSTM con num_capas capas apiladas
    - Capa fully-connected para mapear el último estado
      oculto a la predicción escalar
    """
    def __init__(self, dim_entrada, dim_oculta, num_capas, dim_salida,
                 dropout=0.0):
        """
        Args:
            dim_entrada: Dimensión de cada elemento de la secuencia
                         (1 para serie univariada)
            dim_oculta:  Dimensión del estado oculto h_t
            num_capas:   Número de capas LSTM apiladas
            dim_salida:  Dimensión de la salida (1 para predicción
                         escalar)
            dropout:     Probabilidad de dropout entre capas LSTM
                         (solo aplica si num_capas > 1)
        """
        super(PredictorLSTM, self).__init__()

        self.dim_oculta = dim_oculta
        self.num_capas = num_capas

        # Capa LSTM de PyTorch:
        # - batch_first=True: la entrada tiene forma (batch, seq, feat)
        # - dropout: se aplica entre capas, no dentro de una capa
        self.lstm = nn.LSTM(
            input_size=dim_entrada,
            hidden_size=dim_oculta,
            num_layers=num_capas,
            batch_first=True,
            dropout=dropout if num_capas > 1 else 0.0
        )

        # Capa fully-connected: mapea h_T -> y_hat
        self.fc = nn.Linear(dim_oculta, dim_salida)

    def forward(self, x):
        """
        Propagación hacia adelante.

        Args:
            x: Tensor de entrada, forma (batch, seq_len, dim_entrada)

        Returns:
            prediccion: Tensor de salida, forma (batch, dim_salida)
        """
        # Inicializar estados oculto y de celda con ceros
        # Forma: (num_capas, batch, dim_oculta)
        batch_size = x.size(0)
        h_0 = torch.zeros(self.num_capas, batch_size,
                          self.dim_oculta).to(x.device)
        c_0 = torch.zeros(self.num_capas, batch_size,
                          self.dim_oculta).to(x.device)

        # Procesar la secuencia completa con la LSTM
        # salida_lstm: (batch, seq_len, dim_oculta)
        #   contiene h_t para todo t
        # (h_n, c_n): estados finales, forma (num_capas, batch, dim_oculta)
        salida_lstm, (h_n, c_n) = self.lstm(x, (h_0, c_0))

        # Usar solo el último estado oculto h_T para la predicción
        # h_n[-1] tiene forma (batch, dim_oculta)
        h_ultimo = h_n[-1]

        # Mapear a la dimensión de salida
        prediccion = self.fc(h_ultimo)

        return prediccion

# ============================================================
# 4. Configuración del entrenamiento
# ============================================================

# Hiperparámetros
dim_entrada = 1       # Serie univariada
dim_oculta = 64       # Dimensión del estado oculto
num_capas = 2         # Dos capas LSTM apiladas
dim_salida = 1        # Predecir un valor escalar
tasa_aprendizaje = 0.001
num_epocas = 100
tam_batch = 32

# Instanciar modelo, función de pérdida y optimizador
modelo = PredictorLSTM(dim_entrada, dim_oculta, num_capas, dim_salida,
                       dropout=0.2)
criterio = nn.MSELoss()              # Error cuadrático medio
optimizador = torch.optim.Adam(modelo.parameters(), lr=tasa_aprendizaje)

# Contar parámetros totales
num_params = sum(p.numel() for p in modelo.parameters() if p.requires_grad)
print(f"\nArquitectura del modelo:")
print(modelo)
print(f"\nParámetros entrenables: {num_params:,}")

# Crear DataLoaders para iterar por mini-batches
dataset_train = torch.utils.data.TensorDataset(X_train_t, y_train_t)
loader_train = torch.utils.data.DataLoader(
    dataset_train, batch_size=tam_batch, shuffle=True
)

# ============================================================
# 5. Bucle de entrenamiento
# ============================================================

historial_perdida_train = []
historial_perdida_test = []

print("\nIniciando entrenamiento...")
for epoca in range(num_epocas):
    modelo.train()
    perdida_acumulada = 0.0
    num_batches = 0

    for X_batch, y_batch in loader_train:
        # Propagación hacia adelante
        predicciones = modelo(X_batch)
        perdida = criterio(predicciones, y_batch)

        # Retropropagación y actualización de parámetros
        optimizador.zero_grad()
        perdida.backward()

        # Recorte de gradientes para estabilidad
        torch.nn.utils.clip_grad_norm_(modelo.parameters(), max_norm=1.0)

        optimizador.step()

        perdida_acumulada += perdida.item()
        num_batches += 1

    perdida_media_train = perdida_acumulada / num_batches
    historial_perdida_train.append(perdida_media_train)

    # Evaluar en el conjunto de prueba
    modelo.eval()
    with torch.no_grad():
        pred_test = modelo(X_test_t)
        perdida_test = criterio(pred_test, y_test_t).item()
        historial_perdida_test.append(perdida_test)

    # Imprimir progreso cada 10 épocas
    if (epoca + 1) % 10 == 0:
        print(f"  Época [{epoca+1:3d}/{num_epocas}]  "
              f"Pérdida train: {perdida_media_train:.6f}  "
              f"Pérdida test: {perdida_test:.6f}")

# ============================================================
# 6. Evaluación y visualización
# ============================================================

modelo.eval()
with torch.no_grad():
    predicciones_test = modelo(X_test_t).numpy().flatten()
    valores_reales = y_test_t.numpy().flatten()

# Calcular métricas de rendimiento
mse = np.mean((predicciones_test - valores_reales) ** 2)
mae = np.mean(np.abs(predicciones_test - valores_reales))
rmse = np.sqrt(mse)

print(f"\n--- Métricas de evaluación ---")
print(f"MSE  (Error Cuadrático Medio):     {mse:.6f}")
print(f"RMSE (Raíz del Error Cuad. Medio): {rmse:.6f}")
print(f"MAE  (Error Absoluto Medio):       {mae:.6f}")

# Gráfica 1: Curvas de pérdida durante el entrenamiento
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

axes[0].plot(historial_perdida_train, label='Entrenamiento', color='blue')
axes[0].plot(historial_perdida_test, label='Prueba', color='red')
axes[0].set_xlabel('Época')
axes[0].set_ylabel('MSE')
axes[0].set_title('Curva de aprendizaje')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Gráfica 2: Predicciones vs valores reales
N_mostrar = 200  # Mostrar los primeros 200 puntos del test
axes[1].plot(valores_reales[:N_mostrar], label='Real', color='blue',
             linewidth=1.5)
axes[1].plot(predicciones_test[:N_mostrar], label='Predicción LSTM',
             color='red', linewidth=1.5, linestyle='--')
axes[1].set_xlabel('Paso temporal')
axes[1].set_ylabel('Valor de la señal')
axes[1].set_title('Predicciones vs Valores Reales')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

# Gráfica 3: Error de predicción
error = predicciones_test[:N_mostrar] - valores_reales[:N_mostrar]
axes[2].plot(error, color='green', alpha=0.7)
axes[2].axhline(y=0, color='black', linestyle='-', linewidth=0.5)
axes[2].fill_between(range(len(error)), error, alpha=0.3, color='green')
axes[2].set_xlabel('Paso temporal')
axes[2].set_ylabel('Error')
axes[2].set_title(f'Error de predicción (RMSE={rmse:.4f})')
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('lstm_prediccion_serie_temporal.png', dpi=150,
            bbox_inches='tight')
plt.show()
print("\nGráfica guardada en 'lstm_prediccion_serie_temporal.png'")
```

### 4.7.3 Análisis del código

Examinemos los aspectos más relevantes de la implementación:

**Preparación de datos con ventana deslizante**: La función `crear_secuencias` transforma una serie temporal en pares de entrenamiento supervisado. Para cada posición $i$, la entrada es el vector $\mathbf{x} = [s_i, s_{i+1}, \ldots, s_{i+L-1}]$ y el objetivo es $s_{i+L}$. La longitud de ventana $L=50$ determina cuántos pasos temporales pasados utiliza el modelo para predecir el siguiente valor. Esta elección debe balancear la capacidad de capturar dependencias a largo plazo con la eficiencia computacional.

**Arquitectura del modelo**: Utilizamos dos capas LSTM apiladas con $d_h = 64$. La primera capa recibe la secuencia de entrada y produce una secuencia de estados ocultos, que sirven como entrada para la segunda capa. Esto permite que el modelo aprenda representaciones jerárquicas de los patrones temporales. El dropout de 0.2 entre capas ayuda a prevenir el sobreajuste.

**Estado inicial**: Los estados $\mathbf{h}_0$ y $\mathbf{C}_0$ se inicializan a cero, que es la convención estándar. En PyTorch, la función `nn.LSTM` acepta opcionalmente los estados iniciales; si no se proporcionan, se inicializan a cero automáticamente.

**Predicción a partir del último estado oculto**: Para la predicción de series temporales, utilizamos solo el último estado oculto $\mathbf{h}_T$ de la capa superior. Esto se debe a que $\mathbf{h}_T$ resume la información de toda la secuencia de entrada. La capa fully-connected final transforma $\mathbf{h}_T \in \mathbb{R}^{64}$ en la predicción escalar $\hat{y} \in \mathbb{R}$.

**Recorte de gradientes**: La línea `clip_grad_norm_` implementa el recorte de gradientes discutido en la Sección 4.2.5, limitando la norma $L_2$ del vector de gradientes a 1.0. Esto previene la explosión de gradientes que puede ocurrir durante el entrenamiento de RNN/LSTM, especialmente con secuencias largas.

**Optimizador Adam**: Utilizamos el optimizador Adam, que adapta la tasa de aprendizaje individualmente para cada parámetro basándose en las estimaciones de los primeros dos momentos del gradiente. Adam es particularmente efectivo para el entrenamiento de RNN/LSTM, ya que maneja bien las superficies de error con curvaturas muy diferentes en distintas direcciones, que son comunes en estas arquitecturas.

### 4.7.4 Extensiones para comunicaciones semánticas

Este ejemplo básico de predicción de series temporales puede extenderse de múltiples maneras para aplicaciones en comunicaciones semánticas:

1. **Predicción de canal**: Reemplazando la señal sintética por mediciones reales de coeficientes de canal (por ejemplo, coeficientes de desvanecimiento en un canal de Rayleigh), la misma arquitectura puede utilizarse para predecir el estado futuro del canal, permitiendo la adaptación proactiva de los esquemas de modulación y codificación (*Adaptive Modulation and Coding*, AMC).

2. **Codificador semántico para series temporales**: La LSTM puede utilizarse como el codificador de un sistema de codificación conjunta fuente-canal (JSCC) para datos de series temporales. En este caso, el último estado oculto $\mathbf{h}_T$ actúa como la representación semántica comprimida de la secuencia de entrada, que se transmite a través del canal. El decodificador en el receptor utiliza otra LSTM para reconstruir la secuencia original.

3. **Detección de anomalías en comunicaciones**: El error de predicción de la LSTM puede utilizarse como indicador de anomalías: cuando la señal real difiere significativamente de la predicción, puede indicar interferencia, ataques maliciosos o cambios abruptos en las condiciones del canal.

---

## Referencias

- Elman, J. L. (1990). Finding structure in time. *Cognitive Science*, 14(2), 179–211. DOI: [10.1207/s15516709cog1402_1](https://doi.org/10.1207/s15516709cog1402_1)

- Hochreiter, S. (1991). *Untersuchungen zu dynamischen neuronalen Netzen*. Diploma thesis, Technische Universität München.

- Bengio, Y., Simard, P., & Frasconi, P. (1994). Learning long-term dependencies with gradient descent is difficult. *IEEE Transactions on Neural Networks*, 5(2), 157–166. DOI: [10.1109/72.279181](https://doi.org/10.1109/72.279181)

- Hochreiter, S., & Schmidhuber, J. (1997). Long short-term memory. *Neural Computation*, 9(8), 1735–1780. DOI: [10.1162/neco.1997.9.8.1735](https://doi.org/10.1162/neco.1997.9.8.1735)

- Schuster, M., & Paliwal, K. K. (1997). Bidirectional recurrent neural networks. *IEEE Transactions on Signal Processing*, 45(11), 2673–2681. DOI: [10.1109/78.650093](https://doi.org/10.1109/78.650093)

- Gers, F. A., Schmidhuber, J., & Cummins, F. (2000). Learning to forget: Continual prediction with LSTM. *Neural Computation*, 12(10), 2451–2471. DOI: [10.1162/089976600300015015](https://doi.org/10.1162/089976600300015015)

- Pascanu, R., Mikolov, T., & Bengio, Y. (2013). On the difficulty of training recurrent neural networks. *Proceedings of the 30th International Conference on Machine Learning (ICML)*, 1310–1318.

- Cho, K., van Merriënboer, B., Gulcehre, C., Bahdanau, D., Bougares, F., Schwenk, H., & Bengio, Y. (2014). Learning phrase representations using RNN encoder-decoder for statistical machine translation. *Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing (EMNLP)*, 1724–1734. DOI: [10.3115/v1/D14-1179](https://doi.org/10.3115/v1/D14-1179)

- Gal, Y., & Ghahramani, Z. (2016). A theoretically grounded application of dropout in recurrent neural networks. *Advances in Neural Information Processing Systems (NeurIPS)*, 29, 1019–1027.

- Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). Attention is all you need. *Advances in Neural Information Processing Systems (NeurIPS)*, 30, 5998–6008.
