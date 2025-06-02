import matplotlib.pyplot as plt
import numpy as np

import pandas as pd

# Crear DataFrame con los datos
data = {
    'Grupo Etario': ['18-25', '25-35', '35-45', '45-55', '55-65'],
    '% Empleados': [60, 85, 95, 97, 97],  # Asumo que 55-65 tiene el mismo % que 45-55
    '% Desempleados': [40, 15, 5, 3, 3],
    'Total': [100, 100, 100, 100, 100]
}

df = pd.DataFrame(data)
print("Tabla Cruzada de Empleo por Grupo Etario:")
print(df.to_string(index=False))

# Configuración de datos
grupos = df['Grupo Etario']
empleados = df['% Empleados']
desempleados = df['% Desempleados']
x = np.arange(len(grupos))  # ubicaciones de las etiquetas
ancho = 0.35  # ancho de las barras

# Crear figura y ejes
fig, ax = plt.subplots(figsize=(12, 6))

# Barras para empleados y desempleados
rects1 = ax.bar(x - ancho/2, empleados, ancho, label='Empleados', color='#1f77b4')
rects2 = ax.bar(x + ancho/2, desempleados, ancho, label='Desempleados', color='#ff7f0e')

# Personalización del gráfico
ax.set_title('Distribución de Empleo por Grupo Etario', pad=20, fontsize=14)
ax.set_xlabel('Grupo Etario', fontsize=12)
ax.set_ylabel('Porcentaje (%)', fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(grupos)
ax.legend(fontsize=12)
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Añadir valores en las barras
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height}%',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.tight_layout()
plt.show()