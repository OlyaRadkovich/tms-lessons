class Rational:
    def __init__(self, numerator: int, denominator: int):
        self.__numer = numerator
        self.__den = denominator
        self.__normalise()

    @property
    def numerator(self):
        return self.__numer

    @property
    def denominator(self):
        return self.__den

    def __str__(self):
        return f'{self.__numer}/{self.__den}'

    def __mul__(self, other: 'Rational') -> 'Rational':
        numer = self.__numer * other.__numer
        den = self.__den * other.__den
        return Rational(numer, den)

    def __truediv__(self, other: 'Rational') -> 'Rational':
        numer = self.__numer * other.__den
        den = self.__den * other.__numer
        return Rational(numer, den)

    def __add__(self, other: 'Rational') -> 'Rational':
        numer = self.__numer * other.__den + other.__numer * self.__den
        den = self.__den * other.__den
        return Rational(numer, den)

    def __sub__(self, other: 'Rational') -> 'Rational':
        numer = self.__numer * other.__den - other.__numer * self.__den
        den = self.__den * other.__den
        return Rational(numer, den)

    def __normalise(self):
        a = abs(self.numerator)
        b = abs(self.denominator)
        while b:
            a, b = b, a % b
        self.__numer //= a
        self.__den //= a
        if self.denominator < 0:
            self.__numer *= -1
            self.__den *= -1

    def __eq__(self, other: 'Rational'):
        return self.__numer * other.__den == other.__numer * self.__den

    def __ne__(self, other: 'Rational'):
        return self.__numer * other.__den != other.__numer * self.__den

    def __lt__(self, other: 'Rational'):
        return self.__numer * other.__den < other.__numer * self.__den

    def __le__(self, other: 'Rational'):
        return self.__numer * other.__den <= other.__numer * self.__den

    def __gt__(self, other: 'Rational'):
        return self.__numer * other.__den > other.__numer * self.__den

    def __ge__(self, other: 'Rational'):
        return self.__numer * other.__den >= other.__numer * self.__den


if __name__ == '__main__':
    assert str(Rational(4, 8)) == '1/2'
    num1 = Rational(1, 5)
    num2 = Rational(3, 7)
    assert str(Rational.__add__(num1, num2)) == '22/35'
    assert str(Rational.__sub__(num1, num2)) == '-8/35'
    assert str(Rational.__mul__(num1, num2)) == '3/35'
    assert str(Rational.__truediv__(num1, num2)) == '7/15'
    assert Rational(1, 2) == Rational(3, 6)
    assert Rational(3, 8) != Rational(3, 7)
    assert Rational(3, 8) > Rational(3, 9)
    assert Rational(3, 8) < Rational(3, 7)
    assert Rational(3, 5) >= Rational(3, 7)
    assert Rational(3, 8) <= Rational(3, 7)
    assert str(Rational(1, 4) * (Rational(3, 2)
                                 + Rational(1, 8)) + Rational(156, 100)) == '1573/800'
