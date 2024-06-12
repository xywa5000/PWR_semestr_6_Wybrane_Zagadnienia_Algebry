import numpy as np
import matplotlib.pyplot as plt

def f(x, y, a):
    return x**3 + x*y**2 - (1 + a)*x**2 - y**2

# Zakres wartości x i y
x = np.linspace(-5, 5, 400)
y = np.linspace(-5, 5, 400)
X, Y = np.meshgrid(x, y)

# Wartości parametru a
a_values = [-4, -2, 0, 1, 2, 3]

# Wykresy dla każdej krzywej
fig, axs = plt.subplots(2, 3, figsize=(10, 8))

for i, a in enumerate(a_values):
    Z = f(X, Y, a)
    ax = axs[i // 3, i % 3]
    contour = ax.contour(X, Y, Z, levels=[0], colors='blue')
    ax.set_title(f'$a = {a}$')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.grid(True)

plt.tight_layout()
plt.show()

# Wszystkie krzywe na jednym wykresie
plt.figure(figsize=(6, 6))
colors = plt.cm.viridis(np.linspace(0, 1, len(a_values)))

for i, a in enumerate(a_values):
    Z = f(X, Y, a)
    plt.contour(X, Y, Z, levels=[0], colors=[colors[i]], label=f'a = {a}')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Contours of $f(x, y, a) = x^3 + x y^2 - (1 + a) x^2 - y^2$')
plt.grid(True)
plt.axis('equal')
plt.tight_layout()
plt.show()
