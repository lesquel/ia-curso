import matplotlib.pyplot as plt
import numpy as np

def draw_neural_net(ax, left, right, bottom, top, layer_sizes):
    '''
    left, right, bottom, top: boundaries of the drawing area
    layer_sizes: list containing number of nodes per layer
    '''
    v_spacing = (top - bottom)/float(max(layer_sizes))
    h_spacing = (right - left)/float(len(layer_sizes) - 1)
    
    # Nodes
    for i, layer_size in enumerate(layer_sizes):
        layer_top = v_spacing*(layer_size - 1)/2. + (top + bottom)/2.
        for j in range(layer_size):
            circle = plt.Circle((left + i*h_spacing, layer_top - j*v_spacing), 0.05,
                                color='navy', ec='white', zorder=4)
            ax.add_artist(circle)
    
    # Connections
    for i, (layer_size_a, layer_size_b) in enumerate(zip(layer_sizes[:-1], layer_sizes[1:])):
        layer_top_a = v_spacing*(layer_size_a - 1)/2. + (top + bottom)/2.
        layer_top_b = v_spacing*(layer_size_b - 1)/2. + (top + bottom)/2.
        for j in range(layer_size_a):
            for k in range(layer_size_b):
                line = plt.Line2D([left + i*h_spacing, left + (i + 1)*h_spacing],
                                  [layer_top_a - j*v_spacing, layer_top_b - k*v_spacing],
                                  c='navy', lw=0.5)
                ax.add_artist(line)

# Parámetros
fig, ax = plt.subplots(figsize=(12, 6))
ax.axis('off')
draw_neural_net(ax, 0.1, 0.9, 0.1, 0.9, [9, 9, 9, 9, 4])

# Etiquetas
input_labels = [f'$h_{{{i+1}}}$' for i in range(9)]
for i, label in enumerate(input_labels):
    ax.text(0.05, 0.88 - i*0.08, label, fontsize=10, ha='right')

output_labels = [f'Objetivo {i+1}' for i in range(4)]
for i, label in enumerate(output_labels):
    ax.text(0.93, 0.82 - i*0.18, label, fontsize=10, ha='left')

# Títulos de capas
layer_titles = ['Capa de entrada', 'Capa oculta 1', 'Capa oculta 2', 'Capa oculta 3', 'Capa de salida']
for i, title in enumerate(layer_titles):
    ax.text(0.1 + i*0.2, 0.95, title, fontsize=11, ha='center')

# Mostrar gráfico
plt.show()
