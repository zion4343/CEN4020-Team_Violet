'''
Test Script to test the functions in f_AfterLogin.py
'''

import pytest
from unittest.mock import patch
import numpy as np

# Import functions from the program to be tested
from f_AfterLogin import addOptions, postJob, toggleFeature, guestControls 

#Test addOptions()
@patch('builtins.input', side_effect=['1', '1'])
def test_addOptions_search_job(mock_input):
    assert addOptions("testuser") == 1

@patch('builtins.input', side_effect=['1', '2'])
@patch('f_AfterLogin.postJob', return_value=None)
def test_addOptions_post_job(mock_postJob, mock_input):
    assert addOptions("testuser") == 1

@patch('builtins.input', side_effect=['2'])
def test_addOptions_find_someone(mock_input):
    assert addOptions("testuser") == 1

@patch('builtins.input', side_effect=['3', '1'])
def test_addOptions_learn_programming(mock_input):
    assert addOptions("testuser") == 1

@patch('builtins.input', side_effect=['3', '2'])
def test_addOptions_learn_prompt_engineering(mock_input):
    assert addOptions("testuser") == 1

@patch('builtins.input', side_effect=['3', '3'])
def test_addOptions_learn_3d_modeling(mock_input):
    assert addOptions("testuser") == 1

@patch('builtins.input', side_effect=['3', '4'])
def test_addOptions_learn_data_analysis(mock_input):
    assert addOptions("testuser") == 1

@patch('builtins.input', side_effect=['3', '5'])
def test_addOptions_learn_language_learning(mock_input):
    assert addOptions("testuser") == 1

@patch('builtins.input', side_effect=['4'])
@patch('f_AfterLogin.guestControls', return_value=None)
def test_addOptions_guest_controls(mock_guestControls, mock_input):
    assert addOptions("testuser") == 1

@patch('builtins.input', side_effect=['5'])
def test_addOptions_invalid_choice(mock_input):
    assert addOptions("testuser") == 1
    
#Test postJob()
@patch('builtins.input', side_effect=['Job Title', 'Job Description', 'Employer Name', 'Job Location', 'Job Salary'])
@patch('f_AfterLogin.loadJobPostings', return_value=[{} for _ in range(4)])  # Less than 5 job postings
@patch('numpy.save')
def test_postJob_success(mock_save, mock_loadJobPostings, mock_input):
    assert postJob("testuser") == 1

@patch('f_AfterLogin.loadJobPostings', return_value=[{} for _ in range(5)])  # 5 job postings
def test_postJob_failure(mock_loadJobPostings):
    assert postJob("testuser") == 0
    
#Test toggleFeature()

#Test guestControls()
# Function to handle guest controls
@patch('builtins.input', side_effect=['1'])
@patch('f_AfterLogin.toggleFeature', return_value = 1)
def test_guestControls_email(mock_toggleFeature, mock_input):
    assert guestControls("testuser") == 1
    

@patch('builtins.input', side_effect=['2'])
@patch('f_AfterLogin.toggleFeature', return_value = 1)
def test_guestControls_sms(mock_toggleFeature, mock_input):
    assert guestControls("testuser") == 1

@patch('builtins.input', side_effect=['3'])
@patch('f_AfterLogin.toggleFeature', return_value = 1)
def test_guestControls_targeted_advertising(mock_toggleFeature, mock_input):
    assert guestControls("testuser") == 1

@patch('builtins.input', side_effect=['4'])
@patch('f_AfterLogin.toggleFeature', return_value = 1)
@patch('f_AfterLogin.addOptions', return_value = 1)
def test_guestControls_return_previous_level(mock_toggleFeature, mock_addOptions, mock_input):
    assert guestControls("testuser") == 1

@patch('builtins.input', side_effect=['5', '1'])
@patch('f_AfterLogin.toggleFeature', return_value = 1)
def test_guestControls_invalid_choice(mock_toggleFeature, mock_input):
    assert guestControls("testuser") == 1