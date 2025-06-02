import matplotlib.pyplot as plt
import numpy as np

# Datos de Apple y Google (Alphabet) basados en la tabla
# Fechas aproximadas y precios de cierre
apple_prices = [
    116.05, 116.28, 115.38, 118.11, 118.92, 115.34, 
    102.04, 103.12, 108.92, 108.99, 108.70, 114.19,
    123.84, 124.68, 125.04, 124.98, 125.83, 125.75,
    126.66, 124.83, 125.86, 125.31, 124.04, 120.44,
    121.26, 120.33, 122.44, 119.36, 118.34, 115.36
]

alphabet_prices = [
    813.67, 822.41, 835.24, 826.01, 829.05, 834.44,
    843.36, 857.00, 856.02, 862.30, 869.17, 861.37,
    863.99, 866.45, 866.91, 863.35, 863.35, 862.19,
    863.80, 859.93, 863.95, 862.08, 861.35, 856.33,
    858.71, 849.23, 849.21, 829.80, 841.48, 837.02
]

# Crear el gráfico de dispersión
plt.figure(figsize=(10, 8))
plt.scatter(apple_prices, alphabet_prices, alpha=0.7, s=50, color='blue')

# Configurar el gráfico
plt.xlabel('Apple', fontsize=12)
plt.ylabel('Google', fontsize=12)
plt.title('Apple - Google', fontsize=14, pad=20, loc='left')

# Configurar los ejes para que coincidan con la imagen
plt.xlim(0, 180)
plt.ylim(0, 1200)

# Agregar grilla más visible como en la imagen original
plt.grid(True, alpha=0.6, linestyle='-', linewidth=0.5)

# Ajustar el layout
plt.tight_layout()

# Mostrar el gráfico
plt.show()

# Calcular y mostrar estadísticas básicas
correlation = np.corrcoef(apple_prices, alphabet_prices)[0,1]
print(f"Correlación entre Apple y Alphabet: {correlation:.4f}")
print(f"Precio promedio Apple: ${np.mean(apple_prices):.2f}")
print(f"Precio promedio Alphabet: ${np.mean(alphabet_prices):.2f}")