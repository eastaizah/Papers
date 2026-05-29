# Tutorial de Redes Inalámbricas — Parte 3B: WiFi 8, Dimensionamiento Avanzado, Seguridad y Tendencias Futuras

**Autor:** Tutorial Pedagógico de Telecomunicaciones  
**Nivel:** Introductorio–Avanzado  
**Continuación de:** Parte 3A — WiFi 7 (secciones 9.1–9.8)

---

## 10. WiFi 8: IEEE 802.11bn — Ultra High Reliability (UHR)

### 10.1 Motivación y Visión de WiFi 8

WiFi 8, asociado al grupo de trabajo **IEEE 802.11bn**, se está concibiendo como la generación orientada no tanto a maximizar el pico de velocidad, sino a mejorar de forma decisiva la **fiabilidad**, la **latencia acotada** y la **coordinación entre puntos de acceso (APs)** [1], [4]. En otras palabras, mientras WiFi 7 enfatiza el rendimiento extremo y la operación multi-enlace, WiFi 8 aspira a que la red inalámbrica se comporte de manera más predecible, más robusta y más cercana a los requisitos de sistemas críticos.

La visión técnica puede resumirse en tres ideas:

- **Latencia determinista:** no basta con que la latencia media sea baja; también debe reducirse la variabilidad (*jitter*), de modo que exista una cota superior razonable para aplicaciones sensibles al tiempo.
- **Coordinación Multi-AP:** varios APs cercanos podrían dejar de comportarse como entidades completamente independientes y pasar a cooperar en transmisión, recepción, planificación y beamforming.
- **Fiabilidad mejorada:** la probabilidad de error de paquete, de retransmisión excesiva o de interrupción perceptible debe disminuir para servicios críticos.

Este cambio de filosofía responde a nuevas aplicaciones objetivo:

- **Automatización industrial:** robots móviles, vehículos guiados autónomos, sensores y actuadores que requieren latencia estable y pérdida de paquetes muy baja.
- **XR (Extended Reality):** realidad aumentada, realidad virtual y realidad mixta, donde pequeñas oscilaciones de latencia pueden producir mareo, desalineación visual o pérdida de inmersión.
- **Telemedicina:** monitorización remota, videoconsulta de alta resolución, transmisión de imágenes médicas y equipos clínicos inalámbricos que no toleran desconexiones frecuentes.

Desde el punto de vista temporal, el trabajo de 802.11bn sigue en desarrollo. La **ratificación se espera aproximadamente hacia 2028**, aunque los detalles técnicos finales todavía pueden cambiar [4]. Por ello, en esta sección hablaremos de **tecnologías propuestas o plausibles**, distinguiendo claramente entre conceptos consolidados y elementos aún sujetos a discusión.

**Descripción de Figura — Visión de una red WiFi 8 UHR cooperativa:**

> *La figura debe representar una planta industrial o un entorno hospitalario dividido en varias zonas. En el techo aparecen tres APs etiquetados como AP₁, AP₂ y AP₃, unidos entre sí por una línea discontinua gruesa que simboliza coordinación mediante red de retorno de baja latencia. Debajo de ellos se observan varios dispositivos: un robot móvil, gafas XR, una estación clínica y sensores IoT. Desde dos APs salen haces coordinados hacia un mismo dispositivo, ilustrando transmisión conjunta. Sobre el dibujo se incluyen etiquetas como “latencia acotada”, “fiabilidad > 99.99%”, “HARQ” y “integración TSN”. En un lateral, una pequeña gráfica muestra dos distribuciones de latencia: una ancha para generaciones previas y otra estrecha para WiFi 8, enfatizando que el objetivo principal no es solo bajar la media, sino reducir la dispersión temporal.*

### 10.2 Tecnologías Clave Propuestas para WiFi 8

#### 10.2.1 Coordinated Multi-AP Operation

En las generaciones anteriores, los APs suelen operar de forma relativamente autónoma: cada uno transmite a sus clientes, compite por el canal y trata de minimizar la interferencia. En WiFi 8 se propone avanzar hacia una operación **coordinada**, donde varios APs cercanos compartan información de canal, estado de colas, horarios de transmisión y posiblemente datos de usuario [4].

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

En redes de propósito general suele medirse la **latencia media**. Sin embargo, en control industrial y XR interesa más la **latencia máxima probable** o incluso una cota superior planificada. WiFi 8 busca integrarse mejor con conceptos de **Time-Sensitive Networking (TSN)**, de forma que ciertas clases de tráfico tengan ventanas de transmisión reservadas, prioridades más estrictas y menor incertidumbre [4].

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

El dimensionamiento por cobertura parte de modelos de propagación como los tratados en la Parte 1. Para interiores, una referencia muy usada es **ITU-R P.1238** [5]. Una forma habitual del modelo es:

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

**WEP (Wired Equivalent Privacy)** pretendía ofrecer a la red inalámbrica una seguridad “equivalente” a la de una LAN cableada, pero resultó criptográficamente débil [6]. Usaba el cifrador RC4 con un vector de inicialización (IV) de solo **24 bits**, demasiado corto para redes con tráfico elevado.

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

**WPA3-Personal** sustituye el clásico intercambio basado en PSK por **SAE**, derivado del protocolo **Dragonfly** [8]. Esto es importante por tres razones:

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

**Enhanced Open** usa **OWE (Opportunistic Wireless Encryption)** [9]. La idea es proporcionar cifrado individual en redes abiertas, incluso sin autenticación previa compartida. OWE emplea un intercambio tipo Diffie–Hellman. En forma simplificada:

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

**Interpretación:** si se derivan claves distintas por enlace, se limita el impacto de errores o exposiciones puntuales en uno de ellos. No obstante, la superficie de ataque total aumenta porque hay más estados, más contadores, más sincronización y más posibilidades de inconsistencia [2], [3].

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

El ataque **KRACK** explotó la reinstalación de claves en WPA2 bajo ciertas implementaciones [7]. El problema fundamental era que repetir una clave/transmisión podía llevar a reutilizar nonces. Si se reutiliza el mismo flujo de clave en cifrado tipo *stream* o contador, ocurre algo muy peligroso:

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

La frontera entre WLAN y red celular es cada vez menos rígida. En vez de pensar “WiFi o 5G”, el futuro apunta a “WiFi y 5G/6G como recursos coordinados” [12], [13].

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

ATSSS permite dirigir, conmutar o dividir tráfico entre múltiples accesos, típicamente WiFi y 5G [13]. Si un flujo puede enviarse por ambos accesos en paralelo, el caudal útil agregado ideal sería:

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

**WiFi Sensing**, asociado a **IEEE 802.11bf**, aprovecha que la señal de radio “ilumina” el entorno. Cuando una persona se mueve, respira o gesticula, altera ligeramente la propagación, y esa alteración puede medirse mediante **CSI (Channel State Information)** [11].

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

La complejidad creciente de WiFi hace atractiva la incorporación de **IA/ML** para canalización, roaming, balance de carga y planificación dinámica [14].

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

---

## Referencias

[1] IEEE Computer Society, "IEEE Standard for Information Technology—Telecommunications and Information Exchange between Systems—Local and Metropolitan Area Networks—Specific Requirements—Part 11: Wireless LAN Medium Access Control (MAC) and Physical Layer (PHY) Specifications," *IEEE Std 802.11-2020*, Feb. 2021. DOI: [10.1109/IEEESTD.2021.9363693](https://doi.org/10.1109/IEEESTD.2021.9363693)

[2] E. Khorov, I. Levitsky, and A. Kiryanov, "IEEE 802.11be: Wi-Fi 7 Strikes Back," *IEEE Communications Standards Magazine*, vol. 4, no. 3, pp. 40–47, 2020. DOI: [10.1109/MCOMSTD.001.2000014](https://doi.org/10.1109/MCOMSTD.001.2000014)

[3] J. Li, X. Peng, Z. Liu, and Y. Wang, "Multi-link Operation in Wi-Fi 7: Overview and Performance," *IEEE Communications Standards Magazine*, vol. 7, no. 2, pp. 43–49, 2023. DOI: [10.1109/MCOMSTD.001.2200019](https://doi.org/10.1109/MCOMSTD.001.2200019)

[4] E. Khorov, A. Kiryanov, A. Krasilov, G. Bianchi, and Y. Shi, "IEEE 802.11bn: Ultra High Reliability in Next-Generation Wi-Fi," *IEEE Communications Standards Magazine*, vol. 8, no. 1, pp. 58–64, 2024. DOI: [10.1109/MCOMSTD.2024.3343936](https://doi.org/10.1109/MCOMSTD.2024.3343936)

[5] ITU-R, "Propagation data and prediction methods for the planning of indoor radiocommunication systems and radio local area networks in the frequency range 900 MHz to 100 GHz," *Recommendation ITU-R P.1238-11*, Sep. 2022. Disponible en: [https://www.itu.int/rec/R-REC-P.1238](https://www.itu.int/rec/R-REC-P.1238)

[6] N. Borisov, I. Goldberg, and D. Wagner, "Intercepting Mobile Communications: The Insecurity of 802.11," in *Proceedings of the 7th Annual International Conference on Mobile Computing and Networking (MobiCom '01)*, pp. 180–189, 2001. DOI: [10.1145/381677.381695](https://doi.org/10.1145/381677.381695)

[7] M. Vanhoef and F. Piessens, "Key Reinstallation Attacks: Forcing Nonce Reuse in WPA2," in *Proceedings of the 24th ACM SIGSAC Conference on Computer and Communications Security*, pp. 1313–1328, 2017. DOI: [10.1145/3133956.3134027](https://doi.org/10.1145/3133956.3134027)

[8] D. Harkins, "Dragonfly Key Exchange," RFC 7664, RFC Editor, Oct. 2015. DOI: [10.17487/RFC7664](https://doi.org/10.17487/RFC7664)

[9] D. Harkins and W. Kumari, "Opportunistic Wireless Encryption," RFC 8110, RFC Editor, Mar. 2017. DOI: [10.17487/RFC8110](https://doi.org/10.17487/RFC8110)

[10] Wi-Fi Alliance, *Wi-Fi CERTIFIED WPA3™ Specification*, 2020. Disponible en: [https://www.wi-fi.org/](https://www.wi-fi.org/)

[11] J. Zhang, Y. Xiao, S. Chen, J. Choi, and P. Fan, "IEEE 802.11bf: Toward Wi-Fi Sensing—Current Status and Directions for IoT Applications," *IEEE Internet of Things Journal*, vol. 9, no. 1, pp. 716–732, 2022. DOI: [10.1109/JIOT.2021.3103215](https://doi.org/10.1109/JIOT.2021.3103215)

[12] M. Y. Alias, N. M. Din, N. Fisal, and N. F. Abdullah, "Converged 5G and Wi-Fi Networks: Opportunities and Challenges," *IEEE Access*, vol. 9, pp. 29641–29659, 2021. DOI: [10.1109/ACCESS.2021.3058482](https://doi.org/10.1109/ACCESS.2021.3058482)

[13] T. Paavola, F. Mir, M. Serror, C. Caba, E. Seidel, and J. Torsner, "Transport Protocol Considerations for ATSSS Services in 5G," *IEEE Communications Standards Magazine*, vol. 6, no. 3, pp. 62–68, 2022. DOI: [10.1109/MCOMSTD.001.2100005](https://doi.org/10.1109/MCOMSTD.001.2100005)

[14] D. Atzeni, D. Bacciu, D. Mazzei, and G. Prencipe, "A Systematic Review of Wi-Fi and Machine Learning Integration with Topic Modeling Techniques," *Sensors*, vol. 22, no. 13, 4925, 2022. DOI: [10.3390/s22134925](https://doi.org/10.3390/s22134925)

[15] G. V. Frangulea, P. Assimakopoulos, B. Bojović, and S. Lagén, "NR-U and Wi-Fi Coexistence in sub-7 GHz bands: Implementation and Evaluation of NR-U Type 1 Channel Access in ns-3," in *2024 Workshop on ns-3 (WNS3 2024)*, 2024. DOI: [10.1145/3659111.3659114](https://doi.org/10.1145/3659111.3659114)

[16] D. López-Pérez, A. Garcia-Rodriguez, L. Galati-Giordano, M. Kasslin, and K. Doppler, "IEEE 802.11be Extremely High Throughput: The Next Generation of Wi-Fi Technology Beyond 802.11ax," *IEEE Communications Magazine*, vol. 57, no. 9, pp. 113–119, 2019. DOI: [10.1109/MCOM.001.1900338](https://doi.org/10.1109/MCOM.001.1900338)
