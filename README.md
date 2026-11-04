# 🧊 Cero Absoluto — Simulación Física Clásica

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue)](https://python.org)
[![NumPy](https://img.shields.io/badge/NumPy-1.20%2B-orange)](https://numpy.org)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.5%2B-green)](https://matplotlib.org)
[![Licencia](https://img.shields.io/badge/Licencia-MIT-yellow)]()

**Simulaciones computacionales ilustrativas sobre el límite del cero absoluto (0 K), con modelos clásicos y visualizaciones 2D/3D/4D.**

Este proyecto explora la evolución térmica de sistemas físicos al acercarse al Cero Absoluto (0 K), mediante modelos matemáticos y visualizaciones. Las salidas son simulaciones computacionales, no mediciones físicas ni evidencia experimental de fluctuaciones cuánticas.

---

## � Inicio Rápido

```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/Cero-Absoluto-Simulation.git
cd Cero-Absoluto-Simulation

# Crear entorno virtual
python -m venv env
source env/bin/activate  # Linux/Mac
# env\Scripts\activate    # Windows

# Instalar dependencias
pip install numpy matplotlib

# Ejecutar primera simulación
python Cero-Absoluto.py
```

---

## 📦 Contenido del Proyecto

### Scripts de Simulación

| Script | Descripción | Dimensionalidad |
|--------|-------------|-----------------|
| `Cero-Absoluto.py` | Simulación base de enfriamiento exponencial | 2D |
| `Cero-Absoluto01.py` | Modelo con rebote térmico y oscilaciones | 2D |
| `Cero-Absoluto02.py` | Enfriamiento con control activo | 2D |
| `Cero-Absoluto03.py` | Interferencia coherente (animación) | 2D Animada |
| `Cero-Absoluto04.py` | Análisis del "Instante Cero" | 2D Mapa |
| `Cero-Absoluto05.py` | Visualización 3D del campo energético | 3D |
| `Cero-Absoluto06.py` | Fusión matemática/física (escala Kelvin) | 2D Dual |
| `Cero-Absoluto07.py` | Esqueleto matemático del campo | 3D |
| `Cero_Absoluto_4D.py` | Simulación completa (espacio-tiempo-energía-entropía) | 4D |

### Estructura del Proyecto

```
Cero-Absoluto-Simulation/
├── Cero-Absoluto*.py          # Scripts de simulación (9 archivos)
├── README.md                   # Este archivo
├── .gitignore                  # Archivos ignorados por Git
├── docs/                       # Documentación completa
│   ├── scripts/               # Documentación individual de cada script
│   ├── guias/                 # Guías de inicio, instalación y GitHub
│   └── teoria/                # Fundamentos teóricos
└── env/                       # Entorno virtual (no incluido en repo)
```

---

## 🎓 Conceptos Físicos

### Tercera Ley de la Termodinámica
> Es imposible alcanzar el cero absoluto (0 K) mediante ningún proceso finito.

Los scripts ilustran matemáticamente comportamientos compatibles con este principio mediante:
- **Enfriamiento asintótico:** T(t) → 0 pero nunca T(t) = 0
- **Energía del punto cero:** E_min > 0 incluso a T → 0
- **Rebotes térmicos:** Términos oscilatorios incluidos en el modelo (no mediciones de fluctuaciones cuánticas)

### Record de Temperatura
- **NASA Cold Atom Lab:** 3.8 × 10⁻¹¹ K (38 picokelvin)
- **Técnica:** Enfriamiento por evaporación en microgravedad
- **Referencia:** Usado en `Cero-Absoluto06.py` para escala real

---

## 📖 Documentación

La documentación completa está en la carpeta `docs/`:

- **[Guía de Inicio Rápido](docs/guias/inicio-rapido.md)** — Primeros pasos en 5 minutos
- **[Guía de Instalación](docs/guias/instalacion.md)** — Instalación detallada en Windows/Mac/Linux
- **[Guía de GitHub](docs/guias/github-setup.md)** — Cómo subir tu proyecto a GitHub
- **[Teoría del Cero Absoluto](docs/teoria/cero-absoluto.md)** — Fundamentos conceptuales
- **[Termodinámica](docs/teoria/fisica-termodinamica.md)** — Leyes y principios físicos

Cada script tiene su propia documentación detallada en `docs/scripts/`.

---

## 🔬 Modelos Matemáticos

### 1. Enfriamiento Exponencial Base
```
T(t) = T₀ · e^(-αt)
```

### 2. Con Rebote Térmico
```
T(t) = T₀ · e^(-αt) · [1 + β·sin(ωt)·e^(-γt)]
```

### 3. Con Control Activo
```
T(t) = T₀ · e^(-αt) · [1 + β·sin(ωt)·e^(-γt) - K·max(sin(ωt), 0)]
```

### 4. Campo de Interferencia Coherente
```
Y = 2A · sin(k·x) · cos(ω·t)
E_total = ½(∂Y/∂x)² + ½(∂Y/∂t)²
```

---

## 💻 Requisitos

- **Python:** 3.7 o superior
- **NumPy:** 1.20+ (cálculos numéricos)
- **Matplotlib:** 3.5+ (visualización)

```bash
pip install numpy matplotlib
```

---

## 📊 Galería de Visualizaciones

Las simulaciones generan:
- **Gráficos 2D:** Curvas de enfriamiento, mapas de calor
- **Animaciones:** Ondas estacionarias, interferencia
- **Gráficos 3D:** Superficies de energía, esqueletos de campo
- **Visualizaciones 4D:** Campos con entropía codificada en color

*(Agrega capturas de pantalla en `docs/images/` para mostrar ejemplos)*

---

## 🛠️ Uso Avanzado

### Orden Recomendado de Ejecución
```bash
# Principiante: Conceptos básicos
python Cero-Absoluto.py      # Enfriamiento exponencial
python Cero-Absoluto01.py    # Con rebote térmico

# Intermedio: Fenómenos dinámicos
python Cero-Absoluto02.py    # Control activo
python Cero-Absoluto03.py    # Interferencia coherente

# Avanzado: Análisis espacio-temporal
python Cero-Absoluto04.py    # Instante cero
python Cero-Absoluto05.py    # Mapa 3D de energía

# Experto: Fusión y esqueletos
python Cero-Absoluto06.py    # Escala Kelvin real
python Cero-Absoluto07.py    # Esqueleto del campo
python Cero_Absoluto_4D.py   # Simulación 4D completa
```

---

## 🌐 Inspiración y Referencias

- **NASA Cold Atom Lab:** [nasa.gov/coldatomlab](https://www.nasa.gov/coldatomlab)
- **Record de temperatura:** 3.8×10⁻¹¹ K en la ISS (2021)
- **Tercera Ley:** Nernst (1906), Planck (1911)
- **Constantes:** CODATA 2018

---

## 🤝 Contribuir

1. Fork el repositorio
2. Crea una rama (`git checkout -b feature/nueva-simulacion`)
3. Commit tus cambios (`git commit -am 'Agrega nueva simulación'`)
4. Push a la rama (`git push origin feature/nueva-simulacion`)
5. Abre un Pull Request

---

## � Licencia

Uso libre con atribución a **Hanzzel Corp ∑Δ9**.

---

## 👤 Autor

**Hanzzel Corp ∑Δ9**

- Explorando los límites de la física clásica y cuántica mediante simulaciones computacionales

---

<p align="center">🧊 <i>El cero absoluto es asintótico... nunca alcanzable, siempre perseguido</i> 🧊</p>

---

## Dirección de investigación y autoría

**José Zamora — Investigador principal independiente (Independent Principal Investigator), Hanzzel Corp.**

Este repositorio es un proyecto individual del ecosistema Hanzzel Corp. Su pertenencia al ecosistema no implica integración técnica con NCT ni validación de resultados más allá de la evidencia documentada aquí.
