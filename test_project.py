import pytest
from project import generate_password, password_starting_with, password_ending_with

def test_generate_password():
    """Test case for generate_password function."""
    length = 12
    password = generate_password(length)
    assert len(password) == length

def test_password_starting_with():
    """Test case for password_starting_with function."""
    start_word = "Start"
    length = 12
    password = password_starting_with(start_word, length)
    assert password.startswith(start_word)
    assert len(password) == length

def test_password_ending_with():
    """Test case for password_ending_with function."""
    end_word = "End"
    length = 12
    password = password_ending_with(end_word, length)
    assert password.endswith(end_word)
    assert len(password) == length
