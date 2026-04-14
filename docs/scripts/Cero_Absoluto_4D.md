# 🪐 Cero_Absoluto_4D.py

## Descripción
**Cero Absoluto 4D** - Visualización del campo energético en cuatro dimensiones: **espacio, tiempo, energía y entropía**. Esta es la simulación más completa del proyecto, incorporando la cuarta dimensión como color/gradiente.

## Conceptos Físicos

### Cuatro Dimensiones
1. **Espacio (x):** Posición en el campo
2. **Tiempo (t):** Evolución temporal
3. **Energía (E):** Altura en el gráfico 3D
4. **Entropía (S):** Color de las líneas (velocidad de cambio)

### Entropía Local
- **Definición:** Tasa de cambio temporal de la energía
- **Fórmula:** S = |∂E/∂t|
- **Significado:** Indica qué tan rápido cambia la energía en cada punto

### Representación Cromática
- **Colores fríos (azul/violeta):** Baja entropía (cambio lento)
- **Colores cálidos (amarillo/rojo):** Alta entropía (cambio rápido)
- **Mapa:** 'plasma' de matplotlib

## Parámetros del Modelo

| Parámetro | Valor | Descripción |
|-----------|-------|-------------|
| A | 1.0 | Amplitud del campo |
| f | 1.0 Hz | Frecuencia base |
| λ | 1.0 | Longitud de onda |
| ω | 2π rad/s | Frecuencia angular |
| k | 2π rad/m | Número de onda |
| Resolución | 400×400 | Malla espacio-tiempo |
| Frames | 40 | Líneas temporales mostradas |

## Modelo Matemático

### Campo de Ondas (Modelo Lineal)
```
Y = 2A * sin(k·X) * cos(ω·T)
```

### Energía Total
```
∂Y/∂x = 2A·k * cos(k·X) * cos(ω·T)
∂Y/∂t = -2A·ω * sin(k·X) * sin(ω·T)
E_pot = 0.5 * (∂Y/∂x)²
E_cin = 0.5 * (∂Y/∂t)²
E_tot = E_pot + E_cin
E_norm = E_tot / max(E_tot)
```

### Entropía (Derivada Temporal)
```
dE/dt = ∇ₜ(E_norm)  # Gradiente temporal
S = |dE/dt|         # Valor absoluto
S_norm = S / max(S) # Normalización
```

## Visualización 4D

### Estructura del Gráfico 3D
- **Eje X:** Espacio (x)
- **Eje Y:** Tiempo (t)
- **Eje Z:** Energía normalizada
- **Color:** Entropía normalizada (cmap 'plasma')

### Líneas Temporales
```python
frames = np.linspace(0, len(t)-1, 40, dtype=int)
for i in frame:
    color_map = cm.plasma(Entropy_norm[i])
    ax.plot(x, np.full_like(x, t[i]), E_norm[i], 
            color=color_map.mean(axis=0))
```

Se muestran 40 "rebanadas" temporales del campo.

### Vista Inicial
- **Elevación:** 35 grados
- **Azimut:** 45 grados
- Permite ver la estructura 4D desde perspectiva óptima

## Interpretación Física

### Entropía como Color
- **Regiones azules/moradas:** Equilibrio estable (bajo cambio)
- **Regiones amarillas/rojas:** Transiciones rápidas (alto cambio)
- **Interfaces:** Zonas de alta actividad energética

### Evolución Espacio-Tiempo
Cada línea colorida representa una instantánea del campo en un momento específico:
- La secuencia muestra la evolución temporal
- Los colores revelan dónde ocurren los cambios más rápidos
- La forma 3D muestra la distribución espacial de energía

## Comparativa con Modelos 3D

| Modelo | Dimensiones | Eje Z | Color |
|--------|-------------|-------|-------|
| Cero-Absoluto05.py | 3D | log(Energía) | Energía (inferno) |
| Cero-Absoluto07.py | 3D | Energía normalizada | Esqueleto (cian) |
| Cero_Absoluto_4D.py | 4D | Energía normalizada | Entropía (plasma) |

## Salida de Consola
```
✅ Simulación 4D completada — Cero Absoluto clásico 
   (espacio, tiempo, energía, entropía)
```

## Uso
```bash
python Cero_Absoluto_4D.py
```

## Requisitos
- Python 3.x
- NumPy
- Matplotlib (con mplot3d y colormaps)

## Aplicaciones Avanzadas

### Termodinámica de Campos
- Visualización del flujo de entropía
- Regiones de equilibrio vs. no equilibrio
- Transiciones de fase en campos

### Cosmología Teórica
- Evolución del campo del universo temprano
- Distribución de entropía en el espacio-tiempo
- Estructura de fluctuaciones primigenias

### Física de Partículas
- Campos escalares en teoría de campos
- Evolución de la energía del vacío
- Visualización de modos de oscilación

## Referencias
- Termodinámica de campos escalares
- Visualización de datos 4D
- Entropía en sistemas dinámicos
- Mapas de colores científicos (viridis, plasma, inferno)
