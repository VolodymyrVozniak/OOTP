from .user import User


class Authentication:
    def __init__(self):
        self.users = []

    def register(self, username, password):
        self.users.append(User(username, password))

    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                return True
        return False
