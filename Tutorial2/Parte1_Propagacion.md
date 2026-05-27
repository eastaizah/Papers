# Tutorial: Propagación de Ondas Electromagnéticas para Dimensionamiento de Cobertura

## Parte 1: Fundamentos, Modelos de Propagación en Exteriores e Interiores

---

## 1. Introducción General al Tutorial

### 1.1 Motivación y Objetivos

El diseño y la planificación de redes de telecomunicaciones inalámbricas constituyen una de las disciplinas más relevantes de la ingeniería moderna. Desde las redes celulares de quinta generación (5G NR) hasta las redes de área local inalámbricas (Wi-Fi 6/6E/7), el éxito de cualquier despliegue depende de una comprensión profunda de cómo las ondas electromagnéticas se propagan a través de distintos entornos. Sin esta comprensión, el ingeniero no puede estimar con precisión el alcance de una estación base, determinar la cantidad de puntos de acceso necesarios para cubrir un edificio de oficinas, ni garantizar que los usuarios finales experimenten una calidad de servicio adecuada.

La motivación principal de este tutorial es proporcionar al lector una guía completa, rigurosa y pedagógica sobre los modelos de propagación electromagnética más utilizados en la industria y en los estándares internacionales. El objetivo no es simplemente presentar ecuaciones, sino desarrollar en el lector una intuición física sólida que le permita seleccionar, aplicar e interpretar correctamente estos modelos en escenarios reales de dimensionamiento de cobertura.

Los objetivos específicos de este tutorial son:

1. Comprender los fundamentos físicos de la propagación de ondas electromagnéticas, incluyendo los mecanismos de reflexión, difracción, dispersión y absorción.
2. Dominar los modelos empíricos y semi-empíricos de propagación en exteriores, desde el clásico Okumura-Hata hasta el modelo 3GPP TR 38.901 utilizado en el diseño de redes 5G.
3. Conocer en detalle los modelos de propagación en interiores, incluyendo la recomendación ITU-R P.1238, los modelos IEEE 802.11ax/be y las técnicas de presupuesto de enlace (*link budget*) para entornos *indoor*.
4. Aplicar estos conocimientos al dimensionamiento práctico de cobertura, realizando cálculos completos con ejemplos numéricos representativos.

### 1.2 Audiencia Objetivo

Este tutorial está dirigido a estudiantes de ingeniería de telecomunicaciones, electrónica o afines que se encuentran en los últimos semestres de su formación de pregrado o en los primeros semestres de posgrado. También resulta útil para ingenieros en ejercicio que deseen actualizar sus conocimientos en modelos de propagación modernos, particularmente aquellos relacionados con tecnologías 5G NR y Wi-Fi 6E/7.

Se asume que el lector posee conocimientos básicos de:

- Álgebra y cálculo diferencial e integral.
- Fundamentos de campos electromagnéticos (al menos un curso introductorio).
- Nociones elementales de probabilidad y estadística.
- Conceptos básicos de sistemas de comunicaciones.

No se requiere experiencia previa en planificación de redes ni en el uso de herramientas profesionales de cobertura.

### 1.3 Estructura del Documento

El presente documento (Parte 1) está organizado en cuatro secciones principales. La Sección 2 establece los fundamentos teóricos de la propagación electromagnética, incluyendo las ecuaciones de Maxwell, los mecanismos de propagación a gran escala y el modelado estadístico de la pérdida de trayectoria. La Sección 3 presenta los modelos de propagación en exteriores más relevantes: Okumura-Hata, COST-231 Hata y el modelo 3GPP TR 38.901 para redes 5G. La Sección 4 aborda los modelos de propagación en interiores, incluyendo la recomendación ITU-R P.1238-11, los modelos IEEE 802.11ax/be y las técnicas de dimensionamiento de cobertura *indoor*. Cada sección incluye ejemplos numéricos detallados y descripciones de figuras que facilitan la comprensión de los conceptos presentados.

---

## 2. Fundamentos de Propagación de Ondas Electromagnéticas

### 2.1 Conceptos Básicos

#### 2.1.1 Ondas Electromagnéticas: Definición, Espectro, Longitud de Onda y Frecuencia

Una onda electromagnética es una perturbación que se propaga a través del espacio transportando energía mediante la oscilación acoplada de campos eléctricos y magnéticos mutuamente perpendiculares. A diferencia de las ondas mecánicas (como el sonido), las ondas electromagnéticas no requieren un medio material para propagarse: pueden viajar en el vacío a la velocidad de la luz.

La relación fundamental entre la frecuencia $f$, la longitud de onda $\lambda$ y la velocidad de propagación $c$ está dada por:

$$\lambda = \frac{c}{f}$$

donde:

- $\lambda$ es la longitud de onda, medida en metros (m). Representa la distancia espacial entre dos puntos consecutivos de la onda que se encuentran en la misma fase (por ejemplo, entre dos crestas consecutivas).
- $c$ es la velocidad de la luz en el vacío, cuyo valor es $c \approx 3 \times 10^8$ m/s. En medios materiales, la velocidad de propagación es menor y depende del índice de refracción del medio.
- $f$ es la frecuencia de la onda, medida en hercios (Hz). Indica el número de ciclos completos de oscilación que la onda realiza por segundo.

El espectro electromagnético abarca un rango enorme de frecuencias, desde las ondas de radio de extremadamente baja frecuencia (ELF, por debajo de 3 kHz) hasta los rayos gamma (por encima de $10^{19}$ Hz). En telecomunicaciones inalámbricas, las bandas de mayor interés son:

- **Banda UHF (300 MHz – 3 GHz):** Utilizada por redes celulares 2G, 3G, 4G y la banda baja de 5G (FR1). A 900 MHz, la longitud de onda es $\lambda = 3 \times 10^8 / 9 \times 10^8 = 0.333$ m.
- **Banda SHF (3 GHz – 30 GHz):** Incluye las bandas de Wi-Fi (5 GHz, 6 GHz) y las bandas medias y altas de 5G. A 5 GHz, $\lambda = 0.06$ m = 6 cm.
- **Banda EHF / ondas milimétricas (30 GHz – 300 GHz):** Utilizada por 5G FR2. A 28 GHz, $\lambda = 0.0107$ m $\approx$ 1.07 cm.

**[Descripción de Figura 2.1]:** *Diagrama del espectro electromagnético orientado a telecomunicaciones. Eje horizontal representando la frecuencia en escala logarítmica desde 100 MHz hasta 100 GHz. Eje vertical superior indicando la longitud de onda correspondiente (de 3 m a 3 mm). Bandas coloreadas para UHF (verde claro), SHF (azul claro) y EHF (violeta). Dentro de cada banda, marcas indicando las tecnologías que operan en ella: GSM/UMTS/LTE en UHF, Wi-Fi 5/6/6E y 5G Sub-6 en SHF, y 5G mmWave en EHF. Flechas indicando que a mayor frecuencia, menor longitud de onda y mayor atenuación por propagación.*

#### 2.1.2 Ecuaciones de Maxwell Simplificadas y su Relevancia

Las ecuaciones de Maxwell constituyen el marco teórico fundamental que describe completamente el comportamiento de los campos eléctricos y magnéticos, y por lo tanto, de todas las ondas electromagnéticas. En su forma diferencial para un medio lineal, homogéneo e isótropo, y en ausencia de fuentes (región libre de cargas y corrientes), las ecuaciones de Maxwell se reducen a:

$$\nabla \cdot \mathbf{E} = 0$$

$$\nabla \cdot \mathbf{B} = 0$$

$$\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}$$

$$\nabla \times \mathbf{B} = \mu_0 \epsilon_0 \frac{\partial \mathbf{E}}{\partial t}$$

donde:

- $\mathbf{E}$ es el vector de campo eléctrico, medido en voltios por metro (V/m). Representa la fuerza que experimentaría una carga unitaria positiva colocada en ese punto del espacio.
- $\mathbf{B}$ es el vector de densidad de flujo magnético (o inducción magnética), medido en teslas (T). Describe la componente magnética del campo electromagnético.
- $\nabla \cdot$ es el operador divergencia, que mide la tendencia de un campo vectorial a emanar de un punto (o converger hacia él).
- $\nabla \times$ es el operador rotacional, que mide la tendencia de un campo vectorial a "girar" alrededor de un punto.
- $\mu_0 = 4\pi \times 10^{-7}$ H/m es la permeabilidad magnética del vacío.
- $\epsilon_0 = 8.854 \times 10^{-12}$ F/m es la permitividad eléctrica del vacío.
- $\partial / \partial t$ denota la derivada parcial con respecto al tiempo.

La primera ecuación ($\nabla \cdot \mathbf{E} = 0$) establece que, en ausencia de cargas libres, el campo eléctrico no tiene fuentes ni sumideros puntuales: las líneas de campo eléctrico no comienzan ni terminan en el espacio libre. La segunda ecuación ($\nabla \cdot \mathbf{B} = 0$) expresa el hecho experimental de que no existen monopolos magnéticos: las líneas de campo magnético siempre forman bucles cerrados.

La tercera ecuación (ley de Faraday) establece que un campo magnético que varía en el tiempo genera un campo eléctrico rotacional. La cuarta ecuación (ley de Ampère-Maxwell) establece el fenómeno recíproco: un campo eléctrico que varía en el tiempo genera un campo magnético rotacional. Es precisamente este acoplamiento mutuo entre los campos eléctrico y magnético lo que permite la existencia de ondas electromagnéticas que se autosostienen y se propagan a través del espacio.

A partir de estas ecuaciones, combinándolas mediante manipulación vectorial, se obtiene la ecuación de onda para el campo eléctrico en el vacío:

$$\nabla^2 \mathbf{E} = \mu_0 \epsilon_0 \frac{\partial^2 \mathbf{E}}{\partial t^2}$$

Esta ecuación de onda demuestra que las perturbaciones del campo eléctrico se propagan como ondas con velocidad:

$$c = \frac{1}{\sqrt{\mu_0 \epsilon_0}} = \frac{1}{\sqrt{4\pi \times 10^{-7} \times 8.854 \times 10^{-12}}} \approx 3 \times 10^8 \text{ m/s}$$

Este resultado, obtenido teóricamente por James Clerk Maxwell en 1865, fue una de las predicciones más profundas de la física: la velocidad de propagación de las ondas electromagnéticas coincide con la velocidad de la luz medida experimentalmente, lo que llevó a Maxwell a proponer que la luz misma es una onda electromagnética.

Para los propósitos de la ingeniería de propagación, las ecuaciones de Maxwell proporcionan la base teórica que justifica todos los fenómenos que estudiaremos (reflexión, difracción, dispersión), aunque en la práctica utilizaremos modelos empíricos simplificados que capturan los efectos dominantes sin necesidad de resolver las ecuaciones completas.

#### 2.1.3 Potencia Radiada, PIRE y Ganancia de Antena

En un sistema de comunicaciones inalámbrico, la estación transmisora convierte la señal eléctrica en una onda electromagnética mediante una antena. No toda la potencia entregada a la antena se convierte en radiación útil; existen pérdidas en los cables de conexión, conectores y en la propia antena. Para caracterizar la emisión de un transmisor, se definen varios conceptos fundamentales.

La **potencia de transmisión** $P_T$ es la potencia eléctrica que el transmisor entrega a la entrada de la antena, típicamente medida en vatios (W) o en decibelios referidos a un milivatio (dBm):

$$P_{T,\text{dBm}} = 10 \log_{10}\left(\frac{P_T}{1 \text{ mW}}\right)$$

Por ejemplo, un transmisor que entrega $P_T = 1$ W tiene una potencia de $P_{T,\text{dBm}} = 10 \log_{10}(1000) = 30$ dBm. Un transmisor Wi-Fi típico con $P_T = 100$ mW tiene $P_{T,\text{dBm}} = 10 \log_{10}(100) = 20$ dBm.

La **ganancia de antena** $G_T$ describe la capacidad de la antena para concentrar la energía radiada en una dirección particular, en comparación con una antena isotrópica (hipotética antena que radia uniformemente en todas las direcciones). Se expresa en decibelios referidos a una antena isotrópica (dBi):

$$G_{T,\text{dBi}} = 10 \log_{10}\left(\frac{U(\theta, \phi)}{U_{\text{iso}}}\right)$$

donde $U(\theta, \phi)$ es la intensidad de radiación de la antena en la dirección $(\theta, \phi)$ y $U_{\text{iso}} = P_T / (4\pi)$ es la intensidad de radiación uniforme de una antena isotrópica. Una antena dipolo de media onda tiene una ganancia máxima de aproximadamente 2.15 dBi, mientras que una antena sectorial de estación base celular puede tener una ganancia de 15 a 18 dBi.

La **Potencia Isotrópica Radiada Equivalente (PIRE)**, conocida en inglés como *Equivalent Isotropically Radiated Power (EIRP)*, es la potencia que debería radiar una antena isotrópica para producir la misma densidad de potencia que la antena real en la dirección de máxima radiación:

$$\text{PIRE} = P_T \cdot G_T$$

En decibelios:

$$\text{PIRE}_{\text{dBm}} = P_{T,\text{dBm}} + G_{T,\text{dBi}}$$

La PIRE es un parámetro fundamental en la planificación de redes, ya que los organismos reguladores especifican límites de PIRE para cada banda de frecuencias. Por ejemplo, si un punto de acceso Wi-Fi opera con $P_T = 20$ dBm y utiliza una antena con $G_T = 6$ dBi, la PIRE es $20 + 6 = 26$ dBm.

La **densidad de potencia** $S$ a una distancia $d$ de una antena isotrópica que radia una potencia $P_T$ se obtiene distribuyendo la potencia uniformemente sobre la superficie de una esfera de radio $d$:

$$S = \frac{P_T \cdot G_T}{4\pi d^2} \quad \text{[W/m}^2\text{]}$$

Esta expresión es fundamental porque conecta la potencia transmitida con la intensidad de la señal en el receptor, y será la base para derivar la ecuación de transmisión de Friis en secciones posteriores.

### 2.2 Mecanismos de Propagación a Gran Escala

Cuando una onda electromagnética viaja desde un transmisor hacia un receptor en un entorno real (urbano, suburbano, rural o interior), interactúa con los objetos presentes en el medio: edificios, vehículos, árboles, terreno, muebles, paredes, etc. Estas interacciones modifican la amplitud, fase, dirección y polarización de la onda. Los mecanismos fundamentales de interacción son la reflexión, la difracción, la dispersión (*scattering*) y la absorción. Comprender estos mecanismos es esencial para interpretar correctamente los modelos de propagación que se presentarán en las secciones siguientes.

#### 2.2.1 Reflexión

La reflexión ocurre cuando una onda electromagnética incide sobre una superficie cuyas dimensiones son mucho mayores que la longitud de onda de la señal. En este caso, parte de la energía de la onda es reflejada de regreso al medio original, y parte es transmitida (refractada) hacia el segundo medio. Este fenómeno es particularmente relevante en entornos urbanos, donde las fachadas de los edificios, el suelo, las superficies acristaladas y las estructuras metálicas actúan como reflectores eficientes.

**Ley de Snell de la reflexión y la refracción:**

Cuando una onda electromagnética incide sobre la interfaz plana entre dos medios con índices de refracción $n_1$ y $n_2$, se cumple la ley de Snell:

$$n_1 \sin(\theta_i) = n_2 \sin(\theta_t)$$

donde:

- $\theta_i$ es el ángulo de incidencia, medido desde la normal a la superficie. Es el ángulo que forma el rayo incidente con la perpendicular a la superficie en el punto de incidencia.
- $\theta_t$ es el ángulo de transmisión (o refracción), medido desde la misma normal. Es el ángulo que forma el rayo transmitido con la perpendicular a la superficie.
- $n_1$ es el índice de refracción del primer medio (del cual proviene la onda). Para el aire, $n_1 \approx 1$.
- $n_2$ es el índice de refracción del segundo medio. Para vidrio común, $n_2 \approx 1.5$; para hormigón, $n_2 \approx 2.3$ a frecuencias de microondas.

Además, el ángulo de reflexión $\theta_r$ es igual al ángulo de incidencia: $\theta_r = \theta_i$.

**Coeficientes de reflexión de Fresnel:**

La fracción de energía reflejada depende de la polarización de la onda, del ángulo de incidencia y de las propiedades electromagnéticas de los medios. Los coeficientes de reflexión de Fresnel cuantifican esta fracción para las dos polarizaciones lineales fundamentales.

Para la **polarización perpendicular** (TE, campo eléctrico perpendicular al plano de incidencia):

$$\Gamma_{\perp} = \frac{n_1 \cos(\theta_i) - n_2 \cos(\theta_t)}{n_1 \cos(\theta_i) + n_2 \cos(\theta_t)}$$

Para la **polarización paralela** (TM, campo eléctrico en el plano de incidencia):

$$\Gamma_{\parallel} = \frac{n_2 \cos(\theta_i) - n_1 \cos(\theta_t)}{n_2 \cos(\theta_i) + n_1 \cos(\theta_t)}$$

donde $\theta_t$ se obtiene de la ley de Snell. El coeficiente de reflexión $\Gamma$ es un número adimensional que puede tomar valores entre $-1$ y $+1$. Su magnitud al cuadrado, $|\Gamma|^2$, representa la fracción de potencia incidente que es reflejada (reflectancia). La fracción transmitida es $1 - |\Gamma|^2$.

**Ejemplo numérico 2.1:** Una onda electromagnética a 2.4 GHz ($\lambda = 0.125$ m) incide sobre una pared de hormigón con un ángulo de $\theta_i = 30°$. El índice de refracción del hormigón a esta frecuencia es aproximadamente $n_2 = 2.3$ (el aire tiene $n_1 = 1.0$).

Paso 1: Calcular el ángulo de transmisión usando la ley de Snell:

$$\sin(\theta_t) = \frac{n_1}{n_2}\sin(\theta_i) = \frac{1.0}{2.3}\sin(30°) = \frac{0.5}{2.3} = 0.2174$$

$$\theta_t = \arcsin(0.2174) = 12.56°$$

Paso 2: Calcular el coeficiente de reflexión para polarización perpendicular:

$$\Gamma_{\perp} = \frac{1.0 \times \cos(30°) - 2.3 \times \cos(12.56°)}{1.0 \times \cos(30°) + 2.3 \times \cos(12.56°)}$$

$$\Gamma_{\perp} = \frac{0.866 - 2.3 \times 0.976}{0.866 + 2.3 \times 0.976} = \frac{0.866 - 2.245}{0.866 + 2.245} = \frac{-1.379}{3.111} = -0.443$$

La potencia reflejada es $|\Gamma_{\perp}|^2 = 0.443^2 = 0.196$, es decir, aproximadamente el 19.6% de la potencia incidente se refleja y el 80.4% se transmite hacia el interior de la pared (donde sufrirá atenuación adicional al atravesarla).

**[Descripción de Figura 2.2]:** *Diagrama que ilustra la reflexión y refracción de una onda electromagnética en la interfaz entre aire y hormigón. A la izquierda, el medio 1 (aire, $n_1 = 1.0$) con un rayo incidente que forma un ángulo $\theta_i = 30°$ con la línea normal (punteada, perpendicular a la superficie). Se muestra el rayo reflejado saliendo con el mismo ángulo $\theta_r = 30°$ al otro lado de la normal. A la derecha, el medio 2 (hormigón, $n_2 = 2.3$) con el rayo transmitido formando un ángulo $\theta_t = 12.56°$ con la normal. Flechas indicando la amplitud relativa de cada rayo: el rayo reflejado más delgado (19.6% de potencia) y el transmitido más grueso (80.4% de potencia). Vectores de campo eléctrico $\mathbf{E}$ y magnético $\mathbf{H}$ indicados en cada rayo.*

#### 2.2.2 Difracción

La difracción es el fenómeno por el cual las ondas electromagnéticas pueden rodear obstáculos y alcanzar regiones que no están en línea de visión directa (*Non-Line-of-Sight, NLoS*) con el transmisor. Este mecanismo es crucial en entornos urbanos, donde edificios, colinas y otras estructuras bloquean parcialmente la trayectoria directa entre el transmisor y el receptor.

**Principio de Huygens-Fresnel:**

El fundamento teórico de la difracción es el principio de Huygens (formulado por Christiaan Huygens en 1678 y formalizado matemáticamente por Augustin-Jean Fresnel en 1818). Este principio establece que cada punto de un frente de onda puede considerarse como una fuente puntual de ondas esféricas secundarias. La onda en cualquier punto posterior del espacio es el resultado de la superposición (interferencia) de todas estas ondas secundarias.

**Modelo de difracción de Fresnel – Zona de Fresnel:**

Para analizar la difracción de manera cuantitativa, se utiliza el concepto de zonas de Fresnel. Considérese un enlace de radio entre un transmisor T y un receptor R separados una distancia $d$. Las zonas de Fresnel son regiones elipsoidales concéntricas alrededor de la línea de visión directa T-R. La $n$-ésima zona de Fresnel está definida como el lugar geométrico de todos los puntos P tales que la diferencia entre la trayectoria T-P-R y la trayectoria directa T-R es exactamente $n\lambda/2$:

$$|TP| + |PR| - |TR| = \frac{n\lambda}{2}$$

El radio de la $n$-ésima zona de Fresnel a una distancia $d_1$ del transmisor (y $d_2 = d - d_1$ del receptor) se calcula como:

$$r_n = \sqrt{\frac{n \lambda \, d_1 \, d_2}{d_1 + d_2}}$$

donde:

- $r_n$ es el radio de la $n$-ésima zona de Fresnel en metros.
- $n$ es el número de la zona (1, 2, 3, ...).
- $\lambda$ es la longitud de onda de la señal en metros.
- $d_1$ es la distancia desde el transmisor al punto de observación en metros.
- $d_2$ es la distancia desde el punto de observación al receptor en metros.

La primera zona de Fresnel ($n = 1$) es la más importante desde el punto de vista práctico. Se considera que un enlace de radio tiene despejamiento adecuado (sin difracción significativa) cuando al menos el 60% del radio de la primera zona de Fresnel está libre de obstáculos. Si un obstáculo penetra en la primera zona de Fresnel, se produce una pérdida adicional por difracción que puede ser significativa.

**Ejemplo numérico 2.2:** Calcular el radio de la primera zona de Fresnel en el punto medio de un enlace punto a punto de 2 km a una frecuencia de 2.4 GHz.

Datos: $f = 2.4$ GHz, $d = 2000$ m, punto medio: $d_1 = d_2 = 1000$ m.

Paso 1: Calcular la longitud de onda:

$$\lambda = \frac{c}{f} = \frac{3 \times 10^8}{2.4 \times 10^9} = 0.125 \text{ m}$$

Paso 2: Calcular el radio de la primera zona de Fresnel ($n = 1$):

$$r_1 = \sqrt{\frac{1 \times 0.125 \times 1000 \times 1000}{1000 + 1000}} = \sqrt{\frac{125000}{2000}} = \sqrt{62.5} = 7.91 \text{ m}$$

Esto significa que en el punto medio del enlace, cualquier obstáculo (edificio, árbol, colina) debe estar al menos a $0.6 \times 7.91 = 4.74$ m por debajo de la línea de visión directa para no causar pérdidas significativas por difracción.

Para el modelo de difracción de borde afilado (*knife-edge diffraction*), la pérdida por difracción se puede estimar utilizando el parámetro de Fresnel-Kirchhoff $\nu$:

$$\nu = h \sqrt{\frac{2(d_1 + d_2)}{\lambda \, d_1 \, d_2}}$$

donde $h$ es la altura efectiva del obstáculo por encima de la línea de visión directa (positiva si el obstáculo sobresale, negativa si está por debajo). La pérdida por difracción en dB se aproxima como:

$$L_{\text{diff}} \approx \begin{cases} 0 \text{ dB} & \text{si } \nu \leq -1 \\ 20 \log_{10}(0.5 - 0.62\nu) & \text{si } -1 < \nu \leq 0 \\ 20 \log_{10}(0.5 \, e^{-0.95\nu}) & \text{si } 0 < \nu \leq 1 \\ 20 \log_{10}\left(\frac{0.4}{\sqrt{0.1184 + (0.38 - 0.1\nu)^2}}\right) & \text{si } 1 < \nu \leq 2.4 \\ 20 \log_{10}\left(\frac{0.225}{\nu}\right) & \text{si } \nu > 2.4 \end{cases}$$

**[Descripción de Figura 2.3]:** *Diagrama que ilustra las zonas de Fresnel entre un transmisor T (a la izquierda) y un receptor R (a la derecha), separados una distancia $d$. Vista lateral mostrando la línea de visión directa como una línea horizontal central. Tres elipses concéntricas alrededor de esta línea representan la primera (sombreada en verde claro), segunda (amarillo) y tercera (naranja) zonas de Fresnel. Las etiquetas $r_1$, $r_2$, $r_3$ indican los radios de cada zona en el punto medio. Un edificio parcialmente obstruyendo la primera zona de Fresnel, con una flecha indicando la altura $h$ del edificio por encima de la línea de visión. Los parámetros $d_1$ y $d_2$ están marcados como las distancias del transmisor y receptor al obstáculo, respectivamente.*

#### 2.2.3 Dispersión (Scattering)

La dispersión, o *scattering*, ocurre cuando una onda electromagnética incide sobre un objeto cuyas dimensiones son comparables o menores que la longitud de onda. A diferencia de la reflexión (que ocurre en superficies lisas y extensas), la dispersión redistribuye la energía de la onda en múltiples direcciones. Este fenómeno es particularmente relevante cuando la señal interactúa con objetos como postes de iluminación, señales de tráfico, follaje de árboles, cables aéreos y superficies rugosas.

La dispersión se clasifica en función de la relación entre el tamaño del objeto dispersor y la longitud de onda:

- **Dispersión de Rayleigh:** Ocurre cuando el tamaño del objeto es mucho menor que la longitud de onda ($a \ll \lambda$, donde $a$ es la dimensión característica del objeto). La intensidad de la dispersión es proporcional a $f^4$, lo que significa que las frecuencias más altas se dispersan mucho más que las frecuencias bajas. Este tipo de dispersión es relevante, por ejemplo, para gotas de lluvia a frecuencias por debajo de unos 10 GHz.

- **Dispersión de Mie:** Ocurre cuando el tamaño del objeto es comparable a la longitud de onda ($a \approx \lambda$). La distribución angular de la energía dispersada es más compleja y depende fuertemente de la forma y composición del objeto.

- **Dispersión geométrica (óptica):** Ocurre cuando el tamaño del objeto es mucho mayor que la longitud de onda ($a \gg \lambda$). En este régimen, la dispersión se describe mejor mediante las leyes de la óptica geométrica (reflexión y refracción).

En la planificación de redes urbanas, la dispersión por superficies rugosas es relevante. El criterio de Rayleigh establece que una superficie se considera rugosa si la variación de altura $\Delta h$ de la superficie satisface:

$$\Delta h > \frac{\lambda}{8 \cos(\theta_i)}$$

donde $\theta_i$ es el ángulo de incidencia. Si la superficie es rugosa según este criterio, la reflexión especular se atenúa y una parte significativa de la energía se dispersa en múltiples direcciones.

**[Descripción de Figura 2.4]:** *Tres paneles que ilustran los tipos de dispersión. Panel izquierdo: "Dispersión de Rayleigh" — una onda incidente (flecha azul) golpea una partícula pequeña (círculo rojo, con etiqueta $a \ll \lambda$), y flechas de dispersión distribuidas de manera simétrica hacia adelante y atrás. Panel central: "Dispersión de Mie" — la onda incide sobre una partícula de tamaño comparable a $\lambda$, con un lóbulo de dispersión predominante hacia adelante y lóbulos laterales más pequeños. Panel derecho: "Dispersión por superficie rugosa" — una onda incidente sobre una superficie irregular, con múltiples rayos reflejados en direcciones diferentes (a diferencia de la reflexión especular en una superficie lisa, que se muestra como referencia con línea punteada).*

#### 2.2.4 Absorción Atmosférica

La absorción atmosférica es el mecanismo por el cual las moléculas de los gases constituyentes de la atmósfera (principalmente oxígeno O$_2$ y vapor de agua H$_2$O) absorben energía de la onda electromagnética, convirtiéndola en calor. Este efecto es despreciable a frecuencias por debajo de aproximadamente 10 GHz y para distancias cortas, pero se vuelve significativo en las bandas de ondas milimétricas utilizadas por 5G FR2.

Los picos de absorción más relevantes son:

- **Vapor de agua (H$_2$O):** Picos de absorción a 22.2 GHz y 183.3 GHz. A 22.2 GHz, la atenuación es de aproximadamente 0.2 dB/km en condiciones estándar de humedad.
- **Oxígeno (O$_2$):** Pico de absorción a 60 GHz, donde la atenuación puede alcanzar 15-16 dB/km. A 28 GHz (banda candidata de 5G mmWave), la atenuación atmosférica es de solo aproximadamente 0.07 dB/km, lo que hace que esta banda sea viable para comunicaciones terrestres en distancias cortas.

La atenuación atmosférica total $A_a$ (en dB) para un enlace de longitud $d$ (en km) se calcula como:

$$A_a = \gamma_a \cdot d$$

donde $\gamma_a$ es el coeficiente de atenuación específica en dB/km, que depende de la frecuencia, la temperatura, la presión y la humedad. Los valores detallados se encuentran en la Recomendación ITU-R P.676.

La atenuación por lluvia es otro factor importante en bandas de ondas milimétricas. La Recomendación ITU-R P.838 proporciona un modelo para estimar la atenuación específica por lluvia $\gamma_R$ (en dB/km):

$$\gamma_R = k \cdot R^{\alpha}$$

donde $R$ es la tasa de lluvia en mm/h, y $k$ y $\alpha$ son coeficientes que dependen de la frecuencia y la polarización. A 28 GHz, para una lluvia intensa de $R = 50$ mm/h, la atenuación puede ser del orden de 10 dB/km.

### 2.3 Modelado de Pérdida de Trayectoria (Path Loss)

#### 2.3.1 Modelo de Espacio Libre (Ecuación de Friis)

El modelo más fundamental de propagación es el de espacio libre, que describe la atenuación de la señal cuando la onda viaja en un medio sin obstáculos, reflexiones ni otros efectos. Aunque esta situación ideal rara vez se da en la práctica (quizás solo en enlaces satelitales o comunicaciones en el espacio profundo), la ecuación de Friis constituye el punto de partida y la referencia contra la cual se comparan todos los demás modelos.

**Derivación completa:**

Considérese un transmisor con potencia $P_T$ y ganancia de antena $G_T$. La densidad de potencia a una distancia $d$ del transmisor es:

$$S = \frac{P_T \cdot G_T}{4\pi d^2}$$

La antena receptora captura esta densidad de potencia a través de su área efectiva $A_e$. La relación entre la ganancia de la antena receptora $G_R$ y su área efectiva es:

$$A_e = \frac{G_R \lambda^2}{4\pi}$$

Esta ecuación fundamental de la teoría de antenas establece que el área efectiva de una antena es proporcional a su ganancia y al cuadrado de la longitud de onda. A frecuencias más altas (longitudes de onda más cortas), una antena con la misma ganancia tiene un área efectiva menor.

La potencia recibida $P_R$ es el producto de la densidad de potencia por el área efectiva:

$$P_R = S \cdot A_e = \frac{P_T \cdot G_T}{4\pi d^2} \cdot \frac{G_R \lambda^2}{4\pi} = P_T G_T G_R \left(\frac{\lambda}{4\pi d}\right)^2$$

Esta es la **ecuación de transmisión de Friis**. Reordenando:

$$\frac{P_R}{P_T} = G_T G_R \left(\frac{\lambda}{4\pi d}\right)^2$$

La **pérdida de propagación en espacio libre (FSPL)** se define como la atenuación sufrida por la señal considerando antenas isotrópicas ($G_T = G_R = 1$):

$$\text{FSPL} = \left(\frac{4\pi d}{\lambda}\right)^2$$

Expresada en decibelios:

$$\text{FSPL}_{\text{dB}} = 10 \log_{10}\left(\frac{4\pi d}{\lambda}\right)^2 = 20 \log_{10}\left(\frac{4\pi d}{\lambda}\right)$$

Sustituyendo $\lambda = c/f$:

$$\text{FSPL}_{\text{dB}} = 20 \log_{10}(d) + 20 \log_{10}(f) + 20 \log_{10}\left(\frac{4\pi}{c}\right)$$

Evaluando la constante con $d$ en metros y $f$ en Hz:

$$20 \log_{10}\left(\frac{4\pi}{3 \times 10^8}\right) = 20 \log_{10}(4.189 \times 10^{-8}) = -147.56 \text{ dB}$$

Si expresamos $d$ en kilómetros y $f$ en MHz, la ecuación se simplifica a la forma más conocida:

$$\boxed{\text{FSPL}_{\text{dB}} = 32.44 + 20 \log_{10}(d_{\text{km}}) + 20 \log_{10}(f_{\text{MHz}})}$$

Es importante comprender el significado físico de esta ecuación. La FSPL no representa una absorción de energía por el medio (en el espacio libre no hay absorción). Representa la atenuación geométrica debida a la expansión esférica del frente de onda: a medida que la onda se aleja del transmisor, la misma potencia se distribuye sobre una superficie esférica cada vez mayor, por lo que la densidad de potencia disminuye con el cuadrado de la distancia. El término que depende de la frecuencia refleja la dependencia del área efectiva de la antena receptora con $\lambda^2$.

**Ejemplo numérico 2.3:** Calcular la potencia recibida en un enlace Wi-Fi a 5 GHz con las siguientes condiciones: $P_T = 20$ dBm, $G_T = 3$ dBi, $G_R = 0$ dBi, distancia $d = 50$ m, en condiciones de espacio libre.

Paso 1: Calcular la FSPL:

$$\text{FSPL}_{\text{dB}} = 32.44 + 20 \log_{10}(0.05) + 20 \log_{10}(5000)$$

$$= 32.44 + 20 \times (-1.301) + 20 \times 3.699$$

$$= 32.44 - 26.02 + 73.98 = 80.40 \text{ dB}$$

Paso 2: Calcular la potencia recibida usando la ecuación de enlace (*link budget*):

$$P_R = P_T + G_T + G_R - \text{FSPL}$$

$$P_R = 20 + 3 + 0 - 80.40 = -57.40 \text{ dBm}$$

Este resultado indica que a 50 metros en espacio libre, un receptor Wi-Fi recibiría $-57.40$ dBm, un nivel que proporciona una señal excelente (la sensibilidad típica de un receptor Wi-Fi 802.11ac/ax es del orden de $-70$ a $-85$ dBm, dependiendo del MCS utilizado).

#### 2.3.2 Modelo General de Pérdida de Trayectoria

En entornos reales, la señal recibida fluctúa significativamente respecto al valor predicho por el modelo de espacio libre. Los edificios, el terreno, la vegetación y otros obstáculos causan reflexiones, difracciones y dispersiones que pueden atenuar o, en algunos casos, reforzar la señal. Para capturar estas variaciones, la pérdida de trayectoria total se modela como la suma de una componente determinista media y una componente aleatoria:

$$PL(d) \text{ [dB]} = \overline{PL}(d) + X_{\sigma}$$

donde:

- $PL(d)$ es la pérdida de trayectoria total a una distancia $d$, en dB.
- $\overline{PL}(d)$ es la pérdida de trayectoria media (o mediana), que depende determinísticamente de la distancia y que predicen los modelos de propagación empíricos como Okumura-Hata o COST-231.
- $X_{\sigma}$ es una variable aleatoria de media cero que modela las fluctuaciones de gran escala (*large-scale fading* o *shadowing*) debidas al sombreado por obstáculos. Se modela como una variable aleatoria gaussiana (normal) con media cero y desviación estándar $\sigma$ (en dB).

La pérdida de trayectoria media se puede expresar de forma general mediante un modelo exponencial:

$$\overline{PL}(d) \text{ [dB]} = \overline{PL}(d_0) + 10n \log_{10}\left(\frac{d}{d_0}\right)$$

donde:

- $\overline{PL}(d_0)$ es la pérdida de trayectoria medida o calculada a una distancia de referencia $d_0$ (típicamente $d_0 = 1$ m para interiores o $d_0 = 1$ km para exteriores).
- $n$ es el **exponente de pérdida de trayectoria** (*path loss exponent*), que caracteriza la tasa a la cual la señal se atenúa con la distancia. En espacio libre, $n = 2$. En entornos urbanos densos, $n$ puede variar entre 2.7 y 5. En interiores, depende del tipo de edificio, con valores típicos entre 1.6 (corredores con efecto de guía de onda) y 6 (ambientes con múltiples pisos y paredes).

#### 2.3.3 Desvanecimiento por Sombra (Shadowing Log-Normal)

El término $X_{\sigma}$ en el modelo general de pérdida de trayectoria captura las variaciones de la señal causadas por el *shadowing* (sombreado), es decir, la presencia variable de obstáculos grandes (edificios, colinas) entre el transmisor y el receptor en diferentes ubicaciones. Cuando un móvil se desplaza a lo largo de una ruta en un entorno urbano, la señal recibida varía lentamente a medida que pasa detrás de edificios o emerge a zonas más abiertas.

Extensas campañas de medición han demostrado que estas variaciones de la señal, expresadas en dB, siguen una distribución gaussiana (normal). Esto equivale a decir que la potencia recibida (en unidades lineales, como mW) sigue una distribución log-normal. Por esta razón, el fenómeno se denomina **desvanecimiento log-normal** o *log-normal shadowing*.

La función de densidad de probabilidad de $X_{\sigma}$ es:

$$f_{X_{\sigma}}(x) = \frac{1}{\sigma\sqrt{2\pi}} \exp\left(-\frac{x^2}{2\sigma^2}\right)$$

donde $\sigma$ es la desviación estándar del shadowing, medida en dB. Los valores típicos de $\sigma$ son:

- **Entornos urbanos macro-celulares:** $\sigma = 6$ a 10 dB.
- **Entornos suburbanos:** $\sigma = 4$ a 8 dB.
- **Entornos interiores:** $\sigma = 3$ a 6 dB.

**Margen de desvanecimiento (*fade margin*):**

En la planificación de redes, es necesario garantizar que la señal recibida sea superior al umbral mínimo de sensibilidad del receptor durante un porcentaje determinado del tiempo y del área de cobertura. Para ello, se añade un margen de desvanecimiento $M_{\text{fade}}$ al presupuesto de enlace.

Si se desea que la probabilidad de que la señal esté por encima del umbral sea $P_{\text{cob}}$ (por ejemplo, 90% o 95%), el margen de desvanecimiento se calcula como:

$$M_{\text{fade}} = Q^{-1}(1 - P_{\text{cob}}) \cdot \sigma$$

donde $Q^{-1}$ es la función inversa de la función Q (complementaria de la distribución normal acumulada). Para probabilidades de cobertura comunes:

| Probabilidad de cobertura $P_{\text{cob}}$ | $Q^{-1}(1 - P_{\text{cob}})$ | Margen ($\sigma = 8$ dB) |
|:---:|:---:|:---:|
| 50% | 0 | 0 dB |
| 75% | 0.674 | 5.4 dB |
| 90% | 1.282 | 10.3 dB |
| 95% | 1.645 | 13.2 dB |
| 99% | 2.326 | 18.6 dB |

**Ejemplo numérico 2.4:** Una estación base celular debe proporcionar cobertura con una probabilidad del 90% en el borde de la celda. La desviación estándar del shadowing es $\sigma = 8$ dB. ¿Cuál es el margen de desvanecimiento necesario?

$$M_{\text{fade}} = 1.282 \times 8 = 10.26 \text{ dB}$$

Esto significa que la potencia de la señal media en el borde de la celda debe ser 10.26 dB superior al nivel mínimo de sensibilidad del receptor para garantizar que el 90% de las ubicaciones en el borde de la celda tengan una señal adecuada.

---

## 3. Modelos de Propagación en Exteriores

### 3.1 Modelo Okumura-Hata

#### 3.1.1 Contexto Histórico

El modelo de Okumura-Hata es uno de los modelos empíricos de propagación más ampliamente utilizados en la planificación de redes celulares. Su desarrollo se remonta a las extensas campañas de medición realizadas por Yoshihisa Okumura y sus colaboradores en la ciudad de Tokio durante la década de 1960. Okumura realizó mediciones detalladas de la intensidad de señal en la banda de 100 MHz a 3 GHz a diversas distancias de estaciones base con diferentes alturas de antena. Los resultados, publicados en 1968, se presentaron en forma de curvas gráficas de atenuación media relativa al espacio libre, parametrizadas por frecuencia, distancia, alturas de antena y tipo de entorno.

En 1980, Masaharu Hata formuló una serie de ecuaciones empíricas que aproximaban las curvas gráficas de Okumura, facilitando enormemente su implementación computacional. Estas ecuaciones, conocidas colectivamente como el modelo Okumura-Hata, se convirtieron rápidamente en el estándar de la industria para la planificación de redes celulares en la banda de 150 MHz a 1500 MHz.

#### 3.1.2 Ecuación del Modelo Okumura-Hata

La ecuación de pérdida de trayectoria media del modelo Okumura-Hata para entornos urbanos es:

$$L_{\text{urbano}} \text{ [dB]} = 69.55 + 26.16 \log_{10}(f) - 13.82 \log_{10}(h_b) - a(h_m) + \left[44.9 - 6.55 \log_{10}(h_b)\right] \log_{10}(d)$$

donde:

- $L_{\text{urbano}}$ es la pérdida de trayectoria mediana en entorno urbano, en dB.
- $f$ es la frecuencia de la portadora en MHz. Rango de validez: $150 \leq f \leq 1500$ MHz.
- $h_b$ es la altura efectiva de la antena de la estación base sobre el nivel del suelo, en metros. Rango de validez: $30 \leq h_b \leq 200$ m.
- $h_m$ es la altura de la antena del terminal móvil sobre el nivel del suelo, en metros. Rango de validez: $1 \leq h_m \leq 10$ m.
- $d$ es la distancia entre la estación base y el terminal móvil, en kilómetros. Rango de validez: $1 \leq d \leq 20$ km.
- $a(h_m)$ es el factor de corrección por altura de la antena del móvil, que depende del tipo de entorno.

Analicemos cada término de la ecuación:

- **$69.55$:** Constante de referencia que calibra el modelo al entorno urbano de Tokio.
- **$26.16 \log_{10}(f)$:** Término que captura el aumento de la pérdida con la frecuencia. A mayor frecuencia, mayor atenuación, ya que las ondas de mayor frecuencia sufren más difracción y dispersión.
- **$-13.82 \log_{10}(h_b)$:** Término que modela la reducción de la pérdida al aumentar la altura de la estación base. Una antena más alta "ve" por encima de más obstáculos, mejorando el enlace.
- **$-a(h_m)$:** Factor de corrección que refleja el beneficio de elevar la antena del terminal móvil.
- **$[44.9 - 6.55 \log_{10}(h_b)] \log_{10}(d)$:** Término que describe cómo la pérdida aumenta con la distancia. El exponente de pérdida de trayectoria efectivo depende de $h_b$.

#### 3.1.3 Factor de Corrección $a(h_m)$

El factor de corrección $a(h_m)$ varía según el tamaño de la ciudad:

**Para ciudades medianas y pequeñas:**

$$a(h_m) = (1.1 \log_{10}(f) - 0.7)h_m - (1.56 \log_{10}(f) - 0.8) \quad \text{[dB]}$$

**Para ciudades grandes (a frecuencias $f \leq 300$ MHz):**

$$a(h_m) = 8.29 [\log_{10}(1.54 \, h_m)]^2 - 1.1 \quad \text{[dB]}$$

**Para ciudades grandes (a frecuencias $f \geq 300$ MHz):**

$$a(h_m) = 3.2 [\log_{10}(11.75 \, h_m)]^2 - 4.97 \quad \text{[dB]}$$

Para entornos suburbanos, la pérdida se corrige como:

$$L_{\text{suburbano}} = L_{\text{urbano}} - 2\left[\log_{10}\left(\frac{f}{28}\right)\right]^2 - 5.4 \quad \text{[dB]}$$

Para entornos rurales abiertos:

$$L_{\text{rural}} = L_{\text{urbano}} - 4.78 [\log_{10}(f)]^2 + 18.33 \log_{10}(f) - 40.94 \quad \text{[dB]}$$

#### 3.1.4 Ejemplo Numérico Completo

**Ejemplo 3.1 (Ciudad mediana):** Calcular la pérdida de trayectoria para un enlace celular GSM 900 con los siguientes parámetros: $f = 900$ MHz, $h_b = 40$ m, $h_m = 1.5$ m, $d = 5$ km, en una ciudad mediana.

Paso 1: Calcular el factor de corrección $a(h_m)$ para ciudad mediana:

$$a(h_m) = (1.1 \log_{10}(900) - 0.7) \times 1.5 - (1.56 \log_{10}(900) - 0.8)$$

$$= (1.1 \times 2.954 - 0.7) \times 1.5 - (1.56 \times 2.954 - 0.8)$$

$$= (3.250 - 0.7) \times 1.5 - (4.608 - 0.8)$$

$$= 2.550 \times 1.5 - 3.808 = 3.825 - 3.808 = 0.017 \text{ dB}$$

Paso 2: Calcular cada término de la ecuación principal:

$$69.55 + 26.16 \log_{10}(900) = 69.55 + 26.16 \times 2.954 = 69.55 + 77.28 = 146.83$$

$$13.82 \log_{10}(40) = 13.82 \times 1.602 = 22.14$$

$$[44.9 - 6.55 \log_{10}(40)] \log_{10}(5) = [44.9 - 6.55 \times 1.602] \times 0.699$$

$$= [44.9 - 10.49] \times 0.699 = 34.41 \times 0.699 = 24.06$$

Paso 3: Calcular la pérdida total:

$$L_{\text{urbano}} = 146.83 - 22.14 - 0.017 + 24.06 = 148.73 \text{ dB}$$

**Ejemplo 3.2 (Gran ciudad):** Con los mismos parámetros pero para una gran ciudad ($f = 900$ MHz $\geq 300$ MHz):

$$a(h_m) = 3.2[\log_{10}(11.75 \times 1.5)]^2 - 4.97$$

$$= 3.2[\log_{10}(17.625)]^2 - 4.97 = 3.2 \times [1.246]^2 - 4.97$$

$$= 3.2 \times 1.553 - 4.97 = 4.97 - 4.97 = 0.0 \text{ dB}$$

En este caso, la pérdida para gran ciudad resulta:

$$L_{\text{urbano}} = 146.83 - 22.14 - 0.0 + 24.06 = 148.75 \text{ dB}$$

La diferencia entre ciudad mediana y gran ciudad es mínima para $h_m = 1.5$ m, pero se hace más significativa para alturas de antena del móvil mayores.

#### 3.1.5 Limitaciones del Modelo

El modelo Okumura-Hata tiene las siguientes limitaciones importantes:

1. **Rango de frecuencia limitado:** Solo es válido para $150 \leq f \leq 1500$ MHz. No es aplicable a redes 3G UMTS (2100 MHz), LTE en bandas altas ni 5G.
2. **Distancia mínima de 1 km:** No es adecuado para microceldas o picoceldas, donde las distancias son menores.
3. **Basado en un entorno específico:** Las mediciones originales se realizaron en Tokio, una ciudad con características urbanas particulares (edificios de alturas relativamente uniformes).
4. **No diferencia entre LoS y NLoS:** El modelo proporciona una pérdida media sin distinguir si existe línea de visión directa o no.

### 3.2 Modelo COST-231 Hata

#### 3.2.1 Extensión del Modelo Hata

Para superar la limitación de frecuencia del modelo Okumura-Hata original, el proyecto europeo COST 231 (*European Cooperative for Scientific and Technical Research*) desarrolló una extensión que amplía el rango de frecuencia hasta 2 GHz. Esta extensión, conocida como modelo COST-231 Hata (o Hata extendido), fue publicada en 1999 y ha sido ampliamente utilizada en la planificación de redes GSM 1800, UMTS y LTE en la banda de 1800-2000 MHz.

#### 3.2.2 Ecuación del Modelo COST-231 Hata

$$L_u \text{ [dB]} = 46.3 + 33.9 \log_{10}(f) - 13.82 \log_{10}(h_b) - a(h_m) + \left[44.9 - 6.55 \log_{10}(h_b)\right] \log_{10}(d) + C_m$$

donde:

- $L_u$ es la pérdida de trayectoria mediana, en dB.
- $f$ es la frecuencia de la portadora en MHz. Rango de validez: $1500 \leq f \leq 2000$ MHz.
- $h_b$ es la altura de la antena de la estación base, en metros. Rango: $30 \leq h_b \leq 200$ m.
- $h_m$ es la altura de la antena del terminal móvil, en metros. Rango: $1 \leq h_m \leq 10$ m.
- $d$ es la distancia, en kilómetros. Rango: $1 \leq d \leq 20$ km.
- $a(h_m)$ es el factor de corrección de la antena del móvil, que se calcula con la misma fórmula que para ciudades medianas del modelo Okumura-Hata:

$$a(h_m) = (1.1 \log_{10}(f) - 0.7) h_m - (1.56 \log_{10}(f) - 0.8)$$

- $C_m$ es el factor de corrección metropolitano:
  - $C_m = 0$ dB para ciudades medianas y áreas suburbanas.
  - $C_m = 3$ dB para centros metropolitanos (grandes ciudades).

**Comparación de las constantes con el modelo Okumura-Hata original:**

| Constante | Okumura-Hata | COST-231 Hata |
|:---:|:---:|:---:|
| Término constante | 69.55 | 46.3 |
| Coeficiente de $\log_{10}(f)$ | 26.16 | 33.9 |
| Coeficiente de $\log_{10}(h_b)$ | $-13.82$ | $-13.82$ |
| Exponente de distancia | $44.9 - 6.55\log_{10}(h_b)$ | $44.9 - 6.55\log_{10}(h_b)$ |
| Corrección metropolitana | Implícita en $a(h_m)$ | $C_m$ explícito |

Las principales diferencias son la constante de referencia y el coeficiente de frecuencia, que se ajustaron para reflejar la mayor atenuación a frecuencias más altas.

#### 3.2.3 Ejemplo Numérico Completo

**Ejemplo 3.3:** Calcular la pérdida de trayectoria para un enlace UMTS a 2000 MHz con: $h_b = 50$ m, $h_m = 1.5$ m, $d = 3$ km, en una ciudad mediana ($C_m = 0$ dB).

Paso 1: Factor de corrección $a(h_m)$:

$$a(h_m) = (1.1 \log_{10}(2000) - 0.7) \times 1.5 - (1.56 \log_{10}(2000) - 0.8)$$

$$= (1.1 \times 3.301 - 0.7) \times 1.5 - (1.56 \times 3.301 - 0.8)$$

$$= (3.631 - 0.7) \times 1.5 - (5.150 - 0.8)$$

$$= 2.931 \times 1.5 - 4.350 = 4.397 - 4.350 = 0.047 \text{ dB}$$

Paso 2: Calcular cada término:

$$46.3 + 33.9 \log_{10}(2000) = 46.3 + 33.9 \times 3.301 = 46.3 + 111.90 = 158.20$$

$$13.82 \log_{10}(50) = 13.82 \times 1.699 = 23.48$$

$$[44.9 - 6.55 \log_{10}(50)] \log_{10}(3) = [44.9 - 6.55 \times 1.699] \times 0.477$$

$$= [44.9 - 11.13] \times 0.477 = 33.77 \times 0.477 = 16.11$$

Paso 3: Pérdida total:

$$L_u = 158.20 - 23.48 - 0.047 + 16.11 + 0 = 150.78 \text{ dB}$$

Si el mismo cálculo se realizara para un centro metropolitano ($C_m = 3$ dB):

$$L_u = 150.78 + 3 = 153.78 \text{ dB}$$

La diferencia de 3 dB entre ciudad mediana y centro metropolitano corresponde a una reducción del 50% en la potencia recibida, lo que se traduce en una reducción significativa del radio de cobertura.

### 3.3 Modelo 3GPP TR 38.901 (5G NR)

#### 3.3.1 Contexto: Rangos de Frecuencia FR1 y FR2

El 3rd Generation Partnership Project (3GPP) ha desarrollado un modelo de canal completo para 5G NR documentado en el informe técnico TR 38.901, que cubre frecuencias desde 0.5 GHz hasta 100 GHz. Este modelo supera las limitaciones de frecuencia de los modelos clásicos y es esencial para el diseño de redes 5G tanto en el rango de frecuencias Sub-6 GHz (FR1: 410 MHz – 7125 MHz) como en ondas milimétricas (FR2: 24.25 GHz – 52.6 GHz).

El modelo define varios escenarios de despliegue, cada uno con ecuaciones de pérdida de trayectoria específicas para condiciones de línea de visión (LoS) y sin línea de visión (NLoS):

- **UMa (Urban Macro):** Estaciones base macro-celulares en entornos urbanos, con altenas típicamente a 25 m de altura.
- **UMi-Street Canyon (Urban Micro):** Estaciones base de baja potencia en entornos urbanos, con antenas a nivel de azoteas de edificios bajos (típicamente 10 m). Los usuarios están en calles tipo cañón.
- **RMa (Rural Macro):** Entornos rurales con baja densidad de obstáculos.
- **InH (Indoor Hotspot):** Entornos interiores tipo oficina abierta.

#### 3.3.2 Modelo UMi-Street Canyon

Para el escenario **UMi-Street Canyon**, las ecuaciones de pérdida de trayectoria son:

**Condición LoS:**

$$PL_{\text{UMi-LoS}} \text{ [dB]} = \begin{cases} PL_1 & \text{si } 10 \text{ m} \leq d_{2D} \leq d'_{BP} \\ PL_2 & \text{si } d'_{BP} < d_{2D} \leq 5000 \text{ m} \end{cases}$$

donde:

$$PL_1 = 32.4 + 21 \log_{10}(d_{3D}) + 20 \log_{10}(f_c)$$

$$PL_2 = 32.4 + 40 \log_{10}(d_{3D}) + 20 \log_{10}(f_c) - 9.5\log_{10}\left[(d'_{BP})^2 + (h_{BS} - h_{UT})^2\right]$$

La **distancia de punto de quiebre** (*breakpoint distance*) $d'_{BP}$ marca la transición entre dos regímenes de propagación:

$$d'_{BP} = \frac{4 \, h'_{BS} \, h'_{UT} \, f_c}{c}$$

donde:

- $d_{2D}$ es la distancia horizontal entre estación base y usuario, en metros.
- $d_{3D} = \sqrt{d_{2D}^2 + (h_{BS} - h_{UT})^2}$ es la distancia tridimensional en metros.
- $f_c$ es la frecuencia de la portadora en GHz.
- $h_{BS}$ es la altura de la estación base (valor por defecto: 10 m).
- $h_{UT}$ es la altura del terminal de usuario (valor por defecto: 1.5 m).
- $h'_{BS} = h_{BS} - h_E$ y $h'_{UT} = h_{UT} - h_E$ son las alturas efectivas de las antenas, donde $h_E = 1.0$ m es la altura efectiva del entorno.
- $c = 3 \times 10^8$ m/s es la velocidad de la luz.

Para distancias menores que $d'_{BP}$, el exponente de pérdida es 2.1 (similar al espacio libre), mientras que para distancias mayores, el exponente aumenta a 4.0, reflejando la fuerte atenuación debida a reflexiones en el suelo que interfieren destructivamente con la señal directa.

**Condición NLoS:**

$$PL_{\text{UMi-NLoS}} \text{ [dB]} = \max(PL_{\text{UMi-LoS}}, PL'_{\text{UMi-NLoS}})$$

donde:

$$PL'_{\text{UMi-NLoS}} = 22.4 + 35.3 \log_{10}(d_{3D}) + 21.3 \log_{10}(f_c) - 0.3(h_{UT} - 1.5)$$

La desviación estándar del shadowing es $\sigma_{SF} = 4.0$ dB para LoS y $\sigma_{SF} = 7.82$ dB para NLoS.

#### 3.3.3 Modelo UMa

Para el escenario **UMa** (Urban Macro), con $h_{BS} = 25$ m:

**LoS:**

$$PL_1 = 28.0 + 22\log_{10}(d_{3D}) + 20\log_{10}(f_c)$$

$$PL_2 = 28.0 + 40\log_{10}(d_{3D}) + 20\log_{10}(f_c) - 9\log_{10}\left[(d'_{BP})^2 + (h_{BS} - h_{UT})^2\right]$$

con $d'_{BP} = 4 \, h'_{BS} \, h'_{UT} \, f_c / c$, donde la altura efectiva del entorno $h_E$ se calcula con una distribución probabilística condicionada a la distancia.

**NLoS:**

$$PL_{\text{UMa-NLoS}} = \max(PL_{\text{UMa-LoS}}, PL'_{\text{UMa-NLoS}})$$

$$PL'_{\text{UMa-NLoS}} = 13.54 + 39.08\log_{10}(d_{3D}) + 20\log_{10}(f_c) - 0.6(h_{UT} - 1.5)$$

#### 3.3.4 Modelo RMa

Para el escenario **RMa** (Rural Macro), el modelo considera alturas de antena de estación base más elevadas ($h_{BS} = 35$ m) y distancias mayores:

**LoS:**

$$PL_1 = 20\log_{10}\left(\frac{40\pi d_{3D} f_c}{3}\right) + \min(0.03h^{1.72}, 10)\log_{10}(d_{3D}) - \min(0.044h^{1.72}, 14.77) + 0.002\log_{10}(h) d_{3D}$$

donde $h$ es la altura media de los edificios del entorno (por defecto $h = 5$ m).

#### 3.3.5 Probabilidad LoS/NLoS

El modelo 3GPP TR 38.901 también define la probabilidad de que un usuario se encuentre en condición LoS en función de la distancia $d_{2D}$. Para UMi-Street Canyon:

$$P_{\text{LoS}} = \begin{cases} 1 & \text{si } d_{2D} \leq 18 \text{ m} \\ \frac{18}{d_{2D}} + \exp\left(-\frac{d_{2D}}{36}\right)\left(1 - \frac{18}{d_{2D}}\right) & \text{si } d_{2D} > 18 \text{ m} \end{cases}$$

Esta función decrece rápidamente con la distancia: a 50 m, $P_{\text{LoS}} \approx 0.63$; a 200 m, $P_{\text{LoS}} \approx 0.10$.

#### 3.3.6 Ejemplo Numérico para UMi-LoS

**Ejemplo 3.4:** Calcular la pérdida de trayectoria para un enlace 5G NR UMi-LoS con: $f_c = 3.5$ GHz (FR1), $h_{BS} = 10$ m, $h_{UT} = 1.5$ m, $d_{2D} = 200$ m, $h_E = 1.0$ m.

Paso 1: Calcular alturas efectivas:

$$h'_{BS} = 10 - 1.0 = 9.0 \text{ m}$$

$$h'_{UT} = 1.5 - 1.0 = 0.5 \text{ m}$$

Paso 2: Calcular la distancia de punto de quiebre:

$$d'_{BP} = \frac{4 \times 9.0 \times 0.5 \times 3.5 \times 10^9}{3 \times 10^8} = \frac{63 \times 10^9}{3 \times 10^8} = 210 \text{ m}$$

Paso 3: Verificar la condición. Como $d_{2D} = 200$ m $\leq d'_{BP} = 210$ m, usamos $PL_1$.

Paso 4: Calcular $d_{3D}$:

$$d_{3D} = \sqrt{200^2 + (10 - 1.5)^2} = \sqrt{40000 + 72.25} = \sqrt{40072.25} = 200.18 \text{ m}$$

Paso 5: Calcular $PL_1$:

$$PL_1 = 32.4 + 21 \log_{10}(200.18) + 20 \log_{10}(3.5)$$

$$= 32.4 + 21 \times 2.3014 + 20 \times 0.5441$$

$$= 32.4 + 48.33 + 10.88 = 91.61 \text{ dB}$$

Este valor es significativamente menor que los $\sim$148 dB obtenidos con Okumura-Hata a 5 km, lo que refleja tanto la menor distancia como la condición favorable de LoS. A 200 m, la señal 5G a 3.5 GHz tiene una pérdida moderada que permite tasas de datos muy altas.

**[Descripción de Figura 3.1]:** *Gráfico de pérdida de trayectoria (eje Y, en dB, de 60 a 180 dB) versus distancia logarítmica (eje X, de 10 m a 5 km). Se trazan cinco curvas: (1) Espacio libre a 3.5 GHz (línea punteada gris), (2) UMi-LoS a 3.5 GHz (línea sólida azul), (3) UMi-NLoS a 3.5 GHz (línea sólida roja), (4) UMa-LoS a 3.5 GHz (línea discontinua verde), (5) UMa-NLoS a 3.5 GHz (línea discontinua naranja). Se marca la distancia de punto de quiebre $d'_{BP}$ con una línea vertical punteada para cada escenario LoS, mostrando el cambio de pendiente. Leyenda en la esquina superior izquierda. Nota al pie indicando: "Modelo 3GPP TR 38.901, $h_{BS} = 10$ m (UMi) / 25 m (UMa), $h_{UT} = 1.5$ m".*

---

## 4. Modelos de Propagación en Interiores

### 4.1 Recomendación ITU-R P.1238-11

#### 4.1.1 Introducción

La Recomendación ITU-R P.1238 (*Propagation data and prediction methods for the planning of indoor radiocommunication systems and radio local area networks in the frequency range 300 MHz to 450 GHz*) es el estándar internacional de la Unión Internacional de Telecomunicaciones (UIT) para la predicción de pérdida de trayectoria en entornos interiores. La versión más reciente (P.1238-11, de 2021) amplía el rango de frecuencia para incluir bandas de ondas milimétricas, relevantes para 5G NR y WiGig (802.11ad/ay) a 60 GHz.

#### 4.1.2 Ecuación del Modelo

La pérdida de trayectoria total según la Recomendación ITU-R P.1238 se calcula como:

$$L_{\text{total}} \text{ [dB]} = 20 \log_{10}(f) + N \log_{10}(d) + L_f(n) - 28$$

donde:

- $L_{\text{total}}$ es la pérdida de trayectoria total en dB.
- $f$ es la frecuencia en MHz.
- $d$ es la distancia entre transmisor y receptor en metros (con $d > 1$ m).
- $N$ es el **coeficiente de pérdida por distancia** (*distance power loss coefficient*), que reemplaza al exponente $10n$ del modelo general. Es un factor empírico que depende del tipo de entorno y la frecuencia. El valor de $N$ determina la tasa de decaimiento de la señal con la distancia.
- $L_f(n)$ es el **factor de penetración de pisos** (*floor penetration loss factor*) en dB, que representa la atenuación adicional causada al atravesar $n$ pisos del edificio. Su valor depende del número de pisos $n$, la frecuencia y el tipo de edificio.
- $-28$ es una constante de calibración en dB.

#### 4.1.3 Valores Típicos de N

Los valores típicos del coeficiente de pérdida por distancia $N$ para diferentes entornos y frecuencias, según la Recomendación ITU-R P.1238-11, son:

| Entorno | Frecuencia | $N$ |
|:---|:---:|:---:|
| Oficina | 900 MHz | 33 |
| Oficina | 2.4 GHz | 30 |
| Oficina | 5 GHz | 31 |
| Oficina | 6 GHz | 31 |
| Oficina | 28 GHz | 32.7 |
| Oficina | 60 GHz | 20.9 |
| Residencial | 2.4 GHz | 28 |
| Residencial | 5 GHz | 28 |
| Residencial | 6 GHz | 28 |
| Comercio/Fábrica | 2.4 GHz | 22 |
| Comercio/Fábrica | 5 GHz | 22 |
| Comercio/Fábrica | 6 GHz | 23 |
| Corredor (mismo piso) | 900 MHz | 20 |
| Corredor (mismo piso) | 2.4 GHz | 20 |

Un valor de $N = 31$ para una oficina a 5 GHz indica un exponente de pérdida de trayectoria de $n = N/10 = 3.1$, significativamente mayor que el valor de espacio libre ($n = 2$). Este incremento refleja la atenuación adicional causada por paredes, muebles, divisiones y otros elementos propios del entorno de oficina.

#### 4.1.4 Valores de $L_f(n)$

El factor de penetración de pisos representa la atenuación acumulada al atravesar múltiples pisos de un edificio. Valores típicos:

| Tipo de edificio | Frecuencia | $L_f(1)$ | $L_f(2)$ | $L_f(3)$ |
|:---|:---:|:---:|:---:|:---:|
| Oficina | 2.4 GHz | 15 dB | 19 dB | 24 dB |
| Oficina | 5 GHz | 16 dB | 22 dB | 28 dB |
| Residencial | 2.4 GHz | 10 dB | 14 dB | 18 dB |
| Comercial | 5 GHz | 18 dB | 25 dB | — |

Se observa que la pérdida por piso no es lineal: la atenuación del segundo piso es menor que la del primero, lo que se atribuye a que las trayectorias de señal entre pisos distantes tienden a utilizar caminos indirectos (como escaleras, ductos de ventilación) que no sufren la misma atenuación que la penetración directa a través del suelo/techo.

#### 4.1.5 Ejemplo Numérico Completo

**Ejemplo 4.1:** Calcular la pérdida de trayectoria en una oficina a 5 GHz para un punto de acceso Wi-Fi y un terminal ubicado en el mismo piso a 30 metros de distancia.

Datos: $f = 5000$ MHz, $N = 31$, $d = 30$ m, $n = 0$ pisos (mismo piso, $L_f(0) = 0$).

$$L_{\text{total}} = 20 \log_{10}(5000) + 31 \times \log_{10}(30) + 0 - 28$$

$$= 20 \times 3.699 + 31 \times 1.477 + 0 - 28$$

$$= 73.98 + 45.79 - 28 = 91.77 \text{ dB}$$

Ahora, si el terminal está en un piso diferente ($n = 1$, $L_f(1) = 16$ dB):

$$L_{\text{total}} = 73.98 + 45.79 + 16 - 28 = 107.77 \text{ dB}$$

La diferencia de 16 dB entre mismo piso y un piso de diferencia es significativa: equivale a reducir la potencia recibida por un factor de $10^{1.6} \approx 40$.

**[Descripción de Figura 4.1]:** *Gráfico de pérdida de trayectoria indoor (eje Y, de 40 a 130 dB) versus distancia (eje X, logarítmica, de 1 m a 100 m). Se trazan cuatro curvas para un entorno de oficina a 5 GHz: (1) mismo piso (línea azul sólida), (2) 1 piso de diferencia (línea verde discontinua), (3) 2 pisos de diferencia (línea naranja punteada), (4) espacio libre a 5 GHz como referencia (línea gris punteada fina). La separación entre las curvas refleja el factor $L_f(n)$. Leyenda indicando cada curva. Título: "Modelo ITU-R P.1238 — Pérdida de trayectoria en oficina a 5 GHz".*

### 4.2 Modelos IEEE 802.11 (TGax y TGbe)

#### 4.2.1 Introducción

Los grupos de trabajo IEEE 802.11ax (TGax, responsable de Wi-Fi 6/6E) y 802.11be (TGbe, responsable de Wi-Fi 7) han adoptado modelos de canal específicos para evaluar el rendimiento de sus estándares. Estos modelos, basados en los modelos de canal IEEE 802.11 desarrollados originalmente para 802.11n/ac, definen escenarios residenciales y empresariales con parámetros de propagación detallados.

#### 4.2.2 Escenario Residencial (TGax Residential)

El modelo de propagación para el escenario residencial se basa en el modelo de penetración de paredes:

$$PL(d) \text{ [dB]} = 40.05 + 20 \log_{10}\left(\frac{f_c}{2.4}\right) + 20\log_{10}(\min(d, 5)) + \begin{cases} 0 & d \leq 5 \\ 35\log_{10}\left(\frac{d}{5}\right) & d > 5 \end{cases}$$

donde $f_c$ es la frecuencia en GHz y $d$ es la distancia en metros. Este modelo presenta un cambio de pendiente a 5 metros: dentro de esa distancia, el exponente de pérdida es 2.0 (similar a espacio libre dentro de una habitación); más allá, el exponente aumenta a 3.5, reflejando la penetración de paredes interiores.

La desviación estándar del shadowing es $\sigma = 7$ dB para el escenario residencial.

#### 4.2.3 Escenario Empresarial (Enterprise)

Para el escenario empresarial (oficina de planta abierta con cubículos), el modelo es:

$$PL(d) \text{ [dB]} = 40.05 + 20 \log_{10}\left(\frac{f_c}{2.4}\right) + 20\log_{10}(\min(d, 10)) + \begin{cases} 0 & d \leq 10 \\ 35\log_{10}\left(\frac{d}{10}\right) & d > 10 \end{cases}$$

La distancia de quiebre aumenta a 10 metros, reflejando que en oficinas abiertas hay menos paredes interiores que en residencias. La desviación estándar del shadowing es $\sigma = 7$ dB.

#### 4.2.4 Atenuación por Materiales

Una parte fundamental de la modelación de propagación en interiores es la atenuación que sufre la señal al atravesar diferentes materiales de construcción. Los valores varían significativamente con la frecuencia y el tipo de material:

| Material | Espesor típico | Atenuación a 2.4 GHz | Atenuación a 5 GHz | Atenuación a 6 GHz |
|:---|:---:|:---:|:---:|:---:|
| Pared de yeso (drywall) | 12 cm | 3-5 dB | 4-7 dB | 5-8 dB |
| Pared de ladrillo | 20 cm | 5-8 dB | 8-12 dB | 9-14 dB |
| Pared de hormigón | 15-20 cm | 10-15 dB | 15-20 dB | 17-23 dB |
| Puerta de madera | 4 cm | 3-4 dB | 4-6 dB | 5-7 dB |
| Ventana simple (vidrio) | 6 mm | 2-3 dB | 3-5 dB | 3-6 dB |
| Vidrio con capa metálica (Low-E) | 6 mm | 8-15 dB | 15-25 dB | 18-28 dB |
| Vidrio con película de protección solar | 6 mm | 20-30 dB | 25-35 dB | 28-40 dB |
| Piso/techo de hormigón | 20-30 cm | 12-18 dB | 18-25 dB | 20-28 dB |
| Panel metálico | — | 30-40 dB | 40-50 dB | 45-55 dB |
| Cuerpo humano | — | 3-5 dB | 5-8 dB | 6-10 dB |

Estos valores son fundamentales para el diseño de redes Wi-Fi, donde las paredes internas definen las fronteras de cobertura de cada punto de acceso.

#### 4.2.5 BSS Coloring como Respuesta a Interferencia Espacial

En despliegues densos de redes Wi-Fi, múltiples puntos de acceso (AP) operan en canales superpuestos, generando interferencia co-canal. El estándar IEEE 802.11ax introdujo el mecanismo de **BSS Coloring** (coloreado del conjunto de servicio básico) como una técnica de reutilización espacial para mitigar este problema.

El concepto básico es asignar un identificador numérico (el "color", un campo de 6 bits en la cabecera del marco PLCP) a cada BSS. Cuando un dispositivo detecta una trama con un color diferente al suyo y cuya potencia recibida está por debajo de un umbral configurable (OBSS/PD threshold, *Overlapping BSS Preamble Detection*), puede considerar que el medio está libre y transmitir simultáneamente. Esto permite la reutilización espacial del espectro cuando la atenuación por propagación entre BSS vecinos es suficiente.

El umbral OBSS/PD se ajusta dinámicamente según la potencia de transmisión. Según el estándar 802.11ax:

$$\text{OBSS/PD}_{\text{max}} \text{ [dBm]} = \max(-82, \min(-62, -82 + (P_{TX,\text{ref}} - P_{TX})))$$

donde $P_{TX,\text{ref}}$ es la potencia de transmisión de referencia (21 dBm para transmisiones no-SRT) y $P_{TX}$ es la potencia de transmisión actual del dispositivo. Este mecanismo vincula la reutilización espacial con la potencia de transmisión, asegurando que las transmisiones de alta potencia sean más conservadoras en la reutilización.

### 4.3 Modelo de Pérdida por Materiales y Link Budget Indoor

#### 4.3.1 Modelo de Pérdida por Materiales

Un enfoque más detallado para la propagación en interiores consiste en modelar explícitamente la atenuación causada por cada obstáculo que la señal debe atravesar. Este modelo se expresa como:

$$L \text{ [dB]} = L_0 + 10n \log_{10}(d) + \sum_{i} L_{\text{wall},i} + L_{\text{floor}}$$

donde:

- $L_0$ es la pérdida de referencia a 1 metro (en dB). Se calcula típicamente como la FSPL a 1 metro: $L_0 = 20\log_{10}(f) + 20\log_{10}\left(\frac{4\pi}{c}\right) = 20\log_{10}(f_{\text{MHz}}) - 27.56$.
- $n$ es el exponente de pérdida de trayectoria (típicamente entre 2.0 y 3.0 para ambientes interiores sin paredes obstruyendo).
- $d$ es la distancia en metros.
- $\sum_{i} L_{\text{wall},i}$ es la suma de las atenuaciones de cada pared que la señal atraviesa en su trayectoria directa.
- $L_{\text{floor}}$ es la atenuación por penetración de piso(s), si transmisor y receptor están en pisos diferentes.

#### 4.3.2 Tabla de Pérdidas por Material

La siguiente tabla resume las pérdidas por material más utilizadas en el diseño de redes Wi-Fi:

| Material | Pérdida a 2.4 GHz | Pérdida a 5 GHz | Pérdida a 6 GHz |
|:---|:---:|:---:|:---:|
| Pared ligera (yeso/drywall) | 4 dB | 6 dB | 7 dB |
| Pared de ladrillo | 7 dB | 10 dB | 12 dB |
| Pared de hormigón armado | 12 dB | 18 dB | 20 dB |
| Puerta de madera | 3 dB | 5 dB | 6 dB |
| Puerta metálica | 15 dB | 20 dB | 22 dB |
| Ventana (vidrio simple) | 3 dB | 4 dB | 5 dB |
| Ventana (vidrio Low-E) | 12 dB | 20 dB | 23 dB |
| Piso/techo de hormigón | 15 dB | 20 dB | 23 dB |

#### 4.3.3 Ejemplo Completo de Link Budget Indoor

**Ejemplo 4.2:** Un punto de acceso Wi-Fi 6E opera a 6 GHz con $P_T = 18$ dBm y antena interna con $G_T = 4$ dBi. El terminal de usuario tiene una ganancia de antena $G_R = 0$ dBi. Se desea calcular la potencia recibida y la viabilidad del enlace a un usuario ubicado a $d = 25$ m del AP, donde la señal debe atravesar 2 paredes de yeso y 1 pared de ladrillo.

Paso 1: Calcular la pérdida de referencia $L_0$ a 1 metro a 6000 MHz:

$$L_0 = 20 \log_{10}(6000) - 27.56 = 20 \times 3.778 - 27.56 = 75.56 - 27.56 = 48.0 \text{ dB}$$

Paso 2: Calcular la pérdida por distancia (usando $n = 2.5$ para oficina con paredes):

$$10 \times 2.5 \times \log_{10}(25) = 25 \times 1.398 = 34.95 \text{ dB}$$

Paso 3: Sumar las pérdidas por paredes:

$$\sum L_{\text{wall}} = 2 \times 7 + 1 \times 12 = 14 + 12 = 26 \text{ dB}$$

Paso 4: Pérdida total de trayectoria:

$$L = 48.0 + 34.95 + 26 = 108.95 \text{ dB}$$

Paso 5: Presupuesto de enlace completo:

$$P_R = P_T + G_T + G_R - L = 18 + 4 + 0 - 108.95 = -86.95 \text{ dBm}$$

Paso 6: Evaluación. ¿Es viable este enlace? La sensibilidad de un terminal Wi-Fi 6E típico es:

- MCS 11 (1024-QAM, 5/6, máxima velocidad): sensibilidad $\approx -54$ dBm. **No viable** ($-86.95 < -54$).
- MCS 7 (256-QAM, 3/4): sensibilidad $\approx -65$ dBm. **No viable**.
- MCS 4 (16-QAM, 3/4): sensibilidad $\approx -73$ dBm. **No viable**.
- MCS 1 (QPSK, 1/2): sensibilidad $\approx -82$ dBm. **No viable**.
- MCS 0 (BPSK, 1/2): sensibilidad $\approx -85$ dBm. **Marginalmente no viable**.

**Conclusión:** A 25 metros con 3 paredes intermedias a 6 GHz, el enlace no es viable para ningún MCS útil. El diseñador de red debería considerar: (a) agregar un punto de acceso adicional más cercano al usuario, (b) reducir el número de paredes en la trayectoria, o (c) utilizar la banda de 5 GHz o 2.4 GHz como alternativa para este enlace.

#### 4.3.4 Relación entre RSSI, SNR y MCS

La **Indicación de Intensidad de Señal Recibida (RSSI)** es la potencia total de la señal recibida, incluyendo señal deseada, interferencia y ruido. En la práctica, el RSSI es la métrica que reportan los dispositivos Wi-Fi y los teléfonos móviles.

La **Relación Señal a Ruido (SNR)** es la diferencia (en dB) entre la potencia de la señal deseada y la potencia del ruido térmico:

$$\text{SNR [dB]} = P_R \text{ [dBm]} - N_{\text{floor}} \text{ [dBm]}$$

El piso de ruido térmico se calcula como:

$$N_{\text{floor}} = -174 + 10 \log_{10}(B) + NF$$

donde:

- $-174$ dBm/Hz es la densidad espectral de potencia del ruido térmico a temperatura ambiente ($T = 290$ K): $kT = 1.38 \times 10^{-23} \times 290 = 4.0 \times 10^{-21}$ W/Hz $= -174$ dBm/Hz.
- $B$ es el ancho de banda del canal en Hz.
- $NF$ es la figura de ruido del receptor en dB (típicamente 5-7 dB para receptores Wi-Fi).

**Ejemplo:** Para un canal Wi-Fi de 80 MHz con $NF = 6$ dB:

$$N_{\text{floor}} = -174 + 10\log_{10}(80 \times 10^6) + 6 = -174 + 79.03 + 6 = -88.97 \text{ dBm}$$

Si la potencia recibida es $P_R = -65$ dBm:

$$\text{SNR} = -65 - (-88.97) = 23.97 \text{ dB}$$

El **Esquema de Modulación y Codificación (MCS)** que puede utilizarse depende directamente del SNR. A mayor SNR, se puede utilizar un MCS más agresivo (mayor orden de modulación y mayor tasa de código), lo que se traduce en mayor velocidad de transmisión. Esta adaptación dinámica se denomina **adaptación de enlace (*link adaptation*)** o *Adaptive Modulation and Coding (AMC)*. El transmisor monitorea continuamente la calidad del canal (a través de retroalimentación del receptor) y selecciona el MCS más alto que garantice una tasa de error de trama aceptable (típicamente FER < 10%).

#### 4.3.5 Capacidad MIMO

La tecnología MIMO (*Multiple-Input Multiple-Output*) utiliza múltiples antenas tanto en el transmisor como en el receptor para crear flujos de datos espaciales independientes, multiplicando la capacidad del enlace. La capacidad teórica de un sistema MIMO se aproxima como:

$$C \approx \min(N_T, N_R) \times B \times \log_2(1 + \text{SNR})$$

donde:

- $C$ es la capacidad del canal en bits por segundo (bps).
- $N_T$ es el número de antenas transmisoras.
- $N_R$ es el número de antenas receptoras.
- $\min(N_T, N_R)$ es el número máximo de flujos espaciales independientes (*spatial streams*) que el sistema puede soportar, asumiendo una matriz de canal de rango completo (decorrelación espacial suficiente entre las antenas).
- $B$ es el ancho de banda del canal en Hz.
- $\text{SNR}$ es la relación señal a ruido lineal (no en dB).

Esta ecuación muestra que MIMO puede, idealmente, multiplicar la capacidad por un factor igual al número mínimo de antenas. Por ejemplo, un sistema Wi-Fi 6 con $4 \times 4$ MIMO ($N_T = N_R = 4$), ancho de banda $B = 160$ MHz y $\text{SNR} = 25$ dB ($\text{SNR}_{\text{lineal}} = 10^{2.5} = 316.2$):

$$C \approx 4 \times 160 \times 10^6 \times \log_2(1 + 316.2)$$

$$= 4 \times 160 \times 10^6 \times 8.31 = 5.32 \times 10^9 \text{ bps} = 5.32 \text{ Gbps}$$

En la práctica, la capacidad real es menor debido a la correlación espacial entre antenas, la sobrecarga de protocolos y las imperfecciones del canal.

#### 4.3.6 Adaptación de Enlace

La adaptación de enlace es el proceso mediante el cual el transmisor ajusta dinámicamente los parámetros de transmisión (MCS, número de flujos espaciales, ancho de banda) en respuesta a las condiciones cambiantes del canal. Este proceso es fundamental para maximizar el *throughput* y mantener la fiabilidad del enlace.

En Wi-Fi 6/6E/7, la adaptación de enlace funciona de la siguiente manera:

1. El transmisor envía tramas de datos con un MCS inicial.
2. El receptor evalúa la calidad de la señal recibida (SNR, tasa de error).
3. El receptor envía retroalimentación al transmisor (implícita, mediante acuse de recibo, o explícita mediante tramas de reporte de canal).
4. El transmisor ajusta el MCS para la siguiente transmisión:
   - Si el SNR es alto y no hay errores, el transmisor puede probar un MCS más alto (mayor velocidad).
   - Si hay errores o el SNR disminuye, el transmisor reduce el MCS (mayor robustez, menor velocidad).

Este mecanismo de adaptación implica que la relación entre la pérdida de trayectoria y la velocidad experimentada por el usuario no es lineal sino escalonada: a medida que el usuario se aleja del punto de acceso, la velocidad se mantiene constante hasta que el SNR cae por debajo del umbral del MCS actual, momento en el cual se produce una transición abrupta al MCS inferior.

### 4.4 Dimensionamiento de Cobertura

#### 4.4.1 Cálculo del Radio de Cobertura

El dimensionamiento de cobertura consiste en determinar el área que un punto de acceso o estación base puede cubrir garantizando un nivel mínimo de servicio. El procedimiento general es:

1. **Definir el nivel mínimo de señal requerido ($P_{R,\text{min}}$):** Esto depende del MCS mínimo aceptable, que a su vez depende de la velocidad de datos mínima requerida.

2. **Calcular el presupuesto de enlace descendente (*downlink link budget*):**

$$P_{R,\text{min}} = P_T + G_T - L_{\text{cables}} + G_R - PL_{\text{max}} - M_{\text{fade}} - M_{\text{interferencia}}$$

3. **Resolver para la pérdida de trayectoria máxima permitida:**

$$PL_{\text{max}} = P_T + G_T - L_{\text{cables}} + G_R - P_{R,\text{min}} - M_{\text{fade}} - M_{\text{interferencia}}$$

4. **Usar el modelo de propagación apropiado para determinar la distancia máxima ($d_{\text{max}}$)** a la cual la pérdida de trayectoria iguala $PL_{\text{max}}$.

5. **Calcular el área de cobertura** como $A = \pi \, d_{\text{max}}^2$ (para una celda circular idealizada).

#### 4.4.2 Ejemplo Completo de Dimensionamiento para Oficina

**Ejemplo 4.3:** Dimensionar la cobertura de un punto de acceso Wi-Fi 6 operando a 5 GHz en una oficina de planta abierta (sin paredes interiores significativas). Requisito: velocidad mínima de 100 Mbps por usuario con un flujo espacial.

**Parámetros del sistema:**

| Parámetro | Valor |
|:---|:---:|
| Potencia de transmisión del AP ($P_T$) | 20 dBm |
| Ganancia de antena del AP ($G_T$) | 4 dBi |
| Pérdida en cables/conectores ($L_{\text{cables}}$) | 1 dB |
| Ganancia de antena del terminal ($G_R$) | 0 dBi |
| Margen de shadowing ($M_{\text{fade}}$, 90%) | 7 dB |
| Margen de interferencia ($M_{\text{interf}}$) | 3 dB |
| Modelo de propagación | ITU-R P.1238 ($N = 31$) |
| Ancho de banda | 80 MHz |
| Figura de ruido del receptor | 6 dB |

**Paso 1:** Determinar el MCS mínimo necesario.

Para lograr 100 Mbps con un flujo espacial en un canal de 80 MHz (factor de muestreo: 234 subportadoras de datos × 3.2 µs de símbolo OFDM), los MCS candidatos según Wi-Fi 6 con 80 MHz, 1 flujo espacial y GI de 800 ns son:

- MCS 7 (64-QAM, 5/6): tasa PHY = 293.1 Mbps → **suficiente**.
- MCS 4 (16-QAM, 3/4): tasa PHY = 175.5 Mbps → **suficiente**.
- MCS 3 (16-QAM, 1/2): tasa PHY = 117.0 Mbps → **suficiente** (margen mínimo).

Seleccionamos **MCS 3** como mínimo, cuya sensibilidad típica es $P_{R,\text{min}} \approx -76$ dBm.

**Paso 2:** Calcular la pérdida de trayectoria máxima:

$$PL_{\text{max}} = P_T + G_T - L_{\text{cables}} + G_R - P_{R,\text{min}} - M_{\text{fade}} - M_{\text{interf}}$$

$$PL_{\text{max}} = 20 + 4 - 1 + 0 - (-76) - 7 - 3 = 89 \text{ dB}$$

**Paso 3:** Calcular el radio de cobertura usando el modelo ITU-R P.1238:

$$PL_{\text{max}} = 20 \log_{10}(f) + N \log_{10}(d_{\text{max}}) - 28$$

$$89 = 20 \log_{10}(5000) + 31 \log_{10}(d_{\text{max}}) - 28$$

$$89 = 73.98 + 31 \log_{10}(d_{\text{max}}) - 28$$

$$89 = 45.98 + 31 \log_{10}(d_{\text{max}})$$

$$31 \log_{10}(d_{\text{max}}) = 89 - 45.98 = 43.02$$

$$\log_{10}(d_{\text{max}}) = \frac{43.02}{31} = 1.388$$

$$d_{\text{max}} = 10^{1.388} = 24.4 \text{ m}$$

**Paso 4:** Calcular el área de cobertura:

$$A = \pi \times d_{\text{max}}^2 = \pi \times 24.4^2 = \pi \times 595.4 = 1870 \text{ m}^2$$

**Paso 5:** Dimensionamiento del número de APs.

Si la oficina tiene un área total de $A_{\text{oficina}} = 5000$ m², el número mínimo de puntos de acceso necesarios es:

$$N_{AP} = \left\lceil \frac{A_{\text{oficina}}}{A} \right\rceil = \left\lceil \frac{5000}{1870} \right\rceil = \lceil 2.67 \rceil = 3 \text{ APs}$$

Sin embargo, en la práctica se recomienda agregar un factor de seguridad del 20-30% y considerar la superposición de cobertura necesaria para roaming suave (*soft handover*), lo que llevaría a un diseño con **4 APs**.

**Paso 6:** Verificación del enlace ascendente (*uplink*).

Es fundamental verificar también el enlace ascendente, ya que los terminales de usuario (smartphones, laptops) tienen menor potencia de transmisión que el AP. Considerando un terminal con $P_{T,\text{UE}} = 15$ dBm (potencia EIRP típica de un smartphone):

$$P_{R,\text{AP}} = 15 + 0 + 4 - 1 - PL(24.4) - 0 = 18 - 89 = -71 \text{ dBm}$$

Si la sensibilidad del AP es similar a la del terminal ($\approx -76$ dBm para MCS 3), el enlace ascendente tiene un margen de $-71 - (-76) = 5$ dB sin considerar los márgenes de desvanecimiento. Descontando los márgenes ($7 + 3 = 10$ dB), el enlace ascendente no cierra con MCS 3 en el borde. Este análisis revela que el enlace ascendente es el enlace limitante, y el radio de cobertura real debería ser menor o el MCS mínimo más bajo.

**[Descripción de Figura 4.2]:** *Plano de planta de una oficina rectangular de 100 m × 50 m (5000 m²). Se muestran 4 puntos de acceso (iconos de AP en azul) distribuidos uniformemente. Cada AP tiene un círculo de cobertura con radio $d_{\text{max}} = 24.4$ m, representado como un área circular semitransparente en azul claro. Los círculos se superponen ligeramente en las zonas de transición (áreas de roaming, coloreadas en verde claro). Las esquinas de la oficina que quedan fuera de cualquier círculo de cobertura están sombreadas en rojo claro, indicando zonas sin cobertura o con cobertura marginal. Una leyenda indica: azul = cobertura garantizada, verde = zona de roaming, rojo = cobertura insuficiente. Dimensiones acotadas en el plano. Escala gráfica en la esquina inferior.*

---

## Referencias

1. T. S. Rappaport, *Wireless Communications: Principles and Practice*, 2nd ed. Upper Saddle River, NJ: Prentice Hall, 2002. ISBN: 978-0130422323.

2. A. Goldsmith, *Wireless Communications*. Cambridge: Cambridge University Press, 2005. DOI: [10.1017/CBO9780511841224](https://doi.org/10.1017/CBO9780511841224).

3. Y. Okumura, E. Ohmori, T. Kawano, and K. Fukuda, "Field strength and its variability in VHF and UHF land-mobile radio service," *Review of the Electrical Communication Laboratory*, vol. 16, no. 9-10, pp. 825–873, Sept.–Oct. 1968.

4. M. Hata, "Empirical formula for propagation loss in land mobile radio services," *IEEE Transactions on Vehicular Technology*, vol. VT-29, no. 3, pp. 317–325, Aug. 1980. DOI: [10.1109/T-VT.1980.23859](https://doi.org/10.1109/T-VT.1980.23859).

5. COST Action 231, "Digital mobile radio towards future generation systems, final report," *European Commission*, EUR 18957, 1999.

6. 3GPP, "Study on channel model for frequencies from 0.5 to 100 GHz," 3GPP TR 38.901, v17.0.0, Mar. 2022. [En línea]. Disponible: https://www.3gpp.org/ftp/Specs/archive/38_series/38.901/

7. ITU-R, "Propagation data and prediction methods for the planning of indoor radiocommunication systems and radio local area networks in the frequency range 300 MHz to 450 GHz," Recommendation ITU-R P.1238-11, 2021.

8. ITU-R, "Attenuation by atmospheric gases and related effects," Recommendation ITU-R P.676-13, 2022.

9. ITU-R, "Specific attenuation model for rain for use in prediction methods," Recommendation ITU-R P.838-3, 2005.

10. IEEE, "IEEE Standard for Information Technology—Telecommunications and Information Exchange Between Systems—Local and Metropolitan Area Networks—Specific Requirements—Part 11: Wireless LAN Medium Access Control (MAC) and Physical Layer (PHY) Specifications—Amendment 1: Enhancements for High-Efficiency WLAN," IEEE Std 802.11ax-2021. DOI: [10.1109/IEEESTD.2021.9442429](https://doi.org/10.1109/IEEESTD.2021.9442429).

11. IEEE 802.11be Task Group, "IEEE P802.11be/D5.0 - Draft Standard for Information Technology—Telecommunications and Information Exchange between Systems Local and Metropolitan Area Networks—Specific Requirements, Part 11: Wireless LAN Medium Access Control (MAC) and Physical Layer (PHY) Specifications, Amendment: Enhancements for Extremely High Throughput (EHT)," 2024.

12. S. Sun et al., "Propagation path loss models for 5G urban micro- and macro-cellular scenarios," in *Proc. IEEE 83rd Vehicular Technology Conference (VTC Spring)*, Nanjing, China, 2016, pp. 1–6. DOI: [10.1109/VTCSpring.2016.7504435](https://doi.org/10.1109/VTCSpring.2016.7504435).

13. T. S. Rappaport et al., "Millimeter wave mobile communications for 5G cellular: It will work!," *IEEE Access*, vol. 1, pp. 335–349, 2013. DOI: [10.1109/ACCESS.2013.2260813](https://doi.org/10.1109/ACCESS.2013.2260813).

---

*Fin de la Parte 1*
