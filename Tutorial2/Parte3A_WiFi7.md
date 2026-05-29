# Tutorial de Redes Inalámbricas — Parte 3A: WiFi 7 (IEEE 802.11be)

**Autor:** Tutorial Pedagógico de Telecomunicaciones  
**Nivel:** Introductorio–Intermedio  
**Prerrequisitos:** Parte 1 — Fundamentos de Propagación y Comunicaciones Inalámbricas; Parte 2 — WiFi 5, WiFi 6 y WiFi 6E

---

## 9. WiFi 7: IEEE 802.11be — Extremely High Throughput (EHT)

WiFi 7, formalmente **IEEE 802.11be**, es la evolución natural de WiFi 6/6E y fue diseñado con una idea central: no basta con aumentar la velocidad pico; también hay que reducir la latencia, mejorar la predictibilidad del retardo y aprovechar el espectro de manera más flexible [1]–[6]. Por eso, el nombre técnico de la enmienda es **Extremely High Throughput (EHT)**: la ambición ya no es solo “alta eficiencia” como en 802.11ax, sino **caudal extremadamente alto**.

Desde un punto de vista práctico, WiFi 7 busca servir aplicaciones que combinan tres exigencias simultáneas:

1. **Mucho caudal** (por ejemplo, video 8K, transferencia masiva de datos, renderizado remoto).
2. **Poca latencia** (realidad aumentada/virtual, juegos en la nube, control industrial).
3. **Gran fiabilidad bajo carga** (oficinas densas, campus, fábricas, hogares con muchos dispositivos).

A lo largo de esta sección estudiaremos sus mecanismos principales con una perspectiva pedagógica, pero sin perder rigor matemático.

### 9.1 Motivación y Contexto de WiFi 7

#### 9.1.1 ¿Por qué hizo falta WiFi 7?

WiFi 6 y WiFi 6E resolvieron muchos problemas de eficiencia en entornos densos mediante **OFDMA**, **MU-MIMO uplink/downlink**, **1024-QAM** y el uso de la banda de **6 GHz**. Sin embargo, seguían existiendo cuatro limitaciones importantes:

- **Ancho de canal máximo limitado a 160 MHz.** Para aplicaciones multi-gigabit, 160 MHz puede resultar insuficiente.
- **Un solo enlace lógico principal por asociación.** Aunque un dispositivo sea tribanda, tradicionalmente una sesión de datos se apoya sobre un enlace principal, con cambios de banda relativamente rígidos.
- **Latencia variable.** En un medio compartido, las colas MAC, la contención y la interferencia generan jitter.
- **Capacidad limitada para flujos inmersivos y sincronizados.** Aplicaciones como AR/VR no solo requieren muchos Mbps, sino que además exigen retardos pequeños y estables.

Un modo simple de ver la presión de tráfico moderna es sumar demandas concurrentes. Si en un hogar u oficina pequeña hay varias aplicaciones activas, el caudal agregado puede estimarse como

$$
R_{\text{agregado}} = \sum_{i=1}^{K} R_i
$$

donde $R_i$ es la tasa requerida por la aplicación $i$ y $K$ es el número de aplicaciones activas al mismo tiempo.

Esta ecuación parece trivial, pero es importante pedagógicamente: en redes reales, el cuello de botella aparece cuando muchas aplicaciones coinciden. Por ejemplo, si una vivienda tiene simultáneamente:

- dos flujos de video 4K/8K comprimidos de $80\ \text{Mbps}$ cada uno,
- una sesión de VR de $400\ \text{Mbps}$,
- un juego en la nube de $35\ \text{Mbps}$,
- y tráfico IoT, copias en la nube y señalización por $25\ \text{Mbps}$,

entonces

$$
R_{\text{agregado}} = 80 + 80 + 400 + 35 + 25 = 620\ \text{Mbps}
$$

El resultado, $620\ \text{Mbps}$, no parece extremo para WiFi 6. El problema es que ese valor representa solo el **caudal medio agregado**. Si además se exige latencia sub-5 ms y estabilidad temporal, la red necesita margen adicional para retransmisiones, overhead MAC, contención y variaciones instantáneas del canal. WiFi 7 nace precisamente para ofrecer ese margen.

#### 9.1.2 Aplicaciones impulsoras

Las aplicaciones que más han empujado el desarrollo de WiFi 7 son:

- **AR/VR/XR:** muy sensibles a latencia y jitter. Una imagen que llega tarde no solo degrada calidad: puede generar mareo o mala experiencia de usuario.
- **Streaming 8K y video volumétrico:** demandan caudales sostenidos altos.
- **Cloud gaming:** combina tráfico constante con exigencia fuerte de retardo extremo a extremo.
- **Industrial IoT y automatización:** requieren comunicaciones predecibles y robustas, no solo “rápidas” en promedio.
- **Transporte inalámbrico local (backhaul/fronthaul):** en oficinas y hogares avanzados se usan enlaces WiFi para distribuir tráfico multi-gigabit dentro del edificio.

#### 9.1.3 Línea temporal y proceso de normalización

El proceso de estandarización de 802.11be puede resumirse así [1]–[4]:

- **2018–2019:** se consolida la idea de una nueva evolución más allá de 802.11ax; se forma el grupo de trabajo **TGbe**.
- **2021:** aparecen borradores tempranos que ya incluyen MLO, 320 MHz y 4096-QAM.
- **2022:** el borrador **IEEE P802.11be/D3.0** refleja una versión bastante madura de la especificación [2].
- **2024:** se publica la enmienda final **IEEE Std 802.11be-2024** [1].

Desde el punto de vista académico, es útil recordar una regla: **la industria comercializa chipsets y APs antes de la publicación final del estándar**, apoyándose en borradores avanzados. Por eso existen productos “WiFi 7” previos a la edición definitiva del estándar.

#### 9.1.4 Objetivos de desempeño

Aunque el rendimiento real siempre depende del número de usuarios, del canal y del dispositivo, los objetivos de diseño asociados a WiFi 7 suelen resumirse así [3]–[6]:

- **Caudal pico PHY superior a 40 Gbps** en configuraciones extremas.
- **Latencia de acceso muy baja**, con objetivos prácticos del orden de **menos de 5 ms** para ciertas aplicaciones y arquitecturas locales.
- **Mayor fiabilidad** mediante agregación/selección entre múltiples enlaces.

---

### 9.2 Arquitectura y Características Fundamentales de WiFi 7

Las cuatro novedades más emblemáticas de WiFi 7 son:

1. **Multi-Link Operation (MLO)**
2. **Canales de 320 MHz**
3. **4096-QAM (4K-QAM)**
4. **Hasta 16 flujos espaciales**

A continuación se estudia cada una.

#### 9.2.1 Multi-Link Operation (MLO)

La idea de MLO es conceptualmente muy poderosa: un dispositivo ya no se ve como un único enlace WiFi, sino como un **conjunto coordinado de enlaces** que pueden operar en **2.4 GHz, 5 GHz y 6 GHz** [1], [3], [4].

Si un dispositivo dispone de $L$ enlaces simultáneos, el caudal agregado ideal puede modelarse como

$$
R_{\text{MLO}} = \sum_{\ell=1}^{L} R_{\ell}
$$

donde $R_{\ell}$ es la tasa de transmisión del enlace $\ell$.

**Explicación detallada de la ecuación:**

- El símbolo $L$ representa cuántos enlaces físicos están activos y coordinados.
- Cada término $R_{\ell}$ representa la tasa de un enlace individual; por ejemplo, uno en 5 GHz y otro en 6 GHz.
- La suma expresa que, en el caso ideal, la capacidad total es la adición de todas las capacidades individuales.
- El calificativo “ideal” es importante: en la práctica hay overhead de coordinación, colas, contención y límites del hardware.

Para modelar ese overhead de manera sencilla, se introduce una eficiencia por enlace $\alpha_{\ell}$ con $0 < \alpha_{\ell} \leq 1$:

$$
R_{\text{MLO,ef}} = \sum_{\ell=1}^{L} \alpha_{\ell} R_{\ell}
$$

Aquí, $\alpha_{\ell}$ recoge pérdidas por cabeceras MAC, tiempos muertos, coordinación entre radios y retransmisiones. Si $\alpha_{\ell}=0.9$, significa que solo el 90% de la tasa PHY de ese enlace se convierte en rendimiento útil.

**Ejemplo numérico sencillo:**

Supongamos un equipo con tres enlaces:

- enlace 1 en 2.4 GHz con $R_1 = 0.6\ \text{Gbps}$,
- enlace 2 en 5 GHz con $R_2 = 2.4\ \text{Gbps}$,
- enlace 3 en 6 GHz con $R_3 = 5.8\ \text{Gbps}$.

En el caso ideal:

$$
R_{\text{MLO}} = 0.6 + 2.4 + 5.8 = 8.8\ \text{Gbps}
$$

Si tomamos eficiencias $\alpha_1 = 0.80$, $\alpha_2 = 0.88$ y $\alpha_3 = 0.90$,

$$
R_{\text{MLO,ef}} = 0.80\cdot0.6 + 0.88\cdot2.4 + 0.90\cdot5.8
$$

$$
R_{\text{MLO,ef}} = 0.48 + 2.112 + 5.22 = 7.812\ \text{Gbps}
$$

Es decir, el agregado realista sería aproximadamente **$7.81\ \text{Gbps}$**.

##### Modelo simple de reducción de latencia

MLO no solo sirve para sumar caudal; también puede **reducir la latencia** si un paquete se envía por el enlace más rápido disponible o incluso se duplica para que “gane” el primero que llegue.

Si el tiempo de servicio de cada enlace es una variable aleatoria $T_{\ell}$, y se usa el primer enlace que complete la transmisión, entonces el retardo efectivo es

$$
T_{\text{MLO}} = \min(T_1,T_2,\dots,T_L)
$$

Esta ecuación significa que el paquete “termina” cuando termina el enlace más rápido entre todos los enlaces candidatos. Matemáticamente, el mínimo de varias variables aleatorias suele ser menor que cada una por separado.

Si aproximamos cada tiempo de servicio como exponencial con tasa $\mu_{\ell} = 1/\bar T_{\ell}$, entonces

$$
\mathbb{E}[T_{\text{MLO}}] = \frac{1}{\sum_{\ell=1}^{L} \mu_{\ell}}
$$

donde $\bar T_{\ell}$ es el retardo medio del enlace $\ell$ y $\mathbb{E}[\cdot]$ representa el valor esperado.

**Ejemplo:** si dos enlaces tienen retardos medios de $\bar T_1 = 4\ \text{ms}$ y $\bar T_2 = 2.5\ \text{ms}$, entonces

$$
\mu_1 = \frac{1}{4} = 0.25\ \text{ms}^{-1}, \qquad \mu_2 = \frac{1}{2.5} = 0.4\ \text{ms}^{-1}
$$

por tanto,

$$
\mathbb{E}[T_{\text{MLO}}] = \frac{1}{0.25+0.4} = \frac{1}{0.65} \approx 1.54\ \text{ms}
$$

El resultado es muy instructivo: aunque ninguno de los enlaces por sí solo tenga $1.54\ \text{ms}$ de media, el uso coordinado de ambos sí puede aproximarse a ese valor en el modelo idealizado.

**Descripción de Figura — Arquitectura MLO y MLD:**

> *La Figura 9.1 debe mostrar, en el centro, un dispositivo cliente representado como un bloque grande etiquetado “MLD cliente”. Dentro del bloque aparecen tres radios o interfaces separadas: “Link 1: 2.4 GHz”, “Link 2: 5 GHz” y “Link 3: 6 GHz”. A la derecha se muestra un AP tribanda representado como “AP-MLD”, también con tres enlaces. En la parte superior del dibujo, una cola de paquetes de aplicación se divide mediante un planificador hacia los tres enlaces; algunas flechas sólidas representan reparto de carga y una flecha duplicada representa envío redundante de un paquete de baja latencia por dos enlaces a la vez. Debajo del esquema aparece una línea temporal con tres barras horizontales, una por enlace, donde se ve que el paquete entregado por el enlace más rápido determina el retardo final. La figura debe enfatizar visualmente que MLO no es simple itinerancia entre bandas, sino coordinación simultánea y consciente entre múltiples enlaces.*

#### 9.2.2 Canales de 320 MHz

La evolución de anchos de canal en WiFi puede resumirse así:

- WiFi 4: hasta 40 MHz
- WiFi 5: hasta 160 MHz
- WiFi 6/6E: hasta 160 MHz
- WiFi 7: hasta **320 MHz**

La relación básica entre capacidad y ancho de banda está dada por Shannon:

$$
C = B\log_2(1+\text{SNR})
$$

donde:

- $C$ es la capacidad teórica del canal en bits/s,
- $B$ es el ancho de banda en Hz,
- $\text{SNR}$ es la relación señal/ruido en forma lineal.

**Explicación detallada:**

- La fórmula indica que la capacidad crece linealmente con el ancho de banda $B$.
- También crece con la SNR, pero no linealmente, sino con un logaritmo base 2.
- Por eso, si la SNR se mantiene, **duplicar el ancho de banda** aproximadamente **duplica la capacidad**.

**Ejemplo numérico:** con $\text{SNR}=20\ \text{dB}$, primero se convierte a escala lineal:

$$
\text{SNR}_{\text{lin}} = 10^{20/10} = 100
$$

Entonces, para $B = 160\ \text{MHz}$,

$$
C_{160} = 160\times10^6\log_2(1+100)
$$

$$
C_{160} \approx 160\times10^6\times 6.658 = 1.065\times10^9\ \text{bps}
$$

Para $B = 320\ \text{MHz}$,

$$
C_{320} = 320\times10^6\log_2(101) \approx 2.130\times10^9\ \text{bps}
$$

Se observa que $C_{320} \approx 2C_{160}$. Esta es la razón fundamental por la que 320 MHz es tan relevante: incluso antes de hablar de MIMO o de 4096-QAM, el ancho de banda ya se ha duplicado.

##### Espaciado entre subportadoras y tamaño FFT

WiFi 6 y WiFi 7 usan un espaciado entre subportadoras de aproximadamente

$$
\Delta f = 78.125\ \text{kHz}
$$

Como en OFDM se cumple aproximadamente

$$
N_{\text{FFT}} \approx \frac{B}{\Delta f}
$$

para $B = 320\ \text{MHz}$ se obtiene

$$
N_{\text{FFT}} = \frac{320\times10^6}{78.125\times10^3} = 4096
$$

Esto justifica el uso de una **FFT de 4096 puntos**.

**Interpretación pedagógica:** una FFT mayor permite representar más subportadoras ortogonales dentro del mismo canal ancho. Eso aumenta el paralelismo en frecuencia y, por tanto, la cantidad de símbolos transmitidos en cada intervalo OFDM.

#### 9.2.3 4096-QAM (4K-QAM)

La modulación 4096-QAM usa una constelación de $4096$ símbolos. El número de bits por símbolo es

$$
\log_2(4096) = 12\ \text{bits/símbolo}
$$

Esta ecuación se explica así: si existen $M$ símbolos posibles, hacen falta $\log_2(M)$ bits para identificar uno de ellos. Como $4096 = 2^{12}$, cada símbolo transporta exactamente **12 bits**.

Para comparar con WiFi 6, que llega hasta 1024-QAM:

$$
\log_2(1024) = 10\ \text{bits/símbolo}
$$

La mejora relativa en bits por símbolo es

$$
\text{Ganancia} = \frac{12-10}{10}\times 100\% = 20\%
$$

Es decir, **4096-QAM ofrece un 20% más de bits por símbolo que 1024-QAM**, manteniendo todo lo demás constante.

##### Requisito de SNR

Un límite inferior teórico para la SNR puede estimarse a partir de Shannon. Si la eficiencia espectral objetivo es $\eta$ bits/s/Hz, entonces

$$
\eta = \log_2(1+\text{SNR}) \quad \Rightarrow \quad \text{SNR}_{\min} = 2^{\eta}-1
$$

Para 4096-QAM con tasa de codificación $R_c=5/6$, la eficiencia espectral bruta por subportadora puede aproximarse como

$$
\eta_{4096} = 12\cdot\frac{5}{6} = 10\ \text{bits/s/Hz}
$$

Por tanto, el límite ideal sería

$$
\text{SNR}_{\min,ideal} = 2^{10}-1 = 1023
$$

En decibelios,

$$
\text{SNR}_{\min,ideal,dB} = 10\log_{10}(1023) \approx 30.1\ \text{dB}
$$

Este valor **no** es la SNR práctica final, sino un límite teórico optimista. En sistemas reales hacen falta márgenes adicionales por imperfecciones de RF, sincronización, estimación de canal, EVM y no idealidad del decodificador. Por eso, en la práctica, 4096-QAM solo es viable en condiciones excelentes, típicamente muy cerca del AP.

**Ejemplo comparativo:** para 1024-QAM con $R_c=5/6$,

$$
\eta_{1024} = 10\cdot\frac{5}{6} = 8.33\ \text{bits/s/Hz}
$$

$$
\text{SNR}_{\min,ideal} = 2^{8.33}-1 \approx 321
$$

$$
10\log_{10}(321) \approx 25.1\ \text{dB}
$$

La diferencia ideal es de aproximadamente **$5\ \text{dB}$**, lo cual ya es significativa. En la práctica, la penalización puede ser aún mayor.

**Descripción de Figura — Constelación 1024-QAM vs 4096-QAM:**

> *La Figura 9.2 debe mostrar dos diagramas de constelación en el plano I-Q. A la izquierda, una cuadrícula de 32×32 puntos correspondiente a 1024-QAM; a la derecha, una cuadrícula de 64×64 puntos correspondiente a 4096-QAM. En ambos casos, los ejes horizontal y vertical deben etiquetarse como I (in-phase) y Q (quadrature). Una línea roja debe marcar la distancia mínima entre puntos adyacentes, mostrando visualmente que en 4096-QAM los puntos están mucho más apretados para la misma potencia media. Debajo de cada constelación debe aparecer un pequeño recuadro comparando “10 bits/símbolo” frente a “12 bits/símbolo” y una nota indicando que la mejora del 20% exige una calidad de canal mucho mayor. La figura debe transmitir la intuición de que el precio de meter más bits por símbolo es hacer la decisión del receptor mucho más delicada frente al ruido y a la distorsión.*

#### 9.2.4 Hasta 16 flujos espaciales

WiFi 7 amplía el número máximo de flujos espaciales hasta **16**, frente a los 8 de WiFi 5 y WiFi 6 [1], [3]–[6].

La expresión más general de la capacidad MIMO es

$$
C = B\log_2\det\left(\mathbf{I}_{N_r} + \frac{\rho}{N_t}\mathbf{H}\mathbf{H}^H\right)
$$

donde:

- $\mathbf{H}$ es la matriz de canal MIMO,
- $N_t$ es el número de antenas transmisoras,
- $N_r$ es el número de antenas receptoras,
- $\rho$ es la SNR total,
- $\mathbf{I}_{N_r}$ es la matriz identidad de dimensión $N_r$.

**Explicación pedagógica:** esta ecuación dice que la capacidad depende del rango y de los autovalores de la matriz de canal. Si el canal ofrece múltiples caminos suficientemente independientes, entonces pueden enviarse varios flujos paralelos a la vez.

En una simplificación ideal, si hay $N_{SS}$ flujos ortogonales con la misma SNR, puede aproximarse como

$$
C \approx N_{SS} B\log_2(1+\gamma)
$$

donde $\gamma$ es la SNR por flujo.

**Ejemplo numérico:** para $B=320\ \text{MHz}$ y $\gamma=20\ \text{dB}=100$,

- con $N_{SS}=8$:

$$
C_8 \approx 8\cdot320\times10^6\cdot\log_2(101) \approx 17.0\ \text{Gbps}
$$

- con $N_{SS}=16$:

$$
C_{16} \approx 16\cdot320\times10^6\cdot\log_2(101) \approx 34.1\ \text{Gbps}
$$

La duplicación de flujos espaciales **duplica la capacidad ideal**. Sin embargo, en la práctica solo se logra esta ganancia si el hardware, el canal y la correlación espacial lo permiten.

**Comparación histórica:**

- **WiFi 5:** hasta 8 SS
- **WiFi 6/6E:** hasta 8 SS
- **WiFi 7:** hasta 16 SS

---

### 9.3 Cálculo de Throughput Máximo Teórico de WiFi 7

La fórmula de velocidad PHY pedida en este tutorial es

$$
R = N_{SS} \times \frac{N_{SD}}{T_{\text{sym}}} \times \log_2(M) \times R_c
$$

donde:

- $N_{SS}$ = número de flujos espaciales,
- $N_{SD}$ = número de subportadoras de datos,
- $T_{\text{sym}}$ = duración del símbolo OFDM,
- $M$ = orden de modulación,
- $R_c$ = tasa de codificación.

#### 9.3.1 Significado físico de cada parámetro

- $\frac{N_{SD}}{T_{\text{sym}}}$ indica cuántas subportadoras de datos se transmiten por segundo.
- $\log_2(M)$ indica cuántos bits lleva cada símbolo QAM.
- $R_c$ corrige por redundancia de codificación; por ejemplo, $5/6$ significa que de cada 6 bits transmitidos, 5 son útiles.
- $N_{SS}$ multiplica el resultado por el número de flujos espaciales paralelos.

#### 9.3.2 Parámetros para el caso máximo WiFi 7

Tomamos la configuración extrema más citada para WiFi 7:

- $N_{SS}=16$
- $N_{SD}=3920$ para 320 MHz EHT
- $T_{\text{sym}} = 12.8\ \mu s + 0.8\ \mu s = 13.6\ \mu s$
- $M=4096 \Rightarrow \log_2(M)=12$
- $R_c = 5/6$

Sustituyendo en la fórmula:

$$
R = 16 \times \frac{3920}{13.6\times10^{-6}} \times 12 \times \frac{5}{6}
$$

Conviene agrupar primero los bits útiles por símbolo y por flujo espacial:

$$
3920 \times 12 = 47040\ \text{bits/símbolo bruto por flujo}
$$

Aplicando la codificación:

$$
47040\times\frac{5}{6} = 39200\ \text{bits útiles/símbolo por flujo}
$$

Ahora calculamos la tasa por flujo:

$$
R_{1\,SS} = \frac{39200}{13.6\times10^{-6}} \approx 2.882352941\times10^9\ \text{bps}
$$

es decir,

$$
R_{1\,SS} \approx 2.882\ \text{Gbps}
$$

Finalmente, con 16 flujos espaciales:

$$
R = 16\times 2.882\ \text{Gbps} \approx 46.12\ \text{Gbps}
$$

Por tanto,

$$
\boxed{R_{\text{WiFi 7, máx}} \approx 46.1\ \text{Gbps}}
$$

#### 9.3.3 ¿Por qué el resultado es tan alto?

Porque WiFi 7 combina **cuatro multiplicadores grandes** al mismo tiempo:

1. **320 MHz** de ancho de canal,
2. **3920** subportadoras de datos,
3. **12 bits por símbolo** con 4096-QAM,
4. **16 flujos espaciales**.

Si cualquiera de estos factores disminuye, la velocidad también disminuye proporcionalmente.

#### 9.3.4 Tabla comparativa con WiFi 5, 6 y 6E

| Generación | Configuración extrema de referencia | Fórmula resumida | Velocidad PHY máxima aproximada |
|---|---|---|---:|
| WiFi 5 | 8 SS, 160 MHz, 256-QAM, $R_c=5/6$, GI corto | $8\times468\times8\times\frac{5}{6}/3.6\mu s$ | $6.93\ \text{Gbps}$ |
| WiFi 6 | 8 SS, 160 MHz, 1024-QAM, $R_c=5/6$ | $8\times1960\times10\times\frac{5}{6}/13.6\mu s$ | $9.6\ \text{Gbps}$ |
| WiFi 6E | Igual a WiFi 6, pero en 6 GHz | misma expresión | $9.6\ \text{Gbps}$ |
| WiFi 7 | 16 SS, 320 MHz, 4096-QAM, $R_c=5/6$ | $16\times3920\times12\times\frac{5}{6}/13.6\mu s$ | $46.1\ \text{Gbps}$ |

**Observación importante:** esta tabla compara **tasas PHY máximas teóricas**. El rendimiento útil a nivel IP o aplicación siempre será menor por sobrecarga MAC/PHY, contención, ACKs, cabeceras, colisiones y variabilidad del canal.

---

### 9.4 Multi-Link Operation (MLO) — Análisis Detallado

MLO es probablemente la característica más transformadora de WiFi 7 porque cambia la forma de pensar el enlace inalámbrico: ya no es “una estación asociada a una banda”, sino “un dispositivo multi-enlace coordinado”.

#### 9.4.1 Concepto de MLD (Multi-Link Device)

Un **MLD** es una abstracción lógica que agrupa múltiples enlaces 802.11 bajo una entidad común [1], [2]. Puede tratarse de:

- un **AP-MLD**, o
- una **STA-MLD**.

El MLD comparte funciones de gestión, asociación y coordinación, mientras que cada enlace mantiene su propia PHY y su propia operación de canal.

Pedagógicamente, puede pensarse así:

- antes: **un dispositivo = un enlace principal**;
- ahora: **un dispositivo = una plataforma que coordina varios enlaces**.

#### 9.4.2 Tipos principales de MLO

##### a) STR — Simultaneous Transmit and Receive

En **STR**, el dispositivo puede transmitir y recibir simultáneamente en distintos enlaces, siempre que el hardware lo permita. Es el caso más potente, porque permite verdadero paralelismo.

##### b) NSTR — Non-Simultaneous Transmit and Receive

En **NSTR**, existen limitaciones de coexistencia interna, aislamiento RF o arquitectura del front-end, de modo que el dispositivo no puede transmitir y recibir libremente al mismo tiempo en todos los enlaces. Aun así, sigue habiendo coordinación multi-enlace, pero con restricciones de simultaneidad.

##### c) eMLSR — operación multi-enlace mejorada con radio único

En **eMLSR**, un único radio o una arquitectura con recursos RF compartidos puede conmutar o coordinar múltiples enlaces de forma mejorada, aunque no con el paralelismo completo de un STR puro. Es especialmente relevante para clientes de costo/consumo limitado.

#### 9.4.3 Modelo matemático de caudal agregado

En una forma un poco más realista que la de la Sección 9.2, el caudal agregado puede escribirse como

$$
R_{\text{agg}} = \sum_{\ell=1}^{L} p_{\ell}\,\alpha_{\ell}\,R_{\ell}
$$

donde:

- $p_{\ell}$ es la fracción del tráfico asignada al enlace $\ell$,
- $\alpha_{\ell}$ es la eficiencia MAC/PHY útil del enlace,
- $R_{\ell}$ es la tasa PHY nominal del enlace.

La condición natural es

$$
\sum_{\ell=1}^{L} p_{\ell} = 1
$$

si solo estamos repartiendo el tráfico total entre enlaces.

**Explicación:**

- Si $p_{\ell}$ es grande, significa que mucho tráfico usa ese enlace.
- Si $\alpha_{\ell}$ es bajo, ese enlace es ineficiente, quizá por contención o por mala calidad de canal.
- El producto $p_{\ell}\alpha_{\ell}R_{\ell}$ representa la contribución útil de cada enlace al total.

#### 9.4.4 Modelo de reducción de latencia

Para tráfico crítico, una estrategia frecuente es la duplicación selectiva. Si la probabilidad de éxito en un enlace es $p_{s,\ell}$ y se duplican paquetes sobre enlaces independientes, la probabilidad de que **al menos uno** llegue correctamente es

$$
P_{\text{éxito,dup}} = 1 - \prod_{\ell=1}^{L}(1-p_{s,\ell})
$$

**Interpretación:**

- $(1-p_{s,\ell})$ es la probabilidad de fallo del enlace $\ell$.
- El producto de todos los fallos es la probabilidad de que fallen todos a la vez.
- Restar ese valor a 1 da la probabilidad de éxito global.

**Ejemplo:** si dos enlaces tienen probabilidades de éxito $0.92$ y $0.95$,

$$
P_{\text{éxito,dup}} = 1 - (1-0.92)(1-0.95)
$$

$$
P_{\text{éxito,dup}} = 1 - (0.08)(0.05) = 1 - 0.004 = 0.996
$$

Es decir, la fiabilidad sube a **99.6%** para ese paquete duplicado.

#### 9.4.5 Ejemplo detallado: hogar con 3 enlaces simultáneos

Consideremos un AP-MLD y un cliente-MLD con estos enlaces:

- **2.4 GHz, 40 MHz, 2 SS, 1024-QAM, $R_c=5/6$**
- **5 GHz, 160 MHz, 2 SS, 4096-QAM, $R_c=5/6$**
- **6 GHz, 320 MHz, 2 SS, 4096-QAM, $R_c=5/6$**

Aproximaremos sus tasas PHY como:

- $R_{2.4} \approx 0.574\ \text{Gbps}$
- $R_{5} \approx 2.882\ \text{Gbps}$
- $R_{6} \approx 5.765\ \text{Gbps}$

Si las eficiencias útiles son $\alpha_{2.4}=0.75$, $\alpha_5=0.85$ y $\alpha_6=0.88$, y el planificador reparte el tráfico según $p_{2.4}=0.10$, $p_5=0.30$, $p_6=0.60$, entonces

$$
R_{\text{agg}} = 0.10\cdot0.75\cdot0.574 + 0.30\cdot0.85\cdot2.882 + 0.60\cdot0.88\cdot5.765
$$

$$
R_{\text{agg}} \approx 0.043 + 0.735 + 3.044 = 3.822\ \text{Gbps}
$$

Obsérvese que el caudal agregado útil es menor que la suma bruta porque el tráfico no se reparte uniformemente y porque hemos incluido eficiencia realista.

Ahora estudiemos latencia. Supongamos retardos medios:

- $\bar T_{2.4}=7\ \text{ms}$
- $\bar T_5=4\ \text{ms}$
- $\bar T_6=2.5\ \text{ms}$

Con duplicación para paquetes críticos:

$$
\mathbb{E}[T_{\min}] = \frac{1}{1/7 + 1/4 + 1/2.5}
$$

$$
\mathbb{E}[T_{\min}] = \frac{1}{0.1429 + 0.25 + 0.4} = \frac{1}{0.7929} \approx 1.26\ \text{ms}
$$

Esto no significa que toda la red opere siempre a $1.26\ \text{ms}$, pero sí muestra el potencial matemático de MLO para reducir el retardo de tráfico prioritario.

---

### 9.5 Preamble Puncturing en WiFi 7

#### 9.5.1 ¿Qué es?

**Preamble puncturing** es una técnica que permite usar un canal ancho aunque una parte pequeña del espectro esté ocupada o interferida. En vez de renunciar al canal completo de 320 MHz, el sistema “perfora” o excluye subcanales de 20 MHz o grupos equivalentes y sigue transmitiendo en el resto [1], [4], [6].

La intuición es muy importante: si una sola porción de 20 MHz está contaminada por interferencia, sería muy ineficiente descartar los 320 MHz completos. El puncturing permite conservar la mayor parte del ancho útil.

#### 9.5.2 Ancho efectivo

Si el canal nominal es $B_{\text{nom}}$ y se anulan $N_p$ subcanales de 20 MHz, una primera aproximación al ancho efectivo es

$$
B_{\text{ef}} = B_{\text{nom}} - 20\,N_p\ \text{MHz}
$$

**Explicación:**

- $B_{\text{nom}}$ es el ancho del canal completo, por ejemplo 320 MHz.
- Cada subcanal perforado resta 20 MHz.
- El modelo supone que la reducción del recurso espectral es lineal con el número de subcanales excluidos.

Si además suponemos que la tasa PHY escala aproximadamente con el ancho útil, entonces

$$
R_{\text{punct}} \approx R_{\text{nom}}\frac{B_{\text{ef}}}{B_{\text{nom}}}
$$

#### 9.5.3 Ejemplo: canal de 320 MHz con dos subcanales de 20 MHz perforados

Supongamos:

- $B_{\text{nom}}=320\ \text{MHz}$
- $N_p=2$
- $R_{\text{nom}} = 46.1\ \text{Gbps}$

Entonces,

$$
B_{\text{ef}} = 320 - 20\cdot2 = 280\ \text{MHz}
$$

La tasa aproximada sería

$$
R_{\text{punct}} \approx 46.1\cdot\frac{280}{320}
$$

$$
R_{\text{punct}} \approx 46.1\cdot0.875 = 40.34\ \text{Gbps}
$$

**Interpretación:** con dos perforaciones de 20 MHz, la pérdida teórica es solo del 12.5%, y la red aún conserva más de **40 Gbps** PHY en la configuración extrema. Si, en cambio, hubiera que reducir todo el canal a 160 MHz, el máximo teórico caería aproximadamente a la mitad.

**Descripción de Figura — Preamble puncturing en 320 MHz:**

> *La Figura 9.3 debe representar una barra horizontal de 320 MHz dividida en dieciséis bloques de 20 MHz. Dos de esos bloques, por ejemplo el quinto y el undécimo, deben aparecer en color rojo con una etiqueta “interferencia/incumbente”. Los demás bloques deben mostrarse en verde. Encima de la barra debe dibujarse un preámbulo EHT donde los bloques verdes se mantienen activos y los rojos aparecen marcados como anulados o excluidos. Debajo, una segunda línea debe comparar dos estrategias: “sin puncturing: retroceso a 160 MHz” frente a “con puncturing: 280 MHz efectivos”. La figura debe dejar claro que la innovación no consiste en eliminar la interferencia, sino en evitar que una pequeña porción inutilice el resto del canal ancho.*

---

### 9.6 OFDMA Mejorado en WiFi 7

WiFi 7 hereda la filosofía OFDMA de WiFi 6, pero la hace más flexible para escenarios de muy alta capacidad. Entre las novedades más importantes destacan [1], [5], [6]:

- soporte de **RUs más grandes**, hasta **$4\times 996$ tonos por RU**,
- **asignación Multi-RU** a un mismo usuario,
- planificación más flexible en canales muy anchos.

#### 9.6.1 Tamaños de Unidad de Recursos (RU)

En términos conceptuales, una **RU** es un subconjunto de subportadoras asignadas a un usuario dentro de un símbolo OFDMA. En EHT aparecen tamaños como:

- 26 tonos,
- 52 tonos,
- 106 tonos,
- 242 tonos,
- 484 tonos,
- 996 tonos,
- $2\times996$ tonos,
- $4\times996$ tonos.

La lógica es sencilla: usuarios con poca demanda reciben RUs pequeñas; usuarios con mucha demanda pueden recibir recursos grandes o múltiples RUs.

#### 9.6.2 Multi-RU allocation

En WiFi 6, un usuario estaba más limitado en cómo recibía recursos OFDMA. WiFi 7 permite que un mismo usuario reciba **varias RUs** dentro de la misma asignación. Esto reduce fragmentación espectral.

Podemos medir la eficiencia de asignación como

$$
\eta_{\text{alloc}} = \frac{N_{\text{útil}}}{N_{\text{asignado}}}
$$

donde:

- $N_{\text{útil}}$ es el número de tonos realmente necesarios o utilizados por el usuario,
- $N_{\text{asignado}}$ es el número de tonos que se le reservan.

**Ejemplo 1: usuario que necesita 726 tonos**

- Sin Multi-RU, podría recibir una RU de 996 tonos.
- Con Multi-RU, podría recibir $484 + 242 = 726$ tonos.

Sin Multi-RU:

$$
\eta_{\text{alloc, WiFi6}} = \frac{726}{996} \approx 0.729 = 72.9\%
$$

Con Multi-RU:

$$
\eta_{\text{alloc, WiFi7}} = \frac{726}{726} = 1 = 100\%
$$

Esto significa que la nueva flexibilidad evita desperdiciar aproximadamente un **27.1%** de los tonos reservados en este ejemplo.

#### 9.6.3 Ejemplo de ocupación en un canal EHT muy ancho

Supongamos un canal donde el planificador reparte recursos así:

- usuario A: $2\times996 = 1992$ tonos,
- usuario B: $996$ tonos,
- usuario C: $484$ tonos,
- usuario D: $484$ tonos.

Entonces el total asignado es

$$
N_{\text{ocupado}} = 1992 + 996 + 484 + 484 = 3956\ \text{tonos}
$$

Si la rejilla OFDMA disponible se aproxima como $4\times996 = 3984$ tonos, la ocupación relativa es

$$
\eta_{\text{rejilla}} = \frac{3956}{3984} \approx 0.993 = 99.3\%
$$

Este resultado ilustra que OFDMA en WiFi 7 puede aprovechar de manera extremadamente fina un canal de gran ancho.

---

### 9.7 Presupuesto de Enlace y Dimensionamiento de Cobertura WiFi 7

En esta sección nos centraremos en la banda de **6 GHz**, que es donde WiFi 7 explota mejor los canales de 320 MHz.

#### 9.7.1 Ecuación general del presupuesto de enlace

La ecuación básica del presupuesto de enlace es

$$
P_{RX} = P_{TX} + G_{TX} - L_{TX} - L_{\text{path}} + G_{RX} - L_{RX}
$$

donde:

- $P_{RX}$ es la potencia recibida en dBm,
- $P_{TX}$ es la potencia transmitida en dBm,
- $G_{TX}$ y $G_{RX}$ son las ganancias de antena en dBi,
- $L_{TX}$ y $L_{RX}$ son pérdidas internas,
- $L_{\text{path}}$ es la pérdida de propagación.

Para que el enlace funcione con un MCS dado, debe cumplirse

$$
P_{RX} \geq S_{\min} + M_{\text{fade}}
$$

donde $S_{\min}$ es la sensibilidad mínima del receptor y $M_{\text{fade}}$ es un margen de desvanecimiento, típicamente entre 6 y 10 dB.

#### 9.7.2 Cálculo de sensibilidad a partir del ruido térmico

Una forma de estimar la sensibilidad es

$$
S_{\min} = -174 + 10\log_{10}(B) + NF + \text{SNR}_{\min}
$$

donde:

- $-174\ \text{dBm/Hz}$ es la densidad espectral de ruido térmico a temperatura ambiente,
- $B$ es el ancho de banda en Hz,
- $NF$ es la figura de ruido del receptor en dB,
- $\text{SNR}_{\min}$ es la SNR mínima necesaria para el MCS considerado.

Tomemos $B=320\ \text{MHz}$ y $NF=7\ \text{dB}$.

Primero, el ruido térmico integrado sobre 320 MHz es

$$
N = -174 + 10\log_{10}(320\times10^6)
$$

$$
N = -174 + 85.05 = -88.95\ \text{dBm}
$$

Añadiendo la figura de ruido:

$$
N_{\text{eq}} = -88.95 + 7 = -81.95\ \text{dBm}
$$

Ahora obtenemos sensibilidades aproximadas para tres niveles de modulación:

1. **MCS bajo** (por ejemplo, BPSK con fuerte protección): $\text{SNR}_{\min}\approx 4\ \text{dB}$

$$
S_{\min, bajo} = -81.95 + 4 = -77.95\ \text{dBm}
$$

2. **MCS medio** (por ejemplo, 256-QAM/1024-QAM intermedio): $\text{SNR}_{\min}\approx 20\ \text{dB}$

$$
S_{\min, medio} = -81.95 + 20 = -61.95\ \text{dBm}
$$

3. **MCS alto** (por ejemplo, 4096-QAM, $R_c=5/6$): $\text{SNR}_{\min}\approx 33\ \text{dB}$

$$
S_{\min, alto} = -81.95 + 33 = -48.95\ \text{dBm}
$$

Estos valores son **estimaciones de ingeniería**, no cifras normativas exactas. Son útiles para dimensionamiento preliminar.

#### 9.7.3 Modelo de pérdida de propagación

Siguiendo el enfoque de la Parte 1 y usando un modelo de oficina interior basado en ITU-R P.1238 [7], la pérdida puede estimarse como

$$
L(d) = 20\log_{10}(f) + N\log_{10}(d) + L_f(n) - 28
$$

donde:

- $f$ está en MHz,
- $d$ está en metros,
- $N$ es el coeficiente de pérdida con la distancia,
- $L_f(n)$ es la pérdida adicional por pisos.

Para una oficina en la misma planta, tomamos:

- $f = 6100\ \text{MHz}$,
- $N = 31$,
- $L_f(n)=0$.

Entonces

$$
L(d) = 20\log_{10}(6100) + 31\log_{10}(d) - 28
$$

Como

$$
20\log_{10}(6100) \approx 75.71
$$

obtenemos

$$
L(d) \approx 47.71 + 31\log_{10}(d)
$$

#### 9.7.4 Ejemplo detallado: despliegue empresarial en 6 GHz

Supongamos un AP WiFi 7 indoor con:

- $P_{TX}=23\ \text{dBm}$,
- $G_{TX}=5\ \text{dBi}$,
- $L_{TX}=1\ \text{dB}$,
- cliente con $G_{RX}=2\ \text{dBi}$,
- $L_{RX}=0\ \text{dB}$,
- margen de desvanecimiento $M_{\text{fade}}=8\ \text{dB}$.

Entonces

$$
P_{RX} = 23 + 5 - 1 - L_{\text{path}} + 2 = 29 - L_{\text{path}}
$$

##### Caso A: MCS alto (4096-QAM)

Con $S_{\min,alto}=-48.95\ \text{dBm}$, la potencia requerida con margen es

$$
P_{RX,req} = -48.95 + 8 = -40.95\ \text{dBm}
$$

Por tanto, la pérdida máxima permitida es

$$
L_{\max} = 29 - (-40.95) = 69.95\ \text{dB}
$$

Igualando con el modelo ITU:

$$
69.95 = 47.71 + 31\log_{10}(d)
$$

$$
31\log_{10}(d) = 22.24
$$

$$
\log_{10}(d) = 0.717
$$

$$
d = 10^{0.717} \approx 5.21\ \text{m}
$$

**Conclusión:** 4096-QAM solo es razonable a distancias muy cortas en interior, del orden de **5 m** en este ejemplo.

##### Caso B: MCS medio

Con $S_{\min,medio}=-61.95\ \text{dBm}$,

$$
P_{RX,req} = -61.95 + 8 = -53.95\ \text{dBm}
$$

$$
L_{\max} = 29 - (-53.95) = 82.95\ \text{dB}
$$

Entonces

$$
82.95 = 47.71 + 31\log_{10}(d)
$$

$$
31\log_{10}(d) = 35.24
$$

$$
\log_{10}(d) = 1.137
$$

$$
d = 10^{1.137} \approx 13.71\ \text{m}
$$

**Conclusión:** para modulación media/alta más realista en celda empresarial, el radio útil está del orden de **12–14 m**.

##### Caso C: MCS robusto

Con $S_{\min,bajo}=-77.95\ \text{dBm}$,

$$
P_{RX,req} = -77.95 + 8 = -69.95\ \text{dBm}
$$

$$
L_{\max} = 29 - (-69.95) = 98.95\ \text{dB}
$$

De donde

$$
98.95 = 47.71 + 31\log_{10}(d)
$$

$$
31\log_{10}(d) = 51.24
$$

$$
\log_{10}(d) = 1.653
$$

$$
d = 10^{1.653} \approx 45.0\ \text{m}
$$

Esto muestra una lección fundamental de diseño: **la cobertura básica puede ser amplia, pero la cobertura para 4096-QAM es mucho más pequeña**. En WiFi 7, la red de 6 GHz suele diseñarse por capacidad y calidad, no solo por “llegar señal”.

#### 9.7.5 Consideraciones de planificación celular WiFi 7

Para dimensionar WiFi 7 en 6 GHz, conviene recordar:

- la banda de 6 GHz ofrece mucho espectro, pero **más pérdida de propagación** que 5 GHz y bastante más que 2.4 GHz;
- **320 MHz** es excelente para capacidad, pero exige muy buena calidad de canal;
- **4096-QAM** debe verse como un modo “de proximidad”; no como el MCS de borde de celda;
- en muchas redes empresariales, la capa de 6 GHz se diseña con celdas relativamente pequeñas, mientras 5 GHz y 2.4 GHz aportan respaldo y compatibilidad.

---

### 9.8 Ejemplo Integral de Dimensionamiento WiFi 7

Vamos a desarrollar un caso completo para un edificio de oficinas de **$5000\ \text{m}^2$**.

#### 9.8.1 Escenario de partida

Suposiciones de diseño:

- superficie total: $A_{\text{tot}} = 5000\ \text{m}^2$,
- ocupación máxima: 250 usuarios,
- usuarios activos simultáneos en hora cargada: 150,
- objetivo de diseño: al menos $100\ \text{Mbps}$ útiles por usuario activo,
- latencia objetivo para aplicaciones sensibles en LAN local: menor que $5\ \text{ms}$,
- APs tribanda WiFi 7 con MLO entre 5 GHz y 6 GHz,
- 2.4 GHz reservado sobre todo para IoT y legado.

#### 9.8.2 Dimensionamiento por capacidad

La demanda agregada objetivo es

$$
R_{\text{dem}} = N_{\text{act}}\times R_{\text{usuario}}
$$

donde $N_{\text{act}}=150$ y $R_{\text{usuario}}=100\ \text{Mbps}$.

Entonces

$$
R_{\text{dem}} = 150\times100\ \text{Mbps} = 15000\ \text{Mbps} = 15\ \text{Gbps}
$$

Supongamos que cada AP puede ofrecer, de forma conservadora y promediada en condiciones reales, unos

$$
R_{\text{AP,ef}} = 1.5\ \text{Gbps}
$$

útiles agregando 6 GHz y 5 GHz mediante MLO, después de overhead, reparto multiusuario y variación de MCS.

Entonces el número de APs por capacidad sería

$$
N_{\text{AP,cap}} = \frac{R_{\text{dem}}}{R_{\text{AP,ef}}} = \frac{15}{1.5} = 10
$$

Por capacidad, **10 APs** serían suficientes.

#### 9.8.3 Dimensionamiento por cobertura

Ahora usamos el resultado de la Sección 9.7. Para una cobertura 6 GHz razonable con MCS medio, adoptamos un radio útil de diseño más conservador que el teórico, por ejemplo

$$
r_{\text{diseño}} = 10\ \text{m}
$$

para contemplar paredes, mobiliario, cuerpos humanos y solapamiento entre celdas.

Si aproximamos el área efectiva cubierta por AP como

$$
A_{\text{celda,ef}} = 250\ \text{m}^2
$$

entonces

$$
N_{\text{AP,cov}} = \frac{A_{\text{tot}}}{A_{\text{celda,ef}}} = \frac{5000}{250} = 20
$$

Por cobertura hacen falta **20 APs**.

#### 9.8.4 Decisión final de número de APs

En diseño inalámbrico se toma el máximo entre el resultado por capacidad y el resultado por cobertura:

$$
N_{\text{AP}} = \max(N_{\text{AP,cap}}, N_{\text{AP,cov}})
$$

por tanto,

$$
N_{\text{AP}} = \max(10,20) = 20
$$

**Conclusión principal del ejemplo:** en este despliegue WiFi 7 de 6 GHz, la red queda **limitada por cobertura**, no por capacidad. Esto es muy típico en despliegues modernos de muy alta frecuencia/ancho de banda.

#### 9.8.5 Plan de canales con MLO

Propuesta pedagógica de canalización:

- **6 GHz:** usar **3 bloques de 320 MHz** no solapados, llamados A, B y C.
- **5 GHz:** usar **4 canales de 80 MHz** con reutilización espacial, llamados F1, F2, F3 y F4.
- **2.4 GHz:** canales 1, 6 y 11 para IoT/legado.

Cada AP anuncia un **MLD** con dos enlaces de alto rendimiento:

- **enlace principal de capacidad:** 6 GHz / 320 MHz,
- **enlace de soporte y continuidad:** 5 GHz / 80 MHz.

Una distribución posible para 20 APs en una malla 5×4 es:

- fila 1: A/F1, B/F2, C/F3, A/F4, B/F1
- fila 2: B/F2, C/F3, A/F4, B/F1, C/F2
- fila 3: C/F3, A/F4, B/F1, C/F2, A/F3
- fila 4: A/F4, B/F1, C/F2, A/F3, B/F4

La idea no es memorizar esta matriz, sino entender el principio: **se alternan bloques de 6 GHz y, simultáneamente, se desfasan los canales de 5 GHz** para que el MLO no agregue enlaces altamente correlacionados en interferencia.

#### 9.8.6 Throughput esperado por usuario

Si la demanda total en hora cargada es 15 Gbps y hay 150 usuarios activos, entonces el caudal objetivo medio por usuario ya es

$$
\bar R_{\text{usuario}} = \frac{15\ \text{Gbps}}{150} = 0.1\ \text{Gbps} = 100\ \text{Mbps}
$$

Como el despliegue final usa 20 APs, el número medio de usuarios activos por AP es

$$
N_{\text{act/AP}} = \frac{150}{20} = 7.5
$$

Si cada AP entrega de media $1.5\ \text{Gbps}$ útiles,

$$
\bar R_{\text{usuario,AP}} = \frac{1.5\ \text{Gbps}}{7.5} = 0.2\ \text{Gbps} = 200\ \text{Mbps}
$$

Este valor de **200 Mbps por usuario activo** representa una media razonable dentro de cada celda cuando la carga está balanceada. En condiciones favorables, usuarios cercanos al AP pueden observar picos muy superiores; en borde de celda o en horas de contención más fuerte, el valor será menor.

#### 9.8.7 Análisis de latencia

Supongamos que, para tráfico interactivo, el retardo medio de acceso por enlace es:

- en 6 GHz: $\bar T_6 = 2.4\ \text{ms}$,
- en 5 GHz: $\bar T_5 = 4.0\ \text{ms}$.

Con selección del primero disponible mediante MLO:

$$
\mathbb{E}[T_{\text{acc}}] = \frac{1}{1/2.4 + 1/4.0}
$$

$$
\mathbb{E}[T_{\text{acc}}] = \frac{1}{0.4167 + 0.25} = \frac{1}{0.6667} \approx 1.5\ \text{ms}
$$

Si añadimos aproximadamente:

- $1\ \text{ms}$ de LAN cableada/switching,
- $1\ \text{ms}$ de procesamiento local o servidor cercano,

entonces la latencia total aproximada sería

$$
T_{\text{e2e}} \approx 1.5 + 1 + 1 = 3.5\ \text{ms}
$$

que cumple holgadamente el objetivo de **menos de 5 ms** para servicios locales o de edge computing.

#### 9.8.8 Conclusiones del ejemplo integral

El ejercicio muestra varias lecciones muy importantes:

1. **WiFi 7 no debe dimensionarse solo por tasa pico.**
2. **En 6 GHz, muchas veces manda la cobertura antes que la capacidad.**
3. **MLO permite combinar una capa de alta capacidad (6 GHz) con otra de soporte/continuidad (5 GHz).**
4. **4096-QAM es excelente, pero solo en regiones cercanas al AP.**
5. **La promesa de baja latencia depende tanto del diseño de celdas como del uso inteligente de MLO.**

**Descripción de Figura — Plano conceptual de despliegue en oficina de 5000 m²:**

> *La Figura 9.4 debe mostrar el plano rectangular de una oficina de 100 m × 50 m dividido en zonas de trabajo abiertas, salas de reunión y pasillos. Sobre el plano deben colocarse 20 APs en una disposición tipo malla 5×4, con celdas ligeramente solapadas. Cada AP debe tener dos etiquetas de color: una letra A/B/C para el bloque de 6 GHz y una marca F1/F2/F3/F4 para el canal de 5 GHz. Alrededor de cada AP debe dibujarse un círculo o hexágono de cobertura principal de 6 GHz y otro contorno más amplio para 5 GHz. Flechas pequeñas deben indicar que el tráfico de alto caudal tiende a usar 6 GHz, mientras que el tráfico más robusto o de continuidad puede mantenerse en 5 GHz. En una esquina del plano debe aparecer un recuadro resumen con cuatro números: “20 APs”, “15 Gbps demanda agregada”, “200 Mbps/usuario activo promedio intra-AP” y “latencia local estimada: 3.5 ms”. La figura debe servir como puente entre la teoría de MLO, el presupuesto de enlace y el diseño práctico de una red empresarial.*

---

## Referencias

[1] IEEE Computer Society, *IEEE Standard for Information Technology—Telecommunications and information exchange between systems Local and metropolitan area networks—Specific requirements—Part 11: Wireless LAN Medium Access Control (MAC) and Physical Layer (PHY) Specifications Amendment 2: Enhancements for Extremely High Throughput (EHT)*, **IEEE Std 802.11be-2024**, 2024.

[2] IEEE Computer Society, *IEEE Draft Standard for Information Technology—Telecommunications and information exchange between systems Local and metropolitan area networks—Specific requirements—Part 11: Wireless LAN Medium Access Control (MAC) and Physical Layer (PHY) Specifications Amendment 9: Enhancements for Extremely High Throughput (EHT)*, **IEEE P802.11be/D3.0**, 2022. DOI: [10.1109/IEEESTD.2022.9808491](https://doi.org/10.1109/IEEESTD.2022.9808491)

[3] D. López-Pérez, A. Garcia-Rodriguez, L. Galati-Giordano, M. Kasslin, and K. Doppler, “IEEE 802.11be Extremely High Throughput: The Next Generation of Wi-Fi Technology Beyond 802.11ax,” *IEEE Communications Magazine*, vol. 57, no. 9, pp. 113–119, Sep. 2019. DOI: [10.1109/MCOM.001.1900338](https://doi.org/10.1109/MCOM.001.1900338)

[4] B. Bellalta, “Wi-Fi 7 Strikes Back,” *IEEE Communications Magazine*, vol. 59, no. 4, pp. 102–108, Apr. 2021. DOI: [10.1109/MCOM.001.2100043](https://doi.org/10.1109/MCOM.001.2100043)

[5] M. A. Kishk, T. Khattab, M. Guizani, J. S. Thompson, and M. Ghogho, “A Survey on IEEE 802.11be (Wi-Fi 7): Recent Advances, Open Challenges, and Future Trends,” *IEEE Communications Surveys & Tutorials*, vol. 24, no. 2, pp. 909–957, 2022. DOI: [10.1109/COMST.2022.3154044](https://doi.org/10.1109/COMST.2022.3154044)

[6] B. Bellalta, J. Barceló, A. Zubow, A. D. Campo, and T. Rasheed, “IEEE 802.11be Extremely High Throughput (Wi-Fi 7): Advances and Future Directions,” *IEEE Communications Surveys & Tutorials*, vol. 24, no. 1, pp. 674–716, 2022. DOI: [10.1109/COMST.2022.3141194](https://doi.org/10.1109/COMST.2022.3141194)

[7] ITU-R, *Recommendation ITU-R P.1238-13: Propagation data and prediction methods for the planning of indoor radiocommunication systems and radio local area networks in the frequency range 300 MHz to 450 GHz*, International Telecommunication Union, 2023.

[8] 3GPP, *TR 38.901: Study on channel model for frequencies from 0.5 to 100 GHz*, 3rd Generation Partnership Project.

[9] IEEE Computer Society, “IEEE Standard for Information Technology—Telecommunications and Information Exchange between Systems—Local and Metropolitan Area Networks—Specific Requirements—Amendment 1: Enhancements for High-Efficiency WLAN,” *IEEE Std 802.11ax-2021*, May 2021. DOI: [10.1109/IEEESTD.2021.9442429](https://doi.org/10.1109/IEEESTD.2021.9442429)
