# 🧊 Cero-Absoluto.py

## Descripción
Simulación base del acercamiento al Cero Absoluto siguiendo la física moderna. Este script introduce los conceptos fundamentales de la Tercera Ley de la Termodinámica de manera visual e interactiva.

## Conceptos Físicos

### Tercera Ley de la Termodinámica
- A medida que la temperatura se acerca a 0 K, la entropía tiende a un valor mínimo
- El 0 K exacto es asintótico e inalcanzable
- La energía del punto cero persiste incluso al mínimo teórico

### Constantes Utilizadas
| Constante | Valor | Significado |
|-----------|-------|-------------|
| k_B | 1.380649e-23 J/K | Constante de Boltzmann |
| E0 | 1e-20 J | Energía inicial del sistema |
| E_min | 1e-30 J | Energía mínima cuántica |

## Modelo Matemático

```
Energía(t) = E0 * exp(-t)
Temperatura(t) = Energía(t) / k_B
```

El modelo usa una **disipación exponencial** que representa:
- Enfriamiento gradual del sistema
- Pérdida de energía térmica
- Límite asintótico al cero absoluto

## Gráfico Generado

**Ejes:**
- **X:** Tiempo (unidades arbitrarias, 0-10)
- **Y:** Temperatura en escala logarítmica (K)

**Elementos visuales:**
- Línea azul de profundidad mostrando el decaimiento exponencial
- Escala logarítmica para visualizar la asintota
- Anotación explicativa sobre el comportamiento asintótico

## Salida de Consola
```
Temperatura final simulada: X.XXXXXe-XX K
→ Se aproxima al 0 K, pero no lo alcanza (energía del punto cero persiste).
```

## Uso
```bash
python Cero-Absoluto.py
```

## Requisitos
- Python 3.x
- NumPy
- Matplotlib

## Referencias
- Constante de Boltzmann: CODATA 2018
- Tercera Ley de la Termodinámica: Nernst, 1906
