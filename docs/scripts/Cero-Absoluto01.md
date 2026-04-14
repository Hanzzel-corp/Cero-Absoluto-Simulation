# 🧊 Cero-Absoluto01.py

## Descripción
Simulación del Cero Absoluto con efectos de **rebote térmico**. Este modelo extiende la simulación base incluyendo microoscilaciones internas del sistema, más realistas desde el punto de vista termodinámico.

## Conceptos Físicos

### Rebote Térmico
- Microoscilaciones causadas por reorganización interna del sistema
- Fluctuaciones térmicas inevitables al acercarse al cero
- Amortiguación gradual de estas fluctuaciones

### Energía Residual del Punto Cero
- Energía mínima que persiste incluso a temperatura cero
- Consecuencia de la mecánica cuántica
- Impide alcanzar el 0 K exacto

## Parámetros del Modelo

| Parámetro | Valor | Descripción |
|-----------|-------|-------------|
| alpha | 0.4 | Factor de enfriamiento base |
| beta | 0.3 | Amplitud del rebote térmico |
| omega | 4.0 | Frecuencia del rebote (Hz) |
| gamma | 0.3 | Amortiguación del rebote |
| E_min | 1e-30 J | Energía mínima cuántica |

## Modelo Matemático

```
E_base = E0 * exp(-alpha * t)
Rebote = beta * sin(omega * t) * exp(-gamma * t)
E_total = E_base * (1 + Rebote)
E_final = max(E_total, E_min)
```

El modelo combina:
1. **Enfriamiento exponencial** (tendencia general)
2. **Oscilación sinusoidal** (fluctuaciones térmicas)
3. **Amortiguación** (decrecimiento de fluctuaciones)
4. **Corte cuántico** (límite físico inferior)

## Gráfico Generado

**Título:** "Simulación del Enfriamiento con Rebote (Cero Absoluto Físico)"

**Características:**
- Escala logarítmica en temperatura
- Línea azul real mostrando oscilaciones
- Texto explicativo sobre el comportamiento vibracional

## Diferencias con el Script Base

| Aspecto | Cero-Absoluto.py | Cero-Absoluto01.py |
|---------|------------------|-------------------|
| Modelo | Exponencial puro | Exponencial + oscilaciones |
| Física | Ideal | Con fluctuaciones |
| Resultado | Curva suave | Curva con microoscilaciones |

## Salida de Consola
```
Temperatura final simulada: X.XXXXXe-XX K
→ Se observa un rebote térmico y luego estabilización por energía del punto cero.
```

## Uso
```bash
python Cero-Absoluto01.py
```

## Requisitos
- Python 3.x
- NumPy
- Matplotlib

## Referencias Térmicas
- Fluctuaciones térmicas en sistemas cuánticos
- Amortiguación de oscilaciones térmicas cerca del cero absoluto
