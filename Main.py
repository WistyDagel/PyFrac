from UserDialogue import UserDialogue

class Main:
    def __init__(self):
        self.dialogue = UserDialogue()
    
    def main(self):
        firstFractionCorrect = False
        while (firstFractionCorrect == False):
            # print(self.dialogue.f1.toString())
            print("--FIRST FRACTION--")
            self.dialogue.f1 = self.dialogue.retrieveFraction()
            UserDialogue.printFraction(self.dialogue.f1)
            response = input("\nIs this your fraction? (y/n)")
            if (response == "y"):
                firstFractionCorrect = True
            elif (response == "n"):
                firstFractionCorrect = False
        # self.dialogue.printFraction(self.dialogue.f1)
        secondFractionCorrect = False 
        while (secondFractionCorrect == False):
            print("--SECOND FRACTION--")
            self.dialogue.f2 = self.dialogue.retrieveFraction()
            UserDialogue.printFraction(self.dialogue.f2)
            response = input("\nIs this your fraction? (y/n)")
            if (response == "y"):
                secondFractionCorrect = True
            elif (response == "n"): 
                secondFractionCorrect = False
        
        notEquated = True
        while (notEquated):
            print("--SELECT AN OPERATION--")
            selection = input("1) Add \n2) Subtract \n3) Multiply \n4) Divide\n")
            if (selection == "1"):
                self.add(self.dialogue.f1, self.dialogue.f2)
                notEquated = False
            elif (selection == "2"):
                self.subtract(self.dialogue.f1, self.dialogue.f2)
                notEquated = False
            elif (selection == "3"):
                self.multiply(self.dialogue.f1, self.dialogue.f2)
                notEquated = False
            elif (selection == "4"):
                self.divide(self.dialogue.f1, self.dialogue.f2)
                notEquated = False

    
    def add(self, f1, f2):
        f1.makeImproper()
        f2.makeImproper()
        self.dialogue.result.denominator = f1.denominator * f2.denominator
        self.dialogue.result.numerator = (f1.numerator * f2.denominator) + (f2.numerator * f1.denominator)
        self.dialogue.result.reduce()
        f1.makeProper()
        f2.makeProper()
        UserDialogue.printFraction(self.dialogue.f1)
        print(" + ", end="")
        UserDialogue.printFraction(self.dialogue.f2)
        print(" = ", end="")
        UserDialogue.printFraction(self.dialogue.result)

    def subtract(self, f1, f2):
        f1.makeImproper()
        f2.makeImproper()
        self.dialogue.result.denominator = f1.denominator * f2.denominator
        self.dialogue.result.numerator = (f1.numerator * f2.denominator) - (f2.numerator * f1.denominator)
        self.dialogue.result.reduce()
        f1.makeProper()
        f2.makeProper()
        UserDialogue.printFraction(self.dialogue.f1)
        print(" - ", end="")
        UserDialogue.printFraction(self.dialogue.f2)
        print(" = ", end="")
        UserDialogue.printFraction(self.dialogue.result)

    def multiply(self, f1, f2):
        f1.makeImproper()
        f2.makeImproper()
        self.dialogue.result.numerator = f1.numerator * f2.numerator
        self.dialogue.result.denominator = f1.denominator * f2.denominator
        self.dialogue.result.reduce()
        f1.makeProper()
        f2.makeProper()
        UserDialogue.printFraction(self.dialogue.f1)
        print(" * ", end="")
        UserDialogue.printFraction(self.dialogue.f2)
        print(" = ", end="")
        UserDialogue.printFraction(self.dialogue.result)

    def divide(self, f1, f2):
        f1.makeImproper()
        f2.makeImproper()
        self.dialogue.result.numerator = f1.numerator * f2.denominator
        self.dialogue.result.denominator = f1.denominator * f2.numerator
        self.dialogue.result.reduce()
        f1.makeProper()
        f2.makeProper()
        UserDialogue.printFraction(self.dialogue.f1)
        print(" / ", end="")
        UserDialogue.printFraction(self.dialogue.f2)
        print(" = ", end="")
        UserDialogue.printFraction(self.dialogue.result)
    
main = Main()
main.main()