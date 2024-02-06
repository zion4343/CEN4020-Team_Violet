'''
The program support Log-in Interface
There provide two options, Log-in with existing account or creating new account
'''
MAX_ACCOUNTS = 5
MIN_PASSWORD_LENGTH = 8
MAX_PASSWORD_LENGTH = 12

#The directionary that store 5 unique student accounts
#Name: Password
account = {}

special_characters = "!@#$%^&*()-+?_=,<>/"
'''
Functions
'''
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
                print("invalid password")
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
            
    
#The fuction that is called after a successful login
def Validlogin():
    #Ask user options
    print("1. Search for a Job.")
    print("2. Find someone you know.")
    print("3. Learn a new skill.")
    loginoption = int(input("Select an option: "))

    if (loginoption == 1):
        print("under construction.")
    elif (loginoption == 2):
        print("under construction.")
    elif (loginoption == 3):
        skills()

#Function that displays avaliable skills for the user to learn
def skills():
    #User options
    print("Choose a skill you want to learn!")
    print("1. Data analysis")
    print("2. Web development")
    print("3. Programming")
    print("4. Cloud skill")
    print("5. Git")
    print("Press '0' to exit")

    choice = int(input("Select a skill: "))

    #Loop ensures the user enters a valid choice
    while (choice < 0 and choice > 5):
        print("Invalid choice")
        print("Choose a skill you want to learn!")
        print("1. Data analysis")
        print("2. Web development")
        print("3. Programming")
        print("4. Cloud skill")
        print("5. Git")
        print("Press '0' to exit")
        print(" ")

        choice = input("Select a skill: ")

    if (choice == 1):
        print("under construction")
    elif (choice == 2):
        print("under construction")
    elif (choice == 3):
        print("under construction")
    elif (choice == 4):
        print("under construction")
    elif (choice == 5):
        print("under construction")
    elif (choice == 0):
        Validlogin()

'''
Main Function
'''
print("Welcome to InCollege")

userselect = 1
#Loop until user can login
while(userselect != 0):
    #Ask user select
    print("1. Create new account")
    print("2. Login with existing account")
    userselect = int(input("Select your option: "))

    #If user select invalid option, ask to select again
    while(userselect != 1 and userselect != 2):
        print("Invalid Input")
        print("1. Create new account")
        print("2. Login with existing account")
        userselect = int(("Please select your option again: "))
        
    #Create new account 
    if(userselect == 1):
        CreateNewAccount()
    #LogIn Process
    if(userselect == 2):
        if(LogIn()):
            userselect = 0 #If LogIn Process is successed, break out from loop


#After Login
Validlogin()
                
    


