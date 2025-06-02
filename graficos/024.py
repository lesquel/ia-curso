import numpy as np
import matplotlib.pyplot as plt

# Datos de ejemplo (simulando los datos distribuidos aproximadamente normalmente)
np.random.seed(42)
datos_originales = np.random.normal(loc=73.95, scale=15, size=200)

# Cálculos solicitados
media = np.mean(datos_originales)
desv_est = np.std(datos_originales)

# Estandarización de los datos
datos_estandarizados = (datos_originales - media) / desv_est

# Creación de los gráficos
plt.figure(figsize=(15, 5))

# Gráfico 1: Datos originales
plt.subplot(1, 3, 1)
plt.hist(datos_originales, bins=20, color='skyblue', edgecolor='black')
plt.axvline(media, color='red', linestyle='dashed', linewidth=1, label=f'Media: {media:.2f}')
plt.title('Datos Originales')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.legend()
plt.grid(True, alpha=0.3)

# Gráfico 2: Datos estandarizados
plt.subplot(1, 3, 2)
plt.hist(datos_estandarizados, bins=20, color='lightgreen', edgecolor='black')
plt.axvline(0, color='red', linestyle='dashed', linewidth=1, label='Media: 0.00')
plt.title('Datos Estandarizados')
plt.xlabel('Valores estandarizados')
plt.ylabel('Frecuencia')
plt.legend()
plt.grid(True, alpha=0.3)

# Gráfico 3: Comparación de distribuciones
plt.subplot(1, 3, 3)
plt.hist(datos_originales, bins=20, alpha=0.5, label='Originales', color='skyblue')
plt.hist(datos_estandarizados, bins=20, alpha=0.5, label='Estandarizados', color='lightgreen')
plt.title('Comparación de Distribuciones')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Mostrar los valores calculados
print(f"Media de los datos originales: {media:.2f}")
print(f"Desviación estándar de los datos originales: {desv_est:.2f}")
print("\nNota: Los datos estandarizados tienen media ≈ 0 y desviación estándar ≈ 1")