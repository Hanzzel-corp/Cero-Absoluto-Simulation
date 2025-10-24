#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🪐 Cero Absoluto 4D — Versión Clásica (Física Vigente)
-------------------------------------------------------
Visualiza el campo energético del universo acercándose al cero absoluto
en cuatro dimensiones: espacio, tiempo, energía y entropía.
Autor: Hanzzel Corp ∑Δ9
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

# Parámetros base (modelo clásico)
A = 1.0           # Amplitud
f = 1.0           # Frecuencia base
λ = 1.0           # Longitud de onda
ω = 2 * np.pi * f # Frecuencia angular
k = 2 * np.pi / λ # Número de onda

# Malla espacio-tiempo
x = np.linspace(0, 2*λ, 400)
t = np.linspace(0, 2/f, 400)
X, T = np.meshgrid(x, t)

# Campo de ondas y energía total (modelo lineal)
Y = 2 * A * np.sin(k*X) * np.cos(ω*T)
dYdx = 2 * A * k * np.cos(k*X) * np.cos(ω*T)
dYdt = -2 * A * ω * np.sin(k*X) * np.sin(ω*T)
E_pot = 0.5 * (dYdx**2)
E_cin = 0.5 * (dYdt**2)
E_tot = E_pot + E_cin
E_norm = E_tot / np.max(E_tot)

# --- Cálculo de entropía local (derivada temporal de la energía)
dE_dt = np.gradient(E_norm, axis=0)
Entropy = np.abs(dE_dt)
Entropy_norm = Entropy / np.max(Entropy)

# --- Visualización 4D: color = entropía (velocidad del cambio energético)
fig = plt.figure(figsize=(11,8))
ax = fig.add_subplot(111, projection='3d')

# Seleccionamos una rebanada para graficar en 3D (tamaño representativo)
frame = np.linspace(0, len(t)-1, 40, dtype=int)
for i in frame:
    color_map = cm.plasma(Entropy_norm[i])
    ax.plot(x, np.full_like(x, t[i]), E_norm[i], color=color_map.mean(axis=0))

# Etiquetas y estética
ax.set_xlabel("Espacio (x)")
ax.set_ylabel("Tiempo (t)")
ax.set_zlabel("Energía Normalizada")
ax.set_title("🪐 Cero Absoluto 4D — Evolución Espacio-Tiempo-Energía-Entropía")

# Ajuste visual
ax.view_init(elev=35, azim=45)
plt.tight_layout()
plt.show()

print("✅ Simulación 4D completada — Cero Absoluto clásico (espacio, tiempo, energía, entropía)")
