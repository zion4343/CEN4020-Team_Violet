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
    print("Welcome! What would you like to do?")
    print("1. Search for a job/internship")
    print("2. Find someone you know")
    print("3. Learn a new skill")

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
            addOptions()

    else:
        print("Invalid choice.")

    return 1

# Function to post a job
def postJob(username):
    if len(jobPostings) >= 5:
        print("Maximum number of job postings reached.")
        return

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

# Load job postings
def loadJobPostings():
    global jobPostings
    try:
        jobPostings = np.load("job_postings.npy", allow_pickle=True)
    except FileNotFoundError:
        jobPostings = []