'''
The functions developed in Epic 8
'''

'''
Import
'''
import numpy as np
from datetime import datetime

'''
Functions
'''
#The function to update lastApplyTime
def updateApplyTime(username):
    #read accounts
    py_dict = np.load("accounts.npy", allow_pickle = "TRUE")
    accounts = py_dict.item()
    
    #Update the last login time
    accounts[username]["lastApplyTime"] = datetime.now()
    
    #save accounts
    np.save("accounts.npy", accounts)
    
    return 1

#The function to send notification if the user does not apply to a job over 7 days
def recommendApplyJob(username):
    #read accounts
    py_dict = np.load("accounts.npy", allow_pickle = "TRUE")
    accounts = py_dict.item()
    
    #Get the current time and last time & Convert them into float
    currentTime = datetime.now()
    current_float = currentTime.timestamp()
    
    lastTime = accounts[username]["lastApplyTime"] = datetime.now()
    last_float = lastTime.timestamp()
    
    #if the difference is over 7 days(7 * 24 * 60 * 60), print the notification
    if(current_float - last_float > 604800):
        print("Remember - you're going to want to have a job when you graduate. Make sure that you start to apply for jobs today!")
    
    return 1

#The function that recommend users to set profile if the user have not set the profile
def recommendSettingProfile(username):
    #Read profile
    try:
        # Load existing profile if it exists
        profile = np.load(f"profileFiles/{username}_profile.npy", allow_pickle=True).item()
        
    except FileNotFoundError:
        print("You did not set your profile. Don't forget to create a profile!")
        return 0
    
    return 1

#The function to store NewUser for notification to existing user
def newUser(username):
    #read accounts
    try:
        py_dict = np.load("accounts.npy", allow_pickle = "TRUE")
        accounts = py_dict.item()
    except:
        accounts = {}
    
    #read newUsers
    try:
        py_dict = np.load("newUsers.npy", allow_pickle = "TRUE")
        newUsers = py_dict.item()
        
    except FileNotFoundError:
        newUsers = {}
        
    #Set the newUsers to notify the new Users to existing users
    for account in accounts.keys():
        try:
            newUsers[account].append({username: "NotAnnounced"})
        except KeyError:
            newUsers[account] = {username: "NotAnnounced"}
        
    #save newUsers
    np.save("newUsers.npy", newUsers)
    
    return 1 

def newUserNotification(username):
    #read newUsers
    try:
        py_dict = np.load("newUsers.npy", allow_pickle = "TRUE")
        newUsers = py_dict.item()
        
    except FileNotFoundError:
        return 0
    
    #read accounts
    try:
        py_dict = np.load("accounts.npy", allow_pickle = "TRUE")
        accounts = py_dict.item()
        
    except FileNotFoundError:
        return 0
    
    #Announce New Users
    for newUser in newUsers[username].keys():
        print(accounts[newUser]["last_name"] + " " + accounts[newUser]["first_name"] + " has joined InCollege!")
        
    #Delete announced NewUsers
    newUsers[username].clear()
        
    #save newUsers
    np.save("newUsers.npy", newUsers)
    
    return 1   

# Notify Applied Jobs Count
def notifyAppliedJobsCount(username):
    # Load accounts from file
    try:
        accounts = np.load("accounts.npy", allow_pickle=True).item()
    except FileNotFoundError:
        print("Error: Unable to load accounts.")
        return

    # Retrieve the number of applied jobs for the user
    applied_jobs_count = len(accounts.get(username, {}).get('applied_jobs', []))
    print(f"You have currently applied for {applied_jobs_count} jobs.")

# Notify about a deleted job
def notifyDeletedJob(username, deleted_job_title):
    print(f"A Job you {username} applied for ({deleted_job_title}) has been deleted.")
