import pytest
from project import generate_password, password_strength

def test_generate_password():
    password = generate_password(12)
    assert len(password) == 12

def test_password_strength():
    strength = password_strength("TestPassword123!")
    assert strength == "Strong"  # Example test, adapt based on your strength evaluation logic

if __name__ == "__main__":
    pytest.main()
