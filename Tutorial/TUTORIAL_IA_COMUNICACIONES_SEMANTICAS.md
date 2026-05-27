# TUTORIAL: De las Neuronas Artificiales a las Comunicaciones Semánticas
## Una Guía Pedagógica Integral sobre Inteligencia Artificial Aplicada a las Comunicaciones Inalámbricas

---

**Autores:** Tutorial generado con asistencia de IA  
**Fecha:** Mayo 2026  
**Versión:** 1.0

---

## Tabla de Contenidos

- **Sección 1: Introducción y Fundamentos de las Neuronas Artificiales**
  - 1.1 Introducción al tutorial
  - 1.2 La neurona biológica y la neurona artificial
    - 1.2.1 La neurona biológica
    - 1.2.2 La neurona artificial: el modelo de McCulloch-Pitts y sus extensiones
  - 1.3 El Perceptrón simple
    - 1.3.1 Definición y modelo matemático
    - 1.3.2 Interpretación geométrica: la frontera de decisión como un hiperplano
    - 1.3.3 Ejemplo: implementación de la compuerta OR
  - 1.4 Funciones de activación
    - 1.4.1 Función escalón (Heaviside)
    - 1.4.2 Función sigmoide (logística)
    - 1.4.3 Tangente hiperbólica (tanh)
    - 1.4.4 Unidad Lineal Rectificada (ReLU)
    - 1.4.5 Variantes de ReLU
    - 1.4.6 Función Softmax para clasificación multi-clase
    - 1.4.7 Descripción de figura: funciones de activación
  - 1.5 Aprendizaje y la regla de actualización de pesos
    - 1.5.1 El concepto de aprendizaje en redes neuronales
    - 1.5.2 Descenso de gradiente: intuición geométrica
    - 1.5.3 Tasa de aprendizaje y regla de actualización
    - 1.5.4 Funciones de pérdida
    - 1.5.5 Ejemplo completo: entrenamiento de un perceptrón para la compuerta AND
    - 1.5.6 Resumen y conexión con las secciones posteriores
- **2. El Perceptrón Multicapa (MLP)**
  - 2.1 Arquitectura del MLP
    - 2.1.1 Estructura general
    - 2.1.2 Capas totalmente conectadas (densas)
    - 2.1.3 Notación formal
    - 2.1.4 Propagación hacia adelante (*Forward Pass*)
    - 2.1.5 Diagrama de un MLP de tres capas
    - 2.1.6 Ejemplo numérico detallado
  - 2.2 Retropropagación del error (*Backpropagation*)
    - 2.2.1 Motivación y contexto histórico
    - 2.2.2 La regla de la cadena en detalle
    - 2.2.3 Cálculo de los deltas
    - 2.2.4 Gradientes de los pesos y sesgos
    - 2.2.5 Algoritmo completo de retropropagación
    - 2.2.6 Ejemplo numérico completo de retropropagación
    - 2.2.7 Diagrama del flujo de gradientes
  - 2.3 Funciones de pérdida
    - 2.3.1 Error cuadrático medio (MSE)
    - 2.3.2 Entropía cruzada binaria (BCE)
    - 2.3.3 Entropía cruzada categórica
    - 2.3.4 Criterios de selección
  - 2.4 Optimizadores
    - 2.4.1 Descenso de gradiente estocástico (SGD)
    - 2.4.2 SGD con momento (*momentum*)
    - 2.4.3 Adam (*Adaptive Moment Estimation*)
    - 2.4.4 Programación de la tasa de aprendizaje (*Learning Rate Scheduling*)
  - 2.5 Regularización
    - 2.5.1 Sobreajuste vs. subajuste
    - 2.5.2 Regularización L1 (*Lasso*)
    - 2.5.3 Regularización L2 (*Ridge* o *Weight Decay*)
    - 2.5.4 Dropout
    - 2.5.5 Normalización por lotes (*Batch Normalization*)
  - 2.6 Ejemplo práctico: Clasificación con MLP
    - 2.6.1 Planteamiento del problema
    - 2.6.2 Implementación en PyTorch
- **============================================================**
- **1. Generar datos sintéticos**
- **============================================================**
- **Fijamos la semilla para reproducibilidad**
- **Generamos 1000 muestras con 2 características**
- **Característica 1: ingreso mensual normalizado (media 0, std 1)**
- **Característica 2: puntuación crediticia normalizada**
- **Regla de decisión: aprobado si 0.5*x1 + 0.8*x2 + ruido > 0**
- **Esto crea una frontera de decisión lineal con algo de ruido**
- **Convertir a tensores de PyTorch**
- **Dividir en conjuntos de entrenamiento (80%) y prueba (20%)**
- **Crear DataLoaders para iterar sobre mini-batches**
- **TensorDataset agrupa las características y etiquetas**
- **DataLoader gestiona la iteración por mini-batches y el mezclado**
- **============================================================**
- **2. Definir la arquitectura del MLP**
- **============================================================**
- **Instanciar el modelo**
- **Verificar la arquitectura**
- **Contar el número total de parámetros**
- **============================================================**
- **3. Definir la función de pérdida y el optimizador**
- **============================================================**
- **Entropía cruzada binaria (BCE)**
- **Mide la discrepancia entre la distribución predicha y la real**
- **Optimizador Adam con tasa de aprendizaje 0.001**
- **y regularización L2 (weight_decay) con lambda = 1e-4**
- **Programador de tasa de aprendizaje: reduce lr al 50%**
- **si la pérdida no mejora en 5 épocas**
- **============================================================**
- **4. Bucle de entrenamiento**
- **============================================================**
- **============================================================**
- **5. Evaluación final**
- **============================================================**
    - 2.6.3 Explicación del bucle de entrenamiento
    - 2.6.4 Análisis de los resultados
    - 2.6.5 Conexión con comunicaciones semánticas
- **3. Redes Neuronales Convolucionales (CNN)**
  - 3.1 Motivación y concepto de convolución
    - 3.1.1 La explosión de parámetros en redes totalmente conectadas
    - 3.1.2 Definición matemática de la convolución continua
    - 3.1.3 La convolución discreta
    - 3.1.4 Principios fundamentales: campos receptivos locales, compartición de pesos e invarianza a traslaciones
  - 3.2 Capas convolucionales
    - 3.2.1 Convolución 2D para imágenes
    - 3.2.2 Parámetros de la convolución: tamaño del kernel, stride y padding
    - 3.2.3 Fórmula del tamaño de salida
    - 3.2.4 Mapas de características y filtros múltiples
    - 3.2.5 Ejemplo numérico: detección de bordes con un filtro 3×3
  - 3.3 Capas de Pooling
    - 3.3.1 Max Pooling
    - 3.3.2 Average Pooling
    - 3.3.3 Propósito y ventajas del pooling
    - 3.3.4 Ejemplo numérico de pooling
  - 3.4 Arquitectura completa de una CNN
    - 3.4.1 Pipeline estándar
    - 3.4.2 Arquitecturas clásicas
  - 3.5 Convolución 1D para señales de telecomunicaciones
    - 3.5.1 De 2D a 1D: adaptando las CNN para señales
    - 3.5.2 Procesamiento de señales de radiofrecuencia (RF)
    - 3.5.3 Filtros para patrones en señales de comunicación
  - 3.6 Caso práctico: Clasificación Automática de Modulación (AMC)
    - 3.6.1 Descripción del problema
    - 3.6.2 Arquitectura CNN para AMC
    - 3.6.3 Implementación en PyTorch
- **============================================================**
- **Definición de la arquitectura CNN para clasificación de modulación**
- **============================================================**
- **============================================================**
- **Configuración del entrenamiento**
- **============================================================**
- **Hiperparámetros**
- **Simulación de datos de ejemplo (en la práctica, se usaría un dataset**
- **real como RadioML 2016.10A o RadioML 2018.01A)**
- **X_train: (N, 1, 2, 128) - N señales, 1 canal, 2 filas I/Q, 128 muestras**
- **y_train: (N,) - etiquetas de modulación (enteros 0 a num_classes-1)**
- **Crear DataLoader para iteración eficiente por lotes**
- **Instanciar el modelo**
- **Función de pérdida: entropía cruzada (incluye softmax internamente)**
- **Es la elección estándar para clasificación multiclase.**
- **Optimizador: Adam (combina momento y tasas de aprendizaje adaptativas)**
- **============================================================**
- **Bucle de entrenamiento**
- **============================================================**
- **============================================================**
- **Inferencia (clasificación de nuevas señales)**
- **============================================================**
  - 3.7 Autoencoders convolucionales para detección de anomalías
    - 3.7.1 Concepto de autoencoder
    - 3.7.2 Función de pérdida: error de reconstrucción
    - 3.7.3 Entrenamiento con datos "normales" y detección de anomalías
    - 3.7.4 Aplicación: detección de señales anómalas en telecomunicaciones
    - Resumen de la Sección 3
- **4. Redes Neuronales Recurrentes (RNN) y LSTM**
  - 4.1 Motivación: procesamiento de secuencias
    - 4.1.1 Por qué los MLP y las CNN son insuficientes para datos secuenciales
    - 4.1.2 Datos donde el orden importa
    - 4.1.3 El concepto de memoria en redes neuronales
  - 4.2 La Red Neuronal Recurrente (RNN) básica
    - 4.2.1 Arquitectura: el estado oculto que se retroalimenta
    - 4.2.2 Formulación matemática
    - 4.2.3 Despliegue de la RNN en el tiempo
    - 4.2.4 Retropropagación a través del tiempo (BPTT)
    - 4.2.5 El problema del gradiente desvaneciente
  - 4.3 Long Short-Term Memory (LSTM)
    - 4.3.1 Motivación: resolver el problema del gradiente desvaneciente
    - 4.3.2 El estado de celda como "cinta transportadora"
    - 4.3.3 Las tres puertas: formulación matemática completa
      - Puerta de olvido (*Forget Gate*)
      - Puerta de entrada (*Input Gate*) y celda candidata
      - Actualización del estado de celda
      - Puerta de salida (*Output Gate*) y estado oculto
    - 4.3.4 Recuento de parámetros
    - 4.3.5 Ejemplo numérico detallado
    - 4.3.6 Análisis del flujo de gradientes en la LSTM
  - 4.4 Gated Recurrent Unit (GRU)
    - 4.4.1 Una versión simplificada de la LSTM
    - 4.4.2 Formulación matemática
    - 4.4.3 Comparación entre GRU y LSTM
  - 4.5 Arquitecturas bidireccionales y apiladas
    - 4.5.1 RNN/LSTM bidireccionales
    - 4.5.2 Capas recurrentes apiladas (Deep RNN)
    - 4.5.3 Aplicaciones en NLP y procesamiento de señales
  - 4.6 Limitaciones de las RNN/LSTM frente a los Transformers
    - 4.6.1 Procesamiento secuencial: imposibilidad de paralelizar
    - 4.6.2 Ventana de contexto limitada en la práctica
    - 4.6.3 Dificultad con secuencias muy largas
    - 4.6.4 Hacia la arquitectura Transformer
  - 4.7 Ejemplo práctico: Predicción de series temporales
    - 4.7.1 Descripción del problema
    - 4.7.2 Implementación en PyTorch
- **============================================================**
- **1. Generación de datos sintéticos**
- **============================================================**
- **Simulamos una señal que podría representar variaciones**
- **temporales de un canal inalámbrico: una combinación de**
- **sinusoides con ruido gaussiano aditivo.**
- **Señal compuesta: dos sinusoides + ruido**
- **Normalizar la señal al rango [-1, 1] para facilitar**
- **el entrenamiento con activaciones tanh**
- **============================================================**
- **2. Preparación de datos: ventanas deslizantes**
- **============================================================**
- **Creamos pares (entrada, objetivo) usando una ventana**
- **deslizante: la entrada son los L pasos anteriores y**
- **el objetivo es el siguiente valor.**
- **División en conjuntos de entrenamiento y prueba (80/20)**
- **Convertir a tensores de PyTorch**
- **LSTM espera entrada con forma (batch, seq_len, input_size)**
- **============================================================**
- **3. Definición del modelo LSTM**
- **============================================================**
- **============================================================**
- **4. Configuración del entrenamiento**
- **============================================================**
- **Hiperparámetros**
- **Instanciar modelo, función de pérdida y optimizador**
- **Contar parámetros totales**
- **Crear DataLoaders para iterar por mini-batches**
- **============================================================**
- **5. Bucle de entrenamiento**
- **============================================================**
- **============================================================**
- **6. Evaluación y visualización**
- **============================================================**
- **Calcular métricas de rendimiento**
- **Gráfica 1: Curvas de pérdida durante el entrenamiento**
- **Gráfica 2: Predicciones vs valores reales**
- **Gráfica 3: Error de predicción**
    - 4.7.3 Análisis del código
    - 4.7.4 Extensiones para comunicaciones semánticas
  - Referencias
- **5. Mecanismos de Atención**
  - 5.1 Motivación: el cuello de botella de la información
    - 5.1.1 El problema fundamental de los modelos seq2seq
    - 5.1.2 El cuello de botella informacional
    - 5.1.3 La intuición detrás de la atención
    - 5.1.4 Relevancia para las comunicaciones semánticas
  - 5.2 Atención de Bahdanau (Atención Aditiva)
    - 5.2.1 Contexto histórico
    - 5.2.2 Arquitectura del codificador bidireccional
    - 5.2.3 El mecanismo de alineación (scoring)
    - 5.2.4 Pesos de atención
    - 5.2.5 Vector de contexto dinámico
    - 5.2.6 Integración con el decodificador
    - 5.2.7 Visualización del mecanismo
    - 5.2.8 Complejidad computacional
  - 5.3 Atención de Luong (Atención Multiplicativa)
    - 5.3.1 Motivación y contexto
    - 5.3.2 Funciones de puntuación
    - 5.3.3 Diferencias clave con la atención de Bahdanau
    - 5.3.4 Eficiencia computacional
  - 5.4 Self-Attention (Auto-Atención)
    - 5.4.1 De la atención cruzada a la auto-atención
    - 5.4.2 Queries, Keys y Values
    - 5.4.3 La analogía de la biblioteca
    - 5.4.4 Scaled Dot-Product Attention
    - 5.4.5 Propiedades fundamentales de la auto-atención
  - 5.5 Ejemplo detallado paso a paso
    - 5.5.1 Configuración del ejemplo
    - 5.5.2 Definición de las matrices de proyección
    - 5.5.3 Cálculo de Q, K, V
    - 5.5.4 Cálculo de $\mathbf{Q}\mathbf{K}^T$
    - 5.5.5 Escalamiento por $\sqrt{d_k}$
    - 5.5.6 Aplicación de softmax
    - 5.5.7 Cálculo de la salida $\boldsymbol{\alpha}\mathbf{V}$
    - 5.5.8 Interpretación de los resultados
  - 5.6 Multi-Head Attention (Atención Multi-Cabeza)
    - 5.6.1 Limitaciones de una sola cabeza de atención
    - 5.6.2 Formulación matemática
    - 5.6.3 Desglose dimensional
    - 5.6.4 Intuición: ¿por qué múltiples cabezas?
    - 5.6.5 Análisis de parámetros
    - 5.6.6 Complejidad computacional
  - 5.7 Implementación en PyTorch
    - 5.7.1 Implementación de Scaled Dot-Product Attention
    - 5.7.2 Implementación de Multi-Head Attention
    - 5.7.3 Ejemplo de uso y verificación
- **Crear máscara causal para decodificadores autoregresivos**
    - 5.7.4 Notas de implementación
  - Referencias
- **6. La Arquitectura Transformer**
  - 6.1 Contexto histórico y motivación
    - 6.1.1 Limitaciones de las arquitecturas recurrentes
    - 6.1.2 El artículo "Attention Is All You Need"
  - 6.2 Codificación posicional (*Positional Encoding*)
    - 6.2.1 La necesidad de codificar posiciones
    - 6.2.2 Codificación sinusoidal
    - 6.2.3 Propiedad de posiciones relativas
    - 6.2.4 Ejemplo numérico
    - 6.2.5 Codificaciones posicionales aprendidas
  - 6.3 El bloque Encoder del Transformer
    - 6.3.1 Visión general de la arquitectura del encoder
    - 6.3.2 Embedding de entrada y codificación posicional
    - 6.3.3 Multi-Head Self-Attention
    - 6.3.4 Conexiones residuales
    - 6.3.5 Normalización de capa (*Layer Normalization*)
    - 6.3.6 Red Feed-Forward posición por posición
    - 6.3.7 Estructura completa de un bloque encoder
  - 6.4 El bloque Decoder del Transformer
    - 6.4.1 Estructura del decoder
    - 6.4.2 Máscara causal (*Causal Mask*)
    - 6.4.3 Atención Encoder-Decoder (*Cross-Attention*)
    - 6.4.4 Feed-Forward Network del decoder
  - 6.5 La arquitectura completa Encoder-Decoder
    - 6.5.1 Pipeline completo
    - 6.5.2 Parámetros del modelo base
    - 6.5.3 Complejidad computacional
  - 6.6 Entrenamiento del Transformer
    - 6.6.1 Teacher Forcing
    - 6.6.2 Función de pérdida: Entropía cruzada
    - 6.6.3 Suavizado de etiquetas (*Label Smoothing*)
    - 6.6.4 Esquema de tasa de aprendizaje con calentamiento (*Warm-up*)
    - 6.6.5 Regularización
  - 6.7 Variantes de Transformers
    - 6.7.1 Modelos solo-encoder: BERT
    - 6.7.2 Modelos solo-decoder: GPT
    - 6.7.3 Modelos Encoder-Decoder: T5
    - 6.7.4 Vision Transformer (ViT)
    - 6.7.5 Resumen comparativo
  - 6.8 Implementación en PyTorch
    - 6.8.1 Codificación posicional
    - 6.8.2 Bloque Transformer (Encoder)
    - 6.8.3 Apilamiento de bloques: Encoder completo
    - 6.8.4 Bloque Decoder
    - 6.8.5 Generación de la máscara causal
    - 6.8.6 Modelo Transformer completo
- **Instanciar modelo con hiperparámetros del Transformer base**
- **Verificar número de parámetros**
  - 6.9 Ejemplo: Transformer para traducción
    - 6.9.1 Descripción conceptual del proceso
    - 6.9.2 Procesamiento en el encoder
    - 6.9.3 Generación en el decoder (inferencia)
    - 6.9.4 Diferencia entre entrenamiento e inferencia
    - 6.9.5 Relevancia para comunicaciones semánticas
    - Resumen de la Sección 6
- **7. Fundamentos de las Comunicaciones Semánticas**
  - 7.1 Del modelo de Shannon a la comunicación semántica
    - 7.1.1 La teoría matemática de la comunicación de Shannon (1948)
    - 7.1.2 Los tres niveles de comunicación de Weaver (1949)
    - 7.1.3 El "efecto precipicio" y las limitaciones del paradigma clásico
    - 7.1.4 El cambio de paradigma: transmitir significado, no bits
  - 7.2 ¿Qué es la "semántica" en comunicaciones?
    - 7.2.1 Información semántica versus información sintáctica
    - 7.2.2 Ejemplo ilustrativo: transmisión de una imagen
    - 7.2.3 Comunicaciones orientadas a tareas
    - 7.2.4 Entropía semántica e información mutua semántica
  - 7.3 Arquitectura general de un sistema de comunicación semántica
    - 7.3.1 Codificación conjunta de fuente y canal (JSCC)
    - 7.3.2 Aprendizaje de extremo a extremo (E2E)
    - 7.3.3 Componentes del sistema
  - 7.4 El papel de los Transformers en las comunicaciones semánticas
    - 7.4.1 ¿Por qué los Transformers son ideales para la extracción semántica?
    - 7.4.2 DeepSC: Comunicación semántica basada en Transformers para texto
    - 7.4.3 Los pesos de atención como codificación de importancia semántica
    - 7.4.4 El "vector de atención" como representación semántica
  - 7.5 Ventajas de las comunicaciones semánticas
    - 7.5.1 Eficiencia en el uso del ancho de banda
    - 7.5.2 Degradación gradual versus efecto precipicio
    - 7.5.3 Robustez al ruido del canal
    - 7.5.4 Orientación a la tarea
    - 7.5.5 Compatibilidad con la visión de 6G
  - 7.6 Métricas de evaluación semántica
    - 7.6.1 Métricas tradicionales (sintácticas)
    - 7.6.2 Métricas semánticas
    - 7.6.3 Comparación entre métricas clásicas y semánticas
  - 7.7 Ejemplo conceptual: transmisión semántica de texto
    - 7.7.1 Descripción del ejemplo paso a paso
    - 7.7.2 Pseudocódigo en PyTorch
- **============================================================**
- **Componentes del sistema de comunicación semántica**
- **============================================================**
- **============================================================**
- **Sistema completo de comunicación semántica**
- **============================================================**
- **============================================================**
- **Ejemplo de uso: entrenamiento y evaluación**
- **============================================================**
- **--- Simulación conceptual ---**
    - 7.7.3 Análisis del ejemplo
  - Referencias
- **8. Sistemas de Comunicación Semántica de Extremo a Extremo (E2E)**
  - 8.1 Arquitectura E2E: Encoder Semántico-Canal (Transmisor)
    - 8.1.1 Visión general del transmisor semántico
    - 8.1.2 El encoder semántico
    - 8.1.3 El encoder de canal
    - 8.1.4 Diseño conjunto y formulación compuesta
    - 8.1.5 Normalización de potencia
    - 8.1.6 La razón de codificación $k/n$
    - 8.1.7 Diagrama del transmisor
  - 8.2 El Canal Físico como Capa Diferenciable
    - 8.2.1 Motivación: el canal como capa de la red neuronal
    - 8.2.2 Canal AWGN (Ruido Gaussiano Blanco Aditivo)
    - 8.2.3 Canal con desvanecimiento Rayleigh
    - 8.2.4 Canal con desvanecimiento Riciano
    - 8.2.5 Relación señal a ruido (SNR)
    - 8.2.6 Requisito de diferenciabilidad para la retropropagación
    - 8.2.7 El truco de reparametrización para canales estocásticos
    - 8.2.8 Visualización del efecto del canal
  - 8.3 El Decoder Semántico-Canal (Receptor)
    - 8.3.1 Estructura general del receptor
    - 8.3.2 El decoder de canal
    - 8.3.3 El decoder semántico
    - 8.3.4 Formulación completa del receptor
  - 8.4 Funciones de Pérdida para Comunicaciones Semánticas
    - 8.4.1 El papel central de la función de pérdida
    - 8.4.2 Funciones de pérdida para transmisión de texto
    - 8.4.3 Funciones de pérdida para transmisión de imágenes
    - 8.4.4 Función de pérdida combinada
  - 8.5 Proceso de Entrenamiento E2E Paso a Paso
    - 8.5.1 Visión general del entrenamiento
    - 8.5.2 Paso 1: Propagación hacia adelante (*Forward Pass*)
    - 8.5.3 Paso 2: Cálculo de la pérdida
    - 8.5.4 Paso 3: Retropropagación (*Backpropagation*)
    - 8.5.5 Paso 4: Actualización de parámetros
    - 8.5.6 Entrenamiento con currículo de SNR
    - 8.5.7 Diagrama del proceso de entrenamiento
  - 8.6 Conversión de Señales Multimedia a Representación Semántica
    - 8.6.1 El desafío de la representación universal
    - 8.6.2 Audio y voz: de la onda acústica a tokens semánticos
    - 8.6.3 Video: de fotogramas a representación espacio-temporal
    - 8.6.4 Texto: tokenización y embeddings
    - 8.6.5 El puente de la tokenización: de señales continuas a unidades semánticas discretas
    - 8.6.6 Superioridad sobre la codificación de fuente tradicional
  - 8.7 Degradación Suave vs. Efecto Acantilado
    - 8.7.1 El efecto acantilado en los sistemas clásicos
    - 8.7.2 Degradación suave en los sistemas semánticos
    - 8.7.3 Análisis matemático comparativo
    - 8.7.4 Implicaciones prácticas
    - 8.7.5 Diagrama comparativo
  - 8.8 Implementación Completa en PyTorch
    - 8.8.1 Descripción del sistema implementado
- **===========================================================**
- **SISTEMA DE COMUNICACIÓN SEMÁNTICA E2E EN PYTORCH**
- **Basado en la arquitectura DeepSC para transmisión de texto**
- **===========================================================**
- **===========================================================**
- **FUNCIONES DE ENTRENAMIENTO**
- **===========================================================**
- **===========================================================**
- **EJEMPLO DE USO**
- **===========================================================**
    - 8.8.2 Explicación detallada de los componentes del código
  - 8.9 Resumen y Conexiones
    - Referencias
- **9. Temas Avanzados en Comunicaciones Semánticas**
  - 9.1 Conformación de formas de onda semánticas
    - 9.1.1 Diseño tradicional de formas de onda
    - 9.1.2 Formas de onda aprendidas: el codificador de canal como conformador
    - 9.1.3 Densidad espectral de potencia y restricciones regulatorias
    - 9.1.4 Constelaciones aprendidas vs. constelaciones tradicionales
  - 9.2 Comunicaciones semánticas para MIMO masivo
    - 9.2.1 Modelo del sistema MIMO
    - 9.2.2 Precodificación en sistemas semánticos
    - 9.2.3 Conformación de haz (*beamforming*) integrada con codificación semántica
    - 9.2.4 Convergencia de características semánticas entre antenas
  - 9.3 Comunicaciones semánticas en bandas milimétricas (mmWave) y THz
    - 9.3.1 Desafíos en altas frecuencias
    - 9.3.2 Valor de las comunicaciones semánticas en mmWave/THz
    - 9.3.3 Modulación OTFS para canales de alta movilidad
    - 9.3.4 Integración de OTFS con codificación semántica
  - 9.4 Sensing semántico: ISAC (Integrated Sensing and Communications)
    - 9.4.1 Comunicaciones y sensado integrado
    - 9.4.2 Sensado semántico: extracción de información del canal
    - 9.4.3 Sección transversal de radar y extracción de características semánticas
    - 9.4.4 Función dual: comunicar y sensar simultáneamente
  - 9.5 Modelos fundacionales multimodales para comunicaciones semánticas
    - 9.5.1 Modelos preentrenados como columna vertebral semántica
    - 9.5.2 Aprendizaje por transferencia para tareas de comunicación
    - 9.5.3 Comunicación semántica multimodal
    - 9.5.4 La base de conocimiento (KB) compartida
    - 9.5.5 Comunicación semántica basada en ontologías
  - 9.6 Aprendizaje federado para comunicaciones semánticas
    - 9.6.1 Entrenamiento distribuido con preservación de privacidad
    - 9.6.2 Formulación del aprendizaje federado
    - 9.6.3 Codificación semántica local y agregación en el servidor
    - 9.6.4 Modelos semánticos adaptativos que aprenden de condiciones de red
    - 9.6.5 Detección de deriva semántica y actualización de modelos
  - 9.7 El plano de control semántico
    - 9.7.1 La cabecera semántica
    - 9.7.2 Modificaciones al modelo OSI para comunicaciones semánticas
    - 9.7.3 Pila de protocolos semántica
    - 9.7.4 Calidad de experiencia (QoE) vs. calidad de servicio (QoS)
    - 9.7.5 Deriva semántica: detección y resincronización
  - 9.8 Perspectivas futuras y 6G
    - 9.8.1 Comunicación semántica como pilar de 6G
    - 9.8.2 IA nativa en la interfaz aérea
    - 9.8.3 Comunicación orientada a objetivos (*goal-oriented communication*)
    - 9.8.4 Seguridad y privacidad semántica
    - 9.8.5 Desafíos de estandarización
    - 9.8.6 Problemas abiertos de investigación
    - Referencias de la Sección 9
- **10. Conclusiones, Glosario y Referencias**
  - 10.1 Conclusiones y recapitulación
    - 10.1.1 Resumen del recorrido tutorial
    - 10.1.2 Lecciones clave del tutorial
    - 10.1.3 El camino hacia adelante: 6G y más allá
    - 10.1.4 Reflexión final: la convergencia de la IA y las comunicaciones
  - 10.2 Apéndice matemático
    - 10.2.1 Álgebra lineal
    - 10.2.2 Cálculo diferencial
    - 10.2.3 Probabilidad y estadística
    - 10.2.4 Teoría de la información
    - 10.2.5 La función Softmax: propiedades y estabilidad numérica
    - 10.2.6 Cálculo matricial: Jacobianos en la retropropagación
  - 10.3 Glosario de términos
  - 10.4 Referencias bibliográficas
    - Fundamentos de redes neuronales
    - Mecanismos de atención y Transformers
    - Comunicaciones semánticas
    - Aprendizaje profundo para comunicaciones
    - Teoría de la información y comunicaciones
    - Aprendizaje profundo — textos generales

---

# Sección 1: Introducción y Fundamentos de las Neuronas Artificiales

---

## 1.1 Introducción al tutorial

Las comunicaciones semánticas representan un cambio de paradigma en la ingeniería de telecomunicaciones. Mientras que los sistemas de comunicación convencionales —desde los trabajos fundacionales de Claude Shannon en 1948— se han enfocado en transmitir bits de forma confiable a través de un canal ruidoso, las comunicaciones semánticas buscan transmitir el *significado* de la información, priorizando la relevancia y la interpretación del mensaje en el receptor por encima de la reproducción exacta de cada símbolo transmitido. Este enfoque, anticipado conceptualmente por Warren Weaver en su célebre artículo conjunto con Shannon, ha cobrado nueva relevancia gracias a los avances extraordinarios de la inteligencia artificial (IA), y en particular del aprendizaje profundo (*deep learning*), que proporcionan las herramientas matemáticas y computacionales necesarias para extraer, codificar y reconstruir el contenido semántico de señales complejas como texto, voz, imágenes y video.

El presente tutorial tiene como objetivo ofrecer una guía completa, rigurosa y autocontenida que permita al lector —ya sea estudiante de posgrado, investigador o ingeniero profesional en telecomunicaciones— comprender los fundamentos de la inteligencia artificial que sustentan las comunicaciones semánticas modernas. El recorrido comienza aquí, en esta primera sección, con los bloques de construcción más elementales: la neurona artificial y el perceptrón. A partir de estos conceptos básicos, las secciones posteriores del tutorial irán construyendo, de manera progresiva, las arquitecturas más sofisticadas que habilitan los sistemas de comunicación semántica de vanguardia: redes neuronales profundas, redes convolucionales (CNN), redes recurrentes (RNN y LSTM), mecanismos de atención, transformers, autoencoders variacionales (VAE), redes generativas adversarias (GAN) y, finalmente, su integración en esquemas de codificación y decodificación conjunta de fuente y canal (*Joint Source-Channel Coding*, JSCC).

La motivación de este tutorial es doble. Por un lado, existe una brecha significativa entre la literatura de aprendizaje automático —frecuentemente orientada a la visión por computadora o el procesamiento de lenguaje natural— y las necesidades específicas de la comunidad de telecomunicaciones. Muchos textos asumen familiaridad con conceptos de IA que no forman parte de la formación tradicional de un ingeniero de comunicaciones. Por otro lado, la literatura emergente sobre comunicaciones semánticas a menudo presupone un dominio de arquitecturas de aprendizaje profundo sin ofrecer las bases necesarias para comprenderlas. Este tutorial busca cerrar ambas brechas, proporcionando un camino pedagógico que parte desde los principios más básicos de las redes neuronales hasta su aplicación concreta en sistemas de comunicación semántica.

A lo largo de todo el tutorial se adoptará un enfoque formal pero accesible: cada concepto se introducirá con intuición geométrica o física, se formalizará mediante ecuaciones matemáticas expresadas con rigor y se ilustrará con ejemplos concretos. Se utilizará notación vectorial y matricial estándar, y todas las ecuaciones se presentarán en formato LaTeX para facilitar su reproducción. No se asumirán conocimientos previos de aprendizaje automático, aunque sí se espera familiaridad con álgebra lineal, cálculo multivariable y probabilidad a nivel de pregrado en ingeniería.

---

## 1.2 La neurona biológica y la neurona artificial

### 1.2.1 La neurona biológica

El cerebro humano está compuesto por aproximadamente $8.6 \times 10^{10}$ neuronas (86 mil millones), interconectadas a través de una red extraordinariamente compleja de conexiones sinápticas cuyo número se estima en el orden de $10^{14}$ a $10^{15}$. Cada neurona biológica es una célula especializada en el procesamiento y la transmisión de señales electroquímicas que, en su conjunto, dan lugar a la cognición, la percepción, el aprendizaje y la memoria. Comprender la estructura y el funcionamiento básico de la neurona biológica resulta fundamental, ya que la neurona artificial se concibió originalmente como una abstracción simplificada de su contraparte natural.

La estructura de una neurona biológica puede describirse mediante tres componentes funcionales principales:

1. **Dendritas:** Son las ramificaciones que se extienden desde el cuerpo celular y actúan como las "antenas receptoras" de la neurona. Las dendritas reciben señales electroquímicas provenientes de otras neuronas a través de las sinapsis. Una neurona típica puede tener miles de conexiones dendríticas, cada una de las cuales recibe una señal con una intensidad (o "peso") diferente, determinada por la eficacia sináptica de cada conexión. Es precisamente esta eficacia sináptica variable la que constituye el sustrato biológico del aprendizaje: cuando una conexión se refuerza (potenciación a largo plazo, LTP) o se debilita (depresión a largo plazo, LTD), la neurona modifica su respuesta ante determinados patrones de entrada.

2. **Soma (cuerpo celular):** El soma es el componente central de la neurona, donde se encuentra el núcleo celular. Desde la perspectiva del procesamiento de información, el soma realiza una función de integración: acumula las señales electroquímicas recibidas a través de las dendritas, sumando tanto las señales excitatorias (que tienden a activar la neurona) como las inhibitorias (que tienden a suprimirla). Si la suma neta de estas señales supera un cierto umbral de activación —conocido como potencial de umbral, típicamente alrededor de $-55$ mV en una neurona humana—, la neurona se "dispara", generando un potencial de acción.

3. **Axón:** Es la prolongación que se extiende desde el soma y se encarga de transmitir el potencial de acción hacia otras neuronas. El axón puede ramificarse en sus terminales (terminales axónicas o botones sinápticos), permitiendo que una sola neurona transmita su señal a miles de neuronas receptoras. La transmisión a lo largo del axón es de naturaleza binaria en cierto sentido: la neurona dispara o no dispara (principio de "todo o nada"), aunque la frecuencia de disparo puede variar, codificando así información de manera analógica a través de un mecanismo digital.

### 1.2.2 La neurona artificial: el modelo de McCulloch-Pitts y sus extensiones

En 1943, Warren McCulloch y Walter Pitts propusieron el primer modelo matemático de una neurona, estableciendo las bases de lo que hoy conocemos como redes neuronales artificiales. Su modelo, aunque extremadamente simplificado respecto a la complejidad biológica real, captura la esencia computacional de una neurona: recibir múltiples entradas, ponderarlas, sumarlas y producir una salida basada en si la suma supera un umbral.

La neurona artificial opera de la siguiente manera:

1. **Entradas ($x_1, x_2, \ldots, x_n$):** Análogas a las señales recibidas por las dendritas, representan los datos o características que alimentan a la neurona. Cada entrada $x_i$ es un valor numérico que puede provenir de los datos originales del problema o de la salida de otra neurona en una capa anterior.

2. **Pesos sinápticos ($w_1, w_2, \ldots, w_n$):** Cada conexión de entrada tiene asociado un peso $w_i \in \mathbb{R}$ que modula la importancia de la señal correspondiente. Los pesos son análogos a la eficacia sináptica en la neurona biológica: un peso grande (en valor absoluto) indica una conexión fuerte, mientras que un peso cercano a cero indica una conexión débil. Los pesos positivos modelan conexiones excitatorias y los pesos negativos, conexiones inhibitorias. El aprendizaje en una red neuronal artificial consiste, fundamentalmente, en ajustar estos pesos.

3. **Suma ponderada y sesgo (*bias*):** La neurona computa la suma ponderada de sus entradas más un término de sesgo $b$:

$$z = \sum_{i=1}^{n} w_i x_i + b = w_1 x_1 + w_2 x_2 + \cdots + w_n x_n + b$$

En notación vectorial, si definimos el vector de entradas $\mathbf{x} = [x_1, x_2, \ldots, x_n]^T \in \mathbb{R}^n$ y el vector de pesos $\mathbf{w} = [w_1, w_2, \ldots, w_n]^T \in \mathbb{R}^n$, la expresión anterior se escribe de forma compacta como:

$$z = \mathbf{w}^T \mathbf{x} + b$$

El término $z$ se denomina frecuentemente *pre-activación* o *logit*. El sesgo $b$ cumple una función análoga al umbral de activación de la neurona biológica (con signo invertido): permite desplazar la frontera de decisión de la neurona sin depender de los valores de entrada.

4. **Función de activación ($f$):** La salida final de la neurona se obtiene aplicando una función de activación $f(\cdot)$ a la pre-activación:

$$y = f(z) = f(\mathbf{w}^T \mathbf{x} + b)$$

La función de activación introduce no linealidad en el modelo. En la neurona biológica, esta no linealidad corresponde al mecanismo de disparo (todo o nada) del potencial de acción. En la neurona artificial, la elección de la función de activación es un aspecto de diseño fundamental que afecta profundamente la capacidad expresiva de la red y las propiedades de su entrenamiento, como se discutirá en detalle en la Sección 1.4.

5. **Salida ($y$):** El valor producido por la función de activación, análogo al potencial de acción transmitido por el axón. Esta salida puede servir como entrada a otras neuronas o como la predicción final del modelo.

**Figura 1.1:** *Diagrama comparativo entre la neurona biológica y la neurona artificial. En el lado izquierdo se ilustra una neurona biológica con sus tres componentes principales: (i) las dendritas, representadas como ramificaciones arbóreas que se extienden desde el cuerpo celular y que reciben señales electroquímicas de otras neuronas a través de las sinapsis; (ii) el soma o cuerpo celular, dibujado como una forma ovalada central que contiene el núcleo, donde se realiza la integración de todas las señales recibidas; y (iii) el axón, representado como una prolongación larga que parte del soma y se ramifica en su extremo terminal en múltiples botones sinápticos que transmiten la señal a las dendritas de neuronas subsiguientes. Las flechas indican el flujo de información desde las dendritas, pasando por el soma, hasta las terminales del axón. En el lado derecho se muestra el modelo matemático de la neurona artificial: las entradas $x_1, x_2, \ldots, x_n$ llegan por la izquierda, cada una multiplicada por su peso correspondiente $w_1, w_2, \ldots, w_n$ (representados como valores numéricos junto a cada conexión). Todas las señales ponderadas convergen en un nodo sumador circular marcado con el símbolo $\Sigma$, que calcula $z = \sum_{i} w_i x_i + b$, donde el sesgo $b$ entra como una entrada adicional con valor constante igual a 1. La salida del sumador alimenta un bloque rectangular etiquetado $f(\cdot)$ que representa la función de activación. Finalmente, la salida $y = f(z)$ emerge por la derecha. Líneas de correspondencia punteadas conectan las dendritas con las entradas ponderadas, el soma con el sumador y la función de activación, y el axón con la salida, evidenciando la analogía funcional entre ambos modelos.*

Es importante enfatizar que la neurona artificial es una simplificación drástica de la biología real. Las neuronas biológicas exhiben dinámicas temporales complejas, operan con pulsos (*spikes*) en lugar de valores continuos, poseen una geometría tridimensional intrincada y se comunican mediante mecanismos químicos y eléctricos sofisticados. No obstante, la abstracción de McCulloch-Pitts y sus extensiones posteriores han demostrado ser extraordinariamente poderosas para tareas de reconocimiento de patrones, clasificación, regresión y, como veremos en este tutorial, para el diseño de sistemas de comunicación semántica.

---

## 1.3 El Perceptrón simple

### 1.3.1 Definición y modelo matemático

El perceptrón, propuesto por Frank Rosenblatt en 1958, constituye el modelo más simple de neurona artificial con capacidad de aprendizaje. A diferencia del modelo estático de McCulloch-Pitts, donde los pesos debían ser determinados manualmente, Rosenblatt introdujo un algoritmo de aprendizaje que permite a la neurona ajustar automáticamente sus pesos a partir de ejemplos de entrenamiento. Este avance marcó el nacimiento del aprendizaje automático supervisado.

El perceptrón simple recibe un vector de entrada $\mathbf{x} = [x_1, x_2, \ldots, x_n]^T \in \mathbb{R}^n$ y produce una salida binaria $y \in \{0, 1\}$ (o equivalentemente $y \in \{-1, +1\}$ según la convención utilizada). Su operación se describe matemáticamente de la siguiente forma:

**Paso 1: Cómputo de la pre-activación.** Se calcula la suma ponderada de las entradas más el sesgo:

$$z = \sum_{i=1}^{n} w_i x_i + b = \mathbf{w}^T \mathbf{x} + b$$

donde $\mathbf{w} = [w_1, w_2, \ldots, w_n]^T \in \mathbb{R}^n$ es el vector de pesos y $b \in \mathbb{R}$ es el sesgo.

**Paso 2: Aplicación de la función de activación escalón.** La salida del perceptrón se determina mediante la función escalón unitario (función de Heaviside):

$$y = f(z) = \begin{cases} 1 & \text{si } z \geq 0 \\ 0 & \text{si } z < 0 \end{cases}$$

Es decir:

$$y = f\left(\sum_{i=1}^{n} w_i x_i + b\right) = f(\mathbf{w}^T \mathbf{x} + b)$$

El perceptrón, por tanto, implementa un clasificador binario: dado un punto $\mathbf{x}$ en el espacio $n$-dimensional, la salida es 1 si el punto cae en un lado de una frontera de decisión, y 0 si cae en el otro.

### 1.3.2 Interpretación geométrica: la frontera de decisión como un hiperplano

Una de las perspectivas más reveladoras para comprender el perceptrón es la interpretación geométrica. La condición de decisión del perceptrón es:

$$\mathbf{w}^T \mathbf{x} + b = 0$$

Esta ecuación define un **hiperplano** en el espacio $\mathbb{R}^n$. Un hiperplano es la generalización a $n$ dimensiones de los conceptos familiares de punto (0D), línea (1D) y plano (2D). Específicamente:

- En $\mathbb{R}^1$ (una sola entrada), la frontera de decisión es un punto en la recta real: $w_1 x_1 + b = 0 \Rightarrow x_1 = -b/w_1$.
- En $\mathbb{R}^2$ (dos entradas), la frontera de decisión es una línea recta: $w_1 x_1 + w_2 x_2 + b = 0$.
- En $\mathbb{R}^3$ (tres entradas), la frontera de decisión es un plano: $w_1 x_1 + w_2 x_2 + w_3 x_3 + b = 0$.
- En $\mathbb{R}^n$, es un hiperplano $(n-1)$-dimensional.

El vector de pesos $\mathbf{w}$ es **normal** (perpendicular) al hiperplano de decisión. Para verificar esto, consideremos dos puntos $\mathbf{x}_a$ y $\mathbf{x}_b$ que yacen sobre el hiperplano, de modo que $\mathbf{w}^T \mathbf{x}_a + b = 0$ y $\mathbf{w}^T \mathbf{x}_b + b = 0$. Restando ambas ecuaciones:

$$\mathbf{w}^T (\mathbf{x}_a - \mathbf{x}_b) = 0$$

Esto demuestra que $\mathbf{w}$ es ortogonal a cualquier vector contenido en el hiperplano, es decir, $\mathbf{w}$ es el vector normal del hiperplano. La dirección de $\mathbf{w}$ apunta hacia la región donde $y = 1$ (la clase positiva), y el sesgo $b$ determina la distancia del hiperplano al origen, que está dada por:

$$d = \frac{|b|}{\|\mathbf{w}\|}$$

donde $\|\mathbf{w}\| = \sqrt{w_1^2 + w_2^2 + \cdots + w_n^2}$ es la norma euclidiana del vector de pesos.

Esta interpretación geométrica tiene consecuencias fundamentales. El perceptrón solo puede resolver problemas de clasificación **linealmente separables**, es decir, aquellos en los que existe un hiperplano que separa perfectamente las dos clases. Como demostraron Minsky y Papert en su influyente libro de 1969, existen problemas aparentemente simples —como la función XOR— que no son linealmente separables y, por tanto, no pueden ser resueltos por un perceptrón simple.

### 1.3.3 Ejemplo: implementación de la compuerta OR

Para ilustrar concretamente el funcionamiento del perceptrón, consideremos la implementación de la función lógica OR. La tabla de verdad de la compuerta OR con dos entradas es:

| $x_1$ | $x_2$ | $y = x_1 \text{ OR } x_2$ |
|:------:|:------:|:--------------------------:|
|   0    |   0    |             0              |
|   0    |   1    |             1              |
|   1    |   0    |             1              |
|   1    |   1    |             1              |

Necesitamos encontrar valores de $w_1$, $w_2$ y $b$ tales que el perceptrón produzca las salidas correctas. La frontera de decisión debe separar el punto $(0,0)$ (clase 0) de los puntos $(0,1)$, $(1,0)$ y $(1,1)$ (clase 1).

Seleccionemos los siguientes parámetros: $w_1 = 1$, $w_2 = 1$ y $b = -0.5$. Verifiquemos cada caso:

1. **Entrada** $(0, 0)$: $z = 1 \cdot 0 + 1 \cdot 0 + (-0.5) = -0.5 < 0 \Rightarrow y = 0$ ✓
2. **Entrada** $(0, 1)$: $z = 1 \cdot 0 + 1 \cdot 1 + (-0.5) = 0.5 \geq 0 \Rightarrow y = 1$ ✓
3. **Entrada** $(1, 0)$: $z = 1 \cdot 1 + 1 \cdot 0 + (-0.5) = 0.5 \geq 0 \Rightarrow y = 1$ ✓
4. **Entrada** $(1, 1)$: $z = 1 \cdot 1 + 1 \cdot 1 + (-0.5) = 1.5 \geq 0 \Rightarrow y = 1$ ✓

La frontera de decisión está dada por la ecuación:

$$x_1 + x_2 - 0.5 = 0 \quad \Longrightarrow \quad x_2 = -x_1 + 0.5$$

Esta es una recta en el plano $x_1$-$x_2$ con pendiente $-1$ y ordenada al origen $0.5$. El vector normal a esta recta es $\mathbf{w} = [1, 1]^T$, que apunta hacia la región donde la salida es 1.

Observemos que la solución no es única. Por ejemplo, los parámetros $w_1 = 2$, $w_2 = 2$, $b = -1$ también funcionan, generando la frontera $2x_1 + 2x_2 - 1 = 0$, que es equivalente a $x_1 + x_2 = 0.5$. De hecho, cualquier hiperplano que separe correctamente el punto $(0,0)$ de los demás será una solución válida, lo que ilustra que en problemas linealmente separables la solución del perceptrón no es única.

**Figura 1.2:** *Visualización de la frontera de decisión del perceptrón para la compuerta OR en el plano $x_1$-$x_2$. Se representan los cuatro puntos de la tabla de verdad: el punto $(0,0)$ se marca con un símbolo circular vacío (○) indicando la clase 0, mientras que los puntos $(0,1)$, $(1,0)$ y $(1,1)$ se marcan con símbolos circulares rellenos (●) indicando la clase 1. La línea de decisión $x_1 + x_2 = 0.5$ se traza como una recta diagonal que va desde el punto $(0, 0.5)$ hasta el punto $(0.5, 0)$, separando perfectamente el punto de clase 0 del resto de puntos de clase 1. La región por encima y a la derecha de la recta (sombreada en azul claro) corresponde a la zona donde $z \geq 0$ y la salida es $y = 1$. La región por debajo y a la izquierda (sin sombrear) corresponde a $z < 0$ y salida $y = 0$. Una flecha etiquetada $\mathbf{w} = [1,1]^T$ parte perpendicular a la recta, apuntando hacia la región de clase positiva, indicando la dirección del vector normal al hiperplano de decisión. Los ejes están etiquetados como $x_1$ (horizontal) y $x_2$ (vertical), con marcas en $0$, $0.5$ y $1$.*

---

## 1.4 Funciones de activación

La función de activación es uno de los componentes más críticos de una neurona artificial. Su papel fundamental es introducir **no linealidad** en el modelo. Sin funciones de activación no lineales, una red neuronal de múltiples capas colapsaría matemáticamente en una sola transformación lineal, ya que la composición de funciones lineales es, a su vez, lineal:

$$f_2(f_1(\mathbf{x})) = \mathbf{W}_2(\mathbf{W}_1 \mathbf{x} + \mathbf{b}_1) + \mathbf{b}_2 = \mathbf{W}_2 \mathbf{W}_1 \mathbf{x} + \mathbf{W}_2 \mathbf{b}_1 + \mathbf{b}_2 = \tilde{\mathbf{W}} \mathbf{x} + \tilde{\mathbf{b}}$$

donde $\tilde{\mathbf{W}} = \mathbf{W}_2 \mathbf{W}_1$ y $\tilde{\mathbf{b}} = \mathbf{W}_2 \mathbf{b}_1 + \mathbf{b}_2$. Esto significa que sin no linealidad, agregar capas no incrementa la capacidad expresiva de la red.

A continuación se presentan las funciones de activación más importantes, organizadas desde la más simple hasta las más sofisticadas.

### 1.4.1 Función escalón (Heaviside)

La función escalón, también conocida como función de Heaviside, es la función de activación más simple y fue la utilizada en el perceptrón original de Rosenblatt:

$$f(z) = \theta(z) = \begin{cases} 1 & \text{si } z \geq 0 \\ 0 & \text{si } z < 0 \end{cases}$$

Alternativamente, usando la convención con salidas en $\{-1, +1\}$:

$$f(z) = \text{sgn}(z) = \begin{cases} +1 & \text{si } z \geq 0 \\ -1 & \text{si } z < 0 \end{cases}$$

La función escalón produce una salida binaria, lo que resulta natural para problemas de clasificación. Sin embargo, presenta una limitación fundamental para el entrenamiento mediante descenso de gradiente: su derivada es cero en todo punto excepto en $z = 0$, donde no está definida (o formalmente, es una distribución delta de Dirac):

$$\frac{d\theta}{dz} = \begin{cases} 0 & \text{si } z \neq 0 \\ \text{indefinida} & \text{si } z = 0 \end{cases}$$

Esta propiedad hace que los métodos de optimización basados en gradientes no puedan utilizarse con la función escalón, ya que el gradiente no proporciona información sobre la dirección en la que deben ajustarse los pesos. Por esta razón, la función escalón se utiliza en la actualidad casi exclusivamente con fines pedagógicos.

### 1.4.2 Función sigmoide (logística)

La función sigmoide, también llamada función logística, fue durante décadas la función de activación estándar en las redes neuronales:

$$\sigma(z) = \frac{1}{1 + e^{-z}}$$

La función sigmoide mapea cualquier valor real $z \in (-\infty, +\infty)$ al intervalo $(0, 1)$, lo que permite interpretarla como una probabilidad. Sus propiedades principales son:

- **Rango:** $(0, 1)$. Nótese que los valores 0 y 1 son límites asintóticos que nunca se alcanzan exactamente.
- **Monotonía:** Es estrictamente creciente para todo $z$.
- **Simetría:** Satisface la relación $\sigma(-z) = 1 - \sigma(z)$.
- **Punto de inflexión:** En $z = 0$, donde $\sigma(0) = 0.5$.
- **Comportamiento asintótico:** $\lim_{z \to -\infty} \sigma(z) = 0$ y $\lim_{z \to +\infty} \sigma(z) = 1$.

**Derivación de la derivada de la sigmoide.** Una propiedad matemática notable de la sigmoide es que su derivada puede expresarse de forma cerrada en términos de sí misma. Derivemos este resultado paso a paso:

$$\sigma(z) = \frac{1}{1 + e^{-z}} = (1 + e^{-z})^{-1}$$

Aplicando la regla de la cadena:

$$\sigma'(z) = \frac{d}{dz}\left[(1 + e^{-z})^{-1}\right] = -(1 + e^{-z})^{-2} \cdot \frac{d}{dz}(1 + e^{-z})$$

El término $\frac{d}{dz}(1 + e^{-z}) = -e^{-z}$, por lo que:

$$\sigma'(z) = -(1 + e^{-z})^{-2} \cdot (-e^{-z}) = \frac{e^{-z}}{(1 + e^{-z})^2}$$

Ahora, observemos que:

$$\sigma(z) \cdot (1 - \sigma(z)) = \frac{1}{1 + e^{-z}} \cdot \frac{e^{-z}}{1 + e^{-z}} = \frac{e^{-z}}{(1 + e^{-z})^2}$$

donde hemos utilizado que $1 - \sigma(z) = 1 - \frac{1}{1+e^{-z}} = \frac{e^{-z}}{1+e^{-z}}$. Comparando ambas expresiones, concluimos:

$$\boxed{\sigma'(z) = \sigma(z)(1 - \sigma(z))}$$

Este resultado es computacionalmente conveniente, ya que durante el entrenamiento de la red, si ya se ha calculado $\sigma(z)$, obtener su derivada requiere solo una multiplicación y una resta. El valor máximo de la derivada ocurre en $z = 0$, donde $\sigma'(0) = 0.5 \times 0.5 = 0.25$.

**Problema del desvanecimiento de gradientes (*vanishing gradients*).** A pesar de sus propiedades elegantes, la sigmoide sufre un problema importante cuando se utiliza en redes profundas: para valores de $|z|$ grandes, la derivada $\sigma'(z)$ tiende a cero. Esto significa que durante la retropropagación, los gradientes que se multiplican a través de muchas capas se vuelven exponencialmente pequeños, ralentizando o deteniendo completamente el aprendizaje en las capas más profundas. Dado que $\sigma'(z) \leq 0.25$ para todo $z$, al pasar por $L$ capas con activación sigmoide, el gradiente se escala por un factor del orden de $(0.25)^L$, que decrece rápidamente.

### 1.4.3 Tangente hiperbólica (tanh)

La tangente hiperbólica es otra función de activación suave y diferenciable, definida como:

$$\tanh(z) = \frac{e^z - e^{-z}}{e^z + e^{-z}}$$

Es posible demostrar que la tangente hiperbólica es, en realidad, una versión reescalada y desplazada de la sigmoide:

$$\tanh(z) = 2\sigma(2z) - 1$$

Esta relación puede verificarse directamente:

$$2\sigma(2z) - 1 = \frac{2}{1 + e^{-2z}} - 1 = \frac{2 - (1 + e^{-2z})}{1 + e^{-2z}} = \frac{1 - e^{-2z}}{1 + e^{-2z}}$$

Multiplicando numerador y denominador por $e^z$:

$$= \frac{e^z - e^{-z}}{e^z + e^{-z}} = \tanh(z) \quad \checkmark$$

Las propiedades principales de la tangente hiperbólica son:

- **Rango:** $(-1, 1)$. A diferencia de la sigmoide, la tanh está centrada en cero, lo que hace que sus salidas tengan media aproximadamente cero. Esta propiedad es beneficiosa para el entrenamiento, ya que las entradas a la siguiente capa no estarán sesgadas hacia valores positivos.
- **Simetría:** Es una función impar: $\tanh(-z) = -\tanh(z)$.
- **Derivada:** $\tanh'(z) = 1 - \tanh^2(z)$. En $z = 0$, $\tanh'(0) = 1$, lo cual es cuatro veces mayor que la derivada máxima de la sigmoide ($0.25$), lo que proporciona gradientes más fuertes.

A pesar de estas ventajas sobre la sigmoide, la tangente hiperbólica también sufre el problema de desvanecimiento de gradientes para valores grandes de $|z|$, ya que $\tanh'(z) \to 0$ cuando $|z| \to \infty$.

### 1.4.4 Unidad Lineal Rectificada (ReLU)

La función ReLU (*Rectified Linear Unit*), propuesta como función de activación para redes neuronales y popularizada a partir del trabajo de Nair y Hinton (2010) y del impacto práctico demostrado por Krizhevsky, Sutskever e Hinton en la arquitectura AlexNet (2012), representa un punto de inflexión en la historia del aprendizaje profundo:

$$f(z) = \text{ReLU}(z) = \max(0, z) = \begin{cases} z & \text{si } z > 0 \\ 0 & \text{si } z \leq 0 \end{cases}$$

Su derivada es:

$$f'(z) = \begin{cases} 1 & \text{si } z > 0 \\ 0 & \text{si } z < 0 \\ \text{indefinida} & \text{si } z = 0 \end{cases}$$

En la práctica, la derivada en $z = 0$ se define convencionalmente como 0 o 1.

Las ventajas de ReLU son significativas:

1. **Eficiencia computacional:** Su cómputo es extremadamente simple —solo una comparación y una asignación—, en contraste con las funciones exponenciales de la sigmoide y la tanh.
2. **Mitigación del desvanecimiento de gradientes:** Para $z > 0$, la derivada es exactamente 1, lo que permite que los gradientes fluyan sin atenuación a través de las capas de la red.
3. **Esparsidad:** ReLU produce exactamente cero para todas las entradas negativas, lo que genera representaciones esparsas (muchas neuronas con salida cero). Esta esparsidad ha demostrado ser beneficiosa para la generalización.

**El problema de las neuronas muertas (*dying ReLU*).** A pesar de sus ventajas, ReLU presenta un problema conocido: si durante el entrenamiento una neurona recibe consistentemente entradas negativas (es decir, $z < 0$), su gradiente será perpetuamente cero. Esto significa que los pesos de esa neurona nunca se actualizarán y la neurona quedará permanentemente "muerta" —produciendo siempre una salida de cero, independientemente de la entrada. Este fenómeno puede ocurrir si la tasa de aprendizaje es demasiado alta, causando que los pesos se actualicen de forma tan abrupta que la neurona se mueve a la región negativa y no puede regresar. En redes profundas con muchas neuronas ReLU, no es infrecuente que un porcentaje significativo de las neuronas (a veces hasta el 40% o más) estén "muertas" al final del entrenamiento.

### 1.4.5 Variantes de ReLU

Para abordar el problema de las neuronas muertas, se han propuesto diversas variantes de ReLU:

**Leaky ReLU (ReLU con fuga):** Introduce una pequeña pendiente $\alpha$ (típicamente $\alpha = 0.01$) para las entradas negativas:

$$f(z) = \begin{cases} z & \text{si } z > 0 \\ \alpha z & \text{si } z \leq 0 \end{cases} = \max(\alpha z, z)$$

De esta forma, la derivada para $z < 0$ es $\alpha \neq 0$, lo que evita que las neuronas mueran completamente. El hiperparámetro $\alpha$ controla la pendiente en la región negativa.

**Parametric ReLU (PReLU):** Es una generalización de Leaky ReLU en la que el parámetro $\alpha$ no se fija manualmente, sino que se aprende durante el entrenamiento como un parámetro más del modelo:

$$f(z) = \max(\alpha z, z), \quad \alpha \text{ aprendible}$$

**Exponential Linear Unit (ELU):** Propuesta por Clevert, Unterthiner y Hochreiter (2016), utiliza una función exponencial para la región negativa:

$$f(z) = \begin{cases} z & \text{si } z > 0 \\ \alpha(e^z - 1) & \text{si } z \leq 0 \end{cases}$$

donde $\alpha > 0$ es un hiperparámetro (comúnmente $\alpha = 1$). A diferencia de Leaky ReLU, la ELU se satura en $-\alpha$ para valores muy negativos, lo que proporciona robustez al ruido. Además, la ELU produce salidas con media más cercana a cero que ReLU, lo que puede acelerar el entrenamiento.

**GELU (Gaussian Error Linear Unit):** Propuesta por Hendrycks y Gimpel (2016), la GELU pondera la entrada por la probabilidad de que sea mayor que las demás entradas, bajo la suposición de una distribución normal:

$$\text{GELU}(z) = z \cdot \Phi(z) = z \cdot \frac{1}{2}\left[1 + \text{erf}\left(\frac{z}{\sqrt{2}}\right)\right]$$

donde $\Phi(z)$ es la función de distribución acumulada (CDF) de la distribución normal estándar y $\text{erf}$ es la función error. Una aproximación práctica frecuentemente utilizada es:

$$\text{GELU}(z) \approx 0.5 \, z \left[1 + \tanh\left(\sqrt{\frac{2}{\pi}}\left(z + 0.044715 \, z^3\right)\right)\right]$$

La GELU se ha convertido en la función de activación predominante en modelos de lenguaje basados en transformers, como BERT y GPT. A diferencia de ReLU, que aplica una "compuerta" determinista (pasa o no pasa), la GELU aplica una compuerta estocástica suave que depende del valor de la entrada, produciendo una transición gradual.

**Swish (SiLU):** Propuesta por Ramachandran, Zoph y Le (2017), y también conocida como SiLU (*Sigmoid Linear Unit*):

$$\text{Swish}(z) = z \cdot \sigma(\beta z) = \frac{z}{1 + e^{-\beta z}}$$

donde $\beta$ es un parámetro que controla la forma de la función. Cuando $\beta = 1$ (caso más común), se reduce a:

$$\text{Swish}(z) = \frac{z}{1 + e^{-z}}$$

La Swish es no monótona: para valores negativos cercanos a cero, la función puede tomar valores ligeramente negativos antes de saturarse a cero, lo que la diferencia fundamentalmente de ReLU. Se ha observado empíricamente que Swish iguala o supera a ReLU en una variedad de tareas, particularmente en redes profundas.

### 1.4.6 Función Softmax para clasificación multi-clase

Todas las funciones de activación discutidas hasta ahora operan elemento a elemento: cada neurona aplica la función de activación de manera independiente a su propia pre-activación. La función softmax, en cambio, opera sobre un **vector** completo de pre-activaciones y produce un vector de probabilidades. Se utiliza típicamente en la capa de salida de redes neuronales diseñadas para clasificación multi-clase.

Dado un vector de pre-activaciones $\mathbf{z} = [z_1, z_2, \ldots, z_K]^T$, donde $K$ es el número de clases, la función softmax se define como:

$$\text{softmax}(z_i) = \frac{e^{z_i}}{\sum_{j=1}^{K} e^{z_j}}, \quad \text{para } i = 1, 2, \ldots, K$$

Las propiedades de la softmax son:

1. **Positividad:** $\text{softmax}(z_i) > 0$ para todo $i$, ya que la función exponencial es siempre positiva.
2. **Normalización:** $\sum_{i=1}^{K} \text{softmax}(z_i) = 1$. Las salidas forman una distribución de probabilidad válida sobre las $K$ clases.
3. **Monotonía relativa:** Si $z_i > z_j$, entonces $\text{softmax}(z_i) > \text{softmax}(z_j)$. La clase con la mayor pre-activación tendrá la mayor probabilidad.
4. **Amplificación de diferencias:** La función exponencial amplifica las diferencias entre las pre-activaciones. Si una pre-activación es significativamente mayor que las demás, la probabilidad correspondiente se acercará a 1, mientras que las demás se acercarán a 0. Este efecto se puede controlar introduciendo un parámetro de temperatura $T$:

$$\text{softmax}(z_i; T) = \frac{e^{z_i / T}}{\sum_{j=1}^{K} e^{z_j / T}}$$

Con $T \to 0$, la softmax tiende a una función argmax determinista (one-hot); con $T \to \infty$, la distribución se acerca a la uniforme $1/K$.

**Estabilidad numérica.** En la implementación práctica, calcular $e^{z_i}$ directamente puede causar desbordamiento numérico (*overflow*) si $z_i$ es muy grande. Para evitar esto, se utiliza el truco de restar el valor máximo:

$$\text{softmax}(z_i) = \frac{e^{z_i - z_{\max}}}{\sum_{j=1}^{K} e^{z_j - z_{\max}}}, \quad \text{donde } z_{\max} = \max_j z_j$$

Esta modificación no altera el resultado matemático (las constantes se cancelan), pero garantiza que el mayor exponente sea $e^0 = 1$, previniendo el desbordamiento.

### 1.4.7 Descripción de figura: funciones de activación

**Figura 1.3:** *Gráficas comparativas de las principales funciones de activación utilizadas en redes neuronales. La figura se organiza en una cuadrícula de $3 \times 3$ subgráficas, cada una mostrando una función diferente junto con su derivada (en línea punteada). (a) Función escalón (Heaviside): una línea horizontal en $y=0$ para $z<0$ y una línea horizontal en $y=1$ para $z \geq 0$, con una discontinuidad de salto en $z=0$. (b) Sigmoide $\sigma(z) = 1/(1+e^{-z})$: una curva en forma de "S" suave que transita gradualmente de 0 a 1, con su derivada en forma de campana centrada en $z=0$ con un máximo de $0.25$. (c) Tangente hiperbólica $\tanh(z)$: similar a la sigmoide pero centrada en cero, transitando de $-1$ a $+1$, con su derivada en forma de campana con máximo en $1.0$ en $z=0$. (d) ReLU: una línea en $y=0$ para $z \leq 0$ y una línea con pendiente 1 para $z > 0$, formando un "codo" en el origen; su derivada es una función escalón (0 para $z<0$, 1 para $z>0$). (e) Leaky ReLU ($\alpha = 0.1$): similar a ReLU pero con una línea de pendiente suave $0.1$ para $z < 0$. (f) ELU ($\alpha = 1$): idéntica a ReLU para $z > 0$, pero con una curva exponencial suave que se satura en $-1$ para $z \ll 0$. (g) GELU: una curva suave similar a ReLU para $z > 0$ pero con una pequeña región negativa antes del origen, sin codo abrupto. (h) Swish ($\beta = 1$): similar a GELU, con una curva suave que presenta un mínimo negativo alrededor de $z \approx -1.28$ antes de saturarse a cero para $z \to -\infty$. (i) Softmax: se muestra un ejemplo con $K=3$ clases, graficando las tres probabilidades de salida como funciones de $z_1$ mientras se mantienen $z_2=0$ y $z_3=0$ fijos, mostrando cómo la probabilidad de la clase 1 crece sigmoidealmente mientras las otras decrecen simétricamente. Todos los ejes horizontales abarcan el rango $[-5, 5]$, y las funciones se dibujan en azul sólido con sus derivadas en rojo punteado.*

---

## 1.5 Aprendizaje y la regla de actualización de pesos

### 1.5.1 El concepto de aprendizaje en redes neuronales

En el contexto de las redes neuronales artificiales, **aprender** significa encontrar el conjunto de parámetros (pesos $\mathbf{w}$ y sesgos $b$) que minimiza una **función de pérdida** (*loss function*) $L$ que cuantifica la discrepancia entre las predicciones del modelo $\hat{y}$ y los valores verdaderos $y$ en un conjunto de datos de entrenamiento.

Formalmente, dado un conjunto de datos de entrenamiento $\mathcal{D} = \{(\mathbf{x}^{(1)}, y^{(1)}), (\mathbf{x}^{(2)}, y^{(2)}), \ldots, (\mathbf{x}^{(N)}, y^{(N)})\}$, donde $\mathbf{x}^{(k)} \in \mathbb{R}^n$ es el vector de entrada $k$-ésimo e $y^{(k)}$ es su etiqueta o valor objetivo correspondiente, el problema de aprendizaje se formula como un problema de **optimización**:

$$\min_{\mathbf{w}, b} \; L(\mathbf{w}, b) = \min_{\mathbf{w}, b} \; \frac{1}{N} \sum_{k=1}^{N} \ell\left(y^{(k)}, \hat{y}^{(k)}\right)$$

donde $\ell(y, \hat{y})$ es la función de pérdida evaluada en un solo ejemplo y $\hat{y}^{(k)} = f(\mathbf{w}^T \mathbf{x}^{(k)} + b)$ es la predicción del modelo para la entrada $\mathbf{x}^{(k)}$.

### 1.5.2 Descenso de gradiente: intuición geométrica

El **descenso de gradiente** (*gradient descent*) es el algoritmo fundamental para la optimización de redes neuronales. Su intuición geométrica es poderosa y sencilla: imaginemos la función de pérdida $L(\mathbf{w})$ como una superficie montañosa en un espacio de alta dimensión, donde cada eje corresponde a un peso de la red y la "altitud" representa el valor de la pérdida. El objetivo es encontrar el punto más bajo de esta superficie (el mínimo global, o al menos un buen mínimo local).

El gradiente de $L$ respecto a los pesos, denotado $\nabla_{\mathbf{w}} L$, es un vector que apunta en la **dirección de máximo crecimiento** de $L$. Matemáticamente:

$$\nabla_{\mathbf{w}} L = \left[\frac{\partial L}{\partial w_1}, \frac{\partial L}{\partial w_2}, \ldots, \frac{\partial L}{\partial w_n}\right]^T$$

Para descender por la superficie de la pérdida (es decir, reducir $L$), debemos movernos en la dirección **opuesta** al gradiente: $-\nabla_{\mathbf{w}} L$. Esta es la dirección de máximo decrecimiento local de la función de pérdida.

### 1.5.3 Tasa de aprendizaje y regla de actualización

La **tasa de aprendizaje** $\eta > 0$ (*learning rate*) es un hiperparámetro escalar que controla el tamaño del paso que damos en cada iteración del descenso de gradiente. La regla de actualización de pesos es:

$$w_i^{(t+1)} = w_i^{(t)} - \eta \frac{\partial L}{\partial w_i}$$

o en notación vectorial:

$$\mathbf{w}^{(t+1)} = \mathbf{w}^{(t)} - \eta \nabla_{\mathbf{w}} L$$

y de manera análoga para el sesgo:

$$b^{(t+1)} = b^{(t)} - \eta \frac{\partial L}{\partial b}$$

donde el superíndice $(t)$ indica la iteración actual y $(t+1)$ la siguiente.

La elección de la tasa de aprendizaje es crítica:

- **$\eta$ demasiado grande:** Los pasos de actualización son muy grandes, lo que puede causar que el algoritmo "salte" sobre el mínimo, oscile sin convergir o incluso diverja (la pérdida aumenta en lugar de disminuir).
- **$\eta$ demasiado pequeña:** Los pasos son muy pequeños, lo que hace que la convergencia sea extremadamente lenta. Además, el algoritmo tiene mayor riesgo de quedar atrapado en mínimos locales poco profundos o en puntos de silla (*saddle points*).
- **$\eta$ adecuada:** Los pasos son lo suficientemente grandes para avanzar con rapidez, pero lo suficientemente pequeños para no sobrepasar el mínimo.

En la práctica, los valores típicos iniciales de $\eta$ oscilan entre $10^{-4}$ y $10^{-1}$, dependiendo del problema, la arquitectura y el optimizador utilizado. Es frecuente emplear **programas de tasa de aprendizaje** (*learning rate schedules*) que reducen $\eta$ a medida que avanza el entrenamiento.

### 1.5.4 Funciones de pérdida

La elección de la función de pérdida $\ell(y, \hat{y})$ depende del tipo de problema:

**Error cuadrático medio (MSE, *Mean Squared Error*):*** Se utiliza principalmente en problemas de regresión, donde la salida es un valor continuo:

$$L_{\text{MSE}} = \frac{1}{N} \sum_{k=1}^{N} \left(y^{(k)} - \hat{y}^{(k)}\right)^2$$

La derivada de la pérdida MSE respecto a la predicción es:

$$\frac{\partial \ell}{\partial \hat{y}} = \frac{\partial}{\partial \hat{y}}\left(y - \hat{y}\right)^2 = -2(y - \hat{y})$$

El MSE penaliza cuadráticamente los errores grandes, lo que puede ser ventajoso (prioriza la corrección de errores grandes) o desventajoso (es sensible a valores atípicos u *outliers*).

**Entropía cruzada binaria (*Binary Cross-Entropy*):*** Se utiliza en problemas de clasificación binaria, donde $y \in \{0, 1\}$ y $\hat{y} = \sigma(z) \in (0, 1)$ representa la probabilidad estimada de que la entrada pertenezca a la clase 1:

$$L_{\text{BCE}} = -\frac{1}{N} \sum_{k=1}^{N} \left[y^{(k)} \log \hat{y}^{(k)} + (1 - y^{(k)}) \log(1 - \hat{y}^{(k)})\right]$$

La entropía cruzada tiene una interpretación profunda en teoría de la información: mide la divergencia entre la distribución verdadera $p = [y, 1-y]$ y la distribución estimada $q = [\hat{y}, 1-\hat{y}]$. Minimizar la entropía cruzada equivale a minimizar la divergencia de Kullback-Leibler $D_{\text{KL}}(p \| q)$, dado que la entropía de la distribución verdadera $H(p)$ es constante.

La derivada de la entropía cruzada binaria respecto a la pre-activación $z$ (cuando se usa activación sigmoide) tiene una forma particularmente elegante:

$$\frac{\partial L_{\text{BCE}}}{\partial z} = \hat{y} - y = \sigma(z) - y$$

Esta simplicidad es una de las razones por las que la combinación sigmoide + entropía cruzada es tan popular.

**Entropía cruzada categórica (*Categorical Cross-Entropy*):*** Generalización para clasificación multi-clase con $K$ clases, donde $y$ es un vector one-hot y $\hat{y}$ es la salida de la función softmax:

$$L_{\text{CCE}} = -\sum_{i=1}^{K} y_i \log \hat{y}_i$$

donde $y_i = 1$ solo para la clase correcta y $y_i = 0$ para las demás.

### 1.5.5 Ejemplo completo: entrenamiento de un perceptrón para la compuerta AND

Para solidificar la comprensión de los conceptos de aprendizaje, desarrollemos paso a paso el entrenamiento de un perceptrón para implementar la función lógica AND. Utilizaremos la regla de aprendizaje del perceptrón, que es un caso especial del descenso de gradiente para la función de activación escalón.

**Tabla de verdad de la compuerta AND:**

| $x_1$ | $x_2$ | $y = x_1 \text{ AND } x_2$ |
|:------:|:------:|:---------------------------:|
|   0    |   0    |              0              |
|   0    |   1    |              0              |
|   1    |   0    |              0              |
|   1    |   1    |              1              |

**Regla de actualización del perceptrón.** Para el perceptrón con activación escalón, la regla de actualización es:

$$w_i^{(t+1)} = w_i^{(t)} + \eta \left(y^{(k)} - \hat{y}^{(k)}\right) x_i^{(k)}$$

$$b^{(t+1)} = b^{(t)} + \eta \left(y^{(k)} - \hat{y}^{(k)}\right)$$

donde $y^{(k)}$ es la salida deseada para el ejemplo $k$, $\hat{y}^{(k)}$ es la salida predicha, y $\eta$ es la tasa de aprendizaje. Nótese que los pesos solo se actualizan cuando hay un error de clasificación ($y^{(k)} \neq \hat{y}^{(k)}$).

**Configuración inicial:**
- Tasa de aprendizaje: $\eta = 1$
- Pesos iniciales: $w_1 = 0$, $w_2 = 0$
- Sesgo inicial: $b = 0$

**Época 1** (una pasada completa por todos los datos de entrenamiento):

**Iteración 1** — Entrada: $(x_1, x_2) = (0, 0)$, Objetivo: $y = 0$

$$z = w_1 x_1 + w_2 x_2 + b = 0 \cdot 0 + 0 \cdot 0 + 0 = 0$$

$$\hat{y} = f(z) = f(0) = 1 \quad (\text{ya que } z \geq 0)$$

Error: $e = y - \hat{y} = 0 - 1 = -1 \neq 0 \Rightarrow$ actualizar pesos.

$$w_1 \leftarrow 0 + 1 \cdot (-1) \cdot 0 = 0$$

$$w_2 \leftarrow 0 + 1 \cdot (-1) \cdot 0 = 0$$

$$b \leftarrow 0 + 1 \cdot (-1) = -1$$

Estado actual: $w_1 = 0, \; w_2 = 0, \; b = -1$.

**Iteración 2** — Entrada: $(x_1, x_2) = (0, 1)$, Objetivo: $y = 0$

$$z = 0 \cdot 0 + 0 \cdot 1 + (-1) = -1$$

$$\hat{y} = f(-1) = 0 \quad (\text{ya que } z < 0)$$

Error: $e = 0 - 0 = 0 \Rightarrow$ no actualizar. ✓

Estado actual: $w_1 = 0, \; w_2 = 0, \; b = -1$.

**Iteración 3** — Entrada: $(x_1, x_2) = (1, 0)$, Objetivo: $y = 0$

$$z = 0 \cdot 1 + 0 \cdot 0 + (-1) = -1$$

$$\hat{y} = f(-1) = 0$$

Error: $e = 0 - 0 = 0 \Rightarrow$ no actualizar. ✓

Estado actual: $w_1 = 0, \; w_2 = 0, \; b = -1$.

**Iteración 4** — Entrada: $(x_1, x_2) = (1, 1)$, Objetivo: $y = 1$

$$z = 0 \cdot 1 + 0 \cdot 1 + (-1) = -1$$

$$\hat{y} = f(-1) = 0$$

Error: $e = 1 - 0 = 1 \neq 0 \Rightarrow$ actualizar pesos.

$$w_1 \leftarrow 0 + 1 \cdot 1 \cdot 1 = 1$$

$$w_2 \leftarrow 0 + 1 \cdot 1 \cdot 1 = 1$$

$$b \leftarrow -1 + 1 \cdot 1 = 0$$

Estado actual: $w_1 = 1, \; w_2 = 1, \; b = 0$.

**Fin de la Época 1.** Hubo errores, por lo que es necesario continuar el entrenamiento.

---

**Época 2:**

**Iteración 5** — Entrada: $(0, 0)$, Objetivo: $y = 0$

$$z = 1 \cdot 0 + 1 \cdot 0 + 0 = 0$$

$$\hat{y} = f(0) = 1$$

Error: $e = 0 - 1 = -1 \Rightarrow$ actualizar.

$$w_1 \leftarrow 1 + 1 \cdot (-1) \cdot 0 = 1$$

$$w_2 \leftarrow 1 + 1 \cdot (-1) \cdot 0 = 1$$

$$b \leftarrow 0 + 1 \cdot (-1) = -1$$

Estado actual: $w_1 = 1, \; w_2 = 1, \; b = -1$.

**Iteración 6** — Entrada: $(0, 1)$, Objetivo: $y = 0$

$$z = 1 \cdot 0 + 1 \cdot 1 + (-1) = 0$$

$$\hat{y} = f(0) = 1$$

Error: $e = 0 - 1 = -1 \Rightarrow$ actualizar.

$$w_1 \leftarrow 1 + 1 \cdot (-1) \cdot 0 = 1$$

$$w_2 \leftarrow 1 + 1 \cdot (-1) \cdot 1 = 0$$

$$b \leftarrow -1 + 1 \cdot (-1) = -2$$

Estado actual: $w_1 = 1, \; w_2 = 0, \; b = -2$.

**Iteración 7** — Entrada: $(1, 0)$, Objetivo: $y = 0$

$$z = 1 \cdot 1 + 0 \cdot 0 + (-2) = -1$$

$$\hat{y} = f(-1) = 0$$

Error: $e = 0 - 0 = 0 \Rightarrow$ no actualizar. ✓

Estado actual: $w_1 = 1, \; w_2 = 0, \; b = -2$.

**Iteración 8** — Entrada: $(1, 1)$, Objetivo: $y = 1$

$$z = 1 \cdot 1 + 0 \cdot 1 + (-2) = -1$$

$$\hat{y} = f(-1) = 0$$

Error: $e = 1 - 0 = 1 \Rightarrow$ actualizar.

$$w_1 \leftarrow 1 + 1 \cdot 1 \cdot 1 = 2$$

$$w_2 \leftarrow 0 + 1 \cdot 1 \cdot 1 = 1$$

$$b \leftarrow -2 + 1 \cdot 1 = -1$$

Estado actual: $w_1 = 2, \; w_2 = 1, \; b = -1$.

**Fin de la Época 2.** Hubo errores, continuar.

---

**Época 3:**

**Iteración 9** — Entrada: $(0, 0)$, Objetivo: $y = 0$

$$z = 2 \cdot 0 + 1 \cdot 0 + (-1) = -1$$

$$\hat{y} = f(-1) = 0$$

Error: $e = 0 - 0 = 0 \Rightarrow$ no actualizar. ✓

**Iteración 10** — Entrada: $(0, 1)$, Objetivo: $y = 0$

$$z = 2 \cdot 0 + 1 \cdot 1 + (-1) = 0$$

$$\hat{y} = f(0) = 1$$

Error: $e = 0 - 1 = -1 \Rightarrow$ actualizar.

$$w_1 \leftarrow 2 + 1 \cdot (-1) \cdot 0 = 2$$

$$w_2 \leftarrow 1 + 1 \cdot (-1) \cdot 1 = 0$$

$$b \leftarrow -1 + 1 \cdot (-1) = -2$$

Estado actual: $w_1 = 2, \; w_2 = 0, \; b = -2$.

**Iteración 11** — Entrada: $(1, 0)$, Objetivo: $y = 0$

$$z = 2 \cdot 1 + 0 \cdot 0 + (-2) = 0$$

$$\hat{y} = f(0) = 1$$

Error: $e = 0 - 1 = -1 \Rightarrow$ actualizar.

$$w_1 \leftarrow 2 + 1 \cdot (-1) \cdot 1 = 1$$

$$w_2 \leftarrow 0 + 1 \cdot (-1) \cdot 0 = 0$$

$$b \leftarrow -2 + 1 \cdot (-1) = -3$$

Estado actual: $w_1 = 1, \; w_2 = 0, \; b = -3$.

**Iteración 12** — Entrada: $(1, 1)$, Objetivo: $y = 1$

$$z = 1 \cdot 1 + 0 \cdot 1 + (-3) = -2$$

$$\hat{y} = f(-2) = 0$$

Error: $e = 1 - 0 = 1 \Rightarrow$ actualizar.

$$w_1 \leftarrow 1 + 1 \cdot 1 \cdot 1 = 2$$

$$w_2 \leftarrow 0 + 1 \cdot 1 \cdot 1 = 1$$

$$b \leftarrow -3 + 1 \cdot 1 = -2$$

Estado actual: $w_1 = 2, \; w_2 = 1, \; b = -2$.

**Fin de la Época 3.** Hubo errores, continuar.

---

**Época 4:**

**Iteración 13** — Entrada: $(0, 0)$, Objetivo: $y = 0$

$$z = 2 \cdot 0 + 1 \cdot 0 + (-2) = -2$$

$$\hat{y} = f(-2) = 0 \quad \checkmark$$

**Iteración 14** — Entrada: $(0, 1)$, Objetivo: $y = 0$

$$z = 2 \cdot 0 + 1 \cdot 1 + (-2) = -1$$

$$\hat{y} = f(-1) = 0 \quad \checkmark$$

**Iteración 15** — Entrada: $(1, 0)$, Objetivo: $y = 0$

$$z = 2 \cdot 1 + 1 \cdot 0 + (-2) = 0$$

$$\hat{y} = f(0) = 1$$

Error: $e = 0 - 1 = -1 \Rightarrow$ actualizar.

$$w_1 \leftarrow 2 + 1 \cdot (-1) \cdot 1 = 1$$

$$w_2 \leftarrow 1 + 1 \cdot (-1) \cdot 0 = 1$$

$$b \leftarrow -2 + 1 \cdot (-1) = -3$$

Estado actual: $w_1 = 1, \; w_2 = 1, \; b = -3$.

**Iteración 16** — Entrada: $(1, 1)$, Objetivo: $y = 1$

$$z = 1 \cdot 1 + 1 \cdot 1 + (-3) = -1$$

$$\hat{y} = f(-1) = 0$$

Error: $e = 1 - 0 = 1 \Rightarrow$ actualizar.

$$w_1 \leftarrow 1 + 1 \cdot 1 \cdot 1 = 2$$

$$w_2 \leftarrow 1 + 1 \cdot 1 \cdot 1 = 2$$

$$b \leftarrow -3 + 1 \cdot 1 = -2$$

Estado actual: $w_1 = 2, \; w_2 = 2, \; b = -2$.

**Fin de la Época 4.** Hubo errores, continuar.

---

**Época 5:**

**Iteración 17** — Entrada: $(0, 0)$, Objetivo: $y = 0$

$$z = 2 \cdot 0 + 2 \cdot 0 + (-2) = -2, \quad \hat{y} = 0 \quad \checkmark$$

**Iteración 18** — Entrada: $(0, 1)$, Objetivo: $y = 0$

$$z = 2 \cdot 0 + 2 \cdot 1 + (-2) = 0, \quad \hat{y} = f(0) = 1$$

Error: $e = -1 \Rightarrow$ actualizar.

$$w_1 \leftarrow 2, \quad w_2 \leftarrow 2 + (-1)(1) = 1, \quad b \leftarrow -2 + (-1) = -3$$

Estado: $w_1 = 2, \; w_2 = 1, \; b = -3$.

**Iteración 19** — Entrada: $(1, 0)$, Objetivo: $y = 0$

$$z = 2 \cdot 1 + 1 \cdot 0 + (-3) = -1, \quad \hat{y} = 0 \quad \checkmark$$

**Iteración 20** — Entrada: $(1, 1)$, Objetivo: $y = 1$

$$z = 2 \cdot 1 + 1 \cdot 1 + (-3) = 0, \quad \hat{y} = f(0) = 1 \quad \checkmark$$

**Fin de la Época 5.** Hubo un error. Continuar.

---

**Época 6:**

**Iteración 21** — $(0, 0)$, $y = 0$:

$$z = 2 \cdot 0 + 1 \cdot 0 - 3 = -3, \quad \hat{y} = 0 \quad \checkmark$$

**Iteración 22** — $(0, 1)$, $y = 0$:

$$z = 2 \cdot 0 + 1 \cdot 1 - 3 = -2, \quad \hat{y} = 0 \quad \checkmark$$

**Iteración 23** — $(1, 0)$, $y = 0$:

$$z = 2 \cdot 1 + 1 \cdot 0 - 3 = -1, \quad \hat{y} = 0 \quad \checkmark$$

**Iteración 24** — $(1, 1)$, $y = 1$:

$$z = 2 \cdot 1 + 1 \cdot 1 - 3 = 0, \quad \hat{y} = f(0) = 1 \quad \checkmark$$

**Fin de la Época 6.** ¡Ningún error! El perceptrón ha **convergido**.

---

**Resultado final:** Los parámetros aprendidos son $w_1 = 2$, $w_2 = 1$, $b = -3$. La frontera de decisión resultante es:

$$2x_1 + x_2 - 3 = 0 \quad \Longrightarrow \quad x_2 = -2x_1 + 3$$

Verifiquemos que esta solución clasifica correctamente todos los ejemplos:

| $(x_1, x_2)$ | $z = 2x_1 + x_2 - 3$ | $\hat{y}$ | $y$ | ¿Correcto? |
|:-------------:|:----------------------:|:---------:|:---:|:----------:|
| $(0, 0)$      | $-3$                   | $0$       | $0$ | ✓          |
| $(0, 1)$      | $-2$                   | $0$       | $0$ | ✓          |
| $(1, 0)$      | $-1$                   | $0$       | $0$ | ✓          |
| $(1, 1)$      | $0$                    | $1$       | $1$ | ✓          |

Este ejemplo ilustra varios aspectos fundamentales del aprendizaje del perceptrón:

1. **Convergencia garantizada:** El teorema de convergencia del perceptrón (Rosenblatt, 1962) establece que si los datos de entrenamiento son linealmente separables, el algoritmo del perceptrón convergerá en un número finito de iteraciones, sin importar la inicialización de los pesos. En nuestro ejemplo, la convergencia ocurrió después de 6 épocas (24 iteraciones individuales).

2. **Sensibilidad al orden de presentación:** El número de épocas necesarias para converger depende del orden en que se presentan los ejemplos y de la inicialización de los pesos. Un orden diferente o una inicialización diferente podrían llevar a una convergencia más rápida o más lenta.

3. **La solución no es única:** Diferentes inicializaciones y órdenes de presentación conducen a diferentes soluciones finales ($w_1 = 2, w_2 = 1, b = -3$ no es la única solución válida). Por ejemplo, $w_1 = 1, w_2 = 1, b = -1.5$ también clasifica correctamente todos los ejemplos de AND.

4. **Relación con la geometría:** El punto $(1,1)$ yace exactamente sobre la frontera de decisión ($z = 0$), lo que significa que el perceptrón clasifica este punto como 1 con margen cero. En la práctica, se prefieren soluciones con un margen más amplio, lo que motiva el uso de métodos como las máquinas de vectores de soporte (SVM) y técnicas de regularización.

### 1.5.6 Resumen y conexión con las secciones posteriores

En esta sección hemos establecido los cimientos sobre los cuales se construirá todo el tutorial. Los conceptos clave introducidos son:

- La **neurona artificial** como unidad computacional que calcula $y = f(\mathbf{w}^T \mathbf{x} + b)$.
- Las **funciones de activación** que introducen no linealidad, desde la función escalón hasta las modernas GELU y Swish.
- El **descenso de gradiente** como mecanismo de aprendizaje, que ajusta iterativamente los parámetros para minimizar una función de pérdida.
- Las **funciones de pérdida** (MSE, entropía cruzada) que cuantifican la discrepancia entre predicciones y valores verdaderos.

En la siguiente sección, extenderemos estos conceptos al **perceptrón multicapa** (*Multi-Layer Perceptron*, MLP), donde múltiples neuronas se organizan en capas sucesivas. Introduciremos el algoritmo de **retropropagación** (*backpropagation*), que permite calcular eficientemente los gradientes en redes de múltiples capas mediante la regla de la cadena del cálculo diferencial. Este paso es esencial para el entrenamiento de las arquitecturas profundas que sustentan los sistemas de comunicación semántica modernos, incluyendo los autoencoders que implementan la codificación conjunta de fuente y canal.

---

*Fin de la Sección 1.*

---

# 2. El Perceptrón Multicapa (MLP)

El perceptrón multicapa (*Multilayer Perceptron*, MLP) constituye una de las arquitecturas fundamentales del aprendizaje profundo y, en sentido estricto, la primera extensión práctica del perceptrón simple propuesto por Rosenblatt en 1958. Mientras que el perceptrón simple es capaz de resolver únicamente problemas linealmente separables, el MLP incorpora una o más capas ocultas de neuronas con funciones de activación no lineales, lo que le confiere la capacidad teórica de aproximar cualquier función continua definida sobre un subconjunto compacto de $\mathbb{R}^n$, resultado conocido como el *Teorema de Aproximación Universal* (Hornik, 1991, DOI: 10.1016/0893-6080(91)90009-T). En el contexto de las comunicaciones semánticas, los MLPs sirven como bloques constructivos esenciales dentro de codificadores y decodificadores semánticos, módulos de estimación de canal y componentes de sistemas extremo a extremo (*end-to-end*). Comprender su funcionamiento interno —desde la propagación hacia adelante hasta la retropropagación del error— es requisito indispensable para abordar arquitecturas más avanzadas como las redes convolucionales, recurrentes y los transformadores.

En esta sección se presenta la arquitectura del MLP, el algoritmo de retropropagación, las funciones de pérdida más utilizadas, los principales optimizadores, las técnicas de regularización y un ejemplo práctico completo de clasificación binaria implementado en PyTorch.

---

## 2.1 Arquitectura del MLP

### 2.1.1 Estructura general

Un perceptrón multicapa es una red neuronal artificial *feedforward* (de propagación hacia adelante) compuesta por múltiples capas de neuronas organizadas de forma jerárquica. La información fluye en una única dirección: desde la capa de entrada, a través de una o más capas ocultas, hasta la capa de salida. No existen conexiones recurrentes ni retroalimentación entre capas, lo cual distingue al MLP de las redes recurrentes que se estudiarán en secciones posteriores.

Formalmente, un MLP con $L$ capas se define mediante la siguiente estructura:

1. **Capa de entrada (capa 0):** Recibe el vector de características $\mathbf{x} \in \mathbb{R}^{n^{(0)}}$, donde $n^{(0)}$ denota la dimensionalidad del espacio de entrada. Esta capa no realiza ningún cómputo; simplemente distribuye los valores de entrada hacia las neuronas de la primera capa oculta. En el contexto de comunicaciones, $\mathbf{x}$ podría representar una señal recibida, un vector de símbolos modulados o una representación semántica de un mensaje.

2. **Capas ocultas (capas $1, 2, \ldots, L-1$):** Cada capa oculta $l$ contiene $n^{(l)}$ neuronas que aplican una transformación afín seguida de una función de activación no lineal. Estas capas son responsables de extraer representaciones intermedias (*features*) de complejidad creciente. La profundidad de la red (número de capas ocultas) y la anchura de cada capa (número de neuronas $n^{(l)}$) son hiperparámetros de diseño.

3. **Capa de salida (capa $L$):** Produce la predicción final $\hat{\mathbf{y}} \in \mathbb{R}^{n^{(L)}}$. La dimensión $n^{(L)}$ y la función de activación de esta capa dependen del tipo de problema: una neurona con activación sigmoide para clasificación binaria, $K$ neuronas con activación *softmax* para clasificación multiclase con $K$ categorías, o $n^{(L)}$ neuronas con activación lineal (identidad) para problemas de regresión.

### 2.1.2 Capas totalmente conectadas (densas)

En un MLP, cada capa es una capa *totalmente conectada* o *densa* (*fully connected* o *dense layer*), lo que significa que cada neurona de la capa $l$ está conectada con todas las neuronas de la capa $l-1$. Esto implica que la cantidad de parámetros entre dos capas consecutivas es $n^{(l)} \times n^{(l-1)}$ pesos más $n^{(l)}$ sesgos (*biases*), resultando en un total de $n^{(l)} \times (n^{(l-1)} + 1)$ parámetros por capa.

Esta conectividad completa permite al MLP capturar interacciones complejas entre todas las componentes de la entrada, pero también implica un crecimiento cuadrático del número de parámetros con respecto al tamaño de las capas. Esta limitación motivará, en secciones posteriores, el estudio de arquitecturas con conectividad estructurada como las redes convolucionales.

### 2.1.3 Notación formal

Para describir de manera precisa las operaciones del MLP, adoptamos la siguiente notación que se utilizará de forma consistente a lo largo de este tutorial:

- $L$: número total de capas (sin contar la capa de entrada). Un MLP con una capa oculta tiene $L = 2$.
- $l \in \{1, 2, \ldots, L\}$: índice de capa.
- $n^{(l)}$: número de neuronas en la capa $l$. En particular, $n^{(0)}$ es la dimensión de la entrada.
- $\mathbf{W}^{(l)} \in \mathbb{R}^{n^{(l)} \times n^{(l-1)}}$: matriz de pesos de la capa $l$. El elemento $W_{ij}^{(l)}$ representa el peso de la conexión desde la neurona $j$ de la capa $l-1$ hasta la neurona $i$ de la capa $l$.
- $\mathbf{b}^{(l)} \in \mathbb{R}^{n^{(l)}}$: vector de sesgos (*biases*) de la capa $l$.
- $\mathbf{z}^{(l)} \in \mathbb{R}^{n^{(l)}}$: vector de pre-activaciones de la capa $l$ (salida de la transformación afín, antes de aplicar la función de activación).
- $\mathbf{a}^{(l)} \in \mathbb{R}^{n^{(l)}}$: vector de activaciones de la capa $l$ (salida después de aplicar la función de activación). Se define $\mathbf{a}^{(0)} = \mathbf{x}$ para la capa de entrada.
- $f(\cdot)$: función de activación (puede variar entre capas, en cuyo caso se escribe $f^{(l)}(\cdot)$).

### 2.1.4 Propagación hacia adelante (*Forward Pass*)

La propagación hacia adelante describe el proceso mediante el cual un vector de entrada $\mathbf{x}$ es transformado sucesivamente por cada capa de la red hasta producir la salida $\hat{\mathbf{y}}$. Para cada capa $l = 1, 2, \ldots, L$, se realizan dos operaciones:

**Paso 1 — Transformación afín:** Se calcula la combinación lineal ponderada de las activaciones de la capa anterior más el sesgo:

$$\mathbf{z}^{(l)} = \mathbf{W}^{(l)} \mathbf{a}^{(l-1)} + \mathbf{b}^{(l)}$$

donde $\mathbf{W}^{(l)} \in \mathbb{R}^{n^{(l)} \times n^{(l-1)}}$ es la matriz de pesos, $\mathbf{a}^{(l-1)} \in \mathbb{R}^{n^{(l-1)}}$ es el vector de activaciones de la capa previa y $\mathbf{b}^{(l)} \in \mathbb{R}^{n^{(l)}}$ es el vector de sesgos. El vector resultante $\mathbf{z}^{(l)} \in \mathbb{R}^{n^{(l)}}$ se denomina *pre-activación* o *logit*.

En forma componente a componente, la pre-activación de la neurona $i$ en la capa $l$ se escribe como:

$$z_i^{(l)} = \sum_{j=1}^{n^{(l-1)}} W_{ij}^{(l)} a_j^{(l-1)} + b_i^{(l)}$$

Esta expresión es simplemente un producto punto entre la fila $i$ de la matriz de pesos y el vector de activaciones de la capa anterior, más el sesgo correspondiente.

**Paso 2 — Activación no lineal:** Se aplica la función de activación elemento a elemento:

$$\mathbf{a}^{(l)} = f(\mathbf{z}^{(l)})$$

o equivalentemente, $a_i^{(l)} = f(z_i^{(l)})$ para cada neurona $i$. La función de activación introduce la no linealidad necesaria para que la red pueda representar funciones complejas. Sin ella, la composición de transformaciones afines seguiría siendo una transformación afín, y el MLP sería equivalente a una regresión lineal independientemente de su profundidad.

La propagación completa se resume como la composición:

$$\hat{\mathbf{y}} = \mathbf{a}^{(L)} = f^{(L)}\left(\mathbf{W}^{(L)} f^{(L-1)}\left(\cdots f^{(1)}\left(\mathbf{W}^{(1)} \mathbf{x} + \mathbf{b}^{(1)}\right) \cdots\right) + \mathbf{b}^{(L)}\right)$$

Las funciones de activación más comunes ya fueron presentadas en la Sección 1. En resumen, las capas ocultas suelen emplear ReLU ($f(z) = \max(0, z)$) o variantes como Leaky ReLU o GELU, mientras que la capa de salida utiliza la activación apropiada al problema: sigmoide para clasificación binaria, softmax para clasificación multiclase, o identidad para regresión.

### 2.1.5 Diagrama de un MLP de tres capas

**Figura 2.1:** *Diagrama esquemático de un perceptrón multicapa con tres capas: una capa de entrada con $n^{(0)} = 3$ neuronas (representadas como nodos circulares en la columna izquierda, etiquetados como $x_1$, $x_2$, $x_3$), una capa oculta con $n^{(1)} = 4$ neuronas (nodos en la columna central, etiquetados como $a_1^{(1)}$, $a_2^{(1)}$, $a_3^{(1)}$, $a_4^{(1)}$) y una capa de salida con $n^{(2)} = 2$ neuronas (nodos en la columna derecha, etiquetados como $\hat{y}_1$, $\hat{y}_2$). Cada neurona de la capa de entrada está conectada mediante flechas dirigidas a todas las neuronas de la capa oculta; estas flechas representan los pesos $W_{ij}^{(1)}$. Análogamente, cada neurona de la capa oculta está conectada con todas las neuronas de la capa de salida mediante flechas con pesos $W_{ij}^{(2)}$. Debajo de cada capa oculta y de salida se indica el sesgo $\mathbf{b}^{(l)}$ como una entrada adicional constante. Las flechas fluyen de izquierda a derecha, ilustrando la propagación hacia adelante de la información. A la derecha de cada neurona oculta se anota la función de activación $f(\cdot)$, y al lado de las neuronas de salida se indica la activación de salida (por ejemplo, softmax). El diagrama resalta la conectividad completa entre capas adyacentes y la ausencia de conexiones dentro de una misma capa o entre capas no adyacentes.*

### 2.1.6 Ejemplo numérico detallado

Consideremos un MLP sencillo con la siguiente arquitectura:
- **Capa de entrada:** $n^{(0)} = 2$ (dos características de entrada)
- **Capa oculta:** $n^{(1)} = 2$ (dos neuronas con activación sigmoide)
- **Capa de salida:** $n^{(2)} = 1$ (una neurona con activación sigmoide, para clasificación binaria)

Definamos los siguientes parámetros:

$$\mathbf{W}^{(1)} = \begin{pmatrix} 0.15 & 0.20 \\ 0.25 & 0.30 \end{pmatrix}, \quad \mathbf{b}^{(1)} = \begin{pmatrix} 0.35 \\ 0.35 \end{pmatrix}$$

$$\mathbf{W}^{(2)} = \begin{pmatrix} 0.40 & 0.45 \end{pmatrix}, \quad b^{(2)} = 0.60$$

Y sea el vector de entrada:

$$\mathbf{x} = \mathbf{a}^{(0)} = \begin{pmatrix} 0.05 \\ 0.10 \end{pmatrix}$$

La función de activación utilizada en todas las capas es la sigmoide:

$$\sigma(z) = \frac{1}{1 + e^{-z}}$$

**Paso 1: Cálculo de las pre-activaciones de la capa oculta**

$$\mathbf{z}^{(1)} = \mathbf{W}^{(1)} \mathbf{a}^{(0)} + \mathbf{b}^{(1)}$$

Desarrollando componente a componente:

$$z_1^{(1)} = W_{11}^{(1)} \cdot a_1^{(0)} + W_{12}^{(1)} \cdot a_2^{(0)} + b_1^{(1)}$$
$$z_1^{(1)} = 0.15 \times 0.05 + 0.20 \times 0.10 + 0.35 = 0.0075 + 0.0200 + 0.35 = 0.3775$$

$$z_2^{(1)} = W_{21}^{(1)} \cdot a_1^{(0)} + W_{22}^{(1)} \cdot a_2^{(0)} + b_2^{(1)}$$
$$z_2^{(1)} = 0.25 \times 0.05 + 0.30 \times 0.10 + 0.35 = 0.0125 + 0.0300 + 0.35 = 0.3925$$

**Paso 2: Cálculo de las activaciones de la capa oculta**

$$a_1^{(1)} = \sigma(z_1^{(1)}) = \sigma(0.3775) = \frac{1}{1 + e^{-0.3775}} = \frac{1}{1 + 0.6856} = \frac{1}{1.6856} \approx 0.5933$$

$$a_2^{(1)} = \sigma(z_2^{(1)}) = \sigma(0.3925) = \frac{1}{1 + e^{-0.3925}} = \frac{1}{1 + 0.6753} = \frac{1}{1.6753} \approx 0.5969$$

**Paso 3: Cálculo de la pre-activación de la capa de salida**

$$z^{(2)} = \mathbf{W}^{(2)} \mathbf{a}^{(1)} + b^{(2)}$$
$$z^{(2)} = 0.40 \times 0.5933 + 0.45 \times 0.5969 + 0.60$$
$$z^{(2)} = 0.2373 + 0.2686 + 0.60 = 1.1059$$

**Paso 4: Cálculo de la activación de la capa de salida**

$$\hat{y} = a^{(2)} = \sigma(z^{(2)}) = \sigma(1.1059) = \frac{1}{1 + e^{-1.1059}} = \frac{1}{1 + 0.3313} \approx 0.7514$$

La red predice $\hat{y} \approx 0.7514$. Si la etiqueta verdadera fuera $y = 1$ (clase positiva), la red estaría acercándose al valor correcto pero aún no es precisa. Si la etiqueta fuera $y = 0$, la predicción sería bastante errónea. En la subsección siguiente, veremos cómo el algoritmo de retropropagación calcula los gradientes necesarios para ajustar los pesos y reducir el error.

Este ejemplo, aunque sencillo, ilustra la mecánica fundamental del *forward pass*: cada capa toma las activaciones de la capa anterior, aplica una transformación afín (producto matricial más sesgo) y luego una no linealidad. La composición de estas operaciones permite a la red construir funciones de decisión complejas a partir de operaciones elementales.

---

## 2.2 Retropropagación del error (*Backpropagation*)

### 2.2.1 Motivación y contexto histórico

El algoritmo de retropropagación del error (*backpropagation*), popularizado por Rumelhart, Hinton y Williams (1986, DOI: 10.1038/323533a0), es el mecanismo central mediante el cual las redes neuronales aprenden. Su objetivo es calcular de manera eficiente el gradiente de la función de pérdida con respecto a cada uno de los parámetros de la red (pesos y sesgos), de modo que estos puedan ser actualizados en la dirección que reduce el error.

En esencia, la retropropagación es una aplicación sistemática de la **regla de la cadena** del cálculo diferencial multivariable. El nombre "retropropagación" refleja el hecho de que los gradientes se calculan comenzando desde la capa de salida y propagándose hacia atrás (*backward*) a través de la red, capa por capa, hasta la capa de entrada.

### 2.2.2 La regla de la cadena en detalle

Recordemos que la regla de la cadena establece que si $y = f(g(x))$, entonces:

$$\frac{dy}{dx} = \frac{dy}{dg} \cdot \frac{dg}{dx} = f'(g(x)) \cdot g'(x)$$

En el contexto de una red neuronal, queremos calcular $\frac{\partial L}{\partial W_{ij}^{(l)}}$ para cada peso $W_{ij}^{(l)}$ de la red, donde $L$ es la función de pérdida. Dado que la pérdida depende de la salida de la red, que a su vez depende de las activaciones de las capas intermedias, que dependen de las pre-activaciones, que dependen de los pesos, la regla de la cadena nos permite descomponer esta derivada en un producto de derivadas parciales más simples:

$$\frac{\partial L}{\partial W_{ij}^{(l)}} = \frac{\partial L}{\partial z_i^{(l)}} \cdot \frac{\partial z_i^{(l)}}{\partial W_{ij}^{(l)}}$$

Para simplificar la notación, definimos el **error local** o **delta** de la neurona $i$ en la capa $l$ como:

$$\delta_i^{(l)} \equiv \frac{\partial L}{\partial z_i^{(l)}}$$

Este término $\delta_i^{(l)}$ cuantifica cuánto contribuye la pre-activación $z_i^{(l)}$ al error total. En notación vectorial, el vector de deltas de la capa $l$ es:

$$\boldsymbol{\delta}^{(l)} = \frac{\partial L}{\partial \mathbf{z}^{(l)}} \in \mathbb{R}^{n^{(l)}}$$

La clave de la retropropagación es que los deltas pueden calcularse de forma recursiva, comenzando por la capa de salida y retrocediendo hacia la entrada.

### 2.2.3 Cálculo de los deltas

**Delta de la capa de salida ($l = L$):**

Para la capa de salida, el delta se calcula directamente a partir de la derivada de la función de pérdida con respecto a las activaciones de salida y la derivada de la función de activación:

$$\boldsymbol{\delta}^{(L)} = \frac{\partial L}{\partial \mathbf{a}^{(L)}} \odot f'(\mathbf{z}^{(L)})$$

donde $\odot$ denota el producto de Hadamard (producto elemento a elemento) y $f'(\mathbf{z}^{(L)})$ es la derivada de la función de activación evaluada en las pre-activaciones de la capa de salida. Este resultado se obtiene aplicando la regla de la cadena:

$$\delta_i^{(L)} = \frac{\partial L}{\partial a_i^{(L)}} \cdot \frac{\partial a_i^{(L)}}{\partial z_i^{(L)}} = \frac{\partial L}{\partial a_i^{(L)}} \cdot f'(z_i^{(L)})$$

La forma específica de $\frac{\partial L}{\partial a_i^{(L)}}$ depende de la función de pérdida utilizada. Por ejemplo, para el error cuadrático medio, esta derivada es proporcional a $(a_i^{(L)} - y_i)$; para la entropía cruzada combinada con una activación sigmoide o softmax, la expresión se simplifica notablemente, como veremos más adelante.

**Delta de las capas ocultas ($l = L-1, L-2, \ldots, 1$):**

Para las capas ocultas, el delta se calcula de forma recursiva a partir de los deltas de la capa siguiente:

$$\boldsymbol{\delta}^{(l)} = \left(\mathbf{W}^{(l+1)}\right)^T \boldsymbol{\delta}^{(l+1)} \odot f'(\mathbf{z}^{(l)})$$

Esta ecuación es el corazón de la retropropagación. Vamos a desglosarla:

1. $\boldsymbol{\delta}^{(l+1)} \in \mathbb{R}^{n^{(l+1)}}$: el vector de deltas de la capa siguiente, que ya fue calculado en la iteración anterior del algoritmo (o directamente si $l+1 = L$).

2. $\left(\mathbf{W}^{(l+1)}\right)^T \in \mathbb{R}^{n^{(l)} \times n^{(l+1)}}$: la transpuesta de la matriz de pesos de la capa siguiente. Este producto $\left(\mathbf{W}^{(l+1)}\right)^T \boldsymbol{\delta}^{(l+1)}$ distribuye (*propaga hacia atrás*) el error de la capa $l+1$ hacia cada neurona de la capa $l$, ponderado por los pesos de las conexiones. Intuitivamente, si el peso $W_{ji}^{(l+1)}$ es grande, entonces la neurona $i$ de la capa $l$ tiene una gran influencia sobre la neurona $j$ de la capa $l+1$, y por tanto hereda una porción proporcional de su error.

3. $f'(\mathbf{z}^{(l)})$: la derivada de la función de activación evaluada en las pre-activaciones de la capa $l$. Este factor modula el error retropropagado según la "sensibilidad" local de la activación. Si la neurona está en una zona de saturación (por ejemplo, en los extremos de la sigmoide, donde $f'(z) \approx 0$), el gradiente se atenúa fuertemente, fenómeno conocido como **desvanecimiento del gradiente** (*vanishing gradient*).

4. $\odot$: el producto de Hadamard garantiza que la modulación se realice elemento a elemento, pues cada neurona tiene su propia pre-activación.

En forma componente a componente, la ecuación recursiva se escribe:

$$\delta_i^{(l)} = \left(\sum_{j=1}^{n^{(l+1)}} W_{ji}^{(l+1)} \delta_j^{(l+1)}\right) \cdot f'(z_i^{(l)})$$

Esta expresión muestra que el delta de la neurona $i$ en la capa $l$ es la suma ponderada de los deltas de todas las neuronas de la capa $l+1$ (ponderada por los pesos de las conexiones), multiplicada por la derivada local de la activación.

### 2.2.4 Gradientes de los pesos y sesgos

Una vez calculados todos los deltas, los gradientes de la función de pérdida con respecto a los pesos y sesgos se obtienen directamente:

**Gradiente respecto a los pesos:**

$$\frac{\partial L}{\partial \mathbf{W}^{(l)}} = \boldsymbol{\delta}^{(l)} \left(\mathbf{a}^{(l-1)}\right)^T$$

donde $\boldsymbol{\delta}^{(l)} \in \mathbb{R}^{n^{(l)}}$ y $\left(\mathbf{a}^{(l-1)}\right)^T \in \mathbb{R}^{1 \times n^{(l-1)}}$, de modo que el producto exterior resulta en una matriz de dimensiones $n^{(l)} \times n^{(l-1)}$, que son exactamente las mismas dimensiones que $\mathbf{W}^{(l)}$. En forma componente a componente:

$$\frac{\partial L}{\partial W_{ij}^{(l)}} = \delta_i^{(l)} \cdot a_j^{(l-1)}$$

Esta expresión tiene una interpretación elegante: el gradiente de un peso es el producto del error de la neurona destino por la activación de la neurona origen. Si ambos valores son grandes, el peso tiene una gran influencia en el error y debe ser ajustado significativamente.

**Gradiente respecto a los sesgos:**

$$\frac{\partial L}{\partial \mathbf{b}^{(l)}} = \boldsymbol{\delta}^{(l)}$$

Es decir, el gradiente del sesgo es simplemente el delta correspondiente. Esto se debe a que $\frac{\partial z_i^{(l)}}{\partial b_i^{(l)}} = 1$, ya que el sesgo aparece como un sumando aditivo en la pre-activación.

### 2.2.5 Algoritmo completo de retropropagación

El algoritmo completo se puede resumir en los siguientes pasos:

1. **Propagación hacia adelante:** Para $l = 1, 2, \ldots, L$, calcular $\mathbf{z}^{(l)} = \mathbf{W}^{(l)} \mathbf{a}^{(l-1)} + \mathbf{b}^{(l)}$ y $\mathbf{a}^{(l)} = f(\mathbf{z}^{(l)})$. Almacenar todos los valores intermedios $\mathbf{z}^{(l)}$ y $\mathbf{a}^{(l)}$.

2. **Cálculo del delta de la capa de salida:** $\boldsymbol{\delta}^{(L)} = \frac{\partial L}{\partial \mathbf{a}^{(L)}} \odot f'(\mathbf{z}^{(L)})$.

3. **Retropropagación de los deltas:** Para $l = L-1, L-2, \ldots, 1$, calcular $\boldsymbol{\delta}^{(l)} = \left(\mathbf{W}^{(l+1)}\right)^T \boldsymbol{\delta}^{(l+1)} \odot f'(\mathbf{z}^{(l)})$.

4. **Cálculo de los gradientes:** Para cada capa $l$, calcular $\frac{\partial L}{\partial \mathbf{W}^{(l)}} = \boldsymbol{\delta}^{(l)} \left(\mathbf{a}^{(l-1)}\right)^T$ y $\frac{\partial L}{\partial \mathbf{b}^{(l)}} = \boldsymbol{\delta}^{(l)}$.

5. **Actualización de parámetros:** Aplicar la regla de actualización del optimizador (por ejemplo, descenso de gradiente: $\mathbf{W}^{(l)} \leftarrow \mathbf{W}^{(l)} - \eta \frac{\partial L}{\partial \mathbf{W}^{(l)}}$).

### 2.2.6 Ejemplo numérico completo de retropropagación

Continuemos con el ejemplo de la Subsección 2.1.6. Recordemos los resultados del *forward pass*:

- Entrada: $\mathbf{x} = (0.05, 0.10)^T$
- Activaciones de la capa oculta: $a_1^{(1)} = 0.5933$, $a_2^{(1)} = 0.5969$
- Pre-activaciones de la capa oculta: $z_1^{(1)} = 0.3775$, $z_2^{(1)} = 0.3925$
- Pre-activación de la salida: $z^{(2)} = 1.1059$
- Salida: $\hat{y} = a^{(2)} = 0.7514$

Supongamos que la etiqueta verdadera es $y = 1$ y utilizamos la función de pérdida de **error cuadrático medio** (para una sola muestra):

$$L = \frac{1}{2}(y - \hat{y})^2 = \frac{1}{2}(1 - 0.7514)^2 = \frac{1}{2}(0.2486)^2 = \frac{1}{2}(0.0618) = 0.0309$$

Nota: usamos el factor $\frac{1}{2}$ en lugar de $\frac{1}{N}$ para simplificar las derivadas.

**Paso 1: Delta de la capa de salida**

$$\delta^{(2)} = \frac{\partial L}{\partial a^{(2)}} \cdot f'(z^{(2)})$$

La derivada de la pérdida MSE (con factor $\frac{1}{2}$) respecto a la activación de salida:

$$\frac{\partial L}{\partial a^{(2)}} = -(y - \hat{y}) = -(1 - 0.7514) = -0.2486$$

La derivada de la sigmoide es $\sigma'(z) = \sigma(z)(1 - \sigma(z))$:

$$f'(z^{(2)}) = \sigma'(1.1059) = 0.7514 \times (1 - 0.7514) = 0.7514 \times 0.2486 = 0.1868$$

Por lo tanto:

$$\delta^{(2)} = -0.2486 \times 0.1868 = -0.0464$$

El signo negativo indica que la pre-activación debería *aumentar* para reducir el error (la salida actual es menor que el valor objetivo).

**Paso 2: Gradientes de $\mathbf{W}^{(2)}$ y $b^{(2)}$**

$$\frac{\partial L}{\partial W_{11}^{(2)}} = \delta^{(2)} \cdot a_1^{(1)} = -0.0464 \times 0.5933 = -0.0275$$

$$\frac{\partial L}{\partial W_{12}^{(2)}} = \delta^{(2)} \cdot a_2^{(1)} = -0.0464 \times 0.5969 = -0.0277$$

$$\frac{\partial L}{\partial b^{(2)}} = \delta^{(2)} = -0.0464$$

**Paso 3: Deltas de la capa oculta**

$$\boldsymbol{\delta}^{(1)} = \left(\mathbf{W}^{(2)}\right)^T \delta^{(2)} \odot f'(\mathbf{z}^{(1)})$$

Primero, calculamos $\left(\mathbf{W}^{(2)}\right)^T \delta^{(2)}$:

$$\left(\mathbf{W}^{(2)}\right)^T \delta^{(2)} = \begin{pmatrix} 0.40 \\ 0.45 \end{pmatrix} \times (-0.0464) = \begin{pmatrix} -0.0186 \\ -0.0209 \end{pmatrix}$$

Ahora calculamos las derivadas de la sigmoide para la capa oculta:

$$f'(z_1^{(1)}) = \sigma(0.3775)(1 - \sigma(0.3775)) = 0.5933 \times 0.4067 = 0.2413$$

$$f'(z_2^{(1)}) = \sigma(0.3925)(1 - \sigma(0.3925)) = 0.5969 \times 0.4031 = 0.2406$$

Aplicamos el producto de Hadamard:

$$\delta_1^{(1)} = -0.0186 \times 0.2413 = -0.0045$$

$$\delta_2^{(1)} = -0.0209 \times 0.2406 = -0.0050$$

**Paso 4: Gradientes de $\mathbf{W}^{(1)}$ y $\mathbf{b}^{(1)}$**

$$\frac{\partial L}{\partial W_{11}^{(1)}} = \delta_1^{(1)} \cdot a_1^{(0)} = -0.0045 \times 0.05 = -0.000225$$

$$\frac{\partial L}{\partial W_{12}^{(1)}} = \delta_1^{(1)} \cdot a_2^{(0)} = -0.0045 \times 0.10 = -0.000450$$

$$\frac{\partial L}{\partial W_{21}^{(1)}} = \delta_2^{(1)} \cdot a_1^{(0)} = -0.0050 \times 0.05 = -0.000250$$

$$\frac{\partial L}{\partial W_{22}^{(1)}} = \delta_2^{(1)} \cdot a_2^{(0)} = -0.0050 \times 0.10 = -0.000500$$

$$\frac{\partial L}{\partial \mathbf{b}^{(1)}} = \boldsymbol{\delta}^{(1)} = \begin{pmatrix} -0.0045 \\ -0.0050 \end{pmatrix}$$

**Paso 5: Actualización de pesos (con tasa de aprendizaje $\eta = 0.5$)**

$$W_{11}^{(2)} \leftarrow 0.40 - 0.5 \times (-0.0275) = 0.40 + 0.0138 = 0.4138$$

$$W_{12}^{(2)} \leftarrow 0.45 - 0.5 \times (-0.0277) = 0.45 + 0.0139 = 0.4639$$

$$b^{(2)} \leftarrow 0.60 - 0.5 \times (-0.0464) = 0.60 + 0.0232 = 0.6232$$

Y de manera análoga para los pesos de la capa oculta. Obsérvese cómo todos los gradientes son negativos (porque la salida debe aumentar para acercarse a $y=1$), lo que hace que los pesos *aumenten* tras la actualización, incrementando así la salida de la red en la dirección correcta.

### 2.2.7 Diagrama del flujo de gradientes

**Figura 2.2:** *Diagrama del flujo de gradientes en la retropropagación para el MLP de dos capas del ejemplo. La parte superior muestra la propagación hacia adelante (de izquierda a derecha): la entrada $\mathbf{x}$ fluye a través de $\mathbf{W}^{(1)}$, pasa por la función de activación $\sigma(\cdot)$ para producir $\mathbf{a}^{(1)}$, luego a través de $\mathbf{W}^{(2)}$ y $\sigma(\cdot)$ para producir $\hat{y}$, y finalmente se compara con $y$ mediante la función de pérdida $L$. La parte inferior muestra la retropropagación (de derecha a izquierda): desde $L$, se calcula $\frac{\partial L}{\partial a^{(2)}}$, luego se multiplica por $f'(z^{(2)})$ para obtener $\delta^{(2)}$, el cual se propaga hacia atrás a través de $(\mathbf{W}^{(2)})^T$ y se modula por $f'(\mathbf{z}^{(1)})$ para obtener $\boldsymbol{\delta}^{(1)}$. En cada etapa, flechas laterales descendentes muestran cómo los deltas se combinan con las activaciones de la capa anterior para producir los gradientes $\frac{\partial L}{\partial \mathbf{W}^{(l)}}$. Las flechas de retropropagación se dibujan en rojo para distinguirlas de las flechas azules de la propagación hacia adelante. Se anotan las dimensiones de cada tensor en cada punto del diagrama.*

---

## 2.3 Funciones de pérdida

La función de pérdida (*loss function*), también denominada función de costo o función objetivo, cuantifica la discrepancia entre las predicciones del modelo $\hat{\mathbf{y}}$ y las etiquetas verdaderas $\mathbf{y}$. La elección de la función de pérdida apropiada es crucial, pues define el paisaje de optimización que el algoritmo de entrenamiento debe navegar. En esta subsección describimos las funciones de pérdida más utilizadas en aprendizaje profundo.

### 2.3.1 Error cuadrático medio (MSE)

El error cuadrático medio (*Mean Squared Error*, MSE) es la función de pérdida estándar para problemas de **regresión**, donde la salida del modelo es un valor continuo. Se define como:

$$L_{\text{MSE}} = \frac{1}{N} \sum_{i=1}^{N} (y_i - \hat{y}_i)^2$$

donde $N$ es el número de muestras en el *batch*, $y_i$ es el valor objetivo para la muestra $i$ y $\hat{y}_i$ es la predicción correspondiente del modelo. El MSE penaliza los errores de forma cuadrática: errores grandes reciben una penalización desproporcionadamente mayor que errores pequeños. Esta propiedad tiene ventajas e inconvenientes. Por un lado, incentiva al modelo a evitar errores grandes; por otro, hace que la pérdida sea sensible a valores atípicos (*outliers*).

La derivada del MSE respecto a una predicción individual es:

$$\frac{\partial L_{\text{MSE}}}{\partial \hat{y}_i} = -\frac{2}{N}(y_i - \hat{y}_i)$$

Esta derivada es proporcional al error residual, lo que da lugar a gradientes que son mayores cuando las predicciones están lejos de los objetivos (actualizaciones más agresivas) y menores cuando las predicciones son cercanas (actualizaciones más finas), un comportamiento deseable para la convergencia.

En comunicaciones semánticas, el MSE se utiliza frecuentemente para medir la fidelidad de la reconstrucción en sistemas que transmiten representaciones continuas, por ejemplo, la calidad de una imagen reconstruida tras la transmisión a través de un canal ruidoso.

Una variante común es la **raíz del error cuadrático medio** (RMSE, $\sqrt{L_{\text{MSE}}}$), que tiene la ventaja de estar en las mismas unidades que la variable objetivo. Otra variante es el **error absoluto medio** (MAE, $\frac{1}{N}\sum |y_i - \hat{y}_i|$), que es más robusto ante outliers pero cuyo gradiente es constante en magnitud, lo que puede dificultar la convergencia cerca del mínimo.

### 2.3.2 Entropía cruzada binaria (BCE)

La entropía cruzada binaria (*Binary Cross-Entropy*, BCE) es la función de pérdida estándar para problemas de **clasificación binaria**, donde la salida del modelo es una probabilidad $\hat{y}_i \in (0, 1)$ de que la muestra pertenezca a la clase positiva. Se define como:

$$L_{\text{BCE}} = -\frac{1}{N} \sum_{i=1}^{N} \left[ y_i \log(\hat{y}_i) + (1 - y_i) \log(1 - \hat{y}_i) \right]$$

donde $y_i \in \{0, 1\}$ es la etiqueta verdadera de la muestra $i$.

Para comprender esta función, analicemos sus dos términos:

- Cuando $y_i = 1$ (la muestra pertenece a la clase positiva), el segundo término se anula y la pérdida es $-\log(\hat{y}_i)$. Si el modelo predice $\hat{y}_i$ cercano a 1 (predicción correcta con alta confianza), $-\log(\hat{y}_i) \approx 0$ (pérdida baja). Si predice $\hat{y}_i$ cercano a 0 (predicción incorrecta), $-\log(\hat{y}_i) \to \infty$ (pérdida muy alta). La función logarítmica penaliza de forma extremadamente severa las predicciones confiantes pero erróneas.

- Cuando $y_i = 0$ (la muestra pertenece a la clase negativa), el primer término se anula y la pérdida es $-\log(1 - \hat{y}_i)$. Análogamente, se penaliza al modelo si predice $\hat{y}_i$ cercano a 1 cuando la clase verdadera es 0.

La derivada de la BCE respecto a una predicción individual es:

$$\frac{\partial L_{\text{BCE}}}{\partial \hat{y}_i} = -\frac{1}{N} \left(\frac{y_i}{\hat{y}_i} - \frac{1 - y_i}{1 - \hat{y}_i}\right)$$

Cuando la capa de salida utiliza una activación sigmoide ($\hat{y}_i = \sigma(z_i)$), la combinación de BCE y sigmoide produce un gradiente particularmente limpio para el delta de la capa de salida:

$$\delta_i^{(L)} = \frac{\partial L_{\text{BCE}}}{\partial z_i} = \frac{1}{N}(\hat{y}_i - y_i)$$

Esta simplificación evita el problema de saturación de la sigmoide en los gradientes y es una de las razones por las que la combinación BCE + sigmoide es preferida sobre MSE + sigmoide para clasificación binaria.

La BCE tiene una interpretación desde la teoría de la información: es la entropía cruzada entre la distribución verdadera $p = (y_i, 1-y_i)$ y la distribución predicha $q = (\hat{y}_i, 1-\hat{y}_i)$. Minimizar la BCE equivale a minimizar la divergencia de Kullback-Leibler entre ambas distribuciones, lo que tiene una conexión directa con la eficiencia de codificación en comunicaciones.

### 2.3.3 Entropía cruzada categórica

Para problemas de **clasificación multiclase** con $K$ clases mutuamente excluyentes, la entropía cruzada categórica (*Categorical Cross-Entropy*, CCE) generaliza la BCE. La etiqueta verdadera se representa como un vector *one-hot* $\mathbf{y}_i \in \{0, 1\}^K$ con $\sum_k y_{ik} = 1$, y la salida del modelo es un vector de probabilidades $\hat{\mathbf{y}}_i \in (0, 1)^K$ con $\sum_k \hat{y}_{ik} = 1$, típicamente obtenido mediante la función softmax:

$$\hat{y}_{ik} = \text{softmax}(z_{ik}) = \frac{e^{z_{ik}}}{\sum_{j=1}^{K} e^{z_{ij}}}$$

La función de pérdida se define como:

$$L_{\text{CCE}} = -\frac{1}{N} \sum_{i=1}^{N} \sum_{k=1}^{K} y_{ik} \log(\hat{y}_{ik})$$

Dado que $\mathbf{y}_i$ es *one-hot*, solo el término correspondiente a la clase verdadera $c_i$ contribuye a la suma sobre $k$:

$$L_{\text{CCE}} = -\frac{1}{N} \sum_{i=1}^{N} \log(\hat{y}_{i, c_i})$$

Es decir, la pérdida mide el logaritmo negativo de la probabilidad asignada por el modelo a la clase correcta. Un modelo perfecto asigna probabilidad 1 a la clase correcta, obteniendo pérdida 0. La combinación de softmax con CCE también produce gradientes limpios:

$$\delta_k^{(L)} = \hat{y}_k - y_k$$

lo que facilita la optimización y evita problemas numéricos.

### 2.3.4 Criterios de selección

La selección de la función de pérdida debe alinearse con la naturaleza del problema:

| Problema | Función de pérdida | Activación de salida |
|---|---|---|
| Regresión | MSE (o MAE, Huber) | Lineal (identidad) |
| Clasificación binaria | Entropía cruzada binaria | Sigmoide |
| Clasificación multiclase | Entropía cruzada categórica | Softmax |
| Clasificación multi-etiqueta | BCE (por cada etiqueta) | Sigmoide (por cada etiqueta) |

En el contexto de las comunicaciones semánticas, la elección de la función de pérdida es particularmente relevante porque define qué aspecto de la información transmitida se prioriza preservar. Un sistema que utiliza MSE prioriza la fidelidad numérica de la reconstrucción, mientras que un sistema con entropía cruzada prioriza la preservación del contenido semántico (categorías, clases). Algunas arquitecturas avanzadas combinan múltiples funciones de pérdida —por ejemplo, un término de reconstrucción MSE más un término de clasificación de entropía cruzada— para balancear fidelidad perceptual y semántica.

---

## 2.4 Optimizadores

Los optimizadores son los algoritmos encargados de ajustar los parámetros $\boldsymbol{\theta} = \{\mathbf{W}^{(l)}, \mathbf{b}^{(l)}\}_{l=1}^{L}$ de la red neuronal con el objetivo de minimizar la función de pérdida $L(\boldsymbol{\theta})$. Todos se basan en el principio del descenso de gradiente, pero difieren en cómo utilizan la información del gradiente para determinar la dirección y magnitud de las actualizaciones.

### 2.4.1 Descenso de gradiente estocástico (SGD)

El descenso de gradiente estocástico (*Stochastic Gradient Descent*, SGD) es la forma más básica de optimización. En el **descenso de gradiente por lotes** (*batch gradient descent*), el gradiente se calcula sobre todo el conjunto de entrenamiento antes de actualizar los parámetros:

$$\boldsymbol{\theta}_{t+1} = \boldsymbol{\theta}_t - \eta \nabla_{\boldsymbol{\theta}} L(\boldsymbol{\theta}_t)$$

donde $\eta > 0$ es la **tasa de aprendizaje** (*learning rate*), un hiperparámetro fundamental que controla el tamaño del paso de actualización, y $\nabla_{\boldsymbol{\theta}} L(\boldsymbol{\theta}_t)$ es el gradiente de la función de pérdida evaluado en los parámetros actuales.

En la versión **estocástica**, el gradiente se estima utilizando un solo ejemplo o un subconjunto pequeño (*mini-batch*) de $B$ ejemplos seleccionados aleatoriamente:

$$\boldsymbol{\theta}_{t+1} = \boldsymbol{\theta}_t - \eta \frac{1}{B} \sum_{i=1}^{B} \nabla_{\boldsymbol{\theta}} L_i(\boldsymbol{\theta}_t)$$

El SGD estocástico introduce ruido en la estimación del gradiente, lo cual puede parecer desventajoso pero en la práctica ofrece varios beneficios: permite un entrenamiento más rápido (no es necesario procesar todo el dataset para cada actualización), puede escapar de mínimos locales superficiales gracias al ruido, y requiere menos memoria.

La elección de la tasa de aprendizaje $\eta$ es crítica:
- Si $\eta$ es demasiado grande, las actualizaciones pueden sobrepasar el mínimo, causando oscilaciones o divergencia.
- Si $\eta$ es demasiado pequeña, la convergencia será extremadamente lenta.
- Un valor típico inicial está en el rango $[10^{-4}, 10^{-1}]$, dependiendo del problema y la arquitectura.

### 2.4.2 SGD con momento (*momentum*)

Una limitación del SGD básico es que puede oscilar en direcciones con curvatura pronunciada del paisaje de pérdida, avanzando lentamente a lo largo de valles estrechos. El **momento** (*momentum*) aborda este problema incorporando una "inercia" que acumula la historia de los gradientes pasados:

$$\mathbf{v}_t = \gamma \mathbf{v}_{t-1} + \eta \nabla_{\boldsymbol{\theta}} L(\boldsymbol{\theta}_t)$$

$$\boldsymbol{\theta}_{t+1} = \boldsymbol{\theta}_t - \mathbf{v}_t$$

donde $\mathbf{v}_t$ es el vector de velocidad y $\gamma \in [0, 1)$ es el coeficiente de momento, típicamente $\gamma = 0.9$.

La velocidad $\mathbf{v}_t$ acumula los gradientes de iteraciones pasadas con un decaimiento exponencial. Si el gradiente apunta consistentemente en la misma dirección, la velocidad crece, acelerando la convergencia (similar a una bola rodando cuesta abajo que gana velocidad). Si el gradiente oscila (cambia de signo frecuentemente), las contribuciones pasadas se cancelan, amortiguando las oscilaciones.

Para visualizar el efecto, expandamos la recurrencia:

$$\mathbf{v}_t = \eta \nabla L(\boldsymbol{\theta}_t) + \gamma \eta \nabla L(\boldsymbol{\theta}_{t-1}) + \gamma^2 \eta \nabla L(\boldsymbol{\theta}_{t-2}) + \cdots$$

Cada gradiente pasado contribuye con un peso que decae exponencialmente ($\gamma^k$ para el gradiente de $k$ pasos atrás). Esto constituye una media móvil exponencialmente ponderada de los gradientes.

Una variante mejorada es el **momento de Nesterov** (*Nesterov Accelerated Gradient*, NAG), que evalúa el gradiente no en la posición actual sino en la posición anticipada $\boldsymbol{\theta}_t - \gamma \mathbf{v}_{t-1}$:

$$\mathbf{v}_t = \gamma \mathbf{v}_{t-1} + \eta \nabla_{\boldsymbol{\theta}} L(\boldsymbol{\theta}_t - \gamma \mathbf{v}_{t-1})$$

$$\boldsymbol{\theta}_{t+1} = \boldsymbol{\theta}_t - \mathbf{v}_t$$

Esta "mirada hacia adelante" permite al optimizador corregir su trayectoria de forma anticipada, lo que acelera la convergencia en la práctica.

### 2.4.3 Adam (*Adaptive Moment Estimation*)

Adam (Kingma y Ba, 2015, DOI: 10.48550/arXiv.1412.6980) es uno de los optimizadores más utilizados en aprendizaje profundo debido a su robustez y buen rendimiento con los hiperparámetros por defecto. Adam combina las ideas del momento (estimación del primer momento del gradiente) con la adaptación individual de la tasa de aprendizaje para cada parámetro (estimación del segundo momento del gradiente).

El algoritmo mantiene dos estadísticas móviles para cada parámetro:

**Primer momento (media del gradiente):**

$$\mathbf{m}_t = \beta_1 \mathbf{m}_{t-1} + (1 - \beta_1) \nabla_{\boldsymbol{\theta}} L(\boldsymbol{\theta}_t)$$

**Segundo momento (media del gradiente al cuadrado):**

$$\mathbf{v}_t = \beta_2 \mathbf{v}_{t-1} + (1 - \beta_2) \left[\nabla_{\boldsymbol{\theta}} L(\boldsymbol{\theta}_t)\right]^2$$

donde el cuadrado se aplica elemento a elemento, y $\beta_1, \beta_2 \in [0, 1)$ son las tasas de decaimiento exponencial. Los valores recomendados son $\beta_1 = 0.9$ y $\beta_2 = 0.999$.

Dado que $\mathbf{m}_0 = \mathbf{0}$ y $\mathbf{v}_0 = \mathbf{0}$ (inicialización en cero), las estimaciones están sesgadas hacia cero, especialmente en las primeras iteraciones. Para corregir este sesgo, se aplica la **corrección de sesgo** (*bias correction*):

$$\hat{\mathbf{m}}_t = \frac{\mathbf{m}_t}{1 - \beta_1^t}$$

$$\hat{\mathbf{v}}_t = \frac{\mathbf{v}_t}{1 - \beta_2^t}$$

donde $\beta_1^t$ y $\beta_2^t$ denotan $\beta_1$ y $\beta_2$ elevados a la potencia $t$ (el número de iteración). En las primeras iteraciones, $1 - \beta_1^t$ es pequeño, por lo que la corrección amplifica las estimaciones; conforme $t$ crece, $\beta_1^t \to 0$ y la corrección se vuelve despreciable.

La regla de actualización de Adam es:

$$\boldsymbol{\theta}_{t+1} = \boldsymbol{\theta}_t - \frac{\eta}{\sqrt{\hat{\mathbf{v}}_t} + \epsilon} \hat{\mathbf{m}}_t$$

donde $\epsilon \approx 10^{-8}$ es una constante pequeña para evitar la división por cero, y las operaciones $\sqrt{\cdot}$ y la división se aplican elemento a elemento.

La interpretación de esta regla es intuitiva:

- **Dirección:** La actualización apunta en la dirección de $\hat{\mathbf{m}}_t$, que es la media suavizada de los gradientes recientes (similar al momento).
- **Magnitud adaptativa:** La magnitud de la actualización para cada parámetro se normaliza por $\sqrt{\hat{\mathbf{v}}_t}$, que estima la desviación estándar del gradiente. Los parámetros con gradientes históricamente grandes reciben actualizaciones más pequeñas, y viceversa. Esto adapta automáticamente la tasa de aprendizaje efectiva a la geometría local del paisaje de pérdida.

En la práctica, Adam funciona bien con la tasa de aprendizaje por defecto $\eta = 10^{-3}$ para la mayoría de los problemas, lo que simplifica la búsqueda de hiperparámetros. Sin embargo, investigaciones recientes han mostrado que SGD con momento bien ajustado puede generalizar mejor que Adam en algunos dominios (como visión por computador con CNNs), mientras que Adam suele ser preferido para modelos de lenguaje y transformadores.

### 2.4.4 Programación de la tasa de aprendizaje (*Learning Rate Scheduling*)

Independientemente del optimizador elegido, la **programación de la tasa de aprendizaje** (*learning rate scheduling*) es una técnica fundamental que ajusta la tasa de aprendizaje $\eta$ durante el entrenamiento según un esquema predefinido o adaptativo. La intuición es utilizar una tasa alta al inicio del entrenamiento (para explorar rápidamente el paisaje de pérdida) y reducirla progresivamente (para refinar la solución cerca del mínimo).

Los esquemas más comunes incluyen:

1. **Decaimiento escalonado (*Step Decay*):** Reduce $\eta$ por un factor constante cada cierto número de épocas:
$$\eta_t = \eta_0 \cdot \gamma^{\lfloor t / s \rfloor}$$
donde $s$ es el intervalo de decaimiento (en épocas) y $\gamma < 1$ es el factor de reducción.

2. **Decaimiento exponencial:** Reduce $\eta$ de forma continua y exponencial:
$$\eta_t = \eta_0 \cdot e^{-\lambda t}$$

3. **Decaimiento coseno (*Cosine Annealing*):** Reduce $\eta$ siguiendo la forma de un coseno:
$$\eta_t = \eta_{\min} + \frac{1}{2}(\eta_0 - \eta_{\min})\left(1 + \cos\left(\frac{\pi t}{T}\right)\right)$$
donde $T$ es el número total de iteraciones y $\eta_{\min}$ es la tasa mínima.

4. **Calentamiento (*Warm-up*):** Incrementa linealmente $\eta$ desde un valor muy pequeño hasta el valor objetivo durante las primeras $T_w$ iteraciones:
$$\eta_t = \eta_0 \cdot \frac{t}{T_w}, \quad t \leq T_w$$
El calentamiento es especialmente importante para optimizadores adaptativos como Adam cuando se entrenan modelos grandes (como transformadores), pues las estimaciones de los momentos son poco fiables en las primeras iteraciones.

5. **Reducción en meseta (*ReduceLROnPlateau*):** Monitoriza una métrica de validación y reduce $\eta$ cuando la métrica deja de mejorar durante un número especificado de épocas (*patience*).

En la práctica, muchos esquemas exitosos combinan un calentamiento inicial seguido de un decaimiento coseno, configuración que se ha convertido en estándar para el entrenamiento de transformadores y modelos de comunicaciones semánticas de extremo a extremo.

---

## 2.5 Regularización

La regularización comprende un conjunto de técnicas diseñadas para prevenir el **sobreajuste** (*overfitting*), que ocurre cuando el modelo aprende los patrones específicos del conjunto de entrenamiento (incluyendo el ruido) en lugar de las relaciones generales subyacentes. Un modelo sobreajustado tiene un rendimiento excelente en los datos de entrenamiento pero pobre en datos nuevos no vistos, es decir, tiene mala capacidad de **generalización**.

### 2.5.1 Sobreajuste vs. subajuste

Para comprender la regularización, es esencial entender el equilibrio entre **sesgo** (*bias*) y **varianza** (*variance*) del modelo:

- **Subajuste (*underfitting*):** El modelo es demasiado simple para capturar los patrones relevantes de los datos. Tiene alto sesgo: comete errores sistemáticos tanto en entrenamiento como en validación. Ejemplo: usar una regresión lineal para datos con relaciones fuertemente no lineales. Se manifiesta como una pérdida de entrenamiento alta que no disminuye significativamente con más entrenamiento.

- **Sobreajuste (*overfitting*):** El modelo es demasiado complejo relativo a la cantidad y complejidad de los datos disponibles. Tiene alta varianza: memoriza los ejemplos de entrenamiento en lugar de aprender patrones generalizables. Se manifiesta como una divergencia entre la pérdida de entrenamiento (que sigue disminuyendo) y la pérdida de validación (que comienza a aumentar en cierto punto). Ejemplo: un MLP con millones de parámetros entrenado con pocos cientos de ejemplos.

El objetivo es encontrar el punto óptimo de **complejidad del modelo** que minimiza el error de generalización. Las técnicas de regularización permiten utilizar modelos de alta capacidad (necesarios para problemas complejos) al tiempo que limitan su tendencia al sobreajuste.

### 2.5.2 Regularización L1 (*Lasso*)

La regularización L1 añade a la función de pérdida un término de penalización proporcional a la suma de los valores absolutos de los pesos:

$$L_{\text{reg}} = L + \lambda \sum_{l} \sum_{i,j} |W_{ij}^{(l)}|$$

donde $\lambda > 0$ es el **hiperparámetro de regularización** que controla la intensidad de la penalización. El término $\lambda \sum |W_{ij}^{(l)}|$ corresponde a la norma $\ell_1$ del vector de pesos.

La regularización L1 tiene una propiedad notable: tiende a llevar muchos pesos exactamente a cero, produciendo modelos **dispersos** (*sparse*). Esto ocurre porque el subdgradiente de $|w|$ tiene magnitud constante (no decrece conforme $w \to 0$, a diferencia de L2), por lo que la fuerza de regularización sigue "empujando" el peso hacia cero incluso cuando este es muy pequeño. Esta propiedad convierte a L1 en una técnica de **selección de características**, ya que las neuronas cuyos pesos se anulan quedan efectivamente desactivadas.

El gradiente del término de regularización L1 (en realidad, un subgradiente, ya que $|w|$ no es diferenciable en $w = 0$) es:

$$\frac{\partial}{\partial W_{ij}^{(l)}} \lambda |W_{ij}^{(l)}| = \lambda \cdot \text{sign}(W_{ij}^{(l)})$$

donde $\text{sign}(\cdot)$ es la función signo.

### 2.5.3 Regularización L2 (*Ridge* o *Weight Decay*)

La regularización L2 añade un término proporcional a la suma de los cuadrados de los pesos:

$$L_{\text{reg}} = L + \frac{\lambda}{2} \sum_{l} \sum_{i,j} (W_{ij}^{(l)})^2$$

El factor $\frac{1}{2}$ se incluye por conveniencia matemática, ya que simplifica la derivada. Este término corresponde al cuadrado de la norma $\ell_2$ del vector de pesos (norma de Frobenius para matrices).

El gradiente del término de regularización L2 es:

$$\frac{\partial}{\partial W_{ij}^{(l)}} \frac{\lambda}{2} (W_{ij}^{(l)})^2 = \lambda W_{ij}^{(l)}$$

Este gradiente es proporcional al peso actual, lo que significa que la fuerza de regularización es mayor para pesos grandes y menor para pesos pequeños. A diferencia de L1, L2 no produce pesos exactamente iguales a cero, sino que los mantiene pequeños. Esto se denomina **decaimiento de pesos** (*weight decay*): en cada iteración, antes de aplicar el gradiente de la pérdida, los pesos se multiplican por un factor $1 - \eta\lambda < 1$:

$$W_{ij}^{(l)} \leftarrow (1 - \eta\lambda) W_{ij}^{(l)} - \eta \frac{\partial L}{\partial W_{ij}^{(l)}}$$

Intuitivamente, la regularización L2 penaliza las soluciones con pesos grandes, favoreciendo funciones más "suaves" y con menor complejidad efectiva. Esto reduce la capacidad del modelo para memorizar ruido, ya que las soluciones que se ajustan al ruido típicamente requieren pesos grandes para producir las oscilaciones necesarias.

### 2.5.4 Dropout

El *dropout* (Srivastava et al., 2014, DOI: 10.5555/2627435.2670313) es una técnica de regularización específica para redes neuronales que consiste en **desactivar aleatoriamente** una fracción de las neuronas de cada capa durante cada iteración de entrenamiento.

Formalmente, durante el entrenamiento, cada neurona de una capa es desactivada (su activación se fija en cero) con probabilidad $p$ (la **tasa de dropout**), independientemente de las demás neuronas. Esto se implementa multiplicando las activaciones por una máscara binaria aleatoria $\mathbf{m}^{(l)} \sim \text{Bernoulli}(1-p)$:

$$\tilde{\mathbf{a}}^{(l)} = \mathbf{m}^{(l)} \odot \mathbf{a}^{(l)}$$

donde $m_i^{(l)} \in \{0, 1\}$ es 1 con probabilidad $1-p$ y 0 con probabilidad $p$, y $\tilde{\mathbf{a}}^{(l)}$ son las activaciones modificadas que se pasan a la siguiente capa. Para compensar el hecho de que se están eliminando neuronas (lo cual reduce la magnitud esperada de las activaciones), las activaciones supervivientes se escalan por $\frac{1}{1-p}$ durante el entrenamiento (*inverted dropout*):

$$\tilde{\mathbf{a}}^{(l)} = \frac{1}{1-p} \mathbf{m}^{(l)} \odot \mathbf{a}^{(l)}$$

Esto garantiza que el valor esperado de $\tilde{\mathbf{a}}^{(l)}$ sea igual al de $\mathbf{a}^{(l)}$, de modo que durante la **inferencia** (evaluación) no se necesita ningún ajuste: simplemente se utilizan todas las neuronas sin dropout.

¿Por qué funciona el dropout? Se pueden ofrecer varias interpretaciones:

1. **Ensamble implícito:** Cada iteración de entrenamiento usa una subred diferente (definida por la máscara aleatoria). Con $n$ neuronas susceptibles de dropout, existen $2^n$ posibles subredes. El entrenamiento con dropout es, en cierto sentido, un entrenamiento simultáneo de un ensamble exponencialmente grande de redes con parámetros compartidos. La predicción final (sin dropout) puede verse como una media ponderada de las predicciones de todas estas subredes.

2. **Reducción de co-adaptaciones:** Sin dropout, las neuronas pueden desarrollar dependencias mutuas complejas: una neurona puede "confiar" en que otra neurona corregirá sus errores. El dropout obliga a cada neurona a ser útil por sí misma, produciendo representaciones más robustas y redundantes.

3. **Inyección de ruido:** El dropout puede verse como una forma de inyectar ruido multiplicativo en las activaciones, lo cual actúa como un regularizador al impedir que el modelo se ajuste demasiado a los datos de entrenamiento.

Los valores típicos de la tasa de dropout $p$ son:
- $p = 0.5$ para capas ocultas (valor por defecto)
- $p = 0.2$ para la capa de entrada (si se aplica dropout a la entrada)
- Para capas más anchas se puede usar $p$ mayor; para capas estrechas, $p$ menor

### 2.5.5 Normalización por lotes (*Batch Normalization*)

La normalización por lotes (*Batch Normalization*, BN), propuesta por Ioffe y Szegedy (2015, DOI: 10.48550/arXiv.1502.03167), es una técnica que normaliza las pre-activaciones de cada capa para que tengan media cero y varianza unitaria dentro de cada mini-batch de entrenamiento. Aunque fue propuesta originalmente como un acelerador de entrenamiento (no como regularizador), tiene un efecto regularizador significativo en la práctica.

Para un mini-batch $\mathcal{B} = \{z_1, z_2, \ldots, z_B\}$ de pre-activaciones de una neurona particular, la normalización por lotes aplica:

**Paso 1 — Calcular estadísticas del batch:**

$$\mu_{\mathcal{B}} = \frac{1}{B} \sum_{i=1}^{B} z_i, \quad \sigma_{\mathcal{B}}^2 = \frac{1}{B} \sum_{i=1}^{B} (z_i - \mu_{\mathcal{B}})^2$$

**Paso 2 — Normalizar:**

$$\hat{z}_i = \frac{z_i - \mu_{\mathcal{B}}}{\sqrt{\sigma_{\mathcal{B}}^2 + \epsilon}}$$

donde $\epsilon \approx 10^{-5}$ es una constante para estabilidad numérica.

**Paso 3 — Escalar y desplazar (parámetros aprendibles):**

$$\tilde{z}_i = \gamma \hat{z}_i + \beta$$

donde $\gamma$ (escala) y $\beta$ (desplazamiento) son parámetros aprendibles que permiten a la red "deshacer" la normalización si esto es beneficioso para la tarea. Sin estos parámetros, la normalización limitaría la capacidad expresiva de la red.

Beneficios de la normalización por lotes:

1. **Permite tasas de aprendizaje más altas:** Al mantener las activaciones en un rango normalizado, se reduce la sensibilidad a la escala de los parámetros, lo que permite usar tasas de aprendizaje más agresivas sin riesgo de inestabilidad.

2. **Acelera la convergencia:** Al reducir el fenómeno de *internal covariate shift* (cambio en la distribución de las activaciones de una capa cuando cambian los parámetros de las capas anteriores), cada capa puede aprender de forma más estable.

3. **Efecto regularizador:** La normalización basada en estadísticas del mini-batch introduce ruido estocástico (las estadísticas varían de un batch a otro), lo que actúa como regularizador y puede reducir la necesidad de dropout.

4. **Reduce la sensibilidad a la inicialización:** Los modelos con BN son menos dependientes de la elección cuidadosa de los pesos iniciales.

Durante la **inferencia**, no se dispone de un mini-batch, por lo que se utilizan medias y varianzas calculadas como medias móviles exponenciales durante el entrenamiento. PyTorch maneja esto automáticamente al alternar entre los modos `model.train()` y `model.eval()`.

---

## 2.6 Ejemplo práctico: Clasificación con MLP

### 2.6.1 Planteamiento del problema

Para consolidar los conceptos presentados en esta sección, implementaremos un clasificador binario basado en un MLP utilizando PyTorch. El problema consiste en predecir si una solicitud de crédito será **aprobada** (clase 1) o **rechazada** (clase 0) a partir de dos características numéricas: el ingreso mensual del solicitante (normalizado) y su puntuación de historial crediticio (normalizada).

Generaremos datos sintéticos que simulan este escenario, entrenaremos un MLP con una capa oculta y evaluaremos su rendimiento. Aunque el problema es sencillo, el código y las técnicas son directamente escalables a problemas reales de mayor complejidad.

### 2.6.2 Implementación en PyTorch

```python
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
import numpy as np

# ============================================================
# 1. Generar datos sintéticos
# ============================================================
# Fijamos la semilla para reproducibilidad
torch.manual_seed(42)
np.random.seed(42)

# Generamos 1000 muestras con 2 características
N = 1000
# Característica 1: ingreso mensual normalizado (media 0, std 1)
# Característica 2: puntuación crediticia normalizada
X = np.random.randn(N, 2).astype(np.float32)

# Regla de decisión: aprobado si 0.5*x1 + 0.8*x2 + ruido > 0
# Esto crea una frontera de decisión lineal con algo de ruido
ruido = 0.3 * np.random.randn(N).astype(np.float32)
y = (0.5 * X[:, 0] + 0.8 * X[:, 1] + ruido > 0).astype(np.float32)

# Convertir a tensores de PyTorch
X_tensor = torch.from_numpy(X)                  # Forma: (1000, 2)
y_tensor = torch.from_numpy(y).unsqueeze(1)      # Forma: (1000, 1)

# Dividir en conjuntos de entrenamiento (80%) y prueba (20%)
N_train = int(0.8 * N)
X_train, X_test = X_tensor[:N_train], X_tensor[N_train:]
y_train, y_test = y_tensor[:N_train], y_tensor[N_train:]

# Crear DataLoaders para iterar sobre mini-batches
# TensorDataset agrupa las características y etiquetas
dataset_train = TensorDataset(X_train, y_train)
# DataLoader gestiona la iteración por mini-batches y el mezclado
train_loader = DataLoader(dataset_train, batch_size=32, shuffle=True)

# ============================================================
# 2. Definir la arquitectura del MLP
# ============================================================
class MLPClasificador(nn.Module):
    """
    Perceptrón multicapa para clasificación binaria.
    Arquitectura: 2 -> 16 -> 8 -> 1
    """
    def __init__(self):
        # Llamar al constructor de nn.Module (obligatorio)
        super(MLPClasificador, self).__init__()

        # Primera capa oculta: 2 entradas -> 16 neuronas
        # nn.Linear implementa la transformación z = Wx + b
        self.capa1 = nn.Linear(in_features=2, out_features=16)

        # Segunda capa oculta: 16 -> 8 neuronas
        self.capa2 = nn.Linear(in_features=16, out_features=8)

        # Capa de salida: 8 -> 1 neurona (clasificación binaria)
        self.salida = nn.Linear(in_features=8, out_features=1)

        # Función de activación ReLU para capas ocultas
        self.relu = nn.ReLU()

        # Activación sigmoide para la salida (probabilidad entre 0 y 1)
        self.sigmoid = nn.Sigmoid()

        # Normalización por lotes para la primera capa oculta
        self.bn1 = nn.BatchNorm1d(num_features=16)

        # Dropout con tasa p=0.3 (desactiva 30% de las neuronas)
        self.dropout = nn.Dropout(p=0.3)

    def forward(self, x):
        """
        Define la propagación hacia adelante.
        x: tensor de entrada con forma (batch_size, 2)
        """
        # Capa 1: transformación afín -> batch norm -> ReLU -> dropout
        x = self.capa1(x)        # z^(1) = W^(1)x + b^(1)
        x = self.bn1(x)          # Normalización por lotes
        x = self.relu(x)         # a^(1) = ReLU(z^(1))
        x = self.dropout(x)      # Dropout (solo activo en entrenamiento)

        # Capa 2: transformación afín -> ReLU
        x = self.capa2(x)        # z^(2) = W^(2)a^(1) + b^(2)
        x = self.relu(x)         # a^(2) = ReLU(z^(2))

        # Capa de salida: transformación afín -> sigmoide
        x = self.salida(x)       # z^(3) = W^(3)a^(2) + b^(3)
        x = self.sigmoid(x)      # y_hat = sigma(z^(3))

        return x

# Instanciar el modelo
modelo = MLPClasificador()

# Verificar la arquitectura
print(modelo)
# Contar el número total de parámetros
total_params = sum(p.numel() for p in modelo.parameters())
print(f"Parámetros totales: {total_params}")

# ============================================================
# 3. Definir la función de pérdida y el optimizador
# ============================================================
# Entropía cruzada binaria (BCE)
# Mide la discrepancia entre la distribución predicha y la real
criterio = nn.BCELoss()

# Optimizador Adam con tasa de aprendizaje 0.001
# y regularización L2 (weight_decay) con lambda = 1e-4
optimizador = optim.Adam(
    modelo.parameters(),
    lr=0.001,
    weight_decay=1e-4    # Regularización L2
)

# Programador de tasa de aprendizaje: reduce lr al 50%
# si la pérdida no mejora en 5 épocas
scheduler = optim.lr_scheduler.ReduceLROnPlateau(
    optimizador,
    mode='min',
    factor=0.5,
    patience=5,
    verbose=True
)

# ============================================================
# 4. Bucle de entrenamiento
# ============================================================
num_epocas = 50

for epoca in range(num_epocas):
    # Activar modo entrenamiento (activa dropout y batch norm)
    modelo.train()

    perdida_acumulada = 0.0
    num_batches = 0

    # Iterar sobre mini-batches
    for X_batch, y_batch in train_loader:
        # --- Propagación hacia adelante ---
        # Calcular las predicciones del modelo
        predicciones = modelo(X_batch)

        # Calcular la pérdida (BCE) entre predicciones y etiquetas
        perdida = criterio(predicciones, y_batch)

        # --- Retropropagación ---
        # Poner a cero los gradientes acumulados del paso anterior
        # (PyTorch acumula gradientes por defecto)
        optimizador.zero_grad()

        # Calcular los gradientes de la pérdida respecto a todos
        # los parámetros del modelo (retropropagación automática)
        perdida.backward()

        # --- Actualización de parámetros ---
        # El optimizador actualiza los pesos usando los gradientes
        # calculados y la regla de Adam
        optimizador.step()

        perdida_acumulada += perdida.item()
        num_batches += 1

    # Pérdida promedio de la época
    perdida_promedio = perdida_acumulada / num_batches

    # Actualizar el scheduler basado en la pérdida de la época
    scheduler.step(perdida_promedio)

    # --- Evaluación en el conjunto de prueba ---
    # Activar modo evaluación (desactiva dropout, usa estadísticas
    # de batch norm calculadas durante el entrenamiento)
    modelo.eval()

    # Desactivar el cálculo de gradientes (ahorra memoria y tiempo)
    with torch.no_grad():
        pred_test = modelo(X_test)
        perdida_test = criterio(pred_test, y_test)

        # Convertir probabilidades a clases (umbral 0.5)
        clases_pred = (pred_test >= 0.5).float()
        precision = (clases_pred == y_test).float().mean()

    # Imprimir cada 10 épocas
    if (epoca + 1) % 10 == 0:
        print(f"Época [{epoca+1}/{num_epocas}] | "
              f"Pérdida Train: {perdida_promedio:.4f} | "
              f"Pérdida Test: {perdida_test:.4f} | "
              f"Precisión Test: {precision:.4f}")

# ============================================================
# 5. Evaluación final
# ============================================================
modelo.eval()
with torch.no_grad():
    pred_final = modelo(X_test)
    clases_final = (pred_final >= 0.5).float()
    precision_final = (clases_final == y_test).float().mean()
    print(f"\nPrecisión final en test: {precision_final:.4f}")
```

### 2.6.3 Explicación del bucle de entrenamiento

El bucle de entrenamiento es el corazón del proceso de aprendizaje y merece una explicación detallada:

1. **`modelo.train()`**: Activa el modo de entrenamiento, lo que habilita el dropout (desactivación aleatoria de neuronas) y la normalización por lotes con estadísticas del mini-batch actual. Sin esta llamada, el modelo no aplicaría regularización durante el entrenamiento.

2. **Iteración sobre mini-batches**: El `DataLoader` se encarga de dividir el conjunto de entrenamiento en mini-batches de tamaño 32 y mezclarlos aleatoriamente en cada época (`shuffle=True`). Cada iteración del bucle interno procesa un mini-batch.

3. **`predicciones = modelo(X_batch)`**: Realiza la propagación hacia adelante. PyTorch ejecuta automáticamente el método `forward()` y construye el **grafo computacional** (*computational graph*), una estructura de datos que registra todas las operaciones realizadas y que será utilizada por la retropropagación para calcular los gradientes.

4. **`perdida = criterio(predicciones, y_batch)`**: Calcula la función de pérdida (BCE) entre las predicciones y las etiquetas verdaderas. Este valor escalar es el punto de partida para la retropropagación.

5. **`optimizador.zero_grad()`**: Pone a cero los gradientes de todos los parámetros. Esto es necesario porque PyTorch **acumula** los gradientes por defecto (los suma en cada llamada a `.backward()`). Sin esta línea, los gradientes de iteraciones anteriores se sumarían a los actuales, produciendo actualizaciones incorrectas. La acumulación de gradientes es útil en ciertos escenarios (por ejemplo, para simular batches más grandes), pero en el caso estándar debe ser reiniciada en cada iteración.

6. **`perdida.backward()`**: Esta es la llamada clave que ejecuta la **retropropagación automática** (*automatic differentiation*). PyTorch recorre el grafo computacional en orden inverso, calculando $\frac{\partial L}{\partial \theta}$ para cada parámetro $\theta$ del modelo utilizando la regla de la cadena, exactamente como se describió en la Subsección 2.2. Los gradientes calculados se almacenan en el atributo `.grad` de cada parámetro.

7. **`optimizador.step()`**: Actualiza todos los parámetros del modelo utilizando los gradientes almacenados en `.grad` y la regla de actualización del optimizador (en este caso, Adam). Para el optimizador Adam, esto implica actualizar las estimaciones de primer y segundo momento, aplicar la corrección de sesgo y calcular la actualización final como se describió en la Subsección 2.4.3.

8. **`modelo.eval()` y `torch.no_grad()`**: Para la evaluación, se desactiva el dropout y se utilizan las estadísticas de BN acumuladas. El contexto `torch.no_grad()` desactiva la construcción del grafo computacional, reduciendo el consumo de memoria y acelerando la inferencia.

### 2.6.4 Análisis de los resultados

El código anterior produce un clasificador que aprende la frontera de decisión lineal subyacente en los datos. Al ser un problema relativamente simple (frontera lineal con algo de ruido), un MLP incluso pequeño logra una precisión alta ($> 90\%$) tras pocas épocas de entrenamiento.

Algunos aspectos a observar:

- **La pérdida de entrenamiento disminuye monótonamente** en cada época, lo que indica que el optimizador está actualizando los parámetros en la dirección correcta.
- **La pérdida de test puede fluctuar** ligeramente, pero con la regularización aplicada (dropout + L2 + BN), debería permanecer cercana a la pérdida de entrenamiento, indicando buena generalización.
- **El scheduler de tasa de aprendizaje** reduce $\eta$ automáticamente si la pérdida se estanca, permitiendo un refinamiento más fino en las etapas finales del entrenamiento.
- **El número de parámetros** del modelo es $2 \times 16 + 16 + 16 \times 8 + 8 + 8 \times 1 + 1 + 16 \times 2 = 32 + 16 + 128 + 8 + 8 + 1 + 32 = 225$ (incluyendo los parámetros $\gamma$ y $\beta$ del BatchNorm). Este número es modesto para un MLP, pero las técnicas empleadas son idénticas a las utilizadas en modelos con millones de parámetros.

### 2.6.5 Conexión con comunicaciones semánticas

En un sistema de comunicaciones semánticas basado en MLP, la arquitectura del ejemplo puede extenderse de la siguiente manera:

- **Codificador semántico (transmisor):** Un MLP que recibe datos de alta dimensionalidad (texto tokenizado, píxeles de imagen, muestras de audio) y los comprime en una representación latente de baja dimensionalidad, análoga a un código de canal. La regularización (dropout, L2) previene el sobreajuste y promueve representaciones robustas al ruido del canal.

- **Canal:** La representación latente se transmite a través de un canal con ruido (por ejemplo, AWGN), que puede modelarse como una capa sin parámetros aprendibles que suma ruido gaussiano.

- **Decodificador semántico (receptor):** Otro MLP que recibe la señal ruidosa y reconstruye la información semántica relevante. La función de pérdida se elige según el objetivo: MSE para reconstrucción exacta, entropía cruzada si el objetivo es clasificar correctamente el contenido del mensaje.

El entrenamiento extremo a extremo de este sistema utiliza exactamente los mismos principios de retropropagación, funciones de pérdida y optimizadores descritos en esta sección, con la diferencia de que el gradiente debe propagarse a través de la capa de canal (lo que requiere técnicas especiales cuando el canal no es diferenciable, tema que se abordará en secciones posteriores).

---

**Resumen de la sección:** En esta sección hemos estudiado el perceptrón multicapa como la arquitectura fundamental del aprendizaje profundo. Hemos formalizado la propagación hacia adelante mediante la composición de transformaciones afines y funciones de activación no lineales, y hemos derivado en detalle el algoritmo de retropropagación como una aplicación sistemática de la regla de la cadena. Se presentaron las funciones de pérdida más importantes (MSE, BCE, CCE) y sus criterios de selección, los optimizadores modernos (SGD, SGD con momento, Adam) y sus propiedades, y las técnicas de regularización (L1, L2, dropout, normalización por lotes) necesarias para lograr buena generalización. Finalmente, se implementó un ejemplo completo de clasificación binaria en PyTorch que integra todos estos conceptos. Los principios aquí presentados constituyen la base sobre la cual se construirán las arquitecturas más sofisticadas de las secciones siguientes: redes convolucionales, redes recurrentes y transformadores.

---

# 3. Redes Neuronales Convolucionales (CNN)

Las redes neuronales convolucionales (CNN, por sus siglas en inglés, *Convolutional Neural Networks*) constituyen una de las arquitecturas más influyentes y exitosas del aprendizaje profundo. Originalmente diseñadas para el procesamiento de imágenes, las CNN han demostrado una versatilidad extraordinaria que se extiende a dominios tan diversos como el procesamiento de señales de radiofrecuencia, el análisis de series temporales y, de manera particularmente relevante para este tutorial, las comunicaciones semánticas. En esta sección, desarrollaremos los fundamentos matemáticos de la convolución, describiremos cada componente de una CNN y exploraremos sus aplicaciones directas en sistemas de telecomunicaciones, incluyendo la clasificación automática de modulación y la detección de anomalías en señales.

---

## 3.1 Motivación y concepto de convolución

### 3.1.1 La explosión de parámetros en redes totalmente conectadas

En las secciones anteriores se presentaron las redes neuronales densas (*fully connected*), donde cada neurona de una capa está conectada a todas las neuronas de la capa anterior. Aunque este enfoque es conceptualmente simple y universal en su capacidad de aproximación, presenta una limitación práctica severa cuando se aplica a datos de alta dimensionalidad, como las imágenes.

Consideremos una imagen en escala de grises de tamaño modesto, por ejemplo $256 \times 256$ píxeles. Esta imagen, al ser representada como un vector de entrada para una red densa, tiene $256 \times 256 = 65{,}536$ componentes. Si la primera capa oculta contiene tan solo 1,000 neuronas, el número de pesos entre la capa de entrada y esta primera capa oculta sería:

$$W = 65{,}536 \times 1{,}000 = 65{,}536{,}000 \text{ parámetros}$$

Para una imagen a color de dimensiones $224 \times 224 \times 3$ (tres canales RGB), como las que se utilizan comúnmente en visión por computadora, el número de entradas asciende a $224 \times 224 \times 3 = 150{,}528$, lo que produce más de 150 millones de parámetros solo en la primera capa. Esta explosión combinatoria genera múltiples problemas:

1. **Sobreajuste (*overfitting*):** Con tantos parámetros libres, el modelo tiende a memorizar los datos de entrenamiento en lugar de aprender patrones generalizables, especialmente cuando el conjunto de datos no es extremadamente grande.

2. **Costo computacional prohibitivo:** El almacenamiento y la actualización de millones de parámetros demandan cantidades enormes de memoria y tiempo de cómputo, haciendo el entrenamiento impracticable para imágenes de resolución moderada o alta.

3. **Ignorancia de la estructura espacial:** Una red densa trata cada píxel como una variable independiente. No incorpora la noción fundamental de que los píxeles cercanos entre sí tienden a estar altamente correlacionados, ni que los patrones visuales (bordes, texturas, formas) son locales y pueden aparecer en cualquier posición de la imagen.

Estas limitaciones motivaron la búsqueda de una arquitectura que pudiera explotar la estructura inherente de los datos espaciales. La respuesta se encontró en la operación matemática de convolución, una herramienta fundamental del análisis funcional y el procesamiento de señales, que fue adaptada al contexto de las redes neuronales de manera pionera por Yann LeCun y colaboradores en la década de 1990.

### 3.1.2 Definición matemática de la convolución continua

La convolución es una operación matemática que combina dos funciones para producir una tercera función que expresa cómo la forma de una modifica a la otra. En el dominio continuo, la convolución de dos funciones $f$ y $g$ se define como:

$$(f * g)(t) = \int_{-\infty}^{\infty} f(\tau) \, g(t - \tau) \, d\tau$$

donde $\tau$ es la variable de integración y $t$ es la variable de la función resultante. Esta operación tiene una interpretación intuitiva y profunda: se invierte una de las funciones (reflexión temporal), se desplaza a lo largo del eje temporal, y en cada posición de desplazamiento se computa el producto interno (integral del producto punto a punto) entre las dos funciones.

La convolución satisface varias propiedades algebraicas fundamentales que la hacen particularmente útil tanto en matemáticas puras como en ingeniería:

- **Conmutatividad:** $(f * g)(t) = (g * f)(t)$. Esto significa que el orden de las funciones no altera el resultado.
- **Asociatividad:** $(f * (g * h))(t) = ((f * g) * h)(t)$. Esto permite encadenar múltiples convoluciones de manera flexible.
- **Distributividad:** $f * (g + h) = (f * g) + (f * h)$. La convolución se distribuye sobre la suma.
- **Teorema de convolución:** En el dominio de Fourier, la convolución se transforma en multiplicación punto a punto: $\mathcal{F}\{f * g\} = \mathcal{F}\{f\} \cdot \mathcal{F}\{g\}$. Esta propiedad es la base del procesamiento eficiente de señales y establece un puente directo con los sistemas de telecomunicaciones.

En el contexto de las telecomunicaciones, la convolución aparece de manera natural en múltiples escenarios: cuando una señal pasa a través de un canal de comunicación (la señal recibida es la convolución de la señal transmitida con la respuesta al impulso del canal), en el diseño de filtros (un filtro lineal e invariante en el tiempo opera mediante convolución), y en la ecualización de canal.

### 3.1.3 La convolución discreta

En el procesamiento digital de señales y, por extensión, en las redes neuronales, trabajamos con datos discretos (muestras). La versión discreta de la convolución se define como:

$$(f * g)[n] = \sum_{k=-\infty}^{\infty} f[k] \, g[n - k]$$

donde $f$ y $g$ son secuencias discretas y $n$ es el índice de la secuencia resultante. En la práctica, las secuencias tienen soporte finito, por lo que la suma se realiza sobre un número finito de términos:

$$(f * g)[n] = \sum_{k=0}^{K-1} f[k] \, g[n - k]$$

donde $K$ es la longitud del filtro (o *kernel*). Cada valor de la señal de salida se calcula como una suma ponderada de valores vecinos de la señal de entrada, donde los pesos están determinados por el filtro $g$.

Consideremos un ejemplo concreto. Sea $f = [1, 3, 5, 2, 4]$ una señal de entrada y $g = [1, 0, -1]$ un filtro de tamaño $K=3$. Para calcular la salida en el índice $n=1$:

$$(f * g)[1] = f[0] \cdot g[1] + f[1] \cdot g[0] + f[2] \cdot g[-1]$$

En la práctica de las redes neuronales, se utiliza una operación ligeramente diferente llamada correlación cruzada (*cross-correlation*), que omite la reflexión del kernel:

$$(f \star g)[n] = \sum_{k=0}^{K-1} f[n + k] \, g[k]$$

Aunque matemáticamente la convolución y la correlación cruzada difieren en la reflexión del kernel, en el contexto de las redes neuronales esta distinción es irrelevante, ya que los pesos del kernel se aprenden durante el entrenamiento. Si el kernel óptimo para la convolución es $[a, b, c]$, el kernel óptimo aprendido para la correlación cruzada sería simplemente $[c, b, a]$. Por convención, en la comunidad de aprendizaje profundo se utiliza el término "convolución" para referirse a la operación de correlación cruzada.

### 3.1.4 Principios fundamentales: campos receptivos locales, compartición de pesos e invarianza a traslaciones

Las CNN incorporan tres principios arquitectónicos fundamentales que abordan directamente las limitaciones de las redes densas:

**Campos receptivos locales (*local receptive fields*).** En lugar de conectar cada neurona de salida a todos los píxeles de la imagen de entrada, cada neurona se conecta únicamente a una región pequeña y localizada de la entrada, denominada *campo receptivo*. Si el kernel tiene un tamaño de $k \times k$, cada neurona de salida depende solo de $k^2$ valores de entrada, en contraste con los $n^2$ valores que requeriría una conexión densa para una imagen de $n \times n$. Este enfoque se alinea con el conocimiento neurobiológico de la corteza visual, donde las neuronas individuales responden a estímulos en regiones específicas del campo visual, no a la totalidad de la escena.

**Compartición de pesos (*weight sharing*).** El mismo conjunto de pesos (el kernel o filtro) se aplica a todas las posiciones de la imagen de entrada. Esto significa que un detector de bordes verticales, por ejemplo, utiliza exactamente los mismos pesos sin importar si está analizando la esquina superior izquierda o el centro de la imagen. Este principio reduce drásticamente el número de parámetros: en lugar de tener un conjunto de pesos diferente para cada posición espacial, un solo kernel de $k \times k$ se reutiliza en toda la imagen. Para una imagen de $n \times n$ con un kernel de $k \times k$, el número de parámetros por filtro es simplemente $k^2$ (más un sesgo), independientemente del tamaño de la imagen.

**Invarianza a traslaciones (*translation equivariance*).** Como consecuencia directa de la compartición de pesos, las CNN son equivariantes a traslaciones. Si un patrón (por ejemplo, un gato) aparece en una posición diferente de la imagen, la representación aprendida en las capas convolucionales se desplaza correspondientemente, pero mantiene la misma activación. Formalmente, si $T_{\mathbf{d}}$ denota un operador de traslación por un vector $\mathbf{d}$, entonces:

$$\text{Conv}(T_{\mathbf{d}}(\mathbf{X})) = T_{\mathbf{d}}(\text{Conv}(\mathbf{X}))$$

Es importante distinguir entre *equivarianza* e *invarianza*: la convolución es equivariante (la salida se desplaza con la entrada), mientras que la invarianza completa (la salida no cambia ante traslaciones) se logra posteriormente mediante las capas de pooling o las capas densas finales.

Estos tres principios trabajan en conjunto para crear una arquitectura que es simultáneamente eficiente en parámetros, capaz de detectar patrones locales relevantes y robusta ante cambios de posición de los objetos de interés.

**Figura 3.1:** *Visualización de la operación de convolución 2D. Se muestra una imagen de entrada de dimensiones $5 \times 5$ (representada como una matriz de valores de intensidad de píxel) y un kernel (filtro) de tamaño $3 \times 3$. El kernel se desliza sobre la imagen de izquierda a derecha y de arriba a abajo, con un paso (stride) de 1. En cada posición, se calcula el producto punto entre los valores del kernel y la región correspondiente de la imagen (el campo receptivo local), y el resultado escalar se coloca en la posición correspondiente de la matriz de salida (mapa de características). Se destacan tres posiciones del kernel: (a) esquina superior izquierda, produciendo el primer elemento de la salida; (b) una posición intermedia; y (c) la esquina inferior derecha, produciendo el último elemento. Las flechas indican la dirección del deslizamiento. La matriz de salida resultante tiene dimensiones $3 \times 3$ (calculada según la fórmula de tamaño de salida sin relleno). Los colores resaltan qué píxeles de la entrada contribuyen a cada valor de la salida.*

---

## 3.2 Capas convolucionales

### 3.2.1 Convolución 2D para imágenes

La capa convolucional es el componente fundamental de las CNN. Formalmente, la convolución 2D discreta (en realidad, correlación cruzada, como se discutió anteriormente) entre una imagen de entrada $\mathbf{X}$ y un kernel $\mathbf{K}$ de tamaño $k_h \times k_w$ produce un mapa de características (*feature map*) $\mathbf{Y}$ definido por:

$$\mathbf{Y}[i, j] = (\mathbf{X} * \mathbf{K})[i, j] = \sum_{m=0}^{k_h - 1} \sum_{n=0}^{k_w - 1} \mathbf{X}[i + m, \, j + n] \cdot \mathbf{K}[m, n]$$

donde $(i, j)$ indica la posición espacial en el mapa de salida, y $(m, n)$ recorre las posiciones del kernel. Además de los pesos del kernel, cada filtro convolucional incluye un término de sesgo (*bias*) $b$, y la salida completa de una neurona convolucional se pasa típicamente por una función de activación no lineal $\sigma$ (como ReLU):

$$\mathbf{Y}[i, j] = \sigma\left( \sum_{m=0}^{k_h - 1} \sum_{n=0}^{k_w - 1} \mathbf{X}[i + m, \, j + n] \cdot \mathbf{K}[m, n] + b \right)$$

Cuando la entrada tiene múltiples canales (por ejemplo, una imagen RGB con 3 canales, o un mapa de características de una capa anterior con $C_{in}$ canales), el kernel se extiende a tres dimensiones ($C_{in} \times k_h \times k_w$), y la convolución se realiza como:

$$\mathbf{Y}[i, j] = \sigma\left( \sum_{c=0}^{C_{in}-1} \sum_{m=0}^{k_h - 1} \sum_{n=0}^{k_w - 1} \mathbf{X}[c, \, i + m, \, j + n] \cdot \mathbf{K}[c, \, m, n] + b \right)$$

Aquí, el kernel realiza la convolución en cada canal de manera independiente y luego suma los resultados, produciendo un único mapa de características escalar 2D como salida. Para obtener múltiples mapas de características (cada uno detectando un patrón diferente), se utilizan múltiples kernels, lo que nos lleva al concepto de filtros múltiples.

### 3.2.2 Parámetros de la convolución: tamaño del kernel, stride y padding

La operación de convolución se configura mediante tres hiperparámetros fundamentales que determinan tanto el comportamiento como las dimensiones de la salida:

**Tamaño del kernel (*kernel size*), $k$.** El tamaño del kernel define la extensión del campo receptivo local. Los tamaños más comunes en la práctica son $3 \times 3$, $5 \times 5$ y $7 \times 7$. Kernels más pequeños capturan patrones más finos y locales (bordes, esquinas), mientras que kernels más grandes pueden detectar patrones más extensos, pero a costa de un mayor número de parámetros ($k^2$ por canal). La arquitectura VGGNet demostró que apilar múltiples capas con kernels $3 \times 3$ es preferible a usar un solo kernel grande, ya que dos capas de $3 \times 3$ tienen un campo receptivo efectivo de $5 \times 5$ pero con menos parámetros ($2 \times 3^2 = 18$ versus $5^2 = 25$) y mayor capacidad de representación no lineal (al intercalar funciones de activación).

**Paso (*stride*), $s$.** El stride define cuántas posiciones se desplaza el kernel en cada paso. Un stride de $s = 1$ significa que el kernel se mueve un píxel a la vez, produciendo un mapa de salida de dimensiones cercanas a las de la entrada. Un stride de $s = 2$ reduce las dimensiones espaciales aproximadamente a la mitad, ya que el kernel salta de dos en dos posiciones. Un stride mayor reduce la resolución espacial pero aumenta el campo receptivo efectivo de capas posteriores y reduce el costo computacional.

**Relleno (*padding*), $p$.** El padding consiste en agregar filas y columnas de valores (típicamente ceros) alrededor del borde de la imagen de entrada antes de aplicar la convolución. Existen dos modos principales:

- ***Valid padding*** ($p = 0$): No se agrega relleno. La convolución solo se aplica donde el kernel cabe completamente dentro de la entrada. Esto reduce las dimensiones de salida.
- ***Same padding*** ($p = \lfloor k/2 \rfloor$ para stride $s=1$): Se agrega suficiente relleno para que la salida tenga las mismas dimensiones espaciales que la entrada. Para un kernel de $3 \times 3$, esto requiere $p = 1$; para un kernel de $5 \times 5$, $p = 2$.

### 3.2.3 Fórmula del tamaño de salida

Dados los hiperparámetros anteriores, el tamaño de la salida se calcula mediante la siguiente fórmula:

$$o = \left\lfloor \frac{n + 2p - k}{s} \right\rfloor + 1$$

donde:
- $o$ es la dimensión de salida (ancho o alto del mapa de características),
- $n$ es la dimensión de entrada correspondiente,
- $p$ es el padding,
- $k$ es el tamaño del kernel en esa dimensión,
- $s$ es el stride,
- $\lfloor \cdot \rfloor$ denota la función piso (redondeo hacia abajo al entero más cercano).

Verifiquemos con algunos casos concretos:

- **Entrada $n=32$, kernel $k=5$, stride $s=1$, padding $p=0$:** $o = \lfloor (32 + 0 - 5)/1 \rfloor + 1 = 27 + 1 = 28$.
- **Entrada $n=32$, kernel $k=5$, stride $s=1$, padding $p=2$ (same):** $o = \lfloor (32 + 4 - 5)/1 \rfloor + 1 = 31 + 1 = 32$. La salida mantiene el mismo tamaño.
- **Entrada $n=32$, kernel $k=3$, stride $s=2$, padding $p=1$:** $o = \lfloor (32 + 2 - 3)/2 \rfloor + 1 = \lfloor 31/2 \rfloor + 1 = 15 + 1 = 16$. La dimensión se reduce a la mitad.

Esta fórmula se aplica independientemente a cada dimensión espacial (alto y ancho), permitiendo el uso de kernels rectangulares y strides asimétricos cuando sea necesario.

### 3.2.4 Mapas de características y filtros múltiples

Una sola operación de convolución con un kernel produce un único mapa de características 2D. Sin embargo, una capa convolucional típica contiene múltiples filtros (kernels), cada uno aprendiendo a detectar un patrón diferente. Si la capa tiene $C_{out}$ filtros, la salida será un tensor tridimensional de dimensiones $C_{out} \times o_h \times o_w$, donde $o_h$ y $o_w$ son las dimensiones espaciales de salida.

El número total de parámetros aprendibles en una capa convolucional es:

$$\text{Parámetros} = C_{out} \times (C_{in} \times k_h \times k_w + 1)$$

donde el $+1$ corresponde al sesgo de cada filtro. Por ejemplo, una capa convolucional con entrada de 3 canales (RGB), 64 filtros de tamaño $3 \times 3$ tiene:

$$\text{Parámetros} = 64 \times (3 \times 3 \times 3 + 1) = 64 \times 28 = 1{,}792$$

Comparemos esto con una capa densa equivalente. Si la entrada es una imagen de $224 \times 224 \times 3$ y la salida tiene $224 \times 224 \times 64$ unidades, la capa densa requeriría $150{,}528 \times 3{,}211{,}264 \approx 4.83 \times 10^{11}$ parámetros, un número absurdamente grande. La convolución con compartición de pesos reduce esto a menos de dos mil parámetros, una reducción de ocho órdenes de magnitud.

En las primeras capas de la red, los filtros aprenden a detectar características de bajo nivel como bordes horizontales, verticales, diagonales y gradientes de color. En capas intermedias, los filtros combinan estas características básicas para detectar texturas, esquinas y partes de objetos. En las capas más profundas, los filtros responden a patrones de alto nivel como rostros, ruedas o texto, construyendo una jerarquía de representaciones cada vez más abstractas.

### 3.2.5 Ejemplo numérico: detección de bordes con un filtro 3×3

Para consolidar la comprensión de la operación de convolución, desarrollaremos un ejemplo completo paso a paso. Consideremos una imagen de entrada en escala de grises de tamaño $5 \times 5$:

$$\mathbf{X} = \begin{bmatrix} 10 & 10 & 10 & 0 & 0 \\ 10 & 10 & 10 & 0 & 0 \\ 10 & 10 & 10 & 0 & 0 \\ 10 & 10 & 10 & 0 & 0 \\ 10 & 10 & 10 & 0 & 0 \end{bmatrix}$$

Esta imagen simula una transición vertical (borde) entre una región clara (valor 10) a la izquierda y una región oscura (valor 0) a la derecha. Aplicaremos un filtro Sobel vertical para la detección de bordes:

$$\mathbf{K} = \begin{bmatrix} -1 & 0 & 1 \\ -2 & 0 & 2 \\ -1 & 0 & 1 \end{bmatrix}$$

Utilizaremos *valid padding* ($p = 0$) y stride $s = 1$. La dimensión de salida será:

$$o = \left\lfloor \frac{5 + 0 - 3}{1} \right\rfloor + 1 = 3$$

Por lo tanto, el mapa de características de salida tendrá dimensiones $3 \times 3$. Calculemos cada elemento:

**Posición $(0, 0)$:** El kernel se superpone con la submatriz de $\mathbf{X}$ que comprende las filas 0–2 y columnas 0–2:

$$\mathbf{Y}[0,0] = \sum_{m=0}^{2}\sum_{n=0}^{2} \mathbf{X}[m, n] \cdot \mathbf{K}[m, n]$$

$$= 10 \cdot (-1) + 10 \cdot 0 + 10 \cdot 1 + 10 \cdot (-2) + 10 \cdot 0 + 10 \cdot 2 + 10 \cdot (-1) + 10 \cdot 0 + 10 \cdot 1$$

$$= -10 + 0 + 10 - 20 + 0 + 20 - 10 + 0 + 10 = 0$$

No se detecta borde porque la región cubierta es completamente uniforme (todo valor 10).

**Posición $(0, 1)$:** El kernel cubre las columnas 1–3:

$$\mathbf{Y}[0,1] = 10 \cdot (-1) + 10 \cdot 0 + 0 \cdot 1 + 10 \cdot (-2) + 10 \cdot 0 + 0 \cdot 2 + 10 \cdot (-1) + 10 \cdot 0 + 0 \cdot 1$$

$$= -10 + 0 + 0 - 20 + 0 + 0 - 10 + 0 + 0 = -40$$

El valor negativo grande indica la presencia de un borde vertical con transición de claro a oscuro.

**Posición $(0, 2)$:** El kernel cubre las columnas 2–4:

$$\mathbf{Y}[0,2] = 10 \cdot (-1) + 0 \cdot 0 + 0 \cdot 1 + 10 \cdot (-2) + 0 \cdot 0 + 0 \cdot 2 + 10 \cdot (-1) + 0 \cdot 0 + 0 \cdot 1$$

$$= -10 + 0 + 0 - 20 + 0 + 0 - 10 + 0 + 0 = -40$$

Nuevamente se detecta el borde. Podemos observar que, por la simetría de la imagen (el borde vertical se extiende a lo largo de toda la altura), las posiciones con los mismos índices de columna producen los mismos valores independientemente de la fila. Continuando el cálculo para las filas restantes:

**Posición $(1, 0)$:** Filas 1–3, columnas 0–2: $\mathbf{Y}[1,0] = 0$ (región uniforme).

**Posición $(1, 1)$:** Filas 1–3, columnas 1–3: $\mathbf{Y}[1,1] = -40$.

**Posición $(1, 2)$:** Filas 1–3, columnas 2–4: $\mathbf{Y}[1,2] = -40$.

**Posición $(2, 0)$:** Filas 2–4, columnas 0–2: $\mathbf{Y}[2,0] = 0$.

**Posición $(2, 1)$:** Filas 2–4, columnas 1–3: $\mathbf{Y}[2,1] = -40$.

**Posición $(2, 2)$:** Filas 2–4, columnas 2–4: $\mathbf{Y}[2,2] = -40$.

El mapa de características resultante es:

$$\mathbf{Y} = \begin{bmatrix} 0 & -40 & -40 \\ 0 & -40 & -40 \\ 0 & -40 & -40 \end{bmatrix}$$

Este resultado es extremadamente informativo. La primera columna tiene valores cero, indicando que no hay borde en esa posición. Las columnas segunda y tercera tienen valores negativos grandes ($-40$), indicando la presencia de un borde vertical fuerte. El signo negativo indica la dirección de la transición (de claro a oscuro de izquierda a derecha); si la transición fuera en sentido contrario, los valores serían positivos ($+40$). La magnitud absoluta ($40$) refleja la intensidad del contraste.

Este ejemplo ilustra cómo un único filtro, con solo 9 parámetros fijos, puede detectar un tipo específico de patrón en cualquier posición de la imagen. En una CNN, estos parámetros no se fijan manualmente sino que se aprenden automáticamente durante el entrenamiento, permitiendo a la red descubrir los patrones más relevantes para la tarea.

**Figura 3.1b:** *Ejemplo numérico de convolución paso a paso. A la izquierda se muestra la imagen de entrada $\mathbf{X}$ de $5 \times 5$ con una región clara (valor 10) en las tres primeras columnas y una región oscura (valor 0) en las dos últimas. En el centro se presenta el kernel Sobel vertical $\mathbf{K}$ de $3 \times 3$. A la derecha se muestra el mapa de características resultante $\mathbf{Y}$ de $3 \times 3$. Las flechas conectan cada posición del kernel sobre la imagen con el valor correspondiente de la salida. Se resaltan tres pasos: (a) posición $(0,0)$ donde el kernel cubre una región uniforme, produciendo salida $0$; (b) posición $(0,1)$ donde el kernel cruza el borde vertical, produciendo salida $-40$; (c) posición $(0,2)$ donde el kernel cubre otra región del borde, produciendo $-40$. La columna de ceros en la salida indica ausencia de borde; las columnas con valores $-40$ marcan la ubicación del borde vertical detectado.*

---

## 3.3 Capas de Pooling

### 3.3.1 Max Pooling

Las capas de pooling (o submuestreo) son componentes esenciales de las CNN que reducen progresivamente la resolución espacial de los mapas de características. La operación de Max Pooling selecciona el valor máximo dentro de una ventana deslizante de tamaño fijo. Formalmente, dado un mapa de características $\mathbf{Y}$ y una ventana de pooling de tamaño $p_h \times p_w$ con stride $s$, la salida del Max Pooling es:

$$\mathbf{Z}[i, j] = \max_{0 \leq m < p_h, \, 0 \leq n < p_w} \mathbf{Y}[i \cdot s + m, \, j \cdot s + n]$$

La configuración más común es una ventana de $2 \times 2$ con stride $s = 2$, lo que reduce cada dimensión espacial exactamente a la mitad. Por ejemplo, un mapa de características de $32 \times 32$ se convierte en uno de $16 \times 16$ después del Max Pooling.

El Max Pooling preserva las activaciones más fuertes (los valores más altos) dentro de cada vecindario, lo que tiene una interpretación intuitiva: si un detector de bordes produce una activación fuerte en algún lugar dentro de una región de $2 \times 2$ píxeles, el Max Pooling retiene esa detección independientemente de la posición exacta dentro de la ventana. Esto confiere a la red una cierta *invarianza a pequeñas traslaciones*, complementando la equivarianza proporcionada por las capas convolucionales.

### 3.3.2 Average Pooling

El Average Pooling calcula el promedio de los valores dentro de la ventana deslizante:

$$\mathbf{Z}[i, j] = \frac{1}{p_h \times p_w} \sum_{m=0}^{p_h - 1} \sum_{n=0}^{p_w - 1} \mathbf{Y}[i \cdot s + m, \, j \cdot s + n]$$

A diferencia del Max Pooling, que retiene la activación más fuerte, el Average Pooling considera la contribución promedio de todos los valores en la ventana. Esto produce representaciones más suaves y es particularmente útil en las capas finales de la red. Una variante especial es el *Global Average Pooling* (GAP), que calcula el promedio sobre toda la extensión espacial del mapa de características (la ventana es del mismo tamaño que el mapa), reduciendo cada canal a un único valor escalar. El GAP fue introducido por Lin, Chen y Yan (2014, DOI: 10.48550/arXiv.1312.4400) como una alternativa a las capas densas finales, reduciendo significativamente el número de parámetros y el riesgo de sobreajuste.

### 3.3.3 Propósito y ventajas del pooling

Las capas de pooling cumplen múltiples funciones:

1. **Reducción de dimensionalidad.** Al reducir las dimensiones espaciales, el pooling disminuye el número de computaciones y parámetros en las capas subsecuentes. Un Max Pooling $2 \times 2$ con stride 2 reduce el número de activaciones en un factor de 4 (reduce tanto el alto como el ancho a la mitad).

2. **Invarianza a traslaciones locales.** Si una característica (por ejemplo, un borde) se desplaza uno o dos píxeles, su activación máxima dentro de la ventana de pooling permanecerá siendo seleccionada, haciendo que la representación sea robusta ante pequeños desplazamientos.

3. **Aumento del campo receptivo efectivo.** Después del pooling, las capas convolucionales subsecuentes "ven" una porción mayor de la imagen original, ya que cada posición del mapa reducido corresponde a una región más grande de la entrada.

4. **Regularización implícita.** La reducción de resolución actúa como una forma de regularización, previniendo el sobreajuste al descartar información posicional precisa que podría ser ruidosa o irrelevante.

### 3.3.4 Ejemplo numérico de pooling

Consideremos el siguiente mapa de características de $4 \times 4$:

$$\mathbf{Y} = \begin{bmatrix} 1 & 3 & 2 & 4 \\ 5 & 6 & 1 & 2 \\ 7 & 8 & 3 & 0 \\ 2 & 4 & 1 & 5 \end{bmatrix}$$

**Max Pooling con ventana $2 \times 2$ y stride $2$:**

La imagen se divide en cuatro bloques no superpuestos de $2 \times 2$:

- Bloque superior izquierdo: $\begin{bmatrix} 1 & 3 \\ 5 & 6 \end{bmatrix} \rightarrow \max = 6$

- Bloque superior derecho: $\begin{bmatrix} 2 & 4 \\ 1 & 2 \end{bmatrix} \rightarrow \max = 4$

- Bloque inferior izquierdo: $\begin{bmatrix} 7 & 8 \\ 2 & 4 \end{bmatrix} \rightarrow \max = 8$

- Bloque inferior derecho: $\begin{bmatrix} 3 & 0 \\ 1 & 5 \end{bmatrix} \rightarrow \max = 5$

$$\text{MaxPool}(\mathbf{Y}) = \begin{bmatrix} 6 & 4 \\ 8 & 5 \end{bmatrix}$$

**Average Pooling con ventana $2 \times 2$ y stride $2$:**

- Bloque superior izquierdo: $\frac{1 + 3 + 5 + 6}{4} = \frac{15}{4} = 3.75$

- Bloque superior derecho: $\frac{2 + 4 + 1 + 2}{4} = \frac{9}{4} = 2.25$

- Bloque inferior izquierdo: $\frac{7 + 8 + 2 + 4}{4} = \frac{21}{4} = 5.25$

- Bloque inferior derecho: $\frac{3 + 0 + 1 + 5}{4} = \frac{9}{4} = 2.25$

$$\text{AvgPool}(\mathbf{Y}) = \begin{bmatrix} 3.75 & 2.25 \\ 5.25 & 2.25 \end{bmatrix}$$

Observemos cómo el Max Pooling resalta las activaciones dominantes (valor 8 del bloque inferior izquierdo), mientras que el Average Pooling produce valores más moderados que representan la activación promedio de cada región.

---

## 3.4 Arquitectura completa de una CNN

### 3.4.1 Pipeline estándar

Una CNN para clasificación de imágenes sigue típicamente una arquitectura secuencial que combina los componentes descritos en las secciones anteriores. El pipeline estándar se puede expresar como:

$$\text{Input} \rightarrow [\text{Conv} \rightarrow \text{ReLU} \rightarrow \text{Pool}]_{\times N} \rightarrow \text{Flatten} \rightarrow [\text{Dense} \rightarrow \text{ReLU}]_{\times M} \rightarrow \text{Softmax} \rightarrow \text{Output}$$

Cada etapa tiene un propósito específico:

1. **Capas convolucionales (Conv).** Extraen características locales mediante la operación de convolución descrita en la Sección 3.2. Las capas iniciales detectan patrones de bajo nivel (bordes, texturas), mientras que las capas más profundas capturan patrones de alto nivel (partes de objetos, estructuras complejas).

2. **Activación ReLU.** Después de cada convolución, se aplica la función de activación ReLU (*Rectified Linear Unit*), $\text{ReLU}(x) = \max(0, x)$, que introduce no linealidad. Sin estas no linealidades, la composición de múltiples capas convolucionales sería equivalente a una sola convolución lineal, limitando drásticamente la capacidad expresiva de la red.

3. **Capas de Pooling (Pool).** Reducen la dimensionalidad espacial, incrementan el campo receptivo efectivo y proporcionan invarianza a pequeñas traslaciones, como se explicó en la Sección 3.3.

4. **Aplanamiento (Flatten).** Después de las capas convolucionales y de pooling, el tensor tridimensional de mapas de características se "aplana" en un vector unidimensional. Si el tensor final tiene dimensiones $C \times H \times W$, el vector resultante tiene $C \times H \times W$ componentes. Esta operación no tiene parámetros aprendibles; simplemente reorganiza los datos para que puedan ser procesados por capas densas.

5. **Capas densas (*fully connected*).** Combinan las características extraídas por las capas convolucionales para tomar la decisión de clasificación final. Estas capas operan como las redes neuronales densas descritas en la sección anterior del tutorial.

6. **Softmax.** La última capa aplica la función softmax para producir una distribución de probabilidad sobre las $C$ clases:

$$P(y = c \mid \mathbf{x}) = \frac{e^{z_c}}{\sum_{j=1}^{C} e^{z_j}}$$

donde $z_c$ es la salida (*logit*) correspondiente a la clase $c$.

Es importante observar que, a medida que los datos fluyen a través de la red, las dimensiones espaciales se reducen progresivamente (mediante stride y pooling), mientras que el número de canales (filtros) aumenta. Un patrón típico podría ser:

$$[224 \times 224 \times 3] \xrightarrow{\text{Conv}} [224 \times 224 \times 64] \xrightarrow{\text{Pool}} [112 \times 112 \times 64] \xrightarrow{\text{Conv}} [112 \times 112 \times 128] \xrightarrow{\text{Pool}} [56 \times 56 \times 128] \rightarrow \cdots$$

Esta progresión de "alto en espacio, bajo en canales" a "bajo en espacio, alto en canales" refleja una transición de representaciones locales y detalladas a representaciones globales y abstractas.

**Figura 3.2:** *Arquitectura completa de una CNN para clasificación de imágenes. Se muestra el flujo de datos desde la imagen de entrada (por ejemplo, una imagen RGB de $224 \times 224 \times 3$) a través de múltiples bloques convolucionales. Cada bloque consiste en una capa convolucional (representada como un conjunto de mapas de características apilados en profundidad), seguida de una activación ReLU y una capa de Max Pooling que reduce las dimensiones espaciales a la mitad. Se ilustran dos bloques convolucionales: el primero con 32 filtros de $3 \times 3$ produciendo 32 mapas de $112 \times 112$, y el segundo con 64 filtros produciendo 64 mapas de $56 \times 56$. Después de los bloques convolucionales, una operación de aplanamiento (Flatten) convierte el tensor 3D en un vector 1D, que alimenta dos capas densas (fully connected) con activación ReLU. La capa final tiene tantas neuronas como clases y aplica softmax para producir probabilidades de clase. Las flechas indican el flujo de datos, y junto a cada etapa se muestran las dimensiones del tensor. Se observa visualmente cómo las dimensiones espaciales disminuyen mientras el número de canales aumenta a lo largo de la red.*

### 3.4.2 Arquitecturas clásicas

El desarrollo de las CNN ha sido marcado por una serie de arquitecturas innovadoras que establecieron hitos en el campo:

**LeNet-5 (LeCun et al., 1998, DOI: 10.1109/5.726791).** Considerada la primera CNN moderna, fue diseñada para el reconocimiento de dígitos manuscritos (dataset MNIST). Su arquitectura consta de dos capas convolucionales con kernels de $5 \times 5$, cada una seguida de average pooling, y tres capas densas. Aunque modesta para los estándares actuales (aproximadamente 60,000 parámetros), LeNet-5 estableció los principios fundamentales que se mantienen vigentes: campos receptivos locales, compartición de pesos y reducción espacial progresiva.

**AlexNet (Krizhevsky, Sutskever e Hinton, 2012, DOI: 10.1145/3065386).** Esta arquitectura representó el punto de inflexión que catapultó el aprendizaje profundo al centro de la investigación en inteligencia artificial. AlexNet ganó la competición ImageNet Large Scale Visual Recognition Challenge (ILSVRC) 2012 por un margen dramático, reduciendo el error top-5 del 26% al 15.3%. Sus innovaciones clave incluyeron el uso de activación ReLU (en lugar de sigmoid o tanh), dropout para regularización, aumento de datos (*data augmentation*) y entrenamiento paralelo en GPUs. La arquitectura tiene 8 capas (5 convolucionales y 3 densas) con aproximadamente 60 millones de parámetros.

**VGGNet (Simonyan y Zisserman, 2015, DOI: 10.48550/arXiv.1409.1556).** VGGNet demostró que la profundidad de la red es un factor crítico para el rendimiento. Su principal contribución fue el uso exclusivo de kernels $3 \times 3$ (los más pequeños que capturan la noción de izquierda/derecha, arriba/abajo, centro) en configuraciones de hasta 19 capas (VGG-19). Esta decisión de diseño mostró que apilar múltiples capas con kernels pequeños es más efectivo que usar pocas capas con kernels grandes, tanto en términos de parámetros como de capacidad de representación.

**ResNet (He et al., 2016, DOI: 10.1109/CVPR.2016.90).** Las redes residuales (ResNet) resolvieron el problema de la degradación del entrenamiento en redes muy profundas mediante la introducción de *conexiones residuales* (*skip connections*). En lugar de aprender la transformación completa $\mathcal{H}(\mathbf{x})$, cada bloque residual aprende la función residual $\mathcal{F}(\mathbf{x}) = \mathcal{H}(\mathbf{x}) - \mathbf{x}$, con la salida del bloque calculada como:

$$\mathbf{y} = \mathcal{F}(\mathbf{x}) + \mathbf{x}$$

Esta formulación facilita el flujo del gradiente durante la retropropagación y permite entrenar redes con cientos o incluso miles de capas. ResNet ganó ILSVRC 2015 con una red de 152 capas, superando por primera vez el rendimiento humano en la tarea de clasificación de ImageNet.

Estas arquitecturas no solo son relevantes históricamente, sino que sus principios de diseño (profundidad, kernels pequeños, conexiones residuales, normalización) se aplican directamente a las CNN utilizadas en sistemas de comunicaciones, como veremos en las secciones siguientes.

---

## 3.5 Convolución 1D para señales de telecomunicaciones

### 3.5.1 De 2D a 1D: adaptando las CNN para señales

Si bien las CNN fueron popularizadas por sus logros en visión por computadora (datos 2D), la operación de convolución se generaliza de manera natural a datos unidimensionales, como las señales temporales que son ubicuas en las telecomunicaciones. La convolución 1D se define como:

$$(\mathbf{x} * \mathbf{k})[n] = \sum_{m=0}^{K-1} \mathbf{x}[n + m] \cdot \mathbf{k}[m]$$

donde $\mathbf{x}$ es la señal de entrada de longitud $N$, $\mathbf{k}$ es el kernel de longitud $K$, y la salida tiene longitud $N - K + 1$ (sin padding). Esta operación es formalmente idéntica al filtrado digital, una operación fundamental en el procesamiento de señales.

La convolución 1D es particularmente adecuada para señales de telecomunicaciones por varias razones:

- Las señales de comunicación son inherentemente secuenciales (muestras ordenadas en el tiempo).
- Los patrones de interés (transiciones de fase, envolventes de amplitud, patrones de modulación) son locales y se repiten a lo largo de la señal.
- Las técnicas tradicionales de procesamiento de señales (filtros FIR/IIR, ecualización, detección) ya operan mediante convolución, por lo que las CNN 1D son una extensión natural que permite *aprender* los filtros óptimos directamente de los datos.

### 3.5.2 Procesamiento de señales de radiofrecuencia (RF)

En los sistemas de comunicación digital modernos, las señales de radiofrecuencia se capturan y procesan en banda base mediante conversores analógico-digitales (ADC). La señal resultante se representa comúnmente en formato de componentes en fase y cuadratura (I/Q), donde:

$$s(t) = I(t) \cos(2\pi f_c t) - Q(t) \sin(2\pi f_c t)$$

En banda base, cada muestra temporal se describe como un número complejo:

$$s[n] = I[n] + j \cdot Q[n]$$

donde $I[n]$ es la componente en fase y $Q[n]$ es la componente en cuadratura. Esta representación compleja codifica tanto la amplitud como la fase de la señal:

$$A[n] = \sqrt{I[n]^2 + Q[n]^2}, \qquad \phi[n] = \arctan\left(\frac{Q[n]}{I[n]}\right)$$

Para procesar señales I/Q con una CNN, la práctica estándar es representar la señal como una matriz de dimensiones $2 \times N$, donde la primera fila contiene las $N$ muestras de la componente en fase $I[n]$ y la segunda fila contiene las $N$ muestras de la componente en cuadratura $Q[n]$:

$$\mathbf{S} = \begin{bmatrix} I[0] & I[1] & I[2] & \cdots & I[N-1] \\ Q[0] & Q[1] & Q[2] & \cdots & Q[N-1] \end{bmatrix} \in \mathbb{R}^{2 \times N}$$

Esta representación preserva la relación entre las componentes I y Q en cada instante temporal, permitiendo a la CNN explotar tanto las correlaciones temporales (a lo largo del eje horizontal) como las correlaciones entre I y Q (a lo largo del eje vertical).

### 3.5.3 Filtros para patrones en señales de comunicación

Los kernels aprendidos por una CNN 1D para señales de telecomunicaciones desarrollan funcionalidades análogas a los filtros clásicos del procesamiento de señales, pero optimizados para la tarea específica de interés:

**Detectores de transiciones de fase.** En esquemas de modulación por desplazamiento de fase (PSK), la información se codifica en los cambios de fase de la señal portadora. Un kernel que ha aprendido a detectar transiciones de fase podría tener una forma similar a una derivada discreta, respondiendo con alta activación cuando las componentes I/Q cambian de manera consistente con una transición de fase específica (por ejemplo, de $0°$ a $180°$ en BPSK).

**Detectores de patrones de amplitud.** En esquemas de modulación por amplitud en cuadratura (QAM), tanto la amplitud como la fase codifican información. Algunos kernels aprenderán a detectar niveles de amplitud específicos o patrones de transición de amplitud que caracterizan diferentes órdenes de modulación.

**Filtros de ecualización adaptativa.** En canales con desvanecimiento (*fading*) o interferencia entre símbolos (ISI), algunos kernels pueden aprender funciones similares a un ecualizador, compensando las distorsiones del canal para extraer características más limpias de la señal.

La ventaja fundamental de las CNN sobre los métodos clásicos de procesamiento de señales radica en que estos filtros se aprenden automáticamente de los datos, sin requerir un diseño manual basado en modelos matemáticos del canal o la modulación. Esto es particularmente valioso en escenarios de comunicaciones semánticas, donde las características relevantes de la señal pueden no ser evidentes a priori.

**Figura 3.3:** *Convolución 1D aplicada a datos de señales I/Q. Se muestra una señal de entrada representada como una matriz $2 \times N$, donde la fila superior corresponde a la componente en fase $I[n]$ (representada en azul) y la fila inferior a la componente en cuadratura $Q[n]$ (representada en rojo). Un kernel de dimensiones $2 \times 7$ (altura 2 para abarcar ambos canales I/Q, ancho 7 para capturar un patrón temporal de 7 muestras) se desliza horizontalmente sobre la señal. En cada posición, el kernel realiza un producto punto con la submatriz correspondiente de la señal, produciendo un valor escalar en el mapa de características de salida (una secuencia 1D de longitud $N - 7 + 1$). Se destacan tres posiciones del kernel y sus activaciones resultantes. En la parte inferior, se muestran los pesos del kernel visualizados como un mapa de calor de $2 \times 7$, ilustrando cómo diferentes filas capturan patrones en I y Q respectivamente, mientras que las columnas capturan la evolución temporal del patrón.*

---

## 3.6 Caso práctico: Clasificación Automática de Modulación (AMC)

### 3.6.1 Descripción del problema

La clasificación automática de modulación (*Automatic Modulation Classification*, AMC) es una tarea fundamental en los sistemas de comunicaciones inalámbricas, con aplicaciones tanto en escenarios civiles como militares. El objetivo consiste en identificar el tipo de modulación utilizado por un transmisor a partir de las muestras de la señal recibida, sin conocimiento previo del esquema de modulación empleado. Formalmente, dado un vector de muestras I/Q recibidas $\mathbf{s} = \{s[0], s[1], \ldots, s[N-1]\}$, donde $s[n] = I[n] + jQ[n]$, el problema de AMC se formula como un problema de clasificación:

$$\hat{c} = \arg\max_{c \in \mathcal{C}} P(c \mid \mathbf{s})$$

donde $\mathcal{C} = \{\text{BPSK}, \text{QPSK}, \text{8PSK}, \text{QAM16}, \text{QAM64}, \text{GFSK}, \text{OFDM}, \ldots\}$ es el conjunto de esquemas de modulación posibles.

La AMC tiene múltiples aplicaciones prácticas de gran relevancia:

- **Radio cognitiva (*cognitive radio*).** Los sistemas de radio cognitiva necesitan identificar los esquemas de modulación de los usuarios primarios para adaptar sus propias transmisiones y evitar interferencias, o para reutilizar espectro de manera oportunista.
- **Monitoreo del espectro.** Los reguladores de telecomunicaciones utilizan AMC para supervisar el uso del espectro electromagnético, detectar transmisiones no autorizadas e identificar fuentes de interferencia.
- **Comunicaciones adaptativas.** En sistemas de modulación y codificación adaptativa (AMC/ACM), el receptor debe clasificar la modulación para decodificar correctamente los datos cuando el esquema cambia dinámicamente según las condiciones del canal.
- **Inteligencia de señales (SIGINT).** En aplicaciones de defensa, la identificación de la modulación es un paso crucial en la cadena de procesamiento de señales interceptadas.

Los enfoques tradicionales de AMC se basan en características diseñadas manualmente (*hand-crafted features*), como momentos estadísticos de orden superior, cumulantes, funciones de densidad espectral y características cíclicas. Estos métodos requieren un conocimiento profundo del dominio y pueden fallar cuando las condiciones del canal difieren de los modelos asumidos. Las CNN ofrecen una alternativa poderosa: aprender las características relevantes directamente de las muestras crudas de I/Q, eliminando la necesidad de ingeniería de características manual.

### 3.6.2 Arquitectura CNN para AMC

La arquitectura CNN para AMC que presentamos se basa en el trabajo seminal de O'Shea, Corgan y Clancy (2016, DOI: 10.1109/MILCOM.2016.7795369), quienes demostraron que las CNN pueden aprender a clasificar modulaciones directamente de datos I/Q crudos, igualando o superando a los métodos basados en características manuales. La arquitectura toma como entrada un tensor de dimensiones $(2, 128)$, donde:

- El primer eje (dimensión 2) corresponde a los dos canales: componente en fase $I[n]$ y componente en cuadratura $Q[n]$.
- El segundo eje (dimensión 128) corresponde a 128 muestras temporales consecutivas.

**Diseño del kernel: $(2, 7)$.** La elección del tamaño del kernel es crucial y merece una explicación detallada:

- **Altura $= 2$:** El kernel abarca ambas filas de la representación I/Q. Esto permite que cada filtro compute funciones que involucran simultáneamente las componentes $I[n]$ y $Q[n]$ en cada posición temporal. Dado que la información de modulación está codificada en la relación entre I y Q (por ejemplo, la constelación QAM se define por los pares $(I, Q)$ en el plano complejo), es esencial que el kernel pueda acceder a ambas componentes. Un kernel con altura $1$ solo vería una componente a la vez, perdiendo la capacidad de computar la fase $\phi = \arctan(Q/I)$ o la amplitud $A = \sqrt{I^2 + Q^2}$.

- **Ancho $= 7$:** El kernel cubre 7 muestras temporales consecutivas. Este ancho se escoge para capturar patrones temporales que abarcan varios períodos de símbolo. Dependiendo de la tasa de muestreo, 7 muestras pueden cubrir entre 1 y 3 símbolos, lo que permite detectar transiciones entre símbolos, patrones de conformación de pulso (*pulse shaping*) y la estructura temporal de la modulación. Un kernel demasiado estrecho (por ejemplo, ancho 1) solo vería una muestra I/Q aislada, perdiendo el contexto temporal. Un kernel demasiado ancho tendría demasiados parámetros y podría capturar correlaciones espurias.

- **Por qué esta forma funcional específica opera correctamente.** El kernel $(2, 7)$ realiza esencialmente una operación de filtrado lineal en el dominio complejo. Para cada posición del deslizamiento, el kernel computa:

$$y[n] = \sum_{m=0}^{6} \left( w_{I}[m] \cdot I[n+m] + w_{Q}[m] \cdot Q[n+m] \right)$$

donde $w_I[m] = K[0, m]$ y $w_Q[m] = K[1, m]$ son los pesos del kernel para las componentes I y Q respectivamente. Esta operación es equivalente a un filtro complejo $h[m] = w_I[m] + j \cdot w_Q[m]$ aplicado a la señal compleja $s[n] = I[n] + jQ[n]$, lo que conecta directamente la convolución de la CNN con el procesamiento clásico de señales en banda base.

La arquitectura completa se puede describir esquemáticamente:

1. **Entrada:** Tensor $(2, 128)$ — muestras I/Q
2. **Conv1 + ReLU:** 64 filtros de $(2, 7)$, stride $(1, 1)$, sin padding → Salida: $(64, 1, 122)$
3. **Conv2 + ReLU:** 32 filtros de $(1, 5)$, stride $(1, 1)$ → Salida: $(32, 1, 118)$
4. **Flatten:** Vector de $32 \times 118 = 3{,}776$ elementos
5. **Dense1 + ReLU:** 128 neuronas
6. **Dropout:** $p = 0.5$
7. **Dense2 + Softmax:** $C$ neuronas (una por cada tipo de modulación)

**Figura 3.4:** *Pipeline del sistema de clasificación automática de modulación (AMC) basado en CNN. De izquierda a derecha: (1) Una señal de radiofrecuencia es captada por una antena receptora. (2) Un conversor analógico-digital (ADC) muestrea la señal y la descompone en componentes I/Q. (3) Las muestras I/Q se organizan en una matriz $2 \times 128$ que sirve como entrada a la CNN. (4) La CNN procesa la señal a través de capas convolucionales 1D (con kernels de $(2,7)$) que extraen características de la señal, seguidas de capas densas. (5) La capa de salida softmax produce probabilidades para cada tipo de modulación posible (BPSK, QPSK, 8PSK, QAM16, QAM64, etc.). Se muestra una barra de probabilidades donde la clase predicha (por ejemplo, QPSK) tiene la probabilidad más alta. A lo largo del pipeline se indican las dimensiones del tensor en cada etapa.*

### 3.6.3 Implementación en PyTorch

A continuación, presentamos una implementación completa en PyTorch de la arquitectura CNN para AMC, con explicación línea por línea:

```python
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset

# ============================================================
# Definición de la arquitectura CNN para clasificación de modulación
# ============================================================

class ModulationCNN(nn.Module):
    """
    Red neuronal convolucional para clasificación automática de modulación.
    Recibe muestras I/Q crudas y predice el tipo de modulación.
    """

    def __init__(self, num_classes=8):
        """
        Inicializa las capas de la CNN.

        Args:
            num_classes: Número de tipos de modulación a clasificar.
                         Ejemplo: 8 para {BPSK, QPSK, 8PSK, QAM16,
                         QAM64, GFSK, CPFSK, PAM4}.
        """
        super(ModulationCNN, self).__init__()

        # --- Primera capa convolucional ---
        # nn.Conv2d(in_channels, out_channels, kernel_size)
        # in_channels=1: la entrada tiene 1 "imagen" (la matriz 2x128)
        # out_channels=64: aprendemos 64 filtros diferentes
        # kernel_size=(2, 7): altura=2 (cubre I y Q), ancho=7 (patrón temporal)
        # Cada filtro aprende un patrón I/Q-temporal diferente.
        self.conv1 = nn.Conv2d(
            in_channels=1,
            out_channels=64,
            kernel_size=(2, 7),
            stride=(1, 1),
            padding=0
        )
        # Activación ReLU: introduce no linealidad, permite combinaciones
        # complejas de características I/Q.
        self.relu1 = nn.ReLU()

        # --- Segunda capa convolucional ---
        # in_channels=64: recibe los 64 mapas de la capa anterior
        # out_channels=32: comprime a 32 mapas de características
        # kernel_size=(1, 5): altura=1 (dimensión I/Q ya fue colapsada),
        #                     ancho=5 (combina 5 posiciones temporales)
        # Esta capa combina las características de bajo nivel aprendidas
        # por conv1 en patrones temporales más complejos.
        self.conv2 = nn.Conv2d(
            in_channels=64,
            out_channels=32,
            kernel_size=(1, 5),
            stride=(1, 1),
            padding=0
        )
        self.relu2 = nn.ReLU()

        # --- Capa densa 1 ---
        # Después de conv1: salida espacial = (1, 122) → 64 canales
        # Después de conv2: salida espacial = (1, 118) → 32 canales
        # Flatten: 32 * 1 * 118 = 3776 elementos
        # La capa densa combina toda la información espacial y de canal
        # para formar una representación global de la señal.
        self.fc1 = nn.Linear(32 * 1 * 118, 128)
        self.relu3 = nn.ReLU()

        # --- Dropout para regularización ---
        # Durante el entrenamiento, desactiva aleatoriamente el 50% de
        # las neuronas para prevenir sobreajuste y forzar redundancia.
        self.dropout = nn.Dropout(p=0.5)

        # --- Capa de salida ---
        # Produce un logit por cada clase de modulación.
        # La función softmax se aplica implícitamente por
        # nn.CrossEntropyLoss durante el entrenamiento.
        self.fc2 = nn.Linear(128, num_classes)

    def forward(self, x):
        """
        Propagación hacia adelante.

        Args:
            x: Tensor de forma (batch_size, 1, 2, 128)
               batch_size: número de señales en el lote
               1: canal de la "imagen" (no confundir con I/Q)
               2: dimensión I/Q (fila 0 = I, fila 1 = Q)
               128: muestras temporales

        Returns:
            Tensor de logits de forma (batch_size, num_classes)
        """
        # Capa convolucional 1: (batch, 1, 2, 128) → (batch, 64, 1, 122)
        x = self.relu1(self.conv1(x))

        # Capa convolucional 2: (batch, 64, 1, 122) → (batch, 32, 1, 118)
        x = self.relu2(self.conv2(x))

        # Aplanar: (batch, 32, 1, 118) → (batch, 3776)
        x = x.view(x.size(0), -1)

        # Capa densa 1: (batch, 3776) → (batch, 128)
        x = self.relu3(self.fc1(x))

        # Dropout: desactiva neuronas aleatoriamente (solo en entrenamiento)
        x = self.dropout(x)

        # Capa de salida: (batch, 128) → (batch, num_classes)
        x = self.fc2(x)

        return x


# ============================================================
# Configuración del entrenamiento
# ============================================================

# Hiperparámetros
num_classes = 8        # Tipos de modulación
batch_size = 64        # Señales procesadas por iteración
learning_rate = 0.001  # Tasa de aprendizaje para Adam
num_epochs = 50        # Pasadas completas por el dataset

# Simulación de datos de ejemplo (en la práctica, se usaría un dataset
# real como RadioML 2016.10A o RadioML 2018.01A)
# X_train: (N, 1, 2, 128) - N señales, 1 canal, 2 filas I/Q, 128 muestras
# y_train: (N,) - etiquetas de modulación (enteros 0 a num_classes-1)
N_train = 10000
X_train = torch.randn(N_train, 1, 2, 128)  # Datos simulados
y_train = torch.randint(0, num_classes, (N_train,))  # Etiquetas simuladas

# Crear DataLoader para iteración eficiente por lotes
train_dataset = TensorDataset(X_train, y_train)
train_loader = DataLoader(
    train_dataset,
    batch_size=batch_size,
    shuffle=True  # Mezclar datos en cada época para mejor convergencia
)

# Instanciar el modelo
model = ModulationCNN(num_classes=num_classes)

# Función de pérdida: entropía cruzada (incluye softmax internamente)
# Es la elección estándar para clasificación multiclase.
criterion = nn.CrossEntropyLoss()

# Optimizador: Adam (combina momento y tasas de aprendizaje adaptativas)
optimizer = optim.Adam(model.parameters(), lr=learning_rate)

# ============================================================
# Bucle de entrenamiento
# ============================================================

for epoch in range(num_epochs):
    model.train()  # Modo entrenamiento: activa dropout y batch norm
    running_loss = 0.0
    correct = 0
    total = 0

    for batch_X, batch_y in train_loader:
        # 1. Limpiar gradientes de la iteración anterior
        optimizer.zero_grad()

        # 2. Propagación hacia adelante: calcular predicciones
        outputs = model(batch_X)

        # 3. Calcular la pérdida (entropía cruzada)
        loss = criterion(outputs, batch_y)

        # 4. Retropropagación: calcular gradientes de todos los parámetros
        loss.backward()

        # 5. Actualizar parámetros usando los gradientes calculados
        optimizer.step()

        # Estadísticas de entrenamiento
        running_loss += loss.item()
        _, predicted = torch.max(outputs.data, 1)
        total += batch_y.size(0)
        correct += (predicted == batch_y).sum().item()

    # Imprimir progreso cada 10 épocas
    if (epoch + 1) % 10 == 0:
        accuracy = 100.0 * correct / total
        avg_loss = running_loss / len(train_loader)
        print(f'Época [{epoch+1}/{num_epochs}], '
              f'Pérdida: {avg_loss:.4f}, '
              f'Precisión: {accuracy:.2f}%')

# ============================================================
# Inferencia (clasificación de nuevas señales)
# ============================================================

model.eval()  # Modo evaluación: desactiva dropout
with torch.no_grad():  # No calcular gradientes (ahorra memoria y tiempo)
    # Señal de prueba: una muestra I/Q de 128 puntos
    test_signal = torch.randn(1, 1, 2, 128)  # (1 señal, 1 canal, 2xI/Q, 128)
    output = model(test_signal)

    # Aplicar softmax para obtener probabilidades
    probabilities = torch.softmax(output, dim=1)

    # Obtener la clase predicha
    _, predicted_class = torch.max(probabilities, 1)

    modulation_names = ['BPSK', 'QPSK', '8PSK', 'QAM16',
                        'QAM64', 'GFSK', 'CPFSK', 'PAM4']
    print(f'\nModulación predicha: {modulation_names[predicted_class.item()]}')
    print(f'Probabilidades: {probabilities.squeeze().numpy()}')
```

Este código ilustra el pipeline completo de una CNN para AMC. En la práctica, el modelo se entrenaría con un dataset real como RadioML 2016.10A, que contiene señales simuladas bajo diversas condiciones de relación señal a ruido (SNR). Los resultados publicados en la literatura demuestran que este tipo de arquitectura alcanza precisiones superiores al 90% para valores de SNR moderados (por encima de 5 dB) en la clasificación de 8 a 11 tipos de modulación.

---

## 3.7 Autoencoders convolucionales para detección de anomalías

### 3.7.1 Concepto de autoencoder

Un autoencoder es una red neuronal que aprende a reconstruir su propia entrada. A diferencia de los modelos de clasificación que mapean entradas a etiquetas, un autoencoder aprende un mapeo identidad $f: \mathbb{R}^d \rightarrow \mathbb{R}^d$, pero con una restricción crucial: la información debe pasar a través de una representación intermedia (espacio latente) de dimensionalidad reducida. Esta restricción fuerza a la red a aprender una compresión eficiente de los datos, capturando solo las características más relevantes y descartando el ruido y la información redundante.

Formalmente, un autoencoder consta de dos componentes:

**Encoder (codificador).** Transforma la entrada $\mathbf{x} \in \mathbb{R}^d$ en una representación latente $\mathbf{z} \in \mathbb{R}^{d_z}$ con $d_z \ll d$:

$$\mathbf{z} = f_{\text{enc}}(\mathbf{x}; \theta_{\text{enc}})$$

donde $f_{\text{enc}}$ es la función del encoder parametrizada por $\theta_{\text{enc}}$. En un autoencoder convolucional, el encoder utiliza capas convolucionales con stride mayor que 1 (o pooling) para reducir progresivamente la dimensionalidad espacial.

**Decoder (decodificador).** Reconstruye la entrada original a partir de la representación latente:

$$\hat{\mathbf{x}} = f_{\text{dec}}(\mathbf{z}; \theta_{\text{dec}})$$

En un autoencoder convolucional, el decoder utiliza operaciones de convolución transpuesta (*transposed convolution* o *deconvolution*) para aumentar progresivamente la dimensionalidad espacial hasta recuperar las dimensiones originales de la entrada.

La composición de ambos componentes produce la reconstrucción:

$$\hat{\mathbf{x}} = f_{\text{dec}}(f_{\text{enc}}(\mathbf{x}; \theta_{\text{enc}}); \theta_{\text{dec}})$$

La arquitectura se denomina frecuentemente como un modelo de "reloj de arena" (*hourglass*) o "cuello de botella" (*bottleneck*), ya que las dimensiones se reducen en el encoder y se expanden en el decoder, con el punto más estrecho siendo el espacio latente.

### 3.7.2 Función de pérdida: error de reconstrucción

El autoencoder se entrena minimizando el error de reconstrucción entre la entrada original $\mathbf{x}$ y la salida reconstruida $\hat{\mathbf{x}}$. La función de pérdida más comúnmente utilizada es el error cuadrático medio (*Mean Squared Error*, MSE):

$$L(\theta_{\text{enc}}, \theta_{\text{dec}}) = \frac{1}{N} \sum_{i=1}^{N} ||\mathbf{x}_i - \hat{\mathbf{x}}_i||^2$$

donde $N$ es el número de muestras en el conjunto de entrenamiento y $||\cdot||^2$ denota la norma $L^2$ al cuadrado. Para una señal individual, la pérdida de reconstrucción es:

$$L = ||\mathbf{x} - \hat{\mathbf{x}}||^2 = \sum_{j=1}^{d} (x_j - \hat{x}_j)^2$$

Esta función de pérdida tiene una interpretación probabilística: minimizar el MSE es equivalente a maximizar la log-verosimilitud bajo un modelo gaussiano con varianza constante:

$$\log p(\mathbf{x} \mid \hat{\mathbf{x}}) = -\frac{d}{2}\log(2\pi\sigma^2) - \frac{1}{2\sigma^2}||\mathbf{x} - \hat{\mathbf{x}}||^2$$

Alternativas al MSE incluyen el error absoluto medio (MAE, o norma $L^1$), que es más robusto a valores atípicos, y la divergencia de Kullback-Leibler, utilizada en autoencoders variacionales (VAE).

### 3.7.3 Entrenamiento con datos "normales" y detección de anomalías

La clave de la detección de anomalías mediante autoencoders reside en una estrategia de entrenamiento asimétrica: el autoencoder se entrena exclusivamente con datos que representan el comportamiento "normal" o esperado del sistema. Durante el entrenamiento, la red aprende a comprimir y reconstruir con alta fidelidad los patrones normales, ya que estos son los únicos que observa repetidamente.

Una vez entrenado, el autoencoder se utiliza para evaluar nuevas señales. Si una señal es "normal" (similar a los datos de entrenamiento), el autoencoder la reconstruirá con un error bajo, ya que ha aprendido las regularidades de ese tipo de datos. Si la señal es "anómala" (diferente de los patrones normales), el autoencoder no podrá reconstruirla adecuadamente, produciendo un error de reconstrucción elevado.

Formalmente, se define un umbral de anomalía $\tau$ y se clasifica cada señal según:

$$\text{Decisión}(\mathbf{x}) = \begin{cases} \text{Normal} & \text{si } ||\mathbf{x} - \hat{\mathbf{x}}||^2 \leq \tau \\ \text{Anomalía} & \text{si } ||\mathbf{x} - \hat{\mathbf{x}}||^2 > \tau \end{cases}$$

El umbral $\tau$ se determina típicamente a partir de la distribución de errores de reconstrucción sobre un conjunto de validación de datos normales. Una elección común es establecer $\tau$ como el percentil 95 o 99 de esta distribución:

$$\tau = Q_{1-\alpha}(\{L_i\}_{i=1}^{N_{\text{val}}})$$

donde $Q_{1-\alpha}$ denota el cuantil $(1-\alpha)$ y $\alpha$ es la tasa de falsa alarma deseada.

Esta metodología tiene una ventaja fundamental: no requiere ejemplos de anomalías para el entrenamiento. Esto es especialmente valioso en telecomunicaciones, donde las anomalías pueden ser eventos raros, diversos e impredecibles (nuevos tipos de interferencia, ataques de *jamming* no anticipados, fallos de hardware novedosos).

### 3.7.4 Aplicación: detección de señales anómalas en telecomunicaciones

En el contexto de las telecomunicaciones, los autoencoders convolucionales pueden aplicarse para detectar una amplia variedad de anomalías en señales de radiofrecuencia:

**Detección de interferencia.** Un autoencoder entrenado con señales "limpias" (sin interferencia) producirá un error de reconstrucción elevado cuando la señal recibida contenga interferencia de fuentes externas, ya que los patrones de interferencia no forman parte de la distribución aprendida.

**Detección de *jamming*.** Los ataques de *jamming* introducen señales artificiales diseñadas para degradar las comunicaciones. Estos ataques generan patrones en las señales I/Q que difieren de las comunicaciones legítimas, produciendo errores de reconstrucción anómalos.

**Detección de fallos de hardware.** Fallos en los componentes del transmisor o receptor (amplificadores no lineales, osciladores con deriva de frecuencia, conversores defectuosos) generan distorsiones características en la señal que el autoencoder puede detectar como anomalías.

**Monitoreo de calidad del canal.** Cambios abruptos en las condiciones del canal (desvanecimiento profundo, obstrucciones súbitas, cambios en el entorno de propagación) se reflejan como alteraciones en las características estadísticas de la señal que elevan el error de reconstrucción.

La arquitectura de un autoencoder convolucional para señales I/Q sigue una estructura simétrica. El encoder aplica capas convolucionales con stride 2 para reducir progresivamente la dimensión temporal, mientras que el decoder utiliza convoluciones transpuestas con stride 2 para expandir la dimensión temporal hasta recuperar la longitud original. Por ejemplo:

**Encoder:**
$$\mathbf{x} \in \mathbb{R}^{2 \times 128} \xrightarrow{\text{Conv}(16, (2,7), s=2)} \mathbb{R}^{16 \times 1 \times 61} \xrightarrow{\text{Conv}(32, (1,5), s=2)} \mathbb{R}^{32 \times 1 \times 29} \xrightarrow{\text{Conv}(64, (1,3), s=2)} \mathbb{R}^{64 \times 1 \times 14}$$

**Espacio latente:** $\mathbf{z} \in \mathbb{R}^{64 \times 1 \times 14}$ (compresión de $256$ a $896$ valores, aunque con mayor número de canales que capturan la estructura de los datos)

**Decoder:**
$$\mathbf{z} \xrightarrow{\text{ConvT}(32, (1,3), s=2)} \mathbb{R}^{32 \times 1 \times 29} \xrightarrow{\text{ConvT}(16, (1,5), s=2)} \mathbb{R}^{16 \times 1 \times 61} \xrightarrow{\text{ConvT}(1, (2,7), s=2)} \mathbb{R}^{1 \times 2 \times 128}$$

En la práctica, las dimensiones exactas del decoder requieren ajustes de relleno (*output padding*) para garantizar que la salida tenga exactamente las mismas dimensiones que la entrada. La función de pérdida MSE se calcula sobre todos los valores de la señal reconstruida:

$$L = \frac{1}{2 \times 128} \sum_{c=0}^{1} \sum_{n=0}^{127} (x[c, n] - \hat{x}[c, n])^2$$

donde $c \in \{0, 1\}$ indexa las componentes I y Q, y $n$ indexa las muestras temporales.

Durante la operación, el sistema monitorea continuamente el error de reconstrucción. Un incremento sostenido por encima del umbral $\tau$ activa una alarma que puede desencadenar acciones correctivas: cambio de frecuencia de operación, activación de mecanismos anti-*jamming*, notificación al operador de red, o adaptación automática de los parámetros de transmisión. En el contexto de las comunicaciones semánticas, esta capacidad de detección de anomalías es particularmente relevante, ya que permite al sistema identificar cuándo las condiciones del canal o el entorno de transmisión se desvían de lo esperado, adaptando dinámicamente la codificación semántica para mantener la fidelidad de la comunicación.

---

### Resumen de la Sección 3

En esta sección hemos desarrollado exhaustivamente los fundamentos de las redes neuronales convolucionales, desde la motivación teórica y la definición matemática de la convolución hasta sus aplicaciones prácticas en telecomunicaciones. Los conceptos clave incluyen:

- La operación de convolución como alternativa eficiente a las capas densas, explotando localidad, compartición de pesos e invarianza a traslaciones.
- Los componentes de una CNN: capas convolucionales (con sus hiperparámetros de kernel, stride y padding), capas de pooling (Max y Average), y capas densas finales.
- La fórmula del tamaño de salida: $o = \lfloor (n + 2p - k) / s \rfloor + 1$.
- Las arquitecturas clásicas (LeNet-5, AlexNet, VGG, ResNet) y sus contribuciones al campo.
- La convolución 1D y su aplicación natural al procesamiento de señales I/Q.
- Un caso práctico completo de clasificación automática de modulación (AMC) con implementación en PyTorch.
- Los autoencoders convolucionales para detección de anomalías en señales de telecomunicaciones.

Estos conceptos forman la base para entender cómo las CNN se integran en los sistemas de comunicaciones semánticas, donde la extracción de características relevantes de señales complejas es un requisito fundamental.

---

# 4. Redes Neuronales Recurrentes (RNN) y LSTM

En las secciones anteriores de este tutorial hemos estudiado los perceptrones multicapa (MLP) y las redes neuronales convolucionales (CNN), dos arquitecturas fundamentales del aprendizaje profundo que han demostrado un rendimiento sobresaliente en tareas de clasificación, regresión y procesamiento de señales e imágenes. Sin embargo, estas arquitecturas presentan una limitación fundamental cuando se enfrentan a datos de naturaleza secuencial: carecen de un mecanismo intrínseco para capturar dependencias temporales. En el contexto de las comunicaciones semánticas, la información que se transmite frecuentemente adopta la forma de secuencias —texto, voz, series temporales de señales de canal, tramas de bits correlacionadas en el tiempo— lo que exige arquitecturas capaces de modelar la estructura temporal inherente a estos datos. Las redes neuronales recurrentes (RNN, *Recurrent Neural Networks*) y sus variantes avanzadas, particularmente las redes de memoria a largo-corto plazo (LSTM, *Long Short-Term Memory*), fueron diseñadas precisamente para abordar este desafío.

Esta sección presenta un tratamiento riguroso y pedagógico de las RNN, LSTM y sus variantes, comenzando desde la motivación fundamental, pasando por la formulación matemática completa, e incluyendo ejemplos numéricos detallados y una implementación práctica en PyTorch. Comprender estas arquitecturas es esencial no solo por su relevancia histórica, sino porque constituyen los cimientos sobre los cuales se han construido los sistemas modernos de comunicación semántica basados en codificación conjunta fuente-canal (*Joint Source-Channel Coding*, JSCC) para datos secuenciales.

---

## 4.1 Motivación: procesamiento de secuencias

### 4.1.1 Por qué los MLP y las CNN son insuficientes para datos secuenciales

Consideremos la tarea de predecir la siguiente palabra en una oración, estimar el estado futuro de un canal de comunicaciones inalámbricas, o decodificar una secuencia de símbolos transmitidos a través de un canal con memoria. En todos estos casos, el dato en el instante $t$ depende no solo de la entrada actual, sino de las entradas en instantes anteriores $t-1, t-2, \ldots, t-k$. Esta dependencia temporal es una característica fundamental de los datos secuenciales.

Un MLP estándar procesa cada entrada de forma independiente. Si deseamos que un MLP procese una secuencia de longitud $T$, podemos concatenar todos los elementos de la secuencia en un único vector de entrada $\mathbf{x} = [\mathbf{x}_1, \mathbf{x}_2, \ldots, \mathbf{x}_T]$. Sin embargo, este enfoque presenta múltiples problemas graves:

1. **Longitud fija de entrada**: El MLP requiere que el vector de entrada tenga una dimensión fija, lo que impide procesar secuencias de longitud variable sin técnicas de relleno (*padding*) o truncamiento que introducen artefactos.

2. **Explosión de parámetros**: Para una secuencia de longitud $T$ donde cada elemento tiene dimensión $d$, el vector de entrada tendría dimensión $Td$. Si la primera capa oculta tiene $H$ neuronas, la matriz de pesos $\mathbf{W}^{(1)} \in \mathbb{R}^{H \times Td}$ crece linealmente con la longitud de la secuencia, lo que resulta computacionalmente prohibitivo para secuencias largas.

3. **Ausencia de compartición de parámetros temporal**: En un MLP, los pesos que procesan la entrada en el instante $t=1$ son completamente distintos de los que procesan la entrada en $t=2$. Esto significa que el modelo no puede generalizar un patrón aprendido en una posición temporal a otra posición. Si el modelo aprende que la secuencia de símbolos "01" en la posición $t=5$ tiene cierto significado semántico, no puede transferir automáticamente ese conocimiento cuando la misma secuencia aparece en la posición $t=100$.

4. **No captura el orden**: Un MLP trata la concatenación $[\mathbf{x}_1, \mathbf{x}_2, \mathbf{x}_3]$ de manera fundamentalmente diferente a $[\mathbf{x}_3, \mathbf{x}_1, \mathbf{x}_2]$ solo porque los pesos son diferentes en cada posición, no porque tenga un mecanismo explícito para comprender la noción de orden o causalidad temporal.

Las CNN, por su parte, ofrecen una mejora parcial gracias a la compartición de parámetros a través de filtros convolucionales y la capacidad de capturar patrones locales. Una CNN 1D puede aplicar filtros a lo largo de la dimensión temporal, capturando dependencias dentro de una ventana receptiva local. Sin embargo, las CNN también presentan limitaciones significativas para el procesamiento secuencial:

- **Campo receptivo limitado**: Un filtro de tamaño $k$ solo puede capturar dependencias dentro de una ventana de $k$ pasos temporales. Para capturar dependencias a largo plazo, se requieren múltiples capas apiladas o filtros dilatados (*dilated convolutions*), lo que complica la arquitectura.

- **No mantienen estado**: Las CNN procesan toda la secuencia de una vez, sin mantener un estado interno que evolucione a medida que se procesan los elementos secuencialmente. Esto las hace menos naturales para tareas donde la predicción en el instante $t$ depende críticamente de toda la historia previa.

- **Causalidad**: Las CNN estándar aplican filtros que abarcan posiciones futuras y pasadas simultáneamente. Para aplicaciones causales (donde solo se dispone de información pasada), se requieren convoluciones causales (*causal convolutions*), que restringen el campo receptivo y complican el diseño.

### 4.1.2 Datos donde el orden importa

Los datos secuenciales son ubicuos tanto en las telecomunicaciones como en la inteligencia artificial en general. Algunos ejemplos representativos incluyen:

**Series temporales de canal**: En un sistema de comunicaciones inalámbricas, la respuesta del canal $h(t)$ varía en el tiempo debido al movimiento relativo entre transmisor y receptor, la dispersión por múltiples trayectos (*multipath*) y las variaciones del entorno. Predecir el estado futuro del canal a partir de sus valores pasados es un problema inherentemente secuencial. Los coeficientes de desvanecimiento (*fading*) en un canal Rayleigh exhiben correlación temporal que puede ser explotada por un modelo recurrente para mejorar la estimación y predicción de canal.

**Texto y lenguaje natural**: En comunicaciones semánticas, el transmisor puede necesar codificar texto en una representación semántica compacta para su transmisión. La comprensión del texto requiere modelar dependencias a larga distancia: en la oración "El ingeniero que diseñó el sistema de antenas MIMO para la estación base *terminó* el proyecto", el verbo "terminó" depende del sujeto "El ingeniero" a pesar de la distancia de múltiples palabras.

**Señales de voz y audio**: La señal de voz es intrínsecamente temporal, donde cada muestra depende de las anteriores. Los fonemas, las palabras y las oraciones se desarrollan a lo largo del tiempo, y su interpretación correcta requiere considerar el contexto temporal completo.

**Secuencias de símbolos codificados**: En sistemas de codificación de canal, las secuencias de bits codificadas tienen estructura temporal introducida por el codificador. Los códigos convolucionales, por ejemplo, producen símbolos de salida que dependen de los bits de entrada actuales y de un número finito de bits anteriores, almacenados en registros de desplazamiento. Un decodificador basado en redes neuronales recurrentes puede aprender a explotar esta estructura temporal.

### 4.1.3 El concepto de memoria en redes neuronales

La idea central que motiva las redes recurrentes es dotar a la red neuronal de **memoria**: la capacidad de mantener y actualizar un estado interno que resuma la información relevante de las entradas procesadas hasta el momento. Este concepto se puede formalizar de la siguiente manera.

Definimos una función de transición de estado $\phi$ que, dado el estado actual $\mathbf{h}_{t-1}$ y una nueva entrada $\mathbf{x}_t$, produce un nuevo estado $\mathbf{h}_t$:

$$\mathbf{h}_t = \phi(\mathbf{h}_{t-1}, \mathbf{x}_t)$$

y una función de salida $\psi$ que produce la salida $\mathbf{y}_t$ a partir del estado actual:

$$\mathbf{y}_t = \psi(\mathbf{h}_t)$$

El estado oculto $\mathbf{h}_t \in \mathbb{R}^{d_h}$ actúa como una memoria comprimida de toda la secuencia procesada hasta el instante $t$. Idealmente, $\mathbf{h}_t$ debería contener toda la información de $\mathbf{x}_1, \mathbf{x}_2, \ldots, \mathbf{x}_t$ que sea relevante para la tarea en cuestión.

Esta formulación tiene una analogía directa con los sistemas dinámicos en teoría de control y con los modelos ocultos de Markov (*Hidden Markov Models*, HMM) ampliamente utilizados en telecomunicaciones. La diferencia fundamental es que, en una RNN, las funciones $\phi$ y $\psi$ son parametrizadas por redes neuronales cuyos parámetros se aprenden a partir de los datos, en lugar de ser especificadas manualmente o estimadas mediante algoritmos como Baum-Welch.

La capacidad de mantener memoria es lo que distingue a las redes recurrentes de las redes *feedforward*. Mientras que un MLP implementa una función estática $\mathbf{y} = f(\mathbf{x})$ sin estado interno, una RNN implementa un sistema dinámico donde la salida depende tanto de la entrada actual como del historial acumulado en el estado oculto. Esta propiedad es fundamental para las comunicaciones semánticas, donde el significado de un símbolo o una palabra frecuentemente depende del contexto proporcionado por los elementos anteriores de la secuencia.

---

## 4.2 La Red Neuronal Recurrente (RNN) básica

### 4.2.1 Arquitectura: el estado oculto que se retroalimenta

La red neuronal recurrente (RNN) básica, también conocida como RNN de Elman (en honor a Jeffrey Elman, quien popularizó esta arquitectura en 1990), implementa las funciones de transición y salida mediante transformaciones afines seguidas de funciones de activación no lineales. La característica definitoria de la RNN es la presencia de una **conexión recurrente**: la salida de la capa oculta en el instante $t-1$ se retroalimenta como entrada adicional en el instante $t$.

La arquitectura de una celda RNN básica consta de tres componentes principales:

1. **Capa de entrada**: Recibe el vector de entrada $\mathbf{x}_t \in \mathbb{R}^{d_x}$ en cada paso temporal $t$.
2. **Capa oculta recurrente**: Mantiene un vector de estado oculto $\mathbf{h}_t \in \mathbb{R}^{d_h}$ que se actualiza en cada paso temporal incorporando tanto la entrada actual como el estado oculto anterior.
3. **Capa de salida**: Produce un vector de salida $\mathbf{y}_t \in \mathbb{R}^{d_y}$ a partir del estado oculto actual.

La conexión recurrente $\mathbf{h}_{t-1} \to \mathbf{h}_t$ es la que confiere a la red su capacidad de memoria. Sin esta conexión, la RNN se reduciría a un MLP aplicado independientemente en cada paso temporal.

### 4.2.2 Formulación matemática

La dinámica de una RNN básica se describe mediante las siguientes ecuaciones:

**Estado oculto:**

$$\mathbf{h}_t = f\!\left(\mathbf{W}_{hh}\mathbf{h}_{t-1} + \mathbf{W}_{xh}\mathbf{x}_t + \mathbf{b}_h\right)$$

**Salida:**

$$\mathbf{y}_t = g\!\left(\mathbf{W}_{hy}\mathbf{h}_t + \mathbf{b}_y\right)$$

donde:

- $\mathbf{x}_t \in \mathbb{R}^{d_x}$ es el vector de entrada en el paso temporal $t$.
- $\mathbf{h}_t \in \mathbb{R}^{d_h}$ es el vector de estado oculto en el paso temporal $t$.
- $\mathbf{h}_{t-1} \in \mathbb{R}^{d_h}$ es el vector de estado oculto en el paso temporal anterior $t-1$.
- $\mathbf{y}_t \in \mathbb{R}^{d_y}$ es el vector de salida en el paso temporal $t$.
- $\mathbf{W}_{xh} \in \mathbb{R}^{d_h \times d_x}$ es la matriz de pesos de entrada a oculta. Transforma la entrada $\mathbf{x}_t$ al espacio del estado oculto.
- $\mathbf{W}_{hh} \in \mathbb{R}^{d_h \times d_h}$ es la matriz de pesos de oculta a oculta, también llamada **matriz de recurrencia**. Es la responsable de la retroalimentación temporal y constituye el elemento diferenciador de la RNN respecto a una red *feedforward*.
- $\mathbf{W}_{hy} \in \mathbb{R}^{d_y \times d_h}$ es la matriz de pesos de oculta a salida.
- $\mathbf{b}_h \in \mathbb{R}^{d_h}$ es el vector de sesgo de la capa oculta.
- $\mathbf{b}_y \in \mathbb{R}^{d_y}$ es el vector de sesgo de la capa de salida.
- $f(\cdot)$ es la función de activación de la capa oculta, típicamente $\tanh$ o ReLU.
- $g(\cdot)$ es la función de activación de la capa de salida, que depende de la tarea (softmax para clasificación, lineal para regresión, sigmoide para probabilidades).

Es crucial observar que las matrices de pesos $\mathbf{W}_{xh}$, $\mathbf{W}_{hh}$ y $\mathbf{W}_{hy}$ son **compartidas a lo largo de todos los pasos temporales**. Esto significa que la misma transformación se aplica en cada instante $t$, independientemente de la longitud de la secuencia. Esta compartición de parámetros tiene dos consecuencias importantes:

1. **Eficiencia paramétrica**: El número total de parámetros entrenables de la RNN es independiente de la longitud de la secuencia. Específicamente, el número de parámetros es $d_h \times d_x + d_h \times d_h + d_h + d_y \times d_h + d_y = d_h(d_x + d_h + 1) + d_y(d_h + 1)$, que depende únicamente de las dimensiones de entrada, oculta y salida, no de $T$.

2. **Generalización temporal**: Un patrón aprendido en una posición temporal puede aplicarse automáticamente en cualquier otra posición, de manera análoga a como los filtros convolucionales generalizan a través del espacio.

El estado oculto $\mathbf{h}_t$ se inicializa típicamente como el vector cero $\mathbf{h}_0 = \mathbf{0}$, aunque en algunas aplicaciones puede inicializarse con un vector aprendido o proporcionado por otra red.

Analicemos con mayor detalle la ecuación del estado oculto. El argumento de la función de activación es:

$$\mathbf{a}_t = \mathbf{W}_{hh}\mathbf{h}_{t-1} + \mathbf{W}_{xh}\mathbf{x}_t + \mathbf{b}_h$$

Este vector $\mathbf{a}_t \in \mathbb{R}^{d_h}$, llamado **preactivación**, es la suma de tres componentes:

- $\mathbf{W}_{hh}\mathbf{h}_{t-1}$: la contribución del estado oculto anterior, que codifica la "memoria" de la secuencia procesada hasta $t-1$.
- $\mathbf{W}_{xh}\mathbf{x}_t$: la contribución de la entrada actual, que aporta información nueva.
- $\mathbf{b}_h$: el sesgo, que permite desplazar la preactivación independientemente de las entradas.

La función de activación $f$ aplica una transformación no lineal a $\mathbf{a}_t$ para obtener $\mathbf{h}_t = f(\mathbf{a}_t)$. La elección de $f = \tanh$ es particularmente común en las RNN porque produce valores en el rango $(-1, 1)$, lo que ayuda a mantener los valores del estado oculto acotados a lo largo de múltiples pasos temporales. Si se utilizara una activación sin saturación como ReLU, los valores del estado oculto podrían crecer sin límite a lo largo de la secuencia.

Una forma alternativa y compacta de escribir las ecuaciones de la RNN es concatenar $\mathbf{h}_{t-1}$ y $\mathbf{x}_t$ en un único vector y utilizar una sola matriz de pesos. Definimos:

$$\mathbf{W} = [\mathbf{W}_{hh} \mid \mathbf{W}_{xh}] \in \mathbb{R}^{d_h \times (d_h + d_x)}$$

y el vector concatenado:

$$[\mathbf{h}_{t-1}, \mathbf{x}_t] \in \mathbb{R}^{d_h + d_x}$$

Entonces la ecuación del estado oculto se puede reescribir como:

$$\mathbf{h}_t = f\!\left(\mathbf{W}[\mathbf{h}_{t-1}, \mathbf{x}_t] + \mathbf{b}_h\right)$$

Esta notación concatenada es la que se utiliza con mayor frecuencia en la literatura moderna y en las implementaciones de software como PyTorch y TensorFlow.

### 4.2.3 Despliegue de la RNN en el tiempo

Para comprender mejor cómo fluye la información a través de una RNN, resulta útil "desplegar" (*unroll*) la red en el tiempo. El despliegue consiste en representar explícitamente la RNN como una red *feedforward* profunda donde cada capa corresponde a un paso temporal.

Dado una secuencia de entrada $(\mathbf{x}_1, \mathbf{x}_2, \ldots, \mathbf{x}_T)$, el despliegue produce las siguientes ecuaciones:

$$\mathbf{h}_1 = f(\mathbf{W}_{hh}\mathbf{h}_0 + \mathbf{W}_{xh}\mathbf{x}_1 + \mathbf{b}_h)$$
$$\mathbf{h}_2 = f(\mathbf{W}_{hh}\mathbf{h}_1 + \mathbf{W}_{xh}\mathbf{x}_2 + \mathbf{b}_h)$$
$$\mathbf{h}_3 = f(\mathbf{W}_{hh}\mathbf{h}_2 + \mathbf{W}_{xh}\mathbf{x}_3 + \mathbf{b}_h)$$
$$\vdots$$
$$\mathbf{h}_T = f(\mathbf{W}_{hh}\mathbf{h}_{T-1} + \mathbf{W}_{xh}\mathbf{x}_T + \mathbf{b}_h)$$

Y las salidas correspondientes:

$$\mathbf{y}_t = g(\mathbf{W}_{hy}\mathbf{h}_t + \mathbf{b}_y), \quad t = 1, 2, \ldots, T$$

**Figura 4.1:** *Diagrama de una celda RNN y su versión desplegada en el tiempo. A la izquierda se muestra la representación compacta de una celda RNN con la conexión recurrente indicada por una flecha circular. La celda recibe la entrada $\mathbf{x}_t$ y el estado oculto anterior $\mathbf{h}_{t-1}$, produce el nuevo estado oculto $\mathbf{h}_t$ y la salida $\mathbf{y}_t$. A la derecha se muestra la misma red desplegada a lo largo de cuatro pasos temporales ($t=1, 2, 3, 4$). Cada copia de la celda comparte los mismos parámetros $\mathbf{W}_{xh}$, $\mathbf{W}_{hh}$, $\mathbf{W}_{hy}$, $\mathbf{b}_h$ y $\mathbf{b}_y$. Las entradas $\mathbf{x}_1, \mathbf{x}_2, \mathbf{x}_3, \mathbf{x}_4$ alimentan a la red desde abajo, los estados ocultos $\mathbf{h}_0 \to \mathbf{h}_1 \to \mathbf{h}_2 \to \mathbf{h}_3 \to \mathbf{h}_4$ fluyen horizontalmente de izquierda a derecha conectando las celdas, y las salidas $\mathbf{y}_1, \mathbf{y}_2, \mathbf{y}_3, \mathbf{y}_4$ se producen en la parte superior. El estado inicial $\mathbf{h}_0$ se inicializa típicamente como el vector cero.*

La vista desplegada revela que una RNN procesando una secuencia de longitud $T$ es equivalente a una red *feedforward* con $T$ capas, donde cada capa comparte los mismos pesos. Esta equivalencia es fundamental para el entrenamiento, ya que permite aplicar el algoritmo de retropropagación estándar a la red desplegada.

Es importante notar que existen diferentes configuraciones de entrada-salida para las RNN, dependiendo de la tarea:

- **Muchos a muchos** (*many-to-many*): Se produce una salida en cada paso temporal. Ejemplo: traducción automática, decodificación símbolo por símbolo.
- **Muchos a uno** (*many-to-one*): Se procesa toda la secuencia y se produce una única salida al final ($\mathbf{y}_T$). Ejemplo: clasificación de sentimiento, detección de tipo de modulación.
- **Uno a muchos** (*one-to-many*): Se proporciona una única entrada y se genera una secuencia de salida. Ejemplo: generación de texto a partir de un vector de contexto.

### 4.2.4 Retropropagación a través del tiempo (BPTT)

El entrenamiento de una RNN se realiza mediante el algoritmo de **retropropagación a través del tiempo** (BPTT, *Backpropagation Through Time*), que es simplemente la aplicación del algoritmo de retropropagación estándar a la RNN desplegada en el tiempo.

Supongamos que la función de pérdida total para una secuencia de longitud $T$ es la suma de las pérdidas en cada paso temporal:

$$\mathcal{L} = \sum_{t=1}^{T} \mathcal{L}_t(\mathbf{y}_t, \hat{\mathbf{y}}_t)$$

donde $\hat{\mathbf{y}}_t$ es la etiqueta verdadera en el paso $t$ y $\mathcal{L}_t$ es la función de pérdida en ese paso (por ejemplo, entropía cruzada para clasificación o error cuadrático medio para regresión).

Para actualizar los parámetros de la red, necesitamos calcular los gradientes de $\mathcal{L}$ con respecto a cada parámetro. Consideremos el gradiente con respecto a la matriz de recurrencia $\mathbf{W}_{hh}$. Dado que $\mathbf{W}_{hh}$ se utiliza en todos los pasos temporales, su gradiente total es la suma de las contribuciones de cada paso:

$$\frac{\partial \mathcal{L}}{\partial \mathbf{W}_{hh}} = \sum_{t=1}^{T} \frac{\partial \mathcal{L}_t}{\partial \mathbf{W}_{hh}}$$

Para calcular $\frac{\partial \mathcal{L}_t}{\partial \mathbf{W}_{hh}}$, debemos aplicar la regla de la cadena a través de todos los pasos temporales desde $t$ hasta $1$. La pérdida $\mathcal{L}_t$ depende de $\mathbf{y}_t$, que depende de $\mathbf{h}_t$, que a su vez depende de $\mathbf{h}_{t-1}$, y así sucesivamente hasta $\mathbf{h}_1$. Por lo tanto:

$$\frac{\partial \mathcal{L}_t}{\partial \mathbf{W}_{hh}} = \sum_{k=1}^{t} \frac{\partial \mathcal{L}_t}{\partial \mathbf{y}_t} \frac{\partial \mathbf{y}_t}{\partial \mathbf{h}_t} \left(\prod_{j=k+1}^{t} \frac{\partial \mathbf{h}_j}{\partial \mathbf{h}_{j-1}}\right) \frac{\partial \mathbf{h}_k}{\partial \mathbf{W}_{hh}}$$

El término $\frac{\partial \mathbf{h}_j}{\partial \mathbf{h}_{j-1}}$ es la Jacobiana de la transición de estado, que para la RNN básica con activación $f$ es:

$$\frac{\partial \mathbf{h}_j}{\partial \mathbf{h}_{j-1}} = \text{diag}\!\left(f'(\mathbf{a}_j)\right) \cdot \mathbf{W}_{hh}$$

donde $\mathbf{a}_j = \mathbf{W}_{hh}\mathbf{h}_{j-1} + \mathbf{W}_{xh}\mathbf{x}_j + \mathbf{b}_h$ y $\text{diag}(f'(\mathbf{a}_j))$ es la matriz diagonal con las derivadas de la función de activación evaluadas en las preactivaciones.

### 4.2.5 El problema del gradiente desvaneciente

El producto de Jacobianas que aparece en la expresión del gradiente es la fuente de uno de los problemas más fundamentales del entrenamiento de RNN: el **problema del gradiente desvaneciente** (*vanishing gradient problem*), identificado formalmente por Hochreiter (1991) y analizado en profundidad por Bengio, Simard y Frasconi (1994).

Consideremos el producto:

$$\prod_{j=k+1}^{t} \frac{\partial \mathbf{h}_j}{\partial \mathbf{h}_{j-1}} = \prod_{j=k+1}^{t} \text{diag}\!\left(f'(\mathbf{a}_j)\right) \cdot \mathbf{W}_{hh}$$

Para analizar el comportamiento de este producto, examinemos su norma. Utilizando la propiedad de submultiplicatividad de la norma matricial:

$$\left\|\prod_{j=k+1}^{t} \frac{\partial \mathbf{h}_j}{\partial \mathbf{h}_{j-1}}\right\| \leq \prod_{j=k+1}^{t} \left\|\text{diag}\!\left(f'(\mathbf{a}_j)\right)\right\| \cdot \left\|\mathbf{W}_{hh}\right\|$$

Si utilizamos la función de activación $\tanh$, su derivada satisface $0 < f'(a) = 1 - \tanh^2(a) \leq 1$ para todo $a$. Sea $\gamma = \max_j \|f'(\mathbf{a}_j)\|_\infty \leq 1$ y $\lambda_{\max}$ el mayor valor singular de $\mathbf{W}_{hh}$. Entonces:

$$\left\|\prod_{j=k+1}^{t} \frac{\partial \mathbf{h}_j}{\partial \mathbf{h}_{j-1}}\right\| \leq (\gamma \cdot \lambda_{\max})^{t-k}$$

Este resultado tiene consecuencias dramáticas:

- Si $\gamma \cdot \lambda_{\max} < 1$: El producto decrece exponencialmente con la distancia temporal $(t-k)$. Para dependencias a largo plazo donde $t - k$ es grande, el gradiente se vuelve exponencialmente pequeño — **se desvanece**. Esto significa que la red no puede aprender dependencias temporales a largo plazo porque el gradiente de la pérdida con respecto a las entradas antiguas es esencialmente cero.

- Si $\gamma \cdot \lambda_{\max} > 1$: El producto crece exponencialmente — **el gradiente explota**. Los gradientes se vuelven enormes, causando actualizaciones de parámetros inestables y divergencia del entrenamiento. Este caso es técnicamente más fácil de manejar (mediante *gradient clipping*), pero igualmente problemático.

- Si $\gamma \cdot \lambda_{\max} \approx 1$: El gradiente se mantiene estable, pero este régimen es difícil de mantener en la práctica.

Para ilustrar numéricamente la gravedad del problema, supongamos $\gamma \cdot \lambda_{\max} = 0.9$ y consideremos una secuencia de longitud $T = 100$. El gradiente de una dependencia que abarque 50 pasos temporales se atenuaría por un factor de $0.9^{50} \approx 0.0052$, y para 100 pasos: $0.9^{100} \approx 2.66 \times 10^{-5}$. En la práctica, con valores de $\gamma$ menores (la derivada de $\tanh$ es frecuentemente mucho menor que 1 para preactivaciones grandes), la atenuación puede ser aún más severa.

Este problema impone una **barrera fundamental** a las RNN básicas: en la práctica, solo pueden aprender dependencias temporales que abarquen unas pocas decenas de pasos temporales. Para secuencias más largas, la información de los pasos iniciales se pierde irrecuperablemente durante la retropropagación. Esta limitación motivó directamente el desarrollo de las redes LSTM, que abordaremos en la siguiente subsección.

La técnica de **recorte de gradientes** (*gradient clipping*), propuesta por Pascanu, Mikolov y Bengio (2013), mitiga parcialmente el problema de la explosión de gradientes al limitar la norma del vector de gradientes:

$$\text{Si } \|\nabla\mathcal{L}\| > \theta, \quad \nabla\mathcal{L} \leftarrow \frac{\theta}{\|\nabla\mathcal{L}\|} \nabla\mathcal{L}$$

donde $\theta$ es un umbral predefinido. Sin embargo, el recorte de gradientes no resuelve el problema del desvanecimiento, que requiere cambios arquitectónicos fundamentales.

---

## 4.3 Long Short-Term Memory (LSTM)

### 4.3.1 Motivación: resolver el problema del gradiente desvaneciente

La red de **memoria a largo-corto plazo** (LSTM, *Long Short-Term Memory*) fue propuesta por Hochreiter y Schmidhuber en 1997 como una solución arquitectónica al problema del gradiente desvaneciente. La idea fundamental de la LSTM es introducir un **camino de gradiente directo** a través del tiempo, de manera que los gradientes puedan fluir a lo largo de muchos pasos temporales sin atenuarse exponencialmente.

La innovación clave de la LSTM es la introducción del **estado de celda** (*cell state*) $\mathbf{C}_t$, un vector que actúa como una "cinta transportadora" de información a lo largo del tiempo. El estado de celda se actualiza mediante operaciones aditivas y multiplicativas controladas por **puertas** (*gates*) que aprenden a regular el flujo de información. Crucialmente, la actualización del estado de celda incluye un término aditivo que permite que los gradientes fluyan a través de él sin multiplicaciones matriciales repetidas, evitando así el desvanecimiento exponencial.

La LSTM fue posteriormente refinada por Gers, Schmidhuber y Cummins (2000), quienes añadieron la puerta de olvido (*forget gate*), y su formulación moderna se consolidó como el estándar de facto para el procesamiento de secuencias hasta la llegada de la arquitectura Transformer.

### 4.3.2 El estado de celda como "cinta transportadora"

El estado de celda $\mathbf{C}_t \in \mathbb{R}^{d_h}$ es un vector que atraviesa toda la cadena temporal de la red, sufriendo solo interacciones lineales menores (multiplicaciones punto a punto y sumas) en cada paso temporal. Esta propiedad es análoga a una cinta transportadora en una fábrica: la información puede viajar a lo largo de muchos pasos temporales con modificaciones mínimas, sin pasar por las transformaciones no lineales altamente compresivas que caracterizan a la RNN básica.

La ecuación de actualización del estado de celda tiene la forma:

$$\mathbf{C}_t = \mathbf{f}_t \odot \mathbf{C}_{t-1} + \mathbf{i}_t \odot \tilde{\mathbf{C}}_t$$

donde $\odot$ denota el producto de Hadamard (multiplicación elemento a elemento). Observemos que esta ecuación es **lineal en $\mathbf{C}_{t-1}$** (modulada por $\mathbf{f}_t$), lo que significa que el gradiente $\frac{\partial \mathbf{C}_t}{\partial \mathbf{C}_{t-1}} = \text{diag}(\mathbf{f}_t)$, que es simplemente una matriz diagonal cuyos elementos están en $[0, 1]$. Cuando la puerta de olvido está cerca de 1, el gradiente fluye sin atenuación, resolviendo el problema del gradiente desvaneciente para las dependencias codificadas en el estado de celda.

### 4.3.3 Las tres puertas: formulación matemática completa

La LSTM utiliza tres puertas (*gates*) —la puerta de olvido, la puerta de entrada y la puerta de salida— para controlar el flujo de información hacia, dentro de y desde el estado de celda. Cada puerta es un vector cuyos elementos están en el intervalo $[0, 1]$, producido por una función sigmoide aplicada a una transformación afín de las entradas.

A continuación, presentamos las ecuaciones completas de la LSTM, donde $\mathbf{x}_t \in \mathbb{R}^{d_x}$ es la entrada, $\mathbf{h}_{t-1} \in \mathbb{R}^{d_h}$ es el estado oculto anterior, y $\mathbf{C}_{t-1} \in \mathbb{R}^{d_h}$ es el estado de celda anterior.

#### Puerta de olvido (*Forget Gate*)

$$\mathbf{f}_t = \sigma\!\left(\mathbf{W}_f [\mathbf{h}_{t-1}, \mathbf{x}_t] + \mathbf{b}_f\right)$$

La puerta de olvido determina **qué información del estado de celda anterior debe descartarse**. El vector $\mathbf{f}_t \in \mathbb{R}^{d_h}$ tiene elementos en $[0, 1]$: un valor de 0 indica "olvidar completamente" y un valor de 1 indica "recordar completamente". La notación $[\mathbf{h}_{t-1}, \mathbf{x}_t]$ denota la concatenación de los vectores $\mathbf{h}_{t-1}$ y $\mathbf{x}_t$, resultando en un vector de dimensión $d_h + d_x$. La matriz de pesos $\mathbf{W}_f \in \mathbb{R}^{d_h \times (d_h + d_x)}$ y el vector de sesgo $\mathbf{b}_f \in \mathbb{R}^{d_h}$ son parámetros aprendidos durante el entrenamiento. La función sigmoide $\sigma(z) = \frac{1}{1+e^{-z}}$ asegura que los valores de la puerta estén en el rango $(0, 1)$.

Intuitivamente, la puerta de olvido actúa como un "filtro de relevancia temporal". Consideremos una analogía con las comunicaciones: si un codificador semántico está procesando una oración y encuentra un punto final, la puerta de olvido puede aprender a "reiniciar" partes del estado de celda que almacenaban información sobre la oración anterior, ya que esa información ya no es relevante para procesar la siguiente oración.

#### Puerta de entrada (*Input Gate*) y celda candidata

$$\mathbf{i}_t = \sigma\!\left(\mathbf{W}_i [\mathbf{h}_{t-1}, \mathbf{x}_t] + \mathbf{b}_i\right)$$

$$\tilde{\mathbf{C}}_t = \tanh\!\left(\mathbf{W}_C [\mathbf{h}_{t-1}, \mathbf{x}_t] + \mathbf{b}_C\right)$$

La puerta de entrada opera en dos pasos. Primero, el vector $\mathbf{i}_t \in \mathbb{R}^{d_h}$ determina **qué componentes del estado de celda se actualizarán** con nueva información. Segundo, el vector $\tilde{\mathbf{C}}_t \in \mathbb{R}^{d_h}$ es la **celda candidata**, que contiene los valores potenciales que podrían añadirse al estado de celda. La celda candidata se calcula mediante una transformación afín seguida de $\tanh$, que produce valores en $(-1, 1)$. Las matrices $\mathbf{W}_i \in \mathbb{R}^{d_h \times (d_h + d_x)}$, $\mathbf{W}_C \in \mathbb{R}^{d_h \times (d_h + d_x)}$ y los vectores de sesgo $\mathbf{b}_i, \mathbf{b}_C \in \mathbb{R}^{d_h}$ son parámetros aprendidos independientes de los de la puerta de olvido.

La analogía para la puerta de entrada es la de un "controlador de escritura" en una memoria. El vector $\mathbf{i}_t$ decide qué posiciones de la memoria se van a escribir, y $\tilde{\mathbf{C}}_t$ contiene los datos que se van a escribir. Solo donde $\mathbf{i}_t$ tiene valores altos se incorporará la información de $\tilde{\mathbf{C}}_t$ al estado de celda.

#### Actualización del estado de celda

$$\mathbf{C}_t = \mathbf{f}_t \odot \mathbf{C}_{t-1} + \mathbf{i}_t \odot \tilde{\mathbf{C}}_t$$

Esta ecuación combina las dos operaciones anteriores. El primer término $\mathbf{f}_t \odot \mathbf{C}_{t-1}$ retiene selectivamente la información del estado anterior (según lo que la puerta de olvido decida preservar), y el segundo término $\mathbf{i}_t \odot \tilde{\mathbf{C}}_t$ añade nueva información (filtrada por la puerta de entrada). La operación $\odot$ es el producto de Hadamard, que opera elemento a elemento:

$$[\mathbf{C}_t]_j = [\mathbf{f}_t]_j \cdot [\mathbf{C}_{t-1}]_j + [\mathbf{i}_t]_j \cdot [\tilde{\mathbf{C}}_t]_j, \quad j = 1, 2, \ldots, d_h$$

Cada componente $j$ del estado de celda se actualiza de forma independiente, lo que permite que diferentes "ranuras" de memoria almacenen y olviden información de manera independiente. Algunas componentes pueden mantener información durante cientos de pasos temporales (cuando $[\mathbf{f}_t]_j \approx 1$ consistentemente), mientras que otras se actualizan frecuentemente.

#### Puerta de salida (*Output Gate*) y estado oculto

$$\mathbf{o}_t = \sigma\!\left(\mathbf{W}_o [\mathbf{h}_{t-1}, \mathbf{x}_t] + \mathbf{b}_o\right)$$

$$\mathbf{h}_t = \mathbf{o}_t \odot \tanh(\mathbf{C}_t)$$

La puerta de salida $\mathbf{o}_t \in \mathbb{R}^{d_h}$ determina **qué partes del estado de celda se exponen como estado oculto**. El estado de celda $\mathbf{C}_t$ pasa primero por una función $\tanh$ para normalizar sus valores al rango $(-1, 1)$, y luego se filtra por la puerta de salida mediante el producto de Hadamard. El estado oculto resultante $\mathbf{h}_t$ es lo que se pasa a la siguiente celda LSTM y, opcionalmente, a la capa de salida para producir la predicción.

La puerta de salida implementa un "controlador de lectura": el estado de celda puede contener mucha información almacenada, pero solo una fracción de ella es relevante para la salida en el instante actual. Por ejemplo, en un sistema de comunicación semántica que procesa texto, el estado de celda puede almacenar información sobre el sujeto, el verbo y el objeto de una oración simultáneamente, pero en un momento dado solo necesita exponer la información relevante para predecir el siguiente token.

**Figura 4.2:** *Diagrama detallado de la arquitectura interna de una celda LSTM. La celda recibe tres entradas: la entrada actual $\mathbf{x}_t$ (desde abajo), el estado oculto anterior $\mathbf{h}_{t-1}$ (desde la izquierda) y el estado de celda anterior $\mathbf{C}_{t-1}$ (desde la izquierda, por la línea horizontal superior que representa la "cinta transportadora"). Dentro de la celda se muestran: (1) La puerta de olvido $\mathbf{f}_t$, representada por un nodo con el símbolo $\sigma$, que recibe $[\mathbf{h}_{t-1}, \mathbf{x}_t]$ y produce un vector que se multiplica punto a punto ($\odot$) con $\mathbf{C}_{t-1}$. (2) La puerta de entrada $\mathbf{i}_t$ (nodo $\sigma$) y la celda candidata $\tilde{\mathbf{C}}_t$ (nodo $\tanh$), ambas recibiendo $[\mathbf{h}_{t-1}, \mathbf{x}_t]$; sus salidas se multiplican punto a punto y el resultado se suma ($+$) al estado de celda filtrado, produciendo $\mathbf{C}_t$. (3) La puerta de salida $\mathbf{o}_t$ (nodo $\sigma$), que recibe $[\mathbf{h}_{t-1}, \mathbf{x}_t]$; su salida se multiplica punto a punto con $\tanh(\mathbf{C}_t)$ para producir el estado oculto $\mathbf{h}_t$. Las salidas de la celda son $\mathbf{C}_t$ (hacia la derecha por la cinta transportadora) y $\mathbf{h}_t$ (hacia la derecha y hacia arriba). Los nodos circulares representan operaciones punto a punto ($\odot$ para multiplicación, $+$ para suma), y los nodos rectangulares representan capas neuronales con la activación indicada ($\sigma$ o $\tanh$).*

### 4.3.4 Recuento de parámetros

Es instructivo calcular el número total de parámetros de una celda LSTM, ya que esto ilustra el costo computacional respecto a una RNN básica. La LSTM tiene cuatro conjuntos de parámetros (uno para cada una de las tres puertas y uno para la celda candidata):

- Puerta de olvido: $\mathbf{W}_f \in \mathbb{R}^{d_h \times (d_h + d_x)}$, $\mathbf{b}_f \in \mathbb{R}^{d_h}$ → $d_h(d_h + d_x) + d_h$ parámetros
- Puerta de entrada: $\mathbf{W}_i \in \mathbb{R}^{d_h \times (d_h + d_x)}$, $\mathbf{b}_i \in \mathbb{R}^{d_h}$ → $d_h(d_h + d_x) + d_h$ parámetros
- Celda candidata: $\mathbf{W}_C \in \mathbb{R}^{d_h \times (d_h + d_x)}$, $\mathbf{b}_C \in \mathbb{R}^{d_h}$ → $d_h(d_h + d_x) + d_h$ parámetros
- Puerta de salida: $\mathbf{W}_o \in \mathbb{R}^{d_h \times (d_h + d_x)}$, $\mathbf{b}_o \in \mathbb{R}^{d_h}$ → $d_h(d_h + d_x) + d_h$ parámetros

**Total**: $4 \cdot [d_h(d_h + d_x) + d_h] = 4d_h(d_h + d_x + 1)$

Comparado con una RNN básica que tiene $d_h(d_h + d_x) + d_h = d_h(d_h + d_x + 1)$ parámetros (excluyendo la capa de salida), la LSTM tiene exactamente **4 veces más parámetros**. Este incremento es el precio de la capacidad de mantener gradientes estables a lo largo del tiempo, y en la práctica es un compromiso altamente favorable dado el dramático mejoramiento en el aprendizaje de dependencias a largo plazo.

### 4.3.5 Ejemplo numérico detallado

Para consolidar la comprensión de las ecuaciones de la LSTM, trabajemos un ejemplo numérico completo con dimensiones pequeñas: $d_x = 2$ (dimensión de entrada) y $d_h = 2$ (dimensión del estado oculto). Procesaremos una secuencia de 3 pasos temporales.

**Inicialización de parámetros** (valores simplificados para facilitar el cálculo):

Para todas las matrices de pesos, usaremos la notación $\mathbf{W}_g \in \mathbb{R}^{2 \times 4}$ (ya que $d_h + d_x = 4$), y para los vectores de sesgo, $\mathbf{b}_g \in \mathbb{R}^2$.

$$\mathbf{W}_f = \begin{bmatrix} 0.5 & 0.1 & 0.2 & 0.3 \\ 0.4 & 0.6 & 0.1 & 0.2 \end{bmatrix}, \quad \mathbf{b}_f = \begin{bmatrix} 0.1 \\ 0.1 \end{bmatrix}$$

$$\mathbf{W}_i = \begin{bmatrix} 0.3 & 0.2 & 0.5 & 0.1 \\ 0.1 & 0.4 & 0.3 & 0.6 \end{bmatrix}, \quad \mathbf{b}_i = \begin{bmatrix} 0.0 \\ 0.0 \end{bmatrix}$$

$$\mathbf{W}_C = \begin{bmatrix} 0.2 & 0.3 & 0.4 & 0.1 \\ 0.5 & 0.1 & 0.2 & 0.3 \end{bmatrix}, \quad \mathbf{b}_C = \begin{bmatrix} 0.0 \\ 0.0 \end{bmatrix}$$

$$\mathbf{W}_o = \begin{bmatrix} 0.4 & 0.2 & 0.1 & 0.5 \\ 0.3 & 0.5 & 0.4 & 0.2 \end{bmatrix}, \quad \mathbf{b}_o = \begin{bmatrix} 0.1 \\ 0.1 \end{bmatrix}$$

**Estado inicial**: $\mathbf{h}_0 = [0, 0]^\top$, $\mathbf{C}_0 = [0, 0]^\top$.

**Secuencia de entrada**: $\mathbf{x}_1 = [1, 0]^\top$, $\mathbf{x}_2 = [0, 1]^\top$, $\mathbf{x}_3 = [1, 1]^\top$.

---

**Paso temporal $t = 1$:**

Vector concatenado: $[\mathbf{h}_0, \mathbf{x}_1] = [0, 0, 1, 0]^\top$

**Puerta de olvido:**

$$\mathbf{W}_f [\mathbf{h}_0, \mathbf{x}_1] + \mathbf{b}_f = \begin{bmatrix} 0.5 \cdot 0 + 0.1 \cdot 0 + 0.2 \cdot 1 + 0.3 \cdot 0 \\ 0.4 \cdot 0 + 0.6 \cdot 0 + 0.1 \cdot 1 + 0.2 \cdot 0 \end{bmatrix} + \begin{bmatrix} 0.1 \\ 0.1 \end{bmatrix} = \begin{bmatrix} 0.3 \\ 0.2 \end{bmatrix}$$

$$\mathbf{f}_1 = \sigma\!\left(\begin{bmatrix} 0.3 \\ 0.2 \end{bmatrix}\right) = \begin{bmatrix} 0.574 \\ 0.550 \end{bmatrix}$$

**Puerta de entrada:**

$$\mathbf{W}_i [\mathbf{h}_0, \mathbf{x}_1] + \mathbf{b}_i = \begin{bmatrix} 0.3 \cdot 0 + 0.2 \cdot 0 + 0.5 \cdot 1 + 0.1 \cdot 0 \\ 0.1 \cdot 0 + 0.4 \cdot 0 + 0.3 \cdot 1 + 0.6 \cdot 0 \end{bmatrix} = \begin{bmatrix} 0.5 \\ 0.3 \end{bmatrix}$$

$$\mathbf{i}_1 = \sigma\!\left(\begin{bmatrix} 0.5 \\ 0.3 \end{bmatrix}\right) = \begin{bmatrix} 0.622 \\ 0.574 \end{bmatrix}$$

**Celda candidata:**

$$\mathbf{W}_C [\mathbf{h}_0, \mathbf{x}_1] + \mathbf{b}_C = \begin{bmatrix} 0.2 \cdot 0 + 0.3 \cdot 0 + 0.4 \cdot 1 + 0.1 \cdot 0 \\ 0.5 \cdot 0 + 0.1 \cdot 0 + 0.2 \cdot 1 + 0.3 \cdot 0 \end{bmatrix} = \begin{bmatrix} 0.4 \\ 0.2 \end{bmatrix}$$

$$\tilde{\mathbf{C}}_1 = \tanh\!\left(\begin{bmatrix} 0.4 \\ 0.2 \end{bmatrix}\right) = \begin{bmatrix} 0.380 \\ 0.197 \end{bmatrix}$$

**Actualización del estado de celda:**

$$\mathbf{C}_1 = \mathbf{f}_1 \odot \mathbf{C}_0 + \mathbf{i}_1 \odot \tilde{\mathbf{C}}_1 = \begin{bmatrix} 0.574 \\ 0.550 \end{bmatrix} \odot \begin{bmatrix} 0 \\ 0 \end{bmatrix} + \begin{bmatrix} 0.622 \\ 0.574 \end{bmatrix} \odot \begin{bmatrix} 0.380 \\ 0.197 \end{bmatrix} = \begin{bmatrix} 0.236 \\ 0.113 \end{bmatrix}$$

Nótese que, dado que $\mathbf{C}_0 = \mathbf{0}$, el primer término es cero y el estado de celda se inicializa completamente a partir de la celda candidata filtrada por la puerta de entrada.

**Puerta de salida:**

$$\mathbf{W}_o [\mathbf{h}_0, \mathbf{x}_1] + \mathbf{b}_o = \begin{bmatrix} 0.4 \cdot 0 + 0.2 \cdot 0 + 0.1 \cdot 1 + 0.5 \cdot 0 \\ 0.3 \cdot 0 + 0.5 \cdot 0 + 0.4 \cdot 1 + 0.2 \cdot 0 \end{bmatrix} + \begin{bmatrix} 0.1 \\ 0.1 \end{bmatrix} = \begin{bmatrix} 0.2 \\ 0.5 \end{bmatrix}$$

$$\mathbf{o}_1 = \sigma\!\left(\begin{bmatrix} 0.2 \\ 0.5 \end{bmatrix}\right) = \begin{bmatrix} 0.550 \\ 0.622 \end{bmatrix}$$

**Estado oculto:**

$$\mathbf{h}_1 = \mathbf{o}_1 \odot \tanh(\mathbf{C}_1) = \begin{bmatrix} 0.550 \\ 0.622 \end{bmatrix} \odot \tanh\!\left(\begin{bmatrix} 0.236 \\ 0.113 \end{bmatrix}\right) = \begin{bmatrix} 0.550 \\ 0.622 \end{bmatrix} \odot \begin{bmatrix} 0.232 \\ 0.113 \end{bmatrix} = \begin{bmatrix} 0.128 \\ 0.070 \end{bmatrix}$$

---

**Paso temporal $t = 2$:**

Vector concatenado: $[\mathbf{h}_1, \mathbf{x}_2] = [0.128, 0.070, 0, 1]^\top$

**Puerta de olvido:**

$$\mathbf{W}_f [\mathbf{h}_1, \mathbf{x}_2] + \mathbf{b}_f = \begin{bmatrix} 0.5(0.128) + 0.1(0.070) + 0.2(0) + 0.3(1) \\ 0.4(0.128) + 0.6(0.070) + 0.1(0) + 0.2(1) \end{bmatrix} + \begin{bmatrix} 0.1 \\ 0.1 \end{bmatrix}$$

$$= \begin{bmatrix} 0.064 + 0.007 + 0 + 0.3 + 0.1 \\ 0.051 + 0.042 + 0 + 0.2 + 0.1 \end{bmatrix} = \begin{bmatrix} 0.471 \\ 0.393 \end{bmatrix}$$

$$\mathbf{f}_2 = \sigma\!\left(\begin{bmatrix} 0.471 \\ 0.393 \end{bmatrix}\right) = \begin{bmatrix} 0.616 \\ 0.597 \end{bmatrix}$$

**Puerta de entrada:**

$$\mathbf{W}_i [\mathbf{h}_1, \mathbf{x}_2] + \mathbf{b}_i = \begin{bmatrix} 0.3(0.128) + 0.2(0.070) + 0.5(0) + 0.1(1) \\ 0.1(0.128) + 0.4(0.070) + 0.3(0) + 0.6(1) \end{bmatrix} = \begin{bmatrix} 0.152 \\ 0.641 \end{bmatrix}$$

$$\mathbf{i}_2 = \sigma\!\left(\begin{bmatrix} 0.152 \\ 0.641 \end{bmatrix}\right) = \begin{bmatrix} 0.538 \\ 0.655 \end{bmatrix}$$

**Celda candidata:**

$$\mathbf{W}_C [\mathbf{h}_1, \mathbf{x}_2] + \mathbf{b}_C = \begin{bmatrix} 0.2(0.128) + 0.3(0.070) + 0.4(0) + 0.1(1) \\ 0.5(0.128) + 0.1(0.070) + 0.2(0) + 0.3(1) \end{bmatrix} = \begin{bmatrix} 0.147 \\ 0.371 \end{bmatrix}$$

$$\tilde{\mathbf{C}}_2 = \tanh\!\left(\begin{bmatrix} 0.147 \\ 0.371 \end{bmatrix}\right) = \begin{bmatrix} 0.146 \\ 0.355 \end{bmatrix}$$

**Actualización del estado de celda:**

$$\mathbf{C}_2 = \mathbf{f}_2 \odot \mathbf{C}_1 + \mathbf{i}_2 \odot \tilde{\mathbf{C}}_2 = \begin{bmatrix} 0.616 \\ 0.597 \end{bmatrix} \odot \begin{bmatrix} 0.236 \\ 0.113 \end{bmatrix} + \begin{bmatrix} 0.538 \\ 0.655 \end{bmatrix} \odot \begin{bmatrix} 0.146 \\ 0.355 \end{bmatrix} = \begin{bmatrix} 0.145 + 0.079 \\ 0.067 + 0.233 \end{bmatrix} = \begin{bmatrix} 0.224 \\ 0.300 \end{bmatrix}$$

Observemos cómo la puerta de olvido retiene parcialmente la información del paso anterior ($\mathbf{f}_2 \approx 0.6$), mientras que la puerta de entrada permite la incorporación de nueva información.

**Puerta de salida y estado oculto:**

$$\mathbf{o}_2 = \sigma\!\left(\mathbf{W}_o [\mathbf{h}_1, \mathbf{x}_2] + \mathbf{b}_o\right)$$

$$\mathbf{W}_o [\mathbf{h}_1, \mathbf{x}_2] + \mathbf{b}_o = \begin{bmatrix} 0.4(0.128) + 0.2(0.070) + 0.1(0) + 0.5(1) + 0.1 \\ 0.3(0.128) + 0.5(0.070) + 0.4(0) + 0.2(1) + 0.1 \end{bmatrix} = \begin{bmatrix} 0.665 \\ 0.373 \end{bmatrix}$$

$$\mathbf{o}_2 = \sigma\!\left(\begin{bmatrix} 0.665 \\ 0.373 \end{bmatrix}\right) = \begin{bmatrix} 0.660 \\ 0.592 \end{bmatrix}$$

$$\mathbf{h}_2 = \mathbf{o}_2 \odot \tanh(\mathbf{C}_2) = \begin{bmatrix} 0.660 \\ 0.592 \end{bmatrix} \odot \begin{bmatrix} 0.220 \\ 0.291 \end{bmatrix} = \begin{bmatrix} 0.145 \\ 0.172 \end{bmatrix}$$

---

**Paso temporal $t = 3$:**

Vector concatenado: $[\mathbf{h}_2, \mathbf{x}_3] = [0.145, 0.172, 1, 1]^\top$

**Puerta de olvido:**

$$\mathbf{W}_f [\mathbf{h}_2, \mathbf{x}_3] + \mathbf{b}_f = \begin{bmatrix} 0.5(0.145) + 0.1(0.172) + 0.2(1) + 0.3(1) + 0.1 \\ 0.4(0.145) + 0.6(0.172) + 0.1(1) + 0.2(1) + 0.1 \end{bmatrix} = \begin{bmatrix} 0.690 \\ 0.561 \end{bmatrix}$$

$$\mathbf{f}_3 = \sigma\!\left(\begin{bmatrix} 0.690 \\ 0.561 \end{bmatrix}\right) = \begin{bmatrix} 0.666 \\ 0.637 \end{bmatrix}$$

**Puerta de entrada:**

$$\mathbf{W}_i [\mathbf{h}_2, \mathbf{x}_3] + \mathbf{b}_i = \begin{bmatrix} 0.3(0.145) + 0.2(0.172) + 0.5(1) + 0.1(1) \\ 0.1(0.145) + 0.4(0.172) + 0.3(1) + 0.6(1) \end{bmatrix} = \begin{bmatrix} 0.678 \\ 0.983 \end{bmatrix}$$

$$\mathbf{i}_3 = \sigma\!\left(\begin{bmatrix} 0.678 \\ 0.983 \end{bmatrix}\right) = \begin{bmatrix} 0.663 \\ 0.728 \end{bmatrix}$$

**Celda candidata:**

$$\mathbf{W}_C [\mathbf{h}_2, \mathbf{x}_3] + \mathbf{b}_C = \begin{bmatrix} 0.2(0.145) + 0.3(0.172) + 0.4(1) + 0.1(1) \\ 0.5(0.145) + 0.1(0.172) + 0.2(1) + 0.3(1) \end{bmatrix} = \begin{bmatrix} 0.581 \\ 0.590 \end{bmatrix}$$

$$\tilde{\mathbf{C}}_3 = \tanh\!\left(\begin{bmatrix} 0.581 \\ 0.590 \end{bmatrix}\right) = \begin{bmatrix} 0.523 \\ 0.530 \end{bmatrix}$$

**Actualización del estado de celda:**

$$\mathbf{C}_3 = \mathbf{f}_3 \odot \mathbf{C}_2 + \mathbf{i}_3 \odot \tilde{\mathbf{C}}_3 = \begin{bmatrix} 0.666(0.224) + 0.663(0.523) \\ 0.637(0.300) + 0.728(0.530) \end{bmatrix} = \begin{bmatrix} 0.149 + 0.347 \\ 0.191 + 0.386 \end{bmatrix} = \begin{bmatrix} 0.496 \\ 0.577 \end{bmatrix}$$

**Puerta de salida y estado oculto:**

$$\mathbf{W}_o [\mathbf{h}_2, \mathbf{x}_3] + \mathbf{b}_o = \begin{bmatrix} 0.4(0.145) + 0.2(0.172) + 0.1(1) + 0.5(1) + 0.1 \\ 0.3(0.145) + 0.5(0.172) + 0.4(1) + 0.2(1) + 0.1 \end{bmatrix} = \begin{bmatrix} 0.792 \\ 0.830 \end{bmatrix}$$

$$\mathbf{o}_3 = \sigma\!\left(\begin{bmatrix} 0.792 \\ 0.830 \end{bmatrix}\right) = \begin{bmatrix} 0.688 \\ 0.696 \end{bmatrix}$$

$$\mathbf{h}_3 = \mathbf{o}_3 \odot \tanh(\mathbf{C}_3) = \begin{bmatrix} 0.688 \\ 0.696 \end{bmatrix} \odot \begin{bmatrix} 0.457 \\ 0.520 \end{bmatrix} = \begin{bmatrix} 0.314 \\ 0.362 \end{bmatrix}$$

---

**Resumen del ejemplo:**

| Paso $t$ | $\mathbf{f}_t$ | $\mathbf{i}_t$ | $\tilde{\mathbf{C}}_t$ | $\mathbf{C}_t$ | $\mathbf{o}_t$ | $\mathbf{h}_t$ |
|-----------|-----------|-----------|-------------|-----------|-----------|-----------|
| 1 | [0.574, 0.550] | [0.622, 0.574] | [0.380, 0.197] | [0.236, 0.113] | [0.550, 0.622] | [0.128, 0.070] |
| 2 | [0.616, 0.597] | [0.538, 0.655] | [0.146, 0.355] | [0.224, 0.300] | [0.660, 0.592] | [0.145, 0.172] |
| 3 | [0.666, 0.637] | [0.663, 0.728] | [0.523, 0.530] | [0.496, 0.577] | [0.688, 0.696] | [0.314, 0.362] |

Este ejemplo ilustra varios aspectos importantes. Primero, los valores de las puertas son moderados (en el rango 0.5-0.7) debido a que los pesos son pequeños y las entradas al sigmoide están cerca de cero. En la práctica, después del entrenamiento, las puertas tienden a producir valores más extremos (cercanos a 0 o 1), lo que resulta en decisiones más definidas de "olvidar" o "recordar". Segundo, el estado de celda $\mathbf{C}_t$ acumula gradualmente información a lo largo de la secuencia, creciendo de $[0.236, 0.113]$ a $[0.496, 0.577]$. Tercero, el estado oculto $\mathbf{h}_t$ es siempre más pequeño en magnitud que el estado de celda, debido al filtrado por la puerta de salida y la compresión de $\tanh$.

### 4.3.6 Análisis del flujo de gradientes en la LSTM

Para comprender formalmente por qué la LSTM resuelve el problema del gradiente desvaneciente, examinemos el gradiente del estado de celda. A partir de la ecuación de actualización:

$$\mathbf{C}_t = \mathbf{f}_t \odot \mathbf{C}_{t-1} + \mathbf{i}_t \odot \tilde{\mathbf{C}}_t$$

el gradiente del estado de celda futuro con respecto al estado de celda pasado es:

$$\frac{\partial \mathbf{C}_t}{\partial \mathbf{C}_{t-1}} = \text{diag}(\mathbf{f}_t) + \text{términos adicionales}$$

Los "términos adicionales" surgen porque $\mathbf{f}_t$, $\mathbf{i}_t$ y $\tilde{\mathbf{C}}_t$ también dependen (indirectamente) de $\mathbf{C}_{t-1}$ a través de $\mathbf{h}_{t-1}$, pero el término dominante es $\text{diag}(\mathbf{f}_t)$.

Para una cadena de múltiples pasos temporales:

$$\frac{\partial \mathbf{C}_T}{\partial \mathbf{C}_k} \approx \prod_{t=k+1}^{T} \text{diag}(\mathbf{f}_t)$$

Cada factor $\text{diag}(\mathbf{f}_t)$ es una matriz diagonal con elementos en $[0, 1]$. Si la puerta de olvido aprende a mantener $\mathbf{f}_t \approx 1$ (es decir, a no olvidar), entonces:

$$\prod_{t=k+1}^{T} \text{diag}(\mathbf{f}_t) \approx \mathbf{I}$$

y el gradiente fluye sin atenuación desde el paso $T$ hasta el paso $k$, sin importar cuán grande sea la distancia $T - k$. Esto contrasta dramáticamente con la RNN básica, donde el producto de matrices $\mathbf{W}_{hh}$ y derivadas de activaciones conduce inevitablemente a la atenuación exponencial.

La clave está en que **la red aprende cuándo olvidar y cuándo recordar** a través de la puerta de olvido. No se fuerza un valor fijo de retención; en cambio, la red adapta dinámicamente el flujo de gradientes según la tarea y los datos.

---

## 4.4 Gated Recurrent Unit (GRU)

### 4.4.1 Una versión simplificada de la LSTM

La **Unidad Recurrente con Puerta** (GRU, *Gated Recurrent Unit*), propuesta por Cho et al. en 2014, es una variante simplificada de la LSTM que combina las puertas de olvido y de entrada en una sola "puerta de actualización", y fusiona el estado de celda con el estado oculto. El resultado es una arquitectura con solo dos puertas (en lugar de tres) y un único vector de estado (en lugar de dos), lo que reduce significativamente el número de parámetros y el costo computacional, manteniendo un rendimiento comparable al de la LSTM en muchas tareas.

### 4.4.2 Formulación matemática

Las ecuaciones de la GRU son las siguientes:

**Puerta de reinicio (*Reset Gate*):**

$$\mathbf{r}_t = \sigma\!\left(\mathbf{W}_r [\mathbf{h}_{t-1}, \mathbf{x}_t]\right)$$

La puerta de reinicio $\mathbf{r}_t \in \mathbb{R}^{d_h}$ determina cuánto del estado oculto anterior debe ser "olvidado" al calcular el nuevo estado candidato. Cuando $\mathbf{r}_t \approx 0$, el estado candidato se calcula como si no hubiera historia previa, lo que permite que la red "reinicie" su estado. Cuando $\mathbf{r}_t \approx 1$, toda la información del estado anterior se utiliza para calcular el candidato. La matriz $\mathbf{W}_r \in \mathbb{R}^{d_h \times (d_h + d_x)}$ es un parámetro aprendido. Nótese que, a diferencia de la formulación de la LSTM presentada anteriormente, aquí se omite el sesgo por simplicidad (en la práctica, las implementaciones suelen incluirlo).

**Puerta de actualización (*Update Gate*):**

$$\mathbf{z}_t = \sigma\!\left(\mathbf{W}_z [\mathbf{h}_{t-1}, \mathbf{x}_t]\right)$$

La puerta de actualización $\mathbf{z}_t \in \mathbb{R}^{d_h}$ controla el equilibrio entre el estado anterior y el nuevo estado candidato. Esta puerta unifica las funciones de las puertas de olvido y de entrada de la LSTM: un valor $\mathbf{z}_t \approx 0$ significa "mantener el estado anterior" (equivalente a $\mathbf{f}_t \approx 1$, $\mathbf{i}_t \approx 0$ en la LSTM), mientras que $\mathbf{z}_t \approx 1$ significa "adoptar completamente el estado candidato" (equivalente a $\mathbf{f}_t \approx 0$, $\mathbf{i}_t \approx 1$).

**Estado oculto candidato:**

$$\tilde{\mathbf{h}}_t = \tanh\!\left(\mathbf{W} [\mathbf{r}_t \odot \mathbf{h}_{t-1}, \mathbf{x}_t]\right)$$

El estado candidato $\tilde{\mathbf{h}}_t$ se calcula de forma similar a la RNN básica, pero con una diferencia crucial: el estado oculto anterior se filtra por la puerta de reinicio antes de ser utilizado. El producto $\mathbf{r}_t \odot \mathbf{h}_{t-1}$ permite que la red borre selectivamente componentes del estado anterior que no son relevantes para el cálculo del nuevo candidato. La matriz $\mathbf{W} \in \mathbb{R}^{d_h \times (d_h + d_x)}$ transforma la concatenación del estado filtrado y la entrada actual.

**Estado oculto final:**

$$\mathbf{h}_t = (1 - \mathbf{z}_t) \odot \mathbf{h}_{t-1} + \mathbf{z}_t \odot \tilde{\mathbf{h}}_t$$

Esta ecuación es la interpolación lineal entre el estado anterior y el estado candidato, controlada por la puerta de actualización. Analicemos los casos extremos:

- Si $\mathbf{z}_t = \mathbf{0}$: $\mathbf{h}_t = \mathbf{h}_{t-1}$, el estado se copia sin modificación (la red "ignora" la entrada actual).
- Si $\mathbf{z}_t = \mathbf{1}$: $\mathbf{h}_t = \tilde{\mathbf{h}}_t$, el estado se reemplaza completamente por el candidato.
- En general, la puerta de actualización permite una mezcla suave entre mantener la memoria y actualizar con nueva información.

La relación entre la puerta de actualización de la GRU y las puertas de la LSTM se hace evidente al comparar la ecuación de actualización de la GRU con la del estado de celda de la LSTM. Definiendo $\mathbf{f}_t = 1 - \mathbf{z}_t$ y $\mathbf{i}_t = \mathbf{z}_t$, la ecuación de la GRU se puede reescribir como:

$$\mathbf{h}_t = \mathbf{f}_t \odot \mathbf{h}_{t-1} + \mathbf{i}_t \odot \tilde{\mathbf{h}}_t$$

que tiene la misma estructura que la actualización del estado de celda de la LSTM, con la restricción adicional de que $\mathbf{f}_t + \mathbf{i}_t = \mathbf{1}$ (las puertas están "acopladas"). En la LSTM, $\mathbf{f}_t$ e $\mathbf{i}_t$ son independientes, lo que le confiere mayor flexibilidad.

### 4.4.3 Comparación entre GRU y LSTM

La siguiente tabla resume las diferencias principales:

| Característica | LSTM | GRU |
|---|---|---|
| Vectores de estado | 2 ($\mathbf{C}_t$ y $\mathbf{h}_t$) | 1 ($\mathbf{h}_t$) |
| Puertas | 3 (olvido, entrada, salida) | 2 (reinicio, actualización) |
| Parámetros | $4d_h(d_h + d_x + 1)$ | $3d_h(d_h + d_x)$ |
| Puertas acopladas | No ($\mathbf{f}_t$ e $\mathbf{i}_t$ independientes) | Sí ($\mathbf{z}_t$ y $1-\mathbf{z}_t$) |
| Control de exposición | Sí (puerta de salida) | No |

En la práctica, múltiples estudios empíricos han mostrado que la LSTM y la GRU alcanzan rendimientos similares en una amplia variedad de tareas, incluyendo modelado de lenguaje, traducción automática y reconocimiento de voz. La GRU suele ser preferida cuando los recursos computacionales son limitados o cuando se trabaja con conjuntos de datos pequeños, ya que su menor número de parámetros reduce el riesgo de sobreajuste (*overfitting*). La LSTM, por su parte, tiende a ser preferida en tareas que requieren un control fino sobre la memoria y la exposición de información, o cuando se dispone de grandes volúmenes de datos.

En el contexto de las comunicaciones semánticas, la elección entre LSTM y GRU depende de la tarea específica. Para la codificación semántica de texto, donde las dependencias pueden ser muy largas y el control fino de la memoria es importante, la LSTM ha sido la elección predominante. Para tareas de estimación y predicción de canal en tiempo real, donde la eficiencia computacional es crítica y las dependencias temporales son más cortas, la GRU puede ser una alternativa atractiva.

---

## 4.5 Arquitecturas bidireccionales y apiladas

### 4.5.1 RNN/LSTM bidireccionales

En una RNN unidireccional estándar, la información fluye exclusivamente de izquierda a derecha: el estado oculto $\mathbf{h}_t$ en el instante $t$ captura información únicamente de las entradas pasadas $\mathbf{x}_1, \ldots, \mathbf{x}_t$. Sin embargo, en muchas aplicaciones es deseable que la representación en el instante $t$ capture información tanto del pasado como del futuro. Esto es particularmente relevante cuando se dispone de la secuencia completa antes de procesarla, como ocurre en tareas de clasificación de secuencias, traducción automática, o decodificación de canal con latencia permitida.

La **RNN bidireccional** (*Bidirectional RNN*, BiRNN), propuesta por Schuster y Paliwal en 1997, aborda esta limitación procesando la secuencia en ambas direcciones simultáneamente. La arquitectura consta de dos capas recurrentes independientes:

1. **Capa hacia adelante** (*forward*): Procesa la secuencia de izquierda a derecha, produciendo estados ocultos $\overrightarrow{\mathbf{h}}_t$:

$$\overrightarrow{\mathbf{h}}_t = f\!\left(\overrightarrow{\mathbf{W}}_{hh}\overrightarrow{\mathbf{h}}_{t-1} + \overrightarrow{\mathbf{W}}_{xh}\mathbf{x}_t + \overrightarrow{\mathbf{b}}_h\right)$$

2. **Capa hacia atrás** (*backward*): Procesa la secuencia de derecha a izquierda, produciendo estados ocultos $\overleftarrow{\mathbf{h}}_t$:

$$\overleftarrow{\mathbf{h}}_t = f\!\left(\overleftarrow{\mathbf{W}}_{hh}\overleftarrow{\mathbf{h}}_{t+1} + \overleftarrow{\mathbf{W}}_{xh}\mathbf{x}_t + \overleftarrow{\mathbf{b}}_h\right)$$

La representación final en cada paso temporal se obtiene concatenando ambos estados ocultos:

$$\mathbf{h}_t = [\overrightarrow{\mathbf{h}}_t, \overleftarrow{\mathbf{h}}_t] \in \mathbb{R}^{2d_h}$$

El estado $\overrightarrow{\mathbf{h}}_t$ codifica el contexto pasado (desde $\mathbf{x}_1$ hasta $\mathbf{x}_t$) y $\overleftarrow{\mathbf{h}}_t$ codifica el contexto futuro (desde $\mathbf{x}_T$ hasta $\mathbf{x}_t$). La concatenación $\mathbf{h}_t$ proporciona una representación rica que captura el contexto completo de la secuencia en cada posición.

Las capas hacia adelante y hacia atrás tienen parámetros completamente independientes (denotados con las flechas en las matrices de pesos), lo que duplica el número de parámetros respecto a una RNN unidireccional.

Es importante notar que las BiRNN solo son aplicables en situaciones donde la secuencia completa está disponible antes del procesamiento, lo que excluye aplicaciones estrictamente causales o en tiempo real. En comunicaciones, esto corresponde a escenarios de procesamiento por bloques: el receptor espera a recibir una trama completa antes de decodificarla. Para la transmisión en flujo continuo (*streaming*), se requieren arquitecturas unidireccionales.

La misma idea bidireccional se aplica directamente a las LSTM y GRU, resultando en las arquitecturas **BiLSTM** y **BiGRU**, que son ampliamente utilizadas en procesamiento de lenguaje natural y que han sido adoptadas en sistemas de comunicación semántica, particularmente para la codificación y decodificación semántica de texto.

### 4.5.2 Capas recurrentes apiladas (Deep RNN)

Así como las redes *feedforward* se benefician de múltiples capas para aprender representaciones jerárquicas, las RNN pueden apilarse en profundidad para crear **RNN profundas** (*Deep RNN* o *Stacked RNN*). En esta configuración, la salida de la capa recurrente $l$ en el paso temporal $t$ se utiliza como entrada de la capa $l+1$:

$$\mathbf{h}_t^{(l)} = f\!\left(\mathbf{W}_{hh}^{(l)}\mathbf{h}_{t-1}^{(l)} + \mathbf{W}_{xh}^{(l)}\mathbf{h}_t^{(l-1)} + \mathbf{b}_h^{(l)}\right)$$

donde $\mathbf{h}_t^{(0)} \equiv \mathbf{x}_t$ es la entrada original. Cada capa tiene sus propios parámetros $\mathbf{W}_{hh}^{(l)}$, $\mathbf{W}_{xh}^{(l)}$, $\mathbf{b}_h^{(l)}$, y captura patrones a diferentes niveles de abstracción: las capas inferiores tienden a capturar patrones locales y de bajo nivel, mientras que las capas superiores capturan patrones globales y de alto nivel.

La profundidad de las RNN apiladas suele ser más modesta que la de las CNN o los Transformers: típicamente se utilizan 2 a 4 capas recurrentes. Esto se debe a que cada capa recurrente ya es "profunda" en la dimensión temporal (desplegada a lo largo de $T$ pasos), y apilar demasiadas capas puede dificultar el entrenamiento y aumentar el riesgo de sobreajuste.

Las técnicas de regularización son especialmente importantes en las RNN profundas. El **dropout** se aplica típicamente entre capas (no entre pasos temporales dentro de la misma capa), ya que el dropout temporal destruye la información almacenada en el estado oculto. Gal y Ghahramani (2016) propusieron el **dropout variacional** para RNN, donde la máscara de dropout se mantiene constante a lo largo de los pasos temporales pero varía entre secuencias.

### 4.5.3 Aplicaciones en NLP y procesamiento de señales

Las arquitecturas bidireccionales y apiladas han encontrado aplicaciones extensas tanto en procesamiento de lenguaje natural como en procesamiento de señales para telecomunicaciones:

**Procesamiento de lenguaje natural (NLP)**: Las BiLSTM apiladas fueron la arquitectura dominante para muchas tareas de NLP antes de la era de los Transformers. En particular, fueron utilizadas exitosamente en:
- Etiquetado de secuencias (POS tagging, NER)
- Análisis de sentimiento
- Traducción automática (como componente del codificador en modelos *sequence-to-sequence*)
- Comprensión lectora

**Procesamiento de señales para telecomunicaciones**: Las RNN y LSTM han sido aplicadas en:
- Estimación y predicción de canal en sistemas OFDM
- Detección de señales en canales con memoria
- Decodificación de códigos convolucionales y turbo códigos
- Compresión de voz y audio para transmisión eficiente
- Codificación semántica conjunta fuente-canal para texto y voz

En el paradigma de comunicaciones semánticas, las LSTM bidireccionales son particularmente relevantes en el codificador semántico (*semantic encoder*), donde la secuencia completa (por ejemplo, una oración) está disponible y se desea generar una representación semántica que capture el contexto completo. El decodificador semántico, por su parte, puede utilizar una LSTM unidireccional en modo autoregresivo, generando la secuencia de salida token por token.

---

## 4.6 Limitaciones de las RNN/LSTM frente a los Transformers

A pesar de los avances significativos que las LSTM y GRU representan sobre las RNN básicas, estas arquitecturas recurrentes presentan limitaciones fundamentales que motivaron el desarrollo de la arquitectura Transformer, que estudiaremos en secciones posteriores de este tutorial.

### 4.6.1 Procesamiento secuencial: imposibilidad de paralelizar

La limitación más severa de las RNN/LSTM desde el punto de vista computacional es su naturaleza **inherentemente secuencial**. El cálculo del estado oculto $\mathbf{h}_t$ requiere el estado anterior $\mathbf{h}_{t-1}$, que a su vez requiere $\mathbf{h}_{t-2}$, y así sucesivamente. Esto crea una **cadena de dependencias** que impide la paralelización del cómputo a lo largo de la dimensión temporal.

En términos de complejidad computacional, procesar una secuencia de longitud $T$ con una RNN/LSTM requiere $\mathcal{O}(T)$ operaciones secuenciales. Cada operación individual tiene complejidad $\mathcal{O}(d_h^2)$ (dominada por la multiplicación matricial $\mathbf{W}_{hh}\mathbf{h}_{t-1}$), resultando en una complejidad total de $\mathcal{O}(T \cdot d_h^2)$. El problema no es la complejidad total, sino que las $T$ operaciones deben ejecutarse en serie: no es posible calcular $\mathbf{h}_{50}$ hasta que $\mathbf{h}_{49}$ esté disponible.

Esto contrasta fuertemente con las operaciones convolucionales y de atención del Transformer, que pueden paralelizarse a lo largo de la dimensión temporal, aprovechando las capacidades de las unidades de procesamiento gráfico (GPU) modernas. En la práctica, esta diferencia se traduce en tiempos de entrenamiento significativamente mayores para las RNN/LSTM, especialmente para secuencias largas.

### 4.6.2 Ventana de contexto limitada en la práctica

Aunque las LSTM resuelven teóricamente el problema del gradiente desvaneciente, en la práctica su capacidad para capturar dependencias a largo plazo sigue siendo limitada. El estado oculto $\mathbf{h}_t \in \mathbb{R}^{d_h}$ tiene una capacidad de información fija (determinada por $d_h$), y debe comprimir toda la información relevante de la secuencia procesada hasta el instante $t$ en este vector de dimensión fija. A medida que la secuencia se alarga, la información de los pasos iniciales inevitablemente se diluye o se pierde, un fenómeno conocido como el **cuello de botella de la información** (*information bottleneck*).

Estudios empíricos han mostrado que las LSTM estándar típicamente pueden capturar dependencias efectivas de hasta unos pocos cientos de pasos temporales, con un degradamiento gradual más allá de esa distancia. Para secuencias de miles o decenas de miles de elementos (como las que aparecen en la generación de textos largos o en el procesamiento de señales de alta resolución), las LSTM resultan insuficientes.

### 4.6.3 Dificultad con secuencias muy largas

Relacionado con el punto anterior, pero desde una perspectiva diferente, el procesamiento de secuencias muy largas con RNN/LSTM presenta desafíos tanto de memoria como de estabilidad numérica. Durante el entrenamiento con BPTT, la red desplegada tiene una profundidad igual a la longitud de la secuencia $T$, lo que requiere almacenar los $T$ estados intermedios para la retropropagación. El consumo de memoria es $\mathcal{O}(T \cdot d_h)$, lo que puede ser prohibitivo para secuencias muy largas.

La técnica de **BPTT truncado** (*Truncated BPTT*) mitiga este problema al limitar la retropropagación a una ventana de $k < T$ pasos temporales, pero introduce un sesgo en la estimación del gradiente que impide el aprendizaje de dependencias más largas que $k$.

### 4.6.4 Hacia la arquitectura Transformer

Estas limitaciones —procesamiento secuencial, ventana de contexto prácticamente limitada y dificultad con secuencias largas— motivaron la búsqueda de arquitecturas alternativas que pudieran:

1. **Paralelizar** el cómputo a lo largo de la secuencia para un entrenamiento más rápido.
2. Proporcionar **acceso directo** a cualquier posición de la secuencia, sin la necesidad de propagar información a través de una cadena de estados ocultos.
3. **Escalar** eficientemente a secuencias mucho más largas.

La arquitectura Transformer, propuesta por Vaswani et al. (2017), logra estos tres objetivos mediante el mecanismo de **autoatención** (*self-attention*), que calcula las relaciones entre todas las posiciones de la secuencia en paralelo. Esta arquitectura revolucionaria será el tema de las secciones siguientes de este tutorial, pero es esencial comprender las RNN/LSTM como sus predecesoras para apreciar las motivaciones y las innovaciones que el Transformer introduce.

---

## 4.7 Ejemplo práctico: Predicción de series temporales

### 4.7.1 Descripción del problema

Para ilustrar la implementación práctica de una LSTM, consideremos el problema de **predicción de series temporales**, que tiene aplicaciones directas en telecomunicaciones: predicción de tráfico de red, predicción de estado de canal, estimación de calidad de enlace, entre otros.

En este ejemplo, implementaremos una LSTM en PyTorch para predecir los valores futuros de una señal sinusoidal con ruido, que puede interpretarse como una simplificación de la predicción de variaciones de potencia de señal recibida en un canal inalámbrico.

### 4.7.2 Implementación en PyTorch

```python
import torch
import torch.nn as nn
import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# 1. Generación de datos sintéticos
# ============================================================
# Simulamos una señal que podría representar variaciones
# temporales de un canal inalámbrico: una combinación de
# sinusoides con ruido gaussiano aditivo.

np.random.seed(42)
torch.manual_seed(42)

T_total = 1000          # Longitud total de la serie temporal
frecuencia_1 = 0.02     # Frecuencia de la componente principal
frecuencia_2 = 0.05     # Frecuencia de la componente secundaria
sigma_ruido = 0.1       # Desviación estándar del ruido

t = np.arange(T_total)
# Señal compuesta: dos sinusoides + ruido
senal = (
    np.sin(2 * np.pi * frecuencia_1 * t)
    + 0.5 * np.sin(2 * np.pi * frecuencia_2 * t)
    + sigma_ruido * np.random.randn(T_total)
)

# Normalizar la señal al rango [-1, 1] para facilitar
# el entrenamiento con activaciones tanh
senal = senal / np.max(np.abs(senal))

# ============================================================
# 2. Preparación de datos: ventanas deslizantes
# ============================================================
# Creamos pares (entrada, objetivo) usando una ventana
# deslizante: la entrada son los L pasos anteriores y
# el objetivo es el siguiente valor.

longitud_ventana = 50   # Número de pasos de entrada (L)

def crear_secuencias(datos, L):
    """
    Crea pares (X, y) a partir de una serie temporal.
    X[i] = datos[i:i+L]    (secuencia de entrada)
    y[i] = datos[i+L]      (valor a predecir)
    """
    X, y = [], []
    for i in range(len(datos) - L):
        X.append(datos[i:i+L])
        y.append(datos[i+L])
    return np.array(X), np.array(y)

X, y = crear_secuencias(senal, longitud_ventana)

# División en conjuntos de entrenamiento y prueba (80/20)
N_train = int(0.8 * len(X))
X_train, X_test = X[:N_train], X[N_train:]
y_train, y_test = y[:N_train], y[N_train:]

# Convertir a tensores de PyTorch
# LSTM espera entrada con forma (batch, seq_len, input_size)
X_train_t = torch.FloatTensor(X_train).unsqueeze(-1)  # (N, L, 1)
y_train_t = torch.FloatTensor(y_train).unsqueeze(-1)  # (N, 1)
X_test_t  = torch.FloatTensor(X_test).unsqueeze(-1)
y_test_t  = torch.FloatTensor(y_test).unsqueeze(-1)

print(f"Forma de X_train: {X_train_t.shape}")
print(f"Forma de y_train: {y_train_t.shape}")
print(f"Muestras de entrenamiento: {N_train}")
print(f"Muestras de prueba: {len(X_test)}")

# ============================================================
# 3. Definición del modelo LSTM
# ============================================================

class PredictorLSTM(nn.Module):
    """
    Red LSTM para predicción de series temporales.

    Arquitectura:
    - Capa LSTM con num_capas capas apiladas
    - Capa fully-connected para mapear el último estado
      oculto a la predicción escalar
    """
    def __init__(self, dim_entrada, dim_oculta, num_capas, dim_salida,
                 dropout=0.0):
        """
        Args:
            dim_entrada: Dimensión de cada elemento de la secuencia
                         (1 para serie univariada)
            dim_oculta:  Dimensión del estado oculto h_t
            num_capas:   Número de capas LSTM apiladas
            dim_salida:  Dimensión de la salida (1 para predicción
                         escalar)
            dropout:     Probabilidad de dropout entre capas LSTM
                         (solo aplica si num_capas > 1)
        """
        super(PredictorLSTM, self).__init__()

        self.dim_oculta = dim_oculta
        self.num_capas = num_capas

        # Capa LSTM de PyTorch:
        # - batch_first=True: la entrada tiene forma (batch, seq, feat)
        # - dropout: se aplica entre capas, no dentro de una capa
        self.lstm = nn.LSTM(
            input_size=dim_entrada,
            hidden_size=dim_oculta,
            num_layers=num_capas,
            batch_first=True,
            dropout=dropout if num_capas > 1 else 0.0
        )

        # Capa fully-connected: mapea h_T -> y_hat
        self.fc = nn.Linear(dim_oculta, dim_salida)

    def forward(self, x):
        """
        Propagación hacia adelante.

        Args:
            x: Tensor de entrada, forma (batch, seq_len, dim_entrada)

        Returns:
            prediccion: Tensor de salida, forma (batch, dim_salida)
        """
        # Inicializar estados oculto y de celda con ceros
        # Forma: (num_capas, batch, dim_oculta)
        batch_size = x.size(0)
        h_0 = torch.zeros(self.num_capas, batch_size,
                          self.dim_oculta).to(x.device)
        c_0 = torch.zeros(self.num_capas, batch_size,
                          self.dim_oculta).to(x.device)

        # Procesar la secuencia completa con la LSTM
        # salida_lstm: (batch, seq_len, dim_oculta)
        #   contiene h_t para todo t
        # (h_n, c_n): estados finales, forma (num_capas, batch, dim_oculta)
        salida_lstm, (h_n, c_n) = self.lstm(x, (h_0, c_0))

        # Usar solo el último estado oculto h_T para la predicción
        # h_n[-1] tiene forma (batch, dim_oculta)
        h_ultimo = h_n[-1]

        # Mapear a la dimensión de salida
        prediccion = self.fc(h_ultimo)

        return prediccion

# ============================================================
# 4. Configuración del entrenamiento
# ============================================================

# Hiperparámetros
dim_entrada = 1       # Serie univariada
dim_oculta = 64       # Dimensión del estado oculto
num_capas = 2         # Dos capas LSTM apiladas
dim_salida = 1        # Predecir un valor escalar
tasa_aprendizaje = 0.001
num_epocas = 100
tam_batch = 32

# Instanciar modelo, función de pérdida y optimizador
modelo = PredictorLSTM(dim_entrada, dim_oculta, num_capas, dim_salida,
                       dropout=0.2)
criterio = nn.MSELoss()              # Error cuadrático medio
optimizador = torch.optim.Adam(modelo.parameters(), lr=tasa_aprendizaje)

# Contar parámetros totales
num_params = sum(p.numel() for p in modelo.parameters() if p.requires_grad)
print(f"\nArquitectura del modelo:")
print(modelo)
print(f"\nParámetros entrenables: {num_params:,}")

# Crear DataLoaders para iterar por mini-batches
dataset_train = torch.utils.data.TensorDataset(X_train_t, y_train_t)
loader_train = torch.utils.data.DataLoader(
    dataset_train, batch_size=tam_batch, shuffle=True
)

# ============================================================
# 5. Bucle de entrenamiento
# ============================================================

historial_perdida_train = []
historial_perdida_test = []

print("\nIniciando entrenamiento...")
for epoca in range(num_epocas):
    modelo.train()
    perdida_acumulada = 0.0
    num_batches = 0

    for X_batch, y_batch in loader_train:
        # Propagación hacia adelante
        predicciones = modelo(X_batch)
        perdida = criterio(predicciones, y_batch)

        # Retropropagación y actualización de parámetros
        optimizador.zero_grad()
        perdida.backward()

        # Recorte de gradientes para estabilidad
        torch.nn.utils.clip_grad_norm_(modelo.parameters(), max_norm=1.0)

        optimizador.step()

        perdida_acumulada += perdida.item()
        num_batches += 1

    perdida_media_train = perdida_acumulada / num_batches
    historial_perdida_train.append(perdida_media_train)

    # Evaluar en el conjunto de prueba
    modelo.eval()
    with torch.no_grad():
        pred_test = modelo(X_test_t)
        perdida_test = criterio(pred_test, y_test_t).item()
        historial_perdida_test.append(perdida_test)

    # Imprimir progreso cada 10 épocas
    if (epoca + 1) % 10 == 0:
        print(f"  Época [{epoca+1:3d}/{num_epocas}]  "
              f"Pérdida train: {perdida_media_train:.6f}  "
              f"Pérdida test: {perdida_test:.6f}")

# ============================================================
# 6. Evaluación y visualización
# ============================================================

modelo.eval()
with torch.no_grad():
    predicciones_test = modelo(X_test_t).numpy().flatten()
    valores_reales = y_test_t.numpy().flatten()

# Calcular métricas de rendimiento
mse = np.mean((predicciones_test - valores_reales) ** 2)
mae = np.mean(np.abs(predicciones_test - valores_reales))
rmse = np.sqrt(mse)

print(f"\n--- Métricas de evaluación ---")
print(f"MSE  (Error Cuadrático Medio):     {mse:.6f}")
print(f"RMSE (Raíz del Error Cuad. Medio): {rmse:.6f}")
print(f"MAE  (Error Absoluto Medio):       {mae:.6f}")

# Gráfica 1: Curvas de pérdida durante el entrenamiento
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

axes[0].plot(historial_perdida_train, label='Entrenamiento', color='blue')
axes[0].plot(historial_perdida_test, label='Prueba', color='red')
axes[0].set_xlabel('Época')
axes[0].set_ylabel('MSE')
axes[0].set_title('Curva de aprendizaje')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Gráfica 2: Predicciones vs valores reales
N_mostrar = 200  # Mostrar los primeros 200 puntos del test
axes[1].plot(valores_reales[:N_mostrar], label='Real', color='blue',
             linewidth=1.5)
axes[1].plot(predicciones_test[:N_mostrar], label='Predicción LSTM',
             color='red', linewidth=1.5, linestyle='--')
axes[1].set_xlabel('Paso temporal')
axes[1].set_ylabel('Valor de la señal')
axes[1].set_title('Predicciones vs Valores Reales')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

# Gráfica 3: Error de predicción
error = predicciones_test[:N_mostrar] - valores_reales[:N_mostrar]
axes[2].plot(error, color='green', alpha=0.7)
axes[2].axhline(y=0, color='black', linestyle='-', linewidth=0.5)
axes[2].fill_between(range(len(error)), error, alpha=0.3, color='green')
axes[2].set_xlabel('Paso temporal')
axes[2].set_ylabel('Error')
axes[2].set_title(f'Error de predicción (RMSE={rmse:.4f})')
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('lstm_prediccion_serie_temporal.png', dpi=150,
            bbox_inches='tight')
plt.show()
print("\nGráfica guardada en 'lstm_prediccion_serie_temporal.png'")
```

### 4.7.3 Análisis del código

Examinemos los aspectos más relevantes de la implementación:

**Preparación de datos con ventana deslizante**: La función `crear_secuencias` transforma una serie temporal en pares de entrenamiento supervisado. Para cada posición $i$, la entrada es el vector $\mathbf{x} = [s_i, s_{i+1}, \ldots, s_{i+L-1}]$ y el objetivo es $s_{i+L}$. La longitud de ventana $L=50$ determina cuántos pasos temporales pasados utiliza el modelo para predecir el siguiente valor. Esta elección debe balancear la capacidad de capturar dependencias a largo plazo con la eficiencia computacional.

**Arquitectura del modelo**: Utilizamos dos capas LSTM apiladas con $d_h = 64$. La primera capa recibe la secuencia de entrada y produce una secuencia de estados ocultos, que sirven como entrada para la segunda capa. Esto permite que el modelo aprenda representaciones jerárquicas de los patrones temporales. El dropout de 0.2 entre capas ayuda a prevenir el sobreajuste.

**Estado inicial**: Los estados $\mathbf{h}_0$ y $\mathbf{C}_0$ se inicializan a cero, que es la convención estándar. En PyTorch, la función `nn.LSTM` acepta opcionalmente los estados iniciales; si no se proporcionan, se inicializan a cero automáticamente.

**Predicción a partir del último estado oculto**: Para la predicción de series temporales, utilizamos solo el último estado oculto $\mathbf{h}_T$ de la capa superior. Esto se debe a que $\mathbf{h}_T$ resume la información de toda la secuencia de entrada. La capa fully-connected final transforma $\mathbf{h}_T \in \mathbb{R}^{64}$ en la predicción escalar $\hat{y} \in \mathbb{R}$.

**Recorte de gradientes**: La línea `clip_grad_norm_` implementa el recorte de gradientes discutido en la Sección 4.2.5, limitando la norma $L_2$ del vector de gradientes a 1.0. Esto previene la explosión de gradientes que puede ocurrir durante el entrenamiento de RNN/LSTM, especialmente con secuencias largas.

**Optimizador Adam**: Utilizamos el optimizador Adam, que adapta la tasa de aprendizaje individualmente para cada parámetro basándose en las estimaciones de los primeros dos momentos del gradiente. Adam es particularmente efectivo para el entrenamiento de RNN/LSTM, ya que maneja bien las superficies de error con curvaturas muy diferentes en distintas direcciones, que son comunes en estas arquitecturas.

### 4.7.4 Extensiones para comunicaciones semánticas

Este ejemplo básico de predicción de series temporales puede extenderse de múltiples maneras para aplicaciones en comunicaciones semánticas:

1. **Predicción de canal**: Reemplazando la señal sintética por mediciones reales de coeficientes de canal (por ejemplo, coeficientes de desvanecimiento en un canal de Rayleigh), la misma arquitectura puede utilizarse para predecir el estado futuro del canal, permitiendo la adaptación proactiva de los esquemas de modulación y codificación (*Adaptive Modulation and Coding*, AMC).

2. **Codificador semántico para series temporales**: La LSTM puede utilizarse como el codificador de un sistema de codificación conjunta fuente-canal (JSCC) para datos de series temporales. En este caso, el último estado oculto $\mathbf{h}_T$ actúa como la representación semántica comprimida de la secuencia de entrada, que se transmite a través del canal. El decodificador en el receptor utiliza otra LSTM para reconstruir la secuencia original.

3. **Detección de anomalías en comunicaciones**: El error de predicción de la LSTM puede utilizarse como indicador de anomalías: cuando la señal real difiere significativamente de la predicción, puede indicar interferencia, ataques maliciosos o cambios abruptos en las condiciones del canal.

---

## Referencias

- Elman, J. L. (1990). Finding structure in time. *Cognitive Science*, 14(2), 179–211. DOI: [10.1207/s15516709cog1402_1](https://doi.org/10.1207/s15516709cog1402_1)

- Hochreiter, S. (1991). *Untersuchungen zu dynamischen neuronalen Netzen*. Diploma thesis, Technische Universität München.

- Bengio, Y., Simard, P., & Frasconi, P. (1994). Learning long-term dependencies with gradient descent is difficult. *IEEE Transactions on Neural Networks*, 5(2), 157–166. DOI: [10.1109/72.279181](https://doi.org/10.1109/72.279181)

- Hochreiter, S., & Schmidhuber, J. (1997). Long short-term memory. *Neural Computation*, 9(8), 1735–1780. DOI: [10.1162/neco.1997.9.8.1735](https://doi.org/10.1162/neco.1997.9.8.1735)

- Schuster, M., & Paliwal, K. K. (1997). Bidirectional recurrent neural networks. *IEEE Transactions on Signal Processing*, 45(11), 2673–2681. DOI: [10.1109/78.650093](https://doi.org/10.1109/78.650093)

- Gers, F. A., Schmidhuber, J., & Cummins, F. (2000). Learning to forget: Continual prediction with LSTM. *Neural Computation*, 12(10), 2451–2471. DOI: [10.1162/089976600300015015](https://doi.org/10.1162/089976600300015015)

- Pascanu, R., Mikolov, T., & Bengio, Y. (2013). On the difficulty of training recurrent neural networks. *Proceedings of the 30th International Conference on Machine Learning (ICML)*, 1310–1318.

- Cho, K., van Merriënboer, B., Gulcehre, C., Bahdanau, D., Bougares, F., Schwenk, H., & Bengio, Y. (2014). Learning phrase representations using RNN encoder-decoder for statistical machine translation. *Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing (EMNLP)*, 1724–1734. DOI: [10.3115/v1/D14-1179](https://doi.org/10.3115/v1/D14-1179)

- Gal, Y., & Ghahramani, Z. (2016). A theoretically grounded application of dropout in recurrent neural networks. *Advances in Neural Information Processing Systems (NeurIPS)*, 29, 1019–1027.

- Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). Attention is all you need. *Advances in Neural Information Processing Systems (NeurIPS)*, 30, 5998–6008.

---

# 5. Mecanismos de Atención

Los mecanismos de atención constituyen uno de los avances más transformadores en la historia del aprendizaje profundo. Surgidos como una solución elegante a un problema fundamental de las redes neuronales recurrentes, estos mecanismos han redefinido por completo la forma en que los modelos neuronales procesan, relacionan y comprenden la información secuencial. En el contexto de las comunicaciones semánticas, los mecanismos de atención desempeñan un papel central: permiten que el sistema identifique qué partes de un mensaje son más relevantes para la tarea comunicativa, facilitando una compresión inteligente que preserva el significado esencial mientras descarta la redundancia. Este capítulo presenta una exposición exhaustiva de los mecanismos de atención, desde su motivación original hasta las formulaciones modernas que sustentan arquitecturas como el Transformer.

---

## 5.1 Motivación: el cuello de botella de la información

### 5.1.1 El problema fundamental de los modelos seq2seq

En la Sección 4 estudiamos los modelos secuencia-a-secuencia (*sequence-to-sequence*, seq2seq) basados en redes neuronales recurrentes (RNN). Recordemos que la arquitectura canónica seq2seq, propuesta por Sutskever et al. (2014), consta de dos componentes principales:

1. **Codificador (Encoder):** Una RNN que procesa la secuencia de entrada token por token, actualizando su estado oculto en cada paso temporal. Al finalizar el procesamiento de toda la secuencia de entrada $(x_1, x_2, \ldots, x_T)$, el codificador produce un estado oculto final $\mathbf{h}_T$.

2. **Decodificador (Decoder):** Una segunda RNN que recibe el estado oculto final del codificador como su estado inicial y genera la secuencia de salida token por token.

El elemento crítico de esta arquitectura es que **toda la información** de la secuencia de entrada debe comprimirse en un único vector de longitud fija $\mathbf{h}_T \in \mathbb{R}^n$, donde $n$ es la dimensión del estado oculto. Este vector, denominado comúnmente **vector de contexto**, actúa como el único puente de comunicación entre el codificador y el decodificador.

Formalmente, si el codificador procesa una secuencia de $T$ tokens, la dinámica es:

$$\mathbf{h}_t = f(\mathbf{h}_{t-1}, \mathbf{x}_t), \quad t = 1, 2, \ldots, T$$

donde $f$ representa la función de transición de la RNN (ya sea una celda simple, LSTM o GRU). El vector de contexto es simplemente:

$$\mathbf{c} = \mathbf{h}_T$$

El decodificador entonces genera la salida condicionada únicamente en este vector:

$$\mathbf{s}_t = g(\mathbf{s}_{t-1}, y_{t-1}, \mathbf{c})$$

$$P(y_t \mid y_1, \ldots, y_{t-1}, \mathbf{x}) = \text{softmax}(\mathbf{W}_o \mathbf{s}_t)$$

### 5.1.2 El cuello de botella informacional

Este diseño presenta un **cuello de botella informacional** severo. Consideremos las implicaciones:

- **Compresión lossy obligatoria:** Un párrafo de 100 palabras, con toda su riqueza semántica, sintáctica y pragmática, debe representarse en un vector de, digamos, 256 o 512 dimensiones. Esto es análogo a intentar comprimir una imagen de alta resolución en unos pocos bytes: inevitablemente se pierde información.

- **Degradación con la longitud:** A medida que la secuencia de entrada se hace más larga, el problema se agrava. Las primeras palabras de la secuencia deben "sobrevivir" a través de múltiples pasos de actualización del estado oculto, y la información que portan se diluye progresivamente. Incluso con arquitecturas como LSTM o GRU, que mitigan parcialmente el problema del desvanecimiento del gradiente, la capacidad de retención de información a largo plazo es limitada.

- **Tratamiento uniforme:** El decodificador recibe la misma representación comprimida $\mathbf{c}$ en cada paso de generación, sin importar qué parte de la salida está generando. Intuitivamente, cuando se traduce una oración larga, las primeras palabras de la traducción deberían depender más de las primeras palabras del original, pero el modelo no tiene mecanismo para implementar esta dependencia selectiva.

Cho et al. (2014) demostraron empíricamente esta limitación: el rendimiento de los modelos seq2seq basados en RNN se degradaba significativamente a medida que la longitud de las oraciones de entrada aumentaba, especialmente para secuencias de más de 20-30 tokens.

### 5.1.3 La intuición detrás de la atención

La solución a este cuello de botella es conceptualmente simple pero profundamente elegante: **permitir que el decodificador "mire hacia atrás" a todos los estados ocultos del codificador**, no solo al último. En lugar de forzar toda la información a pasar por un único vector, el mecanismo de atención permite que el decodificador, en cada paso de generación, consulte selectivamente diferentes partes de la secuencia de entrada.

La analogía humana es inmediata. Cuando un traductor humano trabaja con un texto largo, no lee el texto completo, memoriza todo en su mente, y luego escribe la traducción sin volver a mirar el original. En su lugar, el traductor consulta repetidamente el texto fuente, enfocándose en las partes relevantes para la porción que está traduciendo en ese momento. El mecanismo de atención dota a las redes neuronales de esta misma capacidad.

Matemáticamente, en lugar de un vector de contexto fijo $\mathbf{c}$, el mecanismo de atención produce un vector de contexto **dinámico** $\mathbf{c}_i$ que cambia en cada paso temporal $i$ del decodificador:

$$\mathbf{c}_i = \sum_{j=1}^{T} \alpha_{ij} \mathbf{h}_j$$

donde $\alpha_{ij}$ son **pesos de atención** que determinan cuánta atención presta el decodificador (en el paso $i$) al estado oculto del codificador en la posición $j$. Estos pesos satisfacen:

$$\alpha_{ij} \geq 0, \quad \sum_{j=1}^{T} \alpha_{ij} = 1$$

Es decir, los pesos de atención forman una distribución de probabilidad sobre las posiciones de la secuencia de entrada, lo que permite interpretar $\alpha_{ij}$ como la probabilidad de que la posición $j$ de la entrada sea relevante para generar el token $i$ de la salida.

### 5.1.4 Relevancia para las comunicaciones semánticas

En el contexto de las comunicaciones semánticas, el cuello de botella de la información es particularmente pertinente. Un sistema de comunicación semántica debe decidir qué información transmitir a través de un canal con capacidad limitada. El mecanismo de atención proporciona un marco natural para esta tarea: los pesos de atención pueden interpretarse como una medida de la **importancia semántica** de cada elemento de la señal. Los elementos con altos pesos de atención portan información semántica crítica y deben protegerse durante la transmisión, mientras que los elementos con bajos pesos de atención pueden comprimirse más agresivamente o incluso descartarse sin pérdida significativa de significado.

---

## 5.2 Atención de Bahdanau (Atención Aditiva)

### 5.2.1 Contexto histórico

El mecanismo de atención fue introducido formalmente por Dzmitry Bahdanau, Kyunghyun Cho y Yoshua Bengio en su influyente trabajo de 2015 (Bahdanau et al., 2015). Este trabajo, titulado *"Neural Machine Translation by Jointly Learning to Align and Translate"*, propuso el mecanismo de atención en el contexto de la traducción automática neuronal y demostró mejoras significativas sobre los modelos seq2seq estándar, especialmente para oraciones largas.

La idea central es que, en lugar de codificar toda la oración de entrada en un vector de contexto fijo, el modelo aprende a **alinear** (*align*) y **traducir** conjuntamente. La alineación se refiere al proceso de determinar qué partes de la oración fuente son más relevantes para generar cada palabra de la oración objetivo.

### 5.2.2 Arquitectura del codificador bidireccional

Bahdanau et al. utilizaron un codificador **bidireccional** (BiRNN) para obtener representaciones más ricas de cada posición de la entrada. El codificador bidireccional consta de dos RNN: una que procesa la secuencia de izquierda a derecha (forward) y otra de derecha a izquierda (backward):

**RNN forward:**

$$\overrightarrow{\mathbf{h}}_j = \overrightarrow{f}(\overrightarrow{\mathbf{h}}_{j-1}, \mathbf{x}_j)$$

**RNN backward:**

$$\overleftarrow{\mathbf{h}}_j = \overleftarrow{f}(\overleftarrow{\mathbf{h}}_{j+1}, \mathbf{x}_j)$$

La representación final de cada posición $j$ se obtiene concatenando ambos estados ocultos:

$$\mathbf{h}_j = [\overrightarrow{\mathbf{h}}_j; \overleftarrow{\mathbf{h}}_j] \in \mathbb{R}^{2n}$$

Esta representación bidireccional captura tanto el contexto precedente como el contexto subsiguiente de cada token, proporcionando una representación más completa que una RNN unidireccional. El estado $\mathbf{h}_j$ resume la información de toda la oración de entrada con un enfoque especial en las palabras cercanas a la posición $j$.

### 5.2.3 El mecanismo de alineación (scoring)

El componente central de la atención de Bahdanau es la **función de alineación** (también llamada función de puntuación o *score function*), que calcula un escalar $e_{ij}$ que mide cuán relevante es el estado oculto del codificador $\mathbf{h}_j$ para el paso de decodificación $i$. Esta función se define como:

$$e_{ij} = \mathbf{v}^T \tanh(\mathbf{W}_1 \mathbf{s}_{i-1} + \mathbf{W}_2 \mathbf{h}_j)$$

Desglosemos cada componente de esta ecuación con extremo detalle:

**1. Estado del decodificador $\mathbf{s}_{i-1} \in \mathbb{R}^m$:**
Este es el estado oculto del decodificador en el paso temporal *anterior* ($i-1$). Representa lo que el decodificador "sabe" hasta el momento, incluyendo toda la información sobre los tokens de salida ya generados. Es crucial notar que se usa $\mathbf{s}_{i-1}$ y no $\mathbf{s}_i$: la atención se calcula *antes* de actualizar el estado del decodificador, porque el vector de contexto resultante se utilizará como entrada para dicha actualización.

**2. Estado del codificador $\mathbf{h}_j \in \mathbb{R}^{2n}$:**
Este es el estado oculto del codificador bidireccional en la posición $j$ de la secuencia de entrada. Como se describió anteriormente, es la concatenación de los estados ocultos forward y backward, y por lo tanto contiene información contextual tanto del pasado como del futuro de la posición $j$.

**3. Matrices de pesos $\mathbf{W}_1 \in \mathbb{R}^{d_a \times m}$ y $\mathbf{W}_2 \in \mathbb{R}^{d_a \times 2n}$:**
Estas son matrices de pesos aprendibles que proyectan los estados del decodificador y del codificador, respectivamente, a un espacio común de dimensión $d_a$ (la dimensión de la atención). La proyección a un espacio común es necesaria porque $\mathbf{s}_{i-1}$ y $\mathbf{h}_j$ pueden tener dimensiones diferentes y, más importante, provienen de espacios de representación distintos. Las matrices $\mathbf{W}_1$ y $\mathbf{W}_2$ aprenden a transformar ambas representaciones de manera que sean comparables.

El producto $\mathbf{W}_1 \mathbf{s}_{i-1} \in \mathbb{R}^{d_a}$ puede interpretarse como la "pregunta" que el decodificador formula: "¿Qué información necesito del codificador para generar el siguiente token?"

El producto $\mathbf{W}_2 \mathbf{h}_j \in \mathbb{R}^{d_a}$ puede interpretarse como la "respuesta potencial" de cada posición del codificador: "Esta es la información que yo puedo ofrecer."

**4. Función de activación $\tanh$:**
La función tangente hiperbólica se aplica elemento a elemento sobre la suma de las dos proyecciones:

$$\tanh(\mathbf{W}_1 \mathbf{s}_{i-1} + \mathbf{W}_2 \mathbf{h}_j) \in \mathbb{R}^{d_a}$$

La función $\tanh$ introduce no-linealidad, lo que permite al modelo capturar relaciones complejas entre las posiciones del codificador y el estado del decodificador. Sin esta no-linealidad, la función de alineación sería simplemente una función bilineal, limitando significativamente su expresividad. Además, $\tanh$ acota los valores al rango $[-1, 1]$, lo que contribuye a la estabilidad numérica del entrenamiento.

**5. Vector de pesos $\mathbf{v} \in \mathbb{R}^{d_a}$:**
Este es un vector de pesos aprendible que convierte el vector resultado de la $\tanh$ (de dimensión $d_a$) en un escalar. El producto punto $\mathbf{v}^T \tanh(\cdot)$ puede verse como una capa de red neuronal que produce una puntuación escalar de alineación. El vector $\mathbf{v}$ aprende a ponderar las diferentes dimensiones del espacio de alineación, determinando qué aspectos de la comparación entre codificador y decodificador son más informativos.

**¿Por qué se llama "atención aditiva"?** El nombre proviene del hecho de que los estados del decodificador y del codificador se **suman** dentro de la función $\tanh$:

$$\mathbf{W}_1 \mathbf{s}_{i-1} + \mathbf{W}_2 \mathbf{h}_j$$

Esta operación de suma es la que distingue este mecanismo de otras variantes (como la atención multiplicativa que veremos en la siguiente sección). La atención aditiva puede verse como una red neuronal feedforward de una capa oculta (con activación $\tanh$ y capa de salida lineal $\mathbf{v}^T$) que toma como entrada la concatenación de $\mathbf{s}_{i-1}$ y $\mathbf{h}_j$.

### 5.2.4 Pesos de atención

Una vez calculadas las puntuaciones de alineación $e_{ij}$ para todas las posiciones $j = 1, 2, \ldots, T$ del codificador, estas se normalizan mediante la función **softmax** para obtener los pesos de atención:

$$\alpha_{ij} = \frac{\exp(e_{ij})}{\sum_{k=1}^{T} \exp(e_{ik})}$$

La función softmax garantiza dos propiedades esenciales:

1. **No negatividad:** $\alpha_{ij} > 0$ para todo $j$. Esto asegura que los pesos representen una "contribución positiva" de cada posición.

2. **Normalización:** $\sum_{j=1}^{T} \alpha_{ij} = 1$. Esto permite interpretar los pesos como una distribución de probabilidad sobre las posiciones de la entrada.

Los pesos de atención $\alpha_{ij}$ tienen una interpretación intuitiva poderosa: $\alpha_{ij}$ representa la **probabilidad** de que la posición $j$ de la entrada sea la más relevante para generar el token $i$ de la salida. Un valor alto de $\alpha_{ij}$ indica que el modelo "presta mucha atención" a la posición $j$ al generar el $i$-ésimo token de salida.

Es importante observar que la función softmax es una operación **diferenciable**, lo que permite que los pesos de atención se aprendan mediante retropropagación estándar. No es necesario especificar *a priori* qué posiciones son relevantes; el modelo descubre estas relaciones automáticamente durante el entrenamiento.

### 5.2.5 Vector de contexto dinámico

Finalmente, el vector de contexto para el paso $i$ del decodificador se calcula como una **suma ponderada** de todos los estados ocultos del codificador, utilizando los pesos de atención como coeficientes:

$$\mathbf{c}_i = \sum_{j=1}^{T} \alpha_{ij} \mathbf{h}_j$$

Este vector de contexto $\mathbf{c}_i$ es una combinación convexa de los estados ocultos del codificador, donde los coeficientes (pesos de atención) determinan la contribución relativa de cada posición. A diferencia del vector de contexto fijo $\mathbf{c} = \mathbf{h}_T$ del modelo seq2seq estándar, $\mathbf{c}_i$ cambia en cada paso del decodificador, adaptándose dinámicamente a las necesidades de generación del token actual.

La propiedad de **diferenciabilidad** del vector de contexto es fundamental: como $\mathbf{c}_i$ es una combinación lineal de los $\mathbf{h}_j$ con coeficientes que dependen suavemente de los parámetros del modelo (a través de la softmax), los gradientes fluyen sin obstáculo desde la función de pérdida hacia todas las partes del modelo, incluyendo las matrices $\mathbf{W}_1$, $\mathbf{W}_2$ y el vector $\mathbf{v}$.

### 5.2.6 Integración con el decodificador

El vector de contexto $\mathbf{c}_i$ se integra en el decodificador RNN de la siguiente manera:

$$\mathbf{s}_i = g(\mathbf{s}_{i-1}, y_{i-1}, \mathbf{c}_i)$$

$$P(y_i \mid y_1, \ldots, y_{i-1}, \mathbf{x}) = \text{softmax}(\mathbf{W}_o [\mathbf{s}_i; \mathbf{c}_i] + \mathbf{b}_o)$$

donde $[\mathbf{s}_i; \mathbf{c}_i]$ denota la concatenación del estado del decodificador y el vector de contexto. Nótese que $\mathbf{c}_i$ se utiliza tanto para actualizar el estado del decodificador como para predecir el token de salida, maximizando el flujo de información desde el codificador.

### 5.2.7 Visualización del mecanismo

**Figura 5.1:** *Diagrama del mecanismo de atención de Bahdanau en una arquitectura seq2seq. A la izquierda se muestra el codificador bidireccional procesando la secuencia de entrada $(x_1, x_2, x_3, x_4)$, generando los estados ocultos $(\mathbf{h}_1, \mathbf{h}_2, \mathbf{h}_3, \mathbf{h}_4)$, representados como rectángulos apilados (cada uno compuesto por la concatenación de los estados forward y backward). En el centro se ilustra el módulo de atención: flechas punteadas conectan el estado del decodificador $\mathbf{s}_{i-1}$ con cada estado del codificador $\mathbf{h}_j$, confluyendo en bloques que representan el cálculo de las puntuaciones de alineación $e_{ij}$ mediante la red feedforward $\mathbf{v}^T \tanh(\mathbf{W}_1 \mathbf{s}_{i-1} + \mathbf{W}_2 \mathbf{h}_j)$. Las puntuaciones alimentan un bloque softmax que produce los pesos de atención $\alpha_{ij}$, visualizados como un mapa de calor con intensidades proporcionales a los pesos. Los pesos se combinan con los estados del codificador en un bloque de suma ponderada que genera el vector de contexto $\mathbf{c}_i$. A la derecha se muestra el decodificador, donde $\mathbf{c}_i$ se concatena con $\mathbf{s}_{i-1}$ y el embedding del token previo $y_{i-1}$ para producir el nuevo estado $\mathbf{s}_i$ y la predicción del token $y_i$. Las flechas de diferentes grosores que conectan los estados del codificador con el vector de contexto representan visualmente los diferentes magnitudes de los pesos de atención.*

### 5.2.8 Complejidad computacional

El costo computacional de la atención de Bahdanau para cada paso del decodificador es:

- **Cálculo de puntuaciones:** $O(T \cdot d_a)$, donde $T$ es la longitud de la secuencia de entrada y $d_a$ es la dimensión de la atención. Para cada una de las $T$ posiciones, se realizan dos multiplicaciones matriz-vector ($\mathbf{W}_1 \mathbf{s}_{i-1}$ y $\mathbf{W}_2 \mathbf{h}_j$), una suma, una $\tanh$ y un producto punto con $\mathbf{v}$.

- **Softmax:** $O(T)$ para la normalización.

- **Vector de contexto:** $O(T \cdot 2n)$ para la suma ponderada.

Nótese que $\mathbf{W}_1 \mathbf{s}_{i-1}$ puede calcularse una sola vez por cada paso del decodificador (ya que no depende de $j$), y los productos $\mathbf{W}_2 \mathbf{h}_j$ pueden pre-calcularse una sola vez para toda la secuencia. El número total de parámetros aprendibles en el módulo de atención es $m \cdot d_a + 2n \cdot d_a + d_a$, correspondiente a $\mathbf{W}_1$, $\mathbf{W}_2$ y $\mathbf{v}$ respectivamente.

---

## 5.3 Atención de Luong (Atención Multiplicativa)

### 5.3.1 Motivación y contexto

Poco después del trabajo de Bahdanau, Minh-Thang Luong, Hieu Pham e Ilya Manning propusieron variantes simplificadas del mecanismo de atención en su artículo *"Effective Approaches to Attention-based Neural Machine Translation"* (Luong et al., 2015). El trabajo de Luong se distingue por proponer funciones de puntuación más eficientes computacionalmente y por explorar diferentes estrategias de integración de la atención con el decodificador.

### 5.3.2 Funciones de puntuación

Luong et al. propusieron tres variantes de la función de puntuación:

**1. Atención dot-product (producto punto):**

$$e_{ij} = \mathbf{s}_i^T \mathbf{h}_j$$

Esta es la variante más simple: la puntuación de alineación es simplemente el producto punto entre el estado del decodificador $\mathbf{s}_i$ y el estado del codificador $\mathbf{h}_j$. El producto punto mide la similitud coseno (no normalizada) entre los dos vectores, por lo que posiciones cuyas representaciones son más similares al estado actual del decodificador recibirán puntuaciones más altas.

**Requisito dimensional:** Para que el producto punto sea válido, ambos vectores deben tener la misma dimensión: $\mathbf{s}_i, \mathbf{h}_j \in \mathbb{R}^n$. Esto puede requerir que el codificador y el decodificador tengan el mismo tamaño de estado oculto, o que se aplique una proyección previa.

**Ventaja:** No tiene parámetros aprendibles adicionales, lo que reduce el riesgo de sobreajuste y acelera el entrenamiento.

**2. Atención general (bilineal):**

$$e_{ij} = \mathbf{s}_i^T \mathbf{W} \mathbf{h}_j$$

Aquí se introduce una matriz de pesos $\mathbf{W} \in \mathbb{R}^{m \times n}$ que permite una interacción más rica entre los estados del decodificador y del codificador. Esta formulación puede verse como una **forma bilineal**: primero se transforma $\mathbf{h}_j$ mediante $\mathbf{W}$, y luego se calcula el producto punto con $\mathbf{s}_i$. La matriz $\mathbf{W}$ aprende qué combinaciones de dimensiones del codificador y del decodificador son más informativas para determinar la alineación.

**Ventaja sobre dot-product:** Permite que codificador y decodificador tengan dimensiones diferentes ($m \neq n$), y puede capturar relaciones más complejas entre las representaciones.

**3. Atención concatenativa (similar a Bahdanau):**

$$e_{ij} = \mathbf{v}^T \tanh(\mathbf{W}[\mathbf{s}_i; \mathbf{h}_j])$$

donde $[\mathbf{s}_i; \mathbf{h}_j]$ denota la concatenación de ambos vectores. Esta variante es funcionalmente equivalente a la atención de Bahdanau, pero con una formulación ligeramente diferente.

### 5.3.3 Diferencias clave con la atención de Bahdanau

| Aspecto | Bahdanau | Luong |
|---------|----------|-------|
| Estado del decodificador | $\mathbf{s}_{i-1}$ (paso anterior) | $\mathbf{s}_i$ (paso actual) |
| Codificador | Bidireccional | Unidireccional (generalmente) |
| Función de puntuación | Aditiva (feedforward) | Multiplicativa (producto punto/bilineal) |
| Cálculo del contexto | Antes de actualizar $\mathbf{s}_i$ | Después de calcular $\mathbf{s}_i$ |
| Complejidad | Mayor (red feedforward) | Menor (producto punto) |

Una diferencia sutil pero importante es el momento en que se utiliza el estado del decodificador. En la atención de Bahdanau, se usa $\mathbf{s}_{i-1}$ (el estado anterior), porque el vector de contexto $\mathbf{c}_i$ se necesita como entrada para calcular $\mathbf{s}_i$. En la atención de Luong, se usa $\mathbf{s}_i$ (el estado actual), calculado sin atención, y luego se combina con el vector de contexto:

$$\tilde{\mathbf{s}}_i = \tanh(\mathbf{W}_c [\mathbf{c}_i; \mathbf{s}_i])$$

$$P(y_i \mid y_1, \ldots, y_{i-1}, \mathbf{x}) = \text{softmax}(\mathbf{W}_o \tilde{\mathbf{s}}_i)$$

### 5.3.4 Eficiencia computacional

La atención multiplicativa (dot-product y general) es significativamente más eficiente que la atención aditiva. El producto punto $\mathbf{s}_i^T \mathbf{h}_j$ es una operación $O(n)$, mientras que la atención aditiva requiere dos multiplicaciones matriz-vector más la aplicación de $\tanh$, resultando en $O(d_a \cdot (m + n))$. En la práctica, para las dimensiones típicas utilizadas en redes neuronales modernas, la atención multiplicativa puede ser hasta 2-3 veces más rápida.

Además, las puntuaciones de todas las posiciones pueden calcularse en una sola operación matricial:

$$\mathbf{e}_i = \mathbf{s}_i^T \mathbf{H}$$

donde $\mathbf{H} = [\mathbf{h}_1, \mathbf{h}_2, \ldots, \mathbf{h}_T] \in \mathbb{R}^{n \times T}$ es la matriz de estados ocultos del codificador. Esto permite una implementación altamente eficiente mediante operaciones matriciales paralelas en GPUs modernas.

---

## 5.4 Self-Attention (Auto-Atención)

### 5.4.1 De la atención cruzada a la auto-atención

Los mecanismos de atención que hemos estudiado hasta ahora son ejemplos de **atención cruzada** (*cross-attention*): el decodificador atiende a los estados del codificador, es decir, la "consulta" proviene de una secuencia y las "respuestas" provienen de otra secuencia diferente. Pero, ¿qué sucede si aplicamos el mismo principio dentro de una misma secuencia?

La **auto-atención** (*self-attention*), también conocida como **atención intra-secuencia** (*intra-attention*), es un mecanismo en el que cada elemento de una secuencia atiende a todos los demás elementos de **la misma secuencia**. Esto permite que el modelo capture dependencias y relaciones entre todas las posiciones de la secuencia, independientemente de su distancia.

La auto-atención fue popularizada por Vaswani et al. (2017) en su trabajo seminal *"Attention Is All You Need"*, donde se demostró que los mecanismos de atención podían reemplazar completamente las redes recurrentes y convolucionales para el procesamiento de secuencias.

### 5.4.2 Queries, Keys y Values

La formulación moderna de la auto-atención se basa en tres conceptos fundamentales: **consultas** (*queries*, $\mathbf{Q}$), **claves** (*keys*, $\mathbf{K}$) y **valores** (*values*, $\mathbf{V}$). Estos tres componentes se derivan de la misma secuencia de entrada mediante transformaciones lineales aprendidas.

Dada una secuencia de entrada representada como una matriz $\mathbf{X} \in \mathbb{R}^{T \times d}$, donde $T$ es la longitud de la secuencia y $d$ es la dimensión de los embeddings, las matrices $\mathbf{Q}$, $\mathbf{K}$ y $\mathbf{V}$ se calculan como:

$$\mathbf{Q} = \mathbf{X}\mathbf{W}^Q \in \mathbb{R}^{T \times d_k}$$

$$\mathbf{K} = \mathbf{X}\mathbf{W}^K \in \mathbb{R}^{T \times d_k}$$

$$\mathbf{V} = \mathbf{X}\mathbf{W}^V \in \mathbb{R}^{T \times d_v}$$

donde:

- $\mathbf{W}^Q \in \mathbb{R}^{d \times d_k}$ es la matriz de proyección de consultas.
- $\mathbf{W}^K \in \mathbb{R}^{d \times d_k}$ es la matriz de proyección de claves.
- $\mathbf{W}^V \in \mathbb{R}^{d \times d_v}$ es la matriz de proyección de valores.
- $d_k$ es la dimensión de las consultas y claves (deben coincidir para el producto punto).
- $d_v$ es la dimensión de los valores (puede diferir de $d_k$).

Cada fila de $\mathbf{Q}$, $\mathbf{K}$ y $\mathbf{V}$ corresponde a un token de la secuencia. El token en la posición $t$ tiene:

- **Consulta** $\mathbf{q}_t = \mathbf{x}_t \mathbf{W}^Q$: Representa "lo que este token está buscando" — la información que necesita de otros tokens.
- **Clave** $\mathbf{k}_t = \mathbf{x}_t \mathbf{W}^K$: Representa "lo que este token ofrece" — un índice de la información que contiene.
- **Valor** $\mathbf{v}_t = \mathbf{x}_t \mathbf{W}^V$: Representa "el contenido real" — la información que se transmitirá si este token es seleccionado.

### 5.4.3 La analogía de la biblioteca

Para desarrollar una intuición más profunda sobre el mecanismo query-key-value, consideremos la **analogía de la biblioteca**:

Imaginemos que estamos en una biblioteca y necesitamos encontrar información para responder una pregunta de investigación.

- **Query (Consulta) = La pregunta del investigador:** Es lo que buscamos. Cada token formula su propia pregunta: "¿Qué información del contexto me es útil?"

- **Key (Clave) = El catálogo o índice de los libros:** Cada libro (token) tiene una entrada en el catálogo que describe brevemente su contenido. No es el contenido completo del libro, sino una descripción resumida que permite determinar si el libro es relevante para nuestra pregunta.

- **Value (Valor) = El contenido real de los libros:** Una vez que determinamos que un libro es relevante (comparando nuestra consulta con la entrada del catálogo), extraemos el contenido real del libro.

El proceso de atención es entonces análogo a:

1. **Formular la consulta** (calcular $\mathbf{Q}$): El investigador articula qué información necesita.
2. **Comparar con el catálogo** (calcular $\mathbf{Q}\mathbf{K}^T$): Se compara la consulta con cada entrada del catálogo para determinar la relevancia de cada libro.
3. **Asignar relevancias** (aplicar softmax): Se normalizan las puntuaciones de relevancia para obtener una distribución de probabilidad.
4. **Extraer información** (multiplicar por $\mathbf{V}$): Se extrae y combina el contenido de los libros relevantes, ponderado por su relevancia.

La separación entre claves y valores es conceptualmente importante: las claves determinan **si** un token es relevante, y los valores determinan **qué información** se extrae de ese token. Esta separación permite que el mecanismo sea más flexible: un token podría contener cierta información (valor) pero ser recuperable mediante diferentes tipos de consultas (clave).

### 5.4.4 Scaled Dot-Product Attention

La formulación completa de la atención de producto punto escalado (*Scaled Dot-Product Attention*) es:

$$\text{Attention}(\mathbf{Q}, \mathbf{K}, \mathbf{V}) = \text{softmax}\left(\frac{\mathbf{Q}\mathbf{K}^T}{\sqrt{d_k}}\right)\mathbf{V}$$

Analicemos cada paso de esta ecuación con detalle minucioso:

**Paso 1: Calcular las puntuaciones brutas $\mathbf{Q}\mathbf{K}^T$**

El producto matricial $\mathbf{Q}\mathbf{K}^T \in \mathbb{R}^{T \times T}$ produce una **matriz de puntuaciones** donde el elemento $(i, j)$ es:

$$(\mathbf{Q}\mathbf{K}^T)_{ij} = \mathbf{q}_i^T \mathbf{k}_j = \sum_{l=1}^{d_k} q_{il} \cdot k_{jl}$$

Esta puntuación mide la **compatibilidad** o **afinidad** entre la consulta del token $i$ y la clave del token $j$. Un valor alto indica que el token $j$ contiene información relevante para lo que el token $i$ está buscando. La matriz resultante tiene dimensión $T \times T$, representando todas las relaciones par a par entre los $T$ tokens de la secuencia.

**Paso 2: Escalar por $\sqrt{d_k}$**

$$\frac{\mathbf{Q}\mathbf{K}^T}{\sqrt{d_k}}$$

El factor de escalamiento $\frac{1}{\sqrt{d_k}}$ es crucial para la estabilidad numérica del entrenamiento. La justificación es la siguiente:

Supongamos que los componentes de $\mathbf{q}_i$ y $\mathbf{k}_j$ son variables aleatorias independientes con media 0 y varianza 1. Entonces, el producto punto $\mathbf{q}_i^T \mathbf{k}_j = \sum_{l=1}^{d_k} q_{il} k_{jl}$ tiene:

$$\mathbb{E}[\mathbf{q}_i^T \mathbf{k}_j] = \sum_{l=1}^{d_k} \mathbb{E}[q_{il}] \cdot \mathbb{E}[k_{jl}] = 0$$

$$\text{Var}[\mathbf{q}_i^T \mathbf{k}_j] = \sum_{l=1}^{d_k} \text{Var}[q_{il} k_{jl}] = d_k$$

Es decir, la varianza del producto punto crece linealmente con $d_k$. Para valores grandes de $d_k$ (por ejemplo, $d_k = 64$ o $d_k = 128$), los productos punto pueden tener magnitudes muy grandes. Cuando valores de gran magnitud entran en la función softmax, esta produce distribuciones extremadamente concentradas (cercanas a *one-hot*), lo que resulta en gradientes extremadamente pequeños (casi cero), dificultando severamente el aprendizaje.

Al dividir por $\sqrt{d_k}$, el producto punto escalado $\frac{\mathbf{q}_i^T \mathbf{k}_j}{\sqrt{d_k}}$ tiene varianza 1, independientemente de $d_k$, lo que mantiene la softmax en una región de operación con gradientes informativos.

**Paso 3: Aplicar softmax**

$$\alpha_{ij} = \text{softmax}\left(\frac{\mathbf{q}_i^T \mathbf{k}_j}{\sqrt{d_k}}\right)_j = \frac{\exp\left(\frac{\mathbf{q}_i^T \mathbf{k}_j}{\sqrt{d_k}}\right)}{\sum_{l=1}^{T} \exp\left(\frac{\mathbf{q}_i^T \mathbf{k}_l}{\sqrt{d_k}}\right)}$$

La softmax se aplica **por filas** de la matriz $\frac{\mathbf{Q}\mathbf{K}^T}{\sqrt{d_k}}$. Cada fila $i$ se convierte en una distribución de probabilidad sobre las $T$ posiciones, determinando cómo el token $i$ distribuye su atención sobre todos los tokens. Después de la softmax, la suma de cada fila es 1:

$$\sum_{j=1}^{T} \alpha_{ij} = 1, \quad \forall i$$

La matriz $\boldsymbol{\alpha} \in \mathbb{R}^{T \times T}$ resultante se denomina **matriz de pesos de atención** y es una de las herramientas más valiosas para la interpretabilidad de los modelos basados en atención.

**Paso 4: Calcular la salida ponderada**

$$\text{Attention}(\mathbf{Q}, \mathbf{K}, \mathbf{V}) = \boldsymbol{\alpha} \mathbf{V} \in \mathbb{R}^{T \times d_v}$$

La multiplicación de la matriz de pesos de atención $\boldsymbol{\alpha}$ por la matriz de valores $\mathbf{V}$ produce la **salida de la atención**. Cada fila $i$ del resultado es:

$$\text{output}_i = \sum_{j=1}^{T} \alpha_{ij} \mathbf{v}_j$$

Es decir, la salida para cada token es una **suma ponderada de los valores de todos los tokens**, donde los pesos están determinados por las afinidades query-key. Los tokens más relevantes (con $\alpha_{ij}$ alto) contribuyen más a la representación actualizada del token $i$.

### 5.4.5 Propiedades fundamentales de la auto-atención

**1. Conexiones directas entre cualquier par de tokens:** A diferencia de las RNN, donde la información entre posiciones distantes debe propagarse a través de múltiples pasos temporales (dando lugar al problema del desvanecimiento del gradiente), la auto-atención establece **conexiones directas** entre todas las posiciones. La distancia máxima del camino de señal entre cualquier par de posiciones es $O(1)$, comparado con $O(T)$ en una RNN y $O(\log T)$ en una red convolucional dilatada.

**2. Paralelización completa:** Todas las puntuaciones de atención pueden calcularse simultáneamente, ya que no existen dependencias secuenciales (a diferencia de las RNN). Esto permite una utilización eficiente del hardware paralelo moderno (GPUs, TPUs).

**3. Complejidad computacional:** La complejidad temporal de la auto-atención es $O(T^2 \cdot d_k)$ para el cálculo de $\mathbf{Q}\mathbf{K}^T$, y $O(T^2 \cdot d_v)$ para la multiplicación por $\mathbf{V}$. La complejidad cuadrática en $T$ es la principal limitación de la auto-atención para secuencias muy largas, lo que ha motivado investigación significativa en variantes de atención eficiente (como Linformer, Performer, etc.).

**Figura 5.2:** *Diagrama esquemático del mecanismo de Scaled Dot-Product Attention. En la parte superior se muestran tres flujos de entrada paralelos: la matriz de entrada $\mathbf{X}$ (representada como una secuencia de vectores de embedding apilados verticalmente) se multiplica por tres matrices de proyección $\mathbf{W}^Q$, $\mathbf{W}^K$ y $\mathbf{W}^V$ (mostradas como rectángulos con flechas salientes) para producir las matrices $\mathbf{Q}$, $\mathbf{K}$ y $\mathbf{V}$ respectivamente. En la parte central se ilustra el cálculo del producto punto: $\mathbf{Q}$ y $\mathbf{K}^T$ (transpuesta de $\mathbf{K}$) se combinan mediante multiplicación matricial, generando la matriz de puntuaciones $\mathbf{Q}\mathbf{K}^T$ de dimensión $T \times T$, visualizada como un mapa de calor cuadrado. A continuación, un bloque de escala divide cada elemento por $\sqrt{d_k}$, seguido de un bloque softmax aplicado por filas que produce la matriz de pesos de atención $\boldsymbol{\alpha}$ (otro mapa de calor, ahora con filas que suman a 1). Finalmente, $\boldsymbol{\alpha}$ se multiplica por $\mathbf{V}$ para obtener la salida de dimensión $T \times d_v$. Debajo del diagrama se muestra un ejemplo de mapa de calor de atención para una oración corta, donde la intensidad del color indica la fuerza de la atención entre cada par de palabras.*

---

## 5.5 Ejemplo detallado paso a paso

Para consolidar la comprensión del mecanismo de auto-atención, trabajaremos un ejemplo numérico completo con la oración en español: **"El gato se sentó"**.

### 5.5.1 Configuración del ejemplo

Consideremos una secuencia de 4 tokens: $x_1 = \text{"El"}$, $x_2 = \text{"gato"}$, $x_3 = \text{"se"}$, $x_4 = \text{"sentó"}$.

Para simplificar los cálculos, utilizaremos embeddings de dimensión $d = 4$ y dimensiones de atención $d_k = d_v = 3$.

**Embeddings de entrada** (valores ilustrativos asignados para facilitar el cálculo):

$$\mathbf{x}_1 = \begin{bmatrix} 1.0 \\ 0.0 \\ 1.0 \\ 0.0 \end{bmatrix}, \quad \mathbf{x}_2 = \begin{bmatrix} 0.0 \\ 1.0 \\ 0.0 \\ 1.0 \end{bmatrix}, \quad \mathbf{x}_3 = \begin{bmatrix} 1.0 \\ 1.0 \\ 0.0 \\ 0.0 \end{bmatrix}, \quad \mathbf{x}_4 = \begin{bmatrix} 0.0 \\ 0.0 \\ 1.0 \\ 1.0 \end{bmatrix}$$

La matriz de entrada es:

$$\mathbf{X} = \begin{bmatrix} 1.0 & 0.0 & 1.0 & 0.0 \\ 0.0 & 1.0 & 0.0 & 1.0 \\ 1.0 & 1.0 & 0.0 & 0.0 \\ 0.0 & 0.0 & 1.0 & 1.0 \end{bmatrix} \in \mathbb{R}^{4 \times 4}$$

### 5.5.2 Definición de las matrices de proyección

Definimos matrices de pesos $\mathbf{W}^Q, \mathbf{W}^K \in \mathbb{R}^{4 \times 3}$ y $\mathbf{W}^V \in \mathbb{R}^{4 \times 3}$:

$$\mathbf{W}^Q = \begin{bmatrix} 1 & 0 & 1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \\ 1 & 1 & 0 \end{bmatrix}, \quad \mathbf{W}^K = \begin{bmatrix} 0 & 1 & 1 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \\ 1 & 0 & 1 \end{bmatrix}, \quad \mathbf{W}^V = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \\ 1 & 1 & 0 \end{bmatrix}$$

### 5.5.3 Cálculo de Q, K, V

**Cálculo de $\mathbf{Q} = \mathbf{X}\mathbf{W}^Q$:**

Para la primera fila (token "El", $\mathbf{x}_1 = [1, 0, 1, 0]$):

$$\mathbf{q}_1 = [1 \cdot 1 + 0 \cdot 0 + 1 \cdot 0 + 0 \cdot 1, \; 1 \cdot 0 + 0 \cdot 1 + 1 \cdot 0 + 0 \cdot 1, \; 1 \cdot 1 + 0 \cdot 0 + 1 \cdot 1 + 0 \cdot 0] = [1, 0, 2]$$

Para "gato" ($\mathbf{x}_2 = [0, 1, 0, 1]$):

$$\mathbf{q}_2 = [0 + 0 + 0 + 1, \; 0 + 1 + 0 + 1, \; 0 + 0 + 0 + 0] = [1, 2, 0]$$

Para "se" ($\mathbf{x}_3 = [1, 1, 0, 0]$):

$$\mathbf{q}_3 = [1 + 0 + 0 + 0, \; 0 + 1 + 0 + 0, \; 1 + 0 + 0 + 0] = [1, 1, 1]$$

Para "sentó" ($\mathbf{x}_4 = [0, 0, 1, 1]$):

$$\mathbf{q}_4 = [0 + 0 + 0 + 1, \; 0 + 0 + 0 + 1, \; 0 + 0 + 1 + 0] = [1, 1, 1]$$

$$\mathbf{Q} = \begin{bmatrix} 1 & 0 & 2 \\ 1 & 2 & 0 \\ 1 & 1 & 1 \\ 1 & 1 & 1 \end{bmatrix}$$

**Cálculo de $\mathbf{K} = \mathbf{X}\mathbf{W}^K$:**

Para "El" ($\mathbf{x}_1 = [1, 0, 1, 0]$):

$$\mathbf{k}_1 = [0 + 0 + 0 + 0, \; 1 + 0 + 0 + 0, \; 1 + 0 + 1 + 0] = [0, 1, 2]$$

Para "gato" ($\mathbf{x}_2 = [0, 1, 0, 1]$):

$$\mathbf{k}_2 = [0 + 1 + 0 + 1, \; 0 + 0 + 0 + 0, \; 0 + 0 + 0 + 1] = [2, 0, 1]$$

Para "se" ($\mathbf{x}_3 = [1, 1, 0, 0]$):

$$\mathbf{k}_3 = [0 + 1 + 0 + 0, \; 1 + 0 + 0 + 0, \; 1 + 0 + 0 + 0] = [1, 1, 1]$$

Para "sentó" ($\mathbf{x}_4 = [0, 0, 1, 1]$):

$$\mathbf{k}_4 = [0 + 0 + 0 + 1, \; 0 + 0 + 0 + 0, \; 0 + 0 + 1 + 1] = [1, 0, 2]$$

$$\mathbf{K} = \begin{bmatrix} 0 & 1 & 2 \\ 2 & 0 & 1 \\ 1 & 1 & 1 \\ 1 & 0 & 2 \end{bmatrix}$$

**Cálculo de $\mathbf{V} = \mathbf{X}\mathbf{W}^V$:**

Para "El" ($\mathbf{x}_1 = [1, 0, 1, 0]$):

$$\mathbf{v}_1 = [1 + 0 + 0 + 0, \; 0 + 0 + 0 + 0, \; 0 + 0 + 1 + 0] = [1, 0, 1]$$

Para "gato" ($\mathbf{x}_2 = [0, 1, 0, 1]$):

$$\mathbf{v}_2 = [0 + 0 + 0 + 1, \; 0 + 1 + 0 + 1, \; 0 + 0 + 0 + 0] = [1, 2, 0]$$

Para "se" ($\mathbf{x}_3 = [1, 1, 0, 0]$):

$$\mathbf{v}_3 = [1 + 0 + 0 + 0, \; 0 + 1 + 0 + 0, \; 0 + 0 + 0 + 0] = [1, 1, 0]$$

Para "sentó" ($\mathbf{x}_4 = [0, 0, 1, 1]$):

$$\mathbf{v}_4 = [0 + 0 + 0 + 1, \; 0 + 0 + 0 + 1, \; 0 + 0 + 1 + 0] = [1, 1, 1]$$

$$\mathbf{V} = \begin{bmatrix} 1 & 0 & 1 \\ 1 & 2 & 0 \\ 1 & 1 & 0 \\ 1 & 1 & 1 \end{bmatrix}$$

### 5.5.4 Cálculo de $\mathbf{Q}\mathbf{K}^T$

Ahora calculamos la matriz de puntuaciones brutas. Recordemos que $\mathbf{K}^T \in \mathbb{R}^{3 \times 4}$:

$$\mathbf{K}^T = \begin{bmatrix} 0 & 2 & 1 & 1 \\ 1 & 0 & 1 & 0 \\ 2 & 1 & 1 & 2 \end{bmatrix}$$

Calculemos $\mathbf{Q}\mathbf{K}^T$ elemento por elemento:

**Fila 1 (token "El", $\mathbf{q}_1 = [1, 0, 2]$):**

- $\mathbf{q}_1 \cdot \mathbf{k}_1 = 1 \cdot 0 + 0 \cdot 1 + 2 \cdot 2 = 4$
- $\mathbf{q}_1 \cdot \mathbf{k}_2 = 1 \cdot 2 + 0 \cdot 0 + 2 \cdot 1 = 4$
- $\mathbf{q}_1 \cdot \mathbf{k}_3 = 1 \cdot 1 + 0 \cdot 1 + 2 \cdot 1 = 3$
- $\mathbf{q}_1 \cdot \mathbf{k}_4 = 1 \cdot 1 + 0 \cdot 0 + 2 \cdot 2 = 5$

**Fila 2 (token "gato", $\mathbf{q}_2 = [1, 2, 0]$):**

- $\mathbf{q}_2 \cdot \mathbf{k}_1 = 1 \cdot 0 + 2 \cdot 1 + 0 \cdot 2 = 2$
- $\mathbf{q}_2 \cdot \mathbf{k}_2 = 1 \cdot 2 + 2 \cdot 0 + 0 \cdot 1 = 2$
- $\mathbf{q}_2 \cdot \mathbf{k}_3 = 1 \cdot 1 + 2 \cdot 1 + 0 \cdot 1 = 3$
- $\mathbf{q}_2 \cdot \mathbf{k}_4 = 1 \cdot 1 + 2 \cdot 0 + 0 \cdot 2 = 1$

**Fila 3 (token "se", $\mathbf{q}_3 = [1, 1, 1]$):**

- $\mathbf{q}_3 \cdot \mathbf{k}_1 = 1 \cdot 0 + 1 \cdot 1 + 1 \cdot 2 = 3$
- $\mathbf{q}_3 \cdot \mathbf{k}_2 = 1 \cdot 2 + 1 \cdot 0 + 1 \cdot 1 = 3$
- $\mathbf{q}_3 \cdot \mathbf{k}_3 = 1 \cdot 1 + 1 \cdot 1 + 1 \cdot 1 = 3$
- $\mathbf{q}_3 \cdot \mathbf{k}_4 = 1 \cdot 1 + 1 \cdot 0 + 1 \cdot 2 = 3$

**Fila 4 (token "sentó", $\mathbf{q}_4 = [1, 1, 1]$):**

Los cálculos son idénticos a la fila 3 ya que $\mathbf{q}_4 = \mathbf{q}_3$:

- $[3, 3, 3, 3]$

Resultado completo:

$$\mathbf{Q}\mathbf{K}^T = \begin{bmatrix} 4 & 4 & 3 & 5 \\ 2 & 2 & 3 & 1 \\ 3 & 3 & 3 & 3 \\ 3 & 3 & 3 & 3 \end{bmatrix}$$

### 5.5.5 Escalamiento por $\sqrt{d_k}$

Con $d_k = 3$, tenemos $\sqrt{d_k} = \sqrt{3} \approx 1.732$:

$$\frac{\mathbf{Q}\mathbf{K}^T}{\sqrt{d_k}} = \begin{bmatrix} 2.309 & 2.309 & 1.732 & 2.887 \\ 1.155 & 1.155 & 1.732 & 0.577 \\ 1.732 & 1.732 & 1.732 & 1.732 \\ 1.732 & 1.732 & 1.732 & 1.732 \end{bmatrix}$$

### 5.5.6 Aplicación de softmax

Aplicamos softmax por filas. Para la fila 1:

$$\exp(2.309) \approx 10.06, \quad \exp(2.309) \approx 10.06, \quad \exp(1.732) \approx 5.65, \quad \exp(2.887) \approx 17.94$$

Suma: $10.06 + 10.06 + 5.65 + 17.94 = 43.71$

$$\alpha_{1,:} = \left[\frac{10.06}{43.71}, \frac{10.06}{43.71}, \frac{5.65}{43.71}, \frac{17.94}{43.71}\right] = [0.230, 0.230, 0.129, 0.410]$$

Para la fila 2:

$$\exp(1.155) \approx 3.17, \quad \exp(1.155) \approx 3.17, \quad \exp(1.732) \approx 5.65, \quad \exp(0.577) \approx 1.78$$

Suma: $3.17 + 3.17 + 5.65 + 1.78 = 13.77$

$$\alpha_{2,:} = [0.230, 0.230, 0.410, 0.129]$$

Para las filas 3 y 4, todos los valores escalados son iguales ($1.732$), por lo que la softmax produce una distribución uniforme:

$$\alpha_{3,:} = \alpha_{4,:} = [0.25, 0.25, 0.25, 0.25]$$

Matriz de pesos de atención completa:

$$\boldsymbol{\alpha} = \begin{bmatrix} 0.230 & 0.230 & 0.129 & 0.410 \\ 0.230 & 0.230 & 0.410 & 0.129 \\ 0.250 & 0.250 & 0.250 & 0.250 \\ 0.250 & 0.250 & 0.250 & 0.250 \end{bmatrix}$$

### 5.5.7 Cálculo de la salida $\boldsymbol{\alpha}\mathbf{V}$

Finalmente, multiplicamos la matriz de atención por la matriz de valores:

**Fila 1 (representación actualizada de "El"):**

$$\text{out}_1 = 0.230 \cdot [1, 0, 1] + 0.230 \cdot [1, 2, 0] + 0.129 \cdot [1, 1, 0] + 0.410 \cdot [1, 1, 1]$$

$$= [0.230, 0, 0.230] + [0.230, 0.460, 0] + [0.129, 0.129, 0] + [0.410, 0.410, 0.410]$$

$$= [0.999, 0.999, 0.640]$$

$$\approx [1.00, 1.00, 0.64]$$

**Fila 2 (representación actualizada de "gato"):**

$$\text{out}_2 = 0.230 \cdot [1, 0, 1] + 0.230 \cdot [1, 2, 0] + 0.410 \cdot [1, 1, 0] + 0.129 \cdot [1, 1, 1]$$

$$= [0.230, 0, 0.230] + [0.230, 0.460, 0] + [0.410, 0.410, 0] + [0.129, 0.129, 0.129]$$

$$= [0.999, 0.999, 0.359]$$

$$\approx [1.00, 1.00, 0.36]$$

**Fila 3 (representación actualizada de "se"):**

$$\text{out}_3 = 0.25 \cdot [1, 0, 1] + 0.25 \cdot [1, 2, 0] + 0.25 \cdot [1, 1, 0] + 0.25 \cdot [1, 1, 1]$$

$$= [0.25, 0, 0.25] + [0.25, 0.50, 0] + [0.25, 0.25, 0] + [0.25, 0.25, 0.25]$$

$$= [1.00, 1.00, 0.50]$$

**Fila 4 (representación actualizada de "sentó"):**

$$\text{out}_4 = [1.00, 1.00, 0.50]$$

(Idéntico a la fila 3, ya que los pesos de atención son iguales.)

Resultado final:

$$\text{Attention}(\mathbf{Q}, \mathbf{K}, \mathbf{V}) = \begin{bmatrix} 1.00 & 1.00 & 0.64 \\ 1.00 & 1.00 & 0.36 \\ 1.00 & 1.00 & 0.50 \\ 1.00 & 1.00 & 0.50 \end{bmatrix}$$

### 5.5.8 Interpretación de los resultados

Analicemos los pesos de atención para extraer información semántica:

**Token "El" (fila 1: $[0.230, 0.230, 0.129, 0.410]$):**
El artículo "El" presta la mayor atención al verbo "sentó" ($\alpha = 0.410$) y una atención considerable al sustantivo "gato" ($\alpha = 0.230$). Esto tiene sentido lingüístico: el artículo definido se relaciona directamente con el sustantivo que determina y, a través de la concordancia, con el verbo principal de la oración.

**Token "gato" (fila 2: $[0.230, 0.230, 0.410, 0.129]$):**
El sustantivo "gato" presta la mayor atención al pronombre reflexivo "se" ($\alpha = 0.410$). Esto refleja la relación sintáctica entre el sujeto y el pronombre reflexivo en la construcción "se sentó": el pronombre "se" está directamente vinculado al sujeto "gato" que realiza la acción.

**Tokens "se" y "sentó" (filas 3-4: $[0.25, 0.25, 0.25, 0.25]$):**
La atención uniforme indica que, con estos embeddings y pesos particulares, estos tokens no distinguen entre las diferentes posiciones. En un modelo entrenado con datos reales, estas distribuciones serían considerablemente más informativas.

Este ejemplo, aunque simplificado, ilustra cómo la auto-atención permite a cada token construir una representación contextualizada que incorpora información de toda la secuencia, con énfasis diferenciado según las relaciones aprendidas.

---

## 5.6 Multi-Head Attention (Atención Multi-Cabeza)

### 5.6.1 Limitaciones de una sola cabeza de atención

La auto-atención con una única cabeza (*single-head attention*) tiene una limitación fundamental: para cada par de tokens, produce una **única puntuación de atención** $\alpha_{ij}$. Sin embargo, las relaciones entre tokens son multifacéticas. Consideremos la palabra "banco" en la oración "El banco del parque está cerca del banco de inversiones". La palabra "banco" en cada aparición necesita atender a diferentes palabras según el tipo de relación:

- **Relación semántica:** "banco" (asiento) debería atender a "parque"; "banco" (institución) debería atender a "inversiones".
- **Relación sintáctica:** Ambos "banco" deberían atender al artículo "El" y a la preposición "del".
- **Relación posicional:** Cada "banco" podría atender a palabras cercanas para captar contexto local.

Una única cabeza de atención debe comprimir todas estas relaciones diversas en un único conjunto de pesos, lo que limita la riqueza representacional del modelo.

### 5.6.2 Formulación matemática

La **atención multi-cabeza** (*Multi-Head Attention*, MHA) aborda esta limitación ejecutando múltiples operaciones de atención en paralelo, cada una con sus propias matrices de proyección. Formalmente, dadas $h$ cabezas de atención:

$$\text{head}_i = \text{Attention}(\mathbf{Q}\mathbf{W}_i^Q, \mathbf{K}\mathbf{W}_i^K, \mathbf{V}\mathbf{W}_i^V), \quad i = 1, 2, \ldots, h$$

donde las matrices de proyección para la cabeza $i$ son:

- $\mathbf{W}_i^Q \in \mathbb{R}^{d_{\text{model}} \times d_k}$
- $\mathbf{W}_i^K \in \mathbb{R}^{d_{\text{model}} \times d_k}$
- $\mathbf{W}_i^V \in \mathbb{R}^{d_{\text{model}} \times d_v}$

Cada cabeza $i$ proyecta las consultas, claves y valores a un subespacio de menor dimensión y calcula la atención de forma independiente. Los resultados de todas las cabezas se concatenan y se proyectan de vuelta al espacio original:

$$\text{MultiHead}(\mathbf{Q}, \mathbf{K}, \mathbf{V}) = \text{Concat}(\text{head}_1, \text{head}_2, \ldots, \text{head}_h) \mathbf{W}^O$$

donde $\mathbf{W}^O \in \mathbb{R}^{h \cdot d_v \times d_{\text{model}}}$ es la matriz de proyección de salida.

### 5.6.3 Desglose dimensional

Para mantener la complejidad computacional comparable a la de una atención de cabeza única, las dimensiones de cada cabeza se reducen proporcionalmente al número de cabezas:

$$d_k = d_v = \frac{d_{\text{model}}}{h}$$

Con esta elección, las dimensiones de las diferentes matrices y tensores son:

| Componente | Dimensión |
|-----------|-----------|
| Entrada $\mathbf{X}$ | $T \times d_{\text{model}}$ |
| Proyección por cabeza $\mathbf{W}_i^Q$ | $d_{\text{model}} \times d_k$ |
| $\mathbf{Q}_i = \mathbf{X}\mathbf{W}_i^Q$ | $T \times d_k$ |
| $\mathbf{Q}_i \mathbf{K}_i^T$ | $T \times T$ |
| Salida por cabeza $\text{head}_i$ | $T \times d_v$ |
| Concatenación | $T \times (h \cdot d_v) = T \times d_{\text{model}}$ |
| Proyección de salida $\mathbf{W}^O$ | $d_{\text{model}} \times d_{\text{model}}$ |
| Salida final | $T \times d_{\text{model}}$ |

La dimensión de salida $T \times d_{\text{model}}$ es la misma que la de entrada, lo que permite apilar múltiples capas de atención multi-cabeza de forma composicional.

### 5.6.4 Intuición: ¿por qué múltiples cabezas?

Cada cabeza de atención aprende a especializarse en un **tipo diferente de relación** entre tokens. Investigaciones empíricas han revelado patrones de especialización notables:

1. **Cabezas sintácticas:** Algunas cabezas aprenden relaciones gramaticales, como la relación sujeto-verbo, determinante-sustantivo, o modificador-núcleo.

2. **Cabezas posicionales:** Algunas cabezas aprenden patrones de atención basados en la distancia relativa, atendiendo preferentemente a tokens adyacentes (capturando n-gramas) o a posiciones fijas.

3. **Cabezas semánticas:** Otras cabezas capturan relaciones semánticas, como correferencialidad (pronombres que refieren al mismo antecedente), sinonimia contextual o relaciones temáticas.

4. **Cabezas de copia:** En modelos de lenguaje, algunas cabezas aprenden a "copiar" tokens anteriores a posiciones posteriores, lo que es esencial para tareas como la repetición y la referencia.

La combinación de múltiples perspectivas a través de la concatenación y la proyección de salida $\mathbf{W}^O$ permite al modelo integrar información de diversas naturalezas en una representación unificada.

Formalmente, la proyección de salida $\mathbf{W}^O$ aprende a **fusionar** las diferentes perspectivas:

$$\text{output} = [\text{head}_1; \text{head}_2; \ldots; \text{head}_h] \mathbf{W}^O$$

donde cada $\text{head}_i \in \mathbb{R}^{T \times d_v}$ captura un aspecto diferente de las relaciones inter-token, y $\mathbf{W}^O$ aprende la combinación óptima de estas perspectivas para la tarea en cuestión.

### 5.6.5 Análisis de parámetros

Calculemos el número total de parámetros del módulo de atención multi-cabeza:

**Matrices de proyección por cabeza:**
- $\mathbf{W}_i^Q$: $d_{\text{model}} \times d_k$ parámetros
- $\mathbf{W}_i^K$: $d_{\text{model}} \times d_k$ parámetros
- $\mathbf{W}_i^V$: $d_{\text{model}} \times d_v$ parámetros

**Total por cabeza:** $d_{\text{model}} \times (2d_k + d_v)$

**Total para $h$ cabezas:** $h \times d_{\text{model}} \times (2d_k + d_v)$

Con $d_k = d_v = d_{\text{model}} / h$:

$$h \times d_{\text{model}} \times \frac{3 \, d_{\text{model}}}{h} = 3 \, d_{\text{model}}^2$$

**Matriz de proyección de salida:** $\mathbf{W}^O$: $d_{\text{model}} \times d_{\text{model}} = d_{\text{model}}^2$ parámetros.

**Total de parámetros MHA (sin sesgos):**

$$\text{Params}_{\text{MHA}} = 3\,d_{\text{model}}^2 + d_{\text{model}}^2 = 4\,d_{\text{model}}^2$$

**Ejemplo numérico:** Para el Transformer base de Vaswani et al. (2017), con $d_{\text{model}} = 512$ y $h = 8$:

- $d_k = d_v = 512 / 8 = 64$
- Parámetros por cabeza: $512 \times 64 \times 3 = 98{,}304$
- Parámetros de todas las cabezas: $8 \times 98{,}304 = 786{,}432$
- Parámetros de $\mathbf{W}^O$: $512 \times 512 = 262{,}144$
- **Total:** $786{,}432 + 262{,}144 = 1{,}048{,}576 \approx 1\text{M}$ parámetros

Nótese que este total ($4 \times 512^2 = 1{,}048{,}576$) es **independiente del número de cabezas** $h$: dividir la atención en más cabezas reduce la dimensión de cada cabeza pero no cambia el número total de parámetros. La elección de $h$ es, por lo tanto, una decisión arquitectónica que afecta la **capacidad de especialización** de cada cabeza, no el costo paramétrico total.

### 5.6.6 Complejidad computacional

La complejidad computacional del módulo MHA es:

- **Proyecciones lineales:** $O(T \cdot d_{\text{model}}^2)$ para calcular $\mathbf{Q}_i$, $\mathbf{K}_i$, $\mathbf{V}_i$ de todas las cabezas.
- **Atención por cabeza:** $O(T^2 \cdot d_k)$ para cada cabeza.
- **Total atención:** $h \times O(T^2 \cdot d_k) = O(T^2 \cdot h \cdot d_k) = O(T^2 \cdot d_{\text{model}})$.
- **Proyección de salida:** $O(T \cdot d_{\text{model}}^2)$.

**Complejidad total:** $O(T \cdot d_{\text{model}}^2 + T^2 \cdot d_{\text{model}})$.

Para secuencias cortas ($T \ll d_{\text{model}}$), el costo está dominado por las proyecciones lineales. Para secuencias largas ($T \gg d_{\text{model}}$), el término cuadrático $T^2$ domina, lo que constituye el principal cuello de botella de los modelos basados en atención para secuencias muy largas.

**Figura 5.3:** *Diagrama de la arquitectura de Multi-Head Attention. En la parte superior se muestra la entrada (las matrices $\mathbf{Q}$, $\mathbf{K}$, $\mathbf{V}$) alimentando $h$ bloques de atención en paralelo (dispuestos horizontalmente), etiquetados como "Cabeza 1", "Cabeza 2", ..., "Cabeza $h$". Dentro de cada bloque de cabeza se muestra una versión compacta del diagrama de Scaled Dot-Product Attention de la Figura 5.2, con las matrices de proyección específicas de cada cabeza ($\mathbf{W}_i^Q$, $\mathbf{W}_i^K$, $\mathbf{W}_i^V$) señaladas explícitamente como entradas. Los mapas de calor de atención dentro de cada cabeza muestran patrones diferentes: la Cabeza 1 podría mostrar un patrón diagonal (atención local), la Cabeza 2 un patrón con líneas verticales (atención a tokens globalmente importantes), y la Cabeza 3 un patrón disperso (relaciones semánticas específicas). Las salidas de todas las cabezas ($\text{head}_1, \ldots, \text{head}_h$, cada una de dimensión $T \times d_v$) convergen en un bloque de "Concatenación" (representado como la unión horizontal de los tensores), seguido de un bloque de "Proyección Lineal" ($\mathbf{W}^O$) que produce la salida final de dimensión $T \times d_{\text{model}}$. Las dimensiones se anotan en cada conexión para claridad.*

---

## 5.7 Implementación en PyTorch

### 5.7.1 Implementación de Scaled Dot-Product Attention

A continuación se presenta una implementación completa y comentada del mecanismo de Scaled Dot-Product Attention en PyTorch.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
import math


class ScaledDotProductAttention(nn.Module):
    """
    Implementación del mecanismo Scaled Dot-Product Attention.
    
    Calcula:
        Attention(Q, K, V) = softmax(Q K^T / sqrt(d_k)) V
    
    Args:
        temperature (float): Factor de escalamiento. Normalmente sqrt(d_k).
    """
    
    def __init__(self, temperature: float):
        super().__init__()
        # El factor de escalamiento controla la "suavidad" de la distribución
        # de atención. Valores más altos producen distribuciones más uniformes;
        # valores más bajos producen distribuciones más concentradas.
        self.temperature = temperature
    
    def forward(
        self,
        query: torch.Tensor,   # (batch, T_q, d_k)
        key: torch.Tensor,     # (batch, T_k, d_k)
        value: torch.Tensor,   # (batch, T_k, d_v)
        mask: torch.Tensor = None  # (batch, T_q, T_k) o (batch, 1, T_k)
    ) -> tuple[torch.Tensor, torch.Tensor]:
        """
        Calcula la atención escalada de producto punto.
        
        Args:
            query: Tensor de consultas de forma (batch, T_q, d_k).
            key: Tensor de claves de forma (batch, T_k, d_k).
            value: Tensor de valores de forma (batch, T_k, d_v).
            mask: Máscara opcional para impedir la atención a ciertas posiciones.
                  Las posiciones con valor True (o 1) serán enmascaradas
                  (recibirán -inf antes de la softmax).
        
        Returns:
            output: Resultado de la atención, forma (batch, T_q, d_v).
            attn_weights: Pesos de atención, forma (batch, T_q, T_k).
        """
        # Paso 1: Calcular puntuaciones brutas mediante producto punto
        # Q: (batch, T_q, d_k), K^T: (batch, d_k, T_k)
        # Resultado: (batch, T_q, T_k)
        scores = torch.bmm(query, key.transpose(1, 2))
        
        # Paso 2: Escalar por la temperatura (sqrt(d_k))
        # Esto previene que las puntuaciones tengan magnitudes muy grandes,
        # lo cual causaría que la softmax produzca gradientes cercanos a cero.
        scores = scores / self.temperature
        
        # Paso 3: Aplicar máscara (opcional)
        # Útil para: (a) ignorar tokens de padding,
        #            (b) atención causal (el decodificador no puede ver el futuro).
        if mask is not None:
            scores = scores.masked_fill(mask == 1, float('-inf'))
        
        # Paso 4: Softmax por la última dimensión (sobre las claves)
        # Convierte las puntuaciones en una distribución de probabilidad
        # para cada consulta sobre todas las claves.
        attn_weights = F.softmax(scores, dim=-1)
        
        # Paso 5: Multiplicar por los valores
        # Cada consulta obtiene una suma ponderada de los valores,
        # donde los pesos son las probabilidades de atención.
        output = torch.bmm(attn_weights, value)
        
        return output, attn_weights
```

### 5.7.2 Implementación de Multi-Head Attention

```python
class MultiHeadAttention(nn.Module):
    """
    Implementación del mecanismo Multi-Head Attention.
    
    MultiHead(Q, K, V) = Concat(head_1, ..., head_h) W^O
    donde head_i = Attention(Q W_i^Q, K W_i^K, V W_i^V)
    
    Args:
        d_model (int): Dimensión del modelo (tamaño de los embeddings).
        n_heads (int): Número de cabezas de atención.
        dropout (float): Tasa de dropout aplicada a los pesos de atención.
    """
    
    def __init__(self, d_model: int, n_heads: int, dropout: float = 0.1):
        super().__init__()
        
        # Verificar que d_model sea divisible entre n_heads
        assert d_model % n_heads == 0, \
            f"d_model ({d_model}) debe ser divisible entre n_heads ({n_heads})"
        
        self.d_model = d_model
        self.n_heads = n_heads
        self.d_k = d_model // n_heads  # Dimensión de cada cabeza
        self.d_v = d_model // n_heads
        
        # Proyecciones lineales para Q, K, V.
        # En lugar de tener h matrices separadas de tamaño (d_model, d_k),
        # usamos una sola matriz de tamaño (d_model, d_model) que proyecta
        # todas las cabezas simultáneamente. Esto es más eficiente en GPU.
        self.W_Q = nn.Linear(d_model, d_model, bias=False)
        self.W_K = nn.Linear(d_model, d_model, bias=False)
        self.W_V = nn.Linear(d_model, d_model, bias=False)
        
        # Proyección de salida W^O: combina las salidas de todas las cabezas
        self.W_O = nn.Linear(d_model, d_model, bias=False)
        
        # Módulo de atención escalada
        self.attention = ScaledDotProductAttention(
            temperature=math.sqrt(self.d_k)
        )
        
        # Dropout para regularización de los pesos de atención
        self.dropout = nn.Dropout(dropout)
    
    def forward(
        self,
        query: torch.Tensor,   # (batch, T_q, d_model)
        key: torch.Tensor,     # (batch, T_k, d_model)
        value: torch.Tensor,   # (batch, T_k, d_model)
        mask: torch.Tensor = None
    ) -> tuple[torch.Tensor, torch.Tensor]:
        """
        Calcula la atención multi-cabeza.
        
        En auto-atención: query = key = value = X (la misma entrada).
        En atención cruzada: query proviene del decodificador,
                             key y value del codificador.
        
        Args:
            query: (batch, T_q, d_model)
            key: (batch, T_k, d_model)
            value: (batch, T_k, d_model)
            mask: Máscara opcional (batch, T_q, T_k)
        
        Returns:
            output: (batch, T_q, d_model)
            attn_weights: (batch, n_heads, T_q, T_k)
        """
        batch_size = query.size(0)
        T_q = query.size(1)
        T_k = key.size(1)
        
        # --- Paso 1: Proyecciones lineales ---
        # Cada proyección: (batch, T, d_model) -> (batch, T, d_model)
        Q = self.W_Q(query)
        K = self.W_K(key)
        V = self.W_V(value)
        
        # --- Paso 2: Separar en múltiples cabezas ---
        # Reorganizar de (batch, T, d_model) a (batch, n_heads, T, d_k)
        # Esto se logra con reshape + transpose:
        #   (batch, T, d_model) -> (batch, T, n_heads, d_k) -> (batch, n_heads, T, d_k)
        Q = Q.view(batch_size, T_q, self.n_heads, self.d_k).transpose(1, 2)
        K = K.view(batch_size, T_k, self.n_heads, self.d_k).transpose(1, 2)
        V = V.view(batch_size, T_k, self.n_heads, self.d_v).transpose(1, 2)
        
        # Aplanar batch y heads para usar bmm:
        # (batch, n_heads, T, d_k) -> (batch * n_heads, T, d_k)
        Q = Q.reshape(batch_size * self.n_heads, T_q, self.d_k)
        K = K.reshape(batch_size * self.n_heads, T_k, self.d_k)
        V = V.reshape(batch_size * self.n_heads, T_k, self.d_v)
        
        # Ajustar máscara para las múltiples cabezas
        if mask is not None:
            # (batch, T_q, T_k) -> (batch * n_heads, T_q, T_k)
            mask = mask.unsqueeze(1).repeat(1, self.n_heads, 1, 1)
            mask = mask.reshape(batch_size * self.n_heads, T_q, T_k)
        
        # --- Paso 3: Calcular la atención para todas las cabezas ---
        # Esto es equivalente a calcular h atenciones independientes
        attn_output, attn_weights = self.attention(Q, K, V, mask=mask)
        # attn_output: (batch * n_heads, T_q, d_v)
        # attn_weights: (batch * n_heads, T_q, T_k)
        
        # Aplicar dropout a los pesos de atención
        attn_output = self.dropout(attn_output)
        
        # --- Paso 4: Concatenar las cabezas ---
        # (batch * n_heads, T_q, d_v) -> (batch, n_heads, T_q, d_v)
        attn_output = attn_output.view(
            batch_size, self.n_heads, T_q, self.d_v
        )
        # (batch, n_heads, T_q, d_v) -> (batch, T_q, n_heads, d_v)
        attn_output = attn_output.transpose(1, 2)
        # (batch, T_q, n_heads, d_v) -> (batch, T_q, n_heads * d_v = d_model)
        attn_output = attn_output.contiguous().view(
            batch_size, T_q, self.d_model
        )
        
        # --- Paso 5: Proyección de salida ---
        # (batch, T_q, d_model) -> (batch, T_q, d_model)
        output = self.W_O(attn_output)
        
        # Reorganizar pesos de atención para visualización
        attn_weights = attn_weights.view(
            batch_size, self.n_heads, T_q, T_k
        )
        
        return output, attn_weights
```

### 5.7.3 Ejemplo de uso y verificación

```python
def ejemplo_atencion():
    """
    Ejemplo completo que demuestra el uso de Multi-Head Attention
    con la oración "El gato se sentó".
    """
    # Configuración
    d_model = 16     # Dimensión del modelo (pequeña para demostración)
    n_heads = 4      # Número de cabezas de atención
    seq_len = 4      # 4 tokens: "El", "gato", "se", "sentó"
    batch_size = 1   # Un solo ejemplo
    
    # Fijar semilla para reproducibilidad
    torch.manual_seed(42)
    
    # Simular embeddings de entrada (normalmente provendrían
    # de una capa de embedding + codificación posicional)
    X = torch.randn(batch_size, seq_len, d_model)
    
    # Crear el módulo de atención multi-cabeza
    mha = MultiHeadAttention(d_model=d_model, n_heads=n_heads, dropout=0.0)
    
    # Auto-atención: Q = K = V = X
    output, attn_weights = mha(query=X, key=X, value=X)
    
    print(f"Entrada X:          {X.shape}")        # (1, 4, 16)
    print(f"Salida:             {output.shape}")    # (1, 4, 16)
    print(f"Pesos de atención:  {attn_weights.shape}")  # (1, 4, 4, 4)
    
    # Visualizar los pesos de atención de cada cabeza
    tokens = ["El", "gato", "se", "sentó"]
    for head in range(n_heads):
        print(f"\n--- Cabeza {head + 1} ---")
        weights = attn_weights[0, head].detach()
        for i, token_q in enumerate(tokens):
            pesos_str = ", ".join(
                f"{tokens[j]}: {weights[i, j]:.3f}"
                for j in range(seq_len)
            )
            print(f"  {token_q:>6s} atiende a -> {pesos_str}")
    
    # Verificar que la salida tiene la misma forma que la entrada
    assert output.shape == X.shape, "La forma de salida debe coincidir"
    
    # Verificar que los pesos de atención suman 1 por fila
    row_sums = attn_weights.sum(dim=-1)
    assert torch.allclose(row_sums, torch.ones_like(row_sums), atol=1e-5), \
        "Los pesos de atención deben sumar 1 por fila"
    
    print("\n¡Todas las verificaciones pasaron correctamente!")


# Crear máscara causal para decodificadores autoregresivos
def crear_mascara_causal(seq_len: int) -> torch.Tensor:
    """
    Crea una máscara triangular superior que impide que cada posición
    atienda a posiciones futuras. Esencial para decodificadores.
    
    Para seq_len=4, la máscara es:
        [[0, 1, 1, 1],
         [0, 0, 1, 1],
         [0, 0, 0, 1],
         [0, 0, 0, 0]]
    
    Donde 1 indica posiciones enmascaradas (no atender).
    """
    mask = torch.triu(torch.ones(seq_len, seq_len), diagonal=1)
    return mask.unsqueeze(0)  # (1, seq_len, seq_len) para broadcasting


if __name__ == "__main__":
    ejemplo_atencion()
```

### 5.7.4 Notas de implementación

**Eficiencia de la implementación conjunta de proyecciones:** En la implementación presentada, cada proyección ($\mathbf{W}^Q$, $\mathbf{W}^K$, $\mathbf{W}^V$) se realiza como una transformación lineal de $d_{\text{model}}$ a $d_{\text{model}}$, seguida de una reorganización de dimensiones para separar las cabezas. Esto es matemáticamente equivalente a tener $h$ proyecciones separadas de $d_{\text{model}}$ a $d_k$, pero es significativamente más eficiente porque se aprovecha el paralelismo de las operaciones matriciales grandes en GPU. En algunos frameworks y bibliotecas, las tres proyecciones ($\mathbf{W}^Q$, $\mathbf{W}^K$, $\mathbf{W}^V$) se combinan incluso en una sola capa lineal de $d_{\text{model}}$ a $3 \cdot d_{\text{model}}$, seguida de un corte (*split*) en tres partes, lo que maximiza la eficiencia computacional.

**Máscara causal:** En el decodificador de un Transformer autoregresivo, es fundamental impedir que cada posición atienda a posiciones futuras (ya que durante la inferencia, esos tokens aún no se han generado). Esto se logra mediante una **máscara causal** (triangular superior) que asigna $-\infty$ a las posiciones futuras antes de la softmax, forzando que $\alpha_{ij} = 0$ para $j > i$.

**Máscara de padding:** Cuando se procesan lotes (*batches*) de secuencias de longitud variable, las secuencias más cortas se rellenan con tokens de *padding*. La máscara de padding evita que el modelo preste atención a estas posiciones artificiales, que no contienen información semántica relevante.

---

## Referencias

- Bahdanau, D., Cho, K., & Bengio, Y. (2015). Neural Machine Translation by Jointly Learning to Align and Translate. *Proceedings of the 3rd International Conference on Learning Representations (ICLR 2015)*. arXiv:1409.0473.

- Cho, K., van Merriënboer, B., Gulcehre, C., Bahdanau, D., Bougares, F., Schwenk, H., & Bengio, Y. (2014). Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation. *Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing (EMNLP)*, pp. 1724–1734. DOI: 10.3115/v1/D14-1179.

- Luong, M.-T., Pham, H., & Manning, C. D. (2015). Effective Approaches to Attention-based Neural Machine Translation. *Proceedings of the 2015 Conference on Empirical Methods in Natural Language Processing (EMNLP)*, pp. 1412–1421. DOI: 10.18653/v1/D15-1166.

- Sutskever, I., Vinyals, O., & Le, Q. V. (2014). Sequence to Sequence Learning with Neural Networks. *Advances in Neural Information Processing Systems 27 (NeurIPS 2014)*, pp. 3104–3112. arXiv:1409.3215.

- Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). Attention Is All You Need. *Advances in Neural Information Processing Systems 30 (NeurIPS 2017)*, pp. 5998–6008. arXiv:1706.03762.

---

# 6. La Arquitectura Transformer

La arquitectura Transformer representa, sin lugar a dudas, uno de los avances más trascendentales en la historia del aprendizaje profundo y del procesamiento de lenguaje natural. Publicada en 2017 por Vaswani y colaboradores, esta arquitectura rompió con el paradigma dominante de las redes neuronales recurrentes al demostrar que el mecanismo de atención, por sí solo, era suficiente para modelar dependencias secuenciales de manera más eficiente y efectiva. En esta sección, estudiaremos en profundidad cada componente de la arquitectura Transformer, desde la codificación posicional hasta la estructura completa encoder-decoder, proporcionando las bases matemáticas, la intuición geométrica y los detalles de implementación necesarios para comprender su funcionamiento y su papel fundamental en las comunicaciones semánticas modernas.

---

## 6.1 Contexto histórico y motivación

### 6.1.1 Limitaciones de las arquitecturas recurrentes

Antes de la aparición del Transformer, las redes neuronales recurrentes (RNN), las redes LSTM (*Long Short-Term Memory*) y las redes GRU (*Gated Recurrent Unit*) constituían el estado del arte para el procesamiento de secuencias. Estas arquitecturas procesan los elementos de una secuencia de manera estrictamente secuencial: para computar la representación oculta $\mathbf{h}_t$ en la posición $t$, es necesario haber calculado previamente $\mathbf{h}_{t-1}$. Esta dependencia secuencial se expresa formalmente como:

$$\mathbf{h}_t = f(\mathbf{h}_{t-1}, \mathbf{x}_t)$$

donde $f$ es la función de transición de estado (que en el caso de LSTM incluye las compuertas de olvido, entrada y salida), $\mathbf{x}_t$ es la entrada en la posición $t$ y $\mathbf{h}_{t-1}$ es el estado oculto anterior.

Esta naturaleza secuencial impone varias limitaciones fundamentales:

1. **Paralelismo limitado durante el entrenamiento.** Dado que cada paso temporal depende del anterior, no es posible calcular los estados ocultos de diferentes posiciones de manera simultánea. En una secuencia de longitud $T$, el cálculo requiere $T$ pasos secuenciales, lo que impide aprovechar eficientemente las capacidades de cómputo paralelo de las GPU modernas. Mientras que las operaciones sobre lotes (*batches*) de secuencias pueden paralelizarse, las operaciones *dentro* de cada secuencia individual permanecen inherentemente secuenciales.

2. **Degradación en dependencias de largo alcance.** A pesar de que las LSTM fueron diseñadas específicamente para mitigar el problema del desvanecimiento del gradiente (*vanishing gradient*), en la práctica su capacidad para capturar dependencias a muy largo alcance sigue siendo limitada. La información debe fluir a través de múltiples pasos de la cadena recurrente, y con cada paso existe la posibilidad de que se diluya o se pierda. En una secuencia de longitud $T$, la señal entre la posición $1$ y la posición $T$ debe recorrer $O(T)$ pasos, lo que dificulta el aprendizaje de relaciones distantes.

3. **Cuello de botella de información.** En las arquitecturas encoder-decoder basadas en RNN, toda la información de la secuencia de entrada se comprime en un único vector de contexto $\mathbf{c}$ (el último estado oculto del encoder). Para secuencias largas, este vector fijo se convierte en un cuello de botella que limita la cantidad de información que puede transmitirse al decoder. Aunque el mecanismo de atención de Bahdanau (2014) alivió parcialmente este problema al permitir que el decoder accediera a todos los estados ocultos del encoder, la arquitectura subyacente seguía siendo recurrente.

4. **Velocidad de entrenamiento.** La imposibilidad de paralelizar el procesamiento dentro de cada secuencia se traduce en tiempos de entrenamiento significativamente más largos, especialmente para conjuntos de datos masivos y secuencias extensas. Esta limitación práctica restringía la escala de los modelos y los datos que podían utilizarse.

### 6.1.2 El artículo "Attention Is All You Need"

En junio de 2017, Vaswani, Shazeer, Parmar, Uszkoreit, Jones, Gomez, Kaiser y Polosukhin publicaron el artículo seminal *"Attention Is All You Need"*, presentado en la conferencia NeurIPS (Vaswani et al., 2017). La idea central del artículo era revolucionariamente simple: **eliminar por completo la recurrencia** y basar la arquitectura exclusivamente en mecanismos de atención.

Los autores propusieron el *Transformer*, una arquitectura que reemplaza las capas recurrentes por capas de *self-attention* (auto-atención) y redes *feed-forward* posición por posición. Las contribuciones clave del artículo incluyen:

- **Self-Attention Multi-Cabezal (*Multi-Head Attention*)**: permite que cada posición de la secuencia atienda simultáneamente a todas las demás posiciones, capturando dependencias sin importar la distancia.
- **Codificación posicional**: dado que la arquitectura no tiene noción inherente de orden secuencial (a diferencia de las RNN), se introduce información posicional mediante funciones sinusoidales.
- **Paralelismo completo**: todas las posiciones de la secuencia pueden procesarse simultáneamente durante el entrenamiento, aprovechando al máximo la arquitectura de las GPU.
- **Rendimiento superior**: el Transformer estableció nuevos récords en tareas de traducción automática, alcanzando un BLEU de 28.4 en la tarea inglés-alemán del WMT 2014, superando a todos los modelos previos incluyendo ensambles (*ensembles*).

La intuición fundamental detrás del Transformer puede resumirse así: en lugar de procesar una secuencia elemento por elemento y acumular información en un estado oculto, se permite que todos los elementos de la secuencia "se comuniquen" directamente entre sí a través del mecanismo de atención. La longitud del camino entre cualquier par de posiciones se reduce de $O(T)$ en las RNN a $O(1)$ en el Transformer, lo que facilita enormemente el aprendizaje de dependencias a largo alcance.

Esta idea, que en retrospectiva parece natural, representó un cambio de paradigma que transformó no solo el procesamiento de lenguaje natural, sino también la visión por computadora, el procesamiento de audio, la bioinformática y, como veremos en secciones posteriores, las comunicaciones semánticas.

> **Referencia:** Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). Attention is all you need. *Advances in Neural Information Processing Systems*, 30. (DOI: 10.48550/arXiv.1706.03762)

---

## 6.2 Codificación posicional (*Positional Encoding*)

### 6.2.1 La necesidad de codificar posiciones

Las redes recurrentes tienen una ventaja inherente sobre las arquitecturas basadas puramente en atención: procesan la secuencia de manera ordenada, de modo que la posición de cada elemento está implícitamente codificada en el orden de procesamiento. El estado oculto $\mathbf{h}_t$ "sabe" que corresponde a la posición $t$ porque fue calculado después de $\mathbf{h}_{t-1}$.

El Transformer, en cambio, procesa todas las posiciones de la secuencia de manera simultánea. La operación de self-attention es, en esencia, una operación sobre *conjuntos* (*sets*): si permutamos las posiciones de entrada, las salidas se permutan de la misma manera, pero las relaciones de atención entre tokens no cambian. Formalmente, si $\pi$ es una permutación y $\mathbf{X} = [\mathbf{x}_1, \ldots, \mathbf{x}_T]$ es la matriz de entrada, entonces:

$$\text{Attention}(\pi(\mathbf{X})) = \pi(\text{Attention}(\mathbf{X}))$$

Esto significa que, sin información posicional adicional, el modelo trataría las oraciones "El gato persigue al ratón" y "El ratón persigue al gato" de manera idéntica (asumiendo que los embeddings de las palabras son los mismos), ya que los mismos tokens están presentes en ambas oraciones, solo cambia su orden.

Para resolver este problema, Vaswani et al. propusieron sumar una *codificación posicional* (*positional encoding*) a los embeddings de entrada. Formalmente, si $\mathbf{e}_i$ es el embedding del token en la posición $i$, la entrada al primer bloque del Transformer es:

$$\mathbf{z}_i = \mathbf{e}_i + \mathbf{PE}_i$$

donde $\mathbf{PE}_i \in \mathbb{R}^{d_{model}}$ es el vector de codificación posicional para la posición $i$. La suma (en lugar de concatenación) se elige para mantener la dimensionalidad del modelo y porque empíricamente funciona bien.

### 6.2.2 Codificación sinusoidal

Vaswani et al. propusieron una codificación posicional basada en funciones sinusoidales de diferentes frecuencias. Para cada posición $pos$ en la secuencia y cada dimensión $i$ del vector de embedding, la codificación posicional se define como:

$$PE_{(pos, 2i)} = \sin\left(\frac{pos}{10000^{2i/d_{model}}}\right)$$

$$PE_{(pos, 2i+1)} = \cos\left(\frac{pos}{10000^{2i/d_{model}}}\right)$$

donde $pos \in \{0, 1, 2, \ldots, T-1\}$ es la posición en la secuencia, $i \in \{0, 1, 2, \ldots, d_{model}/2 - 1\}$ es el índice de la dimensión del par seno-coseno, y $d_{model}$ es la dimensión del modelo (es decir, la dimensión de los embeddings y de todas las representaciones internas).

Analicemos esta fórmula con cuidado. Para cada par de dimensiones $(2i, 2i+1)$, se utiliza una función sinusoidal con una frecuencia angular específica:

$$\omega_i = \frac{1}{10000^{2i/d_{model}}}$$

La frecuencia $\omega_i$ varía geométricamente a lo largo de las dimensiones: para $i = 0$, tenemos $\omega_0 = 1$ (frecuencia más alta, período $2\pi \approx 6.28$ posiciones), y para $i = d_{model}/2 - 1$, tenemos $\omega_{d_{model}/2 - 1} \approx 1/10000$ (frecuencia más baja, período $2\pi \cdot 10000 \approx 62832$ posiciones). Esta progresión geométrica de frecuencias es análoga a la representación de un número en diferentes bases: las dimensiones de alta frecuencia cambian rápidamente con la posición (como los dígitos menos significativos), mientras que las dimensiones de baja frecuencia cambian lentamente (como los dígitos más significativos).

### 6.2.3 Propiedad de posiciones relativas

Una propiedad crucial de la codificación sinusoidal es que permite al modelo aprender a atender a posiciones relativas. Esto se debe a que, para cualquier desplazamiento fijo $k$, la codificación posicional $\mathbf{PE}_{pos+k}$ puede expresarse como una transformación lineal de $\mathbf{PE}_{pos}$.

Para demostrar esto, consideremos un par de dimensiones $(2i, 2i+1)$. Usando las identidades trigonométricas de suma de ángulos:

$$\sin(\alpha + \beta) = \sin \alpha \cos \beta + \cos \alpha \sin \beta$$
$$\cos(\alpha + \beta) = \cos \alpha \cos \beta - \sin \alpha \sin \beta$$

Con $\alpha = pos \cdot \omega_i$ y $\beta = k \cdot \omega_i$, obtenemos:

$$PE_{(pos+k, 2i)} = \sin((pos+k) \cdot \omega_i) = \sin(pos \cdot \omega_i) \cos(k \cdot \omega_i) + \cos(pos \cdot \omega_i) \sin(k \cdot \omega_i)$$

$$PE_{(pos+k, 2i+1)} = \cos((pos+k) \cdot \omega_i) = \cos(pos \cdot \omega_i) \cos(k \cdot \omega_i) - \sin(pos \cdot \omega_i) \sin(k \cdot \omega_i)$$

Esto puede escribirse en forma matricial como:

$$\begin{bmatrix} PE_{(pos+k, 2i)} \\ PE_{(pos+k, 2i+1)} \end{bmatrix} = \begin{bmatrix} \cos(k \cdot \omega_i) & \sin(k \cdot \omega_i) \\ -\sin(k \cdot \omega_i) & \cos(k \cdot \omega_i) \end{bmatrix} \begin{bmatrix} PE_{(pos, 2i)} \\ PE_{(pos, 2i+1)} \end{bmatrix}$$

La matriz de transformación es una *matriz de rotación* que depende únicamente del desplazamiento $k$ y de la frecuencia $\omega_i$, pero **no** de la posición absoluta $pos$. Esto significa que la relación entre las codificaciones posicionales de dos posiciones separadas por una distancia $k$ es siempre la misma, independientemente de dónde se encuentren en la secuencia. Esta propiedad permite que las capas de atención aprendan patrones basados en posiciones relativas, lo cual es fundamental para la generalización a secuencias de longitudes no vistas durante el entrenamiento.

### 6.2.4 Ejemplo numérico

Para solidificar la comprensión, calculemos la codificación posicional para las posiciones $pos = 0, 1, 2, 3, 4$ con un modelo pequeño de dimensión $d_{model} = 4$. Tenemos dos pares de dimensiones: $(2i=0, 2i+1=1)$ con $i=0$ y $(2i=2, 2i+1=3)$ con $i=1$.

Primero, calculamos las frecuencias angulares:

- Para $i = 0$: $\omega_0 = \frac{1}{10000^{0/4}} = \frac{1}{10000^0} = 1$
- Para $i = 1$: $\omega_1 = \frac{1}{10000^{2/4}} = \frac{1}{10000^{0.5}} = \frac{1}{100} = 0.01$

Ahora calculamos los valores para cada posición:

**Posición $pos = 0$:**

$$PE_{(0,0)} = \sin(0 \cdot 1) = \sin(0) = 0$$
$$PE_{(0,1)} = \cos(0 \cdot 1) = \cos(0) = 1$$
$$PE_{(0,2)} = \sin(0 \cdot 0.01) = \sin(0) = 0$$
$$PE_{(0,3)} = \cos(0 \cdot 0.01) = \cos(0) = 1$$

$$\mathbf{PE}_0 = [0, \ 1, \ 0, \ 1]$$

**Posición $pos = 1$:**

$$PE_{(1,0)} = \sin(1 \cdot 1) = \sin(1) \approx 0.8415$$
$$PE_{(1,1)} = \cos(1 \cdot 1) = \cos(1) \approx 0.5403$$
$$PE_{(1,2)} = \sin(1 \cdot 0.01) = \sin(0.01) \approx 0.0100$$
$$PE_{(1,3)} = \cos(1 \cdot 0.01) = \cos(0.01) \approx 0.9999$$

$$\mathbf{PE}_1 \approx [0.8415, \ 0.5403, \ 0.0100, \ 0.9999]$$

**Posición $pos = 2$:**

$$PE_{(2,0)} = \sin(2) \approx 0.9093$$
$$PE_{(2,1)} = \cos(2) \approx -0.4161$$
$$PE_{(2,2)} = \sin(0.02) \approx 0.0200$$
$$PE_{(2,3)} = \cos(0.02) \approx 0.9998$$

$$\mathbf{PE}_2 \approx [0.9093, \ {-0.4161}, \ 0.0200, \ 0.9998]$$

**Posición $pos = 3$:**

$$PE_{(3,0)} = \sin(3) \approx 0.1411$$
$$PE_{(3,1)} = \cos(3) \approx -0.9900$$
$$PE_{(3,2)} = \sin(0.03) \approx 0.0300$$
$$PE_{(3,3)} = \cos(0.03) \approx 0.9996$$

$$\mathbf{PE}_3 \approx [0.1411, \ {-0.9900}, \ 0.0300, \ 0.9996]$$

**Posición $pos = 4$:**

$$PE_{(4,0)} = \sin(4) \approx -0.7568$$
$$PE_{(4,1)} = \cos(4) \approx -0.6536$$
$$PE_{(4,2)} = \sin(0.04) \approx 0.0400$$
$$PE_{(4,3)} = \cos(0.04) \approx 0.9992$$

$$\mathbf{PE}_4 \approx [-0.7568, \ {-0.6536}, \ 0.0400, \ 0.9992]$$

Observemos varios patrones importantes en estos resultados:

- Las dimensiones 0 y 1 (alta frecuencia, $\omega_0 = 1$) oscilan rápidamente: los valores cambian significativamente de una posición a la siguiente.
- Las dimensiones 2 y 3 (baja frecuencia, $\omega_1 = 0.01$) cambian muy lentamente: los valores apenas se modifican entre posiciones consecutivas.
- Cada posición tiene un vector de codificación único, lo que permite distinguirla de las demás.
- Los vectores de posiciones cercanas son más similares entre sí que los de posiciones lejanas, lo cual es una propiedad deseable.

En un modelo real con $d_{model} = 512$, habría 256 pares de frecuencias cubriendo un espectro continuo desde oscilaciones rápidas hasta oscilaciones extremadamente lentas, proporcionando una representación rica y expresiva de la posición.

**Figura 6.1:** *Mapa de calor de la codificación posicional sinusoidal para posiciones $0$ a $49$ (eje vertical) y dimensiones $0$ a $127$ (eje horizontal), con $d_{model} = 128$. Cada fila corresponde al vector de codificación posicional de una posición específica. Las dimensiones bajas (izquierda) presentan patrones de alta frecuencia que oscilan rápidamente entre valores positivos (colores cálidos) y negativos (colores fríos), mientras que las dimensiones altas (derecha) muestran patrones de frecuencia progresivamente menor, con ondas cada vez más amplias. Se observa que cada posición genera un patrón sinusoidal único, creando una "huella digital" posicional. Las franjas verticales de la izquierda, que alternan rápidamente, corresponden a $\omega_i$ grandes, y las bandas anchas de la derecha corresponden a $\omega_i$ pequeños. Esta variación multiescala permite que el Transformer capture tanto relaciones posicionales locales como globales.*

### 6.2.5 Codificaciones posicionales aprendidas

Además de la codificación sinusoidal fija, los autores del Transformer original también experimentaron con codificaciones posicionales aprendidas, donde cada posición tiene un vector de embedding que se optimiza durante el entrenamiento, de manera similar a los embeddings de palabras. Los resultados mostraron que ambos enfoques producían un rendimiento prácticamente idéntico. Sin embargo, la codificación sinusoidal tiene la ventaja teórica de poder generalizar a secuencias más largas que las vistas durante el entrenamiento, ya que las funciones sinusoidales están definidas para cualquier valor de $pos$, mientras que las codificaciones aprendidas están limitadas a las posiciones vistas durante el entrenamiento.

En la práctica, muchas implementaciones modernas de Transformers utilizan codificaciones posicionales aprendidas (como en BERT y GPT) o variantes más sofisticadas como las codificaciones posicionales rotatorias (*Rotary Position Embeddings*, RoPE), que incorporan la información posicional directamente en el mecanismo de atención mediante rotaciones en el espacio de embeddings.

---

## 6.3 El bloque Encoder del Transformer

### 6.3.1 Visión general de la arquitectura del encoder

El encoder del Transformer tiene como objetivo transformar una secuencia de entrada $\mathbf{X} = (\mathbf{x}_1, \mathbf{x}_2, \ldots, \mathbf{x}_T)$ en una secuencia de representaciones contextualizadas $\mathbf{Z} = (\mathbf{z}_1, \mathbf{z}_2, \ldots, \mathbf{z}_T)$, donde cada vector $\mathbf{z}_t$ captura no solo la información del token $t$, sino también su relación con todos los demás tokens de la secuencia.

El encoder está compuesto por una pila de $N$ bloques (*layers*) idénticos. En el modelo base del Transformer original, $N = 6$. Cada bloque consta de dos sub-capas principales, cada una envuelta en una conexión residual y seguida de una normalización de capa. El flujo de datos a través de un bloque encoder es el siguiente:

1. **Embedding de entrada + Codificación posicional**
2. **Multi-Head Self-Attention**
3. **Add & Norm** (conexión residual + normalización de capa)
4. **Red Feed-Forward** posición por posición
5. **Add & Norm** (conexión residual + normalización de capa)

Describamos cada componente en detalle.

### 6.3.2 Embedding de entrada y codificación posicional

El primer paso consiste en convertir los tokens de entrada (típicamente representados como índices enteros en un vocabulario) en vectores densos de dimensión $d_{model}$. Esto se logra mediante una capa de embedding:

$$\mathbf{e}_t = \text{Embedding}(x_t) \in \mathbb{R}^{d_{model}}$$

A estos vectores de embedding se les suma la codificación posicional:

$$\mathbf{z}_t^{(0)} = \mathbf{e}_t + \mathbf{PE}_t$$

donde $\mathbf{z}_t^{(0)}$ denota la representación de entrada antes de pasar por los bloques del encoder. Es importante notar que los embeddings se escalan típicamente por un factor de $\sqrt{d_{model}}$ antes de sumar la codificación posicional:

$$\mathbf{z}_t^{(0)} = \sqrt{d_{model}} \cdot \mathbf{e}_t + \mathbf{PE}_t$$

Este escalado se realiza porque los valores de los embeddings aprendidos tienden a tener magnitudes pequeñas (especialmente al inicio del entrenamiento, cuando se inicializan aleatoriamente), mientras que las codificaciones posicionales sinusoidales tienen valores en el rango $[-1, 1]$. El factor $\sqrt{d_{model}}$ asegura que la magnitud de los embeddings sea comparable a la de las codificaciones posicionales, evitando que la información posicional domine sobre la información semántica.

### 6.3.3 Multi-Head Self-Attention

La primera sub-capa de cada bloque encoder es una capa de *Multi-Head Self-Attention* (MHSA), que fue descrita en detalle en la Sección 5. En la self-attention del encoder, las matrices de consulta ($\mathbf{Q}$), clave ($\mathbf{K}$) y valor ($\mathbf{V}$) se derivan todas de la misma entrada:

$$\mathbf{Q} = \mathbf{Z}^{(\ell-1)} \mathbf{W}^Q, \quad \mathbf{K} = \mathbf{Z}^{(\ell-1)} \mathbf{W}^K, \quad \mathbf{V} = \mathbf{Z}^{(\ell-1)} \mathbf{W}^V$$

donde $\mathbf{Z}^{(\ell-1)} \in \mathbb{R}^{T \times d_{model}}$ es la salida de la capa anterior (o la entrada con codificación posicional para la primera capa), y $\mathbf{W}^Q, \mathbf{W}^K \in \mathbb{R}^{d_{model} \times d_k}$, $\mathbf{W}^V \in \mathbb{R}^{d_{model} \times d_v}$ son matrices de proyección aprendibles.

La atención escalada por producto punto se calcula como:

$$\text{Attention}(\mathbf{Q}, \mathbf{K}, \mathbf{V}) = \text{softmax}\left(\frac{\mathbf{Q}\mathbf{K}^\top}{\sqrt{d_k}}\right)\mathbf{V}$$

En la versión multi-cabezal con $h$ cabezas, cada cabeza $j$ tiene sus propias proyecciones $\mathbf{W}_j^Q, \mathbf{W}_j^K, \mathbf{W}_j^V$, y las salidas de todas las cabezas se concatenan y se proyectan:

$$\text{MultiHead}(\mathbf{Q}, \mathbf{K}, \mathbf{V}) = \text{Concat}(\text{head}_1, \ldots, \text{head}_h)\mathbf{W}^O$$

donde $\text{head}_j = \text{Attention}(\mathbf{Q}\mathbf{W}_j^Q, \mathbf{K}\mathbf{W}_j^K, \mathbf{V}\mathbf{W}_j^V)$ y $\mathbf{W}^O \in \mathbb{R}^{hd_v \times d_{model}}$.

En el encoder, la self-attention es *bidireccional*: cada token puede atender a todos los demás tokens de la secuencia, incluyendo los que están antes y después de él. No se aplica ninguna máscara causal, lo que permite al encoder construir representaciones que incorporan contexto de toda la secuencia.

### 6.3.4 Conexiones residuales

Las conexiones residuales (*residual connections* o *skip connections*), introducidas por He et al. (2016) en el contexto de redes convolucionales profundas (ResNet), son un componente esencial del Transformer. La idea es simple pero poderosa: en lugar de que cada sub-capa aprenda la transformación deseada $F(\mathbf{x})$, se le pide que aprenda la *función residual* $F(\mathbf{x}) - \mathbf{x}$, y la salida se obtiene sumando la entrada original:

$$\text{Output} = \mathbf{x} + \text{Sublayer}(\mathbf{x})$$

Las conexiones residuales ofrecen varias ventajas críticas:

1. **Facilitan el flujo del gradiente.** Durante la retropropagación, el gradiente de la pérdida con respecto a $\mathbf{x}$ es:

$$\frac{\partial \mathcal{L}}{\partial \mathbf{x}} = \frac{\partial \mathcal{L}}{\partial \text{Output}} \cdot \left(\mathbf{I} + \frac{\partial \text{Sublayer}(\mathbf{x})}{\partial \mathbf{x}}\right)$$

El término $\mathbf{I}$ (la matriz identidad) asegura que siempre existe un camino directo para el gradiente, incluso si $\frac{\partial \text{Sublayer}(\mathbf{x})}{\partial \mathbf{x}}$ es pequeño. Esto mitiga el problema del desvanecimiento del gradiente en redes profundas.

2. **Preservan la información.** La conexión residual garantiza que la información de la entrada original siempre está disponible en la salida. La sub-capa solo necesita aprender las *modificaciones* que deben hacerse a la representación, no reconstruirla desde cero.

3. **Facilitan el aprendizaje de funciones identidad.** Si la transformación óptima en una capa determinada es la identidad (es decir, no hacer nada), la red simplemente necesita que $\text{Sublayer}(\mathbf{x}) \approx 0$, lo cual es mucho más fácil de aprender que hacer que $F(\mathbf{x}) \approx \mathbf{x}$ directamente.

4. **Permiten la construcción de redes más profundas.** Sin conexiones residuales, entrenar redes con muchas capas se vuelve extremadamente difícil. Los Transformers grandes pueden tener docenas o incluso cientos de capas, lo cual sería imposible sin conexiones residuales.

> **Referencia:** He, K., Zhang, X., Ren, S., & Sun, J. (2016). Deep residual learning for image recognition. *Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition*, 770-778. (DOI: 10.1109/CVPR.2016.90)

### 6.3.5 Normalización de capa (*Layer Normalization*)

Después de la conexión residual, se aplica *Layer Normalization* (LN), propuesta por Ba, Kiros y Hinton (2016). A diferencia de la *Batch Normalization*, que normaliza a lo largo de la dimensión del lote (y por tanto depende del tamaño del lote y no es adecuada para secuencias de longitud variable), la Layer Normalization normaliza a lo largo de la dimensión de las características para cada ejemplo individual.

Dado un vector $\mathbf{x} \in \mathbb{R}^{d_{model}}$, la Layer Normalization se define como:

$$\text{LN}(\mathbf{x}) = \gamma \odot \frac{\mathbf{x} - \mu}{\sigma + \epsilon} + \beta$$

donde:

- $\mu = \frac{1}{d_{model}} \sum_{j=1}^{d_{model}} x_j$ es la media de los elementos del vector.
- $\sigma = \sqrt{\frac{1}{d_{model}} \sum_{j=1}^{d_{model}} (x_j - \mu)^2}$ es la desviación estándar de los elementos del vector.
- $\gamma \in \mathbb{R}^{d_{model}}$ y $\beta \in \mathbb{R}^{d_{model}}$ son parámetros aprendibles de escala y desplazamiento, respectivamente.
- $\epsilon$ es una constante pequeña (típicamente $10^{-5}$ o $10^{-6}$) para estabilidad numérica, evitando la división por cero.
- $\odot$ denota el producto elemento a elemento (producto de Hadamard).

La normalización tiene varios efectos beneficiosos:

1. **Estabiliza el entrenamiento.** Al normalizar las activaciones, se evitan problemas de escalas muy diferentes entre las representaciones de distintas capas, lo que permite utilizar tasas de aprendizaje más altas.
2. **Reduce la dependencia de la inicialización.** La normalización hace que la red sea menos sensible a la elección de los valores iniciales de los pesos.
3. **Actúa como regularizador.** La normalización introduce una forma sutil de regularización que puede mejorar la generalización.

Los parámetros $\gamma$ y $\beta$ son necesarios porque, sin ellos, la normalización restringiría las activaciones a tener media cero y varianza unitaria, lo cual podría ser una restricción demasiado fuerte. Estos parámetros permiten que la red aprenda a "des-normalizar" si es necesario, recuperando la capacidad representativa completa.

En el Transformer original, la normalización se aplica *después* de la conexión residual (*Post-LN*):

$$\mathbf{z}' = \text{LN}(\mathbf{x} + \text{Sublayer}(\mathbf{x}))$$

Sin embargo, trabajos posteriores han mostrado que aplicar la normalización *antes* de la sub-capa (*Pre-LN*) puede mejorar la estabilidad del entrenamiento, especialmente para modelos muy profundos:

$$\mathbf{z}' = \mathbf{x} + \text{Sublayer}(\text{LN}(\mathbf{x}))$$

> **Referencia:** Ba, J. L., Kiros, J. R., & Hinton, G. E. (2016). Layer normalization. *arXiv preprint arXiv:1607.06450*. (DOI: 10.48550/arXiv.1607.06450)

### 6.3.6 Red Feed-Forward posición por posición

La segunda sub-capa de cada bloque encoder es una red *feed-forward* (FFN) que se aplica de manera independiente y posición por posición. Es decir, la misma red se aplica a cada posición de la secuencia de manera idéntica, sin interacción entre posiciones (la interacción entre posiciones ya fue capturada por la capa de atención).

La FFN consiste en dos transformaciones lineales con una activación ReLU (o variantes como GELU) entre ellas:

$$\text{FFN}(\mathbf{x}) = \max(0, \mathbf{x}\mathbf{W}_1 + \mathbf{b}_1)\mathbf{W}_2 + \mathbf{b}_2$$

donde:

- $\mathbf{W}_1 \in \mathbb{R}^{d_{model} \times d_{ff}}$ y $\mathbf{b}_1 \in \mathbb{R}^{d_{ff}}$ son los pesos y bias de la primera capa lineal.
- $\mathbf{W}_2 \in \mathbb{R}^{d_{ff} \times d_{model}}$ y $\mathbf{b}_2 \in \mathbb{R}^{d_{model}}$ son los pesos y bias de la segunda capa lineal.
- $\max(0, \cdot)$ es la función de activación ReLU.
- $d_{ff}$ es la dimensión de la capa oculta interna de la FFN.

En el modelo base del Transformer, $d_{model} = 512$ y $d_{ff} = 2048$, es decir, la capa oculta tiene una dimensionalidad cuatro veces mayor que la dimensión del modelo. Esta expansión y posterior compresión permite a la red aprender transformaciones no lineales complejas en un espacio de mayor dimensionalidad.

La FFN puede interpretarse como una red de dos capas que actúa como un "procesador" local: mientras que la capa de atención mezcla información entre posiciones, la FFN procesa la información de cada posición de manera independiente, refinando las representaciones contextualizadas.

Investigaciones recientes han sugerido que la FFN actúa como una especie de *memoria clave-valor*, donde la primera capa lineal ($\mathbf{W}_1$) actúa como la clave que detecta ciertos patrones en la entrada, y la segunda capa lineal ($\mathbf{W}_2$) produce los valores asociados. Bajo esta interpretación, las neuronas de la capa oculta se especializan en detectar patrones específicos (como n-gramas, categorías semánticas o relaciones sintácticas), y sus activaciones determinan qué información se añade a la representación.

### 6.3.7 Estructura completa de un bloque encoder

Combinando todos los componentes, el procesamiento de un bloque encoder completo puede describirse formalmente como:

$$\mathbf{a}^{(\ell)} = \text{LN}\left(\mathbf{Z}^{(\ell-1)} + \text{MHSA}\left(\mathbf{Z}^{(\ell-1)}\right)\right)$$

$$\mathbf{Z}^{(\ell)} = \text{LN}\left(\mathbf{a}^{(\ell)} + \text{FFN}\left(\mathbf{a}^{(\ell)}\right)\right)$$

donde $\mathbf{Z}^{(\ell-1)} \in \mathbb{R}^{T \times d_{model}}$ es la entrada al bloque $\ell$ (con $\ell = 1, 2, \ldots, N$), $\mathbf{a}^{(\ell)}$ es la salida intermedia después de la self-attention con su Add & Norm, y $\mathbf{Z}^{(\ell)} \in \mathbb{R}^{T \times d_{model}}$ es la salida del bloque.

Los $N$ bloques se apilan secuencialmente, de modo que la salida del bloque $\ell$ se convierte en la entrada del bloque $\ell + 1$. Es importante enfatizar que, aunque todos los bloques tienen la misma estructura, **no comparten parámetros**: cada bloque tiene sus propias matrices de proyección para la atención ($\mathbf{W}_j^Q, \mathbf{W}_j^K, \mathbf{W}_j^V, \mathbf{W}^O$), sus propios pesos de la FFN ($\mathbf{W}_1, \mathbf{b}_1, \mathbf{W}_2, \mathbf{b}_2$), y sus propios parámetros de normalización ($\gamma, \beta$) para cada sub-capa.

La salida del último bloque encoder, $\mathbf{Z}^{(N)} \in \mathbb{R}^{T \times d_{model}}$, constituye la representación final de la secuencia de entrada y será utilizada por el decoder (en arquitecturas encoder-decoder) o directamente para tareas de clasificación u otras tareas de comprensión (en arquitecturas solo-encoder como BERT).

**Figura 6.2:** *Diagrama detallado de un bloque encoder del Transformer. La entrada $\mathbf{Z}^{(\ell-1)}$ (representada como una matriz de $T$ vectores de dimensión $d_{model}$) ingresa simultáneamente a la sub-capa de Multi-Head Self-Attention y a una conexión residual (representada como una flecha que rodea la sub-capa). La salida de la self-attention se suma con la entrada original (Add) y se normaliza (Norm), produciendo una representación intermedia. Esta representación alimenta a la sub-capa Feed-Forward Network, que también tiene su propia conexión residual. La salida de la FFN se suma con su entrada (Add) y se normaliza (Norm), produciendo la salida del bloque $\mathbf{Z}^{(\ell)}$. Las conexiones residuales se muestran como flechas curvas que conectan directamente la entrada de cada sub-capa con la operación de suma posterior. Los bloques de normalización de capa se representan como barras horizontales etiquetadas "Layer Norm". Todo el bloque está encerrado en un rectángulo con la etiqueta "$\times N$" indicando que se repite $N$ veces.*

---

## 6.4 El bloque Decoder del Transformer

### 6.4.1 Estructura del decoder

El decoder del Transformer es más complejo que el encoder, ya que incorpora una sub-capa adicional para atender a la salida del encoder. Cada bloque decoder consta de tres sub-capas, cada una con su propia conexión residual y normalización:

1. **Masked Multi-Head Self-Attention** (self-attention enmascarada)
2. **Multi-Head Encoder-Decoder Attention** (atención cruzada)
3. **Feed-Forward Network** (red feed-forward, idéntica en estructura a la del encoder)

El flujo de datos a través de un bloque decoder es:

$$\mathbf{m}^{(\ell)} = \text{LN}\left(\mathbf{Y}^{(\ell-1)} + \text{MaskedMHSA}\left(\mathbf{Y}^{(\ell-1)}\right)\right)$$

$$\mathbf{c}^{(\ell)} = \text{LN}\left(\mathbf{m}^{(\ell)} + \text{MHCA}\left(\mathbf{m}^{(\ell)}, \mathbf{Z}^{(N)}\right)\right)$$

$$\mathbf{Y}^{(\ell)} = \text{LN}\left(\mathbf{c}^{(\ell)} + \text{FFN}\left(\mathbf{c}^{(\ell)}\right)\right)$$

donde $\mathbf{Y}^{(\ell-1)}$ es la entrada al bloque decoder $\ell$, $\mathbf{Z}^{(N)}$ es la salida del último bloque encoder, $\text{MHCA}$ denota la atención cruzada multi-cabezal (*Multi-Head Cross-Attention*), $\mathbf{m}^{(\ell)}$ es la representación intermedia después de la self-attention enmascarada, y $\mathbf{c}^{(\ell)}$ es la representación después de la atención cruzada.

### 6.4.2 Máscara causal (*Causal Mask*)

La diferencia fundamental entre la self-attention del encoder y la del decoder es la *máscara causal*. Durante la generación de secuencias, el decoder produce un token a la vez, de izquierda a derecha. Al generar el token en la posición $t$, el modelo solo debería tener acceso a los tokens que ya se han generado (posiciones $1, 2, \ldots, t-1$), pero no a los tokens futuros (posiciones $t+1, t+2, \ldots$). Permitir que el decoder "vea" los tokens futuros durante el entrenamiento constituiría una fuga de información (*information leakage*) que haría inútil el modelo para generación.

La máscara causal se implementa modificando los puntajes de atención antes de aplicar la función softmax. Definimos una matriz de máscara $\mathbf{M} \in \mathbb{R}^{T \times T}$ de la siguiente forma:

$$M_{ij} = \begin{cases} 0 & \text{si } j \leq i \\ -\infty & \text{si } j > i \end{cases}$$

Esta es una matriz triangular superior (excluyendo la diagonal) con valores $-\infty$. La atención enmascarada se calcula como:

$$\text{MaskedAttention}(\mathbf{Q}, \mathbf{K}, \mathbf{V}) = \text{softmax}\left(\frac{\mathbf{Q}\mathbf{K}^\top}{\sqrt{d_k}} + \mathbf{M}\right)\mathbf{V}$$

La adición de $-\infty$ en las posiciones correspondientes a tokens futuros tiene un efecto crucial: al aplicar la función softmax, $e^{-\infty} = 0$, por lo que los pesos de atención para las posiciones futuras se anulan completamente. Veamos un ejemplo concreto para una secuencia de longitud $T = 4$. La matriz de puntajes brutos (antes de la máscara) podría ser:

$$\frac{\mathbf{Q}\mathbf{K}^\top}{\sqrt{d_k}} = \begin{bmatrix} s_{11} & s_{12} & s_{13} & s_{14} \\ s_{21} & s_{22} & s_{23} & s_{24} \\ s_{31} & s_{32} & s_{33} & s_{34} \\ s_{41} & s_{42} & s_{43} & s_{44} \end{bmatrix}$$

Después de aplicar la máscara:

$$\frac{\mathbf{Q}\mathbf{K}^\top}{\sqrt{d_k}} + \mathbf{M} = \begin{bmatrix} s_{11} & -\infty & -\infty & -\infty \\ s_{21} & s_{22} & -\infty & -\infty \\ s_{31} & s_{32} & s_{33} & -\infty \\ s_{41} & s_{42} & s_{43} & s_{44} \end{bmatrix}$$

Y después de softmax (aplicado fila por fila):

$$\text{softmax}\left(\frac{\mathbf{Q}\mathbf{K}^\top}{\sqrt{d_k}} + \mathbf{M}\right) = \begin{bmatrix} 1 & 0 & 0 & 0 \\ \alpha_{21} & \alpha_{22} & 0 & 0 \\ \alpha_{31} & \alpha_{32} & \alpha_{33} & 0 \\ \alpha_{41} & \alpha_{42} & \alpha_{43} & \alpha_{44} \end{bmatrix}$$

donde $\alpha_{ij} > 0$ y $\sum_j \alpha_{ij} = 1$ para cada fila $i$. Observemos que:

- El token en la posición 1 solo puede atender a sí mismo (toda la distribución se concentra en la posición 1).
- El token en la posición 2 puede atender a las posiciones 1 y 2.
- El token en la posición 3 puede atender a las posiciones 1, 2 y 3.
- El token en la posición 4 puede atender a todas las posiciones.

Esta estructura triangular inferior garantiza la propiedad *autoregresiva*: la predicción del token $t$ depende únicamente de los tokens anteriores, lo cual es esencial para la generación secuencial de texto.

### 6.4.3 Atención Encoder-Decoder (*Cross-Attention*)

La segunda sub-capa del decoder, la *atención cruzada* o *encoder-decoder attention*, es el mecanismo que permite al decoder acceder a la información codificada por el encoder. En esta sub-capa:

- Las **consultas** ($\mathbf{Q}$) provienen de la salida de la sub-capa anterior del decoder (la self-attention enmascarada).
- Las **claves** ($\mathbf{K}$) y los **valores** ($\mathbf{V}$) provienen de la salida del último bloque encoder.

Formalmente:

$$\mathbf{Q} = \mathbf{m}^{(\ell)} \mathbf{W}^Q_{\text{cross}}, \quad \mathbf{K} = \mathbf{Z}^{(N)} \mathbf{W}^K_{\text{cross}}, \quad \mathbf{V} = \mathbf{Z}^{(N)} \mathbf{W}^V_{\text{cross}}$$

donde $\mathbf{m}^{(\ell)} \in \mathbb{R}^{T_{\text{target}} \times d_{model}}$ es la salida de la self-attention enmascarada del decoder y $\mathbf{Z}^{(N)} \in \mathbb{R}^{T_{\text{source}} \times d_{model}}$ es la salida del encoder.

La atención cruzada no utiliza máscara causal, ya que cada posición del decoder puede (y debe) atender a todas las posiciones de la secuencia de entrada. La matriz de atención resultante tiene dimensiones $T_{\text{target}} \times T_{\text{source}}$, donde cada fila indica cómo una posición del decoder distribuye su atención sobre las posiciones de la secuencia de entrada.

Este mecanismo es análogo al mecanismo de atención de Bahdanau utilizado en las arquitecturas encoder-decoder basadas en RNN, pero con la diferencia crucial de que aquí se emplea atención multi-cabezal con múltiples proyecciones aprendidas, lo que permite al modelo capturar diferentes tipos de relaciones entre la fuente y el objetivo simultáneamente.

La atención cruzada es particularmente importante en tareas como la traducción automática, donde el decoder necesita saber qué partes de la oración fuente son relevantes para generar cada palabra de la oración objetivo. En el contexto de las comunicaciones semánticas, la atención cruzada permite que el receptor (decoder) acceda a las representaciones codificadas del transmisor (encoder) para reconstruir o interpretar el mensaje original.

### 6.4.4 Feed-Forward Network del decoder

La tercera sub-capa del decoder es una red feed-forward idéntica en estructura a la del encoder:

$$\text{FFN}(\mathbf{x}) = \max(0, \mathbf{x}\mathbf{W}_1 + \mathbf{b}_1)\mathbf{W}_2 + \mathbf{b}_2$$

Al igual que en el encoder, esta red se aplica posición por posición de manera independiente, con los mismos hiperparámetros ($d_{model}$ y $d_{ff}$). Sin embargo, los pesos de la FFN del decoder son distintos de los del encoder: cada bloque decoder tiene sus propios parámetros independientes.

**Figura 6.3:** *Diagrama detallado de un bloque decoder del Transformer. La entrada $\mathbf{Y}^{(\ell-1)}$ (los embeddings de la secuencia objetivo, desplazados una posición) ingresa a la primera sub-capa: Masked Multi-Head Self-Attention, donde la máscara causal impide que las posiciones atiendan a tokens futuros (representada visualmente como una matriz triangular inferior). La salida se suma con la entrada (Add) y se normaliza (Norm). La representación resultante alimenta la segunda sub-capa: Multi-Head Encoder-Decoder Attention, donde las consultas provienen del decoder y las claves/valores provienen de la salida del encoder $\mathbf{Z}^{(N)}$ (mostrada como una flecha que ingresa desde la izquierda, procedente del encoder). Nuevamente se aplica Add & Norm. Finalmente, la tercera sub-capa es la Feed-Forward Network, seguida de Add & Norm, produciendo la salida $\mathbf{Y}^{(\ell)}$. Las tres conexiones residuales se muestran como flechas que bordean cada sub-capa. El bloque completo está etiquetado "$\times N$" para indicar su repetición.*

---

## 6.5 La arquitectura completa Encoder-Decoder

### 6.5.1 Pipeline completo

La arquitectura completa del Transformer combina las pilas de encoder y decoder en un flujo de procesamiento de extremo a extremo para tareas de secuencia a secuencia (*sequence-to-sequence*). El pipeline completo es el siguiente:

**Lado del encoder:**
1. La secuencia de entrada $(x_1, x_2, \ldots, x_{T_s})$ se convierte en embeddings mediante una capa de embedding compartida o dedicada.
2. Se suman las codificaciones posicionales: $\mathbf{z}_t^{(0)} = \sqrt{d_{model}} \cdot \text{Embed}(x_t) + \mathbf{PE}_t$.
3. Los vectores resultantes pasan a través de la pila de $N$ bloques encoder: $\mathbf{Z}^{(0)} \rightarrow \mathbf{Z}^{(1)} \rightarrow \cdots \rightarrow \mathbf{Z}^{(N)}$.
4. La salida del encoder $\mathbf{Z}^{(N)} \in \mathbb{R}^{T_s \times d_{model}}$ contiene las representaciones contextualizadas de la secuencia fuente.

**Lado del decoder:**
1. La secuencia objetivo $(y_1, y_2, \ldots, y_{T_t})$ se desplaza una posición a la derecha, insertando un token especial de inicio $\langle \text{SOS} \rangle$ al principio: $(\langle \text{SOS} \rangle, y_1, y_2, \ldots, y_{T_t-1})$.
2. Se aplican embeddings y codificaciones posicionales de manera análoga al encoder.
3. Los vectores pasan a través de la pila de $N$ bloques decoder, donde cada bloque recibe la salida del encoder $\mathbf{Z}^{(N)}$ a través de las capas de atención cruzada.
4. La salida del decoder $\mathbf{Y}^{(N)} \in \mathbb{R}^{T_t \times d_{model}}$ contiene las representaciones del objetivo.

**Capa de salida:**
1. Se aplica una transformación lineal: $\mathbf{logits} = \mathbf{Y}^{(N)} \mathbf{W}_{\text{out}} + \mathbf{b}_{\text{out}}$, donde $\mathbf{W}_{\text{out}} \in \mathbb{R}^{d_{model} \times V}$ y $V$ es el tamaño del vocabulario.
2. Se aplica softmax para obtener las probabilidades sobre el vocabulario: $P(y_t | y_{<t}, \mathbf{X}) = \text{softmax}(\mathbf{logits}_t)$.

Formalmente, el Transformer completo modela la distribución condicional:

$$P(y_1, y_2, \ldots, y_{T_t} | x_1, x_2, \ldots, x_{T_s}) = \prod_{t=1}^{T_t} P(y_t | y_1, \ldots, y_{t-1}, x_1, \ldots, x_{T_s})$$

La factorización autoregresiva del lado derecho es lo que permite la generación token por token durante la inferencia.

### 6.5.2 Parámetros del modelo base

El Transformer original se presentó en dos configuraciones:

**Modelo base (*Transformer Base*):**

| Hiperparámetro | Símbolo | Valor |
|---|---|---|
| Dimensión del modelo | $d_{model}$ | 512 |
| Número de cabezas de atención | $h$ | 8 |
| Número de capas (encoder y decoder) | $N$ | 6 |
| Dimensión de la capa oculta FFN | $d_{ff}$ | 2048 |
| Dimensión de consultas y claves | $d_k$ | 64 |
| Dimensión de valores | $d_v$ | 64 |
| Dropout | $p_{drop}$ | 0.1 |

**Modelo grande (*Transformer Big*):**

| Hiperparámetro | Símbolo | Valor |
|---|---|---|
| Dimensión del modelo | $d_{model}$ | 1024 |
| Número de cabezas de atención | $h$ | 16 |
| Número de capas (encoder y decoder) | $N$ | 6 |
| Dimensión de la capa oculta FFN | $d_{ff}$ | 4096 |
| Dimensión de consultas y claves | $d_k$ | 64 |
| Dimensión de valores | $d_v$ | 64 |
| Dropout | $p_{drop}$ | 0.3 |

Nótese que en ambos modelos se cumple que $d_k = d_v = d_{model} / h$. Esta relación asegura que el costo computacional de la atención multi-cabezal sea comparable al de una atención de una sola cabeza con la dimensión completa $d_{model}$.

El número total de parámetros del modelo base es aproximadamente 65 millones, distribuidos entre las capas de embedding, las matrices de proyección de la atención, los pesos de las FFN y los parámetros de normalización. Para el modelo grande, el número de parámetros asciende a aproximadamente 213 millones.

### 6.5.3 Complejidad computacional

Es instructivo analizar la complejidad computacional de las operaciones principales del Transformer. Para una secuencia de longitud $T$:

- **Self-Attention**: La multiplicación $\mathbf{Q}\mathbf{K}^\top$ tiene complejidad $O(T^2 \cdot d_k)$, y la multiplicación del resultado con $\mathbf{V}$ tiene complejidad $O(T^2 \cdot d_v)$. La complejidad total es $O(T^2 \cdot d_{model})$, que es cuadrática en la longitud de la secuencia.
- **FFN posición por posición**: Tiene complejidad $O(T \cdot d_{model} \cdot d_{ff})$, que es lineal en la longitud de la secuencia.
- **RNN (para comparación)**: Tiene complejidad $O(T \cdot d_{model}^2)$ por capa, también lineal en $T$ pero con una constante mayor.

La complejidad cuadrática de la self-attention con respecto a $T$ es la principal limitación del Transformer para secuencias muy largas, y ha motivado una línea activa de investigación en variantes eficientes como Linformer, Performer, o los mecanismos de atención local/dispersa (*sparse attention*).

Sin embargo, para secuencias de longitud moderada (hasta unos pocos miles de tokens), la ventaja del Transformer reside en su *longitud de camino máxima* constante $O(1)$ entre cualquier par de posiciones (frente a $O(T)$ en RNN y $O(\log T)$ en redes convolucionales), lo que facilita el aprendizaje de dependencias a largo alcance.

**Figura 6.4:** *Arquitectura completa del Transformer tal como se presenta en el artículo original. En el lado izquierdo se muestra el encoder: la secuencia de entrada pasa por la capa de embeddings (rectángulo inferior), a la que se suman las codificaciones posicionales (representadas por ondas sinusoidales). Los vectores resultantes ingresan a una pila de $N=6$ bloques encoder idénticos (representados como un rectángulo grande con la etiqueta "$\times N$"), cada uno con sus sub-capas de Multi-Head Attention y Feed Forward con conexiones Add & Norm. En el lado derecho se muestra el decoder: la secuencia objetivo (desplazada a la derecha) pasa igualmente por embeddings y codificaciones posicionales, e ingresa a una pila de $N=6$ bloques decoder, cada uno con Masked Multi-Head Attention, atención cruzada (con flechas que conectan desde la salida del encoder) y Feed Forward, todas con Add & Norm. La salida del último bloque decoder pasa por una capa lineal y softmax para producir las probabilidades de salida. Las flechas entre el encoder y el decoder representan el flujo de las claves y valores del encoder hacia las capas de atención cruzada del decoder.*

---

## 6.6 Entrenamiento del Transformer

### 6.6.1 Teacher Forcing

El entrenamiento del Transformer para tareas de generación de secuencias utiliza una técnica llamada *teacher forcing* (forzamiento por el profesor). En lugar de alimentar al decoder con sus propias predicciones (lo que introduciría un problema de retroalimentación y haría el entrenamiento más lento e inestable), durante el entrenamiento se le proporciona la secuencia objetivo correcta (*ground truth*) como entrada.

Concretamente, si la secuencia objetivo es $(y_1, y_2, \ldots, y_{T_t})$, la entrada al decoder es la secuencia desplazada $(\langle \text{SOS} \rangle, y_1, y_2, \ldots, y_{T_t-1})$, y se espera que la salida prediga $(y_1, y_2, \ldots, y_{T_t})$. Es decir, en cada posición $t$, el decoder recibe los tokens correctos en las posiciones $1, \ldots, t-1$ y debe predecir $y_t$.

La máscara causal garantiza que, aunque todos los tokens correctos están presentes en la entrada, la posición $t$ solo puede ver los tokens en las posiciones $1, \ldots, t-1$. Esto simula las condiciones de inferencia, donde los tokens futuros no están disponibles, pero permite que todas las posiciones se procesen en paralelo durante el entrenamiento.

El *teacher forcing* tiene la ventaja de acelerar significativamente el entrenamiento al proporcionar una señal de supervisión clara en cada posición. Sin embargo, puede crear una discrepancia entre el entrenamiento (donde las entradas siempre son correctas) y la inferencia (donde las entradas pueden contener errores de predicciones anteriores). Esta discrepancia, conocida como *exposure bias* (sesgo de exposición), puede mitigarse parcialmente con técnicas como el *scheduled sampling*, donde gradualmente se reemplazan algunas entradas correctas por predicciones del modelo durante el entrenamiento.

### 6.6.2 Función de pérdida: Entropía cruzada

El objetivo del entrenamiento es minimizar la *entropía cruzada* (*cross-entropy loss*) entre la distribución de probabilidad predicha y la distribución real (one-hot) sobre el vocabulario. Para una secuencia objetivo $(y_1, y_2, \ldots, y_{T_t})$, la pérdida se define como:

$$\mathcal{L} = -\frac{1}{T_t} \sum_{t=1}^{T_t} \log P(y_t | y_{<t}, \mathbf{X})$$

donde $P(y_t | y_{<t}, \mathbf{X})$ es la probabilidad asignada por el modelo al token correcto $y_t$ en la posición $t$, dada la secuencia de entrada $\mathbf{X}$ y los tokens objetivo anteriores $y_{<t} = (y_1, \ldots, y_{t-1})$.

Equivalentemente, si $\hat{\mathbf{p}}_t \in \mathbb{R}^V$ es el vector de probabilidades predicho por el modelo (después de softmax) y $\mathbf{y}_t \in \mathbb{R}^V$ es la representación one-hot del token objetivo, entonces:

$$\mathcal{L} = -\frac{1}{T_t} \sum_{t=1}^{T_t} \mathbf{y}_t^\top \log \hat{\mathbf{p}}_t = -\frac{1}{T_t} \sum_{t=1}^{T_t} \log \hat{p}_{t, y_t}$$

Minimizar esta pérdida es equivalente a maximizar la verosimilitud (*likelihood*) de la secuencia objetivo dado el modelo, es decir, maximizar:

$$\prod_{t=1}^{T_t} P(y_t | y_{<t}, \mathbf{X})$$

### 6.6.3 Suavizado de etiquetas (*Label Smoothing*)

El Transformer original utiliza *label smoothing* con un parámetro $\epsilon_{ls} = 0.1$. En lugar de usar distribuciones one-hot puras para los tokens objetivo, se suaviza la distribución asignando una pequeña probabilidad a todos los tokens del vocabulario:

$$q(y_t = k) = \begin{cases} 1 - \epsilon_{ls} & \text{si } k = y_t^* \text{ (token correcto)} \\ \frac{\epsilon_{ls}}{V - 1} & \text{en caso contrario} \end{cases}$$

donde $y_t^*$ es el token objetivo correcto y $V$ es el tamaño del vocabulario. La pérdida con label smoothing se calcula entonces como la divergencia KL entre esta distribución suavizada $q$ y la distribución predicha $\hat{p}$:

$$\mathcal{L}_{ls} = -\sum_{k=1}^{V} q(y_t = k) \log \hat{p}_{t,k}$$

El label smoothing tiene varios beneficios:

1. **Previene sobreconfianza.** Sin suavizado, el modelo tiende a asignar probabilidades muy cercanas a 1 para el token correcto, lo cual puede llevar a gradientes extremadamente pequeños y reducir la capacidad del modelo para seguir aprendiendo.
2. **Actúa como regularizador.** Al penalizar distribuciones muy concentradas, el label smoothing fomenta que el modelo produzca distribuciones más calibradas.
3. **Mejora la generalización.** Aunque el label smoothing reduce ligeramente la perplejidad en el conjunto de entrenamiento, típicamente mejora las métricas de evaluación como BLEU en el conjunto de prueba.

### 6.6.4 Esquema de tasa de aprendizaje con calentamiento (*Warm-up*)

El Transformer utiliza un esquema de tasa de aprendizaje no estándar que combina una fase de calentamiento lineal con una fase de decaimiento proporcional al inverso de la raíz cuadrada del número de pasos. La fórmula es:

$$lr = d_{model}^{-0.5} \cdot \min\left(step^{-0.5}, \ step \cdot warmup\_steps^{-1.5}\right)$$

Analicemos esta fórmula en detalle:

- **Fase de calentamiento** ($step \leq warmup\_steps$): cuando $step$ es pequeño, $step \cdot warmup\_steps^{-1.5} < step^{-0.5}$, por lo que $lr = d_{model}^{-0.5} \cdot step \cdot warmup\_steps^{-1.5}$. La tasa de aprendizaje crece *linealmente* con el número de pasos, desde un valor cercano a cero hasta su máximo. Con $warmup\_steps = 4000$ (el valor usado en el artículo original), el máximo se alcanza en el paso 4000.

- **Fase de decaimiento** ($step > warmup\_steps$): cuando $step$ es grande, $step^{-0.5} < step \cdot warmup\_steps^{-1.5}$, por lo que $lr = d_{model}^{-0.5} \cdot step^{-0.5}$. La tasa de aprendizaje decrece proporcionalmente a $1/\sqrt{step}$, lo que corresponde a un decaimiento suave.

- **Valor máximo**: el máximo de la tasa de aprendizaje se alcanza cuando $step = warmup\_steps$, y su valor es $lr_{\max} = d_{model}^{-0.5} \cdot warmup\_steps^{-0.5}$. Para $d_{model} = 512$ y $warmup\_steps = 4000$, esto da $lr_{\max} = \frac{1}{\sqrt{512} \cdot \sqrt{4000}} \approx \frac{1}{22.63 \times 63.25} \approx 6.99 \times 10^{-4}$.

El factor $d_{model}^{-0.5}$ ajusta la tasa de aprendizaje según el tamaño del modelo: modelos más grandes tienen tasas de aprendizaje más pequeñas, lo cual es consistente con la observación empírica de que los gradientes tienden a ser más grandes en modelos con mayor dimensionalidad.

La fase de calentamiento es crucial para la estabilidad del entrenamiento. Al inicio del entrenamiento, las representaciones del modelo están esencialmente aleatorias, y los gradientes pueden ser ruidosos y de gran magnitud. Comenzar con una tasa de aprendizaje pequeña permite que el modelo se "estabilice" gradualmente antes de aplicar actualizaciones más agresivas. Sin el calentamiento, el entrenamiento del Transformer tiende a ser inestable y puede divergir.

El optimizador utilizado es Adam (Kingma & Ba, 2015), con parámetros $\beta_1 = 0.9$, $\beta_2 = 0.98$ y $\epsilon = 10^{-9}$.

> **Referencia:** Kingma, D. P., & Ba, J. (2015). Adam: A method for stochastic optimization. *Proceedings of the 3rd International Conference on Learning Representations (ICLR)*. (DOI: 10.48550/arXiv.1412.6980)

### 6.6.5 Regularización

Además del label smoothing, el Transformer original emplea las siguientes técnicas de regularización:

1. **Dropout.** Se aplica dropout con probabilidad $p_{drop} = 0.1$ (modelo base) o $p_{drop} = 0.3$ (modelo grande) a:
   - Las salidas de cada sub-capa, antes de la conexión residual.
   - Los pesos de atención (después de softmax).
   - Las codificaciones posicionales sumadas a los embeddings.

2. **Compartición de pesos.** En el modelo original, la matriz de embeddings de entrada del encoder, la matriz de embeddings de entrada del decoder y la matriz de proyección de salida antes del softmax comparten los mismos pesos (transpuestos para la capa de salida). Esto reduce el número total de parámetros y proporciona una regularización implícita al vincular las representaciones de entrada y salida.

---

## 6.7 Variantes de Transformers

Desde la publicación del Transformer original, la arquitectura ha dado lugar a una familia diversa de modelos que se han convertido en la base del aprendizaje profundo moderno. Las tres principales variantes arquitectónicas se distinguen por qué componentes del Transformer original utilizan.

### 6.7.1 Modelos solo-encoder: BERT

BERT (*Bidirectional Encoder Representations from Transformers*), desarrollado por Devlin et al. (2019) en Google, utiliza únicamente la pila de encoder del Transformer. La idea central de BERT es pre-entrenar representaciones bidireccionales profundas a partir de texto no etiquetado, condicionando cada token en su contexto tanto izquierdo como derecho.

**Características clave:**
- **Bidireccionalidad completa:** A diferencia de los modelos autoregresivos que solo procesan el contexto izquierdo (o derecho), BERT utiliza self-attention sin máscara causal, permitiendo que cada token atienda a todos los demás tokens de la secuencia. Esto es posible porque BERT no genera texto, sino que produce representaciones para tareas de comprensión.
- **Pre-entrenamiento con Masked Language Modeling (MLM):** Durante el pre-entrenamiento, se enmascara aleatoriamente el 15% de los tokens de entrada (reemplazándolos por un token especial `[MASK]`) y el modelo debe predecir los tokens originales. Esto obliga al modelo a desarrollar representaciones contextuales ricas.
- **Pre-entrenamiento con Next Sentence Prediction (NSP):** El modelo también aprende a predecir si dos oraciones son consecutivas en el texto original.
- **Fine-tuning:** Después del pre-entrenamiento, BERT se ajusta finamente (*fine-tuning*) en tareas específicas como clasificación de texto, respuesta a preguntas o reconocimiento de entidades nombradas, añadiendo una capa de salida simple.

BERT-base tiene 12 capas, $d_{model} = 768$ y 12 cabezas de atención (110M parámetros), mientras que BERT-large tiene 24 capas, $d_{model} = 1024$ y 16 cabezas (340M parámetros).

> **Referencia:** Devlin, J., Chang, M.-W., Lee, K., & Toutanova, K. (2019). BERT: Pre-training of deep bidirectional transformers for language understanding. *Proceedings of NAACL-HLT*, 4171-4186. (DOI: 10.18653/v1/N19-1423)

### 6.7.2 Modelos solo-decoder: GPT

La familia GPT (*Generative Pre-trained Transformer*), desarrollada por OpenAI, utiliza únicamente la pila de decoder del Transformer (sin atención cruzada, ya que no hay encoder). Estos modelos son *autoregresivos*: generan texto un token a la vez, condicionando cada token en todos los tokens anteriores.

**Características clave:**
- **Atención causal (unidireccional):** Se utiliza la máscara causal para que cada posición solo pueda atender a las posiciones anteriores, lo cual es necesario para la generación secuencial.
- **Pre-entrenamiento con modelado de lenguaje:** El objetivo del pre-entrenamiento es predecir el siguiente token dado los tokens anteriores: $P(x_t | x_1, \ldots, x_{t-1})$. Este objetivo es más simple que el MLM de BERT y se entrena con la pérdida de entropía cruzada estándar.
- **Escalabilidad:** La familia GPT ha demostrado que aumentar el tamaño del modelo y la cantidad de datos de entrenamiento mejora consistentemente el rendimiento (*scaling laws*). GPT-2 tiene 1.5 mil millones de parámetros, GPT-3 tiene 175 mil millones, y modelos posteriores son aún mayores.
- **Aprendizaje en contexto (*In-context Learning*):** Los modelos GPT grandes pueden realizar tareas sin necesidad de fine-tuning, simplemente proporcionando ejemplos en el *prompt* (pocos disparos o *few-shot learning*).

> **Referencia:** Radford, A., Narasimhan, K., Salimans, T., & Sutskever, I. (2018). Improving language understanding by generative pre-training. *OpenAI technical report*.

### 6.7.3 Modelos Encoder-Decoder: T5

T5 (*Text-to-Text Transfer Transformer*), desarrollado por Raffel et al. (2020) en Google, utiliza la arquitectura encoder-decoder completa del Transformer original. La innovación principal de T5 es reformular *todas* las tareas de NLP como problemas de texto a texto: la entrada es una cadena de texto y la salida es otra cadena de texto.

**Características clave:**
- **Formato unificado:** Tareas como clasificación, resumen, traducción, respuesta a preguntas, y análisis de sentimiento se expresan todas como transformaciones de texto a texto, precedidas por un prefijo que indica la tarea (por ejemplo, "translate English to German: ...").
- **Pre-entrenamiento con span corruption:** Similar al MLM de BERT, pero en lugar de enmascarar tokens individuales, se enmascaran *spans* (secuencias contiguas) de tokens, y el decoder genera los spans faltantes.
- **Estudio exhaustivo:** El artículo de T5 realizó un estudio comparativo sistemático de diferentes arquitecturas, objetivos de pre-entrenamiento, conjuntos de datos y estrategias de transferencia, proporcionando insights valiosos para la comunidad.

> **Referencia:** Raffel, C., Shazeer, N., Roberts, A., Lee, K., Narang, S., Matena, M., Zhou, Y., Li, W., & Liu, P. J. (2020). Exploring the limits of transfer learning with a unified text-to-text transformer. *Journal of Machine Learning Research*, 21(140), 1-67. (DOI: 10.5555/3455716.3455856)

### 6.7.4 Vision Transformer (ViT)

El Vision Transformer (ViT), propuesto por Dosovitskiy et al. (2021), demostró que la arquitectura Transformer puede aplicarse directamente a imágenes, rompiendo el dominio de las redes convolucionales (CNN) en visión por computadora.

**Funcionamiento:**
1. La imagen de entrada de dimensiones $H \times W \times C$ se divide en parches (*patches*) no superpuestos de tamaño $P \times P$.
2. Cada parche se aplana y se proyecta linealmente a un vector de dimensión $d_{model}$, creando una secuencia de $N = HW/P^2$ "tokens de imagen".
3. Se añade un token especial `[CLS]` al inicio de la secuencia, cuya representación final se usa para clasificación.
4. Se suman codificaciones posicionales aprendidas (en lugar de sinusoidales).
5. La secuencia resultante se procesa con un encoder Transformer estándar.
6. La representación del token `[CLS]` en la última capa se usa para clasificación.

ViT demostró que, con suficientes datos de pre-entrenamiento (como JFT-300M o ImageNet-21k), los Transformers pueden igualar o superar a las CNN más avanzadas, con la ventaja de una mayor flexibilidad y escalabilidad. Este resultado ha tenido un impacto profundo en la visión por computadora y ha inspirado numerosas extensiones, incluidas las que son relevantes para la codificación de imágenes y video en comunicaciones semánticas.

> **Referencia:** Dosovitskiy, A., Beyer, L., Kolesnikov, A., Weissenborn, D., Zhai, X., Unterthiner, T., Dehghani, M., Minderer, M., Heigold, G., Gelly, S., Uszkoreit, J., & Houlsby, N. (2021). An image is worth 16x16 words: Transformers for image recognition at scale. *Proceedings of the 9th International Conference on Learning Representations (ICLR)*. (DOI: 10.48550/arXiv.2010.11929)

### 6.7.5 Resumen comparativo

| Variante | Componentes | Atención | Tarea típica | Ejemplo |
|---|---|---|---|---|
| Solo-Encoder | Encoder | Bidireccional | Comprensión | BERT, RoBERTa |
| Solo-Decoder | Decoder | Causal (unidireccional) | Generación | GPT, LLaMA |
| Encoder-Decoder | Ambos | Bidireccional + Causal + Cruzada | Seq2Seq | T5, BART, Transformer original |
| ViT | Encoder | Bidireccional | Clasificación de imágenes | ViT, DeiT |

---

## 6.8 Implementación en PyTorch

### 6.8.1 Codificación posicional

A continuación, presentamos una implementación completa y comentada de la codificación posicional sinusoidal en PyTorch:

```python
import torch
import torch.nn as nn
import math

class PositionalEncoding(nn.Module):
    """
    Codificación posicional sinusoidal según Vaswani et al. (2017).
    Genera vectores de posición fijos basados en funciones seno y coseno
    de diferentes frecuencias, que se suman a los embeddings de entrada.
    """
    def __init__(self, d_model: int, max_len: int = 5000, dropout: float = 0.1):
        """
        Args:
            d_model: Dimensión del modelo (debe ser par).
            max_len: Longitud máxima de secuencia soportada.
            dropout: Probabilidad de dropout aplicada después de sumar PE.
        """
        super().__init__()
        self.dropout = nn.Dropout(p=dropout)

        # Crear matriz de codificación posicional [max_len, d_model]
        pe = torch.zeros(max_len, d_model)

        # Vector de posiciones: [0, 1, 2, ..., max_len-1], shape [max_len, 1]
        position = torch.arange(0, max_len, dtype=torch.float).unsqueeze(1)

        # Término de división para las frecuencias geométricas.
        # exp(-2i * log(10000) / d_model) = 1 / 10000^(2i/d_model)
        div_term = torch.exp(
            torch.arange(0, d_model, 2).float() * (-math.log(10000.0) / d_model)
        )

        # Dimensiones pares: seno
        pe[:, 0::2] = torch.sin(position * div_term)
        # Dimensiones impares: coseno
        pe[:, 1::2] = torch.cos(position * div_term)

        # Añadir dimensión de batch: [1, max_len, d_model]
        pe = pe.unsqueeze(0)

        # Registrar como buffer (no es un parámetro entrenable)
        self.register_buffer('pe', pe)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Args:
            x: Tensor de embeddings [batch_size, seq_len, d_model]
        Returns:
            Embeddings con codificación posicional sumada [batch_size, seq_len, d_model]
        """
        # Sumar codificación posicional (broadcasting sobre batch)
        x = x + self.pe[:, :x.size(1), :]
        return self.dropout(x)
```

Observemos que la codificación posicional se registra como un *buffer* (no como un parámetro), lo que significa que se guarda con el modelo pero no se actualiza durante el entrenamiento. El cálculo del `div_term` utiliza la identidad $10000^{-2i/d_{model}} = e^{-2i \cdot \ln(10000) / d_{model}}$, que es numéricamente más estable que calcular la potencia directamente.

### 6.8.2 Bloque Transformer (Encoder)

Implementamos ahora un bloque encoder completo del Transformer:

```python
class MultiHeadAttention(nn.Module):
    """
    Atención multi-cabezal escalada por producto punto.
    Implementa h cabezas de atención en paralelo.
    """
    def __init__(self, d_model: int, num_heads: int, dropout: float = 0.1):
        super().__init__()
        assert d_model % num_heads == 0, "d_model debe ser divisible por num_heads"

        self.d_model = d_model
        self.num_heads = num_heads
        self.d_k = d_model // num_heads  # Dimensión por cabeza

        # Proyecciones lineales para Q, K, V y salida
        self.W_q = nn.Linear(d_model, d_model)  # Proyecta a [batch, seq, d_model]
        self.W_k = nn.Linear(d_model, d_model)
        self.W_v = nn.Linear(d_model, d_model)
        self.W_o = nn.Linear(d_model, d_model)  # Proyección de salida

        self.dropout = nn.Dropout(p=dropout)

    def scaled_dot_product_attention(
        self, Q: torch.Tensor, K: torch.Tensor, V: torch.Tensor,
        mask: torch.Tensor = None
    ) -> torch.Tensor:
        """
        Calcula atención escalada por producto punto.
        Args:
            Q: Consultas [batch, heads, seq_q, d_k]
            K: Claves   [batch, heads, seq_k, d_k]
            V: Valores   [batch, heads, seq_k, d_v]
            mask: Máscara opcional [batch, 1, seq_q, seq_k] o [1, 1, seq_q, seq_k]
        Returns:
            Salida de atención [batch, heads, seq_q, d_v]
        """
        # Puntajes de atención: QK^T / sqrt(d_k)
        scores = torch.matmul(Q, K.transpose(-2, -1)) / math.sqrt(self.d_k)

        # Aplicar máscara si se proporciona
        if mask is not None:
            scores = scores.masked_fill(mask == 0, float('-inf'))

        # Softmax sobre la última dimensión (dim de claves)
        attention_weights = torch.softmax(scores, dim=-1)
        attention_weights = self.dropout(attention_weights)

        # Multiplicar por valores
        output = torch.matmul(attention_weights, V)
        return output

    def forward(
        self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor,
        mask: torch.Tensor = None
    ) -> torch.Tensor:
        """
        Args:
            query: [batch, seq_q, d_model]
            key:   [batch, seq_k, d_model]
            value: [batch, seq_k, d_model]
            mask:  Máscara opcional
        Returns:
            Salida [batch, seq_q, d_model]
        """
        batch_size = query.size(0)

        # 1. Proyecciones lineales y reorganización en cabezas
        #    [batch, seq, d_model] -> [batch, seq, num_heads, d_k] -> [batch, num_heads, seq, d_k]
        Q = self.W_q(query).view(batch_size, -1, self.num_heads, self.d_k).transpose(1, 2)
        K = self.W_k(key).view(batch_size, -1, self.num_heads, self.d_k).transpose(1, 2)
        V = self.W_v(value).view(batch_size, -1, self.num_heads, self.d_k).transpose(1, 2)

        # 2. Atención escalada
        attn_output = self.scaled_dot_product_attention(Q, K, V, mask)

        # 3. Concatenar cabezas y proyectar
        #    [batch, num_heads, seq, d_k] -> [batch, seq, d_model]
        attn_output = attn_output.transpose(1, 2).contiguous().view(
            batch_size, -1, self.d_model
        )

        # 4. Proyección de salida
        return self.W_o(attn_output)


class FeedForwardNetwork(nn.Module):
    """
    Red feed-forward posición por posición.
    Dos capas lineales con activación ReLU intermedia.
    """
    def __init__(self, d_model: int, d_ff: int, dropout: float = 0.1):
        super().__init__()
        self.linear1 = nn.Linear(d_model, d_ff)    # Expansión: d_model -> d_ff
        self.linear2 = nn.Linear(d_ff, d_model)    # Compresión: d_ff -> d_model
        self.dropout = nn.Dropout(p=dropout)
        self.relu = nn.ReLU()

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Args:
            x: [batch, seq_len, d_model]
        Returns:
            [batch, seq_len, d_model]
        """
        # FFN(x) = max(0, xW1 + b1)W2 + b2
        return self.linear2(self.dropout(self.relu(self.linear1(x))))


class TransformerEncoderBlock(nn.Module):
    """
    Un bloque encoder del Transformer.
    Contiene: Multi-Head Self-Attention + Add&Norm + FFN + Add&Norm
    """
    def __init__(self, d_model: int, num_heads: int, d_ff: int, dropout: float = 0.1):
        super().__init__()

        # Sub-capa 1: Multi-Head Self-Attention
        self.self_attention = MultiHeadAttention(d_model, num_heads, dropout)
        self.norm1 = nn.LayerNorm(d_model)

        # Sub-capa 2: Feed-Forward Network
        self.feed_forward = FeedForwardNetwork(d_model, d_ff, dropout)
        self.norm2 = nn.LayerNorm(d_model)

        # Dropout para conexiones residuales
        self.dropout = nn.Dropout(p=dropout)

    def forward(self, x: torch.Tensor, mask: torch.Tensor = None) -> torch.Tensor:
        """
        Args:
            x: Entrada [batch, seq_len, d_model]
            mask: Máscara de padding opcional
        Returns:
            Salida [batch, seq_len, d_model]
        """
        # Sub-capa 1: Self-Attention con conexión residual y normalización
        # Post-LN: LN(x + Sublayer(x))
        attn_output = self.self_attention(x, x, x, mask)  # Q=K=V=x (self-attention)
        x = self.norm1(x + self.dropout(attn_output))     # Add & Norm

        # Sub-capa 2: FFN con conexión residual y normalización
        ff_output = self.feed_forward(x)
        x = self.norm2(x + self.dropout(ff_output))        # Add & Norm

        return x
```

### 6.8.3 Apilamiento de bloques: Encoder completo

Los bloques encoder se apilan para formar el encoder completo:

```python
class TransformerEncoder(nn.Module):
    """
    Encoder completo del Transformer: Embedding + PE + N bloques encoder.
    """
    def __init__(
        self, vocab_size: int, d_model: int, num_heads: int,
        d_ff: int, num_layers: int, max_len: int = 5000,
        dropout: float = 0.1
    ):
        super().__init__()

        # Capa de embedding: convierte índices de tokens en vectores densos
        self.embedding = nn.Embedding(vocab_size, d_model)
        self.d_model = d_model

        # Codificación posicional sinusoidal
        self.positional_encoding = PositionalEncoding(d_model, max_len, dropout)

        # Pila de N bloques encoder (cada uno con parámetros independientes)
        self.layers = nn.ModuleList([
            TransformerEncoderBlock(d_model, num_heads, d_ff, dropout)
            for _ in range(num_layers)
        ])

        # Normalización final (opcional, usada en algunas implementaciones)
        self.norm = nn.LayerNorm(d_model)

    def forward(self, src: torch.Tensor, mask: torch.Tensor = None) -> torch.Tensor:
        """
        Args:
            src: Tokens de entrada [batch, seq_len] (índices enteros)
            mask: Máscara de padding [batch, 1, 1, seq_len]
        Returns:
            Representaciones contextualizadas [batch, seq_len, d_model]
        """
        # 1. Embedding con escalado por sqrt(d_model)
        x = self.embedding(src) * math.sqrt(self.d_model)

        # 2. Sumar codificación posicional
        x = self.positional_encoding(x)

        # 3. Pasar por los N bloques encoder secuencialmente
        for layer in self.layers:
            x = layer(x, mask)

        # 4. Normalización final
        return self.norm(x)
```

### 6.8.4 Bloque Decoder

```python
class TransformerDecoderBlock(nn.Module):
    """
    Un bloque decoder del Transformer.
    Contiene: Masked Self-Attention + Add&Norm +
              Cross-Attention + Add&Norm + FFN + Add&Norm
    """
    def __init__(self, d_model: int, num_heads: int, d_ff: int, dropout: float = 0.1):
        super().__init__()

        # Sub-capa 1: Masked Multi-Head Self-Attention
        self.masked_self_attention = MultiHeadAttention(d_model, num_heads, dropout)
        self.norm1 = nn.LayerNorm(d_model)

        # Sub-capa 2: Multi-Head Encoder-Decoder (Cross) Attention
        self.cross_attention = MultiHeadAttention(d_model, num_heads, dropout)
        self.norm2 = nn.LayerNorm(d_model)

        # Sub-capa 3: Feed-Forward Network
        self.feed_forward = FeedForwardNetwork(d_model, d_ff, dropout)
        self.norm3 = nn.LayerNorm(d_model)

        self.dropout = nn.Dropout(p=dropout)

    def forward(
        self, x: torch.Tensor, encoder_output: torch.Tensor,
        src_mask: torch.Tensor = None, tgt_mask: torch.Tensor = None
    ) -> torch.Tensor:
        """
        Args:
            x: Entrada del decoder [batch, tgt_len, d_model]
            encoder_output: Salida del encoder [batch, src_len, d_model]
            src_mask: Máscara para la secuencia fuente (padding)
            tgt_mask: Máscara causal para la secuencia objetivo
        Returns:
            Salida [batch, tgt_len, d_model]
        """
        # Sub-capa 1: Masked Self-Attention (Q=K=V provienen del decoder)
        attn_output = self.masked_self_attention(x, x, x, tgt_mask)
        x = self.norm1(x + self.dropout(attn_output))

        # Sub-capa 2: Cross-Attention (Q del decoder, K y V del encoder)
        cross_output = self.cross_attention(x, encoder_output, encoder_output, src_mask)
        x = self.norm2(x + self.dropout(cross_output))

        # Sub-capa 3: Feed-Forward Network
        ff_output = self.feed_forward(x)
        x = self.norm3(x + self.dropout(ff_output))

        return x
```

### 6.8.5 Generación de la máscara causal

Una función auxiliar esencial es la creación de la máscara causal:

```python
def generate_causal_mask(size: int) -> torch.Tensor:
    """
    Genera una máscara causal (triangular inferior) para el decoder.
    Las posiciones futuras se enmascaran con False (0).

    Args:
        size: Longitud de la secuencia objetivo
    Returns:
        Máscara booleana [1, 1, size, size] donde True = posición permitida
    """
    # torch.tril: triangular inferior (incluye diagonal)
    mask = torch.tril(torch.ones(size, size)).bool()
    return mask.unsqueeze(0).unsqueeze(0)  # [1, 1, size, size]
```

Esta función genera la matriz de máscara descrita en la Sección 6.4.2. Por ejemplo, para `size=4`:

```
[[True,  False, False, False],
 [True,  True,  False, False],
 [True,  True,  True,  False],
 [True,  True,  True,  True ]]
```

Las posiciones con `False` recibirán un valor de $-\infty$ en los puntajes de atención, lo que se traduce en un peso de atención de cero después de la softmax.

### 6.8.6 Modelo Transformer completo

Finalmente, la integración de todos los componentes en un modelo Transformer completo para tareas de secuencia a secuencia:

```python
class Transformer(nn.Module):
    """
    Modelo Transformer completo (encoder-decoder) para tareas seq2seq.
    """
    def __init__(
        self, src_vocab_size: int, tgt_vocab_size: int,
        d_model: int = 512, num_heads: int = 8, num_layers: int = 6,
        d_ff: int = 2048, max_len: int = 5000, dropout: float = 0.1
    ):
        super().__init__()

        # Embeddings para fuente y objetivo
        self.src_embedding = nn.Embedding(src_vocab_size, d_model)
        self.tgt_embedding = nn.Embedding(tgt_vocab_size, d_model)
        self.d_model = d_model

        # Codificación posicional (compartida)
        self.positional_encoding = PositionalEncoding(d_model, max_len, dropout)

        # Pila de bloques encoder
        self.encoder_layers = nn.ModuleList([
            TransformerEncoderBlock(d_model, num_heads, d_ff, dropout)
            for _ in range(num_layers)
        ])

        # Pila de bloques decoder
        self.decoder_layers = nn.ModuleList([
            TransformerDecoderBlock(d_model, num_heads, d_ff, dropout)
            for _ in range(num_layers)
        ])

        # Normalizaciones finales
        self.encoder_norm = nn.LayerNorm(d_model)
        self.decoder_norm = nn.LayerNorm(d_model)

        # Capa de salida: proyección al vocabulario objetivo
        self.output_projection = nn.Linear(d_model, tgt_vocab_size)

    def encode(self, src: torch.Tensor, src_mask: torch.Tensor = None) -> torch.Tensor:
        """Procesa la secuencia fuente a través del encoder."""
        x = self.src_embedding(src) * math.sqrt(self.d_model)
        x = self.positional_encoding(x)
        for layer in self.encoder_layers:
            x = layer(x, src_mask)
        return self.encoder_norm(x)

    def decode(
        self, tgt: torch.Tensor, encoder_output: torch.Tensor,
        src_mask: torch.Tensor = None, tgt_mask: torch.Tensor = None
    ) -> torch.Tensor:
        """Procesa la secuencia objetivo a través del decoder."""
        x = self.tgt_embedding(tgt) * math.sqrt(self.d_model)
        x = self.positional_encoding(x)
        for layer in self.decoder_layers:
            x = layer(x, encoder_output, src_mask, tgt_mask)
        return self.decoder_norm(x)

    def forward(
        self, src: torch.Tensor, tgt: torch.Tensor,
        src_mask: torch.Tensor = None, tgt_mask: torch.Tensor = None
    ) -> torch.Tensor:
        """
        Forward pass completo del Transformer.
        Args:
            src: Tokens fuente [batch, src_len]
            tgt: Tokens objetivo [batch, tgt_len]
            src_mask: Máscara de padding para la fuente
            tgt_mask: Máscara causal para el objetivo
        Returns:
            Logits sobre el vocabulario [batch, tgt_len, tgt_vocab_size]
        """
        # 1. Codificar la secuencia fuente
        encoder_output = self.encode(src, src_mask)

        # 2. Decodificar la secuencia objetivo con contexto del encoder
        decoder_output = self.decode(tgt, encoder_output, src_mask, tgt_mask)

        # 3. Proyectar al espacio del vocabulario
        logits = self.output_projection(decoder_output)

        return logits
```

Este código define un modelo Transformer completo que puede instanciarse con los hiperparámetros del modelo base original:

```python
# Instanciar modelo con hiperparámetros del Transformer base
model = Transformer(
    src_vocab_size=32000,   # Vocabulario fuente
    tgt_vocab_size=32000,   # Vocabulario objetivo
    d_model=512,            # Dimensión del modelo
    num_heads=8,            # Número de cabezas de atención
    num_layers=6,           # Número de capas (encoder y decoder)
    d_ff=2048,              # Dimensión de la FFN
    dropout=0.1             # Probabilidad de dropout
)

# Verificar número de parámetros
total_params = sum(p.numel() for p in model.parameters())
print(f"Parámetros totales: {total_params:,}")
```

---

## 6.9 Ejemplo: Transformer para traducción

### 6.9.1 Descripción conceptual del proceso

Para ilustrar el funcionamiento del Transformer de manera concreta, consideremos el ejemplo de traducir la oración del inglés al español:

- **Oración fuente (inglés):** "The cat sits on the mat"
- **Oración objetivo (español):** "El gato se sienta en la alfombra"

Veamos paso a paso cómo el Transformer procesa esta tarea.

### 6.9.2 Procesamiento en el encoder

**Paso 1: Tokenización.** La oración fuente se tokeniza (posiblemente usando subpalabras como BPE o SentencePiece) y se convierte en una secuencia de índices enteros:

$$\text{src} = [102, \ 3847, \ 9215, \ 87, \ 102, \ 5631]$$

donde cada número corresponde al índice del token en el vocabulario fuente. La secuencia tiene longitud $T_s = 6$.

**Paso 2: Embedding y codificación posicional.** Cada índice se convierte en un vector de dimensión $d_{model} = 512$, se escala por $\sqrt{512} \approx 22.63$, y se le suma su codificación posicional correspondiente:

$$\mathbf{z}_t^{(0)} = \sqrt{512} \cdot \text{Embed}(x_t) + \mathbf{PE}_t, \quad t = 1, \ldots, 6$$

El resultado es una matriz $\mathbf{Z}^{(0)} \in \mathbb{R}^{6 \times 512}$, donde cada fila es la representación inicial de un token con su información posicional.

**Paso 3: Pila de bloques encoder.** La matriz $\mathbf{Z}^{(0)}$ pasa secuencialmente por los $N = 6$ bloques encoder. En cada bloque:

- **Self-Attention Multi-Cabezal ($h = 8$):** Cada token "atiende" a todos los demás tokens. Por ejemplo, al procesar "sits", el mecanismo de atención podría asignar pesos altos a "cat" (su sujeto) y "mat" (su complemento), capturando las dependencias sintácticas y semánticas.

  Con 8 cabezas de atención, el modelo puede capturar simultáneamente diferentes tipos de relaciones:
  - Una cabeza podría capturar relaciones sujeto-verbo ("cat" → "sits").
  - Otra podría capturar relaciones de posición espacial ("on" → "mat").
  - Otra podría capturar la estructura del artículo definido ("the" → "cat", "the" → "mat").

- **Add & Norm:** La salida de la atención se suma con la entrada (conexión residual) y se normaliza.

- **FFN:** Se aplica la red feed-forward $\text{FFN}(\mathbf{x}) = \max(0, \mathbf{x}\mathbf{W}_1 + \mathbf{b}_1)\mathbf{W}_2 + \mathbf{b}_2$ de manera independiente a cada posición, refinando las representaciones.

- **Add & Norm:** Otra conexión residual y normalización.

Después de 6 bloques, la salida final del encoder es $\mathbf{Z}^{(6)} \in \mathbb{R}^{6 \times 512}$, donde cada vector de 512 dimensiones contiene una representación rica y contextualizada de cada token de la oración fuente. Crucialmente, la representación de "cat" en $\mathbf{Z}^{(6)}$ no solo codifica la semántica de la palabra "cat", sino también su papel como sujeto de "sits", su relación con "the", y su contexto dentro de toda la oración.

### 6.9.3 Generación en el decoder (inferencia)

Durante la inferencia, el decoder genera la traducción token por token de manera autoregresiva. Veamos el proceso:

**Paso 0: Inicio.** La entrada inicial al decoder es el token de inicio: $\text{tgt} = [\langle \text{SOS} \rangle]$.

**Paso 1: Generar "El".**
1. El token $\langle \text{SOS} \rangle$ se convierte en embedding y se suma su codificación posicional.
2. Pasa por los bloques decoder:
   - **Masked Self-Attention:** Solo hay un token, así que la atención es trivial.
   - **Cross-Attention:** El token $\langle \text{SOS} \rangle$ del decoder (como consulta $\mathbf{Q}$) atiende a la representación del encoder $\mathbf{Z}^{(6)}$ (como claves $\mathbf{K}$ y valores $\mathbf{V}$). El modelo aprende a enfocarse en "The" como la fuente más relevante para generar el primer token de la traducción.
   - **FFN:** Refina la representación.
3. La capa de salida produce un vector de logits sobre el vocabulario español.
4. Se aplica softmax y se selecciona el token con mayor probabilidad: "El".

$\text{tgt} = [\langle \text{SOS} \rangle, \ \text{El}]$

**Paso 2: Generar "gato".**
1. Ahora la entrada al decoder es $[\langle \text{SOS} \rangle, \ \text{El}]$.
2. En la masked self-attention, "El" puede atender a $\langle \text{SOS} \rangle$ y a sí mismo, pero la máscara causal impide que $\langle \text{SOS} \rangle$ atienda a "El".
3. En la cross-attention, las representaciones del decoder atienden al encoder. El modelo debería enfocarse principalmente en "cat" para generar la traducción correspondiente.
4. Se genera "gato".

$\text{tgt} = [\langle \text{SOS} \rangle, \ \text{El}, \ \text{gato}]$

**Paso 3: Generar "se".**
1. Entrada: $[\langle \text{SOS} \rangle, \ \text{El}, \ \text{gato}]$.
2. La self-attention enmascarada permite que "se" atienda a los tres tokens anteriores.
3. La cross-attention se enfoca en "sits" y su contexto.
4. Se genera "se".

Este proceso continúa token por token: "sienta" → "en" → "la" → "alfombra" → $\langle \text{EOS} \rangle$.

**Paso final:** Cuando el modelo genera el token especial de fin de secuencia $\langle \text{EOS} \rangle$, la generación se detiene. La traducción completa es:

$$\text{Salida} = [\text{El}, \ \text{gato}, \ \text{se}, \ \text{sienta}, \ \text{en}, \ \text{la}, \ \text{alfombra}]$$

### 6.9.4 Diferencia entre entrenamiento e inferencia

Es fundamental entender la diferencia entre el modo de entrenamiento y el modo de inferencia del decoder:

- **Entrenamiento (*teacher forcing*):** La entrada completa al decoder es la secuencia objetivo desplazada: $[\langle \text{SOS} \rangle, \text{El}, \text{gato}, \text{se}, \text{sienta}, \text{en}, \text{la}, \text{alfombra}]$. Todos los tokens se procesan en paralelo (la máscara causal previene la fuga de información), y la pérdida se calcula simultáneamente para todas las posiciones. Esto es eficiente porque permite el procesamiento en paralelo de la secuencia completa.

- **Inferencia (*autoregresiva*):** El decoder genera un token a la vez. En cada paso, la secuencia de entrada crece en un token, y todo el bloque decoder debe re-ejecutarse. Esto es inherentemente secuencial y más lento que el entrenamiento. Para mejorar la eficiencia, se utiliza *KV-caching*: las claves y valores calculados para posiciones anteriores se almacenan en caché y se reutilizan, evitando recalcularlos en cada paso.

### 6.9.5 Relevancia para comunicaciones semánticas

El ejemplo de traducción ilustra perfectamente la analogía con las comunicaciones semánticas. En un sistema de comunicación semántica basado en Transformer:

- El **encoder semántico** (análogo al encoder del Transformer) extrae representaciones semánticas ricas de la fuente de información (texto, imagen, audio).
- La **transmisión por el canal** corresponde al paso de la representación codificada a través de un medio con ruido e interferencia.
- El **decoder semántico** (análogo al decoder del Transformer) reconstruye o interpreta el mensaje a partir de las representaciones recibidas, utilizando atención cruzada para alinear las representaciones del transmisor con la generación del receptor.

La capacidad del Transformer para capturar dependencias globales, procesar secuencias en paralelo y aprender representaciones contextualizadas ricas lo convierte en la arquitectura ideal para los sistemas de comunicación semántica modernos, donde la eficiencia y la fidelidad semántica son primordiales.

---

### Resumen de la Sección 6

En esta sección hemos estudiado en profundidad la arquitectura Transformer, cubriendo:

1. **Motivación:** Las limitaciones de las RNN (secuencialidad, dependencias de largo alcance) que motivaron la creación del Transformer.
2. **Codificación posicional:** Las funciones sinusoidales que inyectan información de posición, con la propiedad clave de que las posiciones relativas pueden representarse como transformaciones lineales.
3. **Encoder:** Multi-Head Self-Attention + Add & Norm + FFN + Add & Norm, apilados $N$ veces.
4. **Decoder:** Masked Self-Attention + Cross-Attention + FFN, con conexiones residuales y normalización.
5. **Arquitectura completa:** El pipeline encoder-decoder con capa de salida softmax.
6. **Entrenamiento:** Teacher forcing, label smoothing, warm-up de tasa de aprendizaje, y entropía cruzada.
7. **Variantes:** BERT (encoder), GPT (decoder), T5 (encoder-decoder), ViT (visión).
8. **Implementación:** Código PyTorch completo y comentado.
9. **Ejemplo práctico:** Traducción paso a paso mostrando el flujo de información.

En la siguiente sección, exploraremos cómo estas ideas se aplican específicamente al diseño de sistemas de comunicación semántica, donde el Transformer sirve como la columna vertebral para la extracción, transmisión y reconstrucción de significado.

---

# 7. Fundamentos de las Comunicaciones Semánticas

Las comunicaciones inalámbricas han alcanzado niveles de madurez extraordinarios gracias a décadas de investigación fundamentada en la teoría de la información de Shannon. Sin embargo, a medida que nos acercamos a los límites teóricos de la capacidad del canal, surge una pregunta fundamental: ¿es posible comunicar de forma más eficiente si transmitimos *significado* en lugar de *bits*? Esta pregunta, planteada originalmente por Warren Weaver en 1949, ha permanecido latente durante más de siete décadas y hoy resurge con fuerza gracias a los avances en inteligencia artificial, particularmente en modelos basados en Transformers y aprendizaje profundo.

En esta sección exploramos los fundamentos de las comunicaciones semánticas, un paradigma que promete revolucionar el diseño de sistemas de comunicación al operar en el nivel del significado. Partiremos del modelo clásico de Shannon, identificaremos sus limitaciones inherentes, y construiremos paso a paso la arquitectura de un sistema de comunicación semántica moderno. Veremos cómo los Transformers, estudiados en secciones anteriores de este tutorial, se convierten en la pieza clave que habilita la extracción y reconstrucción de información semántica.

---

## 7.1 Del modelo de Shannon a la comunicación semántica

### 7.1.1 La teoría matemática de la comunicación de Shannon (1948)

En 1948, Claude E. Shannon publicó su trabajo seminal *"A Mathematical Theory of Communication"* (Shannon, 1948), estableciendo los cimientos de la teoría de la información moderna. En este trabajo, Shannon definió un marco matemático riguroso para cuantificar la información y establecer los límites fundamentales de la transmisión de datos a través de canales con ruido.

El modelo de Shannon se compone de cinco elementos esenciales:

1. **Fuente de información**: produce un mensaje o una secuencia de mensajes que se desean comunicar.
2. **Transmisor (codificador)**: transforma el mensaje en una señal adecuada para ser transmitida por el canal.
3. **Canal**: el medio físico por el cual se transmite la señal, sujeto a ruido e interferencias.
4. **Receptor (decodificador)**: reconstruye el mensaje a partir de la señal recibida.
5. **Destino**: la entidad a la cual va dirigido el mensaje.

Shannon introdujo el concepto de **entropía de la información** como medida de la incertidumbre asociada a una fuente de mensajes. Para una variable aleatoria discreta $X$ con alfabeto $\mathcal{X}$ y función de probabilidad $p(x)$, la entropía se define como:

$$H(X) = -\sum_{x \in \mathcal{X}} p(x) \log_2 p(x)$$

La entropía representa la cantidad mínima de bits necesarios, en promedio, para representar un símbolo de la fuente. Si la fuente produce símbolos equiprobables de un alfabeto de tamaño $M$, entonces $H(X) = \log_2 M$ bits por símbolo. Si algunos símbolos son más probables que otros, la entropía disminuye, reflejando la redundancia inherente en la fuente.

Uno de los resultados más profundos de Shannon es el **teorema de la capacidad del canal**, que establece que para un canal con ancho de banda $B$ (en Hz) y relación señal a ruido $\text{SNR}$ (lineal), la capacidad máxima de transmisión libre de errores es:

$$C = B \log_2(1 + \text{SNR})$$

Este resultado, conocido como la **fórmula de Shannon-Hartley**, tiene implicaciones extraordinarias. Nos dice que existe un límite superior absoluto a la tasa de información que se puede transmitir de forma fiable a través de un canal con ruido aditivo gaussiano blanco (AWGN). Si la tasa de transmisión $R$ satisface $R < C$, entonces existe un esquema de codificación que permite una probabilidad de error arbitrariamente pequeña. Si $R > C$, la comunicación fiable es imposible sin importar el esquema de codificación utilizado.

Para comprender la profundidad de este resultado, desglosemos sus componentes. El ancho de banda $B$ representa el rango de frecuencias disponible para la transmisión; un mayor ancho de banda permite transmitir más información por unidad de tiempo. La relación señal a ruido $\text{SNR} = P_s / P_n$, donde $P_s$ es la potencia de la señal y $P_n$ es la potencia del ruido, cuantifica la calidad del canal. El logaritmo en base 2 expresa la capacidad en bits por segundo. Observemos que la capacidad crece logarítmicamente con la $\text{SNR}$: duplicar la potencia de transmisión no duplica la capacidad, sino que la incrementa en solo $B$ bits/s. Esta dependencia logarítmica impone rendimientos decrecientes al aumentar la potencia.

Es fundamental observar que el marco de Shannon opera exclusivamente en el **nivel sintáctico** de la comunicación. La teoría se preocupa por la transmisión fiel de secuencias de símbolos, sin considerar en absoluto el significado que dichos símbolos puedan representar. Como el propio Shannon declaró explícitamente en su artículo:

> *"The fundamental problem of communication is that of reproducing at one point either exactly or approximately a message selected at another point. Frequently the messages have meaning... these semantic aspects of communication are irrelevant to the engineering problem."*

Esta deliberada exclusión del significado fue una decisión de diseño brillante que permitió construir una teoría matemática precisa y universal. Sin embargo, como veremos, esta exclusión también impone limitaciones fundamentales que las comunicaciones semánticas buscan superar.

### 7.1.2 Los tres niveles de comunicación de Weaver (1949)

Warren Weaver, en su influyente ensayo introductorio al trabajo de Shannon titulado *"Recent Contributions to the Mathematical Theory of Communication"* (Weaver, 1949), propuso una taxonomía de tres niveles para el problema de la comunicación:

**Nivel A — Problema técnico**: ¿Con qué precisión se pueden transmitir los símbolos de la comunicación? Este es el nivel en el que opera la teoría de Shannon. Se preocupa por la fidelidad bit a bit de la transmisión: ¿llegó cada bit correctamente al receptor? Las métricas relevantes son la tasa de error de bit (BER, *Bit Error Rate*), la tasa de error de bloque (BLER, *Block Error Rate*) y la capacidad del canal. Los sistemas de comunicación modernos —desde 2G hasta 5G— han sido diseñados y optimizados fundamentalmente en este nivel.

**Nivel B — Problema semántico**: ¿Con qué precisión los símbolos transmitidos transportan el significado deseado? Este nivel se pregunta si el receptor comprende lo que el transmisor quiso comunicar. Ya no importa si cada bit es correcto; lo que importa es si el *significado* se preserva. Por ejemplo, si se transmite la oración "El gato está sobre la mesa" y el receptor recibe "El felino se encuentra encima de la mesa", desde el punto de vista del Nivel A hay muchos errores (las palabras son diferentes), pero desde el Nivel B la comunicación ha sido perfecta (el significado es idéntico).

**Nivel C — Problema de efectividad**: ¿Con qué eficacia el significado recibido afecta la conducta del receptor de la manera deseada? Este nivel se preocupa por el impacto pragmático de la comunicación. En un sistema de conducción autónoma, por ejemplo, no basta con que el vehículo "comprenda" que hay un peatón adelante (Nivel B); debe tomar la acción correcta de frenar (Nivel C). Las comunicaciones orientadas a tareas (*task-oriented communications*) operan en este nivel.

La relación entre estos tres niveles es jerárquica pero no simplemente inclusiva. El éxito en el Nivel A no garantiza el éxito en el Nivel B (se pueden recibir todos los bits correctamente pero no comprender el mensaje si falta contexto). Análogamente, el éxito en el Nivel B no garantiza el éxito en el Nivel C (se puede comprender perfectamente un mensaje pero no actuar correctamente en consecuencia).

Las comunicaciones semánticas operan principalmente en el **Nivel B**, con extensiones naturales hacia el **Nivel C**. La idea central es diseñar sistemas que optimicen la preservación del significado, no la fidelidad de los bits, lo que permite una eficiencia radicalmente superior cuando los recursos del canal son limitados.

### 7.1.3 El "efecto precipicio" y las limitaciones del paradigma clásico

Los sistemas de comunicación clásicos exhiben un fenómeno conocido como el **efecto precipicio** (*cliff effect*): cuando la relación señal a ruido cae por debajo de un umbral crítico determinado por el esquema de modulación y codificación (MCS, *Modulation and Coding Scheme*), el rendimiento se desploma abruptamente. El sistema pasa de funcionar casi perfectamente a fallar completamente en un rango estrecho de SNR.

Este comportamiento se debe a la naturaleza discreta de las decisiones de decodificación en los sistemas clásicos. Cuando el canal es suficientemente bueno, el decodificador de canal puede corregir los errores y recuperar los bits originales con alta fiabilidad. Pero cuando el ruido supera la capacidad de corrección del código, los errores se propagan de forma catastrófica, el decodificador de fuente recibe bits incorrectos y la señal reconstruida se degrada dramáticamente.

Consideremos un sistema clásico de transmisión de imágenes. A una $\text{SNR}$ de 10 dB, el sistema podría producir una imagen perfecta. A 8 dB, quizás aparezcan algunos artefactos menores. Pero a 5 dB, la imagen podría ser completamente irreconocible — una cascada de píxeles erróneos sin estructura alguna. No hay degradación gradual: el sistema simplemente "se cae del precipicio".

Este fenómeno tiene consecuencias prácticas severas. En redes móviles, los usuarios que se encuentran en los bordes de las celdas o en condiciones de desvanecimiento profundo experimentan cortes abruptos del servicio. Los protocolos de adaptación de enlace (*link adaptation*) intentan mitigar este problema seleccionando MCS menos agresivos, pero esto reduce significativamente la eficiencia espectral.

### 7.1.4 El cambio de paradigma: transmitir significado, no bits

Las comunicaciones semánticas proponen un cambio de paradigma radical: en lugar de transmitir una representación fiel de los datos de la fuente (cada píxel, cada muestra de audio, cada carácter), se transmite una representación compacta del *significado* contenido en dichos datos.

Este cambio tiene implicaciones profundas. Primero, la cantidad de información a transmitir se reduce drásticamente, porque el significado es típicamente mucho más comprimible que los datos crudos. Una imagen de un gato sobre una mesa requiere millones de bits para su representación pixel a pixel, pero su significado semántico ("un gato anaranjado sentado sobre una mesa de madera en una cocina") puede representarse con unos pocos cientos de bits.

Segundo, la comunicación se vuelve **robusta al ruido de forma natural**. El ruido del canal corrompe bits individuales, pero la representación semántica, al ser una abstracción de alto nivel, es intrínsecamente más resiliente a perturbaciones en el nivel de bits. Un vector semántico ligeramente perturbado por ruido gaussiano sigue representando aproximadamente el mismo concepto.

Tercero, el sistema puede **degradarse graciosamente** en lugar de exhibir el efecto precipicio. A medida que la SNR disminuye, la calidad semántica de la reconstrucción se degrada de forma gradual y predecible, no abrupta. Bajo condiciones muy adversas, el receptor podría obtener una reconstrucción aproximada (quizás menos detallada o con vocabulario diferente), pero que preserva el significado esencial.

**Figura 7.1:** *Comparación entre un sistema de comunicación clásico y un sistema de comunicación semántica. (a) Sistema clásico: la fuente genera un mensaje que pasa por una cadena de bloques separados — codificación de fuente (compresión, e.g., JPEG, H.265), codificación de canal (protección contra errores, e.g., LDPC, Turbo codes), modulación (mapeo a símbolos, e.g., QAM), transmisión por el canal físico (sujeto a ruido e interferencia), demodulación, decodificación de canal, decodificación de fuente, y finalmente el destino recibe una reconstrucción del mensaje original. Cada bloque está optimizado de forma independiente. (b) Sistema semántico: la fuente genera un mensaje que es procesado por un codificador semántico (extrae el significado, típicamente una red neuronal) y un codificador de canal (adapta la representación semántica al canal), la señal atraviesa el canal físico, y en el receptor un decodificador de canal y un decodificador semántico (reconstruye un mensaje con el mismo significado, típicamente otra red neuronal) entregan el contenido al destino. Los bloques de codificación de fuente y canal se fusionan en la codificación semántica conjunta. La optimización es de extremo a extremo.*

---

## 7.2 ¿Qué es la "semántica" en comunicaciones?

### 7.2.1 Información semántica versus información sintáctica

Para comprender las comunicaciones semánticas es esencial distinguir con precisión entre **información sintáctica** e **información semántica**.

La **información sintáctica**, en el sentido de Shannon, se refiere a la secuencia de símbolos que compone un mensaje, sin consideración alguna por su significado. Dos mensajes con idéntica estructura estadística (misma distribución de probabilidad sobre los símbolos) tienen la misma entropía de Shannon, independientemente de si uno es una oración con sentido y el otro es una secuencia aleatoria de caracteres. La entropía de Shannon mide la *sorpresa* estadística, no el *contenido semántico*.

Formalmente, si un mensaje $\mathbf{s} = (s_1, s_2, \ldots, s_N)$ es una secuencia de $N$ símbolos de un alfabeto $\mathcal{S}$, la información sintáctica se cuantifica mediante:

$$I_{\text{sintáctica}}(\mathbf{s}) = -\log_2 p(\mathbf{s})$$

donde $p(\mathbf{s})$ es la probabilidad de ocurrencia del mensaje $\mathbf{s}$ según el modelo estadístico de la fuente. Esta medida no captura la relación entre el mensaje y su referente en el mundo real.

La **información semántica**, en contraste, se refiere al *significado* que el mensaje transporta — su contenido proposicional, las entidades que describe, las relaciones que establece, las acciones que implica. Dos mensajes con diferentes secuencias de símbolos pueden transportar la misma información semántica. Por ejemplo:

- "La temperatura en Madrid es de 35°C"
- "En la capital española, el termómetro marca treinta y cinco grados centígrados"

Estas dos oraciones tienen información sintáctica completamente diferente (diferentes palabras, diferente longitud, diferentes estadísticas de caracteres), pero transportan información semántica prácticamente idéntica.

La cuantificación rigurosa de la información semántica ha sido un desafío abierto durante décadas. Diversos enfoques han sido propuestos, desde la teoría de la información semántica de Bar-Hillel y Carnap (1952) basada en lógica proposicional, hasta los enfoques modernos basados en representaciones distribuidas (*embeddings*) aprendidos por redes neuronales.

En el paradigma moderno de comunicaciones semánticas, la información semántica de un mensaje $\mathbf{s}$ se representa como un **vector de características semánticas** $\mathbf{z} \in \mathbb{R}^d$, obtenido mediante un codificador semántico $f_\theta$:

$$\mathbf{z} = f_\theta(\mathbf{s})$$

donde $\theta$ denota los parámetros del codificador (típicamente una red neuronal profunda). Este vector $\mathbf{z}$ vive en un espacio semántico de dimensión $d$, donde la proximidad geométrica refleja la similitud de significado. Mensajes con significado similar producen vectores cercanos en este espacio; mensajes con significado diferente producen vectores distantes.

### 7.2.2 Ejemplo ilustrativo: transmisión de una imagen

Consideremos el problema de transmitir una fotografía de un perro jugando en un parque a través de un canal con capacidad limitada. Este ejemplo ilustra de manera contundente la diferencia entre los paradigmas clásico y semántico.

**Enfoque clásico (sintáctico):**

1. La imagen se representa como una matriz de píxeles, por ejemplo $1024 \times 768$ píxeles con 3 canales de color (RGB) y 8 bits por canal.
2. La cantidad total de datos es $1024 \times 768 \times 3 \times 8 = 18{,}874{,}368$ bits (≈ 18.9 Mbits) sin comprimir.
3. Se aplica codificación de fuente (e.g., JPEG) para comprimir, reduciendo quizás a 500 Kbits.
4. Se aplica codificación de canal (e.g., código LDPC) para proteger contra errores, añadiendo redundancia.
5. La señal resultante se modula y transmite.
6. En el receptor, se demodula, decodifica el canal, y decodifica la fuente.
7. El objetivo es reconstruir cada píxel con la mayor fidelidad posible.

Si las condiciones del canal son buenas, se obtiene una imagen idéntica o muy similar a la original. Si las condiciones son malas (baja SNR), la decodificación de canal falla y la imagen reconstruida presenta artefactos severos o es completamente irreconocible.

**Enfoque semántico:**

1. Un codificador semántico (e.g., una red neuronal convolucional profunda como ResNet o un Vision Transformer) procesa la imagen y extrae su contenido semántico.
2. La representación semántica podría codificarse como un vector compacto que capture: "perro de raza labrador, color dorado, corriendo, pelota roja en la boca, parque con césped verde, día soleado".
3. Esta representación compacta requiere quizás solo $d = 256$ o $d = 512$ valores de punto flotante, es decir, unos pocos miles de bits.
4. El codificador de canal adapta esta representación para transmisión eficiente.
5. En el receptor, el decodificador de canal recupera una versión posiblemente ruidosa de la representación semántica.
6. El decodificador semántico (e.g., un modelo generativo) reconstruye una imagen que es **semánticamente consistente** con la original, aunque puede diferir en detalles de bajo nivel (la posición exacta de cada hoja de césped, la textura precisa del pelaje).

La reducción en la cantidad de datos es dramática: de cientos de miles de bits a unos pocos miles. Además, la imagen reconstruida preserva su significado incluso bajo condiciones de canal adversas, exhibiendo una degradación gradual en lugar del efecto precipicio.

### 7.2.3 Comunicaciones orientadas a tareas

Un concepto estrechamente relacionado con las comunicaciones semánticas es el de **comunicaciones orientadas a tareas** (*task-oriented communications*), que operan en el Nivel C de Weaver. En este paradigma, el objetivo del sistema no es reconstruir el mensaje original ni siquiera preservar su significado completo, sino transmitir únicamente la información necesaria para que el receptor realice una tarea específica.

Consideremos un vehículo autónomo que captura imágenes con su cámara y necesita enviarlas a un servidor en la nube para su procesamiento. En un sistema clásico, se transmitiría la imagen completa. En un sistema semántico, se transmitiría una representación del significado de la imagen. En un sistema orientado a tareas, si la tarea es detectar peatones, se transmitiría únicamente la información relevante para esa tarea: presencia/ausencia de peatones, sus posiciones y velocidades estimadas.

Formalmente, si la tarea del receptor se modela como una función $g: \mathcal{Z} \rightarrow \mathcal{Y}$ que mapea la información recibida a una acción o decisión, entonces el objetivo del sistema orientado a tareas es maximizar:

$$\max_{\theta, \phi} \mathbb{E}\left[\mathcal{U}(g(f_\phi(\hat{\mathbf{z}})), y^*)\right]$$

donde $\hat{\mathbf{z}}$ es la representación semántica recibida (posiblemente corrompida por el canal), $f_\phi$ es el decodificador semántico con parámetros $\phi$, $y^*$ es la acción óptima, y $\mathcal{U}$ es una función de utilidad que mide la calidad de la decisión tomada.

### 7.2.4 Entropía semántica e información mutua semántica

La extensión de los conceptos de entropía e información mutua al dominio semántico es un área activa de investigación. La **entropía semántica** busca cuantificar la incertidumbre asociada al significado de un mensaje, en contraste con la entropía de Shannon que cuantifica la incertidumbre sobre la secuencia de símbolos.

Intuitivamente, la entropía semántica de una fuente mide la diversidad de significados que puede generar. Una fuente que produce mensajes con gran variedad de significados tiene alta entropía semántica. Una fuente repetitiva que dice siempre esencialmente lo mismo tiene baja entropía semántica, incluso si utiliza diferentes palabras cada vez (lo que le daría alta entropía de Shannon).

Si denotamos el contenido semántico de un mensaje $\mathbf{s}$ como $\mathbf{z} = f_\theta(\mathbf{s})$, la entropía semántica puede definirse sobre la distribución del vector semántico:

$$H_{\text{sem}}(Z) = -\int_{\mathcal{Z}} p(\mathbf{z}) \log_2 p(\mathbf{z}) \, d\mathbf{z}$$

donde la integral se extiende sobre el espacio semántico $\mathcal{Z} \subseteq \mathbb{R}^d$. En la práctica, dado que $\mathbf{z}$ es continuo, se trabaja con la entropía diferencial.

La **información mutua semántica** entre el mensaje transmitido y el recibido cuantifica cuánto significado se preserva a través del canal:

$$I_{\text{sem}}(Z; \hat{Z}) = H_{\text{sem}}(Z) - H_{\text{sem}}(Z | \hat{Z})$$

donde $Z$ es la representación semántica transmitida y $\hat{Z}$ es la representación semántica recibida. Esta cantidad mide la reducción en la incertidumbre semántica del mensaje transmitido dada la observación en el receptor. Un sistema de comunicación semántica ideal maximizaría esta información mutua semántica.

---

## 7.3 Arquitectura general de un sistema de comunicación semántica

### 7.3.1 Codificación conjunta de fuente y canal (JSCC)

Los sistemas de comunicación clásicos se basan en el **teorema de separación** de Shannon, que establece que la codificación de fuente y la codificación de canal pueden diseñarse de forma independiente sin pérdida de optimalidad, siempre que se permitan longitudes de bloque arbitrariamente grandes y se disponga de tiempo ilimitado para la codificación y decodificación. Formalmente, si la entropía de la fuente $H(S)$ es menor que la capacidad del canal $C$, entonces la comunicación fiable es posible, y la codificación de fuente óptima seguida de la codificación de canal óptima alcanza este límite.

Sin embargo, el teorema de separación requiere condiciones ideales que rara vez se satisfacen en la práctica:

- **Longitud de bloque infinita**: el rendimiento óptimo se alcanza asintóticamente; en la práctica, los bloques tienen longitud finita, lo que introduce pérdida de rendimiento.
- **Modelo estadístico perfecto de la fuente**: se asume que la distribución de la fuente es conocida exactamente, lo cual es difícil para fuentes complejas como imágenes naturales, voz o texto.
- **Canal estacionario y ergódico**: se asume que las estadísticas del canal no cambian, lo cual es una aproximación en canales móviles con desvanecimiento variable.
- **Sin restricciones de complejidad ni latencia**: el diseño separado introduce latencia adicional y puede requerir complejidad computacional prohibitiva.

La **codificación conjunta de fuente y canal** (*Joint Source-Channel Coding*, JSCC) abandona el principio de separación y diseña un esquema unificado que simultáneamente comprime la fuente y protege contra errores del canal. La JSCC puede superar al diseño separado en régimen de longitud de bloque finita, cuando el modelo de la fuente es imperfecto, o cuando las condiciones del canal varían rápidamente.

En el contexto de las comunicaciones semánticas, la JSCC toma una forma particularmente natural. El codificador semántico realiza implícitamente tanto la compresión de fuente (al extraer solo el significado relevante) como la codificación de canal (al generar una representación que sea robusta al ruido). Ambas funciones se optimizan conjuntamente a través del aprendizaje de extremo a extremo.

Matemáticamente, un sistema JSCC aprendido puede modelarse como:

$$\hat{\mathbf{s}} = g_\phi(h(\text{enc}_\theta(\mathbf{s})) + \mathbf{n})$$

donde $\mathbf{s}$ es el mensaje fuente, $\text{enc}_\theta: \mathcal{S} \rightarrow \mathbb{R}^k$ es el codificador con parámetros $\theta$ que mapea el mensaje a $k$ símbolos de canal, $h(\cdot)$ representa los efectos del canal (atenuación, rotación de fase, etc.), $\mathbf{n}$ es el ruido aditivo, y $g_\phi: \mathbb{R}^k \rightarrow \hat{\mathcal{S}}$ es el decodificador con parámetros $\phi$ que reconstruye el mensaje. Los parámetros $\theta$ y $\phi$ se optimizan conjuntamente para minimizar una función de pérdida que mide la distorsión semántica.

### 7.3.2 Aprendizaje de extremo a extremo (E2E)

El enfoque de **aprendizaje de extremo a extremo** (*End-to-End Learning*, E2E) es la metodología dominante para el diseño de sistemas de comunicación semántica. En lugar de diseñar cada bloque del sistema de forma independiente y luego integrarlos, el enfoque E2E entrena todo el sistema como una única red neuronal, optimizando directamente la métrica de rendimiento final deseada.

El principio fundamental es modelar todo el sistema de comunicación — codificador, canal y decodificador — como un grafo computacional diferenciable, lo que permite utilizar el algoritmo de retropropagación (*backpropagation*) para optimizar los parámetros de extremo a extremo.

El desafío principal es que el canal físico es una componente estocástica no parametrizada que no tiene gradientes analíticos. Para resolver esto, se utiliza una de varias estrategias:

1. **Modelo diferenciable del canal**: se reemplaza el canal físico por un modelo matemático diferenciable. Para un canal AWGN, esto es simplemente añadir ruido gaussiano: $\mathbf{y} = \mathbf{x} + \mathbf{n}$, donde $\mathbf{n} \sim \mathcal{N}(\mathbf{0}, \sigma^2 \mathbf{I})$. Este modelo es trivialmente diferenciable (los gradientes fluyen a través de la suma sin modificación). Para un canal de desvanecimiento Rayleigh, el modelo es $\mathbf{y} = \mathbf{h} \odot \mathbf{x} + \mathbf{n}$, donde $\mathbf{h} \sim \mathcal{CN}(\mathbf{0}, \mathbf{I})$ son los coeficientes de desvanecimiento, y $\odot$ denota el producto elemento a elemento.

2. **Truco de reparametrización**: similar al utilizado en autoencoders variacionales (VAEs), se reparametriza la componente estocástica del canal para permitir el flujo de gradientes.

3. **Estimación de gradientes por políticas**: se utilizan técnicas de aprendizaje por refuerzo (e.g., REINFORCE) para estimar los gradientes a través de componentes no diferenciables.

La función de pérdida del sistema E2E típicamente toma la forma:

$$\mathcal{L}(\theta, \phi) = \mathbb{E}_{\mathbf{s} \sim p(\mathbf{s}),\, \mathbf{n} \sim \mathcal{N}}\left[d(\mathbf{s}, \hat{\mathbf{s}})\right]$$

donde $d(\cdot, \cdot)$ es una medida de distorsión semántica entre el mensaje original $\mathbf{s}$ y el reconstruido $\hat{\mathbf{s}} = g_\phi(h(\text{enc}_\theta(\mathbf{s})) + \mathbf{n})$. La elección de $d$ depende del tipo de datos y la tarea:

- Para texto: entropía cruzada a nivel de palabra, similitud semántica en espacio de embeddings.
- Para imágenes: error cuadrático medio ponderado perceptualmente, distancia en espacio de características de una red pre-entrenada.
- Para tareas: función de pérdida específica de la tarea (e.g., exactitud de clasificación, error de detección).

### 7.3.3 Componentes del sistema

Un sistema de comunicación semántica completo consta de los siguientes componentes principales:

**Transmisor:**

El transmisor se compone de dos sub-bloques conceptuales que, en la práctica, pueden implementarse como una única red neuronal entrenada de extremo a extremo:

- **Codificador semántico** ($\text{SemEnc}_\theta$): este módulo procesa el mensaje de la fuente $\mathbf{s}$ y extrae su representación semántica $\mathbf{z} \in \mathbb{R}^d$. Típicamente se implementa como una red neuronal profunda: un Transformer para texto, una red convolucional (CNN) o un Vision Transformer (ViT) para imágenes, o una red recurrente para secuencias temporales. La dimensión $d$ del espacio semántico es un hiperparámetro que controla la compresión: un $d$ menor implica mayor compresión pero potencialmente mayor pérdida semántica.

$$\mathbf{z} = \text{SemEnc}_\theta(\mathbf{s}) \in \mathbb{R}^d$$

- **Codificador de canal** ($\text{ChEnc}_\alpha$): este módulo transforma la representación semántica $\mathbf{z}$ en símbolos de canal $\mathbf{x} \in \mathbb{C}^k$ (o $\mathbb{R}^{2k}$) adecuados para la transmisión por el medio físico. Debe satisfacer una restricción de potencia promedio: $\mathbb{E}[||\mathbf{x}||^2] \leq k \cdot P$, donde $P$ es la potencia por uso de canal. El ratio $\rho = d / k$ se denomina **tasa de compresión de canal** y determina cuántos símbolos de canal se utilizan para transmitir cada componente de la representación semántica.

$$\mathbf{x} = \text{ChEnc}_\alpha(\mathbf{z}) \in \mathbb{C}^k$$

**Canal:**

El canal físico introduce distorsiones en la señal transmitida. Los modelos de canal más utilizados son:

- **Canal AWGN** (*Additive White Gaussian Noise*):

$$\mathbf{y} = \mathbf{x} + \mathbf{n}, \quad \mathbf{n} \sim \mathcal{CN}(\mathbf{0}, \sigma_n^2 \mathbf{I})$$

donde $\sigma_n^2$ es la potencia del ruido, y la SNR se define como $\text{SNR} = P / \sigma_n^2$.

- **Canal de desvanecimiento Rayleigh** (*Rayleigh Fading Channel*):

$$\mathbf{y} = \mathbf{h} \odot \mathbf{x} + \mathbf{n}, \quad h_i \sim \mathcal{CN}(0, 1)$$

donde $\mathbf{h}$ es el vector de coeficientes de desvanecimiento. Este modelo representa escenarios donde no hay línea de vista directa entre el transmisor y el receptor, como en entornos urbanos con múltiples reflexiones. Los coeficientes $h_i$ siguen una distribución Rayleigh en magnitud, y la fase es uniformemente distribuida en $[0, 2\pi)$.

- **Canal de desvanecimiento Rician** (*Rician Fading Channel*):

$$\mathbf{y} = \left(\sqrt{\frac{K}{K+1}} \mathbf{h}_{\text{LoS}} + \sqrt{\frac{1}{K+1}} \mathbf{h}_{\text{NLoS}}\right) \odot \mathbf{x} + \mathbf{n}$$

donde $K$ es el factor de Rician que representa la relación entre la componente de línea de vista directa $\mathbf{h}_{\text{LoS}}$ y las componentes de dispersión $\mathbf{h}_{\text{NLoS}}$.

**Receptor:**

El receptor es simétrico al transmisor y también consta de dos sub-bloques:

- **Decodificador de canal** ($\text{ChDec}_\beta$): procesa la señal recibida $\mathbf{y}$ y produce una estimación de la representación semántica $\hat{\mathbf{z}}$. En un sistema entrenado de extremo a extremo, este módulo aprende implícitamente a realizar ecualización, estimación de canal y decodificación de forma conjunta.

$$\hat{\mathbf{z}} = \text{ChDec}_\beta(\mathbf{y}) \in \mathbb{R}^d$$

- **Decodificador semántico** ($\text{SemDec}_\gamma$): transforma la representación semántica estimada $\hat{\mathbf{z}}$ en una reconstrucción del mensaje original $\hat{\mathbf{s}}$. Para texto, esto implica generar una secuencia de palabras; para imágenes, reconstruir una matriz de píxeles.

$$\hat{\mathbf{s}} = \text{SemDec}_\gamma(\hat{\mathbf{z}})$$

El sistema completo puede expresarse como la composición:

$$\hat{\mathbf{s}} = \text{SemDec}_\gamma\left(\text{ChDec}_\beta\left(h\left(\text{ChEnc}_\alpha\left(\text{SemEnc}_\theta(\mathbf{s})\right)\right) + \mathbf{n}\right)\right)$$

y todos los parámetros $\{\theta, \alpha, \beta, \gamma\}$ se optimizan conjuntamente minimizando la pérdida semántica $\mathcal{L}$.

**Figura 7.2:** *Arquitectura detallada de un sistema de comunicación semántica de extremo a extremo (E2E). El diagrama muestra el flujo completo de información. En el transmisor: el mensaje fuente $\mathbf{s}$ (texto, imagen o señal) ingresa al Codificador Semántico (red neuronal profunda, e.g., Transformer), que produce la representación semántica $\mathbf{z} \in \mathbb{R}^d$; esta pasa al Codificador de Canal (capas densas con normalización de potencia), que genera los símbolos de canal $\mathbf{x} \in \mathbb{C}^k$. Los símbolos atraviesan el Canal Físico (modelado como capa diferenciable: AWGN, Rayleigh, o Rician), produciendo la señal recibida $\mathbf{y}$. En el receptor: $\mathbf{y}$ ingresa al Decodificador de Canal (capas densas), que estima $\hat{\mathbf{z}}$; esta pasa al Decodificador Semántico (red neuronal profunda, e.g., Transformer), que produce el mensaje reconstruido $\hat{\mathbf{s}}$. Una flecha de retropropagación recorre todo el sistema de extremo a extremo, indicando que los gradientes fluyen desde la función de pérdida $\mathcal{L}(\mathbf{s}, \hat{\mathbf{s}})$ a través de todos los bloques para la optimización conjunta.*

---

## 7.4 El papel de los Transformers en las comunicaciones semánticas

### 7.4.1 ¿Por qué los Transformers son ideales para la extracción semántica?

Los Transformers, introducidos por Vaswani et al. (2017) en el artículo *"Attention Is All You Need"*, se han convertido en la arquitectura dominante para el procesamiento de lenguaje natural y, progresivamente, para visión por computador y procesamiento de señales. Su adopción en comunicaciones semánticas no es casual; las propiedades fundamentales de la arquitectura Transformer la hacen excepcionalmente adecuada para la extracción y reconstrucción de significado:

**1. El mecanismo de auto-atención captura significado contextual.**

La operación de auto-atención (*self-attention*) permite que cada elemento de una secuencia de entrada interactúe con todos los demás, ponderando su importancia relativa de forma aprendida. Recordemos que la auto-atención se calcula como:

$$\text{Attention}(\mathbf{Q}, \mathbf{K}, \mathbf{V}) = \text{softmax}\left(\frac{\mathbf{Q}\mathbf{K}^\top}{\sqrt{d_k}}\right)\mathbf{V}$$

donde $\mathbf{Q}$, $\mathbf{K}$ y $\mathbf{V}$ son las matrices de consultas (*queries*), claves (*keys*) y valores (*values*), respectivamente, obtenidas como proyecciones lineales de la entrada, y $d_k$ es la dimensión de las claves, utilizado como factor de escalado para estabilizar los gradientes.

Esta operación es crucial para las comunicaciones semánticas porque permite capturar dependencias de largo alcance y relaciones contextuales en el mensaje. En una oración como "El banco donde me senté estaba junto al banco del río", el mecanismo de atención puede desambiguar el doble significado de "banco" atendiendo al contexto ("senté" y "río"), una capacidad esencial para la extracción semántica precisa.

Los pesos de atención $\mathbf{A} = \text{softmax}\left(\frac{\mathbf{Q}\mathbf{K}^\top}{\sqrt{d_k}}\right)$ forman una matriz $N \times N$ (donde $N$ es la longitud de la secuencia) que codifica las relaciones de importancia entre cada par de elementos. El elemento $A_{ij}$ indica cuánta atención presta el elemento $i$ al elemento $j$. Estos pesos de atención son, en cierto sentido, una representación explícita de la estructura semántica del mensaje: revelan qué partes del mensaje son relevantes para entender cada otra parte.

**2. Capacidad multimodal.**

Los Transformers pueden procesar diferentes modalidades de datos — texto, imágenes, audio, señales — con la misma arquitectura base. Para texto, la entrada son embeddings de tokens (palabras o subpalabras). Para imágenes, se utilizan *patches* (regiones cuadradas de la imagen) como tokens (Vision Transformer, ViT). Para señales, se pueden utilizar ventanas temporales o representaciones en el dominio de la frecuencia. Esta versatilidad permite diseñar sistemas de comunicación semántica unificados para múltiples tipos de datos.

**3. Modelos pre-entrenados como base de conocimiento.**

Los modelos de lenguaje pre-entrenados a gran escala (e.g., BERT, GPT) han internalizado vastas cantidades de conocimiento sobre la estructura del lenguaje y las relaciones semánticas entre conceptos. Este conocimiento pre-entrenado puede aprovecharse en comunicaciones semánticas: un codificador semántico basado en un Transformer pre-entrenado ya posee una comprensión profunda del lenguaje, lo que reduce la cantidad de datos de entrenamiento necesarios y mejora la calidad de la extracción semántica.

Formalmente, el espacio de representaciones de un Transformer pre-entrenado define un espacio semántico $\mathcal{Z}$ con propiedades deseables: vectores cercanos corresponden a conceptos semánticamente similares, las direcciones en el espacio capturan relaciones semánticas (e.g., la dirección "rey" - "hombre" + "mujer" ≈ "reina"), y la estructura del espacio es suave (pequeñas perturbaciones producen pequeños cambios en el significado).

### 7.4.2 DeepSC: Comunicación semántica basada en Transformers para texto

El sistema **DeepSC** (*Deep Learning Enabled Semantic Communication*), propuesto por Xie et al. (2021) en el artículo *"Deep Learning Enabled Semantic Communication Systems"* (DOI: 10.1109/TSP.2021.3071082), es uno de los trabajos pioneros y más influyentes en comunicaciones semánticas basadas en Transformers. DeepSC demostró que un sistema de comunicación semántica entrenado de extremo a extremo puede superar significativamente a los sistemas clásicos, especialmente en condiciones de baja SNR.

La arquitectura de DeepSC consta de los siguientes componentes:

**Codificador semántico (Transmisor):**

El codificador semántico de DeepSC utiliza la arquitectura del codificador Transformer para extraer las características semánticas del texto de entrada. El proceso comienza con la tokenización de la oración de entrada en una secuencia de tokens $\mathbf{s} = (w_1, w_2, \ldots, w_L)$, donde $L$ es la longitud de la oración.

Cada token se convierte en un vector de embedding denso $\mathbf{e}_i \in \mathbb{R}^{d_{\text{model}}}$ mediante una capa de embedding entrenada. A estos embeddings se les suma una codificación posicional $\mathbf{PE}_i$ para incorporar información sobre la posición de cada token en la secuencia:

$$\mathbf{h}_i^{(0)} = \mathbf{e}_i + \mathbf{PE}_i$$

Los vectores $\{\mathbf{h}_i^{(0)}\}_{i=1}^L$ pasan por $N_e$ capas de codificador Transformer. Cada capa aplica auto-atención multi-cabeza (*multi-head attention*) seguida de una red *feed-forward*, con conexiones residuales y normalización de capa:

$$\mathbf{h}^{(\ell)} = \text{TransformerEncoderLayer}(\mathbf{h}^{(\ell-1)}), \quad \ell = 1, \ldots, N_e$$

La salida del último nivel del codificador Transformer $\mathbf{h}^{(N_e)} \in \mathbb{R}^{L \times d_{\text{model}}}$ constituye las características semánticas crudas. Estas se procesan mediante capas densas adicionales para producir la representación semántica final $\mathbf{z} \in \mathbb{R}^{L \times d_z}$, donde $d_z$ es la dimensión de la representación semántica por token.

$$\mathbf{z} = \text{Dense}_\theta(\mathbf{h}^{(N_e)})$$

**Codificador de canal:**

El codificador de canal transforma la representación semántica en símbolos aptos para la transmisión física. En DeepSC, esto se implementa mediante capas densas que mapean $\mathbf{z}$ a los símbolos de canal $\mathbf{x} \in \mathbb{R}^{L \times d_c}$, donde $d_c$ determina el número de símbolos de canal por token. La tasa de transmisión semántica se define como $R_s = d_c / d_{\text{model}}$, que indica cuántos símbolos de canal se utilizan por cada dimensión del modelo.

Se aplica una normalización de potencia para satisfacer la restricción de potencia del canal:

$$\mathbf{x} = \sqrt{k \cdot P} \cdot \frac{\tilde{\mathbf{x}}}{||\tilde{\mathbf{x}}||}$$

donde $\tilde{\mathbf{x}}$ es la salida de las capas densas antes de la normalización.

**Canal físico:**

DeepSC modela el canal como una capa estocástica diferenciable. Para un canal AWGN:

$$\mathbf{y} = \mathbf{x} + \mathbf{n}, \quad n_i \sim \mathcal{N}(0, \sigma_n^2)$$

Para un canal Rayleigh:

$$\mathbf{y} = \mathbf{h} \odot \mathbf{x} + \mathbf{n}, \quad h_i \sim \mathcal{CN}(0, 1)$$

Como estas operaciones son diferenciables (la adición de ruido y la multiplicación por coeficientes de canal), los gradientes pueden fluir directamente a través del modelo del canal durante la retropropagación.

**Decodificador de canal:**

El decodificador de canal es simétrico al codificador de canal: capas densas que transforman la señal recibida $\mathbf{y}$ en una estimación de la representación semántica $\hat{\mathbf{z}}$.

$$\hat{\mathbf{z}} = \text{Dense}_\beta(\mathbf{y})$$

**Decodificador semántico (Receptor):**

El decodificador semántico utiliza la arquitectura del decodificador Transformer para reconstruir el texto a partir de la representación semántica estimada. Emplea auto-atención enmascarada (*masked self-attention*) para la generación autorregresiva y atención cruzada (*cross-attention*) para atender a la representación semántica recibida.

$$\hat{\mathbf{s}} = \text{TransformerDecoder}_\gamma(\hat{\mathbf{z}})$$

La salida del decodificador es una distribución de probabilidad sobre el vocabulario para cada posición, de la cual se generan los tokens reconstruidos:

$$p(\hat{w}_t | \hat{w}_{<t}, \hat{\mathbf{z}}) = \text{softmax}(\mathbf{W}_o \cdot \text{TransDec}(\hat{w}_{<t}, \hat{\mathbf{z}}))$$

donde $\mathbf{W}_o$ es la matriz de proyección de salida.

**Entrenamiento:**

El sistema se entrena de extremo a extremo minimizando la entropía cruzada entre las palabras originales y las reconstruidas:

$$\mathcal{L}_{\text{CE}} = -\frac{1}{L}\sum_{t=1}^{L} \log p(\hat{w}_t = w_t | \hat{w}_{<t}, \hat{\mathbf{z}})$$

Además, DeepSC incorpora una pérdida basada en información mutua para garantizar que la representación semántica transmitida capture la mayor cantidad posible de información relevante sobre el mensaje original. Esta pérdida adicional se puede formular como una cota inferior variacional de la información mutua $I(\mathbf{s}; \hat{\mathbf{z}})$, estimada mediante una red discriminadora auxiliar:

$$\mathcal{L}_{\text{MI}} = -\hat{I}(\mathbf{s}; \hat{\mathbf{z}})$$

La pérdida total es:

$$\mathcal{L} = \mathcal{L}_{\text{CE}} + \lambda \cdot \mathcal{L}_{\text{MI}}$$

donde $\lambda$ es un hiperparámetro que controla la importancia relativa de cada componente.

### 7.4.3 Los pesos de atención como codificación de importancia semántica

Una perspectiva particularmente reveladora es interpretar los pesos de atención del Transformer como una medida de la **importancia semántica** de cada parte del mensaje. En el contexto de comunicaciones semánticas, esta interpretación tiene implicaciones prácticas directas.

Consideremos una oración como: "El presidente anunció una nueva política económica en la conferencia de prensa." Los pesos de atención del codificador semántico asignarán diferentes niveles de importancia a cada palabra:

- "presidente", "anunció", "política", "económica" → alta atención (palabras con alto contenido semántico)
- "El", "una", "en", "la", "de" → baja atención (palabras funcionales con bajo contenido semántico)

Esta distribución de atención se refleja directamente en la representación semántica $\mathbf{z}$: las dimensiones del vector asociadas a conceptos semánticamente importantes tendrán magnitudes mayores, mientras que las asociadas a información redundante o poco relevante tendrán magnitudes menores. En condiciones de ruido, las componentes de mayor magnitud son más robustas a la corrupción, lo que significa que el sistema naturalmente protege más la información semántica importante.

Formalmente, si $\mathbf{A}^{(\ell)} \in \mathbb{R}^{L \times L}$ es la matriz de atención de la capa $\ell$, podemos definir un **vector de importancia semántica** como:

$$\mathbf{v}_{\text{imp}} = \frac{1}{N_e} \sum_{\ell=1}^{N_e} \text{diag}\left(\mathbf{A}^{(\ell)\top} \mathbf{1}\right)$$

donde $\mathbf{1}$ es un vector de unos. El elemento $v_{\text{imp},i}$ indica la importancia semántica promedio del token $i$ según los patrones de atención aprendidos. Tokens con alto $v_{\text{imp},i}$ son semánticamente más relevantes.

### 7.4.4 El "vector de atención" como representación semántica

En el paradigma de comunicaciones semánticas con Transformers, la representación semántica $\mathbf{z}$ puede conceptualizarse como un "vector de atención" — no en el sentido literal de los pesos de atención, sino en el sentido de que es un vector que ha sido moldeado por múltiples capas de operaciones de atención para capturar una representación rica, contextualizada y comprimida del significado del mensaje.

Este vector tiene propiedades notables:

1. **Composicionalidad**: el significado de una oración compleja se construye composicionalmente a partir de los significados de sus partes, reflejado en cómo cada capa de atención combina las representaciones de diferentes tokens.

2. **Invarianza a la paráfrasis**: oraciones con el mismo significado pero diferente formulación producen vectores semánticos cercanos en el espacio $\mathcal{Z}$, porque el Transformer ha aprendido a abstraer más allá de la forma superficial.

3. **Sensibilidad al contexto**: la misma palabra produce diferentes representaciones según su contexto, permitiendo la desambiguación automática.

4. **Compresibilidad**: la dimensión $d$ del vector semántico puede ser significativamente menor que la dimensión del mensaje original (medido en bits), logrando una compresión semántica efectiva.

**Figura 7.3:** *Arquitectura del sistema de comunicación semántica DeepSC basado en Transformers (Xie et al., 2021). El diagrama muestra el flujo de procesamiento para la transmisión semántica de texto. En el transmisor: la oración de entrada "El avión aterrizó en el aeropuerto" se tokeniza y convierte en embeddings; estos pasan por un Codificador Transformer de $N_e$ capas (cada una con auto-atención multi-cabeza, normalización de capa y red feed-forward) que produce las características semánticas $\mathbf{z}$; las características se procesan mediante un Codificador de Canal (capas densas con normalización de potencia) que genera los símbolos de canal $\mathbf{x}$. Los símbolos atraviesan el Canal (AWGN o Rayleigh, modelado como capa diferenciable). En el receptor: la señal recibida $\mathbf{y}$ pasa por el Decodificador de Canal (capas densas) que estima $\hat{\mathbf{z}}$; estas características alimentan un Decodificador Transformer de $N_d$ capas (con auto-atención enmascarada, atención cruzada con $\hat{\mathbf{z}}$, y red feed-forward) que genera autorregressivamente la oración reconstruida "El avión llegó al aeropuerto". Se muestra el flujo de gradientes de retropropagación a través de todo el sistema, incluyendo la capa de canal diferenciable.*

---

## 7.5 Ventajas de las comunicaciones semánticas

### 7.5.1 Eficiencia en el uso del ancho de banda

La ventaja más inmediata y quizás más impactante de las comunicaciones semánticas es la **reducción drástica en la cantidad de datos que es necesario transmitir**. Al transmitir el significado en lugar de la representación literal de los datos, se logra una compresión que va mucho más allá de lo que los algoritmos de compresión de datos clásicos pueden alcanzar.

Para cuantificar esta ventaja, definimos la **tasa de compresión semántica** como:

$$\eta_{\text{sem}} = \frac{|\mathbf{s}|_{\text{bits}}}{|\mathbf{x}|_{\text{símbolos}} \times \log_2 M}$$

donde $|\mathbf{s}|_{\text{bits}}$ es el tamaño del mensaje original en bits, $|\mathbf{x}|_{\text{símbolos}}$ es el número de símbolos de canal utilizados, y $M$ es el orden de la modulación. Una tasa de compresión alta indica que se están transmitiendo pocos símbolos en relación al tamaño del mensaje original.

Consideremos un ejemplo concreto. Una oración típica en español contiene alrededor de 15 palabras, cada una representada por un índice en un vocabulario de 50,000 palabras, lo que requiere $15 \times \lceil\log_2 50{,}000\rceil \approx 15 \times 16 = 240$ bits. En un sistema de comunicación semántica como DeepSC, la representación semántica podría consistir en $L \times d_c$ símbolos de canal reales, donde $d_c$ puede ser tan pequeño como 4 o 8. Si $L = 15$ y $d_c = 4$, se transmiten solo 60 valores reales. En comparación, un sistema clásico que transmite el texto codificado carácter por carácter (con codificación de canal y modulación) requeriría significativamente más símbolos de canal.

La eficiencia se amplifica para datos de alta dimensionalidad como imágenes o video. Una imagen de alta resolución requiere millones de bits para su representación literal, pero su "significado" puede capturarse en un vector semántico de unas pocas centenas de dimensiones.

### 7.5.2 Degradación gradual versus efecto precipicio

Como se mencionó en la Sección 7.1.3, los sistemas clásicos sufren el efecto precipicio: un colapso abrupto del rendimiento cuando la SNR cae por debajo de un umbral. Los sistemas de comunicación semántica, en contraste, exhiben una **degradación gradual** (*graceful degradation*).

Este comportamiento se debe a la naturaleza de la representación semántica. En un sistema clásico, el decodificador de canal intenta recuperar bits exactos. Si la tasa de errores supera la capacidad de corrección del código, la decodificación falla catastróficamente. En un sistema semántico, el decodificador de canal produce una estimación de la representación semántica que es continuamente perturbada por el ruido. El decodificador semántico (red neuronal) es tolerante a estas perturbaciones porque ha sido entrenado para reconstruir significado a partir de representaciones ruidosas.

Matemáticamente, si $\hat{\mathbf{z}} = \mathbf{z} + \boldsymbol{\epsilon}$ donde $\boldsymbol{\epsilon}$ es el ruido efectivo en el espacio semántico, la calidad de la reconstrucción depende continuamente de $||\boldsymbol{\epsilon}||$. Para ruido pequeño, la reconstrucción es casi perfecta. A medida que $||\boldsymbol{\epsilon}||$ crece, la calidad se degrada suavemente. No hay un umbral abrupto.

Los resultados experimentales de DeepSC (Xie et al., 2021) demuestran que a una SNR de 0 dB (donde los sistemas clásicos basados en codificación Huffman + Turbo codes + modulación BPSK prácticamente no funcionan), el sistema semántico aún logra una similitud semántica (medida por BLEU score) significativamente superior a cero. A -2 dB, el sistema clásico es completamente inoperante, mientras que el sistema semántico todavía puede transmitir el significado esencial del mensaje, aunque con menor fidelidad léxica.

### 7.5.3 Robustez al ruido del canal

La robustez de los sistemas semánticos se debe a una propiedad fundamental de las representaciones distribuidas (*distributed representations*) aprendidas por redes neuronales: **la información semántica está codificada de forma distribuida a lo largo de todo el vector**, no concentrada en bits individuales.

En un sistema clásico, cada bit transporta información específica. Si un bit de la imagen comprimida en JPEG está en error, un bloque de 8×8 píxeles puede corromperse completamente. En un sistema semántico, la información está distribuida: cada componente del vector semántico contribuye de forma parcial al significado total. Corromper una componente degrada ligeramente el significado global, pero no lo destruye.

Esta propiedad se puede formalizar utilizando la noción de **lipschitzianidad** del decodificador semántico. Si el decodificador $g_\phi$ es Lipschitz-continuo con constante $L_g$, entonces:

$$||g_\phi(\hat{\mathbf{z}}) - g_\phi(\mathbf{z})|| \leq L_g \cdot ||\hat{\mathbf{z}} - \mathbf{z}||$$

Esto garantiza que pequeñas perturbaciones en la representación semántica producen pequeños cambios en la salida. Las redes neuronales modernas con normalización de capa, funciones de activación suaves y regularización tienden a tener constantes de Lipschitz moderadas, lo que les confiere esta propiedad de robustez.

### 7.5.4 Orientación a la tarea

Los sistemas de comunicación semántica pueden optimizarse directamente para la tarea que el receptor necesita realizar, en lugar de optimizarse para la reconstrucción fiel de los datos. Esta optimización orientada a la tarea permite ganancias de eficiencia adicionales significativas.

Por ejemplo, en un sistema de monitorización remota donde un sensor de imagen transmite datos a un servidor que debe detectar incendios forestales, el sistema semántico puede ser entrenado con una función de pérdida que mide directamente la exactitud de detección de incendios:

$$\mathcal{L}_{\text{tarea}} = -\mathbb{E}\left[y^* \log \hat{y} + (1 - y^*) \log(1 - \hat{y})\right]$$

donde $y^* \in \{0, 1\}$ es la etiqueta real (incendio/no incendio) y $\hat{y}$ es la predicción del receptor basada en la representación semántica recibida. Este enfoque transmite solo la información relevante para la detección de incendios, ignorando detalles irrelevantes (la textura exacta de las nubes, la forma precisa de cada árbol), lo que reduce drásticamente la cantidad de datos a transmitir.

### 7.5.5 Compatibilidad con la visión de 6G

Las comunicaciones semánticas se alinean naturalmente con la visión de las redes de sexta generación (6G), que se espera que soporten:

- **Comunicaciones ultra-masivas**: miles de millones de dispositivos IoT generando enormes volúmenes de datos. Transmitir solo el significado reduce la carga en la red.
- **Comunicaciones de latencia ultra-baja**: la compresión semántica reduce la cantidad de datos a transmitir, disminuyendo la latencia.
- **Inteligencia ubicua**: los dispositivos incorporan capacidades de IA que permiten la extracción y reconstrucción semántica local.
- **Eficiencia energética extrema**: transmitir menos datos implica menor consumo energético.
- **Conectividad en escenarios extremos**: la robustez a baja SNR permite la comunicación en condiciones donde los sistemas clásicos fallan.

La integración de comunicaciones semánticas con otras tecnologías 6G como superficies inteligentes reconfigurables (RIS), redes de funciones de red virtualizadas (NFV), y computación en el borde (*edge computing*) promete crear un ecosistema de comunicaciones radicalmente más eficiente.

---

## 7.6 Métricas de evaluación semántica

### 7.6.1 Métricas tradicionales (sintácticas)

Las métricas de evaluación clásicas en sistemas de comunicación operan en el nivel sintáctico, midiendo la fidelidad de la transmisión a nivel de bits o símbolos:

**Tasa de error de bit (BER, *Bit Error Rate*):**

$$\text{BER} = \frac{\text{Número de bits erróneos}}{\text{Número total de bits transmitidos}}$$

El BER es la métrica más fundamental en comunicaciones digitales. Un BER de $10^{-3}$ significa que, en promedio, 1 de cada 1,000 bits se recibe incorrectamente. Los estándares de comunicación modernos (e.g., 5G NR) especifican requisitos de BER típicamente del orden de $10^{-5}$ a $10^{-6}$ para servicios de datos.

**Tasa de error de bloque (BLER, *Block Error Rate*):**

$$\text{BLER} = \frac{\text{Número de bloques con al menos un error}}{\text{Número total de bloques transmitidos}}$$

El BLER es más relevante en sistemas que utilizan codificación de canal basada en bloques, ya que un solo bit erróneo en un bloque codificado puede causar la decodificación incorrecta de todo el bloque.

**Relación señal a ruido pico (PSNR, *Peak Signal-to-Noise Ratio*):**

$$\text{PSNR} = 10 \log_{10}\left(\frac{\text{MAX}^2}{\text{MSE}}\right) \text{ dB}$$

donde $\text{MAX}$ es el valor máximo posible del píxel (e.g., 255 para imágenes de 8 bits) y $\text{MSE}$ es el error cuadrático medio entre la imagen original y la reconstruida:

$$\text{MSE} = \frac{1}{M \times N}\sum_{i=1}^{M}\sum_{j=1}^{N}(I(i,j) - \hat{I}(i,j))^2$$

El PSNR es ampliamente utilizado para evaluar la calidad de imágenes reconstruidas. Valores típicos son 30-50 dB para una buena calidad. Sin embargo, el PSNR tiene una limitación fundamental: no se correlaciona bien con la percepción humana de calidad. Una imagen puede tener un PSNR alto pero ser visualmente insatisfactoria, y viceversa.

**Índice de similitud estructural (SSIM, *Structural Similarity Index*):**

$$\text{SSIM}(\mathbf{x}, \mathbf{y}) = \frac{(2\mu_x\mu_y + c_1)(2\sigma_{xy} + c_2)}{(\mu_x^2 + \mu_y^2 + c_1)(\sigma_x^2 + \sigma_y^2 + c_2)}$$

donde $\mu_x$ y $\mu_y$ son las medias, $\sigma_x^2$ y $\sigma_y^2$ son las varianzas, $\sigma_{xy}$ es la covarianza, y $c_1$, $c_2$ son constantes de estabilización. El SSIM evalúa la similitud estructural entre dos imágenes considerando luminancia, contraste y estructura, proporcionando una evaluación más alineada con la percepción humana que el PSNR. Sus valores van de -1 a 1, donde 1 indica imágenes idénticas.

### 7.6.2 Métricas semánticas

Las comunicaciones semánticas requieren métricas que evalúen la preservación del *significado*, no la fidelidad de los bits o los píxeles. Estas métricas operan en el espacio semántico y miden cuánto del significado original se preserva en la reconstrucción.

**BLEU (*Bilingual Evaluation Understudy*) para texto:**

El puntaje BLEU mide la superposición de n-gramas entre el texto generado y el texto de referencia. Se define como:

$$\text{BLEU} = \text{BP} \cdot \exp\left(\sum_{n=1}^{N} w_n \log p_n\right)$$

donde $p_n$ es la precisión de n-gramas modificada (la fracción de n-gramas en el texto generado que aparecen en la referencia, con recuento recortado para evitar repeticiones), $w_n = 1/N$ son pesos uniformes (típicamente $N = 4$), y $\text{BP}$ es una penalización por brevedad:

$$\text{BP} = \begin{cases} 1 & \text{si } c > r \\ e^{1 - r/c} & \text{si } c \leq r \end{cases}$$

donde $c$ es la longitud del texto generado y $r$ es la longitud de referencia. El BLEU varía de 0 a 1 y es una métrica parcialmente semántica: captura la superposición léxica, que se correlaciona con la similitud semántica, pero no captura sinónimos ni paráfrasis.

**ROUGE (*Recall-Oriented Understudy for Gisting Evaluation*) para texto:**

ROUGE es una familia de métricas que miden la superposición entre el texto generado y la referencia, enfocándose en el recall (cobertura) en lugar de la precisión. ROUGE-L, basado en la subsecuencia común más larga (*Longest Common Subsequence*, LCS), es particularmente útil:

$$\text{ROUGE-L} = \frac{(1 + \beta^2) \cdot R_{\text{LCS}} \cdot P_{\text{LCS}}}{R_{\text{LCS}} + \beta^2 \cdot P_{\text{LCS}}}$$

donde $R_{\text{LCS}} = \text{LCS}(X, Y) / |Y|$ es el recall basado en LCS, $P_{\text{LCS}} = \text{LCS}(X, Y) / |X|$ es la precisión basada en LCS, y $\beta$ controla la importancia relativa del recall sobre la precisión.

**Similitud semántica por coseno en espacio de embeddings:**

Quizás la métrica más directa para evaluar la preservación semántica es la **similitud coseno** entre las representaciones vectoriales (*embeddings*) del texto original y el reconstruido:

$$\text{sim}(\mathbf{a}, \mathbf{b}) = \frac{\mathbf{a} \cdot \mathbf{b}}{||\mathbf{a}|| \, ||\mathbf{b}||}$$

donde $\mathbf{a}, \mathbf{b} \in \mathbb{R}^d$ son los embeddings del texto original y reconstruido, obtenidos mediante un modelo pre-entrenado (e.g., Sentence-BERT). Esta métrica varía de -1 a 1, donde 1 indica significado idéntico, 0 indica ausencia de relación semántica, y -1 indica significados opuestos.

La similitud coseno tiene la propiedad deseable de ser independiente de la magnitud de los vectores y depender solo de su dirección en el espacio semántico. Esto la hace robusta a variaciones en la escala de las representaciones y permite comparaciones significativas entre textos de diferente longitud.

Para comprender por qué esta métrica es adecuada, recordemos que en un espacio de embeddings bien entrenado, las direcciones codifican relaciones semánticas. Dos vectores con alta similitud coseno apuntan aproximadamente en la misma dirección, lo que significa que capturan el mismo concepto semántico, incluso si las palabras utilizadas son diferentes.

**Tasa de éxito de la tarea:**

Para comunicaciones orientadas a tareas, la métrica más relevante es la **tasa de éxito de la tarea**:

$$\text{TSR} = \frac{\text{Número de tareas completadas exitosamente}}{\text{Número total de tareas intentadas}}$$

Esta métrica evalúa directamente el Nivel C de Weaver: ¿el receptor tomó la acción correcta? Es la métrica más pragmática y la más directamente útil en aplicaciones reales, pero requiere definir claramente qué constituye un "éxito" en la tarea específica.

**Tasa semántica:**

La **tasa semántica** (*semantic rate*) cuantifica la cantidad de significado transmitido por uso del canal:

$$R_{\text{sem}} = \frac{\text{Información semántica transmitida}}{\text{Número de usos del canal}}$$

La cuantificación precisa de la "información semántica transmitida" es un desafío abierto. Una aproximación práctica consiste en definirla como la información mutua semántica $I_{\text{sem}}(S; \hat{S})$, estimada mediante técnicas variacionales o basadas en embeddings. Otra aproximación utiliza la reducción en la entropía semántica del receptor:

$$R_{\text{sem}} = \frac{H_{\text{sem}}(S) - H_{\text{sem}}(S | \hat{S})}{k}$$

donde $k$ es el número de usos del canal. Esta definición captura intuitivamente la idea de "bits de significado por uso del canal".

### 7.6.3 Comparación entre métricas clásicas y semánticas

La siguiente tabla resume las diferencias fundamentales entre las métricas clásicas y semánticas:

| Aspecto | Métricas clásicas (BER, PSNR) | Métricas semánticas (similitud coseno, BLEU) |
|---|---|---|
| Nivel de Weaver | Nivel A (técnico) | Nivel B (semántico) / Nivel C (efectividad) |
| Objeto de medición | Fidelidad de bits/píxeles | Preservación de significado |
| Sensibilidad a sinónimos | Penaliza palabras diferentes | Reconoce significados equivalentes |
| Correlación con percepción humana | Moderada (PSNR) a baja (BER) | Alta |
| Aplicabilidad | Universal | Depende de la modalidad y tarea |
| Complejidad computacional | Baja | Moderada a alta |
| Necesidad de modelo auxiliar | No | Sí (modelo de embeddings) |

---

## 7.7 Ejemplo conceptual: transmisión semántica de texto

### 7.7.1 Descripción del ejemplo paso a paso

Para consolidar los conceptos presentados en esta sección, desarrollemos un ejemplo completo y detallado de transmisión semántica de texto, siguiendo cada etapa del procesamiento desde la fuente hasta el destino.

**Paso 1: Oración de entrada**

Consideremos la oración en español:

> "El avión aterrizó en el aeropuerto"

Esta oración contiene 6 tokens principales (excluyendo artículos como entrada independiente, o considerando subpalabras según el tokenizador). En un sistema con un vocabulario de 30,000 palabras, cada token se representa como un índice entero. La representación sintáctica (bit a bit) de esta oración requeriría aproximadamente $6 \times \lceil\log_2 30{,}000\rceil \approx 6 \times 15 = 90$ bits.

**Paso 2: Codificación semántica (Codificador Transformer)**

El codificador semántico, basado en un Transformer, procesa la oración de la siguiente manera:

a) *Tokenización y embedding*: Cada palabra se convierte en un vector de embedding de dimensión $d_{\text{model}} = 128$:

$$\mathbf{e}_1 = \text{Embed}(\text{"El"}), \quad \mathbf{e}_2 = \text{Embed}(\text{"avión"}), \quad \ldots, \quad \mathbf{e}_6 = \text{Embed}(\text{"aeropuerto"})$$

b) *Codificación posicional*: Se añade información posicional para que el modelo distinga el orden de las palabras:

$$\mathbf{h}_i^{(0)} = \mathbf{e}_i + \mathbf{PE}_i, \quad i = 1, \ldots, 6$$

c) *Capas del Transformer*: Los vectores pasan por $N_e = 4$ capas de codificador Transformer. En cada capa, el mecanismo de auto-atención permite que cada palabra atienda a todas las demás, construyendo progresivamente una representación más rica y contextualizada.

Después del procesamiento, la representación semántica de la oración es un conjunto de vectores $\mathbf{z} = \{\mathbf{z}_1, \ldots, \mathbf{z}_6\} \in \mathbb{R}^{6 \times d_z}$, donde $d_z = 16$ (la dimensión de la representación semántica por token, significativamente menor que $d_{\text{model}} = 128$, lo que implica una compresión de 8:1).

El vector semántico de la palabra "aterrizó" capturará no solo su significado léxico sino también su contexto: que el sujeto es un "avión" y que el destino es un "aeropuerto". Esta contextualización es la esencia de lo que hace que la representación sea *semántica* y no meramente *léxica*.

**Paso 3: Codificación de canal**

El codificador de canal transforma la representación semántica en símbolos adecuados para la transmisión:

$$\mathbf{x} = \text{ChEnc}(\mathbf{z}) \in \mathbb{R}^{k}$$

donde $k = 6 \times d_c$ y $d_c = 8$ es el número de símbolos de canal por token, resultando en $k = 48$ símbolos de canal reales. Estos se normalizan para satisfacer la restricción de potencia:

$$\mathbf{x} \leftarrow \sqrt{k} \cdot \frac{\mathbf{x}}{||\mathbf{x}||}$$

La cantidad total de información transmitida es de 48 valores reales. Si cada valor se cuantiza a 16 bits de punto flotante (half precision), esto corresponde a $48 \times 16 = 768$ bits. Sin embargo, en la transmisión analógica (como en los sistemas de comunicación semántica), los valores se transmiten como amplitudes continuas sin cuantización explícita, y la precisión efectiva depende de la SNR del canal.

**Paso 4: Canal AWGN**

La señal transmitida atraviesa un canal AWGN con $\text{SNR} = 7$ dB:

$$\mathbf{y} = \mathbf{x} + \mathbf{n}, \quad \mathbf{n} \sim \mathcal{N}(\mathbf{0}, \sigma_n^2 \mathbf{I})$$

donde $\sigma_n^2 = P_x / \text{SNR}_{\text{lineal}} = 1 / 10^{0.7} \approx 0.2$. Cada componente de la señal transmitida es perturbada por ruido gaussiano independiente con varianza 0.2 (desviación estándar ≈ 0.45).

**Paso 5: Decodificación de canal**

El decodificador de canal produce una estimación de la representación semántica:

$$\hat{\mathbf{z}} = \text{ChDec}(\mathbf{y})$$

Las capas densas del decodificador de canal han sido entrenadas para compensar los efectos del ruido, produciendo una estimación $\hat{\mathbf{z}}$ que es cercana a $\mathbf{z}$ pero no idéntica. El error de estimación $\boldsymbol{\epsilon} = \hat{\mathbf{z}} - \mathbf{z}$ depende del nivel de ruido y de la calidad del entrenamiento.

**Paso 6: Decodificación semántica (Decodificador Transformer)**

El decodificador Transformer genera la oración reconstruida de forma autorregresiva, token por token:

$$p(\hat{w}_t | \hat{w}_1, \ldots, \hat{w}_{t-1}, \hat{\mathbf{z}})$$

Para cada posición $t$, el decodificador calcula una distribución de probabilidad sobre todo el vocabulario y selecciona la palabra más probable (o utiliza *beam search* para explorar múltiples candidatos).

El resultado podría ser:

> "El avión llegó al aeropuerto"

Observemos que la oración reconstruida no es idéntica a la original: "aterrizó" ha sido reemplazado por "llegó" y "en el" por "al". Sin embargo, el *significado* se ha preservado casi perfectamente. El hecho de que un avión llegó/aterrizó en un aeropuerto se ha comunicado correctamente.

**Paso 7: Evaluación**

Evaluemos la calidad de la transmisión con diferentes métricas:

*Métricas sintácticas:*
- A nivel de caracteres, hay múltiples diferencias → BER relativamente alto.
- Si comparamos palabra por palabra: 4 de 6 palabras son diferentes ("aterrizó"→"llegó", "en"→"al", "el"→ ∅) → tasa de error de palabra del ~50%.

*Métricas semánticas:*
- Si usamos un modelo de embeddings para calcular los vectores semánticos $\mathbf{a}$ (original) y $\mathbf{b}$ (reconstruido), obtenemos:

$$\text{sim}(\mathbf{a}, \mathbf{b}) = \frac{\mathbf{a} \cdot \mathbf{b}}{||\mathbf{a}|| \, ||\mathbf{b}||} \approx 0.95$$

Una similitud coseno de 0.95 indica una excelente preservación del significado. El sistema clásico reportaría un "fallo" (alta tasa de error), mientras que el sistema semántico reporta un "éxito" (alta similitud semántica).

Este ejemplo ilustra de manera poderosa la diferencia fundamental entre los paradigmas: **en comunicaciones semánticas, la fidelidad de las palabras es secundaria; lo que importa es la fidelidad del significado**.

### 7.7.2 Pseudocódigo en PyTorch

A continuación presentamos un pseudocódigo en PyTorch que implementa la arquitectura conceptual del sistema de comunicación semántica descrito. Este código es pedagógico y tiene como objetivo ilustrar la estructura y el flujo de datos del sistema; una implementación de producción requeriría optimizaciones adicionales, manejo de vocabulario más sofisticado, y entrenamiento con datasets extensos.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
import math

# ============================================================
# Componentes del sistema de comunicación semántica
# ============================================================

class SemanticEncoder(nn.Module):
    """
    Codificador semántico basado en Transformer.
    Extrae características semánticas del texto de entrada.
    """
    def __init__(self, vocab_size, d_model=128, nhead=8,
                 num_layers=4, d_semantic=16):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, d_model)
        self.pos_encoder = PositionalEncoding(d_model)
        encoder_layer = nn.TransformerEncoderLayer(
            d_model=d_model, nhead=nhead,
            dim_feedforward=4*d_model, batch_first=True
        )
        self.transformer_encoder = nn.TransformerEncoder(
            encoder_layer, num_layers=num_layers
        )
        # Proyección a espacio semántico compacto
        self.semantic_proj = nn.Linear(d_model, d_semantic)

    def forward(self, src, src_mask=None):
        # src: (batch, seq_len) índices de tokens
        x = self.embedding(src)           # (batch, seq_len, d_model)
        x = self.pos_encoder(x)
        x = self.transformer_encoder(x, src_key_padding_mask=src_mask)
        z = self.semantic_proj(x)          # (batch, seq_len, d_semantic)
        return z


class ChannelEncoder(nn.Module):
    """
    Codificador de canal: mapea la representación semántica
    a símbolos de canal con normalización de potencia.
    """
    def __init__(self, d_semantic=16, d_channel=8):
        super().__init__()
        self.fc = nn.Sequential(
            nn.Linear(d_semantic, d_semantic),
            nn.ReLU(),
            nn.Linear(d_semantic, d_channel)
        )

    def forward(self, z):
        # z: (batch, seq_len, d_semantic)
        x = self.fc(z)                    # (batch, seq_len, d_channel)
        # Normalización de potencia
        x_flat = x.reshape(x.size(0), -1)
        power = torch.sqrt(torch.mean(x_flat**2, dim=-1, keepdim=True))
        x_flat = x_flat / (power + 1e-8)
        x = x_flat.reshape(x.shape)
        return x


class AWGNChannel(nn.Module):
    """
    Canal AWGN diferenciable.
    Añade ruido gaussiano según la SNR especificada.
    """
    def __init__(self):
        super().__init__()

    def forward(self, x, snr_db):
        if not self.training:
            snr_db = snr_db
        snr_linear = 10 ** (snr_db / 10.0)
        # Potencia de la señal normalizada a 1
        noise_power = 1.0 / snr_linear
        noise = torch.randn_like(x) * math.sqrt(noise_power)
        return x + noise


class RayleighChannel(nn.Module):
    """
    Canal de desvanecimiento Rayleigh diferenciable.
    Aplica desvanecimiento multiplicativo y ruido aditivo.
    """
    def __init__(self):
        super().__init__()

    def forward(self, x, snr_db):
        snr_linear = 10 ** (snr_db / 10.0)
        noise_power = 1.0 / snr_linear
        # Coeficientes de desvanecimiento Rayleigh
        h_real = torch.randn_like(x) / math.sqrt(2)
        h_imag = torch.randn_like(x) / math.sqrt(2)
        h_mag = torch.sqrt(h_real**2 + h_imag**2)
        # Señal desvanecida + ruido
        noise = torch.randn_like(x) * math.sqrt(noise_power)
        y = h_mag * x + noise
        return y


class ChannelDecoder(nn.Module):
    """
    Decodificador de canal: estima la representación
    semántica a partir de la señal recibida.
    """
    def __init__(self, d_channel=8, d_semantic=16):
        super().__init__()
        self.fc = nn.Sequential(
            nn.Linear(d_channel, d_semantic),
            nn.ReLU(),
            nn.Linear(d_semantic, d_semantic)
        )

    def forward(self, y):
        # y: (batch, seq_len, d_channel)
        z_hat = self.fc(y)               # (batch, seq_len, d_semantic)
        return z_hat


class SemanticDecoder(nn.Module):
    """
    Decodificador semántico basado en Transformer.
    Reconstruye el texto a partir de la representación
    semántica estimada.
    """
    def __init__(self, vocab_size, d_model=128, nhead=8,
                 num_layers=4, d_semantic=16):
        super().__init__()
        self.semantic_to_model = nn.Linear(d_semantic, d_model)
        decoder_layer = nn.TransformerDecoderLayer(
            d_model=d_model, nhead=nhead,
            dim_feedforward=4*d_model, batch_first=True
        )
        self.transformer_decoder = nn.TransformerDecoder(
            decoder_layer, num_layers=num_layers
        )
        self.output_proj = nn.Linear(d_model, vocab_size)

    def forward(self, z_hat, tgt_emb):
        # z_hat: (batch, seq_len, d_semantic) - memoria del decoder
        # tgt_emb: (batch, seq_len, d_model) - embeddings del target
        memory = self.semantic_to_model(z_hat)
        # Máscara causal para generación autorregresiva
        tgt_len = tgt_emb.size(1)
        tgt_mask = torch.triu(
            torch.ones(tgt_len, tgt_len, device=tgt_emb.device),
            diagonal=1
        ).bool()
        output = self.transformer_decoder(
            tgt_emb, memory, tgt_mask=tgt_mask
        )
        logits = self.output_proj(output)  # (batch, seq_len, vocab_size)
        return logits


class PositionalEncoding(nn.Module):
    """Codificación posicional sinusoidal."""
    def __init__(self, d_model, max_len=512):
        super().__init__()
        pe = torch.zeros(max_len, d_model)
        position = torch.arange(0, max_len).unsqueeze(1).float()
        div_term = torch.exp(
            torch.arange(0, d_model, 2).float()
            * (-math.log(10000.0) / d_model)
        )
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)
        self.register_buffer('pe', pe.unsqueeze(0))

    def forward(self, x):
        return x + self.pe[:, :x.size(1), :]


# ============================================================
# Sistema completo de comunicación semántica
# ============================================================

class SemanticCommSystem(nn.Module):
    """
    Sistema de comunicación semántica de extremo a extremo.
    Integra codificador semántico, codificador/decodificador
    de canal, canal físico, y decodificador semántico.
    """
    def __init__(self, vocab_size, d_model=128, nhead=8,
                 num_enc_layers=4, num_dec_layers=4,
                 d_semantic=16, d_channel=8,
                 channel_type='awgn'):
        super().__init__()
        self.sem_encoder = SemanticEncoder(
            vocab_size, d_model, nhead,
            num_enc_layers, d_semantic
        )
        self.ch_encoder = ChannelEncoder(d_semantic, d_channel)

        if channel_type == 'awgn':
            self.channel = AWGNChannel()
        elif channel_type == 'rayleigh':
            self.channel = RayleighChannel()

        self.ch_decoder = ChannelDecoder(d_channel, d_semantic)
        self.sem_decoder = SemanticDecoder(
            vocab_size, d_model, nhead,
            num_dec_layers, d_semantic
        )
        self.embedding = self.sem_encoder.embedding
        self.pos_encoder = self.sem_encoder.pos_encoder

    def forward(self, src, tgt, snr_db, src_mask=None):
        # --- Transmisor ---
        z = self.sem_encoder(src, src_mask)     # Codificación semántica
        x = self.ch_encoder(z)                   # Codificación de canal

        # --- Canal ---
        y = self.channel(x, snr_db)              # Canal físico

        # --- Receptor ---
        z_hat = self.ch_decoder(y)               # Decodificación de canal
        tgt_emb = self.pos_encoder(
            self.embedding(tgt)
        )
        logits = self.sem_decoder(z_hat, tgt_emb) # Decodificación semántica
        return logits


# ============================================================
# Ejemplo de uso: entrenamiento y evaluación
# ============================================================

def train_step(model, optimizer, src, tgt, snr_db):
    """Un paso de entrenamiento del sistema semántico."""
    model.train()
    optimizer.zero_grad()

    # Forward pass: tgt_input excluye último token,
    # tgt_output excluye primer token (teacher forcing)
    tgt_input = tgt[:, :-1]
    tgt_output = tgt[:, 1:]

    logits = model(src, tgt_input, snr_db)

    # Pérdida de entropía cruzada (semántica)
    loss = F.cross_entropy(
        logits.reshape(-1, logits.size(-1)),
        tgt_output.reshape(-1),
        ignore_index=0  # Ignorar padding
    )

    loss.backward()  # Retropropagación E2E
    optimizer.step()
    return loss.item()


def evaluate_semantic_similarity(original_emb, reconstructed_emb):
    """
    Calcula la similitud coseno entre embeddings
    del texto original y reconstruido.
    """
    cos_sim = F.cosine_similarity(
        original_emb, reconstructed_emb, dim=-1
    )
    return cos_sim.mean().item()


# --- Simulación conceptual ---
if __name__ == "__main__":
    VOCAB_SIZE = 30000
    model = SemanticCommSystem(
        vocab_size=VOCAB_SIZE,
        d_model=128, nhead=8,
        num_enc_layers=4, num_dec_layers=4,
        d_semantic=16, d_channel=8,
        channel_type='awgn'
    )
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-4)

    # Simulación con datos ficticios
    batch_size = 32
    seq_len = 10
    src = torch.randint(1, VOCAB_SIZE, (batch_size, seq_len))
    tgt = torch.randint(1, VOCAB_SIZE, (batch_size, seq_len))

    # Entrenar a diferentes SNR para robustez
    for epoch in range(100):
        snr_db = torch.FloatTensor(1).uniform_(0, 20).item()
        loss = train_step(model, optimizer, src, tgt, snr_db)
        if (epoch + 1) % 10 == 0:
            print(f"Epoch {epoch+1}, SNR={snr_db:.1f} dB, "
                  f"Loss={loss:.4f}")
```

### 7.7.3 Análisis del ejemplo

Este ejemplo ilustra varios puntos fundamentales:

**1. Compresión semántica.** La oración original de 6 tokens, cada uno con un embedding de dimensión 128, se comprime a una representación semántica de 6 vectores de dimensión 16 (compresión 8:1). El codificador de canal la transforma en $6 \times 8 = 48$ símbolos de canal. En un sistema clásico, los 90 bits de la oración, con codificación de canal a tasa 1/2 y modulación BPSK, requerirían 180 símbolos de canal. El sistema semántico logra una reducción significativa.

**2. Diferenciabilidad del canal.** El canal AWGN se implementa como una simple adición de ruido gaussiano, que es una operación diferenciable. Esto permite que los gradientes fluyan a través del canal durante el entrenamiento, haciendo posible la optimización de extremo a extremo. Durante la retropropagación, el gradiente de la pérdida con respecto a los símbolos transmitidos $\mathbf{x}$ es simplemente $\partial \mathcal{L}/\partial \mathbf{x} = \partial \mathcal{L}/\partial \mathbf{y}$, ya que $\mathbf{y} = \mathbf{x} + \mathbf{n}$ y el ruido $\mathbf{n}$ no depende de $\mathbf{x}$.

**3. Robustez a diferentes SNR.** El sistema se entrena con valores de SNR aleatorios en cada epoch (entre 0 y 20 dB), lo que le confiere robustez a un amplio rango de condiciones de canal. Esta estrategia de entrenamiento, conocida como *curriculum training* o entrenamiento con SNR variable, es una técnica común en comunicaciones semánticas que permite que un único modelo funcione bien en diferentes condiciones sin necesidad de adaptación.

**4. Preservación semántica vs. fidelidad léxica.** El decodificador semántico genera palabras secuencialmente, seleccionando en cada paso la palabra más probable dado el contexto. Esto puede resultar en paráfrasis: "aterrizó" → "llegó", una sustitución que preserva el significado pero cambia la forma léxica. Las métricas semánticas (similitud coseno) reflejan correctamente esta preservación, mientras que las métricas léxicas (BER, tasa de error de palabra) la penalizarían.

**5. Entrenamiento de extremo a extremo.** Todos los componentes — codificador semántico, codificador de canal, canal, decodificador de canal, decodificador semántico — forman un único grafo computacional. La función de pérdida (entropía cruzada) se calcula al final del sistema, y los gradientes se propagan hacia atrás a través de todos los módulos. No hay optimización separada de cada bloque; el sistema se optimiza como un todo, permitiendo que cada componente se adapte a los demás de forma sinérgica.

---

## Referencias

1. Shannon, C. E. (1948). "A Mathematical Theory of Communication." *The Bell System Technical Journal*, 27(3), 379–423.

2. Weaver, W. (1949). "Recent Contributions to the Mathematical Theory of Communication." En C. E. Shannon y W. Weaver, *The Mathematical Theory of Communication*. University of Illinois Press.

3. Xie, H., Qin, Z., Li, G. Y., y Juang, B.-H. (2021). "Deep Learning Enabled Semantic Communication Systems." *IEEE Transactions on Signal Processing*, 69, 2663–2675. DOI: [10.1109/TSP.2021.3071082](https://doi.org/10.1109/TSP.2021.3071082).

4. Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., y Polosukhin, I. (2017). "Attention Is All You Need." *Advances in Neural Information Processing Systems (NeurIPS)*, 30.

---

# 8. Sistemas de Comunicación Semántica de Extremo a Extremo (E2E)

Los capítulos anteriores han establecido los fundamentos teóricos del aprendizaje profundo, la teoría de la información semántica y las arquitecturas neuronales que constituyen los bloques de construcción de los sistemas modernos de comunicación. En esta sección, integramos todos estos componentes para presentar el diseño, entrenamiento y operación de **sistemas de comunicación semántica de extremo a extremo** (*End-to-End Semantic Communication Systems*, E2E SemCom). A diferencia de los sistemas de comunicación convencionales —donde la codificación de fuente, la codificación de canal y la modulación se diseñan y optimizan por separado—, los sistemas E2E proponen un paradigma radicalmente distinto: **todas las etapas del transmisor y receptor se entrenan conjuntamente como una única red neuronal**, optimizando directamente una métrica de fidelidad semántica a nivel de significado, en lugar de minimizar la tasa de error de bit.

Este enfoque, inspirado en los autoencoders profundos y catalizado por los avances en redes neuronales diferenciables, permite que el sistema aprenda representaciones intermedias que no corresponden necesariamente a símbolos discretos de una constelación clásica, sino a **vectores latentes semánticos** optimizados para sobrevivir las distorsiones del canal físico manteniendo el contenido semántico relevante. El resultado es un sistema que exhibe propiedades notablemente superiores a los sistemas convencionales, incluyendo degradación suave en lugar del efecto acantilado, compresión adaptativa del contenido semántico, y robustez intrínseca al ruido del canal.

A lo largo de esta sección, desarrollaremos cada componente con rigor matemático, proporcionaremos descripciones detalladas de las arquitecturas, analizaremos las funciones de pérdida apropiadas para distintas modalidades de datos, y culminaremos con una implementación completa en PyTorch que el lector podrá utilizar como punto de partida para sus propias investigaciones.

---

## 8.1 Arquitectura E2E: Encoder Semántico-Canal (Transmisor)

### 8.1.1 Visión general del transmisor semántico

El transmisor en un sistema de comunicación semántica E2E tiene una función fundamentalmente diferente a la de un transmisor convencional. En un sistema clásico, el transmisor realiza secuencialmente tres operaciones independientes: (1) la codificación de fuente, que comprime los datos eliminando redundancia estadística (por ejemplo, mediante algoritmos como Huffman, Lempel-Ziv o transformadas como la DCT en JPEG); (2) la codificación de canal, que añade redundancia controlada para proteger contra errores del canal (mediante códigos como Turbo, LDPC o Polar); y (3) la modulación, que mapea los bits codificados a símbolos de una constelación (como QAM o PSK) aptos para la transmisión por el medio físico. Cada una de estas etapas se diseña aplicando el teorema de separación fuente-canal de Shannon, que garantiza que la optimización independiente es óptima asintóticamente.

Sin embargo, el teorema de separación de Shannon se aplica bajo condiciones idealizadas: longitud de bloque infinita, distribuciones estacionarias y ergódicas, y sin restricciones de complejidad. En la práctica, con longitudes de bloque finitas, datos no estacionarios (como texto, imágenes o video) y requisitos de latencia estrictos, la separación es subóptima. Los sistemas E2E explotan esta observación al **fusionar todas las etapas del transmisor en una única red neuronal** que aprende simultáneamente a extraer significado, comprimir la información semántica relevante y codificarla de manera robusta para su transmisión por el canal.

### 8.1.2 El encoder semántico

El **encoder semántico** es la primera etapa del transmisor. Su función es transformar los datos de origen $\mathbf{s}$ en una representación latente semántica $\mathbf{h}$ que capture el significado esencial del mensaje, descartando la información irrelevante o redundante desde el punto de vista de la tarea comunicativa. Formalmente, el encoder semántico se define como una función parametrizada:

$$\mathbf{h} = f_{\theta_{se}}(\mathbf{s})$$

donde $\mathbf{s} \in \mathcal{S}$ es el dato de origen (que puede ser un texto, una imagen, una señal de audio, etc.), $f_{\theta_{se}}$ es la función de codificación semántica implementada por una red neuronal con parámetros $\theta_{se}$, y $\mathbf{h} \in \mathbb{R}^{k}$ es el vector de características semánticas de dimensión $k$.

La arquitectura del encoder semántico depende de la modalidad de los datos de entrada. Para **datos textuales**, la arquitectura dominante es el Transformer, que utiliza mecanismos de auto-atención (*self-attention*) para capturar dependencias a largo plazo entre las palabras de la oración. El texto de entrada se tokeniza primero en una secuencia de tokens $\mathbf{s} = (s_1, s_2, \ldots, s_L)$, donde $L$ es la longitud de la secuencia. Cada token $s_i$ se mapea a un vector de *embedding* $\mathbf{e}_i \in \mathbb{R}^{d_{model}}$ mediante una matriz de *embeddings* $\mathbf{E} \in \mathbb{R}^{|V| \times d_{model}}$, donde $|V|$ es el tamaño del vocabulario. A estos *embeddings* se les añade la codificación posicional:

$$\mathbf{e}_i' = \mathbf{e}_i + \mathbf{PE}(i)$$

donde $\mathbf{PE}(i)$ es el vector de codificación posicional para la posición $i$, típicamente definido mediante funciones sinusoidales:

$$\text{PE}(i, 2j) = \sin\left(\frac{i}{10000^{2j/d_{model}}}\right), \quad \text{PE}(i, 2j+1) = \cos\left(\frac{i}{10000^{2j/d_{model}}}\right)$$

La secuencia de *embeddings* con posición $(\mathbf{e}_1', \mathbf{e}_2', \ldots, \mathbf{e}_L')$ se procesa a través de $N_{se}$ capas de Transformer encoder, cada una de las cuales aplica:

$$\mathbf{H}^{(l)} = \text{TransformerLayer}^{(l)}(\mathbf{H}^{(l-1)})$$

donde cada capa consiste en auto-atención multi-cabeza seguida de una red *feed-forward* con conexiones residuales y normalización de capa. La salida final $\mathbf{H}^{(N_{se})}$ es una representación contextualizada de la secuencia completa.

Para **datos de imagen**, el encoder semántico típicamente emplea una arquitectura de red neuronal convolucional (CNN), como una ResNet o una red similar, que progresivamente reduce la resolución espacial mientras incrementa la profundidad de canales de características. La imagen de entrada $\mathbf{s} \in \mathbb{R}^{H \times W \times C}$ se transforma en un mapa de características $\mathbf{h} \in \mathbb{R}^{H' \times W' \times C'}$ donde $H' \ll H$, $W' \ll W$ y $C' \gg C$. Alternativamente, arquitecturas más recientes emplean Vision Transformers (ViT), que dividen la imagen en parches y los procesan con capas de Transformer.

### 8.1.3 El encoder de canal

El **encoder de canal** toma la representación semántica $\mathbf{h}$ producida por el encoder semántico y la transforma en un vector de símbolos de canal $\mathbf{z}$ adecuado para la transmisión por el medio físico. Formalmente:

$$\mathbf{z} = f_{\theta_{ce}}(\mathbf{h})$$

donde $f_{\theta_{ce}}$ es la función de codificación de canal implementada por una red neuronal con parámetros $\theta_{ce}$, y $\mathbf{z} \in \mathbb{R}^{2n}$ es el vector de símbolos de canal (donde el factor 2 aparece porque cada símbolo complejo se representa como dos valores reales: parte real e imaginaria, o bien I y Q en cuadratura).

La arquitectura del encoder de canal consiste típicamente en una o más **capas densas** (*fully connected layers*) que mapean el espacio semántico al espacio de símbolos de canal. Cada capa realiza la operación:

$$\mathbf{z}^{(l)} = \sigma\left(\mathbf{W}^{(l)} \mathbf{z}^{(l-1)} + \mathbf{b}^{(l)}\right)$$

donde $\mathbf{W}^{(l)}$ y $\mathbf{b}^{(l)}$ son los pesos y sesgos de la capa $l$, y $\sigma(\cdot)$ es una función de activación no lineal (típicamente ReLU o GELU para capas intermedias). La última capa no utiliza función de activación, permitiendo que los símbolos de salida tomen cualquier valor real.

### 8.1.4 Diseño conjunto y formulación compuesta

La operación completa del transmisor se expresa como la composición de ambos encoders:

$$\mathbf{z} = f_{\theta_{ce}}\left(f_{\theta_{se}}(\mathbf{s})\right)$$

Esta formulación enfatiza que el transmisor completo es una única función diferenciable parametrizada por $\theta_{tx} = \{\theta_{se}, \theta_{ce}\}$. La clave del diseño E2E es que **no existe una interfaz de bits entre el encoder semántico y el encoder de canal**: la representación intermedia $\mathbf{h}$ es un vector de valores reales continuos, no una secuencia de bits. Esto permite que la información fluya de manera más eficiente entre las etapas y que los gradientes se propaguen sin obstáculos durante el entrenamiento.

Esta ausencia de la interfaz binaria tradicional es, simultáneamente, una de las mayores fortalezas y uno de los desafíos más significativos de los sistemas E2E. La fortaleza radica en que elimina la pérdida de información inherente a la cuantización y permite una optimización verdaderamente conjunta. El desafío es que rompe la compatibilidad con los estándares de comunicación existentes y dificulta la interoperabilidad con otros sistemas.

### 8.1.5 Normalización de potencia

Para que los símbolos transmitidos $\mathbf{z}$ sean físicamente realizables, es necesario imponer una **restricción de potencia** que limite la energía promedio de la señal transmitida. Esta restricción se expresa como:

$$\mathbb{E}\left[||\mathbf{z}||^2\right] \leq P$$

donde $P$ es la potencia máxima permitida y $||\cdot||^2$ denota la norma euclidiana al cuadrado. En la práctica, esta restricción se implementa mediante una **capa de normalización de potencia** al final del encoder de canal. Las dos estrategias más comunes son:

**Normalización por lote** (*batch normalization*): Se normaliza cada símbolo para que el promedio sobre todo el lote de entrenamiento cumpla la restricción:

$$\mathbf{z}_{norm} = \sqrt{nP} \cdot \frac{\mathbf{z}}{||\mathbf{z}||_2}$$

donde $n$ es el número de usos del canal (dimensión de $\mathbf{z}$ dividida por 2 para canales complejos). Esta normalización garantiza que $||\mathbf{z}_{norm}||^2 = nP$ exactamente, lo cual es una restricción de potencia promedio por bloque.

**Normalización promedio** (*average power constraint*): Se normaliza para que la potencia promedio por símbolo sea igual a $P/n$:

$$\mathbf{z}_{norm} = \sqrt{P} \cdot \frac{\mathbf{z}}{\sqrt{\frac{1}{B}\sum_{b=1}^{B}||\mathbf{z}_b||^2}}$$

donde $B$ es el tamaño del lote. Esta normalización es más suave y permite variaciones en la potencia instantánea entre diferentes muestras, lo cual puede ser beneficioso para el aprendizaje de constelaciones adaptativas.

### 8.1.6 La razón de codificación $k/n$

Un parámetro fundamental del sistema es la **razón de codificación** o **tasa de compresión semántica**, definida como:

$$R = \frac{k}{n}$$

donde $k$ es la dimensión de la representación semántica (o equivalentemente, el número de valores reales que describen el significado del mensaje original) y $n$ es el número de usos del canal (o símbolos complejos transmitidos). Esta razón cuantifica el grado de compresión que el sistema aplica sobre la información semántica.

Cuando $R < 1$, el sistema está comprimiendo: transmite menos símbolos de los necesarios para representar completamente la información semántica. Esto es posible porque el encoder de canal aprende a codificar la información semántica de manera redundante solo donde es necesario para la protección contra errores. Cuando $R > 1$, el sistema está expandiendo, lo que corresponde a una codificación de canal fuerte que proporciona mayor protección.

La elección de $R$ implica un compromiso fundamental entre **eficiencia espectral** (valores bajos de $R$ permiten transmitir más información semántica por uso del canal) y **robustez** (valores altos de $R$ proporcionan mayor protección contra el ruido del canal a costa de utilizar más recursos de canal). En los sistemas E2E, este compromiso se aprende automáticamente durante el entrenamiento, en contraste con los sistemas convencionales donde debe diseñarse manualmente seleccionando tasas de codificación de fuente y canal específicas.

### 8.1.7 Diagrama del transmisor

> **Figura 8.1:** Arquitectura detallada del transmisor semántico E2E. El dato de origen $\mathbf{s}$ (por ejemplo, una oración de texto) ingresa al **Encoder Semántico**, compuesto por una capa de *embedding* seguida de $N_{se}$ capas de Transformer (cada una con auto-atención multi-cabeza, normalización de capa y red *feed-forward*). La salida del Transformer produce la representación semántica $\mathbf{h} \in \mathbb{R}^k$. Esta representación alimenta al **Encoder de Canal**, formado por una secuencia de capas densas con activaciones no lineales (Dense $\rightarrow$ ReLU $\rightarrow$ Dense $\rightarrow$ ReLU $\rightarrow$ Dense) que transforman progresivamente las dimensiones: $k \rightarrow 256 \rightarrow 128 \rightarrow 2n$. La salida pasa por una **capa de normalización de potencia** que asegura $\mathbb{E}[||\mathbf{z}||^2] \leq P$, produciendo el vector de símbolos de canal $\mathbf{z} \in \mathbb{R}^{2n}$ listo para la transmisión. Las flechas de gradiente (punteadas, en dirección opuesta) ilustran el flujo de retropropagación durante el entrenamiento.

---

## 8.2 El Canal Físico como Capa Diferenciable

### 8.2.1 Motivación: el canal como capa de la red neuronal

En el paradigma E2E, el canal de comunicación ocupa una posición central y a la vez paradójica. Por un lado, es un componente que **no se puede modificar ni optimizar**: el medio físico (aire, fibra óptica, cable) introduce distorsiones que son gobernadas por las leyes de la física electromagnética. Por otro lado, el entrenamiento E2E requiere que los gradientes de la función de pérdida fluyan **a través de todos los componentes del sistema**, incluyendo el canal, para actualizar los parámetros del transmisor. Esto exige que el canal se modele como una **capa diferenciable** dentro de la red neuronal completa.

La clave conceptual es la siguiente: aunque el canal real no tiene parámetros que optimizar, su modelo matemático puede incorporarse como una capa estocástica fija (sin parámetros entrenables) dentro del grafo computacional. Los gradientes no necesitan fluir *a través* del canal para actualizar parámetros del canal (que no existen), pero sí necesitan fluir *a través del modelo del canal* para llegar a los parámetros del transmisor. Esto es posible siempre que el modelo del canal sea diferenciable con respecto a su entrada $\mathbf{z}$.

### 8.2.2 Canal AWGN (Ruido Gaussiano Blanco Aditivo)

El modelo de canal más fundamental es el **canal AWGN** (*Additive White Gaussian Noise*), que modela un canal ideal con únicamente ruido térmico aditivo. La relación entrada-salida es:

$$\mathbf{y} = \mathbf{z} + \mathbf{n}$$

donde $\mathbf{z} \in \mathbb{R}^{2n}$ es el vector de símbolos transmitidos, $\mathbf{n} \sim \mathcal{N}(\mathbf{0}, \sigma^2\mathbf{I})$ es el vector de ruido gaussiano con media cero y varianza $\sigma^2$ por componente, y $\mathbf{y} \in \mathbb{R}^{2n}$ es el vector recibido. El término $\mathbf{I}$ denota la matriz identidad de dimensión apropiada, indicando que las componentes de ruido son independientes e idénticamente distribuidas (*i.i.d.*).

La diferenciabilidad de este canal con respecto a $\mathbf{z}$ es inmediata y elegante: puesto que la relación es lineal (una simple suma), el gradiente de $\mathbf{y}$ respecto a $\mathbf{z}$ es:

$$\frac{\partial \mathbf{y}}{\partial \mathbf{z}} = \mathbf{I}$$

Es decir, el gradiente pasa sin modificación a través del canal AWGN. La aleatoriedad del ruido no afecta la diferenciabilidad porque $\mathbf{n}$ no depende de $\mathbf{z}$. Esto convierte al canal AWGN en la capa diferenciable más sencilla posible: es equivalente a una capa de *dropout* que, en lugar de poner a cero aleatoriamente algunas activaciones, añade perturbaciones gaussianas a todas.

### 8.2.3 Canal con desvanecimiento Rayleigh

En entornos de comunicación inalámbrica, especialmente en escenarios urbanos o interiores donde no existe línea de vista directa entre transmisor y receptor, el canal experimenta **desvanecimiento Rayleigh** (*Rayleigh fading*). Este fenómeno se produce cuando la señal llega al receptor por múltiples trayectos, cada uno con diferente amplitud, fase y retardo, y ninguno de ellos es dominante. El modelo entrada-salida es:

$$\mathbf{y} = \mathbf{h} \odot \mathbf{z} + \mathbf{n}$$

donde $\odot$ denota el producto elemento a elemento (producto de Hadamard), $\mathbf{h} \sim \mathcal{CN}(\mathbf{0}, \mathbf{I})$ es el vector de coeficientes de desvanecimiento que sigue una distribución compleja gaussiana circular con media cero y varianza unitaria, y $\mathbf{n} \sim \mathcal{CN}(\mathbf{0}, \sigma^2\mathbf{I})$ es el ruido complejo gaussiano. El término $\mathcal{CN}$ denota la distribución gaussiana circular compleja.

En la representación en componentes reales (partes real e imaginaria separadas), cada coeficiente de canal $h_i = h_i^{(R)} + jh_i^{(I)}$ tiene partes real e imaginaria que son variables aleatorias gaussianas independientes: $h_i^{(R)}, h_i^{(I)} \sim \mathcal{N}(0, 1/2)$. La magnitud $|h_i|$ sigue una distribución Rayleigh con parámetro $\sigma_h = 1/\sqrt{2}$:

$$f_{|h_i|}(r) = 2r \cdot e^{-r^2}, \quad r \geq 0$$

La diferenciabilidad del canal Rayleigh con respecto a $\mathbf{z}$ se verifica fácilmente. Dado que la operación es un producto elemento a elemento, el gradiente es:

$$\frac{\partial y_i}{\partial z_i} = h_i$$

Es decir, el gradiente se escala por el coeficiente de canal correspondiente. En términos matriciales:

$$\frac{\partial \mathbf{y}}{\partial \mathbf{z}} = \text{diag}(\mathbf{h})$$

donde $\text{diag}(\mathbf{h})$ es la matriz diagonal cuyos elementos diagonales son las componentes de $\mathbf{h}$. Esto significa que durante la retropropagación, los gradientes que llegan al transmisor están modulados por la realización del canal, lo cual tiene una interpretación intuitiva: el sistema aprende a transmitir de manera que sea robusto frente a las variaciones de ganancia del canal.

### 8.2.4 Canal con desvanecimiento Riciano

Cuando existe una componente de **línea de vista** (*Line-of-Sight*, LoS) dominante entre transmisor y receptor, además de las componentes multitrayecto, el canal se modela mediante el **desvanecimiento Riciano** (*Rician fading*). El modelo entrada-salida tiene la misma estructura multiplicativa:

$$\mathbf{y} = \mathbf{h}_{Ric} \odot \mathbf{z} + \mathbf{n}$$

pero el vector de coeficientes de canal $\mathbf{h}_{Ric}$ se descompone en una componente determinista (LoS) y una componente aleatoria (dispersión):

$$\mathbf{h}_{Ric} = \sqrt{\frac{K}{K+1}} \mathbf{h}_{LoS} + \sqrt{\frac{1}{K+1}} \mathbf{h}_{NLoS}$$

donde $K$ es el **factor Riciano** (también llamado factor $K$), que cuantifica la razón de potencia entre la componente LoS y la componente dispersa. $\mathbf{h}_{LoS}$ es el vector de respuesta de la componente de línea de vista (típicamente un vector de fase $\mathbf{h}_{LoS} = e^{j\phi}\mathbf{1}$ para un canal de banda estrecha), y $\mathbf{h}_{NLoS} \sim \mathcal{CN}(\mathbf{0}, \mathbf{I})$ es la componente dispersa que sigue la distribución Rayleigh.

El factor $K$ controla la severidad del desvanecimiento:
- Cuando $K = 0$: no hay componente LoS, y el canal se reduce al modelo Rayleigh.
- Cuando $K \to \infty$: la componente LoS domina completamente y el canal se aproxima a un canal AWGN con ganancia fija.
- Para valores intermedios de $K$ (típicamente $K = 3$ a $K = 10$ dB en escenarios prácticos): coexisten ambas componentes.

La magnitud de cada coeficiente de canal $|h_{Ric,i}|$ sigue la distribución Rice:

$$f_{|h_{Ric,i}|}(r) = \frac{2r(K+1)}{1} \cdot e^{-K - (K+1)r^2} \cdot I_0\left(2r\sqrt{K(K+1)}\right), \quad r \geq 0$$

donde $I_0(\cdot)$ es la función de Bessel modificada de primera especie de orden cero. La diferenciabilidad del canal Riciano es idéntica a la del canal Rayleigh, ya que la estructura multiplicativa se mantiene.

### 8.2.5 Relación señal a ruido (SNR)

La **relación señal a ruido** (*Signal-to-Noise Ratio*, SNR) es el parámetro fundamental que caracteriza la calidad del canal. Se define como la razón entre la potencia de la señal transmitida y la potencia del ruido:

$$\text{SNR} = \frac{P}{\sigma^2}$$

donde $P = \mathbb{E}[||\mathbf{z}||^2]/n$ es la potencia promedio por símbolo (asumiendo $n$ símbolos complejos o $2n$ símbolos reales) y $\sigma^2$ es la varianza del ruido por componente. En decibelios (dB), la SNR se expresa como:

$$\text{SNR}_{\text{dB}} = 10\log_{10}\left(\frac{P}{\sigma^2}\right)$$

La escala logarítmica en decibelios es la convención estándar en telecomunicaciones porque permite expresar de manera compacta rangos muy amplios de SNR. Valores típicos en sistemas de comunicación prácticos van desde $\text{SNR}_{\text{dB}} \approx -5$ dB (canales muy ruidosos, como comunicaciones en el límite de cobertura celular) hasta $\text{SNR}_{\text{dB}} \approx 30$ dB (canales de alta calidad, como comunicaciones por fibra óptica o enlaces inalámbricos de corto alcance).

Durante el entrenamiento del sistema E2E, la varianza del ruido $\sigma^2$ se calcula a partir de la SNR deseada y la potencia de la señal (normalizada a $P = 1$ típicamente):

$$\sigma^2 = \frac{P}{10^{\text{SNR}_{\text{dB}}/10}} = 10^{-\text{SNR}_{\text{dB}}/10}$$

Esta relación permite simular diferentes condiciones de canal durante el entrenamiento simplemente ajustando el valor de $\sigma^2$ al generar el ruido gaussiano.

### 8.2.6 Requisito de diferenciabilidad para la retropropagación

El entrenamiento de redes neuronales mediante descenso de gradiente estocástico (SGD) requiere calcular las derivadas parciales de la función de pérdida $L$ con respecto a todos los parámetros del modelo. En un sistema E2E, los parámetros del transmisor $\theta_{tx}$ aparecen *antes* del canal en el grafo computacional. Para calcular $\frac{\partial L}{\partial \theta_{tx}}$ mediante la regla de la cadena, necesitamos:

$$\frac{\partial L}{\partial \theta_{tx}} = \frac{\partial L}{\partial \hat{\mathbf{s}}} \cdot \frac{\partial \hat{\mathbf{s}}}{\partial \mathbf{y}} \cdot \frac{\partial \mathbf{y}}{\partial \mathbf{z}} \cdot \frac{\partial \mathbf{z}}{\partial \theta_{tx}}$$

El factor crítico es $\frac{\partial \mathbf{y}}{\partial \mathbf{z}}$, que requiere que el canal sea diferenciable con respecto a su entrada. Como hemos visto, para los canales AWGN y con desvanecimiento, este gradiente existe y es sencillo de calcular. Sin embargo, hay situaciones donde la diferenciabilidad no es trivial, por ejemplo, cuando el canal incluye cuantización (conversión analógico-digital), detección de umbral, o cualquier operación discontinua.

### 8.2.7 El truco de reparametrización para canales estocásticos

Aunque los canales estudiados son diferenciables con respecto a $\mathbf{z}$, la presencia de variables aleatorias ($\mathbf{n}$, $\mathbf{h}$) introduce un desafío computacional. Al entrenar, necesitamos calcular el gradiente de la esperanza de la pérdida:

$$\nabla_{\theta_{tx}} \mathbb{E}_{\mathbf{n}, \mathbf{h}}\left[L\left(g_{\theta_{rx}}(\mathbf{h} \odot f_{\theta_{tx}}(\mathbf{s}) + \mathbf{n}), \mathbf{s}\right)\right]$$

El **truco de reparametrización** (*reparameterization trick*), popularizado por Kingma y Welling en el contexto de los autoencoders variacionales (VAE), permite mover el operador de gradiente dentro de la esperanza. La idea es expresar las variables aleatorias como transformaciones deterministas de una variable auxiliar con distribución fija. Para el canal AWGN:

$$\mathbf{y} = \mathbf{z} + \sigma \boldsymbol{\epsilon}, \quad \boldsymbol{\epsilon} \sim \mathcal{N}(\mathbf{0}, \mathbf{I})$$

Aquí, $\boldsymbol{\epsilon}$ es una variable aleatoria que no depende de los parámetros del modelo. La varianza del ruido $\sigma$ actúa como un factor de escala determinista. Esto permite escribir:

$$\nabla_{\theta_{tx}} \mathbb{E}_{\boldsymbol{\epsilon}}\left[L\left(g_{\theta_{rx}}(\mathbf{z} + \sigma\boldsymbol{\epsilon}), \mathbf{s}\right)\right] = \mathbb{E}_{\boldsymbol{\epsilon}}\left[\nabla_{\theta_{tx}} L\left(g_{\theta_{rx}}(\mathbf{z} + \sigma\boldsymbol{\epsilon}), \mathbf{s}\right)\right]$$

El intercambio del gradiente y la esperanza es válido bajo condiciones de regularidad suaves (que se cumplen para las distribuciones gaussianas y funciones de pérdida suaves). En la práctica, la esperanza se aproxima mediante Monte Carlo con una sola muestra por cada elemento del mini-lote:

$$\nabla_{\theta_{tx}} L \approx \frac{1}{B} \sum_{b=1}^{B} \nabla_{\theta_{tx}} L\left(g_{\theta_{rx}}(\mathbf{z}_b + \sigma\boldsymbol{\epsilon}_b), \mathbf{s}_b\right)$$

donde $\boldsymbol{\epsilon}_b \sim \mathcal{N}(\mathbf{0}, \mathbf{I})$ se muestrea de forma independiente para cada elemento del lote. Esta aproximación es no sesgada y tiene varianza controlable (que disminuye con $1/B$).

Para el canal Rayleigh, la reparametrización es análoga:

$$\mathbf{y} = (\boldsymbol{\epsilon}_h) \odot \mathbf{z} + \sigma\boldsymbol{\epsilon}_n$$

donde $\boldsymbol{\epsilon}_h \sim \mathcal{CN}(\mathbf{0}, \mathbf{I})$ y $\boldsymbol{\epsilon}_n \sim \mathcal{CN}(\mathbf{0}, \mathbf{I})$ son variables auxiliares independientes de los parámetros del modelo.

### 8.2.8 Visualización del efecto del canal

> **Figura 8.2:** Efecto de los modelos de canal sobre los símbolos transmitidos, visualizado en un diagrama de constelación (plano I-Q). Se muestran tres paneles: **(a) Canal AWGN:** los símbolos transmitidos (puntos azules) se dispersan isotrópicamente alrededor de sus posiciones originales, formando nubes gaussianas circulares. La dispersión es proporcional a $\sigma$. A SNR alta, las nubes son compactas y separables; a SNR baja, se solapan causando errores. **(b) Canal Rayleigh:** los símbolos experimentan rotaciones y escalados aleatorios (cada símbolo se multiplica por un coeficiente complejo aleatorio $h_i$), produciendo una dispersión no uniforme que incluye desvanecimiento profundo (símbolos que se atenúan casi a cero). La nube resultante tiene una envolvente Rayleigh que concentra energía cerca del origen. **(c) Canal Riciano ($K = 5$ dB):** el efecto es intermedio; la componente LoS mantiene una dirección preferencial mientras la componente dispersa añade variación, generando una distribución Rice en la magnitud de los símbolos recibidos. En los tres paneles, los puntos rojos representan los símbolos recibidos $\mathbf{y}$ y las flechas verdes ilustran la distorsión introducida por el canal.

---

## 8.3 El Decoder Semántico-Canal (Receptor)

### 8.3.1 Estructura general del receptor

El receptor en un sistema de comunicación semántica E2E tiene la tarea de reconstruir el dato original $\mathbf{s}$ (o una aproximación semánticamente fiel $\hat{\mathbf{s}}$) a partir de la señal recibida $\mathbf{y}$, que ha sido corrompida por el canal. Al igual que el transmisor se divide conceptualmente en encoder semántico y encoder de canal, el receptor se estructura en dos etapas complementarias: el **decoder de canal** y el **decoder semántico**.

### 8.3.2 El decoder de canal

El **decoder de canal** es la primera etapa del receptor. Recibe la señal ruidosa $\mathbf{y}$ y produce una estimación de la representación semántica $\hat{\mathbf{h}}$:

$$\hat{\mathbf{h}} = g_{\theta_{cd}}(\mathbf{y})$$

donde $g_{\theta_{cd}}$ es la función de decodificación de canal implementada por una red neuronal con parámetros $\theta_{cd}$. La función de este componente es *deshacer* las distorsiones del canal —ruido, desvanecimiento, interferencia— y recuperar la representación semántica latente que fue codificada por el transmisor.

Arquitectónicamente, el decoder de canal suele ser el espejo del encoder de canal: si el encoder de canal utilizó capas densas para reducir la dimensión desde $k$ (espacio semántico) hasta $2n$ (espacio de canal), el decoder de canal utiliza capas densas que transforman desde $2n$ de vuelta a $k$. Cada capa aplica:

$$\hat{\mathbf{h}}^{(l)} = \sigma\left(\mathbf{W}_{cd}^{(l)} \hat{\mathbf{h}}^{(l-1)} + \mathbf{b}_{cd}^{(l)}\right)$$

con la entrada inicial $\hat{\mathbf{h}}^{(0)} = \mathbf{y}$. Las dimensiones se expanden progresivamente: $2n \rightarrow 128 \rightarrow 256 \rightarrow k$, invirtiendo la compresión realizada por el encoder de canal.

En canales con desvanecimiento, cuando la información de estado del canal (CSI, *Channel State Information*) está disponible en el receptor, esta puede incorporarse como entrada adicional al decoder de canal:

$$\hat{\mathbf{h}} = g_{\theta_{cd}}(\mathbf{y}, \hat{\mathbf{h}}_{csi})$$

donde $\hat{\mathbf{h}}_{csi}$ representa la estimación de los coeficientes del canal. En la práctica, esto puede implementarse concatenando $\mathbf{y}$ y $\hat{\mathbf{h}}_{csi}$ como entrada a la primera capa densa, o utilizando capas de atención que ponderen la señal recibida en función de la calidad estimada del canal.

### 8.3.3 El decoder semántico

El **decoder semántico** toma la representación semántica recuperada $\hat{\mathbf{h}}$ y produce la reconstrucción final del dato original:

$$\hat{\mathbf{s}} = g_{\theta_{sd}}(\hat{\mathbf{h}})$$

donde $g_{\theta_{sd}}$ es la función de decodificación semántica con parámetros $\theta_{sd}$. La arquitectura de este componente depende críticamente de la modalidad de datos:

**Para texto:** El decoder semántico emplea un **Transformer decoder** con mecanismo de **atención cruzada** (*cross-attention*) que atiende a la representación semántica recuperada $\hat{\mathbf{h}}$. La generación de texto es **autoregresiva**: los tokens de salida se generan uno a uno, donde la predicción de cada token $\hat{s}_t$ depende de la representación semántica y de todos los tokens previamente generados:

$$p(\hat{s}_t | \hat{s}_{<t}, \hat{\mathbf{h}}) = \text{softmax}\left(\mathbf{W}_o \cdot \text{TransformerDecoder}(\hat{s}_{<t}, \hat{\mathbf{h}})\right)$$

donde $\hat{s}_{<t} = (\hat{s}_1, \hat{s}_2, \ldots, \hat{s}_{t-1})$ denota la secuencia de tokens generados hasta el paso $t-1$, y $\mathbf{W}_o \in \mathbb{R}^{|V| \times d_{model}}$ es la matriz de proyección de salida que mapea al espacio del vocabulario. El mecanismo de atención cruzada permite que el decoder semántico "consulte" selectivamente diferentes partes de la representación semántica al generar cada token, de manera análoga a como un traductor humano consulta repetidamente el texto fuente al redactar la traducción.

**Para imágenes:** El decoder semántico emplea una arquitectura de **red convolucional transpuesta** (también llamada deconvolucional) que progresivamente incrementa la resolución espacial y reduce la profundidad de canales. Si la representación semántica $\hat{\mathbf{h}} \in \mathbb{R}^{H' \times W' \times C'}$, el decoder aplica una secuencia de capas de sobremuestreo (*upsampling*):

$$\hat{\mathbf{s}}^{(l)} = \sigma\left(\text{ConvTranspose2d}\left(\hat{\mathbf{s}}^{(l-1)}\right)\right)$$

donde cada capa de convolución transpuesta duplica las dimensiones espaciales y reduce los canales: $H' \times W' \times C' \rightarrow 2H' \times 2W' \times C'/2 \rightarrow \cdots \rightarrow H \times W \times C$. La última capa utiliza una activación sigmoide o tangente hiperbólica para producir valores de píxeles en el rango apropiado ($[0,1]$ o $[-1,1]$).

### 8.3.4 Formulación completa del receptor

La operación completa del receptor se expresa como la composición de ambos decoders:

$$\hat{\mathbf{s}} = g_{\theta_{sd}}\left(g_{\theta_{cd}}(\mathbf{y})\right)$$

y el receptor completo está parametrizado por $\theta_{rx} = \{\theta_{cd}, \theta_{sd}\}$. Combinando con la expresión del transmisor, el sistema E2E completo se describe como:

$$\hat{\mathbf{s}} = g_{\theta_{sd}}\left(g_{\theta_{cd}}\left(\text{Canal}\left(f_{\theta_{ce}}\left(f_{\theta_{se}}(\mathbf{s})\right)\right)\right)\right)$$

Esta cadena de funciones compuestas constituye el grafo computacional completo del sistema, a través del cual fluyen los gradientes durante el entrenamiento. La simetría entre transmisor y receptor (encoder/decoder) no es accidental: el sistema E2E es esencialmente un **autoencoder** cuyo cuello de botella no es una capa de dimensión reducida, sino el canal de comunicación físico.

---

## 8.4 Funciones de Pérdida para Comunicaciones Semánticas

### 8.4.1 El papel central de la función de pérdida

La función de pérdida es, junto con la arquitectura de la red, el componente más crítico del diseño de un sistema de comunicación semántica E2E. Mientras que en los sistemas de comunicación convencionales la métrica de rendimiento es la tasa de error de bit (BER) o la tasa de error de bloque (BLER) —métricas puramente sintácticas que tratan todos los bits como igualmente importantes—, los sistemas semánticos requieren funciones de pérdida que capturen la **fidelidad del significado** transmitido. La elección de la función de pérdida determina qué aspectos del mensaje el sistema priorizará preservar.

### 8.4.2 Funciones de pérdida para transmisión de texto

La transmisión de texto presenta desafíos particulares porque el lenguaje natural es discreto (secuencias de tokens de un vocabulario finito), altamente estructurado (con sintaxis, semántica y pragmática) y ambiguo (diferentes secuencias de palabras pueden expresar el mismo significado).

**Pérdida de entropía cruzada (*Cross-Entropy Loss*):** La función de pérdida estándar para modelos generativos de texto es la entropía cruzada entre la distribución de probabilidad predicha y el token verdadero, sumada sobre todas las posiciones de la secuencia:

$$L_{CE} = -\sum_{t=1}^{T} \log p_{\theta}(\hat{s}_t = s_t \mid \hat{s}_{<t}, \mathbf{y})$$

donde $T$ es la longitud de la secuencia objetivo, $s_t$ es el token verdadero en la posición $t$, $\hat{s}_{<t}$ son los tokens generados en las posiciones anteriores (durante el entrenamiento, se usa *teacher forcing* con los tokens verdaderos), y $p_{\theta}(\cdot)$ es la distribución de probabilidad sobre el vocabulario predicha por el modelo.

La entropía cruzada tiene una interpretación profunda en teoría de la información: es equivalente a la log-verosimilitud negativa (*negative log-likelihood*) de la secuencia objetivo bajo el modelo, y su minimización es equivalente a minimizar la divergencia KL entre la distribución verdadera de los datos y la distribución del modelo:

$$L_{CE} = -\log p_{\theta}(s_1, s_2, \ldots, s_T \mid \mathbf{y}) = \text{KL}(p_{data} || p_{\theta}) + H(p_{data})$$

donde $H(p_{data})$ es la entropía de la distribución verdadera (una constante con respecto a $\theta$). Por tanto, minimizar $L_{CE}$ es equivalente a minimizar la divergencia KL.

Sin embargo, la entropía cruzada opera a nivel de **token individual** y no captura directamente la similitud semántica a nivel de oración. Dos oraciones pueden tener la misma semántica pero diferir significativamente token a token (por ejemplo, "El gato está sobre la alfombra" vs. "Encima del tapete se encuentra el felino"), lo que resultaría en una pérdida de entropía cruzada alta a pesar de la equivalencia semántica.

**Pérdida de similitud semántica basada en embeddings:** Para capturar la fidelidad semántica a nivel de oración, se puede emplear una pérdida basada en la similitud entre las representaciones vectoriales (*embeddings*) de las oraciones original y reconstruida. Utilizando un modelo de *embeddings* de oraciones pre-entrenado $\phi(\cdot)$ (como BERT o Sentence-BERT):

$$L_{sem} = 1 - \frac{\phi(\mathbf{s})^{\top} \phi(\hat{\mathbf{s}})}{||\phi(\mathbf{s})|| \cdot ||\phi(\hat{\mathbf{s}})||}$$

donde el cociente es la **similitud coseno** entre los embeddings de la oración original y la reconstruida. Esta pérdida vale 0 cuando las oraciones son semánticamente idénticas (embeddings paralelos) y 1 cuando son completamente disímiles (embeddings ortogonales). Un valor de 2 correspondería a significados opuestos (embeddings antiparalelos), aunque esto raramente ocurre en la práctica.

La ventaja de esta pérdida es que permite paráfrasis: el sistema puede reconstruir el significado del mensaje usando palabras diferentes sin ser penalizado, lo cual es deseable desde el punto de vista de la comunicación semántica. Su desventaja es que depende de la calidad del modelo de embeddings pre-entrenado y añade un costo computacional no despreciable al calcular los embeddings en cada paso de entrenamiento.

### 8.4.3 Funciones de pérdida para transmisión de imágenes

La transmisión de imágenes permite utilizar funciones de pérdida que operan en el dominio continuo de los valores de píxeles, pero la elección de la función tiene un impacto significativo en la calidad perceptual de las imágenes reconstruidas.

**Error cuadrático medio (*Mean Squared Error*, MSE):** La función de pérdida más fundamental para imágenes es el MSE, que mide la diferencia promedio al cuadrado entre cada píxel de la imagen original y la reconstruida:

$$L_{MSE} = \frac{1}{N}\sum_{i=1}^{N}(s_i - \hat{s}_i)^2 = \frac{1}{N}||\mathbf{s} - \hat{\mathbf{s}}||^2$$

donde $N = H \times W \times C$ es el número total de píxeles (alto × ancho × canales de color). El MSE es equivalente al PSNR (*Peak Signal-to-Noise Ratio*) a través de la relación:

$$\text{PSNR} = 10\log_{10}\left(\frac{\text{MAX}^2}{L_{MSE}}\right)$$

donde $\text{MAX}$ es el valor máximo del píxel (255 para imágenes de 8 bits o 1.0 para imágenes normalizadas).

El MSE es matemáticamente conveniente (es suave, convexo y fácil de optimizar), pero tiene una limitación fundamental: trata todos los errores de píxel como igualmente importantes, independientemente de su relevancia perceptual. Esto produce imágenes que, aunque tienen PSNR alto, pueden parecer borrosas porque el MSE favorece la predicción del promedio de posibles reconstrucciones en regiones de alta incertidumbre.

**Pérdida perceptual (*Perceptual Loss*):** Para superar las limitaciones del MSE, se emplea la pérdida perceptual, que compara las imágenes en el espacio de características de una red de clasificación pre-entrenada (típicamente VGG-16 o VGG-19 entrenada en ImageNet):

$$L_{perceptual} = \sum_{l \in \mathcal{L}} \frac{1}{N_l}||\Phi_l(\mathbf{s}) - \Phi_l(\hat{\mathbf{s}})||^2$$

donde $\Phi_l(\cdot)$ denota el mapa de activaciones de la capa $l$ de la red VGG, $N_l$ es el número de elementos en el mapa de activaciones de la capa $l$, y $\mathcal{L}$ es el conjunto de capas seleccionadas (típicamente capas de las primeras etapas del bloque convolucional).

La intuición detrás de la pérdida perceptual es que las capas internas de una red de clasificación de imágenes pre-entrenada han aprendido a extraer características perceptualmente relevantes: bordes, texturas, formas y estructuras. Comparar imágenes en este espacio de características, en lugar del espacio de píxeles, resulta en reconstrucciones que se parecen más a la imagen original desde el punto de vista humano, aunque puedan diferir en detalles de píxel.

**Pérdida basada en SSIM (*Structural Similarity Index Measure*):** El índice de similitud estructural SSIM compara las imágenes en términos de luminancia, contraste y estructura:

$$\text{SSIM}(\mathbf{s}, \hat{\mathbf{s}}) = \frac{(2\mu_s\mu_{\hat{s}} + c_1)(2\sigma_{s\hat{s}} + c_2)}{(\mu_s^2 + \mu_{\hat{s}}^2 + c_1)(\sigma_s^2 + \sigma_{\hat{s}}^2 + c_2)}$$

donde $\mu_s$, $\mu_{\hat{s}}$ son las medias locales, $\sigma_s^2$, $\sigma_{\hat{s}}^2$ son las varianzas locales, $\sigma_{s\hat{s}}$ es la covarianza local, y $c_1$, $c_2$ son constantes de estabilización. El SSIM se calcula localmente en ventanas deslizantes y se promedia sobre toda la imagen. La pérdida basada en SSIM se define como:

$$L_{SSIM} = 1 - \text{SSIM}(\mathbf{s}, \hat{\mathbf{s}})$$

El SSIM captura mejor la percepción humana de calidad que el MSE porque se basa en la comparación de estadísticas locales de luminancia, contraste y estructura, que son los elementos que el sistema visual humano utiliza para evaluar la calidad de las imágenes.

### 8.4.4 Función de pérdida combinada

En la práctica, los sistemas de comunicación semántica E2E suelen emplear una **función de pérdida combinada** que integra múltiples objetivos:

$$L = \alpha L_{task} + \beta L_{semantic} + \gamma L_{channel}$$

donde:
- $L_{task}$ es la pérdida específica de la tarea (por ejemplo, entropía cruzada para texto, MSE para imágenes).
- $L_{semantic}$ es una pérdida que mide la fidelidad semántica (por ejemplo, similitud coseno de embeddings, pérdida perceptual).
- $L_{channel}$ es un término de regularización que puede incluir restricciones sobre la distribución de los símbolos transmitidos (por ejemplo, penalización de potencia, suavidad de la constelación, o restricciones de forma de espectro).
- $\alpha, \beta, \gamma \geq 0$ son hiperparámetros que ponderan la contribución relativa de cada componente.

El diseño de estos pesos implica compromisos fundamentales. Un valor alto de $\alpha$ con $\beta \approx 0$ produce un sistema que replica fielmente la secuencia de símbolos originales pero puede no capturar la semántica subyacente. Un valor alto de $\beta$ con $\alpha \approx 0$ produce un sistema que preserva el significado global pero puede alterar los detalles superficiales del mensaje. El término $\gamma$ controla la regularización del espacio de señales de canal y puede mejorar la robustez del sistema frente a condiciones de canal no vistas durante el entrenamiento.

En la práctica, estos hiperparámetros se seleccionan mediante validación cruzada o búsqueda de hiperparámetros, y sus valores óptimos dependen de la modalidad de datos, la arquitectura del sistema, el rango de SNR operativo y los requisitos de la aplicación.

---

## 8.5 Proceso de Entrenamiento E2E Paso a Paso

### 8.5.1 Visión general del entrenamiento

El entrenamiento de un sistema de comunicación semántica E2E sigue el paradigma estándar de aprendizaje profundo —retropropagación con descenso de gradiente estocástico— pero con particularidades importantes derivadas de la presencia del canal estocástico en medio de la red. En esta subsección, desglosamos el proceso paso a paso con rigor matemático.

### 8.5.2 Paso 1: Propagación hacia adelante (*Forward Pass*)

Dado un mini-lote de $B$ muestras de entrenamiento $\{\mathbf{s}_1, \mathbf{s}_2, \ldots, \mathbf{s}_B\}$ extraídas del conjunto de datos de entrenamiento, la propagación hacia adelante recorre secuencialmente todos los componentes del sistema:

**Etapa 1 — Encoder semántico:** Para cada muestra $b$:
$$\mathbf{h}_b = f_{\theta_{se}}(\mathbf{s}_b), \quad b = 1, 2, \ldots, B$$

**Etapa 2 — Encoder de canal:**
$$\mathbf{z}_b = f_{\theta_{ce}}(\mathbf{h}_b)$$

**Etapa 3 — Normalización de potencia:**
$$\mathbf{z}_b^{norm} = \text{PowerNorm}(\mathbf{z}_b)$$

**Etapa 4 — Canal (con reparametrización):**
Se muestrea ruido $\boldsymbol{\epsilon}_b \sim \mathcal{N}(\mathbf{0}, \mathbf{I})$ y, opcionalmente, coeficientes de desvanecimiento $\boldsymbol{\epsilon}_{h,b} \sim \mathcal{CN}(\mathbf{0}, \mathbf{I})$. La señal recibida se calcula como:
$$\mathbf{y}_b = \mathbf{z}_b^{norm} + \sigma\boldsymbol{\epsilon}_b \quad \text{(AWGN)}$$
$$\mathbf{y}_b = \boldsymbol{\epsilon}_{h,b} \odot \mathbf{z}_b^{norm} + \sigma\boldsymbol{\epsilon}_b \quad \text{(Rayleigh)}$$

**Etapa 5 — Decoder de canal:**
$$\hat{\mathbf{h}}_b = g_{\theta_{cd}}(\mathbf{y}_b)$$

**Etapa 6 — Decoder semántico:**
$$\hat{\mathbf{s}}_b = g_{\theta_{sd}}(\hat{\mathbf{h}}_b)$$

Es fundamental observar que cada etapa mantiene el grafo computacional necesario para la retropropagación. Las variables aleatorias $\boldsymbol{\epsilon}_b$ y $\boldsymbol{\epsilon}_{h,b}$ se tratan como constantes durante la retropropagación (no tienen gradientes), pero la reparametrización asegura que $\mathbf{y}_b$ permanece diferenciable con respecto a $\mathbf{z}_b^{norm}$ y, por tanto, con respecto a todos los parámetros del transmisor.

### 8.5.3 Paso 2: Cálculo de la pérdida

Se computa la función de pérdida promediada sobre el mini-lote:

$$L = \frac{1}{B}\sum_{b=1}^{B} \ell(\mathbf{s}_b, \hat{\mathbf{s}}_b)$$

donde $\ell(\cdot, \cdot)$ es la función de pérdida por muestra (por ejemplo, entropía cruzada, MSE o una combinación ponderada). El valor escalar $L$ cuantifica qué tan bien el sistema completo —desde la entrada del transmisor hasta la salida del receptor, pasando por el canal ruidoso— preserva el contenido del mensaje.

### 8.5.4 Paso 3: Retropropagación (*Backpropagation*)

El cálculo de gradientes se realiza mediante la aplicación recursiva de la regla de la cadena, fluyendo desde la pérdida hacia atrás a través de todos los componentes del sistema:

**Gradientes del decoder semántico:**
$$\frac{\partial L}{\partial \theta_{sd}} = \frac{1}{B}\sum_{b=1}^{B} \frac{\partial \ell}{\partial \hat{\mathbf{s}}_b} \cdot \frac{\partial \hat{\mathbf{s}}_b}{\partial \theta_{sd}}$$

**Gradientes del decoder de canal:**
$$\frac{\partial L}{\partial \theta_{cd}} = \frac{1}{B}\sum_{b=1}^{B} \frac{\partial \ell}{\partial \hat{\mathbf{s}}_b} \cdot \frac{\partial \hat{\mathbf{s}}_b}{\partial \hat{\mathbf{h}}_b} \cdot \frac{\partial \hat{\mathbf{h}}_b}{\partial \theta_{cd}}$$

**Gradientes a través del canal:** Aquí es donde la reparametrización juega su papel crucial. Para AWGN:
$$\frac{\partial \mathbf{y}_b}{\partial \mathbf{z}_b^{norm}} = \mathbf{I}$$

Para Rayleigh:
$$\frac{\partial \mathbf{y}_b}{\partial \mathbf{z}_b^{norm}} = \text{diag}(\boldsymbol{\epsilon}_{h,b})$$

**Gradientes del encoder de canal:**
$$\frac{\partial L}{\partial \theta_{ce}} = \frac{1}{B}\sum_{b=1}^{B} \frac{\partial \ell}{\partial \hat{\mathbf{s}}_b} \cdot \frac{\partial \hat{\mathbf{s}}_b}{\partial \hat{\mathbf{h}}_b} \cdot \frac{\partial \hat{\mathbf{h}}_b}{\partial \mathbf{y}_b} \cdot \frac{\partial \mathbf{y}_b}{\partial \mathbf{z}_b^{norm}} \cdot \frac{\partial \mathbf{z}_b^{norm}}{\partial \theta_{ce}}$$

**Gradientes del encoder semántico:**
$$\frac{\partial L}{\partial \theta_{se}} = \frac{1}{B}\sum_{b=1}^{B} \frac{\partial \ell}{\partial \hat{\mathbf{s}}_b} \cdot \frac{\partial \hat{\mathbf{s}}_b}{\partial \hat{\mathbf{h}}_b} \cdot \frac{\partial \hat{\mathbf{h}}_b}{\partial \mathbf{y}_b} \cdot \frac{\partial \mathbf{y}_b}{\partial \mathbf{z}_b^{norm}} \cdot \frac{\partial \mathbf{z}_b^{norm}}{\partial \mathbf{h}_b} \cdot \frac{\partial \mathbf{h}_b}{\partial \theta_{se}}$$

Observe cómo los gradientes fluyen a través de toda la cadena, incluyendo el canal. La estocasticidad del canal introduce variabilidad en los gradientes (ya que $\boldsymbol{\epsilon}_{h,b}$ y $\boldsymbol{\epsilon}_b$ son diferentes para cada muestra y cada época), lo cual actúa como una forma adicional de regularización que mejora la generalización del modelo.

### 8.5.5 Paso 4: Actualización de parámetros

Todos los parámetros del sistema se actualizan **conjuntamente** utilizando un optimizador de descenso de gradiente. Con el optimizador Adam:

$$\theta \leftarrow \theta - \eta \cdot \text{Adam}(\nabla_\theta L)$$

donde $\theta = \{\theta_{se}, \theta_{ce}, \theta_{cd}, \theta_{sd}\}$ es el conjunto completo de parámetros y $\eta$ es la tasa de aprendizaje. El optimizador Adam adapta la tasa de aprendizaje para cada parámetro individualmente utilizando estimaciones de los momentos de primer y segundo orden de los gradientes:

$$m_t = \beta_1 m_{t-1} + (1-\beta_1)\nabla_\theta L$$
$$v_t = \beta_2 v_{t-1} + (1-\beta_2)(\nabla_\theta L)^2$$
$$\hat{m}_t = \frac{m_t}{1-\beta_1^t}, \quad \hat{v}_t = \frac{v_t}{1-\beta_2^t}$$
$$\theta_{t+1} = \theta_t - \eta \frac{\hat{m}_t}{\sqrt{\hat{v}_t} + \epsilon}$$

donde $\beta_1 = 0.9$ y $\beta_2 = 0.999$ son valores típicos de los hiperparámetros de Adam, y $\epsilon = 10^{-8}$ es un factor de estabilización numérica.

La actualización conjunta es esencial: permite que el transmisor y el receptor co-adapten sus estrategias. El transmisor aprende a codificar la información de una manera que el receptor pueda decodificar eficientemente dado el ruido del canal, y el receptor aprende a decodificar de una manera que explota las regularidades de la codificación del transmisor.

### 8.5.6 Entrenamiento con currículo de SNR

Una técnica crucial para el entrenamiento exitoso de sistemas E2E es el **entrenamiento con currículo de SNR** (*SNR curriculum training*). La idea es comenzar el entrenamiento con valores altos de SNR (canal menos ruidoso) y gradualmente reducir la SNR a lo largo del entrenamiento (incrementando el nivel de ruido).

La justificación pedagógica es análoga a la enseñanza humana: primero se aprenden los conceptos básicos en un entorno "fácil" (alto SNR, poco ruido) y después se desarrolla robustez frente a condiciones adversas (bajo SNR, mucho ruido). Formalmente, la varianza del ruido sigue un programa:

$$\sigma^2(e) = \frac{P}{10^{\text{SNR}(e)/10}}$$

donde $\text{SNR}(e)$ es la SNR programada para la época $e$. Un programa típico podría ser:

$$\text{SNR}(e) = \text{SNR}_{max} - \frac{e}{E}(\text{SNR}_{max} - \text{SNR}_{min})$$

donde $E$ es el número total de épocas, $\text{SNR}_{max}$ (por ejemplo, 20 dB) es la SNR inicial y $\text{SNR}_{min}$ (por ejemplo, 0 dB) es la SNR final.

**Entrenamiento con SNR mixto por lote:** Una alternativa al currículo temporal es entrenar cada mini-lote con **valores de SNR variados**. Para cada muestra $b$ del lote, se selecciona una SNR diferente $\text{SNR}_b \sim \mathcal{U}[\text{SNR}_{min}, \text{SNR}_{max}]$ muestreada uniformemente del rango operativo deseado:

$$\sigma_b^2 = 10^{-\text{SNR}_b/10}$$

Esta estrategia produce un modelo que funciona razonablemente bien en todo el rango de SNR, en lugar de estar optimizado para un único valor. El costo es que el rendimiento en cualquier SNR específica puede ser ligeramente inferior al de un modelo entrenado exclusivamente para esa SNR.

### 8.5.7 Diagrama del proceso de entrenamiento

> **Figura 8.3:** Diagrama completo del bucle de entrenamiento E2E. El flujo de datos comienza con un mini-lote de muestras $\{\mathbf{s}_b\}_{b=1}^B$ (izquierda). **Propagación hacia adelante** (flechas azules, de izquierda a derecha): los datos pasan secuencialmente por el Encoder Semántico ($f_{\theta_{se}}$), el Encoder de Canal ($f_{\theta_{ce}}$), la Normalización de Potencia, el Canal Estocástico (representado como una nube con ruido $\mathbf{n}$ y, opcionalmente, desvanecimiento $\mathbf{h}$), el Decoder de Canal ($g_{\theta_{cd}}$) y el Decoder Semántico ($g_{\theta_{sd}}$), produciendo las reconstrucciones $\{\hat{\mathbf{s}}_b\}$. El módulo de **Cálculo de Pérdida** (derecha) compara $\mathbf{s}_b$ con $\hat{\mathbf{s}}_b$ y produce el escalar $L$. **Retropropagación** (flechas rojas punteadas, de derecha a izquierda): los gradientes $\nabla L$ fluyen en dirección opuesta a través de todos los componentes, incluyendo a través del canal (gracias a la reparametrización). El **Optimizador Adam** (parte inferior) recibe todos los gradientes y actualiza conjuntamente los parámetros $\theta = \{\theta_{se}, \theta_{ce}, \theta_{cd}, \theta_{sd}\}$. Un módulo de **Programación de SNR** (esquina superior derecha) controla la varianza del ruido $\sigma^2$ que se inyecta en el canal, permitiendo el entrenamiento con currículo.

---

## 8.6 Conversión de Señales Multimedia a Representación Semántica

### 8.6.1 El desafío de la representación universal

Uno de los aspectos más fascinantes y técnicamente desafiantes de la comunicación semántica es la transformación de señales multimedia en su forma nativa —ondas sonoras, secuencias de fotogramas de video, secuencias de caracteres— en representaciones semánticas compactas que capturan el significado esencial. Esta transformación debe ser simultáneamente eficiente (comprimir la información drásticamente), informativa (preservar el contenido semántico) y robusta (las representaciones deben ser adecuadas para su transmisión por canales ruidosos). En esta subsección, examinamos en detalle cómo se realiza esta conversión para las principales modalidades multimedia.

### 8.6.2 Audio y voz: de la onda acústica a tokens semánticos

El procesamiento de señales de audio y voz para comunicación semántica sigue una cadena de transformaciones progresivas:

**Paso 1 — De la forma de onda al espectrograma:** La señal de audio cruda es una forma de onda unidimensional $x(t)$ muestreada típicamente a 16 kHz o 44.1 kHz. El primer paso es convertirla en una representación tiempo-frecuencia bidimensional mediante la **Transformada de Fourier de Tiempo Corto** (STFT):

$$X(t, f) = \sum_{\tau} x(\tau) w(\tau - t) e^{-j2\pi f \tau}$$

donde $w(\tau)$ es una función ventana (típicamente Hann o Hamming) de longitud 25 ms con desplazamiento de 10 ms. El resultado $|X(t, f)|^2$ es el espectrograma de potencia: una imagen 2D donde el eje horizontal representa el tiempo, el eje vertical representa la frecuencia, y la intensidad representa la potencia.

**Paso 2 — Del espectrograma al mel-espectrograma:** Para capturar la percepción auditiva humana (que es logarítmica en frecuencia), se aplica un banco de filtros mel al espectrograma:

$$M(t, m) = \sum_{f} |X(t, f)|^2 \cdot \Phi_m(f)$$

donde $\Phi_m(f)$ es el $m$-ésimo filtro triangular en la escala mel. Típicamente se utilizan 80 filtros mel, produciendo un mel-espectrograma $\mathbf{M} \in \mathbb{R}^{T' \times 80}$ donde $T'$ es el número de tramas temporales.

**Paso 3 — Del mel-espectrograma a tokens semánticos:** El mel-espectrograma se procesa mediante un encoder (CNN o Transformer) que extrae una secuencia de vectores semánticos. Modelos como wav2vec 2.0 o HuBERT aprenden representaciones semánticas del habla directamente de la forma de onda, capturando el contenido lingüístico (fonemas, palabras, significado) mientras descartan variaciones acústicas irrelevantes (ruido ambiental, reverberación). Alternativamente, se puede aplicar cuantización vectorial para obtener tokens discretos semánticos, lo que facilita la integración con modelos de lenguaje.

### 8.6.3 Video: de fotogramas a representación espacio-temporal

El video presenta un desafío adicional respecto a las imágenes estáticas: la dimensión temporal. Un video consiste en una secuencia de fotogramas $\mathbf{V} = (\mathbf{I}_1, \mathbf{I}_2, \ldots, \mathbf{I}_F)$ donde cada fotograma $\mathbf{I}_f \in \mathbb{R}^{H \times W \times 3}$ es una imagen en color. La cadena de conversión semántica para video procede en dos etapas:

**Etapa espacial — Extracción de características por fotograma:** Cada fotograma se procesa individualmente mediante una red convolucional (CNN) pre-entrenada (por ejemplo, ResNet-50 o EfficientNet):

$$\mathbf{f}_f = \text{CNN}(\mathbf{I}_f) \in \mathbb{R}^{d_{spatial}}$$

produciendo un vector de características espaciales $\mathbf{f}_f$ que describe el contenido visual de cada fotograma. Alternativamente, redes convolucionales 3D como C3D o SlowFast procesan conjuntamente bloques de fotogramas consecutivos para capturar el movimiento de manera implícita.

**Etapa temporal — Modelado de dependencias entre fotogramas:** La secuencia de características espaciales $(\mathbf{f}_1, \mathbf{f}_2, \ldots, \mathbf{f}_F)$ se procesa mediante un modelo de secuencia —un Transformer temporal o una red LSTM— que captura las dependencias temporales (movimiento de objetos, evolución de escenas, dinámica de acciones):

$$\mathbf{h}_{video} = \text{Transformer}(\mathbf{f}_1, \mathbf{f}_2, \ldots, \mathbf{f}_F) \in \mathbb{R}^{d_{semantic}}$$

El resultado es una representación semántica del video que captura tanto el contenido visual de cada fotograma como la estructura temporal de la secuencia. La redundancia temporal del video (fotogramas consecutivos son muy similares) se elimina automáticamente por el mecanismo de atención del Transformer, que aprende a focalizar la atención en los cambios significativos entre fotogramas.

### 8.6.4 Texto: tokenización y embeddings

Para el texto, la conversión a representación semántica sigue un proceso bien establecido en el procesamiento de lenguaje natural:

**Tokenización:** El texto crudo se segmenta en **tokens** (subpalabras) mediante algoritmos como:

- **BPE (*Byte Pair Encoding*):** Construye iterativamente un vocabulario fusionando los pares de caracteres más frecuentes. Produce un vocabulario de tamaño fijo (típicamente 30,000–50,000 tokens) que puede representar cualquier texto, incluyendo palabras fuera de vocabulario, mediante secuencias de subtokens.

- **WordPiece:** Similar a BPE pero utiliza un criterio de máxima verosimilitud para seleccionar las fusiones, optimizando la probabilidad del corpus de entrenamiento bajo un modelo unigram.

- **SentencePiece:** Una implementación que no asume pre-tokenización por espacios, permitiendo aplicar BPE o unigram directamente sobre texto crudo, lo que es esencial para idiomas sin separadores de palabras (como chino o japonés).

**Embedding:** Cada token $s_i$ del vocabulario se mapea a un vector denso de dimensión $d_{model}$ mediante una tabla de búsqueda (*lookup table*):

$$\mathbf{e}_i = \mathbf{E}[s_i] \in \mathbb{R}^{d_{model}}$$

donde $\mathbf{E} \in \mathbb{R}^{|V| \times d_{model}}$ es la matriz de embeddings, con $|V|$ el tamaño del vocabulario. Los embeddings se inicializan aleatoriamente y se ajustan durante el entrenamiento del sistema E2E.

**Codificación Transformer:** La secuencia de embeddings (con codificación posicional añadida) se procesa a través de las capas del Transformer para producir la representación semántica contextualizada:

$$\mathbf{h}_{text} = \text{TransformerEncoder}(\mathbf{e}_1 + \mathbf{PE}_1, \ldots, \mathbf{e}_L + \mathbf{PE}_L)$$

### 8.6.5 El puente de la tokenización: de señales continuas a unidades semánticas discretas

Un concepto unificador en todas las modalidades es el **puente de tokenización**: la conversión de señales continuas del mundo físico en unidades semánticas discretas o cuasi-discretas que pueden procesarse eficientemente por modelos neuronales. Este puente es un punto de diseño crítico que determina:

- **La granularidad de la representación:** Tokens más finos capturan más detalle pero requieren secuencias más largas; tokens más gruesos son más compactos pero pierden matices.
- **El balance entre compresión y fidelidad:** La cuantización inherente a la tokenización introduce una pérdida de información que debe balancearse con la eficiencia de la transmisión.
- **La adaptabilidad al contenido:** Los mejores sistemas aprenden tokenizaciones adaptativas que asignan más tokens a las partes informativas del contenido y menos a las partes redundantes o predecibles.

### 8.6.6 Superioridad sobre la codificación de fuente tradicional

Los métodos tradicionales de codificación de fuente —JPEG para imágenes, MP3/AAC para audio, H.264/H.265 para video— fueron diseñados con un objetivo fundamentalmente diferente al de la comunicación semántica. Estos códecs se optimizan para **minimizar la tasa de bits** sujeta a una **restricción de distorsión** (típicamente MSE o alguna métrica perceptual simple), operando bajo el paradigma de la teoría de tasa-distorsión de Shannon.

La comunicación semántica E2E supera este paradigma en varios aspectos fundamentales:

1. **Optimización conjunta fuente-canal:** Los códecs tradicionales producen un flujo de bits que luego debe protegerse con codificación de canal. Esta separación es subóptima para longitudes de bloque finitas. El sistema E2E elimina esta separación, optimizando directamente la calidad de la reconstrucción bajo las condiciones reales del canal.

2. **Adaptación al contenido semántico:** JPEG comprime todos los bloques de 8×8 de una imagen de la misma manera, independientemente de su importancia semántica. Un sistema semántico puede asignar más recursos de canal a las regiones semánticamente relevantes (por ejemplo, la cara de una persona en una videollamada) y menos a las regiones de fondo.

3. **Robustez frente a errores de canal:** Cuando un bit protegido por codificación de canal se decodifica erróneamente, el efecto puede ser catastrófico (pérdida de paquetes completos, artefactos de bloque). En un sistema semántico, los errores del canal se manifiestan como degradaciones suaves y distribuidas que preservan la interpretabilidad del contenido.

4. **Eliminación de la interfaz binaria:** Al no requerir la conversión de la representación intermedia a bits, el sistema E2E evita la pérdida de cuantización y puede explotar la naturaleza continua de las señales analógicas de manera más eficiente.

---

## 8.7 Degradación Suave vs. Efecto Acantilado

### 8.7.1 El efecto acantilado en los sistemas clásicos

Los sistemas de comunicación digital convencionales exhiben un comportamiento característico conocido como **efecto acantilado** (*cliff effect* o *threshold effect*). Este fenómeno se manifiesta de la siguiente manera: cuando la SNR del canal está por encima de un cierto umbral (determinado por la tasa de codificación del canal y el esquema de modulación seleccionados), el sistema funciona prácticamente sin errores, con una calidad de recepción excelente. Pero cuando la SNR cae por debajo de ese umbral, la calidad se degrada de manera **abrupta y catastrófica**, pasando de una operación casi perfecta a una falla total en un rango muy estrecho de SNR.

Matemáticamente, este comportamiento se puede entender analizando la probabilidad de error de bit (BER) de un sistema con modulación $M$-QAM y codificación de canal con tasa $R_c$:

$$\text{BER}(\text{SNR}) \approx \frac{4}{\log_2 M}\left(1 - \frac{1}{\sqrt{M}}\right) Q\left(\sqrt{\frac{3 R_c \cdot \text{SNR}}{M-1}}\right)$$

donde $Q(x) = \frac{1}{\sqrt{2\pi}}\int_x^{\infty}e^{-t^2/2}dt$ es la función Q gaussiana, que decae exponencialmente. La transición de BER alta a BER baja ocurre en un rango de SNR de apenas 2–3 dB, creando el "acantilado" en la curva de rendimiento. Con codificación de canal moderna (Turbo, LDPC, Polar) con longitudes de bloque largas, la caída es aún más pronunciada —de $10^{-1}$ a $10^{-6}$ en menos de 1 dB—, lo cual es deseable operativamente pero exacerba el efecto acantilado.

El problema se agrava cuando consideramos la capa de aplicación. Un video codificado con H.264 y transmitido con 16-QAM y código LDPC de tasa 3/4 se verá perfecto si la SNR > 15 dB, pero será completamente ilegible si la SNR < 12 dB. No hay un término medio: el sistema no puede degradar gracefully la calidad del video para adaptarse a la SNR disponible (a menos que se implementen mecanismos de adaptación de enlace, que son complejos e introducen latencia).

### 8.7.2 Degradación suave en los sistemas semánticos

Los sistemas de comunicación semántica E2E exhiben un comportamiento radicalmente diferente: la **degradación suave** (*graceful degradation*). A medida que la SNR disminuye, la calidad de la reconstrucción se degrada de manera **continua y gradual**, sin transiciones abruptas. Incluso a SNR muy bajas, el sistema produce reconstrucciones que, aunque imperfectas, preservan el significado esencial del mensaje original.

Este comportamiento emerge naturalmente de la arquitectura E2E y se puede explicar intuitivamente. En un sistema semántico, la información no se codifica como bits individuales (donde un error en un solo bit puede corromper un símbolo completo), sino como **vectores continuos en un espacio latente**. Cuando el ruido del canal perturba estos vectores, la perturbación se distribuye de manera suave sobre todas las dimensiones de la representación. El decoder, entrenado para reconstruir el significado a partir de representaciones ruidosas, produce una reconstrucción que refleja la *distancia* en el espacio semántico a la representación original, no una reconstrucción perfecta o nula.

### 8.7.3 Análisis matemático comparativo

Para formalizar la comparación, definamos una métrica de calidad semántica $Q(\text{SNR})$ que varía entre 0 (calidad nula, significado completamente perdido) y 1 (calidad perfecta, significado completamente preservado). Para un sistema clásico, esta métrica tiene la forma aproximada de una función escalón:

$$Q_{clasico}(\text{SNR}) \approx \begin{cases} 1 - \epsilon & \text{si } \text{SNR} > \text{SNR}_{th} + \delta \\ \text{transición abrupta} & \text{si } |\text{SNR} - \text{SNR}_{th}| \leq \delta \\ \epsilon' & \text{si } \text{SNR} < \text{SNR}_{th} - \delta \end{cases}$$

donde $\text{SNR}_{th}$ es el umbral del sistema, $\delta \approx 1\text{–}2$ dB es el ancho de la transición (muy estrecho), $\epsilon$ es el error residual a alta SNR (muy pequeño) y $\epsilon'$ es la calidad a baja SNR (esencialmente cero para aplicaciones prácticas).

Para un sistema semántico E2E, la métrica de calidad tiene una forma sigmoidal suave:

$$Q_{semantico}(\text{SNR}) \approx 1 - \frac{C_1}{1 + C_2 \cdot \text{SNR}^{\alpha}}$$

donde $C_1$, $C_2$ y $\alpha$ son constantes que dependen de la arquitectura, la razón de codificación y la distribución de los datos. Esta curva varía suavemente sobre todo el rango de SNR, sin discontinuidades.

Otra forma de analizar la comparación es mediante la **similitud semántica** (por ejemplo, la puntuación BLEU para texto o el SSIM para imágenes) como función de la SNR. Empíricamente, para el sistema DeepSC (Xie et al., 2021, DOI: 10.1109/TSP.2021.3071082), la similitud semántica del texto varía aproximadamente como:

$$\text{SemSim}(\text{SNR}) \approx \text{SemSim}_{max} \left(1 - e^{-\lambda(\text{SNR} - \text{SNR}_0)}\right)$$

para $\text{SNR} > \text{SNR}_0$, donde $\lambda$ controla la tasa de convergencia y $\text{SNR}_0$ es el punto de inflexión. Esta curva exponencial saturante produce una degradación suave.

### 8.7.4 Implicaciones prácticas

La degradación suave tiene implicaciones prácticas profundas:

1. **Robustez ante variaciones del canal:** En entornos inalámbricos donde la SNR fluctúa rápidamente (por ejemplo, comunicaciones vehiculares o IoT en entornos industriales), un sistema con degradación suave mantiene una calidad aceptable incluso durante caídas momentáneas de la SNR, mientras que un sistema clásico experimentaría interrupciones frecuentes.

2. **Simplificación del diseño del sistema:** Los sistemas clásicos requieren mecanismos complejos de **adaptación de enlace** (*link adaptation*) que seleccionan dinámicamente el esquema de modulación y codificación (MCS) óptimo para la SNR actual. Los sistemas semánticos eliminan esta necesidad, ya que un único modelo entrenado para un rango de SNR funciona adecuadamente en todo ese rango.

3. **Eficiencia en el uso del espectro:** Los sistemas clásicos deben diseñarse con márgenes de SNR conservadores para evitar el efecto acantilado, desperdiciando capacidad. Los sistemas semánticos pueden operar más cerca del límite de capacidad porque no hay un acantilado que evitar.

### 8.7.5 Diagrama comparativo

> **Figura 8.4:** Comparación del rendimiento de un sistema clásico y un sistema de comunicación semántica en función de la SNR. El eje horizontal representa la SNR en dB (de $-5$ a 25 dB) y el eje vertical representa la métrica de calidad normalizada $Q$ (de 0 a 1). **Curva azul (Sistema clásico):** muestra una transición abrupta tipo escalón alrededor de $\text{SNR}_{th} \approx 10$ dB. Por debajo de $\sim$8 dB, la calidad es prácticamente cero (efecto acantilado); por encima de $\sim$12 dB, la calidad es casi perfecta. La zona sombreada roja marca la región de falla catastrófica. **Curva roja (Sistema semántico E2E):** muestra una curva sigmoidal suave que mejora gradualmente con la SNR. A 0 dB, la calidad es aproximadamente 0.4 (parcialmente inteligible); a 10 dB, es aproximadamente 0.85; y satura cerca de 0.95 a SNR altas. No hay transición abrupta. La zona sombreada verde marca la región donde el sistema semántico supera al clásico (SNR baja). La zona sombreada azul marca la región donde el sistema clásico es ligeramente superior (SNR alta). Una anotación señala el "crossover point" donde ambas curvas se cruzan (aproximadamente a 11 dB), y otra anotación explica "Degradación suave: calidad proporcional a SNR" para la curva semántica.

---

## 8.8 Implementación Completa en PyTorch

### 8.8.1 Descripción del sistema implementado

A continuación, presentamos una implementación completa y funcional de un sistema de comunicación semántica E2E en PyTorch. El sistema implementa la transmisión de texto a través de un canal AWGN, siguiendo la arquitectura inspirada en DeepSC (Xie et al., 2021, DOI: 10.1109/TSP.2021.3071082). El código incluye todos los componentes discutidos en esta sección: encoder semántico basado en Transformer, encoder de canal con capas densas y normalización de potencia, canal AWGN diferenciable, decoder de canal y decoder semántico autoregresivo.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
import math
import numpy as np

# ===========================================================
# SISTEMA DE COMUNICACIÓN SEMÁNTICA E2E EN PYTORCH
# Basado en la arquitectura DeepSC para transmisión de texto
# ===========================================================

class PositionalEncoding(nn.Module):
    """
    Codificación posicional sinusoidal para el Transformer.
    Añade información de posición a los embeddings de entrada,
    permitiendo que el modelo distinga entre tokens en diferentes
    posiciones de la secuencia.
    """
    def __init__(self, d_model, max_len=512, dropout=0.1):
        super().__init__()
        self.dropout = nn.Dropout(p=dropout)

        # Crear la matriz de codificación posicional [max_len, d_model]
        pe = torch.zeros(max_len, d_model)
        position = torch.arange(0, max_len, dtype=torch.float).unsqueeze(1)
        # Factor de escala exponencial para las frecuencias
        div_term = torch.exp(
            torch.arange(0, d_model, 2).float()
            * (-math.log(10000.0) / d_model)
        )
        # Componentes seno (dimensiones pares) y coseno (impares)
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)
        pe = pe.unsqueeze(0)  # [1, max_len, d_model]
        self.register_buffer('pe', pe)

    def forward(self, x):
        # x: [batch_size, seq_len, d_model]
        x = x + self.pe[:, :x.size(1), :]
        return self.dropout(x)


class SemanticEncoder(nn.Module):
    """
    Encoder Semántico basado en Transformer.
    Transforma la secuencia de tokens de entrada en una
    representación semántica densa que captura el significado
    del mensaje completo.
    """
    def __init__(self, vocab_size, d_model=128, nhead=8,
                 num_layers=3, dim_feedforward=512, dropout=0.1):
        super().__init__()
        self.d_model = d_model

        # Capa de embedding: mapea índices de tokens a vectores densos
        self.embedding = nn.Embedding(vocab_size, d_model)
        self.pos_encoder = PositionalEncoding(d_model, dropout=dropout)

        # Capas del Transformer Encoder
        encoder_layer = nn.TransformerEncoderLayer(
            d_model=d_model,
            nhead=nhead,
            dim_feedforward=dim_feedforward,
            dropout=dropout,
            batch_first=True
        )
        self.transformer_encoder = nn.TransformerEncoder(
            encoder_layer, num_layers=num_layers
        )

        # Capa de proyección: reduce la representación del Transformer
        # a un vector semántico de dimensión fija
        self.fc_semantic = nn.Linear(d_model, d_model)

    def forward(self, src, src_mask=None, src_key_padding_mask=None):
        """
        Args:
            src: Tensor de tokens [batch_size, seq_len]
            src_mask: Máscara de atención opcional
            src_key_padding_mask: Máscara de padding [batch_size, seq_len]
        Returns:
            h: Representación semántica [batch_size, seq_len, d_model]
        """
        # Embedding con escalado por sqrt(d_model) para estabilizar
        x = self.embedding(src) * math.sqrt(self.d_model)
        x = self.pos_encoder(x)

        # Procesamiento por las capas de Transformer
        h = self.transformer_encoder(
            x, mask=src_mask,
            src_key_padding_mask=src_key_padding_mask
        )

        # Proyección semántica
        h = self.fc_semantic(h)
        return h


class ChannelEncoder(nn.Module):
    """
    Encoder de Canal: transforma la representación semántica
    en símbolos de canal con normalización de potencia.
    Mapea del espacio semántico (d_model dimensiones) al
    espacio de canal (channel_dim dimensiones = 2n para n
    símbolos complejos).
    """
    def __init__(self, d_model=128, channel_dim=32):
        super().__init__()
        self.channel_dim = channel_dim

        # Red de capas densas para la codificación de canal
        self.encoder = nn.Sequential(
            nn.Linear(d_model, 256),
            nn.ReLU(),
            nn.Linear(256, channel_dim)
        )

    def power_normalize(self, z):
        """
        Normalización de potencia: asegura E[||z||^2] = channel_dim.
        Cada vector de símbolos se normaliza para tener potencia
        unitaria por dimensión.
        """
        # Calcular la potencia promedio por muestra del lote
        batch_power = torch.mean(z ** 2, dim=-1, keepdim=True)
        # Normalizar para potencia unitaria por dimensión
        z_norm = z / torch.sqrt(batch_power + 1e-8)
        return z_norm

    def forward(self, h):
        """
        Args:
            h: Representación semántica [batch_size, seq_len, d_model]
        Returns:
            z: Símbolos de canal normalizados
               [batch_size, seq_len, channel_dim]
        """
        z = self.encoder(h)
        z = self.power_normalize(z)
        return z


class AWGNChannel(nn.Module):
    """
    Canal AWGN diferenciable.
    Implementa y = z + n, donde n ~ N(0, sigma^2 * I).
    Utiliza el truco de reparametrización: y = z + sigma * epsilon,
    con epsilon ~ N(0, I), para permitir la retropropagación
    de gradientes a través del canal.
    """
    def __init__(self):
        super().__init__()

    def forward(self, z, snr_db):
        """
        Args:
            z: Señal transmitida [batch_size, seq_len, channel_dim]
            snr_db: Relación señal a ruido en dB (escalar o tensor)
        Returns:
            y: Señal recibida con ruido [batch_size, seq_len, channel_dim]
        """
        if self.training:
            # Convertir SNR de dB a escala lineal
            snr_linear = 10.0 ** (snr_db / 10.0)
            # Calcular la potencia de la señal (ya normalizada a ~1)
            signal_power = torch.mean(z ** 2)
            # Calcular varianza del ruido: sigma^2 = P / SNR
            noise_std = torch.sqrt(signal_power / snr_linear)
            # Truco de reparametrización: muestrear epsilon ~ N(0, I)
            # y escalar por sigma
            epsilon = torch.randn_like(z)
            y = z + noise_std * epsilon
            return y
        else:
            # En modo evaluación, también añadir ruido para simular
            # condiciones reales del canal
            snr_linear = 10.0 ** (snr_db / 10.0)
            signal_power = torch.mean(z ** 2)
            noise_std = torch.sqrt(signal_power / snr_linear)
            epsilon = torch.randn_like(z)
            y = z + noise_std * epsilon
            return y


class RayleighChannel(nn.Module):
    """
    Canal con desvanecimiento Rayleigh diferenciable.
    Implementa y = h ⊙ z + n, donde h ~ CN(0, I) y n ~ N(0, σ²I).
    """
    def __init__(self):
        super().__init__()

    def forward(self, z, snr_db):
        """
        Args:
            z: Señal transmitida [batch_size, seq_len, channel_dim]
            snr_db: Relación señal a ruido en dB
        Returns:
            y: Señal recibida [batch_size, seq_len, channel_dim]
        """
        snr_linear = 10.0 ** (snr_db / 10.0)
        signal_power = torch.mean(z ** 2)
        noise_std = torch.sqrt(signal_power / snr_linear)

        # Coeficientes de desvanecimiento Rayleigh (reparametrizados)
        # Para canal real: |h| ~ Rayleigh, implementado como
        # h = h_real donde h_real ~ N(0, 1/sqrt(2))
        h = torch.randn_like(z) * (1.0 / math.sqrt(2.0))
        epsilon = torch.randn_like(z)

        # y = h ⊙ z + sigma * epsilon
        y = h * z + noise_std * epsilon
        return y


class ChannelDecoder(nn.Module):
    """
    Decoder de Canal: recupera la representación semántica
    a partir de la señal recibida ruidosa.
    Arquitectura espejo del encoder de canal.
    """
    def __init__(self, channel_dim=32, d_model=128):
        super().__init__()
        self.decoder = nn.Sequential(
            nn.Linear(channel_dim, 256),
            nn.ReLU(),
            nn.Linear(256, d_model)
        )

    def forward(self, y):
        """
        Args:
            y: Señal recibida [batch_size, seq_len, channel_dim]
        Returns:
            h_hat: Representación semántica estimada
                   [batch_size, seq_len, d_model]
        """
        h_hat = self.decoder(y)
        return h_hat


class SemanticDecoder(nn.Module):
    """
    Decoder Semántico basado en Transformer.
    Reconstruye la secuencia de tokens a partir de la
    representación semántica recuperada.
    """
    def __init__(self, vocab_size, d_model=128, nhead=8,
                 num_layers=3, dim_feedforward=512, dropout=0.1):
        super().__init__()
        self.d_model = d_model

        # Capas del Transformer Decoder
        decoder_layer = nn.TransformerDecoderLayer(
            d_model=d_model,
            nhead=nhead,
            dim_feedforward=dim_feedforward,
            dropout=dropout,
            batch_first=True
        )
        self.transformer_decoder = nn.TransformerDecoder(
            decoder_layer, num_layers=num_layers
        )

        # Proyección final al vocabulario
        self.fc_out = nn.Linear(d_model, vocab_size)

    def forward(self, h_hat, tgt_embedding,
                tgt_mask=None, tgt_key_padding_mask=None):
        """
        Args:
            h_hat: Representación semántica recuperada (memoria)
                   [batch_size, seq_len_src, d_model]
            tgt_embedding: Embeddings del objetivo (teacher forcing)
                           [batch_size, seq_len_tgt, d_model]
            tgt_mask: Máscara causal para generación autoregresiva
            tgt_key_padding_mask: Máscara de padding del objetivo
        Returns:
            logits: Distribución sobre vocabulario
                    [batch_size, seq_len_tgt, vocab_size]
        """
        decoded = self.transformer_decoder(
            tgt_embedding, h_hat,
            tgt_mask=tgt_mask,
            tgt_key_padding_mask=tgt_key_padding_mask
        )
        logits = self.fc_out(decoded)
        return logits


class E2ESemanticCommSystem(nn.Module):
    """
    Sistema de Comunicación Semántica E2E completo.
    Integra todos los componentes: encoder semántico, encoder de canal,
    canal físico (AWGN o Rayleigh), decoder de canal y decoder semántico.
    """
    def __init__(self, vocab_size, d_model=128, nhead=8,
                 num_encoder_layers=3, num_decoder_layers=3,
                 dim_feedforward=512, channel_dim=32,
                 channel_type='awgn', dropout=0.1):
        super().__init__()
        self.d_model = d_model
        self.vocab_size = vocab_size

        # Componentes del transmisor
        self.semantic_encoder = SemanticEncoder(
            vocab_size, d_model, nhead,
            num_encoder_layers, dim_feedforward, dropout
        )
        self.channel_encoder = ChannelEncoder(d_model, channel_dim)

        # Canal físico
        if channel_type == 'awgn':
            self.channel = AWGNChannel()
        elif channel_type == 'rayleigh':
            self.channel = RayleighChannel()
        else:
            raise ValueError(
                f"Tipo de canal '{channel_type}' no soportado. "
                f"Usar 'awgn' o 'rayleigh'."
            )

        # Componentes del receptor
        self.channel_decoder = ChannelDecoder(channel_dim, d_model)
        self.semantic_decoder = SemanticDecoder(
            vocab_size, d_model, nhead,
            num_decoder_layers, dim_feedforward, dropout
        )

        # Embedding compartido (opcional) para el decoder
        self.tgt_embedding = nn.Embedding(vocab_size, d_model)
        self.tgt_pos_encoder = PositionalEncoding(d_model, dropout=dropout)

    def generate_square_subsequent_mask(self, sz):
        """
        Genera máscara causal triangular superior para el decoder.
        Impide que la posición i atienda a posiciones j > i,
        forzando la generación autoregresiva.
        """
        mask = torch.triu(torch.ones(sz, sz), diagonal=1).bool()
        return mask

    def forward(self, src, tgt, snr_db,
                src_key_padding_mask=None,
                tgt_key_padding_mask=None):
        """
        Propagación hacia adelante completa del sistema E2E.

        Args:
            src: Tokens de entrada [batch_size, src_len]
            tgt: Tokens objetivo [batch_size, tgt_len]
            snr_db: SNR del canal en dB
            src_key_padding_mask: Máscara de padding de la fuente
            tgt_key_padding_mask: Máscara de padding del objetivo
        Returns:
            logits: Predicciones sobre el vocabulario
                    [batch_size, tgt_len, vocab_size]
        """
        # === TRANSMISOR ===
        # Paso 1: Codificación semántica
        h = self.semantic_encoder(
            src, src_key_padding_mask=src_key_padding_mask
        )

        # Paso 2: Codificación de canal + normalización de potencia
        z = self.channel_encoder(h)

        # === CANAL FÍSICO ===
        # Paso 3: Transmisión a través del canal ruidoso
        y = self.channel(z, snr_db)

        # === RECEPTOR ===
        # Paso 4: Decodificación de canal
        h_hat = self.channel_decoder(y)

        # Paso 5: Decodificación semántica (con teacher forcing)
        tgt_emb = self.tgt_embedding(tgt) * math.sqrt(self.d_model)
        tgt_emb = self.tgt_pos_encoder(tgt_emb)
        tgt_mask = self.generate_square_subsequent_mask(
            tgt.size(1)
        ).to(tgt.device)

        logits = self.semantic_decoder(
            h_hat, tgt_emb,
            tgt_mask=tgt_mask,
            tgt_key_padding_mask=tgt_key_padding_mask
        )

        return logits


# ===========================================================
# FUNCIONES DE ENTRENAMIENTO
# ===========================================================

class SNRScheduler:
    """
    Programador de SNR para entrenamiento con currículo.
    Comienza con SNR alta (canal fácil) y gradualmente
    reduce la SNR (canal más difícil).
    """
    def __init__(self, snr_max=20.0, snr_min=0.0,
                 total_epochs=100, mode='linear'):
        self.snr_max = snr_max
        self.snr_min = snr_min
        self.total_epochs = total_epochs
        self.mode = mode

    def get_snr(self, epoch):
        """Calcula la SNR para la época actual."""
        if self.mode == 'linear':
            progress = min(epoch / self.total_epochs, 1.0)
            return self.snr_max - progress * (self.snr_max - self.snr_min)
        elif self.mode == 'cosine':
            progress = min(epoch / self.total_epochs, 1.0)
            return self.snr_min + 0.5 * (self.snr_max - self.snr_min) \
                   * (1 + math.cos(math.pi * progress))
        elif self.mode == 'random':
            # SNR aleatoria uniforme en [snr_min, snr_max]
            return np.random.uniform(self.snr_min, self.snr_max)
        else:
            raise ValueError(f"Modo '{self.mode}' no reconocido.")


def train_epoch(model, dataloader, optimizer, snr_db,
                pad_idx, device):
    """
    Entrena el modelo durante una época completa.

    Args:
        model: Sistema E2E de comunicación semántica
        dataloader: DataLoader con pares (src, tgt) de texto
        optimizer: Optimizador (Adam recomendado)
        snr_db: SNR del canal para esta época
        pad_idx: Índice del token de padding en el vocabulario
        device: Dispositivo de cómputo (CPU o GPU)

    Returns:
        avg_loss: Pérdida promedio de la época
    """
    model.train()
    total_loss = 0
    num_batches = 0

    for batch_idx, (src, tgt) in enumerate(dataloader):
        src = src.to(device)     # [batch_size, src_len]
        tgt = tgt.to(device)     # [batch_size, tgt_len]

        # Preparar entrada y objetivo del decoder
        # (desplazamiento de un token para teacher forcing)
        tgt_input = tgt[:, :-1]  # Todos menos el último token
        tgt_label = tgt[:, 1:]   # Todos menos el primer token

        # Crear máscaras de padding
        src_pad_mask = (src == pad_idx)
        tgt_pad_mask = (tgt_input == pad_idx)

        # Paso 1: Forward pass completo
        optimizer.zero_grad()
        logits = model(
            src, tgt_input, snr_db,
            src_key_padding_mask=src_pad_mask,
            tgt_key_padding_mask=tgt_pad_mask
        )

        # Paso 2: Calcular pérdida de entropía cruzada
        # Reshape para compatibilidad con cross_entropy:
        # logits: [batch * tgt_len, vocab_size]
        # labels: [batch * tgt_len]
        loss = F.cross_entropy(
            logits.reshape(-1, logits.size(-1)),
            tgt_label.reshape(-1),
            ignore_index=pad_idx
        )

        # Paso 3: Retropropagación a través de todo el sistema,
        # incluyendo el canal (gracias a la reparametrización)
        loss.backward()

        # Gradient clipping para estabilidad
        torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)

        # Paso 4: Actualización conjunta de todos los parámetros
        optimizer.step()

        total_loss += loss.item()
        num_batches += 1

    avg_loss = total_loss / max(num_batches, 1)
    return avg_loss


@torch.no_grad()
def evaluate(model, dataloader, snr_db, pad_idx, device):
    """
    Evalúa el modelo en un conjunto de datos de validación.

    Args:
        model: Sistema E2E
        dataloader: DataLoader de validación
        snr_db: SNR del canal para evaluación
        pad_idx: Índice del token de padding
        device: Dispositivo de cómputo

    Returns:
        avg_loss: Pérdida promedio de validación
    """
    model.eval()
    total_loss = 0
    num_batches = 0

    for src, tgt in dataloader:
        src = src.to(device)
        tgt = tgt.to(device)

        tgt_input = tgt[:, :-1]
        tgt_label = tgt[:, 1:]

        src_pad_mask = (src == pad_idx)
        tgt_pad_mask = (tgt_input == pad_idx)

        logits = model(
            src, tgt_input, snr_db,
            src_key_padding_mask=src_pad_mask,
            tgt_key_padding_mask=tgt_pad_mask
        )

        loss = F.cross_entropy(
            logits.reshape(-1, logits.size(-1)),
            tgt_label.reshape(-1),
            ignore_index=pad_idx
        )

        total_loss += loss.item()
        num_batches += 1

    return total_loss / max(num_batches, 1)


def train_e2e_system(model, train_loader, val_loader,
                     num_epochs=100, lr=1e-4, pad_idx=0,
                     snr_max=20.0, snr_min=0.0,
                     snr_mode='linear', device='cpu'):
    """
    Bucle de entrenamiento completo con currículo de SNR.

    Args:
        model: Sistema E2E de comunicación semántica
        train_loader: DataLoader de entrenamiento
        val_loader: DataLoader de validación
        num_epochs: Número de épocas de entrenamiento
        lr: Tasa de aprendizaje inicial
        pad_idx: Índice del token de padding
        snr_max: SNR máxima (dB) al inicio del entrenamiento
        snr_min: SNR mínima (dB) al final del entrenamiento
        snr_mode: Modo del programador de SNR
        device: Dispositivo de cómputo
    """
    model = model.to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=lr, betas=(0.9, 0.999))

    # Programador de tasa de aprendizaje con calentamiento
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(
        optimizer, T_max=num_epochs, eta_min=lr * 0.01
    )

    # Programador de SNR con currículo
    snr_scheduler = SNRScheduler(
        snr_max=snr_max, snr_min=snr_min,
        total_epochs=num_epochs, mode=snr_mode
    )

    best_val_loss = float('inf')

    for epoch in range(num_epochs):
        # Obtener SNR para esta época (currículo)
        current_snr = snr_scheduler.get_snr(epoch)

        # Entrenamiento
        train_loss = train_epoch(
            model, train_loader, optimizer,
            current_snr, pad_idx, device
        )

        # Validación (evaluada a múltiples SNR)
        val_loss = evaluate(
            model, val_loader, current_snr, pad_idx, device
        )

        # Actualizar tasa de aprendizaje
        scheduler.step()

        # Guardar mejor modelo
        if val_loss < best_val_loss:
            best_val_loss = val_loss
            torch.save(model.state_dict(), 'best_semcom_model.pth')

        # Registro de progreso
        if (epoch + 1) % 10 == 0:
            print(
                f"Época [{epoch+1}/{num_epochs}] | "
                f"SNR: {current_snr:.1f} dB | "
                f"Pérdida Train: {train_loss:.4f} | "
                f"Pérdida Val: {val_loss:.4f} | "
                f"LR: {scheduler.get_last_lr()[0]:.6f}"
            )


# ===========================================================
# EJEMPLO DE USO
# ===========================================================

if __name__ == "__main__":
    # Hiperparámetros del sistema
    VOCAB_SIZE = 30000    # Tamaño del vocabulario (BPE tokens)
    D_MODEL = 128         # Dimensión del modelo Transformer
    NHEAD = 8             # Número de cabezas de atención
    NUM_ENC_LAYERS = 3    # Capas del encoder Transformer
    NUM_DEC_LAYERS = 3    # Capas del decoder Transformer
    DIM_FF = 512          # Dimensión de la red feed-forward
    CHANNEL_DIM = 16      # Dimensión del canal (2n para n símbolos)
    CHANNEL_TYPE = 'awgn' # Tipo de canal: 'awgn' o 'rayleigh'
    DROPOUT = 0.1         # Probabilidad de dropout

    # Crear el sistema E2E
    system = E2ESemanticCommSystem(
        vocab_size=VOCAB_SIZE,
        d_model=D_MODEL,
        nhead=NHEAD,
        num_encoder_layers=NUM_ENC_LAYERS,
        num_decoder_layers=NUM_DEC_LAYERS,
        dim_feedforward=DIM_FF,
        channel_dim=CHANNEL_DIM,
        channel_type=CHANNEL_TYPE,
        dropout=DROPOUT
    )

    # Contar parámetros totales del sistema
    total_params = sum(p.numel() for p in system.parameters())
    trainable_params = sum(
        p.numel() for p in system.parameters() if p.requires_grad
    )
    print(f"Parámetros totales: {total_params:,}")
    print(f"Parámetros entrenables: {trainable_params:,}")
    print(f"Razón de codificación k/n: "
          f"{D_MODEL}/{CHANNEL_DIM} = {D_MODEL/CHANNEL_DIM:.2f}")

    # Ejemplo de forward pass con datos sintéticos
    batch_size = 4
    src_len = 20
    tgt_len = 20
    snr_db = 10.0  # 10 dB

    src = torch.randint(1, VOCAB_SIZE, (batch_size, src_len))
    tgt = torch.randint(1, VOCAB_SIZE, (batch_size, tgt_len))

    # Forward pass
    logits = system(src, tgt[:, :-1], snr_db)
    print(f"\nForward pass exitoso:")
    print(f"  Entrada: {src.shape}")
    print(f"  Salida (logits): {logits.shape}")
    print(f"  SNR del canal: {snr_db} dB")
```

### 8.8.2 Explicación detallada de los componentes del código

El código anterior implementa cada componente del sistema E2E tal como se describió en las subsecciones anteriores. A continuación, detallamos los aspectos más relevantes de la implementación:

**Clase `PositionalEncoding`:** Implementa la codificación posicional sinusoidal estándar del Transformer. La matriz de codificaciones se pre-calcula para todas las posiciones hasta `max_len` y se almacena como un buffer (no como parámetro entrenable) mediante `register_buffer`. Esto es eficiente porque la codificación posicional no cambia durante el entrenamiento.

**Clase `SemanticEncoder`:** El encoder semántico utiliza `nn.TransformerEncoderLayer` de PyTorch, que internamente implementa la auto-atención multi-cabeza, las conexiones residuales, la normalización de capa y la red *feed-forward*. La capa de embedding incluye el escalado por $\sqrt{d_{model}}$, que es una práctica estándar para estabilizar los gradientes durante el entrenamiento (compensando el hecho de que los embeddings se inicializan con valores pequeños).

**Clase `ChannelEncoder`:** La codificación de canal se realiza mediante dos capas densas con activación ReLU intermedia. La función `power_normalize` implementa la normalización de potencia dividiendo cada vector de símbolos por su norma RMS (raíz cuadrada de la media de los cuadrados), lo que garantiza que la potencia promedio por dimensión sea unitaria.

**Clases `AWGNChannel` y `RayleighChannel`:** Estas clases implementan los canales diferenciables. Observe cómo la reparametrización se aplica explícitamente: primero se genera $\boldsymbol{\epsilon} \sim \mathcal{N}(\mathbf{0}, \mathbf{I})$ con `torch.randn_like(z)`, y luego se escala por $\sigma$ para obtener el ruido con la varianza deseada. Dado que `torch.randn_like` genera tensores que no forman parte del grafo computacional de los parámetros, pero $\mathbf{z}$ sí lo es, los gradientes pueden fluir a través de la suma $\mathbf{y} = \mathbf{z} + \sigma\boldsymbol{\epsilon}$ sin problemas.

**Clase `SemanticDecoder`:** El decoder semántico utiliza `nn.TransformerDecoderLayer`, que implementa la auto-atención enmascarada (causal), la atención cruzada con la representación del encoder, y la red *feed-forward*. La máscara causal, generada por `generate_square_subsequent_mask`, es una matriz triangular superior booleana que impide que la posición $i$ atienda a posiciones $j > i$, forzando la generación autoregresiva durante el entrenamiento.

**Función `train_epoch`:** Implementa el bucle de entrenamiento estándar con *teacher forcing*: al decoder se le proporciona la secuencia objetivo desplazada un token (`tgt[:, :-1]`) como entrada, y se le pide predecir la secuencia objetivo desplazada en la otra dirección (`tgt[:, 1:]`). El *gradient clipping* (limitación de la norma del gradiente a 1.0) es una técnica importante para la estabilidad del entrenamiento de Transformers, que son propensos a gradientes explosivos.

**Clase `SNRScheduler`:** Implementa tres estrategias de programación de SNR: lineal (decrecimiento uniforme), coseno (decrecimiento suave con inicio y final lentos) y aleatorio (SNR uniformemente distribuida en cada época). La estrategia coseno es generalmente preferida en la práctica, ya que proporciona una transición más suave y dedica más tiempo tanto a SNR altas (aprendizaje de representaciones) como a SNR bajas (aprendizaje de robustez).

---

## 8.9 Resumen y Conexiones

En esta sección hemos desarrollado de manera exhaustiva los sistemas de comunicación semántica de extremo a extremo, desde sus fundamentos arquitectónicos hasta su implementación práctica. Los puntos clave son:

1. **Diseño conjunto:** La fusión de la codificación de fuente, la codificación de canal y la modulación en una única red neuronal diferenciable permite una optimización global que supera el rendimiento de los sistemas diseñados por separado, especialmente en regímenes de longitud de bloque finita.

2. **Canal diferenciable:** El modelado del canal físico como una capa estocástica diferenciable, junto con el truco de reparametrización, permite que los gradientes fluyan a través de todo el sistema durante el entrenamiento.

3. **Funciones de pérdida semánticas:** La elección de funciones de pérdida que operan a nivel de significado —como la similitud coseno de embeddings o la pérdida perceptual— es fundamental para que el sistema optimice la fidelidad semántica en lugar de la fidelidad bit a bit.

4. **Degradación suave:** Una de las propiedades más valiosas de los sistemas E2E es la degradación gradual de la calidad con la SNR, en contraste con el efecto acantilado catastrófico de los sistemas convencionales.

Los sistemas aquí descritos constituyen la base sobre la cual se construyen las variantes más avanzadas que se explorarán en las secciones posteriores: sistemas adaptativos, sistemas multi-usuario, y sistemas con retroalimentación semántica.

---

### Referencias

- Xie, H., Qin, Z., Li, G. Y., & Juang, B.-H. (2021). Deep learning enabled semantic communication systems. *IEEE Transactions on Signal Processing*, 69, 2663–2675. DOI: [10.1109/TSP.2021.3071082](https://doi.org/10.1109/TSP.2021.3071082)

- Bourtsoulatze, E., Kurka, D. B., & Gündüz, D. (2019). Deep joint source-channel coding for wireless image transmission. *IEEE Transactions on Cognitive Communications and Networking*, 5(3), 567–579. DOI: [10.1109/TCCN.2019.2919300](https://doi.org/10.1109/TCCN.2019.2919300)

- Farsad, N., Rao, M., & Goldsmith, A. (2018). Deep learning for joint source-channel coding of text. *IEEE Transactions on Communications*, 66(11), 5765–5775. DOI: [10.1109/TCOMM.2018.2827020](https://doi.org/10.1109/TCOMM.2018.2827020)

---

# 9. Temas Avanzados en Comunicaciones Semánticas

Las secciones anteriores de este tutorial han establecido los fundamentos teóricos, las arquitecturas basadas en aprendizaje profundo y los esquemas de codificación conjunta fuente-canal para comunicaciones semánticas. En esta sección, nos adentramos en los temas más avanzados y las fronteras de investigación que están definiendo el futuro de esta disciplina. Desde la conformación inteligente de formas de onda hasta la integración con sistemas MIMO masivo, desde las bandas de frecuencia milimétricas y de terahercios hasta la convergencia con sensing integrado, cada uno de estos temas representa una dirección de investigación activa con profundas implicaciones para las redes de sexta generación (6G). Abordaremos también el papel transformador de los modelos fundacionales multimodales, el aprendizaje federado como mecanismo de entrenamiento distribuido y privado, la necesidad de un plano de control semántico, y finalmente, las perspectivas futuras que situarán a las comunicaciones semánticas como un pilar fundamental de las arquitecturas 6G (Luo et al., 2022, DOI: 10.1109/COMST.2022.3195590).

---

## 9.1 Conformación de formas de onda semánticas

### 9.1.1 Diseño tradicional de formas de onda

En los sistemas de comunicación convencionales, el diseño de la forma de onda constituye una etapa claramente separada dentro de la cadena de transmisión. Las técnicas de modulación y multiplexación determinan cómo los bits de información se mapean a señales analógicas para su transmisión a través del canal físico. Las dos formas de onda dominantes en las comunicaciones móviles modernas son OFDM (*Orthogonal Frequency Division Multiplexing*) y SC-FDMA (*Single Carrier Frequency Division Multiple Access*).

En OFDM, el ancho de banda disponible se divide en $N$ subportadoras ortogonales, cada una de las cuales transporta un símbolo modulado de manera independiente. La señal transmitida en el dominio del tiempo puede expresarse como:

$$x(t) = \sum_{k=0}^{N-1} X[k] \, e^{j2\pi f_k t}, \quad 0 \leq t \leq T_s$$

donde $X[k]$ es el símbolo complejo asignado a la $k$-ésima subportadora, $f_k = f_0 + k\Delta f$ es la frecuencia de dicha subportadora con espaciado $\Delta f = 1/T_s$, y $T_s$ es la duración del símbolo OFDM. La ortogonalidad entre subportadoras garantiza que:

$$\int_0^{T_s} e^{j2\pi f_k t} \cdot e^{-j2\pi f_m t} \, dt = \begin{cases} T_s & \text{si } k = m \\ 0 & \text{si } k \neq m \end{cases}$$

Esta propiedad permite que cada subportadora sea demodulada independientemente en el receptor mediante una transformada rápida de Fourier (FFT), lo que simplifica enormemente la ecualización en canales con desvanecimiento selectivo en frecuencia. Sin embargo, OFDM presenta limitaciones: una alta relación potencia pico a potencia media (PAPR, *Peak-to-Average Power Ratio*), sensibilidad al desplazamiento de frecuencia Doppler, y la necesidad de un prefijo cíclico que reduce la eficiencia espectral.

SC-FDMA, utilizada en el enlace ascendente de LTE, aborda el problema del PAPR al realizar un pre-codificación DFT antes de la asignación de subportadoras, produciendo una señal con características más cercanas a una portadora única:

$$\tilde{X}[k] = \frac{1}{\sqrt{M}} \sum_{m=0}^{M-1} x[m] \, e^{-j2\pi mk/M}$$

donde $x[m]$ son los símbolos en el dominio del tiempo y $M$ es el número de símbolos agrupados. Esta transformación reduce significativamente el PAPR, lo cual es crítico para dispositivos móviles con amplificadores de potencia limitados.

En ambos casos, los símbolos $X[k]$ provienen de constelaciones de modulación predefinidas como QPSK, 16-QAM o 64-QAM, donde cada punto de la constelación corresponde a una secuencia fija de bits. Por ejemplo, en 16-QAM, los 16 puntos de la constelación se distribuyen en una cuadrícula regular en el plano complejo:

$$X \in \left\{ (\pm 1 \pm j\cdot 3, \pm 3 \pm j\cdot 1, \pm 1 \pm j\cdot 1, \pm 3 \pm j\cdot 3) \cdot d_{\min}/2 \right\}$$

donde $d_{\min}$ es la distancia mínima entre puntos. Esta distribución uniforme y simétrica está diseñada para maximizar la distancia euclidiana mínima bajo una restricción de potencia promedio, optimizando así la tasa de error de bit (BER) en canales con ruido gaussiano aditivo blanco (AWGN).

### 9.1.2 Formas de onda aprendidas: el codificador de canal como conformador

El paradigma de comunicaciones semánticas introduce un cambio radical en el diseño de formas de onda. En lugar de separar las etapas de codificación fuente, codificación de canal y modulación, un sistema semántico extremo a extremo integra todas estas funciones en una red neuronal conjunta. El resultado es que la salida del codificador de canal neuronal **es directamente la forma de onda transmitida**, sin necesidad de pasar por un modulador convencional.

Formalmente, sea $\mathbf{s}$ la fuente semántica (texto, imagen, audio) y $f_\theta(\cdot)$ el codificador semántico conjunto parametrizado por $\theta$. La señal transmitida se genera como:

$$\mathbf{x} = f_\theta(\mathbf{s}) \in \mathbb{C}^n$$

donde $\mathbf{x}$ es un vector de $n$ símbolos complejos que se transmiten directamente a través del canal. No existe una etapa separada de mapeo a constelación: la red neuronal aprende simultáneamente a extraer características semánticas, comprimir la información, protegerla contra errores del canal y conformar la señal para cumplir con restricciones físicas.

Para que esta forma de onda aprendida sea físicamente realizable, debe cumplir con la restricción de potencia promedio:

$$\frac{1}{n} \mathbb{E}\left[\|\mathbf{x}\|^2\right] \leq P_{\max}$$

Esta restricción se implementa típicamente mediante una capa de normalización al final del codificador. Una implementación común es la normalización por lote (*batch normalization*):

$$\mathbf{x}_{\text{norm}} = \sqrt{nP_{\max}} \cdot \frac{\mathbf{x}}{\|\mathbf{x}\|}$$

que garantiza que la potencia total transmitida sea exactamente $nP_{\max}$.

### 9.1.3 Densidad espectral de potencia y restricciones regulatorias

Además de la restricción de potencia total, las señales transmitidas deben cumplir con restricciones sobre la densidad espectral de potencia (PSD, *Power Spectral Density*). Las regulaciones de espectro imponen máscaras espectrales que limitan la potencia emitida en cada banda de frecuencia:

$$S_x(f) \leq S_{\text{máscara}}(f), \quad \forall f$$

donde $S_x(f) = \lim_{T\to\infty} \frac{1}{T}\mathbb{E}\left[|X_T(f)|^2\right]$ es la PSD de la señal transmitida y $S_{\text{máscara}}(f)$ es la máscara espectral regulatoria. Incorporar esta restricción en el entrenamiento de una red neuronal no es trivial, ya que implica una restricción en el dominio de la frecuencia sobre una señal generada en el dominio del tiempo.

Una solución propuesta es incluir un término de penalización en la función de pérdida del entrenamiento:

$$\mathcal{L}_{\text{total}} = \mathcal{L}_{\text{semántica}} + \lambda_{\text{PSD}} \cdot \max\left(0, \max_f \left[S_x(f) - S_{\text{máscara}}(f)\right]\right)$$

donde $\mathcal{L}_{\text{semántica}}$ es la pérdida de distorsión semántica (por ejemplo, pérdida de similitud SSIM para imágenes o BLEU para texto) y $\lambda_{\text{PSD}}$ es un multiplicador que controla la importancia de la restricción espectral. Alternativamente, se pueden utilizar filtros conformadores de espectro diferenciables como capas finales de la red, permitiendo que el gradiente fluya a través de ellos durante el entrenamiento.

### 9.1.4 Constelaciones aprendidas vs. constelaciones tradicionales

Una de las propiedades más fascinantes de las formas de onda semánticas es que los puntos en el espacio de señal ya no se distribuyen según patrones geométricos regulares (cuadrículas QAM, anillos PSK), sino que adoptan distribuciones aprendidas y adaptadas al canal y a la tarea semántica.

En un autoencoder de comunicación entrenado extremo a extremo, si visualizamos la distribución de los símbolos transmitidos en el plano complejo $(\text{Re}(x), \text{Im}(x))$, observamos que los puntos de la "constelación aprendida" presentan las siguientes características:

1. **Distribución no uniforme**: los puntos se agrupan de manera desigual, con mayor densidad en regiones del espacio de señal que corresponden a características semánticas frecuentes o importantes.

2. **Geometría adaptada al canal**: en un canal AWGN, los puntos tienden a distribuirse en configuraciones que maximizan la distancia mínima, similares pero no idénticas a QAM. En canales con desvanecimiento Rayleigh, la distribución se adapta para ser más robusta, con puntos más separados y agrupaciones que explotan la diversidad.

3. **Codificación semántica implícita**: puntos que corresponden a características semánticas similares (por ejemplo, imágenes del mismo objeto con diferentes orientaciones) se mapean a regiones cercanas del espacio de señal, creando una estructura de código continuo que permite una degradación graceful.

4. **Adaptación a la relación señal a ruido (SNR)**: a SNR bajas, la constelación se "contrae" hacia configuraciones más simples con mayor separación entre puntos, mientras que a SNR altas, los puntos se distribuyen más finamente para aprovechar la alta capacidad del canal.

La relación entre la distancia semántica y la distancia euclidiana en el espacio de señal puede formalizarse como:

$$d_{\text{semántica}}(\mathbf{s}_i, \mathbf{s}_j) \propto \|\mathbf{x}_i - \mathbf{x}_j\|^2$$

donde $\mathbf{s}_i, \mathbf{s}_j$ son dos fuentes semánticas y $\mathbf{x}_i = f_\theta(\mathbf{s}_i)$, $\mathbf{x}_j = f_\theta(\mathbf{s}_j)$ son sus representaciones en el espacio de señal. Esta propiedad, que emerge naturalmente del entrenamiento conjunto, no existe en los sistemas convencionales donde la modulación es independiente del contenido.

**Figura 9.1:** *Comparación entre una constelación QAM tradicional y una constelación semántica aprendida. Panel izquierdo: constelación 16-QAM convencional con 16 puntos distribuidos en una cuadrícula regular $4 \times 4$ en el plano complejo $(\text{Re}(x), \text{Im}(x))$, donde cada punto representa una secuencia fija de 4 bits y todos los puntos tienen igual importancia. Panel derecho: constelación semántica aprendida por un autoencoder entrenado extremo a extremo para transmisión de imágenes sobre un canal con desvanecimiento Rayleigh. Los puntos se distribuyen de manera no uniforme, con agrupaciones (*clusters*) que corresponden a categorías semánticas distintas (por ejemplo, diferentes objetos en las imágenes). Se observan regiones de alta densidad para categorías semánticas frecuentes y mayor separación entre clusters que representan significados semánticamente distantes. Los puntos no siguen un patrón geométrico regular, sino que adoptan una distribución optimizada conjuntamente para la compresión semántica, la protección contra errores y la eficiencia espectral.*

---

## 9.2 Comunicaciones semánticas para MIMO masivo

### 9.2.1 Modelo del sistema MIMO

Los sistemas MIMO (*Multiple-Input Multiple-Output*) constituyen una de las tecnologías más importantes de las comunicaciones inalámbricas modernas, al explotar la dimensión espacial para multiplicar la capacidad del canal sin requerir ancho de banda adicional. En un sistema MIMO con $N_t$ antenas de transmisión y $N_r$ antenas de recepción, la relación entrada-salida se expresa mediante la ecuación matricial fundamental:

$$\mathbf{Y} = \mathbf{H}\mathbf{X} + \mathbf{N}$$

donde $\mathbf{Y} \in \mathbb{C}^{N_r \times T}$ es la matriz de señales recibidas a lo largo de $T$ instantes de tiempo, $\mathbf{H} \in \mathbb{C}^{N_r \times N_t}$ es la matriz de canal que captura las ganancias complejas entre cada par de antenas transmisora-receptora, $\mathbf{X} \in \mathbb{C}^{N_t \times T}$ es la matriz de señales transmitidas, y $\mathbf{N} \in \mathbb{C}^{N_r \times T}$ es la matriz de ruido gaussiano con entradas i.i.d. $\mathcal{CN}(0, \sigma^2)$.

Cada elemento $h_{ij}$ de la matriz $\mathbf{H}$ representa el coeficiente de canal complejo desde la $j$-ésima antena transmisora hasta la $i$-ésima antena receptora. En un entorno de dispersión rica (*rich scattering*), estos coeficientes se modelan como variables aleatorias complejas gaussianas independientes, dando lugar al modelo de canal de Rayleigh:

$$h_{ij} \sim \mathcal{CN}(0, 1)$$

La capacidad ergódica del canal MIMO, bajo el supuesto de conocimiento perfecto del canal en el receptor (CSIR) y distribución uniforme de potencia entre antenas, está dada por la célebre expresión:

$$C = \mathbb{E}_{\mathbf{H}}\left[\log_2\det\left(\mathbf{I}_{N_r} + \frac{P}{N_t\sigma^2}\mathbf{H}\mathbf{H}^H\right)\right]$$

donde $P$ es la potencia total de transmisión, $\mathbf{I}_{N_r}$ es la matriz identidad de dimensión $N_r$, y $(\cdot)^H$ denota la transpuesta conjugada (hermitiana). Esta expresión revela una propiedad fundamental: en el régimen de alta SNR, la capacidad crece linealmente con $\min(N_t, N_r)$, es decir:

$$C \approx \min(N_t, N_r) \cdot \log_2\left(\frac{P}{N_t \sigma^2}\right) \quad \text{(alta SNR)}$$

Cuando el transmisor también conoce el canal (CSIT), se puede aplicar la descomposición en valores singulares (SVD) $\mathbf{H} = \mathbf{U}\mathbf{\Sigma}\mathbf{V}^H$ para diagonalizar el canal en $r = \text{rank}(\mathbf{H})$ canales paralelos independientes con ganancias $\sigma_1 \geq \sigma_2 \geq \cdots \geq \sigma_r > 0$, y la capacidad se maximiza mediante asignación de potencia *water-filling*:

$$C_{\text{CSIT}} = \sum_{i=1}^{r} \log_2\left(1 + \frac{p_i \sigma_i^2}{\sigma_n^2}\right)$$

donde $p_i = \left(\mu - \sigma_n^2/\sigma_i^2\right)^+$ y $\mu$ se elige para satisfacer la restricción de potencia total $\sum_i p_i = P$.

### 9.2.2 Precodificación en sistemas semánticos

En los sistemas MIMO convencionales, la precodificación es una operación lineal que se aplica a los símbolos modulados antes de la transmisión para dirigir la energía hacia las direcciones espaciales deseadas. La señal transmitida precodificada es:

$$\mathbf{X} = \mathbf{W}\mathbf{S}$$

donde $\mathbf{W} \in \mathbb{C}^{N_t \times d}$ es la matriz de precodificación y $\mathbf{S} \in \mathbb{C}^{d \times T}$ contiene los $d$ flujos de datos independientes. Esquemas clásicos de precodificación incluyen *zero-forcing* ($\mathbf{W} = \mathbf{H}^H(\mathbf{H}\mathbf{H}^H)^{-1}$) y MMSE.

En el contexto de las comunicaciones semánticas, la precodificación se integra directamente dentro del codificador neuronal, eliminando la separación tradicional entre codificación y precodificación. El codificador semántico MIMO puede modelarse como:

$$\mathbf{X} = f_\theta(\mathbf{s}, \mathbf{H}) \in \mathbb{C}^{N_t \times T}$$

donde ahora el codificador $f_\theta$ recibe no solo la fuente semántica $\mathbf{s}$ sino también el estado del canal $\mathbf{H}$ (o una estimación de este), y produce directamente la señal a transmitir por todas las $N_t$ antenas. Esta formulación permite que la red neuronal aprenda simultáneamente:

1. **Extracción de características semánticas**: identificar qué información es relevante del mensaje fuente.
2. **Compresión adaptativa**: ajustar la tasa de compresión según las condiciones del canal MIMO.
3. **Asignación de potencia espacial**: distribuir la potencia entre las antenas de manera óptima, aprendiendo implícitamente una versión no lineal del *water-filling*.
4. **Conformación de haz semántica**: dirigir las características semánticas más importantes a través de los modos espaciales con mejor ganancia, y las menos importantes por modos con menor ganancia, logrando una degradación graceful en la reconstrucción.

La función de pérdida para el entrenamiento del sistema semántico MIMO incorpora tanto la fidelidad semántica como las restricciones de potencia:

$$\mathcal{L} = \mathbb{E}_{\mathbf{s}, \mathbf{H}}\left[d_{\text{sem}}\left(\mathbf{s}, g_\phi\left(\mathbf{H}f_\theta(\mathbf{s}, \mathbf{H}) + \mathbf{N}\right)\right)\right] + \lambda \cdot \left(\frac{1}{T}\mathbb{E}\left[\text{tr}(\mathbf{X}\mathbf{X}^H)\right] - P\right)^2$$

donde $g_\phi(\cdot)$ es el decodificador semántico en el receptor, $d_{\text{sem}}$ es una distancia semántica apropiada y $\text{tr}(\cdot)$ denota la traza matricial.

### 9.2.3 Conformación de haz (*beamforming*) integrada con codificación semántica

La conformación de haz o *beamforming* permite dirigir la energía transmitida hacia direcciones específicas en el espacio, lo que es especialmente importante en MIMO masivo donde $N_t \gg 1$. En sistemas convencionales, el vector de *beamforming* analógico para dirigir el haz hacia un ángulo $\theta$ es:

$$\mathbf{a}(\theta) = \frac{1}{\sqrt{N_t}}\left[1, e^{j\frac{2\pi d}{\lambda}\sin\theta}, e^{j\frac{2\pi \cdot 2d}{\lambda}\sin\theta}, \ldots, e^{j\frac{2\pi(N_t-1)d}{\lambda}\sin\theta}\right]^T$$

donde $d$ es el espaciado entre antenas y $\lambda$ es la longitud de onda.

En un sistema semántico con *beamforming*, la arquitectura puede diseñarse como:

$$\mathbf{x}[t] = \sum_{m=1}^{M} \mathbf{w}_m \cdot s_m[t] = \mathbf{W}\mathbf{s}[t]$$

donde $\mathbf{s}[t] = [s_1[t], \ldots, s_M[t]]^T$ son los $M$ flujos de símbolos semánticos y $\mathbf{W} = [\mathbf{w}_1, \ldots, \mathbf{w}_M]$ es la matriz de *beamforming*. La clave de la innovación semántica es que tanto $\mathbf{s}[t]$ como $\mathbf{W}$ son generados conjuntamente por la red neuronal, permitiendo que la conformación de haz se adapte al contenido semántico del mensaje.

Por ejemplo, en un sistema de transmisión de video, el codificador semántico MIMO podría asignar los flujos que contienen información del fondo de la escena (menos relevante semánticamente) a haces con menor ganancia, mientras que los flujos que contienen información de objetos en primer plano o movimiento se asignan a haces con mayor ganancia y menor probabilidad de error. Esta priorización semántica del *beamforming* no tiene análogo en los sistemas convencionales, donde la modulación es independiente del contenido.

### 9.2.4 Convergencia de características semánticas entre antenas

Un fenómeno particularmente interesante en los sistemas semánticos MIMO es la convergencia de las representaciones semánticas a través de las múltiples antenas. Cuando el codificador semántico produce $N_t$ flujos de señal (uno por antena), surge la pregunta de cómo se distribuye la información semántica entre estos flujos.

Los estudios empíricos han mostrado que durante el entrenamiento, las redes neuronales semánticas MIMO aprenden a realizar una especie de "factorización semántica" donde diferentes aspectos del mensaje se separan naturalmente en diferentes flujos espaciales. Esto puede analizarse mediante la información mutua entre cada flujo transmitido y la fuente:

$$I(\mathbf{s}; x_i) \quad \text{para cada antena } i = 1, \ldots, N_t$$

En un codificador semántico MIMO bien entrenado, se observa que $I(\mathbf{s}; x_1) > I(\mathbf{s}; x_2) > \cdots > I(\mathbf{s}; x_{N_t})$, es decir, existe una jerarquía natural de importancia semántica entre los flujos, análoga a los valores singulares decrecientes de la descomposición SVD del canal. Esta convergencia permite implementar estrategias de transmisión robustas donde los flujos menos importantes pueden sacrificarse si las condiciones del canal se deterioran, sin pérdida significativa de fidelidad semántica.

**Figura 9.2:** *Sistema MIMO semántico con $N_t = 4$ antenas de transmisión y $N_r = 4$ antenas de recepción. En el transmisor, la fuente semántica (una imagen) ingresa al codificador semántico basado en red neuronal profunda, que produce $N_t$ flujos de salida paralelos, cada uno alimentando una antena distinta. Los flujos están etiquetados jerárquicamente: el flujo 1 contiene las características semánticas de más alta prioridad (estructura global de la imagen), el flujo 2 contiene características de nivel medio (texturas y bordes), el flujo 3 contiene detalles finos y el flujo 4 contiene información residual. Las señales se propagan a través del canal MIMO representado por la matriz $\mathbf{H}$, con flechas que indican los $N_t \times N_r = 16$ caminos de propagación. En el receptor, las $N_r$ antenas capturan la señal combinada, que se alimenta al decodificador semántico neuronal para reconstruir la imagen. Se muestra también el módulo de estimación de canal que proporciona $\hat{\mathbf{H}}$ al codificador (vía retroalimentación) y al decodificador.*

---

## 9.3 Comunicaciones semánticas en bandas milimétricas (mmWave) y THz

### 9.3.1 Desafíos en altas frecuencias

Las bandas de frecuencia milimétricas (mmWave, 30–300 GHz) y de terahercios (THz, 0.1–10 THz) ofrecen anchos de banda extraordinarios que pueden soportar tasas de datos de múltiples gigabits por segundo e incluso terabits por segundo. Sin embargo, estas frecuencias presentan desafíos físicos fundamentales que limitan severamente su aprovechamiento en sistemas convencionales.

La pérdida en el espacio libre (*free-space path loss*, FSPL) sigue la ecuación de Friis y aumenta cuadráticamente con la frecuencia:

$$\text{FSPL}(f, d) = \left(\frac{4\pi d f}{c}\right)^2$$

donde $d$ es la distancia, $f$ es la frecuencia portadora y $c$ es la velocidad de la luz. A 300 GHz, la FSPL es 40 dB mayor que a 3 GHz para la misma distancia, lo que significa que la potencia recibida es $10{,}000$ veces menor. Esta atenuación se compensa parcialmente mediante el uso de antenas altamente directivas (arreglos masivos), pero esto introduce el problema de haces extremadamente estrechos que requieren alineamiento preciso.

Adicionalmente, las frecuencias mmWave y THz sufren de:

- **Atenuación atmosférica**: la absorción por moléculas de agua y oxígeno crea ventanas de transmisión y bandas de absorción. A 60 GHz existe una banda de absorción por oxígeno de aproximadamente 15 dB/km, y en THz existen múltiples líneas de absorción por vapor de agua.

- **Bloqueo por obstáculos**: la difracción es mínima a estas frecuencias, por lo que cualquier obstáculo sólido (personas, muebles, paredes) puede causar una atenuación de 20-40 dB o bloqueo total del enlace. El fenómeno de bloqueo puede modelarse como:

$$P_{\text{bloqueo}} = 1 - e^{-\beta d}$$

donde $\beta$ es la densidad de obstáculos bloqueantes por unidad de distancia.

- **Haces estrechos**: el ancho de haz de media potencia para un arreglo lineal uniforme (ULA) es aproximadamente $\theta_{3\text{dB}} \approx \frac{2}{N_t}$ radianes, lo que para $N_t = 256$ antenas resulta en haces de menos de 0.5°. Esto requiere procedimientos de búsqueda de haz (*beam search*) costosos en tiempo y energía.

### 9.3.2 Valor de las comunicaciones semánticas en mmWave/THz

Las comunicaciones semánticas son especialmente valiosas en las bandas mmWave y THz debido a una asimetría fundamental en estas bandas: **el ancho de banda es abundante, pero el enlace es frágil**. Esta combinación crea un escenario donde la compresión semántica y la robustez ante interrupciones se vuelven críticas.

**Compresión semántica para reducir la tasa requerida**: En un enlace THz con 10 GHz de ancho de banda disponible, la capacidad teórica máxima podría ser de 40 Gbps. Sin embargo, debido a las limitaciones de potencia y la alta atenuación, la capacidad práctica podría ser solo de 1 Gbps durante períodos de buen enlace y caer a cero durante bloqueos. Un codificador semántico que comprima una imagen de 10 MB a 100 KB (relación de compresión 100:1) mientras preserva la información semántica relevante permite transmitir la imagen en $100 \times 8 / 10^9 = 0.8$ ms, minimizando la exposición a eventos de bloqueo.

La tasa semántica efectiva puede definirse como:

$$R_{\text{sem}} = \frac{S(\mathbf{s}) - S(\mathbf{s}|\hat{\mathbf{s}})}{n \cdot T_s}$$

donde $S(\mathbf{s})$ es la entropía semántica de la fuente, $S(\mathbf{s}|\hat{\mathbf{s}})$ es la incertidumbre semántica residual después de la reconstrucción, $n$ es el número de símbolos transmitidos y $T_s$ es la duración de cada símbolo.

**Robustez ante conectividad intermitente**: Los sistemas semánticos pueden diseñarse para transmitir primero las características semánticas más importantes y luego refinar progresivamente. Si el enlace se interrumpe después de transmitir solo el 30% de los símbolos, el decodificador semántico puede aún reconstruir una versión útil del mensaje. Esto se logra mediante esquemas de codificación progresiva semántica:

$$\hat{\mathbf{s}}_k = g_\phi\left(\mathbf{y}_1, \mathbf{y}_2, \ldots, \mathbf{y}_k\right), \quad k = 1, 2, \ldots, n$$

donde $\hat{\mathbf{s}}_k$ es la reconstrucción basada en los primeros $k$ símbolos recibidos. La calidad semántica mejora monótonamente con $k$: $d_{\text{sem}}(\mathbf{s}, \hat{\mathbf{s}}_1) \geq d_{\text{sem}}(\mathbf{s}, \hat{\mathbf{s}}_2) \geq \cdots \geq d_{\text{sem}}(\mathbf{s}, \hat{\mathbf{s}}_n)$.

**Reducción de la sobrecarga de búsqueda de haz**: El proceso convencional de búsqueda de haz requiere transmitir pilotos en múltiples direcciones, lo que consume tiempo y energía. Un sistema semántico puede utilizar la información semántica del canal (por ejemplo, la geometría del entorno percibida a través de estimaciones de canal previas) para predecir la dirección óptima del haz, reduciendo significativamente la sobrecarga.

### 9.3.3 Modulación OTFS para canales de alta movilidad

La modulación OTFS (*Orthogonal Time Frequency Space*) es una técnica de multiplexación diseñada para operar eficientemente en canales de alta movilidad, donde el desplazamiento Doppler varía rápidamente y degrada severamente el rendimiento de OFDM. OTFS opera en el dominio retardo-Doppler (*delay-Doppler domain*), donde el canal se representa de manera más compacta y estable.

En el dominio retardo-Doppler, el canal se modela como una función de dispersión:

$$h(\tau, \nu) = \sum_{p=1}^{P} h_p \, \delta(\tau - \tau_p) \, \delta(\nu - \nu_p)$$

donde $P$ es el número de caminos de propagación, $h_p$ es la ganancia compleja, $\tau_p$ es el retardo y $\nu_p$ es el desplazamiento Doppler del $p$-ésimo camino. En el dominio discreto, la relación entrada-salida OTFS se expresa como:

$$\mathbf{Y}[k,l] = \sum_{k'=0}^{N-1}\sum_{l'=0}^{M-1} \mathbf{H}[k-k',l-l']\mathbf{X}[k',l'] + \mathbf{N}[k,l]$$

donde $\mathbf{X}[k',l']$ y $\mathbf{Y}[k,l]$ son los símbolos transmitidos y recibidos en el punto $(k',l')$ y $(k,l)$ de la cuadrícula retardo-Doppler respectivamente, con $k = 0, \ldots, N-1$ indexando la dimensión Doppler y $l = 0, \ldots, M-1$ indexando la dimensión de retardo. La función de transferencia del canal discretizada es:

$$\mathbf{H}[k,l] = \sum_{p=1}^{P} h_p \, e^{-j2\pi \frac{k \nu_p}{N\Delta\nu}} \, \delta[l - l_p]$$

donde $l_p = \tau_p / \Delta\tau$ es el índice de retardo discreto y $\Delta\nu$, $\Delta\tau$ son las resoluciones en Doppler y retardo, respectivamente.

La ventaja fundamental de OTFS sobre OFDM es que en el dominio retardo-Doppler, el canal es **cuasi-estático**: mientras que en OFDM la matriz de canal varía rápidamente en el dominio tiempo-frecuencia (cada subportadora experimenta un desvanecimiento diferente y variante en el tiempo), en OTFS la representación retardo-Doppler del canal cambia lentamente incluso en escenarios de alta movilidad. Esto significa que:

1. Cada símbolo OTFS experimenta efectivamente el **canal completo** (toda la diversidad), lo que elimina el problema de desvanecimiento profundo que afecta a subportadoras individuales en OFDM.
2. La estimación de canal es más eficiente, ya que solo se necesita estimar $P$ coeficientes complejos (uno por camino) en lugar de $N \times M$ coeficientes en el dominio tiempo-frecuencia.
3. La ecualización se simplifica significativamente en el dominio retardo-Doppler.

### 9.3.4 Integración de OTFS con codificación semántica

La sinergia entre OTFS y comunicaciones semánticas es particularmente prometedora. El codificador semántico puede diseñarse para operar directamente en el dominio retardo-Doppler:

$$\mathbf{X}_{\text{DD}} = f_\theta(\mathbf{s}) \in \mathbb{C}^{N \times M}$$

donde $\mathbf{X}_{\text{DD}}$ es la cuadrícula de símbolos semánticos en el dominio retardo-Doppler. La red neuronal aprende a colocar las características semánticas más importantes en las posiciones de la cuadrícula que experimentan mejor calidad de canal, y las menos importantes en posiciones con menor calidad.

La ventaja de esta integración es triple: (1) el codificador semántico puede explotar la cuasi-estacionariedad del canal retardo-Doppler para producir representaciones más eficientes; (2) la diversidad completa del canal beneficia a todas las características semánticas; y (3) la estimación de canal simplificada puede integrarse como una capa de la red neuronal, permitiendo un sistema verdaderamente extremo a extremo que funcione eficientemente incluso en las desafiantes condiciones de las bandas THz con alta movilidad.

---

## 9.4 Sensing semántico: ISAC (Integrated Sensing and Communications)

### 9.4.1 Comunicaciones y sensado integrado

ISAC (*Integrated Sensing and Communications*) es un paradigma emergente que busca la convergencia de las funciones de radar (sensado) y comunicaciones en un único sistema, compartiendo hardware, forma de onda y recursos espectrales. En lugar de diseñar sistemas de radar y comunicaciones de manera independiente y gestionando la interferencia entre ellos, ISAC los unifica para lograr eficiencia espectral, energética y de costos.

En un sistema ISAC, la señal transmitida $\mathbf{x}(t)$ sirve simultáneamente dos propósitos:

1. **Comunicación**: transportar información semántica desde el transmisor al receptor.
2. **Sensado**: iluminar objetivos en el entorno y analizar los ecos reflejados para extraer información sobre posición, velocidad, forma y tipo de los objetos.

La señal recibida en el receptor de comunicación es:

$$\mathbf{y}_{\text{com}}(t) = \mathbf{h}_{\text{com}}(t) * \mathbf{x}(t) + \mathbf{n}_{\text{com}}(t)$$

mientras que la señal de eco recibida por el radar es:

$$\mathbf{y}_{\text{radar}}(t) = \sum_{q=1}^{Q} \alpha_q \, \mathbf{x}(t - \tau_q) \, e^{j2\pi \nu_q t} + \mathbf{n}_{\text{radar}}(t)$$

donde $Q$ es el número de objetivos, $\alpha_q$ es el coeficiente de reflexión del $q$-ésimo objetivo (relacionado con su sección transversal de radar, RCS), $\tau_q = 2d_q/c$ es el retardo de ida y vuelta proporcional a la distancia $d_q$, y $\nu_q = 2v_q f_c/c$ es el desplazamiento Doppler proporcional a la velocidad radial $v_q$.

El desafío fundamental de ISAC es diseñar la señal $\mathbf{x}(t)$ y los algoritmos de procesamiento para optimizar simultáneamente el rendimiento de ambas funciones, que tienen requerimientos potencialmente conflictivos. La comunicación requiere alta entropía en la señal (aleatoriedad para transportar información), mientras que el radar tradicional prefiere señales deterministas con buenas propiedades de autocorrelación.

### 9.4.2 Sensado semántico: extracción de información del canal

En el marco de las comunicaciones semánticas, la función de sensado adquiere una dimensión adicional: el **sensado semántico**. En lugar de simplemente estimar parámetros físicos del canal (retardos, Doppler, ángulos), un sistema de sensado semántico busca extraer información de alto nivel sobre el entorno.

La estimación del canal puede verse como una forma fundamental de sensado. Cuando el sistema estima la matriz de canal $\hat{\mathbf{H}}$, está implícitamente capturando información sobre el entorno de propagación:

$$\hat{\mathbf{H}} = \sum_{p=1}^{P} \hat{h}_p \, \mathbf{a}_r(\hat{\theta}_{r,p}) \, \mathbf{a}_t^H(\hat{\theta}_{t,p}) \, e^{-j2\pi \hat{\tau}_p f}$$

donde $\hat{\theta}_{r,p}$ y $\hat{\theta}_{t,p}$ son los ángulos de llegada y salida estimados del $p$-ésimo camino, $\hat{\tau}_p$ es el retardo estimado, y $\mathbf{a}_r$, $\mathbf{a}_t$ son los vectores de dirección del arreglo de antenas.

El sensado semántico va más allá: utiliza una red neuronal para inferir características de alto nivel del entorno a partir de los parámetros de canal estimados:

$$\mathbf{c}_{\text{env}} = h_\psi(\hat{\mathbf{H}}_1, \hat{\mathbf{H}}_2, \ldots, \hat{\mathbf{H}}_T)$$

donde $h_\psi$ es una red neuronal de sensado semántico que procesa una secuencia temporal de estimaciones de canal $\{\hat{\mathbf{H}}_t\}$ para inferir un vector de características ambientales $\mathbf{c}_{\text{env}}$ que puede incluir:

- Número y tipo de objetos en el entorno (personas, vehículos, obstáculos).
- Actividad de las personas (caminando, sentado, gesticulando) — lo que se conoce como reconocimiento de actividad basado en Wi-Fi.
- Mapa del entorno (localización de paredes, muebles, puertas).
- Condiciones atmosféricas (lluvia, niebla) que afectan la propagación.

### 9.4.3 Sección transversal de radar y extracción de características semánticas

La sección transversal de radar (RCS, *Radar Cross Section*) $\sigma_{\text{RCS}}$ de un objetivo cuantifica cuánta energía de la señal incidente es reflejada hacia el radar. Para un objetivo puntual, la potencia recibida sigue la ecuación del radar:

$$P_r = \frac{P_t G_t G_r \lambda^2 \sigma_{\text{RCS}}}{(4\pi)^3 d^4}$$

donde $P_t$ es la potencia transmitida, $G_t$ y $G_r$ son las ganancias de antena de transmisión y recepción, $\lambda$ es la longitud de onda y $d$ es la distancia al objetivo.

En un sistema ISAC semántico, la RCS no se trata como un simple escalar, sino como una función del ángulo, la frecuencia y la polarización que contiene una "huella" del objetivo:

$$\sigma_{\text{RCS}}(\theta, \phi, f, \hat{p}_r, \hat{p}_t) = \lim_{d\to\infty} 4\pi d^2 \frac{|\mathbf{E}_s(\theta, \phi)|^2}{|\mathbf{E}_i|^2}$$

donde $\mathbf{E}_s$ y $\mathbf{E}_i$ son los campos eléctricos dispersado e incidente. Un codificador semántico de sensado puede extraer características de alto nivel a partir de esta firma:

$$\hat{c}_{\text{objeto}} = f_{\text{sense}}(\sigma_{\text{RCS}}(\theta, \phi, f))$$

clasificando el tipo de objetivo (peatón, automóvil, ciclista), estimando sus dimensiones y prediciendo su trayectoria futura.

### 9.4.4 Función dual: comunicar y sensar simultáneamente

La función dual ISAC en el contexto semántico puede formalizarse como un problema de optimización multiobjetivo:

$$\min_{\theta, \phi, \mathbf{X}} \quad \alpha \cdot \mathcal{L}_{\text{com}}(\theta, \phi, \mathbf{X}) + (1-\alpha) \cdot \mathcal{L}_{\text{sense}}(\mathbf{X})$$

sujeto a:

$$\frac{1}{T}\text{tr}(\mathbf{X}\mathbf{X}^H) \leq P, \quad S_x(f) \leq S_{\text{máscara}}(f)$$

donde $\mathcal{L}_{\text{com}}$ es la pérdida de comunicación semántica (por ejemplo, la distorsión en la reconstrucción), $\mathcal{L}_{\text{sense}}$ es la pérdida de sensado (por ejemplo, el error en la detección o clasificación de objetos), y $\alpha \in [0,1]$ es un parámetro de compromiso (*trade-off*) que balancea ambos objetivos.

La red neuronal conjunta puede diseñarse con una estructura de codificador compartido y dos decodificadores especializados:

$$\mathbf{z} = f_{\text{encoder}}(\mathbf{s})$$
$$\mathbf{X} = f_{\text{waveform}}(\mathbf{z})$$
$$\hat{\mathbf{s}} = g_{\text{com}}(\mathbf{y}_{\text{com}})$$
$$\hat{\mathbf{c}} = g_{\text{sense}}(\mathbf{y}_{\text{radar}})$$

donde $\mathbf{z}$ es una representación latente compartida, $f_{\text{waveform}}$ genera la forma de onda que sirve tanto para comunicación como para sensado, y $g_{\text{com}}$, $g_{\text{sense}}$ son los decodificadores de comunicación y sensado, respectivamente.

**Figura 9.3:** *Sistema ISAC (*Integrated Sensing and Communications*) semántico. El transmisor contiene un codificador semántico que genera una forma de onda $\mathbf{x}(t)$ de función dual. Esta forma de onda se irradia a través de un arreglo de antenas MIMO. Parte de la energía llega al receptor de comunicación (usuario) a través del canal directo, donde el decodificador semántico reconstruye el mensaje original $\hat{\mathbf{s}}$. Simultáneamente, la misma señal ilumina objetos en el entorno (un vehículo, un peatón), y los ecos reflejados son captados por las antenas del transmisor (en configuración mono-estática) o por antenas separadas (configuración bi-estática). El procesador de sensado semántico analiza los ecos para extraer información de alto nivel: tipo de objeto, posición $(x, y)$, velocidad $v$ y dirección de movimiento. Se muestra la coexistencia del flujo de datos semántico (línea sólida, del Tx al Rx de comunicación) y el flujo de sensado (línea discontinua, del Tx al objetivo y de vuelta), ambos utilizando la misma señal transmitida y los mismos recursos espectrales.*

---

## 9.5 Modelos fundacionales multimodales para comunicaciones semánticas

### 9.5.1 Modelos preentrenados como columna vertebral semántica

Los modelos fundacionales (*foundation models*) representan un cambio de paradigma en la inteligencia artificial. Estos modelos masivos, preentrenados con enormes volúmenes de datos heterogéneos, aprenden representaciones generales del mundo que pueden transferirse a una amplia variedad de tareas. Los ejemplos más destacados incluyen los modelos de lenguaje grande (LLMs, *Large Language Models*) como GPT y los transformadores de visión (ViTs, *Vision Transformers*).

La integración de modelos fundacionales en comunicaciones semánticas ofrece ventajas fundamentales:

1. **Representaciones semánticas ricas**: Los modelos fundacionales aprenden representaciones que capturan relaciones semánticas profundas entre conceptos. Un ViT preentrenado en millones de imágenes ha aprendido a distinguir entre objetos, escenas, acciones y atributos a múltiples niveles de abstracción. Un LLM ha aprendido la estructura del lenguaje, el conocimiento del mundo y las relaciones lógicas. Estas representaciones son intrínsecamente semánticas.

2. **Generalización**: A diferencia de los codificadores semánticos entrenados desde cero para una tarea específica, los modelos fundacionales generalizan a distribuciones de datos nunca vistas durante el entrenamiento. Esto es crucial en comunicaciones, donde la distribución de los datos fuente puede variar significativamente entre usuarios y contextos.

3. **Eficiencia de datos**: El entrenamiento de un codificador semántico desde cero requiere grandes conjuntos de datos pareados (fuente-canal-reconstrucción). Con un modelo fundacional como inicialización, se requieren significativamente menos datos de entrenamiento específico de comunicación.

La arquitectura de un sistema semántico basado en modelos fundacionales puede formularse como:

$$\mathbf{z} = f_{\text{proj}}\left(f_{\text{fund}}(\mathbf{s})\right)$$
$$\mathbf{x} = f_{\text{canal}}(\mathbf{z})$$

donde $f_{\text{fund}}(\cdot)$ es el modelo fundacional preentrenado (cuyos pesos pueden congelarse o ajustarse finamente), $f_{\text{proj}}(\cdot)$ es una capa de proyección que adapta la representación del modelo fundacional al espacio de transmisión, y $f_{\text{canal}}(\cdot)$ es el codificador de canal neuronal. La representación $\mathbf{z}$ reside en un espacio semántico de dimensión típicamente mucho menor que la dimensión de la fuente original.

### 9.5.2 Aprendizaje por transferencia para tareas de comunicación

El aprendizaje por transferencia (*transfer learning*) permite adaptar los modelos fundacionales a la tarea específica de comunicación semántica. El procedimiento típico involucra las siguientes etapas:

**Etapa 1: Preentrenamiento** (ya completada por los desarrolladores del modelo fundacional). El modelo $f_{\text{fund}}$ se entrena con un objetivo genérico (por ejemplo, predicción de palabras enmascaradas para LLMs, o clasificación de imágenes para ViTs) usando un conjunto de datos masivo $\mathcal{D}_{\text{pre}}$:

$$\theta_{\text{fund}}^* = \arg\min_\theta \sum_{(\mathbf{x},y) \in \mathcal{D}_{\text{pre}}} \mathcal{L}_{\text{pre}}(f_\theta(\mathbf{x}), y)$$

**Etapa 2: Ajuste fino (*fine-tuning*) para comunicación**. Se congela la mayor parte de los pesos del modelo fundacional y se entrenan las capas adicionales (proyección y codificador de canal) junto con un ajuste fino de las últimas capas del modelo fundacional:

$$(\theta_{\text{proj}}^*, \theta_{\text{canal}}^*, \theta_{\text{dec}}^*) = \arg\min \mathbb{E}_{\mathbf{s}, \mathbf{H}} \left[\mathcal{L}_{\text{sem}}\left(\mathbf{s}, g_{\theta_{\text{dec}}}\left(\mathbf{H} \cdot f_{\theta_{\text{canal}}}(f_{\theta_{\text{proj}}}(f_{\text{fund}}(\mathbf{s}))) + \mathbf{n}\right)\right)\right]$$

**Etapa 3: Adaptación continua**. El modelo se sigue adaptando durante la operación en función de las condiciones del canal y la distribución de los datos de los usuarios.

Una técnica particularmente eficiente para el ajuste fino es LoRA (*Low-Rank Adaptation*), donde en lugar de modificar todos los pesos del modelo fundacional, se añaden matrices de bajo rango que capturan las adaptaciones necesarias:

$$\mathbf{W}_{\text{adaptado}} = \mathbf{W}_{\text{fund}} + \mathbf{B}\mathbf{A}$$

donde $\mathbf{W}_{\text{fund}} \in \mathbb{R}^{d \times d}$ es la matriz de pesos original (congelada), $\mathbf{B} \in \mathbb{R}^{d \times r}$ y $\mathbf{A} \in \mathbb{R}^{r \times d}$ son matrices entrenables de bajo rango $r \ll d$. Esto reduce drásticamente el número de parámetros a entrenar de $d^2$ a $2dr$, lo que es crucial para el despliegue en dispositivos con recursos limitados.

### 9.5.3 Comunicación semántica multimodal

Los sistemas de comunicación del futuro no transportarán un solo tipo de datos, sino flujos multimodales integrados: texto, imágenes, audio, video, datos de sensores y señales de control, todos ellos portadores de significado semántico interrelacionado. La comunicación semántica multimodal busca explotar estas relaciones para lograr una compresión y protección más eficientes.

El modelo de un sistema semántico multimodal puede formalizarse como:

$$\mathbf{z}_{\text{fusión}} = f_{\text{fusión}}\left(f_{\text{texto}}(\mathbf{s}_{\text{texto}}), f_{\text{imagen}}(\mathbf{s}_{\text{imagen}}), f_{\text{audio}}(\mathbf{s}_{\text{audio}})\right)$$

donde $f_{\text{texto}}$, $f_{\text{imagen}}$, $f_{\text{audio}}$ son codificadores semánticos específicos de cada modalidad (potencialmente basados en modelos fundacionales), y $f_{\text{fusión}}$ es un módulo de fusión que combina las representaciones de las diferentes modalidades en un espacio semántico unificado.

La fusión puede realizarse mediante mecanismos de atención cruzada (*cross-attention*):

$$\text{CrossAttn}(\mathbf{Q}_i, \mathbf{K}_j, \mathbf{V}_j) = \text{softmax}\left(\frac{\mathbf{Q}_i \mathbf{K}_j^T}{\sqrt{d_k}}\right)\mathbf{V}_j$$

donde $\mathbf{Q}_i$ proviene de la modalidad $i$ y $\mathbf{K}_j$, $\mathbf{V}_j$ provienen de la modalidad $j$, permitiendo que cada modalidad atienda a la información relevante de las demás.

La ventaja clave de la comunicación multimodal semántica es la **redundancia intermodal**: la información contenida en una modalidad puede ayudar a reconstruir o completar la información de otra. Por ejemplo, en una videollamada, si se pierden fotogramas de video, el audio puede ayudar a inferir las expresiones faciales del hablante; si se corrompe el audio, el movimiento de los labios en el video puede ayudar a reconstruir el habla. Esta redundancia se explota naturalmente por los modelos fundacionales multimodales, que aprenden alineaciones semánticas entre modalidades.

### 9.5.4 La base de conocimiento (KB) compartida

Un concepto fundamental en las comunicaciones semánticas es la **base de conocimiento** (*Knowledge Base*, KB) compartida entre el transmisor y el receptor (Shi et al., 2021, DOI: 10.1109/JSAC.2021.3126078). Esta KB representa el conocimiento común que ambos extremos poseen y que permite la interpretación correcta del mensaje semántico.

En el contexto de modelos fundacionales, la KB puede identificarse con los pesos del modelo preentrenado compartido:

$$\text{KB} = \{\theta_{\text{fund}}\}$$

Cuando tanto el transmisor como el receptor utilizan el mismo modelo fundacional (o versiones compatibles), comparten implícitamente una vasta base de conocimiento que incluye:

- Conocimiento lingüístico: gramática, semántica léxica, relaciones entre conceptos.
- Conocimiento visual: tipos de objetos, escenas, relaciones espaciales.
- Conocimiento del mundo: hechos, relaciones causales, expectativas contextuales.

La eficiencia de la comunicación semántica depende directamente de la riqueza y alineación de las KBs:

$$R_{\text{sem}} \propto \frac{1}{H(\mathbf{s} | \text{KB})}$$

donde $H(\mathbf{s} | \text{KB})$ es la entropía condicional de la fuente dado el conocimiento compartido. Cuanto mayor sea el conocimiento compartido, menor será la información que necesita transmitirse explícitamente, y mayor será la eficiencia semántica.

### 9.5.5 Comunicación semántica basada en ontologías

Las ontologías proporcionan una estructura formal para representar el conocimiento y las relaciones entre conceptos. En comunicaciones semánticas, una ontología compartida entre Tx y Rx define un vocabulario común de conceptos, propiedades y relaciones que permite una comunicación extremadamente eficiente.

Una ontología puede representarse como un grafo dirigido:

$$\mathcal{O} = (\mathcal{C}, \mathcal{R}, \mathcal{A})$$

donde $\mathcal{C}$ es un conjunto de conceptos (nodos), $\mathcal{R}$ es un conjunto de relaciones (aristas) entre conceptos, y $\mathcal{A}$ es un conjunto de axiomas que definen restricciones y reglas de inferencia. En este marco, un mensaje semántico se codifica como un subgrafo de la ontología:

$$\mathbf{m} = (\mathcal{C}_m \subseteq \mathcal{C}, \mathcal{R}_m \subseteq \mathcal{R})$$

La eficiencia de esta representación radica en que transmitir las identidades de los conceptos y relaciones activados (que pueden codificarse como índices enteros) es vastamente más eficiente que transmitir los datos crudos. Por ejemplo, transmitir la tripleta ontológica *(perro, persigue, gato)* requiere solo tres índices, mientras que una imagen o video que muestre esta escena requeriría millones de bits. Naturalmente, esto presupone que ambos extremos comparten la ontología y la capacidad de generar o interpretar representaciones a partir de las tripletas ontológicas.

---

## 9.6 Aprendizaje federado para comunicaciones semánticas

### 9.6.1 Entrenamiento distribuido con preservación de privacidad

El entrenamiento de codificadores y decodificadores semánticos requiere grandes volúmenes de datos que frecuentemente residen en dispositivos de los usuarios (teléfonos móviles, cámaras, sensores IoT). Centralizar estos datos en un servidor para el entrenamiento plantea serios problemas de privacidad, ancho de banda y latencia. El aprendizaje federado (*Federated Learning*, FL) ofrece una solución elegante al permitir el entrenamiento colaborativo de modelos sin compartir datos crudos.

En el paradigma de FL, cada dispositivo $k$ posee un conjunto de datos local $\mathcal{D}_k = \{(\mathbf{s}_i^{(k)}, \tilde{\mathbf{s}}_i^{(k)})\}_{i=1}^{n_k}$ donde $\mathbf{s}_i^{(k)}$ es una muestra de la fuente semántica y $\tilde{\mathbf{s}}_i^{(k)}$ es la reconstrucción objetivo (o la fuente misma en esquemas autoencoder). El objetivo global del entrenamiento es minimizar la pérdida agregada:

$$\min_\theta \mathcal{L}(\theta) = \sum_{k=1}^{K} \frac{n_k}{n} \mathcal{L}_k(\theta)$$

donde $K$ es el número de dispositivos participantes, $n_k = |\mathcal{D}_k|$ es el tamaño del conjunto de datos local, $n = \sum_{k=1}^K n_k$ es el tamaño total, y $\mathcal{L}_k(\theta)$ es la pérdida local del dispositivo $k$:

$$\mathcal{L}_k(\theta) = \frac{1}{n_k} \sum_{i=1}^{n_k} \ell\left(\mathbf{s}_i^{(k)}, g_\phi\left(h_{\text{canal}}\left(f_\theta\left(\mathbf{s}_i^{(k)}\right)\right)\right)\right)$$

donde $\ell$ es la función de pérdida por muestra (distorsión semántica), $f_\theta$ es el codificador semántico, $h_{\text{canal}}$ simula el efecto del canal (durante el entrenamiento), y $g_\phi$ es el decodificador semántico.

### 9.6.2 Formulación del aprendizaje federado

El algoritmo FedAvg (*Federated Averaging*), la variante más utilizada de FL, procede en rondas de comunicación. En cada ronda $t$:

**Paso 1: Distribución del modelo global.** El servidor envía el modelo global actual $\theta^t$ a un subconjunto $\mathcal{S}_t \subseteq \{1, \ldots, K\}$ de dispositivos seleccionados.

**Paso 2: Entrenamiento local.** Cada dispositivo $k \in \mathcal{S}_t$ realiza $E$ épocas de SGD local:

$$\theta_k^{t,e+1} = \theta_k^{t,e} - \eta_{\text{local}} \nabla \mathcal{L}_k(\theta_k^{t,e}), \quad e = 0, 1, \ldots, E-1$$

con $\theta_k^{t,0} = \theta^t$. La actualización local se define como $\Delta\theta_k^t = \theta_k^{t,E} - \theta^t$.

**Paso 3: Agregación.** El servidor recibe las actualizaciones locales y calcula el modelo global actualizado mediante promedio ponderado:

$$\theta^{t+1} = \theta^t + \sum_{k \in \mathcal{S}_t} \frac{n_k}{\sum_{j \in \mathcal{S}_t} n_j} \Delta\theta_k^t$$

que es equivalente a la actualización:

$$\theta^{t+1} = \theta^t - \eta \sum_{k=1}^{K} \frac{n_k}{n} \nabla \mathcal{L}_k(\theta^t)$$

en el caso idealizado de $E = 1$ paso local y selección de todos los dispositivos, donde $\eta$ es la tasa de aprendizaje global. Esta es la formulación clásica del aprendizaje federado.

### 9.6.3 Codificación semántica local y agregación en el servidor

En el contexto específico de las comunicaciones semánticas, la aplicación de FL presenta características particulares. Cada dispositivo entrena localmente tanto su codificador semántico como su decodificador. Sin embargo, surge una asimetría natural:

- **El codificador** se ejecuta en el dispositivo del usuario (transmisor) y debe adaptarse a la distribución local de datos de ese usuario.
- **El decodificador** puede ejecutarse en una estación base o servidor (receptor) y debe ser universal, capaz de decodificar mensajes de cualquier usuario.

Esta asimetría sugiere una estrategia de FL diferenciada:

$$\theta_{\text{enc}}^{t+1} = \text{FedAvg}\left(\{\theta_{\text{enc},k}^t\}_{k \in \mathcal{S}_t}\right) + \alpha_k \cdot \Delta\theta_{\text{personal},k}$$

$$\theta_{\text{dec}}^{t+1} = \text{FedAvg}\left(\{\theta_{\text{dec},k}^t\}_{k \in \mathcal{S}_t}\right)$$

donde el codificador incluye un componente de personalización $\Delta\theta_{\text{personal},k}$ que permite adaptar la codificación a las particularidades de cada usuario (tipo de datos, distribución estadística, preferencias), mientras que el decodificador se mantiene completamente compartido para garantizar la interoperabilidad.

### 9.6.4 Modelos semánticos adaptativos que aprenden de condiciones de red

Una ventaja clave del FL para comunicaciones semánticas es la capacidad de entrenar modelos que se adaptan continuamente a las condiciones cambiantes de la red. Cada dispositivo experimenta condiciones de canal únicas (SNR, modelo de desvanecimiento, interferencia) que varían con el tiempo y la ubicación.

Un modelo semántico adaptativo puede parametrizarse condicionalmente:

$$\mathbf{x} = f_\theta(\mathbf{s} ; \mathbf{c}_{\text{canal}})$$

donde $\mathbf{c}_{\text{canal}}$ es un vector de contexto del canal que incluye la SNR estimada, el perfil de retardo de potencia, el esparcimiento Doppler, etc. El FL permite que los modelos aprendan de la diversidad de condiciones de canal experimentadas por todos los dispositivos del sistema, produciendo codificadores más robustos que los entrenados solo con datos de un único dispositivo o con modelos de canal sintéticos.

La diversidad de las condiciones de canal entre los dispositivos participantes actúa como una forma de regularización natural que previene el sobreajuste a un modelo de canal particular. Formalmente, si $p_k(\mathbf{H})$ es la distribución del canal experimentada por el dispositivo $k$, el modelo federado se entrena implícitamente bajo la distribución mezcla:

$$p(\mathbf{H}) = \sum_{k=1}^{K} \frac{n_k}{n} p_k(\mathbf{H})$$

que es más rica y diversa que cualquier distribución individual.

### 9.6.5 Detección de deriva semántica y actualización de modelos

Un problema crítico en sistemas semánticos desplegados es la **deriva semántica** (*semantic drift*): la degradación gradual del rendimiento del sistema cuando las distribuciones de los datos o las condiciones del canal cambian con respecto a las condiciones de entrenamiento. El FL proporciona un mecanismo natural para detectar y corregir la deriva semántica.

La detección de deriva puede realizarse monitoreando la pérdida local de cada dispositivo:

$$\delta_k^t = \mathcal{L}_k(\theta^t) - \mathcal{L}_k(\theta^{t-\Delta t})$$

Si $\delta_k^t > \epsilon_{\text{drift}}$ para una fracción significativa de dispositivos, se activa un ciclo de reentrenamiento federado. Adicionalmente, la divergencia entre los gradientes locales puede indicar que los dispositivos están experimentando distribuciones de datos incompatibles:

$$D_{\text{grad}}^t = \frac{1}{K(K-1)} \sum_{i \neq j} \left\|  \nabla \mathcal{L}_i(\theta^t) - \nabla \mathcal{L}_j(\theta^t) \right\|^2$$

Un valor alto de $D_{\text{grad}}^t$ sugiere heterogeneidad en los datos o condiciones de canal, lo que puede requerir estrategias de personalización más agresivas o incluso la segmentación de los dispositivos en clusters con condiciones similares.

---

## 9.7 El plano de control semántico

### 9.7.1 La cabecera semántica

En las comunicaciones convencionales, cada paquete de datos incluye cabeceras de protocolo que describen el tipo de datos, la dirección de destino, la secuencia, los mecanismos de control de errores, etc. En las comunicaciones semánticas, surge la necesidad de una **cabecera semántica** (*Semantic Header*) que describa las propiedades del contenido semántico y los metadatos necesarios para su correcta decodificación e interpretación.

La cabecera semántica puede incluir los siguientes campos:

1. **Tipo de fuente semántica**: texto, imagen, audio, video, datos de sensores, multimodal.
2. **Nivel de abstracción semántica**: indica la granularidad de la representación (píxeles, objetos, escena, concepto abstracto).
3. **Identificador del modelo codificador/decodificador**: referencia al modelo neuronal utilizado para la codificación, necesario para que el receptor seleccione el decodificador compatible.
4. **Versión de la base de conocimiento**: identifica la versión de la KB utilizada, crucial para detectar desincronización.
5. **Importancia semántica**: prioridad del paquete basada en su relevancia semántica para la tarea del receptor.
6. **Mapa de confianza**: indica la fiabilidad estimada de cada componente semántico.
7. **Dependencias semánticas**: identifica relaciones con otros paquetes semánticos (por ejemplo, un paquete de refinamiento que depende de un paquete base).

Formalmente, la cabecera semántica $\mathbf{h}_{\text{sem}}$ puede representarse como:

$$\mathbf{h}_{\text{sem}} = (\text{tipo}, \text{nivel}, \text{id\_modelo}, \text{ver\_KB}, \text{prioridad}, \mathbf{conf}, \text{deps})$$

Un desafío de diseño importante es el equilibrio entre la riqueza de la cabecera (que permite una decodificación e interpretación más precisa) y su sobrecarga (que reduce la eficiencia espectral). En sistemas semánticos altamente comprimidos, una cabecera excesivamente grande puede dominar el tamaño del paquete.

### 9.7.2 Modificaciones al modelo OSI para comunicaciones semánticas

El modelo de referencia OSI (*Open Systems Interconnection*) de siete capas ha sido el marco conceptual dominante para las arquitecturas de redes de comunicación durante décadas. Sin embargo, este modelo fue diseñado para la transmisión fiable de bits, sin consideración alguna del significado de la información transportada. Las comunicaciones semánticas requieren una reestructuración fundamental del modelo OSI.

Las modificaciones principales incluyen:

**Capa semántica**: Una nueva capa se inserta entre la capa de aplicación (Capa 7) y la capa de presentación (Capa 6). Esta capa es responsable de:
- Extracción de significado de los datos de la aplicación.
- Compresión semántica.
- Priorización basada en relevancia semántica.
- Gestión de la base de conocimiento compartida.

**Fusión de capas inferiores**: En los sistemas semánticos extremo a extremo, las capas de presentación, sesión, transporte y red pueden fusionarse parcialmente, ya que la codificación conjunta fuente-canal elimina la separación entre la representación de datos y la protección contra errores.

**Capa de codificación conjunta fuente-canal semántica (JSCC semántico)**: Reemplaza las funciones separadas de las capas 2 (enlace de datos), 3 (red) y 4 (transporte) para la codificación y protección de datos, integrándolas en un único bloque neuronal.

### 9.7.3 Pila de protocolos semántica

La pila de protocolos semántica propuesta redefine las interacciones entre capas:

**Nivel 1 — Capa física semántica**: Genera directamente la forma de onda a transmitir a partir de las características semánticas. Integra modulación, codificación de canal y conformación de onda en una operación neuronal unificada.

**Nivel 2 — Capa de enlace semántico**: Gestiona la transmisión de unidades de datos semánticos (SDUs, *Semantic Data Units*) entre nodos adyacentes. Implementa control de acceso al medio (MAC) basado en prioridad semántica y mecanismos de retransmisión selectiva semántica (solo se retransmiten las componentes con mayor pérdida semántica).

**Nivel 3 — Capa de red semántica**: Enruta los paquetes semánticos basándose no solo en la dirección de destino sino también en el contenido semántico. Permite el procesamiento semántico en nodos intermedios (*semantic relay*) donde la información puede ser recodificada, resumida o filtrada semánticamente.

**Nivel 4 — Capa de control semántico**: Gestiona la sincronización de bases de conocimiento, la negociación de modelos codificador/decodificador, la detección de deriva semántica y la calidad de experiencia semántica.

**Nivel 5 — Capa de aplicación semántica**: Interfaz con las aplicaciones del usuario, proporcionando APIs para la transmisión y recepción de datos semánticos con diferentes niveles de abstracción y fidelidad.

### 9.7.4 Calidad de experiencia (QoE) vs. calidad de servicio (QoS)

En las comunicaciones convencionales, la calidad del servicio se mide mediante métricas técnicas como el *throughput*, la latencia, la tasa de error de bit (BER) y el *jitter*. Estas métricas son objetivas y medibles en la capa física y de enlace, pero no capturan necesariamente la calidad percibida por el usuario.

Las comunicaciones semánticas naturalmente se alinean con métricas de Calidad de Experiencia (QoE), que miden la satisfacción del usuario con el servicio recibido. La relación entre QoS y QoE no es lineal; por ejemplo, una mejora del 50% en BER podría traducirse en una mejora imperceptible en la calidad de video percibida, o podría ser la diferencia entre un video utilizable e inutilizable.

Las métricas semánticas de QoE incluyen:

- **Fidelidad semántica**: ¿Se preservó el significado del mensaje? Medida mediante distancias en el espacio semántico:

$$\text{SF} = 1 - \frac{d_{\text{sem}}(\mathbf{s}, \hat{\mathbf{s}})}{d_{\text{sem}}^{\max}}$$

- **Relevancia de la tarea**: ¿Fue útil la información recibida para la tarea del receptor? Medida mediante la precisión en tareas posteriores (*downstream task accuracy*).

- **Oportunidad semántica** (*semantic timeliness*): ¿Llegó la información a tiempo para ser relevante? Generalización del concepto de *Age of Information* (AoI) al dominio semántico:

$$\text{AoSI}(t) = t - U_{\text{sem}}(t)$$

donde $U_{\text{sem}}(t)$ es el tiempo de generación de la actualización semántica más reciente cuyo contenido sigue siendo relevante en el tiempo $t$.

### 9.7.5 Deriva semántica: detección y resincronización

La deriva semántica ocurre cuando los modelos del transmisor y receptor divergen, lo que puede suceder por varias razones:

1. **Actualización asimétrica de modelos**: si uno de los extremos actualiza su modelo neuronal sin sincronizar con el otro.
2. **Cambio en la distribución de datos**: si el tipo de contenido transmitido cambia significativamente respecto al entrenamiento.
3. **Degradación del canal**: si las condiciones del canal cambian de manera que el modelo codificador/decodificador ya no es apropiado.

La detección de deriva semántica puede realizarse monitoreando la similitud semántica entre muestras de referencia. Sea $\mathcal{R} = \{\mathbf{s}_1, \ldots, \mathbf{s}_R\}$ un conjunto de mensajes de referencia conocidos por ambos extremos. Periódicamente, se calcula la fidelidad de reconstrucción:

$$\text{SM}^t = \frac{1}{R}\sum_{r=1}^{R} \text{sim}\left(\mathbf{s}_r, \hat{\mathbf{s}}_r^t\right)$$

donde $\hat{\mathbf{s}}_r^t$ es la reconstrucción del $r$-ésimo mensaje de referencia en el tiempo $t$ y $\text{sim}(\cdot, \cdot)$ es una métrica de similitud semántica (por ejemplo, similitud coseno en el espacio de representación del modelo fundacional). Si $\text{SM}^t < \text{SM}^{t_0} - \delta$, se detecta deriva semántica y se activa un protocolo de resincronización.

Las estrategias de resincronización incluyen:

- **Actualización completa del modelo**: el transmisor envía los pesos actualizados al receptor (o viceversa). Costoso en ancho de banda pero garantiza sincronización completa.
- **Actualización diferencial**: solo se transmiten las diferencias $\Delta\theta = \theta_{\text{nuevo}} - \theta_{\text{antiguo}}$, potencialmente comprimidas.
- **Destilación de conocimiento**: se entrena un modelo estudiante en el receptor utilizando las salidas del modelo actualizado del transmisor como guía, sin necesidad de transmitir los pesos.
- **Negociación de KB**: ambos extremos intercambian resúmenes de sus bases de conocimiento y resuelven discrepancias.

**Figura 9.4:** *Pila de protocolos modificada con capa semántica. Panel izquierdo: modelo OSI convencional de 7 capas (Aplicación, Presentación, Sesión, Transporte, Red, Enlace, Física), donde cada capa opera de manera independiente sobre flujos de bits sin considerar el significado de los datos. Panel derecho: pila de protocolos semántica propuesta. Se muestra una nueva "Capa Semántica" insertada entre la capa de Aplicación y las capas inferiores. Esta capa contiene los módulos de: (1) extracción semántica, (2) codificación conjunta fuente-canal semántica (JSCC), (3) gestión de base de conocimiento (KB), y (4) control de calidad semántica (QoE semántica). Las capas inferiores (Física y Enlace) se simplifican, ya que la codificación conjunta elimina la necesidad de capas separadas de codificación fuente y canal. Se muestran flechas bidireccionales entre la capa semántica y la capa de aplicación (extracción/entrega de significado), y entre la capa semántica y la capa física (generación/procesamiento de la forma de onda). También se ilustra el protocolo de sincronización de KB entre los extremos Tx y Rx, representado como un canal de señalización bidireccional (plano de control semántico) paralelo al canal de datos.*

---

## 9.8 Perspectivas futuras y 6G

### 9.8.1 Comunicación semántica como pilar de 6G

La sexta generación de comunicaciones móviles (6G), cuyo despliegue se anticipa para la década de 2030, promete una transformación radical respecto a 5G. Mientras que 5G se diseñó para conectar personas y dispositivos con altas tasas de datos, baja latencia y alta fiabilidad, 6G aspira a crear un *mundo conectado inteligente* donde la comunicación trasciende la mera transferencia de bits para convertirse en un intercambio de significado y propósito (Strinati et al., 2021, DOI: 10.1109/MNET.011.2000568).

Las comunicaciones semánticas se perfilan como uno de los pilares fundamentales de la arquitectura 6G por las siguientes razones:

**Eficiencia espectral más allá de Shannon**: La teoría de Shannon establece límites fundamentales para la transmisión fiable de bits. Sin embargo, estos límites asumen que todos los bits son igualmente importantes, lo cual no es cierto cuando el objetivo es transmitir significado. Las comunicaciones semánticas pueden operar "más allá" de la capacidad de Shannon en el sentido de que logran una calidad de tarea superior al transmitir menos bits pero más relevantes. Esto no viola el teorema de Shannon, sino que redefine la métrica de éxito de la comunicación.

**Escalabilidad para el Internet de Todo**: 6G contempla escenarios con billones de dispositivos conectados, incluyendo sensores ambientales, robots, vehículos autónomos, dispositivos de realidad extendida y más. La compresión semántica es esencial para manejar estos volúmenes de datos sin precedentes.

**Soporte para aplicaciones de IA distribuida**: Muchas aplicaciones 6G involucrarán inferencia de IA distribuida, donde los datos capturados por un dispositivo deben procesarse en múltiples nodos de la red. Las comunicaciones semánticas permiten que cada nodo transmita solo las características relevantes para la tarea de IA, reduciendo dramáticamente el tráfico de red.

### 9.8.2 IA nativa en la interfaz aérea

El concepto de "IA nativa" (*native AI*) en la interfaz aérea implica que los algoritmos de inteligencia artificial no son una adición opcional a un sistema de comunicaciones convencional, sino que están integrados desde el diseño fundamental de la capa física. Esto significa que:

- Las señales transmitidas no se generan mediante operaciones de procesamiento digital de señales convencional (modulación, codificación, OFDM), sino mediante redes neuronales.
- El receptor no utiliza algoritmos de estimación de canal, ecualización y demodulación separados, sino una red neuronal integrada de extremo a extremo.
- Los estándares de comunicación no definen formatos de modulación y esquemas de codificación fijos, sino arquitecturas de redes neuronales y protocolos de entrenamiento.

La formulación de IA nativa puede expresarse como:

$$\hat{\mathbf{s}} = g_\phi(r(f_\theta(\mathbf{s}))) \approx \mathbf{s}$$

donde todo el procesamiento de señal está encapsulado en las funciones neuronales $f_\theta$ (transmisor) y $g_\phi$ (receptor), y $r(\cdot)$ representa el canal físico real (no un modelo matemático).

Un desafío clave es la estandarización: mientras que los esquemas de modulación convencionales como 64-QAM están completamente especificados por un estándar, una "red neuronal de modulación" tiene millones de parámetros que pueden variar entre implementaciones. Esto requiere nuevos paradigmas de estandarización que especifiquen interfaces, objetivos de rendimiento y protocolos de interoperabilidad en lugar de implementaciones específicas.

### 9.8.3 Comunicación orientada a objetivos (*goal-oriented communication*)

La comunicación orientada a objetivos representa la evolución más avanzada del paradigma semántico. En lugar de medir el éxito por la fidelidad de reconstrucción del mensaje original, se mide por la utilidad del mensaje para lograr un objetivo específico en el receptor.

Formalmente, el problema de comunicación orientada a objetivos puede plantearse como:

$$\max_{\theta, \phi} \mathbb{E}\left[U\left(a\left(g_\phi(\mathbf{y})\right), \omega\right)\right]$$

sujeto a restricciones de recursos (potencia, ancho de banda, latencia), donde $U(a, \omega)$ es la función de utilidad que depende de la acción $a$ tomada por el receptor (basada en el mensaje decodificado) y del estado del mundo $\omega$. La cadena completa es: el transmisor observa $\mathbf{s}$ (que contiene información parcial sobre $\omega$), codifica y transmite $\mathbf{x} = f_\theta(\mathbf{s})$, el receptor decodifica $\hat{\mathbf{s}} = g_\phi(\mathbf{y})$ y toma una acción $a = \pi(\hat{\mathbf{s}})$.

Ejemplos de comunicación orientada a objetivos incluyen:

- **Conducción autónoma**: un vehículo transmite datos de sensores a un servidor de borde. El objetivo no es reconstruir los datos del sensor perfectamente, sino que el servidor tome decisiones de control correctas (frenar, girar, acelerar).
- **Telecirugía**: un cirujano opera remotamente. El objetivo es que los movimientos del robot quirúrgico sean precisos, no que la imagen del campo quirúrgico sea pixel-perfect.
- **Monitoreo ambiental**: sensores IoT reportan condiciones ambientales. El objetivo es que las alertas de desastres sean oportunas y precisas.

### 9.8.4 Seguridad y privacidad semántica

Las comunicaciones semánticas introducen nuevas dimensiones de seguridad y privacidad que no existen en los sistemas convencionales:

**Seguridad semántica**: En criptografía convencional, un sistema es semánticamente seguro si un adversario no puede distinguir entre las encriptaciones de dos mensajes cualesquiera. En comunicaciones semánticas, la seguridad semántica debe extenderse al nivel del significado: un adversario no debe poder inferir el significado del mensaje, incluso si puede observar la señal transmitida y conoce parcialmente el modelo codificador.

La seguridad semántica puede cuantificarse mediante la información mutua entre la observación del adversario y el significado del mensaje:

$$I(\mathbf{s}; \mathbf{y}_{\text{eve}}) \leq \epsilon_{\text{sec}}$$

donde $\mathbf{y}_{\text{eve}}$ es la señal observada por el adversario y $\epsilon_{\text{sec}}$ es el nivel de seguridad deseado.

**Privacidad de atributos**: Además de proteger el mensaje completo, puede ser necesario proteger atributos específicos. Por ejemplo, en una transmisión de imagen de vigilancia, se desea comunicar la actividad (persona caminando) pero ocultar la identidad (rostro). Esto puede lograrse mediante técnicas de aprendizaje de representaciones invariantes:

$$\min_\theta \mathcal{L}_{\text{tarea}}(f_\theta(\mathbf{s})) + \lambda \cdot I(f_\theta(\mathbf{s}); a_{\text{privado}})$$

donde $a_{\text{privado}}$ es el atributo a proteger y el segundo término penaliza las representaciones que contengan información sobre él.

**Ataques adversarios semánticos**: Los sistemas semánticos basados en redes neuronales son vulnerables a ataques adversarios que perturban sutilmente la entrada para causar errores semánticos catastróficos. Una perturbación imperceptible $\delta$ puede hacer que el sistema interprete completamente mal el mensaje:

$$d_{\text{sem}}\left(\mathbf{s}, g_\phi(h_{\text{canal}}(f_\theta(\mathbf{s} + \delta)))\right) \gg d_{\text{sem}}\left(\mathbf{s}, g_\phi(h_{\text{canal}}(f_\theta(\mathbf{s})))\right)$$

con $\|\delta\| \leq \epsilon$. Desarrollar sistemas semánticos robustos a estos ataques es un problema abierto de investigación.

### 9.8.5 Desafíos de estandarización

La estandarización de las comunicaciones semánticas para 6G enfrenta desafíos sin precedentes:

1. **Interoperabilidad**: ¿Cómo garantizar que dispositivos de diferentes fabricantes, con modelos neuronales potencialmente diferentes, puedan comunicarse entre sí? Se requieren estándares que definan formatos de representación semántica, protocolos de negociación de modelos y mecanismos de conversión entre representaciones.

2. **Métricas de rendimiento**: ¿Cómo definir métricas universales de calidad semántica que sean comparables entre diferentes implementaciones y tipos de contenido? Las métricas de distorsión semántica son inherentemente dependientes de la tarea y la aplicación.

3. **Modelo de referencia**: ¿Cómo actualizar el modelo de referencia de protocolos para incorporar capas semánticas manteniendo la compatibilidad con sistemas existentes?

4. **Certificación y pruebas**: ¿Cómo certificar que un sistema semántico cumple con requisitos de rendimiento cuando su comportamiento depende de redes neuronales cuyo funcionamiento detallado no es completamente interpretable?

5. **Aspectos regulatorios**: ¿Cómo regular formas de onda aprendidas que no corresponden a esquemas de modulación estándar? Las agencias regulatorias necesitan nuevos marcos para evaluar la conformidad espectral de señales generadas por redes neuronales.

### 9.8.6 Problemas abiertos de investigación

La investigación en comunicaciones semánticas es un campo vibrante con numerosos problemas abiertos:

- **Teoría de la información semántica rigurosa**: Aunque los trabajos de Bao et al. y otros han avanzado en la formalización teórica, aún no existe un análogo completo de la teoría de Shannon para comunicaciones semánticas. Se necesitan definiciones formales de entropía semántica, capacidad semántica y teoremas de codificación semántica con demostraciones de alcanzabilidad y converso.

- **Métricas de distorsión semántica universales**: Las métricas existentes (BLEU, SSIM, precisión de clasificación) son específicas de un tipo de datos o tarea. Se requieren métricas que capturen la distorsión semántica de manera universal y que permitan comparaciones justas entre sistemas.

- **Codificación semántica de tasa adaptativa**: Sistemas que ajusten dinámicamente la tasa de compresión semántica en función de la complejidad del contenido, las condiciones del canal y los requisitos del usuario, de manera continua y sin interrupciones.

- **Comunicación semántica multiusuario**: La mayoría de los trabajos existentes consideran escenarios punto a punto. Los escenarios multiusuario (acceso múltiple semántico, difusión semántica, relay semántico) presentan desafíos adicionales de interferencia, asignación de recursos y equidad semántica.

- **Complejidad computacional**: Los modelos neuronales utilizados en comunicaciones semánticas pueden ser computacionalmente costosos, especialmente los basados en transformadores. Es necesario desarrollar arquitecturas eficientes que puedan ejecutarse en tiempo real en dispositivos con recursos limitados, manteniendo la calidad semántica.

- **Explicabilidad y confianza**: Para la adopción en sistemas críticos (salud, transporte, seguridad), los sistemas semánticos deben ser interpretables y predecibles. La naturaleza de "caja negra" de las redes neuronales es una barrera significativa.

- **Integración con infraestructura existente**: Los sistemas semánticos deben coexistir con la infraestructura de comunicaciones actual durante un período de transición prolongado. Se necesitan arquitecturas híbridas que puedan operar en modo semántico o convencional según las capacidades de los extremos.

En conclusión, los temas avanzados presentados en esta sección representan las fronteras más activas de la investigación en comunicaciones semánticas. Desde la conformación inteligente de formas de onda hasta la integración con sistemas MIMO masivo, OTFS y ISAC, desde los modelos fundacionales multimodales hasta el aprendizaje federado y el plano de control semántico, cada uno de estos temas contribuye a la visión de un sistema de comunicaciones que trasciende la transmisión de bits para convertirse en un verdadero intercambio de significado. La convergencia de estas líneas de investigación será fundamental para la realización de las redes 6G y la materialización de un mundo conectado inteligente donde la comunicación sea tan eficiente y natural como la comunicación humana.

---

### Referencias de la Sección 9

- Luo, X. et al. (2022). "Semantic Communications: Overview, Open Issues, and Future Research Directions." *IEEE Communications Surveys & Tutorials*, vol. 24, no. 4, pp. 2586–2630. DOI: [10.1109/COMST.2022.3195590](https://doi.org/10.1109/COMST.2022.3195590)

- Strinati, E. C. et al. (2021). "6G: The Next Frontier." *IEEE Network*, vol. 35, no. 1, pp. 22–28. DOI: [10.1109/MNET.011.2000568](https://doi.org/10.1109/MNET.011.2000568)

- Shi, G. et al. (2021). "From Semantic Communication to Semantic-Aware Networking: Model, Architecture, and Open Problems." *IEEE Journal on Selected Areas in Communications*, vol. 39, no. 8, pp. 2322–2340. DOI: [10.1109/JSAC.2021.3126078](https://doi.org/10.1109/JSAC.2021.3126078)

---

# 10. Conclusiones, Glosario y Referencias

---

## 10.1 Conclusiones y recapitulación

### 10.1.1 Resumen del recorrido tutorial

A lo largo de este tutorial, hemos emprendido un viaje que conecta dos disciplinas que, durante décadas, evolucionaron de manera independiente: la **inteligencia artificial** y las **comunicaciones**. Partimos desde los fundamentos más elementales —la neurona artificial y el perceptrón— y construimos, paso a paso, un edificio conceptual que culmina en los **sistemas de comunicación semántica**, una de las áreas de investigación más prometedoras para las redes de sexta generación (6G) y más allá.

El recorrido puede resumirse en las siguientes etapas fundamentales:

**Etapa 1: El perceptrón como unidad fundamental.** En las secciones iniciales, estudiamos cómo una única neurona artificial puede realizar clasificación binaria mediante la combinación lineal de entradas ponderadas por pesos, seguida de una función de activación:

$$y = f\left(\sum_{i=1}^{n} w_i x_i + b\right)$$

Este modelo, propuesto originalmente por Rosenblatt (1958), constituye el bloque de construcción elemental de todas las arquitecturas de aprendizaje profundo que vendrían después. Comprendimos sus limitaciones —la incapacidad de resolver problemas no linealmente separables como la función XOR— y cómo esta limitación motivó el desarrollo de redes más complejas.

**Etapa 2: Redes multicapa y retropropagación.** Exploramos cómo al apilar múltiples capas de neuronas —formando el perceptrón multicapa (MLP)— se obtiene la capacidad de aproximar cualquier función continua, un resultado formalizado por el **teorema de aproximación universal** (Hornik, 1991). El algoritmo de retropropagación (Rumelhart *et al.*, 1986), basado en la regla de la cadena del cálculo diferencial, proporcionó el mecanismo para entrenar estas redes de manera eficiente:

$$\frac{\partial \mathcal{L}}{\partial w_{ij}^{(l)}} = \frac{\partial \mathcal{L}}{\partial a_j^{(l)}} \cdot \frac{\partial a_j^{(l)}}{\partial z_j^{(l)}} \cdot \frac{\partial z_j^{(l)}}{\partial w_{ij}^{(l)}}$$

Aprendimos que el descenso del gradiente, en sus diversas variantes (SGD, Adam, RMSProp), permite navegar paisajes de pérdida de alta dimensionalidad para encontrar configuraciones de pesos que minimizan la función de costo.

**Etapa 3: Redes convolucionales y la explotación de la estructura espacial.** Las redes neuronales convolucionales (CNN), inspiradas en el trabajo seminal de LeCun *et al.* (1998), introdujeron el concepto de **compartición de pesos** y **conectividad local**, lo que las hace especialmente adecuadas para datos con estructura espacial como imágenes, señales y espectrogramas. La operación de convolución:

$$(\mathbf{X} * \mathbf{K})[i,j] = \sum_m \sum_n \mathbf{X}[i+m, j+n] \cdot \mathbf{K}[m,n]$$

permite detectar patrones locales de forma invariante a la posición, reduciendo drásticamente el número de parámetros respecto a una red completamente conectada. Estas arquitecturas encontraron aplicaciones directas en comunicaciones: estimación de canal, detección de señales y, crucialmente, como codificadores/decodificadores en sistemas de comunicación semántica para imágenes.

**Etapa 4: Redes recurrentes y el modelado de secuencias.** Las RNN y, en particular, las celdas LSTM (Hochreiter y Schmidhuber, 1997) abordaron el desafío de modelar dependencias temporales en datos secuenciales. El mecanismo de compuertas de la LSTM:

$$\mathbf{f}_t = \sigma(\mathbf{W}_f [\mathbf{h}_{t-1}, \mathbf{x}_t] + \mathbf{b}_f)$$
$$\mathbf{i}_t = \sigma(\mathbf{W}_i [\mathbf{h}_{t-1}, \mathbf{x}_t] + \mathbf{b}_i)$$
$$\mathbf{o}_t = \sigma(\mathbf{W}_o [\mathbf{h}_{t-1}, \mathbf{x}_t] + \mathbf{b}_o)$$

permite la preservación selectiva de información a lo largo de secuencias extensas, mitigando los problemas de desvanecimiento y explosión del gradiente. No obstante, la naturaleza inherentemente secuencial de estas redes limita su capacidad de paralelización y, por tanto, su escalabilidad.

**Etapa 5: Mecanismos de atención y la revolución del Transformer.** El mecanismo de atención (Bahdanau *et al.*, 2015) representó un cambio de paradigma al permitir que los modelos aprendan a **focalizar su procesamiento** en las partes más relevantes de la entrada. La auto-atención escalada:

$$\text{Attention}(\mathbf{Q}, \mathbf{K}, \mathbf{V}) = \text{softmax}\left(\frac{\mathbf{Q}\mathbf{K}^T}{\sqrt{d_k}}\right)\mathbf{V}$$

y su extensión multi-cabeza en la arquitectura Transformer (Vaswani *et al.*, 2017) eliminaron la dependencia del procesamiento secuencial, habilitando un entrenamiento masivamente paralelo. El Transformer no solo revolucionó el procesamiento de lenguaje natural —dando lugar a modelos como BERT y GPT— sino que se ha convertido en la arquitectura dominante en múltiples dominios, incluyendo las comunicaciones.

**Etapa 6: Comunicaciones semánticas.** En la culminación del tutorial, convergieron todas las herramientas previamente desarrolladas. Los sistemas de comunicación semántica (Xie *et al.*, 2021) redefinen el objetivo de un sistema de comunicación: en lugar de garantizar la reproducción exacta de bits transmitidos, buscan preservar el **significado** de la información. La arquitectura codificador-canal-decodificador:

$$\hat{s} = D_\phi(C(E_\theta(s)))$$

donde $E_\theta$ es el codificador semántico, $C$ representa el canal de comunicación y $D_\phi$ es el decodificador semántico, se entrena de extremo a extremo (E2E) optimizando una función de pérdida semántica. Este enfoque, conocido como **codificación conjunta fuente-canal** (JSCC), supera la separación clásica fuente-canal de Shannon en regímenes de latencia finita y ofrece una degradación graceful (gradual) del rendimiento con la relación señal a ruido (SNR), eliminando el **efecto acantilado** (*cliff effect*) de los sistemas digitales tradicionales.

### 10.1.2 Lecciones clave del tutorial

Las principales lecciones que emergen de este recorrido son:

1. **El perceptrón es el bloque fundamental.** Toda la complejidad del aprendizaje profundo se construye a partir de la operación elemental de una neurona: una combinación lineal seguida de una no linealidad. Esta simplicidad es poderosa porque permite composición jerárquica.

2. **Los MLP aprenden mediante retropropagación.** El algoritmo de retropropagación, combinado con el descenso del gradiente, proporciona un mecanismo general y escalable para ajustar millones (o miles de millones) de parámetros a partir de datos. El gradiente $\nabla_{\mathbf{w}} \mathcal{L}$ guía la optimización en espacios de muy alta dimensionalidad.

3. **Las CNN explotan la estructura espacial.** Al incorporar **sesgos inductivos** como la invariancia traslacional y la localidad, las CNN logran eficiencia y rendimiento superiores en tareas que involucran datos con estructura espacial: imágenes, señales de comunicación, mapas de canal, etc.

4. **Las RNN/LSTM manejan datos secuenciales, pero tienen limitaciones.** Aunque las RNN y LSTM son capaces de capturar dependencias temporales, su procesamiento secuencial intrínseco limita la paralelización y el manejo de dependencias de muy largo alcance. Estas limitaciones motivaron la búsqueda de alternativas.

5. **Los mecanismos de atención permiten focalizar en lo relevante.** La atención proporciona un mecanismo diferenciable para ponderar dinámicamente la importancia de diferentes partes de la entrada, y puede interpretarse como una forma suave de recuperación de información basada en similitud.

6. **Los Transformers combinan atención con procesamiento paralelo.** Al reemplazar la recurrencia por auto-atención y codificación posicional, los Transformers logran modelar dependencias de rango arbitrario con complejidad computacional $O(n^2 d)$ pero total paralelización. Esto ha permitido escalar los modelos a tamaños sin precedentes y alcanzar rendimiento estado del arte en prácticamente todos los dominios.

7. **Las comunicaciones semánticas aprovechan el aprendizaje profundo para transmitir significado.** Al integrar codificación de fuente y de canal en una sola red neuronal entrenada E2E, los sistemas de comunicación semántica superan las limitaciones del paradigma de Shannon para escenarios prácticos con longitud de bloque finita, recursos limitados y requisitos de baja latencia.

8. **El entrenamiento E2E a través de canales diferenciables habilita la optimización conjunta.** La modelización del canal como una capa diferenciable (ya sea mediante modelos analíticos o redes generativas adversarias) permite que el gradiente fluya desde el decodificador hasta el codificador, optimizando todo el sistema de comunicación como una única red neuronal.

### 10.1.3 El camino hacia adelante: 6G y más allá

El futuro de las comunicaciones semánticas está intrínsecamente ligado a la evolución de las redes móviles hacia la sexta generación (6G), cuyo despliegue se anticipa para la década de 2030. Las principales direcciones de investigación y desarrollo incluyen:

**Comunicación semántica multimodal.** Los sistemas actuales se han centrado predominantemente en modalidades individuales (texto, imagen, voz). El futuro demanda sistemas que integren múltiples modalidades simultáneamente, transmitiendo la semántica de escenas complejas que combinan audio, video, texto y datos sensoriales. Esto requerirá avances en modelos de fusión multimodal y representaciones semánticas unificadas.

**Comunicación orientada a tareas.** Más allá de la reconstrucción fiel de la fuente, los sistemas futuros se orientarán hacia la **efectividad**: transmitir solo la información necesaria para que el receptor complete una tarea específica (clasificación, control, toma de decisiones). Esto implica funciones de pérdida diseñadas en torno al rendimiento de la tarea, no a la fidelidad de reconstrucción.

**Bases de conocimiento compartidas.** Los sistemas de comunicación semántica del futuro podrán aprovechar **bases de conocimiento** compartidas entre transmisor y receptor, permitiendo una compresión aún mayor al transmitir solo las diferencias respecto al conocimiento común. Esto introduce desafíos relacionados con la sincronización del conocimiento y la detección de **deriva semántica** (*semantic drift*).

**Integración con ISAC (Integrated Sensing and Communications).** La convergencia de percepción (radar, localización) y comunicaciones en una sola infraestructura se potenciará con la comunicación semántica, donde los datos sensoriales se comprimen y transmiten preservando su significado relevante para la tarea de percepción.

**Robustez y seguridad.** Los sistemas basados en redes neuronales son vulnerables a ataques adversariales. Garantizar la robustez y seguridad de las comunicaciones semánticas frente a perturbaciones intencionales y condiciones de canal extremas es un desafío abierto crítico.

**Escalabilidad y eficiencia.** La implementación de Transformers de gran escala en dispositivos con recursos limitados (IoT, sensores, dispositivos móviles) requiere técnicas de compresión de modelos, cuantización, poda y destilación de conocimiento.

**Métricas semánticas estandarizadas.** A diferencia de la tasa de error de bit (BER) o la tasa de error de bloque (BLER), no existe aún un consenso sobre métricas universales para evaluar la calidad semántica. El desarrollo de métricas estandarizadas que capturen fielmente la preservación del significado es fundamental para la adopción práctica de estos sistemas.

### 10.1.4 Reflexión final: la convergencia de la IA y las comunicaciones

La historia de las telecomunicaciones ha estado marcada por una separación conceptual clara entre la **fuente de información**, el **canal de transmisión** y el **destino**, siguiendo el modelo propuesto por Shannon en 1948. Esta separación, que demostró ser óptima en el límite asintótico de longitud de bloque infinita, ha sido la piedra angular del diseño de sistemas de comunicación durante más de siete décadas.

Sin embargo, los avances en aprendizaje profundo han revelado que, en condiciones prácticas con restricciones de latencia, ancho de banda y complejidad computacional, la **optimización conjunta** de todos los componentes del sistema de comunicación puede superar significativamente a los diseños modulares tradicionales. Esta convergencia entre IA y comunicaciones no es simplemente una mejora incremental; representa un **cambio de paradigma** en la forma en que concebimos la transmisión de información.

El modelo clásico de Shannon se centra en el **nivel técnico** de la comunicación: ¿con qué precisión pueden transmitirse los símbolos? Las comunicaciones semánticas, apoyadas por las capacidades representacionales del aprendizaje profundo, abordan el **nivel semántico**: ¿con qué precisión los símbolos transmitidos comunican el significado deseado? Y, en última instancia, el **nivel de efectividad**: ¿con qué eficacia el significado recibido afecta la conducta deseada?

Esta visión, articulada por Weaver y Shannon en 1949 pero imposible de realizar con las herramientas de la época, se está materializando ahora gracias a la convergencia de:

- **Potencia computacional** sin precedentes (GPUs, TPUs, aceleradores de IA).
- **Volúmenes masivos de datos** para el entrenamiento de modelos.
- **Arquitecturas neuronales** poderosas y flexibles (especialmente el Transformer).
- **Técnicas de entrenamiento** sofisticadas (E2E, aprendizaje por transferencia, aprendizaje auto-supervisado).

El futuro de las comunicaciones no reside únicamente en transmitir más bits por segundo, sino en transmitir **significado** de manera más eficiente, robusta e inteligente. Los ingenieros y científicos que dominen tanto los fundamentos del aprendizaje profundo como los principios de las comunicaciones estarán en una posición privilegiada para diseñar los sistemas que definirán la próxima era de las telecomunicaciones.

Como reflexión final, cabe señalar que el viaje desde el perceptrón de Rosenblatt hasta los sistemas de comunicación semántica basados en Transformers no es simplemente una progresión tecnológica: es un testimonio de cómo ideas aparentemente simples —una neurona que suma entradas ponderadas, un mecanismo que puntúa la relevancia de diferentes partes de una secuencia, un canal ruidoso modelado como una capa diferenciable— pueden combinarse para crear sistemas de una complejidad y capacidad extraordinarias. Esta es, en esencia, la belleza del aprendizaje profundo aplicado a las comunicaciones: la emergencia de comportamiento inteligente a partir de componentes simples, entrenados de extremo a extremo para un objetivo común.

---

## 10.2 Apéndice matemático

Este apéndice recopila las herramientas matemáticas fundamentales utilizadas a lo largo del tutorial. Su propósito es servir como referencia rápida para el lector que necesite refrescar conceptos específicos, así como proporcionar una visión unificada del aparato matemático que sustenta el aprendizaje profundo y las comunicaciones semánticas.

### 10.2.1 Álgebra lineal

El álgebra lineal constituye el lenguaje fundamental del aprendizaje profundo. Las operaciones sobre vectores y matrices son el núcleo computacional de todas las redes neuronales.

**Vectores.** Un vector $\mathbf{x} \in \mathbb{R}^n$ es una colección ordenada de $n$ números reales:

$$\mathbf{x} = \begin{bmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{bmatrix}$$

**Producto escalar (dot product).** Dados dos vectores $\mathbf{a}, \mathbf{b} \in \mathbb{R}^n$, su producto escalar se define como:

$$\mathbf{a} \cdot \mathbf{b} = \sum_{i=1}^{n} a_i b_i = ||\mathbf{a}||\,||\mathbf{b}||\cos\theta$$

donde $\theta$ es el ángulo entre ambos vectores y $||\mathbf{a}|| = \sqrt{\sum_i a_i^2}$ es la norma euclidiana. Esta relación es fundamental en los mecanismos de atención, donde la similitud entre vectores *query* y *key* se calcula mediante el producto escalar.

**Matrices.** Una matriz $\mathbf{A} \in \mathbb{R}^{m \times n}$ es un arreglo rectangular de números con $m$ filas y $n$ columnas. Las operaciones fundamentales incluyen:

- **Transposición:** $(\mathbf{A}^T)_{ij} = \mathbf{A}_{ji}$, que intercambia filas por columnas.
- **Multiplicación matricial:** Dadas $\mathbf{A} \in \mathbb{R}^{m \times p}$ y $\mathbf{B} \in \mathbb{R}^{p \times n}$:

$$(\mathbf{A}\mathbf{B})_{ij} = \sum_{k=1}^{p} A_{ik} B_{kj}$$

La operación fundamental de una capa neuronal se expresa como $\mathbf{z} = \mathbf{W}\mathbf{x} + \mathbf{b}$, que es una transformación afín donde $\mathbf{W} \in \mathbb{R}^{m \times n}$ es la matriz de pesos y $\mathbf{b} \in \mathbb{R}^m$ es el vector de sesgo.

**Valores y vectores propios.** Una matriz cuadrada $\mathbf{A}$ tiene un valor propio $\lambda$ y un vector propio $\mathbf{v}$ si:

$$\mathbf{A}\mathbf{v} = \lambda\mathbf{v}$$

Estos conceptos son relevantes en el análisis de la convergencia del entrenamiento, en la descomposición de la matriz de covarianza (PCA) y en la comprensión de la dinámica del gradiente.

### 10.2.2 Cálculo diferencial

El cálculo diferencial es esencial para la optimización de redes neuronales, pues el entrenamiento se basa fundamentalmente en el cómputo de gradientes.

**Derivada parcial.** La derivada parcial de una función $f(x_1, x_2, \ldots, x_n)$ respecto a la variable $x_i$ mide la tasa de cambio de $f$ cuando solo $x_i$ varía:

$$\frac{\partial f}{\partial x_i} = \lim_{\Delta x_i \to 0} \frac{f(\ldots, x_i + \Delta x_i, \ldots) - f(\ldots, x_i, \ldots)}{\Delta x_i}$$

**Gradiente.** El vector gradiente agrupa todas las derivadas parciales y apunta en la dirección de máximo crecimiento de la función:

$$\nabla f = \left[\frac{\partial f}{\partial x_1}, \frac{\partial f}{\partial x_2}, \ldots, \frac{\partial f}{\partial x_n}\right]^T$$

En el descenso del gradiente, los parámetros se actualizan en la dirección opuesta al gradiente:

$$\mathbf{w}_{t+1} = \mathbf{w}_t - \eta \nabla_{\mathbf{w}} \mathcal{L}(\mathbf{w}_t)$$

donde $\eta > 0$ es la tasa de aprendizaje.

**Regla de la cadena.** Para funciones compuestas $f(g(x))$, la regla de la cadena establece:

$$\frac{d f}{d x} = \frac{d f}{d g} \cdot \frac{d g}{d x}$$

En su versión multivariable, para $\mathbf{y} = g(\mathbf{x})$ y $z = f(\mathbf{y})$:

$$\frac{\partial z}{\partial x_i} = \sum_j \frac{\partial z}{\partial y_j} \cdot \frac{\partial y_j}{\partial x_i}$$

Esta es la base matemática del algoritmo de retropropagación: el gradiente de la pérdida respecto a los pesos de cada capa se calcula propagando las derivadas parciales desde la salida hacia la entrada, capa por capa.

### 10.2.3 Probabilidad y estadística

Los conceptos probabilísticos permean el aprendizaje profundo, desde la modelización de datos hasta la interpretación de las salidas de los modelos.

**Esperanza matemática.** El valor esperado de una variable aleatoria $X$ con función de densidad $p(x)$ es:

$$\mathbb{E}[X] = \int_{-\infty}^{\infty} x \, p(x) \, dx \quad \text{(caso continuo)}$$

$$\mathbb{E}[X] = \sum_x x \, p(x) \quad \text{(caso discreto)}$$

**Varianza.** La varianza mide la dispersión de $X$ respecto a su media $\mu = \mathbb{E}[X]$:

$$\text{Var}(X) = \mathbb{E}[(X - \mu)^2] = \mathbb{E}[X^2] - (\mathbb{E}[X])^2$$

**Distribución Gaussiana.** La distribución normal $\mathcal{N}(\mu, \sigma^2)$ tiene función de densidad:

$$p(x) = \frac{1}{\sqrt{2\pi\sigma^2}}\exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)$$

Esta distribución es omnipresente en comunicaciones (modelo de ruido AWGN) y en aprendizaje profundo (inicialización de pesos, regularización, modelos generativos). En el caso multivariado, la distribución Gaussiana con vector de medias $\boldsymbol{\mu}$ y matriz de covarianza $\boldsymbol{\Sigma}$ se expresa como:

$$p(\mathbf{x}) = \frac{1}{(2\pi)^{d/2}|\boldsymbol{\Sigma}|^{1/2}}\exp\left(-\frac{1}{2}(\mathbf{x}-\boldsymbol{\mu})^T\boldsymbol{\Sigma}^{-1}(\mathbf{x}-\boldsymbol{\mu})\right)$$

### 10.2.4 Teoría de la información

La teoría de la información, fundada por Shannon (1948), proporciona el marco teórico para las comunicaciones y establece los límites fundamentales que los sistemas de comunicación semántica buscan abordar de manera más eficiente.

**Entropía.** La entropía de una variable aleatoria discreta $X$ cuantifica la incertidumbre promedio asociada a sus posibles valores:

$$H(X) = -\sum_{x \in \mathcal{X}} p(x)\log_2 p(x)$$

Se mide en bits (cuando se usa $\log_2$) y alcanza su máximo para la distribución uniforme: $H(X) \leq \log_2 |\mathcal{X}|$.

**Entropía conjunta y condicional.** La entropía conjunta de dos variables $X$ e $Y$ es:

$$H(X, Y) = -\sum_{x,y} p(x,y) \log_2 p(x,y)$$

La entropía condicional, que mide la incertidumbre restante sobre $X$ dado el conocimiento de $Y$, se define como:

$$H(X|Y) = -\sum_{x,y} p(x,y) \log_2 p(x|y) = H(X,Y) - H(Y)$$

**Información mutua.** La información mutua entre $X$ e $Y$ cuantifica la reducción de incertidumbre sobre una variable al observar la otra:

$$I(X;Y) = H(X) - H(X|Y) = H(Y) - H(Y|X) = H(X) + H(Y) - H(X,Y)$$

La información mutua es simétrica, no negativa, y es igual a cero si y solo si $X$ e $Y$ son estadísticamente independientes. Es la cantidad fundamental que los sistemas de comunicación buscan maximizar.

**Capacidad del canal.** La capacidad de un canal de comunicación es la tasa máxima de información que puede transmitirse de manera fiable:

$$C = \max_{p(x)} I(X;Y)$$

Para el canal AWGN con potencia de señal $P$ y potencia de ruido $N$, la capacidad es:

$$C = \frac{1}{2}\log_2\left(1 + \frac{P}{N}\right) \quad \text{bits por uso del canal}$$

El teorema de codificación de canal de Shannon establece que es posible comunicarse con probabilidad de error arbitrariamente pequeña a cualquier tasa $R < C$, pero no para $R > C$. Los sistemas de comunicación semántica reinterpretan este resultado al operar sobre representaciones de significado en lugar de secuencias de bits.

### 10.2.5 La función Softmax: propiedades y estabilidad numérica

La función softmax transforma un vector de valores reales en una distribución de probabilidad:

$$\text{softmax}(\mathbf{z})_i = \frac{e^{z_i}}{\sum_{j=1}^{K} e^{z_j}}, \quad i = 1, \ldots, K$$

**Propiedades:**

1. **Normalización:** $\sum_{i=1}^{K} \text{softmax}(\mathbf{z})_i = 1$ y $\text{softmax}(\mathbf{z})_i > 0$ para todo $i$.
2. **Invariancia a traslación:** $\text{softmax}(\mathbf{z} + c\mathbf{1}) = \text{softmax}(\mathbf{z})$ para cualquier constante $c$.
3. **Comportamiento límite:** Cuando una componente $z_k \gg z_j$ para todo $j \neq k$, la softmax se aproxima a un vector one-hot.
4. **Temperatura:** La variante con temperatura $\tau > 0$:

$$\text{softmax}(\mathbf{z}/\tau)_i = \frac{e^{z_i/\tau}}{\sum_{j} e^{z_j/\tau}}$$

controla la "suavidad" de la distribución: $\tau \to 0$ produce una distribución concentrada (argmax suave); $\tau \to \infty$ produce una distribución uniforme.

**Estabilidad numérica.** En la práctica, los valores $e^{z_i}$ pueden causar desbordamiento numérico (*overflow*) cuando $z_i$ es grande, o subdesbordamiento (*underflow*) cuando $z_i$ es muy negativo. La solución estándar explota la propiedad de invariancia a traslación:

$$\text{softmax}(\mathbf{z})_i = \frac{e^{z_i - z_{\max}}}{\sum_{j} e^{z_j - z_{\max}}}, \quad z_{\max} = \max_j z_j$$

Al restar el valor máximo, se garantiza que el exponente mayor es $0$, evitando desbordamientos sin alterar el resultado.

### 10.2.6 Cálculo matricial: Jacobianos en la retropropagación

En la retropropagación a través de redes neuronales, las derivadas entre cantidades vectoriales se representan mediante **matrices jacobianas**.

**Matriz Jacobiana.** Dada una función vectorial $\mathbf{f}: \mathbb{R}^n \to \mathbb{R}^m$, la matriz Jacobiana $\mathbf{J} \in \mathbb{R}^{m \times n}$ se define como:

$$\mathbf{J} = \frac{\partial \mathbf{f}}{\partial \mathbf{x}} = \begin{bmatrix}
\frac{\partial f_1}{\partial x_1} & \cdots & \frac{\partial f_1}{\partial x_n} \\
\vdots & \ddots & \vdots \\
\frac{\partial f_m}{\partial x_1} & \cdots & \frac{\partial f_m}{\partial x_n}
\end{bmatrix}$$

**Aplicación en la retropropagación.** Si la capa $l$ computa $\mathbf{z}^{(l)} = \mathbf{W}^{(l)}\mathbf{a}^{(l-1)} + \mathbf{b}^{(l)}$ y $\mathbf{a}^{(l)} = \sigma(\mathbf{z}^{(l)})$, entonces:

$$\frac{\partial \mathcal{L}}{\partial \mathbf{z}^{(l)}} = \frac{\partial \mathcal{L}}{\partial \mathbf{a}^{(l)}} \odot \sigma'(\mathbf{z}^{(l)})$$

$$\frac{\partial \mathcal{L}}{\partial \mathbf{W}^{(l)}} = \frac{\partial \mathcal{L}}{\partial \mathbf{z}^{(l)}} \cdot (\mathbf{a}^{(l-1)})^T$$

$$\frac{\partial \mathcal{L}}{\partial \mathbf{a}^{(l-1)}} = (\mathbf{W}^{(l)})^T \cdot \frac{\partial \mathcal{L}}{\partial \mathbf{z}^{(l)}}$$

donde $\odot$ denota el producto elemento a elemento (producto de Hadamard). Estas ecuaciones forman el núcleo del algoritmo de retropropagación y permiten el cómputo eficiente de gradientes en redes de profundidad arbitraria.

**Jacobiano de la softmax.** Un caso particularmente importante es el Jacobiano de la función softmax. Si $\mathbf{p} = \text{softmax}(\mathbf{z})$, entonces:

$$\frac{\partial p_i}{\partial z_j} = p_i(\delta_{ij} - p_j)$$

donde $\delta_{ij}$ es la delta de Kronecker. Esta expresión se utiliza frecuentemente en la retropropagación a través de capas de atención y clasificación.

---

## 10.3 Glosario de términos

A continuación se presenta un glosario completo de los términos técnicos más relevantes utilizados a lo largo de este tutorial. Cada entrada incluye el término en inglés (cuando difiere) y su definición en español.

1. **Aprendizaje automático** (*Machine Learning*): Rama de la inteligencia artificial que desarrolla algoritmos capaces de aprender patrones a partir de datos sin ser programados explícitamente para cada tarea.

2. **Aprendizaje profundo** (*Deep Learning*): Subconjunto del aprendizaje automático que utiliza redes neuronales con múltiples capas ocultas para aprender representaciones jerárquicas de los datos.

3. **Atención** (*Attention*): Mecanismo que permite a un modelo ponderar dinámicamente la importancia de diferentes partes de la entrada al generar cada elemento de la salida, basándose en una función de similitud entre consultas y claves.

4. **Auto-atención** (*Self-Attention*): Variante del mecanismo de atención donde las consultas, claves y valores provienen de la misma secuencia de entrada, permitiendo que cada posición atienda a todas las demás posiciones de la misma secuencia.

5. **Autoencoder**: Arquitectura de red neuronal que aprende a comprimir (codificar) la entrada en una representación de menor dimensión y luego reconstruirla (decodificar), utilizada para aprendizaje de representaciones y reducción de dimensionalidad.

6. **AWGN** (*Additive White Gaussian Noise*): Modelo de ruido aditivo blanco gaussiano, ampliamente utilizado en comunicaciones para modelar el ruido térmico del canal. Se caracteriza por tener densidad espectral de potencia constante y distribución gaussiana.

7. **Batch Normalization**: Técnica de normalización que estandariza las activaciones de cada capa utilizando la media y varianza del mini-lote actual durante el entrenamiento, acelerando la convergencia y estabilizando el proceso de entrenamiento.

8. **BERT** (*Bidirectional Encoder Representations from Transformers*): Modelo de lenguaje basado en el codificador del Transformer, pre-entrenado bidireccionalmente mediante tareas de modelado de lenguaje enmascarado y predicción de la siguiente oración.

9. **Capacidad del canal** (*Channel Capacity*): Tasa máxima de información (en bits por uso del canal) que puede transmitirse de manera fiable a través de un canal de comunicación, definida como $C = \max_{p(x)} I(X;Y)$.

10. **Capa oculta** (*Hidden Layer*): Capa intermedia de una red neuronal situada entre la capa de entrada y la capa de salida. Las capas ocultas realizan transformaciones no lineales sucesivas que permiten a la red aprender representaciones complejas.

11. **CNN** (*Convolutional Neural Network* / Red Neuronal Convolucional): Tipo de red neuronal que emplea capas de convolución con filtros de pesos compartidos para extraer características locales, especialmente efectiva en datos con estructura espacial como imágenes y señales.

12. **Codificación conjunta fuente-canal** (*JSCC – Joint Source-Channel Coding*): Paradigma de codificación que integra la compresión de fuente y la protección contra errores del canal en un único proceso, en contraste con la separación clásica de Shannon. En el contexto de comunicaciones semánticas, se implementa mediante redes neuronales entrenadas de extremo a extremo.

13. **Codificador** (*Encoder*): Componente de una arquitectura que transforma la entrada en una representación intermedia (latente o codificada). En comunicaciones semánticas, el codificador extrae las características semánticas de la fuente y las mapea a símbolos adecuados para la transmisión por el canal.

14. **Cross-Entropy** (Entropía cruzada): Función de pérdida que mide la discrepancia entre la distribución de probabilidad predicha $\hat{p}$ y la distribución verdadera $p$: $H(p, \hat{p}) = -\sum_x p(x)\log \hat{p}(x)$. Es la función de pérdida estándar para tareas de clasificación.

15. **Decodificador** (*Decoder*): Componente de una arquitectura que transforma la representación intermedia en la salida deseada. En comunicaciones semánticas, el decodificador reconstruye la información semántica a partir de la señal recibida a través del canal.

16. **Descenso del gradiente** (*Gradient Descent*): Algoritmo de optimización iterativo que actualiza los parámetros en la dirección opuesta al gradiente de la función de pérdida: $\mathbf{w}_{t+1} = \mathbf{w}_t - \eta \nabla \mathcal{L}(\mathbf{w}_t)$.

17. **Dropout**: Técnica de regularización que, durante el entrenamiento, desactiva aleatoriamente una fracción $p$ de las neuronas de una capa en cada iteración, forzando a la red a aprender representaciones más robustas y reduciendo el sobreajuste.

18. **E2E** (*End-to-End* / Extremo a extremo): Enfoque de diseño en el que todo el sistema (desde la entrada hasta la salida) se entrena conjuntamente como una sola red neuronal diferenciable, optimizando directamente la métrica de rendimiento final.

19. **Efecto acantilado** (*Cliff Effect*): Fenómeno observado en sistemas de comunicación digital tradicionales donde el rendimiento se degrada abrupta y catastróficamente cuando la SNR cae por debajo de un umbral crítico, en contraste con la degradación gradual de los sistemas analógicos o los sistemas basados en JSCC.

20. **Embedding**: Representación vectorial densa y de baja dimensionalidad de entidades discretas (palabras, tokens, categorías) en un espacio continuo, donde la proximidad geométrica refleja similitud semántica o funcional.

21. **Entropía** (*Entropy*): Medida de la incertidumbre promedio asociada a una variable aleatoria: $H(X) = -\sum_x p(x)\log p(x)$. En teoría de la información, representa el número mínimo de bits necesarios, en promedio, para codificar los resultados de la variable.

22. **Época** (*Epoch*): Una pasada completa por todo el conjunto de datos de entrenamiento. El entrenamiento típicamente requiere múltiples épocas para que los pesos converjan a valores adecuados.

23. **Filtro / Kernel**: Matriz de pesos pequeña (por ejemplo, $3 \times 3$ o $5 \times 5$) que se desliza sobre la entrada en una capa convolucional para detectar patrones locales como bordes, texturas o formas.

24. **Función de activación** (*Activation Function*): Función no lineal aplicada a la salida de una neurona, como ReLU ($f(x) = \max(0,x)$), sigmoide ($\sigma(x) = 1/(1+e^{-x})$) o tanh. Introduce no linealidad en la red, permitiéndole aprender relaciones complejas.

25. **Función de pérdida** (*Loss Function*): Función escalar que cuantifica la discrepancia entre la predicción del modelo y la salida deseada. Su gradiente respecto a los parámetros guía el proceso de entrenamiento. Ejemplos comunes: error cuadrático medio (MSE), entropía cruzada, pérdida semántica.

26. **GPT** (*Generative Pre-trained Transformer*): Familia de modelos de lenguaje basados en el decodificador del Transformer, entrenados de forma auto-regresiva para predecir el siguiente token en una secuencia.

27. **GRU** (*Gated Recurrent Unit*): Variante simplificada de la LSTM que combina las compuertas de olvido y de entrada en una sola compuerta de actualización, reduciendo el número de parámetros mientras mantiene la capacidad de capturar dependencias a largo plazo.

28. **Información mutua** (*Mutual Information*): Medida de la dependencia estadística entre dos variables aleatorias: $I(X;Y) = H(X) - H(X|Y)$. Cuantifica la cantidad de información que una variable proporciona sobre la otra.

29. **ISAC** (*Integrated Sensing and Communications*): Paradigma que integra las funciones de percepción (radar, localización) y comunicación en una sola infraestructura, compartiendo recursos de hardware, espectro y procesamiento de señales.

30. **Layer Normalization** (Normalización de capa): Técnica de normalización que estandariza las activaciones a lo largo de la dimensión de características para cada muestra individual, independientemente del tamaño del lote. Es la normalización predominante en arquitecturas Transformer.

31. **LSTM** (*Long Short-Term Memory*): Tipo de celda de red neuronal recurrente diseñada para capturar dependencias a largo plazo en secuencias, mediante un mecanismo de compuertas (entrada, olvido, salida) que regula el flujo de información a través del estado de celda.

32. **Mapa de características** (*Feature Map*): Salida de una capa convolucional que representa la respuesta de un filtro aplicado sobre la entrada. Cada filtro genera un mapa de características que destaca un patrón específico detectado en la entrada.

33. **MIMO** (*Multiple-Input Multiple-Output*): Tecnología de comunicaciones inalámbricas que utiliza múltiples antenas en el transmisor y el receptor para mejorar la capacidad, la fiabilidad y la eficiencia espectral del enlace.

34. **MLP** (*Multilayer Perceptron* / Perceptrón multicapa): Red neuronal totalmente conectada con una o más capas ocultas, capaz de aproximar funciones continuas arbitrarias según el teorema de aproximación universal.

35. **Multi-Head Attention** (Atención multi-cabeza): Extensión del mecanismo de atención que ejecuta múltiples funciones de atención en paralelo con diferentes proyecciones lineales aprendidas, permitiendo que el modelo atienda simultáneamente a información de diferentes subespacios de representación:
$$\text{MultiHead}(\mathbf{Q}, \mathbf{K}, \mathbf{V}) = \text{Concat}(\text{head}_1, \ldots, \text{head}_h)\mathbf{W}^O$$

36. **OFDM** (*Orthogonal Frequency-Division Multiplexing*): Técnica de modulación multiportadora que divide el espectro disponible en múltiples subportadoras ortogonales de banda estrecha, proporcionando robustez frente al desvanecimiento selectivo en frecuencia y eficiencia espectral.

37. **OTFS** (*Orthogonal Time Frequency Space*): Esquema de modulación que opera en el dominio retardo-Doppler, ofreciendo ventajas sobre OFDM en canales con alta movilidad al representar el canal como una función quasi-estática en el dominio retardo-Doppler.

38. **Overfitting** (Sobreajuste): Fenómeno en el que un modelo se ajusta excesivamente a los datos de entrenamiento, memorizando ruido y particularidades específicas del conjunto de entrenamiento, lo que resulta en un rendimiento pobre sobre datos no vistos.

39. **Perceptrón** (*Perceptron*): Modelo de neurona artificial propuesto por Rosenblatt (1958) que calcula una combinación lineal ponderada de las entradas, le suma un sesgo y aplica una función de activación escalón para producir una salida binaria. Es el bloque de construcción fundamental de las redes neuronales.

40. **Peso** (*Weight*): Parámetro numérico ajustable de una red neuronal que pondera la importancia de cada conexión entre neuronas. Los pesos se ajustan durante el entrenamiento mediante algoritmos de optimización basados en gradientes.

41. **Pooling**: Operación de reducción espacial que reduce las dimensiones de los mapas de características al resumir regiones locales mediante operaciones como el máximo (*max pooling*) o el promedio (*average pooling*), proporcionando cierta invariancia a pequeñas traslaciones y reduciendo la carga computacional.

42. **Positional Encoding** (Codificación posicional): Mecanismo que inyecta información sobre la posición de cada token en una secuencia, necesario en arquitecturas como el Transformer que carecen de recurrencia inherente. Típicamente se implementa mediante funciones sinusoidales:
$$PE_{(pos,2i)} = \sin(pos / 10000^{2i/d_{\text{model}}})$$
$$PE_{(pos,2i+1)} = \cos(pos / 10000^{2i/d_{\text{model}}})$$

43. **Query, Key, Value (Q, K, V)** (Consulta, Clave, Valor): Las tres proyecciones lineales utilizadas en el mecanismo de atención. La *query* representa la consulta de información, la *key* representa las claves contra las que se compara la consulta, y el *value* contiene la información que se agrega ponderadamente según las puntuaciones de atención.

44. **Regularización** (*Regularization*): Conjunto de técnicas para prevenir el sobreajuste, incluyendo regularización L1 ($\lambda\sum|w_i|$), L2 ($\lambda\sum w_i^2$), dropout, data augmentation y early stopping.

45. **Residual Connection** (Conexión residual): Conexión de atajo que suma la entrada de un bloque directamente a su salida ($\mathbf{y} = F(\mathbf{x}) + \mathbf{x}$), facilitando el flujo del gradiente en redes profundas y mitigando el problema de degradación. Introducida por He *et al.* (2016).

46. **Retropropagación** (*Backpropagation*): Algoritmo eficiente para calcular el gradiente de la función de pérdida respecto a todos los pesos de la red, basado en la aplicación recursiva de la regla de la cadena desde la capa de salida hacia la capa de entrada.

47. **RNN** (*Recurrent Neural Network* / Red Neuronal Recurrente): Red neuronal diseñada para procesar datos secuenciales, donde la salida en cada paso temporal depende de la entrada actual y del estado oculto del paso anterior: $\mathbf{h}_t = f(\mathbf{W}_h\mathbf{h}_{t-1} + \mathbf{W}_x\mathbf{x}_t + \mathbf{b})$.

48. **Semantic Communication** (Comunicación semántica): Paradigma de comunicación que busca transmitir el significado o la información semántica del mensaje en lugar de reproducir exactamente la secuencia de bits original, aprovechando técnicas de aprendizaje profundo para lograr mayor eficiencia y robustez.

49. **Semantic Drift** (Deriva semántica): Fenómeno que ocurre cuando las bases de conocimiento o los modelos del transmisor y receptor divergen con el tiempo, causando errores de interpretación semántica. Es un desafío clave en la implementación práctica de sistemas de comunicación semántica.

50. **Sesgo** (*Bias*): (1) En redes neuronales: parámetro aditivo $b$ en la combinación lineal $z = \mathbf{w}^T\mathbf{x} + b$ que permite desplazar la función de activación. (2) En aprendizaje automático: suposiciones implícitas del modelo (*sesgo inductivo*) que facilitan la generalización.

51. **Sigmoide** (*Sigmoid*): Función de activación que mapea valores reales al intervalo $(0,1)$: $\sigma(x) = \frac{1}{1+e^{-x}}$. Históricamente utilizada en redes neuronales, ha sido mayormente reemplazada por ReLU en capas ocultas pero sigue siendo fundamental en compuertas de LSTM/GRU y en la capa de salida para clasificación binaria.

52. **SNR** (*Signal-to-Noise Ratio* / Relación señal a ruido): Métrica que cuantifica la potencia de la señal respecto a la potencia del ruido, típicamente expresada en decibelios: $\text{SNR}_{\text{dB}} = 10\log_{10}(P_s/P_n)$.

53. **Softmax**: Función que transforma un vector de valores reales en una distribución de probabilidad: $\text{softmax}(z_i) = e^{z_i}/\sum_j e^{z_j}$. Se utiliza en la capa de salida para clasificación multiclase y en el mecanismo de atención para obtener pesos de atención normalizados.

54. **Stride** (Paso): Número de posiciones que el filtro se desplaza en cada paso durante la operación de convolución o pooling. Un stride mayor que 1 reduce las dimensiones espaciales de la salida.

55. **Tasa de aprendizaje** (*Learning Rate*): Hiperparámetro $\eta > 0$ que controla el tamaño del paso en la actualización de los pesos durante el descenso del gradiente. Una tasa demasiado alta puede causar divergencia; una demasiado baja, convergencia lenta.

56. **Transformer**: Arquitectura de red neuronal basada enteramente en mecanismos de auto-atención y redes feed-forward, sin recurrencia ni convoluciones. Propuesta por Vaswani *et al.* (2017), permite procesamiento paralelo y captura de dependencias de largo alcance, convirtiéndose en la arquitectura dominante en procesamiento de lenguaje natural, visión por computador y comunicaciones semánticas.

57. **Feed-Forward Network** (Red de propagación hacia adelante): Red neuronal en la que la información fluye exclusivamente desde la entrada hacia la salida, sin conexiones recurrentes ni retroalimentación. En el contexto del Transformer, se refiere a la subred de dos capas lineales con activación no lineal intermedia que se aplica posición por posición tras la capa de atención.

58. **Red generativa adversarial** (*GAN – Generative Adversarial Network*): Arquitectura compuesta por un generador y un discriminador que se entrenan de forma adversarial. En comunicaciones semánticas, los GAN se utilizan para modelar canales complejos y para mejorar la calidad de la reconstrucción semántica.

59. **Desvanecimiento del gradiente** (*Vanishing Gradient*): Problema que ocurre en redes profundas cuando los gradientes se hacen exponencialmente pequeños al propagarse hacia las capas iniciales, dificultando el aprendizaje de las primeras capas. Es especialmente pronunciado con funciones de activación saturantes como la sigmoide y la tangente hiperbólica.

60. **Explosión del gradiente** (*Exploding Gradient*): Problema opuesto al desvanecimiento, donde los gradientes crecen exponencialmente durante la retropropagación, causando inestabilidad numérica y actualizaciones de pesos excesivamente grandes. Se mitiga mediante técnicas como el recorte de gradiente (*gradient clipping*).

61. **Cuantización** (*Quantization*): Técnica de compresión de modelos que reduce la precisión numérica de los pesos y activaciones (por ejemplo, de punto flotante de 32 bits a enteros de 8 bits), reduciendo el tamaño del modelo y acelerando la inferencia con una pérdida mínima de rendimiento.

62. **Destilación de conocimiento** (*Knowledge Distillation*): Técnica en la que un modelo pequeño (estudiante) se entrena para replicar el comportamiento de un modelo grande (profesor), transfiriendo el conocimiento aprendido a una arquitectura más eficiente.

---

## 10.4 Referencias bibliográficas

Las siguientes referencias se organizan por área temática y han sido verificadas con sus respectivos identificadores DOI o de publicación.

### Fundamentos de redes neuronales

[1] F. Rosenblatt, "The Perceptron: A Probabilistic Model for Information Storage and Organization in the Brain," *Psychological Review*, vol. 65, no. 6, pp. 386–408, 1958. DOI: [10.1037/h0042519](https://doi.org/10.1037/h0042519)

[2] D. E. Rumelhart, G. E. Hinton, y R. J. Williams, "Learning representations by back-propagating errors," *Nature*, vol. 323, pp. 533–536, 1986. DOI: [10.1038/323533a0](https://doi.org/10.1038/323533a0)

[3] K. Hornik, "Approximation capabilities of multilayer feedforward networks," *Neural Networks*, vol. 4, no. 2, pp. 251–257, 1991. DOI: [10.1016/0893-6080(91)90009-T](https://doi.org/10.1016/0893-6080(91)90009-T)

[4] Y. LeCun, L. Bottou, Y. Bengio, y P. Haffner, "Gradient-based learning applied to document recognition," *Proceedings of the IEEE*, vol. 86, no. 11, pp. 2278–2324, 1998. DOI: [10.1109/5.726791](https://doi.org/10.1109/5.726791)

[5] S. Hochreiter y J. Schmidhuber, "Long Short-Term Memory," *Neural Computation*, vol. 9, no. 8, pp. 1735–1780, 1997. DOI: [10.1162/neco.1997.9.8.1735](https://doi.org/10.1162/neco.1997.9.8.1735)

### Mecanismos de atención y Transformers

[6] D. Bahdanau, K. Cho, y Y. Bengio, "Neural Machine Translation by Jointly Learning to Align and Translate," en *Proc. International Conference on Learning Representations (ICLR)*, 2015. arXiv: [1409.0473](https://arxiv.org/abs/1409.0473)

[7] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, Ł. Kaiser, e I. Polosukhin, "Attention Is All You Need," en *Advances in Neural Information Processing Systems (NeurIPS)*, vol. 30, 2017. DOI: [10.48550/arXiv.1706.03762](https://doi.org/10.48550/arXiv.1706.03762)

[8] J. Devlin, M.-W. Chang, K. Lee, y K. Toutanova, "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding," en *Proc. North American Chapter of the Association for Computational Linguistics (NAACL)*, 2019. DOI: [10.18653/v1/N19-1423](https://doi.org/10.18653/v1/N19-1423)

### Comunicaciones semánticas

[9] C. E. Shannon, "A Mathematical Theory of Communication," *Bell System Technical Journal*, vol. 27, pp. 379–423, 623–656, 1948. DOI: [10.1002/j.1538-7305.1948.tb01338.x](https://doi.org/10.1002/j.1538-7305.1948.tb01338.x)

[10] H. Xie, Z. Qin, G. Y. Li, y B.-H. Juang, "Deep Learning Enabled Semantic Communication Systems," *IEEE Transactions on Signal Processing*, vol. 69, pp. 2663–2675, 2021. DOI: [10.1109/TSP.2021.3071082](https://doi.org/10.1109/TSP.2021.3071082)

[11] E. Bourtsoulatze, D. Burth Kurka, y D. Gündüz, "Deep Joint Source-Channel Coding for Wireless Image Transmission," *IEEE Transactions on Cognitive Communications and Networking*, vol. 5, no. 3, pp. 567–579, 2019. DOI: [10.1109/TCCN.2019.2919300](https://doi.org/10.1109/TCCN.2019.2919300)

[12] X. Luo, H.-H. Chen, y Q. Guo, "Semantic Communications: Overview, Open Issues, and Future Research Directions," *IEEE Wireless Communications*, vol. 29, no. 1, pp. 210–219, 2022. DOI: [10.1109/MWC.101.2100269](https://doi.org/10.1109/MWC.101.2100269)

### Aprendizaje profundo para comunicaciones

[13] T. O'Shea y J. Hoydis, "An Introduction to Deep Learning for the Physical Layer," *IEEE Transactions on Cognitive Communications and Networking*, vol. 3, no. 4, pp. 563–575, 2017. DOI: [10.1109/TCCN.2017.2758370](https://doi.org/10.1109/TCCN.2017.2758370)

[14] K. He, X. Zhang, S. Ren, y J. Sun, "Deep Residual Learning for Image Recognition," en *Proc. IEEE Conference on Computer Vision and Pattern Recognition (CVPR)*, pp. 770–778, 2016. DOI: [10.1109/CVPR.2016.90](https://doi.org/10.1109/CVPR.2016.90)

### Teoría de la información y comunicaciones

[15] C. E. Shannon y W. Weaver, *The Mathematical Theory of Communication*. Urbana, IL: University of Illinois Press, 1949. ISBN: 978-0252725463

[16] T. M. Cover y J. A. Thomas, *Elements of Information Theory*, 2.ª ed. Hoboken, NJ: Wiley-Interscience, 2006. DOI: [10.1002/047174882X](https://doi.org/10.1002/047174882X)

### Aprendizaje profundo — textos generales

[17] I. Goodfellow, Y. Bengio, y A. Courville, *Deep Learning*. Cambridge, MA: MIT Press, 2016. ISBN: 978-0262035613. Disponible en: [https://www.deeplearningbook.org](https://www.deeplearningbook.org)

[18] Y. LeCun, Y. Bengio, y G. Hinton, "Deep learning," *Nature*, vol. 521, pp. 436–444, 2015. DOI: [10.1038/nature14539](https://doi.org/10.1038/nature14539)

---

*Fin del tutorial.*

*Este tutorial ha proporcionado una introducción integral a las herramientas de inteligencia artificial —desde el perceptrón hasta los Transformers— y su aplicación en los sistemas de comunicación semántica. Esperamos que sirva como punto de partida sólido para investigadores, estudiantes e ingenieros interesados en esta fascinante intersección entre la inteligencia artificial y las telecomunicaciones.*
