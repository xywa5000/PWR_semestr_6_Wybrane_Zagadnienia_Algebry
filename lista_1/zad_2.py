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

    def gcd(self, other):
        if self.degree() < other.degree():
            return other.gcd(self)
        a = self
        b = other
        while b.coefficients != [0.0]:
            _, r = a / b
            a = b
            b = r
        return a

    def lcm(self, other):
        gcd = self.gcd(other)
        product = self * other
        return product // gcd

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

# Przykładowe użycie
p1 = Polynomial([6., 7., 1.])
p2 = Polynomial([-6., -5., 1.])


print(p1.gcd(p2))   # Polynomial([12., 12.])

p3 = Polynomial([6., 7., 1.])
p4 = Polynomial([-6., -5., 1.])
print(p1.lcm(p2))   # Polynomial([-3., -3., 1./12., 1./12.])

p5 = Polynomial([1.0, 0.0, 1.0, 0.0, 1.0])
p6 = Polynomial([-1.0, -2.0, -1.0, 0.0, 1.0])
p7 = Polynomial([-1.0, 0.0, 0.0, 1.0])
print(Polynomial.gcd_all([p5, p6, p7]))  # Polynomial([1.0])


p8 = Polynomial([1.0, 1.0])
print(Polynomial.ext_gcd(p1, p2))    # (Polynomial([1.0]), Polynomial([-2.0, 1.0]), Polynomial([1.0, -1.0]))
