#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🧬 Cero Kelvin — Esqueleto Matemático del Reposo Universal
----------------------------------------------------------
Simula el campo energético y su esqueleto geométrico cuando
el universo se aproxima al cero absoluto.
Autor: Hanzzel Corp ∑Δ9
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parámetros del campo
A = 1.0
f = 1.0
λ = 1.0
ω = 2 * np.pi * f
k = 2 * np.pi / λ

# Malla espacio-tiempo
x = np.linspace(0, 2*λ, 400)
t = np.linspace(0, 2/f, 400)
X, T = np.meshgrid(x, t)

# Campo vibracional
Y = 2 * A * np.sin(k*X) * np.cos(ω*T)

# Derivadas parciales (gradientes)
dYdx = 2 * A * k * np.cos(k*X) * np.cos(ω*T)
dYdt = -2 * A * ω * np.sin(k*X) * np.sin(ω*T)

# Energía total (potencial + cinética)
E_pot = 0.5 * (dYdx**2)
E_cin = 0.5 * (dYdt**2)
E_tot = E_pot + E_cin

# Normalización
E_norm = E_tot / np.max(E_tot)

# Umbral de energía "esquelética"
threshold = 0.05
esqueleto = np.where(E_norm < threshold, E_norm, np.nan)

# --------------------------------------------------------
# Visualización 3D del Esqueleto del Cero
# --------------------------------------------------------
fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111, projection='3d')

# Superficie energética
surf = ax.plot_surface(X, T, E_norm, cmap='inferno', alpha=0.7)

# Superficie del esqueleto (campo casi estático)
ax.plot_surface(X, T, esqueleto, color='cyan', alpha=0.6, rstride=3, cstride=3)

# Líneas de referencia
ax.set_xlabel("Espacio (x)")
ax.set_ylabel("Tiempo (t)")
ax.set_zlabel("Energía normalizada")
ax.set_title("🧬 Esqueleto Matemático del Cero Kelvin — Campo de Reposo")

plt.tight_layout()
plt.show()




