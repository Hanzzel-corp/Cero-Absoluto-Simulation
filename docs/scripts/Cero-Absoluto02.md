# 🧊 Cero-Absoluto02.py

## Descripción
Simulación del **Cero Absoluto forzado** con control activo. Este modelo explora si es posible acelerar el enfriamiento mediante un mecanismo de control que absorbe activamente los rebotes térmicos.

## Conceptos Físicos

### Control Activo
- Mecanismo que "captura" y drena la energía de los rebotes térmicos
- Activación cuando el rebote es positivo (sistema intenta oscilar hacia arriba)
- Robo de energía en los momentos de fluctuación positiva

### Límite Cuántico
- Control activo tiene límites físicos
- No es posible superar la energía del punto cero sin violar principios cuánticos
- Aún con control perfecto, el 0 K exacto es inalcanzable

## Parámetros del Modelo

| Parámetro | Valor | Descripción |
|-----------|-------|-------------|
| E0 | 1e-20 J | Energía inicial |
| alpha | 0.4 | Enfriamiento base |
| beta | 0.3 | Amplitud del rebote interno |
| omega | 4.0 | Frecuencia del rebote |
| gamma | 0.3 | Amortiguación interna |
| control_K | 0.6 | Intensidad del control activo |
| E_min | 1e-32 J | Límite cuántico residual |

## Modelo Matemático

```
E_base = E0 * exp(-alpha * t)
Rebote = beta * sin(omega * t) * exp(-gamma * t)
Absorción = control_K * max(Rebote, 0)
E_total = E_base * (1 + Rebote - Absorción)
E_final = max(E_total, E_min)
```

### Explicación del Control
- `max(Rebote, 0)`: Solo absorbe cuando el rebote es positivo
- `control_K = 0.6`: Absorbe el 60% del rebote positivo
- Representa un sistema de enfriamiento activo optimizado

## Gráfico Generado

**Título:** "Intento de Alcanzar el Cero Absoluto con Control Activo"

**Anotaciones:**
- "Se enfría - Control absorbe rebotes" (etapa inicial)
- "Límite cuántico (punto cero)" (región final)

**Características:**
- Curva más pronunciada al inicio (efecto del control)
- Estabilización más temprana que en modelos sin control
- Línea de límite cuántico visible

## Resultados del Control

### Efectividad
- Captura parcial de picos térmicos
- Aceleración del enfriamiento inicial
- Reducción de fluctuaciones

### Limitaciones
- No elimina completamente las fluctuaciones
- No puede superar el límite cuántico
- El 0 K sigue siendo asintótico

## Comparativa con Scripts Anteriores

| Modelo | Temperatura Final | Tiempo de Enfriamiento | Control |
|--------|-------------------|------------------------|---------|
| Cero-Absoluto.py | ~1e-7 K | Moderado | Ninguno |
| Cero-Absoluto01.py | ~1e-7 K | Moderado | Ninguno |
| Cero-Absoluto02.py | ~7e-9 K | Más rápido | Activo |

## Salida de Consola
```
Temperatura final simulada: X.XXXXXe-XX K
→ El control activo captura los picos, pero la curva sigue sin tocar 0 K exacto.
```

## Uso
```bash
python Cero-Absoluto02.py
```

## Requisitos
- Python 3.x
- NumPy
- Matplotlib

## Referencias
- Sistemas de enfriamiento por evaporación
- Control activo en sistemas cuánticos
- Limitaciones cuánticas del enfriamiento
