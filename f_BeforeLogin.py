'''
The functions support Log-in Interface
'''

'''
Import
'''
import numpy as np

'''
Pre-difined Variables
'''
MAX_ACCOUNTS = 5
MIN_PASSWORD_LENGTH = 8
MAX_PASSWORD_LENGTH = 12

#The dictionary that store 5 unique student accounts
#Name: Password
accounts = {}
accFullName = {}
accFriends = {} # disctionaty to store friends
pending_requests = {} # dictionary to store pending friend requests
usernameTrue = ""
special_characters = "!@#$%^&*()-+?_=,<>/"
loginStat = 0
flag = False

"""
Functions
"""
def flagUpdate(val):
    global flag
    flag = val

#The function that create new unique account
#Ask unique username and secure password: 
#minimum of 8 characters, maximum of 12 characters, at least one capital letter, one digit, one special character
def CreateNewAccount():
    readDictonary()
    if(len(accounts) >= MAX_ACCOUNTS):
        print("All permitted accounts have been created, please come back later")
        return 0
    else:
        #Ask Unique username
        while(1):
            #Stores users' name so they can be searched for by another user
            firstName = input(str("Please enter your first name: "))
            lastName = input(str("\nPlease enter your last name: "))
            fullname = firstName + lastName
            accFriends[username] = []
            #Checks to make sure the full name is unique
            for i in accFullName.keys():
                if(i == fullname): #Checks to see if the first name and last name are a unique combination
                    print("This name already exists for an account")
                    print("\n")
                    flagUpdate(True)
                    break
                    

                else:
                    break

            #When name already exists in the system, user gets asked name again
            if (flag == True):
                while(flag == True):
                    firstName = input(str("Please enter your first name: "))
                    lastName = input(str("\nPlease enter your last name: "))
                    fullname = firstName + lastName

                    for i in accFullName.keys():
                        if(i == fullname): #Checks to see if the first name and last name are a unique combination
                            print("This name already exists for an account")
                            print("\n")
                            break
                    

                        else:
                            flagUpdate(False)
                            break
            else:
                #Moves on to making a username
                print("")
                
             
            #Checks to make sure the username is unique
            global username
            username = input("Input your Username: ")
            for i in accounts.keys():
                if(i == username):
                    print("Existing username")
                    print("\n")
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
                print("Invalid password")
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
                accounts[username] = password
                accFullName[fullname] = username #Saves the firstName and lastName as the key and the username as the value
                print("Your account created successful!")
                print("\n")
                writeDictonary()
                return 1
            else:
                print("Invalid password")
                print("\n")
        

#The function that log in with existing account
#When succeed LogIn return 1, else return 0
def LogIn():
    readDictonary()
    global username
    username = input("Input your Username: ")
    password = input("Input your Password: ")
    for name, pw in accounts.items():
        if(name == username):
            if(pw == password):
                print("Login was successful!")
                print("\n")
                return 1
    else:
        print("Login was failed.")
        print("\n")
        return 0
    
#The function that provide a student success story 
def successStory():
    #Tell the story
    print("Maria Rodriguez was just another freshman at State University, navigating the labyrinth of college life. With dreams of a successful career in marketing, she knew she needed to seize every opportunity to gain experience and make connections. That's when she discovered InCollege, a powerful tool designed to bridge the gap between college and career.")
    print("\nUpon creating her account, Maria wasted no time in optimizing her profile. She uploaded a professional photo, polished her resume, and highlighted her skills and experiences. With her profile complete, she began exploring the job search feature. Filtering by industry and location, she found a marketing internship at a local startup that seemed tailor-made for her aspirations.")
    print("\nWith determination in her heart, Maria crafted a personalized cover letter and submitted her application through InCollege. Within days, she received an interview request. Armed with confidence and preparation, she aced the interview and landed the internship.")
    print("\nBut Maria's journey didn't stop there. Through InCollege's networking feature, she connected with fellow students studying marketing at universities across the country. They shared insights, exchanged tips, and even collaborated on projects. This virtual community became her support system, providing guidance and encouragement every step of the way.")
    print("\nAs Maria progressed through her college years, InCollege remained her trusted companion. She continued to explore job opportunities, attend virtual career fairs, and expand her professional network. By the time she graduated, Maria had secured a full-time position at a top marketing agency, thanks in large part to the connections she had made and the experiences she had gained through InCollege.")
    print("\nToday, Maria looks back on her college journey with gratitude and pride. InCollege not only helped her transition from campus to career but also empowered her to realize her dreams. From a wide-eyed freshman to a successful marketing professional, Maria's story is a testament to the power of ambition, perseverance, and the right tools at the right time.\n")
    return 1


def writeDictonary():
    #Saves the username and the user full name to numpy files
    np.save("accounts.npy", accounts)
    np.save("fullnames.npy", accFullName)
    return 1

def readDictonary():
    # print(" ")
    py_dict = np.load("accounts.npy", allow_pickle = "TRUE")
    py_dictFullName = np.load("fullnames.npy", allow_pickle = "TRUE")

    global accounts
    global accFullName

    accounts = py_dict.item()
    accFullName = py_dictFullName.item()
    return 1


#This function connects user with people that can help them
def connectPeople():
    readDictonary() #Puts the name values in accounts and accFullName dictionary
    firstNameSearch = input(str("Please enter the first name of the person you are looking for: "))
    lastNameSearch = input(str("\nNow please enter the last name of the person you are looking for: "))
    fullNameSearch = firstNameSearch + lastNameSearch

    if fullNameSearch in accFullName: #Searchs through names of registered users
        #print("It is: ", fullNameSearch)
        print("\nThey are a part of the InCollege system \n") #If a match is found, it prints a message
        print("Follow {} {} and come be apart of the InCollege System! \n".format(firstNameSearch, lastNameSearch))
        print("Please log in or sign up for an account \n")
        
        #User gets invited to join the InCollege System if contact is found
        searchJoin = int(input("Please select 1 to log in or select 2 to sign up: "))

        return searchJoin


        

    else: #When no match is found
        print("\nThey are not yet a part of the InCollege system yet \n")
        return 1





# Function to send friend request
def sendFriendRequest(sender, receiver):
    if receiver in pending_requests:
        pending_requests[receiver].append(sender)
    else:
        pending_requests[receiver] = [sender]
    print("Friend request sent successfully.")

# Function to display pending friend requests
def displayPendingRequests(username):
    if username in pending_requests:
        print("Pending friend requests:")
        for request in pending_requests[username]:
            print(request)
    else:
        print("No pending friend requests.")

# Function to handle accepting or rejecting friend requests
def handleFriendRequests(receiver, sender, decision):
    if decision.lower() == 'accept':
        # Add sender to receiver's friends list
        if receiver in accFriends:
            accFriends[receiver].append(sender)
        else:
            accFriends[receiver] = [sender]
        # Add receiver to sender's friends list
        if sender in accFriends:
            accFriends[sender].append(receiver)
        else:
            accFriends[sender] = [receiver]
        # Remove sender from pending requests of receiver
        if receiver in pending_requests:
            pending_requests[receiver].remove(sender)
        print("Friend request accepted.")
    elif decision.lower() == 'reject':
        # Remove sender from pending requests of receiver
        if receiver in pending_requests:
            pending_requests[receiver].remove(sender)
        print("Friend request rejected.")
    else:
        print("Invalid decision.")

