# 3. Redes Neuronales Convolucionales (CNN)

Las redes neuronales convolucionales (CNN, por sus siglas en inglés, *Convolutional Neural Networks*) constituyen una de las arquitecturas más influyentes y exitosas del aprendizaje profundo. Originalmente diseñadas para el procesamiento de imágenes, las CNN han demostrado una versatilidad extraordinaria que se extiende a dominios tan diversos como el procesamiento de señales de radiofrecuencia, el análisis de series temporales y, de manera particularmente relevante para este tutorial, las comunicaciones semánticas. En esta sección, desarrollaremos los fundamentos matemáticos de la convolución, describiremos cada componente de una CNN y exploraremos sus aplicaciones directas en sistemas de telecomunicaciones, incluyendo la clasificación automática de modulación y la detección de anomalías en señales.

---

## 3.1 Motivación y concepto de convolución

### 3.1.1 La explosión de parámetros en redes totalmente conectadas

En las secciones anteriores se presentaron las redes neuronales densas (*fully connected*), donde cada neurona de una capa está conectada a todas las neuronas de la capa anterior. Aunque este enfoque es conceptualmente simple y universal en su capacidad de aproximación, presenta una limitación práctica severa cuando se aplica a datos de alta dimensionalidad, como las imágenes.

Consideremos una imagen en escala de grises de tamaño modesto, por ejemplo $256 \times 256$ píxeles. Esta imagen, al ser representada como un vector de entrada para una red densa, tiene $256 \times 256 = 65{,}536$ componentes. Si la primera capa oculta contiene tan solo 1,000 neuronas, el número de pesos entre la capa de entrada y esta primera capa oculta sería:

$$W = 65{,}536 \times 1{,}000 = 65{,}536{,}000 \text{ parámetros}$$

Para una imagen a color de dimensiones $224 \times 224 \times 3$ (tres canales RGB), como las que se utilizan comúnmente en visión por computadora, el número de entradas asciende a $224 \times 224 \times 3 = 150{,}528$, lo que produce más de 150 millones de parámetros solo en la primera capa. Esta explosión combinatoria genera múltiples problemas:

1. **Sobreajuste (*overfitting*):** Con tantos parámetros libres, el modelo tiende a memorizar los datos de entrenamiento en lugar de aprender patrones generalizables, especialmente cuando el conjunto de datos no es extremadamente grande.

2. **Costo computacional prohibitivo:** El almacenamiento y la actualización de millones de parámetros demandan cantidades enormes de memoria y tiempo de cómputo, haciendo el entrenamiento impracticable para imágenes de resolución moderada o alta.

3. **Ignorancia de la estructura espacial:** Una red densa trata cada píxel como una variable independiente. No incorpora la noción fundamental de que los píxeles cercanos entre sí tienden a estar altamente correlacionados, ni que los patrones visuales (bordes, texturas, formas) son locales y pueden aparecer en cualquier posición de la imagen.

Estas limitaciones motivaron la búsqueda de una arquitectura que pudiera explotar la estructura inherente de los datos espaciales. La respuesta se encontró en la operación matemática de convolución, una herramienta fundamental del análisis funcional y el procesamiento de señales, que fue adaptada al contexto de las redes neuronales de manera pionera por Yann LeCun y colaboradores en la década de 1990.

### 3.1.2 Definición matemática de la convolución continua

La convolución es una operación matemática que combina dos funciones para producir una tercera función que expresa cómo la forma de una modifica a la otra. En el dominio continuo, la convolución de dos funciones $f$ y $g$ se define como:

$$(f * g)(t) = \int_{-\infty}^{\infty} f(\tau) \, g(t - \tau) \, d\tau$$

donde $\tau$ es la variable de integración y $t$ es la variable de la función resultante. Esta operación tiene una interpretación intuitiva y profunda: se invierte una de las funciones (reflexión temporal), se desplaza a lo largo del eje temporal, y en cada posición de desplazamiento se computa el producto interno (integral del producto punto a punto) entre las dos funciones.

La convolución satisface varias propiedades algebraicas fundamentales que la hacen particularmente útil tanto en matemáticas puras como en ingeniería:

- **Conmutatividad:** $(f * g)(t) = (g * f)(t)$. Esto significa que el orden de las funciones no altera el resultado.
- **Asociatividad:** $(f * (g * h))(t) = ((f * g) * h)(t)$. Esto permite encadenar múltiples convoluciones de manera flexible.
- **Distributividad:** $f * (g + h) = (f * g) + (f * h)$. La convolución se distribuye sobre la suma.
- **Teorema de convolución:** En el dominio de Fourier, la convolución se transforma en multiplicación punto a punto: $\mathcal{F}\{f * g\} = \mathcal{F}\{f\} \cdot \mathcal{F}\{g\}$. Esta propiedad es la base del procesamiento eficiente de señales y establece un puente directo con los sistemas de telecomunicaciones.

En el contexto de las telecomunicaciones, la convolución aparece de manera natural en múltiples escenarios: cuando una señal pasa a través de un canal de comunicación (la señal recibida es la convolución de la señal transmitida con la respuesta al impulso del canal), en el diseño de filtros (un filtro lineal e invariante en el tiempo opera mediante convolución), y en la ecualización de canal.

### 3.1.3 La convolución discreta

En el procesamiento digital de señales y, por extensión, en las redes neuronales, trabajamos con datos discretos (muestras). La versión discreta de la convolución se define como:

$$(f * g)[n] = \sum_{k=-\infty}^{\infty} f[k] \, g[n - k]$$

donde $f$ y $g$ son secuencias discretas y $n$ es el índice de la secuencia resultante. En la práctica, las secuencias tienen soporte finito, por lo que la suma se realiza sobre un número finito de términos:

$$(f * g)[n] = \sum_{k=0}^{K-1} f[k] \, g[n - k]$$

donde $K$ es la longitud del filtro (o *kernel*). Cada valor de la señal de salida se calcula como una suma ponderada de valores vecinos de la señal de entrada, donde los pesos están determinados por el filtro $g$.

Consideremos un ejemplo concreto. Sea $f = [1, 3, 5, 2, 4]$ una señal de entrada y $g = [1, 0, -1]$ un filtro de tamaño $K=3$. Para calcular la salida en el índice $n=1$:

$$(f * g)[1] = f[0] \cdot g[1] + f[1] \cdot g[0] + f[2] \cdot g[-1]$$

En la práctica de las redes neuronales, se utiliza una operación ligeramente diferente llamada correlación cruzada (*cross-correlation*), que omite la reflexión del kernel:

$$(f \star g)[n] = \sum_{k=0}^{K-1} f[n + k] \, g[k]$$

Aunque matemáticamente la convolución y la correlación cruzada difieren en la reflexión del kernel, en el contexto de las redes neuronales esta distinción es irrelevante, ya que los pesos del kernel se aprenden durante el entrenamiento. Si el kernel óptimo para la convolución es $[a, b, c]$, el kernel óptimo aprendido para la correlación cruzada sería simplemente $[c, b, a]$. Por convención, en la comunidad de aprendizaje profundo se utiliza el término "convolución" para referirse a la operación de correlación cruzada.

### 3.1.4 Principios fundamentales: campos receptivos locales, compartición de pesos e invarianza a traslaciones

Las CNN incorporan tres principios arquitectónicos fundamentales que abordan directamente las limitaciones de las redes densas:

**Campos receptivos locales (*local receptive fields*).** En lugar de conectar cada neurona de salida a todos los píxeles de la imagen de entrada, cada neurona se conecta únicamente a una región pequeña y localizada de la entrada, denominada *campo receptivo*. Si el kernel tiene un tamaño de $k \times k$, cada neurona de salida depende solo de $k^2$ valores de entrada, en contraste con los $n^2$ valores que requeriría una conexión densa para una imagen de $n \times n$. Este enfoque se alinea con el conocimiento neurobiológico de la corteza visual, donde las neuronas individuales responden a estímulos en regiones específicas del campo visual, no a la totalidad de la escena.

**Compartición de pesos (*weight sharing*).** El mismo conjunto de pesos (el kernel o filtro) se aplica a todas las posiciones de la imagen de entrada. Esto significa que un detector de bordes verticales, por ejemplo, utiliza exactamente los mismos pesos sin importar si está analizando la esquina superior izquierda o el centro de la imagen. Este principio reduce drásticamente el número de parámetros: en lugar de tener un conjunto de pesos diferente para cada posición espacial, un solo kernel de $k \times k$ se reutiliza en toda la imagen. Para una imagen de $n \times n$ con un kernel de $k \times k$, el número de parámetros por filtro es simplemente $k^2$ (más un sesgo), independientemente del tamaño de la imagen.

**Invarianza a traslaciones (*translation equivariance*).** Como consecuencia directa de la compartición de pesos, las CNN son equivariantes a traslaciones. Si un patrón (por ejemplo, un gato) aparece en una posición diferente de la imagen, la representación aprendida en las capas convolucionales se desplaza correspondientemente, pero mantiene la misma activación. Formalmente, si $T_{\mathbf{d}}$ denota un operador de traslación por un vector $\mathbf{d}$, entonces:

$$\text{Conv}(T_{\mathbf{d}}(\mathbf{X})) = T_{\mathbf{d}}(\text{Conv}(\mathbf{X}))$$

Es importante distinguir entre *equivarianza* e *invarianza*: la convolución es equivariante (la salida se desplaza con la entrada), mientras que la invarianza completa (la salida no cambia ante traslaciones) se logra posteriormente mediante las capas de pooling o las capas densas finales.

Estos tres principios trabajan en conjunto para crear una arquitectura que es simultáneamente eficiente en parámetros, capaz de detectar patrones locales relevantes y robusta ante cambios de posición de los objetos de interés.

**Figura 3.1:** *Visualización de la operación de convolución 2D. Se muestra una imagen de entrada de dimensiones $5 \times 5$ (representada como una matriz de valores de intensidad de píxel) y un kernel (filtro) de tamaño $3 \times 3$. El kernel se desliza sobre la imagen de izquierda a derecha y de arriba a abajo, con un paso (stride) de 1. En cada posición, se calcula el producto punto entre los valores del kernel y la región correspondiente de la imagen (el campo receptivo local), y el resultado escalar se coloca en la posición correspondiente de la matriz de salida (mapa de características). Se destacan tres posiciones del kernel: (a) esquina superior izquierda, produciendo el primer elemento de la salida; (b) una posición intermedia; y (c) la esquina inferior derecha, produciendo el último elemento. Las flechas indican la dirección del deslizamiento. La matriz de salida resultante tiene dimensiones $3 \times 3$ (calculada según la fórmula de tamaño de salida sin relleno). Los colores resaltan qué píxeles de la entrada contribuyen a cada valor de la salida.*

---

## 3.2 Capas convolucionales

### 3.2.1 Convolución 2D para imágenes

La capa convolucional es el componente fundamental de las CNN. Formalmente, la convolución 2D discreta (en realidad, correlación cruzada, como se discutió anteriormente) entre una imagen de entrada $\mathbf{X}$ y un kernel $\mathbf{K}$ de tamaño $k_h \times k_w$ produce un mapa de características (*feature map*) $\mathbf{Y}$ definido por:

$$\mathbf{Y}[i, j] = (\mathbf{X} * \mathbf{K})[i, j] = \sum_{m=0}^{k_h - 1} \sum_{n=0}^{k_w - 1} \mathbf{X}[i + m, \, j + n] \cdot \mathbf{K}[m, n]$$

donde $(i, j)$ indica la posición espacial en el mapa de salida, y $(m, n)$ recorre las posiciones del kernel. Además de los pesos del kernel, cada filtro convolucional incluye un término de sesgo (*bias*) $b$, y la salida completa de una neurona convolucional se pasa típicamente por una función de activación no lineal $\sigma$ (como ReLU):

$$\mathbf{Y}[i, j] = \sigma\left( \sum_{m=0}^{k_h - 1} \sum_{n=0}^{k_w - 1} \mathbf{X}[i + m, \, j + n] \cdot \mathbf{K}[m, n] + b \right)$$

Cuando la entrada tiene múltiples canales (por ejemplo, una imagen RGB con 3 canales, o un mapa de características de una capa anterior con $C_{in}$ canales), el kernel se extiende a tres dimensiones ($C_{in} \times k_h \times k_w$), y la convolución se realiza como:

$$\mathbf{Y}[i, j] = \sigma\left( \sum_{c=0}^{C_{in}-1} \sum_{m=0}^{k_h - 1} \sum_{n=0}^{k_w - 1} \mathbf{X}[c, \, i + m, \, j + n] \cdot \mathbf{K}[c, \, m, n] + b \right)$$

Aquí, el kernel realiza la convolución en cada canal de manera independiente y luego suma los resultados, produciendo un único mapa de características escalar 2D como salida. Para obtener múltiples mapas de características (cada uno detectando un patrón diferente), se utilizan múltiples kernels, lo que nos lleva al concepto de filtros múltiples.

### 3.2.2 Parámetros de la convolución: tamaño del kernel, stride y padding

La operación de convolución se configura mediante tres hiperparámetros fundamentales que determinan tanto el comportamiento como las dimensiones de la salida:

**Tamaño del kernel (*kernel size*), $k$.** El tamaño del kernel define la extensión del campo receptivo local. Los tamaños más comunes en la práctica son $3 \times 3$, $5 \times 5$ y $7 \times 7$. Kernels más pequeños capturan patrones más finos y locales (bordes, esquinas), mientras que kernels más grandes pueden detectar patrones más extensos, pero a costa de un mayor número de parámetros ($k^2$ por canal). La arquitectura VGGNet demostró que apilar múltiples capas con kernels $3 \times 3$ es preferible a usar un solo kernel grande, ya que dos capas de $3 \times 3$ tienen un campo receptivo efectivo de $5 \times 5$ pero con menos parámetros ($2 \times 3^2 = 18$ versus $5^2 = 25$) y mayor capacidad de representación no lineal (al intercalar funciones de activación).

**Paso (*stride*), $s$.** El stride define cuántas posiciones se desplaza el kernel en cada paso. Un stride de $s = 1$ significa que el kernel se mueve un píxel a la vez, produciendo un mapa de salida de dimensiones cercanas a las de la entrada. Un stride de $s = 2$ reduce las dimensiones espaciales aproximadamente a la mitad, ya que el kernel salta de dos en dos posiciones. Un stride mayor reduce la resolución espacial pero aumenta el campo receptivo efectivo de capas posteriores y reduce el costo computacional.

**Relleno (*padding*), $p$.** El padding consiste en agregar filas y columnas de valores (típicamente ceros) alrededor del borde de la imagen de entrada antes de aplicar la convolución. Existen dos modos principales:

- ***Valid padding*** ($p = 0$): No se agrega relleno. La convolución solo se aplica donde el kernel cabe completamente dentro de la entrada. Esto reduce las dimensiones de salida.
- ***Same padding*** ($p = \lfloor k/2 \rfloor$ para stride $s=1$): Se agrega suficiente relleno para que la salida tenga las mismas dimensiones espaciales que la entrada. Para un kernel de $3 \times 3$, esto requiere $p = 1$; para un kernel de $5 \times 5$, $p = 2$.

### 3.2.3 Fórmula del tamaño de salida

Dados los hiperparámetros anteriores, el tamaño de la salida se calcula mediante la siguiente fórmula:

$$o = \left\lfloor \frac{n + 2p - k}{s} \right\rfloor + 1$$

donde:
- $o$ es la dimensión de salida (ancho o alto del mapa de características),
- $n$ es la dimensión de entrada correspondiente,
- $p$ es el padding,
- $k$ es el tamaño del kernel en esa dimensión,
- $s$ es el stride,
- $\lfloor \cdot \rfloor$ denota la función piso (redondeo hacia abajo al entero más cercano).

Verifiquemos con algunos casos concretos:

- **Entrada $n=32$, kernel $k=5$, stride $s=1$, padding $p=0$:** $o = \lfloor (32 + 0 - 5)/1 \rfloor + 1 = 27 + 1 = 28$.
- **Entrada $n=32$, kernel $k=5$, stride $s=1$, padding $p=2$ (same):** $o = \lfloor (32 + 4 - 5)/1 \rfloor + 1 = 31 + 1 = 32$. La salida mantiene el mismo tamaño.
- **Entrada $n=32$, kernel $k=3$, stride $s=2$, padding $p=1$:** $o = \lfloor (32 + 2 - 3)/2 \rfloor + 1 = \lfloor 31/2 \rfloor + 1 = 15 + 1 = 16$. La dimensión se reduce a la mitad.

Esta fórmula se aplica independientemente a cada dimensión espacial (alto y ancho), permitiendo el uso de kernels rectangulares y strides asimétricos cuando sea necesario.

### 3.2.4 Mapas de características y filtros múltiples

Una sola operación de convolución con un kernel produce un único mapa de características 2D. Sin embargo, una capa convolucional típica contiene múltiples filtros (kernels), cada uno aprendiendo a detectar un patrón diferente. Si la capa tiene $C_{out}$ filtros, la salida será un tensor tridimensional de dimensiones $C_{out} \times o_h \times o_w$, donde $o_h$ y $o_w$ son las dimensiones espaciales de salida.

El número total de parámetros aprendibles en una capa convolucional es:

$$\text{Parámetros} = C_{out} \times (C_{in} \times k_h \times k_w + 1)$$

donde el $+1$ corresponde al sesgo de cada filtro. Por ejemplo, una capa convolucional con entrada de 3 canales (RGB), 64 filtros de tamaño $3 \times 3$ tiene:

$$\text{Parámetros} = 64 \times (3 \times 3 \times 3 + 1) = 64 \times 28 = 1{,}792$$

Comparemos esto con una capa densa equivalente. Si la entrada es una imagen de $224 \times 224 \times 3$ y la salida tiene $224 \times 224 \times 64$ unidades, la capa densa requeriría $150{,}528 \times 3{,}211{,}264 \approx 4.83 \times 10^{11}$ parámetros, un número absurdamente grande. La convolución con compartición de pesos reduce esto a menos de dos mil parámetros, una reducción de ocho órdenes de magnitud.

En las primeras capas de la red, los filtros aprenden a detectar características de bajo nivel como bordes horizontales, verticales, diagonales y gradientes de color. En capas intermedias, los filtros combinan estas características básicas para detectar texturas, esquinas y partes de objetos. En las capas más profundas, los filtros responden a patrones de alto nivel como rostros, ruedas o texto, construyendo una jerarquía de representaciones cada vez más abstractas.

### 3.2.5 Ejemplo numérico: detección de bordes con un filtro 3×3

Para consolidar la comprensión de la operación de convolución, desarrollaremos un ejemplo completo paso a paso. Consideremos una imagen de entrada en escala de grises de tamaño $5 \times 5$:

$$\mathbf{X} = \begin{bmatrix} 10 & 10 & 10 & 0 & 0 \\ 10 & 10 & 10 & 0 & 0 \\ 10 & 10 & 10 & 0 & 0 \\ 10 & 10 & 10 & 0 & 0 \\ 10 & 10 & 10 & 0 & 0 \end{bmatrix}$$

Esta imagen simula una transición vertical (borde) entre una región clara (valor 10) a la izquierda y una región oscura (valor 0) a la derecha. Aplicaremos un filtro Sobel vertical para la detección de bordes:

$$\mathbf{K} = \begin{bmatrix} -1 & 0 & 1 \\ -2 & 0 & 2 \\ -1 & 0 & 1 \end{bmatrix}$$

Utilizaremos *valid padding* ($p = 0$) y stride $s = 1$. La dimensión de salida será:

$$o = \left\lfloor \frac{5 + 0 - 3}{1} \right\rfloor + 1 = 3$$

Por lo tanto, el mapa de características de salida tendrá dimensiones $3 \times 3$. Calculemos cada elemento:

**Posición $(0, 0)$:** El kernel se superpone con la submatriz de $\mathbf{X}$ que comprende las filas 0–2 y columnas 0–2:

$$\mathbf{Y}[0,0] = \sum_{m=0}^{2}\sum_{n=0}^{2} \mathbf{X}[m, n] \cdot \mathbf{K}[m, n]$$

$$= 10 \cdot (-1) + 10 \cdot 0 + 10 \cdot 1 + 10 \cdot (-2) + 10 \cdot 0 + 10 \cdot 2 + 10 \cdot (-1) + 10 \cdot 0 + 10 \cdot 1$$

$$= -10 + 0 + 10 - 20 + 0 + 20 - 10 + 0 + 10 = 0$$

No se detecta borde porque la región cubierta es completamente uniforme (todo valor 10).

**Posición $(0, 1)$:** El kernel cubre las columnas 1–3:

$$\mathbf{Y}[0,1] = 10 \cdot (-1) + 10 \cdot 0 + 0 \cdot 1 + 10 \cdot (-2) + 10 \cdot 0 + 0 \cdot 2 + 10 \cdot (-1) + 10 \cdot 0 + 0 \cdot 1$$

$$= -10 + 0 + 0 - 20 + 0 + 0 - 10 + 0 + 0 = -40$$

El valor negativo grande indica la presencia de un borde vertical con transición de claro a oscuro.

**Posición $(0, 2)$:** El kernel cubre las columnas 2–4:

$$\mathbf{Y}[0,2] = 10 \cdot (-1) + 0 \cdot 0 + 0 \cdot 1 + 10 \cdot (-2) + 0 \cdot 0 + 0 \cdot 2 + 10 \cdot (-1) + 0 \cdot 0 + 0 \cdot 1$$

$$= -10 + 0 + 0 - 20 + 0 + 0 - 10 + 0 + 0 = -40$$

Nuevamente se detecta el borde. Podemos observar que, por la simetría de la imagen (el borde vertical se extiende a lo largo de toda la altura), las posiciones con los mismos índices de columna producen los mismos valores independientemente de la fila. Continuando el cálculo para las filas restantes:

**Posición $(1, 0)$:** Filas 1–3, columnas 0–2: $\mathbf{Y}[1,0] = 0$ (región uniforme).

**Posición $(1, 1)$:** Filas 1–3, columnas 1–3: $\mathbf{Y}[1,1] = -40$.

**Posición $(1, 2)$:** Filas 1–3, columnas 2–4: $\mathbf{Y}[1,2] = -40$.

**Posición $(2, 0)$:** Filas 2–4, columnas 0–2: $\mathbf{Y}[2,0] = 0$.

**Posición $(2, 1)$:** Filas 2–4, columnas 1–3: $\mathbf{Y}[2,1] = -40$.

**Posición $(2, 2)$:** Filas 2–4, columnas 2–4: $\mathbf{Y}[2,2] = -40$.

El mapa de características resultante es:

$$\mathbf{Y} = \begin{bmatrix} 0 & -40 & -40 \\ 0 & -40 & -40 \\ 0 & -40 & -40 \end{bmatrix}$$

Este resultado es extremadamente informativo. La primera columna tiene valores cero, indicando que no hay borde en esa posición. Las columnas segunda y tercera tienen valores negativos grandes ($-40$), indicando la presencia de un borde vertical fuerte. El signo negativo indica la dirección de la transición (de claro a oscuro de izquierda a derecha); si la transición fuera en sentido contrario, los valores serían positivos ($+40$). La magnitud absoluta ($40$) refleja la intensidad del contraste.

Este ejemplo ilustra cómo un único filtro, con solo 9 parámetros fijos, puede detectar un tipo específico de patrón en cualquier posición de la imagen. En una CNN, estos parámetros no se fijan manualmente sino que se aprenden automáticamente durante el entrenamiento, permitiendo a la red descubrir los patrones más relevantes para la tarea.

**Figura 3.1b:** *Ejemplo numérico de convolución paso a paso. A la izquierda se muestra la imagen de entrada $\mathbf{X}$ de $5 \times 5$ con una región clara (valor 10) en las tres primeras columnas y una región oscura (valor 0) en las dos últimas. En el centro se presenta el kernel Sobel vertical $\mathbf{K}$ de $3 \times 3$. A la derecha se muestra el mapa de características resultante $\mathbf{Y}$ de $3 \times 3$. Las flechas conectan cada posición del kernel sobre la imagen con el valor correspondiente de la salida. Se resaltan tres pasos: (a) posición $(0,0)$ donde el kernel cubre una región uniforme, produciendo salida $0$; (b) posición $(0,1)$ donde el kernel cruza el borde vertical, produciendo salida $-40$; (c) posición $(0,2)$ donde el kernel cubre otra región del borde, produciendo $-40$. La columna de ceros en la salida indica ausencia de borde; las columnas con valores $-40$ marcan la ubicación del borde vertical detectado.*

---

## 3.3 Capas de Pooling

### 3.3.1 Max Pooling

Las capas de pooling (o submuestreo) son componentes esenciales de las CNN que reducen progresivamente la resolución espacial de los mapas de características. La operación de Max Pooling selecciona el valor máximo dentro de una ventana deslizante de tamaño fijo. Formalmente, dado un mapa de características $\mathbf{Y}$ y una ventana de pooling de tamaño $p_h \times p_w$ con stride $s$, la salida del Max Pooling es:

$$\mathbf{Z}[i, j] = \max_{0 \leq m < p_h, \, 0 \leq n < p_w} \mathbf{Y}[i \cdot s + m, \, j \cdot s + n]$$

La configuración más común es una ventana de $2 \times 2$ con stride $s = 2$, lo que reduce cada dimensión espacial exactamente a la mitad. Por ejemplo, un mapa de características de $32 \times 32$ se convierte en uno de $16 \times 16$ después del Max Pooling.

El Max Pooling preserva las activaciones más fuertes (los valores más altos) dentro de cada vecindario, lo que tiene una interpretación intuitiva: si un detector de bordes produce una activación fuerte en algún lugar dentro de una región de $2 \times 2$ píxeles, el Max Pooling retiene esa detección independientemente de la posición exacta dentro de la ventana. Esto confiere a la red una cierta *invarianza a pequeñas traslaciones*, complementando la equivarianza proporcionada por las capas convolucionales.

### 3.3.2 Average Pooling

El Average Pooling calcula el promedio de los valores dentro de la ventana deslizante:

$$\mathbf{Z}[i, j] = \frac{1}{p_h \times p_w} \sum_{m=0}^{p_h - 1} \sum_{n=0}^{p_w - 1} \mathbf{Y}[i \cdot s + m, \, j \cdot s + n]$$

A diferencia del Max Pooling, que retiene la activación más fuerte, el Average Pooling considera la contribución promedio de todos los valores en la ventana. Esto produce representaciones más suaves y es particularmente útil en las capas finales de la red. Una variante especial es el *Global Average Pooling* (GAP), que calcula el promedio sobre toda la extensión espacial del mapa de características (la ventana es del mismo tamaño que el mapa), reduciendo cada canal a un único valor escalar. El GAP fue introducido por Lin, Chen y Yan (2014, DOI: 10.48550/arXiv.1312.4400) como una alternativa a las capas densas finales, reduciendo significativamente el número de parámetros y el riesgo de sobreajuste.

### 3.3.3 Propósito y ventajas del pooling

Las capas de pooling cumplen múltiples funciones:

1. **Reducción de dimensionalidad.** Al reducir las dimensiones espaciales, el pooling disminuye el número de computaciones y parámetros en las capas subsecuentes. Un Max Pooling $2 \times 2$ con stride 2 reduce el número de activaciones en un factor de 4 (reduce tanto el alto como el ancho a la mitad).

2. **Invarianza a traslaciones locales.** Si una característica (por ejemplo, un borde) se desplaza uno o dos píxeles, su activación máxima dentro de la ventana de pooling permanecerá siendo seleccionada, haciendo que la representación sea robusta ante pequeños desplazamientos.

3. **Aumento del campo receptivo efectivo.** Después del pooling, las capas convolucionales subsecuentes "ven" una porción mayor de la imagen original, ya que cada posición del mapa reducido corresponde a una región más grande de la entrada.

4. **Regularización implícita.** La reducción de resolución actúa como una forma de regularización, previniendo el sobreajuste al descartar información posicional precisa que podría ser ruidosa o irrelevante.

### 3.3.4 Ejemplo numérico de pooling

Consideremos el siguiente mapa de características de $4 \times 4$:

$$\mathbf{Y} = \begin{bmatrix} 1 & 3 & 2 & 4 \\ 5 & 6 & 1 & 2 \\ 7 & 8 & 3 & 0 \\ 2 & 4 & 1 & 5 \end{bmatrix}$$

**Max Pooling con ventana $2 \times 2$ y stride $2$:**

La imagen se divide en cuatro bloques no superpuestos de $2 \times 2$:

- Bloque superior izquierdo: $\begin{bmatrix} 1 & 3 \\ 5 & 6 \end{bmatrix} \rightarrow \max = 6$

- Bloque superior derecho: $\begin{bmatrix} 2 & 4 \\ 1 & 2 \end{bmatrix} \rightarrow \max = 4$

- Bloque inferior izquierdo: $\begin{bmatrix} 7 & 8 \\ 2 & 4 \end{bmatrix} \rightarrow \max = 8$

- Bloque inferior derecho: $\begin{bmatrix} 3 & 0 \\ 1 & 5 \end{bmatrix} \rightarrow \max = 5$

$$\text{MaxPool}(\mathbf{Y}) = \begin{bmatrix} 6 & 4 \\ 8 & 5 \end{bmatrix}$$

**Average Pooling con ventana $2 \times 2$ y stride $2$:**

- Bloque superior izquierdo: $\frac{1 + 3 + 5 + 6}{4} = \frac{15}{4} = 3.75$

- Bloque superior derecho: $\frac{2 + 4 + 1 + 2}{4} = \frac{9}{4} = 2.25$

- Bloque inferior izquierdo: $\frac{7 + 8 + 2 + 4}{4} = \frac{21}{4} = 5.25$

- Bloque inferior derecho: $\frac{3 + 0 + 1 + 5}{4} = \frac{9}{4} = 2.25$

$$\text{AvgPool}(\mathbf{Y}) = \begin{bmatrix} 3.75 & 2.25 \\ 5.25 & 2.25 \end{bmatrix}$$

Observemos cómo el Max Pooling resalta las activaciones dominantes (valor 8 del bloque inferior izquierdo), mientras que el Average Pooling produce valores más moderados que representan la activación promedio de cada región.

---

## 3.4 Arquitectura completa de una CNN

### 3.4.1 Pipeline estándar

Una CNN para clasificación de imágenes sigue típicamente una arquitectura secuencial que combina los componentes descritos en las secciones anteriores. El pipeline estándar se puede expresar como:

$$\text{Input} \rightarrow [\text{Conv} \rightarrow \text{ReLU} \rightarrow \text{Pool}]_{\times N} \rightarrow \text{Flatten} \rightarrow [\text{Dense} \rightarrow \text{ReLU}]_{\times M} \rightarrow \text{Softmax} \rightarrow \text{Output}$$

Cada etapa tiene un propósito específico:

1. **Capas convolucionales (Conv).** Extraen características locales mediante la operación de convolución descrita en la Sección 3.2. Las capas iniciales detectan patrones de bajo nivel (bordes, texturas), mientras que las capas más profundas capturan patrones de alto nivel (partes de objetos, estructuras complejas).

2. **Activación ReLU.** Después de cada convolución, se aplica la función de activación ReLU (*Rectified Linear Unit*), $\text{ReLU}(x) = \max(0, x)$, que introduce no linealidad. Sin estas no linealidades, la composición de múltiples capas convolucionales sería equivalente a una sola convolución lineal, limitando drásticamente la capacidad expresiva de la red.

3. **Capas de Pooling (Pool).** Reducen la dimensionalidad espacial, incrementan el campo receptivo efectivo y proporcionan invarianza a pequeñas traslaciones, como se explicó en la Sección 3.3.

4. **Aplanamiento (Flatten).** Después de las capas convolucionales y de pooling, el tensor tridimensional de mapas de características se "aplana" en un vector unidimensional. Si el tensor final tiene dimensiones $C \times H \times W$, el vector resultante tiene $C \times H \times W$ componentes. Esta operación no tiene parámetros aprendibles; simplemente reorganiza los datos para que puedan ser procesados por capas densas.

5. **Capas densas (*fully connected*).** Combinan las características extraídas por las capas convolucionales para tomar la decisión de clasificación final. Estas capas operan como las redes neuronales densas descritas en la sección anterior del tutorial.

6. **Softmax.** La última capa aplica la función softmax para producir una distribución de probabilidad sobre las $C$ clases:

$$P(y = c \mid \mathbf{x}) = \frac{e^{z_c}}{\sum_{j=1}^{C} e^{z_j}}$$

donde $z_c$ es la salida (*logit*) correspondiente a la clase $c$.

Es importante observar que, a medida que los datos fluyen a través de la red, las dimensiones espaciales se reducen progresivamente (mediante stride y pooling), mientras que el número de canales (filtros) aumenta. Un patrón típico podría ser:

$$[224 \times 224 \times 3] \xrightarrow{\text{Conv}} [224 \times 224 \times 64] \xrightarrow{\text{Pool}} [112 \times 112 \times 64] \xrightarrow{\text{Conv}} [112 \times 112 \times 128] \xrightarrow{\text{Pool}} [56 \times 56 \times 128] \rightarrow \cdots$$

Esta progresión de "alto en espacio, bajo en canales" a "bajo en espacio, alto en canales" refleja una transición de representaciones locales y detalladas a representaciones globales y abstractas.

**Figura 3.2:** *Arquitectura completa de una CNN para clasificación de imágenes. Se muestra el flujo de datos desde la imagen de entrada (por ejemplo, una imagen RGB de $224 \times 224 \times 3$) a través de múltiples bloques convolucionales. Cada bloque consiste en una capa convolucional (representada como un conjunto de mapas de características apilados en profundidad), seguida de una activación ReLU y una capa de Max Pooling que reduce las dimensiones espaciales a la mitad. Se ilustran dos bloques convolucionales: el primero con 32 filtros de $3 \times 3$ produciendo 32 mapas de $112 \times 112$, y el segundo con 64 filtros produciendo 64 mapas de $56 \times 56$. Después de los bloques convolucionales, una operación de aplanamiento (Flatten) convierte el tensor 3D en un vector 1D, que alimenta dos capas densas (fully connected) con activación ReLU. La capa final tiene tantas neuronas como clases y aplica softmax para producir probabilidades de clase. Las flechas indican el flujo de datos, y junto a cada etapa se muestran las dimensiones del tensor. Se observa visualmente cómo las dimensiones espaciales disminuyen mientras el número de canales aumenta a lo largo de la red.*

### 3.4.2 Arquitecturas clásicas

El desarrollo de las CNN ha sido marcado por una serie de arquitecturas innovadoras que establecieron hitos en el campo:

**LeNet-5 (LeCun et al., 1998, DOI: 10.1109/5.726791).** Considerada la primera CNN moderna, fue diseñada para el reconocimiento de dígitos manuscritos (dataset MNIST). Su arquitectura consta de dos capas convolucionales con kernels de $5 \times 5$, cada una seguida de average pooling, y tres capas densas. Aunque modesta para los estándares actuales (aproximadamente 60,000 parámetros), LeNet-5 estableció los principios fundamentales que se mantienen vigentes: campos receptivos locales, compartición de pesos y reducción espacial progresiva.

**AlexNet (Krizhevsky, Sutskever e Hinton, 2012, DOI: 10.1145/3065386).** Esta arquitectura representó el punto de inflexión que catapultó el aprendizaje profundo al centro de la investigación en inteligencia artificial. AlexNet ganó la competición ImageNet Large Scale Visual Recognition Challenge (ILSVRC) 2012 por un margen dramático, reduciendo el error top-5 del 26% al 15.3%. Sus innovaciones clave incluyeron el uso de activación ReLU (en lugar de sigmoid o tanh), dropout para regularización, aumento de datos (*data augmentation*) y entrenamiento paralelo en GPUs. La arquitectura tiene 8 capas (5 convolucionales y 3 densas) con aproximadamente 60 millones de parámetros.

**VGGNet (Simonyan y Zisserman, 2015, DOI: 10.48550/arXiv.1409.1556).** VGGNet demostró que la profundidad de la red es un factor crítico para el rendimiento. Su principal contribución fue el uso exclusivo de kernels $3 \times 3$ (los más pequeños que capturan la noción de izquierda/derecha, arriba/abajo, centro) en configuraciones de hasta 19 capas (VGG-19). Esta decisión de diseño mostró que apilar múltiples capas con kernels pequeños es más efectivo que usar pocas capas con kernels grandes, tanto en términos de parámetros como de capacidad de representación.

**ResNet (He et al., 2016, DOI: 10.1109/CVPR.2016.90).** Las redes residuales (ResNet) resolvieron el problema de la degradación del entrenamiento en redes muy profundas mediante la introducción de *conexiones residuales* (*skip connections*). En lugar de aprender la transformación completa $\mathcal{H}(\mathbf{x})$, cada bloque residual aprende la función residual $\mathcal{F}(\mathbf{x}) = \mathcal{H}(\mathbf{x}) - \mathbf{x}$, con la salida del bloque calculada como:

$$\mathbf{y} = \mathcal{F}(\mathbf{x}) + \mathbf{x}$$

Esta formulación facilita el flujo del gradiente durante la retropropagación y permite entrenar redes con cientos o incluso miles de capas. ResNet ganó ILSVRC 2015 con una red de 152 capas, superando por primera vez el rendimiento humano en la tarea de clasificación de ImageNet.

Estas arquitecturas no solo son relevantes históricamente, sino que sus principios de diseño (profundidad, kernels pequeños, conexiones residuales, normalización) se aplican directamente a las CNN utilizadas en sistemas de comunicaciones, como veremos en las secciones siguientes.

---

## 3.5 Convolución 1D para señales de telecomunicaciones

### 3.5.1 De 2D a 1D: adaptando las CNN para señales

Si bien las CNN fueron popularizadas por sus logros en visión por computadora (datos 2D), la operación de convolución se generaliza de manera natural a datos unidimensionales, como las señales temporales que son ubicuas en las telecomunicaciones. La convolución 1D se define como:

$$(\mathbf{x} * \mathbf{k})[n] = \sum_{m=0}^{K-1} \mathbf{x}[n + m] \cdot \mathbf{k}[m]$$

donde $\mathbf{x}$ es la señal de entrada de longitud $N$, $\mathbf{k}$ es el kernel de longitud $K$, y la salida tiene longitud $N - K + 1$ (sin padding). Esta operación es formalmente idéntica al filtrado digital, una operación fundamental en el procesamiento de señales.

La convolución 1D es particularmente adecuada para señales de telecomunicaciones por varias razones:

- Las señales de comunicación son inherentemente secuenciales (muestras ordenadas en el tiempo).
- Los patrones de interés (transiciones de fase, envolventes de amplitud, patrones de modulación) son locales y se repiten a lo largo de la señal.
- Las técnicas tradicionales de procesamiento de señales (filtros FIR/IIR, ecualización, detección) ya operan mediante convolución, por lo que las CNN 1D son una extensión natural que permite *aprender* los filtros óptimos directamente de los datos.

### 3.5.2 Procesamiento de señales de radiofrecuencia (RF)

En los sistemas de comunicación digital modernos, las señales de radiofrecuencia se capturan y procesan en banda base mediante conversores analógico-digitales (ADC). La señal resultante se representa comúnmente en formato de componentes en fase y cuadratura (I/Q), donde:

$$s(t) = I(t) \cos(2\pi f_c t) - Q(t) \sin(2\pi f_c t)$$

En banda base, cada muestra temporal se describe como un número complejo:

$$s[n] = I[n] + j \cdot Q[n]$$

donde $I[n]$ es la componente en fase y $Q[n]$ es la componente en cuadratura. Esta representación compleja codifica tanto la amplitud como la fase de la señal:

$$A[n] = \sqrt{I[n]^2 + Q[n]^2}, \qquad \phi[n] = \arctan\left(\frac{Q[n]}{I[n]}\right)$$

Para procesar señales I/Q con una CNN, la práctica estándar es representar la señal como una matriz de dimensiones $2 \times N$, donde la primera fila contiene las $N$ muestras de la componente en fase $I[n]$ y la segunda fila contiene las $N$ muestras de la componente en cuadratura $Q[n]$:

$$\mathbf{S} = \begin{bmatrix} I[0] & I[1] & I[2] & \cdots & I[N-1] \\ Q[0] & Q[1] & Q[2] & \cdots & Q[N-1] \end{bmatrix} \in \mathbb{R}^{2 \times N}$$

Esta representación preserva la relación entre las componentes I y Q en cada instante temporal, permitiendo a la CNN explotar tanto las correlaciones temporales (a lo largo del eje horizontal) como las correlaciones entre I y Q (a lo largo del eje vertical).

### 3.5.3 Filtros para patrones en señales de comunicación

Los kernels aprendidos por una CNN 1D para señales de telecomunicaciones desarrollan funcionalidades análogas a los filtros clásicos del procesamiento de señales, pero optimizados para la tarea específica de interés:

**Detectores de transiciones de fase.** En esquemas de modulación por desplazamiento de fase (PSK), la información se codifica en los cambios de fase de la señal portadora. Un kernel que ha aprendido a detectar transiciones de fase podría tener una forma similar a una derivada discreta, respondiendo con alta activación cuando las componentes I/Q cambian de manera consistente con una transición de fase específica (por ejemplo, de $0°$ a $180°$ en BPSK).

**Detectores de patrones de amplitud.** En esquemas de modulación por amplitud en cuadratura (QAM), tanto la amplitud como la fase codifican información. Algunos kernels aprenderán a detectar niveles de amplitud específicos o patrones de transición de amplitud que caracterizan diferentes órdenes de modulación.

**Filtros de ecualización adaptativa.** En canales con desvanecimiento (*fading*) o interferencia entre símbolos (ISI), algunos kernels pueden aprender funciones similares a un ecualizador, compensando las distorsiones del canal para extraer características más limpias de la señal.

La ventaja fundamental de las CNN sobre los métodos clásicos de procesamiento de señales radica en que estos filtros se aprenden automáticamente de los datos, sin requerir un diseño manual basado en modelos matemáticos del canal o la modulación. Esto es particularmente valioso en escenarios de comunicaciones semánticas, donde las características relevantes de la señal pueden no ser evidentes a priori.

**Figura 3.3:** *Convolución 1D aplicada a datos de señales I/Q. Se muestra una señal de entrada representada como una matriz $2 \times N$, donde la fila superior corresponde a la componente en fase $I[n]$ (representada en azul) y la fila inferior a la componente en cuadratura $Q[n]$ (representada en rojo). Un kernel de dimensiones $2 \times 7$ (altura 2 para abarcar ambos canales I/Q, ancho 7 para capturar un patrón temporal de 7 muestras) se desliza horizontalmente sobre la señal. En cada posición, el kernel realiza un producto punto con la submatriz correspondiente de la señal, produciendo un valor escalar en el mapa de características de salida (una secuencia 1D de longitud $N - 7 + 1$). Se destacan tres posiciones del kernel y sus activaciones resultantes. En la parte inferior, se muestran los pesos del kernel visualizados como un mapa de calor de $2 \times 7$, ilustrando cómo diferentes filas capturan patrones en I y Q respectivamente, mientras que las columnas capturan la evolución temporal del patrón.*

---

## 3.6 Caso práctico: Clasificación Automática de Modulación (AMC)

### 3.6.1 Descripción del problema

La clasificación automática de modulación (*Automatic Modulation Classification*, AMC) es una tarea fundamental en los sistemas de comunicaciones inalámbricas, con aplicaciones tanto en escenarios civiles como militares. El objetivo consiste en identificar el tipo de modulación utilizado por un transmisor a partir de las muestras de la señal recibida, sin conocimiento previo del esquema de modulación empleado. Formalmente, dado un vector de muestras I/Q recibidas $\mathbf{s} = \{s[0], s[1], \ldots, s[N-1]\}$, donde $s[n] = I[n] + jQ[n]$, el problema de AMC se formula como un problema de clasificación:

$$\hat{c} = \arg\max_{c \in \mathcal{C}} P(c \mid \mathbf{s})$$

donde $\mathcal{C} = \{\text{BPSK}, \text{QPSK}, \text{8PSK}, \text{QAM16}, \text{QAM64}, \text{GFSK}, \text{OFDM}, \ldots\}$ es el conjunto de esquemas de modulación posibles.

La AMC tiene múltiples aplicaciones prácticas de gran relevancia:

- **Radio cognitiva (*cognitive radio*).** Los sistemas de radio cognitiva necesitan identificar los esquemas de modulación de los usuarios primarios para adaptar sus propias transmisiones y evitar interferencias, o para reutilizar espectro de manera oportunista.
- **Monitoreo del espectro.** Los reguladores de telecomunicaciones utilizan AMC para supervisar el uso del espectro electromagnético, detectar transmisiones no autorizadas e identificar fuentes de interferencia.
- **Comunicaciones adaptativas.** En sistemas de modulación y codificación adaptativa (AMC/ACM), el receptor debe clasificar la modulación para decodificar correctamente los datos cuando el esquema cambia dinámicamente según las condiciones del canal.
- **Inteligencia de señales (SIGINT).** En aplicaciones de defensa, la identificación de la modulación es un paso crucial en la cadena de procesamiento de señales interceptadas.

Los enfoques tradicionales de AMC se basan en características diseñadas manualmente (*hand-crafted features*), como momentos estadísticos de orden superior, cumulantes, funciones de densidad espectral y características cíclicas. Estos métodos requieren un conocimiento profundo del dominio y pueden fallar cuando las condiciones del canal difieren de los modelos asumidos. Las CNN ofrecen una alternativa poderosa: aprender las características relevantes directamente de las muestras crudas de I/Q, eliminando la necesidad de ingeniería de características manual.

### 3.6.2 Arquitectura CNN para AMC

La arquitectura CNN para AMC que presentamos se basa en el trabajo seminal de O'Shea, Corgan y Clancy (2016, DOI: 10.1109/MILCOM.2016.7795369), quienes demostraron que las CNN pueden aprender a clasificar modulaciones directamente de datos I/Q crudos, igualando o superando a los métodos basados en características manuales. La arquitectura toma como entrada un tensor de dimensiones $(2, 128)$, donde:

- El primer eje (dimensión 2) corresponde a los dos canales: componente en fase $I[n]$ y componente en cuadratura $Q[n]$.
- El segundo eje (dimensión 128) corresponde a 128 muestras temporales consecutivas.

**Diseño del kernel: $(2, 7)$.** La elección del tamaño del kernel es crucial y merece una explicación detallada:

- **Altura $= 2$:** El kernel abarca ambas filas de la representación I/Q. Esto permite que cada filtro compute funciones que involucran simultáneamente las componentes $I[n]$ y $Q[n]$ en cada posición temporal. Dado que la información de modulación está codificada en la relación entre I y Q (por ejemplo, la constelación QAM se define por los pares $(I, Q)$ en el plano complejo), es esencial que el kernel pueda acceder a ambas componentes. Un kernel con altura $1$ solo vería una componente a la vez, perdiendo la capacidad de computar la fase $\phi = \arctan(Q/I)$ o la amplitud $A = \sqrt{I^2 + Q^2}$.

- **Ancho $= 7$:** El kernel cubre 7 muestras temporales consecutivas. Este ancho se escoge para capturar patrones temporales que abarcan varios períodos de símbolo. Dependiendo de la tasa de muestreo, 7 muestras pueden cubrir entre 1 y 3 símbolos, lo que permite detectar transiciones entre símbolos, patrones de conformación de pulso (*pulse shaping*) y la estructura temporal de la modulación. Un kernel demasiado estrecho (por ejemplo, ancho 1) solo vería una muestra I/Q aislada, perdiendo el contexto temporal. Un kernel demasiado ancho tendría demasiados parámetros y podría capturar correlaciones espurias.

- **Por qué esta forma funcional específica opera correctamente.** El kernel $(2, 7)$ realiza esencialmente una operación de filtrado lineal en el dominio complejo. Para cada posición del deslizamiento, el kernel computa:

$$y[n] = \sum_{m=0}^{6} \left( w_{I}[m] \cdot I[n+m] + w_{Q}[m] \cdot Q[n+m] \right)$$

donde $w_I[m] = K[0, m]$ y $w_Q[m] = K[1, m]$ son los pesos del kernel para las componentes I y Q respectivamente. Esta operación es equivalente a un filtro complejo $h[m] = w_I[m] + j \cdot w_Q[m]$ aplicado a la señal compleja $s[n] = I[n] + jQ[n]$, lo que conecta directamente la convolución de la CNN con el procesamiento clásico de señales en banda base.

La arquitectura completa se puede describir esquemáticamente:

1. **Entrada:** Tensor $(2, 128)$ — muestras I/Q
2. **Conv1 + ReLU:** 64 filtros de $(2, 7)$, stride $(1, 1)$, sin padding → Salida: $(64, 1, 122)$
3. **Conv2 + ReLU:** 32 filtros de $(1, 5)$, stride $(1, 1)$ → Salida: $(32, 1, 118)$
4. **Flatten:** Vector de $32 \times 118 = 3{,}776$ elementos
5. **Dense1 + ReLU:** 128 neuronas
6. **Dropout:** $p = 0.5$
7. **Dense2 + Softmax:** $C$ neuronas (una por cada tipo de modulación)

**Figura 3.4:** *Pipeline del sistema de clasificación automática de modulación (AMC) basado en CNN. De izquierda a derecha: (1) Una señal de radiofrecuencia es captada por una antena receptora. (2) Un conversor analógico-digital (ADC) muestrea la señal y la descompone en componentes I/Q. (3) Las muestras I/Q se organizan en una matriz $2 \times 128$ que sirve como entrada a la CNN. (4) La CNN procesa la señal a través de capas convolucionales 1D (con kernels de $(2,7)$) que extraen características de la señal, seguidas de capas densas. (5) La capa de salida softmax produce probabilidades para cada tipo de modulación posible (BPSK, QPSK, 8PSK, QAM16, QAM64, etc.). Se muestra una barra de probabilidades donde la clase predicha (por ejemplo, QPSK) tiene la probabilidad más alta. A lo largo del pipeline se indican las dimensiones del tensor en cada etapa.*

### 3.6.3 Implementación en PyTorch

A continuación, presentamos una implementación completa en PyTorch de la arquitectura CNN para AMC, con explicación línea por línea:

```python
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset

# ============================================================
# Definición de la arquitectura CNN para clasificación de modulación
# ============================================================

class ModulationCNN(nn.Module):
    """
    Red neuronal convolucional para clasificación automática de modulación.
    Recibe muestras I/Q crudas y predice el tipo de modulación.
    """

    def __init__(self, num_classes=8):
        """
        Inicializa las capas de la CNN.

        Args:
            num_classes: Número de tipos de modulación a clasificar.
                         Ejemplo: 8 para {BPSK, QPSK, 8PSK, QAM16,
                         QAM64, GFSK, CPFSK, PAM4}.
        """
        super(ModulationCNN, self).__init__()

        # --- Primera capa convolucional ---
        # nn.Conv2d(in_channels, out_channels, kernel_size)
        # in_channels=1: la entrada tiene 1 "imagen" (la matriz 2x128)
        # out_channels=64: aprendemos 64 filtros diferentes
        # kernel_size=(2, 7): altura=2 (cubre I y Q), ancho=7 (patrón temporal)
        # Cada filtro aprende un patrón I/Q-temporal diferente.
        self.conv1 = nn.Conv2d(
            in_channels=1,
            out_channels=64,
            kernel_size=(2, 7),
            stride=(1, 1),
            padding=0
        )
        # Activación ReLU: introduce no linealidad, permite combinaciones
        # complejas de características I/Q.
        self.relu1 = nn.ReLU()

        # --- Segunda capa convolucional ---
        # in_channels=64: recibe los 64 mapas de la capa anterior
        # out_channels=32: comprime a 32 mapas de características
        # kernel_size=(1, 5): altura=1 (dimensión I/Q ya fue colapsada),
        #                     ancho=5 (combina 5 posiciones temporales)
        # Esta capa combina las características de bajo nivel aprendidas
        # por conv1 en patrones temporales más complejos.
        self.conv2 = nn.Conv2d(
            in_channels=64,
            out_channels=32,
            kernel_size=(1, 5),
            stride=(1, 1),
            padding=0
        )
        self.relu2 = nn.ReLU()

        # --- Capa densa 1 ---
        # Después de conv1: salida espacial = (1, 122) → 64 canales
        # Después de conv2: salida espacial = (1, 118) → 32 canales
        # Flatten: 32 * 1 * 118 = 3776 elementos
        # La capa densa combina toda la información espacial y de canal
        # para formar una representación global de la señal.
        self.fc1 = nn.Linear(32 * 1 * 118, 128)
        self.relu3 = nn.ReLU()

        # --- Dropout para regularización ---
        # Durante el entrenamiento, desactiva aleatoriamente el 50% de
        # las neuronas para prevenir sobreajuste y forzar redundancia.
        self.dropout = nn.Dropout(p=0.5)

        # --- Capa de salida ---
        # Produce un logit por cada clase de modulación.
        # La función softmax se aplica implícitamente por
        # nn.CrossEntropyLoss durante el entrenamiento.
        self.fc2 = nn.Linear(128, num_classes)

    def forward(self, x):
        """
        Propagación hacia adelante.

        Args:
            x: Tensor de forma (batch_size, 1, 2, 128)
               batch_size: número de señales en el lote
               1: canal de la "imagen" (no confundir con I/Q)
               2: dimensión I/Q (fila 0 = I, fila 1 = Q)
               128: muestras temporales

        Returns:
            Tensor de logits de forma (batch_size, num_classes)
        """
        # Capa convolucional 1: (batch, 1, 2, 128) → (batch, 64, 1, 122)
        x = self.relu1(self.conv1(x))

        # Capa convolucional 2: (batch, 64, 1, 122) → (batch, 32, 1, 118)
        x = self.relu2(self.conv2(x))

        # Aplanar: (batch, 32, 1, 118) → (batch, 3776)
        x = x.view(x.size(0), -1)

        # Capa densa 1: (batch, 3776) → (batch, 128)
        x = self.relu3(self.fc1(x))

        # Dropout: desactiva neuronas aleatoriamente (solo en entrenamiento)
        x = self.dropout(x)

        # Capa de salida: (batch, 128) → (batch, num_classes)
        x = self.fc2(x)

        return x


# ============================================================
# Configuración del entrenamiento
# ============================================================

# Hiperparámetros
num_classes = 8        # Tipos de modulación
batch_size = 64        # Señales procesadas por iteración
learning_rate = 0.001  # Tasa de aprendizaje para Adam
num_epochs = 50        # Pasadas completas por el dataset

# Simulación de datos de ejemplo (en la práctica, se usaría un dataset
# real como RadioML 2016.10A o RadioML 2018.01A)
# X_train: (N, 1, 2, 128) - N señales, 1 canal, 2 filas I/Q, 128 muestras
# y_train: (N,) - etiquetas de modulación (enteros 0 a num_classes-1)
N_train = 10000
X_train = torch.randn(N_train, 1, 2, 128)  # Datos simulados
y_train = torch.randint(0, num_classes, (N_train,))  # Etiquetas simuladas

# Crear DataLoader para iteración eficiente por lotes
train_dataset = TensorDataset(X_train, y_train)
train_loader = DataLoader(
    train_dataset,
    batch_size=batch_size,
    shuffle=True  # Mezclar datos en cada época para mejor convergencia
)

# Instanciar el modelo
model = ModulationCNN(num_classes=num_classes)

# Función de pérdida: entropía cruzada (incluye softmax internamente)
# Es la elección estándar para clasificación multiclase.
criterion = nn.CrossEntropyLoss()

# Optimizador: Adam (combina momento y tasas de aprendizaje adaptativas)
optimizer = optim.Adam(model.parameters(), lr=learning_rate)

# ============================================================
# Bucle de entrenamiento
# ============================================================

for epoch in range(num_epochs):
    model.train()  # Modo entrenamiento: activa dropout y batch norm
    running_loss = 0.0
    correct = 0
    total = 0

    for batch_X, batch_y in train_loader:
        # 1. Limpiar gradientes de la iteración anterior
        optimizer.zero_grad()

        # 2. Propagación hacia adelante: calcular predicciones
        outputs = model(batch_X)

        # 3. Calcular la pérdida (entropía cruzada)
        loss = criterion(outputs, batch_y)

        # 4. Retropropagación: calcular gradientes de todos los parámetros
        loss.backward()

        # 5. Actualizar parámetros usando los gradientes calculados
        optimizer.step()

        # Estadísticas de entrenamiento
        running_loss += loss.item()
        _, predicted = torch.max(outputs.data, 1)
        total += batch_y.size(0)
        correct += (predicted == batch_y).sum().item()

    # Imprimir progreso cada 10 épocas
    if (epoch + 1) % 10 == 0:
        accuracy = 100.0 * correct / total
        avg_loss = running_loss / len(train_loader)
        print(f'Época [{epoch+1}/{num_epochs}], '
              f'Pérdida: {avg_loss:.4f}, '
              f'Precisión: {accuracy:.2f}%')

# ============================================================
# Inferencia (clasificación de nuevas señales)
# ============================================================

model.eval()  # Modo evaluación: desactiva dropout
with torch.no_grad():  # No calcular gradientes (ahorra memoria y tiempo)
    # Señal de prueba: una muestra I/Q de 128 puntos
    test_signal = torch.randn(1, 1, 2, 128)  # (1 señal, 1 canal, 2xI/Q, 128)
    output = model(test_signal)

    # Aplicar softmax para obtener probabilidades
    probabilities = torch.softmax(output, dim=1)

    # Obtener la clase predicha
    _, predicted_class = torch.max(probabilities, 1)

    modulation_names = ['BPSK', 'QPSK', '8PSK', 'QAM16',
                        'QAM64', 'GFSK', 'CPFSK', 'PAM4']
    print(f'\nModulación predicha: {modulation_names[predicted_class.item()]}')
    print(f'Probabilidades: {probabilities.squeeze().numpy()}')
```

Este código ilustra el pipeline completo de una CNN para AMC. En la práctica, el modelo se entrenaría con un dataset real como RadioML 2016.10A, que contiene señales simuladas bajo diversas condiciones de relación señal a ruido (SNR). Los resultados publicados en la literatura demuestran que este tipo de arquitectura alcanza precisiones superiores al 90% para valores de SNR moderados (por encima de 5 dB) en la clasificación de 8 a 11 tipos de modulación.

---

## 3.7 Autoencoders convolucionales para detección de anomalías

### 3.7.1 Concepto de autoencoder

Un autoencoder es una red neuronal que aprende a reconstruir su propia entrada. A diferencia de los modelos de clasificación que mapean entradas a etiquetas, un autoencoder aprende un mapeo identidad $f: \mathbb{R}^d \rightarrow \mathbb{R}^d$, pero con una restricción crucial: la información debe pasar a través de una representación intermedia (espacio latente) de dimensionalidad reducida. Esta restricción fuerza a la red a aprender una compresión eficiente de los datos, capturando solo las características más relevantes y descartando el ruido y la información redundante.

Formalmente, un autoencoder consta de dos componentes:

**Encoder (codificador).** Transforma la entrada $\mathbf{x} \in \mathbb{R}^d$ en una representación latente $\mathbf{z} \in \mathbb{R}^{d_z}$ con $d_z \ll d$:

$$\mathbf{z} = f_{\text{enc}}(\mathbf{x}; \theta_{\text{enc}})$$

donde $f_{\text{enc}}$ es la función del encoder parametrizada por $\theta_{\text{enc}}$. En un autoencoder convolucional, el encoder utiliza capas convolucionales con stride mayor que 1 (o pooling) para reducir progresivamente la dimensionalidad espacial.

**Decoder (decodificador).** Reconstruye la entrada original a partir de la representación latente:

$$\hat{\mathbf{x}} = f_{\text{dec}}(\mathbf{z}; \theta_{\text{dec}})$$

En un autoencoder convolucional, el decoder utiliza operaciones de convolución transpuesta (*transposed convolution* o *deconvolution*) para aumentar progresivamente la dimensionalidad espacial hasta recuperar las dimensiones originales de la entrada.

La composición de ambos componentes produce la reconstrucción:

$$\hat{\mathbf{x}} = f_{\text{dec}}(f_{\text{enc}}(\mathbf{x}; \theta_{\text{enc}}); \theta_{\text{dec}})$$

La arquitectura se denomina frecuentemente como un modelo de "reloj de arena" (*hourglass*) o "cuello de botella" (*bottleneck*), ya que las dimensiones se reducen en el encoder y se expanden en el decoder, con el punto más estrecho siendo el espacio latente.

### 3.7.2 Función de pérdida: error de reconstrucción

El autoencoder se entrena minimizando el error de reconstrucción entre la entrada original $\mathbf{x}$ y la salida reconstruida $\hat{\mathbf{x}}$. La función de pérdida más comúnmente utilizada es el error cuadrático medio (*Mean Squared Error*, MSE):

$$L(\theta_{\text{enc}}, \theta_{\text{dec}}) = \frac{1}{N} \sum_{i=1}^{N} ||\mathbf{x}_i - \hat{\mathbf{x}}_i||^2$$

donde $N$ es el número de muestras en el conjunto de entrenamiento y $||\cdot||^2$ denota la norma $L^2$ al cuadrado. Para una señal individual, la pérdida de reconstrucción es:

$$L = ||\mathbf{x} - \hat{\mathbf{x}}||^2 = \sum_{j=1}^{d} (x_j - \hat{x}_j)^2$$

Esta función de pérdida tiene una interpretación probabilística: minimizar el MSE es equivalente a maximizar la log-verosimilitud bajo un modelo gaussiano con varianza constante:

$$\log p(\mathbf{x} \mid \hat{\mathbf{x}}) = -\frac{d}{2}\log(2\pi\sigma^2) - \frac{1}{2\sigma^2}||\mathbf{x} - \hat{\mathbf{x}}||^2$$

Alternativas al MSE incluyen el error absoluto medio (MAE, o norma $L^1$), que es más robusto a valores atípicos, y la divergencia de Kullback-Leibler, utilizada en autoencoders variacionales (VAE).

### 3.7.3 Entrenamiento con datos "normales" y detección de anomalías

La clave de la detección de anomalías mediante autoencoders reside en una estrategia de entrenamiento asimétrica: el autoencoder se entrena exclusivamente con datos que representan el comportamiento "normal" o esperado del sistema. Durante el entrenamiento, la red aprende a comprimir y reconstruir con alta fidelidad los patrones normales, ya que estos son los únicos que observa repetidamente.

Una vez entrenado, el autoencoder se utiliza para evaluar nuevas señales. Si una señal es "normal" (similar a los datos de entrenamiento), el autoencoder la reconstruirá con un error bajo, ya que ha aprendido las regularidades de ese tipo de datos. Si la señal es "anómala" (diferente de los patrones normales), el autoencoder no podrá reconstruirla adecuadamente, produciendo un error de reconstrucción elevado.

Formalmente, se define un umbral de anomalía $\tau$ y se clasifica cada señal según:

$$\text{Decisión}(\mathbf{x}) = \begin{cases} \text{Normal} & \text{si } ||\mathbf{x} - \hat{\mathbf{x}}||^2 \leq \tau \\ \text{Anomalía} & \text{si } ||\mathbf{x} - \hat{\mathbf{x}}||^2 > \tau \end{cases}$$

El umbral $\tau$ se determina típicamente a partir de la distribución de errores de reconstrucción sobre un conjunto de validación de datos normales. Una elección común es establecer $\tau$ como el percentil 95 o 99 de esta distribución:

$$\tau = Q_{1-\alpha}(\{L_i\}_{i=1}^{N_{\text{val}}})$$

donde $Q_{1-\alpha}$ denota el cuantil $(1-\alpha)$ y $\alpha$ es la tasa de falsa alarma deseada.

Esta metodología tiene una ventaja fundamental: no requiere ejemplos de anomalías para el entrenamiento. Esto es especialmente valioso en telecomunicaciones, donde las anomalías pueden ser eventos raros, diversos e impredecibles (nuevos tipos de interferencia, ataques de *jamming* no anticipados, fallos de hardware novedosos).

### 3.7.4 Aplicación: detección de señales anómalas en telecomunicaciones

En el contexto de las telecomunicaciones, los autoencoders convolucionales pueden aplicarse para detectar una amplia variedad de anomalías en señales de radiofrecuencia:

**Detección de interferencia.** Un autoencoder entrenado con señales "limpias" (sin interferencia) producirá un error de reconstrucción elevado cuando la señal recibida contenga interferencia de fuentes externas, ya que los patrones de interferencia no forman parte de la distribución aprendida.

**Detección de *jamming*.** Los ataques de *jamming* introducen señales artificiales diseñadas para degradar las comunicaciones. Estos ataques generan patrones en las señales I/Q que difieren de las comunicaciones legítimas, produciendo errores de reconstrucción anómalos.

**Detección de fallos de hardware.** Fallos en los componentes del transmisor o receptor (amplificadores no lineales, osciladores con deriva de frecuencia, conversores defectuosos) generan distorsiones características en la señal que el autoencoder puede detectar como anomalías.

**Monitoreo de calidad del canal.** Cambios abruptos en las condiciones del canal (desvanecimiento profundo, obstrucciones súbitas, cambios en el entorno de propagación) se reflejan como alteraciones en las características estadísticas de la señal que elevan el error de reconstrucción.

La arquitectura de un autoencoder convolucional para señales I/Q sigue una estructura simétrica. El encoder aplica capas convolucionales con stride 2 para reducir progresivamente la dimensión temporal, mientras que el decoder utiliza convoluciones transpuestas con stride 2 para expandir la dimensión temporal hasta recuperar la longitud original. Por ejemplo:

**Encoder:**
$$\mathbf{x} \in \mathbb{R}^{2 \times 128} \xrightarrow{\text{Conv}(16, (2,7), s=2)} \mathbb{R}^{16 \times 1 \times 61} \xrightarrow{\text{Conv}(32, (1,5), s=2)} \mathbb{R}^{32 \times 1 \times 29} \xrightarrow{\text{Conv}(64, (1,3), s=2)} \mathbb{R}^{64 \times 1 \times 14}$$

**Espacio latente:** $\mathbf{z} \in \mathbb{R}^{64 \times 1 \times 14}$ (compresión de $256$ a $896$ valores, aunque con mayor número de canales que capturan la estructura de los datos)

**Decoder:**
$$\mathbf{z} \xrightarrow{\text{ConvT}(32, (1,3), s=2)} \mathbb{R}^{32 \times 1 \times 29} \xrightarrow{\text{ConvT}(16, (1,5), s=2)} \mathbb{R}^{16 \times 1 \times 61} \xrightarrow{\text{ConvT}(1, (2,7), s=2)} \mathbb{R}^{1 \times 2 \times 128}$$

En la práctica, las dimensiones exactas del decoder requieren ajustes de relleno (*output padding*) para garantizar que la salida tenga exactamente las mismas dimensiones que la entrada. La función de pérdida MSE se calcula sobre todos los valores de la señal reconstruida:

$$L = \frac{1}{2 \times 128} \sum_{c=0}^{1} \sum_{n=0}^{127} (x[c, n] - \hat{x}[c, n])^2$$

donde $c \in \{0, 1\}$ indexa las componentes I y Q, y $n$ indexa las muestras temporales.

Durante la operación, el sistema monitorea continuamente el error de reconstrucción. Un incremento sostenido por encima del umbral $\tau$ activa una alarma que puede desencadenar acciones correctivas: cambio de frecuencia de operación, activación de mecanismos anti-*jamming*, notificación al operador de red, o adaptación automática de los parámetros de transmisión. En el contexto de las comunicaciones semánticas, esta capacidad de detección de anomalías es particularmente relevante, ya que permite al sistema identificar cuándo las condiciones del canal o el entorno de transmisión se desvían de lo esperado, adaptando dinámicamente la codificación semántica para mantener la fidelidad de la comunicación.

---

### Resumen de la Sección 3

En esta sección hemos desarrollado exhaustivamente los fundamentos de las redes neuronales convolucionales, desde la motivación teórica y la definición matemática de la convolución hasta sus aplicaciones prácticas en telecomunicaciones. Los conceptos clave incluyen:

- La operación de convolución como alternativa eficiente a las capas densas, explotando localidad, compartición de pesos e invarianza a traslaciones.
- Los componentes de una CNN: capas convolucionales (con sus hiperparámetros de kernel, stride y padding), capas de pooling (Max y Average), y capas densas finales.
- La fórmula del tamaño de salida: $o = \lfloor (n + 2p - k) / s \rfloor + 1$.
- Las arquitecturas clásicas (LeNet-5, AlexNet, VGG, ResNet) y sus contribuciones al campo.
- La convolución 1D y su aplicación natural al procesamiento de señales I/Q.
- Un caso práctico completo de clasificación automática de modulación (AMC) con implementación en PyTorch.
- Los autoencoders convolucionales para detección de anomalías en señales de telecomunicaciones.

Estos conceptos forman la base para entender cómo las CNN se integran en los sistemas de comunicaciones semánticas, donde la extracción de características relevantes de señales complejas es un requisito fundamental.
