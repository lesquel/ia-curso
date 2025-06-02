import matplotlib.pyplot as plt
import numpy as np

# Datos proporcionados
size = np.array([650, 785, 1200, 720, 975])  # Tamaño en ft²
price = np.array([772000, 998000, 1200000, 800000, 895000])  # Precio en $

# Calculamos las medias
mean_size = np.mean(size)
mean_price = np.mean(price)

# Creamos el gráfico de dispersión
plt.figure(figsize=(10, 6))
plt.scatter(size, price, color='blue', s=100, label='Datos')

# Añadimos líneas de medias
plt.axhline(mean_price, color='red', linestyle='--', alpha=0.5, label='Media de precio')
plt.axvline(mean_size, color='green', linestyle='--', alpha=0.5, label='Media de tamaño')

# Añadimos etiquetas y título
plt.title('Relación entre Tamaño de Casa y Precio (Covarianza Positiva)', fontsize=14)
plt.xlabel('Tamaño (ft²)', fontsize=12)
plt.ylabel('Precio ($)', fontsize=12)
plt.legend()

# Mostramos el gráfico
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()