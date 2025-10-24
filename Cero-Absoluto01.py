#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🧊 Simulación del Cero Absoluto con Rebote (Física Clásica Corregida)
---------------------------------------------------------------
Incluye:
- Enfriamiento exponencial.
- Rebote térmico (microoscilaciones).
- Energía residual del punto cero.

Autor: Hanzzel Corp ∑Δ9
"""

import numpy as np
import matplotlib.pyplot as plt

# Constantes
k_B = 1.380649e-23  # Constante de Boltzmann (J/K)
E0 = 1e-20          # Energía inicial (J)
alpha = 0.4         # Factor de enfriamiento
beta = 0.3          # Amplitud del rebote térmico
omega = 4.0         # Frecuencia del rebote
gamma = 0.3         # Amortiguación del rebote
E_min = 1e-30       # Energía mínima (punto cero)
n = 1000

# Tiempo y energía
t = np.linspace(0, 10, n)
E = E0 * np.exp(-alpha * t) * (1 + beta * np.sin(omega * t) * np.exp(-gamma * t))
E = np.maximum(E, E_min)
T = E / k_B

# Gráfica
plt.figure(figsize=(10,5))
plt.plot(t, T, color='royalblue', linewidth=2)
plt.title("Simulación del Enfriamiento con Rebote (Cero Absoluto Físico)")
plt.xlabel("Tiempo (unidades arbitrarias)")
plt.ylabel("Temperatura (K)")
plt.yscale("log")
plt.grid(True, which="both", ls="--", alpha=0.5)
plt.text(1, 1e10, "El sistema vibra cerca del 0 K, nunca lo alcanza", fontsize=9, color='gray')
plt.show()

print(f"Temperatura final simulada: {T[-1]:.5e} K")
print("→ Se observa un rebote térmico y luego estabilización por energía del punto cero.")
