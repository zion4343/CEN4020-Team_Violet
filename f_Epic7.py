'''
The functions developed in Epic 6
'''

'''
Import
'''
import numpy as np

'''
Functions
'''

#Checks if user is a an Plus or Standard user
isPlus = False

def checkUserPlan(username):
    #Loads the accounts dictionary and checks for error
    try:
        accounts = np.load("accounts.npy", allow_pickle=True).item()

    except FileNotFoundError:
        print("Accounts file not found. Make sure you have run the account creation process.")
        return
    
   #Check if the logged-in user is a "plus" user
    if username in accounts and 'plus' in accounts[username] and accounts[username]['plus'] == '1':
        isPlus = True

    else: #User is on the standard plan
        isPlus = False

    return isPlus

def flagAssign(num):
    global flag
    flag = num

    return flag




def manageMessage(username):
    #Checks whether user is an Plus user or just Standard
    global isPlus
    isPlus = checkUserPlan(username)

    #Displays a menu option for users
    print("1. Send a message")
    print("2. View your messages")
    print("3. Delete Message from Inbox \n")

    messageChoice = int(input("Please select 1 or 2 or 3 from the menu options: "))
    print("\n")

    #User can send a message when option 1 is chosen
    if messageChoice == 1:

        if isPlus == False: #Uses the messaging function for standard users
            sendMessage(username)

        else: #Uses the messaging function for plus users
            sendMessagePlus(username)

    #User can view their own inbox when option 2 is chosen    
    elif messageChoice == 2:
        viewInbox(username)

    #User deletes their inbox
    elif messageChoice == 3:
        deleteMessage(username)

    else:
        print("That was an invalid selection.")

    return



#Function that enables a message to be sent to a friend for plus users
def sendMessagePlus(username):
    
    
    #Loads the accounts dictionary and checks for error
    try:
        accounts = np.load("accounts.npy", allow_pickle=True).item()

    except FileNotFoundError:
        print("Accounts file not found. Make sure you have run the account creation process.")
        return

    #Asks the user to select a friend to send a message to
    friends_list = list(accounts.keys()) #SHOWS LIST OF ALL USERS

    

    #Displays the all the friends in the friends list
    print("Here is a list of all users")
    print("-----------------------------------------")
    for index, friend_username in enumerate(friends_list, start=1):
        friend_full_name = accounts[friend_username].get('full_name', 'No name available')

        #Skips printing user's own name
        if username == friend_username:
            continue

        else:
            print(f"{index}. {friend_full_name} ({friend_username})") 
    
    
    #Asks the user to select a person from the list
    selection = input("\nEnter the number of the person you want to send a message to: ")

    if selection.isdigit():
        selection = int(selection)
        if 1 <= selection <= len(friends_list):
            recipient_username = friends_list[selection - 1]
            message = input("Enter your message: ") #Asks user to submit their message

            #Saves the message in recipient's inbox
            saveMessage(recipient_username, username, message, 1)
            print("Message sent successfully.")


        else:
            print("Invalid selection.")

    else:
        print("Invalid input.")


#Function that enables a message to be sent to a friend
def sendMessage(username):
    
    #Turns to 1 when the person user chose is in the friends' list
    flag = 0

    #Loads the accounts dictionary and checks for error
    try:
        accounts = np.load("accounts.npy", allow_pickle=True).item()

    except FileNotFoundError:
        print("Accounts file not found. Make sure you have run the account creation process.")
        return
       
    

    #Asks the user to select a friend to send a message to
    friendPick = input("Enter the username of a friend to send a message: ")
    print("\n")

    #Loads (or creates) a temp inbox dictionary
    try:
        inboxTemp = np.load(f"{username}_temp_inbox.npy", allow_pickle=True).item()

    except FileNotFoundError:
        inboxTemp = {}

    friends_list = accounts[username].get('friends', []) #SHOWS LIST OF FRIENDS
    friends_listTemp = list(inboxTemp.values()) #SHOWS LIST OF FRIENDS

   
    
    # #Checks to makes sure friend is in list
    # if not friends_list: #If the user has no friends yet
    #     print("You don't have any friends yet.")
    #     return

    #Displays the all the friends in the friends list
    for indexTrue, friend_username in enumerate(friends_list, start=1):
        friend_full_name = accounts[friend_username].get('full_name', 'No name available')
        
        #Checks if user pick is a friend
        if friendPick == friend_username:
            flagAssign(1)
            #flag = 1 #Verifys that user's pick is a friend

    #Assigns the index of chosen friend to selection variable
    if flag == 1:
        selection = str(indexTrue)

    #Runs through the temp list of names for recipent
    for i in friends_listTemp:
        for j in i:
            if friendPick == j:
                #flag = 2
                flag = flagAssign(2)

    if flag == 2:
        message = input("Enter your message: ") #Asks user to submit their message

        #Saves the message in recipient's inbox
        saveMessage(friendPick, username, message, 0)
        print("Message sent successfully.")
        return

    if flag == 0: #If the user's pick is not a friend then the friends list will be shown
        print ("You are not friends with that person.")

        #Checks if list empty
        if len(friends_list) == 0:
            print("Make new connections to message!\n")
            return
         
        print("Here is your Friend's List\n")
        for index, friend_username in enumerate(friends_list, start=1):
            friend_full_name = accounts[friend_username].get('full_name', 'No name available')      
            print(f"{index}. {friend_full_name} ({friend_username})") 
    
        #Asks the user to select a friend from the list
        selection = input("Enter the number of the friend you want to send a message to: ")

    if selection.isdigit():
        selection = int(selection)
        if 1 <= selection <= len(friends_list):
            recipient_username = friends_list[selection - 1]
            message = input("Enter your message: ") #Asks user to submit their message

            #Checks if recipient is a friend
            if recipient_username in friends_list:

                #Saves the message in recipient's inbox
                saveMessage(recipient_username, username, message, 0)
                print("Message sent successfully.")

            else:
                print("I'm sorry, you are not friends with that person.")

        else:
            print("Invalid selection.")

    else:
        print("Invalid input.")



#Function to save a message in the recipient's inbox (used in sendMessage function)
def saveMessage(recipient_username, sender_username, message, plusNum):
     #Loads the accounts dictionary and checks for error
    try:
        accounts = np.load("accounts.npy", allow_pickle=True).item()

    except FileNotFoundError:
        print("Accounts file not found. Make sure you have run the account creation process.")
        return

    #Loads (or creates) an inbox dictionary just for each recipients inbox
    try:
        inbox = np.load(f"{recipient_username}_inbox.npy", allow_pickle=True).item()

    except FileNotFoundError:
        inbox = {}

    #Creates an list inside the recipient inbox to store messages from that sender if it doesn't already exist
    if sender_username not in inbox:
        inbox[sender_username] = []

    #Adds the message to the list
    inbox[sender_username].append(message)

    #Stores list in a dictionary in a numpy file
    np.save(f"{recipient_username}_inbox.npy", inbox)

    #Checks what user type sent this message (plus = 1, standard = 0)
    userType = plusNum
    flag = 0

    #Puts plus user on a temp list so person they sent a message to can respond to them
    friendsRecList = accounts[recipient_username].get('friends', []) #SHOWS LIST OF FRIENDS
    for index, friend_username in enumerate(friendsRecList, start=1):
        friend_full_name = accounts[friend_username].get('full_name', 'No name available')
        
        #Checks if user pick is a friend
        if sender_username == friend_username:
            flag += 1 #Verifys that user's pick is a friend

    #A temporary list is made that stores the plus user who sent the message so the receiver can still answer them
    if flag == 0 and userType == 1: 

        #Loads (or creates) a temp inbox dictionary
        try:
            inboxTemp = np.load(f"{recipient_username}_temp_inbox.npy", allow_pickle=True).item()

        except FileNotFoundError:
            inboxTemp = {}

        #Creates an list inside the recipient inbox to store messages from that sender if it doesn't already exist
        if recipient_username not in inboxTemp:
            inboxTemp[recipient_username] = []
            
        inboxTemp[recipient_username].append(sender_username)

        #Stores list in a dictionary in a numpy file
        np.save(f"{recipient_username}_temp_inbox.npy", inboxTemp)
        




#Function to view messages in the user's inbox
def viewInbox(username):
    try:
        inbox = np.load(f"{username}_inbox.npy", allow_pickle=True).item()
    except FileNotFoundError:
        inbox = {}

    if inbox:
        print("Your Inbox:")
        for sender, messages in inbox.item():
            print(f"From: {sender}")
            for message in messages:
                print(f"- {message}")
    else:
        print("Your inbox is empty.")


#Function to delete a message from the user's inbox
def deleteMessage(username):
    try:
        inbox = np.load(f"{username}_inbox.npy", allow_pickle=True).item()
    except FileNotFoundError:
        inbox = {}

    if inbox:
        print("Your Inbox:")
        for sender, messages in inbox.item():
            print(f"From: {sender}")
            for index, message in enumerate(messages, start=1):
                print(f"{index}. {message}")

            selection = input("Enter the number of the message you want to delete (0 to cancel): ")

            if selection.isdigit():
                selection = int(selection)
                if 0 < selection <= len(messages):
                    del inbox[sender][selection - 1]

                    #Updates the user's inbox
                    np.save(f"{username}_inbox.npy", inbox)
                    print("Message deleted successfully.")

                elif selection == 0:
                    print("Operation cancelled.")
                    
                else:
                    print("Invalid selection.")
            else:
                print("Invalid input.")
    else:
        print("Your inbox is empty.")


# Function to clear the inbox after reading messages
def clearInbox(username):
    np.save(f"{username}_inbox.npy", {})

