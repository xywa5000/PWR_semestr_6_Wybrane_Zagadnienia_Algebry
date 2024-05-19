import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from python_lib.Polynomial import Polynomial

a = Polynomial([1., 0., 1., 0., 1.])
b = Polynomial([-1., -2., -1., 0., 1.])
c = Polynomial([-1., 0., 0., 1])
d = Polynomial([-4., -4., 1., 1.])
e = Polynomial([4., -4., -1., 1.])
f = Polynomial([2., -1., -2., 1.])

print(f"GCD: {a}; {b}; {c}")
print(Polynomial.gcd_all([a, b, c]))

print(f"GCD: {d}; {e}; {f}")
print(Polynomial.gcd_all([d, e, f]))
