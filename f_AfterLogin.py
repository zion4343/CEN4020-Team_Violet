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
    print ("5. InCollege Important Links")
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
        print("6. Return to the previous level. . .")

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
        
        else:
            print("6. Returning to the previous level. . .")
            addOptions(username)
    elif choice == "4":
        guestControls(username)

    elif choice == "5":
        goingBackLoggedIn = handleImportantLinks()

        #Checks if the user wants to come back to main screen after clicking InCollege Important Links
        if goingBackLoggedIn == 0:
            addOptions(username)

        else: #Or go back to Important Links option
            handleImportantLinks()
        

    else:
        print("Invalid choice.")

    return 1

# Function to post a job
def postJob(username):
    jobPostings = loadJobPostings()
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

  

    job = np.array(job)  #Converts job to a numpy array 
    jobPostings = np.concatenate((jobPostings, np.expand_dims(job, axis=0)), axis=0) #Concatenates job array

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
        user_settings[username] = {"email": True, "sms": True, "targeted_advertising": True}

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
def userImportantExit(userChoice):
    if userChoice == 1:
        handleImportantLinks()
        
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
#Function to display file content
def getFile(filename):
    with open(filename, 'r') as file:
        content = file.read()
    print(content)



#Takes the selection of user in main.py and if it is 5 (Important Links, then it displays the Important Links menu)
def handleImportantLinks():

    #This is to display the InCollege Important Links before the user is logged in 
    displayImportantLinks()
    back = 0

    #User chooses between 0 and 10 for various options
    importantLinkChoice = inputValidation("\n\nPlease select the number corresponding to your choice: ", list(range(11)))

    #Displays the content for every option chosen
    if importantLinkChoice == 1:

        
        print("\nCopyright Notice\n")
        filename = returnFilename(importantLinkChoice)
        getFile(filename)
        
        #Gives user the chance to go back up a level in the menu or exit entirely
        userImportantReturn = int(input("Press 1 to return to previous menu or press 2 to exit entirely: "))
        userImportantExit(userImportantReturn)

    elif importantLinkChoice == 2:
        
        print("\nAbout\n")
        filename = returnFilename(importantLinkChoice)
        getFile(filename)
        
        #Gives user the chance to go back up a level in the menu or exit entirely
        userImportantReturn = int(input("Press 1 to return to previous menu or press 2 to exit entirely: "))
        userImportantExit(userImportantReturn)

    elif importantLinkChoice == 3:
        print("\nAccessibility\n")
        filename = returnFilename(importantLinkChoice)
        getFile(filename)
        
        #Gives user the chance to go back up a level in the menu or exit entirely
        userImportantReturn = int(input("Press 1 to return to previous menu or press 2 to exit entirely: "))
        userImportantExit(userImportantReturn)

    elif importantLinkChoice == 4:
        print("\nUser Agreement\n")
        filename = returnFilename(importantLinkChoice)
        getFile(filename)
        
        #Gives user the chance to go back up a level in the menu or exit entirely
        userImportantReturn = int(input("Press 1 to return to previous menu or press 2 to exit entirely: "))
        userImportantExit(userImportantReturn)

    elif importantLinkChoice == 5:
        print("\nPrivacy Policy\n")
        filename = returnFilename(importantLinkChoice)
        getFile(filename)
        
        #Gives user the chance to go back up a level in the menu or exit entirely
        userImportantReturn = int(input("Press 1 to return to previous menu or press 2 to exit entirely: "))
        userImportantExit(userImportantReturn)

    elif importantLinkChoice == 6:
        print("\nCookie Policy\n")
        filename = returnFilename(importantLinkChoice)
        getFile(filename)
        
        #Gives user the chance to go back up a level in the menu or exit entirely
        userImportantReturn = int(input("Press 1 to return to previous menu or press 2 to exit entirely: "))
        userImportantExit(userImportantReturn)

    elif importantLinkChoice == 7:
        print("\nCopyright Policy\n")
        filename = returnFilename(importantLinkChoice)
        getFile(filename)
        
        #Gives user the chance to go back up a level in the menu or exit entirely
        userImportantReturn = int(input("Press 1 to return to previous menu or press 2 to exit entirely: "))
        userImportantExit(userImportantReturn)

    elif importantLinkChoice == 8:
        print("\nBrand Policy\n")
        filename = returnFilename(importantLinkChoice)
        getFile(filename)
        
        #Gives user the chance to go back up a level in the menu or exit entirely
        userImportantReturn = int(input("Press 1 to return to previous menu or press 2 to exit entirely: "))
        userImportantExit(userImportantReturn)

    elif importantLinkChoice == 9:
        print("\nGuest Controls\n")
        
        
        #Gives user the chance to go back up a level in the menu or exit entirely
        userImportantReturn = int(input("Press 1 to return to previous menu or press 2 to exit entirely: "))
        userImportantExit(userImportantReturn)

    elif importantLinkChoice == 10:
        print("\nLanguages\n")
        
        #Gives user the chance to go back up a level in the menu or exit entirely
        userImportantReturn = int(input("Press 1 to return to previous menu or press 2 to exit entirely: "))
        userImportantExit(userImportantReturn)

    elif importantLinkChoice == 0:
        return 0

   
    
    return back