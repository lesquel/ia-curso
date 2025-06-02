import matplotlib.pyplot as plt
import numpy as np

# Generar datos que imiten exactamente el patrón del gráfico mostrado
np.random.seed(123)

# El gráfico original muestra:
# - Cluster denso entre ~$150k-$300k con Y entre 20-70
# - Puntos dispersos hasta $600k
# - Concentración mayor en Y=40-60 en la zona densa
# - Algunos puntos aislados en la parte derecha

x = []
y = []

# Cluster principal denso (zona izquierda-centro)
n_cluster = 120
x_cluster = np.random.normal(220000, 35000, n_cluster)
x_cluster = np.clip(x_cluster, 150000, 320000)

# Y values para el cluster principal - más concentrados entre 30-65
y_cluster_base = np.random.normal(45, 12, n_cluster)
y_cluster = []
for i, x_val in enumerate(x_cluster):
    # Crear la forma más densa en el centro
    if 180000 < x_val < 280000:
        y_val = np.random.normal(48, 10)
    else:
        y_val = np.random.normal(45, 15)
    
    # Algunos puntos más altos para crear la dispersión vertical
    if np.random.random() < 0.15:
        y_val += np.random.uniform(15, 25)
    
    y_cluster.append(max(20, min(75, y_val)))

x.extend(x_cluster)
y.extend(y_cluster)

# Puntos dispersos en la zona derecha
n_scattered = 60
x_scattered = np.random.uniform(320000, 580000, n_scattered)
y_scattered = []

for x_val in x_scattered:
    if x_val < 400000:
        # Transición gradual
        y_val = np.random.uniform(25, 65)
    else:
        # Más dispersos en la derecha
        y_val = np.random.uniform(20, 70)
    
    y_scattered.append(y_val)

x.extend(x_scattered)
y.extend(y_scattered)

# Algunos puntos muy dispersos para completar el patrón
n_extra = 20
x_extra = np.random.uniform(100000, 600000, n_extra)
y_extra = np.random.uniform(15, 75, n_extra)

x.extend(x_extra)
y.extend(y_extra)

x = np.array(x)
y = np.array(y)

# Crear el gráfico
plt.figure(figsize=(12, 6))
plt.scatter(x, y, color='#1f4e79', alpha=0.7, s=15, edgecolors='none')

# Configurar ejes exactamente como en la imagen
plt.xlim(50000, 650000)
plt.ylim(0, 85)

# Formatear eje X para mostrar valores en formato de dinero
x_ticks = [100000, 200000, 300000, 400000, 500000, 600000]
x_labels = ['$100,000.00', '$200,000.00', '$300,000.00', '$400,000.00', '$500,000.00', '$600,000.00']
plt.xticks(x_ticks, x_labels, rotation=45, ha='right')

# Configurar eje Y
plt.yticks(range(0, 90, 10))

# Configurar grilla y estilo para que coincida con la imagen
plt.grid(True, alpha=0.2, linestyle='-', linewidth=0.5)
plt.gca().set_axisbelow(True)

# Configurar bordes - mantener todos los bordes como en la imagen original
plt.gca().spines['top'].set_visible(True)
plt.gca().spines['right'].set_visible(True)
plt.gca().spines['left'].set_visible(True)
plt.gca().spines['bottom'].set_visible(True)

# Hacer las líneas de los bordes más sutiles
for spine in plt.gca().spines.values():
    spine.set_color('gray')
    spine.set_linewidth(0.5)

# Ajustar layout
plt.tight_layout()

# Mostrar el gráfico
plt.show()

# Opcional: Guardar el gráfico
# plt.savefig('scatter_plot.png', dpi=300, bbox_inches='tight')