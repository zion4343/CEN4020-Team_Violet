'''
Test Script to test the functions in f_Epic6.py
'''

import pytest
from unittest.mock import patch
import numpy as np

# Import functions from the program to be tested
from f_Epic6 import applyForJob, saveJob

#Test applyForJob()
jobNumber = 0
jobPostings = [
                {"title": "ML Engineer",
                "description": "This is description",
                "employer": "employer",
                "location": "location",
                "salary": "salary",
                "posted_by": "postedUser",
                "applied_by": {"appliedUser":["appliedUser"], "graduationDate":["05/05/2025"], "startWorkingDate":["08/08/2025"], "reason":["Reason"]},
                "saved_by": {"savedUser":["savedUser"]}}
               ]

@patch('builtins.input', side_effect=['05/05/2025', '08/08/2025', 'Apply Reason'])
def test_applyForJob(mock_input):
    assert applyForJob("passUser", jobPostings, jobNumber) == 1
    
#When the job is posted by the applied user
def test_applyForJob_posted():
    assert applyForJob("postedUser", jobPostings, jobNumber) == 0
    
#When the job is already applied by the user
def test_applyForJob_applied():
    assert applyForJob("appliedUser", jobPostings, jobNumber) == 0
    
#Test saveJob()
def test_saveJob():
    assert saveJob("passUser", jobPostings, jobNumber) == 1
    
def test_saveJob_saved():
    assert saveJob("savedUser", jobPostings, jobNumber) == 0
