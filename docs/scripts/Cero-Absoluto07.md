# 🧬 Cero-Absoluto07.py

## Descripción
**Esqueleto Matemático del Cero Kelvin** - Visualización 3D del campo de reposo universal. Este script muestra la estructura geométrica del campo cuando el universo se aproxima al cero absoluto, destacando las regiones de mínima energía.

## Conceptos Físicos

### Esqueleto del Campo
- **Definición:** Regiones donde la energía es menor que un umbral determinado
- **Umbral:** 5% de la energía máxima (threshold = 0.05)
- **Significado:** Zonas de "reposo" en el campo vibracional

### Campo de Reposo
Cuando el universo se aproxima al cero absoluto:
- Las fluctuaciones se reducen drásticamente
- El campo tiende a un estado casi estático
- Persiste solo la estructura "esquelética" de mínima energía

### Zonas de Mínima Energía
- Representadas en color cian semi-transparente
- Superficies donde E_norm < 0.05
- Geometría del reposo inherente al campo

## Parámetros del Modelo

| Parámetro | Valor | Descripción |
|-----------|-------|-------------|
| A | 1.0 | Amplitud del campo |
| f | 1.0 Hz | Frecuencia |
| λ | 1.0 | Longitud de onda |
| ω | 2π rad/s | Frecuencia angular |
| k | 2π rad/m | Número de onda |
| Resolución | 400×400 | Resolución espacio-tiempo |
| threshold | 0.05 | Umbral para el esqueleto (5%) |

## Modelo Matemático

### Campo Vibracional
```
Y = 2A * sin(k·X) * cos(ω·T)
```

### Gradientes (Derivadas Parciales)
```
∂Y/∂x = 2A·k * cos(k·X) * cos(ω·T)  # Gradiente espacial
∂Y/∂t = -2A·ω * sin(k·X) * sin(ω·T)  # Gradiente temporal
```

### Energía Total
```
E_pot = 0.5 * (∂Y/∂x)²   # Energía potencial
E_cin = 0.5 * (∂Y/∂t)²   # Energía cinética
E_tot = E_pot + E_cin    # Energía total
E_norm = E_tot / max(E_tot)  # Normalización
```

### Esqueleto (Máscara de Umbral)
```python
esqueleto = np.where(E_norm < threshold, E_norm, NaN)
# threshold = 0.05 (5% de la energía máxima)
```

## Visualización 3D

### Superficie Energética Total
- **Color:** Mapa 'inferno' (negro → amarillo)
- **Opacidad:** 0.7 (70% visible)
- **Rango:** 0 a 1 (energía normalizada)

### Superficie del Esqueleto
- **Color:** Cian
- **Opacidad:** 0.6 (60% visible)
- **Resolución:** rstride=3, cstride=3 (menos denso)
- **Significado:** Regiones de E_norm < 0.05

### Ejes y Título
- **X:** Espacio (x)
- **Y:** Tiempo (t)
- **Z:** Energía normalizada
- **Título:** "🧬 Esqueleto Matemático del Cero Kelvin — Campo de Reposo"

## Interpretación Geométrica

### Estructura del Esqueleto
El esqueleto forma una **rejilla espacio-temporal** característica:
- **Periodicidad espacial:** λ/2 (nodos espaciales)
- **Periodicidad temporal:** 1/(2f) (nodos temporales)
- **Forma:** Superficies que conectan los nodos del campo

### Relación con el Cero Absoluto
- El esqueleto representa las **posiciones favorables** de mínima energía
- A medida que T → 0, el sistema queda "atrapado" en estas regiones
- La estructura persiste incluso cuando el resto del campo se disipa

## Comparativa con Cero-Absoluto05.py

| Aspecto | Cero-Absoluto05.py | Cero-Absoluto07.py |
|---------|-------------------|-------------------|
| Resolución | 2000×1600 | 400×400 |
| Enfoque | Punto de mínimo exacto | Estructura del esqueleto |
| Superficies | Una (energía log) | Dos (energía + esqueleto) |
| Representación | Mapa de calor 3D | Esqueleto destacado |
| Umbral | Ninguno (todo el campo) | 5% (solo esqueleto) |

## Uso
```bash
python Cero-Absoluto07.py
```

## Requisitos
- Python 3.x
- NumPy
- Matplotlib (con mplot3d)

## Aplicaciones Conceptuales

### Modelado de Sistemas Cuánticos
- Pozos de potencial en cristales
- Estados de mínima energía en átomos
- Estructura de bandas en sólidos

### Cosmología
- Estructura del vacío cuántico
- Fluctuaciones del campo en el universo temprano
- Geometría del espacio-tiempo "frío"

## Referencias
- Estructuras periódicas en campos escalares
- Nodos y superficies nodales en física cuántica
- Geometría de estados de mínima energía
