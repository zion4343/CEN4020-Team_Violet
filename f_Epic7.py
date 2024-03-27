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
# Function to manage messages
def manageMessage(username):
    print("Select an option:")
    print("1. Send a message")
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
        
    inbox[sender_username].append(message_content)
    
    np.save(f"{receiver_username}_inbox.npy", inbox)

# Function to check the inbox
def checkInbox(username):
    try:
        inbox = np.load(f"{username}_inbox.npy", allow_pickle=True).item()
    except FileNotFoundError:
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

