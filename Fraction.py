def gcf(x, y):
    result = 1

    if (y == 0):
        result = x
    else:
        result = gcf(y, x % y)
    
    if (result < 0):
        result *= -1

    return result

class Fraction:
    def __init__(self, wholeNumber, numerator, denominator):
        self.wholeNumber = wholeNumber
        self.numerator = numerator
        if (denominator == 0):
            raise ValueError("Denominator must not be zero.")
        else:
            self.denominator = denominator

    def makeImproper(self):
        self.numerator = (self.wholeNumber * self.denominator) + self.numerator
        self.wholeNumber = 0

    def makeProper(self):
        if (self.numerator > self.denominator):
            self.wholeNumber = self.numerator // self.denominator
            self.numerator = self.numerator % self.denominator

    def reduce(self):
        self.makeImproper()
        # TODO loop? also, does this work properly?
        factor = gcf(self.numerator, self.denominator)
        self.numerator //= factor
        self.denominator //= factor
        self.makeProper()

    def toString(self):
        string = ""
        if (self.wholeNumber > 0):
            string = f'{self.wholeNumber} {self.numerator}/{self.denominator}'
        else:
            string = f'{self.numerator}/{self.denominator}'
        return string

# f1 = Fraction(0, 26, 12)
# print(f1.toString())
# f1.reduce()
# print(f1.toString())
