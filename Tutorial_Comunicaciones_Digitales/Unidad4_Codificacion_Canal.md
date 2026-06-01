# Unidad 4: Codificación de Canal

## Introducción de la unidad

La **codificación de canal** añade redundancia estructurada a la información para combatir los errores introducidos por ruido térmico, interferencia, desvanecimiento, distorsión no lineal y pérdidas del medio físico. A diferencia de la codificación de fuente, que busca eliminar redundancia, la codificación de canal la **introduce deliberadamente** para aumentar la confiabilidad.

Desde el punto de vista geométrico, codificar equivale a separar más las señales o las palabras-código válidas dentro de un espacio de decisión. Desde el punto de vista algebraico, equivale a restringir la transmisión a subconjuntos con estructura matemática controlada. Desde el punto de vista probabilístico, equivale a reducir la probabilidad de error a costa de transmitir más símbolos por bit de información.

En esta unidad se desarrollan cuatro bloques complementarios:

- **4.1 Espacio de señal y espacios vectoriales**, base geométrica de la detección óptima.
- **4.2 Teoría de campos de Galois y construcción de códigos**, fundamento algebraico de los códigos modernos.
- **4.3 Codificación de bloques**, incluyendo códigos lineales, cíclicos, Hamming, BCH, Reed-Solomon, LDPC y polares.
- **4.4 Codificación convolucional**, incluyendo variantes sistemáticas, no sistemáticas, RSC, códigos punzados y turbo.

La meta pedagógica es enlazar la intuición física del canal con la formalización matemática de la codificación. En particular, se mostrará que conceptos como distancia de Hamming, síndrome, raíces consecutivas, polinomio generador, trellis o distancia libre no son piezas aisladas, sino manifestaciones de una misma idea: **imponer estructura para hacer inferencia confiable**.

> **Concepto clave:** un buen código de canal no “elimina” el ruido; lo hace **observable y corregible** mediante relaciones algebraicas o temporales entre símbolos transmitidos.

---

# 4.1 Espacio de Señal y Espacios Vectoriales

## 4.1.1 Representación vectorial de señales

En comunicaciones digitales, una señal transmitida durante el intervalo $0 \le t \le T$ puede modelarse como un elemento de un espacio funcional. Cuando el conjunto relevante de señales tiene dimensión finita, es posible trabajar con una base ortonormal y representar cada señal por un vector de coordenadas.

Sea
$$
\mathcal{S} = \{s_1(t), s_2(t), \dots, s_M(t)\}, \qquad 0 \le t \le T.
$$

Si existen $N$ funciones ortonormales $\{\phi_1(t),\phi_2(t),\dots,\phi_N(t)\}$ tales que
$$
s_m(t)=\sum_{i=1}^{N} s_{mi}\,\phi_i(t),
$$
entonces la señal queda representada por el vector
$$
\mathbf{s}_m=[s_{m1},s_{m2},\dots,s_{mN}]^T.
$$

Los coeficientes se obtienen por proyección:
$$
s_{mi}=\langle s_m,\phi_i\rangle = \int_0^T s_m(t)\phi_i(t)\,dt.
$$

El producto interno entre dos señales se define como
$$
\langle x,y\rangle = \int_0^T x(t)y(t)\,dt,
$$
y la energía de la señal es
$$
E_s = \int_0^T |s_m(t)|^2dt = \sum_{i=1}^{N}s_{mi}^2 = \|\mathbf{s}_m\|^2.
$$

Esta formulación convierte un problema analógico continuo en uno geométrico discreto sobre $\mathbb{R}^N$.

> **Concepto clave:** al pasar del dominio temporal al vectorial, la detección óptima se reformula como un problema de distancias, ángulos y proyecciones.

**[Figura 4.1]:** representación conceptual de varias formas de onda temporales proyectadas sobre una base ortonormal de dos o tres dimensiones. A la izquierda deben verse señales $s_1(t),s_2(t),s_3(t)$ en el tiempo; a la derecha, sus vectores asociados en el plano o en el espacio. La figura debe enfatizar que las diferencias temporales entre señales se convierten en separación geométrica entre puntos.

**Ejemplo 4.1:** representación vectorial en una base dada.

Sea
$$
s(t)=3\phi_1(t)-2\phi_2(t).
$$
Entonces
$$
\mathbf{s}=[3,-2]^T.
$$
Si otra señal es
$$
r(t)=2\phi_1(t)+\phi_2(t),
$$
entonces
$$
\mathbf{r}=[2,1]^T.
$$
La energía de $s(t)$ es
$$
E_s=3^2+(-2)^2=13.
$$
La energía de $r(t)$ es
$$
E_r=2^2+1^2=5.
$$
El producto interno resulta
$$
\langle s,r\rangle = 3\cdot 2 + (-2)\cdot 1 = 4.
$$
Por tanto,
$$
\cos\theta = \frac{\langle s,r\rangle}{\|\mathbf{s}\|\,\|\mathbf{r}\|} = \frac{4}{\sqrt{13}\sqrt{5}}.
$$
El ejemplo muestra que la correlación entre señales se traduce directamente en el ángulo entre vectores.

## 4.1.2 Base ortonormal: procedimiento de Gram-Schmidt

En la práctica, las funciones disponibles no siempre son ortogonales. El procedimiento de Gram-Schmidt permite construir una base ortonormal equivalente sin perder información.

Dado un conjunto linealmente independiente $\{g_1(t),g_2(t),\dots,g_N(t)\}$, se define:

$$
\phi_1(t)=\frac{g_1(t)}{\|g_1\|},
$$
$$
\nu_2(t)=g_2(t)-\langle g_2,\phi_1\rangle\phi_1(t),
$$
$$
\phi_2(t)=\frac{\nu_2(t)}{\|\nu_2\|},
$$

y, en general,
$$
\nu_k(t)=g_k(t)-\sum_{i=1}^{k-1}\langle g_k,\phi_i\rangle\phi_i(t),
$$
$$
\phi_k(t)=\frac{\nu_k(t)}{\|\nu_k\|}.
$$

Las funciones construidas satisfacen
$$
\langle \phi_i,\phi_j\rangle =
\begin{cases}
1, & i=j,\\
0, & i\neq j.
\end{cases}
$$

> **Concepto clave:** Gram-Schmidt no altera el subespacio útil de señales; únicamente lo expresa en coordenadas ortogonales, lo que simplifica análisis, implementación de receptores y cálculo de distancia.

**[Figura 4.2]:** visualización geométrica del procedimiento de Gram-Schmidt. Debe mostrarse primero $g_1$ y su versión normalizada $\phi_1$, y después el vector $g_2$ descompuesto en una proyección sobre $\phi_1$ y una componente ortogonal $\nu_2$ que, al normalizarse, produce $\phi_2$. El mensaje central es que la ortogonalización consiste en “restar dependencia angular”.

**Ejemplo 4.2:** Gram-Schmidt con dos señales en $[0,1]$.

Sea
$$
g_1(t)=1, \qquad g_2(t)=t.
$$
Entonces
$$
\|g_1\|=\sqrt{\int_0^1 1\,dt}=1,
$$
por lo que
$$
\phi_1(t)=1.
$$
La proyección de $g_2$ sobre $\phi_1$ vale
$$
\langle g_2,\phi_1\rangle = \int_0^1 t\,dt = \frac{1}{2}.
$$
Por tanto,
$$
\nu_2(t)=t-\frac{1}{2}.
$$
La norma de $\nu_2$ es
$$
\|\nu_2\|=\sqrt{\int_0^1\left(t-\frac{1}{2}\right)^2dt} = \sqrt{\frac{1}{12}} = \frac{1}{2\sqrt{3}}.
$$
Finalmente,
$$
\phi_2(t)=\frac{t-1/2}{1/(2\sqrt{3})}=2\sqrt{3}\left(t-\frac{1}{2}\right).
$$
Se verifica que
$$
\langle \phi_1,\phi_2\rangle = 0,
$$
y que ambas funciones tienen norma unitaria.

## 4.1.3 Geometría de las señales de comunicación

En un canal AWGN, la señal recibida puede escribirse como
$$
r(t)=s_m(t)+n(t),
$$
o, en forma vectorial,
$$
\mathbf{r}=\mathbf{s}_m+\mathbf{n},
$$
donde $\mathbf{n}$ es un vector gaussiano con componentes independientes de media cero y varianza $N_0/2$ sobre cada dimensión ortonormal.

La detección de máxima verosimilitud se formula como
$$
\hat{\mathbf{s}} = \arg\min_{\mathbf{s}_i\in\mathcal{S}} \|\mathbf{r}-\mathbf{s}_i\|^2.
$$

Si las señales son equiprobables, la regla óptima es escoger la señal más cercana en distancia euclidiana. Esto induce regiones de Voronoi: cada punto del espacio queda asignado a la señal más próxima.

La correlación entre señales también es central:
$$
\langle s_i,s_j\rangle = \sum_{k=1}^{N}s_{ik}s_{jk}.
$$
Si dos señales son ortogonales, entonces
$$
\langle s_i,s_j\rangle = 0,
$$
lo que favorece la separación geométrica.

> **Concepto clave:** en AWGN, la probabilidad de error decrece cuando las señales válidas están más separadas en el espacio euclidiano; por eso la codificación busca incrementar distancias efectivas.

**[Figura 4.3]:** plano de señales con fronteras de decisión entre varios puntos. Debe ilustrarse una realización del ruido que no cruza la frontera y otra que sí lo hace. La figura debe conectar de manera visual la geometría de Voronoi con la ocurrencia de errores de detección.

**Ejemplo 4.3:** señales antipodales.

Sea
$$
s_1(t)=+\sqrt{E_b}\,\phi(t), \qquad s_2(t)=-\sqrt{E_b}\,\phi(t), \qquad \|\phi\|=1.
$$
Entonces
$$
\mathbf{s}_1=[\sqrt{E_b}], \qquad \mathbf{s}_2=[-\sqrt{E_b}].
$$
La distancia euclidiana entre ambas señales es
$$
d_E = \|\mathbf{s}_1-\mathbf{s}_2\| = 2\sqrt{E_b}.
$$
La frontera de decisión se ubica en el origen. Si se transmite $s_1$ y el ruido desplaza la observación a la región negativa, el receptor decide erróneamente $s_2$.

## 4.1.4 Distancia euclidiana y probabilidad de error

La distancia euclidiana entre dos señales $s_i(t)$ y $s_j(t)$ es
$$
d_{ij}=\left(\int_0^T |s_i(t)-s_j(t)|^2dt\right)^{1/2} = \|\mathbf{s}_i-\mathbf{s}_j\|.
$$

Para señales binarias equiprobables en AWGN,
$$
P_e = Q\left(\frac{d_{12}}{\sqrt{2N_0}}\right),
$$
donde
$$
Q(x)=\frac{1}{\sqrt{2\pi}}\int_x^{\infty}e^{-u^2/2}\,du.
$$

En particular, para señalización antipodal binaria coherente,
$$
P_b = Q\left(\sqrt{\frac{2E_b}{N_0}}\right),
$$
y para señalización ortogonal binaria coherente,
$$
P_b = Q\left(\sqrt{\frac{E_b}{N_0}}\right).
$$

La diferencia aparece porque la distancia entre señales ortogonales es menor que la distancia entre señales antipodales de la misma energía.

> **Concepto clave:** la distancia mínima relevante para el desempeño no es únicamente la energía, sino cómo esa energía se distribuye geométricamente entre palabras o trayectorias candidatas.

**Ejemplo 4.4:** probabilidad de error a partir de la distancia.

Si dos señales binarias tienen separación euclidiana
$$
d_{12}=4,
$$
y el canal tiene
$$
N_0=2,
$$
entonces
$$
P_e = Q\left(\frac{4}{\sqrt{4}}\right)=Q(2)\approx 2.28\times 10^{-2}.
$$
Si la distancia se duplica a $8$, entonces
$$
P_e = Q\left(\frac{8}{2}\right)=Q(4)\approx 3.17\times 10^{-5}.
$$
El descenso es drástico, lo que anticipa por qué la codificación de canal es tan poderosa.

## 4.1.5 Ejemplos resueltos integradores

**Ejemplo 4.5:** expansión de señales y distancia entre ellas.

Sean
$$
s_1(t)=2\phi_1(t)+\phi_2(t), \qquad s_2(t)=\phi_1(t)-2\phi_2(t),
$$
con $\phi_1$ y $\phi_2$ ortonormales. Entonces
$$
\mathbf{s}_1=[2,1]^T, \qquad \mathbf{s}_2=[1,-2]^T.
$$
La diferencia es
$$
\mathbf{s}_1-\mathbf{s}_2=[1,3]^T,
$$
y la distancia euclidiana vale
$$
d_{12}=\sqrt{1^2+3^2}=\sqrt{10}.
$$
El producto interno es
$$
\langle s_1,s_2\rangle = 2\cdot 1 + 1\cdot (-2)=0,
$$
por lo que las señales son ortogonales, aunque no tengan la misma energía.

**Ejemplo 4.6:** construcción de un receptor correlador.

Si el conjunto de señales usa la base ortonormal $\{\phi_1,\phi_2\}$, el receptor suficiente calcula
$$
y_1 = \int_0^T r(t)\phi_1(t)dt, \qquad y_2 = \int_0^T r(t)\phi_2(t)dt.
$$
Supóngase que se recibe el vector
$$
\mathbf{y}=[1.9,0.8]^T,
$$
y que las hipótesis posibles son $\mathbf{s}_1=[2,1]^T$ y $\mathbf{s}_2=[1,-2]^T$. Entonces
$$
\|\mathbf{y}-\mathbf{s}_1\|^2=(1.9-2)^2+(0.8-1)^2=0.01+0.04=0.05,
$$
$$
\|\mathbf{y}-\mathbf{s}_2\|^2=(1.9-1)^2+(0.8+2)^2=0.81+7.84=8.65.
$$
Por consiguiente, el detector decide $\mathbf{s}_1$.

---

# 4.2 Teoría de Campos de Galois y Construcción de Códigos

La teoría algebraica de códigos modernos descansa sobre estructuras finitas en las que suma y multiplicación están perfectamente controladas. Los polinomios generadores de los códigos cíclicos, BCH y Reed-Solomon no aparecen por casualidad: emergen de la aritmética en campos finitos y de la teoría de raíces de polinomios.

## 4.2.1 Fundamentos algebraicos: grupos, anillos y campos

Un **grupo** $(G,+)$ es un conjunto dotado de una operación interna asociativa, con elemento neutro, inversos y, en el caso abeliano, conmutatividad. Un **anillo** $(R,+,\cdot)$ añade una segunda operación compatible con la suma. Un **campo** $(F,+,\cdot)$ es un anillo conmutativo en el que todo elemento no nulo posee inverso multiplicativo.

En codificación interesa especialmente el caso binario $GF(2)=\{0,1\}$, donde
$$
1+1=0, \qquad 1\cdot 1=1.
$$
Este simple hecho explica que las matrices generadoras, las matrices de paridad y las ecuaciones de síndrome se escriban como álgebra lineal sobre $GF(2)$.

> **Concepto clave:** la teoría de códigos lineales es álgebra lineal sobre campos finitos; la teoría de códigos cíclicos y BCH es álgebra polinomial sobre esos mismos campos.

**[Figura 4.4]:** diagrama jerárquico que muestre la inclusión conceptual **grupo $\subset$ anillo $\subset$ campo**. Debajo del diagrama deben aparecer ejemplos: enteros módulo $p$, polinomios binarios y campos finitos usados en codificación. La intención didáctica es evidenciar que cada capa algebraica agrega herramientas nuevas para diseñar códigos.

## 4.2.2 Campos finitos $GF(p)$

Si $p$ es primo, el conjunto de clases de equivalencia módulo $p$ forma un campo finito:
$$
GF(p)=\mathbb{Z}_p=\{0,1,\dots,p-1\}.
$$
Las operaciones se realizan módulo $p$.

Por ejemplo, en $GF(5)$,
$$
3+4 \equiv 2 \pmod{5}, \qquad 3\cdot 4 \equiv 2 \pmod{5}, \qquad 2^{-1}=3,
$$
porque $2\cdot 3=6\equiv 1 \pmod{5}$.

Todos los códigos lineales bloque clásicos sobre alfabeto binario trabajan sobre $GF(2)$. Cuando el alfabeto es no binario, como en Reed-Solomon, se utiliza $GF(q)$ con $q=p^m$.

**Ejemplo 4.7:** aritmética elemental en $GF(5)$.

Calcular
$$
(4+4)\cdot 3^{-1}.
$$
Primero,
$$
4+4 = 8 \equiv 3 \pmod{5}.
$$
Como
$$
3^{-1}=2,
$$
se obtiene
$$
(4+4)\cdot 3^{-1} \equiv 3\cdot 2 = 6 \equiv 1 \pmod{5}.
$$
El ejemplo prepara la intuición para trabajar después con clases de equivalencia polinómicas.

## 4.2.3 Extensiones $GF(p^m)$ y polinomios irreducibles

No existen campos de cardinalidad arbitraria; solo existen campos de tamaño $p^m$, con $p$ primo y $m\in\mathbb{N}$. Para construir $GF(2^m)$ se parte del anillo de polinomios binarios $GF(2)[x]$ y se toma cociente por un polinomio irreducible $p(x)$ de grado $m$:
$$
GF(2^m) \cong GF(2)[x]/\langle p(x)\rangle.
$$

Si $\alpha$ denota la clase del polinomio $x$, entonces en el campo se cumple la relación
$$
p(\alpha)=0.
$$
Por ello, todas las potencias de grado mayor o igual que $m$ pueden reducirse a combinaciones de $1,\alpha,\alpha^2,\dots,\alpha^{m-1}$.

Para $GF(2^3)$ elegimos típicamente
$$
p(x)=x^3+x+1,
$$
de modo que
$$
\alpha^3=\alpha+1.
$$
Para $GF(2^4)$ es común usar
$$
p(x)=x^4+x+1,
$$
lo que implica
$$
\alpha^4=\alpha+1.
$$

> **Concepto clave:** un polinomio irreducible juega el mismo papel que un número primo en aritmética entera: permite construir una estructura en la que la división por elementos no nulos vuelve a ser posible.

**[Figura 4.5]:** representación circular de las potencias de un elemento primitivo $\alpha$ en $GF(2^m)$, mostrando cómo la multiplicación por $\alpha$ recorre cíclicamente los elementos no nulos del campo. Sobre la figura deben indicarse las reducciones impuestas por el polinomio irreducible, por ejemplo $\alpha^3=\alpha+1$ o $\alpha^4=\alpha+1$.

**Ejemplo 4.8:** construcción explícita de $GF(2^3)$.

Con
$$
p(x)=x^3+x+1,
$$
se tiene
$$
\alpha^3=\alpha+1.
$$
Entonces:
$$
\alpha^4=\alpha\cdot\alpha^3=\alpha(\alpha+1)=\alpha^2+\alpha,
$$
$$
\alpha^5=\alpha\cdot\alpha^4=\alpha^3+\alpha^2=(\alpha+1)+\alpha^2=\alpha^2+\alpha+1,
$$
$$
\alpha^6=\alpha\cdot\alpha^5=\alpha^3+\alpha^2+\alpha=(\alpha+1)+\alpha^2+\alpha=\alpha^2+1,
$$
$$
\alpha^7=\alpha\cdot\alpha^6=\alpha^3+\alpha=(\alpha+1)+\alpha=1.
$$
Como $\alpha^7=1$, el elemento $\alpha$ genera todos los elementos no nulos y, por tanto, es **primitivo**.

## 4.2.4 Elementos primitivos, orden multiplicativo y polinomios mínimos

El conjunto no nulo de $GF(q)$ forma un grupo multiplicativo cíclico de orden $q-1$. Un elemento $\alpha$ se dice **primitivo** si genera todos los elementos no nulos:
$$
GF(q)^* = \{1,\alpha,\alpha^2,\dots,\alpha^{q-2}\}.
$$

El **orden multiplicativo** de $\beta\neq 0$ es el menor entero $\ell$ tal que
$$
\beta^{\ell}=1.
$$

El **polinomio mínimo** de un elemento $\beta\in GF(2^m)$ sobre $GF(2)$ es el polinomio mónico de menor grado con coeficientes en $GF(2)$ tal que
$$
M_\beta(\beta)=0.
$$

Si $\beta=\alpha^i$, sus conjugados bajo el automorfismo de Frobenius son
$$
\beta,\beta^2,\beta^{2^2},\dots
$$
hasta cerrar ciclo. El polinomio mínimo es el producto
$$
M_\beta(x)=\prod_j (x-\beta^{2^j}).
$$
En característica $2$, restar y sumar son equivalentes.

**Ejemplo 4.9:** polinomio mínimo de $\alpha$ y de $\alpha^3$ en $GF(2^4)$.

Usando $p(x)=x^4+x+1$ y un elemento primitivo $\alpha$, los conjugados de $\alpha$ son
$$
\alpha,\alpha^2,\alpha^4,\alpha^8.
$$
Entonces
$$
M_{\alpha}(x)=(x+\alpha)(x+\alpha^2)(x+\alpha^4)(x+\alpha^8)=x^4+x+1.
$$
Es decir, el propio polinomio irreducible de construcción es el polinomio mínimo de $\alpha$.

Para $\alpha^3$, los conjugados son
$$
\alpha^3,\alpha^6,\alpha^{12},\alpha^9.
$$
Por tanto,
$$
M_{\alpha^3}(x)=(x+\alpha^3)(x+\alpha^6)(x+\alpha^{12})(x+\alpha^9)=x^4+x^3+x^2+x+1.
$$
Este resultado será esencial cuando se diseñen códigos BCH mediante raíces consecutivas.

## 4.2.5 Tabla completa de representaciones y aritmética en $GF(2^3)$

Tomando $GF(2^3)=GF(2)[x]/\langle x^3+x+1\rangle$, la representación completa de los elementos es la siguiente:

|Representación|Polinomio asociado|Vector binario|Inverso multiplicativo|
|---|---|---|---|
|0|0|[0,0,0]|No existe|
|1|1|[0,0,1]|1|
|α|x|[0,1,0]|α^6|
|α^2|x^2|[1,0,0]|α^5|
|α^3|x + 1|[0,1,1]|α^4|
|α^4|x^2 + x|[1,1,0]|α^3|
|α^5|x^2 + x + 1|[1,1,1]|α^2|
|α^6|x^2 + 1|[1,0,1]|α|

La suma se realiza coeficiente a coeficiente módulo $2$, es decir, mediante una operación XOR sobre los vectores binarios. La tabla completa de suma es:

|+|0|1|α|α^2|α^3|α^4|α^5|α^6|
|---|---|---|---|---|---|---|---|---|
|0|0|1|α|α^2|α^3|α^4|α^5|α^6|
|1|1|0|α^3|α^6|α|α^5|α^4|α^2|
|α|α|α^3|0|α^4|1|α^2|α^6|α^5|
|α^2|α^2|α^6|α^4|0|α^5|α|α^3|1|
|α^3|α^3|α|1|α^5|0|α^6|α^2|α^4|
|α^4|α^4|α^5|α^2|α|α^6|0|1|α^3|
|α^5|α^5|α^4|α^6|α^3|α^2|1|0|α|
|α^6|α^6|α^2|α^5|1|α^4|α^3|α|0|

La multiplicación se obtiene reduciendo potencias con la identidad $\alpha^3=\alpha+1$. La tabla completa de multiplicación es:

|×|0|1|α|α^2|α^3|α^4|α^5|α^6|
|---|---|---|---|---|---|---|---|---|
|0|0|0|0|0|0|0|0|0|
|1|0|1|α|α^2|α^3|α^4|α^5|α^6|
|α|0|α|α^2|α^3|α^4|α^5|α^6|1|
|α^2|0|α^2|α^3|α^4|α^5|α^6|1|α|
|α^3|0|α^3|α^4|α^5|α^6|1|α|α^2|
|α^4|0|α^4|α^5|α^6|1|α|α^2|α^3|
|α^5|0|α^5|α^6|1|α|α^2|α^3|α^4|
|α^6|0|α^6|1|α|α^2|α^3|α^4|α^5|

**Ejemplo 4.10:** operaciones completas en $GF(2^3)$.

1. **Suma:**
$$
\alpha^5+\alpha^2 = (\alpha^2+\alpha+1)+\alpha^2 = \alpha+1 = \alpha^3.
$$

2. **Producto:**
$$
\alpha^4\cdot \alpha^6 = \alpha^{10}=\alpha^{10\bmod 7}=\alpha^3=\alpha+1.
$$
También puede verificarse en forma polinómica:
$$
(\alpha^2+\alpha)(\alpha^2+1)=\alpha^4+\alpha^3+\alpha^2+\alpha.
$$
Como
$$
\alpha^4=\alpha^2+\alpha, \qquad \alpha^3=\alpha+1,
$$
se obtiene
$$
(\alpha^2+\alpha)+(\alpha+1)+\alpha^2+\alpha = \alpha+1 = \alpha^3.
$$

3. **Inverso:**
$$
(\alpha^4)^{-1}=\alpha^3,
$$
porque
$$
\alpha^4\cdot \alpha^3 = \alpha^7 = 1.
$$

## 4.2.6 Tabla de representaciones, logaritmos e inversos en $GF(2^4)$

Tomando $GF(2^4)=GF(2)[x]/\langle x^4+x+1\rangle$, la tabla completa de representación es:

|Representación|Polinomio asociado|Vector binario|Inverso multiplicativo|
|---|---|---|---|
|0|0|[0,0,0,0]|No existe|
|1|1|[0,0,0,1]|1|
|α|x|[0,0,1,0]|α^14|
|α^2|x^2|[0,1,0,0]|α^13|
|α^3|x^3|[1,0,0,0]|α^12|
|α^4|x + 1|[0,0,1,1]|α^11|
|α^5|x^2 + x|[0,1,1,0]|α^10|
|α^6|x^3 + x^2|[1,1,0,0]|α^9|
|α^7|x^3 + x + 1|[1,0,1,1]|α^8|
|α^8|x^2 + 1|[0,1,0,1]|α^7|
|α^9|x^3 + x|[1,0,1,0]|α^6|
|α^10|x^2 + x + 1|[0,1,1,1]|α^5|
|α^11|x^3 + x^2 + x|[1,1,1,0]|α^4|
|α^12|x^3 + x^2 + x + 1|[1,1,1,1]|α^3|
|α^13|x^3 + x^2 + 1|[1,1,0,1]|α^2|
|α^14|x^3 + 1|[1,0,0,1]|α|

Una tabla log/antilog completa, útil para implementación práctica, es:

|Exponente|Elemento|Polinomio|
|---|---|---|
|-∞|0|0|
|0|1|1|
|1|α|x|
|2|α^2|x^2|
|3|α^3|x^3|
|4|α^4|x + 1|
|5|α^5|x^2 + x|
|6|α^6|x^3 + x^2|
|7|α^7|x^3 + x + 1|
|8|α^8|x^2 + 1|
|9|α^9|x^3 + x|
|10|α^10|x^2 + x + 1|
|11|α^11|x^3 + x^2 + x|
|12|α^12|x^3 + x^2 + x + 1|
|13|α^13|x^3 + x^2 + 1|
|14|α^14|x^3 + 1|

Como el grupo multiplicativo no nulo tiene orden $15$, toda multiplicación entre elementos no nulos puede escribirse como
$$
\alpha^i\cdot\alpha^j = \alpha^{(i+j)\bmod 15},
$$
y el inverso se obtiene como
$$
(\alpha^i)^{-1}=\alpha^{15-i}.
$$
La suma sigue siendo XOR sobre las representaciones binarias. Este doble punto de vista —vectorial para sumar y exponencial para multiplicar— es la herramienta práctica más utilizada en implementación de decodificadores BCH y Reed-Solomon.

**Ejemplo 4.11:** aritmética en $GF(2^4)$.

Usando $\alpha^4=\alpha+1$:

1. **Suma:**
$$
\alpha^7+\alpha^3 = (\alpha^3+\alpha+1)+\alpha^3 = \alpha+1 = \alpha^4.
$$

2. **Producto:**
$$
\alpha^9\cdot\alpha^{11}=\alpha^{20}=\alpha^5.
$$
En forma polinómica,
$$
\alpha^9=x^3+x, \qquad \alpha^{11}=x^3+x^2+x,
$$
por lo que
$$
(x^3+x)(x^3+x^2+x)=x^6+x^5+x^3+x^2.
$$
Reduciendo con $x^4=x+1$:
$$
x^6=x^2x^4=x^2(x+1)=x^3+x^2,
$$
$$
x^5=x(x^4)=x(x+1)=x^2+x.
$$
Entonces
$$
x^6+x^5+x^3+x^2=(x^3+x^2)+(x^2+x)+x^3+x^2=x^2+x=\alpha^5.
$$

3. **Polinomio mínimo de $\alpha^5$:** como sus conjugados son $\alpha^5$ y $\alpha^{10}$, se obtiene
$$
M_{\alpha^5}(x)=(x+\alpha^5)(x+\alpha^{10})=x^2+x+1.
$$

## 4.2.7 De la teoría de campos a los polinomios generadores

Sea $C$ un código cíclico binario de longitud $n$. Si identificamos una palabra-código
$$
\mathbf{c}=(c_0,c_1,\dots,c_{n-1})
$$
con el polinomio
$$
c(x)=c_0+c_1x+\cdots+c_{n-1}x^{n-1},
$$
entonces la ciclicidad equivale a trabajar en el anillo cociente
$$
GF(2)[x]/\langle x^n-1\rangle.
$$
Todo ideal de este anillo es principal, luego existe un único polinomio mónico $g(x)$ tal que
$$
C=\{m(x)g(x)\bmod (x^n-1)\}.
$$
Ese polinomio es el **polinomio generador** del código.

La teoría de campos de Galois entra en juego cuando se eligen raíces deseadas de $g(x)$. Si $\alpha$ es un elemento de orden $n$ en una extensión adecuada, un diseño BCH prescribe que
$$
g(\alpha^b)=g(\alpha^{b+1})=\cdots=g(\alpha^{b+\delta-2})=0.
$$
Entonces $g(x)$ debe contener los polinomios mínimos de esas raíces:
$$
g(x)=\operatorname{mcm}\big(M_{\alpha^b}(x),M_{\alpha^{b+1}}(x),\dots,M_{\alpha^{b+\delta-2}}(x)\big).
$$

> **Concepto clave:** la distancia mínima de muchos códigos algebraicos se controla imponiendo que el polinomio generador tenga raíces consecutivas en una extensión $GF(2^m)$.

**[Figura 4.6]:** diagrama que conecte tres niveles: abajo, el campo extendido $GF(2^m)$ con sus potencias de $\alpha$; en el medio, los polinomios mínimos asociados a clases ciclotómicas; arriba, el polinomio generador $g(x)$ obtenido como mínimo común múltiplo. La figura debe hacer visible que el diseño de un código es una selección organizada de raíces.

**Ejemplo 4.12:** obtención del polinomio generador del Hamming $(7,4)$ desde teoría de campos.

Sea $n=7=2^3-1$ y sea $\alpha$ primitivo en $GF(2^3)$. Para un BCH binario de distancia diseñada $\delta=3$, se imponen como raíces $\alpha$ y $\alpha^2$. Ambas pertenecen a la misma clase ciclotómica
$$
C_1=\{1,2,4\}.
$$
Su polinomio mínimo es
$$
M_{\alpha}(x)=(x+\alpha)(x+\alpha^2)(x+\alpha^4)=x^3+x+1.
$$
Luego
$$
g(x)=x^3+x+1.
$$
Como $\deg g=3$, la dimensión es
$$
k=n-\deg g = 7-3=4.
$$
Por tanto, el Hamming $(7,4)$ aparece como un caso particular de código BCH primitivo binario.

**Ejemplo 4.13:** polinomio generador de un Reed-Solomon corto sobre $GF(2^3)$.

Considérese un código RS de longitud $n=7$ sobre $GF(2^3)$ con dos raíces consecutivas $\alpha$ y $\alpha^2$. Entonces
$$
g(x)=(x-\alpha)(x-\alpha^2).
$$
En característica $2$, restar y sumar coinciden, así que
$$
g(x)=(x+\alpha)(x+\alpha^2)=x^2+\alpha^4x+\alpha^3.
$$
La verificación se obtiene al expandir:
$$
(x+\alpha)(x+\alpha^2)=x^2+(\alpha+\alpha^2)x+\alpha^3.
$$
Como
$$
\alpha+\alpha^2 = \alpha^4,
$$
se concluye que
$$
g(x)=x^2+\alpha^4x+\alpha^3.
$$
Este ejemplo ilustra que en Reed-Solomon los coeficientes del generador viven en el propio campo extendido, no necesariamente en $GF(2)$.

---

# 4.3 Codificación de Bloques

## 4.3.1 Conceptos fundamentales: código $(n,k)$, tasa y distancia de Hamming

Un código de bloques transforma cada bloque de $k$ símbolos de información en una palabra-código de longitud $n$. En el caso binario,
$$
\mathbf{u}\in GF(2)^k \longmapsto \mathbf{c}\in GF(2)^n.
$$
La **tasa de código** es
$$
R=\frac{k}{n}.
$$
La **distancia de Hamming** entre dos palabras $\mathbf{x}$ y $\mathbf{y}$ es el número de posiciones en las que difieren:
$$
d_H(\mathbf{x},\mathbf{y}) = w_H(\mathbf{x}-\mathbf{y}),
$$
donde $w_H$ es el peso de Hamming.

La distancia mínima del código es
$$
d_{\min}=\min_{\mathbf{c}_i\neq \mathbf{c}_j} d_H(\mathbf{c}_i,\mathbf{c}_j).
$$
Sus consecuencias operativas son
$$
\text{detección máxima}=d_{\min}-1,
$$
$$
\text{corrección máxima}=\left\lfloor\frac{d_{\min}-1}{2}\right\rfloor.
$$

> **Concepto clave:** en códigos de bloques, la confiabilidad se diseña en el espacio discreto de palabras binarias mediante la separación en distancia de Hamming.

**Ejemplo 4.14:** parámetros básicos de un código.

Si un código tiene $n=7$ y $k=4$, entonces
$$
R=\frac{4}{7}\approx 0.571.
$$
Si además $d_{\min}=3$, puede detectar hasta
$$
3-1=2
$$
errores y corregir
$$
\left\lfloor\frac{3-1}{2}\right\rfloor=1
$$
error por palabra.

## 4.3.2 Códigos lineales: definición y propiedades

Un código binario es **lineal** si el conjunto de palabras-código forma un subespacio vectorial de $GF(2)^n$. Por tanto, para cualesquiera $\mathbf{c}_1,\mathbf{c}_2\in C$ y $a,b\in GF(2)$ se cumple
$$
a\mathbf{c}_1+b\mathbf{c}_2\in C.
$$

En el caso binario, esto implica en particular que la suma módulo $2$ de dos palabras válidas es otra palabra válida. Una propiedad fundamental es que, en un código lineal,
$$
d_{\min}=\min_{\mathbf{c}\neq\mathbf{0}} w_H(\mathbf{c}).
$$

**Ejemplo 4.15:** verificación de linealidad.

Considérese el código generado por
$$
G=
\begin{bmatrix}
1&0&0&1&1&0\\
0&1&0&1&0&1\\
0&0&1&0&1&1
\end{bmatrix}.
$$
Dos mensajes son
$$
\mathbf{u}_1=[1\ 0\ 1], \qquad \mathbf{u}_2=[0\ 1\ 1].
$$
Sus palabras-código son
$$
\mathbf{c}_1=\mathbf{u}_1G=[1\ 0\ 1\ 1\ 0\ 1],
$$
$$
\mathbf{c}_2=\mathbf{u}_2G=[0\ 1\ 1\ 1\ 1\ 0].
$$
La suma es
$$
\mathbf{c}_1+\mathbf{c}_2=[1\ 1\ 0\ 0\ 1\ 1].
$$
Pero también
$$
\mathbf{u}_1+\mathbf{u}_2=[1\ 1\ 0],
$$
y
$$
[1\ 1\ 0]G=[1\ 1\ 0\ 0\ 1\ 1].
$$
Por tanto, el conjunto es lineal.

## 4.3.3 Matriz generadora $G$ y forma sistemática

En un código lineal $(n,k)$, una matriz generadora $G$ de tamaño $k\times n$ permite codificar mediante
$$
\mathbf{c}=\mathbf{u}G.
$$
Si $G$ está en forma sistemática,
$$
G=[I_k\; P],
$$
entonces la palabra-código se escribe como
$$
\mathbf{c}=[\mathbf{u}\;\mathbf{p}],
$$
donde $\mathbf{p}=\mathbf{u}P$ contiene los bits de paridad.

Esta forma es especialmente útil porque separa de manera explícita la información y la redundancia.

**Ejemplo 4.16:** construcción de $G$ en forma sistemática.

Tomando
$$
P=
\begin{bmatrix}
1&1&0\\
1&0&1\\
0&1&1
\end{bmatrix},
$$
se obtiene
$$
G=
\left[
\begin{array}{ccc|ccc}
1&0&0&1&1&0\\
0&1&0&1&0&1\\
0&0&1&0&1&1
\end{array}
\right].
$$
El código tiene longitud $n=6$, dimensión $k=3$ y tasa
$$
R=\frac{3}{6}=\frac{1}{2}.
$$
Las tres filas de $G$ forman una base del subespacio codificado.

## 4.3.4 Codificación usando $G$

La codificación es una transformación lineal sobre $GF(2)$. Si
$$
\mathbf{u}=[u_1\ u_2\ \dots\ u_k],
$$
entonces
$$
\mathbf{c}=u_1\mathbf{g}_1+u_2\mathbf{g}_2+\cdots+u_k\mathbf{g}_k,
$$
donde $\mathbf{g}_i$ son las filas de $G$.

**Ejemplo 4.17:** enumeración completa de palabras-código.

Para la matriz del ejemplo anterior, se obtienen las palabras:

|Mensaje $\mathbf{u}$|Palabra-código $\mathbf{c}$|
|---|---|
|000|000000|
|001|001011|
|010|010101|
|011|011110|
|100|100110|
|101|101101|
|110|110011|
|111|111000|

Los pesos no nulos son $3$, $3$, $3$, $3$, $4$, $4$ y $4$, por lo que
$$
d_{\min}=3.
$$
Así, el código corrige un error y detecta hasta dos.

## 4.3.5 Matriz de chequeo de paridad $H$ y relación con $G$

Para un código lineal sistemático con
$$
G=[I_k\;P],
$$
una matriz de chequeo válida es
$$
H=[P^T\;I_{n-k}].
$$
Toda palabra-código satisface
$$
GH^T=0,
$$
y equivalentemente
$$
\mathbf{c}H^T=0.
$$

**Ejemplo 4.18:** construcción de $H$ a partir de $G$.

Con el mismo $P$ del ejemplo anterior,
$$
H=
\left[
\begin{array}{ccc|ccc}
1&1&0&1&0&0\\
1&0&1&0&1&0\\
0&1&1&0&0&1
\end{array}
\right].
$$
Se verifica que
$$
GH^T=0.
$$
Por ejemplo, para la primera fila de $G$,
$$
[1\ 0\ 0\ 1\ 1\ 0]H^T=[0\ 0\ 0].
$$
La misma verificación aplica a todas las palabras-código del subespacio generado.

## 4.3.6 Síndrome: definición e interpretación

Dado un vector recibido $\mathbf{r}$, su síndrome se define como
$$
\mathbf{s}=\mathbf{r}H^T.
$$
Si $\mathbf{r}=\mathbf{c}+\mathbf{e}$, entonces
$$
\mathbf{s}=\mathbf{c}H^T+\mathbf{e}H^T=\mathbf{e}H^T,
$$
porque $\mathbf{c}H^T=0$. El síndrome depende solo del error, no del mensaje transmitido.

> **Concepto clave:** el síndrome es una “firma algebraica” del patrón de error respecto de las restricciones del código.

**Ejemplo 4.19:** cálculo de síndrome.

Supóngase que se transmitió
$$
\mathbf{c}=101101,
$$
y el error fue
$$
\mathbf{e}=000100.
$$
Entonces
$$
\mathbf{r}=101001.
$$
Con la matriz $H$ anterior,
$$
\mathbf{s}=\mathbf{r}H^T=\mathbf{e}H^T=[1\ 0\ 0].
$$
Ese síndrome coincide con la cuarta columna de $H$, por lo que el receptor identifica un error en la cuarta posición y corrige sumando $000100$.

## 4.3.7 Capacidad de detección y corrección

La interpretación geométrica en el espacio de Hamming es inmediata: para corregir $t$ errores, las esferas de radio $t$ alrededor de las palabras-código deben ser disjuntas. De ahí proviene la condición
$$
d_{\min}\ge 2t+1.
$$
Para detectar hasta $s$ errores basta exigir
$$
d_{\min}\ge s+1.
$$

**Ejemplo 4.20:** capacidad correctora de un código.

Si un código tiene
$$
d_{\min}=5,
$$
entonces puede corregir
$$
t=\left\lfloor\frac{5-1}{2}\right\rfloor=2
$$
errores y detectar hasta
$$
5-1=4
$$
errores. Si ocurren tres errores, el código puede detectarlos en general, pero no garantizar su corrección unívoca.

## 4.3.8 Arreglo estándar y líderes de coset

Un **arreglo estándar** organiza todo $GF(2)^n$ en cosets del código:
$$
\mathbf{e}+C=\{\mathbf{e}+\mathbf{c}:\mathbf{c}\in C\}.
$$
Cada fila se etiqueta por un **líder de coset**, normalmente el vector de menor peso dentro del coset. La decodificación por probabilidad máxima en un canal binario simétrico asocia el recibido al coset cuyo líder tiene menor peso compatible con el síndrome observado.

**Ejemplo 4.21:** arreglo estándar para un código sencillo de paridad.

Considérese el código de paridad par de longitud $3$:
$$
C=\{000,011,101,110\}.
$$
El arreglo estándar es

|Líder|Elementos del coset|
|---|---|
|000|000, 011, 101, 110|
|001|001, 010, 100, 111|

El síndrome distingue entre ambas filas: la primera tiene paridad par y la segunda, paridad impar. Si el canal produce un solo error, el líder $001$ representa el coset más probable.

## 4.3.9 Decodificación por síndrome

La decodificación por síndrome consiste en:

1. calcular $\mathbf{s}=\mathbf{r}H^T$;
2. buscar el líder de coset $\hat{\mathbf{e}}$ con ese síndrome;
3. corregir como
$$
\hat{\mathbf{c}}=\mathbf{r}+\hat{\mathbf{e}}.
$$

**Ejemplo 4.22:** decodificación por síndrome.

Recibido
$$
\mathbf{r}=111001,
$$
con la matriz $H$ del ejemplo 4.18. Se calcula
$$
\mathbf{s}=\mathbf{r}H^T=[0\ 1\ 0].
$$
Ese síndrome coincide con la quinta columna de $H$, luego el error estimado es
$$
\hat{\mathbf{e}}=000010.
$$
La palabra corregida es
$$
\hat{\mathbf{c}}=111001+000010=111011.
$$
Si se verifica que $\hat{\mathbf{c}}H^T=0$, la corrección es consistente.

## 4.3.10 Códigos cíclicos: representación polinomial y codificación

En un código cíclico, toda rotación cíclica de una palabra-código vuelve a ser una palabra-código. Si identificamos palabras con polinomios módulo $x^n-1$, la ciclicidad se expresa como clausura bajo multiplicación por $x$ módulo $x^n-1$.

Un código cíclico binario de longitud $n$ tiene un generador mónico $g(x)$ tal que
$$
g(x)\mid (x^n-1).
$$
Toda palabra-código puede escribirse como
$$
c(x)=m(x)g(x), \qquad \deg m(x) < k.
$$

La codificación sistemática se obtiene mediante
$$
c(x)=x^{n-k}m(x)+r(x),
$$
donde $r(x)$ es el residuo de dividir $x^{n-k}m(x)$ por $g(x)$.

**Ejemplo 4.23:** codificación cíclica con el Hamming $(7,4)$.

Sea
$$
g(x)=x^3+x+1.
$$
Tomemos el mensaje
$$
m(x)=x^3+1.
$$
Entonces
$$
x^{3}m(x)=x^6+x^3.
$$
Al dividir por $g(x)$ se obtiene residuo
$$
r(x)=x^2+x.
$$
Por tanto, la palabra sistemática es
$$
c(x)=x^6+x^3+x^2+x.
$$
En forma binaria,
$$
\mathbf{c}=1001110.
$$

**Ejemplo 4.24:** detección de error por residuo.

Sea la palabra recibida
$$
r(x)=x^6+x^3+x^2+1.
$$
Si se divide por
$$
g(x)=x^3+x+1,
$$
se obtiene un residuo no nulo. Como una palabra-código válida debe cumplir
$$
r(x) \bmod g(x)=0,
$$
la recepción se declara errónea. Esta es la base conceptual de la comprobación cíclica usada en CRC.

## 4.3.11 Códigos de paridad

El código de paridad simple añade un bit de control para imponer que el peso total sea par o impar. Para paridad par,
$$
p = u_1+u_2+\cdots+u_k.
$$
Se trata del código lineal más sencillo, con
$$
d_{\min}=2.
$$
Detecta un error, pero no corrige ninguno.

**Ejemplo 4.25:** código de paridad simple.

Si el mensaje es
$$
\mathbf{u}=1011,
$$
entonces su peso es $3$. Para paridad par, el bit de control debe ser $1$, pues
$$
1+0+1+1+1 = 4 \equiv 0 \pmod 2.
$$
La palabra transmitida es
$$
\mathbf{c}=10111.
$$
Si se recibe $10110$, la paridad total pasa a ser impar y el error se detecta.

## 4.3.12 Códigos Hamming: construcción desde teoría de campos, propiedades y límites

Los códigos Hamming binarios tienen parámetros
$$
(n,k)=(2^m-1,2^m-m-1), \qquad d_{\min}=3.
$$
Pueden construirse de dos maneras equivalentes:

1. **vía matriz de chequeo**, tomando como columnas todos los vectores binarios no nulos de longitud $m$;
2. **vía teoría de campos**, como BCH primitivos binarios con raíces $\alpha$ y $\alpha^2$ en $GF(2^m)$.

La segunda construcción da directamente el polinomio generador
$$
g(x)=M_{\alpha}(x),
$$
donde $M_{\alpha}(x)$ es el polinomio mínimo del elemento primitivo $\alpha$.

Limitaciones principales:

- solo corrigen **un error**;
- cuando la tasa crece, su ganancia de codificación es moderada frente a familias modernas;
- no son adecuados para canales con ráfagas largas ni para longitudes muy grandes cuando se exige cercanía a capacidad.

**Ejemplo 4.26:** construcción completa del Hamming $(7,4)$.

Tomando $m=3$, las columnas de $H$ son todos los vectores binarios no nulos de longitud $3$:
$$
H=
\begin{bmatrix}
1&0&1&0&1&0&1\\
0&1&1&0&0&1&1\\
0&0&0&1&1&1&1
\end{bmatrix}.
$$
Llevando $H$ a forma sistemática se obtiene una matriz generadora válida
$$
G=
\begin{bmatrix}
1&0&0&0&1&1&0\\
0&1&0&0&1&0&1\\
0&0&1&0&0&1&1\\
0&0&0&1&1&1&1
\end{bmatrix}.
$$
Si el mensaje es
$$
\mathbf{u}=1011,
$$
entonces
$$
\mathbf{c}=\mathbf{u}G=1011010.
$$
Si durante la transmisión ocurre un error en la sexta posición,
$$
\mathbf{r}=1011000.
$$
El síndrome es la sexta columna de $H$,
$$
\mathbf{s}=\mathbf{r}H^T=[0\ 1\ 1]^T,
$$
por lo que el receptor corrige invirtiendo ese bit.

Desde el punto de vista de teoría de campos, el mismo código se obtiene con
$$
g(x)=x^3+x+1,
$$
que es el polinomio mínimo de $\alpha$ en $GF(2^3)$.

## 4.3.13 Códigos BCH: diseño algebraico por raíces consecutivas

Un código BCH binario primitivo de longitud
$$
n=2^m-1
$$
y distancia diseñada $\delta$ se construye imponiendo que su polinomio generador tenga como raíces consecutivas
$$
\alpha^b,\alpha^{b+1},\dots,\alpha^{b+\delta-2}.
$$
Entonces
$$
g(x)=\operatorname{mcm}\left(M_{\alpha^b}(x),M_{\alpha^{b+1}}(x),\dots,M_{\alpha^{b+\delta-2}}(x)\right).
$$

La cota BCH garantiza
$$
d_{\min}\ge \delta,
$$
y por tanto la capacidad correctora es al menos
$$
t\ge \left\lfloor\frac{\delta-1}{2}\right\rfloor.
$$

**Ejemplo 4.27:** BCH binario $(15,7)$ con $t=2$.

En $GF(2^4)$ con $\alpha$ primitivo y $n=15$, para diseñar $\delta=5$ se imponen las raíces
$$
\alpha,\alpha^2,\alpha^3,\alpha^4.
$$
Las clases ciclotómicas relevantes son
$$
C_1=\{1,2,4,8\}, \qquad C_3=\{3,6,12,9\}.
$$
Por tanto,
$$
M_{\alpha}(x)=x^4+x+1,
$$
$$
M_{\alpha^3}(x)=x^4+x^3+x^2+x+1.
$$
Luego,
$$
g(x)=M_{\alpha}(x)M_{\alpha^3}(x)=x^8+x^7+x^6+x^4+1.
$$
Como $\deg g=8$,
$$
k=15-8=7.
$$
El código puede corregir hasta
$$
t=2
$$
errores binarios por palabra.

## 4.3.14 Códigos Reed-Solomon: BCH no binarios, símbolos y borrados

Los códigos Reed-Solomon (RS) son una subfamilia de BCH definida sobre $GF(q)$, típicamente con $q=2^m$. Tienen parámetros
$$
(n,k), \qquad n\le q-1,
$$
y generador
$$
g(x)=\prod_{i=b}^{b+n-k-1}(x-\alpha^i).
$$
Trabajan a nivel de **símbolos** en lugar de bits, por lo que son extraordinariamente eficaces contra errores en ráfaga y borrados.

Su capacidad viene dada por
$$
2e+s \le n-k,
$$
donde $e$ es el número de errores de símbolo y $s$ el número de borrados.

> **Concepto clave:** un Reed-Solomon no “ve” bits aislados, sino símbolos de $m$ bits; por eso corrige muy bien paquetes perdidos o ráfagas largas concentradas.

**Ejemplo 4.28:** generador y capacidad de un RS sobre $GF(2^3)$.

Para un RS$(7,5)$ sobre $GF(2^3)$ con raíces $\alpha$ y $\alpha^2$,
$$
g(x)=(x-\alpha)(x-\alpha^2)=x^2+\alpha^4x+\alpha^3.
$$
Como
$$
n-k=2,
$$
puede corregir:

- $1$ error de símbolo, porque $2e\le 2$ si $e=1$;
- o $2$ borrados, porque $s\le 2$.

Si un paquete Ethernet, una trama óptica o varios bytes contiguos se pierden, el descodificador RS puede reconstruirlos siempre que se respeten esas condiciones.

## 4.3.15 LDPC: matrices dispersas, grafos de Tanner y propagación de creencias

Los códigos **LDPC** (Low-Density Parity-Check) se definen mediante una matriz de paridad muy dispersa
$$
H\mathbf{c}^T=0,
$$
con operaciones en $GF(2)$. La baja densidad permite representar el código por un **grafo de Tanner**, con nodos de variable y nodos de chequeo, y descodificarlo mediante **belief propagation** o algoritmos de paso de mensajes.

En variantes cuasi-cíclicas, la matriz de paridad puede describirse mediante polinomios en
$$
GF(2)[x]/\langle x^Z-1\rangle,
$$
lo cual enlaza de nuevo con la teoría algebraica de campos y anillos.

Un generador $G$ puede obtenerse a partir de $H$ por eliminación gaussiana sobre $GF(2)$, pero en diseño práctico suele trabajarse directamente con $H$ por su estructura dispersa.

**Ejemplo 4.29:** mini-LDPC y una iteración conceptual.

Considérese
$$
H=
\begin{bmatrix}
1&1&0&1&0&0\\
0&1&1&0&1&0\\
1&0&1&0&0&1
\end{bmatrix}.
$$
Las ecuaciones de paridad son
$$
c_1+c_2+c_4=0,
$$
$$
c_2+c_3+c_5=0,
$$
$$
c_1+c_3+c_6=0.
$$
Si una decisión dura inicial produce
$$
\hat{\mathbf{c}}^{(0)}=101100,
$$
entonces los chequeos dan
$$
1+0+1=0,
$$
$$
0+1+0=1,
$$
$$
1+1+0=0.
$$
Falla solo el segundo chequeo. En un algoritmo iterativo, ese nodo de chequeo “envía” evidencia correctiva a $c_2$, $c_3$ y $c_5$, y el bit menos confiable entre ellos se revisa. Esta filosofía local explica la excelente relación desempeño-complejidad de los LDPC modernos.

## 4.3.16 Códigos polares: polarización de canal y generador sobre $GF(2)$

Los códigos polares de Arıkan se construyen sobre el kernel binario
$$
F=
\begin{bmatrix}
1&0\\
1&1
\end{bmatrix},
$$
y su generador base es
$$
G_N = B_NF^{\otimes n}, \qquad N=2^n,
$$
donde $B_N$ es la permutación de bit-reversal y $F^{\otimes n}$ es la potencia de Kronecker. Toda la construcción ocurre sobre $GF(2)$.

La idea esencial es la **polarización del canal**: al combinar y separar canales recursivamente, algunos subcanales se vuelven muy confiables y otros muy poco confiables. Los bits de información se colocan en los primeros y los demás se congelan.

**Ejemplo 4.30:** generador polar de longitud $4$.

Para $N=4$,
$$
F^{\otimes 2}=
\begin{bmatrix}
1&0&0&0\\
1&1&0&0\\
1&0&1&0\\
1&1&1&1
\end{bmatrix}.
$$
Si se eligen como congelados $u_1=u_2=0$ y como información $u_3=1$, $u_4=0$, entonces
$$
\mathbf{u}=[0\ 0\ 1\ 0].
$$
La palabra polar es
$$
\mathbf{x}=\mathbf{u}F^{\otimes 2}=[1\ 0\ 1\ 0].
$$
La matriz generadora es completamente binaria y, por tanto, también está anclada en la aritmética de $GF(2)$.

## 4.3.17 Comparación de familias de códigos de bloques

|Familia|Base algebraica|Generador desde teoría de campos|Ventaja principal|Limitación típica|Decodificación típica|
|---|---|---|---|---|---|
|Paridad|$GF(2)$|Una sola ecuación lineal de suma nula|Simplicidad extrema|Solo detecta 1 error|Comprobación de paridad|
|Hamming|$GF(2)$ y $GF(2^m)$|$g(x)=M_\alpha(x)$ o columnas no nulas de $H$|Corrección de 1 error con alta tasa|No corrige múltiples errores|Síndrome|
|BCH|$GF(2^m)$|m.c.m. de polinomios mínimos de raíces consecutivas|Diseño algebraico con $t$ controlable|Complejidad creciente|Berlekamp-Massey, Chien|
|Reed-Solomon|$GF(2^m)$|$g(x)=\prod(x-\alpha^i)$|Excelente contra ráfagas y borrados|Opera por símbolos, no por bit aislado|Euclídeo extendido, BM, Forney|
|LDPC|$GF(2)$ con $H$ dispersa|Matrices de paridad dispersas o polinomiales QC|Muy cerca de capacidad|Error floor, diseño delicado|Belief propagation|
|Polar|$GF(2)$ y kernel de Kronecker|$G_N=B_NF^{\otimes n}$|Pruebas de capacidad, adoptados en 5G|Bloques largos y diseño de congelados|SC, SCL, CRC-aided SCL|

## 4.3.18 Ejemplos integradores adicionales

**Ejemplo 4.31:** relación entre distancia mínima y desempeño.

Si dos códigos tienen la misma tasa pero uno posee $d_{\min}=3$ y otro $d_{\min}=5$, el segundo tolera un radio de corrección mayor:
$$
t_1=1, \qquad t_2=2.
$$
Sin embargo, esto no implica automáticamente mejor desempeño asintótico en todos los regímenes; también influyen la multiplicidad de palabras de bajo peso y el algoritmo de decodificación.

**Ejemplo 4.32:** el síndrome como firma del error.

Para el Hamming $(7,4)$, si ocurre un error único en la posición $i$, el síndrome es exactamente la columna $i$ de $H$. De esta forma, el espacio de errores de peso $1$ queda etiquetado sin ambigüedad. Esta observación es la esencia algebraica de la corrección de un error.

---

# 4.4 Codificación Convolucional

## 4.4.1 Estructura del codificador convolucional: registros, memoria, tasa y matriz generadora

A diferencia de los códigos de bloques, un código convolucional introduce redundancia de manera secuencial. La salida actual depende del bit de entrada presente y de un número finito de bits anteriores almacenados en registros de desplazamiento.

Un codificador de tasa
$$
R=\frac{k_0}{n_0}
$$
convierte $k_0$ bits de entrada por instante en $n_0$ bits de salida. La **memoria** total $m$ determina la **longitud de restricción**
$$
K=m+1.
$$

En el caso binario de una entrada y dos salidas, la representación polinomial usa el retardo $D$ y generadores sobre $GF(2)$:
$$
G(D)=[g_1(D)\; g_2(D)].
$$
También puede representarse mediante una matriz semi-infinita de Toeplitz sobre $GF(2)$.

> **Concepto clave:** en un código convolucional, la redundancia no está repartida por bloques aislados, sino “convolucionada” con la historia de la secuencia.

**Ejemplo 4.33:** parámetros de un codificador clásico.

Sea
$$
G(D)=[1+D+D^2\; 1+D^2].
$$
Entonces el codificador produce dos bits por cada bit de entrada, luego
$$
R=\frac{1}{2}.
$$
El mayor grado de los generadores es $2$, por lo que
$$
m=2, \qquad K=3.
$$
El número de estados del trellis es
$$
2^m=4.
$$

## 4.4.2 Representación polinomial y construcción desde $GF(2)$

Los generadores de un código convolucional pertenecen al anillo de polinomios binarios en el retardo $D$. Por ejemplo,
$$
g_1(D)=1+D+D^2, \qquad g_2(D)=1+D^2.
$$
Si la secuencia de entrada se modela como
$$
u(D)=u_0+u_1D+u_2D^2+\cdots,
$$
las salidas son
$$
v_1(D)=u(D)g_1(D), \qquad v_2(D)=u(D)g_2(D),
$$
con operaciones módulo $2$.

Esto conecta de forma natural con la teoría de campos: toda la aritmética de codificación se hace en el campo base $GF(2)$, aunque la memoria temporal sustituya aquí a la estructura de bloque.

**Ejemplo 4.34:** interpretación de generadores.

Para
$$
g_1(D)=1+D+D^2,
$$
la primera salida en el instante $k$ es
$$
v_{1,k}=u_k+u_{k-1}+u_{k-2}.
$$
Para
$$
g_2(D)=1+D^2,
$$
la segunda salida es
$$
v_{2,k}=u_k+u_{k-2}.
$$
Todas las sumas son en $GF(2)$. Esta forma hace explícito qué bits de memoria participan en cada rama del codificador.

## 4.4.3 Códigos convolucionales sistemáticos y no sistemáticos

Un código convolucional es **sistemático** si una de sus salidas reproduce directamente la entrada:
$$
v^{(s)}_k=u_k.
$$
Es **no sistemático** si todas las salidas son combinaciones lineales de bits actuales y pasados.

Los códigos sistemáticos facilitan el intercambio de información extrínseca en decodificación iterativa y por ello son esenciales en turbo códigos. Los no sistemáticos suelen ofrecer mejor dispersión de peso para una misma complejidad.

**Ejemplo 4.35:** comparación simple.

- No sistemático:
$$
G(D)=[1+D+D^2\; 1+D^2].
$$
- Sistemático:
$$
G(D)=\left[1\; \frac{1+D^2}{1+D+D^2}\right].
$$

En el primero, ambos bits de salida son paridades. En el segundo, la primera salida es el bit de información y la segunda es una paridad recursiva. Esta diferencia será decisiva al construir turbo códigos.

## 4.4.4 Códigos RSC: Recursive Systematic Convolutional

Un código **RSC** posee una salida sistemática y una realimentación interna. En notación racional sobre $GF(2)$,
$$
G(D)=\left[1\; \frac{P(D)}{F(D)}\right],
$$
donde $F(D)$ es el polinomio de realimentación y $P(D)$ el de avance.

La realimentación introduce trayectorias con pesos más favorables para decodificación iterativa. Por esta razón, los RSC son los bloques elementales de los turbo códigos clásicos.

**Ejemplo 4.36:** estructura RSC de tasa $1/2$.

Sea
$$
G(D)=\left[1\;\frac{1+D^2}{1+D+D^2}\right].
$$
Definamos $x_k$ como la señal interna a la memoria. Entonces
$$
x_k = u_k + x_{k-1} + x_{k-2},
$$
y la paridad de salida es
$$
p_k = x_k + x_{k-2}.
$$
Si la secuencia de entrada comienza con $u_0=1$, $u_1=0$, $u_2=1$ y el estado inicial es cero, se calculan sucesivamente:
$$
x_0=1, \quad p_0=1,
$$
$$
x_1=0+1+0=1, \quad p_1=1,
$$
$$
x_2=1+1+1=1, \quad p_2=0.
$$
La salida sistemática es $101$ y la paridad correspondiente es $110$.

## 4.4.5 Códigos punzados: adaptación de tasa

Un código punzado se obtiene eliminando periódicamente algunos bits de salida de un código madre. Si el código madre tiene tasa $1/2$ y se elimina un bit de cada cuatro salidas según un patrón periódico, la tasa efectiva aumenta.

Formalmente, si el patrón de punción es una matriz binaria $P$, solo se transmiten las salidas cuyas posiciones contienen $1$.

**Ejemplo 4.37:** adaptación de $R=1/2$ a $R=2/3$.

Partamos de un código madre de tasa $1/2$ con salidas por tiempo
$$
(v_{1,k},v_{2,k}).
$$
Use el patrón periódico
$$
P=
\begin{bmatrix}
1&1\\
1&0
\end{bmatrix}.
$$
En dos instantes se generan cuatro bits,
$$
(v_{1,1},v_{2,1},v_{1,2},v_{2,2}),
$$
pero se transmite
$$
(v_{1,1},v_{2,1},v_{1,2}).
$$
Se enviaron $2$ bits de información y $3$ bits codificados, luego
$$
R_{\text{ef}}=\frac{2}{3}.
$$
La ventaja es la flexibilidad; la desventaja, una menor distancia libre.

## 4.4.6 Diagrama de estados

El estado de un codificador convolucional viene determinado por el contenido de sus memorias. Para memoria $m$, el número de estados es
$$
2^m.
$$
Cada transición está etiquetada por un bit de entrada y la salida correspondiente.

**Ejemplo 4.38:** diagrama de estados para el código $(7,5)$ en octal.

Los generadores octales
$$
(7,5)
$$
corresponden a
$$
g_1(D)=1+D+D^2, \qquad g_2(D)=1+D^2.
$$
Con memoria $m=2$, los estados son
$$
00,01,10,11.
$$
Desde cada estado parten dos ramas, una para entrada $0$ y otra para entrada $1$. Por ejemplo, desde el estado $10$:

- con entrada $0$ la salida es $10$ y el siguiente estado es $01$;
- con entrada $1$ la salida es $01$ y el siguiente estado es $11$.

El diagrama de estados compacta la dinámica del codificador en una máquina finita.

## 4.4.7 Diagrama de trellis

El trellis despliega el diagrama de estados a lo largo del tiempo. Cada columna representa un instante y cada nodo un estado posible en ese instante. El algoritmo de Viterbi opera precisamente sobre este grafo temporal.

**Ejemplo 4.39:** construcción inicial de un trellis.

Para el código $(7,5)$ con estado inicial $00$, en la primera etapa solo existen dos transiciones posibles:

- $00 \xrightarrow{0/00} 00$,
- $00 \xrightarrow{1/11} 10$.

En la segunda etapa, desde cada estado alcanzado vuelven a abrirse dos ramas. Después de pocas etapas, el trellis contiene múltiples caminos competidores que representan secuencias de entrada distintas pero compatibles con la misma longitud observada.

## 4.4.8 Codificación paso a paso y ecuaciones recursivas

La codificación secuencial puede seguirse directamente con los registros de desplazamiento o con las ecuaciones en $GF(2)$.

**Ejemplo 4.40:** codificación completa de la secuencia $101100$ con el código $(7,5)$.

Estado inicial: $00$.

1. **Entrada $1$**:
$$
v_1=1+0+0=1, \qquad v_2=1+0=1.
$$
Salida: $11$. Nuevo estado: $10$.

2. **Entrada $0$**:
$$
v_1=0+1+0=1, \qquad v_2=0+0=0.
$$
Salida: $10$. Nuevo estado: $01$.

3. **Entrada $1$**:
$$
v_1=1+0+1=0, \qquad v_2=1+1=0.
$$
Salida: $00$. Nuevo estado: $10$.

4. **Entrada $1$**:
$$
v_1=1+1+0=0, \qquad v_2=1+0=1.
$$
Salida: $01$. Nuevo estado: $11$.

5. **Entrada $0$**:
$$
v_1=0+1+1=0, \qquad v_2=0+1=1.
$$
Salida: $01$. Nuevo estado: $01$.

6. **Entrada $0$**:
$$
v_1=0+0+1=1, \qquad v_2=0+1=1.
$$
Salida: $11$. Nuevo estado: $00$.

La secuencia codificada es
$$
11\;10\;00\;01\;01\;11.
$$

La misma salida puede verificarse con las ecuaciones recursivas del ejemplo 4.34, confirmando la consistencia entre las representaciones temporal, polinomial y de estados.

## 4.4.9 Algoritmo de Viterbi

El algoritmo de Viterbi realiza decodificación de máxima verosimilitud sobre el trellis. En cada instante:

1. calcula métricas de rama;
2. acumula métricas de camino;
3. conserva, para cada estado, solo el superviviente de menor métrica;
4. al final, realiza traza hacia atrás.

Con decisión dura, la métrica de rama es una distancia de Hamming. Con decisión suave, es habitual usar distancia euclidiana o log-verosimilitudes.

> **Concepto clave:** Viterbi no examina exhaustivamente todos los caminos; elimina tempranamente los peores y conserva solo los supervivientes óptimos estado a estado.

**Ejemplo 4.41:** Viterbi con decisión dura.

Supóngase que el receptor observa la secuencia de pares
$$
11,\ 10,\ 01.
$$
Para el código $(7,5)$ y estado inicial $00$:

- **Etapa 1:** las transiciones posibles desde $00$ son $0/00$ y $1/11$. Como se recibió $11$, las métricas son $2$ y $0$, respectivamente. Sobrevive el camino hacia $10$ con métrica $0$.
- **Etapa 2:** desde los estados alcanzables se comparan las ramas compatibles con el recibido $10$. El algoritmo suma distancias de Hamming y conserva, para cada estado de llegada, el camino de menor métrica acumulada.
- **Etapa 3:** se repite el proceso con $01$.

Tras completar las tres etapas, el camino de menor métrica corresponde a la secuencia de entrada más probable. El procedimiento exacto depende de las ramas concretas del trellis, pero la regla general es siempre la misma: **mínima métrica acumulada**.

## 4.4.10 Decisión dura frente a decisión suave

Con decisión dura, cada símbolo recibido se cuantiza primero a $0$ o $1$. Con decisión suave, el decodificador conserva información analógica adicional, por ejemplo muestras o LLR.

Para BPSK,
$$
0 \mapsto +1, \qquad 1 \mapsto -1,
$$
y si se recibe una muestra $y$, la métrica euclidiana para una rama candidata $\mathbf{x}$ es
$$
\mu(\mathbf{x})=\sum_i (y_i-x_i)^2.
$$

**Ejemplo 4.42:** comparación dura vs. suave.

Supóngase que una rama candidata transmite $[+1,-1]$ y otra $[-1,+1]$, mientras que el receptor observa
$$
\mathbf{y}=[0.2,-0.9].
$$
Las métricas euclidianas son
$$
\mu_1=(0.2-1)^2+(-0.9+1)^2=0.64+0.01=0.65,
$$
$$
\mu_2=(0.2+1)^2+(-0.9-1)^2=1.44+3.61=5.05.
$$
La decisión suave favorece contundentemente a la primera rama. Si se hubiera cuantizado duramente a $[0,1]$, se perdería parte de esa evidencia.

## 4.4.11 Turbo códigos: concatenación paralela de RSC e iteración

Un turbo código clásico concatena en paralelo dos codificadores RSC idénticos. El primero recibe la secuencia original y el segundo una versión permutada por un **interleaver**.

La palabra transmitida suele contener:

- la salida sistemática,
- una primera paridad RSC,
- una segunda paridad RSC.

La decodificación se realiza iterativamente mediante intercambio de información extrínseca entre dos decodificadores SISO.

**Ejemplo 4.43:** estructura conceptual de un turbo código.

Sea la secuencia de entrada
$$
\mathbf{u}=1011.
$$
Si el interleaver aplica la permutación
$$
\pi=(1,3,4,2),
$$
la segunda rama procesa
$$
\pi(\mathbf{u})=1110.
$$
El primer RSC genera una paridad $\mathbf{p}^{(1)}$ a partir de $1011$ y el segundo una paridad $\mathbf{p}^{(2)}$ a partir de $1110$. La transmisión turbo queda conceptualmente como
$$
[\mathbf{u}\;\mathbf{p}^{(1)}\;\mathbf{p}^{(2)}].
$$
La ganancia turbo no proviene de una gran distancia mínima clásica, sino del refinamiento iterativo de probabilidades a través del interleaver.

## 4.4.12 Distancia libre y rendimiento

La **distancia libre** $d_{free}$ de un código convolucional es la mínima distancia de Hamming entre dos trayectorias distintas del trellis que parten y regresan al mismo estado de referencia. Es el análogo convolucional de $d_{\min}$.

A altas relaciones señal-ruido, la probabilidad de error está fuertemente influida por $d_{free}$ y por la multiplicidad de trayectorias asociadas.

**Ejemplo 4.44:** interpretación de $d_{free}$.

Si un código convolucional tiene
$$
d_{free}=5,
$$
su desempeño asintótico será mejor que el de otro con
$$
d_{free}=3,
$$
si ambos se decodifican óptimamente y tienen complejidad comparable. Sin embargo, aumentar $d_{free}$ suele requerir mayor memoria y, por tanto, más estados en el trellis.

## 4.4.13 Comparación de variantes convolucionales

|Familia|Generador sobre $GF(2)$|Rasgo estructural|Ventaja|Limitación|Uso típico|
|---|---|---|---|---|---|
|No sistemático|$[g_1(D),g_2(D),\dots]$|Todas las salidas son paridades|Buena dispersión de peso|Menor transparencia del bit fuente|Enlaces clásicos con Viterbi|
|Sistemático|$[1,p_2(D),\dots]$|Una salida replica la entrada|Útil para iteración y análisis|Puede penalizar algo la distancia|Turbo, HARQ|
|RSC|$[1,P(D)/F(D)]$|Realimentación interna|Excelente para turbo|Más delicado de terminar|Turbo clásicos|
|Punzado|Código madre + patrón $P$|Elimina bits de salida|Adaptación flexible de tasa|Reduce distancia libre|Estándares con múltiples tasas|
|Turbo|Paralelo de dos RSC + interleaver|Decodificación iterativa|Muy cerca de capacidad|Latencia y complejidad iterativa|3G/4G, satélite, espacio profundo|

## 4.4.14 Ejemplos resueltos adicionales

**Ejemplo 4.45:** número de estados y complejidad.

Si un codificador binario tiene memoria $m=4$, entonces posee
$$
2^4=16
$$
estados. Viterbi debe mantener un superviviente por estado y por etapa, de modo que la complejidad crece exponencialmente con la memoria.

**Ejemplo 4.46:** tasa efectiva con bits de cola.

Supóngase un código de tasa nominal $1/2$, memoria $m=2$ y una trama de $L=100$ bits. Para volver al estado cero se añaden $m=2$ bits de cola. El número total de bits codificados es
$$
2(L+m)=2(102)=204.
$$
La tasa efectiva es
$$
R_{\text{ef}}=\frac{100}{204}\approx 0.4902.
$$
Se observa que la terminación reduce ligeramente la tasa real.

**Ejemplo 4.47:** métrica de rama euclidiana en BPSK.

Si una rama candidata del trellis transmite la palabra binaria $10$, su imagen BPSK puede tomarse como
$$
[-1,+1].
$$
Si el receptor observa
$$
\mathbf{y}=[-0.8,0.3],
$$
la métrica euclidiana es
$$
(-0.8+1)^2+(0.3-1)^2=0.04+0.49=0.53.
$$
Para la rama alternativa $01\mapsto [+1,-1]$,
$$
( -0.8-1)^2+(0.3+1)^2=3.24+1.69=4.93.
$$
Luego la primera rama es mucho más verosímil.

---

# Resumen de conceptos clave

- La representación vectorial de señales permite formular la detección óptima como un problema de distancia euclidiana.
- Gram-Schmidt produce bases ortonormales equivalentes y facilita el diseño de receptores correladores.
- La teoría de campos de Galois explica la construcción de $GF(p)$ y $GF(p^m)$, el papel de los elementos primitivos y de los polinomios mínimos.
- Los polinomios generadores de códigos cíclicos, BCH y Reed-Solomon se obtienen a partir de raíces en campos finitos.
- En un código lineal, la matriz generadora $G$ produce palabras válidas y la matriz de paridad $H$ permite calcular síndromes.
- La distancia mínima $d_{\min}$ gobierna la capacidad de detección y corrección en códigos de bloques.
- Los códigos Hamming son BCH de corrección simple; los BCH generalizan la corrección múltiple y los Reed-Solomon trabajan sobre símbolos de $GF(2^m)$.
- Los LDPC se describen con matrices dispersas y grafos de Tanner; los códigos polares se construyen por polarización de canal y potencias de Kronecker sobre $GF(2)$.
- Los códigos convolucionales introducen memoria; su descripción natural usa polinomios en el retardo $D$ sobre $GF(2)$.
- La distancia libre $d_{free}$ juega en códigos convolucionales el mismo papel que $d_{\min}$ en códigos de bloques.
- Los códigos RSC, punzados y turbo extienden la familia convolucional para ofrecer flexibilidad de tasa y ganancias iterativas cercanas a capacidad.

---

# Referencias

1. S. Lin y D. J. Costello, *Error Control Coding*, 2nd ed., Pearson, 2004.
2. F. J. MacWilliams y N. J. A. Sloane, *The Theory of Error-Correcting Codes*, North-Holland, 1977.
3. T. K. Moon, *Error Correction Coding: Mathematical Methods and Algorithms*, Wiley, 2005.
4. B. Sklar, *Digital Communications: Fundamentals and Applications*, 2nd ed., Prentice Hall, 2001.
5. J. G. Proakis y M. Salehi, *Digital Communications*, 5th ed., McGraw-Hill, 2008.
6. R. E. Blahut, *Algebraic Codes for Data Transmission*, Cambridge University Press, 2003.
7. S. B. Wicker y V. K. Bhargava (eds.), *Reed-Solomon Codes and Their Applications*, IEEE Press, 1994.
8. T. Richardson y R. Urbanke, *Modern Coding Theory*, Cambridge University Press, 2008.
9. E. Arıkan, “Channel Polarization: A Method for Constructing Capacity-Achieving Codes for Symmetric Binary-Input Memoryless Channels,” *IEEE Transactions on Information Theory*, vol. 55, no. 7, pp. 3051–3073, 2009.
10. C. Berrou, A. Glavieux y P. Thitimajshima, “Near Shannon Limit Error-Correcting Coding and Decoding: Turbo Codes,” *Proceedings of ICC*, 1993.
