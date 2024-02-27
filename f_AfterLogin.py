'''
The functions support After Log-in
'''

'''
Import
'''
import numpy as np

'''
Functions
'''

#This function to gives additional options after login is successful
def addOptions(username):
    print("\n")
    print("Welcome! What would you like to do?")
    print("1. Search for a job/internship")
    print("2. Find someone you know")
    print("3. Learn a new skill")
    print("4. Guest Controls")
    choice = input("Enter your choice: ")

    if choice == "1":
        print("Would you like to search or post a job/internship?")
        print("1. Search")
        print("2. Post a job")
        
        choiceJob = input("Enter your job choice: ")
        
        if choiceJob == "1":
            # Load job postings for searching
            loadJobPostings()
            print("Here are the available job postings:")
            for index, job in enumerate(jobPostings, start=1):
                print(f"Job {index}: {job['title']} - {job['description']} - {job['employer']} - {job['location']} - {job['salary']}")
                
        elif choiceJob == "2":            
            postJob(username)

    elif choice == "2":
        print("Find someone you know option is currently under construction.")

    elif choice == "3":
        print("Here are 5 skills you can learn:")
        print("1. Programming")
        print("2. Prompt Engineering")
        print("3. 3D Modeling & Simulation")
        print("4. Data Analysis")
        print("5. Language Learning")
        print("6. Show my Network")
        print("7. Return to the previous level. . .")

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
        elif choiceSkill == "6":
            showMyNetwork(username)
            disconnectOption = input("Would you like to disconnect from anyone in your network? (yes/no): ")
            if disconnectOption.lower() == "yes":
                disconnectFromFriendOption(username)
        else:
            print("7. Returning to the previous level. . .")
            addOptions(username)
    elif choice == "4":
        guestControls(username)
    else:
        print("Invalid choice.")

    return 1

# Function to display connected friends
def showMyNetwork(username):
    if username in accFriends:
        print("Your network:")
        for friend in accFriends[username]:
            print(friend)
    else:
        print("You haven't connected with anyone yet.")

# Function to handle disconnection from friends
def disconnectFromFriend(username, friend_to_disconnect):
    if username in accFriends and friend_to_disconnect in accFriends[username]:
        accFriends[username].remove(friend_to_disconnect)
        if friend_to_disconnect in accFriends and username in accFriends[friend_to_disconnect]:
            accFriends[friend_to_disconnect].remove(username)
        print(f"You have disconnected from {friend_to_disconnect}.")
    else:
        print(f"You are not connected with {friend_to_disconnect}.")



# Function to post a job
def postJob(username):
    loadJobPostings()
    if len(jobPostings) >= 5:
        print("Maximum number of job postings reached.")
        return 0

    print("Posting a job:")
    title = input("Enter job title: ")
    description = input("Enter job description: ")
    employer = input("Enter employer name: ")
    location = input("Enter job location: ")
    salary = input("Enter job salary: ")

    job = {
        "title": title,
        "description": description,
        "employer": employer,
        "location": location,
        "salary": salary,
        "posted_by": username
    }

    jobPostings.append(job)
    print("Job posted successfully.")

    # Save the updated job postings
    np.save("job_postings.npy", jobPostings)
    
    return 1

# Load job postings
def loadJobPostings():
    global jobPostings
    try:
        jobPostings = np.load("job_postings.npy", allow_pickle=True)
    except FileNotFoundError:
        jobPostings = []

# Dictionary to store user settings
user_settings = {}

# Function to load user settings
def loadUserSettings():
    global user_settings
    try:
        user_settings = np.load("user_settings.npy", allow_pickle=True).item()
    except FileNotFoundError:
        user_settings = {}

# Call this function at the beginning of the main program
loadUserSettings()

# Function to toggle features on and off
def toggleFeature(username, feature):
    if username not in user_settings:
        user_settings[username] = {"email": True, "sms": True, "targeted_advertising": True}

    if user_settings[username][feature]:
        user_settings[username][feature] = False
        print(f"{feature.capitalize()} notifications have been turned off.")
    else:
        user_settings[username][feature] = True
        print(f"{feature.capitalize()} notifications have been turned on.")

    # Save the updated user settings
    np.save("user_settings.npy", user_settings)

        
# Function to handle guest controls
def guestControls(username):
    print("\nGuest Controls:")
    print("1. Email Notifications")
    print("2. SMS Notifications")
    print("3. Targeted Advertising")
    print("4. Return to the previous level. . .")

    choice = input("Enter your choice: ")

    if choice == "1":
        toggleFeature(username, "email")
    elif choice == "2":
        toggleFeature(username, "sms")
    elif choice == "3":
        toggleFeature(username, "targeted_advertising")
    elif choice =="4":
        addOptions(username)
    else:
        print("Invalid choice.")
        guestControls(username)
        
        
# Function to display connected friends
def showMyNetwork(username):
    if username in accFriends:
        print("Your network:")
        for friend in accFriends[username]:
            print(friend)
    else:
        print("You haven't connected with anyone yet.")

# Function to handle disconnection from friends
def disconnectFromFriend(username, friend_to_disconnect):
    if username in accFriends and friend_to_disconnect in accFriends[username]:
        accFriends[username].remove(friend_to_disconnect)
        accFriends[friend_to_disconnect].remove(username)
        print(f"You have disconnected from {friend_to_disconnect}.")
    else:
        print(f"You are not connected with {friend_to_disconnect}.")