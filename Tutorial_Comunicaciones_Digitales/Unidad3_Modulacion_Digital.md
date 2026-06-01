# Unidad 3: Modulación Digital

## Introducción de la unidad

La modulación digital es el conjunto de técnicas mediante las cuales una secuencia discreta de bits se transforma en una señal analógica apta para propagarse sobre un canal físico. En sistemas móviles, satelitales, Wi-Fi, enlaces ópticos, redes IoT y prácticamente cualquier sistema moderno, la elección de la modulación determina un compromiso entre **robustez al ruido**, **eficiencia espectral**, **complejidad del receptor**, **requisitos de linealidad del transmisor**, **sensibilidad a desincronizaciones** y **susceptibilidad a distorsiones de RF**.

Desde el punto de vista matemático, la modulación digital conecta tres espacios fundamentales:

1. el espacio de bits,
2. el espacio de señales temporales, y
3. el espacio geométrico de constelaciones.

En esta unidad se desarrolla esa conexión de forma rigurosa y pedagógica. Primero se estudia la representación pasabanda y su equivalente pasabajo complejo; luego se analizan ASK, FSK, PSK y QPSK; posteriormente se profundiza en QAM; después se introduce la teoría de detección óptima, demodulación coherente y no coherente; finalmente se incorporan dos bloques imprescindibles en sistemas modernos: los **impairments** de la cadena Tx-Rx y la **decisión blanda basada en log-likelihood ratios (LLRs)**.

> **Concepto clave:** una señal modulada puede entenderse como un punto que viaja en el plano complejo, filtrado en el tiempo por un pulso, desplazado en frecuencia por una portadora y observado por un receptor inmerso en ruido, desincronización y desvanecimiento.

---

## 3.1 Análisis de Señales Pasabajas y Pasabanda

### 3.1.1 Señales pasabanda y la necesidad de una representación equivalente

Una señal **pasabanda** es aquella cuya energía espectral se concentra alrededor de una frecuencia portadora $f_c \gg 0$. Una representación típica es

$$
s(t)=A(t)\cos\big(2\pi f_c t+\phi(t)\big),
$$

donde $A(t)$ y $\phi(t)$ varían lentamente respecto de la portadora. En una implementación física, $A(t)$ y $\phi(t)$ son producidas por el procesamiento en banda base y la portadora desplaza la señal hacia una banda de RF adecuada para el canal.

Trabajar directamente con $s(t)$ en banda pasante suele ser algebraicamente incómodo. Por ello se introduce una representación **pasabaja equivalente** que traslada toda la información de amplitud y fase a una envolvente compleja alrededor de frecuencia cero.

### 3.1.2 Representación compleja de envolvente

Sea $s(t)$ una señal real. Su **transformada de Hilbert** se define como

$$
\hat{s}(t)=\mathcal{H}\{s(t)\}=\frac{1}{\pi}\operatorname{p.v.}\int_{-\infty}^{\infty}\frac{s(\tau)}{t-\tau}\,d\tau,
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

> **Concepto clave:** la señal real pasabanda $s(t)$ y su equivalente complejo pasabajo $u(t)$ contienen exactamente la misma información, pero $u(t)$ es mucho más conveniente para análisis, simulación, sincronización y diseño de receptores.

**[Figura 3.1]:** representación conceptual de una señal pasabanda senoidal cuya amplitud y fase cambian lentamente, acompañada de su envolvente compleja en el plano $I$-$Q$. La figura debe mostrar arriba una oscilación rápida alrededor de cero y abajo una trayectoria compleja suave que gira y cambia de radio. El mensaje visual es que la oscilación de alta frecuencia se factoriza y la información útil queda encapsulada en una señal compleja de baja frecuencia.

### 3.1.3 Componentes en fase (I) y cuadratura (Q)

La envolvente compleja puede descomponerse como

$$
u(t)=I(t)+jQ(t).
$$

Por tanto,

$$
s(t)=I(t)\cos(2\pi f_c t)-Q(t)\sin(2\pi f_c t).
$$

Las funciones $I(t)$ y $Q(t)$ se denominan, respectivamente, **componente en fase** y **componente en cuadratura**. Geométricamente, son las coordenadas cartesianas del símbolo en el plano complejo. Si escribimos

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

### 3.1.4 Conversión pasabanda a pasabajo equivalente

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

Este resultado es el fundamento de los moduladores y demoduladores en cuadratura usados en SDR, LTE, 5G, Wi-Fi, DVB y sistemas satelitales.

En frecuencia, si $U(f)$ es la transformada de Fourier de $u(t)$, entonces la señal real pasabanda posee espectro

$$
S(f)=\frac{1}{2}U(f-f_c)+\frac{1}{2}U^*(-f-f_c).
$$

Así, el espectro pasabajo se traslada a $\pm f_c$, generando las dos bandas laterales conjugadas requeridas para que la señal temporal sea real.

### 3.1.5 Representación compleja de señales moduladas lineales

En una modulación lineal digital, la envolvente compleja suele escribirse como

$$
u(t)=\sum_k a_k p(t-kT_s),
$$

donde:

- $a_k$ es el símbolo complejo transmitido,
- $p(t)$ es el pulso conformador,
- $T_s$ es el período de símbolo.

Entonces la señal pasabanda real es

$$
s(t)=\Re\left\{\left(\sum_k a_k p(t-kT_s)\right)e^{j2\pi f_c t}\right\}.
$$

Toda modulación lineal bidimensional (QPSK, M-QAM, OQPSK, $\pi/4$-QPSK, etc.) puede analizarse con esta ecuación. Si $a_k=a_{I,k}+ja_{Q,k}$, entonces

$$
s(t)=\sum_k a_{I,k}p(t-kT_s)\cos(2\pi f_c t)-\sum_k a_{Q,k}p(t-kT_s)\sin(2\pi f_c t).
$$

### 3.1.6 Arquitectura detallada del transmisor pasabanda

En un transmisor moderno la cadena física es más rica que la ecuación ideal anterior. Una arquitectura típica contiene:

1. **codificador y formateador de bits**,
2. **mapeador de símbolos** $b_k \mapsto a_k$,
3. **interpolación y conformación de pulsos**,
4. **conversión digital-analógica (DAC)**,
5. **filtrado de reconstrucción**,
6. **mezclado en cuadratura y upconversion**,
7. **amplificación de potencia (PA)** y adaptación de impedancias.

En tiempo discreto, si se emplean $L$ muestras por símbolo, la señal antes del DAC puede modelarse como

$$
x[n]=\sum_k a_k p[n-kL].
$$

El DAC real no genera impulsos ideales, sino una salida de retención de orden cero (ZOH). Si $T_{DAC}$ es el período de muestreo,

$$
u_{DAC}(t)=\sum_n x[n]\,\Pi\left(\frac{t-nT_{DAC}}{T_{DAC}}\right),
$$

donde $\Pi(\cdot)$ es un pulso rectangular unitario. La respuesta en frecuencia del ZOH es

$$
H_{ZOH}(f)=T_{DAC}\,\operatorname{sinc}(fT_{DAC})e^{-j\pi fT_{DAC}}.
$$

Por tanto, el DAC introduce una envolvente tipo $\operatorname{sinc}(\cdot)$ que atenúa altas frecuencias y provoca una inclinación espectral que, en práctica, suele compensarse digitalmente.

Tras el filtrado analógico de reconstrucción, la señal compleja de RF equivalente puede escribirse como

$$
u_{RF}(t)=\big(\nu_{DAC}(t)*h_{rec}(t)\big)e^{j\phi_{LO}},
$$

y la señal pasabanda radiada es

$$
s_{RF}(t)=\Re\{G_{RF}\,u_{RF}(t)e^{j2\pi f_c t}\},
$$

donde $G_{RF}$ incorpora la ganancia total de la cadena analógica.

Dos observaciones de diseño son fundamentales:

- el **pulso conformador** controla simultáneamente la ocupación espectral y la ISI;
- el **PA** puede distorsionar modulaciones con alta variación de envolvente, como QAM, generando expansión espectral y error de magnitud vectorial (EVM).

> **Concepto clave:** la modulación digital no termina en el mapeador de constelaciones; el filtro conformador, el DAC, el mezclador y el amplificador alteran la forma final de la señal y condicionan el desempeño real del enlace.

**[Figura 3.2]:** diagrama detallado del transmisor pasabanda. Debe incluir fuente binaria, codificador, mapeador, filtro conformador RRC, interpolador, DAC con efecto ZOH, filtro de reconstrucción, mezclador I/Q, oscilador local, PA y antena. La descripción debe resaltar cómo cada bloque añade una restricción física: ancho de banda, linealidad, ruido de fase, resolución del DAC y potencia radiada.

### 3.1.7 Arquitectura detallada del receptor pasabanda

La arquitectura dual del receptor contiene normalmente:

1. **LNA** y filtro de RF,
2. **downconversion** con oscilador local,
3. **ADC**,
4. **filtrado pasabajo y filtro adaptado**,
5. **AGC**, sincronización de frecuencia, fase y tiempo,
6. **muestreo a ritmo de símbolo**,
7. **demapper y decisión**.

Si la señal recibida en RF es $r_{RF}(t)$, el equivalente en banda base tras mezclar con una portadora estimada $\hat{f}_c$ y fase $\hat{\phi}$ es

$$
r_{BB}(t)=\operatorname{LPF}\left\{2r_{RF}(t)e^{-j(2\pi \hat{f}_c t+\hat{\phi})}\right\}.
$$

Luego se aplica el filtro adaptado $h_{MF}(t)$:

$$
y(t)=(r_{BB}*h_{MF})(t).
$$

El receptor ideal muestrea en los instantes correctos,

$$
y[k]=y(kT_s+\hat{\tau}),
$$

donde $\hat{\tau}$ es la estimación del desfase temporal. Si el pulso total cumple el criterio de Nyquist y la sincronización es perfecta, entonces

$$
y[k]=a_k+w[k],
$$

con $w[k]$ ruido gaussiano complejo circular.

En la práctica, sin embargo, aparecen desajustes de frecuencia, fase, temporización, desbalance I/Q, cuantización del ADC y desvanecimiento multitrayecto. Esos efectos se analizarán con detalle en la Sección 3.5.

**[Figura 3.3]:** diagrama del receptor en cuadratura: antena, filtro de RF, LNA, mezclador con $\cos(2\pi f_c t)$ y $-\sin(2\pi f_c t)$, filtros pasabajo, ADC, filtro adaptado, recuperación de reloj, recuperación de portadora y bloque de decisión. La figura debe enfatizar que el receptor no sólo detecta símbolos: también debe estimar parámetros ocultos del canal y del hardware.

### 3.1.8 Energía de la señal y equivalencia en banda base

Si adoptamos la convención

$$
s(t)=\Re\{u(t)e^{j2\pi f_c t}\},
$$

entonces, bajo la aproximación de banda angosta,

$$
E_s=\int_{-\infty}^{\infty}|s(t)|^2dt=\frac{1}{2}\int_{-\infty}^{\infty}|u(t)|^2dt.
$$

Esta relación permite calcular probabilidades de error directamente en banda base compleja, evitando el tratamiento explícito de la portadora. Para constelaciones normalizadas suele imponerse

$$
\mathbb{E}[|a_k|^2]=E_s,
$$

y la energía por bit queda dada por

$$
E_b=\frac{E_s}{\log_2 M}
$$

para una modulación de orden $M$.

### 3.1.9 Ejemplos resueltos

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

El símbolo se ubica en el segundo cuadrante del plano de constelación.

**Ejemplo 3.3:** efecto del DAC idealizado sobre una secuencia alternante.

Considérese $x[n]=(-1)^n$ y un DAC ZOH con período $T_{DAC}$. La salida es escalonada y su espectro queda multiplicado por

$$
|H_{ZOH}(f)|=T_{DAC}|\operatorname{sinc}(fT_{DAC})|.
$$

En la frecuencia de Nyquist $f=\frac{1}{2T_{DAC}}$,

$$
|H_{ZOH}(f)|=T_{DAC}\left|\operatorname{sinc}\left(\frac{1}{2}\right)\right|=T_{DAC}\frac{2}{\pi}.
$$

Es decir, la componente de mayor frecuencia útil aparece atenuada por un factor $\frac{2}{\pi}\approx 0.637$. Esta pérdida explica por qué los transmisores reales incorporan pre-ecualización digital o filtros de reconstrucción cuidados.

---

## 3.2 Técnicas de Modulación Binaria y M-aria

### 3.2.1 Idea general

En modulación digital, cada símbolo transmite $k=\log_2 M$ bits y selecciona una señal entre $M$ posibles. El conjunto de señales puede diferir en amplitud, frecuencia, fase o combinaciones de ellas. El reto del diseñador consiste en maximizar la tasa de información y minimizar la probabilidad de error bajo restricciones de potencia y ancho de banda.

Las familias clásicas son:

- **ASK**: cambio de amplitud,
- **FSK**: cambio de frecuencia,
- **PSK**: cambio de fase,
- **QAM**: cambio conjunto de amplitud y fase.

### 3.2.2 ASK (Amplitude Shift Keying)

#### a) Señal temporal

En la versión binaria más simple,

$$
s_i(t)=A_i p(t)\cos(2\pi f_c t), \qquad i\in\{0,1\},
$$

donde típicamente $A_0=0$ y $A_1=A$ para OOK, o bien $A_0=-A$, $A_1=+A$ para una versión bipolar equivalente a 2-PAM en banda base.

ASK resulta conceptualmente simple y compatible con detección de envolvente, pero es sensible a variaciones de amplitud del canal y del hardware.

#### b) Constelación

En banda base equivalente, la modulación ASK binaria genera puntos sobre el eje real:

$$
a_0=0,\qquad a_1=A
$$

o, en versión bipolar,

$$
a_0=-A,\qquad a_1=A.
$$

La distancia entre puntos controla la BER. Para potencia media fija, las constelaciones con puntos más separados son más robustas.

#### c) Espectro

Si el pulso es rectangular de duración $T_s$,

$$
p(t)=
\begin{cases}
1,&0\le t<T_s,\\
0,&\text{otro caso},
\end{cases}
$$

su transformada es

$$
P(f)=T_s\operatorname{sinc}(fT_s)e^{-j\pi fT_s}.
$$

Por tanto, el espectro pasabanda de ASK se centra en $\pm f_c$ y hereda la envolvente $\operatorname{sinc}(\cdot)$ del pulso. Si se reemplaza el pulso rectangular por uno Nyquist, el espectro se compacta mejor y se reduce la ISI.

#### d) BER

Para detección coherente de 2-ASK bipolar, la expresión coincide con BPSK:

$$
P_b=Q\left(\sqrt{\frac{2E_b}{N_0}}\right).
$$

Para OOK con detección coherente y símbolos equiprobables,

$$
P_b=Q\left(\sqrt{\frac{E_b}{N_0}}\right),
$$

mientras que con detección no coherente la penalización es aún mayor.

> **Concepto clave:** ASK es intuitiva pero su sensibilidad a desvanecimientos y fluctuaciones de ganancia la hace menos robusta que PSK para la misma energía media.

**[Figura 3.4]:** constelación de ASK binaria y comparación con su forma de onda temporal. Debe mostrarse un único eje real con dos niveles, junto con la señal pasabanda cuyo sobre cambia de un símbolo a otro. La descripción debe destacar que el parámetro informativo es la amplitud de la envolvente.

### 3.2.3 FSK (Frequency Shift Keying)

#### a) Señal temporal

En BFSK,

$$
s_i(t)=\sqrt{\frac{2E_b}{T_b}}\cos\big(2\pi f_i t\big), \qquad i\in\{0,1\},
$$

donde $f_0$ y $f_1$ representan dos frecuencias distintas. Si la separación es adecuada, las señales son ortogonales en el intervalo de bit.

#### b) Interpretación geométrica

Aunque en tiempo la diferencia sea de frecuencia, en el espacio de señales BFSK ortogonal se representa con dos vectores ortogonales:

$$
\mathbf{s}_0=(\sqrt{E_b},0),
\qquad
\mathbf{s}_1=(0,\sqrt{E_b}).
$$

Esto muestra que FSK no está fuera de la geometría de constelaciones: simplemente ocupa otra base ortonormal.

#### c) Espectro

FSK tiende a ocupar más ancho de banda que PSK o QAM, especialmente cuando se usan pulsos abruptos o desviaciones grandes de frecuencia. Su ventaja es la robustez frente a no linealidades del PA, especialmente en variantes de envolvente casi constante como CPFSK o GMSK.

#### d) Detección coherente y no coherente

En detección coherente, el receptor proyecta la señal sobre las dos formas de onda candidatas y escoge la de mayor correlación. Para BFSK ortogonal coherente,

$$
P_b=Q\left(\sqrt{\frac{E_b}{N_0}}\right).
$$

En detección no coherente, el receptor usa detectores de energía. Para BFSK ortogonal no coherente,

$$
P_b=\frac{1}{2}e^{-E_b/(2N_0)}.
$$

La versión no coherente evita sincronización de fase absoluta, pero paga una penalización de desempeño.

**[Figura 3.5]:** comparación entre BFSK coherente y no coherente. La figura debe mostrar dos ramas correladoras o de energía sintonizadas a $f_0$ y $f_1$, y debe remarcar que el receptor coherente usa fase conocida, mientras que el no coherente sólo compara magnitudes o energías.

### 3.2.4 PSK (Phase Shift Keying)

#### a) BPSK: señal, constelación, espectro y BER

En BPSK,

$$
s(t)=\sqrt{\frac{2E_b}{T_b}}\,b_k\,p(t)\cos(2\pi f_c t),
\qquad b_k\in\{+1,-1\}.
$$

En banda base,

$$
a_k\in\{+\sqrt{E_b},-\sqrt{E_b}\}.
$$

La constelación tiene sólo dos puntos sobre el eje real, separados una distancia

$$
d_{\min}=2\sqrt{E_b}.
$$

Su BER en AWGN es

$$
P_b=Q\left(\sqrt{\frac{2E_b}{N_0}}\right).
$$

BPSK es una de las modulaciones más robustas porque maximiza la separación euclidiana para $M=2$.

#### b) Generalización a M-PSK

En M-PSK,

$$
a_m=\sqrt{E_s}e^{j2\pi m/M}, \qquad m=0,1,\dots,M-1.
$$

Los símbolos se distribuyen uniformemente sobre un círculo de radio $\sqrt{E_s}$. La distancia mínima es

$$
d_{\min}=2\sqrt{E_s}\sin\left(\frac{\pi}{M}\right).
$$

A medida que $M$ crece, los puntos se acercan angularmente. Esto mejora la eficiencia espectral pero empeora la robustez al ruido y a errores de fase.

### 3.2.5 QPSK

QPSK transmite dos bits por símbolo. Una formulación habitual es

$$
a_k\in\left\{\sqrt{\frac{E_s}{2}}(\pm1\pm j)\right\}.
$$

#### a) Señal

La señal pasabanda se escribe como

$$
s(t)=I_k p(t)\cos(2\pi f_c t)-Q_k p(t)\sin(2\pi f_c t),
$$

con $I_k,Q_k\in\left\{\pm\sqrt{\frac{E_s}{2}}\right\}$.

#### b) Constelación

Los cuatro puntos están ubicados a $45^\circ$, $135^\circ$, $225^\circ$ y $315^\circ$. Con codificación Gray, símbolos vecinos difieren en un solo bit.

#### c) Relación con BPSK y BER

QPSK puede interpretarse como dos BPSK ortogonales, una en la rama I y otra en la rama Q. Con codificación Gray,

$$
P_b=Q\left(\sqrt{\frac{2E_b}{N_0}}\right),
$$

igual que en BPSK a igualdad de energía por bit.

#### d) Espectro

QPSK es más eficiente espectralmente que BPSK porque transmite dos bits por símbolo sin ensanchar la banda si se mantiene la misma tasa binaria total mediante reducción de la tasa de símbolos.

> **Concepto clave:** QPSK duplica la eficiencia espectral de BPSK manteniendo la misma BER por bit en AWGN, siempre que se compare a igual $E_b/N_0$ y con detección coherente.

### 3.2.6 Conformación de pulsos

La modulación digital no depende sólo de la constelación; también depende del pulso $p(t)$.

#### a) Pulso rectangular

El pulso rectangular es simple, pero su espectro tiene colas laterales lentas:

$$
P(f)=T_s\operatorname{sinc}(fT_s)e^{-j\pi fT_s}.
$$

Ello produce ocupación espectral elevada y sensibilidad a interferencia entre canales adyacentes.

#### b) Pulso coseno alzado

Un pulso de coseno alzado (RC) cumple el criterio de Nyquist de cero ISI. Su respuesta en frecuencia es

$$
P_{RC}(f)=
\begin{cases}
T_s, & |f|\le \frac{1-\alpha}{2T_s},\\
\frac{T_s}{2}\left[1+\cos\left(\frac{\pi T_s}{\alpha}\left(|f|-\frac{1-\alpha}{2T_s}\right)\right)\right], & \frac{1-\alpha}{2T_s}<|f|\le \frac{1+\alpha}{2T_s},\\
0, & |f|>\frac{1+\alpha}{2T_s},
\end{cases}
$$

donde $\alpha$ es el factor de roll-off.

En práctica se usa con frecuencia la pareja **root-raised cosine** en transmisión y recepción, porque

$$
|P_{RRC}(f)|^2=P_{RC}(f).
$$

Esto reparte el filtrado Nyquist entre Tx y Rx y facilita la implementación del filtro adaptado.

### 3.2.7 Análisis espectral comparativo

Bajo una misma tasa binaria, ASK/PSK/QAM lineales con pulsos Nyquist pueden ocupar bandas similares, mientras que FSK suele requerir más banda para garantizar separación suficiente entre frecuencias. Sin embargo, FSK y CPFSK son especialmente atractivas cuando la cadena de RF es fuertemente no lineal.

La eficiencia real depende de:

- la tasa de símbolos,
- el orden de modulación,
- el roll-off del filtro,
- las máscaras espectrales regulatorias,
- la linealidad del PA.

### 3.2.8 Eficiencia espectral comparativa

La eficiencia espectral ideal puede aproximarse por

$$
\eta\approx\frac{\log_2 M}{1+\alpha}\quad \text{bit/s/Hz}
$$

para modulaciones lineales con filtrado Nyquist. Así, en igualdad de $\alpha$, aumentar $M$ incrementa $\eta$, pero también reduce la distancia mínima de la constelación para una potencia media dada.

**Ejemplo 3.4:** comparación rápida entre BPSK y QPSK con $\alpha=0.25$.

Para BPSK, $\log_2 M=1$ y

$$
\eta_{\text{BPSK}}\approx\frac{1}{1.25}=0.8\ \text{bit/s/Hz}.
$$

Para QPSK,

$$
\eta_{\text{QPSK}}\approx\frac{2}{1.25}=1.6\ \text{bit/s/Hz}.
$$

QPSK duplica la eficiencia espectral ideal respecto a BPSK bajo el mismo roll-off.

**Ejemplo 3.5:** BER de BFSK no coherente a $E_b/N_0=8$ dB.

Como $8$ dB equivale a $\gamma_b=10^{0.8}\approx 6.31$,

$$
P_b=\frac{1}{2}e^{-\gamma_b/2}=\frac{1}{2}e^{-3.155}\approx 2.13\times 10^{-2}.
$$

La BER es mucho mayor que la de BPSK en el mismo $E_b/N_0$, lo que ilustra el costo de evitar la referencia de fase.

**Ejemplo 3.6:** distancia mínima en 8-PSK.

Si los puntos tienen energía $E_s$, entonces

$$
d_{\min}=2\sqrt{E_s}\sin\left(\frac{\pi}{8}\right)\approx 0.765\sqrt{E_s}.
$$

En QPSK,

$$
d_{\min}=2\sqrt{E_s}\sin\left(\frac{\pi}{4}\right)=\sqrt{2E_s}\approx 1.414\sqrt{E_s}.
$$

La distancia mínima de 8-PSK es sustancialmente menor; por eso requiere mayor SNR para lograr la misma BER.

**Ejemplo 3.7:** ancho de banda ocupado por un sistema QPSK con $R_b=2$ Mbit/s y $\alpha=0.35$.

Como QPSK transmite $2$ bits por símbolo,

$$
R_s=\frac{R_b}{2}=1\ \text{Msímb/s}.
$$

El ancho de banda aproximado de Nyquist es

$$
B\approx (1+\alpha)R_s=1.35\ \text{MHz}.
$$

---

## 3.3 Modulación de Amplitud en Cuadratura (QAM)

### 3.3.1 Definición y señal QAM general

QAM combina variaciones simultáneas de amplitud y fase mediante la modulación de dos portadoras ortogonales. Su forma general es

$$
s(t)=I(t)\cos(2\pi f_c t)-Q(t)\sin(2\pi f_c t),
$$

o equivalentemente,

$$
s(t)=\Re\{u(t)e^{j2\pi f_c t}\}, \qquad u(t)=I(t)+jQ(t).
$$

Si la señal es digital lineal,

$$
u(t)=\sum_k a_k p(t-kT_s),
$$

donde $a_k$ toma valores de una constelación bidimensional.

### 3.3.2 Constelaciones M-QAM

En constelaciones cuadradas M-QAM, los puntos se organizan en una rejilla cartesiana.

#### a) 4-QAM

4-QAM es equivalente a QPSK.

#### b) 16-QAM

En 16-QAM, las componentes I y Q toman niveles típicos $\{\pm d,\pm 3d\}$. La constelación contiene cuatro niveles por eje y transmite $4$ bits por símbolo.

#### c) 64-QAM

64-QAM usa ocho niveles por eje. Transmite $6$ bits por símbolo y es común en estándares como Wi-Fi y LTE en buenas condiciones de canal.

#### d) 256-QAM

256-QAM usa dieciséis niveles por eje y transmite $8$ bits por símbolo. Exige alta SNR, baja EVM y muy buena calibración de RF.

**[Figura 3.6]:** evolución visual de 4-QAM, 16-QAM, 64-QAM y 256-QAM. La figura debe mostrar cómo aumenta la densidad de puntos en el plano $I$-$Q$ y cómo disminuye la separación entre símbolos vecinos. El mensaje central es que la eficiencia espectral crece, pero también la sensibilidad a ruido e impairments.

### 3.3.3 Codificación Gray en constelaciones

La codificación Gray asigna etiquetas binarias de modo que puntos adyacentes difieran en un solo bit. Esto reduce la probabilidad de múltiples errores de bit cuando ocurre un error de símbolo hacia un vecino cercano.

Si la probabilidad de error está dominada por vecinos inmediatos, Gray coding hace que

$$
P_b\approx \frac{P_s}{\log_2 M},
$$

relación especialmente útil a alta SNR.

### 3.3.4 Análisis espectral de QAM

QAM es una modulación lineal, por lo que su espectro está dominado por el pulso conformador. Si se usa RRC, el ancho de banda aproximado es

$$
B\approx (1+\alpha)R_s.
$$

Lo relevante no es sólo el ancho de banda ocupado, sino también:

- la máscara espectral,
- la regrowth espectral debida al PA,
- la EVM permitida por el estándar,
- la supresión de la imagen I/Q.

### 3.3.5 Impairments en QAM

QAM es especialmente sensible a degradaciones de la cadena analógica.

#### a) Desbalance I/Q

Un desbalance de ganancia o fase deforma la constelación, rompe la ortogonalidad y crea interferencia-imagen.

#### b) Offset de portadora

Un pequeño error de frecuencia hace rotar la constelación con el tiempo. En constelaciones densas, esa rotación puede causar múltiples errores antes de ser corregida.

#### c) No linealidades

El PA produce compresión AM/AM y conversión AM/PM. Los puntos más externos de la constelación son los más afectados, lo que eleva la EVM y ensancha el espectro.

> **Concepto clave:** QAM logra alta eficiencia espectral, pero sólo cuando el transmisor y el receptor preservan con gran fidelidad las magnitudes y fases relativas de la constelación.

### 3.3.6 Eficiencia espectral de M-QAM

Para M-QAM cuadrada,

$$
\eta\approx\frac{\log_2 M}{1+\alpha}\quad \text{bit/s/Hz}.
$$

Así, con $\alpha=0.2$,

$$
\eta_{16\text{-QAM}}\approx\frac{4}{1.2}=3.33\ \text{bit/s/Hz},
$$

$$
\eta_{64\text{-QAM}}\approx\frac{6}{1.2}=5\ \text{bit/s/Hz},
$$

$$
\eta_{256\text{-QAM}}\approx\frac{8}{1.2}=6.67\ \text{bit/s/Hz}.
$$

### 3.3.7 Comparación con M-PSK

A igual orden $M$, QAM suele ofrecer mejor eficiencia energética que M-PSK porque utiliza los dos grados de libertad del plano complejo para separar mejor los puntos. Sin embargo, la amplitud ya no es constante, por lo que la linealidad del transmisor se vuelve crítica.

### 3.3.8 Ejemplos resueltos

**Ejemplo 3.8:** energía media de 16-QAM no normalizada.

Sea una constelación con niveles por eje $\{\pm d,\pm 3d\}$. La energía media por eje es

$$
E[I^2]=\frac{1}{4}(d^2+d^2+9d^2+9d^2)=5d^2.
$$

Como la constelación es separable,

$$
E_s=E[I^2]+E[Q^2]=10d^2.
$$

Para normalizar a energía unidad debe elegirse

$$
d=\frac{1}{\sqrt{10}}.
$$

**Ejemplo 3.9:** BER aproximada de 16-QAM a $E_b/N_0=12$ dB.

Con $\gamma_b=10^{1.2}\approx 15.85$ y $k=4$,

$$
P_b\approx \frac{4}{4}\left(1-\frac{1}{4}\right)Q\left(\sqrt{\frac{3\cdot 4}{15}\gamma_b}\right)
=\frac{3}{4}Q\left(\sqrt{0.8\cdot 15.85}\right).
$$

Como $\sqrt{12.68}\approx 3.56$,

$$
Q(3.56)\approx 1.85\times 10^{-4},
$$

y por tanto

$$
P_b\approx 1.39\times 10^{-4}.
$$

**Ejemplo 3.10:** tasa de datos con 64-QAM.

Si el sistema transmite a $R_s=5$ Msímb/s, entonces con 64-QAM ($6$ bits por símbolo),

$$
R_b=6R_s=30\ \text{Mbit/s}.
$$

Si además $\alpha=0.25$,

$$
B\approx (1+0.25)5=6.25\ \text{MHz},
$$

y la eficiencia espectral ideal es

$$
\eta\approx \frac{30}{6.25}=4.8\ \text{bit/s/Hz}.
$$

---

## 3.4 Detección y Demodulación

### 3.4.1 Modelo de recepción

En presencia de AWGN, el modelo continuo básico es

$$
r(t)=s_i(t)+n(t),
$$

donde $s_i(t)$ es una de las señales posibles y $n(t)$ es ruido blanco gaussiano con densidad espectral bilateral $N_0/2$.

Tras proyectar sobre una base ortonormal o aplicar el filtro adaptado y muestrear, el modelo discreto equivalente queda

$$
\mathbf{r}=\mathbf{s}_i+\mathbf{n},
$$

con $\mathbf{n}\sim \mathcal{N}(\mathbf{0},\frac{N_0}{2}\mathbf{I})$ en representación real, o bien $n\sim\mathcal{CN}(0,N_0)$ por dimensión compleja.

### 3.4.2 Diseño de receptores óptimos: filtro adaptado

Sea un filtro LTI de respuesta $h(t)$ y transformada $H(f)$. La salida debida a la señal en el instante de decisión $T$ vale

$$
y_s(T)=\int_{-\infty}^{\infty}S(f)H(f)e^{j2\pi fT}\,df.
$$

La varianza del ruido a la salida es

$$
\sigma_n^2=\frac{N_0}{2}\int_{-\infty}^{\infty}|H(f)|^2df.
$$

Por tanto, la SNR de salida es

$$
\mathrm{SNR}_{out}=\frac{\left|\int S(f)H(f)e^{j2\pi fT}df\right|^2}{\frac{N_0}{2}\int |H(f)|^2df}.
$$

Aplicando la desigualdad de Cauchy-Schwarz se concluye que la SNR se maximiza cuando

$$
H_{MF}(f)=K S^*(f)e^{-j2\pi fT},
$$

donde $K$ es una constante arbitraria. En tiempo,

$$
h_{MF}(t)=Ks^*(T-t).
$$

Éste es el **filtro adaptado**: una versión invertida en el tiempo y conjugada de la señal buscada.

La SNR máxima resultante es

$$
\mathrm{SNR}_{max}=\frac{2E_s}{N_0}.
$$

**[Figura 3.7]:** diagrama del receptor óptimo con filtro adaptado: señal ruidosa de entrada, filtro cuya respuesta es el espejo temporal del pulso transmitido, bloque de muestreo en el instante óptimo y dispositivo de decisión. La descripción debe subrayar que el filtro adaptado no elimina el ruido, sino que concentra la energía útil del símbolo en el instante de muestreo maximizando la SNR.

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
\hat{i}=\arg\min_i\|\mathbf{r}-\mathbf{s}_i\|^2.
$$

Esta regla coincide con el criterio de máxima verosimilitud en AWGN.

### 3.4.4 Demodulación coherente vs. no coherente

#### a) Detección coherente: derivación completa

La demodulación coherente asume que el receptor conoce o estima con precisión la fase y frecuencia de la portadora. Para un conjunto de símbolos equiprobables $\{s_m(t)\}$ en AWGN,

$$
p(r|s_m)\propto \exp\left(-\frac{1}{N_0}\int_0^T |r(t)-s_m(t)|^2dt\right).
$$

La regla ML es entonces

$$
\hat{m}=\arg\max_m p(r|s_m)=\arg\min_m \int_0^T |r(t)-s_m(t)|^2dt.
$$

Expandiendo,

$$
\int |r-s_m|^2dt=\int |r|^2dt+\int |s_m|^2dt-2\Re\left\{\int r(t)s_m^*(t)dt\right\}.
$$

Como el primer término no depende de $m$, y si las energías son iguales el segundo tampoco, la decisión equivalente es

$$
\hat{m}=\arg\max_m \Re\left\{\int_0^T r(t)s_m^*(t)dt\right\}.
$$

Para BPSK, si se usa la función base unitaria $\phi(t)$, la salida del correlador es

$$
z=\int_0^T r(t)\phi(t)dt=\pm\sqrt{E_b}+n_0,
$$

donde $n_0\sim\mathcal{N}(0,N_0/2)$. La regla de decisión es simplemente

$$
\hat{b}=
\begin{cases}
0,& z>0,\\
1,& z<0.
\end{cases}
$$

De ahí se obtiene

$$
P_b=Q\left(\sqrt{\frac{2E_b}{N_0}}\right).
$$

#### b) Detección no coherente: derivación básica

En detección no coherente la fase absoluta es desconocida y se trata como parámetro aleatorio o molesto. Considérese BFSK ortogonal. Las salidas complejas de dos correladores sintonizados pueden modelarse como

$$
y_1=\sqrt{E_b}e^{j\theta}+n_1,
\qquad
y_0=n_0
$$

si se transmitió el símbolo 1, con $\theta$ desconocida y uniforme en $[0,2\pi)$. La verosimilitud condicional marginalizada respecto de $\theta$ es

$$
p(y_1,y_0|s_1)=C\exp\left(-\frac{|y_1|^2+|y_0|^2+E_b}{N_0}\right)I_0\left(\frac{2\sqrt{E_b}|y_1|}{N_0}\right),
$$

donde $I_0(\cdot)$ es la función de Bessel modificada de orden cero. Como $I_0(x)$ es monótonamente creciente, la regla óptima se reduce a comparar energías:

$$
\hat{b}=1 \quad \text{si} \quad |y_1|^2>|y_0|^2.
$$

Para BFSK ortogonal no coherente,

$$
P_b=\frac{1}{2}e^{-E_b/(2N_0)}.
$$

#### c) Detección diferencial

Una alternativa intermedia es DPSK, donde la información se codifica en el cambio de fase entre símbolos consecutivos. Si $r_k$ es la muestra compleja del símbolo $k$, la estadística diferencial es

$$
z_k=r_k r_{k-1}^*.
$$

La decisión se toma sobre el signo del ángulo de $z_k$ o sobre la parte real, según el esquema. Para DBPSK en AWGN,

$$
P_b=\frac{1}{2}e^{-E_b/N_0}.
$$

#### d) Interpretación física

- **Coherente:** usa referencia de fase; mejor BER; requiere lazo de sincronización.
- **No coherente:** evita fase absoluta; más simple; peor BER.
- **Diferencial:** evita fase absoluta instantánea pero conserva sensibilidad a ruido entre símbolos adyacentes.

> **Concepto clave:** la diferencia entre receptores coherentes y no coherentes no es meramente arquitectónica; cambia la estadística suficiente y, por tanto, el límite de desempeño alcanzable.

**[Figura 3.8]:** comparación entre constelación estabilizada por recuperación de portadora y constelación observada sin referencia coherente. La primera debe mostrarse fija y agrupada; la segunda, girando o difusa. La descripción debe enfatizar que la recuperación de portadora convierte un problema temporal de sincronización en un problema geométrico estable de decisión.

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

Si $k=\log_2 M$,

$$
P_b\approx \frac{4}{k}\left(1-\frac{1}{\sqrt{M}}\right)Q\left(\sqrt{\frac{3k}{M-1}\gamma_b}\right).
$$

Estas expresiones explican las curvas BER frente a $E_b/N_0$: a medida que la modulación se hace de mayor orden, la curva se desplaza hacia la derecha, es decir, requiere más SNR para la misma BER.

**[Figura 3.9]:** familia de curvas BER semilogarítmicas frente a $E_b/N_0$ para BPSK, QPSK, 16-QAM y 64-QAM. BPSK y QPSK deben coincidir; 16-QAM debe aparecer desplazada a la derecha; 64-QAM aún más. La descripción debe indicar que la pendiente refleja la naturaleza exponencial de la función $Q(\cdot)$ y que el precio de mayor eficiencia espectral es una mayor exigencia de SNR.

### 3.4.6 Distancia mínima y probabilidad de error

En AWGN, la probabilidad de confundir símbolos depende primordialmente de la distancia mínima $d_{\min}$ de la constelación. Para detección binaria equiprobable,

$$
P_e=Q\left(\frac{d}{\sqrt{2N_0}}\right),
$$

donde $d$ es la distancia entre ambas señales en el espacio euclidiano.

Para constelaciones generales, una cota por unión es

$$
P_s\le \sum_{j\neq i}Q\left(\frac{d_{ij}}{\sqrt{2N_0}}\right),
$$

y a alta SNR suele dominar el vecino más cercano, por lo que intuitivamente

$$
P_s\propto Q\left(\frac{d_{\min}}{\sqrt{2N_0}}\right).
$$

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

que resulta idéntico al propio pulso por su simetría temporal. La salida en $t=T$ es la integral de la señal recibida sobre el intervalo del símbolo. Esto muestra que el receptor *integrate-and-dump* es un caso particular de filtro adaptado.

**Ejemplo 3.12:** comparación de BER entre BPSK y 16-QAM a $E_b/N_0=10$ dB.

Para BPSK,

$$
P_b^{\text{BPSK}}=Q(\sqrt{20})\approx 3.87\times 10^{-6}.
$$

Para 16-QAM,

$$
P_b^{16\text{-QAM}}\approx \frac{3}{4}Q\left(\sqrt{8}\right)\approx 1.76\times 10^{-3}.
$$

La diferencia es enorme: la mayor eficiencia espectral de 16-QAM se obtiene a costa de una sensibilidad mucho mayor al ruido.

**Ejemplo 3.13:** comparación entre BFSK coherente y no coherente para $E_b/N_0=6$ dB.

Con $\gamma_b=10^{0.6}\approx 3.98$,

$$
P_b^{\text{coh}}=Q(\sqrt{3.98})\approx Q(1.995)\approx 2.3\times 10^{-2}.
$$

Para BFSK no coherente,

$$
P_b^{\text{no coh}}=\frac{1}{2}e^{-3.98/2}\approx 6.8\times 10^{-2}.
$$

La penalización por no conocer la fase es clara.

---

## 3.5 Impairments en el Canal y la Cadena Tx-Rx

### 3.5.1 Visión general

Los modelos ideales de las secciones anteriores suponen sincronización perfecta, osciladores idénticos, ramas I/Q equilibradas y canales invariantes. En un sistema real, la observación del receptor se parece más a una versión distorsionada, rotada, retrasada y filtrada del símbolo transmitido. Una formulación útil es

$$
r(t)=\mathcal{D}\left\{\sum_{\ell=0}^{L-1} h_\ell s(t-\tau_\ell)\right\}+n(t),
$$

donde $\mathcal{D}\{\cdot\}$ resume efectos de CFO, offset de fase, error de temporización, desbalance I/Q y otras imperfecciones de hardware.

> **Concepto clave:** la constelación observada en el receptor no sólo refleja ruido; también refleja la física del hardware y del canal. Interpretar correctamente esa geometría es esencial para sincronizar, ecualizar y demodular.

### 3.5.2 Carrier Frequency Offset (CFO)

Si existe una diferencia $\Delta f=f_c-\hat{f}_c$ entre la portadora real y la estimada, el equivalente complejo recibido es

$$
r(t)=s(t)e^{j2\pi \Delta f t}+n(t).
$$

En tiempo discreto, muestreando a ritmo de símbolo,

$$
r[k]=a_k e^{j2\pi \Delta f kT_s}+w[k].
$$

El CFO produce una rotación progresiva de la constelación. El incremento angular por símbolo es

$$
\Delta \theta=2\pi \Delta f T_s.
$$

Si $\Delta \theta$ es pequeño, la constelación gira lentamente; si es grande, el receptor pierde la referencia antes de completar la decisión.

#### a) Impacto geométrico

Para un símbolo ideal $a_k=\rho e^{j\theta_k}$,

$$
r[k]=\rho e^{j(\theta_k+2\pi \Delta f kT_s)}+w[k].
$$

Es decir, el radio no cambia, pero el ángulo sí. En QPSK o QAM, este efecto puede desplazar un punto hacia otra región de decisión.

#### b) Estimación y corrección

Los métodos más comunes son:

1. **Estimación basada en preámbulo o pilotos**:
   $$
   \widehat{\Delta f}=\frac{1}{2\pi NT_s}\angle\left(\sum_{k=0}^{N-1}r[k+N]r^*[k]\right).
   $$
2. **Métodos no asistidos por datos** usando periodicidades estadísticas, por ejemplo elevar a la potencia $M$ en M-PSK:
   $$
   z[k]=r[k]^M\approx |a_k|^M e^{j2\pi M\Delta f kT_s}.
   $$
3. **Lazos de seguimiento** como FLL/PLL o Costas loop, que corrigen residuales en tiempo real.

Una vez estimado el CFO, la compensación es

$$
\tilde{r}[k]=r[k]e^{-j2\pi \widehat{\Delta f}kT_s}.
$$

**[Figura 3.10]:** constelación QPSK observada con CFO. Debe mostrarse una secuencia de nubes girando con el tiempo alrededor del origen. La descripción debe resaltar que no se trata de un simple ensanchamiento aleatorio, sino de una rotación sistemática cuya velocidad es proporcional a $\Delta f$.

### 3.5.3 Phase Offset

Si el receptor tiene un error de fase constante $\phi_0$, el modelo es

$$
r(t)=s(t)e^{j\phi_0}+n(t).
$$

A diferencia del CFO, el offset de fase produce una **rotación estática** de la constelación. En discreto,

$$
r[k]=a_k e^{j\phi_0}+w[k].
$$

La corrección consiste en estimar $\phi_0$ y multiplicar por $e^{-j\widehat{\phi}_0}$. Los estimadores pueden basarse en pilotos, preámbulos o decisiones retroalimentadas.

Si el receptor conoce una secuencia piloto $p_k$, una estimación simple es

$$
\widehat{\phi}_0=\angle\left(\sum_k r[k]p_k^*\right).
$$

### 3.5.4 Sincronización temporal de símbolo

Supóngase que la señal filtrada total es

$$
y(t)=\sum_k a_k g(t-kT_s-\tau)+w(t),
$$

donde $g(t)=p(t)*h_{MF}(t)$ y $\tau$ es el error temporal residual. Al muestrear en $t=mT_s$,

$$
y[m]=\sum_k a_k g((m-k)T_s-\tau)+w[m].
$$

Si $\tau\neq 0$, el símbolo deseado se atenúa y aparecen contribuciones de símbolos vecinos. Es decir, un error temporal genera simultáneamente **pérdida de SNR útil** e **ISI residual**.

#### a) Detector early-late gate

Una forma clásica de estimar $\tau$ compara muestras tempranas y tardías alrededor del instante actual. Una forma simplificada del error es

$$
e[m]=\Re\left\{z_p^*[m]\big(z_e[m]-z_l[m]\big)\right\},
$$

donde $z_e[m]$, $z_p[m]$ y $z_l[m]$ son las muestras *early*, *prompt* y *late*. Si $e[m]>0$, el reloj se desplaza en una dirección; si $e[m]<0$, en la contraria.

#### b) Algoritmo Mueller-Muller

Para señales PAM/QAM, un detector ampliamente usado es Mueller-Muller (M&M). Una forma representativa del error es

$$
e[m]=\Re\left\{y[m]\hat{a}^*[m-1]-y[m-1]\hat{a}^*[m]\right\},
$$

donde $\hat{a}[m]$ es la decisión del símbolo. El TED M&M explota la propiedad de simetría local de los pulsos Nyquist alrededor del instante óptimo.

**[Figura 3.11]:** diagrama de ojo ideal y diagrama de ojo con desfase temporal. La figura debe mostrar claramente cómo un error de muestreo reduce la apertura vertical y horizontal del ojo, acercando el instante de decisión a regiones con mayor ISI y ruido. El mensaje visual debe ser que la sincronización temporal es un problema geométrico en el tiempo.

### 3.5.5 IQ Imbalance

Un mezclador en cuadratura ideal requiere ganancias iguales en I y Q y un desfase exacto de $90^\circ$. Si hay desbalance de ganancia $\epsilon$ y error de fase $\phi$, el equivalente complejo puede expresarse como

$$
r(t)=\alpha s(t)+\beta s^*(t)+n(t),
$$

donde

$$
\alpha=\frac{1}{2}\left[(1+\epsilon)e^{-j\phi/2}+(1-\epsilon)e^{j\phi/2}\right],
$$

$$
\beta=\frac{1}{2}\left[(1+\epsilon)e^{j\phi/2}-(1-\epsilon)e^{-j\phi/2}\right].
$$

El término $\beta s^*(t)$ es una **imagen compleja conjugada** que rompe la separación limpia entre bandas positiva y negativa. La relación de rechazo de imagen (IRR) se define como

$$
\mathrm{IRR}=\frac{|\alpha|^2}{|\beta|^2}.
$$

Cuanto mayor es la IRR, menor es la interferencia imagen. La compensación digital suele consistir en estimar $\alpha$ y $\beta$ y aplicar un ecualizador *widely linear*.

**[Figura 3.12]:** constelación QAM afectada por desbalance I/Q y representación espectral de la imagen. La figura debe mostrar nubes elípticas y sesgadas, junto con un espectro donde aparece una réplica no deseada respecto a la frecuencia imagen. La descripción debe remarcar que el desbalance I/Q no es sólo una rotación o escalado simple: introduce un término conjugado que mezcla información y su imagen.

### 3.5.6 Desvanecimiento multitrayecto: Rayleigh y Rician

El canal multitrayecto de baja movilidad puede modelarse como

$$
h(t,\tau)=\sum_{\ell=0}^{L-1} \alpha_\ell(t)e^{j\varphi_\ell(t)}\delta(\tau-\tau_\ell).
$$

Si el ancho de banda de la señal es estrecho respecto del inverso de la dispersión temporal, puede aproximarse como un canal plano complejo

$$
r(t)=h s(t)+n(t).
$$

#### a) Rayleigh

Si no existe componente dominante de línea de vista (LOS) y el canal es la suma de muchos reflejos pequeños, entonces por el teorema central del límite

$$
h=h_I+jh_Q,
$$

con $h_I$ y $h_Q$ gaussianas de media cero y varianza $\sigma^2$. La envolvente $\alpha=|h|$ tiene densidad

$$
p_\alpha(a)=\frac{a}{\sigma^2}e^{-a^2/(2\sigma^2)}, \qquad a\ge 0.
$$

Ésta es la distribución de Rayleigh.

#### b) Rician

Si además existe una componente LOS determinista $m$, entonces

$$
h=m+g,
$$

con $g\sim\mathcal{CN}(0,2\sigma^2)$. La envolvente cumple una distribución de Rice:

$$
p_\alpha(a)=\frac{a}{\sigma^2}\exp\left(-\frac{a^2+|m|^2}{2\sigma^2}\right)I_0\left(\frac{a|m|}{\sigma^2}\right),\qquad a\ge 0.
$$

El factor de Rice es

$$
K=\frac{|m|^2}{2\sigma^2}.
$$

Cuando $K\to 0$, el canal se aproxima a Rayleigh; cuando $K\to\infty$, se aproxima a un canal casi AWGN con ganancia determinista.

#### c) Impacto en la BER

Para BPSK coherente en Rayleigh plano, la BER media es

$$
\bar{P}_b=\frac{1}{2}\left(1-\sqrt{\frac{\gamma_b}{1+\gamma_b}}\right).
$$

Esta expresión es mucho peor que la de AWGN puro, mostrando el impacto severo del desvanecimiento profundo.

**[Figura 3.13]:** canal multitrayecto con varias trayectorias de distinta amplitud y retardo, y su consecuencia sobre la respuesta impulsional. La figura debe representar al menos una trayectoria LOS y varias reflejadas, así como la suma de taps complejos que genera dispersión temporal, desvanecimientos selectivos y rotaciones de fase dependientes de frecuencia.

### 3.5.7 Modelo combinado de impairments

En un sistema real, varios efectos aparecen simultáneamente. Un modelo discreto suficientemente general es

$$
r[k]=\alpha e^{j(2\pi \Delta f kT_s+\phi_0)}\sum_{\ell=0}^{L-1} h_\ell a_{k-\ell} g(\tau-\ell T_s)
+\beta e^{-j(2\pi \Delta f kT_s+\phi_0)}\left(\sum_{\ell=0}^{L-1} h_\ell a_{k-\ell} g(\tau-\ell T_s)\right)^*+w[k].
$$

Este modelo reúne:

- **CFO** mediante $e^{j2\pi \Delta f kT_s}$,
- **offset de fase** mediante $e^{j\phi_0}$,
- **error temporal** mediante $g(\tau-\ell T_s)$,
- **multitrayecto** mediante $h_\ell$,
- **desbalance I/Q** mediante $\alpha$ y $\beta$,
- **ruido** mediante $w[k]$.

La cadena típica de mitigación sigue el orden:

1. control de ganancia y ADC,
2. corrección gruesa de frecuencia,
3. sincronización temporal,
4. filtro adaptado y muestreo,
5. corrección fina de frecuencia y fase,
6. ecualización del canal,
7. compensación I/Q residual,
8. demapper y decodificación.

### 3.5.8 Ejemplos resueltos

**Ejemplo 3.14:** impacto numérico del CFO.

Supóngase QPSK con período de símbolo $T_s=100\ \mu s$ y un error de frecuencia $\Delta f=250$ Hz. La rotación por símbolo es

$$
\Delta \theta=2\pi \Delta f T_s=2\pi(250)(100\times 10^{-6})\approx 0.157\ \text{rad}=9^\circ.
$$

Luego de $5$ símbolos, la rotación acumulada es

$$
5\Delta\theta=45^\circ.
$$

Un símbolo originalmente ubicado en $\frac{1+j}{\sqrt{2}}$ pasa de un ángulo de $45^\circ$ a uno de $90^\circ$, quedando prácticamente sobre el eje imaginario y muy próximo al borde entre regiones de decisión. Este ejemplo muestra por qué incluso offsets modestos pueden ser críticos en pocos símbolos.

**Ejemplo 3.15:** impacto de un offset de fase estático.

Considérese nuevamente el símbolo QPSK

$$
a=\frac{1+j}{\sqrt{2}}=e^{j45^\circ}
$$

y un error de fase $\phi_0=20^\circ$. La observación ideal sin ruido es

$$
r=ae^{j20^\circ}=e^{j65^\circ}.
$$

Por tanto,

$$
r=\cos 65^\circ + j\sin 65^\circ \approx 0.423 + j0.906.
$$

El margen mínimo respecto de los ejes de decisión baja de $0.707$ a $0.423$. La relación entre ambos márgenes es

$$
\frac{0.423}{0.707}\approx 0.598,
$$

lo que equivale a una reducción de potencia efectiva cercana a

$$
20\log_{10}(0.598)\approx -4.47\ \text{dB}
$$

en el margen geométrico de la componente más crítica.

**Ejemplo 3.16:** pérdida por error temporal con pulso coseno alzado.

Para un pulso RC con $\alpha=0.25$, el valor normalizado del pulso en $\tau=0.2T_s$ es aproximadamente

$$
g(0.2T_s)\approx 0.933.
$$

Esto significa que el símbolo útil se atenúa un $6.7\%$ en amplitud. La pérdida de potencia equivalente es

$$
10\log_{10}(0.933^2)\approx -0.60\ \text{dB}.
$$

Además, las muestras vecinas dejan de ser nulas, por lo que aparece ISI residual. Un pequeño error temporal puede degradar notablemente el rendimiento aun antes de que la constelación parezca visualmente muy dispersa.

**Ejemplo 3.17:** desbalance I/Q y rechazo de imagen.

Supóngase un desbalance de ganancia $\epsilon=0.1$ y error de fase $\phi=5^\circ$. Sustituyendo en las expresiones de $\alpha$ y $\beta$ se obtiene aproximadamente

$$
|\alpha|\approx 0.999,
\qquad
|\beta|\approx 0.109.
$$

Luego,

$$
\mathrm{IRR}=\frac{|\alpha|^2}{|\beta|^2}\approx 84.0,
$$

y en decibelios,

$$
\mathrm{IRR}_{dB}=10\log_{10}(84.0)\approx 19.24\ \text{dB}.
$$

Es decir, la imagen aparece sólo $19.24$ dB por debajo de la señal útil, valor claramente insuficiente para constelaciones densas.

**Ejemplo 3.18:** BER de BPSK en Rayleigh frente a AWGN para $E_b/N_0=10$ dB.

En AWGN,

$$
P_b^{AWGN}=Q(\sqrt{20})\approx 3.87\times 10^{-6}.
$$

En Rayleigh plano,

$$
\bar{P}_b^{Rayleigh}=\frac{1}{2}\left(1-\sqrt{\frac{10}{11}}\right)\approx 2.33\times 10^{-2}.
$$

La degradación es enorme: el desvanecimiento produce una BER varias órdenes de magnitud peor que el canal AWGN puro.

---

## 3.6 Decisión Óptima Basada en Log-Likelihood Ratios (LLRs)

### 3.6.1 De MAP a LLR: derivación completa

En detección binaria sobre una observación $\mathbf{r}$, la regla MAP decide $b_k=0$ si

$$
P(b_k=0|\mathbf{r})>P(b_k=1|\mathbf{r}).
$$

Usando Bayes,

$$
P(b_k=i|\mathbf{r})=\frac{p(\mathbf{r}|b_k=i)P(b_k=i)}{p(\mathbf{r})},\qquad i\in\{0,1\}.
$$

Como $p(\mathbf{r})$ es común, la comparación equivalente es

$$
\frac{p(\mathbf{r}|b_k=0)P(b_k=0)}{p(\mathbf{r}|b_k=1)P(b_k=1)}\mathop{\gtrless}_{b_k=1}^{b_k=0} 1.
$$

Tomando logaritmo natural se define el **log-likelihood ratio**

$$
L(b_k)=\ln\frac{P(b_k=0|\mathbf{r})}{P(b_k=1|\mathbf{r})}.
$$

La regla óptima es simplemente

$$
\hat{b}_k=
\begin{cases}
0,&L(b_k)>0,\\
1,&L(b_k)<0.
\end{cases}
$$

El valor absoluto $|L(b_k)|$ mide la confiabilidad: cuanto mayor es, más segura es la decisión.

> **Concepto clave:** la salida verdaderamente informativa del demodulador moderno no es el bit duro, sino el LLR, porque contiene simultáneamente decisión y confianza.

### 3.6.2 LLR bit a bit para constelaciones M-arias

Sea $\mathcal{S}_{k,0}$ el subconjunto de símbolos cuyo bit $k$ vale $0$ y $\mathcal{S}_{k,1}$ el subconjunto con bit $1$. En AWGN complejo con símbolos equiprobables,

$$
p(\mathbf{r}|s_m)=\frac{1}{(\pi N_0)^n}\exp\left(-\frac{\|\mathbf{r}-\mathbf{s}_m\|^2}{N_0}\right).
$$

Entonces

$$
L(b_k)=\ln\frac{\sum_{s\in\mathcal{S}_{k,0}}\exp\left(-\frac{\|\mathbf{r}-s\|^2}{N_0}\right)}{\sum_{s\in\mathcal{S}_{k,1}}\exp\left(-\frac{\|\mathbf{r}-s\|^2}{N_0}\right)}.
$$

Si existen *a priori* no equiprobables, deben incluirse dentro de cada suma como factores adicionales.

### 3.6.3 Aproximación max-log

En SNR moderada o alta, cada suma suele estar dominada por el símbolo más cercano. Entonces,

$$
\ln\sum_i e^{-x_i}\approx -\min_i x_i,
$$

y se obtiene la aproximación **max-log**:

$$
L(b_k)\approx \frac{1}{N_0}\left[\min_{s\in\mathcal{S}_{k,1}}\|\mathbf{r}-s\|^2-\min_{s\in\mathcal{S}_{k,0}}\|\mathbf{r}-s\|^2\right].
$$

Esta expresión es extremadamente importante porque convierte el cálculo de LLRs en una comparación de distancias euclidianas mínimas, fácil de implementar en hardware.

### 3.6.4 LLRs explícitos para BPSK, QPSK y 16-QAM

#### a) BPSK

Si los símbolos son $\{+A,-A\}$ y la observación real es $r$, entonces

$$
L(b)=\ln\frac{\exp\left(-\frac{(r-A)^2}{N_0}\right)}{\exp\left(-\frac{(r+A)^2}{N_0}\right)}
=\frac{(r+A)^2-(r-A)^2}{N_0}.
$$

Por tanto,

$$
L(b)=\frac{4Ar}{N_0}.
$$

Si $A=\sqrt{E_b}$,

$$
L(b)=\frac{4\sqrt{E_b}}{N_0}r.
$$

#### b) QPSK

Para QPSK Gray, las ramas I y Q son dos BPSK independientes. Si

$$
s=I+jQ,\qquad I,Q\in\{\pm A\},
$$

y se observa $r=r_I+jr_Q$, entonces

$$
L(b_I)=\frac{4Ar_I}{N_0},
\qquad
L(b_Q)=\frac{4Ar_Q}{N_0}.
$$

Si la constelación está normalizada con $A=\sqrt{E_s/2}$, basta sustituir ese valor.

#### c) 16-QAM

Considérese una 16-QAM Gray separable con niveles por eje $\{\pm d,\pm 3d\}$. Para la componente I, defínanse:

- bit más significativo de signo: $b_{I,MSB}=0$ para $\{+d,+3d\}$ y $1$ para $\{-d,-3d\}$,
- bit menos significativo de amplitud: $b_{I,LSB}=0$ para $\{\pm 3d\}$ y $1$ para $\{\pm d\}$.

Si la observación en el eje I es $y$, los LLR exactos son

$$
L(b_{I,MSB})=
\ln\frac{e^{-\frac{(y-d)^2}{N_0}}+e^{-\frac{(y-3d)^2}{N_0}}}{e^{-\frac{(y+d)^2}{N_0}}+e^{-\frac{(y+3d)^2}{N_0}}},
$$

$$
L(b_{I,LSB})=
\ln\frac{e^{-\frac{(y-3d)^2}{N_0}}+e^{-\frac{(y+3d)^2}{N_0}}}{e^{-\frac{(y-d)^2}{N_0}}+e^{-\frac{(y+d)^2}{N_0}}}.
$$

Para el eje Q se obtienen expresiones análogas sustituyendo $y$ por $r_Q$.

Con max-log,

$$
L(b_{I,MSB})\approx \frac{1}{N_0}\left[\min\big((y+d)^2,(y+3d)^2\big)-\min\big((y-d)^2,(y-3d)^2\big)\right],
$$

$$
L(b_{I,LSB})\approx \frac{1}{N_0}\left[\min\big((y-d)^2,(y+d)^2\big)-\min\big((y-3d)^2,(y+3d)^2\big)\right].
$$

**[Figura 3.14]:** curvas LLR de BPSK y QPSK en función de la muestra recibida. La figura debe mostrar rectas que cruzan por cero en el umbral de decisión, con pendiente proporcional a $1/N_0$. La descripción debe resaltar que una observación alejada del umbral no sólo decide el bit, sino que lo hace con alta confiabilidad.

**[Figura 3.15]:** partición de una constelación 16-QAM en subconjuntos asociados a cada bit y visualización geométrica del max-log. Debe mostrarse cómo, para cada bit, el demapper compara la distancia a dos grupos de puntos, no simplemente al símbolo más cercano global. Esto ayuda a entender por qué el demapper blando alimenta a los decodificadores modernos.

### 3.6.5 Soft-decision vs. hard-decision

En decisión dura, el demodulador produce sólo $\hat{b}_k\in\{0,1\}$. En decisión blanda produce $L(b_k)$ o una cuantización de él. La decisión dura descarta información de confiabilidad. Por ejemplo, las observaciones $r=0.01$ y $r=2$ en BPSK producen el mismo bit duro si son positivas, aunque su confiabilidad sea radicalmente distinta.

En sistemas codificados, esta diferencia se traduce en ganancia de desempeño. En muchos esquemas convolucionales, turbo o LDPC, la entrada blanda proporciona ganancias típicas del orden de $1$ a $2$ dB frente a entrada dura para la misma BER objetivo.

### 3.6.6 Conexión con codificación de canal

Los decodificadores modernos operan sobre métricas blandas:

- Viterbi blando usa distancias o LLRs cuantizados,
- turbo decoders intercambian información extrínseca en forma de LLR,
- LDPC decoders implementan *belief propagation* con mensajes logarítmicos.

Si el demapper entrega LLRs mal escalados, el decodificador puede degradarse aunque el signo de los bits sea correcto. Por ello, la estimación de $N_0$, la compensación de impairments y la correcta normalización de las distancias son pasos esenciales.

> **Concepto clave:** el demapper blando es la interfaz crítica entre modulación y codificación de canal; un buen diseño conjunto Tx-Rx casi siempre requiere explotar LLRs y no sólo bits duros.

### 3.6.7 Ejemplos resueltos

**Ejemplo 3.19:** LLR en BPSK.

Supóngase BPSK con $A=1$, $N_0=0.5$ y una observación $r=0.35$. Entonces

$$
L(b)=\frac{4Ar}{N_0}=\frac{4(1)(0.35)}{0.5}=2.8.
$$

Como $L(b)>0$, se decide $b=0$ (asociado al símbolo $+1$). Además,

$$
\frac{P(b=0|r)}{P(b=1|r)}=e^{2.8}\approx 16.44.
$$

La decisión no sólo es favorable a $b=0$, sino claramente confiable.

**Ejemplo 3.20:** LLRs en QPSK.

Considérese QPSK con $A=1$, $N_0=0.4$ y observación

$$
r=0.25-0.9j.
$$

Entonces

$$
L(b_I)=\frac{4Ar_I}{N_0}=\frac{4(0.25)}{0.4}=2.5,
$$

$$
L(b_Q)=\frac{4Ar_Q}{N_0}=\frac{4(-0.9)}{0.4}=-9.
$$

La rama I favorece fuertemente el bit asociado al semiplano positivo, mientras que la rama Q favorece de forma todavía más contundente el bit asociado al semiplano negativo. La decisión dura sería la misma que con un simple signo, pero el decodificador blando recibe además la confiabilidad relativa de ambas ramas.

**Ejemplo 3.21:** LLRs exactos en 16-QAM.

Considérese una 16-QAM con $d=1$, $N_0=1$ y observación sobre el eje I igual a $y=2.2$. Entonces

$$
L(b_{I,MSB})=
\ln\frac{e^{-(2.2-1)^2}+e^{-(2.2-3)^2}}{e^{-(2.2+1)^2}+e^{-(2.2+3)^2}}
\approx 9.97,
$$

$$
L(b_{I,LSB})=
\ln\frac{e^{-(2.2-3)^2}+e^{-(2.2+3)^2}}{e^{-(2.2-1)^2}+e^{-(2.2+1)^2}}
\approx 0.80.
$$

Interpretación:

- el bit de signo es **muy confiable** y favorece amplitud positiva,
- el bit de magnitud favorece ligeramente la región externa $+3d$ frente a la interna $+d$.

Este ejemplo ilustra una propiedad central de los LLRs: dentro del mismo símbolo, no todos los bits tienen la misma confiabilidad.

---

## Resumen de conceptos clave

1. **La representación pasabaja compleja** permite estudiar señales pasabanda mediante su envolvente $u(t)=I(t)+jQ(t)$.
2. **Las componentes I y Q** son proyecciones ortogonales de la señal sobre dos portadoras desfasadas $90^\circ$.
3. **ASK** modula amplitud; **FSK** modula frecuencia; **PSK** modula fase; **QAM** modula amplitud y fase simultáneamente.
4. **La cadena de transmisión real** incluye conformación de pulsos, interpolación, DAC, upconversion y amplificación; todos estos bloques afectan el desempeño final.
5. **La cadena de recepción real** incluye downconversion, filtro adaptado, sincronización de frecuencia, fase y tiempo, AGC, muestreo y decisión.
6. **BPSK y QPSK** ofrecen excelente robustez; **QAM** ofrece alta eficiencia espectral, pero exige mayor SNR y mejor linealidad.
7. **La conformación de pulsos** determina el espectro y controla la ISI; el coseno alzado y el RRC son centrales en sistemas prácticos.
8. **El filtro adaptado** maximiza la SNR a la salida del receptor y conduce a la detección óptima en AWGN.
9. **La demodulación coherente** supera a la no coherente, pero requiere sincronización precisa de portadora.
10. **CFO, offset de fase, error temporal, desbalance I/Q y desvanecimiento** deforman la constelación y deben mitigarse explícitamente.
11. **La BER** depende fuertemente de $E_b/N_0$ y de la **distancia mínima** de la constelación.
12. **Los LLRs** constituyen la salida natural del demapper moderno y permiten explotar toda la ganancia de la codificación de canal.

En síntesis, la modulación digital no es sólo una técnica de mapeo de bits: es un problema profundo de geometría, probabilidad, espectro, RF, sincronización y procesamiento estadístico. Comprender esta unidad es indispensable para abordar OFDM, ecualización adaptativa, MIMO, sincronización avanzada, turbo/LDPC y sistemas celulares contemporáneos.

---

## Referencias

1. Proakis, J. G., & Salehi, M. (2008). *Digital Communications* (5th ed.). McGraw-Hill.
2. Sklar, B. (2001). *Digital Communications: Fundamentals and Applications* (2nd ed.). Prentice Hall.
3. Goldsmith, A. (2005). *Wireless Communications*. Cambridge University Press. https://doi.org/10.1017/CBO9780511841224
4. Haykin, S. (2001). *Communication Systems* (4th ed.). John Wiley & Sons.
5. Simon, M. K., & Alouini, M.-S. (2005). *Digital Communication over Fading Channels* (2nd ed.). Wiley. https://doi.org/10.1002/0471749425
6. Barry, J. R., Lee, E. A., & Messerschmitt, D. G. (2004). *Digital Communication* (3rd ed.). Springer.
7. Meyr, H., Moeneclaey, M., & Fechtel, S. A. (1998). *Digital Communication Receivers: Synchronization, Channel Estimation, and Signal Processing*. Wiley.
8. Rice, M. (2008). *Digital Communications: A Discrete-Time Approach*. Pearson.
9. Nyquist, H. (1928). Certain topics in telegraph transmission theory. *Transactions of the American Institute of Electrical Engineers*, 47(2), 617-644. https://doi.org/10.1109/T-AIEE.1928.5055024
10. Viterbi, A. J. (1965). Error probability for differential detection of phase-shift keying modulated waves. *IEEE Transactions on Information Theory*, 11(4), 514-522. https://doi.org/10.1109/TIT.1965.1053801
11. Mueller, K. H., & Müller, M. (1976). Timing recovery in digital synchronous data receivers. *IEEE Transactions on Communications*, 24(5), 516-531. https://doi.org/10.1109/TCOM.1976.1093326
12. Mengali, U., & D'Andrea, A. N. (1997). *Synchronization Techniques for Digital Receivers*. Springer.
