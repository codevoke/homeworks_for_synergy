from multipledispatch import dispatch


class My_Fraction:
    pass


class My_Fraction:
    def __init__(self, num: int, den: int):
        if den == 0:
            raise ZeroDivisionError("Fraction's denominator can't be 0")
        self.num = num
        self.den = den

    def simplify(self):
        for _ in range(min(self.num, self.den), 1, -1):
            if self.num % _ == 0 and self.den % _ == 0:
                self.num = self.num // _
                self.den = self.den // _
                self.simplify()

    def multiply(self, number: int | My_Fraction) -> My_Fraction:
        ...
    

@dispatch(int)
def multiply(self, number: int):
    self.num = self.num * number
    self.den = self.den
    self.simplify()


@dispatch(My_Fraction)
def multiply(self, fraction: My_Fraction):
    self.num = self.num * fraction.num
    self.den = self.den * fraction.den
    self.simplify()


My_Fraction.multiply = multiply
