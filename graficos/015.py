import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr

# Datos proporcionados
tamanos = np.array([650, 755, 1200, 720, 975])
precios = np.array([772000, 988000, 1200000, 800000, 895000])

# Medias y desviaciones estándar
media_tamano = 866
media_precio = 933000
desv_tamano = 222
desv_precio = 173615

# Calcular covarianza y correlación
covarianza = np.cov(tamanos, precios, bias=True)[0, 1]  # bias=True para población
correlacion, _ = pearsonr(tamanos, precios)

# Crear el gráfico de dispersión
plt.figure(figsize=(10, 6))

# Diagrama de dispersión
plt.scatter(tamanos, precios, color='blue', s=100, label='Datos de casas')

# Añadir líneas de medias
plt.axhline(y=media_precio, color='red', linestyle='--', alpha=0.5, label=f'Media precio (${media_precio:,.0f})')
plt.axvline(x=media_tamano, color='green', linestyle='--', alpha=0.5, label=f'Media tamaño ({media_tamano} pies²)')

# Añadir etiquetas a los puntos
for i, (x, y) in enumerate(zip(tamanos, precios)):
    plt.annotate(f'${y/1000:.0f}K', (x, y), textcoords="offset points", xytext=(5,5), ha='left')

# Configuración del gráfico
plt.title('Relación entre Tamaño de Casa y Precio', pad=20)
plt.xlabel('Tamaño (pies cuadrados)')
plt.ylabel('Precio ($)')
plt.legend()
plt.grid(True)

# Ajustar límites del eje y para mejor visualización
plt.ylim(700000, 1300000)

# Formatear eje y para mostrar precios en formato de dólares
plt.gca().yaxis.set_major_formatter('${x:,.0f}')

# Mostrar coeficiente de correlación en el gráfico
plt.text(600, 1250000, f'Coeficiente de correlación (r) = {correlacion:.2f}', 
         bbox=dict(facecolor='white', alpha=0.8))

plt.tight_layout()
plt.show()

# Mostrar cálculos en consola
print(f"Covarianza calculada: {covarianza:,.2f}")
print(f"Coeficiente de correlación calculado: {correlacion:.2f}")