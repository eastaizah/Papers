# INFORME DE EVALUACIÓN PARA PUBLICACIÓN EN IEEE WIRELESS COMMUNICATIONS (Q1)

**Artículo:** UMRO-5G: A Unified Framework for Management and Resource Orchestration in AI-Native 5G and Beyond Networks  
**Autores:** Evelio Astaiza Hoyos, Héctor Fabio Bermúdez-Orozco, Nasly Cristina Rodriguez-Idrobo (Universidad del Quindío, Colombia)  
**Evaluador:** Editor Académico Experto — Redes Inalámbricas e Inteligencia Artificial  
**Fecha:** Mayo 2026  
**Journal Objetivo:** IEEE Wireless Communications (Q1, Factor de Impacto ~12.7)  
**Decisión Preliminar:** **Major Revision**

---

## RESUMEN EJECUTIVO

El artículo presenta UMRO-5G, un marco jerárquico de cuatro capas para la gestión y orquestación de recursos en redes 5G con proyección hacia 6G. La propuesta integra Infrastructure, Virtualization & Slicing, Intelligence y Orchestration con tres lazos de control anidados (Fast <10 ms, Medium 10 ms–1 s, Slow >1 s), acompañados de una formulación matemática de optimización cruzada con descomposición Lagrangiana (Ecuaciones F1–F16). El artículo también ofrece una taxonomía de cinco dimensiones que clasifica 28 técnicas de gestión de recursos, y un conjunto de simulaciones numéricas de validación. El alcance temático —que abarca RRM, NFV/SDN, network slicing, O-RAN, ML/DRL y desafíos hacia 6G— es coherente con el alcance de IEEE Wireless Communications.

Sin embargo, el artículo tiene una extensión aproximada de 15,000–18,000 palabras con 18+16 ecuaciones, siete figuras y tres tablas extensas, lo que excede significativamente el formato habitual de IEEE Wireless Communications (4,500 palabras para artículos de revista; hasta 7,000 palabras para artículos tutorial). Esta incompatibilidad de formato es la primera corrección mayor que los autores deben abordar. Adicionalmente, se detectan inconsistencias críticas entre las afirmaciones numéricas del texto (valores en Mbps) y los scripts de simulación (unidades en bps/Hz × PRBs), discrepancias en el número de iteraciones Monte Carlo declaradas (texto: 1,000; script: 200), y la ausencia de la figura arquitectónica principal (Fig. 1 del marco UMRO-5G referenciada en la Sección VI.B pero no presente en el directorio de figuras).

En términos de contribución científica, UMRO-5G aporta una síntesis coherente y matemáticamente estructurada de dominios que raramente se integran en un solo trabajo. La taxonomía 5D es el elemento de mayor originalidad, junto con la formulación unificada F1–F16. No obstante, la novedad incremental respecto a trabajos como Polese et al. [11] debe articularse con mayor precisión, y las simulaciones deben corregirse para garantizar coherencia interna antes de la publicación. Con las revisiones solicitadas, el artículo tendría potencial de impacto en la comunidad de gestión de redes inalámbricas.

La decisión es **Major Revision**. Los autores deben: (1) adaptar el artículo al formato de IEEE Wireless Communications o redirigirlo a IEEE Communications Surveys & Tutorials; (2) corregir las inconsistencias de unidades en las simulaciones; (3) incorporar la figura de arquitectura del sistema; (4) numerar la ecuación de recompensa; y (5) actualizar el estado del arte con referencias recientes sobre gemelos digitales de red, ISAC, y LLMs para gestión autónoma.

---

## 1. EVALUACIÓN DESDE LA PERSPECTIVA DEL EDITOR DE LA REVISTA

### 1.1 Impacto, Originalidad y Encaje con IEEE Wireless Communications

**Encaje temático:** El artículo aborda la gestión y orquestación de recursos en redes 5G con proyección 6G, integrando O-RAN, NFV, DRL y network slicing. Estos temas son de máxima relevancia para IEEE Wireless Communications, que publicó recientemente artículos de alta citación sobre O-RAN (Polese et al. 2023 [11], ~400 citas), deep reinforcement learning para RRM, y arquitecturas AI-native. El encaje temático es correcto.

**Originalidad:** La originalidad del trabajo reside principalmente en tres elementos: (i) el marco unificado UMRO-5G que integra formalmente cuatro dominios técnicos bajo una formulación matemática única; (ii) la taxonomía de cinco dimensiones (5D) que clasifica 28 técnicas con granularidad superior a clasificaciones previas; y (iii) el mapeo explícito de técnicas a capas y lazos de control. Sin embargo, cada componente individual —la descomposición Lagrangiana jerárquica, los lazos de control multi-escala, la arquitectura de cuatro capas— está bien documentado en la literatura. La originalidad es de carácter integrador, no disruptivo, lo cual es aceptable para IEEE WC siempre que el trabajo sea presentado como survey/tutorial y no como investigación experimental primaria.

**Potencial de impacto:** Si se adapta correctamente al formato de IEEE WC y se corrigen las inconsistencias identificadas, el artículo tiene potencial de convertirse en una referencia citada para investigadores que busquen una visión unificada de la gestión de redes 5G/6G. La Tabla I (comparativa con surveys previos), la Tabla II (mapeo UMRO-5G) y la Tabla III (taxonomía 5D) son activos de alto valor de citación.

**Presentación internacional:** El artículo está escrito en inglés técnico correcto, con terminología estándar del ecosistema 3GPP/ETSI/O-RAN. La presentación es profesional y apropiada para una audiencia internacional de ingenieros de telecomunicaciones e investigadores de IA aplicada a redes.

### 1.2 Tipo de Artículo y Alcance

Este es un punto crítico. El artículo está clasificado por los autores como "Research Article — IEEE Transactions Format" en el encabezado de metadatos, pero su contenido es fundamentalmente un **survey/tutorial** con contribuciones de framework y simulaciones. Esta distinción tiene implicaciones directas para el journal objetivo:

- **IEEE Wireless Communications** publica artículos de tipo *magazine* con orientación tutorial/perspectiva, típicamente de **4,000–5,000 palabras** con no más de 4–6 figuras. Los artículos de investigación original van a IEEE Transactions on Wireless Communications o IEEE JSAC.
- **IEEE Communications Surveys & Tutorials** (también Q1, IF ~35) es el destino natural para un survey de esta envergadura, con límites de longitud más amplios (20,000+ palabras permitidas).
- **IEEE Transactions on Network and Service Management** sería adecuado para el componente de framework con validación experimental.

**Recomendación de formato:** Los autores deben decidir entre dos trayectorias:
1. **Ruta A (IEEE WC Magazine):** Condensar el artículo a ~4,500 palabras, enfocándose en el marco UMRO-5G y la taxonomía 5D como contribuciones principales, moviendo los detalles matemáticos a un apéndice electrónico o material suplementario. Mantener solo 4–5 figuras clave.
2. **Ruta B (IEEE Comms. Surveys & Tutorials):** Expandir el estado del arte, añadir las referencias faltantes identificadas en la Sección 3.2, y presentar el trabajo como un survey comprehensivo con validación. Esta ruta requiere mayor trabajo pero produciría el mayor impacto en términos de citaciones.

### 1.3 Potencial de Citación y Relevancia Temporal

El contenido es **temporalmente relevante**: la Tabla I cita el reporte de Ericsson Mobility 2023 [2], estándares 3GPP Release 17 [12][19] y especificaciones O-RAN 2023 [22]. La proyección hacia 6G con RIS, NTN, comunicaciones semánticas y ZSM (Secciones IX.E–IX.J) es apropiada para el horizonte 2026–2030. Sin embargo, la ausencia de referencias a trabajos sobre gemelos digitales de red (2022–2025), comunicaciones ISAC, y uso de Large Language Models (LLMs) para gestión inteligente de redes puede reducir la percepción de exhaustividad del estado del arte.

El potencial de citación se estima en **alto** (50–150 citas en 3 años) si el artículo se publica en IEEE WC con las correcciones solicitadas, y **muy alto** (200+ citas) si se redirige a IEEE Comms. Surveys & Tutorials con ampliación del estado del arte.

---

## 2. EVALUACIÓN DESDE LA PERSPECTIVA DEL INVESTIGADOR EXPERTO

### 2.1 Solidez y Reproducibilidad de los Métodos

**Formulación matemática:** Las ecuaciones 1–18 del cuerpo principal son correctas y bien derivadas. La ecuación (2) de Polyanskiy-Poor-Verdú para finite blocklength URLLC, la formulación MINLP de la Ecuación (4)–(5), la solución water-filling de la Ecuación (6), y las formulaciones de network slicing (Ecuaciones 9–11) son estándares en la literatura y están correctamente presentadas.

Las Ecuaciones F1–F16 del marco UMRO-5G son internamente consistentes. La descomposición Lagrangiana de F16 es matemáticamente válida bajo las condiciones declaradas (convergencia garantizada con paso decreciente). La función de utilidad F2 captura apropiadamente los trade-offs entre throughput eMBB, latencia URLLC y conectividad mMTC.

**Reproducibilidad:** Los scripts de simulación están disponibles (Python, NumPy, Matplotlib) con semillas fijas (SEEDS = [42, 123, 256, 789, 1024]). Esto es positivo. Sin embargo, existen tres problemas de reproducibilidad:

1. **Discrepancia N_MONTE_CARLO:** El texto de la Sección VIII.B declara "1,000 Monte Carlo iterations" pero el script `sim_multi_slice.py` define `N_MONTE_CARLO = 200`. Esta inconsistencia debe ser resuelta —o el texto debe corregirse a 200, o el script debe ser actualizado a 1,000 con tiempo de cómputo suficiente.

2. **Modelos proxy DRL:** La simulación de convergencia DRL en `sim_drl_convergence.py` utiliza proxies tabulares simplificados en lugar de redes neuronales reales (DQN con capas densas, QMIX con mixing network). Los resultados de convergencia presentados en la Sección VIII.C no corresponden a experimentos reales de DRL sino a curvas generadas por modelos aproximados. Esto debe declararse explícitamente como "ilustración conceptual" o debe implementarse con frameworks reales (PyTorch/TensorFlow).

3. **Ausencia de código para figura de arquitectura:** La Figura 1 (diagrama de arquitectura UMRO-5G) es referenciada en la Sección VI.B ("The UMRO-5G architecture comprises four functional layers (Fig. 1)") pero no existe en el directorio de figuras. Esta es una omisión crítica.

### 2.2 Robustez de los Datos y Validación Experimental

**Monte Carlo con N=200, 5 semillas:** Para las simulaciones de asignación multi-slice (Sección VIII.B), N=200 iteraciones con 5 semillas independientes proporciona 1,000 realizaciones totales, lo cual es estadísticamente suficiente para estimar medias y desviaciones estándar con intervalos de confianza del 95%. Sin embargo, el texto afirma 1,000 iteraciones por configuración, no 200.

**Modelo de eficiencia espectral simplificado:** El script usa valores fijos de eficiencia espectral (SPEC_EFF = [4.0, 1.5, 0.5] bps/Hz/PRB para eMBB, URLLC, mMTC). Esta es una simplificación significativa: en sistemas 5G NR reales, la eficiencia espectral varía entre 0.1 y 7.8 bps/Hz dependiendo del CQI, la relación señal-ruido, y el esquema MCS. El modelo no incorpora la fórmula de Shannon ni los efectos del desvanecimiento de canal. Los autores deben declarar explícitamente que el modelo de eficiencia espectral es una aproximación de primer orden para ilustrar el comportamiento cualitativo del framework.

**Validez del modelo M/M/1 para SFC:** La validación del modelo M/M/1 de Jackson contra simulación de eventos discretos (DES) es metodológicamente sólida. La concordancia dentro del 5% para cargas inferiores al 80% de la capacidad del cuello de botella es un resultado estándar y correctamente interpretado.

### 2.3 Corrección de Resultados y Análisis Estadístico

#### INCONSISTENCIA CRÍTICA DE UNIDADES

Este es el problema más grave detectado en el análisis de las simulaciones:

El script `sim_multi_slice.py` calcula el throughput como:
```python
def compute_throughput(alloc):
    return alloc * SPEC_EFF  # alloc en PRBs, SPEC_EFF en bps/Hz
```

El resultado es `throughput = PRBs_asignados × bps/Hz`, que tiene dimensiones de **bps/Hz** (o equivalentemente, bps por Hz de ancho de banda de subportadora), **no Mbps**. Con TOTAL_PRBS = 100 y SPEC_EFF = [4.0, 1.5, 0.5], el throughput máximo posible para el slice eMBB es 50 PRBs × 4.0 bps/Hz = **200 bps/Hz** en notación adimensional.

Sin embargo, el texto de la Sección VIII.B afirma: *"At ρ=0.9, Hard Isolation achieves approximately 450 Mbps aggregate throughput, Soft Isolation achieves 510 Mbps, and UMRO-5G achieves 550 Mbps."* Estos valores en Mbps requerirían multiplicar por el ancho de banda de subportadora en Hz, pero el script nunca realiza esta conversión.

**La disparidad es inaceptable para publicación.** Los autores tienen tres opciones:
- **Opción A:** Corregir el texto para que indique las unidades correctas (bps/Hz normalizado por PRB, o simplemente "unidades normalizadas").
- **Opción B:** Actualizar el script para incluir la conversión al ancho de banda real de la subportadora 5G NR (15 kHz × 12 subportadoras = 180 kHz por PRB, o usar el ancho de banda total del canal dividido entre N_PRB).
- **Opción C (recomendada):** Reformular la simulación usando parámetros 5G NR reales: ancho de banda de canal B = 20 MHz, N_PRB = 100 PRBs con Δf = 15 kHz (numerología μ=0, SCS=15 kHz, 12 subportadoras/PRB → ancho de banda por PRB = 180 kHz), de modo que Throughput_eMBB = 50 PRBs × 180 kHz/PRB × 4.0 bps/Hz = 36 Mbps por slot de 1 ms, escalable a los valores típicos de 5G.

**Análisis estadístico:** Los resultados de las figuras presentan bandas de confianza (mean ± std), lo cual es positivo. Sin embargo, el artículo no reporta intervalos de confianza formales (p.ej., IC del 95% via bootstrap) ni tests de significancia estadística para comparar los tres esquemas de asignación. Para una publicación Q1, se recomienda añadir al menos pruebas t-test pareadas o ANOVA para las comparaciones de throughput entre Hard/Soft/UMRO-5G.

### 2.4 Coherencia entre Resultados y Conclusiones

Las conclusiones de la Sección X son coherentes cualitativamente con los resultados presentados. Las afirmaciones sobre "15–25% higher throughput than static hard isolation" y "URLLC violation probability below 1.5%" son consistentes con las figuras generadas. La afirmación sobre "GNN-DRL achieves approximately 95% of theoretical optimum" es consistente con la figura de convergencia.

Sin embargo, dado que las simulaciones DRL no utilizan redes neuronales reales (ver Sección 2.1), las conclusiones sobre la velocidad de convergencia de los algoritmos (DQN ~500 episodios, Fed-DQN ~1,800 episodios) deben matizarse indicando que son estimaciones basadas en modelos proxy y no en implementaciones reales de los algoritmos citados [25][26][27].

### 2.5 Estado del Arte y Citaciones Relevantes

El estado del arte cubre adecuadamente los trabajos fundacionales en NFV (Mijumbi [7]), network slicing (Foukas [9], Afolabi [10]), O-RAN (Polese [11], Bonati [23]), DRL (Mnih [25]), MARL (Rashid [26]), FL (McMahan [27]) y GNN (Eisen [28]). La Tabla I es una contribución útil para posicionar el artículo.

No obstante, existen ausencias notables en el estado del arte (ver también Sección 3.2):

1. **Gemelos Digitales de Red:** No se citan trabajos recientes de 2022–2024 sobre Network Digital Twins en 5G/6G, a pesar de que la Sección IX.G los identifica como desafío abierto.
2. **ISAC (Integrated Sensing and Communications):** Mencionado brevemente en la Sección IX.K pero sin referencias específicas sobre optimización conjunta de recursos radar-comunicaciones.
3. **Large Language Models para gestión de redes:** Trabajos de 2023–2024 sobre uso de GPT/LLMs para configuración inteligente y troubleshooting de redes 5G/6G están completamente ausentes.
4. **RIS en sistemas URLLC:** Existen trabajos recientes sobre optimización de RIS bajo restricciones URLLC que deben citarse dado que la Sección IX.E aborda este tema.
5. **Fundamentos de comunicaciones semánticas:** La Sección IX.I menciona comunicaciones semánticas sin citar los trabajos seminales de Farsad et al. (2018) o Xie et al. (2021).

### 2.6 Calidad de Escritura y Flujo del Artículo

El artículo está bien escrito en inglés técnico estándar. La estructura sigue un flujo lógico: motivación → fundamentos → NFV/SDN → O-RAN → ML/DRL → framework → taxonomía → simulaciones → desafíos → conclusiones. El abstract es completo e incluye las contribuciones C1–C4.

**Observaciones de estilo:**
- La Sección IX tiene 10 subsecciones (A–J más una K adicional sobre Evolución 6G), lo que indica que esta sección fue expandida más allá del plan declarado. El artículo original declara "10 subsections" pero contiene 11.
- Algunos párrafos son excesivamente largos (>200 palabras), en particular en las Secciones VI.G y VII.H, lo cual dificulta la lectura en formato magazine.
- La presentación de la Tabla III podría beneficiarse de columnas adicionales indicando el nivel de madurez TRL (Technology Readiness Level) de cada técnica, lo cual aumentaría el valor informativo para lectores industriales.

### 2.7 Contribución al Conocimiento del Campo

La contribución principal de UMRO-5G al conocimiento del campo es la **integración formal** de seis dominios técnicos previamente tratados de forma aislada en la literatura. La formulación unificada F1–F16 con descomposición jerárquica es el aporte matemático más original, aunque su novedad es modesta en comparación con trabajos de optimización de recursos multi-dominio publicados en IEEE JSAC y IEEE TWC en 2022–2024.

La taxonomía 5D es el aporte más diferenciador respecto a surveys previos. Las dimensiones "Architectural Scope" y "Virtualization Level" no suelen considerarse en clasificaciones existentes, y su combinación con las tres dimensiones más comunes (Resource Domain, Timescale, Optimization Approach) ofrece un mapa de coordenadas útil para navegar la literatura.

La propuesta de **interfaces formales** (I₁₂, I₂₃, I₃₄) entre capas es prácticamente valiosa porque especifica los flujos de datos entre el RIC y el stack MANO, un aspecto que estudios previos como Polese et al. [11] describen cualitativamente pero no formalizan. Esta contribución debería destacarse más prominentemente en el abstract y en las conclusiones.

---

## 3. VERIFICACIÓN DE CONSISTENCIA Y COHERENCIA DE LAS CITAS

### 3.1 Análisis de Referencias [1]–[29]

| Ref | Autores | Año | Fuente | DOI disponible | Uso en artículo | Observación |
|:---|:---|:---:|:---|:---:|:---|:---|
| [1] | Andrews et al. | 2014 | IEEE JSAC vol.32 no.6 pp.1065–1082 | ✓ (10.1109/JSAC.2014.2328098) | Motivación, paradigma 5G | Correctamente citado; trabajo seminal |
| [2] | Ericsson | 2023 | Ericsson Mobility Report, Nov. 2023 | ✗ (URL requerida) | Proyección de tráfico 1000× | Falta URL; informes técnicos de Ericsson están disponibles en ericsson.com; añadir URL acceso |
| [3] | ITU-R | 2017 | Rep. ITU-R M.2410-0 | ✗ (acceso libre ITU) | Requisitos IMT-2020 | Estándar; sin DOI comercial; añadir URL ITU-R |
| [4] | Osseiran et al. | 2014 | IEEE Commun. Mag. vol.52 no.5 pp.26–35 | ✓ (10.1109/MCOM.2014.6815890) | Escenarios 5G | Uso correcto |
| [5] | Rappaport et al. | 2013 | IEEE Access vol.1 pp.335–349 | ✓ (10.1109/ACCESS.2013.2260813) | Expansión espectral mmWave | Uso correcto; trabajo seminal mmWave |
| [6] | Larsson et al. | 2014 | IEEE Commun. Mag. vol.52 no.2 pp.186–195 | ✓ (10.1109/MCOM.2014.6736761) | Massive MIMO | Uso correcto |
| [7] | Mijumbi et al. | 2016 | IEEE Commun. Surveys Tuts. vol.18 no.1 pp.236–262 | ✓ (10.1109/COMST.2015.2477041) | NFV/MANO; referencia de comparación Table I | Correctamente citado como referencia base |
| [8] | Popovski et al. | 2018 | IEEE Access vol.6 pp.55765–55779 | ✓ (10.1109/ACCESS.2018.2872781) | Slicing eMBB/URLLC/mMTC | Uso correcto y relevante |
| [9] | Foukas et al. | 2017 | IEEE Commun. Mag. vol.55 no.5 pp.94–100 | ✓ (10.1109/MCOM.2017.1600951) | Network slicing; Tabla I | Uso correcto |
| [10] | Afolabi et al. | 2018 | IEEE Commun. Surveys Tuts. vol.20 no.3 pp.2429–2453 | ✓ (10.1109/COMST.2018.2835696) | Network slicing; Tabla I | Correctamente citado |
| [11] | Polese et al. | 2023 | IEEE Commun. Surveys Tuts. vol.25 no.2 pp.1376–1411 | ✓ (10.1109/COMST.2023.3239220) | O-RAN; Tabla I | Referencia central y muy relevante; verificar número de páginas exacto |
| [12] | 3GPP | 2022 | TS 38.214 V17.3.0 | ✗ (portal 3GPP) | MAC scheduler 5G NR | Estándar técnico; añadir URL 3GPP portal |
| [13] | Polyanskiy et al. | 2010 | IEEE Trans. Inf. Theory vol.56 no.5 pp.2307–2359 | ✓ (10.1109/TIT.2010.2043769) | URLLC finite blocklength (Ec. 2) | Uso correcto; trabajo seminal FBL |
| [14] | Cover & Thomas | 2006 | Libro: Wiley, 2nd ed. | ✗ (libro) | Water-filling (Ec. 6) | Referencia estándar; sin DOI por ser libro; ISBN 978-0-471-24195-9 |
| [15] | ETSI | 2014 | GS NFV-MAN 001 V1.1.1 | ✗ (portal ETSI) | NFV MANO framework | Estándar; añadir URL ETSI portal |
| [16] | Herrera & Botero | 2016 | IEEE Trans. Netw. Serv. Manag. vol.13 no.3 pp.518–532 | ✓ (10.1109/TNSM.2016.2598420) | VNF placement NP-complete | Uso correcto |
| [17] | Garey & Johnson | 1979 | Libro: W.H. Freeman | ✗ (libro clásico) | NP-completitud | Referencia estándar de complejidad; correctamente citado |
| [18] | Quinn & Nadeau | 2015 | RFC 7498, IETF | ✗ (RFC IETF) | Service Function Chaining | RFC accesible en tools.ietf.org; añadir URL |
| [19] | 3GPP | 2022 | TS 28.530 V17.2.0 | ✗ (portal 3GPP) | Gestión de slices | Estándar técnico; añadir URL |
| [20] | Bertsekas | 2016 | Libro: Athena Scientific, 3rd ed. | ✗ (libro) | Lagrangian decomposition (Ec. 11, F16) | ISBN 978-1-886529-05-2; sin DOI |
| [21] | Nandagopal et al. | 2000 | Proc. ACM MobiCom pp.87–98 | ✓ (10.1145/345910.345925) | PF scheduler (Ec. 12) | Uso correcto; verificar que el DOI sea correcto para MobiCom 2000 |
| [22] | O-RAN Alliance | 2023 | O-RAN.WG1.O-RAN-Architecture-Description-v07.00 | ✗ (portal O-RAN) | Arquitectura O-RAN | Añadir URL de O-RAN Alliance; documento público |
| [23] | Bonati et al. | 2020 | Computer Networks vol.182 p.107516 | ✓ (10.1016/j.comnet.2020.107516) | xApps O-RAN | Correctamente citado |
| [24] | Sutton & Barto | 2018 | Libro: MIT Press, 2nd ed. | ✗ (libro) | MDP/RL fundamentals | Referencia estándar; disponible en http://incompleteideas.net/book/the-book-2nd.html |
| [25] | Mnih et al. | 2015 | Nature vol.518 no.7540 pp.529–533 | ✓ (10.1038/nature14236) | DQN (Ec. 15) | Trabajo seminal; uso correcto |
| [26] | Rashid et al. | 2018 | Proc. ICML vol.80 pp.4295–4304 | ✓ (PMLR acceso libre) | QMIX/MADRL (Ec. 16) | El primer autor es "Tabish Rashid", no "J. Rashid"; verificar nombre completo |
| [27] | McMahan et al. | 2017 | Proc. AISTATS vol.54 pp.1273–1282 | ✓ (PMLR acceso libre) | FedAvg (Ec. 17) | Uso correcto |
| [28] | Eisen & Ribeiro | 2020 | IEEE Trans. Signal Process. vol.68 pp.2977–2991 | ✓ (10.1109/TSP.2020.2979638) | GNN para RRM (Ec. 18) | Uso correcto |
| [29] | Ahmad et al. | 2018 | IEEE Commun. Standards Mag. vol.2 no.1 pp.36–43 | ✓ (10.1109/MCOMSTD.2018.1700063) | Seguridad 5G | Uso correcto; algo desactualizado para 2026 |

**Observaciones sobre DOIs:** 8 de las 29 referencias carecen de DOI porque son libros, estándares técnicos o informes. Esto es aceptable para estas categorías. Sin embargo, los informes de Ericsson [2], especificaciones ETSI [15], estándares 3GPP [12][19] y especificaciones O-RAN [22] deben incluir URLs de acceso para asegurar que los lectores puedan verificar la información. Los estándares 3GPP están disponibles gratuitamente en portal.3gpp.org.

### 3.2 Referencias Faltantes Críticas

Las siguientes referencias son importantes para el campo y deben considerarse para inclusión:

**Gemelos Digitales de Red:**
- Nguyen et al., "Digital Twin for 5G and Beyond Network: A Systematic Survey," *IEEE Access*, 2021.
- Wu et al., "Digital Twin Networks: A Survey," *IEEE Internet Things J.*, 2021.
- Masood et al., "Towards Autonomous Network Management: A Comprehensive Survey on Network Digital Twins," *IEEE Commun. Surveys Tuts.*, 2024.

**ISAC (Integrated Sensing and Communications):**
- Liu et al., "Integrated Sensing and Communication with Reconfigurable Intelligent Surface," *IEEE Trans. Wireless Commun.*, 2023.
- Zhang et al., "Enabling Joint Communication and Radar Sensing in Mobile Networks," *IEEE Commun. Surveys Tuts.*, 2022.

**LLMs/IA Generativa para Gestión de Redes:**
- Zhou et al., "Large Language Models for Telecom Network Management: Current Status and Future Directions," *IEEE Commun. Mag.*, 2024.
- Friha et al., "LLM-based Edge Intelligence: A Comprehensive Survey on Capabilities, Applications and Challenges," *IEEE Open J. Commun. Soc.*, 2024.

**RIS en contextos URLLC:**
- Xu et al., "Resource Management for RIS-Assisted URLLC Networks with Finite Blocklength Coding," *IEEE Trans. Wireless Commun.*, 2023.
- Pan et al., "Multicell MIMO Communications Relying on Intelligent Reflecting Surfaces," *IEEE Trans. Wireless Commun.*, 2020.

**Comunicaciones Semánticas:**
- Xie et al., "Deep Learning Enabled Semantic Communication Systems," *IEEE Trans. Signal Process.*, 2021.
- Qin et al., "Semantic Communications: Principles and Challenges," *arXiv*, 2021 (precursor de múltiples papers publicados en IEEE en 2022–2024).

**Zero-Touch Management:**
- Benzaid & Taleb, "AI-Driven Zero Touch Network and Service Management in 5G and Beyond," *IEEE Netw.*, 2020.
- ETSI GS ZSM 002 V1.1.1, "Zero-touch network and Service Management; Reference Architecture," 2019.

**O-RAN Reciente:**
- Lacava et al., "Programmable and Customized Intelligence for Traffic Steering in 5G Networks Using Open RAN Interfaces," *IEEE Trans. Mobile Comput.*, 2023.
- D'Oro et al., "DAPPS: Distributed and Asynchronous Privacy-Preserving Stochastic Optimization for Network Applications," *IEEE INFOCOM*, 2023.

### 3.3 Coherencia Interna de las Citas

**Posible error de nombre en [26]:** El primer autor de QMIX es "Tabish Rashid" (no "J. Rashid"). Los autores deben verificar el nombre completo. La referencia correcta es: T. Rashid, M. Samvelyan, C. S. de Witt, G. Farquhar, J. Foerster, and S. Whiteson.

**Referencia [29] desactualizada:** Ahmad et al. 2018 cubre seguridad 5G pero data de 2018. Para un artículo de 2026, debe complementarse con referencias más recientes sobre seguridad en O-RAN (e.g., trabajos del O-RAN WG11 publicados en 2022–2024).

**Referencia [21] sobre PF scheduling:** Nandagopal et al. 2000 es un paper de MobiCom sobre fairness en redes inalámbricas que sirvió como base para el Proportional Fair Scheduling. Es una cita válida, pero se recomienda complementar con la derivación formal del PF Scheduler de 3GPP para 5G NR, citando también Kelly et al. (1998) sobre proportional fairness y Nash bargaining, que es la base teórica de la optimización logarítmica.

---

## 4. VERIFICACIÓN DE EXPRESIONES MATEMÁTICAS EN FORMATO LATEX

### 4.1 Análisis de Ecuaciones

**Ecuaciones del cuerpo (1–18):**

| Ecuación | Descripción | Formato LaTeX | Numeración | Observación |
|:---:|:---|:---:|:---:|:---|
| (1) | Utilidad eMBB logarítmica | ✓ | ✓ `\tag{1}` | Correcta |
| (2) | Polyanskyi-Poor-Verdú FBL | ✓ | ✓ `\tag{2}` | Correcta; notación $Q^{-1}(\epsilon)$ estándar |
| (3) | Probabilidad de colisión RACH | ✓ | ✓ `\tag{3}` | Correcta |
| (4) | Problema MINLP RRM | ✓ | ✓ `\tag{4}` | Correcta; `\!\left(` para espaciado correcto ✓ |
| (5) | Restricciones MINLP | ✓ | ✓ `\tag{5}` | Correcta |
| (6) | Water-filling | ✓ | ✓ `\tag{6}` | Correcta; notación $(\cdot)^+$ apropiada |
| (7) | VNF Placement (bin-packing) | ✓ | ✓ `\tag{7}` | Correcta |
| (8) | SFC latency M/M/1 | ✓ | ✓ `\tag{8}` | Correcta |
| (9) | Hard isolation | ✓ | ✓ `\tag{9}` | Correcta |
| (10) | Soft isolation | ✓ | ✓ `\tag{10}` | Correcta |
| (11) | Lagrangian dual update | ✓ | ✓ `\tag{11}` | Correcta |
| (12) | PF scheduling metric | ✓ | ✓ `\tag{12}` | Correcta |
| (13) | Precoders MRT/ZF/MMSE | ✓ | ✓ `\tag{13}` | Correcta; tres fórmulas en una ecuación es aceptable |
| (14) | xApp optimization | ✓ | ✓ `\tag{14}` | Correcta |
| (15) | DQN loss function | ✓ | ✓ `\tag{15}` | Correcta; notación $\boldsymbol{\theta}^-$ estándar |
| (16) | QMIX value function | ✓ | ✓ `\tag{16}` | Correcta |
| (17) | FedAvg aggregation | ✓ | ✓ `\tag{17}` | Correcta |
| (18) | GNN message passing | ✓ | ✓ `\tag{18}` | Correcta |

**Ecuaciones del framework UMRO-5G (F1–F16):**

| Ecuación | Descripción | Formato LaTeX | Numeración | Observación |
|:---:|:---|:---:|:---:|:---|
| (F1) | Problema global UMRO-5G | ✓ | ✓ `\tag{F1}` | Correcta; `\substack{}` bien usado |
| (F2) | Función utilidad de slice | ✓ | ✓ `\tag{F2}` | Correcta; operador $[\cdot]^+$ apropiado |
| (F3) | Tasa alcanzable | ✓ | ✓ `\tag{F3}` | Correcta |
| (F4) | Latencia E2E descompuesta | ✓ | ✓ `\tag{F4}` | Correcta; `\underbrace{}` bien usado |
| (F5) | Restricción de potencia | ✓ | ✓ `\tag{F5}` | Correcta |
| (F6) | Restricción de subportadora | ✓ | ✓ `\tag{F6}` | Correcta |
| (F7) | Mínimo garantía slice | ✓ | ✓ `\tag{F7}` | Correcta |
| (F8) | Suma de recursos de slice | ✓ | ✓ `\tag{F8}` | Correcta |
| (F9) | Capacidad de cómputo | ✓ | ✓ `\tag{F9}` | Correcta |
| (F10) | Capacidad de memoria | ✓ | ✓ `\tag{F10}` | Correcta |
| (F11) | SLA latencia determinista | ✓ | ✓ `\tag{F11}` | Correcta |
| (F12) | SLA latencia probabilista URLLC | ✓ | ✓ `\tag{F12}` | Correcta; usar $\mathbb{P}$ en lugar de $\Pr$ para consistencia con IEEE style |
| (F13) | Restricción throughput mínimo | ✓ | ✓ `\tag{F13}` | Correcta |
| (F14) | Consistencia cross-layer | ✓ | ✓ `\tag{F14}` | Correcta |
| (F15) | Restricción de carga VNF | ✓ | ✓ `\tag{F15}` | Correcta |
| (F16) | Actualización dual Lagrangiana | ✓ | ✓ `\tag{F16}` | Correcta; consistente con (11) |

### 4.2 Ecuaciones sin Numeración o con Errores

**PROBLEMA CRÍTICO: La función de recompensa DRL en la Sección VIII.C carece de número de ecuación.** El texto la presenta como:

```latex
$$r_t = \sum_{k=1}^{K} w_k \log(1 + \text{SINR}_k) - \lambda \sum_{k \in \mathcal{K}_{\text{URLLC}}} \mathbb{1}[D_k > D^{\max}]$$
```

Esta ecuación utiliza el delimitador `$$...$$` sin `\tag{}`, lo que produce una ecuación en bloque sin número. En el contexto de la Sección VIII.C, esta es la ecuación que define el objetivo de entrenamiento de todos los agentes DRL comparados. Su importancia justifica una numeración formal (recomendado: `\tag{19}` o `\tag{R1}` para diferenciarla).

Adicionalmente, el símbolo $\lambda$ en la función de recompensa puede confundirse con los multiplicadores de Lagrange $\lambda_k^{(r)}$ definidos en las Ecuaciones (11) y (F16). Se recomienda usar una letra diferente, por ejemplo $\kappa$ o $\eta$, para el factor de penalización en la función de recompensa.

### 4.3 Consistencia de Notación

**Observaciones sobre consistencia notacional:**

1. **Símbolo $\lambda$:** Utilizado para cuatro conceptos distintos: (i) multiplicador de Lagrange en (11) y (F16); (ii) tasa de llegada en (8) y la Sección VIII.E; (iii) penalización en la función de recompensa (Sección VIII.C); (iv) factor de descuento aparece como $\gamma$ en (15). La reutilización de $\lambda$ para multiplicadores de Lagrange y tasas de llegada en el mismo documento es potencialmente confusa y debe resolverse mediante subscripts distintivos (e.g., $\lambda^{\text{Lag}}$ vs. $\lambda^{\text{arr}}$) o usando $\nu$ para uno de los usos.

2. **Símbolo $\sigma$:** Utilizado como (i) varianza del ruido ($\sigma^2$) en (4)(6)(F3); y (ii) factor de escala de VNF ($\sigma_f$) en (F9)(F10)(F15). Dos significados distintos para el mismo símbolo en el mismo artículo es incorrecto. Recomendación: usar $N_0$ o $\sigma_n^2$ para el ruido y $\xi_f$ para el factor de escala de VNF.

3. **Subíndices de slice:** El artículo usa $s$, $r$, y superscripts $(r)$ de forma no completamente consistente entre las Secciones III.B y VI.D. Unificar la notación de slice index a lo largo del documento.

4. **Notación de interfaces:** $\mathcal{I}_{12}$, $\mathcal{I}_{23}$, $\mathcal{I}_{34}$ son definidas en la Sección VI.F pero no aparecen en las ecuaciones del framework F1–F16. Incluir las interfaces en el diagrama de arquitectura (Fig. 1, que actualmente falta) reforzaría su definición.

---

## 5. ANÁLISIS DE FIGURAS Y RESULTADOS DE SIMULACIÓN

### 5.1 Figuras Existentes (fig1–fig7)

**fig1_throughput_vs_load.png** (Figura de throughput multi-slice vs carga):
- *Descripción:* Panel de tres subgráficas mostrando throughput por slice (eMBB, URLLC, mMTC) en función del factor de carga normalizado ρ ∈ [0.1, 1.0], comparando Hard/Soft/UMRO-5G.
- *Calidad:* Las etiquetas de ejes en bps/Hz son técnicamente correctas para el script pero inconsistentes con el texto que afirma Mbps. **Inconsistencia crítica:** ver Sección 2.3.
- *Recomendación:* Corregir las unidades y añadir grid lines. El título debería indicar "Normalized Spectral Efficiency" si se mantiene bps/Hz.

**fig2_utilization_vs_load.png** (Utilización de PRBs vs carga):
- *Descripción:* Curvas de utilización en porcentaje para los tres esquemas de asignación.
- *Calidad:* Figura clara y bien etiquetada. Las bandas de confianza son apropiadas.
- *Observación:* La curva UMRO-5G debería incluir una línea de referencia del 100% para destacar que logra saturación óptima.

**fig3_latency_violation.png** (Probabilidad de violación de latencia URLLC):
- *Descripción:* Probabilidad de violación del presupuesto de latencia URLLC en función de ρ.
- *Calidad:* La línea de referencia roja al 1% es excelente práctica de visualización. Las tendencias son físicamente plausibles.
- *Observación:* El eje Y debería usar escala logarítmica para mejor visualización de probabilidades pequeñas (<0.01), especialmente para la curva Hard Isolation que permanece por debajo del 0.5%.

**fig4_drl_convergence.png** (Curvas de convergencia DRL):
- *Descripción:* Recompensa normalizada (porcentaje del óptimo teórico) vs episodio de entrenamiento para DQN, MADRL/QMIX, Fed-DQN, y GNN-DRL.
- *Calidad:* Las curvas son conceptualmente correctas pero, como se indicó en Sección 2.1, provienen de modelos proxy tabulares, no de implementaciones reales. Esto debe declararse en el caption.
- *Observación:* Añadir bandas de confianza (5 semillas) y una línea horizontal de referencia para el "óptimo teórico" (100%).

**fig5a–fig5e** (Comparación de schedulers):
- *fig5a (avg throughput):* Barras comparativas para RR/MR/PF/DRL — bien ejecutado.
- *fig5b (Jain's fairness):* Índice de Jain — correctamente computado.
- *fig5c (5th percentile):* Throughput en percentil 5 — relevante para URLLC/cell-edge.
- *fig5d (cell-edge):* Throughput en usuarios de borde — complementa fig5c.
- *fig5e (CDF throughput):* CDF de throughput por usuario — la figura de mayor valor informativo del conjunto.
- *Calidad general:* Buena. Incluir en el caption la especificación del entorno (50 usuarios, 20 PRBs, SNR 0–25 dB).

**fig6_sfc_latency.png y fig6b_sfc_latency_combined.png** (Latencia SFC):
- *Descripción:* Latencia E2E del SFC vs tasa de llegada λ, comparando modelo M/M/1 vs DES.
- *Calidad:* La concordancia M/M/1 vs DES dentro del 5% es claramente visible. La región de alta carga donde el modelo analítico subestima la latencia también se distingue bien.
- *Observación:* Añadir líneas verticales indicando el 70% y 80% de la capacidad de cuello de botella (punto de operación seguro para URLLC).

**fig7_complexity.png** (Complejidad computacional):
- *Descripción:* Tiempo de decisión (ms) vs número de usuarios N para DRL/water-filling/B&B.
- *Calidad:* Excelente figura que justifica cuantitativamente la ventaja de DRL. El eje Y debería ser logarítmico para mostrar mejor el comportamiento exponencial de Branch-and-Bound.
- *Observación:* Añadir la línea de 1 ms (deadline URLLC) como referencia horizontal.

### 5.2 INCONSISTENCIAS DETECTADAS EN SIMULACIONES

#### Inconsistencia Principal: Unidades de Throughput

El script `sim_multi_slice.py` define la función de throughput como:
```python
SPEC_EFF = np.array([4.0, 1.5, 0.5])  # bps/Hz
def compute_throughput(alloc):
    return alloc * SPEC_EFF  # PRBs × bps/Hz = bps/Hz (adimensional normalizado)
```

El resultado numérico para el caso UMRO-5G a ρ=0.9 sería, aproximadamente:
- eMBB: ~45 PRBs × 4.0 bps/Hz = 180 "unidades"
- URLLC: ~28 PRBs × 1.5 bps/Hz = 42 "unidades"  
- mMTC: ~20 PRBs × 0.5 bps/Hz = 10 "unidades"
- **Total: ~232 "unidades"** — muy lejos de los 550 Mbps afirmados en el texto.

Para obtener throughput en Mbps realistas para 5G NR, sería necesario:
1. Definir el ancho de banda por PRB: con μ=0 (SCS=15 kHz), cada PRB tiene 12 subportadoras × 15 kHz = 180 kHz.
2. Multiplicar: throughput_eMBB = 45 PRBs × 180 kHz × 4.0 bps/Hz = 32.4 Mbps (por slot de 1 ms).
3. O alternativamente, escalar al ancho de banda total de canal: si B=20 MHz con 100 PRBs, ancho de banda_PRB = 200 kHz → throughput_eMBB_total = 45 × 200 kHz × 4.0 bps/Hz = 36 Mbps.

Los 450/510/550 Mbps afirmados en el texto corresponderían a un sistema con un ancho de banda significativamente mayor (p.ej., B=100 MHz) o a un escenario multi-celda. Esta inconsistencia debe resolverse definitivamente antes de la publicación.

#### Inconsistencia Secundaria: N_MONTE_CARLO

- Texto (Sección VIII.B): *"1,000 Monte Carlo iterations with 5 independent random seeds"*
- Script `sim_multi_slice.py`: `N_MONTE_CARLO = 200  # reduced for speed`

El comentario `# reduced for speed` sugiere que el script fue modificado para acortar el tiempo de ejecución durante el desarrollo, pero el texto nunca fue actualizado. Esto es una inconsistencia que compromete la reproducibilidad.

#### Inconsistencia Terciaria: Modelos DRL Proxy

El script `sim_drl_convergence.py` implementa un ambiente simplificado `SimpleEnv` con Q-learning tabular aproximado, no redes neuronales reales. Las curvas de convergencia presentadas en la Figura 4 y discutidas en la Sección VIII.C son *ilustrativas*, no el resultado de experimentos con implementaciones reales de DQN/QMIX/FedDQN/GNN-DRL. Esta limitación debe declararse explícitamente en el texto y en el caption de la figura.

### 5.3 Figuras Recomendadas para Incorporar

---

**Figura Recomendada 8: Diagrama de Arquitectura del Marco UMRO-5G**

- **Título:** "UMRO-5G Four-Layer Hierarchical Architecture with Three Nested Control Loops"
- **Descripción detallada para generación Python/Matplotlib:**  
  Esta figura debe ser un diagrama de arquitectura de sistema con cuatro bloques horizontales apilados (de abajo hacia arriba: Layer 1 Infrastructure, Layer 2 Virtualization & Slicing, Layer 3 Intelligence, Layer 4 Orchestration), cada uno representado como un rectángulo con fondo de color distinto (azul para L1, verde para L2, naranja para L3, rojo para L4). Dentro de cada capa, listar los componentes principales con texto: L1 contiene "O-RU Arrays, PRBs, COTS Servers (CPU/GPU), Fronthaul/Midhaul/Backhaul Links"; L2 contiene "NFVI (KVM/Kubernetes), SDN Controller, Network Slice Instances (NSI_eMBB, NSI_URLLC, NSI_mMTC)"; L3 contiene "Near-RT RIC (xApps: Traffic Steering, QoS Opt), Non-RT RIC (rApps: Policy, ML Training), DQN / QMIX / FedDQN / GNN-DRL Engines"; L4 contiene "ETSI MANO (NFVO, VNFM, VIM), 3GPP SA5 (CSMF, NSMF, NSSMF), SLA Engine, ZSM Intent Interface". En el lado derecho del diagrama, dibujar tres corchetes curvos de diferente longitud verticales etiquetados: "Fast Loop (<10ms)" abarcando solo L1, "Medium Loop (10ms–1s)" abarcando L1+L2+L3, "Slow Loop (>1s)" abarcando todas las capas. Entre capas adyacentes, dibujar flechas bidireccionales etiquetadas: I₁₂ (entre L1 y L2), I₂₃ (entre L2 y L3), I₃₄ (entre L3 y L4). Los protocolos de interfaz deben estar indicados: I₁₂ incluye "PRB telemetry / Resource reservation"; I₂₃ incluye "E2/O1 KPIs / RRM actions"; I₃₄ incluye "A1/O1 Policy / Lifecycle events". El tamaño recomendado es 12×10 pulgadas, fuente Helvetica/Arial 10pt, resolución mínima 300 DPI para IEEE.
- **Referencia en artículo:** Esta figura debe ser la Figura 1 en la Sección VI.B, donde el texto ya dice "The UMRO-5G architecture comprises four functional layers (Fig. 1)". Actualmente es la única figura mencionada en el texto que no existe físicamente en el directorio de figuras.

---

**Figura Recomendada 9: Optimización de Phase Shift en RIS con Restricciones URLLC**

- **Título:** "RIS Phase Shift Optimization: Joint Active-Passive Beamforming Performance vs. Number of RIS Elements"
- **Descripción detallada para generación Python/Matplotlib:**  
  Esta figura debe contener dos subgráficas. La subgráfica (a) muestra el throughput promedio del sistema (bps/Hz) en función del número de elementos RIS (N_RIS ∈ {16, 32, 64, 128, 256, 512}) para tres esquemas: (1) "Sin RIS" (línea base horizontal constante), (2) "RIS con optimización aleatoria de phase shift" (curva inferior de mejora moderada), y (3) "RIS con alternating optimization (AO)" (curva superior con mayor ganancia). El throughput base sin RIS podría ser 4.0 bps/Hz, con RIS aleatorio alcanzando hasta 5.5 bps/Hz en N=512, y con AO alcanzando hasta 7.2 bps/Hz. Las curvas deben incluir barras de error (5 semillas Monte Carlo). La subgráfica (b) muestra la probabilidad de violación de latencia URLLC P(D>D_max) en función de N_RIS para los mismos tres esquemas, demostrando que más elementos RIS no necesariamente mejoran la confiabilidad URLLC si el canal de control es lento. Los valores típicos: sin RIS P_viol=0.015, con AO N=512 P_viol=0.008, con AO N=128 P_viol=0.010. Ambas subgráficas deben tener eje X logarítmico en base 2 (16, 32, 64...). Parámetros del sistema: 1 BS con M=64 antenas, 1 RIS, K=10 usuarios, SNR=-10 dB (entorno adverso donde RIS es más útil), 1000 realizaciones de canal. El modelo de ganancia RIS sigue el modelo LoS: g_k = sqrt(N_RIS × beta_k) donde beta_k es el path loss del canal cascado BS-RIS-UE.
- **Referencia en artículo:** Debe ser referenciada en la Sección IX.E (Reconfigurable Intelligent Surfaces), reemplazando o complementando el texto descriptivo existente con evidencia numérica sobre la ganancia de RIS y sus trade-offs con URLLC.

---

**Figura Recomendada 10: Trade-off Eficiencia Energética vs. Throughput en el Marco UMRO-5G**

- **Título:** "Energy Efficiency-Throughput Trade-off Under UMRO-5G with Adaptive Cell Sleeping"
- **Descripción detallada para generación Python/Matplotlib:**  
  Esta figura debe mostrar la frontera de Pareto del trade-off entre Eficiencia Energética (EE, en bits/Joule) y Throughput del sistema (bps/Hz) para tres estrategias de gestión energética integradas en el lazo Slow de UMRO-5G: (1) "Always-On: todos los O-RUs activos" — punto fijo en baja EE y alto throughput; (2) "Static Sleep: apagado de O-RUs fijo según horario" — varios puntos en la frontera inferior; (3) "UMRO-5G Dynamic: apagado predicho por LSTM + realimentación Near-RT RIC" — frontera superior de Pareto. El eje X debe ir de 0 a 6 bps/Hz y el eje Y de 0 a 25 Mbits/Joule. La frontera UMRO-5G debe mostrar ~10–15 puntos que forman una curva convexa superior a las otras estrategias, con bandas de error de ±1 desviación estándar. Adicionalmente, marcar con un triángulo rojo el "Operating Point" de UMRO-5G que satisface los SLAs (D_URLLC ≤ 1 ms, R_eMBB ≥ 100 Mbps). El número de O-RUs activos puede variar de 2 a 20 en el escenario. Los parámetros energéticos típicos son: P_O-RU_active = 200 W, P_O-RU_sleep = 20 W, P_overhead = 500 W (backhaul, cooling). Incluir una leyenda indicando el número de O-RUs activos en la curva UMRO-5G mediante un colorbar o marcadores de tamaño variable.
- **Referencia en artículo:** Debe referenciarse en la Sección IX.D (Energy Efficiency) para complementar la discusión sobre "20–40% energy consumption reduction" mencionada en el texto con evidencia cuantitativa en un espacio de trade-off bidimensional.

---

**Figura Recomendada 11: Descomposición del Presupuesto de Latencia E2E por Capas UMRO-5G**

- **Título:** "End-to-End Latency Budget Decomposition Across UMRO-5G Layers for URLLC Service (1 ms Budget)"
- **Descripción detallada para generación Python/Matplotlib:**  
  Esta figura debe ser un diagrama de barras apiladas horizontales donde cada barra representa el presupuesto de latencia total de 1 ms (1000 μs) para un servicio URLLC, y cada segmento de color dentro de la barra corresponde a la contribución de cada componente UMRO-5G. Los componentes y sus latencias típicas son: L1 Processing (PHY/MAC @ DU): 100 μs; L1 Transmission (O-RU → O-DU fronthaul): 50 μs; L2 VNF Processing (UPF/AMF en NFVI): 150 μs; L2 Transport (fronthaul + midhaul): 100 μs; L3 DRL Inference (Near-RT RIC xApp): 100 μs; L4 Orchestration Overhead (bajo demanda, normalmente 0 en fast-path): 0–50 μs; Propagation + UE Processing: 200 μs; Margin (safety buffer): 250 μs. Las barras deben comparar tres escenarios: (1) "Baseline 5G (no UMRO-5G)", (2) "UMRO-5G Layer 1+2 only", (3) "Full UMRO-5G (all layers)". Usar colores distintos para cada componente: azul oscuro para L1 Processing, azul claro para L1 Transmission, verde para L2 VNF, verde claro para L2 Transport, naranja para L3 Inference, rojo para L4 Overhead, gris para propagación, y amarillo para margin. Incluir una línea vertical discontinua roja en x=1000 μs marcada "URLLC Deadline". El tamaño recomendado es 10×6 pulgadas con DPI=300. La leyenda debe explicar cada componente con su ecuación de referencia (e.g., "L2 VNF Processing: Eq. (8) M/M/1 term").
- **Referencia en artículo:** Debe referenciarse en la Sección VI.D al introducir la Ecuación (F4) de descomposición de latencia E2E, y también en la Sección VIII.E (SFC Latency Sensitivity Analysis) para conectar el análisis analítico M/M/1 con la distribución real del presupuesto de latencia en el sistema completo.

---

## 6. ESTADO DEL ARTE Y SUGERENCIAS DE EXPLORACIÓN ADICIONAL

### 6.1 Cobertura del Estado del Arte

**Bien cubierto:**
- Fundamentos de RRM 5G NR: Ecuaciones 1–6 cubren adecuadamente los modelos de Shannon, finite blocklength, OFDMA y water-filling.
- NFV/SDN/MANO: Sección III con referencias a ETSI [15], Mijumbi [7], Herrera & Botero [16].
- Network Slicing: Secciones III.B-C con Popovski [8], Foukas [9], Afolabi [10].
- O-RAN: Sección IV.C y referencias a O-RAN Alliance [22], Polese [11], Bonati [23].
- DRL/MARL/FL/GNN: Sección V con referencias seminales [25][26][27][28].

**Insuficientemente cubierto:**
- Gemelos Digitales de Red (solo mención cualitativa en Sección IX.G).
- ISAC (solo en Sección IX.K sobre evolución 6G, sin referencias).
- Comunicaciones THz (mencionadas en IX.K sin fórmulas ni referencias de modelos de canal).
- LLMs y IA generativa para gestión de redes (completamente ausente).
- Seguridad en O-RAN con referencias post-2020 (solo Ahmad 2018 [29]).
- Optimización multiobjetivo y algoritmos evolutivos para RRM (Pareto front, NSGA-II).

### 6.2 Temas Relevantes No Explorados o Poco Explorados

**1. ISAC (Integrated Sensing and Communications):**  
La Sección IX.K menciona ISAC como funcionalidad de 5G-Advanced/6G pero sin desarrollo técnico. Dado que el UMRO-5G framework incluye una capa de Infrastructure con arrays Massive MIMO, la extensión natural sería incluir las variables de diseño dual (beamforming para sensing y comunicación simultáneos). Los trabajos de Liu et al. (IEEE Trans. Wireless Commun., 2022–2023) sobre ISAC con OFDM y beamforming robusto son directamente relevantes.

**2. Modelos de Canal THz:**  
Las comunicaciones THz (0.1–10 THz) mencionadas en IX.K tienen modelos de canal radicalmente diferentes (absorción molecular, coherencia de tiempo en microsegundos). Los autores deberían citar los trabajos de Jornet & Akyildiz sobre modelado de canal THz y los resultados del proyecto TERRANOVA/6G-XTREME de la UE para dar sustento técnico a esta sección.

**3. Digital Twin Synchronization:**  
Los gemelos digitales de red requieren protocolos de sincronización con overhead controlado. El trabajo de Masood et al. (IEEE Commun. Surveys Tuts., 2024) proporciona un marco sistemático que complementaría la Sección IX.G.

**4. Verificación Formal de Controladores Neuronales:**  
La Sección IX.J menciona "formal verification" como dirección prometedora. Citar los trabajos de Katz et al. sobre Reluplex/Marabou (NIPS 2017, JAR 2022) y Singh et al. sobre abstract interpretation para redes neuronales daría sustento a esta afirmación.

**5. LLMs para Gestión de Redes (Intent-Based ZSM):**  
Trabajos de 2023–2024 de Samsung Research, Nokia Bell Labs y el ETSI ZSM ISG sobre el uso de GPT/LLaMA para interpretación de intents en ZSM son altamente relevantes para la Sección IX.J. La conexión entre las interfaces de intent de ZSM y los LLMs es uno de los temas más calientes en la comunidad de gestión de redes en 2024–2025.

**6. AI-Native Air Interface:**  
3GPP Release 18 introduce elementos de air interface basados en AI/ML (channel estimation con NN, beam prediction). Citar los documentos TR 38.843 (AI/ML for NR air interface) daría soporte a la discusión de la Sección IX.K sobre "AI-native air interface design."

### 6.3 Simulaciones Adicionales Recomendadas

**Simulación Adicional A: Scalability del Framework UMRO-5G con Multi-Cell**  
Extender la simulación multi-slice (Sección VIII.B) a un escenario multi-celda con B ∈ {1, 4, 9, 16} celdas, mostrando cómo la complejidad computacional del Slow Loop escala con el número de celdas y VNFs, y comparando el gap de optimalidad de la descomposición Lagrangiana frente a la solución centralizada. Este experimento validaría directamente la afirmación sobre reducción de complejidad de O(K^S × 2^{F×N}) a subproblemas manejables.

**Simulación Adicional B: SFC con VNFs en MEC vs. Cloud Central**  
Extender la simulación SFC (Sección VIII.E) para comparar el placement de VNFs en tres escenarios: (1) todos los VNFs en cloud central, (2) todos en MEC (edge), y (3) placement óptimo UMRO-5G (algunos VNFs en edge, otros en cloud según la latencia crítica). Esta simulación mostraría la ventaja del framework UMRO-5G sobre decisiones de placement estáticas, conectando directamente con la Sección IX.F sobre MEC.

**Simulación Adicional C: Robustez de DRL ante Non-Stationarity**  
Simular la degradación del rendimiento de los cuatro algoritmos DRL (DQN/QMIX/FedDQN/GNN-DRL) cuando el entorno cambia abruptamente (p.ej., un cambio súbito en la distribución de tráfico simulando un evento de pandemia), y evaluar la velocidad de re-adaptación de cada algoritmo. Esta simulación abordaría la limitación de "generalization" mencionada en la Sección IX.C y justificaría la necesidad de Transfer Learning en el framework UMRO-5G.

---

## 7. CORRECCIONES NECESARIAS PARA PUBLICACIÓN

### 7.1 Correcciones Mayores (Obligatorias)

1. **Inconsistencia de unidades en simulaciones** (Sección VIII.B, `sim_multi_slice.py`): La función `compute_throughput()` retorna bps/Hz × PRBs (unidades adimensionales normalizadas), mientras que el texto afirma valores en Mbps (450/510/550 Mbps). Los autores deben: (a) corregir los scripts para incluir conversión de unidades al ancho de banda real del canal 5G NR, o (b) corregir el texto para reportar las unidades correctas. Esta inconsistencia invalida las afirmaciones numéricas concretas del artículo y debe resolverse antes de cualquier consideración de aceptación.

2. **Figura de arquitectura UMRO-5G faltante** (Sección VI.B, Fig. 1): El texto referencia explícitamente "Fig. 1" en la Sección VI.B ("The UMRO-5G architecture comprises four functional layers (Fig. 1)") pero esta figura no existe en el directorio de figuras (`P11/simulations/figures/`). La descripción detallada para generarla se proporciona en la Sección 5.3 de este informe (Figura Recomendada 8). Esta figura es la contribución visual central del artículo y su ausencia es inaceptable para publicación.

3. **Numeración de ecuación de recompensa** (Sección VIII.C): La función de recompensa $r_t = \sum_{k} w_k \log(1+\text{SINR}_k) - \lambda \sum_{k \in \mathcal{K}_\text{URLLC}} \mathbb{1}[D_k > D^{\max}]$ carece de número de ecuación. Debe recibir una numeración formal (p.ej., `\tag{19}`). Además, $\lambda$ en esta ecuación colisiona con el uso de $\lambda$ para multiplicadores de Lagrange; debe cambiarse a otro símbolo (p.ej., $\kappa$).

4. **Discrepancia N_MONTE_CARLO** (Sección VIII.B, `sim_multi_slice.py`): El texto afirma 1,000 iteraciones MC pero el script define 200. Corregir la inconsistencia: actualizar el texto a 200 iteraciones o re-ejecutar con 1,000 (con tiempo de cómputo adecuado y semillas actualizadas).

5. **Declaración de limitaciones del modelo DRL proxy** (Sección VIII.C, Fig. 4): Las simulaciones de convergencia DRL utilizan modelos proxy tabulares simplificados, no implementaciones reales de DQN/QMIX/FedDQN/GNN-DRL con redes neuronales. Añadir una nota explícita en la Sección VIII.C y en el caption de la Figura 4 indicando: *"Las curvas de convergencia mostradas son ilustrativas, generadas mediante agentes tabulares proxy que capturan el comportamiento cualitativo de los algoritmos. Los valores cuantitativos exactos de convergencia dependerán de la implementación específica y del entorno de despliegue."*

6. **Adaptación al formato IEEE Wireless Communications** (Artículo completo): El artículo excede significativamente el límite de longitud de IEEE WC (~4,500 palabras magazine). Los autores deben elegir entre las dos rutas descritas en la Sección 1.2: condensar para IEEE WC o redirigir a IEEE Communications Surveys & Tutorials. Si se elige IEEE WC, los Apéndices con las ecuaciones detalladas y la taxonomía completa pueden moverse a material suplementario en línea.

7. **Corrección notacional: símbolo $\sigma$** (Secciones II–VI): El símbolo $\sigma^2$ se usa para varianza del ruido (Ecuaciones 4, 6, F3) y $\sigma_f$ se usa para el factor de escala de VNF (Ecuaciones F9, F10, F15). Esta ambigüedad debe resolverse cambiando el factor de escala de VNF a $\xi_f$ o $\kappa_f$.

### 7.2 Correcciones Menores (Recomendadas)

1. **Verificar nombre del primer autor de QMIX** [26]: El primer autor es "Tabish Rashid", no "J. Rashid". Verificar y corregir la referencia.

2. **Añadir URLs a referencias sin DOI** ([2], [3], [12], [15], [18], [19], [22], [24]): Incluir URLs de acceso para el Ericsson Mobility Report, ITU-R M.2410, 3GPP TS 38.214 y TS 28.530, IETF RFC 7498, ETSI GS NFV-MAN 001, y O-RAN Architecture Description.

3. **Añadir escala logarítmica en Fig. 3**: El eje Y de la figura de probabilidad de violación URLLC debe ser logarítmico para visualizar mejor el rango completo de probabilidades.

4. **Añadir escala logarítmica en Fig. 7**: El eje Y de la figura de complejidad computacional debe ser logarítmico para mostrar el comportamiento exponencial de Branch-and-Bound.

5. **Añadir línea de referencia en Fig. 7**: Incluir una línea horizontal discontinua en 1 ms (deadline URLLC) para contextualizar los resultados de complejidad.

6. **Corregir el conteo de subsecciones en Sección IX**: El artículo declara "10 subsections" pero contiene 11 (A–K). Actualizar la declaración o consolidar subsecciones.

7. **Actualizar referencia de seguridad [29]**: Ahmad et al. 2018 está desactualizado para un artículo de 2026. Complementar con una referencia post-2022 sobre seguridad en O-RAN (e.g., O-RAN Alliance WG11 Security specifications).

8. **Añadir $\Pr$ vs $\mathbb{P}$**: En la Ecuación (F12), usar $\mathbb{P}[\cdot]$ en lugar de $\Pr[\cdot]$ para consistencia con el estilo IEEE. Alternativamente, usar $\Pr$ consistentemente en todo el documento.

9. **Añadir intervalos de confianza formales**: Incluir al menos un párrafo en la Sección VIII.A describiendo el método de estimación de intervalos de confianza (bootstrap o t-distribution), indicando el nivel de confianza (95%) y el número efectivo de muestras independientes.

10. **Corregir el tipo de artículo en metadatos**: El encabezado del archivo indica "Research Article — IEEE Transactions Format" pero el contenido es fundamentalmente un survey/tutorial. Actualizar a "Survey/Tutorial Article — IEEE Wireless Communications Magazine Format" o el tipo apropiado según el journal destino elegido.

### 7.3 Correcciones de Estilo y Formato IEEE Wireless Communications

**Límites de longitud y formato IEEE WC:**
- IEEE Wireless Communications acepta artículos de tipo magazine de 4,000–5,000 palabras con hasta 6 figuras para el cuerpo principal, más material suplementario.
- El artículo actual contiene aproximadamente 15,000–18,000 palabras con 16+16=34 ecuaciones numeradas, 3 tablas extensas y referencias a 7+ figuras.
- Para adaptarse al formato IEEE WC, se sugiere la siguiente estructura condensada:
  - Abstract: máximo 200 palabras (actualmente ~250 palabras ✓ cercano al límite)
  - Introducción (~500 palabras): mantener Tabla I pero simplificar narrativa
  - Secciones II–V: condensar en una única sección de "5G RRM and AI Background" (~800 palabras) con referencias cruzadas
  - Sección VI (UMRO-5G Framework): mantener completa (~1,500 palabras) — esta es la contribución central
  - Sección VII (Taxonomía 5D): condensar a 400 palabras + Tabla III en material suplementario
  - Sección VIII (Simulaciones): 700 palabras con las figuras más relevantes (Fig. 1 arquitectura + 3 figuras de resultados)
  - Sección IX (Desafíos): condensar a 600 palabras con los 5 desafíos más relevantes
  - Conclusiones: 300 palabras
  - **Total estimado condensado: ~5,000 palabras** — compatible con IEEE WC

**Alternativa recomendada (Ruta B):** Redirigir a IEEE Communications Surveys & Tutorials, donde el artículo sería más competitivo en su formato actual con las adiciones del estado del arte identificadas en la Sección 3.2. IEEE CSTUT tiene un Factor de Impacto de ~35 y una audiencia mayor para surveys de este tipo.

---

## 8. ANÁLISIS DE IMPACTO Y ADECUACIÓN AL JOURNAL

### 8.1 Encaje con el Alcance de IEEE Wireless Communications

IEEE Wireless Communications cubre "emerging wireless communications technologies, systems, and applications with emphasis on practical system considerations." El artículo propuesto encaja en este alcance desde la perspectiva de:
- Gestión de recursos en redes 5G/6G: tema central de IEEE WC desde 2019–presente
- O-RAN y redes AI-native: área de creciente publicación en IEEE WC
- DRL para telecomunicaciones: múltiples artículos publicados en IEEE WC 2021–2024

Sin embargo, el nivel de detalle matemático (34 ecuaciones numeradas) y la amplitud del survey (cubriendo RRM, NFV, SDN, slicing, O-RAN, DRL en detalle) son más propios de IEEE Communications Surveys & Tutorials o IEEE Transactions que del estilo magazine de IEEE WC.

### 8.2 Impacto y Novedad

| Aspecto | Evaluación | Justificación |
|:---|:---:|:---|
| Novedad del framework UMRO-5G | Alta (integradora) | Primera integración formal de 4 dominios con F1–F16 |
| Novedad de la taxonomía 5D | Alta | Dimensiones "Architectural Scope" y "Virtualization Level" son nuevas |
| Novedad de las interfaces I₁₂, I₂₃, I₃₄ | Media-Alta | Formalización de flujos de datos inter-capa es contribución práctica |
| Novedad de las simulaciones | Media | Uso de proxies simplificados limita la validez experimental |
| Cobertura del estado del arte | Media | Ausencias notables en NDT, ISAC, LLMs |
| Solidez matemática | Alta | Ecuaciones correctas; descomposición Lagrangiana bien fundamentada |
| Reproducibilidad | Media | Scripts disponibles pero con inconsistencias que deben corregirse |

### 8.3 Recomendación Final

**Decisión: MAJOR REVISION**

El artículo tiene valor científico real en su taxonomía 5D y la formulación unificada UMRO-5G, y cubre un área temática de máxima relevancia para la comunidad de redes inalámbricas. Sin embargo, las inconsistencias identificadas —especialmente la discrepancia de unidades en throughput y la ausencia de la figura de arquitectura principal— deben corregirse antes de cualquier aceptación.

Se recomienda que los autores:

1. **Elijan explícitamente el formato objetivo:** IEEE WC (condensado, ~5,000 palabras) o IEEE CSTUT (ampliado con estado del arte completo).
2. **Corrijan las inconsistencias de simulación** (unidades, N_MONTE_CARLO, declaración de modelos proxy) antes de re-someter.
3. **Generen la figura de arquitectura** (Fig. 1 de UMRO-5G) que ya está referenciada en el texto.
4. **Actualicen el estado del arte** con referencias de 2022–2024 sobre NDT, ISAC, LLMs para gestión de redes.
5. **Sometan el artículo revisado** en un plazo de 60 días con carta de respuesta detallando cada corrección.

La re-evaluación se enfocará en la corrección de las inconsistencias numéricas y la adecuación al formato, asumiendo que las contribuciones conceptuales (taxonomía 5D, framework UMRO-5G, formulación F1–F16) se mantienen sin cambios substanciales.

---

## CHECKLIST DE VERIFICACIÓN

| Criterio | Estado | Observaciones |
|:---|:---:|:---|
| Abstract claro y completo | ✓ | Incluye C1–C4, métricas clave y alcance 6G |
| Keywords apropiados | ✓ | 9 keywords apropiados; considerar añadir "network digital twins" |
| Introducción con motivación clara | ✓ | Motivación cuantitativa con ITU-R IMT-2020; Tabla I posiciona bien |
| Contribuciones claramente definidas | ✓ | C1–C4 explícitas en Sección I.C |
| Marco matemático riguroso | ✓ | Ecuaciones F1–F16 internamente consistentes; Lagrangiana bien formulada |
| Ecuaciones en formato LaTeX | ✓ | Todas las ecuaciones usan `$$...$$` con `\tag{}`; sin errores de sintaxis |
| Ecuación de recompensa numerada | ✗ | Sección VIII.C: función r_t sin `\tag{}`; corrección requerida |
| Simulaciones reproducibles | ⚠ | Scripts disponibles con semillas fijas; inconsistencia N_MC=200 vs texto 1000 |
| Unidades consistentes | ✗ | Script: bps/Hz × PRBs; Texto: Mbps — inconsistencia crítica |
| Figuras con calidad IEEE | ⚠ | Figuras generadas a 200 DPI; incrementar a 300+ DPI para publicación |
| Figura de arquitectura del sistema | ✗ | Fig. 1 referenciada en Sec. VI.B pero no existe en directorio de figuras |
| Referencias completas y verificadas | ⚠ | 29 refs presentes; verificar nombre de autor [26]; URLs faltantes en [2][3][12][15][18][19][22] |
| DOIs disponibles | ⚠ | 20/29 referencias con DOI; 9 sin DOI (libros, estándares, RFC — aceptable) |
| Conclusiones apoyadas por datos | ⚠ | Cualitativamente correctas; valores numéricos afectados por inconsistencia de unidades |
| Comparación con estado del arte | ✓ | Tabla I compara con 4 surveys previos; gaps en NDT/ISAC/LLMs |
| Ajuste a formato IEEE WC | ✗ | Artículo ~15,000 palabras vs límite ~4,500 palabras de IEEE WC |
| Longitud apropiada para la revista | ✗ | Necesita condensación significativa para IEEE WC; adecuado para IEEE CSTUT |
| Notación matemática consistente | ⚠ | Símbolo $\sigma$ con doble significado; $\lambda$ con triple significado |
| Estado del arte actualizado | ⚠ | Base sólida pero falta NDT, ISAC, LLMs, RIS-URLLC, comunicaciones semánticas |
| Modelos DRL correctamente declarados | ⚠ | Implementaciones proxy no declaradas explícitamente como tales |

---

## INSTRUCCIONES PARA EL AUTOR

Estimados autores,

El artículo "UMRO-5G: A Unified Framework for Management and Resource Orchestration in AI-Native 5G and Beyond Networks" ha sido evaluado y se solicita una **revisión mayor** antes de que pueda ser considerado para publicación en IEEE Wireless Communications. El trabajo presenta contribuciones científicas genuinas —especialmente la taxonomía de cinco dimensiones y la formulación matemática unificada F1–F16— y su temática es de alta relevancia para la comunidad de redes inalámbricas. Sin embargo, deben abordarse las siguientes correcciones antes de la re-evaluación.

**Correcciones Obligatorias (deben resolverse completamente):**

**[C-M1] Inconsistencia crítica de unidades (Sección VIII.B y scripts de simulación):**  
Los scripts de simulación calculan el throughput en unidades de bps/Hz × PRBs (adimensional normalizado), mientras que el texto del artículo afirma valores en Mbps (450 Mbps, 510 Mbps, 550 Mbps). Esta inconsistencia invalida las comparaciones numéricas concretas del artículo. Deben corregir: (a) los scripts para incluir conversión al ancho de banda real del sistema 5G NR (indicando B en MHz, Δf en kHz, y N_PRB), y actualizar las figuras resultantes; o (b) el texto para reportar las unidades correctas del script. Recomendamos la opción (a) para que los resultados sean físicamente interpretables. Por ejemplo, con B=20 MHz, N_PRB=100, SCS=15 kHz → throughput real = resultado_script × (B/N_PRB) × 1000 = resultado_script × 200 kHz.

**[C-M2] Figura de arquitectura UMRO-5G faltante (Sección VI.B):**  
El texto referencia "Fig. 1" con la arquitectura de cuatro capas del framework UMRO-5G en la Sección VI.B, pero esta figura no está presente en el directorio de figuras. Deben generar un diagrama de arquitectura del sistema que muestre las cuatro capas (Infrastructure, Virtualization & Slicing, Intelligence, Orchestration), los tres lazos de control (Fast/Medium/Slow) con sus rangos temporales, las interfaces inter-capa (I₁₂, I₂₃, I₃₄) con sus protocolos, y los componentes principales de cada capa. Una descripción detallada suficiente para la generación automática con Python/Matplotlib se proporciona en la Sección 5.3 (Figura Recomendada 8) de este informe.

**[C-M3] Numeración y corrección de la ecuación de recompensa (Sección VIII.C):**  
La función de recompensa $r_t$ presentada en la Sección VIII.C carece de número de ecuación (`\tag{}`). Añadir numeración formal. Adicionalmente, el símbolo $\lambda$ en esta ecuación colisiona con el uso de $\lambda$ para multiplicadores de Lagrange en Ecuaciones (11) y (F16). Cambiar el factor de penalización en la función de recompensa a otro símbolo (p.ej., $\kappa$ o $\eta$).

**[C-M4] Corrección de N_MONTE_CARLO (Sección VIII.B y script):**  
El texto afirma "1,000 Monte Carlo iterations" pero el script define `N_MONTE_CARLO = 200`. Deben resolver esta inconsistencia actualizando el texto (si 200 es el valor real) o re-ejecutando los scripts con 1,000 iteraciones y semillas actualizadas.

**[C-M5] Declaración explícita de modelos DRL proxy (Sección VIII.C y Fig. 4):**  
Las simulaciones de convergencia DRL utilizan agentes tabulares simplificados que aproximan el comportamiento de DQN/QMIX/FedDQN/GNN-DRL, no implementaciones reales con redes neuronales. Deben añadir una nota explícita en el texto de la Sección VIII.C y en el caption de la Figura 4 indicando esta limitación. La nota sugerida es: *"The convergence curves shown are generated using simplified tabular proxy agents that capture the qualitative convergence behavior of each algorithm. Exact quantitative convergence rates will vary depending on specific hyperparameter configurations, neural network architectures, and deployment environments."*

**[C-M6] Adaptación al formato del journal (Artículo completo):**  
Con aproximadamente 15,000–18,000 palabras y 34 ecuaciones numeradas, el artículo excede significativamente el límite de IEEE Wireless Communications (~4,500 palabras para artículos magazine). Deben elegir una de las siguientes rutas:  
- **Ruta A (IEEE WC):** Condensar el artículo a ~5,000 palabras, manteniendo el framework UMRO-5G (Sección VI), la taxonomía simplificada (Tabla III), y 3–4 figuras clave. Mover las Ecuaciones F1–F16 detalladas y la Tabla II a material suplementario en línea.  
- **Ruta B (IEEE Communications Surveys & Tutorials):** Ampliar el estado del arte con las referencias faltantes identificadas en la Sección 3.2 de este informe (NDT, ISAC, LLMs, RIS-URLLC, comunicaciones semánticas), expandir la sección de simulaciones con los experimentos adicionales propuestos (Sección 6.3), y someter a IEEE CSTUT donde la longitud actual sería apropiada.

**Correcciones de Notación (menores pero importantes):**

**[C-m1] Símbolo $\sigma$ ambiguo:** $\sigma^2$ se usa para ruido (Ecuaciones 4, 6, F3) y $\sigma_f$ para factor de escala VNF (F9, F10, F15). Cambiar el factor de escala VNF a $\xi_f$ o $\kappa_f$ en todas sus apariciones.

**[C-m2] Verificar nombre de autor [26]:** El primer autor de QMIX es "Tabish Rashid", no "J. Rashid". Verificar y corregir todos los detalles bibliográficos de la referencia.

**[C-m3] URLs para referencias sin DOI:** Añadir URLs de acceso para [2] (Ericsson Mobility Report), [3] (ITU-R M.2410), [12] (3GPP TS 38.214), [15] (ETSI GS NFV-MAN 001), [18] (RFC 7498), [19] (3GPP TS 28.530), [22] (O-RAN Alliance Architecture Description).

**[C-m4] Escala logarítmica en figuras:** Añadir escala logarítmica en el eje Y de la Figura 3 (probabilidad de violación URLLC) y en el eje Y de la Figura 7 (complejidad computacional). Añadir línea de referencia horizontal en 1 ms en la Figura 7.

**Actualizaciones del Estado del Arte (recomendadas para Ruta B):**  
Se recomienda citar trabajos recientes sobre: (1) gemelos digitales de red (Masood et al. IEEE CSTUT 2024); (2) ISAC (Zhang et al. IEEE CSTUT 2022); (3) LLMs para gestión de redes (Zhou et al. IEEE Commun. Mag. 2024); (4) RIS en URLLC (Xu et al. IEEE TWC 2023); (5) comunicaciones semánticas (Xie et al. IEEE TSP 2021); (6) Zero-Touch Management formal (Benzaid & Taleb IEEE Netw. 2020; ETSI ZSM 002).

**Sobre el Tipo de Artículo:**  
Se recomienda reconsiderar la clasificación del artículo. El trabajo es fundamentalmente un survey/tutorial con contribuciones de framework, no un artículo de investigación experimental primaria. Esta distinción es importante para la selección del journal y para las expectativas del lector respecto a la validación experimental.

El plazo sugerido para la revisión es de **60 días**. La carta de respuesta debe incluir una tabla punto a punto que mapee cada corrección solicitada con los cambios realizados en el manuscrito (indicando sección, número de línea, y descripción del cambio). Un re-envío bien documentado acelerará el proceso de re-evaluación.

Los autores han realizado un trabajo substantivo de síntesis e integración que, una vez corregidos los problemas identificados, tiene potencial real de convertirse en una referencia citada en la comunidad de gestión de redes 5G/6G. Se anima a los autores a abordar las correcciones con rigor y a considerar la Ruta B (IEEE CSTUT) como la opción de mayor impacto a largo plazo para este tipo de contribución comprehensiva.

---

*Informe de evaluación preparado por: Editor Académico Experto en Redes Inalámbricas e Inteligencia Artificial.*  
*Fecha: Mayo 2026.*  
*Documento generado para: IEEE Wireless Communications (Q1) — Proceso de revisión por pares.*
