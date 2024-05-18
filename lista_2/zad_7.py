import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from python_lib.Polynomial import Polynomial

# Przykładowe użycie funkcji
a = Polynomial([1., 0., 1., 0., 1.])
b = Polynomial([-1., -2., -1., 0., 1.])
c = Polynomial([-1., 0., 0., 1])
d = Polynomial([-4., -4., 1., 1.])
e = Polynomial([4., -4., -1., 1.])
f = Polynomial([2., -1., -2., 1.])
