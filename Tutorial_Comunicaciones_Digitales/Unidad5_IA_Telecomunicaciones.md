# Unidad 5: Introducción a la IA en Telecomunicaciones

## Introducción de la unidad

La inteligencia artificial (IA) ha pasado de ser una herramienta auxiliar a convertirse en un **componente estructural** de los sistemas modernos de telecomunicaciones. En generaciones previas, el diseño de enlaces y redes se apoyaba principalmente en modelos explícitos: canal lineal, ruido gaussiano, sincronización ideal, estimación separada y decisiones óptimas bajo hipótesis bien definidas. Ese enfoque sigue siendo fundamental, pero empieza a mostrar límites cuando el sistema real presenta **no linealidades, movilidad extrema, heterogeneidad de servicios, datos multimodales y necesidad de adaptación en tiempo real**.

En este contexto, la IA y el aprendizaje automático permiten aprender relaciones complejas directamente a partir de datos, construir receptores más robustos, optimizar recursos de red, mover inteligencia al borde y, en la visión 6G, diseñar una **arquitectura AI-nativa** en la que la comunicación y la inteligencia coevolucionan. Esta unidad introduce, con enfoque pedagógico y matemático, cuatro pilares:

1. fundamentos de redes neuronales;
2. receptores neuronales para procesamiento de señales;
3. integración de IA en redes 6G e IMT-2030;
4. comunicaciones semánticas y sistemas de próxima generación.

El objetivo es que el lector comprenda no solo *qué* hace la IA en telecomunicaciones, sino también *cómo* se modela, *por qué* funciona, *cuáles son sus límites* y *por qué la semántica será probablemente una dimensión central de 6G y de sistemas posteriores*.

> **Concepto clave:** Shannon resolvió brillantemente el problema de transmitir símbolos con fiabilidad, pero las redes futuras también deberán decidir **qué significado merece ser transmitido**, **con qué fidelidad semántica** y **para qué tarea final**.

---

## 5.1 Conceptos Básicos de Redes Neuronales

### 5.1.1 Arquitectura de la neurona artificial

La neurona artificial abstrae el comportamiento de una neurona biológica: recibe entradas, las pondera, suma un sesgo y produce una salida no lineal. La forma general es:

$$
y = f\left(\sum_{i=1}^{n} w_i x_i + b\right)
$$

donde:

- $x_i$ son las entradas;
- $w_i$ son los pesos sinápticos;
- $b$ es el sesgo (*bias*);
- $f(\cdot)$ es la función de activación;
- $y$ es la salida.

En forma vectorial:

$$
y = f(\mathbf{w}^T\mathbf{x} + b)
$$

con $\mathbf{x} \in \mathbb{R}^n$ y $\mathbf{w} \in \mathbb{R}^n$.

#### a) Modelo de McCulloch-Pitts

El modelo de McCulloch-Pitts es un precursor lógico de la neurona artificial. Se basa en una suma ponderada y una activación umbral:

$$
y = \begin{cases}
1, & \text{si } \sum_i w_i x_i \geq \theta \\
0, & \text{si } \sum_i w_i x_i < \theta
\end{cases}
$$

Aquí $\theta$ es un umbral. Este modelo implementa funciones lógicas simples, pero no permite entrenamiento diferencial porque la activación es no derivable.

#### b) Perceptrón

El perceptrón reemplaza el umbral fijo por un sesgo $b=-\theta$:

$$
y = \phi(\mathbf{w}^T\mathbf{x}+b)
$$

con función escalón:

$$
\phi(z)=\begin{cases}
1, & z\geq 0 \\
0, & z<0
\end{cases}
$$

El perceptrón aprende un hiperplano separador. Si los datos son linealmente separables, existe un conjunto de pesos que clasifica correctamente las muestras.

#### c) Regla de aprendizaje del perceptrón

Si la salida deseada es $d \in \{0,1\}$ y la salida predicha es $y$, una actualización elemental es:

$$
\mathbf{w}_{t+1}=\mathbf{w}_t + \eta (d-y)\mathbf{x}
$$

$$
b_{t+1}=b_t + \eta (d-y)
$$

con $\eta$ la tasa de aprendizaje. Esta regla ilustra la idea central de aprendizaje: **ajustar parámetros para reducir error**.

> **Concepto clave:** una red neuronal no “entiende” símbolos como un humano; aprende una función $f_\theta(\cdot)$ que aproxima una relación entrada-salida útil para detección, clasificación, predicción o control.

### 5.1.2 Funciones de activación

La activación introduce no linealidad. Sin ella, una red multicapa colapsaría en una sola transformación lineal.

**Sigmoide**:

$$
\sigma(z)=\frac{1}{1+e^{-z}}
$$

Derivada:

$$
\sigma'(z)=\sigma(z)(1-\sigma(z))
$$

Se usa en salidas binarias o interpretación probabilística, aunque puede sufrir desvanecimiento del gradiente cuando $|z|$ es grande.

**Tangente hiperbólica**:

$$
\tanh(z)=\frac{e^z-e^{-z}}{e^z+e^{-z}}
$$

Derivada:

$$
\frac{d}{dz}\tanh(z)=1-\tanh^2(z)
$$

**ReLU**:

$$
\mathrm{ReLU}(z)=\max(0,z)
$$

Derivada idealizada:

$$
\mathrm{ReLU}'(z)=\begin{cases}
1, & z>0 \\
0, & z<0
\end{cases}
$$

**Leaky ReLU**:

$$
\mathrm{LReLU}(z)=\begin{cases}
z, & z\geq 0 \\
\alpha z, & z<0
\end{cases}
$$

con $0<\alpha\ll 1$.

**Softmax** para clasificación multiclase:

$$
\hat{y}_k = \frac{e^{z_k}}{\sum_{j=1}^{K} e^{z_j}}, \qquad k=1,\dots,K
$$

La suma de probabilidades satisface:

$$
\sum_{k=1}^{K} \hat{y}_k = 1
$$

En telecomunicaciones, esta salida es natural cuando la red debe decidir entre símbolos, órdenes de modulación, usuarios, haces (*beams*) o estados discretos del canal.

### 5.1.3 Red neuronal multicapa

Una red multicapa (*Multilayer Perceptron, MLP*) compone varias capas de transformaciones afines y no lineales. Para la capa $l$:

$$
\mathbf{z}^{[l]}=\mathbf{W}^{[l]}\mathbf{a}^{[l-1]}+\mathbf{b}^{[l]}
$$

$$
\mathbf{a}^{[l]}=f^{[l]}(\mathbf{z}^{[l]})
$$

con $\mathbf{a}^{[0]}=\mathbf{x}$.

Para una red de $L$ capas:

$$
\hat{\mathbf{y}} = f^{[L]}\Big(\mathbf{W}^{[L]} f^{[L-1]}(\cdots f^{[1]}(\mathbf{W}^{[1]}\mathbf{x}+\mathbf{b}^{[1]})\cdots)+\mathbf{b}^{[L]}\Big)
$$

En telecomunicaciones, estas capas pueden recibir como entrada:

- muestras I/Q;
- estimaciones CSI;
- mapas de potencia;
- medidas de interferencia;
- historiales temporales;
- contexto de red o movilidad.

[Figura 5.1]: **Neurona artificial y red multicapa aplicada a telecomunicaciones.** La figura debe mostrar una neurona elemental con entradas $x_1,\dots,x_n$, pesos $w_1,\dots,w_n$, sesgo $b$ y salida $y=f(\mathbf{w}^T\mathbf{x}+b)$. A continuación, debe ampliarse a una red multicapa con capa de entrada, una o dos capas ocultas y una capa de salida. Se recomienda añadir ejemplos de variables de entrada típicas en telecomunicaciones: muestras I/Q, SNR estimada, coeficientes de canal o estado de red. La finalidad pedagógica es conectar la abstracción matemática con aplicaciones reales del dominio.

### 5.1.4 Función de pérdida

La red aprende minimizando una función de pérdida $\mathcal{L}$.

#### a) Error cuadrático medio (MSE)

Para regresión:

$$
\mathcal{L}_{\mathrm{MSE}}=\frac{1}{m}\sum_{i=1}^{m}(y_i-\hat{y}_i)^2
$$

#### b) Entropía cruzada binaria (BCE)

Para clasificación binaria:

$$
\mathcal{L}_{\mathrm{BCE}}=-\frac{1}{m}\sum_{i=1}^{m}\left[y_i\log(\hat{y}_i)+(1-y_i)\log(1-\hat{y}_i)\right]
$$

#### c) Entropía cruzada multiclase

$$
\mathcal{L}_{\mathrm{CE}}=-\frac{1}{m}\sum_{i=1}^{m}\sum_{k=1}^{K} y_{ik}\log(\hat{y}_{ik})
$$

Si $\mathbf{y}_i$ es *one-hot*, solo contribuye la probabilidad asignada a la clase correcta.

#### d) Regularización

Para evitar sobreajuste se añade, por ejemplo, penalización $L_2$:

$$
\mathcal{L}_{\mathrm{reg}} = \mathcal{L} + \lambda \sum_{l=1}^{L} \|\mathbf{W}^{[l]}\|_F^2
$$

con $\lambda>0$ un hiperparámetro.

> **Concepto clave:** en problemas de telecomunicaciones, una pérdida pequeña en entrenamiento no basta; la red debe generalizar frente a variaciones de canal, SNR, interferencia, movilidad y hardware.

### 5.1.5 Propagación hacia atrás (*backpropagation*)

La retropropagación calcula gradientes de la pérdida respecto a todos los parámetros usando la regla de la cadena.

Sea una red con pérdida $\mathcal{L}$. Queremos calcular:

$$
\frac{\partial \mathcal{L}}{\partial \mathbf{W}^{[l]}}, \qquad \frac{\partial \mathcal{L}}{\partial \mathbf{b}^{[l]}}
$$

#### Paso 1: error en la capa de salida

Definimos:

$$
\boldsymbol{\delta}^{[L]} = \frac{\partial \mathcal{L}}{\partial \mathbf{z}^{[L]}}
$$

Como $\mathbf{a}^{[L]}=f^{[L]}(\mathbf{z}^{[L]})$, entonces:

$$
\boldsymbol{\delta}^{[L]} = \frac{\partial \mathcal{L}}{\partial \mathbf{a}^{[L]}} \odot f'^{[L]}(\mathbf{z}^{[L]})
$$

Para salida softmax con entropía cruzada:

$$
\boldsymbol{\delta}^{[L]} = \hat{\mathbf{y}}-\mathbf{y}
$$

Para salida sigmoide con BCE:

$$
\delta^{[L]} = \hat{y}-y
$$

#### Paso 2: error en capas ocultas

Para $l=L-1,L-2,\dots,1$:

$$
\boldsymbol{\delta}^{[l]} = \left((\mathbf{W}^{[l+1]})^T\boldsymbol{\delta}^{[l+1]}\right)\odot f'^{[l]}(\mathbf{z}^{[l]})
$$

#### Paso 3: gradientes

Para una muestra individual:

$$
\frac{\partial \mathcal{L}}{\partial \mathbf{W}^{[l]}} = \boldsymbol{\delta}^{[l]}(\mathbf{a}^{[l-1]})^T
$$

$$
\frac{\partial \mathcal{L}}{\partial \mathbf{b}^{[l]}} = \boldsymbol{\delta}^{[l]}
$$

Para un mini-lote de tamaño $m$:

$$
\frac{\partial \mathcal{L}}{\partial \mathbf{W}^{[l]}} = \frac{1}{m}\boldsymbol{\Delta}^{[l]}(\mathbf{A}^{[l-1]})^T
$$

$$
\frac{\partial \mathcal{L}}{\partial \mathbf{b}^{[l]}} = \frac{1}{m}\sum_{i=1}^{m}\boldsymbol{\delta}^{[l]}_i
$$

[Figura 5.2]: **Propagación hacia adelante y hacia atrás en una red multicapa.** La figura debe mostrar claramente dos flujos. De izquierda a derecha: cálculo de $\mathbf{z}^{[l]}$, aplicación de activaciones $\mathbf{a}^{[l]}$ y obtención de la pérdida. De derecha a izquierda: propagación de errores $\boldsymbol{\delta}^{[l]}$, cálculo de gradientes y actualización de parámetros. Debe resaltarse que el entrenamiento de redes profundas no es un procedimiento misterioso sino una aplicación sistemática de cálculo diferencial y álgebra matricial.

### 5.1.6 Descenso del gradiente y optimizadores

Una vez obtenidos los gradientes, los parámetros se actualizan para reducir la pérdida.

#### a) Gradiente descendente básico

$$
\mathbf{W}^{[l]} \leftarrow \mathbf{W}^{[l]} - \eta \frac{\partial \mathcal{L}}{\partial \mathbf{W}^{[l]}}
$$

$$
\mathbf{b}^{[l]} \leftarrow \mathbf{b}^{[l]} - \eta \frac{\partial \mathcal{L}}{\partial \mathbf{b}^{[l]}}
$$

#### b) SGD

$$
\theta \leftarrow \theta - \eta \nabla_\theta \mathcal{L}(\theta;\mathcal{B})
$$

con $\mathcal{B}$ un mini-lote.

#### c) Adam

Si $g_t=\nabla_\theta \mathcal{L}_t$, entonces:

$$
m_t=\beta_1m_{t-1}+(1-\beta_1)g_t
$$

$$
v_t=\beta_2v_{t-1}+(1-\beta_2)g_t^2
$$

Corrección de sesgo:

$$
\hat{m}_t=\frac{m_t}{1-\beta_1^t}, \qquad \hat{v}_t=\frac{v_t}{1-\beta_2^t}
$$

Actualización:

$$
\theta_t=\theta_{t-1}-\eta \frac{\hat{m}_t}{\sqrt{\hat{v}_t}+\epsilon}
$$

Usualmente:

$$
\beta_1=0.9, \qquad \beta_2=0.999, \qquad \epsilon=10^{-8}
$$

### 5.1.7 Ejemplo completo de *forward* y *backpropagation*

**Ejemplo 5.1:** red con dos entradas, una capa oculta de dos neuronas y una salida binaria.

Supongamos:

$$
\mathbf{x}=\begin{bmatrix}1 \\ 0.5\end{bmatrix}, \qquad y=1
$$

Pesos y sesgos de la capa oculta:

$$
\mathbf{W}^{[1]} = \begin{bmatrix}
0.2 & -0.4 \\
0.7 & 0.1
\end{bmatrix}, \qquad
\mathbf{b}^{[1]} = \begin{bmatrix}0.1 \\ -0.2\end{bmatrix}
$$

Pesos y sesgo de salida:

$$
\mathbf{W}^{[2]}=\begin{bmatrix}0.6 & -0.1\end{bmatrix}, \qquad b^{[2]}=0.05
$$

Activación sigmoide en ambas capas.

**Paso 1: propagación hacia adelante**

$$
\mathbf{z}^{[1]}=\mathbf{W}^{[1]}\mathbf{x}+\mathbf{b}^{[1]}=\begin{bmatrix}0.1 \\ 0.55\end{bmatrix}
$$

$$
\mathbf{a}^{[1]} = \begin{bmatrix}\sigma(0.1) \\ \sigma(0.55)\end{bmatrix} \approx \begin{bmatrix}0.52498 \\ 0.63414\end{bmatrix}
$$

$$
z^{[2]} = \mathbf{W}^{[2]}\mathbf{a}^{[1]}+b^{[2]} \approx 0.30157
$$

$$
\hat{y}=\sigma(0.30157)\approx 0.57483
$$

**Paso 2: pérdida**

$$
\mathcal{L}=-\log(\hat{y})=-\log(0.57483)\approx 0.5537
$$

**Paso 3: retropropagación en la salida**

$$
\delta^{[2]}=\hat{y}-y=0.57483-1=-0.42517
$$

$$
\frac{\partial \mathcal{L}}{\partial \mathbf{W}^{[2]}}=\delta^{[2]}(\mathbf{a}^{[1]})^T \approx \begin{bmatrix}-0.22320 & -0.26962\end{bmatrix}
$$

$$
\frac{\partial \mathcal{L}}{\partial b^{[2]}}=-0.42517
$$

**Paso 4: retropropagación a la capa oculta**

$$
(\mathbf{W}^{[2]})^T\delta^{[2]} = \begin{bmatrix}0.6 \\ -0.1\end{bmatrix}(-0.42517) = \begin{bmatrix}-0.25510 \\ 0.04252\end{bmatrix}
$$

$$
\boldsymbol{\delta}^{[1]} \approx \begin{bmatrix}-0.06362 \\ 0.00986\end{bmatrix}
$$

$$
\frac{\partial \mathcal{L}}{\partial \mathbf{W}^{[1]}} = \boldsymbol{\delta}^{[1]}\mathbf{x}^T \approx \begin{bmatrix}
-0.06362 & -0.03181 \\
0.00986 & 0.00493
\end{bmatrix}
$$

$$
\frac{\partial \mathcal{L}}{\partial \mathbf{b}^{[1]}} \approx \begin{bmatrix}-0.06362 \\ 0.00986\end{bmatrix}
$$

**Paso 5: actualización** con $\eta=0.1$:

$$
\mathbf{W}^{[2]}_{\text{nuevo}} \approx \begin{bmatrix}0.62232 & -0.07304\end{bmatrix}
$$

$$
b^{[2]}_{\text{nuevo}} \approx 0.09252
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

**Conclusión:** la red ajusta sus parámetros para aumentar la probabilidad de la clase correcta. El mismo mecanismo, repetido sobre muchos ejemplos, permite aprender tareas complejas de clasificación, predicción y control en telecomunicaciones.

---

## 5.2 Receptores Neuronales

### 5.2.1 Definición y cambio de paradigma

Un **receptor neuronal** es un receptor de comunicaciones que utiliza redes neuronales para realizar una o varias funciones tradicionalmente resueltas con técnicas basadas en modelo: sincronización, estimación de canal, ecualización, demodulación, decodificación o decisión final.

En el enfoque clásico se parte de ecuaciones como:

$$
\mathbf{r}=\mathbf{H}\mathbf{s}+\mathbf{n}
$$

mientras que en el enfoque neuronal se aprende una aplicación:

$$
\hat{\mathbf{p}}=g_\theta(\mathbf{r})
$$

con $g_\theta$ una red neuronal parametrizada por $\theta$ y $\hat{\mathbf{p}}$ la probabilidad de cada símbolo o bit.

> **Concepto clave:** el receptor neuronal no elimina la teoría clásica; la complementa cuando el modelo analítico es incompleto, inexacto o demasiado costoso.

### 5.2.2 Limitaciones de los métodos clásicos

Los métodos clásicos son óptimos cuando sus hipótesis se cumplen. Sin embargo, en escenarios reales pueden aparecer:

- no linealidades del amplificador de potencia;
- ruido impulsivo o no gaussiano;
- desajustes de fase y frecuencia;
- interferencia multiusuario compleja;
- hardware heterogéneo;
- canales altamente dinámicos.

En detección coherente ideal, por ejemplo:

$$
y_k = \int_0^T r(t)s_k^*(t)\,dt
$$

Y la decisión ML en AWGN puede escribirse como:

$$
\hat{\mathbf{s}}=\arg\min_{\mathbf{s}\in\mathcal{S}} \|\mathbf{r}-\mathbf{H}\mathbf{s}\|_2^2
$$

Cuando el modelo se aleja de la realidad, la distancia euclídea ya no captura toda la estructura del problema.

### 5.2.3 Receptor neuronal para detección de señales

Si se reciben $N$ muestras complejas I/Q:

$$
\mathbf{r}=[r_1,r_2,\dots,r_N]^T, \qquad r_n\in\mathbb{C}
$$

una representación real habitual es:

$$
\mathbf{x}=[\Re(r_1),\Im(r_1),\dots,\Re(r_N),\Im(r_N)]^T
$$

Entonces la red produce probabilidades sobre los $M$ símbolos posibles:

$$
\hat{\mathbf{p}}=\mathrm{softmax}(f_\theta(\mathbf{x}))
$$

La decisión final es:

$$
\hat{m}=\arg\max_{i\in\{1,\dots,M\}} \hat{p}_i
$$

Una arquitectura típica podría ser:

$$
\mathbf{a}^{[1]}=\mathrm{ReLU}(\mathbf{W}^{[1]}\mathbf{x}+\mathbf{b}^{[1]})
$$

$$
\mathbf{a}^{[2]}=\mathrm{ReLU}(\mathbf{W}^{[2]}\mathbf{a}^{[1]}+\mathbf{b}^{[2]})
$$

$$
\hat{\mathbf{p}}=\mathrm{softmax}(\mathbf{W}^{[3]}\mathbf{a}^{[2]}+\mathbf{b}^{[3]})
$$

[Figura 5.3]: **Receptor neuronal para demodulación.** La figura debe mostrar la cadena símbolo transmitido $\rightarrow$ canal $\rightarrow$ ruido e interferencia $\rightarrow$ muestras I/Q $\rightarrow$ preprocesamiento $\rightarrow$ red neuronal $\rightarrow$ salida softmax sobre la constelación. Debe enfatizarse visualmente el cambio de paradigma entre un receptor por bloques diseñados manualmente y un receptor discriminativo aprendido a partir de datos.

### 5.2.4 Autoencoder como sistema de comunicación *end-to-end*

Una de las ideas más influyentes en aprendizaje profundo aplicado a capa física es modelar el enlace completo como un **autoencoder**.

- El transmisor es una red $f_{\theta_T}$.
- El canal es una capa no entrenable o parcialmente diferenciable $h(\cdot)$.
- El receptor es otra red $g_{\theta_R}$.

Si el mensaje es $m\in\{1,2,\dots,M\}$ y su codificación *one-hot* es $\mathbf{e}_m$, entonces:

$$
\mathbf{x}=f_{\theta_T}(\mathbf{e}_m)
$$

sujeta a restricción de potencia media:

$$
\frac{1}{n}\mathbb{E}[\|\mathbf{x}\|_2^2]\leq P
$$

En AWGN:

$$
\mathbf{r}=\mathbf{x}+\mathbf{n}, \qquad \mathbf{n}\sim\mathcal{N}(0,\sigma^2\mathbf{I})
$$

El receptor estima:

$$
\hat{\mathbf{p}}=g_{\theta_R}(\mathbf{r})
$$

con pérdida:

$$
\mathcal{L}(\theta_T,\theta_R)=-\sum_{m=1}^{M}\sum_{k=1}^{M}e_{m,k}\log \hat{p}_k
$$

La tasa de información por uso de canal es:

$$
R=\frac{\log_2 M}{n}\quad \text{bits/uso de canal}
$$

Este marco permite **optimizar conjuntamente** representación, codificación y detección para un canal dado.

### 5.2.5 Entrenamiento y métricas de desempeño

En telecomunicaciones, los datos de entrenamiento pueden generarse por simulación o medirse experimentalmente. Conviene dividirlos en entrenamiento, validación y prueba. Una estrategia útil es muestrear varios valores de SNR:

$$
\mathrm{SNR}_{\mathrm{dB}} \sim \mathcal{U}(\gamma_{\min},\gamma_{\max})
$$

para mejorar robustez.

Las métricas clásicas siguen siendo centrales.

**BER:**

$$
\mathrm{BER}=\frac{N_{\mathrm{bits\ erróneos}}}{N_{\mathrm{bits\ transmitidos}}}
$$

**SER:**

$$
\mathrm{SER}=\frac{N_{\mathrm{símbolos\ erróneos}}}{N_{\mathrm{símbolos\ transmitidos}}}
$$

También se monitorizan pérdida de entrenamiento, pérdida de validación, exactitud de clasificación y robustez fuera de distribución.

### 5.2.6 Comparación de rendimiento: receptor neuronal vs. clásico

El receptor clásico suele ser preferible cuando:

- el modelo de canal es correcto;
- el canal es relativamente simple;
- la complejidad debe ser muy baja;
- se requiere interpretabilidad fuerte.

El receptor neuronal puede ser preferible cuando:

- el canal real es difícil de modelar;
- existen no linealidades importantes;
- se desea aprender de datos medidos;
- se busca adaptabilidad a escenarios heterogéneos.

Si para una BER objetivo de $10^{-3}$ un receptor neuronal necesita 1 dB menos que uno clásico, se habla de una **ganancia de 1 dB** en ese punto operativo. Sin embargo, deben evaluarse también complejidad, consumo energético, tiempo de entrenamiento y generalización.

### 5.2.7 Herramientas de implementación

- **TensorFlow/Keras:** prototipado rápido y entrenamiento con GPU.
- **PyTorch:** gran flexibilidad para investigación.
- **Sionna (NVIDIA):** canales diferenciables y componentes de capa física orientados a telecomunicaciones.

### 5.2.8 Ejemplos resueltos

**Ejemplo 5.2:** demodulación neuronal de QPSK mediante softmax.

Supongamos logits:

$$
\mathbf{z}=[2.2,\ 1.0,\ 0.1,\ -0.5]^T
$$

Exponenciales:

$$
e^{2.2}\approx 9.025, \quad e^{1.0}\approx 2.718, \quad e^{0.1}\approx 1.105, \quad e^{-0.5}\approx 0.607
$$

Suma:

$$
S=13.455
$$

Probabilidades:

$$
\hat{\mathbf{p}}\approx [0.671,\ 0.202,\ 0.082,\ 0.045]^T
$$

La decisión es:

$$
\hat{m}=1
$$

Si la clase correcta era la 1, la pérdida es:

$$
\mathcal{L}=-\log(0.671)\approx 0.399
$$

**Ejemplo 5.3:** cálculo de BER de un receptor neuronal.

Se transmiten 10 bits y se observan 3 errores. Entonces:

$$
\mathrm{BER}=\frac{3}{10}=0.3
$$

Este valor es alto porque el conjunto es diminuto; en evaluación real se requieren miles o millones de bits.

**Ejemplo 5.4:** interpretación de un autoencoder de comunicaciones.

Si $M=16$ mensajes posibles y longitud de bloque $n=4$ usos de canal, la tasa es:

$$
R=\frac{\log_2(16)}{4}=1\ \text{bit/uso de canal}
$$

El transmisor aprende una constelación o código y el receptor aprende la regla de decisión asociada.

---

## 5.3 IA Nativa en Redes 6G (IMT-2030)

### 5.3.1 Visión de 6G e IMT-2030

La visión IMT-2030 propone una evolución más profunda que un simple aumento de tasa binaria. El objetivo es integrar comunicaciones, inteligencia, sensado, automatización y servicios inmersivos en una infraestructura ubicua, eficiente y adaptable.

Entre los ejes más citados de 6G se encuentran:

- comunicación inmersiva;
- conectividad ubicua;
- ultra baja latencia y alta fiabilidad;
- integración de IA en la red;
- sensado y comunicación integrados (ISAC);
- sostenibilidad energética.

Algunos KPIs representativos son:

$$
T_{\mathrm{e2e}}\leq T_{\max}
$$

$$
\Pr\{\text{éxito}\} \ge 1-\varepsilon
$$

$$
E_b=\frac{P}{R_b}
$$

### 5.3.2 Arquitectura AI-nativa

Decir que una red es **AI-nativa** significa que la IA no es un accesorio externo, sino una función integrada en múltiples planos:

1. observabilidad;
2. plano de datos para IA;
3. entrenamiento;
4. inferencia distribuida;
5. realimentación y adaptación cerrada.

Si el estado de red es $s_t$, la acción de control es $a_t$ y la recompensa es $r_t$, una política puede modelarse como:

$$
a_t=\pi_\theta(s_t)
$$

con objetivo:

$$
J(\pi_\theta)=\mathbb{E}\left[\sum_{t=0}^{\infty}\gamma^tr_t\right]
$$

[Figura 5.4]: **Arquitectura AI-nativa de red 6G.** La figura debe superponer un plano de inteligencia sobre RAN, core, edge y terminales. Deben aparecer fuentes de datos, repositorio o *data fabric*, entrenamiento, registro de modelos e inferencia distribuida. La figura debe comunicar que la IA atraviesa todo el ciclo operativo de la red.

### 5.3.3 AI/ML como función nativa de red

Podemos pensar en una función de red de IA:

$$
\mathcal{F}_{\mathrm{AI}}:(\text{datos},\text{contexto},\text{políticas})\mapsto(\text{predicciones},\text{acciones},\text{modelos})
$$

Esto habilita casos como predicción de congestión, selección de haz, control energético, clasificación de tráfico, transferencia de modelos y compresión semántica.

### 5.3.4 Computación distribuida y Edge AI

La latencia extremo a extremo puede descomponerse como:

$$
T_{\mathrm{total}} = T_{\mathrm{uplink}} + T_{\mathrm{transporte}} + T_{\mathrm{cola}} + T_{\mathrm{cómputo}} + T_{\mathrm{downlink}}
$$

Cuando la inferencia se realiza en el borde, el término $T_{\mathrm{transporte}}$ se reduce drásticamente.

**Ejemplo 5.5:** latencia nube vs. borde.

Si en nube la latencia es $5+10+25+15=55$ ms y en edge es $3+0+8+3=14$ ms, la reducción es:

$$
\Delta T = 55-14 = 41\ \text{ms}
$$

### 5.3.5 Técnicas de aprendizaje distribuido

#### a) Aprendizaje federado

Si el nodo $k$ tiene pérdida local $F_k(\theta)$ y $n_k$ muestras, el objetivo global es:

$$
F(\theta)=\sum_{k=1}^{K}\frac{n_k}{N}F_k(\theta), \qquad N=\sum_{k=1}^{K}n_k
$$

En FedAvg:

$$
\theta_k^{(t,e+1)}=\theta_k^{(t,e)}-\eta\nabla F_k(\theta_k^{(t,e)})
$$

$$
\theta^{(t+1)}=\sum_{k=1}^{K}\frac{n_k}{N}\theta_k^{(t,E)}
$$

**Ejemplo 5.6:** una ronda de FedAvg.

Con $\theta^{(0)}=1.0$, $n_1=60$, $n_2=40$, gradientes $g_1=0.8$, $g_2=-0.2$ y $\eta=0.5$:

$$
\theta_1=1.0-0.5(0.8)=0.6
$$

$$
\theta_2=1.0-0.5(-0.2)=1.1
$$

$$
\theta^{(1)}=\frac{60}{100}(0.6)+\frac{40}{100}(1.1)=0.80
$$

[Figura 5.5]: **Aprendizaje federado en red móvil.** La figura debe mostrar varios dispositivos o estaciones base con datos locales, un servidor agregador y rondas de comunicación de parámetros. Debe destacarse que los datos no abandonan el origen, solo lo hacen actualizaciones del modelo.

#### b) Split Learning

Si la red se corta en la capa $c$:

$$
\mathbf{h}^{[c]}=f_{\theta_{1:c}}(\mathbf{x})
$$

$$
\hat{\mathbf{y}}=g_{\theta_{c+1:L}}(\mathbf{h}^{[c]})
$$

Durante retropropagación el servidor devuelve:

$$
\frac{\partial \mathcal{L}}{\partial \mathbf{h}^{[c]}}
$$

#### c) Aprendizaje por refuerzo distribuido

$$
\nabla_\phi J(\phi)=\mathbb{E}_{\pi_\phi}\left[\sum_t \nabla_\phi \log \pi_\phi(a_t|s_t)\,\hat{A}_t\right]
$$

### 5.3.6 Edge Large AI Models (Edge LAMs)

Los modelos grandes desplegados en edge requieren *pruning*, cuantización y destilación.

**Pruning:**

$$
\theta_{\mathrm{pruned}} = \mathbf{m}\odot\theta, \qquad \|\mathbf{m}\|_0\le K
$$

**Cuantización:**

$$
q=\mathrm{round}\left(\frac{w}{\Delta}\right), \qquad \hat{w}=\Delta q
$$

**Destilación:**

$$
\mathcal{L}=\alpha T^2\,\mathrm{KL}\left(\sigma\left(\frac{\mathbf{z}_T}{T}\right)\Bigg\|\sigma\left(\frac{\mathbf{z}_S}{T}\right)\right)+(1-\alpha)\,\mathrm{CE}(\mathbf{y},\sigma(\mathbf{z}_S))
$$

### 5.3.7 Sinergias con gemelos digitales e ISAC

Si el estado físico de la red es $\mathbf{x}(t)$, el gemelo digital mantiene una estimación:

$$
\hat{\mathbf{x}}(t+1)=f_\psi\big(\hat{\mathbf{x}}(t),\mathbf{u}(t),\mathbf{y}(t)\big)
$$

En ISAC, puede distinguirse entre señal de comunicación y señal de sensado:

$$
\mathbf{y}_c=\mathbf{H}_c\mathbf{x}+\mathbf{n}_c
$$

$$
\mathbf{y}_s=\mathbf{H}_s\mathbf{x}+\mathbf{n}_s
$$

Una formulación multiobjetivo es:

$$
\max_{\mathbf{x},\pi}\ \lambda R(\mathbf{x},\pi)+(1-\lambda)S(\mathbf{x},\pi)
$$

sujeta a:

$$
\|\mathbf{x}\|_2^2\le P
$$

[Figura 5.6]: **Convergencia IA + Gemelo Digital + ISAC.** La figura debe mostrar la red física real, el gemelo digital y un motor de IA cerrando el lazo. ISAC genera observaciones, el gemelo actualiza estados y la IA optimiza acciones que luego se aplican a la red real.

### 5.3.8 Ejemplos y casos de estudio

**Ejemplo 5.7:** optimización multiobjetivo en ISAC.

Si $R=8$, $S=5$ y $\lambda=0.7$:

$$
U=\lambda R+(1-\lambda)S=0.7(8)+0.3(5)=7.1
$$

Si otra configuración produce $R'=7$ y $S'=7$:

$$
U'=0.7(7)+0.3(7)=7
$$

La primera es preferible bajo esa ponderación.

**Ejemplo 5.8:** papel de un gemelo digital.

Si la carga actual es:

$$
\mathbf{x}(t)=[0.8,\ 0.6,\ 0.4]
$$

y el gemelo predice:

$$
\hat{\mathbf{x}}(t+1)=[0.9,\ 0.65,\ 0.5]
$$

una acción de descarga de tráfico:

$$
\mathbf{u}(t)=[-0.1,\ 0,\ +0.1]
$$

puede generar el estado estimado:

$$
\hat{\mathbf{x}}'(t+1)=[0.8,\ 0.65,\ 0.6]
$$

lo que reduce riesgo de congestión antes de actuar sobre la red real.

---

## 5.4 Comunicaciones Semánticas y Sistemas de Próxima Generación

### 5.4.1 De la teoría de información a las comunicaciones semánticas

La teoría clásica de Shannon respondió a una pregunta fundamental: **¿cuál es la tasa máxima a la que pueden transmitirse símbolos por un canal con error arbitrariamente pequeño?** Esa teoría fue revolucionaria precisamente porque separó el problema ingenieril del transporte fiable del problema del significado. Shannon, y más explícitamente Weaver, distinguieron tres niveles:

1. **nivel técnico:** exactitud con que se transmiten símbolos;
2. **nivel semántico:** precisión con que se transmite el significado;
3. **nivel de efectividad:** influencia del mensaje en la conducta o en la tarea.

En la Unidad 2 vimos que la autoinformación y la entropía de Shannon miden sorpresa probabilística, no significado. Allí mismo apareció una observación crucial: la medida de Shannon es deliberadamente **agnóstica respecto de la semántica**. Esa separación fue una fortaleza para construir la teoría clásica, pero en 6G se vuelve insuficiente para aplicaciones donde el objetivo no es reconstruir exactamente todos los bits, sino **preservar aquello que importa para una tarea**.

#### a) Conexión con Weaver, Carnap-Bar-Hillel y Floridi

- **Weaver** sugirió que la teoría de Shannon resolvía el nivel técnico, pero dejaba abiertos los niveles semántico y pragmático.
- **Carnap y Bar-Hillel** desarrollaron una teoría lógica de la información semántica, donde el contenido semántico se vincula con el conjunto de mundos posibles que una proposición excluye.
- **Floridi** reformuló la información semántica subrayando que para hablar de información significativa no basta con que exista contenido; además debe haber verdad, coherencia y relevancia contextual.

Si $\Omega$ es el conjunto de mundos posibles y una proposición $p$ es verdadera en el subconjunto $\Omega_p\subseteq\Omega$, una intuición de contenido semántico puede expresarse por la capacidad de $p$ de reducir posibilidades. Una medida esquemática es:

$$
I_{\mathrm{sem}}(p) \propto -\log \frac{|\Omega_p|}{|\Omega|}
$$

Cuanto menor sea el conjunto de mundos compatibles con el mensaje, mayor será su contenido semántico. Esta idea no sustituye a Shannon, pero muestra que la semántica introduce **estructura, contexto y relevancia**, no solo probabilidad.

#### b) Variables sintácticas, semánticas y de tarea

En comunicaciones semánticas conviene distinguir tres niveles de variables aleatorias:

- $X$: representación sintáctica cruda (bits, muestras, texto, píxeles);
- $S$: contenido semántico extraído del mensaje;
- $T$: tarea final o decisión de interés.

La cadena conceptual puede representarse como:

$$
X \longrightarrow S \longrightarrow T
$$

En una comunicación clásica, el criterio típico es minimizar una distorsión sintáctica $d_X(X,\hat{X})$. En una comunicación semántica o orientada a tareas interesa minimizar una distorsión semántica $d_S(S,\hat{S})$ o una pérdida de tarea $\ell(T,\hat{T})$.

#### c) JSCC como precursor

La codificación separada de fuente y canal fue una de las grandes ideas de la teoría clásica. Sin embargo, en enlaces de bloque finito, baja latencia o canales muy variables, el paradigma de separación puede no ser la mejor solución práctica. Aquí aparece la **codificación conjunta fuente-canal** (*Joint Source-Channel Coding, JSCC*).

Si una fuente $U$ debe enviarse sobre un canal con entrada $X$ y salida $Y$, un codificador JSCC implementa directamente:

$$
X^n = f(U^k)
$$

mientras el decodificador produce:

$$
\hat{U}^k = g(Y^n)
$$

En lugar de optimizar por separado la compresión y la protección al ruido, JSCC aprende o diseña una representación robusta de extremo a extremo. Ese principio es un precursor natural de las comunicaciones semánticas: **no se protege todo por igual, sino aquello que afecta la reconstrucción útil**.

#### d) DeepJSCC

La versión moderna de JSCC es **DeepJSCC**, donde codificador y decodificador son redes neuronales entrenadas extremo a extremo. Para una imagen $\mathbf{u}$, el transmisor profundo produce:

$$
\mathbf{x}=f_{\theta_T}(\mathbf{u})
$$

sujeto a potencia:

$$
\frac{1}{n}\mathbb{E}[\|\mathbf{x}\|_2^2]\le P
$$

El canal genera:

$$
\mathbf{y}=h(\mathbf{x},\mathbf{n})
$$

y el decodificador reconstruye:

$$
\hat{\mathbf{u}}=g_{\theta_R}(\mathbf{y})
$$

El entrenamiento minimiza una pérdida como:

$$
\mathcal{L}_{\mathrm{DeepJSCC}} = \mathbb{E}\big[d(\mathbf{u},\hat{\mathbf{u}})\big]
$$

que puede ser MSE, una pérdida perceptual o incluso una pérdida semántica si se mide similitud en un espacio de *embeddings*.

> **Concepto clave:** DeepJSCC no es todavía comunicación semántica en sentido pleno, pero sí representa el paso decisivo desde una reconstrucción exacta de bits hacia una **preservación útil del contenido** frente al ruido del canal.

[Figura 5.7]: **Evolución conceptual desde Shannon hasta DeepJSCC y comunicaciones semánticas.** La figura debe presentar tres columnas. En la primera, la cadena clásica fuente-codificador de fuente-codificador de canal-canal-decodificador de canal-decodificador de fuente, optimizada con BER o tasa. En la segunda, JSCC/DeepJSCC como bloque extremo a extremo entrenable. En la tercera, una arquitectura semántica que incluye base de conocimiento, extracción de significado, objetivo de tarea y métrica semántica. La figura debe dejar claro que el cambio no es solo algorítmico, sino también de **objeto de optimización**: de bits a significado y de significado a tarea.

### 5.4.2 Arquitectura de comunicación semántica

Una arquitectura semántica simplificada puede descomponerse en cinco bloques:

1. fuente de datos $X$;
2. **codificador semántico** que extrae significado $S$;
3. codificador físico o de canal que genera una señal $\mathbf{x}$;
4. canal físico con ruido e interferencia;
5. **decodificador semántico** que reconstruye $\hat{S}$ y eventualmente una salida de tarea $\hat{T}$.

#### a) Codificador semántico

El codificador semántico no trabaja solo con estadística superficial, sino con una representación estructurada del conocimiento. Formalmente:

$$
S = \Phi(X;\mathcal{K},\theta_E)
$$

donde:

- $\mathcal{K}$ es una base de conocimiento o contexto;
- $\theta_E$ son parámetros del extractor;
- $S$ es una representación semántica latente o simbólica.

Por ejemplo, si $X$ es una frase, $S$ puede ser una estructura de intención, entidades y relaciones. Si $X$ es un vídeo, $S$ puede ser una descripción de objetos, trayectorias y eventos relevantes para conducción autónoma.

#### b) Canal semántico

El canal físico introduce ruido en la forma sintáctica, pero en comunicaciones semánticas importa cómo ese ruido afecta el significado. Por ello se modela un **canal semántico** como la transformación inducida entre representaciones semánticas:

$$
p(\hat{S}|S)
$$

Incluso si $p(\hat{X}|X)$ es pobre, puede ocurrir que $p(\hat{S}|S)$ siga siendo aceptable para la tarea. En otras palabras, un error sintáctico no implica necesariamente un error semántico.

#### c) Decodificador semántico

El decodificador semántico reconstruye significado y, si corresponde, una decisión final:

$$
\hat{S}=\Psi(Y;\hat{\mathcal{K}},\theta_D)
$$

$$
\hat{T}=\Gamma(\hat{S})
$$

La calidad del sistema se evalúa no solo por la cercanía entre $X$ y $\hat{X}$, sino por la preservación de relaciones, intención o utilidad de tarea.

#### d) Tasa semántica, distorsión semántica y capacidad semántica

Sea $S$ la variable semántica original y $\hat{S}$ la reconstrucción. Una definición útil de **tasa semántica** es:

$$
R_s = H_s(S)-H_s(S|\hat{S})
$$

donde $H_s(\cdot)$ denota entropía semántica. Esta expresión es análoga a una información mutua semántica y mide cuánta incertidumbre de significado queda resuelta tras la reconstrucción.

La **distorsión semántica** puede definirse como:

$$
D_s = \mathbb{E}\big[d_s(S,\hat{S})\big]
$$

con $d_s(\cdot,\cdot)$ una métrica de pérdida de significado. En aplicaciones orientadas a tareas, una forma alternativa es:

$$
D_T = \mathbb{E}[\ell(T,\hat{T})]
$$

La **capacidad semántica** puede formularse como la máxima tasa semántica alcanzable bajo restricciones físicas y semánticas:

$$
C_s = \sup_{p(x),\Phi,\Psi} R_s
$$

sujeta a:

$$
D_s \le D_{s,\max}, \qquad \mathbb{E}[\|X\|^2]\le P
$$

Esta definición es deliberadamente abstracta porque, a diferencia de Shannon, la semántica depende de contexto, conocimiento compartido y tarea. Sin embargo, expresa con claridad la idea de fondo: **la red debe transportar significado útil, no necesariamente todos los símbolos**.

#### e) Comunicación orientada a tareas

En comunicaciones clásicas el objetivo suele ser reconstruir datos. En comunicaciones orientadas a tareas el objetivo es maximizar éxito operativo. Si $T$ es la tarea y $\hat{T}$ la decisión, puede optimizarse:

$$
\min_{\Phi,\Psi,p(x)} \mathbb{E}[\ell(T,\hat{T})]
$$

Por ejemplo, en visión remota para conducción autónoma quizá no haga falta reconstruir toda la imagen, sino decidir correctamente si hay un peatón, un ciclista o una señal de stop.

> **Concepto clave:** la diferencia entre comunicación orientada a datos y comunicación orientada a tareas es profunda. En la primera se pregunta “¿puedo reconstruir el mensaje?”, mientras que en la segunda se pregunta “¿puedo ejecutar correctamente la tarea usando la información transmitida?”.

[Figura 5.8]: **Arquitectura de un sistema de comunicación semántica.** La figura debe incluir una fuente multimodal, un codificador semántico con acceso a una base de conocimiento, un codificador físico, el canal, un decodificador semántico y un módulo final de tarea. Debe visualizarse la separación entre representación sintáctica, representación semántica y salida de tarea. Conviene incorporar flechas laterales desde la base de conocimiento hacia emisor y receptor para subrayar que el significado depende de contexto compartido.

### 5.4.3 Métricas para comunicaciones semánticas

Las métricas sintácticas clásicas como BER, throughput y SNR siguen siendo importantes, pero dejan de ser suficientes cuando el objetivo es preservar significado.

#### a) Similitud semántica por coseno

Si $\mathbf{e}(S)$ y $\mathbf{e}(\hat{S})$ son *embeddings* del contenido semántico, la similitud coseno es:

$$
\mathrm{Sim}_{\cos}(S,\hat{S}) = \frac{\mathbf{e}(S)^T\mathbf{e}(\hat{S})}{\|\mathbf{e}(S)\|_2\,\|\mathbf{e}(\hat{S})\|_2}
$$

Toma valores cercanos a 1 cuando el significado es muy parecido.

#### b) BLEU y métricas de lenguaje

Para texto, una métrica clásica es BLEU, basada en coincidencia de *n-gramas* con penalización por longitud. Simplificando:

$$
\mathrm{BLEU}=\mathrm{BP}\cdot \exp\left(\sum_{n=1}^{N} w_n \log p_n\right)
$$

con $p_n$ la precisión de *n-gramas* y $\mathrm{BP}$ la penalización por brevedad.

Aunque BLEU es útil, no siempre captura significado profundo; dos frases pueden tener baja coincidencia léxica y alta equivalencia semántica.

#### c) Distancia semántica

Una métrica general puede definirse como:

$$
d_s(S,\hat{S}) = 1-\mathrm{Sim}_{\cos}(S,\hat{S})
$$

O bien mediante divergencias distribucionales:

$$
d_s(S,\hat{S}) = D_{\mathrm{KL}}\big(p(z|S)\|p(z|\hat{S})\big)
$$

si $z$ es una representación latente compartida.

#### d) Task Success Rate (TSR)

La **Task Success Rate** mide la fracción de ocasiones en que la tarea final se resuelve correctamente:

$$
\mathrm{TSR} = \frac{N_{\mathrm{tareas\ exitosas}}}{N_{\mathrm{tareas\ ejecutadas}}}
$$

En un sistema de control remoto, por ejemplo, puede interpretarse como probabilidad de tomar la decisión correcta usando la información recibida.

#### e) Eficiencia espectral semántica

Una definición simple de **eficiencia espectral semántica** es la cantidad de información semántica útil por unidad de ancho de banda:

$$
\eta_s = \frac{R_s}{B}
$$

con $R_s$ en bits semánticos por segundo y $B$ en Hz.

Si además queremos ponderar por éxito de tarea:

$$
\eta_{s,T} = \frac{R_s\cdot \mathrm{TSR}}{B}
$$

Esta métrica conecta semántica, eficiencia radioeléctrica y utilidad operativa.

#### f) Comparación con métricas tradicionales

- **BER** mide exactitud de bits, no significado.
- **SNR** mide calidad física del enlace, no utilidad del contenido.
- **Throughput** mide volumen de datos, no relevancia.
- **TSR** y $\eta_s$ miden desempeño respecto al objetivo final.

[Figura 5.9]: **Comparación entre métricas sintácticas y semánticas.** La figura debe representar dos ejes. En el primero, un sistema puede tener BER muy baja pero TSR mediocre si transmite información poco relevante. En el segundo, otro sistema puede tener BER moderada y, sin embargo, TSR alta al preservar solo el contenido necesario para la tarea. La figura debe ayudar al estudiante a entender por qué una red futura puede sacrificar fidelidad sintáctica para ganar utilidad real.

### 5.4.4 Relevancia en sistemas de próxima generación (6G/IMT-2030)

Las comunicaciones semánticas no son una curiosidad académica aislada; encajan de forma natural en la visión IMT-2030 y en la arquitectura AI-nativa de 6G.

#### a) IMT-2030 y visión semántica

El marco IMT-2030 destaca conectividad inmersiva, inteligencia distribuida, sensado integrado y automatización. En ese contexto, tiene sentido que la red priorice información relevante para la aplicación y no necesariamente el flujo bruto completo. Conceptualmente, una red 6G puede optimizar una utilidad como:

$$
U = \alpha\,\mathrm{TSR} + \beta\,\eta_s - \gamma T_{\mathrm{e2e}} - \delta E_b
$$

con $\alpha,\beta,\gamma,\delta \ge 0$ pesos de diseño.

#### b) IA nativa para extracción y reconstrucción de significado

La semántica requiere modelos capaces de entender contexto, lenguaje, escenas, mapas y tareas. Eso implica una infraestructura AI-nativa donde emisor, receptor, borde y nube compartan modelos y bases de conocimiento. Si $\mathcal{M}_e$ y $\mathcal{M}_r$ son modelos semánticos en emisor y receptor, la calidad depende también de su alineamiento:

$$
\Delta_{\mathcal{M}} = d(\mathcal{M}_e,\mathcal{M}_r)
$$

Cuanto menor sea $\Delta_{\mathcal{M}}$, mayor será la consistencia del significado reconstruido.

#### c) Asignación de recursos consciente de semántica

En una red clásica, la asignación de recursos suele maximizar throughput, SINR o equidad. En una red semántica, el planificador puede asignar potencia, RBs o prioridad de acuerdo con relevancia de contenido. Si el usuario $k$ tiene utilidad semántica $u_k$ y recibe recursos $r_k$:

$$
\max_{\{r_k\}} \sum_{k=1}^{K} u_k(r_k)
$$

sujeto a:

$$
\sum_{k=1}^{K} r_k \le R_{\mathrm{tot}}, \qquad r_k\ge 0
$$

Aquí $u_k(\cdot)$ puede depender de TSR, latencia de tarea, urgencia contextual o criticidad de la información.

#### d) Gemelos digitales y semántica

Los gemelos digitales son especialmente compatibles con el paradigma semántico, porque la red no solo transmite datos del sistema, sino estados relevantes para predicción y control. Si el estado verdadero es $\mathbf{x}_t$ y el estado semántico transmitido es $S_t$, el gemelo puede actualizarse como:

$$
\hat{\mathbf{x}}_{t+1}=f_{\mathrm{DT}}(\hat{\mathbf{x}}_t,S_t,\mathbf{u}_t)
$$

Así, el enlace no necesita reconstruir cada muestra cruda, sino la información suficiente para mantener coherente el gemelo.

#### e) ISAC con capa semántica

En ISAC, una red capta observaciones del entorno además de comunicar. La capa semántica puede convertir esas observaciones en descripciones útiles: objetos, trayectorias, eventos, riesgos. Si $\mathbf{o}_t$ es la observación sensada, el extractor semántico genera:

$$
S_t = \Phi_{\mathrm{ISAC}}(\mathbf{o}_t)
$$

La decisión de control puede depender directamente de $S_t$:

$$
a_t = \pi(S_t)
$$

con lo cual comunicación y sensado convergen en un lazo orientado a tareas.

#### f) Inteligencia de borde y computación semántica

La extracción semántica suele ser costosa computacionalmente, por lo que el borde resulta esencial. Si una tarea requiere $C_s$ operaciones para inferencia semántica y el nodo edge ofrece $f_{\mathrm{edge}}$ operaciones por segundo:

$$
T_{\mathrm{sem}} \approx \frac{C_s}{f_{\mathrm{edge}}}
$$

La decisión de procesar en dispositivo, borde o nube debe equilibrar latencia, energía, privacidad y alineamiento de modelos.

> **Concepto clave:** en 6G, la comunicación semántica no sustituirá a toda la capa física clásica; coexistirá con ella como una capa superior de compresión, priorización e inferencia orientada a servicio.

[Figura 5.10]: **Pila 6G con capa semántica, edge intelligence, ISAC y gemelo digital.** La figura debe mostrar una pila de red donde la capa física y MAC conviven con un plano semántico transversal. Ese plano debe conectarse con sensores ISAC, motores de IA en edge, un gemelo digital de red y un planificador de recursos consciente de significado. La intención es visualizar que en 6G la semántica será una función de sistema, no un módulo aislado.

### 5.4.5 Fronteras de investigación

#### a) Comunicaciones semánticas basadas en grafos de conocimiento

Si el conocimiento compartido entre emisor y receptor se modela como un grafo $\mathcal{G}=(\mathcal{V},\mathcal{E})$, el mensaje puede expresarse como un subgrafo relevante o como un recorrido semántico. El codificador ya no transmite una secuencia plana, sino relaciones entre entidades. Una medida de distorsión estructural podría ser:

$$
d_{\mathcal{G}}(\mathcal{G},\hat{\mathcal{G}})=\lambda_1 d_{\mathcal{V}} + \lambda_2 d_{\mathcal{E}} + \lambda_3 d_{\mathrm{path}}
$$

Esto es especialmente útil en redes industriales, Internet táctil, logística y sistemas cooperativos autónomos.

#### b) Comunicaciones semánticas multimodales

Los sistemas futuros no transmitirán solo texto. También manejarán imagen, vídeo, habla, sensores 3D y mapas. Si cada modalidad $m$ produce una representación $S^{(m)}$, una fusión multimodal puede escribirse como:

$$
S_{\mathrm{fusion}} = \mathcal{F}\big(S^{(1)},S^{(2)},\dots,S^{(M)}\big)
$$

El reto consiste en diseñar métricas y codificadores capaces de decidir qué modalidad importa más para la tarea en cada instante.

#### c) Seguridad y privacidad semánticas

Una red semántica puede filtrar datos sensibles aunque no transmita bits crudos. Por ello interesa controlar fuga de información. Si $Z$ es un atributo privado, una restricción útil es:

$$
I(Z;\hat{S}) \le \epsilon
$$

mientras se mantiene utilidad de tarea alta. También aparecen ataques adversarios semánticos: pequeñas perturbaciones físicas o lingüísticas que alteran el significado reconstruido sin degradar notablemente BER o SNR.

#### d) Estandarización

Aunque el área sigue siendo emergente, ya existen debates en **3GPP**, **ITU-T** y otros foros sobre transporte de modelos AI/ML, integración de inteligencia nativa, métricas orientadas a tareas y posibles marcos para comunicación semántica. El reto de estandarización es doble:

1. definir interfaces e interoperabilidad;
2. evitar fijar demasiado pronto una semántica única para casos de uso muy distintos.

#### e) Problemas abiertos fundamentales

Entre las preguntas de investigación más importantes destacan:

- ¿cómo definir rigurosamente $H_s(S)$ de forma universal o al menos interoperable?
- ¿cómo alinear bases de conocimiento entre emisor y receptor?
- ¿cómo combinar eficiencia espectral clásica con utilidad semántica?
- ¿cómo medir robustez semántica frente a cambios de dominio?
- ¿cómo garantizar privacidad, equidad y trazabilidad de decisiones semánticas?

### 5.4.6 Ejemplos resueltos de comunicaciones semánticas

**Ejemplo 5.9:** cálculo de tasa semántica a partir de una matriz de confusión semántica.

Supongamos que una fuente semántica puede generar dos estados de igual probabilidad:

- $S_1$: “peatón presente”;
- $S_2$: “peatón ausente”.

Luego:

$$
P(S_1)=P(S_2)=0.5
$$

La entropía semántica inicial es:

$$
H_s(S) = -\sum_{i=1}^{2} P(S_i)\log_2 P(S_i) = 1\ \text{bit semántico}
$$

El receptor semántico cumple:

$$
P(\hat{S}=S|S)=0.9, \qquad P(\hat{S}\neq S|S)=0.1
$$

Es decir, el canal semántico es binario simétrico con probabilidad de error $0.1$. Entonces:

$$
H_s(S|\hat{S}) = H_2(0.1) = -0.1\log_2 0.1 - 0.9\log_2 0.9
$$

$$
H_s(S|\hat{S}) \approx 0.469\ \text{bits semánticos}
$$

La tasa semántica es:

$$
R_s = H_s(S)-H_s(S|\hat{S}) = 1-0.469 = 0.531\ \text{bits semánticos/uso}
$$

**Interpretación:** aunque el sistema no preserve todo el significado, aún transmite de manera útil aproximadamente el $53.1\%$ del bit semántico máximo por uso.

**Ejemplo 5.10:** similitud coseno y distorsión semántica.

Supongamos que el significado original y el reconstruido se representan por *embeddings*:

$$
\mathbf{e}(S) = [1,\ 2,\ 2]^T, \qquad \mathbf{e}(\hat{S}) = [1,\ 1,\ 2]^T
$$

Producto interno:

$$
\mathbf{e}(S)^T\mathbf{e}(\hat{S}) = 1\cdot 1 + 2\cdot 1 + 2\cdot 2 = 7
$$

Normas:

$$
\|\mathbf{e}(S)\|_2 = \sqrt{1^2+2^2+2^2}=3
$$

$$
\|\mathbf{e}(\hat{S})\|_2 = \sqrt{1^2+1^2+2^2}=\sqrt{6}\approx 2.449
$$

Similitud coseno:

$$
\mathrm{Sim}_{\cos}(S,\hat{S}) = \frac{7}{3\sqrt{6}} \approx 0.953
$$

Si definimos distorsión semántica como:

$$
d_s = 1-\mathrm{Sim}_{\cos}
$$

entonces:

$$
d_s \approx 1-0.953 = 0.047
$$

**Conclusión:** la reconstrucción presenta un error sintáctico o representacional, pero la pérdida de significado es pequeña.

**Ejemplo 5.11:** Task Success Rate y eficiencia espectral semántica.

Un sistema transmite descripciones semánticas a razón de:

$$
R_s = 2\times 10^6\ \text{bits semánticos/s}
$$

sobre un canal de ancho de banda:

$$
B = 5\times 10^6\ \text{Hz}
$$

La eficiencia espectral semántica es:

$$
\eta_s = \frac{R_s}{B} = \frac{2\times 10^6}{5\times 10^6} = 0.4\ \text{bits semánticos/s/Hz}
$$

Si, además, la tarea final tiene éxito en 92 de cada 100 intentos:

$$
\mathrm{TSR}=0.92
$$

entonces la eficiencia espectral semántica orientada a tarea es:

$$
\eta_{s,T} = \frac{R_s\cdot \mathrm{TSR}}{B} = 0.4\times 0.92 = 0.368\ \text{bits semánticos/s/Hz}
$$

**Interpretación:** no toda la información semántica transmitida se traduce en éxito operativo; al ponderar por TSR obtenemos una medida más realista del valor útil del enlace.

**Ejemplo 5.12:** comparación numérica entre transmisión clásica y transmisión semántica orientada a tarea.

Supongamos dos estrategias para asistencia a conducción:

- **estrategia A (clásica):** transmite una imagen comprimida de $1$ Mbit por trama con éxito de tarea del $98\%$;
- **estrategia B (semántica):** transmite solo objetos, trayectorias y alertas, usando $0.12$ Mbit por trama con éxito del $95\%$.

Definimos una utilidad simple por trama como:

$$
U = \frac{\mathrm{TSR}}{\text{bits transmitidos}}
$$

Para A:

$$
U_A = \frac{0.98}{1} = 0.98\ \text{éxitos/Mbit}
$$

Para B:

$$
U_B = \frac{0.95}{0.12} \approx 7.92\ \text{éxitos/Mbit}
$$

Aunque la estrategia clásica logra un TSR ligeramente mayor, la estrategia semántica ofrece una utilidad por bit mucho más alta.

**Conclusión:** cuando el recurso crítico es ancho de banda o latencia, una representación semántica puede ser claramente preferible.

**Ejemplo 5.13:** asignación de recursos consciente de semántica.

Dos usuarios compiten por $10$ unidades de recurso radio. Sea $r_1+r_2=10$. La utilidad semántica se modela como:

$$
u_1(r_1)=4\log(1+r_1), \qquad u_2(r_2)=2\log(1+r_2)
$$

Maximizamos:

$$
\max_{r_1,r_2}\ 4\log(1+r_1)+2\log(1+r_2)
$$

sujeto a $r_1+r_2=10$.

Sustituyendo $r_2=10-r_1$:

$$
f(r_1)=4\log(1+r_1)+2\log(11-r_1)
$$

Derivando e igualando a cero:

$$
f'(r_1)=\frac{4}{1+r_1}-\frac{2}{11-r_1}=0
$$

$$
4(11-r_1)=2(1+r_1)
$$

$$
44-4r_1 = 2 + 2r_1
$$

$$
42 = 6r_1 \Rightarrow r_1 = 7
$$

Por tanto:

$$
r_2 = 3
$$

**Interpretación:** el usuario 1 recibe más recursos porque su utilidad semántica marginal es mayor.

### 5.4.7 Discusión final: de bits a significado, y de significado a acción

La evolución conceptual puede resumirse así:

1. **Shannon:** transmitir símbolos con fiabilidad.
2. **JSCC/DeepJSCC:** aprender representaciones robustas extremo a extremo.
3. **Comunicaciones semánticas:** preservar significado relevante.
4. **Comunicaciones orientadas a tareas:** maximizar éxito de decisión o control.

Desde el punto de vista pedagógico, esto no implica desechar la teoría clásica. Al contrario: BER, capacidad, SNR, codificación y detección óptima siguen siendo la base. Lo nuevo es que ahora debemos añadir una capa de modelado donde el recurso escaso no es solo el bit, sino también la **atención de la red**, la **relevancia contextual** y la **utilidad para la tarea**.

---

## Resumen de conceptos clave

- Una red neuronal implementa una composición de transformaciones lineales y no lineales:

$$
\mathbf{a}^{[l]}=f^{[l]}(\mathbf{W}^{[l]}\mathbf{a}^{[l-1]}+\mathbf{b}^{[l]})
$$

- La pérdida cuantifica el error entre predicción y verdad de referencia; destacan MSE, BCE y entropía cruzada.
- La retropropagación aplica sistemáticamente la regla de la cadena para obtener gradientes.
- El descenso del gradiente y Adam permiten entrenar redes profundas.
- Un receptor neuronal aprende a detectar símbolos o bits desde muestras recibidas.
- Los autoencoders modelan el sistema transmisor-canal-receptor como una arquitectura entrenable *end-to-end*.
- En 6G, la IA será una capacidad nativa distribuida entre nube, borde y dispositivos.
- Técnicas como aprendizaje federado, Split Learning y RL distribuido serán esenciales para entrenar inteligencia sin centralizar todos los datos.
- Gemelos digitales e ISAC permitirán redes que observan, simulan, predicen y actúan.
- La teoría de Shannon mide información sintáctica, no significado.
- Las comunicaciones semánticas introducen variables de significado $S$, métricas de tarea y nociones como tasa semántica, distorsión semántica y capacidad semántica.
- DeepJSCC actúa como puente entre codificación conjunta clásica y comunicaciones semánticas modernas.
- En sistemas de próxima generación, la métrica relevante ya no será solo BER o throughput, sino también TSR, similitud semántica y eficiencia espectral semántica.

---

## Referencias

1. C. E. Shannon y W. Weaver, *The Mathematical Theory of Communication*. University of Illinois Press, 1949.
2. R. Carnap y Y. Bar-Hillel, *An Outline of a Theory of Semantic Information*. MIT Research Laboratory of Electronics, Technical Report No. 247, 1952.
3. L. Floridi, “Outline of a Theory of Strongly Semantic Information,” *Minds and Machines*, vol. 14, no. 2, pp. 197-221, 2004.
4. I. Goodfellow, Y. Bengio y A. Courville, *Deep Learning*. MIT Press, 2016. Disponible en: https://www.deeplearningbook.org/
5. T. J. O'Shea y J. Hoydis, “An Introduction to Deep Learning for the Physical Layer,” *IEEE Transactions on Cognitive Communications and Networking*, vol. 3, no. 4, pp. 563-575, 2017. DOI: $10.1109/TCCN.2017.2758370$.
6. D. B. Kurka y D. Gündüz, “DeepJSCC for Wireless Image Transmission,” *IEEE Transactions on Cognitive Communications and Networking*, vol. 5, no. 3, pp. 567-579, 2019. DOI: $10.1109/TCCN.2019.2919300$.
7. H. Xie, Z. Qin, G. Y. Li y B.-H. Juang, “Deep Learning Enabled Semantic Communication Systems,” *IEEE Transactions on Signal Processing*, vol. 69, pp. 2663-2675, 2021.
8. D. Gündüz, P. de Kerret, N. D. Sidiropoulos, D. Gesbert, C. Murthy y M. van der Schaar, “Beyond Transmitting Bits: Context, Semantics, and Task-Oriented Communications,” *IEEE Journal on Selected Areas in Communications*, vol. 41, no. 1, pp. 5-41, 2023.
9. International Telecommunication Union, Radiocommunication Sector, **Recommendation ITU-R M.2160-0**: *Framework and overall objectives of the future development of IMT for 2030 and beyond*, 2023. Disponible en: https://www.itu.int/rec/R-REC-M.2160/en
10. F. Liu, Y.-F. Liu, A. Li, C. Masouros, Y. C. Eldar y S. Cui, “Integrated Sensing and Communications: Toward Dual-Functional Wireless Networks for 6G and Beyond,” *IEEE Journal on Selected Areas in Communications*, vol. 40, no. 6, pp. 1728-1767, 2022. DOI: $10.1109/JSAC.2022.3156632$.
11. C. Zhang, Y. Huang, Z. Yang, Y. Chen, C. Yuen y M. Debbah, “Edge Artificial Intelligence for 6G: Vision, Enabling Technologies, and Applications,” *IEEE Journal on Selected Areas in Communications*, vol. 40, no. 1, pp. 5-36, 2022. DOI: $10.1109/JSAC.2021.3126062$.
12. A. Alkhateeb, Y. Jiang y H. Wymeersch, “Real-Time Digital Twins: Vision and Research Directions for 6G and Beyond,” *IEEE Communications Magazine*, vol. 61, no. 11, 2023.
