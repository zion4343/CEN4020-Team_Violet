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
#Function displays all links
def displayLinks():
    print("\nUseful Links:")
    print("1. General")
    print("2. Browse InCollege")
    print("3. Business Solutions")
    print("4. Directories")
    print("0. Exit")

#displays all the general links (if 1 is chosen)
def displayGeneralLinks():
    print("\nGeneral Links:")
    print("1. Sign Up")
    print("2. Help Center")
    print("3. About")
    print("4. Press")
    print("5. Blog")
    print("6. Careers")
    print("7. Developers")
    print("0. Back")

#Choosing general
def handle_general_link_selection(selection):
    if selection == 1:
        while True:
            print("\n1. Create new account")
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

                    ###This part shows a bug in code since the while loop is no longer running on the condition of userselect.
                    ###Other instances need to be fixed
                    userselect = 0 #If LogIn Process is succesful, break out from loop
                    a_login.addOptions(b_login.username)
                    break
                    
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
                userJoinNum = b_login.connectPeople()
                #User wants to log in
                if (userJoinNum == 1):
                    #If LogIn Process is succesful, break out from loop
                    if(b_login.LogIn()):
                        userselect = 0 

                #User wants to sign up for an account
                elif userJoinNum == 2:
                    b_login.CreateNewAccount()
                continue

    elif selection == 2:
        print("We're here to help")
    elif selection == 3:
        print("InCollege: Welcome to InCollege, the world's largest college student network with many users in many countries and territories worldwide")
    elif selection == 4:
        print("InCollege Pressroom: Stay on top of the latest news, updates, and reports")
    elif selection in range(5, 8):
        print("Under construction")



def inputValidation(prompt, valid_options):
    while True:
        try:
            user_input = int(input(prompt))
            if user_input in valid_options:
                return user_input
            print("Invalid input. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

'''
Main Function
'''

userselect = 1

print("Welcome to InCollege")

while True:
    displayLinks()
    userselect = inputValidation("Select your options: ", [0,1,2,3,4])

    if userselect == 0:
        print("Exiting...")
        break
    elif userselect == 1:
        displayGeneralLinks()
        general_selection = inputValidation("Select an option: ", list(range(8)))
        if general_selection == 0:
            continue
        handle_general_link_selection(general_selection)
        break
    else:
        print("Under construction")   
        break