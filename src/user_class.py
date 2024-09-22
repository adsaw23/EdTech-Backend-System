import time

class User:
    def __init__(self, user_id, name, email, password):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password

    def update_email(self, new_email):
        self.email = new_email

    def update_password(self, new_password):
        self.password = new_password

    def validate_credentials(self, email, password):
        return self.email == email and self.password == password