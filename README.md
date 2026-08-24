# 🤖 AI Eye Tracking Laboratory (Preventative Health Project)

Este repositorio contiene la arquitectura lógica y los algoritmos base para un sistema de visión artificial enfocado en la salud laboral digital, diseñado para monitorizar la fatiga visual humana en tiempo real.

🔗 **Conectado a mi ecosistema principal:** [hazaelu.github.io](https://hazaelu.github.io/)

---

## 🛠️ Requisitos de Infraestructura / Infrastructure Prerequisites

### Español
- **Runtime:** Python 3.10 o superior.
- **Librerías Nucleares:** OpenCV (Procesamiento gráfico) y NumPy (Cálculo matricial de alta velocidad).
- **Hardware:** Cámara web local activa o flujo de video balanceado.

### English
- **Runtime:** Python 3.10 or higher.
- **Core Libraries:** OpenCV (Image processing) and NumPy (High-speed matrix computation).
- **Hardware:** Active local webcam or balanced video data stream.

---

## 🧠 Arquitectura del Algoritmo / Algorithmic Core

```text
[Hardware: Webcam Feed] 
          │
          ▼ (BGR to Gray Matrix Conversion)
[Mathematical Optimization: NumPy Array]
          │
          ▼ (Haar Cascade Classifiers)
[Face Boundary Coordinates (Green Box)]
          │
          ▼ (Region of Interest - ROI Segment)
[Eye Gaze Tracking Detection (Gold Box)]
```

### Español
1. **Conversión Matricial:** El script captura el flujo de video en color (BGR) y lo transforma inmediatamente a escala de grises. Esto reduce las dimensiones de los datos a una sola matriz de luminosidad con **NumPy**, optimizando los ciclos de CPU.
2. **Segmentación ROI (Region of Interest):** En lugar de buscar los ojos en todo el fotograma, el clasificador localiza primero el rostro (`face_cascade`) y recorta esa coordenada matemática específica. La búsqueda de los ojos (`eye_cascade`) se ejecuta únicamente dentro de ese fragmento, economizando ciclos de cómputo.

### English
1. **Matrix Conversion:** The script captures the BGR color stream and instantly converts it to grayscale. This reduces the data dimensions into a single luminosity matrix via **NumPy**, optimizing CPU overhead.
2. **ROI (Region of Interest) Segmentation:** Instead of scanning the entire frame for eyes, the classifier spots the face coordinates first (`face_cascade`). The eye search (`eye_cascade`) is executed exclusively inside that isolated matrix fragment, reducing computational costs.

---

## 🚀 Inicialización del Laboratorio / Local Launch

Para clonar e inicializar este entorno de Inteligencia Artificial de forma segura en su terminal **Bash**, ejecute la siguiente secuencia de comandos:

```bash
# 1. Clonar este laboratorio independiente
git clone https://github.com
cd preventive-eye-ai

# 2. Inicializar y activar el entorno virtual aislado (Linux/macOS)
python3 -m venv venv
source venv/bin/activate

# Nota para entornos Windows: venv\Scripts\activate

# 3. Instalar dependencias moleculares en la nube
pip install -r requirements.txt

# 4. Lanzar el algoritmo de visión artificial
python3 main.py
```
