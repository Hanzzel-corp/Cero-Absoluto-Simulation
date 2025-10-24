#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🕰️ Simulación del Instante Cero (Tiempo y Espacio detenidos)
------------------------------------------------------------
Explora el punto donde:
- No hay desplazamiento (y = 0)
- No hay velocidad (∂y/∂t = 0)
- No hay tensión (∂y/∂x = 0)
Es decir, un instante de equilibrio total del campo.

Autor: Hanzzel Corp ∑Δ9
"""

import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la onda
A = 1.0        # Amplitud
f = 1.0        # Frecuencia
λ = 1.0        # Longitud de onda
ω = 2 * np.pi * f
k = 2 * np.pi / λ

# Malla espacio-tiempo
x = np.linspace(0, 2*λ, 500)
t = np.linspace(0, 2/f, 400)

# Campo total (superposición de dos ondas coherentes)
X, T = np.meshgrid(x, t)
Y = 2 * A * np.sin(k*X) * np.cos(ω*T)

# Derivadas espaciales y temporales
dYdx = 2 * A * k * np.cos(k*X) * np.cos(ω*T)
dYdt = -2 * A * ω * np.sin(k*X) * np.sin(ω*T)

# Energía local (clásica)
E_pot = 0.5 * (dYdx**2)
E_cin = 0.5 * (dYdt**2)
E_tot = E_pot + E_cin

# Buscamos el punto donde todo tiende a cero
mask = (np.abs(Y) < 1e-5) & (np.abs(dYdx) < 1e-5) & (np.abs(dYdt) < 1e-5)
indices = np.argwhere(mask)

if len(indices) > 0:
    idx = indices[0]
    x0, t0 = X[idx[0], idx[1]], T[idx[0], idx[1]]
    E0 = E_tot[idx[0], idx[1]]
    print(f"🧊 Punto de simetría total encontrado en:")
    print(f"   x = {x0:.5f}  |  t = {t0:.5f}  |  Energía total ≈ {E0:.5e} J (arbitrario)")
else:
    print("⚠️ No se encontró un punto exacto con energía nula. Aumentá la resolución o relajá los límites.")

# Visualización: mapa de energía total con el punto de equilibrio
plt.figure(figsize=(9, 5))
plt.imshow(E_tot, extent=[x.min(), x.max(), t.min(), t.max()],
           origin='lower', aspect='auto', cmap='inferno', norm=plt.matplotlib.colors.LogNorm(vmin=1e-6, vmax=E_tot.max()))
plt.colorbar(label="Energía total (unidades arbitrarias)")
plt.xlabel("Posición (x)")
plt.ylabel("Tiempo (t)")
plt.title("🕰️ Mapa espacio-temporal — Instante Cero (Energía total ≈ 0)")

if len(indices) > 0:
    plt.scatter(x0, t0, color='cyan', s=80, label='Instante Cero')
    plt.legend()

plt.show()

