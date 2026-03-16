import hashlib

class UserManager:
    def __init__(self):
        self.users = {}  # A dictionary to store user data

    def register(self, username, password):
        if username in self.users:
            raise ValueError('User already exists.')  # Handle user already exists
        hashed_password = self.hash_password(password)
        self.users[username] = hashed_password
        return 'User registered successfully!'

    def authenticate(self, username, password):
        hashed_password = self.hash_password(password)
        if self.users.get(username) == hashed_password:
            return 'Authentication successful!'
        else:
            return 'Authentication failed.'

    def hash_password(self, password):
        # Hash the password using SHA-256
        return hashlib.sha256(password.encode()).hexdigest()

    def change_password(self, username, old_password, new_password):
        if self.authenticate(username, old_password) == 'Authentication successful!':
            self.users[username] = self.hash_password(new_password)
            return 'Password changed successfully!'
        else:
            return 'Authentication failed. Password not changed.'
