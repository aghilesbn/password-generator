import pytest
from project import generate_password, password_strength, additional_function

def test_generate_password():
    password = generate_password(12)
    assert len(password) == 12

def test_password_strength():
    strength = password_strength("TestPassword123!")
    assert strength == "Strong"  # À ajuster selon la logique implémentée

def test_additional_function():
    result = additional_function()
    assert result is not None

# Autres tests pour les fonctions supplémentaires si nécessaire
