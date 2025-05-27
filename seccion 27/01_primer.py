# import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
data = pd.read_csv('./data.csv')
"""
print(data) # imprime la primera linea de datos
print(data.head()) # imprime la primera 5 lineas de datos
print(data.describe()) # imprime una descripcion de datos como media, desviacion estandar, etc.
print(data.info()) # imprime informacion de datos como nombres de columnas, tipos de datos, etc.
"""

# regresion lineal y = b0 + b1*x
y = data["GPA"]
x1 = data["SAT"]

plt.scatter(x1, y) # plotea puntos de datos (x1, y)
plt.xlabel("SAT") # leyenda x
plt.ylabel("GPA") # leyenda y
plt.show() # muestra grafico


x = sm.add_constant(x1) # agrega una constante a x (es decir, x = [1, 2, 3, ...] se transforma en [1, 2, 3, ..., 1])
resul = sm.OLS(y, x).fit() # ajusta lineal y = b0 + b1*x
print(resul.summary()) # imprime resumen de ajuste





plt.scatter(x1, y) # plotea puntos de datos (x1, y)
yhat = resul.predict(x) # prediccion de y para cada valor de x ( es decir, y_hat = b0 + b1*x)
plt.plot(x1, yhat, color="red") # plotea linea de prediccion (x1, y_hat)
plt.xlabel("SAT") # leyenda x
plt.ylabel("GPA") # leyenda y
plt.show() # muestra grafico