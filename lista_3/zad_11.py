import numpy as np
import matplotlib.pyplot as plt

# Parametryczne równania generujące okrąg
def x(t):
    return (1 - t**2) / (1 + t**2)

def y(t):
    return 2 * t / (1 + t**2)

# Implicityzacja
def circle_eq(theta):
    return np.cos(theta/2)

# Zakres parametru theta
theta_vals = np.linspace(0, 2*np.pi, 1000)

# Parametr t
t_vals = np.tan(theta_vals / 2)

# Wykres parametryczny okręgu
plt.figure(figsize=(8, 8))
plt.plot(x(t_vals), y(t_vals), label='Parametryczny okrąg')

# Wykres implicityznej rozmaitości (okrąg jednostkowy)
plt.plot(circle_eq(theta_vals), circle_eq(theta_vals) * np.sin(theta_vals), label='Okrąg jednostkowy', linestyle='--')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Porównanie parametrycznego okręgu i okręgu jednostkowego')
plt.axis('equal')
plt.legend()
plt.grid(True)
plt.show()
