class ShapePrinter():

    def getHeight(self):
        userInput =  input("Enter the height: \n >>")
        try:
            # Attempt to convert the input to an integer
            userInput = int(userInput)
            return int(userInput)
        except ValueError:
            # If conversion fails, print an error message
            print("Invalid input. Please enter a number.")
            self.getHeight()
    
    def getWidth(self):
        userInput = (input("Enter the width: \n >>"))
        try:
            # Attempt to convert the input to an integer
            userInput = int(userInput)
            return int(userInput)
        except ValueError:
            # If conversion fails, print an error message
            print("Invalid input. Please enter a number.")
            self.getWidth()
    
    def getCaracter(self):
        userInput = input("Enter the caracter: \n 1. # \n 2. * \n 3. | \n >>")
        if userInput == "1":
            return "#"
        elif userInput == "2":
            return "*"
        elif userInput == "3":
            return "|"
        else: 
            print("Invalid input")
            self.getCaracter()
    
    def getShape(self):
        userInput = input("Enter the shape: \n 1. Rectangle \n 2. Triangle \n 3. Square \n >>")
        if userInput == "1":
            return "Rectangle"
        elif userInput == "2":
            return "Triangle"
        elif userInput == "3":
            return "Square"
        else: 
            print("Invalid input")
            self.getShape()
        
    def printShape(self):
        height = self.getHeight()
        caracter = self.getCaracter()
        shape = self.getShape()
        
        
        if shape == "Rectangle":
            width = self.getWidth()
            if caracter == "#":
                print("#" * width)
                for i in range(height - 2):
                    print("#" + " " * (width - 2) + "#")
                print("#" * width)
            elif caracter == "*":
                print("*" * width)
                for i in range(height - 2):
                    print("*" + " " * (width - 2) + "*")
                print("*" * width)
            elif caracter == "|":
                print("_" * width)
                for i in range(height - 2):
                    print("|" + " " * (width - 2) + "|")
                print("_" * width)
        if shape == "Triangle":
            if caracter == "#":
                for i in range(height):
                    print("#" * (i + 1))
            elif caracter == "*":
                for i in range(height):
                    print("*" * (i + 1))
            elif caracter == "|":
                for i in range(height):
                    print("|" * (i + 1))
        if shape == "Square":
            if caracter == "#":
                for i in range(height):
                    print("#" * height)
            elif caracter == "*":
                for i in range(height):
                    print("*" * height)
            elif caracter == "|":
                for i in range(height):
                    print("|" * height)

    def main(self):
        run = True
        while run == True:
            if input("Do you want to print a shape? (y/n) \n >>") == "y":
                shapePrinter = ShapePrinter()
                shapePrinter.printShape()
            else:
                run = False

ShapePrinter().main()