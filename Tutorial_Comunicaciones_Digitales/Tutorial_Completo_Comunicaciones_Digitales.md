# Tutorial de Comunicaciones Digitales: Fundamentos, Modulación, Codificación e Inteligencia Artificial

## Información General

**Título:** Tutorial de Comunicaciones Digitales — De los Fundamentos a la Inteligencia Artificial en Redes 6G

**Audiencia:** Estudiantes de pregrado y posgrado en Ingeniería de Telecomunicaciones, Electrónica o áreas afines. Se asume conocimiento básico de cálculo, álgebra lineal y probabilidad.

**Objetivo:** Proporcionar un recorrido pedagógico, riguroso y detallado por los principios fundamentales de las comunicaciones digitales, desde la teoría de señales y sistemas hasta las técnicas más recientes de inteligencia artificial aplicadas a la capa física y la arquitectura de redes 6G.

**Formato de ecuaciones:** Todas las expresiones matemáticas se presentan en formato LaTeX.

**Idioma:** Español.

---

## Tabla de Contenidos

### [Unidad 1: Introducción a las Comunicaciones Digitales en Banda Base](Unidad1_Introduccion_Comunicaciones_Digitales_Banda_Base.md)

Esta unidad establece el marco teórico para el análisis de señales en sistemas digitales, enfocándose en la naturaleza estocástica de la información y el impacto del ruido.

- **1.1** Fundamentos de Señales Determinísticas y Sistemas Digitales
- **1.2** Análisis de Señales Aleatorias
- **1.3** Respuesta de Sistemas Lineales e Invariantes en el Tiempo (LTI)
- **1.4** Modelado de Ruido
- **1.5** Ancho de Banda de Señales

### [Unidad 2: Teoría de Información y Codificación de Fuente](Unidad2_Teoria_Informacion_Codificacion_Fuente.md)

Se exploran los límites fundamentales de la compresión y la eficiencia en la representación de datos, así como los criterios de detección óptima.

- **2.1** Medida de Información y Entropía
- **2.2** Modulación por Codificación de Pulsos (PCM)
- **2.3** Capacidad de Canal
- **2.4** Detección Digital Óptima

### [Unidad 3: Modulación Digital](Unidad3_Modulacion_Digital.md)

Estudio de las técnicas de adaptación de la señal digital al canal físico, analizando el compromiso entre potencia y ancho de banda.

- **3.1** Análisis de Señales Pasabajas y Pasabanda
- **3.2** Técnicas de Modulación Binaria y M-aria (ASK, FSK, PSK, QPSK)
- **3.3** Modulación de Amplitud en Cuadratura (QAM)
- **3.4** Detección y Demodulación

### [Unidad 4: Codificación de Canal](Unidad4_Codificacion_Canal.md)

Enfoque en la protección de la información frente a errores introducidos por el canal mediante redundancia controlada.

- **4.1** Espacio de Señal y Espacios Vectoriales
- **4.2** Codificación de Bloques
- **4.3** Codificación Convolucional

### [Unidad 5: Introducción a la IA en Telecomunicaciones](Unidad5_IA_Telecomunicaciones.md)

Integración de los conceptos de inteligencia computacional aplicados a la capa física y la arquitectura de red, con visión hacia 6G.

- **5.1** Conceptos Básicos de Redes Neuronales
- **5.2** Receptores Neuronales
- **5.3** IA Nativa en Redes 6G (IMT-2030)

---

## Cómo usar este tutorial

Cada unidad se encuentra en un archivo Markdown independiente, enlazado desde esta tabla de contenidos. El tutorial está diseñado para lectura secuencial, pero cada unidad es razonablemente autocontenida. Las ecuaciones están en formato LaTeX y pueden renderizarse con cualquier visor compatible (GitHub, Jupyter, Pandoc, etc.).

### Convenciones utilizadas

- **Ecuaciones en línea:** Se delimitan con `$...$`
- **Ecuaciones desplegadas:** Se delimitan con `$$...$$`
- **Ejemplos resueltos:** Se identifican con el formato `**Ejemplo X.Y:**`
- **Figuras descriptivas:** Se identifican con el formato `**[Figura X.Y]:**` seguido de un párrafo descriptivo detallado del contenido visual
- **Conceptos clave:** Se resaltan en **negrita**
- **Referencias:** Se incluyen al final de cada unidad con DOI cuando está disponible

---

## Estructura del Repositorio

```
Tutorial_Comunicaciones_Digitales/
├── Tutorial_Completo_Comunicaciones_Digitales.md   ← Este archivo (índice)
├── Unidad1_Introduccion_Comunicaciones_Digitales_Banda_Base.md
├── Unidad2_Teoria_Informacion_Codificacion_Fuente.md
├── Unidad3_Modulacion_Digital.md
├── Unidad4_Codificacion_Canal.md
└── Unidad5_IA_Telecomunicaciones.md
```

---

## Nota sobre las figuras

Las figuras en este tutorial se presentan como **párrafos descriptivos detallados** que especifican con precisión el contenido visual que debe generarse. Cada descripción incluye suficiente detalle (ejes, curvas, etiquetas, rangos, colores sugeridos) para que un generador gráfico (matplotlib, TikZ, herramientas de IA generativa, etc.) pueda producir la figura correspondiente de forma fiel al contexto pedagógico de la sección.

---

*Tutorial generado como material de apoyo para cursos de Comunicaciones Digitales e Inalámbricas.*
