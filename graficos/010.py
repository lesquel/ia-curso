import matplotlib.pyplot as plt
import numpy as np

# Datos que coinciden con el patrón de la imagen
# Apple: rango aproximado de 100 a 170
# Alphabet: rango aproximado de 700 a 1000
apple_prices = [
    108, 110, 112, 115, 116, 118, 120, 122, 125, 128,
    130, 132, 135, 138, 140, 142, 145, 148, 150, 152,
    155, 158, 160, 162, 165, 168, 170, 172, 175, 178
]

alphabet_prices = [
    780, 785, 790, 800, 810, 820, 825, 830, 840, 850,
    860, 865, 870, 880, 885, 890, 895, 900, 905, 910,
    920, 925, 930, 935, 940, 945, 950, 955, 960, 970
]

# Crear el gráfico con el tamaño y estilo exacto
plt.figure(figsize=(10, 7))

# Crear el gráfico de dispersión con puntos azules
plt.scatter(apple_prices, alphabet_prices, alpha=0.8, s=60, color='darkblue', edgecolors='navy', linewidth=0.5)

# Configurar título
plt.title('Apple - Google', fontsize=12, pad=15, loc='left')

# Configurar etiquetas de los ejes
plt.xlabel('Apple', fontsize=11)
plt.ylabel('Alphabet (Google)', fontsize=11)

# Configurar los límites de los ejes para que coincidan exactamente
plt.xlim(100, 180)
plt.ylim(700, 1100)

# Configurar los ticks de los ejes
plt.xticks(range(100, 181, 10))
plt.yticks(range(700, 1101, 50))

# Agregar grilla como en la imagen original
plt.grid(True, alpha=0.4, linestyle='-', linewidth=0.5, color='gray')

# Ajustar el layout para que se vea limpio
plt.tight_layout()

# Agregar un borde alrededor del gráfico
ax = plt.gca()
ax.spines['top'].set_visible(True)
ax.spines['right'].set_visible(True)
ax.spines['bottom'].set_visible(True)
ax.spines['left'].set_visible(True)

# Mostrar el gráfico
plt.show()

# Estadísticas
correlation = np.corrcoef(apple_prices, alphabet_prices)[0,1]
print(f"Correlación entre Apple y Alphabet: {correlation:.4f}")
print(f"Rango Apple: ${min(apple_prices)} - ${max(apple_prices)}")
print(f"Rango Alphabet: ${min(alphabet_prices)} - ${max(alphabet_prices)}")