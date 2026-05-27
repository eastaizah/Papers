# 9. Temas Avanzados en Comunicaciones Semánticas

Las secciones anteriores de este tutorial han establecido los fundamentos teóricos, las arquitecturas basadas en aprendizaje profundo y los esquemas de codificación conjunta fuente-canal para comunicaciones semánticas. En esta sección, nos adentramos en los temas más avanzados y las fronteras de investigación que están definiendo el futuro de esta disciplina. Desde la conformación inteligente de formas de onda hasta la integración con sistemas MIMO masivo, desde las bandas de frecuencia milimétricas y de terahercios hasta la convergencia con sensing integrado, cada uno de estos temas representa una dirección de investigación activa con profundas implicaciones para las redes de sexta generación (6G). Abordaremos también el papel transformador de los modelos fundacionales multimodales, el aprendizaje federado como mecanismo de entrenamiento distribuido y privado, la necesidad de un plano de control semántico, y finalmente, las perspectivas futuras que situarán a las comunicaciones semánticas como un pilar fundamental de las arquitecturas 6G (Luo et al., 2022, DOI: 10.1109/COMST.2022.3195590).

---

## 9.1 Conformación de formas de onda semánticas

### 9.1.1 Diseño tradicional de formas de onda

En los sistemas de comunicación convencionales, el diseño de la forma de onda constituye una etapa claramente separada dentro de la cadena de transmisión. Las técnicas de modulación y multiplexación determinan cómo los bits de información se mapean a señales analógicas para su transmisión a través del canal físico. Las dos formas de onda dominantes en las comunicaciones móviles modernas son OFDM (*Orthogonal Frequency Division Multiplexing*) y SC-FDMA (*Single Carrier Frequency Division Multiple Access*).

En OFDM, el ancho de banda disponible se divide en $N$ subportadoras ortogonales, cada una de las cuales transporta un símbolo modulado de manera independiente. La señal transmitida en el dominio del tiempo puede expresarse como:

$$x(t) = \sum_{k=0}^{N-1} X[k] \, e^{j2\pi f_k t}, \quad 0 \leq t \leq T_s$$

donde $X[k]$ es el símbolo complejo asignado a la $k$-ésima subportadora, $f_k = f_0 + k\Delta f$ es la frecuencia de dicha subportadora con espaciado $\Delta f = 1/T_s$, y $T_s$ es la duración del símbolo OFDM. La ortogonalidad entre subportadoras garantiza que:

$$\int_0^{T_s} e^{j2\pi f_k t} \cdot e^{-j2\pi f_m t} \, dt = \begin{cases} T_s & \text{si } k = m \\ 0 & \text{si } k \neq m \end{cases}$$

Esta propiedad permite que cada subportadora sea demodulada independientemente en el receptor mediante una transformada rápida de Fourier (FFT), lo que simplifica enormemente la ecualización en canales con desvanecimiento selectivo en frecuencia. Sin embargo, OFDM presenta limitaciones: una alta relación potencia pico a potencia media (PAPR, *Peak-to-Average Power Ratio*), sensibilidad al desplazamiento de frecuencia Doppler, y la necesidad de un prefijo cíclico que reduce la eficiencia espectral.

SC-FDMA, utilizada en el enlace ascendente de LTE, aborda el problema del PAPR al realizar un pre-codificación DFT antes de la asignación de subportadoras, produciendo una señal con características más cercanas a una portadora única:

$$\tilde{X}[k] = \frac{1}{\sqrt{M}} \sum_{m=0}^{M-1} x[m] \, e^{-j2\pi mk/M}$$

donde $x[m]$ son los símbolos en el dominio del tiempo y $M$ es el número de símbolos agrupados. Esta transformación reduce significativamente el PAPR, lo cual es crítico para dispositivos móviles con amplificadores de potencia limitados.

En ambos casos, los símbolos $X[k]$ provienen de constelaciones de modulación predefinidas como QPSK, 16-QAM o 64-QAM, donde cada punto de la constelación corresponde a una secuencia fija de bits. Por ejemplo, en 16-QAM, los 16 puntos de la constelación se distribuyen en una cuadrícula regular en el plano complejo:

$$X \in \left\{ (\pm 1 \pm j\cdot 3, \pm 3 \pm j\cdot 1, \pm 1 \pm j\cdot 1, \pm 3 \pm j\cdot 3) \cdot d_{\min}/2 \right\}$$

donde $d_{\min}$ es la distancia mínima entre puntos. Esta distribución uniforme y simétrica está diseñada para maximizar la distancia euclidiana mínima bajo una restricción de potencia promedio, optimizando así la tasa de error de bit (BER) en canales con ruido gaussiano aditivo blanco (AWGN).

### 9.1.2 Formas de onda aprendidas: el codificador de canal como conformador

El paradigma de comunicaciones semánticas introduce un cambio radical en el diseño de formas de onda. En lugar de separar las etapas de codificación fuente, codificación de canal y modulación, un sistema semántico extremo a extremo integra todas estas funciones en una red neuronal conjunta. El resultado es que la salida del codificador de canal neuronal **es directamente la forma de onda transmitida**, sin necesidad de pasar por un modulador convencional.

Formalmente, sea $\mathbf{s}$ la fuente semántica (texto, imagen, audio) y $f_\theta(\cdot)$ el codificador semántico conjunto parametrizado por $\theta$. La señal transmitida se genera como:

$$\mathbf{x} = f_\theta(\mathbf{s}) \in \mathbb{C}^n$$

donde $\mathbf{x}$ es un vector de $n$ símbolos complejos que se transmiten directamente a través del canal. No existe una etapa separada de mapeo a constelación: la red neuronal aprende simultáneamente a extraer características semánticas, comprimir la información, protegerla contra errores del canal y conformar la señal para cumplir con restricciones físicas.

Para que esta forma de onda aprendida sea físicamente realizable, debe cumplir con la restricción de potencia promedio:

$$\frac{1}{n} \mathbb{E}\left[\|\mathbf{x}\|^2\right] \leq P_{\max}$$

Esta restricción se implementa típicamente mediante una capa de normalización al final del codificador. Una implementación común es la normalización por lote (*batch normalization*):

$$\mathbf{x}_{\text{norm}} = \sqrt{nP_{\max}} \cdot \frac{\mathbf{x}}{\|\mathbf{x}\|}$$

que garantiza que la potencia total transmitida sea exactamente $nP_{\max}$.

### 9.1.3 Densidad espectral de potencia y restricciones regulatorias

Además de la restricción de potencia total, las señales transmitidas deben cumplir con restricciones sobre la densidad espectral de potencia (PSD, *Power Spectral Density*). Las regulaciones de espectro imponen máscaras espectrales que limitan la potencia emitida en cada banda de frecuencia:

$$S_x(f) \leq S_{\text{máscara}}(f), \quad \forall f$$

donde $S_x(f) = \lim_{T\to\infty} \frac{1}{T}\mathbb{E}\left[|X_T(f)|^2\right]$ es la PSD de la señal transmitida y $S_{\text{máscara}}(f)$ es la máscara espectral regulatoria. Incorporar esta restricción en el entrenamiento de una red neuronal no es trivial, ya que implica una restricción en el dominio de la frecuencia sobre una señal generada en el dominio del tiempo.

Una solución propuesta es incluir un término de penalización en la función de pérdida del entrenamiento:

$$\mathcal{L}_{\text{total}} = \mathcal{L}_{\text{semántica}} + \lambda_{\text{PSD}} \cdot \max\left(0, \max_f \left[S_x(f) - S_{\text{máscara}}(f)\right]\right)$$

donde $\mathcal{L}_{\text{semántica}}$ es la pérdida de distorsión semántica (por ejemplo, pérdida de similitud SSIM para imágenes o BLEU para texto) y $\lambda_{\text{PSD}}$ es un multiplicador que controla la importancia de la restricción espectral. Alternativamente, se pueden utilizar filtros conformadores de espectro diferenciables como capas finales de la red, permitiendo que el gradiente fluya a través de ellos durante el entrenamiento.

### 9.1.4 Constelaciones aprendidas vs. constelaciones tradicionales

Una de las propiedades más fascinantes de las formas de onda semánticas es que los puntos en el espacio de señal ya no se distribuyen según patrones geométricos regulares (cuadrículas QAM, anillos PSK), sino que adoptan distribuciones aprendidas y adaptadas al canal y a la tarea semántica.

En un autoencoder de comunicación entrenado extremo a extremo, si visualizamos la distribución de los símbolos transmitidos en el plano complejo $(\text{Re}(x), \text{Im}(x))$, observamos que los puntos de la "constelación aprendida" presentan las siguientes características:

1. **Distribución no uniforme**: los puntos se agrupan de manera desigual, con mayor densidad en regiones del espacio de señal que corresponden a características semánticas frecuentes o importantes.

2. **Geometría adaptada al canal**: en un canal AWGN, los puntos tienden a distribuirse en configuraciones que maximizan la distancia mínima, similares pero no idénticas a QAM. En canales con desvanecimiento Rayleigh, la distribución se adapta para ser más robusta, con puntos más separados y agrupaciones que explotan la diversidad.

3. **Codificación semántica implícita**: puntos que corresponden a características semánticas similares (por ejemplo, imágenes del mismo objeto con diferentes orientaciones) se mapean a regiones cercanas del espacio de señal, creando una estructura de código continuo que permite una degradación graceful.

4. **Adaptación a la relación señal a ruido (SNR)**: a SNR bajas, la constelación se "contrae" hacia configuraciones más simples con mayor separación entre puntos, mientras que a SNR altas, los puntos se distribuyen más finamente para aprovechar la alta capacidad del canal.

La relación entre la distancia semántica y la distancia euclidiana en el espacio de señal puede formalizarse como:

$$d_{\text{semántica}}(\mathbf{s}_i, \mathbf{s}_j) \propto \|\mathbf{x}_i - \mathbf{x}_j\|^2$$

donde $\mathbf{s}_i, \mathbf{s}_j$ son dos fuentes semánticas y $\mathbf{x}_i = f_\theta(\mathbf{s}_i)$, $\mathbf{x}_j = f_\theta(\mathbf{s}_j)$ son sus representaciones en el espacio de señal. Esta propiedad, que emerge naturalmente del entrenamiento conjunto, no existe en los sistemas convencionales donde la modulación es independiente del contenido.

**Figura 9.1:** *Comparación entre una constelación QAM tradicional y una constelación semántica aprendida. Panel izquierdo: constelación 16-QAM convencional con 16 puntos distribuidos en una cuadrícula regular $4 \times 4$ en el plano complejo $(\text{Re}(x), \text{Im}(x))$, donde cada punto representa una secuencia fija de 4 bits y todos los puntos tienen igual importancia. Panel derecho: constelación semántica aprendida por un autoencoder entrenado extremo a extremo para transmisión de imágenes sobre un canal con desvanecimiento Rayleigh. Los puntos se distribuyen de manera no uniforme, con agrupaciones (*clusters*) que corresponden a categorías semánticas distintas (por ejemplo, diferentes objetos en las imágenes). Se observan regiones de alta densidad para categorías semánticas frecuentes y mayor separación entre clusters que representan significados semánticamente distantes. Los puntos no siguen un patrón geométrico regular, sino que adoptan una distribución optimizada conjuntamente para la compresión semántica, la protección contra errores y la eficiencia espectral.*

---

## 9.2 Comunicaciones semánticas para MIMO masivo

### 9.2.1 Modelo del sistema MIMO

Los sistemas MIMO (*Multiple-Input Multiple-Output*) constituyen una de las tecnologías más importantes de las comunicaciones inalámbricas modernas, al explotar la dimensión espacial para multiplicar la capacidad del canal sin requerir ancho de banda adicional. En un sistema MIMO con $N_t$ antenas de transmisión y $N_r$ antenas de recepción, la relación entrada-salida se expresa mediante la ecuación matricial fundamental:

$$\mathbf{Y} = \mathbf{H}\mathbf{X} + \mathbf{N}$$

donde $\mathbf{Y} \in \mathbb{C}^{N_r \times T}$ es la matriz de señales recibidas a lo largo de $T$ instantes de tiempo, $\mathbf{H} \in \mathbb{C}^{N_r \times N_t}$ es la matriz de canal que captura las ganancias complejas entre cada par de antenas transmisora-receptora, $\mathbf{X} \in \mathbb{C}^{N_t \times T}$ es la matriz de señales transmitidas, y $\mathbf{N} \in \mathbb{C}^{N_r \times T}$ es la matriz de ruido gaussiano con entradas i.i.d. $\mathcal{CN}(0, \sigma^2)$.

Cada elemento $h_{ij}$ de la matriz $\mathbf{H}$ representa el coeficiente de canal complejo desde la $j$-ésima antena transmisora hasta la $i$-ésima antena receptora. En un entorno de dispersión rica (*rich scattering*), estos coeficientes se modelan como variables aleatorias complejas gaussianas independientes, dando lugar al modelo de canal de Rayleigh:

$$h_{ij} \sim \mathcal{CN}(0, 1)$$

La capacidad ergódica del canal MIMO, bajo el supuesto de conocimiento perfecto del canal en el receptor (CSIR) y distribución uniforme de potencia entre antenas, está dada por la célebre expresión:

$$C = \mathbb{E}_{\mathbf{H}}\left[\log_2\det\left(\mathbf{I}_{N_r} + \frac{P}{N_t\sigma^2}\mathbf{H}\mathbf{H}^H\right)\right]$$

donde $P$ es la potencia total de transmisión, $\mathbf{I}_{N_r}$ es la matriz identidad de dimensión $N_r$, y $(\cdot)^H$ denota la transpuesta conjugada (hermitiana). Esta expresión revela una propiedad fundamental: en el régimen de alta SNR, la capacidad crece linealmente con $\min(N_t, N_r)$, es decir:

$$C \approx \min(N_t, N_r) \cdot \log_2\left(\frac{P}{N_t \sigma^2}\right) \quad \text{(alta SNR)}$$

Cuando el transmisor también conoce el canal (CSIT), se puede aplicar la descomposición en valores singulares (SVD) $\mathbf{H} = \mathbf{U}\mathbf{\Sigma}\mathbf{V}^H$ para diagonalizar el canal en $r = \text{rank}(\mathbf{H})$ canales paralelos independientes con ganancias $\sigma_1 \geq \sigma_2 \geq \cdots \geq \sigma_r > 0$, y la capacidad se maximiza mediante asignación de potencia *water-filling*:

$$C_{\text{CSIT}} = \sum_{i=1}^{r} \log_2\left(1 + \frac{p_i \sigma_i^2}{\sigma_n^2}\right)$$

donde $p_i = \left(\mu - \sigma_n^2/\sigma_i^2\right)^+$ y $\mu$ se elige para satisfacer la restricción de potencia total $\sum_i p_i = P$.

### 9.2.2 Precodificación en sistemas semánticos

En los sistemas MIMO convencionales, la precodificación es una operación lineal que se aplica a los símbolos modulados antes de la transmisión para dirigir la energía hacia las direcciones espaciales deseadas. La señal transmitida precodificada es:

$$\mathbf{X} = \mathbf{W}\mathbf{S}$$

donde $\mathbf{W} \in \mathbb{C}^{N_t \times d}$ es la matriz de precodificación y $\mathbf{S} \in \mathbb{C}^{d \times T}$ contiene los $d$ flujos de datos independientes. Esquemas clásicos de precodificación incluyen *zero-forcing* ($\mathbf{W} = \mathbf{H}^H(\mathbf{H}\mathbf{H}^H)^{-1}$) y MMSE.

En el contexto de las comunicaciones semánticas, la precodificación se integra directamente dentro del codificador neuronal, eliminando la separación tradicional entre codificación y precodificación. El codificador semántico MIMO puede modelarse como:

$$\mathbf{X} = f_\theta(\mathbf{s}, \mathbf{H}) \in \mathbb{C}^{N_t \times T}$$

donde ahora el codificador $f_\theta$ recibe no solo la fuente semántica $\mathbf{s}$ sino también el estado del canal $\mathbf{H}$ (o una estimación de este), y produce directamente la señal a transmitir por todas las $N_t$ antenas. Esta formulación permite que la red neuronal aprenda simultáneamente:

1. **Extracción de características semánticas**: identificar qué información es relevante del mensaje fuente.
2. **Compresión adaptativa**: ajustar la tasa de compresión según las condiciones del canal MIMO.
3. **Asignación de potencia espacial**: distribuir la potencia entre las antenas de manera óptima, aprendiendo implícitamente una versión no lineal del *water-filling*.
4. **Conformación de haz semántica**: dirigir las características semánticas más importantes a través de los modos espaciales con mejor ganancia, y las menos importantes por modos con menor ganancia, logrando una degradación graceful en la reconstrucción.

La función de pérdida para el entrenamiento del sistema semántico MIMO incorpora tanto la fidelidad semántica como las restricciones de potencia:

$$\mathcal{L} = \mathbb{E}_{\mathbf{s}, \mathbf{H}}\left[d_{\text{sem}}\left(\mathbf{s}, g_\phi\left(\mathbf{H}f_\theta(\mathbf{s}, \mathbf{H}) + \mathbf{N}\right)\right)\right] + \lambda \cdot \left(\frac{1}{T}\mathbb{E}\left[\text{tr}(\mathbf{X}\mathbf{X}^H)\right] - P\right)^2$$

donde $g_\phi(\cdot)$ es el decodificador semántico en el receptor, $d_{\text{sem}}$ es una distancia semántica apropiada y $\text{tr}(\cdot)$ denota la traza matricial.

### 9.2.3 Conformación de haz (*beamforming*) integrada con codificación semántica

La conformación de haz o *beamforming* permite dirigir la energía transmitida hacia direcciones específicas en el espacio, lo que es especialmente importante en MIMO masivo donde $N_t \gg 1$. En sistemas convencionales, el vector de *beamforming* analógico para dirigir el haz hacia un ángulo $\theta$ es:

$$\mathbf{a}(\theta) = \frac{1}{\sqrt{N_t}}\left[1, e^{j\frac{2\pi d}{\lambda}\sin\theta}, e^{j\frac{2\pi \cdot 2d}{\lambda}\sin\theta}, \ldots, e^{j\frac{2\pi(N_t-1)d}{\lambda}\sin\theta}\right]^T$$

donde $d$ es el espaciado entre antenas y $\lambda$ es la longitud de onda.

En un sistema semántico con *beamforming*, la arquitectura puede diseñarse como:

$$\mathbf{x}[t] = \sum_{m=1}^{M} \mathbf{w}_m \cdot s_m[t] = \mathbf{W}\mathbf{s}[t]$$

donde $\mathbf{s}[t] = [s_1[t], \ldots, s_M[t]]^T$ son los $M$ flujos de símbolos semánticos y $\mathbf{W} = [\mathbf{w}_1, \ldots, \mathbf{w}_M]$ es la matriz de *beamforming*. La clave de la innovación semántica es que tanto $\mathbf{s}[t]$ como $\mathbf{W}$ son generados conjuntamente por la red neuronal, permitiendo que la conformación de haz se adapte al contenido semántico del mensaje.

Por ejemplo, en un sistema de transmisión de video, el codificador semántico MIMO podría asignar los flujos que contienen información del fondo de la escena (menos relevante semánticamente) a haces con menor ganancia, mientras que los flujos que contienen información de objetos en primer plano o movimiento se asignan a haces con mayor ganancia y menor probabilidad de error. Esta priorización semántica del *beamforming* no tiene análogo en los sistemas convencionales, donde la modulación es independiente del contenido.

### 9.2.4 Convergencia de características semánticas entre antenas

Un fenómeno particularmente interesante en los sistemas semánticos MIMO es la convergencia de las representaciones semánticas a través de las múltiples antenas. Cuando el codificador semántico produce $N_t$ flujos de señal (uno por antena), surge la pregunta de cómo se distribuye la información semántica entre estos flujos.

Los estudios empíricos han mostrado que durante el entrenamiento, las redes neuronales semánticas MIMO aprenden a realizar una especie de "factorización semántica" donde diferentes aspectos del mensaje se separan naturalmente en diferentes flujos espaciales. Esto puede analizarse mediante la información mutua entre cada flujo transmitido y la fuente:

$$I(\mathbf{s}; x_i) \quad \text{para cada antena } i = 1, \ldots, N_t$$

En un codificador semántico MIMO bien entrenado, se observa que $I(\mathbf{s}; x_1) > I(\mathbf{s}; x_2) > \cdots > I(\mathbf{s}; x_{N_t})$, es decir, existe una jerarquía natural de importancia semántica entre los flujos, análoga a los valores singulares decrecientes de la descomposición SVD del canal. Esta convergencia permite implementar estrategias de transmisión robustas donde los flujos menos importantes pueden sacrificarse si las condiciones del canal se deterioran, sin pérdida significativa de fidelidad semántica.

**Figura 9.2:** *Sistema MIMO semántico con $N_t = 4$ antenas de transmisión y $N_r = 4$ antenas de recepción. En el transmisor, la fuente semántica (una imagen) ingresa al codificador semántico basado en red neuronal profunda, que produce $N_t$ flujos de salida paralelos, cada uno alimentando una antena distinta. Los flujos están etiquetados jerárquicamente: el flujo 1 contiene las características semánticas de más alta prioridad (estructura global de la imagen), el flujo 2 contiene características de nivel medio (texturas y bordes), el flujo 3 contiene detalles finos y el flujo 4 contiene información residual. Las señales se propagan a través del canal MIMO representado por la matriz $\mathbf{H}$, con flechas que indican los $N_t \times N_r = 16$ caminos de propagación. En el receptor, las $N_r$ antenas capturan la señal combinada, que se alimenta al decodificador semántico neuronal para reconstruir la imagen. Se muestra también el módulo de estimación de canal que proporciona $\hat{\mathbf{H}}$ al codificador (vía retroalimentación) y al decodificador.*

---

## 9.3 Comunicaciones semánticas en bandas milimétricas (mmWave) y THz

### 9.3.1 Desafíos en altas frecuencias

Las bandas de frecuencia milimétricas (mmWave, 30–300 GHz) y de terahercios (THz, 0.1–10 THz) ofrecen anchos de banda extraordinarios que pueden soportar tasas de datos de múltiples gigabits por segundo e incluso terabits por segundo. Sin embargo, estas frecuencias presentan desafíos físicos fundamentales que limitan severamente su aprovechamiento en sistemas convencionales.

La pérdida en el espacio libre (*free-space path loss*, FSPL) sigue la ecuación de Friis y aumenta cuadráticamente con la frecuencia:

$$\text{FSPL}(f, d) = \left(\frac{4\pi d f}{c}\right)^2$$

donde $d$ es la distancia, $f$ es la frecuencia portadora y $c$ es la velocidad de la luz. A 300 GHz, la FSPL es 40 dB mayor que a 3 GHz para la misma distancia, lo que significa que la potencia recibida es $10{,}000$ veces menor. Esta atenuación se compensa parcialmente mediante el uso de antenas altamente directivas (arreglos masivos), pero esto introduce el problema de haces extremadamente estrechos que requieren alineamiento preciso.

Adicionalmente, las frecuencias mmWave y THz sufren de:

- **Atenuación atmosférica**: la absorción por moléculas de agua y oxígeno crea ventanas de transmisión y bandas de absorción. A 60 GHz existe una banda de absorción por oxígeno de aproximadamente 15 dB/km, y en THz existen múltiples líneas de absorción por vapor de agua.

- **Bloqueo por obstáculos**: la difracción es mínima a estas frecuencias, por lo que cualquier obstáculo sólido (personas, muebles, paredes) puede causar una atenuación de 20-40 dB o bloqueo total del enlace. El fenómeno de bloqueo puede modelarse como:

$$P_{\text{bloqueo}} = 1 - e^{-\beta d}$$

donde $\beta$ es la densidad de obstáculos bloqueantes por unidad de distancia.

- **Haces estrechos**: el ancho de haz de media potencia para un arreglo lineal uniforme (ULA) es aproximadamente $\theta_{3\text{dB}} \approx \frac{2}{N_t}$ radianes, lo que para $N_t = 256$ antenas resulta en haces de menos de 0.5°. Esto requiere procedimientos de búsqueda de haz (*beam search*) costosos en tiempo y energía.

### 9.3.2 Valor de las comunicaciones semánticas en mmWave/THz

Las comunicaciones semánticas son especialmente valiosas en las bandas mmWave y THz debido a una asimetría fundamental en estas bandas: **el ancho de banda es abundante, pero el enlace es frágil**. Esta combinación crea un escenario donde la compresión semántica y la robustez ante interrupciones se vuelven críticas.

**Compresión semántica para reducir la tasa requerida**: En un enlace THz con 10 GHz de ancho de banda disponible, la capacidad teórica máxima podría ser de 40 Gbps. Sin embargo, debido a las limitaciones de potencia y la alta atenuación, la capacidad práctica podría ser solo de 1 Gbps durante períodos de buen enlace y caer a cero durante bloqueos. Un codificador semántico que comprima una imagen de 10 MB a 100 KB (relación de compresión 100:1) mientras preserva la información semántica relevante permite transmitir la imagen en $100 \times 8 / 10^9 = 0.8$ ms, minimizando la exposición a eventos de bloqueo.

La tasa semántica efectiva puede definirse como:

$$R_{\text{sem}} = \frac{S(\mathbf{s}) - S(\mathbf{s}|\hat{\mathbf{s}})}{n \cdot T_s}$$

donde $S(\mathbf{s})$ es la entropía semántica de la fuente, $S(\mathbf{s}|\hat{\mathbf{s}})$ es la incertidumbre semántica residual después de la reconstrucción, $n$ es el número de símbolos transmitidos y $T_s$ es la duración de cada símbolo.

**Robustez ante conectividad intermitente**: Los sistemas semánticos pueden diseñarse para transmitir primero las características semánticas más importantes y luego refinar progresivamente. Si el enlace se interrumpe después de transmitir solo el 30% de los símbolos, el decodificador semántico puede aún reconstruir una versión útil del mensaje. Esto se logra mediante esquemas de codificación progresiva semántica:

$$\hat{\mathbf{s}}_k = g_\phi\left(\mathbf{y}_1, \mathbf{y}_2, \ldots, \mathbf{y}_k\right), \quad k = 1, 2, \ldots, n$$

donde $\hat{\mathbf{s}}_k$ es la reconstrucción basada en los primeros $k$ símbolos recibidos. La calidad semántica mejora monótonamente con $k$: $d_{\text{sem}}(\mathbf{s}, \hat{\mathbf{s}}_1) \geq d_{\text{sem}}(\mathbf{s}, \hat{\mathbf{s}}_2) \geq \cdots \geq d_{\text{sem}}(\mathbf{s}, \hat{\mathbf{s}}_n)$.

**Reducción de la sobrecarga de búsqueda de haz**: El proceso convencional de búsqueda de haz requiere transmitir pilotos en múltiples direcciones, lo que consume tiempo y energía. Un sistema semántico puede utilizar la información semántica del canal (por ejemplo, la geometría del entorno percibida a través de estimaciones de canal previas) para predecir la dirección óptima del haz, reduciendo significativamente la sobrecarga.

### 9.3.3 Modulación OTFS para canales de alta movilidad

La modulación OTFS (*Orthogonal Time Frequency Space*) es una técnica de multiplexación diseñada para operar eficientemente en canales de alta movilidad, donde el desplazamiento Doppler varía rápidamente y degrada severamente el rendimiento de OFDM. OTFS opera en el dominio retardo-Doppler (*delay-Doppler domain*), donde el canal se representa de manera más compacta y estable.

En el dominio retardo-Doppler, el canal se modela como una función de dispersión:

$$h(\tau, \nu) = \sum_{p=1}^{P} h_p \, \delta(\tau - \tau_p) \, \delta(\nu - \nu_p)$$

donde $P$ es el número de caminos de propagación, $h_p$ es la ganancia compleja, $\tau_p$ es el retardo y $\nu_p$ es el desplazamiento Doppler del $p$-ésimo camino. En el dominio discreto, la relación entrada-salida OTFS se expresa como:

$$\mathbf{Y}[k,l] = \sum_{k'=0}^{N-1}\sum_{l'=0}^{M-1} \mathbf{H}[k-k',l-l']\mathbf{X}[k',l'] + \mathbf{N}[k,l]$$

donde $\mathbf{X}[k',l']$ y $\mathbf{Y}[k,l]$ son los símbolos transmitidos y recibidos en el punto $(k',l')$ y $(k,l)$ de la cuadrícula retardo-Doppler respectivamente, con $k = 0, \ldots, N-1$ indexando la dimensión Doppler y $l = 0, \ldots, M-1$ indexando la dimensión de retardo. La función de transferencia del canal discretizada es:

$$\mathbf{H}[k,l] = \sum_{p=1}^{P} h_p \, e^{-j2\pi \frac{k \nu_p}{N\Delta\nu}} \, \delta[l - l_p]$$

donde $l_p = \tau_p / \Delta\tau$ es el índice de retardo discreto y $\Delta\nu$, $\Delta\tau$ son las resoluciones en Doppler y retardo, respectivamente.

La ventaja fundamental de OTFS sobre OFDM es que en el dominio retardo-Doppler, el canal es **cuasi-estático**: mientras que en OFDM la matriz de canal varía rápidamente en el dominio tiempo-frecuencia (cada subportadora experimenta un desvanecimiento diferente y variante en el tiempo), en OTFS la representación retardo-Doppler del canal cambia lentamente incluso en escenarios de alta movilidad. Esto significa que:

1. Cada símbolo OTFS experimenta efectivamente el **canal completo** (toda la diversidad), lo que elimina el problema de desvanecimiento profundo que afecta a subportadoras individuales en OFDM.
2. La estimación de canal es más eficiente, ya que solo se necesita estimar $P$ coeficientes complejos (uno por camino) en lugar de $N \times M$ coeficientes en el dominio tiempo-frecuencia.
3. La ecualización se simplifica significativamente en el dominio retardo-Doppler.

### 9.3.4 Integración de OTFS con codificación semántica

La sinergia entre OTFS y comunicaciones semánticas es particularmente prometedora. El codificador semántico puede diseñarse para operar directamente en el dominio retardo-Doppler:

$$\mathbf{X}_{\text{DD}} = f_\theta(\mathbf{s}) \in \mathbb{C}^{N \times M}$$

donde $\mathbf{X}_{\text{DD}}$ es la cuadrícula de símbolos semánticos en el dominio retardo-Doppler. La red neuronal aprende a colocar las características semánticas más importantes en las posiciones de la cuadrícula que experimentan mejor calidad de canal, y las menos importantes en posiciones con menor calidad.

La ventaja de esta integración es triple: (1) el codificador semántico puede explotar la cuasi-estacionariedad del canal retardo-Doppler para producir representaciones más eficientes; (2) la diversidad completa del canal beneficia a todas las características semánticas; y (3) la estimación de canal simplificada puede integrarse como una capa de la red neuronal, permitiendo un sistema verdaderamente extremo a extremo que funcione eficientemente incluso en las desafiantes condiciones de las bandas THz con alta movilidad.

---

## 9.4 Sensing semántico: ISAC (Integrated Sensing and Communications)

### 9.4.1 Comunicaciones y sensado integrado

ISAC (*Integrated Sensing and Communications*) es un paradigma emergente que busca la convergencia de las funciones de radar (sensado) y comunicaciones en un único sistema, compartiendo hardware, forma de onda y recursos espectrales. En lugar de diseñar sistemas de radar y comunicaciones de manera independiente y gestionando la interferencia entre ellos, ISAC los unifica para lograr eficiencia espectral, energética y de costos.

En un sistema ISAC, la señal transmitida $\mathbf{x}(t)$ sirve simultáneamente dos propósitos:

1. **Comunicación**: transportar información semántica desde el transmisor al receptor.
2. **Sensado**: iluminar objetivos en el entorno y analizar los ecos reflejados para extraer información sobre posición, velocidad, forma y tipo de los objetos.

La señal recibida en el receptor de comunicación es:

$$\mathbf{y}_{\text{com}}(t) = \mathbf{h}_{\text{com}}(t) * \mathbf{x}(t) + \mathbf{n}_{\text{com}}(t)$$

mientras que la señal de eco recibida por el radar es:

$$\mathbf{y}_{\text{radar}}(t) = \sum_{q=1}^{Q} \alpha_q \, \mathbf{x}(t - \tau_q) \, e^{j2\pi \nu_q t} + \mathbf{n}_{\text{radar}}(t)$$

donde $Q$ es el número de objetivos, $\alpha_q$ es el coeficiente de reflexión del $q$-ésimo objetivo (relacionado con su sección transversal de radar, RCS), $\tau_q = 2d_q/c$ es el retardo de ida y vuelta proporcional a la distancia $d_q$, y $\nu_q = 2v_q f_c/c$ es el desplazamiento Doppler proporcional a la velocidad radial $v_q$.

El desafío fundamental de ISAC es diseñar la señal $\mathbf{x}(t)$ y los algoritmos de procesamiento para optimizar simultáneamente el rendimiento de ambas funciones, que tienen requerimientos potencialmente conflictivos. La comunicación requiere alta entropía en la señal (aleatoriedad para transportar información), mientras que el radar tradicional prefiere señales deterministas con buenas propiedades de autocorrelación.

### 9.4.2 Sensado semántico: extracción de información del canal

En el marco de las comunicaciones semánticas, la función de sensado adquiere una dimensión adicional: el **sensado semántico**. En lugar de simplemente estimar parámetros físicos del canal (retardos, Doppler, ángulos), un sistema de sensado semántico busca extraer información de alto nivel sobre el entorno.

La estimación del canal puede verse como una forma fundamental de sensado. Cuando el sistema estima la matriz de canal $\hat{\mathbf{H}}$, está implícitamente capturando información sobre el entorno de propagación:

$$\hat{\mathbf{H}} = \sum_{p=1}^{P} \hat{h}_p \, \mathbf{a}_r(\hat{\theta}_{r,p}) \, \mathbf{a}_t^H(\hat{\theta}_{t,p}) \, e^{-j2\pi \hat{\tau}_p f}$$

donde $\hat{\theta}_{r,p}$ y $\hat{\theta}_{t,p}$ son los ángulos de llegada y salida estimados del $p$-ésimo camino, $\hat{\tau}_p$ es el retardo estimado, y $\mathbf{a}_r$, $\mathbf{a}_t$ son los vectores de dirección del arreglo de antenas.

El sensado semántico va más allá: utiliza una red neuronal para inferir características de alto nivel del entorno a partir de los parámetros de canal estimados:

$$\mathbf{c}_{\text{env}} = h_\psi(\hat{\mathbf{H}}_1, \hat{\mathbf{H}}_2, \ldots, \hat{\mathbf{H}}_T)$$

donde $h_\psi$ es una red neuronal de sensado semántico que procesa una secuencia temporal de estimaciones de canal $\{\hat{\mathbf{H}}_t\}$ para inferir un vector de características ambientales $\mathbf{c}_{\text{env}}$ que puede incluir:

- Número y tipo de objetos en el entorno (personas, vehículos, obstáculos).
- Actividad de las personas (caminando, sentado, gesticulando) — lo que se conoce como reconocimiento de actividad basado en Wi-Fi.
- Mapa del entorno (localización de paredes, muebles, puertas).
- Condiciones atmosféricas (lluvia, niebla) que afectan la propagación.

### 9.4.3 Sección transversal de radar y extracción de características semánticas

La sección transversal de radar (RCS, *Radar Cross Section*) $\sigma_{\text{RCS}}$ de un objetivo cuantifica cuánta energía de la señal incidente es reflejada hacia el radar. Para un objetivo puntual, la potencia recibida sigue la ecuación del radar:

$$P_r = \frac{P_t G_t G_r \lambda^2 \sigma_{\text{RCS}}}{(4\pi)^3 d^4}$$

donde $P_t$ es la potencia transmitida, $G_t$ y $G_r$ son las ganancias de antena de transmisión y recepción, $\lambda$ es la longitud de onda y $d$ es la distancia al objetivo.

En un sistema ISAC semántico, la RCS no se trata como un simple escalar, sino como una función del ángulo, la frecuencia y la polarización que contiene una "huella" del objetivo:

$$\sigma_{\text{RCS}}(\theta, \phi, f, \hat{p}_r, \hat{p}_t) = \lim_{d\to\infty} 4\pi d^2 \frac{|\mathbf{E}_s(\theta, \phi)|^2}{|\mathbf{E}_i|^2}$$

donde $\mathbf{E}_s$ y $\mathbf{E}_i$ son los campos eléctricos dispersado e incidente. Un codificador semántico de sensado puede extraer características de alto nivel a partir de esta firma:

$$\hat{c}_{\text{objeto}} = f_{\text{sense}}(\sigma_{\text{RCS}}(\theta, \phi, f))$$

clasificando el tipo de objetivo (peatón, automóvil, ciclista), estimando sus dimensiones y prediciendo su trayectoria futura.

### 9.4.4 Función dual: comunicar y sensar simultáneamente

La función dual ISAC en el contexto semántico puede formalizarse como un problema de optimización multiobjetivo:

$$\min_{\theta, \phi, \mathbf{X}} \quad \alpha \cdot \mathcal{L}_{\text{com}}(\theta, \phi, \mathbf{X}) + (1-\alpha) \cdot \mathcal{L}_{\text{sense}}(\mathbf{X})$$

sujeto a:

$$\frac{1}{T}\text{tr}(\mathbf{X}\mathbf{X}^H) \leq P, \quad S_x(f) \leq S_{\text{máscara}}(f)$$

donde $\mathcal{L}_{\text{com}}$ es la pérdida de comunicación semántica (por ejemplo, la distorsión en la reconstrucción), $\mathcal{L}_{\text{sense}}$ es la pérdida de sensado (por ejemplo, el error en la detección o clasificación de objetos), y $\alpha \in [0,1]$ es un parámetro de compromiso (*trade-off*) que balancea ambos objetivos.

La red neuronal conjunta puede diseñarse con una estructura de codificador compartido y dos decodificadores especializados:

$$\mathbf{z} = f_{\text{encoder}}(\mathbf{s})$$
$$\mathbf{X} = f_{\text{waveform}}(\mathbf{z})$$
$$\hat{\mathbf{s}} = g_{\text{com}}(\mathbf{y}_{\text{com}})$$
$$\hat{\mathbf{c}} = g_{\text{sense}}(\mathbf{y}_{\text{radar}})$$

donde $\mathbf{z}$ es una representación latente compartida, $f_{\text{waveform}}$ genera la forma de onda que sirve tanto para comunicación como para sensado, y $g_{\text{com}}$, $g_{\text{sense}}$ son los decodificadores de comunicación y sensado, respectivamente.

**Figura 9.3:** *Sistema ISAC (*Integrated Sensing and Communications*) semántico. El transmisor contiene un codificador semántico que genera una forma de onda $\mathbf{x}(t)$ de función dual. Esta forma de onda se irradia a través de un arreglo de antenas MIMO. Parte de la energía llega al receptor de comunicación (usuario) a través del canal directo, donde el decodificador semántico reconstruye el mensaje original $\hat{\mathbf{s}}$. Simultáneamente, la misma señal ilumina objetos en el entorno (un vehículo, un peatón), y los ecos reflejados son captados por las antenas del transmisor (en configuración mono-estática) o por antenas separadas (configuración bi-estática). El procesador de sensado semántico analiza los ecos para extraer información de alto nivel: tipo de objeto, posición $(x, y)$, velocidad $v$ y dirección de movimiento. Se muestra la coexistencia del flujo de datos semántico (línea sólida, del Tx al Rx de comunicación) y el flujo de sensado (línea discontinua, del Tx al objetivo y de vuelta), ambos utilizando la misma señal transmitida y los mismos recursos espectrales.*

---

## 9.5 Modelos fundacionales multimodales para comunicaciones semánticas

### 9.5.1 Modelos preentrenados como columna vertebral semántica

Los modelos fundacionales (*foundation models*) representan un cambio de paradigma en la inteligencia artificial. Estos modelos masivos, preentrenados con enormes volúmenes de datos heterogéneos, aprenden representaciones generales del mundo que pueden transferirse a una amplia variedad de tareas. Los ejemplos más destacados incluyen los modelos de lenguaje grande (LLMs, *Large Language Models*) como GPT y los transformadores de visión (ViTs, *Vision Transformers*).

La integración de modelos fundacionales en comunicaciones semánticas ofrece ventajas fundamentales:

1. **Representaciones semánticas ricas**: Los modelos fundacionales aprenden representaciones que capturan relaciones semánticas profundas entre conceptos. Un ViT preentrenado en millones de imágenes ha aprendido a distinguir entre objetos, escenas, acciones y atributos a múltiples niveles de abstracción. Un LLM ha aprendido la estructura del lenguaje, el conocimiento del mundo y las relaciones lógicas. Estas representaciones son intrínsecamente semánticas.

2. **Generalización**: A diferencia de los codificadores semánticos entrenados desde cero para una tarea específica, los modelos fundacionales generalizan a distribuciones de datos nunca vistas durante el entrenamiento. Esto es crucial en comunicaciones, donde la distribución de los datos fuente puede variar significativamente entre usuarios y contextos.

3. **Eficiencia de datos**: El entrenamiento de un codificador semántico desde cero requiere grandes conjuntos de datos pareados (fuente-canal-reconstrucción). Con un modelo fundacional como inicialización, se requieren significativamente menos datos de entrenamiento específico de comunicación.

La arquitectura de un sistema semántico basado en modelos fundacionales puede formularse como:

$$\mathbf{z} = f_{\text{proj}}\left(f_{\text{fund}}(\mathbf{s})\right)$$
$$\mathbf{x} = f_{\text{canal}}(\mathbf{z})$$

donde $f_{\text{fund}}(\cdot)$ es el modelo fundacional preentrenado (cuyos pesos pueden congelarse o ajustarse finamente), $f_{\text{proj}}(\cdot)$ es una capa de proyección que adapta la representación del modelo fundacional al espacio de transmisión, y $f_{\text{canal}}(\cdot)$ es el codificador de canal neuronal. La representación $\mathbf{z}$ reside en un espacio semántico de dimensión típicamente mucho menor que la dimensión de la fuente original.

### 9.5.2 Aprendizaje por transferencia para tareas de comunicación

El aprendizaje por transferencia (*transfer learning*) permite adaptar los modelos fundacionales a la tarea específica de comunicación semántica. El procedimiento típico involucra las siguientes etapas:

**Etapa 1: Preentrenamiento** (ya completada por los desarrolladores del modelo fundacional). El modelo $f_{\text{fund}}$ se entrena con un objetivo genérico (por ejemplo, predicción de palabras enmascaradas para LLMs, o clasificación de imágenes para ViTs) usando un conjunto de datos masivo $\mathcal{D}_{\text{pre}}$:

$$\theta_{\text{fund}}^* = \arg\min_\theta \sum_{(\mathbf{x},y) \in \mathcal{D}_{\text{pre}}} \mathcal{L}_{\text{pre}}(f_\theta(\mathbf{x}), y)$$

**Etapa 2: Ajuste fino (*fine-tuning*) para comunicación**. Se congela la mayor parte de los pesos del modelo fundacional y se entrenan las capas adicionales (proyección y codificador de canal) junto con un ajuste fino de las últimas capas del modelo fundacional:

$$(\theta_{\text{proj}}^*, \theta_{\text{canal}}^*, \theta_{\text{dec}}^*) = \arg\min \mathbb{E}_{\mathbf{s}, \mathbf{H}} \left[\mathcal{L}_{\text{sem}}\left(\mathbf{s}, g_{\theta_{\text{dec}}}\left(\mathbf{H} \cdot f_{\theta_{\text{canal}}}(f_{\theta_{\text{proj}}}(f_{\text{fund}}(\mathbf{s}))) + \mathbf{n}\right)\right)\right]$$

**Etapa 3: Adaptación continua**. El modelo se sigue adaptando durante la operación en función de las condiciones del canal y la distribución de los datos de los usuarios.

Una técnica particularmente eficiente para el ajuste fino es LoRA (*Low-Rank Adaptation*), donde en lugar de modificar todos los pesos del modelo fundacional, se añaden matrices de bajo rango que capturan las adaptaciones necesarias:

$$\mathbf{W}_{\text{adaptado}} = \mathbf{W}_{\text{fund}} + \mathbf{B}\mathbf{A}$$

donde $\mathbf{W}_{\text{fund}} \in \mathbb{R}^{d \times d}$ es la matriz de pesos original (congelada), $\mathbf{B} \in \mathbb{R}^{d \times r}$ y $\mathbf{A} \in \mathbb{R}^{r \times d}$ son matrices entrenables de bajo rango $r \ll d$. Esto reduce drásticamente el número de parámetros a entrenar de $d^2$ a $2dr$, lo que es crucial para el despliegue en dispositivos con recursos limitados.

### 9.5.3 Comunicación semántica multimodal

Los sistemas de comunicación del futuro no transportarán un solo tipo de datos, sino flujos multimodales integrados: texto, imágenes, audio, video, datos de sensores y señales de control, todos ellos portadores de significado semántico interrelacionado. La comunicación semántica multimodal busca explotar estas relaciones para lograr una compresión y protección más eficientes.

El modelo de un sistema semántico multimodal puede formalizarse como:

$$\mathbf{z}_{\text{fusión}} = f_{\text{fusión}}\left(f_{\text{texto}}(\mathbf{s}_{\text{texto}}), f_{\text{imagen}}(\mathbf{s}_{\text{imagen}}), f_{\text{audio}}(\mathbf{s}_{\text{audio}})\right)$$

donde $f_{\text{texto}}$, $f_{\text{imagen}}$, $f_{\text{audio}}$ son codificadores semánticos específicos de cada modalidad (potencialmente basados en modelos fundacionales), y $f_{\text{fusión}}$ es un módulo de fusión que combina las representaciones de las diferentes modalidades en un espacio semántico unificado.

La fusión puede realizarse mediante mecanismos de atención cruzada (*cross-attention*):

$$\text{CrossAttn}(\mathbf{Q}_i, \mathbf{K}_j, \mathbf{V}_j) = \text{softmax}\left(\frac{\mathbf{Q}_i \mathbf{K}_j^T}{\sqrt{d_k}}\right)\mathbf{V}_j$$

donde $\mathbf{Q}_i$ proviene de la modalidad $i$ y $\mathbf{K}_j$, $\mathbf{V}_j$ provienen de la modalidad $j$, permitiendo que cada modalidad atienda a la información relevante de las demás.

La ventaja clave de la comunicación multimodal semántica es la **redundancia intermodal**: la información contenida en una modalidad puede ayudar a reconstruir o completar la información de otra. Por ejemplo, en una videollamada, si se pierden fotogramas de video, el audio puede ayudar a inferir las expresiones faciales del hablante; si se corrompe el audio, el movimiento de los labios en el video puede ayudar a reconstruir el habla. Esta redundancia se explota naturalmente por los modelos fundacionales multimodales, que aprenden alineaciones semánticas entre modalidades.

### 9.5.4 La base de conocimiento (KB) compartida

Un concepto fundamental en las comunicaciones semánticas es la **base de conocimiento** (*Knowledge Base*, KB) compartida entre el transmisor y el receptor (Shi et al., 2021, DOI: 10.1109/JSAC.2021.3126078). Esta KB representa el conocimiento común que ambos extremos poseen y que permite la interpretación correcta del mensaje semántico.

En el contexto de modelos fundacionales, la KB puede identificarse con los pesos del modelo preentrenado compartido:

$$\text{KB} = \{\theta_{\text{fund}}\}$$

Cuando tanto el transmisor como el receptor utilizan el mismo modelo fundacional (o versiones compatibles), comparten implícitamente una vasta base de conocimiento que incluye:

- Conocimiento lingüístico: gramática, semántica léxica, relaciones entre conceptos.
- Conocimiento visual: tipos de objetos, escenas, relaciones espaciales.
- Conocimiento del mundo: hechos, relaciones causales, expectativas contextuales.

La eficiencia de la comunicación semántica depende directamente de la riqueza y alineación de las KBs:

$$R_{\text{sem}} \propto \frac{1}{H(\mathbf{s} | \text{KB})}$$

donde $H(\mathbf{s} | \text{KB})$ es la entropía condicional de la fuente dado el conocimiento compartido. Cuanto mayor sea el conocimiento compartido, menor será la información que necesita transmitirse explícitamente, y mayor será la eficiencia semántica.

### 9.5.5 Comunicación semántica basada en ontologías

Las ontologías proporcionan una estructura formal para representar el conocimiento y las relaciones entre conceptos. En comunicaciones semánticas, una ontología compartida entre Tx y Rx define un vocabulario común de conceptos, propiedades y relaciones que permite una comunicación extremadamente eficiente.

Una ontología puede representarse como un grafo dirigido:

$$\mathcal{O} = (\mathcal{C}, \mathcal{R}, \mathcal{A})$$

donde $\mathcal{C}$ es un conjunto de conceptos (nodos), $\mathcal{R}$ es un conjunto de relaciones (aristas) entre conceptos, y $\mathcal{A}$ es un conjunto de axiomas que definen restricciones y reglas de inferencia. En este marco, un mensaje semántico se codifica como un subgrafo de la ontología:

$$\mathbf{m} = (\mathcal{C}_m \subseteq \mathcal{C}, \mathcal{R}_m \subseteq \mathcal{R})$$

La eficiencia de esta representación radica en que transmitir las identidades de los conceptos y relaciones activados (que pueden codificarse como índices enteros) es vastamente más eficiente que transmitir los datos crudos. Por ejemplo, transmitir la tripleta ontológica *(perro, persigue, gato)* requiere solo tres índices, mientras que una imagen o video que muestre esta escena requeriría millones de bits. Naturalmente, esto presupone que ambos extremos comparten la ontología y la capacidad de generar o interpretar representaciones a partir de las tripletas ontológicas.

---

## 9.6 Aprendizaje federado para comunicaciones semánticas

### 9.6.1 Entrenamiento distribuido con preservación de privacidad

El entrenamiento de codificadores y decodificadores semánticos requiere grandes volúmenes de datos que frecuentemente residen en dispositivos de los usuarios (teléfonos móviles, cámaras, sensores IoT). Centralizar estos datos en un servidor para el entrenamiento plantea serios problemas de privacidad, ancho de banda y latencia. El aprendizaje federado (*Federated Learning*, FL) ofrece una solución elegante al permitir el entrenamiento colaborativo de modelos sin compartir datos crudos.

En el paradigma de FL, cada dispositivo $k$ posee un conjunto de datos local $\mathcal{D}_k = \{(\mathbf{s}_i^{(k)}, \tilde{\mathbf{s}}_i^{(k)})\}_{i=1}^{n_k}$ donde $\mathbf{s}_i^{(k)}$ es una muestra de la fuente semántica y $\tilde{\mathbf{s}}_i^{(k)}$ es la reconstrucción objetivo (o la fuente misma en esquemas autoencoder). El objetivo global del entrenamiento es minimizar la pérdida agregada:

$$\min_\theta \mathcal{L}(\theta) = \sum_{k=1}^{K} \frac{n_k}{n} \mathcal{L}_k(\theta)$$

donde $K$ es el número de dispositivos participantes, $n_k = |\mathcal{D}_k|$ es el tamaño del conjunto de datos local, $n = \sum_{k=1}^K n_k$ es el tamaño total, y $\mathcal{L}_k(\theta)$ es la pérdida local del dispositivo $k$:

$$\mathcal{L}_k(\theta) = \frac{1}{n_k} \sum_{i=1}^{n_k} \ell\left(\mathbf{s}_i^{(k)}, g_\phi\left(h_{\text{canal}}\left(f_\theta\left(\mathbf{s}_i^{(k)}\right)\right)\right)\right)$$

donde $\ell$ es la función de pérdida por muestra (distorsión semántica), $f_\theta$ es el codificador semántico, $h_{\text{canal}}$ simula el efecto del canal (durante el entrenamiento), y $g_\phi$ es el decodificador semántico.

### 9.6.2 Formulación del aprendizaje federado

El algoritmo FedAvg (*Federated Averaging*), la variante más utilizada de FL, procede en rondas de comunicación. En cada ronda $t$:

**Paso 1: Distribución del modelo global.** El servidor envía el modelo global actual $\theta^t$ a un subconjunto $\mathcal{S}_t \subseteq \{1, \ldots, K\}$ de dispositivos seleccionados.

**Paso 2: Entrenamiento local.** Cada dispositivo $k \in \mathcal{S}_t$ realiza $E$ épocas de SGD local:

$$\theta_k^{t,e+1} = \theta_k^{t,e} - \eta_{\text{local}} \nabla \mathcal{L}_k(\theta_k^{t,e}), \quad e = 0, 1, \ldots, E-1$$

con $\theta_k^{t,0} = \theta^t$. La actualización local se define como $\Delta\theta_k^t = \theta_k^{t,E} - \theta^t$.

**Paso 3: Agregación.** El servidor recibe las actualizaciones locales y calcula el modelo global actualizado mediante promedio ponderado:

$$\theta^{t+1} = \theta^t + \sum_{k \in \mathcal{S}_t} \frac{n_k}{\sum_{j \in \mathcal{S}_t} n_j} \Delta\theta_k^t$$

que es equivalente a la actualización:

$$\theta^{t+1} = \theta^t - \eta \sum_{k=1}^{K} \frac{n_k}{n} \nabla \mathcal{L}_k(\theta^t)$$

en el caso idealizado de $E = 1$ paso local y selección de todos los dispositivos, donde $\eta$ es la tasa de aprendizaje global. Esta es la formulación clásica del aprendizaje federado.

### 9.6.3 Codificación semántica local y agregación en el servidor

En el contexto específico de las comunicaciones semánticas, la aplicación de FL presenta características particulares. Cada dispositivo entrena localmente tanto su codificador semántico como su decodificador. Sin embargo, surge una asimetría natural:

- **El codificador** se ejecuta en el dispositivo del usuario (transmisor) y debe adaptarse a la distribución local de datos de ese usuario.
- **El decodificador** puede ejecutarse en una estación base o servidor (receptor) y debe ser universal, capaz de decodificar mensajes de cualquier usuario.

Esta asimetría sugiere una estrategia de FL diferenciada:

$$\theta_{\text{enc}}^{t+1} = \text{FedAvg}\left(\{\theta_{\text{enc},k}^t\}_{k \in \mathcal{S}_t}\right) + \alpha_k \cdot \Delta\theta_{\text{personal},k}$$

$$\theta_{\text{dec}}^{t+1} = \text{FedAvg}\left(\{\theta_{\text{dec},k}^t\}_{k \in \mathcal{S}_t}\right)$$

donde el codificador incluye un componente de personalización $\Delta\theta_{\text{personal},k}$ que permite adaptar la codificación a las particularidades de cada usuario (tipo de datos, distribución estadística, preferencias), mientras que el decodificador se mantiene completamente compartido para garantizar la interoperabilidad.

### 9.6.4 Modelos semánticos adaptativos que aprenden de condiciones de red

Una ventaja clave del FL para comunicaciones semánticas es la capacidad de entrenar modelos que se adaptan continuamente a las condiciones cambiantes de la red. Cada dispositivo experimenta condiciones de canal únicas (SNR, modelo de desvanecimiento, interferencia) que varían con el tiempo y la ubicación.

Un modelo semántico adaptativo puede parametrizarse condicionalmente:

$$\mathbf{x} = f_\theta(\mathbf{s} ; \mathbf{c}_{\text{canal}})$$

donde $\mathbf{c}_{\text{canal}}$ es un vector de contexto del canal que incluye la SNR estimada, el perfil de retardo de potencia, el esparcimiento Doppler, etc. El FL permite que los modelos aprendan de la diversidad de condiciones de canal experimentadas por todos los dispositivos del sistema, produciendo codificadores más robustos que los entrenados solo con datos de un único dispositivo o con modelos de canal sintéticos.

La diversidad de las condiciones de canal entre los dispositivos participantes actúa como una forma de regularización natural que previene el sobreajuste a un modelo de canal particular. Formalmente, si $p_k(\mathbf{H})$ es la distribución del canal experimentada por el dispositivo $k$, el modelo federado se entrena implícitamente bajo la distribución mezcla:

$$p(\mathbf{H}) = \sum_{k=1}^{K} \frac{n_k}{n} p_k(\mathbf{H})$$

que es más rica y diversa que cualquier distribución individual.

### 9.6.5 Detección de deriva semántica y actualización de modelos

Un problema crítico en sistemas semánticos desplegados es la **deriva semántica** (*semantic drift*): la degradación gradual del rendimiento del sistema cuando las distribuciones de los datos o las condiciones del canal cambian con respecto a las condiciones de entrenamiento. El FL proporciona un mecanismo natural para detectar y corregir la deriva semántica.

La detección de deriva puede realizarse monitoreando la pérdida local de cada dispositivo:

$$\delta_k^t = \mathcal{L}_k(\theta^t) - \mathcal{L}_k(\theta^{t-\Delta t})$$

Si $\delta_k^t > \epsilon_{\text{drift}}$ para una fracción significativa de dispositivos, se activa un ciclo de reentrenamiento federado. Adicionalmente, la divergencia entre los gradientes locales puede indicar que los dispositivos están experimentando distribuciones de datos incompatibles:

$$D_{\text{grad}}^t = \frac{1}{K(K-1)} \sum_{i \neq j} \left\|  \nabla \mathcal{L}_i(\theta^t) - \nabla \mathcal{L}_j(\theta^t) \right\|^2$$

Un valor alto de $D_{\text{grad}}^t$ sugiere heterogeneidad en los datos o condiciones de canal, lo que puede requerir estrategias de personalización más agresivas o incluso la segmentación de los dispositivos en clusters con condiciones similares.

---

## 9.7 El plano de control semántico

### 9.7.1 La cabecera semántica

En las comunicaciones convencionales, cada paquete de datos incluye cabeceras de protocolo que describen el tipo de datos, la dirección de destino, la secuencia, los mecanismos de control de errores, etc. En las comunicaciones semánticas, surge la necesidad de una **cabecera semántica** (*Semantic Header*) que describa las propiedades del contenido semántico y los metadatos necesarios para su correcta decodificación e interpretación.

La cabecera semántica puede incluir los siguientes campos:

1. **Tipo de fuente semántica**: texto, imagen, audio, video, datos de sensores, multimodal.
2. **Nivel de abstracción semántica**: indica la granularidad de la representación (píxeles, objetos, escena, concepto abstracto).
3. **Identificador del modelo codificador/decodificador**: referencia al modelo neuronal utilizado para la codificación, necesario para que el receptor seleccione el decodificador compatible.
4. **Versión de la base de conocimiento**: identifica la versión de la KB utilizada, crucial para detectar desincronización.
5. **Importancia semántica**: prioridad del paquete basada en su relevancia semántica para la tarea del receptor.
6. **Mapa de confianza**: indica la fiabilidad estimada de cada componente semántico.
7. **Dependencias semánticas**: identifica relaciones con otros paquetes semánticos (por ejemplo, un paquete de refinamiento que depende de un paquete base).

Formalmente, la cabecera semántica $\mathbf{h}_{\text{sem}}$ puede representarse como:

$$\mathbf{h}_{\text{sem}} = (\text{tipo}, \text{nivel}, \text{id\_modelo}, \text{ver\_KB}, \text{prioridad}, \mathbf{conf}, \text{deps})$$

Un desafío de diseño importante es el equilibrio entre la riqueza de la cabecera (que permite una decodificación e interpretación más precisa) y su sobrecarga (que reduce la eficiencia espectral). En sistemas semánticos altamente comprimidos, una cabecera excesivamente grande puede dominar el tamaño del paquete.

### 9.7.2 Modificaciones al modelo OSI para comunicaciones semánticas

El modelo de referencia OSI (*Open Systems Interconnection*) de siete capas ha sido el marco conceptual dominante para las arquitecturas de redes de comunicación durante décadas. Sin embargo, este modelo fue diseñado para la transmisión fiable de bits, sin consideración alguna del significado de la información transportada. Las comunicaciones semánticas requieren una reestructuración fundamental del modelo OSI.

Las modificaciones principales incluyen:

**Capa semántica**: Una nueva capa se inserta entre la capa de aplicación (Capa 7) y la capa de presentación (Capa 6). Esta capa es responsable de:
- Extracción de significado de los datos de la aplicación.
- Compresión semántica.
- Priorización basada en relevancia semántica.
- Gestión de la base de conocimiento compartida.

**Fusión de capas inferiores**: En los sistemas semánticos extremo a extremo, las capas de presentación, sesión, transporte y red pueden fusionarse parcialmente, ya que la codificación conjunta fuente-canal elimina la separación entre la representación de datos y la protección contra errores.

**Capa de codificación conjunta fuente-canal semántica (JSCC semántico)**: Reemplaza las funciones separadas de las capas 2 (enlace de datos), 3 (red) y 4 (transporte) para la codificación y protección de datos, integrándolas en un único bloque neuronal.

### 9.7.3 Pila de protocolos semántica

La pila de protocolos semántica propuesta redefine las interacciones entre capas:

**Nivel 1 — Capa física semántica**: Genera directamente la forma de onda a transmitir a partir de las características semánticas. Integra modulación, codificación de canal y conformación de onda en una operación neuronal unificada.

**Nivel 2 — Capa de enlace semántico**: Gestiona la transmisión de unidades de datos semánticos (SDUs, *Semantic Data Units*) entre nodos adyacentes. Implementa control de acceso al medio (MAC) basado en prioridad semántica y mecanismos de retransmisión selectiva semántica (solo se retransmiten las componentes con mayor pérdida semántica).

**Nivel 3 — Capa de red semántica**: Enruta los paquetes semánticos basándose no solo en la dirección de destino sino también en el contenido semántico. Permite el procesamiento semántico en nodos intermedios (*semantic relay*) donde la información puede ser recodificada, resumida o filtrada semánticamente.

**Nivel 4 — Capa de control semántico**: Gestiona la sincronización de bases de conocimiento, la negociación de modelos codificador/decodificador, la detección de deriva semántica y la calidad de experiencia semántica.

**Nivel 5 — Capa de aplicación semántica**: Interfaz con las aplicaciones del usuario, proporcionando APIs para la transmisión y recepción de datos semánticos con diferentes niveles de abstracción y fidelidad.

### 9.7.4 Calidad de experiencia (QoE) vs. calidad de servicio (QoS)

En las comunicaciones convencionales, la calidad del servicio se mide mediante métricas técnicas como el *throughput*, la latencia, la tasa de error de bit (BER) y el *jitter*. Estas métricas son objetivas y medibles en la capa física y de enlace, pero no capturan necesariamente la calidad percibida por el usuario.

Las comunicaciones semánticas naturalmente se alinean con métricas de Calidad de Experiencia (QoE), que miden la satisfacción del usuario con el servicio recibido. La relación entre QoS y QoE no es lineal; por ejemplo, una mejora del 50% en BER podría traducirse en una mejora imperceptible en la calidad de video percibida, o podría ser la diferencia entre un video utilizable e inutilizable.

Las métricas semánticas de QoE incluyen:

- **Fidelidad semántica**: ¿Se preservó el significado del mensaje? Medida mediante distancias en el espacio semántico:

$$\text{SF} = 1 - \frac{d_{\text{sem}}(\mathbf{s}, \hat{\mathbf{s}})}{d_{\text{sem}}^{\max}}$$

- **Relevancia de la tarea**: ¿Fue útil la información recibida para la tarea del receptor? Medida mediante la precisión en tareas posteriores (*downstream task accuracy*).

- **Oportunidad semántica** (*semantic timeliness*): ¿Llegó la información a tiempo para ser relevante? Generalización del concepto de *Age of Information* (AoI) al dominio semántico:

$$\text{AoSI}(t) = t - U_{\text{sem}}(t)$$

donde $U_{\text{sem}}(t)$ es el tiempo de generación de la actualización semántica más reciente cuyo contenido sigue siendo relevante en el tiempo $t$.

### 9.7.5 Deriva semántica: detección y resincronización

La deriva semántica ocurre cuando los modelos del transmisor y receptor divergen, lo que puede suceder por varias razones:

1. **Actualización asimétrica de modelos**: si uno de los extremos actualiza su modelo neuronal sin sincronizar con el otro.
2. **Cambio en la distribución de datos**: si el tipo de contenido transmitido cambia significativamente respecto al entrenamiento.
3. **Degradación del canal**: si las condiciones del canal cambian de manera que el modelo codificador/decodificador ya no es apropiado.

La detección de deriva semántica puede realizarse monitoreando la similitud semántica entre muestras de referencia. Sea $\mathcal{R} = \{\mathbf{s}_1, \ldots, \mathbf{s}_R\}$ un conjunto de mensajes de referencia conocidos por ambos extremos. Periódicamente, se calcula la fidelidad de reconstrucción:

$$\text{SM}^t = \frac{1}{R}\sum_{r=1}^{R} \text{sim}\left(\mathbf{s}_r, \hat{\mathbf{s}}_r^t\right)$$

donde $\hat{\mathbf{s}}_r^t$ es la reconstrucción del $r$-ésimo mensaje de referencia en el tiempo $t$ y $\text{sim}(\cdot, \cdot)$ es una métrica de similitud semántica (por ejemplo, similitud coseno en el espacio de representación del modelo fundacional). Si $\text{SM}^t < \text{SM}^{t_0} - \delta$, se detecta deriva semántica y se activa un protocolo de resincronización.

Las estrategias de resincronización incluyen:

- **Actualización completa del modelo**: el transmisor envía los pesos actualizados al receptor (o viceversa). Costoso en ancho de banda pero garantiza sincronización completa.
- **Actualización diferencial**: solo se transmiten las diferencias $\Delta\theta = \theta_{\text{nuevo}} - \theta_{\text{antiguo}}$, potencialmente comprimidas.
- **Destilación de conocimiento**: se entrena un modelo estudiante en el receptor utilizando las salidas del modelo actualizado del transmisor como guía, sin necesidad de transmitir los pesos.
- **Negociación de KB**: ambos extremos intercambian resúmenes de sus bases de conocimiento y resuelven discrepancias.

**Figura 9.4:** *Pila de protocolos modificada con capa semántica. Panel izquierdo: modelo OSI convencional de 7 capas (Aplicación, Presentación, Sesión, Transporte, Red, Enlace, Física), donde cada capa opera de manera independiente sobre flujos de bits sin considerar el significado de los datos. Panel derecho: pila de protocolos semántica propuesta. Se muestra una nueva "Capa Semántica" insertada entre la capa de Aplicación y las capas inferiores. Esta capa contiene los módulos de: (1) extracción semántica, (2) codificación conjunta fuente-canal semántica (JSCC), (3) gestión de base de conocimiento (KB), y (4) control de calidad semántica (QoE semántica). Las capas inferiores (Física y Enlace) se simplifican, ya que la codificación conjunta elimina la necesidad de capas separadas de codificación fuente y canal. Se muestran flechas bidireccionales entre la capa semántica y la capa de aplicación (extracción/entrega de significado), y entre la capa semántica y la capa física (generación/procesamiento de la forma de onda). También se ilustra el protocolo de sincronización de KB entre los extremos Tx y Rx, representado como un canal de señalización bidireccional (plano de control semántico) paralelo al canal de datos.*

---

## 9.8 Perspectivas futuras y 6G

### 9.8.1 Comunicación semántica como pilar de 6G

La sexta generación de comunicaciones móviles (6G), cuyo despliegue se anticipa para la década de 2030, promete una transformación radical respecto a 5G. Mientras que 5G se diseñó para conectar personas y dispositivos con altas tasas de datos, baja latencia y alta fiabilidad, 6G aspira a crear un *mundo conectado inteligente* donde la comunicación trasciende la mera transferencia de bits para convertirse en un intercambio de significado y propósito (Strinati et al., 2021, DOI: 10.1109/MNET.011.2000568).

Las comunicaciones semánticas se perfilan como uno de los pilares fundamentales de la arquitectura 6G por las siguientes razones:

**Eficiencia espectral más allá de Shannon**: La teoría de Shannon establece límites fundamentales para la transmisión fiable de bits. Sin embargo, estos límites asumen que todos los bits son igualmente importantes, lo cual no es cierto cuando el objetivo es transmitir significado. Las comunicaciones semánticas pueden operar "más allá" de la capacidad de Shannon en el sentido de que logran una calidad de tarea superior al transmitir menos bits pero más relevantes. Esto no viola el teorema de Shannon, sino que redefine la métrica de éxito de la comunicación.

**Escalabilidad para el Internet de Todo**: 6G contempla escenarios con billones de dispositivos conectados, incluyendo sensores ambientales, robots, vehículos autónomos, dispositivos de realidad extendida y más. La compresión semántica es esencial para manejar estos volúmenes de datos sin precedentes.

**Soporte para aplicaciones de IA distribuida**: Muchas aplicaciones 6G involucrarán inferencia de IA distribuida, donde los datos capturados por un dispositivo deben procesarse en múltiples nodos de la red. Las comunicaciones semánticas permiten que cada nodo transmita solo las características relevantes para la tarea de IA, reduciendo dramáticamente el tráfico de red.

### 9.8.2 IA nativa en la interfaz aérea

El concepto de "IA nativa" (*native AI*) en la interfaz aérea implica que los algoritmos de inteligencia artificial no son una adición opcional a un sistema de comunicaciones convencional, sino que están integrados desde el diseño fundamental de la capa física. Esto significa que:

- Las señales transmitidas no se generan mediante operaciones de procesamiento digital de señales convencional (modulación, codificación, OFDM), sino mediante redes neuronales.
- El receptor no utiliza algoritmos de estimación de canal, ecualización y demodulación separados, sino una red neuronal integrada de extremo a extremo.
- Los estándares de comunicación no definen formatos de modulación y esquemas de codificación fijos, sino arquitecturas de redes neuronales y protocolos de entrenamiento.

La formulación de IA nativa puede expresarse como:

$$\hat{\mathbf{s}} = g_\phi(r(f_\theta(\mathbf{s}))) \approx \mathbf{s}$$

donde todo el procesamiento de señal está encapsulado en las funciones neuronales $f_\theta$ (transmisor) y $g_\phi$ (receptor), y $r(\cdot)$ representa el canal físico real (no un modelo matemático).

Un desafío clave es la estandarización: mientras que los esquemas de modulación convencionales como 64-QAM están completamente especificados por un estándar, una "red neuronal de modulación" tiene millones de parámetros que pueden variar entre implementaciones. Esto requiere nuevos paradigmas de estandarización que especifiquen interfaces, objetivos de rendimiento y protocolos de interoperabilidad en lugar de implementaciones específicas.

### 9.8.3 Comunicación orientada a objetivos (*goal-oriented communication*)

La comunicación orientada a objetivos representa la evolución más avanzada del paradigma semántico. En lugar de medir el éxito por la fidelidad de reconstrucción del mensaje original, se mide por la utilidad del mensaje para lograr un objetivo específico en el receptor.

Formalmente, el problema de comunicación orientada a objetivos puede plantearse como:

$$\max_{\theta, \phi} \mathbb{E}\left[U\left(a\left(g_\phi(\mathbf{y})\right), \omega\right)\right]$$

sujeto a restricciones de recursos (potencia, ancho de banda, latencia), donde $U(a, \omega)$ es la función de utilidad que depende de la acción $a$ tomada por el receptor (basada en el mensaje decodificado) y del estado del mundo $\omega$. La cadena completa es: el transmisor observa $\mathbf{s}$ (que contiene información parcial sobre $\omega$), codifica y transmite $\mathbf{x} = f_\theta(\mathbf{s})$, el receptor decodifica $\hat{\mathbf{s}} = g_\phi(\mathbf{y})$ y toma una acción $a = \pi(\hat{\mathbf{s}})$.

Ejemplos de comunicación orientada a objetivos incluyen:

- **Conducción autónoma**: un vehículo transmite datos de sensores a un servidor de borde. El objetivo no es reconstruir los datos del sensor perfectamente, sino que el servidor tome decisiones de control correctas (frenar, girar, acelerar).
- **Telecirugía**: un cirujano opera remotamente. El objetivo es que los movimientos del robot quirúrgico sean precisos, no que la imagen del campo quirúrgico sea pixel-perfect.
- **Monitoreo ambiental**: sensores IoT reportan condiciones ambientales. El objetivo es que las alertas de desastres sean oportunas y precisas.

### 9.8.4 Seguridad y privacidad semántica

Las comunicaciones semánticas introducen nuevas dimensiones de seguridad y privacidad que no existen en los sistemas convencionales:

**Seguridad semántica**: En criptografía convencional, un sistema es semánticamente seguro si un adversario no puede distinguir entre las encriptaciones de dos mensajes cualesquiera. En comunicaciones semánticas, la seguridad semántica debe extenderse al nivel del significado: un adversario no debe poder inferir el significado del mensaje, incluso si puede observar la señal transmitida y conoce parcialmente el modelo codificador.

La seguridad semántica puede cuantificarse mediante la información mutua entre la observación del adversario y el significado del mensaje:

$$I(\mathbf{s}; \mathbf{y}_{\text{eve}}) \leq \epsilon_{\text{sec}}$$

donde $\mathbf{y}_{\text{eve}}$ es la señal observada por el adversario y $\epsilon_{\text{sec}}$ es el nivel de seguridad deseado.

**Privacidad de atributos**: Además de proteger el mensaje completo, puede ser necesario proteger atributos específicos. Por ejemplo, en una transmisión de imagen de vigilancia, se desea comunicar la actividad (persona caminando) pero ocultar la identidad (rostro). Esto puede lograrse mediante técnicas de aprendizaje de representaciones invariantes:

$$\min_\theta \mathcal{L}_{\text{tarea}}(f_\theta(\mathbf{s})) + \lambda \cdot I(f_\theta(\mathbf{s}); a_{\text{privado}})$$

donde $a_{\text{privado}}$ es el atributo a proteger y el segundo término penaliza las representaciones que contengan información sobre él.

**Ataques adversarios semánticos**: Los sistemas semánticos basados en redes neuronales son vulnerables a ataques adversarios que perturban sutilmente la entrada para causar errores semánticos catastróficos. Una perturbación imperceptible $\delta$ puede hacer que el sistema interprete completamente mal el mensaje:

$$d_{\text{sem}}\left(\mathbf{s}, g_\phi(h_{\text{canal}}(f_\theta(\mathbf{s} + \delta)))\right) \gg d_{\text{sem}}\left(\mathbf{s}, g_\phi(h_{\text{canal}}(f_\theta(\mathbf{s})))\right)$$

con $\|\delta\| \leq \epsilon$. Desarrollar sistemas semánticos robustos a estos ataques es un problema abierto de investigación.

### 9.8.5 Desafíos de estandarización

La estandarización de las comunicaciones semánticas para 6G enfrenta desafíos sin precedentes:

1. **Interoperabilidad**: ¿Cómo garantizar que dispositivos de diferentes fabricantes, con modelos neuronales potencialmente diferentes, puedan comunicarse entre sí? Se requieren estándares que definan formatos de representación semántica, protocolos de negociación de modelos y mecanismos de conversión entre representaciones.

2. **Métricas de rendimiento**: ¿Cómo definir métricas universales de calidad semántica que sean comparables entre diferentes implementaciones y tipos de contenido? Las métricas de distorsión semántica son inherentemente dependientes de la tarea y la aplicación.

3. **Modelo de referencia**: ¿Cómo actualizar el modelo de referencia de protocolos para incorporar capas semánticas manteniendo la compatibilidad con sistemas existentes?

4. **Certificación y pruebas**: ¿Cómo certificar que un sistema semántico cumple con requisitos de rendimiento cuando su comportamiento depende de redes neuronales cuyo funcionamiento detallado no es completamente interpretable?

5. **Aspectos regulatorios**: ¿Cómo regular formas de onda aprendidas que no corresponden a esquemas de modulación estándar? Las agencias regulatorias necesitan nuevos marcos para evaluar la conformidad espectral de señales generadas por redes neuronales.

### 9.8.6 Problemas abiertos de investigación

La investigación en comunicaciones semánticas es un campo vibrante con numerosos problemas abiertos:

- **Teoría de la información semántica rigurosa**: Aunque los trabajos de Bao et al. y otros han avanzado en la formalización teórica, aún no existe un análogo completo de la teoría de Shannon para comunicaciones semánticas. Se necesitan definiciones formales de entropía semántica, capacidad semántica y teoremas de codificación semántica con demostraciones de alcanzabilidad y converso.

- **Métricas de distorsión semántica universales**: Las métricas existentes (BLEU, SSIM, precisión de clasificación) son específicas de un tipo de datos o tarea. Se requieren métricas que capturen la distorsión semántica de manera universal y que permitan comparaciones justas entre sistemas.

- **Codificación semántica de tasa adaptativa**: Sistemas que ajusten dinámicamente la tasa de compresión semántica en función de la complejidad del contenido, las condiciones del canal y los requisitos del usuario, de manera continua y sin interrupciones.

- **Comunicación semántica multiusuario**: La mayoría de los trabajos existentes consideran escenarios punto a punto. Los escenarios multiusuario (acceso múltiple semántico, difusión semántica, relay semántico) presentan desafíos adicionales de interferencia, asignación de recursos y equidad semántica.

- **Complejidad computacional**: Los modelos neuronales utilizados en comunicaciones semánticas pueden ser computacionalmente costosos, especialmente los basados en transformadores. Es necesario desarrollar arquitecturas eficientes que puedan ejecutarse en tiempo real en dispositivos con recursos limitados, manteniendo la calidad semántica.

- **Explicabilidad y confianza**: Para la adopción en sistemas críticos (salud, transporte, seguridad), los sistemas semánticos deben ser interpretables y predecibles. La naturaleza de "caja negra" de las redes neuronales es una barrera significativa.

- **Integración con infraestructura existente**: Los sistemas semánticos deben coexistir con la infraestructura de comunicaciones actual durante un período de transición prolongado. Se necesitan arquitecturas híbridas que puedan operar en modo semántico o convencional según las capacidades de los extremos.

En conclusión, los temas avanzados presentados en esta sección representan las fronteras más activas de la investigación en comunicaciones semánticas. Desde la conformación inteligente de formas de onda hasta la integración con sistemas MIMO masivo, OTFS y ISAC, desde los modelos fundacionales multimodales hasta el aprendizaje federado y el plano de control semántico, cada uno de estos temas contribuye a la visión de un sistema de comunicaciones que trasciende la transmisión de bits para convertirse en un verdadero intercambio de significado. La convergencia de estas líneas de investigación será fundamental para la realización de las redes 6G y la materialización de un mundo conectado inteligente donde la comunicación sea tan eficiente y natural como la comunicación humana.

---

### Referencias de la Sección 9

- Luo, X. et al. (2022). "Semantic Communications: Overview, Open Issues, and Future Research Directions." *IEEE Communications Surveys & Tutorials*, vol. 24, no. 4, pp. 2586–2630. DOI: [10.1109/COMST.2022.3195590](https://doi.org/10.1109/COMST.2022.3195590)

- Strinati, E. C. et al. (2021). "6G: The Next Frontier." *IEEE Network*, vol. 35, no. 1, pp. 22–28. DOI: [10.1109/MNET.011.2000568](https://doi.org/10.1109/MNET.011.2000568)

- Shi, G. et al. (2021). "From Semantic Communication to Semantic-Aware Networking: Model, Architecture, and Open Problems." *IEEE Journal on Selected Areas in Communications*, vol. 39, no. 8, pp. 2322–2340. DOI: [10.1109/JSAC.2021.3126078](https://doi.org/10.1109/JSAC.2021.3126078)
