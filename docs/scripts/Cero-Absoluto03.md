# 🌊 Cero-Absoluto03.py

## Descripción
Simulación de **Interferencia Coherente** mostrando el Cero Vibracional Clásico. Este script crea una animación de dos ondas idénticas propagándose en sentidos opuestos, generando una zona de neutralización dinámica.

## Conceptos Físicos

### Interferencia Coherente
- Dos ondas idénticas (misma fase) propagándose en direcciones opuestas
- Superposición que genera nodos estacionarios
- Vibración interna sin desplazamiento neto

### Cero Vibracional
- El sistema vibra internamente
- No hay desplazamiento neto del campo
- Representa un estado de equilibrio dinámico

### Ondas Estacionarias
- Formación de nodos (puntos de amplitud cero)
- Formación de antinodos (puntos de máxima amplitud)
- Patrón espacial que no se desplaza

## Parámetros del Modelo

| Parámetro | Valor | Descripción |
|-----------|-------|-------------|
| A | 1.0 | Amplitud de la onda |
| f | 1.0 Hz | Frecuencia |
| λ | 1.0 | Longitud de onda |
| v | 1.0 | Velocidad de propagación (v = f·λ) |
| ω | 2π rad/s | Frecuencia angular |
| k | 2π rad/m | Número de onda |

## Modelo Matemático

### Ondas Individuales
```
y1 = A * sin(k·x - ω·t)  # Onda propagándose en +x
y2 = A * sin(k·x + ω·t)  # Onda propagándose en -x
```

### Superposición
```
y_sum = y1 + y2 = 2A * sin(k·x) * cos(ω·t)
```

Esta es la ecuación de una **onda estacionaria** con:
- Factor espacial: `sin(k·x)` (determina nodos y antinodos)
- Factor temporal: `cos(ω·t)` (vibración temporal)

## Animación Generada

**Elementos visuales:**
- **Onda 1 (azul):** Propagación hacia la derecha
- **Onda 2 (naranja):** Propagación hacia la izquierda
- **Superposición (negro):** Resultado de la interferencia

**Características:**
- 400 frames de animación
- Intervalo de 20ms entre frames
- Ejes: Posición (x) vs Amplitud (A)

## Nodos y Antinodos

### Nodos (Puntos de Cero)
- Posiciones: x = n·λ/2 (n = 0, 1, 2, ...)
- Amplitud siempre cero
- Puntos de equilibrio perfecto

### Antinodos (Puntos de Máximo)
- Posiciones: x = (2n+1)·λ/4
- Amplitud oscila entre +2A y -2A
- Máxima energía vibracional

## Transición a Modelos Más Avanzados

Este script establece las bases para:
- `Cero-Absoluto04.py`: Análisis del instante cero
- `Cero-Absoluto05.py`: Visualización 3D del campo
- `Cero-Absoluto07.py`: Esqueleto matemático del campo

## Uso
```bash
python Cero-Absoluto03.py
```

**Nota:** La animación se muestra en una ventana interactiva de matplotlib.

## Requisitos
- Python 3.x
- NumPy
- Matplotlib (con soporte de animación)

## Referencias
- Ondas estacionarias: principio de superposición
- Interferencia coherente en física clásica
- Nodos y antinodos en cuerdas vibrantes
