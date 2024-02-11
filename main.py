import logging

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
usernameTrue = ""
special_characters = "!@#$%^&*()-+?_=,<>/"
loginStat = 0

'''
Functions
'''
#This function to updates the global variable
def updateLogin():
    global loginStat  #Accesses the global variable within the function
    loginStat = 1  #This update the value of the global variable




#The function that create new unique account
#Ask unique username and secure password: 
#minimum of 8 characters, maximum of 12 characters, at least one capital letter, one digit, one special character
def CreateNewAccount(username):
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
def LogIn(username):
    username = input("Input your Username: ")
    password = input("Input your Password: ")
    for name, pw in account.items():
        if(name == username):
            if(pw == password):
                print("Login was successful!")
                updateLogin()
                return 1
    else:
        print("Login was failed.")
        return 0
    

#This function to gives additional options after login is successful
def addOptions():
    print("Welcome! What would you like to do?")
    print("1. Search for a job")
    print("2. Find someone you know")
    print("3. Learn a new skill")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Job search/internship option is currently under construction.")

    elif choice == "2":
        print("Find someone you know option is currently under construction.")

    elif choice == "3":
        print("Here are 5 skills you can learn:")
        print("1. Programming")
        print("2. Prompt Engineering")
        print("3. 3D Modeling & Simulation")
        print("4. Data Analysis")
        print("5. Language Learning")
        print("6. Return to the previous level. . .")

        #Presents the user with the option to choose a skill
        choiceSkill = input("Enter your skill choice: ")

        if choiceSkill == "1":
            print("The Programming option is currently under construction.")

        elif choiceSkill == "2":
            print("The Prompt Engineering option is currently under construction.")

        elif choiceSkill == "3":
            print("The 3D Modeling & Simulation option is currently under construction.")

        elif choiceSkill == "4":
            print("The Data Analysis option is currently under construction.")

        elif choiceSkill == "5":
            print("The Language Learning option is currently under construction.")
        
        else:
            print("6. Returning to the previous level. . .")
            addOptions()

    else:
        print("Invalid choice.")

    return 1
            
    

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
        userselect = int(("Please select your option again (1 or 2): "))
        
    #Create new account 
    if(userselect == 1):
        print("\n")
        CreateNewAccount(usernameTrue)

    #LogIn Process
    if(userselect == 2):
        if(LogIn(usernameTrue)):
            userselect = 0 #If LogIn Process is succesful, break out from loop



#After Login
if(loginStat == 1):
    addOptions()    

                
    

