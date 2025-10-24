#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🧊 Simulación del Cero Absoluto (Física Moderna)
------------------------------------------------
Este script muestra cómo un sistema se enfría hacia 0 K,
siguiendo la Tercera Ley de la Termodinámica:
→ A medida que T → 0, la entropía tiende a un valor mínimo.
Pero el 0 K exacto es inalcanzable (asintótico).

Autor: Hanzzel Corp ∑Δ9
"""

import numpy as np
import matplotlib.pyplot as plt

# Constantes físicas
k_B = 1.380649e-23  # Constante de Boltzmann (J/K)
E0 = 1e-20          # Energía inicial del sistema (J)
n = 1000            # Número de pasos

# Simulación de enfriamiento exponencial
tiempo = np.linspace(0, 10, n)
energia = E0 * np.exp(-tiempo)          # disipación exponencial
temperatura = energia / k_B             # conversión a Kelvin

# Evitamos que llegue a cero exacto (mínimo cuántico)
energia_cero = 1e-30
temperatura = np.maximum(temperatura, energia_cero / k_B)

# Visualización
plt.figure(figsize=(10,5))
plt.plot(tiempo, temperatura, color='deepskyblue', linewidth=2)
plt.title("Simulación del acercamiento al Cero Absoluto (Física Moderna)")
plt.xlabel("Tiempo (unidades arbitrarias)")
plt.ylabel("Temperatura (Kelvin)")
plt.yscale("log")
plt.grid(True, which="both", ls="--", alpha=0.5)
plt.text(1, 1e10, "Asintótico → nunca alcanza 0 K", fontsize=10, color='gray')
plt.show()

# Resultado numérico final
print(f"Temperatura final simulada: {temperatura[-1]:.5e} K")
print("→ Se aproxima al 0 K, pero no lo alcanza (energía del punto cero persiste).")
