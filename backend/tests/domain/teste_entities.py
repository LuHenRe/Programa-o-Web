from uuid import uuid4
import pytest
from app.domain.entities.user import User
from app.domain.value_objects.email import Email
from app.domain.value_objects.password import Password

def test_create_valid_user():
    id=uuid4()
    user = User(id=id, email=Email("test@example.com"), password=Password("password123"))
    assert user.id == id
    assert user.email.value == "test@example.com"
    assert user.password.value == "password123"
