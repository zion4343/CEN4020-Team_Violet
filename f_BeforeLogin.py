'''
The functions support Log-in Interface
'''

MAX_ACCOUNTS = 5
MIN_PASSWORD_LENGTH = 8
MAX_PASSWORD_LENGTH = 12

#The directionary that store 5 unique student accounts
#Name: Password
account = {}
usernameTrue = ""
special_characters = "!@#$%^&*()-+?_=,<>/"
loginStat = 0

"""
Functions
"""

#The function that create new unique account
#Ask unique username and secure password: 
#minimum of 8 characters, maximum of 12 characters, at least one capital letter, one digit, one special character
def CreateNewAccount():
    if(len(account) > MAX_ACCOUNTS):
        print("All permitted accounts have been created, please come back later")
    else:
        #Ask Unique username
        while(1):
            username = input("Input your Username: ")
            for i in account.keys():
                if(i == username):
                    print("Existing username")
                    break
            else:
                break
        #Ask Secure password
        while(1):
            hasCapital = 0
            hasDigit = 0
            hasSpecial = 0  
            print("Create your password")
            print("Password need to fill the requirements")
            print("- minimum of 8 characters, maximum of 12 characters")
            print("- at least one capital letter")
            print("- at least one digit")
            print("- at least one special character")
            password = input("Input your password: ")
            
            #Indentify the password is secure or not
            #Password Length
            if(len(password) < MIN_PASSWORD_LENGTH or len(password) > MAX_PASSWORD_LENGTH):
                print("Invalid password!")
                print("\n")
                continue
            
            #Password Letters
            for i in password:
                if(i.isupper()):
                    hasCapital = 1
                elif(i.isdigit()):
                    hasDigit = 1
                elif any(c in special_characters for c in i):
                    hasSpecial = 1
            
            if(hasCapital and hasDigit and hasSpecial):
                account[username] = password
                print("Your account created successful!")
                return 1
            else:
                print("Invalid password")
        

#The function that log in with existing account
#When succeed LogIn return 1, else return 0
def LogIn():
    username = input("Input your Username: ")
    password = input("Input your Password: ")
    for name, pw in account.items():
        if(name == username):
            if(pw == password):
                print("Login was successful!")
                return 1
    else:
        print("Login was failed.")
        return 0
    
#The function that provide a student success story 
def successStory():
    return 0