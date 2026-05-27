# Tutorial de Redes Inalámbricas — Parte 2: Estándares WiFi 5, WiFi 6 y WiFi 6E

**Autor:** Tutorial Pedagógico de Telecomunicaciones  
**Nivel:** Introductorio–Intermedio  
**Prerrequisitos:** Parte 1 — Fundamentos de Propagación y Comunicaciones Inalámbricas

---

## 5. Introducción a las Redes WiFi

### 5.1 ¿Qué es WiFi?

WiFi es una tecnología de comunicación inalámbrica que permite a dispositivos electrónicos intercambiar datos mediante ondas de radio, sin necesidad de cables físicos. El término "WiFi" es una marca comercial registrada por la **Wi-Fi Alliance**, una organización sin fines de lucro que certifica la interoperabilidad de productos basados en los estándares **IEEE 802.11**. Es importante aclarar un error común: WiFi **no** es un acrónimo de "Wireless Fidelity"; el nombre fue creado por la firma de marketing Interbrand como una marca fácil de recordar.

Desde el punto de vista técnico, WiFi implementa las capas **PHY** (física) y **MAC** (control de acceso al medio) del modelo OSI, ambas definidas por la familia de estándares IEEE 802.11. La capa PHY se encarga de la modulación, codificación y transmisión de señales de radiofrecuencia, mientras que la capa MAC gestiona el acceso al medio compartido, la formación de tramas, la autenticación y la asociación de dispositivos.

**La familia IEEE 802.11** es un conjunto de estándares desarrollados por el Instituto de Ingenieros Eléctricos y Electrónicos (IEEE) desde 1997. Cada enmienda al estándar original se identifica con un sufijo de una o dos letras (por ejemplo, 802.11a, 802.11b, 802.11n, 802.11ac, 802.11ax). A partir de 2018, la Wi-Fi Alliance introdujo una nomenclatura simplificada basada en generaciones numéricas (WiFi 4, WiFi 5, WiFi 6, etc.) para facilitar la comprensión del consumidor.

**Concepto de WLAN (Wireless Local Area Network):** Una WLAN es una red de área local que utiliza ondas de radio en lugar de cables para conectar dispositivos. A diferencia de las redes celulares, que cubren áreas extensas (kilómetros), las WLAN están diseñadas para cubrir áreas relativamente pequeñas: una habitación, un edificio o un campus. Las WLAN basadas en IEEE 802.11 operan en bandas de espectro **no licenciado** (ISM/UNII), lo que significa que cualquier persona puede desplegar una red WiFi sin necesidad de adquirir una licencia de espectro.

**Analogía pedagógica — WiFi como una conversación en una sala:** Imagine una sala de conferencias donde varias personas desean comunicarse. En una red cableada (Ethernet), cada persona tendría un tubo de comunicación privado con el moderador (switch): pueden hablar simultáneamente sin interferirse. En WiFi, todas las personas comparten el mismo aire: si dos personas hablan al mismo tiempo, se produce una "colisión" y nadie entiende nada. Por eso WiFi utiliza un protocolo llamado **CSMA/CA** (Carrier Sense Multiple Access with Collision Avoidance): antes de hablar, cada persona escucha si alguien más está hablando; si el canal está libre, espera un tiempo aleatorio adicional y luego transmite. Esta analogía ilustra por qué el rendimiento de WiFi se degrada en entornos densos con muchos usuarios.

**Arquitectura básica de una red WiFi:**

La arquitectura fundamental de IEEE 802.11 se compone de los siguientes elementos:

- **STA (Station):** Cualquier dispositivo con una interfaz de red inalámbrica 802.11. Incluye laptops, smartphones, tablets, dispositivos IoT, etc. Cada STA tiene una dirección MAC única de 48 bits.

- **AP (Access Point):** Un dispositivo que actúa como puente entre la red inalámbrica y la red cableada (generalmente Ethernet). El AP transmite periódicamente tramas *beacon* (balizas) que anuncian la existencia de la red, su SSID (nombre), las tasas soportadas y los parámetros de seguridad.

- **BSS (Basic Service Set):** Es la unidad fundamental de una red WiFi. Un BSS consta de un AP y todas las STAs asociadas a él. Cada BSS se identifica mediante un **BSSID**, que es la dirección MAC del AP. El área de cobertura de un BSS se denomina **BSA** (Basic Service Area). Existe también el modo **IBSS** (Independent BSS), conocido como modo ad-hoc, donde las STAs se comunican directamente entre sí sin un AP.

- **DS (Distribution System):** Es la infraestructura (generalmente una red Ethernet cableada) que interconecta múltiples APs, permitiendo que las STAs asociadas a diferentes APs se comuniquen entre sí.

- **ESS (Extended Service Set):** Es un conjunto de BSS interconectados a través del DS que comparten el mismo **SSID**. Desde la perspectiva del usuario, un ESS aparece como una única red inalámbrica. Cuando una STA se mueve de un BSS a otro dentro del mismo ESS, realiza un proceso de **roaming** (itinerancia) que idealmente es transparente para el usuario.

**Descripción de Figura — Arquitectura BSS y ESS:**

> *La Figura 5.1 muestra la arquitectura jerárquica de una red WiFi. En la parte izquierda se representa un BSS individual: un punto de acceso (AP₁) se dibuja como un triángulo en el centro, rodeado por un círculo punteado que representa su área de cobertura (BSA₁). Dentro de este círculo, tres estaciones (STA₁, STA₂, STA₃) se representan como rectángulos pequeños (laptop, smartphone, tablet). Líneas onduladas conectan cada STA con el AP, representando los enlaces inalámbricos. En la parte derecha se muestra un segundo BSS (AP₂ con STA₄ y STA₅). Ambos APs están conectados mediante líneas sólidas a un switch Ethernet que forma el Distribution System (DS). El conjunto de ambos BSS forma un ESS, indicado por un rectángulo punteado grande que engloba toda la estructura. Una flecha curvada entre los dos BSS indica la zona de superposición donde es posible el roaming. En la parte superior, el DS se conecta a un router que proporciona acceso a Internet.*

### 5.2 Evolución Histórica de WiFi

La tecnología WiFi ha experimentado una evolución extraordinaria desde su primera versión en 1997. Cada nueva generación ha introducido mejoras significativas en velocidad, eficiencia, alcance y capacidad para manejar múltiples dispositivos. A continuación se presenta un recorrido cronológico completo.

**IEEE 802.11 original (1997):** El estándar original definió velocidades de 1 y 2 Mbps en la banda de 2.4 GHz, utilizando técnicas de espectro ensanchado por salto de frecuencia (FHSS) y por secuencia directa (DSSS). Aunque revolucionario en concepto, estas velocidades eran demasiado limitadas para la mayoría de aplicaciones prácticas.

**IEEE 802.11b (1999) — WiFi 1:** Incrementó la velocidad máxima a 11 Mbps en 2.4 GHz mediante la modulación CCK (Complementary Code Keying). Fue el primer estándar WiFi comercialmente exitoso, impulsando la adopción masiva en hogares y oficinas. Sin embargo, la banda de 2.4 GHz solo ofrece 3 canales no solapados (1, 6, 11), lo que limita la capacidad en entornos densos.

**IEEE 802.11a (1999) — WiFi 2:** Lanzado simultáneamente con 802.11b, introdujo la modulación **OFDM** (Orthogonal Frequency Division Multiplexing) en la banda de 5 GHz, alcanzando hasta 54 Mbps. Aunque técnicamente superior, su mayor costo y menor alcance (debido a la mayor atenuación a 5 GHz) retrasaron su adopción.

**IEEE 802.11g (2003) — WiFi 3:** Combinó lo mejor de 802.11a y 802.11b: OFDM en la banda de 2.4 GHz, logrando 54 Mbps con compatibilidad hacia atrás con 802.11b. Se convirtió en el estándar dominante durante la primera mitad de la década de 2000.

**IEEE 802.11n (2009) — WiFi 4:** Marcó un salto cualitativo con la introducción de **MIMO** (Multiple-Input Multiple-Output), que utiliza múltiples antenas para transmitir y recibir flujos de datos paralelos. Soporta hasta 4 flujos espaciales, anchos de canal de 20 y 40 MHz, y opera en ambas bandas (2.4 y 5 GHz). La velocidad máxima teórica es de 600 Mbps (4 flujos × 150 Mbps/flujo). También introdujo la agregación de tramas (A-MPDU, A-MSDU) para mejorar la eficiencia MAC.

**IEEE 802.11ac (2013/2016) — WiFi 5:** Operando exclusivamente en 5 GHz, introdujo anchos de canal de hasta 160 MHz, modulación 256-QAM, MU-MIMO en enlace descendente (hasta 8 flujos espaciales) y beamforming estandarizado. La Ola 1 (2013) soportaba hasta 80 MHz y SU-MIMO; la Ola 2 (2016) añadió 160 MHz y MU-MIMO. Velocidad máxima: 6.93 Gbps.

**IEEE 802.11ax (2021) — WiFi 6/6E:** Diseñado para entornos densos, introdujo OFDMA, 1024-QAM, MU-MIMO bidireccional (DL + UL), BSS Coloring, Target Wake Time y mayor duración de símbolo OFDM. WiFi 6E extiende las mismas capacidades a la banda de 6 GHz (5.925–7.125 GHz), añadiendo hasta 1200 MHz de espectro adicional. Velocidad máxima: 9.6 Gbps.

**IEEE 802.11be (2024) — WiFi 7:** La generación más reciente introduce operación multi-enlace (MLO), modulación 4096-QAM (4K-QAM), canales de 320 MHz, MIMO mejorado (16 flujos espaciales) y latencia ultra-baja. Velocidad máxima teórica: ~46 Gbps.

**IEEE 802.11bn (en desarrollo) — WiFi 8:** Actualmente en fase de definición, WiFi 8 se enfocará en comunicaciones cooperativas, MIMO distribuido, y acceso coordinado al medio para alcanzar velocidades aún mayores y mejorar la eficiencia en redes extremadamente densas.

**Tabla 5.1 — Comparativa de Generaciones WiFi**

| Generación | Estándar IEEE | Año | Banda(s) (GHz) | Ancho Canal Máx. | Modulación Máx. | MIMO Máx. | Velocidad Máx. Teórica |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| — | 802.11 | 1997 | 2.4 | 22 MHz | DSSS/FHSS | — | 2 Mbps |
| WiFi 1 | 802.11b | 1999 | 2.4 | 22 MHz | CCK | — | 11 Mbps |
| WiFi 2 | 802.11a | 1999 | 5 | 20 MHz | 64-QAM OFDM | — | 54 Mbps |
| WiFi 3 | 802.11g | 2003 | 2.4 | 20 MHz | 64-QAM OFDM | — | 54 Mbps |
| WiFi 4 | 802.11n | 2009 | 2.4 / 5 | 40 MHz | 64-QAM OFDM | 4×4 | 600 Mbps |
| WiFi 5 | 802.11ac | 2013 | 5 | 160 MHz | 256-QAM OFDM | 8×8 MU-MIMO DL | 6.93 Gbps |
| WiFi 6 | 802.11ax | 2021 | 2.4 / 5 | 160 MHz | 1024-QAM OFDMA | 8×8 MU-MIMO DL+UL | 9.6 Gbps |
| WiFi 6E | 802.11ax | 2021 | 6 | 160 MHz | 1024-QAM OFDMA | 8×8 MU-MIMO DL+UL | 9.6 Gbps |
| WiFi 7 | 802.11be | 2024 | 2.4 / 5 / 6 | 320 MHz | 4096-QAM OFDMA | 16×16 MU-MIMO | ~46 Gbps |
| WiFi 8 | 802.11bn | ~2028 | 2.4 / 5 / 6 | 320 MHz | 4096-QAM+ | Dist. MIMO | TBD |

**Descripción de Figura — Línea de Tiempo de la Evolución WiFi:**

> *La Figura 5.2 presenta una línea de tiempo horizontal que abarca desde 1997 hasta 2028. Sobre el eje temporal, cada generación WiFi se marca con un punto y una etiqueta vertical. En 1997 se ubica "802.11 (2 Mbps)"; en 1999, dos puntos para "802.11a (54 Mbps, 5 GHz)" y "802.11b (11 Mbps, 2.4 GHz)"; en 2003, "802.11g (54 Mbps)"; en 2009, "802.11n / WiFi 4 (600 Mbps)" con un ícono de antenas MIMO; en 2013, "802.11ac / WiFi 5 (6.9 Gbps)" con un ícono de MU-MIMO; en 2021, "802.11ax / WiFi 6/6E (9.6 Gbps)" con íconos de OFDMA y 6 GHz; en 2024, "802.11be / WiFi 7 (~46 Gbps)" con un ícono de MLO; y en 2028, "802.11bn / WiFi 8 (TBD)" con línea punteada indicando futuro. Debajo de la línea, barras de colores muestran la evolución del ancho de canal (de 22 MHz a 320 MHz) y la modulación (de DSSS a 4096-QAM). La escala vertical logarítmica a la derecha muestra el crecimiento exponencial de la velocidad máxima teórica.*

---

## 6. WiFi 5 (IEEE 802.11ac)

### 6.1 Características Principales

WiFi 5, formalmente definido por la enmienda **IEEE 802.11ac**, fue publicado en dos fases: la **Ola 1** fue certificada por la Wi-Fi Alliance en junio de 2013, y la **Ola 2** en junio de 2016. Este estándar fue diseñado con un objetivo claro: proporcionar velocidades multi-gigabit en la banda de 5 GHz para satisfacer la creciente demanda de streaming de video de alta definición, transferencia de archivos grandes y aplicaciones en la nube.

Las características principales de WiFi 5 son:

- **Banda de operación:** Exclusivamente **5 GHz**. A diferencia de WiFi 4 (802.11n), que opera en 2.4 y 5 GHz, WiFi 5 se concentra en 5 GHz para aprovechar el espectro más limpio y los anchos de canal mayores disponibles en esta banda. Los dispositivos WiFi 5 que también soportan 2.4 GHz lo hacen mediante la parte 802.11n del chipset.

- **Ancho de canal:** Soporta canales de **20, 40, 80 y 160 MHz**. El canal de 80 MHz es obligatorio para la certificación WiFi 5, mientras que 160 MHz es opcional. El ancho de 160 MHz puede implementarse como un canal contiguo de 160 MHz o como **80+80 MHz** (dos segmentos de 80 MHz no contiguos).

- **Modulación:** Hasta **256-QAM** (Quadrature Amplitude Modulation), que codifica 8 bits por símbolo. Esto representa un incremento del 33% sobre la 64-QAM de WiFi 4 (6 bits por símbolo).

- **MIMO:** Soporta hasta **8 flujos espaciales** (8×8:8 MIMO), aunque la mayoría de dispositivos comerciales implementan 2×2 o 4×4. Introduce **MU-MIMO** (Multi-User MIMO) en enlace descendente, permitiendo que el AP transmita simultáneamente a hasta 4 usuarios (Ola 2).

- **Beamforming:** A diferencia de WiFi 4, donde el beamforming era opcional y existían múltiples métodos incompatibles, WiFi 5 estandariza un único mecanismo de beamforming basado en **NDP** (Null Data Packet) sounding, haciéndolo obligatorio para dispositivos que implementan más de un flujo espacial.

- **Velocidad máxima teórica:** **6.93 Gbps** con la configuración máxima (8 flujos espaciales, 160 MHz, 256-QAM, intervalo de guarda corto de 400 ns).

### 6.2 Mejoras sobre WiFi 4 (802.11n)

WiFi 5 introdujo cuatro mejoras fundamentales respecto a su predecesor. A continuación se explica cada una en detalle.

#### 6.2.1 Mayor Ancho de Banda: Hasta 160 MHz vs 40 MHz

En comunicaciones digitales, el ancho de banda del canal tiene un impacto directo sobre la tasa de transmisión. Según el teorema de Shannon, la capacidad de un canal es:

$$C = B \cdot \log_2(1 + \text{SNR})$$

donde $C$ es la capacidad en bits por segundo, $B$ es el ancho de banda en Hz y SNR es la relación señal a ruido. Duplicar el ancho de banda $B$ duplica la capacidad. WiFi 5 cuadruplica el ancho máximo de canal respecto a WiFi 4 (de 40 MHz a 160 MHz), lo que teóricamente cuadruplica la velocidad por flujo espacial.

En la práctica, un canal de 80 MHz en WiFi 5 contiene **234 subportadoras de datos** (frente a 108 en un canal de 40 MHz de WiFi 4), lo que más que duplica el número de subportadoras disponibles para transmitir datos. Un canal de 160 MHz contiene **468 subportadoras de datos**.

Sin embargo, es importante destacar que canales más anchos también capturan más ruido térmico (el piso de ruido aumenta en $10\log_{10}(B)$ dB) y son más susceptibles a la interferencia, lo que puede reducir el rango efectivo del enlace.

#### 6.2.2 MU-MIMO Downlink (Hasta 4 usuarios simultáneos)

En WiFi 4, el AP solo podía comunicarse con **una STA a la vez** en cada instante, independientemente de cuántas antenas tuviera. Esto se denomina **SU-MIMO** (Single-User MIMO). WiFi 5 introduce **MU-MIMO** (Multi-User MIMO) en el enlace descendente, lo que permite al AP dividir sus flujos espaciales entre múltiples usuarios simultáneos.

Por ejemplo, un AP 4×4 en WiFi 4 podría enviar 4 flujos espaciales a un único cliente 4×4, logrando una alta velocidad para ese cliente pero dejando a los demás en espera. Con MU-MIMO en WiFi 5, el mismo AP puede enviar simultáneamente 1 flujo a cada uno de 4 clientes 1×1, multiplicando la capacidad agregada de la red.

El MU-MIMO funciona mediante técnicas de **precodificación** (precoding): el AP aplica una matriz de pesos a las señales transmitidas por cada antena para crear haces dirigidos hacia cada usuario, minimizando la interferencia inter-usuario. Para ello, el AP necesita conocer el canal hacia cada STA, lo que se logra mediante el proceso de **channel sounding** con tramas NDP.

La tasa total del sistema con MU-MIMO puede expresarse como:

$$R_{\text{total}} = \sum_{k=1}^{K} R_k = \sum_{k=1}^{K} N_{s,k} \cdot r_k$$

donde $K$ es el número de usuarios simultáneos (hasta 4 en WiFi 5), $N_{s,k}$ es el número de flujos espaciales asignados al usuario $k$, y $r_k$ es la tasa por flujo del usuario $k$.

#### 6.2.3 256-QAM vs 64-QAM: Explicación Detallada de QAM

**QAM (Quadrature Amplitude Modulation)** es un esquema de modulación digital que combina modulación de amplitud en dos portadoras en cuadratura (desfasadas 90°). Cada símbolo QAM se representa como un punto en el plano complejo (diagrama de constelación), definido por una amplitud $I$ (in-phase) y una amplitud $Q$ (quadrature):

$$s(t) = I \cdot \cos(2\pi f_c t) - Q \cdot \sin(2\pi f_c t)$$

donde $f_c$ es la frecuencia de la portadora, $I$ y $Q$ son las componentes en fase y en cuadratura respectivamente.

En un esquema $M$-QAM, existen $M$ puntos posibles en la constelación, cada uno representando una combinación única de $\log_2(M)$ bits:

| Modulación | $M$ | Bits/símbolo ($\log_2 M$) | Uso en WiFi |
|:---:|:---:|:---:|:---:|
| BPSK | 2 | 1 | MCS 0 |
| QPSK | 4 | 2 | MCS 1-2 |
| 16-QAM | 16 | 4 | MCS 3-4 |
| 64-QAM | 64 | 6 | MCS 5-7 (WiFi 4) |
| 256-QAM | 256 | 8 | MCS 8-9 (WiFi 5) |
| 1024-QAM | 1024 | 10 | MCS 10-11 (WiFi 6) |

**Diagrama de constelación de 64-QAM:** La constelación forma una cuadrícula de $8 \times 8 = 64$ puntos uniformemente espaciados. Cada punto codifica 6 bits (por ejemplo, el punto en la esquina superior derecha podría representar "000000" y el punto inferior izquierdo "111111", usando codificación Gray para minimizar errores de bit en puntos adyacentes). La distancia mínima entre puntos adyacentes determina la robustez frente al ruido.

**Diagrama de constelación de 256-QAM:** La constelación forma una cuadrícula de $16 \times 16 = 256$ puntos. Al duplicar el número de niveles en cada eje (de 8 a 16), los puntos están más cercanos entre sí para la misma potencia promedio de señal, lo que exige un SNR más alto para decodificar correctamente. Cada punto codifica 8 bits.

**Descripción de Figura — Constelaciones QAM:**

> *La Figura 6.1 muestra tres diagramas de constelación lado a lado. A la izquierda, la constelación 64-QAM: una cuadrícula regular de 8×8 = 64 puntos azules en el plano I-Q, con ejes I (horizontal) y Q (vertical). Los puntos están espaciados uniformemente, y cada punto lleva una etiqueta de 6 bits en codificación Gray. La distancia mínima entre puntos adyacentes se marca con una línea roja y la etiqueta $d_{\min}$. En el centro, la constelación 256-QAM: una cuadrícula de 16×16 = 256 puntos verdes, más densamente empaquetados. Se observa claramente que $d_{\min}$ es menor que en 64-QAM para la misma potencia media. A la derecha, un gráfico de barras compara los bits por símbolo: 6 bits para 64-QAM y 8 bits para 256-QAM, con una flecha indicando la mejora del 33%. Debajo de cada constelación se indica el requisito aproximado de SNR: ~24 dB para 64-QAM y ~30 dB para 256-QAM.*

La ganancia de eficiencia espectral al pasar de 64-QAM a 256-QAM es:

$$\text{Ganancia} = \frac{\log_2(256) - \log_2(64)}{\log_2(64)} \times 100\% = \frac{8 - 6}{6} \times 100\% = 33.3\%$$

Sin embargo, esta ganancia tiene un costo: el SNR requerido para decodificar 256-QAM correctamente es aproximadamente 6 dB mayor que para 64-QAM, lo que significa que 256-QAM solo es utilizable cuando el dispositivo está relativamente cerca del AP y el canal es de buena calidad.

#### 6.2.4 Beamforming Obligatorio

**Beamforming** (conformación de haz) es una técnica de procesamiento de señales que utiliza múltiples antenas para dirigir la energía de la señal transmitida hacia la ubicación del receptor deseado, en lugar de radiar en todas las direcciones por igual. Esto aumenta la potencia recibida por el dispositivo destino y reduce la interferencia hacia otros dispositivos.

En un arreglo de $N$ antenas, la señal transmitida por cada antena se multiplica por un peso complejo $w_n$. La ganancia del arreglo en la dirección del receptor es:

$$G_{\text{BF}} = \left| \sum_{n=0}^{N-1} w_n \cdot e^{j \cdot n \cdot k \cdot d \cdot \sin(\theta)} \right|^2$$

donde $k = 2\pi/\lambda$ es el número de onda, $d$ es la separación entre antenas (típicamente $\lambda/2$), $\theta$ es el ángulo de llegada y $w_n$ son los pesos de beamforming calculados a partir de la información de canal (CSI).

Si los pesos se eligen de forma óptima (conjugado del canal, $w_n = h_n^*$), la ganancia de beamforming para $N$ antenas es:

$$G_{\text{BF, máx}} = 10 \log_{10}(N) \quad \text{[dB]}$$

Por ejemplo, un AP con $N = 4$ antenas puede lograr una ganancia de beamforming de $10\log_{10}(4) = 6$ dB, lo que equivale a cuadruplicar la potencia efectiva en la dirección del receptor.

En WiFi 5, el proceso de beamforming funciona así:

1. El AP envía una trama **NDP Announcement** seguida de una trama **NDP** (Null Data Packet).
2. La STA estima el canal a partir del NDP y calcula una **matriz de beamforming comprimida** $\mathbf{V}$ (usando descomposición SVD del canal).
3. La STA envía la matriz $\mathbf{V}$ al AP en una trama **Beamforming Report**.
4. El AP utiliza $\mathbf{V}$ para precodificar las transmisiones futuras hacia esa STA.

**Descripción de Figura — Beamforming:**

> *La Figura 6.2 ilustra el concepto de beamforming. En la parte superior, se muestra un AP con 4 antenas transmitiendo sin beamforming: el patrón de radiación es omnidireccional (un círculo azul claro que irradia uniformemente en todas las direcciones), y la potencia recibida por la STA objetivo es baja. En la parte inferior, el mismo AP con beamforming activado: el patrón de radiación se concentra en un lóbulo principal (color verde intenso) dirigido hacia la STA objetivo, mientras que en otras direcciones la radiación es mínima (lóbulos secundarios pequeños). Flechas indican las señales de cada antena, mostrando que cada una transmite con una fase ligeramente diferente ($\phi_1, \phi_2, \phi_3, \phi_4$) para lograr la interferencia constructiva en la dirección deseada. Un diagrama polar a la derecha cuantifica la diferencia: la ganancia en la dirección de la STA pasa de 0 dBi (sin beamforming) a +6 dBi (con beamforming de 4 antenas).*

### 6.3 Cálculo de Velocidad PHY WiFi 5

La velocidad de la capa física (PHY rate) en WiFi 5 se calcula mediante la siguiente fórmula:

$$R_{\text{PHY}} = N_{SS} \times N_{SD} \times b \times R_c \times \frac{1}{T_{\text{SYM}}}$$

donde cada variable tiene el siguiente significado:

- $N_{SS}$: **Número de flujos espaciales** (spatial streams). Es el número de flujos de datos independientes transmitidos simultáneamente mediante MIMO. WiFi 5 soporta de 1 a 8 flujos. El número de flujos está limitado por $\min(N_{TX}, N_{RX})$, donde $N_{TX}$ y $N_{RX}$ son el número de antenas del transmisor y receptor.

- $N_{SD}$: **Número de subportadoras de datos** por símbolo OFDM. En OFDM, el canal se divide en múltiples subportadoras ortogonales. No todas transportan datos: algunas son subportadoras piloto (para estimación de canal), subportadoras nulas (en los bordes del canal) y la subportadora DC (en el centro). Los valores de $N_{SD}$ en WiFi 5 son:
  - 20 MHz: $N_{SD} = 52$
  - 40 MHz: $N_{SD} = 108$
  - 80 MHz: $N_{SD} = 234$
  - 160 MHz: $N_{SD} = 468$

- $b$: **Bits por símbolo de modulación** ($\log_2 M$, donde $M$ es el orden de modulación). Los valores dependen del MCS (Modulation and Coding Scheme):
  - BPSK: $b = 1$
  - QPSK: $b = 2$
  - 16-QAM: $b = 4$
  - 64-QAM: $b = 6$
  - 256-QAM: $b = 8$

- $R_c$: **Tasa de codificación** (code rate). Es la proporción de bits de información respecto al total de bits transmitidos (datos + redundancia). WiFi 5 utiliza codificación BCC (Binary Convolutional Coding) o LDPC (Low-Density Parity-Check). Valores típicos: $1/2$, $2/3$, $3/4$, $5/6$.

- $T_{\text{SYM}}$: **Duración del símbolo OFDM**, que incluye la duración útil del símbolo más el intervalo de guarda (GI). En WiFi 5:
  - Duración útil del símbolo: $T_{\text{FFT}} = 3.2 \, \mu\text{s}$
  - Intervalo de guarda normal: $T_{\text{GI}} = 0.8 \, \mu\text{s}$, resultando en $T_{\text{SYM}} = 3.2 + 0.8 = 4.0 \, \mu\text{s}$
  - Intervalo de guarda corto: $T_{\text{GI}} = 0.4 \, \mu\text{s}$, resultando en $T_{\text{SYM}} = 3.2 + 0.4 = 3.6 \, \mu\text{s}$

**Estructura del símbolo OFDM en WiFi 5:**

Un símbolo OFDM consiste en dos partes:

1. **Periodo útil ($T_{\text{FFT}}$):** Es la parte del símbolo que contiene la información. Se genera aplicando una IFFT (Transformada Rápida de Fourier Inversa) a los datos modulados en las subportadoras. En WiFi 5, $T_{\text{FFT}} = 3.2 \, \mu\text{s}$, lo que corresponde a un espaciado entre subportadoras de:

$$\Delta f = \frac{1}{T_{\text{FFT}}} = \frac{1}{3.2 \times 10^{-6}} = 312.5 \, \text{kHz}$$

2. **Intervalo de guarda ($T_{\text{GI}}$):** Es una copia cíclica del final del símbolo que se antepone al inicio. Su propósito es absorber la dispersión temporal del canal (multipath), evitando la interferencia intersimbólica (ISI). Si el retardo máximo de propagación multitrayecto ($\tau_{\max}$) es menor que $T_{\text{GI}}$, no habrá ISI. En WiFi 5, el GI estándar es $0.8 \, \mu\text{s}$ y el corto es $0.4 \, \mu\text{s}$. El GI corto solo debe usarse cuando el entorno de propagación tiene poca dispersión temporal.

**Ejemplo numérico completo — Velocidad máxima de WiFi 5:**

Calculemos la velocidad PHY máxima teórica con la configuración más agresiva:

Parámetros:
- $N_{SS} = 8$ (8 flujos espaciales, 8×8 MIMO)
- $N_{SD} = 468$ (canal de 160 MHz)
- $b = 8$ (256-QAM)
- $R_c = 5/6$ (MCS 9)
- $T_{\text{SYM}} = 3.6 \, \mu\text{s}$ (GI corto de 0.4 μs)

Sustituyendo:

$$R_{\text{PHY}} = 8 \times 468 \times 8 \times \frac{5}{6} \times \frac{1}{3.6 \times 10^{-6}}$$

Paso a paso:

$$R_{\text{PHY}} = 8 \times 468 \times 8 \times 0.8333 \times 277{,}778$$

$$= 8 \times 468 \times 8 \times 0.8333 \times 277{,}778$$

Primero: $8 \times 468 = 3{,}744$

Luego: $3{,}744 \times 8 = 29{,}952$ bits por símbolo OFDM (antes de coding)

Con code rate: $29{,}952 \times 5/6 = 24{,}960$ bits de información por símbolo

Tasa: $24{,}960 / 3.6 \times 10^{-6} = 6{,}933{,}333{,}333$ bps

$$\boxed{R_{\text{PHY, máx}} = 6.93 \, \text{Gbps}}$$

**Ejemplo para una configuración común — Laptop con WiFi 5 (2×2, 80 MHz):**

- $N_{SS} = 2$
- $N_{SD} = 234$ (80 MHz)
- $b = 8$ (256-QAM, MCS 9)
- $R_c = 5/6$
- $T_{\text{SYM}} = 3.6 \, \mu\text{s}$ (GI corto)

$$R_{\text{PHY}} = 2 \times 234 \times 8 \times \frac{5}{6} \times \frac{1}{3.6 \times 10^{-6}}$$

$$= 2 \times 234 \times 8 \times 0.8333 \times 277{,}778$$

$$= 2 \times 234 = 468$$

$$468 \times 8 = 3{,}744$$

$$3{,}744 \times 0.8333 = 3{,}120$$

$$3{,}120 \times 277{,}778 = 866{,}666{,}667 \, \text{bps}$$

$$\boxed{R_{\text{PHY}} = 866.7 \, \text{Mbps}}$$

**Tabla 6.1 — Velocidades PHY comunes de WiFi 5 (GI = 0.4 μs)**

| Config. MIMO | Ancho Canal | MCS | Modulación | $R_c$ | Velocidad PHY |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 1×1 | 20 MHz | 9 | 256-QAM | 5/6 | 96.3 Mbps |
| 1×1 | 40 MHz | 9 | 256-QAM | 5/6 | 200 Mbps |
| 1×1 | 80 MHz | 9 | 256-QAM | 5/6 | 433.3 Mbps |
| 2×2 | 80 MHz | 9 | 256-QAM | 5/6 | 866.7 Mbps |
| 3×3 | 80 MHz | 9 | 256-QAM | 5/6 | 1.3 Gbps |
| 4×4 | 80 MHz | 9 | 256-QAM | 5/6 | 1.73 Gbps |
| 4×4 | 160 MHz | 9 | 256-QAM | 5/6 | 3.47 Gbps |
| 8×8 | 160 MHz | 9 | 256-QAM | 5/6 | 6.93 Gbps |

### 6.4 Canales en 5 GHz

La banda de 5 GHz ofrece significativamente más espectro que la banda de 2.4 GHz, pero está dividida en varias sub-bandas con distintas regulaciones. En Estados Unidos (regulación FCC), estas sub-bandas se denominan **UNII** (Unlicensed National Information Infrastructure):

- **UNII-1 (5.150–5.250 GHz):** Canales 36, 40, 44, 48. Originalmente limitada a uso interior con potencia máxima de 200 mW (23 dBm) EIRP. No requiere DFS. Es la sub-banda más utilizada para WiFi.

- **UNII-2A (5.250–5.350 GHz):** Canales 52, 56, 60, 64. Potencia máxima de 250 mW (24 dBm) EIRP. **Requiere DFS** (Dynamic Frequency Selection) porque comparte espectro con sistemas de radar meteorológico y militar.

- **UNII-2C / UNII-2 Extended (5.470–5.725 GHz):** Canales 100 a 144 (con algunas exclusiones por región). Potencia máxima de 1 W (30 dBm) EIRP. **Requiere DFS y TPC** (Transmit Power Control). Proporciona la mayor cantidad de espectro, pero es la banda más afectada por radares.

- **UNII-3 (5.725–5.850 GHz):** Canales 149, 153, 157, 161, 165. Potencia máxima de 1 W (30 dBm) EIRP. No requiere DFS. Es popular en exteriores.

**Numeración de canales:** Los canales WiFi en 5 GHz se numeran según la fórmula:

$$f_c = 5000 + 5 \times n \quad \text{[MHz]}$$

donde $n$ es el número de canal y $f_c$ es la frecuencia central. Por ejemplo, el canal 36 tiene frecuencia central $f_c = 5000 + 5 \times 36 = 5180$ MHz.

**Channel Bonding (Agregación de Canales):**

Channel bonding es la técnica de combinar canales adyacentes de 20 MHz para formar un canal más ancho. En WiFi 5:

- **40 MHz:** Se combinan 2 canales de 20 MHz. Ejemplo: canales 36+40 forman un canal de 40 MHz centrado en 5190 MHz. Se designa como canal 38 (40 MHz).

- **80 MHz:** Se combinan 4 canales de 20 MHz. Ejemplo: canales 36+40+44+48 forman un canal de 80 MHz centrado en 5210 MHz. Se designa como canal 42 (80 MHz). En UNII-1, solo hay **un** canal de 80 MHz disponible.

- **160 MHz:** Se combinan 8 canales de 20 MHz. Ejemplo: canales 36+40+44+48+52+56+60+64 forman un canal de 160 MHz. Alternativamente, se puede usar **80+80 MHz**: dos canales de 80 MHz no contiguos (por ejemplo, canal 42 de 80 MHz en UNII-1 + canal 155 de 80 MHz en UNII-3), tratados lógicamente como un canal de 160 MHz.

En total, la banda de 5 GHz ofrece aproximadamente:
- **25** canales de 20 MHz (varía por región)
- **12** canales de 40 MHz no solapados
- **6** canales de 80 MHz no solapados
- **2** canales de 160 MHz contiguos (o más en 80+80)

**DFS (Dynamic Frequency Selection):**

DFS es un mecanismo regulatorio que obliga a los dispositivos WiFi a detectar señales de radar y evacuar el canal si se detecta un radar. El proceso funciona así:

1. **CAC (Channel Availability Check):** Antes de transmitir en un canal DFS, el AP debe escuchar durante **60 segundos** (o 600 segundos en canales de banda meteorológica) para verificar que no hay radar presente.

2. **In-Service Monitoring:** Durante la operación normal, el AP monitorea continuamente el canal. Si detecta un pulso de radar, debe cesar las transmisiones en **200 ms** y mover todas las STAs a un canal limpio.

3. **Non-Occupancy Period:** Después de detectar un radar, el AP no puede regresar al canal afectado durante al menos **30 minutos**.

DFS amplía significativamente el espectro utilizable en 5 GHz, pero introduce complejidad operativa y puede causar interrupciones breves cuando se detecta un radar (real o falso positivo).

**Descripción de Figura — Asignación de Canales en 5 GHz:**

> *La Figura 6.3 muestra el espectro de la banda de 5 GHz como una barra horizontal que abarca de 5.150 a 5.850 GHz. La barra está dividida en cuatro secciones coloreadas: UNII-1 (verde, 5.150–5.250 GHz, canales 36-48), UNII-2A (amarillo, 5.250–5.350 GHz, canales 52-64, etiquetada "DFS"), UNII-2C (naranja, 5.470–5.725 GHz, canales 100-144, etiquetada "DFS + TPC"), y UNII-3 (azul, 5.725–5.850 GHz, canales 149-165). Debajo de la barra, se muestran rectángulos superpuestos que ilustran el channel bonding: rectángulos estrechos de 20 MHz para canales individuales (36, 40, 44, 48...), rectángulos medianos de 40 MHz que engloban pares (36+40, 44+48...), rectángulos anchos de 80 MHz que engloban cuatro canales, y un rectángulo muy ancho de 160 MHz que cruza de UNII-1 a UNII-2A. Un ícono de radar con un símbolo de advertencia aparece sobre las bandas UNII-2A y UNII-2C.*

### 6.5 Link Budget WiFi 5

El **link budget** (presupuesto de enlace) es un cálculo que determina si una señal transmitida llegará al receptor con suficiente potencia para ser decodificada correctamente. Es fundamental para el diseño de cobertura de redes WiFi. La ecuación general del link budget es:

$$P_{RX} = P_{TX} + G_{TX} - L_{TX} - L_{\text{path}} + G_{RX} - L_{RX}$$

donde:
- $P_{RX}$: Potencia recibida [dBm]
- $P_{TX}$: Potencia transmitida [dBm]
- $G_{TX}$: Ganancia de la antena transmisora [dBi]
- $L_{TX}$: Pérdidas en el transmisor (cables, conectores) [dB]
- $L_{\text{path}}$: Pérdida de propagación en el trayecto [dB]
- $G_{RX}$: Ganancia de la antena receptora [dBi]
- $L_{RX}$: Pérdidas en el receptor [dB]

Para que el enlace funcione, se debe cumplir:

$$P_{RX} \geq S_{\min} + M_{\text{fade}}$$

donde $S_{\min}$ es la **sensibilidad del receptor** (la potencia mínima necesaria para decodificar la señal con una tasa de error aceptable) y $M_{\text{fade}}$ es un **margen de desvanecimiento** que protege contra fluctuaciones de la señal (típicamente 6–10 dB).

**Pérdida en espacio libre (FSPL) a 5 GHz:**

La pérdida de propagación en espacio libre se calcula con la ecuación de Friis:

$$L_{\text{FSPL}} = 20\log_{10}(d) + 20\log_{10}(f) + 32.44 \quad \text{[dB]}$$

donde $d$ es la distancia en km y $f$ es la frecuencia en MHz.

Para WiFi a 5 GHz (tomando 5.5 GHz = 5500 MHz), a una distancia de referencia de $d = 0.01$ km (10 metros):

$$L_{\text{FSPL}} = 20\log_{10}(0.01) + 20\log_{10}(5500) + 32.44$$

$$= -40 + 74.81 + 32.44 = 67.25 \, \text{dB}$$

**Ejemplo numérico completo — Link Budget WiFi 5 (Interior):**

Diseñemos el enlace descendente para un AP WiFi 5 en un entorno de oficina interior.

*Datos del transmisor (AP):*
- $P_{TX} = 20$ dBm (100 mW, potencia típica de AP indoor)
- $G_{TX} = 5$ dBi (antena omnidireccional con ganancia moderada)
- $L_{TX} = 1$ dB (pérdidas internas)
- Beamforming: ganancia adicional de $G_{\text{BF}} = 3$ dB (AP 2×2)

*Datos del receptor (STA — laptop):*
- $G_{RX} = 2$ dBi (antena integrada)
- $L_{RX} = 0$ dB
- Sensibilidad para MCS 9, 80 MHz: $S_{\min} = -57$ dBm
- Sensibilidad para MCS 7, 80 MHz: $S_{\min} = -66$ dBm
- Sensibilidad para MCS 0, 80 MHz: $S_{\min} = -82$ dBm

*Margen de desvanecimiento:* $M_{\text{fade}} = 8$ dB

*Modelo de propagación interior:* Para un entorno de oficina, usamos un modelo de pérdida logarítmica:

$$L_{\text{path}}(d) = L_0 + 10 \cdot n \cdot \log_{10}\left(\frac{d}{d_0}\right) + \sum L_{\text{pared}}$$

donde $L_0 = 67.25$ dB es la pérdida a $d_0 = 10$ m (calculada arriba), $n = 3.5$ es el exponente de pérdida en interior, y $\sum L_{\text{pared}}$ son las pérdidas adicionales por paredes.

*Cálculo — ¿A qué distancia máxima funciona MCS 9 (256-QAM, 866.7 Mbps)?*

Potencia recibida necesaria:

$$P_{RX, \min} = S_{\min} + M_{\text{fade}} = -57 + 8 = -49 \, \text{dBm}$$

Pérdida máxima permitida:

$$L_{\text{path, máx}} = P_{TX} + G_{TX} - L_{TX} + G_{\text{BF}} + G_{RX} - L_{RX} - P_{RX, \min}$$

$$L_{\text{path, máx}} = 20 + 5 - 1 + 3 + 2 - 0 - (-49) = 78 \, \text{dB}$$

Distancia máxima (sin paredes):

$$78 = 67.25 + 10 \times 3.5 \times \log_{10}\left(\frac{d}{10}\right)$$

$$10.75 = 35 \times \log_{10}\left(\frac{d}{10}\right)$$

$$\log_{10}\left(\frac{d}{10}\right) = 0.307$$

$$\frac{d}{10} = 10^{0.307} = 2.03$$

$$\boxed{d_{\max} \approx 20.3 \, \text{m} \quad \text{(MCS 9, 256-QAM, sin paredes)}}$$

Si añadimos 2 paredes de yeso ($L_{\text{pared}} = 3$ dB cada una, total 6 dB):

$$L_{\text{path, máx}} = 78 - 6 = 72 \, \text{dB}$$

$$72 = 67.25 + 35 \times \log_{10}\left(\frac{d}{10}\right)$$

$$\log_{10}\left(\frac{d}{10}\right) = \frac{4.75}{35} = 0.136$$

$$d = 10 \times 10^{0.136} = 10 \times 1.37 = 13.7 \, \text{m}$$

Para **MCS 0** (BPSK, mayor alcance, $S_{\min} = -82$ dBm):

$$P_{RX, \min} = -82 + 8 = -74 \, \text{dBm}$$

$$L_{\text{path, máx}} = 20 + 5 - 1 + 3 + 2 - 0 - (-74) = 103 \, \text{dB}$$

$$103 = 67.25 + 35 \times \log_{10}\left(\frac{d}{10}\right)$$

$$\log_{10}\left(\frac{d}{10}\right) = \frac{35.75}{35} = 1.021$$

$$d = 10 \times 10^{1.021} = 10 \times 10.5 = 105 \, \text{m}$$

$$\boxed{d_{\max} \approx 105 \, \text{m} \quad \text{(MCS 0, BPSK, sin paredes)}}$$

Este resultado muestra la adaptación de velocidad en WiFi 5: cerca del AP (< 20 m) se puede disfrutar de velocidades de 866 Mbps con 256-QAM, mientras que a distancias mayores el sistema reduce automáticamente la modulación, sacrificando velocidad a cambio de mayor alcance y confiabilidad, hasta llegar a cobertura básica (~105 m con BPSK, pero a solo unos pocos Mbps).

---

## 7. WiFi 6 (IEEE 802.11ax)

### 7.1 Motivaciones y Contexto

WiFi 6, formalmente definido por la enmienda **IEEE 802.11ax**, fue aprobado en febrero de 2021 (aunque la certificación Wi-Fi Alliance comenzó en septiembre de 2020). A diferencia de generaciones anteriores que se enfocaban en incrementar la velocidad máxima individual, WiFi 6 fue diseñado con una filosofía fundamentalmente diferente: **mejorar la eficiencia de la red en entornos densos**.

**El problema de las redes densas:** El número de dispositivos WiFi por hogar pasó de un promedio de 5 en 2015 a más de 15 en 2020, y se proyectan más de 25 para 2025. En entornos como estadios, aeropuertos, centros de convenciones y campus universitarios, miles de dispositivos compiten por el mismo espectro. En estos escenarios, la velocidad máxima teórica del estándar es irrelevante; lo que importa es el **rendimiento por usuario**, la **latencia** y la **equidad** en el acceso al medio.

**El cambio de paradigma:** WiFi 5 buscaba maximizar la velocidad pico ($R_{\text{pico}}$), pero en redes densas el rendimiento efectivo por usuario es:

$$R_{\text{usuario}} = \frac{R_{\text{pico}} \times \eta_{\text{MAC}}}{N_{\text{usuarios}}}$$

donde $\eta_{\text{MAC}}$ es la eficiencia de la capa MAC (típicamente 50–70% en WiFi 5 debido al overhead de contención y headers) y $N_{\text{usuarios}}$ es el número de usuarios activos. WiFi 6 ataca tanto el numerador (incrementando $R_{\text{pico}}$ y $\eta_{\text{MAC}}$) como el denominador conceptual, permitiendo servir a múltiples usuarios **simultáneamente** en el dominio de frecuencia (OFDMA) además del dominio espacial (MU-MIMO).

**El problema de la superposición de BSS (BSS overlap):** En despliegues densos, múltiples APs operan en los mismos canales. En WiFi 5, cuando una STA detecta cualquier trama WiFi (incluso de un BSS vecino) con potencia superior al umbral de detección de energía (Energy Detection, $-62$ dBm) o al umbral de detección de preámbulo ($-82$ dBm), debe diferir su transmisión. Esto crea un efecto de "zona muerta" donde la interferencia de BSSs vecinos impide que las STAs de un BSS dado accedan al medio, aunque la señal de su propio AP sea fuerte. WiFi 6 aborda este problema con **BSS Coloring** (Sección 7.5).

### 7.2 OFDMA (Orthogonal Frequency Division Multiple Access)

#### Explicación detallada de OFDMA vs OFDM

**OFDM** (Orthogonal Frequency Division Multiplexing), utilizado en WiFi 4 y WiFi 5, divide el canal en múltiples subportadoras ortogonales. Sin embargo, en cada instante de transmisión (símbolo OFDM), **todas las subportadoras se asignan a un único usuario**. Si el AP necesita enviar datos a 4 usuarios, debe servir a cada uno secuencialmente, uno tras otro, en el dominio del tiempo. Esto introduce latencia y overhead por la contención de acceso al medio para cada transmisión individual.

**OFDMA** (Orthogonal Frequency Division Multiple Access), introducido en WiFi 6, permite dividir las subportadoras en grupos llamados **Resource Units (RUs)** y asignar diferentes RUs a diferentes usuarios **simultáneamente** dentro del mismo símbolo OFDM. De esta forma, múltiples usuarios transmiten (o reciben) datos al mismo tiempo, compartiendo el canal en el dominio de la frecuencia.

**Analogía pedagógica — La autopista:**

Imagine OFDM como una autopista de 4 carriles donde solo un vehículo puede circular a la vez, aunque sea muy pequeño y solo necesite un carril: la autopista completa se reserva para cada vehículo en su turno. OFDMA convierte esa autopista en una carretera donde los carriles se asignan independientemente: un camión puede usar 2 carriles mientras dos motocicletas usan un carril cada una, todos circulando simultáneamente. Para paquetes pequeños (confirmaciones de IoT, mensajes cortos), OFDMA es dramáticamente más eficiente porque evita desperdiciar el ancho de canal completo para una transmisión mínima.

#### Resource Units (RUs)

Las subportadoras de un canal se agrupan en **Resource Units (RUs)** de varios tamaños:

| RU | Subportadoras de datos | Subportadoras totales | Ancho aprox. |
|:---:|:---:|:---:|:---:|
| 26-tone RU | 24 | 26 | ~2 MHz |
| 52-tone RU | 48 | 52 | ~4 MHz |
| 106-tone RU | 102 | 106 | ~8 MHz |
| 242-tone RU | 234 | 242 | ~20 MHz |
| 484-tone RU | 468 | 484 | ~40 MHz |
| 996-tone RU | 980 | 996 | ~80 MHz |

El número y tipo de RUs disponibles depende del ancho del canal:

- **20 MHz (242 tonos totales):** Se puede dividir en:
  - 1 × RU-242 (1 usuario, ancho completo), o
  - 2 × RU-106 + 1 × RU-26, o
  - 4 × RU-52 + 1 × RU-26, o
  - 9 × RU-26, o
  - otras combinaciones válidas.

- **40 MHz (484 tonos totales):** Hasta 18 × RU-26 o 1 × RU-484.

- **80 MHz (996 tonos totales):** Hasta 37 × RU-26 o 1 × RU-996.

- **160 MHz (2×996 tonos totales):** Hasta 74 × RU-26 o 2 × RU-996.

#### Uplink y Downlink OFDMA

Una innovación clave de WiFi 6 es que OFDMA funciona tanto en **downlink** (DL) como en **uplink** (UL).

- **DL-OFDMA:** El AP divide su transmisión en RUs y envía datos a múltiples STAs simultáneamente. El AP controla completamente la asignación de RUs.

- **UL-OFDMA:** El AP envía una **Trigger Frame** (trama de activación) que indica a cada STA en qué RU debe transmitir y con qué parámetros (potencia, MCS). Las STAs transmiten simultáneamente en sus RUs asignados, de forma coordinada. Esto es revolucionario porque el uplink en WiFi siempre había sido gobernado exclusivamente por contención (CSMA/CA); ahora el AP puede programar el acceso de las STAs, evitando colisiones y mejorando la eficiencia.

#### Ejemplo numérico — Eficiencia de OFDMA

Considere un escenario con un AP WiFi 6 y 9 dispositivos IoT, cada uno con un paquete pequeño de 100 bytes para enviar. El canal es de 20 MHz.

**Sin OFDMA (WiFi 5 / OFDM):**

Cada dispositivo debe esperar su turno. Asumiendo un overhead MAC de $T_{\text{overhead}} = 200 \, \mu\text{s}$ (incluye DIFS, backoff, preámbulo, ACK, SIFS) y un tiempo de transmisión de datos de $T_{\text{datos}} = 50 \, \mu\text{s}$ por paquete:

$$T_{\text{total, OFDM}} = 9 \times (T_{\text{overhead}} + T_{\text{datos}}) = 9 \times 250 = 2{,}250 \, \mu\text{s}$$

Eficiencia:

$$\eta_{\text{OFDM}} = \frac{9 \times T_{\text{datos}}}{T_{\text{total}}} = \frac{9 \times 50}{2{,}250} = 20\%$$

**Con UL-OFDMA (WiFi 6):**

El AP envía una Trigger Frame ($T_{\text{TF}} \approx 100 \, \mu\text{s}$) que asigna un RU-26 a cada dispositivo. Los 9 dispositivos transmiten simultáneamente, cada uno en su RU de 26 tonos. Como los RUs son $\approx 1/9$ del canal de 20 MHz, la transmisión tarda $T_{\text{datos, RU}} = 50 \times 9 = 450 \, \mu\text{s}$ (misma cantidad de datos, pero en un ancho de banda 9 veces menor, por lo que tarda 9 veces más). Sin embargo, solo hay **un** evento de contención y overhead:

$$T_{\text{total, OFDMA}} = T_{\text{overhead}} + T_{\text{TF}} + T_{\text{datos, RU}} = 200 + 100 + 450 = 750 \, \mu\text{s}$$

Eficiencia:

$$\eta_{\text{OFDMA}} = \frac{9 \times T_{\text{datos}}}{T_{\text{total}}} = \frac{9 \times 50}{750} = 60\%$$

$$\boxed{\text{Mejora de eficiencia: } \frac{60\%}{20\%} = 3\times}$$

**Descripción de Figura — OFDM vs OFDMA:**

> *La Figura 7.1 compara OFDM (WiFi 5) con OFDMA (WiFi 6) mediante dos diagramas de tiempo-frecuencia. En el diagrama superior (OFDM), el eje horizontal representa el tiempo y el vertical la frecuencia (subportadoras). En cada intervalo de tiempo, todo el ancho del canal (representado como un bloque rectangular ancho) se asigna a un solo usuario, coloreado de un color distinto: azul para Usuario 1 en el intervalo $t_1$, rojo para Usuario 2 en $t_2$, verde para Usuario 3 en $t_3$, y amarillo para Usuario 4 en $t_4$. Los usuarios se atienden secuencialmente, y entre cada bloque hay un espacio gris que representa el overhead de contención (DIFS + backoff). En el diagrama inferior (OFDMA), en un único intervalo de tiempo $t_1$, el canal se divide verticalmente en 4 Resource Units: las subportadoras inferiores (RU-1, azul) para Usuario 1, las siguientes (RU-2, rojo) para Usuario 2, las siguientes (RU-3, verde) para Usuario 3, y las superiores (RU-4, amarillo) para Usuario 4. Los cuatro usuarios transmiten simultáneamente, y solo hay un overhead de contención. Una flecha indica que el tiempo total en OFDMA es significativamente menor.*

### 7.3 1024-QAM

WiFi 6 introduce la modulación **1024-QAM**, que corresponde a los niveles MCS 10 y MCS 11 del estándar 802.11ax.

**Constelación 1024-QAM:** La constelación es una cuadrícula de $32 \times 32 = 1{,}024$ puntos en el plano I-Q. Cada símbolo codifica:

$$b = \log_2(1024) = 10 \, \text{bits/símbolo}$$

Comparación directa con 256-QAM ($\log_2(256) = 8$ bits/símbolo):

$$\text{Mejora} = \frac{10 - 8}{8} \times 100\% = 25\%$$

Esto significa un incremento del 25% en la eficiencia espectral respecto a WiFi 5, para la misma configuración de canal y MIMO.

**Requisitos de SNR:** La distancia mínima entre puntos adyacentes en una constelación $M$-QAM normalizada (energía promedio unitaria) es:

$$d_{\min} = \sqrt{\frac{6}{M - 1}}$$

Para 256-QAM: $d_{\min} = \sqrt{6/255} = 0.153$

Para 1024-QAM: $d_{\min} = \sqrt{6/1023} = 0.0766$

La distancia mínima se reduce a la mitad, lo que significa que el receptor necesita distinguir entre puntos mucho más cercanos. En la práctica, 1024-QAM requiere un SNR de al menos **35 dB** (comparado con ~30 dB para 256-QAM y ~24 dB para 64-QAM).

**¿Cuándo es práctico usar 1024-QAM?** Solo en condiciones de canal excelentes: distancias cortas (< 5-10 m del AP), sin obstrucciones, con mínima interferencia, y con dispositivos de alta calidad que tengan bajo ruido de fase y alta linealidad en la cadena de RF. En un entorno de oficina típico, 1024-QAM podría estar disponible solo en las posiciones más cercanas al AP. Según mediciones de campo, 1024-QAM típicamente solo puede utilizarse en el 10-20% del área de cobertura de un BSS, dependiendo de la densidad de usuarios y el entorno.

**Descripción de Figura — Constelaciones QAM:**

> *La Figura 7.2 muestra tres constelaciones QAM en diagramas I-Q de igual escala para facilitar la comparación visual. A la izquierda, la constelación 64-QAM (WiFi 4/5) con 8×8 = 64 puntos azules bien separados entre sí; la etiqueta "6 bits/símbolo" aparece debajo. En el centro, la constelación 256-QAM (WiFi 5) con 16×16 = 256 puntos verdes más densamente empaquetados; etiqueta "8 bits/símbolo". A la derecha, la constelación 1024-QAM (WiFi 6) con 32×32 = 1024 puntos rojos extremadamente densos, casi formando un cuadrado sólido; etiqueta "10 bits/símbolo". Debajo de las tres constelaciones, un gráfico de barras muestra el SNR requerido: ~24 dB (64-QAM), ~30 dB (256-QAM), ~35 dB (1024-QAM). Líneas punteadas conectan cada barra con su constelación correspondiente. Una nota señala: "Mayor eficiencia → Mayor requisito de SNR → Menor alcance".*

### 7.4 MU-MIMO Bidireccional

WiFi 6 expande significativamente las capacidades MU-MIMO respecto a WiFi 5:

| Característica | WiFi 5 (802.11ac) | WiFi 6 (802.11ax) |
|:---|:---:|:---:|
| Flujos espaciales máx. | 8 | 8 |
| MU-MIMO Downlink | Sí (hasta 4 usuarios) | Sí (hasta 8 usuarios) |
| MU-MIMO Uplink | No | Sí (hasta 8 usuarios) |
| Máx. usuarios MU-MIMO simultáneos | 4 (solo DL) | 8 (DL) + 8 (UL) |

**MU-MIMO en Uplink (UL MU-MIMO):** Esta es una innovación significativa. En WiFi 5, el uplink siempre era SU-MIMO: solo una STA podía transmitir al AP en cada instante. En WiFi 6, el AP puede recibir transmisiones simultáneas de hasta 8 STAs, cada una en diferentes flujos espaciales. El AP coordina la transmisión UL MU-MIMO mediante **Trigger Frames**, similar al UL-OFDMA. De hecho, WiFi 6 permite combinar **UL-OFDMA con UL MU-MIMO**: diferentes RUs pueden ser asignados a diferentes usuarios, y dentro de un mismo RU, múltiples usuarios pueden transmitir usando MU-MIMO.

**Multiplexación espacial:** En un sistema MU-MIMO con $N_t$ antenas en el transmisor (AP) y $K$ usuarios con $N_{r,k}$ antenas cada uno, la capacidad suma se puede acotar por:

$$C_{\text{sum}} = \sum_{k=1}^{K} \log_2 \det\left(\mathbf{I} + \text{SNR}_k \cdot \mathbf{H}_k \mathbf{W}_k \mathbf{W}_k^H \mathbf{H}_k^H\right)$$

donde $\mathbf{H}_k$ es la matriz de canal del usuario $k$ y $\mathbf{W}_k$ es la matriz de precodificación asignada al usuario $k$. Para que MU-MIMO funcione eficientemente, los canales de los usuarios deben ser **suficientemente ortogonales** (decorrelados) en el dominio espacial.

**Beamforming mejorado:** WiFi 6 añade feedback comprimido más eficiente para el sondeo de canal MU-MIMO, reduciendo el overhead de sounding en escenarios con muchos usuarios.

### 7.5 BSS Coloring

#### Problema: Interferencia inter-BSS

En redes WiFi densas, múltiples APs (BSSs) operan frecuentemente en el mismo canal. En WiFi 5 y anteriores, el mecanismo de acceso al medio trata a **todas** las señales WiFi detectadas por encima del umbral de detección como una razón para diferir la transmisión, sin distinguir si la señal proviene de su propio BSS o de un BSS vecino. Esto se denomina **problema de OBSS** (Overlapping BSS) y resulta en:

- Diferimientos innecesarios cuando la señal interfiriente es de un BSS lejano que no causa interferencia real.
- Reducción significativa del throughput (hasta 40-50% en escenarios densos).
- Inequidad en el acceso al medio.

#### Solución: BSS Color de 6 bits

WiFi 6 asigna un **identificador de color de 6 bits** (0–63) a cada BSS. Este color se incluye en el campo **HE-SIG-A** del preámbulo de todas las tramas 802.11ax, lo que permite a cualquier dispositivo identificar a qué BSS pertenece una trama **antes de decodificar completamente el encabezado**.

Cuando una STA o AP detecta una trama con un color **diferente** al de su propio BSS (inter-BSS), puede aplicar un umbral de detección más alto (**OBSS/PD threshold**, ajustable hasta $-62$ dBm) en lugar del umbral estándar de $-82$ dBm. Esto significa que si la señal inter-BSS es débil (pero superior a $-82$ dBm), la STA puede **ignorarla y transmitir simultáneamente**, realizando reutilización espacial del canal.

El ajuste del umbral OBSS/PD está regulado por una relación con la potencia de transmisión:

$$\text{OBSS/PD}_{\text{máx}} = \max\left(-82 \, \text{dBm}, \min\left(-62 \, \text{dBm}, -82 + (P_{TX, \text{ref}} - P_{TX})\right)\right)$$

donde $P_{TX, \text{ref}} = 21$ dBm y $P_{TX}$ es la potencia de transmisión actual del dispositivo. Esto garantiza que un dispositivo que transmite con mayor potencia no use un umbral demasiado agresivo que pudiera causar interferencia excesiva.

#### Ejemplo de BSS Coloring

Considere 3 APs (AP₁, AP₂, AP₃) operando en el mismo canal de 80 MHz, con colores BSS = 1, 2, 3 respectivamente. La STA₁ está asociada a AP₁ (color 1).

**Sin BSS Coloring (WiFi 5):**
STA₁ detecta tramas de AP₂ a $-75$ dBm (superior al umbral de $-82$ dBm). STA₁ difiere su transmisión, aunque la señal de AP₂ no interfiere significativamente con la recepción de AP₁ (cuya señal es de $-50$ dBm, resultando en un SIR de $-50 - (-75) = 25$ dB, más que suficiente para decodificar).

**Con BSS Coloring (WiFi 6):**
STA₁ detecta el color 2 en la trama de AP₂ → identifica que es una trama inter-BSS. Aplica el umbral OBSS/PD de $-72$ dBm (valor ajustado). Como la señal de AP₂ es $-75$ dBm $<$ $-72$ dBm, STA₁ **ignora la trama y procede a transmitir**. Resultado: reutilización espacial exitosa, mejorando el throughput hasta un 20-30%.

**Descripción de Figura — BSS Coloring:**

> *La Figura 7.3 ilustra el mecanismo de BSS Coloring. Se muestran tres BSSs superpuestos: BSS₁ (AP₁ en el centro-izquierda, color rojo, etiqueta "Color=1"), BSS₂ (AP₂ en el centro, color azul, etiqueta "Color=2") y BSS₃ (AP₃ en la derecha, color verde, etiqueta "Color=3"). Los círculos de cobertura se superponen significativamente. En la zona de superposición entre BSS₁ y BSS₂, una STA₁ (asociada a AP₁) detecta tramas de ambos APs. En la parte superior, un diagrama temporal muestra el comportamiento sin BSS Coloring: STA₁ detecta la trama de AP₂, marca el canal como ocupado (barra gris "DEFER") y no puede transmitir. En la parte inferior, con BSS Coloring: STA₁ detecta el color 2 en la trama de AP₂, lo compara con su color (1), determina que es inter-BSS, verifica que la potencia ($-75$ dBm) está por debajo del umbral OBSS/PD ($-72$ dBm), e inmediatamente transmite su propia trama (barra verde "TX"). El resultado se etiqueta como "Reutilización Espacial Exitosa".*

### 7.6 Target Wake Time (TWT)

**Target Wake Time (TWT)** es un mecanismo de ahorro de energía introducido en WiFi 6, especialmente diseñado para dispositivos IoT (sensores, cámaras, dispositivos de domótica) que transmiten datos de forma infrecuente y necesitan maximizar la duración de la batería.

**Mecanismo de negociación:** Cada STA negocia con el AP un **programa de despertares** (wake schedule):

1. La STA envía una **TWT Request** indicando sus preferencias: intervalo entre despertares ($T_{\text{TWT}}$), duración del periodo activo ($T_{\text{wake}}$), y si el acuerdo es individual o de difusión.

2. El AP responde con una **TWT Response** confirmando o ajustando los parámetros.

3. A partir de ese momento, la STA puede entrar en modo **doze** (dormida) durante los intervalos entre sus TWT sessions, apagando completamente su radio WiFi. Solo despierta en los instantes programados.

**Cálculo del ciclo de trabajo y ahorro de energía:**

El ciclo de trabajo (duty cycle) de un dispositivo con TWT es:

$$D = \frac{T_{\text{wake}}}{T_{\text{TWT}}}$$

donde $T_{\text{wake}}$ es la duración del periodo activo y $T_{\text{TWT}}$ es el intervalo entre despertares.

El consumo promedio de potencia es:

$$P_{\text{avg}} = D \times P_{\text{active}} + (1 - D) \times P_{\text{sleep}}$$

donde $P_{\text{active}}$ es el consumo en modo activo (transmitiendo/recibiendo) y $P_{\text{sleep}}$ es el consumo en modo dormido.

**Ejemplo numérico — Sensor de temperatura IoT:**

Un sensor de temperatura envía una lectura de 50 bytes cada 10 minutos.

Parámetros TWT:
- $T_{\text{TWT}} = 600 \, \text{s}$ (10 minutos)
- $T_{\text{wake}} = 0.05 \, \text{s}$ (50 ms: tiempo para despertar, transmitir 50 bytes, recibir ACK)
- $P_{\text{active}} = 300 \, \text{mW}$ (consumo típico del radio WiFi activo)
- $P_{\text{sleep}} = 0.01 \, \text{mW}$ (consumo del microcontrolador en modo deep sleep)

Ciclo de trabajo:

$$D = \frac{0.05}{600} = 8.33 \times 10^{-5} = 0.00833\%$$

Consumo promedio:

$$P_{\text{avg}} = 8.33 \times 10^{-5} \times 300 + (1 - 8.33 \times 10^{-5}) \times 0.01$$

$$= 0.025 + 0.01 = 0.035 \, \text{mW}$$

**Sin TWT** (modo legacy PSM, despertando cada beacon a 100 ms):

$$D_{\text{legacy}} = \frac{T_{\text{wake, listen}}}{T_{\text{beacon}}} = \frac{0.005}{0.1} = 5\%$$

$$P_{\text{avg, legacy}} = 0.05 \times 100 + 0.95 \times 0.01 = 5.01 \, \text{mW}$$

Nota: en modo legacy PSM, el dispositivo despierta brevemente para escuchar cada beacon (5 ms cada 100 ms), con consumo de ~100 mW en modo de escucha (menor que transmisión).

**Mejora en duración de batería:**

Suponga una batería de 1000 mAh a 3.3 V (energía = 3.3 Wh = 3300 mWh):

- Con TWT: $\text{Duración} = \frac{3300}{0.035} = 94{,}286 \, \text{h} \approx 10.8 \, \text{años}$
- Sin TWT (PSM): $\text{Duración} = \frac{3300}{5.01} = 659 \, \text{h} \approx 27 \, \text{días}$

$$\boxed{\text{Mejora: } \frac{10.8 \, \text{años}}{27 \, \text{días}} \approx 146\times}$$

### 7.7 Cálculo de Velocidad PHY WiFi 6

WiFi 6 modifica los parámetros del símbolo OFDM para mejorar la eficiencia en entornos multipath densos:

**Cambios en el símbolo OFDM:**

| Parámetro | WiFi 5 (802.11ac) | WiFi 6 (802.11ax) |
|:---|:---:|:---:|
| Duración útil del símbolo ($T_{\text{FFT}}$) | 3.2 μs | **12.8 μs** (4× mayor) |
| Espaciado entre subportadoras ($\Delta f$) | 312.5 kHz | **78.125 kHz** (4× menor) |
| Opciones de GI | 0.4 μs, 0.8 μs | **0.8 μs, 1.6 μs, 3.2 μs** |
| Duración total del símbolo | 3.6 – 4.0 μs | **13.6 – 16.0 μs** |
| Subportadoras de datos (80 MHz) | 234 | **980** |

El espaciado entre subportadoras se calcula como:

$$\Delta f = \frac{1}{T_{\text{FFT}}} = \frac{1}{12.8 \times 10^{-6}} = 78{,}125 \, \text{Hz} = 78.125 \, \text{kHz}$$

¿Por qué un símbolo más largo? Un símbolo 4× más largo con subportadoras 4× más estrechas tiene ventajas en entornos densos:

1. **Mayor robustez al multipath:** El prefijo cíclico (GI) es proporcionalmente más corto respecto al símbolo útil, lo que mejora la eficiencia. En WiFi 5, el GI de 0.8 μs representa el 20% del símbolo (0.8/4.0). En WiFi 6, el GI de 0.8 μs representa solo el 5.9% (0.8/13.6).

2. **Mayor número de subportadoras por Hz:** Al estrechar las subportadoras, caben más en el mismo ancho de canal. Un canal de 80 MHz tiene $80{,}000/78.125 = 1024$ subportadoras en WiFi 6, frente a $80{,}000/312.5 = 256$ en WiFi 5. Descontando pilotos, DC y bandas de guarda, WiFi 6 tiene 980 subportadoras de datos vs 234 en WiFi 5 para 80 MHz. Sin embargo, la tasa por subportadora es 4× menor (porque el símbolo es 4× más largo), por lo que la velocidad neta por flujo es comparable (ligeramente mayor gracias al mayor número relativo de subportadoras de datos).

**Fórmula de velocidad PHY WiFi 6:**

$$R_{\text{PHY}} = N_{SS} \times N_{SD} \times b \times R_c \times \frac{1}{T_{\text{SYM}}}$$

La fórmula es la misma que WiFi 5, pero con valores actualizados.

**Ejemplo — Velocidad máxima WiFi 6 (configuración extrema):**

- $N_{SS} = 8$ (8 flujos espaciales)
- $N_{SD} = 1960$ (160 MHz: $2 \times 980$)
- $b = 10$ (1024-QAM, MCS 11)
- $R_c = 5/6$
- $T_{\text{SYM}} = 12.8 + 0.8 = 13.6 \, \mu\text{s}$ (GI de 0.8 μs)

$$R_{\text{PHY}} = 8 \times 1960 \times 10 \times \frac{5}{6} \times \frac{1}{13.6 \times 10^{-6}}$$

Paso a paso:

$$8 \times 1960 = 15{,}680$$

$$15{,}680 \times 10 = 156{,}800 \, \text{bits por símbolo}$$

$$156{,}800 \times \frac{5}{6} = 130{,}667 \, \text{bits de información por símbolo}$$

$$\frac{130{,}667}{13.6 \times 10^{-6}} = 9{,}607{,}843{,}137 \, \text{bps}$$

$$\boxed{R_{\text{PHY, máx WiFi 6}} = 9.6 \, \text{Gbps}}$$

**Tabla comparativa — Velocidad máxima WiFi 5 vs WiFi 6 (8×8, 160 MHz, GI mínimo):**

| Parámetro | WiFi 5 | WiFi 6 | Cambio |
|:---|:---:|:---:|:---:|
| Modulación máx. | 256-QAM (8 bits) | 1024-QAM (10 bits) | +25% |
| $N_{SD}$ (160 MHz) | 468 | 1960 | +4.19× |
| $T_{\text{SYM}}$ (GI mín.) | 3.6 μs | 13.6 μs | +3.78× |
| $N_{SD} / T_{\text{SYM}}$ | 130.0 kHz | 144.1 kHz | +10.8% |
| $R_c$ máx. | 5/6 | 5/6 | = |
| $R_{\text{PHY}}$ (1 SS) | 866.7 Mbps | 1201 Mbps | +38.6% |
| $R_{\text{PHY}}$ (8 SS) | 6.93 Gbps | 9.6 Gbps | +38.5% |

La mejora del 38.5% en velocidad PHY máxima proviene de dos factores: 25% por la mejora en modulación (1024-QAM vs 256-QAM) y ~10.8% por la mayor eficiencia espectral del nuevo diseño OFDM (más subportadoras de datos por Hz de ancho de banda).

---

## 8. WiFi 6E (IEEE 802.11ax en 6 GHz)

### 8.1 Espectro de 6 GHz

WiFi 6E no es un nuevo estándar PHY: utiliza exactamente la misma tecnología 802.11ax de WiFi 6. La "E" significa **Extended**, refiriéndose a la extensión del espectro operativo a la banda de **6 GHz** (5.925–7.125 GHz), que proporciona **1200 MHz** de espectro adicional para WiFi.

Para poner en perspectiva la magnitud de esta adición:
- La banda de 2.4 GHz ofrece ~83.5 MHz de espectro utilizable.
- La banda de 5 GHz ofrece ~500 MHz (varía por región, incluyendo canales DFS).
- La banda de 6 GHz añade **1200 MHz**, más que duplicando el espectro WiFi total disponible.

$$\text{Espectro total WiFi 6E} = 83.5 + 500 + 1200 = 1783.5 \, \text{MHz}$$

$$\text{Incremento} = \frac{1200}{83.5 + 500} \times 100\% = 205.6\%$$

**Panorama regulatorio:**

La disponibilidad de la banda de 6 GHz varía significativamente por región:

- **Estados Unidos (FCC):** Aprobó todo el rango de 5.925–7.125 GHz (1200 MHz) en abril de 2020 para uso sin licencia. Permite tanto uso interior (LPI — Low Power Indoor) como exterior (SP — Standard Power, con AFC).

- **Europa (CEPT/ETSI):** Inicialmente aprobó solo la parte baja, 5.925–6.425 GHz (500 MHz), exclusivamente para uso interior (LPI). La parte alta (6.425–7.125 GHz) está en proceso de evaluación regulatoria y hay presión de operadores móviles para asignarla a 5G/IMT.

- **Latinoamérica:** Brasil y México han adoptado regulaciones similares a la FCC (1200 MHz). Chile y Colombia han seguido parcialmente. Otros países siguen en proceso regulatorio.

- **Asia:** Corea del Sur aprobó los 1200 MHz. Japón autorizó la parte baja. China e India aún no han asignado espectro en 6 GHz para WiFi.

**AFC (Automated Frequency Coordination):**

Para operaciones de potencia estándar (SP) en exteriores, la FCC exige el uso de un sistema **AFC** (Coordinación Automática de Frecuencias). El AFC funciona como una base de datos central que:

1. El AP reporta su ubicación geográfica al servidor AFC.
2. El servidor AFC consulta una base de datos de sistemas incumbentes (enlaces fijos punto a punto, estaciones de TV por cable, satélites) que operan en la banda de 6 GHz.
3. El servidor responde al AP con una lista de canales y niveles de potencia permitidos en esa ubicación.
4. El AP solo puede operar en los canales y potencias autorizados por el AFC.

Este mecanismo permite proteger a los usuarios incumbentes del espectro de 6 GHz mientras maximiza el acceso para WiFi.

### 8.2 Canales Disponibles en 6 GHz

La banda de 6 GHz ofrece un número significativamente mayor de canales no solapados comparada con 5 GHz:

| Ancho de Canal | Canales en 5 GHz | Canales en 6 GHz | Incremento |
|:---:|:---:|:---:|:---:|
| 20 MHz | ~25 | **59** | +136% |
| 40 MHz | ~12 | **29** | +142% |
| 80 MHz | ~6 | **14** | +133% |
| 160 MHz | ~2 | **7** | +250% |

Estos números son particularmente impactantes para canales anchos:

- **7 canales de 160 MHz** sin solapamiento en 6 GHz, comparados con apenas 2 en 5 GHz. Esto significa que en un despliegue empresarial, se pueden tener 7 APs con 160 MHz cada uno sin interferencia mutua, lo cual era prácticamente imposible en 5 GHz.

- **14 canales de 80 MHz** permiten despliegues densos de alta capacidad donde cada AP opera en un canal limpio.

**Numeración de canales en 6 GHz:**

Los canales en 6 GHz comienzan en el canal **1** (frecuencia central 5.955 GHz para 20 MHz) y se incrementan en pasos de 4 para canales de 20 MHz:

$$f_c = 5950 + 5 \times n \quad \text{[MHz]}$$

donde $n$ es el número de canal. El primer canal de 20 MHz es $n = 1$ ($f_c = 5955$ MHz) y el último es $n = 233$ ($f_c = 7115$ MHz).

Para canales de 160 MHz, los canales centrales son: 15, 47, 79, 111, 143, 175, 207.

**Descriptive figure paragraph — Comparativa de espectro disponible:**

> *La Figura 8.1 presenta una comparación visual del espectro disponible en las tres bandas WiFi. En la parte superior, la banda de 2.4 GHz se muestra como una barra estrecha (83.5 MHz) con solo 3 canales no solapados de 20 MHz (1, 6, 11), coloreados en rojo, verde y azul. En el medio, la banda de 5 GHz se muestra como una barra más ancha (~500 MHz) con sus canales de 20 MHz agrupados por sub-bandas UNII, algunos marcados como "DFS". Se indican 6 canales de 80 MHz y 2 de 160 MHz no solapados. En la parte inferior, la banda de 6 GHz se muestra como una barra muy ancha (1200 MHz) que es visualmente mayor que las otras dos combinadas. Los 14 canales de 80 MHz se muestran como rectángulos verdes no solapados, y los 7 canales de 160 MHz como rectángulos azules. Debajo, un gráfico de barras resume: 2.4 GHz = 83.5 MHz (3 canales 20 MHz), 5 GHz ≈ 500 MHz (6 canales 80 MHz), 6 GHz = 1200 MHz (14 canales 80 MHz). Un diagrama circular muestra que 6 GHz representa el 67% del espectro WiFi total.*

### 8.3 Beneficios de WiFi 6E

#### Despliegue Greenfield (Sin dispositivos legacy)

Uno de los beneficios más significativos de WiFi 6E no es tecnológico sino operativo: la banda de 6 GHz es un **espacio limpio** donde solo dispositivos WiFi 6E (o posteriores) pueden operar. No existen dispositivos legacy (WiFi 4, WiFi 5, etc.) en 6 GHz.

¿Por qué es esto tan importante? En las bandas de 2.4 y 5 GHz, los APs WiFi 6 deben mantener compatibilidad hacia atrás con dispositivos antiguos. Esto implica:

- **Transmisión de tramas de protección** (CTS-to-Self, RTS/CTS) para que dispositivos legacy entiendan las duraciones de transmisión.
- **Reducción del ancho de canal** cuando dispositivos legacy se conectan a canales anchos.
- **Uso de modulaciones inferiores** para los tramas de management y control.
- **Imposibilidad de usar OFDMA** o BSS Coloring con dispositivos que no soportan 802.11ax.

En 6 GHz, al ser 100% WiFi 6E/7, el AP puede:
- Usar OFDMA en todas las transmisiones.
- Utilizar el ancho de canal completo sin restricciones.
- Eliminar tramas de protección legacy.
- Operar con la máxima eficiencia MAC posible.

Mediciones de campo han mostrado que un AP WiFi 6 en 5 GHz con una mezcla de clientes legacy puede perder 20-30% de eficiencia comparado con el mismo AP en 6 GHz donde todos los clientes son WiFi 6E.

#### Reducción de Interferencia

La amplia disponibilidad de canales en 6 GHz reduce drásticamente la probabilidad de co-canal interference (CCI). En un despliegue empresarial típico con 20 APs:

- En 5 GHz (6 canales de 80 MHz): Factor de reuso = $\lceil 20/6 \rceil = 4$, es decir, al menos 4 APs comparten cada canal.
- En 6 GHz (14 canales de 80 MHz): Factor de reuso = $\lceil 20/14 \rceil = 2$, o incluso 1 si se usan los 14 canales.

La reducción de co-channel APs por canal mejora directamente la capacidad de la red, ya que el throughput en un canal compartido se degrada aproximadamente como:

$$R_{\text{efectivo}} \approx \frac{R_{\text{máx}}}{N_{\text{APs/canal}}}$$

#### Más Canales No Solapados para Canales Anchos

WiFi 5 y 6 soportan canales de 160 MHz, pero en 5 GHz solo hay 2 canales contiguos de 160 MHz, y uno de ellos cruza bandas DFS. En 6 GHz, los **7 canales de 160 MHz** sin solapamiento hacen que el uso de 160 MHz sea práctico para despliegues reales, multiplicando el throughput por AP.

#### Misma PHY que WiFi 6 pero en espectro más limpio

Las velocidades PHY de WiFi 6E son idénticas a WiFi 6 (mismo 802.11ax), por lo que la velocidad máxima sigue siendo 9.6 Gbps con la configuración más agresiva. La ventaja está en que estas velocidades son más **alcanzables en la práctica** gracias al espectro más limpio y la ausencia de dispositivos legacy.

### 8.4 Consideraciones de Propagación en 6 GHz

#### Mayor pérdida de trayecto a 6 GHz vs 5 GHz

La pérdida de propagación en espacio libre es proporcional al cuadrado de la frecuencia. Comparando 6 GHz con 5 GHz:

$$\Delta L = 20\log_{10}\left(\frac{f_{6\text{GHz}}}{f_{5\text{GHz}}}\right) = 20\log_{10}\left(\frac{6500}{5500}\right) = 20\log_{10}(1.182) = 1.45 \, \text{dB}$$

Tomando frecuencias centrales de cada banda (5.5 GHz vs 6.5 GHz), la pérdida adicional es de aproximadamente **1.45 dB** en espacio libre. Este valor es relativamente modesto, pero la situación empeora significativamente en entornos interiores.

#### Pérdidas de penetración en paredes

Las pérdidas de penetración a través de materiales de construcción aumentan con la frecuencia. Valores típicos comparativos:

| Material | 5 GHz | 6 GHz | Diferencia |
|:---|:---:|:---:|:---:|
| Pared de yeso (drywall) | 3–4 dB | 4–5 dB | +1 dB |
| Pared de ladrillo | 8–10 dB | 10–13 dB | +2–3 dB |
| Concreto (15 cm) | 15–20 dB | 18–25 dB | +3–5 dB |
| Vidrio estándar | 4–6 dB | 5–8 dB | +1–2 dB |
| Vidrio Low-E | 25–30 dB | 28–35 dB | +3–5 dB |
| Piso/techo (concreto) | 18–22 dB | 22–28 dB | +4–6 dB |

Estos incrementos acumulativos pueden ser significativos en edificios con múltiples paredes entre el AP y la STA.

#### Implicaciones de cobertura

La combinación de mayor FSPL y mayores pérdidas por materiales resulta en un **área de cobertura menor** para WiFi 6E comparado con WiFi 6 en 5 GHz, para la misma potencia de transmisión y sensibilidad del receptor.

#### Ejemplo numérico — Comparación de cobertura 5 GHz vs 6 GHz

Comparemos el radio de cobertura de un AP en 5 GHz vs 6 GHz, para una configuración MCS 7 (64-QAM, 2/3) en 80 MHz con 2 flujos espaciales.

**Parámetros comunes:**
- $P_{TX} = 20$ dBm
- $G_{TX} = 5$ dBi
- $G_{RX} = 2$ dBi
- $L_{TX} + L_{RX} = 1$ dB
- $G_{\text{BF}} = 3$ dB
- $M_{\text{fade}} = 8$ dB
- Sensibilidad MCS 7: $S_{\min} = -66$ dBm (asumida igual en ambas bandas)
- Exponente de propagación: $n = 3.0$ (interior típico)
- Sin paredes adicionales (línea de vista interior)

**EIRP efectiva:** $P_{TX} + G_{TX} - L_{TX} + G_{\text{BF}} + G_{RX} = 20 + 5 - 1 + 3 + 2 = 29$ dBm

**Potencia mínima requerida:** $P_{RX, \min} = S_{\min} + M_{\text{fade}} = -66 + 8 = -58$ dBm

**Pérdida máxima:** $L_{\text{máx}} = 29 - (-58) = 87$ dB

**A 5.5 GHz:**

$$L_0 = 20\log_{10}(0.01) + 20\log_{10}(5500) + 32.44 = -40 + 74.81 + 32.44 = 67.25 \, \text{dB}$$

$$87 = 67.25 + 10 \times 3.0 \times \log_{10}\left(\frac{d}{10}\right)$$

$$\log_{10}\left(\frac{d}{10}\right) = \frac{19.75}{30} = 0.658$$

$$d_{5\text{GHz}} = 10 \times 10^{0.658} = 10 \times 4.55 = 45.5 \, \text{m}$$

**A 6.5 GHz:**

$$L_0 = 20\log_{10}(0.01) + 20\log_{10}(6500) + 32.44 = -40 + 76.26 + 32.44 = 68.70 \, \text{dB}$$

$$87 = 68.70 + 30 \times \log_{10}\left(\frac{d}{10}\right)$$

$$\log_{10}\left(\frac{d}{10}\right) = \frac{18.30}{30} = 0.610$$

$$d_{6\text{GHz}} = 10 \times 10^{0.610} = 10 \times 4.07 = 40.7 \, \text{m}$$

**Comparación:**

$$\frac{d_{6\text{GHz}}}{d_{5\text{GHz}}} = \frac{40.7}{45.5} = 0.895$$

$$\boxed{\text{El radio de cobertura a 6 GHz es aproximadamente 10.5\% menor que a 5 GHz}}$$

En términos de **área** de cobertura (proporcional a $d^2$):

$$\frac{A_{6\text{GHz}}}{A_{5\text{GHz}}} = \left(\frac{40.7}{45.5}\right)^2 = 0.80$$

$$\boxed{\text{El área de cobertura a 6 GHz es aproximadamente 20\% menor que a 5 GHz}}$$

Esta reducción del 20% en área significa que un despliegue WiFi 6E requerirá **más APs** para cubrir la misma superficie que un despliegue WiFi 6 en 5 GHz. Sin embargo, dado que 6 GHz ofrece muchos más canales, el costo adicional de más APs se compensa con la mayor capacidad y menor interferencia.

Si añadimos paredes (por ejemplo, 2 paredes de ladrillo con pérdida de 10 dB a 5 GHz y 13 dB a 6 GHz), la diferencia se amplifica:

- $d_{5\text{GHz}}$ (con 2 paredes a 10 dB): $L_{\text{máx}} = 87 - 20 = 67$ dB → $d = 10^{(67 - 67.25)/30 + 1} \times 10 = 9.94$ m
- $d_{6\text{GHz}}$ (con 2 paredes a 13 dB): $L_{\text{máx}} = 87 - 26 = 61$ dB → $d = 10^{(61 - 68.70)/30 + 1} \times 10 = 5.57$ m

$$\frac{d_{6\text{GHz}}}{d_{5\text{GHz}}} = \frac{5.57}{9.94} = 0.56$$

Con paredes gruesas, el alcance a 6 GHz puede reducirse al **56%** del alcance a 5 GHz, lo que implica la necesidad de aproximadamente **3.2× más APs** para cubrir la misma área. Esto resalta la importancia de una planificación cuidadosa del despliegue WiFi 6E, especialmente en edificios con materiales de construcción densos.

---

## Referencias

[1] IEEE Computer Society, "IEEE Standard for Information Technology—Telecommunications and Information Exchange between Systems—Local and Metropolitan Area Networks—Specific Requirements—Part 11: Wireless LAN Medium Access Control (MAC) and Physical Layer (PHY) Specifications," *IEEE Std 802.11-2020*, Feb. 2021. DOI: [10.1109/IEEESTD.2021.9363693](https://doi.org/10.1109/IEEESTD.2021.9363693)

[2] IEEE Computer Society, "IEEE Standard for Information Technology—Telecommunications and Information Exchange between Systems—Local and Metropolitan Area Networks—Specific Requirements—Amendment 4: Enhancements for Very High Throughput for Operation in Bands below 6 GHz," *IEEE Std 802.11ac-2013*, Dec. 2013. DOI: [10.1109/IEEESTD.2013.6687187](https://doi.org/10.1109/IEEESTD.2013.6687187)

[3] IEEE Computer Society, "IEEE Standard for Information Technology—Telecommunications and Information Exchange between Systems—Local and Metropolitan Area Networks—Specific Requirements—Amendment 1: Enhancements for High-Efficiency WLAN," *IEEE Std 802.11ax-2021*, May 2021. DOI: [10.1109/IEEESTD.2021.9442429](https://doi.org/10.1109/IEEESTD.2021.9442429)

[4] E. Khorov, A. Kiryanov, A. Lyakhov, and G. Bianchi, "A Tutorial on IEEE 802.11ax High Efficiency WLANs," *IEEE Communications Surveys & Tutorials*, vol. 21, no. 1, pp. 197–216, First Quarter 2019. DOI: [10.1109/COMST.2018.2871099](https://doi.org/10.1109/COMST.2018.2871099)

[5] B. Bellalta, "IEEE 802.11ax: High-Efficiency WLANs," *IEEE Wireless Communications*, vol. 23, no. 1, pp. 38–46, Feb. 2016. DOI: [10.1109/MWC.2016.7422404](https://doi.org/10.1109/MWC.2016.7422404)

[6] D. López-Pérez, A. Garcia-Rodriguez, L. Galati-Giordano, M. Kasslin, and K. Doppler, "IEEE 802.11be Extremely High Throughput: The Next Generation of Wi-Fi Technology Beyond 802.11ax," *IEEE Communications Magazine*, vol. 57, no. 9, pp. 113–119, Sep. 2019. DOI: [10.1109/MCOM.001.1900338](https://doi.org/10.1109/MCOM.001.1900338)

[7] M. S. Afaqui, E. Garcia-Villegas, and E. Lopez-Aguilera, "IEEE 802.11ax: Challenges and Requirements for Future High Efficiency WiFi," *IEEE Wireless Communications*, vol. 24, no. 3, pp. 130–137, Jun. 2017. DOI: [10.1109/MWC.2016.1600089WC](https://doi.org/10.1109/MWC.2016.1600089WC)

[8] Wi-Fi Alliance, "Wi-Fi 6E: The Next Great Chapter in Wi-Fi," White Paper, 2021. Disponible en: [https://www.wi-fi.org/discover-wi-fi/wi-fi-6e](https://www.wi-fi.org/discover-wi-fi/wi-fi-6e)

[9] Federal Communications Commission (FCC), "Unlicensed Use of the 6 GHz Band," *Report and Order and Further Notice of Proposed Rulemaking*, ET Docket No. 18-295, Apr. 2020.

[10] A. Goldsmith, *Wireless Communications*, Cambridge University Press, 2005. ISBN: 978-0521837163.

[11] T. S. Rappaport, *Wireless Communications: Principles and Practice*, 2nd ed., Prentice Hall, 2002. ISBN: 978-0130422323.
