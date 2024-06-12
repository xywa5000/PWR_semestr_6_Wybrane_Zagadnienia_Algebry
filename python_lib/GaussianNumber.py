# GaussianNumber.py

class GaussianNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __repr__(self):
        return f"GaussianNumber({self.real}, {self.imag})"

    def norm(self):
        return self.real ** 2 + self.imag ** 2

    def gcd(self, other):
        if self.norm() < other.norm():
            return other.gcd(self)
        while other.norm() != 0:
            self, other = other, (self // other)[1]
        return self

    def lcm(self, other):
        gcd = self.gcd(other)
        product = self * other
        quotient, remainder = product // gcd
        return quotient

    def __add__(self, other):
        return GaussianNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return GaussianNumber(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return GaussianNumber(
            self.real * other.real - self.imag * other.imag,
            self.real * other.imag + self.imag * other.real
        )

    def __truediv__(self, other):
        quotient = GaussianNumber((self.real * other.real + self.imag * other.imag) // other.norm(), (self.imag * other.real - self.real * other.imag) // other.norm())
        remainder = self - quotient * other
        return quotient, remainder

    def __floordiv__(self, other):
        return self.__truediv__(other)

    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag

    def __str__(self):
        if self.imag == 0:
            return f"{self.real}"
        if self.real == 0:
            return f"{self.imag}i"
        if self.imag < 0:
            return f"{self.real} - {-self.imag}i"
        return f"{self.real} + {self.imag}i"
