import numpy as np
import matplotlib.pyplot as plt


def zadanie_4_1():
    # Definicja funkcji r(θ)
    def r(theta, param):
        return np.sin(param * theta)

    # Tworzenie wartości kąta theta od 0 do 2*pi
    theta = np.linspace(0, 2*np.pi, 1000)
    # Zmienny parametr z zadania
    param = 2

    # Obliczanie współrzędnych (x, y) z współrzędnych biegunowych
    x = r(theta, param) * np.cos(theta)
    y = r(theta, param) * np.sin(theta)

    # Rysowanie krzywej czterolistnej
    plt.figure(figsize=(6, 6))
    plt.plot(x, y, label=f'Krzywa parametr = {param}', color='blue')
    plt.title('Zadanie Lab 4.')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axis('equal')
    plt.grid(True)
    plt.legend()
    plt.show()


def zadanie_4_2():
    x = np.linspace(-1, 1, 1000)
    y = np.linspace(-1, 1, 1000)

    x, y = np.meshgrid(x, y)

    plt.figure(figsize=(6, 6))
    plt.contour(x, y, (x**2 + y**2)**3 - 4*x**2*y**2, levels=[0], colors='blue')
    plt.title('$(x^2 + y^2)^3 = 4x^2y^2$')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()


zadanie_4_1()
zadanie_4_2()
