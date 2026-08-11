from value_objects.password import Password
from value_objects.email import Email

class User:
    def __init__(self, id: str, email: Email, password: Password):
        self.id = id
        self.email = email
        self.password = password