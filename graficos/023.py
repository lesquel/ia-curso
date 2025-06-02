import matplotlib.pyplot as plt
import numpy as np

# Datos basados en la imagen
paises = ['EE.UU.', 'Canada', 'Russia', 'Belgium', 'UK', 'Denmark', 'Germany', 'Mexico']
valores_barras = [180, 8, 6, 4, 3, 2, 2, 1]  # Valores aproximados de las barras
porcentajes = [91, 94, 96, 97, 98, 99, 99, 100]  # Porcentajes acumulados

# Crear figura con dos ejes Y
fig, ax1 = plt.subplots(figsize=(14, 8))

# Crear las barras (eje Y izquierdo)
bars = ax1.bar(paises, valores_barras, 
               color='navy', 
               alpha=0.8,
               edgecolor='black',
               linewidth=0.5)

# Configurar el primer eje Y (barras)
ax1.set_ylabel('Valores', fontsize=12, color='black')
ax1.set_ylim(0, 200)
ax1.set_yticks(range(0, 201, 20))
ax1.tick_params(axis='y', labelcolor='black')

# Crear el segundo eje Y para los porcentajes
ax2 = ax1.twinx()

# Crear la línea de porcentajes
line = ax2.plot(paises, porcentajes, 
                color='darkorange', 
                marker='o', 
                linewidth=2, 
                markersize=6,
                markerfacecolor='darkorange',
                markeredgecolor='red',
                markeredgewidth=1)

# Configurar el segundo eje Y (línea)
ax2.set_ylabel('Porcentaje (%)', fontsize=12, color='darkorange')
ax2.set_ylim(0, 100)
ax2.set_yticks(range(0, 101, 10))
ax2.tick_params(axis='y', labelcolor='darkorange')

# Añadir etiquetas de porcentaje encima de cada punto
for i, (pais, porcentaje) in enumerate(zip(paises, porcentajes)):
    ax2.annotate(f'{porcentaje}%', 
                xy=(i, porcentaje), 
                xytext=(0, 10), 
                textcoords='offset points',
                ha='center', 
                va='bottom',
                fontsize=10,
                color='darkorange',
                fontweight='bold')

# Configurar título y etiquetas
ax1.set_title('Task 7', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Países', fontsize=12)

# Rotar las etiquetas del eje X para mejor legibilidad
plt.setp(ax1.get_xticklabels(), rotation=45, ha='right')

# Añadir cuadrícula solo para el eje principal
ax1.grid(True, axis='y', alpha=0.3, linestyle='-', linewidth=0.5)
ax1.set_axisbelow(True)

# Resaltar la barra más alta (EE.UU.)
bars[0].set_color('darkblue')
bars[0].set_alpha(0.9)

# Configurar el fondo
ax1.set_facecolor('white')
fig.patch.set_facecolor('white')

# Ajustar el layout
plt.tight_layout()

# Mostrar el gráfico
plt.show()

# Imprimir estadísticas
print("Gráfico 'Task 7' generado exitosamente!")
print(f"Países: {len(paises)}")
print(f"Valor máximo: {max(valores_barras)}")
print(f"Porcentaje final: {porcentajes[-1]}%")
print("\nDatos por país:")
for pais, valor, pct in zip(paises, valores_barras, porcentajes):
    print(f"{pais:8}: {valor:3} | {pct}%")
