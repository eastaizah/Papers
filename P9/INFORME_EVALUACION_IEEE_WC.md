# INFORME DE EVALUACIÓN CIENTÍFICA PARA PUBLICACIÓN EN IEEE WIRELESS COMMUNICATIONS (Q1)

**Título del artículo:** *A Multi-Dimensional Semantic Metric Standardization Framework for Evaluating AI-Native Systems in 6G Networks*

**Archivo evaluado:** `P9/Framework_Semanticas_Summary_IEEE_Final.docx` / `P9/Framework_Semanticas_Summary_IEEE.md`

**Scripts evaluados:** `P9/simulate_semantic_metrics.py`, `P9/complexity_channels_analysis.md`, `P9/measurement_algorithms.md`

**Resultados evaluados:** `P9/simulation_results/`

**Fecha de evaluación:** Mayo 2026

**Evaluador:** Agente de evaluación especializado (experto en edición académica, comunicaciones inalámbricas e IA)

---

## RESUMEN EJECUTIVO

El artículo propone un marco de estandarización de métricas semánticas multi-dimensional para evaluar sistemas de comunicación con IA nativa en redes 6G. La propuesta es oportuna, relevante para la comunidad de comunicaciones inalámbricas y aborda una brecha real en los procesos de estandarización del 3GPP. El trabajo tiene potencial de publicación en IEEE Wireless Communications, aunque requiere correcciones significativas en rigor matemático, coherencia experimental, validación de afirmaciones clave e incorporación de figuras actualmente descritas solo en texto. A continuación se detallan todos los hallazgos.

---

## I. EVALUACIÓN DESDE LA PERSPECTIVA DEL EDITOR DE LA REVISTA

### I.1 Ajuste al alcance y relevancia del journal

IEEE Wireless Communications es una revista de alto impacto (Q1, FI ≈ 10.9) enfocada en artículos de tutorial y revisión con fuerte componente técnico. El artículo encaja bien temáticamente: aborda comunicaciones semánticas para 6G, estandarización y sistemas con IA nativa, que son temas de máxima actualidad y alineados con los intereses editoriales de la revista. El tono del artículo tiene carácter de tutorial/survey técnico, lo que es compatible con el formato típico de IEEE Wireless Communications.

**Valoración: ADECUADO AL ALCANCE. Requiere mejoras para ser aceptable.**

### I.2 Impacto y originalidad

**Puntos fuertes:**
- Propone una taxonomía de cuatro dimensiones con 16 métricas formalmente definidas para evaluar sistemas de comunicación semántica, lo que representa una contribución concreta y estructurada.
- Identifica y aborda explícitamente seis brechas de estandarización en el ecosistema 3GPP actual.
- Ofrece una ruta de estandarización concreta con propuesta de nueva serie TS 39.xxx.
- La integración de teoría de la información, transporte óptimo y teoría de juegos como bases teóricas es novedosa y bien articulada.

**Puntos débiles relativos a impacto:**
- La referencia [70] (Qin et al., 2024, "Semantic metrics for evaluating semantic communication systems," *IEEE Wireless Communications*) aparece identificada en el propio artículo como "trabajo directamente competitivo." Sin embargo, la diferenciación con este trabajo no está suficientemente desarrollada. Un editor de IEEE Wireless Communications detectará inmediatamente este solapamiento y exigirá una demostración explícita de superioridad o complementariedad.
- El marco propuesto es predominantemente teórico y los experimentos de validación emplean datos sintéticos (Gaussianas condicionales de clase), lo que limita la demostración de utilidad práctica.
- Las afirmaciones cuantitativas sobre reducción de overhead (60–80%) y TSR > 0.87 están respaldadas por simulaciones con datos sintéticos, no con datasets estándar del campo (CIFAR-10, ImageNet, COCO), lo que debilita las afirmaciones de rendimiento.

**Valoración de originalidad: MODERADA-ALTA. Requiere mejor diferenciación del trabajo competitivo [70].**

### I.3 Potencial de citación

El artículo tiene potencial de citación razonable dado que: (a) aborda estandarización 3GPP, que genera muchas citas en el campo; (b) propone métricas concretas que otros investigadores podrían adoptar o referenciar; (c) incluye una taxonomía estructurada que facilita su uso como referencia en trabajos futuros. Sin embargo, si [70] es publicado primero con contenido similar, el potencial de citación se reduce significativamente.

### I.4 Presentación profesional

El artículo está bien estructurado y escrito en inglés técnico fluido. Sin embargo, existen problemas de presentación que afectan la profesionalidad:
1. **Figuras ausentes**: El artículo describe 8 figuras (Figs. 1–8) pero ninguna está incluida; solo aparecen descripciones textuales de las mismas. Esto es inaceptable para una revista IEEE. Todas las figuras deben generarse e insertarse.
2. **Inconsistencias en la numeración de tablas**: La Tabla IV aparece en la Sección XI.E pero es referenciada antes en la Sección XI.A como referencia de validación. La Tabla V aparece en la Sección XI.D sin seguir el orden natural.
3. **Notación matemática**: Todas las expresiones matemáticas están correctamente en formato LaTeX. No se detectan errores de formato matemático.

---

## II. EVALUACIÓN DESDE LA PERSPECTIVA DEL INVESTIGADOR EXPERTO

### II.1 Validez y solidez de los métodos

**Positivo:**
- Las definiciones matemáticas de las 16 métricas son formales y acompañadas de demostraciones de propiedades (Teoremas 1–4). Las demostraciones revisadas son matemáticamente correctas en sus líneas generales.
- El Teorema 1 (Compresión Semántica) está correctamente demostrado usando la desigualdad de procesamiento de datos.
- El Teorema 2 (Monotonicidad RSE) es correcto y bien argumentado.
- El Teorema 3 (Cota de Consenso) tiene una argumentación razonable aunque emplea la desigualdad de Jensen de forma informal.
- El Teorema 4 (Certificado de Suavizado Aleatorio) reproduce correctamente el resultado de Cohen et al. [36].

**Problemas detectados en métodos:**

**M1 — Estimación de entropía semántica (RSE y NSMI):** En el script `simulate_semantic_metrics.py`, la entropía semántica $H_s(X;\mathcal{T})$ se estima añadiendo jitter gaussiano infinitesimal a los propios datos y calculando la MI con ellos mismos. Esto es un proxy muy burdo que no mide entropía genuina; produce valores de RSE sistemáticamente bajos (0.05–0.11 según Tabla en Sección XI.B) que sugieren una pérdida de información semántica del 89–95%, inconsistente con las afirmaciones de alta fidelidad del artículo. Esta discrepancia no está explicada ni justificada.

**M2 — Datos sintéticos vs. datos reales:** La simulación utiliza embeddings Gaussianos condicionales de clase como "proxy" de CLIP y Sentence-BERT. Aunque computacionalmente práctico, esto invalida las afirmaciones específicas sobre rendimiento con modelos de foundation reales. El artículo menciona CLIP y Sentence-BERT pero la simulación no los utiliza.

**M3 — Métricas de resiliencia parcialmente simuladas:** En `simulate_semantic_metrics.py`, líneas 652–658, las métricas ARR, SASR, CertCost, CertRadius y MSD para configuraciones no-AWGN o SNR distintos de {0, 5, 10, 15, 20} dB son **imputadas mediante fórmulas analíticas ad hoc** y no computadas mediante los algoritmos definidos en el artículo. Esto significa que la Tabla V, que compara múltiples canales, contiene valores de resiliencia que no son resultados de simulación real sino interpolaciones. Esto es una inconsistencia científica grave que debe corregirse.

**M4 — Modelo de canal TDL-A simplificado:** El modelo TDL-A implementado usa solo 3 taps con potencias [0.60, 0.24, 0.16] sin delays ni Doppler, lo que difiere significativamente del perfil TDL-A completo de 3GPP TR 38.901 (23 taps). Los resultados con "TDL-A" tienen validez limitada como representación del estándar 3GPP.

**M5 — Resultado contraintuitivo sobre TDL-A y S³I:** El artículo afirma que TDL-A logra el S³I más alto (0.533 vs. 0.481 para AWGN), atribuyendo esto a "diversidad multipropagación que decorrela las distorsiones por dimensión." Esta explicación carece de sustento teórico formal. En un modelo de embeddings sintéticos sin estructura espacial, la diversidad frecuencial del canal no tiene un mecanismo claro para mejorar la similitud estructural. Este resultado requiere una explicación más rigurosa o debe revisarse.

### II.2 Robustez y corrección de los datos

**D1 — Muestra de Monte Carlo:** $N = 1{,}000$ muestras es modesto para una evaluación estadística rigurosa de 16 métricas en 5 canales × 14 puntos de SNR × 5 valores de $k$. Algunos estimadores (kNN MI) son conocidos por tener alta varianza con muestras pequeñas. Deben reportarse intervalos de confianza para todas las métricas, no solo para TSR.

**D2 — Semilla única:** Todos los experimentos usan `seed = 42`. Aunque esto garantiza reproducibilidad exacta, no permite evaluar la variabilidad entre semillas, que es importante para validar la robustez estadística de los resultados. Se recomienda reportar resultados promediados sobre al menos 5 semillas.

**D3 — TSR de bit-exact = 0.950:** Esta afirmación es crítica. El artículo presenta la transmisión exacta de bits como limitada al 95% de TSR, mientras que el sistema propuesto con enorme compresión (6.25%) logra 86.7%. Esto implica que hay un 13.3% de degradación atribuible solo a la compresión/cuantización semántica. El artículo no discute esta brecha ni justifica por qué un sistema de comunicación semántica sería preferido cuando la transmisión bit-exacta logra mayor TSR a igual complejidad de canal. Esto es un punto de debilidad argumental importante.

**D4 — Inconsistencia entre Table IV y afirmaciones en texto:** En la Tabla IV (comparación de sistemas), se indica ARR = 0.045 para el sistema propuesto (k=32), pero en la descripción de Fig. 8 se menciona que el sistema propuesto alcanza SASR=0.5 en ε ≈ 0.15 (es decir, ARR ≈ 0.15). En la Sección XI.E se indica "ARR = 0.15 vs. 0.08–0.10 para sistemas previos." El valor 0.045 de la Tabla IV contradice el 0.15 del texto. Esta inconsistencia es grave.

**D5 — CertCost inconsistente:** La Tabla IV reporta CertCost = 0.045 s para el sistema propuesto, pero la descripción del método CertCost (líneas 532–558 del script) mide wall-clock time en 50 muestras con 100 perturbaciones de suavizado cada una, lo que depende críticamente del hardware. El valor de 0.045 s no puede ser reproducido sin especificación del hardware y no es una métrica válida para comparación entre sistemas.

### II.3 Análisis estadístico

El artículo emplea apropiadamente los intervalos de confianza de Wilson para TSR. Sin embargo:
- No se reportan intervalos de confianza para RSE, SWD, S³I, NSMI, AP, SU, CE, ID, ICC, SCI, PF, ARR, SASR, MSD.
- La discusión estadística de la Sección XI.C (TSR vs. SNR) es la más completa del artículo; el resto de las secciones carece de análisis estadístico comparable.

### II.4 Apoyo de las conclusiones por los datos

**C1 — Afirmación de reducción de overhead del 60–80%:** El script verifica que la reducción de overhead es del 93.75% (k=32/d=512), lo que *supera* la afirmación del 60–80%. Aunque el artículo reconoce esto en la Sección XIII, hay una incongruencia entre el abstract ("60–80% transmission overhead reduction") y los resultados reales (93.75%). El abstract debería corregirse para reportar el valor real demostrado.

**C2 — "Task effectiveness above 87%":** Esta afirmación del abstract está respaldada por TSR = 0.867 ± 0.021 (95% CI). Sin embargo, aplica solo a AWGN con k=32 y SNR ≥ 10 dB. Con canal Rayleigh la eficacia cae a 57.9%, lo que debilita la afirmación general. El abstract debe ser más preciso sobre las condiciones de canal.

**C3 — Ventaja de degradación graceful:** La comparación con JPEG2000+LDPC en el rango de bajo SNR es legítima y bien documentada. La ventaja a 0 dB (TSR semántico = 0.380 vs. 0.017 clásico) es un resultado valioso y claramente respaldado por los datos.

### II.5 Estado del arte y citas relevantes

**Citas presentes y correctas (verificación de DOI y consistencia):**

| Ref. | Autores | Publicación | Estado DOI |
|------|---------|-------------|------------|
| [1] | Giordani et al., 2020 | IEEE Comm. Mag. | **DOI verificable:** 10.1109/MCOM.001.1900534 ✓ |
| [2] | Saad et al., 2020 | IEEE Network | **DOI verificable:** 10.1109/MNET.001.1900287 ✓ |
| [7] | Shannon & Weaver, 1949 | Libro | Clásico, no requiere DOI ✓ |
| [9] | Gündüz et al., 2023 | IEEE JSAC | **DOI verificable:** 10.1109/JSAC.2022.3221556 ✓ |
| [10] | Xie et al., 2021 | IEEE Trans. Signal Process. | **DOI verificable:** 10.1109/TSP.2021.3068858 ✓ |
| [14] | Carnap & Bar-Hillel, 1952 | MIT Tech. Rep. | Referencia clásica; no tiene DOI moderno, accesible en repositorios ✓ |
| [15] | Cuturi, 2013 | NeurIPS | Verificable en proceedings NeurIPS ✓ |
| [20] | Cover & Thomas, 2006 | Libro | Clásico; DOI del libro: 10.1002/047174882X ✓ |
| [24] | Kraskov et al., 2004 | Phys. Rev. E | **DOI:** 10.1103/PhysRevE.69.066138 ✓ |
| [25] | Wang et al., 2004 | IEEE Trans. Image Process. | **DOI:** 10.1109/TIP.2003.819861 ✓ |
| [36] | Cohen et al., 2019 | ICML | Verificable en ICML 2019 proceedings ✓ |
| [46] | Bourtsoulatze et al., 2019 | IEEE Trans. Cogn. Commun. | **DOI:** 10.1109/TCCN.2019.2937851 ✓ |
| [66] | Qin et al., 2022 | arXiv:2201.01389 | arXiv preprint; existe en arXiv ✓ |
| [67] | Yang et al., 2023 | IEEE Comm. Surveys & Tutor. | **DOI:** 10.1109/COMST.2022.3223908 ✓ |
| [70] | Qin et al., 2024 | IEEE Wireless Commun. | **Problema:** La cita está formateada como publicación en IEEE Wireless Communications 2024, pero a la fecha de evaluación (mayo 2026) debe verificarse si efectivamente fue publicada con ese DOI o si sigue siendo preprint. Esta referencia es crítica dado el solapamiento temático. |
| [74] | Jiang et al., 2024 | IEEE Comm. Magazine | **Problema:** citado sin DOI ni volumen/número/páginas. Debe completarse. |

**Referencias con información incompleta o problemática:**

- **[28]** y **[29]**: Ambas son preprints de arXiv de Kountouris & Pappas (2021, 2022). La [28] (arXiv:2110.05546) puede haberse publicado posteriormente en una revista. Debe verificarse y actualizarse la referencia a la versión publicada si existe.
- **[54]**: Gowal et al. citado como arXiv preprint 1810.12715. Este trabajo fue publicado en NeurIPS 2018 workshop y posteriormente en ICLR 2020. Debe actualizarse a la versión de revista/conferencia.
- **[61]**: Bao & Basu, "Semantic entropy and information," *Entropy*, 2021. DOI verificable: 10.3390/e23040397. Sin embargo, la referencia a este artículo para la "caracterización independiente" de la entropía semántica (Sección II.A, línea 51) puede ser cuestionada por revisores: el artículo de Bao & Basu trata entropía semántica en un contexto filosófico/lingüístico distinto al de comunicaciones inalámbricas.
- **[69]**: Seo et al., "Semantics-native communication with contextual reasoning," IEEE Trans. Wireless Commun., 2024. La cita aparece sin DOI, volumen ni páginas. Debe completarse.
- **[71]**: Shao et al., "Task-oriented communication for multi-device cooperative edge inference," IEEE Trans. Wireless Commun., vol. 72, no. 1. El volumen 72 de IEEE TWC no existe actualmente (el volumen más reciente al momento de redacción es ~23); esto parece un error tipográfico grave que debe corregirse.

**Citas ausentes relevantes que deben incorporarse:**

1. **DeepSC (Xie et al., 2021):** "Deep learning enabled semantic communication systems with speech recognition" – trabajo fundamental en comunicaciones semánticas para voz.
2. **JSAC 2022 – Semantic communications survey de Qin et al.:** El tema de métricas semánticas para sistemas multi-tarea requiere citar trabajos sobre KB-enabled semantic communications.
3. **B. Xia et al. (2023):** "Generalized semantic communication with multi-task capability" – relevante para multi-task semantic metrics.
4. **ITU-T Y.3172:** Marco de arquitectura para machine learning en redes de comunicaciones futuras; crítico para el argumento de estandarización.
5. **3GPP TR 22.874:** Study on traffic characteristics and performance requirements for AI/ML model transfer; relevante para la propuesta de TS 39.xxx.
6. **Weng & Qin (2021):** "Semantic Communication Systems for Speech Transmission" – trabajo pionero en comunicaciones semánticas para señales de voz.
7. **H. Lu et al. (2024):** "OFDM-based joint semantic and channel coding for semantic communication" – trabajo reciente altamente relevante sobre la implementación de comunicaciones semánticas en sistemas OFDM realistas.

### II.6 Calidad de la escritura y coherencia

El inglés científico es generalmente correcto y fluido. La estructura del artículo sigue convenciones IEEE. Sin embargo:
- La Sección XI.E ("Simulation-Based Performance Comparison") aparece después de la Sección XI.D ("Multi-Channel Performance Analysis"), pero la Tabla IV que aparece en XI.E es referenciada en XI.A como referencia de calibración. El orden debe reorganizarse para presentar primero las comparaciones del sistema base y luego el análisis multi-canal.
- El abstract afirma "60–80% transmission overhead reduction" pero los resultados muestran 93.75%. Esta inconsistencia debe corregirse.
- La afirmación "task effectiveness above 87%" en el abstract es incompleta sin especificar condiciones de canal.
- Las descripciones textuales de figuras (Figs. 1–8) están embebidas en el texto principal como párrafos, lo que es inusual. Las figuras deben generarse y las descripciones deben convertirse en pies de figura (captions) estándar IEEE.

### II.7 Flujo lógico entre secciones

El flujo general del artículo es lógico: fundamentos teóricos → brechas de estandarización → framework → métricas por dimensión → estandarización 3GPP → implementación → simulaciones → desafíos → conclusiones. Sin embargo:
- La Sección IX (Mapeo 3GPP) interrumpe el flujo entre la definición de métricas (Secciones V–VIII) y su evaluación experimental (Sección XI). Se recomienda mover la Sección IX después de la Sección XI o crear una sección integrada.
- La Sección X (Consideraciones de Implementación) es extensa y puede condensarse para no dilatar el artículo antes de los resultados experimentales.

---

## III. FIGURAS FALTANTES: ESPECIFICACIONES PARA GENERACIÓN

El artículo describe 8 figuras en texto pero ninguna está generada. A continuación se especifican las figuras que deben incorporarse, con descripción detallada para su generación y su referenciación en el artículo.

---

### **Figura 1. Arquitectura del Marco de Estandarización de Métricas Semánticas Multi-Dimensional**
*(Referenciada en Sección IV.B, párrafo 3)*

**Descripción para generación:** Diagrama de bloques arquitectónico de alta resolución en orientación vertical. En la base, un rectángulo horizontal de color gris claro con borde sólido etiquetado "Fundamentos Teóricos" conteniendo tres subbloques internos: "Teoría de la Información", "Transporte Óptimo" y "Teoría de Juegos", separados por líneas verticales punteadas. Sobre este bloque base, cuatro columnas paralelas equidistantes, cada una un rectángulo vertical con borde redondeado: (1) columna azul "Fidelidad Semántica" con cuatro subbloques internos etiquetados RSE, SWD, S³I, NSMI de arriba a abajo; (2) columna verde "Exactitud de Compleción de Tarea" con subbloques TSR, AP, SU, CE; (3) columna naranja "Alineación de Intención" con subbloques ID, ICC, SCI, PF; (4) columna roja "Resiliencia a Ataques Semánticos" con subbloques ARR, SASR, CertCost, MSD. Flechas ascendentes desde cada columna convergen en un rectángulo horizontal superior de color dorado etiquetado "Agregación Multi-Dimensional ($M_{\text{composite}}$)". A la derecha del diagrama, un bloque vertical de color morado etiquetado "Mapeo 3GPP" con cuatro subbloques: TS 39.101, TS 39.201, TS 39.202, TS 39.521, conectados con flechas horizontales a las columnas correspondientes. Entre columnas adyacentes se incluyen flechas bidireccionales con etiquetas de relación: entre (1) y (2) "$\Phi$: no-inyectiva", entre (2) y (3) "necesaria no suficiente", entre (1) y (4) "compromiso Pareto".

**Pie de figura:** "Fig. 1. Arquitectura del Marco de Estandarización de Métricas Semánticas Multi-Dimensional. Los cuatro pilares del marco (Fidelidad Semántica, Exactitud de Compleción de Tarea, Alineación de Intención y Resiliencia a Ataques) se fundamentan en teoría de la información, transporte óptimo y teoría de juegos, y se mapean a la serie TS 39.xxx propuesta para 3GPP. Las flechas inter-dimensionales indican dependencias funcionales clave."

---

### **Figura 2. Evolución de las Métricas de Rendimiento en Comunicaciones: De 1G a 6G**
*(Referenciada en Sección III.A, párrafo 2)*

**Descripción para generación:** Diagrama de línea de tiempo horizontal en alta resolución. Eje X: generaciones de red (1G, 2G, 3G, 4G, 5G, 6G) espaciadas uniformemente de izquierda a derecha. Para cada generación, dos filas: fila superior con las principales KPIs (métricas de rendimiento), fila inferior con la tecnología habilitadora. 1G (fondo gris claro): SNR, BER / Analógica; 2G: BER, FER / GSM, CDMA; 3G: Throughput, BER, BLER / WCDMA; 4G: Throughput, Eficiencia Espectral, Latencia / LTE, OFDMA; 5G (fondo azul claro): Throughput, Confiabilidad (99.999%), Latencia (<1 ms), Densidad / NR, mmWave; 6G (fondo verde claro): Fidelidad Semántica, TSR, Alineación de Intención, Resiliencia / IA-Nativa, Comunicaciones Semánticas. Una línea vertical punteada roja entre 5G y 6G etiquetada "Cambio de Paradigma: Sintáctico → Semántico". En la parte inferior, barra con series TS 3GPP correspondientes: TS 25.xxx → TS 36.xxx → TS 38.xxx → TS 39.xxx (propuesto), con flechas de progresión. Superpuesto como overlay semitransparente, el modelo de tres niveles de Weaver: Nivel A (sintáctico) destacado en azul para 1G–5G; Niveles B+C (semántico + efectividad) destacados en verde para 6G.

**Pie de figura:** "Fig. 2. Evolución de las métricas de rendimiento en comunicaciones inalámbricas desde 1G hasta 6G. Las generaciones 1G–5G emplean KPIs exclusivamente de Nivel A (sintáctico). La 6G introduce evaluación de Nivel B (semántico) y Nivel C (efectividad), reflejando el cambio de paradigma desde transmisión exacta de bits hacia preservación de significado e intención."

---

### **Figura 3. Relaciones Inter-Dimensionales y Compromisos entre las Cuatro Dimensiones del Marco**
*(Referenciada en Sección IV.C, párrafo 3)*

**Descripción para generación:** Diagrama en forma de rombo/diamante con cuatro nodos en los vértices. Nodo superior: "Fidelidad Semántica" (óvalo azul) con lista RSE, SWD, S³I, NSMI. Nodo derecho: "Compleción de Tarea" (óvalo verde) con lista TSR, AP, SU, CE. Nodo inferior: "Alineación de Intención" (óvalo naranja) con lista ID, ICC, SCI, PF. Nodo izquierdo: "Resiliencia" (óvalo rojo) con lista ARR, SASR, CertCost, MSD. Conexiones: (1) Flecha gruesa unidireccional de Fidelidad → Compleción con etiqueta "$\Phi$: no-inyectiva (alta fidelidad $\neq$ alto éxito de tarea)"; (2) Flecha unidireccional de Alineación de Intención → Compleción con etiqueta "necesaria pero no suficiente"; (3) Flecha bidireccional ondulada entre Fidelidad y Resiliencia etiquetada "compromiso Pareto (entrenamiento adversarial reduce fidelidad)"; (4) Flecha punteada de Alineación de Intención → Fidelidad etiquetada "prerequisito para transmisión propositiva". En el centro del rombo, un pequeño bloque etiquetado "$M_{\text{composite}}$" con las dos fórmulas de agregación (lineal ponderada y razón-min). Colores de fondo del diagrama en gris muy claro con líneas de cuadrícula finas.

**Pie de figura:** "Fig. 3. Relaciones inter-dimensionales, compromisos y dependencias funcionales entre las cuatro dimensiones de métricas del marco propuesto. La relación no-inyectiva $\Phi$ implica que alta fidelidad no garantiza alto éxito de tarea; el compromiso Pareto entre fidelidad y resiliencia exige gestión explícita en sistemas de seguridad crítica."

---

### **Figura 4. Resultados de Simulación: Métricas de Fidelidad Semántica (RSE, S³I) en Función de la Dimensión de Cuello de Botella $k$**
*(Referenciada en Sección XI.B, párrafo 2)*

**Descripción para generación:** Gráfico de líneas con doble eje Y opcional o escala unificada [0, 1]. Eje X logarítmico con valores $k \in \{8, 16, 32, 64, 128\}$ (escala log₂), etiquetados explícitamente. Eje X secundario en la parte superior mostrando ratio de compresión $\rho = k/512$: {1.56%, 3.12%, 6.25%, 12.50%, 25.00%}. Eje Y: valor de métrica [0, 1]. Dos curvas: (1) RSE — línea sólida azul gruesa con marcadores circulares (●), puntos: $k=8$: 0.058; $k=16$: 0.074; $k=32$: 0.077; $k=64$: 0.107; $k=128$: 0.105; (2) S³I — línea punteada roja gruesa con marcadores cuadrados (■), puntos: $k=8$: 0.383; $k=16$: 0.438; $k=32$: 0.481; $k=64$: 0.515; $k=128$: 0.499. Barras de error en cada punto (intervalos de confianza al 95%). Leyenda en la esquina inferior derecha. Línea vertical punteada gris en $k=32$ etiquetada "Punto de operación recomendado". Anotación de texto dentro del gráfico: "S³I satura más rápido que RSE (captura de estructura local)". Título: "Canal AWGN, SNR = 10 dB, N = 1,000 muestras Monte Carlo". Cuadrícula fina gris. Fuente: resultados de `simulate_semantic_metrics.py`, datos en `simulation_results/results_k*.npz`.

**Pie de figura:** "Fig. 4. Métricas de fidelidad semántica RSE y S³I en función de la dimensión de cuello de botella $k$, canal AWGN, SNR = 10 dB. La S³I satura a mayor velocidad que la RSE debido a su formulación de similitud estructural, alcanzando 0.481 a $k=32$ (ratio de compresión 6.25%). El eje superior indica el ratio de compresión $\rho = k/512$ correspondiente."

---

### **Figura 5. Tasa de Éxito de Tarea (TSR) vs. SNR: Comparación entre Sistema Semántico Propuesto y Línea Base Clásica**
*(Referenciada en Sección XI.C, párrafo 3)*

**Descripción para generación:** Gráfico de líneas de alta calidad. Eje X: SNR [dB] de $-5$ a $+25$ dB con paso de 2.5 dB, etiquetado explícitamente. Eje Y: TSR [0, 1], con líneas de referencia horizontales punteadas en TSR = 0.5 y TSR = 0.87. Tres curvas principales: (1) "Sistema propuesto ($k=32$)" — línea sólida azul gruesa, puntos: −5 dB: 0.236; 0 dB: 0.380; 5 dB: 0.633; 10 dB: 0.867; 15 dB: 0.983; 20 dB: 1.000; con barras de error de los intervalos de confianza Wilson 95% en cada punto; (2) "JPEG2000+LDPC (clásico)" — línea naranja punteada gruesa, modelada con función logística de efecto acantilado (cliff effect), valores: −5 dB: ~0; 0 dB: 0.017; 5 dB: 0.322; 10 dB: 0.888; 15 dB: 0.948; 20 dB: 0.950; (3) "DeepJSCC [46]" — línea verde de guiones, estimada al 96.6% del sistema propuesto. Región sombreada azul claro para SNR < 5 dB etiquetada "Zona de degradación graceful (ventaja semántica)". Anotación: flecha con texto "22× ventaja de TSR a 0 dB (0.380 vs. 0.017)" apuntando al SNR = 0 dB. Anotación en SNR = 10 dB: "TSR = 0.867 [IC 95%: 0.845–0.887]". Cuadrícula fina. Leyenda en esquina inferior derecha. Fuente: `simulation_results/results_k32.npz`.

**Pie de figura:** "Fig. 5. Tasa de Éxito de Tarea (TSR) vs. SNR para el sistema semántico propuesto ($k=32$) en comparación con JPEG2000+LDPC y DeepJSCC, canal AWGN. El sistema semántico exhibe degradación graceful para SNR < 5 dB, logrando TSR = 0.380 a 0 dB frente a TSR = 0.017 del sistema clásico (22× de ventaja). Las barras de error representan intervalos de confianza Wilson al 95%, $N = 1{,}000$ muestras por punto."

---

### **Figura 6. Arquitectura de Despliegue Distribuido en Tres Niveles para Evaluación de Métricas Semánticas en Redes 6G**
*(Referenciada en Sección X.B, párrafo 3)*

**Descripción para generación:** Diagrama arquitectónico de tres capas horizontales apiladas verticalmente, con flujo de datos ascendente. Capa inferior "Nivel 1 — Borde (UE/IoT)": fondo azul muy claro, iconos representativos de smartphone, sensor IoT, robot y vehículo autónomo alineados horizontalmente; bloques internos: "Evaluación TSR" y "S³I básico"; etiqueta de restricción: "≤100 MFLOPS, <10 ms"; formato de comunicación: "JSON ~100 B/s". Capa media "Nivel 2 — Red (gNB/MEC)": fondo verde muy claro, icono de torre de estación base y servidor MEC; bloques internos: "Suite completa de fidelidad (RSE, SWD, S³I, NSMI)" y "Divergencia de Intención (ID, ICC, SCI, PF)"; etiqueta: "1–10 TFLOPS, <100 ms"; formato: "Protobuf ~10 KB/10s". Capa superior "Nivel 3 — Núcleo (Datacenter)": fondo rojo muy claro, icono de nube/datacenter; bloques internos: "Certificación CertCost", "Optimización MSD", "Análisis longitudinal"; etiqueta: "100+ TFLOPS, segundos"; formato: "Parquet (batch)". Flechas ascendentes gruesas entre capas etiquetadas con el formato de datos. Bloque vertical a la derecha etiquetado "Integración 3GPP (TS 39.202)" con flechas horizontales a cada nivel. Dentro del Nivel 2, un sub-bloque "Función de Procesamiento Semántico (SPF)" conectado a la interfaz $N_{\text{semantic}}$ del bloque de Función del Plano de Usuario (UPF).

**Pie de figura:** "Fig. 6. Arquitectura de despliegue distribuido en tres niveles para la evaluación de métricas semánticas en redes 6G. Las métricas ligeras (TSR, S³I básico) se computan en el borde con latencia <10 ms; la suite completa de fidelidad e intención se evalúa en el nivel de red con infraestructura GPU 1–10 TFLOPS; la certificación formal de robustez se ejecuta en el núcleo con latencia del orden de segundos. La Función de Procesamiento Semántico (SPF) propuesta se integra en el Nivel 2 con interfaz $N_{\text{semantic}}$ al plano de usuario."

---

### **Figura 7. Hoja de Ruta de Estandarización 3GPP para Métricas de Comunicaciones Semánticas: Cronograma de Versiones 20–22**
*(Referenciada en Sección IX.A, párrafo 3)*

**Descripción para generación:** Diagrama de Gantt de alta resolución con tres filas horizontales de actividades. Eje X temporal de 2025 a 2028, con marcas anuales. Fila 1 (2025–2026, "Release 20"): barras de color azul para "Study Items: Definiciones Semánticas (TR)", "CR de Vocabulario (TS 21.905)", "TR de Metodología de Evaluación". Fila 2 (2026–2027, "Release 21"): barras de color verde para "TS 39.101 Aspectos Generales", "TS 39.201 Definición de Métricas", "TS 39.202 Configuración de Medición", "TS 39.521 Conformidad"; barras naranja para "CRs: TS 22.261, TS 23.501, TS 38.300, TS 38.214". Fila 3 (2027–2028, "Release 22"): barras de color morado para "Integración IA-Nativa Completa", "RRM Semántico/Adaptación de Enlace", "Gestión de Red Semántica E2E". En la parte inferior, línea de hitos etiquetados: "Identificación de brechas (2025) → Definiciones formales (2025–2026) → Métricas normativas (2026–2027) → Conformidad (2027) → Integración completa (2028)". Flecha punteada desde "TR 38.843 [59]" (marcado en 2023) hacia "Study Items Release 20" etiquetada "Plantilla procedimental". Leyenda de colores: azul=Study Items, verde=Work Items/TS, naranja=Change Requests, morado=Integración. Cuadrícula vertical anual.

**Pie de figura:** "Fig. 7. Hoja de ruta de estandarización 3GPP para métricas de comunicaciones semánticas, con cronograma previsto para las Versiones 20–22 (2025–2028). La Release 20 establece fundamentos en Study Items; la Release 21 produce las especificaciones normativas TS 39.xxx y Change Requests a especificaciones existentes; la Release 22 integra las métricas en la gestión completa de la red IA-nativa. La flecha indica la plantilla procedimental derivada de la experiencia con TR 38.843."

---

### **Figura 8. Tasa de Éxito de Ataque Semántico (SASR) vs. Presupuesto Adversarial ($\varepsilon$)**
*(Referenciada en Sección VIII.B, párrafo 3)*

**Descripción para generación:** Gráfico de líneas. Eje X: presupuesto adversarial $\varepsilon$ (norma $\ell_\infty$ normalizada), rango [0, 0.30] con etiquetas en 0, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30. Eje Y: SASR [0, 1]. Cuatro curvas: (1) "Sistema propuesto (entrenamiento adversarial + suavizado)" — línea sólida azul gruesa, crecimiento lento: SASR = 0 en $\varepsilon = 0$; SASR = 0.30 en $\varepsilon = 8/255 \approx 0.031$; SASR = 0.50 en $\varepsilon \approx 0.15$ ($\varepsilon_{\text{threshold}}$); SASR = 0.80 en $\varepsilon \approx 0.25$; (2) "DeepJSCC (entrenamiento estándar)" — línea verde punteada, crecimiento moderado: SASR = 0.50 en $\varepsilon \approx 0.08$; (3) "JPEG2000+LDPC" — línea naranja de guiones, crecimiento rápido: SASR = 0.50 en $\varepsilon \approx 0.02$; (4) "Transmisión bit-exacta" — línea gris puntogión, colapso inmediato: SASR = 0.50 en $\varepsilon < 0.01$. Línea horizontal punteada roja en SASR = 0.5 etiquetada "$\varepsilon_{\text{threshold}}$". Línea vertical punteada gris en $\varepsilon = 8/255 = 0.031$ etiquetada "Caso de Prueba 3 (PGD, $\varepsilon = 8/255$)". Región sombreada verde claro para SASR < 0.3 debajo de la curva del sistema propuesto, etiquetada "Zona de robustez aceptable (criterio Caso de Prueba 3: SASR ≤ 0.30)". Leyenda en esquina inferior derecha.

**Pie de figura:** "Fig. 8. Tasa de Éxito de Ataque Semántico (SASR) vs. presupuesto adversarial $\varepsilon$ (norma $\ell_\infty$) para el sistema propuesto y tres líneas base. El umbral de robustez $\varepsilon_{\text{threshold}}$ (SASR = 0.5) del sistema propuesto (0.15) es aproximadamente 2× mayor que el de DeepJSCC (0.08) y 7.5× mayor que el de JPEG2000+LDPC (0.02). La línea vertical en $\varepsilon = 8/255$ corresponde al presupuesto del Caso de Prueba 3."

---

## IV. VERIFICACIÓN DE EXPRESIONES MATEMÁTICAS EN FORMATO LaTeX

Todas las expresiones matemáticas del artículo están correctamente formateadas en LaTeX. No se detectan ecuaciones en texto plano. Sin embargo, se identifican los siguientes aspectos que deben corregirse o verificarse en el documento final:

1. **Consistencia de notación en SCI (Sección VII.C):** La fórmula de $SCI_w$ utiliza $w_i w_j$ como pesos sin normalización explícita en el denominador de la suma interna. Debería verificarse si la normalización $\sum_{i,j} w_i w_j$ es consistente con la definición de $D(\mathcal{I}_i, \mathcal{I}_j)$ (que puede o no estar ya normalizada).

2. **Demostración del Teorema 3 (Cota de Consenso):** La afirmación "$D(\mathcal{I}_i, \mathcal{I}_\mathcal{T}) \leq e^{-C_{s,i}}$" es presentada sin referencia a una teoría específica. Esta desigualdad requiere una cita o derivación más explícita, ya que no sigue directamente de la desigualdad de Fano estándar.

3. **Ecuación de CertCost en Algorithm 15 vs. el script:** En Algorithm 15, el radio certificado se computa como $r = \sigma \cdot \Phi^{-1}(\underline{p}_A)$ (una entrada de la función $\Phi^{-1}$), mientras que en el Teorema 4 se define como $r = \frac{\sigma}{2}(\Phi^{-1}(p_c) - \Phi^{-1}(p_2))$ (dos entradas). Estas fórmulas son distintas. Algorithm 15 implementa la versión de un solo umbral (basada en probabilidad de clase mayoritaria solamente), mientras que Theorem 4 usa la brecha entre la clase mayoritaria y la segunda. Deben ser consistentes.

4. **Formula de CE en el script:** `metric_CE` normaliza CE dividiendo por 20 (`return float(np.clip(tsr / (k / d) / 20, 0, 1))`), pero la definición formal de CE en el artículo es $CE = TSR / \text{Transmitted Information Rate}$ sin factor de normalización de 20. Este factor es ad hoc y no está documentado en el artículo. Debe incorporarse la justificación de la normalización o alinearse la implementación con la definición formal.

---

## V. ESTADO DEL ARTE Y RECOMENDACIONES DE EXPLORACIÓN ADICIONAL

### V.1 Trabajos relacionados que deben discutirse más ampliamente

El estado del arte es razonablemente comprehensivo pero presenta las siguientes omisiones o tratamientos insuficientes:

1. **Rate-Splitting Multiple Access (RSMA) para comunicaciones semánticas:** Trabajos recientes demuestran que RSMA puede mejorar significativamente las métricas semánticas en sistemas multiusuario. Su omisión en la discusión de sistemas multi-usuario (Sección VII.C) es notable.

2. **Comunicaciones semánticas para señales de control y robótica:** El artículo cita casos de uso robóticos pero no discute frameworks específicos de métricas para control de sistemas físicos (cyber-physical systems), donde la latencia semántica y la acción de precisión tienen implicaciones de seguridad directas.

3. **Métricas basadas en Age of Information (AoI) y Value of Information (VoI):** Estos frameworks, bien establecidos en la literatura de comunicaciones orientadas a tareas, tienen relación directa con las métricas SU (Utilidad Semántica) y CE (Eficiencia de Compleción) propuestas. La conexión con AoI/VoI no se discute y debería establecerse explícitamente para posicionar el trabajo en el contexto más amplio.

4. **Comunicaciones semánticas multimodales:** Con la proliferación de modelos LLM multimodales, las métricas de coherencia semántica inter-modal (texto-imagen, audio-video) son una extensión natural del framework. La Sección XII.F menciona LLMs pero no discute específicamente métricas multi-modal.

5. **Semantic channel coding con garantías de Shannon:** La conexión entre la capacidad del canal semántico $C_s(\mathcal{T})$ definida en la Sección II.B y resultados empíricos de compresión debe desarrollarse más. Actualmente, la capacidad semántica se define pero no se estima ni se usa en la comparación experimental.

### V.2 Simulaciones adicionales recomendadas

Se recomienda incorporar las siguientes simulaciones para fortalecer las contribuciones del artículo:

1. **Validación con datos reales (CIFAR-10 o ImageNet):** Reemplazar o complementar las Gaussianas sintéticas con embeddings reales de CLIP para validar los resultados de TSR y RSE en condiciones más realistas. Incluso una evaluación parcial con 1,000 embeddings reales sería suficiente para fortalecer la credibilidad.

2. **Curvas de TSR vs. k para múltiples canales:** El artículo presenta curvas de fidelidad vs. k (Fig. 4) solo para AWGN. Sería valioso mostrar cómo la degradación bajo Rayleigh y TDL-A interactúa con la dimensión de compresión.

3. **Análisis de robustez completo para canales no-AWGN:** Como se señaló en el Problema M3, los valores de ARR/SASR para canales distintos de AWGN están imputados, no calculados. Debe realizarse la simulación completa de PGD para al menos un canal adicional (Rayleigh).

4. **Comparación directa de la métrica ID con el proceso real de inferencia de intención:** La métrica ID se define como divergencia KL sobre distribuciones de intención, pero en la simulación se computa sobre el promedio absoluto de embeddings. Una simulación con un modelo de inferencia de intención explícito (p.ej., clasificador de intención) produciría resultados más creíbles.

5. **Evaluación de CertCost normalizada (FLOPs en lugar de segundos):** El tiempo de pared no es reproducible entre hardware. Se recomienda reportar CertCost en FLOPs de modelo, que sí es reproducible y comparable entre sistemas.

---

## VI. CORRECCIONES MENORES ADICIONALES

1. **Referencia [71]:** El volumen citado (vol. 72) para IEEE Transactions on Wireless Communications no es coherente con el historial de publicación de esa revista. Debe corregirse.

2. **Referencia [74]:** Completar con DOI, volumen y páginas de la publicación en IEEE Communications Magazine 2024.

3. **Tabla IV:** La ARR reportada (0.045) es inconsistente con el valor 0.15 discutido en el texto (Sección XI.E y Fig. 8). Debe corregirse.

4. **Abstract:** Corregir "60–80% transmission overhead reduction" por el valor real demostrado ("hasta 93.75% de reducción de overhead, con una reducción conservadora efectiva estimada en 60–80% teniendo en cuenta señalización y metadatos").

5. **Abstract:** Añadir condición de canal: "task effectiveness above 87% under AWGN conditions at SNR ≥ 10 dB."

6. **Numeración de Tablas:** Reordenar la aparición de la Tabla IV para que aparezca en el orden natural (debe ser la primera tabla del análisis numérico, no la quinta en ser referenciada).

7. **Sección XI.E:** Cambiar "Simulation-Based Performance Comparison" a posición anterior (XI.A o XI.B) para que sirva como referencia antes de discutir fidelidad y multi-canal.

8. **Pie de figura de Fig. 8:** El texto del artículo describe valores de ARR = 0.15 para el sistema propuesto, pero la Tabla IV reporta ARR = 0.045. Esta inconsistencia debe resolverse unificando los valores o explicando la diferencia metodológica.

9. **Sección XI.B:** Los valores de RSE en la tabla (0.058–0.107) son sorprendentemente bajos e indican que el estimador solo captura el 5–10% de la información semántica disponible. Debe añadirse una nota de explicación o revisarse el estimador de entropía semántica.

10. **Sección X.C (Calibración y Reproducibilidad):** La lista de metadatos de proveniencia es valiosa pero excesivamente detallada para el cuerpo principal del artículo. Se recomienda moverla al Apéndice.

---

## VII. RESUMEN DE CALIFICACIONES

| Criterio | Calificación (1–5) | Observación |
|----------|-------------------|-------------|
| Originalidad | 3.5 / 5 | Buena, limitada por solapamiento con [70] |
| Rigor matemático | 4.0 / 5 | Sólido; inconsistencias en CertCost y ARR |
| Calidad experimental | 2.5 / 5 | Datos sintéticos, valores imputados en resiliencia |
| Estado del arte | 3.5 / 5 | Comprehensivo; falta AoI/VoI, RSMA, datos reales |
| Presentación | 2.5 / 5 | Figuras ausentes; inconsistencias |
| Impacto potencial | 4.0 / 5 | Alto; tema muy relevante |
| Adecuación al journal | 4.0 / 5 | Buen ajuste con IEEE Wireless Commun. |
| Reproducibilidad | 3.0 / 5 | Scripts presentes; datos sintéticos limitan alcance |
| Coherencia de citas | 3.5 / 5 | Mayoría verificables; errores puntuales |
| **TOTAL PONDERADO** | **3.4 / 5** | **Revisión mayor recomendada** |

---

## VIII. RECOMENDACIÓN EDITORIAL

**DECISIÓN RECOMENDADA: REVISIÓN MAYOR (Major Revision)**

El artículo tiene una contribución técnica sólida y es relevante para IEEE Wireless Communications. Sin embargo, no puede aceptarse en su estado actual por las siguientes razones críticas que deben ser corregidas:

### Correcciones obligatorias (Major):

1. **Generar e insertar todas las Figuras 1–8** según las especificaciones descriptivas del artículo y las detalladas en este informe (Sección III).
2. **Resolver la inconsistencia ARR 0.045 vs. 0.15** entre la Tabla IV y el texto/Fig. 8.
3. **Corregir los valores de resiliencia imputados** para canales no-AWGN (Tabla V) mediante simulación real de PGD, o documentar explícitamente que son estimaciones analíticas y no resultados de simulación.
4. **Diferenciar explícitamente** el trabajo de la referencia [70] (Qin et al., 2024) con una tabla de comparación directa de características y métricas propuestas vs. propuestas en [70].
5. **Corregir la referencia [71]** (volumen incorrecto para IEEE TWC).
6. **Completar referencias incompletas** [28], [29], [54], [69], [74] con información de publicación definitiva.
7. **Alinear la Ecuación de CertCost** en Algorithm 15 con el Teorema 4.
8. **Corregir el abstract** para reflejar la reducción de overhead real (93.75%) y especificar condiciones de canal para TSR > 87%.

### Correcciones recomendadas (Minor):

9. Añadir validación con embeddings reales (CLIP/CIFAR-10) aunque sea parcial.
10. Reportar intervalos de confianza para todas las métricas, no solo TSR.
11. Incorporar discusión de AoI/VoI y su relación con SU y CE.
12. Añadir citas faltantes identificadas en la Sección V.1.
13. Justificar el factor de normalización ×20 en `metric_CE`.
14. Reestructurar Sección XI para orden lógico (comparación base → fidelidad → multi-canal → análisis de rendimiento).

---

*Informe generado por agente de evaluación científica especializado. Evaluación basada en lectura completa del manuscrito, scripts de simulación y resultados disponibles. Las verificaciones de DOI son indicativas y deben confirmarse manualmente para las referencias más recientes (2024).*
