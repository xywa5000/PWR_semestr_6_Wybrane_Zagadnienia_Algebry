import numpy as np
import matplotlib.pyplot as plt

# Definicja funkcji r(θ)
def r(theta, param):
    return np.sin(param * theta)

# Tworzenie wartości kąta theta od 0 do 2*pi
theta = np.linspace(0, 2*np.pi, 1000)
# Zmienny parametr z zadania
param = 7

# Obliczanie współrzędnych (x, y) z współrzędnych biegunowych
x = r(theta, param) * np.cos(theta)
y = r(theta, param) * np.sin(theta)

# Rysowanie krzywej czterolistnej
plt.figure(figsize=(6,6))
plt.plot(x, y, label=f'Krzywa parametr = {param}', color='blue')
plt.title('Zadanie Lab 4.')
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')
plt.grid(True)
plt.legend()
plt.show()
