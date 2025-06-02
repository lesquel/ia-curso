import matplotlib.pyplot as plt
import numpy as np

# Datos proporcionados
estados = ['California', 'Nevada', 'Oregon', 'Arizona', 'Colorado', 
           'Utah', 'Virginia', 'Wyoming', 'Kansas']
frecuencias = [119, 17, 11, 11, 11, 6, 4, 1, 1]
frec_relativas = [49, 6, 4, 4, 4, 2, 1, 0, 0]  # en porcentaje
acumulativa_total = [45, 51, 55, 55, 61, 65, 67, 67, 68]  # en porcentaje
acumulativa_eeuu = [60, 75, 81, 87, 93, 97, 99, 99, 100]  # en porcentaje

total = sum(frecuencias)
porcentajes = [f/total*100 for f in frecuencias]

# Ordenar los datos de mayor a menor frecuencia (excepto Nagoya que va al final)
orden = np.argsort(frecuencias[:-1])[::-1].tolist() + [len(frecuencias)-1]
estados_ordenados = [estados[i] for i in orden]
frecuencias_ordenadas = [frecuencias[i] for i in orden]
acumulativa_ordenada = np.cumsum([frecuencias[i] for i in orden])/total*100

# Crear figura y eje primario
fig, ax1 = plt.subplots(figsize=(14, 7))

# Barras de frecuencia absoluta
bars = ax1.bar(estados_ordenados, frecuencias_ordenadas, color='#1f77b4')
ax1.set_xlabel('Estado/Ubicación', fontsize=12)
ax1.set_ylabel('Número de Clientes', color='#1f77b4', fontsize=12)
ax1.tick_params(axis='y', labelcolor='#1f77b4')
ax1.set_title('Distribución de Clientes por Ubicación - Diagrama de Pareto', pad=20, fontsize=14)

# Rotar etiquetas del eje x
plt.xticks(rotation=45, ha='right')

# Añadir valores encima de las barras
for bar in bars:
    height = bar.get_height()
    ax1.annotate(f'{height}',
                 xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 3),  # 3 points vertical offset
                 textcoords="offset points",
                 ha='center', va='bottom')

# Eje secundario para la frecuencia acumulativa
ax2 = ax1.twinx()
line, = ax2.plot(estados_ordenados, acumulativa_ordenada, color='#ff7f0e', 
                 marker='o', ms=5, label='Frec. Acumulada (Total)')
ax2.set_ylabel('Porcentaje Acumulado', color='#ff7f0e', fontsize=12)
ax2.tick_params(axis='y', labelcolor='#ff7f0e')
ax2.set_ylim(0, 110)

# Añadir línea punteada para el 80% (principio de Pareto)
ax2.axhline(y=80, color='red', linestyle='--', alpha=0.5)
ax2.text(-0.5, 82, '80%', color='red', va='center')

# Añadir leyenda
ax2.legend([line], ['Frecuencia Acumulada (Total)'], loc='upper right')

# Añadir anotaciones explicativas
plt.figtext(0.5, -0.15, 
            "Nota:\n"
            "- '% Relativo sobre todo' incluye tanto clientes de EE.UU. como del exterior.\n"
            "- '% Acumulado sobre todo' sube hasta 100% cuando añadimos también los fuera de EE.UU.\n"
            "- '% Acumulado solo EE.UU.' ignora al 32% de clientes internacionales y llega a 100% en EE.UU.",
            ha="center", fontsize=10, bbox=dict(facecolor='white', alpha=0.8))

plt.tight_layout()
plt.show()

# Mostrar tabla resumen en consola
print("\nTabla de distribución de frecuencias:")
print(f"{'Estado':<15} {'Clientes':>10} {'% Total':>10} {'% Acum Total':>14} {'% Acum EE.UU.':>14}")
print("-"*65)
for estado, freq, rel, acu_total, acu_eeuu in zip(estados, frecuencias, frec_relativas, acumulativa_total, acumulativa_eeuu):
    print(f"{estado:<15} {freq:>10} {rel:>9}% {acu_total:>12}% {f'{acu_eeuu:.0f}%' if not np.isnan(acu_eeuu) else '':>14}")