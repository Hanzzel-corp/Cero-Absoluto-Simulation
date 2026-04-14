#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🧊 Cero Absoluto forzado (marco clásico con control activo)
----------------------------------------------------------
- Enfriamiento exponencial natural.
- Rebotes térmicos (reorganización interna del sistema).
- Control activo que intenta "capturar" esos rebotes y drenarlos.
- Límite cuántico final (no podés pasar de ahí sin violar física actual).

Autor: Hanzzel Corp ∑Δ9
"""

import numpy as np
import matplotlib.pyplot as plt

# Constantes físicas
k_B = 1.380649e-23  # Constante de Boltzmann [J/K]

# Parámetros iniciales
E0        = 1e-20     # Energía inicial [J]
alpha     = 0.4       # Enfriamiento base
beta      = 0.3       # Amplitud del rebote interno
omega     = 4.0       # Frecuencia del rebote
gamma     = 0.3       # Amortiguación interna del rebote
control_K = 0.6       # Intensidad del "control activo" (cuánta energía le robamos al rebote)

E_min     = 1e-32     # Límite cuántico residual (energía del punto cero)
n         = 1000

# Eje temporal
t = np.linspace(0, 10, n)

# Energía base que decae
E_base = E0 * np.exp(-alpha * t)

# Rebote térmico interno (lo que vimos antes)
rebote = beta * np.sin(omega * t) * np.exp(-gamma * t)

# Control activo: succiona parte del rebote cuando el rebote es positivo
# Idea física: cuando el sistema intenta oscilar hacia arriba, el control roba esa energía
absorcion_control = control_K * np.clip(rebote, 0, None)

# Energía total = base + rebote - control
E = E_base * (1 + rebote - absorcion_control)

# Nunca bajar del cero cuántico
E = np.maximum(E, E_min)

# Temperatura efectiva
T = E / k_B

# Plot
plt.figure(figsize=(10,5))
plt.plot(t, T, linewidth=2)
plt.title("Intento de Alcanzar el Cero Absoluto con Control Activo")
plt.xlabel("Tiempo (unidades arbitrarias)")
plt.ylabel("Temperatura (K)")
plt.yscale("log")
plt.grid(True, which="both", ls="--", alpha=0.5)
plt.text(0.5, T[0], "Se enfría\nControl absorbe rebotes", fontsize=9)
plt.text(7, 1e-2, "Límite cuántico\n(punto cero)", fontsize=9)
plt.show()

print(f"Temperatura final simulada: {T[-1]:.5e} K")
print("→ El control activo captura los picos, pero la curva sigue sin tocar 0 K exacto.")
