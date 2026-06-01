# Unidad 1. Introducción a las comunicaciones digitales en banda base

## Introducción de la unidad

Las comunicaciones digitales en banda base constituyen el punto de partida para comprender los sistemas modernos de transmisión de información. Antes de estudiar modulación, codificación de canal, detección o sincronización, es imprescindible dominar el lenguaje matemático de las señales, los sistemas lineales e invariantes en el tiempo (LTI), los procesos aleatorios, el ruido y el concepto de ancho de banda. Esta unidad desarrolla estos fundamentos con un enfoque pedagógico, pero manteniendo el rigor matemático propio de la teoría de telecomunicaciones.

En banda base, la señal se transmite sin desplazar su espectro a una portadora senoidal de radiofrecuencia. Por ello, el análisis temporal y espectral de pulsos, secuencias digitales, ruido y filtros resulta central. A lo largo del capítulo se enfatiza la interpretación física de cada concepto, la relación entre formulaciones temporales y frecuenciales, y su utilidad directa en el diseño y análisis de enlaces digitales.

**Objetivos de la unidad:**

- Comprender la representación matemática de señales determinísticas y aleatorias.
- Dominar las herramientas fundamentales de análisis en tiempo y frecuencia.
- Interpretar la respuesta de sistemas LTI sobre señales útiles y ruido.
- Modelar el ruido blanco Gaussiano aditivo y cuantificar la relación señal-ruido.
- Relacionar el ancho de banda con la estructura espectral de las señales y con la tasa de datos.

[Figura 1.0]: Diagrama conceptual introductorio de la unidad. La figura debe mostrar, de izquierda a derecha, una fuente de información digital que genera bits, un bloque formador de pulsos en banda base, un canal con adición de ruido, un filtro receptor y un bloque de decisión. Debajo de cada bloque deben aparecer las herramientas matemáticas asociadas: “señales determinísticas”, “series/transformadas de Fourier”, “procesos aleatorios”, “sistemas LTI”, “AWGN”, “PSD” y “ancho de banda”. La intención es que el lector visualice desde el inicio cómo cada sección del capítulo se conecta con un sistema de comunicaciones digitales real.

---

## 1.1 Fundamentos de Señales Determinísticas y Sistemas Digitales

### 1.1.1 Caracterización y clasificación de señales determinísticas

Una **señal determinística** es aquella cuyo valor puede describirse exactamente mediante una expresión matemática o una regla conocida. Si conocemos la forma funcional de la señal, entonces podemos predecir su valor para cualquier instante de tiempo. Formalmente, una señal continua en el tiempo puede representarse como $x(t)$, mientras que una señal discreta en el tiempo se representa como $x[n]$.

En comunicaciones digitales de banda base es habitual trabajar con pulsos rectangulares, pulsos triangulares, secuencias binarias codificadas y respuestas impulsionales de filtros, todas las cuales pueden modelarse inicialmente como señales determinísticas.

#### Criterios de clasificación

**a) Según el dominio temporal**

- **Tiempo continuo:** $x(t)$ está definida para todo $t \in \mathbb{R}$.
- **Tiempo discreto:** $x[n]$ está definida solo para $n \in \mathbb{Z}$.

**b) Según la amplitud**

- **Amplitud continua:** puede tomar cualquier valor real en un intervalo.
- **Amplitud discreta:** toma valores de un conjunto discreto, por ejemplo $\{+A,-A\}$.

**c) Según periodicidad**

Una señal es **periódica** si existe un $T_0>0$ tal que

$$
 x(t+T_0)=x(t), \quad \forall t.
$$

El menor valor positivo que satisface esta condición se denomina **período fundamental**. Si no existe tal valor, la señal es **aperiódica**.

Para señales discretas, la periodicidad se define como

$$
 x[n+N_0]=x[n], \quad \forall n,
$$

donde $N_0$ es el período fundamental en muestras.

**d) Según energía y potencia**

Una señal de energía tiene energía finita:

$$
 E_x=\int_{-\infty}^{\infty} |x(t)|^2 \, dt < \infty.
$$

Una señal de potencia tiene potencia media finita y no nula:

$$
 P_x=\lim_{T\to\infty} \frac{1}{2T}\int_{-T}^{T}|x(t)|^2\,dt, \quad 0<P_x<\infty.
$$

En general, una señal no puede ser simultáneamente de energía finita no nula y de potencia finita no nula. Las señales periódicas no nulas suelen ser señales de potencia; los pulsos de duración finita suelen ser señales de energía.

**e) Según simetría**

- **Par:** $x(t)=x(-t)$.
- **Impar:** $x(t)=-x(-t)$.

Toda señal puede descomponerse como

$$
 x(t)=x_p(t)+x_i(t),
$$

con

$$
 x_p(t)=\frac{x(t)+x(-t)}{2}, \qquad x_i(t)=\frac{x(t)-x(-t)}{2}.
$$

**f) Según causalidad**

Una señal es causal si $x(t)=0$ para $t<0$. En modelado de sistemas físicos esta propiedad es particularmente útil.

**g) Según su naturaleza en comunicaciones digitales**

- Pulsos aislados.
- Trenes periódicos de pulsos.
- Señales binarias polarizadas: $\pm A$.
- Secuencias codificadas mediante retención rectangular de duración $T_b$.

[Figura 1.1]: Conjunto comparativo de señales determinísticas. La figura debe incluir, en paneles separados, una señal sinusoidal periódica, un pulso rectangular aislado, un tren periódico de pulsos y una señal binaria polar NRZ. En cada panel deben marcarse claramente amplitud, duración, período y ejes temporales. Debe apreciarse visualmente la diferencia entre señal de energía y señal de potencia, y entre señal periódica y aperiódica.

#### Concepto clave

**Una señal determinística queda completamente especificada por una ley matemática; su análisis puede realizarse tanto en el dominio del tiempo como en el de la frecuencia.**

### 1.1.2 Promedios temporales

El promedio temporal de una señal continua $x(t)$ en el intervalo $[-T,T]$ se define como

$$
 \overline{x}_T = \frac{1}{2T}\int_{-T}^{T} x(t)\,dt.
$$

Si existe el límite cuando $T\to\infty$, el promedio temporal es

$$
 \overline{x}=\lim_{T\to\infty}\frac{1}{2T}\int_{-T}^{T}x(t)\,dt.
$$

Para señales periódicas de período $T_0$, basta integrar sobre un período:

$$
 \overline{x}=\frac{1}{T_0}\int_{t_0}^{t_0+T_0}x(t)\,dt.
$$

De modo análogo, el promedio temporal cuadrático define la potencia media:

$$
 P_x=\overline{|x(t)|^2}=\lim_{T\to\infty}\frac{1}{2T}\int_{-T}^{T}|x(t)|^2dt.
$$

El valor eficaz o RMS es

$$
 x_{\mathrm{rms}}=\sqrt{P_x}.
$$

Estos promedios son fundamentales porque describen magnitudes medibles físicamente: componente continua, potencia entregada y amplitud eficaz.

#### Ejemplo 1.1: promedio temporal de una senoide

Considérese

$$
 x(t)=A\cos(2\pi f_0 t+\phi).
$$

**Solución:**

El promedio temporal sobre un período $T_0=1/f_0$ es

$$
 \overline{x}=\frac{1}{T_0}\int_0^{T_0}A\cos(2\pi f_0 t+\phi)dt.
$$

Integrando:

$$
 \overline{x}=\frac{A}{T_0}\left[\frac{1}{2\pi f_0}\sin(2\pi f_0 t+\phi)\right]_0^{T_0}=0.
$$

La potencia media es

$$
 P_x=\frac{1}{T_0}\int_0^{T_0}A^2\cos^2(2\pi f_0 t+\phi)dt.
$$

Usando $\cos^2(\theta)=\frac{1}{2}(1+\cos 2\theta)$,

$$
 P_x=\frac{A^2}{2}.
$$

Por tanto,

$$
 x_{\mathrm{rms}}=\frac{A}{\sqrt{2}}.
$$

**Interpretación:** la senoide tiene promedio nulo, pero potencia distinta de cero; por eso es una señal de potencia.

#### Ejemplo 1.2: energía de un pulso rectangular

Sea

$$
 x(t)=A\,\mathrm{rect}\left(\frac{t}{T}\right),
$$

donde

$$
 \mathrm{rect}\left(\frac{t}{T}\right)=
 \begin{cases}
 1, & |t|<\frac{T}{2},\\
 0, & |t|>\frac{T}{2}.
 \end{cases}
$$

**Solución:**

La energía es

$$
 E_x=\int_{-\infty}^{\infty}|x(t)|^2dt=\int_{-T/2}^{T/2}A^2dt=A^2T.
$$

La potencia media es

$$
 P_x=\lim_{L\to\infty}\frac{1}{2L}\int_{-L}^{L}|x(t)|^2dt=
 \lim_{L\to\infty}\frac{A^2T}{2L}=0.
$$

Luego es una señal de energía.

### 1.1.3 Descomposición en series de Fourier

Las señales periódicas pueden representarse como combinación de armónicos sinusoidales. Esta idea es extraordinariamente importante en telecomunicaciones, porque muestra que incluso un tren de pulsos digitales puede verse como suma de componentes en frecuencia.

Sea $x(t)$ periódica con período $T_0$ y frecuencia fundamental $f_0=1/T_0$, o frecuencia angular fundamental $\omega_0=2\pi/T_0$.

#### Forma trigonométrica

La serie de Fourier trigonométrica es

$$
 x(t)=a_0+\sum_{n=1}^{\infty}\left[a_n\cos(n\omega_0 t)+b_n\sin(n\omega_0 t)\right].
$$

Los coeficientes se obtienen mediante ortogonalidad:

$$
 a_0=\frac{1}{T_0}\int_{t_0}^{t_0+T_0}x(t)\,dt,
$$

$$
 a_n=\frac{2}{T_0}\int_{t_0}^{t_0+T_0}x(t)\cos(n\omega_0 t)\,dt,
$$

$$
 b_n=\frac{2}{T_0}\int_{t_0}^{t_0+T_0}x(t)\sin(n\omega_0 t)\,dt.
$$

La forma amplitud-fase equivalente es

$$
 x(t)=a_0+\sum_{n=1}^{\infty}C_n\cos(n\omega_0 t+\theta_n),
$$

con

$$
 C_n=\sqrt{a_n^2+b_n^2}, \qquad \theta_n=\tan^{-1}\left(-\frac{b_n}{a_n}\right).
$$

#### Forma exponencial compleja

Usando $e^{jn\omega_0 t}$, la serie toma la forma

$$
 x(t)=\sum_{n=-\infty}^{\infty} c_n e^{jn\omega_0 t},
$$

con coeficientes

$$
 c_n=\frac{1}{T_0}\int_{t_0}^{t_0+T_0}x(t)e^{-jn\omega_0 t}dt.
$$

Relación entre ambas formas:

$$
 c_0=a_0,
$$

$$
 c_n=\frac{1}{2}(a_n-jb_n), \quad n>0,
$$

$$
 c_{-n}=\frac{1}{2}(a_n+jb_n), \quad n>0.
$$

Si $x(t)$ es real, entonces

$$
 c_{-n}=c_n^*.
$$

#### Condiciones de Dirichlet

Una señal periódica admite serie de Fourier en sentido clásico si, en un período, satisface condiciones suficientes como:

- número finito de discontinuidades,
- número finito de máximos y mínimos,
- integrabilidad absoluta.

#### Parseval para series de Fourier

La potencia media de una señal periódica puede expresarse como

$$
 P_x=\frac{1}{T_0}\int_{t_0}^{t_0+T_0}|x(t)|^2dt=
 a_0^2+\frac{1}{2}\sum_{n=1}^{\infty}(a_n^2+b_n^2)
$$

O, en forma exponencial,

$$
 P_x=\sum_{n=-\infty}^{\infty}|c_n|^2.
$$

**Esta ecuación conecta el contenido temporal de potencia con la distribución armónica.**

[Figura 1.2]: Representación conceptual de la descomposición en serie de Fourier. La figura debe mostrar un tren periódico de pulsos rectangulares en el dominio del tiempo y, al lado, un espectro discreto de líneas en frecuencias $0$, $\pm f_0$, $\pm 2f_0$, etc. La altura de cada línea debe decrecer con la envolvente tipo sinc. La figura debe resaltar que una señal periódica posee un espectro discreto y que cada armónico contribuye a reconstruir la forma de onda original.

#### Ejemplo 1.3: serie de Fourier de una onda cuadrada bipolar

Sea la señal periódica de período $T_0$:

$$
 x(t)=
 \begin{cases}
 A, & 0<t<\frac{T_0}{2},\\
 -A, & \frac{T_0}{2}<t<T_0,
 \end{cases}
$$

extendida periódicamente.

**Solución:**

Como la señal tiene simetría impar alrededor de su centro adecuado, su promedio es cero y $a_n=0$. Calculamos $b_n$:

$$
 b_n=\frac{2}{T_0}\int_0^{T_0}x(t)\sin(n\omega_0 t)dt.
$$

Separando intervalos:

$$
 b_n=\frac{2}{T_0}\left[\int_0^{T_0/2}A\sin(n\omega_0 t)dt+\int_{T_0/2}^{T_0}(-A)\sin(n\omega_0 t)dt\right].
$$

Tras integrar y simplificar,

$$
 b_n=
 \begin{cases}
 \dfrac{4A}{n\pi}, & n \text{ impar},\\
 0, & n \text{ par}.
 \end{cases}
$$

Por tanto,

$$
 x(t)=\frac{4A}{\pi}\left(\sin\omega_0 t+\frac{1}{3}\sin 3\omega_0 t+\frac{1}{5}\sin 5\omega_0 t+\cdots\right).
$$

**Interpretación física:** una onda cuadrada requiere infinitos armónicos impares para ser reconstruida exactamente. Los armónicos altos son responsables de los bordes abruptos.

#### Ejemplo 1.4: tren periódico de pulsos rectangulares

Sea un tren periódico de amplitud $A$, ancho $\tau$ y período $T_0$:

$$
 x(t)=A, \quad |t|<\frac{\tau}{2}
$$

en cada período, y cero fuera de ese intervalo dentro del período.

**Solución en forma exponencial:**

$$
 c_n=\frac{1}{T_0}\int_{-\tau/2}^{\tau/2} A e^{-jn\omega_0 t}dt.
$$

Entonces,

$$
 c_n=\frac{A}{T_0}\left[\frac{e^{-jn\omega_0 t}}{-jn\omega_0}\right]_{-\tau/2}^{\tau/2}
 =\frac{A}{T_0}\frac{2\sin(n\omega_0\tau/2)}{n\omega_0}.
$$

Como $\omega_0=2\pi/T_0$,

$$
 c_n=A\frac{\tau}{T_0}\,\mathrm{sinc}\left(n\frac{\tau}{T_0}\right),
$$

si se usa la convención normalizada $\mathrm{sinc}(x)=\frac{\sin(\pi x)}{\pi x}$.

Además,

$$
 c_0=A\frac{\tau}{T_0}.
$$

**Conclusión:** el espectro discreto queda modulado por una envolvente sinc, lo que anticipa la relación entre pulsos rectangulares y ancho de banda elevado.

### 1.1.4 Transformada de Fourier

Mientras la serie de Fourier representa señales periódicas mediante espectros discretos, la **transformada de Fourier (TF)** representa señales aperiódicas mediante espectros continuos.

#### Definición

Para una señal $x(t)$ integrable, su transformada de Fourier se define como

$$
 X(f)=\int_{-\infty}^{\infty}x(t)e^{-j2\pi f t}dt.
$$

La transformada inversa es

$$
 x(t)=\int_{-\infty}^{\infty}X(f)e^{j2\pi f t}df.
$$

También puede usarse la variable angular $\omega=2\pi f$:

$$
 X(\omega)=\int_{-\infty}^{\infty}x(t)e^{-j\omega t}dt,
$$

$$
 x(t)=\frac{1}{2\pi}\int_{-\infty}^{\infty}X(\omega)e^{j\omega t}d\omega.
$$

#### Interpretación

$X(f)$ indica cuánto de cada componente senoidal compleja de frecuencia $f$ está presente en $x(t)$. En comunicaciones, esto permite estudiar ocupación espectral, filtrado, interferencia y diseño de receptores.

#### Propiedades principales

1. **Linealidad**

$$
 a x_1(t)+b x_2(t) \leftrightarrow aX_1(f)+bX_2(f).
$$

2. **Desplazamiento temporal**

$$
 x(t-t_0) \leftrightarrow X(f)e^{-j2\pi f t_0}.
$$

3. **Desplazamiento en frecuencia**

$$
 x(t)e^{j2\pi f_0 t} \leftrightarrow X(f-f_0).
$$

4. **Escalamiento temporal**

$$
 x(at) \leftrightarrow \frac{1}{|a|}X\left(\frac{f}{a}\right), \quad a\neq 0.
$$

5. **Convolución en tiempo**

$$
 x(t)*h(t) \leftrightarrow X(f)H(f).
$$

6. **Multiplicación en tiempo**

$$
 x(t)h(t) \leftrightarrow X(f)*H(f).
$$

7. **Derivación temporal**

$$
 \frac{d}{dt}x(t) \leftrightarrow j2\pi f X(f).
$$

8. **Parseval**

$$
 \int_{-\infty}^{\infty}|x(t)|^2dt=\int_{-\infty}^{\infty}|X(f)|^2df.
$$

9. **Simetría para señales reales**

Si $x(t)$ es real,

$$
 X(-f)=X^*(f).
$$

Entonces $|X(f)|$ es par y la fase es impar.

#### Pares de transformadas importantes

1. **Delta de Dirac**

$$
 \delta(t) \leftrightarrow 1.
$$

2. **Exponencial compleja**

$$
 e^{j2\pi f_0 t} \leftrightarrow \delta(f-f_0).
$$

3. **Pulso rectangular**

$$
 \mathrm{rect}\left(\frac{t}{T}\right) \leftrightarrow T\,\mathrm{sinc}(fT).
$$

4. **Función sinc**

$$
 \mathrm{sinc}\left(\frac{t}{T}\right) \leftrightarrow T\,\mathrm{rect}(fT).
$$

5. **Gaussiana**

Si

$$
 x(t)=e^{-\pi t^2/a}, \quad a>0,
$$

entonces

$$
 X(f)=\sqrt{a}\,e^{-\pi a f^2}.
$$

6. **Pulso triangular**

$$
 \Lambda\left(\frac{t}{T}\right) \leftrightarrow T\,\mathrm{sinc}^2(fT),
$$

donde $\Lambda(\cdot)$ es la función triangular.

[Figura 1.3]: Correspondencia tiempo-frecuencia de pulsos básicos. La figura debe disponer tres filas: pulso rectangular con espectro sinc, pulso triangular con espectro sinc cuadrado y pulso gaussiano con espectro gaussiano. Cada fila debe mostrar claramente que señales más localizadas en el tiempo tienden a ocupar más ancho espectral, mientras que señales suaves temporalmente generan espectros con mejor confinamiento y menos lóbulos laterales.

#### Ejemplo 1.5: transformada de Fourier de un pulso rectangular

Sea

$$
 x(t)=A\,\mathrm{rect}\left(\frac{t}{T}\right).
$$

**Solución:**

Por definición,

$$
 X(f)=\int_{-T/2}^{T/2}A e^{-j2\pi ft}dt.
$$

Integrando,

$$
 X(f)=A\left[\frac{e^{-j2\pi ft}}{-j2\pi f}\right]_{-T/2}^{T/2}
 =A\frac{e^{-j\pi fT}-e^{j\pi fT}}{-j2\pi f}.
$$

Usando $e^{-j\theta}-e^{j\theta}=-2j\sin\theta$,

$$
 X(f)=AT\,\frac{\sin(\pi fT)}{\pi fT}=AT\,\mathrm{sinc}(fT).
$$

**Observación:** los ceros espectrales aparecen en $f=\pm 1/T, \pm 2/T, \ldots$.

#### Ejemplo 1.6: efecto de un retardo temporal

Si $x(t) \leftrightarrow X(f)$, hallar la transformada de $x(t-t_0)$.

**Solución:**

Aplicando la propiedad de desplazamiento temporal:

$$
 x(t-t_0) \leftrightarrow X(f)e^{-j2\pi f t_0}.
$$

**Interpretación:** el retardo no modifica la magnitud espectral; únicamente añade una fase lineal con la frecuencia.

### 1.1.5 Función de densidad espectral de potencia

La **densidad espectral de potencia (PSD, Power Spectral Density)** describe cómo se distribuye la potencia de una señal o proceso a través de la frecuencia. En señales de potencia, el cuadrado de la transformada convencional no es directamente suficiente, porque la energía total es infinita. Por ello se define a partir de un truncamiento temporal.

Sea $x(t)$ una señal de potencia y defínase la versión truncada en $[-T,T]$:

$$
 x_T(t)=
 \begin{cases}
 x(t), & |t|\le T,\\
 0, & |t|>T.
 \end{cases}
$$

Entonces, la PSD se define como

$$
 S_x(f)=\lim_{T\to\infty}\frac{1}{2T}|X_T(f)|^2,
$$

donde $X_T(f)$ es la transformada de $x_T(t)$.

Para procesos estacionarios se suele definir mediante transformada de la autocorrelación, como se formalizará en la Sección 1.2.

#### Propiedades

1. **No negatividad**

$$
 S_x(f)\ge 0.
$$

2. **Señales reales**

$$
 S_x(-f)=S_x(f).
$$

3. **Potencia total**

$$
 P_x=\int_{-\infty}^{\infty}S_x(f)df.
$$

4. **Relación con autocorrelación**

$$
 S_x(f)=\mathcal{F}\{R_x(\tau)\},
$$

siendo $R_x(\tau)$ la autocorrelación adecuada de la señal o proceso.

5. **Salida de un sistema LTI**

Si $y(t)=x(t)*h(t)$, entonces

$$
 S_y(f)=|H(f)|^2S_x(f).
$$

Esta propiedad es esencial en comunicaciones: el canal y los filtros moldean el espectro de potencia multiplicándolo por la ganancia en potencia del sistema.

[Figura 1.4]: Interpretación de la densidad espectral de potencia. La figura debe mostrar, en la parte superior, una señal temporal larga con apariencia periódica o pseudoaleatoria; en la parte inferior, una curva de PSD donde el eje horizontal es frecuencia y el eje vertical es potencia por hercio. Debe destacarse visualmente que el área bajo la curva corresponde a la potencia media total. En una anotación lateral puede indicarse cómo un filtro pasabajos recorta la PSD y reduce la potencia fuera de banda.

#### Ejemplo 1.7: PSD de una senoide periódica

Sea

$$
 x(t)=A\cos(2\pi f_0 t).
$$

**Solución conceptual:** al ser una señal periódica de potencia, su espectro está concentrado en líneas discretas. Puede escribirse como

$$
 x(t)=\frac{A}{2}e^{j2\pi f_0 t}+\frac{A}{2}e^{-j2\pi f_0 t}.
$$

La PSD está formada por deltas en $\pm f_0$:

$$
 S_x(f)=\frac{A^2}{4}\delta(f-f_0)+\frac{A^2}{4}\delta(f+f_0).
$$

Verificación de potencia:

$$
 \int_{-\infty}^{\infty}S_x(f)df=\frac{A^2}{2}=P_x.
$$

#### Ejemplo 1.8: PSD de un tren de pulsos rectangular

Un tren periódico de pulsos posee espectro discreto con coeficientes $c_n$. Por Parseval espectral,

$$
 S_x(f)=\sum_{n=-\infty}^{\infty}|c_n|^2\delta(f-nf_0).
$$

Si $c_n=A\frac{\tau}{T_0}\mathrm{sinc}\left(n\frac{\tau}{T_0}\right)$, entonces

$$
 S_x(f)=\sum_{n=-\infty}^{\infty}A^2\left(\frac{\tau}{T_0}\right)^2
 \mathrm{sinc}^2\left(n\frac{\tau}{T_0}\right)\delta(f-nf_0).
$$

**Interpretación:** la distribución de potencia entre armónicos queda modulada por una envolvente $\mathrm{sinc}^2$.

### 1.1.6 Cierre conceptual de la sección

En señales determinísticas, la idea central es que una forma de onda puede describirse exactamente, promediarse temporalmente, descomponerse en armónicos si es periódica y analizarse mediante espectro continuo si es aperiódica. Estas herramientas constituyen el lenguaje base del análisis de pulsos digitales y del diseño espectral en banda base.

---

## 1.2 Análisis de Señales Aleatorias

En sistemas reales, las señales recibidas no son perfectamente determinísticas. El ruido, las interferencias, las fluctuaciones de canal y hasta la propia fuente de datos pueden requerir una descripción probabilística. Por ello se introducen los **procesos estocásticos** o aleatorios.

### 1.2.1 Procesos estocásticos: definición formal y clasificación

Un **proceso estocástico** es una familia de variables aleatorias indexadas por el tiempo:

$$
 \{X(t,\zeta),\; t\in T,\; \zeta\in\Omega\},
 $$

donde $\Omega$ es el espacio muestral del experimento aleatorio. Para un $t$ fijo, $X(t,\zeta)$ es una variable aleatoria. Para una realización fija $\zeta=\zeta_0$, la función resultante $x(t)=X(t,\zeta_0)$ se denomina **trayectoria** o **realización**.

#### Clasificación básica

- **Tiempo continuo / discreto**.
- **Amplitud continua / discreta**.
- **Estacionario / no estacionario**.
- **Gaussiano / no Gaussiano**.
- **Markoviano / no Markoviano**.
- **Ergódico / no ergódico**.

En comunicaciones digitales son frecuentes:

- ruido blanco Gaussiano,
- secuencias binarias aleatorias independientes,
- procesos coloreados a la salida de filtros,
- procesos estacionarios de interferencia.

[Figura 1.5]: Visualización de un proceso estocástico mediante múltiples realizaciones. La figura debe mostrar varias trayectorias posibles de un mismo proceso sobre el mismo sistema de ejes tiempo-amplitud. En un instante fijo $t_1$ debe dibujarse una línea vertical destacando que los valores de distintas trayectorias forman una variable aleatoria. Esta figura debe ayudar a distinguir claramente entre “proceso”, “realización” y “variable aleatoria en un instante”.

### 1.2.2 Promedios muestrales: media, varianza y momentos

Para un proceso $X(t)$, la **media de conjunto** o valor esperado es

$$
 m_X(t)=\mathbb{E}[X(t)].
$$

El segundo momento es

$$
 \mathbb{E}[X^2(t)].
$$

La varianza es

$$
 \sigma_X^2(t)=\mathbb{E}\left[(X(t)-m_X(t))^2\right]=\mathbb{E}[X^2(t)]-m_X^2(t).
$$

Más generalmente, el momento de orden $n$ es

$$
 m_n(t)=\mathbb{E}[X^n(t)].
$$

En la práctica, a partir de una realización finita o de datos muestreados, se calculan **promedios muestrales**. Si disponemos de $N$ muestras $x_1,x_2,\ldots,x_N$, entonces:

- Media muestral:

$$
 \hat{\mu} = \frac{1}{N}\sum_{k=1}^{N}x_k.
$$

- Varianza muestral (versión insesgada):

$$
 \hat{\sigma}^2 = \frac{1}{N-1}\sum_{k=1}^{N}(x_k-\hat{\mu})^2.
$$

- Momento muestral de orden $n$:

$$
 \hat{m}_n=\frac{1}{N}\sum_{k=1}^{N}x_k^n.
$$

En telecomunicaciones, estos estimadores se usan para caracterizar ruido medido, interferencia y niveles de señal.

#### Ejemplo 1.9: media y varianza muestrales

Supóngase que se miden cinco muestras de ruido: $\{-1, 0, 2, 1, -2\}$.

**Solución:**

La media muestral es

$$
 \hat{\mu}=\frac{-1+0+2+1-2}{5}=0.
$$

La varianza muestral es

$$
 \hat{\sigma}^2=\frac{1}{4}\left[(-1)^2+0^2+2^2+1^2+(-2)^2\right]=\frac{10}{4}=2.5.
$$

El segundo momento muestral es

$$
 \hat{m}_2=\frac{10}{5}=2.
$$

Nótese que $\hat{m}_2 \neq \hat{\sigma}^2$ porque la varianza insesgada usa $N-1$ en el denominador.

### 1.2.3 Funciones de autocorrelación y correlación cruzada

La **autocorrelación** de un proceso $X(t)$ se define como

$$
 R_X(t_1,t_2)=\mathbb{E}[X(t_1)X^*(t_2)].
$$

Si el proceso es real, el conjugado puede omitirse. La autocovarianza es

$$
 C_X(t_1,t_2)=\mathbb{E}[(X(t_1)-m_X(t_1))(X(t_2)-m_X(t_2))].
$$

La **correlación cruzada** entre dos procesos $X(t)$ y $Y(t)$ es

$$
 R_{XY}(t_1,t_2)=\mathbb{E}[X(t_1)Y^*(t_2)].
$$

#### Interpretación física

- Si $R_X(t_1,t_2)$ es grande, los valores del proceso en los instantes $t_1$ y $t_2$ tienden a parecerse estadísticamente.
- Si decrece rápidamente con $|t_1-t_2|$, el proceso “pierde memoria” rápidamente.
- La correlación cruzada permite detectar dependencia entre señal útil y ruido, o entre entrada y salida de un sistema.

Para procesos estacionarios en sentido amplio,

$$
 R_X(t_1,t_2)=R_X(\tau), \quad \tau=t_1-t_2.
$$

Entonces,

$$
 R_X(0)=\mathbb{E}[|X(t)|^2],
$$

es decir, el valor en cero es la potencia media si la media es nula.

#### Propiedades importantes

1. **Hermiticidad**

$$
 R_X(t_1,t_2)=R_X^*(t_2,t_1).
$$

2. **Máximo en el origen** para procesos WSS reales adecuados:

$$
 |R_X(\tau)|\le R_X(0).
$$

3. **Para media nula y WSS**,

$$
 C_X(\tau)=R_X(\tau).
$$

#### Ejemplo 1.10: autocorrelación de una senoide con fase aleatoria

Sea

$$
 X(t)=A\cos(2\pi f_0 t+\Theta),
$$

donde $\Theta$ es uniforme en $[0,2\pi)$.

**Media:**

$$
 m_X(t)=\mathbb{E}[A\cos(2\pi f_0 t+\Theta)]=0.
$$

**Autocorrelación:**

$$
 R_X(t_1,t_2)=A^2\mathbb{E}[\cos(2\pi f_0 t_1+\Theta)\cos(2\pi f_0 t_2+\Theta)].
$$

Usando la identidad

$$
 \cos\alpha\cos\beta=\frac{1}{2}[\cos(\alpha-\beta)+\cos(\alpha+\beta)],
$$

queda

$$
 R_X(t_1,t_2)=\frac{A^2}{2}\cos(2\pi f_0(t_1-t_2))+rac{A^2}{2}\mathbb{E}[\cos(2\pi f_0(t_1+t_2)+2\Theta)].
$$

El segundo término es cero por uniformidad de $\Theta$, por tanto

$$
 R_X(\tau)=\frac{A^2}{2}\cos(2\pi f_0\tau).
$$

**Conclusión:** el proceso es WSS.

### 1.2.4 Estacionariedad: sentido amplio y sentido estricto

La estacionariedad indica invariancia estadística frente a desplazamientos temporales.

#### Estacionariedad en sentido estricto (SSS)

Un proceso es estrictamente estacionario si todas sus distribuciones conjuntas son invariantes ante desplazamientos temporales. Es decir, para cualquier conjunto de tiempos $t_1,\ldots,t_n$ y cualquier $\Delta$,

$$
 F_{X(t_1),\ldots,X(t_n)}(x_1,\ldots,x_n)=F_{X(t_1+\Delta),\ldots,X(t_n+\Delta)}(x_1,\ldots,x_n).
$$

Es una condición fuerte porque exige invariancia de toda la estructura probabilística.

#### Estacionariedad en sentido amplio (WSS)

Un proceso es estacionario en sentido amplio si:

1. La media es constante:

$$
 m_X(t)=m_X.
$$

2. La autocorrelación depende solo del retardo:

$$
 R_X(t_1,t_2)=R_X(t_1-t_2)=R_X(\tau).
$$

Para procesos Gaussianos, WSS más media constante suele ser muy poderosa, porque los momentos de segundo orden determinan completamente la estadística.

#### Importancia práctica

La mayoría del análisis de ruido y filtrado lineal en comunicaciones se formula bajo hipótesis WSS, porque permite utilizar PSD y el teorema de Wiener-Khintchine.

[Figura 1.6]: Comparación entre proceso estacionario y no estacionario. La figura debe tener dos paneles. En el primero, múltiples realizaciones con media y dispersión aproximadamente constantes a lo largo del tiempo. En el segundo, realizaciones cuyo valor medio o varianza crecen con el tiempo. Deben incluirse anotaciones explicando que en el caso estacionario la estadística no cambia al desplazar la observación temporal, mientras que en el no estacionario sí lo hace.

#### Ejemplo 1.11: proceso no estacionario

Sea

$$
 X(t)=At,
$$

donde $A$ es una variable aleatoria con media cero y varianza $\sigma_A^2$.

Entonces,

$$
 m_X(t)=\mathbb{E}[A]t=0,
$$

pero

$$
 R_X(t_1,t_2)=\mathbb{E}[A^2]t_1t_2=\sigma_A^2 t_1 t_2.
$$

Esta autocorrelación depende de $t_1$ y $t_2$ por separado, no solo de la diferencia, por lo que el proceso **no es WSS**.

### 1.2.5 Ergodicidad: definición, condiciones e importancia práctica

La **ergodicidad** conecta promedios temporales con promedios de conjunto. Un proceso puede ser estacionario pero no ergódico. En ingeniería, la ergodicidad es crucial porque normalmente disponemos de una sola realización temporal larga del proceso, no de infinitas realizaciones paralelas.

#### Definición intuitiva

Un proceso es ergódico en media si, para casi toda realización,

$$
 \lim_{T\to\infty}\frac{1}{2T}\int_{-T}^{T}x(t)dt=\mathbb{E}[X(t)].
$$

Es ergódico en autocorrelación si

$$
 \lim_{T\to\infty}\frac{1}{2T}\int_{-T}^{T}x(t)x(t+\tau)dt=R_X(\tau).
$$

Si ambas condiciones se cumplen, las propiedades estadísticas pueden estimarse mediante promedios temporales sobre una sola trayectoria suficientemente larga.

#### Importancia práctica

- Permite estimar media, varianza y PSD a partir de medidas reales.
- Justifica el uso de periodogramas y estimadores espectrales sobre datos temporales.
- Conecta la teoría probabilística con la instrumentación experimental.

#### Comentario técnico

La ergodicidad suele requerir, además de estacionariedad, cierta pérdida de memoria o mezcla estadística suficientemente fuerte. No toda señal WSS es ergódica.

#### Ejemplo 1.12: proceso estacionario no ergódico

Considérese

$$
 X(t)=A,
$$

donde $A$ es una variable aleatoria que vale $+1$ o $-1$ con igual probabilidad, constante para todo tiempo en cada realización.

**Media de conjunto:**

$$
 \mathbb{E}[X(t)]=0.
$$

**Promedio temporal de una realización:**

Si la realización corresponde a $A=+1$, entonces

$$
 \frac{1}{2T}\int_{-T}^{T}x(t)dt=1.
$$

Si corresponde a $A=-1$, el promedio es $-1$.

Por lo tanto, el promedio temporal no coincide con la media de conjunto. El proceso es estacionario, pero **no ergódico en media**.

### 1.2.6 Densidad espectral de potencia de procesos estacionarios: teorema de Wiener-Khintchine

Para un proceso WSS, la PSD y la autocorrelación forman un par de transformadas de Fourier:

$$
 S_X(f)=\int_{-\infty}^{\infty}R_X(\tau)e^{-j2\pi f\tau}d\tau,
$$

$$
 R_X(\tau)=\int_{-\infty}^{\infty}S_X(f)e^{j2\pi f\tau}df.
$$

Esto es el **teorema de Wiener-Khintchine**.

#### Consecuencias fundamentales

1. La PSD es la transformada de la autocorrelación.
2. El valor medio cuadrático del proceso viene dado por

$$
 R_X(0)=\int_{-\infty}^{\infty}S_X(f)df.
$$

3. Si la media es cero, $R_X(0)=\sigma_X^2$.
4. Filtrar un proceso WSS modifica la PSD por el factor $|H(f)|^2$.

#### Ejemplo 1.13: PSD a partir de autocorrelación exponencial

Sea un proceso WSS de media cero con

$$
 R_X(\tau)=\sigma^2 e^{-a|\tau|}, \quad a>0.
$$

**Solución:**

Aplicando Fourier,

$$
 S_X(f)=\int_{-\infty}^{\infty}\sigma^2 e^{-a|\tau|}e^{-j2\pi f\tau}d\tau.
$$

Por simetría,

$$
 S_X(f)=2\sigma^2\int_{0}^{\infty}e^{-a\tau}\cos(2\pi f\tau)d\tau.
$$

Usando la integral conocida

$$
 \int_0^{\infty}e^{-a\tau}\cos(b\tau)d\tau=\frac{a}{a^2+b^2},
$$

se obtiene

$$
 S_X(f)=\frac{2a\sigma^2}{a^2+(2\pi f)^2}.
$$

**Interpretación:** es un espectro tipo Lorentziano, típico de procesos con memoria exponencial.

[Figura 1.7]: Relación entre autocorrelación y PSD según Wiener-Khintchine. La figura debe mostrar en el panel izquierdo una autocorrelación exponencial decreciente simétrica respecto a $\tau=0$, y en el panel derecho la PSD correspondiente de forma campaniforme centrada en frecuencia cero. Debe incluirse una flecha entre ambas con la leyenda “Transformada de Fourier”. La figura debe enfatizar que correlaciones temporales largas producen espectros más angostos, mientras que correlaciones muy cortas producen espectros más anchos.

### 1.2.7 Periodograma de Welch

La PSD teórica rara vez es conocida exactamente; por ello se utilizan estimadores a partir de datos observados. Uno de los más usados es el **periodograma de Welch**, por su robustez y reducción de varianza.

#### Periodograma clásico

Dada una secuencia finita $x[n]$, $n=0,1,\ldots,N-1$, el periodograma clásico es

$$
 \hat{S}_{xx}^{(P)}(f)=\frac{1}{N F_s}\left|\sum_{n=0}^{N-1}x[n]e^{-j2\pi fn/F_s}\right|^2,
$$

donde $F_s$ es la frecuencia de muestreo.

Aunque sencillo, presenta alta varianza y fuerte fuga espectral si no se aplican ventanas adecuadas.

#### Idea de Welch

Welch propuso:

1. Dividir la secuencia en varios segmentos, usualmente solapados.
2. Multiplicar cada segmento por una ventana (Hamming, Hann, etc.).
3. Calcular el periodograma de cada segmento.
4. Promediar los periodogramas.

Esto reduce la varianza del estimador, aunque a costa de menor resolución espectral.

#### Formulación

Sea la señal segmentada en $K$ bloques de longitud $L$, con solapamiento. Para el bloque $k$, la secuencia ventaneada es $x_k[n]w[n]$, $0\le n\le L-1$.

El periodograma del bloque $k$ es

$$
 P_k(f)=\frac{1}{L U F_s}\left|\sum_{n=0}^{L-1}x_k[n]w[n]e^{-j2\pi fn/F_s}\right|^2,
$$

donde

$$
 U=\frac{1}{L}\sum_{n=0}^{L-1}w^2[n]
$$

normaliza la potencia de la ventana.

El estimador de Welch es

$$
 \hat{S}_{xx}^{(W)}(f)=\frac{1}{K}\sum_{k=1}^{K}P_k(f).
$$

#### Ventajas sobre el periodograma clásico

- Menor varianza del estimador.
- Menor sensibilidad a fluctuaciones aleatorias.
- Mejor comportamiento práctico en presencia de ruido.
- Posibilidad de controlar el compromiso resolución-varianza mediante longitud de ventana, tipo de ventana y solapamiento.

#### Limitaciones

- Menor resolución frecuencial al usar segmentos más cortos.
- El suavizado puede ocultar líneas espectrales muy cercanas.

#### Algoritmo resumido

1. Seleccionar $L$, ventana y solapamiento.
2. Extraer segmentos.
3. Ventanear cada segmento.
4. Calcular FFT de cada segmento.
5. Elevar módulo al cuadrado y normalizar.
6. Promediar todos los periodogramas parciales.

[Figura 1.8]: Procedimiento del método de Welch. La figura debe mostrar una secuencia temporal larga dividida en segmentos solapados, cada uno multiplicado por una ventana suave. Luego deben aparecer pequeñas FFT de cada segmento y finalmente un bloque de promedio que produce una PSD estimada más suave. Deben indicarse con flechas las etapas “segmentación”, “ventaneo”, “FFT”, “potencia” y “promedio”.

#### Ejemplo 1.14: interpretación del método de Welch

Supóngase una secuencia de $N=4096$ muestras de una señal ruidosa. Si se usa un periodograma clásico, la estimación fluctúa mucho. Si se divide en $K=8$ segmentos de longitud $L=1024$ con 50% de solapamiento y ventana de Hann, el promedio de periodogramas reduce notablemente la varianza.

**Comentario pedagógico:** aunque no se realiza aquí una FFT numérica, conceptualmente el método de Welch reemplaza una estimación muy “rugosa” por otra más “estable”, lo cual es especialmente útil para medir el ruido de un receptor o caracterizar una señal digital en banda base.

### 1.2.8 Ejemplo integrador de la sección

#### Ejemplo 1.15: secuencia binaria aleatoria polar

Considérese una secuencia discreta $a_k\in\{+A,-A\}$ equiprobable e independiente.

**Media:**

$$
 \mathbb{E}[a_k]=A\cdot\frac{1}{2}+(-A)\cdot\frac{1}{2}=0.
$$

**Varianza:**

$$
 \sigma_a^2=\mathbb{E}[a_k^2]-\mathbb{E}[a_k]^2=A^2.
$$

**Autocorrelación discreta:**

$$
 R_a[m]=\mathbb{E}[a_k a_{k+m}].
$$

Por independencia,

$$
 R_a[m]=
 \begin{cases}
 A^2, & m=0,\\
 0, & m\neq 0.
 \end{cases}
$$

**Interpretación:** la secuencia es blanca en tiempo discreto, ya que no presenta correlación entre símbolos distintos. Este resultado será decisivo al estudiar conformación de pulsos y PSD de señales digitales.

---

## 1.3 Respuesta de Sistemas Lineales e Invariantes en el Tiempo (LTI)

Los sistemas LTI constituyen la clase más importante de sistemas en telecomunicaciones porque describen filtros, canales idealizados, circuitos lineales y etapas de recepción. Su relevancia se debe a que admiten una caracterización completa mediante respuesta al impulso o función de transferencia.

### 1.3.1 Análisis en el dominio de la frecuencia

Sea un sistema LTI con respuesta al impulso $h(t)$. Su **función de transferencia** o respuesta en frecuencia es

$$
 H(f)=\int_{-\infty}^{\infty}h(t)e^{-j2\pi ft}dt.
$$

Si la entrada es una exponencial compleja

$$
 x(t)=e^{j2\pi f t},
$$

la salida es

$$
 y(t)=H(f)e^{j2\pi f t}.
$$

Es decir, las exponenciales complejas son funciones propias de los sistemas LTI. El sistema solo modifica su amplitud y fase.

#### Interpretación de $H(f)$

- $|H(f)|$: ganancia en amplitud para la frecuencia $f$.
- $\angle H(f)$: desplazamiento de fase introducido por el sistema.

#### Tipos de filtros ideales

- **Pasabajos ideal:**

$$
 H(f)=
 \begin{cases}
 1, & |f|\le B,\\
 0, & |f|>B.
 \end{cases}
$$

- **Pasaaltos ideal**.
- **Pasabanda ideal**.
- **Rechazabanda ideal**.

En banda base, el pasabajos es especialmente importante porque las señales útiles suelen concentrarse alrededor de $f=0$.

[Figura 1.9]: Respuesta en frecuencia de filtros LTI básicos. La figura debe mostrar cuatro subgráficas con magnitud de $H(f)$ frente a frecuencia: pasabajos, pasaaltos, pasabanda y rechazabanda. Deben destacarse bandas de paso, bandas de rechazo y frecuencias de corte. La finalidad es que el lector asocie intuitivamente la forma de $H(f)$ con el efecto espectral sobre una señal de entrada.

#### Ejemplo 1.16: salida de un sistema pasabajos ideal ante una senoide

Si

$$
 x(t)=A\cos(2\pi f_0 t),
$$

y el sistema es pasabajos ideal con ancho $B$.

**Solución:**

La senoide tiene componentes espectrales en $\pm f_0$. Si $|f_0|<B$, ambas componentes atraviesan el filtro y la salida es la misma senoide (posiblemente escalada). Si $|f_0|>B$, la salida es nula.

En forma compacta, si $H(f_0)=1$,

$$
 y(t)=A\cos(2\pi f_0 t).
$$

Si $H(f_0)=0$,

$$
 y(t)=0.
$$

### 1.3.2 Análisis en el dominio del tiempo: respuesta al impulso y convolución

La salida de un sistema LTI ante una entrada arbitraria $x(t)$ se obtiene por convolución:

$$
 y(t)=x(t)*h(t)=\int_{-\infty}^{\infty}x(\lambda)h(t-\lambda)d\lambda.
$$

En tiempo discreto,

$$
 y[n]=\sum_{k=-\infty}^{\infty}x[k]h[n-k].
$$

#### Justificación conceptual

Una señal puede verse como suma continua de impulsos desplazados y ponderados:

$$
 x(t)=\int_{-\infty}^{\infty}x(\lambda)\delta(t-\lambda)d\lambda.
$$

Por linealidad e invariancia temporal, la respuesta a cada impulso es $h(t-\lambda)$; sumando todas las contribuciones se obtiene la convolución.

#### Propiedades de la convolución

1. Conmutativa:

$$
 x*h=h*x.
$$

2. Asociativa:

$$
 x*(h_1*h_2)=(x*h_1)*h_2.
$$

3. Distributiva:

$$
 x*(h_1+h_2)=x*h_1+x*h_2.
$$

4. En frecuencia:

$$
 Y(f)=X(f)H(f).
$$

#### Causalidad y estabilidad

- El sistema es causal si $h(t)=0$ para $t<0$.
- El sistema es BIBO estable si

$$
 \int_{-\infty}^{\infty}|h(t)|dt<\infty.
$$

Estas condiciones son importantes en filtros realizables físicamente.

[Figura 1.10]: Ilustración gráfica de la convolución. La figura debe mostrar cuatro etapas: (1) señal de entrada $x(\lambda)$, (2) respuesta al impulso invertida temporalmente $h(-\lambda)$, (3) respuesta desplazada $h(t-\lambda)$ para un valor particular de $t$, y (4) producto punto a punto seguido de integración del área solapada para obtener $y(t)$. La secuencia de paneles debe ayudar a comprender geométricamente cómo se construye la convolución.

#### Ejemplo 1.17: convolución de un pulso con un filtro integrador finito

Sea

$$
 x(t)=u(t)-u(t-T),
$$

un pulso rectangular unitario, y

$$
 h(t)=u(t)-u(t-T),
$$

el mismo pulso usado como respuesta al impulso.

**Solución:**

La convolución de dos rectángulos de duración $T$ produce un triángulo:

$$
 y(t)=x(t)*h(t)=
 \begin{cases}
 0, & t<0,\\
 t, & 0\le t<T,\\
 2T-t, & T\le t<2T,\\
 0, & t\ge 2T.
 \end{cases}
$$

**Interpretación:** el área de solapamiento entre ambos pulsos crece linealmente, alcanza un máximo y luego decrece linealmente.

### 1.3.3 Respuesta de sistemas LTI a señales aleatorias

Si la entrada de un sistema LTI es un proceso aleatorio WSS $X(t)$ y la salida es $Y(t)$, entonces:

#### Media de salida

$$
 m_Y=\mathbb{E}[Y(t)]=m_X\int_{-\infty}^{\infty}h(\tau)d\tau = m_X H(0),
$$

si el sistema es estable y el proceso es WSS.

#### Autocorrelación de salida

La autocorrelación de la salida es

$$
 R_Y(\tau)=R_X(\tau)*h(\tau)*h^*(-\tau),
$$

en una formulación compacta equivalente. Más directamente en frecuencia:

$$
 S_Y(f)=|H(f)|^2S_X(f).
$$

Esta expresión es una de las más importantes del capítulo. Significa que el filtro modifica la PSD de entrada multiplicándola por su respuesta en potencia.

#### Correlación cruzada entrada-salida

$$
 R_{XY}(\tau)=R_X(\tau)*h(\tau),
$$

con el cuidado de la convención temporal empleada.

#### Caso de ruido blanco a la entrada

Si la entrada es ruido blanco con PSD plana

$$
 S_X(f)=\frac{N_0}{2},
$$

entonces

$$
 S_Y(f)=\frac{N_0}{2}|H(f)|^2.
$$

La potencia de ruido de salida es

$$
 P_Y=\int_{-\infty}^{\infty}S_Y(f)df=rac{N_0}{2}\int_{-\infty}^{\infty}|H(f)|^2df.
$$

Este resultado fundamenta la definición de ancho de banda de ruido equivalente.

[Figura 1.11]: Efecto de un sistema LTI sobre la PSD de una señal aleatoria. La figura debe mostrar tres paneles: PSD de entrada, magnitud cuadrática del filtro $|H(f)|^2$ y PSD de salida. La PSD de salida debe verse como el producto “moldeado” de las dos primeras. Deben señalarse frecuencias atenuadas y transmitidas, para enfatizar el papel del filtro como conformador espectral.

#### Ejemplo 1.18: ruido blanco a través de un filtro pasabajos ideal

Sea un filtro pasabajos ideal con

$$
 H(f)=
 \begin{cases}
 1, & |f|\le B,\\
 0, & |f|>B.
 \end{cases}
$$

La entrada es ruido blanco con PSD bilateral $S_X(f)=N_0/2$.

**Solución:**

La PSD de salida es

$$
 S_Y(f)=
 \begin{cases}
 \frac{N_0}{2}, & |f|\le B,\\
 0, & |f|>B.
 \end{cases}
$$

La potencia de ruido de salida resulta

$$
 P_Y=\int_{-B}^{B}\frac{N_0}{2}df=N_0B.
$$

**Conclusión:** el ruido blanco ideal tiene potencia infinita antes de filtrar, pero potencia finita a la salida de un filtro de ancho finito.

### 1.3.4 Ejemplo integrador de la sección

#### Ejemplo 1.19: respuesta de un filtro RC idealizado a un pulso digital

Considérese un sistema con respuesta en frecuencia aproximada

$$
 H(f)=\frac{1}{1+jf/f_c}.
$$

Si la entrada es un pulso rectangular de duración $T$, el espectro de salida es

$$
 Y(f)=AT\,\mathrm{sinc}(fT)\frac{1}{1+jf/f_c}.
$$

**Interpretación cualitativa:** las componentes altas del pulso, responsables de sus transiciones abruptas, quedan atenuadas. Por ello, en el dominio del tiempo la salida presenta bordes redondeados. Este fenómeno es la base del ensanchamiento de pulsos y la interferencia entre símbolos cuando el canal no tiene ancho suficiente.

---

## 1.4 Modelado de Ruido

El ruido es una perturbación aleatoria no deseada que se superpone a la señal útil. En comunicaciones digitales, el modelo más importante es el **ruido blanco Gaussiano aditivo (AWGN, Additive White Gaussian Noise)**, porque proporciona una aproximación muy útil y analíticamente tratable de numerosos fenómenos físicos.

### 1.4.1 Caracterización del ruido blanco Gaussiano (AWGN)

Un proceso $N(t)$ es AWGN si cumple simultáneamente:

1. **Aditivo:** se suma a la señal útil,

$$
 r(t)=s(t)+n(t).
$$

2. **Gaussiano:** para cualquier conjunto de instantes, las variables aleatorias asociadas tienen distribución conjunta Gaussiana; en particular, para cada $t$, $N(t)$ es Gaussiano.

3. **Blanco:** su PSD es constante en frecuencia,

$$
 S_N(f)=\frac{N_0}{2}, \quad -\infty<f<\infty,
$$

para la representación bilateral.

La media suele asumirse nula:

$$
 \mathbb{E}[N(t)]=0.
$$

#### Consecuencia sobre autocorrelación

Por Wiener-Khintchine,

$$
 R_N(\tau)=\frac{N_0}{2}\delta(\tau).
$$

Esto expresa ausencia ideal de correlación temporal para retardos no nulos.

#### Comentario físico

El ruido estrictamente blanco ideal no existe en toda la banda infinita; se trata de una idealización. Sin embargo, dentro del ancho de banda relevante de un sistema, muchos ruidos pueden modelarse como aproximadamente blancos.

[Figura 1.12]: Modelo de canal AWGN. La figura debe mostrar una señal digital en banda base entrando a un sumador donde se añade un bloque de ruido $n(t)$. Debe aparecer la ecuación $r(t)=s(t)+n(t)$ y, en un panel inferior, una PSD plana del ruido extendiéndose uniformemente sobre la frecuencia. La figura debe transmitir la idea de que el ruido afecta a toda la banda del sistema y que su suma con la señal es un proceso aleatorio.

### 1.4.2 Propiedades estadísticas del ruido blanco

Si $N(t)$ es AWGN de media nula:

- Media:

$$
 \mathbb{E}[N(t)]=0.
$$

- Varianza instantánea idealmente infinita si se considera ancho infinito. En práctica, tras filtrar a un ancho $B$, la potencia es finita.

- Autocorrelación:

$$
 R_N(\tau)=\frac{N_0}{2}\delta(\tau).
$$

- Para muestras temporales suficientemente separadas respecto a la banda efectiva, la correlación puede ser despreciable.

- Si el ruido es Gaussiano y de media cero, queda completamente caracterizado por su segundo orden.

#### Ruido blanco filtrado

A la salida de un filtro LTI con $H(f)$:

$$
 S_{N_o}(f)=\frac{N_0}{2}|H(f)|^2.
$$

La potencia de ruido de salida es

$$
 \sigma_{N_o}^2=\int_{-\infty}^{\infty}S_{N_o}(f)df=\frac{N_0}{2}\int_{-\infty}^{\infty}|H(f)|^2df.
$$

Este resultado aparece constantemente en el cálculo de ruido de receptores.

#### Ejemplo 1.20: autocorrelación de AWGN

Dado que $S_N(f)=N_0/2$, por transformada inversa de Fourier

$$
 R_N(\tau)=\int_{-\infty}^{\infty}\frac{N_0}{2}e^{j2\pi f\tau}df=rac{N_0}{2}\delta(\tau).
$$

**Interpretación:** el ruido blanco es no correlacionado en tiempos distintos. Matemáticamente, la concentración en $\tau=0$ se representa mediante una delta de Dirac.

### 1.4.3 Impacto en la relación señal-ruido (SNR)

La **relación señal-ruido** es una medida central del desempeño de un sistema de comunicaciones. En forma lineal se define como

$$
 \mathrm{SNR}=\frac{P_s}{P_n},
$$

donde $P_s$ es la potencia media de señal y $P_n$ la potencia media de ruido en el punto de observación considerado.

En decibelios,

$$
 \mathrm{SNR}_{\mathrm{dB}}=10\log_{10}\left(\frac{P_s}{P_n}\right).
$$

Si se trabaja con amplitudes o voltajes sobre igual impedancia,

$$
 \mathrm{SNR}_{\mathrm{dB}}=20\log_{10}\left(\frac{V_s}{V_n}\right).
$$

#### Relación con $E_b/N_0$

En comunicaciones digitales, además de la SNR tradicional, es muy importante el cociente energía por bit a densidad espectral de ruido:

$$
 \frac{E_b}{N_0}.
$$

Si la tasa de bits es $R_b$ y la potencia de señal es $P_s$,

$$
 E_b=\frac{P_s}{R_b}.
$$

Si la potencia de ruido en una banda $B$ es aproximadamente

$$
 P_n=N_0B,
$$

entonces la SNR puede relacionarse como

$$
 \mathrm{SNR}=\frac{P_s}{N_0B}=\frac{E_bR_b}{N_0B}=\frac{E_b}{N_0}\frac{R_b}{B}.
$$

Esta ecuación muestra el papel de la **eficiencia espectral** $R_b/B$.

[Figura 1.13]: Interpretación de la SNR en el tiempo y en frecuencia. La figura debe tener un panel temporal donde una señal digital limpia se compara con la misma señal contaminada con ruido de baja y alta potencia. En un panel espectral debe mostrarse una banda donde la potencia de señal sobresale sobre un piso de ruido. Debe incluirse una escala cualitativa que relacione mayor SNR con detección más confiable.

#### Ejemplo 1.21: cálculo de SNR

Sea una señal con potencia media de $1\ \mathrm{mW}$ y ruido con potencia de $10\ \mu\mathrm{W}$.

**Solución:**

$$
 \mathrm{SNR}=\frac{1\times 10^{-3}}{10\times 10^{-6}}=100.
$$

En decibelios,

$$
 \mathrm{SNR}_{\mathrm{dB}}=10\log_{10}(100)=20\ \mathrm{dB}.
$$

#### Ejemplo 1.22: potencia de ruido tras un filtro

Si $N_0/2=10^{-9}\ \mathrm{W/Hz}$ y el receptor tiene ancho pasabajos ideal $B=1\ \mathrm{MHz}$, la potencia total de ruido es

$$
 P_n=N_0B=2\times 10^{-9}\times 10^{6}=2\times 10^{-3}\ \mathrm{W}.
$$

Esto supone una PSD bilateral constante y filtro ideal.

### 1.4.4 Ruido térmico y fórmula de Nyquist

El ruido térmico surge de la agitación térmica de portadores de carga en conductores y resistencias. Es uno de los orígenes físicos más importantes del ruido electrónico.

#### Fórmula de Nyquist

La potencia de ruido disponible en una resistencia a temperatura absoluta $T$ sobre una banda $B$ es

$$
 P_n=kTB,
$$

donde:

- $k=1.380649\times 10^{-23}\ \mathrm{J/K}$ es la constante de Boltzmann,
- $T$ es la temperatura en kelvin,
- $B$ es el ancho de banda en hercios.

La densidad espectral unilateral correspondiente es

$$
 N_0=kT,
$$

y la bilateral es

$$
 \frac{N_0}{2}=\frac{kT}{2}.
$$

A temperatura ambiente, $T\approx 290\ \mathrm{K}$,

$$
 kT\approx 4\times 10^{-21}\ \mathrm{W/Hz},
$$

o en dBm/Hz,

$$
 10\log_{10}\left(\frac{kT}{1\ \mathrm{mW}}\right)\approx -174\ \mathrm{dBm/Hz}.
$$

Este valor es fundamental en presupuestos de enlace y diseño de receptores.

[Figura 1.14]: Origen físico del ruido térmico y su representación espectral. La figura debe mostrar una resistencia a temperatura $T$ con movimiento aleatorio de electrones y un bloque equivalente de fuente de ruido. En otro panel debe aparecer una PSD plana aproximadamente constante dentro de la banda de interés. Debe incluirse la ecuación $P_n=kTB$ como elemento central.

#### Ejemplo 1.23: cálculo de ruido térmico

Calcular la potencia de ruido térmico a $T=290\ \mathrm{K}$ en una banda de $B=1\ \mathrm{MHz}$.

**Solución:**

$$
 P_n=kTB=(1.380649\times 10^{-23})(290)(10^6).
$$

Numéricamente,

$$
 P_n\approx 4.00\times 10^{-15}\ \mathrm{W}.
$$

En dBm,

$$
 P_{n,\mathrm{dBm}}=10\log_{10}\left(\frac{4.00\times 10^{-15}}{10^{-3}}\right)
=10\log_{10}(4.00\times 10^{-12})
\approx -113.98\ \mathrm{dBm}.
$$

### 1.4.5 Ejemplo integrador de la sección

#### Ejemplo 1.24: señal digital rectangular en AWGN

Sea una señal polar NRZ con amplitud $\pm 1\ \mathrm{V}$ sobre $1\ \Omega$, de modo que la potencia media de la señal es

$$
 P_s=1\ \mathrm{W}.
$$

Si el receptor tiene ancho de banda equivalente de ruido $B_n=100\ \mathrm{kHz}$ y el canal aporta una densidad bilateral $N_0/2=10^{-7}\ \mathrm{W/Hz}$, entonces

$$
 N_0=2\times 10^{-7}\ \mathrm{W/Hz}.
$$

La potencia de ruido es

$$
 P_n=N_0B_n=2\times 10^{-7}\times 10^5=2\times 10^{-2}\ \mathrm{W}.
$$

Así,

$$
 \mathrm{SNR}=\frac{1}{0.02}=50.
$$

En decibelios,

$$
 \mathrm{SNR}_{\mathrm{dB}}=10\log_{10}(50)\approx 16.99\ \mathrm{dB}.
$$

**Interpretación:** aun con amplitud aparentemente alta, el desempeño depende críticamente de cuánto ruido atraviesa el filtro del receptor.

---

## 1.5 Ancho de Banda de Señales

El concepto de ancho de banda es central en comunicaciones digitales porque determina ocupación espectral, requisitos del canal, velocidad máxima de transmisión y sensibilidad al ruido e interferencia.

### 1.5.1 Concepto de ancho de banda

En sentido general, el **ancho de banda** es la extensión frecuencial significativa ocupada por una señal o transmitida por un sistema. Sin embargo, no existe una única definición universal. La definición adecuada depende del contexto: potencia, energía, respuesta del filtro o compromiso tiempo-frecuencia.

En señales ideales como el pulso rectangular, el espectro sinc se extiende infinitamente, por lo que no existe un corte natural exacto. De ahí la necesidad de definiciones operativas.

[Figura 1.15]: Diferentes interpretaciones del ancho de banda sobre un mismo espectro. La figura debe mostrar el espectro de un pulso rectangular con lóbulo principal y lóbulos laterales. Sobre él deben marcarse con colores distintos el primer nulo, el nivel de 3 dB, una región que contenga el 99% de la potencia y una anchura equivalente de ruido sobre un filtro ideal de igual área. El objetivo es que el lector vea de un vistazo por qué existen varias definiciones de ancho de banda.

### 1.5.2 Definiciones de ancho de banda

#### a) Ancho de banda a 3 dB

Es la frecuencia para la cual la potencia cae a la mitad del valor máximo, o equivalentemente la amplitud cae a $1/\sqrt{2}$ del máximo.

Si la respuesta en frecuencia de un sistema es $|H(f)|$, el ancho de banda a 3 dB $B_{3\mathrm{dB}}$ satisface

$$
 |H(B_{3\mathrm{dB}})|^2=\frac{1}{2}|H(0)|^2.
$$

Esta definición es muy usada en circuitos y filtros.

#### b) Ancho de banda de ruido equivalente

Se define como el ancho del filtro pasabajos ideal de ganancia máxima igual a $|H(0)|^2$ que dejaría pasar la misma potencia de ruido que el sistema real.

Para un filtro de referencia de baja frecuencia,

$$
 B_{eq}=\frac{1}{|H(0)|^2}\int_{0}^{\infty}|H(f)|^2df
$$

para PSD unilateral, o con la formulación bilateral correspondiente

$$
 B_{eq}=\frac{1}{|H(0)|^2}\cdot\frac{1}{2}\int_{-\infty}^{\infty}|H(f)|^2df.
$$

Es muy importante para calcular ruido de salida.

#### c) Ancho de banda de primer nulo

Es la frecuencia del primer cero del espectro. Para un pulso rectangular de duración $T$,

$$
 X(f)=AT\,\mathrm{sinc}(fT),
$$

y el primer nulo ocurre en

$$
 |f|=\frac{1}{T}.
$$

Entonces el ancho de banda unilateral de primer nulo es $1/T$ y el bilateral entre primeros nulos es $2/T$.

#### d) Ancho de banda al 99% de potencia

Es el menor ancho $B_{99}$ tal que

$$
 \int_{-B_{99}}^{B_{99}}S_x(f)df = 0.99 \int_{-\infty}^{\infty}S_x(f)df.
$$

Esta definición es útil cuando el espectro no es estrictamente limitado, pero sí concentra casi toda su potencia en una banda finita.

#### e) Ancho de banda de Gabor

El ancho de banda de Gabor surge del análisis conjunto tiempo-frecuencia. Se define mediante la dispersión cuadrática en frecuencia de una señal de energía normalizada. Si $|X(f)|^2$ se interpreta como densidad de energía espectral, la dispersión en frecuencia puede definirse como

$$
 \sigma_f^2=\frac{\int_{-\infty}^{\infty}(f-f_0)^2|X(f)|^2df}{\int_{-\infty}^{\infty}|X(f)|^2df},
$$

donde

$$
 f_0=\frac{\int_{-\infty}^{\infty}f|X(f)|^2df}{\int_{-\infty}^{\infty}|X(f)|^2df}
$$

es la frecuencia central espectral.

Análogamente, la dispersión temporal es

$$
 \sigma_t^2=\frac{\int_{-\infty}^{\infty}(t-t_0)^2|x(t)|^2dt}{\int_{-\infty}^{\infty}|x(t)|^2dt}.
$$

Gabor mostró una relación de incertidumbre:

$$
 \sigma_t\sigma_f \ge \frac{1}{4\pi}.
$$

**Interpretación:** una señal muy concentrada en tiempo necesariamente se dispersa en frecuencia, y viceversa. La gaussiana alcanza la cota mínima.

[Figura 1.16]: Compromiso tiempo-frecuencia y ancho de banda de Gabor. La figura debe comparar un pulso rectangular muy breve con una señal gaussiana más suave. En el dominio del tiempo, el rectangular debe aparecer más confinado; en el dominio de la frecuencia, su espectro debe ser más extenso y con lóbulos laterales. La gaussiana debe verse equilibrada temporal y espectralmente, ilustrando la desigualdad de incertidumbre.

#### Ejemplo 1.25: ancho de banda de primer nulo de un pulso rectangular

Para

$$
 x(t)=A\,\mathrm{rect}\left(\frac{t}{T}\right),
$$

su transformada es

$$
 X(f)=AT\,\mathrm{sinc}(fT).
$$

Los ceros ocurren en $f=\pm n/T$, con $n=1,2,\ldots$. El primer nulo está en

$$
 f=\pm \frac{1}{T}.
$$

Luego,

- ancho unilateral de primer nulo: $B=1/T$,
- ancho bilateral entre primeros nulos: $2/T$.

#### Ejemplo 1.26: ancho de banda a 3 dB de un filtro RC de primer orden

Sea

$$
 H(f)=\frac{1}{1+jf/f_c}.
$$

Entonces

$$
 |H(f)|^2=\frac{1}{1+(f/f_c)^2}.
$$

La condición de 3 dB es

$$
 \frac{1}{1+(f/f_c)^2}=\frac{1}{2}.
$$

De donde

$$
 1+(f/f_c)^2=2 \quad \Rightarrow \quad (f/f_c)^2=1.
$$

Así,

$$
 B_{3\mathrm{dB}}=f_c.
 $$

#### Ejemplo 1.27: ancho de banda de ruido equivalente de un filtro RC

Con el mismo filtro,

$$
 |H(f)|^2=\frac{1}{1+(f/f_c)^2}.
$$

Usando la definición unilateral,

$$
 B_{eq}=\int_0^{\infty}\frac{1}{1+(f/f_c)^2}df.
$$

Haciendo el cambio $u=f/f_c$, $df=f_cdu$:

$$
 B_{eq}=f_c\int_0^{\infty}\frac{1}{1+u^2}du=f_c\left[\tan^{-1}(u)\right]_0^{\infty}=rac{\pi}{2}f_c.
$$

**Resultado importante:** para un filtro RC de primer orden,

$$
 B_{eq}=\frac{\pi}{2}B_{3\mathrm{dB}}.
$$

### 1.5.3 Relación ancho de banda - tasa de datos

La tasa de bits $R_b$ y el ancho de banda están íntimamente relacionados. En banda base, transmitir bits más rápidamente requiere pulsos más cortos en el tiempo y, por la dualidad tiempo-frecuencia, ello implica mayor extensión espectral.

#### Caso de pulsos rectangulares NRZ

Si la duración de bit es $T_b$, entonces

$$
 R_b=\frac{1}{T_b}.
$$

El espectro del pulso elemental tiene primer nulo en

$$
 B\approx \frac{1}{T_b}=R_b.
$$

Esto sugiere que una señal NRZ rectangular requiere un ancho de banda del orden de la tasa binaria.

#### Criterio de Nyquist para ausencia de ISI

En teoría de transmisión digital, el criterio de Nyquist muestra que es posible transmitir a una tasa simbólica $R_s$ sobre un canal de ancho $B$ sin interferencia entre símbolos si se diseñan adecuadamente los pulsos. En su forma ideal mínima para banda base,

$$
 B_{\min}=\frac{R_s}{2}.
$$

Si cada símbolo porta $\log_2 M$ bits,

$$
 R_b=R_s\log_2 M.
$$

Luego,

$$
 B_{\min}=\frac{R_b}{2\log_2 M}.
$$

Esto evidencia que la modulación multinivel puede aumentar la eficiencia espectral, aunque normalmente a costa de mayor sensibilidad al ruido.

#### Eficiencia espectral

Se define como

$$
 \eta=\frac{R_b}{B} \quad [\text{bit/s/Hz}].
$$

Es una métrica central en el diseño de sistemas modernos.

[Figura 1.17]: Relación entre duración de pulso, tasa de bits y espectro. La figura debe mostrar dos pulsos NRZ: uno ancho (bit lento) y otro angosto (bit rápido). Debajo de cada uno debe aparecer su espectro sinc correspondiente, donde el pulso angosto exhibe un espectro más ancho. A la derecha debe incluirse un gráfico conceptual indicando que al aumentar $R_b$ suele aumentar el ancho de banda requerido, salvo que se use conformación de pulsos y técnicas de mayor eficiencia espectral.

#### Ejemplo 1.28: estimación de ancho de banda para NRZ

Una señal binaria NRZ transmite a

$$
 R_b=1\ \mathrm{Mb/s}.
$$

Entonces

$$
 T_b=1\ \mu s.
$$

El primer nulo del espectro del pulso elemental ocurre aproximadamente en

$$
 B\approx \frac{1}{T_b}=1\ \mathrm{MHz}.
$$

**Interpretación:** una transmisión más rápida exige mayor ancho de banda si se mantienen pulsos rectangulares.

#### Ejemplo 1.29: límite ideal de Nyquist

Si se desea transmitir a

$$
 R_b=10\ \mathrm{Mb/s}
$$

con modulación binaria ($M=2$, luego $R_s=R_b$), el ancho mínimo ideal de Nyquist es

$$
 B_{\min}=\frac{R_b}{2}=5\ \mathrm{MHz}.
$$

Si en cambio se usa una modulación cuaternaria ($M=4$), entonces $\log_2 M=2$ y

$$
 R_s=\frac{R_b}{2}=5\ \mathrm{Mbaud},
$$

por lo que el ancho mínimo ideal baja a

$$
 B_{\min}=\frac{R_s}{2}=2.5\ \mathrm{MHz}.
$$

**Conclusión:** transportar más bits por símbolo reduce el ancho de banda requerido, pero exige mayor precisión frente al ruido y distorsión.

### 1.5.4 Ejemplo integrador de la sección

#### Ejemplo 1.30: comparación de métricas de ancho de banda

Considérese un pulso rectangular de duración $T=0.5\ \mu s$.

1. **Primer nulo:**

$$
 B_{nulo}=\frac{1}{T}=2\ \mathrm{MHz}.
$$

2. **Relación con tasa de bits si representa un bit NRZ:**

$$
 R_b=\frac{1}{T}=2\ \mathrm{Mb/s}.
$$

3. **Comentario sobre 99% de potencia:** como el espectro sinc se extiende infinitamente, el ancho al 99% de potencia será finito pero superior al ancho de 3 dB del lóbulo principal e inferior a una interpretación “infinita”.

4. **Comentario sobre Gabor:** al ser un pulso abrupto y corto, su concentración temporal es alta, por lo que su dispersión en frecuencia también será alta.

Este ejemplo recuerda que “ancho de banda” no es un número absoluto independiente del criterio adoptado.

---

## Resumen de conceptos clave

- **Las señales determinísticas** pueden describirse exactamente y clasificarse por periodicidad, energía, potencia, simetría y causalidad.
- **Los promedios temporales** permiten definir valor medio, potencia media y valor eficaz.
- **La serie de Fourier** representa señales periódicas mediante sumas de armónicos discretos; **la transformada de Fourier** extiende esta idea a señales aperiódicas con espectro continuo.
- **La densidad espectral de potencia** describe cómo se reparte la potencia en frecuencia y se relaciona íntimamente con la autocorrelación.
- **Los procesos estocásticos** modelan señales aleatorias como ruido, secuencias digitales aleatorias e interferencias.
- **La estacionariedad** y la **ergodicidad** son hipótesis clave para poder inferir propiedades estadísticas a partir de observaciones temporales.
- El **teorema de Wiener-Khintchine** establece que, para procesos WSS, PSD y autocorrelación son pares de Fourier.
- El **periodograma de Welch** es un estimador práctico y robusto de la PSD, con menor varianza que el periodograma clásico.
- **Los sistemas LTI** se caracterizan completamente por su respuesta al impulso $h(t)$ o por su función de transferencia $H(f)$.
- Para entrada aleatoria WSS en un sistema LTI, se cumple la relación fundamental

$$
 S_Y(f)=|H(f)|^2S_X(f).
$$

- **El ruido AWGN** es el modelo de referencia en telecomunicaciones: Gaussiano, aditivo y con PSD plana.
- La **SNR** cuantifica la calidad del enlace, mientras que $E_b/N_0$ conecta energía por bit, ruido y rendimiento digital.
- El **ruido térmico** obedece la ley de Nyquist

$$
 P_n=kTB.
$$

- El **ancho de banda** admite múltiples definiciones operativas: a 3 dB, equivalente de ruido, de primer nulo, al 99% de potencia y de Gabor.
- Existe una relación fundamental entre **ancho de banda y tasa de datos**: pulsos más cortos en el tiempo requieren espectros más anchos.

**Idea final de la unidad:** las comunicaciones digitales en banda base se comprenden mejor como la interacción entre señales, sistemas, ruido y espectro. Todo el desarrollo posterior —modulación, filtrado óptimo, detección y desempeño— descansa sobre los conceptos estudiados en esta primera unidad.

---

## Referencias

1. A. V. Oppenheim, A. S. Willsky y S. H. Nawab, *Signals and Systems*, 2nd ed., Prentice Hall, 1997. ISBN de referencia clásica; no se dispone de DOI ampliamente estandarizado para esta edición.
2. B. P. Lathi, *Linear Systems and Signals*, 2nd ed., Oxford University Press, 2005. Texto clásico de sistemas y señales; sin DOI editorial de uso estándar.
3. S. Haykin, *Communication Systems*, 4th ed., Wiley, 2001. Texto de referencia en sistemas de comunicación; sin DOI editorial estándar ampliamente citado.
4. J. G. Proakis y M. Salehi, *Digital Communications*, 5th ed., McGraw-Hill, 2008. Texto de referencia en comunicaciones digitales; sin DOI editorial estándar ampliamente citado.
5. B. Sklar, *Digital Communications: Fundamentals and Applications*, 2nd ed., Prentice Hall, 2001. Texto clásico en comunicaciones digitales; sin DOI editorial estándar ampliamente citado.
6. P. D. Welch, “The use of fast Fourier transform for the estimation of power spectra: A method based on time averaging over short, modified periodograms,” *IEEE Transactions on Audio and Electroacoustics*, vol. 15, no. 2, pp. 70–73, 1967. DOI: $10.1109/TAU.1967.1161901$.
7. H. Nyquist, “Thermal agitation of electric charge in conductors,” *Physical Review*, vol. 32, no. 1, pp. 110–113, 1928. DOI: $10.1103/PhysRev.32.110$.
8. D. Gabor, “Theory of communication,” *Journal of the Institution of Electrical Engineers - Part III: Radio and Communication Engineering*, vol. 93, no. 26, pp. 429–457, 1946. DOI: $10.1049/ji-3-2.1946.0074$.
9. N. Wiener, *Extrapolation, Interpolation, and Smoothing of Stationary Time Series*, MIT Press, 1949. Referencia fundamental para procesos estacionarios; sin DOI editorial estándar ampliamente usado.
10. A. Khintchine, “Korrelationstheorie der stationären stochastischen Prozesse,” *Mathematische Annalen*, vol. 109, pp. 604–615, 1934. DOI: $10.1007/BF01449156$.

