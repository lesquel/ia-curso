import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import PercentFormatter

# Datos para el gráfico
ciudades = ['San Francisco', 'LA', 'Nueva York']
participacion = [40, 35, 25]  # Porcentajes de participación
ventas = [19923, 17129, 12327]  # Valores absolutos de ventas
total_ventas = sum(ventas)

# Calcular frecuencia acumulada
acumulado = np.cumsum(ventas)
porcentaje_acumulado = acumulado / total_ventas * 100

# Configuración del gráfico
fig, ax1 = plt.subplots(figsize=(12, 8))

# --- Tarea 5: Gráfico circular ---
# Crear un eje para el gráfico circular
ax_pie = fig.add_axes([0.35, 0.35, 0.3, 0.3])  # [left, bottom, width, height]

# Colores para las porciones
colors = ['#FF9999', '#66B2FF', '#99FF99']
explode = (0.1, 0.05, 0)  # Destacar San Francisco

# Dibujar el gráfico circular
wedges, texts, autotexts = ax_pie.pie(
    participacion,
    labels=ciudades,
    autopct='%1.0f%%',
    startangle=90,
    colors=colors,
    explode=explode,
    shadow=True,
    textprops={'fontsize': 10, 'fontweight': 'bold'},
    wedgeprops={'edgecolor': 'black', 'linewidth': 1}
)

# Hacer el gráfico circular más visible
plt.setp(autotexts, size=12, weight="bold", color='black')
ax_pie.set_title('Participación en Ventas de Helados', fontsize=14, fontweight='bold')
ax_pie.axis('equal')  # Asegura que el pastel sea circular

# --- Tarea 6: Frecuencia acumulada ---
# Gráfico de barras para ventas
bars = ax1.bar(ciudades, ventas, color=colors, edgecolor='black', alpha=0.7)
ax1.set_title('Ventas por Ciudad con Frecuencia Acumulada', fontsize=16, pad=20, fontweight='bold')
ax1.set_ylabel('Ventas (Unidades)', fontsize=12)
ax1.set_xlabel('Ciudades', fontsize=12)
ax1.grid(axis='y', linestyle='--', alpha=0.7)

# Añadir valores en las barras
for bar in bars:
    height = bar.get_height()
    ax1.annotate(f'{height:,}'.replace(',', '.'),
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom',
                fontsize=10)

# Crear segundo eje para la frecuencia acumulada
ax2 = ax1.twinx()
ax2.plot(ciudades, porcentaje_acumulado, 
         color='red', 
         marker='o', 
         markersize=8,
         linewidth=3,
         label='Frecuencia Acumulada')
ax2.set_ylim(0, 110)
ax2.yaxis.set_major_formatter(PercentFormatter())
ax2.set_ylabel('Porcentaje Acumulado', fontsize=12, color='red')
ax2.tick_params(axis='y', labelcolor='red')

# Añadir valores en la línea de acumulación
for i, (ciudad, valor) in enumerate(zip(ciudades, porcentaje_acumulado)):
    ax2.annotate(f'{valor:.1f}%', 
                 xy=(i, valor),
                 xytext=(0, 10),
                 textcoords="offset points",
                 ha='center',
                 color='red',
                 fontsize=10,
                 fontweight='bold',
                 bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="red", alpha=0.7))

# Añadir leyenda
ax2.legend(loc='upper left', fontsize=12)

# Mostrar el total
fig.text(0.95, 0.95, f'Total Ventas: {total_ventas:,}'.replace(',', '.'), 
         fontsize=12, ha='right', va='top',
         bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", lw=1))

plt.tight_layout()
plt.savefig('ventas_helados_completo.png', dpi=300)
plt.show()