import matplotlib.pyplot as plt
import numpy as np

# Datos proporcionados
ciudades = ['Nueva York', 'LA', 'San Francisco']
ventas = [12327, 17129, 19923]
total = sum(ventas)  # 49,379

# Configuración del gráfico
plt.figure(figsize=(10, 6))
bar_colors = ['#1f77b4', '#ff7f0e', '#2ca02c']  # Colores para cada barra
bars = plt.bar(ciudades, ventas, color=bar_colors, edgecolor='black', width=0.7)

# Personalización del gráfico
plt.title('Ventas por Ciudad', fontsize=16, pad=20, fontweight='bold')
plt.ylabel('Frecuencia', fontsize=12, labelpad=10)
plt.ylim(0, max(ventas) * 1.15)  # Margen superior para los valores

# Añadir valores encima de cada barra
for bar in bars:
    height = bar.get_height()
    plt.annotate(f'{height:,}'.replace(',', '.'),  # Formato con puntos separadores
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # 3 puntos de desplazamiento vertical
                textcoords="offset points",
                ha='center', va='bottom',
                fontsize=12)

# Añadir el total en la parte superior
plt.annotate(f'Total: {total:,}'.replace(',', '.'), 
            xy=(0.98, 0.95), 
            xycoords='axes fraction',
            ha='right', va='top',
            fontsize=12,
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", lw=1))

# Mostrar el gráfico
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()