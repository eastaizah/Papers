# 2. El Perceptrón Multicapa (MLP)

El perceptrón multicapa (*Multilayer Perceptron*, MLP) constituye una de las arquitecturas fundamentales del aprendizaje profundo y, en sentido estricto, la primera extensión práctica del perceptrón simple propuesto por Rosenblatt en 1958. Mientras que el perceptrón simple es capaz de resolver únicamente problemas linealmente separables, el MLP incorpora una o más capas ocultas de neuronas con funciones de activación no lineales, lo que le confiere la capacidad teórica de aproximar cualquier función continua definida sobre un subconjunto compacto de $\mathbb{R}^n$, resultado conocido como el *Teorema de Aproximación Universal* (Hornik, 1991, DOI: 10.1016/0893-6080(91)90009-T). En el contexto de las comunicaciones semánticas, los MLPs sirven como bloques constructivos esenciales dentro de codificadores y decodificadores semánticos, módulos de estimación de canal y componentes de sistemas extremo a extremo (*end-to-end*). Comprender su funcionamiento interno —desde la propagación hacia adelante hasta la retropropagación del error— es requisito indispensable para abordar arquitecturas más avanzadas como las redes convolucionales, recurrentes y los transformadores.

En esta sección se presenta la arquitectura del MLP, el algoritmo de retropropagación, las funciones de pérdida más utilizadas, los principales optimizadores, las técnicas de regularización y un ejemplo práctico completo de clasificación binaria implementado en PyTorch.

---

## 2.1 Arquitectura del MLP

### 2.1.1 Estructura general

Un perceptrón multicapa es una red neuronal artificial *feedforward* (de propagación hacia adelante) compuesta por múltiples capas de neuronas organizadas de forma jerárquica. La información fluye en una única dirección: desde la capa de entrada, a través de una o más capas ocultas, hasta la capa de salida. No existen conexiones recurrentes ni retroalimentación entre capas, lo cual distingue al MLP de las redes recurrentes que se estudiarán en secciones posteriores.

Formalmente, un MLP con $L$ capas se define mediante la siguiente estructura:

1. **Capa de entrada (capa 0):** Recibe el vector de características $\mathbf{x} \in \mathbb{R}^{n^{(0)}}$, donde $n^{(0)}$ denota la dimensionalidad del espacio de entrada. Esta capa no realiza ningún cómputo; simplemente distribuye los valores de entrada hacia las neuronas de la primera capa oculta. En el contexto de comunicaciones, $\mathbf{x}$ podría representar una señal recibida, un vector de símbolos modulados o una representación semántica de un mensaje.

2. **Capas ocultas (capas $1, 2, \ldots, L-1$):** Cada capa oculta $l$ contiene $n^{(l)}$ neuronas que aplican una transformación afín seguida de una función de activación no lineal. Estas capas son responsables de extraer representaciones intermedias (*features*) de complejidad creciente. La profundidad de la red (número de capas ocultas) y la anchura de cada capa (número de neuronas $n^{(l)}$) son hiperparámetros de diseño.

3. **Capa de salida (capa $L$):** Produce la predicción final $\hat{\mathbf{y}} \in \mathbb{R}^{n^{(L)}}$. La dimensión $n^{(L)}$ y la función de activación de esta capa dependen del tipo de problema: una neurona con activación sigmoide para clasificación binaria, $K$ neuronas con activación *softmax* para clasificación multiclase con $K$ categorías, o $n^{(L)}$ neuronas con activación lineal (identidad) para problemas de regresión.

### 2.1.2 Capas totalmente conectadas (densas)

En un MLP, cada capa es una capa *totalmente conectada* o *densa* (*fully connected* o *dense layer*), lo que significa que cada neurona de la capa $l$ está conectada con todas las neuronas de la capa $l-1$. Esto implica que la cantidad de parámetros entre dos capas consecutivas es $n^{(l)} \times n^{(l-1)}$ pesos más $n^{(l)}$ sesgos (*biases*), resultando en un total de $n^{(l)} \times (n^{(l-1)} + 1)$ parámetros por capa.

Esta conectividad completa permite al MLP capturar interacciones complejas entre todas las componentes de la entrada, pero también implica un crecimiento cuadrático del número de parámetros con respecto al tamaño de las capas. Esta limitación motivará, en secciones posteriores, el estudio de arquitecturas con conectividad estructurada como las redes convolucionales.

### 2.1.3 Notación formal

Para describir de manera precisa las operaciones del MLP, adoptamos la siguiente notación que se utilizará de forma consistente a lo largo de este tutorial:

- $L$: número total de capas (sin contar la capa de entrada). Un MLP con una capa oculta tiene $L = 2$.
- $l \in \{1, 2, \ldots, L\}$: índice de capa.
- $n^{(l)}$: número de neuronas en la capa $l$. En particular, $n^{(0)}$ es la dimensión de la entrada.
- $\mathbf{W}^{(l)} \in \mathbb{R}^{n^{(l)} \times n^{(l-1)}}$: matriz de pesos de la capa $l$. El elemento $W_{ij}^{(l)}$ representa el peso de la conexión desde la neurona $j$ de la capa $l-1$ hasta la neurona $i$ de la capa $l$.
- $\mathbf{b}^{(l)} \in \mathbb{R}^{n^{(l)}}$: vector de sesgos (*biases*) de la capa $l$.
- $\mathbf{z}^{(l)} \in \mathbb{R}^{n^{(l)}}$: vector de pre-activaciones de la capa $l$ (salida de la transformación afín, antes de aplicar la función de activación).
- $\mathbf{a}^{(l)} \in \mathbb{R}^{n^{(l)}}$: vector de activaciones de la capa $l$ (salida después de aplicar la función de activación). Se define $\mathbf{a}^{(0)} = \mathbf{x}$ para la capa de entrada.
- $f(\cdot)$: función de activación (puede variar entre capas, en cuyo caso se escribe $f^{(l)}(\cdot)$).

### 2.1.4 Propagación hacia adelante (*Forward Pass*)

La propagación hacia adelante describe el proceso mediante el cual un vector de entrada $\mathbf{x}$ es transformado sucesivamente por cada capa de la red hasta producir la salida $\hat{\mathbf{y}}$. Para cada capa $l = 1, 2, \ldots, L$, se realizan dos operaciones:

**Paso 1 — Transformación afín:** Se calcula la combinación lineal ponderada de las activaciones de la capa anterior más el sesgo:

$$\mathbf{z}^{(l)} = \mathbf{W}^{(l)} \mathbf{a}^{(l-1)} + \mathbf{b}^{(l)}$$

donde $\mathbf{W}^{(l)} \in \mathbb{R}^{n^{(l)} \times n^{(l-1)}}$ es la matriz de pesos, $\mathbf{a}^{(l-1)} \in \mathbb{R}^{n^{(l-1)}}$ es el vector de activaciones de la capa previa y $\mathbf{b}^{(l)} \in \mathbb{R}^{n^{(l)}}$ es el vector de sesgos. El vector resultante $\mathbf{z}^{(l)} \in \mathbb{R}^{n^{(l)}}$ se denomina *pre-activación* o *logit*.

En forma componente a componente, la pre-activación de la neurona $i$ en la capa $l$ se escribe como:

$$z_i^{(l)} = \sum_{j=1}^{n^{(l-1)}} W_{ij}^{(l)} a_j^{(l-1)} + b_i^{(l)}$$

Esta expresión es simplemente un producto punto entre la fila $i$ de la matriz de pesos y el vector de activaciones de la capa anterior, más el sesgo correspondiente.

**Paso 2 — Activación no lineal:** Se aplica la función de activación elemento a elemento:

$$\mathbf{a}^{(l)} = f(\mathbf{z}^{(l)})$$

o equivalentemente, $a_i^{(l)} = f(z_i^{(l)})$ para cada neurona $i$. La función de activación introduce la no linealidad necesaria para que la red pueda representar funciones complejas. Sin ella, la composición de transformaciones afines seguiría siendo una transformación afín, y el MLP sería equivalente a una regresión lineal independientemente de su profundidad.

La propagación completa se resume como la composición:

$$\hat{\mathbf{y}} = \mathbf{a}^{(L)} = f^{(L)}\left(\mathbf{W}^{(L)} f^{(L-1)}\left(\cdots f^{(1)}\left(\mathbf{W}^{(1)} \mathbf{x} + \mathbf{b}^{(1)}\right) \cdots\right) + \mathbf{b}^{(L)}\right)$$

Las funciones de activación más comunes ya fueron presentadas en la Sección 1. En resumen, las capas ocultas suelen emplear ReLU ($f(z) = \max(0, z)$) o variantes como Leaky ReLU o GELU, mientras que la capa de salida utiliza la activación apropiada al problema: sigmoide para clasificación binaria, softmax para clasificación multiclase, o identidad para regresión.

### 2.1.5 Diagrama de un MLP de tres capas

**Figura 2.1:** *Diagrama esquemático de un perceptrón multicapa con tres capas: una capa de entrada con $n^{(0)} = 3$ neuronas (representadas como nodos circulares en la columna izquierda, etiquetados como $x_1$, $x_2$, $x_3$), una capa oculta con $n^{(1)} = 4$ neuronas (nodos en la columna central, etiquetados como $a_1^{(1)}$, $a_2^{(1)}$, $a_3^{(1)}$, $a_4^{(1)}$) y una capa de salida con $n^{(2)} = 2$ neuronas (nodos en la columna derecha, etiquetados como $\hat{y}_1$, $\hat{y}_2$). Cada neurona de la capa de entrada está conectada mediante flechas dirigidas a todas las neuronas de la capa oculta; estas flechas representan los pesos $W_{ij}^{(1)}$. Análogamente, cada neurona de la capa oculta está conectada con todas las neuronas de la capa de salida mediante flechas con pesos $W_{ij}^{(2)}$. Debajo de cada capa oculta y de salida se indica el sesgo $\mathbf{b}^{(l)}$ como una entrada adicional constante. Las flechas fluyen de izquierda a derecha, ilustrando la propagación hacia adelante de la información. A la derecha de cada neurona oculta se anota la función de activación $f(\cdot)$, y al lado de las neuronas de salida se indica la activación de salida (por ejemplo, softmax). El diagrama resalta la conectividad completa entre capas adyacentes y la ausencia de conexiones dentro de una misma capa o entre capas no adyacentes.*

### 2.1.6 Ejemplo numérico detallado

Consideremos un MLP sencillo con la siguiente arquitectura:
- **Capa de entrada:** $n^{(0)} = 2$ (dos características de entrada)
- **Capa oculta:** $n^{(1)} = 2$ (dos neuronas con activación sigmoide)
- **Capa de salida:** $n^{(2)} = 1$ (una neurona con activación sigmoide, para clasificación binaria)

Definamos los siguientes parámetros:

$$\mathbf{W}^{(1)} = \begin{pmatrix} 0.15 & 0.20 \\ 0.25 & 0.30 \end{pmatrix}, \quad \mathbf{b}^{(1)} = \begin{pmatrix} 0.35 \\ 0.35 \end{pmatrix}$$

$$\mathbf{W}^{(2)} = \begin{pmatrix} 0.40 & 0.45 \end{pmatrix}, \quad b^{(2)} = 0.60$$

Y sea el vector de entrada:

$$\mathbf{x} = \mathbf{a}^{(0)} = \begin{pmatrix} 0.05 \\ 0.10 \end{pmatrix}$$

La función de activación utilizada en todas las capas es la sigmoide:

$$\sigma(z) = \frac{1}{1 + e^{-z}}$$

**Paso 1: Cálculo de las pre-activaciones de la capa oculta**

$$\mathbf{z}^{(1)} = \mathbf{W}^{(1)} \mathbf{a}^{(0)} + \mathbf{b}^{(1)}$$

Desarrollando componente a componente:

$$z_1^{(1)} = W_{11}^{(1)} \cdot a_1^{(0)} + W_{12}^{(1)} \cdot a_2^{(0)} + b_1^{(1)}$$
$$z_1^{(1)} = 0.15 \times 0.05 + 0.20 \times 0.10 + 0.35 = 0.0075 + 0.0200 + 0.35 = 0.3775$$

$$z_2^{(1)} = W_{21}^{(1)} \cdot a_1^{(0)} + W_{22}^{(1)} \cdot a_2^{(0)} + b_2^{(1)}$$
$$z_2^{(1)} = 0.25 \times 0.05 + 0.30 \times 0.10 + 0.35 = 0.0125 + 0.0300 + 0.35 = 0.3925$$

**Paso 2: Cálculo de las activaciones de la capa oculta**

$$a_1^{(1)} = \sigma(z_1^{(1)}) = \sigma(0.3775) = \frac{1}{1 + e^{-0.3775}} = \frac{1}{1 + 0.6856} = \frac{1}{1.6856} \approx 0.5933$$

$$a_2^{(1)} = \sigma(z_2^{(1)}) = \sigma(0.3925) = \frac{1}{1 + e^{-0.3925}} = \frac{1}{1 + 0.6753} = \frac{1}{1.6753} \approx 0.5969$$

**Paso 3: Cálculo de la pre-activación de la capa de salida**

$$z^{(2)} = \mathbf{W}^{(2)} \mathbf{a}^{(1)} + b^{(2)}$$
$$z^{(2)} = 0.40 \times 0.5933 + 0.45 \times 0.5969 + 0.60$$
$$z^{(2)} = 0.2373 + 0.2686 + 0.60 = 1.1059$$

**Paso 4: Cálculo de la activación de la capa de salida**

$$\hat{y} = a^{(2)} = \sigma(z^{(2)}) = \sigma(1.1059) = \frac{1}{1 + e^{-1.1059}} = \frac{1}{1 + 0.3313} \approx 0.7514$$

La red predice $\hat{y} \approx 0.7514$. Si la etiqueta verdadera fuera $y = 1$ (clase positiva), la red estaría acercándose al valor correcto pero aún no es precisa. Si la etiqueta fuera $y = 0$, la predicción sería bastante errónea. En la subsección siguiente, veremos cómo el algoritmo de retropropagación calcula los gradientes necesarios para ajustar los pesos y reducir el error.

Este ejemplo, aunque sencillo, ilustra la mecánica fundamental del *forward pass*: cada capa toma las activaciones de la capa anterior, aplica una transformación afín (producto matricial más sesgo) y luego una no linealidad. La composición de estas operaciones permite a la red construir funciones de decisión complejas a partir de operaciones elementales.

---

## 2.2 Retropropagación del error (*Backpropagation*)

### 2.2.1 Motivación y contexto histórico

El algoritmo de retropropagación del error (*backpropagation*), popularizado por Rumelhart, Hinton y Williams (1986, DOI: 10.1038/323533a0), es el mecanismo central mediante el cual las redes neuronales aprenden. Su objetivo es calcular de manera eficiente el gradiente de la función de pérdida con respecto a cada uno de los parámetros de la red (pesos y sesgos), de modo que estos puedan ser actualizados en la dirección que reduce el error.

En esencia, la retropropagación es una aplicación sistemática de la **regla de la cadena** del cálculo diferencial multivariable. El nombre "retropropagación" refleja el hecho de que los gradientes se calculan comenzando desde la capa de salida y propagándose hacia atrás (*backward*) a través de la red, capa por capa, hasta la capa de entrada.

### 2.2.2 La regla de la cadena en detalle

Recordemos que la regla de la cadena establece que si $y = f(g(x))$, entonces:

$$\frac{dy}{dx} = \frac{dy}{dg} \cdot \frac{dg}{dx} = f'(g(x)) \cdot g'(x)$$

En el contexto de una red neuronal, queremos calcular $\frac{\partial L}{\partial W_{ij}^{(l)}}$ para cada peso $W_{ij}^{(l)}$ de la red, donde $L$ es la función de pérdida. Dado que la pérdida depende de la salida de la red, que a su vez depende de las activaciones de las capas intermedias, que dependen de las pre-activaciones, que dependen de los pesos, la regla de la cadena nos permite descomponer esta derivada en un producto de derivadas parciales más simples:

$$\frac{\partial L}{\partial W_{ij}^{(l)}} = \frac{\partial L}{\partial z_i^{(l)}} \cdot \frac{\partial z_i^{(l)}}{\partial W_{ij}^{(l)}}$$

Para simplificar la notación, definimos el **error local** o **delta** de la neurona $i$ en la capa $l$ como:

$$\delta_i^{(l)} \equiv \frac{\partial L}{\partial z_i^{(l)}}$$

Este término $\delta_i^{(l)}$ cuantifica cuánto contribuye la pre-activación $z_i^{(l)}$ al error total. En notación vectorial, el vector de deltas de la capa $l$ es:

$$\boldsymbol{\delta}^{(l)} = \frac{\partial L}{\partial \mathbf{z}^{(l)}} \in \mathbb{R}^{n^{(l)}}$$

La clave de la retropropagación es que los deltas pueden calcularse de forma recursiva, comenzando por la capa de salida y retrocediendo hacia la entrada.

### 2.2.3 Cálculo de los deltas

**Delta de la capa de salida ($l = L$):**

Para la capa de salida, el delta se calcula directamente a partir de la derivada de la función de pérdida con respecto a las activaciones de salida y la derivada de la función de activación:

$$\boldsymbol{\delta}^{(L)} = \frac{\partial L}{\partial \mathbf{a}^{(L)}} \odot f'(\mathbf{z}^{(L)})$$

donde $\odot$ denota el producto de Hadamard (producto elemento a elemento) y $f'(\mathbf{z}^{(L)})$ es la derivada de la función de activación evaluada en las pre-activaciones de la capa de salida. Este resultado se obtiene aplicando la regla de la cadena:

$$\delta_i^{(L)} = \frac{\partial L}{\partial a_i^{(L)}} \cdot \frac{\partial a_i^{(L)}}{\partial z_i^{(L)}} = \frac{\partial L}{\partial a_i^{(L)}} \cdot f'(z_i^{(L)})$$

La forma específica de $\frac{\partial L}{\partial a_i^{(L)}}$ depende de la función de pérdida utilizada. Por ejemplo, para el error cuadrático medio, esta derivada es proporcional a $(a_i^{(L)} - y_i)$; para la entropía cruzada combinada con una activación sigmoide o softmax, la expresión se simplifica notablemente, como veremos más adelante.

**Delta de las capas ocultas ($l = L-1, L-2, \ldots, 1$):**

Para las capas ocultas, el delta se calcula de forma recursiva a partir de los deltas de la capa siguiente:

$$\boldsymbol{\delta}^{(l)} = \left(\mathbf{W}^{(l+1)}\right)^T \boldsymbol{\delta}^{(l+1)} \odot f'(\mathbf{z}^{(l)})$$

Esta ecuación es el corazón de la retropropagación. Vamos a desglosarla:

1. $\boldsymbol{\delta}^{(l+1)} \in \mathbb{R}^{n^{(l+1)}}$: el vector de deltas de la capa siguiente, que ya fue calculado en la iteración anterior del algoritmo (o directamente si $l+1 = L$).

2. $\left(\mathbf{W}^{(l+1)}\right)^T \in \mathbb{R}^{n^{(l)} \times n^{(l+1)}}$: la transpuesta de la matriz de pesos de la capa siguiente. Este producto $\left(\mathbf{W}^{(l+1)}\right)^T \boldsymbol{\delta}^{(l+1)}$ distribuye (*propaga hacia atrás*) el error de la capa $l+1$ hacia cada neurona de la capa $l$, ponderado por los pesos de las conexiones. Intuitivamente, si el peso $W_{ji}^{(l+1)}$ es grande, entonces la neurona $i$ de la capa $l$ tiene una gran influencia sobre la neurona $j$ de la capa $l+1$, y por tanto hereda una porción proporcional de su error.

3. $f'(\mathbf{z}^{(l)})$: la derivada de la función de activación evaluada en las pre-activaciones de la capa $l$. Este factor modula el error retropropagado según la "sensibilidad" local de la activación. Si la neurona está en una zona de saturación (por ejemplo, en los extremos de la sigmoide, donde $f'(z) \approx 0$), el gradiente se atenúa fuertemente, fenómeno conocido como **desvanecimiento del gradiente** (*vanishing gradient*).

4. $\odot$: el producto de Hadamard garantiza que la modulación se realice elemento a elemento, pues cada neurona tiene su propia pre-activación.

En forma componente a componente, la ecuación recursiva se escribe:

$$\delta_i^{(l)} = \left(\sum_{j=1}^{n^{(l+1)}} W_{ji}^{(l+1)} \delta_j^{(l+1)}\right) \cdot f'(z_i^{(l)})$$

Esta expresión muestra que el delta de la neurona $i$ en la capa $l$ es la suma ponderada de los deltas de todas las neuronas de la capa $l+1$ (ponderada por los pesos de las conexiones), multiplicada por la derivada local de la activación.

### 2.2.4 Gradientes de los pesos y sesgos

Una vez calculados todos los deltas, los gradientes de la función de pérdida con respecto a los pesos y sesgos se obtienen directamente:

**Gradiente respecto a los pesos:**

$$\frac{\partial L}{\partial \mathbf{W}^{(l)}} = \boldsymbol{\delta}^{(l)} \left(\mathbf{a}^{(l-1)}\right)^T$$

donde $\boldsymbol{\delta}^{(l)} \in \mathbb{R}^{n^{(l)}}$ y $\left(\mathbf{a}^{(l-1)}\right)^T \in \mathbb{R}^{1 \times n^{(l-1)}}$, de modo que el producto exterior resulta en una matriz de dimensiones $n^{(l)} \times n^{(l-1)}$, que son exactamente las mismas dimensiones que $\mathbf{W}^{(l)}$. En forma componente a componente:

$$\frac{\partial L}{\partial W_{ij}^{(l)}} = \delta_i^{(l)} \cdot a_j^{(l-1)}$$

Esta expresión tiene una interpretación elegante: el gradiente de un peso es el producto del error de la neurona destino por la activación de la neurona origen. Si ambos valores son grandes, el peso tiene una gran influencia en el error y debe ser ajustado significativamente.

**Gradiente respecto a los sesgos:**

$$\frac{\partial L}{\partial \mathbf{b}^{(l)}} = \boldsymbol{\delta}^{(l)}$$

Es decir, el gradiente del sesgo es simplemente el delta correspondiente. Esto se debe a que $\frac{\partial z_i^{(l)}}{\partial b_i^{(l)}} = 1$, ya que el sesgo aparece como un sumando aditivo en la pre-activación.

### 2.2.5 Algoritmo completo de retropropagación

El algoritmo completo se puede resumir en los siguientes pasos:

1. **Propagación hacia adelante:** Para $l = 1, 2, \ldots, L$, calcular $\mathbf{z}^{(l)} = \mathbf{W}^{(l)} \mathbf{a}^{(l-1)} + \mathbf{b}^{(l)}$ y $\mathbf{a}^{(l)} = f(\mathbf{z}^{(l)})$. Almacenar todos los valores intermedios $\mathbf{z}^{(l)}$ y $\mathbf{a}^{(l)}$.

2. **Cálculo del delta de la capa de salida:** $\boldsymbol{\delta}^{(L)} = \frac{\partial L}{\partial \mathbf{a}^{(L)}} \odot f'(\mathbf{z}^{(L)})$.

3. **Retropropagación de los deltas:** Para $l = L-1, L-2, \ldots, 1$, calcular $\boldsymbol{\delta}^{(l)} = \left(\mathbf{W}^{(l+1)}\right)^T \boldsymbol{\delta}^{(l+1)} \odot f'(\mathbf{z}^{(l)})$.

4. **Cálculo de los gradientes:** Para cada capa $l$, calcular $\frac{\partial L}{\partial \mathbf{W}^{(l)}} = \boldsymbol{\delta}^{(l)} \left(\mathbf{a}^{(l-1)}\right)^T$ y $\frac{\partial L}{\partial \mathbf{b}^{(l)}} = \boldsymbol{\delta}^{(l)}$.

5. **Actualización de parámetros:** Aplicar la regla de actualización del optimizador (por ejemplo, descenso de gradiente: $\mathbf{W}^{(l)} \leftarrow \mathbf{W}^{(l)} - \eta \frac{\partial L}{\partial \mathbf{W}^{(l)}}$).

### 2.2.6 Ejemplo numérico completo de retropropagación

Continuemos con el ejemplo de la Subsección 2.1.6. Recordemos los resultados del *forward pass*:

- Entrada: $\mathbf{x} = (0.05, 0.10)^T$
- Activaciones de la capa oculta: $a_1^{(1)} = 0.5933$, $a_2^{(1)} = 0.5969$
- Pre-activaciones de la capa oculta: $z_1^{(1)} = 0.3775$, $z_2^{(1)} = 0.3925$
- Pre-activación de la salida: $z^{(2)} = 1.1059$
- Salida: $\hat{y} = a^{(2)} = 0.7514$

Supongamos que la etiqueta verdadera es $y = 1$ y utilizamos la función de pérdida de **error cuadrático medio** (para una sola muestra):

$$L = \frac{1}{2}(y - \hat{y})^2 = \frac{1}{2}(1 - 0.7514)^2 = \frac{1}{2}(0.2486)^2 = \frac{1}{2}(0.0618) = 0.0309$$

Nota: usamos el factor $\frac{1}{2}$ en lugar de $\frac{1}{N}$ para simplificar las derivadas.

**Paso 1: Delta de la capa de salida**

$$\delta^{(2)} = \frac{\partial L}{\partial a^{(2)}} \cdot f'(z^{(2)})$$

La derivada de la pérdida MSE (con factor $\frac{1}{2}$) respecto a la activación de salida:

$$\frac{\partial L}{\partial a^{(2)}} = -(y - \hat{y}) = -(1 - 0.7514) = -0.2486$$

La derivada de la sigmoide es $\sigma'(z) = \sigma(z)(1 - \sigma(z))$:

$$f'(z^{(2)}) = \sigma'(1.1059) = 0.7514 \times (1 - 0.7514) = 0.7514 \times 0.2486 = 0.1868$$

Por lo tanto:

$$\delta^{(2)} = -0.2486 \times 0.1868 = -0.0464$$

El signo negativo indica que la pre-activación debería *aumentar* para reducir el error (la salida actual es menor que el valor objetivo).

**Paso 2: Gradientes de $\mathbf{W}^{(2)}$ y $b^{(2)}$**

$$\frac{\partial L}{\partial W_{11}^{(2)}} = \delta^{(2)} \cdot a_1^{(1)} = -0.0464 \times 0.5933 = -0.0275$$

$$\frac{\partial L}{\partial W_{12}^{(2)}} = \delta^{(2)} \cdot a_2^{(1)} = -0.0464 \times 0.5969 = -0.0277$$

$$\frac{\partial L}{\partial b^{(2)}} = \delta^{(2)} = -0.0464$$

**Paso 3: Deltas de la capa oculta**

$$\boldsymbol{\delta}^{(1)} = \left(\mathbf{W}^{(2)}\right)^T \delta^{(2)} \odot f'(\mathbf{z}^{(1)})$$

Primero, calculamos $\left(\mathbf{W}^{(2)}\right)^T \delta^{(2)}$:

$$\left(\mathbf{W}^{(2)}\right)^T \delta^{(2)} = \begin{pmatrix} 0.40 \\ 0.45 \end{pmatrix} \times (-0.0464) = \begin{pmatrix} -0.0186 \\ -0.0209 \end{pmatrix}$$

Ahora calculamos las derivadas de la sigmoide para la capa oculta:

$$f'(z_1^{(1)}) = \sigma(0.3775)(1 - \sigma(0.3775)) = 0.5933 \times 0.4067 = 0.2413$$

$$f'(z_2^{(1)}) = \sigma(0.3925)(1 - \sigma(0.3925)) = 0.5969 \times 0.4031 = 0.2406$$

Aplicamos el producto de Hadamard:

$$\delta_1^{(1)} = -0.0186 \times 0.2413 = -0.0045$$

$$\delta_2^{(1)} = -0.0209 \times 0.2406 = -0.0050$$

**Paso 4: Gradientes de $\mathbf{W}^{(1)}$ y $\mathbf{b}^{(1)}$**

$$\frac{\partial L}{\partial W_{11}^{(1)}} = \delta_1^{(1)} \cdot a_1^{(0)} = -0.0045 \times 0.05 = -0.000225$$

$$\frac{\partial L}{\partial W_{12}^{(1)}} = \delta_1^{(1)} \cdot a_2^{(0)} = -0.0045 \times 0.10 = -0.000450$$

$$\frac{\partial L}{\partial W_{21}^{(1)}} = \delta_2^{(1)} \cdot a_1^{(0)} = -0.0050 \times 0.05 = -0.000250$$

$$\frac{\partial L}{\partial W_{22}^{(1)}} = \delta_2^{(1)} \cdot a_2^{(0)} = -0.0050 \times 0.10 = -0.000500$$

$$\frac{\partial L}{\partial \mathbf{b}^{(1)}} = \boldsymbol{\delta}^{(1)} = \begin{pmatrix} -0.0045 \\ -0.0050 \end{pmatrix}$$

**Paso 5: Actualización de pesos (con tasa de aprendizaje $\eta = 0.5$)**

$$W_{11}^{(2)} \leftarrow 0.40 - 0.5 \times (-0.0275) = 0.40 + 0.0138 = 0.4138$$

$$W_{12}^{(2)} \leftarrow 0.45 - 0.5 \times (-0.0277) = 0.45 + 0.0139 = 0.4639$$

$$b^{(2)} \leftarrow 0.60 - 0.5 \times (-0.0464) = 0.60 + 0.0232 = 0.6232$$

Y de manera análoga para los pesos de la capa oculta. Obsérvese cómo todos los gradientes son negativos (porque la salida debe aumentar para acercarse a $y=1$), lo que hace que los pesos *aumenten* tras la actualización, incrementando así la salida de la red en la dirección correcta.

### 2.2.7 Diagrama del flujo de gradientes

**Figura 2.2:** *Diagrama del flujo de gradientes en la retropropagación para el MLP de dos capas del ejemplo. La parte superior muestra la propagación hacia adelante (de izquierda a derecha): la entrada $\mathbf{x}$ fluye a través de $\mathbf{W}^{(1)}$, pasa por la función de activación $\sigma(\cdot)$ para producir $\mathbf{a}^{(1)}$, luego a través de $\mathbf{W}^{(2)}$ y $\sigma(\cdot)$ para producir $\hat{y}$, y finalmente se compara con $y$ mediante la función de pérdida $L$. La parte inferior muestra la retropropagación (de derecha a izquierda): desde $L$, se calcula $\frac{\partial L}{\partial a^{(2)}}$, luego se multiplica por $f'(z^{(2)})$ para obtener $\delta^{(2)}$, el cual se propaga hacia atrás a través de $(\mathbf{W}^{(2)})^T$ y se modula por $f'(\mathbf{z}^{(1)})$ para obtener $\boldsymbol{\delta}^{(1)}$. En cada etapa, flechas laterales descendentes muestran cómo los deltas se combinan con las activaciones de la capa anterior para producir los gradientes $\frac{\partial L}{\partial \mathbf{W}^{(l)}}$. Las flechas de retropropagación se dibujan en rojo para distinguirlas de las flechas azules de la propagación hacia adelante. Se anotan las dimensiones de cada tensor en cada punto del diagrama.*

---

## 2.3 Funciones de pérdida

La función de pérdida (*loss function*), también denominada función de costo o función objetivo, cuantifica la discrepancia entre las predicciones del modelo $\hat{\mathbf{y}}$ y las etiquetas verdaderas $\mathbf{y}$. La elección de la función de pérdida apropiada es crucial, pues define el paisaje de optimización que el algoritmo de entrenamiento debe navegar. En esta subsección describimos las funciones de pérdida más utilizadas en aprendizaje profundo.

### 2.3.1 Error cuadrático medio (MSE)

El error cuadrático medio (*Mean Squared Error*, MSE) es la función de pérdida estándar para problemas de **regresión**, donde la salida del modelo es un valor continuo. Se define como:

$$L_{\text{MSE}} = \frac{1}{N} \sum_{i=1}^{N} (y_i - \hat{y}_i)^2$$

donde $N$ es el número de muestras en el *batch*, $y_i$ es el valor objetivo para la muestra $i$ y $\hat{y}_i$ es la predicción correspondiente del modelo. El MSE penaliza los errores de forma cuadrática: errores grandes reciben una penalización desproporcionadamente mayor que errores pequeños. Esta propiedad tiene ventajas e inconvenientes. Por un lado, incentiva al modelo a evitar errores grandes; por otro, hace que la pérdida sea sensible a valores atípicos (*outliers*).

La derivada del MSE respecto a una predicción individual es:

$$\frac{\partial L_{\text{MSE}}}{\partial \hat{y}_i} = -\frac{2}{N}(y_i - \hat{y}_i)$$

Esta derivada es proporcional al error residual, lo que da lugar a gradientes que son mayores cuando las predicciones están lejos de los objetivos (actualizaciones más agresivas) y menores cuando las predicciones son cercanas (actualizaciones más finas), un comportamiento deseable para la convergencia.

En comunicaciones semánticas, el MSE se utiliza frecuentemente para medir la fidelidad de la reconstrucción en sistemas que transmiten representaciones continuas, por ejemplo, la calidad de una imagen reconstruida tras la transmisión a través de un canal ruidoso.

Una variante común es la **raíz del error cuadrático medio** (RMSE, $\sqrt{L_{\text{MSE}}}$), que tiene la ventaja de estar en las mismas unidades que la variable objetivo. Otra variante es el **error absoluto medio** (MAE, $\frac{1}{N}\sum |y_i - \hat{y}_i|$), que es más robusto ante outliers pero cuyo gradiente es constante en magnitud, lo que puede dificultar la convergencia cerca del mínimo.

### 2.3.2 Entropía cruzada binaria (BCE)

La entropía cruzada binaria (*Binary Cross-Entropy*, BCE) es la función de pérdida estándar para problemas de **clasificación binaria**, donde la salida del modelo es una probabilidad $\hat{y}_i \in (0, 1)$ de que la muestra pertenezca a la clase positiva. Se define como:

$$L_{\text{BCE}} = -\frac{1}{N} \sum_{i=1}^{N} \left[ y_i \log(\hat{y}_i) + (1 - y_i) \log(1 - \hat{y}_i) \right]$$

donde $y_i \in \{0, 1\}$ es la etiqueta verdadera de la muestra $i$.

Para comprender esta función, analicemos sus dos términos:

- Cuando $y_i = 1$ (la muestra pertenece a la clase positiva), el segundo término se anula y la pérdida es $-\log(\hat{y}_i)$. Si el modelo predice $\hat{y}_i$ cercano a 1 (predicción correcta con alta confianza), $-\log(\hat{y}_i) \approx 0$ (pérdida baja). Si predice $\hat{y}_i$ cercano a 0 (predicción incorrecta), $-\log(\hat{y}_i) \to \infty$ (pérdida muy alta). La función logarítmica penaliza de forma extremadamente severa las predicciones confiantes pero erróneas.

- Cuando $y_i = 0$ (la muestra pertenece a la clase negativa), el primer término se anula y la pérdida es $-\log(1 - \hat{y}_i)$. Análogamente, se penaliza al modelo si predice $\hat{y}_i$ cercano a 1 cuando la clase verdadera es 0.

La derivada de la BCE respecto a una predicción individual es:

$$\frac{\partial L_{\text{BCE}}}{\partial \hat{y}_i} = -\frac{1}{N} \left(\frac{y_i}{\hat{y}_i} - \frac{1 - y_i}{1 - \hat{y}_i}\right)$$

Cuando la capa de salida utiliza una activación sigmoide ($\hat{y}_i = \sigma(z_i)$), la combinación de BCE y sigmoide produce un gradiente particularmente limpio para el delta de la capa de salida:

$$\delta_i^{(L)} = \frac{\partial L_{\text{BCE}}}{\partial z_i} = \frac{1}{N}(\hat{y}_i - y_i)$$

Esta simplificación evita el problema de saturación de la sigmoide en los gradientes y es una de las razones por las que la combinación BCE + sigmoide es preferida sobre MSE + sigmoide para clasificación binaria.

La BCE tiene una interpretación desde la teoría de la información: es la entropía cruzada entre la distribución verdadera $p = (y_i, 1-y_i)$ y la distribución predicha $q = (\hat{y}_i, 1-\hat{y}_i)$. Minimizar la BCE equivale a minimizar la divergencia de Kullback-Leibler entre ambas distribuciones, lo que tiene una conexión directa con la eficiencia de codificación en comunicaciones.

### 2.3.3 Entropía cruzada categórica

Para problemas de **clasificación multiclase** con $K$ clases mutuamente excluyentes, la entropía cruzada categórica (*Categorical Cross-Entropy*, CCE) generaliza la BCE. La etiqueta verdadera se representa como un vector *one-hot* $\mathbf{y}_i \in \{0, 1\}^K$ con $\sum_k y_{ik} = 1$, y la salida del modelo es un vector de probabilidades $\hat{\mathbf{y}}_i \in (0, 1)^K$ con $\sum_k \hat{y}_{ik} = 1$, típicamente obtenido mediante la función softmax:

$$\hat{y}_{ik} = \text{softmax}(z_{ik}) = \frac{e^{z_{ik}}}{\sum_{j=1}^{K} e^{z_{ij}}}$$

La función de pérdida se define como:

$$L_{\text{CCE}} = -\frac{1}{N} \sum_{i=1}^{N} \sum_{k=1}^{K} y_{ik} \log(\hat{y}_{ik})$$

Dado que $\mathbf{y}_i$ es *one-hot*, solo el término correspondiente a la clase verdadera $c_i$ contribuye a la suma sobre $k$:

$$L_{\text{CCE}} = -\frac{1}{N} \sum_{i=1}^{N} \log(\hat{y}_{i, c_i})$$

Es decir, la pérdida mide el logaritmo negativo de la probabilidad asignada por el modelo a la clase correcta. Un modelo perfecto asigna probabilidad 1 a la clase correcta, obteniendo pérdida 0. La combinación de softmax con CCE también produce gradientes limpios:

$$\delta_k^{(L)} = \hat{y}_k - y_k$$

lo que facilita la optimización y evita problemas numéricos.

### 2.3.4 Criterios de selección

La selección de la función de pérdida debe alinearse con la naturaleza del problema:

| Problema | Función de pérdida | Activación de salida |
|---|---|---|
| Regresión | MSE (o MAE, Huber) | Lineal (identidad) |
| Clasificación binaria | Entropía cruzada binaria | Sigmoide |
| Clasificación multiclase | Entropía cruzada categórica | Softmax |
| Clasificación multi-etiqueta | BCE (por cada etiqueta) | Sigmoide (por cada etiqueta) |

En el contexto de las comunicaciones semánticas, la elección de la función de pérdida es particularmente relevante porque define qué aspecto de la información transmitida se prioriza preservar. Un sistema que utiliza MSE prioriza la fidelidad numérica de la reconstrucción, mientras que un sistema con entropía cruzada prioriza la preservación del contenido semántico (categorías, clases). Algunas arquitecturas avanzadas combinan múltiples funciones de pérdida —por ejemplo, un término de reconstrucción MSE más un término de clasificación de entropía cruzada— para balancear fidelidad perceptual y semántica.

---

## 2.4 Optimizadores

Los optimizadores son los algoritmos encargados de ajustar los parámetros $\boldsymbol{\theta} = \{\mathbf{W}^{(l)}, \mathbf{b}^{(l)}\}_{l=1}^{L}$ de la red neuronal con el objetivo de minimizar la función de pérdida $L(\boldsymbol{\theta})$. Todos se basan en el principio del descenso de gradiente, pero difieren en cómo utilizan la información del gradiente para determinar la dirección y magnitud de las actualizaciones.

### 2.4.1 Descenso de gradiente estocástico (SGD)

El descenso de gradiente estocástico (*Stochastic Gradient Descent*, SGD) es la forma más básica de optimización. En el **descenso de gradiente por lotes** (*batch gradient descent*), el gradiente se calcula sobre todo el conjunto de entrenamiento antes de actualizar los parámetros:

$$\boldsymbol{\theta}_{t+1} = \boldsymbol{\theta}_t - \eta \nabla_{\boldsymbol{\theta}} L(\boldsymbol{\theta}_t)$$

donde $\eta > 0$ es la **tasa de aprendizaje** (*learning rate*), un hiperparámetro fundamental que controla el tamaño del paso de actualización, y $\nabla_{\boldsymbol{\theta}} L(\boldsymbol{\theta}_t)$ es el gradiente de la función de pérdida evaluado en los parámetros actuales.

En la versión **estocástica**, el gradiente se estima utilizando un solo ejemplo o un subconjunto pequeño (*mini-batch*) de $B$ ejemplos seleccionados aleatoriamente:

$$\boldsymbol{\theta}_{t+1} = \boldsymbol{\theta}_t - \eta \frac{1}{B} \sum_{i=1}^{B} \nabla_{\boldsymbol{\theta}} L_i(\boldsymbol{\theta}_t)$$

El SGD estocástico introduce ruido en la estimación del gradiente, lo cual puede parecer desventajoso pero en la práctica ofrece varios beneficios: permite un entrenamiento más rápido (no es necesario procesar todo el dataset para cada actualización), puede escapar de mínimos locales superficiales gracias al ruido, y requiere menos memoria.

La elección de la tasa de aprendizaje $\eta$ es crítica:
- Si $\eta$ es demasiado grande, las actualizaciones pueden sobrepasar el mínimo, causando oscilaciones o divergencia.
- Si $\eta$ es demasiado pequeña, la convergencia será extremadamente lenta.
- Un valor típico inicial está en el rango $[10^{-4}, 10^{-1}]$, dependiendo del problema y la arquitectura.

### 2.4.2 SGD con momento (*momentum*)

Una limitación del SGD básico es que puede oscilar en direcciones con curvatura pronunciada del paisaje de pérdida, avanzando lentamente a lo largo de valles estrechos. El **momento** (*momentum*) aborda este problema incorporando una "inercia" que acumula la historia de los gradientes pasados:

$$\mathbf{v}_t = \gamma \mathbf{v}_{t-1} + \eta \nabla_{\boldsymbol{\theta}} L(\boldsymbol{\theta}_t)$$

$$\boldsymbol{\theta}_{t+1} = \boldsymbol{\theta}_t - \mathbf{v}_t$$

donde $\mathbf{v}_t$ es el vector de velocidad y $\gamma \in [0, 1)$ es el coeficiente de momento, típicamente $\gamma = 0.9$.

La velocidad $\mathbf{v}_t$ acumula los gradientes de iteraciones pasadas con un decaimiento exponencial. Si el gradiente apunta consistentemente en la misma dirección, la velocidad crece, acelerando la convergencia (similar a una bola rodando cuesta abajo que gana velocidad). Si el gradiente oscila (cambia de signo frecuentemente), las contribuciones pasadas se cancelan, amortiguando las oscilaciones.

Para visualizar el efecto, expandamos la recurrencia:

$$\mathbf{v}_t = \eta \nabla L(\boldsymbol{\theta}_t) + \gamma \eta \nabla L(\boldsymbol{\theta}_{t-1}) + \gamma^2 \eta \nabla L(\boldsymbol{\theta}_{t-2}) + \cdots$$

Cada gradiente pasado contribuye con un peso que decae exponencialmente ($\gamma^k$ para el gradiente de $k$ pasos atrás). Esto constituye una media móvil exponencialmente ponderada de los gradientes.

Una variante mejorada es el **momento de Nesterov** (*Nesterov Accelerated Gradient*, NAG), que evalúa el gradiente no en la posición actual sino en la posición anticipada $\boldsymbol{\theta}_t - \gamma \mathbf{v}_{t-1}$:

$$\mathbf{v}_t = \gamma \mathbf{v}_{t-1} + \eta \nabla_{\boldsymbol{\theta}} L(\boldsymbol{\theta}_t - \gamma \mathbf{v}_{t-1})$$

$$\boldsymbol{\theta}_{t+1} = \boldsymbol{\theta}_t - \mathbf{v}_t$$

Esta "mirada hacia adelante" permite al optimizador corregir su trayectoria de forma anticipada, lo que acelera la convergencia en la práctica.

### 2.4.3 Adam (*Adaptive Moment Estimation*)

Adam (Kingma y Ba, 2015, DOI: 10.48550/arXiv.1412.6980) es uno de los optimizadores más utilizados en aprendizaje profundo debido a su robustez y buen rendimiento con los hiperparámetros por defecto. Adam combina las ideas del momento (estimación del primer momento del gradiente) con la adaptación individual de la tasa de aprendizaje para cada parámetro (estimación del segundo momento del gradiente).

El algoritmo mantiene dos estadísticas móviles para cada parámetro:

**Primer momento (media del gradiente):**

$$\mathbf{m}_t = \beta_1 \mathbf{m}_{t-1} + (1 - \beta_1) \nabla_{\boldsymbol{\theta}} L(\boldsymbol{\theta}_t)$$

**Segundo momento (media del gradiente al cuadrado):**

$$\mathbf{v}_t = \beta_2 \mathbf{v}_{t-1} + (1 - \beta_2) \left[\nabla_{\boldsymbol{\theta}} L(\boldsymbol{\theta}_t)\right]^2$$

donde el cuadrado se aplica elemento a elemento, y $\beta_1, \beta_2 \in [0, 1)$ son las tasas de decaimiento exponencial. Los valores recomendados son $\beta_1 = 0.9$ y $\beta_2 = 0.999$.

Dado que $\mathbf{m}_0 = \mathbf{0}$ y $\mathbf{v}_0 = \mathbf{0}$ (inicialización en cero), las estimaciones están sesgadas hacia cero, especialmente en las primeras iteraciones. Para corregir este sesgo, se aplica la **corrección de sesgo** (*bias correction*):

$$\hat{\mathbf{m}}_t = \frac{\mathbf{m}_t}{1 - \beta_1^t}$$

$$\hat{\mathbf{v}}_t = \frac{\mathbf{v}_t}{1 - \beta_2^t}$$

donde $\beta_1^t$ y $\beta_2^t$ denotan $\beta_1$ y $\beta_2$ elevados a la potencia $t$ (el número de iteración). En las primeras iteraciones, $1 - \beta_1^t$ es pequeño, por lo que la corrección amplifica las estimaciones; conforme $t$ crece, $\beta_1^t \to 0$ y la corrección se vuelve despreciable.

La regla de actualización de Adam es:

$$\boldsymbol{\theta}_{t+1} = \boldsymbol{\theta}_t - \frac{\eta}{\sqrt{\hat{\mathbf{v}}_t} + \epsilon} \hat{\mathbf{m}}_t$$

donde $\epsilon \approx 10^{-8}$ es una constante pequeña para evitar la división por cero, y las operaciones $\sqrt{\cdot}$ y la división se aplican elemento a elemento.

La interpretación de esta regla es intuitiva:

- **Dirección:** La actualización apunta en la dirección de $\hat{\mathbf{m}}_t$, que es la media suavizada de los gradientes recientes (similar al momento).
- **Magnitud adaptativa:** La magnitud de la actualización para cada parámetro se normaliza por $\sqrt{\hat{\mathbf{v}}_t}$, que estima la desviación estándar del gradiente. Los parámetros con gradientes históricamente grandes reciben actualizaciones más pequeñas, y viceversa. Esto adapta automáticamente la tasa de aprendizaje efectiva a la geometría local del paisaje de pérdida.

En la práctica, Adam funciona bien con la tasa de aprendizaje por defecto $\eta = 10^{-3}$ para la mayoría de los problemas, lo que simplifica la búsqueda de hiperparámetros. Sin embargo, investigaciones recientes han mostrado que SGD con momento bien ajustado puede generalizar mejor que Adam en algunos dominios (como visión por computador con CNNs), mientras que Adam suele ser preferido para modelos de lenguaje y transformadores.

### 2.4.4 Programación de la tasa de aprendizaje (*Learning Rate Scheduling*)

Independientemente del optimizador elegido, la **programación de la tasa de aprendizaje** (*learning rate scheduling*) es una técnica fundamental que ajusta la tasa de aprendizaje $\eta$ durante el entrenamiento según un esquema predefinido o adaptativo. La intuición es utilizar una tasa alta al inicio del entrenamiento (para explorar rápidamente el paisaje de pérdida) y reducirla progresivamente (para refinar la solución cerca del mínimo).

Los esquemas más comunes incluyen:

1. **Decaimiento escalonado (*Step Decay*):** Reduce $\eta$ por un factor constante cada cierto número de épocas:
$$\eta_t = \eta_0 \cdot \gamma^{\lfloor t / s \rfloor}$$
donde $s$ es el intervalo de decaimiento (en épocas) y $\gamma < 1$ es el factor de reducción.

2. **Decaimiento exponencial:** Reduce $\eta$ de forma continua y exponencial:
$$\eta_t = \eta_0 \cdot e^{-\lambda t}$$

3. **Decaimiento coseno (*Cosine Annealing*):** Reduce $\eta$ siguiendo la forma de un coseno:
$$\eta_t = \eta_{\min} + \frac{1}{2}(\eta_0 - \eta_{\min})\left(1 + \cos\left(\frac{\pi t}{T}\right)\right)$$
donde $T$ es el número total de iteraciones y $\eta_{\min}$ es la tasa mínima.

4. **Calentamiento (*Warm-up*):** Incrementa linealmente $\eta$ desde un valor muy pequeño hasta el valor objetivo durante las primeras $T_w$ iteraciones:
$$\eta_t = \eta_0 \cdot \frac{t}{T_w}, \quad t \leq T_w$$
El calentamiento es especialmente importante para optimizadores adaptativos como Adam cuando se entrenan modelos grandes (como transformadores), pues las estimaciones de los momentos son poco fiables en las primeras iteraciones.

5. **Reducción en meseta (*ReduceLROnPlateau*):** Monitoriza una métrica de validación y reduce $\eta$ cuando la métrica deja de mejorar durante un número especificado de épocas (*patience*).

En la práctica, muchos esquemas exitosos combinan un calentamiento inicial seguido de un decaimiento coseno, configuración que se ha convertido en estándar para el entrenamiento de transformadores y modelos de comunicaciones semánticas de extremo a extremo.

---

## 2.5 Regularización

La regularización comprende un conjunto de técnicas diseñadas para prevenir el **sobreajuste** (*overfitting*), que ocurre cuando el modelo aprende los patrones específicos del conjunto de entrenamiento (incluyendo el ruido) en lugar de las relaciones generales subyacentes. Un modelo sobreajustado tiene un rendimiento excelente en los datos de entrenamiento pero pobre en datos nuevos no vistos, es decir, tiene mala capacidad de **generalización**.

### 2.5.1 Sobreajuste vs. subajuste

Para comprender la regularización, es esencial entender el equilibrio entre **sesgo** (*bias*) y **varianza** (*variance*) del modelo:

- **Subajuste (*underfitting*):** El modelo es demasiado simple para capturar los patrones relevantes de los datos. Tiene alto sesgo: comete errores sistemáticos tanto en entrenamiento como en validación. Ejemplo: usar una regresión lineal para datos con relaciones fuertemente no lineales. Se manifiesta como una pérdida de entrenamiento alta que no disminuye significativamente con más entrenamiento.

- **Sobreajuste (*overfitting*):** El modelo es demasiado complejo relativo a la cantidad y complejidad de los datos disponibles. Tiene alta varianza: memoriza los ejemplos de entrenamiento en lugar de aprender patrones generalizables. Se manifiesta como una divergencia entre la pérdida de entrenamiento (que sigue disminuyendo) y la pérdida de validación (que comienza a aumentar en cierto punto). Ejemplo: un MLP con millones de parámetros entrenado con pocos cientos de ejemplos.

El objetivo es encontrar el punto óptimo de **complejidad del modelo** que minimiza el error de generalización. Las técnicas de regularización permiten utilizar modelos de alta capacidad (necesarios para problemas complejos) al tiempo que limitan su tendencia al sobreajuste.

### 2.5.2 Regularización L1 (*Lasso*)

La regularización L1 añade a la función de pérdida un término de penalización proporcional a la suma de los valores absolutos de los pesos:

$$L_{\text{reg}} = L + \lambda \sum_{l} \sum_{i,j} |W_{ij}^{(l)}|$$

donde $\lambda > 0$ es el **hiperparámetro de regularización** que controla la intensidad de la penalización. El término $\lambda \sum |W_{ij}^{(l)}|$ corresponde a la norma $\ell_1$ del vector de pesos.

La regularización L1 tiene una propiedad notable: tiende a llevar muchos pesos exactamente a cero, produciendo modelos **dispersos** (*sparse*). Esto ocurre porque el subdgradiente de $|w|$ tiene magnitud constante (no decrece conforme $w \to 0$, a diferencia de L2), por lo que la fuerza de regularización sigue "empujando" el peso hacia cero incluso cuando este es muy pequeño. Esta propiedad convierte a L1 en una técnica de **selección de características**, ya que las neuronas cuyos pesos se anulan quedan efectivamente desactivadas.

El gradiente del término de regularización L1 (en realidad, un subgradiente, ya que $|w|$ no es diferenciable en $w = 0$) es:

$$\frac{\partial}{\partial W_{ij}^{(l)}} \lambda |W_{ij}^{(l)}| = \lambda \cdot \text{sign}(W_{ij}^{(l)})$$

donde $\text{sign}(\cdot)$ es la función signo.

### 2.5.3 Regularización L2 (*Ridge* o *Weight Decay*)

La regularización L2 añade un término proporcional a la suma de los cuadrados de los pesos:

$$L_{\text{reg}} = L + \frac{\lambda}{2} \sum_{l} \sum_{i,j} (W_{ij}^{(l)})^2$$

El factor $\frac{1}{2}$ se incluye por conveniencia matemática, ya que simplifica la derivada. Este término corresponde al cuadrado de la norma $\ell_2$ del vector de pesos (norma de Frobenius para matrices).

El gradiente del término de regularización L2 es:

$$\frac{\partial}{\partial W_{ij}^{(l)}} \frac{\lambda}{2} (W_{ij}^{(l)})^2 = \lambda W_{ij}^{(l)}$$

Este gradiente es proporcional al peso actual, lo que significa que la fuerza de regularización es mayor para pesos grandes y menor para pesos pequeños. A diferencia de L1, L2 no produce pesos exactamente iguales a cero, sino que los mantiene pequeños. Esto se denomina **decaimiento de pesos** (*weight decay*): en cada iteración, antes de aplicar el gradiente de la pérdida, los pesos se multiplican por un factor $1 - \eta\lambda < 1$:

$$W_{ij}^{(l)} \leftarrow (1 - \eta\lambda) W_{ij}^{(l)} - \eta \frac{\partial L}{\partial W_{ij}^{(l)}}$$

Intuitivamente, la regularización L2 penaliza las soluciones con pesos grandes, favoreciendo funciones más "suaves" y con menor complejidad efectiva. Esto reduce la capacidad del modelo para memorizar ruido, ya que las soluciones que se ajustan al ruido típicamente requieren pesos grandes para producir las oscilaciones necesarias.

### 2.5.4 Dropout

El *dropout* (Srivastava et al., 2014, DOI: 10.5555/2627435.2670313) es una técnica de regularización específica para redes neuronales que consiste en **desactivar aleatoriamente** una fracción de las neuronas de cada capa durante cada iteración de entrenamiento.

Formalmente, durante el entrenamiento, cada neurona de una capa es desactivada (su activación se fija en cero) con probabilidad $p$ (la **tasa de dropout**), independientemente de las demás neuronas. Esto se implementa multiplicando las activaciones por una máscara binaria aleatoria $\mathbf{m}^{(l)} \sim \text{Bernoulli}(1-p)$:

$$\tilde{\mathbf{a}}^{(l)} = \mathbf{m}^{(l)} \odot \mathbf{a}^{(l)}$$

donde $m_i^{(l)} \in \{0, 1\}$ es 1 con probabilidad $1-p$ y 0 con probabilidad $p$, y $\tilde{\mathbf{a}}^{(l)}$ son las activaciones modificadas que se pasan a la siguiente capa. Para compensar el hecho de que se están eliminando neuronas (lo cual reduce la magnitud esperada de las activaciones), las activaciones supervivientes se escalan por $\frac{1}{1-p}$ durante el entrenamiento (*inverted dropout*):

$$\tilde{\mathbf{a}}^{(l)} = \frac{1}{1-p} \mathbf{m}^{(l)} \odot \mathbf{a}^{(l)}$$

Esto garantiza que el valor esperado de $\tilde{\mathbf{a}}^{(l)}$ sea igual al de $\mathbf{a}^{(l)}$, de modo que durante la **inferencia** (evaluación) no se necesita ningún ajuste: simplemente se utilizan todas las neuronas sin dropout.

¿Por qué funciona el dropout? Se pueden ofrecer varias interpretaciones:

1. **Ensamble implícito:** Cada iteración de entrenamiento usa una subred diferente (definida por la máscara aleatoria). Con $n$ neuronas susceptibles de dropout, existen $2^n$ posibles subredes. El entrenamiento con dropout es, en cierto sentido, un entrenamiento simultáneo de un ensamble exponencialmente grande de redes con parámetros compartidos. La predicción final (sin dropout) puede verse como una media ponderada de las predicciones de todas estas subredes.

2. **Reducción de co-adaptaciones:** Sin dropout, las neuronas pueden desarrollar dependencias mutuas complejas: una neurona puede "confiar" en que otra neurona corregirá sus errores. El dropout obliga a cada neurona a ser útil por sí misma, produciendo representaciones más robustas y redundantes.

3. **Inyección de ruido:** El dropout puede verse como una forma de inyectar ruido multiplicativo en las activaciones, lo cual actúa como un regularizador al impedir que el modelo se ajuste demasiado a los datos de entrenamiento.

Los valores típicos de la tasa de dropout $p$ son:
- $p = 0.5$ para capas ocultas (valor por defecto)
- $p = 0.2$ para la capa de entrada (si se aplica dropout a la entrada)
- Para capas más anchas se puede usar $p$ mayor; para capas estrechas, $p$ menor

### 2.5.5 Normalización por lotes (*Batch Normalization*)

La normalización por lotes (*Batch Normalization*, BN), propuesta por Ioffe y Szegedy (2015, DOI: 10.48550/arXiv.1502.03167), es una técnica que normaliza las pre-activaciones de cada capa para que tengan media cero y varianza unitaria dentro de cada mini-batch de entrenamiento. Aunque fue propuesta originalmente como un acelerador de entrenamiento (no como regularizador), tiene un efecto regularizador significativo en la práctica.

Para un mini-batch $\mathcal{B} = \{z_1, z_2, \ldots, z_B\}$ de pre-activaciones de una neurona particular, la normalización por lotes aplica:

**Paso 1 — Calcular estadísticas del batch:**

$$\mu_{\mathcal{B}} = \frac{1}{B} \sum_{i=1}^{B} z_i, \quad \sigma_{\mathcal{B}}^2 = \frac{1}{B} \sum_{i=1}^{B} (z_i - \mu_{\mathcal{B}})^2$$

**Paso 2 — Normalizar:**

$$\hat{z}_i = \frac{z_i - \mu_{\mathcal{B}}}{\sqrt{\sigma_{\mathcal{B}}^2 + \epsilon}}$$

donde $\epsilon \approx 10^{-5}$ es una constante para estabilidad numérica.

**Paso 3 — Escalar y desplazar (parámetros aprendibles):**

$$\tilde{z}_i = \gamma \hat{z}_i + \beta$$

donde $\gamma$ (escala) y $\beta$ (desplazamiento) son parámetros aprendibles que permiten a la red "deshacer" la normalización si esto es beneficioso para la tarea. Sin estos parámetros, la normalización limitaría la capacidad expresiva de la red.

Beneficios de la normalización por lotes:

1. **Permite tasas de aprendizaje más altas:** Al mantener las activaciones en un rango normalizado, se reduce la sensibilidad a la escala de los parámetros, lo que permite usar tasas de aprendizaje más agresivas sin riesgo de inestabilidad.

2. **Acelera la convergencia:** Al reducir el fenómeno de *internal covariate shift* (cambio en la distribución de las activaciones de una capa cuando cambian los parámetros de las capas anteriores), cada capa puede aprender de forma más estable.

3. **Efecto regularizador:** La normalización basada en estadísticas del mini-batch introduce ruido estocástico (las estadísticas varían de un batch a otro), lo que actúa como regularizador y puede reducir la necesidad de dropout.

4. **Reduce la sensibilidad a la inicialización:** Los modelos con BN son menos dependientes de la elección cuidadosa de los pesos iniciales.

Durante la **inferencia**, no se dispone de un mini-batch, por lo que se utilizan medias y varianzas calculadas como medias móviles exponenciales durante el entrenamiento. PyTorch maneja esto automáticamente al alternar entre los modos `model.train()` y `model.eval()`.

---

## 2.6 Ejemplo práctico: Clasificación con MLP

### 2.6.1 Planteamiento del problema

Para consolidar los conceptos presentados en esta sección, implementaremos un clasificador binario basado en un MLP utilizando PyTorch. El problema consiste en predecir si una solicitud de crédito será **aprobada** (clase 1) o **rechazada** (clase 0) a partir de dos características numéricas: el ingreso mensual del solicitante (normalizado) y su puntuación de historial crediticio (normalizada).

Generaremos datos sintéticos que simulan este escenario, entrenaremos un MLP con una capa oculta y evaluaremos su rendimiento. Aunque el problema es sencillo, el código y las técnicas son directamente escalables a problemas reales de mayor complejidad.

### 2.6.2 Implementación en PyTorch

```python
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
import numpy as np

# ============================================================
# 1. Generar datos sintéticos
# ============================================================
# Fijamos la semilla para reproducibilidad
torch.manual_seed(42)
np.random.seed(42)

# Generamos 1000 muestras con 2 características
N = 1000
# Característica 1: ingreso mensual normalizado (media 0, std 1)
# Característica 2: puntuación crediticia normalizada
X = np.random.randn(N, 2).astype(np.float32)

# Regla de decisión: aprobado si 0.5*x1 + 0.8*x2 + ruido > 0
# Esto crea una frontera de decisión lineal con algo de ruido
ruido = 0.3 * np.random.randn(N).astype(np.float32)
y = (0.5 * X[:, 0] + 0.8 * X[:, 1] + ruido > 0).astype(np.float32)

# Convertir a tensores de PyTorch
X_tensor = torch.from_numpy(X)                  # Forma: (1000, 2)
y_tensor = torch.from_numpy(y).unsqueeze(1)      # Forma: (1000, 1)

# Dividir en conjuntos de entrenamiento (80%) y prueba (20%)
N_train = int(0.8 * N)
X_train, X_test = X_tensor[:N_train], X_tensor[N_train:]
y_train, y_test = y_tensor[:N_train], y_tensor[N_train:]

# Crear DataLoaders para iterar sobre mini-batches
# TensorDataset agrupa las características y etiquetas
dataset_train = TensorDataset(X_train, y_train)
# DataLoader gestiona la iteración por mini-batches y el mezclado
train_loader = DataLoader(dataset_train, batch_size=32, shuffle=True)

# ============================================================
# 2. Definir la arquitectura del MLP
# ============================================================
class MLPClasificador(nn.Module):
    """
    Perceptrón multicapa para clasificación binaria.
    Arquitectura: 2 -> 16 -> 8 -> 1
    """
    def __init__(self):
        # Llamar al constructor de nn.Module (obligatorio)
        super(MLPClasificador, self).__init__()

        # Primera capa oculta: 2 entradas -> 16 neuronas
        # nn.Linear implementa la transformación z = Wx + b
        self.capa1 = nn.Linear(in_features=2, out_features=16)

        # Segunda capa oculta: 16 -> 8 neuronas
        self.capa2 = nn.Linear(in_features=16, out_features=8)

        # Capa de salida: 8 -> 1 neurona (clasificación binaria)
        self.salida = nn.Linear(in_features=8, out_features=1)

        # Función de activación ReLU para capas ocultas
        self.relu = nn.ReLU()

        # Activación sigmoide para la salida (probabilidad entre 0 y 1)
        self.sigmoid = nn.Sigmoid()

        # Normalización por lotes para la primera capa oculta
        self.bn1 = nn.BatchNorm1d(num_features=16)

        # Dropout con tasa p=0.3 (desactiva 30% de las neuronas)
        self.dropout = nn.Dropout(p=0.3)

    def forward(self, x):
        """
        Define la propagación hacia adelante.
        x: tensor de entrada con forma (batch_size, 2)
        """
        # Capa 1: transformación afín -> batch norm -> ReLU -> dropout
        x = self.capa1(x)        # z^(1) = W^(1)x + b^(1)
        x = self.bn1(x)          # Normalización por lotes
        x = self.relu(x)         # a^(1) = ReLU(z^(1))
        x = self.dropout(x)      # Dropout (solo activo en entrenamiento)

        # Capa 2: transformación afín -> ReLU
        x = self.capa2(x)        # z^(2) = W^(2)a^(1) + b^(2)
        x = self.relu(x)         # a^(2) = ReLU(z^(2))

        # Capa de salida: transformación afín -> sigmoide
        x = self.salida(x)       # z^(3) = W^(3)a^(2) + b^(3)
        x = self.sigmoid(x)      # y_hat = sigma(z^(3))

        return x

# Instanciar el modelo
modelo = MLPClasificador()

# Verificar la arquitectura
print(modelo)
# Contar el número total de parámetros
total_params = sum(p.numel() for p in modelo.parameters())
print(f"Parámetros totales: {total_params}")

# ============================================================
# 3. Definir la función de pérdida y el optimizador
# ============================================================
# Entropía cruzada binaria (BCE)
# Mide la discrepancia entre la distribución predicha y la real
criterio = nn.BCELoss()

# Optimizador Adam con tasa de aprendizaje 0.001
# y regularización L2 (weight_decay) con lambda = 1e-4
optimizador = optim.Adam(
    modelo.parameters(),
    lr=0.001,
    weight_decay=1e-4    # Regularización L2
)

# Programador de tasa de aprendizaje: reduce lr al 50%
# si la pérdida no mejora en 5 épocas
scheduler = optim.lr_scheduler.ReduceLROnPlateau(
    optimizador,
    mode='min',
    factor=0.5,
    patience=5,
    verbose=True
)

# ============================================================
# 4. Bucle de entrenamiento
# ============================================================
num_epocas = 50

for epoca in range(num_epocas):
    # Activar modo entrenamiento (activa dropout y batch norm)
    modelo.train()

    perdida_acumulada = 0.0
    num_batches = 0

    # Iterar sobre mini-batches
    for X_batch, y_batch in train_loader:
        # --- Propagación hacia adelante ---
        # Calcular las predicciones del modelo
        predicciones = modelo(X_batch)

        # Calcular la pérdida (BCE) entre predicciones y etiquetas
        perdida = criterio(predicciones, y_batch)

        # --- Retropropagación ---
        # Poner a cero los gradientes acumulados del paso anterior
        # (PyTorch acumula gradientes por defecto)
        optimizador.zero_grad()

        # Calcular los gradientes de la pérdida respecto a todos
        # los parámetros del modelo (retropropagación automática)
        perdida.backward()

        # --- Actualización de parámetros ---
        # El optimizador actualiza los pesos usando los gradientes
        # calculados y la regla de Adam
        optimizador.step()

        perdida_acumulada += perdida.item()
        num_batches += 1

    # Pérdida promedio de la época
    perdida_promedio = perdida_acumulada / num_batches

    # Actualizar el scheduler basado en la pérdida de la época
    scheduler.step(perdida_promedio)

    # --- Evaluación en el conjunto de prueba ---
    # Activar modo evaluación (desactiva dropout, usa estadísticas
    # de batch norm calculadas durante el entrenamiento)
    modelo.eval()

    # Desactivar el cálculo de gradientes (ahorra memoria y tiempo)
    with torch.no_grad():
        pred_test = modelo(X_test)
        perdida_test = criterio(pred_test, y_test)

        # Convertir probabilidades a clases (umbral 0.5)
        clases_pred = (pred_test >= 0.5).float()
        precision = (clases_pred == y_test).float().mean()

    # Imprimir cada 10 épocas
    if (epoca + 1) % 10 == 0:
        print(f"Época [{epoca+1}/{num_epocas}] | "
              f"Pérdida Train: {perdida_promedio:.4f} | "
              f"Pérdida Test: {perdida_test:.4f} | "
              f"Precisión Test: {precision:.4f}")

# ============================================================
# 5. Evaluación final
# ============================================================
modelo.eval()
with torch.no_grad():
    pred_final = modelo(X_test)
    clases_final = (pred_final >= 0.5).float()
    precision_final = (clases_final == y_test).float().mean()
    print(f"\nPrecisión final en test: {precision_final:.4f}")
```

### 2.6.3 Explicación del bucle de entrenamiento

El bucle de entrenamiento es el corazón del proceso de aprendizaje y merece una explicación detallada:

1. **`modelo.train()`**: Activa el modo de entrenamiento, lo que habilita el dropout (desactivación aleatoria de neuronas) y la normalización por lotes con estadísticas del mini-batch actual. Sin esta llamada, el modelo no aplicaría regularización durante el entrenamiento.

2. **Iteración sobre mini-batches**: El `DataLoader` se encarga de dividir el conjunto de entrenamiento en mini-batches de tamaño 32 y mezclarlos aleatoriamente en cada época (`shuffle=True`). Cada iteración del bucle interno procesa un mini-batch.

3. **`predicciones = modelo(X_batch)`**: Realiza la propagación hacia adelante. PyTorch ejecuta automáticamente el método `forward()` y construye el **grafo computacional** (*computational graph*), una estructura de datos que registra todas las operaciones realizadas y que será utilizada por la retropropagación para calcular los gradientes.

4. **`perdida = criterio(predicciones, y_batch)`**: Calcula la función de pérdida (BCE) entre las predicciones y las etiquetas verdaderas. Este valor escalar es el punto de partida para la retropropagación.

5. **`optimizador.zero_grad()`**: Pone a cero los gradientes de todos los parámetros. Esto es necesario porque PyTorch **acumula** los gradientes por defecto (los suma en cada llamada a `.backward()`). Sin esta línea, los gradientes de iteraciones anteriores se sumarían a los actuales, produciendo actualizaciones incorrectas. La acumulación de gradientes es útil en ciertos escenarios (por ejemplo, para simular batches más grandes), pero en el caso estándar debe ser reiniciada en cada iteración.

6. **`perdida.backward()`**: Esta es la llamada clave que ejecuta la **retropropagación automática** (*automatic differentiation*). PyTorch recorre el grafo computacional en orden inverso, calculando $\frac{\partial L}{\partial \theta}$ para cada parámetro $\theta$ del modelo utilizando la regla de la cadena, exactamente como se describió en la Subsección 2.2. Los gradientes calculados se almacenan en el atributo `.grad` de cada parámetro.

7. **`optimizador.step()`**: Actualiza todos los parámetros del modelo utilizando los gradientes almacenados en `.grad` y la regla de actualización del optimizador (en este caso, Adam). Para el optimizador Adam, esto implica actualizar las estimaciones de primer y segundo momento, aplicar la corrección de sesgo y calcular la actualización final como se describió en la Subsección 2.4.3.

8. **`modelo.eval()` y `torch.no_grad()`**: Para la evaluación, se desactiva el dropout y se utilizan las estadísticas de BN acumuladas. El contexto `torch.no_grad()` desactiva la construcción del grafo computacional, reduciendo el consumo de memoria y acelerando la inferencia.

### 2.6.4 Análisis de los resultados

El código anterior produce un clasificador que aprende la frontera de decisión lineal subyacente en los datos. Al ser un problema relativamente simple (frontera lineal con algo de ruido), un MLP incluso pequeño logra una precisión alta ($> 90\%$) tras pocas épocas de entrenamiento.

Algunos aspectos a observar:

- **La pérdida de entrenamiento disminuye monótonamente** en cada época, lo que indica que el optimizador está actualizando los parámetros en la dirección correcta.
- **La pérdida de test puede fluctuar** ligeramente, pero con la regularización aplicada (dropout + L2 + BN), debería permanecer cercana a la pérdida de entrenamiento, indicando buena generalización.
- **El scheduler de tasa de aprendizaje** reduce $\eta$ automáticamente si la pérdida se estanca, permitiendo un refinamiento más fino en las etapas finales del entrenamiento.
- **El número de parámetros** del modelo es $2 \times 16 + 16 + 16 \times 8 + 8 + 8 \times 1 + 1 + 16 \times 2 = 32 + 16 + 128 + 8 + 8 + 1 + 32 = 225$ (incluyendo los parámetros $\gamma$ y $\beta$ del BatchNorm). Este número es modesto para un MLP, pero las técnicas empleadas son idénticas a las utilizadas en modelos con millones de parámetros.

### 2.6.5 Conexión con comunicaciones semánticas

En un sistema de comunicaciones semánticas basado en MLP, la arquitectura del ejemplo puede extenderse de la siguiente manera:

- **Codificador semántico (transmisor):** Un MLP que recibe datos de alta dimensionalidad (texto tokenizado, píxeles de imagen, muestras de audio) y los comprime en una representación latente de baja dimensionalidad, análoga a un código de canal. La regularización (dropout, L2) previene el sobreajuste y promueve representaciones robustas al ruido del canal.

- **Canal:** La representación latente se transmite a través de un canal con ruido (por ejemplo, AWGN), que puede modelarse como una capa sin parámetros aprendibles que suma ruido gaussiano.

- **Decodificador semántico (receptor):** Otro MLP que recibe la señal ruidosa y reconstruye la información semántica relevante. La función de pérdida se elige según el objetivo: MSE para reconstrucción exacta, entropía cruzada si el objetivo es clasificar correctamente el contenido del mensaje.

El entrenamiento extremo a extremo de este sistema utiliza exactamente los mismos principios de retropropagación, funciones de pérdida y optimizadores descritos en esta sección, con la diferencia de que el gradiente debe propagarse a través de la capa de canal (lo que requiere técnicas especiales cuando el canal no es diferenciable, tema que se abordará en secciones posteriores).

---

**Resumen de la sección:** En esta sección hemos estudiado el perceptrón multicapa como la arquitectura fundamental del aprendizaje profundo. Hemos formalizado la propagación hacia adelante mediante la composición de transformaciones afines y funciones de activación no lineales, y hemos derivado en detalle el algoritmo de retropropagación como una aplicación sistemática de la regla de la cadena. Se presentaron las funciones de pérdida más importantes (MSE, BCE, CCE) y sus criterios de selección, los optimizadores modernos (SGD, SGD con momento, Adam) y sus propiedades, y las técnicas de regularización (L1, L2, dropout, normalización por lotes) necesarias para lograr buena generalización. Finalmente, se implementó un ejemplo completo de clasificación binaria en PyTorch que integra todos estos conceptos. Los principios aquí presentados constituyen la base sobre la cual se construirán las arquitecturas más sofisticadas de las secciones siguientes: redes convolucionales, redes recurrentes y transformadores.
