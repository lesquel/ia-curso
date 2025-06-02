import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator

# Generar datos de ejemplo que sigan una distribución normal
np.random.seed(42)  # Para resultados reproducibles
data = np.concatenate([
    np.random.normal(loc=20, scale=5, size=150),
    np.random.normal(loc=50, scale=10, size=250),
    np.random.normal(loc=80, scale=7, size=200)
])

# Definir los intervalos de clase (bins) según la descripción
bins = [1, 21, 41, 61, 81, 101]

# Configurar el gráfico
plt.figure(figsize=(12, 8))
ax = plt.gca()

# Crear el histograma
n, bins, patches = plt.hist(data, 
                           bins=bins, 
                           color='#1f77b4', 
                           edgecolor='black', 
                           alpha=0.85)

# Personalizar el gráfico
plt.title('Histograma de Distribución de Datos', fontsize=16, pad=20)
plt.xlabel('Intervalos de Clase (X)', fontsize=12, labelpad=15)
plt.ylabel('Frecuencia Absoluta (Y)', fontsize=12, labelpad=15)

# Añadir etiquetas a los intervalos
interval_labels = ['[1, 21]', '[21, 41]', '[41, 61]', '[61, 81]', '[81, 101]']
plt.xticks([(bins[i] + bins[i+1])/2 for i in range(len(bins)-1)], 
           interval_labels, 
           fontsize=11)

# Añadir valores de frecuencia en cada barra
for i in range(len(patches)):
    plt.annotate(f'Freq: {int(n[i])}', 
                xy=((bins[i] + bins[i+1])/2, n[i]), 
                xytext=(0, 5), 
                textcoords="offset points", 
                ha='center', 
                va='bottom',
                fontsize=10,
                fontweight='bold')

# Líneas de guía y grid
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.axhline(y=0, color='k', linewidth=0.8)  # Línea base en y=0

# Añadir flechas y anotaciones explicativas
plt.annotate('Eje Vertical (Y):\nFrecuencia Absoluta', 
             xy=(0.02, 0.95), 
             xycoords='axes fraction',
             fontsize=11,
             bbox=dict(boxstyle="round,pad=0.3", fc="yellow", alpha=0.2))

plt.annotate('Eje Horizontal (X):\nIntervalos de Clase', 
             xy=(0.4, 0.05), 
             xycoords='axes fraction',
             fontsize=11,
             bbox=dict(boxstyle="round,pad=0.3", fc="yellow", alpha=0.2))

# Añadir flecha para eje Y
ax.annotate('',
            xy=(0.02, 0.85), 
            xytext=(0.02, 0.05), 
            xycoords='axes fraction',
            arrowprops=dict(arrowstyle="->", color="red"))

# Añadir flecha para eje X
ax.annotate('',
            xy=(0.15, 0.05), 
            xytext=(0.95, 0.05), 
            xycoords='axes fraction',
            arrowprops=dict(arrowstyle="->", color="red"))

# Ajustar límites y formato
plt.ylim(0, max(n)*1.15)
ax.yaxis.set_major_locator(MaxNLocator(integer=True))  # Solo enteros en el eje Y

# Información adicional
plt.figtext(0.5, 0.01, 
           'Cómo se construye un histograma:\n'
           '1. Dividir el rango de datos en intervalos de clase (bins)\n'
           '2. Contar la frecuencia de datos en cada intervalo\n'
           '3. Representar las frecuencias como barras contiguas', 
           ha='center', 
           fontsize=11, 
           bbox=dict(facecolor='lightgray', alpha=0.2, boxstyle='round,pad=1'))

plt.tight_layout()
plt.subplots_adjust(bottom=0.15)  # Espacio para la nota inferior
plt.savefig('histograma_explicativo.png', dpi=300)
plt.show()