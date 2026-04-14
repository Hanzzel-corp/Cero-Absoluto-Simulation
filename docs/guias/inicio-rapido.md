# 🚀 Guía de Inicio Rápido

## Primeros Pasos

### 1. Clonar o Descargar el Proyecto
```bash
git clone https://github.com/tu-usuario/Cero-Absoluto-Simulation.git
cd Cero-Absoluto-Simulation
```

### 2. Crear Entorno Virtual (Recomendado)
```bash
python -m venv env
source env/bin/activate  # Linux/Mac
# o
env\Scripts\activate     # Windows
```

### 3. Instalar Dependencias
```bash
pip install numpy matplotlib
```

### 4. Ejecutar Primera Simulación
```bash
python Cero-Absoluto.py
```

Deberías ver una gráfica de enfriamiento exponencial hacia el cero absoluto.

## Orden Recomendado de Ejecución

Para entender la progresión del proyecto, ejecuta los scripts en este orden:

| Orden | Script | Descripción | Tiempo |
|-------|--------|-------------|--------|
| 1 | `Cero-Absoluto.py` | Simulación base | 5s |
| 2 | `Cero-Absoluto01.py` | Con rebote térmico | 5s |
| 3 | `Cero-Absoluto02.py` | Control activo | 5s |
| 4 | `Cero-Absoluto03.py` | Interferencia coherente (animada) | 15s |
| 5 | `Cero-Absoluto04.py` | Instante cero 2D | 5s |
| 6 | `Cero-Absoluto05.py` | Mapa 3D de energía | 10s |
| 7 | `Cero-Absoluto06.py` | Fusión matemática/física | 5s |
| 8 | `Cero-Absoluto07.py` | Esqueleto del campo | 5s |
| 9 | `Cero_Absoluto_4D.py` | Simulación 4D completa | 10s |

## Verificación de Instalación

Ejecuta este script de prueba:

```python
import numpy as np
import matplotlib.pyplot as plt

print(f"NumPy version: {np.__version__}")
print(f"Matplotlib version: {plt.matplotlib.__version__}")
print("✅ Instalación correcta")
```

## Solución de Problemas Comunes

### Error: "ModuleNotFoundError: No module named 'numpy'"
```bash
pip install numpy matplotlib
```

### Error: "RuntimeError: Invalid DISPLAY variable" (Linux sin GUI)
```bash
# Agrega al inicio del script:
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
```

### Las gráficas no se muestran (se cierran inmediatamente)
Agrega al final de cada script:
```python
input("Presiona Enter para cerrar...")
```

## Próximos Pasos

- 📖 Lee la [Teoría del Cero Absoluto](../teoria/cero-absoluto.md)
- 🔬 Explora la documentación de cada script en `docs/scripts/`
- 🌐 Prepara el proyecto para [GitHub](github-setup.md)
