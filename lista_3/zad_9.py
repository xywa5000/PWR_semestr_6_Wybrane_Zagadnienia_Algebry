import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

def plot_curve(func, rng, title):
    x = np.linspace(-rng, rng, 1000)
    y = np.linspace(-rng, rng, 1000)

    X, Y = np.meshgrid(x, y)
    Z = func(X, Y)[0]

    plt.figure(figsize=(6, 6))
    plt.contour(X, Y, Z, levels=[0], colors='blue')

    for point in func(X, Y)[1]:
        plt.scatter(point[0], point[1], color='red')

    plt.title(title)
    plt.xticks(range(-9, 10))
    plt.yticks(range(-9, 10))
    plt.grid(True, which='major', linestyle='--', linewidth=0.5)
    plt.show()

def func1(x, y):
    return (x**2 + y**2 + 4*y)**2 - 16*(x**2 + y**2), [(0, 0)]

def func2(x, y):
    return 2*(x**2 + 9)*(y**2 - 16) + (x**2 - 9)**2 + (y**2 - 16)**2, [(0, sqrt(7)), (0, -sqrt(7))]

def func3(x, y):
    return 350*x**2*y**2 - 15**2*(x**2 + y**2) + 12**2*(x**4 + y**4) + 81, []

if __name__ == "__main__":
    
    plot_curve(func1, 10, '$(x^2 + y^2 + 4y)^2 - 16(x^2 + y^2) = 0$')
    plot_curve(func2, 10, '$2(x^2 + 9)(y^2 - 16) + (x^2 - 9)^2 + (y^2 - 16)^2 = 0$')
    plot_curve(func3, 1.5, '$350x^2y^2 - 15^2(x^2 + y^2) + 12^2(x^4 + y^4) + 81 = 0$')
