### Wybrane Zagadnienia Algebry

***

# Lista 1

## Zadanie 1

- Liczbami Gaussa nazywamy pierścień $ \mathbb{Z}[ı] = \{a + bı : a, b \in \mathbb{Z}\} $ z dodawaniem i dzieleniem odziedziczonym z liczb zespolonych. 
- Na $ \mathbb{Z}[ı] $ określamy funkcję (zwaną normą) $ N(a + bı) = a^2 + b^2 $. 
- Dla $ x, y \in \mathbb{Z}[ı] $ określamy
$ x \mid y \leftrightarrow (\exists z \in \mathbb{Z}[ı])(y = x \cdot z) $

### Zadanie 1.1

Implementacja dzielenia z resztą na Liczbach Gaussa.

### Zadanie 1.2

Implementacja funkcji wyznaczającej NWD (gcd()) na Liczbach Gaussa.

### Zadanie 1.3

Implementacja funkcji wyznaczającej NWW (lcm()) na Liczbach Gaussa.

### Zadanie 1.4

Ideały generowane przez:

- $ (3 + 4i, 1 + 3i) = gcd(3 + 4i, 1 + 3i) = -1 + 2i $
- $ (3 + 4i) \cap (1 + 3i) = lcm(3 + 4i, 1 + 3i) = 7 + 1i $

## Zadanie 2

Wielomian $ a_0 + a_1 \cdot x + \ldots + a_n x^n \in \mathbb{R}[x] $ interpretujemy jako ciąg $ [a_0, \ldots, a_n] $

### Zadanie 2.1

Implementacja dzielenia z resztą w $ \mathbb{R}[x] $.

### Zadanie 2.2

Implementacja funkcji wyznaczającej NWD (gcd()) w $ \mathbb{R}[x] $.

### Zadanie 2.3

Implementacja funkcji wyznaczającej NWW (lcm()) w $ \mathbb{R}[x] $.

### Zadanie 2.4

Ideały generowane przez:

- $ (1 + x^2, 1 + 2x + x^2) = gcd(1 + x^2, 1 + 2x + x^2) = 1 $
- $ (1 + x^2) \cap (1 + 2x + x^2) = lcm(1 + x^2, 1 + 2x + x^2) = 1 + 2x + 2x^2 + 2x^3 + x^4 $

## Zadanie 3

Rozmaitości algebraiczne:

### Zadanie 3.1

$ V(z - x^2 - y^2) \rightarrow z = x^2 + y^2 $

### Zadanie 3.2

$ V(z^2 - x^2 - y^2) \rightarrow z^2 = x^2 + y^2 \rightarrow z = \sqrt{x^2 + y^2} $

### Zadanie 3.3

$ V(z^2 - x^2 + y^2) \rightarrow z^2 = x^2 - y^2 $

### Zadanie 3.4

$ V(xz + yz) \rightarrow 0 = z(x + y) \rightarrow z = 0 \vee x + y = 0 $

## Zadanie 4

Krzywa czterolistna we współrzędnych biegunowych: $ r(\theta) = \sin(2\theta) $

### Zadanie 4.1

Narysuj tę krzywą: *zad_4.py > zadanie_4_1()*

### Zadanie 4.2

Znajdź wielomian, który odpowiada tej krzywej (konwersja z biehunowych na kartezjańskie).

$r(t) = sin(2t) = 2sin(t)cos(t)$

$r(t)^3 = 2(rsin(t))(rcos(t))$

$rcos(t) = x$

$rsin(t) = y$

$r(t) = sqrt(x^2 + y^2)$

$\texttt{zatem } r^3 = 2xy \texttt{ oraz } r = sqrt(x^2 + y^2)$

$(x^2 + y^2)^{3/2} = 2xy$

$(x^2 + y^2)^3 = 4x^2y^2$

$ 0 = 4x^2y^2 - (x^2 + y^2)^3 $

Narysuj ten wielomian: *zad_4.py > zadanie_4_2()*

## Zadanie 5

### Zadanie 5.1

Polecenia systemu Wolfram Alpha do działań na wielomianach:

- $ PolynomialQuotientReminder(4x^2 + 2x + 1, x - 1, x) = {4x + 6, 7} $

- $ PolynomialGCD(x^3 - 4x^2 + 1, x +1, x) = 1 $

- $ PolynomialLCM(x^3 - 4x^2 + 1, x +1, x) = x + x^2 - 4 x^3 - 3 x^4 + x^5 $

### Zadanie 5.2

Polecenia systemu Wolfram Alpha do genrowania krzywych i powierzchni:

- $ ParametricPlot(x+y^2, \{x, -10, 10\}, \{y, -10, 10\}) $ - powierzchnia

- $ ParametricPlot(sin(x)+y^2=0, \{x, -10, 10\}, \{y, -10, 10\}) $ - krzywa