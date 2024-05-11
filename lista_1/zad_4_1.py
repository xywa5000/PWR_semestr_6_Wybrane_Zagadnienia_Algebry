import numpy as np
import matplotlib.pyplot as plt

# Definicja funkcji r(θ)
def r(theta):
    return np.sin(2 * theta)

# Tworzenie wartości kąta theta od 0 do 2*pi
theta = np.linspace(0, 2*np.pi, 1000)

# Obliczanie współrzędnych (x, y) z współrzędnych biegunowych
x = r(theta) * np.cos(theta)
y = r(theta) * np.sin(theta)

# Rysowanie krzywej czterolistnej
plt.figure(figsize=(6,6))
plt.plot(x, y, label='Krzywa czterolistna', color='blue')
plt.title('Krzywa czterolistna')
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')
plt.grid(True)
plt.legend()
plt.show()
