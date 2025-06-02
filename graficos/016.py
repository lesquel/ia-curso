import matplotlib.pyplot as plt

# Datos proporcionados
categorias = ['Masculino', 'Femenino', 'Empresas']
frecuencias = [108, 70, 17]
total = sum(frecuencias)
porcentajes = [f/total*100 for f in frecuencias]

# Colores personalizados
colores = ['#1f77b4', '#ff7f0e', '#2ca02c']

# Crear el gráfico circular
plt.figure(figsize=(10, 6))
wedges, texts, autotexts = plt.pie(frecuencias, 
                                  labels=categorias, 
                                  colors=colores,
                                  autopct='%1.1f%%',
                                  startangle=90,
                                  wedgeprops={'linewidth': 1, 'edgecolor': 'white'},
                                  textprops={'fontsize': 12})

# Añadir título y nota explicativa
plt.title('Distribución de Compras por Género y Empresas', pad=20, fontsize=14)
plt.text(0, -1.2, f"Total de compras: {total}\n"
                 "Nota: Las empresas no tienen género, pero se incluyen\n"
                 "para una representación completa de los datos.",
         ha='center', fontsize=10, bbox=dict(facecolor='white', alpha=0.8))

# Resaltar la porción más grande (Masculino)
wedges[0].set_edgecolor('black')
wedges[0].set_linewidth(1.5)

# Añadir leyenda
plt.legend(wedges, 
           [f'{c} - {f} compras ({p:.1f}%)' for c, f, p in zip(categorias, frecuencias, porcentajes)],
           title="Categorías",
           loc="center left",
           bbox_to_anchor=(1, 0, 0.5, 1))

plt.tight_layout()
plt.show()

# Mostrar datos en consola
print("\nResumen estadístico:")
print(f"{'Categoría':<10} {'Frecuencia':>12} {'Porcentaje':>12}")
print("-"*36)
for cat, freq, perc in zip(categorias, frecuencias, porcentajes):
    print(f"{cat:<10} {freq:>12} {perc:>10.1f}%")
print(f"{'Total':<10} {total:>12} {100:>10.1f}%")