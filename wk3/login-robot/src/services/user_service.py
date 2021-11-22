import re
from entities.user import User


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
        if self._user_repository.find_by_username(username):
            raise UserInputError("Username already in use")
        if len(username)<3:
            raise UserInputError("Username has to contain at least 3 characters")
        # if not bool(re.match("^[a-z]+$", username)):
        if not (username.isalpha() and username.islower()):
            raise UserInputError("Username can only contain characters a-z")
        if len(password)<8:
            raise UserInputError("Password has to contain at least 8 characters")
        # if not bool(re.fullmatch("[^A-Za-z]", password)):
        # regex ei ole ystävä en osaa )--:
        if password.isalpha():
            raise UserInputError("Password cannot contain only letters")