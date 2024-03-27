'''
The functions support After Log-in
'''
'''
Import
'''
import numpy as np
import f_BeforeLogin as b_login
from f_BeforeLogin import accounts
import f_Epic6 as epic6
import f_Epic7 as epic7


'''
Functions
'''


#This function to gives additional options after login is successful
def addOptions(username):
  print("\n")
  print("Welcome! What would you like to do?")
  print("\n")
  print("1. Search for a job/internship")
  print("2. Find someone you know")
  print("3. Learn a new skill")
  print("4. InCollege Important Links")
  print("5. Manage friend requests")
  print("6. Create your Personal Profile")
  print("7. Remove Job")
  print("8. Manage Messages")
  print("\n")
  
  #Check for the pending friend request
  checkPendingFriendRequest(username)
  #Check for deleted jobs user applied for
  checkDeletedJobs(username)
  
  choice = input("Enter your choice: ")

  if choice == "1":
    print("Would you like to search or post a job/internship?")
    print("1. Search")
    print("2. Post a job")

    choiceJob = input("Enter your job choice: ")

    if choiceJob == "1":
      # Load job postings for searching
      while(1):
        loadJobPostings()
        print("\nHere are the available job postings:")
        for index, job in enumerate(jobPostings, start=0):
          print(
              f"Job {index + 1}: {job['title']}"
          )
        # Ask user to choose the choice  
        jobNumber = int(input("Choose the job number you want to see the details (If you want to quit the Job Posting list, enter 0): "))
        while(len(jobPostings) < jobNumber | jobNumber < 0):
          jobNumber = int(input("Invalid Input, Choose the job you want to see the details: "))
        #If user choose 0, return to the Option list for AfterLogin
        if(jobNumber == 0):
          addOptions(username)
          return 1
        #Show the details of the selected job
        else:
          jobNumber = jobNumber - 1
          print("\nThat's the details of the job")
          print(f"Title: {jobPostings[jobNumber]['title']}")
          print(f"Description: {jobPostings[jobNumber]['description']}")
          print(f"Employer: {jobPostings[jobNumber]['employer']}") 
          print(f"Location: {jobPostings[jobNumber]['location']}")
          print(f"Salary: {jobPostings[jobNumber]['salary']}\n")
          
          print("1: Apply for a job")
          print("2: Save the job and Return to the list of job posting")
          print("3: Return to the list of job posting")

          userSelect = int(input("Choose your option: "))
          while(userSelect < 1 | userSelect > 3):
            userSelect = int(input("Invalid Input, Choose your option: "))
          if(userSelect == 1):
            print("")
            epic6.applyForJob(username, jobPostings, jobNumber)
          elif(userSelect == 2):
            print("")
            epic6.saveJob(username, jobPostings, jobNumber)
          print("")
          print("Returning to the list of Job Posting...")

    elif choiceJob == "2":
      postJob(username)

  elif choice == "2":
    #print("Find someone you know option is currently under construction.")
    searchAndConnect(username)
    addOptions(username)
    return

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
        print("The Programming option is currently under construction.\n")
        addOptions(username)
        return

      elif choiceSkill == "2":
        print("The Prompt Engineering option is currently under construction.\n")
        addOptions(username)
        return

      elif choiceSkill == "3":
        print("The 3D Modeling & Simulation option is currently under construction.\n")
        addOptions(username)
        return

      elif choiceSkill == "4":
        print("The Data Analysis option is currently under construction.\n")
        addOptions(username)

      elif choiceSkill == "5":
        print("The Language Learning option is currently under construction.\n")
        addOptions(username)
        
      elif choiceSkill == "6":
        showMyNetwork(username)
        addOptions(username)
        return
      
      else:
        print("7. Returning to the previous level. . .")
        addOptions(username)

  elif choice == "4":
    goingBackLoggedIn = handleImportantLinks(username)

    #Checks if the user wants to come back to main screen after clicking InCollege Important Links
    if goingBackLoggedIn == 0:
      addOptions(username)

    else:  #Or go back to Important Links option
      handleImportantLinks()

  elif choice == "5":
    manageFriendRequests(username)
    addOptions(username)
      
  elif choice == "6":
    createProfile(username)
    addOptions(username)
  
  elif choice == "7":
    removeJob(username)
    addOptions(username)
  
  elif choice == "8":
    epic7.manageMessage(username)
    addOptions(username)
    
  else:
    print("Invalid choice.")
    addOptions(username)  

  return 1

# Function to post a job
def postJob(username):
  jobPostings = loadJobPostings()
  if len(jobPostings) > 10:
    print("Maximum number of job postings reached.")
    return 0

  print("Posting a job:")
  title = input("Enter job title: ")
  description = input("Enter job description: ")
  employer = input("Enter employer name: ")
  location = input("Enter job location: ")
  salary = input("Enter job salary: ")
  
  job_id = len(jobPostings) + 1

  job = {
      "job_id": job_id,
      "title": title,
      "description": description,
      "employer": employer,
      "location": location,
      "salary": salary,
      "posted_by": username,
      "applied_by": {"appliedUser":[], "graduationDate":[], "startWorkingDate":[], "reason":[]}, #The Directionary that store the info about the Applied User
      "saved_by": {"savedUser":[]}
  }

  job = np.array(job)  #Converts job to a numpy array
  jobPostings = np.concatenate((jobPostings, np.expand_dims(job, axis=0)),
                               axis=0)  #Concatenates job array

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

  return jobPostings


# Dictionary to store user settings
user_settings = {}


# Function to load user settings
def loadUserSettings():
  global user_settings
  try:
    user_settings = np.load("user_settings.npy", allow_pickle=True).item()
  except FileNotFoundError:
    user_settings = {}


# Function to toggle features on and off
def toggleFeature(username, feature):
  if username not in user_settings:
    user_settings[username] = {
        "email": True,
        "sms": True,
        "targeted_advertising": True
    }

  if user_settings[username][feature]:
    user_settings[username][feature] = False
    print(f"{feature.capitalize()} notifications have been turned off.")
  else:
    user_settings[username][feature] = True
    print(f"{feature.capitalize()} notifications have been turned on.")

  # Save the updated user settings
  np.save("user_settings.npy", user_settings)
  return 1


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
    addOptions(username)
  elif choice == "2":
    toggleFeature(username, "sms")
    addOptions(username)
  elif choice == "3":
    toggleFeature(username, "targeted_advertising")
    addOptions(username)
  elif choice == "4":
    addOptions(username)
  else:
    print("Invalid choice.")
    guestControls(username)
  return 1


#Verifies if the user is inputting a number in the acceptable range (a more general purpose one needs to be made)
def inputValidation(prompt, valid_options):
  while True:
    try:
      user_input = int(input(prompt))
      if user_input in valid_options:
        return user_input
      print("Invalid input. Please try again.")
    except ValueError:
      print("Invalid input. Please enter a number.")


#Displays all the InCollege Important Links (if 5 is chosen)
def displayImportantLinks():
  print("\nInCollege Important Links:")
  print("1. Copyright Notice")
  print("2. About")
  print("3. Accessibility")
  print("4. User Agreement")
  print("5. Privacy Policy")
  print("6. Cookie Policy")
  print("7. Copyright Policy")
  print("8. Brand Policy")
  print("9. Guest Controls")
  print("10. Languages")
  print("0. Back")


#Gives user the chance to go back up a level in the menu or exit entirely#
def userImportantExit(userChoice, username):
  if userChoice == 1:
    handleImportantLinks(username)

  else:
    return 0


#Names the files to be printed according to user selection
def returnFilename(number):
  if number == 1:
    file = "Copyright_Notice.txt"

  elif number == 2:
    file = "About.txt"

  elif number == 3:
    file = "About.txt"

  elif number == 4:
    file = "User_Agreement.txt"

  elif number == 5:
    file = "Privacy_Policy.txt"

  elif number == 6:
    file = "Cookie_Policy.txt"

  elif number == 7:
    file = "Copyright_Policy.txt"

  elif number == 8:
    file = "Brand_Policy.txt"

  return file


###Addded after Epic 3: Menus###


# Function to read user settings from a file
def readUserLangSettings():
  try:
    with open("Language_Choice.txt", "r") as file:
      language = file.read().strip()

  #If the file doesn't exist, it will return default language (English)
  except FileNotFoundError:
    language = "English"

  return language


#Function to save user language choice to a text file
def saveUserLangSettings(language):
  with open("Language_Choice.txt", "w") as file:
    file.write(language)


#Function to deal with the language selection
def langSelect():
  #has the user select their language preference
  print("Select your preferred language: \n")
  print("1. English\n")
  print("2. Spanish\n")
  langChoice = input("\nEnter your choice: ")

  #Sets the language choice to 1 if English and 2 if Spanish
  if langChoice == "1":
    return "English"

  elif langChoice == "2":
    return "Spanish"

  else:
    print("Invalid choice")
    return None


#Function to display file content
def getFile(filename):
  with open(filename, 'r') as file:
    content = file.read()
  print(content)


#Takes the selection of user in main.py and if it is 5 (Important Links, then it displays the Important Links menu)
def handleImportantLinks(username):

  #This is to display the InCollege Important Links before the user is logged in
  displayImportantLinks()
  back = 0

  #User chooses between 0 and 10 for various options
  importantLinkChoice = inputValidation(
      "\n\nPlease select the number corresponding to your choice: ",
      list(range(11)))

  #Displays the content for every option chosen
  if importantLinkChoice == 1:

    print("\nCopyright Notice\n")
    filename = returnFilename(importantLinkChoice)
    getFile(filename)

    #Gives user the chance to go back up a level in the menu or exit entirely
    userImportantReturn = int(
        input(
            "Press 1 to return to previous menu or press 2 to exit entirely: ")
    )
    userImportantExit(userImportantReturn, username)

  elif importantLinkChoice == 2:

    print("\nAbout\n")
    filename = returnFilename(importantLinkChoice)
    getFile(filename)

    #Gives user the chance to go back up a level in the menu or exit entirely
    userImportantReturn = int(
        input(
            "Press 1 to return to previous menu or press 2 to exit entirely: ")
    )
    userImportantExit(userImportantReturn, username)

  elif importantLinkChoice == 3:
    print("\nAccessibility\n")
    filename = returnFilename(importantLinkChoice)
    getFile(filename)

    #Gives user the chance to go back up a level in the menu or exit entirely
    userImportantReturn = int(
        input(
            "Press 1 to return to previous menu or press 2 to exit entirely: ")
    )
    userImportantExit(userImportantReturn, username)

  elif importantLinkChoice == 4:
    print("\nUser Agreement\n")
    filename = returnFilename(importantLinkChoice)
    getFile(filename)

    #Gives user the chance to go back up a level in the menu or exit entirely
    userImportantReturn = int(
        input(
            "Press 1 to return to previous menu or press 2 to exit entirely: ")
    )
    userImportantExit(userImportantReturn, username)

  elif importantLinkChoice == 5:
    print("\nPrivacy Policy\n")
    filename = returnFilename(importantLinkChoice)
    getFile(filename)

    #Gives user the chance to go back up a level in the menu or exit entirely
    userImportantReturn = int(
        input(
            "Press 1 to return to previous menu or press 2 to exit entirely: ")
    )
    userImportantExit(userImportantReturn, username)

  elif importantLinkChoice == 6:
    print("\nCookie Policy\n")
    filename = returnFilename(importantLinkChoice)
    getFile(filename)

    #Gives user the chance to go back up a level in the menu or exit entirely
    userImportantReturn = int(
        input(
            "Press 1 to return to previous menu or press 2 to exit entirely: ")
    )
    userImportantExit(userImportantReturn, username)

  elif importantLinkChoice == 7:
    print("\nCopyright Policy\n")
    filename = returnFilename(importantLinkChoice)
    getFile(filename)

    #Gives user the chance to go back up a level in the menu or exit entirely
    userImportantReturn = int(
        input(
            "Press 1 to return to previous menu or press 2 to exit entirely: ")
    )
    userImportantExit(userImportantReturn, username)

  elif importantLinkChoice == 8:
    print("\nBrand Policy\n")
    filename = returnFilename(importantLinkChoice)
    getFile(filename)

    #Gives user the chance to go back up a level in the menu or exit entirely
    userImportantReturn = int(
        input(
            "Press 1 to return to previous menu or press 2 to exit entirely: ")
    )
    userImportantExit(userImportantReturn, username)

  elif importantLinkChoice == 9:
    print("\nGuest Controls\n")
    guestControls(username)

    #Gives user the chance to go back up a level in the menu or exit entirely
    userImportantReturn = int(
        input(
            "Press 1 to return to previous menu or press 2 to exit entirely: ")
    )
    userImportantExit(userImportantReturn, username)

  elif importantLinkChoice == 10:
    print("\nLanguages\n")

    # Read user language choice
    userLanguage = readUserLangSettings()

    print("Welcome!")
    print("Your current language setting:", userLanguage)

    print(
        "Please select an option:\n1. Select a new language setting \n2. Keep current language setting\n"
    )
    option = input("Enter your choice: ")

    #If the user wants to change the language setting
    if option == "1":
      newLanguage = langSelect()

      #When user language choice is updated successfully
      if newLanguage:
        print("\nLanguage updated successfully!")
        saveUserLangSettings(newLanguage)

    #User does not change language setting
    elif option == "2":
      print("Your current language setting is still: ", userLanguage)

    else:
      print("Invalid option")

    #Gives user the chance to go back up a level in the menu or exit entirely
    userImportantReturn = int(
        input(
            "Press 1 to return to previous menu or press 2 to exit entirely: ")
    )
    userImportantExit(userImportantReturn, username)

  elif importantLinkChoice == 0:
    return 0

  return back

# Function searches for a user based on either last name, major or university and allows user to connect
# with the user if found
def searchAndConnect(username):
    # Read the dictionary of user information
    b_login.readDictionary()

    # Prompt the user to choose the search criteria
    print("Search for a user by:")
    print("1. Last Name")
    print("2. Major")
    print("3. University")
    
    search_criteria = input("Enter your choice: ")

    if search_criteria == "1":
        # Search by last name
        last_name = input("Enter the last name of the user you want to connect with: ")
        matching_users = findUsersByLastName(last_name)
    elif search_criteria == "2":
        # Search by major
        major = input("Enter the major of the user you want to connect with: ")
        matching_users = findUsersByMajor(major,username)
    elif search_criteria == "3":
        # Search by university
        university = input("Enter the university of the user you want to connect with: ")
        matching_users = findUsersByUniversity(university,username)
    else:
        print("Invalid choice.")
        return

    # If no matching users found, inform the user and return
    if not matching_users:
        print("No users found with the provided criteria.")
        return

    # Display matching users and prompt the user to select a user to send a friend request
    print("Matching Users:")
    # Number the users so that current user is able to choose from the list of matching users
    for index, user in enumerate(matching_users, start=1):
        print(f"{index}. {user}")

    # Prompt the user to select a user to send a friend request to
    selection = input("Enter the number of the user you want to send a friend request to (0 to cancel): ")
    if selection.isdigit():
        selection = int(selection)
        if 0 < selection <= len(matching_users):
            selected_user = matching_users[selection - 1]
            sendFriendRequest(username, selected_user)
            print(f"Friend request sent to {selected_user}.")
        elif selection == 0:
            print("Operation cancelled.")
        else:
            print("Invalid selection.")
    else:
        print("Invalid input.")
       
# Function to find users by last name
def findUsersByLastName(last_name):
    # Load the full names and usernames from the file
    try:
        fullnames = np.load("fullnames.npy", allow_pickle=True).item()
    except FileNotFoundError:
        print("Error: Fullnames file not found.")
        return []

    # Search for users based on the last name
    matching_users = []
    for user, fullname in fullnames.items():
        # Check if the last name matches
        if last_name.lower() in fullname.lower():
            matching_users.append(user)

    return matching_users

# Function to find users by major
def findUsersByMajor(major,current_username):
    #Load the accounts data from .npy file
    accounts = np.load('accounts.npy', allow_pickle=True).item()
    
    # Search for users by major, excluding the current user
    matching_users_full_names = [
        details['full_name'] for username, details in accounts.items() 
        if details['major'].lower() == major.lower() and username != current_username
    ]
    
    return matching_users_full_names

# Function to find users by university 
def findUsersByUniversity(university,current_username):
    #Load the accounts data from .npy file
    accounts = np.load('accounts.npy', allow_pickle=True).item()
    
    # Search for users by major, excluding the current user
    matching_users_full_names = [
        details['full_name'] for username, details in accounts.items() 
        if details['university'].lower() == university.lower() and username != current_username
    ]
    
    return matching_users_full_names

# Finding which user is currently logged in
def getLoggedInUserFullName():
    # Ensure that the 'username' variable is accessible within this function
    global username

    # Check if the 'username' variable is defined and not empty
    if 'username' in globals() and username in accounts:
        return accounts[username]['full_name']
    else:
        return "No user is currently logged in."

#The function to check pending friend request
def checkPendingFriendRequest(username):
  loadFriendRequest()
  
  #Checks if username is present in friends_request.npy
  for all in pending_requests.keys():
    if username != pending_requests.keys():
      return
        

  ##FIXED the issue below using the above for statement
  NoPendingRequest = len(pending_requests[username]) ##Causes an error(KeyError: 'odanobu' for example) when user has no pending friend request (ie, username not present in numpy file)

  # Check if there are pending requests
  if (NoPendingRequest) > 0:
    print("You have pending friend request!")
  return

def loadFriendRequest():
  global pending_requests
  try:
    pending_requests = np.load("friend_request.npy", allow_pickle = True).item()
  except FileNotFoundError:
    pending_requests = {}
    
  return pending_requests

# Function to send a friend request to another user
def sendFriendRequest(sender_username, receiver_fullname):
    # Load the accounts dictionary
    try:
        accounts = np.load("accounts.npy", allow_pickle=True).item()
    except FileNotFoundError:
        print("Accounts file not found. Make sure you have run the account creation process.")
        return

    # Debug print to check the loaded accounts structure
    #print("Loaded accounts:", accounts)

    # Retrieve the actual username using the full name
    receiver_username = None
    for username, details in accounts.items():
        # Use the 'full_name' key for comparison
        if details['full_name'].lower().strip() == receiver_fullname.lower().strip():
            receiver_username = username
            break


    if receiver_username is None:
        print("Receiver not found. Make sure the full name is correct.")
        return

    # Continue with the friend request process using receiver_username...
    
    try:
        # Load existing friend requests if file exists
        existing_requests = np.load("friend_request.npy", allow_pickle=True)
    except FileNotFoundError:
        # If file does not exist, start with an empty dic
        existing_requests = {}
        existing_requests[receiver_username] = [{sender_username: "Pending"}]
    
    # Add the new friend request
    
    #existing_requests.append({"Sender": sender_username, "Status": "Pending"})
    existing_requests[receiver_username].append({sender_username: "Pending"})
    
    # Save the updated list back to the file
    np.save("friend_request.npy", existing_requests)

    # print(f"Friend request sent to {receiver_username}.")


def manageFriendRequests(username):
    # Load pending friend requests
    loadFriendRequest()
    
    senderUsername = []
    
    NoPendingRequest = len(pending_requests[username])
    # Check if there are pending requests
    if (NoPendingRequest) > 0:
        print("Pending Friend Requests:")
        list_of_requests = pending_requests[username]
        # Display each request with a number
        i = 0
        while(i < NoPendingRequest):
          for sender, status in list_of_requests[i].items():
            print(f"{i+1}. Sender: {sender}, Status: {status}")
            senderUsername.append(sender)
            i = i + 1

        # Prompt the user to choose a request to accept or reject
        user_choice = input("Enter the number of the friend request you want to respond to (or type 'cancel' to exit): ")
        
        # Validate user input
        if user_choice.isdigit():
            choice_index = int(user_choice) - 1
            if 0 <= choice_index < len(pending_requests):
                # Further prompt for accept or reject
                action = input("Do you want to accept (A) or reject (R) this friend request?: ").upper()
                if action == "A":
                    # Call function to accept friend request
                    #accept_friend_request(username, pending_requests[choice_index]['Sender'])
                    accept_friend_request(username, senderUsername[choice_index])
                    pending_requests[username].pop(choice_index)
                    print("Accept the friend request!")
                    np.save("friend_request.npy", pending_requests)
                    
                elif action == "R":
                    # Simply remove the request from the list to "reject" it
                    #del pending_requests[choice_index]
                    pending_requests[username].pop(choice_index)
                    print("Friend request rejected.")
                    # Save the updated list of pending requests back to the file
                    np.save("friend_request.npy", pending_requests)
                else:
                    print("Invalid choice. Please enter 'A' to accept or 'R' to reject.")
            else:
                print("Invalid selection. Please enter a valid request number.")
        elif user_choice.lower() == 'cancel':
            print("Operation cancelled.")
        else:
            print("Invalid input. Please enter a number or 'cancel' to exit.")
    else:
        print("No pending friend requests.")


def accept_friend_request( user_receiving, user_requesting):
    accounts = np.load('accounts.npy', allow_pickle=True).item()
    
    # Add user_requesting to user_receiving's friends list
    if user_requesting not in accounts[user_receiving]['friends']:
        accounts[user_receiving]['friends'].append(user_requesting)
    
    # Add user_receiving to user_requesting's friends list
    if user_receiving not in accounts[user_requesting]['friends']:
        accounts[user_requesting]['friends'].append(user_receiving)
    
    # Save the updated accounts back to the file
    np.save('accounts.npy', accounts)

# Function to show a user's list of friends
def showMyNetwork(username):
    accounts = np.load('accounts.npy', allow_pickle=True).item()
    
    if username in accounts and 'friends' in accounts[username]:
        friends_list = accounts[username]['friends']
        if friends_list:
            print(f"{username}'s network:")
            for index, friend_username in enumerate(friends_list, start=1):
                friend_full_name = accounts[friend_username].get('full_name', 'No name available')
                print(f"{index}. {friend_full_name}")
            
            # Ask if the user wants to disconnect from a friend
            disconnect_choice = input("Do you want to disconnect from a friend? Enter the number (or 'n' to skip): ")
            if disconnect_choice.isdigit():
                disconnectFromFriend(username, int(disconnect_choice), accounts)
            elif disconnect_choice.lower() == 'n':
                print("No changes made to your network.")
            else:
                print("Invalid input.")
        else:
            print("You haven't connected with anyone yet.")
    else:
        print("No friends to show or user not found.")

# Function to handle disconnection from friends
def disconnectFromFriend(username, friend_index, accounts):
    friends_list = accounts[username].get('friends', [])
    
    if 1 <= friend_index <= len(friends_list):
        # Adjust the index since list indices start at 0
        friend_username = friends_list[friend_index - 1]
        
        # Remove each user from the other's friend list
        accounts[username]['friends'].remove(friend_username)
        accounts[friend_username]['friends'].remove(username)
        
        # Save the updated accounts back to the file
        np.save('accounts.npy', accounts)
        
        print(f"You have disconnected from {accounts[friend_username].get('full_name', 'a friend')}.")
    else:
        print("Invalid selection. No changes made.")

'''
# Function to find users by last name
def findUsersByLastName(last_name):
    # Load the full names and usernames from the file
    try:
        fullnames = np.load("fullnames.npy", allow_pickle=True).item()
    except FileNotFoundError:
        print("Error: Fullnames file not found.")
        return []

    # Search for users based on the last name
    matching_users = []
    for user, fullname in fullnames.items():
        # Check if the last name matches
        if last_name.lower() in fullname.lower():
            matching_users.append(user)

    return matching_users
'''

# Function to create or update a personal profile
def createProfile(username):
  try:
    # Load existing profile if it exists
    profile = np.load(f"{username}_profile.npy", allow_pickle=True).item()
    print("Existing Profile Found. You can update it.")
  except FileNotFoundError:
    # If profile doesn't exist, create a new one
    print("Create Your Personal Profile:")
    profile = {
        "title": "",
        "major": "",
        "university": "",
        "about": "",
        "experience": [],
        "education": []
    }

  # Display existing profile (if any) and options
  #print("\nYour Profile:")
  displayProfile(profile, username)
  print("\nOptions:")
  print("1. Update title")
  print("2. Update major")
  print("3. Update university")
  print("4. Update about")
  print("5. Add experience")
  print("6. Add education")
  print("7. Display profile")
  print("8. Display friends profile")
  print("9. Quit")

  while True:
    choice = input("Enter your choice of operation (between 1 and 9): ")
    if choice == "1":
      profile["title"] = input("Enter your profile title: ")
    elif choice == "2":
      profile["major"] = formatText(input("Enter your major: "))
    elif choice == "3":
      profile["university"] = formatText(input("Enter your university name: "))
    elif choice == "4":
      profile["about"] = input("Write a paragraph about yourself: ")
    elif choice == "5":
      addExperience(profile)
    elif choice == "6":
      addEducation(profile)
    elif choice == "7":
       displayProfile(profile, username)
       break
    elif choice == "8":
       displayFriendsList(username)
       friend_username = input("Enter the username of the friend whose profile you want to display: ")
       print("")
       displayfriendprofile(username, friend_username)
       break
    elif choice == "9":
      break
    else:
      print("Invalid choice.")

  # Save profile
  np.save(f"{username}_profile.npy", np.array(profile))
  print("Profile updated successfully.")


# Function to display profile
def displayProfile(profile, username):
  if profile:
    print(f"{username}'s profile:")
    for key, value in profile.items():
      if isinstance(value, list):
        print(f"{key.capitalize()}:")
        for item in value:
          print(f" - {item}")
      else:
        print(f"{key.capitalize()}: {value}")
  else:
    print("No profile found.")

def displayFriendsList(username):
    accounts = np.load('accounts.npy', allow_pickle=True).item()
    if 'friends' in accounts[username]:
        friends_list = accounts[username]['friends']
        print("")
        print("Your Friends:")
        for friend_username in friends_list:
            friend_full_name = accounts[friend_username].get('full_name', 'No name available')
            print(f"Username: {friend_username} , Full Name: {friend_full_name} -Profile")
    else:
        print("You don't have any friends.")


def displayfriendprofile(username, friend_username):
    accounts = np.load('accounts.npy', allow_pickle=True).item()  
    if friend_username in accounts[username]['friends']:
        friend_full_name = accounts[friend_username].get('full_name', 'No name available')
        #print(f"{friend_username}'s Profile:")
        print(f"Full Name: {friend_full_name}")
        # Check if profile file exists for the friend
        try:
            friend_profile = np.load(f"{friend_username}_profile.npy", allow_pickle=True).item()
            displayProfile(friend_profile, friend_username)
        except FileNotFoundError:
            print("No profile found for this friend.")
    else:
        print("You are not friends with this person.")
        
# Function to handle the option to display a friend's profile
# def displayFriendProfileOption(username):
#     # Display user's friends
#     showMyNetwork(username)
    
#     # Let the user select a friend's profile
#     friend_index = int(input("Select a friend's profile (enter the corresponding number): "))
    
#     # Get the selected friend's username
#     accounts = np.load('accounts.npy', allow_pickle=True).item()
#     if username in accounts and 'friends' in accounts[username]:
#         friends_list = accounts[username]['friends']
#         if 1 <= friend_index <= len(friends_list):
#             selected_friend_username = friends_list[friend_index - 1]
#             profile = np.load(f"{selected_friend_username}_profile.npy", allow_pickle=True).item()
#             displayfriendprofile(profile, username, selected_friend_username)
#         else:
#             print("Invalid selection.")
#     else:
#         print("User not found or no friends list available.")


# def displayfriendprofile(profile, username):
#   accounts = np.load('accounts.npy', allow_pickle=True).item()  
#   if username in accounts and 'friends' in accounts[username]:
#       friends_list = accounts[username]['friends']
#       if friends_list:
#           print(f"{username}'s friends network:")
#           for index, friend_username in enumerate(friends_list, start=1):
#               friend_full_name = accounts[friend_username].get('full_name', 'No name available')
#               print(f"{index}. {friend_full_name}")

#           # Letting the user select a friend's profile
#           selected_index = int(input("Select a friend's profile (enter the corresponding number): "))
#           if 1 <= selected_index <= len(friends_list):
#               selected_friend_username = friends_list[selected_index - 1]
#               displayProfile(profile, selected_friend_username)  
#           else:
#               print("Invalid selection.")
#       else:
#             print("You don't have any friends yet.")
#   else:
#         print("User not found or no friends list available.")

# Function to add experience
def addExperience(profile):
  if len(profile["experience"]) >= 3:
    print("Maximum limit of experiences reached.")
    return

  experience = input(
      "Enter information for experience (leave blank to skip): ")
  if experience:
    profile["experience"].append(experience)


# Function to add education
def addEducation(profile):
  education = input("Enter information for education (leave blank to skip): ")
  if education:
    profile["education"].append(education)


# Function to format text (capitalize first letter of each word)
def formatText(text):
  return " ".join(word.capitalize() for word in text.split())


#Functions added Epic6 by Lampi
def checkDeletedJobs(username):
   applied_jobs = loadAppliedJobs()

   if username in applied_jobs:
      for applied_job in applied_jobs[username]:
         job_id = applied_job["job_id"]
         job_title = applied_job["job_title"]
         jobPostings = loadJobPostings()
         job_exists = any(int(job["job_id"]) == int(job_id) for  job in jobPostings)
         if not job_exists:
            print(f"A Job you applied for ({job_title}, Job ID: {job_id}) has been deleted.")
            print("")
            removeAppliedJob(username, job_id) # Remove the applied job after notification 

def removeAppliedJob(username, job_id):
   applied_jobs = loadAppliedJobs()
   if username in applied_jobs:
      for i, applied_job in enumerate(applied_jobs[username]):
         if applied_job["job_id"] == job_id:
            del applied_jobs[username][i]
            saveAppliedJobs(applied_jobs)
            break

def removeJob(username):
   jobPostings = loadJobPostings()
   print("Jobs posted by you: ")
   for job in jobPostings:
      if job["posted_by"] == username:
         print(f"Job ID: {job['job_id']}, Title: {job['title']}")

   job_id = input("Enter the job ID to delete: ")

   found = False
   for i, job in enumerate(jobPostings):
      if job["posted_by"] == username and str(job["job_id"]) == job_id:
         found = True
         #Remove notifications for applied users
         applied_users = job["applied_by"]["appliedUser"]
         for user in applied_users:
            saveAppliedJob(user, job_id,job["title"])
            #removeNotification(user, job_id)
         jobPostings = np.delete(jobPostings, i) #Delete the job from this array
         saveJobPostings(jobPostings)
         print("Job deleted successfully.")
         break

   if not found:
         print("Job not found or you are not the owner.")

def saveAppliedJob(username, job_id, job_title):
   applied_jobs = loadAppliedJobs()
   if username not in applied_jobs:
      applied_jobs[username] = []
   applied_jobs[username].append({"job_id": job_id, "job_title": job_title})
   saveAppliedJobs(applied_jobs)



def loadAppliedJobs():
   try:
      applied_jobs = np.load("applied_jobs.npy", allow_pickle=True).item()
   except FileNotFoundError:
      applied_jobs = {}
   return applied_jobs
 
def saveAppliedJobs(applied_jobs):
   np.save("applied_jobs.npy", applied_jobs)

def removeNotification(username, job_id):
   jobPostings = loadJobPostings()
   found = False
   for job in jobPostings:
      if job["job_id"] == job_id:
         found = True
         if username in job["applied_by"]["appliedUser"]:
            print(f"A Job you applied for (Job ID: {job_id}) has been deleted.")
         break

   if not found:
         print(f"A Job you applied for (Job ID: {job_id}) has been deleted.")

def getUserAppliedJobs(username):
   jobPostings = loadJobPostings()
   applied_jobs = {}
   for job in jobPostings:
      if username in job["applied_by"]["appliedUser"]:
         applied_jobs[job["job_id"]] = job["title"]
   return applied_jobs

def saveJobPostings(jobPostings):
   np.save("job_postings.npy", jobPostings)