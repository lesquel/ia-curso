import matplotlib.pyplot as plt
import numpy as np

# Generar datos aleatorios simulados (100 estudiantes)
np.random.seed(42)  # Para reproducibilidad
lectura = np.random.randint(200, 800, 100)
escritura = np.random.normal(loc=0.7*lectura + 50, scale=80, size=100)
escritura = np.clip(escritura, 200, 800)  # Asegurar que estén dentro del rango

# Crear el diagrama de dispersión
plt.figure(figsize=(10, 6))
plt.scatter(lectura, escritura, color='blue', alpha=0.6, edgecolors='w', s=80)

# Personalización del gráfico
plt.title('Relación entre Puntuaciones de Lectura y Escritura', pad=20)
plt.xlabel('Puntuación en Lectura (200-800)')
plt.ylabel('Puntuación en Escritura (200-800)')
plt.xlim(200, 800)
plt.ylim(200, 800)

# Añadir línea de tendencia
z = np.polyfit(lectura, escritura, 1)
p = np.poly1d(z)
plt.plot(lectura, p(lectura), "r--", linewidth=1.5, 
         label=f'Tendencia: y = {z[0]:.2f}x + {z[1]:.2f}')

# Añadir cuadrícula y leyenda
plt.grid(True, linestyle='--', alpha=0.3)
plt.legend()

# Resaltar la zona de concentración central (400-600)
plt.axvspan(400, 600, color='yellow', alpha=0.1, label='Zona de concentración')
plt.axhspan(400, 600, color='yellow', alpha=0.1)

plt.tight_layout()
plt.show()