# 5. Mecanismos de Atención

Los mecanismos de atención constituyen uno de los avances más transformadores en la historia del aprendizaje profundo. Surgidos como una solución elegante a un problema fundamental de las redes neuronales recurrentes, estos mecanismos han redefinido por completo la forma en que los modelos neuronales procesan, relacionan y comprenden la información secuencial. En el contexto de las comunicaciones semánticas, los mecanismos de atención desempeñan un papel central: permiten que el sistema identifique qué partes de un mensaje son más relevantes para la tarea comunicativa, facilitando una compresión inteligente que preserva el significado esencial mientras descarta la redundancia. Este capítulo presenta una exposición exhaustiva de los mecanismos de atención, desde su motivación original hasta las formulaciones modernas que sustentan arquitecturas como el Transformer.

---

## 5.1 Motivación: el cuello de botella de la información

### 5.1.1 El problema fundamental de los modelos seq2seq

En la Sección 4 estudiamos los modelos secuencia-a-secuencia (*sequence-to-sequence*, seq2seq) basados en redes neuronales recurrentes (RNN). Recordemos que la arquitectura canónica seq2seq, propuesta por Sutskever et al. (2014), consta de dos componentes principales:

1. **Codificador (Encoder):** Una RNN que procesa la secuencia de entrada token por token, actualizando su estado oculto en cada paso temporal. Al finalizar el procesamiento de toda la secuencia de entrada $(x_1, x_2, \ldots, x_T)$, el codificador produce un estado oculto final $\mathbf{h}_T$.

2. **Decodificador (Decoder):** Una segunda RNN que recibe el estado oculto final del codificador como su estado inicial y genera la secuencia de salida token por token.

El elemento crítico de esta arquitectura es que **toda la información** de la secuencia de entrada debe comprimirse en un único vector de longitud fija $\mathbf{h}_T \in \mathbb{R}^n$, donde $n$ es la dimensión del estado oculto. Este vector, denominado comúnmente **vector de contexto**, actúa como el único puente de comunicación entre el codificador y el decodificador.

Formalmente, si el codificador procesa una secuencia de $T$ tokens, la dinámica es:

$$\mathbf{h}_t = f(\mathbf{h}_{t-1}, \mathbf{x}_t), \quad t = 1, 2, \ldots, T$$

donde $f$ representa la función de transición de la RNN (ya sea una celda simple, LSTM o GRU). El vector de contexto es simplemente:

$$\mathbf{c} = \mathbf{h}_T$$

El decodificador entonces genera la salida condicionada únicamente en este vector:

$$\mathbf{s}_t = g(\mathbf{s}_{t-1}, y_{t-1}, \mathbf{c})$$

$$P(y_t \mid y_1, \ldots, y_{t-1}, \mathbf{x}) = \text{softmax}(\mathbf{W}_o \mathbf{s}_t)$$

### 5.1.2 El cuello de botella informacional

Este diseño presenta un **cuello de botella informacional** severo. Consideremos las implicaciones:

- **Compresión lossy obligatoria:** Un párrafo de 100 palabras, con toda su riqueza semántica, sintáctica y pragmática, debe representarse en un vector de, digamos, 256 o 512 dimensiones. Esto es análogo a intentar comprimir una imagen de alta resolución en unos pocos bytes: inevitablemente se pierde información.

- **Degradación con la longitud:** A medida que la secuencia de entrada se hace más larga, el problema se agrava. Las primeras palabras de la secuencia deben "sobrevivir" a través de múltiples pasos de actualización del estado oculto, y la información que portan se diluye progresivamente. Incluso con arquitecturas como LSTM o GRU, que mitigan parcialmente el problema del desvanecimiento del gradiente, la capacidad de retención de información a largo plazo es limitada.

- **Tratamiento uniforme:** El decodificador recibe la misma representación comprimida $\mathbf{c}$ en cada paso de generación, sin importar qué parte de la salida está generando. Intuitivamente, cuando se traduce una oración larga, las primeras palabras de la traducción deberían depender más de las primeras palabras del original, pero el modelo no tiene mecanismo para implementar esta dependencia selectiva.

Cho et al. (2014) demostraron empíricamente esta limitación: el rendimiento de los modelos seq2seq basados en RNN se degradaba significativamente a medida que la longitud de las oraciones de entrada aumentaba, especialmente para secuencias de más de 20-30 tokens.

### 5.1.3 La intuición detrás de la atención

La solución a este cuello de botella es conceptualmente simple pero profundamente elegante: **permitir que el decodificador "mire hacia atrás" a todos los estados ocultos del codificador**, no solo al último. En lugar de forzar toda la información a pasar por un único vector, el mecanismo de atención permite que el decodificador, en cada paso de generación, consulte selectivamente diferentes partes de la secuencia de entrada.

La analogía humana es inmediata. Cuando un traductor humano trabaja con un texto largo, no lee el texto completo, memoriza todo en su mente, y luego escribe la traducción sin volver a mirar el original. En su lugar, el traductor consulta repetidamente el texto fuente, enfocándose en las partes relevantes para la porción que está traduciendo en ese momento. El mecanismo de atención dota a las redes neuronales de esta misma capacidad.

Matemáticamente, en lugar de un vector de contexto fijo $\mathbf{c}$, el mecanismo de atención produce un vector de contexto **dinámico** $\mathbf{c}_i$ que cambia en cada paso temporal $i$ del decodificador:

$$\mathbf{c}_i = \sum_{j=1}^{T} \alpha_{ij} \mathbf{h}_j$$

donde $\alpha_{ij}$ son **pesos de atención** que determinan cuánta atención presta el decodificador (en el paso $i$) al estado oculto del codificador en la posición $j$. Estos pesos satisfacen:

$$\alpha_{ij} \geq 0, \quad \sum_{j=1}^{T} \alpha_{ij} = 1$$

Es decir, los pesos de atención forman una distribución de probabilidad sobre las posiciones de la secuencia de entrada, lo que permite interpretar $\alpha_{ij}$ como la probabilidad de que la posición $j$ de la entrada sea relevante para generar el token $i$ de la salida.

### 5.1.4 Relevancia para las comunicaciones semánticas

En el contexto de las comunicaciones semánticas, el cuello de botella de la información es particularmente pertinente. Un sistema de comunicación semántica debe decidir qué información transmitir a través de un canal con capacidad limitada. El mecanismo de atención proporciona un marco natural para esta tarea: los pesos de atención pueden interpretarse como una medida de la **importancia semántica** de cada elemento de la señal. Los elementos con altos pesos de atención portan información semántica crítica y deben protegerse durante la transmisión, mientras que los elementos con bajos pesos de atención pueden comprimirse más agresivamente o incluso descartarse sin pérdida significativa de significado.

---

## 5.2 Atención de Bahdanau (Atención Aditiva)

### 5.2.1 Contexto histórico

El mecanismo de atención fue introducido formalmente por Dzmitry Bahdanau, Kyunghyun Cho y Yoshua Bengio en su influyente trabajo de 2015 (Bahdanau et al., 2015). Este trabajo, titulado *"Neural Machine Translation by Jointly Learning to Align and Translate"*, propuso el mecanismo de atención en el contexto de la traducción automática neuronal y demostró mejoras significativas sobre los modelos seq2seq estándar, especialmente para oraciones largas.

La idea central es que, en lugar de codificar toda la oración de entrada en un vector de contexto fijo, el modelo aprende a **alinear** (*align*) y **traducir** conjuntamente. La alineación se refiere al proceso de determinar qué partes de la oración fuente son más relevantes para generar cada palabra de la oración objetivo.

### 5.2.2 Arquitectura del codificador bidireccional

Bahdanau et al. utilizaron un codificador **bidireccional** (BiRNN) para obtener representaciones más ricas de cada posición de la entrada. El codificador bidireccional consta de dos RNN: una que procesa la secuencia de izquierda a derecha (forward) y otra de derecha a izquierda (backward):

**RNN forward:**

$$\overrightarrow{\mathbf{h}}_j = \overrightarrow{f}(\overrightarrow{\mathbf{h}}_{j-1}, \mathbf{x}_j)$$

**RNN backward:**

$$\overleftarrow{\mathbf{h}}_j = \overleftarrow{f}(\overleftarrow{\mathbf{h}}_{j+1}, \mathbf{x}_j)$$

La representación final de cada posición $j$ se obtiene concatenando ambos estados ocultos:

$$\mathbf{h}_j = [\overrightarrow{\mathbf{h}}_j; \overleftarrow{\mathbf{h}}_j] \in \mathbb{R}^{2n}$$

Esta representación bidireccional captura tanto el contexto precedente como el contexto subsiguiente de cada token, proporcionando una representación más completa que una RNN unidireccional. El estado $\mathbf{h}_j$ resume la información de toda la oración de entrada con un enfoque especial en las palabras cercanas a la posición $j$.

### 5.2.3 El mecanismo de alineación (scoring)

El componente central de la atención de Bahdanau es la **función de alineación** (también llamada función de puntuación o *score function*), que calcula un escalar $e_{ij}$ que mide cuán relevante es el estado oculto del codificador $\mathbf{h}_j$ para el paso de decodificación $i$. Esta función se define como:

$$e_{ij} = \mathbf{v}^T \tanh(\mathbf{W}_1 \mathbf{s}_{i-1} + \mathbf{W}_2 \mathbf{h}_j)$$

Desglosemos cada componente de esta ecuación con extremo detalle:

**1. Estado del decodificador $\mathbf{s}_{i-1} \in \mathbb{R}^m$:**
Este es el estado oculto del decodificador en el paso temporal *anterior* ($i-1$). Representa lo que el decodificador "sabe" hasta el momento, incluyendo toda la información sobre los tokens de salida ya generados. Es crucial notar que se usa $\mathbf{s}_{i-1}$ y no $\mathbf{s}_i$: la atención se calcula *antes* de actualizar el estado del decodificador, porque el vector de contexto resultante se utilizará como entrada para dicha actualización.

**2. Estado del codificador $\mathbf{h}_j \in \mathbb{R}^{2n}$:**
Este es el estado oculto del codificador bidireccional en la posición $j$ de la secuencia de entrada. Como se describió anteriormente, es la concatenación de los estados ocultos forward y backward, y por lo tanto contiene información contextual tanto del pasado como del futuro de la posición $j$.

**3. Matrices de pesos $\mathbf{W}_1 \in \mathbb{R}^{d_a \times m}$ y $\mathbf{W}_2 \in \mathbb{R}^{d_a \times 2n}$:**
Estas son matrices de pesos aprendibles que proyectan los estados del decodificador y del codificador, respectivamente, a un espacio común de dimensión $d_a$ (la dimensión de la atención). La proyección a un espacio común es necesaria porque $\mathbf{s}_{i-1}$ y $\mathbf{h}_j$ pueden tener dimensiones diferentes y, más importante, provienen de espacios de representación distintos. Las matrices $\mathbf{W}_1$ y $\mathbf{W}_2$ aprenden a transformar ambas representaciones de manera que sean comparables.

El producto $\mathbf{W}_1 \mathbf{s}_{i-1} \in \mathbb{R}^{d_a}$ puede interpretarse como la "pregunta" que el decodificador formula: "¿Qué información necesito del codificador para generar el siguiente token?"

El producto $\mathbf{W}_2 \mathbf{h}_j \in \mathbb{R}^{d_a}$ puede interpretarse como la "respuesta potencial" de cada posición del codificador: "Esta es la información que yo puedo ofrecer."

**4. Función de activación $\tanh$:**
La función tangente hiperbólica se aplica elemento a elemento sobre la suma de las dos proyecciones:

$$\tanh(\mathbf{W}_1 \mathbf{s}_{i-1} + \mathbf{W}_2 \mathbf{h}_j) \in \mathbb{R}^{d_a}$$

La función $\tanh$ introduce no-linealidad, lo que permite al modelo capturar relaciones complejas entre las posiciones del codificador y el estado del decodificador. Sin esta no-linealidad, la función de alineación sería simplemente una función bilineal, limitando significativamente su expresividad. Además, $\tanh$ acota los valores al rango $[-1, 1]$, lo que contribuye a la estabilidad numérica del entrenamiento.

**5. Vector de pesos $\mathbf{v} \in \mathbb{R}^{d_a}$:**
Este es un vector de pesos aprendible que convierte el vector resultado de la $\tanh$ (de dimensión $d_a$) en un escalar. El producto punto $\mathbf{v}^T \tanh(\cdot)$ puede verse como una capa de red neuronal que produce una puntuación escalar de alineación. El vector $\mathbf{v}$ aprende a ponderar las diferentes dimensiones del espacio de alineación, determinando qué aspectos de la comparación entre codificador y decodificador son más informativos.

**¿Por qué se llama "atención aditiva"?** El nombre proviene del hecho de que los estados del decodificador y del codificador se **suman** dentro de la función $\tanh$:

$$\mathbf{W}_1 \mathbf{s}_{i-1} + \mathbf{W}_2 \mathbf{h}_j$$

Esta operación de suma es la que distingue este mecanismo de otras variantes (como la atención multiplicativa que veremos en la siguiente sección). La atención aditiva puede verse como una red neuronal feedforward de una capa oculta (con activación $\tanh$ y capa de salida lineal $\mathbf{v}^T$) que toma como entrada la concatenación de $\mathbf{s}_{i-1}$ y $\mathbf{h}_j$.

### 5.2.4 Pesos de atención

Una vez calculadas las puntuaciones de alineación $e_{ij}$ para todas las posiciones $j = 1, 2, \ldots, T$ del codificador, estas se normalizan mediante la función **softmax** para obtener los pesos de atención:

$$\alpha_{ij} = \frac{\exp(e_{ij})}{\sum_{k=1}^{T} \exp(e_{ik})}$$

La función softmax garantiza dos propiedades esenciales:

1. **No negatividad:** $\alpha_{ij} > 0$ para todo $j$. Esto asegura que los pesos representen una "contribución positiva" de cada posición.

2. **Normalización:** $\sum_{j=1}^{T} \alpha_{ij} = 1$. Esto permite interpretar los pesos como una distribución de probabilidad sobre las posiciones de la entrada.

Los pesos de atención $\alpha_{ij}$ tienen una interpretación intuitiva poderosa: $\alpha_{ij}$ representa la **probabilidad** de que la posición $j$ de la entrada sea la más relevante para generar el token $i$ de la salida. Un valor alto de $\alpha_{ij}$ indica que el modelo "presta mucha atención" a la posición $j$ al generar el $i$-ésimo token de salida.

Es importante observar que la función softmax es una operación **diferenciable**, lo que permite que los pesos de atención se aprendan mediante retropropagación estándar. No es necesario especificar *a priori* qué posiciones son relevantes; el modelo descubre estas relaciones automáticamente durante el entrenamiento.

### 5.2.5 Vector de contexto dinámico

Finalmente, el vector de contexto para el paso $i$ del decodificador se calcula como una **suma ponderada** de todos los estados ocultos del codificador, utilizando los pesos de atención como coeficientes:

$$\mathbf{c}_i = \sum_{j=1}^{T} \alpha_{ij} \mathbf{h}_j$$

Este vector de contexto $\mathbf{c}_i$ es una combinación convexa de los estados ocultos del codificador, donde los coeficientes (pesos de atención) determinan la contribución relativa de cada posición. A diferencia del vector de contexto fijo $\mathbf{c} = \mathbf{h}_T$ del modelo seq2seq estándar, $\mathbf{c}_i$ cambia en cada paso del decodificador, adaptándose dinámicamente a las necesidades de generación del token actual.

La propiedad de **diferenciabilidad** del vector de contexto es fundamental: como $\mathbf{c}_i$ es una combinación lineal de los $\mathbf{h}_j$ con coeficientes que dependen suavemente de los parámetros del modelo (a través de la softmax), los gradientes fluyen sin obstáculo desde la función de pérdida hacia todas las partes del modelo, incluyendo las matrices $\mathbf{W}_1$, $\mathbf{W}_2$ y el vector $\mathbf{v}$.

### 5.2.6 Integración con el decodificador

El vector de contexto $\mathbf{c}_i$ se integra en el decodificador RNN de la siguiente manera:

$$\mathbf{s}_i = g(\mathbf{s}_{i-1}, y_{i-1}, \mathbf{c}_i)$$

$$P(y_i \mid y_1, \ldots, y_{i-1}, \mathbf{x}) = \text{softmax}(\mathbf{W}_o [\mathbf{s}_i; \mathbf{c}_i] + \mathbf{b}_o)$$

donde $[\mathbf{s}_i; \mathbf{c}_i]$ denota la concatenación del estado del decodificador y el vector de contexto. Nótese que $\mathbf{c}_i$ se utiliza tanto para actualizar el estado del decodificador como para predecir el token de salida, maximizando el flujo de información desde el codificador.

### 5.2.7 Visualización del mecanismo

**Figura 5.1:** *Diagrama del mecanismo de atención de Bahdanau en una arquitectura seq2seq. A la izquierda se muestra el codificador bidireccional procesando la secuencia de entrada $(x_1, x_2, x_3, x_4)$, generando los estados ocultos $(\mathbf{h}_1, \mathbf{h}_2, \mathbf{h}_3, \mathbf{h}_4)$, representados como rectángulos apilados (cada uno compuesto por la concatenación de los estados forward y backward). En el centro se ilustra el módulo de atención: flechas punteadas conectan el estado del decodificador $\mathbf{s}_{i-1}$ con cada estado del codificador $\mathbf{h}_j$, confluyendo en bloques que representan el cálculo de las puntuaciones de alineación $e_{ij}$ mediante la red feedforward $\mathbf{v}^T \tanh(\mathbf{W}_1 \mathbf{s}_{i-1} + \mathbf{W}_2 \mathbf{h}_j)$. Las puntuaciones alimentan un bloque softmax que produce los pesos de atención $\alpha_{ij}$, visualizados como un mapa de calor con intensidades proporcionales a los pesos. Los pesos se combinan con los estados del codificador en un bloque de suma ponderada que genera el vector de contexto $\mathbf{c}_i$. A la derecha se muestra el decodificador, donde $\mathbf{c}_i$ se concatena con $\mathbf{s}_{i-1}$ y el embedding del token previo $y_{i-1}$ para producir el nuevo estado $\mathbf{s}_i$ y la predicción del token $y_i$. Las flechas de diferentes grosores que conectan los estados del codificador con el vector de contexto representan visualmente los diferentes magnitudes de los pesos de atención.*

### 5.2.8 Complejidad computacional

El costo computacional de la atención de Bahdanau para cada paso del decodificador es:

- **Cálculo de puntuaciones:** $O(T \cdot d_a)$, donde $T$ es la longitud de la secuencia de entrada y $d_a$ es la dimensión de la atención. Para cada una de las $T$ posiciones, se realizan dos multiplicaciones matriz-vector ($\mathbf{W}_1 \mathbf{s}_{i-1}$ y $\mathbf{W}_2 \mathbf{h}_j$), una suma, una $\tanh$ y un producto punto con $\mathbf{v}$.

- **Softmax:** $O(T)$ para la normalización.

- **Vector de contexto:** $O(T \cdot 2n)$ para la suma ponderada.

Nótese que $\mathbf{W}_1 \mathbf{s}_{i-1}$ puede calcularse una sola vez por cada paso del decodificador (ya que no depende de $j$), y los productos $\mathbf{W}_2 \mathbf{h}_j$ pueden pre-calcularse una sola vez para toda la secuencia. El número total de parámetros aprendibles en el módulo de atención es $m \cdot d_a + 2n \cdot d_a + d_a$, correspondiente a $\mathbf{W}_1$, $\mathbf{W}_2$ y $\mathbf{v}$ respectivamente.

---

## 5.3 Atención de Luong (Atención Multiplicativa)

### 5.3.1 Motivación y contexto

Poco después del trabajo de Bahdanau, Minh-Thang Luong, Hieu Pham e Ilya Manning propusieron variantes simplificadas del mecanismo de atención en su artículo *"Effective Approaches to Attention-based Neural Machine Translation"* (Luong et al., 2015). El trabajo de Luong se distingue por proponer funciones de puntuación más eficientes computacionalmente y por explorar diferentes estrategias de integración de la atención con el decodificador.

### 5.3.2 Funciones de puntuación

Luong et al. propusieron tres variantes de la función de puntuación:

**1. Atención dot-product (producto punto):**

$$e_{ij} = \mathbf{s}_i^T \mathbf{h}_j$$

Esta es la variante más simple: la puntuación de alineación es simplemente el producto punto entre el estado del decodificador $\mathbf{s}_i$ y el estado del codificador $\mathbf{h}_j$. El producto punto mide la similitud coseno (no normalizada) entre los dos vectores, por lo que posiciones cuyas representaciones son más similares al estado actual del decodificador recibirán puntuaciones más altas.

**Requisito dimensional:** Para que el producto punto sea válido, ambos vectores deben tener la misma dimensión: $\mathbf{s}_i, \mathbf{h}_j \in \mathbb{R}^n$. Esto puede requerir que el codificador y el decodificador tengan el mismo tamaño de estado oculto, o que se aplique una proyección previa.

**Ventaja:** No tiene parámetros aprendibles adicionales, lo que reduce el riesgo de sobreajuste y acelera el entrenamiento.

**2. Atención general (bilineal):**

$$e_{ij} = \mathbf{s}_i^T \mathbf{W} \mathbf{h}_j$$

Aquí se introduce una matriz de pesos $\mathbf{W} \in \mathbb{R}^{m \times n}$ que permite una interacción más rica entre los estados del decodificador y del codificador. Esta formulación puede verse como una **forma bilineal**: primero se transforma $\mathbf{h}_j$ mediante $\mathbf{W}$, y luego se calcula el producto punto con $\mathbf{s}_i$. La matriz $\mathbf{W}$ aprende qué combinaciones de dimensiones del codificador y del decodificador son más informativas para determinar la alineación.

**Ventaja sobre dot-product:** Permite que codificador y decodificador tengan dimensiones diferentes ($m \neq n$), y puede capturar relaciones más complejas entre las representaciones.

**3. Atención concatenativa (similar a Bahdanau):**

$$e_{ij} = \mathbf{v}^T \tanh(\mathbf{W}[\mathbf{s}_i; \mathbf{h}_j])$$

donde $[\mathbf{s}_i; \mathbf{h}_j]$ denota la concatenación de ambos vectores. Esta variante es funcionalmente equivalente a la atención de Bahdanau, pero con una formulación ligeramente diferente.

### 5.3.3 Diferencias clave con la atención de Bahdanau

| Aspecto | Bahdanau | Luong |
|---------|----------|-------|
| Estado del decodificador | $\mathbf{s}_{i-1}$ (paso anterior) | $\mathbf{s}_i$ (paso actual) |
| Codificador | Bidireccional | Unidireccional (generalmente) |
| Función de puntuación | Aditiva (feedforward) | Multiplicativa (producto punto/bilineal) |
| Cálculo del contexto | Antes de actualizar $\mathbf{s}_i$ | Después de calcular $\mathbf{s}_i$ |
| Complejidad | Mayor (red feedforward) | Menor (producto punto) |

Una diferencia sutil pero importante es el momento en que se utiliza el estado del decodificador. En la atención de Bahdanau, se usa $\mathbf{s}_{i-1}$ (el estado anterior), porque el vector de contexto $\mathbf{c}_i$ se necesita como entrada para calcular $\mathbf{s}_i$. En la atención de Luong, se usa $\mathbf{s}_i$ (el estado actual), calculado sin atención, y luego se combina con el vector de contexto:

$$\tilde{\mathbf{s}}_i = \tanh(\mathbf{W}_c [\mathbf{c}_i; \mathbf{s}_i])$$

$$P(y_i \mid y_1, \ldots, y_{i-1}, \mathbf{x}) = \text{softmax}(\mathbf{W}_o \tilde{\mathbf{s}}_i)$$

### 5.3.4 Eficiencia computacional

La atención multiplicativa (dot-product y general) es significativamente más eficiente que la atención aditiva. El producto punto $\mathbf{s}_i^T \mathbf{h}_j$ es una operación $O(n)$, mientras que la atención aditiva requiere dos multiplicaciones matriz-vector más la aplicación de $\tanh$, resultando en $O(d_a \cdot (m + n))$. En la práctica, para las dimensiones típicas utilizadas en redes neuronales modernas, la atención multiplicativa puede ser hasta 2-3 veces más rápida.

Además, las puntuaciones de todas las posiciones pueden calcularse en una sola operación matricial:

$$\mathbf{e}_i = \mathbf{s}_i^T \mathbf{H}$$

donde $\mathbf{H} = [\mathbf{h}_1, \mathbf{h}_2, \ldots, \mathbf{h}_T] \in \mathbb{R}^{n \times T}$ es la matriz de estados ocultos del codificador. Esto permite una implementación altamente eficiente mediante operaciones matriciales paralelas en GPUs modernas.

---

## 5.4 Self-Attention (Auto-Atención)

### 5.4.1 De la atención cruzada a la auto-atención

Los mecanismos de atención que hemos estudiado hasta ahora son ejemplos de **atención cruzada** (*cross-attention*): el decodificador atiende a los estados del codificador, es decir, la "consulta" proviene de una secuencia y las "respuestas" provienen de otra secuencia diferente. Pero, ¿qué sucede si aplicamos el mismo principio dentro de una misma secuencia?

La **auto-atención** (*self-attention*), también conocida como **atención intra-secuencia** (*intra-attention*), es un mecanismo en el que cada elemento de una secuencia atiende a todos los demás elementos de **la misma secuencia**. Esto permite que el modelo capture dependencias y relaciones entre todas las posiciones de la secuencia, independientemente de su distancia.

La auto-atención fue popularizada por Vaswani et al. (2017) en su trabajo seminal *"Attention Is All You Need"*, donde se demostró que los mecanismos de atención podían reemplazar completamente las redes recurrentes y convolucionales para el procesamiento de secuencias.

### 5.4.2 Queries, Keys y Values

La formulación moderna de la auto-atención se basa en tres conceptos fundamentales: **consultas** (*queries*, $\mathbf{Q}$), **claves** (*keys*, $\mathbf{K}$) y **valores** (*values*, $\mathbf{V}$). Estos tres componentes se derivan de la misma secuencia de entrada mediante transformaciones lineales aprendidas.

Dada una secuencia de entrada representada como una matriz $\mathbf{X} \in \mathbb{R}^{T \times d}$, donde $T$ es la longitud de la secuencia y $d$ es la dimensión de los embeddings, las matrices $\mathbf{Q}$, $\mathbf{K}$ y $\mathbf{V}$ se calculan como:

$$\mathbf{Q} = \mathbf{X}\mathbf{W}^Q \in \mathbb{R}^{T \times d_k}$$

$$\mathbf{K} = \mathbf{X}\mathbf{W}^K \in \mathbb{R}^{T \times d_k}$$

$$\mathbf{V} = \mathbf{X}\mathbf{W}^V \in \mathbb{R}^{T \times d_v}$$

donde:

- $\mathbf{W}^Q \in \mathbb{R}^{d \times d_k}$ es la matriz de proyección de consultas.
- $\mathbf{W}^K \in \mathbb{R}^{d \times d_k}$ es la matriz de proyección de claves.
- $\mathbf{W}^V \in \mathbb{R}^{d \times d_v}$ es la matriz de proyección de valores.
- $d_k$ es la dimensión de las consultas y claves (deben coincidir para el producto punto).
- $d_v$ es la dimensión de los valores (puede diferir de $d_k$).

Cada fila de $\mathbf{Q}$, $\mathbf{K}$ y $\mathbf{V}$ corresponde a un token de la secuencia. El token en la posición $t$ tiene:

- **Consulta** $\mathbf{q}_t = \mathbf{x}_t \mathbf{W}^Q$: Representa "lo que este token está buscando" — la información que necesita de otros tokens.
- **Clave** $\mathbf{k}_t = \mathbf{x}_t \mathbf{W}^K$: Representa "lo que este token ofrece" — un índice de la información que contiene.
- **Valor** $\mathbf{v}_t = \mathbf{x}_t \mathbf{W}^V$: Representa "el contenido real" — la información que se transmitirá si este token es seleccionado.

### 5.4.3 La analogía de la biblioteca

Para desarrollar una intuición más profunda sobre el mecanismo query-key-value, consideremos la **analogía de la biblioteca**:

Imaginemos que estamos en una biblioteca y necesitamos encontrar información para responder una pregunta de investigación.

- **Query (Consulta) = La pregunta del investigador:** Es lo que buscamos. Cada token formula su propia pregunta: "¿Qué información del contexto me es útil?"

- **Key (Clave) = El catálogo o índice de los libros:** Cada libro (token) tiene una entrada en el catálogo que describe brevemente su contenido. No es el contenido completo del libro, sino una descripción resumida que permite determinar si el libro es relevante para nuestra pregunta.

- **Value (Valor) = El contenido real de los libros:** Una vez que determinamos que un libro es relevante (comparando nuestra consulta con la entrada del catálogo), extraemos el contenido real del libro.

El proceso de atención es entonces análogo a:

1. **Formular la consulta** (calcular $\mathbf{Q}$): El investigador articula qué información necesita.
2. **Comparar con el catálogo** (calcular $\mathbf{Q}\mathbf{K}^T$): Se compara la consulta con cada entrada del catálogo para determinar la relevancia de cada libro.
3. **Asignar relevancias** (aplicar softmax): Se normalizan las puntuaciones de relevancia para obtener una distribución de probabilidad.
4. **Extraer información** (multiplicar por $\mathbf{V}$): Se extrae y combina el contenido de los libros relevantes, ponderado por su relevancia.

La separación entre claves y valores es conceptualmente importante: las claves determinan **si** un token es relevante, y los valores determinan **qué información** se extrae de ese token. Esta separación permite que el mecanismo sea más flexible: un token podría contener cierta información (valor) pero ser recuperable mediante diferentes tipos de consultas (clave).

### 5.4.4 Scaled Dot-Product Attention

La formulación completa de la atención de producto punto escalado (*Scaled Dot-Product Attention*) es:

$$\text{Attention}(\mathbf{Q}, \mathbf{K}, \mathbf{V}) = \text{softmax}\left(\frac{\mathbf{Q}\mathbf{K}^T}{\sqrt{d_k}}\right)\mathbf{V}$$

Analicemos cada paso de esta ecuación con detalle minucioso:

**Paso 1: Calcular las puntuaciones brutas $\mathbf{Q}\mathbf{K}^T$**

El producto matricial $\mathbf{Q}\mathbf{K}^T \in \mathbb{R}^{T \times T}$ produce una **matriz de puntuaciones** donde el elemento $(i, j)$ es:

$$(\mathbf{Q}\mathbf{K}^T)_{ij} = \mathbf{q}_i^T \mathbf{k}_j = \sum_{l=1}^{d_k} q_{il} \cdot k_{jl}$$

Esta puntuación mide la **compatibilidad** o **afinidad** entre la consulta del token $i$ y la clave del token $j$. Un valor alto indica que el token $j$ contiene información relevante para lo que el token $i$ está buscando. La matriz resultante tiene dimensión $T \times T$, representando todas las relaciones par a par entre los $T$ tokens de la secuencia.

**Paso 2: Escalar por $\sqrt{d_k}$**

$$\frac{\mathbf{Q}\mathbf{K}^T}{\sqrt{d_k}}$$

El factor de escalamiento $\frac{1}{\sqrt{d_k}}$ es crucial para la estabilidad numérica del entrenamiento. La justificación es la siguiente:

Supongamos que los componentes de $\mathbf{q}_i$ y $\mathbf{k}_j$ son variables aleatorias independientes con media 0 y varianza 1. Entonces, el producto punto $\mathbf{q}_i^T \mathbf{k}_j = \sum_{l=1}^{d_k} q_{il} k_{jl}$ tiene:

$$\mathbb{E}[\mathbf{q}_i^T \mathbf{k}_j] = \sum_{l=1}^{d_k} \mathbb{E}[q_{il}] \cdot \mathbb{E}[k_{jl}] = 0$$

$$\text{Var}[\mathbf{q}_i^T \mathbf{k}_j] = \sum_{l=1}^{d_k} \text{Var}[q_{il} k_{jl}] = d_k$$

Es decir, la varianza del producto punto crece linealmente con $d_k$. Para valores grandes de $d_k$ (por ejemplo, $d_k = 64$ o $d_k = 128$), los productos punto pueden tener magnitudes muy grandes. Cuando valores de gran magnitud entran en la función softmax, esta produce distribuciones extremadamente concentradas (cercanas a *one-hot*), lo que resulta en gradientes extremadamente pequeños (casi cero), dificultando severamente el aprendizaje.

Al dividir por $\sqrt{d_k}$, el producto punto escalado $\frac{\mathbf{q}_i^T \mathbf{k}_j}{\sqrt{d_k}}$ tiene varianza 1, independientemente de $d_k$, lo que mantiene la softmax en una región de operación con gradientes informativos.

**Paso 3: Aplicar softmax**

$$\alpha_{ij} = \text{softmax}\left(\frac{\mathbf{q}_i^T \mathbf{k}_j}{\sqrt{d_k}}\right)_j = \frac{\exp\left(\frac{\mathbf{q}_i^T \mathbf{k}_j}{\sqrt{d_k}}\right)}{\sum_{l=1}^{T} \exp\left(\frac{\mathbf{q}_i^T \mathbf{k}_l}{\sqrt{d_k}}\right)}$$

La softmax se aplica **por filas** de la matriz $\frac{\mathbf{Q}\mathbf{K}^T}{\sqrt{d_k}}$. Cada fila $i$ se convierte en una distribución de probabilidad sobre las $T$ posiciones, determinando cómo el token $i$ distribuye su atención sobre todos los tokens. Después de la softmax, la suma de cada fila es 1:

$$\sum_{j=1}^{T} \alpha_{ij} = 1, \quad \forall i$$

La matriz $\boldsymbol{\alpha} \in \mathbb{R}^{T \times T}$ resultante se denomina **matriz de pesos de atención** y es una de las herramientas más valiosas para la interpretabilidad de los modelos basados en atención.

**Paso 4: Calcular la salida ponderada**

$$\text{Attention}(\mathbf{Q}, \mathbf{K}, \mathbf{V}) = \boldsymbol{\alpha} \mathbf{V} \in \mathbb{R}^{T \times d_v}$$

La multiplicación de la matriz de pesos de atención $\boldsymbol{\alpha}$ por la matriz de valores $\mathbf{V}$ produce la **salida de la atención**. Cada fila $i$ del resultado es:

$$\text{output}_i = \sum_{j=1}^{T} \alpha_{ij} \mathbf{v}_j$$

Es decir, la salida para cada token es una **suma ponderada de los valores de todos los tokens**, donde los pesos están determinados por las afinidades query-key. Los tokens más relevantes (con $\alpha_{ij}$ alto) contribuyen más a la representación actualizada del token $i$.

### 5.4.5 Propiedades fundamentales de la auto-atención

**1. Conexiones directas entre cualquier par de tokens:** A diferencia de las RNN, donde la información entre posiciones distantes debe propagarse a través de múltiples pasos temporales (dando lugar al problema del desvanecimiento del gradiente), la auto-atención establece **conexiones directas** entre todas las posiciones. La distancia máxima del camino de señal entre cualquier par de posiciones es $O(1)$, comparado con $O(T)$ en una RNN y $O(\log T)$ en una red convolucional dilatada.

**2. Paralelización completa:** Todas las puntuaciones de atención pueden calcularse simultáneamente, ya que no existen dependencias secuenciales (a diferencia de las RNN). Esto permite una utilización eficiente del hardware paralelo moderno (GPUs, TPUs).

**3. Complejidad computacional:** La complejidad temporal de la auto-atención es $O(T^2 \cdot d_k)$ para el cálculo de $\mathbf{Q}\mathbf{K}^T$, y $O(T^2 \cdot d_v)$ para la multiplicación por $\mathbf{V}$. La complejidad cuadrática en $T$ es la principal limitación de la auto-atención para secuencias muy largas, lo que ha motivado investigación significativa en variantes de atención eficiente (como Linformer, Performer, etc.).

**Figura 5.2:** *Diagrama esquemático del mecanismo de Scaled Dot-Product Attention. En la parte superior se muestran tres flujos de entrada paralelos: la matriz de entrada $\mathbf{X}$ (representada como una secuencia de vectores de embedding apilados verticalmente) se multiplica por tres matrices de proyección $\mathbf{W}^Q$, $\mathbf{W}^K$ y $\mathbf{W}^V$ (mostradas como rectángulos con flechas salientes) para producir las matrices $\mathbf{Q}$, $\mathbf{K}$ y $\mathbf{V}$ respectivamente. En la parte central se ilustra el cálculo del producto punto: $\mathbf{Q}$ y $\mathbf{K}^T$ (transpuesta de $\mathbf{K}$) se combinan mediante multiplicación matricial, generando la matriz de puntuaciones $\mathbf{Q}\mathbf{K}^T$ de dimensión $T \times T$, visualizada como un mapa de calor cuadrado. A continuación, un bloque de escala divide cada elemento por $\sqrt{d_k}$, seguido de un bloque softmax aplicado por filas que produce la matriz de pesos de atención $\boldsymbol{\alpha}$ (otro mapa de calor, ahora con filas que suman a 1). Finalmente, $\boldsymbol{\alpha}$ se multiplica por $\mathbf{V}$ para obtener la salida de dimensión $T \times d_v$. Debajo del diagrama se muestra un ejemplo de mapa de calor de atención para una oración corta, donde la intensidad del color indica la fuerza de la atención entre cada par de palabras.*

---

## 5.5 Ejemplo detallado paso a paso

Para consolidar la comprensión del mecanismo de auto-atención, trabajaremos un ejemplo numérico completo con la oración en español: **"El gato se sentó"**.

### 5.5.1 Configuración del ejemplo

Consideremos una secuencia de 4 tokens: $x_1 = \text{"El"}$, $x_2 = \text{"gato"}$, $x_3 = \text{"se"}$, $x_4 = \text{"sentó"}$.

Para simplificar los cálculos, utilizaremos embeddings de dimensión $d = 4$ y dimensiones de atención $d_k = d_v = 3$.

**Embeddings de entrada** (valores ilustrativos asignados para facilitar el cálculo):

$$\mathbf{x}_1 = \begin{bmatrix} 1.0 \\ 0.0 \\ 1.0 \\ 0.0 \end{bmatrix}, \quad \mathbf{x}_2 = \begin{bmatrix} 0.0 \\ 1.0 \\ 0.0 \\ 1.0 \end{bmatrix}, \quad \mathbf{x}_3 = \begin{bmatrix} 1.0 \\ 1.0 \\ 0.0 \\ 0.0 \end{bmatrix}, \quad \mathbf{x}_4 = \begin{bmatrix} 0.0 \\ 0.0 \\ 1.0 \\ 1.0 \end{bmatrix}$$

La matriz de entrada es:

$$\mathbf{X} = \begin{bmatrix} 1.0 & 0.0 & 1.0 & 0.0 \\ 0.0 & 1.0 & 0.0 & 1.0 \\ 1.0 & 1.0 & 0.0 & 0.0 \\ 0.0 & 0.0 & 1.0 & 1.0 \end{bmatrix} \in \mathbb{R}^{4 \times 4}$$

### 5.5.2 Definición de las matrices de proyección

Definimos matrices de pesos $\mathbf{W}^Q, \mathbf{W}^K \in \mathbb{R}^{4 \times 3}$ y $\mathbf{W}^V \in \mathbb{R}^{4 \times 3}$:

$$\mathbf{W}^Q = \begin{bmatrix} 1 & 0 & 1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \\ 1 & 1 & 0 \end{bmatrix}, \quad \mathbf{W}^K = \begin{bmatrix} 0 & 1 & 1 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \\ 1 & 0 & 1 \end{bmatrix}, \quad \mathbf{W}^V = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \\ 1 & 1 & 0 \end{bmatrix}$$

### 5.5.3 Cálculo de Q, K, V

**Cálculo de $\mathbf{Q} = \mathbf{X}\mathbf{W}^Q$:**

Para la primera fila (token "El", $\mathbf{x}_1 = [1, 0, 1, 0]$):

$$\mathbf{q}_1 = [1 \cdot 1 + 0 \cdot 0 + 1 \cdot 0 + 0 \cdot 1, \; 1 \cdot 0 + 0 \cdot 1 + 1 \cdot 0 + 0 \cdot 1, \; 1 \cdot 1 + 0 \cdot 0 + 1 \cdot 1 + 0 \cdot 0] = [1, 0, 2]$$

Para "gato" ($\mathbf{x}_2 = [0, 1, 0, 1]$):

$$\mathbf{q}_2 = [0 + 0 + 0 + 1, \; 0 + 1 + 0 + 1, \; 0 + 0 + 0 + 0] = [1, 2, 0]$$

Para "se" ($\mathbf{x}_3 = [1, 1, 0, 0]$):

$$\mathbf{q}_3 = [1 + 0 + 0 + 0, \; 0 + 1 + 0 + 0, \; 1 + 0 + 0 + 0] = [1, 1, 1]$$

Para "sentó" ($\mathbf{x}_4 = [0, 0, 1, 1]$):

$$\mathbf{q}_4 = [0 + 0 + 0 + 1, \; 0 + 0 + 0 + 1, \; 0 + 0 + 1 + 0] = [1, 1, 1]$$

$$\mathbf{Q} = \begin{bmatrix} 1 & 0 & 2 \\ 1 & 2 & 0 \\ 1 & 1 & 1 \\ 1 & 1 & 1 \end{bmatrix}$$

**Cálculo de $\mathbf{K} = \mathbf{X}\mathbf{W}^K$:**

Para "El" ($\mathbf{x}_1 = [1, 0, 1, 0]$):

$$\mathbf{k}_1 = [0 + 0 + 0 + 0, \; 1 + 0 + 0 + 0, \; 1 + 0 + 1 + 0] = [0, 1, 2]$$

Para "gato" ($\mathbf{x}_2 = [0, 1, 0, 1]$):

$$\mathbf{k}_2 = [0 + 1 + 0 + 1, \; 0 + 0 + 0 + 0, \; 0 + 0 + 0 + 1] = [2, 0, 1]$$

Para "se" ($\mathbf{x}_3 = [1, 1, 0, 0]$):

$$\mathbf{k}_3 = [0 + 1 + 0 + 0, \; 1 + 0 + 0 + 0, \; 1 + 0 + 0 + 0] = [1, 1, 1]$$

Para "sentó" ($\mathbf{x}_4 = [0, 0, 1, 1]$):

$$\mathbf{k}_4 = [0 + 0 + 0 + 1, \; 0 + 0 + 0 + 0, \; 0 + 0 + 1 + 1] = [1, 0, 2]$$

$$\mathbf{K} = \begin{bmatrix} 0 & 1 & 2 \\ 2 & 0 & 1 \\ 1 & 1 & 1 \\ 1 & 0 & 2 \end{bmatrix}$$

**Cálculo de $\mathbf{V} = \mathbf{X}\mathbf{W}^V$:**

Para "El" ($\mathbf{x}_1 = [1, 0, 1, 0]$):

$$\mathbf{v}_1 = [1 + 0 + 0 + 0, \; 0 + 0 + 0 + 0, \; 0 + 0 + 1 + 0] = [1, 0, 1]$$

Para "gato" ($\mathbf{x}_2 = [0, 1, 0, 1]$):

$$\mathbf{v}_2 = [0 + 0 + 0 + 1, \; 0 + 1 + 0 + 1, \; 0 + 0 + 0 + 0] = [1, 2, 0]$$

Para "se" ($\mathbf{x}_3 = [1, 1, 0, 0]$):

$$\mathbf{v}_3 = [1 + 0 + 0 + 0, \; 0 + 1 + 0 + 0, \; 0 + 0 + 0 + 0] = [1, 1, 0]$$

Para "sentó" ($\mathbf{x}_4 = [0, 0, 1, 1]$):

$$\mathbf{v}_4 = [0 + 0 + 0 + 1, \; 0 + 0 + 0 + 1, \; 0 + 0 + 1 + 0] = [1, 1, 1]$$

$$\mathbf{V} = \begin{bmatrix} 1 & 0 & 1 \\ 1 & 2 & 0 \\ 1 & 1 & 0 \\ 1 & 1 & 1 \end{bmatrix}$$

### 5.5.4 Cálculo de $\mathbf{Q}\mathbf{K}^T$

Ahora calculamos la matriz de puntuaciones brutas. Recordemos que $\mathbf{K}^T \in \mathbb{R}^{3 \times 4}$:

$$\mathbf{K}^T = \begin{bmatrix} 0 & 2 & 1 & 1 \\ 1 & 0 & 1 & 0 \\ 2 & 1 & 1 & 2 \end{bmatrix}$$

Calculemos $\mathbf{Q}\mathbf{K}^T$ elemento por elemento:

**Fila 1 (token "El", $\mathbf{q}_1 = [1, 0, 2]$):**

- $\mathbf{q}_1 \cdot \mathbf{k}_1 = 1 \cdot 0 + 0 \cdot 1 + 2 \cdot 2 = 4$
- $\mathbf{q}_1 \cdot \mathbf{k}_2 = 1 \cdot 2 + 0 \cdot 0 + 2 \cdot 1 = 4$
- $\mathbf{q}_1 \cdot \mathbf{k}_3 = 1 \cdot 1 + 0 \cdot 1 + 2 \cdot 1 = 3$
- $\mathbf{q}_1 \cdot \mathbf{k}_4 = 1 \cdot 1 + 0 \cdot 0 + 2 \cdot 2 = 5$

**Fila 2 (token "gato", $\mathbf{q}_2 = [1, 2, 0]$):**

- $\mathbf{q}_2 \cdot \mathbf{k}_1 = 1 \cdot 0 + 2 \cdot 1 + 0 \cdot 2 = 2$
- $\mathbf{q}_2 \cdot \mathbf{k}_2 = 1 \cdot 2 + 2 \cdot 0 + 0 \cdot 1 = 2$
- $\mathbf{q}_2 \cdot \mathbf{k}_3 = 1 \cdot 1 + 2 \cdot 1 + 0 \cdot 1 = 3$
- $\mathbf{q}_2 \cdot \mathbf{k}_4 = 1 \cdot 1 + 2 \cdot 0 + 0 \cdot 2 = 1$

**Fila 3 (token "se", $\mathbf{q}_3 = [1, 1, 1]$):**

- $\mathbf{q}_3 \cdot \mathbf{k}_1 = 1 \cdot 0 + 1 \cdot 1 + 1 \cdot 2 = 3$
- $\mathbf{q}_3 \cdot \mathbf{k}_2 = 1 \cdot 2 + 1 \cdot 0 + 1 \cdot 1 = 3$
- $\mathbf{q}_3 \cdot \mathbf{k}_3 = 1 \cdot 1 + 1 \cdot 1 + 1 \cdot 1 = 3$
- $\mathbf{q}_3 \cdot \mathbf{k}_4 = 1 \cdot 1 + 1 \cdot 0 + 1 \cdot 2 = 3$

**Fila 4 (token "sentó", $\mathbf{q}_4 = [1, 1, 1]$):**

Los cálculos son idénticos a la fila 3 ya que $\mathbf{q}_4 = \mathbf{q}_3$:

- $[3, 3, 3, 3]$

Resultado completo:

$$\mathbf{Q}\mathbf{K}^T = \begin{bmatrix} 4 & 4 & 3 & 5 \\ 2 & 2 & 3 & 1 \\ 3 & 3 & 3 & 3 \\ 3 & 3 & 3 & 3 \end{bmatrix}$$

### 5.5.5 Escalamiento por $\sqrt{d_k}$

Con $d_k = 3$, tenemos $\sqrt{d_k} = \sqrt{3} \approx 1.732$:

$$\frac{\mathbf{Q}\mathbf{K}^T}{\sqrt{d_k}} = \begin{bmatrix} 2.309 & 2.309 & 1.732 & 2.887 \\ 1.155 & 1.155 & 1.732 & 0.577 \\ 1.732 & 1.732 & 1.732 & 1.732 \\ 1.732 & 1.732 & 1.732 & 1.732 \end{bmatrix}$$

### 5.5.6 Aplicación de softmax

Aplicamos softmax por filas. Para la fila 1:

$$\exp(2.309) \approx 10.06, \quad \exp(2.309) \approx 10.06, \quad \exp(1.732) \approx 5.65, \quad \exp(2.887) \approx 17.94$$

Suma: $10.06 + 10.06 + 5.65 + 17.94 = 43.71$

$$\alpha_{1,:} = \left[\frac{10.06}{43.71}, \frac{10.06}{43.71}, \frac{5.65}{43.71}, \frac{17.94}{43.71}\right] = [0.230, 0.230, 0.129, 0.410]$$

Para la fila 2:

$$\exp(1.155) \approx 3.17, \quad \exp(1.155) \approx 3.17, \quad \exp(1.732) \approx 5.65, \quad \exp(0.577) \approx 1.78$$

Suma: $3.17 + 3.17 + 5.65 + 1.78 = 13.77$

$$\alpha_{2,:} = [0.230, 0.230, 0.410, 0.129]$$

Para las filas 3 y 4, todos los valores escalados son iguales ($1.732$), por lo que la softmax produce una distribución uniforme:

$$\alpha_{3,:} = \alpha_{4,:} = [0.25, 0.25, 0.25, 0.25]$$

Matriz de pesos de atención completa:

$$\boldsymbol{\alpha} = \begin{bmatrix} 0.230 & 0.230 & 0.129 & 0.410 \\ 0.230 & 0.230 & 0.410 & 0.129 \\ 0.250 & 0.250 & 0.250 & 0.250 \\ 0.250 & 0.250 & 0.250 & 0.250 \end{bmatrix}$$

### 5.5.7 Cálculo de la salida $\boldsymbol{\alpha}\mathbf{V}$

Finalmente, multiplicamos la matriz de atención por la matriz de valores:

**Fila 1 (representación actualizada de "El"):**

$$\text{out}_1 = 0.230 \cdot [1, 0, 1] + 0.230 \cdot [1, 2, 0] + 0.129 \cdot [1, 1, 0] + 0.410 \cdot [1, 1, 1]$$

$$= [0.230, 0, 0.230] + [0.230, 0.460, 0] + [0.129, 0.129, 0] + [0.410, 0.410, 0.410]$$

$$= [0.999, 0.999, 0.640]$$

$$\approx [1.00, 1.00, 0.64]$$

**Fila 2 (representación actualizada de "gato"):**

$$\text{out}_2 = 0.230 \cdot [1, 0, 1] + 0.230 \cdot [1, 2, 0] + 0.410 \cdot [1, 1, 0] + 0.129 \cdot [1, 1, 1]$$

$$= [0.230, 0, 0.230] + [0.230, 0.460, 0] + [0.410, 0.410, 0] + [0.129, 0.129, 0.129]$$

$$= [0.999, 0.999, 0.359]$$

$$\approx [1.00, 1.00, 0.36]$$

**Fila 3 (representación actualizada de "se"):**

$$\text{out}_3 = 0.25 \cdot [1, 0, 1] + 0.25 \cdot [1, 2, 0] + 0.25 \cdot [1, 1, 0] + 0.25 \cdot [1, 1, 1]$$

$$= [0.25, 0, 0.25] + [0.25, 0.50, 0] + [0.25, 0.25, 0] + [0.25, 0.25, 0.25]$$

$$= [1.00, 1.00, 0.50]$$

**Fila 4 (representación actualizada de "sentó"):**

$$\text{out}_4 = [1.00, 1.00, 0.50]$$

(Idéntico a la fila 3, ya que los pesos de atención son iguales.)

Resultado final:

$$\text{Attention}(\mathbf{Q}, \mathbf{K}, \mathbf{V}) = \begin{bmatrix} 1.00 & 1.00 & 0.64 \\ 1.00 & 1.00 & 0.36 \\ 1.00 & 1.00 & 0.50 \\ 1.00 & 1.00 & 0.50 \end{bmatrix}$$

### 5.5.8 Interpretación de los resultados

Analicemos los pesos de atención para extraer información semántica:

**Token "El" (fila 1: $[0.230, 0.230, 0.129, 0.410]$):**
El artículo "El" presta la mayor atención al verbo "sentó" ($\alpha = 0.410$) y una atención considerable al sustantivo "gato" ($\alpha = 0.230$). Esto tiene sentido lingüístico: el artículo definido se relaciona directamente con el sustantivo que determina y, a través de la concordancia, con el verbo principal de la oración.

**Token "gato" (fila 2: $[0.230, 0.230, 0.410, 0.129]$):**
El sustantivo "gato" presta la mayor atención al pronombre reflexivo "se" ($\alpha = 0.410$). Esto refleja la relación sintáctica entre el sujeto y el pronombre reflexivo en la construcción "se sentó": el pronombre "se" está directamente vinculado al sujeto "gato" que realiza la acción.

**Tokens "se" y "sentó" (filas 3-4: $[0.25, 0.25, 0.25, 0.25]$):**
La atención uniforme indica que, con estos embeddings y pesos particulares, estos tokens no distinguen entre las diferentes posiciones. En un modelo entrenado con datos reales, estas distribuciones serían considerablemente más informativas.

Este ejemplo, aunque simplificado, ilustra cómo la auto-atención permite a cada token construir una representación contextualizada que incorpora información de toda la secuencia, con énfasis diferenciado según las relaciones aprendidas.

---

## 5.6 Multi-Head Attention (Atención Multi-Cabeza)

### 5.6.1 Limitaciones de una sola cabeza de atención

La auto-atención con una única cabeza (*single-head attention*) tiene una limitación fundamental: para cada par de tokens, produce una **única puntuación de atención** $\alpha_{ij}$. Sin embargo, las relaciones entre tokens son multifacéticas. Consideremos la palabra "banco" en la oración "El banco del parque está cerca del banco de inversiones". La palabra "banco" en cada aparición necesita atender a diferentes palabras según el tipo de relación:

- **Relación semántica:** "banco" (asiento) debería atender a "parque"; "banco" (institución) debería atender a "inversiones".
- **Relación sintáctica:** Ambos "banco" deberían atender al artículo "El" y a la preposición "del".
- **Relación posicional:** Cada "banco" podría atender a palabras cercanas para captar contexto local.

Una única cabeza de atención debe comprimir todas estas relaciones diversas en un único conjunto de pesos, lo que limita la riqueza representacional del modelo.

### 5.6.2 Formulación matemática

La **atención multi-cabeza** (*Multi-Head Attention*, MHA) aborda esta limitación ejecutando múltiples operaciones de atención en paralelo, cada una con sus propias matrices de proyección. Formalmente, dadas $h$ cabezas de atención:

$$\text{head}_i = \text{Attention}(\mathbf{Q}\mathbf{W}_i^Q, \mathbf{K}\mathbf{W}_i^K, \mathbf{V}\mathbf{W}_i^V), \quad i = 1, 2, \ldots, h$$

donde las matrices de proyección para la cabeza $i$ son:

- $\mathbf{W}_i^Q \in \mathbb{R}^{d_{\text{model}} \times d_k}$
- $\mathbf{W}_i^K \in \mathbb{R}^{d_{\text{model}} \times d_k}$
- $\mathbf{W}_i^V \in \mathbb{R}^{d_{\text{model}} \times d_v}$

Cada cabeza $i$ proyecta las consultas, claves y valores a un subespacio de menor dimensión y calcula la atención de forma independiente. Los resultados de todas las cabezas se concatenan y se proyectan de vuelta al espacio original:

$$\text{MultiHead}(\mathbf{Q}, \mathbf{K}, \mathbf{V}) = \text{Concat}(\text{head}_1, \text{head}_2, \ldots, \text{head}_h) \mathbf{W}^O$$

donde $\mathbf{W}^O \in \mathbb{R}^{h \cdot d_v \times d_{\text{model}}}$ es la matriz de proyección de salida.

### 5.6.3 Desglose dimensional

Para mantener la complejidad computacional comparable a la de una atención de cabeza única, las dimensiones de cada cabeza se reducen proporcionalmente al número de cabezas:

$$d_k = d_v = \frac{d_{\text{model}}}{h}$$

Con esta elección, las dimensiones de las diferentes matrices y tensores son:

| Componente | Dimensión |
|-----------|-----------|
| Entrada $\mathbf{X}$ | $T \times d_{\text{model}}$ |
| Proyección por cabeza $\mathbf{W}_i^Q$ | $d_{\text{model}} \times d_k$ |
| $\mathbf{Q}_i = \mathbf{X}\mathbf{W}_i^Q$ | $T \times d_k$ |
| $\mathbf{Q}_i \mathbf{K}_i^T$ | $T \times T$ |
| Salida por cabeza $\text{head}_i$ | $T \times d_v$ |
| Concatenación | $T \times (h \cdot d_v) = T \times d_{\text{model}}$ |
| Proyección de salida $\mathbf{W}^O$ | $d_{\text{model}} \times d_{\text{model}}$ |
| Salida final | $T \times d_{\text{model}}$ |

La dimensión de salida $T \times d_{\text{model}}$ es la misma que la de entrada, lo que permite apilar múltiples capas de atención multi-cabeza de forma composicional.

### 5.6.4 Intuición: ¿por qué múltiples cabezas?

Cada cabeza de atención aprende a especializarse en un **tipo diferente de relación** entre tokens. Investigaciones empíricas han revelado patrones de especialización notables:

1. **Cabezas sintácticas:** Algunas cabezas aprenden relaciones gramaticales, como la relación sujeto-verbo, determinante-sustantivo, o modificador-núcleo.

2. **Cabezas posicionales:** Algunas cabezas aprenden patrones de atención basados en la distancia relativa, atendiendo preferentemente a tokens adyacentes (capturando n-gramas) o a posiciones fijas.

3. **Cabezas semánticas:** Otras cabezas capturan relaciones semánticas, como correferencialidad (pronombres que refieren al mismo antecedente), sinonimia contextual o relaciones temáticas.

4. **Cabezas de copia:** En modelos de lenguaje, algunas cabezas aprenden a "copiar" tokens anteriores a posiciones posteriores, lo que es esencial para tareas como la repetición y la referencia.

La combinación de múltiples perspectivas a través de la concatenación y la proyección de salida $\mathbf{W}^O$ permite al modelo integrar información de diversas naturalezas en una representación unificada.

Formalmente, la proyección de salida $\mathbf{W}^O$ aprende a **fusionar** las diferentes perspectivas:

$$\text{output} = [\text{head}_1; \text{head}_2; \ldots; \text{head}_h] \mathbf{W}^O$$

donde cada $\text{head}_i \in \mathbb{R}^{T \times d_v}$ captura un aspecto diferente de las relaciones inter-token, y $\mathbf{W}^O$ aprende la combinación óptima de estas perspectivas para la tarea en cuestión.

### 5.6.5 Análisis de parámetros

Calculemos el número total de parámetros del módulo de atención multi-cabeza:

**Matrices de proyección por cabeza:**
- $\mathbf{W}_i^Q$: $d_{\text{model}} \times d_k$ parámetros
- $\mathbf{W}_i^K$: $d_{\text{model}} \times d_k$ parámetros
- $\mathbf{W}_i^V$: $d_{\text{model}} \times d_v$ parámetros

**Total por cabeza:** $d_{\text{model}} \times (2d_k + d_v)$

**Total para $h$ cabezas:** $h \times d_{\text{model}} \times (2d_k + d_v)$

Con $d_k = d_v = d_{\text{model}} / h$:

$$h \times d_{\text{model}} \times \frac{3 \, d_{\text{model}}}{h} = 3 \, d_{\text{model}}^2$$

**Matriz de proyección de salida:** $\mathbf{W}^O$: $d_{\text{model}} \times d_{\text{model}} = d_{\text{model}}^2$ parámetros.

**Total de parámetros MHA (sin sesgos):**

$$\text{Params}_{\text{MHA}} = 3\,d_{\text{model}}^2 + d_{\text{model}}^2 = 4\,d_{\text{model}}^2$$

**Ejemplo numérico:** Para el Transformer base de Vaswani et al. (2017), con $d_{\text{model}} = 512$ y $h = 8$:

- $d_k = d_v = 512 / 8 = 64$
- Parámetros por cabeza: $512 \times 64 \times 3 = 98{,}304$
- Parámetros de todas las cabezas: $8 \times 98{,}304 = 786{,}432$
- Parámetros de $\mathbf{W}^O$: $512 \times 512 = 262{,}144$
- **Total:** $786{,}432 + 262{,}144 = 1{,}048{,}576 \approx 1\text{M}$ parámetros

Nótese que este total ($4 \times 512^2 = 1{,}048{,}576$) es **independiente del número de cabezas** $h$: dividir la atención en más cabezas reduce la dimensión de cada cabeza pero no cambia el número total de parámetros. La elección de $h$ es, por lo tanto, una decisión arquitectónica que afecta la **capacidad de especialización** de cada cabeza, no el costo paramétrico total.

### 5.6.6 Complejidad computacional

La complejidad computacional del módulo MHA es:

- **Proyecciones lineales:** $O(T \cdot d_{\text{model}}^2)$ para calcular $\mathbf{Q}_i$, $\mathbf{K}_i$, $\mathbf{V}_i$ de todas las cabezas.
- **Atención por cabeza:** $O(T^2 \cdot d_k)$ para cada cabeza.
- **Total atención:** $h \times O(T^2 \cdot d_k) = O(T^2 \cdot h \cdot d_k) = O(T^2 \cdot d_{\text{model}})$.
- **Proyección de salida:** $O(T \cdot d_{\text{model}}^2)$.

**Complejidad total:** $O(T \cdot d_{\text{model}}^2 + T^2 \cdot d_{\text{model}})$.

Para secuencias cortas ($T \ll d_{\text{model}}$), el costo está dominado por las proyecciones lineales. Para secuencias largas ($T \gg d_{\text{model}}$), el término cuadrático $T^2$ domina, lo que constituye el principal cuello de botella de los modelos basados en atención para secuencias muy largas.

**Figura 5.3:** *Diagrama de la arquitectura de Multi-Head Attention. En la parte superior se muestra la entrada (las matrices $\mathbf{Q}$, $\mathbf{K}$, $\mathbf{V}$) alimentando $h$ bloques de atención en paralelo (dispuestos horizontalmente), etiquetados como "Cabeza 1", "Cabeza 2", ..., "Cabeza $h$". Dentro de cada bloque de cabeza se muestra una versión compacta del diagrama de Scaled Dot-Product Attention de la Figura 5.2, con las matrices de proyección específicas de cada cabeza ($\mathbf{W}_i^Q$, $\mathbf{W}_i^K$, $\mathbf{W}_i^V$) señaladas explícitamente como entradas. Los mapas de calor de atención dentro de cada cabeza muestran patrones diferentes: la Cabeza 1 podría mostrar un patrón diagonal (atención local), la Cabeza 2 un patrón con líneas verticales (atención a tokens globalmente importantes), y la Cabeza 3 un patrón disperso (relaciones semánticas específicas). Las salidas de todas las cabezas ($\text{head}_1, \ldots, \text{head}_h$, cada una de dimensión $T \times d_v$) convergen en un bloque de "Concatenación" (representado como la unión horizontal de los tensores), seguido de un bloque de "Proyección Lineal" ($\mathbf{W}^O$) que produce la salida final de dimensión $T \times d_{\text{model}}$. Las dimensiones se anotan en cada conexión para claridad.*

---

## 5.7 Implementación en PyTorch

### 5.7.1 Implementación de Scaled Dot-Product Attention

A continuación se presenta una implementación completa y comentada del mecanismo de Scaled Dot-Product Attention en PyTorch.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
import math


class ScaledDotProductAttention(nn.Module):
    """
    Implementación del mecanismo Scaled Dot-Product Attention.
    
    Calcula:
        Attention(Q, K, V) = softmax(Q K^T / sqrt(d_k)) V
    
    Args:
        temperature (float): Factor de escalamiento. Normalmente sqrt(d_k).
    """
    
    def __init__(self, temperature: float):
        super().__init__()
        # El factor de escalamiento controla la "suavidad" de la distribución
        # de atención. Valores más altos producen distribuciones más uniformes;
        # valores más bajos producen distribuciones más concentradas.
        self.temperature = temperature
    
    def forward(
        self,
        query: torch.Tensor,   # (batch, T_q, d_k)
        key: torch.Tensor,     # (batch, T_k, d_k)
        value: torch.Tensor,   # (batch, T_k, d_v)
        mask: torch.Tensor = None  # (batch, T_q, T_k) o (batch, 1, T_k)
    ) -> tuple[torch.Tensor, torch.Tensor]:
        """
        Calcula la atención escalada de producto punto.
        
        Args:
            query: Tensor de consultas de forma (batch, T_q, d_k).
            key: Tensor de claves de forma (batch, T_k, d_k).
            value: Tensor de valores de forma (batch, T_k, d_v).
            mask: Máscara opcional para impedir la atención a ciertas posiciones.
                  Las posiciones con valor True (o 1) serán enmascaradas
                  (recibirán -inf antes de la softmax).
        
        Returns:
            output: Resultado de la atención, forma (batch, T_q, d_v).
            attn_weights: Pesos de atención, forma (batch, T_q, T_k).
        """
        # Paso 1: Calcular puntuaciones brutas mediante producto punto
        # Q: (batch, T_q, d_k), K^T: (batch, d_k, T_k)
        # Resultado: (batch, T_q, T_k)
        scores = torch.bmm(query, key.transpose(1, 2))
        
        # Paso 2: Escalar por la temperatura (sqrt(d_k))
        # Esto previene que las puntuaciones tengan magnitudes muy grandes,
        # lo cual causaría que la softmax produzca gradientes cercanos a cero.
        scores = scores / self.temperature
        
        # Paso 3: Aplicar máscara (opcional)
        # Útil para: (a) ignorar tokens de padding,
        #            (b) atención causal (el decodificador no puede ver el futuro).
        if mask is not None:
            scores = scores.masked_fill(mask == 1, float('-inf'))
        
        # Paso 4: Softmax por la última dimensión (sobre las claves)
        # Convierte las puntuaciones en una distribución de probabilidad
        # para cada consulta sobre todas las claves.
        attn_weights = F.softmax(scores, dim=-1)
        
        # Paso 5: Multiplicar por los valores
        # Cada consulta obtiene una suma ponderada de los valores,
        # donde los pesos son las probabilidades de atención.
        output = torch.bmm(attn_weights, value)
        
        return output, attn_weights
```

### 5.7.2 Implementación de Multi-Head Attention

```python
class MultiHeadAttention(nn.Module):
    """
    Implementación del mecanismo Multi-Head Attention.
    
    MultiHead(Q, K, V) = Concat(head_1, ..., head_h) W^O
    donde head_i = Attention(Q W_i^Q, K W_i^K, V W_i^V)
    
    Args:
        d_model (int): Dimensión del modelo (tamaño de los embeddings).
        n_heads (int): Número de cabezas de atención.
        dropout (float): Tasa de dropout aplicada a los pesos de atención.
    """
    
    def __init__(self, d_model: int, n_heads: int, dropout: float = 0.1):
        super().__init__()
        
        # Verificar que d_model sea divisible entre n_heads
        assert d_model % n_heads == 0, \
            f"d_model ({d_model}) debe ser divisible entre n_heads ({n_heads})"
        
        self.d_model = d_model
        self.n_heads = n_heads
        self.d_k = d_model // n_heads  # Dimensión de cada cabeza
        self.d_v = d_model // n_heads
        
        # Proyecciones lineales para Q, K, V.
        # En lugar de tener h matrices separadas de tamaño (d_model, d_k),
        # usamos una sola matriz de tamaño (d_model, d_model) que proyecta
        # todas las cabezas simultáneamente. Esto es más eficiente en GPU.
        self.W_Q = nn.Linear(d_model, d_model, bias=False)
        self.W_K = nn.Linear(d_model, d_model, bias=False)
        self.W_V = nn.Linear(d_model, d_model, bias=False)
        
        # Proyección de salida W^O: combina las salidas de todas las cabezas
        self.W_O = nn.Linear(d_model, d_model, bias=False)
        
        # Módulo de atención escalada
        self.attention = ScaledDotProductAttention(
            temperature=math.sqrt(self.d_k)
        )
        
        # Dropout para regularización de los pesos de atención
        self.dropout = nn.Dropout(dropout)
    
    def forward(
        self,
        query: torch.Tensor,   # (batch, T_q, d_model)
        key: torch.Tensor,     # (batch, T_k, d_model)
        value: torch.Tensor,   # (batch, T_k, d_model)
        mask: torch.Tensor = None
    ) -> tuple[torch.Tensor, torch.Tensor]:
        """
        Calcula la atención multi-cabeza.
        
        En auto-atención: query = key = value = X (la misma entrada).
        En atención cruzada: query proviene del decodificador,
                             key y value del codificador.
        
        Args:
            query: (batch, T_q, d_model)
            key: (batch, T_k, d_model)
            value: (batch, T_k, d_model)
            mask: Máscara opcional (batch, T_q, T_k)
        
        Returns:
            output: (batch, T_q, d_model)
            attn_weights: (batch, n_heads, T_q, T_k)
        """
        batch_size = query.size(0)
        T_q = query.size(1)
        T_k = key.size(1)
        
        # --- Paso 1: Proyecciones lineales ---
        # Cada proyección: (batch, T, d_model) -> (batch, T, d_model)
        Q = self.W_Q(query)
        K = self.W_K(key)
        V = self.W_V(value)
        
        # --- Paso 2: Separar en múltiples cabezas ---
        # Reorganizar de (batch, T, d_model) a (batch, n_heads, T, d_k)
        # Esto se logra con reshape + transpose:
        #   (batch, T, d_model) -> (batch, T, n_heads, d_k) -> (batch, n_heads, T, d_k)
        Q = Q.view(batch_size, T_q, self.n_heads, self.d_k).transpose(1, 2)
        K = K.view(batch_size, T_k, self.n_heads, self.d_k).transpose(1, 2)
        V = V.view(batch_size, T_k, self.n_heads, self.d_v).transpose(1, 2)
        
        # Aplanar batch y heads para usar bmm:
        # (batch, n_heads, T, d_k) -> (batch * n_heads, T, d_k)
        Q = Q.reshape(batch_size * self.n_heads, T_q, self.d_k)
        K = K.reshape(batch_size * self.n_heads, T_k, self.d_k)
        V = V.reshape(batch_size * self.n_heads, T_k, self.d_v)
        
        # Ajustar máscara para las múltiples cabezas
        if mask is not None:
            # (batch, T_q, T_k) -> (batch * n_heads, T_q, T_k)
            mask = mask.unsqueeze(1).repeat(1, self.n_heads, 1, 1)
            mask = mask.reshape(batch_size * self.n_heads, T_q, T_k)
        
        # --- Paso 3: Calcular la atención para todas las cabezas ---
        # Esto es equivalente a calcular h atenciones independientes
        attn_output, attn_weights = self.attention(Q, K, V, mask=mask)
        # attn_output: (batch * n_heads, T_q, d_v)
        # attn_weights: (batch * n_heads, T_q, T_k)
        
        # Aplicar dropout a los pesos de atención
        attn_output = self.dropout(attn_output)
        
        # --- Paso 4: Concatenar las cabezas ---
        # (batch * n_heads, T_q, d_v) -> (batch, n_heads, T_q, d_v)
        attn_output = attn_output.view(
            batch_size, self.n_heads, T_q, self.d_v
        )
        # (batch, n_heads, T_q, d_v) -> (batch, T_q, n_heads, d_v)
        attn_output = attn_output.transpose(1, 2)
        # (batch, T_q, n_heads, d_v) -> (batch, T_q, n_heads * d_v = d_model)
        attn_output = attn_output.contiguous().view(
            batch_size, T_q, self.d_model
        )
        
        # --- Paso 5: Proyección de salida ---
        # (batch, T_q, d_model) -> (batch, T_q, d_model)
        output = self.W_O(attn_output)
        
        # Reorganizar pesos de atención para visualización
        attn_weights = attn_weights.view(
            batch_size, self.n_heads, T_q, T_k
        )
        
        return output, attn_weights
```

### 5.7.3 Ejemplo de uso y verificación

```python
def ejemplo_atencion():
    """
    Ejemplo completo que demuestra el uso de Multi-Head Attention
    con la oración "El gato se sentó".
    """
    # Configuración
    d_model = 16     # Dimensión del modelo (pequeña para demostración)
    n_heads = 4      # Número de cabezas de atención
    seq_len = 4      # 4 tokens: "El", "gato", "se", "sentó"
    batch_size = 1   # Un solo ejemplo
    
    # Fijar semilla para reproducibilidad
    torch.manual_seed(42)
    
    # Simular embeddings de entrada (normalmente provendrían
    # de una capa de embedding + codificación posicional)
    X = torch.randn(batch_size, seq_len, d_model)
    
    # Crear el módulo de atención multi-cabeza
    mha = MultiHeadAttention(d_model=d_model, n_heads=n_heads, dropout=0.0)
    
    # Auto-atención: Q = K = V = X
    output, attn_weights = mha(query=X, key=X, value=X)
    
    print(f"Entrada X:          {X.shape}")        # (1, 4, 16)
    print(f"Salida:             {output.shape}")    # (1, 4, 16)
    print(f"Pesos de atención:  {attn_weights.shape}")  # (1, 4, 4, 4)
    
    # Visualizar los pesos de atención de cada cabeza
    tokens = ["El", "gato", "se", "sentó"]
    for head in range(n_heads):
        print(f"\n--- Cabeza {head + 1} ---")
        weights = attn_weights[0, head].detach()
        for i, token_q in enumerate(tokens):
            pesos_str = ", ".join(
                f"{tokens[j]}: {weights[i, j]:.3f}"
                for j in range(seq_len)
            )
            print(f"  {token_q:>6s} atiende a -> {pesos_str}")
    
    # Verificar que la salida tiene la misma forma que la entrada
    assert output.shape == X.shape, "La forma de salida debe coincidir"
    
    # Verificar que los pesos de atención suman 1 por fila
    row_sums = attn_weights.sum(dim=-1)
    assert torch.allclose(row_sums, torch.ones_like(row_sums), atol=1e-5), \
        "Los pesos de atención deben sumar 1 por fila"
    
    print("\n¡Todas las verificaciones pasaron correctamente!")


# Crear máscara causal para decodificadores autoregresivos
def crear_mascara_causal(seq_len: int) -> torch.Tensor:
    """
    Crea una máscara triangular superior que impide que cada posición
    atienda a posiciones futuras. Esencial para decodificadores.
    
    Para seq_len=4, la máscara es:
        [[0, 1, 1, 1],
         [0, 0, 1, 1],
         [0, 0, 0, 1],
         [0, 0, 0, 0]]
    
    Donde 1 indica posiciones enmascaradas (no atender).
    """
    mask = torch.triu(torch.ones(seq_len, seq_len), diagonal=1)
    return mask.unsqueeze(0)  # (1, seq_len, seq_len) para broadcasting


if __name__ == "__main__":
    ejemplo_atencion()
```

### 5.7.4 Notas de implementación

**Eficiencia de la implementación conjunta de proyecciones:** En la implementación presentada, cada proyección ($\mathbf{W}^Q$, $\mathbf{W}^K$, $\mathbf{W}^V$) se realiza como una transformación lineal de $d_{\text{model}}$ a $d_{\text{model}}$, seguida de una reorganización de dimensiones para separar las cabezas. Esto es matemáticamente equivalente a tener $h$ proyecciones separadas de $d_{\text{model}}$ a $d_k$, pero es significativamente más eficiente porque se aprovecha el paralelismo de las operaciones matriciales grandes en GPU. En algunos frameworks y bibliotecas, las tres proyecciones ($\mathbf{W}^Q$, $\mathbf{W}^K$, $\mathbf{W}^V$) se combinan incluso en una sola capa lineal de $d_{\text{model}}$ a $3 \cdot d_{\text{model}}$, seguida de un corte (*split*) en tres partes, lo que maximiza la eficiencia computacional.

**Máscara causal:** En el decodificador de un Transformer autoregresivo, es fundamental impedir que cada posición atienda a posiciones futuras (ya que durante la inferencia, esos tokens aún no se han generado). Esto se logra mediante una **máscara causal** (triangular superior) que asigna $-\infty$ a las posiciones futuras antes de la softmax, forzando que $\alpha_{ij} = 0$ para $j > i$.

**Máscara de padding:** Cuando se procesan lotes (*batches*) de secuencias de longitud variable, las secuencias más cortas se rellenan con tokens de *padding*. La máscara de padding evita que el modelo preste atención a estas posiciones artificiales, que no contienen información semántica relevante.

---

## Referencias

- Bahdanau, D., Cho, K., & Bengio, Y. (2015). Neural Machine Translation by Jointly Learning to Align and Translate. *Proceedings of the 3rd International Conference on Learning Representations (ICLR 2015)*. arXiv:1409.0473.

- Cho, K., van Merriënboer, B., Gulcehre, C., Bahdanau, D., Bougares, F., Schwenk, H., & Bengio, Y. (2014). Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation. *Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing (EMNLP)*, pp. 1724–1734. DOI: 10.3115/v1/D14-1179.

- Luong, M.-T., Pham, H., & Manning, C. D. (2015). Effective Approaches to Attention-based Neural Machine Translation. *Proceedings of the 2015 Conference on Empirical Methods in Natural Language Processing (EMNLP)*, pp. 1412–1421. DOI: 10.18653/v1/D15-1166.

- Sutskever, I., Vinyals, O., & Le, Q. V. (2014). Sequence to Sequence Learning with Neural Networks. *Advances in Neural Information Processing Systems 27 (NeurIPS 2014)*, pp. 3104–3112. arXiv:1409.3215.

- Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). Attention Is All You Need. *Advances in Neural Information Processing Systems 30 (NeurIPS 2017)*, pp. 5998–6008. arXiv:1706.03762.
