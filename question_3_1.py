import hashlib
import re

class Authenticator:
    #get the username from user
    def getUsername(self):
        username = input("Username: \n >>")
        return username.strip() #strip whitespace from username

    #get the password from user 
    def getPassword(self):
        password = input("Password: \n >>")
        return password.strip() #strip whitespace from password

    #get hashed user from textfile
    def getStoredUsers(self):
        users = []
        with open("users.txt", "r") as file:
            for line in file:
                users.append(line.strip()) 
        return users

    #hash the username and password
    def hashUser(self, username, password):
        return hashlib.sha256((username + password).encode()).hexdigest()

    #check if the user is in the textfile
    def checkUser(self, hashedUser, storedUsers):
        for user in storedUsers:
            if hashedUser == user:
                return True
        return False

    #check if username and password are valid strings
    def validateUser(self, username, password,):
        #test for all characters that are not a letter, number or underscore
        def isSpecialCharacter(char):
            regex = re.compile('[^a-zA-Z0-9_]')
            return bool(regex.search(char))

        #flags for validation
        isValid = False
        isUsernameValid = False
        isPasswordValid = False
        
        #flags for password validation
        isLengthValid = False
        isUpperCase = False
        isNumber = False
        isSpecialChar = False

        #list for password characters
        passwordChars = []

        #test if username length is greater than zero
        if len(username) > 0:
            isUsernameValid = True
        else:
            print("Username cannot be empty")

        passwordChars = list(password)

        if len(password) >= 8: #test password length 
            isLengthValid = True
            
            for char in passwordChars:
                if char.isupper():
                    isUpperCase = True
                elif char.isnumeric():
                    isNumber = True
                elif isSpecialCharacter(char):
                    isSpecialChar = True

        # validate password
        if isUpperCase and isNumber and isSpecialChar and isLengthValid:
            isPasswordValid = True
        else: 
            print("Invalid password. Must be at least 8 characters, contain one uppercase, one number, and one special character")
        
        # validate username and password
        if isUsernameValid and isPasswordValid:
            isValid = True

        return isValid
            
    #add validated user to textfile
    def addUser(self, hashedUser):
        with open("users.txt", "a") as file:
            file.write(hashedUser + "\n")

    def main():
        auth = Authenticator()
        
        run = True
        
        while run:
            userInput = input("1. Login \n2. Register \n3. Exit\n>> ")
            
            if userInput == "1":
                username = auth.getUsername()
                password = auth.getPassword()
                hashedUser = auth.hashUser(username, password)
                storedUsers = auth.getStoredUsers()
                
                if auth.checkUser(hashedUser, storedUsers):
                    print("Login successful")
                else:
                    print("Login failed")
                    
            elif userInput == "2":
                username = auth.getUsername()
                password = auth.getPassword()
                
                if auth.validateUser(username, password) == True:
                    auth.addUser(auth.hashUser(username, password))
                    
            elif userInput == "3":
                run = False
                
Authenticator.main()