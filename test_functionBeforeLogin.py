import pytest
import numpy as np
from unittest.mock import patch
from f_BeforeLogin import CreateNewAccount, LogIn, successStory, connectPeople

# Test CreateNewAccount function
def test_CreateNewAccount():
    # Test account creation with valid inputs
    with pytest.raises(SystemExit):
        # Simulate user input for testing
        inputs = iter(['Test', 'User', 'test_user', 'Test123!', 'Test123!', 'n'])
        # Patch input function to return predefined values
        with pytest.raises(SystemExit):
            with patch('builtins.input', lambda: next(inputs)):
                CreateNewAccount()

# Test LogIn function
def test_LogIn():
    # Test login with existing account
    with patch('builtins.input', side_effect=['test_user', 'Test123!']), \
         patch('f_BeforeLogin.accounts', {'test_user': 'Test123!'}):
        assert LogIn() == 1

    # Test login with incorrect password
    with patch('builtins.input', side_effect=['test_user', 'WrongPassword']), \
         patch('f_BeforeLogin.accounts', {'test_user': 'Test123!'}):
        assert LogIn() == 0

    # Test login with non-existing account
    with patch('builtins.input', side_effect=['NonExistingUser', 'Test123!']), \
         patch('f_BeforeLogin.accounts', {'test_user': 'Test123!'}):
        assert LogIn() == 0

# Test connectPeople function
def test_connectPeople():
    # Test connection with existing user
    with patch('builtins.input', side_effect=['Test', 'User', 1]):
        assert connectPeople() is None

    # Test connection with non-existing user
    with patch('builtins.input', side_effect=['NonExisting', 'User']):
        assert connectPeople() is None