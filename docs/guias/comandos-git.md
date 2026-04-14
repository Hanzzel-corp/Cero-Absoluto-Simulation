# 🔧 Comandos Git de Referencia

## Configuración Inicial

### Configurar Usuario
```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"
```

### Ver Configuración
```bash
git config --list
```

## Comandos Básicos

### Iniciar Repositorio
```bash
git init
```

### Ver Estado
```bash
git status
```

### Agregar Archivos
```bash
git add archivo.py              # Agregar archivo específico
git add carpeta/                # Agregar carpeta
git add .                       # Agregar todos los cambios
git add -A                      # Agregar todos (incluye borrados)
```

### Crear Commit
```bash
git commit -m "Mensaje del commit"
git commit -m "Título" -m "Descripción detallada"
```

### Ver Historial
```bash
git log                         # Historial completo
git log --oneline               # Historial resumido
git log --oneline --graph       # Con gráfico de ramas
git log -5                      # Últimos 5 commits
```

## Trabajo con Remotos

### Ver Remotos Configurados
```bash
git remote -v
```

### Agregar Remoto
```bash
git remote add origin https://github.com/usuario/repo.git
```

### Cambiar URL de Remoto
```bash
git remote set-url origin https://github.com/usuario/nuevo-repo.git
```

### Obtener Cambios
```bash
git fetch origin
```

### Descargar y Fusionar
```bash
git pull origin main
```

### Subir Cambios
```bash
git push origin main
```

### Primera Subida
```bash
git push -u origin main
```

## Ramas

### Ver Ramas
```bash
git branch                      # Ramas locales
git branch -a                   # Todas las ramas (local y remoto)
git branch -r                   # Solo ramas remotas
```

### Crear Rama
```bash
git branch nombre-rama
```

### Cambiar de Rama
```bash
git checkout nombre-rama
```

### Crear y Cambiar (atajo)
```bash
git checkout -b nombre-rama
```

### Fusionar Rama
```bash
git checkout main
git merge nombre-rama
```

### Eliminar Rama
```bash
git branch -d nombre-rama       # Rama fusionada
git branch -D nombre-rama       # Rama no fusionada (forzar)
```

### Subir Rama a GitHub
```bash
git push -u origin nombre-rama
```

## Deshacer Cambios

### Deshacer Cambios en Working Directory
```bash
git checkout -- archivo.py      # Revertir archivo
git checkout -- .               # Revertir todos los cambios
```

### Deshacer Staging
```bash
git reset HEAD archivo.py       # Quitar del staging
```

### Deshacer Último Commit (mantener cambios)
```bash
git reset --soft HEAD~1
```

### Deshacer Último Commit (eliminar cambios)
```bash
git reset --hard HEAD~1
```

### Ver Cambios Antes de Commit
```bash
git diff                        # Working vs Staging
git diff --staged              # Staging vs Último commit
git diff HEAD                  # Working vs Último commit
```

## Stash (Guardar Temporalmente)

### Guardar Cambios
```bash
git stash
```

### Guardar con Nombre
```bash
git stash push -m "descripción"
```

### Ver Stashes
```bash
git stash list
```

### Recuperar Stash
```bash
git stash pop                   # Recuperar y eliminar
git stash apply                 # Recuperar manteniendo stash
```

### Eliminar Stash
```bash
git stash drop stash@{0}
```

## Etiquetas (Tags)

### Crear Tag
```bash
git tag -a v1.0 -m "Versión 1.0"
```

### Ver Tags
```bash
git tag
```

### Subir Tag a GitHub
```bash
git push origin v1.0
git push origin --tags          # Subir todos los tags
```

## Flujo de Trabajo Completo

### 1. Iniciar Proyecto
```bash
mkdir mi-proyecto
cd mi-proyecto
git init
```

### 2. Conectar con GitHub
```bash
git remote add origin https://github.com/usuario/mi-proyecto.git
```

### 3. Flujo Diario
```bash
# Ver cambios
git status

# Agregar cambios
git add .

# Crear commit
git commit -m "Descripción de cambios"

# Subir a GitHub
git push origin main
```

### 4. Trabajar con Ramas
```bash
# Crear rama para nueva feature
git checkout -b feature/nueva-simulacion

# Hacer cambios y commits...
git add .
git commit -m "Agrega nueva simulación"

# Subir rama
git push -u origin feature/nueva-simulacion

# Crear Pull Request en GitHub
# Después de mergear, volver a main y actualizar
git checkout main
git pull origin main

# Eliminar rama local
git branch -d feature/nueva-simulacion
```

## Solución de Problemas

### Error: "fatal: not a git repository"
```bash
cd /ruta/correcta/del/proyecto
# o
git init
```

### Error: "Permission denied"
```bash
# Configurar SSH
git remote set-url origin git@github.com:usuario/repo.git
```

### Error: "failed to push some refs"
```bash
git pull origin main --rebase
git push origin main
```

### Archivos no rastreados aparecen
```bash
# Agregar a .gitignore
echo "archivo.txt" >> .gitignore
git add .gitignore
git commit -m "Agrega archivo a gitignore"
```

## Alias Útiles

### Crear Alias
```bash
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.st status
git config --global alias.lg "log --oneline --graph --all"
```

### Usar Alias
```bash
git co main          # git checkout main
git br               # git branch
git ci -m "msg"      # git commit -m "msg"
git st               # git status
git lg               # git log --oneline --graph --all
```

## Tips

- **Commits frecuentes:** Haz commits pequeños y frecuentes
- **Mensajes claros:** Describe qué cambió y por qué
- **Pull antes de push:** Siempre haz `git pull` antes de `git push`
- **Ramas para features:** Usa ramas para cada nueva característica
- **.gitignore:** Mantén el archivo .gitignore actualizado

## Recursos

- [Git Documentation](https://git-scm.com/doc)
- [GitHub Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
- [Oh Shit, Git!?!](https://ohshitgit.com/) - Solución de problemas
