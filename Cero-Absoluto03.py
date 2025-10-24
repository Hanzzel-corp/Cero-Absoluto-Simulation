#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🌊 Interferencia Coherente — Simulación del Cero Vibracional Clásico
--------------------------------------------------------------------
Muestra cómo dos ondas idénticas (no opuestas, sino en fase)
pueden generar una zona de neutralización dinámica:
→ el sistema vibra internamente, pero no hay desplazamiento neto.

Autor: Hanzzel Corp ∑Δ9
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parámetros de la onda
A = 1.0          # Amplitud
f = 1.0          # Frecuencia (Hz)
λ = 1.0          # Longitud de onda
v = f * λ        # Velocidad de propagación
ω = 2 * np.pi * f
k = 2 * np.pi / λ

# Espacio y tiempo
x = np.linspace(0, 2*λ, 500)
t = np.linspace(0, 4/f, 400)

# Figura
fig, ax = plt.subplots(figsize=(10,5))
line1, = ax.plot([], [], lw=2, color='royalblue', label='Onda 1')
line2, = ax.plot([], [], lw=2, color='orange', label='Onda 2')
line_sum, = ax.plot([], [], lw=3, color='black', label='Superposición (nodo)')

ax.set_xlim(0, 2*λ)
ax.set_ylim(-2*A, 2*A)
ax.set_xlabel("Posición (x)")
ax.set_ylabel("Amplitud (A)")
ax.set_title("Interferencia Coherente — Cero Vibracional Clásico")
ax.legend()
ax.grid(True, ls="--", alpha=0.5)

# Animación
def update(frame):
    t_now = t[frame]
    # Dos ondas idénticas, propagándose en sentidos opuestos
    y1 = A * np.sin(k*x - ω*t_now)
    y2 = A * np.sin(k*x + ω*t_now)  # misma fase, sentido contrario
    y_sum = y1 + y2
    line1.set_data(x, y1)
    line2.set_data(x, y2)
    line_sum.set_data(x, y_sum)
    return line1, line2, line_sum

ani = animation.FuncAnimation(fig, update, frames=len(t), interval=20, blit=True)
plt.show()
