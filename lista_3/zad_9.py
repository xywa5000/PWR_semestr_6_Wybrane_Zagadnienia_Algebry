import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Definiowanie zmiennych
x, y = sp.symbols('x y')

# Definiowanie równań krzywych
curve1 = (x**2 + y**2 + 4*y**2) - 16 * (x**2 * y**2)
curve2 = 2 * (x**2 + 9) * (y**2 - 16) + (x**2 - 9) ** 2 + (y ** 2  - 16) ** 2
curve3 = 350*x**2 * y**2 - 152 * (x**2 + y**2) + 122 * (x**4 + y**4)

# Obliczanie punktów osobliwych (gdzie pochodne cząstkowe są równe zeru)
singular_points_curve1 = sp.solve([sp.diff(curve1, x), sp.diff(curve1, y)], (x, y))
singular_points_curve2 = sp.solve([sp.diff(curve2, x), sp.diff(curve2, y)], (x, y))
singular_points_curve3 = sp.solve([sp.diff(curve3, x), sp.diff(curve3, y)], (x, y))

# Tworzenie funkcji do rysowania wykresów
def plot_curve(eq, title):
    p = sp.plot_implicit(sp.Eq(eq, 0), (x, -10, 10), (y, -10, 10), show=False)
    p.title = title
    p.xlabel = 'x'
    p.ylabel = 'y'
    p.show()

plot_curve(curve1, 'Curve 1: $x^2 + y^2 + 4y^2 - 16x^2 * y^2 = 0$')
plot_curve(curve2, 'Curve 2: $2x^2 + 9y^2 - 16 + x^2 - 9y^2 + y^2 - 16 = 0$')
plot_curve(curve3, 'Curve 3: $350x^2y^2 - 152(x^2 + y^2) + 122(x^4 + y^4) = 0$')

print("Singular points for Curve 1:", singular_points_curve1)
print("Singular points for Curve 2:", singular_points_curve2)
print("Singular points for Curve 3:", singular_points_curve3)

# Konwertowanie punktów osobliwych na wartości liczbowe
singular_points_curve1 = [(pt[0].evalf(), pt[1].evalf()) for pt in singular_points_curve1]
singular_points_curve2 = [(pt[0].evalf(), pt[1].evalf()) for pt in singular_points_curve2]
singular_points_curve3 = [(pt[0].evalf(), pt[1].evalf()) for pt in singular_points_curve3]

print("Singular points for Curve 1:", singular_points_curve1)
print("Singular points for Curve 2:", singular_points_curve2)
print("Singular points for Curve 3:", singular_points_curve3)
