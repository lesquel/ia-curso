import matplotlib.pyplot as plt
import numpy as np

# Datos basados en la imagen
categorias = ['Categoría 1', 'Categoría 2', 'Categoría 3', 'Categoría 4', 'Categoría 5']
valores = [70, 125, 50, 25, 5]  # Valores aproximados basados en la imagen

# Etiquetas con formato de dinero (como se ve en la imagen)
etiquetas_dinero = [
    '($217,564.07...)',
    '($217,564.07...)', 
    '($217,564.07...)',
    '($417,564.07...)',
    '($517,564.07...)'
]

# Crear el gráfico
fig, ax = plt.subplots(figsize=(12, 8))

# Crear las barras
bars = ax.bar(categorias, valores, 
              color='navy', 
              alpha=0.8,
              edgecolor='black',
              linewidth=0.5)

# Configurar el título
ax.set_title('Tarea 3', fontsize=16, fontweight='bold', pad=20)

# Configurar los ejes
ax.set_ylabel('Valores', fontsize=12)
ax.set_ylim(0, max(valores) * 1.1)

# Añadir las etiquetas de dinero debajo de cada barra
for i, (bar, etiqueta) in enumerate(zip(bars, etiquetas_dinero)):
    # Posición de la etiqueta debajo de cada barra
    ax.text(bar.get_x() + bar.get_width()/2, -8, 
            etiqueta, 
            ha='center', va='top', 
            fontsize=9, 
            rotation=0)

# Configurar la cuadrícula
ax.grid(True, axis='y', alpha=0.3, linestyle='-', linewidth=0.5)
ax.set_axisbelow(True)

# Establecer los ticks del eje Y
ax.set_yticks(range(0, int(max(valores)) + 20, 20))

# Ajustar márgenes para que las etiquetas sean visibles
plt.subplots_adjust(bottom=0.15)

# Remover las etiquetas del eje X por defecto para usar solo las etiquetas de dinero
ax.set_xticklabels([''] * len(categorias))

# Añadir valores encima de cada barra
for bar, valor in zip(bars, valores):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 1,
            f'{valor}',
            ha='center', va='bottom', fontsize=10, fontweight='bold')

# Configurar el fondo
ax.set_facecolor('white')
fig.patch.set_facecolor('white')

# Mostrar el gráfico
plt.tight_layout()
plt.show()

# Imprimir información del gráfico
print("Gráfico 'Tarea 3' generado exitosamente!")
print(f"Valores: {valores}")
print(f"Total: {sum(valores)}")
print(f"Promedio: {np.mean(valores):.1f}")
