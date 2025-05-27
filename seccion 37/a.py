"""
Ejercicios a resolver usando el mismo código anterior:
    1. Cambiar el número de observaciones a 100,000 y observar qué sucede.
    2. Experimentar con la tasa de aprendizaje. Valores como 0.0001, 0.001, 0.1, 1 son interesantes de observar.
    3. Cambiar la función de pérdida. Una pérdida alternativa para regresiones es la pérdida Huber.
    La pérdida Huber es más apropiada que la norma L2 cuando hay valores atípicos, ya que es menos sensible a ellos
    (en nuestro ejemplo no hay valores atípicos, pero seguramente encontrarás conjuntos con ellos en el futuro).
    La sintaxis correcta para la pérdida Huber es 'huber_loss'
    
Consejo útil: Cuando hagas cambios, no olvides VOLVER A EJECUTAR todas las celdas. Esto se puede hacer fácilmente haciendo clic en:
Kernel -> Restart & Run All
Si no lo haces, tu algoritmo mantendrá los VALORES ANTIGUOS de todos los parámetros.

Puedes usar este archivo para todos los ejercicios, o ver las soluciones de CADA UNO en los archivos separados proporcionados.
Es recomendable restaurar el archivo a su estado original después de resolver un problema para usar la lección como base de comparación.
"""

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

observaciones = 100000

# Generar variables de entrada
xs = np.random.uniform(low=-10, high=10, size=(observaciones,1))
zs = np.random.uniform(-10, 10, (observaciones,1))

# Combinar entradas
generated_inputs = np.column_stack((xs,zs))

# Generar ruido
noise = np.random.uniform(-1, 1, (observaciones,1))

# Generar objetivos
generated_targets = 2*xs - 3*zs + 5 + noise

# Guardar en archivo npz
np.savez('TF_intro', inputs=generated_inputs, targets=generated_targets)

# Cargar los datos de entrenamiento
training_data = np.load('TF_intro.npz')

input_size = 2
output_size = 1

# Definir modelo
model = tf.keras.Sequential([
    tf.keras.layers.Dense(output_size,
                          kernel_initializer=tf.random_uniform_initializer(minval=-0.1, maxval=0.1),
                          bias_initializer=tf.random_uniform_initializer(minval=-0.1, maxval=0.1))
])

# Configurar optimizador y función de pérdida
custom_optimizer = tf.keras.optimizers.SGD(learning_rate=0.001)
model.compile(optimizer=custom_optimizer, loss='huber_loss')

# Entrenar el modelo
model.fit(training_data['inputs'], training_data['targets'], epochs=100, verbose=2)

pesos = model.layers[0].get_weights()[0]
sesgo = model.layers[0].get_weights()[1]

print("Pesos:", pesos)
print("Sesgo:", sesgo)

predicciones = model.predict_on_batch(training_data['inputs']).round(1)
objetivos_reales = training_data['targets'].round(1)

print("Predicciones:", predicciones)
print("Objetivos reales:", objetivos_reales)

plt.plot(np.squeeze(predicciones), np.squeeze(objetivos_reales))
plt.xlabel('Salidas')
plt.ylabel('Objetivos')
plt.title('Comparación de predicciones vs objetivos reales')
plt.show()

"""
Nota final: Aunque en este ejemplo simple TensorFlow no parece ahorrar líneas de código,
su verdadero poder se apreciará cuando trabajemos con modelos más complejos en próximos capítulos,
donde puede ahorrarnos cientos de líneas de código.
"""