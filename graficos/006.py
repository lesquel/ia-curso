import matplotlib.pyplot as plt
import numpy as np

# Datos de la tabla
inversores = ['Inversor A', 'Inversor B', 'Inversor C']
tipos_inversion = ['Acciones', 'Bonos', 'Inmuebles']

# Valores para cada inversor (filas: tipos, columnas: inversores)
datos = np.array([
    [96, 185, 39],   # Acciones
    [181, 3, 29],     # Bonos
    [88, 152, 142]    # Inmuebles
])

# Configuración del gráfico
fig, ax = plt.subplots(figsize=(10, 6))

# Ancho de las barras
ancho_barra = 0.25
indices = np.arange(len(inversores))

# Crear barras para cada tipo de inversión
for i, tipo in enumerate(tipos_inversion):
    desplazamiento = ancho_barra * i
    ax.bar(indices + desplazamiento, datos[i], width=ancho_barra, label=tipo)

# Personalización del gráfico
ax.set_title('Distribución de Inversiones por Tipo e Inversor', pad=20)
ax.set_xlabel('Inversores')
ax.set_ylabel('Cantidad Invertida (en unidades monetarias)')
ax.set_xticks(indices + ancho_barra)
ax.set_xticklabels(inversores)
ax.legend(title='Tipo de Inversión')
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Mostrar valores en las barras
for i in range(len(tipos_inversion)):
    for j in range(len(inversores)):
        altura = datos[i][j]
        ax.text(j + ancho_barra*i, altura + 5, str(altura), 
                ha='center', va='bottom')

plt.tight_layout()
plt.show()