import matplotlib.pyplot as plt
import numpy as np

# Datos proporcionados
datos = [13, 68, 165, 193, 216, 228, 361, 470, 500, 561,
         634, 647, 692, 695, 699, 802, 896, 899, 936]

# Crear 10 intervalos (bins)
bins = np.linspace(min(datos), max(datos), 11)  # 10 intervalos = 11 bordes

# Crear histograma
fig, ax = plt.subplots(figsize=(10, 5))
n, bins, patches = ax.hist(datos, bins=bins, color='navy', edgecolor='white', rwidth=0.9)

# Etiquetas personalizadas para los intervalos
etiquetas = [f"[{int(bins[i])}, {int(bins[i+1])})" for i in range(len(bins)-1)]
centros = 0.5 * (bins[:-1] + bins[1:])
ax.set_xticks(centros)
ax.set_xticklabels(etiquetas, rotation=45, ha='right', fontsize=9)

# Título y etiquetas
ax.set_title("Histograma", fontsize=14, fontweight='bold')
ax.set_ylabel("Frecuencia")

# Quitar grid y ajustar espacio
ax.grid(False)
plt.tight_layout()

# Mostrar gráfico
plt.show()
