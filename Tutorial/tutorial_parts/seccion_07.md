# 7. Fundamentos de las Comunicaciones Semánticas

Las comunicaciones inalámbricas han alcanzado niveles de madurez extraordinarios gracias a décadas de investigación fundamentada en la teoría de la información de Shannon. Sin embargo, a medida que nos acercamos a los límites teóricos de la capacidad del canal, surge una pregunta fundamental: ¿es posible comunicar de forma más eficiente si transmitimos *significado* en lugar de *bits*? Esta pregunta, planteada originalmente por Warren Weaver en 1949, ha permanecido latente durante más de siete décadas y hoy resurge con fuerza gracias a los avances en inteligencia artificial, particularmente en modelos basados en Transformers y aprendizaje profundo.

En esta sección exploramos los fundamentos de las comunicaciones semánticas, un paradigma que promete revolucionar el diseño de sistemas de comunicación al operar en el nivel del significado. Partiremos del modelo clásico de Shannon, identificaremos sus limitaciones inherentes, y construiremos paso a paso la arquitectura de un sistema de comunicación semántica moderno. Veremos cómo los Transformers, estudiados en secciones anteriores de este tutorial, se convierten en la pieza clave que habilita la extracción y reconstrucción de información semántica.

---

## 7.1 Del modelo de Shannon a la comunicación semántica

### 7.1.1 La teoría matemática de la comunicación de Shannon (1948)

En 1948, Claude E. Shannon publicó su trabajo seminal *"A Mathematical Theory of Communication"* (Shannon, 1948), estableciendo los cimientos de la teoría de la información moderna. En este trabajo, Shannon definió un marco matemático riguroso para cuantificar la información y establecer los límites fundamentales de la transmisión de datos a través de canales con ruido.

El modelo de Shannon se compone de cinco elementos esenciales:

1. **Fuente de información**: produce un mensaje o una secuencia de mensajes que se desean comunicar.
2. **Transmisor (codificador)**: transforma el mensaje en una señal adecuada para ser transmitida por el canal.
3. **Canal**: el medio físico por el cual se transmite la señal, sujeto a ruido e interferencias.
4. **Receptor (decodificador)**: reconstruye el mensaje a partir de la señal recibida.
5. **Destino**: la entidad a la cual va dirigido el mensaje.

Shannon introdujo el concepto de **entropía de la información** como medida de la incertidumbre asociada a una fuente de mensajes. Para una variable aleatoria discreta $X$ con alfabeto $\mathcal{X}$ y función de probabilidad $p(x)$, la entropía se define como:

$$H(X) = -\sum_{x \in \mathcal{X}} p(x) \log_2 p(x)$$

La entropía representa la cantidad mínima de bits necesarios, en promedio, para representar un símbolo de la fuente. Si la fuente produce símbolos equiprobables de un alfabeto de tamaño $M$, entonces $H(X) = \log_2 M$ bits por símbolo. Si algunos símbolos son más probables que otros, la entropía disminuye, reflejando la redundancia inherente en la fuente.

Uno de los resultados más profundos de Shannon es el **teorema de la capacidad del canal**, que establece que para un canal con ancho de banda $B$ (en Hz) y relación señal a ruido $\text{SNR}$ (lineal), la capacidad máxima de transmisión libre de errores es:

$$C = B \log_2(1 + \text{SNR})$$

Este resultado, conocido como la **fórmula de Shannon-Hartley**, tiene implicaciones extraordinarias. Nos dice que existe un límite superior absoluto a la tasa de información que se puede transmitir de forma fiable a través de un canal con ruido aditivo gaussiano blanco (AWGN). Si la tasa de transmisión $R$ satisface $R < C$, entonces existe un esquema de codificación que permite una probabilidad de error arbitrariamente pequeña. Si $R > C$, la comunicación fiable es imposible sin importar el esquema de codificación utilizado.

Para comprender la profundidad de este resultado, desglosemos sus componentes. El ancho de banda $B$ representa el rango de frecuencias disponible para la transmisión; un mayor ancho de banda permite transmitir más información por unidad de tiempo. La relación señal a ruido $\text{SNR} = P_s / P_n$, donde $P_s$ es la potencia de la señal y $P_n$ es la potencia del ruido, cuantifica la calidad del canal. El logaritmo en base 2 expresa la capacidad en bits por segundo. Observemos que la capacidad crece logarítmicamente con la $\text{SNR}$: duplicar la potencia de transmisión no duplica la capacidad, sino que la incrementa en solo $B$ bits/s. Esta dependencia logarítmica impone rendimientos decrecientes al aumentar la potencia.

Es fundamental observar que el marco de Shannon opera exclusivamente en el **nivel sintáctico** de la comunicación. La teoría se preocupa por la transmisión fiel de secuencias de símbolos, sin considerar en absoluto el significado que dichos símbolos puedan representar. Como el propio Shannon declaró explícitamente en su artículo:

> *"The fundamental problem of communication is that of reproducing at one point either exactly or approximately a message selected at another point. Frequently the messages have meaning... these semantic aspects of communication are irrelevant to the engineering problem."*

Esta deliberada exclusión del significado fue una decisión de diseño brillante que permitió construir una teoría matemática precisa y universal. Sin embargo, como veremos, esta exclusión también impone limitaciones fundamentales que las comunicaciones semánticas buscan superar.

### 7.1.2 Los tres niveles de comunicación de Weaver (1949)

Warren Weaver, en su influyente ensayo introductorio al trabajo de Shannon titulado *"Recent Contributions to the Mathematical Theory of Communication"* (Weaver, 1949), propuso una taxonomía de tres niveles para el problema de la comunicación:

**Nivel A — Problema técnico**: ¿Con qué precisión se pueden transmitir los símbolos de la comunicación? Este es el nivel en el que opera la teoría de Shannon. Se preocupa por la fidelidad bit a bit de la transmisión: ¿llegó cada bit correctamente al receptor? Las métricas relevantes son la tasa de error de bit (BER, *Bit Error Rate*), la tasa de error de bloque (BLER, *Block Error Rate*) y la capacidad del canal. Los sistemas de comunicación modernos —desde 2G hasta 5G— han sido diseñados y optimizados fundamentalmente en este nivel.

**Nivel B — Problema semántico**: ¿Con qué precisión los símbolos transmitidos transportan el significado deseado? Este nivel se pregunta si el receptor comprende lo que el transmisor quiso comunicar. Ya no importa si cada bit es correcto; lo que importa es si el *significado* se preserva. Por ejemplo, si se transmite la oración "El gato está sobre la mesa" y el receptor recibe "El felino se encuentra encima de la mesa", desde el punto de vista del Nivel A hay muchos errores (las palabras son diferentes), pero desde el Nivel B la comunicación ha sido perfecta (el significado es idéntico).

**Nivel C — Problema de efectividad**: ¿Con qué eficacia el significado recibido afecta la conducta del receptor de la manera deseada? Este nivel se preocupa por el impacto pragmático de la comunicación. En un sistema de conducción autónoma, por ejemplo, no basta con que el vehículo "comprenda" que hay un peatón adelante (Nivel B); debe tomar la acción correcta de frenar (Nivel C). Las comunicaciones orientadas a tareas (*task-oriented communications*) operan en este nivel.

La relación entre estos tres niveles es jerárquica pero no simplemente inclusiva. El éxito en el Nivel A no garantiza el éxito en el Nivel B (se pueden recibir todos los bits correctamente pero no comprender el mensaje si falta contexto). Análogamente, el éxito en el Nivel B no garantiza el éxito en el Nivel C (se puede comprender perfectamente un mensaje pero no actuar correctamente en consecuencia).

Las comunicaciones semánticas operan principalmente en el **Nivel B**, con extensiones naturales hacia el **Nivel C**. La idea central es diseñar sistemas que optimicen la preservación del significado, no la fidelidad de los bits, lo que permite una eficiencia radicalmente superior cuando los recursos del canal son limitados.

### 7.1.3 El "efecto precipicio" y las limitaciones del paradigma clásico

Los sistemas de comunicación clásicos exhiben un fenómeno conocido como el **efecto precipicio** (*cliff effect*): cuando la relación señal a ruido cae por debajo de un umbral crítico determinado por el esquema de modulación y codificación (MCS, *Modulation and Coding Scheme*), el rendimiento se desploma abruptamente. El sistema pasa de funcionar casi perfectamente a fallar completamente en un rango estrecho de SNR.

Este comportamiento se debe a la naturaleza discreta de las decisiones de decodificación en los sistemas clásicos. Cuando el canal es suficientemente bueno, el decodificador de canal puede corregir los errores y recuperar los bits originales con alta fiabilidad. Pero cuando el ruido supera la capacidad de corrección del código, los errores se propagan de forma catastrófica, el decodificador de fuente recibe bits incorrectos y la señal reconstruida se degrada dramáticamente.

Consideremos un sistema clásico de transmisión de imágenes. A una $\text{SNR}$ de 10 dB, el sistema podría producir una imagen perfecta. A 8 dB, quizás aparezcan algunos artefactos menores. Pero a 5 dB, la imagen podría ser completamente irreconocible — una cascada de píxeles erróneos sin estructura alguna. No hay degradación gradual: el sistema simplemente "se cae del precipicio".

Este fenómeno tiene consecuencias prácticas severas. En redes móviles, los usuarios que se encuentran en los bordes de las celdas o en condiciones de desvanecimiento profundo experimentan cortes abruptos del servicio. Los protocolos de adaptación de enlace (*link adaptation*) intentan mitigar este problema seleccionando MCS menos agresivos, pero esto reduce significativamente la eficiencia espectral.

### 7.1.4 El cambio de paradigma: transmitir significado, no bits

Las comunicaciones semánticas proponen un cambio de paradigma radical: en lugar de transmitir una representación fiel de los datos de la fuente (cada píxel, cada muestra de audio, cada carácter), se transmite una representación compacta del *significado* contenido en dichos datos.

Este cambio tiene implicaciones profundas. Primero, la cantidad de información a transmitir se reduce drásticamente, porque el significado es típicamente mucho más comprimible que los datos crudos. Una imagen de un gato sobre una mesa requiere millones de bits para su representación pixel a pixel, pero su significado semántico ("un gato anaranjado sentado sobre una mesa de madera en una cocina") puede representarse con unos pocos cientos de bits.

Segundo, la comunicación se vuelve **robusta al ruido de forma natural**. El ruido del canal corrompe bits individuales, pero la representación semántica, al ser una abstracción de alto nivel, es intrínsecamente más resiliente a perturbaciones en el nivel de bits. Un vector semántico ligeramente perturbado por ruido gaussiano sigue representando aproximadamente el mismo concepto.

Tercero, el sistema puede **degradarse graciosamente** en lugar de exhibir el efecto precipicio. A medida que la SNR disminuye, la calidad semántica de la reconstrucción se degrada de forma gradual y predecible, no abrupta. Bajo condiciones muy adversas, el receptor podría obtener una reconstrucción aproximada (quizás menos detallada o con vocabulario diferente), pero que preserva el significado esencial.

**Figura 7.1:** *Comparación entre un sistema de comunicación clásico y un sistema de comunicación semántica. (a) Sistema clásico: la fuente genera un mensaje que pasa por una cadena de bloques separados — codificación de fuente (compresión, e.g., JPEG, H.265), codificación de canal (protección contra errores, e.g., LDPC, Turbo codes), modulación (mapeo a símbolos, e.g., QAM), transmisión por el canal físico (sujeto a ruido e interferencia), demodulación, decodificación de canal, decodificación de fuente, y finalmente el destino recibe una reconstrucción del mensaje original. Cada bloque está optimizado de forma independiente. (b) Sistema semántico: la fuente genera un mensaje que es procesado por un codificador semántico (extrae el significado, típicamente una red neuronal) y un codificador de canal (adapta la representación semántica al canal), la señal atraviesa el canal físico, y en el receptor un decodificador de canal y un decodificador semántico (reconstruye un mensaje con el mismo significado, típicamente otra red neuronal) entregan el contenido al destino. Los bloques de codificación de fuente y canal se fusionan en la codificación semántica conjunta. La optimización es de extremo a extremo.*

---

## 7.2 ¿Qué es la "semántica" en comunicaciones?

### 7.2.1 Información semántica versus información sintáctica

Para comprender las comunicaciones semánticas es esencial distinguir con precisión entre **información sintáctica** e **información semántica**.

La **información sintáctica**, en el sentido de Shannon, se refiere a la secuencia de símbolos que compone un mensaje, sin consideración alguna por su significado. Dos mensajes con idéntica estructura estadística (misma distribución de probabilidad sobre los símbolos) tienen la misma entropía de Shannon, independientemente de si uno es una oración con sentido y el otro es una secuencia aleatoria de caracteres. La entropía de Shannon mide la *sorpresa* estadística, no el *contenido semántico*.

Formalmente, si un mensaje $\mathbf{s} = (s_1, s_2, \ldots, s_N)$ es una secuencia de $N$ símbolos de un alfabeto $\mathcal{S}$, la información sintáctica se cuantifica mediante:

$$I_{\text{sintáctica}}(\mathbf{s}) = -\log_2 p(\mathbf{s})$$

donde $p(\mathbf{s})$ es la probabilidad de ocurrencia del mensaje $\mathbf{s}$ según el modelo estadístico de la fuente. Esta medida no captura la relación entre el mensaje y su referente en el mundo real.

La **información semántica**, en contraste, se refiere al *significado* que el mensaje transporta — su contenido proposicional, las entidades que describe, las relaciones que establece, las acciones que implica. Dos mensajes con diferentes secuencias de símbolos pueden transportar la misma información semántica. Por ejemplo:

- "La temperatura en Madrid es de 35°C"
- "En la capital española, el termómetro marca treinta y cinco grados centígrados"

Estas dos oraciones tienen información sintáctica completamente diferente (diferentes palabras, diferente longitud, diferentes estadísticas de caracteres), pero transportan información semántica prácticamente idéntica.

La cuantificación rigurosa de la información semántica ha sido un desafío abierto durante décadas. Diversos enfoques han sido propuestos, desde la teoría de la información semántica de Bar-Hillel y Carnap (1952) basada en lógica proposicional, hasta los enfoques modernos basados en representaciones distribuidas (*embeddings*) aprendidos por redes neuronales.

En el paradigma moderno de comunicaciones semánticas, la información semántica de un mensaje $\mathbf{s}$ se representa como un **vector de características semánticas** $\mathbf{z} \in \mathbb{R}^d$, obtenido mediante un codificador semántico $f_\theta$:

$$\mathbf{z} = f_\theta(\mathbf{s})$$

donde $\theta$ denota los parámetros del codificador (típicamente una red neuronal profunda). Este vector $\mathbf{z}$ vive en un espacio semántico de dimensión $d$, donde la proximidad geométrica refleja la similitud de significado. Mensajes con significado similar producen vectores cercanos en este espacio; mensajes con significado diferente producen vectores distantes.

### 7.2.2 Ejemplo ilustrativo: transmisión de una imagen

Consideremos el problema de transmitir una fotografía de un perro jugando en un parque a través de un canal con capacidad limitada. Este ejemplo ilustra de manera contundente la diferencia entre los paradigmas clásico y semántico.

**Enfoque clásico (sintáctico):**

1. La imagen se representa como una matriz de píxeles, por ejemplo $1024 \times 768$ píxeles con 3 canales de color (RGB) y 8 bits por canal.
2. La cantidad total de datos es $1024 \times 768 \times 3 \times 8 = 18{,}874{,}368$ bits (≈ 18.9 Mbits) sin comprimir.
3. Se aplica codificación de fuente (e.g., JPEG) para comprimir, reduciendo quizás a 500 Kbits.
4. Se aplica codificación de canal (e.g., código LDPC) para proteger contra errores, añadiendo redundancia.
5. La señal resultante se modula y transmite.
6. En el receptor, se demodula, decodifica el canal, y decodifica la fuente.
7. El objetivo es reconstruir cada píxel con la mayor fidelidad posible.

Si las condiciones del canal son buenas, se obtiene una imagen idéntica o muy similar a la original. Si las condiciones son malas (baja SNR), la decodificación de canal falla y la imagen reconstruida presenta artefactos severos o es completamente irreconocible.

**Enfoque semántico:**

1. Un codificador semántico (e.g., una red neuronal convolucional profunda como ResNet o un Vision Transformer) procesa la imagen y extrae su contenido semántico.
2. La representación semántica podría codificarse como un vector compacto que capture: "perro de raza labrador, color dorado, corriendo, pelota roja en la boca, parque con césped verde, día soleado".
3. Esta representación compacta requiere quizás solo $d = 256$ o $d = 512$ valores de punto flotante, es decir, unos pocos miles de bits.
4. El codificador de canal adapta esta representación para transmisión eficiente.
5. En el receptor, el decodificador de canal recupera una versión posiblemente ruidosa de la representación semántica.
6. El decodificador semántico (e.g., un modelo generativo) reconstruye una imagen que es **semánticamente consistente** con la original, aunque puede diferir en detalles de bajo nivel (la posición exacta de cada hoja de césped, la textura precisa del pelaje).

La reducción en la cantidad de datos es dramática: de cientos de miles de bits a unos pocos miles. Además, la imagen reconstruida preserva su significado incluso bajo condiciones de canal adversas, exhibiendo una degradación gradual en lugar del efecto precipicio.

### 7.2.3 Comunicaciones orientadas a tareas

Un concepto estrechamente relacionado con las comunicaciones semánticas es el de **comunicaciones orientadas a tareas** (*task-oriented communications*), que operan en el Nivel C de Weaver. En este paradigma, el objetivo del sistema no es reconstruir el mensaje original ni siquiera preservar su significado completo, sino transmitir únicamente la información necesaria para que el receptor realice una tarea específica.

Consideremos un vehículo autónomo que captura imágenes con su cámara y necesita enviarlas a un servidor en la nube para su procesamiento. En un sistema clásico, se transmitiría la imagen completa. En un sistema semántico, se transmitiría una representación del significado de la imagen. En un sistema orientado a tareas, si la tarea es detectar peatones, se transmitiría únicamente la información relevante para esa tarea: presencia/ausencia de peatones, sus posiciones y velocidades estimadas.

Formalmente, si la tarea del receptor se modela como una función $g: \mathcal{Z} \rightarrow \mathcal{Y}$ que mapea la información recibida a una acción o decisión, entonces el objetivo del sistema orientado a tareas es maximizar:

$$\max_{\theta, \phi} \mathbb{E}\left[\mathcal{U}(g(f_\phi(\hat{\mathbf{z}})), y^*)\right]$$

donde $\hat{\mathbf{z}}$ es la representación semántica recibida (posiblemente corrompida por el canal), $f_\phi$ es el decodificador semántico con parámetros $\phi$, $y^*$ es la acción óptima, y $\mathcal{U}$ es una función de utilidad que mide la calidad de la decisión tomada.

### 7.2.4 Entropía semántica e información mutua semántica

La extensión de los conceptos de entropía e información mutua al dominio semántico es un área activa de investigación. La **entropía semántica** busca cuantificar la incertidumbre asociada al significado de un mensaje, en contraste con la entropía de Shannon que cuantifica la incertidumbre sobre la secuencia de símbolos.

Intuitivamente, la entropía semántica de una fuente mide la diversidad de significados que puede generar. Una fuente que produce mensajes con gran variedad de significados tiene alta entropía semántica. Una fuente repetitiva que dice siempre esencialmente lo mismo tiene baja entropía semántica, incluso si utiliza diferentes palabras cada vez (lo que le daría alta entropía de Shannon).

Si denotamos el contenido semántico de un mensaje $\mathbf{s}$ como $\mathbf{z} = f_\theta(\mathbf{s})$, la entropía semántica puede definirse sobre la distribución del vector semántico:

$$H_{\text{sem}}(Z) = -\int_{\mathcal{Z}} p(\mathbf{z}) \log_2 p(\mathbf{z}) \, d\mathbf{z}$$

donde la integral se extiende sobre el espacio semántico $\mathcal{Z} \subseteq \mathbb{R}^d$. En la práctica, dado que $\mathbf{z}$ es continuo, se trabaja con la entropía diferencial.

La **información mutua semántica** entre el mensaje transmitido y el recibido cuantifica cuánto significado se preserva a través del canal:

$$I_{\text{sem}}(Z; \hat{Z}) = H_{\text{sem}}(Z) - H_{\text{sem}}(Z | \hat{Z})$$

donde $Z$ es la representación semántica transmitida y $\hat{Z}$ es la representación semántica recibida. Esta cantidad mide la reducción en la incertidumbre semántica del mensaje transmitido dada la observación en el receptor. Un sistema de comunicación semántica ideal maximizaría esta información mutua semántica.

---

## 7.3 Arquitectura general de un sistema de comunicación semántica

### 7.3.1 Codificación conjunta de fuente y canal (JSCC)

Los sistemas de comunicación clásicos se basan en el **teorema de separación** de Shannon, que establece que la codificación de fuente y la codificación de canal pueden diseñarse de forma independiente sin pérdida de optimalidad, siempre que se permitan longitudes de bloque arbitrariamente grandes y se disponga de tiempo ilimitado para la codificación y decodificación. Formalmente, si la entropía de la fuente $H(S)$ es menor que la capacidad del canal $C$, entonces la comunicación fiable es posible, y la codificación de fuente óptima seguida de la codificación de canal óptima alcanza este límite.

Sin embargo, el teorema de separación requiere condiciones ideales que rara vez se satisfacen en la práctica:

- **Longitud de bloque infinita**: el rendimiento óptimo se alcanza asintóticamente; en la práctica, los bloques tienen longitud finita, lo que introduce pérdida de rendimiento.
- **Modelo estadístico perfecto de la fuente**: se asume que la distribución de la fuente es conocida exactamente, lo cual es difícil para fuentes complejas como imágenes naturales, voz o texto.
- **Canal estacionario y ergódico**: se asume que las estadísticas del canal no cambian, lo cual es una aproximación en canales móviles con desvanecimiento variable.
- **Sin restricciones de complejidad ni latencia**: el diseño separado introduce latencia adicional y puede requerir complejidad computacional prohibitiva.

La **codificación conjunta de fuente y canal** (*Joint Source-Channel Coding*, JSCC) abandona el principio de separación y diseña un esquema unificado que simultáneamente comprime la fuente y protege contra errores del canal. La JSCC puede superar al diseño separado en régimen de longitud de bloque finita, cuando el modelo de la fuente es imperfecto, o cuando las condiciones del canal varían rápidamente.

En el contexto de las comunicaciones semánticas, la JSCC toma una forma particularmente natural. El codificador semántico realiza implícitamente tanto la compresión de fuente (al extraer solo el significado relevante) como la codificación de canal (al generar una representación que sea robusta al ruido). Ambas funciones se optimizan conjuntamente a través del aprendizaje de extremo a extremo.

Matemáticamente, un sistema JSCC aprendido puede modelarse como:

$$\hat{\mathbf{s}} = g_\phi(h(\text{enc}_\theta(\mathbf{s})) + \mathbf{n})$$

donde $\mathbf{s}$ es el mensaje fuente, $\text{enc}_\theta: \mathcal{S} \rightarrow \mathbb{R}^k$ es el codificador con parámetros $\theta$ que mapea el mensaje a $k$ símbolos de canal, $h(\cdot)$ representa los efectos del canal (atenuación, rotación de fase, etc.), $\mathbf{n}$ es el ruido aditivo, y $g_\phi: \mathbb{R}^k \rightarrow \hat{\mathcal{S}}$ es el decodificador con parámetros $\phi$ que reconstruye el mensaje. Los parámetros $\theta$ y $\phi$ se optimizan conjuntamente para minimizar una función de pérdida que mide la distorsión semántica.

### 7.3.2 Aprendizaje de extremo a extremo (E2E)

El enfoque de **aprendizaje de extremo a extremo** (*End-to-End Learning*, E2E) es la metodología dominante para el diseño de sistemas de comunicación semántica. En lugar de diseñar cada bloque del sistema de forma independiente y luego integrarlos, el enfoque E2E entrena todo el sistema como una única red neuronal, optimizando directamente la métrica de rendimiento final deseada.

El principio fundamental es modelar todo el sistema de comunicación — codificador, canal y decodificador — como un grafo computacional diferenciable, lo que permite utilizar el algoritmo de retropropagación (*backpropagation*) para optimizar los parámetros de extremo a extremo.

El desafío principal es que el canal físico es una componente estocástica no parametrizada que no tiene gradientes analíticos. Para resolver esto, se utiliza una de varias estrategias:

1. **Modelo diferenciable del canal**: se reemplaza el canal físico por un modelo matemático diferenciable. Para un canal AWGN, esto es simplemente añadir ruido gaussiano: $\mathbf{y} = \mathbf{x} + \mathbf{n}$, donde $\mathbf{n} \sim \mathcal{N}(\mathbf{0}, \sigma^2 \mathbf{I})$. Este modelo es trivialmente diferenciable (los gradientes fluyen a través de la suma sin modificación). Para un canal de desvanecimiento Rayleigh, el modelo es $\mathbf{y} = \mathbf{h} \odot \mathbf{x} + \mathbf{n}$, donde $\mathbf{h} \sim \mathcal{CN}(\mathbf{0}, \mathbf{I})$ son los coeficientes de desvanecimiento, y $\odot$ denota el producto elemento a elemento.

2. **Truco de reparametrización**: similar al utilizado en autoencoders variacionales (VAEs), se reparametriza la componente estocástica del canal para permitir el flujo de gradientes.

3. **Estimación de gradientes por políticas**: se utilizan técnicas de aprendizaje por refuerzo (e.g., REINFORCE) para estimar los gradientes a través de componentes no diferenciables.

La función de pérdida del sistema E2E típicamente toma la forma:

$$\mathcal{L}(\theta, \phi) = \mathbb{E}_{\mathbf{s} \sim p(\mathbf{s}),\, \mathbf{n} \sim \mathcal{N}}\left[d(\mathbf{s}, \hat{\mathbf{s}})\right]$$

donde $d(\cdot, \cdot)$ es una medida de distorsión semántica entre el mensaje original $\mathbf{s}$ y el reconstruido $\hat{\mathbf{s}} = g_\phi(h(\text{enc}_\theta(\mathbf{s})) + \mathbf{n})$. La elección de $d$ depende del tipo de datos y la tarea:

- Para texto: entropía cruzada a nivel de palabra, similitud semántica en espacio de embeddings.
- Para imágenes: error cuadrático medio ponderado perceptualmente, distancia en espacio de características de una red pre-entrenada.
- Para tareas: función de pérdida específica de la tarea (e.g., exactitud de clasificación, error de detección).

### 7.3.3 Componentes del sistema

Un sistema de comunicación semántica completo consta de los siguientes componentes principales:

**Transmisor:**

El transmisor se compone de dos sub-bloques conceptuales que, en la práctica, pueden implementarse como una única red neuronal entrenada de extremo a extremo:

- **Codificador semántico** ($\text{SemEnc}_\theta$): este módulo procesa el mensaje de la fuente $\mathbf{s}$ y extrae su representación semántica $\mathbf{z} \in \mathbb{R}^d$. Típicamente se implementa como una red neuronal profunda: un Transformer para texto, una red convolucional (CNN) o un Vision Transformer (ViT) para imágenes, o una red recurrente para secuencias temporales. La dimensión $d$ del espacio semántico es un hiperparámetro que controla la compresión: un $d$ menor implica mayor compresión pero potencialmente mayor pérdida semántica.

$$\mathbf{z} = \text{SemEnc}_\theta(\mathbf{s}) \in \mathbb{R}^d$$

- **Codificador de canal** ($\text{ChEnc}_\alpha$): este módulo transforma la representación semántica $\mathbf{z}$ en símbolos de canal $\mathbf{x} \in \mathbb{C}^k$ (o $\mathbb{R}^{2k}$) adecuados para la transmisión por el medio físico. Debe satisfacer una restricción de potencia promedio: $\mathbb{E}[||\mathbf{x}||^2] \leq k \cdot P$, donde $P$ es la potencia por uso de canal. El ratio $\rho = d / k$ se denomina **tasa de compresión de canal** y determina cuántos símbolos de canal se utilizan para transmitir cada componente de la representación semántica.

$$\mathbf{x} = \text{ChEnc}_\alpha(\mathbf{z}) \in \mathbb{C}^k$$

**Canal:**

El canal físico introduce distorsiones en la señal transmitida. Los modelos de canal más utilizados son:

- **Canal AWGN** (*Additive White Gaussian Noise*):

$$\mathbf{y} = \mathbf{x} + \mathbf{n}, \quad \mathbf{n} \sim \mathcal{CN}(\mathbf{0}, \sigma_n^2 \mathbf{I})$$

donde $\sigma_n^2$ es la potencia del ruido, y la SNR se define como $\text{SNR} = P / \sigma_n^2$.

- **Canal de desvanecimiento Rayleigh** (*Rayleigh Fading Channel*):

$$\mathbf{y} = \mathbf{h} \odot \mathbf{x} + \mathbf{n}, \quad h_i \sim \mathcal{CN}(0, 1)$$

donde $\mathbf{h}$ es el vector de coeficientes de desvanecimiento. Este modelo representa escenarios donde no hay línea de vista directa entre el transmisor y el receptor, como en entornos urbanos con múltiples reflexiones. Los coeficientes $h_i$ siguen una distribución Rayleigh en magnitud, y la fase es uniformemente distribuida en $[0, 2\pi)$.

- **Canal de desvanecimiento Rician** (*Rician Fading Channel*):

$$\mathbf{y} = \left(\sqrt{\frac{K}{K+1}} \mathbf{h}_{\text{LoS}} + \sqrt{\frac{1}{K+1}} \mathbf{h}_{\text{NLoS}}\right) \odot \mathbf{x} + \mathbf{n}$$

donde $K$ es el factor de Rician que representa la relación entre la componente de línea de vista directa $\mathbf{h}_{\text{LoS}}$ y las componentes de dispersión $\mathbf{h}_{\text{NLoS}}$.

**Receptor:**

El receptor es simétrico al transmisor y también consta de dos sub-bloques:

- **Decodificador de canal** ($\text{ChDec}_\beta$): procesa la señal recibida $\mathbf{y}$ y produce una estimación de la representación semántica $\hat{\mathbf{z}}$. En un sistema entrenado de extremo a extremo, este módulo aprende implícitamente a realizar ecualización, estimación de canal y decodificación de forma conjunta.

$$\hat{\mathbf{z}} = \text{ChDec}_\beta(\mathbf{y}) \in \mathbb{R}^d$$

- **Decodificador semántico** ($\text{SemDec}_\gamma$): transforma la representación semántica estimada $\hat{\mathbf{z}}$ en una reconstrucción del mensaje original $\hat{\mathbf{s}}$. Para texto, esto implica generar una secuencia de palabras; para imágenes, reconstruir una matriz de píxeles.

$$\hat{\mathbf{s}} = \text{SemDec}_\gamma(\hat{\mathbf{z}})$$

El sistema completo puede expresarse como la composición:

$$\hat{\mathbf{s}} = \text{SemDec}_\gamma\left(\text{ChDec}_\beta\left(h\left(\text{ChEnc}_\alpha\left(\text{SemEnc}_\theta(\mathbf{s})\right)\right) + \mathbf{n}\right)\right)$$

y todos los parámetros $\{\theta, \alpha, \beta, \gamma\}$ se optimizan conjuntamente minimizando la pérdida semántica $\mathcal{L}$.

**Figura 7.2:** *Arquitectura detallada de un sistema de comunicación semántica de extremo a extremo (E2E). El diagrama muestra el flujo completo de información. En el transmisor: el mensaje fuente $\mathbf{s}$ (texto, imagen o señal) ingresa al Codificador Semántico (red neuronal profunda, e.g., Transformer), que produce la representación semántica $\mathbf{z} \in \mathbb{R}^d$; esta pasa al Codificador de Canal (capas densas con normalización de potencia), que genera los símbolos de canal $\mathbf{x} \in \mathbb{C}^k$. Los símbolos atraviesan el Canal Físico (modelado como capa diferenciable: AWGN, Rayleigh, o Rician), produciendo la señal recibida $\mathbf{y}$. En el receptor: $\mathbf{y}$ ingresa al Decodificador de Canal (capas densas), que estima $\hat{\mathbf{z}}$; esta pasa al Decodificador Semántico (red neuronal profunda, e.g., Transformer), que produce el mensaje reconstruido $\hat{\mathbf{s}}$. Una flecha de retropropagación recorre todo el sistema de extremo a extremo, indicando que los gradientes fluyen desde la función de pérdida $\mathcal{L}(\mathbf{s}, \hat{\mathbf{s}})$ a través de todos los bloques para la optimización conjunta.*

---

## 7.4 El papel de los Transformers en las comunicaciones semánticas

### 7.4.1 ¿Por qué los Transformers son ideales para la extracción semántica?

Los Transformers, introducidos por Vaswani et al. (2017) en el artículo *"Attention Is All You Need"*, se han convertido en la arquitectura dominante para el procesamiento de lenguaje natural y, progresivamente, para visión por computador y procesamiento de señales. Su adopción en comunicaciones semánticas no es casual; las propiedades fundamentales de la arquitectura Transformer la hacen excepcionalmente adecuada para la extracción y reconstrucción de significado:

**1. El mecanismo de auto-atención captura significado contextual.**

La operación de auto-atención (*self-attention*) permite que cada elemento de una secuencia de entrada interactúe con todos los demás, ponderando su importancia relativa de forma aprendida. Recordemos que la auto-atención se calcula como:

$$\text{Attention}(\mathbf{Q}, \mathbf{K}, \mathbf{V}) = \text{softmax}\left(\frac{\mathbf{Q}\mathbf{K}^\top}{\sqrt{d_k}}\right)\mathbf{V}$$

donde $\mathbf{Q}$, $\mathbf{K}$ y $\mathbf{V}$ son las matrices de consultas (*queries*), claves (*keys*) y valores (*values*), respectivamente, obtenidas como proyecciones lineales de la entrada, y $d_k$ es la dimensión de las claves, utilizado como factor de escalado para estabilizar los gradientes.

Esta operación es crucial para las comunicaciones semánticas porque permite capturar dependencias de largo alcance y relaciones contextuales en el mensaje. En una oración como "El banco donde me senté estaba junto al banco del río", el mecanismo de atención puede desambiguar el doble significado de "banco" atendiendo al contexto ("senté" y "río"), una capacidad esencial para la extracción semántica precisa.

Los pesos de atención $\mathbf{A} = \text{softmax}\left(\frac{\mathbf{Q}\mathbf{K}^\top}{\sqrt{d_k}}\right)$ forman una matriz $N \times N$ (donde $N$ es la longitud de la secuencia) que codifica las relaciones de importancia entre cada par de elementos. El elemento $A_{ij}$ indica cuánta atención presta el elemento $i$ al elemento $j$. Estos pesos de atención son, en cierto sentido, una representación explícita de la estructura semántica del mensaje: revelan qué partes del mensaje son relevantes para entender cada otra parte.

**2. Capacidad multimodal.**

Los Transformers pueden procesar diferentes modalidades de datos — texto, imágenes, audio, señales — con la misma arquitectura base. Para texto, la entrada son embeddings de tokens (palabras o subpalabras). Para imágenes, se utilizan *patches* (regiones cuadradas de la imagen) como tokens (Vision Transformer, ViT). Para señales, se pueden utilizar ventanas temporales o representaciones en el dominio de la frecuencia. Esta versatilidad permite diseñar sistemas de comunicación semántica unificados para múltiples tipos de datos.

**3. Modelos pre-entrenados como base de conocimiento.**

Los modelos de lenguaje pre-entrenados a gran escala (e.g., BERT, GPT) han internalizado vastas cantidades de conocimiento sobre la estructura del lenguaje y las relaciones semánticas entre conceptos. Este conocimiento pre-entrenado puede aprovecharse en comunicaciones semánticas: un codificador semántico basado en un Transformer pre-entrenado ya posee una comprensión profunda del lenguaje, lo que reduce la cantidad de datos de entrenamiento necesarios y mejora la calidad de la extracción semántica.

Formalmente, el espacio de representaciones de un Transformer pre-entrenado define un espacio semántico $\mathcal{Z}$ con propiedades deseables: vectores cercanos corresponden a conceptos semánticamente similares, las direcciones en el espacio capturan relaciones semánticas (e.g., la dirección "rey" - "hombre" + "mujer" ≈ "reina"), y la estructura del espacio es suave (pequeñas perturbaciones producen pequeños cambios en el significado).

### 7.4.2 DeepSC: Comunicación semántica basada en Transformers para texto

El sistema **DeepSC** (*Deep Learning Enabled Semantic Communication*), propuesto por Xie et al. (2021) en el artículo *"Deep Learning Enabled Semantic Communication Systems"* (DOI: 10.1109/TSP.2021.3071082), es uno de los trabajos pioneros y más influyentes en comunicaciones semánticas basadas en Transformers. DeepSC demostró que un sistema de comunicación semántica entrenado de extremo a extremo puede superar significativamente a los sistemas clásicos, especialmente en condiciones de baja SNR.

La arquitectura de DeepSC consta de los siguientes componentes:

**Codificador semántico (Transmisor):**

El codificador semántico de DeepSC utiliza la arquitectura del codificador Transformer para extraer las características semánticas del texto de entrada. El proceso comienza con la tokenización de la oración de entrada en una secuencia de tokens $\mathbf{s} = (w_1, w_2, \ldots, w_L)$, donde $L$ es la longitud de la oración.

Cada token se convierte en un vector de embedding denso $\mathbf{e}_i \in \mathbb{R}^{d_{\text{model}}}$ mediante una capa de embedding entrenada. A estos embeddings se les suma una codificación posicional $\mathbf{PE}_i$ para incorporar información sobre la posición de cada token en la secuencia:

$$\mathbf{h}_i^{(0)} = \mathbf{e}_i + \mathbf{PE}_i$$

Los vectores $\{\mathbf{h}_i^{(0)}\}_{i=1}^L$ pasan por $N_e$ capas de codificador Transformer. Cada capa aplica auto-atención multi-cabeza (*multi-head attention*) seguida de una red *feed-forward*, con conexiones residuales y normalización de capa:

$$\mathbf{h}^{(\ell)} = \text{TransformerEncoderLayer}(\mathbf{h}^{(\ell-1)}), \quad \ell = 1, \ldots, N_e$$

La salida del último nivel del codificador Transformer $\mathbf{h}^{(N_e)} \in \mathbb{R}^{L \times d_{\text{model}}}$ constituye las características semánticas crudas. Estas se procesan mediante capas densas adicionales para producir la representación semántica final $\mathbf{z} \in \mathbb{R}^{L \times d_z}$, donde $d_z$ es la dimensión de la representación semántica por token.

$$\mathbf{z} = \text{Dense}_\theta(\mathbf{h}^{(N_e)})$$

**Codificador de canal:**

El codificador de canal transforma la representación semántica en símbolos aptos para la transmisión física. En DeepSC, esto se implementa mediante capas densas que mapean $\mathbf{z}$ a los símbolos de canal $\mathbf{x} \in \mathbb{R}^{L \times d_c}$, donde $d_c$ determina el número de símbolos de canal por token. La tasa de transmisión semántica se define como $R_s = d_c / d_{\text{model}}$, que indica cuántos símbolos de canal se utilizan por cada dimensión del modelo.

Se aplica una normalización de potencia para satisfacer la restricción de potencia del canal:

$$\mathbf{x} = \sqrt{k \cdot P} \cdot \frac{\tilde{\mathbf{x}}}{||\tilde{\mathbf{x}}||}$$

donde $\tilde{\mathbf{x}}$ es la salida de las capas densas antes de la normalización.

**Canal físico:**

DeepSC modela el canal como una capa estocástica diferenciable. Para un canal AWGN:

$$\mathbf{y} = \mathbf{x} + \mathbf{n}, \quad n_i \sim \mathcal{N}(0, \sigma_n^2)$$

Para un canal Rayleigh:

$$\mathbf{y} = \mathbf{h} \odot \mathbf{x} + \mathbf{n}, \quad h_i \sim \mathcal{CN}(0, 1)$$

Como estas operaciones son diferenciables (la adición de ruido y la multiplicación por coeficientes de canal), los gradientes pueden fluir directamente a través del modelo del canal durante la retropropagación.

**Decodificador de canal:**

El decodificador de canal es simétrico al codificador de canal: capas densas que transforman la señal recibida $\mathbf{y}$ en una estimación de la representación semántica $\hat{\mathbf{z}}$.

$$\hat{\mathbf{z}} = \text{Dense}_\beta(\mathbf{y})$$

**Decodificador semántico (Receptor):**

El decodificador semántico utiliza la arquitectura del decodificador Transformer para reconstruir el texto a partir de la representación semántica estimada. Emplea auto-atención enmascarada (*masked self-attention*) para la generación autorregresiva y atención cruzada (*cross-attention*) para atender a la representación semántica recibida.

$$\hat{\mathbf{s}} = \text{TransformerDecoder}_\gamma(\hat{\mathbf{z}})$$

La salida del decodificador es una distribución de probabilidad sobre el vocabulario para cada posición, de la cual se generan los tokens reconstruidos:

$$p(\hat{w}_t | \hat{w}_{<t}, \hat{\mathbf{z}}) = \text{softmax}(\mathbf{W}_o \cdot \text{TransDec}(\hat{w}_{<t}, \hat{\mathbf{z}}))$$

donde $\mathbf{W}_o$ es la matriz de proyección de salida.

**Entrenamiento:**

El sistema se entrena de extremo a extremo minimizando la entropía cruzada entre las palabras originales y las reconstruidas:

$$\mathcal{L}_{\text{CE}} = -\frac{1}{L}\sum_{t=1}^{L} \log p(\hat{w}_t = w_t | \hat{w}_{<t}, \hat{\mathbf{z}})$$

Además, DeepSC incorpora una pérdida basada en información mutua para garantizar que la representación semántica transmitida capture la mayor cantidad posible de información relevante sobre el mensaje original. Esta pérdida adicional se puede formular como una cota inferior variacional de la información mutua $I(\mathbf{s}; \hat{\mathbf{z}})$, estimada mediante una red discriminadora auxiliar:

$$\mathcal{L}_{\text{MI}} = -\hat{I}(\mathbf{s}; \hat{\mathbf{z}})$$

La pérdida total es:

$$\mathcal{L} = \mathcal{L}_{\text{CE}} + \lambda \cdot \mathcal{L}_{\text{MI}}$$

donde $\lambda$ es un hiperparámetro que controla la importancia relativa de cada componente.

### 7.4.3 Los pesos de atención como codificación de importancia semántica

Una perspectiva particularmente reveladora es interpretar los pesos de atención del Transformer como una medida de la **importancia semántica** de cada parte del mensaje. En el contexto de comunicaciones semánticas, esta interpretación tiene implicaciones prácticas directas.

Consideremos una oración como: "El presidente anunció una nueva política económica en la conferencia de prensa." Los pesos de atención del codificador semántico asignarán diferentes niveles de importancia a cada palabra:

- "presidente", "anunció", "política", "económica" → alta atención (palabras con alto contenido semántico)
- "El", "una", "en", "la", "de" → baja atención (palabras funcionales con bajo contenido semántico)

Esta distribución de atención se refleja directamente en la representación semántica $\mathbf{z}$: las dimensiones del vector asociadas a conceptos semánticamente importantes tendrán magnitudes mayores, mientras que las asociadas a información redundante o poco relevante tendrán magnitudes menores. En condiciones de ruido, las componentes de mayor magnitud son más robustas a la corrupción, lo que significa que el sistema naturalmente protege más la información semántica importante.

Formalmente, si $\mathbf{A}^{(\ell)} \in \mathbb{R}^{L \times L}$ es la matriz de atención de la capa $\ell$, podemos definir un **vector de importancia semántica** como:

$$\mathbf{v}_{\text{imp}} = \frac{1}{N_e} \sum_{\ell=1}^{N_e} \text{diag}\left(\mathbf{A}^{(\ell)\top} \mathbf{1}\right)$$

donde $\mathbf{1}$ es un vector de unos. El elemento $v_{\text{imp},i}$ indica la importancia semántica promedio del token $i$ según los patrones de atención aprendidos. Tokens con alto $v_{\text{imp},i}$ son semánticamente más relevantes.

### 7.4.4 El "vector de atención" como representación semántica

En el paradigma de comunicaciones semánticas con Transformers, la representación semántica $\mathbf{z}$ puede conceptualizarse como un "vector de atención" — no en el sentido literal de los pesos de atención, sino en el sentido de que es un vector que ha sido moldeado por múltiples capas de operaciones de atención para capturar una representación rica, contextualizada y comprimida del significado del mensaje.

Este vector tiene propiedades notables:

1. **Composicionalidad**: el significado de una oración compleja se construye composicionalmente a partir de los significados de sus partes, reflejado en cómo cada capa de atención combina las representaciones de diferentes tokens.

2. **Invarianza a la paráfrasis**: oraciones con el mismo significado pero diferente formulación producen vectores semánticos cercanos en el espacio $\mathcal{Z}$, porque el Transformer ha aprendido a abstraer más allá de la forma superficial.

3. **Sensibilidad al contexto**: la misma palabra produce diferentes representaciones según su contexto, permitiendo la desambiguación automática.

4. **Compresibilidad**: la dimensión $d$ del vector semántico puede ser significativamente menor que la dimensión del mensaje original (medido en bits), logrando una compresión semántica efectiva.

**Figura 7.3:** *Arquitectura del sistema de comunicación semántica DeepSC basado en Transformers (Xie et al., 2021). El diagrama muestra el flujo de procesamiento para la transmisión semántica de texto. En el transmisor: la oración de entrada "El avión aterrizó en el aeropuerto" se tokeniza y convierte en embeddings; estos pasan por un Codificador Transformer de $N_e$ capas (cada una con auto-atención multi-cabeza, normalización de capa y red feed-forward) que produce las características semánticas $\mathbf{z}$; las características se procesan mediante un Codificador de Canal (capas densas con normalización de potencia) que genera los símbolos de canal $\mathbf{x}$. Los símbolos atraviesan el Canal (AWGN o Rayleigh, modelado como capa diferenciable). En el receptor: la señal recibida $\mathbf{y}$ pasa por el Decodificador de Canal (capas densas) que estima $\hat{\mathbf{z}}$; estas características alimentan un Decodificador Transformer de $N_d$ capas (con auto-atención enmascarada, atención cruzada con $\hat{\mathbf{z}}$, y red feed-forward) que genera autorregressivamente la oración reconstruida "El avión llegó al aeropuerto". Se muestra el flujo de gradientes de retropropagación a través de todo el sistema, incluyendo la capa de canal diferenciable.*

---

## 7.5 Ventajas de las comunicaciones semánticas

### 7.5.1 Eficiencia en el uso del ancho de banda

La ventaja más inmediata y quizás más impactante de las comunicaciones semánticas es la **reducción drástica en la cantidad de datos que es necesario transmitir**. Al transmitir el significado en lugar de la representación literal de los datos, se logra una compresión que va mucho más allá de lo que los algoritmos de compresión de datos clásicos pueden alcanzar.

Para cuantificar esta ventaja, definimos la **tasa de compresión semántica** como:

$$\eta_{\text{sem}} = \frac{|\mathbf{s}|_{\text{bits}}}{|\mathbf{x}|_{\text{símbolos}} \times \log_2 M}$$

donde $|\mathbf{s}|_{\text{bits}}$ es el tamaño del mensaje original en bits, $|\mathbf{x}|_{\text{símbolos}}$ es el número de símbolos de canal utilizados, y $M$ es el orden de la modulación. Una tasa de compresión alta indica que se están transmitiendo pocos símbolos en relación al tamaño del mensaje original.

Consideremos un ejemplo concreto. Una oración típica en español contiene alrededor de 15 palabras, cada una representada por un índice en un vocabulario de 50,000 palabras, lo que requiere $15 \times \lceil\log_2 50{,}000\rceil \approx 15 \times 16 = 240$ bits. En un sistema de comunicación semántica como DeepSC, la representación semántica podría consistir en $L \times d_c$ símbolos de canal reales, donde $d_c$ puede ser tan pequeño como 4 o 8. Si $L = 15$ y $d_c = 4$, se transmiten solo 60 valores reales. En comparación, un sistema clásico que transmite el texto codificado carácter por carácter (con codificación de canal y modulación) requeriría significativamente más símbolos de canal.

La eficiencia se amplifica para datos de alta dimensionalidad como imágenes o video. Una imagen de alta resolución requiere millones de bits para su representación literal, pero su "significado" puede capturarse en un vector semántico de unas pocas centenas de dimensiones.

### 7.5.2 Degradación gradual versus efecto precipicio

Como se mencionó en la Sección 7.1.3, los sistemas clásicos sufren el efecto precipicio: un colapso abrupto del rendimiento cuando la SNR cae por debajo de un umbral. Los sistemas de comunicación semántica, en contraste, exhiben una **degradación gradual** (*graceful degradation*).

Este comportamiento se debe a la naturaleza de la representación semántica. En un sistema clásico, el decodificador de canal intenta recuperar bits exactos. Si la tasa de errores supera la capacidad de corrección del código, la decodificación falla catastróficamente. En un sistema semántico, el decodificador de canal produce una estimación de la representación semántica que es continuamente perturbada por el ruido. El decodificador semántico (red neuronal) es tolerante a estas perturbaciones porque ha sido entrenado para reconstruir significado a partir de representaciones ruidosas.

Matemáticamente, si $\hat{\mathbf{z}} = \mathbf{z} + \boldsymbol{\epsilon}$ donde $\boldsymbol{\epsilon}$ es el ruido efectivo en el espacio semántico, la calidad de la reconstrucción depende continuamente de $||\boldsymbol{\epsilon}||$. Para ruido pequeño, la reconstrucción es casi perfecta. A medida que $||\boldsymbol{\epsilon}||$ crece, la calidad se degrada suavemente. No hay un umbral abrupto.

Los resultados experimentales de DeepSC (Xie et al., 2021) demuestran que a una SNR de 0 dB (donde los sistemas clásicos basados en codificación Huffman + Turbo codes + modulación BPSK prácticamente no funcionan), el sistema semántico aún logra una similitud semántica (medida por BLEU score) significativamente superior a cero. A -2 dB, el sistema clásico es completamente inoperante, mientras que el sistema semántico todavía puede transmitir el significado esencial del mensaje, aunque con menor fidelidad léxica.

### 7.5.3 Robustez al ruido del canal

La robustez de los sistemas semánticos se debe a una propiedad fundamental de las representaciones distribuidas (*distributed representations*) aprendidas por redes neuronales: **la información semántica está codificada de forma distribuida a lo largo de todo el vector**, no concentrada en bits individuales.

En un sistema clásico, cada bit transporta información específica. Si un bit de la imagen comprimida en JPEG está en error, un bloque de 8×8 píxeles puede corromperse completamente. En un sistema semántico, la información está distribuida: cada componente del vector semántico contribuye de forma parcial al significado total. Corromper una componente degrada ligeramente el significado global, pero no lo destruye.

Esta propiedad se puede formalizar utilizando la noción de **lipschitzianidad** del decodificador semántico. Si el decodificador $g_\phi$ es Lipschitz-continuo con constante $L_g$, entonces:

$$||g_\phi(\hat{\mathbf{z}}) - g_\phi(\mathbf{z})|| \leq L_g \cdot ||\hat{\mathbf{z}} - \mathbf{z}||$$

Esto garantiza que pequeñas perturbaciones en la representación semántica producen pequeños cambios en la salida. Las redes neuronales modernas con normalización de capa, funciones de activación suaves y regularización tienden a tener constantes de Lipschitz moderadas, lo que les confiere esta propiedad de robustez.

### 7.5.4 Orientación a la tarea

Los sistemas de comunicación semántica pueden optimizarse directamente para la tarea que el receptor necesita realizar, en lugar de optimizarse para la reconstrucción fiel de los datos. Esta optimización orientada a la tarea permite ganancias de eficiencia adicionales significativas.

Por ejemplo, en un sistema de monitorización remota donde un sensor de imagen transmite datos a un servidor que debe detectar incendios forestales, el sistema semántico puede ser entrenado con una función de pérdida que mide directamente la exactitud de detección de incendios:

$$\mathcal{L}_{\text{tarea}} = -\mathbb{E}\left[y^* \log \hat{y} + (1 - y^*) \log(1 - \hat{y})\right]$$

donde $y^* \in \{0, 1\}$ es la etiqueta real (incendio/no incendio) y $\hat{y}$ es la predicción del receptor basada en la representación semántica recibida. Este enfoque transmite solo la información relevante para la detección de incendios, ignorando detalles irrelevantes (la textura exacta de las nubes, la forma precisa de cada árbol), lo que reduce drásticamente la cantidad de datos a transmitir.

### 7.5.5 Compatibilidad con la visión de 6G

Las comunicaciones semánticas se alinean naturalmente con la visión de las redes de sexta generación (6G), que se espera que soporten:

- **Comunicaciones ultra-masivas**: miles de millones de dispositivos IoT generando enormes volúmenes de datos. Transmitir solo el significado reduce la carga en la red.
- **Comunicaciones de latencia ultra-baja**: la compresión semántica reduce la cantidad de datos a transmitir, disminuyendo la latencia.
- **Inteligencia ubicua**: los dispositivos incorporan capacidades de IA que permiten la extracción y reconstrucción semántica local.
- **Eficiencia energética extrema**: transmitir menos datos implica menor consumo energético.
- **Conectividad en escenarios extremos**: la robustez a baja SNR permite la comunicación en condiciones donde los sistemas clásicos fallan.

La integración de comunicaciones semánticas con otras tecnologías 6G como superficies inteligentes reconfigurables (RIS), redes de funciones de red virtualizadas (NFV), y computación en el borde (*edge computing*) promete crear un ecosistema de comunicaciones radicalmente más eficiente.

---

## 7.6 Métricas de evaluación semántica

### 7.6.1 Métricas tradicionales (sintácticas)

Las métricas de evaluación clásicas en sistemas de comunicación operan en el nivel sintáctico, midiendo la fidelidad de la transmisión a nivel de bits o símbolos:

**Tasa de error de bit (BER, *Bit Error Rate*):**

$$\text{BER} = \frac{\text{Número de bits erróneos}}{\text{Número total de bits transmitidos}}$$

El BER es la métrica más fundamental en comunicaciones digitales. Un BER de $10^{-3}$ significa que, en promedio, 1 de cada 1,000 bits se recibe incorrectamente. Los estándares de comunicación modernos (e.g., 5G NR) especifican requisitos de BER típicamente del orden de $10^{-5}$ a $10^{-6}$ para servicios de datos.

**Tasa de error de bloque (BLER, *Block Error Rate*):**

$$\text{BLER} = \frac{\text{Número de bloques con al menos un error}}{\text{Número total de bloques transmitidos}}$$

El BLER es más relevante en sistemas que utilizan codificación de canal basada en bloques, ya que un solo bit erróneo en un bloque codificado puede causar la decodificación incorrecta de todo el bloque.

**Relación señal a ruido pico (PSNR, *Peak Signal-to-Noise Ratio*):**

$$\text{PSNR} = 10 \log_{10}\left(\frac{\text{MAX}^2}{\text{MSE}}\right) \text{ dB}$$

donde $\text{MAX}$ es el valor máximo posible del píxel (e.g., 255 para imágenes de 8 bits) y $\text{MSE}$ es el error cuadrático medio entre la imagen original y la reconstruida:

$$\text{MSE} = \frac{1}{M \times N}\sum_{i=1}^{M}\sum_{j=1}^{N}(I(i,j) - \hat{I}(i,j))^2$$

El PSNR es ampliamente utilizado para evaluar la calidad de imágenes reconstruidas. Valores típicos son 30-50 dB para una buena calidad. Sin embargo, el PSNR tiene una limitación fundamental: no se correlaciona bien con la percepción humana de calidad. Una imagen puede tener un PSNR alto pero ser visualmente insatisfactoria, y viceversa.

**Índice de similitud estructural (SSIM, *Structural Similarity Index*):**

$$\text{SSIM}(\mathbf{x}, \mathbf{y}) = \frac{(2\mu_x\mu_y + c_1)(2\sigma_{xy} + c_2)}{(\mu_x^2 + \mu_y^2 + c_1)(\sigma_x^2 + \sigma_y^2 + c_2)}$$

donde $\mu_x$ y $\mu_y$ son las medias, $\sigma_x^2$ y $\sigma_y^2$ son las varianzas, $\sigma_{xy}$ es la covarianza, y $c_1$, $c_2$ son constantes de estabilización. El SSIM evalúa la similitud estructural entre dos imágenes considerando luminancia, contraste y estructura, proporcionando una evaluación más alineada con la percepción humana que el PSNR. Sus valores van de -1 a 1, donde 1 indica imágenes idénticas.

### 7.6.2 Métricas semánticas

Las comunicaciones semánticas requieren métricas que evalúen la preservación del *significado*, no la fidelidad de los bits o los píxeles. Estas métricas operan en el espacio semántico y miden cuánto del significado original se preserva en la reconstrucción.

**BLEU (*Bilingual Evaluation Understudy*) para texto:**

El puntaje BLEU mide la superposición de n-gramas entre el texto generado y el texto de referencia. Se define como:

$$\text{BLEU} = \text{BP} \cdot \exp\left(\sum_{n=1}^{N} w_n \log p_n\right)$$

donde $p_n$ es la precisión de n-gramas modificada (la fracción de n-gramas en el texto generado que aparecen en la referencia, con recuento recortado para evitar repeticiones), $w_n = 1/N$ son pesos uniformes (típicamente $N = 4$), y $\text{BP}$ es una penalización por brevedad:

$$\text{BP} = \begin{cases} 1 & \text{si } c > r \\ e^{1 - r/c} & \text{si } c \leq r \end{cases}$$

donde $c$ es la longitud del texto generado y $r$ es la longitud de referencia. El BLEU varía de 0 a 1 y es una métrica parcialmente semántica: captura la superposición léxica, que se correlaciona con la similitud semántica, pero no captura sinónimos ni paráfrasis.

**ROUGE (*Recall-Oriented Understudy for Gisting Evaluation*) para texto:**

ROUGE es una familia de métricas que miden la superposición entre el texto generado y la referencia, enfocándose en el recall (cobertura) en lugar de la precisión. ROUGE-L, basado en la subsecuencia común más larga (*Longest Common Subsequence*, LCS), es particularmente útil:

$$\text{ROUGE-L} = \frac{(1 + \beta^2) \cdot R_{\text{LCS}} \cdot P_{\text{LCS}}}{R_{\text{LCS}} + \beta^2 \cdot P_{\text{LCS}}}$$

donde $R_{\text{LCS}} = \text{LCS}(X, Y) / |Y|$ es el recall basado en LCS, $P_{\text{LCS}} = \text{LCS}(X, Y) / |X|$ es la precisión basada en LCS, y $\beta$ controla la importancia relativa del recall sobre la precisión.

**Similitud semántica por coseno en espacio de embeddings:**

Quizás la métrica más directa para evaluar la preservación semántica es la **similitud coseno** entre las representaciones vectoriales (*embeddings*) del texto original y el reconstruido:

$$\text{sim}(\mathbf{a}, \mathbf{b}) = \frac{\mathbf{a} \cdot \mathbf{b}}{||\mathbf{a}|| \, ||\mathbf{b}||}$$

donde $\mathbf{a}, \mathbf{b} \in \mathbb{R}^d$ son los embeddings del texto original y reconstruido, obtenidos mediante un modelo pre-entrenado (e.g., Sentence-BERT). Esta métrica varía de -1 a 1, donde 1 indica significado idéntico, 0 indica ausencia de relación semántica, y -1 indica significados opuestos.

La similitud coseno tiene la propiedad deseable de ser independiente de la magnitud de los vectores y depender solo de su dirección en el espacio semántico. Esto la hace robusta a variaciones en la escala de las representaciones y permite comparaciones significativas entre textos de diferente longitud.

Para comprender por qué esta métrica es adecuada, recordemos que en un espacio de embeddings bien entrenado, las direcciones codifican relaciones semánticas. Dos vectores con alta similitud coseno apuntan aproximadamente en la misma dirección, lo que significa que capturan el mismo concepto semántico, incluso si las palabras utilizadas son diferentes.

**Tasa de éxito de la tarea:**

Para comunicaciones orientadas a tareas, la métrica más relevante es la **tasa de éxito de la tarea**:

$$\text{TSR} = \frac{\text{Número de tareas completadas exitosamente}}{\text{Número total de tareas intentadas}}$$

Esta métrica evalúa directamente el Nivel C de Weaver: ¿el receptor tomó la acción correcta? Es la métrica más pragmática y la más directamente útil en aplicaciones reales, pero requiere definir claramente qué constituye un "éxito" en la tarea específica.

**Tasa semántica:**

La **tasa semántica** (*semantic rate*) cuantifica la cantidad de significado transmitido por uso del canal:

$$R_{\text{sem}} = \frac{\text{Información semántica transmitida}}{\text{Número de usos del canal}}$$

La cuantificación precisa de la "información semántica transmitida" es un desafío abierto. Una aproximación práctica consiste en definirla como la información mutua semántica $I_{\text{sem}}(S; \hat{S})$, estimada mediante técnicas variacionales o basadas en embeddings. Otra aproximación utiliza la reducción en la entropía semántica del receptor:

$$R_{\text{sem}} = \frac{H_{\text{sem}}(S) - H_{\text{sem}}(S | \hat{S})}{k}$$

donde $k$ es el número de usos del canal. Esta definición captura intuitivamente la idea de "bits de significado por uso del canal".

### 7.6.3 Comparación entre métricas clásicas y semánticas

La siguiente tabla resume las diferencias fundamentales entre las métricas clásicas y semánticas:

| Aspecto | Métricas clásicas (BER, PSNR) | Métricas semánticas (similitud coseno, BLEU) |
|---|---|---|
| Nivel de Weaver | Nivel A (técnico) | Nivel B (semántico) / Nivel C (efectividad) |
| Objeto de medición | Fidelidad de bits/píxeles | Preservación de significado |
| Sensibilidad a sinónimos | Penaliza palabras diferentes | Reconoce significados equivalentes |
| Correlación con percepción humana | Moderada (PSNR) a baja (BER) | Alta |
| Aplicabilidad | Universal | Depende de la modalidad y tarea |
| Complejidad computacional | Baja | Moderada a alta |
| Necesidad de modelo auxiliar | No | Sí (modelo de embeddings) |

---

## 7.7 Ejemplo conceptual: transmisión semántica de texto

### 7.7.1 Descripción del ejemplo paso a paso

Para consolidar los conceptos presentados en esta sección, desarrollemos un ejemplo completo y detallado de transmisión semántica de texto, siguiendo cada etapa del procesamiento desde la fuente hasta el destino.

**Paso 1: Oración de entrada**

Consideremos la oración en español:

> "El avión aterrizó en el aeropuerto"

Esta oración contiene 6 tokens principales (excluyendo artículos como entrada independiente, o considerando subpalabras según el tokenizador). En un sistema con un vocabulario de 30,000 palabras, cada token se representa como un índice entero. La representación sintáctica (bit a bit) de esta oración requeriría aproximadamente $6 \times \lceil\log_2 30{,}000\rceil \approx 6 \times 15 = 90$ bits.

**Paso 2: Codificación semántica (Codificador Transformer)**

El codificador semántico, basado en un Transformer, procesa la oración de la siguiente manera:

a) *Tokenización y embedding*: Cada palabra se convierte en un vector de embedding de dimensión $d_{\text{model}} = 128$:

$$\mathbf{e}_1 = \text{Embed}(\text{"El"}), \quad \mathbf{e}_2 = \text{Embed}(\text{"avión"}), \quad \ldots, \quad \mathbf{e}_6 = \text{Embed}(\text{"aeropuerto"})$$

b) *Codificación posicional*: Se añade información posicional para que el modelo distinga el orden de las palabras:

$$\mathbf{h}_i^{(0)} = \mathbf{e}_i + \mathbf{PE}_i, \quad i = 1, \ldots, 6$$

c) *Capas del Transformer*: Los vectores pasan por $N_e = 4$ capas de codificador Transformer. En cada capa, el mecanismo de auto-atención permite que cada palabra atienda a todas las demás, construyendo progresivamente una representación más rica y contextualizada.

Después del procesamiento, la representación semántica de la oración es un conjunto de vectores $\mathbf{z} = \{\mathbf{z}_1, \ldots, \mathbf{z}_6\} \in \mathbb{R}^{6 \times d_z}$, donde $d_z = 16$ (la dimensión de la representación semántica por token, significativamente menor que $d_{\text{model}} = 128$, lo que implica una compresión de 8:1).

El vector semántico de la palabra "aterrizó" capturará no solo su significado léxico sino también su contexto: que el sujeto es un "avión" y que el destino es un "aeropuerto". Esta contextualización es la esencia de lo que hace que la representación sea *semántica* y no meramente *léxica*.

**Paso 3: Codificación de canal**

El codificador de canal transforma la representación semántica en símbolos adecuados para la transmisión:

$$\mathbf{x} = \text{ChEnc}(\mathbf{z}) \in \mathbb{R}^{k}$$

donde $k = 6 \times d_c$ y $d_c = 8$ es el número de símbolos de canal por token, resultando en $k = 48$ símbolos de canal reales. Estos se normalizan para satisfacer la restricción de potencia:

$$\mathbf{x} \leftarrow \sqrt{k} \cdot \frac{\mathbf{x}}{||\mathbf{x}||}$$

La cantidad total de información transmitida es de 48 valores reales. Si cada valor se cuantiza a 16 bits de punto flotante (half precision), esto corresponde a $48 \times 16 = 768$ bits. Sin embargo, en la transmisión analógica (como en los sistemas de comunicación semántica), los valores se transmiten como amplitudes continuas sin cuantización explícita, y la precisión efectiva depende de la SNR del canal.

**Paso 4: Canal AWGN**

La señal transmitida atraviesa un canal AWGN con $\text{SNR} = 7$ dB:

$$\mathbf{y} = \mathbf{x} + \mathbf{n}, \quad \mathbf{n} \sim \mathcal{N}(\mathbf{0}, \sigma_n^2 \mathbf{I})$$

donde $\sigma_n^2 = P_x / \text{SNR}_{\text{lineal}} = 1 / 10^{0.7} \approx 0.2$. Cada componente de la señal transmitida es perturbada por ruido gaussiano independiente con varianza 0.2 (desviación estándar ≈ 0.45).

**Paso 5: Decodificación de canal**

El decodificador de canal produce una estimación de la representación semántica:

$$\hat{\mathbf{z}} = \text{ChDec}(\mathbf{y})$$

Las capas densas del decodificador de canal han sido entrenadas para compensar los efectos del ruido, produciendo una estimación $\hat{\mathbf{z}}$ que es cercana a $\mathbf{z}$ pero no idéntica. El error de estimación $\boldsymbol{\epsilon} = \hat{\mathbf{z}} - \mathbf{z}$ depende del nivel de ruido y de la calidad del entrenamiento.

**Paso 6: Decodificación semántica (Decodificador Transformer)**

El decodificador Transformer genera la oración reconstruida de forma autorregresiva, token por token:

$$p(\hat{w}_t | \hat{w}_1, \ldots, \hat{w}_{t-1}, \hat{\mathbf{z}})$$

Para cada posición $t$, el decodificador calcula una distribución de probabilidad sobre todo el vocabulario y selecciona la palabra más probable (o utiliza *beam search* para explorar múltiples candidatos).

El resultado podría ser:

> "El avión llegó al aeropuerto"

Observemos que la oración reconstruida no es idéntica a la original: "aterrizó" ha sido reemplazado por "llegó" y "en el" por "al". Sin embargo, el *significado* se ha preservado casi perfectamente. El hecho de que un avión llegó/aterrizó en un aeropuerto se ha comunicado correctamente.

**Paso 7: Evaluación**

Evaluemos la calidad de la transmisión con diferentes métricas:

*Métricas sintácticas:*
- A nivel de caracteres, hay múltiples diferencias → BER relativamente alto.
- Si comparamos palabra por palabra: 4 de 6 palabras son diferentes ("aterrizó"→"llegó", "en"→"al", "el"→ ∅) → tasa de error de palabra del ~50%.

*Métricas semánticas:*
- Si usamos un modelo de embeddings para calcular los vectores semánticos $\mathbf{a}$ (original) y $\mathbf{b}$ (reconstruido), obtenemos:

$$\text{sim}(\mathbf{a}, \mathbf{b}) = \frac{\mathbf{a} \cdot \mathbf{b}}{||\mathbf{a}|| \, ||\mathbf{b}||} \approx 0.95$$

Una similitud coseno de 0.95 indica una excelente preservación del significado. El sistema clásico reportaría un "fallo" (alta tasa de error), mientras que el sistema semántico reporta un "éxito" (alta similitud semántica).

Este ejemplo ilustra de manera poderosa la diferencia fundamental entre los paradigmas: **en comunicaciones semánticas, la fidelidad de las palabras es secundaria; lo que importa es la fidelidad del significado**.

### 7.7.2 Pseudocódigo en PyTorch

A continuación presentamos un pseudocódigo en PyTorch que implementa la arquitectura conceptual del sistema de comunicación semántica descrito. Este código es pedagógico y tiene como objetivo ilustrar la estructura y el flujo de datos del sistema; una implementación de producción requeriría optimizaciones adicionales, manejo de vocabulario más sofisticado, y entrenamiento con datasets extensos.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
import math

# ============================================================
# Componentes del sistema de comunicación semántica
# ============================================================

class SemanticEncoder(nn.Module):
    """
    Codificador semántico basado en Transformer.
    Extrae características semánticas del texto de entrada.
    """
    def __init__(self, vocab_size, d_model=128, nhead=8,
                 num_layers=4, d_semantic=16):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, d_model)
        self.pos_encoder = PositionalEncoding(d_model)
        encoder_layer = nn.TransformerEncoderLayer(
            d_model=d_model, nhead=nhead,
            dim_feedforward=4*d_model, batch_first=True
        )
        self.transformer_encoder = nn.TransformerEncoder(
            encoder_layer, num_layers=num_layers
        )
        # Proyección a espacio semántico compacto
        self.semantic_proj = nn.Linear(d_model, d_semantic)

    def forward(self, src, src_mask=None):
        # src: (batch, seq_len) índices de tokens
        x = self.embedding(src)           # (batch, seq_len, d_model)
        x = self.pos_encoder(x)
        x = self.transformer_encoder(x, src_key_padding_mask=src_mask)
        z = self.semantic_proj(x)          # (batch, seq_len, d_semantic)
        return z


class ChannelEncoder(nn.Module):
    """
    Codificador de canal: mapea la representación semántica
    a símbolos de canal con normalización de potencia.
    """
    def __init__(self, d_semantic=16, d_channel=8):
        super().__init__()
        self.fc = nn.Sequential(
            nn.Linear(d_semantic, d_semantic),
            nn.ReLU(),
            nn.Linear(d_semantic, d_channel)
        )

    def forward(self, z):
        # z: (batch, seq_len, d_semantic)
        x = self.fc(z)                    # (batch, seq_len, d_channel)
        # Normalización de potencia
        x_flat = x.reshape(x.size(0), -1)
        power = torch.sqrt(torch.mean(x_flat**2, dim=-1, keepdim=True))
        x_flat = x_flat / (power + 1e-8)
        x = x_flat.reshape(x.shape)
        return x


class AWGNChannel(nn.Module):
    """
    Canal AWGN diferenciable.
    Añade ruido gaussiano según la SNR especificada.
    """
    def __init__(self):
        super().__init__()

    def forward(self, x, snr_db):
        if not self.training:
            snr_db = snr_db
        snr_linear = 10 ** (snr_db / 10.0)
        # Potencia de la señal normalizada a 1
        noise_power = 1.0 / snr_linear
        noise = torch.randn_like(x) * math.sqrt(noise_power)
        return x + noise


class RayleighChannel(nn.Module):
    """
    Canal de desvanecimiento Rayleigh diferenciable.
    Aplica desvanecimiento multiplicativo y ruido aditivo.
    """
    def __init__(self):
        super().__init__()

    def forward(self, x, snr_db):
        snr_linear = 10 ** (snr_db / 10.0)
        noise_power = 1.0 / snr_linear
        # Coeficientes de desvanecimiento Rayleigh
        h_real = torch.randn_like(x) / math.sqrt(2)
        h_imag = torch.randn_like(x) / math.sqrt(2)
        h_mag = torch.sqrt(h_real**2 + h_imag**2)
        # Señal desvanecida + ruido
        noise = torch.randn_like(x) * math.sqrt(noise_power)
        y = h_mag * x + noise
        return y


class ChannelDecoder(nn.Module):
    """
    Decodificador de canal: estima la representación
    semántica a partir de la señal recibida.
    """
    def __init__(self, d_channel=8, d_semantic=16):
        super().__init__()
        self.fc = nn.Sequential(
            nn.Linear(d_channel, d_semantic),
            nn.ReLU(),
            nn.Linear(d_semantic, d_semantic)
        )

    def forward(self, y):
        # y: (batch, seq_len, d_channel)
        z_hat = self.fc(y)               # (batch, seq_len, d_semantic)
        return z_hat


class SemanticDecoder(nn.Module):
    """
    Decodificador semántico basado en Transformer.
    Reconstruye el texto a partir de la representación
    semántica estimada.
    """
    def __init__(self, vocab_size, d_model=128, nhead=8,
                 num_layers=4, d_semantic=16):
        super().__init__()
        self.semantic_to_model = nn.Linear(d_semantic, d_model)
        decoder_layer = nn.TransformerDecoderLayer(
            d_model=d_model, nhead=nhead,
            dim_feedforward=4*d_model, batch_first=True
        )
        self.transformer_decoder = nn.TransformerDecoder(
            decoder_layer, num_layers=num_layers
        )
        self.output_proj = nn.Linear(d_model, vocab_size)

    def forward(self, z_hat, tgt_emb):
        # z_hat: (batch, seq_len, d_semantic) - memoria del decoder
        # tgt_emb: (batch, seq_len, d_model) - embeddings del target
        memory = self.semantic_to_model(z_hat)
        # Máscara causal para generación autorregresiva
        tgt_len = tgt_emb.size(1)
        tgt_mask = torch.triu(
            torch.ones(tgt_len, tgt_len, device=tgt_emb.device),
            diagonal=1
        ).bool()
        output = self.transformer_decoder(
            tgt_emb, memory, tgt_mask=tgt_mask
        )
        logits = self.output_proj(output)  # (batch, seq_len, vocab_size)
        return logits


class PositionalEncoding(nn.Module):
    """Codificación posicional sinusoidal."""
    def __init__(self, d_model, max_len=512):
        super().__init__()
        pe = torch.zeros(max_len, d_model)
        position = torch.arange(0, max_len).unsqueeze(1).float()
        div_term = torch.exp(
            torch.arange(0, d_model, 2).float()
            * (-math.log(10000.0) / d_model)
        )
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)
        self.register_buffer('pe', pe.unsqueeze(0))

    def forward(self, x):
        return x + self.pe[:, :x.size(1), :]


# ============================================================
# Sistema completo de comunicación semántica
# ============================================================

class SemanticCommSystem(nn.Module):
    """
    Sistema de comunicación semántica de extremo a extremo.
    Integra codificador semántico, codificador/decodificador
    de canal, canal físico, y decodificador semántico.
    """
    def __init__(self, vocab_size, d_model=128, nhead=8,
                 num_enc_layers=4, num_dec_layers=4,
                 d_semantic=16, d_channel=8,
                 channel_type='awgn'):
        super().__init__()
        self.sem_encoder = SemanticEncoder(
            vocab_size, d_model, nhead,
            num_enc_layers, d_semantic
        )
        self.ch_encoder = ChannelEncoder(d_semantic, d_channel)

        if channel_type == 'awgn':
            self.channel = AWGNChannel()
        elif channel_type == 'rayleigh':
            self.channel = RayleighChannel()

        self.ch_decoder = ChannelDecoder(d_channel, d_semantic)
        self.sem_decoder = SemanticDecoder(
            vocab_size, d_model, nhead,
            num_dec_layers, d_semantic
        )
        self.embedding = self.sem_encoder.embedding
        self.pos_encoder = self.sem_encoder.pos_encoder

    def forward(self, src, tgt, snr_db, src_mask=None):
        # --- Transmisor ---
        z = self.sem_encoder(src, src_mask)     # Codificación semántica
        x = self.ch_encoder(z)                   # Codificación de canal

        # --- Canal ---
        y = self.channel(x, snr_db)              # Canal físico

        # --- Receptor ---
        z_hat = self.ch_decoder(y)               # Decodificación de canal
        tgt_emb = self.pos_encoder(
            self.embedding(tgt)
        )
        logits = self.sem_decoder(z_hat, tgt_emb) # Decodificación semántica
        return logits


# ============================================================
# Ejemplo de uso: entrenamiento y evaluación
# ============================================================

def train_step(model, optimizer, src, tgt, snr_db):
    """Un paso de entrenamiento del sistema semántico."""
    model.train()
    optimizer.zero_grad()

    # Forward pass: tgt_input excluye último token,
    # tgt_output excluye primer token (teacher forcing)
    tgt_input = tgt[:, :-1]
    tgt_output = tgt[:, 1:]

    logits = model(src, tgt_input, snr_db)

    # Pérdida de entropía cruzada (semántica)
    loss = F.cross_entropy(
        logits.reshape(-1, logits.size(-1)),
        tgt_output.reshape(-1),
        ignore_index=0  # Ignorar padding
    )

    loss.backward()  # Retropropagación E2E
    optimizer.step()
    return loss.item()


def evaluate_semantic_similarity(original_emb, reconstructed_emb):
    """
    Calcula la similitud coseno entre embeddings
    del texto original y reconstruido.
    """
    cos_sim = F.cosine_similarity(
        original_emb, reconstructed_emb, dim=-1
    )
    return cos_sim.mean().item()


# --- Simulación conceptual ---
if __name__ == "__main__":
    VOCAB_SIZE = 30000
    model = SemanticCommSystem(
        vocab_size=VOCAB_SIZE,
        d_model=128, nhead=8,
        num_enc_layers=4, num_dec_layers=4,
        d_semantic=16, d_channel=8,
        channel_type='awgn'
    )
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-4)

    # Simulación con datos ficticios
    batch_size = 32
    seq_len = 10
    src = torch.randint(1, VOCAB_SIZE, (batch_size, seq_len))
    tgt = torch.randint(1, VOCAB_SIZE, (batch_size, seq_len))

    # Entrenar a diferentes SNR para robustez
    for epoch in range(100):
        snr_db = torch.FloatTensor(1).uniform_(0, 20).item()
        loss = train_step(model, optimizer, src, tgt, snr_db)
        if (epoch + 1) % 10 == 0:
            print(f"Epoch {epoch+1}, SNR={snr_db:.1f} dB, "
                  f"Loss={loss:.4f}")
```

### 7.7.3 Análisis del ejemplo

Este ejemplo ilustra varios puntos fundamentales:

**1. Compresión semántica.** La oración original de 6 tokens, cada uno con un embedding de dimensión 128, se comprime a una representación semántica de 6 vectores de dimensión 16 (compresión 8:1). El codificador de canal la transforma en $6 \times 8 = 48$ símbolos de canal. En un sistema clásico, los 90 bits de la oración, con codificación de canal a tasa 1/2 y modulación BPSK, requerirían 180 símbolos de canal. El sistema semántico logra una reducción significativa.

**2. Diferenciabilidad del canal.** El canal AWGN se implementa como una simple adición de ruido gaussiano, que es una operación diferenciable. Esto permite que los gradientes fluyan a través del canal durante el entrenamiento, haciendo posible la optimización de extremo a extremo. Durante la retropropagación, el gradiente de la pérdida con respecto a los símbolos transmitidos $\mathbf{x}$ es simplemente $\partial \mathcal{L}/\partial \mathbf{x} = \partial \mathcal{L}/\partial \mathbf{y}$, ya que $\mathbf{y} = \mathbf{x} + \mathbf{n}$ y el ruido $\mathbf{n}$ no depende de $\mathbf{x}$.

**3. Robustez a diferentes SNR.** El sistema se entrena con valores de SNR aleatorios en cada epoch (entre 0 y 20 dB), lo que le confiere robustez a un amplio rango de condiciones de canal. Esta estrategia de entrenamiento, conocida como *curriculum training* o entrenamiento con SNR variable, es una técnica común en comunicaciones semánticas que permite que un único modelo funcione bien en diferentes condiciones sin necesidad de adaptación.

**4. Preservación semántica vs. fidelidad léxica.** El decodificador semántico genera palabras secuencialmente, seleccionando en cada paso la palabra más probable dado el contexto. Esto puede resultar en paráfrasis: "aterrizó" → "llegó", una sustitución que preserva el significado pero cambia la forma léxica. Las métricas semánticas (similitud coseno) reflejan correctamente esta preservación, mientras que las métricas léxicas (BER, tasa de error de palabra) la penalizarían.

**5. Entrenamiento de extremo a extremo.** Todos los componentes — codificador semántico, codificador de canal, canal, decodificador de canal, decodificador semántico — forman un único grafo computacional. La función de pérdida (entropía cruzada) se calcula al final del sistema, y los gradientes se propagan hacia atrás a través de todos los módulos. No hay optimización separada de cada bloque; el sistema se optimiza como un todo, permitiendo que cada componente se adapte a los demás de forma sinérgica.

---

## Referencias

1. Shannon, C. E. (1948). "A Mathematical Theory of Communication." *The Bell System Technical Journal*, 27(3), 379–423.

2. Weaver, W. (1949). "Recent Contributions to the Mathematical Theory of Communication." En C. E. Shannon y W. Weaver, *The Mathematical Theory of Communication*. University of Illinois Press.

3. Xie, H., Qin, Z., Li, G. Y., y Juang, B.-H. (2021). "Deep Learning Enabled Semantic Communication Systems." *IEEE Transactions on Signal Processing*, 69, 2663–2675. DOI: [10.1109/TSP.2021.3071082](https://doi.org/10.1109/TSP.2021.3071082).

4. Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., y Polosukhin, I. (2017). "Attention Is All You Need." *Advances in Neural Information Processing Systems (NeurIPS)*, 30.
