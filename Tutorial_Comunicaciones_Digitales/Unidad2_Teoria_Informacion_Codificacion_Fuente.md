# Unidad 2: Teoría de Información y Codificación de Fuente

## Introducción de la unidad

La teoría de la información constituye uno de los pilares de las comunicaciones digitales modernas. Gracias a ella es posible responder preguntas fundamentales: ¿cuánta información produce una fuente?, ¿cuál es el límite último de compresión sin pérdida?, ¿qué tasa máxima puede transportar un canal con ruido?, ¿cómo debe diseñarse un receptor para minimizar errores? Esta unidad introduce, con enfoque pedagógico y matemático, los conceptos esenciales de **medida de información**, **entropía**, **codificación de fuente**, **PCM**, **capacidad de canal**, **detección digital óptima** y, como ampliación contemporánea, los fundamentos de la **teoría de la información semántica**.

El hilo conductor será el siguiente. Primero estudiaremos cómo cuantificar la incertidumbre y la información de una fuente discreta. Después analizaremos la conversión analógico-digital mediante **Pulse Code Modulation (PCM)**, enlazando el muestreo, la cuantización y la codificación binaria. Luego abordaremos el concepto de **capacidad de canal**, que fija el límite teórico de transmisión fiable. Más adelante estudiaremos los criterios óptimos de decisión en recepción digital, especialmente **máxima verosimilitud (ML)** y **máximo a posteriori (MAP)**. Finalmente, ampliaremos la discusión hacia la pregunta que Shannon deliberadamente dejó fuera de su formalismo: **¿qué ocurre cuando no basta con transmitir símbolos correctamente, sino que además importa transmitir significado?**

A lo largo del capítulo se empleará notación matemática en LaTeX y se incluirán ejemplos completamente resueltos en cada sección. El objetivo es que un estudiante principiante adquiera comprensión conceptual rigurosa y también habilidad operativa para resolver problemas. Se insistirá, además, en un aspecto crucial para las telecomunicaciones del futuro: la diferencia entre **información sintáctica** y **contenido semántico**.

> **Concepto clave:** en su formulación clásica, la teoría de Shannon cuantifica **incertidumbre estadística** y no **significado**. Esta distinción, lejos de ser una limitación menor, abre una línea completa de investigación que hoy reaparece en comunicaciones semánticas, inteligencia distribuida y redes 6G.

---

## 2.1 Medida de Información y Entropía

### 2.1.1 Concepto de información

En teoría de la información, la idea central es que la **información** está asociada a la **reducción de incertidumbre**. Un suceso muy improbable aporta más información cuando ocurre que un suceso casi seguro. Esta definición es deliberadamente operacional: no pregunta si el mensaje es importante, útil, verdadero o relevante, sino cuán inesperado resulta bajo un modelo probabilístico.

Supongamos una fuente discreta que emite un símbolo $x_i$ con probabilidad $p(x_i)$. Shannon propuso medir la información asociada a la ocurrencia del símbolo $x_i$ mediante la **autoinformación**:

$$
I(x_i) = -\log_b p(x_i)
$$

Donde:

- $p(x_i)$ es la probabilidad del suceso.
- $b$ es la base del logaritmo.
- Si $b = 2$, la unidad es el **bit**.
- Si $b = e$, la unidad es el **nat**.
- Si $b = 10$, la unidad es el **hartley** o dígito decimal.

#### Justificación de la forma logarítmica

La medida de información debe satisfacer propiedades intuitivas:

1. **Monotonía**: cuanto menor sea $p(x_i)$, mayor debe ser la información.
2. **Aditividad para sucesos independientes**: si dos sucesos independientes $x_i$ y $y_j$ ocurren conjuntamente, entonces
   $$
   I(x_i,y_j) = I(x_i) + I(y_j)
   $$
3. **Continuidad** con respecto a la probabilidad.
4. **Normalización razonable**: dos sucesos equiprobables de una elección binaria deben aportar 1 bit cada uno cuando $b=2$.

Si $x_i$ y $y_j$ son independientes:

$$
P(x_i,y_j) = P(x_i)P(y_j)
$$

Entonces, para que la información sea aditiva:

$$
I(x_i,y_j) = -\log_b [P(x_i)P(y_j)] = -\log_b P(x_i) - \log_b P(y_j)
$$

lo cual verifica la forma logarítmica.

Una lectura importante para el estudiante es la siguiente: el logaritmo transforma productos de probabilidades en sumas de informaciones. Por ello la medida de Shannon se adapta tan bien a procesos secuenciales, cadenas de símbolos y canales concatenados.

#### Propiedades de la autoinformación

- Si $p(x_i)=1$, entonces
  $$
  I(x_i)= -\log_2 1 = 0
  $$
  Un suceso seguro no aporta información nueva.

- Si $0<p(x_i)<1$, entonces $I(x_i)>0$.

- Si $p(x_i)$ disminuye, $I(x_i)$ aumenta.

- Si dos sucesos son equiprobables, aportan la misma autoinformación.

- Si un alfabeto es uniforme con $M$ símbolos, cada símbolo aporta
  $$
  I(x_i)=\log_2 M
  $$
  bits.

> **Concepto clave:** la información de Shannon no mide “importancia semántica”, sino **sorpresa probabilística**. Un mensaje gramaticalmente absurdo pero improbable puede tener gran autoinformación; un mensaje crucial pero perfectamente esperado puede tener autoinformación baja.

**[Figura 2.1]:** Curva de autoinformación $I(x)=-\log_2 p(x)$ en función de la probabilidad. La figura debe mostrar una curva decreciente y convexa: cuando $p(x)$ es cercana a 1, la información es casi nula; cuando $p(x)$ es pequeña, la información crece rápidamente. Debe añadirse una anotación comparando dos mensajes: uno altamente inesperado pero semánticamente trivial, y otro muy relevante pero esperado, para remarcar la diferencia entre sorpresa estadística y significado.

#### Ejemplo 2.1: Autoinformación de varios sucesos

Una fuente emite tres símbolos con probabilidades:

$$
p(a)=0.5, \qquad p(b)=0.25, \qquad p(c)=0.125
$$

Calcular la autoinformación de cada símbolo en bits.

**Solución:**

Para $a$:

$$
I(a)=-\log_2(0.5)=1 \text{ bit}
$$

Para $b$:

$$
I(b)=-\log_2(0.25)=2 \text{ bits}
$$

Para $c$:

$$
I(c)=-\log_2(0.125)=3 \text{ bits}
$$

**Conclusión:** el símbolo menos probable aporta más información. La dependencia es inversa respecto a la probabilidad y lineal respecto al logaritmo.

#### Ejemplo 2.2: Comparación entre sorpresa sintáctica y relevancia

Considérense dos mensajes en un sistema de monitoreo industrial:

- Mensaje A: “Temperatura normal: $25^\circ$C”, con probabilidad $0.95$.
- Mensaje B: “Fallo crítico en turbina”, con probabilidad $0.05$.

La autoinformación es:

$$
I(A)=-\log_2(0.95)\approx 0.074\text{ bits}
$$

$$
I(B)=-\log_2(0.05)\approx 4.322\text{ bits}
$$

Desde Shannon, el mensaje B transmite más información porque es menos probable. Sin embargo, este ejemplo también anticipa una discusión semántica: el valor operativo del mensaje no depende sólo de su rareza, sino de su **significado para la acción**.

---

### 2.1.2 Entropía de una fuente discreta

La autoinformación mide la información de un suceso concreto. Pero para caracterizar una **fuente** completa necesitamos el promedio estadístico de esa información. Esto conduce a la **entropía de Shannon**.

Sea una fuente discreta $X$ con alfabeto $\mathcal{X} = \{x_1,x_2,\dots,x_M\}$ y probabilidades $p(x_i)$. Su entropía se define como

$$
H(X) = -\sum_{i=1}^{M} p(x_i) \log_2 p(x_i)
$$

La entropía representa la **incertidumbre media** o la **información media por símbolo** emitido por la fuente.

#### Interpretación física y estadística

- Si la fuente es muy predecible, su entropía es baja.
- Si todos los símbolos son equiprobables, la incertidumbre es máxima.
- La entropía también establece el límite teórico de compresión sin pérdida promedio por símbolo.
- Desde una perspectiva operativa, una fuente con menor entropía admite representaciones más compactas.

La entropía puede interpretarse como la longitud promedio mínima ideal de una descripción binaria de los símbolos, si se permiten códigos suficientemente largos y eficientes.

#### Propiedades fundamentales

##### 1. No negatividad

$$
H(X) \ge 0
$$

con igualdad si y solo si la fuente es determinista.

##### 2. Entropía nula para fuente cierta

Si existe un símbolo $x_k$ tal que $p(x_k)=1$, entonces

$$
H(X)=0
$$

##### 3. Máximo para distribución uniforme

Si la fuente tiene $M$ símbolos y todos son equiprobables:

$$
p(x_i)=\frac{1}{M}, \qquad i=1,\dots,M
$$

entonces

$$
H(X)= -\sum_{i=1}^{M} \frac{1}{M}\log_2\left(\frac{1}{M}\right)
= -\log_2\left(\frac{1}{M}\right)=\log_2 M
$$

Por tanto,

$$
H(X) \le \log_2 M
$$

##### 4. Concavidad

La entropía es una función cóncava de la distribución de probabilidad. Esto significa que la mezcla de distribuciones aumenta la incertidumbre promedio.

##### 5. Aditividad para variables independientes

Si $X$ e $Y$ son independientes,

$$
H(X,Y)=H(X)+H(Y)
$$

##### 6. Continuidad

Pequeñas variaciones en las probabilidades producen pequeñas variaciones en la entropía. Esta propiedad es importante cuando se estiman probabilidades empíricas a partir de datos.

#### Demostración del máximo de entropía

Queremos maximizar

$$
H(X) = -\sum_{i=1}^{M} p_i \log_2 p_i
$$

sujeto a la restricción

$$
\sum_{i=1}^{M} p_i = 1
$$

Usando multiplicadores de Lagrange y trabajando con logaritmo natural:

$$
\mathcal{L} = -\sum_{i=1}^{M} p_i \ln p_i + \lambda \left(\sum_{i=1}^{M} p_i -1\right)
$$

Derivando respecto a $p_i$:

$$
\frac{\partial \mathcal{L}}{\partial p_i} = -(\ln p_i +1)+\lambda =0
$$

entonces

$$
\ln p_i = \lambda -1
$$

lo cual implica que todos los $p_i$ son iguales. Como suman 1,

$$
p_i = \frac{1}{M}
$$

Así se demuestra que la entropía máxima ocurre para distribución uniforme. El punto encontrado es máximo y no mínimo por la concavidad global de la entropía.

> **Concepto clave:** la entropía es máxima cuando el observador sabe menos sobre el resultado. Esta intuición volverá a aparecer en la sección 2.5, donde veremos que **máxima incertidumbre sintáctica** no equivale necesariamente a **máximo contenido semántico**.

**[Figura 2.2]:** Curva de entropía binaria $H_2(p) = -p\log_2 p -(1-p)\log_2(1-p)$ para $0\le p\le1$. La figura debe ser simétrica respecto a $p=0.5$, nula en $p=0$ y $p=1$, y máxima en $p=0.5$ con valor 1 bit. Conviene superponer una nota indicando que esta curva mide incertidumbre estadística pura y no la relevancia conceptual del evento observado.

#### Ejemplo 2.3: Entropía de una fuente binaria

Sea una fuente binaria con:

$$
p(0)=0.9, \qquad p(1)=0.1
$$

Calcular la entropía.

**Solución:**

$$
H(X)= -0.9\log_2(0.9)-0.1\log_2(0.1)
$$

Usando valores numéricos:

$$
\log_2(0.9)\approx -0.1520, \qquad \log_2(0.1)\approx -3.3219
$$

Entonces:

$$
H(X) \approx -0.9(-0.1520)-0.1(-3.3219)
$$

$$
H(X) \approx 0.1368+0.3322 = 0.4690 \text{ bits/símbolo}
$$

**Interpretación:** aunque la fuente es binaria, produce menos de 1 bit por símbolo en promedio porque es muy predecible.

#### Ejemplo 2.4: Entropía máxima

Una fuente cuaternaria tiene cuatro símbolos equiprobables. Calcular la entropía.

**Solución:**

$$
H(X)=\log_2 4=2 \text{ bits/símbolo}
$$

Este es el valor máximo posible para una fuente de cuatro símbolos.

#### Ejemplo 2.5: Entropía comparada de dos fuentes con igual alfabeto

Considérense dos fuentes cuaternarias:

- Fuente A: $\left(\frac{1}{4},\frac{1}{4},\frac{1}{4},\frac{1}{4}\right)$
- Fuente B: $(0.7,0.1,0.1,0.1)$

Para la fuente A:

$$
H_A=2\text{ bits/símbolo}
$$

Para la fuente B:

$$
H_B=-0.7\log_2 0.7-3(0.1\log_2 0.1)
$$

$$
H_B\approx 0.3602+0.9966=1.3568\text{ bits/símbolo}
$$

**Interpretación:** ambas fuentes usan el mismo alfabeto, pero la fuente B es más sesgada y por tanto menos incierta. La reducción de entropía indica también mayor potencial de compresión.

---

### 2.1.3 Incertidumbre y redundancia en la fuente

La **incertidumbre** está directamente asociada a la entropía. Sin embargo, en muchas fuentes reales existe estructura, repetición o sesgo estadístico. Esa parte “predecible” se denomina **redundancia**.

Si una fuente tiene $M$ símbolos, su entropía máxima es:

$$
H_{\max} = \log_2 M
$$

La **redundancia absoluta** puede definirse como:

$$
R_a = H_{\max} - H(X)
$$

La **redundancia relativa** o fracción redundante se expresa como:

$$
R_r = 1 - \frac{H(X)}{H_{\max}}
$$

Y la **eficiencia de la fuente** es:

$$
\eta = \frac{H(X)}{H_{\max}}
$$

con

$$
0 \le \eta \le 1
$$

#### Interpretación

- Si $\eta = 1$, la fuente es estadísticamente eficiente: no hay redundancia.
- Si $\eta < 1$, existe posibilidad de compresión.
- La redundancia es útil en algunos contextos: por ejemplo, mejora robustez o inteligibilidad, pero reduce eficiencia.
- En fuentes lingüísticas, la redundancia también ayuda a reconstruir mensajes ante errores, ruido o pérdidas.

En lenguaje humano, por ejemplo, letras y palabras no son equiprobables. Además, existen dependencias sintácticas y semánticas, lo que introduce alta redundancia.

Desde una perspectiva moderna, aquí aparece una conexión con la semántica: cierta redundancia sintáctica puede ser “ineficiente” para Shannon y, al mismo tiempo, extremadamente valiosa para preservar significado, contexto o inferencias.

> **Concepto clave:** la redundancia no siempre es un defecto. En sistemas humanos, biológicos y perceptuales, parte de la redundancia protege el contenido útil frente a ruido, ambigüedad o errores de interpretación.

#### Ejemplo 2.6: Redundancia de una fuente ternaria

Sea una fuente con tres símbolos y probabilidades:

$$
p(x_1)=0.5,\quad p(x_2)=0.3,\quad p(x_3)=0.2
$$

Calcular entropía, eficiencia y redundancia relativa.

**Solución:**

Primero, la entropía:

$$
H(X)= -0.5\log_2 0.5 -0.3\log_2 0.3 -0.2\log_2 0.2
$$

Valores aproximados:

$$
-0.5\log_2 0.5 = 0.5
$$

$$
-0.3\log_2 0.3 \approx 0.5211
$$

$$
-0.2\log_2 0.2 \approx 0.4644
$$

Por tanto:

$$
H(X) \approx 1.4855 \text{ bits/símbolo}
$$

La entropía máxima para $M=3$ es:

$$
H_{\max}=\log_2 3 \approx 1.5850
$$

Eficiencia:

$$
\eta = \frac{1.4855}{1.5850} \approx 0.9372
$$

Redundancia relativa:

$$
R_r = 1-0.9372 = 0.0628
$$

**Resultado:** la fuente tiene una redundancia relativa de aproximadamente $6.28\%$.

#### Ejemplo 2.7: Redundancia en una palabra codificada

Supóngase que una fuente emite 8 símbolos posibles, pero sólo 4 aparecen con frecuencia apreciable y las otras 4 son prácticamente imposibles. Si para simplificar consideramos una distribución uniforme sobre 4 símbolos efectivos, la entropía es:

$$
H(X)=\log_2 4=2\text{ bits/símbolo}
$$

Sin embargo, el alfabeto total tiene $M=8$, luego

$$
H_{\max}=\log_2 8=3\text{ bits/símbolo}
$$

La redundancia relativa resulta:

$$
R_r=1-\frac{2}{3}=\frac{1}{3}\approx 33.33\%
$$

**Lectura:** un tercio de la capacidad potencial del alfabeto no se utiliza de manera efectiva. Esta redundancia puede explotarse mediante codificación de fuente.

---

### 2.1.4 Entropía conjunta y condicional

En muchas aplicaciones interesa estudiar dos variables aleatorias conjuntamente, por ejemplo una fuente y su salida retardada, o la entrada y salida de un canal.

#### Entropía conjunta

Para dos variables discretas $X$ e $Y$ con distribución conjunta $p(x,y)$, la **entropía conjunta** se define como

$$
H(X,Y) = -\sum_x \sum_y p(x,y)\log_2 p(x,y)
$$

Mide la incertidumbre total del par $(X,Y)$.

#### Entropía condicional

La **entropía condicional** de $Y$ dado $X$ es

$$
H(Y|X)= -\sum_x \sum_y p(x,y)\log_2 p(y|x)
$$

Análogamente,

$$
H(X|Y)= -\sum_x \sum_y p(x,y)\log_2 p(x|y)
$$

Mide la incertidumbre residual sobre una variable cuando la otra es conocida.

#### Relación en cadena

Una identidad fundamental es:

$$
H(X,Y)=H(X)+H(Y|X)
$$

y también

$$
H(X,Y)=H(Y)+H(X|Y)
$$

**Demostración:**

Como

$$
p(x,y)=p(x)p(y|x)
$$

entonces

$$
\log_2 p(x,y)=\log_2 p(x)+\log_2 p(y|x)
$$

Sustituyendo en la definición de entropía conjunta:

$$
H(X,Y)= -\sum_x\sum_y p(x,y)[\log_2 p(x)+\log_2 p(y|x)]
$$

Separando términos:

$$
H(X,Y)= -\sum_x\sum_y p(x,y)\log_2 p(x) - \sum_x\sum_y p(x,y)\log_2 p(y|x)
$$

Como $\sum_y p(x,y)=p(x)$, el primer término queda:

$$
-\sum_x p(x)\log_2 p(x)=H(X)
$$

Y el segundo término es $H(Y|X)$. Por tanto:

$$
H(X,Y)=H(X)+H(Y|X)
$$

#### Propiedades importantes

- $H(Y|X) \le H(Y)$
- La igualdad ocurre si y solo si $X$ e $Y$ son independientes.
- Si $Y$ es una función determinista de $X$, entonces
  $$
  H(Y|X)=0
  $$
- En general, el conocimiento adicional no puede aumentar la incertidumbre promedio.

La relación entre entropía total e incertidumbre residual anticipa una analogía útil con la teoría semántica: conocer el **contexto** reduce la ambigüedad de interpretación, del mismo modo que una variable condicionante reduce entropía estadística.

#### Ejemplo 2.8: Entropía conjunta y condicional

Sea la distribución conjunta:

$$
p(0,0)=0.4, \quad p(0,1)=0.1, \quad p(1,0)=0.2, \quad p(1,1)=0.3
$$

Calcular $H(X)$, $H(Y)$, $H(X,Y)$ y $H(Y|X)$.

**Solución:**

Distribuciones marginales:

$$
p_X(0)=0.4+0.1=0.5, \qquad p_X(1)=0.2+0.3=0.5
$$

$$
p_Y(0)=0.4+0.2=0.6, \qquad p_Y(1)=0.1+0.3=0.4
$$

Entonces:

$$
H(X)= -0.5\log_2 0.5 -0.5\log_2 0.5 =1 \text{ bit}
$$

$$
H(Y)= -0.6\log_2 0.6 -0.4\log_2 0.4
$$

$$
H(Y)\approx 0.97095 \text{ bits}
$$

Ahora la entropía conjunta:

$$
H(X,Y)= -\sum p(x,y)\log_2 p(x,y)
$$

$$
H(X,Y)= -0.4\log_2 0.4 -0.1\log_2 0.1 -0.2\log_2 0.2 -0.3\log_2 0.3
$$

$$
H(X,Y) \approx 1.8464 \text{ bits}
$$

Finalmente:

$$
H(Y|X)=H(X,Y)-H(X)=1.8464-1=0.8464 \text{ bits}
$$

#### Ejemplo 2.9: Caso determinista

Sea $Y=X$ con $P(X=0)=0.7$ y $P(X=1)=0.3$. Entonces:

$$
H(Y|X)=0
$$

porque el conocimiento de $X$ determina completamente a $Y$. Sin embargo,

$$
H(Y)=H(X)=-0.7\log_2 0.7-0.3\log_2 0.3\approx 0.8813\text{ bits}
$$

**Interpretación:** la incertidumbre de $Y$ existe antes de observar $X$, pero desaparece después de condicionarla. Esta idea será esencial cuando discutamos cómo el contexto puede reducir incertidumbre semántica.

---

### 2.1.5 Canal simétrico binario (BSC)

El **canal simétrico binario** o **Binary Symmetric Channel (BSC)** es uno de los modelos más importantes en teoría de la información.

#### Modelo

La entrada del canal es binaria:

$$
X \in \{0,1\}
$$

La salida también es binaria:

$$
Y \in \{0,1\}
$$

El canal invierte el bit transmitido con probabilidad $p$ y lo entrega correctamente con probabilidad $1-p$.

#### Probabilidades de transición

$$
P(Y=1|X=0)=p, \qquad P(Y=0|X=1)=p
$$

$$
P(Y=0|X=0)=1-p, \qquad P(Y=1|X=1)=1-p
$$

Su matriz de transición es:

$$
P_{Y|X} =
\begin{bmatrix}
1-p & p \\
p & 1-p
\end{bmatrix}
$$

#### Interpretación

- Si $p=0$, el canal es perfecto.
- Si $p=0.5$, la salida es completamente aleatoria e independiente de la entrada.
- Si $p>0.5$, el canal es peor que lanzar una moneda, aunque en muchos casos puede reinterpretarse invirtiendo la salida.

El BSC es un modelo abstracto, pero extraordinariamente útil para comprender la relación entre probabilidad de error, incertidumbre residual e información transferida.

**[Figura 2.3]:** Diagrama del canal simétrico binario. La figura debe representar dos nodos de entrada (0 y 1) y dos nodos de salida (0 y 1), con flechas rectas etiquetadas con probabilidad $1-p$ y flechas cruzadas etiquetadas con probabilidad $p$. Conviene añadir una observación visual indicando que el canal preserva la “estructura sintáctica binaria”, aunque degrade la confiabilidad de los símbolos.

#### Distribución de salida del BSC

Si $P(X=0)=q$ y $P(X=1)=1-q$, entonces:

$$
P(Y=0)=q(1-p)+(1-q)p
$$

$$
P(Y=1)=qp+(1-q)(1-p)
$$

#### Ejemplo 2.10: Salida de un BSC

Sea un BSC con $p=0.1$ y una fuente de entrada con:

$$
P(X=0)=0.7, \qquad P(X=1)=0.3
$$

Calcular $P(Y=0)$ y $P(Y=1)$.

**Solución:**

$$
P(Y=0)=0.7(0.9)+0.3(0.1)=0.63+0.03=0.66
$$

$$
P(Y=1)=0.7(0.1)+0.3(0.9)=0.07+0.27=0.34
$$

#### Ejemplo 2.11: Incertidumbre residual en el BSC

Si $p=0.2$, la incertidumbre del canal condicionada a la entrada es

$$
H(Y|X)=H_2(0.2)
$$

$$
H_2(0.2)=-0.2\log_2 0.2-0.8\log_2 0.8\approx 0.7219\text{ bits}
$$

**Interpretación:** incluso conociendo el bit transmitido, la salida conserva una incertidumbre de $0.7219$ bits debido al ruido del canal.

---

### 2.1.6 Información mutua

La **información mutua** cuantifica cuánta información comparte una variable con otra. En comunicaciones, mide cuánta información sobre la entrada $X$ puede extraerse a partir de la salida $Y$.

Se define como:

$$
I(X;Y)= \sum_x \sum_y p(x,y) \log_2 \frac{p(x,y)}{p(x)p(y)}
$$

También puede escribirse como:

$$
I(X;Y)=H(X)-H(X|Y)
$$

$$
I(X;Y)=H(Y)-H(Y|X)
$$

$$
I(X;Y)=H(X)+H(Y)-H(X,Y)
$$

#### Interpretación

- $I(X;Y)=0$ si $X$ e $Y$ son independientes.
- Cuanto mayor es $I(X;Y)$, más informa $Y$ sobre $X$.
- En un canal ideal sin ruido, si $Y=X$, entonces
  $$
  I(X;Y)=H(X)
  $$

La información mutua es el puente natural entre el estudio de fuentes y el estudio de canales. Si la entropía mide incertidumbre en el origen, la información mutua mide la parte de esa incertidumbre que **sí logra preservarse** a través del medio de transmisión.

#### Demostración de la relación con entropías

Partiendo de

$$
I(X;Y)= \sum_{x,y} p(x,y)\log_2\frac{p(x,y)}{p(x)p(y)}
$$

como $p(x,y)=p(x|y)p(y)$,

$$
I(X;Y)=\sum_{x,y} p(x,y)\log_2\frac{p(x|y)}{p(x)}
$$

Separando:

$$
I(X;Y)=\sum_{x,y} p(x,y)\log_2 p(x|y) - \sum_{x,y} p(x,y)\log_2 p(x)
$$

Entonces:

$$
I(X;Y)= -H(X|Y)+H(X)
$$

es decir,

$$
I(X;Y)=H(X)-H(X|Y)
$$

#### Propiedades importantes

1. **Simetría**:
   $$
   I(X;Y)=I(Y;X)
   $$

2. **No negatividad**:
   $$
   I(X;Y)\ge 0
   $$

3. **Cota superior**:
   $$
   I(X;Y)\le \min\{H(X),H(Y)\}
   $$

4. **Interpretación como divergencia**:
   $$
   I(X;Y)=D\big(p(x,y)\,\|\,p(x)p(y)\big)
   $$
   es decir, la información mutua mide cuánto se aparta la distribución conjunta del caso de independencia.

#### Información mutua en un BSC

Para un BSC con probabilidad de cruce $p$:

$$
H(Y|X)=H_2(p)
$$

siendo

$$
H_2(p) = -p\log_2 p -(1-p)\log_2(1-p)
$$

Por tanto:

$$
I(X;Y)=H(Y)-H_2(p)
$$

Si además la entrada es equiprobable, entonces la salida también lo es y $H(Y)=1$, luego:

$$
I(X;Y)=1-H_2(p)
$$

> **Concepto clave:** en teoría semántica moderna, a veces interesa no sólo la información mutua entre símbolos transmitidos y recibidos, sino la información mutua entre **estados del mundo**, **conocimiento del receptor** y **acción resultante**. La teoría clásica ofrece la base estadística; la teoría semántica intenta extender el análisis hacia el significado.

#### Ejemplo 2.12: Información mutua en un BSC con entrada equiprobable

Sea un BSC con $p=0.1$. Hallar la información mutua si la entrada es equiprobable.

**Solución:**

Primero calculamos la entropía binaria del error:

$$
H_2(0.1)= -0.1\log_2 0.1 -0.9\log_2 0.9
$$

$$
H_2(0.1) \approx 0.4690
$$

Entonces:

$$
I(X;Y)=1-0.4690=0.5310 \text{ bits/uso de canal}
$$

#### Ejemplo 2.13: Canal inútil

Si $p=0.5$, entonces

$$
H_2(0.5)=1
$$

y por tanto, para entrada equiprobable,

$$
I(X;Y)=1-1=0
$$

**Interpretación:** la salida no aporta ninguna información sobre la entrada. El canal conserva símbolos físicos, pero destruye completamente la dependencia estadística útil.

---

### 2.1.7 Capacidad del canal simétrico binario

La **capacidad de canal** es la máxima información mutua sobre todas las distribuciones posibles de entrada:

$$
C = \max_{p(x)} I(X;Y)
$$

Para el BSC,

$$
C_{BSC}=1-H_2(p)
$$

#### Derivación

Para un BSC,

$$
I(X;Y)=H(Y)-H(Y|X)
$$

Como $H(Y|X)=H_2(p)$ no depende de la distribución de entrada, maximizar $I(X;Y)$ equivale a maximizar $H(Y)$.

La entropía de una variable binaria es máxima cuando la salida es equiprobable. En un BSC esto se consigue con entrada equiprobable:

$$
P(X=0)=P(X=1)=\frac{1}{2}
$$

Entonces:

$$
H(Y)=1
$$

y por tanto:

$$
C=1-H_2(p)
$$

#### Interpretación de casos límite

- Si $p=0$:
  $$
  C=1 \text{ bit/uso}
  $$
- Si $p=0.5$:
  $$
  C=0
  $$
- Si $0<p<0.5$, la capacidad disminuye con $p$.

El resultado expresa una idea esencial: el ruido resta capacidad no porque borre la existencia física del símbolo, sino porque incrementa la incertidumbre residual sobre él.

**[Figura 2.4]:** Capacidad del BSC $C=1-H_2(p)$ frente a la probabilidad de cruce $p$. La figura debe mostrar una curva que parte de 1 bit en $p=0$, desciende de forma suave y alcanza 0 en $p=0.5$. Debe añadirse una nota comparativa indicando que esta capacidad es puramente sintáctica: aun si el bit recibido fuese “suficiente” para inferir una decisión semántica, la teoría de Shannon seguiría midiendo únicamente confiabilidad simbólica.

#### Ejemplo 2.14: Capacidad de un BSC

Calcular la capacidad para $p=0.01$, $p=0.1$ y $p=0.2$.

**Solución:**

Para $p=0.01$:

$$
H_2(0.01)= -0.01\log_2 0.01 -0.99\log_2 0.99 \approx 0.0808
$$

$$
C \approx 1-0.0808 = 0.9192 \text{ bits/uso}
$$

Para $p=0.1$:

$$
H_2(0.1)\approx 0.4690
$$

$$
C \approx 0.5310 \text{ bits/uso}
$$

Para $p=0.2$:

$$
H_2(0.2)= -0.2\log_2 0.2 -0.8\log_2 0.8 \approx 0.7219
$$

$$
C \approx 0.2781 \text{ bits/uso}
$$

#### Ejemplo 2.15: Sensibilidad de capacidad al error

Determinar la variación aproximada de capacidad al pasar de $p=0.05$ a $p=0.15$.

$$
C(0.05)=1-H_2(0.05)
$$

Con

$$
H_2(0.05)\approx 0.2864 \Rightarrow C(0.05)\approx 0.7136
$$

Para $p=0.15$:

$$
H_2(0.15)\approx 0.6098 \Rightarrow C(0.15)\approx 0.3902
$$

Entonces la pérdida de capacidad es

$$
\Delta C\approx 0.7136-0.3902=0.3234\text{ bits/uso}
$$

**Lectura ingenieril:** un aumento moderado de la probabilidad de cruce puede producir una degradación sustancial de la tasa máxima fiable.

---

### 2.1.8 Síntesis conceptual de la sección 2.1

La sección 2.1 establece las bases cuantitativas de toda la teoría de comunicaciones:

- La **autoinformación** mide la sorpresa de un símbolo individual.
- La **entropía** mide la incertidumbre promedio de la fuente.
- La **redundancia** cuantifica cuán compresible o predecible es una fuente.
- La **entropía conjunta y condicional** permiten modelar dependencias.
- La **información mutua** mide la información transferida.
- La **capacidad** representa el límite último de transmisión fiable.

Además, se ha anticipado una idea central para esta unidad ampliada: estas magnitudes describen cómo se comportan los **símbolos**, pero no necesariamente cómo se conserva su **significado**. La teoría de la información semántica, que estudiaremos en la sección 2.5, puede entenderse como un intento de extender estas nociones hacia el plano del contenido, la verdad, la relevancia y la eficacia comunicativa.

---

## 2.2 Modulación por Codificación de Pulsos (PCM)

La **PCM (Pulse Code Modulation)** es el esquema clásico de digitalización de señales analógicas. Convierte una señal continua en el tiempo y en amplitud en una secuencia binaria mediante tres operaciones básicas:

1. **Muestreo**
2. **Cuantización**
3. **Codificación**

PCM es la base de numerosos sistemas digitales de voz, audio, instrumentación y comunicaciones.

Desde la perspectiva de teoría de la información, PCM transforma una fuente analógica en una representación discreta que puede ser tratada por métodos de compresión, detección y transmisión digital. Es, por tanto, un puente entre el mundo continuo de las señales físicas y el mundo discreto de los símbolos binarios.

---

### 2.2.1 Teorema de muestreo de Nyquist-Shannon

Sea $x(t)$ una señal de tiempo continuo con transformada de Fourier $X(f)$ estrictamente limitada en banda:

$$
X(f)=0 \quad \text{para} \quad |f|>W
$$

Entonces, $x(t)$ puede reconstruirse perfectamente a partir de sus muestras uniformes $x(nT_s)$ si la frecuencia de muestreo satisface

$$
f_s = \frac{1}{T_s} \ge 2W
$$

La cantidad

$$
f_N = 2W
$$

se denomina **frecuencia de Nyquist**.

#### Demostración en frecuencia

El muestreo ideal consiste en multiplicar la señal por un tren de impulsos:

$$
s(t)=\sum_{n=-\infty}^{\infty} \delta(t-nT_s)
$$

La señal muestreada es:

$$
x_s(t)=x(t)s(t)=\sum_{n=-\infty}^{\infty} x(nT_s)\delta(t-nT_s)
$$

La transformada de Fourier del tren de impulsos es:

$$
S(f)=\frac{1}{T_s}\sum_{k=-\infty}^{\infty} \delta(f-kf_s)
$$

Como la multiplicación en tiempo corresponde a convolución en frecuencia:

$$
X_s(f)=X(f) * S(f)=\frac{1}{T_s}\sum_{k=-\infty}^{\infty} X(f-kf_s)
$$

Esto significa que el espectro original se replica periódicamente cada $f_s$ Hz. Para evitar solapamiento entre réplicas debe cumplirse:

$$
f_s \ge 2W
$$

Si se cumple estrictamente, un filtro paso bajo ideal puede recuperar $X(f)$ y, por tanto, $x(t)$.

#### Fórmula de interpolación de Shannon

$$
x(t)=\sum_{n=-\infty}^{\infty} x(nT_s)\, \mathrm{sinc}\left(\frac{t-nT_s}{T_s}\right)
$$

con

$$
\mathrm{sinc}(u)=\frac{\sin(\pi u)}{\pi u}
$$

#### Condiciones del teorema

1. La señal debe ser estrictamente limitada en banda.
2. El muestreo debe ser uniforme.
3. La reconstrucción ideal requiere filtro ideal.
4. En la práctica se usa sobremuestreo y filtros antialiasing para aproximar estas condiciones.

#### Aliasing

Si $f_s<2W$, las réplicas espectrales se superponen. Este fenómeno se llama **aliasing**. Una vez que aparece, la distorsión es irreversible porque diferentes componentes espectrales quedan mezcladas.

En términos informacionales, el aliasing puede interpretarse como una pérdida irreversible de separabilidad entre componentes de la fuente. Una vez colapsadas dos contribuciones distintas sobre la misma representación muestreada, la incertidumbre original ya no puede resolverse.

**[Figura 2.5]:** Réplicas espectrales de una señal muestreada. La figura debe mostrar primero el espectro original limitado a $[-W,W]$ y después varias copias centradas en múltiplos de $f_s$. Debe incluir dos casos: uno con $f_s>2W$, sin superposición, y otro con $f_s<2W$, donde se observe aliasing. El objetivo pedagógico es visualizar por qué la frecuencia de muestreo mínima debe ser al menos el doble del ancho de banda y cómo una elección inadecuada destruye información recuperable.

#### Ejemplo 2.16: Frecuencia mínima de muestreo

Una señal de voz tiene ancho de banda de $3.4\,\text{kHz}$. Hallar la frecuencia mínima de muestreo.

**Solución:**

$$
f_s \ge 2W = 2(3.4\,\text{kHz}) = 6.8\,\text{kHz}
$$

En telefonía digital se adopta típicamente:

$$
f_s = 8\,\text{kHz}
$$

para dejar margen práctico de filtrado.

#### Ejemplo 2.17: Evaluación de aliasing

Una señal con ancho de banda $W=5\,\text{kHz}$ se muestrea a $f_s=8\,\text{kHz}$. Verificar si existe aliasing.

La condición de Nyquist exige:

$$
f_s\ge 2W=10\,\text{kHz}
$$

Como

$$
8\,\text{kHz}<10\,\text{kHz}
$$

**sí aparece aliasing**. En consecuencia, no es posible reconstruir perfectamente la señal original sin distorsión.

---

### 2.2.2 Muestreo ideal y práctico

#### Muestreo ideal

En el muestreo ideal, cada muestra es un impulso ponderado por el valor instantáneo de la señal:

$$
x_s(t)=\sum_{n=-\infty}^{\infty} x(nT_s)\delta(t-nT_s)
$$

Es un modelo matemático exacto, pero no realizable físicamente porque requeriría pulsos de duración nula.

#### Muestreo natural

En el muestreo natural, la señal se multiplica por un tren periódico de pulsos rectangulares de duración finita $\tau$. Se utiliza la función pulso rectangular $\Pi(t)$, definida como:

$$
\Pi(t)=\begin{cases}1,&|t|\le\tfrac{1}{2},\\0,&|t|>\tfrac{1}{2}.\end{cases}
$$

Con esta definición, el tren de pulsos es:

$$
p(t)=\sum_{n=-\infty}^{\infty} \Pi\left(\frac{t-nT_s}{\tau}\right)
$$

La señal muestreada natural es:

$$
x_n(t)=x(t)p(t)
$$

Durante cada pulso, la cima sigue la variación local de la señal analógica.

#### Muestreo flat-top o de techo plano

En este caso, el valor instantáneo de la señal en el instante de muestreo se mantiene constante durante un intervalo $\tau$. Se modela como una secuencia de pulsos rectangulares de amplitud constante por muestra.

Este tipo de muestreo es muy importante en circuitos de **sample-and-hold**.

#### Efecto del hold de orden cero

El muestreo flat-top introduce una respuesta en frecuencia adicional:

$$
H_0(f)=\tau\, \mathrm{sinc}(f\tau)e^{-j\pi f\tau}
$$

lo cual provoca una atenuación dependiente de la frecuencia conocida como **aperture effect** o efecto de apertura.

#### Comparación conceptual

- **Ideal**: exacto matemáticamente, no realizable.
- **Natural**: realizable, pero la muestra sigue variando dentro del pulso.
- **Flat-top**: práctico para ADC, introduce distorsión por retención.

En diseño real, el ingeniero balancea costo, complejidad y fidelidad. Lo importante es reconocer que toda implementación práctica sustituye el modelo ideal por una aproximación física cuya respuesta espectral debe ser compensada o tolerada.

**[Figura 2.6]:** Comparación entre muestreo ideal, natural y flat-top sobre una senoide. La figura debe mostrar la señal analógica original, impulsos ideales, pulsos naturales cuya parte superior sigue la señal, y pulsos flat-top con amplitud constante durante cada intervalo. El texto de la figura debe enfatizar que el muestreo práctico siempre implica aproximaciones físicas que afectan al espectro y a la fidelidad.

#### Ejemplo 2.18: Duración de muestra y efecto de apertura

Sea un sistema con $f_s=8\,\text{kHz}$ y duración de retención $\tau=10\,\mu s$. Evaluar el módulo del factor de retención a $f=3\,\text{kHz}$.

**Solución:**

$$
|H_0(f)| = \tau \left|\mathrm{sinc}(f\tau)\right|
$$

Calculamos:

$$
f\tau = 3000 \times 10^{-5} = 0.03
$$

Entonces:

$$
\mathrm{sinc}(0.03)=\frac{\sin(\pi\cdot0.03)}{\pi\cdot0.03} \approx 0.9985
$$

Por tanto, la atenuación es muy pequeña en esta frecuencia.

---

### 2.2.3 Cuantización lineal

Tras el muestreo, cada muestra aún puede tomar infinitos valores continuos. La **cuantización** aproxima cada muestra al nivel discreto más cercano.

#### Niveles de cuantización

Si el rango dinámico es $[V_{\min},V_{\max}]$ y se usan $L$ niveles uniformes, el paso de cuantización es:

$$
\Delta = \frac{V_{\max}-V_{\min}}{L}
$$

Si el número de bits por muestra es $n$, entonces

$$
L=2^n
$$

#### Regla de cuantización uniforme

Dada una muestra $x$, el cuantizador produce

$$
Q(x)=x_q
$$

siendo $x_q$ el nivel representativo más cercano.

#### Error de cuantización

El error es:

$$
e_q = x-x_q
$$

En cuantización uniforme ideal,

$$
-\frac{\Delta}{2} \le e_q \le \frac{\Delta}{2}
$$

Si se asume que el error es uniforme e independiente de la señal (hipótesis válida para señales suficientemente “ricas” y muchos niveles), entonces su potencia media es:

$$
\sigma_q^2 = E[e_q^2] = \frac{\Delta^2}{12}
$$

#### Tipos de cuantizador uniforme

- **Midrise**: no tiene nivel en cero.
- **Midtread**: sí tiene nivel en cero.

El cuantizador midtread es útil para señales con valores pequeños alrededor de cero.

> **Concepto clave:** al cuantizar, el sistema sustituye una variable continua por una variable discreta. Desde la teoría de la información, esto equivale a imponer un alfabeto finito; desde la óptica semántica, puede verse como una abstracción que conserva lo relevante y descarta detalle fino.

**[Figura 2.7]:** Característica entrada-salida de un cuantizador uniforme. La figura debe mostrar una curva escalonada que aproxima la recta ideal $y=x$. Es conveniente incluir una representación del error de cuantización como diferencia horizontal o vertical entre la señal real y el nivel asignado. La intuición visual es que la cuantización reemplaza un continuo por un conjunto finito de escalones.

#### Ejemplo 2.19: Paso de cuantización y error máximo

Un ADC cubre el rango $[-1\text{ V},1\text{ V}]$ con $n=3$ bits.

**Solución:**

Número de niveles:

$$
L=2^3=8
$$

Paso de cuantización:

$$
\Delta = \frac{1-(-1)}{8}=\frac{2}{8}=0.25\text{ V}
$$

Error máximo absoluto:

$$
|e_q|_{\max}=\frac{\Delta}{2}=0.125\text{ V}
$$

Varianza del ruido de cuantización:

$$
\sigma_q^2=\frac{\Delta^2}{12}=\frac{0.25^2}{12}=0.005208\text{ V}^2
$$

#### Ejemplo 2.20: Cuantización de una muestra

Sea el mismo cuantizador del ejemplo anterior y una muestra $x=0.33\text{ V}$. Si los niveles representativos son los puntos medios, el intervalo correspondiente es $[0.25,0.5)$ y el nivel representativo es

$$
x_q=0.375\text{ V}
$$

El error es

$$
e_q=x-x_q=0.33-0.375=-0.045\text{ V}
$$

El valor cumple la cota $|e_q|<0.125\text{ V}$.

---

### 2.2.4 Cuantización no lineal

La cuantización uniforme asigna el mismo paso $\Delta$ en todo el rango. Esto no es óptimo cuando la señal presenta alta concentración de valores pequeños, como ocurre en voz.

#### Motivación

Si la señal pasa mucho tiempo cerca de amplitudes bajas, una cuantización uniforme desperdicia niveles en amplitudes extremas y ofrece poca resolución relativa alrededor de cero. La solución es usar una cuantización de paso variable:

- pasos pequeños para amplitudes pequeñas,
- pasos grandes para amplitudes grandes.

Esto mejora la calidad perceptual para señales de amplia gama dinámica.

#### Enfoques

1. **Companding**: comprimir antes de cuantizar y expandir después.
2. **Cuantizador no uniforme directo**.

En PCM de voz se usa típicamente el primer enfoque.

#### Ventajas

- Mejor SQNR para señales débiles.
- Mejor aprovechamiento de niveles de cuantización.
- Adecuado para señales no uniformemente distribuidas.

La idea profunda es adaptar la precisión de representación a la estadística de la fuente. En otras palabras, se asignan más recursos donde la señal ocurre con mayor frecuencia o donde el error es perceptualmente más crítico.

#### Ejemplo 2.21: Razón conceptual para usar cuantización no lineal

Supóngase una señal de voz con la mayoría de muestras entre $-0.1$ y $0.1$, pero picos ocasionales hasta $\pm 1$.

**Explicación:**

Con cuantización uniforme, si el rango cubre $[-1,1]$, el paso mínimo está fijado por ese rango total. Muchas muestras pequeñas quedarán mal representadas relativamente. En cambio, si se comprime la señal antes de cuantizar, las amplitudes pequeñas quedan “expandidas” en la escala del cuantizador, obteniéndose menor error relativo en la región donde la señal pasa más tiempo.

---

### 2.2.5 Leyes de compresión: Ley-$\mu$ y Ley-A

Las leyes de compresión son funciones no lineales aplicadas antes de la cuantización. Después, en el receptor, se realiza la expansión inversa.

#### 2.2.5.1 Ley-$\mu$

Usada principalmente en Norteamérica y Japón.

Para una señal normalizada $x$ con $|x|\le 1$, la salida comprimida es:

$$
y = F_\mu(x)= \operatorname{sgn}(x)\,\frac{\ln(1+\mu |x|)}{\ln(1+\mu)}
$$

con $\mu>0$, típicamente:

$$
\mu = 255
$$

La expansión correspondiente es:

$$
x = F_\mu^{-1}(y)= \operatorname{sgn}(y)\,\frac{(1+\mu)^{|y|}-1}{\mu}
$$

##### Propiedades

- Para amplitudes pequeñas, la pendiente es alta: mayor resolución.
- Para amplitudes grandes, la compresión reduce el crecimiento.
- La transformación es impar y monótonamente creciente.

#### 2.2.5.2 Ley-A

Usada principalmente en Europa.

Para $|x|\le 1$,

$$
F_A(x)=
\begin{cases}
\operatorname{sgn}(x)\,\dfrac{A|x|}{1+\ln A}, & 0\le |x|<\dfrac{1}{A} \\
\operatorname{sgn}(x)\,\dfrac{1+\ln(A|x|)}{1+\ln A}, & \dfrac{1}{A}\le |x|\le 1
\end{cases}
$$

con valor típico:

$$
A=87.6
$$

La expansión inversa es:

$$
x=
\begin{cases}
\operatorname{sgn}(y)\,\dfrac{|y|(1+\ln A)}{A}, & 0\le |y|<\dfrac{1}{1+\ln A} \\
\operatorname{sgn}(y)\,\dfrac{1}{A}\exp\left(|y|(1+\ln A)-1\right), & \dfrac{1}{1+\ln A}\le |y|\le 1
\end{cases}
$$

#### Comparación entre Ley-$\mu$ y Ley-A

- Ambas mejoran la representación de señales débiles.
- La Ley-$\mu$ presenta una compresión más agresiva.
- La Ley-A tiene un tramo lineal alrededor del origen.

**[Figura 2.8]:** Curvas de compresión Ley-$\mu$ y Ley-A comparadas con la recta $y=x$. La figura debe mostrar que ambas leyes son más empinadas cerca del origen y se aplanan para amplitudes altas. Debe explicarse que esta forma geométrica traduce el principio de “más resolución donde la señal ocurre con mayor frecuencia”.

#### Ejemplo 2.22: Compresión con Ley-$\mu$

Sea $x=0.1$ y $\mu=255$. Calcular la amplitud comprimida.

**Solución:**

$$
y=\frac{\ln(1+255\cdot 0.1)}{\ln(256)}
$$

$$
y=\frac{\ln(26.5)}{\ln(256)}
$$

Con valores aproximados:

$$
\ln(26.5)\approx 3.2771, \qquad \ln(256)\approx 5.5452
$$

$$
y \approx 0.5910
$$

**Interpretación:** una amplitud pequeña de 0.1 se “expande” en el dominio comprimido hasta aproximadamente 0.591, mejorando su resolución tras cuantización uniforme.

#### Ejemplo 2.23: Compresión con Ley-A

Sea $x=0.01$ y $A=87.6$. Como

$$
\frac{1}{A}\approx 0.0114
$$

se cumple $|x|<1/A$, por lo que usamos el primer tramo:

$$
y = \frac{A|x|}{1+\ln A}
$$

$$
y = \frac{87.6\cdot 0.01}{1+\ln 87.6}
$$

$$
\ln 87.6 \approx 4.4728
$$

$$
y \approx \frac{0.876}{5.4728}\approx 0.1601
$$

---

### 2.2.6 Relación señal a ruido de cuantización (SQNR)

La **Signal-to-Quantization-Noise Ratio (SQNR)** es una métrica central en PCM. Se define como:

$$
\mathrm{SQNR}=\frac{P_s}{P_q}
$$

Donde:

- $P_s$ es la potencia media de la señal.
- $P_q$ es la potencia del ruido de cuantización.

En decibelios:

$$
\mathrm{SQNR}_{dB}=10\log_{10}\left(\frac{P_s}{P_q}\right)
$$

#### Caso de senoide a escala completa y cuantización uniforme

Para una senoide de amplitud pico $A$ ajustada al rango total del cuantizador:

$$
P_s = \frac{A^2}{2}
$$

Si el rango total es $[-A,A]$, entonces:

$$
\Delta = \frac{2A}{2^n}
$$

Ruido de cuantización:

$$
P_q = \frac{\Delta^2}{12} = \frac{1}{12}\left(\frac{2A}{2^n}\right)^2
$$

Entonces:

$$
\mathrm{SQNR}=\frac{A^2/2}{(4A^2)/(12\cdot 2^{2n})}
$$

$$
\mathrm{SQNR}=\frac{A^2}{2}\cdot \frac{12\cdot 2^{2n}}{4A^2}= \frac{3}{2}2^{2n}
$$

En decibelios:

$$
\mathrm{SQNR}_{dB}=10\log_{10}\left(\frac{3}{2}2^{2n}\right)
$$

$$
\mathrm{SQNR}_{dB}=10\log_{10}\left(\frac{3}{2}\right)+20n\log_{10}2
$$

Como

$$
10\log_{10}(3/2)\approx 1.76 \text{ dB}, \qquad 20\log_{10}2\approx 6.02 \text{ dB}
$$

resulta la fórmula clásica:

$$
\boxed{\mathrm{SQNR}_{dB} \approx 6.02n + 1.76}
$$

#### Interpretación

Cada bit adicional incrementa aproximadamente la SQNR en **6 dB**.

Este resultado muestra la conexión entre resolución binaria y calidad de representación. A mayor número de bits, menor incertidumbre residual debida a la discretización de amplitud.

#### Ejemplo 2.24: SQNR para varios números de bits

Calcular la SQNR ideal para $n=8$, $n=12$ y $n=16$ bits.

**Solución:**

Para $n=8$:

$$
\mathrm{SQNR}_{dB} \approx 6.02(8)+1.76=49.92\,\text{dB}
$$

Para $n=12$:

$$
\mathrm{SQNR}_{dB} \approx 6.02(12)+1.76=74.00\,\text{dB}
$$

Para $n=16$:

$$
\mathrm{SQNR}_{dB} \approx 6.02(16)+1.76=98.08\,\text{dB}
$$

#### Ejemplo 2.25: Bits requeridos para una SQNR objetivo

Si se desea una SQNR ideal de al menos $62\,\text{dB}$, aproximar el número mínimo de bits.

Usamos:

$$
6.02n+1.76\ge 62
$$

$$
6.02n\ge 60.24
$$

$$
n\ge 10.01
$$

Por tanto, se requieren al menos

$$
n=11\text{ bits}
$$

si se exige superar la cota con margen entero.

---

### 2.2.7 Codificación PCM completa

Un sistema PCM realiza la siguiente cadena funcional:

1. **Filtrado antialiasing**
2. **Muestreo**
3. **Compresión** (opcional)
4. **Cuantización**
5. **Codificación binaria**
6. **Transmisión**
7. **Decodificación**
8. **Expansión** (si hubo compresión)
9. **Reconstrucción analógica**

#### Secuencia matemática

Sea una señal analógica $x(t)$.

##### Paso 1: muestreo

$$
x[n]=x(nT_s)
$$

##### Paso 2: cuantización

$$
x_q[n]=Q(x[n])
$$

##### Paso 3: codificación binaria

Cada nivel cuantizado se asigna a una palabra binaria de $n$ bits.

Si hay $L=2^n$ niveles, la salida codificada es una secuencia digital de bits.

#### Ejemplo de tabla PCM

Para $n=3$ bits, una tabla posible de niveles y códigos es:

| Nivel | Código |
|---|---|
| 0 | 000 |
| 1 | 001 |
| 2 | 010 |
| 3 | 011 |
| 4 | 100 |
| 5 | 101 |
| 6 | 110 |
| 7 | 111 |

**[Figura 2.9]:** Diagrama de bloques completo de un sistema PCM. La figura debe incluir fuente analógica, filtro antialiasing, muestreador, compresor opcional, cuantizador, codificador, canal digital, decodificador, expansor y filtro de reconstrucción. La descripción debe remarcar que PCM transforma gradualmente la señal desde el dominio analógico al digital y después la reconstruye de forma aproximada, con errores dominados por muestreo no ideal y cuantización.

#### Ejemplo 2.26: Codificación PCM de una muestra

Sea un cuantizador uniforme de 3 bits sobre el rango $[0,1]$ V. Codificar la muestra $x=0.68$ V.

**Solución:**

Número de niveles:

$$
L=8
$$

Paso:

$$
\Delta = \frac{1-0}{8}=0.125\text{ V}
$$

Los intervalos son:

- $[0,0.125)$ nivel 0
- $[0.125,0.25)$ nivel 1
- $[0.25,0.375)$ nivel 2
- $[0.375,0.5)$ nivel 3
- $[0.5,0.625)$ nivel 4
- $[0.625,0.75)$ nivel 5
- $[0.75,0.875)$ nivel 6
- $[0.875,1]$ nivel 7

Como $0.68 \in [0.625,0.75)$, corresponde el nivel 5.

Código binario:

$$
5 \rightarrow 101
$$

Error máximo local, dependiendo del nivel representativo, del orden de $\pm 0.0625$ V.

#### Ejemplo 2.27: Cadena conceptual de información en PCM

Supóngase una señal analógica que, tras muestreo y cuantización, produce la secuencia de niveles $[3,5,4,6]$ en un cuantizador de 3 bits. La salida codificada es:

$$
3\to 011,\quad 5\to 101,\quad 4\to 100,\quad 6\to 110
$$

Por tanto, la trama binaria es

$$
011\,101\,100\,110
$$

**Interpretación:** PCM convierte amplitudes continuas en palabras binarias. Una vez hecho esto, todo el aparato de teoría de la información discreta puede aplicarse sobre la nueva secuencia simbólica.

---

### 2.2.8 Tasa de bits y ancho de banda de PCM

#### Tasa de bits

Si la frecuencia de muestreo es $f_s$ y cada muestra se codifica con $n$ bits, la tasa binaria es:

$$
R_b = n f_s \quad [\text{bit/s}]
$$

Si existen $m$ canales multiplexados por división en tiempo, entonces:

$$
R_b = m n f_s
$$

#### Ejemplo clásico de telefonía PCM

Para voz telefónica:

$$
f_s=8\,\text{kHz}, \qquad n=8
$$

Entonces:

$$
R_b=8 \times 8000 = 64\,\text{kbit/s}
$$

#### Ancho de banda de transmisión

El ancho de banda requerido depende del formato de línea y del pulso de transmisión. En un caso ideal de transmisión binaria base banda con pulsos NRZ, una estimación aproximada es:

$$
B \approx \frac{R_b}{2}
$$

Mientras que con otras formas de pulsos y criterios de Nyquist puede variar.

Más generalmente, si se utiliza señalización binaria ideal con conformación de Nyquist y factor de roll-off $\alpha$, el ancho de banda pasobanda mínimo relacionado con una tasa simbólica $R_s$ es:

$$
B = \frac{(1+\alpha)R_s}{2}
$$

Para PCM binario, usualmente $R_s=R_b$.

#### Ejemplo 2.28: Tasa de bits de un sistema PCM multicanal

Un sistema multiplexa 24 canales de voz, cada uno muestreado a $8\,\text{kHz}$ y cuantizado con 8 bits.

**Solución:**

Tasa por canal:

$$
R_{b,\text{canal}}=8\times 8000=64\,\text{kbit/s}
$$

Tasa total:

$$
R_b=24\times 64\,\text{kbit/s}=1536\,\text{kbit/s}=1.536\,\text{Mbit/s}
$$

Si se añade señalización o bits de sincronismo, la tasa real aumenta ligeramente.

#### Ejemplo 2.29: Estimación de ancho de banda

Si un sistema PCM transmite a

$$
R_b=2\,\text{Mbit/s}
$$

mediante pulsos NRZ, una estimación base banda del ancho de banda es

$$
B\approx \frac{R_b}{2}=1\,\text{MHz}
$$

Esta aproximación es útil para cálculos preliminares, aunque el diseño final depende de la forma de pulso y del espectro permitido.

---

### 2.2.9 Ejemplo integral de PCM

#### Ejemplo 2.30: Diseño básico de un sistema PCM

Se desea digitalizar una señal de audio limitada a $W=4\,\text{kHz}$ con cuantización uniforme de 10 bits y rango $[-2,2]$ V. Hallar:

1. frecuencia mínima de muestreo,
2. número de niveles,
3. paso de cuantización,
4. tasa de bits,
5. SQNR ideal para senoide a escala completa.

**Solución:**

1. Frecuencia mínima de muestreo:

$$
f_s\ge 2W = 8\,\text{kHz}
$$

2. Número de niveles:

$$
L=2^{10}=1024
$$

3. Paso de cuantización:

$$
\Delta = \frac{2-(-2)}{1024}=\frac{4}{1024}=3.90625\,\text{mV}
$$

4. Tasa binaria:

$$
R_b = nf_s = 10\times 8000 = 80\,\text{kbit/s}
$$

5. SQNR ideal:

$$
\mathrm{SQNR}_{dB}\approx 6.02(10)+1.76=61.96\,\text{dB}
$$

**Comentario final:** este ejemplo muestra la interdependencia entre muestreo, precisión de amplitud y caudal binario.

#### Ejemplo 2.31: Impacto de aumentar un bit adicional

Si el sistema anterior pasa de 10 a 11 bits, entonces:

- los niveles se duplican a
  $$
  L=2^{11}=2048
  $$
- el paso se reduce a
  $$
  \Delta=\frac{4}{2048}=1.953125\,\text{mV}
  $$
- la tasa aumenta a
  $$
  R_b=11\times 8000=88\,\text{kbit/s}
  $$
- la SQNR ideal sube aproximadamente 6 dB:
  $$
  \mathrm{SQNR}_{dB}\approx 68.0\,\text{dB}
  $$

**Conclusión:** más resolución mejora fidelidad, pero también incrementa el caudal requerido. Aquí reaparece el compromiso entre representación, compresión y recursos de transmisión.

---

## 2.3 Capacidad de Canal

La teoría de capacidad de canal responde a una pregunta decisiva: **¿cuál es la máxima tasa a la que se puede transmitir información con probabilidad de error arbitrariamente pequeña?** Claude Shannon respondió esta cuestión en 1948 y estableció los límites fundamentales que aún rigen el diseño de sistemas modernos.

La capacidad no es una tasa que dependa de un esquema particular, sino una propiedad del canal y de sus restricciones físicas. Por ello constituye un referente normativo para el diseño: ningún sistema real puede superar ese límite de forma sostenida y fiable.

---

### 2.3.1 Teorema de codificación de Shannon

#### Enunciado formal

Para un canal discreto sin memoria con capacidad $C$, se cumple:

1. Para toda tasa de transmisión $R < C$, existen códigos de longitud suficientemente grande tales que la probabilidad de error puede hacerse arbitrariamente pequeña.
2. Para toda tasa $R > C$, no existe ningún esquema de codificación que permita probabilidad de error arbitrariamente pequeña.

#### Interpretación

El teorema no dice cómo construir el mejor código de forma explícita, pero garantiza su existencia. Es un teorema de **posibilidad** y de **límite fundamental**.

#### Significado operacional

- **Por debajo de capacidad**: la transmisión fiable es teóricamente posible.
- **Por encima de capacidad**: la transmisión fiable es imposible.

#### Implicación histórica

Este resultado cambió toda la ingeniería de comunicaciones, pues demostró que el ruido no impone un error mínimo inevitable si se emplea suficiente redundancia de canal y códigos adecuados.

En términos conceptuales, Shannon mostró que la comunicación fiable puede separarse en gran medida del soporte físico mediante un diseño correcto del código. Este es uno de los resultados más profundos de toda la ingeniería moderna.

**[Figura 2.10]:** Representación conceptual del teorema de Shannon mediante una curva de probabilidad de error frente a la tasa normalizada $R/C$. La figura debe mostrar una región a la izquierda de $C$ donde el error puede tender a cero para códigos largos, y una región a la derecha donde no es posible. La interpretación visual debe subrayar la capacidad como frontera fundamental entre transmisión fiable e imposible.

#### Ejemplo 2.32: Interpretación de una capacidad dada

Un canal tiene capacidad $C=2\,\text{Mbit/s}$. Analizar si son teóricamente posibles las tasas $1.5$, $2$ y $2.5\,\text{Mbit/s}$.

**Solución:**

- Para $R=1.5<C$, la transmisión fiable es teóricamente posible.
- Para $R=2=C$, el caso límite es delicado; en la formulación clásica práctica se trabaja estrictamente con $R<C$.
- Para $R=2.5>C$, la transmisión fiable es imposible.

#### Ejemplo 2.33: Interpretación con margen de diseño

Si un enlace tiene capacidad estimada $C=10\,\text{Mbit/s}$, un diseño a $R=9\,\text{Mbit/s}$ deja margen para codificación práctica y pérdidas de implementación. Un diseño a $R=9.99\,\text{Mbit/s}$ puede ser teóricamente atractivo, pero será mucho más difícil de realizar con complejidad razonable. Esto muestra que la distancia a capacidad también es una métrica útil de ingeniería.

---

### 2.3.2 Capacidad de canal para canales AWGN

El canal **AWGN** (Additive White Gaussian Noise) es el modelo fundamental para enlaces con ruido térmico.

#### Modelo

La señal recibida es:

$$
r(t)=s(t)+n(t)
$$

Donde:

- $s(t)$ es la señal transmitida,
- $n(t)$ es ruido gaussiano blanco aditivo con densidad espectral bilateral $N_0/2$.

#### Fórmula de capacidad de Shannon-Hartley

Si el canal tiene ancho de banda $B$ y relación señal a ruido lineal $\mathrm{SNR}=S/N$, entonces su capacidad es:

$$
\boxed{C = B\log_2(1+\mathrm{SNR})}
$$

expresada en bit/s.

#### Derivación esquemática

La derivación rigurosa usa procesos gaussianos, discretización en dimensiones ortogonales y maximización de información mutua. La idea central es que un canal de ancho de banda $B$ durante un intervalo $T$ posee aproximadamente $2BT$ grados de libertad reales. Distribuyendo potencia de forma óptima sobre tales dimensiones y usando una entrada gaussiana, se obtiene la máxima información mutua:

$$
I = T B \log_2(1+\mathrm{SNR})
$$

Al dividir entre $T$ se llega a la capacidad por unidad de tiempo:

$$
C=B\log_2(1+\mathrm{SNR})
$$

#### Propiedades

1. La capacidad crece linealmente con $B$.
2. La capacidad crece logarítmicamente con la SNR.
3. Duplicar el ancho de banda duplica aproximadamente la capacidad si la SNR permanece constante.
4. Duplicar la SNR no duplica la capacidad; el crecimiento es sublineal.

Esto explica por qué el ancho de banda y la potencia no son recursos equivalentes: el primero entra linealmente, el segundo logarítmicamente.

#### Ejemplo 2.34: Capacidad AWGN

Sea un canal con:

$$
B=1\,\text{MHz}, \qquad \mathrm{SNR}=15\,\text{dB}
$$

Calcular la capacidad.

**Solución:**

Primero convertimos SNR a escala lineal:

$$
\mathrm{SNR}=10^{15/10}=31.6228
$$

Entonces:

$$
C = 10^6 \log_2(1+31.6228)
$$

$$
C = 10^6 \log_2(32.6228)
$$

Como

$$
\log_2(32.6228) \approx 5.028
$$

se obtiene:

$$
C \approx 5.028\times 10^6\,\text{bit/s}=5.028\,\text{Mbit/s}
$$

#### Ejemplo 2.35: Efecto de duplicar la SNR

Para el mismo ancho de banda $B=1\,\text{MHz}$, comparar capacidades para $\mathrm{SNR}=10$ y $\mathrm{SNR}=20$ en escala lineal.

$$
C_1=10^6\log_2(11)\approx 3.459\,\text{Mbit/s}
$$

$$
C_2=10^6\log_2(21)\approx 4.392\,\text{Mbit/s}
$$

Aunque la SNR se duplicó, la capacidad no se duplicó. Ésta es una consecuencia directa de la ley logarítmica.

---

### 2.3.3 Límite de Shannon

El **límite de Shannon** suele expresarse en términos de energía por bit y densidad espectral de ruido.

#### Relación entre SNR, capacidad y eficiencia espectral

La eficiencia espectral es:

$$
\eta = \frac{R}{B} \quad [\text{bit/s/Hz}]
$$

La SNR puede escribirse como:

$$
\mathrm{SNR} = \frac{S}{N} = \frac{E_b R}{N_0 B} = \frac{E_b}{N_0}\eta
$$

Sustituyendo en la fórmula de capacidad:

$$
\eta \le \log_2\left(1+\eta\frac{E_b}{N_0}\right)
$$

Esta expresión conecta eficiencia espectral y energía por bit.

#### Límite mínimo de $E_b/N_0$

Para eficiencias espectrales muy bajas ($\eta \to 0$), el mínimo valor teórico de energía por bit requerido es:

$$
\left(\frac{E_b}{N_0}\right)_{\min}=\ln 2 \approx 0.693
$$

En decibelios:

$$
10\log_{10}(\ln 2) \approx -1.59\,\text{dB}
$$

Este valor es el famoso **límite de Shannon** en potencia.

#### Interpretación

Ningún sistema de comunicación digital fiable puede operar por debajo de:

$$
\boxed{\frac{E_b}{N_0} = -1.59\,\text{dB}}
$$

cuando la eficiencia espectral tiende a cero.

#### Ejemplo 2.36: Cálculo de SNR a partir de $E_b/N_0$

Sea un sistema con eficiencia espectral:

$$
\eta = 2\,\text{bit/s/Hz}
$$

Si opera con

$$
\frac{E_b}{N_0}=6\,\text{dB}
$$

hallar la SNR.

**Solución:**

Convertimos $E_b/N_0$ a lineal:

$$
\frac{E_b}{N_0}=10^{6/10}=3.9811
$$

Entonces:

$$
\mathrm{SNR}=\eta \frac{E_b}{N_0}=2\times 3.9811=7.9622
$$

En decibelios:

$$
\mathrm{SNR}_{dB}=10\log_{10}(7.9622)\approx 9.01\,\text{dB}
$$

#### Ejemplo 2.37: Aproximación al límite fundamental

Si un sistema opera a $E_b/N_0=-1\,\text{dB}$ y muy baja eficiencia espectral, está aproximadamente a $0.59\,\text{dB}$ por encima del límite teórico:

$$
-1-(-1.59)=0.59\,\text{dB}
$$

Esto indica un diseño extremadamente eficiente desde el punto de vista energético.

---

### 2.3.4 Eficiencia espectral y compromiso potencia-ancho de banda

Todo sistema de comunicaciones enfrenta un compromiso esencial entre:

- **potencia transmitida**, y
- **ancho de banda ocupado**.

#### Eficiencia espectral

Definimos:

$$
\eta = \frac{R}{B}
$$

Una eficiencia espectral alta significa transmitir muchos bits por segundo por cada hercio disponible.

#### Compromiso fundamental

A partir de

$$
C=B\log_2(1+\mathrm{SNR})
$$

si queremos aumentar la tasa $R$, existen dos estrategias:

1. aumentar $B$,
2. aumentar SNR.

Pero:

- el ancho de banda suele ser un recurso escaso;
- aumentar la potencia incrementa consumo, interferencia y coste.

#### Forma en términos de $E_b/N_0$

De

$$
\eta = \log_2\left(1+\eta\frac{E_b}{N_0}\right)
$$

podemos despejar:

$$
\frac{E_b}{N_0} = \frac{2^{\eta}-1}{\eta}
$$

Esta expresión muestra que para altas eficiencias espectrales el requisito de energía por bit crece rápidamente.

#### Interpretación física

- En **región limitada por potencia**, conviene usar gran ancho de banda y baja eficiencia espectral.
- En **región limitada por ancho de banda**, se requiere mayor $E_b/N_0$ y modulaciones/códigos más eficientes espectralmente.

#### Ejemplo 2.38: Energía por bit requerida para una eficiencia dada

Calcular el mínimo $E_b/N_0$ teórico para:

1. $\eta=1$ bit/s/Hz,
2. $\eta=4$ bit/s/Hz.

**Solución:**

Usamos:

$$
\frac{E_b}{N_0}=\frac{2^{\eta}-1}{\eta}
$$

Para $\eta=1$:

$$
\frac{E_b}{N_0}=\frac{2^1-1}{1}=1
$$

En dB:

$$
0\,\text{dB}
$$

Para $\eta=4$:

$$
\frac{E_b}{N_0}=\frac{2^4-1}{4}=\frac{15}{4}=3.75
$$

En dB:

$$
10\log_{10}(3.75)\approx 5.74\,\text{dB}
$$

**Conclusión:** transmitir 4 bit/s/Hz exige bastante más energía por bit que transmitir 1 bit/s/Hz.

#### Ejemplo 2.39: Compromiso de diseño

Si un sistema debe duplicar su tasa y no puede aumentar potencia, una alternativa es duplicar aproximadamente el ancho de banda disponible. Esta estrategia suele aparecer en sistemas ultra-wideband y en arquitecturas donde el espectro es abundante pero la energía es crítica.

---

### 2.3.5 Plano de Shannon

El **plano de Shannon** representa la región teóricamente alcanzable en un gráfico de eficiencia espectral $\eta$ frente a $E_b/N_0$.

#### Ecuación límite

La frontera teórica está dada por:

$$
\eta = \log_2\left(1+\eta\frac{E_b}{N_0}\right)
$$

O equivalentemente:

$$
\frac{E_b}{N_0}=\frac{2^{\eta}-1}{\eta}
$$

#### Rasgos de la curva

- Cuando $\eta \to 0$,
  $$
  \frac{E_b}{N_0} \to \ln 2 \approx -1.59\,\text{dB}
  $$
- Cuando $\eta$ crece, el requisito de $E_b/N_0$ aumenta.
- La región factible está por encima de la curva.

#### Utilidad del plano

Permite comparar:

- modulación,
- codificación,
- rendimiento práctico,
- distancia al límite teórico.

**[Figura 2.11]:** Plano de Shannon con eje horizontal $E_b/N_0$ en dB y eje vertical eficiencia espectral $\eta$ en bit/s/Hz. La figura debe mostrar la curva límite, la asíntota de $-1.59$ dB cuando $\eta\to0$ y una región prohibida por debajo de la curva. La explicación debe destacar que todo sistema real opera por encima de esta frontera y que el objetivo del diseño moderno es acercarse a ella.

#### Ejemplo 2.40: Ubicación de un sistema en el plano de Shannon

Un sistema transmite a:

$$
R=6\,\text{Mbit/s}, \qquad B=2\,\text{MHz}
$$

con

$$
\frac{E_b}{N_0}=4\,\text{dB}
$$

Determinar su eficiencia espectral y comparar con el límite teórico.

**Solución:**

Eficiencia espectral:

$$
\eta = \frac{R}{B}=\frac{6\times10^6}{2\times10^6}=3\,\text{bit/s/Hz}
$$

Convertimos $E_b/N_0$ a lineal:

$$
\frac{E_b}{N_0}=10^{4/10}=2.5119
$$

El mínimo teórico para $\eta=3$ es:

$$
\frac{E_b}{N_0}_{\min}=\frac{2^3-1}{3}=\frac{7}{3}=2.3333
$$

En dB:

$$
10\log_{10}(2.3333)\approx 3.68\,\text{dB}
$$

El sistema opera a 4 dB, es decir, aproximadamente a:

$$
4-3.68=0.32\,\text{dB}
$$

por encima del límite teórico.

---

### 2.3.6 Síntesis de la sección 2.3

Los conceptos centrales son:

- La **capacidad** es un límite teórico absoluto.
- En AWGN,
  $$
  C=B\log_2(1+\mathrm{SNR})
  $$
- El **límite de Shannon** mínimo de energía por bit es $-1.59$ dB.
- Existe un compromiso inevitable entre **ancho de banda** y **potencia**.
- El **plano de Shannon** permite evaluar cuán cerca está un sistema real del óptimo teórico.

En conexión con la teoría semántica, conviene recordar que alcanzar capacidad sintáctica no garantiza transmitir “lo importante”. Un sistema puede ser casi óptimo en bits/s/Hz y, sin embargo, resultar ineficiente para tareas donde sólo interesa el significado final o la decisión contextual.

---

## 2.4 Detección Digital Óptima

La etapa de detección en el receptor digital decide qué símbolo fue transmitido a partir de una observación ruidosa. Esta decisión debe diseñarse de forma óptima según un criterio estadístico bien definido.

El receptor es el punto donde la incertidumbre del canal se transforma en una inferencia concreta. Por ello, la teoría de detección enlaza directamente con la información mutua y con la probabilidad de error.

---

### 2.4.1 Modelo del sistema de comunicación digital

Consideremos un sistema digital que transmite uno de $M$ símbolos posibles:

$$
\{s_1(t), s_2(t), \dots, s_M(t)\}, \qquad 0\le t\le T
$$

El canal AWGN produce una señal recibida:

$$
r(t)=s_i(t)+n(t)
$$

si se transmitió $s_i(t)$, donde $n(t)$ es ruido gaussiano blanco aditivo.

#### Representación vectorial

Expresando las señales sobre una base ortonormal $\{\phi_k(t)\}_{k=1}^{N}$:

$$
s_i(t)=\sum_{k=1}^{N} s_{ik}\phi_k(t)
$$

$$
r(t)=\sum_{k=1}^{N} r_k\phi_k(t)
$$

Entonces el problema se reduce a un modelo vectorial:

$$
\mathbf{r}=\mathbf{s}_i+\mathbf{n}
$$

con $\mathbf{n}$ gaussiano multivariante de media cero y covarianza proporcional a la identidad.

#### Receptor correlador / filtro casado

Las observaciones suficientes pueden obtenerse mediante correladores:

$$
r_k = \int_0^T r(t)\phi_k(t)dt
$$

Esto equivale a proyectar la señal recibida en el espacio de señales.

**[Figura 2.12]:** Modelo general de un receptor digital óptimo. La figura debe mostrar banco de correladores o filtros casados, muestreo de estadísticas suficientes, bloque de decisión y salida estimada. El texto debe explicar que el receptor transforma un problema continuo en tiempo en un problema geométrico en un espacio vectorial con ruido gaussiano.

#### Ejemplo 2.41: Modelo binario unidimensional

Supongamos dos señales antipodales en una dimensión:

$$
s_1=+A, \qquad s_2=-A
$$

La observación es:

$$
r=s_i+n
$$

con $n\sim \mathcal{N}(0,\sigma^2)$.

Este es el modelo más simple y servirá como base para los ejemplos posteriores.

---

### 2.4.2 Criterio de máxima verosimilitud (ML)

El criterio de **máxima verosimilitud** decide el símbolo que hace más probable la observación recibida.

#### Definición

Dada una observación $\mathbf{r}$, la regla ML es:

$$
\hat{s}_{ML}=\arg\max_{s_i} p(\mathbf{r}|s_i)
$$

Es decir, elegimos el símbolo cuya densidad condicional de la observación es mayor.

#### Derivación para canal AWGN

En AWGN, si se transmite $\mathbf{s}_i$, entonces

$$
\mathbf{r}=\mathbf{s}_i+\mathbf{n}
$$

con $\mathbf{n}\sim \mathcal{N}(\mathbf{0},\sigma^2\mathbf{I})$.

La densidad condicional es:

$$
p(\mathbf{r}|s_i)=\frac{1}{(2\pi\sigma^2)^{N/2}}\exp\left(-\frac{1}{2\sigma^2}\|\mathbf{r}-\mathbf{s}_i\|^2\right)
$$

Maximizar esta expresión equivale a maximizar su logaritmo:

$$
\ln p(\mathbf{r}|s_i)= -\frac{N}{2}\ln(2\pi\sigma^2)-\frac{1}{2\sigma^2}\|\mathbf{r}-\mathbf{s}_i\|^2
$$

El primer término no depende de $i$, así que la decisión ML equivale a:

$$
\hat{s}_{ML}=\arg\min_{s_i}\|\mathbf{r}-\mathbf{s}_i\|^2
$$

#### Interpretación geométrica

En AWGN, el detector ML elige el punto de la constelación **más cercano en distancia euclídea** a la observación recibida.

#### Forma expandida

Como

$$
\|\mathbf{r}-\mathbf{s}_i\|^2 = \|\mathbf{r}\|^2 -2\mathbf{r}\cdot \mathbf{s}_i + \|\mathbf{s}_i\|^2
$$

si todas las señales tienen la misma energía, el término $\|\mathbf{s}_i\|^2$ también es constante y la regla se reduce a:

$$
\hat{s}_{ML}=\arg\max_{s_i}\, \mathbf{r}\cdot \mathbf{s}_i
$$

Es decir, elegir la señal con mayor correlación con la observación.

**[Figura 2.13]:** Interpretación geométrica del criterio ML en el espacio de señales. La figura debe mostrar varios puntos de constelación, una observación ruidosa y regiones de Voronoi definidas por distancia euclídea. La descripción debe enfatizar que el detector ML elige el símbolo más próximo geométricamente a la muestra recibida.

#### Ejemplo 2.42: ML para señales binarias antipodales

Sean dos símbolos:

$$
s_1=+1, \qquad s_2=-1
$$

Se observa $r=0.2$. Decidir por ML.

**Solución:**

Calculamos las distancias:

$$
(r-s_1)^2=(0.2-1)^2=0.64
$$

$$
(r-s_2)^2=(0.2+1)^2=1.44
$$

Como $0.64<1.44$, se decide:

$$
\hat{s}_{ML}=s_1
$$

Equivalentemente, el umbral está en cero: si $r>0$, decidir $+1$; si $r<0$, decidir $-1$.

#### Ejemplo 2.43: ML en 2 dimensiones

Si una constelación tiene puntos $\mathbf{s}_1=(1,1)$ y $\mathbf{s}_2=(-1,1)$ y la observación es $\mathbf{r}=(0.2,0.8)$, las distancias cuadráticas son:

$$
\|\mathbf{r}-\mathbf{s}_1\|^2=(0.2-1)^2+(0.8-1)^2=0.64+0.04=0.68
$$

$$
\|\mathbf{r}-\mathbf{s}_2\|^2=(0.2+1)^2+(0.8-1)^2=1.44+0.04=1.48
$$

Se elige $\mathbf{s}_1$. El ejemplo ilustra que ML conserva la misma lógica en cualquier dimensión.

---

### 2.4.3 Criterio de máximo a posteriori (MAP)

El criterio **MAP** incorpora no sólo la verosimilitud del canal, sino también las probabilidades a priori de los símbolos.

#### Definición

La regla MAP es:

$$
\hat{s}_{MAP}=\arg\max_{s_i} P(s_i|\mathbf{r})
$$

Usando Bayes:

$$
P(s_i|\mathbf{r}) = \frac{p(\mathbf{r}|s_i)P(s_i)}{p(\mathbf{r})}
$$

Como $p(\mathbf{r})$ no depende de $i$, la regla equivale a:

$$
\hat{s}_{MAP}=\arg\max_{s_i} p(\mathbf{r}|s_i)P(s_i)
$$

Tomando logaritmos:

$$
\hat{s}_{MAP}=\arg\max_{s_i}\left[\ln p(\mathbf{r}|s_i)+\ln P(s_i)\right]
$$

#### Caso AWGN

Sustituyendo la densidad gaussiana:

$$
\hat{s}_{MAP}=\arg\min_{s_i}\left[\|\mathbf{r}-\mathbf{s}_i\|^2 - 2\sigma^2 \ln P(s_i)\right]
$$

Esta expresión muestra que el MAP corrige la distancia euclídea según las probabilidades a priori.

#### Interpretación

- Si un símbolo es más probable a priori, el receptor necesita menos evidencia para decidirlo.
- El MAP minimiza la **probabilidad de error promedio** cuando las probabilidades a priori son conocidas.

**[Figura 2.14]:** Regiones de decisión MAP para dos símbolos con probabilidades a priori desiguales. La figura debe mostrar dos puntos de señal y un umbral desplazado hacia el símbolo menos probable. El objetivo visual es explicar que el símbolo más probable “gana territorio” en el espacio de decisión, reduciendo el error promedio global.

#### Ejemplo 2.44: MAP para símbolos binarios con priori desiguales

Sean:

$$
s_1=+1, \qquad s_2=-1
$$

con probabilidades:

$$
P(s_1)=0.8, \qquad P(s_2)=0.2
$$

ruido gaussiano $n\sim \mathcal{N}(0,\sigma^2)$ con $\sigma^2=0.25$.

Hallar el umbral MAP.

**Solución:**

Decidimos $s_1$ si:

$$
p(r|s_1)P(s_1) > p(r|s_2)P(s_2)
$$

Tomando logaritmos y sustituyendo densidades gaussianas:

$$
-\frac{(r-1)^2}{2\sigma^2}+\ln 0.8 > -\frac{(r+1)^2}{2\sigma^2}+\ln 0.2
$$

Reordenando:

$$
\frac{(r+1)^2-(r-1)^2}{2\sigma^2} > \ln\left(\frac{0.8}{0.2}\right)
$$

Como

$$
(r+1)^2-(r-1)^2 = 4r
$$

queda:

$$
\frac{4r}{2\sigma^2} > \ln 4
$$

Con $\sigma^2=0.25$:

$$
\frac{4r}{0.5} > 1.3863
$$

$$
8r > 1.3863
$$

$$
r > 0.1733
$$

**Resultado:** el umbral MAP es $0.1733$, desplazado hacia la derecha respecto al umbral ML (que sería 0). Como $s_1$ es más probable, se favorece su decisión.

---

### 2.4.4 Relación entre ML y MAP (caso equiprobable)

Si todos los símbolos son equiprobables,

$$
P(s_i)=\frac{1}{M}
$$

entonces $\ln P(s_i)$ es el mismo para todos los $i$, por lo que no afecta a la decisión MAP. En consecuencia:

$$
\boxed{\text{MAP} \equiv \text{ML} \quad \text{si los símbolos son equiprobables}}
$$

#### Consecuencia práctica

En muchos problemas introductorios se asume equiprobabilidad, por lo que basta con aplicar ML. Sin embargo, en sistemas reales con fuentes sesgadas o decisiones secuenciales, MAP suele ser más adecuado.

#### Ejemplo 2.45: Equivalencia ML/MAP

Sean tres símbolos equiprobables transmitidos por AWGN. ¿Cambiaría la regla de decisión al pasar de ML a MAP?

**Solución:**

No. Al ser todos equiprobables:

$$
P(s_1)=P(s_2)=P(s_3)=\frac{1}{3}
$$

los factores a priori son constantes y el criterio MAP se reduce exactamente al ML.

---

### 2.4.5 Regiones de decisión óptimas

Las **regiones de decisión** son subconjuntos del espacio de observaciones donde el receptor decide cada símbolo.

#### Definición formal

La región de decisión asociada a $s_i$ es:

$$
\mathcal{R}_i = \left\{\mathbf{r}: p(\mathbf{r}|s_i)P(s_i) \ge p(\mathbf{r}|s_j)P(s_j), \; \forall j\neq i \right\}
$$

En AWGN equiprobable, estas regiones son celdas de Voronoi respecto a distancia euclídea.

#### Fronteras de decisión

Para dos señales $\mathbf{s}_i$ y $\mathbf{s}_j$, la frontera ML satisface:

$$
\|\mathbf{r}-\mathbf{s}_i\|^2 = \|\mathbf{r}-\mathbf{s}_j\|^2
$$

Expandiendo:

$$
\mathbf{r}\cdot(\mathbf{s}_i-\mathbf{s}_j)=\frac{1}{2}\left(\|\mathbf{s}_i\|^2-\|\mathbf{s}_j\|^2\right)
$$

Esta es la ecuación de un hiperplano perpendicular al segmento que une ambos puntos de señal.

Para MAP, la frontera se modifica a:

$$
\|\mathbf{r}-\mathbf{s}_i\|^2 -2\sigma^2\ln P(s_i)= \|\mathbf{r}-\mathbf{s}_j\|^2 -2\sigma^2\ln P(s_j)
$$

#### Ejemplo 2.46: Región de decisión binaria

Con símbolos antipodales $s_1=+A$ y $s_2=-A$, equiprobables, la frontera ML es:

$$
(r-A)^2=(r+A)^2
$$

Desarrollando:

$$
r^2-2Ar+A^2 = r^2+2Ar+A^2
$$

$$
-2Ar=2Ar \Rightarrow r=0
$$

Por tanto:

- si $r>0$, decidir $s_1$,
- si $r<0$, decidir $s_2$.

Esta es la región óptima unidimensional.

---

### 2.4.6 Probabilidad de error

La **probabilidad de error** cuantifica el rendimiento del detector.

#### Definición general

Para decisiones sobre símbolos:

$$
P_e = P(\hat{s} \ne s)
$$

#### Caso binario antipodal en AWGN

Sea el modelo:

$$
r = \pm A + n, \qquad n\sim \mathcal{N}(0,\sigma^2)
$$

con símbolos equiprobables y umbral en cero.

Si se transmite $+A$, ocurre error si $r<0$, es decir, si:

$$
A+n<0 \Rightarrow n<-A
$$

Luego:

$$
P(e|s_1)=P(n<-A)
$$

Como $n$ es gaussiano:

$$
P(e|s_1)=Q\left(\frac{A}{\sigma}\right)
$$

Por simetría:

$$
P(e|s_2)=Q\left(\frac{A}{\sigma}\right)
$$

Y la probabilidad total de error es:

$$
\boxed{P_e = Q\left(\frac{A}{\sigma}\right)}
$$

Donde la función Q se define como:

$$
Q(x)=\frac{1}{\sqrt{2\pi}}\int_x^{\infty} e^{-u^2/2}du
$$

#### Expresión en términos de energía

Para BPSK, si la energía por bit es $E_b$, se obtiene:

$$
P_b = Q\left(\sqrt{\frac{2E_b}{N_0}}\right)
$$

#### Interpretación

- A mayor distancia entre señales, menor error.
- A mayor ruido, mayor error.
- La geometría del espacio de señales determina el rendimiento.

**[Figura 2.15]:** Distribuciones gaussianas superpuestas en la variable de decisión para señales binarias antipodales. La figura debe mostrar dos campanas centradas en $+A$ y $-A$, separadas por un umbral en 0. Las áreas de cola que cruzan el umbral representan la probabilidad de error. Esta imagen es esencial para comprender la relación entre distancia entre símbolos y BER.

#### Ejemplo 2.47: Probabilidad de error binaria

Sea un sistema binario antipodal con:

$$
A=1, \qquad \sigma=0.5
$$

Calcular la probabilidad de error.

**Solución:**

$$
P_e = Q\left(\frac{1}{0.5}\right)=Q(2)
$$

De tablas de la función Q:

$$
Q(2)\approx 0.0228
$$

Luego:

$$
P_e \approx 2.28\%
$$

#### Ejemplo 2.48: BER de BPSK en términos de $E_b/N_0$

Calcular la BER ideal de BPSK para:

$$
\frac{E_b}{N_0}=6\,\text{dB}
$$

**Solución:**

Pasamos a escala lineal:

$$
\frac{E_b}{N_0}=10^{6/10}=3.9811
$$

Entonces:

$$
P_b = Q\left(\sqrt{2\cdot 3.9811}\right)=Q(2.822)
$$

Usando tablas o aproximación numérica:

$$
Q(2.822) \approx 0.0024
$$

Por tanto:

$$
P_b \approx 2.4\times10^{-3}
$$

---

### 2.4.7 Ejemplo integrado de detección binaria

#### Ejemplo 2.49: Comparación ML y MAP en un caso concreto

Considérese un sistema binario con:

$$
s_1=+2, \qquad s_2=-2
$$

ruido gaussiano con varianza:

$$
\sigma^2=1
$$

probabilidades a priori:

$$
P(s_1)=0.9, \qquad P(s_2)=0.1
$$

Se recibe:

$$
r=0.3
$$

Determinar la decisión por ML y por MAP.

**Solución ML:**

Comparamos distancias:

$$
(r-2)^2=(0.3-2)^2=2.89
$$

$$
(r+2)^2=(0.3+2)^2=5.29
$$

Luego:

$$
\hat{s}_{ML}=s_1
$$

**Solución MAP:**

Comparamos:

$$
p(r|s_1)P(s_1) \quad \text{vs} \quad p(r|s_2)P(s_2)
$$

Usamos forma logarítmica:

$$
-\frac{(r-2)^2}{2}+\ln 0.9 \quad \text{vs} \quad -\frac{(r+2)^2}{2}+\ln 0.1
$$

Calculamos:

$$
-\frac{2.89}{2}+\ln 0.9 \approx -1.445 -0.1054 = -1.5504
$$

$$
-\frac{5.29}{2}+\ln 0.1 \approx -2.645 -2.3026 = -4.9476
$$

Como $-1.5504 > -4.9476$,

$$
\hat{s}_{MAP}=s_1
$$

**Comentario:** en este caso ambos coinciden, pero MAP favorece aún más al símbolo más probable.

---

### 2.4.8 Síntesis de la sección 2.4

- El receptor digital óptimo se formula como un problema estadístico de decisión.
- En AWGN, el criterio **ML** equivale a minimizar distancia euclídea.
- El criterio **MAP** añade las probabilidades a priori y minimiza la probabilidad de error promedio.
- Si los símbolos son equiprobables, **ML y MAP coinciden**.
- Las regiones de decisión óptimas se interpretan geométricamente.
- La probabilidad de error en sistemas binarios gaussianos se expresa mediante la función $Q$.

Desde la perspectiva semántica, esta sección deja una pregunta abierta: el detector clásico decide cuál símbolo fue transmitido. Pero en sistemas cognitivos o semánticos podría interesar, más bien, decidir **qué intención**, **qué estado del entorno** o **qué acción** debe inferirse, incluso si no todos los bits se recuperan exactamente. Esta idea reaparecerá en la sección 2.5.

---

## 2.5 Teoría de Información Semántica

La teoría clásica de Shannon resolvió magistralmente el problema técnico de cuantificar, comprimir y transmitir símbolos bajo incertidumbre. Sin embargo, el propio Shannon advirtió que los aspectos semánticos de la comunicación eran “irrelevantes para el problema de ingeniería” que él deseaba resolver. Esa exclusión metodológica fue extraordinariamente fecunda: permitió desarrollar una teoría general, elegante y aplicable. Pero también dejó abierta una cuestión profunda: **¿cómo medir la información cuando lo que importa no es sólo la señal, sino su significado?**

Esta sección introduce la **teoría de la información semántica** como una extensión conceptual del marco clásico. No reemplaza a Shannon, sino que lo complementa. En lugar de preguntar sólo “¿cuántos bits se transmiten?”, pregunta también “¿qué contenido verdadero, relevante o útil se comunica?”. Esta distinción es especialmente importante en redes inteligentes, sistemas autónomos, internet táctil, percepción distribuida y comunicaciones semánticas de próxima generación.

---

### 2.5.1 Contexto histórico: los niveles de comunicación de Shannon y Weaver

En la formulación clásica, Shannon estudió el problema técnico de reconstruir mensajes a la salida de un canal con la mayor fidelidad posible. Poco después, **Warren Weaver** destacó que la comunicación puede analizarse en tres niveles:

1. **Nivel técnico**: con qué precisión se transmiten los símbolos.
2. **Nivel semántico**: con qué precisión transmiten los símbolos el significado deseado.
3. **Nivel de efectividad**: con qué eficacia el mensaje produce la conducta o acción esperada en el destinatario.

En notación esquemática:

$$
\text{Símbolos} \longrightarrow \text{Significado} \longrightarrow \text{Acción}
$$

La teoría de Shannon cubre de forma rigurosa el primer nivel. Los niveles segundo y tercero requieren modelar contexto, interpretación, conocimiento previo, verdad, relevancia y decisión.

> **Concepto clave:** Shannon resolvió el problema **técnico** de la comunicación; la teoría semántica intenta formalizar los niveles **semántico** y, en parte, **pragmático** o de efectividad.

#### Conexión con la teoría clásica

- La **entropía de Shannon** mide incertidumbre sobre símbolos.
- La **información semántica** intenta medir reducción de incertidumbre sobre estados del mundo, proposiciones verdaderas o tareas relevantes.
- La **información mutua** clásica cuantifica dependencia estadística; su contraparte semántica busca cuantificar dependencia **significativa**.

**[Figura 2.16]:** Diagrama de tres niveles de comunicación inspirado en Weaver. La figura debe mostrar una fuente, un transmisor, un canal y un receptor para el nivel técnico; encima, una capa de “significado” que conecta intención del emisor e interpretación del receptor; y finalmente una capa de “efectividad” vinculada con acción, decisión o cambio de estado. Debe resaltarse que la teoría de Shannon modela rigurosamente la capa inferior, mientras que la teoría semántica amplía el análisis hacia las capas superiores.

---

### 2.5.2 Carnap y Bar-Hillel: teoría lógica de la información semántica

En 1952, **Rudolf Carnap** y **Yehoshua Bar-Hillel** propusieron una teoría formal de información semántica basada en lógica y probabilidad. Su idea central era que una proposición informa en la medida en que **excluye posibilidades**.

#### Universo de estados posibles

Supóngase un conjunto finito de mundos o estados posibles:

$$
\Omega = \{\omega_1,\omega_2,\dots,\omega_N\}
$$

Una proposición $\varphi$ será verdadera en un subconjunto de esos mundos:

$$
[\varphi] \subseteq \Omega
$$

La **probabilidad lógica** de la proposición se define como la proporción de mundos en que resulta verdadera:

$$
P_L(\varphi)=\frac{|[\varphi]|}{|\Omega|}
$$

si todos los mundos son considerados inicialmente equiprobables. Más generalmente, puede definirse una medida lógica sobre $\Omega$.

#### Contenido semántico como exclusión de posibilidades

Cuanto menos mundos satisfacen $\varphi$, más restrictiva es la proposición y mayor es su contenido. La medida de contenido semántico se define análogamente a Shannon como:

$$
\operatorname{Cont}(\varphi)=-\log P_L(\varphi)
$$

Si $\varphi$ es una tautología, entonces $P_L(\varphi)=1$ y

$$
\operatorname{Cont}(\varphi)=0
$$

Si $\varphi$ es más específica, su probabilidad lógica disminuye y su contenido aumenta.

#### Paradoja de las contradicciones

Aquí aparece una dificultad clásica. Si $\varphi$ es una contradicción, entonces

$$
P_L(\varphi)=0
$$

por lo que formalmente

$$
\operatorname{Cont}(\varphi)=\infty
$$

Esto parece problemático, porque una contradicción no comunica contenido verdadero útil. Esta objeción fue uno de los grandes límites del modelo original y motivó desarrollos posteriores, entre ellos la teoría de Floridi.

> **Concepto clave:** Carnap y Bar-Hillel conectaron el contenido semántico con la **exclusión lógica de posibilidades**. Su marco es elegante, pero necesita distinguir entre meramente ser informativo en sentido lógico y ser **verdadero** o **significativo** en sentido fuerte.

#### Derivación básica de la medida lógica

Si el universo tiene $N$ mundos equiprobables y la proposición $\varphi$ es verdadera en $m$ de ellos, entonces:

$$
P_L(\varphi)=\frac{m}{N}
$$

Luego su contenido es

$$
\operatorname{Cont}(\varphi)=-\log_2\left(\frac{m}{N}\right)=\log_2\left(\frac{N}{m}\right)
$$

La interpretación es inmediata: la proposición elimina $N-m$ posibilidades y deja sólo $m$ compatibles.

#### Ejemplo 2.50: Contenido semántico lógico simple

Supóngase un universo de 8 estados posibles de una red de sensores:

$$
\Omega=\{\omega_1,\dots,\omega_8\}
$$

La proposición $\varphi$: “hay fallo en el sensor 1” es verdadera en 2 estados. Entonces:

$$
P_L(\varphi)=\frac{2}{8}=0.25
$$

Su contenido semántico lógico es:

$$
\operatorname{Cont}(\varphi)=-\log_2(0.25)=2\text{ bits semánticos lógicos}
$$

**Interpretación:** la proposición reduce el conjunto de posibilidades a una cuarta parte del total.

#### Ejemplo 2.51: Tautología y contradicción

Considérese:

- $\tau$: “el enlace está operativo o no lo está”
- $\kappa$: “el enlace está operativo y no lo está simultáneamente”

Para la tautología $\tau$:

$$
P_L(\tau)=1 \Rightarrow \operatorname{Cont}(\tau)=0
$$

Para la contradicción $\kappa$:

$$
P_L(\kappa)=0 \Rightarrow \operatorname{Cont}(\kappa)=\infty
$$

**Discusión:** el segundo resultado muestra precisamente la tensión entre contenido lógico y valor semántico genuino. Una contradicción excluye todos los mundos, pero no por ello es informativamente útil en sentido fuerte.

---

### 2.5.3 Floridi y la información semántica fuerte

Para superar la dificultad anterior, **Luciano Floridi** desarrolló la noción de **información fuertemente semántica** (*strongly semantic information*). Su tesis central es que la información semántica no puede desligarse de la **veracidad**.

#### Idea central

Un dato o mensaje sólo constituye información semántica en sentido fuerte si cumple al menos tres condiciones:

1. Está **bien formado**.
2. Es **significativo**.
3. Es **verdadero**.

En forma abreviada:

$$
\text{SSI} = \text{well-formed} + \text{meaningful} + \text{truthful}
$$

Bajo esta perspectiva:

- una tautología tiene bajo contenido informativo,
- una falsedad no es información semántica fuerte,
- una contradicción no aporta información semántica válida.

#### Formalización conceptual

Sea $m$ un mensaje y $W$ el estado real del mundo. Podemos pensar que la información semántica fuerte requiere:

$$
\mathcal{S}(m;W)>0 \quad \text{sólo si} \quad m \text{ es verdadero respecto de } W
$$

Un formalismo simple consiste en definir una función de veracidad:

$$
T(m,W)=
\begin{cases}
1, & \text{si } m \text{ es verdadero en } W \\
0, & \text{si } m \text{ es falso en } W
\end{cases}
$$

Entonces una medida elemental de contenido semántico fuerte puede escribirse como:

$$
I_S(m;W)=T(m,W)\,[-\log P_L(m)]
$$

Bajo esta forma:

- si el mensaje es falso, $I_S=0$;
- si es verdadero y restrictivo, $I_S$ es grande;
- si es verdadero pero trivial, $I_S$ es pequeño.

Esta formulación es pedagógica y no agota la teoría de Floridi, pero capta su intuición principal: **la verdad no es opcional** en la información semántica fuerte.

> **Concepto clave:** mientras Shannon mide mensajes independientemente de su verdad, Floridi sostiene que la información semántica fuerte debe excluir la falsedad como candidata válida.

#### Ejemplo 2.52: Mensaje verdadero frente a mensaje falso

Supongamos cuatro estados posibles de un sistema eléctrico:

$$
\Omega=\{\omega_1,\omega_2,\omega_3,\omega_4\}
$$

La proposición $m$: “hay sobrecarga en la línea 2” es verdadera en un solo estado, luego

$$
P_L(m)=\frac{1}{4}
$$

Si el estado real es ese mundo verdadero, entonces

$$
I_S(m;W)=1\cdot[-\log_2(1/4)]=2\text{ bits semánticos fuertes}
$$

Pero si el estado real no corresponde, entonces

$$
I_S(m;W)=0
$$

**Interpretación:** el mismo enunciado puede tener alto contenido potencial, pero sólo cuenta como información semántica fuerte cuando es verdadero.

---

### 2.5.4 Probabilidad lógica y medidas cuantitativas de contenido

La teoría semántica requiere distinguir entre **probabilidad estadística** y **probabilidad lógica**.

#### Probabilidad estadística vs probabilidad lógica

- La probabilidad estadística $P(X=x)$ describe frecuencia o incertidumbre empírica sobre eventos.
- La probabilidad lógica $P_L(\varphi)$ describe en cuántos mundos posibles es verdadera una proposición.

En Shannon, la rareza de un símbolo depende de una distribución observacional. En Carnap-Bar-Hillel, el contenido depende del conjunto de estados compatibles con una descripción.

#### Medida general de contenido semántico lógico

Sea $\varphi$ una proposición. Entonces:

$$
\operatorname{Cont}(\varphi)=-\log_b P_L(\varphi)
$$

Si $\varphi$ y $\psi$ son lógicamente independientes en el espacio considerado, entonces:

$$
P_L(\varphi\land\psi)=P_L(\varphi)P_L(\psi)
$$

y por tanto

$$
\operatorname{Cont}(\varphi\land\psi)=\operatorname{Cont}(\varphi)+\operatorname{Cont}(\psi)
$$

Aquí aparece una analogía formal directa con la autoinformación de Shannon.

#### Derivación con universo discreto ponderado

Si los mundos no son equiprobables, podemos definir una medida lógica ponderada:

$$
P_L(\varphi)=\sum_{\omega\in [\varphi]} \pi(\omega)
$$

con

$$
\sum_{\omega\in\Omega}\pi(\omega)=1
$$

Entonces el contenido se vuelve:

$$
\operatorname{Cont}(\varphi)=-\log_2 \left(\sum_{\omega\in [\varphi]} \pi(\omega)\right)
$$

Este paso permite conectar marcos lógicos y probabilísticos.

#### Relación con actualización bayesiana

Si un mensaje verdadero reduce la distribución del receptor desde una creencia previa $P(\omega)$ a una posterior $P(\omega|m)$, una forma útil de medir la ganancia de contenido es mediante divergencia de Kullback-Leibler:

$$
D\big(P(\omega|m)\,\|\,P(\omega)\big)=\sum_{\omega} P(\omega|m)\log_2\frac{P(\omega|m)}{P(\omega)}
$$

Esta cantidad captura cuánto cambia el conocimiento del receptor tras recibir el mensaje. En contextos semánticos, este cambio puede interpretarse como una aproximación cuantitativa al **impacto cognitivo** del mensaje.

#### Ejemplo 2.53: Contenido lógico con mundos ponderados

Sea un conjunto de estados con probabilidades a priori:

$$
\pi(\omega_1)=0.4,\quad \pi(\omega_2)=0.3,\quad \pi(\omega_3)=0.2,\quad \pi(\omega_4)=0.1
$$

La proposición $\varphi$ es verdadera en $\omega_3$ y $\omega_4$. Entonces:

$$
P_L(\varphi)=0.2+0.1=0.3
$$

Su contenido es:

$$
\operatorname{Cont}(\varphi)=-\log_2(0.3)\approx 1.737\text{ bits}
$$

**Interpretación:** la medida no depende ya del número de mundos, sino del peso lógico total de los mundos compatibles con la proposición.

---

### 2.5.5 Entropía semántica y diferencia con la entropía de Shannon

La **entropía de Shannon** mide incertidumbre media sobre símbolos emitidos por una fuente. La **entropía semántica**, en cambio, intenta medir incertidumbre media sobre **significados**, **proposiciones**, **interpretaciones** o **estados del mundo relevantes**.

#### Modelo básico

Sea una variable semántica $M$ que representa significados posibles o estados conceptuales relevantes, con distribución

$$
P(M=m_j)=q_j
$$

Entonces una definición análoga de entropía semántica puede escribirse como:

$$
H_S(M)= -\sum_j q_j \log_2 q_j
$$

Formalmente se parece a Shannon, pero la diferencia reside en **qué representan los estados**. En lugar de símbolos físicos, ahora los estados corresponden a significados, intenciones o hipótesis relevantes.

#### Entropía semántica condicionada por el mensaje recibido

Si $Y$ es el mensaje recibido y el receptor mantiene una distribución posterior sobre significados, entonces

$$
H_S(M|Y)= -\sum_y P(y)\sum_m P(m|y)\log_2 P(m|y)
$$

La reducción

$$
I_S(M;Y)=H_S(M)-H_S(M|Y)
$$

puede interpretarse como **información semántica mutua**: cuánto disminuye la incertidumbre del receptor sobre el significado gracias al mensaje observado.

#### Diferencias esenciales con Shannon

1. En Shannon, el alfabeto puede ser puramente formal; en semántica, los estados deben tener interpretación.
2. La teoría semántica requiere modelar conocimiento previo, contexto y, con frecuencia, verdad.
3. Dos secuencias con igual distribución sintáctica pueden tener diferente contenido semántico para un receptor concreto.
4. Puede ocurrir que una gran cantidad de bits tenga poco valor semántico, o que pocos bits activen una gran reducción de incertidumbre relevante.

#### Ejemplo ilustrativo

Supóngase que un receptor debe decidir entre cuatro posibles intenciones del emisor:

$$
M\in\{m_1,m_2,m_3,m_4\}
$$

con distribución uniforme. Entonces:

$$
H_S(M)=\log_2 4 = 2\text{ bits semánticos}
$$

Si tras recibir cierto mensaje el receptor reduce las posibilidades a dos equiprobables, entonces:

$$
H_S(M|Y)=1\text{ bit}
$$

y la ganancia semántica es:

$$
I_S(M;Y)=2-1=1\text{ bit}
$$

El cálculo es formalmente idéntico al clásico, pero su interpretación es distinta: la incertidumbre reducida es sobre **intención o significado**, no sobre símbolos transmitidos.

> **Concepto clave:** la diferencia entre entropía de Shannon y entropía semántica no está sólo en la fórmula, sino en la **naturaleza del espacio de estados** y en la necesidad de incorporar contexto, conocimiento y verdad.

**[Figura 2.17]:** Comparación visual entre entropía de Shannon y entropía semántica. La figura debe dividirse en dos paneles. En el primero, una fuente produce símbolos con ciertas probabilidades y la incertidumbre se mide sobre el alfabeto. En el segundo, los mismos símbolos apuntan a varios significados posibles y la incertidumbre se mide sobre interpretaciones o estados del mundo. La figura debe enfatizar que una misma señal sintáctica puede generar distintas distribuciones semánticas según el contexto del receptor.

---

### 2.5.6 Formalización matemática detallada

Para articular con más rigor la relación entre comunicación clásica y semántica, introducimos tres niveles aleatorios:

- $W$: estado del mundo o hecho relevante.
- $X$: representación simbólica generada por el emisor.
- $Y$: señal o mensaje recibido tras el canal.

Podemos modelar la cadena:

$$
W \longrightarrow X \longrightarrow Y
$$

Si el emisor observa o conoce parcialmente $W$ y genera $X$ para describirlo, y el canal produce $Y$, entonces el objetivo semántico del receptor no es sólo estimar $X$, sino inferir $W$.

#### Paso 1: teoría clásica

La teoría clásica se centra en

$$
I(X;Y)
$$

que mide cuánta información sobre el símbolo transmitido se recupera en la salida.

#### Paso 2: objetivo semántico

La cantidad realmente relevante para el significado puede ser

$$
I(W;Y)
$$

pues mide cuánta información sobre el estado del mundo conserva la señal recibida.

#### Relación por desigualdad de procesamiento de datos

Si se cumple la cadena de Markov $W\to X\to Y$, entonces

$$
I(W;Y) \le I(X;Y)
$$

Esta desigualdad tiene una interpretación decisiva: la recuperación de significado no puede exceder la recuperación de símbolos si el significado pasa exclusivamente a través de ellos. Sin embargo, en tareas concretas puede suceder que el sistema no necesite reconstruir completamente $X$ para recuperar satisfactoriamente $W$.

#### Derivación de reducción de incertidumbre semántica

Por definición,

$$
I(W;Y)=H(W)-H(W|Y)
$$

Si el conjunto de estados del mundo es $\{w_1,\dots,w_K\}$ con priori $P(w_k)$, entonces

$$
H(W)= -\sum_{k=1}^{K} P(w_k)\log_2 P(w_k)
$$

Tras recibir $y$, el receptor actualiza sus creencias a

$$
P(w_k|y)=\frac{P(y|w_k)P(w_k)}{P(y)}
$$

La entropía condicional semántica es

$$
H(W|Y)= -\sum_y P(y)\sum_k P(w_k|y)\log_2 P(w_k|y)
$$

La reducción promedio de esta incertidumbre es exactamente la información mutua sobre el estado del mundo.

#### Incorporación de veracidad

Para capturar la dimensión fuerte de Floridi, introducimos una variable de validez semántica $T\in\{0,1\}$ que indica si el contenido inferido es verdadero respecto del estado real. Entonces una medida corregida puede escribirse como

$$
I_{FS}(W;Y)=\mathbb{E}[T]\,I(W;Y)
$$

Si el sistema produce inferencias altamente informativas pero sistemáticamente falsas, la ganancia fuerte debe reducirse drásticamente.

#### Incorporación de relevancia para una tarea

En comunicaciones semánticas modernas no siempre interesa la reconstrucción literal del mensaje, sino su utilidad para una tarea. Sea $A$ una acción o decisión. Entonces puede ser más relevante maximizar

$$
I(A;Y)
$$

o minimizar una función de pérdida semántica:

$$
\mathcal{L}_S = \mathbb{E}[d_S(W,\hat{W}(Y))]
$$

con $d_S$ una distancia semántica o de tarea. Ésta es una generalización del problema clásico de distorsión, pero ahora la distorsión se define sobre significado o acción, no sobre amplitudes o símbolos.

#### Conexión con tasa-distorsión semántica

En teoría clásica, la función de tasa-distorsión es

$$
R(D)=\min_{p(\hat{x}|x):\,E[d(X,\hat{X})]\le D} I(X;\hat{X})
$$

En un problema semántico, una formulación análoga sería

$$
R_S(D_S)=\min_{p(\hat{w}|x):\,E[d_S(W,\hat{W})]\le D_S} I(X;\hat{W})
$$

lo que sugiere una teoría de compresión orientada a significado: no se preserva necesariamente toda la señal, sino sólo lo necesario para mantener acotada la distorsión semántica.

> **Concepto clave:** la teoría semántica no elimina la teoría clásica; la reordena jerárquicamente. Primero hay que modelar símbolos y canales, pero el objetivo final puede ser optimizar la inferencia sobre $W$ o la decisión $A$, no la reproducción perfecta de $X$.

---

### 2.5.7 Comparación entre teoría sintáctica y teoría semántica

| Aspecto | Teoría de Shannon (sintáctica) | Teoría de información semántica |
|---|---|---|
| Objeto principal | Símbolos, secuencias, señales | Significados, proposiciones, estados del mundo |
| Pregunta central | ¿Cuánta incertidumbre estadística hay? | ¿Cuánto significado verdadero o relevante se transmite? |
| Magnitud base | Entropía $H(X)$ | Contenido semántico, entropía semántica $H_S(M)$ |
| Criterio de información | Rareza probabilística | Restricción lógica, verdad, relevancia o utilidad |
| Tratamiento de la falsedad | Puede tener alta información si es improbable | En enfoques fuertes, la falsedad no cuenta como información válida |
| Canal ideal | Preserva símbolos | Preserva significado o decisión relevante |
| Optimización | Maximizar $I(X;Y)$ o capacidad | Maximizar $I(W;Y)$, utilidad o reducir distorsión semántica |
| Aplicaciones clásicas | Compresión, codificación, detección | Comunicaciones semánticas, IA distribuida, redes orientadas a tarea |

#### Comentario comparativo

La tabla deja ver que las dos teorías no compiten directamente. La teoría clásica proporciona la infraestructura cuantitativa indispensable. La teoría semántica busca añadir una capa interpretativa. En sistemas reales, ambas pueden coexistir:

- la capa física y de enlace optimiza transmisión sintáctica,
- las capas cognitivas o de aplicación optimizan valor semántico.

---

### 2.5.8 Ejemplos resueltos de información semántica

#### Ejemplo 2.54: Misma cantidad de bits, diferente valor semántico

Un sensor envía una palabra binaria de 8 bits cada segundo. En dos instantes distintos transmite:

- Mensaje 1: estado rutinario, sin cambios de operación.
- Mensaje 2: alarma crítica que activa parada de emergencia.

Desde el punto de vista clásico, ambos mensajes ocupan 8 bits y, si son equiprobables en su alfabeto local, pueden aportar la misma cantidad sintáctica. Sin embargo, si modelamos dos estados del mundo relevantes,

$$
W\in\{\text{normal},\text{crítico}\}
$$

y asumimos un priori

$$
P(\text{normal})=0.98,\qquad P(\text{crítico})=0.02
$$

la entropía semántica previa es:

$$
H(W)=-0.98\log_2 0.98-0.02\log_2 0.02
$$

$$
H(W)\approx 0.0286+0.1129=0.1415\text{ bits}
$$

Si el mensaje 2 identifica perfectamente el estado crítico, entonces para ese caso la reducción de incertidumbre semántica es muy valiosa respecto al estado del mundo, aunque la longitud binaria del mensaje sea igual a la del mensaje rutinario.

**Conclusión:** igualdad en bits no implica igualdad en significado operativo.

#### Ejemplo 2.55: Cálculo de información semántica mutua sobre estados del mundo

Sea un sistema con tres estados del mundo:

$$
W\in\{w_1,w_2,w_3\}
$$

con priori uniforme. Un receptor, tras observar $Y$, genera la siguiente distribución posterior para un mensaje particular $y$:

$$
P(W|y)=\{0.8,0.1,0.1\}
$$

La entropía previa es:

$$
H(W)=\log_2 3\approx 1.585\text{ bits}
$$

La entropía posterior para ese mensaje es:

$$
H(W|y)= -0.8\log_2 0.8 -0.1\log_2 0.1 -0.1\log_2 0.1
$$

$$
H(W|y)\approx 0.2575+0.3322+0.3322=0.9219\text{ bits}
$$

La reducción de incertidumbre asociada a ese mensaje es:

$$
\Delta H_S=1.585-0.9219=0.6631\text{ bits}
$$

**Interpretación:** el mensaje no necesariamente identifica por completo el estado del mundo, pero sí reduce de manera apreciable la incertidumbre semántica.

#### Ejemplo 2.56: Veracidad y semántica fuerte

Considérese una proposición $m$: “el paciente presenta fibrilación auricular”. En un espacio de 16 estados diagnósticos posibles, el enunciado es compatible con sólo 2 estados, de modo que:

$$
P_L(m)=\frac{2}{16}=0.125
$$

Su contenido lógico sería:

$$
\operatorname{Cont}(m)=-\log_2(0.125)=3\text{ bits}
$$

Si el diagnóstico real confirma la afirmación, una medida fuerte elemental da:

$$
I_S(m;W)=3\text{ bits}
$$

Pero si el diagnóstico real la contradice, bajo el criterio fuerte:

$$
I_S(m;W)=0
$$

**Conclusión:** la teoría fuerte distingue entre un mensaje específico y un mensaje verdadero. La especificidad sola no basta.

#### Ejemplo 2.57: Compresión semántica orientada a tarea

Un vehículo autónomo recibe una imagen de cámara de gran tamaño. Desde el punto de vista sintáctico, la imagen contiene millones de bits. Sin embargo, para la tarea de frenado inmediato sólo importa una variable semántica:

$$
W\in\{\text{peatón presente},\text{peatón ausente}\}
$$

Si el sistema consigue transmitir únicamente una representación compacta que preserve esa decisión con alta confiabilidad, la tasa binaria puede reducirse enormemente sin perder utilidad para la tarea. Este ejemplo no requiere un cálculo único, sino una conclusión estructural:

$$
I(W;Y)\text{ puede ser alto aunque }I(X;Y)\text{ sea muy inferior a la descripción completa de la imagen}
$$

**Mensaje central:** en comunicaciones semánticas, el objetivo no es reproducir todo el contenido visual, sino preservar la información necesaria para la decisión correcta.

---

### 2.5.9 Relevancia en comunicaciones modernas: 6G y comunicaciones semánticas

Las redes futuras, en particular **6G**, se proyectan como plataformas para comunicaciones inmersivas, inteligencia distribuida, gemelos digitales, coordinación multiagente, redes de sensores masivos y sistemas autónomos. En estos escenarios, transmitir todos los bits crudos no siempre es eficiente ni necesario.

#### Motivaciones principales

1. **Explosión de datos multimodales**: video, nubes de puntos, señales biomédicas, mapas y telemetría.
2. **Sistemas orientados a tarea**: no siempre interesa reconstruir la señal completa, sino habilitar una decisión.
3. **Integración con inteligencia artificial**: los modelos pueden extraer representaciones latentes más compactas y semánticamente relevantes.
4. **Restricciones de energía y latencia**: especialmente en IoT, edge intelligence y control en tiempo real.

#### Vista preliminar de comunicación semántica

Un esquema semántico puede representarse como:

$$
\text{Fuente física} \to \text{Extractor semántico} \to \text{Codificador} \to \text{Canal} \to \text{Decodificador} \to \text{Inferencia/acción}
$$

La novedad está en el bloque de extracción semántica: antes de transmitir, el sistema intenta conservar sólo los atributos relevantes para la tarea.

#### Conexión con teoría clásica

- La capacidad de Shannon sigue siendo un límite físico para la transmisión de representaciones.
- Pero la variable optimizada ya no tiene por qué ser la señal cruda $X$, sino una representación semántica $Z$ o un estado del mundo $W$.
- En ese contexto, el problema puede reformularse como maximizar $I(W;Y)$ bajo restricciones de tasa, energía y latencia.

#### Retos abiertos

- definir formalmente “significado” en diferentes tareas;
- diseñar métricas semánticas universales;
- separar error sintáctico tolerable de error semántico crítico;
- garantizar robustez, explicabilidad y veracidad en la inferencia;
- integrar teoría clásica, aprendizaje automático y teoría de decisión.

> **Concepto clave:** la comunicación semántica no busca reemplazar la codificación clásica, sino redistribuir el presupuesto de bits hacia aquello que más importa para la inferencia o la acción final.

---

### 2.5.10 Síntesis de la sección 2.5

- Shannon y Weaver distinguieron niveles **técnico**, **semántico** y **de efectividad**.
- Carnap y Bar-Hillel formalizaron el contenido semántico como reducción lógica de posibilidades.
- Floridi introdujo la idea de información semántica **fuerte**, donde la verdad es esencial.
- La probabilidad lógica difiere de la probabilidad estadística, aunque ambas pueden relacionarse.
- La entropía semántica mide incertidumbre sobre significados o estados del mundo, no sólo sobre símbolos.
- En comunicaciones modernas, resulta natural optimizar la transmisión respecto a tareas, decisiones o conocimiento relevante, especialmente en contextos 6G y sistemas inteligentes.

En resumen, la teoría de la información semántica amplía el programa clásico de la comunicación: de transmitir correctamente símbolos, a transmitir correctamente **lo que importa**.

---

## Resumen general de la unidad

En esta unidad se han desarrollado cinco bloques fundamentales de las comunicaciones digitales:

1. **Teoría de la información**:
   - La autoinformación se define como
     $$
     I(x)=-\log_2 p(x)
     $$
   - La entropía de una fuente discreta es
     $$
     H(X)=-\sum_x p(x)\log_2 p(x)
     $$
   - La información mutua y la capacidad permiten cuantificar la transferencia de información a través de un canal.

2. **Codificación de fuente y PCM**:
   - El teorema de muestreo establece la condición
     $$
     f_s\ge 2W
     $$
   - La cuantización introduce error y ruido de cuantización.
   - El sistema PCM completo traduce señales analógicas en secuencias binarias.
   - La SQNR ideal de un cuantizador uniforme es
     $$
     \mathrm{SQNR}_{dB}\approx 6.02n+1.76
     $$

3. **Capacidad de canal**:
   - Shannon demostró que existe una tasa máxima de transmisión fiable.
   - Para AWGN,
     $$
     C=B\log_2(1+\mathrm{SNR})
     $$
   - El límite mínimo teórico de potencia por bit es
     $$
     \left(\frac{E_b}{N_0}\right)_{\min}=-1.59\,\text{dB}
     $$

4. **Detección digital óptima**:
   - El criterio ML escoge el símbolo que maximiza $p(r|s_i)$.
   - El criterio MAP escoge el símbolo que maximiza $P(s_i|r)$.
   - En AWGN, ML equivale a distancia mínima.
   - La probabilidad de error para BPSK es
     $$
     P_b=Q\left(\sqrt{\frac{2E_b}{N_0}}\right)
     $$

5. **Teoría de la información semántica**:
   - Shannon-Weaver distinguen entre precisión técnica, significado y efectividad.
   - Carnap y Bar-Hillel relacionan contenido semántico con probabilidad lógica.
   - Floridi exige verdad para hablar de información semántica fuerte.
   - La entropía semántica modela incertidumbre sobre significados, estados del mundo o tareas.
   - Las comunicaciones 6G y semánticas retoman estas ideas para transmitir no sólo bits, sino conocimiento útil para decisiones.

En conjunto, estos resultados conectan la producción de información por una fuente, su digitalización, su transmisión por canales ruidosos, su recuperación óptima en recepción y su posible reinterpretación en términos de significado. Constituyen la base conceptual sobre la cual se construyen los sistemas modernos de telecomunicaciones móviles, satelitales, ópticas, sensoriales y de redes inalámbricas avanzadas.

---

## Referencias

1. C. E. Shannon, “A Mathematical Theory of Communication,” *Bell System Technical Journal*, vol. 27, no. 3, pp. 379–423, 1948; vol. 27, no. 4, pp. 623–656, 1948. DOI: $10.1002/j.1538-7305.1948.tb01338.x$ y $10.1002/j.1538-7305.1948.tb00917.x$.
2. C. E. Shannon y W. Weaver, *The Mathematical Theory of Communication*. University of Illinois Press, 1949.
3. T. M. Cover y J. A. Thomas, *Elements of Information Theory*, 2nd ed. Wiley, 2006. DOI: $10.1002/047174882X$.
4. J. G. Proakis y M. Salehi, *Digital Communications*, 5th ed. McGraw-Hill, 2008.
5. S. Haykin, *Communication Systems*, 4th ed. Wiley, 2001.
6. B. Sklar, *Digital Communications: Fundamentals and Applications*, 2nd ed. Prentice Hall, 2001.
7. A. Papoulis y S. U. Pillai, *Probability, Random Variables, and Stochastic Processes*, 4th ed. McGraw-Hill, 2002.
8. J. R. Pierce, “Information Theory,” *Scientific American*, vol. 200, no. 1, pp. 42–51, 1959. DOI: $10.1038/scientificamerican0159-42$.
9. R. Carnap y Y. Bar-Hillel, “An Outline of a Theory of Semantic Information,” *Technical Report No. 247*, Research Laboratory of Electronics, MIT, 1952.
10. L. Floridi, *The Philosophy of Information*. Oxford University Press, 2011.
11. B. Güler, A. Yener y A. Swami, “The Semantic Communication Game,” *IEEE Transactions on Cognitive Communications and Networking*, vol. 4, no. 4, pp. 787–802, 2018.
12. M. K. Khandani, “Media-Based Modulation: A New Approach to Wireless Transmission,” *IEEE International Symposium on Information Theory*, 2013. (Referencia útil para discutir nuevos paradigmas más allá del enfoque estrictamente sintáctico).
13. H. Xie, Z. Qin, G. Y. Li, B.-H. Juang y Z. Han, “Deep Learning Enabled Semantic Communication Systems,” *IEEE Transactions on Signal Processing*, vol. 69, pp. 2663–2675, 2021.
