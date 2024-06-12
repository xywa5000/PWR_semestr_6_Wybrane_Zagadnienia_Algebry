import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from python_lib.Polynomial import Polynomial

if __name__ == "__main__":

    f = Polynomial([4, 3, 2, 1])
    g = Polynomial([2, 3, 1])

    d, A, B = Polynomial.ext_gcd(f, g)

    print(f"f = {f}")
    print(f"g = {g}")

    print("gcd(f, g) = A * f + B * g")
    print(f"{d} = {A} * {f} + {B} * {g}")
