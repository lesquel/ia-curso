import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import PercentFormatter

# Datos corregidos y verificados
marcas = ['Audi', 'Mercedes', 'BMW']
frecuencias = [124, 113, 98]  # Orden descendente para Pareto
porcentajes = [37, 34, 29]    # Porcentajes de mercado
total = sum(frecuencias)       # 335

# Configuración de estilo y colores
plt.style.use('ggplot')
colors = ['#1f77b4', '#2ca02c', '#ff7f0e']

# --------------------------------------------------------
# 1. Gráfico de barras (frecuencias absolutas)
# --------------------------------------------------------
plt.figure(figsize=(12, 6))
bars = plt.bar(marcas, frecuencias, color=colors, edgecolor='black', width=0.7)
plt.title('Distribución de Frecuencias de Ventas', fontsize=16, pad=20)
plt.ylabel('Cantidad de Vehículos', fontsize=12)
plt.ylim(0, max(frecuencias) * 1.15)

# Añadir valores en las barras
for bar in bars:
    height = bar.get_height()
    plt.annotate(f'{height}\n({height/total:.1%})', 
                 xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 3),
                 textcoords="offset points",
                 ha='center', 
                 va='bottom', 
                 fontsize=11)

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('grafico_barras.png', dpi=300)
plt.show()

# --------------------------------------------------------
# 2. Gráfico circular (participación de mercado)
# --------------------------------------------------------
plt.figure(figsize=(8, 8))
explode = (0.05, 0.02, 0.02)
plt.pie(porcentajes, 
        labels=marcas, 
        autopct='%1.1f%%', 
        startangle=90,
        colors=colors,
        explode=explode,
        shadow=True,
        textprops={'fontsize': 12},
        wedgeprops={'edgecolor': 'black', 'linewidth': 1})
plt.title('Participación de Mercado en Bonn', fontsize=16, pad=20)
plt.axis('equal')

plt.tight_layout()
plt.savefig('grafico_circular.png', dpi=300)
plt.show()

# --------------------------------------------------------
# 3. Diagrama de Pareto
# --------------------------------------------------------
# Ordenar datos de mayor a menor frecuencia
sorted_indices = np.argsort(frecuencias)[::-1]
marcas_ordenadas = [marcas[i] for i in sorted_indices]
frecuencias_ordenadas = [frecuencias[i] for i in sorted_indices]

# Calcular frecuencias acumuladas y porcentajes
acumulado = np.cumsum(frecuencias_ordenadas)
porcentaje_acumulado = acumulado / total * 100

fig, ax = plt.subplots(figsize=(12, 6))

# Gráfico de barras (frecuencias)
bars = ax.bar(marcas_ordenadas, frecuencias_ordenadas, color=colors, edgecolor='black', width=0.7)
ax.set_title('Diagrama de Pareto: Ventas por Marca', fontsize=16, pad=20)
ax.set_xlabel('Marcas', fontsize=12)
ax.set_ylabel('Ventas (Unidades)', fontsize=12)
ax.tick_params(axis='y')

# Línea de porcentaje acumulado
ax2 = ax.twinx()
ax2.plot(marcas_ordenadas, porcentaje_acumulado, 
         color='red', 
         marker='o', 
         linestyle='-', 
         linewidth=2,
         markersize=6)
ax2.set_ylim(0, 110)
ax2.yaxis.set_major_formatter(PercentFormatter())
ax2.set_ylabel('Porcentaje Acumulado', fontsize=12)

# Añadir valores
for i, bar in enumerate(bars):
    height = bar.get_height()
    ax.annotate(f'{height}', 
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', 
                va='bottom', 
                fontsize=10)
    
    ax2.annotate(f'{porcentaje_acumulado[i]:.1f}%', 
                 xy=(i, porcentaje_acumulado[i]),
                 xytext=(0, 7),
                 textcoords="offset points",
                 ha='center',
                 color='red',
                 fontsize=10,
                 weight='bold')

# Línea horizontal en 80%
ax2.axhline(y=80, color='gray', linestyle='--', alpha=0.7)
ax2.annotate('80%', xy=(0.5, 82), color='gray', fontsize=10)

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('pareto.png', dpi=300)
plt.show()