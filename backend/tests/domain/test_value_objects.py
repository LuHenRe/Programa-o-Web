import pytest
from app.domain.value_objects.email import Email
from app.domain.value_objects.password import Password

def test_email_creation():
    email = Email("test@example.com")
    assert email.value == "test@example.com"

def test_password_creation():
    password = Password("password123")
    assert password.value == "password123"

def test_email_validation():
    with pytest.raises(ValueError):
        Email("invalid-email")

def test_password_validation():
    with pytest.raises(ValueError):
        Password("short")
