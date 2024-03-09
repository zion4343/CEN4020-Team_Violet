'''
The functions developed in Epic 6
'''

'''
Import
'''
import numpy as np

def applyForJob(username, jobPostings, jobNumber):
    #student cannot apply for a job that they posted.
    if(username == jobPostings[jobNumber]["posted_by"]):
        print("The job is the one you posted")
        print("You cannot apply to the job")
        return 0
    #Once they have applied for a job, they cannot apply for it again.
    elif(username in jobPostings[jobNumber]["applied_by"]["appliedUser"]):
        print("You already applied for a job")
        return 0        
    #Input the information to apply
    print("Enter the information to apply for the job")
    jobPostings[jobNumber]["applied_by"]["appliedUser"].append(username)
    jobPostings[jobNumber]["applied_by"]["graduationDate"].append(input("Enter your graduation date(mm/dd/yyyy): "))
    jobPostings[jobNumber]["applied_by"]["startWorkingDate"].append(input("Enter a date that you can start working(mm/dd/yyyy): "))
    jobPostings[jobNumber]["applied_by"]["reason"].append(input("Enter a paragraph text explaining why you think that you would be a good fit for this job: "))
    
    # Save the updated job postings
    np.save("job_postings.npy", jobPostings)
    
    print("You applied for the job successfully")
    return 1
    
def saveJob(username, jobPostings, jobNumber):
    jobPostings[jobNumber]["saved_by"]["savedUser"].append(username)
    print("You saved the job!")
    
    # Save the updated job postings
    np.save("job_postings.npy", jobPostings)
    
    return 1