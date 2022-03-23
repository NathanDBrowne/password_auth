import os
import re
from getpass import getpass

from utils.passwords import encrypt
from utils.users import Admin, Lecturer, User


class FrontEnd:
    def __init__(self):
        self.available_files = os.listdir("users")

    def login(self):
        """the login function which will allow the cli user to interact with the text files"""

        logged_in = False

        while not logged_in:
            username = input("Enter your username: ")
            password = getpass("Enter your password: ")

            if "{}.txt".format(username) not in self.available_files:
                print("Invalid: please check your username/password are both correct.")
            else:
                with open(os.path.join("users", "{}.txt".format(username)), "r") as f:
                    f_content = f.read()
                hashed_pwd = f_content.split("****")[1]
                if encrypt(password) == hashed_pwd:
                    logged_in = True
                else:
                    print("Invalid: please check your username/password are both correct.")

        auth_level = f_content.split("****")[0]

        _map = {"ADMIN": Admin, "LECTURER": Lecturer, "STUDENT": User}
        cls = _map[auth_level]
        cls(username).run()

    def run(self):
        print(
            "What would you like to do?\n-(l)ogin\n-(c)reate account\n(To create admin or lecturer accounts you must log in as an admin first)\n"
        )
        action = ""
        while not re.match(r"^(l|c)$", action):
            action = input("Enter: ")

        _map = {"l": self.login, "c": User().creation_interface}

        fn = _map[action]
        fn()


if __name__ == "__main__":
    f = FrontEnd()
    f.run()
