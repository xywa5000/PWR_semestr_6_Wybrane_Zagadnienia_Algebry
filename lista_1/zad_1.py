import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from python_lib.GaussianNumber import GaussianNumber

# Przykładowe użycie funkcji
a = GaussianNumber(2, -3)
b = GaussianNumber(3, 5)
x = GaussianNumber(3, 4)
y = GaussianNumber(1, 3)

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
print("\tc = (3 + 4i; 1 + 3i)")
print(f"\tc = {x.gcd(y)}")
print("\td = (3 + 4i) * (1 + 3i)")
print(f"\td = {x.lcm(y)}")
