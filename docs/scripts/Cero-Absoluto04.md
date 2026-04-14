# 🕰️ Cero-Absoluto04.py

## Descripción
Simulación del **Instante Cero** - el punto donde el tiempo y el espacio parecen detenerse. Este modelo explora el equilibrio total del campo donde no hay desplazamiento, velocidad ni tensión.

## Conceptos Físicos

### Instante de Equilibrio Total
Un punto (x, t) donde simultáneamente:
- **y = 0:** No hay desplazamiento del campo
- **∂y/∂t = 0:** No hay velocidad (cambio temporal nulo)
- **∂y/∂x = 0:** No hay tensión (gradiente espacial nulo)

### Significado Físico
Representa un momento de **perfecto equilibrio** en el campo energético:
- El sistema está en reposo absoluto momentáneo
- No hay flujo de energía ni en el espacio ni en el tiempo
- Estado transitorio de mínima energía local

## Parámetros del Modelo

| Parámetro | Valor | Descripción |
|-----------|-------|-------------|
| A | 1.0 | Amplitud |
| f | 1.0 Hz | Frecuencia |
| λ | 1.0 | Longitud de onda |
| ω | 2π rad/s | Frecuencia angular |
| k | 2π rad/m | Número de onda |
| Resolución | 500×400 | Malla espacio-tiempo |

## Modelo Matemático

### Campo Total (Superposición Coherente)
```
Y = 2A * sin(k·X) * cos(ω·T)
```

### Derivadas
```
∂Y/∂x = 2A·k * cos(k·X) * cos(ω·T)  # Tensión espacial
∂Y/∂t = -2A·ω * sin(k·X) * sin(ω·T)  # Velocidad temporal
```

### Energía
```
E_pot = 0.5 * (∂Y/∂x)²   # Energía potencial (tensión)
E_cin = 0.5 * (∂Y/∂t)²   # Energía cinética (velocidad)
E_tot = E_pot + E_cin    # Energía total
```

### Condición del Instante Cero
```python
mask = (|Y| < 1e-5) & (|∂Y/∂x| < 1e-5) & (|∂Y/∂t| < 1e-5)
```

## Mapa de Calor Generado

**Visualización:**
- Mapa de energía total en escala logarítmica
- Eje X: Posición (0 a 2λ)
- Eje Y: Tiempo (0 a 2/f)
- Color: Energía total (escala inferno)

**Punto Destacado:**
- Marcador cian indica el "Instante Cero"
- Ubicación precisa del equilibrio total

## Salida de Consola

Cuando se encuentra el punto:
```
🧊 Punto de simetría total encontrado en:
   x = X.XXXXX  |  t = X.XXXXX  |  Energía total ≈ X.XXXXXe-XX J
```

Si no se encuentra (resolución insuficiente):
```
⚠️ No se encontró un punto exacto con energía nula. 
   Aumentá la resolución o relajá los límites.
```

## Interpretación Física

### ¿Qué representa el Instante Cero?
1. **Momento de reposo:** El campo está momentáneamente en equilibrio
2. **Punto de inflexión:** Antes de que la energía fluya en una nueva dirección
3. **Simetría máxima:** Equilibrio perfecto entre componentes espaciales y temporales

### Relación con el Cero Absoluto
- El "Instante Cero" es un **análogo geométrico** del cero absoluto
- Representa el mínimo local de energía
- No es el cero absoluto físico, sino un modelo matemático del reposo

## Gráficos 2D vs 3D

| Aspecto | Cero-Absoluto04.py | Cero-Absoluto05.py |
|---------|-------------------|-------------------|
| Dimensionalidad | 2D (mapa de calor) | 3D (superficie) |
| Perspectiva | Vista plana espacio-tiempo | Volumen con profundidad |
| Énfasis | Detección del punto exacto | Visualización del campo completo |

## Uso
```bash
python Cero-Absoluto04.py
```

## Requisitos
- Python 3.x
- NumPy
- Matplotlib

## Referencias
- Ecuaciones de onda bidimensionales
- Análisis de puntos críticos en campos escalares
- Mínimos locales en energía potencial
