#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🌡️ Cero Kelvin Híbrido — Esqueleto Matemático + Escala Física
--------------------------------------------------------------
Visualiza el punto de energía mínima (modelo clásico) y el
cero absoluto físico (escala Kelvin real) en un mismo gráfico.
Autor: Hanzzel Corp ∑Δ9
"""

import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------------------
# PARTE 1 — MODELO MATEMÁTICO DEL CAMPO (Tu esqueleto)
# -------------------------------------------------------------

A = 1.0
f = 1.0
λ = 1.0
ω = 2 * np.pi * f
k = 2 * np.pi / λ

# Malla fina
x = np.linspace(0, 2*λ, 2000)
t = np.linspace(0, 2/f, 1600)
X, T = np.meshgrid(x, t)

# Campo total
Y = 2 * A * np.sin(k*X) * np.cos(ω*T)
dYdx = 2 * A * k * np.cos(k*X) * np.cos(ω*T)
dYdt = -2 * A * ω * np.sin(k*X) * np.sin(ω*T)

# Energía total
E_pot = 0.5 * (dYdx**2)
E_cin = 0.5 * (dYdt**2)
E_tot = E_pot + E_cin

# Energía mínima detectada
E_min = np.min(E_tot)
x0, t0 = np.unravel_index(np.argmin(E_tot, axis=None), E_tot.shape)
E_min_val = E_tot[x0, t0]

# Normalización de energía para graficar
E_norm = E_tot / np.max(E_tot)

# -------------------------------------------------------------
# PARTE 2 — ESCALA FÍSICA (KELVIN)
# -------------------------------------------------------------

# Convertimos energía arbitraria a Kelvin relativos
# Usando la relación E = k_B * T  (k_B = 1.380649e-23 J/K)
# pero aquí usamos escala relativa
k_B = 1.380649e-23
T_equiv = E_norm * (3.8e-11 / np.min(E_norm[np.nonzero(E_norm)]))

# -------------------------------------------------------------
# PARTE 3 — VISUALIZACIÓN HÍBRIDA
# -------------------------------------------------------------

fig, ax1 = plt.subplots(figsize=(10,6))

# Curva de energía (modelo matemático)
ax1.plot(x, E_norm[int(len(t)/2), :], color='royalblue', lw=2, label='Energía Normalizada (Esqueleto Matemático)')
ax1.set_xlabel("Posición (x)")
ax1.set_ylabel("Energía Normalizada", color='royalblue')
ax1.tick_params(axis='y', labelcolor='royalblue')
ax1.grid(True, ls='--', alpha=0.5)

# Segundo eje — Temperatura en Kelvin reales
ax2 = ax1.twinx()
ax2.plot(x, T_equiv[int(len(t)/2), :], color='darkorange', lw=2, label='Temperatura Equivalente (Kelvin)')
ax2.set_ylabel("Temperatura (K)", color='darkorange')
ax2.tick_params(axis='y', labelcolor='darkorange')
ax2.set_yscale('log')

# Línea de referencia — Cero Humano y Cero Matemático
ax1.axhline(y=np.min(E_norm), color='cyan', lw=2, ls=':', label='Cero Matemático')
ax2.axhline(y=3.8e-11, color='red', lw=2, ls='--', label='Cero Humano (3.8×10⁻¹¹ K)')

# Títulos
plt.title("🌡️ Fusión del Cero Kelvin — Esqueleto Matemático y Cero Físico")
fig.legend(loc="upper right", bbox_to_anchor=(1,1), bbox_transform=ax1.transAxes)
plt.tight_layout()
plt.show()

# -------------------------------------------------------------
print("🧩 Resultado:")
print(f"   Energía mínima simulada (E_min) ≈ {E_min:.6e}")
print(f"   Cero humano de referencia: 3.8×10⁻¹¹ K")
print("   → El punto donde ambas curvas convergen representa el límite físico observable del Cero Kelvin.")



