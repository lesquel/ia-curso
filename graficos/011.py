import numpy as np
import matplotlib.pyplot as plt

# Configuración general
plt.figure(figsize=(15, 5))

# --- 1. Sesgo Positivo (cola a la derecha) ---
plt.subplot(1, 3, 1)
data_positivo = np.random.exponential(scale=2, size=1000)  # Datos con sesgo positivo
plt.hist(data_positivo, bins=30, color='skyblue', edgecolor='black', alpha=0.7)
plt.title('Sesgo Positivo', fontweight='bold')
plt.xlabel('Valores → Concentración a la izquierda')
plt.ylabel('Frecuencia')
plt.grid(axis='y', alpha=0.3)
plt.axvline(np.mean(data_positivo), color='red', linestyle='--', label='Media')

# --- 2. Cero Sesgo (distribución simétrica) ---
plt.subplot(1, 3, 2)
data_cero = np.random.normal(loc=0, scale=1, size=1000)  # Datos simétricos
plt.hist(data_cero, bins=30, color='lightgreen', edgecolor='black', alpha=0.7)
plt.title('Cero Sesgo (Simétrico)', fontweight='bold')
plt.xlabel('Valores → Frecuencias idénticas en ambos lados')
plt.grid(axis='y', alpha=0.3)
plt.axvline(np.mean(data_cero), color='red', linestyle='--', label='Media')

# --- 3. Sesgo Negativo (cola a la izquierda) ---
plt.subplot(1, 3, 3)
data_negativo = -np.random.exponential(scale=2, size=1000)  # Datos con sesgo negativo
plt.hist(data_negativo, bins=30, color='salmon', edgecolor='black', alpha=0.7)
plt.title('Sesgo Negativo', fontweight='bold')
plt.xlabel('Valores → Concentración a la derecha')
plt.grid(axis='y', alpha=0.3)
plt.axvline(np.mean(data_negativo), color='red', linestyle='--', label='Media')

plt.tight_layout()
plt.show()