# Importamos las librerías necesarias
import matplotlib.pyplot as plt
import numpy as np

# Creamos una figura con un tamaño específico
plt.figure(figsize=(8, 7))

# Definimos los parámetros t, x e y para la ecuación del corazón
# t: Array de valores que va desde 0 a 2π, con 1000 puntos en total.
t = np.linspace(0, 2 * np.pi, 1000)

# x e y: Ecuaciones paramétricas que definen la forma de un corazón.
x = 16 * np.sin(t)**3
y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)

# Graficamos la función con los valores de x e y, definiendo el color de la línea.
plt.plot(x, y, color='red')

# Ajustes estéticos para la gráfica
plt.title('Gráfica')  
plt.axis('equal')  # Asegura que los aspectos de la gráfica sean iguales en ambos ejes.
plt.axis('off')  # Oculta los ejes para una mejor visualización del corazón.

# Mostramos la gráfica
plt.show()