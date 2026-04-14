# ⚛️ Fundamentos de Termodinámica

## Leyes de la Termodinámica

### Primera Ley (Conservación de la Energía)
> La energía no se crea ni se destruye, solo se transforma.

**Ecuación:**
```
ΔU = Q - W
```

Donde:
- ΔU = cambio en energía interna
- Q = calor transferido al sistema
- W = trabajo realizado por el sistema

### Segunda Ley (Entropía)
> La entropía de un sistema aislado nunca disminuye.

**Ecuación:**
```
ΔS ≥ 0
```

Para procesos reversibles:
```
dS = dQ_rev / T
```

### Tercera Ley (Cero Absoluto)
> Es imposible alcanzar el cero absoluto en un número finito de pasos.

**Implicaciones:**
- La entropía tiende a un mínimo constante cuando T → 0
- Los cristales perfectos tienen S → 0 cuando T → 0

## Conceptos Clave

### Entropía
Medida del desorden o aleatoriedad de un sistema.

**Interpretación Estadística (Boltzmann):**
```
S = k_B · ln(W)
```

Donde:
- k_B = constante de Boltzmann
- W = número de microestados posibles

### Energía Interna
Suma de todas las formas de energía en un sistema.

**Para gas ideal:**
```
U = (f/2) · n · R · T
```

Donde f = grados de libertad.

### Capacidad Calorífica
Cantidad de calor necesaria para cambiar la temperatura.

**Definiciones:**
```
C_v = (∂U/∂T)_v      # A volumen constante
C_p = (∂H/∂T)_p      # A presión constante
```

## Procesos Termodinámicos

| Proceso | Condición | Ecuación |
|---------|-----------|----------|
| Isocórico | V = cte | Q = ΔU |
| Isóbaro | P = cte | W = PΔV |
| Isotermo | T = cte | ΔU = 0, Q = W |
| Adiabático | Q = 0 | PV^γ = cte |

## Ciclos Termodinámicos

### Ciclo de Carnot
El ciclo más eficiente posible.

**Eficiencia:**
```
η = 1 - T_fria / T_caliente
```

### Ciclo de Refrigeración
Coeficiente de rendimiento:
```
COP = Q_fria / W
```

## Aplicación al Cero Absoluto

### Límite de Enfriamiento
A medida que T → 0:
- La eficiencia de refrigeración → 0
- El trabajo necesario → ∞
- El tiempo requerido → ∞

### Capacidad Calorífica a Baja Temperatura
**Ley de Debye:**
```
C_v ∝ T³  (para sólidos a bajas temperaturas)
```

Esto significa que se necesita cada vez menos energía para cambiar la temperatura, ¡pero extraer esa energía se vuelve exponencialmente más difícil!

## Relación con las Simulaciones

### Enfriamiento Exponencial
Los scripts modelan:
```
dT/dt = -α(T - T_ambiente)
```

Solución:
```
T(t) = T_ambiente + (T_0 - T_ambiente)e^(-αt)
```

### Modelo con Rebote Térmico
Incluye términos de:
- **Disipación:** Pérdida de energía al ambiente
- **Fluctuación:** Intercambio interno de energía
- **Amortiguación:** Decaimiento de fluctuaciones

### Modelo con Control Activo
Intenta modificar:
```
dT/dt = -α(T) - control(T)
```

Pero la Tercera Ley establece que:
```
lim(T→0) control(T) < α(T)
```

Por lo tanto, T nunca llega exactamente a cero.

## Constantes Fundamentales

| Constante | Símbolo | Valor | Unidades |
|-----------|---------|-------|----------|
| Boltzmann | k_B | 1.380649×10⁻²³ | J/K |
| Gas ideal | R | 8.314 | J/(mol·K) |
| Avogadro | N_A | 6.02214076×10²³ | mol⁻¹ |
| Planck | h | 6.62607015×10⁻³⁴ | J·s |
| Cero Celsius | T_0 | 273.15 | K |

## Referencias

- **Fermi, E.** (1956). "Thermodynamics"
- **Callen, H.B.** (1985). "Thermodynamics and an Introduction to Thermostatistics"
- **Reif, F.** (1965). "Fundamentals of Statistical and Thermal Physics"
