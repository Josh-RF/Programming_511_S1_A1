class Factorial():

    def getUserInput(self): 
        # Prompt the user to enter a number
        userInput = input("Enter a number: \n>> ")
        return userInput
    
    def validateUserInput(self, userInput):
        # Check if the user wants to quit
        if userInput.lower() == 'q':
            return False, userInput
        try:
            # Attempt to convert the input to an integer
            userInput = int(userInput)
            return True, userInput
        except ValueError:
            # If conversion fails, print an error message
            print("Invalid input. Please enter a number.")
            return False, None
        
    def determineFactorial(self, userInput):
        # Calculate the factorial of the input number
        if userInput == 0:
            return 1
        else:
            factorial = 1
            while userInput > 1:
                factorial *= userInput
                userInput -= 1
            return factorial

    def main(self):
        # Create an instance of the Factorial class
        factorial = Factorial()
        print("To quit enter q")
        run = True

        while run == True:
            # Get user input
            userInput = factorial.getUserInput()
            # Validate user input
            isValid, userInput = self.validateUserInput(userInput)
            # Check if user wants to quit
            if isValid == False and userInput == 'q':
                run = False
            elif isValid == True:
                # Calculate and print the factorial
                print(factorial.determineFactorial(int(userInput)))
            
# Call the main method to start the program
Factorial().main()
