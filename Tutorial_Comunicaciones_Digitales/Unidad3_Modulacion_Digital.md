# Unidad 3: Modulación Digital

## Introducción de la unidad

La modulación digital es el conjunto de técnicas mediante las cuales una secuencia discreta de bits se transforma en una señal analógica apta para propagarse sobre un canal físico. En sistemas móviles, satelitales, Wi-Fi, enlaces ópticos y prácticamente cualquier sistema de comunicaciones moderno, la elección de la modulación determina el compromiso entre **robustez al ruido**, **eficiencia espectral**, **complejidad del receptor** y **requisitos de linealidad del transmisor**.

Desde el punto de vista matemático, la modulación digital conecta tres espacios:

1. el espacio de bits,
2. el espacio de señales temporales, y
3. el espacio geométrico de constelaciones.

Esta unidad desarrolla esa conexión de forma rigurosa y pedagógica. Primero se estudia la representación pasabanda y su equivalente pasabajo complejo; luego se analizan ASK, FSK, PSK y QPSK; posteriormente se profundiza en QAM; finalmente se presenta la teoría de detección óptima y la relación entre geometría de la constelación y probabilidad de error.

**Idea central de la unidad:** una señal modulada puede entenderse como un punto que viaja en el plano complejo, filtrado en el tiempo por un pulso, desplazado en frecuencia por una portadora y observado por un receptor inmerso en ruido.

---

## 3.1 Análisis de Señales Pasabajas y Pasabanda

### 3.1.1 Señales pasabanda y la necesidad de una representación equivalente

Una señal **pasabanda** es aquella cuya energía espectral se concentra alrededor de una frecuencia portadora $f_c \gg 0$. Una representación típica es

$$
s(t)=A(t)\cos\big(2\pi f_c t+\phi(t)\big),
$$

donde $A(t)$ y $\phi(t)$ varían lentamente respecto de la portadora.

Trabajar directamente con $s(t)$ en banda pasante suele ser algebraicamente incómodo. Por ello se introduce una representación **pasabaja equivalente** que traslada toda la información de amplitud y fase a una envolvente compleja alrededor de frecuencia cero.

### 3.1.2 Representación compleja de envolvente

Sea $s(t)$ una señal real. Su **transformada de Hilbert** se define como

$$
\hat{s}(t)=\mathcal{H}\{s(t)\}=\frac{1}{\pi} \operatorname{p.v.}\int_{-\infty}^{\infty}\frac{s(\tau)}{t-\tau}\,d\tau,
$$

donde $\operatorname{p.v.}$ indica el valor principal de Cauchy.

La **señal analítica** asociada a $s(t)$ es

$$
s_a(t)=s(t)+j\hat{s}(t).
$$

En frecuencia,

$$
S_a(f)=
\begin{cases}
2S(f), & f>0,\\
S(0), & f=0,\\
0, & f<0.
\end{cases}
$$

Es decir, la señal analítica elimina las frecuencias negativas y duplica la parte positiva. Con ella definimos la **envolvente compleja**

$$
u(t)=s_a(t)e^{-j2\pi f_c t}.
$$

Entonces la señal pasabanda puede recuperarse como

$$
s(t)=\Re\{u(t)e^{j2\pi f_c t}\}.
$$

Esta ecuación es fundamental: toda la modulación reside en $u(t)$, mientras que $e^{j2\pi f_c t}$ sólo desplaza espectralmente la señal.

**Concepto clave:** la señal real pasabanda $s(t)$ y su equivalente complejo pasabajo $u(t)$ contienen exactamente la misma información, pero $u(t)$ es mucho más conveniente para análisis, simulación y diseño de receptores.

**[Figura 3.1]:** representación conceptual de una señal pasabanda senoidal cuya amplitud y fase cambian lentamente, acompañada de su envolvente compleja en el plano $I$-$Q$. La figura debe mostrar arriba una oscilación rápida alrededor de cero, y abajo una trayectoria compleja suave que gira y cambia de radio. El mensaje visual importante es que la oscilación de alta frecuencia “se factoriza” y la información útil queda encapsulada en una señal compleja de baja frecuencia.

### 3.1.3 Componentes en fase (I) y cuadratura (Q)

La envolvente compleja puede descomponerse como

$$
u(t)=I(t)+jQ(t).
$$

Por tanto,

$$
s(t)=I(t)\cos(2\pi f_c t)-Q(t)\sin(2\pi f_c t).
$$

Las funciones $I(t)$ y $Q(t)$ se denominan, respectivamente, **componente en fase** e **componente en cuadratura**. Geométricamente, son las coordenadas cartesianas del símbolo en el plano complejo. Si escribimos

$$
u(t)=\rho(t)e^{j\theta(t)},
$$

entonces

$$
I(t)=\rho(t)\cos\theta(t),
\qquad
Q(t)=\rho(t)\sin\theta(t),
$$

y la señal pasabanda es

$$
s(t)=\rho(t)\cos\big(2\pi f_c t+\theta(t)\big).
$$

Por ello:

- variar $\rho(t)$ implica **modulación de amplitud**,
- variar $\theta(t)$ implica **modulación de fase**,
- variar la derivada de fase $\frac{1}{2\pi}\frac{d\theta}{dt}$ implica **modulación de frecuencia**.

### 3.1.4 Conversión pasabanda a pasabajas equivalente

La conversión pasabanda a pasabajo equivalente se realiza multiplicando por una exponencial compleja conjugada y filtrando pasabajo:

$$
u(t)=\operatorname{LPF}\{2s(t)e^{-j2\pi f_c t}\}.
$$

Separando partes real e imaginaria,

$$
I(t)=\operatorname{LPF}\{2s(t)\cos(2\pi f_c t)\},
$$

$$
Q(t)=\operatorname{LPF}\{-2s(t)\sin(2\pi f_c t)\}.
$$

Este resultado es el fundamento de los moduladores y demoduladores en cuadratura usados en SDR, LTE, 5G y Wi-Fi.

En frecuencia, si $U(f)$ es la transformada de Fourier de $u(t)$, entonces la señal real pasabanda posee espectro

$$
S(f)=\frac{1}{2}U(f-f_c)+\frac{1}{2}U^*(-f-f_c).
$$

Así, el espectro pasabajo se traslada a $\pm f_c$, generando las dos bandas laterales conjugadas requeridas para que la señal temporal sea real.

### 3.1.5 Representación compleja de señales moduladas lineales

En una modulación lineal digital, la envolvente compleja suele escribirse como

$$
u(t)=\sum_{k} a_k p(t-kT_s),
$$

donde:

- $a_k$ es el símbolo complejo transmitido,
- $p(t)$ es el pulso conformador,
- $T_s$ es el período de símbolo.

Entonces la señal pasabanda real es

$$
s(t)=\Re\left\{\left(\sum_k a_k p(t-kT_s)\right)e^{j2\pi f_c t}\right\}.
$$

Toda modulación lineal bidimensional (QPSK, M-QAM, OQPSK, etc.) puede analizarse con esta ecuación. Si $a_k=a_{I,k}+ja_{Q,k}$, entonces

$$
s(t)=\sum_k a_{I,k}p(t-kT_s)\cos(2\pi f_c t)-\sum_k a_{Q,k}p(t-kT_s)\sin(2\pi f_c t).
$$

### 3.1.6 Energía de la señal y equivalencia en banda base

Si adoptamos la convención

$$
s(t)=\Re\{u(t)e^{j2\pi f_c t}\},
$$

entonces, bajo la aproximación de banda angosta,

$$
E_s=\int_{-\infty}^{\infty}|s(t)|^2 dt = \frac{1}{2}\int_{-\infty}^{\infty}|u(t)|^2 dt.
$$

Esta relación permite calcular probabilidades de error directamente en banda base compleja, evitando el tratamiento explícito de la portadora.

**[Figura 3.2]:** diagrama en bloques de conversión pasabanda-pasabajo: a la entrada, una señal real en torno a $f_c$; luego dos ramas multiplicadoras con $\cos(2\pi f_c t)$ y $-\sin(2\pi f_c t)$; después filtros pasabajo; finalmente las salidas $I(t)$ y $Q(t)$. La descripción debe resaltar que la rama I mide la proyección sobre el eje real y la rama Q mide la proyección sobre un eje ortogonal desplazado $90^\circ$.

### 3.1.7 Ejemplos resueltos

**Ejemplo 3.1:** obtener la representación $I/Q$ de una senoidal modulada.

Considérese

$$
s(t)=3\cos\left(2\pi f_c t+\frac{\pi}{6}\right).
$$

Usando

$$
\cos(\alpha+\beta)=\cos\alpha\cos\beta-\sin\alpha\sin\beta,
$$

se obtiene

$$
s(t)=3\cos\left(\frac{\pi}{6}\right)\cos(2\pi f_c t)-3\sin\left(\frac{\pi}{6}\right)\sin(2\pi f_c t).
$$

Como $\cos(\pi/6)=\sqrt{3}/2$ y $\sin(\pi/6)=1/2$,

$$
I=\frac{3\sqrt{3}}{2},
\qquad
Q=\frac{3}{2}.
$$

La envolvente compleja es

$$
u(t)=I+jQ=\frac{3\sqrt{3}}{2}+j\frac{3}{2}=3e^{j\pi/6}.
$$

**Conclusión:** una sola senoidal modulada puede verse como un punto fijo del plano complejo con radio $3$ y ángulo $\pi/6$.

**Ejemplo 3.2:** conversión de una señal QPSK elemental a banda base equivalente.

Sea

$$
s(t)=A p(t)\cos\left(2\pi f_c t+\frac{3\pi}{4}\right),
$$

donde $p(t)$ es un pulso de duración $T_s$.

Su envolvente compleja vale

$$
u(t)=A p(t)e^{j3\pi/4}.
$$

Como

$$
e^{j3\pi/4}=-\frac{1}{\sqrt{2}}+j\frac{1}{\sqrt{2}},
$$

entonces

$$
I(t)=-\frac{A}{\sqrt{2}}p(t),
\qquad
Q(t)=\frac{A}{\sqrt{2}}p(t).
$$

El símbolo se ubica en el segundo cuadrante del plano de constelación. Ésta es exactamente la interpretación geométrica usada en QPSK.

---

## 3.2 Técnicas de Modulación Binaria y M-aria

### 3.2.1 Idea general

En una modulación digital, cada símbolo pertenece a un conjunto finito de formas de onda. Si ese conjunto tiene cardinalidad $M$, hablamos de una modulación **M-aria**. Cada símbolo transporta

$$
k=\log_2 M
$$

bits, y la relación entre tasa de bits $R_b$ y tasa de símbolos $R_s$ es

$$
R_b=kR_s.
$$

El incremento de $M$ mejora la eficiencia espectral, pero normalmente reduce la distancia euclidiana entre símbolos para energía media fija, lo que empeora la robustez al ruido.

### 3.2.2 ASK (Amplitude Shift Keying)

#### a) Señal temporal

En ASK binaria, la información se codifica variando la amplitud. Una expresión general es

$$
s_i(t)=A_i p(t)\cos(2\pi f_c t), \qquad i\in\{0,1\},
$$

con $A_0\neq A_1$.

El caso más común es **OOK (On-Off Keying)**:

$$
s_1(t)=A p(t)\cos(2\pi f_c t),
\qquad
s_0(t)=0.
$$

Si definimos $E_b$ como energía media por bit y bits equiprobables, entonces la energía del símbolo “1” debe ser $2E_b$.

#### b) Constelación

En banda base equivalente, ASK binaria ocupa una sola dimensión. Para OOK, la constelación puede representarse como

$$
\mathcal{A}_{\text{OOK}}=\{0,\sqrt{2E_b}\}
$$

si $E_b$ es energía media por bit.

#### c) Espectro

Si el pulso es rectangular,

$$
p(t)=
\begin{cases}
1, & 0\le t < T_b,\\
0, & \text{en otro caso},
\end{cases}
$$

entonces

$$
P(f)=T_b\,\operatorname{sinc}(fT_b)e^{-j\pi fT_b},
$$

con

$$
\operatorname{sinc}(x)=\frac{\sin(\pi x)}{\pi x}.
$$

La densidad espectral de potencia en banda base es proporcional a $|P(f)|^2$, es decir, a una función $\operatorname{sinc}^2$. En pasabanda, el espectro aparece desplazado alrededor de $\pm f_c$.

#### d) BER

Para detección coherente binaria OOK en AWGN, con umbral óptimo y energía media por bit $E_b$,

$$
P_b=Q\left(\sqrt{\frac{E_b}{N_0}}\right),
$$

donde

$$
Q(x)=\frac{1}{\sqrt{2\pi}}\int_x^{\infty} e^{-u^2/2}\,du.
$$

Comparada con BPSK, ASK/OOK es menos robusta porque la distancia entre sus señales es menor para la misma energía media.

**[Figura 3.3]:** constelación de ASK binaria sobre el eje I. Deben verse dos puntos: uno en el origen para el bit 0 y otro sobre el eje positivo para el bit 1. El texto descriptivo debe enfatizar que el receptor sólo necesita decidir sobre una coordenada, pero que el punto en el origen queda más expuesto al ruido y a incertidumbres de amplitud.

**Ejemplo 3.3:** BER de OOK coherente.

Si $E_b/N_0=10$ dB, entonces

$$
\frac{E_b}{N_0}=10.
$$

Así,

$$
P_b=Q(\sqrt{10})=Q(3.162).
$$

Usando una tabla o aproximación numérica,

$$
Q(3.162)\approx 7.8\times 10^{-4}.
$$

Por tanto, una de cada aproximadamente $1280$ decisiones de bit sería errónea en promedio.

### 3.2.3 FSK (Frequency Shift Keying)

#### a) Señal temporal

En BFSK binaria, cada bit se representa por una frecuencia distinta:

$$
s_1(t)=\sqrt{\frac{2E_b}{T_b}}\cos\big(2\pi(f_c+\Delta f)t\big),
$$

$$
s_0(t)=\sqrt{\frac{2E_b}{T_b}}\cos\big(2\pi(f_c-\Delta f)t\big).
$$

Para ortogonalidad exacta en el intervalo $[0,T_b)$ se requiere, típicamente,

$$
\Delta f = \frac{1}{2T_b}
$$

para una formulación coherente ortogonal conveniente.

#### b) Interpretación geométrica

BFSK ortogonal usa dos funciones base ortogonales. Los símbolos se representan por

$$
\mathbf{s}_1=(\sqrt{E_b},0),
\qquad
\mathbf{s}_0=(0,\sqrt{E_b}).
$$

La distancia euclidiana es

$$
d^2=\|\mathbf{s}_1-\mathbf{s}_0\|^2=2E_b.
$$

#### c) Espectro

El espectro de FSK se compone de dos lóbulos principales centrados en $f_c\pm\Delta f$. A mayor separación frecuencial, mayor ortogonalidad y robustez, pero menor eficiencia espectral.

Un estimado simple del ancho de banda para BFSK rectangular es

$$
B_{\text{FSK}} \approx 2\Delta f + \frac{2}{T_b},
$$

lo cual muestra explícitamente el costo espectral de separar frecuencias.

#### d) Detección coherente y no coherente

- **Coherente:** el receptor dispone de una referencia de fase adecuada.
- **No coherente:** el receptor detecta energía en cada rama, sin necesidad de fase portadora exacta.

Para BFSK ortogonal coherente en AWGN:

$$
P_b=Q\left(\sqrt{\frac{E_b}{N_0}}\right).
$$

Para BFSK ortogonal no coherente:

$$
P_b=\frac{1}{2}e^{-E_b/(2N_0)}.
$$

La detección no coherente simplifica el receptor, pero penaliza el desempeño.

**[Figura 3.4]:** dos formas de onda BFSK dentro de un intervalo de bit: una con frecuencia ligeramente mayor y otra ligeramente menor. Debe apreciarse que la información ya no está en la amplitud ni en la fase instantánea, sino en la “densidad de oscilaciones” por intervalo. También es importante mostrar dos filtros o correladores en el receptor, uno sintonizado a cada tono.

**Ejemplo 3.4:** BER de BFSK coherente y no coherente.

Para $E_b/N_0=8$ dB,

$$
\frac{E_b}{N_0}=10^{0.8}\approx 6.31.
$$

Entonces, para BFSK coherente,

$$
P_b=Q(\sqrt{6.31})=Q(2.512)\approx 6.0\times 10^{-3}.
$$

Para BFSK no coherente,

$$
P_b=\frac{1}{2}e^{-6.31/2}=\frac{1}{2}e^{-3.155}\approx 2.13\times 10^{-2}.
$$

La detección no coherente comete varios errores más que la coherente al mismo $E_b/N_0$.

### 3.2.4 PSK (Phase Shift Keying)

#### a) BPSK: señal, constelación, espectro y BER

En **BPSK** la fase cambia entre dos valores separados $\pi$ radianes:

$$
s_b(t)=\sqrt{\frac{2E_b}{T_b}}\,b_k p(t)\cos(2\pi f_c t),
\qquad b_k\in\{+1,-1\}.
$$

En banda base equivalente,

$$
a_k\in\{+\sqrt{E_b},-\sqrt{E_b}\}.
$$

La constelación es unidimensional y antipodal. La distancia entre símbolos es

$$
d=2\sqrt{E_b}.
$$

El espectro depende del pulso $p(t)$. Con pulso rectangular, la envolvente espectral vuelve a ser $\operatorname{sinc}^2$, centrada alrededor de $\pm f_c$.

La BER exacta en AWGN es

$$
P_b=Q\left(\sqrt{\frac{2E_b}{N_0}}\right).
$$

Esta modulación es óptima entre las binarias lineales en términos de distancia mínima para energía dada.

**[Figura 3.5]:** constelación BPSK sobre el eje real con dos puntos simétricos respecto del origen. El texto descriptivo debe destacar que la simetría antipodal maximiza la separación euclidiana y por ello BPSK es notablemente robusta frente a ruido gaussiano.

**Ejemplo 3.5:** BER de BPSK.

Si $E_b/N_0=10$ dB,

$$
P_b=Q(\sqrt{20})=Q(4.472)\approx 3.87\times10^{-6}.
$$

Esto significa aproximadamente 4 errores por cada millón de bits transmitidos.

#### b) Generalización a M-PSK

En M-PSK los símbolos tienen amplitud constante y fases igualmente espaciadas:

$$
s_m(t)=\sqrt{\frac{2E_s}{T_s}}p(t)\cos\left(2\pi f_c t+\frac{2\pi m}{M}\right),
\qquad m=0,1,\dots,M-1.
$$

En banda base,

$$
a_m=\sqrt{E_s}e^{j2\pi m/M}.
$$

Todos los puntos están sobre un círculo de radio $\sqrt{E_s}$. La distancia mínima entre vecinos es

$$
d_{\min}=2\sqrt{E_s}\sin\left(\frac{\pi}{M}\right).
$$

Para $M$ grande, $\sin(\pi/M)\approx \pi/M$, por lo que $d_{\min}$ decrece y el sistema se vuelve más sensible al ruido.

Una aproximación usual para la probabilidad de error de símbolo en AWGN es

$$
P_s \approx 2Q\left(\sqrt{\frac{2E_s}{N_0}}\sin\frac{\pi}{M}\right), \qquad M\ge 4.
$$

Con codificación Gray,

$$
P_b \approx \frac{P_s}{\log_2 M}.
$$

### 3.2.5 QPSK

QPSK puede verse como dos BPSK ortogonales transmitidas simultáneamente. Cada símbolo transporta $k=2$ bits.

#### a) Señal

Sea la pareja de bits $(b_I,b_Q)$ con valores en $\{\pm1\}$. Entonces

$$
s(t)=\sqrt{\frac{E_s}{T_s}}p(t)b_I\cos(2\pi f_ct)-\sqrt{\frac{E_s}{T_s}}p(t)b_Q\sin(2\pi f_ct).
$$

Equivalentemente,

$$
a_k=\sqrt{\frac{E_s}{2}}(b_I+jb_Q).
$$

#### b) Constelación

La constelación QPSK consta de cuatro puntos:

$$
\left\{\pm\sqrt{\frac{E_s}{2}} \pm j\sqrt{\frac{E_s}{2}}\right\}.
$$

Con codificación Gray, puntos adyacentes difieren en un solo bit.

#### c) Relación con BPSK y BER

Como $E_s=2E_b$, cada rama transporta un bit con energía $E_b$. Por tanto,

$$
P_b^{\text{QPSK}}=Q\left(\sqrt{\frac{2E_b}{N_0}}\right),
$$

igual que BPSK.

#### d) Espectro

A tasa de bits fija, QPSK transmite 2 bits por símbolo, de modo que la tasa simbólica es la mitad que en BPSK:

$$
R_s=\frac{R_b}{2}.
$$

Por eso, para igual conformación de pulso, QPSK ocupa aproximadamente la mitad del ancho de banda que BPSK a igual tasa de bits.

**[Figura 3.6]:** constelación QPSK en los cuatro cuadrantes del plano $I$-$Q$, con etiquetas Gray, por ejemplo 00, 01, 11, 10 alrededor del círculo. La descripción debe enfatizar que QPSK se interpreta como la transmisión simultánea de dos secuencias binarias ortogonales: una en la rama I y otra en la rama Q.

**Ejemplo 3.6:** coordenadas de una constelación QPSK.

Supóngase $E_b=1$. Entonces $E_s=2$ y

$$
\sqrt{\frac{E_s}{2}}=1.
$$

Los cuatro símbolos son

$$
1+j,\quad -1+j,\quad -1-j,\quad 1-j.
$$

Si se usa Gray y el bit-par 10 se asigna a $-1-j$, entonces transmitir 10 significa ubicar el símbolo en el tercer cuadrante.

### 3.2.6 Conformación de pulsos

La modulación no queda completamente definida por la constelación; el pulso $p(t)$ es igualmente esencial.

#### a) Pulso rectangular

$$
p_{\text{rect}}(t)=
\begin{cases}
1, & 0\le t < T_s,\\
0, & \text{en otro caso}.
\end{cases}
$$

Su transformada es

$$
P_{\text{rect}}(f)=T_s\operatorname{sinc}(fT_s)e^{-j\pi fT_s}.
$$

Ventaja: implementación simple. Desventaja: lóbulos laterales elevados y peor confinamiento espectral.

#### b) Pulso coseno alzado

La respuesta en frecuencia del pulso coseno alzado es

$$
P_{RC}(f)=
\begin{cases}
T_s, & |f|\le \frac{1-\alpha}{2T_s},\\
\frac{T_s}{2}\left[1+\cos\left(\frac{\pi T_s}{\alpha}\left(|f|-\frac{1-\alpha}{2T_s}\right)\right)\right], & \frac{1-\alpha}{2T_s}<|f|\le \frac{1+\alpha}{2T_s},\\
0, & |f|>\frac{1+\alpha}{2T_s},
\end{cases}
$$

donde $\alpha\in[0,1]$ es el **factor de roll-off**.

En tiempo,

$$
p_{RC}(t)=\frac{\sin(\pi t/T_s)}{\pi t/T_s}\cdot \frac{\cos(\pi \alpha t/T_s)}{1-(2\alpha t/T_s)^2}.
$$

El ancho de banda unilateral mínimo requerido es

$$
B=\frac{1+\alpha}{2T_s}.
$$

El criterio de Nyquist para ausencia de ISI exige

$$
p(nT_s)=
\begin{cases}
1, & n=0,\\
0, & n\neq 0.
\end{cases}
$$

El pulso coseno alzado cumple esta propiedad.

**[Figura 3.7]:** comparación entre el espectro de un pulso rectangular y uno coseno alzado. La figura debe mostrar que el rectangular concentra mucha energía en lóbulos laterales, mientras el coseno alzado suaviza la transición y reduce interferencia fuera de banda. La anotación visual más importante es el papel de $\alpha$: a mayor roll-off, mayor ancho de banda pero menor sensibilidad a imperfecciones temporales.

**Ejemplo 3.7:** ancho de banda con coseno alzado.

Para QPSK con $R_b=10$ Mb/s y $\alpha=0.25$,

$$
R_s=\frac{R_b}{2}=5\text{ Mbaud}.
$$

Luego,

$$
B\approx (1+\alpha)R_s=1.25\times 5 = 6.25\text{ MHz}
$$

para el ancho de banda pasabanda aproximado. La eficiencia espectral es

$$
\eta=\frac{R_b}{B}=\frac{10}{6.25}=1.6\text{ bit/s/Hz}.
$$

### 3.2.7 Análisis espectral comparativo

Bajo pulsos Nyquist con roll-off $\alpha$, una expresión práctica del ancho de banda pasabanda es

$$
B\approx (1+\alpha)R_s=(1+\alpha)\frac{R_b}{\log_2M}
$$

para modulaciones lineales como PSK y QAM.

Por tanto,

$$
\eta=\frac{R_b}{B}\approx \frac{\log_2 M}{1+\alpha}.
$$

De aquí se deduce:

- BPSK: $\eta\approx \dfrac{1}{1+\alpha}$,
- QPSK: $\eta\approx \dfrac{2}{1+\alpha}$,
- 8-PSK: $\eta\approx \dfrac{3}{1+\alpha}$,
- 16-QAM: $\eta\approx \dfrac{4}{1+\alpha}$.

FSK suele ser menos eficiente porque necesita separación en frecuencia. ASK puede alcanzar eficiencias comparables a PSK, pero con peor sensibilidad a ruido/amplitud.

### 3.2.8 Eficiencia espectral comparativa

Para $\alpha=0.25$:

$$
\eta_{\text{BPSK}}\approx 0.8\text{ bit/s/Hz},
$$

$$
\eta_{\text{QPSK}}\approx 1.6\text{ bit/s/Hz},
$$

$$
\eta_{8\text{-PSK}}\approx 2.4\text{ bit/s/Hz},
$$

$$
\eta_{16\text{-QAM}}\approx 3.2\text{ bit/s/Hz}.
$$

Sin embargo, elevar la eficiencia espectral aumenta la exigencia de SNR para mantener la misma BER.

---

## 3.3 Modulación de Amplitud en Cuadratura (QAM)

### 3.3.1 Definición y señal QAM general

QAM combina variaciones simultáneas de amplitud en las ramas I y Q. La señal general puede escribirse como

$$
s_m(t)=I_m p(t)\cos(2\pi f_c t)-Q_m p(t)\sin(2\pi f_c t),
$$

o equivalentemente,

$$
s_m(t)=\Re\{a_m p(t)e^{j2\pi f_c t}\}, \qquad a_m=I_m+jQ_m.
$$

A diferencia de M-PSK, el módulo de $a_m$ ya no es constante: tanto amplitud como fase transportan información.

### 3.3.2 Constelaciones M-QAM

En una constelación cuadrada $M$-QAM, con $M=L^2$, cada eje adopta $L=\sqrt{M}$ niveles igualmente espaciados. Una parametrización común es

$$
I,Q\in \{\pm a,\pm 3a,\dots,\pm(L-1)a\}.
$$

#### a) 4-QAM

4-QAM es geométricamente idéntica a QPSK:

$$
\mathcal{A}_{4\text{-QAM}}=\{\pm a \pm ja\}.
$$

#### b) 16-QAM

Cada eje toma los niveles $\{\pm a,\pm 3a\}$, dando 16 puntos.

#### c) 64-QAM

Cada eje toma los niveles $\{\pm a,\pm 3a,\pm 5a,\pm 7a\}$, generando 64 puntos.

#### d) 256-QAM

Cada eje toma 16 niveles equiespaciados, desde $\pm a$ hasta $\pm 15a$.

A medida que aumenta $M$, la constelación se densifica y la distancia mínima disminuye para energía media fija.

Para constelaciones cuadradas,

$$
E_s=\frac{2}{3}(M-1)a^2,
$$

y la distancia mínima es

$$
d_{\min}=2a=\sqrt{\frac{6E_s}{M-1}}.
$$

Como $E_s=E_b\log_2M$,

$$
d_{\min}=\sqrt{\frac{6E_b\log_2 M}{M-1}}.
$$

Esta ecuación muestra por qué QAM de alto orden requiere SNR elevada.

**[Figura 3.8]:** mosaico de constelaciones 4-QAM, 16-QAM, 64-QAM y 256-QAM. Debe apreciarse visualmente cómo, al crecer $M$, los puntos se hacen más numerosos y cercanos. La descripción debe resaltar que el aumento de eficiencia espectral se compra a costa de menor distancia mínima y mayor vulnerabilidad al ruido, al error de fase y a las no linealidades.

### 3.3.3 Codificación Gray en constelaciones

La codificación Gray asigna etiquetas binarias de modo que símbolos vecinos difieran en un solo bit. En 16-QAM, por ejemplo, los niveles en cada eje pueden etiquetarse como

$$
-3a\to 00,
\quad
-a\to 01,
\quad
+a\to 11,
\quad
+3a\to 10.
$$

La palabra final del símbolo se construye concatenando bits de I y Q. La razón de usar Gray es que, a alta SNR, los errores más probables son hacia vecinos inmediatos; si éstos difieren sólo en un bit, se minimiza la BER para una misma tasa de error de símbolo.

### 3.3.4 Análisis espectral de QAM

QAM es una modulación lineal. Por ello su espectro está determinado principalmente por el pulso $p(t)$ y la tasa simbólica $R_s$.

Si los símbolos $a_k$ son i.i.d. de media cero y varianza $\sigma_a^2$, la PSD de la envolvente compleja es aproximadamente

$$
S_u(f)=\frac{\sigma_a^2}{T_s}|P(f)|^2.
$$

El espectro pasabanda queda centrado en $\pm f_c$ como

$$
S_s(f)=\frac{1}{4}S_u(f-f_c)+\frac{1}{4}S_u(-f-f_c).
$$

Con pulsos coseno alzado, QAM puede confinarse con alta eficiencia dentro de un ancho de banda de aproximadamente

$$
B\approx (1+\alpha)R_s=(1+\alpha)\frac{R_b}{\log_2M}.
$$

### 3.3.5 Impairments en QAM

QAM es muy eficiente, pero también particularmente sensible a imperfecciones analógicas.

#### a) Desbalance I/Q

Si las ramas I y Q tienen ganancias distintas o no están exactamente en cuadratura, la señal recibida puede modelarse como

$$
r(t)=\alpha_I I(t)\cos(2\pi f_ct)-\alpha_Q Q(t)\sin(2\pi f_ct+\varepsilon),
$$

donde $\alpha_I\neq \alpha_Q$ y $\varepsilon\neq 0$ generan distorsión geométrica: la constelación se estira, se inclina o se convierte en una elipse.

#### b) Offset de portadora

Si existe error de frecuencia $\Delta f$ y error de fase $\theta_0$, la envolvente compleja observada es

$$
u_r(t)=\nu(t)e^{j(2\pi \Delta f t+\theta_0)}.
$$

Esto produce rotación continua de la constelación. En QAM de alto orden, pequeños errores de fase pueden causar decisiones erróneas.

#### c) No linealidades

Los amplificadores de potencia reales introducen leyes AM/AM y AM/PM:

$$
A_{out}=g(A_{in}),
\qquad
\phi_{out}=\Phi(A_{in}).
$$

Como QAM posee envolvente no constante, la no linealidad desplaza los puntos de la constelación, incrementa la dispersión espectral y degrada EVM (Error Vector Magnitude).

**[Figura 3.9]:** comparación entre una constelación 16-QAM ideal y versiones degradadas por: (i) rotación global debida a error de portadora, (ii) estiramiento/compresión por desbalance I/Q, y (iii) deformación radial por compresión del amplificador. La descripción debe destacar que, en sistemas reales, el receptor no combate sólo ruido térmico, sino también imperfecciones de RF.

### 3.3.6 Eficiencia espectral de M-QAM

Bajo conformación Nyquist,

$$
\eta_{M\text{-QAM}}\approx \frac{\log_2M}{1+\alpha}.
$$

Por ejemplo, con $\alpha=0.2$:

- 16-QAM: $\eta\approx 4/1.2=3.33$ bit/s/Hz,
- 64-QAM: $\eta\approx 6/1.2=5.0$ bit/s/Hz,
- 256-QAM: $\eta\approx 8/1.2=6.67$ bit/s/Hz.

Esto explica por qué las redes 4G/5G incrementan el orden de QAM cuando el canal es favorable.

### 3.3.7 Comparación con M-PSK

Para igual $M$ y energía media, las constelaciones cuadradas M-QAM suelen ofrecer mayor distancia mínima que M-PSK, por lo que requieren menor SNR para una BER dada. Sin embargo:

- M-PSK tiene envolvente constante, conveniente para amplificadores no lineales.
- M-QAM es más eficiente en potencia, pero exige transmisores y receptores más lineales y precisos.

En resumen:

- si la restricción dominante es la linealidad del amplificador, PSK puede ser preferible;
- si la restricción dominante es la eficiencia espectral, QAM suele ser superior.

### 3.3.8 Ejemplos resueltos

**Ejemplo 3.8:** energía media de 16-QAM.

Para 16-QAM con niveles $\{\pm a,\pm 3a\}$, la energía media por dimensión es

$$
E[I^2]=\frac{1}{4}(a^2+a^2+9a^2+9a^2)=5a^2.
$$

Como I y Q son independientes e idénticas,

$$
E_s=E[I^2]+E[Q^2]=10a^2.
$$

Esto coincide con la fórmula general:

$$
E_s=\frac{2}{3}(16-1)a^2=10a^2.
$$

**Ejemplo 3.9:** BER aproximada de 16-QAM.

Con codificación Gray, una aproximación útil es

$$
P_b\approx \frac{4}{\log_2M}\left(1-\frac{1}{\sqrt{M}}\right)Q\left(\sqrt{\frac{3\log_2M}{M-1}\frac{E_b}{N_0}}\right).
$$

Para $M=16$ y $E_b/N_0=10$ dB,

$$
P_b\approx \frac{4}{4}\left(1-\frac{1}{4}\right)Q\left(\sqrt{\frac{12}{15}\times 10}\right)
=0.75Q(\sqrt{8}).
$$

Como $\sqrt{8}=2.828$,

$$
Q(2.828)\approx 2.34\times 10^{-3}.
$$

Por tanto,

$$
P_b\approx 0.75(2.34\times 10^{-3})\approx 1.76\times 10^{-3}.
$$

Obsérvese que esta BER es bastante mayor que la de BPSK al mismo $E_b/N_0$.

**Ejemplo 3.10:** efecto de un error de fase en 16-QAM.

Supóngase un símbolo ideal

$$
a=3a_0+ja_0.
$$

Si el receptor tiene un error de fase $\theta=10^\circ$, observa

$$
a'=ae^{j\theta}.
$$

Expandiendo,

$$
a'=(3a_0+ja_0)(\cos\theta+j\sin\theta).
$$

Por tanto,

$$
I'=3a_0\cos\theta-a_0\sin\theta,
$$

$$
Q'=3a_0\sin\theta+a_0\cos\theta.
$$

Con $\cos10^\circ\approx0.9848$ y $\sin10^\circ\approx0.1736$,

$$
I'\approx 2.7808a_0,
\qquad
Q'\approx 1.5056a_0.
$$

La constelación gira y el punto se acerca a otras regiones de decisión. En órdenes altos, esta rotación es crítica.

---

## 3.4 Detección y Demodulación

### 3.4.1 Modelo de recepción

En AWGN, el receptor observa

$$
r(t)=s_i(t)+n(t),
$$

donde $s_i(t)$ es una de las formas de onda posibles y $n(t)$ es ruido gaussiano blanco aditivo con PSD bilateral $N_0/2$.

El problema de detección consiste en decidir cuál símbolo fue transmitido a partir de $r(t)$.

### 3.4.2 Diseño de receptores óptimos: filtro adaptado

Supóngase un símbolo $s(t)$ observado en $0\le t\le T$. Sea $h(t)$ la respuesta impulsional de un filtro lineal. La salida en el instante de muestreo $T$ es

$$
y(T)=\int_{-\infty}^{\infty} r(\tau)h(T-\tau)\,d\tau.
$$

En frecuencia,

$$
y_s(T)=\int_{-\infty}^{\infty} S(f)H(f)e^{j2\pi fT}\,df
$$

para la contribución de señal.

La varianza del ruido a la salida es

$$
\sigma_n^2=\frac{N_0}{2}\int_{-\infty}^{\infty}|H(f)|^2df.
$$

Por tanto, la SNR a la salida vale

$$
\mathrm{SNR}_{out}=\frac{\left|\int S(f)H(f)e^{j2\pi fT}df\right|^2}{\frac{N_0}{2}\int |H(f)|^2 df}.
$$

Aplicando la desigualdad de Cauchy-Schwarz,

$$
\left|\int X(f)Y(f)df\right|^2 \le \left(\int |X(f)|^2 df\right)\left(\int |Y(f)|^2 df\right),
$$

con

$$
X(f)=S(f)e^{j2\pi fT},
\qquad
Y(f)=H(f),
$$

se concluye que la SNR se maximiza cuando

$$
H_{MF}(f)=K S^*(f)e^{-j2\pi fT},
$$

donde $K$ es una constante arbitraria.

En tiempo,

$$
h_{MF}(t)=Ks^*(T-t).
$$

Éste es el **filtro adaptado**: una versión invertida en el tiempo y conjugada de la señal buscada.

La SNR máxima resultante es

$$
\mathrm{SNR}_{max}=\frac{2E_s}{N_0}.
$$

**Ecuación clave:**

$$
H_{MF}(f)=K S^*(f)e^{-j2\pi fT}
$$

resume uno de los resultados más importantes de toda la teoría de comunicaciones digitales.

**[Figura 3.10]:** diagrama del receptor óptimo con filtro adaptado: señal ruidosa de entrada, filtro con respuesta “espejo” del pulso transmitido, bloque de muestreo en el instante óptimo y dispositivo de decisión. La descripción debe subrayar que el filtro no elimina mágicamente el ruido, sino que concentra la energía útil del símbolo en el instante de muestreo maximizando la SNR.

### 3.4.3 Correlador y equivalencia con filtro adaptado

Un correlador calcula

$$
z_i=\int_0^T r(t)s_i(t)\,dt.
$$

Puede demostrarse que un banco de correladores y un banco de filtros adaptados son estructuras equivalentes. En el espacio de señales, el receptor óptimo compara proyecciones de $r(t)$ sobre funciones base ortonormales.

Si

$$
s_i(t)=\sum_{m=1}^N s_{i,m}\phi_m(t),
$$

entonces el receptor produce el vector observado

$$
\mathbf{r}=\mathbf{s}_i+\mathbf{n}
$$

y decide el símbolo cuya distancia euclidiana al vector observado es mínima:

$$
\hat{i}=\arg\min_i \|\mathbf{r}-\mathbf{s}_i\|^2.
$$

Esta regla coincide con el criterio de máxima verosimilitud en AWGN.

### 3.4.4 Demodulación coherente vs. no coherente

#### a) Coherente

La demodulación coherente asume que el receptor conoce o estima con precisión la fase y frecuencia de la portadora. Sus ventajas son:

- máximo desempeño en BER,
- compatibilidad con constelaciones densas,
- facilidad de interpretación geométrica.

Su desventaja es la necesidad de sincronización portadora.

#### b) No coherente

La demodulación no coherente evita estimar fase absoluta. Se usa, por ejemplo, en BFSK y DPSK. Su ventaja principal es la simplicidad; su costo es una penalización en desempeño. En general,

$$
P_b^{\text{no coherente}} > P_b^{\text{coherente}}
$$

a igualdad de $E_b/N_0$.

### 3.4.5 BER en función de $E_b/N_0$

La relación señal-ruido normalizada por bit es

$$
\gamma_b=\frac{E_b}{N_0}.
$$

Es la variable estándar para comparar esquemas de modulación.

#### a) BPSK

$$
P_b=Q\left(\sqrt{2\gamma_b}\right).
$$

#### b) QPSK con Gray

$$
P_b=Q\left(\sqrt{2\gamma_b}\right).
$$

#### c) M-QAM cuadrada con Gray (aproximación)

Si $k=\log_2M$,

$$
P_b\approx \frac{4}{k}\left(1-\frac{1}{\sqrt{M}}\right)Q\left(\sqrt{\frac{3k}{M-1}\gamma_b}\right).
$$

Estas expresiones explican las curvas BER vs. $E_b/N_0$: a medida que la modulación se hace de mayor orden, la curva se desplaza hacia la derecha, es decir, requiere más SNR para la misma BER.

**[Figura 3.11]:** familia de curvas BER semilogarítmicas frente a $E_b/N_0$ para BPSK, QPSK, 16-QAM y 64-QAM. BPSK y QPSK deben coincidir; 16-QAM debe aparecer desplazada a la derecha; 64-QAM aún más. La descripción debe indicar que la pendiente refleja la naturaleza exponencial de la función $Q(\cdot)$ y que el “precio” de mayor eficiencia espectral es una mayor exigencia de SNR.

### 3.4.6 Distancia mínima y probabilidad de error

En AWGN, la probabilidad de confundir símbolos depende primordialmente de la distancia mínima $d_{\min}$ de la constelación. Para detección binaria equiprobable,

$$
P_e=Q\left(\frac{d}{\sqrt{2N_0}}\right),
$$

donde $d$ es la distancia entre ambas señales en el espacio euclidiano.

Para constelaciones generales, una cota por unión es

$$
P_s \le \sum_{j\neq i} Q\left(\frac{d_{ij}}{\sqrt{2N_0}}\right),
$$

y a alta SNR suele dominar el vecino más cercano, por lo que intuitivamente

$$
P_s \propto Q\left(\frac{d_{\min}}{\sqrt{2N_0}}\right).
$$

**Conclusión clave:** diseñar buenas modulaciones equivale, en gran medida, a distribuir eficientemente puntos en el plano complejo maximizando $d_{\min}$ bajo restricciones de energía y ancho de banda.

### 3.4.7 Ejemplos resueltos

**Ejemplo 3.11:** derivación operativa del filtro adaptado para pulso rectangular.

Sea un pulso de símbolo

$$
p(t)=
\begin{cases}
1, & 0\le t<T,\\
0, & \text{otro caso}.
\end{cases}
$$

Entonces el filtro adaptado es

$$
h(t)=p(T-t)=
\begin{cases}
1, & 0\le t<T,\\
0, & \text{otro caso},
\end{cases}
$$

que resulta idéntico al propio pulso por su simetría temporal. La salida en $t=T$ es la integral de la señal recibida sobre el intervalo del símbolo, es decir, un acumulador o integrador. Esto muestra que el clásico receptor “integrate-and-dump” es un caso particular de filtro adaptado.

**Ejemplo 3.12:** comparación de BER entre BPSK y 16-QAM a $E_b/N_0=10$ dB.

Para BPSK,

$$
P_b^{\text{BPSK}}=Q(\sqrt{20})\approx 3.87\times10^{-6}.
$$

Para 16-QAM, usando la aproximación anterior,

$$
P_b^{16\text{-QAM}}\approx 1.76\times10^{-3}.
$$

La diferencia es enorme: la mayor eficiencia espectral de 16-QAM se obtiene a costa de una sensibilidad mucho mayor al ruido.

**Ejemplo 3.13:** distancia mínima y error en BPSK.

Los puntos de BPSK son $\pm\sqrt{E_b}$. Por tanto,

$$
d_{\min}=2\sqrt{E_b}.
$$

Sustituyendo en la expresión binaria general,

$$
P_e=Q\left(\frac{2\sqrt{E_b}}{\sqrt{2N_0}}\right)=Q\left(\sqrt{\frac{2E_b}{N_0}}\right),
$$

que recupera la fórmula exacta de BPSK. Este ejemplo demuestra con claridad la conexión entre geometría y desempeño probabilístico.

---

## Resumen de conceptos clave

1. **La representación pasabaja compleja** permite estudiar señales pasabanda mediante su envolvente $u(t)=I(t)+jQ(t)$.
2. **Las componentes I y Q** son las proyecciones ortogonales de la señal sobre dos portadoras desfasadas $90^\circ$.
3. **ASK** modula amplitud; **FSK** modula frecuencia; **PSK** modula fase; **QAM** modula amplitud y fase simultáneamente.
4. **BPSK** y **QPSK** ofrecen excelente robustez; **QAM** ofrece alta eficiencia espectral, pero exige mayor SNR y mejor linealidad.
5. **La conformación de pulsos** determina el espectro y controla la ISI; el coseno alzado es central en sistemas prácticos.
6. **El filtro adaptado** maximiza la SNR a la salida del receptor y conduce a la detección óptima en AWGN.
7. **La BER** depende fuertemente de $E_b/N_0$ y de la **distancia mínima** de la constelación.
8. **La eficiencia espectral** crece con $\log_2M$, pero normalmente a costa de una mayor probabilidad de error para una SNR dada.

En síntesis, la modulación digital no es sólo una técnica de mapeo de bits, sino un problema profundo de geometría, probabilidad, espectro y diseño de receptores. Entender esta unidad es fundamental para abordar temas avanzados como codificación de canal, OFDM, sincronización, ecualización y comunicaciones móviles modernas.

---

## Referencias

1. Proakis, J. G., & Salehi, M. (2008). *Digital Communications* (5th ed.). McGraw-Hill.
2. Sklar, B. (2001). *Digital Communications: Fundamentals and Applications* (2nd ed.). Prentice Hall.
3. Goldsmith, A. (2005). *Wireless Communications*. Cambridge University Press. https://doi.org/10.1017/CBO9780511841224
4. Haykin, S. (2001). *Communication Systems* (4th ed.). John Wiley & Sons.
5. Simon, M. K., & Alouini, M.-S. (2005). *Digital Communication over Fading Channels* (2nd ed.). Wiley. https://doi.org/10.1002/0471749425
6. Nyquist, H. (1928). Certain topics in telegraph transmission theory. *Transactions of the American Institute of Electrical Engineers*, 47(2), 617-644. https://doi.org/10.1109/T-AIEE.1928.5055024
7. Viterbi, A. J. (1965). Error probability for differential detection of phase-shift keying modulated waves. *IEEE Transactions on Information Theory*, 11(4), 514-522. https://doi.org/10.1109/TIT.1965.1053801
