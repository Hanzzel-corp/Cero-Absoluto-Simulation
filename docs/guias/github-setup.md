# 🌐 Guía para Subir a GitHub

## Preparación del Repositorio

### 1. Inicializar Git (si no está hecho)

Si el proyecto aún no está versionado con Git:

```bash
cd /mnt/datos/Cero-absoluto  # o tu carpeta del proyecto

# Inicializar repositorio Git
git init

# Configurar tu identidad (si no está configurada)
git config user.name "Tu Nombre"
git config user.email "tu@email.com"
```

### 2. Crear Archivo .gitignore

Crea un archivo `.gitignore` en la raíz del proyecto:

```bash
touch .gitignore
```

Contenido recomendado:

```gitignore
# Entornos virtuales
env/
venv/
ENV/
env.bak/
venv.bak/

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Archivos de sistema
.DS_Store
Thumbs.db
*.swp
*.swo
*~

# IDEs
.vscode/
.idea/
*.sublime-project
*.sublime-workspace

# Archivos de salida
*.png
*.jpg
*.gif
*.mp4
*.avi

# Logs
*.log
```

### 3. Preparar Archivos para Commit

```bash
# Ver estado actual
git status

# Agregar todos los archivos relevantes
git add Cero-Absoluto*.py
git add Cero_Absoluto_4D.py
git add README.md
git add .gitignore
git add docs/

# Verificar qué se va a commitear
git status
```

### 4. Crear Primer Commit

```bash
git commit -m "🧊 Initial commit: Cero Absoluto Simulation Suite

- 9 scripts de simulación termodinámica
- Documentación completa en docs/
- Modelos de enfriamiento clásico y cuántico
- Visualizaciones 2D, 3D y 4D"
```

## Crear Repositorio en GitHub

### Opción A: Línea de Comandos (GitHub CLI)

```bash
# Instalar GitHub CLI si no lo tienes
# https://cli.github.com/

# Autenticar
gh auth login

# Crear repositorio
gh repo create Cero-Absoluto-Simulation \
  --public \
  --description "Simulaciones físicas del Cero Absoluto - Modelos termodinámicos y visualizaciones 2D/3D/4D" \
  --source=. \
  --remote=origin \
  --push
```

### Opción B: Interfaz Web + Terminal

1. **Ir a GitHub:** https://github.com/new

2. **Configurar el repositorio:**
   - **Repository name:** `Cero-Absoluto-Simulation` (o tu nombre preferido)
   - **Description:** `Simulaciones físicas del Cero Absoluto - Modelos termodinámicos y visualizaciones 2D/3D/4D`
   - **Visibility:** Public (o Private)
   - **Initialize:** ❌ NO marcar "Add a README" (ya tenemos uno)
   - **Click:** "Create repository"

3. **Conectar repositorio local con GitHub:**

   GitHub mostrará instrucciones. Usa las de "push an existing repository":

   ```bash
   git remote add origin https://github.com/TU_USUARIO/Cero-Absoluto-Simulation.git
   git branch -M main
   git push -u origin main
   ```

## Verificar Subida

```bash
# Verificar remote configurado
git remote -v

# Debería mostrar:
# origin  https://github.com/TU_USUARIO/Cero-Absoluto-Simulation.git (fetch)
# origin  https://github.com/TU_USUARIO/Cero-Absoluto-Simulation.git (push)
```

Visita: `https://github.com/TU_USUARIO/Cero-Absoluto-Simulation`

## Actualizaciones Futuras

### Flujo de Trabajo Normal

```bash
# 1. Hacer cambios en archivos

# 2. Ver qué cambió
git status

# 3. Agregar cambios
git add archivo-modificado.py
# o
git add -A  # todos los cambios

# 4. Crear commit
git commit -m "Descripción de los cambios"

# 5. Subir a GitHub
git push origin main
```

### Ejemplo de Commit Estructurado

```bash
git commit -m "📚 Actualizar documentación de scripts 03 y 04

- Agregar sección de nodos y antinodos
- Corregir fórmulas de interferencia
- Mejorar ejemplos de uso"
```

## Configuraciones Recomendadas

### README Atractivo
Asegúrate de que tu `README.md` tenga:
- ✅ Título con emoji (🧊)
- ✅ Descripción clara
- ✅ Badges de versión/licencia
- ✅ Screenshots o GIFs de las simulaciones
- ✅ Instrucciones de instalación
- ✅ Ejemplos de uso

### Licencia
Agrega un archivo `LICENSE`:

```bash
# Opciones comunes:
# MIT - Permisivo
# GPL - Copyleft
# Apache - Permisivo con patente

# GitHub puede generarlo automáticamente
# en la interfaz web: Add file → Create new file → LICENSE
```

### Topics/Tags
En GitHub, agrega estos topics al repositorio:
- `physics`
- `simulation`
- `thermodynamics`
- `python`
- `matplotlib`
- `zero-kelvin`
- `quantum-mechanics`
- `visualization`

## Solución de Problemas

### Error: "fatal: not a git repository"
```bash
cd /ruta/correcta/al/proyecto
git init
```

### Error: "Permission denied"
```bash
# Usa HTTPS con token o SSH
# Para HTTPS, genera un Personal Access Token en GitHub
# Settings → Developer settings → Personal access tokens

# O configura SSH:
ssh-keygen -t ed25519 -C "tu@email.com"
cat ~/.ssh/id_ed25519.pub  # Copia y pega en GitHub SSH settings
```

### Error: "failed to push some refs"
```bash
# Primero haz pull para obtener cambios remotos
git pull origin main

# Luego push
git push origin main
```

## Comandos Rápidos de Referencia

| Comando | Descripción |
|---------|-------------|
| `git status` | Ver estado de archivos |
| `git add .` | Agregar todos los cambios |
| `git commit -m "msg"` | Crear commit |
| `git push` | Subir a GitHub |
| `git pull` | Descargar cambios |
| `git log --oneline` | Ver historial |
| `git diff` | Ver cambios sin commitear |

## Siguientes Pasos

1. 🎨 Personaliza el README con screenshots
2. 🏷️ Agrega topics al repositorio
3. 📋 Crea un CHANGELOG.md
4. 🤝 Configura CONTRIBUTING.md si esperas colaboradores
5. 🔗 Agrega enlace a tu portafolio/LinkedIn

¡Tu proyecto está en GitHub! 🎉
