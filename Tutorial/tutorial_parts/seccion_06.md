# 6. La Arquitectura Transformer

La arquitectura Transformer representa, sin lugar a dudas, uno de los avances más trascendentales en la historia del aprendizaje profundo y del procesamiento de lenguaje natural. Publicada en 2017 por Vaswani y colaboradores, esta arquitectura rompió con el paradigma dominante de las redes neuronales recurrentes al demostrar que el mecanismo de atención, por sí solo, era suficiente para modelar dependencias secuenciales de manera más eficiente y efectiva. En esta sección, estudiaremos en profundidad cada componente de la arquitectura Transformer, desde la codificación posicional hasta la estructura completa encoder-decoder, proporcionando las bases matemáticas, la intuición geométrica y los detalles de implementación necesarios para comprender su funcionamiento y su papel fundamental en las comunicaciones semánticas modernas.

---

## 6.1 Contexto histórico y motivación

### 6.1.1 Limitaciones de las arquitecturas recurrentes

Antes de la aparición del Transformer, las redes neuronales recurrentes (RNN), las redes LSTM (*Long Short-Term Memory*) y las redes GRU (*Gated Recurrent Unit*) constituían el estado del arte para el procesamiento de secuencias. Estas arquitecturas procesan los elementos de una secuencia de manera estrictamente secuencial: para computar la representación oculta $\mathbf{h}_t$ en la posición $t$, es necesario haber calculado previamente $\mathbf{h}_{t-1}$. Esta dependencia secuencial se expresa formalmente como:

$$\mathbf{h}_t = f(\mathbf{h}_{t-1}, \mathbf{x}_t)$$

donde $f$ es la función de transición de estado (que en el caso de LSTM incluye las compuertas de olvido, entrada y salida), $\mathbf{x}_t$ es la entrada en la posición $t$ y $\mathbf{h}_{t-1}$ es el estado oculto anterior.

Esta naturaleza secuencial impone varias limitaciones fundamentales:

1. **Paralelismo limitado durante el entrenamiento.** Dado que cada paso temporal depende del anterior, no es posible calcular los estados ocultos de diferentes posiciones de manera simultánea. En una secuencia de longitud $T$, el cálculo requiere $T$ pasos secuenciales, lo que impide aprovechar eficientemente las capacidades de cómputo paralelo de las GPU modernas. Mientras que las operaciones sobre lotes (*batches*) de secuencias pueden paralelizarse, las operaciones *dentro* de cada secuencia individual permanecen inherentemente secuenciales.

2. **Degradación en dependencias de largo alcance.** A pesar de que las LSTM fueron diseñadas específicamente para mitigar el problema del desvanecimiento del gradiente (*vanishing gradient*), en la práctica su capacidad para capturar dependencias a muy largo alcance sigue siendo limitada. La información debe fluir a través de múltiples pasos de la cadena recurrente, y con cada paso existe la posibilidad de que se diluya o se pierda. En una secuencia de longitud $T$, la señal entre la posición $1$ y la posición $T$ debe recorrer $O(T)$ pasos, lo que dificulta el aprendizaje de relaciones distantes.

3. **Cuello de botella de información.** En las arquitecturas encoder-decoder basadas en RNN, toda la información de la secuencia de entrada se comprime en un único vector de contexto $\mathbf{c}$ (el último estado oculto del encoder). Para secuencias largas, este vector fijo se convierte en un cuello de botella que limita la cantidad de información que puede transmitirse al decoder. Aunque el mecanismo de atención de Bahdanau (2014) alivió parcialmente este problema al permitir que el decoder accediera a todos los estados ocultos del encoder, la arquitectura subyacente seguía siendo recurrente.

4. **Velocidad de entrenamiento.** La imposibilidad de paralelizar el procesamiento dentro de cada secuencia se traduce en tiempos de entrenamiento significativamente más largos, especialmente para conjuntos de datos masivos y secuencias extensas. Esta limitación práctica restringía la escala de los modelos y los datos que podían utilizarse.

### 6.1.2 El artículo "Attention Is All You Need"

En junio de 2017, Vaswani, Shazeer, Parmar, Uszkoreit, Jones, Gomez, Kaiser y Polosukhin publicaron el artículo seminal *"Attention Is All You Need"*, presentado en la conferencia NeurIPS (Vaswani et al., 2017). La idea central del artículo era revolucionariamente simple: **eliminar por completo la recurrencia** y basar la arquitectura exclusivamente en mecanismos de atención.

Los autores propusieron el *Transformer*, una arquitectura que reemplaza las capas recurrentes por capas de *self-attention* (auto-atención) y redes *feed-forward* posición por posición. Las contribuciones clave del artículo incluyen:

- **Self-Attention Multi-Cabezal (*Multi-Head Attention*)**: permite que cada posición de la secuencia atienda simultáneamente a todas las demás posiciones, capturando dependencias sin importar la distancia.
- **Codificación posicional**: dado que la arquitectura no tiene noción inherente de orden secuencial (a diferencia de las RNN), se introduce información posicional mediante funciones sinusoidales.
- **Paralelismo completo**: todas las posiciones de la secuencia pueden procesarse simultáneamente durante el entrenamiento, aprovechando al máximo la arquitectura de las GPU.
- **Rendimiento superior**: el Transformer estableció nuevos récords en tareas de traducción automática, alcanzando un BLEU de 28.4 en la tarea inglés-alemán del WMT 2014, superando a todos los modelos previos incluyendo ensambles (*ensembles*).

La intuición fundamental detrás del Transformer puede resumirse así: en lugar de procesar una secuencia elemento por elemento y acumular información en un estado oculto, se permite que todos los elementos de la secuencia "se comuniquen" directamente entre sí a través del mecanismo de atención. La longitud del camino entre cualquier par de posiciones se reduce de $O(T)$ en las RNN a $O(1)$ en el Transformer, lo que facilita enormemente el aprendizaje de dependencias a largo alcance.

Esta idea, que en retrospectiva parece natural, representó un cambio de paradigma que transformó no solo el procesamiento de lenguaje natural, sino también la visión por computadora, el procesamiento de audio, la bioinformática y, como veremos en secciones posteriores, las comunicaciones semánticas.

> **Referencia:** Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). Attention is all you need. *Advances in Neural Information Processing Systems*, 30. (DOI: 10.48550/arXiv.1706.03762)

---

## 6.2 Codificación posicional (*Positional Encoding*)

### 6.2.1 La necesidad de codificar posiciones

Las redes recurrentes tienen una ventaja inherente sobre las arquitecturas basadas puramente en atención: procesan la secuencia de manera ordenada, de modo que la posición de cada elemento está implícitamente codificada en el orden de procesamiento. El estado oculto $\mathbf{h}_t$ "sabe" que corresponde a la posición $t$ porque fue calculado después de $\mathbf{h}_{t-1}$.

El Transformer, en cambio, procesa todas las posiciones de la secuencia de manera simultánea. La operación de self-attention es, en esencia, una operación sobre *conjuntos* (*sets*): si permutamos las posiciones de entrada, las salidas se permutan de la misma manera, pero las relaciones de atención entre tokens no cambian. Formalmente, si $\pi$ es una permutación y $\mathbf{X} = [\mathbf{x}_1, \ldots, \mathbf{x}_T]$ es la matriz de entrada, entonces:

$$\text{Attention}(\pi(\mathbf{X})) = \pi(\text{Attention}(\mathbf{X}))$$

Esto significa que, sin información posicional adicional, el modelo trataría las oraciones "El gato persigue al ratón" y "El ratón persigue al gato" de manera idéntica (asumiendo que los embeddings de las palabras son los mismos), ya que los mismos tokens están presentes en ambas oraciones, solo cambia su orden.

Para resolver este problema, Vaswani et al. propusieron sumar una *codificación posicional* (*positional encoding*) a los embeddings de entrada. Formalmente, si $\mathbf{e}_i$ es el embedding del token en la posición $i$, la entrada al primer bloque del Transformer es:

$$\mathbf{z}_i = \mathbf{e}_i + \mathbf{PE}_i$$

donde $\mathbf{PE}_i \in \mathbb{R}^{d_{model}}$ es el vector de codificación posicional para la posición $i$. La suma (en lugar de concatenación) se elige para mantener la dimensionalidad del modelo y porque empíricamente funciona bien.

### 6.2.2 Codificación sinusoidal

Vaswani et al. propusieron una codificación posicional basada en funciones sinusoidales de diferentes frecuencias. Para cada posición $pos$ en la secuencia y cada dimensión $i$ del vector de embedding, la codificación posicional se define como:

$$PE_{(pos, 2i)} = \sin\left(\frac{pos}{10000^{2i/d_{model}}}\right)$$

$$PE_{(pos, 2i+1)} = \cos\left(\frac{pos}{10000^{2i/d_{model}}}\right)$$

donde $pos \in \{0, 1, 2, \ldots, T-1\}$ es la posición en la secuencia, $i \in \{0, 1, 2, \ldots, d_{model}/2 - 1\}$ es el índice de la dimensión del par seno-coseno, y $d_{model}$ es la dimensión del modelo (es decir, la dimensión de los embeddings y de todas las representaciones internas).

Analicemos esta fórmula con cuidado. Para cada par de dimensiones $(2i, 2i+1)$, se utiliza una función sinusoidal con una frecuencia angular específica:

$$\omega_i = \frac{1}{10000^{2i/d_{model}}}$$

La frecuencia $\omega_i$ varía geométricamente a lo largo de las dimensiones: para $i = 0$, tenemos $\omega_0 = 1$ (frecuencia más alta, período $2\pi \approx 6.28$ posiciones), y para $i = d_{model}/2 - 1$, tenemos $\omega_{d_{model}/2 - 1} \approx 1/10000$ (frecuencia más baja, período $2\pi \cdot 10000 \approx 62832$ posiciones). Esta progresión geométrica de frecuencias es análoga a la representación de un número en diferentes bases: las dimensiones de alta frecuencia cambian rápidamente con la posición (como los dígitos menos significativos), mientras que las dimensiones de baja frecuencia cambian lentamente (como los dígitos más significativos).

### 6.2.3 Propiedad de posiciones relativas

Una propiedad crucial de la codificación sinusoidal es que permite al modelo aprender a atender a posiciones relativas. Esto se debe a que, para cualquier desplazamiento fijo $k$, la codificación posicional $\mathbf{PE}_{pos+k}$ puede expresarse como una transformación lineal de $\mathbf{PE}_{pos}$.

Para demostrar esto, consideremos un par de dimensiones $(2i, 2i+1)$. Usando las identidades trigonométricas de suma de ángulos:

$$\sin(\alpha + \beta) = \sin \alpha \cos \beta + \cos \alpha \sin \beta$$
$$\cos(\alpha + \beta) = \cos \alpha \cos \beta - \sin \alpha \sin \beta$$

Con $\alpha = pos \cdot \omega_i$ y $\beta = k \cdot \omega_i$, obtenemos:

$$PE_{(pos+k, 2i)} = \sin((pos+k) \cdot \omega_i) = \sin(pos \cdot \omega_i) \cos(k \cdot \omega_i) + \cos(pos \cdot \omega_i) \sin(k \cdot \omega_i)$$

$$PE_{(pos+k, 2i+1)} = \cos((pos+k) \cdot \omega_i) = \cos(pos \cdot \omega_i) \cos(k \cdot \omega_i) - \sin(pos \cdot \omega_i) \sin(k \cdot \omega_i)$$

Esto puede escribirse en forma matricial como:

$$\begin{bmatrix} PE_{(pos+k, 2i)} \\ PE_{(pos+k, 2i+1)} \end{bmatrix} = \begin{bmatrix} \cos(k \cdot \omega_i) & \sin(k \cdot \omega_i) \\ -\sin(k \cdot \omega_i) & \cos(k \cdot \omega_i) \end{bmatrix} \begin{bmatrix} PE_{(pos, 2i)} \\ PE_{(pos, 2i+1)} \end{bmatrix}$$

La matriz de transformación es una *matriz de rotación* que depende únicamente del desplazamiento $k$ y de la frecuencia $\omega_i$, pero **no** de la posición absoluta $pos$. Esto significa que la relación entre las codificaciones posicionales de dos posiciones separadas por una distancia $k$ es siempre la misma, independientemente de dónde se encuentren en la secuencia. Esta propiedad permite que las capas de atención aprendan patrones basados en posiciones relativas, lo cual es fundamental para la generalización a secuencias de longitudes no vistas durante el entrenamiento.

### 6.2.4 Ejemplo numérico

Para solidificar la comprensión, calculemos la codificación posicional para las posiciones $pos = 0, 1, 2, 3, 4$ con un modelo pequeño de dimensión $d_{model} = 4$. Tenemos dos pares de dimensiones: $(2i=0, 2i+1=1)$ con $i=0$ y $(2i=2, 2i+1=3)$ con $i=1$.

Primero, calculamos las frecuencias angulares:

- Para $i = 0$: $\omega_0 = \frac{1}{10000^{0/4}} = \frac{1}{10000^0} = 1$
- Para $i = 1$: $\omega_1 = \frac{1}{10000^{2/4}} = \frac{1}{10000^{0.5}} = \frac{1}{100} = 0.01$

Ahora calculamos los valores para cada posición:

**Posición $pos = 0$:**

$$PE_{(0,0)} = \sin(0 \cdot 1) = \sin(0) = 0$$
$$PE_{(0,1)} = \cos(0 \cdot 1) = \cos(0) = 1$$
$$PE_{(0,2)} = \sin(0 \cdot 0.01) = \sin(0) = 0$$
$$PE_{(0,3)} = \cos(0 \cdot 0.01) = \cos(0) = 1$$

$$\mathbf{PE}_0 = [0, \ 1, \ 0, \ 1]$$

**Posición $pos = 1$:**

$$PE_{(1,0)} = \sin(1 \cdot 1) = \sin(1) \approx 0.8415$$
$$PE_{(1,1)} = \cos(1 \cdot 1) = \cos(1) \approx 0.5403$$
$$PE_{(1,2)} = \sin(1 \cdot 0.01) = \sin(0.01) \approx 0.0100$$
$$PE_{(1,3)} = \cos(1 \cdot 0.01) = \cos(0.01) \approx 0.9999$$

$$\mathbf{PE}_1 \approx [0.8415, \ 0.5403, \ 0.0100, \ 0.9999]$$

**Posición $pos = 2$:**

$$PE_{(2,0)} = \sin(2) \approx 0.9093$$
$$PE_{(2,1)} = \cos(2) \approx -0.4161$$
$$PE_{(2,2)} = \sin(0.02) \approx 0.0200$$
$$PE_{(2,3)} = \cos(0.02) \approx 0.9998$$

$$\mathbf{PE}_2 \approx [0.9093, \ {-0.4161}, \ 0.0200, \ 0.9998]$$

**Posición $pos = 3$:**

$$PE_{(3,0)} = \sin(3) \approx 0.1411$$
$$PE_{(3,1)} = \cos(3) \approx -0.9900$$
$$PE_{(3,2)} = \sin(0.03) \approx 0.0300$$
$$PE_{(3,3)} = \cos(0.03) \approx 0.9996$$

$$\mathbf{PE}_3 \approx [0.1411, \ {-0.9900}, \ 0.0300, \ 0.9996]$$

**Posición $pos = 4$:**

$$PE_{(4,0)} = \sin(4) \approx -0.7568$$
$$PE_{(4,1)} = \cos(4) \approx -0.6536$$
$$PE_{(4,2)} = \sin(0.04) \approx 0.0400$$
$$PE_{(4,3)} = \cos(0.04) \approx 0.9992$$

$$\mathbf{PE}_4 \approx [-0.7568, \ {-0.6536}, \ 0.0400, \ 0.9992]$$

Observemos varios patrones importantes en estos resultados:

- Las dimensiones 0 y 1 (alta frecuencia, $\omega_0 = 1$) oscilan rápidamente: los valores cambian significativamente de una posición a la siguiente.
- Las dimensiones 2 y 3 (baja frecuencia, $\omega_1 = 0.01$) cambian muy lentamente: los valores apenas se modifican entre posiciones consecutivas.
- Cada posición tiene un vector de codificación único, lo que permite distinguirla de las demás.
- Los vectores de posiciones cercanas son más similares entre sí que los de posiciones lejanas, lo cual es una propiedad deseable.

En un modelo real con $d_{model} = 512$, habría 256 pares de frecuencias cubriendo un espectro continuo desde oscilaciones rápidas hasta oscilaciones extremadamente lentas, proporcionando una representación rica y expresiva de la posición.

**Figura 6.1:** *Mapa de calor de la codificación posicional sinusoidal para posiciones $0$ a $49$ (eje vertical) y dimensiones $0$ a $127$ (eje horizontal), con $d_{model} = 128$. Cada fila corresponde al vector de codificación posicional de una posición específica. Las dimensiones bajas (izquierda) presentan patrones de alta frecuencia que oscilan rápidamente entre valores positivos (colores cálidos) y negativos (colores fríos), mientras que las dimensiones altas (derecha) muestran patrones de frecuencia progresivamente menor, con ondas cada vez más amplias. Se observa que cada posición genera un patrón sinusoidal único, creando una "huella digital" posicional. Las franjas verticales de la izquierda, que alternan rápidamente, corresponden a $\omega_i$ grandes, y las bandas anchas de la derecha corresponden a $\omega_i$ pequeños. Esta variación multiescala permite que el Transformer capture tanto relaciones posicionales locales como globales.*

### 6.2.5 Codificaciones posicionales aprendidas

Además de la codificación sinusoidal fija, los autores del Transformer original también experimentaron con codificaciones posicionales aprendidas, donde cada posición tiene un vector de embedding que se optimiza durante el entrenamiento, de manera similar a los embeddings de palabras. Los resultados mostraron que ambos enfoques producían un rendimiento prácticamente idéntico. Sin embargo, la codificación sinusoidal tiene la ventaja teórica de poder generalizar a secuencias más largas que las vistas durante el entrenamiento, ya que las funciones sinusoidales están definidas para cualquier valor de $pos$, mientras que las codificaciones aprendidas están limitadas a las posiciones vistas durante el entrenamiento.

En la práctica, muchas implementaciones modernas de Transformers utilizan codificaciones posicionales aprendidas (como en BERT y GPT) o variantes más sofisticadas como las codificaciones posicionales rotatorias (*Rotary Position Embeddings*, RoPE), que incorporan la información posicional directamente en el mecanismo de atención mediante rotaciones en el espacio de embeddings.

---

## 6.3 El bloque Encoder del Transformer

### 6.3.1 Visión general de la arquitectura del encoder

El encoder del Transformer tiene como objetivo transformar una secuencia de entrada $\mathbf{X} = (\mathbf{x}_1, \mathbf{x}_2, \ldots, \mathbf{x}_T)$ en una secuencia de representaciones contextualizadas $\mathbf{Z} = (\mathbf{z}_1, \mathbf{z}_2, \ldots, \mathbf{z}_T)$, donde cada vector $\mathbf{z}_t$ captura no solo la información del token $t$, sino también su relación con todos los demás tokens de la secuencia.

El encoder está compuesto por una pila de $N$ bloques (*layers*) idénticos. En el modelo base del Transformer original, $N = 6$. Cada bloque consta de dos sub-capas principales, cada una envuelta en una conexión residual y seguida de una normalización de capa. El flujo de datos a través de un bloque encoder es el siguiente:

1. **Embedding de entrada + Codificación posicional**
2. **Multi-Head Self-Attention**
3. **Add & Norm** (conexión residual + normalización de capa)
4. **Red Feed-Forward** posición por posición
5. **Add & Norm** (conexión residual + normalización de capa)

Describamos cada componente en detalle.

### 6.3.2 Embedding de entrada y codificación posicional

El primer paso consiste en convertir los tokens de entrada (típicamente representados como índices enteros en un vocabulario) en vectores densos de dimensión $d_{model}$. Esto se logra mediante una capa de embedding:

$$\mathbf{e}_t = \text{Embedding}(x_t) \in \mathbb{R}^{d_{model}}$$

A estos vectores de embedding se les suma la codificación posicional:

$$\mathbf{z}_t^{(0)} = \mathbf{e}_t + \mathbf{PE}_t$$

donde $\mathbf{z}_t^{(0)}$ denota la representación de entrada antes de pasar por los bloques del encoder. Es importante notar que los embeddings se escalan típicamente por un factor de $\sqrt{d_{model}}$ antes de sumar la codificación posicional:

$$\mathbf{z}_t^{(0)} = \sqrt{d_{model}} \cdot \mathbf{e}_t + \mathbf{PE}_t$$

Este escalado se realiza porque los valores de los embeddings aprendidos tienden a tener magnitudes pequeñas (especialmente al inicio del entrenamiento, cuando se inicializan aleatoriamente), mientras que las codificaciones posicionales sinusoidales tienen valores en el rango $[-1, 1]$. El factor $\sqrt{d_{model}}$ asegura que la magnitud de los embeddings sea comparable a la de las codificaciones posicionales, evitando que la información posicional domine sobre la información semántica.

### 6.3.3 Multi-Head Self-Attention

La primera sub-capa de cada bloque encoder es una capa de *Multi-Head Self-Attention* (MHSA), que fue descrita en detalle en la Sección 5. En la self-attention del encoder, las matrices de consulta ($\mathbf{Q}$), clave ($\mathbf{K}$) y valor ($\mathbf{V}$) se derivan todas de la misma entrada:

$$\mathbf{Q} = \mathbf{Z}^{(\ell-1)} \mathbf{W}^Q, \quad \mathbf{K} = \mathbf{Z}^{(\ell-1)} \mathbf{W}^K, \quad \mathbf{V} = \mathbf{Z}^{(\ell-1)} \mathbf{W}^V$$

donde $\mathbf{Z}^{(\ell-1)} \in \mathbb{R}^{T \times d_{model}}$ es la salida de la capa anterior (o la entrada con codificación posicional para la primera capa), y $\mathbf{W}^Q, \mathbf{W}^K \in \mathbb{R}^{d_{model} \times d_k}$, $\mathbf{W}^V \in \mathbb{R}^{d_{model} \times d_v}$ son matrices de proyección aprendibles.

La atención escalada por producto punto se calcula como:

$$\text{Attention}(\mathbf{Q}, \mathbf{K}, \mathbf{V}) = \text{softmax}\left(\frac{\mathbf{Q}\mathbf{K}^\top}{\sqrt{d_k}}\right)\mathbf{V}$$

En la versión multi-cabezal con $h$ cabezas, cada cabeza $j$ tiene sus propias proyecciones $\mathbf{W}_j^Q, \mathbf{W}_j^K, \mathbf{W}_j^V$, y las salidas de todas las cabezas se concatenan y se proyectan:

$$\text{MultiHead}(\mathbf{Q}, \mathbf{K}, \mathbf{V}) = \text{Concat}(\text{head}_1, \ldots, \text{head}_h)\mathbf{W}^O$$

donde $\text{head}_j = \text{Attention}(\mathbf{Q}\mathbf{W}_j^Q, \mathbf{K}\mathbf{W}_j^K, \mathbf{V}\mathbf{W}_j^V)$ y $\mathbf{W}^O \in \mathbb{R}^{hd_v \times d_{model}}$.

En el encoder, la self-attention es *bidireccional*: cada token puede atender a todos los demás tokens de la secuencia, incluyendo los que están antes y después de él. No se aplica ninguna máscara causal, lo que permite al encoder construir representaciones que incorporan contexto de toda la secuencia.

### 6.3.4 Conexiones residuales

Las conexiones residuales (*residual connections* o *skip connections*), introducidas por He et al. (2016) en el contexto de redes convolucionales profundas (ResNet), son un componente esencial del Transformer. La idea es simple pero poderosa: en lugar de que cada sub-capa aprenda la transformación deseada $F(\mathbf{x})$, se le pide que aprenda la *función residual* $F(\mathbf{x}) - \mathbf{x}$, y la salida se obtiene sumando la entrada original:

$$\text{Output} = \mathbf{x} + \text{Sublayer}(\mathbf{x})$$

Las conexiones residuales ofrecen varias ventajas críticas:

1. **Facilitan el flujo del gradiente.** Durante la retropropagación, el gradiente de la pérdida con respecto a $\mathbf{x}$ es:

$$\frac{\partial \mathcal{L}}{\partial \mathbf{x}} = \frac{\partial \mathcal{L}}{\partial \text{Output}} \cdot \left(\mathbf{I} + \frac{\partial \text{Sublayer}(\mathbf{x})}{\partial \mathbf{x}}\right)$$

El término $\mathbf{I}$ (la matriz identidad) asegura que siempre existe un camino directo para el gradiente, incluso si $\frac{\partial \text{Sublayer}(\mathbf{x})}{\partial \mathbf{x}}$ es pequeño. Esto mitiga el problema del desvanecimiento del gradiente en redes profundas.

2. **Preservan la información.** La conexión residual garantiza que la información de la entrada original siempre está disponible en la salida. La sub-capa solo necesita aprender las *modificaciones* que deben hacerse a la representación, no reconstruirla desde cero.

3. **Facilitan el aprendizaje de funciones identidad.** Si la transformación óptima en una capa determinada es la identidad (es decir, no hacer nada), la red simplemente necesita que $\text{Sublayer}(\mathbf{x}) \approx 0$, lo cual es mucho más fácil de aprender que hacer que $F(\mathbf{x}) \approx \mathbf{x}$ directamente.

4. **Permiten la construcción de redes más profundas.** Sin conexiones residuales, entrenar redes con muchas capas se vuelve extremadamente difícil. Los Transformers grandes pueden tener docenas o incluso cientos de capas, lo cual sería imposible sin conexiones residuales.

> **Referencia:** He, K., Zhang, X., Ren, S., & Sun, J. (2016). Deep residual learning for image recognition. *Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition*, 770-778. (DOI: 10.1109/CVPR.2016.90)

### 6.3.5 Normalización de capa (*Layer Normalization*)

Después de la conexión residual, se aplica *Layer Normalization* (LN), propuesta por Ba, Kiros y Hinton (2016). A diferencia de la *Batch Normalization*, que normaliza a lo largo de la dimensión del lote (y por tanto depende del tamaño del lote y no es adecuada para secuencias de longitud variable), la Layer Normalization normaliza a lo largo de la dimensión de las características para cada ejemplo individual.

Dado un vector $\mathbf{x} \in \mathbb{R}^{d_{model}}$, la Layer Normalization se define como:

$$\text{LN}(\mathbf{x}) = \gamma \odot \frac{\mathbf{x} - \mu}{\sigma + \epsilon} + \beta$$

donde:

- $\mu = \frac{1}{d_{model}} \sum_{j=1}^{d_{model}} x_j$ es la media de los elementos del vector.
- $\sigma = \sqrt{\frac{1}{d_{model}} \sum_{j=1}^{d_{model}} (x_j - \mu)^2}$ es la desviación estándar de los elementos del vector.
- $\gamma \in \mathbb{R}^{d_{model}}$ y $\beta \in \mathbb{R}^{d_{model}}$ son parámetros aprendibles de escala y desplazamiento, respectivamente.
- $\epsilon$ es una constante pequeña (típicamente $10^{-5}$ o $10^{-6}$) para estabilidad numérica, evitando la división por cero.
- $\odot$ denota el producto elemento a elemento (producto de Hadamard).

La normalización tiene varios efectos beneficiosos:

1. **Estabiliza el entrenamiento.** Al normalizar las activaciones, se evitan problemas de escalas muy diferentes entre las representaciones de distintas capas, lo que permite utilizar tasas de aprendizaje más altas.
2. **Reduce la dependencia de la inicialización.** La normalización hace que la red sea menos sensible a la elección de los valores iniciales de los pesos.
3. **Actúa como regularizador.** La normalización introduce una forma sutil de regularización que puede mejorar la generalización.

Los parámetros $\gamma$ y $\beta$ son necesarios porque, sin ellos, la normalización restringiría las activaciones a tener media cero y varianza unitaria, lo cual podría ser una restricción demasiado fuerte. Estos parámetros permiten que la red aprenda a "des-normalizar" si es necesario, recuperando la capacidad representativa completa.

En el Transformer original, la normalización se aplica *después* de la conexión residual (*Post-LN*):

$$\mathbf{z}' = \text{LN}(\mathbf{x} + \text{Sublayer}(\mathbf{x}))$$

Sin embargo, trabajos posteriores han mostrado que aplicar la normalización *antes* de la sub-capa (*Pre-LN*) puede mejorar la estabilidad del entrenamiento, especialmente para modelos muy profundos:

$$\mathbf{z}' = \mathbf{x} + \text{Sublayer}(\text{LN}(\mathbf{x}))$$

> **Referencia:** Ba, J. L., Kiros, J. R., & Hinton, G. E. (2016). Layer normalization. *arXiv preprint arXiv:1607.06450*. (DOI: 10.48550/arXiv.1607.06450)

### 6.3.6 Red Feed-Forward posición por posición

La segunda sub-capa de cada bloque encoder es una red *feed-forward* (FFN) que se aplica de manera independiente y posición por posición. Es decir, la misma red se aplica a cada posición de la secuencia de manera idéntica, sin interacción entre posiciones (la interacción entre posiciones ya fue capturada por la capa de atención).

La FFN consiste en dos transformaciones lineales con una activación ReLU (o variantes como GELU) entre ellas:

$$\text{FFN}(\mathbf{x}) = \max(0, \mathbf{x}\mathbf{W}_1 + \mathbf{b}_1)\mathbf{W}_2 + \mathbf{b}_2$$

donde:

- $\mathbf{W}_1 \in \mathbb{R}^{d_{model} \times d_{ff}}$ y $\mathbf{b}_1 \in \mathbb{R}^{d_{ff}}$ son los pesos y bias de la primera capa lineal.
- $\mathbf{W}_2 \in \mathbb{R}^{d_{ff} \times d_{model}}$ y $\mathbf{b}_2 \in \mathbb{R}^{d_{model}}$ son los pesos y bias de la segunda capa lineal.
- $\max(0, \cdot)$ es la función de activación ReLU.
- $d_{ff}$ es la dimensión de la capa oculta interna de la FFN.

En el modelo base del Transformer, $d_{model} = 512$ y $d_{ff} = 2048$, es decir, la capa oculta tiene una dimensionalidad cuatro veces mayor que la dimensión del modelo. Esta expansión y posterior compresión permite a la red aprender transformaciones no lineales complejas en un espacio de mayor dimensionalidad.

La FFN puede interpretarse como una red de dos capas que actúa como un "procesador" local: mientras que la capa de atención mezcla información entre posiciones, la FFN procesa la información de cada posición de manera independiente, refinando las representaciones contextualizadas.

Investigaciones recientes han sugerido que la FFN actúa como una especie de *memoria clave-valor*, donde la primera capa lineal ($\mathbf{W}_1$) actúa como la clave que detecta ciertos patrones en la entrada, y la segunda capa lineal ($\mathbf{W}_2$) produce los valores asociados. Bajo esta interpretación, las neuronas de la capa oculta se especializan en detectar patrones específicos (como n-gramas, categorías semánticas o relaciones sintácticas), y sus activaciones determinan qué información se añade a la representación.

### 6.3.7 Estructura completa de un bloque encoder

Combinando todos los componentes, el procesamiento de un bloque encoder completo puede describirse formalmente como:

$$\mathbf{a}^{(\ell)} = \text{LN}\left(\mathbf{Z}^{(\ell-1)} + \text{MHSA}\left(\mathbf{Z}^{(\ell-1)}\right)\right)$$

$$\mathbf{Z}^{(\ell)} = \text{LN}\left(\mathbf{a}^{(\ell)} + \text{FFN}\left(\mathbf{a}^{(\ell)}\right)\right)$$

donde $\mathbf{Z}^{(\ell-1)} \in \mathbb{R}^{T \times d_{model}}$ es la entrada al bloque $\ell$ (con $\ell = 1, 2, \ldots, N$), $\mathbf{a}^{(\ell)}$ es la salida intermedia después de la self-attention con su Add & Norm, y $\mathbf{Z}^{(\ell)} \in \mathbb{R}^{T \times d_{model}}$ es la salida del bloque.

Los $N$ bloques se apilan secuencialmente, de modo que la salida del bloque $\ell$ se convierte en la entrada del bloque $\ell + 1$. Es importante enfatizar que, aunque todos los bloques tienen la misma estructura, **no comparten parámetros**: cada bloque tiene sus propias matrices de proyección para la atención ($\mathbf{W}_j^Q, \mathbf{W}_j^K, \mathbf{W}_j^V, \mathbf{W}^O$), sus propios pesos de la FFN ($\mathbf{W}_1, \mathbf{b}_1, \mathbf{W}_2, \mathbf{b}_2$), y sus propios parámetros de normalización ($\gamma, \beta$) para cada sub-capa.

La salida del último bloque encoder, $\mathbf{Z}^{(N)} \in \mathbb{R}^{T \times d_{model}}$, constituye la representación final de la secuencia de entrada y será utilizada por el decoder (en arquitecturas encoder-decoder) o directamente para tareas de clasificación u otras tareas de comprensión (en arquitecturas solo-encoder como BERT).

**Figura 6.2:** *Diagrama detallado de un bloque encoder del Transformer. La entrada $\mathbf{Z}^{(\ell-1)}$ (representada como una matriz de $T$ vectores de dimensión $d_{model}$) ingresa simultáneamente a la sub-capa de Multi-Head Self-Attention y a una conexión residual (representada como una flecha que rodea la sub-capa). La salida de la self-attention se suma con la entrada original (Add) y se normaliza (Norm), produciendo una representación intermedia. Esta representación alimenta a la sub-capa Feed-Forward Network, que también tiene su propia conexión residual. La salida de la FFN se suma con su entrada (Add) y se normaliza (Norm), produciendo la salida del bloque $\mathbf{Z}^{(\ell)}$. Las conexiones residuales se muestran como flechas curvas que conectan directamente la entrada de cada sub-capa con la operación de suma posterior. Los bloques de normalización de capa se representan como barras horizontales etiquetadas "Layer Norm". Todo el bloque está encerrado en un rectángulo con la etiqueta "$\times N$" indicando que se repite $N$ veces.*

---

## 6.4 El bloque Decoder del Transformer

### 6.4.1 Estructura del decoder

El decoder del Transformer es más complejo que el encoder, ya que incorpora una sub-capa adicional para atender a la salida del encoder. Cada bloque decoder consta de tres sub-capas, cada una con su propia conexión residual y normalización:

1. **Masked Multi-Head Self-Attention** (self-attention enmascarada)
2. **Multi-Head Encoder-Decoder Attention** (atención cruzada)
3. **Feed-Forward Network** (red feed-forward, idéntica en estructura a la del encoder)

El flujo de datos a través de un bloque decoder es:

$$\mathbf{m}^{(\ell)} = \text{LN}\left(\mathbf{Y}^{(\ell-1)} + \text{MaskedMHSA}\left(\mathbf{Y}^{(\ell-1)}\right)\right)$$

$$\mathbf{c}^{(\ell)} = \text{LN}\left(\mathbf{m}^{(\ell)} + \text{MHCA}\left(\mathbf{m}^{(\ell)}, \mathbf{Z}^{(N)}\right)\right)$$

$$\mathbf{Y}^{(\ell)} = \text{LN}\left(\mathbf{c}^{(\ell)} + \text{FFN}\left(\mathbf{c}^{(\ell)}\right)\right)$$

donde $\mathbf{Y}^{(\ell-1)}$ es la entrada al bloque decoder $\ell$, $\mathbf{Z}^{(N)}$ es la salida del último bloque encoder, $\text{MHCA}$ denota la atención cruzada multi-cabezal (*Multi-Head Cross-Attention*), $\mathbf{m}^{(\ell)}$ es la representación intermedia después de la self-attention enmascarada, y $\mathbf{c}^{(\ell)}$ es la representación después de la atención cruzada.

### 6.4.2 Máscara causal (*Causal Mask*)

La diferencia fundamental entre la self-attention del encoder y la del decoder es la *máscara causal*. Durante la generación de secuencias, el decoder produce un token a la vez, de izquierda a derecha. Al generar el token en la posición $t$, el modelo solo debería tener acceso a los tokens que ya se han generado (posiciones $1, 2, \ldots, t-1$), pero no a los tokens futuros (posiciones $t+1, t+2, \ldots$). Permitir que el decoder "vea" los tokens futuros durante el entrenamiento constituiría una fuga de información (*information leakage*) que haría inútil el modelo para generación.

La máscara causal se implementa modificando los puntajes de atención antes de aplicar la función softmax. Definimos una matriz de máscara $\mathbf{M} \in \mathbb{R}^{T \times T}$ de la siguiente forma:

$$M_{ij} = \begin{cases} 0 & \text{si } j \leq i \\ -\infty & \text{si } j > i \end{cases}$$

Esta es una matriz triangular superior (excluyendo la diagonal) con valores $-\infty$. La atención enmascarada se calcula como:

$$\text{MaskedAttention}(\mathbf{Q}, \mathbf{K}, \mathbf{V}) = \text{softmax}\left(\frac{\mathbf{Q}\mathbf{K}^\top}{\sqrt{d_k}} + \mathbf{M}\right)\mathbf{V}$$

La adición de $-\infty$ en las posiciones correspondientes a tokens futuros tiene un efecto crucial: al aplicar la función softmax, $e^{-\infty} = 0$, por lo que los pesos de atención para las posiciones futuras se anulan completamente. Veamos un ejemplo concreto para una secuencia de longitud $T = 4$. La matriz de puntajes brutos (antes de la máscara) podría ser:

$$\frac{\mathbf{Q}\mathbf{K}^\top}{\sqrt{d_k}} = \begin{bmatrix} s_{11} & s_{12} & s_{13} & s_{14} \\ s_{21} & s_{22} & s_{23} & s_{24} \\ s_{31} & s_{32} & s_{33} & s_{34} \\ s_{41} & s_{42} & s_{43} & s_{44} \end{bmatrix}$$

Después de aplicar la máscara:

$$\frac{\mathbf{Q}\mathbf{K}^\top}{\sqrt{d_k}} + \mathbf{M} = \begin{bmatrix} s_{11} & -\infty & -\infty & -\infty \\ s_{21} & s_{22} & -\infty & -\infty \\ s_{31} & s_{32} & s_{33} & -\infty \\ s_{41} & s_{42} & s_{43} & s_{44} \end{bmatrix}$$

Y después de softmax (aplicado fila por fila):

$$\text{softmax}\left(\frac{\mathbf{Q}\mathbf{K}^\top}{\sqrt{d_k}} + \mathbf{M}\right) = \begin{bmatrix} 1 & 0 & 0 & 0 \\ \alpha_{21} & \alpha_{22} & 0 & 0 \\ \alpha_{31} & \alpha_{32} & \alpha_{33} & 0 \\ \alpha_{41} & \alpha_{42} & \alpha_{43} & \alpha_{44} \end{bmatrix}$$

donde $\alpha_{ij} > 0$ y $\sum_j \alpha_{ij} = 1$ para cada fila $i$. Observemos que:

- El token en la posición 1 solo puede atender a sí mismo (toda la distribución se concentra en la posición 1).
- El token en la posición 2 puede atender a las posiciones 1 y 2.
- El token en la posición 3 puede atender a las posiciones 1, 2 y 3.
- El token en la posición 4 puede atender a todas las posiciones.

Esta estructura triangular inferior garantiza la propiedad *autoregresiva*: la predicción del token $t$ depende únicamente de los tokens anteriores, lo cual es esencial para la generación secuencial de texto.

### 6.4.3 Atención Encoder-Decoder (*Cross-Attention*)

La segunda sub-capa del decoder, la *atención cruzada* o *encoder-decoder attention*, es el mecanismo que permite al decoder acceder a la información codificada por el encoder. En esta sub-capa:

- Las **consultas** ($\mathbf{Q}$) provienen de la salida de la sub-capa anterior del decoder (la self-attention enmascarada).
- Las **claves** ($\mathbf{K}$) y los **valores** ($\mathbf{V}$) provienen de la salida del último bloque encoder.

Formalmente:

$$\mathbf{Q} = \mathbf{m}^{(\ell)} \mathbf{W}^Q_{\text{cross}}, \quad \mathbf{K} = \mathbf{Z}^{(N)} \mathbf{W}^K_{\text{cross}}, \quad \mathbf{V} = \mathbf{Z}^{(N)} \mathbf{W}^V_{\text{cross}}$$

donde $\mathbf{m}^{(\ell)} \in \mathbb{R}^{T_{\text{target}} \times d_{model}}$ es la salida de la self-attention enmascarada del decoder y $\mathbf{Z}^{(N)} \in \mathbb{R}^{T_{\text{source}} \times d_{model}}$ es la salida del encoder.

La atención cruzada no utiliza máscara causal, ya que cada posición del decoder puede (y debe) atender a todas las posiciones de la secuencia de entrada. La matriz de atención resultante tiene dimensiones $T_{\text{target}} \times T_{\text{source}}$, donde cada fila indica cómo una posición del decoder distribuye su atención sobre las posiciones de la secuencia de entrada.

Este mecanismo es análogo al mecanismo de atención de Bahdanau utilizado en las arquitecturas encoder-decoder basadas en RNN, pero con la diferencia crucial de que aquí se emplea atención multi-cabezal con múltiples proyecciones aprendidas, lo que permite al modelo capturar diferentes tipos de relaciones entre la fuente y el objetivo simultáneamente.

La atención cruzada es particularmente importante en tareas como la traducción automática, donde el decoder necesita saber qué partes de la oración fuente son relevantes para generar cada palabra de la oración objetivo. En el contexto de las comunicaciones semánticas, la atención cruzada permite que el receptor (decoder) acceda a las representaciones codificadas del transmisor (encoder) para reconstruir o interpretar el mensaje original.

### 6.4.4 Feed-Forward Network del decoder

La tercera sub-capa del decoder es una red feed-forward idéntica en estructura a la del encoder:

$$\text{FFN}(\mathbf{x}) = \max(0, \mathbf{x}\mathbf{W}_1 + \mathbf{b}_1)\mathbf{W}_2 + \mathbf{b}_2$$

Al igual que en el encoder, esta red se aplica posición por posición de manera independiente, con los mismos hiperparámetros ($d_{model}$ y $d_{ff}$). Sin embargo, los pesos de la FFN del decoder son distintos de los del encoder: cada bloque decoder tiene sus propios parámetros independientes.

**Figura 6.3:** *Diagrama detallado de un bloque decoder del Transformer. La entrada $\mathbf{Y}^{(\ell-1)}$ (los embeddings de la secuencia objetivo, desplazados una posición) ingresa a la primera sub-capa: Masked Multi-Head Self-Attention, donde la máscara causal impide que las posiciones atiendan a tokens futuros (representada visualmente como una matriz triangular inferior). La salida se suma con la entrada (Add) y se normaliza (Norm). La representación resultante alimenta la segunda sub-capa: Multi-Head Encoder-Decoder Attention, donde las consultas provienen del decoder y las claves/valores provienen de la salida del encoder $\mathbf{Z}^{(N)}$ (mostrada como una flecha que ingresa desde la izquierda, procedente del encoder). Nuevamente se aplica Add & Norm. Finalmente, la tercera sub-capa es la Feed-Forward Network, seguida de Add & Norm, produciendo la salida $\mathbf{Y}^{(\ell)}$. Las tres conexiones residuales se muestran como flechas que bordean cada sub-capa. El bloque completo está etiquetado "$\times N$" para indicar su repetición.*

---

## 6.5 La arquitectura completa Encoder-Decoder

### 6.5.1 Pipeline completo

La arquitectura completa del Transformer combina las pilas de encoder y decoder en un flujo de procesamiento de extremo a extremo para tareas de secuencia a secuencia (*sequence-to-sequence*). El pipeline completo es el siguiente:

**Lado del encoder:**
1. La secuencia de entrada $(x_1, x_2, \ldots, x_{T_s})$ se convierte en embeddings mediante una capa de embedding compartida o dedicada.
2. Se suman las codificaciones posicionales: $\mathbf{z}_t^{(0)} = \sqrt{d_{model}} \cdot \text{Embed}(x_t) + \mathbf{PE}_t$.
3. Los vectores resultantes pasan a través de la pila de $N$ bloques encoder: $\mathbf{Z}^{(0)} \rightarrow \mathbf{Z}^{(1)} \rightarrow \cdots \rightarrow \mathbf{Z}^{(N)}$.
4. La salida del encoder $\mathbf{Z}^{(N)} \in \mathbb{R}^{T_s \times d_{model}}$ contiene las representaciones contextualizadas de la secuencia fuente.

**Lado del decoder:**
1. La secuencia objetivo $(y_1, y_2, \ldots, y_{T_t})$ se desplaza una posición a la derecha, insertando un token especial de inicio $\langle \text{SOS} \rangle$ al principio: $(\langle \text{SOS} \rangle, y_1, y_2, \ldots, y_{T_t-1})$.
2. Se aplican embeddings y codificaciones posicionales de manera análoga al encoder.
3. Los vectores pasan a través de la pila de $N$ bloques decoder, donde cada bloque recibe la salida del encoder $\mathbf{Z}^{(N)}$ a través de las capas de atención cruzada.
4. La salida del decoder $\mathbf{Y}^{(N)} \in \mathbb{R}^{T_t \times d_{model}}$ contiene las representaciones del objetivo.

**Capa de salida:**
1. Se aplica una transformación lineal: $\mathbf{logits} = \mathbf{Y}^{(N)} \mathbf{W}_{\text{out}} + \mathbf{b}_{\text{out}}$, donde $\mathbf{W}_{\text{out}} \in \mathbb{R}^{d_{model} \times V}$ y $V$ es el tamaño del vocabulario.
2. Se aplica softmax para obtener las probabilidades sobre el vocabulario: $P(y_t | y_{<t}, \mathbf{X}) = \text{softmax}(\mathbf{logits}_t)$.

Formalmente, el Transformer completo modela la distribución condicional:

$$P(y_1, y_2, \ldots, y_{T_t} | x_1, x_2, \ldots, x_{T_s}) = \prod_{t=1}^{T_t} P(y_t | y_1, \ldots, y_{t-1}, x_1, \ldots, x_{T_s})$$

La factorización autoregresiva del lado derecho es lo que permite la generación token por token durante la inferencia.

### 6.5.2 Parámetros del modelo base

El Transformer original se presentó en dos configuraciones:

**Modelo base (*Transformer Base*):**

| Hiperparámetro | Símbolo | Valor |
|---|---|---|
| Dimensión del modelo | $d_{model}$ | 512 |
| Número de cabezas de atención | $h$ | 8 |
| Número de capas (encoder y decoder) | $N$ | 6 |
| Dimensión de la capa oculta FFN | $d_{ff}$ | 2048 |
| Dimensión de consultas y claves | $d_k$ | 64 |
| Dimensión de valores | $d_v$ | 64 |
| Dropout | $p_{drop}$ | 0.1 |

**Modelo grande (*Transformer Big*):**

| Hiperparámetro | Símbolo | Valor |
|---|---|---|
| Dimensión del modelo | $d_{model}$ | 1024 |
| Número de cabezas de atención | $h$ | 16 |
| Número de capas (encoder y decoder) | $N$ | 6 |
| Dimensión de la capa oculta FFN | $d_{ff}$ | 4096 |
| Dimensión de consultas y claves | $d_k$ | 64 |
| Dimensión de valores | $d_v$ | 64 |
| Dropout | $p_{drop}$ | 0.3 |

Nótese que en ambos modelos se cumple que $d_k = d_v = d_{model} / h$. Esta relación asegura que el costo computacional de la atención multi-cabezal sea comparable al de una atención de una sola cabeza con la dimensión completa $d_{model}$.

El número total de parámetros del modelo base es aproximadamente 65 millones, distribuidos entre las capas de embedding, las matrices de proyección de la atención, los pesos de las FFN y los parámetros de normalización. Para el modelo grande, el número de parámetros asciende a aproximadamente 213 millones.

### 6.5.3 Complejidad computacional

Es instructivo analizar la complejidad computacional de las operaciones principales del Transformer. Para una secuencia de longitud $T$:

- **Self-Attention**: La multiplicación $\mathbf{Q}\mathbf{K}^\top$ tiene complejidad $O(T^2 \cdot d_k)$, y la multiplicación del resultado con $\mathbf{V}$ tiene complejidad $O(T^2 \cdot d_v)$. La complejidad total es $O(T^2 \cdot d_{model})$, que es cuadrática en la longitud de la secuencia.
- **FFN posición por posición**: Tiene complejidad $O(T \cdot d_{model} \cdot d_{ff})$, que es lineal en la longitud de la secuencia.
- **RNN (para comparación)**: Tiene complejidad $O(T \cdot d_{model}^2)$ por capa, también lineal en $T$ pero con una constante mayor.

La complejidad cuadrática de la self-attention con respecto a $T$ es la principal limitación del Transformer para secuencias muy largas, y ha motivado una línea activa de investigación en variantes eficientes como Linformer, Performer, o los mecanismos de atención local/dispersa (*sparse attention*).

Sin embargo, para secuencias de longitud moderada (hasta unos pocos miles de tokens), la ventaja del Transformer reside en su *longitud de camino máxima* constante $O(1)$ entre cualquier par de posiciones (frente a $O(T)$ en RNN y $O(\log T)$ en redes convolucionales), lo que facilita el aprendizaje de dependencias a largo alcance.

**Figura 6.4:** *Arquitectura completa del Transformer tal como se presenta en el artículo original. En el lado izquierdo se muestra el encoder: la secuencia de entrada pasa por la capa de embeddings (rectángulo inferior), a la que se suman las codificaciones posicionales (representadas por ondas sinusoidales). Los vectores resultantes ingresan a una pila de $N=6$ bloques encoder idénticos (representados como un rectángulo grande con la etiqueta "$\times N$"), cada uno con sus sub-capas de Multi-Head Attention y Feed Forward con conexiones Add & Norm. En el lado derecho se muestra el decoder: la secuencia objetivo (desplazada a la derecha) pasa igualmente por embeddings y codificaciones posicionales, e ingresa a una pila de $N=6$ bloques decoder, cada uno con Masked Multi-Head Attention, atención cruzada (con flechas que conectan desde la salida del encoder) y Feed Forward, todas con Add & Norm. La salida del último bloque decoder pasa por una capa lineal y softmax para producir las probabilidades de salida. Las flechas entre el encoder y el decoder representan el flujo de las claves y valores del encoder hacia las capas de atención cruzada del decoder.*

---

## 6.6 Entrenamiento del Transformer

### 6.6.1 Teacher Forcing

El entrenamiento del Transformer para tareas de generación de secuencias utiliza una técnica llamada *teacher forcing* (forzamiento por el profesor). En lugar de alimentar al decoder con sus propias predicciones (lo que introduciría un problema de retroalimentación y haría el entrenamiento más lento e inestable), durante el entrenamiento se le proporciona la secuencia objetivo correcta (*ground truth*) como entrada.

Concretamente, si la secuencia objetivo es $(y_1, y_2, \ldots, y_{T_t})$, la entrada al decoder es la secuencia desplazada $(\langle \text{SOS} \rangle, y_1, y_2, \ldots, y_{T_t-1})$, y se espera que la salida prediga $(y_1, y_2, \ldots, y_{T_t})$. Es decir, en cada posición $t$, el decoder recibe los tokens correctos en las posiciones $1, \ldots, t-1$ y debe predecir $y_t$.

La máscara causal garantiza que, aunque todos los tokens correctos están presentes en la entrada, la posición $t$ solo puede ver los tokens en las posiciones $1, \ldots, t-1$. Esto simula las condiciones de inferencia, donde los tokens futuros no están disponibles, pero permite que todas las posiciones se procesen en paralelo durante el entrenamiento.

El *teacher forcing* tiene la ventaja de acelerar significativamente el entrenamiento al proporcionar una señal de supervisión clara en cada posición. Sin embargo, puede crear una discrepancia entre el entrenamiento (donde las entradas siempre son correctas) y la inferencia (donde las entradas pueden contener errores de predicciones anteriores). Esta discrepancia, conocida como *exposure bias* (sesgo de exposición), puede mitigarse parcialmente con técnicas como el *scheduled sampling*, donde gradualmente se reemplazan algunas entradas correctas por predicciones del modelo durante el entrenamiento.

### 6.6.2 Función de pérdida: Entropía cruzada

El objetivo del entrenamiento es minimizar la *entropía cruzada* (*cross-entropy loss*) entre la distribución de probabilidad predicha y la distribución real (one-hot) sobre el vocabulario. Para una secuencia objetivo $(y_1, y_2, \ldots, y_{T_t})$, la pérdida se define como:

$$\mathcal{L} = -\frac{1}{T_t} \sum_{t=1}^{T_t} \log P(y_t | y_{<t}, \mathbf{X})$$

donde $P(y_t | y_{<t}, \mathbf{X})$ es la probabilidad asignada por el modelo al token correcto $y_t$ en la posición $t$, dada la secuencia de entrada $\mathbf{X}$ y los tokens objetivo anteriores $y_{<t} = (y_1, \ldots, y_{t-1})$.

Equivalentemente, si $\hat{\mathbf{p}}_t \in \mathbb{R}^V$ es el vector de probabilidades predicho por el modelo (después de softmax) y $\mathbf{y}_t \in \mathbb{R}^V$ es la representación one-hot del token objetivo, entonces:

$$\mathcal{L} = -\frac{1}{T_t} \sum_{t=1}^{T_t} \mathbf{y}_t^\top \log \hat{\mathbf{p}}_t = -\frac{1}{T_t} \sum_{t=1}^{T_t} \log \hat{p}_{t, y_t}$$

Minimizar esta pérdida es equivalente a maximizar la verosimilitud (*likelihood*) de la secuencia objetivo dado el modelo, es decir, maximizar:

$$\prod_{t=1}^{T_t} P(y_t | y_{<t}, \mathbf{X})$$

### 6.6.3 Suavizado de etiquetas (*Label Smoothing*)

El Transformer original utiliza *label smoothing* con un parámetro $\epsilon_{ls} = 0.1$. En lugar de usar distribuciones one-hot puras para los tokens objetivo, se suaviza la distribución asignando una pequeña probabilidad a todos los tokens del vocabulario:

$$q(y_t = k) = \begin{cases} 1 - \epsilon_{ls} & \text{si } k = y_t^* \text{ (token correcto)} \\ \frac{\epsilon_{ls}}{V - 1} & \text{en caso contrario} \end{cases}$$

donde $y_t^*$ es el token objetivo correcto y $V$ es el tamaño del vocabulario. La pérdida con label smoothing se calcula entonces como la divergencia KL entre esta distribución suavizada $q$ y la distribución predicha $\hat{p}$:

$$\mathcal{L}_{ls} = -\sum_{k=1}^{V} q(y_t = k) \log \hat{p}_{t,k}$$

El label smoothing tiene varios beneficios:

1. **Previene sobreconfianza.** Sin suavizado, el modelo tiende a asignar probabilidades muy cercanas a 1 para el token correcto, lo cual puede llevar a gradientes extremadamente pequeños y reducir la capacidad del modelo para seguir aprendiendo.
2. **Actúa como regularizador.** Al penalizar distribuciones muy concentradas, el label smoothing fomenta que el modelo produzca distribuciones más calibradas.
3. **Mejora la generalización.** Aunque el label smoothing reduce ligeramente la perplejidad en el conjunto de entrenamiento, típicamente mejora las métricas de evaluación como BLEU en el conjunto de prueba.

### 6.6.4 Esquema de tasa de aprendizaje con calentamiento (*Warm-up*)

El Transformer utiliza un esquema de tasa de aprendizaje no estándar que combina una fase de calentamiento lineal con una fase de decaimiento proporcional al inverso de la raíz cuadrada del número de pasos. La fórmula es:

$$lr = d_{model}^{-0.5} \cdot \min\left(step^{-0.5}, \ step \cdot warmup\_steps^{-1.5}\right)$$

Analicemos esta fórmula en detalle:

- **Fase de calentamiento** ($step \leq warmup\_steps$): cuando $step$ es pequeño, $step \cdot warmup\_steps^{-1.5} < step^{-0.5}$, por lo que $lr = d_{model}^{-0.5} \cdot step \cdot warmup\_steps^{-1.5}$. La tasa de aprendizaje crece *linealmente* con el número de pasos, desde un valor cercano a cero hasta su máximo. Con $warmup\_steps = 4000$ (el valor usado en el artículo original), el máximo se alcanza en el paso 4000.

- **Fase de decaimiento** ($step > warmup\_steps$): cuando $step$ es grande, $step^{-0.5} < step \cdot warmup\_steps^{-1.5}$, por lo que $lr = d_{model}^{-0.5} \cdot step^{-0.5}$. La tasa de aprendizaje decrece proporcionalmente a $1/\sqrt{step}$, lo que corresponde a un decaimiento suave.

- **Valor máximo**: el máximo de la tasa de aprendizaje se alcanza cuando $step = warmup\_steps$, y su valor es $lr_{\max} = d_{model}^{-0.5} \cdot warmup\_steps^{-0.5}$. Para $d_{model} = 512$ y $warmup\_steps = 4000$, esto da $lr_{\max} = \frac{1}{\sqrt{512} \cdot \sqrt{4000}} \approx \frac{1}{22.63 \times 63.25} \approx 6.99 \times 10^{-4}$.

El factor $d_{model}^{-0.5}$ ajusta la tasa de aprendizaje según el tamaño del modelo: modelos más grandes tienen tasas de aprendizaje más pequeñas, lo cual es consistente con la observación empírica de que los gradientes tienden a ser más grandes en modelos con mayor dimensionalidad.

La fase de calentamiento es crucial para la estabilidad del entrenamiento. Al inicio del entrenamiento, las representaciones del modelo están esencialmente aleatorias, y los gradientes pueden ser ruidosos y de gran magnitud. Comenzar con una tasa de aprendizaje pequeña permite que el modelo se "estabilice" gradualmente antes de aplicar actualizaciones más agresivas. Sin el calentamiento, el entrenamiento del Transformer tiende a ser inestable y puede divergir.

El optimizador utilizado es Adam (Kingma & Ba, 2015), con parámetros $\beta_1 = 0.9$, $\beta_2 = 0.98$ y $\epsilon = 10^{-9}$.

> **Referencia:** Kingma, D. P., & Ba, J. (2015). Adam: A method for stochastic optimization. *Proceedings of the 3rd International Conference on Learning Representations (ICLR)*. (DOI: 10.48550/arXiv.1412.6980)

### 6.6.5 Regularización

Además del label smoothing, el Transformer original emplea las siguientes técnicas de regularización:

1. **Dropout.** Se aplica dropout con probabilidad $p_{drop} = 0.1$ (modelo base) o $p_{drop} = 0.3$ (modelo grande) a:
   - Las salidas de cada sub-capa, antes de la conexión residual.
   - Los pesos de atención (después de softmax).
   - Las codificaciones posicionales sumadas a los embeddings.

2. **Compartición de pesos.** En el modelo original, la matriz de embeddings de entrada del encoder, la matriz de embeddings de entrada del decoder y la matriz de proyección de salida antes del softmax comparten los mismos pesos (transpuestos para la capa de salida). Esto reduce el número total de parámetros y proporciona una regularización implícita al vincular las representaciones de entrada y salida.

---

## 6.7 Variantes de Transformers

Desde la publicación del Transformer original, la arquitectura ha dado lugar a una familia diversa de modelos que se han convertido en la base del aprendizaje profundo moderno. Las tres principales variantes arquitectónicas se distinguen por qué componentes del Transformer original utilizan.

### 6.7.1 Modelos solo-encoder: BERT

BERT (*Bidirectional Encoder Representations from Transformers*), desarrollado por Devlin et al. (2019) en Google, utiliza únicamente la pila de encoder del Transformer. La idea central de BERT es pre-entrenar representaciones bidireccionales profundas a partir de texto no etiquetado, condicionando cada token en su contexto tanto izquierdo como derecho.

**Características clave:**
- **Bidireccionalidad completa:** A diferencia de los modelos autoregresivos que solo procesan el contexto izquierdo (o derecho), BERT utiliza self-attention sin máscara causal, permitiendo que cada token atienda a todos los demás tokens de la secuencia. Esto es posible porque BERT no genera texto, sino que produce representaciones para tareas de comprensión.
- **Pre-entrenamiento con Masked Language Modeling (MLM):** Durante el pre-entrenamiento, se enmascara aleatoriamente el 15% de los tokens de entrada (reemplazándolos por un token especial `[MASK]`) y el modelo debe predecir los tokens originales. Esto obliga al modelo a desarrollar representaciones contextuales ricas.
- **Pre-entrenamiento con Next Sentence Prediction (NSP):** El modelo también aprende a predecir si dos oraciones son consecutivas en el texto original.
- **Fine-tuning:** Después del pre-entrenamiento, BERT se ajusta finamente (*fine-tuning*) en tareas específicas como clasificación de texto, respuesta a preguntas o reconocimiento de entidades nombradas, añadiendo una capa de salida simple.

BERT-base tiene 12 capas, $d_{model} = 768$ y 12 cabezas de atención (110M parámetros), mientras que BERT-large tiene 24 capas, $d_{model} = 1024$ y 16 cabezas (340M parámetros).

> **Referencia:** Devlin, J., Chang, M.-W., Lee, K., & Toutanova, K. (2019). BERT: Pre-training of deep bidirectional transformers for language understanding. *Proceedings of NAACL-HLT*, 4171-4186. (DOI: 10.18653/v1/N19-1423)

### 6.7.2 Modelos solo-decoder: GPT

La familia GPT (*Generative Pre-trained Transformer*), desarrollada por OpenAI, utiliza únicamente la pila de decoder del Transformer (sin atención cruzada, ya que no hay encoder). Estos modelos son *autoregresivos*: generan texto un token a la vez, condicionando cada token en todos los tokens anteriores.

**Características clave:**
- **Atención causal (unidireccional):** Se utiliza la máscara causal para que cada posición solo pueda atender a las posiciones anteriores, lo cual es necesario para la generación secuencial.
- **Pre-entrenamiento con modelado de lenguaje:** El objetivo del pre-entrenamiento es predecir el siguiente token dado los tokens anteriores: $P(x_t | x_1, \ldots, x_{t-1})$. Este objetivo es más simple que el MLM de BERT y se entrena con la pérdida de entropía cruzada estándar.
- **Escalabilidad:** La familia GPT ha demostrado que aumentar el tamaño del modelo y la cantidad de datos de entrenamiento mejora consistentemente el rendimiento (*scaling laws*). GPT-2 tiene 1.5 mil millones de parámetros, GPT-3 tiene 175 mil millones, y modelos posteriores son aún mayores.
- **Aprendizaje en contexto (*In-context Learning*):** Los modelos GPT grandes pueden realizar tareas sin necesidad de fine-tuning, simplemente proporcionando ejemplos en el *prompt* (pocos disparos o *few-shot learning*).

> **Referencia:** Radford, A., Narasimhan, K., Salimans, T., & Sutskever, I. (2018). Improving language understanding by generative pre-training. *OpenAI technical report*.

### 6.7.3 Modelos Encoder-Decoder: T5

T5 (*Text-to-Text Transfer Transformer*), desarrollado por Raffel et al. (2020) en Google, utiliza la arquitectura encoder-decoder completa del Transformer original. La innovación principal de T5 es reformular *todas* las tareas de NLP como problemas de texto a texto: la entrada es una cadena de texto y la salida es otra cadena de texto.

**Características clave:**
- **Formato unificado:** Tareas como clasificación, resumen, traducción, respuesta a preguntas, y análisis de sentimiento se expresan todas como transformaciones de texto a texto, precedidas por un prefijo que indica la tarea (por ejemplo, "translate English to German: ...").
- **Pre-entrenamiento con span corruption:** Similar al MLM de BERT, pero en lugar de enmascarar tokens individuales, se enmascaran *spans* (secuencias contiguas) de tokens, y el decoder genera los spans faltantes.
- **Estudio exhaustivo:** El artículo de T5 realizó un estudio comparativo sistemático de diferentes arquitecturas, objetivos de pre-entrenamiento, conjuntos de datos y estrategias de transferencia, proporcionando insights valiosos para la comunidad.

> **Referencia:** Raffel, C., Shazeer, N., Roberts, A., Lee, K., Narang, S., Matena, M., Zhou, Y., Li, W., & Liu, P. J. (2020). Exploring the limits of transfer learning with a unified text-to-text transformer. *Journal of Machine Learning Research*, 21(140), 1-67. (DOI: 10.5555/3455716.3455856)

### 6.7.4 Vision Transformer (ViT)

El Vision Transformer (ViT), propuesto por Dosovitskiy et al. (2021), demostró que la arquitectura Transformer puede aplicarse directamente a imágenes, rompiendo el dominio de las redes convolucionales (CNN) en visión por computadora.

**Funcionamiento:**
1. La imagen de entrada de dimensiones $H \times W \times C$ se divide en parches (*patches*) no superpuestos de tamaño $P \times P$.
2. Cada parche se aplana y se proyecta linealmente a un vector de dimensión $d_{model}$, creando una secuencia de $N = HW/P^2$ "tokens de imagen".
3. Se añade un token especial `[CLS]` al inicio de la secuencia, cuya representación final se usa para clasificación.
4. Se suman codificaciones posicionales aprendidas (en lugar de sinusoidales).
5. La secuencia resultante se procesa con un encoder Transformer estándar.
6. La representación del token `[CLS]` en la última capa se usa para clasificación.

ViT demostró que, con suficientes datos de pre-entrenamiento (como JFT-300M o ImageNet-21k), los Transformers pueden igualar o superar a las CNN más avanzadas, con la ventaja de una mayor flexibilidad y escalabilidad. Este resultado ha tenido un impacto profundo en la visión por computadora y ha inspirado numerosas extensiones, incluidas las que son relevantes para la codificación de imágenes y video en comunicaciones semánticas.

> **Referencia:** Dosovitskiy, A., Beyer, L., Kolesnikov, A., Weissenborn, D., Zhai, X., Unterthiner, T., Dehghani, M., Minderer, M., Heigold, G., Gelly, S., Uszkoreit, J., & Houlsby, N. (2021). An image is worth 16x16 words: Transformers for image recognition at scale. *Proceedings of the 9th International Conference on Learning Representations (ICLR)*. (DOI: 10.48550/arXiv.2010.11929)

### 6.7.5 Resumen comparativo

| Variante | Componentes | Atención | Tarea típica | Ejemplo |
|---|---|---|---|---|
| Solo-Encoder | Encoder | Bidireccional | Comprensión | BERT, RoBERTa |
| Solo-Decoder | Decoder | Causal (unidireccional) | Generación | GPT, LLaMA |
| Encoder-Decoder | Ambos | Bidireccional + Causal + Cruzada | Seq2Seq | T5, BART, Transformer original |
| ViT | Encoder | Bidireccional | Clasificación de imágenes | ViT, DeiT |

---

## 6.8 Implementación en PyTorch

### 6.8.1 Codificación posicional

A continuación, presentamos una implementación completa y comentada de la codificación posicional sinusoidal en PyTorch:

```python
import torch
import torch.nn as nn
import math

class PositionalEncoding(nn.Module):
    """
    Codificación posicional sinusoidal según Vaswani et al. (2017).
    Genera vectores de posición fijos basados en funciones seno y coseno
    de diferentes frecuencias, que se suman a los embeddings de entrada.
    """
    def __init__(self, d_model: int, max_len: int = 5000, dropout: float = 0.1):
        """
        Args:
            d_model: Dimensión del modelo (debe ser par).
            max_len: Longitud máxima de secuencia soportada.
            dropout: Probabilidad de dropout aplicada después de sumar PE.
        """
        super().__init__()
        self.dropout = nn.Dropout(p=dropout)

        # Crear matriz de codificación posicional [max_len, d_model]
        pe = torch.zeros(max_len, d_model)

        # Vector de posiciones: [0, 1, 2, ..., max_len-1], shape [max_len, 1]
        position = torch.arange(0, max_len, dtype=torch.float).unsqueeze(1)

        # Término de división para las frecuencias geométricas.
        # exp(-2i * log(10000) / d_model) = 1 / 10000^(2i/d_model)
        div_term = torch.exp(
            torch.arange(0, d_model, 2).float() * (-math.log(10000.0) / d_model)
        )

        # Dimensiones pares: seno
        pe[:, 0::2] = torch.sin(position * div_term)
        # Dimensiones impares: coseno
        pe[:, 1::2] = torch.cos(position * div_term)

        # Añadir dimensión de batch: [1, max_len, d_model]
        pe = pe.unsqueeze(0)

        # Registrar como buffer (no es un parámetro entrenable)
        self.register_buffer('pe', pe)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Args:
            x: Tensor de embeddings [batch_size, seq_len, d_model]
        Returns:
            Embeddings con codificación posicional sumada [batch_size, seq_len, d_model]
        """
        # Sumar codificación posicional (broadcasting sobre batch)
        x = x + self.pe[:, :x.size(1), :]
        return self.dropout(x)
```

Observemos que la codificación posicional se registra como un *buffer* (no como un parámetro), lo que significa que se guarda con el modelo pero no se actualiza durante el entrenamiento. El cálculo del `div_term` utiliza la identidad $10000^{-2i/d_{model}} = e^{-2i \cdot \ln(10000) / d_{model}}$, que es numéricamente más estable que calcular la potencia directamente.

### 6.8.2 Bloque Transformer (Encoder)

Implementamos ahora un bloque encoder completo del Transformer:

```python
class MultiHeadAttention(nn.Module):
    """
    Atención multi-cabezal escalada por producto punto.
    Implementa h cabezas de atención en paralelo.
    """
    def __init__(self, d_model: int, num_heads: int, dropout: float = 0.1):
        super().__init__()
        assert d_model % num_heads == 0, "d_model debe ser divisible por num_heads"

        self.d_model = d_model
        self.num_heads = num_heads
        self.d_k = d_model // num_heads  # Dimensión por cabeza

        # Proyecciones lineales para Q, K, V y salida
        self.W_q = nn.Linear(d_model, d_model)  # Proyecta a [batch, seq, d_model]
        self.W_k = nn.Linear(d_model, d_model)
        self.W_v = nn.Linear(d_model, d_model)
        self.W_o = nn.Linear(d_model, d_model)  # Proyección de salida

        self.dropout = nn.Dropout(p=dropout)

    def scaled_dot_product_attention(
        self, Q: torch.Tensor, K: torch.Tensor, V: torch.Tensor,
        mask: torch.Tensor = None
    ) -> torch.Tensor:
        """
        Calcula atención escalada por producto punto.
        Args:
            Q: Consultas [batch, heads, seq_q, d_k]
            K: Claves   [batch, heads, seq_k, d_k]
            V: Valores   [batch, heads, seq_k, d_v]
            mask: Máscara opcional [batch, 1, seq_q, seq_k] o [1, 1, seq_q, seq_k]
        Returns:
            Salida de atención [batch, heads, seq_q, d_v]
        """
        # Puntajes de atención: QK^T / sqrt(d_k)
        scores = torch.matmul(Q, K.transpose(-2, -1)) / math.sqrt(self.d_k)

        # Aplicar máscara si se proporciona
        if mask is not None:
            scores = scores.masked_fill(mask == 0, float('-inf'))

        # Softmax sobre la última dimensión (dim de claves)
        attention_weights = torch.softmax(scores, dim=-1)
        attention_weights = self.dropout(attention_weights)

        # Multiplicar por valores
        output = torch.matmul(attention_weights, V)
        return output

    def forward(
        self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor,
        mask: torch.Tensor = None
    ) -> torch.Tensor:
        """
        Args:
            query: [batch, seq_q, d_model]
            key:   [batch, seq_k, d_model]
            value: [batch, seq_k, d_model]
            mask:  Máscara opcional
        Returns:
            Salida [batch, seq_q, d_model]
        """
        batch_size = query.size(0)

        # 1. Proyecciones lineales y reorganización en cabezas
        #    [batch, seq, d_model] -> [batch, seq, num_heads, d_k] -> [batch, num_heads, seq, d_k]
        Q = self.W_q(query).view(batch_size, -1, self.num_heads, self.d_k).transpose(1, 2)
        K = self.W_k(key).view(batch_size, -1, self.num_heads, self.d_k).transpose(1, 2)
        V = self.W_v(value).view(batch_size, -1, self.num_heads, self.d_k).transpose(1, 2)

        # 2. Atención escalada
        attn_output = self.scaled_dot_product_attention(Q, K, V, mask)

        # 3. Concatenar cabezas y proyectar
        #    [batch, num_heads, seq, d_k] -> [batch, seq, d_model]
        attn_output = attn_output.transpose(1, 2).contiguous().view(
            batch_size, -1, self.d_model
        )

        # 4. Proyección de salida
        return self.W_o(attn_output)


class FeedForwardNetwork(nn.Module):
    """
    Red feed-forward posición por posición.
    Dos capas lineales con activación ReLU intermedia.
    """
    def __init__(self, d_model: int, d_ff: int, dropout: float = 0.1):
        super().__init__()
        self.linear1 = nn.Linear(d_model, d_ff)    # Expansión: d_model -> d_ff
        self.linear2 = nn.Linear(d_ff, d_model)    # Compresión: d_ff -> d_model
        self.dropout = nn.Dropout(p=dropout)
        self.relu = nn.ReLU()

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Args:
            x: [batch, seq_len, d_model]
        Returns:
            [batch, seq_len, d_model]
        """
        # FFN(x) = max(0, xW1 + b1)W2 + b2
        return self.linear2(self.dropout(self.relu(self.linear1(x))))


class TransformerEncoderBlock(nn.Module):
    """
    Un bloque encoder del Transformer.
    Contiene: Multi-Head Self-Attention + Add&Norm + FFN + Add&Norm
    """
    def __init__(self, d_model: int, num_heads: int, d_ff: int, dropout: float = 0.1):
        super().__init__()

        # Sub-capa 1: Multi-Head Self-Attention
        self.self_attention = MultiHeadAttention(d_model, num_heads, dropout)
        self.norm1 = nn.LayerNorm(d_model)

        # Sub-capa 2: Feed-Forward Network
        self.feed_forward = FeedForwardNetwork(d_model, d_ff, dropout)
        self.norm2 = nn.LayerNorm(d_model)

        # Dropout para conexiones residuales
        self.dropout = nn.Dropout(p=dropout)

    def forward(self, x: torch.Tensor, mask: torch.Tensor = None) -> torch.Tensor:
        """
        Args:
            x: Entrada [batch, seq_len, d_model]
            mask: Máscara de padding opcional
        Returns:
            Salida [batch, seq_len, d_model]
        """
        # Sub-capa 1: Self-Attention con conexión residual y normalización
        # Post-LN: LN(x + Sublayer(x))
        attn_output = self.self_attention(x, x, x, mask)  # Q=K=V=x (self-attention)
        x = self.norm1(x + self.dropout(attn_output))     # Add & Norm

        # Sub-capa 2: FFN con conexión residual y normalización
        ff_output = self.feed_forward(x)
        x = self.norm2(x + self.dropout(ff_output))        # Add & Norm

        return x
```

### 6.8.3 Apilamiento de bloques: Encoder completo

Los bloques encoder se apilan para formar el encoder completo:

```python
class TransformerEncoder(nn.Module):
    """
    Encoder completo del Transformer: Embedding + PE + N bloques encoder.
    """
    def __init__(
        self, vocab_size: int, d_model: int, num_heads: int,
        d_ff: int, num_layers: int, max_len: int = 5000,
        dropout: float = 0.1
    ):
        super().__init__()

        # Capa de embedding: convierte índices de tokens en vectores densos
        self.embedding = nn.Embedding(vocab_size, d_model)
        self.d_model = d_model

        # Codificación posicional sinusoidal
        self.positional_encoding = PositionalEncoding(d_model, max_len, dropout)

        # Pila de N bloques encoder (cada uno con parámetros independientes)
        self.layers = nn.ModuleList([
            TransformerEncoderBlock(d_model, num_heads, d_ff, dropout)
            for _ in range(num_layers)
        ])

        # Normalización final (opcional, usada en algunas implementaciones)
        self.norm = nn.LayerNorm(d_model)

    def forward(self, src: torch.Tensor, mask: torch.Tensor = None) -> torch.Tensor:
        """
        Args:
            src: Tokens de entrada [batch, seq_len] (índices enteros)
            mask: Máscara de padding [batch, 1, 1, seq_len]
        Returns:
            Representaciones contextualizadas [batch, seq_len, d_model]
        """
        # 1. Embedding con escalado por sqrt(d_model)
        x = self.embedding(src) * math.sqrt(self.d_model)

        # 2. Sumar codificación posicional
        x = self.positional_encoding(x)

        # 3. Pasar por los N bloques encoder secuencialmente
        for layer in self.layers:
            x = layer(x, mask)

        # 4. Normalización final
        return self.norm(x)
```

### 6.8.4 Bloque Decoder

```python
class TransformerDecoderBlock(nn.Module):
    """
    Un bloque decoder del Transformer.
    Contiene: Masked Self-Attention + Add&Norm +
              Cross-Attention + Add&Norm + FFN + Add&Norm
    """
    def __init__(self, d_model: int, num_heads: int, d_ff: int, dropout: float = 0.1):
        super().__init__()

        # Sub-capa 1: Masked Multi-Head Self-Attention
        self.masked_self_attention = MultiHeadAttention(d_model, num_heads, dropout)
        self.norm1 = nn.LayerNorm(d_model)

        # Sub-capa 2: Multi-Head Encoder-Decoder (Cross) Attention
        self.cross_attention = MultiHeadAttention(d_model, num_heads, dropout)
        self.norm2 = nn.LayerNorm(d_model)

        # Sub-capa 3: Feed-Forward Network
        self.feed_forward = FeedForwardNetwork(d_model, d_ff, dropout)
        self.norm3 = nn.LayerNorm(d_model)

        self.dropout = nn.Dropout(p=dropout)

    def forward(
        self, x: torch.Tensor, encoder_output: torch.Tensor,
        src_mask: torch.Tensor = None, tgt_mask: torch.Tensor = None
    ) -> torch.Tensor:
        """
        Args:
            x: Entrada del decoder [batch, tgt_len, d_model]
            encoder_output: Salida del encoder [batch, src_len, d_model]
            src_mask: Máscara para la secuencia fuente (padding)
            tgt_mask: Máscara causal para la secuencia objetivo
        Returns:
            Salida [batch, tgt_len, d_model]
        """
        # Sub-capa 1: Masked Self-Attention (Q=K=V provienen del decoder)
        attn_output = self.masked_self_attention(x, x, x, tgt_mask)
        x = self.norm1(x + self.dropout(attn_output))

        # Sub-capa 2: Cross-Attention (Q del decoder, K y V del encoder)
        cross_output = self.cross_attention(x, encoder_output, encoder_output, src_mask)
        x = self.norm2(x + self.dropout(cross_output))

        # Sub-capa 3: Feed-Forward Network
        ff_output = self.feed_forward(x)
        x = self.norm3(x + self.dropout(ff_output))

        return x
```

### 6.8.5 Generación de la máscara causal

Una función auxiliar esencial es la creación de la máscara causal:

```python
def generate_causal_mask(size: int) -> torch.Tensor:
    """
    Genera una máscara causal (triangular inferior) para el decoder.
    Las posiciones futuras se enmascaran con False (0).

    Args:
        size: Longitud de la secuencia objetivo
    Returns:
        Máscara booleana [1, 1, size, size] donde True = posición permitida
    """
    # torch.tril: triangular inferior (incluye diagonal)
    mask = torch.tril(torch.ones(size, size)).bool()
    return mask.unsqueeze(0).unsqueeze(0)  # [1, 1, size, size]
```

Esta función genera la matriz de máscara descrita en la Sección 6.4.2. Por ejemplo, para `size=4`:

```
[[True,  False, False, False],
 [True,  True,  False, False],
 [True,  True,  True,  False],
 [True,  True,  True,  True ]]
```

Las posiciones con `False` recibirán un valor de $-\infty$ en los puntajes de atención, lo que se traduce en un peso de atención de cero después de la softmax.

### 6.8.6 Modelo Transformer completo

Finalmente, la integración de todos los componentes en un modelo Transformer completo para tareas de secuencia a secuencia:

```python
class Transformer(nn.Module):
    """
    Modelo Transformer completo (encoder-decoder) para tareas seq2seq.
    """
    def __init__(
        self, src_vocab_size: int, tgt_vocab_size: int,
        d_model: int = 512, num_heads: int = 8, num_layers: int = 6,
        d_ff: int = 2048, max_len: int = 5000, dropout: float = 0.1
    ):
        super().__init__()

        # Embeddings para fuente y objetivo
        self.src_embedding = nn.Embedding(src_vocab_size, d_model)
        self.tgt_embedding = nn.Embedding(tgt_vocab_size, d_model)
        self.d_model = d_model

        # Codificación posicional (compartida)
        self.positional_encoding = PositionalEncoding(d_model, max_len, dropout)

        # Pila de bloques encoder
        self.encoder_layers = nn.ModuleList([
            TransformerEncoderBlock(d_model, num_heads, d_ff, dropout)
            for _ in range(num_layers)
        ])

        # Pila de bloques decoder
        self.decoder_layers = nn.ModuleList([
            TransformerDecoderBlock(d_model, num_heads, d_ff, dropout)
            for _ in range(num_layers)
        ])

        # Normalizaciones finales
        self.encoder_norm = nn.LayerNorm(d_model)
        self.decoder_norm = nn.LayerNorm(d_model)

        # Capa de salida: proyección al vocabulario objetivo
        self.output_projection = nn.Linear(d_model, tgt_vocab_size)

    def encode(self, src: torch.Tensor, src_mask: torch.Tensor = None) -> torch.Tensor:
        """Procesa la secuencia fuente a través del encoder."""
        x = self.src_embedding(src) * math.sqrt(self.d_model)
        x = self.positional_encoding(x)
        for layer in self.encoder_layers:
            x = layer(x, src_mask)
        return self.encoder_norm(x)

    def decode(
        self, tgt: torch.Tensor, encoder_output: torch.Tensor,
        src_mask: torch.Tensor = None, tgt_mask: torch.Tensor = None
    ) -> torch.Tensor:
        """Procesa la secuencia objetivo a través del decoder."""
        x = self.tgt_embedding(tgt) * math.sqrt(self.d_model)
        x = self.positional_encoding(x)
        for layer in self.decoder_layers:
            x = layer(x, encoder_output, src_mask, tgt_mask)
        return self.decoder_norm(x)

    def forward(
        self, src: torch.Tensor, tgt: torch.Tensor,
        src_mask: torch.Tensor = None, tgt_mask: torch.Tensor = None
    ) -> torch.Tensor:
        """
        Forward pass completo del Transformer.
        Args:
            src: Tokens fuente [batch, src_len]
            tgt: Tokens objetivo [batch, tgt_len]
            src_mask: Máscara de padding para la fuente
            tgt_mask: Máscara causal para el objetivo
        Returns:
            Logits sobre el vocabulario [batch, tgt_len, tgt_vocab_size]
        """
        # 1. Codificar la secuencia fuente
        encoder_output = self.encode(src, src_mask)

        # 2. Decodificar la secuencia objetivo con contexto del encoder
        decoder_output = self.decode(tgt, encoder_output, src_mask, tgt_mask)

        # 3. Proyectar al espacio del vocabulario
        logits = self.output_projection(decoder_output)

        return logits
```

Este código define un modelo Transformer completo que puede instanciarse con los hiperparámetros del modelo base original:

```python
# Instanciar modelo con hiperparámetros del Transformer base
model = Transformer(
    src_vocab_size=32000,   # Vocabulario fuente
    tgt_vocab_size=32000,   # Vocabulario objetivo
    d_model=512,            # Dimensión del modelo
    num_heads=8,            # Número de cabezas de atención
    num_layers=6,           # Número de capas (encoder y decoder)
    d_ff=2048,              # Dimensión de la FFN
    dropout=0.1             # Probabilidad de dropout
)

# Verificar número de parámetros
total_params = sum(p.numel() for p in model.parameters())
print(f"Parámetros totales: {total_params:,}")
```

---

## 6.9 Ejemplo: Transformer para traducción

### 6.9.1 Descripción conceptual del proceso

Para ilustrar el funcionamiento del Transformer de manera concreta, consideremos el ejemplo de traducir la oración del inglés al español:

- **Oración fuente (inglés):** "The cat sits on the mat"
- **Oración objetivo (español):** "El gato se sienta en la alfombra"

Veamos paso a paso cómo el Transformer procesa esta tarea.

### 6.9.2 Procesamiento en el encoder

**Paso 1: Tokenización.** La oración fuente se tokeniza (posiblemente usando subpalabras como BPE o SentencePiece) y se convierte en una secuencia de índices enteros:

$$\text{src} = [102, \ 3847, \ 9215, \ 87, \ 102, \ 5631]$$

donde cada número corresponde al índice del token en el vocabulario fuente. La secuencia tiene longitud $T_s = 6$.

**Paso 2: Embedding y codificación posicional.** Cada índice se convierte en un vector de dimensión $d_{model} = 512$, se escala por $\sqrt{512} \approx 22.63$, y se le suma su codificación posicional correspondiente:

$$\mathbf{z}_t^{(0)} = \sqrt{512} \cdot \text{Embed}(x_t) + \mathbf{PE}_t, \quad t = 1, \ldots, 6$$

El resultado es una matriz $\mathbf{Z}^{(0)} \in \mathbb{R}^{6 \times 512}$, donde cada fila es la representación inicial de un token con su información posicional.

**Paso 3: Pila de bloques encoder.** La matriz $\mathbf{Z}^{(0)}$ pasa secuencialmente por los $N = 6$ bloques encoder. En cada bloque:

- **Self-Attention Multi-Cabezal ($h = 8$):** Cada token "atiende" a todos los demás tokens. Por ejemplo, al procesar "sits", el mecanismo de atención podría asignar pesos altos a "cat" (su sujeto) y "mat" (su complemento), capturando las dependencias sintácticas y semánticas.

  Con 8 cabezas de atención, el modelo puede capturar simultáneamente diferentes tipos de relaciones:
  - Una cabeza podría capturar relaciones sujeto-verbo ("cat" → "sits").
  - Otra podría capturar relaciones de posición espacial ("on" → "mat").
  - Otra podría capturar la estructura del artículo definido ("the" → "cat", "the" → "mat").

- **Add & Norm:** La salida de la atención se suma con la entrada (conexión residual) y se normaliza.

- **FFN:** Se aplica la red feed-forward $\text{FFN}(\mathbf{x}) = \max(0, \mathbf{x}\mathbf{W}_1 + \mathbf{b}_1)\mathbf{W}_2 + \mathbf{b}_2$ de manera independiente a cada posición, refinando las representaciones.

- **Add & Norm:** Otra conexión residual y normalización.

Después de 6 bloques, la salida final del encoder es $\mathbf{Z}^{(6)} \in \mathbb{R}^{6 \times 512}$, donde cada vector de 512 dimensiones contiene una representación rica y contextualizada de cada token de la oración fuente. Crucialmente, la representación de "cat" en $\mathbf{Z}^{(6)}$ no solo codifica la semántica de la palabra "cat", sino también su papel como sujeto de "sits", su relación con "the", y su contexto dentro de toda la oración.

### 6.9.3 Generación en el decoder (inferencia)

Durante la inferencia, el decoder genera la traducción token por token de manera autoregresiva. Veamos el proceso:

**Paso 0: Inicio.** La entrada inicial al decoder es el token de inicio: $\text{tgt} = [\langle \text{SOS} \rangle]$.

**Paso 1: Generar "El".**
1. El token $\langle \text{SOS} \rangle$ se convierte en embedding y se suma su codificación posicional.
2. Pasa por los bloques decoder:
   - **Masked Self-Attention:** Solo hay un token, así que la atención es trivial.
   - **Cross-Attention:** El token $\langle \text{SOS} \rangle$ del decoder (como consulta $\mathbf{Q}$) atiende a la representación del encoder $\mathbf{Z}^{(6)}$ (como claves $\mathbf{K}$ y valores $\mathbf{V}$). El modelo aprende a enfocarse en "The" como la fuente más relevante para generar el primer token de la traducción.
   - **FFN:** Refina la representación.
3. La capa de salida produce un vector de logits sobre el vocabulario español.
4. Se aplica softmax y se selecciona el token con mayor probabilidad: "El".

$\text{tgt} = [\langle \text{SOS} \rangle, \ \text{El}]$

**Paso 2: Generar "gato".**
1. Ahora la entrada al decoder es $[\langle \text{SOS} \rangle, \ \text{El}]$.
2. En la masked self-attention, "El" puede atender a $\langle \text{SOS} \rangle$ y a sí mismo, pero la máscara causal impide que $\langle \text{SOS} \rangle$ atienda a "El".
3. En la cross-attention, las representaciones del decoder atienden al encoder. El modelo debería enfocarse principalmente en "cat" para generar la traducción correspondiente.
4. Se genera "gato".

$\text{tgt} = [\langle \text{SOS} \rangle, \ \text{El}, \ \text{gato}]$

**Paso 3: Generar "se".**
1. Entrada: $[\langle \text{SOS} \rangle, \ \text{El}, \ \text{gato}]$.
2. La self-attention enmascarada permite que "se" atienda a los tres tokens anteriores.
3. La cross-attention se enfoca en "sits" y su contexto.
4. Se genera "se".

Este proceso continúa token por token: "sienta" → "en" → "la" → "alfombra" → $\langle \text{EOS} \rangle$.

**Paso final:** Cuando el modelo genera el token especial de fin de secuencia $\langle \text{EOS} \rangle$, la generación se detiene. La traducción completa es:

$$\text{Salida} = [\text{El}, \ \text{gato}, \ \text{se}, \ \text{sienta}, \ \text{en}, \ \text{la}, \ \text{alfombra}]$$

### 6.9.4 Diferencia entre entrenamiento e inferencia

Es fundamental entender la diferencia entre el modo de entrenamiento y el modo de inferencia del decoder:

- **Entrenamiento (*teacher forcing*):** La entrada completa al decoder es la secuencia objetivo desplazada: $[\langle \text{SOS} \rangle, \text{El}, \text{gato}, \text{se}, \text{sienta}, \text{en}, \text{la}, \text{alfombra}]$. Todos los tokens se procesan en paralelo (la máscara causal previene la fuga de información), y la pérdida se calcula simultáneamente para todas las posiciones. Esto es eficiente porque permite el procesamiento en paralelo de la secuencia completa.

- **Inferencia (*autoregresiva*):** El decoder genera un token a la vez. En cada paso, la secuencia de entrada crece en un token, y todo el bloque decoder debe re-ejecutarse. Esto es inherentemente secuencial y más lento que el entrenamiento. Para mejorar la eficiencia, se utiliza *KV-caching*: las claves y valores calculados para posiciones anteriores se almacenan en caché y se reutilizan, evitando recalcularlos en cada paso.

### 6.9.5 Relevancia para comunicaciones semánticas

El ejemplo de traducción ilustra perfectamente la analogía con las comunicaciones semánticas. En un sistema de comunicación semántica basado en Transformer:

- El **encoder semántico** (análogo al encoder del Transformer) extrae representaciones semánticas ricas de la fuente de información (texto, imagen, audio).
- La **transmisión por el canal** corresponde al paso de la representación codificada a través de un medio con ruido e interferencia.
- El **decoder semántico** (análogo al decoder del Transformer) reconstruye o interpreta el mensaje a partir de las representaciones recibidas, utilizando atención cruzada para alinear las representaciones del transmisor con la generación del receptor.

La capacidad del Transformer para capturar dependencias globales, procesar secuencias en paralelo y aprender representaciones contextualizadas ricas lo convierte en la arquitectura ideal para los sistemas de comunicación semántica modernos, donde la eficiencia y la fidelidad semántica son primordiales.

---

### Resumen de la Sección 6

En esta sección hemos estudiado en profundidad la arquitectura Transformer, cubriendo:

1. **Motivación:** Las limitaciones de las RNN (secuencialidad, dependencias de largo alcance) que motivaron la creación del Transformer.
2. **Codificación posicional:** Las funciones sinusoidales que inyectan información de posición, con la propiedad clave de que las posiciones relativas pueden representarse como transformaciones lineales.
3. **Encoder:** Multi-Head Self-Attention + Add & Norm + FFN + Add & Norm, apilados $N$ veces.
4. **Decoder:** Masked Self-Attention + Cross-Attention + FFN, con conexiones residuales y normalización.
5. **Arquitectura completa:** El pipeline encoder-decoder con capa de salida softmax.
6. **Entrenamiento:** Teacher forcing, label smoothing, warm-up de tasa de aprendizaje, y entropía cruzada.
7. **Variantes:** BERT (encoder), GPT (decoder), T5 (encoder-decoder), ViT (visión).
8. **Implementación:** Código PyTorch completo y comentado.
9. **Ejemplo práctico:** Traducción paso a paso mostrando el flujo de información.

En la siguiente sección, exploraremos cómo estas ideas se aplican específicamente al diseño de sistemas de comunicación semántica, donde el Transformer sirve como la columna vertebral para la extracción, transmisión y reconstrucción de significado.
