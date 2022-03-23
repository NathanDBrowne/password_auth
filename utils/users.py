import os
from getpass import getpass

from utils.passwords import PasswordCheck, encrypt


class User:
    """all users will be able to perform these tasks"""

    def __init__(self, username=None) -> None:
        if username:
            self.filename = os.path.join("users", "{}.txt".format(username))
        else:
            self.existing_files = os.listdir("users")

    def creation_interface(self):
        """register a new user in the filesystem"""

        valid_entered = False

        while not valid_entered:
            self.username = input("Enter your username: ")
            self.password = getpass("Enter a password: ")

            if "{}.txt".format(self.username) in self.existing_files:
                print("Invalid username or password.")
            else:
                password_check = PasswordCheck(self.password)
                if len(password_check.suggestions) == 0:
                    password_verify = getpass("Re-enter password:")
                    if password_verify != self.password:
                        print("Passwords do not match.")
                    else:
                        print("Account created!")
                        valid_entered = True
                else:
                    print("Weak password:")
                    for s in password_check.suggestions:
                        print(s)
                    print("\n")

        with open(os.path.join("utils", "modules.txt")) as f:
            possible_modules = [x[:-1] for x in f.readlines()]

        possible_modules.append("")

        valid_entered = False
        self.chosen_module = input("Enter your chosen module (optionally leave blank):")
        while not valid_entered:
            if self.chosen_module not in possible_modules:
                self.chosen_module = input("Invalid module. Try again:")
            else:
                valid_entered = True

        self.register_user()

    def register_user(self, status="STUDENT"):
        with open(os.path.join("users", "{}.txt".format(self.username)), "w") as f:
            f.write(status + "***" + encrypt(self.password))


class Lecturer(User):
    """lecturers have similar permissions to students but can send emails to their entire class"""

    def __init__(self, username) -> None:
        super().__init__(username)

    def send_email_module(self):
        pass


class Admin(User):
    """
    admins have the same permissions as students but can also
    add/delete accounts and send emails to every user
    """

    def __init__(self, username) -> None:
        super().__init__(username)

    def send_email_all(self):
        pass

    def delete_account(self):
        pass
