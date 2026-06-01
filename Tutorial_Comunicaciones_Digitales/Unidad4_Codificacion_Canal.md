# Unidad 4: Codificación de Canal

## Introducción de la unidad

La **codificación de canal** constituye uno de los pilares de las comunicaciones digitales modernas. Su propósito es introducir **redundancia controlada** en la información transmitida para **detectar** y, en muchos casos, **corregir** errores causados por ruido, interferencia, desvanecimiento y otras degradaciones del canal. En términos conceptuales, la codificación de canal transforma una secuencia de bits de información en una secuencia más larga, estructurada de acuerdo con reglas algebraicas o temporales, de modo que el receptor pueda inferir el mensaje original incluso cuando algunos símbolos hayan sido alterados durante la transmisión.

Desde una perspectiva geométrica y probabilística, la codificación de canal puede entenderse como un mecanismo para **separar más claramente** los mensajes posibles en el espacio de señales. Cuanto mayor sea la separación entre palabras-código o trayectorias válidas, menor será la probabilidad de que el ruido haga que el receptor confunda una palabra con otra. Esta idea conecta directamente con conceptos fundamentales como la **distancia euclidiana**, la **distancia de Hamming**, el **síndrome**, la **distancia mínima** y la **distancia libre**.

En esta unidad estudiaremos tres bloques fundamentales:

- **4.1 Espacio de señal y espacios vectoriales**, que proporciona el fundamento geométrico de la detección óptima.
- **4.2 Codificación de bloques**, basada en estructuras algebraicas finitas y matrices generadoras y de chequeo.
- **4.3 Codificación convolucional**, basada en memoria, diagramas de estados y decodificación óptima mediante el algoritmo de Viterbi.

El enfoque será **pedagógico**, **matemáticamente riguroso** y orientado a estudiantes que se inician en el tema, pero sin sacrificar profundidad formal.

---

# 4.1 Espacio de Señal y Espacios Vectoriales

## 4.1.1 Representación vectorial de señales

En comunicaciones digitales, una señal transmitida en un intervalo temporal $0 \le t \le T$ puede representarse como un elemento de un espacio funcional. Si el conjunto de señales de interés tiene dimensión finita, es posible describir cada señal como una combinación lineal de funciones base ortonormales.

Sea un conjunto de señales
$$
\mathcal{S} = \{s_1(t), s_2(t), \dots, s_M(t)\}, \quad 0 \le t \le T.
$$

Si existen $N$ funciones base ortonormales $\{\phi_1(t), \phi_2(t), \dots, \phi_N(t)\}$ tales que toda señal $s_m(t)$ puede escribirse como
$$
s_m(t) = \sum_{i=1}^{N} s_{mi}\, \phi_i(t),
$$
entonces la señal queda asociada al vector
$$
\mathbf{s}_m = [s_{m1}, s_{m2}, \dots, s_{mN}]^{T}.
$$

Los coeficientes se obtienen por proyección:
$$
s_{mi} = \langle s_m(t), \phi_i(t) \rangle = \int_0^T s_m(t)\,\phi_i(t)\,dt.
$$

Aquí el producto interno entre dos señales $x(t)$ y $y(t)$ se define como
$$
\langle x(t), y(t) \rangle = \int_0^T x(t)y(t)\,dt.
$$

La energía de una señal resulta
$$
E_s = \int_0^T |s_m(t)|^2 dt = \sum_{i=1}^{N} s_{mi}^2 = \|\mathbf{s}_m\|^2.
$$

**Concepto clave:** la representación vectorial transforma un problema de detección de señales continuas en un problema geométrico en $\mathbb{R}^N$.

[Figura 4.1]: Imagine un conjunto de señales temporales distintas, cada una proyectada sobre dos o tres funciones base ortonormales. La figura debe mostrar, a la izquierda, varias formas de onda en el tiempo y, a la derecha, los puntos correspondientes en un plano o espacio tridimensional. El objetivo pedagógico de la figura es enfatizar que señales aparentemente complejas en el dominio temporal pueden verse como vectores en un espacio geométrico, donde distancias y ángulos adquieren significado físico en la detección.

### Ejemplo 4.1: Representación vectorial en una base dada

Considérese la base ortonormal en $[0,T]$ formada por dos funciones $\phi_1(t)$ y $\phi_2(t)$, y la señal
$$
s(t) = 3\phi_1(t) - 2\phi_2(t).
$$

Entonces su representación vectorial es
$$
\mathbf{s} = [3, -2]^T.
$$

La energía vale
$$
E_s = 3^2 + (-2)^2 = 13.
$$

Si otra señal es
$$
r(t)=2\phi_1(t)+\phi_2(t),
$$
entonces su vector es
$$
\mathbf{r} = [2,1]^T,
$$
y el producto interno entre ambas señales es
$$
\langle s,r\rangle = 3\cdot 2 + (-2)\cdot 1 = 4.
$$

Por tanto, el ángulo $\theta$ entre ambos vectores satisface
$$
\cos\theta = \frac{\langle s,r\rangle}{\|\mathbf{s}\|\,\|\mathbf{r}\|} = \frac{4}{\sqrt{13}\sqrt{5}}.
$$

---

## 4.1.2 Base ortonormal: procedimiento de Gram-Schmidt

Con frecuencia las señales disponibles no son ortogonales entre sí. En tal caso, puede construirse una base ortonormal equivalente mediante el procedimiento de **Gram-Schmidt**.

Sea un conjunto linealmente independiente de funciones $\{g_1(t), g_2(t), \dots, g_N(t)\}$. El procedimiento construye funciones ortonormales $\{\phi_1(t), \phi_2(t), \dots, \phi_N(t)\}$ tales que generan el mismo subespacio.

### Paso 1
Se define
$$
\phi_1(t) = \frac{g_1(t)}{\|g_1(t)\|}, \qquad \|g_1(t)\| = \sqrt{\langle g_1,g_1\rangle}.
$$

### Paso 2
Se elimina de $g_2(t)$ la componente en la dirección de $\phi_1(t)$:
$$
u_2(t)=g_2(t)-\langle g_2,\phi_1\rangle\phi_1(t).
$$
Luego se normaliza:
$$
\phi_2(t)=\frac{u_2(t)}{\|u_2(t)\|}.
$$

### Paso general
Para $k\ge 2$,
$$
u_k(t)=g_k(t)-\sum_{i=1}^{k-1}\langle g_k,\phi_i\rangle\phi_i(t),
$$
$$
\phi_k(t)=\frac{u_k(t)}{\|u_k(t)\|}.
$$

Estas funciones satisfacen
$$
\langle \phi_i,\phi_j\rangle =
\begin{cases}
1, & i=j,\\
0, & i\ne j.
\end{cases}
$$

**Concepto clave:** Gram-Schmidt no cambia la información contenida en las señales; solo cambia el sistema de coordenadas a uno más conveniente.

[Figura 4.2]: La figura debe representar geométricamente el procedimiento de Gram-Schmidt en un plano o espacio tridimensional. Primero se muestra el vector original $g_1$ y su versión normalizada $\phi_1$. Después, el vector $g_2$ se descompone en una proyección sobre $\phi_1$ y una componente ortogonal $\nu_2$, que al normalizarse produce $\phi_2$. Esta visualización es esencial para comprender que el algoritmo elimina dependencias angulares y construye ejes mutuamente perpendiculares.

### Ejemplo 4.2: Gram-Schmidt con dos señales

Considérense dos señales en $[0,T]$:
$$
g_1(t)=1,
$$
$$
g_2(t)=t,
$$
para $0\le t\le 1$.

#### Paso 1: normalización de $g_1(t)$
Se calcula
$$
\|g_1\| = \sqrt{\int_0^1 1^2 dt} = 1.
$$
Así,
$$
\phi_1(t)=1.
$$

#### Paso 2: ortogonalización de $g_2(t)$
La proyección de $g_2$ sobre $\phi_1$ es
$$
\langle g_2,\phi_1\rangle = \int_0^1 t\,dt = \frac{1}{2}.
$$
Entonces
$$
\nu_2(t)=t-\frac{1}{2}.
$$
Su norma es
$$
\|\nu_2\| = \sqrt{\int_0^1 \left(t-\frac{1}{2}\right)^2 dt}
= \sqrt{\frac{1}{12}} = \frac{1}{2\sqrt{3}}.
$$
Por tanto,
$$
\phi_2(t)=\frac{t-1/2}{1/(2\sqrt{3})}=2\sqrt{3}\left(t-\frac{1}{2}\right).
$$

Se verifica que
$$
\langle \phi_1,\phi_2\rangle=0,
$$
y ambas funciones tienen norma unitaria.

---

## 4.1.3 Geometría de las señales de comunicación

Una vez representadas como vectores, las señales transmitidas se convierten en puntos en un espacio euclidiano. El canal con ruido aditivo blanco gaussiano (AWGN) puede modelarse como
$$
r(t)=s_m(t)+n(t),
$$
o, en forma vectorial,
$$
\mathbf{r}=\mathbf{s}_m+\mathbf{n},
$$
donde $\mathbf{n}$ es un vector gaussiano con componentes independientes de media cero y varianza $N_0/2$ sobre cada dimensión ortonormal.

La detección óptima por máxima verosimilitud en AWGN consiste en elegir la señal $\mathbf{s}_i$ que minimiza la distancia euclidiana al vector recibido:
$$
\hat{\mathbf{s}} = \arg\min_{\mathbf{s}_i\in\mathcal{S}} \|\mathbf{r}-\mathbf{s}_i\|^2.
$$

Si todas las señales son equiprobables y de igual energía, esto equivale a seleccionar la señal más cercana geométricamente.

### Regiones de decisión
El espacio se divide en regiones de Voronoi. Cada región contiene todos los puntos más cercanos a una señal dada que a las demás.

Si el ruido desplaza el punto transmitido dentro de su región, no hay error. Si lo desplaza fuera de ella, ocurre un error de decisión.

[Figura 4.3]: La figura debe mostrar varias señales representadas como puntos en un plano y las fronteras de decisión entre ellas, definidas por los lugares geométricos donde la distancia a dos señales es igual. Es útil destacar una realización del ruido que mueve el punto transmitido sin cruzar la frontera y otra que sí la cruza, para conectar directamente la geometría con el fenómeno de error de detección.

### Correlación y ángulo entre señales
Dos señales cercanas angularmente son más fáciles de confundir. La correlación entre señales se expresa como
$$
\langle s_i,s_j\rangle = \sum_{k=1}^{N} s_{ik}s_{jk}.
$$

Si las señales son ortogonales,
$$
\langle s_i,s_j\rangle = 0,
$$
lo que favorece la separación geométrica y simplifica la detección.

### Ejemplo 4.3: Señales antipodales

Considérense dos señales binarias antipodales:
$$
s_1(t)=+\sqrt{E_b}\,\phi(t), \qquad s_2(t)=-\sqrt{E_b}\,\phi(t),
$$
con $\|\phi(t)\|=1$.

Las representaciones vectoriales son
$$
\mathbf{s}_1=[\sqrt{E_b}], \qquad \mathbf{s}_2=[-\sqrt{E_b}].
$$

La distancia euclidiana entre ambas señales es
$$
d_E = \|\mathbf{s}_1-\mathbf{s}_2\| = 2\sqrt{E_b}.
$$

La frontera de decisión está en el origen. Si se transmite $s_1$ y el ruido es suficientemente negativo como para que la observación caiga a la izquierda de cero, se decide erróneamente $s_2$.

---

## 4.1.4 Distancia euclidiana y su relación con la probabilidad de error

La distancia euclidiana entre dos señales $s_i(t)$ y $s_j(t)$ se define como
$$
d_{ij} = \left( \int_0^T |s_i(t)-s_j(t)|^2 dt \right)^{1/2}.
$$

En representación vectorial,
$$
d_{ij}=\|\mathbf{s}_i-\mathbf{s}_j\|.
$$

### Probabilidad de error binaria en AWGN
Para dos señales equiprobables, la probabilidad de error óptima es
$$
P_e = Q\left(\frac{d_{12}}{2\sigma}\right),
$$
donde $\sigma^2=N_0/2$ por dimensión, y
$$
Q(x)=\frac{1}{\sqrt{2\pi}}\int_x^{\infty} e^{-u^2/2}\,du.
$$

Equivalentemente,
$$
P_e = Q\left(\sqrt{\frac{d_{12}^2}{2N_0}}\right).
$$

Esto muestra un resultado central: **a mayor distancia euclidiana entre señales, menor probabilidad de error**.

### Caso antipodal
Si $d_{12}=2\sqrt{E_b}$,
$$
P_e = Q\left(\sqrt{\frac{2E_b}{N_0}}\right).
$$

### Caso ortogonal binario coherente
Si dos señales ortogonales tienen energía $E_b$, la distancia es
$$
d_{12} = \sqrt{E_b+E_b} = \sqrt{2E_b},
$$
y por tanto
$$
P_e = Q\left(\sqrt{\frac{E_b}{N_0}}\right).
$$

Esto confirma que la señalización antipodal ofrece mejor desempeño que la ortogonal binaria coherente para la misma energía por bit.

[Figura 4.4]: La figura debe comparar, sobre una recta o plano, dos constelaciones binarias: una antipodal y otra ortogonal. Debe remarcarse la separación entre puntos y su relación con la frontera de decisión. Una buena descripción pedagógica destacaría que la constelación antipodal “usa mejor” el espacio disponible al maximizar la distancia entre señales para una energía dada.

### Ejemplo 4.4: Cálculo de probabilidad de error a partir de la distancia

Supóngase un sistema binario con distancia euclidiana entre señales
$$
d_{12}=4,
$$
y varianza de ruido por dimensión
$$
\sigma^2=1.
$$
Entonces
$$
P_e = Q\left(\frac{4}{2\cdot 1}\right)=Q(2).
$$

Usando tablas de la función $Q$,
$$
Q(2)\approx 2.28\times 10^{-2}.
$$

Por tanto,
$$
P_e \approx 0.0228.
$$

Si la distancia se duplicara a $d_{12}=8$,
$$
P_e = Q(4) \approx 3.17\times 10^{-5},
$$
lo que demuestra la fuerte sensibilidad del error frente a la separación geométrica.

---

## 4.1.5 Ejemplos resueltos integradores

### Ejemplo 4.5: Expansión de señales y distancia entre ellas

Sean las señales
$$
s_1(t)=\phi_1(t),
$$
$$
s_2(t)=\frac{1}{2}\phi_1(t)+\frac{\sqrt{3}}{2}\phi_2(t),
$$
con base ortonormal $\{\phi_1,\phi_2\}$.

Sus vectores son
$$
\mathbf{s}_1=[1,0]^T,
$$
$$
\mathbf{s}_2=\left[\frac{1}{2},\frac{\sqrt{3}}{2}\right]^T.
$$

La distancia euclidiana es
$$
d_{12}^2 = \left(1-\frac{1}{2}\right)^2 + \left(0-\frac{\sqrt{3}}{2}\right)^2
=\frac{1}{4}+\frac{3}{4}=1.
$$
Luego,
$$
d_{12}=1.
$$

El producto interno es
$$
\langle s_1,s_2\rangle = \frac{1}{2}.
$$

Como ambas señales tienen energía unitaria,
$$
\cos\theta = \frac{1}{2}, \qquad \theta = 60^{\circ}.
$$

### Ejemplo 4.6: Construcción de receptor correlador

Si una señal cualquiera del conjunto bidimensional se expresa como
$$
s_m(t)=s_{m1}\phi_1(t)+s_{m2}\phi_2(t),
$$
el receptor óptimo puede proyectar la observación $r(t)$ sobre cada base:
$$
r_1=\int_0^T r(t)\phi_1(t)dt,
$$
$$
r_2=\int_0^T r(t)\phi_2(t)dt.
$$

El vector recibido será
$$
\mathbf{r}=[r_1,r_2]^T.
$$
La decisión se toma comparando $\mathbf{r}$ con todos los vectores válidos del alfabeto.

**Interpretación:** el banco de correladores o filtros casados implementa físicamente la proyección sobre la base ortonormal.

---

# 4.2 Codificación de Bloques

## 4.2.1 Conceptos fundamentales: código $(n,k)$, tasa de código, distancia de Hamming

Un **código de bloque** transforma una palabra de información de longitud $k$ bits en una palabra-código de longitud $n$ bits. Se habla de un código $(n,k)$.

- $k$: número de bits de información.
- $n$: número total de bits transmitidos.
- $n-k$: bits de redundancia.

La **tasa de código** se define como
$$
R = \frac{k}{n}.
$$

Cuanto mayor es $R$, menor es la redundancia; cuanto menor es $R$, mayor es la capacidad potencial de protección, a costa de eficiencia espectral.

### Distancia de Hamming
La distancia de Hamming entre dos palabras binarias $\mathbf{x}$ y $\mathbf{y}$, denotada $d_H(\mathbf{x},\mathbf{y})$, es el número de posiciones en que difieren.

Ejemplo:
$$
\mathbf{x}=101101, \qquad \mathbf{y}=100001.
$$
Difieren en dos posiciones, por tanto
$$
d_H(\mathbf{x},\mathbf{y})=2.
$$

El **peso de Hamming** de una palabra $\mathbf{x}$, denotado $w_H(\mathbf{x})$, es el número de unos que contiene.

Para códigos lineales,
$$
d_H(\mathbf{x},\mathbf{y}) = w_H(\mathbf{x}+\mathbf{y}),
$$
donde la suma es módulo 2.

La **distancia mínima** de un código es
$$
d_{\min} = \min_{\mathbf{c}_i\ne \mathbf{c}_j} d_H(\mathbf{c}_i,\mathbf{c}_j).
$$

Esta magnitud determina la capacidad de detección y corrección.

[Figura 4.5]: La figura debe mostrar varias palabras-código binarias representadas como nodos en un hipercubo o, de forma más pedagógica, como cadenas de bits con posiciones marcadas. La idea es ilustrar visualmente qué significa distancia de Hamming: contar cuántos bits deben cambiar para transformar una palabra en otra. También conviene sugerir “esferas” de Hamming alrededor de cada código para anticipar el concepto de corrección de errores.

### Ejemplo 4.7: Parámetros básicos de un código

Considérese el código
$$
\mathcal{C}=\{000,011,101,110\}.
$$

Hay $4$ palabras-código, luego
$$
2^k=4 \Rightarrow k=2.
$$
Como cada palabra tiene longitud 3,
$$
n=3.
$$
Por tanto es un código $(3,2)$ con tasa
$$
R=\frac{2}{3}.
$$

Calculamos distancias:
- $d_H(000,011)=2$
- $d_H(000,101)=2$
- $d_H(000,110)=2$
- $d_H(011,101)=2$
- $d_H(011,110)=2$
- $d_H(101,110)=2$

Así,
$$
d_{\min}=2.
$$

---

## 4.2.2 Códigos lineales: definición y propiedades

Un código binario de bloque de longitud $n$ es **lineal** si el conjunto de palabras-código forma un subespacio vectorial de $\mathbb{F}_2^n$.

Esto implica:
1. La palabra nula $\mathbf{0}$ pertenece al código.
2. La suma módulo 2 de dos palabras-código es otra palabra-código.
3. Todo múltiplo escalar (en $\mathbb{F}_2$, solo 0 o 1) de una palabra-código pertenece al código.

Si el código tiene dimensión $k$, entonces contiene exactamente
$$
2^k
$$
palabras-código.

### Propiedad fundamental
En un código lineal,
$$
d_{\min} = \min_{\mathbf{c}\ne \mathbf{0}} w_H(\mathbf{c}).
$$

Es decir, basta buscar el peso mínimo entre palabras-código no nulas.

### Ejemplo 4.8: Verificación de linealidad

Sea
$$
\mathcal{C}=\{000,011,101,110\}.
$$

Verificamos cierres:
$$
011+101=110,
$$
$$
011+110=101,
$$
$$
101+110=011.
$$
Además, $000\in\mathcal{C}$. Luego el código es lineal.

Los pesos de las palabras no nulas son todos 2, por tanto
$$
d_{\min}=2.
$$

---

## 4.2.3 Matriz generadora $G$: construcción y forma sistemática

Un código lineal $(n,k)$ puede describirse mediante una **matriz generadora** $G$ de tamaño $k\times n$, cuyas filas son linealmente independientes y generan el código.

Si $\mathbf{u}$ es una palabra de información de longitud $k$, la palabra-código es
$$
\mathbf{c} = \mathbf{u}G.
$$

Todas las operaciones son en $\mathbb{F}_2$.

### Forma sistemática
Una forma particularmente útil es
$$
G = [I_k\; P],
$$
donde:
- $I_k$ es la matriz identidad $k\times k$,
- $P$ es una matriz $k\times(n-k)$.

En este caso, la palabra-código tiene la forma
$$
\mathbf{c}=[\mathbf{u}\;\mathbf{p}],
$$
con los bits de información explícitos y seguidos de bits de paridad.

### Ejemplo 4.9: Construcción de un código a partir de $G$

Sea
$$
G=
\begin{bmatrix}
1 & 0 & 0 & 1 & 1\\
0 & 1 & 0 & 1 & 0\\
0 & 0 & 1 & 0 & 1
\end{bmatrix}.
$$

Es un código $(5,3)$, ya que $G$ tiene 3 filas y 5 columnas. La tasa es
$$
R=\frac{3}{5}.
$$

Para la palabra de información
$$
\mathbf{u}=[1\;0\;1],
$$
la palabra-código es
$$
\mathbf{c}=\mathbf{u}G = [1\;0\;1]
\begin{bmatrix}
1 & 0 & 0 & 1 & 1\\
0 & 1 & 0 & 1 & 0\\
0 & 0 & 1 & 0 & 1
\end{bmatrix}.
$$

La multiplicación módulo 2 da
$$
\mathbf{c}=[1\;0\;1\;1\;0].
$$

Comprobación componente a componente:
- Primera: $1$
- Segunda: $0$
- Tercera: $1$
- Cuarta: $1\oplus 0 = 1$
- Quinta: $1\oplus 1 = 0$

---

## 4.2.4 Codificación usando $G$

Dado un mensaje binario $\mathbf{u}$ de longitud $k$, la codificación es el producto lineal
$$
\mathbf{c}=\mathbf{u}G.
$$

Si $G$ está en forma sistemática $[I_k\;P]$, entonces los primeros $k$ bits de $\mathbf{c}$ coinciden con el mensaje.

### Ejemplo 4.10: Enumeración completa de palabras-código

Con la matriz generadora del ejemplo anterior,
$$
G=
\begin{bmatrix}
1 & 0 & 0 & 1 & 1\\
0 & 1 & 0 & 1 & 0\\
0 & 0 & 1 & 0 & 1
\end{bmatrix},
$$
se generan todas las palabras-código para las $2^3=8$ palabras de información:

1. $\mathbf{u}=000 \Rightarrow \mathbf{c}=00000$
2. $\mathbf{u}=001 \Rightarrow \mathbf{c}=00101$
3. $\mathbf{u}=010 \Rightarrow \mathbf{c}=01010$
4. $\mathbf{u}=011 \Rightarrow \mathbf{c}=01111$
5. $\mathbf{u}=100 \Rightarrow \mathbf{c}=10011$
6. $\mathbf{u}=101 \Rightarrow \mathbf{c}=10110$
7. $\mathbf{u}=110 \Rightarrow \mathbf{c}=11001$
8. $\mathbf{u}=111 \Rightarrow \mathbf{c}=11100$

Los pesos no nulos son: $2,2,4,3,3,3,3$, luego
$$
d_{\min}=2.
$$

---

## 4.2.5 Matriz de chequeo de paridad $H$: construcción y relación con $G$

La **matriz de chequeo de paridad** $H$ es una matriz de tamaño $(n-k)\times n$ tal que una palabra $\mathbf{c}$ pertenece al código si y solo si
$$
\mathbf{c}H^T=\mathbf{0}.
$$

Si $G$ está en forma sistemática
$$
G=[I_k\;P],
$$
entonces una matriz de chequeo compatible es
$$
H=[P^T\;I_{n-k}].
$$

En binario, el signo negativo no importa porque $-1 \equiv 1 \pmod 2$.

La relación fundamental es
$$
GH^T=0.
$$

### Ejemplo 4.11: Construcción de $H$ a partir de $G$

Dado
$$
G=
\begin{bmatrix}
1 & 0 & 0 & 1 & 1\\
0 & 1 & 0 & 1 & 0\\
0 & 0 & 1 & 0 & 1
\end{bmatrix}
= [I_3\;P],
$$
se tiene
$$
P=
\begin{bmatrix}
1 & 1\\
1 & 0\\
0 & 1
\end{bmatrix}.
$$
Por tanto,
$$
H=[P^T\;I_2]=
\begin{bmatrix}
1 & 1 & 0 & 1 & 0\\
1 & 0 & 1 & 0 & 1
\end{bmatrix}.
$$

Verificación:
$$
GH^T=0.
$$

Por ejemplo, para la primera fila de $G$, $[1\;0\;0\;1\;1]$:
$$
[1\;0\;0\;1\;1]
\begin{bmatrix}
1 & 1\\
1 & 0\\
0 & 1\\
1 & 0\\
0 & 1
\end{bmatrix}
=
[1\oplus 1,\;1\oplus 1]=[0,0].
$$

---

## 4.2.6 Síndrome: definición $s=rH^T$, interpretación

Si se recibe una palabra
$$
\mathbf{r}=\mathbf{c}+\mathbf{e},
$$
donde $\mathbf{e}$ es el vector de error, entonces el **síndrome** se define como
$$
\mathbf{s}=\mathbf{r}H^T.
$$

Sustituyendo,
$$
\mathbf{s}=(\mathbf{c}+\mathbf{e})H^T = \mathbf{c}H^T + \mathbf{e}H^T = \mathbf{e}H^T,
$$
porque $\mathbf{c}H^T=0$.

**Interpretación clave:** el síndrome depende solo del patrón de error, no de la palabra-código transmitida.

Si $\mathbf{s}=0$, la palabra recibida es una palabra-código válida (aunque en algunos casos podría contener un patrón de error no detectable). Si $\mathbf{s}\ne 0$, se detecta error.

### Ejemplo 4.12: Cálculo del síndrome

Usando la matriz
$$
H=
\begin{bmatrix}
1 & 1 & 0 & 1 & 0\\
1 & 0 & 1 & 0 & 1
\end{bmatrix},
$$
supóngase que se recibe
$$
\mathbf{r}=10100.
$$

Entonces
$$
\mathbf{s}=\mathbf{r}H^T = [1\;0\;1\;0\;0]
\begin{bmatrix}
1 & 1\\
1 & 0\\
0 & 1\\
1 & 0\\
0 & 1
\end{bmatrix}.
$$

Primera componente:
$$
1\cdot 1 \oplus 0\cdot 1 \oplus 1\cdot 0 \oplus 0\cdot 1 \oplus 0\cdot 0 = 1.
$$
Segunda componente:
$$
1\cdot 1 \oplus 0\cdot 0 \oplus 1\cdot 1 \oplus 0\cdot 0 \oplus 0\cdot 1 = 1\oplus 1=0.
$$

Por tanto,
$$
\mathbf{s}=[1\;0].
$$

Se detecta error.

---

## 4.2.7 Capacidad de detección y corrección de errores

Si un código tiene distancia mínima $d_{\min}$, entonces:

- Puede **detectar** hasta
$$
d_{\min}-1
$$
errores.

- Puede **corregir** hasta
$$
t = \left\lfloor \frac{d_{\min}-1}{2} \right\rfloor
$$
errores.

### Justificación intuitiva
Para corregir $t$ errores, las esferas de Hamming de radio $t$ alrededor de palabras-código distintas no deben solaparse. Esto exige
$$
2t+1 \le d_{\min}.
$$

### Ejemplo 4.13: Capacidad correctora

Si un código tiene
$$
d_{\min}=5,
$$
entonces puede detectar hasta
$$
5-1=4
$$
errores y corregir hasta
$$
\left\lfloor\frac{5-1}{2}\right\rfloor=2
$$
errores.

Si ocurren 3 errores, el receptor puede detectar que algo anda mal, pero no necesariamente decidir de forma única cuál era la palabra original.

[Figura 4.6]: La figura debe representar esferas de Hamming alrededor de distintas palabras-código. Cada esfera incluye todas las palabras recibidas que se encuentran a distancia menor o igual que $t$. La figura debe mostrar visualmente que, cuando las esferas no se superponen, la corrección es inequívoca; cuando empiezan a solaparse, aparece la ambigüedad. Esta es una imagen central para conectar la teoría algebraica con la geometría discreta.

---

## 4.2.8 Arreglo estándar: construcción y líderes de coset

El **arreglo estándar** organiza todas las palabras de $\mathbb{F}_2^n$ en una tabla cuyas filas son cosets del código.

- La primera fila contiene todas las palabras-código.
- Cada fila adicional se obtiene sumando un vector llamado **líder de coset** a todas las palabras-código.
- El líder de coset suele escogerse como el vector de menor peso no incluido en filas previas.

Si $\mathcal{C}$ es un código lineal, cada coset tiene la forma
$$
\mathbf{e}+\mathcal{C} = \{\mathbf{e}+\mathbf{c}:\mathbf{c}\in\mathcal{C}\}.
$$

### Ejemplo 4.14: Arreglo estándar para un código simple

Considérese el código
$$
\mathcal{C}=\{000,011,101,110\}.
$$

La primera fila es
$$
000\quad 011\quad 101\quad 110.
$$

Elegimos como primer líder no usado el vector de menor peso:
$$
001.
$$
Entonces su coset es
$$
001+\mathcal{C} = \{001,010,100,111\}.
$$

El arreglo estándar completo es

| Líder de coset | Elementos del coset |
|---|---|
| 000 | 000, 011, 101, 110 |
| 001 | 001, 010, 100, 111 |

Aquí ya se cubren las $2^3=8$ palabras binarias posibles.

**Interpretación:** si una palabra recibida pertenece a la fila cuyo líder es $001$, el decodificador supone que el error más probable fue precisamente $001$.

---

## 4.2.9 Decodificación por síndrome y tabla de búsqueda

La decodificación por síndrome asocia cada síndrome a un patrón de error probable, usualmente el líder de coset.

Procedimiento:
1. Se recibe $\mathbf{r}$.
2. Se calcula el síndrome
$$
\mathbf{s}=\mathbf{r}H^T.
$$
3. Se consulta una tabla síndrome $\leftrightarrow$ líder de coset.
4. Se estima el error $\hat{\mathbf{e}}$.
5. Se corrige:
$$
\hat{\mathbf{c}}=\mathbf{r}+\hat{\mathbf{e}}.
$$

### Ejemplo 4.15: Decodificación por síndrome

Consideremos el código binario de paridad par
$$
\mathcal{C}=\{000,011,101,110\},
$$
que es un código lineal $(3,2)$ con matriz de chequeo
$$
H=\begin{bmatrix}1 & 1 & 1\end{bmatrix}.
$$

Para cualquier palabra recibida $\mathbf{r}=[r_1\;r_2\;r_3]$, el síndrome es
$$
s=\mathbf{r}H^T=r_1\oplus r_2\oplus r_3.
$$

Por tanto:
- si $s=0$, la palabra recibida tiene paridad par y pertenece al código;
- si $s=1$, la palabra recibida no pertenece al código y se detecta error.

Construimos la tabla de síndromes más simple:

| Síndrome | Interpretación |
|---|---|
| $0$ | no se detecta error |
| $1$ | se detecta error |

Supóngase que se transmite la palabra-código
$$
\mathbf{c}=110.
$$
Si durante la transmisión se invierte el tercer bit, el error es
$$
\mathbf{e}=001,
$$
y la palabra recibida es
$$
\mathbf{r}=\mathbf{c}+\mathbf{e}=111.
$$

Calculamos el síndrome:
$$
s=111H^T = 1\oplus 1\oplus 1 = 1.
$$

Luego se detecta que hubo error. Sin embargo, este código tiene
$$
d_{\min}=2,
$$
por lo que **no puede corregirlo unívocamente**. En efecto, cualquiera de los tres errores de un solo bit produce el mismo síndrome 1. Este ejemplo muestra que la decodificación por síndrome puede servir tanto para **detección** como para **corrección**, dependiendo de la distancia mínima del código y de la riqueza de la tabla síndrome-líder de coset.

---

## 4.2.10 Códigos cíclicos: definición, polinomio generador, codificación y decodificación

Un código lineal binario de longitud $n$ es **cíclico** si, cada vez que una palabra-código
$$
(c_0,c_1,\dots,c_{n-1})
$$
pertenece al código, también pertenece el corrimiento cíclico
$$
(c_{n-1},c_0,c_1,\dots,c_{n-2}).
$$

### Representación polinomial
La palabra
$$
\mathbf{c}=(c_0,c_1,\dots,c_{n-1})
$$
se asocia al polinomio
$$
c(x)=c_0+c_1x+\cdots+c_{n-1}x^{n-1}.
$$

Las operaciones se realizan módulo 2 y módulo $x^n+1$ (equivalentemente $x^n-1$ en binario).

### Polinomio generador
Todo código cíclico puede describirse mediante un polinomio generador $g(x)$ de grado $n-k$ tal que
$$
g(x) \mid (x^n+1).
$$

Las palabras-código son todos los múltiplos de $g(x)$:
$$
c(x)=m(x)g(x),
$$
donde $m(x)$ es el polinomio del mensaje de grado menor que $k$.

### Codificación sistemática
Para un mensaje $m(x)$, se forma
$$
x^{n-k}m(x),
$$
se divide entre $g(x)$,
$$
x^{n-k}m(x)=q(x)g(x)+p(x),
$$
y se construye la palabra-código sistemática
$$
c(x)=x^{n-k}m(x)+p(x).
$$
Como en binario suma y resta son iguales, $p(x)$ se agrega módulo 2.

### Ejemplo 4.16: Codificación cíclica

Sea un código cíclico $(7,4)$ con
$$
g(x)=x^3+x+1.
$$
Tomemos el mensaje
$$
m(x)=x^3+x^2+1,
$$
correspondiente a 1101 según la convención adecuada de coeficientes.

Primero multiplicamos por $x^{n-k}=x^3$:
$$
x^3m(x)=x^6+x^5+x^3.
$$

Ahora dividimos $x^6+x^5+x^3$ entre $g(x)=x^3+x+1$.

1. Primer término:
$$
\frac{x^6}{x^3}=x^3.
$$
Multiplicamos:
$$
x^3g(x)=x^6+x^4+x^3.
$$
Restando módulo 2:
$$
(x^6+x^5+x^3)+(x^6+x^4+x^3)=x^5+x^4.
$$

2. Siguiente término:
$$
\frac{x^5}{x^3}=x^2.
$$
Multiplicamos:
$$
x^2g(x)=x^5+x^3+x^2.
$$
Restando:
$$
(x^5+x^4)+(x^5+x^3+x^2)=x^4+x^3+x^2.
$$

3. Siguiente término:
$$
\frac{x^4}{x^3}=x.
$$
Multiplicamos:
$$
xg(x)=x^4+x^2+x.
$$
Restando:
$$
(x^4+x^3+x^2)+(x^4+x^2+x)=x^3+x.
$$

4. Siguiente término:
$$
\frac{x^3}{x^3}=1.
$$
Multiplicamos:
$$
g(x)=x^3+x+1.
$$
Restando:
$$
(x^3+x)+(x^3+x+1)=1.
$$

El residuo es
$$
p(x)=1.
$$

Por tanto, la palabra-código sistemática es
$$
c(x)=x^6+x^5+x^3+1.
$$

En bits, esto corresponde a
$$
1101001.
$$

### Decodificación cíclica
La recepción se modela como
$$
r(x)=c(x)+e(x).
$$
El síndrome polinomial puede obtenerse calculando el residuo de dividir $r(x)$ entre $g(x)$. Si el residuo es cero, no se detecta error.

### Ejemplo 4.17: Detección de error en código cíclico

Si se recibe
$$
r(x)=c(x)+x^2,
$$
entonces como $c(x)$ es múltiplo de $g(x)$,
$$
r(x) \bmod g(x) = x^2 \bmod g(x).
$$
Como $x^2$ tiene grado menor que $g(x)$, el residuo es $x^2\ne 0$, por lo que el error se detecta.

---

## 4.2.11 Códigos de paridad

El código de verificación de paridad simple añade un bit de paridad a $k$ bits de información para forzar que el número total de unos sea par (o impar).

Para paridad par, el bit de paridad es
$$
p=u_1\oplus u_2\oplus \cdots \oplus u_k.
$$

El código resultante es $(k+1,k)$.

Su distancia mínima es
$$
d_{\min}=2.
$$

Por tanto, puede detectar un error, pero no corregirlo.

### Ejemplo 4.18: Código de paridad simple

Sea el mensaje
$$
\mathbf{u}=1011.
$$
La suma módulo 2 es
$$
1\oplus 0\oplus 1\oplus 1 = 1.
$$
Entonces el bit de paridad para paridad par es
$$
p=1,
$$
porque así el número total de unos será 4, que es par.

La palabra-código es
$$
\mathbf{c}=10111.
$$

Si se recibe $10110$, el número de unos es 3, impar, luego se detecta error.

[Figura 4.7]: La figura debe mostrar un bloque de datos de $k$ bits entrando a un circuito XOR en cascada que genera el bit de paridad, el cual se añade al final del bloque. En el receptor, otro bloque calcula de nuevo la paridad y la compara. Pedagógicamente, esta figura ayuda a conectar la definición algebraica con una implementación digital concreta muy simple.

---

## 4.2.12 Código Hamming: construcción, propiedades, ejemplo completo

Los códigos de Hamming binarios son una familia de códigos lineales perfectos con parámetros
$$
(n,k)=\left(2^m-1,\;2^m-m-1\right), \qquad m\ge 2.
$$

Su distancia mínima es
$$
d_{\min}=3,
$$
por lo que corrigen un error y detectan hasta dos.

### Construcción de $H$
La matriz $H$ de un código Hamming se forma colocando como columnas todas las combinaciones binarias no nulas de longitud $m$.

Para $m=3$, se obtiene el código Hamming $(7,4)$. Una posible matriz es
$$
H=
\begin{bmatrix}
1 & 0 & 1 & 0 & 1 & 0 & 1\\
0 & 1 & 1 & 0 & 0 & 1 & 1\\
0 & 0 & 0 & 1 & 1 & 1 & 1
\end{bmatrix}.
$$

Cada columna es la representación binaria de un índice de posición.

### Forma sistemática
Reordenando columnas, puede obtenerse una forma sistemática compatible con
$$
G=[I_4\;P].
$$

### Propiedad de corrección
Si ocurre un error en la posición $i$, el síndrome es igual a la columna $i$ de $H$. Por ello, el receptor puede identificar directamente la posición errónea.

### Ejemplo 4.19: Construcción completa del Hamming $(7,4)$

Tomemos la forma sistemática
$$
G=
\begin{bmatrix}
1 & 0 & 0 & 0 & 1 & 1 & 0\\
0 & 1 & 0 & 0 & 1 & 0 & 1\\
0 & 0 & 1 & 0 & 0 & 1 & 1\\
0 & 0 & 0 & 1 & 1 & 1 & 1
\end{bmatrix}.
$$

Entonces
$$
P=
\begin{bmatrix}
1&1&0\\
1&0&1\\
0&1&1\\
1&1&1
\end{bmatrix},
$$
y por tanto
$$
H=
\begin{bmatrix}
1&1&0&1&1&0&0\\
1&0&1&1&0&1&0\\
0&1&1&1&0&0&1
\end{bmatrix}.
$$

#### Codificación
Sea el mensaje
$$
\mathbf{u}=1011.
$$
Entonces
$$
\mathbf{c}=\mathbf{u}G.
$$

Calculamos:
$$
\mathbf{c}=[1\;0\;1\;1]
\begin{bmatrix}
1 & 0 & 0 & 0 & 1 & 1 & 0\\
0 & 1 & 0 & 0 & 1 & 0 & 1\\
0 & 0 & 1 & 0 & 0 & 1 & 1\\
0 & 0 & 0 & 1 & 1 & 1 & 1
\end{bmatrix}.
$$

Sumamos las filas 1, 3 y 4:
$$
[1\;0\;0\;0\;1\;1\;0]
\oplus
[0\;0\;1\;0\;0\;1\;1]
\oplus
[0\;0\;0\;1\;1\;1\;1]
=
[1\;0\;1\;1\;0\;1\;0].
$$

Así,
$$
\mathbf{c}=1011010.
$$

#### Transmisión con error
Supóngase un error en la posición 6:
$$
\mathbf{e}=0000010.
$$
Entonces se recibe
$$
\mathbf{r}=\mathbf{c}+\mathbf{e}=1011000.
$$

#### Síndrome
Calculamos
$$
\mathbf{s}=\mathbf{r}H^T.
$$
Como $\mathbf{r}=\mathbf{c}+\mathbf{e}$,
$$
\mathbf{s}=\mathbf{e}H^T.
$$
Como el error está en la posición 6, el síndrome es la columna 6 de $H$:
$$
\mathbf{s}=\begin{bmatrix}0\\1\\0\end{bmatrix}.
$$

Esto identifica la posición 6. Corrigiendo:
$$
\hat{\mathbf{c}}=\mathbf{r}+0000010 = 1011010.
$$
Se recupera el código correcto y, por ser sistemático, los primeros 4 bits dan el mensaje:
$$
\hat{\mathbf{u}}=1011.
$$

[Figura 4.8]: La figura debe representar el funcionamiento del código Hamming $(7,4)$: cuatro bits de información, tres bits de paridad, transmisión por canal, un error en una posición y cálculo del síndrome en el receptor. Conviene mostrar una tabla donde cada síndrome se asocia con una posición concreta del bit erróneo. Esta figura es especialmente útil para visualizar por qué un único error queda identificado de manera unívoca.

---

## 4.2.13 Ejemplos adicionales integradores

### Ejemplo 4.20: Relación entre distancia mínima y detección/corrección

Supóngase un código lineal con palabras no nulas de pesos
$$
3,4,5,6.
$$
Entonces
$$
d_{\min}=3.
$$
Por tanto:
- Detecta hasta 2 errores.
- Corrige 1 error.

Si se producen exactamente 2 errores, el código puede advertir la anomalía, pero no necesariamente corregirla.

### Ejemplo 4.21: Síndrome como firma del error

Sea un código con matriz $H$ de columnas distintas y no nulas. Si ocurre un único error en la posición $i$, entonces el vector error es $\mathbf{e}_i$, y
$$
\mathbf{s}=\mathbf{e}_iH^T
$$
es la columna $i$ de $H$. Esto explica por qué los códigos Hamming, cuyas columnas cubren todas las combinaciones binarias no nulas, pueden corregir un error en cualquiera de las $n$ posiciones.

---

# 4.3 Codificación Convolucional

## 4.3.1 Estructura del codificador convolucional: registros de desplazamiento, longitud de restricción, tasa

A diferencia de los códigos de bloque, los **códigos convolucionales** introducen redundancia de forma secuencial y con memoria. La salida en cada instante depende del bit de entrada actual y de un número finito de bits anteriores almacenados en registros de desplazamiento.

Un codificador convolucional se caracteriza por:
- el número de bits de entrada por unidad de tiempo, $k$;
- el número de bits de salida por unidad de tiempo, $n$;
- la tasa de código
$$
R=\frac{k}{n};
$$
- la **longitud de restricción** $K$, relacionada con la memoria del codificador.

Si hay $m$ elementos de memoria, usualmente
$$
K=m+1.
$$

En un codificador binario de tasa $1/2$, por cada bit de entrada se generan dos bits de salida mediante dos sumadores módulo 2 conectados a determinadas etapas del registro.

[Figura 4.9]: La figura debe mostrar un codificador convolucional de tasa $1/2$ con tres etapas (una actual y dos de memoria), incluyendo registros de desplazamiento, conexiones hacia dos sumadores XOR y flechas que indiquen el avance temporal de los bits. La descripción debe remarcar que la salida no depende solo del bit presente sino también del “historial” reciente, lo que introduce memoria y permite distribuir la redundancia a lo largo del tiempo.

### Ejemplo 4.22: Parámetros de un codificador

Considérese un codificador con una entrada, dos salidas y dos memorias. Entonces:
- $k=1$
- $n=2$
- $R=1/2$
- $m=2$
- $K=m+1=3$

El número de estados del codificador es
$$
2^m=4.
$$

---

## 4.3.2 Representación polinomial de generadores

Las conexiones del codificador se describen mediante polinomios generadores. Si el bit actual corresponde al coeficiente de $D^0$ y cada retardo equivale a una potencia adicional de $D$, un generador puede escribirse como
$$
g(D)=g_0 + g_1D + g_2D^2 + \cdots + g_mD^m,
$$
con $g_i\in\{0,1\}$.

Por ejemplo, para un codificador tasa $1/2$ con dos generadores
$$
g^{(1)}(D)=1+D+D^2,
$$
$$
g^{(2)}(D)=1+D^2,
$$
se suele escribir en octal como $(7,5)$, pues
$$
111_2=7_8, \qquad 101_2=5_8.
$$

La salida correspondiente al instante $i$ se obtiene convolucionando la secuencia de entrada con cada generador, módulo 2.

### Ejemplo 4.23: Interpretación de generadores

Si el estado del registro es $[u_i,u_{i-1},u_{i-2}]$, entonces con generadores $(7,5)$:
$$
v_i^{(1)} = u_i \oplus u_{i-1} \oplus u_{i-2},
$$
$$
v_i^{(2)} = u_i \oplus u_{i-2}.
$$

Cada bit de salida es una combinación lineal módulo 2 del contenido del registro.

---

## 4.3.3 Diagrama de estados: construcción y análisis

El **estado** de un codificador convolucional en un instante viene dado por el contenido de sus elementos de memoria. Para $m$ memorias hay
$$
2^m
$$
estados posibles.

En el ejemplo de $m=2$, los estados son
$$
00,01,10,11.
$$

Cada transición de estado depende del bit de entrada actual. Además, cada transición produce una salida etiquetada.

### Construcción
1. Se enumeran todos los estados.
2. Para cada estado, se considera entrada 0 y entrada 1.
3. Se calcula el siguiente estado desplazando el registro.
4. Se calcula la salida asociada usando los generadores.

### Ejemplo 4.24: Diagrama de estados para el código $(7,5)$

Supóngase estado actual $10$, interpretado como $u_{i-1}=1$, $u_{i-2}=0$.

- Si entra $u_i=0$:
  - nuevo estado: $01$
  - salida:
  $$
  v_i^{(1)}=0\oplus 1\oplus 0 =1,
  $$
  $$
  v_i^{(2)}=0\oplus 0 =0.
  $$
  Etiqueta: $0/10$.

- Si entra $u_i=1$:
  - nuevo estado: $11$
  - salida:
  $$
  v_i^{(1)}=1\oplus 1\oplus 0 =0,
  $$
  $$
  v_i^{(2)}=1\oplus 0 =1.
  $$
  Etiqueta: $1/01$.

Repitiendo el proceso para todos los estados se obtiene el diagrama completo.

[Figura 4.10]: La figura debe mostrar el diagrama de estados del codificador convolucional $(7,5)$ con cuatro estados. Desde cada estado deben salir dos ramas: una para entrada 0 y otra para entrada 1, ambas etiquetadas con el formato entrada/salida. La explicación debe enfatizar que el diagrama resume la dinámica del codificador completo y sirve como base para la construcción del trellis y la decodificación Viterbi.

---

## 4.3.4 Diagrama de trellis: construcción paso a paso

El **trellis** es una expansión temporal del diagrama de estados. Cada columna representa un instante de tiempo, y cada nodo un estado posible en ese instante.

### Procedimiento de construcción
1. Se dibujan columnas temporales $t=0,1,2,\dots$.
2. En cada columna se colocan todos los estados.
3. Se conectan los estados entre columnas consecutivas según las transiciones del diagrama de estados.
4. Cada rama se etiqueta con la salida correspondiente.

El trellis es esencial para algoritmos de decodificación óptima, especialmente Viterbi.

### Ejemplo 4.25: Construcción inicial de un trellis

Para el código $(7,5)$ y estado inicial $00$:
- En $t=0$ solo es posible el estado $00$.
- Desde $00$, con entrada 0 se permanece en $00$ y la salida es $00$.
- Desde $00$, con entrada 1 se pasa a $10$ y la salida es $11$.

En el siguiente instante, desde cada nuevo estado vuelven a surgir dos ramas. Así, el número de trayectorias posibles crece exponencialmente con el tiempo, pero Viterbi evita explorarlas de forma ingenua.

[Figura 4.11]: La figura debe representar varias etapas de un trellis, empezando en un estado inicial conocido y mostrando cómo las trayectorias se bifurcan a lo largo del tiempo. Una buena descripción debe subrayar que el trellis convierte el problema de decodificación en un problema de búsqueda de camino óptimo en un grafo acíclico orientado en el tiempo.

---

## 4.3.5 Codificación: ejemplo completo

Considérese el codificador de tasa $1/2$, longitud de restricción $K=3$, generadores $(7,5)$:
$$
g^{(1)}(D)=1+D+D^2,
$$
$$
g^{(2)}(D)=1+D^2.
$$

Supongamos la secuencia de entrada
$$
\mathbf{u}=1011.
$$

Para vaciar el registro, añadimos dos bits de cola 0:
$$
\mathbf{u}_{\text{ext}}=101100.
$$

Estado inicial: $00$.

### Instante 1: entrada 1
Registro: $[1,0,0]$
$$
v_1^{(1)}=1\oplus 0\oplus 0=1,
$$
$$
v_1^{(2)}=1\oplus 0=1.
$$
Salida: $11$
Nuevo estado: $10$

### Instante 2: entrada 0
Registro: $[0,1,0]$
$$
v_2^{(1)}=0\oplus 1\oplus 0=1,
$$
$$
v_2^{(2)}=0\oplus 0=0.
$$
Salida: $10$
Nuevo estado: $01$

### Instante 3: entrada 1
Registro: $[1,0,1]$
$$
v_3^{(1)}=1\oplus 0\oplus 1=0,
$$
$$
v_3^{(2)}=1\oplus 1=0.
$$
Salida: $00$
Nuevo estado: $10$

### Instante 4: entrada 1
Registro: $[1,1,0]$
$$
v_4^{(1)}=1\oplus 1\oplus 0=0,
$$
$$
v_4^{(2)}=1\oplus 0=1.
$$
Salida: $01$
Nuevo estado: $11$

### Instante 5: entrada 0
Registro: $[0,1,1]$
$$
v_5^{(1)}=0\oplus 1\oplus 1=0,
$$
$$
v_5^{(2)}=0\oplus 1=1.
$$
Salida: $01$
Nuevo estado: $01$

### Instante 6: entrada 0
Registro: $[0,0,1]$
$$
v_6^{(1)}=0\oplus 0\oplus 1=1,
$$
$$
v_6^{(2)}=0\oplus 1=1.
$$
Salida: $11$
Nuevo estado: $00$

La secuencia codificada es
$$
11\;10\;00\;01\;01\;11.
$$
Es decir,
$$
111000010111.
$$

### Ejemplo 4.26: Verificación mediante ecuaciones recursivas

El mismo resultado puede obtenerse aplicando las ecuaciones generadoras directamente sobre la secuencia extendida $101100$.

---

## 4.3.6 Algoritmo de Viterbi

### Descripción completa del algoritmo

El algoritmo de Viterbi realiza decodificación de máxima verosimilitud sobre el trellis. En lugar de evaluar todas las trayectorias posibles, conserva en cada estado y cada instante solo la trayectoria de menor métrica acumulada: la **trayectoria superviviente**.

### Idea central
Sea una secuencia recibida segmentada en símbolos de rama. Para cada transición del trellis se calcula una **métrica de rama**, y para cada camino una **métrica de camino** acumulada.

En cada nodo del trellis:
1. llegan usualmente dos caminos candidatos;
2. se suma la métrica de la rama a la métrica acumulada previa;
3. se selecciona el camino con menor métrica (o mayor correlación, según formulación);
4. el camino descartado se elimina.

Al final, se elige el camino superviviente de menor métrica total y se retrotraza para reconstruir la secuencia de entrada.

### Métricas de rama y de camino

#### Decisión dura
Si el receptor cuantiza cada salida recibida a bits 0/1, la métrica de rama es la distancia de Hamming entre la salida recibida y la salida ideal de la rama.

Si la rama esperada es $\mathbf{v}$ y la rama recibida cuantizada es $\mathbf{r}$,
$$
M_B = d_H(\mathbf{r},\mathbf{v}).
$$

La métrica de camino es la suma acumulada:
$$
M_P = \sum M_B.
$$

#### Decisión suave
Si el receptor conserva muestras analógicas, la métrica de rama adecuada en AWGN es la distancia euclidiana:
$$
M_B = \sum_{j}(r_j-v_j)^2.
$$

La decisión suave aprovecha más información y suele ofrecer una ganancia de aproximadamente 2 dB frente a la decisión dura.

[Figura 4.12]: La figura debe mostrar un fragmento de trellis con dos caminos convergiendo a un mismo estado. Cada rama debe estar etiquetada con su salida ideal y su métrica de rama, mientras que en el nodo se compara la suma acumulada de ambos candidatos para elegir el superviviente. La finalidad pedagógica es visualizar cómo el algoritmo realiza una poda sistemática sin perder optimalidad ML.

### Ejemplo 4.27: Viterbi con decisión dura paso a paso

Usaremos el mismo código $(7,5)$, estado inicial $00$, y suponemos que la secuencia transmitida corresponde a la entrada $101$ seguida de bits de cola $00$, es decir, $10100$.

Primero codificamos:
- entrada 1 desde $00$ $\to$ salida $11$, estado $10$
- entrada 0 desde $10$ $\to$ salida $10$, estado $01$
- entrada 1 desde $01$ $\to$ salida $00$, estado $10$
- entrada 0 desde $10$ $\to$ salida $10$, estado $01$
- entrada 0 desde $01$ $\to$ salida $11$, estado $00$

Secuencia ideal transmitida:
$$
11\;10\;00\;10\;11.
$$

Supóngase que el receptor observa, tras decisión dura,
$$
11\;10\;01\;10\;11.
$$
Solo hay un error en la tercera rama.

#### Etapa 0
Estado inicial conocido: $00$ con métrica 0. Los demás estados tienen métrica infinita.

#### Etapa 1, recibido 11
Desde $00$:
- rama entrada 0 produce $00$, métrica de rama
$$
d_H(11,00)=2.
$$
- rama entrada 1 produce $11$, métrica de rama
$$
d_H(11,11)=0.
$$

Se actualiza:
- estado $00$: métrica 2
- estado $10$: métrica 0

#### Etapa 2, recibido 10
Desde estado $00$ (métrica 2):
- con entrada 0: salida 00, métrica rama 1, total 3
- con entrada 1: salida 11, métrica rama 1, total 3

Desde estado $10$ (métrica 0):
- con entrada 0: salida 10, métrica rama 0, total 0
- con entrada 1: salida 01, métrica rama 2, total 2

Tras comparar supervivientes:
- estado $00$: min(3 desde 00) = 3
- estado $10$: min(3 desde 00) = 3
- estado $01$: 0 desde 10
- estado $11$: 2 desde 10

#### Etapa 3, recibido 01
Ahora se evalúan todas las transiciones desde los estados con métricas finitas. Tomemos las principales:

Desde $01$ (métrica 0):
- entrada 0 $\to$ estado $00$, salida 11
$$
d_H(01,11)=1 \Rightarrow \text{total}=1.
$$
- entrada 1 $\to$ estado $10$, salida 00
$$
d_H(01,00)=1 \Rightarrow \text{total}=1.
$$

Desde $11$ (métrica 2):
- entrada 0 $\to$ estado $01$, salida 01
$$
d_H(01,01)=0 \Rightarrow \text{total}=2.
$$
- entrada 1 $\to$ estado $11$, salida 10
$$
d_H(01,10)=2 \Rightarrow \text{total}=4.
$$

Desde $00$ y $10$ con métricas 3 se calculan también sus aportes, pero resultan peores. Tras seleccionar supervivientes, quedan las mejores métricas alrededor de 1 o 2, dominadas por la trayectoria correcta.

#### Etapas finales
Repitiendo el proceso, la trayectoria de menor métrica final coincide con la entrada original $10100$. Al eliminar los bits de cola se obtiene
$$
\hat{\mathbf{u}}=101.
$$

**Conclusión:** aunque una rama se recibió con error, la estructura global del trellis permitió recuperar correctamente la secuencia transmitida.

### Ejemplo 4.28: Comparación dura vs. suave

Supóngase que una rama ideal BPSK para salida binaria 10 es
$$
(+1,-1),
$$
y que se recibe analógicamente
$$
(0.2,-0.7).
$$

- Decisión dura: cuantizamos a $(+1,-1)$, luego la métrica de Hamming frente a 10 es 0.
- Frente a otra rama posible 11, cuya imagen BPSK es $(+1,+1)$, la decisión dura también daría distancia 1.

Pero con decisión suave:
$$
M_B(10)=(0.2-1)^2+(-0.7+1)^2=0.64+0.09=0.73,
$$
$$
M_B(11)=(0.2-1)^2+(-0.7-1)^2=0.64+2.89=3.53.
$$

La diferencia es mucho más informativa. Esto explica la ganancia de la decodificación suave.

---

## 4.3.7 Distancia libre y rendimiento de códigos convolucionales

La magnitud análoga a la distancia mínima en códigos de bloque es la **distancia libre** $d_{free}$.

Se define como la mínima distancia de Hamming entre dos trayectorias distintas del trellis que parten y vuelven al mismo estado (usualmente el estado cero), o equivalentemente, entre la secuencia nula y cualquier otra secuencia codificada no nula de longitud finita.

Formalmente,
$$
d_{free}=\min_{\mathbf{v}\ne \mathbf{0}} w_H(\mathbf{v}),
$$
donde $\mathbf{v}$ recorre todas las secuencias de salida no nulas producidas por secuencias de entrada no nulas que parten y terminan en el estado cero.

Cuanto mayor sea $d_{free}$, mejor el rendimiento asintótico del código frente a ruido.

Para el conocido código convolucional de tasa $1/2$ y generadores $(7,5)$,
$$
d_{free}=5.
$$

### Relación cualitativa con el error
En regímenes de alta SNR, la probabilidad de error de bit decae aproximadamente de forma dominada por eventos a distancia libre, de manera análoga a cómo la distancia mínima domina en códigos de bloque.

### Ejemplo 4.29: Interpretación de $d_{free}$

Si un código A tiene
$$
d_{free}=5,
$$
y un código B tiene
$$
d_{free}=7,
$$
entonces, en general, B ofrecerá mejor capacidad de corrección asintótica, aunque podría requerir mayor complejidad de decodificación si su longitud de restricción es mayor.

[Figura 4.13]: La figura debe mostrar dos trayectorias en el trellis que coinciden al inicio y al final, pero divergen en una sección intermedia. La distancia libre debe interpretarse como el número mínimo de símbolos de salida diferentes entre trayectorias competidoras. Esta representación ayuda a entender por qué el trellis es la estructura natural para analizar el rendimiento de códigos con memoria.

---

## 4.3.8 Ejemplos resueltos adicionales

### Ejemplo 4.30: Número de estados y complejidad

Para un codificador convolucional con memoria $m=4$:
$$
\text{número de estados}=2^4=16.
$$

Si se usa Viterbi, en cada etapa deben actualizarse 16 métricas de estado. Esto ilustra el compromiso entre rendimiento y complejidad: aumentar la memoria suele mejorar la protección, pero incrementa exponencialmente la complejidad del decodificador.

### Ejemplo 4.31: Tasa efectiva con bits de cola

Si una secuencia de información tiene longitud $L=100$ bits y se usa un codificador de tasa nominal $1/2$ con memoria $m=2$, deben añadirse 2 bits de cola. Entonces se transmiten
$$
2(L+m)=2(102)=204
$$
bits codificados.

La tasa efectiva es
$$
R_{\text{ef}}=\frac{100}{204}\approx 0.4902,
$$
ligeramente menor que la tasa nominal $1/2$.

### Ejemplo 4.32: Métrica de rama euclidiana en BPSK

Sea una rama esperada correspondiente a salida binaria 01, que bajo BPSK se mapea como
$$
(-1,+1)
$$
según la convención $0\mapsto -1$, $1\mapsto +1$.

Si se recibe
$$
(-0.6,0.1),
$$
la métrica euclidiana es
$$
M_B = (-0.6+1)^2 + (0.1-1)^2 = 0.16+0.81=0.97.
$$

Si otra rama competidora fuera 11, es decir $(+1,+1)$,
$$
M_B = (-0.6-1)^2 + (0.1-1)^2 = 2.56+0.81=3.37.
$$

La rama 01 es claramente más verosímil.

---

# Resumen de conceptos clave

En esta unidad se han establecido los fundamentos geométricos y algebraicos de la codificación de canal.

1. En **espacio de señal**, las señales pueden representarse como vectores en una base ortonormal, obtenida si es necesario mediante **Gram-Schmidt**. La detección óptima en AWGN se interpreta como una regla de mínima distancia euclidiana. La separación geométrica entre señales determina directamente la probabilidad de error.

2. En **codificación de bloques**, un código $(n,k)$ añade redundancia controlada con tasa
$$
R=\frac{k}{n}.
$$
La magnitud clave es la **distancia mínima** $d_{\min}$, que fija la capacidad de detección y corrección:
$$
\text{detección} = d_{\min}-1,
$$
$$
\text{corrección} = \left\lfloor \frac{d_{\min}-1}{2} \right\rfloor.
$$
Los códigos lineales se describen mediante la **matriz generadora** $G$ y la **matriz de chequeo** $H$, y su decodificación puede realizarse elegantemente mediante el **síndrome**. También se estudiaron códigos cíclicos, códigos de paridad y el importante **código Hamming**, ejemplo clásico de corrección de un error.

3. En **codificación convolucional**, la redundancia se reparte en el tiempo usando memoria y registros de desplazamiento. La descripción mediante generadores polinomiales, diagramas de estados y trellis conduce naturalmente al **algoritmo de Viterbi**, que realiza decodificación de máxima verosimilitud con complejidad manejable. La magnitud de diseño más importante es la **distancia libre** $d_{free}$.

En conjunto, la codificación de canal es el mecanismo que permite acercar el rendimiento de un sistema real a la transmisión confiable en presencia de ruido. Su estudio constituye la base conceptual para técnicas más avanzadas como códigos Reed–Solomon, BCH, turbo códigos, LDPC y codificación polar.

---

# Referencias

1. S. Lin and D. J. Costello, Jr., *Error Control Coding*, 2nd ed., Upper Saddle River, NJ, USA: Pearson Prentice Hall, 2004. ISBN conocido; libro de referencia clásica sobre códigos de bloque, cíclicos, BCH, Reed–Solomon y convolucionales.
2. J. G. Proakis and M. Salehi, *Digital Communications*, 5th ed., New York, NY, USA: McGraw-Hill, 2008. ISBN conocido; texto de referencia sobre espacio de señal, detección óptima y codificación.
3. B. Sklar, *Digital Communications: Fundamentals and Applications*, 2nd ed., Upper Saddle River, NJ, USA: Prentice Hall, 2001. ISBN conocido; texto ampliamente usado en introducción y aplicaciones.
4. S. Haykin, *Communication Systems*, 4th ed., New York, NY, USA: Wiley, 2001. ISBN conocido; referencia clásica para fundamentos de señales y detección.
5. A. J. Viterbi, “Error bounds for convolutional codes and an asymptotically optimum decoding algorithm,” *IEEE Transactions on Information Theory*, vol. 13, no. 2, pp. 260–269, Apr. 1967, doi: 10.1109/TIT.1967.1054010.
6. C. E. Shannon, “A mathematical theory of communication,” *Bell System Technical Journal*, vol. 27, no. 3, pp. 379–423, Jul. 1948, doi: 10.1002/j.1538-7305.1948.tb01338.x.
7. R. W. Hamming, “Error detecting and error correcting codes,” *Bell System Technical Journal*, vol. 29, no. 2, pp. 147–160, Apr. 1950, doi: 10.1002/j.1538-7305.1950.tb00463.x.
