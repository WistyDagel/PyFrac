from UserDialogue import UserDialogue

class Main:
    def __init__(self):
        self.dialogue = UserDialogue()
    
    def main(self):
        self.dialogue.f1 = self.dialogue.retrieveFraction()
        # print(self.dialogue.f1.toString())
        UserDialogue.printFraction(self.dialogue.f1)
        # self.dialogue.printFraction(self.dialogue.f1)

main = Main()
main.main()