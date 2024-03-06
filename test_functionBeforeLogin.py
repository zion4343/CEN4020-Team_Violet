'''
Test Script to test the functions in f_BeforeLogin.py
'''

import pytest
import numpy as np
from unittest.mock import patch
from f_BeforeLogin import CreateNewAccount, LogIn, successStory, connectPeople, handleImportantLinks

#Test CreateNewAccount()
@patch('builtins.input', side_effect=['John', 'Doe', 'johndoe', 'Password123!'])
@patch('f_BeforeLogin.readDictonary', return_value=None)
@patch('f_BeforeLogin.writeDictonary', return_value=None)
def test_CreateNewAccount(mock_readDictonary, mock_writeDictonary, mock_input):
    assert CreateNewAccount() == 1
    
#Invalid Password
@patch('builtins.input', side_effect=['Joe', 'Doe', 'joedoe', 'invalid123', 'Password123!'])
@patch('f_BeforeLogin.readDictonary', return_value=None)
@patch('f_BeforeLogin.writeDictonary', return_value=None)
def test_CreateInvalidAccount(mock_readDictonary, mock_writeDictonary, mock_input):
    assert CreateNewAccount() == 1
    
#Test LogIn()
@patch('builtins.input', side_effect=['johndoe', 'Password123!'])
@patch('f_BeforeLogin.readDictonary', return_value={'johndoe': 'Password123!'})
def test_LogIn(mock_readDictonary, mock_input):
    assert LogIn() == 1
    
#Test successStory()
def test_successStory():
    assert successStory() == 1
    
#Test connectPeople()
@patch('builtins.input', side_effect=['John', 'Doe', '1'])
@patch('f_BeforeLogin.readDictonary', return_value={'JohnDoe': 'Password123!'})
def test_connectPeople(mock_readDictonary, mock_input):
    assert connectPeople() == 1
    
#Test handleImportantLinks()
@patch('builtins.input', side_effect=['1', '1', '1', '2'])
def test_handleImportantLinks(mock_input):
    assert handleImportantLinks() == 0
    
@patch('builtins.input', side_effect=['1', '2'])
def test_handleImportantLinks_Quit(mock_input):
    assert handleImportantLinks() == 0