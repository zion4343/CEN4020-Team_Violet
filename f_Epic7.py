'''
The functions developed in Epic 7
'''

'''
Import
'''
import numpy as np
from f_BeforeLogin import accounts
import f_AfterLogin as AL

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





# Function to manage messages
def manageMessage(username):
    print("Select an option:")
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

    print("2. Check inbox")
    
    message_choice = input("Enter your choice: ")
    
    if message_choice == "1":
        sendMessage(username)
    elif message_choice == "2":
        checkInbox(username)
    else:
        print("Invalid choice.")

# Function to send a message
def sendMessage(sender_username):
    AL.displayFriendsList(sender_username)
    receiver_username = input("Enter the username of the receiver: ")
    
    # Check if receiver exists
    if receiver_username not in accounts:
        print("User not found.")
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

    
    # Check if sender and receiver are friends
    if receiver_username not in accounts[sender_username]["friends"]:
        print("I'm sorry, You are not friends with this person.")
        return
    
    message_content = input("Enter your message: ")
    
    # Save the message to the receiver's inbox
    saveMessage(receiver_username, sender_username, message_content)
    
    print("Message sent successfully.")

# Function to save a message to the receiver's inbox
def saveMessage(receiver_username, sender_username, message_content):
    try:
        inbox = np.load(f"{receiver_username}_inbox.npy", allow_pickle=True).item()
    except FileNotFoundError:
        inbox = {}
        
    if sender_username not in inbox:
        inbox[sender_username] = []
        
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

    inbox[sender_username].append(message_content)
    
    np.save(f"{receiver_username}_inbox.npy", inbox)

# Function to check the inbox
def checkInbox(username):
    try:
        inbox = np.load(f"{username}_inbox.npy", allow_pickle=True).items()
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

        print("No messages in your inbox.")
        return
    
    if not inbox:
        print("No messages in your inbox.")
        return
    
    print("Messages in your inbox:")
    for sender, messages in inbox.items():
        print(f"From: {sender}")
        for message in messages:
            print(f"- {message}")
            
    # Clear the inbox after reading messages
    clearInbox(username)

# Function to clear the inbox after reading messages
def clearInbox(username):
    np.save(f"{username}_inbox.npy", {})

