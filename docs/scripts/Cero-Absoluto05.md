# 🧊 Cero-Absoluto05.py

## Descripción
**Mapa 3D del Instante Cero** - Visualización tridimensional del campo espacio-tiempo-energía. Versión extendida del modelo de interferencia coherente en tres dimensiones.

## Conceptos Físicos

### Visualización 3D del Campo
Representación volumétrica de:
- **Eje X:** Espacio (posición)
- **Eje Y:** Tiempo
- **Eje Z:** Energía total (escala logarítmica)

### Detección de Energía Mínima
- Búsqueda del punto de menor energía en toda la malla
- Identificación precisa de coordenadas (x₀, t₀)
- Medición exacta de E₀ (energía en el mínimo)

## Parámetros del Modelo

| Parámetro | Valor | Descripción |
|-----------|-------|-------------|
| A | 1.0 | Amplitud |
| f | 1.0 Hz | Frecuencia |
| λ | 1.0 | Longitud de onda |
| ω | 2π rad/s | Frecuencia angular |
| k | 2π rad/m | Número de onda |
| Resolución | 2000×1600 | Alta resolución espacio-tiempo |

## Modelo Matemático

### Campo y Derivadas
```
Y = 2A * sin(k·X) * cos(ω·T)
∂Y/∂x = 2A·k * cos(k·X) * cos(ω·T)
∂Y/∂t = -2A·ω * sin(k·X) * sin(ω·T)
```

### Energía Total
```
E_pot = 0.5 * (∂Y/∂x)²
E_cin = 0.5 * (∂Y/∂t)²
E_tot = E_pot + E_cin
```

### Representación Logarítmica
```
E_log = log₁₀(E_tot + 10⁻¹²)
```

El pequeño offset (10⁻¹²) evita log(0) y permite visualizar los mínimos.

## Visualización 3D

### Elementos del Gráfico
1. **Superficie de energía:** Mapa de colores 'inferno' con 90% de opacidad
2. **Punto del Instante Cero:** Marcador cian (s=80)
3. **Ejes etiquetados:**
   - X: Espacio (x)
   - Y: Tiempo (t)
   - Z: log(Energía total)

### Características Visuales
- **Color:** 'inferno' - amarillo/rojo para altas energías, negro/púrpura para bajas
- **Opacidad:** 0.9 para ver estructura interna
- **Marcador:** Cian brillante destacando el mínimo

## Salida de Consola
```
🧩 Punto de energía mínima detectado:
   x = X.XXXXXX  |  t = X.XXXXXX  |  Energía total ≈ X.XXXXXXe-XX
```

## Alta Resolución

### Ventajas
- Detección más precisa del mínimo de energía
- Superficie más suave y detallada
- Mejor visualización de valles energéticos

### Consideraciones
- Mayor consumo de memoria
- Tiempo de renderizado más largo
- Requiere recursos gráficos adecuados

## Comparativa de Scripts de Visualización

| Script | Dimensión | Resolución | Propósito |
|--------|-----------|------------|-----------|
| Cero-Absoluto03.py | 2D animada | 500 puntos | Demostración dinámica |
| Cero-Absoluto04.py | 2D estática | 500×400 | Detección del instante cero |
| Cero-Absoluto05.py | 3D estática | 2000×1600 | Visualización volumétrica |
| Cero-Absoluto07.py | 3D estática | 400×400 | Esqueleto del campo |

## Uso
```bash
python Cero-Absoluto05.py
```

## Requisitos
- Python 3.x
- NumPy
- Matplotlib (con mplot3d)
- Soporte gráfico 3D

## Referencias
- Visualización científica 3D
- Superficies de energía potencial
- Mínimos globales en campos escalares
