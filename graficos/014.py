import matplotlib.pyplot as plt
import numpy as np

# Datos proporcionados
lectura = np.array([344, 383, 611, 713, 589])
escritura = np.array([378, 249, 508, 719, 509])

# Medias calculadas
media_lectura = 517
media_escritura = 490

# Crear figura con dos subtramas
plt.figure(figsize=(12, 6))

# Primer gráfico: Diagrama de dispersión básico
plt.subplot(1, 2, 1)
plt.scatter(lectura, escritura, color='blue')
plt.title('Diagrama de Dispersión: Lectura vs Escritura')
plt.xlabel('Puntuación de Lectura')
plt.ylabel('Puntuación de Escritura')
plt.grid(True)

# Segundo gráfico: Diagrama con líneas de medias y anotaciones
plt.subplot(1, 2, 2)
plt.scatter(lectura, escritura, color='blue')

# Añadir líneas de medias
plt.axhline(y=media_escritura, color='red', linestyle='--', label=f'Media Escritura (490)')
plt.axvline(x=media_lectura, color='green', linestyle='--', label=f'Media Lectura (517)')

# Añadir etiquetas a los puntos
for i, (x, y) in enumerate(zip(lectura, escritura)):
    plt.annotate(f'({x}, {y})', (x, y), textcoords="offset points", xytext=(0,10), ha='center')

plt.title('Diagrama con Medias y Anotaciones')
plt.xlabel('Puntuación de Lectura')
plt.ylabel('Puntuación de Escritura')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

# Mostrar cálculo de covarianza
covarianza = np.cov(lectura, escritura, bias=True)[0, 1]  # bias=True para población
print(f"Covarianza calculada: {covarianza:.2f}")