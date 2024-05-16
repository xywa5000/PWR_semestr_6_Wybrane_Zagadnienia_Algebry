import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from python_lib.Polynomial import Polynomial

# Przykładowe użycie funkcji
a = Polynomial([6., 7., 1.])
b = Polynomial([-6., -5., 1.])
x = Polynomial([1., 0., 1.])
y = Polynomial([1., 2., 1.])

print(f"\na = {a}")
print(f"b = {b}")
print(f"x = {x}")
print(f"y = {y}\n")

print("1. true div (quotient, remainder):")
print(f"\ta // b: {a//b}")
print(f"\tb // a: {b//a}")

print("2. GCD:")
print(f"\tgcd(a, b): {a.gcd(b)}")

print("3. LCM:")
print(f"\tlcm(a, b): {a.lcm(b)}")

# Rozwiązanie punktu 4.
print("4. Ideals")
print("\tc = (x^2 + 1; x^2 + 2x + 1)")
print(f"\tc = {x.gcd(y)}")
print("\td = (x^2 + 1) * (x^2 + 2x + 1)")
print(f"\td = {x.lcm(y)}")
