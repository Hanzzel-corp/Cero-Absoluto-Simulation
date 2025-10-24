#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🧊 Mapa 3D — Instante Cero (Tiempo y Espacio detenidos)
-------------------------------------------------------
Versión extendida del modelo de interferencia coherente.
Detecta y visualiza el punto exacto de energía total nula.
Renderiza el espacio-tiempo como un volumen con curvaturas energéticas.

Autor: Hanzzel Corp ∑Δ9
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parámetros de la onda
A = 1.0
f = 1.0
λ = 1.0
ω = 2 * np.pi * f
k = 2 * np.pi / λ

# Alta resolución
x = np.linspace(0, 2*λ, 2000)
t = np.linspace(0, 2/f, 1600)
X, T = np.meshgrid(x, t)

# Campo total (interferencia coherente)
Y = 2 * A * np.sin(k*X) * np.cos(ω*T)

# Derivadas espaciales y temporales
dYdx = 2 * A * k * np.cos(k*X) * np.cos(ω*T)
dYdt = -2 * A * ω * np.sin(k*X) * np.sin(ω*T)

# Energía total (cinética + potencial)
E_pot = 0.5 * (dYdx**2)
E_cin = 0.5 * (dYdt**2)
E_tot = E_pot + E_cin

# Detección del punto de energía mínima absoluta
min_idx = np.unravel_index(np.argmin(E_tot, axis=None), E_tot.shape)
x0, t0 = X[min_idx], T[min_idx]
E0 = E_tot[min_idx]

print(f"🧩 Punto de energía mínima detectado:")
print(f"   x = {x0:.6f}  |  t = {t0:.6f}  |  Energía total ≈ {E0:.6e}")

# Mapa 3D del campo energético
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111, projection='3d')

# Representación logarítmica para visualizar los mínimos
E_log = np.log10(E_tot + 1e-12)
surf = ax.plot_surface(X, T, E_log, cmap='inferno', linewidth=0, antialiased=True, alpha=0.9)

# Punto del cero absoluto
ax.scatter(x0, t0, np.log10(E0 + 1e-12), color='cyan', s=80, label='Instante Cero')

# Etiquetas y estilo
ax.set_xlabel("Espacio (x)")
ax.set_ylabel("Tiempo (t)")
ax.set_zlabel("log(Energía total)")
ax.set_title("🌌 Mapa 3D — Instante Cero (Tiempo y Espacio detenidos)")
ax.legend()
fig.colorbar(surf, shrink=0.5, aspect=10, label='log(Energía total)')
plt.tight_layout()
plt.show()


