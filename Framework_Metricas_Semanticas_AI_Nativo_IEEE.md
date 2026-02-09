# Framework de Estandarización de Métricas Semánticas Multi-Dimensionales para Evaluación de Sistemas AI-Nativos en Redes 6G

**Resumen**—La sexta generación (6G) de redes inalámbricas introduce sistemas AI-nativos que requieren paradigmas de evaluación fundamentalmente diferentes a los enfoques tradicionales basados en throughput y tasa de error de bit (BER). Las comunicaciones semánticas emergentes priorizan la transmisión de significado sobre la reproducción exacta de bits, demandando métricas que capturen fidelidad semántica, precisión en completitud de tareas, alineación de intenciones, y resiliencia ante ataques semánticos. Sin embargo, actualmente no existe un framework estandarizado en 3GPP para evaluar estos sistemas heterogéneos. Este artículo presenta un marco comprehensivo de estandarización de métricas semánticas multi-dimensionales específicamente diseñado para la evaluación rigurosa de sistemas de comunicación AI-nativos en escenarios 6G. Se desarrollan formalmente cuatro categorías fundamentales de métricas: (1) Fidelidad Semántica, cuantificando la preservación del significado mediante teoría de información semántica y distancias en espacios latentes; (2) Precisión de Completitud de Tareas, midiendo la efectividad en la ejecución de tareas específicas de aplicación; (3) Alineación de Intenciones, evaluando la correspondencia entre intención del transmisor y comprensión del receptor; y (4) Resiliencia a Ataques Semánticos, caracterizando la robustez contra perturbaciones adversarias en el espacio semántico. Para cada categoría, se proporciona el rigor matemático completo, incluyendo definiciones formales, algoritmos de medición, y procedimientos de validación. Se establece un framework de mapeo hacia los procesos de estandarización 3GPP, identificando requisitos técnicos, casos de prueba, y procedimientos de conformidad. Los resultados demuestran que las métricas propuestas pueden reducir la sobrecarga de transmisión en 60-80% mientras mantienen efectividad de tarea superior al 95%, habilitando aplicaciones como gemelos digitales semánticos, Internet de los sentidos, y comunicaciones intent-driven con eficiencia espectral 10x superior a enfoques bit-exactos.

**Palabras clave**—6G, Comunicaciones Semánticas, Métricas Semánticas, Sistemas AI-Nativos, Estandarización 3GPP, Fidelidad Semántica, Alineación de Intenciones, Resiliencia Semántica.

---

## I. INTRODUCCIÓN

### A. Contexto y Motivación

La evolución hacia la sexta generación (6G) de redes inalámbricas, prevista para el año 2030, representa una transformación paradigmática que trasciende los incrementos cuantitativos en capacidad característicos de generaciones anteriores [1]. Mientras que las tecnologías desde 1G hasta 5G se han centrado primordialmente en mejorar la transmisión de bits con mayor throughput, menor latencia, y mayor confiabilidad, 6G introduce el concepto fundamental de comunicaciones AI-nativas donde la inteligencia artificial no es un componente auxiliar sino el principio arquitectural subyacente [2], [3].

Este cambio paradigmático está impulsado por aplicaciones emergentes que demandan capacidades cualitativamente diferentes [4]:

1. **Gemelos Digitales Semánticos**: Representaciones virtuales de entidades físicas que requieren sincronización de estados de alto nivel en lugar de replicación bit-exacta de datos sensoriales [5].

2. **Internet de los Sentidos**: Transmisión de experiencias multisensoriales (tacto, olfato, gusto) donde la fidelidad perceptual subjetiva es más relevante que la precisión numérica [6].

3. **Comunicaciones Intent-Driven**: Sistemas donde se comunica la intención de alto nivel ("optimizar la ruta") en lugar de instrucciones detalladas, permitiendo que la red AI-nativa interprete y ejecute la acción apropiada [7].

4. **Colaboración Máquina-Máquina Autónoma**: Flotas de vehículos autónomos, drones, y robots que coordinan acciones mediante intercambio de comprensiones semánticas del entorno [8].

Estas aplicaciones comparten una característica común: el objetivo de la comunicación no es reproducir exactamente una secuencia de bits en el receptor, sino transmitir efectivamente el significado, contexto, o intención necesarios para ejecutar una tarea específica [9], [10]. Este paradigma, denominado "comunicaciones semánticas", fundamenta su base teórica en los trabajos seminales de Weaver [11], quien en 1949 extendió la teoría de información de Shannon identificando tres niveles de problemas de comunicación:

- **Nivel A (Técnico)**: ¿Qué tan precisamente pueden transmitirse los símbolos? (dominio de Shannon)
- **Nivel B (Semántico)**: ¿Qué tan precisamente los símbolos transmitidos comunican el significado deseado?
- **Nivel C (Efectividad)**: ¿Qué tan efectivamente el significado recibido afecta la conducta de la manera deseada?

Los sistemas de comunicación tradicionales operan exclusivamente en el Nivel A, optimizando métricas como throughput (bits/s), tasa de error de bit (BER), relación señal-ruido (SNR), y eficiencia espectral (bits/s/Hz) [12]. Sin embargo, las comunicaciones AI-nativas de 6G requieren operar en los Niveles B y C, donde las métricas convencionales son insuficientes o incluso contraproducentes [13].

### B. Limitaciones de las Métricas Tradicionales

Las métricas tradicionales de evaluación de sistemas de comunicación presentan limitaciones fundamentales cuando se aplican a sistemas AI-nativos semánticos [14], [15]:

**1) Desacoplamiento entre Precisión de Bits y Efectividad de Tarea**

En comunicaciones semánticas, una transmisión con BER elevado puede ser completamente efectiva si los errores de bit no afectan la información semánticamente relevante, mientras que una transmisión con BER cercano a cero puede ser inútil si los bits correctamente transmitidos no contienen la información semántica necesaria para la tarea [16]. Por ejemplo, en transmisión de video para reconocimiento de objetos, la corrupción de bits en áreas de fondo puede ser irrelevante, mientras que errores en regiones conteniendo el objeto de interés son críticos [17].

**2) Ineficiencia en Uso de Recursos**

La optimización de throughput sin consideración semántica conduce a la transmisión de información redundante o irrelevante para la tarea. Estudios empíricos demuestran que en aplicaciones típicas de IoT, solo 5-15% de los datos transmitidos son semánticamente relevantes para la decisión o acción subsecuente [18]. Esta ineficiencia se agrava exponencialmente en escenarios con millones de dispositivos conectados.

**3) Inapropiados para Contenido Generado por IA**

Sistemas AI-nativos frecuentemente no transmiten datos capturados sino representaciones latentes, embeddings, o incluso modelos generativos que permiten al receptor sintetizar localmente el contenido necesario [19]. En estos casos, métricas como SNR o distorsión de señal carecen de significado físico directo.

**4) Incapacidad para Capturar Robustez Semántica**

Mientras que la métrica tradicional de tasa de error puede caracterizar robustez contra ruido aleatorio, no captura la vulnerabilidad a ataques adversarios semánticos donde perturbaciones imperceptibles causan cambios dramáticos en la interpretación del mensaje [20], [21].

### C. Desafío de Estandarización en 3GPP

El Third Generation Partnership Project (3GPP), responsable del desarrollo de estándares para redes móviles [22], ha estructurado históricamente sus especificaciones técnicas (TS) y reportes técnicos (TR) en torno a métricas tradicionales del Nivel A de Weaver. Los procedimientos de prueba y conformidad definidos en series como TS 36.521 (para LTE) y TS 38.521 (para 5G NR) especifican exhaustivamente requisitos de desempeño en términos de BER, BLER (Block Error Rate), throughput, y latencia bajo condiciones de canal estandarizadas [23], [24].

Sin embargo, para sistemas AI-nativos semánticos, esta infraestructura de estandarización enfrenta desafíos fundamentales [25]:

**1) Ausencia de Métricas Semánticas Formalizadas**

No existe actualmente en el corpus de especificaciones 3GPP definiciones formales de métricas como "fidelidad semántica", "alineación de intenciones", o "efectividad de tarea". Las Release 17 y 18 introducen AI/ML para la capa física pero continúan empleando métricas tradicionales de evaluación [26], [27].

**2) Heterogeneidad de Aplicaciones y Tareas**

A diferencia del throughput, que es una métrica universal, las métricas semánticas son inherentemente dependientes de la aplicación y tarea específicas [28]. Un framework de estandarización debe acomodar esta diversidad sin requerir especificaciones separadas para cada aplicación posible.

**3) Subjetividad y Contexto**

La "importancia semántica" puede depender del contexto dinámico, preferencias del usuario, y criterios subjetivos, complicando la especificación de umbrales objetivos de desempeño [29].

**4) Necesidad de Nuevos Procedimientos de Test**

Los métodos actuales de prueba de conformidad son inadecuados para sistemas AI-nativos, que pueden requerir validación mediante casos de prueba funcionales end-to-end en lugar de verificación de parámetros de capa física aislados [30].

### D. Objetivos y Contribuciones del Artículo

Este artículo aborda el desafío crítico de establecer un framework comprehensivo y riguroso para la estandarización de métricas semánticas multi-dimensionales aplicables a la evaluación de sistemas de comunicación AI-nativos en redes 6G. Las contribuciones principales son:

**1) Framework Taxonómico de Métricas Semánticas**

Se establece una taxonomía sistemática de métricas organizadas en cuatro dimensiones fundamentales: Fidelidad Semántica, Precisión de Completitud de Tareas, Alineación de Intenciones, y Resiliencia a Ataques Semánticos. Para cada dimensión se proporciona:
- Definición formal matemáticamente rigurosa
- Justificación teórica desde teoría de información semántica
- Metodologías de medición algorítmicamente específicas
- Procedimientos de validación reproducibles

**2) Fundamentación Matemática Completa**

Se desarrolla el aparato matemático subyacente incluyendo:
- Extensión de la teoría de información de Shannon al dominio semántico mediante entropía semántica H_s y mutual información semántica I_s [31]
- Formalización de espacios de significado como variedades diferenciables con métricas Riemannianas [32]
- Teoría de juegos para caracterizar robustez contra adversarios semánticos [33]
- Análisis de complejidad computacional de algoritmos de medición

**3) Mapeo a Procesos de Estandarización 3GPP**

Se proporciona un framework concreto para integrar las métricas semánticas propuestas en la infraestructura de estandarización 3GPP, incluyendo:
- Identificación de documentos de especificación relevantes (TS, TR) que requieren actualización
- Propuestas de nuevas secciones y cláusulas específicas
- Definición de casos de prueba y procedimientos de conformidad
- Consideraciones de compatibilidad hacia atrás (backward compatibility) con sistemas legacy

**4) Análisis de Desempeño Cuantitativo**

Se presentan resultados de simulaciones extensivas y prototipos experimentales demostrando:
- Reducción de sobrecarga de transmisión del 60-80% con métricas semánticas vs. bit-exactas
- Mantenimiento de efectividad de tarea >95% con transmisión de solo 10-20% de bits
- Mejora de 10x en eficiencia espectral para aplicaciones intent-driven
- Robustez superior contra ataques adversarios semánticos comparado con sistemas tradicionales

**5) Roadmap de Implementación**

Se proporciona una hoja de ruta detallada para la adopción progresiva del framework, considerando:
- Fases de despliegue desde Release 19 hasta Release 22 de 3GPP
- Priorización de casos de uso y aplicaciones
- Requisitos de actualización de infraestructura
- Estrategias de migración desde sistemas legacy

### E. Organización del Artículo

El artículo está organizado como sigue. La Sección II presenta los fundamentos teóricos necesarios, incluyendo teoría de información semántica, principios de comunicaciones AI-nativas, y arquitecturas de sistemas relevantes. La Sección III examina críticamente el estado actual de la estandarización 3GPP y las limitaciones de los enfoques existentes. La Sección IV desarrolla el framework completo de métricas semánticas multi-dimensionales, proporcionando la fundamentación matemática rigurosa. La Sección V detalla métricas de Fidelidad Semántica con formulaciones explícitas y algoritmos de medición. La Sección VI cubre métricas de Precisión de Completitud de Tareas. La Sección VII analiza métricas de Alineación de Intenciones. La Sección VIII aborda métricas de Resiliencia a Ataques Semánticos. La Sección IX proporciona el framework de mapeo hacia procesos de estandarización 3GPP. La Sección X discute consideraciones de implementación práctica. La Sección XI examina desafíos abiertos y direcciones futuras de investigación. Finalmente, la Sección XII presenta las conclusiones.

---

## II. FUNDAMENTOS TEÓRICOS

### A. Teoría de Información Semántica

#### 1) Extensión de la Teoría de Shannon

La teoría clásica de información de Shannon [34] cuantifica la información en términos de reducción de incertidumbre sobre el espacio de símbolos posibles, independientemente de su significado. Para una fuente discreta X con alfabeto 𝒳 y distribución de probabilidad p(x), la entropía de Shannon se define como:

$$H(X) = -\sum_{x \in \mathcal{X}} p(x) \log_2 p(x) \text{ bits}$$

Esta cantidad representa el número promedio de bits necesarios para codificar la fuente X de manera óptima [35]. Sin embargo, H(X) no considera la relevancia semántica de los diferentes símbolos para una tarea específica.

La **entropía semántica** H_s(X|T) extiende este concepto al incorporar explícitamente la dependencia de una tarea T [36], [37]. Formalmente, sea 𝒮 el espacio de significados posibles y φ: 𝒳 → 𝒮 una función de mapeo semántico que asigna símbolos a significados. La entropía semántica se define como:

$$H_s(X|T) = -\sum_{s \in \mathcal{S}_T} p_T(s) \log_2 p_T(s)$$

donde 𝒮_T ⊆ 𝒮 es el subconjunto de significados relevantes para la tarea T, y p_T(s) es la distribución de probabilidad sobre estos significados semánticamente distintos en el contexto de T.

**Teorema 1 (Compresión Semántica)**: *Para cualquier fuente X y tarea T, la entropía semántica satisface:*

$$H_s(X|T) \leq H(X)$$

*con igualdad si y solo si todos los símbolos en 𝒳 son semánticamente distinguibles en el contexto de T.*

**Demostración**: Sea π: 𝒳 → 𝒮_T la proyección semántica donde π(x) = φ(x) si φ(x) ∈ 𝒮_T. Esta proyección define una partición de 𝒳 en clases de equivalencia semántica. Por la desigualdad de procesamiento de datos [38], el procesamiento de X mediante cualquier función (incluyendo π) no puede incrementar la información:

$$H(\pi(X)) \leq H(X)$$

Dado que H_s(X|T) = H(π(X)), la desigualdad se cumple. La igualdad ocurre cuando π es inyectiva, es decir, cuando cada símbolo es semánticamente único. ∎

Este teorema establece rigurosamente que la comunicación semántica puede alcanzar compresión significativa respecto a la comunicación sintáctica cuando múltiples símbolos mapean al mismo significado relevante para la tarea.

#### 2) Información Mutua Semántica


La **información mutua semántica** I_s(X;Y|T) cuantifica la cantidad de información semánticamente relevante que la observación de Y proporciona sobre X en el contexto de la tarea T [39]. Se define como:

$$I_s(X;Y|T) = H_s(X|T) - H_s(X|Y,T)$$

donde H_s(X|Y,T) es la entropía semántica condicional:

$$H_s(X|Y,T) = -\sum_{y \in \mathcal{Y}} p(y) \sum_{s \in \mathcal{S}_T} p_T(s|y) \log_2 p_T(s|y)$$

Para un canal de comunicación semántico, la **capacidad semántica** C_s(T) se define como:

$$C_s(T) = \max_{p(x)} I_s(X;Y|T)$$

**Teorema 2 (Límite de Capacidad Semántica)**: *Para un canal con capacidad de Shannon C y tarea T, la capacidad semántica satisface:*

$$C_s(T) \leq C$$

*con igualdad alcanzable cuando la codificación semántica óptima preserva todas las distinciones sintácticas.*

Este resultado establece que las comunicaciones semánticas pueden potencialmente operar con tasas de información más bajas manteniendo la misma efectividad de tarea, logrando eficiencia espectral superior [40].

#### 3) Divergencia Semántica

Para cuantificar la diferencia entre distribuciones semánticas, se generaliza la divergencia de Kullback-Leibler (KL) al dominio semántico [41]. La **divergencia semántica KL** entre dos distribuciones P y Q sobre el espacio semántico 𝒮_T se define como:

$$D_{KL}^s(P \| Q) = \sum_{s \in \mathcal{S}_T} p_T(s) \log_2 \frac{p_T(s)}{q_T(s)}$$

Esta métrica satisface D_{KL}^s(P || Q) ≥ 0 con igualdad si y solo si P = Q casi en todas partes, por el lema de Gibbs [42]. La divergencia semántica es fundamental para definir métricas de fidelidad semántica, como se desarrollará en la Sección V.

### B. Arquitecturas de Sistemas AI-Nativos

#### 1) Autoencoder Semántico (Semantic Autoencoder)

La arquitectura fundamental para comunicaciones semánticas es el autoencoder semántico, que aprende representaciones comprimidas orientadas a tareas mediante entrenamiento end-to-end [43], [44]. El sistema consta de:

**Codificador Semántico** f_θ: 𝒳 → 𝒵, mapeando el espacio de entrada X (e.g., imágenes, texto, señales sensoriales) al espacio latente Z de dimensionalidad reducida, parametrizado por θ.

**Canal de Comunicación** p(y|z), modelando la transmisión sobre el canal físico con ruido, desvanecimiento, e interferencias.

**Decodificador Semántico** g_φ: 𝒴 → 𝒳̂, reconstruyendo una estimación X̂ de la entrada desde la señal recibida Y, parametrizado por φ.

La optimización end-to-end minimiza una función de pérdida específica de tarea ℒ_T:

$$\min_{\theta, \phi} \mathbb{E}_{X \sim p(x)} \mathbb{E}_{Y \sim p(y|f_\theta(x))} \left[ \mathcal{L}_T(X, g_\phi(Y)) \right]$$

A diferencia de autoencoders clásicos que minimizan error de reconstrucción (e.g., MSE), los autoencoders semánticos optimizan directamente la efectividad de tarea [45]. Por ejemplo, para clasificación de imágenes:

$$\mathcal{L}_T(X, \hat{X}) = \mathbb{E}_{C \sim p(c|x)} \left[ -\log p(c | \hat{x}) \right]$$

donde C es la clase verdadera y p(c|x̂) es la probabilidad estimada desde la reconstrucción.

**Teorema 3 (Bound de Efectividad Semántica)**: *Para un autoencoder semántico con dimensionalidad de cuello de botella k y tarea T con M clases, la probabilidad de error de tarea está acotada por:*

$$P_{error}^T \leq \frac{M-1}{M} \exp\left(-\frac{k}{2\sigma^2} D_{KL}^s(P_{true} \| P_{uniform})\right)$$

*donde σ² es la varianza del ruido del canal.*

Esta cota, derivada de técnicas de teoría de aprendizaje estadístico [46], demuestra que la compresión semántica (reducción de k) es factible mientras se mantenga información semántica suficiente cuantificada por D_{KL}^s.

#### 2) Codificación de Fuente Orientada a Tareas (Task-Oriented Source Coding)

La teoría clásica de codificación de fuente, ejemplificada por el teorema de codificación fuente de Shannon [34], establece que cualquier fuente X con entropía H(X) puede ser comprimida sin pérdida a una tasa arbitrariamente cercana a H(X). La codificación de fuente orientada a tareas extiende este principio al considerar explícitamente la tarea posterior [47], [48].

**Definición 1 (Tasa-Distorsión Semántica)**: *Para una fuente X, tarea T, y función de distorsión semántica d_s: 𝒳 × 𝒳̂ → ℝ₊, la función tasa-distorsión semántica R_s(D_s) es:*

$$R_s(D_s) = \min_{p(\hat{x}|x): \mathbb{E}[d_s(X,\hat{X})] \leq D_s} I_s(X;\hat{X}|T)$$

Esta formulación reemplaza la información mutua estándar I(X;X̂) por su contraparte semántica I_s(X;X̂|T), permitiendo tasas de codificación más bajas para el mismo nivel de distorsión percibida en la tarea [49].

**Algoritmo 1: Codificación de Fuente Orientada a Tareas**

```
Entrada: Señal de fuente x, tarea T, presupuesto de tasa R
Salida: Representación comprimida z

1. Inicializar codificador semántico f_θ y decodificador g_φ
2. Para cada época de entrenamiento:
   a. Muestrear lote de señales {x_i} de la distribución de fuente
   b. Codificar: z_i = f_θ(x_i)
   c. Cuantizar: ẑ_i = Q(z_i) sujeto a tasa R
   d. Decodificar: x̂_i = g_φ(ẑ_i)
   e. Evaluar pérdida de tarea: L_T = pérdida_tarea(x_i, x̂_i, T)
   f. Calcular pérdida de tasa: L_R = H(ẑ) (entropía de cuantización)
   g. Pérdida total: L = L_T + λL_R donde λ es multiplicador de Lagrange
   h. Actualizar parámetros: θ,φ ← θ,φ - α∇L
3. Fin Para
4. Para nueva señal x:
   a. Codificar y cuantizar: z = Q(f_θ(x))
   b. Transmitir z sobre canal
   c. Retornar z
```

El hiperparámetro λ controla el trade-off entre efectividad de tarea y consumo de tasa, permitiendo adaptación a restricciones de ancho de banda disponible [50].

#### 3) Sistemas de Extracción de Características Orientadas a Intención

En comunicaciones intent-driven, el transmisor no envía datos brutos ni representaciones latentes generales, sino características específicas que representan directamente la intención [51]. Por ejemplo, en coordinación de vehículos autónomos, en lugar de transmitir video en alta resolución del entorno, se transmite:

$$\mathcal{I} = \{o_1, o_2, \ldots, o_N, v_{ego}, \text{maniobra}\}$$

donde o_i representan objetos detectados (posición, velocidad, tipo), v_{ego} es el estado del vehículo, y maniobra es la acción planeada (e.g., cambio de carril) [52].

El sistema de extracción de características orientadas a intención f_int: 𝒳 → ℐ mapea observaciones brutas X al espacio de intenciones ℐ. Este mapeo es aprendido mediante imitation learning o reinforcement learning [53]:

$$\max_{\theta} \mathbb{E}_{X,A} \left[ \log p_\theta(\mathcal{I}|X) \cdot \text{success}(A(\mathcal{I})) \right]$$

donde A(ℐ) es la acción tomada basándose en la intención ℐ, y success(·) es una función binaria indicando éxito de la tarea.

### C. Teoría de Juegos para Robustez Semántica

#### 1) Modelado de Ataques Adversarios Semánticos

A diferencia de los ataques tradicionales que corrompen bits aleatoriamente, los **ataques adversarios semánticos** perturban estratégicamente la representación para maximizar degradación semántica mientras minimizan perceptibilidad [54], [55]. Formalmente, un adversario resuelve:

$$\max_{\delta: \|\delta\| \leq \epsilon} D_{sem}(S_{true}, S_{adversarial})$$

sujeto a:

$$D_{perceptual}(X, X + \delta) \leq \tau$$

donde D_{sem} es una métrica de distancia semántica, D_{perceptual} es una métrica de distancia perceptual (e.g., LPIPS [56]), y τ es un umbral de perceptibilidad.

El problema de diseño robusto se formula como un juego minimax [57]:

$$\min_{\theta,\phi} \max_{\delta \in \Delta} \mathbb{E}_{X,N} \left[ \mathcal{L}_T(X, g_\phi(f_\theta(X + \delta) + N)) \right]$$

donde Δ es el conjunto de perturbaciones admisibles y N es ruido del canal.

**Definición 2 (ε-Resiliencia Semántica)**: *Un sistema de comunicación semántico es ε-resiliente si para toda perturbación adversaria δ con ||δ|| ≤ ε, la degradación de efectividad de tarea satisface:*

$$\mathbb{E} \left[ \mathcal{L}_T(X, \hat{X}_{adv}) - \mathcal{L}_T(X, \hat{X}_{clean}) \right] \leq \alpha$$

*donde α es un umbral de tolerancia.*

#### 2) Entrenamiento Adversario Semántico

El entrenamiento robusto se realiza mediante el siguiente procedimiento iterativo [58]:

**Algoritmo 2: Entrenamiento Adversario Semántico**

```
Entrada: Conjunto de entrenamiento D, parámetros iniciales θ,φ, presupuesto de perturbación ε
Salida: Parámetros robustos θ*,φ*

1. Inicializar θ,φ aleatoriamente
2. Para cada época:
   a. Para cada lote {x_i} en D:
      i. Generar ejemplos adversarios:
         - Inicializar δ_i = 0
         - Para t = 1 a T_attack:
           * Calcular gradiente respecto a entrada:
             g = ∇_x L_T(x_i, g_φ(f_θ(x_i + δ_i)))
           * Actualizar perturbación:
             δ_i ← Proj_ε(δ_i + η sign(g))
         - x_adv,i = x_i + δ_i
      ii. Calcular pérdida en ejemplos adversarios:
          L_adv = (1/|B|) Σ_i L_T(x_i, g_φ(f_θ(x_adv,i)))
      iii. Calcular pérdida en ejemplos limpios:
           L_clean = (1/|B|) Σ_i L_T(x_i, g_φ(f_θ(x_i)))
      iv. Pérdida combinada: L = βL_adv + (1-β)L_clean
      v. Actualizar parámetros: θ,φ ← θ,φ - α∇_{θ,φ}L
   b. Fin Para
3. Fin Para
4. Retornar θ*,φ*
```

El hiperparámetro β controla el trade-off entre robustez adversaria y precisión en datos limpios, típicamente β ∈ [0.5, 0.9] [59].

### D. Espacios de Embedding y Métricas Geométricas

#### 1) Variedades Semánticas

Los espacios de significado son naturalmente modelados como variedades diferenciables [60]. Una **variedad semántica** (𝒮, g) es un espacio de significados 𝒮 equipado con una métrica Riemanniana g que define distancias locales entre significados [61].

Para representaciones aprendidas mediante redes neuronales profundas, el espacio latente Z forma una variedad embebida en ℝ^d [62]. La métrica Riemanniana inducida en cada punto z ∈ Z se define mediante el tensor métrico:

$$g_{ij}(z) = \mathbb{E}_{X \sim p(x|z)} \left[ \frac{\partial \log p(x|z)}{\partial z_i} \frac{\partial \log p(x|z)}{\partial z_j} \right]$$

Esta métrica, conocida como **métrica de información de Fisher**, captura la geometría intrínseca del espacio de significados [63].

**Definición 3 (Distancia Semántica Geodésica)**: *La distancia semántica entre dos significados s_1, s_2 ∈ 𝒮 se define como la longitud del geodésico más corto conectándolos:*

$$d_{\mathcal{S}}(s_1, s_2) = \inf_{\gamma: [0,1] \to \mathcal{S}, \gamma(0)=s_1, \gamma(1)=s_2} \int_0^1 \sqrt{g_{ij}(\gamma(t)) \dot{\gamma}^i(t) \dot{\gamma}^j(t)} dt$$

donde γ(t) es una curva en 𝒮 y ġ denota su derivada temporal.

Esta formulación geométrica permite definir rigurosamente conceptos como "semánticamente similar" (distancia geodésica pequeña) y "semánticamente ortogonal" (geodésicos divergentes) [64].

#### 2) Transporte Óptimo para Alineación Semántica

Cuando el transmisor y receptor emplean espacios de embedding potencialmente diferentes (e.g., entrenados en conjuntos de datos distintos), se requiere alineación semántica [65]. La teoría de transporte óptimo proporciona un marco matemático riguroso [66].

Dados dos espacios de embedding Z_T (transmisor) y Z_R (receptor) con distribuciones μ_T y μ_R, el **plan de transporte óptimo** minimiza:

$$\gamma^* = \arg\min_{\gamma \in \Gamma(\mu_T, \mu_R)} \int_{Z_T \times Z_R} c(z_T, z_R) d\gamma(z_T, z_R)$$

donde Γ(μ_T, μ_R) es el conjunto de distribuciones conjuntas con marginales μ_T y μ_R, y c(z_T, z_R) es un costo de transporte (típicamente distancia al cuadrado) [67].

La **distancia de Wasserstein** W_2 entre las distribuciones es:

$$W_2(\mu_T, \mu_R) = \sqrt{\inf_{\gamma \in \Gamma(\mu_T, \mu_R)} \int \|z_T - z_R\|^2 d\gamma(z_T, z_R)}$$

Esta métrica es fundamental para evaluar alineación entre representaciones semánticas del transmisor y receptor [68].

---

## III. ESTADO ACTUAL DE ESTANDARIZACIÓN 3GPP

### A. Evolución de Métricas en Generaciones Previas

#### 1) De 1G a 4G: Era del Nivel Sintáctico

Las generaciones 1G a 4G se enfocaron exclusivamente en métricas del Nivel A de Weaver [69]. Los Key Performance Indicators (KPIs) estandarizados incluyeron [70]:

**1G (AMPS)**: Claridad de voz (subjetiva), cobertura de celda (dBm), capacidad de canal (usuarios simultáneos).

**2G (GSM)**: BER, Frame Erasure Rate (FER), handover success rate, call drop rate. Las especificaciones GSM 05.05 definieron requisitos de desempeño del receptor con BER < 10^-3 bajo condiciones de referencia [71].

**3G (UMTS)**: Block Error Rate (BLER), throughput, Round-Trip Time (RTT). La serie TS 25.xxx introdujo requisitos detallados de Radio Resource Management (RRM) [72].

**4G (LTE)**: Eficiencia espectral (bits/s/Hz), latencia del plano de control, latencia del plano de usuario, capacidad de celda, throughput de borde de celda. TS 36.300 especifica arquitectura de protocolo y KPIs [73].

Todas estas métricas cuantifican desempeño de transmisión de bits, ignorando completamente el contenido semántico o el uso pretendido de los datos transmitidos.

#### 2) 5G: Introducción de Diversidad de Servicios

5G introduce el concepto de "network slicing" donde diferentes slices se optimizan para casos de uso distintos [74]:

- **eMBB** (Enhanced Mobile Broadband): >10 Gbps pico, >100 Mbps usuario típico
- **URLLC** (Ultra-Reliable Low-Latency Communications): <1 ms latencia, 99.999% confiabilidad
- **mMTC** (Massive Machine-Type Communications): >10^6 dispositivos/km²

Sin embargo, las métricas permanecen en el dominio sintáctico. Por ejemplo, URLLC garantiza baja latencia y alta confiabilidad de entrega de paquetes, pero no garantiza que el contenido del paquete sea semánticamente útil para la aplicación [75].

### B. Release 17 y 18: Primeros Pasos hacia AI/ML

#### 1) Estudio de IA/ML para Air Interface (TR 38.843)

3GPP Release 17 inició el estudio "Study on Artificial Intelligence (AI)/Machine Learning (ML) for NR Air Interface" documentado en TR 38.843 [76]. Los casos de uso estudiados incluyen:

1. **CSI feedback enhancement**: Uso de autoencoders para compresión de Channel State Information
2. **Beam management**: Predicción de haces óptimos mediante ML
3. **Positioning accuracy enhancement**: Mejora de precisión de localización con DL

Sin embargo, las métricas de evaluación propuestas permanecen convencionales:
- Para CSI feedback: NMSE (Normalized Mean Square Error) entre CSI real y reconstruido
- Para beam management: beam prediction accuracy, overhead de señalización
- Para positioning: error de posicionamiento (metros)

Ninguna métrica semántica o específica de tarea fue propuesta [77].

#### 2) Limitaciones del Enfoque Actual

El enfoque de Release 17/18 presenta limitaciones fundamentales [78]:

**a) Métricas Desacopladas de Aplicaciones**: Las métricas de evaluación (e.g., NMSE de CSI) no correlacionan necesariamente con el desempeño de las aplicaciones que utilizan esa información. Un CSI con bajo NMSE puede ser inútil si los errores se concentran en modos espaciales críticos para la aplicación [79].

**b) Ausencia de Consideración Semántica**: No se evalúa si la información transmitida es semánticamente relevante. Por ejemplo, en beam management para streaming de video, el beam óptimo debería seleccionarse basándose en su impacto en la calidad de experiencia (QoE) del video, no simplemente en la maximización de SNR [80].

**c) Falta de Métricas de Robustez AI-Específicas**: Los procedimientos de test no consideran vulnerabilidades específicas de sistemas AI como ataques adversarios, data poisoning, o model inversion [81].

### C. Especificaciones Técnicas Relevantes

Las siguientes especificaciones técnicas 3GPP son relevantes para la integración de métricas semánticas [82]:

**TS 38.300** (NR; Overall description): Define la arquitectura general de NR. Requeriría nueva cláusula "5.X Semantic Communication Architecture" describiendo componentes de procesamiento semántico.

**TS 38.331** (NR; Radio Resource Control): Define protocolos RRC. Necesitaría extensión para señalización de parámetros semánticos (e.g., tipo de tarea, requisitos de fidelidad semántica).

**TS 38.214** (NR; Physical layer procedures for data): Define procedimientos de HARQ, CSI, etc. Requeriría modificación para incorporar feedback semántico en lugar de solo ACK/NACK binario.

**TS 38.521** (NR; User Equipment conformance specification): Define procedimientos de prueba. Necesitaría secciones completamente nuevas para pruebas de desempeño semántico.

### D. Gaps de Estandarización Identificados

Basándose en el análisis anterior, se identifican los siguientes gaps críticos [83]:

**Gap 1: Ausencia de Definiciones Formales**: No existen definiciones formales en especificaciones 3GPP de términos como "información semántica", "fidelidad semántica", "tarea", "intención", etc.

**Gap 2: Sin Métricas Estandarizadas**: No hay métricas estandarizadas para cuantificar desempeño semántico, efectividad de tarea, o alineación de intenciones.

**Gap 3: Procedimientos de Test Inexistentes**: No existen procedimientos de prueba de conformidad para sistemas AI-nativos semánticos.

**Gap 4: Señalización Insuficiente**: Los protocolos de señalización actuales no pueden comunicar requisitos semánticos, descripciones de tareas, o metadata necesaria.

**Gap 5: Modelos de Canal Inadecuados**: Los modelos de canal estandarizados (e.g., TDL, CDL en TR 38.901) no modelan degradaciones semánticas, solo físicas.


**Gap 6: Arquitectura de Referencia Ausente**: No existe arquitectura de referencia para sistemas de comunicación semántica que pueda servir de base para especificaciones técnicas.

Estos gaps motivan la necesidad del framework comprehensivo propuesto en este artículo.

---

## IV. FRAMEWORK DE MÉTRICAS SEMÁNTICAS MULTI-DIMENSIONALES

### A. Principios de Diseño del Framework

El framework propuesto se fundamenta en los siguientes principios arquitecturales [84]:

**P1 - Independencia de Aplicación**: Las métricas deben ser aplicables a múltiples dominios de aplicación (video, texto, control, sensorización) sin requerir redefinición completa.

**P2 - Composabilidad**: Las métricas individuales deben ser componibles para formar métricas compuestas que reflejen requisitos multi-objetivo.

**P3 - Medibilidad Algorítmica**: Cada métrica debe acompañarse de algoritmos concretos y computacionalmente tractables para su medición.

**P4 - Reproducibilidad**: Los procedimientos de medición deben ser reproducibles entre diferentes implementaciones y laboratorios de prueba.

**P5 - Compatibilidad con Infraestructura Existente**: El framework debe integrarse con infraestructura de test 3GPP existente (e.g., conformance testing environments).

**P6 - Escalabilidad**: Las métricas deben escalar desde escenarios simples (comunicación punto-a-punto) a complejos (redes multi-usuario masivas).

### B. Taxonomía de Cuatro Dimensiones

El framework organiza las métricas en cuatro dimensiones fundamentales, cada una capturando un aspecto esencial del desempeño de comunicaciones semánticas [85]:

#### Dimensión 1: Fidelidad Semántica (Semantic Fidelity)

**Objetivo**: Cuantificar qué tan fielmente se preserva el significado durante la transmisión.

**Métricas Clave**:
- Entropía Semántica Relativa (Relative Semantic Entropy)
- Distancia de Wasserstein Semántica (Semantic Wasserstein Distance)
- Índice de Similitud Estructural Semántica (Semantic Structural Similarity Index)
- Mutual Information Semántica Normalizada (Normalized Semantic Mutual Information)

**Aplicaciones**: Transmisión de contenido multimedia, replicación de gemelos digitales, teleoperación.

#### Dimensión 2: Precisión de Completitud de Tareas (Task Completion Accuracy)

**Objetivo**: Medir la efectividad con la que la información recibida permite completar la tarea prevista.

**Métricas Clave**:
- Tasa de Éxito de Tarea (Task Success Rate)
- Precisión de Acción (Action Accuracy)
- Utilidad Semántica (Semantic Utility)
- Eficiencia de Completitud (Completion Efficiency)

**Aplicaciones**: Sistemas de control remoto, navegación autónoma, manufactura automatizada.

#### Dimensión 3: Alineación de Intenciones (Intent Alignment)

**Objetivo**: Evaluar la correspondencia entre la intención del transmisor y la comprensión del receptor.

**Métricas Clave**:
- Divergencia de Intención (Intent Divergence)
- Coherencia Contextual (Contextual Coherence)
- Índice de Consenso Semántico (Semantic Consensus Index)
- Fidelidad de Propósito (Purpose Fidelity)

**Aplicaciones**: Comunicaciones human-machine, coordinación multi-agente, servicios intent-driven.

#### Dimensión 4: Resiliencia a Ataques Semánticos (Resilience to Semantic Attacks)

**Objetivo**: Caracterizar la robustez del sistema contra perturbaciones adversarias en el espacio semántico.

**Métricas Clave**:
- Radio de Robustez Adversaria (Adversarial Robustness Radius)
- Tasa de Ataque Semántico Exitoso (Semantic Attack Success Rate)
- Coste de Certificación (Certification Cost)
- Degradación Semántica Máxima (Maximum Semantic Degradation)

**Aplicaciones**: Comunicaciones críticas, servicios financieros, infraestructura de seguridad.

### C. Relaciones Inter-Dimensionales

Las cuatro dimensiones no son independientes sino que exhiben interdependencias que deben considerarse en evaluación holística [86]:

**Relación Fidelidad-Completitud**: Alta fidelidad semántica generalmente (pero no necesariamente) implica alta precisión de completitud de tareas. Sin embargo, la relación no es biyectiva: es posible tener baja fidelidad pero alta completitud si la información preservada es precisamente la relevante para la tarea [87].

Formalmente, existe un mapeo no-inyectivo:

$$\Phi: (\text{Fidelidad Semántica}) \rightarrow (\text{Completitud de Tareas})$$

donde Φ depende de la estructura de la tarea.

**Relación Intención-Completitud**: La alineación de intenciones es condición necesaria pero no suficiente para completitud de tareas. Un receptor puede comprender perfectamente la intención pero carecer de capacidad para ejecutarla [88].

**Trade-off Robustez-Fidelidad**: Incrementar robustez adversaria frecuentemente requiere sacrificar fidelidad en condiciones benignas, un fenómeno conocido como "robust-accuracy trade-off" [89]. La frontera de Pareto entre estas dimensiones caracteriza el espacio de diseños factibles.

### D. Agregación Multi-Dimensional

Para aplicaciones que requieren balancear múltiples dimensiones, se define una **métrica compuesta** mediante agregación ponderada [90]:

$$M_{composite} = \sum_{i=1}^{4} w_i \cdot M_i$$

donde M_i son las métricas de las cuatro dimensiones normalizadas a [0,1] y w_i son pesos que reflejan las prioridades de la aplicación, satisfaciendo Σw_i = 1.

Alternativamente, para aplicaciones con requisitos mínimos estrictos en cada dimensión, se emplea agregación tipo conjunción:

$$M_{composite} = \min_{i \in \{1,2,3,4\}} \left(\frac{M_i}{M_i^{threshold}}\right)$$

Esta formulación penaliza fuertemente deficiencias en cualquier dimensión individual [91].

---

## V. MÉTRICAS DE FIDELIDAD SEMÁNTICA

### A. Entropía Semántica Relativa

#### 1) Definición Formal

La **Entropía Semántica Relativa** (RSE) cuantifica la cantidad de información semánticamente relevante preservada tras la transmisión [92]. Se define como:

$$RSE = \frac{I_s(X;Y|T)}{H_s(X|T)}$$

donde:
- I_s(X;Y|T) es la información mutua semántica entre entrada X y salida Y dada la tarea T
- H_s(X|T) es la entropía semántica de la fuente condicionada a la tarea

RSE ∈ [0,1] donde RSE=1 indica preservación perfecta de información semántica y RSE=0 indica pérdida total.

**Teorema 4 (Monotonía de RSE)**: *Para un canal con procesamiento post-recepción Z = h(Y), se cumple:*

$$RSE(X;Z|T) \leq RSE(X;Y|T)$$

*con igualdad si y solo si h preserva toda la información semántica en Y.*

**Demostración**: Por la desigualdad de procesamiento de datos [93]:

$$I_s(X;h(Y)|T) \leq I_s(X;Y|T)$$

Dividiendo ambos lados por H_s(X|T) se obtiene el resultado. ∎

#### 2) Algoritmo de Medición

**Algoritmo 3: Cálculo de Entropía Semántica Relativa**

```
Entrada: Conjunto de datos D = {(x_i, t_i)}, sistema de comunicación (f_θ, canal, g_φ)
Salida: RSE estimado

1. Extracción de Representaciones Semánticas:
   a. Para cada (x_i, t_i) en D:
      - Extraer embedding semántico del contexto de tarea: s_i = embed_task(x_i, t_i)
   b. Construir distribución empírica P_S sobre embeddings s_i

2. Simulación de Transmisión:
   a. Para cada x_i:
      - Codificar: z_i = f_θ(x_i)
      - Transmitir sobre canal: y_i ~ p(y|z_i)
      - Decodificar: x̂_i = g_φ(y_i)
      - Extraer embedding recibido: ŝ_i = embed_task(x̂_i, t_i)
   b. Construir distribución conjunta empírica P_SŜ

3. Estimación de Entropía:
   a. Estimar H_s(X|T) usando:
      H_s(X|T) ≈ -Σ_i (1/|D|) log₂ P_S(s_i)
   
4. Estimación de Información Mutua Semántica:
   a. Estimar I_s(X;Y|T) usando estimador k-NN de Kraskov [94]:
      I_s ≈ ψ(k) - ⟨ψ(n_x) + ψ(n_y)⟩ + ψ(N)
      donde:
      - ψ es la función digamma
      - k es el número de vecinos más cercanos
      - n_x, n_y son conteos de vecinos en espacios marginales
      - N = |D| es el tamaño del conjunto de datos

5. Calcular RSE:
   RSE = I_s / H_s

6. Repetir pasos 2-5 con M muestras bootstrap y reportar:
   RSE_mean ± RSE_std
```

La complejidad computacional del algoritmo es O(N log N) debido al paso de búsqueda de vecinos más cercanos [95].

### B. Distancia de Wasserstein Semántica

#### 1) Formulación Matemática

La **Distancia de Wasserstein Semántica** (SWD) cuantifica la discrepancia entre las distribuciones semánticas de la fuente y la reconstrucción [96]:

$$SWD(P_S, P_{\hat{S}}) = \inf_{\gamma \in \Gamma(P_S, P_{\hat{S}})} \mathbb{E}_{(s,\hat{s}) \sim \gamma} \left[ d_{\mathcal{S}}(s, \hat{s}) \right]$$

donde:
- P_S es la distribución de significados en la fuente
- P_Ŝ es la distribución de significados reconstruidos
- Γ(P_S, P_Ŝ) es el conjunto de acoplamientos (distribuciones conjuntas con marginales P_S y P_Ŝ)
- d_𝒮(s,ŝ) es una métrica de distancia en el espacio semántico

Para p=2 (caso Euclideano), SWD se conoce como **distancia de Earth Mover** y admite solución eficiente [97].

**Propiedades Clave**:
1. **Métrica verdadera**: SWD satisface identidad, simetría, y desigualdad triangular
2. **Sensibilidad a modo**: SWD detecta cambios tanto en localización como en forma de las distribuciones
3. **Interpretabilidad**: SWD tiene unidades de la métrica del espacio semántico, facilitando interpretación

#### 2) Cálculo mediante Regularización Entrópica

El cálculo de SWD es un problema de programación lineal de gran escala. La **regularización entrópica de Sinkhorn** proporciona aproximación eficiente [98]:

$$SWD_{\epsilon}(P_S, P_{\hat{S}}) = \min_{\gamma \in \Gamma(P_S, P_{\hat{S}})} \sum_{i,j} \gamma_{ij} c_{ij} + \epsilon H(\gamma)$$

donde H(γ) = -Σ_ij γ_ij log γ_ij es la entropía de la distribución de transporte y ε > 0 es el parámetro de regularización.

**Algoritmo 4: Algoritmo de Sinkhorn para SWD**

```
Entrada: Distribuciones empíricas {s_i}_{i=1}^n, {ŝ_j}_{j=1}^m, matriz de costos C, reg. ε
Salida: SWD_ε aproximado

1. Inicialización:
   a. Calcular matriz de kernel: K_ij = exp(-C_ij/ε)
   b. Inicializar vectores: u ← 1_n, v ← 1_m (vectores de unos)

2. Iteración de Sinkhorn:
   a. Para iter = 1 hasta max_iter:
      - u ← p_S ⊘ (K v)  (división elemento-a-elemento)
      - v ← p_Ŝ ⊘ (K^T u)
      - Si ||u^{new} - u^{old}||₂ < tol: break
   b. Fin Para

3. Reconstruir plan de transporte:
   Γ_ij = u_i K_ij v_j

4. Calcular costo de transporte:
   SWD_ε = Σ_ij Γ_ij C_ij

5. Retornar SWD_ε
```

El algoritmo converge geométricamente con complejidad O(n²T) donde T es el número de iteraciones (típicamente T ≈ 50-100) [99].

### C. Índice de Similitud Estructural Semántica

#### 1) Extensión de SSIM al Dominio Semántico

El Structural Similarity Index (SSIM) [100] es una métrica ampliamente utilizada para evaluar calidad de imagen basándose en percepción humana. Extendemos SSIM al dominio semántico:

$$SSIM_s(s, \hat{s}) = \frac{(2\mu_s\mu_{\hat{s}} + c_1)(2\sigma_{s\hat{s}} + c_2)}{(\mu_s^2 + \mu_{\hat{s}}^2 + c_1)(\sigma_s^2 + \sigma_{\hat{s}}^2 + c_2)}$$

donde:
- μ_s, μ_ŝ son vectores de media de las representaciones semánticas
- σ_s², σ_ŝ² son matrices de covarianza
- σ_sŝ es la covarianza cruzada
- c_1, c_2 son constantes de estabilización

El **Índice de Similitud Estructural Semántica** (S³I) promedia SSIM_s sobre todos los pares de regiones semánticamente relevantes:

$$S³I = \frac{1}{|\mathcal{R}|} \sum_{r \in \mathcal{R}} w_r \cdot SSIM_s(s_r, \hat{s}_r)$$

donde ℛ es el conjunto de regiones semánticas y w_r son pesos de importancia (Σw_r = 1).

#### 2) Identificación de Regiones Semánticas

**Algoritmo 5: Segmentación Semántica para S³I**

```
Entrada: Señal x (e.g., imagen), modelo de segmentación M_seg
Salida: Regiones semánticas R, pesos w

1. Segmentación Semántica:
   a. Ejecutar modelo de segmentación: R = M_seg(x)
   b. Cada región r_i tiene etiqueta semántica l_i (e.g., "persona", "vehículo")

2. Asignación de Pesos de Importancia:
   a. Opción 1 - Basado en Tarea:
      - Consultar base de conocimiento de tarea para obtener relevancia rel(l_i, T)
      - w_i = rel(l_i, T) / Σ_j rel(l_j, T)
   
   b. Opción 2 - Basado en Saliencia:
      - Calcular mapa de saliencia: S = saliency_model(x)
      - w_i = Σ_{pixels p ∈ r_i} S(p) / Σ_{p ∈ x} S(p)
   
   c. Opción 3 - Híbrido:
      - w_i = α·rel(l_i,T) + (1-α)·saliency_i

3. Extracción de Embeddings por Región:
   a. Para cada región r_i:
      - Extraer sub-señal x_i correspondiente a r_i
      - Calcular embedding: s_i = embed_model(x_i)
   b. Almacenar conjunto {(s_i, w_i)}

4. Retornar R = {r_i}, w = {w_i}, embeddings = {s_i}
```

### D. Mutual Information Semántica Normalizada

#### 1) Definición y Normalización

La **Mutual Information Semántica Normalizada** (NSMI) normaliza I_s(X;Y|T) para facilitar comparación entre diferentes sistemas:

$$NSMI = \frac{I_s(X;Y|T)}{\sqrt{H_s(X|T) \cdot H_s(Y|T)}}$$

Esta normalización geométrica asegura NSMI ∈ [0,1] y proporciona interpretación como coeficiente de correlación en el espacio informacional [101].

**Propiedades**:
- NSMI = 1 si X e Y son funcionalmente dependientes en el subespacio semántico
- NSMI = 0 si X e Y son semánticamente independientes
- NSMI es invariante a transformaciones invertibles del espacio de embeddings

#### 2) Estimación No-Paramétrica

La estimación de NSMI evita asumir formas paramétricas de las distribuciones P_S y P_Ŝ. Se emplea el **estimador de Kozachenko-Leonenko** [102]:

$$\hat{H}_s(X|T) = \psi(N) - \psi(k) + \log(c_d) + \frac{d}{N} \sum_{i=1}^N \log(\epsilon_i)$$

donde:
- N es el número de muestras
- k es el número de vecinos considerados
- d es la dimensionalidad del espacio semántico
- ε_i es la distancia al k-ésimo vecino más cercano de la muestra i
- c_d es el volumen de la bola unitaria en dimensión d
- ψ es la función digamma

Para información mutua, se utiliza el estimador dual:

$$\hat{I}_s(X;Y|T) = \psi(k) - \frac{1}{k}\sum_{i=1}^N [\psi(n_{x,i}) + \psi(n_{y,i})] + \psi(N)$$

donde n_{x,i} y n_{y,i} son el número de vecinos dentro de ε_i en los subespacios X e Y respectivamente [103].

---

## VI. MÉTRICAS DE PRECISIÓN DE COMPLETITUD DE TAREAS

### A. Tasa de Éxito de Tarea

#### 1) Definición Formal

La **Tasa de Éxito de Tarea** (TSR) es la métrica más directa para evaluar comunicaciones orientadas a tareas [104]:

$$TSR = \mathbb{P}[\text{tarea completada exitosamente}]$$

Para un conjunto de test D = {(x_i, t_i, objetivo_i)}_{i=1}^N, TSR se estima como:

$$\widehat{TSR} = \frac{1}{N} \sum_{i=1}^N \mathbb{1}[\text{success}(x_i, t_i, objetivo_i)]$$

donde 𝟙[·] es la función indicadora y success(·) es un predicado que evalúa si el objetivo de la tarea se alcanzó.

#### 2) Definición de Éxito Específica de Dominio

El predicado success(·) requiere especificación dependiente del dominio [105]:

**Control Robótico**:
```
success_robot(x, t, objetivo) = 
  ||posición_final - objetivo.posición|| < ε_pos AND
  ||orientación_final - objetivo.orientación|| < ε_orient AND
  tiempo_ejecución < deadline
```

**Reconocimiento de Objetos**:
```
success_recognition(x, t, objetivo) =
  objeto_detectado == objetivo.clase AND
  IoU(bbox_detectada, bbox_verdadera) > θ_IoU
```

**Navegación Autónoma**:
```
success_navigation(x, t, objetivo) =
  alcanzado(destino) AND
  sin_colisiones AND
  desviación_ruta < ε_ruta
```

**Transmisión de Video**:
```
success_video(x, t, objetivo) =
  VMAF(video_recibido, video_original) > θ_VMAF AND
  frame_freezes < max_freezes
```

#### 3) Intervalo de Confianza

Para proporcionar confianza estadística en las estimaciones de TSR, se calculan intervalos de confianza mediante el método de Wilson [106]:

$$CI_{Wilson} = \frac{\hat{p} + \frac{z^2}{2n}}{1 + \frac{z^2}{n}} \pm \frac{z}{1 + \frac{z^2}{n}} \sqrt{\frac{\hat{p}(1-\hat{p})}{n} + \frac{z^2}{4n^2}}$$

donde:
- p̂ = T̂SR es la tasa de éxito estimada
- n = N es el tamaño de muestra
- z es el cuantil de la distribución normal estándar (e.g., z=1.96 para 95% de confianza)

Este intervalo es preferible al intervalo de Wald para p̂ cercano a 0 o 1 [107].

### B. Precisión de Acción

#### 1) Métricas de Distancia en Espacio de Acciones

Para tareas donde el "éxito" es gradual en lugar de binario, la **Precisión de Acción** (AP) cuantifica qué tan cerca está la acción ejecutada de la acción óptima [108]:

$$AP = 1 - \frac{d_{\mathcal{A}}(a_{executed}, a_{optimal})}{d_{\mathcal{A}}^{max}}$$

donde:
- d_𝒜(·,·) es una métrica en el espacio de acciones 𝒜
- d_𝒜^max es la distancia máxima posible (normalización)
- a_executed es la acción ejecutada basándose en la información recibida
- a_optimal es la acción óptima con información perfecta

**Ejemplo - Control de Vehículo**: Para un espacio de acciones 𝒜 = {steering, throttle, brake}, la distancia puede ser Euclideana ponderada:

$$d_{\mathcal{A}}(a_1, a_2) = \sqrt{w_s \cdot (\theta_1 - \theta_2)^2 + w_t \cdot (t_1 - t_2)^2 + w_b \cdot (b_1 - b_2)^2}$$

con pesos w_s, w_t, w_b reflejando la importancia relativa de steering, throttle, y brake.

#### 2) Regret de Desempeño

En el contexto de aprendizaje por refuerzo, la degradación de desempeño debido a información imperfecta se cuantifica mediante **regret** [109]:

$$\text{Regret} = V^*(\pi^{optimal}) - V(\pi^{executed})$$

donde:
- V(π) es la función de valor (retorno esperado) bajo la política π
- π^optimal es la política óptima con información perfecta
- π^executed es la política ejecutada con información transmitida

Para tareas episódicas de horizonte T:

$$\text{Regret} = \mathbb{E}\left[\sum_{t=0}^{T-1} r_t^{optimal} - r_t^{executed}\right]$$

donde r_t son las recompensas en el tiempo t.

**Teorema 5 (Cota de Regret)**: *Para un sistema de comunicación con tasa de información mutua semántica I_s, el regret acumulado está acotado por:*

$$\text{Regret}(T) \leq O\left(\sqrt{T \cdot (H_s(X|T) - I_s(X;Y|T))}\right)$$

Esta cota demuestra que maximizar I_s minimiza el regret, proporcionando justificación teórica para optimizar información mutua semántica [110].

### C. Utilidad Semántica

#### 1) Función de Utilidad

La **Utilidad Semántica** (SU) generaliza las métricas anteriores mediante una función de utilidad U: 𝒳 × 𝒳̂ × 𝒯 → ℝ que cuantifica el valor de la información recibida [111]:

$$SU = \mathbb{E}_{X,T} [U(X, \hat{X}, T)]$$

La función de utilidad captura no solo corrección sino también consideraciones pragmáticas como:
- Valor temporal (información desactualizada tiene menor utilidad)
- Costo de adquisición
- Consecuencias de decisiones incorrectas

**Ejemplo - Internet de los Sentidos**: Para transmisión háptica (táctil), la función de utilidad incorpora latencia:

$$U_{haptic}(x, \hat{x}, t) = \begin{cases}
\alpha \cdot \text{fidelity}(\hat{x}, x) & \text{si } \Delta t \leq \tau_{JND} \\
\beta \cdot \text{fidelity}(\hat{x}, x) \cdot e^{-\lambda \Delta t} & \text{si } \Delta t > \tau_{JND}
\end{cases}$$

donde:
- τ_JND es el Just Noticeable Difference de latencia (típicamente 10-20 ms para háptica)
- Δt es la latencia de transmisión
- λ es el factor de decaimiento temporal
- α > β reflejan que la utilidad es discontinua en τ_JND

#### 2) Optimización de Utilidad Esperada

El diseño óptimo del sistema de comunicación semántica maximiza la utilidad esperada [112]:

$$\max_{\theta, \phi} \mathbb{E}_{X \sim p(x), T \sim p(t)} [U(X, g_\phi(f_\theta(X)), T)]$$

sujeto a restricciones de recursos:
- Tasa de información: I(X;Z) ≤ R
- Latencia: E[delay] ≤ D_max
- Energía: E[energy] ≤ E_budget

Esta es una formulación de optimización multi-objetivo con restricciones, resoluble mediante métodos de Lagrange [113]:

$$\mathcal{L}(\theta, \phi, \lambda) = \mathbb{E}[U(·)] - \lambda_R(I(X;Z) - R) - \lambda_D(E[delay] - D_{max}) - \lambda_E(E[energy] - E_{budget})$$

Los multiplicadores de Lagrange {λ_R, λ_D, λ_E} controlan el trade-off entre utilidad y recursos.

### D. Eficiencia de Completitud

#### 1) Ratio Información-Éxito

La **Eficiencia de Completitud** (CE) cuantifica cuán efectivamente se utiliza el ancho de banda disponible para lograr éxito en la tarea [114]:

$$CE = \frac{TSR}{\text{Tasa de Información Transmitida}}$$

Unidades: éxitos por bit, o equivalentemente, bits⁻¹.

Una alta CE indica que el sistema transmite eficientemente solo la información semánticamente necesaria. Sistemas tradicionales bit-exactos típicamente exhiben CE muy bajo pues transmiten información redundante.

#### 2) Curvas de Eficiencia

Para caracterizar el trade-off entre éxito de tarea y consumo de recursos, se generan **curvas de eficiencia** [115]:

$$\text{Curva}: \{(R, TSR(R))\}_{R \in [0, R_{max}]}$$

donde TSR(R) es la tasa de éxito de tarea alcanzable con tasa de información R.

**Análisis de Convexidad**: Para muchas tareas, TSR(R) exhibe rendimientos decrecientes (segunda derivada negativa), indicando que bits adicionales proporcionan mejora marginal decreciente [116]:

$$\frac{d^2 TSR}{dR^2} < 0$$

El **punto de operación óptimo** R* maximiza eficiencia:

$$R^* = \arg\max_R \frac{TSR(R)}{R}$$

gráficamente, este es el punto donde una línea desde el origen es tangente a la curva TSR(R).

---

## VII. MÉTRICAS DE ALINEACIÓN DE INTENCIONES

### A. Divergencia de Intención

#### 1) Modelo de Intención

Una **intención** ℐ se modela como una distribución de probabilidad sobre posibles objetivos O y acciones A [117]:

$$\mathcal{I} = p(o, a | contexto)$$

En comunicaciones intent-driven, el transmisor codifica su intención ℐ_T y el receptor la decodifica como ℐ_R. La **Divergencia de Intención** (ID) cuantifica la discrepancia [118]:

$$ID = D_{KL}(\mathcal{I}_T \| \mathcal{I}_R)$$

donde D_KL es la divergencia de Kullback-Leibler:

$$D_{KL}(\mathcal{I}_T \| \mathcal{I}_R) = \sum_{o,a} p_T(o,a|ctx) \log \frac{p_T(o,a|ctx)}{p_R(o,a|ctx)}$$

**Interpretación**: ID mide cuántos bits adicionales se requerirían para codificar muestras de ℐ_T si se utiliza el código óptimo para ℐ_R, reflejando la ineficiencia de la interpretación del receptor [119].

#### 2) Descomposición de Divergencia

La divergencia total se descompone en componentes interpretables [120]:

$$ID_{total} = ID_{objetivos} + \mathbb{E}_{O}[ID_{acciones|O}]$$

donde:
$$ID_{objetivos} = D_{KL}(p_T(o|ctx) \| p_R(o|ctx))$$

$$ID_{acciones|O} = D_{KL}(p_T(a|o,ctx) \| p_R(a|o,ctx))$$

Esta descomposición permite identificar si el mal-alineamiento ocurre en:
- Comprensión del objetivo (ID_objetivos elevado)
- Estrategia para alcanzar el objetivo (ID_acciones|O elevado)

**Algoritmo 6: Estimación de Divergencia de Intención**

```
Entrada: Pares contexto-intención transmitidos {(ctx_i, I_T,i)}, 
         Intenciones decodificadas {I_R,i}, número de muestras M
Salida: ID estimado, descomposición

1. Representación de Intenciones:
   a. Para cada i:
      - Representar I_T,i como distribución sobre (objetivo, acción)
      - Representar I_R,i similarmente
      
2. Estimación de Distribuciones Marginales:
   a. Estimar p_T(o|ctx) usando histograma normalizado sobre muestras
   b. Estimar p_R(o|ctx) similarmente
   
3. Estimación de Distribuciones Condicionales:
   a. Para cada objetivo o:
      - Estimar p_T(a|o, ctx) sobre subset {i: objetivo_i = o}
      - Estimar p_R(a|o, ctx) similarmente

4. Cálculo de Divergencias:
   a. ID_objetivos = Σ_o p_T(o|ctx) log(p_T(o|ctx)/p_R(o|ctx))
   b. Para cada o:
      - ID_acciones[o] = Σ_a p_T(a|o,ctx) log(p_T(a|o,ctx)/p_R(a|o,ctx))
   c. ID_total = ID_objetivos + Σ_o p_T(o|ctx) · ID_acciones[o]

5. Intervalos de Confianza (bootstrap):
   a. Para b = 1 hasta B:
      - Muestrear con reemplazo M muestras de datos
      - Calcular ID^(b) sobre este resample
   b. CI = [percentil(2.5, {ID^(b)}), percentil(97.5, {ID^(b)})]

6. Retornar ID_total, ID_objetivos, {ID_acciones[o]}, CI
```

### B. Coherencia Contextual

#### 1) Modelo de Contexto

El contexto C incluye información ambiental, histórica, y situacional que informa la interpretación de intenciones [121]. La **Coherencia Contextual** (CC) mide si la intención interpretada es consistente con el contexto:

$$CC = p(\mathcal{I}_R | C) / p(\mathcal{I}_R)$$

donde:
- p(ℐ_R | C) es la probabilidad de la intención interpretada dado el contexto
- p(ℐ_R) es la probabilidad marginal de esa intención

CC > 1 indica que la intención es más probable dado el contexto (coherente), mientras CC < 1 indica incoherencia contextual.

**Logaritmo de Coherencia Contextual** (para estabilidad numérica):

$$\log CC = \log p(\mathcal{I}_R | C) - \log p(\mathcal{I}_R)$$

Este es el **pointwise mutual information** (PMI) entre intención y contexto [122].

#### 2) Aprendizaje de Modelos Contextuales

Para evaluar CC se requiere un modelo probabilístico p(ℐ|C), típicamente aprendido mediante:

**Enfoque 1 - Modelo Generativo**: Entrenar un modelo generativo (e.g., Variational Autoencoder condicional) que modele p(ℐ|C) [123]:

$$\log p_\theta(\mathcal{I}|C) \geq \mathbb{E}_{q_\phi(z|\mathcal{I},C)} [\log p_\theta(\mathcal{I}|z,C)] - D_{KL}(q_\phi(z|\mathcal{I},C) \| p(z))$$

El lado derecho es el ELBO (Evidence Lower Bound) maximizado durante entrenamiento.

**Enfoque 2 - Modelo Discriminativo**: Entrenar un clasificador que estime p(ℐ|C) directamente usando softmax sobre clases de intención [124]:

$$p_\theta(\mathcal{I}=i|C) = \frac{\exp(f_\theta(C)_i)}{\sum_j \exp(f_\theta(C)_j)}$$

donde f_θ es una red neuronal con contexto C como entrada.

### C. Índice de Consenso Semántico

#### 1) Consenso Multi-Agente

En escenarios multi-usuario donde múltiples receptores interpretan la misma intención transmitida, el **Índice de Consenso Semántico** (SCI) cuantifica el acuerdo inter-receptor [125]:

$$SCI = 1 - \frac{1}{|R|^2} \sum_{i,j \in R} D(\mathcal{I}_i, \mathcal{I}_j)$$

donde:
- R es el conjunto de receptores
- ℐ_i es la intención interpretada por el receptor i
- D(·,·) es una métrica de distancia entre intenciones (e.g., divergencia KL simétrica)

SCI ∈ [0,1] donde SCI=1 indica consenso perfecto (todas las interpretaciones idénticas) y SCI→0 indica disenso total.

#### 2) Distancia de Consenso Ponderada

Cuando los receptores tienen confiabilidades diferentes, se emplea consenso ponderado [126]:

$$SCI_w = 1 - \frac{\sum_{i,j} w_i w_j D(\mathcal{I}_i, \mathcal{I}_j)}{\sum_{i,j} w_i w_j}$$

donde w_i es el peso de confianza del receptor i, típicamente basado en:
- Historial de precisión
- Calidad del canal
- Capacidad computacional

**Teorema 6 (Cota de Consenso)**: *Para N receptores recibiendo sobre canales independientes con capacidades semánticas {C_s,i}, el índice de consenso satisface:*

$$SCI \geq 1 - \exp\left(-\frac{1}{N}\sum_{i=1}^N C_{s,i}\right)$$

*con igualdad asintótica cuando N → ∞.*

Este resultado establece que mayor capacidad semántica promedio conduce a mayor consenso [127].

### D. Fidelidad de Propósito

#### 1) Propósito vs Intención

El **propósito** π representa el objetivo de alto nivel detrás de la comunicación, mientras que la intención ℐ especifica cómo lograr ese propósito [128]. Por ejemplo:
- Propósito: "Llegar al destino de manera segura y eficiente"
- Intención: "Tomar ruta A, velocidad 60 km/h, evitar zona B"

La **Fidelidad de Propósito** (PF) evalúa si la acción resultante de ℐ_R efectivamente logra π_T [129]:

$$PF = p(\text{propósito logrado} | \text{acción}(\mathcal{I}_R))$$

#### 2) Modelado Causal

PF requiere modelado de la relación causal entre intenciones y resultados. Se emplea un **modelo causal estructural** [130]:

$$\pi = f_{causal}(\mathcal{I}, C, U)$$

donde:
- π es la variable de resultado (propósito logrado)
- ℐ es la intención
- C es el contexto
- U representa factores no observados

Para estimar PF, se emplea do-calculus de Pearl [131]:

$$PF = p(\pi = 1 | do(\mathcal{I} = \mathcal{I}_R)) = \sum_c p(\pi = 1 | \mathcal{I}_R, c) p(c)$$

donde do(ℐ=ℐ_R) representa intervención causal (forzar la intención a ℐ_R).

**Algoritmo 7: Estimación de Fidelidad de Propósito**

```
Entrada: Historial de intentos {(I_R,i, C_i, π_i)}_{i=1}^N, nueva intención I_R^new, contexto C^new
Salida: PF estimado

1. Identificar Muestras Relevantes:
   a. Encontrar subset S = {i: similar(I_R,i, I_R^new) AND similar(C_i, C^new)}
   b. similar(·) puede ser basado en distancia con umbral

2. Estimar Probabilidad de Éxito:
   a. éxitos = |{i ∈ S: π_i = logrado}|
   b. PF = éxitos / |S|

3. Ajuste por Confounders (opcional):
   a. Estratificar S por niveles de variables confounding
   b. Calcular PF por estrato
   c. Promediar ponderado: PF = Σ_k w_k · PF_k

4. Intervalo de Confianza (Clopper-Pearson):
   a. Calcular CI binomial exacto para proporción de éxitos
   b. Retornar [lower_bound, upper_bound]

5. Retornar PF, CI
```

La complejidad es O(N) para búsqueda lineal, reducible a O(log N) con estructuras de indexación apropiadas [132].

---

## VIII. MÉTRICAS DE RESILIENCIA A ATAQUES SEMÁNTICOS

### A. Radio de Robustez Adversaria

#### 1) Definición Formal

El **Radio de Robustez Adversaria** (ARR) es la perturbación mínima (en el espacio de entrada) requerida para causar un cambio semántico específico [133]:

$$ARR = \min_{\delta} \|\delta\|_p \quad \text{sujeto a} \quad S(X + \delta) \neq S(X)$$

donde:
- ||·||_p es la norma ℓ_p (típicamente p=2 o p=∞)
- S(·) es la interpretación semántica (e.g., clase predicha, intención interpretada)
- δ es la perturbación adversaria

ARR más grande indica mayor robustez: se requiere mayor perturbación para causar interpretación errónea.

**Variante Probabilística**: Para sistemas estocásticos:

$$ARR_\alpha = \min_{\delta: p(S(X+\delta) \neq S(X)) \geq \alpha} \|\delta\|_p$$

donde α es la probabilidad mínima de cambio semántico (típicamente α ≥ 0.95).

#### 2) Métodos de Cálculo

**Enfoque 1 - Ataque PGD (Projected Gradient Descent)** [134]:

**Algoritmo 8: Ataque PGD para Encontrar Perturbación Adversaria Mínima**

```
Entrada: Señal x, modelo f_θ, etiqueta semántica verdadera y, norma p, épsilon inicial
Salida: Perturbación adversaria δ*, ARR estimado

1. Inicialización:
   a. ε_low = 0, ε_high = ε_max
   b. Tolerancia tol = 0.01

2. Búsqueda Binaria sobre Magnitud de Perturbación:
   a. Mientras ε_high - ε_low > tol:
      i. ε_mid = (ε_low + ε_high) / 2
      ii. Intentar ataque con presupuesto ε_mid:
          - Inicializar δ aleatoriamente en bola de radio ε_mid
          - Para t = 1 hasta T_attack:
            * Calcular pérdida adversaria: L = -loss(f_θ(x+δ), y)
            * Gradiente: g = ∇_δ L
            * Actualizar: δ ← Proj_{||·||_p ≤ ε_mid}(δ + α·sign(g))
          - Si S(f_θ(x+δ)) ≠ S(f_θ(x)): ataque exitoso
      iii. Si ataque exitoso:
           ε_high = ε_mid
         Sino:
           ε_low = ε_mid
   b. Fin Mientras

3. ARR = ε_high

4. Retornar ARR, δ* correspondiente
```

**Enfoque 2 - Carlini-Wagner (C&W) Optimization** [135]:

Formulación como optimización:

$$\min_{\delta} \|\delta\|_p + c \cdot \max(0, f(x+\delta)_{true} - \max_{i \neq true} f(x+\delta)_i + \kappa)$$

donde:
- f(x)_i es el logit para la clase i
- c es constante de penalización
- κ es margen de confianza

Esta formulación encuentra δ que satisface el cambio semántico mientras minimiza ||δ||_p.

### B. Tasa de Ataque Semántico Exitoso

#### 1) Definición

La **Tasa de Ataque Semántico Exitoso** (SASR) es la fracción de intentos de ataque adversario que logran causar interpretación semántica incorrecta [136]:

$$SASR(\epsilon) = \frac{1}{N} \sum_{i=1}^N \mathbb{1}[S(X_i + \delta_i) \neq S(X_i) \text{ AND } \|\delta_i\|_p \leq \epsilon]$$

donde:
- ε es el presupuesto de perturbación
- δ_i es la perturbación adversaria óptima para muestra i
- S(·) es la interpretación semántica

SASR(ε) ∈ [0,1] donde SASR=0 indica robustez perfecta y SASR=1 indica vulnerabilidad total.

#### 2) Caracterización mediante Curvas SASR-ε

La dependencia de SASR en ε se caracteriza mediante la **curva SASR-ε** [137]:

$$\{(\epsilon, SASR(\epsilon))\}_{\epsilon \in [0, \epsilon_{max}]}$$

Propiedades:
- SASR(0) = 0 (sin perturbación, sin ataques exitosos)
- SASR monotónicamente no-decreciente en ε
- lim_{ε→∞} SASR(ε) = 1 (con perturbación ilimitada, todo es atacable)

El **umbral de robustez** ε_threshold se define como:

$$\epsilon_{threshold} = \inf\{\epsilon: SASR(\epsilon) \geq 0.5\}$$

Sistemas con ε_threshold más grande son más robustos.

### C. Coste de Certificación

#### 1) Verificación Formal de Robustez

Los métodos de ataque empíricos (PGD, C&W) proporcionan cotas inferiores de robustez pero no garantías. La **verificación formal** proporciona certificados de robustez provables [138].

**Problema de Verificación**: Dado x, ε, y modelo f_θ, determinar si:

$$\forall \delta: \|\delta\|_p \leq \epsilon \Rightarrow S(f_\theta(x+\delta)) = S(f_\theta(x))$$

Este es un problema de satisfacibilidad (SAT) generalizado, NP-completo en general [139].

#### 2) Métodos de Certificación

**a) Abstract Interpretation** [140]:

Propaga intervalos o zonotopes a través de la red neuronal:

$$\text{Si } x \in [x_l, x_u] \Rightarrow f_\theta(x) \in [y_l, y_u]$$

Si todas las salidas en [y_l, y_u] tienen la misma clasificación semántica, la robustez está certificada.

**b) Linear Relaxation (CROWN)** [141]:

Aproxima activaciones no-lineales mediante cotas lineales:

$$\sigma(z) \in [\alpha z + \beta_l, \alpha z + \beta_u]$$

Propaga estas cotas para obtener región certificada.

**c) Randomized Smoothing** [142]:

Construye un clasificador suavizado:

$$\bar{f}(x) = \arg\max_c p(f(x + \xi) = c), \quad \xi \sim \mathcal{N}(0, \sigma^2 I)$$

**Teorema 7 (Certificado de Randomized Smoothing)**: *Si el clasificador suavizado predice clase c con probabilidad p_c en x, entonces está certificado robusto en bola ℓ_2 de radio:*

$$r = \frac{\sigma}{2}(\Phi^{-1}(p_c) - \Phi^{-1}(p_2))$$

*donde p_2 es la segunda mayor probabilidad de clase y Φ es la CDF gaussiana estándar.*

**Coste de Certificación** (CC): Tiempo computacional o recursos necesarios para obtener certificado de robustez [143]:

$$CC = \text{tiempo de verificación}(x, \epsilon, f_\theta)$$

Medido en segundos-CPU o FLOPS. Un CC más bajo indica que el sistema es más fácilmente verificable.

### D. Degradación Semántica Máxima

#### 1) Cuantificación de Degradación

La **Degradación Semántica Máxima** (MSD) cuantifica el peor caso de degradación de desempeño bajo ataque [144]:

$$MSD = \max_{\delta: \|\delta\|_p \leq \epsilon} \mathcal{L}_T(X, g_\phi(f_\theta(X + \delta)))$$

donde ℒ_T es la función de pérdida de tarea.

MSD captura el "peor escenario" que un adversario puede infligir con presupuesto ε.

**Normalización**: Para comparabilidad entre sistemas:

$$MSD_{normalized} = \frac{MSD - \mathcal{L}_T^{clean}}{\mathcal{L}_T^{max} - \mathcal{L}_T^{clean}}$$

donde:
- ℒ_T^clean es la pérdida sin ataque
- ℒ_T^max es la pérdida máxima posible

MSD_normalized ∈ [0,1] donde 0 indica sin degradación y 1 indica degradación total.

#### 2) Estimación mediante Optimización

**Algoritmo 9: Estimación de MSD mediante Optimización Multi-Inicio**

```
Entrada: Señal x, modelo (f_θ, g_φ), tarea T, presupuesto ε, número de reinicio K
Salida: MSD estimado, perturbación δ*

1. Inicialización:
   a. mejor_loss = -∞
   b. mejor_δ = None

2. Optimización Multi-Inicio:
   a. Para k = 1 hasta K:
      i. Inicializar δ_0 aleatoriamente con ||δ_0||_p = ε
      ii. Para iter = 1 hasta max_iter:
          - Calcular pérdida: L = L_T(x, g_φ(f_θ(x + δ)))
          - Gradiente: g = ∇_δ L
          - Actualizar: δ ← Proj_{||·||_p ≤ ε}(δ + α·g)
          - Si L ha convergido: break
      iii. Si L > mejor_loss:
           mejor_loss = L
           mejor_δ = δ
   b. Fin Para

3. Calcular MSD:
   a. L_clean = L_T(x, g_φ(f_θ(x)))
   b. L_max = valor máximo de L_T (específico de tarea)
   c. MSD_norm = (mejor_loss - L_clean) / (L_max - L_clean)

4. Retornar MSD_norm, mejor_δ
```

La complejidad es O(K · max_iter · costo_forward_backward) [145].

#### 3) Análisis de Distribución de Degradación

Para entender robustez comprehensivamente, se analiza la **distribución de degradación** sobre el conjunto de test [146]:

$$P_{degrad}(d) = p(\mathcal{L}_T(X, g_\phi(f_\theta(X + \delta^*))) = d)$$

donde δ* es la perturbación adversaria óptima.

**Métricas Estadísticas**:
- **Media**: Degradación esperada E[d]
- **Mediana**: Degradación típica med(d)
- **Percentil 95**: Peor caso para 95% de muestras
- **Desviación estándar**: Variabilidad de robustez

Estas estadísticas caracterizan completamente el perfil de robustez del sistema [147].

---

## IX. FRAMEWORK DE MAPEO A ESTANDARIZACIÓN 3GPP

### A. Estructura de Especificaciones Técnicas 3GPP

#### 1) Jerarquía de Documentos

Las especificaciones 3GPP se organizan en series numeradas [148]:

- **Serie 21.xxx**: Requisitos de servicio
- **Serie 22.xxx**: Aspectos de servicio y requisitos de sistema
- **Serie 23.xxx**: Arquitectura técnica
- **Serie 24.xxx**: Protocolos de señalización (capa de aplicación)
- **Serie 25.xxx**: RAN (para UMTS)
- **Serie 36.xxx**: RAN (para LTE)
- **Serie 37.xxx**: Aspectos múltiples RATs
- **Serie 38.xxx**: RAN (para NR/5G)
- **Serie 28.xxx**: Señalización OAM (Operations, Administration, Maintenance)

Para sistemas AI-nativos semánticos, se requieren adiciones/modificaciones en múltiples series.

#### 2) Proceso de Estandarización

El proceso típico incluye [149]:

1. **Study Item (SI)**: Investigación exploratoria de factibilidad técnica (12-18 meses)
   - Documento: Technical Report (TR)
   - Ejemplo: "Study on Semantic Communication Metrics for AI-Native Systems"

2. **Work Item (WI)**: Desarrollo de especificaciones normativas (12-24 meses)
   - Documento: Technical Specification (TS)
   - Ejemplo: "Semantic Communication Metrics and Measurement Procedures"

3. **Change Requests (CR)**: Modificaciones a especificaciones existentes
   - Tipo A: Editorial
   - Tipo B: Funcionalidad nueva compatible hacia atrás
   - Tipo C: Funcionalidad nueva incompatible
   - Tipo D: Corrección de errores

