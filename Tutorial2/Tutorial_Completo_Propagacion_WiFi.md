# Tutorial Completo: Propagación de Ondas Electromagnéticas y Redes WiFi — De los Fundamentos al Dimensionamiento

**Autor:** Tutorial Pedagógico de Telecomunicaciones  
**Nivel:** Introductorio–Avanzado  
**Idioma:** Español  
**Cobertura:** Secciones 1–14: propagación, WiFi 5/6/6E/7/8, dimensionamiento, seguridad y tendencias

---

## Tabla de Contenidos

- 1. Introducción General al Tutorial
  - 1.1 Motivación y Objetivos
  - 1.2 Audiencia Objetivo
  - 1.3 Estructura del Documento
- 2. Fundamentos de Propagación de Ondas Electromagnéticas
  - 2.1 Conceptos Básicos
    - 2.1.1 Ondas Electromagnéticas: Definición, Espectro, Longitud de Onda y Frecuencia
    - 2.1.2 Ecuaciones de Maxwell Simplificadas y su Relevancia
    - 2.1.3 Potencia Radiada, PIRE y Ganancia de Antena
  - 2.2 Mecanismos de Propagación a Gran Escala
    - 2.2.1 Reflexión
    - 2.2.2 Difracción
    - 2.2.3 Dispersión (Scattering)
    - 2.2.4 Absorción Atmosférica
  - 2.3 Modelado de Pérdida de Trayectoria (Path Loss)
    - 2.3.1 Modelo de Espacio Libre (Ecuación de Friis)
    - 2.3.2 Modelo General de Pérdida de Trayectoria
    - 2.3.3 Desvanecimiento por Sombra (Shadowing Log-Normal)
- 3. Modelos de Propagación en Exteriores
  - 3.1 Modelo Okumura-Hata
    - 3.1.1 Contexto Histórico
    - 3.1.2 Ecuación del Modelo Okumura-Hata
    - 3.1.3 Factor de Corrección $a(h_m)$
    - 3.1.4 Ejemplo Numérico Completo
    - 3.1.5 Limitaciones del Modelo
  - 3.2 Modelo COST-231 Hata
    - 3.2.1 Extensión del Modelo Hata
    - 3.2.2 Ecuación del Modelo COST-231 Hata
    - 3.2.3 Ejemplo Numérico Completo
  - 3.3 Modelo 3GPP TR 38.901 (5G NR)
    - 3.3.1 Contexto: Rangos de Frecuencia FR1 y FR2
    - 3.3.2 Modelo UMi-Street Canyon
    - 3.3.3 Modelo UMa
    - 3.3.4 Modelo RMa
    - 3.3.5 Probabilidad LoS/NLoS
    - 3.3.6 Ejemplo Numérico para UMi-LoS
- 4. Modelos de Propagación en Interiores
  - 4.1 Recomendación ITU-R P.1238-11
    - 4.1.1 Introducción
    - 4.1.2 Ecuación del Modelo
    - 4.1.3 Valores Típicos de N
    - 4.1.4 Valores de $L_f(n)$
    - 4.1.5 Ejemplo Numérico Completo
  - 4.2 Modelos IEEE 802.11 (TGax y TGbe)
    - 4.2.1 Introducción
    - 4.2.2 Escenario Residencial (TGax Residential)
    - 4.2.3 Escenario Empresarial (Enterprise)
    - 4.2.4 Atenuación por Materiales
    - 4.2.5 BSS Coloring como Respuesta a Interferencia Espacial
  - 4.3 Modelo de Pérdida por Materiales y Link Budget Indoor
    - 4.3.1 Modelo de Pérdida por Materiales
    - 4.3.2 Tabla de Pérdidas por Material
    - 4.3.3 Ejemplo Completo de Link Budget Indoor
    - 4.3.4 Relación entre RSSI, SNR y MCS
    - 4.3.5 Capacidad MIMO
    - 4.3.6 Adaptación de Enlace
  - 4.4 Dimensionamiento de Cobertura
    - 4.4.1 Cálculo del Radio de Cobertura
    - 4.4.2 Ejemplo Completo de Dimensionamiento para Oficina
- 5. Introducción a las Redes WiFi
  - 5.1 ¿Qué es WiFi?
  - 5.2 Evolución Histórica de WiFi
- 6. WiFi 5 (IEEE 802.11ac)
  - 6.1 Características Principales
  - 6.2 Mejoras sobre WiFi 4 (802.11n)
    - 6.2.1 Mayor Ancho de Banda: Hasta 160 MHz vs 40 MHz
    - 6.2.2 MU-MIMO Downlink (Hasta 4 usuarios simultáneos)
    - 6.2.3 256-QAM vs 64-QAM: Explicación Detallada de QAM
    - 6.2.4 Beamforming Obligatorio
  - 6.3 Cálculo de Velocidad PHY WiFi 5
  - 6.4 Canales en 5 GHz
  - 6.5 Link Budget WiFi 5
- 7. WiFi 6 (IEEE 802.11ax)
  - 7.1 Motivaciones y Contexto
  - 7.2 OFDMA (Orthogonal Frequency Division Multiple Access)
    - Explicación detallada de OFDMA vs OFDM
    - Resource Units (RUs)
    - Uplink y Downlink OFDMA
    - Ejemplo numérico — Eficiencia de OFDMA
  - 7.3 1024-QAM
  - 7.4 MU-MIMO Bidireccional
  - 7.5 BSS Coloring
    - Problema: Interferencia inter-BSS
    - Solución: BSS Color de 6 bits
    - Ejemplo de BSS Coloring
  - 7.6 Target Wake Time (TWT)
  - 7.7 Cálculo de Velocidad PHY WiFi 6
- 8. WiFi 6E (IEEE 802.11ax en 6 GHz)
  - 8.1 Espectro de 6 GHz
  - 8.2 Canales Disponibles en 6 GHz
  - 8.3 Beneficios de WiFi 6E
    - Despliegue Greenfield (Sin dispositivos legacy)
    - Reducción de Interferencia
    - Más Canales No Solapados para Canales Anchos
    - Misma PHY que WiFi 6 pero en espectro más limpio
  - 8.4 Consideraciones de Propagación en 6 GHz
    - Mayor pérdida de trayecto a 6 GHz vs 5 GHz
    - Pérdidas de penetración en paredes
    - Implicaciones de cobertura
    - Ejemplo numérico — Comparación de cobertura 5 GHz vs 6 GHz
- 9. WiFi 7: IEEE 802.11be — Extremely High Throughput (EHT)
  - 9.1 Motivación y Contexto de WiFi 7
    - 9.1.1 ¿Por qué hizo falta WiFi 7?
    - 9.1.2 Aplicaciones impulsoras
    - 9.1.3 Línea temporal y proceso de normalización
    - 9.1.4 Objetivos de desempeño
  - 9.2 Arquitectura y Características Fundamentales de WiFi 7
    - 9.2.1 Multi-Link Operation (MLO)
      - Modelo simple de reducción de latencia
    - 9.2.2 Canales de 320 MHz
      - Espaciado entre subportadoras y tamaño FFT
    - 9.2.3 4096-QAM (4K-QAM)
      - Requisito de SNR
    - 9.2.4 Hasta 16 flujos espaciales
  - 9.3 Cálculo de Throughput Máximo Teórico de WiFi 7
    - 9.3.1 Significado físico de cada parámetro
    - 9.3.2 Parámetros para el caso máximo WiFi 7
    - 9.3.3 ¿Por qué el resultado es tan alto?
    - 9.3.4 Tabla comparativa con WiFi 5, 6 y 6E
  - 9.4 Multi-Link Operation (MLO) — Análisis Detallado
    - 9.4.1 Concepto de MLD (Multi-Link Device)
    - 9.4.2 Tipos principales de MLO
      - a) STR — Simultaneous Transmit and Receive
      - b) NSTR — Non-Simultaneous Transmit and Receive
      - c) eMLSR — operación multi-enlace mejorada con radio único
    - 9.4.3 Modelo matemático de caudal agregado
    - 9.4.4 Modelo de reducción de latencia
    - 9.4.5 Ejemplo detallado: hogar con 3 enlaces simultáneos
  - 9.5 Preamble Puncturing en WiFi 7
    - 9.5.1 ¿Qué es?
    - 9.5.2 Ancho efectivo
    - 9.5.3 Ejemplo: canal de 320 MHz con dos subcanales de 20 MHz perforados
  - 9.6 OFDMA Mejorado en WiFi 7
    - 9.6.1 Tamaños de Unidad de Recursos (RU)
    - 9.6.2 Multi-RU allocation
    - 9.6.3 Ejemplo de ocupación en un canal EHT muy ancho
  - 9.7 Presupuesto de Enlace y Dimensionamiento de Cobertura WiFi 7
    - 9.7.1 Ecuación general del presupuesto de enlace
    - 9.7.2 Cálculo de sensibilidad a partir del ruido térmico
    - 9.7.3 Modelo de pérdida de propagación
    - 9.7.4 Ejemplo detallado: despliegue empresarial en 6 GHz
      - Caso A: MCS alto (4096-QAM)
      - Caso B: MCS medio
      - Caso C: MCS robusto
    - 9.7.5 Consideraciones de planificación celular WiFi 7
  - 9.8 Ejemplo Integral de Dimensionamiento WiFi 7
    - 9.8.1 Escenario de partida
    - 9.8.2 Dimensionamiento por capacidad
    - 9.8.3 Dimensionamiento por cobertura
    - 9.8.4 Decisión final de número de APs
    - 9.8.5 Plan de canales con MLO
    - 9.8.6 Throughput esperado por usuario
    - 9.8.7 Análisis de latencia
    - 9.8.8 Conclusiones del ejemplo integral
- 10. WiFi 8: IEEE 802.11bn — Ultra High Reliability (UHR)
  - 10.1 Motivación y Visión de WiFi 8
  - 10.2 Tecnologías Clave Propuestas para WiFi 8
    - 10.2.1 Coordinated Multi-AP Operation
    - 10.2.2 HARQ (Hybrid Automatic Repeat Request) para WiFi
    - 10.2.3 Enhanced Deterministic Latency
    - 10.2.4 Potencial 16384-QAM (16K-QAM)
  - 10.3 Comparativa Generacional WiFi 5 → WiFi 6 → WiFi 6E → WiFi 7 → WiFi 8
- 11. Dimensionamiento Avanzado de Redes WiFi
  - 11.1 Metodología General de Dimensionamiento
  - 11.2 Dimensionamiento por Cobertura
    - Cálculo del radio de celda por banda
    - Impacto de paredes y plantas
    - Ejemplo numérico completo — edificio de varias plantas
  - 11.3 Dimensionamiento por Capacidad
    - Planificación de reutilización de canal
    - Ejemplo numérico completo — campus universitario con 500 usuarios
  - 11.4 Dimensionamiento Integrado (Cobertura + Capacidad)
    - Ejemplo completo — hospital con requisitos mixtos
    - Consideraciones MLO para WiFi 7
  - 11.5 Herramientas de Planificación y Simulación
- 12. Seguridad en Redes WiFi
  - 12.1 Evolución de los Protocolos de Seguridad WiFi
    - WEP: vulnerabilidades fundamentales
    - WPA: solución intermedia con TKIP
    - WPA2: AES-CCMP y el protocolo de cuatro mensajes
    - WPA3: SAE (Simultaneous Authentication of Equals)
  - 12.2 WPA3 y Enhanced Open — Análisis Detallado
    - Pasos de SAE con ejemplo numérico de juguete
    - Forward secrecy
    - Protección frente a diccionario offline
    - OWE (Opportunistic Wireless Encryption)
    - Modo empresarial de 192 bits
    - PMF (Protected Management Frames)
  - 12.3 Seguridad en WiFi 7
  - 12.4 Amenazas Comunes y Contramedidas
    - Evil Twin
    - Deauthentication y protección con PMF
    - KRACK
    - Detección de AP no autorizado
- 13. Tendencias Futuras y Convergencia Tecnológica
  - 13.1 Convergencia WiFi-5G/6G
    - Network slicing aplicado a WiFi
    - ATSSS (Access Traffic Steering, Switching, Splitting)
    - Compartición de espectro no licenciado: NR-U vs WiFi
  - 13.2 WiFi Sensing (802.11bf)
  - 13.3 Inteligencia Artificial en Redes WiFi
    - Selección de canal y optimización de roaming
    - Reinforcement learning para coordinación de APs
    - Asignación predictiva de recursos
  - 13.4 Hacia WiFi en Espectro Superior a 7 GHz
    - Recapitulación de 60 GHz: 802.11ad/ay
    - Potencial uso de bandas entre 7 y 24 GHz
- 14. Conclusiones del Tutorial
  - 14.1 Síntesis global
  - 14.2 Ideas clave para el profesional
  - 14.3 Próximos pasos recomendados para el lector

---

## 1. Introducción General al Tutorial

### 1.1 Motivación y Objetivos

El diseño y la planificación de redes de telecomunicaciones inalámbricas constituyen una de las disciplinas más relevantes de la ingeniería moderna. Desde las redes celulares de quinta generación (5G NR) hasta las redes de área local inalámbricas (Wi-Fi 6/6E/7), el éxito de cualquier despliegue depende de una comprensión profunda de cómo las ondas electromagnéticas se propagan a través de distintos entornos. Sin esta comprensión, el ingeniero no puede estimar con precisión el alcance de una estación base, determinar la cantidad de puntos de acceso necesarios para cubrir un edificio de oficinas, ni garantizar que los usuarios finales experimenten una calidad de servicio adecuada.

La motivación principal de este tutorial es proporcionar al lector una guía completa, rigurosa y pedagógica sobre los modelos de propagación electromagnética más utilizados en la industria y en los estándares internacionales. El objetivo no es simplemente presentar ecuaciones, sino desarrollar en el lector una intuición física sólida que le permita seleccionar, aplicar e interpretar correctamente estos modelos en escenarios reales de dimensionamiento de cobertura.

Los objetivos específicos de este tutorial son:

1. Comprender los fundamentos físicos de la propagación de ondas electromagnéticas, incluyendo los mecanismos de reflexión, difracción, dispersión y absorción.
2. Dominar los modelos empíricos y semi-empíricos de propagación en exteriores, desde el clásico Okumura-Hata hasta el modelo 3GPP TR 38.901 utilizado en el diseño de redes 5G.
3. Conocer en detalle los modelos de propagación en interiores, incluyendo la recomendación ITU-R P.1238, los modelos IEEE 802.11ax/be y las técnicas de presupuesto de enlace (*link budget*) para entornos *indoor*.
4. Aplicar estos conocimientos al dimensionamiento práctico de cobertura, realizando cálculos completos con ejemplos numéricos representativos.

### 1.2 Audiencia Objetivo

Este tutorial está dirigido a estudiantes de ingeniería de telecomunicaciones, electrónica o afines que se encuentran en los últimos semestres de su formación de pregrado o en los primeros semestres de posgrado. También resulta útil para ingenieros en ejercicio que deseen actualizar sus conocimientos en modelos de propagación modernos, particularmente aquellos relacionados con tecnologías 5G NR y Wi-Fi 6E/7.

Se asume que el lector posee conocimientos básicos de:

- Álgebra y cálculo diferencial e integral.
- Fundamentos de campos electromagnéticos (al menos un curso introductorio).
- Nociones elementales de probabilidad y estadística.
- Conceptos básicos de sistemas de comunicaciones.

No se requiere experiencia previa en planificación de redes ni en el uso de herramientas profesionales de cobertura.

### 1.3 Estructura del Documento

El presente tutorial está organizado en catorce secciones principales. Las Secciones 2 a 4 establecen los fundamentos teóricos de la propagación electromagnética y su aplicación en entornos exteriores e interiores. Las Secciones 5 a 10 recorren la evolución de las redes WiFi desde WiFi 5 hasta WiFi 8. Las Secciones 11 a 13 desarrollan el dimensionamiento avanzado, la seguridad y las tendencias futuras, mientras que la Sección 14 sintetiza las conclusiones. Cada sección incluye ejemplos numéricos detallados y descripciones de figuras que facilitan la comprensión de los conceptos presentados.

---

## 2. Fundamentos de Propagación de Ondas Electromagnéticas

### 2.1 Conceptos Básicos

#### 2.1.1 Ondas Electromagnéticas: Definición, Espectro, Longitud de Onda y Frecuencia

Una onda electromagnética es una perturbación que se propaga a través del espacio transportando energía mediante la oscilación acoplada de campos eléctricos y magnéticos mutuamente perpendiculares. A diferencia de las ondas mecánicas (como el sonido), las ondas electromagnéticas no requieren un medio material para propagarse: pueden viajar en el vacío a la velocidad de la luz.

La relación fundamental entre la frecuencia $f$, la longitud de onda $\lambda$ y la velocidad de propagación $c$ está dada por:

$$\lambda = \frac{c}{f}$$

donde:

- $\lambda$ es la longitud de onda, medida en metros (m). Representa la distancia espacial entre dos puntos consecutivos de la onda que se encuentran en la misma fase (por ejemplo, entre dos crestas consecutivas).
- $c$ es la velocidad de la luz en el vacío, cuyo valor es $c \approx 3 \times 10^8$ m/s. En medios materiales, la velocidad de propagación es menor y depende del índice de refracción del medio.
- $f$ es la frecuencia de la onda, medida en hercios (Hz). Indica el número de ciclos completos de oscilación que la onda realiza por segundo.

El espectro electromagnético abarca un rango enorme de frecuencias, desde las ondas de radio de extremadamente baja frecuencia (ELF, por debajo de 3 kHz) hasta los rayos gamma (por encima de $10^{19}$ Hz). En telecomunicaciones inalámbricas, las bandas de mayor interés son:

- **Banda UHF (300 MHz – 3 GHz):** Utilizada por redes celulares 2G, 3G, 4G y la banda baja de 5G (FR1). A 900 MHz, la longitud de onda es $\lambda = 3 \times 10^8 / 9 \times 10^8 = 0.333$ m.
- **Banda SHF (3 GHz – 30 GHz):** Incluye las bandas de Wi-Fi (5 GHz, 6 GHz) y las bandas medias y altas de 5G. A 5 GHz, $\lambda = 0.06$ m = 6 cm.
- **Banda EHF / ondas milimétricas (30 GHz – 300 GHz):** Utilizada por 5G FR2. A 28 GHz, $\lambda = 0.0107$ m $\approx$ 1.07 cm.

**[Descripción de Figura 2.1]:** *Diagrama del espectro electromagnético orientado a telecomunicaciones. Eje horizontal representando la frecuencia en escala logarítmica desde 100 MHz hasta 100 GHz. Eje vertical superior indicando la longitud de onda correspondiente (de 3 m a 3 mm). Bandas coloreadas para UHF (verde claro), SHF (azul claro) y EHF (violeta). Dentro de cada banda, marcas indicando las tecnologías que operan en ella: GSM/UMTS/LTE en UHF, Wi-Fi 5/6/6E y 5G Sub-6 en SHF, y 5G mmWave en EHF. Flechas indicando que a mayor frecuencia, menor longitud de onda y mayor atenuación por propagación.*

#### 2.1.2 Ecuaciones de Maxwell Simplificadas y su Relevancia

Las ecuaciones de Maxwell constituyen el marco teórico fundamental que describe completamente el comportamiento de los campos eléctricos y magnéticos, y por lo tanto, de todas las ondas electromagnéticas. En su forma diferencial para un medio lineal, homogéneo e isótropo, y en ausencia de fuentes (región libre de cargas y corrientes), las ecuaciones de Maxwell se reducen a:

$$\nabla \cdot \mathbf{E} = 0$$

$$\nabla \cdot \mathbf{B} = 0$$

$$\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}$$

$$\nabla \times \mathbf{B} = \mu_0 \epsilon_0 \frac{\partial \mathbf{E}}{\partial t}$$

donde:

- $\mathbf{E}$ es el vector de campo eléctrico, medido en voltios por metro (V/m). Representa la fuerza que experimentaría una carga unitaria positiva colocada en ese punto del espacio.
- $\mathbf{B}$ es el vector de densidad de flujo magnético (o inducción magnética), medido en teslas (T). Describe la componente magnética del campo electromagnético.
- $\nabla \cdot$ es el operador divergencia, que mide la tendencia de un campo vectorial a emanar de un punto (o converger hacia él).
- $\nabla \times$ es el operador rotacional, que mide la tendencia de un campo vectorial a "girar" alrededor de un punto.
- $\mu_0 = 4\pi \times 10^{-7}$ H/m es la permeabilidad magnética del vacío.
- $\epsilon_0 = 8.854 \times 10^{-12}$ F/m es la permitividad eléctrica del vacío.
- $\partial / \partial t$ denota la derivada parcial con respecto al tiempo.

La primera ecuación ($\nabla \cdot \mathbf{E} = 0$) establece que, en ausencia de cargas libres, el campo eléctrico no tiene fuentes ni sumideros puntuales: las líneas de campo eléctrico no comienzan ni terminan en el espacio libre. La segunda ecuación ($\nabla \cdot \mathbf{B} = 0$) expresa el hecho experimental de que no existen monopolos magnéticos: las líneas de campo magnético siempre forman bucles cerrados.

La tercera ecuación (ley de Faraday) establece que un campo magnético que varía en el tiempo genera un campo eléctrico rotacional. La cuarta ecuación (ley de Ampère-Maxwell) establece el fenómeno recíproco: un campo eléctrico que varía en el tiempo genera un campo magnético rotacional. Es precisamente este acoplamiento mutuo entre los campos eléctrico y magnético lo que permite la existencia de ondas electromagnéticas que se autosostienen y se propagan a través del espacio.

A partir de estas ecuaciones, combinándolas mediante manipulación vectorial, se obtiene la ecuación de onda para el campo eléctrico en el vacío:

$$\nabla^2 \mathbf{E} = \mu_0 \epsilon_0 \frac{\partial^2 \mathbf{E}}{\partial t^2}$$

Esta ecuación de onda demuestra que las perturbaciones del campo eléctrico se propagan como ondas con velocidad:

$$c = \frac{1}{\sqrt{\mu_0 \epsilon_0}} = \frac{1}{\sqrt{4\pi \times 10^{-7} \times 8.854 \times 10^{-12}}} \approx 3 \times 10^8 \text{ m/s}$$

Este resultado, obtenido teóricamente por James Clerk Maxwell en 1865, fue una de las predicciones más profundas de la física: la velocidad de propagación de las ondas electromagnéticas coincide con la velocidad de la luz medida experimentalmente, lo que llevó a Maxwell a proponer que la luz misma es una onda electromagnética.

Para los propósitos de la ingeniería de propagación, las ecuaciones de Maxwell proporcionan la base teórica que justifica todos los fenómenos que estudiaremos (reflexión, difracción, dispersión), aunque en la práctica utilizaremos modelos empíricos simplificados que capturan los efectos dominantes sin necesidad de resolver las ecuaciones completas.

#### 2.1.3 Potencia Radiada, PIRE y Ganancia de Antena

En un sistema de comunicaciones inalámbrico, la estación transmisora convierte la señal eléctrica en una onda electromagnética mediante una antena. No toda la potencia entregada a la antena se convierte en radiación útil; existen pérdidas en los cables de conexión, conectores y en la propia antena. Para caracterizar la emisión de un transmisor, se definen varios conceptos fundamentales.

La **potencia de transmisión** $P_T$ es la potencia eléctrica que el transmisor entrega a la entrada de la antena, típicamente medida en vatios (W) o en decibelios referidos a un milivatio (dBm):

$$P_{T,\text{dBm}} = 10 \log_{10}\left(\frac{P_T}{1 \text{ mW}}\right)$$

Por ejemplo, un transmisor que entrega $P_T = 1$ W tiene una potencia de $P_{T,\text{dBm}} = 10 \log_{10}(1000) = 30$ dBm. Un transmisor Wi-Fi típico con $P_T = 100$ mW tiene $P_{T,\text{dBm}} = 10 \log_{10}(100) = 20$ dBm.

La **ganancia de antena** $G_T$ describe la capacidad de la antena para concentrar la energía radiada en una dirección particular, en comparación con una antena isotrópica (hipotética antena que radia uniformemente en todas las direcciones). Se expresa en decibelios referidos a una antena isotrópica (dBi):

$$G_{T,\text{dBi}} = 10 \log_{10}\left(\frac{U(\theta, \phi)}{U_{\text{iso}}}\right)$$

donde $U(\theta, \phi)$ es la intensidad de radiación de la antena en la dirección $(\theta, \phi)$ y $U_{\text{iso}} = P_T / (4\pi)$ es la intensidad de radiación uniforme de una antena isotrópica. Una antena dipolo de media onda tiene una ganancia máxima de aproximadamente 2.15 dBi, mientras que una antena sectorial de estación base celular puede tener una ganancia de 15 a 18 dBi.

La **Potencia Isotrópica Radiada Equivalente (PIRE)**, conocida en inglés como *Equivalent Isotropically Radiated Power (EIRP)*, es la potencia que debería radiar una antena isotrópica para producir la misma densidad de potencia que la antena real en la dirección de máxima radiación:

$$\text{PIRE} = P_T \cdot G_T$$

En decibelios:

$$\text{PIRE}_{\text{dBm}} = P_{T,\text{dBm}} + G_{T,\text{dBi}}$$

La PIRE es un parámetro fundamental en la planificación de redes, ya que los organismos reguladores especifican límites de PIRE para cada banda de frecuencias. Por ejemplo, si un punto de acceso Wi-Fi opera con $P_T = 20$ dBm y utiliza una antena con $G_T = 6$ dBi, la PIRE es $20 + 6 = 26$ dBm.

La **densidad de potencia** $S$ a una distancia $d$ de una antena isotrópica que radia una potencia $P_T$ se obtiene distribuyendo la potencia uniformemente sobre la superficie de una esfera de radio $d$:

$$S = \frac{P_T \cdot G_T}{4\pi d^2} \quad \text{[W/m}^2\text{]}$$

Esta expresión es fundamental porque conecta la potencia transmitida con la intensidad de la señal en el receptor, y será la base para derivar la ecuación de transmisión de Friis en secciones posteriores.

### 2.2 Mecanismos de Propagación a Gran Escala

Cuando una onda electromagnética viaja desde un transmisor hacia un receptor en un entorno real (urbano, suburbano, rural o interior), interactúa con los objetos presentes en el medio: edificios, vehículos, árboles, terreno, muebles, paredes, etc. Estas interacciones modifican la amplitud, fase, dirección y polarización de la onda. Los mecanismos fundamentales de interacción son la reflexión, la difracción, la dispersión (*scattering*) y la absorción. Comprender estos mecanismos es esencial para interpretar correctamente los modelos de propagación que se presentarán en las secciones siguientes.

#### 2.2.1 Reflexión

La reflexión ocurre cuando una onda electromagnética incide sobre una superficie cuyas dimensiones son mucho mayores que la longitud de onda de la señal. En este caso, parte de la energía de la onda es reflejada de regreso al medio original, y parte es transmitida (refractada) hacia el segundo medio. Este fenómeno es particularmente relevante en entornos urbanos, donde las fachadas de los edificios, el suelo, las superficies acristaladas y las estructuras metálicas actúan como reflectores eficientes.

**Ley de Snell de la reflexión y la refracción:**

Cuando una onda electromagnética incide sobre la interfaz plana entre dos medios con índices de refracción $n_1$ y $n_2$, se cumple la ley de Snell:

$$n_1 \sin(\theta_i) = n_2 \sin(\theta_t)$$

donde:

- $\theta_i$ es el ángulo de incidencia, medido desde la normal a la superficie. Es el ángulo que forma el rayo incidente con la perpendicular a la superficie en el punto de incidencia.
- $\theta_t$ es el ángulo de transmisión (o refracción), medido desde la misma normal. Es el ángulo que forma el rayo transmitido con la perpendicular a la superficie.
- $n_1$ es el índice de refracción del primer medio (del cual proviene la onda). Para el aire, $n_1 \approx 1$.
- $n_2$ es el índice de refracción del segundo medio. Para vidrio común, $n_2 \approx 1.5$; para hormigón, $n_2 \approx 2.3$ a frecuencias de microondas.

Además, el ángulo de reflexión $\theta_r$ es igual al ángulo de incidencia: $\theta_r = \theta_i$.

**Coeficientes de reflexión de Fresnel:**

La fracción de energía reflejada depende de la polarización de la onda, del ángulo de incidencia y de las propiedades electromagnéticas de los medios. Los coeficientes de reflexión de Fresnel cuantifican esta fracción para las dos polarizaciones lineales fundamentales.

Para la **polarización perpendicular** (TE, campo eléctrico perpendicular al plano de incidencia):

$$\Gamma_{\perp} = \frac{n_1 \cos(\theta_i) - n_2 \cos(\theta_t)}{n_1 \cos(\theta_i) + n_2 \cos(\theta_t)}$$

Para la **polarización paralela** (TM, campo eléctrico en el plano de incidencia):

$$\Gamma_{\parallel} = \frac{n_2 \cos(\theta_i) - n_1 \cos(\theta_t)}{n_2 \cos(\theta_i) + n_1 \cos(\theta_t)}$$

donde $\theta_t$ se obtiene de la ley de Snell. El coeficiente de reflexión $\Gamma$ es un número adimensional que puede tomar valores entre $-1$ y $+1$. Su magnitud al cuadrado, $|\Gamma|^2$, representa la fracción de potencia incidente que es reflejada (reflectancia). La fracción transmitida es $1 - |\Gamma|^2$.

**Ejemplo numérico 2.1:** Una onda electromagnética a 2.4 GHz ($\lambda = 0.125$ m) incide sobre una pared de hormigón con un ángulo de $\theta_i = 30°$. El índice de refracción del hormigón a esta frecuencia es aproximadamente $n_2 = 2.3$ (el aire tiene $n_1 = 1.0$).

Paso 1: Calcular el ángulo de transmisión usando la ley de Snell:

$$\sin(\theta_t) = \frac{n_1}{n_2}\sin(\theta_i) = \frac{1.0}{2.3}\sin(30°) = \frac{0.5}{2.3} = 0.2174$$

$$\theta_t = \arcsin(0.2174) = 12.56°$$

Paso 2: Calcular el coeficiente de reflexión para polarización perpendicular:

$$\Gamma_{\perp} = \frac{1.0 \times \cos(30°) - 2.3 \times \cos(12.56°)}{1.0 \times \cos(30°) + 2.3 \times \cos(12.56°)}$$

$$\Gamma_{\perp} = \frac{0.866 - 2.3 \times 0.976}{0.866 + 2.3 \times 0.976} = \frac{0.866 - 2.245}{0.866 + 2.245} = \frac{-1.379}{3.111} = -0.443$$

La potencia reflejada es $|\Gamma_{\perp}|^2 = 0.443^2 = 0.196$, es decir, aproximadamente el 19.6% de la potencia incidente se refleja y el 80.4% se transmite hacia el interior de la pared (donde sufrirá atenuación adicional al atravesarla).

**[Descripción de Figura 2.2]:** *Diagrama que ilustra la reflexión y refracción de una onda electromagnética en la interfaz entre aire y hormigón. A la izquierda, el medio 1 (aire, $n_1 = 1.0$) con un rayo incidente que forma un ángulo $\theta_i = 30°$ con la línea normal (punteada, perpendicular a la superficie). Se muestra el rayo reflejado saliendo con el mismo ángulo $\theta_r = 30°$ al otro lado de la normal. A la derecha, el medio 2 (hormigón, $n_2 = 2.3$) con el rayo transmitido formando un ángulo $\theta_t = 12.56°$ con la normal. Flechas indicando la amplitud relativa de cada rayo: el rayo reflejado más delgado (19.6% de potencia) y el transmitido más grueso (80.4% de potencia). Vectores de campo eléctrico $\mathbf{E}$ y magnético $\mathbf{H}$ indicados en cada rayo.*

#### 2.2.2 Difracción

La difracción es el fenómeno por el cual las ondas electromagnéticas pueden rodear obstáculos y alcanzar regiones que no están en línea de visión directa (*Non-Line-of-Sight, NLoS*) con el transmisor. Este mecanismo es crucial en entornos urbanos, donde edificios, colinas y otras estructuras bloquean parcialmente la trayectoria directa entre el transmisor y el receptor.

**Principio de Huygens-Fresnel:**

El fundamento teórico de la difracción es el principio de Huygens (formulado por Christiaan Huygens en 1678 y formalizado matemáticamente por Augustin-Jean Fresnel en 1818). Este principio establece que cada punto de un frente de onda puede considerarse como una fuente puntual de ondas esféricas secundarias. La onda en cualquier punto posterior del espacio es el resultado de la superposición (interferencia) de todas estas ondas secundarias.

**Modelo de difracción de Fresnel – Zona de Fresnel:**

Para analizar la difracción de manera cuantitativa, se utiliza el concepto de zonas de Fresnel. Considérese un enlace de radio entre un transmisor T y un receptor R separados una distancia $d$. Las zonas de Fresnel son regiones elipsoidales concéntricas alrededor de la línea de visión directa T-R. La $n$-ésima zona de Fresnel está definida como el lugar geométrico de todos los puntos P tales que la diferencia entre la trayectoria T-P-R y la trayectoria directa T-R es exactamente $n\lambda/2$:

$$|TP| + |PR| - |TR| = \frac{n\lambda}{2}$$

El radio de la $n$-ésima zona de Fresnel a una distancia $d_1$ del transmisor (y $d_2 = d - d_1$ del receptor) se calcula como:

$$r_n = \sqrt{\frac{n \lambda \, d_1 \, d_2}{d_1 + d_2}}$$

donde:

- $r_n$ es el radio de la $n$-ésima zona de Fresnel en metros.
- $n$ es el número de la zona (1, 2, 3, ...).
- $\lambda$ es la longitud de onda de la señal en metros.
- $d_1$ es la distancia desde el transmisor al punto de observación en metros.
- $d_2$ es la distancia desde el punto de observación al receptor en metros.

La primera zona de Fresnel ($n = 1$) es la más importante desde el punto de vista práctico. Se considera que un enlace de radio tiene despejamiento adecuado (sin difracción significativa) cuando al menos el 60% del radio de la primera zona de Fresnel está libre de obstáculos. Si un obstáculo penetra en la primera zona de Fresnel, se produce una pérdida adicional por difracción que puede ser significativa.

**Ejemplo numérico 2.2:** Calcular el radio de la primera zona de Fresnel en el punto medio de un enlace punto a punto de 2 km a una frecuencia de 2.4 GHz.

Datos: $f = 2.4$ GHz, $d = 2000$ m, punto medio: $d_1 = d_2 = 1000$ m.

Paso 1: Calcular la longitud de onda:

$$\lambda = \frac{c}{f} = \frac{3 \times 10^8}{2.4 \times 10^9} = 0.125 \text{ m}$$

Paso 2: Calcular el radio de la primera zona de Fresnel ($n = 1$):

$$r_1 = \sqrt{\frac{1 \times 0.125 \times 1000 \times 1000}{1000 + 1000}} = \sqrt{\frac{125000}{2000}} = \sqrt{62.5} = 7.91 \text{ m}$$

Esto significa que en el punto medio del enlace, cualquier obstáculo (edificio, árbol, colina) debe estar al menos a $0.6 \times 7.91 = 4.74$ m por debajo de la línea de visión directa para no causar pérdidas significativas por difracción.

Para el modelo de difracción de borde afilado (*knife-edge diffraction*), la pérdida por difracción se puede estimar utilizando el parámetro de Fresnel-Kirchhoff $\nu$:

$$\nu = h \sqrt{\frac{2(d_1 + d_2)}{\lambda \, d_1 \, d_2}}$$

donde $h$ es la altura efectiva del obstáculo por encima de la línea de visión directa (positiva si el obstáculo sobresale, negativa si está por debajo). La pérdida por difracción en dB se aproxima como:

$$L_{\text{diff}} \approx \begin{cases} 0 \text{ dB} & \text{si } \nu \leq -1 \\ 20 \log_{10}(0.5 - 0.62\nu) & \text{si } -1 < \nu \leq 0 \\ 20 \log_{10}(0.5 \, e^{-0.95\nu}) & \text{si } 0 < \nu \leq 1 \\ 20 \log_{10}\left(\frac{0.4}{\sqrt{0.1184 + (0.38 - 0.1\nu)^2}}\right) & \text{si } 1 < \nu \leq 2.4 \\ 20 \log_{10}\left(\frac{0.225}{\nu}\right) & \text{si } \nu > 2.4 \end{cases}$$

**[Descripción de Figura 2.3]:** *Diagrama que ilustra las zonas de Fresnel entre un transmisor T (a la izquierda) y un receptor R (a la derecha), separados una distancia $d$. Vista lateral mostrando la línea de visión directa como una línea horizontal central. Tres elipses concéntricas alrededor de esta línea representan la primera (sombreada en verde claro), segunda (amarillo) y tercera (naranja) zonas de Fresnel. Las etiquetas $r_1$, $r_2$, $r_3$ indican los radios de cada zona en el punto medio. Un edificio parcialmente obstruyendo la primera zona de Fresnel, con una flecha indicando la altura $h$ del edificio por encima de la línea de visión. Los parámetros $d_1$ y $d_2$ están marcados como las distancias del transmisor y receptor al obstáculo, respectivamente.*

#### 2.2.3 Dispersión (Scattering)

La dispersión, o *scattering*, ocurre cuando una onda electromagnética incide sobre un objeto cuyas dimensiones son comparables o menores que la longitud de onda. A diferencia de la reflexión (que ocurre en superficies lisas y extensas), la dispersión redistribuye la energía de la onda en múltiples direcciones. Este fenómeno es particularmente relevante cuando la señal interactúa con objetos como postes de iluminación, señales de tráfico, follaje de árboles, cables aéreos y superficies rugosas.

La dispersión se clasifica en función de la relación entre el tamaño del objeto dispersor y la longitud de onda:

- **Dispersión de Rayleigh:** Ocurre cuando el tamaño del objeto es mucho menor que la longitud de onda ($a \ll \lambda$, donde $a$ es la dimensión característica del objeto). La intensidad de la dispersión es proporcional a $f^4$, lo que significa que las frecuencias más altas se dispersan mucho más que las frecuencias bajas. Este tipo de dispersión es relevante, por ejemplo, para gotas de lluvia a frecuencias por debajo de unos 10 GHz.

- **Dispersión de Mie:** Ocurre cuando el tamaño del objeto es comparable a la longitud de onda ($a \approx \lambda$). La distribución angular de la energía dispersada es más compleja y depende fuertemente de la forma y composición del objeto.

- **Dispersión geométrica (óptica):** Ocurre cuando el tamaño del objeto es mucho mayor que la longitud de onda ($a \gg \lambda$). En este régimen, la dispersión se describe mejor mediante las leyes de la óptica geométrica (reflexión y refracción).

En la planificación de redes urbanas, la dispersión por superficies rugosas es relevante. El criterio de Rayleigh establece que una superficie se considera rugosa si la variación de altura $\Delta h$ de la superficie satisface:

$$\Delta h > \frac{\lambda}{8 \cos(\theta_i)}$$

donde $\theta_i$ es el ángulo de incidencia. Si la superficie es rugosa según este criterio, la reflexión especular se atenúa y una parte significativa de la energía se dispersa en múltiples direcciones.

**[Descripción de Figura 2.4]:** *Tres paneles que ilustran los tipos de dispersión. Panel izquierdo: "Dispersión de Rayleigh" — una onda incidente (flecha azul) golpea una partícula pequeña (círculo rojo, con etiqueta $a \ll \lambda$), y flechas de dispersión distribuidas de manera simétrica hacia adelante y atrás. Panel central: "Dispersión de Mie" — la onda incide sobre una partícula de tamaño comparable a $\lambda$, con un lóbulo de dispersión predominante hacia adelante y lóbulos laterales más pequeños. Panel derecho: "Dispersión por superficie rugosa" — una onda incidente sobre una superficie irregular, con múltiples rayos reflejados en direcciones diferentes (a diferencia de la reflexión especular en una superficie lisa, que se muestra como referencia con línea punteada).*

#### 2.2.4 Absorción Atmosférica

La absorción atmosférica es el mecanismo por el cual las moléculas de los gases constituyentes de la atmósfera (principalmente oxígeno O$_2$ y vapor de agua H$_2$O) absorben energía de la onda electromagnética, convirtiéndola en calor. Este efecto es despreciable a frecuencias por debajo de aproximadamente 10 GHz y para distancias cortas, pero se vuelve significativo en las bandas de ondas milimétricas utilizadas por 5G FR2.

Los picos de absorción más relevantes son:

- **Vapor de agua (H$_2$O):** Picos de absorción a 22.2 GHz y 183.3 GHz. A 22.2 GHz, la atenuación es de aproximadamente 0.2 dB/km en condiciones estándar de humedad.
- **Oxígeno (O$_2$):** Pico de absorción a 60 GHz, donde la atenuación puede alcanzar 15-16 dB/km. A 28 GHz (banda candidata de 5G mmWave), la atenuación atmosférica es de solo aproximadamente 0.07 dB/km, lo que hace que esta banda sea viable para comunicaciones terrestres en distancias cortas.

La atenuación atmosférica total $A_a$ (en dB) para un enlace de longitud $d$ (en km) se calcula como:

$$A_a = \gamma_a \cdot d$$

donde $\gamma_a$ es el coeficiente de atenuación específica en dB/km, que depende de la frecuencia, la temperatura, la presión y la humedad. Los valores detallados se encuentran en la Recomendación ITU-R P.676.

La atenuación por lluvia es otro factor importante en bandas de ondas milimétricas. La Recomendación ITU-R P.838 proporciona un modelo para estimar la atenuación específica por lluvia $\gamma_R$ (en dB/km):

$$\gamma_R = k \cdot R^{\alpha}$$

donde $R$ es la tasa de lluvia en mm/h, y $k$ y $\alpha$ son coeficientes que dependen de la frecuencia y la polarización. A 28 GHz, para una lluvia intensa de $R = 50$ mm/h, la atenuación puede ser del orden de 10 dB/km.

### 2.3 Modelado de Pérdida de Trayectoria (Path Loss)

#### 2.3.1 Modelo de Espacio Libre (Ecuación de Friis)

El modelo más fundamental de propagación es el de espacio libre, que describe la atenuación de la señal cuando la onda viaja en un medio sin obstáculos, reflexiones ni otros efectos. Aunque esta situación ideal rara vez se da en la práctica (quizás solo en enlaces satelitales o comunicaciones en el espacio profundo), la ecuación de Friis constituye el punto de partida y la referencia contra la cual se comparan todos los demás modelos.

**Derivación completa:**

Considérese un transmisor con potencia $P_T$ y ganancia de antena $G_T$. La densidad de potencia a una distancia $d$ del transmisor es:

$$S = \frac{P_T \cdot G_T}{4\pi d^2}$$

La antena receptora captura esta densidad de potencia a través de su área efectiva $A_e$. La relación entre la ganancia de la antena receptora $G_R$ y su área efectiva es:

$$A_e = \frac{G_R \lambda^2}{4\pi}$$

Esta ecuación fundamental de la teoría de antenas establece que el área efectiva de una antena es proporcional a su ganancia y al cuadrado de la longitud de onda. A frecuencias más altas (longitudes de onda más cortas), una antena con la misma ganancia tiene un área efectiva menor.

La potencia recibida $P_R$ es el producto de la densidad de potencia por el área efectiva:

$$P_R = S \cdot A_e = \frac{P_T \cdot G_T}{4\pi d^2} \cdot \frac{G_R \lambda^2}{4\pi} = P_T G_T G_R \left(\frac{\lambda}{4\pi d}\right)^2$$

Esta es la **ecuación de transmisión de Friis**. Reordenando:

$$\frac{P_R}{P_T} = G_T G_R \left(\frac{\lambda}{4\pi d}\right)^2$$

La **pérdida de propagación en espacio libre (FSPL)** se define como la atenuación sufrida por la señal considerando antenas isotrópicas ($G_T = G_R = 1$):

$$\text{FSPL} = \left(\frac{4\pi d}{\lambda}\right)^2$$

Expresada en decibelios:

$$\text{FSPL}_{\text{dB}} = 10 \log_{10}\left(\frac{4\pi d}{\lambda}\right)^2 = 20 \log_{10}\left(\frac{4\pi d}{\lambda}\right)$$

Sustituyendo $\lambda = c/f$:

$$\text{FSPL}_{\text{dB}} = 20 \log_{10}(d) + 20 \log_{10}(f) + 20 \log_{10}\left(\frac{4\pi}{c}\right)$$

Evaluando la constante con $d$ en metros y $f$ en Hz:

$$20 \log_{10}\left(\frac{4\pi}{3 \times 10^8}\right) = 20 \log_{10}(4.189 \times 10^{-8}) = -147.56 \text{ dB}$$

Si expresamos $d$ en kilómetros y $f$ en MHz, la ecuación se simplifica a la forma más conocida:

$$\boxed{\text{FSPL}_{\text{dB}} = 32.44 + 20 \log_{10}(d_{\text{km}}) + 20 \log_{10}(f_{\text{MHz}})}$$

Es importante comprender el significado físico de esta ecuación. La FSPL no representa una absorción de energía por el medio (en el espacio libre no hay absorción). Representa la atenuación geométrica debida a la expansión esférica del frente de onda: a medida que la onda se aleja del transmisor, la misma potencia se distribuye sobre una superficie esférica cada vez mayor, por lo que la densidad de potencia disminuye con el cuadrado de la distancia. El término que depende de la frecuencia refleja la dependencia del área efectiva de la antena receptora con $\lambda^2$.

**Ejemplo numérico 2.3:** Calcular la potencia recibida en un enlace Wi-Fi a 5 GHz con las siguientes condiciones: $P_T = 20$ dBm, $G_T = 3$ dBi, $G_R = 0$ dBi, distancia $d = 50$ m, en condiciones de espacio libre.

Paso 1: Calcular la FSPL:

$$\text{FSPL}_{\text{dB}} = 32.44 + 20 \log_{10}(0.05) + 20 \log_{10}(5000)$$

$$= 32.44 + 20 \times (-1.301) + 20 \times 3.699$$

$$= 32.44 - 26.02 + 73.98 = 80.40 \text{ dB}$$

Paso 2: Calcular la potencia recibida usando la ecuación de enlace (*link budget*):

$$P_R = P_T + G_T + G_R - \text{FSPL}$$

$$P_R = 20 + 3 + 0 - 80.40 = -57.40 \text{ dBm}$$

Este resultado indica que a 50 metros en espacio libre, un receptor Wi-Fi recibiría $-57.40$ dBm, un nivel que proporciona una señal excelente (la sensibilidad típica de un receptor Wi-Fi 802.11ac/ax es del orden de $-70$ a $-85$ dBm, dependiendo del MCS utilizado).

#### 2.3.2 Modelo General de Pérdida de Trayectoria

En entornos reales, la señal recibida fluctúa significativamente respecto al valor predicho por el modelo de espacio libre. Los edificios, el terreno, la vegetación y otros obstáculos causan reflexiones, difracciones y dispersiones que pueden atenuar o, en algunos casos, reforzar la señal. Para capturar estas variaciones, la pérdida de trayectoria total se modela como la suma de una componente determinista media y una componente aleatoria:

$$PL(d) \text{ [dB]} = \overline{PL}(d) + X_{\sigma}$$

donde:

- $PL(d)$ es la pérdida de trayectoria total a una distancia $d$, en dB.
- $\overline{PL}(d)$ es la pérdida de trayectoria media (o mediana), que depende determinísticamente de la distancia y que predicen los modelos de propagación empíricos como Okumura-Hata o COST-231.
- $X_{\sigma}$ es una variable aleatoria de media cero que modela las fluctuaciones de gran escala (*large-scale fading* o *shadowing*) debidas al sombreado por obstáculos. Se modela como una variable aleatoria gaussiana (normal) con media cero y desviación estándar $\sigma$ (en dB).

La pérdida de trayectoria media se puede expresar de forma general mediante un modelo exponencial:

$$\overline{PL}(d) \text{ [dB]} = \overline{PL}(d_0) + 10n \log_{10}\left(\frac{d}{d_0}\right)$$

donde:

- $\overline{PL}(d_0)$ es la pérdida de trayectoria medida o calculada a una distancia de referencia $d_0$ (típicamente $d_0 = 1$ m para interiores o $d_0 = 1$ km para exteriores).
- $n$ es el **exponente de pérdida de trayectoria** (*path loss exponent*), que caracteriza la tasa a la cual la señal se atenúa con la distancia. En espacio libre, $n = 2$. En entornos urbanos densos, $n$ puede variar entre 2.7 y 5. En interiores, depende del tipo de edificio, con valores típicos entre 1.6 (corredores con efecto de guía de onda) y 6 (ambientes con múltiples pisos y paredes).

#### 2.3.3 Desvanecimiento por Sombra (Shadowing Log-Normal)

El término $X_{\sigma}$ en el modelo general de pérdida de trayectoria captura las variaciones de la señal causadas por el *shadowing* (sombreado), es decir, la presencia variable de obstáculos grandes (edificios, colinas) entre el transmisor y el receptor en diferentes ubicaciones. Cuando un móvil se desplaza a lo largo de una ruta en un entorno urbano, la señal recibida varía lentamente a medida que pasa detrás de edificios o emerge a zonas más abiertas.

Extensas campañas de medición han demostrado que estas variaciones de la señal, expresadas en dB, siguen una distribución gaussiana (normal). Esto equivale a decir que la potencia recibida (en unidades lineales, como mW) sigue una distribución log-normal. Por esta razón, el fenómeno se denomina **desvanecimiento log-normal** o *log-normal shadowing*.

La función de densidad de probabilidad de $X_{\sigma}$ es:

$$f_{X_{\sigma}}(x) = \frac{1}{\sigma\sqrt{2\pi}} \exp\left(-\frac{x^2}{2\sigma^2}\right)$$

donde $\sigma$ es la desviación estándar del shadowing, medida en dB. Los valores típicos de $\sigma$ son:

- **Entornos urbanos macro-celulares:** $\sigma = 6$ a 10 dB.
- **Entornos suburbanos:** $\sigma = 4$ a 8 dB.
- **Entornos interiores:** $\sigma = 3$ a 6 dB.

**Margen de desvanecimiento (*fade margin*):**

En la planificación de redes, es necesario garantizar que la señal recibida sea superior al umbral mínimo de sensibilidad del receptor durante un porcentaje determinado del tiempo y del área de cobertura. Para ello, se añade un margen de desvanecimiento $M_{\text{fade}}$ al presupuesto de enlace.

Si se desea que la probabilidad de que la señal esté por encima del umbral sea $P_{\text{cob}}$ (por ejemplo, 90% o 95%), el margen de desvanecimiento se calcula como:

$$M_{\text{fade}} = Q^{-1}(1 - P_{\text{cob}}) \cdot \sigma$$

donde $Q^{-1}$ es la función inversa de la función Q (complementaria de la distribución normal acumulada). Para probabilidades de cobertura comunes:

| Probabilidad de cobertura $P_{\text{cob}}$ | $Q^{-1}(1 - P_{\text{cob}})$ | Margen ($\sigma = 8$ dB) |
|:---:|:---:|:---:|
| 50% | 0 | 0 dB |
| 75% | 0.674 | 5.4 dB |
| 90% | 1.282 | 10.3 dB |
| 95% | 1.645 | 13.2 dB |
| 99% | 2.326 | 18.6 dB |

**Ejemplo numérico 2.4:** Una estación base celular debe proporcionar cobertura con una probabilidad del 90% en el borde de la celda. La desviación estándar del shadowing es $\sigma = 8$ dB. ¿Cuál es el margen de desvanecimiento necesario?

$$M_{\text{fade}} = 1.282 \times 8 = 10.26 \text{ dB}$$

Esto significa que la potencia de la señal media en el borde de la celda debe ser 10.26 dB superior al nivel mínimo de sensibilidad del receptor para garantizar que el 90% de las ubicaciones en el borde de la celda tengan una señal adecuada.

---

## 3. Modelos de Propagación en Exteriores

### 3.1 Modelo Okumura-Hata

#### 3.1.1 Contexto Histórico

El modelo de Okumura-Hata es uno de los modelos empíricos de propagación más ampliamente utilizados en la planificación de redes celulares. Su desarrollo se remonta a las extensas campañas de medición realizadas por Yoshihisa Okumura y sus colaboradores en la ciudad de Tokio durante la década de 1960. Okumura realizó mediciones detalladas de la intensidad de señal en la banda de 100 MHz a 3 GHz a diversas distancias de estaciones base con diferentes alturas de antena. Los resultados, publicados en 1968, se presentaron en forma de curvas gráficas de atenuación media relativa al espacio libre, parametrizadas por frecuencia, distancia, alturas de antena y tipo de entorno.

En 1980, Masaharu Hata formuló una serie de ecuaciones empíricas que aproximaban las curvas gráficas de Okumura, facilitando enormemente su implementación computacional. Estas ecuaciones, conocidas colectivamente como el modelo Okumura-Hata, se convirtieron rápidamente en el estándar de la industria para la planificación de redes celulares en la banda de 150 MHz a 1500 MHz.

#### 3.1.2 Ecuación del Modelo Okumura-Hata

La ecuación de pérdida de trayectoria media del modelo Okumura-Hata para entornos urbanos es:

$$L_{\text{urbano}} \text{ [dB]} = 69.55 + 26.16 \log_{10}(f) - 13.82 \log_{10}(h_b) - a(h_m) + \left[44.9 - 6.55 \log_{10}(h_b)\right] \log_{10}(d)$$

donde:

- $L_{\text{urbano}}$ es la pérdida de trayectoria mediana en entorno urbano, en dB.
- $f$ es la frecuencia de la portadora en MHz. Rango de validez: $150 \leq f \leq 1500$ MHz.
- $h_b$ es la altura efectiva de la antena de la estación base sobre el nivel del suelo, en metros. Rango de validez: $30 \leq h_b \leq 200$ m.
- $h_m$ es la altura de la antena del terminal móvil sobre el nivel del suelo, en metros. Rango de validez: $1 \leq h_m \leq 10$ m.
- $d$ es la distancia entre la estación base y el terminal móvil, en kilómetros. Rango de validez: $1 \leq d \leq 20$ km.
- $a(h_m)$ es el factor de corrección por altura de la antena del móvil, que depende del tipo de entorno.

Analicemos cada término de la ecuación:

- **$69.55$:** Constante de referencia que calibra el modelo al entorno urbano de Tokio.
- **$26.16 \log_{10}(f)$:** Término que captura el aumento de la pérdida con la frecuencia. A mayor frecuencia, mayor atenuación, ya que las ondas de mayor frecuencia sufren más difracción y dispersión.
- **$-13.82 \log_{10}(h_b)$:** Término que modela la reducción de la pérdida al aumentar la altura de la estación base. Una antena más alta "ve" por encima de más obstáculos, mejorando el enlace.
- **$-a(h_m)$:** Factor de corrección que refleja el beneficio de elevar la antena del terminal móvil.
- **$[44.9 - 6.55 \log_{10}(h_b)] \log_{10}(d)$:** Término que describe cómo la pérdida aumenta con la distancia. El exponente de pérdida de trayectoria efectivo depende de $h_b$.

#### 3.1.3 Factor de Corrección $a(h_m)$

El factor de corrección $a(h_m)$ varía según el tamaño de la ciudad:

**Para ciudades medianas y pequeñas:**

$$a(h_m) = (1.1 \log_{10}(f) - 0.7)h_m - (1.56 \log_{10}(f) - 0.8) \quad \text{[dB]}$$

**Para ciudades grandes (a frecuencias $f \leq 300$ MHz):**

$$a(h_m) = 8.29 [\log_{10}(1.54 \, h_m)]^2 - 1.1 \quad \text{[dB]}$$

**Para ciudades grandes (a frecuencias $f \geq 300$ MHz):**

$$a(h_m) = 3.2 [\log_{10}(11.75 \, h_m)]^2 - 4.97 \quad \text{[dB]}$$

Para entornos suburbanos, la pérdida se corrige como:

$$L_{\text{suburbano}} = L_{\text{urbano}} - 2\left[\log_{10}\left(\frac{f}{28}\right)\right]^2 - 5.4 \quad \text{[dB]}$$

Para entornos rurales abiertos:

$$L_{\text{rural}} = L_{\text{urbano}} - 4.78 [\log_{10}(f)]^2 + 18.33 \log_{10}(f) - 40.94 \quad \text{[dB]}$$

#### 3.1.4 Ejemplo Numérico Completo

**Ejemplo 3.1 (Ciudad mediana):** Calcular la pérdida de trayectoria para un enlace celular GSM 900 con los siguientes parámetros: $f = 900$ MHz, $h_b = 40$ m, $h_m = 1.5$ m, $d = 5$ km, en una ciudad mediana.

Paso 1: Calcular el factor de corrección $a(h_m)$ para ciudad mediana:

$$a(h_m) = (1.1 \log_{10}(900) - 0.7) \times 1.5 - (1.56 \log_{10}(900) - 0.8)$$

$$= (1.1 \times 2.954 - 0.7) \times 1.5 - (1.56 \times 2.954 - 0.8)$$

$$= (3.250 - 0.7) \times 1.5 - (4.608 - 0.8)$$

$$= 2.550 \times 1.5 - 3.808 = 3.825 - 3.808 = 0.017 \text{ dB}$$

Paso 2: Calcular cada término de la ecuación principal:

$$69.55 + 26.16 \log_{10}(900) = 69.55 + 26.16 \times 2.954 = 69.55 + 77.28 = 146.83$$

$$13.82 \log_{10}(40) = 13.82 \times 1.602 = 22.14$$

$$[44.9 - 6.55 \log_{10}(40)] \log_{10}(5) = [44.9 - 6.55 \times 1.602] \times 0.699$$

$$= [44.9 - 10.49] \times 0.699 = 34.41 \times 0.699 = 24.06$$

Paso 3: Calcular la pérdida total:

$$L_{\text{urbano}} = 146.83 - 22.14 - 0.017 + 24.06 = 148.73 \text{ dB}$$

**Ejemplo 3.2 (Gran ciudad):** Con los mismos parámetros pero para una gran ciudad ($f = 900$ MHz $\geq 300$ MHz):

$$a(h_m) = 3.2[\log_{10}(11.75 \times 1.5)]^2 - 4.97$$

$$= 3.2[\log_{10}(17.625)]^2 - 4.97 = 3.2 \times [1.246]^2 - 4.97$$

$$= 3.2 \times 1.553 - 4.97 = 4.97 - 4.97 = 0.0 \text{ dB}$$

En este caso, la pérdida para gran ciudad resulta:

$$L_{\text{urbano}} = 146.83 - 22.14 - 0.0 + 24.06 = 148.75 \text{ dB}$$

La diferencia entre ciudad mediana y gran ciudad es mínima para $h_m = 1.5$ m, pero se hace más significativa para alturas de antena del móvil mayores.

#### 3.1.5 Limitaciones del Modelo

El modelo Okumura-Hata tiene las siguientes limitaciones importantes:

1. **Rango de frecuencia limitado:** Solo es válido para $150 \leq f \leq 1500$ MHz. No es aplicable a redes 3G UMTS (2100 MHz), LTE en bandas altas ni 5G.
2. **Distancia mínima de 1 km:** No es adecuado para microceldas o picoceldas, donde las distancias son menores.
3. **Basado en un entorno específico:** Las mediciones originales se realizaron en Tokio, una ciudad con características urbanas particulares (edificios de alturas relativamente uniformes).
4. **No diferencia entre LoS y NLoS:** El modelo proporciona una pérdida media sin distinguir si existe línea de visión directa o no.

### 3.2 Modelo COST-231 Hata

#### 3.2.1 Extensión del Modelo Hata

Para superar la limitación de frecuencia del modelo Okumura-Hata original, el proyecto europeo COST 231 (*European Cooperative for Scientific and Technical Research*) desarrolló una extensión que amplía el rango de frecuencia hasta 2 GHz. Esta extensión, conocida como modelo COST-231 Hata (o Hata extendido), fue publicada en 1999 y ha sido ampliamente utilizada en la planificación de redes GSM 1800, UMTS y LTE en la banda de 1800-2000 MHz.

#### 3.2.2 Ecuación del Modelo COST-231 Hata

$$L_u \text{ [dB]} = 46.3 + 33.9 \log_{10}(f) - 13.82 \log_{10}(h_b) - a(h_m) + \left[44.9 - 6.55 \log_{10}(h_b)\right] \log_{10}(d) + C_m$$

donde:

- $L_u$ es la pérdida de trayectoria mediana, en dB.
- $f$ es la frecuencia de la portadora en MHz. Rango de validez: $1500 \leq f \leq 2000$ MHz.
- $h_b$ es la altura de la antena de la estación base, en metros. Rango: $30 \leq h_b \leq 200$ m.
- $h_m$ es la altura de la antena del terminal móvil, en metros. Rango: $1 \leq h_m \leq 10$ m.
- $d$ es la distancia, en kilómetros. Rango: $1 \leq d \leq 20$ km.
- $a(h_m)$ es el factor de corrección de la antena del móvil, que se calcula con la misma fórmula que para ciudades medianas del modelo Okumura-Hata:

$$a(h_m) = (1.1 \log_{10}(f) - 0.7) h_m - (1.56 \log_{10}(f) - 0.8)$$

- $C_m$ es el factor de corrección metropolitano:
  - $C_m = 0$ dB para ciudades medianas y áreas suburbanas.
  - $C_m = 3$ dB para centros metropolitanos (grandes ciudades).

**Comparación de las constantes con el modelo Okumura-Hata original:**

| Constante | Okumura-Hata | COST-231 Hata |
|:---:|:---:|:---:|
| Término constante | 69.55 | 46.3 |
| Coeficiente de $\log_{10}(f)$ | 26.16 | 33.9 |
| Coeficiente de $\log_{10}(h_b)$ | $-13.82$ | $-13.82$ |
| Exponente de distancia | $44.9 - 6.55\log_{10}(h_b)$ | $44.9 - 6.55\log_{10}(h_b)$ |
| Corrección metropolitana | Implícita en $a(h_m)$ | $C_m$ explícito |

Las principales diferencias son la constante de referencia y el coeficiente de frecuencia, que se ajustaron para reflejar la mayor atenuación a frecuencias más altas.

#### 3.2.3 Ejemplo Numérico Completo

**Ejemplo 3.3:** Calcular la pérdida de trayectoria para un enlace UMTS a 2000 MHz con: $h_b = 50$ m, $h_m = 1.5$ m, $d = 3$ km, en una ciudad mediana ($C_m = 0$ dB).

Paso 1: Factor de corrección $a(h_m)$:

$$a(h_m) = (1.1 \log_{10}(2000) - 0.7) \times 1.5 - (1.56 \log_{10}(2000) - 0.8)$$

$$= (1.1 \times 3.301 - 0.7) \times 1.5 - (1.56 \times 3.301 - 0.8)$$

$$= (3.631 - 0.7) \times 1.5 - (5.150 - 0.8)$$

$$= 2.931 \times 1.5 - 4.350 = 4.397 - 4.350 = 0.047 \text{ dB}$$

Paso 2: Calcular cada término:

$$46.3 + 33.9 \log_{10}(2000) = 46.3 + 33.9 \times 3.301 = 46.3 + 111.90 = 158.20$$

$$13.82 \log_{10}(50) = 13.82 \times 1.699 = 23.48$$

$$[44.9 - 6.55 \log_{10}(50)] \log_{10}(3) = [44.9 - 6.55 \times 1.699] \times 0.477$$

$$= [44.9 - 11.13] \times 0.477 = 33.77 \times 0.477 = 16.11$$

Paso 3: Pérdida total:

$$L_u = 158.20 - 23.48 - 0.047 + 16.11 + 0 = 150.78 \text{ dB}$$

Si el mismo cálculo se realizara para un centro metropolitano ($C_m = 3$ dB):

$$L_u = 150.78 + 3 = 153.78 \text{ dB}$$

La diferencia de 3 dB entre ciudad mediana y centro metropolitano corresponde a una reducción del 50% en la potencia recibida, lo que se traduce en una reducción significativa del radio de cobertura.

### 3.3 Modelo 3GPP TR 38.901 (5G NR)

#### 3.3.1 Contexto: Rangos de Frecuencia FR1 y FR2

El 3rd Generation Partnership Project (3GPP) ha desarrollado un modelo de canal completo para 5G NR documentado en el informe técnico TR 38.901, que cubre frecuencias desde 0.5 GHz hasta 100 GHz. Este modelo supera las limitaciones de frecuencia de los modelos clásicos y es esencial para el diseño de redes 5G tanto en el rango de frecuencias Sub-6 GHz (FR1: 410 MHz – 7125 MHz) como en ondas milimétricas (FR2: 24.25 GHz – 52.6 GHz).

El modelo define varios escenarios de despliegue, cada uno con ecuaciones de pérdida de trayectoria específicas para condiciones de línea de visión (LoS) y sin línea de visión (NLoS):

- **UMa (Urban Macro):** Estaciones base macro-celulares en entornos urbanos, con altenas típicamente a 25 m de altura.
- **UMi-Street Canyon (Urban Micro):** Estaciones base de baja potencia en entornos urbanos, con antenas a nivel de azoteas de edificios bajos (típicamente 10 m). Los usuarios están en calles tipo cañón.
- **RMa (Rural Macro):** Entornos rurales con baja densidad de obstáculos.
- **InH (Indoor Hotspot):** Entornos interiores tipo oficina abierta.

#### 3.3.2 Modelo UMi-Street Canyon

Para el escenario **UMi-Street Canyon**, las ecuaciones de pérdida de trayectoria son:

**Condición LoS:**

$$PL_{\text{UMi-LoS}} \text{ [dB]} = \begin{cases} PL_1 & \text{si } 10 \text{ m} \leq d_{2D} \leq d'_{BP} \\ PL_2 & \text{si } d'_{BP} < d_{2D} \leq 5000 \text{ m} \end{cases}$$

donde:

$$PL_1 = 32.4 + 21 \log_{10}(d_{3D}) + 20 \log_{10}(f_c)$$

$$PL_2 = 32.4 + 40 \log_{10}(d_{3D}) + 20 \log_{10}(f_c) - 9.5\log_{10}\left[(d'_{BP})^2 + (h_{BS} - h_{UT})^2\right]$$

La **distancia de punto de quiebre** (*breakpoint distance*) $d'_{BP}$ marca la transición entre dos regímenes de propagación:

$$d'_{BP} = \frac{4 \, h'_{BS} \, h'_{UT} \, f_c}{c}$$

donde:

- $d_{2D}$ es la distancia horizontal entre estación base y usuario, en metros.
- $d_{3D} = \sqrt{d_{2D}^2 + (h_{BS} - h_{UT})^2}$ es la distancia tridimensional en metros.
- $f_c$ es la frecuencia de la portadora en GHz.
- $h_{BS}$ es la altura de la estación base (valor por defecto: 10 m).
- $h_{UT}$ es la altura del terminal de usuario (valor por defecto: 1.5 m).
- $h'_{BS} = h_{BS} - h_E$ y $h'_{UT} = h_{UT} - h_E$ son las alturas efectivas de las antenas, donde $h_E = 1.0$ m es la altura efectiva del entorno.
- $c = 3 \times 10^8$ m/s es la velocidad de la luz.

Para distancias menores que $d'_{BP}$, el exponente de pérdida es 2.1 (similar al espacio libre), mientras que para distancias mayores, el exponente aumenta a 4.0, reflejando la fuerte atenuación debida a reflexiones en el suelo que interfieren destructivamente con la señal directa.

**Condición NLoS:**

$$PL_{\text{UMi-NLoS}} \text{ [dB]} = \max(PL_{\text{UMi-LoS}}, PL'_{\text{UMi-NLoS}})$$

donde:

$$PL'_{\text{UMi-NLoS}} = 22.4 + 35.3 \log_{10}(d_{3D}) + 21.3 \log_{10}(f_c) - 0.3(h_{UT} - 1.5)$$

La desviación estándar del shadowing es $\sigma_{SF} = 4.0$ dB para LoS y $\sigma_{SF} = 7.82$ dB para NLoS.

#### 3.3.3 Modelo UMa

Para el escenario **UMa** (Urban Macro), con $h_{BS} = 25$ m:

**LoS:**

$$PL_1 = 28.0 + 22\log_{10}(d_{3D}) + 20\log_{10}(f_c)$$

$$PL_2 = 28.0 + 40\log_{10}(d_{3D}) + 20\log_{10}(f_c) - 9\log_{10}\left[(d'_{BP})^2 + (h_{BS} - h_{UT})^2\right]$$

con $d'_{BP} = 4 \, h'_{BS} \, h'_{UT} \, f_c / c$, donde la altura efectiva del entorno $h_E$ se calcula con una distribución probabilística condicionada a la distancia.

**NLoS:**

$$PL_{\text{UMa-NLoS}} = \max(PL_{\text{UMa-LoS}}, PL'_{\text{UMa-NLoS}})$$

$$PL'_{\text{UMa-NLoS}} = 13.54 + 39.08\log_{10}(d_{3D}) + 20\log_{10}(f_c) - 0.6(h_{UT} - 1.5)$$

#### 3.3.4 Modelo RMa

Para el escenario **RMa** (Rural Macro), el modelo considera alturas de antena de estación base más elevadas ($h_{BS} = 35$ m) y distancias mayores:

**LoS:**

$$PL_1 = 20\log_{10}\left(\frac{40\pi d_{3D} f_c}{3}\right) + \min(0.03h^{1.72}, 10)\log_{10}(d_{3D}) - \min(0.044h^{1.72}, 14.77) + 0.002\log_{10}(h) d_{3D}$$

donde $h$ es la altura media de los edificios del entorno (por defecto $h = 5$ m).

#### 3.3.5 Probabilidad LoS/NLoS

El modelo 3GPP TR 38.901 también define la probabilidad de que un usuario se encuentre en condición LoS en función de la distancia $d_{2D}$. Para UMi-Street Canyon:

$$P_{\text{LoS}} = \begin{cases} 1 & \text{si } d_{2D} \leq 18 \text{ m} \\ \frac{18}{d_{2D}} + \exp\left(-\frac{d_{2D}}{36}\right)\left(1 - \frac{18}{d_{2D}}\right) & \text{si } d_{2D} > 18 \text{ m} \end{cases}$$

Esta función decrece rápidamente con la distancia: a 50 m, $P_{\text{LoS}} \approx 0.63$; a 200 m, $P_{\text{LoS}} \approx 0.10$.

#### 3.3.6 Ejemplo Numérico para UMi-LoS

**Ejemplo 3.4:** Calcular la pérdida de trayectoria para un enlace 5G NR UMi-LoS con: $f_c = 3.5$ GHz (FR1), $h_{BS} = 10$ m, $h_{UT} = 1.5$ m, $d_{2D} = 200$ m, $h_E = 1.0$ m.

Paso 1: Calcular alturas efectivas:

$$h'_{BS} = 10 - 1.0 = 9.0 \text{ m}$$

$$h'_{UT} = 1.5 - 1.0 = 0.5 \text{ m}$$

Paso 2: Calcular la distancia de punto de quiebre:

$$d'_{BP} = \frac{4 \times 9.0 \times 0.5 \times 3.5 \times 10^9}{3 \times 10^8} = \frac{63 \times 10^9}{3 \times 10^8} = 210 \text{ m}$$

Paso 3: Verificar la condición. Como $d_{2D} = 200$ m $\leq d'_{BP} = 210$ m, usamos $PL_1$.

Paso 4: Calcular $d_{3D}$:

$$d_{3D} = \sqrt{200^2 + (10 - 1.5)^2} = \sqrt{40000 + 72.25} = \sqrt{40072.25} = 200.18 \text{ m}$$

Paso 5: Calcular $PL_1$:

$$PL_1 = 32.4 + 21 \log_{10}(200.18) + 20 \log_{10}(3.5)$$

$$= 32.4 + 21 \times 2.3014 + 20 \times 0.5441$$

$$= 32.4 + 48.33 + 10.88 = 91.61 \text{ dB}$$

Este valor es significativamente menor que los $\sim$148 dB obtenidos con Okumura-Hata a 5 km, lo que refleja tanto la menor distancia como la condición favorable de LoS. A 200 m, la señal 5G a 3.5 GHz tiene una pérdida moderada que permite tasas de datos muy altas.

**[Descripción de Figura 3.1]:** *Gráfico de pérdida de trayectoria (eje Y, en dB, de 60 a 180 dB) versus distancia logarítmica (eje X, de 10 m a 5 km). Se trazan cinco curvas: (1) Espacio libre a 3.5 GHz (línea punteada gris), (2) UMi-LoS a 3.5 GHz (línea sólida azul), (3) UMi-NLoS a 3.5 GHz (línea sólida roja), (4) UMa-LoS a 3.5 GHz (línea discontinua verde), (5) UMa-NLoS a 3.5 GHz (línea discontinua naranja). Se marca la distancia de punto de quiebre $d'_{BP}$ con una línea vertical punteada para cada escenario LoS, mostrando el cambio de pendiente. Leyenda en la esquina superior izquierda. Nota al pie indicando: "Modelo 3GPP TR 38.901, $h_{BS} = 10$ m (UMi) / 25 m (UMa), $h_{UT} = 1.5$ m".*

---

## 4. Modelos de Propagación en Interiores

### 4.1 Recomendación ITU-R P.1238-11

#### 4.1.1 Introducción

La Recomendación ITU-R P.1238 (*Propagation data and prediction methods for the planning of indoor radiocommunication systems and radio local area networks in the frequency range 300 MHz to 450 GHz*) es el estándar internacional de la Unión Internacional de Telecomunicaciones (UIT) para la predicción de pérdida de trayectoria en entornos interiores. La versión más reciente (P.1238-11, de 2021) amplía el rango de frecuencia para incluir bandas de ondas milimétricas, relevantes para 5G NR y WiGig (802.11ad/ay) a 60 GHz.

#### 4.1.2 Ecuación del Modelo

La pérdida de trayectoria total según la Recomendación ITU-R P.1238 se calcula como:

$$L_{\text{total}} \text{ [dB]} = 20 \log_{10}(f) + N \log_{10}(d) + L_f(n) - 28$$

donde:

- $L_{\text{total}}$ es la pérdida de trayectoria total en dB.
- $f$ es la frecuencia en MHz.
- $d$ es la distancia entre transmisor y receptor en metros (con $d > 1$ m).
- $N$ es el **coeficiente de pérdida por distancia** (*distance power loss coefficient*), que reemplaza al exponente $10n$ del modelo general. Es un factor empírico que depende del tipo de entorno y la frecuencia. El valor de $N$ determina la tasa de decaimiento de la señal con la distancia.
- $L_f(n)$ es el **factor de penetración de pisos** (*floor penetration loss factor*) en dB, que representa la atenuación adicional causada al atravesar $n$ pisos del edificio. Su valor depende del número de pisos $n$, la frecuencia y el tipo de edificio.
- $-28$ es una constante de calibración en dB.

#### 4.1.3 Valores Típicos de N

Los valores típicos del coeficiente de pérdida por distancia $N$ para diferentes entornos y frecuencias, según la Recomendación ITU-R P.1238-11, son:

| Entorno | Frecuencia | $N$ |
|:---|:---:|:---:|
| Oficina | 900 MHz | 33 |
| Oficina | 2.4 GHz | 30 |
| Oficina | 5 GHz | 31 |
| Oficina | 6 GHz | 31 |
| Oficina | 28 GHz | 32.7 |
| Oficina | 60 GHz | 20.9 |
| Residencial | 2.4 GHz | 28 |
| Residencial | 5 GHz | 28 |
| Residencial | 6 GHz | 28 |
| Comercio/Fábrica | 2.4 GHz | 22 |
| Comercio/Fábrica | 5 GHz | 22 |
| Comercio/Fábrica | 6 GHz | 23 |
| Corredor (mismo piso) | 900 MHz | 20 |
| Corredor (mismo piso) | 2.4 GHz | 20 |

Un valor de $N = 31$ para una oficina a 5 GHz indica un exponente de pérdida de trayectoria de $n = N/10 = 3.1$, significativamente mayor que el valor de espacio libre ($n = 2$). Este incremento refleja la atenuación adicional causada por paredes, muebles, divisiones y otros elementos propios del entorno de oficina.

#### 4.1.4 Valores de $L_f(n)$

El factor de penetración de pisos representa la atenuación acumulada al atravesar múltiples pisos de un edificio. Valores típicos:

| Tipo de edificio | Frecuencia | $L_f(1)$ | $L_f(2)$ | $L_f(3)$ |
|:---|:---:|:---:|:---:|:---:|
| Oficina | 2.4 GHz | 15 dB | 19 dB | 24 dB |
| Oficina | 5 GHz | 16 dB | 22 dB | 28 dB |
| Residencial | 2.4 GHz | 10 dB | 14 dB | 18 dB |
| Comercial | 5 GHz | 18 dB | 25 dB | — |

Se observa que la pérdida por piso no es lineal: la atenuación del segundo piso es menor que la del primero, lo que se atribuye a que las trayectorias de señal entre pisos distantes tienden a utilizar caminos indirectos (como escaleras, ductos de ventilación) que no sufren la misma atenuación que la penetración directa a través del suelo/techo.

#### 4.1.5 Ejemplo Numérico Completo

**Ejemplo 4.1:** Calcular la pérdida de trayectoria en una oficina a 5 GHz para un punto de acceso Wi-Fi y un terminal ubicado en el mismo piso a 30 metros de distancia.

Datos: $f = 5000$ MHz, $N = 31$, $d = 30$ m, $n = 0$ pisos (mismo piso, $L_f(0) = 0$).

$$L_{\text{total}} = 20 \log_{10}(5000) + 31 \times \log_{10}(30) + 0 - 28$$

$$= 20 \times 3.699 + 31 \times 1.477 + 0 - 28$$

$$= 73.98 + 45.79 - 28 = 91.77 \text{ dB}$$

Ahora, si el terminal está en un piso diferente ($n = 1$, $L_f(1) = 16$ dB):

$$L_{\text{total}} = 73.98 + 45.79 + 16 - 28 = 107.77 \text{ dB}$$

La diferencia de 16 dB entre mismo piso y un piso de diferencia es significativa: equivale a reducir la potencia recibida por un factor de $10^{1.6} \approx 40$.

**[Descripción de Figura 4.1]:** *Gráfico de pérdida de trayectoria indoor (eje Y, de 40 a 130 dB) versus distancia (eje X, logarítmica, de 1 m a 100 m). Se trazan cuatro curvas para un entorno de oficina a 5 GHz: (1) mismo piso (línea azul sólida), (2) 1 piso de diferencia (línea verde discontinua), (3) 2 pisos de diferencia (línea naranja punteada), (4) espacio libre a 5 GHz como referencia (línea gris punteada fina). La separación entre las curvas refleja el factor $L_f(n)$. Leyenda indicando cada curva. Título: "Modelo ITU-R P.1238 — Pérdida de trayectoria en oficina a 5 GHz".*

### 4.2 Modelos IEEE 802.11 (TGax y TGbe)

#### 4.2.1 Introducción

Los grupos de trabajo IEEE 802.11ax (TGax, responsable de Wi-Fi 6/6E) y 802.11be (TGbe, responsable de Wi-Fi 7) han adoptado modelos de canal específicos para evaluar el rendimiento de sus estándares. Estos modelos, basados en los modelos de canal IEEE 802.11 desarrollados originalmente para 802.11n/ac, definen escenarios residenciales y empresariales con parámetros de propagación detallados.

#### 4.2.2 Escenario Residencial (TGax Residential)

El modelo de propagación para el escenario residencial se basa en el modelo de penetración de paredes:

$$PL(d) \text{ [dB]} = 40.05 + 20 \log_{10}\left(\frac{f_c}{2.4}\right) + 20\log_{10}(\min(d, 5)) + \begin{cases} 0 & d \leq 5 \\ 35\log_{10}\left(\frac{d}{5}\right) & d > 5 \end{cases}$$

donde $f_c$ es la frecuencia en GHz y $d$ es la distancia en metros. Este modelo presenta un cambio de pendiente a 5 metros: dentro de esa distancia, el exponente de pérdida es 2.0 (similar a espacio libre dentro de una habitación); más allá, el exponente aumenta a 3.5, reflejando la penetración de paredes interiores.

La desviación estándar del shadowing es $\sigma = 7$ dB para el escenario residencial.

#### 4.2.3 Escenario Empresarial (Enterprise)

Para el escenario empresarial (oficina de planta abierta con cubículos), el modelo es:

$$PL(d) \text{ [dB]} = 40.05 + 20 \log_{10}\left(\frac{f_c}{2.4}\right) + 20\log_{10}(\min(d, 10)) + \begin{cases} 0 & d \leq 10 \\ 35\log_{10}\left(\frac{d}{10}\right) & d > 10 \end{cases}$$

La distancia de quiebre aumenta a 10 metros, reflejando que en oficinas abiertas hay menos paredes interiores que en residencias. La desviación estándar del shadowing es $\sigma = 7$ dB.

#### 4.2.4 Atenuación por Materiales

Una parte fundamental de la modelación de propagación en interiores es la atenuación que sufre la señal al atravesar diferentes materiales de construcción. Los valores varían significativamente con la frecuencia y el tipo de material:

| Material | Espesor típico | Atenuación a 2.4 GHz | Atenuación a 5 GHz | Atenuación a 6 GHz |
|:---|:---:|:---:|:---:|:---:|
| Pared de yeso (drywall) | 12 cm | 3-5 dB | 4-7 dB | 5-8 dB |
| Pared de ladrillo | 20 cm | 5-8 dB | 8-12 dB | 9-14 dB |
| Pared de hormigón | 15-20 cm | 10-15 dB | 15-20 dB | 17-23 dB |
| Puerta de madera | 4 cm | 3-4 dB | 4-6 dB | 5-7 dB |
| Ventana simple (vidrio) | 6 mm | 2-3 dB | 3-5 dB | 3-6 dB |
| Vidrio con capa metálica (Low-E) | 6 mm | 8-15 dB | 15-25 dB | 18-28 dB |
| Vidrio con película de protección solar | 6 mm | 20-30 dB | 25-35 dB | 28-40 dB |
| Piso/techo de hormigón | 20-30 cm | 12-18 dB | 18-25 dB | 20-28 dB |
| Panel metálico | — | 30-40 dB | 40-50 dB | 45-55 dB |
| Cuerpo humano | — | 3-5 dB | 5-8 dB | 6-10 dB |

Estos valores son fundamentales para el diseño de redes Wi-Fi, donde las paredes internas definen las fronteras de cobertura de cada punto de acceso.

#### 4.2.5 BSS Coloring como Respuesta a Interferencia Espacial

En despliegues densos de redes Wi-Fi, múltiples puntos de acceso (AP) operan en canales superpuestos, generando interferencia co-canal. El estándar IEEE 802.11ax introdujo el mecanismo de **BSS Coloring** (coloreado del conjunto de servicio básico) como una técnica de reutilización espacial para mitigar este problema.

El concepto básico es asignar un identificador numérico (el "color", un campo de 6 bits en la cabecera del marco PLCP) a cada BSS. Cuando un dispositivo detecta una trama con un color diferente al suyo y cuya potencia recibida está por debajo de un umbral configurable (OBSS/PD threshold, *Overlapping BSS Preamble Detection*), puede considerar que el medio está libre y transmitir simultáneamente. Esto permite la reutilización espacial del espectro cuando la atenuación por propagación entre BSS vecinos es suficiente.

El umbral OBSS/PD se ajusta dinámicamente según la potencia de transmisión. Según el estándar 802.11ax:

$$\text{OBSS/PD}_{\text{max}} \text{ [dBm]} = \max(-82, \min(-62, -82 + (P_{TX,\text{ref}} - P_{TX})))$$

donde $P_{TX,\text{ref}}$ es la potencia de transmisión de referencia (21 dBm para transmisiones no-SRT) y $P_{TX}$ es la potencia de transmisión actual del dispositivo. Este mecanismo vincula la reutilización espacial con la potencia de transmisión, asegurando que las transmisiones de alta potencia sean más conservadoras en la reutilización.

### 4.3 Modelo de Pérdida por Materiales y Link Budget Indoor

#### 4.3.1 Modelo de Pérdida por Materiales

Un enfoque más detallado para la propagación en interiores consiste en modelar explícitamente la atenuación causada por cada obstáculo que la señal debe atravesar. Este modelo se expresa como:

$$L \text{ [dB]} = L_0 + 10n \log_{10}(d) + \sum_{i} L_{\text{wall},i} + L_{\text{floor}}$$

donde:

- $L_0$ es la pérdida de referencia a 1 metro (en dB). Se calcula típicamente como la FSPL a 1 metro: $L_0 = 20\log_{10}(f) + 20\log_{10}\left(\frac{4\pi}{c}\right) = 20\log_{10}(f_{\text{MHz}}) - 27.56$.
- $n$ es el exponente de pérdida de trayectoria (típicamente entre 2.0 y 3.0 para ambientes interiores sin paredes obstruyendo).
- $d$ es la distancia en metros.
- $\sum_{i} L_{\text{wall},i}$ es la suma de las atenuaciones de cada pared que la señal atraviesa en su trayectoria directa.
- $L_{\text{floor}}$ es la atenuación por penetración de piso(s), si transmisor y receptor están en pisos diferentes.

#### 4.3.2 Tabla de Pérdidas por Material

La siguiente tabla resume las pérdidas por material más utilizadas en el diseño de redes Wi-Fi:

| Material | Pérdida a 2.4 GHz | Pérdida a 5 GHz | Pérdida a 6 GHz |
|:---|:---:|:---:|:---:|
| Pared ligera (yeso/drywall) | 4 dB | 6 dB | 7 dB |
| Pared de ladrillo | 7 dB | 10 dB | 12 dB |
| Pared de hormigón armado | 12 dB | 18 dB | 20 dB |
| Puerta de madera | 3 dB | 5 dB | 6 dB |
| Puerta metálica | 15 dB | 20 dB | 22 dB |
| Ventana (vidrio simple) | 3 dB | 4 dB | 5 dB |
| Ventana (vidrio Low-E) | 12 dB | 20 dB | 23 dB |
| Piso/techo de hormigón | 15 dB | 20 dB | 23 dB |

#### 4.3.3 Ejemplo Completo de Link Budget Indoor

**Ejemplo 4.2:** Un punto de acceso Wi-Fi 6E opera a 6 GHz con $P_T = 18$ dBm y antena interna con $G_T = 4$ dBi. El terminal de usuario tiene una ganancia de antena $G_R = 0$ dBi. Se desea calcular la potencia recibida y la viabilidad del enlace a un usuario ubicado a $d = 25$ m del AP, donde la señal debe atravesar 2 paredes de yeso y 1 pared de ladrillo.

Paso 1: Calcular la pérdida de referencia $L_0$ a 1 metro a 6000 MHz:

$$L_0 = 20 \log_{10}(6000) - 27.56 = 20 \times 3.778 - 27.56 = 75.56 - 27.56 = 48.0 \text{ dB}$$

Paso 2: Calcular la pérdida por distancia (usando $n = 2.5$ para oficina con paredes):

$$10 \times 2.5 \times \log_{10}(25) = 25 \times 1.398 = 34.95 \text{ dB}$$

Paso 3: Sumar las pérdidas por paredes:

$$\sum L_{\text{wall}} = 2 \times 7 + 1 \times 12 = 14 + 12 = 26 \text{ dB}$$

Paso 4: Pérdida total de trayectoria:

$$L = 48.0 + 34.95 + 26 = 108.95 \text{ dB}$$

Paso 5: Presupuesto de enlace completo:

$$P_R = P_T + G_T + G_R - L = 18 + 4 + 0 - 108.95 = -86.95 \text{ dBm}$$

Paso 6: Evaluación. ¿Es viable este enlace? La sensibilidad de un terminal Wi-Fi 6E típico es:

- MCS 11 (1024-QAM, 5/6, máxima velocidad): sensibilidad $\approx -54$ dBm. **No viable** ($-86.95 < -54$).
- MCS 7 (256-QAM, 3/4): sensibilidad $\approx -65$ dBm. **No viable**.
- MCS 4 (16-QAM, 3/4): sensibilidad $\approx -73$ dBm. **No viable**.
- MCS 1 (QPSK, 1/2): sensibilidad $\approx -82$ dBm. **No viable**.
- MCS 0 (BPSK, 1/2): sensibilidad $\approx -85$ dBm. **Marginalmente no viable**.

**Conclusión:** A 25 metros con 3 paredes intermedias a 6 GHz, el enlace no es viable para ningún MCS útil. El diseñador de red debería considerar: (a) agregar un punto de acceso adicional más cercano al usuario, (b) reducir el número de paredes en la trayectoria, o (c) utilizar la banda de 5 GHz o 2.4 GHz como alternativa para este enlace.

#### 4.3.4 Relación entre RSSI, SNR y MCS

La **Indicación de Intensidad de Señal Recibida (RSSI)** es la potencia total de la señal recibida, incluyendo señal deseada, interferencia y ruido. En la práctica, el RSSI es la métrica que reportan los dispositivos Wi-Fi y los teléfonos móviles.

La **Relación Señal a Ruido (SNR)** es la diferencia (en dB) entre la potencia de la señal deseada y la potencia del ruido térmico:

$$\text{SNR [dB]} = P_R \text{ [dBm]} - N_{\text{floor}} \text{ [dBm]}$$

El piso de ruido térmico se calcula como:

$$N_{\text{floor}} = -174 + 10 \log_{10}(B) + NF$$

donde:

- $-174$ dBm/Hz es la densidad espectral de potencia del ruido térmico a temperatura ambiente ($T = 290$ K): $kT = 1.38 \times 10^{-23} \times 290 = 4.0 \times 10^{-21}$ W/Hz $= -174$ dBm/Hz.
- $B$ es el ancho de banda del canal en Hz.
- $NF$ es la figura de ruido del receptor en dB (típicamente 5-7 dB para receptores Wi-Fi).

**Ejemplo:** Para un canal Wi-Fi de 80 MHz con $NF = 6$ dB:

$$N_{\text{floor}} = -174 + 10\log_{10}(80 \times 10^6) + 6 = -174 + 79.03 + 6 = -88.97 \text{ dBm}$$

Si la potencia recibida es $P_R = -65$ dBm:

$$\text{SNR} = -65 - (-88.97) = 23.97 \text{ dB}$$

El **Esquema de Modulación y Codificación (MCS)** que puede utilizarse depende directamente del SNR. A mayor SNR, se puede utilizar un MCS más agresivo (mayor orden de modulación y mayor tasa de código), lo que se traduce en mayor velocidad de transmisión. Esta adaptación dinámica se denomina **adaptación de enlace (*link adaptation*)** o *Adaptive Modulation and Coding (AMC)*. El transmisor monitorea continuamente la calidad del canal (a través de retroalimentación del receptor) y selecciona el MCS más alto que garantice una tasa de error de trama aceptable (típicamente FER < 10%).

#### 4.3.5 Capacidad MIMO

La tecnología MIMO (*Multiple-Input Multiple-Output*) utiliza múltiples antenas tanto en el transmisor como en el receptor para crear flujos de datos espaciales independientes, multiplicando la capacidad del enlace. La capacidad teórica de un sistema MIMO se aproxima como:

$$C \approx \min(N_T, N_R) \times B \times \log_2(1 + \text{SNR})$$

donde:

- $C$ es la capacidad del canal en bits por segundo (bps).
- $N_T$ es el número de antenas transmisoras.
- $N_R$ es el número de antenas receptoras.
- $\min(N_T, N_R)$ es el número máximo de flujos espaciales independientes (*spatial streams*) que el sistema puede soportar, asumiendo una matriz de canal de rango completo (decorrelación espacial suficiente entre las antenas).
- $B$ es el ancho de banda del canal en Hz.
- $\text{SNR}$ es la relación señal a ruido lineal (no en dB).

Esta ecuación muestra que MIMO puede, idealmente, multiplicar la capacidad por un factor igual al número mínimo de antenas. Por ejemplo, un sistema Wi-Fi 6 con $4 \times 4$ MIMO ($N_T = N_R = 4$), ancho de banda $B = 160$ MHz y $\text{SNR} = 25$ dB ($\text{SNR}_{\text{lineal}} = 10^{2.5} = 316.2$):

$$C \approx 4 \times 160 \times 10^6 \times \log_2(1 + 316.2)$$

$$= 4 \times 160 \times 10^6 \times 8.31 = 5.32 \times 10^9 \text{ bps} = 5.32 \text{ Gbps}$$

En la práctica, la capacidad real es menor debido a la correlación espacial entre antenas, la sobrecarga de protocolos y las imperfecciones del canal.

#### 4.3.6 Adaptación de Enlace

La adaptación de enlace es el proceso mediante el cual el transmisor ajusta dinámicamente los parámetros de transmisión (MCS, número de flujos espaciales, ancho de banda) en respuesta a las condiciones cambiantes del canal. Este proceso es fundamental para maximizar el *throughput* y mantener la fiabilidad del enlace.

En Wi-Fi 6/6E/7, la adaptación de enlace funciona de la siguiente manera:

1. El transmisor envía tramas de datos con un MCS inicial.
2. El receptor evalúa la calidad de la señal recibida (SNR, tasa de error).
3. El receptor envía retroalimentación al transmisor (implícita, mediante acuse de recibo, o explícita mediante tramas de reporte de canal).
4. El transmisor ajusta el MCS para la siguiente transmisión:
   - Si el SNR es alto y no hay errores, el transmisor puede probar un MCS más alto (mayor velocidad).
   - Si hay errores o el SNR disminuye, el transmisor reduce el MCS (mayor robustez, menor velocidad).

Este mecanismo de adaptación implica que la relación entre la pérdida de trayectoria y la velocidad experimentada por el usuario no es lineal sino escalonada: a medida que el usuario se aleja del punto de acceso, la velocidad se mantiene constante hasta que el SNR cae por debajo del umbral del MCS actual, momento en el cual se produce una transición abrupta al MCS inferior.

### 4.4 Dimensionamiento de Cobertura

#### 4.4.1 Cálculo del Radio de Cobertura

El dimensionamiento de cobertura consiste en determinar el área que un punto de acceso o estación base puede cubrir garantizando un nivel mínimo de servicio. El procedimiento general es:

1. **Definir el nivel mínimo de señal requerido ($P_{R,\text{min}}$):** Esto depende del MCS mínimo aceptable, que a su vez depende de la velocidad de datos mínima requerida.

2. **Calcular el presupuesto de enlace descendente (*downlink link budget*):**

$$P_{R,\text{min}} = P_T + G_T - L_{\text{cables}} + G_R - PL_{\text{max}} - M_{\text{fade}} - M_{\text{interferencia}}$$

3. **Resolver para la pérdida de trayectoria máxima permitida:**

$$PL_{\text{max}} = P_T + G_T - L_{\text{cables}} + G_R - P_{R,\text{min}} - M_{\text{fade}} - M_{\text{interferencia}}$$

4. **Usar el modelo de propagación apropiado para determinar la distancia máxima ($d_{\text{max}}$)** a la cual la pérdida de trayectoria iguala $PL_{\text{max}}$.

5. **Calcular el área de cobertura** como $A = \pi \, d_{\text{max}}^2$ (para una celda circular idealizada).

#### 4.4.2 Ejemplo Completo de Dimensionamiento para Oficina

**Ejemplo 4.3:** Dimensionar la cobertura de un punto de acceso Wi-Fi 6 operando a 5 GHz en una oficina de planta abierta (sin paredes interiores significativas). Requisito: velocidad mínima de 100 Mbps por usuario con un flujo espacial.

**Parámetros del sistema:**

| Parámetro | Valor |
|:---|:---:|
| Potencia de transmisión del AP ($P_T$) | 20 dBm |
| Ganancia de antena del AP ($G_T$) | 4 dBi |
| Pérdida en cables/conectores ($L_{\text{cables}}$) | 1 dB |
| Ganancia de antena del terminal ($G_R$) | 0 dBi |
| Margen de shadowing ($M_{\text{fade}}$, 90%) | 7 dB |
| Margen de interferencia ($M_{\text{interf}}$) | 3 dB |
| Modelo de propagación | ITU-R P.1238 ($N = 31$) |
| Ancho de banda | 80 MHz |
| Figura de ruido del receptor | 6 dB |

**Paso 1:** Determinar el MCS mínimo necesario.

Para lograr 100 Mbps con un flujo espacial en un canal de 80 MHz (factor de muestreo: 234 subportadoras de datos × 3.2 µs de símbolo OFDM), los MCS candidatos según Wi-Fi 6 con 80 MHz, 1 flujo espacial y GI de 800 ns son:

- MCS 7 (64-QAM, 5/6): tasa PHY = 293.1 Mbps → **suficiente**.
- MCS 4 (16-QAM, 3/4): tasa PHY = 175.5 Mbps → **suficiente**.
- MCS 3 (16-QAM, 1/2): tasa PHY = 117.0 Mbps → **suficiente** (margen mínimo).

Seleccionamos **MCS 3** como mínimo, cuya sensibilidad típica es $P_{R,\text{min}} \approx -76$ dBm.

**Paso 2:** Calcular la pérdida de trayectoria máxima:

$$PL_{\text{max}} = P_T + G_T - L_{\text{cables}} + G_R - P_{R,\text{min}} - M_{\text{fade}} - M_{\text{interf}}$$

$$PL_{\text{max}} = 20 + 4 - 1 + 0 - (-76) - 7 - 3 = 89 \text{ dB}$$

**Paso 3:** Calcular el radio de cobertura usando el modelo ITU-R P.1238:

$$PL_{\text{max}} = 20 \log_{10}(f) + N \log_{10}(d_{\text{max}}) - 28$$

$$89 = 20 \log_{10}(5000) + 31 \log_{10}(d_{\text{max}}) - 28$$

$$89 = 73.98 + 31 \log_{10}(d_{\text{max}}) - 28$$

$$89 = 45.98 + 31 \log_{10}(d_{\text{max}})$$

$$31 \log_{10}(d_{\text{max}}) = 89 - 45.98 = 43.02$$

$$\log_{10}(d_{\text{max}}) = \frac{43.02}{31} = 1.388$$

$$d_{\text{max}} = 10^{1.388} = 24.4 \text{ m}$$

**Paso 4:** Calcular el área de cobertura:

$$A = \pi \times d_{\text{max}}^2 = \pi \times 24.4^2 = \pi \times 595.4 = 1870 \text{ m}^2$$

**Paso 5:** Dimensionamiento del número de APs.

Si la oficina tiene un área total de $A_{\text{oficina}} = 5000$ m², el número mínimo de puntos de acceso necesarios es:

$$N_{AP} = \left\lceil \frac{A_{\text{oficina}}}{A} \right\rceil = \left\lceil \frac{5000}{1870} \right\rceil = \lceil 2.67 \rceil = 3 \text{ APs}$$

Sin embargo, en la práctica se recomienda agregar un factor de seguridad del 20-30% y considerar la superposición de cobertura necesaria para roaming suave (*soft handover*), lo que llevaría a un diseño con **4 APs**.

**Paso 6:** Verificación del enlace ascendente (*uplink*).

Es fundamental verificar también el enlace ascendente, ya que los terminales de usuario (smartphones, laptops) tienen menor potencia de transmisión que el AP. Considerando un terminal con $P_{T,\text{UE}} = 15$ dBm (potencia EIRP típica de un smartphone):

$$P_{R,\text{AP}} = 15 + 0 + 4 - 1 - PL(24.4) - 0 = 18 - 89 = -71 \text{ dBm}$$

Si la sensibilidad del AP es similar a la del terminal ($\approx -76$ dBm para MCS 3), el enlace ascendente tiene un margen de $-71 - (-76) = 5$ dB sin considerar los márgenes de desvanecimiento. Descontando los márgenes ($7 + 3 = 10$ dB), el enlace ascendente no cierra con MCS 3 en el borde. Este análisis revela que el enlace ascendente es el enlace limitante, y el radio de cobertura real debería ser menor o el MCS mínimo más bajo.

**[Descripción de Figura 4.2]:** *Plano de planta de una oficina rectangular de 100 m × 50 m (5000 m²). Se muestran 4 puntos de acceso (iconos de AP en azul) distribuidos uniformemente. Cada AP tiene un círculo de cobertura con radio $d_{\text{max}} = 24.4$ m, representado como un área circular semitransparente en azul claro. Los círculos se superponen ligeramente en las zonas de transición (áreas de roaming, coloreadas en verde claro). Las esquinas de la oficina que quedan fuera de cualquier círculo de cobertura están sombreadas en rojo claro, indicando zonas sin cobertura o con cobertura marginal. Una leyenda indica: azul = cobertura garantizada, verde = zona de roaming, rojo = cobertura insuficiente. Dimensiones acotadas en el plano. Escala gráfica en la esquina inferior.*

## 5. Introducción a las Redes WiFi

### 5.1 ¿Qué es WiFi?

WiFi es una tecnología de comunicación inalámbrica que permite a dispositivos electrónicos intercambiar datos mediante ondas de radio, sin necesidad de cables físicos. El término "WiFi" es una marca comercial registrada por la **Wi-Fi Alliance**, una organización sin fines de lucro que certifica la interoperabilidad de productos basados en los estándares **IEEE 802.11**. Es importante aclarar un error común: WiFi **no** es un acrónimo de "Wireless Fidelity"; el nombre fue creado por la firma de marketing Interbrand como una marca fácil de recordar.

Desde el punto de vista técnico, WiFi implementa las capas **PHY** (física) y **MAC** (control de acceso al medio) del modelo OSI, ambas definidas por la familia de estándares IEEE 802.11. La capa PHY se encarga de la modulación, codificación y transmisión de señales de radiofrecuencia, mientras que la capa MAC gestiona el acceso al medio compartido, la formación de tramas, la autenticación y la asociación de dispositivos.

**La familia IEEE 802.11** es un conjunto de estándares desarrollados por el Instituto de Ingenieros Eléctricos y Electrónicos (IEEE) desde 1997. Cada enmienda al estándar original se identifica con un sufijo de una o dos letras (por ejemplo, 802.11a, 802.11b, 802.11n, 802.11ac, 802.11ax). A partir de 2018, la Wi-Fi Alliance introdujo una nomenclatura simplificada basada en generaciones numéricas (WiFi 4, WiFi 5, WiFi 6, etc.) para facilitar la comprensión del consumidor.

**Concepto de WLAN (Wireless Local Area Network):** Una WLAN es una red de área local que utiliza ondas de radio en lugar de cables para conectar dispositivos. A diferencia de las redes celulares, que cubren áreas extensas (kilómetros), las WLAN están diseñadas para cubrir áreas relativamente pequeñas: una habitación, un edificio o un campus. Las WLAN basadas en IEEE 802.11 operan en bandas de espectro **no licenciado** (ISM/UNII), lo que significa que cualquier persona puede desplegar una red WiFi sin necesidad de adquirir una licencia de espectro.

**Analogía pedagógica — WiFi como una conversación en una sala:** Imagine una sala de conferencias donde varias personas desean comunicarse. En una red cableada (Ethernet), cada persona tendría un tubo de comunicación privado con el moderador (switch): pueden hablar simultáneamente sin interferirse. En WiFi, todas las personas comparten el mismo aire: si dos personas hablan al mismo tiempo, se produce una "colisión" y nadie entiende nada. Por eso WiFi utiliza un protocolo llamado **CSMA/CA** (Carrier Sense Multiple Access with Collision Avoidance): antes de hablar, cada persona escucha si alguien más está hablando; si el canal está libre, espera un tiempo aleatorio adicional y luego transmite. Esta analogía ilustra por qué el rendimiento de WiFi se degrada en entornos densos con muchos usuarios.

**Arquitectura básica de una red WiFi:**

La arquitectura fundamental de IEEE 802.11 se compone de los siguientes elementos:

- **STA (Station):** Cualquier dispositivo con una interfaz de red inalámbrica 802.11. Incluye laptops, smartphones, tablets, dispositivos IoT, etc. Cada STA tiene una dirección MAC única de 48 bits.

- **AP (Access Point):** Un dispositivo que actúa como puente entre la red inalámbrica y la red cableada (generalmente Ethernet). El AP transmite periódicamente tramas *beacon* (balizas) que anuncian la existencia de la red, su SSID (nombre), las tasas soportadas y los parámetros de seguridad.

- **BSS (Basic Service Set):** Es la unidad fundamental de una red WiFi. Un BSS consta de un AP y todas las STAs asociadas a él. Cada BSS se identifica mediante un **BSSID**, que es la dirección MAC del AP. El área de cobertura de un BSS se denomina **BSA** (Basic Service Area). Existe también el modo **IBSS** (Independent BSS), conocido como modo ad-hoc, donde las STAs se comunican directamente entre sí sin un AP.

- **DS (Distribution System):** Es la infraestructura (generalmente una red Ethernet cableada) que interconecta múltiples APs, permitiendo que las STAs asociadas a diferentes APs se comuniquen entre sí.

- **ESS (Extended Service Set):** Es un conjunto de BSS interconectados a través del DS que comparten el mismo **SSID**. Desde la perspectiva del usuario, un ESS aparece como una única red inalámbrica. Cuando una STA se mueve de un BSS a otro dentro del mismo ESS, realiza un proceso de **roaming** (itinerancia) que idealmente es transparente para el usuario.

**Descripción de Figura — Arquitectura BSS y ESS:**

> *La Figura 5.1 muestra la arquitectura jerárquica de una red WiFi. En la parte izquierda se representa un BSS individual: un punto de acceso (AP₁) se dibuja como un triángulo en el centro, rodeado por un círculo punteado que representa su área de cobertura (BSA₁). Dentro de este círculo, tres estaciones (STA₁, STA₂, STA₃) se representan como rectángulos pequeños (laptop, smartphone, tablet). Líneas onduladas conectan cada STA con el AP, representando los enlaces inalámbricos. En la parte derecha se muestra un segundo BSS (AP₂ con STA₄ y STA₅). Ambos APs están conectados mediante líneas sólidas a un switch Ethernet que forma el Distribution System (DS). El conjunto de ambos BSS forma un ESS, indicado por un rectángulo punteado grande que engloba toda la estructura. Una flecha curvada entre los dos BSS indica la zona de superposición donde es posible el roaming. En la parte superior, el DS se conecta a un router que proporciona acceso a Internet.*

### 5.2 Evolución Histórica de WiFi

La tecnología WiFi ha experimentado una evolución extraordinaria desde su primera versión en 1997. Cada nueva generación ha introducido mejoras significativas en velocidad, eficiencia, alcance y capacidad para manejar múltiples dispositivos. A continuación se presenta un recorrido cronológico completo.

**IEEE 802.11 original (1997):** El estándar original definió velocidades de 1 y 2 Mbps en la banda de 2.4 GHz, utilizando técnicas de espectro ensanchado por salto de frecuencia (FHSS) y por secuencia directa (DSSS). Aunque revolucionario en concepto, estas velocidades eran demasiado limitadas para la mayoría de aplicaciones prácticas.

**IEEE 802.11b (1999) — WiFi 1:** Incrementó la velocidad máxima a 11 Mbps en 2.4 GHz mediante la modulación CCK (Complementary Code Keying). Fue el primer estándar WiFi comercialmente exitoso, impulsando la adopción masiva en hogares y oficinas. Sin embargo, la banda de 2.4 GHz solo ofrece 3 canales no solapados (1, 6, 11), lo que limita la capacidad en entornos densos.

**IEEE 802.11a (1999) — WiFi 2:** Lanzado simultáneamente con 802.11b, introdujo la modulación **OFDM** (Orthogonal Frequency Division Multiplexing) en la banda de 5 GHz, alcanzando hasta 54 Mbps. Aunque técnicamente superior, su mayor costo y menor alcance (debido a la mayor atenuación a 5 GHz) retrasaron su adopción.

**IEEE 802.11g (2003) — WiFi 3:** Combinó lo mejor de 802.11a y 802.11b: OFDM en la banda de 2.4 GHz, logrando 54 Mbps con compatibilidad hacia atrás con 802.11b. Se convirtió en el estándar dominante durante la primera mitad de la década de 2000.

**IEEE 802.11n (2009) — WiFi 4:** Marcó un salto cualitativo con la introducción de **MIMO** (Multiple-Input Multiple-Output), que utiliza múltiples antenas para transmitir y recibir flujos de datos paralelos. Soporta hasta 4 flujos espaciales, anchos de canal de 20 y 40 MHz, y opera en ambas bandas (2.4 y 5 GHz). La velocidad máxima teórica es de 600 Mbps (4 flujos × 150 Mbps/flujo). También introdujo la agregación de tramas (A-MPDU, A-MSDU) para mejorar la eficiencia MAC.

**IEEE 802.11ac (2013/2016) — WiFi 5:** Operando exclusivamente en 5 GHz, introdujo anchos de canal de hasta 160 MHz, modulación 256-QAM, MU-MIMO en enlace descendente (hasta 8 flujos espaciales) y beamforming estandarizado. La Ola 1 (2013) soportaba hasta 80 MHz y SU-MIMO; la Ola 2 (2016) añadió 160 MHz y MU-MIMO. Velocidad máxima: 6.93 Gbps.

**IEEE 802.11ax (2021) — WiFi 6/6E:** Diseñado para entornos densos, introdujo OFDMA, 1024-QAM, MU-MIMO bidireccional (DL + UL), BSS Coloring, Target Wake Time y mayor duración de símbolo OFDM. WiFi 6E extiende las mismas capacidades a la banda de 6 GHz (5.925–7.125 GHz), añadiendo hasta 1200 MHz de espectro adicional. Velocidad máxima: 9.6 Gbps.

**IEEE 802.11be (2024) — WiFi 7:** La generación más reciente introduce operación multi-enlace (MLO), modulación 4096-QAM (4K-QAM), canales de 320 MHz, MIMO mejorado (16 flujos espaciales) y latencia ultra-baja. Velocidad máxima teórica: ~46 Gbps.

**IEEE 802.11bn (en desarrollo) — WiFi 8:** Actualmente en fase de definición, WiFi 8 se enfocará en comunicaciones cooperativas, MIMO distribuido, y acceso coordinado al medio para alcanzar velocidades aún mayores y mejorar la eficiencia en redes extremadamente densas.

**Tabla 5.1 — Comparativa de Generaciones WiFi**

| Generación | Estándar IEEE | Año | Banda(s) (GHz) | Ancho Canal Máx. | Modulación Máx. | MIMO Máx. | Velocidad Máx. Teórica |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| — | 802.11 | 1997 | 2.4 | 22 MHz | DSSS/FHSS | — | 2 Mbps |
| WiFi 1 | 802.11b | 1999 | 2.4 | 22 MHz | CCK | — | 11 Mbps |
| WiFi 2 | 802.11a | 1999 | 5 | 20 MHz | 64-QAM OFDM | — | 54 Mbps |
| WiFi 3 | 802.11g | 2003 | 2.4 | 20 MHz | 64-QAM OFDM | — | 54 Mbps |
| WiFi 4 | 802.11n | 2009 | 2.4 / 5 | 40 MHz | 64-QAM OFDM | 4×4 | 600 Mbps |
| WiFi 5 | 802.11ac | 2013 | 5 | 160 MHz | 256-QAM OFDM | 8×8 MU-MIMO DL | 6.93 Gbps |
| WiFi 6 | 802.11ax | 2021 | 2.4 / 5 | 160 MHz | 1024-QAM OFDMA | 8×8 MU-MIMO DL+UL | 9.6 Gbps |
| WiFi 6E | 802.11ax | 2021 | 6 | 160 MHz | 1024-QAM OFDMA | 8×8 MU-MIMO DL+UL | 9.6 Gbps |
| WiFi 7 | 802.11be | 2024 | 2.4 / 5 / 6 | 320 MHz | 4096-QAM OFDMA | 16×16 MU-MIMO | ~46 Gbps |
| WiFi 8 | 802.11bn | ~2028 | 2.4 / 5 / 6 | 320 MHz | 4096-QAM+ | Dist. MIMO | TBD |

**Descripción de Figura — Línea de Tiempo de la Evolución WiFi:**

> *La Figura 5.2 presenta una línea de tiempo horizontal que abarca desde 1997 hasta 2028. Sobre el eje temporal, cada generación WiFi se marca con un punto y una etiqueta vertical. En 1997 se ubica "802.11 (2 Mbps)"; en 1999, dos puntos para "802.11a (54 Mbps, 5 GHz)" y "802.11b (11 Mbps, 2.4 GHz)"; en 2003, "802.11g (54 Mbps)"; en 2009, "802.11n / WiFi 4 (600 Mbps)" con un ícono de antenas MIMO; en 2013, "802.11ac / WiFi 5 (6.9 Gbps)" con un ícono de MU-MIMO; en 2021, "802.11ax / WiFi 6/6E (9.6 Gbps)" con íconos de OFDMA y 6 GHz; en 2024, "802.11be / WiFi 7 (~46 Gbps)" con un ícono de MLO; y en 2028, "802.11bn / WiFi 8 (TBD)" con línea punteada indicando futuro. Debajo de la línea, barras de colores muestran la evolución del ancho de canal (de 22 MHz a 320 MHz) y la modulación (de DSSS a 4096-QAM). La escala vertical logarítmica a la derecha muestra el crecimiento exponencial de la velocidad máxima teórica.*

---

## 6. WiFi 5 (IEEE 802.11ac)

### 6.1 Características Principales

WiFi 5, formalmente definido por la enmienda **IEEE 802.11ac**, fue publicado en dos fases: la **Ola 1** fue certificada por la Wi-Fi Alliance en junio de 2013, y la **Ola 2** en junio de 2016. Este estándar fue diseñado con un objetivo claro: proporcionar velocidades multi-gigabit en la banda de 5 GHz para satisfacer la creciente demanda de streaming de video de alta definición, transferencia de archivos grandes y aplicaciones en la nube.

Las características principales de WiFi 5 son:

- **Banda de operación:** Exclusivamente **5 GHz**. A diferencia de WiFi 4 (802.11n), que opera en 2.4 y 5 GHz, WiFi 5 se concentra en 5 GHz para aprovechar el espectro más limpio y los anchos de canal mayores disponibles en esta banda. Los dispositivos WiFi 5 que también soportan 2.4 GHz lo hacen mediante la parte 802.11n del chipset.

- **Ancho de canal:** Soporta canales de **20, 40, 80 y 160 MHz**. El canal de 80 MHz es obligatorio para la certificación WiFi 5, mientras que 160 MHz es opcional. El ancho de 160 MHz puede implementarse como un canal contiguo de 160 MHz o como **80+80 MHz** (dos segmentos de 80 MHz no contiguos).

- **Modulación:** Hasta **256-QAM** (Quadrature Amplitude Modulation), que codifica 8 bits por símbolo. Esto representa un incremento del 33% sobre la 64-QAM de WiFi 4 (6 bits por símbolo).

- **MIMO:** Soporta hasta **8 flujos espaciales** (8×8:8 MIMO), aunque la mayoría de dispositivos comerciales implementan 2×2 o 4×4. Introduce **MU-MIMO** (Multi-User MIMO) en enlace descendente, permitiendo que el AP transmita simultáneamente a hasta 4 usuarios (Ola 2).

- **Beamforming:** A diferencia de WiFi 4, donde el beamforming era opcional y existían múltiples métodos incompatibles, WiFi 5 estandariza un único mecanismo de beamforming basado en **NDP** (Null Data Packet) sounding, haciéndolo obligatorio para dispositivos que implementan más de un flujo espacial.

- **Velocidad máxima teórica:** **6.93 Gbps** con la configuración máxima (8 flujos espaciales, 160 MHz, 256-QAM, intervalo de guarda corto de 400 ns).

### 6.2 Mejoras sobre WiFi 4 (802.11n)

WiFi 5 introdujo cuatro mejoras fundamentales respecto a su predecesor. A continuación se explica cada una en detalle.

#### 6.2.1 Mayor Ancho de Banda: Hasta 160 MHz vs 40 MHz

En comunicaciones digitales, el ancho de banda del canal tiene un impacto directo sobre la tasa de transmisión. Según el teorema de Shannon, la capacidad de un canal es:

$$C = B \cdot \log_2(1 + \text{SNR})$$

donde $C$ es la capacidad en bits por segundo, $B$ es el ancho de banda en Hz y SNR es la relación señal a ruido. Duplicar el ancho de banda $B$ duplica la capacidad. WiFi 5 cuadruplica el ancho máximo de canal respecto a WiFi 4 (de 40 MHz a 160 MHz), lo que teóricamente cuadruplica la velocidad por flujo espacial.

En la práctica, un canal de 80 MHz en WiFi 5 contiene **234 subportadoras de datos** (frente a 108 en un canal de 40 MHz de WiFi 4), lo que más que duplica el número de subportadoras disponibles para transmitir datos. Un canal de 160 MHz contiene **468 subportadoras de datos**.

Sin embargo, es importante destacar que canales más anchos también capturan más ruido térmico (el piso de ruido aumenta en $10\log_{10}(B)$ dB) y son más susceptibles a la interferencia, lo que puede reducir el rango efectivo del enlace.

#### 6.2.2 MU-MIMO Downlink (Hasta 4 usuarios simultáneos)

En WiFi 4, el AP solo podía comunicarse con **una STA a la vez** en cada instante, independientemente de cuántas antenas tuviera. Esto se denomina **SU-MIMO** (Single-User MIMO). WiFi 5 introduce **MU-MIMO** (Multi-User MIMO) en el enlace descendente, lo que permite al AP dividir sus flujos espaciales entre múltiples usuarios simultáneos.

Por ejemplo, un AP 4×4 en WiFi 4 podría enviar 4 flujos espaciales a un único cliente 4×4, logrando una alta velocidad para ese cliente pero dejando a los demás en espera. Con MU-MIMO en WiFi 5, el mismo AP puede enviar simultáneamente 1 flujo a cada uno de 4 clientes 1×1, multiplicando la capacidad agregada de la red.

El MU-MIMO funciona mediante técnicas de **precodificación** (precoding): el AP aplica una matriz de pesos a las señales transmitidas por cada antena para crear haces dirigidos hacia cada usuario, minimizando la interferencia inter-usuario. Para ello, el AP necesita conocer el canal hacia cada STA, lo que se logra mediante el proceso de **channel sounding** con tramas NDP.

La tasa total del sistema con MU-MIMO puede expresarse como:

$$R_{\text{total}} = \sum_{k=1}^{K} R_k = \sum_{k=1}^{K} N_{s,k} \cdot r_k$$

donde $K$ es el número de usuarios simultáneos (hasta 4 en WiFi 5), $N_{s,k}$ es el número de flujos espaciales asignados al usuario $k$, y $r_k$ es la tasa por flujo del usuario $k$.

#### 6.2.3 256-QAM vs 64-QAM: Explicación Detallada de QAM

**QAM (Quadrature Amplitude Modulation)** es un esquema de modulación digital que combina modulación de amplitud en dos portadoras en cuadratura (desfasadas 90°). Cada símbolo QAM se representa como un punto en el plano complejo (diagrama de constelación), definido por una amplitud $I$ (in-phase) y una amplitud $Q$ (quadrature):

$$s(t) = I \cdot \cos(2\pi f_c t) - Q \cdot \sin(2\pi f_c t)$$

donde $f_c$ es la frecuencia de la portadora, $I$ y $Q$ son las componentes en fase y en cuadratura respectivamente.

En un esquema $M$-QAM, existen $M$ puntos posibles en la constelación, cada uno representando una combinación única de $\log_2(M)$ bits:

| Modulación | $M$ | Bits/símbolo ($\log_2 M$) | Uso en WiFi |
|:---:|:---:|:---:|:---:|
| BPSK | 2 | 1 | MCS 0 |
| QPSK | 4 | 2 | MCS 1-2 |
| 16-QAM | 16 | 4 | MCS 3-4 |
| 64-QAM | 64 | 6 | MCS 5-7 (WiFi 4) |
| 256-QAM | 256 | 8 | MCS 8-9 (WiFi 5) |
| 1024-QAM | 1024 | 10 | MCS 10-11 (WiFi 6) |

**Diagrama de constelación de 64-QAM:** La constelación forma una cuadrícula de $8 \times 8 = 64$ puntos uniformemente espaciados. Cada punto codifica 6 bits (por ejemplo, el punto en la esquina superior derecha podría representar "000000" y el punto inferior izquierdo "111111", usando codificación Gray para minimizar errores de bit en puntos adyacentes). La distancia mínima entre puntos adyacentes determina la robustez frente al ruido.

**Diagrama de constelación de 256-QAM:** La constelación forma una cuadrícula de $16 \times 16 = 256$ puntos. Al duplicar el número de niveles en cada eje (de 8 a 16), los puntos están más cercanos entre sí para la misma potencia promedio de señal, lo que exige un SNR más alto para decodificar correctamente. Cada punto codifica 8 bits.

**Descripción de Figura — Constelaciones QAM:**

> *La Figura 6.1 muestra tres diagramas de constelación lado a lado. A la izquierda, la constelación 64-QAM: una cuadrícula regular de 8×8 = 64 puntos azules en el plano I-Q, con ejes I (horizontal) y Q (vertical). Los puntos están espaciados uniformemente, y cada punto lleva una etiqueta de 6 bits en codificación Gray. La distancia mínima entre puntos adyacentes se marca con una línea roja y la etiqueta $d_{\min}$. En el centro, la constelación 256-QAM: una cuadrícula de 16×16 = 256 puntos verdes, más densamente empaquetados. Se observa claramente que $d_{\min}$ es menor que en 64-QAM para la misma potencia media. A la derecha, un gráfico de barras compara los bits por símbolo: 6 bits para 64-QAM y 8 bits para 256-QAM, con una flecha indicando la mejora del 33%. Debajo de cada constelación se indica el requisito aproximado de SNR: ~24 dB para 64-QAM y ~30 dB para 256-QAM.*

La ganancia de eficiencia espectral al pasar de 64-QAM a 256-QAM es:

$$\text{Ganancia} = \frac{\log_2(256) - \log_2(64)}{\log_2(64)} \times 100\% = \frac{8 - 6}{6} \times 100\% = 33.3\%$$

Sin embargo, esta ganancia tiene un costo: el SNR requerido para decodificar 256-QAM correctamente es aproximadamente 6 dB mayor que para 64-QAM, lo que significa que 256-QAM solo es utilizable cuando el dispositivo está relativamente cerca del AP y el canal es de buena calidad.

#### 6.2.4 Beamforming Obligatorio

**Beamforming** (conformación de haz) es una técnica de procesamiento de señales que utiliza múltiples antenas para dirigir la energía de la señal transmitida hacia la ubicación del receptor deseado, en lugar de radiar en todas las direcciones por igual. Esto aumenta la potencia recibida por el dispositivo destino y reduce la interferencia hacia otros dispositivos.

En un arreglo de $N$ antenas, la señal transmitida por cada antena se multiplica por un peso complejo $w_n$. La ganancia del arreglo en la dirección del receptor es:

$$G_{\text{BF}} = \left| \sum_{n=0}^{N-1} w_n \cdot e^{j \cdot n \cdot k \cdot d \cdot \sin(\theta)} \right|^2$$

donde $k = 2\pi/\lambda$ es el número de onda, $d$ es la separación entre antenas (típicamente $\lambda/2$), $\theta$ es el ángulo de llegada y $w_n$ son los pesos de beamforming calculados a partir de la información de canal (CSI).

Si los pesos se eligen de forma óptima (conjugado del canal, $w_n = h_n^*$), la ganancia de beamforming para $N$ antenas es:

$$G_{\text{BF, máx}} = 10 \log_{10}(N) \quad \text{[dB]}$$

Por ejemplo, un AP con $N = 4$ antenas puede lograr una ganancia de beamforming de $10\log_{10}(4) = 6$ dB, lo que equivale a cuadruplicar la potencia efectiva en la dirección del receptor.

En WiFi 5, el proceso de beamforming funciona así:

1. El AP envía una trama **NDP Announcement** seguida de una trama **NDP** (Null Data Packet).
2. La STA estima el canal a partir del NDP y calcula una **matriz de beamforming comprimida** $\mathbf{V}$ (usando descomposición SVD del canal).
3. La STA envía la matriz $\mathbf{V}$ al AP en una trama **Beamforming Report**.
4. El AP utiliza $\mathbf{V}$ para precodificar las transmisiones futuras hacia esa STA.

**Descripción de Figura — Beamforming:**

> *La Figura 6.2 ilustra el concepto de beamforming. En la parte superior, se muestra un AP con 4 antenas transmitiendo sin beamforming: el patrón de radiación es omnidireccional (un círculo azul claro que irradia uniformemente en todas las direcciones), y la potencia recibida por la STA objetivo es baja. En la parte inferior, el mismo AP con beamforming activado: el patrón de radiación se concentra en un lóbulo principal (color verde intenso) dirigido hacia la STA objetivo, mientras que en otras direcciones la radiación es mínima (lóbulos secundarios pequeños). Flechas indican las señales de cada antena, mostrando que cada una transmite con una fase ligeramente diferente ($\phi_1, \phi_2, \phi_3, \phi_4$) para lograr la interferencia constructiva en la dirección deseada. Un diagrama polar a la derecha cuantifica la diferencia: la ganancia en la dirección de la STA pasa de 0 dBi (sin beamforming) a +6 dBi (con beamforming de 4 antenas).*

### 6.3 Cálculo de Velocidad PHY WiFi 5

La velocidad de la capa física (PHY rate) en WiFi 5 se calcula mediante la siguiente fórmula:

$$R_{\text{PHY}} = N_{SS} \times N_{SD} \times b \times R_c \times \frac{1}{T_{\text{SYM}}}$$

donde cada variable tiene el siguiente significado:

- $N_{SS}$: **Número de flujos espaciales** (spatial streams). Es el número de flujos de datos independientes transmitidos simultáneamente mediante MIMO. WiFi 5 soporta de 1 a 8 flujos. El número de flujos está limitado por $\min(N_{TX}, N_{RX})$, donde $N_{TX}$ y $N_{RX}$ son el número de antenas del transmisor y receptor.

- $N_{SD}$: **Número de subportadoras de datos** por símbolo OFDM. En OFDM, el canal se divide en múltiples subportadoras ortogonales. No todas transportan datos: algunas son subportadoras piloto (para estimación de canal), subportadoras nulas (en los bordes del canal) y la subportadora DC (en el centro). Los valores de $N_{SD}$ en WiFi 5 son:
  - 20 MHz: $N_{SD} = 52$
  - 40 MHz: $N_{SD} = 108$
  - 80 MHz: $N_{SD} = 234$
  - 160 MHz: $N_{SD} = 468$

- $b$: **Bits por símbolo de modulación** ($\log_2 M$, donde $M$ es el orden de modulación). Los valores dependen del MCS (Modulation and Coding Scheme):
  - BPSK: $b = 1$
  - QPSK: $b = 2$
  - 16-QAM: $b = 4$
  - 64-QAM: $b = 6$
  - 256-QAM: $b = 8$

- $R_c$: **Tasa de codificación** (code rate). Es la proporción de bits de información respecto al total de bits transmitidos (datos + redundancia). WiFi 5 utiliza codificación BCC (Binary Convolutional Coding) o LDPC (Low-Density Parity-Check). Valores típicos: $1/2$, $2/3$, $3/4$, $5/6$.

- $T_{\text{SYM}}$: **Duración del símbolo OFDM**, que incluye la duración útil del símbolo más el intervalo de guarda (GI). En WiFi 5:
  - Duración útil del símbolo: $T_{\text{FFT}} = 3.2 \, \mu\text{s}$
  - Intervalo de guarda normal: $T_{\text{GI}} = 0.8 \, \mu\text{s}$, resultando en $T_{\text{SYM}} = 3.2 + 0.8 = 4.0 \, \mu\text{s}$
  - Intervalo de guarda corto: $T_{\text{GI}} = 0.4 \, \mu\text{s}$, resultando en $T_{\text{SYM}} = 3.2 + 0.4 = 3.6 \, \mu\text{s}$

**Estructura del símbolo OFDM en WiFi 5:**

Un símbolo OFDM consiste en dos partes:

1. **Periodo útil ($T_{\text{FFT}}$):** Es la parte del símbolo que contiene la información. Se genera aplicando una IFFT (Transformada Rápida de Fourier Inversa) a los datos modulados en las subportadoras. En WiFi 5, $T_{\text{FFT}} = 3.2 \, \mu\text{s}$, lo que corresponde a un espaciado entre subportadoras de:

$$\Delta f = \frac{1}{T_{\text{FFT}}} = \frac{1}{3.2 \times 10^{-6}} = 312.5 \, \text{kHz}$$

2. **Intervalo de guarda ($T_{\text{GI}}$):** Es una copia cíclica del final del símbolo que se antepone al inicio. Su propósito es absorber la dispersión temporal del canal (multipath), evitando la interferencia intersimbólica (ISI). Si el retardo máximo de propagación multitrayecto ($\tau_{\max}$) es menor que $T_{\text{GI}}$, no habrá ISI. En WiFi 5, el GI estándar es $0.8 \, \mu\text{s}$ y el corto es $0.4 \, \mu\text{s}$. El GI corto solo debe usarse cuando el entorno de propagación tiene poca dispersión temporal.

**Ejemplo numérico completo — Velocidad máxima de WiFi 5:**

Calculemos la velocidad PHY máxima teórica con la configuración más agresiva:

Parámetros:
- $N_{SS} = 8$ (8 flujos espaciales, 8×8 MIMO)
- $N_{SD} = 468$ (canal de 160 MHz)
- $b = 8$ (256-QAM)
- $R_c = 5/6$ (MCS 9)
- $T_{\text{SYM}} = 3.6 \, \mu\text{s}$ (GI corto de 0.4 μs)

Sustituyendo:

$$R_{\text{PHY}} = 8 \times 468 \times 8 \times \frac{5}{6} \times \frac{1}{3.6 \times 10^{-6}}$$

Paso a paso:

$$R_{\text{PHY}} = 8 \times 468 \times 8 \times 0.8333 \times 277{,}778$$

$$= 8 \times 468 \times 8 \times 0.8333 \times 277{,}778$$

Primero: $8 \times 468 = 3{,}744$

Luego: $3{,}744 \times 8 = 29{,}952$ bits por símbolo OFDM (antes de coding)

Con code rate: $29{,}952 \times 5/6 = 24{,}960$ bits de información por símbolo

Tasa: $24{,}960 / 3.6 \times 10^{-6} = 6{,}933{,}333{,}333$ bps

$$\boxed{R_{\text{PHY, máx}} = 6.93 \, \text{Gbps}}$$

**Ejemplo para una configuración común — Laptop con WiFi 5 (2×2, 80 MHz):**

- $N_{SS} = 2$
- $N_{SD} = 234$ (80 MHz)
- $b = 8$ (256-QAM, MCS 9)
- $R_c = 5/6$
- $T_{\text{SYM}} = 3.6 \, \mu\text{s}$ (GI corto)

$$R_{\text{PHY}} = 2 \times 234 \times 8 \times \frac{5}{6} \times \frac{1}{3.6 \times 10^{-6}}$$

$$= 2 \times 234 \times 8 \times 0.8333 \times 277{,}778$$

$$= 2 \times 234 = 468$$

$$468 \times 8 = 3{,}744$$

$$3{,}744 \times 0.8333 = 3{,}120$$

$$3{,}120 \times 277{,}778 = 866{,}666{,}667 \, \text{bps}$$

$$\boxed{R_{\text{PHY}} = 866.7 \, \text{Mbps}}$$

**Tabla 6.1 — Velocidades PHY comunes de WiFi 5 (GI = 0.4 μs)**

| Config. MIMO | Ancho Canal | MCS | Modulación | $R_c$ | Velocidad PHY |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 1×1 | 20 MHz | 9 | 256-QAM | 5/6 | 96.3 Mbps |
| 1×1 | 40 MHz | 9 | 256-QAM | 5/6 | 200 Mbps |
| 1×1 | 80 MHz | 9 | 256-QAM | 5/6 | 433.3 Mbps |
| 2×2 | 80 MHz | 9 | 256-QAM | 5/6 | 866.7 Mbps |
| 3×3 | 80 MHz | 9 | 256-QAM | 5/6 | 1.3 Gbps |
| 4×4 | 80 MHz | 9 | 256-QAM | 5/6 | 1.73 Gbps |
| 4×4 | 160 MHz | 9 | 256-QAM | 5/6 | 3.47 Gbps |
| 8×8 | 160 MHz | 9 | 256-QAM | 5/6 | 6.93 Gbps |

### 6.4 Canales en 5 GHz

La banda de 5 GHz ofrece significativamente más espectro que la banda de 2.4 GHz, pero está dividida en varias sub-bandas con distintas regulaciones. En Estados Unidos (regulación FCC), estas sub-bandas se denominan **UNII** (Unlicensed National Information Infrastructure):

- **UNII-1 (5.150–5.250 GHz):** Canales 36, 40, 44, 48. Originalmente limitada a uso interior con potencia máxima de 200 mW (23 dBm) EIRP. No requiere DFS. Es la sub-banda más utilizada para WiFi.

- **UNII-2A (5.250–5.350 GHz):** Canales 52, 56, 60, 64. Potencia máxima de 250 mW (24 dBm) EIRP. **Requiere DFS** (Dynamic Frequency Selection) porque comparte espectro con sistemas de radar meteorológico y militar.

- **UNII-2C / UNII-2 Extended (5.470–5.725 GHz):** Canales 100 a 144 (con algunas exclusiones por región). Potencia máxima de 1 W (30 dBm) EIRP. **Requiere DFS y TPC** (Transmit Power Control). Proporciona la mayor cantidad de espectro, pero es la banda más afectada por radares.

- **UNII-3 (5.725–5.850 GHz):** Canales 149, 153, 157, 161, 165. Potencia máxima de 1 W (30 dBm) EIRP. No requiere DFS. Es popular en exteriores.

**Numeración de canales:** Los canales WiFi en 5 GHz se numeran según la fórmula:

$$f_c = 5000 + 5 \times n \quad \text{[MHz]}$$

donde $n$ es el número de canal y $f_c$ es la frecuencia central. Por ejemplo, el canal 36 tiene frecuencia central $f_c = 5000 + 5 \times 36 = 5180$ MHz.

**Channel Bonding (Agregación de Canales):**

Channel bonding es la técnica de combinar canales adyacentes de 20 MHz para formar un canal más ancho. En WiFi 5:

- **40 MHz:** Se combinan 2 canales de 20 MHz. Ejemplo: canales 36+40 forman un canal de 40 MHz centrado en 5190 MHz. Se designa como canal 38 (40 MHz).

- **80 MHz:** Se combinan 4 canales de 20 MHz. Ejemplo: canales 36+40+44+48 forman un canal de 80 MHz centrado en 5210 MHz. Se designa como canal 42 (80 MHz). En UNII-1, solo hay **un** canal de 80 MHz disponible.

- **160 MHz:** Se combinan 8 canales de 20 MHz. Ejemplo: canales 36+40+44+48+52+56+60+64 forman un canal de 160 MHz. Alternativamente, se puede usar **80+80 MHz**: dos canales de 80 MHz no contiguos (por ejemplo, canal 42 de 80 MHz en UNII-1 + canal 155 de 80 MHz en UNII-3), tratados lógicamente como un canal de 160 MHz.

En total, la banda de 5 GHz ofrece aproximadamente:
- **25** canales de 20 MHz (varía por región)
- **12** canales de 40 MHz no solapados
- **6** canales de 80 MHz no solapados
- **2** canales de 160 MHz contiguos (o más en 80+80)

**DFS (Dynamic Frequency Selection):**

DFS es un mecanismo regulatorio que obliga a los dispositivos WiFi a detectar señales de radar y evacuar el canal si se detecta un radar. El proceso funciona así:

1. **CAC (Channel Availability Check):** Antes de transmitir en un canal DFS, el AP debe escuchar durante **60 segundos** (o 600 segundos en canales de banda meteorológica) para verificar que no hay radar presente.

2. **In-Service Monitoring:** Durante la operación normal, el AP monitorea continuamente el canal. Si detecta un pulso de radar, debe cesar las transmisiones en **200 ms** y mover todas las STAs a un canal limpio.

3. **Non-Occupancy Period:** Después de detectar un radar, el AP no puede regresar al canal afectado durante al menos **30 minutos**.

DFS amplía significativamente el espectro utilizable en 5 GHz, pero introduce complejidad operativa y puede causar interrupciones breves cuando se detecta un radar (real o falso positivo).

**Descripción de Figura — Asignación de Canales en 5 GHz:**

> *La Figura 6.3 muestra el espectro de la banda de 5 GHz como una barra horizontal que abarca de 5.150 a 5.850 GHz. La barra está dividida en cuatro secciones coloreadas: UNII-1 (verde, 5.150–5.250 GHz, canales 36-48), UNII-2A (amarillo, 5.250–5.350 GHz, canales 52-64, etiquetada "DFS"), UNII-2C (naranja, 5.470–5.725 GHz, canales 100-144, etiquetada "DFS + TPC"), y UNII-3 (azul, 5.725–5.850 GHz, canales 149-165). Debajo de la barra, se muestran rectángulos superpuestos que ilustran el channel bonding: rectángulos estrechos de 20 MHz para canales individuales (36, 40, 44, 48...), rectángulos medianos de 40 MHz que engloban pares (36+40, 44+48...), rectángulos anchos de 80 MHz que engloban cuatro canales, y un rectángulo muy ancho de 160 MHz que cruza de UNII-1 a UNII-2A. Un ícono de radar con un símbolo de advertencia aparece sobre las bandas UNII-2A y UNII-2C.*

### 6.5 Link Budget WiFi 5

El **link budget** (presupuesto de enlace) es un cálculo que determina si una señal transmitida llegará al receptor con suficiente potencia para ser decodificada correctamente. Es fundamental para el diseño de cobertura de redes WiFi. La ecuación general del link budget es:

$$P_{RX} = P_{TX} + G_{TX} - L_{TX} - L_{\text{path}} + G_{RX} - L_{RX}$$

donde:
- $P_{RX}$: Potencia recibida [dBm]
- $P_{TX}$: Potencia transmitida [dBm]
- $G_{TX}$: Ganancia de la antena transmisora [dBi]
- $L_{TX}$: Pérdidas en el transmisor (cables, conectores) [dB]
- $L_{\text{path}}$: Pérdida de propagación en el trayecto [dB]
- $G_{RX}$: Ganancia de la antena receptora [dBi]
- $L_{RX}$: Pérdidas en el receptor [dB]

Para que el enlace funcione, se debe cumplir:

$$P_{RX} \geq S_{\min} + M_{\text{fade}}$$

donde $S_{\min}$ es la **sensibilidad del receptor** (la potencia mínima necesaria para decodificar la señal con una tasa de error aceptable) y $M_{\text{fade}}$ es un **margen de desvanecimiento** que protege contra fluctuaciones de la señal (típicamente 6–10 dB).

**Pérdida en espacio libre (FSPL) a 5 GHz:**

La pérdida de propagación en espacio libre se calcula con la ecuación de Friis:

$$L_{\text{FSPL}} = 20\log_{10}(d) + 20\log_{10}(f) + 32.44 \quad \text{[dB]}$$

donde $d$ es la distancia en km y $f$ es la frecuencia en MHz.

Para WiFi a 5 GHz (tomando 5.5 GHz = 5500 MHz), a una distancia de referencia de $d = 0.01$ km (10 metros):

$$L_{\text{FSPL}} = 20\log_{10}(0.01) + 20\log_{10}(5500) + 32.44$$

$$= -40 + 74.81 + 32.44 = 67.25 \, \text{dB}$$

**Ejemplo numérico completo — Link Budget WiFi 5 (Interior):**

Diseñemos el enlace descendente para un AP WiFi 5 en un entorno de oficina interior.

*Datos del transmisor (AP):*
- $P_{TX} = 20$ dBm (100 mW, potencia típica de AP indoor)
- $G_{TX} = 5$ dBi (antena omnidireccional con ganancia moderada)
- $L_{TX} = 1$ dB (pérdidas internas)
- Beamforming: ganancia adicional de $G_{\text{BF}} = 3$ dB (AP 2×2)

*Datos del receptor (STA — laptop):*
- $G_{RX} = 2$ dBi (antena integrada)
- $L_{RX} = 0$ dB
- Sensibilidad para MCS 9, 80 MHz: $S_{\min} = -57$ dBm
- Sensibilidad para MCS 7, 80 MHz: $S_{\min} = -66$ dBm
- Sensibilidad para MCS 0, 80 MHz: $S_{\min} = -82$ dBm

*Margen de desvanecimiento:* $M_{\text{fade}} = 8$ dB

*Modelo de propagación interior:* Para un entorno de oficina, usamos un modelo de pérdida logarítmica:

$$L_{\text{path}}(d) = L_0 + 10 \cdot n \cdot \log_{10}\left(\frac{d}{d_0}\right) + \sum L_{\text{pared}}$$

donde $L_0 = 67.25$ dB es la pérdida a $d_0 = 10$ m (calculada arriba), $n = 3.5$ es el exponente de pérdida en interior, y $\sum L_{\text{pared}}$ son las pérdidas adicionales por paredes.

*Cálculo — ¿A qué distancia máxima funciona MCS 9 (256-QAM, 866.7 Mbps)?*

Potencia recibida necesaria:

$$P_{RX, \min} = S_{\min} + M_{\text{fade}} = -57 + 8 = -49 \, \text{dBm}$$

Pérdida máxima permitida:

$$L_{\text{path, máx}} = P_{TX} + G_{TX} - L_{TX} + G_{\text{BF}} + G_{RX} - L_{RX} - P_{RX, \min}$$

$$L_{\text{path, máx}} = 20 + 5 - 1 + 3 + 2 - 0 - (-49) = 78 \, \text{dB}$$

Distancia máxima (sin paredes):

$$78 = 67.25 + 10 \times 3.5 \times \log_{10}\left(\frac{d}{10}\right)$$

$$10.75 = 35 \times \log_{10}\left(\frac{d}{10}\right)$$

$$\log_{10}\left(\frac{d}{10}\right) = 0.307$$

$$\frac{d}{10} = 10^{0.307} = 2.03$$

$$\boxed{d_{\max} \approx 20.3 \, \text{m} \quad \text{(MCS 9, 256-QAM, sin paredes)}}$$

Si añadimos 2 paredes de yeso ($L_{\text{pared}} = 3$ dB cada una, total 6 dB):

$$L_{\text{path, máx}} = 78 - 6 = 72 \, \text{dB}$$

$$72 = 67.25 + 35 \times \log_{10}\left(\frac{d}{10}\right)$$

$$\log_{10}\left(\frac{d}{10}\right) = \frac{4.75}{35} = 0.136$$

$$d = 10 \times 10^{0.136} = 10 \times 1.37 = 13.7 \, \text{m}$$

Para **MCS 0** (BPSK, mayor alcance, $S_{\min} = -82$ dBm):

$$P_{RX, \min} = -82 + 8 = -74 \, \text{dBm}$$

$$L_{\text{path, máx}} = 20 + 5 - 1 + 3 + 2 - 0 - (-74) = 103 \, \text{dB}$$

$$103 = 67.25 + 35 \times \log_{10}\left(\frac{d}{10}\right)$$

$$\log_{10}\left(\frac{d}{10}\right) = \frac{35.75}{35} = 1.021$$

$$d = 10 \times 10^{1.021} = 10 \times 10.5 = 105 \, \text{m}$$

$$\boxed{d_{\max} \approx 105 \, \text{m} \quad \text{(MCS 0, BPSK, sin paredes)}}$$

Este resultado muestra la adaptación de velocidad en WiFi 5: cerca del AP (< 20 m) se puede disfrutar de velocidades de 866 Mbps con 256-QAM, mientras que a distancias mayores el sistema reduce automáticamente la modulación, sacrificando velocidad a cambio de mayor alcance y confiabilidad, hasta llegar a cobertura básica (~105 m con BPSK, pero a solo unos pocos Mbps).

---

## 7. WiFi 6 (IEEE 802.11ax)

### 7.1 Motivaciones y Contexto

WiFi 6, formalmente definido por la enmienda **IEEE 802.11ax**, fue aprobado en febrero de 2021 (aunque la certificación Wi-Fi Alliance comenzó en septiembre de 2020). A diferencia de generaciones anteriores que se enfocaban en incrementar la velocidad máxima individual, WiFi 6 fue diseñado con una filosofía fundamentalmente diferente: **mejorar la eficiencia de la red en entornos densos**.

**El problema de las redes densas:** El número de dispositivos WiFi por hogar pasó de un promedio de 5 en 2015 a más de 15 en 2020, y se proyectan más de 25 para 2025. En entornos como estadios, aeropuertos, centros de convenciones y campus universitarios, miles de dispositivos compiten por el mismo espectro. En estos escenarios, la velocidad máxima teórica del estándar es irrelevante; lo que importa es el **rendimiento por usuario**, la **latencia** y la **equidad** en el acceso al medio.

**El cambio de paradigma:** WiFi 5 buscaba maximizar la velocidad pico ($R_{\text{pico}}$), pero en redes densas el rendimiento efectivo por usuario es:

$$R_{\text{usuario}} = \frac{R_{\text{pico}} \times \eta_{\text{MAC}}}{N_{\text{usuarios}}}$$

donde $\eta_{\text{MAC}}$ es la eficiencia de la capa MAC (típicamente 50–70% en WiFi 5 debido al overhead de contención y headers) y $N_{\text{usuarios}}$ es el número de usuarios activos. WiFi 6 ataca tanto el numerador (incrementando $R_{\text{pico}}$ y $\eta_{\text{MAC}}$) como el denominador conceptual, permitiendo servir a múltiples usuarios **simultáneamente** en el dominio de frecuencia (OFDMA) además del dominio espacial (MU-MIMO).

**El problema de la superposición de BSS (BSS overlap):** En despliegues densos, múltiples APs operan en los mismos canales. En WiFi 5, cuando una STA detecta cualquier trama WiFi (incluso de un BSS vecino) con potencia superior al umbral de detección de energía (Energy Detection, $-62$ dBm) o al umbral de detección de preámbulo ($-82$ dBm), debe diferir su transmisión. Esto crea un efecto de "zona muerta" donde la interferencia de BSSs vecinos impide que las STAs de un BSS dado accedan al medio, aunque la señal de su propio AP sea fuerte. WiFi 6 aborda este problema con **BSS Coloring** (Sección 7.5).

### 7.2 OFDMA (Orthogonal Frequency Division Multiple Access)

#### Explicación detallada de OFDMA vs OFDM

**OFDM** (Orthogonal Frequency Division Multiplexing), utilizado en WiFi 4 y WiFi 5, divide el canal en múltiples subportadoras ortogonales. Sin embargo, en cada instante de transmisión (símbolo OFDM), **todas las subportadoras se asignan a un único usuario**. Si el AP necesita enviar datos a 4 usuarios, debe servir a cada uno secuencialmente, uno tras otro, en el dominio del tiempo. Esto introduce latencia y overhead por la contención de acceso al medio para cada transmisión individual.

**OFDMA** (Orthogonal Frequency Division Multiple Access), introducido en WiFi 6, permite dividir las subportadoras en grupos llamados **Resource Units (RUs)** y asignar diferentes RUs a diferentes usuarios **simultáneamente** dentro del mismo símbolo OFDM. De esta forma, múltiples usuarios transmiten (o reciben) datos al mismo tiempo, compartiendo el canal en el dominio de la frecuencia.

**Analogía pedagógica — La autopista:**

Imagine OFDM como una autopista de 4 carriles donde solo un vehículo puede circular a la vez, aunque sea muy pequeño y solo necesite un carril: la autopista completa se reserva para cada vehículo en su turno. OFDMA convierte esa autopista en una carretera donde los carriles se asignan independientemente: un camión puede usar 2 carriles mientras dos motocicletas usan un carril cada una, todos circulando simultáneamente. Para paquetes pequeños (confirmaciones de IoT, mensajes cortos), OFDMA es dramáticamente más eficiente porque evita desperdiciar el ancho de canal completo para una transmisión mínima.

#### Resource Units (RUs)

Las subportadoras de un canal se agrupan en **Resource Units (RUs)** de varios tamaños:

| RU | Subportadoras de datos | Subportadoras totales | Ancho aprox. |
|:---:|:---:|:---:|:---:|
| 26-tone RU | 24 | 26 | ~2 MHz |
| 52-tone RU | 48 | 52 | ~4 MHz |
| 106-tone RU | 102 | 106 | ~8 MHz |
| 242-tone RU | 234 | 242 | ~20 MHz |
| 484-tone RU | 468 | 484 | ~40 MHz |
| 996-tone RU | 980 | 996 | ~80 MHz |

El número y tipo de RUs disponibles depende del ancho del canal:

- **20 MHz (242 tonos totales):** Se puede dividir en:
  - 1 × RU-242 (1 usuario, ancho completo), o
  - 2 × RU-106 + 1 × RU-26, o
  - 4 × RU-52 + 1 × RU-26, o
  - 9 × RU-26, o
  - otras combinaciones válidas.

- **40 MHz (484 tonos totales):** Hasta 18 × RU-26 o 1 × RU-484.

- **80 MHz (996 tonos totales):** Hasta 37 × RU-26 o 1 × RU-996.

- **160 MHz (2×996 tonos totales):** Hasta 74 × RU-26 o 2 × RU-996.

#### Uplink y Downlink OFDMA

Una innovación clave de WiFi 6 es que OFDMA funciona tanto en **downlink** (DL) como en **uplink** (UL).

- **DL-OFDMA:** El AP divide su transmisión en RUs y envía datos a múltiples STAs simultáneamente. El AP controla completamente la asignación de RUs.

- **UL-OFDMA:** El AP envía una **Trigger Frame** (trama de activación) que indica a cada STA en qué RU debe transmitir y con qué parámetros (potencia, MCS). Las STAs transmiten simultáneamente en sus RUs asignados, de forma coordinada. Esto es revolucionario porque el uplink en WiFi siempre había sido gobernado exclusivamente por contención (CSMA/CA); ahora el AP puede programar el acceso de las STAs, evitando colisiones y mejorando la eficiencia.

#### Ejemplo numérico — Eficiencia de OFDMA

Considere un escenario con un AP WiFi 6 y 9 dispositivos IoT, cada uno con un paquete pequeño de 100 bytes para enviar. El canal es de 20 MHz.

**Sin OFDMA (WiFi 5 / OFDM):**

Cada dispositivo debe esperar su turno. Asumiendo un overhead MAC de $T_{\text{overhead}} = 200 \, \mu\text{s}$ (incluye DIFS, backoff, preámbulo, ACK, SIFS) y un tiempo de transmisión de datos de $T_{\text{datos}} = 50 \, \mu\text{s}$ por paquete:

$$T_{\text{total, OFDM}} = 9 \times (T_{\text{overhead}} + T_{\text{datos}}) = 9 \times 250 = 2{,}250 \, \mu\text{s}$$

Eficiencia:

$$\eta_{\text{OFDM}} = \frac{9 \times T_{\text{datos}}}{T_{\text{total}}} = \frac{9 \times 50}{2{,}250} = 20\%$$

**Con UL-OFDMA (WiFi 6):**

El AP envía una Trigger Frame ($T_{\text{TF}} \approx 100 \, \mu\text{s}$) que asigna un RU-26 a cada dispositivo. Los 9 dispositivos transmiten simultáneamente, cada uno en su RU de 26 tonos. Como los RUs son $\approx 1/9$ del canal de 20 MHz, la transmisión tarda $T_{\text{datos, RU}} = 50 \times 9 = 450 \, \mu\text{s}$ (misma cantidad de datos, pero en un ancho de banda 9 veces menor, por lo que tarda 9 veces más). Sin embargo, solo hay **un** evento de contención y overhead:

$$T_{\text{total, OFDMA}} = T_{\text{overhead}} + T_{\text{TF}} + T_{\text{datos, RU}} = 200 + 100 + 450 = 750 \, \mu\text{s}$$

Eficiencia:

$$\eta_{\text{OFDMA}} = \frac{9 \times T_{\text{datos}}}{T_{\text{total}}} = \frac{9 \times 50}{750} = 60\%$$

$$\boxed{\text{Mejora de eficiencia: } \frac{60\%}{20\%} = 3\times}$$

**Descripción de Figura — OFDM vs OFDMA:**

> *La Figura 7.1 compara OFDM (WiFi 5) con OFDMA (WiFi 6) mediante dos diagramas de tiempo-frecuencia. En el diagrama superior (OFDM), el eje horizontal representa el tiempo y el vertical la frecuencia (subportadoras). En cada intervalo de tiempo, todo el ancho del canal (representado como un bloque rectangular ancho) se asigna a un solo usuario, coloreado de un color distinto: azul para Usuario 1 en el intervalo $t_1$, rojo para Usuario 2 en $t_2$, verde para Usuario 3 en $t_3$, y amarillo para Usuario 4 en $t_4$. Los usuarios se atienden secuencialmente, y entre cada bloque hay un espacio gris que representa el overhead de contención (DIFS + backoff). En el diagrama inferior (OFDMA), en un único intervalo de tiempo $t_1$, el canal se divide verticalmente en 4 Resource Units: las subportadoras inferiores (RU-1, azul) para Usuario 1, las siguientes (RU-2, rojo) para Usuario 2, las siguientes (RU-3, verde) para Usuario 3, y las superiores (RU-4, amarillo) para Usuario 4. Los cuatro usuarios transmiten simultáneamente, y solo hay un overhead de contención. Una flecha indica que el tiempo total en OFDMA es significativamente menor.*

### 7.3 1024-QAM

WiFi 6 introduce la modulación **1024-QAM**, que corresponde a los niveles MCS 10 y MCS 11 del estándar 802.11ax.

**Constelación 1024-QAM:** La constelación es una cuadrícula de $32 \times 32 = 1{,}024$ puntos en el plano I-Q. Cada símbolo codifica:

$$b = \log_2(1024) = 10 \, \text{bits/símbolo}$$

Comparación directa con 256-QAM ($\log_2(256) = 8$ bits/símbolo):

$$\text{Mejora} = \frac{10 - 8}{8} \times 100\% = 25\%$$

Esto significa un incremento del 25% en la eficiencia espectral respecto a WiFi 5, para la misma configuración de canal y MIMO.

**Requisitos de SNR:** La distancia mínima entre puntos adyacentes en una constelación $M$-QAM normalizada (energía promedio unitaria) es:

$$d_{\min} = \sqrt{\frac{6}{M - 1}}$$

Para 256-QAM: $d_{\min} = \sqrt{6/255} = 0.153$

Para 1024-QAM: $d_{\min} = \sqrt{6/1023} = 0.0766$

La distancia mínima se reduce a la mitad, lo que significa que el receptor necesita distinguir entre puntos mucho más cercanos. En la práctica, 1024-QAM requiere un SNR de al menos **35 dB** (comparado con ~30 dB para 256-QAM y ~24 dB para 64-QAM).

**¿Cuándo es práctico usar 1024-QAM?** Solo en condiciones de canal excelentes: distancias cortas (< 5-10 m del AP), sin obstrucciones, con mínima interferencia, y con dispositivos de alta calidad que tengan bajo ruido de fase y alta linealidad en la cadena de RF. En un entorno de oficina típico, 1024-QAM podría estar disponible solo en las posiciones más cercanas al AP. Según mediciones de campo, 1024-QAM típicamente solo puede utilizarse en el 10-20% del área de cobertura de un BSS, dependiendo de la densidad de usuarios y el entorno.

**Descripción de Figura — Constelaciones QAM:**

> *La Figura 7.2 muestra tres constelaciones QAM en diagramas I-Q de igual escala para facilitar la comparación visual. A la izquierda, la constelación 64-QAM (WiFi 4/5) con 8×8 = 64 puntos azules bien separados entre sí; la etiqueta "6 bits/símbolo" aparece debajo. En el centro, la constelación 256-QAM (WiFi 5) con 16×16 = 256 puntos verdes más densamente empaquetados; etiqueta "8 bits/símbolo". A la derecha, la constelación 1024-QAM (WiFi 6) con 32×32 = 1024 puntos rojos extremadamente densos, casi formando un cuadrado sólido; etiqueta "10 bits/símbolo". Debajo de las tres constelaciones, un gráfico de barras muestra el SNR requerido: ~24 dB (64-QAM), ~30 dB (256-QAM), ~35 dB (1024-QAM). Líneas punteadas conectan cada barra con su constelación correspondiente. Una nota señala: "Mayor eficiencia → Mayor requisito de SNR → Menor alcance".*

### 7.4 MU-MIMO Bidireccional

WiFi 6 expande significativamente las capacidades MU-MIMO respecto a WiFi 5:

| Característica | WiFi 5 (802.11ac) | WiFi 6 (802.11ax) |
|:---|:---:|:---:|
| Flujos espaciales máx. | 8 | 8 |
| MU-MIMO Downlink | Sí (hasta 4 usuarios) | Sí (hasta 8 usuarios) |
| MU-MIMO Uplink | No | Sí (hasta 8 usuarios) |
| Máx. usuarios MU-MIMO simultáneos | 4 (solo DL) | 8 (DL) + 8 (UL) |

**MU-MIMO en Uplink (UL MU-MIMO):** Esta es una innovación significativa. En WiFi 5, el uplink siempre era SU-MIMO: solo una STA podía transmitir al AP en cada instante. En WiFi 6, el AP puede recibir transmisiones simultáneas de hasta 8 STAs, cada una en diferentes flujos espaciales. El AP coordina la transmisión UL MU-MIMO mediante **Trigger Frames**, similar al UL-OFDMA. De hecho, WiFi 6 permite combinar **UL-OFDMA con UL MU-MIMO**: diferentes RUs pueden ser asignados a diferentes usuarios, y dentro de un mismo RU, múltiples usuarios pueden transmitir usando MU-MIMO.

**Multiplexación espacial:** En un sistema MU-MIMO con $N_t$ antenas en el transmisor (AP) y $K$ usuarios con $N_{r,k}$ antenas cada uno, la capacidad suma se puede acotar por:

$$C_{\text{sum}} = \sum_{k=1}^{K} \log_2 \det\left(\mathbf{I} + \text{SNR}_k \cdot \mathbf{H}_k \mathbf{W}_k \mathbf{W}_k^H \mathbf{H}_k^H\right)$$

donde $\mathbf{H}_k$ es la matriz de canal del usuario $k$ y $\mathbf{W}_k$ es la matriz de precodificación asignada al usuario $k$. Para que MU-MIMO funcione eficientemente, los canales de los usuarios deben ser **suficientemente ortogonales** (decorrelados) en el dominio espacial.

**Beamforming mejorado:** WiFi 6 añade feedback comprimido más eficiente para el sondeo de canal MU-MIMO, reduciendo el overhead de sounding en escenarios con muchos usuarios.

### 7.5 BSS Coloring

#### Problema: Interferencia inter-BSS

En redes WiFi densas, múltiples APs (BSSs) operan frecuentemente en el mismo canal. En WiFi 5 y anteriores, el mecanismo de acceso al medio trata a **todas** las señales WiFi detectadas por encima del umbral de detección como una razón para diferir la transmisión, sin distinguir si la señal proviene de su propio BSS o de un BSS vecino. Esto se denomina **problema de OBSS** (Overlapping BSS) y resulta en:

- Diferimientos innecesarios cuando la señal interfiriente es de un BSS lejano que no causa interferencia real.
- Reducción significativa del throughput (hasta 40-50% en escenarios densos).
- Inequidad en el acceso al medio.

#### Solución: BSS Color de 6 bits

WiFi 6 asigna un **identificador de color de 6 bits** (0–63) a cada BSS. Este color se incluye en el campo **HE-SIG-A** del preámbulo de todas las tramas 802.11ax, lo que permite a cualquier dispositivo identificar a qué BSS pertenece una trama **antes de decodificar completamente el encabezado**.

Cuando una STA o AP detecta una trama con un color **diferente** al de su propio BSS (inter-BSS), puede aplicar un umbral de detección más alto (**OBSS/PD threshold**, ajustable hasta $-62$ dBm) en lugar del umbral estándar de $-82$ dBm. Esto significa que si la señal inter-BSS es débil (pero superior a $-82$ dBm), la STA puede **ignorarla y transmitir simultáneamente**, realizando reutilización espacial del canal.

El ajuste del umbral OBSS/PD está regulado por una relación con la potencia de transmisión:

$$\text{OBSS/PD}_{\text{máx}} = \max\left(-82 \, \text{dBm}, \min\left(-62 \, \text{dBm}, -82 + (P_{TX, \text{ref}} - P_{TX})\right)\right)$$

donde $P_{TX, \text{ref}} = 21$ dBm y $P_{TX}$ es la potencia de transmisión actual del dispositivo. Esto garantiza que un dispositivo que transmite con mayor potencia no use un umbral demasiado agresivo que pudiera causar interferencia excesiva.

#### Ejemplo de BSS Coloring

Considere 3 APs (AP₁, AP₂, AP₃) operando en el mismo canal de 80 MHz, con colores BSS = 1, 2, 3 respectivamente. La STA₁ está asociada a AP₁ (color 1).

**Sin BSS Coloring (WiFi 5):**
STA₁ detecta tramas de AP₂ a $-75$ dBm (superior al umbral de $-82$ dBm). STA₁ difiere su transmisión, aunque la señal de AP₂ no interfiere significativamente con la recepción de AP₁ (cuya señal es de $-50$ dBm, resultando en un SIR de $-50 - (-75) = 25$ dB, más que suficiente para decodificar).

**Con BSS Coloring (WiFi 6):**
STA₁ detecta el color 2 en la trama de AP₂ → identifica que es una trama inter-BSS. Aplica el umbral OBSS/PD de $-72$ dBm (valor ajustado). Como la señal de AP₂ es $-75$ dBm $<$ $-72$ dBm, STA₁ **ignora la trama y procede a transmitir**. Resultado: reutilización espacial exitosa, mejorando el throughput hasta un 20-30%.

**Descripción de Figura — BSS Coloring:**

> *La Figura 7.3 ilustra el mecanismo de BSS Coloring. Se muestran tres BSSs superpuestos: BSS₁ (AP₁ en el centro-izquierda, color rojo, etiqueta "Color=1"), BSS₂ (AP₂ en el centro, color azul, etiqueta "Color=2") y BSS₃ (AP₃ en la derecha, color verde, etiqueta "Color=3"). Los círculos de cobertura se superponen significativamente. En la zona de superposición entre BSS₁ y BSS₂, una STA₁ (asociada a AP₁) detecta tramas de ambos APs. En la parte superior, un diagrama temporal muestra el comportamiento sin BSS Coloring: STA₁ detecta la trama de AP₂, marca el canal como ocupado (barra gris "DEFER") y no puede transmitir. En la parte inferior, con BSS Coloring: STA₁ detecta el color 2 en la trama de AP₂, lo compara con su color (1), determina que es inter-BSS, verifica que la potencia ($-75$ dBm) está por debajo del umbral OBSS/PD ($-72$ dBm), e inmediatamente transmite su propia trama (barra verde "TX"). El resultado se etiqueta como "Reutilización Espacial Exitosa".*

### 7.6 Target Wake Time (TWT)

**Target Wake Time (TWT)** es un mecanismo de ahorro de energía introducido en WiFi 6, especialmente diseñado para dispositivos IoT (sensores, cámaras, dispositivos de domótica) que transmiten datos de forma infrecuente y necesitan maximizar la duración de la batería.

**Mecanismo de negociación:** Cada STA negocia con el AP un **programa de despertares** (wake schedule):

1. La STA envía una **TWT Request** indicando sus preferencias: intervalo entre despertares ($T_{\text{TWT}}$), duración del periodo activo ($T_{\text{wake}}$), y si el acuerdo es individual o de difusión.

2. El AP responde con una **TWT Response** confirmando o ajustando los parámetros.

3. A partir de ese momento, la STA puede entrar en modo **doze** (dormida) durante los intervalos entre sus TWT sessions, apagando completamente su radio WiFi. Solo despierta en los instantes programados.

**Cálculo del ciclo de trabajo y ahorro de energía:**

El ciclo de trabajo (duty cycle) de un dispositivo con TWT es:

$$D = \frac{T_{\text{wake}}}{T_{\text{TWT}}}$$

donde $T_{\text{wake}}$ es la duración del periodo activo y $T_{\text{TWT}}$ es el intervalo entre despertares.

El consumo promedio de potencia es:

$$P_{\text{avg}} = D \times P_{\text{active}} + (1 - D) \times P_{\text{sleep}}$$

donde $P_{\text{active}}$ es el consumo en modo activo (transmitiendo/recibiendo) y $P_{\text{sleep}}$ es el consumo en modo dormido.

**Ejemplo numérico — Sensor de temperatura IoT:**

Un sensor de temperatura envía una lectura de 50 bytes cada 10 minutos.

Parámetros TWT:
- $T_{\text{TWT}} = 600 \, \text{s}$ (10 minutos)
- $T_{\text{wake}} = 0.05 \, \text{s}$ (50 ms: tiempo para despertar, transmitir 50 bytes, recibir ACK)
- $P_{\text{active}} = 300 \, \text{mW}$ (consumo típico del radio WiFi activo)
- $P_{\text{sleep}} = 0.01 \, \text{mW}$ (consumo del microcontrolador en modo deep sleep)

Ciclo de trabajo:

$$D = \frac{0.05}{600} = 8.33 \times 10^{-5} = 0.00833\%$$

Consumo promedio:

$$P_{\text{avg}} = 8.33 \times 10^{-5} \times 300 + (1 - 8.33 \times 10^{-5}) \times 0.01$$

$$= 0.025 + 0.01 = 0.035 \, \text{mW}$$

**Sin TWT** (modo legacy PSM, despertando cada beacon a 100 ms):

$$D_{\text{legacy}} = \frac{T_{\text{wake, listen}}}{T_{\text{beacon}}} = \frac{0.005}{0.1} = 5\%$$

$$P_{\text{avg, legacy}} = 0.05 \times 100 + 0.95 \times 0.01 = 5.01 \, \text{mW}$$

Nota: en modo legacy PSM, el dispositivo despierta brevemente para escuchar cada beacon (5 ms cada 100 ms), con consumo de ~100 mW en modo de escucha (menor que transmisión).

**Mejora en duración de batería:**

Suponga una batería de 1000 mAh a 3.3 V (energía = 3.3 Wh = 3300 mWh):

- Con TWT: $\text{Duración} = \frac{3300}{0.035} = 94{,}286 \, \text{h} \approx 10.8 \, \text{años}$
- Sin TWT (PSM): $\text{Duración} = \frac{3300}{5.01} = 659 \, \text{h} \approx 27 \, \text{días}$

$$\boxed{\text{Mejora: } \frac{10.8 \, \text{años}}{27 \, \text{días}} \approx 146\times}$$

### 7.7 Cálculo de Velocidad PHY WiFi 6

WiFi 6 modifica los parámetros del símbolo OFDM para mejorar la eficiencia en entornos multipath densos:

**Cambios en el símbolo OFDM:**

| Parámetro | WiFi 5 (802.11ac) | WiFi 6 (802.11ax) |
|:---|:---:|:---:|
| Duración útil del símbolo ($T_{\text{FFT}}$) | 3.2 μs | **12.8 μs** (4× mayor) |
| Espaciado entre subportadoras ($\Delta f$) | 312.5 kHz | **78.125 kHz** (4× menor) |
| Opciones de GI | 0.4 μs, 0.8 μs | **0.8 μs, 1.6 μs, 3.2 μs** |
| Duración total del símbolo | 3.6 – 4.0 μs | **13.6 – 16.0 μs** |
| Subportadoras de datos (80 MHz) | 234 | **980** |

El espaciado entre subportadoras se calcula como:

$$\Delta f = \frac{1}{T_{\text{FFT}}} = \frac{1}{12.8 \times 10^{-6}} = 78{,}125 \, \text{Hz} = 78.125 \, \text{kHz}$$

¿Por qué un símbolo más largo? Un símbolo 4× más largo con subportadoras 4× más estrechas tiene ventajas en entornos densos:

1. **Mayor robustez al multipath:** El prefijo cíclico (GI) es proporcionalmente más corto respecto al símbolo útil, lo que mejora la eficiencia. En WiFi 5, el GI de 0.8 μs representa el 20% del símbolo (0.8/4.0). En WiFi 6, el GI de 0.8 μs representa solo el 5.9% (0.8/13.6).

2. **Mayor número de subportadoras por Hz:** Al estrechar las subportadoras, caben más en el mismo ancho de canal. Un canal de 80 MHz tiene $80{,}000/78.125 = 1024$ subportadoras en WiFi 6, frente a $80{,}000/312.5 = 256$ en WiFi 5. Descontando pilotos, DC y bandas de guarda, WiFi 6 tiene 980 subportadoras de datos vs 234 en WiFi 5 para 80 MHz. Sin embargo, la tasa por subportadora es 4× menor (porque el símbolo es 4× más largo), por lo que la velocidad neta por flujo es comparable (ligeramente mayor gracias al mayor número relativo de subportadoras de datos).

**Fórmula de velocidad PHY WiFi 6:**

$$R_{\text{PHY}} = N_{SS} \times N_{SD} \times b \times R_c \times \frac{1}{T_{\text{SYM}}}$$

La fórmula es la misma que WiFi 5, pero con valores actualizados.

**Ejemplo — Velocidad máxima WiFi 6 (configuración extrema):**

- $N_{SS} = 8$ (8 flujos espaciales)
- $N_{SD} = 1960$ (160 MHz: $2 \times 980$)
- $b = 10$ (1024-QAM, MCS 11)
- $R_c = 5/6$
- $T_{\text{SYM}} = 12.8 + 0.8 = 13.6 \, \mu\text{s}$ (GI de 0.8 μs)

$$R_{\text{PHY}} = 8 \times 1960 \times 10 \times \frac{5}{6} \times \frac{1}{13.6 \times 10^{-6}}$$

Paso a paso:

$$8 \times 1960 = 15{,}680$$

$$15{,}680 \times 10 = 156{,}800 \, \text{bits por símbolo}$$

$$156{,}800 \times \frac{5}{6} = 130{,}667 \, \text{bits de información por símbolo}$$

$$\frac{130{,}667}{13.6 \times 10^{-6}} = 9{,}607{,}843{,}137 \, \text{bps}$$

$$\boxed{R_{\text{PHY, máx WiFi 6}} = 9.6 \, \text{Gbps}}$$

**Tabla comparativa — Velocidad máxima WiFi 5 vs WiFi 6 (8×8, 160 MHz, GI mínimo):**

| Parámetro | WiFi 5 | WiFi 6 | Cambio |
|:---|:---:|:---:|:---:|
| Modulación máx. | 256-QAM (8 bits) | 1024-QAM (10 bits) | +25% |
| $N_{SD}$ (160 MHz) | 468 | 1960 | +4.19× |
| $T_{\text{SYM}}$ (GI mín.) | 3.6 μs | 13.6 μs | +3.78× |
| $N_{SD} / T_{\text{SYM}}$ | 130.0 kHz | 144.1 kHz | +10.8% |
| $R_c$ máx. | 5/6 | 5/6 | = |
| $R_{\text{PHY}}$ (1 SS) | 866.7 Mbps | 1201 Mbps | +38.6% |
| $R_{\text{PHY}}$ (8 SS) | 6.93 Gbps | 9.6 Gbps | +38.5% |

La mejora del 38.5% en velocidad PHY máxima proviene de dos factores: 25% por la mejora en modulación (1024-QAM vs 256-QAM) y ~10.8% por la mayor eficiencia espectral del nuevo diseño OFDM (más subportadoras de datos por Hz de ancho de banda).

---

## 8. WiFi 6E (IEEE 802.11ax en 6 GHz)

### 8.1 Espectro de 6 GHz

WiFi 6E no es un nuevo estándar PHY: utiliza exactamente la misma tecnología 802.11ax de WiFi 6. La "E" significa **Extended**, refiriéndose a la extensión del espectro operativo a la banda de **6 GHz** (5.925–7.125 GHz), que proporciona **1200 MHz** de espectro adicional para WiFi.

Para poner en perspectiva la magnitud de esta adición:
- La banda de 2.4 GHz ofrece ~83.5 MHz de espectro utilizable.
- La banda de 5 GHz ofrece ~500 MHz (varía por región, incluyendo canales DFS).
- La banda de 6 GHz añade **1200 MHz**, más que duplicando el espectro WiFi total disponible.

$$\text{Espectro total WiFi 6E} = 83.5 + 500 + 1200 = 1783.5 \, \text{MHz}$$

$$\text{Incremento} = \frac{1200}{83.5 + 500} \times 100\% = 205.6\%$$

**Panorama regulatorio:**

La disponibilidad de la banda de 6 GHz varía significativamente por región:

- **Estados Unidos (FCC):** Aprobó todo el rango de 5.925–7.125 GHz (1200 MHz) en abril de 2020 para uso sin licencia. Permite tanto uso interior (LPI — Low Power Indoor) como exterior (SP — Standard Power, con AFC).

- **Europa (CEPT/ETSI):** Inicialmente aprobó solo la parte baja, 5.925–6.425 GHz (500 MHz), exclusivamente para uso interior (LPI). La parte alta (6.425–7.125 GHz) está en proceso de evaluación regulatoria y hay presión de operadores móviles para asignarla a 5G/IMT.

- **Latinoamérica:** Brasil y México han adoptado regulaciones similares a la FCC (1200 MHz). Chile y Colombia han seguido parcialmente. Otros países siguen en proceso regulatorio.

- **Asia:** Corea del Sur aprobó los 1200 MHz. Japón autorizó la parte baja. China e India aún no han asignado espectro en 6 GHz para WiFi.

**AFC (Automated Frequency Coordination):**

Para operaciones de potencia estándar (SP) en exteriores, la FCC exige el uso de un sistema **AFC** (Coordinación Automática de Frecuencias). El AFC funciona como una base de datos central que:

1. El AP reporta su ubicación geográfica al servidor AFC.
2. El servidor AFC consulta una base de datos de sistemas incumbentes (enlaces fijos punto a punto, estaciones de TV por cable, satélites) que operan en la banda de 6 GHz.
3. El servidor responde al AP con una lista de canales y niveles de potencia permitidos en esa ubicación.
4. El AP solo puede operar en los canales y potencias autorizados por el AFC.

Este mecanismo permite proteger a los usuarios incumbentes del espectro de 6 GHz mientras maximiza el acceso para WiFi.

### 8.2 Canales Disponibles en 6 GHz

La banda de 6 GHz ofrece un número significativamente mayor de canales no solapados comparada con 5 GHz:

| Ancho de Canal | Canales en 5 GHz | Canales en 6 GHz | Incremento |
|:---:|:---:|:---:|:---:|
| 20 MHz | ~25 | **59** | +136% |
| 40 MHz | ~12 | **29** | +142% |
| 80 MHz | ~6 | **14** | +133% |
| 160 MHz | ~2 | **7** | +250% |

Estos números son particularmente impactantes para canales anchos:

- **7 canales de 160 MHz** sin solapamiento en 6 GHz, comparados con apenas 2 en 5 GHz. Esto significa que en un despliegue empresarial, se pueden tener 7 APs con 160 MHz cada uno sin interferencia mutua, lo cual era prácticamente imposible en 5 GHz.

- **14 canales de 80 MHz** permiten despliegues densos de alta capacidad donde cada AP opera en un canal limpio.

**Numeración de canales en 6 GHz:**

Los canales en 6 GHz comienzan en el canal **1** (frecuencia central 5.955 GHz para 20 MHz) y se incrementan en pasos de 4 para canales de 20 MHz:

$$f_c = 5950 + 5 \times n \quad \text{[MHz]}$$

donde $n$ es el número de canal. El primer canal de 20 MHz es $n = 1$ ($f_c = 5955$ MHz) y el último es $n = 233$ ($f_c = 7115$ MHz).

Para canales de 160 MHz, los canales centrales son: 15, 47, 79, 111, 143, 175, 207.

**Descriptive figure paragraph — Comparativa de espectro disponible:**

> *La Figura 8.1 presenta una comparación visual del espectro disponible en las tres bandas WiFi. En la parte superior, la banda de 2.4 GHz se muestra como una barra estrecha (83.5 MHz) con solo 3 canales no solapados de 20 MHz (1, 6, 11), coloreados en rojo, verde y azul. En el medio, la banda de 5 GHz se muestra como una barra más ancha (~500 MHz) con sus canales de 20 MHz agrupados por sub-bandas UNII, algunos marcados como "DFS". Se indican 6 canales de 80 MHz y 2 de 160 MHz no solapados. En la parte inferior, la banda de 6 GHz se muestra como una barra muy ancha (1200 MHz) que es visualmente mayor que las otras dos combinadas. Los 14 canales de 80 MHz se muestran como rectángulos verdes no solapados, y los 7 canales de 160 MHz como rectángulos azules. Debajo, un gráfico de barras resume: 2.4 GHz = 83.5 MHz (3 canales 20 MHz), 5 GHz ≈ 500 MHz (6 canales 80 MHz), 6 GHz = 1200 MHz (14 canales 80 MHz). Un diagrama circular muestra que 6 GHz representa el 67% del espectro WiFi total.*

### 8.3 Beneficios de WiFi 6E

#### Despliegue Greenfield (Sin dispositivos legacy)

Uno de los beneficios más significativos de WiFi 6E no es tecnológico sino operativo: la banda de 6 GHz es un **espacio limpio** donde solo dispositivos WiFi 6E (o posteriores) pueden operar. No existen dispositivos legacy (WiFi 4, WiFi 5, etc.) en 6 GHz.

¿Por qué es esto tan importante? En las bandas de 2.4 y 5 GHz, los APs WiFi 6 deben mantener compatibilidad hacia atrás con dispositivos antiguos. Esto implica:

- **Transmisión de tramas de protección** (CTS-to-Self, RTS/CTS) para que dispositivos legacy entiendan las duraciones de transmisión.
- **Reducción del ancho de canal** cuando dispositivos legacy se conectan a canales anchos.
- **Uso de modulaciones inferiores** para los tramas de management y control.
- **Imposibilidad de usar OFDMA** o BSS Coloring con dispositivos que no soportan 802.11ax.

En 6 GHz, al ser 100% WiFi 6E/7, el AP puede:
- Usar OFDMA en todas las transmisiones.
- Utilizar el ancho de canal completo sin restricciones.
- Eliminar tramas de protección legacy.
- Operar con la máxima eficiencia MAC posible.

Mediciones de campo han mostrado que un AP WiFi 6 en 5 GHz con una mezcla de clientes legacy puede perder 20-30% de eficiencia comparado con el mismo AP en 6 GHz donde todos los clientes son WiFi 6E.

#### Reducción de Interferencia

La amplia disponibilidad de canales en 6 GHz reduce drásticamente la probabilidad de co-canal interference (CCI). En un despliegue empresarial típico con 20 APs:

- En 5 GHz (6 canales de 80 MHz): Factor de reuso = $\lceil 20/6 \rceil = 4$, es decir, al menos 4 APs comparten cada canal.
- En 6 GHz (14 canales de 80 MHz): Factor de reuso = $\lceil 20/14 \rceil = 2$, o incluso 1 si se usan los 14 canales.

La reducción de co-channel APs por canal mejora directamente la capacidad de la red, ya que el throughput en un canal compartido se degrada aproximadamente como:

$$R_{\text{efectivo}} \approx \frac{R_{\text{máx}}}{N_{\text{APs/canal}}}$$

#### Más Canales No Solapados para Canales Anchos

WiFi 5 y 6 soportan canales de 160 MHz, pero en 5 GHz solo hay 2 canales contiguos de 160 MHz, y uno de ellos cruza bandas DFS. En 6 GHz, los **7 canales de 160 MHz** sin solapamiento hacen que el uso de 160 MHz sea práctico para despliegues reales, multiplicando el throughput por AP.

#### Misma PHY que WiFi 6 pero en espectro más limpio

Las velocidades PHY de WiFi 6E son idénticas a WiFi 6 (mismo 802.11ax), por lo que la velocidad máxima sigue siendo 9.6 Gbps con la configuración más agresiva. La ventaja está en que estas velocidades son más **alcanzables en la práctica** gracias al espectro más limpio y la ausencia de dispositivos legacy.

### 8.4 Consideraciones de Propagación en 6 GHz

#### Mayor pérdida de trayecto a 6 GHz vs 5 GHz

La pérdida de propagación en espacio libre es proporcional al cuadrado de la frecuencia. Comparando 6 GHz con 5 GHz:

$$\Delta L = 20\log_{10}\left(\frac{f_{6\text{GHz}}}{f_{5\text{GHz}}}\right) = 20\log_{10}\left(\frac{6500}{5500}\right) = 20\log_{10}(1.182) = 1.45 \, \text{dB}$$

Tomando frecuencias centrales de cada banda (5.5 GHz vs 6.5 GHz), la pérdida adicional es de aproximadamente **1.45 dB** en espacio libre. Este valor es relativamente modesto, pero la situación empeora significativamente en entornos interiores.

#### Pérdidas de penetración en paredes

Las pérdidas de penetración a través de materiales de construcción aumentan con la frecuencia. Valores típicos comparativos:

| Material | 5 GHz | 6 GHz | Diferencia |
|:---|:---:|:---:|:---:|
| Pared de yeso (drywall) | 3–4 dB | 4–5 dB | +1 dB |
| Pared de ladrillo | 8–10 dB | 10–13 dB | +2–3 dB |
| Concreto (15 cm) | 15–20 dB | 18–25 dB | +3–5 dB |
| Vidrio estándar | 4–6 dB | 5–8 dB | +1–2 dB |
| Vidrio Low-E | 25–30 dB | 28–35 dB | +3–5 dB |
| Piso/techo (concreto) | 18–22 dB | 22–28 dB | +4–6 dB |

Estos incrementos acumulativos pueden ser significativos en edificios con múltiples paredes entre el AP y la STA.

#### Implicaciones de cobertura

La combinación de mayor FSPL y mayores pérdidas por materiales resulta en un **área de cobertura menor** para WiFi 6E comparado con WiFi 6 en 5 GHz, para la misma potencia de transmisión y sensibilidad del receptor.

#### Ejemplo numérico — Comparación de cobertura 5 GHz vs 6 GHz

Comparemos el radio de cobertura de un AP en 5 GHz vs 6 GHz, para una configuración MCS 7 (64-QAM, 2/3) en 80 MHz con 2 flujos espaciales.

**Parámetros comunes:**
- $P_{TX} = 20$ dBm
- $G_{TX} = 5$ dBi
- $G_{RX} = 2$ dBi
- $L_{TX} + L_{RX} = 1$ dB
- $G_{\text{BF}} = 3$ dB
- $M_{\text{fade}} = 8$ dB
- Sensibilidad MCS 7: $S_{\min} = -66$ dBm (asumida igual en ambas bandas)
- Exponente de propagación: $n = 3.0$ (interior típico)
- Sin paredes adicionales (línea de vista interior)

**EIRP efectiva:** $P_{TX} + G_{TX} - L_{TX} + G_{\text{BF}} + G_{RX} = 20 + 5 - 1 + 3 + 2 = 29$ dBm

**Potencia mínima requerida:** $P_{RX, \min} = S_{\min} + M_{\text{fade}} = -66 + 8 = -58$ dBm

**Pérdida máxima:** $L_{\text{máx}} = 29 - (-58) = 87$ dB

**A 5.5 GHz:**

$$L_0 = 20\log_{10}(0.01) + 20\log_{10}(5500) + 32.44 = -40 + 74.81 + 32.44 = 67.25 \, \text{dB}$$

$$87 = 67.25 + 10 \times 3.0 \times \log_{10}\left(\frac{d}{10}\right)$$

$$\log_{10}\left(\frac{d}{10}\right) = \frac{19.75}{30} = 0.658$$

$$d_{5\text{GHz}} = 10 \times 10^{0.658} = 10 \times 4.55 = 45.5 \, \text{m}$$

**A 6.5 GHz:**

$$L_0 = 20\log_{10}(0.01) + 20\log_{10}(6500) + 32.44 = -40 + 76.26 + 32.44 = 68.70 \, \text{dB}$$

$$87 = 68.70 + 30 \times \log_{10}\left(\frac{d}{10}\right)$$

$$\log_{10}\left(\frac{d}{10}\right) = \frac{18.30}{30} = 0.610$$

$$d_{6\text{GHz}} = 10 \times 10^{0.610} = 10 \times 4.07 = 40.7 \, \text{m}$$

**Comparación:**

$$\frac{d_{6\text{GHz}}}{d_{5\text{GHz}}} = \frac{40.7}{45.5} = 0.895$$

$$\boxed{\text{El radio de cobertura a 6 GHz es aproximadamente 10.5\% menor que a 5 GHz}}$$

En términos de **área** de cobertura (proporcional a $d^2$):

$$\frac{A_{6\text{GHz}}}{A_{5\text{GHz}}} = \left(\frac{40.7}{45.5}\right)^2 = 0.80$$

$$\boxed{\text{El área de cobertura a 6 GHz es aproximadamente 20\% menor que a 5 GHz}}$$

Esta reducción del 20% en área significa que un despliegue WiFi 6E requerirá **más APs** para cubrir la misma superficie que un despliegue WiFi 6 en 5 GHz. Sin embargo, dado que 6 GHz ofrece muchos más canales, el costo adicional de más APs se compensa con la mayor capacidad y menor interferencia.

Si añadimos paredes (por ejemplo, 2 paredes de ladrillo con pérdida de 10 dB a 5 GHz y 13 dB a 6 GHz), la diferencia se amplifica:

- $d_{5\text{GHz}}$ (con 2 paredes a 10 dB): $L_{\text{máx}} = 87 - 20 = 67$ dB → $d = 10^{(67 - 67.25)/30 + 1} \times 10 = 9.94$ m
- $d_{6\text{GHz}}$ (con 2 paredes a 13 dB): $L_{\text{máx}} = 87 - 26 = 61$ dB → $d = 10^{(61 - 68.70)/30 + 1} \times 10 = 5.57$ m

$$\frac{d_{6\text{GHz}}}{d_{5\text{GHz}}} = \frac{5.57}{9.94} = 0.56$$

Con paredes gruesas, el alcance a 6 GHz puede reducirse al **56%** del alcance a 5 GHz, lo que implica la necesidad de aproximadamente **3.2× más APs** para cubrir la misma área. Esto resalta la importancia de una planificación cuidadosa del despliegue WiFi 6E, especialmente en edificios con materiales de construcción densos.

## 9. WiFi 7: IEEE 802.11be — Extremely High Throughput (EHT)

WiFi 7, formalmente **IEEE 802.11be**, es la evolución natural de WiFi 6/6E y fue diseñado con una idea central: no basta con aumentar la velocidad pico; también hay que reducir la latencia, mejorar la predictibilidad del retardo y aprovechar el espectro de manera más flexible [22]–[23], [18], [24]–[26]. Por eso, el nombre técnico de la enmienda es **Extremely High Throughput (EHT)**: la ambición ya no es solo “alta eficiencia” como en 802.11ax, sino **caudal extremadamente alto**.

Desde un punto de vista práctico, WiFi 7 busca servir aplicaciones que combinan tres exigencias simultáneas:

1. **Mucho caudal** (por ejemplo, video 8K, transferencia masiva de datos, renderizado remoto).
2. **Poca latencia** (realidad aumentada/virtual, juegos en la nube, control industrial).
3. **Gran fiabilidad bajo carga** (oficinas densas, campus, fábricas, hogares con muchos dispositivos).

A lo largo de esta sección estudiaremos sus mecanismos principales con una perspectiva pedagógica, pero sin perder rigor matemático.

### 9.1 Motivación y Contexto de WiFi 7

#### 9.1.1 ¿Por qué hizo falta WiFi 7?

WiFi 6 y WiFi 6E resolvieron muchos problemas de eficiencia en entornos densos mediante **OFDMA**, **MU-MIMO uplink/downlink**, **1024-QAM** y el uso de la banda de **6 GHz**. Sin embargo, seguían existiendo cuatro limitaciones importantes:

- **Ancho de canal máximo limitado a 160 MHz.** Para aplicaciones multi-gigabit, 160 MHz puede resultar insuficiente.
- **Un solo enlace lógico principal por asociación.** Aunque un dispositivo sea tribanda, tradicionalmente una sesión de datos se apoya sobre un enlace principal, con cambios de banda relativamente rígidos.
- **Latencia variable.** En un medio compartido, las colas MAC, la contención y la interferencia generan jitter.
- **Capacidad limitada para flujos inmersivos y sincronizados.** Aplicaciones como AR/VR no solo requieren muchos Mbps, sino que además exigen retardos pequeños y estables.

Un modo simple de ver la presión de tráfico moderna es sumar demandas concurrentes. Si en un hogar u oficina pequeña hay varias aplicaciones activas, el caudal agregado puede estimarse como

$$
R_{\text{agregado}} = \sum_{i=1}^{K} R_i
$$

donde $R_i$ es la tasa requerida por la aplicación $i$ y $K$ es el número de aplicaciones activas al mismo tiempo.

Esta ecuación parece trivial, pero es importante pedagógicamente: en redes reales, el cuello de botella aparece cuando muchas aplicaciones coinciden. Por ejemplo, si una vivienda tiene simultáneamente:

- dos flujos de video 4K/8K comprimidos de $80\ \text{Mbps}$ cada uno,
- una sesión de VR de $400\ \text{Mbps}$,
- un juego en la nube de $35\ \text{Mbps}$,
- y tráfico IoT, copias en la nube y señalización por $25\ \text{Mbps}$,

entonces

$$
R_{\text{agregado}} = 80 + 80 + 400 + 35 + 25 = 620\ \text{Mbps}
$$

El resultado, $620\ \text{Mbps}$, no parece extremo para WiFi 6. El problema es que ese valor representa solo el **caudal medio agregado**. Si además se exige latencia sub-5 ms y estabilidad temporal, la red necesita margen adicional para retransmisiones, overhead MAC, contención y variaciones instantáneas del canal. WiFi 7 nace precisamente para ofrecer ese margen.

#### 9.1.2 Aplicaciones impulsoras

Las aplicaciones que más han empujado el desarrollo de WiFi 7 son:

- **AR/VR/XR:** muy sensibles a latencia y jitter. Una imagen que llega tarde no solo degrada calidad: puede generar mareo o mala experiencia de usuario.
- **Streaming 8K y video volumétrico:** demandan caudales sostenidos altos.
- **Cloud gaming:** combina tráfico constante con exigencia fuerte de retardo extremo a extremo.
- **Industrial IoT y automatización:** requieren comunicaciones predecibles y robustas, no solo “rápidas” en promedio.
- **Transporte inalámbrico local (backhaul/fronthaul):** en oficinas y hogares avanzados se usan enlaces WiFi para distribuir tráfico multi-gigabit dentro del edificio.

#### 9.1.3 Línea temporal y proceso de normalización

El proceso de estandarización de 802.11be puede resumirse así [22]–[23], [18], [24]:

- **2018–2019:** se consolida la idea de una nueva evolución más allá de 802.11ax; se forma el grupo de trabajo **TGbe**.
- **2021:** aparecen borradores tempranos que ya incluyen MLO, 320 MHz y 4096-QAM.
- **2022:** el borrador **IEEE P802.11be/D3.0** refleja una versión bastante madura de la especificación [23].
- **2024:** se publica la enmienda final **IEEE Std 802.11be-2024** [22].

Desde el punto de vista académico, es útil recordar una regla: **la industria comercializa chipsets y APs antes de la publicación final del estándar**, apoyándose en borradores avanzados. Por eso existen productos “WiFi 7” previos a la edición definitiva del estándar.

#### 9.1.4 Objetivos de desempeño

Aunque el rendimiento real siempre depende del número de usuarios, del canal y del dispositivo, los objetivos de diseño asociados a WiFi 7 suelen resumirse así [18], [24]–[26]:

- **Caudal pico PHY superior a 40 Gbps** en configuraciones extremas.
- **Latencia de acceso muy baja**, con objetivos prácticos del orden de **menos de 5 ms** para ciertas aplicaciones y arquitecturas locales.
- **Mayor fiabilidad** mediante agregación/selección entre múltiples enlaces.

---

### 9.2 Arquitectura y Características Fundamentales de WiFi 7

Las cuatro novedades más emblemáticas de WiFi 7 son:

1. **Multi-Link Operation (MLO)**
2. **Canales de 320 MHz**
3. **4096-QAM (4K-QAM)**
4. **Hasta 16 flujos espaciales**

A continuación se estudia cada una.

#### 9.2.1 Multi-Link Operation (MLO)

La idea de MLO es conceptualmente muy poderosa: un dispositivo ya no se ve como un único enlace WiFi, sino como un **conjunto coordinado de enlaces** que pueden operar en **2.4 GHz, 5 GHz y 6 GHz** [22], [18], [24].

Si un dispositivo dispone de $L$ enlaces simultáneos, el caudal agregado ideal puede modelarse como

$$
R_{\text{MLO}} = \sum_{\ell=1}^{L} R_{\ell}
$$

donde $R_{\ell}$ es la tasa de transmisión del enlace $\ell$.

**Explicación detallada de la ecuación:**

- El símbolo $L$ representa cuántos enlaces físicos están activos y coordinados.
- Cada término $R_{\ell}$ representa la tasa de un enlace individual; por ejemplo, uno en 5 GHz y otro en 6 GHz.
- La suma expresa que, en el caso ideal, la capacidad total es la adición de todas las capacidades individuales.
- El calificativo “ideal” es importante: en la práctica hay overhead de coordinación, colas, contención y límites del hardware.

Para modelar ese overhead de manera sencilla, se introduce una eficiencia por enlace $\alpha_{\ell}$ con $0 < \alpha_{\ell} \leq 1$:

$$
R_{\text{MLO,ef}} = \sum_{\ell=1}^{L} \alpha_{\ell} R_{\ell}
$$

Aquí, $\alpha_{\ell}$ recoge pérdidas por cabeceras MAC, tiempos muertos, coordinación entre radios y retransmisiones. Si $\alpha_{\ell}=0.9$, significa que solo el 90% de la tasa PHY de ese enlace se convierte en rendimiento útil.

**Ejemplo numérico sencillo:**

Supongamos un equipo con tres enlaces:

- enlace 1 en 2.4 GHz con $R_1 = 0.6\ \text{Gbps}$,
- enlace 2 en 5 GHz con $R_2 = 2.4\ \text{Gbps}$,
- enlace 3 en 6 GHz con $R_3 = 5.8\ \text{Gbps}$.

En el caso ideal:

$$
R_{\text{MLO}} = 0.6 + 2.4 + 5.8 = 8.8\ \text{Gbps}
$$

Si tomamos eficiencias $\alpha_1 = 0.80$, $\alpha_2 = 0.88$ y $\alpha_3 = 0.90$,

$$
R_{\text{MLO,ef}} = 0.80\cdot0.6 + 0.88\cdot2.4 + 0.90\cdot5.8
$$

$$
R_{\text{MLO,ef}} = 0.48 + 2.112 + 5.22 = 7.812\ \text{Gbps}
$$

Es decir, el agregado realista sería aproximadamente **$7.81\ \text{Gbps}$**.

##### Modelo simple de reducción de latencia

MLO no solo sirve para sumar caudal; también puede **reducir la latencia** si un paquete se envía por el enlace más rápido disponible o incluso se duplica para que “gane” el primero que llegue.

Si el tiempo de servicio de cada enlace es una variable aleatoria $T_{\ell}$, y se usa el primer enlace que complete la transmisión, entonces el retardo efectivo es

$$
T_{\text{MLO}} = \min(T_1,T_2,\dots,T_L)
$$

Esta ecuación significa que el paquete “termina” cuando termina el enlace más rápido entre todos los enlaces candidatos. Matemáticamente, el mínimo de varias variables aleatorias suele ser menor que cada una por separado.

Si aproximamos cada tiempo de servicio como exponencial con tasa $\mu_{\ell} = 1/\bar T_{\ell}$, entonces

$$
\mathbb{E}[T_{\text{MLO}}] = \frac{1}{\sum_{\ell=1}^{L} \mu_{\ell}}
$$

donde $\bar T_{\ell}$ es el retardo medio del enlace $\ell$ y $\mathbb{E}[\cdot]$ representa el valor esperado.

**Ejemplo:** si dos enlaces tienen retardos medios de $\bar T_1 = 4\ \text{ms}$ y $\bar T_2 = 2.5\ \text{ms}$, entonces

$$
\mu_1 = \frac{1}{4} = 0.25\ \text{ms}^{-1}, \qquad \mu_2 = \frac{1}{2.5} = 0.4\ \text{ms}^{-1}
$$

por tanto,

$$
\mathbb{E}[T_{\text{MLO}}] = \frac{1}{0.25+0.4} = \frac{1}{0.65} \approx 1.54\ \text{ms}
$$

El resultado es muy instructivo: aunque ninguno de los enlaces por sí solo tenga $1.54\ \text{ms}$ de media, el uso coordinado de ambos sí puede aproximarse a ese valor en el modelo idealizado.

**Descripción de Figura — Arquitectura MLO y MLD:**

> *La Figura 9.1 debe mostrar, en el centro, un dispositivo cliente representado como un bloque grande etiquetado “MLD cliente”. Dentro del bloque aparecen tres radios o interfaces separadas: “Link 1: 2.4 GHz”, “Link 2: 5 GHz” y “Link 3: 6 GHz”. A la derecha se muestra un AP tribanda representado como “AP-MLD”, también con tres enlaces. En la parte superior del dibujo, una cola de paquetes de aplicación se divide mediante un planificador hacia los tres enlaces; algunas flechas sólidas representan reparto de carga y una flecha duplicada representa envío redundante de un paquete de baja latencia por dos enlaces a la vez. Debajo del esquema aparece una línea temporal con tres barras horizontales, una por enlace, donde se ve que el paquete entregado por el enlace más rápido determina el retardo final. La figura debe enfatizar visualmente que MLO no es simple itinerancia entre bandas, sino coordinación simultánea y consciente entre múltiples enlaces.*

#### 9.2.2 Canales de 320 MHz

La evolución de anchos de canal en WiFi puede resumirse así:

- WiFi 4: hasta 40 MHz
- WiFi 5: hasta 160 MHz
- WiFi 6/6E: hasta 160 MHz
- WiFi 7: hasta **320 MHz**

La relación básica entre capacidad y ancho de banda está dada por Shannon:

$$
C = B\log_2(1+\text{SNR})
$$

donde:

- $C$ es la capacidad teórica del canal en bits/s,
- $B$ es el ancho de banda en Hz,
- $\text{SNR}$ es la relación señal/ruido en forma lineal.

**Explicación detallada:**

- La fórmula indica que la capacidad crece linealmente con el ancho de banda $B$.
- También crece con la SNR, pero no linealmente, sino con un logaritmo base 2.
- Por eso, si la SNR se mantiene, **duplicar el ancho de banda** aproximadamente **duplica la capacidad**.

**Ejemplo numérico:** con $\text{SNR}=20\ \text{dB}$, primero se convierte a escala lineal:

$$
\text{SNR}_{\text{lin}} = 10^{20/10} = 100
$$

Entonces, para $B = 160\ \text{MHz}$,

$$
C_{160} = 160\times10^6\log_2(1+100)
$$

$$
C_{160} \approx 160\times10^6\times 6.658 = 1.065\times10^9\ \text{bps}
$$

Para $B = 320\ \text{MHz}$,

$$
C_{320} = 320\times10^6\log_2(101) \approx 2.130\times10^9\ \text{bps}
$$

Se observa que $C_{320} \approx 2C_{160}$. Esta es la razón fundamental por la que 320 MHz es tan relevante: incluso antes de hablar de MIMO o de 4096-QAM, el ancho de banda ya se ha duplicado.

##### Espaciado entre subportadoras y tamaño FFT

WiFi 6 y WiFi 7 usan un espaciado entre subportadoras de aproximadamente

$$
\Delta f = 78.125\ \text{kHz}
$$

Como en OFDM se cumple aproximadamente

$$
N_{\text{FFT}} \approx \frac{B}{\Delta f}
$$

para $B = 320\ \text{MHz}$ se obtiene

$$
N_{\text{FFT}} = \frac{320\times10^6}{78.125\times10^3} = 4096
$$

Esto justifica el uso de una **FFT de 4096 puntos**.

**Interpretación pedagógica:** una FFT mayor permite representar más subportadoras ortogonales dentro del mismo canal ancho. Eso aumenta el paralelismo en frecuencia y, por tanto, la cantidad de símbolos transmitidos en cada intervalo OFDM.

#### 9.2.3 4096-QAM (4K-QAM)

La modulación 4096-QAM usa una constelación de $4096$ símbolos. El número de bits por símbolo es

$$
\log_2(4096) = 12\ \text{bits/símbolo}
$$

Esta ecuación se explica así: si existen $M$ símbolos posibles, hacen falta $\log_2(M)$ bits para identificar uno de ellos. Como $4096 = 2^{12}$, cada símbolo transporta exactamente **12 bits**.

Para comparar con WiFi 6, que llega hasta 1024-QAM:

$$
\log_2(1024) = 10\ \text{bits/símbolo}
$$

La mejora relativa en bits por símbolo es

$$
\text{Ganancia} = \frac{12-10}{10}\times 100\% = 20\%
$$

Es decir, **4096-QAM ofrece un 20% más de bits por símbolo que 1024-QAM**, manteniendo todo lo demás constante.

##### Requisito de SNR

Un límite inferior teórico para la SNR puede estimarse a partir de Shannon. Si la eficiencia espectral objetivo es $\eta$ bits/s/Hz, entonces

$$
\eta = \log_2(1+\text{SNR}) \quad \Rightarrow \quad \text{SNR}_{\min} = 2^{\eta}-1
$$

Para 4096-QAM con tasa de codificación $R_c=5/6$, la eficiencia espectral bruta por subportadora puede aproximarse como

$$
\eta_{4096} = 12\cdot\frac{5}{6} = 10\ \text{bits/s/Hz}
$$

Por tanto, el límite ideal sería

$$
\text{SNR}_{\min,ideal} = 2^{10}-1 = 1023
$$

En decibelios,

$$
\text{SNR}_{\min,ideal,dB} = 10\log_{10}(1023) \approx 30.1\ \text{dB}
$$

Este valor **no** es la SNR práctica final, sino un límite teórico optimista. En sistemas reales hacen falta márgenes adicionales por imperfecciones de RF, sincronización, estimación de canal, EVM y no idealidad del decodificador. Por eso, en la práctica, 4096-QAM solo es viable en condiciones excelentes, típicamente muy cerca del AP.

**Ejemplo comparativo:** para 1024-QAM con $R_c=5/6$,

$$
\eta_{1024} = 10\cdot\frac{5}{6} = 8.33\ \text{bits/s/Hz}
$$

$$
\text{SNR}_{\min,ideal} = 2^{8.33}-1 \approx 321
$$

$$
10\log_{10}(321) \approx 25.1\ \text{dB}
$$

La diferencia ideal es de aproximadamente **$5\ \text{dB}$**, lo cual ya es significativa. En la práctica, la penalización puede ser aún mayor.

**Descripción de Figura — Constelación 1024-QAM vs 4096-QAM:**

> *La Figura 9.2 debe mostrar dos diagramas de constelación en el plano I-Q. A la izquierda, una cuadrícula de 32×32 puntos correspondiente a 1024-QAM; a la derecha, una cuadrícula de 64×64 puntos correspondiente a 4096-QAM. En ambos casos, los ejes horizontal y vertical deben etiquetarse como I (in-phase) y Q (quadrature). Una línea roja debe marcar la distancia mínima entre puntos adyacentes, mostrando visualmente que en 4096-QAM los puntos están mucho más apretados para la misma potencia media. Debajo de cada constelación debe aparecer un pequeño recuadro comparando “10 bits/símbolo” frente a “12 bits/símbolo” y una nota indicando que la mejora del 20% exige una calidad de canal mucho mayor. La figura debe transmitir la intuición de que el precio de meter más bits por símbolo es hacer la decisión del receptor mucho más delicada frente al ruido y a la distorsión.*

#### 9.2.4 Hasta 16 flujos espaciales

WiFi 7 amplía el número máximo de flujos espaciales hasta **16**, frente a los 8 de WiFi 5 y WiFi 6 [22], [18], [24]–[26].

La expresión más general de la capacidad MIMO es

$$
C = B\log_2\det\left(\mathbf{I}_{N_r} + \frac{\rho}{N_t}\mathbf{H}\mathbf{H}^H\right)
$$

donde:

- $\mathbf{H}$ es la matriz de canal MIMO,
- $N_t$ es el número de antenas transmisoras,
- $N_r$ es el número de antenas receptoras,
- $\rho$ es la SNR total,
- $\mathbf{I}_{N_r}$ es la matriz identidad de dimensión $N_r$.

**Explicación pedagógica:** esta ecuación dice que la capacidad depende del rango y de los autovalores de la matriz de canal. Si el canal ofrece múltiples caminos suficientemente independientes, entonces pueden enviarse varios flujos paralelos a la vez.

En una simplificación ideal, si hay $N_{SS}$ flujos ortogonales con la misma SNR, puede aproximarse como

$$
C \approx N_{SS} B\log_2(1+\gamma)
$$

donde $\gamma$ es la SNR por flujo.

**Ejemplo numérico:** para $B=320\ \text{MHz}$ y $\gamma=20\ \text{dB}=100$,

- con $N_{SS}=8$:

$$
C_8 \approx 8\cdot320\times10^6\cdot\log_2(101) \approx 17.0\ \text{Gbps}
$$

- con $N_{SS}=16$:

$$
C_{16} \approx 16\cdot320\times10^6\cdot\log_2(101) \approx 34.1\ \text{Gbps}
$$

La duplicación de flujos espaciales **duplica la capacidad ideal**. Sin embargo, en la práctica solo se logra esta ganancia si el hardware, el canal y la correlación espacial lo permiten.

**Comparación histórica:**

- **WiFi 5:** hasta 8 SS
- **WiFi 6/6E:** hasta 8 SS
- **WiFi 7:** hasta 16 SS

---

### 9.3 Cálculo de Throughput Máximo Teórico de WiFi 7

La fórmula de velocidad PHY pedida en este tutorial es

$$
R = N_{SS} \times \frac{N_{SD}}{T_{\text{sym}}} \times \log_2(M) \times R_c
$$

donde:

- $N_{SS}$ = número de flujos espaciales,
- $N_{SD}$ = número de subportadoras de datos,
- $T_{\text{sym}}$ = duración del símbolo OFDM,
- $M$ = orden de modulación,
- $R_c$ = tasa de codificación.

#### 9.3.1 Significado físico de cada parámetro

- $\frac{N_{SD}}{T_{\text{sym}}}$ indica cuántas subportadoras de datos se transmiten por segundo.
- $\log_2(M)$ indica cuántos bits lleva cada símbolo QAM.
- $R_c$ corrige por redundancia de codificación; por ejemplo, $5/6$ significa que de cada 6 bits transmitidos, 5 son útiles.
- $N_{SS}$ multiplica el resultado por el número de flujos espaciales paralelos.

#### 9.3.2 Parámetros para el caso máximo WiFi 7

Tomamos la configuración extrema más citada para WiFi 7:

- $N_{SS}=16$
- $N_{SD}=3920$ para 320 MHz EHT
- $T_{\text{sym}} = 12.8\ \mu s + 0.8\ \mu s = 13.6\ \mu s$
- $M=4096 \Rightarrow \log_2(M)=12$
- $R_c = 5/6$

Sustituyendo en la fórmula:

$$
R = 16 \times \frac{3920}{13.6\times10^{-6}} \times 12 \times \frac{5}{6}
$$

Conviene agrupar primero los bits útiles por símbolo y por flujo espacial:

$$
3920 \times 12 = 47040\ \text{bits/símbolo bruto por flujo}
$$

Aplicando la codificación:

$$
47040\times\frac{5}{6} = 39200\ \text{bits útiles/símbolo por flujo}
$$

Ahora calculamos la tasa por flujo:

$$
R_{1\,SS} = \frac{39200}{13.6\times10^{-6}} \approx 2.882352941\times10^9\ \text{bps}
$$

es decir,

$$
R_{1\,SS} \approx 2.882\ \text{Gbps}
$$

Finalmente, con 16 flujos espaciales:

$$
R = 16\times 2.882\ \text{Gbps} \approx 46.12\ \text{Gbps}
$$

Por tanto,

$$
\boxed{R_{\text{WiFi 7, máx}} \approx 46.1\ \text{Gbps}}
$$

#### 9.3.3 ¿Por qué el resultado es tan alto?

Porque WiFi 7 combina **cuatro multiplicadores grandes** al mismo tiempo:

1. **320 MHz** de ancho de canal,
2. **3920** subportadoras de datos,
3. **12 bits por símbolo** con 4096-QAM,
4. **16 flujos espaciales**.

Si cualquiera de estos factores disminuye, la velocidad también disminuye proporcionalmente.

#### 9.3.4 Tabla comparativa con WiFi 5, 6 y 6E

| Generación | Configuración extrema de referencia | Fórmula resumida | Velocidad PHY máxima aproximada |
|---|---|---|---:|
| WiFi 5 | 8 SS, 160 MHz, 256-QAM, $R_c=5/6$, GI corto | $8\times468\times8\times\frac{5}{6}/3.6\mu s$ | $6.93\ \text{Gbps}$ |
| WiFi 6 | 8 SS, 160 MHz, 1024-QAM, $R_c=5/6$ | $8\times1960\times10\times\frac{5}{6}/13.6\mu s$ | $9.6\ \text{Gbps}$ |
| WiFi 6E | Igual a WiFi 6, pero en 6 GHz | misma expresión | $9.6\ \text{Gbps}$ |
| WiFi 7 | 16 SS, 320 MHz, 4096-QAM, $R_c=5/6$ | $16\times3920\times12\times\frac{5}{6}/13.6\mu s$ | $46.1\ \text{Gbps}$ |

**Observación importante:** esta tabla compara **tasas PHY máximas teóricas**. El rendimiento útil a nivel IP o aplicación siempre será menor por sobrecarga MAC/PHY, contención, ACKs, cabeceras, colisiones y variabilidad del canal.

---

### 9.4 Multi-Link Operation (MLO) — Análisis Detallado

MLO es probablemente la característica más transformadora de WiFi 7 porque cambia la forma de pensar el enlace inalámbrico: ya no es “una estación asociada a una banda”, sino “un dispositivo multi-enlace coordinado”.

#### 9.4.1 Concepto de MLD (Multi-Link Device)

Un **MLD** es una abstracción lógica que agrupa múltiples enlaces 802.11 bajo una entidad común [22]–[23]. Puede tratarse de:

- un **AP-MLD**, o
- una **STA-MLD**.

El MLD comparte funciones de gestión, asociación y coordinación, mientras que cada enlace mantiene su propia PHY y su propia operación de canal.

Pedagógicamente, puede pensarse así:

- antes: **un dispositivo = un enlace principal**;
- ahora: **un dispositivo = una plataforma que coordina varios enlaces**.

#### 9.4.2 Tipos principales de MLO

##### a) STR — Simultaneous Transmit and Receive

En **STR**, el dispositivo puede transmitir y recibir simultáneamente en distintos enlaces, siempre que el hardware lo permita. Es el caso más potente, porque permite verdadero paralelismo.

##### b) NSTR — Non-Simultaneous Transmit and Receive

En **NSTR**, existen limitaciones de coexistencia interna, aislamiento RF o arquitectura del front-end, de modo que el dispositivo no puede transmitir y recibir libremente al mismo tiempo en todos los enlaces. Aun así, sigue habiendo coordinación multi-enlace, pero con restricciones de simultaneidad.

##### c) eMLSR — operación multi-enlace mejorada con radio único

En **eMLSR**, un único radio o una arquitectura con recursos RF compartidos puede conmutar o coordinar múltiples enlaces de forma mejorada, aunque no con el paralelismo completo de un STR puro. Es especialmente relevante para clientes de costo/consumo limitado.

#### 9.4.3 Modelo matemático de caudal agregado

En una forma un poco más realista que la de la Sección 9.2, el caudal agregado puede escribirse como

$$
R_{\text{agg}} = \sum_{\ell=1}^{L} p_{\ell}\,\alpha_{\ell}\,R_{\ell}
$$

donde:

- $p_{\ell}$ es la fracción del tráfico asignada al enlace $\ell$,
- $\alpha_{\ell}$ es la eficiencia MAC/PHY útil del enlace,
- $R_{\ell}$ es la tasa PHY nominal del enlace.

La condición natural es

$$
\sum_{\ell=1}^{L} p_{\ell} = 1
$$

si solo estamos repartiendo el tráfico total entre enlaces.

**Explicación:**

- Si $p_{\ell}$ es grande, significa que mucho tráfico usa ese enlace.
- Si $\alpha_{\ell}$ es bajo, ese enlace es ineficiente, quizá por contención o por mala calidad de canal.
- El producto $p_{\ell}\alpha_{\ell}R_{\ell}$ representa la contribución útil de cada enlace al total.

#### 9.4.4 Modelo de reducción de latencia

Para tráfico crítico, una estrategia frecuente es la duplicación selectiva. Si la probabilidad de éxito en un enlace es $p_{s,\ell}$ y se duplican paquetes sobre enlaces independientes, la probabilidad de que **al menos uno** llegue correctamente es

$$
P_{\text{éxito,dup}} = 1 - \prod_{\ell=1}^{L}(1-p_{s,\ell})
$$

**Interpretación:**

- $(1-p_{s,\ell})$ es la probabilidad de fallo del enlace $\ell$.
- El producto de todos los fallos es la probabilidad de que fallen todos a la vez.
- Restar ese valor a 1 da la probabilidad de éxito global.

**Ejemplo:** si dos enlaces tienen probabilidades de éxito $0.92$ y $0.95$,

$$
P_{\text{éxito,dup}} = 1 - (1-0.92)(1-0.95)
$$

$$
P_{\text{éxito,dup}} = 1 - (0.08)(0.05) = 1 - 0.004 = 0.996
$$

Es decir, la fiabilidad sube a **99.6%** para ese paquete duplicado.

#### 9.4.5 Ejemplo detallado: hogar con 3 enlaces simultáneos

Consideremos un AP-MLD y un cliente-MLD con estos enlaces:

- **2.4 GHz, 40 MHz, 2 SS, 1024-QAM, $R_c=5/6$**
- **5 GHz, 160 MHz, 2 SS, 4096-QAM, $R_c=5/6$**
- **6 GHz, 320 MHz, 2 SS, 4096-QAM, $R_c=5/6$**

Aproximaremos sus tasas PHY como:

- $R_{2.4} \approx 0.574\ \text{Gbps}$
- $R_{5} \approx 2.882\ \text{Gbps}$
- $R_{6} \approx 5.765\ \text{Gbps}$

Si las eficiencias útiles son $\alpha_{2.4}=0.75$, $\alpha_5=0.85$ y $\alpha_6=0.88$, y el planificador reparte el tráfico según $p_{2.4}=0.10$, $p_5=0.30$, $p_6=0.60$, entonces

$$
R_{\text{agg}} = 0.10\cdot0.75\cdot0.574 + 0.30\cdot0.85\cdot2.882 + 0.60\cdot0.88\cdot5.765
$$

$$
R_{\text{agg}} \approx 0.043 + 0.735 + 3.044 = 3.822\ \text{Gbps}
$$

Obsérvese que el caudal agregado útil es menor que la suma bruta porque el tráfico no se reparte uniformemente y porque hemos incluido eficiencia realista.

Ahora estudiemos latencia. Supongamos retardos medios:

- $\bar T_{2.4}=7\ \text{ms}$
- $\bar T_5=4\ \text{ms}$
- $\bar T_6=2.5\ \text{ms}$

Con duplicación para paquetes críticos:

$$
\mathbb{E}[T_{\min}] = \frac{1}{1/7 + 1/4 + 1/2.5}
$$

$$
\mathbb{E}[T_{\min}] = \frac{1}{0.1429 + 0.25 + 0.4} = \frac{1}{0.7929} \approx 1.26\ \text{ms}
$$

Esto no significa que toda la red opere siempre a $1.26\ \text{ms}$, pero sí muestra el potencial matemático de MLO para reducir el retardo de tráfico prioritario.

---

### 9.5 Preamble Puncturing en WiFi 7

#### 9.5.1 ¿Qué es?

**Preamble puncturing** es una técnica que permite usar un canal ancho aunque una parte pequeña del espectro esté ocupada o interferida. En vez de renunciar al canal completo de 320 MHz, el sistema “perfora” o excluye subcanales de 20 MHz o grupos equivalentes y sigue transmitiendo en el resto [22], [24], [26].

La intuición es muy importante: si una sola porción de 20 MHz está contaminada por interferencia, sería muy ineficiente descartar los 320 MHz completos. El puncturing permite conservar la mayor parte del ancho útil.

#### 9.5.2 Ancho efectivo

Si el canal nominal es $B_{\text{nom}}$ y se anulan $N_p$ subcanales de 20 MHz, una primera aproximación al ancho efectivo es

$$
B_{\text{ef}} = B_{\text{nom}} - 20\,N_p\ \text{MHz}
$$

**Explicación:**

- $B_{\text{nom}}$ es el ancho del canal completo, por ejemplo 320 MHz.
- Cada subcanal perforado resta 20 MHz.
- El modelo supone que la reducción del recurso espectral es lineal con el número de subcanales excluidos.

Si además suponemos que la tasa PHY escala aproximadamente con el ancho útil, entonces

$$
R_{\text{punct}} \approx R_{\text{nom}}\frac{B_{\text{ef}}}{B_{\text{nom}}}
$$

#### 9.5.3 Ejemplo: canal de 320 MHz con dos subcanales de 20 MHz perforados

Supongamos:

- $B_{\text{nom}}=320\ \text{MHz}$
- $N_p=2$
- $R_{\text{nom}} = 46.1\ \text{Gbps}$

Entonces,

$$
B_{\text{ef}} = 320 - 20\cdot2 = 280\ \text{MHz}
$$

La tasa aproximada sería

$$
R_{\text{punct}} \approx 46.1\cdot\frac{280}{320}
$$

$$
R_{\text{punct}} \approx 46.1\cdot0.875 = 40.34\ \text{Gbps}
$$

**Interpretación:** con dos perforaciones de 20 MHz, la pérdida teórica es solo del 12.5%, y la red aún conserva más de **40 Gbps** PHY en la configuración extrema. Si, en cambio, hubiera que reducir todo el canal a 160 MHz, el máximo teórico caería aproximadamente a la mitad.

**Descripción de Figura — Preamble puncturing en 320 MHz:**

> *La Figura 9.3 debe representar una barra horizontal de 320 MHz dividida en dieciséis bloques de 20 MHz. Dos de esos bloques, por ejemplo el quinto y el undécimo, deben aparecer en color rojo con una etiqueta “interferencia/incumbente”. Los demás bloques deben mostrarse en verde. Encima de la barra debe dibujarse un preámbulo EHT donde los bloques verdes se mantienen activos y los rojos aparecen marcados como anulados o excluidos. Debajo, una segunda línea debe comparar dos estrategias: “sin puncturing: retroceso a 160 MHz” frente a “con puncturing: 280 MHz efectivos”. La figura debe dejar claro que la innovación no consiste en eliminar la interferencia, sino en evitar que una pequeña porción inutilice el resto del canal ancho.*

---

### 9.6 OFDMA Mejorado en WiFi 7

WiFi 7 hereda la filosofía OFDMA de WiFi 6, pero la hace más flexible para escenarios de muy alta capacidad. Entre las novedades más importantes destacan [22], [25]–[26]:

- soporte de **RUs más grandes**, hasta **$4\times 996$ tonos por RU**,
- **asignación Multi-RU** a un mismo usuario,
- planificación más flexible en canales muy anchos.

#### 9.6.1 Tamaños de Unidad de Recursos (RU)

En términos conceptuales, una **RU** es un subconjunto de subportadoras asignadas a un usuario dentro de un símbolo OFDMA. En EHT aparecen tamaños como:

- 26 tonos,
- 52 tonos,
- 106 tonos,
- 242 tonos,
- 484 tonos,
- 996 tonos,
- $2\times996$ tonos,
- $4\times996$ tonos.

La lógica es sencilla: usuarios con poca demanda reciben RUs pequeñas; usuarios con mucha demanda pueden recibir recursos grandes o múltiples RUs.

#### 9.6.2 Multi-RU allocation

En WiFi 6, un usuario estaba más limitado en cómo recibía recursos OFDMA. WiFi 7 permite que un mismo usuario reciba **varias RUs** dentro de la misma asignación. Esto reduce fragmentación espectral.

Podemos medir la eficiencia de asignación como

$$
\eta_{\text{alloc}} = \frac{N_{\text{útil}}}{N_{\text{asignado}}}
$$

donde:

- $N_{\text{útil}}$ es el número de tonos realmente necesarios o utilizados por el usuario,
- $N_{\text{asignado}}$ es el número de tonos que se le reservan.

**Ejemplo 1: usuario que necesita 726 tonos**

- Sin Multi-RU, podría recibir una RU de 996 tonos.
- Con Multi-RU, podría recibir $484 + 242 = 726$ tonos.

Sin Multi-RU:

$$
\eta_{\text{alloc, WiFi6}} = \frac{726}{996} \approx 0.729 = 72.9\%
$$

Con Multi-RU:

$$
\eta_{\text{alloc, WiFi7}} = \frac{726}{726} = 1 = 100\%
$$

Esto significa que la nueva flexibilidad evita desperdiciar aproximadamente un **27.1%** de los tonos reservados en este ejemplo.

#### 9.6.3 Ejemplo de ocupación en un canal EHT muy ancho

Supongamos un canal donde el planificador reparte recursos así:

- usuario A: $2\times996 = 1992$ tonos,
- usuario B: $996$ tonos,
- usuario C: $484$ tonos,
- usuario D: $484$ tonos.

Entonces el total asignado es

$$
N_{\text{ocupado}} = 1992 + 996 + 484 + 484 = 3956\ \text{tonos}
$$

Si la rejilla OFDMA disponible se aproxima como $4\times996 = 3984$ tonos, la ocupación relativa es

$$
\eta_{\text{rejilla}} = \frac{3956}{3984} \approx 0.993 = 99.3\%
$$

Este resultado ilustra que OFDMA en WiFi 7 puede aprovechar de manera extremadamente fina un canal de gran ancho.

---

### 9.7 Presupuesto de Enlace y Dimensionamiento de Cobertura WiFi 7

En esta sección nos centraremos en la banda de **6 GHz**, que es donde WiFi 7 explota mejor los canales de 320 MHz.

#### 9.7.1 Ecuación general del presupuesto de enlace

La ecuación básica del presupuesto de enlace es

$$
P_{RX} = P_{TX} + G_{TX} - L_{TX} - L_{\text{path}} + G_{RX} - L_{RX}
$$

donde:

- $P_{RX}$ es la potencia recibida en dBm,
- $P_{TX}$ es la potencia transmitida en dBm,
- $G_{TX}$ y $G_{RX}$ son las ganancias de antena en dBi,
- $L_{TX}$ y $L_{RX}$ son pérdidas internas,
- $L_{\text{path}}$ es la pérdida de propagación.

Para que el enlace funcione con un MCS dado, debe cumplirse

$$
P_{RX} \geq S_{\min} + M_{\text{fade}}
$$

donde $S_{\min}$ es la sensibilidad mínima del receptor y $M_{\text{fade}}$ es un margen de desvanecimiento, típicamente entre 6 y 10 dB.

#### 9.7.2 Cálculo de sensibilidad a partir del ruido térmico

Una forma de estimar la sensibilidad es

$$
S_{\min} = -174 + 10\log_{10}(B) + NF + \text{SNR}_{\min}
$$

donde:

- $-174\ \text{dBm/Hz}$ es la densidad espectral de ruido térmico a temperatura ambiente,
- $B$ es el ancho de banda en Hz,
- $NF$ es la figura de ruido del receptor en dB,
- $\text{SNR}_{\min}$ es la SNR mínima necesaria para el MCS considerado.

Tomemos $B=320\ \text{MHz}$ y $NF=7\ \text{dB}$.

Primero, el ruido térmico integrado sobre 320 MHz es

$$
N = -174 + 10\log_{10}(320\times10^6)
$$

$$
N = -174 + 85.05 = -88.95\ \text{dBm}
$$

Añadiendo la figura de ruido:

$$
N_{\text{eq}} = -88.95 + 7 = -81.95\ \text{dBm}
$$

Ahora obtenemos sensibilidades aproximadas para tres niveles de modulación:

1. **MCS bajo** (por ejemplo, BPSK con fuerte protección): $\text{SNR}_{\min}\approx 4\ \text{dB}$

$$
S_{\min, bajo} = -81.95 + 4 = -77.95\ \text{dBm}
$$

2. **MCS medio** (por ejemplo, 256-QAM/1024-QAM intermedio): $\text{SNR}_{\min}\approx 20\ \text{dB}$

$$
S_{\min, medio} = -81.95 + 20 = -61.95\ \text{dBm}
$$

3. **MCS alto** (por ejemplo, 4096-QAM, $R_c=5/6$): $\text{SNR}_{\min}\approx 33\ \text{dB}$

$$
S_{\min, alto} = -81.95 + 33 = -48.95\ \text{dBm}
$$

Estos valores son **estimaciones de ingeniería**, no cifras normativas exactas. Son útiles para dimensionamiento preliminar.

#### 9.7.3 Modelo de pérdida de propagación

Siguiendo el enfoque presentado en las Secciones 2 a 4 y usando un modelo de oficina interior basado en ITU-R P.1238 [27], la pérdida puede estimarse como

$$
L(d) = 20\log_{10}(f) + N\log_{10}(d) + L_f(n) - 28
$$

donde:

- $f$ está en MHz,
- $d$ está en metros,
- $N$ es el coeficiente de pérdida con la distancia,
- $L_f(n)$ es la pérdida adicional por pisos.

Para una oficina en la misma planta, tomamos:

- $f = 6100\ \text{MHz}$,
- $N = 31$,
- $L_f(n)=0$.

Entonces

$$
L(d) = 20\log_{10}(6100) + 31\log_{10}(d) - 28
$$

Como

$$
20\log_{10}(6100) \approx 75.71
$$

obtenemos

$$
L(d) \approx 47.71 + 31\log_{10}(d)
$$

#### 9.7.4 Ejemplo detallado: despliegue empresarial en 6 GHz

Supongamos un AP WiFi 7 indoor con:

- $P_{TX}=23\ \text{dBm}$,
- $G_{TX}=5\ \text{dBi}$,
- $L_{TX}=1\ \text{dB}$,
- cliente con $G_{RX}=2\ \text{dBi}$,
- $L_{RX}=0\ \text{dB}$,
- margen de desvanecimiento $M_{\text{fade}}=8\ \text{dB}$.

Entonces

$$
P_{RX} = 23 + 5 - 1 - L_{\text{path}} + 2 = 29 - L_{\text{path}}
$$

##### Caso A: MCS alto (4096-QAM)

Con $S_{\min,alto}=-48.95\ \text{dBm}$, la potencia requerida con margen es

$$
P_{RX,req} = -48.95 + 8 = -40.95\ \text{dBm}
$$

Por tanto, la pérdida máxima permitida es

$$
L_{\max} = 29 - (-40.95) = 69.95\ \text{dB}
$$

Igualando con el modelo ITU:

$$
69.95 = 47.71 + 31\log_{10}(d)
$$

$$
31\log_{10}(d) = 22.24
$$

$$
\log_{10}(d) = 0.717
$$

$$
d = 10^{0.717} \approx 5.21\ \text{m}
$$

**Conclusión:** 4096-QAM solo es razonable a distancias muy cortas en interior, del orden de **5 m** en este ejemplo.

##### Caso B: MCS medio

Con $S_{\min,medio}=-61.95\ \text{dBm}$,

$$
P_{RX,req} = -61.95 + 8 = -53.95\ \text{dBm}
$$

$$
L_{\max} = 29 - (-53.95) = 82.95\ \text{dB}
$$

Entonces

$$
82.95 = 47.71 + 31\log_{10}(d)
$$

$$
31\log_{10}(d) = 35.24
$$

$$
\log_{10}(d) = 1.137
$$

$$
d = 10^{1.137} \approx 13.71\ \text{m}
$$

**Conclusión:** para modulación media/alta más realista en celda empresarial, el radio útil está del orden de **12–14 m**.

##### Caso C: MCS robusto

Con $S_{\min,bajo}=-77.95\ \text{dBm}$,

$$
P_{RX,req} = -77.95 + 8 = -69.95\ \text{dBm}
$$

$$
L_{\max} = 29 - (-69.95) = 98.95\ \text{dB}
$$

De donde

$$
98.95 = 47.71 + 31\log_{10}(d)
$$

$$
31\log_{10}(d) = 51.24
$$

$$
\log_{10}(d) = 1.653
$$

$$
d = 10^{1.653} \approx 45.0\ \text{m}
$$

Esto muestra una lección fundamental de diseño: **la cobertura básica puede ser amplia, pero la cobertura para 4096-QAM es mucho más pequeña**. En WiFi 7, la red de 6 GHz suele diseñarse por capacidad y calidad, no solo por “llegar señal”.

#### 9.7.5 Consideraciones de planificación celular WiFi 7

Para dimensionar WiFi 7 en 6 GHz, conviene recordar:

- la banda de 6 GHz ofrece mucho espectro, pero **más pérdida de propagación** que 5 GHz y bastante más que 2.4 GHz;
- **320 MHz** es excelente para capacidad, pero exige muy buena calidad de canal;
- **4096-QAM** debe verse como un modo “de proximidad”; no como el MCS de borde de celda;
- en muchas redes empresariales, la capa de 6 GHz se diseña con celdas relativamente pequeñas, mientras 5 GHz y 2.4 GHz aportan respaldo y compatibilidad.

---

### 9.8 Ejemplo Integral de Dimensionamiento WiFi 7

Vamos a desarrollar un caso completo para un edificio de oficinas de **$5000\ \text{m}^2$**.

#### 9.8.1 Escenario de partida

Suposiciones de diseño:

- superficie total: $A_{\text{tot}} = 5000\ \text{m}^2$,
- ocupación máxima: 250 usuarios,
- usuarios activos simultáneos en hora cargada: 150,
- objetivo de diseño: al menos $100\ \text{Mbps}$ útiles por usuario activo,
- latencia objetivo para aplicaciones sensibles en LAN local: menor que $5\ \text{ms}$,
- APs tribanda WiFi 7 con MLO entre 5 GHz y 6 GHz,
- 2.4 GHz reservado sobre todo para IoT y legado.

#### 9.8.2 Dimensionamiento por capacidad

La demanda agregada objetivo es

$$
R_{\text{dem}} = N_{\text{act}}\times R_{\text{usuario}}
$$

donde $N_{\text{act}}=150$ y $R_{\text{usuario}}=100\ \text{Mbps}$.

Entonces

$$
R_{\text{dem}} = 150\times100\ \text{Mbps} = 15000\ \text{Mbps} = 15\ \text{Gbps}
$$

Supongamos que cada AP puede ofrecer, de forma conservadora y promediada en condiciones reales, unos

$$
R_{\text{AP,ef}} = 1.5\ \text{Gbps}
$$

útiles agregando 6 GHz y 5 GHz mediante MLO, después de overhead, reparto multiusuario y variación de MCS.

Entonces el número de APs por capacidad sería

$$
N_{\text{AP,cap}} = \frac{R_{\text{dem}}}{R_{\text{AP,ef}}} = \frac{15}{1.5} = 10
$$

Por capacidad, **10 APs** serían suficientes.

#### 9.8.3 Dimensionamiento por cobertura

Ahora usamos el resultado de la Sección 9.7. Para una cobertura 6 GHz razonable con MCS medio, adoptamos un radio útil de diseño más conservador que el teórico, por ejemplo

$$
r_{\text{diseño}} = 10\ \text{m}
$$

para contemplar paredes, mobiliario, cuerpos humanos y solapamiento entre celdas.

Si aproximamos el área efectiva cubierta por AP como

$$
A_{\text{celda,ef}} = 250\ \text{m}^2
$$

entonces

$$
N_{\text{AP,cov}} = \frac{A_{\text{tot}}}{A_{\text{celda,ef}}} = \frac{5000}{250} = 20
$$

Por cobertura hacen falta **20 APs**.

#### 9.8.4 Decisión final de número de APs

En diseño inalámbrico se toma el máximo entre el resultado por capacidad y el resultado por cobertura:

$$
N_{\text{AP}} = \max(N_{\text{AP,cap}}, N_{\text{AP,cov}})
$$

por tanto,

$$
N_{\text{AP}} = \max(10,20) = 20
$$

**Conclusión principal del ejemplo:** en este despliegue WiFi 7 de 6 GHz, la red queda **limitada por cobertura**, no por capacidad. Esto es muy típico en despliegues modernos de muy alta frecuencia/ancho de banda.

#### 9.8.5 Plan de canales con MLO

Propuesta pedagógica de canalización:

- **6 GHz:** usar **3 bloques de 320 MHz** no solapados, llamados A, B y C.
- **5 GHz:** usar **4 canales de 80 MHz** con reutilización espacial, llamados F1, F2, F3 y F4.
- **2.4 GHz:** canales 1, 6 y 11 para IoT/legado.

Cada AP anuncia un **MLD** con dos enlaces de alto rendimiento:

- **enlace principal de capacidad:** 6 GHz / 320 MHz,
- **enlace de soporte y continuidad:** 5 GHz / 80 MHz.

Una distribución posible para 20 APs en una malla 5×4 es:

- fila 1: A/F1, B/F2, C/F3, A/F4, B/F1
- fila 2: B/F2, C/F3, A/F4, B/F1, C/F2
- fila 3: C/F3, A/F4, B/F1, C/F2, A/F3
- fila 4: A/F4, B/F1, C/F2, A/F3, B/F4

La idea no es memorizar esta matriz, sino entender el principio: **se alternan bloques de 6 GHz y, simultáneamente, se desfasan los canales de 5 GHz** para que el MLO no agregue enlaces altamente correlacionados en interferencia.

#### 9.8.6 Throughput esperado por usuario

Si la demanda total en hora cargada es 15 Gbps y hay 150 usuarios activos, entonces el caudal objetivo medio por usuario ya es

$$
\bar R_{\text{usuario}} = \frac{15\ \text{Gbps}}{150} = 0.1\ \text{Gbps} = 100\ \text{Mbps}
$$

Como el despliegue final usa 20 APs, el número medio de usuarios activos por AP es

$$
N_{\text{act/AP}} = \frac{150}{20} = 7.5
$$

Si cada AP entrega de media $1.5\ \text{Gbps}$ útiles,

$$
\bar R_{\text{usuario,AP}} = \frac{1.5\ \text{Gbps}}{7.5} = 0.2\ \text{Gbps} = 200\ \text{Mbps}
$$

Este valor de **200 Mbps por usuario activo** representa una media razonable dentro de cada celda cuando la carga está balanceada. En condiciones favorables, usuarios cercanos al AP pueden observar picos muy superiores; en borde de celda o en horas de contención más fuerte, el valor será menor.

#### 9.8.7 Análisis de latencia

Supongamos que, para tráfico interactivo, el retardo medio de acceso por enlace es:

- en 6 GHz: $\bar T_6 = 2.4\ \text{ms}$,
- en 5 GHz: $\bar T_5 = 4.0\ \text{ms}$.

Con selección del primero disponible mediante MLO:

$$
\mathbb{E}[T_{\text{acc}}] = \frac{1}{1/2.4 + 1/4.0}
$$

$$
\mathbb{E}[T_{\text{acc}}] = \frac{1}{0.4167 + 0.25} = \frac{1}{0.6667} \approx 1.5\ \text{ms}
$$

Si añadimos aproximadamente:

- $1\ \text{ms}$ de LAN cableada/switching,
- $1\ \text{ms}$ de procesamiento local o servidor cercano,

entonces la latencia total aproximada sería

$$
T_{\text{e2e}} \approx 1.5 + 1 + 1 = 3.5\ \text{ms}
$$

que cumple holgadamente el objetivo de **menos de 5 ms** para servicios locales o de edge computing.

#### 9.8.8 Conclusiones del ejemplo integral

El ejercicio muestra varias lecciones muy importantes:

1. **WiFi 7 no debe dimensionarse solo por tasa pico.**
2. **En 6 GHz, muchas veces manda la cobertura antes que la capacidad.**
3. **MLO permite combinar una capa de alta capacidad (6 GHz) con otra de soporte/continuidad (5 GHz).**
4. **4096-QAM es excelente, pero solo en regiones cercanas al AP.**
5. **La promesa de baja latencia depende tanto del diseño de celdas como del uso inteligente de MLO.**

**Descripción de Figura — Plano conceptual de despliegue en oficina de 5000 m²:**

> *La Figura 9.4 debe mostrar el plano rectangular de una oficina de 100 m × 50 m dividido en zonas de trabajo abiertas, salas de reunión y pasillos. Sobre el plano deben colocarse 20 APs en una disposición tipo malla 5×4, con celdas ligeramente solapadas. Cada AP debe tener dos etiquetas de color: una letra A/B/C para el bloque de 6 GHz y una marca F1/F2/F3/F4 para el canal de 5 GHz. Alrededor de cada AP debe dibujarse un círculo o hexágono de cobertura principal de 6 GHz y otro contorno más amplio para 5 GHz. Flechas pequeñas deben indicar que el tráfico de alto caudal tiende a usar 6 GHz, mientras que el tráfico más robusto o de continuidad puede mantenerse en 5 GHz. En una esquina del plano debe aparecer un recuadro resumen con cuatro números: “20 APs”, “15 Gbps demanda agregada”, “200 Mbps/usuario activo promedio intra-AP” y “latencia local estimada: 3.5 ms”. La figura debe servir como puente entre la teoría de MLO, el presupuesto de enlace y el diseño práctico de una red empresarial.*

## 10. WiFi 8: IEEE 802.11bn — Ultra High Reliability (UHR)

### 10.1 Motivación y Visión de WiFi 8

WiFi 8, asociado al grupo de trabajo **IEEE 802.11bn**, se está concibiendo como la generación orientada no tanto a maximizar el pico de velocidad, sino a mejorar de forma decisiva la **fiabilidad**, la **latencia acotada** y la **coordinación entre puntos de acceso (APs)** [14], [30]. En otras palabras, mientras WiFi 7 enfatiza el rendimiento extremo y la operación multi-enlace, WiFi 8 aspira a que la red inalámbrica se comporte de manera más predecible, más robusta y más cercana a los requisitos de sistemas críticos.

La visión técnica puede resumirse en tres ideas:

- **Latencia determinista:** no basta con que la latencia media sea baja; también debe reducirse la variabilidad (*jitter*), de modo que exista una cota superior razonable para aplicaciones sensibles al tiempo.
- **Coordinación Multi-AP:** varios APs cercanos podrían dejar de comportarse como entidades completamente independientes y pasar a cooperar en transmisión, recepción, planificación y beamforming.
- **Fiabilidad mejorada:** la probabilidad de error de paquete, de retransmisión excesiva o de interrupción perceptible debe disminuir para servicios críticos.

Este cambio de filosofía responde a nuevas aplicaciones objetivo:

- **Automatización industrial:** robots móviles, vehículos guiados autónomos, sensores y actuadores que requieren latencia estable y pérdida de paquetes muy baja.
- **XR (Extended Reality):** realidad aumentada, realidad virtual y realidad mixta, donde pequeñas oscilaciones de latencia pueden producir mareo, desalineación visual o pérdida de inmersión.
- **Telemedicina:** monitorización remota, videoconsulta de alta resolución, transmisión de imágenes médicas y equipos clínicos inalámbricos que no toleran desconexiones frecuentes.

Desde el punto de vista temporal, el trabajo de 802.11bn sigue en desarrollo. La **ratificación se espera aproximadamente hacia 2028**, aunque los detalles técnicos finales todavía pueden cambiar [30]. Por ello, en esta sección hablaremos de **tecnologías propuestas o plausibles**, distinguiendo claramente entre conceptos consolidados y elementos aún sujetos a discusión.

**Descripción de Figura — Visión de una red WiFi 8 UHR cooperativa:**

> *La figura debe representar una planta industrial o un entorno hospitalario dividido en varias zonas. En el techo aparecen tres APs etiquetados como AP₁, AP₂ y AP₃, unidos entre sí por una línea discontinua gruesa que simboliza coordinación mediante red de retorno de baja latencia. Debajo de ellos se observan varios dispositivos: un robot móvil, gafas XR, una estación clínica y sensores IoT. Desde dos APs salen haces coordinados hacia un mismo dispositivo, ilustrando transmisión conjunta. Sobre el dibujo se incluyen etiquetas como “latencia acotada”, “fiabilidad > 99.99%”, “HARQ” y “integración TSN”. En un lateral, una pequeña gráfica muestra dos distribuciones de latencia: una ancha para generaciones previas y otra estrecha para WiFi 8, enfatizando que el objetivo principal no es solo bajar la media, sino reducir la dispersión temporal.*

### 10.2 Tecnologías Clave Propuestas para WiFi 8

#### 10.2.1 Coordinated Multi-AP Operation

En las generaciones anteriores, los APs suelen operar de forma relativamente autónoma: cada uno transmite a sus clientes, compite por el canal y trata de minimizar la interferencia. En WiFi 8 se propone avanzar hacia una operación **coordinada**, donde varios APs cercanos compartan información de canal, estado de colas, horarios de transmisión y posiblemente datos de usuario [30].

Dos variantes importantes son:

- **Joint Transmission (JT):** varios APs transmiten simultáneamente el mismo flujo o flujos complementarios a un mismo equipo.
- **Coordinated Beamforming (CBF):** los APs ajustan sus haces para reforzar la señal útil y reducir la interferencia mutua.

Una forma compacta de modelar la recepción cooperativa es:

$$
\mathbf{y} = \sum_{m=1}^{M} \mathbf{H}_m \mathbf{W}_m \mathbf{s} + \mathbf{n}
$$

donde:

- $\mathbf{y}$ es el vector de señales recibidas por el usuario o conjunto de usuarios.
- $M$ es el número de APs cooperantes.
- $\mathbf{H}_m$ es la matriz de canal entre el AP $m$ y el receptor.
- $\mathbf{W}_m$ es la matriz de precodificación o beamforming usada por el AP $m$.
- $\mathbf{s}$ es el vector de símbolos transmitidos.
- $\mathbf{n}$ es el ruido térmico más interferencia residual.

**Interpretación pedagógica:** esta ecuación dice que la señal final recibida no proviene de un solo AP, sino de la suma de varias contribuciones. Si los APs se coordinan bien, esas contribuciones pueden **sumarse constructivamente**. Si se coordinan mal, pueden interferirse.

Un modelo escalar útil para entender la ganancia de transmisión conjunta es:

$$
P_{\text{rx,coop}} = \left| \sqrt{P_1}e^{j\phi_1} + \sqrt{P_2}e^{j\phi_2} \right|^2
$$

Aquí:

- $P_1$ y $P_2$ son las potencias recibidas desde dos APs.
- $\phi_1$ y $\phi_2$ son sus fases relativas.
- El valor absoluto al cuadrado representa la potencia total resultante tras la suma compleja.

Si $P_1 = P_2 = P$ y además $\phi_1 = \phi_2$, entonces:

$$
P_{\text{rx,coop}} = \left| \sqrt{P} + \sqrt{P} \right|^2 = |2\sqrt{P}|^2 = 4P
$$

Esto implica una **ganancia ideal de 6 dB** respecto a una sola contribución $P$. En la práctica, debido a errores de sincronización temporal, de frecuencia y de fase, la ganancia real suele ser menor. Aun así, incluso una ganancia efectiva de **3 dB** ya puede traducirse en mejoras apreciables de modulación, codificación o estabilidad.

La tasa agregada de un sistema cooperativo MIMO puede aproximarse mediante:

$$
R = B \log_2 \det\left( \mathbf{I} + \frac{\rho}{N_s} \mathbf{H}_{\text{eq}} \mathbf{H}_{\text{eq}}^{H} \right)
$$

donde:

- $B$ es el ancho de banda del canal.
- $\mathbf{I}$ es la matriz identidad.
- $\rho$ es la SNR global disponible.
- $N_s$ es el número de flujos espaciales.
- $\mathbf{H}_{\text{eq}}$ es la matriz de canal equivalente tras combinar los APs cooperantes.
- $(\cdot)^H$ denota conjugado transpuesto.

Esta ecuación generaliza la idea de Shannon al caso MIMO. El determinante captura cuántos “canales paralelos” independientes puede abrir el sistema. Cuando la cooperación mejora la condición de $\mathbf{H}_{\text{eq}}$, la capacidad total también mejora.

**Ejemplo numérico — ganancia cooperativa simple:**

Supóngase un usuario que recibe de un único AP con SNR de $15\ \text{dB}$. En escala lineal:

$$
\gamma_{\text{single}} = 10^{15/10} = 31.62
$$

Si dos APs cooperan y logran una ganancia efectiva de 3 dB, la nueva SNR será $18\ \text{dB}$:

$$
\gamma_{\text{coop}} = 10^{18/10} = 63.10
$$

La eficiencia espectral ideal tipo Shannon pasaría de:

$$
\eta_{\text{single}} = \log_2(1+31.62) = 5.03\ \text{bits/s/Hz}
$$

a:

$$
\eta_{\text{coop}} = \log_2(1+63.10) = 6.00\ \text{bits/s/Hz}
$$

La mejora relativa sería:

$$
\frac{6.00 - 5.03}{5.03} \times 100\% \approx 19.3\%
$$

Es decir, una ganancia de solo 3 dB ya puede aportar casi un 20% de mejora ideal en eficiencia espectral. Si la cooperación también reduce interferencia, la mejora real percibida por el usuario podría ser aún mayor.

#### 10.2.2 HARQ (Hybrid Automatic Repeat Request) para WiFi

Las redes WiFi clásicas usan retransmisiones ARQ: si una trama falla, se vuelve a enviar. **HARQ** añade una idea más poderosa: el receptor no descarta necesariamente la información previa fallida, sino que la **combina** con la retransmisión. Esto mejora la probabilidad de decodificación correcta.

En el caso más simple, denominado **Chase Combining**, la SNR efectiva tras $q$ transmisiones puede modelarse como:

$$
\gamma_q = \sum_{i=1}^{q} \gamma_i
$$

con las SNRs expresadas en escala lineal, no en dB.

**Interpretación:** si un paquete llega dos veces por caminos estadísticamente similares, el receptor puede “sumar evidencia”. Dos copias moderadas pueden equivaler a una sola copia mucho mejor.

Si la probabilidad de error de bloque en cada intento es $P_e^{(i)}$, una aproximación simple para retransmisiones estadísticamente independientes es:

$$
P_{\text{fallo,total}} \approx \prod_{i=1}^{q} P_e^{(i)}
$$

Esta expresión no sustituye a un análisis de codificación detallado, pero ilustra bien la intuición: con más intentos, la probabilidad de que todos fallen cae rápidamente.

La contrapartida es la eficiencia temporal. Un modelo sencillo de rendimiento es:

$$
S = \frac{L\,(1-P_{\text{drop}})}{\mathbb{E}[N_{\text{tx}}] \cdot T_{\text{slot}}}
$$

donde:

- $L$ es la carga útil en bits.
- $P_{\text{drop}}$ es la probabilidad final de perder el paquete tras agotar retransmisiones.
- $\mathbb{E}[N_{\text{tx}}]$ es el número medio de transmisiones por paquete.
- $T_{\text{slot}}$ es el tiempo medio consumido por intento, incluyendo sobrecarga MAC/PHY.

**Qué enseña esta ecuación:** la fiabilidad aumenta al reducir $P_{\text{drop}}$, pero el caudal útil puede disminuir si $\mathbb{E}[N_{\text{tx}}]$ crece demasiado. Por eso HARQ implica un **compromiso caudal útil–fiabilidad**.

**Ejemplo numérico — dos intentos con Chase Combining:**

Supóngase que un paquete de longitud fija tiene:

- BLER inicial de $0.20$ en el primer intento.
- Tras combinar una retransmisión, BLER residual de $0.02$.
- Máximo de 2 transmisiones.

El número medio de transmisiones será aproximadamente:

$$
\mathbb{E}[N_{\text{tx}}] = 1 + 0.20 = 1.20
$$

porque solo se retransmite cuando falla el primer intento, y eso ocurre el 20% de las veces.

La fiabilidad final será:

$$
P_{\text{éxito}} = 1 - 0.02 = 0.98
$$

Si normalizamos el caudal útil respecto al caso ideal de un solo intento perfecto, el factor de eficiencia es:

$$
\eta_{\text{HARQ}} \approx \frac{0.98}{1.20} = 0.817
$$

Es decir, el sistema entrega alrededor del **81.7% del caudal útil ideal**, pero eleva la fiabilidad de **80% a 98%**. En aplicaciones críticas, este intercambio puede ser muy favorable.

#### 10.2.3 Enhanced Deterministic Latency

En redes de propósito general suele medirse la **latencia media**. Sin embargo, en control industrial y XR interesa más la **latencia máxima probable** o incluso una cota superior planificada. WiFi 8 busca integrarse mejor con conceptos de **Time-Sensitive Networking (TSN)**, de forma que ciertas clases de tráfico tengan ventanas de transmisión reservadas, prioridades más estrictas y menor incertidumbre [30].

Un modelo sencillo de latencia acotada es:

$$
D_{\max} = T_{\text{gate}} + T_{\text{sched}} + T_{\text{queue,max}} + N_{\text{retx,max}}\,T_{\text{retx}} + T_{\text{tx}} + T_{\text{proc}}
$$

con:

- $T_{\text{gate}}$: espera hasta la siguiente ventana TSN o de acceso programado.
- $T_{\text{sched}}$: retardo por planificación en MAC.
- $T_{\text{queue,max}}$: peor retardo de cola admitido.
- $N_{\text{retx,max}}$: máximo número de retransmisiones contempladas en el diseño.
- $T_{\text{retx}}$: coste temporal de cada retransmisión.
- $T_{\text{tx}}$: tiempo real de transmisión de la trama.
- $T_{\text{proc}}$: procesamiento en transmisor y receptor.

Esta ecuación es muy importante porque separa la latencia en componentes. Así, el ingeniero puede preguntar: “¿el problema está en la cola, en la contienda, en la retransmisión o en el procesamiento?”

**Ejemplo numérico — enlace para control industrial:**

Supóngase el siguiente presupuesto temporal:

- $T_{\text{gate}} = 250\ \mu s$
- $T_{\text{sched}} = 100\ \mu s$
- $T_{\text{queue,max}} = 200\ \mu s$
- $N_{\text{retx,max}} = 1$
- $T_{\text{retx}} = 300\ \mu s$
- $T_{\text{tx}} = 150\ \mu s$
- $T_{\text{proc}} = 50\ \mu s$

Entonces:

$$
D_{\max} = 250 + 100 + 200 + 1\cdot 300 + 150 + 50 = 1050\ \mu s
$$

Es decir:

$$
D_{\max} = 1.05\ \text{ms}
$$

Este valor no representa la media, sino la **cota presupuestada** en un diseño planificado. Si la aplicación exige menos de 2 ms, el sistema cumpliría. Si exigiera menos de 1 ms, habría que reducir cola, ventanas o retransmisiones.

#### 10.2.4 Potencial 16384-QAM (16K-QAM)

WiFi 7 ya llevó la modulación hasta **4096-QAM**, equivalente a 12 bits por símbolo. Una evolución futura sería **16384-QAM**, que codifica:

$$
\log_2(16384) = 14\ \text{bits/símbolo}
$$

El aumento bruto frente a 4096-QAM es:

$$
\frac{14-12}{12} \times 100\% = 16.7\%
$$

Es decir, el salto de 4K-QAM a 16K-QAM ofrece un incremento mucho menor que saltos generacionales anteriores. Esto ya anticipa una lección de ingeniería: **cada aumento de orden de modulación aporta menos ganancia relativa y exige mucho más SNR**.

Si se usa una tasa de codificación $r_c = 5/6$, la eficiencia espectral bruta ideal sería:

$$
\eta = r_c \log_2(M) = \frac{5}{6}\cdot 14 = 11.67\ \text{bits/s/Hz}
$$

Aplicando la fórmula de Shannon para un límite ideal:

$$
C = B\log_2(1+\text{SNR}) \Rightarrow \text{SNR}_{\min} = 2^{\eta} - 1
$$

sustituyendo $\eta = 11.67$:

$$
\text{SNR}_{\min} = 2^{11.67} - 1 \approx 3251
$$

En dB:

$$
\text{SNR}_{\min,dB} = 10\log_{10}(3251) \approx 35.1\ \text{dB}
$$

Este es un **límite ideal teórico**. En sistemas prácticos, la modulación 16K-QAM necesitaría pérdidas de implementación, márgenes de linealidad, distorsión de fase y no idealidades del receptor, por lo que el requisito real podría acercarse a **41–44 dB** o más dependiendo del diseño.

**Ejemplo numérico — ganancia marginal real:**

Supóngase una configuración OFDM dada donde 4096-QAM entrega 10 Gbps de PHY. Si todo lo demás permanece constante, 16384-QAM ofrecería:

$$
R_{16K} = 10\ \text{Gbps} \times \frac{14}{12} = 11.67\ \text{Gbps}
$$

La ganancia absoluta es:

$$
11.67 - 10 = 1.67\ \text{Gbps}
$$

La pregunta de diseño no es solo “¿gano 1.67 Gbps?”, sino “¿cuántos usuarios y en qué zona podrán realmente sostener la SNR necesaria?”. Si solo un pequeño porcentaje de usuarios, muy cerca del AP, puede aprovechar 16K-QAM, la ganancia media de red será limitada.

**Conclusión técnica:** 16K-QAM es interesante como posibilidad de laboratorio o de escenarios muy favorables, pero no debe verse como el principal motor de WiFi 8. En UHR probablemente sean más importantes la coordinación multi-AP, HARQ y la latencia determinista.

**Descripción de Figura — comparación entre 4096-QAM y 16384-QAM:**

> *La figura debe mostrar dos constelaciones cuadradas en el plano I-Q. La primera, 4096-QAM, aparece como una malla de 64×64 puntos; la segunda, 16384-QAM, como una malla aún más densa de 128×128 puntos. Debe resaltarse con flechas que la distancia mínima entre símbolos disminuye notablemente. En la parte inferior, una curva SNR-versus-BLER compara ambas modulaciones: 4096-QAM alcanza BLER aceptable con SNR alta, mientras 16384-QAM requiere varios dB adicionales para el mismo BLER. A la derecha, un pequeño recuadro resume “ganancia de bits/símbolo = +16.7%” frente a “exigencia de SNR = muy superior”.*

### 10.3 Comparativa Generacional WiFi 5 → WiFi 6 → WiFi 6E → WiFi 7 → WiFi 8

La evolución reciente de WiFi puede resumirse como el paso desde la **mayor velocidad por usuario** (WiFi 5), hacia la **eficiencia en entornos densos** (WiFi 6/6E), luego a la **operación multi-enlace y canales extremos** (WiFi 7), y finalmente a la **fiabilidad ultra-alta y coordinación de red** (WiFi 8).

| Generación | Estándar | Bandas principales | Ancho de canal máx. | Modulación máx. | Multiplexación destacada | Objetivo dominante | Latencia típica esperada | Estado |
|---|---|---|---:|---:|---|---|---|---|
| WiFi 5 | 802.11ac | 5 GHz | 160 MHz | 256-QAM | MU-MIMO DL | Más caudal útil | Decenas de ms | Consolidado |
| WiFi 6 | 802.11ax | 2.4 / 5 GHz | 160 MHz | 1024-QAM | OFDMA + MU-MIMO UL/DL | Eficiencia en alta densidad | Menor que WiFi 5 | Consolidado |
| WiFi 6E | 802.11ax | 6 GHz | 160 MHz | 1024-QAM | OFDMA + MU-MIMO | Más espectro limpio | Menor contención | Consolidado |
| WiFi 7 | 802.11be | 2.4 / 5 / 6 GHz | 320 MHz | 4096-QAM | MLO + 16 SS | Throughput extremo y baja latencia | Muy baja | En despliegue |
| WiFi 8 | 802.11bn | 2.4 / 5 / 6 GHz | 320 MHz (esperado) | 4096-QAM o superior (posible) | Coordinated Multi-AP + HARQ + UHR | Fiabilidad, latencia acotada, coordinación | Determinista / acotada | En desarrollo |

**Evolución conceptual de métricas clave:**

| Métrica | WiFi 5 | WiFi 6/6E | WiFi 7 | WiFi 8 |
|---|---|---|---|---|
| Throughput pico | Alto | Muy alto | Extremadamente alto | Alto/muy alto, pero no foco principal |
| Eficiencia en densidad | Media | Alta | Muy alta | Muy alta |
| Número de usuarios simultáneos | Moderado | Alto | Muy alto | Muy alto con coordinación |
| Robustez a interferencia | Limitada | Mejorada | Mejorada | Objetivo central |
| Latencia media | Moderada | Menor | Muy baja | Baja y más predecible |
| Latencia determinista | No | Parcial | Parcial | Objetivo central |
| Coordinación inter-AP | Muy limitada | Limitada | Limitada/moderada | Elevada |

---

## 11. Dimensionamiento Avanzado de Redes WiFi

### 11.1 Metodología General de Dimensionamiento

Dimensionar una red WiFi significa decidir **cuántos APs se necesitan, dónde deben colocarse, qué bandas y canales usar, y qué capacidad real podrá ofrecerse**. Un error clásico es dimensionar solo por cobertura (“que haya señal”) y olvidar la capacidad (“que la red soporte la carga”). Un diseño serio debe contemplar ambas dimensiones.

La metodología general puede seguir estos pasos:

1. **Definir objetivos de servicio:** cobertura mínima, tasa objetivo, latencia, roaming, voz, vídeo, telemetría, etc.
2. **Caracterizar el entorno:** oficinas, hospital, campus, almacén, industria, altura de techos, materiales, número de plantas.
3. **Recolectar entradas de tráfico:** número de usuarios, simultaneidad, perfiles de aplicación, clases QoS.
4. **Dimensionar por cobertura:** calcular radios de celda y densidad mínima de APs para cumplir nivel RSSI/SNR.
5. **Dimensionar por capacidad:** verificar cuántos APs se necesitan para absorber la demanda agregada.
6. **Planificar reutilización de canal:** decidir anchos de canal y patrón de reutilización por banda.
7. **Ajustar por redundancia y operación real:** roaming, huecos de cobertura, balance de carga, crecimiento futuro.
8. **Validar con simulación y/o levantamiento de campo:** medir RSSI, SNR, solapamiento, utilización de canal y experiencia real.

Una fórmula simple para la demanda agregada de hora cargada es:

$$
R_{\text{BH}} = N_{\text{users}} \cdot a \cdot R_{\text{active}}
$$

con:

- $N_{\text{users}}$: número total de usuarios o dispositivos.
- $a$: factor de actividad o simultaneidad ($0 \le a \le 1$).
- $R_{\text{active}}$: tasa media requerida por usuario activo.

Esta ecuación es importante porque evita sobreestimar o subestimar. No todos los usuarios transmiten al mismo tiempo, pero tampoco se puede asumir una simultaneidad demasiado pequeña en entornos densos.

También conviene distinguir:

- **Dimensionamiento por cobertura:** responde a “¿llega la señal con calidad suficiente?”
- **Dimensionamiento por capacidad:** responde a “¿la celda soporta el tráfico de todos los usuarios?”

En redes modernas, el diseño final suele venir dado por:

$$
N_{\text{AP,final}} = \max\left(N_{\text{AP,cobertura}},\ N_{\text{AP,capacidad}}\right)
$$

Es decir, el número final de APs debe satisfacer simultáneamente ambos criterios.

### 11.2 Dimensionamiento por Cobertura

El dimensionamiento por cobertura parte de modelos de propagación como los tratados en las Secciones 2 a 4 de este tutorial. Para interiores, una referencia muy usada es **ITU-R P.1238** [7]. Una forma habitual del modelo es:

$$
L(d) = 20\log_{10}(f_{\text{MHz}}) + N\log_{10}(d_{\text{m}}) + L_f(n) - 28
$$

donde:

- $L(d)$ es la pérdida de trayecto en dB.
- $f_{\text{MHz}}$ es la frecuencia en MHz.
- $N$ es el coeficiente de pérdida con la distancia, dependiente del entorno.
- $d_{\text{m}}$ es la distancia en metros.
- $L_f(n)$ es la pérdida adicional por atravesar $n$ plantas.
- El término $-28$ ajusta la formulación empírica.

Para calcular el radio de cobertura, primero se obtiene la pérdida máxima admisible mediante balance de enlace:

$$
L_{\max} = P_t + G_t + G_r - M_f - S_{\min}
$$

con:

- $P_t$: potencia transmitida o EIRP en dBm.
- $G_t$ y $G_r$: ganancias de antena del transmisor y receptor en dBi.
- $M_f$: margen de desvanecimiento en dB.
- $S_{\min}$: sensibilidad del receptor en dBm para la modulación objetivo.

**Explicación importante:** como $S_{\min}$ es un número negativo, restarlo equivale a sumar su valor absoluto. Cuanto más exigente sea la modulación, más alto (menos negativo) suele ser $S_{\min}$, y por tanto menor será $L_{\max}$ permitido.

#### Cálculo del radio de celda por banda

Supongamos:

- $P_t = 20\ \text{dBm}$
- $G_t = G_r = 0\ \text{dBi}$
- $M_f = 10\ \text{dB}$
- $S_{\min} = -67\ \text{dBm}$ para servicio robusto de datos/voz

Entonces:

$$
L_{\max} = 20 + 0 + 0 - 10 - (-67) = 77\ \text{dB}
$$

Para un entorno de oficina, tomemos $N = 28$ y una misma planta inicialmente, es decir, $L_f(n)=0$.

**Banda de 2.4 GHz** ($f = 2400\ \text{MHz}$):

$$
77 = 20\log_{10}(2400) + 28\log_{10}(d) - 28
$$

Como $20\log_{10}(2400) = 67.6$ aproximadamente:

$$
77 = 67.6 + 28\log_{10}(d) - 28 = 39.6 + 28\log_{10}(d)
$$

Luego:

$$
28\log_{10}(d) = 37.4
$$

$$
\log_{10}(d) = 1.336
$$

$$
d \approx 10^{1.336} = 21.7\ \text{m}
$$

**Banda de 5 GHz** ($f = 5000\ \text{MHz}$):

$$
77 = 20\log_{10}(5000) + 28\log_{10}(d) - 28
$$

Como $20\log_{10}(5000) \approx 74.0$:

$$
77 = 46.0 + 28\log_{10}(d)
$$

$$
\log_{10}(d) = \frac{31.0}{28} = 1.107
$$

$$
d \approx 12.8\ \text{m}
$$

**Banda de 6 GHz** ($f = 6000\ \text{MHz}$):

$$
77 = 20\log_{10}(6000) + 28\log_{10}(d) - 28
$$

Como $20\log_{10}(6000) \approx 75.6$:

$$
77 = 47.6 + 28\log_{10}(d)
$$

$$
\log_{10}(d) = \frac{29.4}{28} = 1.05
$$

$$
d \approx 11.2\ \text{m}
$$

**Conclusión:** a igualdad de potencia y sensibilidad, la celda se reduce al subir la frecuencia. Esto es coherente con la intuición física: las bandas más altas ofrecen más espectro, pero menor alcance.

#### Impacto de paredes y plantas

Los obstáculos añaden pérdidas adicionales. Si, por ejemplo, una pared introduce $L_w = 5\ \text{dB}$, la pérdida disponible para la distancia ya no es 77 dB sino:

$$
L'_{\max} = 77 - 5 = 72\ \text{dB}
$$

Recalculando para 5 GHz:

$$
72 = 46 + 28\log_{10}(d)
$$

$$
\log_{10}(d) = \frac{26}{28} = 0.929
$$

$$
d \approx 8.5\ \text{m}
$$

Si además existe penetración vertical entre plantas y se adopta $L_f = 18\ \text{dB}$, entonces para 5 GHz:

$$
77 = 46 + 18 + 28\log_{10}(d)
$$

$$
28\log_{10}(d) = 13
$$

$$
d \approx 10^{13/28} = 2.9\ \text{m}
$$

Es decir, **no conviene confiar en cobertura entre plantas** para un diseño robusto. En la práctica, casi siempre se dimensiona cada planta de forma independiente.

#### Ejemplo numérico completo — edificio de varias plantas

Considérese un edificio de oficinas de **3 plantas**, cada una de **40 m × 20 m = 800\ \text{m}^2**. Se desea cobertura de 5 GHz para voz y datos con un objetivo de al menos $-67\ \text{dBm}$ en la mayor parte de las zonas útiles. Se asume radio útil de planificación de **8.5 m** una vez considerada una pared media.

En lugar de usar $\pi r^2$ directamente, conviene introducir un factor de eficiencia geométrica por solapamiento, pasillos, salas y forma real de celdas. Una aproximación práctica es:

$$
A_{\text{ef}} = \kappa \pi r^2
$$

con $\kappa \approx 0.7$.

Sustituyendo:

$$
A_{\text{ef}} = 0.7 \pi (8.5)^2 \approx 159\ \text{m}^2
$$

APs por planta:

$$
N_{\text{AP/planta}} = \left\lceil \frac{800}{159} \right\rceil = 6
$$

APs totales:

$$
N_{\text{AP,total}} = 3 \times 6 = 18
$$

Por cobertura, este edificio requeriría aproximadamente **18 APs**. En un diseño real, estos APs se colocarían desfasados entre plantas para evitar apilamiento vertical excesivo y facilitar la reutilización de canal.

**Descripción de Figura — mapa de calor de cobertura en edificio de tres plantas:**

> *La figura debe mostrar tres planos horizontales apilados, uno por planta. En cada planta se dibujan seis APs en posiciones de techo y un mapa de calor con colores desde verde intenso (RSSI alto) hasta amarillo y rojo (RSSI marginal). Se deben ver claramente zonas de atenuación detrás de paredes estructurales, así como un pequeño solapamiento entre celdas adyacentes para roaming. En el costado, una escala de colores indica umbrales como −55 dBm, −67 dBm y −75 dBm. Entre plantas, flechas verticales tenues muestran que la cobertura entre pisos existe pero es insuficiente para depender de ella operativamente.*

### 11.3 Dimensionamiento por Capacidad

El dimensionamiento por capacidad parte del tráfico. La pregunta central es: **¿cuántos Mbps útiles puede sostener cada AP en condiciones reales y cuánto tráfico agregado exigen los usuarios?**

Si $R_{\text{user}}$ es la tasa media requerida por usuario durante la hora cargada y $C_{\text{AP}}$ es la capacidad útil de un AP, el número mínimo de APs por capacidad puede estimarse con la expresión solicitada:

$$
N_{AP} = \left\lceil \frac{N_{users} \times R_{user}}{C_{AP} \times \eta_{airtime}} \right\rceil
$$

donde:

- $N_{users}$ es el número de usuarios simultáneos o equivalentes.
- $R_{user}$ es la tasa media requerida por usuario en Mbps.
- $C_{AP}$ es la capacidad útil por AP en Mbps, no el PHY máximo publicitado.
- $\eta_{airtime}$ es la eficiencia de airtime, que refleja pérdidas por contienda, cabeceras, ACKs, backoff y otros overheads.

La eficiencia de airtime puede razonarse con:

$$
\eta_{airtime} = \frac{T_{\text{payload}}}{T_{\text{payload}} + T_{\text{oh}} + T_{\text{cont}}}
$$

siendo:

- $T_{\text{payload}}$: tiempo dedicado a datos útiles.
- $T_{\text{oh}}$: tiempo de cabeceras, preámbulos, ACKs, inter-frame spaces.
- $T_{\text{cont}}$: tiempo perdido en contienda, backoff y esperas.

Esta ecuación explica por qué dos redes con el mismo PHY nominal pueden dar capacidades muy distintas en práctica.

#### Planificación de reutilización de canal

La capacidad no depende solo del número de APs; también del número de **canales realmente reutilizables**. Canales muy anchos aumentan la tasa máxima, pero reducen el número de canales no solapados. Por ello:

- En alta densidad, a menudo convienen **20 o 40 MHz** en 5 GHz.
- En 6 GHz, puede ser razonable usar **80 MHz** o más si hay suficiente espectro y menor densidad de interferencia.
- La planificación debe buscar que APs vecinos inmediatos no compartan canal cuando sea posible.

#### Ejemplo numérico completo — campus universitario con 500 usuarios

Considérese un edificio universitario o biblioteca con:

- $N_{users} = 500$ usuarios simultáneos en hora punta.
- Demanda media por usuario $R_{user} = 5\ \text{Mbps}$.
- Capacidad útil por AP $C_{AP} = 500\ \text{Mbps}$.
- Eficiencia de airtime $\eta_{airtime} = 0.45$.

Aplicando la fórmula:

$$
N_{AP} = \left\lceil \frac{500 \times 5}{500 \times 0.45} \right\rceil
$$

$$
N_{AP} = \left\lceil \frac{2500}{225} \right\rceil = \lceil 11.11 \rceil = 12
$$

Por capacidad se requieren **12 APs**.

Si el diseño usa 5 GHz con 40 MHz y, además, una capa 6 GHz con 80 MHz para clientes modernos, puede repartirse la carga. Por ejemplo, si el 40% del tráfico migra a 6 GHz, la contención efectiva en 5 GHz disminuye y la eficiencia de airtime mejora. No obstante, el valor de 12 APs sigue siendo una base razonable de diseño inicial.

**Chequeo de capacidad por AP:**

La carga media agregada es:

$$
R_{\text{total}} = 500 \times 5 = 2500\ \text{Mbps}
$$

Con 12 APs, la carga media por AP sería:

$$
R_{\text{AP,avg}} = \frac{2500}{12} \approx 208.3\ \text{Mbps}
$$

Como la capacidad efectiva por AP es:

$$
C_{\text{ef,AP}} = 500 \times 0.45 = 225\ \text{Mbps}
$$

la red queda ligeramente por debajo del límite medio. En un proyecto real, suele añadirse margen de crecimiento, por ejemplo un **15–20%** extra, lo que podría elevar el diseño a **13 o 14 APs**.

### 11.4 Dimensionamiento Integrado (Cobertura + Capacidad)

El enfoque correcto consiste en calcular ambos resultados y tomar el mayor:

$$
N_{\text{AP,final}} = \max\left(N_{\text{AP,cobertura}}, N_{\text{AP,capacidad}}\right)
$$

Esto refleja una idea fundamental: una red puede tener suficiente cobertura y aun así colapsar por exceso de usuarios; o puede tener suficiente capacidad teórica, pero dejar huecos de señal. Ambos problemas son graves.

#### Ejemplo completo — hospital con requisitos mixtos

Supóngase un hospital de **4 plantas**, cada una de **750\ \text{m}^2**, totalizando:

$$
A_{\text{total}} = 4 \times 750 = 3000\ \text{m}^2
$$

**Requisito de cobertura:** red clínica en 5 GHz con radio útil de planificación de **8.5 m** y área efectiva por AP de **159 m²** como en el ejemplo anterior.

Entonces:

$$
N_{\text{AP,cobertura}} = \left\lceil \frac{3000}{159} \right\rceil = 19
$$

Redondeando conservadoramente por pasillos, quirófanos blindados y redundancia mínima:

$$
N_{\text{AP,cobertura}} \approx 20
$$

**Requisito de capacidad:** en hora punta se estima un equivalente de **500 usuarios/dispositivos activos** entre personal, pacientes, visitantes, carros clínicos y terminales médicas. La demanda media equivalente es $R_{user}=6\ \text{Mbps}$. Se adopta una capacidad útil por AP de $350\ \text{Mbps}$ y una eficiencia de airtime conservadora de $0.35$ por el carácter crítico y heterogéneo del tráfico.

Aplicando la fórmula:

$$
N_{\text{AP,capacidad}} = \left\lceil \frac{500 \times 6}{350 \times 0.35} \right\rceil
$$

$$
N_{\text{AP,capacidad}} = \left\lceil \frac{3000}{122.5} \right\rceil = \lceil 24.49 \rceil = 25
$$

Por tanto:

$$
N_{\text{AP,final}} = \max(20,25) = 25
$$

El hospital debería diseñarse inicialmente con **25 APs**.

#### Consideraciones MLO para WiFi 7

Si el despliegue se realiza con APs WiFi 7, la operación **MLO (Multi-Link Operation)** puede cambiar la forma de interpretar la capacidad. Un AP MLO no multiplica mágicamente por dos la cobertura, pero sí puede:

- dividir tráfico entre 5 y 6 GHz,
- reducir latencia al escoger el enlace menos congestionado,
- mejorar robustez ante interferencia temporal.

Un modelo simple de capacidad agregada MLO es:

$$
C_{\text{MLO}} \approx \beta \sum_{i=1}^{L} C_i
$$

con:

- $L$ = número de enlaces activos.
- $C_i$ = capacidad útil del enlace $i$.
- $\beta$ = factor de eficiencia de agregación ($0 < \beta \le 1$), que representa pérdidas por coordinación, planificación y asimetrías entre enlaces.

**Ejemplo:** si un AP WiFi 7 dispone de dos enlaces útiles, uno de 400 Mbps y otro de 600 Mbps, y la eficiencia real de agregación es $\beta = 0.85$:

$$
C_{\text{MLO}} \approx 0.85(400+600)=850\ \text{Mbps}
$$

Este valor es menor que la suma ideal de 1000 Mbps, pero aun así puede ser muy ventajoso para servicios críticos. En el hospital, por ejemplo, dispositivos clínicos de alta prioridad podrían cursar tráfico simultáneo por 5 y 6 GHz, mientras visitantes usan preferentemente una sola banda.

### 11.5 Herramientas de Planificación y Simulación

En proyectos reales, el cálculo manual sirve para obtener una primera estimación, pero debe validarse con herramientas profesionales. Entre las más utilizadas se encuentran:

- **Ekahau:** muy extendida en entornos empresariales y sanitarios; permite simulación predictiva, importación de planos, modelado de materiales y validación post-despliegue.
- **iBwave Wi-Fi:** fuerte implantación en grandes edificios, hospitales, aeropuertos y diseños multi-planta con documentación profesional.
- **NetSpot:** útil para levantamientos rápidos, validación de cobertura y análisis más ligero.

Las métricas clave a validar son:

- **RSSI:** nivel de señal recibida.
- **SNR:** diferencia entre señal útil y ruido/interferencia.
- **Utilización de canal:** porcentaje de tiempo que el canal está ocupado.
- **Solapamiento entre celdas:** suficiente para roaming, pero no excesivo.
- **Retry rate:** tasa de retransmisión.
- **Latencia y jitter:** especialmente para voz, vídeo y aplicaciones críticas.

Una regla práctica valiosa es: **si el modelo predictivo y la medición real discrepan mucho, la realidad manda**. Los modelos ayudan, pero no reemplazan el *levantamiento de campo*.

---

## 12. Seguridad en Redes WiFi

### 12.1 Evolución de los Protocolos de Seguridad WiFi

La historia de la seguridad WiFi es también la historia del aprendizaje de la industria. Los primeros mecanismos fueron insuficientes; luego surgieron soluciones transitorias; más tarde llegaron protocolos criptográficamente sólidos, y hoy se buscan propiedades avanzadas como secreto perfecto hacia adelante y resistencia frente a ataques offline.

#### WEP: vulnerabilidades fundamentales

**WEP (Wired Equivalent Privacy)** pretendía ofrecer a la red inalámbrica una seguridad “equivalente” a la de una LAN cableada, pero resultó criptográficamente débil [31]. Usaba el cifrador RC4 con un vector de inicialización (IV) de solo **24 bits**, demasiado corto para redes con tráfico elevado.

La probabilidad de colisión de IV puede estimarse con la aproximación de cumpleaños:

$$
P_{\text{col}} \approx 1 - e^{-\frac{n(n-1)}{2\cdot 2^{24}}}
$$

donde:

- $n$ es el número de tramas transmitidas.
- $2^{24}$ es el número total de IVs posibles.
- $P_{\text{col}}$ es la probabilidad de que al menos dos tramas reutilicen el mismo IV.

**Ejemplo numérico:** si se transmiten $n=5000$ tramas:

$$
\frac{n(n-1)}{2\cdot 2^{24}} = \frac{5000\cdot 4999}{33{,}554{,}432} \approx 0.745
$$

Entonces:

$$
P_{\text{col}} \approx 1 - e^{-0.745} \approx 1 - 0.475 = 0.525
$$

Es decir, con solo 5000 tramas ya hay una probabilidad aproximada del **52.5%** de reutilizar IV. Esa reutilización, combinada con debilidades del algoritmo de inicialización de RC4, permitió ataques prácticos de recuperación de clave.

**Lección pedagógica:** un cifrado no es seguro solo por “usar criptografía”; también importan el tamaño del IV, la gestión de claves y el modo operativo.

#### WPA: solución intermedia con TKIP

**WPA** surgió como solución transitoria. Reemplazó varios elementos inseguros de WEP mediante **TKIP (Temporal Key Integrity Protocol)**, que mezclaba claves por paquete y ampliaba protecciones de integridad. Sin embargo, WPA/TKIP seguía condicionado por hardware legado y no se consideró una solución definitiva. Hoy está obsoleto para despliegues serios.

#### WPA2: AES-CCMP y el protocolo de cuatro mensajes

**WPA2** introdujo **AES-CCMP**, basado en AES en modo contador con protección de integridad CBC-MAC. Durante muchos años fue la base de la seguridad WiFi empresarial y doméstica.

El núcleo de establecimiento de claves es el **protocolo de cuatro mensajes**, que deriva una clave temporal a partir de una clave maestra compartida (**PMK**) y de dos nonces aleatorios. Conceptualmente:

$$
\text{PTK} = \text{PRF}\Big(\text{PMK},\ \text{"Pairwise key expansion"},\ \min(AA,SPA)\|\max(AA,SPA)\|\min(ANonce,SNonce)\|\max(ANonce,SNonce)\Big)
$$

donde:

- $\text{PTK}$ es la **Pairwise Transient Key**.
- $\text{PRF}$ es una función pseudoaleatoria.
- $\text{PMK}$ es la **Pairwise Master Key**.
- $AA$ es la MAC del AP (Authenticator Address).
- $SPA$ es la MAC de la estación (Supplicant Address).
- $ANonce$ y $SNonce$ son números aleatorios generados por AP y estación.
- $\|$ significa concatenación.

**Qué significa esta ecuación:** la PTK final depende de la clave maestra, de quiénes son las dos entidades y de dos nonces frescos. Por tanto, aunque dos clientes usen la misma PMK, no deberían generar la misma PTK si sus direcciones o nonces cambian.

La PTK se divide a su vez en subclaves para autenticación, cifrado y protección de integridad. En términos pedagógicos, el protocolo de cuatro mensajes sirve para demostrar posesión de la PMK y generar claves efímeras de sesión.

**Ejemplo conceptual:** si dos sesiones usan la misma PMK pero cambian los nonces, entonces el resultado de la PRF cambia completamente. Esa es la razón por la cual los nonces deben ser únicos y correctamente gestionados.

#### WPA3: SAE (Simultaneous Authentication of Equals)

**WPA3-Personal** sustituye el clásico intercambio basado en PSK por **SAE**, derivado del protocolo **Dragonfly** [33]. Esto es importante por tres razones:

- mejora la resistencia ante ataques de diccionario offline,
- introduce **secreto perfecto hacia adelante**,
- reduce debilidades derivadas del modelo PSK clásico.

En una versión simplificada sobre un grupo finito, cada par deriva un elemento de grupo asociado a la contraseña, llamado **PWE (Password Element)**. Luego cada estación genera dos secretos efímeros y transmite un compromiso.

Una forma pedagógica de escribirlo es:

$$
s_A = r_A + m_A \pmod q
$$

$$
E_A = P^{-m_A}
$$

análogamente para el par B:

$$
s_B = r_B + m_B \pmod q, \qquad E_B = P^{-m_B}
$$

Aquí:

- $P$ es el elemento de grupo derivado de la contraseña.
- $q$ es el orden del grupo.
- $r_A, r_B$ son secretos efímeros privados.
- $m_A, m_B$ son máscaras efímeras adicionales.
- $s_A, s_B$ y $E_A, E_B$ son los valores de compromiso intercambiados.

El secreto compartido se reconstruye como:

$$
K_A = (P^{s_B}E_B)^{r_A}
$$

Sustituyendo $E_B = P^{-m_B}$ y $s_B = r_B + m_B$:

$$
K_A = (P^{r_B+m_B}P^{-m_B})^{r_A} = (P^{r_B})^{r_A} = P^{r_A r_B}
$$

De forma simétrica, B obtiene el mismo secreto:

$$
K_B = P^{r_A r_B}
$$

**Explicación clave:** la contraseña influye porque determina $P$, pero el secreto de sesión también depende de $r_A$ y $r_B$, que son efímeros. Por eso un atacante que grabe el tráfico no puede verificar millones de contraseñas candidatas offline de la forma tradicional.

### 12.2 WPA3 y Enhanced Open — Análisis Detallado

#### Pasos de SAE con ejemplo numérico de juguete

Usaremos un ejemplo pequeño, **solo pedagógico** e inseguro criptográficamente, para ver las operaciones. Sea un grupo módulo 23 y un elemento derivado de contraseña $P=8$.

Supóngase:

- Para A: $r_A=3$, $m_A=4$.
- Para B: $r_B=6$, $m_B=5$.

Entonces los escalares de compromiso son:

$$
s_A = 3 + 4 = 7
$$

$$
s_B = 6 + 5 = 11
$$

Los elementos de compromiso son inversos de potencias de $P$ en el grupo:

$$
E_A = 8^{-4} \bmod 23 = 12
$$

$$
E_B = 8^{-5} \bmod 23 = 13
$$

Ahora A calcula:

$$
K_A = (8^{11} \cdot 13)^3 \bmod 23 = 12
$$

y B calcula el mismo valor compartido:

$$
K_B = (8^{7} \cdot 12)^6 \bmod 23 = 12
$$

Ambos obtienen el mismo secreto, aquí igual a 12. De nuevo: este ejemplo es de juguete, pero muestra la mecánica algebraica del protocolo.

#### Forward secrecy

El **secreto perfecto hacia adelante** significa que, aunque una contraseña se revele en el futuro, eso no permite descifrar automáticamente capturas antiguas. Matemáticamente, el secreto de sesión depende de $r_A$ y $r_B$:

$$
K_{\text{sesión}} \propto P^{r_A r_B}
$$

Si los valores efímeros $r_A$ y $r_B$ no se almacenan y cambian en cada sesión, conocer solo la contraseña posteriormente no basta para reconstruir sesiones pasadas.

#### Protección frente a diccionario offline

En WPA2-PSK, un atacante podía capturar el protocolo de cuatro mensajes y probar offline contraseñas candidatas hasta que cuadrara la derivación de clave. En SAE, el atacante necesita una interacción activa y no obtiene un verificador estático tan explotable. Esto eleva drásticamente el coste del ataque masivo.

#### OWE (Opportunistic Wireless Encryption)

**Enhanced Open** usa **OWE (Opportunistic Wireless Encryption)** [34]. La idea es proporcionar cifrado individual en redes abiertas, incluso sin autenticación previa compartida. OWE emplea un intercambio tipo Diffie–Hellman. En forma simplificada:

$$
K = g^{ab} \bmod p
$$

donde:

- $g$ es el generador del grupo.
- $p$ es un primo grande.
- $a$ es el secreto efímero del cliente.
- $b$ es el secreto efímero del AP.
- $K$ es el secreto compartido.

**Ejemplo numérico pedagógico:** sea $p=23$, $g=5$, $a=6$, $b=15$.

Cliente publica:

$$
A = 5^6 \bmod 23 = 8
$$

AP publica:

$$
B = 5^{15} \bmod 23 = 19
$$

Cliente calcula:

$$
K = 19^6 \bmod 23 = 2
$$

AP calcula:

$$
K = 8^{15} \bmod 23 = 2
$$

Ambos comparten el mismo secreto. La gran ventaja de OWE es que **el tráfico ya no va en claro**. La limitación es que **no autentica al AP**, así que no evita por sí solo ataques de *gemelo malicioso*.

#### Modo empresarial de 192 bits

WPA3-Enterprise define un modo de seguridad reforzada de **192 bits** para entornos gubernamentales y corporativos de alta exigencia. El objetivo no es que cada paquete tenga literalmente una “clave de 192 bits” aislada, sino que el conjunto de primitivas criptográficas y parámetros cumpla un nivel de seguridad equivalente a ese orden.

#### PMF (Protected Management Frames)

**PMF** protege tramas de gestión críticas frente a falsificación, en especial *deauthentication* y *disassociation*. Conceptualmente puede verse como una etiqueta de integridad sobre el mensaje de gestión:

$$
MIC = \text{CMAC}(K, m)
$$

donde:

- $m$ es la trama de gestión.
- $K$ es la clave de protección de gestión.
- $MIC$ es el código de integridad.

Si un atacante modifica la trama o la inyecta sin conocer la clave, el receptor detectará el fallo de integridad y la descartará.

**Descripción de Figura — protocolo de cuatro mensajes y transición hacia SAE/OWE:**

> *La figura debe dividirse en tres columnas. En la primera, AP y estación intercambian los cuatro mensajes del protocolo de cuatro mensajes, mostrando visualmente ANonce, SNonce, derivación de PTK y confirmación final. En la segunda, se dibuja el flujo de SAE con mensajes de compromiso y confirmación, resaltando que la contraseña se transforma en un elemento de grupo y que ambos lados generan secretos efímeros. En la tercera, se ilustra OWE como un intercambio Diffie–Hellman sin autenticación, con un candado sobre el canal de datos y una advertencia visible que indique “cifrado sí, autenticación del AP no”. La figura debe dejar muy claro qué problema resuelve cada mecanismo y qué limitaciones persisten.*

### 12.3 Seguridad en WiFi 7

WiFi 7 introduce **MLO**, lo que obliga a replantear algunos aspectos de seguridad. Un dispositivo multi-link puede tener múltiples enlaces físicos asociados a una misma identidad lógica (**MLD, Multi-Link Device**). Esto abre dos enfoques:

- **Seguridad por enlace (per-link):** cada enlace mantiene material criptográfico específico.
- **Seguridad a nivel MLD:** existe una asociación principal y luego derivaciones para cada enlace.

Un modelo conceptual de derivación por enlace es:

$$
K_{\text{link},i} = \text{KDF}(K_{\text{MLD}}, \text{LinkID}_i \| \text{Nonce}_i)
$$

donde:

- $K_{\text{MLD}}$ es una clave maestra asociada al dispositivo multi-link.
- $\text{LinkID}_i$ identifica el enlace $i$.
- $\text{Nonce}_i$ aporta frescura adicional.
- $K_{\text{link},i}$ es la clave específica de cada enlace.

**Interpretación:** si se derivan claves distintas por enlace, se limita el impacto de errores o exposiciones puntuales en uno de ellos. No obstante, la superficie de ataque total aumenta porque hay más estados, más contadores, más sincronización y más posibilidades de inconsistencia [28]–[29].

**Nuevas superficies de ataque potenciales:**

- desincronización entre enlaces,
- manejo incorrecto de contadores o nonces por enlace,
- transición insegura entre enlace principal y secundarios,
- políticas de seguridad inconsistentes entre bandas.

**Mitigaciones recomendadas:**

- derivación estricta de claves por enlace,
- contadores independientes y verificados,
- PMF obligatorio,
- validación coherente de estado multi-link,
- actualización frecuente de firmware y controladores.

**Ejemplo conceptual:** si un MLD usa 3 enlaces y deriva $K_{\text{link},1}$, $K_{\text{link},2}$ y $K_{\text{link},3}$ a partir de una raíz común, un error en el contador de un solo enlace no debería permitir repetir nonces en los otros dos. Esto exige una ingeniería de implementación más cuidadosa que en un enlace único.

### 12.4 Amenazas Comunes y Contramedidas

#### Evil Twin

Un ataque **gemelo malicioso** consiste en desplegar un AP falso con el mismo SSID que la red legítima para atraer clientes. Si la red es abierta o el usuario no valida correctamente certificados, el atacante puede interceptar tráfico o credenciales.

**Contramedidas:**

- WPA3-Enterprise con validación estricta de certificado.
- Listas de APs autorizados y *fingerprinting* de BSSID/canal.
- Detección de APs no inventariados.
- Educación del usuario: no confiar solo en el nombre de la red.

#### Deauthentication y protección con PMF

Antes de PMF, un atacante podía falsificar tramas de desautenticación para expulsar clientes. Con PMF, dichas tramas pasan a requerir protección criptográfica. En términos prácticos, esto elimina gran parte de los ataques triviales de expulsión del cliente.

#### KRACK

El ataque **KRACK** explotó la reinstalación de claves en WPA2 bajo ciertas implementaciones [32]. El problema fundamental era que repetir una clave/transmisión podía llevar a reutilizar nonces. Si se reutiliza el mismo flujo de clave en cifrado tipo *stream* o contador, ocurre algo muy peligroso:

$$
C_1 = P_1 \oplus KS
$$

$$
C_2 = P_2 \oplus KS
$$

donde $KS$ es el mismo keystream reutilizado. Entonces:

$$
C_1 \oplus C_2 = P_1 \oplus P_2
$$

**Interpretación:** el atacante no obtiene directamente cada texto plano, pero sí la relación XOR entre ambos. Si uno de los dos es parcialmente predecible, el otro puede deducirse o al menos quedar seriamente expuesto.

**Ejemplo pedagógico:** si $P_1$ contiene una cabecera conocida y se reutiliza el mismo keystream con otro paquete, la porción equivalente de $P_2$ puede recuperarse por simple XOR.

**Mitigaciones:**

- correcciones de implementación en cliente y AP,
- evitar reinstalación de claves,
- WPA3 y pilas modernas mejor diseñadas,
- actualización de dispositivos heredados.

#### Detección de AP no autorizado

Una forma simple de puntuación de sospecha es:

$$
D = w_1|\Delta RSSI| + w_2\,\mathbf{1}_{BSSID \notin \mathcal{B}} + w_3\,\mathbf{1}_{canal \notin \mathcal{C}}
$$

donde:

- $\Delta RSSI$ es la desviación respecto al patrón esperado.
- $\mathcal{B}$ es el conjunto de BSSIDs autorizados.
- $\mathcal{C}$ es el conjunto de canales autorizados.
- $w_1,w_2,w_3$ son pesos.
- $\mathbf{1}_{\cdot}$ vale 1 si la condición se cumple y 0 si no.

Si $D > \theta$, el sistema genera una alerta. Esta fórmula no es un estándar, sino una manera sencilla de formalizar un sistema de detección basado en reglas.

---

## 13. Tendencias Futuras y Convergencia Tecnológica

### 13.1 Convergencia WiFi-5G/6G

La frontera entre WLAN y red celular es cada vez menos rígida. En vez de pensar “WiFi o 5G”, el futuro apunta a “WiFi y 5G/6G como recursos coordinados” [37]–[38].

#### Network slicing aplicado a WiFi

Aunque el concepto de *segmentación lógica de red* nació en el ámbito 5G, puede extrapolarse a WiFi como partición lógica de recursos por servicio. Si un AP o una infraestructura coordinada reparte fracciones de airtime entre servicios, puede modelarse como:

$$
\sum_{i=1}^{S} \alpha_i \le 1
$$

$$
R_i \approx \alpha_i C_{\text{tot}}
$$

donde:

- $S$ es el número de slices o clases de servicio.
- $\alpha_i$ es la fracción de recurso asignada al slice $i$.
- $C_{\text{tot}}$ es la capacidad total disponible.
- $R_i$ es la tasa garantizable aproximada para el slice $i$.

**Ejemplo:** si un sistema dispone de $C_{\text{tot}} = 1\ \text{Gbps}$ y se reservan fracciones $\alpha_1=0.25$ para voz clínica, $\alpha_2=0.45$ para vídeo médico y $\alpha_3=0.30$ para tráfico de mejor esfuerzo, entonces:

$$
R_1 = 250\ \text{Mbps}, \quad R_2 = 450\ \text{Mbps}, \quad R_3 = 300\ \text{Mbps}
$$

#### ATSSS (Access Traffic Steering, Switching, Splitting)

ATSSS permite dirigir, conmutar o dividir tráfico entre múltiples accesos, típicamente WiFi y 5G [38]. Si un flujo puede enviarse por ambos accesos en paralelo, el caudal útil agregado ideal sería:

$$
R_{\text{tot}} = R_{\text{WiFi}} + R_{5G}
$$

Pero el interés mayor en aplicaciones críticas es la fiabilidad. Si se duplica el tráfico por ambos accesos y los fallos son aproximadamente independientes, la probabilidad de éxito es:

$$
P_{\text{succ,dup}} = 1 - (1-P_{\text{WiFi}})(1-P_{5G})
$$

**Ejemplo numérico:** si WiFi entrega con probabilidad $0.97$ y 5G con probabilidad $0.995$:

$$
P_{\text{succ,dup}} = 1 - (1-0.97)(1-0.995)
$$

$$
P_{\text{succ,dup}} = 1 - (0.03)(0.005) = 0.99985
$$

Esto equivale a **99.985%** de probabilidad de entrega, superior a cada acceso por separado.

#### Compartición de espectro no licenciado: NR-U vs WiFi

La coexistencia entre WiFi y NR-U en bandas no licenciadas exige reglas de acceso justas. Un modelo muy simple de ocupación temporal compartida es:

$$
\rho_{\text{WiFi}} + \rho_{\text{NR-U}} \le 1
$$

where $\rho$ representa la fracción de tiempo de ocupación del canal.

**Ejemplo:** si WiFi usa el 55% del airtime y NR-U el 35%:

$$
0.55 + 0.35 = 0.90
$$

queda un 10% libre o de guarda. Si ambos sistemas intentaran usar de forma persistente más del 100% agregado, la contención y la latencia se dispararían.

### 13.2 WiFi Sensing (802.11bf)

**WiFi Sensing**, asociado a **IEEE 802.11bf**, aprovecha que la señal de radio “ilumina” el entorno. Cuando una persona se mueve, respira o gesticula, altera ligeramente la propagación, y esa alteración puede medirse mediante **CSI (Channel State Information)** [36].

El CSI por subportadora puede modelarse como:

$$
H_k(t) = \frac{Y_k(t)}{X_k(t)}
$$

donde:

- $X_k(t)$ es el símbolo transmitido en la subportadora $k$.
- $Y_k(t)$ es el símbolo recibido.
- $H_k(t)$ captura amplitud y fase del canal en función del tiempo.

Si un objeto se mueve, $H_k(t)$ cambia ligeramente. Analizando esas variaciones puede inferirse presencia, distancia relativa, velocidad o patrones de actividad.

La resolución de distancia está relacionada con el ancho de banda:

$$
\Delta d = \frac{c}{2B}
$$

donde:

- $c$ es la velocidad de la luz.
- $B$ es el ancho de banda efectivo.
- $\Delta d$ es la resolución aproximada en rango.

**Ejemplo:** para $B = 160\ \text{MHz}$:

$$
\Delta d = \frac{3\times 10^8}{2\times 160\times 10^6} = 0.9375\ \text{m}
$$

Para $B = 320\ \text{MHz}$:

$$
\Delta d = \frac{3\times 10^8}{2\times 320\times 10^6} = 0.46875\ \text{m}
$$

Es decir, doblar el ancho de banda casi dobla la resolución espacial.

El movimiento genera además un desplazamiento Doppler:

$$
f_D = \frac{v}{\lambda}
$$

donde:

- $f_D$ es la frecuencia Doppler.
- $v$ es la velocidad radial del objeto.
- $\lambda$ es la longitud de onda.

**Ejemplo:** a 5 GHz, $\lambda \approx 0.06\ \text{m}$. Si una persona camina a $v=1\ \text{m/s}$:

$$
f_D = \frac{1}{0.06} \approx 16.7\ \text{Hz}
$$

Ese pequeño desplazamiento puede detectarse en series temporales del CSI.

**Aplicaciones prometedoras:**

- detección de presencia sin cámaras,
- reconocimiento de gestos,
- monitorización respiratoria y caídas,
- analítica de ocupación de espacios.

**Descripción de Figura — cadena de WiFi sensing basada en CSI:**

> *La figura debe mostrar un AP y un dispositivo cliente intercambiando paquetes OFDM mientras una persona se mueve entre ambos. Deben aparecer múltiples trayectorias de propagación: directa, reflejada en una pared y reflejada en el cuerpo humano. En un recuadro lateral, se presenta una matriz de CSI con ejes “subportadora” y “tiempo”, coloreada según amplitud. Sobre esa matriz se marcan cambios periódicos asociados a respiración y cambios más bruscos asociados a gesto o desplazamiento. Debajo, un flujo de procesamiento indica: adquisición CSI → filtrado → extracción de características → clasificación/estimación. La figura debe transmitir claramente que el sistema no “ve” una imagen, sino perturbaciones del canal inalámbrico.*

### 13.3 Inteligencia Artificial en Redes WiFi

La complejidad creciente de WiFi hace atractiva la incorporación de **IA/ML** para canalización, roaming, balance de carga y planificación dinámica [39].

#### Selección de canal y optimización de roaming

Un controlador puede predecir qué canal tendrá menor interferencia o qué AP ofrecerá mejor experiencia. Si definimos una recompensa que combine caudal útil, latencia y utilización de canal, una política de aprendizaje puede ajustar decisiones en tiempo real.

#### Reinforcement learning para coordinación de APs

Una ecuación fundamental de Q-learning es:

$$
Q_{t+1}(s,a) = Q_t(s,a) + \alpha \Big[r + \gamma \max_{a'} Q_t(s',a') - Q_t(s,a)\Big]
$$

donde:

- $Q_t(s,a)$ es el valor estimado de tomar acción $a$ en estado $s$.
- $\alpha$ es la tasa de aprendizaje.
- $r$ es la recompensa inmediata.
- $\gamma$ es el factor de descuento del futuro.
- $s'$ es el estado siguiente.

**Interpretación:** el algoritmo compara lo que esperaba obtener con lo que realmente observó y corrige su estimación.

**Ejemplo pedagógico:** supongamos que un controlador debe elegir entre canal 36 y canal 52. En cierto instante:

- $Q_t(s,36)=4.0$
- recompensa observada $r=3$
- mejor valor futuro estimado $\max_{a'}Q_t(s',a')=5$
- $\alpha=0.1$
- $\gamma=0.9$

Entonces:

$$
Q_{t+1}(s,36)=4.0+0.1\Big[3+0.9\cdot 5 -4.0\Big]
$$

$$
Q_{t+1}(s,36)=4.0+0.1(3.5)=4.35
$$

El sistema aumenta su confianza en ese canal para estados parecidos.

#### Asignación predictiva de recursos

Un predictor simple de carga puede escribirse como:

$$
\hat{\lambda}(t+1) = \alpha\lambda(t) + (1-\alpha)\hat{\lambda}(t)
$$

donde:

- $\lambda(t)$ es la carga observada actual.
- $\hat{\lambda}(t)$ es la estimación previa.
- $\hat{\lambda}(t+1)$ es la predicción siguiente.

**Ejemplo:** si la carga actual es 80 Mbps, la estimación previa era 60 Mbps y $\alpha=0.3$:

$$
\hat{\lambda}(t+1)=0.3\cdot 80 + 0.7\cdot 60 = 66\ \text{Mbps}
$$

Con este tipo de predicción, un sistema puede activar un segundo enlace MLO, cambiar ancho de canal o adelantar reasignación de usuarios antes de la congestión.

### 13.4 Hacia WiFi en Espectro Superior a 7 GHz

#### Recapitulación de 60 GHz: 802.11ad/ay

Las tecnologías **802.11ad** y **802.11ay** explotan 60 GHz para enlaces multi-gigabit de muy corto alcance, altamente direccionales. El principio es claro: mucha capacidad, pero cobertura muy reducida y alta sensibilidad a bloqueo.

#### Potencial uso de bandas entre 7 y 24 GHz

Mirando al futuro, podría explorarse espectro superior a 7 GHz para nuevos modos WiFi. Estas bandas ofrecerían más ancho de banda, pero con mayores pérdidas y menor difracción. La atenuación de espacio libre se modela como:

$$
L_{fs}(dB) = 32.44 + 20\log_{10}(f_{\text{MHz}}) + 20\log_{10}(d_{\text{km}})
$$

donde:

- $f_{\text{MHz}}$ es la frecuencia en MHz.
- $d_{\text{km}}$ es la distancia en km.
- $L_{fs}$ es la pérdida de espacio libre en dB.

**Ejemplo comparativo a 10 m** ($d=0.01\ \text{km}$):

- A 6 GHz:

$$
L_{fs} = 32.44 + 20\log_{10}(6000) + 20\log_{10}(0.01)
$$

$$
L_{fs} = 32.44 + 75.56 - 40 = 67.99\ \text{dB}
$$

- A 15 GHz:

$$
L_{fs} = 32.44 + 83.52 - 40 = 75.96\ \text{dB}
$$

- A 60 GHz:

$$
L_{fs} = 32.44 + 95.56 - 40 = 87.99\ \text{dB}
$$

Comparando con 6 GHz:

- 15 GHz añade casi **8 dB** extra.
- 60 GHz añade unos **20 dB** extra.

Esto significa que para mantener la misma cobertura habría que aumentar ganancias de antena, usar beamforming más estrecho o aceptar celdas mucho menores.

**Implicaciones prácticas:**

- más capacidad puntual,
- mayor direccionalidad,
- peor penetración en paredes y cuerpos,
- diseño mucho más dependiente de línea de vista y alineamiento.

---

## 14. Conclusiones del Tutorial

Este tutorial, sumando las partes previas y la presente, permite recorrer una línea completa de aprendizaje desde los fundamentos de propagación hasta las tendencias más avanzadas de las WLAN modernas.

### 14.1 Síntesis global

- La evolución de WiFi no consiste solo en “más Mbps”; cada generación responde a un problema distinto.
- WiFi 6/6E mejoró la eficiencia en alta densidad.
- WiFi 7 llevó el caudal útil y la flexibilidad multi-enlace a un nivel sin precedentes.
- WiFi 8 apunta a una meta distinta: **ultra alta fiabilidad, latencia acotada y cooperación entre APs**.
- El dimensionamiento profesional exige combinar **cobertura + capacidad + reutilización + validación de campo**.
- La seguridad ha evolucionado desde diseños frágiles como WEP hasta modelos mucho más sólidos como WPA3-SAE y OWE.
- El futuro de WiFi estará cada vez más ligado a 5G/6G, al sensing, a la IA y a bandas de frecuencia más elevadas.

### 14.2 Ideas clave para el profesional

1. **No diseñar por RSSI únicamente.** Una red con “barras completas” puede fallar por capacidad.
2. **Usar capacidad útil, no PHY máximo publicitado.** El overhead importa.
3. **Separar tráfico por criticidad.** Voz, vídeo, clínica, industria y de mejor esfuerzo no deben tratarse igual.
4. **Adoptar WPA3 y PMF siempre que sea posible.** La seguridad heredada ya no es suficiente.
5. **Prepararse para redes coordinadas.** El futuro no será una suma de APs aislados, sino infraestructuras cooperativas.

### 14.3 Próximos pasos recomendados para el lector

- Repetir los ejemplos numéricos cambiando potencias, sensibilidades y densidades de usuario.
- Realizar un pequeño proyecto de dimensionamiento completo sobre un plano real.
- Comparar resultados manuales con una herramienta predictiva.
- Revisar las especificaciones IEEE 802.11, Wi-Fi Alliance y documentos TSN/5G relacionados.
- Profundizar en MIMO, OFDMA, criptografía aplicada y modelado estocástico de latencia para pasar del nivel introductorio al profesional.

## Referencias

1. T. S. Rappaport, *Wireless Communications: Principles and Practice*, 2nd ed. Upper Saddle River, NJ: Prentice Hall, 2002. ISBN: 978-0130422323.

2. A. Goldsmith, *Wireless Communications*. Cambridge: Cambridge University Press, 2005. DOI: [10.1017/CBO9780511841224](https://doi.org/10.1017/CBO9780511841224).

3. Y. Okumura, E. Ohmori, T. Kawano, and K. Fukuda, "Field strength and its variability in VHF and UHF land-mobile radio service," *Review of the Electrical Communication Laboratory*, vol. 16, no. 9-10, pp. 825–873, Sept.–Oct. 1968.

4. M. Hata, "Empirical formula for propagation loss in land mobile radio services," *IEEE Transactions on Vehicular Technology*, vol. VT-29, no. 3, pp. 317–325, Aug. 1980. DOI: [10.1109/T-VT.1980.23859](https://doi.org/10.1109/T-VT.1980.23859).

5. COST Action 231, "Digital mobile radio towards future generation systems, final report," *European Commission*, EUR 18957, 1999.

6. 3GPP, "Study on channel model for frequencies from 0.5 to 100 GHz," 3GPP TR 38.901, v17.0.0, Mar. 2022. [En línea]. Disponible: https://www.3gpp.org/ftp/Specs/archive/38_series/38.901/

7. ITU-R, "Propagation data and prediction methods for the planning of indoor radiocommunication systems and radio local area networks in the frequency range 900 MHz to 100 GHz," *Recommendation ITU-R P.1238-11*, Sep. 2022. Disponible en: [https://www.itu.int/rec/R-REC-P.1238](https://www.itu.int/rec/R-REC-P.1238)

8. ITU-R, "Attenuation by atmospheric gases and related effects," Recommendation ITU-R P.676-13, 2022.

9. ITU-R, "Specific attenuation model for rain for use in prediction methods," Recommendation ITU-R P.838-3, 2005.

10. IEEE, "IEEE Standard for Information Technology—Telecommunications and Information Exchange Between Systems—Local and Metropolitan Area Networks—Specific Requirements—Part 11: Wireless LAN Medium Access Control (MAC) and Physical Layer (PHY) Specifications—Amendment 1: Enhancements for High-Efficiency WLAN," IEEE Std 802.11ax-2021. DOI: [10.1109/IEEESTD.2021.9442429](https://doi.org/10.1109/IEEESTD.2021.9442429).

11. IEEE 802.11be Task Group, "IEEE P802.11be/D5.0 - Draft Standard for Information Technology—Telecommunications and Information Exchange between Systems Local and Metropolitan Area Networks—Specific Requirements, Part 11: Wireless LAN Medium Access Control (MAC) and Physical Layer (PHY) Specifications, Amendment: Enhancements for Extremely High Throughput (EHT)," 2024.

12. S. Sun et al., "Propagation path loss models for 5G urban micro- and macro-cellular scenarios," in *Proc. IEEE 83rd Vehicular Technology Conference (VTC Spring)*, Nanjing, China, 2016, pp. 1–6. DOI: [10.1109/VTCSpring.2016.7504435](https://doi.org/10.1109/VTCSpring.2016.7504435).

13. T. S. Rappaport et al., "Millimeter wave mobile communications for 5G cellular: It will work!," *IEEE Access*, vol. 1, pp. 335–349, 2013. DOI: [10.1109/ACCESS.2013.2260813](https://doi.org/10.1109/ACCESS.2013.2260813).

14. IEEE Computer Society, "IEEE Standard for Information Technology—Telecommunications and Information Exchange between Systems—Local and Metropolitan Area Networks—Specific Requirements—Part 11: Wireless LAN Medium Access Control (MAC) and Physical Layer (PHY) Specifications," *IEEE Std 802.11-2020*, Feb. 2021. DOI: [10.1109/IEEESTD.2021.9363693](https://doi.org/10.1109/IEEESTD.2021.9363693)

15. IEEE Computer Society, "IEEE Standard for Information Technology—Telecommunications and Information Exchange between Systems—Local and Metropolitan Area Networks—Specific Requirements—Amendment 4: Enhancements for Very High Throughput for Operation in Bands below 6 GHz," *IEEE Std 802.11ac-2013*, Dec. 2013. DOI: [10.1109/IEEESTD.2013.6687187](https://doi.org/10.1109/IEEESTD.2013.6687187)

16. E. Khorov, A. Kiryanov, A. Lyakhov, and G. Bianchi, "A Tutorial on IEEE 802.11ax High Efficiency WLANs," *IEEE Communications Surveys & Tutorials*, vol. 21, no. 1, pp. 197–216, First Quarter 2019. DOI: [10.1109/COMST.2018.2871099](https://doi.org/10.1109/COMST.2018.2871099)

17. B. Bellalta, "IEEE 802.11ax: High-Efficiency WLANs," *IEEE Wireless Communications*, vol. 23, no. 1, pp. 38–46, Feb. 2016. DOI: [10.1109/MWC.2016.7422404](https://doi.org/10.1109/MWC.2016.7422404)

18. D. López-Pérez, A. Garcia-Rodriguez, L. Galati-Giordano, M. Kasslin, and K. Doppler, "IEEE 802.11be Extremely High Throughput: The Next Generation of Wi-Fi Technology Beyond 802.11ax," *IEEE Communications Magazine*, vol. 57, no. 9, pp. 113–119, Sep. 2019. DOI: [10.1109/MCOM.001.1900338](https://doi.org/10.1109/MCOM.001.1900338)

19. M. S. Afaqui, E. Garcia-Villegas, and E. Lopez-Aguilera, "IEEE 802.11ax: Challenges and Requirements for Future High Efficiency WiFi," *IEEE Wireless Communications*, vol. 24, no. 3, pp. 130–137, Jun. 2017. DOI: [10.1109/MWC.2016.1600089WC](https://doi.org/10.1109/MWC.2016.1600089WC)

20. Wi-Fi Alliance, "Wi-Fi 6E: The Next Great Chapter in Wi-Fi," White Paper, 2021. Disponible en: [https://www.wi-fi.org/discover-wi-fi/wi-fi-6e](https://www.wi-fi.org/discover-wi-fi/wi-fi-6e)

21. Federal Communications Commission (FCC), "Unlicensed Use of the 6 GHz Band," *Report and Order and Further Notice of Proposed Rulemaking*, ET Docket No. 18-295, Apr. 2020.

22. IEEE Computer Society, *IEEE Standard for Information Technology—Telecommunications and information exchange between systems Local and metropolitan area networks—Specific requirements—Part 11: Wireless LAN Medium Access Control (MAC) and Physical Layer (PHY) Specifications Amendment 2: Enhancements for Extremely High Throughput (EHT)*, **IEEE Std 802.11be-2024**, 2024.

23. IEEE Computer Society, *IEEE Draft Standard for Information Technology—Telecommunications and information exchange between systems Local and metropolitan area networks—Specific requirements—Part 11: Wireless LAN Medium Access Control (MAC) and Physical Layer (PHY) Specifications Amendment 9: Enhancements for Extremely High Throughput (EHT)*, **IEEE P802.11be/D3.0**, 2022. DOI: [10.1109/IEEESTD.2022.9808491](https://doi.org/10.1109/IEEESTD.2022.9808491)

24. B. Bellalta, “Wi-Fi 7 Strikes Back,” *IEEE Communications Magazine*, vol. 59, no. 4, pp. 102–108, Apr. 2021. DOI: [10.1109/MCOM.001.2100043](https://doi.org/10.1109/MCOM.001.2100043)

25. M. A. Kishk, T. Khattab, M. Guizani, J. S. Thompson, and M. Ghogho, “A Survey on IEEE 802.11be (Wi-Fi 7): Recent Advances, Open Challenges, and Future Trends,” *IEEE Communications Surveys & Tutorials*, vol. 24, no. 2, pp. 909–957, 2022. DOI: [10.1109/COMST.2022.3154044](https://doi.org/10.1109/COMST.2022.3154044)

26. B. Bellalta, J. Barceló, A. Zubow, A. D. Campo, and T. Rasheed, “IEEE 802.11be Extremely High Throughput (Wi-Fi 7): Advances and Future Directions,” *IEEE Communications Surveys & Tutorials*, vol. 24, no. 1, pp. 674–716, 2022. DOI: [10.1109/COMST.2022.3141194](https://doi.org/10.1109/COMST.2022.3141194)

27. ITU-R, *Recommendation ITU-R P.1238-13: Propagation data and prediction methods for the planning of indoor radiocommunication systems and radio local area networks in the frequency range 300 MHz to 450 GHz*, International Telecommunication Union, 2023.

28. E. Khorov, I. Levitsky, and A. Kiryanov, "IEEE 802.11be: Wi-Fi 7 Strikes Back," *IEEE Communications Standards Magazine*, vol. 4, no. 3, pp. 40–47, 2020. DOI: [10.1109/MCOMSTD.001.2000014](https://doi.org/10.1109/MCOMSTD.001.2000014)

29. J. Li, X. Peng, Z. Liu, and Y. Wang, "Multi-link Operation in Wi-Fi 7: Overview and Performance," *IEEE Communications Standards Magazine*, vol. 7, no. 2, pp. 43–49, 2023. DOI: [10.1109/MCOMSTD.001.2200019](https://doi.org/10.1109/MCOMSTD.001.2200019)

30. E. Khorov, A. Kiryanov, A. Krasilov, G. Bianchi, and Y. Shi, "IEEE 802.11bn: Ultra High Reliability in Next-Generation Wi-Fi," *IEEE Communications Standards Magazine*, vol. 8, no. 1, pp. 58–64, 2024. DOI: [10.1109/MCOMSTD.2024.3343936](https://doi.org/10.1109/MCOMSTD.2024.3343936)

31. N. Borisov, I. Goldberg, and D. Wagner, "Intercepting Mobile Communications: The Insecurity of 802.11," in *Proceedings of the 7th Annual International Conference on Mobile Computing and Networking (MobiCom '01)*, pp. 180–189, 2001. DOI: [10.1145/381677.381695](https://doi.org/10.1145/381677.381695)

32. M. Vanhoef and F. Piessens, "Key Reinstallation Attacks: Forcing Nonce Reuse in WPA2," in *Proceedings of the 24th ACM SIGSAC Conference on Computer and Communications Security*, pp. 1313–1328, 2017. DOI: [10.1145/3133956.3134027](https://doi.org/10.1145/3133956.3134027)

33. D. Harkins, "Dragonfly Key Exchange," RFC 7664, RFC Editor, Oct. 2015. DOI: [10.17487/RFC7664](https://doi.org/10.17487/RFC7664)

34. D. Harkins and W. Kumari, "Opportunistic Wireless Encryption," RFC 8110, RFC Editor, Mar. 2017. DOI: [10.17487/RFC8110](https://doi.org/10.17487/RFC8110)

35. Wi-Fi Alliance, *Wi-Fi CERTIFIED WPA3™ Specification*, 2020. Disponible en: [https://www.wi-fi.org/](https://www.wi-fi.org/)

36. J. Zhang, Y. Xiao, S. Chen, J. Choi, and P. Fan, "IEEE 802.11bf: Toward Wi-Fi Sensing—Current Status and Directions for IoT Applications," *IEEE Internet of Things Journal*, vol. 9, no. 1, pp. 716–732, 2022. DOI: [10.1109/JIOT.2021.3103215](https://doi.org/10.1109/JIOT.2021.3103215)

37. M. Y. Alias, N. M. Din, N. Fisal, and N. F. Abdullah, "Converged 5G and Wi-Fi Networks: Opportunities and Challenges," *IEEE Access*, vol. 9, pp. 29641–29659, 2021. DOI: [10.1109/ACCESS.2021.3058482](https://doi.org/10.1109/ACCESS.2021.3058482)

38. T. Paavola, F. Mir, M. Serror, C. Caba, E. Seidel, and J. Torsner, "Transport Protocol Considerations for ATSSS Services in 5G," *IEEE Communications Standards Magazine*, vol. 6, no. 3, pp. 62–68, 2022. DOI: [10.1109/MCOMSTD.001.2100005](https://doi.org/10.1109/MCOMSTD.001.2100005)

39. D. Atzeni, D. Bacciu, D. Mazzei, and G. Prencipe, "A Systematic Review of Wi-Fi and Machine Learning Integration with Topic Modeling Techniques," *Sensors*, vol. 22, no. 13, 4925, 2022. DOI: [10.3390/s22134925](https://doi.org/10.3390/s22134925)

40. G. V. Frangulea, P. Assimakopoulos, B. Bojović, and S. Lagén, "NR-U and Wi-Fi Coexistence in sub-7 GHz bands: Implementation and Evaluation of NR-U Type 1 Channel Access in ns-3," in *2024 Workshop on ns-3 (WNS3 2024)*, 2024. DOI: [10.1145/3659111.3659114](https://doi.org/10.1145/3659111.3659114)
