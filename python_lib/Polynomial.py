# Polynomial.py
from functools import reduce

class Polynomial:
    def __init__(self, coefficients):
        # Usunięcie nadmiarowych zer z końca listy współczynników
        while coefficients and coefficients[-1] == 0.0:
            coefficients.pop()
        self.coefficients = coefficients if coefficients else [0.0]

    def __repr__(self):
        return f"Polynomial({self.coefficients})"

    def degree(self):
        if len(self.coefficients) == 1 and self.coefficients[0] == 0.0:
            return -1
        else:
            return len(self.coefficients) - 1

    def lc(self):
        return self.coefficients[-1]
    
    def divide_by_gcd(self):
        if not self.coefficients or all(c == 0 for c in self.coefficients):
            return self  # Jeśli wielomian jest zerowy, zwróć go bez zmian

        def gcd_int(a, b):
            while b:
                a, b = b, a % b
            return a

        def find_gcd_of_list(lst):
            return reduce(gcd_int, lst)

        # Zamiana współczynników na liczby całkowite (lub ich absolutne wartości)
        integer_coefficients = [abs(int(c)) for c in self.coefficients]

        # Znalezienie GCD wszystkich współczynników i Podzielenie każdego współczynnika przez GCD
        if integer_coefficients != [0.0]:
            overall_gcd = find_gcd_of_list(integer_coefficients)
            self.coefficients = [c / overall_gcd for c in self.coefficients]
        return self

    def gcd(self, other):
        if self.degree() < other.degree():
            return other.gcd(self)
        a = self
        b = other
        while b.coefficients != [0.0]:
            _, r = a / b
            a = b
            b = r
        a.divide_by_gcd()
        return a

    def lcm(self, other):
        gcd = self.gcd(other)
        product = self * other
        quotient, remainder = product // gcd
        return quotient

    @staticmethod
    def gcd_all(polynomials):
        from functools import reduce
        return reduce(lambda acc, x: acc.gcd(x), polynomials, Polynomial([0.0]))

    @staticmethod
    def ext_gcd(a, b):
        if b.coefficients == [0.0]:
            return a, Polynomial([1.0]), Polynomial([0.0])
        q, r = a / b
        d, s, t = Polynomial.ext_gcd(b, r)
        return d, t, s - q * t

    def __add__(self, other):
        max_len = max(len(self.coefficients), len(other.coefficients))
        result = [0.0] * max_len
        for i in range(max_len):
            if i < len(self.coefficients):
                result[i] += self.coefficients[i]
            if i < len(other.coefficients):
                result[i] += other.coefficients[i]
        while result and result[-1] == 0.0:
            result.pop()
        return Polynomial(result)

    def __sub__(self, other):
        max_len = max(len(self.coefficients), len(other.coefficients))
        result = [0.0] * max_len
        for i in range(max_len):
            if i < len(self.coefficients):
                result[i] += self.coefficients[i]
            if i < len(other.coefficients):
                result[i] -= other.coefficients[i]
        while result and result[-1] == 0.0:
            result.pop()
        return Polynomial(result)

    def __mul__(self, other):
        result = [0.0] * (len(self.coefficients) + len(other.coefficients) - 1)
        for i in range(len(self.coefficients)):
            for j in range(len(other.coefficients)):
                result[i + j] += self.coefficients[i] * other.coefficients[j]
        return Polynomial(result)

    def __truediv__(self, other):
        q = Polynomial([0.0])
        r = self
        d = other
        c = other.lc()
        while r.degree() >= d.degree() and r.coefficients != [0.0]:
            s = [0.0] * (r.degree() - d.degree())
            s.append(r.lc() / c)
            t = Polynomial(s)
            q = q + t
            r = r - (t * d)
        return q, r

    def __floordiv__(self, other):
        return self.__truediv__(other)

    def __eq__(self, other):
        return self.coefficients == other.coefficients

    def __str__(self):
        if not self.coefficients or self.coefficients == [0.0]:
            return "0"
        terms = []
        for i in range(len(self.coefficients)):
            coeff = self.coefficients[i]
            if coeff != 0.0:
                if i == 0:
                    terms.append(f"{coeff}")
                elif i == 1:
                    terms.append(f"{coeff}x")
                else:
                    terms.append(f"{coeff}x^{i}")
        return " + ".join(reversed(terms))
