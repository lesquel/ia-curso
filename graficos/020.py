import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Generar datos de ejemplo similares al patrón de la imagen
# Puedes reemplazar estos datos con tus datos reales
np.random.seed(42)  # Para reproducibilidad

# Crear etiquetas para el eje x (ajusta según tus datos)
n_puntos = 80  # Número aproximado de barras que se ven en la imagen
categorias = [f'Cat_{i+1:02d}' for i in range(n_puntos)]

# Generar valores que simulan el patrón de la imagen
# Con picos al inicio y valores más bajos hacia el final
valores = []
for i in range(n_puntos):
    if i < 25:  # Primeros valores con más variabilidad y picos más altos
        valor = np.random.exponential(3) + np.random.normal(2, 1)
    elif i < 45:  # Valores medios
        valor = np.random.exponential(1.5) + np.random.normal(1, 0.5)
    else:  # Valores finales más bajos
        valor = np.random.exponential(0.8) + np.random.normal(0.5, 0.3)
    
    valores.append(max(0, valor))  # Asegurar valores no negativos

# Crear el gráfico
plt.figure(figsize=(16, 8))
bars = plt.bar(range(len(categorias)), valores, 
               color='steelblue', 
               alpha=0.7,
               edgecolor='navy',
               linewidth=0.5)

# Personalizar el gráfico
plt.title('Tarea 2', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Categorías', fontsize=12)
plt.ylabel('Valores', fontsize=12)

# Configurar el eje x
plt.xticks(range(len(categorias)), categorias, 
           rotation=45, ha='right', fontsize=8)

# Configurar el eje y
plt.ylabel('Valores', fontsize=12)
max_val = max(valores)
plt.ylim(0, max_val * 1.1)

# Añadir líneas de cuadrícula
plt.grid(True, axis='y', alpha=0.3, linestyle='-', linewidth=0.5)
plt.grid(True, axis='x', alpha=0.2, linestyle='-', linewidth=0.3)

# Ajustar el layout para que las etiquetas no se corten
plt.tight_layout()

# Opcional: Resaltar las barras más altas
max_indices = np.argsort(valores)[-5:]  # Los 5 valores más altos
for idx in max_indices:
    bars[idx].set_color('darkblue')
    bars[idx].set_alpha(0.9)

# Mostrar el gráfico
plt.show()

# Opcional: Guardar el gráfico
# plt.savefig('tarea2_grafico.png', dpi=300, bbox_inches='tight')

print("Gráfico generado exitosamente!")
print(f"Número total de categorías: {len(categorias)}")
print(f"Valor máximo: {max(valores):.2f}")
print(f"Valor promedio: {np.mean(valores):.2f}")
