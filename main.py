'''
The program support main function for InCollege Software
'''

'''
Import
'''
import f_BeforeLogin as b_login
import f_AfterLogin as a_login

'''
Functions
'''


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
    print("3. See a college student success story")
    userselect = int(input("Select your option: "))


    #If user select invalid option, ask to select again
    while(userselect != 1 and userselect != 2):
        print("Invalid Input")
        print("1. Create new account")
        print("2. Login with existing account")
        print("3. See a college student success story")
        userselect = int(("Please select your option again (1 or 2 or 3): "))
        
    #Create new account 
    if(userselect == 1):
        print("\n")
        b_login.CreateNewAccount()

    #LogIn Process
    elif(userselect == 2):
        if(b_login.LogIn()):
            userselect = 0 #If LogIn Process is succesful, break out from loop
            
    #Show Success Story and Provide the option to see the video
    elif(userselect == 3):
        b_login.successStory()
        



#After Login
a_login.addOptions()    

                
    

