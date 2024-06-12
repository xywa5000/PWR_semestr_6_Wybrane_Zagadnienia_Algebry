import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math

# Funkcje definiujące rozmaitości algebraiczne
def variety_1(x, y):
    return x**2 + y**2

def variety_2(x, y):
    z = np.sqrt(x**2 + y**2)
    return z, -z

def variety_3(x, y):
    return x**2 - y**2

def variety_4(x, y):
    type1 = (x == -y)
    type2 = (x == 0) & (y == 0)
    return type1, type2

# Tworzenie siatki punktów dla x i y
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)

# Obliczanie wartości z dla każdej rozmaitości
z1 = variety_1(x, y)
z2_pos, z2_neg = variety_2(x, y)
z3 = variety_3(x, y)
z4_type1, z4_type2 = variety_4(x, y)

# Tworzenie figur i osi 3D
fig = plt.figure(figsize=(12, 10))

# Rysowanie rozmaitości 1
ax1 = fig.add_subplot(221, projection='3d')
ax1.plot_surface(x, y, z1, cmap='viridis')
ax1.set_title('V(z - x^2 - y^2)')

# Rysowanie rozmaitości 2
ax2 = fig.add_subplot(222, projection='3d')
ax2.plot_surface(x, y, z2_pos, cmap='plasma')
ax2.plot_surface(x, y, z2_neg, cmap='plasma')
ax2.set_title('V(z^2 - x^2 - y^2)')

# Rysowanie rozmaitości 3
ax3 = fig.add_subplot(223, projection='3d')
ax3.plot_surface(x, y, z3, cmap='plasma')
ax3.set_title('V(z - x^2 + y^2)')

# Rysowanie rozmaitości 4
ax4 = fig.add_subplot(224, projection='3d')
ax4.plot_surface(x, y, z4_type1, cmap='plasma')
ax4.plot_surface(x, y, z4_type2, cmap='viridis')
ax4.set_title('V(xz + yz)')

plt.show()
