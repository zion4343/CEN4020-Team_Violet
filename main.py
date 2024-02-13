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
    print("4. Connect with a registered member")
    userselect = int(input("Select your option: "))
    print("\n")


    #If user select invalid option, ask to select again
    while(userselect != 1 and userselect != 2 and userselect != 3 and userselect != 4):
        print("Invalid Input")
        print("1. Create new account")
        print("2. Login with existing account")
        print("3. See a college student success story")
        print("4. Connect with a registered member")
        userselect = int(("Please select your option again (1 or 2 or 3 or 4): "))
        print("\n")

    #Create new account 
    if(userselect == 1):
        b_login.CreateNewAccount()

    #LogIn Process
    elif(userselect == 2):
        if(b_login.LogIn()):
            userselect = 0 #If LogIn Process is succesful, break out from loop
            
    #Show Success Story and Provide the option to see the video
    elif(userselect == 3):
        #Show Success Story
        b_login.successStory()
        
        #Ask whether user want to see video or not
        print("Next, do you want to watch the video that explains why user should join in InCollege?")
        watchVideo = int(input("If you want, enter 1, else enter 0: "))
        #If user enter invalid input, ask again
        while(watchVideo != 1 and watchVideo != 0):
            watchVideo = int(input("Invalid Enter, please enter your option again (0 or 1): "))    
        
        if(watchVideo):
            print("Video is now playing")
            watchVideo = input("If do you want to quit, enter something: ")
            print("\n")

    #This allows the user to search for a person using their first and last name, in order to connect with them
    elif(userselect == 4):
        b_login.connectPeople()
        continue

#After Login
a_login.addOptions()    

                
    

