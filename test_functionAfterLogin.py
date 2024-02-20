import pytest
from io import StringIO
from unittest.mock import patch
import numpy as np

# Import functions from the program to be tested
from f_AfterLogin import addOptions, postJob, loadJobPostings

# Test addOptions function
def test_addOptions(capsys):
    with patch('builtins.input', side_effect=['1', '2']):
        addOptions("test_user")
        captured = capsys.readouterr()
        assert "Search for a job/internship" in captured.out
        assert "Find someone you know" in captured.out

# Test postJob function
def test_postJob(tmp_path):
    # Mocking user input and np.save function
    with patch('builtins.input', side_effect=['Test Job', 'Test Description', 'Test Employer', 'Test Location', 'Test Salary']), \
         patch('numpy.save') as mock_save:
        # Create a temporary file to simulate job_postings.npy
        job_postings_file = tmp_path / 'job_postings.npy'
        postJob("test_user")
        # Ensure that np.save was called with the correct arguments
        mock_save.assert_called_once_with(str(job_postings_file), [{'title': 'Test Job', 'description': 'Test Description', 'employer': 'Test Employer', 'location': 'Test Location', 'salary': 'Test Salary', 'posted_by': 'test_user'}])

# Test loadJobPostings function
def test_loadJobPostings(tmp_path):
    # Create a temporary file and save some job postings
    job_postings_file = tmp_path / 'job_postings.npy'
    np.save(job_postings_file, [{'title': 'Test Job', 'description': 'Test Description', 'employer': 'Test Employer', 'location': 'Test Location', 'salary': 'Test Salary', 'posted_by': 'test_user'}])
    # Test if job postings are loaded correctly
    loaded_postings = loadJobPostings()
    assert len(loaded_postings) == 1
    assert loaded_postings[0]['title'] == 'Test Job'