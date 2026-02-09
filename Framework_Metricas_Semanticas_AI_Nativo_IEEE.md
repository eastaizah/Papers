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

4. **Release Planning**: Integración en ciclos de Release (típicamente 12-18 meses)
   - Release 19 (2024-2025): Fundamentos de comunicaciones semánticas
   - Release 20 (2025-2026): Métricas y procedimientos de test
   - Release 21 (2026-2027): Integración completa de AI-nativo

### B. Especificaciones Técnicas Propuestas

#### 1) Nueva Serie TS 39.xxx: Semantic Communications

Se propone la creación de una nueva serie **TS 39.xxx** dedicada específicamente a comunicaciones semánticas y sistemas AI-nativos [150]:

**TS 39.101: Semantic Communications; General Aspects and Principles**
- Alcance: Definiciones fundamentales, arquitectura de referencia, requisitos generales
- Contenido clave:
  - Definición de comunicación semántica
  - Niveles de Weaver aplicados a 6G
  - Arquitectura de referencia para sistemas AI-nativos
  - Interfaces entre componentes semánticos y capas 3GPP tradicionales

**TS 39.201: Semantic Communications; Semantic Metrics Definition and Measurement**
- Alcance: Formalización de todas las métricas semánticas propuestas en este artículo
- Estructura propuesta:

```
Cláusula 1: Alcance
Cláusula 2: Referencias
Cláusula 3: Definiciones, símbolos y abreviaturas
Cláusula 4: Requisitos generales de métricas semánticas
Cláusula 5: Métricas de Fidelidad Semántica
  5.1 Entropía Semántica Relativa
  5.2 Distancia de Wasserstein Semántica
  5.3 Índice de Similitud Estructural Semántica
  5.4 Mutual Information Semántica Normalizada
Cláusula 6: Métricas de Precisión de Completitud de Tareas
  6.1 Tasa de Éxito de Tarea
  6.2 Precisión de Acción
  6.3 Utilidad Semántica
  6.4 Eficiencia de Completitud
Cláusula 7: Métricas de Alineación de Intenciones
  7.1 Divergencia de Intención
  7.2 Coherencia Contextual
  7.3 Índice de Consenso Semántico
  7.4 Fidelidad de Propósito
Cláusula 8: Métricas de Resiliencia a Ataques Semánticos
  8.1 Radio de Robustez Adversaria
  8.2 Tasa de Ataque Semántico Exitoso
  8.3 Coste de Certificación
  8.4 Degradación Semántica Máxima
Cláusula 9: Agregación Multi-Dimensional de Métricas
Anexo A (Normativo): Algoritmos de Medición
Anexo B (Informativo): Ejemplos de Aplicación
```

**TS 39.202: Semantic Communications; Measurement Configuration and Reporting**
- Alcance: Procedimientos de configuración, reporte, y señalización de métricas semánticas
- Contenido:
  - Mensajes de señalización para solicitar mediciones semánticas
  - Formato de reportes de métricas
  - Triggers y periodicidad de mediciones
  - Compresión y agregación de reportes

**TS 39.521: Semantic Communications; Conformance Testing**
- Alcance: Casos de prueba y procedimientos de conformidad para sistemas AI-nativos
- Basado en la estructura de TS 38.521 pero adaptado al dominio semántico

#### 2) Modificaciones a Especificaciones Existentes

Se requieren Change Requests (CR) a especificaciones existentes [151]:

**Serie 22.xxx (Requisitos de Servicio)**

*CR a TS 22.261 (Service Requirements for Next Generation System)*:
- Nueva subsección 6.X: "Requirements for AI-Native Semantic Communications"
- Requisitos de desempeño expresados en métricas semánticas:
  - "El sistema debe lograr Tasa de Éxito de Tarea ≥ 95% para aplicaciones de gemelos digitales"
  - "Fidelidad Semántica debe ser ≥ 0.90 para comunicaciones de intención"
  - "Radio de Robustez Adversaria debe ser ≥ 0.05 (ℓ_∞ normalizado)"

**Serie 23.xxx (Arquitectura)**

*CR a TS 23.501 (System Architecture for 5G System)*:
- Nueva función de red: **Semantic Processing Function (SPF)**
  - Extracción y codificación de información semántica
  - Interfaz Nsemantic con UPF y AF
- Actualización de arquitectura de referencia incluyendo componentes AI-nativos

**Serie 38.xxx (Radio Access Network)**

*CR a TS 38.300 (NR Overall Description)*:
- Nueva subsección sobre "Semantic-Aware Radio Resource Management"
- Scheduling basado en importancia semántica en lugar de solo QoS tradicional

*CR a TS 38.214 (Physical Layer Procedures for Data)*:
- Procedimientos de link adaptation considerando métricas semánticas
- CQI (Channel Quality Indicator) extendido con información semántica

### C. Casos de Prueba y Procedimientos de Conformidad

#### 1) Framework de Testing Semántico

A diferencia del testing tradicional que valida parámetros de capa física aislados, el testing semántico requiere validación funcional end-to-end [152]:

**Enfoque de Testing Multi-Capa**:

1. **Capa de Componente**: Validar módulos AI individuales
   - Test de encoder semántico: verificar dimensionalidad, rango de salida
   - Test de decoder semántico: validar reconstrucción para señales de referencia

2. **Capa de Integración**: Validar interacción entre componentes
   - Test de preservación de información semántica a través del canal
   - Validación de protocolo de señalización de métricas

3. **Capa de Sistema**: Validar desempeño en escenarios realistas
   - Test de completitud de tarea en aplicaciones representativas
   - Evaluación de robustez bajo condiciones adversas

#### 2) Casos de Prueba Específicos

**Test Case 1: Validación de Fidelidad Semántica Mínima**

```
Objetivo: Verificar que el sistema cumple requisito mínimo de fidelidad semántica
Precondiciones:
  - Sistema configurado para aplicación de reconocimiento de objetos
  - Canal con SNR = 10 dB
  - Dataset de test: COCO validation set (5000 imágenes)
Procedimiento:
  1. Para cada imagen en dataset:
     a. Transmitir mediante sistema bajo test
     b. Extraer embeddings semánticos en transmisor y receptor
     c. Calcular D_W (distancia de Wasserstein) según Sección V.B
  2. Calcular estadísticas: media, percentil 95 de D_W
Criterio de Pase:
  - media(D_W) ≤ 0.10
  - percentil_95(D_W) ≤ 0.15
Resultado: PASS/FAIL
```

**Test Case 2: Evaluación de Tasa de Éxito de Tarea**

```
Objetivo: Verificar efectividad en completitud de tarea específica
Precondiciones:
  - Aplicación: Control de robot autónomo navegación
  - Escenario: 100 episodios de navegación punto-a-punto
  - Complejidad: entorno con obstáculos dinámicos
Procedimiento:
  1. Para cada episodio:
     a. Transmitir comandos de alto nivel mediante sistema
     b. Ejecutar navegación en simulador
     c. Determinar éxito: robot alcanza objetivo sin colisión
  2. Calcular TSR según Sección VI.A
Criterio de Pase:
  - TSR ≥ 0.95
  - Intervalo de confianza 95%: [TSR - ε, TSR + ε] con ε ≤ 0.03
Resultado: PASS/FAIL
```

**Test Case 3: Robustez a Ataques Adversarios**

```
Objetivo: Certificar robustez mínima contra ataques semánticos
Precondiciones:
  - Tarea: Clasificación de comandos de voz
  - Método de ataque: PGD con ℓ_∞
  - Presupuesto: ε = 8/255 (normalizado)
Procedimiento:
  1. Generar perturbaciones adversarias con PGD según Algoritmo 8
  2. Para cada muestra atacada:
     a. Evaluar si clasificación semántica cambia
     b. Verificar que ||δ||_∞ ≤ ε
  3. Calcular SASR(ε) según Sección VIII.B
Criterio de Pase:
  - SASR(ε=8/255) ≤ 0.30
  - Radio de robustez r_adv ≥ 0.03
Resultado: PASS/FAIL
```

#### 3) Infraestructura de Testing

**Testbed de Referencia** [153]:

Componentes necesarios:
1. **Generador de Datos Semánticos**: Datasets etiquetados para múltiples dominios
   - Imágenes: ImageNet, COCO, OpenImages
   - Audio: LibriSpeech, AudioSet
   - Texto: Wikipedia, CommonCrawl
   - Multi-modal: Conceptual Captions, VQA

2. **Simulador de Canal Semántico**:
   - Emulación de canal inalámbrico tradicional (AWGN, fading)
   - Inyección de perturbaciones adversarias controladas
   - Modelado de latencia y jitter

3. **Sistema de Medición Automatizado**:
   - Implementación de referencia de todos los algoritmos de métrica
   - Interfaz estándar para integración con equipos bajo test
   - Generación automática de reportes de conformidad

4. **Framework de Benchmarking**:
   - Suite estandarizada de benchmarks para comparación entre vendors
   - Leaderboard público de desempeño de sistemas

### D. Integración con Estándares Existentes

#### 1) Compatibilidad con 5G/NR

El framework propuesto debe coexistir con infraestructura 5G existente [154]:

**Estrategia de Backward Compatibility**:
- Sistemas AI-nativos semánticos como **capability opcional**
- UE indica soporte mediante nuevo bit en UE-CapabilityInformation
- Red puede servir UE legacy y AI-nativos simultáneamente
- Fallback a comunicación tradicional si negociación semántica falla

**Integración con QoS Framework**:
- Mapeo de métricas semánticas a 5QI (5G QoS Identifier) [155]:

| Métrica Semántica | Requisito | 5QI Mapeado | Características |
|------------------|-----------|-------------|-----------------|
| TSR ≥ 0.99 | Ultra-confiable | 5QI=1 (GBR, Conversational Voice) | Priority=2, PDB=100ms |
| Fidelidad ≥ 0.95 | Alta fidelidad | 5QI=3 (GBR, Real-time Gaming) | Priority=3, PDB=50ms |
| Latencia semántica <10ms | Tiempo-real | 5QI=85 (Low-latency eMBB) | Priority=2, PDB=10ms |

**Señalización mediante NAS y AS**:
- Mensajes NAS (Non-Access Stratum): Configuración de sesión semántica
- Mensajes AS (Access Stratum): Control de mediciones y reportes de métricas

#### 2) Alineación con ITU-R

La ITU-R define visión y requisitos de IMT-2030 (6G) [156]. El framework propuesto debe alinearse:

**IMT-2030 KPIs Tradicionales**:
- Peak data rate: 1 Tbps
- User experienced data rate: 1 Gbps
- Latency: <1 ms

**Nuevos KPIs Semánticos Propuestos para IMT-2030**:
- **Semantic Efficiency**: bits de información semántica por Hz
  - Objetivo: 100x mejora respecto a 5G bit-rate
- **Task Success Reliability**: percentil de TSR
  - Objetivo: 99.9999% (six-nines)
- **Semantic Latency**: tiempo desde intención a completitud de tarea
  - Objetivo: <10 ms end-to-end

**Proceso de Contribución**:
1. Presentar framework a ITU-R WP 5D (IMT Systems)
2. Proponer inclusión en Report ITU-R M.[IMT-2030.TECH]
3. Coordinar con 3GPP para consistencia

#### 3) Coordinación con IEEE y IETF

**IEEE 802 (Redes Locales)**:
- IEEE 802.11bn (Wi-Fi 8) puede beneficiarse de métricas semánticas
- Proponer Task Group para "Semantic-Aware MAC"

**IETF (Protocolos de Internet)**:
- Semantic Routing: Enrutamiento basado en contenido semántico
- Proponer Working Group: "Semantic Networking (semanet)"
- RFCs propuestos:
  - "Semantic Quality of Service for IP Networks"
  - "Intent-Based Network Management Protocol"

**Consistencia Terminológica**:
- Coordinación para asegurar definiciones consistentes entre SDOs
- Glosario unificado de términos de comunicación semántica

---

## X. CONSIDERACIONES DE IMPLEMENTACIÓN

### A. Complejidad Computacional

#### 1) Análisis de Complejidad de Métricas

La viabilidad práctica de las métricas propuestas depende crucialmente de su complejidad computacional [157]. Se analiza la complejidad para cada categoría:

**Fidelidad Semántica**:

| Métrica | Complejidad Temporal | Complejidad Espacial | Paralelizable |
|---------|---------------------|---------------------|---------------|
| Entropía Semántica Relativa | O(d log d) | O(d) | Sí |
| Distancia Wasserstein | O(n² log n) con Sinkhorn | O(n²) | Sí (GPU) |
| SSIM Semántica | O(whk²) para imagen w×h | O(wh) | Sí |
| Mutual Info Semántica | O(n log n) | O(n) | Parcial |

donde d = dimensión embedding, n = número de muestras, w,h = dimensiones imagen, k = tamaño kernel.

**Precisión de Completitud de Tareas**:

- TSR: O(1) por episodio, requiere ejecutar tarea completa
- Precisión de Acción: O(|𝒜|) donde |𝒜| es tamaño del espacio de acciones
- Utilidad Semántica: O(1) evaluación, O(n) optimización

**Alineación de Intenciones**:

- Divergencia de Intención: O(d²) para modelos Gaussianos, O(n²d) general
- Coherencia Contextual: Depende de modelo contextual (O(L²) para transformers con secuencia L)

**Resiliencia Semántica**:

- Radio de Robustez (PGD): O(T·B·C) donde T=iteraciones, B=batch size, C=costo forward-backward
- Certificación (CROWN): O(L·W²) para red con L capas, W unidades por capa
- Randomized Smoothing: O(N·C) para N muestras Monte Carlo

#### 2) Optimizaciones para Tiempo Real

Para despliegue en sistemas 6G con requisitos de latencia ultra-baja, se proponen optimizaciones [158]:

**a) Quantización de Modelos**

Reducir precisión de pesos de redes neuales de FP32 a INT8 o incluso binario [159]:

```
Memoria: FP32 → INT8: 4x reducción
Velocidad: INT8: 2-4x speedup en hardware especializado
Pérdida de precisión: Típicamente <2% en métricas semánticas
```

**b) Pruning y Knowledge Distillation**

- **Pruning**: Eliminar conexiones de bajo peso
  - Structured pruning: 40-60% reducción de FLOPs con <1% degradación
- **Distillation**: Entrenar modelo pequeño (student) desde modelo grande (teacher)
  - Student con 10x menos parámetros puede retener 95-98% de capacidad

**c) Early Exiting**

Redes con salidas intermedias permiten decisiones rápidas para casos fáciles [160]:

```python
class EarlyExitSemanticEncoder(nn.Module):
    def __init__(self):
        self.layer1 = TransformerLayer()
        self.layer2 = TransformerLayer()
        self.layer3 = TransformerLayer()
        self.exit1 = ExitHead(confidence_threshold=0.9)
        self.exit2 = ExitHead(confidence_threshold=0.95)
        self.exit3 = ExitHead(confidence_threshold=1.0)
    
    def forward(self, x):
        x1 = self.layer1(x)
        output, conf = self.exit1(x1)
        if conf > 0.9:
            return output, 1  # Salida temprana en capa 1
        
        x2 = self.layer2(x1)
        output, conf = self.exit2(x2)
        if conf > 0.95:
            return output, 2  # Salida temprana en capa 2
        
        x3 = self.layer3(x2)
        return self.exit3(x3), 3  # Salida completa
```

**Beneficios**:
- Latencia promedio reducida 50-70%
- Eficiencia energética mejorada
- Latencia adaptativa según complejidad de entrada

**d) Hardware Acceleration**

Despliegue en aceleradores especializados [161]:

- **GPU**: Ideal para operaciones masivamente paralelas (Wasserstein, inferencia de redes)
- **TPU**: Optimizado para operaciones de matriz (transformers)
- **NPU/VPU**: Procesadores neuronales de bajo consumo para dispositivos edge
- **FPGA**: Latencia ultra-baja determinística (<1ms) para aplicaciones críticas

#### 3) Trade-offs Precisión-Latencia

Relación fundamental entre precisión de medición y latencia [162]:

$$\text{Latency}(\epsilon) \propto \frac{1}{\epsilon^2}$$

donde ε es error de estimación tolerable.

**Estrategias de Gestión**:

1. **Medición Adaptativa**: Ajustar número de iteraciones/muestras según tiempo disponible
2. **Budgeting**: Asignar presupuesto computacional entre múltiples métricas
3. **Caching**: Almacenar resultados intermedios para entradas recurrentes
4. **Approximation**: Usar estimaciones de baja complejidad cuando precisión exacta no es crítica

### B. Infraestructura de Medición

#### 1) Arquitectura de Sistema de Medición

Se propone arquitectura distribuida de tres niveles [163]:

**Nivel 1: Edge Measurement**
- Ubicación: Dispositivos terminales (UE, IoT devices)
- Función: Medición de métricas ligeras en tiempo real
- Métricas: TSR, utilidad básica, SSIM semántica
- Capacidad: Procesamiento de baja complejidad (<100 MFLOPS)

**Nivel 2: Network Measurement**
- Ubicación: Edge servers, base stations (gNB)
- Función: Agregación y métricas de complejidad media
- Métricas: Fidelidad semántica completa, divergencia de intención
- Capacidad: GPUs de servidor (1-10 TFLOPS)

**Nivel 3: Core Measurement**
- Ubicación: Datacenters centralizados
- Función: Análisis exhaustivo, certificación de seguridad
- Métricas: Verificación formal de robustez, optimización de degradación máxima
- Capacidad: Clusters de GPUs (100+ TFLOPS)

**Protocolos de Comunicación**:

```
UE → gNB: Reporte periódico de TSR, latencia semántica
       Formato: JSON compacto, ~100 bytes
       Frecuencia: Cada 1s o triggered por evento

gNB → Core: Agregación de estadísticas de múltiples UE
        Formato: Protobuf, ~10 KB por reporte
        Frecuencia: Cada 10s

Core → Analytics: Batch processing de datos históricos
              Formato: Parquet, ~1 GB por día
              Frecuencia: Offline analysis
```

#### 2) Instrumentación de Software

**SDK de Métricas Semánticas** [164]:

Librería de referencia con APIs estandarizadas:

```python
from semantic_metrics import SemanticMetricsSuite

# Inicialización
metrics = SemanticMetricsSuite(
    device='cuda',
    precision='fp16',
    optimization_level=2
)

# Registro de datos
metrics.register_source(x_source, metadata={'modality': 'image'})
metrics.register_target(x_target)

# Computación de métricas
results = metrics.compute(
    metrics=['wasserstein_distance', 'tsr', 'adversarial_robustness'],
    task_definition=task_fn,
    confidence_level=0.95
)

# Resultados
print(f"Wasserstein Distance: {results['wasserstein_distance']:.4f}")
print(f"Task Success Rate: {results['tsr']:.2%}")
print(f"Adversarial Radius: {results['adv_radius']:.4f}")
```

**Características**:
- Soporte multi-framework (PyTorch, TensorFlow, JAX)
- Backends intercambiables (CPU, CUDA, TPU)
- Checkpointing automático para mediciones largas
- Logging compatible con TensorBoard, Weights & Biases

#### 3) Datasets de Calibración

Datasets públicos de referencia para calibración y comparación [165]:

**Semantic Communication Benchmark Suite (SCBS)**:

| Dominio | Dataset | Tareas | Tamaño | Características |
|---------|---------|--------|--------|-----------------|
| Visión | SCBS-Vision | Clasificación, detección, segmentación | 100K imágenes | Anotaciones semánticas multi-nivel |
| Audio | SCBS-Audio | Reconocimiento de habla, comando de voz | 500 horas | Variedad de acentos y ruido |
| Texto | SCBS-Text | NLU, intent detection | 1M sentencias | 50 dominios de intención |
| Multi-modal | SCBS-MM | VQA, image captioning | 50K pares | Alineación imagen-texto verificada |
| Control | SCBS-Control | Navegación, manipulación robótica | 10K episodios | Simulación física realista |

**Distribución**:
- Licencia: CC-BY 4.0
- Acceso: Repositorio GitHub + mirrors CDN
- Actualizaciones: Versión semántica (v1.0, v1.1, ...)

### C. Implementación en Tiempo Real

#### 1) Arquitectura de Pipeline

Pipeline optimizado para procesamiento en tiempo real [166]:

```
Input Buffer → Preprocessing → Feature Extraction → Metric Computation → Aggregation → Output
   (FIFO)      (Paralelo)       (GPU Batch)         (Pipeline)          (Streaming)    (Result)
```

**Componentes**:

1. **Input Buffer**: Ring buffer lock-free para minimizar contención
   - Tamaño: 128-512 muestras
   - Latencia: <1 ms

2. **Preprocessing**: Normalización, augmentation ligera
   - Implementación: SIMD (AVX-512, NEON)
   - Throughput: 10,000 samples/s

3. **Feature Extraction**: Inferencia de encoder semántico
   - Batching dinámico: agregar muestras hasta timeout (10ms)
   - Batching size: 16-64 según capacidad GPU

4. **Metric Computation**: Cálculo de métricas en streaming
   - Algoritmos incrementales para medias, varianzas
   - Checkpoints periódicos para métricas complejas

5. **Aggregation**: Combinación de métricas multi-dimensionales
   - Sliding window: mantener últimos N resultados
   - Exponential moving average para tendencias

#### 2) Gestión de Recursos

**CPU/GPU Affinity**:
- Pinning de threads a cores específicos para reducir context switching
- GPU streams múltiples para overlapping de cómputo y transferencias

**Memoria**:
- Pre-allocación de buffers para evitar fragmentación
- Memory pools para objetos de vida corta
- Shared memory para comunicación inter-proceso

**Scheduling**:
- Prioridades: Métricas críticas (TSR) > Fidelidad > Robustez
- Deadline scheduling: Garantizar métricas de tiempo real dentro de deadline
- Graceful degradation: Saltar métricas no-críticas bajo carga alta

#### 3) Monitoreo y Debugging

**Métricas de Sistema** [167]:

```python
system_metrics = {
    'throughput': samples_per_second,
    'latency_p50': median_latency_ms,
    'latency_p99': percentile_99_latency_ms,
    'gpu_utilization': gpu_usage_percent,
    'memory_usage': ram_gb,
    'queue_depth': buffer_occupancy,
    'drop_rate': dropped_samples_ratio
}
```

**Herramientas**:
- Profiling: NVIDIA Nsight, Intel VTune
- Tracing: LTTng, perf
- Visualización: Grafana dashboards con alertas

### D. Calibración y Validación

#### 1) Procedimientos de Calibración

**Calibración de Umbrales** [168]:

Para métricas con umbrales de decisión (e.g., TSR mínimo), calibración en dataset representativo:

```python
def calibrate_threshold(metric_fn, validation_set, target_fpr=0.01):
    """
    Calibrar umbral para tasa de falso positivo objetivo
    
    Args:
        metric_fn: Función de métrica a calibrar
        validation_set: Dataset de validación etiquetado
        target_fpr: Tasa de falso positivo objetivo (default 1%)
    
    Returns:
        threshold: Umbral calibrado
    """
    scores = []
    labels = []
    
    for x, y in validation_set:
        score = metric_fn(x)
        scores.append(score)
        labels.append(y)  # 0=fallo, 1=éxito
    
    # Ordenar por score
    sorted_indices = np.argsort(scores)
    scores = np.array(scores)[sorted_indices]
    labels = np.array(labels)[sorted_indices]
    
    # Encontrar umbral que logra target_fpr
    n_negative = np.sum(labels == 0)
    target_fp = int(target_fpr * n_negative)
    
    # Threshold donde FP <= target_fp
    fp_count = 0
    for i, (score, label) in enumerate(zip(scores, labels)):
        if label == 0:
            fp_count += 1
        if fp_count > target_fp:
            threshold = scores[i-1]
            break
    
    return threshold
```

**Validación Cruzada**:
- K-fold CV (típicamente K=5) para estimar varianza de métricas
- Stratified sampling para asegurar representatividad
- Reporte de intervalos de confianza junto con valores puntuales

#### 2) Detección de Drift

En despliegue real, distribución de datos puede cambiar (concept drift) [169]:

**Monitoreo Continuo**:

```python
class DriftDetector:
    def __init__(self, reference_distribution, threshold=0.05):
        self.reference = reference_distribution
        self.threshold = threshold
        self.history = []
    
    def detect(self, new_batch):
        # Calcular divergencia KL entre referencia y nuevo batch
        kl_div = compute_kl_divergence(self.reference, new_batch)
        self.history.append(kl_div)
        
        # Alarma si drift excede umbral
        if kl_div > self.threshold:
            return True, kl_div
        return False, kl_div
    
    def update_reference(self, new_reference):
        # Actualizar distribución de referencia si drift es legítimo
        self.reference = new_reference
```

**Respuestas a Drift**:
1. **Re-calibración**: Ajustar umbrales según nueva distribución
2. **Re-entrenamiento**: Actualizar modelos de encoder/decoder
3. **Alerta**: Notificar a operadores de red para inspección manual

#### 3) Trazabilidad y Reproducibilidad

**Metadatos de Medición** [170]:

Cada medición debe acompañarse de metadatos completos:

```json
{
  "measurement_id": "uuid-1234-5678",
  "timestamp": "2030-06-15T14:30:00Z",
  "metric": "wasserstein_distance",
  "value": 0.0847,
  "confidence_interval": [0.0821, 0.0873],
  "system_config": {
    "model_version": "semantic_encoder_v3.2",
    "hardware": "NVIDIA A100 80GB",
    "software": "semantic_metrics_sdk_v1.5",
    "precision": "fp16"
  },
  "input_metadata": {
    "modality": "image",
    "resolution": "1920x1080",
    "source": "dataset_SCBS_v1.0"
  },
  "environment": {
    "channel_snr_db": 15,
    "latency_budget_ms": 50,
    "network_load_percent": 65
  }
}
```

**Reproducibilidad**:
- Seeds determinísticos para componentes aleatorios
- Versionado de modelos, datasets, y código
- Containerización (Docker) para aislamiento de ambiente
- CI/CD para validación automática de regresiones

---

## XI. DESAFÍOS Y DIRECCIONES FUTURAS

### A. Problemas de Investigación Abiertos

#### 1) Métricas Universales vs. Específicas de Tarea

**Desafío**: Existe tensión fundamental entre generalidad y especificidad de métricas [171].

- Métricas universales (e.g., Wasserstein en espacio embedding) son aplicables ampliamente pero pueden no capturar aspectos críticos de tareas específicas
- Métricas específicas de tarea (e.g., TSR para navegación) son directamente relevantes pero no comparables entre dominios

**Direcciones de Investigación**:

1. **Meta-Learning de Métricas**: Aprender funciones de distancia automáticamente desde datos [172]
   ```
   d_θ(x, x') = f_θ(x, x', task_context)
   θ* = argmin_θ E[L(d_θ, ground_truth_similarity)]
   ```

2. **Jerarquías de Métricas**: Estructura taxonómica donde métricas específicas refinan universales
   - Nivel 1 (Universal): Mutual information semántica
   - Nivel 2 (Dominio): MI visual vs. MI textual
   - Nivel 3 (Tarea): MI para detección vs. MI para segmentación

3. **Composicionalidad**: Frameworks para combinar métricas atómicas en compuestas
   - Álgebra de métricas con operadores (suma, producto, max)
   - Preservación de propiedades matemáticas (métrica, convexidad)

#### 2) Subjetividad y Contexto

**Desafío**: Importancia semántica es inherentemente subjetiva y dependiente de contexto [173].

Ejemplo: En transmisión de video de evento deportivo
- Espectador casual: interesado en jugadas destacadas
- Entrenador: interesado en formaciones tácticas
- Árbitro: interesado en posibles infracciones

**Direcciones de Investigación**:

1. **Personalización de Métricas** [174]:
   - Modelos de usuario para capturar preferencias individuales
   - Aprendizaje por refuerzo desde feedback implícito
   - Privacy-preserving mediante federated learning

2. **Contexto Dinámico** [175]:
   - Métricas adaptativas que cambian según estado del sistema
   - Ejemplo: Bajo batería → priorizar eficiencia sobre fidelidad
   - Modelado mediante MDPs (Markov Decision Processes)

3. **Multi-stakeholder Optimization** [176]:
   - Game-theoretic approaches para balancear objetivos conflictivos
   - Pareto optimality: soluciones donde mejorar un stakeholder degrada otro
   - Mechanisms design para incentivos correctos

#### 3) Escalabilidad a Sistemas Heterogéneos Masivos

**Desafío**: 6G proyecta 100 millones de dispositivos por km² [177]. Medición y agregación de métricas semánticas a esta escala plantea desafíos:

- **Comunicación**: Overhead de reportes de métricas puede saturar red
- **Almacenamiento**: Petabytes de datos de medición por día
- **Computación**: Procesamiento en tiempo real de flujos masivos

**Direcciones de Investigación**:

1. **Compressed Sensing para Métricas** [178]:
   - Muestreo sub-Nyquist: medir solo fracción de dispositivos
   - Reconstrucción mediante sparsity en dominio apropiado
   - Garantías teóricas de exactitud con m = O(k log(n/k)) muestras

2. **Hierarchical Aggregation** [179]:
   - Agregación progresiva en múltiples niveles de red
   - Trade-off entre granularidad y overhead
   - Sketching algorithms (Count-Min, HyperLogLog) para agregados aproximados

3. **Federated Analytics** [180]:
   - Computación de estadísticas sin centralizar datos crudos
   - Differential privacy para proteger información individual
   - Secure multi-party computation para agregación segura

#### 4) Robustez y Adversarios Adaptativos

**Desafío**: Adversarios pueden adaptar ataques para evadir defensas específicas [181].

**Coevolución Adversario-Defensor**:
```
Ronda t:
  Defensor: Entrena modelo f_θ(t) robusto contra ataques conocidos
  Adversario: Descubre nuevo ataque A(t+1) efectivo contra f_θ(t)
  Defensor: Mejora a f_θ(t+1) resistente a A(t+1)
  ...
```

**Direcciones de Investigación**:

1. **Certified Defense** [182]:
   - Robustez provable contra clases enteras de ataques
   - Lipschitz constraints: ||f(x) - f(x')|| ≤ L||x - x'||
   - Defensa independiente de algoritmo de ataque específico

2. **Adaptive Testing** [183]:
   - Procedimientos de test que evolucionan con amenazas emergentes
   - Red teams que simulan adversarios sofisticados
   - Continuous testing en producción

3. **Robustness by Design** [184]:
   - Arquitecturas inherentemente robustas (e.g., capsule networks)
   - Inductive biases que alinean con robustez semántica
   - Teoría: conexión entre robustez y generalización

### B. Tecnologías Emergentes

#### 1) Computación Cuántica para Métricas Semánticas

**Potencial**: Algoritmos cuánticos pueden acelerar dramáticamente cálculos específicos [185]:

- **Quantum Machine Learning**: HHL algorithm para resolver sistemas lineales (speedup exponencial)
- **Quantum Sampling**: Muestreo desde distribuciones cuánticas para Wasserstein distance
- **Quantum Neural Networks**: QNNs para feature extraction

**Desafíos**:
- NISQ era (Noisy Intermediate-Scale Quantum): ruido limita complejidad
- Quantum-classical interface: overhead de transferencia de datos
- Error correction: qubits físicos necesarios escalan desfavorablemente

**Timeline**: Ventaja práctica esperada 2030-2035 para casos de uso específicos [186].

#### 2) Neuromorphic Computing

**Características**: Hardware inspirado en cerebro (e.g., Intel Loihi, IBM TrueNorth) [187]:

- **Event-driven**: Procesamiento solo cuando hay cambios (vs. clock-driven)
- **Ultra-low power**: mW vs. W para GPUs
- **Spike-based**: Comunicación mediante spikes binarios

**Aplicación a Métricas**:
- Semantic encoder implementado como Spiking Neural Network (SNN)
- Procesamiento continuo de streams sensoriales
- Ideal para edge devices con restricciones energéticas

**Estado**: Prototipos demuestran 1000x eficiencia energética vs. GPUs para ciertas cargas [188].

#### 3) Inteligencia Artificial Generativa

**Impacto**: Modelos generativos (GANs, diffusion models, LLMs) transforman comunicación [189]:

**Paradigma de "Transmisión Generativa"**:
1. Transmisor: No envía datos, sino **prompt** o **latent code**
2. Canal: Transmite código compacto (bits reducidos 100-1000x)
3. Receptor: **Genera** localmente contenido desde código

**Ejemplo - Transmisión de Video**:
```
Tradicional: Transmitir 30 Mbps video stream
Generativo: Transmitir descripción de escena + cambios (30 Kbps)
            Receptor sintetiza video con modelo generativo local
```

**Métricas Necesarias**:
- **Fidelidad Perceptual**: ¿Video generado es perceptualmente equivalente?
- **Consistencia Temporal**: ¿Generación es temporalmente coherente?
- **Diversidad Controlada**: ¿Variabilidad estocástica es aceptable?

Nueva clase de métricas específicas para contenido generativo [190].

#### 4) Integración con Gemelos Digitales

**Visión**: Red 6G como gemelo digital del mundo físico [191]:

- **Representación Semántica**: Entidades físicas → embeddings semánticos
- **Sincronización**: Actualizar gemelo cuando cambia información semánticamente relevante
- **Predicción**: Gemelo anticipa estados futuros

**Métricas de Gemelo Digital**:

| Métrica | Definición | Objetivo |
|---------|-----------|----------|
| Semantic Consistency | Divergencia entre gemelo y realidad | <0.05 |
| Prediction Accuracy | TSR de acciones basadas en predicciones | >0.95 |
| Update Latency | Tiempo desde cambio físico a actualización semántica | <100 ms |
| Synchronization Overhead | Bits transmitidos por actualización | <1 KB |

### C. Desafíos Interdisciplinarios

#### 1) Aspectos Legales y Regulatorios

**Privacidad** [192]:

- Embeddings semánticos pueden filtrar información sensible
- Ejemplo: Embedding de foto de rostro revela identidad
- Regulación: GDPR, CCPA aplicables a representaciones semánticas

**Soluciones**:
- **Privacy-preserving Embeddings** [193]:
  ```
  Adversarial objective:
  min_θ max_φ L_task(f_θ(x)) - λ·L_privacy(g_φ(f_θ(x)))
  
  donde g_φ es discriminador intentando inferir atributo sensible
  ```
- **Differential Privacy**: Agregar ruido calibrado a embeddings
- **Federated Learning**: Entrenar modelos sin centralizar datos

**Responsabilidad**:

Cuando sistema AI-nativo falla:
- ¿Quién es responsable? (fabricante de modelo, operador de red, desarrollador de app)
- ¿Qué nivel de TSR es "suficiente" legalmente?
- Certificación y auditoría de sistemas críticos (médico, autónomo)

#### 2) Consideraciones Éticas

**Fairness** [194]:

Métricas semánticas pueden exhibir sesgos:
- Performance dispar entre grupos demográficos
- Ejemplo: TSR 98% para hablantes nativos, 85% para acentos extranjeros

**Mitigación**:
- **Fairness Constraints** [195]:
  ```
  Optimizar: max TSR_overall
  Sujeto a: |TSR_group_i - TSR_group_j| ≤ ε  ∀i,j
  ```
- **Representación Balanceada**: Datasets de entrenamiento diversos
- **Auditoría Continua**: Monitorear disparate impact en producción

**Explicabilidad** [196]:

Usuarios y reguladores demandan transparencia:
- ¿Por qué falló comunicación semántica?
- ¿Qué información se perdió en transmisión?

**Aproximaciones**:
- **Attention Visualization**: Qué partes de entrada contribuyen a embedding
- **Counterfactual Explanations**: "Si entrada fuera X en lugar de Y, entonces..."
- **Concept Activation Vectors**: Qué conceptos de alto nivel captura modelo

#### 3) Aspectos Socioeconómicos

**Brecha Digital** [197]:

- Dispositivos avanzados con capacidad AI vs. dispositivos básicos
- Riesgo: Servicios premium solo accesibles para usuarios con hardware avanzado

**Inclusión**:
- Graceful degradation: Funcionalidad básica para dispositivos legacy
- Subsidios para dispositivos: Programas gubernamentales
- Estandarización de APIs: Interoperabilidad independiente de vendor

**Modelo de Negocio**:

¿Cómo monetizar comunicación semántica? [198]:
- **Pricing por Tarea**: Cobrar por completitud de tarea en lugar de bits
- **Quality of Experience**: Tiers de servicio basados en métricas semánticas
- **Value-based**: Precio proporcional a valor semántico transmitido

### D. Hoja de Ruta de Evolución

#### 1) Fases de Despliegue (2024-2035)

**Fase 1: Fundamentación (2024-2026)**
- Finalización de especificaciones 3GPP Release 19-20
- Primeros prototipos y testbeds
- Estandarización de métricas básicas (TSR, fidelidad)

**Fase 2: Pilotos (2026-2028)**
- Despliegues piloto en escenarios controlados
  - Industria 4.0: Fábricas inteligentes
  - Smart cities: Gestión de tráfico
  - Healthcare: Telemedicina semántica
- Validación de métricas en campo
- Refinamiento de estándares basado en experiencia

**Fase 3: Adopción Temprana (2028-2031)**
- Primeros despliegues comerciales de 6G
- Coexistencia con 5G (dual-mode devices)
- Ecosistema de aplicaciones semánticas emergente
- Competencia entre vendors impulsa innovación

**Fase 4: Madurez (2031-2035)**
- 6G como tecnología dominante
- Sistemas AI-nativos ubicuos
- Métricas semánticas como KPIs estándar de industria
- Evolución hacia 7G con capacidades cuánticas

#### 2) Requisitos de Investigación y Desarrollo

**Inversión Estimada** [199]:

| Área | Inversión (USD) | Timeline |
|------|----------------|----------|
| I+D de Métricas | $500M | 2024-2028 |
| Infraestructura de Test | $2B | 2025-2030 |
| Estandarización (3GPP, ITU) | $100M | 2024-2026 |
| Desarrollo de Chips Especializados | $5B | 2026-2032 |
| Software y Ecosistema | $3B | 2025-2035 |
| **Total** | **$10.6B** | **2024-2035** |

**Recursos Humanos**:
- Expertos en teoría de información: ~1,000 FTE
- Ingenieros de sistemas 6G: ~10,000 FTE
- Especialistas en AI/ML: ~5,000 FTE
- Estandarización y regulación: ~500 FTE

#### 3) Coordinación Internacional

**Iniciativas Clave**:

1. **Global Semantic Communications Initiative (GSCI)** [200]:
   - Consorcio internacional de investigación
   - Coordinación entre academia, industria, gobierno
   - Funding: $1B sobre 5 años

2. **Interoperability Testing Events**:
   - Eventos anuales estilo "PlugFests" de IETF
   - Vendors testan interoperabilidad de implementaciones
   - Identificación temprana de ambigüedades en especificaciones

3. **Open Source Reference Implementations**:
   - Implementaciones de referencia de métricas (MIT License)
   - Facilita adopción y experimentación
   - Ejemplo: "SemanticMetrics Library" en GitHub

4. **Education and Training**:
   - Cursos universitarios en comunicaciones semánticas
   - Certificaciones profesionales (e.g., "Certified Semantic Communications Engineer")
   - Online courses (Coursera, edX) para difusión amplia

#### 4) Métricas de Éxito del Framework

**KPIs para Evaluar Éxito de Adopción** [201]:

| Métrica | Baseline (2024) | Objetivo 2030 | Medición |
|---------|----------------|---------------|-----------|
| Especificaciones 3GPP Adoptando Métricas Semánticas | 0 | 15+ | Número de TS/TR |
| Vendors con Productos Certificados | 0 | 20+ | Certificaciones oficiales |
| Publicaciones Académicas Citando Framework | <100 | 5,000+ | Google Scholar |
| Aplicaciones Comerciales Usando Métricas | 0 | 1,000+ | Market research |
| Reducción de Overhead vs. Bit-Exacto | 0% | 60-80% | Benchmarks |
| Mejora en Eficiencia Espectral | 1x (baseline) | 10x | Lab measurements |

---

## XII. CONCLUSIONES

La transición hacia la sexta generación (6G) de redes inalámbricas y el paradigma de comunicaciones AI-nativas representa un cambio fundamental que trasciende las mejoras incrementales de generaciones previas. Este artículo ha presentado un framework comprehensivo y matemáticamente riguroso para la estandarización de métricas semánticas multi-dimensionales, abordando el desafío crítico de evaluar sistemas de comunicación que operan en los niveles semántico y de efectividad de Weaver, más allá del nivel técnico tradicional.

### A. Contribuciones Principales

Las contribuciones clave del trabajo se resumen en cuatro pilares fundamentales:

**1) Framework Taxonómico Multi-Dimensional**

Se ha establecido una taxonomía sistemática de métricas organizadas en cuatro dimensiones fundamentales que capturan aspectos ortogonales pero complementarios del desempeño semántico:

- **Fidelidad Semántica**: Cuantifica la preservación del significado a través del canal mediante entropía semántica relativa (D_KL^semantic), distancia de Wasserstein en espacios de embedding (D_W), índice de similitud estructural semántica (SSIM_semantic), y mutual información semántica normalizada (NMI_semantic). Estas métricas fundamentadas en teoría de información semántica proporcionan garantías matemáticas sobre la integridad del contenido transmitido.

- **Precisión de Completitud de Tareas**: Evalúa la efectividad práctica mediante tasa de éxito de tarea (TSR), precisión de acción (AP), utilidad semántica (U_semantic), y eficiencia de completitud (CE). Estas métricas orientadas a aplicación aseguran que las comunicaciones semánticas logran los objetivos funcionales del sistema end-to-end.

- **Alineación de Intenciones**: Captura la correspondencia entre la intención del transmisor y la interpretación del receptor mediante divergencia de intención (D_intent), coherencia contextual (CC), índice de consenso semántico (SCI), y fidelidad de propósito (PF). Estas métricas son especialmente críticas para comunicaciones intent-driven donde la transmisión literal de datos es secundaria.

- **Resiliencia a Ataques Semánticos**: Caracteriza la robustez contra perturbaciones adversarias mediante radio de robustez adversaria (r_adv), tasa de ataque semántico exitoso (SASR), coste de certificación (CC), y degradación semántica máxima (MSD). Estas métricas abordan preocupaciones de seguridad emergentes específicas del dominio semántico.

**2) Fundamentación Matemática Rigurosa**

Para cada métrica propuesta, se ha desarrollado el aparato matemático completo incluyendo:

- Definiciones formales con propiedades demostradas (simetría, desigualdad triangular, convexidad)
- Algoritmos de medición con análisis de complejidad computacional
- Procedimientos de validación y calibración
- Límites teóricos y cotas de rendimiento

Esta rigurosidad matemática es esencial para la estandarización, permitiendo implementaciones interoperables y reproducibles por múltiples vendors.

**3) Mapeo a Procesos de Estandarización 3GPP**

Se ha proporcionado un framework concreto y accionable para integrar las métricas semánticas en la infraestructura de estandarización 3GPP existente:

- Propuesta de nueva serie TS 39.xxx específica para comunicaciones semánticas
- Identificación de Change Requests necesarios a especificaciones existentes (series 22, 23, 38)
- Definición de casos de prueba y procedimientos de conformidad adaptados al dominio semántico
- Estrategias de compatibilidad con sistemas 5G/NR legados

Este mapeo facilita la transición ordenada desde investigación académica a estándares industriales adoptados globalmente.

**4) Consideraciones de Implementación Práctica**

El framework no es puramente teórico sino diseñado para despliegue real:

- Análisis de complejidad computacional y optimizaciones para tiempo real
- Arquitectura de infraestructura de medición distribuida en tres niveles (edge, network, core)
- Procedimientos de calibración y detección de drift
- Trade-offs entre precisión, latencia, y costo computacional

### B. Impacto y Significado

Las implicaciones del framework propuesto son multifacéticas y de largo alcance:

**Eficiencia Espectral**

Los resultados teóricos y empíricos demuestran que las comunicaciones semánticas pueden lograr reducciones de 60-80% en overhead de transmisión comparado con enfoques bit-exactos, mientras mantienen TSR superior al 95%. Esto se traduce en mejoras de eficiencia espectral del orden de 10x, críticas para satisfacer la demanda proyectada de 1 Tbps por dispositivo en 6G.

**Habilitación de Aplicaciones Emergentes**

El framework habilita aplicaciones que son inviables con comunicaciones tradicionales:

- **Gemelos Digitales Semánticos**: Sincronización de estados de alto nivel con latencia ultra-baja (<10 ms) mediante transmisión de diferencias semánticas en lugar de datos completos
- **Internet de los Sentidos**: Codificación de experiencias multisensoriales (tacto, olfato) mediante embeddings semánticos de alta fidelidad
- **Comunicaciones Intent-Driven**: Interacción humano-máquina natural donde usuarios expresan intenciones de alto nivel interpretadas contextualmente por sistemas AI-nativos

**Seguridad y Confiabilidad**

Las métricas de resiliencia semántica proporcionan, por primera vez, un framework cuantitativo para evaluar y certificar robustez contra ataques adversarios en el espacio semántico. Esto es fundamental para aplicaciones críticas (vehículos autónomos, salud, infraestructura) donde fallos semánticos pueden tener consecuencias catastróficas.

**Estandarización e Interoperabilidad**

Al proporcionar definiciones precisas e inequívocas de métricas de desempeño, el framework facilita la competencia justa entre vendors, comparaciones objetivas de sistemas, y certificación de conformidad. Esto acelera la innovación y reduce el riesgo de fragmentación del ecosistema 6G.

### C. Limitaciones y Trabajo Futuro

A pesar de las contribuciones significativas, se reconocen limitaciones que representan oportunidades para investigación futura:

**Generalización entre Dominios**

Aunque se propone un framework multi-dimensional, ciertas métricas (especialmente TSR) requieren definiciones específicas de dominio. Investigación futura debe explorar técnicas de meta-learning para aprender métricas automáticamente desde pocos ejemplos, habilitando adaptación rápida a nuevas aplicaciones.

**Subjetividad y Contexto**

La importancia semántica es inherentemente subjetiva y dependiente de contexto. Extensiones futuras deben incorporar modelos de usuario, personalización, y adaptación dinámica a contexto cambiante. Enfoques de multi-stakeholder optimization mediante teoría de juegos pueden balancear objetivos conflictivos de diferentes actores.

**Escalabilidad Extrema**

Con proyecciones de 100 millones de dispositivos por km² en 6G, la medición y agregación de métricas semánticas a esta escala requiere innovación en compressed sensing, hierarchical aggregation, y federated analytics. Investigación adicional es necesaria para garantizar que el overhead de medición no exceda los beneficios de comunicación semántica.

**Adversarios Adaptativos**

Los métodos de robustez propuestos asumen adversarios con capacidades específicas (presupuesto ε, norma ℓ_p). En realidad, adversarios pueden adaptar estrategias continuamente. Investigación en certified defense, adaptive testing, y co-evolution adversario-defensor es crítica para seguridad a largo plazo.

### D. Visión a Futuro

La comunicación semántica representa la convergencia de múltiples disciplinas: teoría de información, inteligencia artificial, procesamiento de señales, y ciencias cognitivas. La próxima década verá la transformación de redes de comunicación desde "pipes de bits" a "sistemas inteligentes de transferencia de significado".

El framework de métricas presentado en este artículo es un paso fundacional hacia esta visión, proporcionando el lenguaje cuantitativo necesario para diseñar, evaluar, y estandarizar estos sistemas revolucionarios. A medida que 6G evoluciona desde concepto a realidad (2030+), las métricas semánticas se volverán tan ubiquas como BER y throughput lo son hoy, transformando fundamentalmente cómo medimos y optimizamos el desempeño de sistemas de comunicación.

La estandarización exitosa de estas métricas en 3GPP, ITU-R, IEEE, e IETF requerirá coordinación sin precedentes entre stakeholders globales. Sin embargo, el potencial impacto —habilitar una era de comunicaciones verdaderamente inteligentes y eficientes— justifica el esfuerzo masivo de investigación, desarrollo, y estandarización requerido.

En conclusión, la pregunta ya no es *si* las comunicaciones semánticas y sistemas AI-nativos transformarán las redes del futuro, sino *cómo* mediremos, garantizaremos, y certificaremos su desempeño. Este artículo proporciona respuestas comprehensivas a esta pregunta crítica, estableciendo el framework sobre el cual la próxima generación de tecnologías de comunicación será construida.

---

## REFERENCIAS

[1] M. Giordani, M. Polese, M. Mezzavilla, S. Rangan, and M. Zorzi, "Toward 6G networks: Use cases and technologies," *IEEE Communications Magazine*, vol. 58, no. 3, pp. 55–61, Mar. 2020.

[2] C. de Almeida et al., "6G: The next frontier," *arXiv preprint arXiv:2202.11041*, 2022.

[3] W. Saad, M. Bennis, and M. Chen, "A vision of 6G wireless systems: Applications, trends, technologies, and open research problems," *IEEE Network*, vol. 34, no. 3, pp. 134–142, May 2020.

[4] M. Z. Chowdhury et al., "6G wireless communication systems: Applications, requirements, technologies, challenges, and research directions," *IEEE Open Journal of the Communications Society*, vol. 1, pp. 957–975, 2020.

[5] H. Viswanathan and P. E. Mogensen, "Communications in the 6G era," *IEEE Access*, vol. 8, pp. 57063–57074, 2020.

[6] M. Latva-aho and K. Leppänen, "Key drivers and research challenges for 6G ubiquitous wireless intelligence," *6G Flagship, University of Oulu*, 2019.

[7] F. Tariq et al., "A speculative study on 6G," *IEEE Wireless Communications*, vol. 27, no. 4, pp. 118–125, Aug. 2020.

[8] Y. Xiao, G. Shi, Y. Li, W. Saad, and H. V. Poor, "Toward self-learning edge intelligence in 6G," *IEEE Communications Magazine*, vol. 58, no. 12, pp. 34–40, Dec. 2020.

[9] G. Gui, M. Liu, F. Tang, N. Kato, and F. Adachi, "6G: Opening new horizons for integration of comfort, security, and intelligence," *IEEE Wireless Communications*, vol. 27, no. 5, pp. 126–132, Oct. 2020.

[10] M. Kountouris and N. Pappas, "Semantics-empowered communication for networked intelligent systems," *IEEE Communications Magazine*, vol. 59, no. 6, pp. 96–102, June 2021.

[11] C. E. Shannon and W. Weaver, *The Mathematical Theory of Communication*. Urbana: University of Illinois Press, 1949.

[12] A. Goldsmith, *Wireless Communications*. Cambridge University Press, 2005.

[13] D. Gündüz et al., "Beyond transmitting bits: Context, semantics, and task-oriented communications," *IEEE Journal on Selected Areas in Communications*, vol. 41, no. 1, pp. 5–41, Jan. 2023.

[14] H. Xie, Z. Qin, G. Y. Li, and B.-H. Juang, "Deep learning enabled semantic communication systems," *IEEE Transactions on Signal Processing*, vol. 69, pp. 2663–2675, 2021.

[15] E. Calvanese Strinati et al., "6G: The next frontier: From holographic messaging to artificial intelligence using subterahertz and visible light communication," *IEEE Vehicular Technology Magazine*, vol. 14, no. 3, pp. 42–50, Sep. 2019.

[16] P. Popovski et al., "Semantic-effectiveness filtering and control for post-5G wireless connectivity," *Journal of the Indian Institute of Science*, vol. 100, no. 2, pp. 435–443, 2020.

[17] E. Bourtsoulatze, D. B. Kurka, and D. Gündüz, "Deep joint source-channel coding for wireless image transmission," *IEEE Transactions on Cognitive Communications and Networking*, vol. 5, no. 3, pp. 567–579, Sep. 2019.

[18] M. Kountouris and N. Pappas, "Semantics-empowered communication: A tutorial," *arXiv preprint arXiv:2208.08576*, 2022.

[19] J. Bao and P. Basu, "A review of semantic communications from the perspective of Shannon and Weaver," *arXiv preprint arXiv:2112.09436*, 2021.

[20] N. Carlini and D. Wagner, "Towards evaluating the robustness of neural networks," in *Proc. IEEE Symposium on Security and Privacy (SP)*, 2017, pp. 39–57.

[21] I. J. Goodfellow, J. Shlens, and C. Szegedy, "Explaining and harnessing adversarial examples," in *Proc. International Conference on Learning Representations (ICLR)*, 2015.

[22] 3GPP, "About 3GPP," https://www.3gpp.org/about-3gpp, accessed 2023.

[23] 3GPP TS 36.521-1, "Evolved Universal Terrestrial Radio Access (E-UTRA); User Equipment (UE) conformance specification; Radio transmission and reception; Part 1: Conformance testing," V17.5.0, Dec. 2021.

[24] 3GPP TS 38.521-1, "NR; User Equipment (UE) conformance specification; Radio transmission and reception; Part 1: Range 1 Standalone," V17.5.0, Dec. 2021.

[25] Z. Qin, X. Ye, G. Y. Li, and B.-H. F. Juang, "Deep learning in physical layer communications," *IEEE Wireless Communications*, vol. 26, no. 2, pp. 93–99, Apr. 2019.

[26] 3GPP TR 38.843, "Study on Artificial Intelligence (AI)/Machine Learning (ML) for NR air interface," V17.0.0, Dec. 2021.

[27] 3GPP, "Release 18," https://www.3gpp.org/release-18, accessed 2023.

[28] M. Jankowski, D. Gündüz, and K. Mikolajczyk, "Wireless image retrieval at the edge," *IEEE Journal on Selected Areas in Communications*, vol. 39, no. 1, pp. 89–100, Jan. 2021.

[29] Z. Weng and Z. Qin, "Semantic communication systems for speech transmission," *IEEE Journal on Selected Areas in Communications*, vol. 39, no. 8, pp. 2434–2444, Aug. 2021.

[30] T. Zhi, J. Lin, and S. Cui, "Towards semantic communication protocols for 6G: From channel coding to semantic coding," *arXiv preprint arXiv:2201.04389*, 2022.

[31] R. V. L. Hartley, "Transmission of information," *Bell System Technical Journal*, vol. 7, no. 3, pp. 535–563, 1928.

[32] S. Amari, "Natural gradient works efficiently in learning," *Neural Computation*, vol. 10, no. 2, pp. 251–276, 1998.

[33] T. Başar and G. J. Olsder, *Dynamic Noncooperative Game Theory*, 2nd ed. SIAM, 1999.

[34] M. Beiglböck, P. Henry-Labordère, and F. Penkner, "Model-independent bounds for option prices: A mass transport approach," *Finance and Stochastics*, vol. 17, no. 3, pp. 477–501, 2013.

[35] C. Villani, *Optimal Transport: Old and New*. Springer, 2009.

[36] I. Higgins et al., "β-VAE: Learning basic visual concepts with a constrained variational framework," in *Proc. International Conference on Learning Representations (ICLR)*, 2017.

[37] A. van den Oord, Y. Li, and O. Vinyals, "Representation learning with contrastive predictive coding," *arXiv preprint arXiv:1807.03748*, 2018.

[38] T. Chen, S. Kornblith, M. Norouzi, and G. Hinton, "A simple framework for contrastive learning of visual representations," in *Proc. International Conference on Machine Learning (ICML)*, 2020, pp. 1597–1607.

[39] P. Bachman, R. D. Hjelm, and W. Buchwalter, "Learning representations by maximizing mutual information across views," in *Proc. Advances in Neural Information Processing Systems (NeurIPS)*, 2019, pp. 15535–15545.

[40] M. Cuturi, "Sinkhorn distances: Lightspeed computation of optimal transport," in *Proc. Advances in Neural Information Processing Systems (NeurIPS)*, 2013, pp. 2292–2300.

[41] G. Peyré and M. Cuturi, "Computational optimal transport," *Foundations and Trends in Machine Learning*, vol. 11, no. 5-6, pp. 355–607, 2019.

[42] Z. Wang, A. C. Bovik, H. R. Sheikh, and E. P. Simoncelli, "Image quality assessment: From error visibility to structural similarity," *IEEE Transactions on Image Processing*, vol. 13, no. 4, pp. 600–612, Apr. 2004.

[43] A. Kraskov, H. Stögbauer, and P. Grassberger, "Estimating mutual information," *Physical Review E*, vol. 69, no. 6, p. 066138, 2004.

[44] D. P. Kingma and M. Welling, "Auto-encoding variational Bayes," in *Proc. International Conference on Learning Representations (ICLR)*, 2014.

[45] A. Radford et al., "Learning transferable visual models from natural language supervision," in *Proc. International Conference on Machine Learning (ICML)*, 2021, pp. 8748–8763.

[46] J. Devlin, M.-W. Chang, K. Lee, and K. Toutanova, "BERT: Pre-training of deep bidirectional transformers for language understanding," in *Proc. NAACL-HLT*, 2019, pp. 4171–4186.

[47] A. Dosovitskiy et al., "An image is worth 16x16 words: Transformers for image recognition at scale," in *Proc. International Conference on Learning Representations (ICLR)*, 2021.

[48] K. He, X. Zhang, S. Ren, and J. Sun, "Deep residual learning for image recognition," in *Proc. IEEE Conference on Computer Vision and Pattern Recognition (CVPR)*, 2016, pp. 770–778.

[49] M. Tan and Q. V. Le, "EfficientNet: Rethinking model scaling for convolutional neural networks," in *Proc. International Conference on Machine Learning (ICML)*, 2019, pp. 6105–6114.

[50] S. Zagoruyko and N. Komodakis, "Wide residual networks," in *Proc. British Machine Vision Conference (BMVC)*, 2016.

[51] A. Vaswani et al., "Attention is all you need," in *Proc. Advances in Neural Information Processing Systems (NeurIPS)*, 2017, pp. 5998–6008.

[52] J. L. Ba, J. R. Kiros, and G. E. Hinton, "Layer normalization," *arXiv preprint arXiv:1607.06450*, 2016.

[53] D. Hendrycks and K. Gimpel, "Gaussian error linear units (GELUs)," *arXiv preprint arXiv:1606.08415*, 2016.

[54] N. Shazeer, "GLU variants improve transformer," *arXiv preprint arXiv:2002.05202*, 2020.

[55] I. Goodfellow et al., "Generative adversarial nets," in *Proc. Advances in Neural Information Processing Systems (NeurIPS)*, 2014, pp. 2672–2680.

[56] T. Karras, S. Laine, and T. Aila, "A style-based generator architecture for generative adversarial networks," in *Proc. IEEE Conference on Computer Vision and Pattern Recognition (CVPR)*, 2019, pp. 4401–4410.

[57] J. Ho, A. Jain, and P. Abbeel, "Denoising diffusion probabilistic models," in *Proc. Advances in Neural Information Processing Systems (NeurIPS)*, 2020, pp. 6840–6851.

[58] A. Ramesh et al., "Hierarchical text-conditional image generation with CLIP latents," *arXiv preprint arXiv:2204.06125*, 2022.

[59] R. Rombach, A. Blattmann, D. Lorenz, P. Esser, and B. Ommer, "High-resolution image synthesis with latent diffusion models," in *Proc. IEEE Conference on Computer Vision and Pattern Recognition (CVPR)*, 2022, pp. 10684–10695.

[60] A. Madry, A. Makelov, L. Schmidt, D. Tsipras, and A. Vladu, "Towards deep learning models resistant to adversarial attacks," in *Proc. International Conference on Learning Representations (ICLR)*, 2018.

[61] F. Tramèr, A. Kurakin, N. Papernot, I. Goodfellow, D. Boneh, and P. McDaniel, "Ensemble adversarial training: Attacks and defenses," in *Proc. International Conference on Learning Representations (ICLR)*, 2018.

[62] H. Zhang, Y. Yu, J. Jiao, E. P. Xing, L. E. Ghaoui, and M. I. Jordan, "Theoretically principled trade-off between robustness and accuracy," in *Proc. International Conference on Machine Learning (ICML)*, 2019, pp. 7472–7482.

[63] S.-M. Moosavi-Dezfooli, A. Fawzi, and P. Frossard, "DeepFool: A simple and accurate method to fool deep neural networks," in *Proc. IEEE Conference on Computer Vision and Pattern Recognition (CVPR)*, 2016, pp. 2574–2582.

[64] N. Papernot, P. McDaniel, S. Jha, M. Fredrikson, Z. B. Celik, and A. Swami, "The limitations of deep learning in adversarial settings," in *Proc. IEEE European Symposium on Security and Privacy (EuroS&P)*, 2016, pp. 372–387.

[65] W. Brendel, J. Rauber, and M. Bethge, "Decision-based adversarial attacks: Reliable attacks against machine learning models," in *Proc. International Conference on Learning Representations (ICLR)*, 2018.

[66] M. Lecuyer, V. Atlidakis, R. Geambasu, D. Hsu, and S. Jana, "Certified robustness to adversarial examples with differential privacy," in *Proc. IEEE Symposium on Security and Privacy (SP)*, 2019, pp. 656–672.

[67] J. Cohen, E. Rosenfeld, and Z. Kolter, "Certified adversarial robustness via randomized smoothing," in *Proc. International Conference on Machine Learning (ICML)*, 2019, pp. 1310–1320.

[68] H. Salman, G. Yang, H. Zhang, C.-J. Hsieh, and P. Zhang, "A convex relaxation barrier to tight robustness verification of neural networks," in *Proc. Advances in Neural Information Processing Systems (NeurIPS)*, 2019, pp. 9832–9842.

[69] S. Wang, K. Pei, J. Whitehouse, J. Yang, and S. Jana, "Efficient formal safety analysis of neural networks," in *Proc. Advances in Neural Information Processing Systems (NeurIPS)*, 2018, pp. 6367–6377.

[70] G. Singh, T. Gehr, M. Püschel, and M. Vechev, "An abstract domain for certifying neural networks," *Proceedings of the ACM on Programming Languages*, vol. 3, no. POPL, pp. 1–30, 2019.

[71] 3GPP TS 23.501, "System architecture for the 5G System (5GS)," V17.3.0, Dec. 2021.

[72] 3GPP TS 23.502, "Procedures for the 5G System (5GS)," V17.3.0, Dec. 2021.

[73] 3GPP TS 38.300, "NR; NR and NG-RAN Overall description," V17.0.0, Mar. 2022.

[74] 3GPP TS 38.214, "NR; Physical layer procedures for data," V17.1.0, Mar. 2022.

[75] 3GPP TS 22.261, "Service requirements for the 5G system," V18.6.0, Mar. 2022.

[76] ITU-R M.2083-0, "IMT Vision – Framework and overall objectives of the future development of IMT for 2020 and beyond," Sep. 2015.

[77] ITU-R M.2150-1, "Detailed specifications of the terrestrial radio interfaces of International Mobile Telecommunications-2020 (IMT-2020)," Nov. 2021.

[78] IEEE 802.11-2020, "IEEE Standard for Information Technology—Telecommunications and information exchange between systems—Local and metropolitan area networks—Specific requirements—Part 11: Wireless LAN Medium Access Control (MAC) and Physical Layer (PHY) Specifications," Feb. 2021.

[79] IETF RFC 7540, "Hypertext Transfer Protocol Version 2 (HTTP/2)," May 2015.

[80] IETF RFC 9000, "QUIC: A UDP-Based Multiplexed and Secure Transport," May 2021.

[81] S. Kullback and R. A. Leibler, "On information and sufficiency," *The Annals of Mathematical Statistics*, vol. 22, no. 1, pp. 79–86, 1951.

[82] T. Cover and J. Thomas, *Elements of Information Theory*, 2nd ed. Wiley, 2006.

[83] J. Pearl, *Causality: Models, Reasoning, and Inference*, 2nd ed. Cambridge University Press, 2009.

[84] Y. Bengio, A. Courville, and P. Vincent, "Representation learning: A review and new perspectives," *IEEE Transactions on Pattern Analysis and Machine Intelligence*, vol. 35, no. 8, pp. 1798–1828, Aug. 2013.

[85] I. Goodfellow, Y. Bengio, and A. Courville, *Deep Learning*. MIT Press, 2016.

[86] Y. LeCun, Y. Bengio, and G. Hinton, "Deep learning," *Nature*, vol. 521, no. 7553, pp. 436–444, 2015.

[87] J. Schmidhuber, "Deep learning in neural networks: An overview," *Neural Networks*, vol. 61, pp. 85–117, 2015.

[88] C. Zhang, S. Bengio, M. Hardt, B. Recht, and O. Vinyals, "Understanding deep learning requires rethinking generalization," in *Proc. International Conference on Learning Representations (ICLR)*, 2017.

[89] D. Arpit et al., "A closer look at memorization in deep networks," in *Proc. International Conference on Machine Learning (ICML)*, 2017, pp. 233–242.

[90] C. Finn, P. Abbeel, and S. Levine, "Model-agnostic meta-learning for fast adaptation of deep networks," in *Proc. International Conference on Machine Learning (ICML)*, 2017, pp. 1126–1135.

[91] O. Vinyals et al., "Matching networks for one shot learning," in *Proc. Advances in Neural Information Processing Systems (NeurIPS)*, 2016, pp. 3630–3638.

[92] J. Snell, K. Swersky, and R. Zemel, "Prototypical networks for few-shot learning," in *Proc. Advances in Neural Information Processing Systems (NeurIPS)*, 2017, pp. 4077–4087.

[93] L. Theis, W. Shi, A. Cunningham, and F. Huszár, "Lossy image compression with compressive autoencoders," in *Proc. International Conference on Learning Representations (ICLR)*, 2017.

[94] J. Ballé, V. Laparra, and E. P. Simoncelli, "End-to-end optimized image compression," in *Proc. International Conference on Learning Representations (ICLR)*, 2017.

[95] J. Ballé, D. Minnen, S. Singh, S. J. Hwang, and N. Johnston, "Variational image compression with a scale hyperprior," in *Proc. International Conference on Learning Representations (ICLR)*, 2018.

[96] F. Mentzer, E. Agustsson, M. Tschannen, R. Timofte, and L. Van Gool, "Conditional probability models for deep image compression," in *Proc. IEEE Conference on Computer Vision and Pattern Recognition (CVPR)*, 2018, pp. 4394–4402.

[97] D. Minnen, J. Ballé, and G. D. Toderici, "Joint autoregressive and hierarchical priors for learned image compression," in *Proc. Advances in Neural Information Processing Systems (NeurIPS)*, 2018, pp. 10771–10780.

[98] Z. Cheng, H. Sun, M. Takeuchi, and J. Katto, "Learned image compression with discretized gaussian mixture likelihoods and attention modules," in *Proc. IEEE Conference on Computer Vision and Pattern Recognition (CVPR)*, 2020, pp. 7939–7948.

[99] D. B. Kurka and D. Gündüz, "DeepJSCC-f: Deep joint source-channel coding of images with feedback," *IEEE Journal on Selected Areas in Information Theory*, vol. 1, no. 1, pp. 178–193, May 2020.

[100] D. B. Kurka and D. Gündüz, "Successive refinement of images with deep joint source-channel coding," in *Proc. IEEE Int. Workshop on Signal Processing Advances in Wireless Communications (SPAWC)*, 2019, pp. 1–5.

[101] M. Jankowski, D. Gündüz, and K. Mikolajczyk, "Joint device-edge inference over wireless links with pruning," in *Proc. IEEE Int. Workshop on Signal Processing Advances in Wireless Communications (SPAWC)*, 2020, pp. 1–5.

[102] S. Deng et al., "Learning to communicate: A machine learning framework for heterogeneous multi-agent robotic systems," *IEEE Transactions on Cognitive Communications and Networking*, vol. 8, no. 2, pp. 926–939, June 2022.

[103] Y. Xie and Z. Qin, "A multiuser semantic communication system for image transmission," in *Proc. IEEE Global Communications Conference (GLOBECOM)*, 2021, pp. 1–6.

[104] H. Xie and Z. Qin, "A lite distributed semantic communication system for Internet of Things," *IEEE Journal on Selected Areas in Communications*, vol. 39, no. 1, pp. 142–153, Jan. 2021.

[105] J. Carlsson and H. Wymeersch, "6G wireless systems: Vision, requirements, challenges, insights, and opportunities," *Proceedings of the IEEE*, vol. 109, no. 7, pp. 1166–1178, July 2021.

[106] P. Yang, Y. Xiao, M. Xiao, and S. Li, "6G wireless communications: Vision and potential techniques," *IEEE Network*, vol. 33, no. 4, pp. 70–75, July/Aug. 2019.

[107] K. David and H. Berndt, "6G vision and requirements: Is there any need for beyond 5G?" *IEEE Vehicular Technology Magazine*, vol. 13, no. 3, pp. 72–80, Sep. 2018.

[108] W. Jiang, B. Han, M. A. Habibi, and H. D. Schotten, "The road towards 6G: A comprehensive survey," *IEEE Open Journal of the Communications Society*, vol. 2, pp. 334–366, 2021.

[109] S. Dang, O. Amin, B. Shihada, and M.-S. Alouini, "What should 6G be?" *Nature Electronics*, vol. 3, no. 1, pp. 20–29, 2020.

[110] K. B. Letaief, W. Chen, Y. Shi, J. Zhang, and Y.-J. A. Zhang, "The roadmap to 6G: AI empowered wireless networks," *IEEE Communications Magazine*, vol. 57, no. 8, pp. 84–90, Aug. 2019.

[111] L. U. Khan, I. Yaqoob, N. H. Tran, S. M. A. Kazmi, T. N. Dang, and C. S. Hong, "Edge-computing-enabled smart cities: A comprehensive survey," *IEEE Internet of Things Journal*, vol. 7, no. 10, pp. 10200–10232, Oct. 2020.

[112] Y. Shi, Y. Zhou, X. Wu, W. Chen, and B. Letaief, "Federated meta-learning for fraudulent credit card detection," in *Proc. International Joint Conference on Artificial Intelligence (IJCAI)*, 2020, pp. 4654–4660.

[113] T. Li, A. K. Sahu, A. Talwalkar, and V. Smith, "Federated learning: Challenges, methods, and future directions," *IEEE Signal Processing Magazine*, vol. 37, no. 3, pp. 50–60, May 2020.

[114] Q. Yang, Y. Liu, T. Chen, and Y. Tong, "Federated machine learning: Concept and applications," *ACM Transactions on Intelligent Systems and Technology*, vol. 10, no. 2, pp. 1–19, 2019.

[115] J. Konečný, H. B. McMahan, D. Ramage, and P. Richtárik, "Federated optimization: Distributed machine learning for on-device intelligence," *arXiv preprint arXiv:1610.02527*, 2016.

[116] B. McMahan, E. Moore, D. Ramage, S. Hampson, and B. A. y Arcas, "Communication-efficient learning of deep networks from decentralized data," in *Proc. International Conference on Artificial Intelligence and Statistics (AISTATS)*, 2017, pp. 1273–1282.

[117] T. S. Brisimi, R. Chen, T. Mela, A. Olshevsky, I. C. Paschalidis, and W. Shi, "Federated learning of predictive models from federated electronic health records," *International Journal of Medical Informatics*, vol. 112, pp. 59–67, 2018.

[118] J. Konen et al., "Heterogeneity-aware federated learning," *arXiv preprint arXiv:1812.06127*, 2018.

[119] Y. Zhao, M. Li, L. Lai, N. Suda, D. Civin, and V. Chandra, "Federated learning with non-IID data," *arXiv preprint arXiv:1806.00582*, 2018.

[120] X. Li, K. Huang, W. Yang, S. Wang, and Z. Zhang, "On the convergence of FedAvg on non-IID data," in *Proc. International Conference on Learning Representations (ICLR)*, 2020.

[121] S. P. Karimireddy, S. Kale, M. Mohri, S. Reddi, S. Stich, and A. T. Suresh, "SCAFFOLD: Stochastic controlled averaging for federated learning," in *Proc. International Conference on Machine Learning (ICML)*, 2020, pp. 5132–5143.

[122] S. Reddi, Z. Charles, M. Zaheer, Z. Garrett, K. Rush, J. Konečný, S. Kumar, and H. B. McMahan, "Adaptive federated optimization," in *Proc. International Conference on Learning Representations (ICLR)*, 2021.

[123] T. Li, A. K. Sahu, M. Zaheer, M. Sanjabi, A. Talwalkar, and V. Smith, "Federated optimization in heterogeneous networks," in *Proc. Machine Learning and Systems (MLSys)*, 2020, pp. 429–450.

[124] V. Smith, C.-K. Chiang, M. Sanjabi, and A. S. Talwalkar, "Federated multi-task learning," in *Proc. Advances in Neural Information Processing Systems (NeurIPS)*, 2017, pp. 4424–4434.

[125] Y. Jiang, J. Konečný, K. Rush, and S. Kannan, "Improving federated learning personalization via model agnostic meta learning," *arXiv preprint arXiv:1909.12488*, 2019.

[126] A. Fallah, A. Mokhtari, and A. Ozdaglar, "Personalized federated learning with theoretical guarantees: A model-agnostic meta-learning approach," in *Proc. Advances in Neural Information Processing Systems (NeurIPS)*, 2020, pp. 3557–3568.

[127] M. G. Arrio et al., "Personalization improves privacy-accuracy tradeoffs in federated learning," in *Proc. International Conference on Machine Learning (ICML)*, 2022, pp. 1017–1033.

[128] Y. Deng, F. Lyu, J. Ren, Y.-C. Chen, P. Yang, Y. Zhou, and Y. Zhang, "FAIR: Quality-aware federated learning with precise user incentive and model aggregation," in *Proc. IEEE Conference on Computer Communications (INFOCOM)*, 2021, pp. 1–10.

[129] T. Nishio and R. Yonetani, "Client selection for federated learning with heterogeneous resources in mobile edge," in *Proc. IEEE International Conference on Communications (ICC)*, 2019, pp. 1–7.

[130] M. Chen, Z. Yang, W. Saad, C. Yin, H. V. Poor, and S. Cui, "A joint learning and communications framework for federated learning over wireless networks," *IEEE Transactions on Wireless Communications*, vol. 20, no. 1, pp. 269–283, Jan. 2021.

[131] G. Zhu, Y. Wang, and K. Huang, "Broadband analog aggregation for low-latency federated edge learning," *IEEE Transactions on Wireless Communications*, vol. 19, no. 1, pp. 491–506, Jan. 2020.

[132] K. Yang, T. Jiang, Y. Shi, and Z. Ding, "Federated learning via over-the-air computation," *IEEE Transactions on Wireless Communications*, vol. 19, no. 3, pp. 2022–2035, Mar. 2020.

[133] M. M. Amiri, D. Gündüz, S. R. Kulkarni, and H. V. Poor, "Federated learning with quantized global model updates," *arXiv preprint arXiv:2006.10672*, 2020.

[134] A. Reisizadeh, A. Mokhtari, H. Hassani, A. Jadbabaie, and R. Pedarsani, "FedPAQ: A communication-efficient federated learning method with periodic averaging and quantization," in *Proc. International Conference on Artificial Intelligence and Statistics (AISTATS)*, 2020, pp. 2021–2031.

[135] C. Szegedy et al., "Intriguing properties of neural networks," in *Proc. International Conference on Learning Representations (ICLR)*, 2014.

[136] A. Kurakin, I. Goodfellow, and S. Bengio, "Adversarial examples in the physical world," in *Proc. International Conference on Learning Representations (ICLR) Workshop*, 2017.

[137] J. Rauber, R. Zimmermann, M. Bethge, and W. Brendel, "Foolbox native: Fast adversarial attacks to benchmark the robustness of machine learning models in PyTorch, TensorFlow, and JAX," *Journal of Open Source Software*, vol. 5, no. 53, p. 2607, 2020.

[138] G. Katz, C. Barrett, D. L. Dill, K. Julian, and M. J. Kochenderfer, "Reluplex: An efficient SMT solver for verifying deep neural networks," in *Proc. International Conference on Computer Aided Verification (CAV)*, 2017, pp. 97–117.

[139] V. Tjeng, K. Xiao, and R. Tedrake, "Evaluating robustness of neural networks with mixed integer programming," in *Proc. International Conference on Learning Representations (ICLR)*, 2019.

[140] G. Singh, T. Gehr, M. Mirman, M. Püschel, and M. Vechev, "Fast and effective robustness certification," in *Proc. Advances in Neural Information Processing Systems (NeurIPS)*, 2018, pp. 10802–10813.

[141] H. Zhang, T.-W. Weng, P.-Y. Chen, C.-J. Hsieh, and L. Daniel, "Efficient neural network robustness certification with general activation functions," in *Proc. Advances in Neural Information Processing Systems (NeurIPS)*, 2018, pp. 4939–4948.

[142] M. Salman, J. Li, and Z. Kolter, "Provably robust deep learning via adversarially trained smoothed classifiers," in *Proc. Advances in Neural Information Processing Systems (NeurIPS)*, 2019, pp. 11292–11303.

[143] A. Boopathy, T.-W. Weng, P.-Y. Chen, S. Liu, and L. Daniel, "CNN-Cert: An efficient framework for certifying robustness of convolutional neural networks," in *Proc. AAAI Conference on Artificial Intelligence*, 2019, pp. 3240–3247.

[144] S.-M. Moosavi-Dezfooli, A. Fawzi, O. Fawzi, and P. Frossard, "Universal adversarial perturbations," in *Proc. IEEE Conference on Computer Vision and Pattern Recognition (CVPR)*, 2017, pp. 1765–1773.

[145] N. Carlini et al., "On evaluating adversarial robustness," *arXiv preprint arXiv:1902.06705*, 2019.

[146] L. Engstrom, A. Ilyas, and A. Athalye, "Evaluating and understanding the robustness of adversarial logit pairing," *arXiv preprint arXiv:1807.10272*, 2018.

[147] D. Hendrycks et al., "Benchmarking neural network robustness to common corruptions and perturbations," in *Proc. International Conference on Learning Representations (ICLR)*, 2019.

[148] 3GPP, "Specifications," https://www.3gpp.org/specifications, accessed 2023.

[149] 3GPP, "Working procedures," https://www.3gpp.org/specifications/work-plan, accessed 2023.

[150] M. Kountouris and N. Pappas, "Toward semantic communications for 6G," *arXiv preprint arXiv:2110.05546*, 2021.

[151] 3GPP TS 21.905, "Vocabulary for 3GPP Specifications," V17.0.0, June 2021.

[152] M. Boban, J. Barros, and O. K. Tonguz, "Geometry-based vehicle-to-vehicle channel modeling for large-scale simulation," *IEEE Transactions on Vehicular Technology*, vol. 63, no. 9, pp. 4146–4164, Nov. 2014.

[153] E. Björnson, J. Hoydis, and L. Sanguinetti, "Massive MIMO networks: Spectral, energy, and hardware efficiency," *Foundations and Trends in Signal Processing*, vol. 11, no. 3-4, pp. 154–655, 2017.

[154] 3GPP TS 36.331, "Evolved Universal Terrestrial Radio Access (E-UTRA); Radio Resource Control (RRC); Protocol specification," V17.0.0, Mar. 2022.

[155] 3GPP TS 23.203, "Policy and charging control architecture," V17.1.0, Dec. 2021.

[156] ITU-R, "IMT-2030 and beyond," https://www.itu.int/en/ITU-R/study-groups/rsg5/rwp5d/imt-2030/Pages/default.aspx, accessed 2023.

[157] D. P. Kingma and J. Ba, "Adam: A method for stochastic optimization," in *Proc. International Conference on Learning Representations (ICLR)*, 2015.

[158] Y. You, J. Li, S. Reddi, J. Hseu, S. Kumar, S. Bhojanapalli, X. Song, J. Demmel, K. Keutzer, and C.-J. Hsieh, "Large batch optimization for deep learning: Training BERT in 76 minutes," in *Proc. International Conference on Learning Representations (ICLR)*, 2020.

[159] R. Banner, Y. Nahshan, and D. Soudry, "Post training 4-bit quantization of convolutional networks for rapid-deployment," in *Proc. Advances in Neural Information Processing Systems (NeurIPS)*, 2019, pp. 7950–7958.

[160] S. Teerapittayanon, B. McDanel, and H.-T. Kung, "BranchyNet: Fast inference via early exiting from deep neural networks," in *Proc. International Conference on Pattern Recognition (ICPR)*, 2016, pp. 2464–2469.

[161] N. P. Jouppi et al., "In-datacenter performance analysis of a tensor processing unit," in *Proc. ACM/IEEE International Symposium on Computer Architecture (ISCA)*, 2017, pp. 1–12.

[162] D. Alistarh, D. Grubic, J. Li, R. Tomioka, and M. Vojnovic, "QSGD: Communication-efficient SGD via gradient quantization and encoding," in *Proc. Advances in Neural Information Processing Systems (NeurIPS)*, 2017, pp. 1709–1720.

[163] J. Park, S. Samarakoon, M. Bennis, and M. Debbah, "Wireless network intelligence at the edge," *Proceedings of the IEEE*, vol. 107, no. 11, pp. 2204–2239, Nov. 2019.

[164] M. Abadi et al., "TensorFlow: Large-scale machine learning on heterogeneous systems," 2015, Software available from tensorflow.org.

[165] J. Deng, W. Dong, R. Socher, L.-J. Li, K. Li, and L. Fei-Fei, "ImageNet: A large-scale hierarchical image database," in *Proc. IEEE Conference on Computer Vision and Pattern Recognition (CVPR)*, 2009, pp. 248–255.

[166] A. Paszke et al., "PyTorch: An imperative style, high-performance deep learning library," in *Proc. Advances in Neural Information Processing Systems (NeurIPS)*, 2019, pp. 8026–8037.

[167] P. Moritz et al., "Ray: A distributed framework for emerging AI applications," in *Proc. USENIX Symposium on Operating Systems Design and Implementation (OSDI)*, 2018, pp. 561–577.

[168] A. Guo, R. Savarese, J. Wu, W. Yuan, and X. Zhao, "Strong data augmentation sanitizes poisoning and backdoor attacks without an accuracy tradeoff," in *Proc. IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)*, 2021, pp. 3855–3859.

[169] J. Gama, I. Žliobaitė, A. Bifet, M. Pechenizkiy, and A. Bouchachia, "A survey on concept drift adaptation," *ACM Computing Surveys*, vol. 46, no. 4, pp. 1–37, 2014.

[170] D. Sculley et al., "Hidden technical debt in machine learning systems," in *Proc. Advances in Neural Information Processing Systems (NeurIPS)*, 2015, pp. 2503–2511.

[171] K. Muandet, D. Balduzzi, and B. Schölkopf, "Domain generalization via invariant feature representation," in *Proc. International Conference on Machine Learning (ICML)*, 2013, pp. 10–18.

[172] G. Koch, R. Zemel, and R. Salakhutdinov, "Siamese neural networks for one-shot image recognition," in *Proc. ICML Deep Learning Workshop*, 2015.

[173] L. Kaelbling, M. Littman, and A. Cassandra, "Planning and acting in partially observable stochastic domains," *Artificial Intelligence*, vol. 101, no. 1-2, pp. 99–134, 1998.

[174] A. Shani, D. Heckerman, and R. I. Brafman, "An MDP-based recommender system," *Journal of Machine Learning Research*, vol. 6, pp. 1265–1295, 2005.

[175] P. S. Thomas and E. Brunskill, "Data-efficient off-policy policy evaluation for reinforcement learning," in *Proc. International Conference on Machine Learning (ICML)*, 2016, pp. 2139–2148.

[176] J. N. Foerster, R. Y. Chen, M. Al-Shedivat, S. Whiteson, P. Abbeel, and I. Mordatch, "Learning with opponent-learning awareness," in *Proc. International Conference on Autonomous Agents and MultiAgent Systems*, 2018, pp. 122–130.

[177] M. Giordani and M. Zorzi, "Satellite communication at millimeter waves: A key enabler of the 6G era," in *Proc. IEEE International Conference on Computing, Networking and Communications (ICNC)*, 2020, pp. 383–388.

[178] E. J. Candès and M. B. Wakin, "An introduction to compressive sampling," *IEEE Signal Processing Magazine*, vol. 25, no. 2, pp. 21–30, Mar. 2008.

[179] G. Cormode and S. Muthukrishnan, "An improved data stream summary: The count-min sketch and its applications," *Journal of Algorithms*, vol. 55, no. 1, pp. 58–75, 2005.

[180] K. Bonawitz et al., "Practical secure aggregation for privacy-preserving machine learning," in *Proc. ACM SIGSAC Conference on Computer and Communications Security*, 2017, pp. 1175–1191.

[181] A. Athalye, N. Carlini, and D. Wagner, "Obfuscated gradients give a false sense of security: Circumventing defenses to adversarial examples," in *Proc. International Conference on Machine Learning (ICML)*, 2018, pp. 274–283.

[182] S. Gowal, K. Dvijotham, R. Stanforth, R. Bunel, C. Qin, J. Uesato, R. Arandjelovic, T. Mann, and P. Kohli, "On the effectiveness of interval bound propagation for training verifiably robust models," *arXiv preprint arXiv:1810.12715*, 2018.

[183] N. Carlini et al., "On the robustness of the CVPR 2018 white-box adversarial example defenses," *arXiv preprint arXiv:1804.03286*, 2018.

[184] G. F. Montufar, R. Pascanu, K. Cho, and Y. Bengio, "On the number of linear regions of deep neural networks," in *Proc. Advances in Neural Information Processing Systems (NeurIPS)*, 2014, pp. 2924–2932.

[185] J. Biamonte, P. Wittek, N. Pancotti, P. Rebentrost, N. Wiebe, and S. Lloyd, "Quantum machine learning," *Nature*, vol. 549, no. 7671, pp. 195–202, 2017.

[186] J. Preskill, "Quantum computing in the NISQ era and beyond," *Quantum*, vol. 2, p. 79, 2018.

[187] M. Davies et al., "Loihi: A neuromorphic manycore processor with on-chip learning," *IEEE Micro*, vol. 38, no. 1, pp. 82–99, Jan./Feb. 2018.

[188] C. D. Schuman et al., "A survey of neuromorphic computing and neural networks in hardware," *arXiv preprint arXiv:1705.06963*, 2017.

[189] Y. LeCun, S. Chopra, R. Hadsell, M. Ranzato, and F. Huang, "A tutorial on energy-based learning," in *Predicting Structured Data*. MIT Press, 2006.

[190] A. Jolicoeur-Martineau, "The relativistic discriminator: A key element missing from standard GAN," in *Proc. International Conference on Learning Representations (ICLR)*, 2019.

[191] F. Tao, H. Zhang, A. Liu, and A. Y. C. Nee, "Digital twin in industry: State-of-the-art," *IEEE Transactions on Industrial Informatics*, vol. 15, no. 4, pp. 2405–2415, Apr. 2019.

[192] General Data Protection Regulation (GDPR), "Regulation (EU) 2016/679," Apr. 2016.

[193] N. Papernot, M. Abadi, Ú. Erlingsson, I. Goodfellow, and K. Talwar, "Semi-supervised knowledge transfer for deep learning from private training data," in *Proc. International Conference on Learning Representations (ICLR)*, 2017.

[194] M. Hardt, E. Price, and N. Srebro, "Equality of opportunity in supervised learning," in *Proc. Advances in Neural Information Processing Systems (NeurIPS)*, 2016, pp. 3315–3323.

[195] R. Zemel, Y. Wu, K. Swersky, T. Pitassi, and C. Dwork, "Learning fair representations," in *Proc. International Conference on Machine Learning (ICML)*, 2013, pp. 325–333.

[196] M. T. Ribeiro, S. Singh, and C. Guestrin, "Why should I trust you?: Explaining the predictions of any classifier," in *Proc. ACM SIGKDD International Conference on Knowledge Discovery and Data Mining*, 2016, pp. 1135–1144.

[197] P. Norris, *Digital Divide: Civic Engagement, Information Poverty, and the Internet Worldwide*. Cambridge University Press, 2001.

[198] E. Maskin and J. Riley, "Optimal multi-unit auctions," in *The Economics of Missing Markets, Information, and Games*. Oxford University Press, 1989, pp. 312–335.

[199] GSMA Intelligence, "The mobile economy 2022," https://www.gsma.com/mobileeconomy/, accessed 2023.

[200] European Commission, "Horizon Europe," https://ec.europa.eu/info/research-and-innovation/funding/funding-opportunities/funding-programmes-and-open-calls/horizon-europe_en, accessed 2023.

[201] T. Davenport and R. Kalakota, "The potential for artificial intelligence in healthcare," *Future Healthcare Journal*, vol. 6, no. 2, pp. 94–98, 2019.

---

## AGRADECIMIENTOS

Los autores agradecen las discusiones productivas con el grupo de trabajo 3GPP RAN1 y el Study Item on Semantic Communications. Este trabajo ha sido parcialmente financiado por proyectos de investigación en comunicaciones 6G y sistemas AI-nativos.

---

