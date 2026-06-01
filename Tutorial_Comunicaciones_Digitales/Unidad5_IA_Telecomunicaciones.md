# Unidad 5: Introducción a la IA en Telecomunicaciones

## Introducción de la unidad

La inteligencia artificial (IA) ha pasado de ser una herramienta auxiliar de análisis a convertirse en un **componente estructural** de los sistemas modernos de telecomunicaciones. En las generaciones previas de redes móviles, el diseño se apoyaba principalmente en modelos matemáticos explícitos: canal lineal, ruido gaussiano, sincronización ideal, estimación separada y decisiones óptimas bajo hipótesis bien definidas. Ese enfoque sigue siendo fundamental, pero empieza a mostrar límites cuando el sistema real presenta **no linealidades, alta dimensionalidad, movilidad extrema, heterogeneidad de servicios y necesidad de adaptación en tiempo real**.

En este contexto, la IA y el aprendizaje automático permiten aprender relaciones complejas directamente a partir de datos, construir receptores más robustos, optimizar recursos de red, mover la inteligencia al borde y, en la visión 6G, diseñar una **arquitectura AI-nativa** en la que la comunicación y la inteligencia coevolucionan. Esta unidad introduce, con enfoque pedagógico y matemático, tres pilares: 

1. los fundamentos de redes neuronales;
2. los receptores neuronales para procesamiento de señales;
3. la integración de IA en redes 6G e IMT-2030.

El objetivo es que un lector principiante comprenda no solo *qué* hace la IA en telecomunicaciones, sino también *cómo* se modela, *por qué* funciona y *cuáles son sus límites*.

---

## 5.1 Conceptos Básicos de Redes Neuronales

### 5.1.1 Arquitectura de la neurona artificial

La neurona artificial abstrae el comportamiento de una neurona biológica: recibe entradas, las pondera, suma un sesgo y produce una salida no lineal.

La forma general es:

$$
y = f\left(\sum_{i=1}^{n} w_i x_i + b\right)
$$

donde:

- $x_i$ son las entradas;
- $w_i$ son los pesos sinápticos;
- $b$ es el sesgo (*bias*);
- $f(\cdot)$ es la función de activación;
- $y$ es la salida.

> **Ecuación clave 5.1:**
>
> $$
> y = f(\mathbf{w}^T \mathbf{x} + b)
> $$
>
> con $\mathbf{x} \in \mathbb{R}^n$ y $\mathbf{w} \in \mathbb{R}^n$.

#### a) Modelo de McCulloch-Pitts

El modelo de McCulloch-Pitts es un precursor lógico de la neurona artificial. Se basa en una suma ponderada y una activación umbral:

$$
y = \begin{cases}
1, & \text{si } \sum_i w_i x_i \geq \theta \\
0, & \text{si } \sum_i w_i x_i < \theta
\end{cases}
$$

Aquí, $\theta$ es un umbral. Este modelo implementa funciones lógicas simples, pero no permite entrenamiento diferencial porque la activación es no derivable.

#### b) Perceptrón

El perceptrón reemplaza el umbral fijo por un sesgo $b = -\theta$:

$$
y = \phi(\mathbf{w}^T\mathbf{x} + b)
$$

con función escalón:

$$
\phi(z) = \begin{cases}
1, & z \geq 0 \\
0, & z < 0
\end{cases}
$$

El perceptrón aprende un hiperplano separador. Si los datos son linealmente separables, existe un conjunto de pesos que clasifica correctamente las muestras.

#### c) Funciones de activación

La activación introduce no linealidad. Sin ella, una red multicapa colapsaría en una sola transformación lineal.

**Sigmoide**:

$$
\sigma(z) = \frac{1}{1 + e^{-z}}
$$

Rango: $\sigma(z) \in (0,1)$.

Derivada:

$$
\sigma'(z) = \sigma(z)(1-\sigma(z))
$$

Se usa en salidas binarias o como probabilidad, pero puede sufrir **desvanecimiento del gradiente** cuando $|z|$ es grande.

**Tangente hiperbólica**:

$$
\tanh(z) = \frac{e^z - e^{-z}}{e^z + e^{-z}}
$$

Rango: $(-1,1)$.

Derivada:

$$
\frac{d}{dz}\tanh(z) = 1 - \tanh^2(z)
$$

Suele centrar activaciones alrededor de cero, lo cual puede facilitar el entrenamiento.

**ReLU** (*Rectified Linear Unit*):

$$
\mathrm{ReLU}(z) = \max(0,z)
$$

Derivada:

$$
\mathrm{ReLU}'(z) = \begin{cases}
1, & z > 0 \\
0, & z < 0
\end{cases}
$$

Es muy usada por su simplicidad y eficiencia, aunque puede producir neuronas muertas si muchas entradas quedan en la región negativa.

**Softmax** para clasificación multiclase:

Si el vector de entrada a la capa de salida es $\mathbf{z} = [z_1,\dots,z_K]^T$, entonces

$$
\mathrm{softmax}(z_k) = \frac{e^{z_k}}{\sum_{j=1}^{K} e^{z_j}}, \qquad k=1,\dots,K
$$

Propiedades:

$$
0 \leq p_k \leq 1, \qquad \sum_{k=1}^{K} p_k = 1
$$

Por tanto, la salida puede interpretarse como distribución de probabilidad sobre clases, por ejemplo, símbolos de una constelación digital.

[Figura 5.1]: **Neurona artificial y activaciones típicas.** La figura debe mostrar una neurona con varias entradas $x_1, x_2, \dots, x_n$, cada una conectada mediante pesos $w_1, w_2, \dots, w_n$, seguida de un sumador que genera $z = \sum_i w_i x_i + b$ y un bloque de activación $f(z)$. Junto a la neurona conviene incluir gráficos de las funciones sigmoide, $\tanh$, ReLU y softmax. El objetivo pedagógico de esta figura es que el lector visualice la separación entre la parte lineal del modelo (suma ponderada) y la parte no lineal (activación), entendiendo que la capacidad de aprendizaje profundo surge precisamente de encadenar muchas de estas transformaciones.

### 5.1.2 Estructura de capas

Una red neuronal típica se organiza en:

- **Capa de entrada**: recibe el vector de características $\mathbf{x}$.
- **Capas ocultas**: transforman progresivamente la representación.
- **Capa de salida**: entrega la predicción final.

Si la red tiene $L$ capas parametrizadas, la propagación se expresa como:

$$
\mathbf{a}^{[0]} = \mathbf{x}
$$

$$
\mathbf{z}^{[l]} = \mathbf{W}^{[l]}\mathbf{a}^{[l-1]} + \mathbf{b}^{[l]}, \qquad l=1,2,\dots,L
$$

$$
\mathbf{a}^{[l]} = f^{[l]}\left(\mathbf{z}^{[l]}\right)
$$

Aquí:

- $\mathbf{W}^{[l]} \in \mathbb{R}^{n_l \times n_{l-1}}$;
- $\mathbf{b}^{[l]} \in \mathbb{R}^{n_l}$;
- $\mathbf{a}^{[l]} \in \mathbb{R}^{n_l}$ es la activación de la capa $l$.

### 5.1.3 Redes completamente conectadas

En una red **fully connected** o **dense**, cada neurona de una capa está conectada con todas las neuronas de la capa anterior. Esto implica un gran poder de representación, pero también un número elevado de parámetros:

$$
\#\text{parámetros en la capa } l = n_l n_{l-1} + n_l
$$

Por ejemplo, si una capa recibe 128 entradas y tiene 64 neuronas, entonces:

$$
128 \times 64 + 64 = 8256
$$

parámetros deben aprenderse.

En telecomunicaciones, estas redes densas son útiles para:

- clasificación de símbolos;
- estimación de canal basada en datos;
- detección multiusuario;
- asignación de recursos a partir de características agregadas.

### 5.1.4 Propagación hacia adelante (*forward propagation*)

La propagación hacia adelante consiste en calcular la salida de la red capa por capa.

Para una red de dos capas ocultas:

$$
\mathbf{a}^{[1]} = f^{[1]}(\mathbf{W}^{[1]}\mathbf{x} + \mathbf{b}^{[1]})
$$

$$
\mathbf{a}^{[2]} = f^{[2]}(\mathbf{W}^{[2]}\mathbf{a}^{[1]} + \mathbf{b}^{[2]})
$$

$$
\hat{\mathbf{y}} = \mathbf{a}^{[3]} = f^{[3]}(\mathbf{W}^{[3]}\mathbf{a}^{[2]} + \mathbf{b}^{[3]})
$$

#### Notación matricial para un lote (*batch*)

Si se procesan $m$ muestras a la vez, con matriz de entrada $\mathbf{X} \in \mathbb{R}^{n_0 \times m}$:

$$
\mathbf{Z}^{[l]} = \mathbf{W}^{[l]}\mathbf{A}^{[l-1]} + \mathbf{b}^{[l]}\mathbf{1}^T
$$

$$
\mathbf{A}^{[l]} = f^{[l]}(\mathbf{Z}^{[l]})
$$

Esta formulación es crucial en hardware paralelo (GPU/TPU), especialmente importante cuando los problemas de telecomunicaciones generan grandes volúmenes de muestras I/Q, snapshots de canal o secuencias temporales.

### 5.1.5 Función de pérdida

La función de pérdida cuantifica la discrepancia entre la salida deseada $\mathbf{y}$ y la predicción $\hat{\mathbf{y}}$.

#### a) Error cuadrático medio (MSE)

Para regresión:

$$
\mathcal{L}_{\mathrm{MSE}} = \frac{1}{m} \sum_{i=1}^{m} \|\hat{\mathbf{y}}_i - \mathbf{y}_i\|_2^2
$$

En el caso escalar:

$$
\mathcal{L}_{\mathrm{MSE}} = \frac{1}{m} \sum_{i=1}^{m} (\hat{y}_i - y_i)^2
$$

Se usa en estimación continua, por ejemplo, predicción de potencia, localización, o estimación de parámetros del canal.

#### b) Entropía cruzada binaria

Para clasificación binaria con salida sigmoide:

$$
\mathcal{L}_{\mathrm{BCE}} = -\frac{1}{m} \sum_{i=1}^{m} \left[y_i \log(\hat{y}_i) + (1-y_i)\log(1-\hat{y}_i)\right]
$$

#### c) Entropía cruzada categórica

Para clasificación multiclase con softmax:

$$
\mathcal{L}_{\mathrm{CE}} = -\frac{1}{m} \sum_{i=1}^{m} \sum_{k=1}^{K} y_{ik} \log(\hat{y}_{ik})
$$

Si $\mathbf{y}_i$ es *one-hot*, solo contribuye la probabilidad asignada a la clase verdadera.

> **Idea clave:** en telecomunicaciones, la entropía cruzada es natural cuando la red debe decidir entre símbolos, clases de modulación, usuarios o estados discretos.

### 5.1.6 Propagación hacia atrás (*backpropagation*)

La retropropagación calcula gradientes de la pérdida respecto a todos los parámetros usando la **regla de la cadena**.

Sea una red con pérdida $\mathcal{L}$. Queremos calcular:

$$
\frac{\partial \mathcal{L}}{\partial \mathbf{W}^{[l]}}, \qquad \frac{\partial \mathcal{L}}{\partial \mathbf{b}^{[l]}}
$$

#### Paso 1: error en la capa de salida

Definimos:

$$
\boldsymbol{\delta}^{[L]} = \frac{\partial \mathcal{L}}{\partial \mathbf{z}^{[L]}}
$$

Como $\mathbf{a}^{[L]} = f^{[L]}(\mathbf{z}^{[L]})$, entonces:

$$
\boldsymbol{\delta}^{[L]} = \frac{\partial \mathcal{L}}{\partial \mathbf{a}^{[L]}} \odot f'^{[L]}(\mathbf{z}^{[L]})
$$

Para salida softmax con entropía cruzada, ocurre una simplificación fundamental:

$$
\boldsymbol{\delta}^{[L]} = \hat{\mathbf{y}} - \mathbf{y}
$$

Para salida sigmoide con entropía cruzada binaria, también se obtiene:

$$
\delta^{[L]} = \hat{y} - y
$$

#### Paso 2: error en capas ocultas

Para $l=L-1, L-2, \dots, 1$:

$$
\boldsymbol{\delta}^{[l]} = \left((\mathbf{W}^{[l+1]})^T \boldsymbol{\delta}^{[l+1]}\right) \odot f'^{[l]}(\mathbf{z}^{[l]})
$$

Esta ecuación expresa cómo el error se propaga hacia atrás a través de la red.

#### Paso 3: gradientes de pesos y sesgos

Para una muestra individual:

$$
\frac{\partial \mathcal{L}}{\partial \mathbf{W}^{[l]}} = \boldsymbol{\delta}^{[l]} (\mathbf{a}^{[l-1]})^T
$$

$$
\frac{\partial \mathcal{L}}{\partial \mathbf{b}^{[l]}} = \boldsymbol{\delta}^{[l]}
$$

Para un lote de tamaño $m$:

$$
\frac{\partial \mathcal{L}}{\partial \mathbf{W}^{[l]}} = \frac{1}{m} \boldsymbol{\Delta}^{[l]} (\mathbf{A}^{[l-1]})^T
$$

$$
\frac{\partial \mathcal{L}}{\partial \mathbf{b}^{[l]}} = \frac{1}{m} \sum_{i=1}^{m} \boldsymbol{\delta}_i^{[l]}
$$

#### Derivación con regla de la cadena

Si una neurona produce:

$$
z_j^{[l]} = \sum_k W_{jk}^{[l]} a_k^{[l-1]} + b_j^{[l]}
$$

entonces:

$$
\frac{\partial \mathcal{L}}{\partial W_{jk}^{[l]}} = \frac{\partial \mathcal{L}}{\partial z_j^{[l]}} \frac{\partial z_j^{[l]}}{\partial W_{jk}^{[l]}} = \delta_j^{[l]} a_k^{[l-1]}
$$

porque:

$$
\frac{\partial z_j^{[l]}}{\partial W_{jk}^{[l]}} = a_k^{[l-1]}
$$

Asimismo:

$$
\frac{\partial \mathcal{L}}{\partial b_j^{[l]}} = \delta_j^{[l]}
$$

La retropropagación es, por tanto, una aplicación estructurada de derivadas parciales y álgebra matricial.

[Figura 5.2]: **Propagación hacia adelante y hacia atrás en una red multicapa.** La figura debe mostrar una red con capa de entrada, una o dos capas ocultas y una capa de salida. Sobre las flechas de izquierda a derecha deben indicarse las operaciones de forward propagation: cálculo de $\mathbf{z}^{[l]}$, activación $\mathbf{a}^{[l]}$ y obtención de la pérdida. Sobre flechas en sentido contrario deben representarse los términos $\boldsymbol{\delta}^{[l]}$ y los gradientes de pesos y sesgos. Esta visualización ayuda a comprender que el entrenamiento no es un “misterio”, sino un procedimiento sistemático de cálculo diferencial.

### 5.1.7 Descenso del gradiente

Una vez obtenidos los gradientes, los parámetros se actualizan para reducir la pérdida.

#### a) Gradiente descendente básico

$$
\mathbf{W}^{[l]} \leftarrow \mathbf{W}^{[l]} - \eta \frac{\partial \mathcal{L}}{\partial \mathbf{W}^{[l]}}
$$

$$
\mathbf{b}^{[l]} \leftarrow \mathbf{b}^{[l]} - \eta \frac{\partial \mathcal{L}}{\partial \mathbf{b}^{[l]}}
$$

Aquí $\eta > 0$ es la **tasa de aprendizaje** (*learning rate*).

#### b) SGD (*Stochastic Gradient Descent*)

En SGD se actualiza usando una sola muestra o un mini-lote pequeño:

$$
\theta \leftarrow \theta - \eta \nabla_\theta \mathcal{L}(\theta; \mathcal{B})
$$

con $\mathcal{B}$ un mini-lote. SGD introduce ruido en la optimización, lo que a menudo ayuda a escapar de mínimos pobres o mesetas.

#### c) Adam

Adam combina momentos de primer y segundo orden del gradiente. Si $g_t = \nabla_\theta \mathcal{L}_t$, entonces:

$$
m_t = \beta_1 m_{t-1} + (1-\beta_1) g_t
$$

$$
v_t = \beta_2 v_{t-1} + (1-\beta_2) g_t^2
$$

Corrección de sesgo:

$$
\hat{m}_t = \frac{m_t}{1-\beta_1^t}, \qquad \hat{v}_t = \frac{v_t}{1-\beta_2^t}
$$

Actualización:

$$
\theta_t = \theta_{t-1} - \eta \frac{\hat{m}_t}{\sqrt{\hat{v}_t} + \epsilon}
$$

Usualmente:

$$
\beta_1 = 0.9, \qquad \beta_2 = 0.999, \qquad \epsilon = 10^{-8}
$$

Adam es muy popular en problemas de telecomunicaciones porque las escalas de gradiente pueden variar mucho entre capas y parámetros.

### 5.1.8 Ejemplo completo de *forward* y *backpropagation*

**Ejemplo 5.1: red con dos entradas, una capa oculta de dos neuronas y una salida binaria.**

Supongamos:

$$
\mathbf{x} = \begin{bmatrix}1 \\ 0.5\end{bmatrix}, \qquad y = 1
$$

Pesos y sesgos de la capa oculta:

$$
\mathbf{W}^{[1]} = \begin{bmatrix}
0.2 & -0.4 \\
0.7 & 0.1
\end{bmatrix}, \qquad
\mathbf{b}^{[1]} = \begin{bmatrix}0.1 \\ -0.2\end{bmatrix}
$$

Pesos y sesgo de la salida:

$$
\mathbf{W}^{[2]} = \begin{bmatrix}0.6 & -0.1\end{bmatrix}, \qquad b^{[2]} = 0.05
$$

Activación sigmoide en ambas capas.

#### Paso 1: propagación hacia adelante

Calculamos la capa oculta:

$$
\mathbf{z}^{[1]} = \mathbf{W}^{[1]}\mathbf{x} + \mathbf{b}^{[1]}
$$

Primera neurona:

$$
z_1^{[1]} = 0.2(1) + (-0.4)(0.5) + 0.1 = 0.1
$$

Segunda neurona:

$$
z_2^{[1]} = 0.7(1) + 0.1(0.5) - 0.2 = 0.55
$$

Entonces:

$$
\mathbf{z}^{[1]} = \begin{bmatrix}0.1 \\ 0.55\end{bmatrix}
$$

Activaciones:

$$
a_1^{[1]} = \sigma(0.1) = \frac{1}{1+e^{-0.1}} \approx 0.52498
$$

$$
a_2^{[1]} = \sigma(0.55) \approx 0.63414
$$

Por tanto:

$$
\mathbf{a}^{[1]} = \begin{bmatrix}0.52498 \\ 0.63414\end{bmatrix}
$$

Ahora la salida:

$$
z^{[2]} = \mathbf{W}^{[2]}\mathbf{a}^{[1]} + b^{[2]}
$$

$$
z^{[2]} = 0.6(0.52498) + (-0.1)(0.63414) + 0.05
$$

$$
z^{[2]} \approx 0.30157
$$

Salida predicha:

$$
\hat{y} = a^{[2]} = \sigma(0.30157) \approx 0.57483
$$

#### Paso 2: pérdida

Usamos entropía cruzada binaria, con $y=1$:

$$
\mathcal{L} = -\log(\hat{y}) = -\log(0.57483) \approx 0.5537
$$

#### Paso 3: retropropagación en la salida

Como la salida es sigmoide y la pérdida es BCE:

$$
\delta^{[2]} = \hat{y} - y = 0.57483 - 1 = -0.42517
$$

Gradiente respecto a los pesos de salida:

$$
\frac{\partial \mathcal{L}}{\partial \mathbf{W}^{[2]}} = \delta^{[2]} (\mathbf{a}^{[1]})^T
$$

$$
\frac{\partial \mathcal{L}}{\partial \mathbf{W}^{[2]}} = -0.42517 \begin{bmatrix}0.52498 & 0.63414\end{bmatrix}
$$

$$
\frac{\partial \mathcal{L}}{\partial \mathbf{W}^{[2]}} \approx \begin{bmatrix}-0.22320 & -0.26962\end{bmatrix}
$$

Y para el sesgo:

$$
\frac{\partial \mathcal{L}}{\partial b^{[2]}} = \delta^{[2]} = -0.42517
$$

#### Paso 4: retropropagación a la capa oculta

Primero:

$$
(\mathbf{W}^{[2]})^T \delta^{[2]} = \begin{bmatrix}0.6 \\ -0.1\end{bmatrix}(-0.42517) = \begin{bmatrix}-0.25510 \\ 0.04252\end{bmatrix}
$$

Derivadas sigmoides en la capa oculta:

$$
\sigma'(0.1) = 0.52498(1-0.52498) \approx 0.24938
$$

$$
\sigma'(0.55) = 0.63414(1-0.63414) \approx 0.23201
$$

Por tanto:

$$
\boldsymbol{\delta}^{[1]} = \begin{bmatrix}-0.25510 \\ 0.04252\end{bmatrix} \odot \begin{bmatrix}0.24938 \\ 0.23201\end{bmatrix} \approx \begin{bmatrix}-0.06362 \\ 0.00986\end{bmatrix}
$$

Gradiente de los pesos de la capa 1:

$$
\frac{\partial \mathcal{L}}{\partial \mathbf{W}^{[1]}} = \boldsymbol{\delta}^{[1]} \mathbf{x}^T
$$

$$
\frac{\partial \mathcal{L}}{\partial \mathbf{W}^{[1]}} = \begin{bmatrix}-0.06362 \\ 0.00986\end{bmatrix} \begin{bmatrix}1 & 0.5\end{bmatrix}
$$

$$
\frac{\partial \mathcal{L}}{\partial \mathbf{W}^{[1]}} \approx \begin{bmatrix}
-0.06362 & -0.03181 \\
0.00986 & 0.00493
\end{bmatrix}
$$

Y el gradiente de los sesgos:

$$
\frac{\partial \mathcal{L}}{\partial \mathbf{b}^{[1]}} = \begin{bmatrix}-0.06362 \\ 0.00986\end{bmatrix}
$$

#### Paso 5: actualización por gradiente descendente

Con tasa de aprendizaje $\eta = 0.1$:

$$
\mathbf{W}^{[2]}_{\text{nuevo}} = \mathbf{W}^{[2]} - 0.1 \frac{\partial \mathcal{L}}{\partial \mathbf{W}^{[2]}} \approx \begin{bmatrix}0.62232 & -0.07304\end{bmatrix}
$$

$$
b^{[2]}_{\text{nuevo}} = 0.05 - 0.1(-0.42517) \approx 0.09252
$$

$$
\mathbf{W}^{[1]}_{\text{nuevo}} \approx \begin{bmatrix}
0.20636 & -0.39682 \\
0.69901 & 0.09951
\end{bmatrix}
$$

$$
\mathbf{b}^{[1]}_{\text{nuevo}} \approx \begin{bmatrix}0.10636 \\ -0.20099\end{bmatrix}
$$

**Conclusión del ejemplo:** la red ha ajustado sus pesos para aumentar la probabilidad de la clase correcta. Este mismo procedimiento, repetido sobre miles o millones de ejemplos, permite aprender tareas complejas de detección, clasificación o predicción en telecomunicaciones.

---

## 5.2 Receptores Neuronales

### 5.2.1 Definición y cambio de paradigma

Un **receptor neuronal** es un receptor de comunicaciones que utiliza redes neuronales para realizar una o varias funciones tradicionalmente resueltas con técnicas basadas en modelo: sincronización, estimación de canal, ecualización, demodulación, decodificación o decisión final.

El cambio de paradigma consiste en pasar de:

- **receptores basados en modelo**, que suponen ecuaciones explícitas del canal y del ruido,

a:

- **receptores basados en datos**, que aprenden la relación entre la señal recibida y los símbolos transmitidos a partir de ejemplos.

En el enfoque clásico, se parte de una ecuación como:

$$
\mathbf{r} = \mathbf{H}\mathbf{s} + \mathbf{n}
$$

mientras que en el enfoque neuronal se aprende una aplicación:

$$
\hat{\mathbf{p}} = g_{\theta}(\mathbf{r})
$$

con $g_{\theta}$ una red neuronal parametrizada por $\theta$ y $\hat{\mathbf{p}}$ la probabilidad de cada símbolo o bit.

### 5.2.2 Limitaciones de los métodos clásicos

Los métodos clásicos siguen siendo óptimos cuando sus hipótesis se cumplen. Sin embargo, en escenarios reales aparecen varias limitaciones.

#### a) Filtro adaptado y correlador

En un receptor coherente ideal, la decisión puede basarse en un correlador:

$$
y_k = \int_0^T r(t) s_k^*(t)\, dt
$$

La decisión ML en ruido blanco gaussiano aditivo (AWGN) y señales conocidas puede expresarse como:

$$
\hat{k} = \arg\max_k \Re\{y_k\}
$$

o, en forma equivalente,

$$
\hat{\mathbf{s}} = \arg\min_{\mathbf{s} \in \mathcal{S}} \|\mathbf{r} - \mathbf{H}\mathbf{s}\|_2^2
$$

#### b) Hipótesis implícitas

Estos métodos requieren, total o parcialmente:

- conocimiento preciso de $\mathbf{H}$;
- linealidad del canal;
- ruido con distribución conocida;
- sincronización razonablemente exacta;
- distorsiones de RF moderadas o modelables.

En la práctica, los sistemas pueden sufrir:

- no linealidades del amplificador de potencia;
- ruido impulsivo o no gaussiano;
- desajustes de fase y frecuencia;
- interferencia multiusuario compleja;
- hardware heterogéneo;
- canales altamente dinámicos.

Cuando los supuestos del modelo se alejan de la realidad, el rendimiento del receptor clásico puede degradarse significativamente.

### 5.2.3 Receptor neuronal para detección de señales

Un receptor neuronal para demodulación puede modelarse como un clasificador supervisado.

#### Representación de entrada

Si se reciben $N$ muestras complejas I/Q:

$$
\mathbf{r} = [r_1, r_2, \dots, r_N]^T, \qquad r_n \in \mathbb{C}
$$

una representación real habitual es:

$$
\mathbf{x} = [\Re(r_1), \Im(r_1), \Re(r_2), \Im(r_2), \dots, \Re(r_N), \Im(r_N)]^T
$$

Entonces la red produce probabilidades sobre los $M$ símbolos posibles:

$$
\hat{\mathbf{p}} = \mathrm{softmax}(f_{\theta}(\mathbf{x}))
$$

La decisión final es:

$$
\hat{m} = \arg\max_{i \in \{1,\dots,M\}} \hat{p}_i
$$

#### Arquitectura DNN típica

Una arquitectura simple para demodulación podría ser:

$$
\mathbf{a}^{[1]} = \mathrm{ReLU}(\mathbf{W}^{[1]}\mathbf{x}+\mathbf{b}^{[1]})
$$

$$
\mathbf{a}^{[2]} = \mathrm{ReLU}(\mathbf{W}^{[2]}\mathbf{a}^{[1]}+\mathbf{b}^{[2]})
$$

$$
\hat{\mathbf{p}} = \mathrm{softmax}(\mathbf{W}^{[3]}\mathbf{a}^{[2]}+\mathbf{b}^{[3]})
$$

La pérdida de entrenamiento es típicamente:

$$
\mathcal{L} = -\sum_{k=1}^{M} y_k \log(\hat{p}_k)
$$

En esencia, la red aprende fronteras de decisión en espacios de alta dimensión donde las regiones óptimas pueden ser muy complejas.

[Figura 5.3]: **Receptor neuronal para demodulación.** La figura debe mostrar una cadena con: símbolo transmitido, canal, ruido, muestras I/Q recibidas, preprocesamiento real-imaginario, red neuronal densa y salida softmax sobre la constelación. Debe remarcarse que el receptor ya no calcula explícitamente un estimador del canal y luego un detector separado, sino que aprende una transformación discriminativa directa desde datos. La descripción visual debe enfatizar el cambio de paradigma entre “bloques diseñados a mano” y “bloques aprendidos”.

### 5.2.4 Autoencoder como sistema de comunicación *end-to-end*

Una de las ideas más influyentes en aprendizaje profundo aplicado a capa física es modelar todo el enlace como un **autoencoder**.

- El transmisor es una red neuronal $f_{\theta_T}$.
- El canal es una capa no entrenable o parcialmente diferenciable $h(\cdot)$.
- El receptor es otra red neuronal $g_{\theta_R}$.

Si el mensaje discreto es $m \in \{1,2,\dots,M\}$, se representa mediante vector one-hot $\mathbf{e}_m$. El transmisor genera una palabra de código o señal:

$$
\mathbf{x} = f_{\theta_T}(\mathbf{e}_m)
$$

sujeta a una restricción de energía media:

$$
\frac{1}{n} \mathbb{E}[\|\mathbf{x}\|_2^2] \leq P
$$

El canal produce:

$$
\mathbf{r} = h(\mathbf{x})
$$

Por ejemplo, en AWGN:

$$
\mathbf{r} = \mathbf{x} + \mathbf{n}, \qquad \mathbf{n} \sim \mathcal{N}(0,\sigma^2 \mathbf{I})
$$

El receptor estima la distribución sobre mensajes:

$$
\hat{\mathbf{p}} = g_{\theta_R}(\mathbf{r})
$$

La pérdida es la entropía cruzada:

$$
\mathcal{L}(\theta_T,\theta_R) = -\sum_{m=1}^{M} \sum_{k=1}^{M} e_{m,k}\log \hat{p}_k
$$

La tasa de información por uso de canal es:

$$
R = \frac{\log_2 M}{n} \quad \text{bits/uso de canal}
$$

Este marco es poderoso porque permite **optimizar conjuntamente** representación, codificación y detección para un canal dado.

### 5.2.5 Entrenamiento y métricas de desempeño

#### a) Conjuntos de datos

En telecomunicaciones, los datos de entrenamiento pueden generarse por simulación o medirse experimentalmente. Suele dividirse en:

- **entrenamiento**: ajuste de parámetros;
- **validación**: selección de hiperparámetros y control de sobreajuste;
- **prueba**: estimación final de desempeño.

Una estrategia útil es muestrear varios valores de SNR durante el entrenamiento:

$$
\mathrm{SNR}_{\mathrm{dB}} \sim \mathcal{U}(\gamma_{\min}, \gamma_{\max})
$$

para mejorar robustez frente a diferentes condiciones de canal.

#### b) BER y SER

Las métricas clásicas siguen siendo centrales.

**Tasa de error de bit (BER):**

$$
\mathrm{BER} = \frac{N_{\mathrm{bits\ erróneos}}}{N_{\mathrm{bits\ transmitidos}}}
$$

**Tasa de error de símbolo (SER):**

$$
\mathrm{SER} = \frac{N_{\mathrm{símbolos\ erróneos}}}{N_{\mathrm{símbolos\ transmitidos}}}
$$

En aprendizaje supervisado también se monitorean:

- pérdida de entrenamiento;
- pérdida de validación;
- exactitud de clasificación;
- robustez fuera de distribución.

### 5.2.6 Comparación de rendimiento: receptor neuronal vs. clásico

No existe una respuesta universal. El rendimiento depende del escenario.

#### El receptor clásico suele ser preferible cuando:

- el modelo de canal es correcto;
- el canal es relativamente simple;
- la complejidad debe ser muy baja;
- se requiere interpretabilidad rigurosa;
- se dispone de estimación precisa del canal.

#### El receptor neuronal puede ser preferible cuando:

- el canal real es difícil de modelar;
- existen no linealidades importantes;
- se desea aprender directamente de datos medidos;
- la arquitectura hardware/software admite entrenamiento e inferencia;
- se busca adaptabilidad a escenarios heterogéneos.

Un criterio de comparación habitual es la BER en función de $E_b/N_0$ o SNR. Si para una BER objetivo de $10^{-3}$ el receptor neuronal necesita 1 dB menos que el clásico, se habla de una **ganancia de 1 dB** en ese punto operativo. Sin embargo, debe evaluarse también:

- complejidad computacional;
- consumo energético;
- tiempo de entrenamiento;
- capacidad de generalización.

### 5.2.7 Herramientas de implementación

#### a) TensorFlow

Ofrece:

- construcción declarativa de modelos;
- entrenamiento con GPU;
- exportación de modelos;
- integración con Keras.

Es útil para prototipos rápidos de receptores neuronales.

#### b) PyTorch

Muy usado en investigación por su flexibilidad y depuración intuitiva. Facilita:

- definición dinámica de grafos;
- experimentación con arquitecturas complejas;
- integración con bibliotecas científicas.

#### c) Sionna (NVIDIA)

Sionna es una biblioteca orientada a comunicaciones y aprendizaje automático. Resulta especialmente valiosa porque proporciona:

- módulos de canal diferenciables;
- componentes de capa física;
- simulación link-level;
- integración con TensorFlow;
- experimentos reproducibles de autoencoders y receptores neuronales.

En docencia e investigación, Sionna es útil para unir el mundo de las telecomunicaciones clásicas con el de las redes neuronales entrenables.

### 5.2.8 Ejemplos resueltos

**Ejemplo 5.2: demodulación neuronal de QPSK mediante softmax.**

Supongamos una modulación QPSK con mapeo Gray:

- clase 1 $\rightarrow 00$
- clase 2 $\rightarrow 01$
- clase 3 $\rightarrow 11$
- clase 4 $\rightarrow 10$

La capa de salida del receptor neuronal produce los logits:

$$
\mathbf{z} = [2.2,\ 1.0,\ 0.1,\ -0.5]^T
$$

Calculamos las probabilidades softmax.

Primero, exponenciales:

$$
e^{2.2} \approx 9.025, \quad e^{1.0} \approx 2.718, \quad e^{0.1} \approx 1.105, \quad e^{-0.5} \approx 0.607
$$

Suma total:

$$
S = 9.025 + 2.718 + 1.105 + 0.607 = 13.455
$$

Probabilidades:

$$
p_1 = \frac{9.025}{13.455} \approx 0.671
$$

$$
p_2 = \frac{2.718}{13.455} \approx 0.202
$$

$$
p_3 = \frac{1.105}{13.455} \approx 0.082
$$

$$
p_4 = \frac{0.607}{13.455} \approx 0.045
$$

Por tanto,

$$
\hat{\mathbf{p}} \approx [0.671,\ 0.202,\ 0.082,\ 0.045]^T
$$

La decisión es:

$$
\hat{m} = \arg\max_i p_i = 1
$$

Luego el receptor decide el símbolo asociado a los bits $00$.

Si la clase verdadera era la clase 1, la pérdida de entropía cruzada sería:

$$
\mathcal{L} = -\log(0.671) \approx 0.399
$$

Si la clase verdadera hubiera sido la clase 2, la pérdida sería mucho mayor:

$$
\mathcal{L} = -\log(0.202) \approx 1.599
$$

**Interpretación:** la red “confía” razonablemente en la clase 1, pero aún asigna una probabilidad apreciable a la clase 2; ello puede ser compatible con una muestra cercana a una frontera de decisión.

**Ejemplo 5.3: cálculo de BER de un receptor neuronal.**

Supongamos que se transmiten 5 símbolos QPSK, es decir, 10 bits. Los bits reales y estimados son:

- reales: $[0,0,\ 0,1,\ 1,1,\ 1,0,\ 0,1]$
- estimados: $[0,0,\ 0,1,\ 1,0,\ 1,0,\ 1,1]$

Comparamos bit a bit:

- símbolo 1: sin error;
- símbolo 2: sin error;
- símbolo 3: un error en el segundo bit;
- símbolo 4: sin error;
- símbolo 5: dos errores.

Total de errores:

$$
N_{\mathrm{err}} = 3
$$

Total de bits transmitidos:

$$
N_b = 10
$$

Entonces:

$$
\mathrm{BER} = \frac{3}{10} = 0.3
$$

Este valor es alto porque el conjunto es minúsculo; en evaluación real se requieren típicamente miles o millones de bits para obtener estimaciones estables de BER.

**Ejemplo 5.4: interpretación de un autoencoder de comunicaciones.**

Supongamos $M=16$ mensajes posibles y longitud de bloque $n=4$ usos de canal. La tasa es:

$$
R = \frac{\log_2(16)}{4} = \frac{4}{4} = 1 \text{ bit/uso de canal}
$$

Esto significa que el sistema neuronal puede aprender a representar 16 mensajes distintos usando vectores de dimensión 4, respetando la potencia. El transmisor aprende una constelación o código, y el receptor aprende la regla de decisión asociada. En esencia, el sistema descubre automáticamente una estrategia de modulación-codificación adaptada al canal incluido durante el entrenamiento.

---

## 5.3 IA Nativa en Redes 6G (IMT-2030)

### 5.3.1 Visión de 6G e IMT-2030

La visión IMT-2030 propone una evolución más profunda que un simple aumento de tasa binaria. El objetivo es integrar comunicaciones, inteligencia, sensado, automatización y servicios inmersivos en una infraestructura ubicua, eficiente y adaptable.

Entre los ejes habitualmente destacados en la visión 6G se encuentran:

- **comunicación inmersiva**;
- **conectividad ubicua**;
- **ultra baja latencia y alta fiabilidad**;
- **integración de IA en la red**;
- **sensado y comunicación integrados (ISAC)**;
- **sostenibilidad energética**.

#### KPIs representativos

La literatura y los documentos de estandarización suelen discutir indicadores como:

- tasa pico;
- tasa experimentada por el usuario;
- latencia extremo a extremo;
- fiabilidad;
- densidad de conexión;
- eficiencia energética;
- eficiencia espectral;
- movilidad soportada;
- precisión de posicionamiento;
- inteligencia distribuida.

Un KPI puede expresarse, por ejemplo, como restricción de latencia:

$$
T_{\mathrm{e2e}} \leq T_{\max}
$$

fiabilidad mínima:

$$
\Pr\{\text{éxito}\} \geq 1-\varepsilon
$$

energía por bit:

$$
E_b = \frac{P}{R_b}
$$

con $P$ potencia consumida y $R_b$ tasa binaria.

### 5.3.2 Arquitectura AI-nativa

Decir que una red es **AI-nativa** significa que la IA no es un accesorio externo, sino una función integrada en múltiples planos y capas de la red:

- capa física;
- capa MAC y radio resource management;
- core de red;
- orquestación de servicios;
- operación, mantenimiento y automatización;
- borde y terminales.

Conceptualmente, una arquitectura AI-nativa incluye:

1. **observabilidad**: recolección de datos de red, radio, tráfico, contexto y usuario;
2. **plano de datos para IA**: almacenamiento, etiquetado y curación;
3. **entrenamiento**: centralizado, federado o híbrido;
4. **inferencia**: en nube, borde o dispositivo;
5. **retroalimentación**: adaptación cerrada de la red.

Si el estado de red es $s_t$, la acción de control es $a_t$ y el desempeño es $r_t$, la IA busca una política:

$$
a_t = \pi_\theta(s_t)
$$

que maximice utilidad acumulada, por ejemplo:

$$
J(\pi_\theta) = \mathbb{E}\left[\sum_{t=0}^{\infty} \gamma^t r_t\right]
$$

Esto conecta naturalmente la operación de red con el aprendizaje por refuerzo.

[Figura 5.4]: **Arquitectura AI-nativa de red 6G.** La figura debe representar capas de red y, superpuesto a ellas, un plano de inteligencia transversal. Deben aparecer fuentes de datos (RAN, core, terminales, sensado), un repositorio o *data fabric*, módulos de entrenamiento, un registro de modelos, inferencia distribuida en nube y borde, y lazos de control cerrados hacia la gestión de recursos. La idea visual central es que la IA ya no se añade “al final”, sino que atraviesa todo el ciclo de vida operativo de la red.

### 5.3.3 AI/ML como función nativa de red

En una red AI-nativa, AI/ML puede ofrecerse como **servicio interno de red**: entrenamiento, distribución de modelos, inferencia, monitorización y actualización.

Podemos pensar en una función de red de IA que implementa:

$$
\mathcal{F}_{\mathrm{AI}}: (\text{datos},\ \text{contexto},\ \text{políticas}) \mapsto (\text{predicciones},\ \text{acciones},\ \text{modelos})
$$

Esto permite casos como:

- predicción de congestión;
- selección de haz (*beam selection*);
- control energético;
- clasificación de tráfico;
- compresión semántica;
- transferencia de modelos AI/ML entre nodos de red.

Desde una perspectiva de ingeniería, esto exige:

- interfaces estándar para modelos;
- métricas de rendimiento y deriva;
- seguridad y trazabilidad;
- gestión de versiones;
- orquestación de inferencia.

### 5.3.4 Computación distribuida y Edge AI

#### Motivación: latencia, privacidad y eficiencia

Enviar todos los datos a la nube introduce coste de transporte, latencia y riesgo de privacidad. Si una decisión debe tomarse cerca del usuario, conviene desplazar la inferencia al borde.

La latencia extremo a extremo puede descomponerse como:

$$
T_{\mathrm{total}} = T_{\mathrm{uplink}} + T_{\mathrm{transporte}} + T_{\mathrm{cola}} + T_{\mathrm{cómputo}} + T_{\mathrm{downlink}}
$$

Cuando la inferencia se realiza en el borde, el término $T_{\mathrm{transporte}}$ puede reducirse drásticamente.

#### Edge computing y MEC

**Mobile Edge Computing (MEC)** sitúa capacidades de cómputo cerca de la RAN o del acceso. Esto permite:

- inferencia rápida para servicios sensibles a latencia;
- procesamiento local de datos sensibles;
- reducción del tráfico hacia nube central;
- adaptación contextual por celda, zona o microservicio.

#### Inferencia en el borde

Si una tarea de inferencia requiere $C$ operaciones y el nodo edge ofrece $f_{\mathrm{edge}}$ operaciones por segundo, el tiempo ideal de cómputo es aproximadamente:

$$
T_{\mathrm{inf}} \approx \frac{C}{f_{\mathrm{edge}}}
$$

Sin embargo, en la práctica deben añadirse costes de memoria, acceso a parámetros, colas y virtualización.

**Ejemplo 5.5: latencia nube vs. borde.**

Supongamos dos opciones para inferencia de un modelo de control radio:

- en nube: $T_{\mathrm{uplink}}=5$ ms, $T_{\mathrm{transporte}}=10$ ms, $T_{\mathrm{cómputo}}=25$ ms, $T_{\mathrm{downlink}}=15$ ms;
- en edge: $T_{\mathrm{uplink}}=3$ ms, $T_{\mathrm{transporte}}=0$ ms, $T_{\mathrm{cómputo}}=8$ ms, $T_{\mathrm{downlink}}=3$ ms.

Latencia en nube:

$$
T_{\mathrm{cloud}} = 5 + 10 + 25 + 15 = 55\ \text{ms}
$$

Latencia en borde:

$$
T_{\mathrm{edge}} = 3 + 0 + 8 + 3 = 14\ \text{ms}
$$

La reducción es:

$$
\Delta T = 55 - 14 = 41\ \text{ms}
$$

Esto ilustra por qué Edge AI es esencial en aplicaciones URLLC, control industrial, XR y sensado cooperativo.

### 5.3.5 Técnicas de aprendizaje distribuido

#### a) Aprendizaje federado (*Federated Learning, FL*)

El aprendizaje federado entrena un modelo global sin mover los datos crudos fuera de cada cliente. Cada nodo local optimiza sus parámetros y solo comparte actualizaciones o pesos.

##### Formulación

Si el nodo $k$ tiene función de pérdida local $F_k(\theta)$ y $n_k$ muestras, el objetivo global es:

$$
F(\theta) = \sum_{k=1}^{K} \frac{n_k}{N} F_k(\theta), \qquad N = \sum_{k=1}^{K} n_k
$$

##### Algoritmo FedAvg

En la ronda global $t$, el servidor distribuye $\theta^{(t)}$ a nodos seleccionados. Cada nodo realiza $E$ pasos locales:

$$
\theta_k^{(t,e+1)} = \theta_k^{(t,e)} - \eta \nabla F_k\big(\theta_k^{(t,e)}\big)
$$

con condición inicial:

$$
\theta_k^{(t,0)} = \theta^{(t)}
$$

Tras $E$ pasos, el servidor agrega:

$$
\theta^{(t+1)} = \sum_{k=1}^{K} \frac{n_k}{N} \theta_k^{(t,E)}
$$

##### Privacidad

FL mejora privacidad porque los datos permanecen locales, pero **no garantiza privacidad perfecta**. Las actualizaciones pueden filtrar información. Por eso suelen añadirse técnicas como:

- privacidad diferencial;
- agregación segura;
- cifrado homomórfico parcial.

**Ejemplo 5.6: una ronda de FedAvg.**

Modelo escalar inicial:

$$
\theta^{(0)} = 1.0
$$

Dos clientes:

- cliente 1: $n_1=60$, gradiente local $g_1=0.8$;
- cliente 2: $n_2=40$, gradiente local $g_2=-0.2$.

Supongamos un solo paso local con $\eta=0.5$.

Cliente 1:

$$
\theta_1 = 1.0 - 0.5(0.8) = 0.6
$$

Cliente 2:

$$
\theta_2 = 1.0 - 0.5(-0.2) = 1.1
$$

Agregación ponderada:

$$
\theta^{(1)} = \frac{60}{100}(0.6) + \frac{40}{100}(1.1)
$$

$$
\theta^{(1)} = 0.36 + 0.44 = 0.80
$$

**Interpretación:** el modelo global se desplaza hacia la preferencia del cliente 1 porque posee más datos.

[Figura 5.5]: **Aprendizaje federado en red móvil.** La figura debe incluir varios dispositivos o estaciones con datos locales, un servidor agregador y rondas de comunicación. Debe verse que los datos no se envían, sino los parámetros o gradientes. Conviene añadir flechas de ida y vuelta para representar la distribución del modelo global y la recolección de actualizaciones locales. La figura debe resaltar el equilibrio entre aprendizaje colaborativo, privacidad y coste de comunicación.

#### b) Split Learning

En **Split Learning**, la red neuronal se divide entre cliente y servidor. Si la red se corta en la capa $c$:

- el cliente computa las capas $1$ a $c$,
- el servidor computa las capas $c+1$ a $L$.

Si $\mathbf{x}$ es la entrada local, el cliente produce una representación intermedia o *smashed data*:

$$
\mathbf{h}^{[c]} = f_{\theta_{1:c}}(\mathbf{x})
$$

El servidor continúa:

$$
\hat{\mathbf{y}} = g_{\theta_{c+1:L}}(\mathbf{h}^{[c]})
$$

Durante retropropagación, el servidor devuelve:

$$
\frac{\partial \mathcal{L}}{\partial \mathbf{h}^{[c]}}
$$

para que el cliente actualice sus capas iniciales.

**Ventaja:** el cliente necesita menos cómputo que en FL.

**Desafío:** la representación intermedia puede aún revelar información y el entrenamiento requiere sincronización estrecha.

#### c) Aprendizaje por refuerzo distribuido

En redes 6G, múltiples agentes pueden aprender políticas para control de recursos, movilidad, selección de haz o coordinación edge-cloud.

El retorno esperado de una política $\pi_\phi$ es:

$$
J(\phi) = \mathbb{E}_{\pi_\phi}\left[\sum_{t=0}^{\infty} \gamma^t r_t\right]
$$

Una forma general del gradiente de política es:

$$
\nabla_\phi J(\phi) = \mathbb{E}_{\pi_\phi}\left[\sum_t \nabla_\phi \log \pi_\phi(a_t|s_t)\, \hat{A}_t\right]
$$

con $\hat{A}_t$ una estimación de ventaja. En versión distribuida, múltiples agentes recopilan experiencias en paralelo y actualizan un modelo compartido o coordinado.

### 5.3.6 Edge Large AI Models (Edge LAMs)

#### Modelos grandes en el borde

Los **Edge LAMs** son modelos de gran capacidad —por ejemplo, modelos de lenguaje o modelos multimodales— desplegados parcial o totalmente en nodos de borde. Su atractivo en telecomunicaciones incluye:

- asistentes locales de red;
- comprensión semántica de tráfico o señalización;
- operación autónoma de nodos;
- soporte a gemelos digitales y automatización.

Sin embargo, el despliegue de modelos grandes está limitado por memoria, consumo energético y latencia.

#### a) *Pruning*

El *pruning* elimina pesos poco relevantes. Si $\theta \in \mathbb{R}^d$ y $\mathbf{m} \in \{0,1\}^d$ es una máscara binaria:

$$
\theta_{\mathrm{pruned}} = \mathbf{m} \odot \theta
$$

con restricción:

$$
\|\mathbf{m}\|_0 \leq K
$$

El objetivo es conservar solo $K$ parámetros efectivos.

#### b) Cuantización

La cuantización reduce la precisión numérica. Para un peso $w$ y paso de cuantización $\Delta$:

$$
q = \mathrm{round}\left(\frac{w}{\Delta}\right), \qquad \hat{w} = \Delta q
$$

Esto reduce memoria y acelera inferencia en hardware especializado.

#### c) Destilación de conocimiento

Un modelo grande (*teacher*) transfiere conocimiento a un modelo pequeño (*student*). Una pérdida típica es:

$$
\mathcal{L} = \alpha T^2\, \mathrm{KL}\left(\sigma\left(\frac{\mathbf{z}_T}{T}\right) \Bigg\| \sigma\left(\frac{\mathbf{z}_S}{T}\right)\right) + (1-\alpha)\, \mathrm{CE}(\mathbf{y}, \sigma(\mathbf{z}_S))
$$

Aquí:

- $T$ es la temperatura;
- $\mathbf{z}_T$ son logits del teacher;
- $\mathbf{z}_S$ son logits del student.

#### Desafíos de despliegue

- memoria limitada;
- consumo de energía;
- latencia estricta;
- heterogeneidad de hardware;
- actualización segura y frecuente;
- robustez ante deriva de datos;
- coste de comunicación si el modelo se reparte entre borde y nube.

### 5.3.7 Sinergias con Gemelos Digitales e ISAC

#### a) Gemelos digitales (*Digital Twins*)

Un gemelo digital es una representación virtual, dinámica y sincronizada de un sistema físico. En redes, puede modelar:

- topología;
- tráfico;
- movilidad;
- canales radio;
- consumo energético;
- comportamiento de nodos.

Si el estado físico es $\mathbf{x}(t)$, el gemelo intenta mantener una estimación $\hat{\mathbf{x}}(t)$ tal que:

$$
\hat{\mathbf{x}}(t+1) = f_\psi\big(\hat{\mathbf{x}}(t), \mathbf{u}(t), \mathbf{y}(t)\big)
$$

con:

- $\mathbf{u}(t)$ acciones o controles,
- $\mathbf{y}(t)$ observaciones,
- $f_\psi$ un modelo del gemelo.

La IA permite calibrar el gemelo, predecir estados futuros y optimizar acciones antes de desplegarlas en la red real.

#### b) ISAC (*Integrated Sensing and Communication*)

ISAC integra en una misma infraestructura funciones de comunicación y sensado. Un mismo recurso radio puede transportar información a usuarios y, simultáneamente, extraer información del entorno.

Un modelo simplificado distingue:

- señal de comunicación recibida:

$$
\mathbf{y}_c = \mathbf{H}_c \mathbf{x} + \mathbf{n}_c
$$

- eco o señal de sensado:

$$
\mathbf{y}_s = \mathbf{H}_s \mathbf{x} + \mathbf{n}_s
$$

El diseño de la señal $\mathbf{x}$ y de los receptores asociados debe equilibrar métricas de ambas funciones.

Una formulación genérica multiobjetivo es:

$$
\max_{\mathbf{x},\,\pi} \ \lambda R(\mathbf{x},\pi) + (1-\lambda) S(\mathbf{x},\pi)
$$

sujeto a:

$$
\|\mathbf{x}\|_2^2 \leq P
$$

Aquí:

- $R(\cdot)$ representa utilidad de comunicación (tasa, BER, cobertura);
- $S(\cdot)$ representa utilidad de sensado (resolución, detección, localización);
- $\lambda \in [0,1]$ controla el compromiso.

#### c) Convergencia IA + Digital Twins + ISAC

La convergencia de estas tres ideas es una de las apuestas más fuertes de 6G:

- **IA** aprende políticas y modelos;
- **gemelos digitales** permiten probar y anticipar decisiones;
- **ISAC** proporciona observabilidad rica del entorno.

Un bucle conceptual sería:

1. ISAC genera observaciones del entorno y de la red.
2. El gemelo digital se actualiza con esas observaciones.
3. La IA optimiza acciones sobre el gemelo.
4. Las acciones validadas se transfieren a la red real.
5. La red produce nuevos datos y el ciclo continúa.

Matemáticamente, si $\mathbf{o}_t$ es la observación ISAC, el gemelo produce estado inferido $\hat{\mathbf{x}}_t$, y la IA decide $\mathbf{u}_t$:

$$
\hat{\mathbf{x}}_t = \mathcal{T}(\hat{\mathbf{x}}_{t-1}, \mathbf{o}_t)
$$

$$
\mathbf{u}_t = \pi_\theta(\hat{\mathbf{x}}_t)
$$

$$
\mathbf{o}_{t+1} \sim p(\mathbf{o}_{t+1}|\mathbf{u}_t, \text{sistema real})
$$

Esto configura un sistema ciberfísico cerrado basado en datos.

[Figura 5.6]: **Convergencia IA + Gemelo Digital + ISAC.** La figura debe mostrar tres bloques principales: la red física real, el gemelo digital y un motor de IA. Desde la red física deben salir datos de comunicación y sensado hacia el gemelo; desde el gemelo deben pasar estados simulados, predicciones y métricas hacia el motor de IA; y desde el motor de IA deben retornar políticas y configuraciones a la red. La utilidad pedagógica de la figura está en mostrar que 6G no solo comunica datos, sino que también observa, modela, predice y actúa.

### 5.3.8 Ejemplos y casos de estudio

**Ejemplo 5.7: optimización multiobjetivo en ISAC.**

Supongamos que una configuración radio produce utilidad de comunicación $R=8$ unidades y utilidad de sensado $S=5$ unidades. Si el operador fija $\lambda = 0.7$, la utilidad total es:

$$
U = \lambda R + (1-\lambda)S
$$

$$
U = 0.7(8) + 0.3(5) = 5.6 + 1.5 = 7.1
$$

Otra configuración produce $R=7$ y $S=7$:

$$
U' = 0.7(7) + 0.3(7) = 7
$$

Con $\lambda=0.7$, la primera configuración es preferible porque prioriza comunicación. Si el operador redujera $\lambda$, la segunda podría resultar mejor. Este ejemplo muestra que ISAC es intrínsecamente un problema de compromiso entre objetivos.

**Ejemplo 5.8: papel de un gemelo digital en una red móvil.**

Supongamos que la carga media de tres celdas en el instante $t$ es:

$$
\mathbf{x}(t) = [0.8,\ 0.6,\ 0.4]
$$

expresada como fracción de utilización. El gemelo digital predice para el siguiente intervalo:

$$
\hat{\mathbf{x}}(t+1) = [0.9,\ 0.65,\ 0.5]
$$

La IA de control decide descargar tráfico de la celda 1 a la celda 3, aplicando una acción:

$$
\mathbf{u}(t) = [-0.1,\ 0,\ +0.1]
$$

Si el gemelo estima que el nuevo estado será:

$$
\hat{\mathbf{x}}'(t+1) = [0.8,\ 0.65,\ 0.6]
$$

entonces la acción reduce el riesgo de congestión en la celda 1 antes de aplicarse en la red real. Este es precisamente el valor de un gemelo digital: experimentar de forma segura antes de actuar.

**Caso de estudio 5.1: Edge AI para selección de haz en 6G.**

En bandas milimétricas o sub-THz, la selección de haz es crítica. Un modelo de IA en el borde puede recibir características como posición, historial de CSI, mapas del entorno y medidas ISAC. Sea $\mathbf{f}$ el vector de características, el modelo predice el haz óptimo:

$$
\hat{b} = \arg\max_{b \in \mathcal{B}} p(b|\mathbf{f})
$$

Si la inferencia se hace en edge, la decisión puede tomarse en milisegundos, mejorando movilidad y robustez frente a bloqueo.

**Caso de estudio 5.2: FL para optimización energética de estaciones base.**

Varias estaciones base aprenden localmente una política de apagado parcial de recursos en horas valle. Cada estación observa tráfico local, clima, movilidad y eventos. FL permite entrenar un modelo común sin compartir datos operacionales sensibles. La función objetivo podría combinar ahorro energético y QoS:

$$
J = \alpha \cdot \mathrm{Ahorro\ energético} - \beta \cdot \mathrm{Penalización\ QoS}
$$

La IA federada aprende una política global, mientras cada sitio mantiene la privacidad de su telemetría.

**Caso de estudio 5.3: receptor neuronal y red AI-nativa.**

Una visión coherente de 6G integra los temas de esta unidad: un receptor neuronal aprende la detección robusta bajo imperfecciones de hardware; sus parámetros se actualizan federadamente desde múltiples nodos; un gemelo digital reproduce el comportamiento del enlace; y módulos ISAC aportan contexto del entorno. Así, la capa física y la capa de red dejan de ser compartimentos estancos y pasan a formar un ecosistema inteligente unificado.

---

## Resumen de conceptos clave

- Una red neuronal implementa una composición de transformaciones lineales y no lineales:

$$
\mathbf{a}^{[l]} = f^{[l]}(\mathbf{W}^{[l]}\mathbf{a}^{[l-1]} + \mathbf{b}^{[l]})
$$

- La pérdida cuantifica el error entre predicción y verdad de referencia; en clasificación destacan BCE y entropía cruzada.
- La retropropagación aplica sistemáticamente la regla de la cadena para obtener gradientes.
- El descenso del gradiente y variantes como Adam permiten entrenar la red.
- En telecomunicaciones, un receptor neuronal aprende a detectar símbolos o bits directamente desde muestras recibidas.
- Los autoencoders modelan el sistema transmisor-canal-receptor como una arquitectura entrenable end-to-end.
- El desempeño de receptores neuronales debe evaluarse con métricas clásicas como BER y SER, no solo con pérdida de entrenamiento.
- En 6G, la IA será una capacidad nativa de red, distribuida entre nube, borde y dispositivos.
- Técnicas como FL, Split Learning y RL distribuido son esenciales para entrenar inteligencia sin centralizar todos los datos.
- Los Edge Large AI Models requieren compresión, cuantización y despliegue eficiente.
- La convergencia entre IA, gemelos digitales e ISAC promete redes capaces de comunicar, observar, simular, predecir y actuar en lazo cerrado.

---

## Referencias

1. I. Goodfellow, Y. Bengio y A. Courville, *Deep Learning*. MIT Press, 2016. Disponible en: https://www.deeplearningbook.org/  
2. International Telecommunication Union, Radiocommunication Sector, **Recommendation ITU-R M.2160-0**: *Framework and overall objectives of the future development of IMT for 2030 and beyond*, 2023. Sin DOI. Disponible en: https://www.itu.int/rec/R-REC-M.2160/en  
3. 3rd Generation Partnership Project (3GPP), **TR 22.874**: *5G System (5GS); Study on traffic characteristics and performance requirements for AI/ML model transfer*, Release 18, 2021. Sin DOI. Disponible en: https://www.3gpp.org/ftp/Specs/archive/22_series/22.874/  
4. T. J. O'Shea y J. Hoydis, “An Introduction to Deep Learning for the Physical Layer,” *IEEE Transactions on Cognitive Communications and Networking*, vol. 3, no. 4, pp. 563-575, 2017. DOI: $10.1109/TCCN.2017.2758370$.  
5. U. Challita, H. Ryden, H. Tullberg y otros, “When Machine Learning Meets Wireless Cellular Networks: Deployment, Challenges, and Applications,” *IEEE Communications Magazine*, vol. 58, no. 6, pp. 12-18, 2020. DOI: $10.1109/MCOM.001.1900664$.  
6. Y. Xiao, G. Shi, Y. Li, W. Saad y H. V. Poor, “Toward Self-Learning Edge Intelligence in 6G,” *IEEE Communications Magazine*, vol. 58, no. 12, pp. 34-40, 2020. DOI: $10.1109/MCOM.001.2000388$.  
7. C. Zhang, Y. Huang, Z. Yang, Y. Chen, C. Yuen y M. Debbah, “Edge Artificial Intelligence for 6G: Vision, Enabling Technologies, and Applications,” *IEEE Journal on Selected Areas in Communications*, vol. 40, no. 1, pp. 5-36, 2022. DOI: $10.1109/JSAC.2021.3126062$.  
8. M. Al-Quraan, L. Mohjazi, L. Bariah y otros, “Edge-Native Intelligence for 6G Communications Driven by Federated Learning: A Survey of Trends and Challenges,” *IEEE Transactions on Emerging Topics in Computational Intelligence*, vol. 7, no. 3, pp. 957-979, 2023. DOI: $10.1109/TETCI.2023.3251404$.  
9. A. Alkhateeb, Y. Jiang y H. Wymeersch, “Real-Time Digital Twins: Vision and Research Directions for 6G and Beyond,” *IEEE Communications Magazine*, vol. 61, no. 11, 2023. DOI: $10.1109/MCOM.001.2300134$.  
10. F. Liu, Y.-F. Liu, A. Li, C. Masouros, Y. C. Eldar y S. Cui, “Integrated Sensing and Communications: Toward Dual-Functional Wireless Networks for 6G and Beyond,” *IEEE Journal on Selected Areas in Communications*, vol. 40, no. 6, pp. 1728-1767, 2022. DOI: $10.1109/JSAC.2022.3156632$.  
