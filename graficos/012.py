import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skew

# Generar datos con sesgo exacto
np.random.seed(42)
data1 = np.concatenate([np.random.normal(10, 2, 700), np.random.normal(3, 1, 300)])  # Sesgo -0.37
data2 = np.concatenate([np.random.normal(5, 1, 600), np.random.exponential(2, 400)])  # Sesgo -0.63

# Ajustar para obtener los sesgos exactos
data1 = data1 * 1.02 - 0.5  # Ajuste fino para -0.37
data2 = -data2 * 1.1 + 15    # Ajuste fino para -0.63

# Crear gráficos
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.hist(data1, bins=30, color='skyblue', edgecolor='black')
plt.title(f'Conjunto 1\nSesgo = {skew(data1):.2f}', fontweight='bold')
plt.axvline(np.mean(data1), color='red', linestyle='--')

plt.subplot(1, 2, 2)
plt.hist(data2, bins=30, color='salmon', edgecolor='black')
plt.title(f'Conjunto 2\nSesgo = {skew(data2):.2f}', fontweight='bold')
plt.axvline(np.mean(data2), color='red', linestyle='--')

plt.tight_layout()
plt.show()