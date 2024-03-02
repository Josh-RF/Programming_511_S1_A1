class Factorial():

    def getUserInput(self):
        userInput = input("Enter a number: \n>> ")
        return userInput
    
    def validateUserInput(self, userInput):
        if userInput.lower() == 'q':
            return False, userInput
        try:
            userInput = int(userInput)
            return True, userInput
        except ValueError:
            print("Invalid input. Please enter a number.")
            return False, None
        
    def determineFactorial(self, userInput):
        if userInput == 0:
            return 1
        else:
            factorial = 1
            while userInput > 1:
                factorial *= userInput
                userInput -= 1
            return factorial

    def main(self):
        factorial = Factorial()
        print("To quit enter q")
        run = True

        while run == True:
            userInput = factorial.getUserInput()
            isValid, userInput = self.validateUserInput(userInput)
            if isValid == False and userInput == 'q':
                run = False
            elif isValid == True:
                print(factorial.determineFactorial(int(userInput)))
            
Factorial().main()