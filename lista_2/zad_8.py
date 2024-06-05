import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from python_lib.Polynomial import Polynomial

if __name__ == "__main__":

    #f = Polynomial([1, -1, -2])  # f(x) = x^2 - x + 1
    #g = Polynomial([3, -2, 1])  # g(x) = x^2 - 2x + 1
    f = Polynomial([6., 7., 3.])
    g = Polynomial([-6., -5., 4.])
    print(f/g)
    d, A, B = Polynomial.ext_gcd(f, g)
    print(f.gcd(g))
    print(f"nwd(f, g) = {d}")
    print(f"A = {A}")
    print(f"B = {B}")
    print(f"A * f + B * g = {A * f + B * g}")
