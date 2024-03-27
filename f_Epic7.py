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
def manageMessage(username):
    #Displays a menu option for users
    print("1. Send a message")
    print("2. View your messages")
    print("3. Delete Message from Inbox \n")

    messageChoice = int(input("Please select 1 or 2 or 3 from the menu options: "))
    print("\n")

    #User can send a message when option 1 is chosen
    if messageChoice == 1:
        sendMessage(username)

    #User can view their own inbox when option 2 is chosen    
    elif messageChoice == 2:
        viewInbox(username)

    #User deletes their inbox
    elif messageChoice == 3:
        deleteMessage(username)
    return


#Function that enables a message to be sent to a friend
def sendMessage(username):

    #Loads the accounts dictionary and checks for error
    try:
        accounts = np.load("accounts.npy", allow_pickle=True).item()

    except FileNotFoundError:
        print("Accounts file not found. Make sure you have run the account creation process.")
        return

    #Asks the user to select a friend to send a message to
    print("Select a friend to send a message:")
    friends_list = accounts[username].get('friends', [])

    #Checks to makes sure friend is in list
    if not friends_list: #If the user has no friends yet
        print("You don't have any friends yet.")
        return

    #Displays the all the friends in the friends list
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
                saveMessage(recipient_username, username, message)

                print("Message sent successfully.")
            else:
                print("I'm sorry, you are not friends with that person.")
        else:
            print("Invalid selection.")
    else:
        print("Invalid input.")



#Function to save a message in the recipient's inbox (used in sendMessage function)
def saveMessage(recipient_username, sender_username, message):
    try:
        inbox = np.load(f"{recipient_username}_inbox.npy", allow_pickle=True).item()
    except FileNotFoundError:
        inbox = {}

    if sender_username not in inbox:
        inbox[sender_username] = []

    inbox[sender_username].append(message)

    np.save(f"{recipient_username}_inbox.npy", inbox)



#Function to view messages in the user's inbox
def viewInbox(username):
    try:
        inbox = np.load(f"{username}_inbox.npy", allow_pickle=True).item()
    except FileNotFoundError:
        inbox = {}

    if inbox:
        print("Your Inbox:")
        for sender, messages in inbox.items():
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
        for sender, messages in inbox.items():
            print(f"From: {sender}")
            for index, message in enumerate(messages, start=1):
                print(f"{index}. {message}")

            selection = input("Enter the number of the message you want to delete (0 to cancel): ")

            if selection.isdigit():
                selection = int(selection)
                if 0 < selection <= len(messages):
                    del inbox[sender][selection - 1]
                    print("Message deleted successfully.")
                elif selection == 0:
                    print("Operation cancelled.")
                else:
                    print("Invalid selection.")
            else:
                print("Invalid input.")
    else:
        print("Your inbox is empty.")
