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
def updateApplyTime(username):
    #read accounts
    py_dict = np.load("accounts.npy", allow_pickle = "TRUE")
    accounts = py_dict.item()
    
    #Update the last login time
    accounts[username]["lastApplyTime"] = datetime.now()
    
    #save accounts
    np.save("accounts.npy", accounts)
    
    return 1

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
    
    
    