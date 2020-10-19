from Fraction import Fraction

class UserDialogue:
    def __init__(self):
        self.f1 = None
        self.f2 = None
        self.result = None
    
    def retrieveFraction(self):
        whole = int(input("Please Enter a Whole Number: "))
        num = int(input("Please Enter a Numerator: "))
        den = int(input("Please Enter a Denominator: "))
        try:
            fraction = Fraction(whole, num, den)
            return fraction
        except ValueError as er:
            print("Denominator can not be zero")
    
    @classmethod
    def printFraction(cls, fraction):
        string = ""
        if (fraction.wholeNumber > 0):
            string = f'{fraction.wholeNumber} {fraction.numerator}/{fraction.denominator}'
        else:
            string = f'{fraction.numerator}/{fraction.denominator}'
        print(string)


# ud = UserDialogue()

# f1 = None
# while (f1 is None):
#     f1 = ud.retrieveFraction()

# print(ud.printFraction(f1))