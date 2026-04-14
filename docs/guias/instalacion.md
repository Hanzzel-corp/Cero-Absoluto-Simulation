# 📦 Guía de Instalación

## Requisitos del Sistema

### Mínimos
- Python 3.7 o superior
- 2 GB RAM
- 100 MB espacio en disco

### Recomendados
- Python 3.10+
- 4 GB RAM
- Tarjeta gráfica con soporte OpenGL (para visualizaciones 3D)

## Instalación Paso a Paso

### 1. Instalar Python

#### Windows
1. Descarga Python desde [python.org](https://python.org)
2. Ejecuta el instalador
3. **IMPORTANTE:** Marca "Add Python to PATH"
4. Selecciona "Install Now"

#### macOS
```bash
# Usando Homebrew
brew install python

# O descarga desde python.org
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

### 2. Verificar Instalación de Python
```bash
python --version
# o
python3 --version
```

Debería mostrar algo como: `Python 3.10.x`

### 3. Crear Entorno Virtual

#### Windows
```cmd
python -m venv env
env\Scripts\activate
```

#### macOS/Linux
```bash
python3 -m venv env
source env/bin/activate
```

Verás `(env)` al inicio de la línea de comandos.

### 4. Instalar Dependencias

```bash
pip install numpy matplotlib
```

Para verificar:
```bash
pip list
```

Deberías ver:
```
numpy        X.X.X
matplotlib   X.X.X
```

### 5. Descargar el Proyecto

#### Opción A: Git (Recomendado)
```bash
git clone https://github.com/tu-usuario/Cero-Absoluto-Simulation.git
cd Cero-Absoluto-Simulation
```

#### Opción B: Descarga ZIP
1. Ve a GitHub → Code → Download ZIP
2. Extrae el archivo
3. Abre terminal en la carpeta extraída

### 6. Ejecutar Primera Simulación

```bash
python Cero-Absoluto.py
```

Si ves una gráfica, ¡la instalación fue exitosa! 🎉

## Dependencias Detalladas

### NumPy
- **Propósito:** Cálculos numéricos, arrays, funciones matemáticas
- **Instalación:** `pip install numpy`
- **Versión mínima:** 1.20.0

### Matplotlib
- **Propósito:** Visualización de datos, gráficos 2D y 3D
- **Instalación:** `pip install matplotlib`
- **Versión mínima:** 3.5.0

### Dependencias Opcionales

Para mejor rendimiento en visualizaciones 3D:
```bash
pip install PyQt5  # Backend gráfico alternativo
```

## Instalación en Diferentes Sistemas

### Windows 10/11
```powershell
# PowerShell como Administrador
python -m venv env
.\env\Scripts\Activate.ps1
pip install numpy matplotlib
```

Si hay error de ejecución de scripts:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### macOS (Intel y Apple Silicon)
```bash
# Verifica tu arquitectura
uname -m  # x86_64 (Intel) o arm64 (Apple Silicon)

# Instalación normal
python3 -m venv env
source env/bin/activate
pip install numpy matplotlib
```

**Nota para Apple Silicon (M1/M2/M3):**
Las versiones recientes de NumPy y Matplotlib tienen soporte nativo ARM64.

### Linux (Ubuntu/Debian/Fedora)

#### Ubuntu/Debian
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv python3-tk
pip3 install numpy matplotlib
```

#### Fedora
```bash
sudo dnf install python3 python3-pip python3-virtualenv
python3 -m venv env
source env/bin/activate
pip install numpy matplotlib
```

#### Arch Linux
```bash
sudo pacman -S python python-pip
python -m venv env
source env/bin/activate
pip install numpy matplotlib
```

## Problemas Comunes y Soluciones

### Error: "No module named 'tkinter'"

#### Ubuntu/Debian
```bash
sudo apt install python3-tk
```

#### Fedora
```bash
sudo dnf install python3-tkinter
```

#### macOS
```bash
brew install python-tk
```

### Error: "Failed building wheel for numpy"
```bash
# Actualiza pip primero
pip install --upgrade pip setuptools wheel

# Luego instala numpy
pip install numpy
```

### Visualizaciones 3D muy lentas
```bash
# Instala un backend más rápido
pip install PyQt5

# Y configúralo en el script:
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
```

## Desinstalación Limpia

Si necesitas eliminar todo:

```bash
# Desactivar entorno
deactivate

# Eliminar carpeta del entorno
# Windows:
rmdir /s env

# macOS/Linux:
rm -rf env

# Eliminar proyecto
# Windows:
rmdir /s Cero-Absoluto-Simulation

# macOS/Linux:
rm -rf Cero-Absoluto-Simulation
```

## Actualización de Dependencias

```bash
source env/bin/activate  # o env\Scripts\activate en Windows
pip install --upgrade numpy matplotlib
```

## Verificación Final

Ejecuta este script de verificación:

```bash
python -c "
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

print('✅ NumPy:', np.__version__)
print('✅ Matplotlib:', plt.matplotlib.__version__)
print('✅ Todas las dependencias están instaladas correctamente')
"
```
