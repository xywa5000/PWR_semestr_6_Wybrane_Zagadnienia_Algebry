import numpy as np
import matplotlib.pyplot as plt

# Generowanie danych dla okręgu x^2 + y^2 = 1
x_circle = np.linspace(-1, 1, 400)
y_circle_positive = np.sqrt(1 - x_circle**2)
y_circle_negative = -np.sqrt(1 - x_circle**2)

# Generowanie danych dla krzywej parametrycznej
t = np.linspace(-100, 100, 40000)
x_parametric = (1 - t**2) / (1 + t**2)
y_parametric = (2 * t) / (1 + t**2)

# Tworzenie subplotów
fig, axs = plt.subplots(1, 2, figsize=(14, 6))

# Wykres okręgu x^2 + y^2 = 1
axs[0].plot(x_circle, y_circle_positive, 'blue')
axs[0].plot(x_circle, y_circle_negative, 'blue')
axs[0].set_xlabel('x')
axs[0].set_ylabel('y')
axs[0].set_title('$y = \sqrt{1 - x^2}$')
axs[0].grid(True)
axs[0].axis('equal')

# Wykres krzywej parametrycznej
axs[1].plot(x_parametric, y_parametric, 'red')
axs[1].set_xlabel('x')
axs[1].set_ylabel('y')
axs[1].set_title('$x(t) = \\frac{1-t^2}{1+t^2}, y(t) = \\frac{2t}{1+t^2}$')
axs[1].grid(True)
axs[1].axis('equal')

plt.tight_layout()
plt.show()
