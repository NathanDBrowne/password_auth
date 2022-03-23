import re


class PasswordCheck:
    def __init__(self, entry):
        self.entry = entry

        self.suggestions = []
        # self.check_length()
        # self.check_number()
        # self.check_special()
        # self.check_capital()

    def check_number(self):
        if not re.match(r".*[0-9].*", self.entry):
            self.suggestions.append("Your password should contain at least one number.")

    def check_special(self):
        if not re.match(
            r".*[\!\@\#\$\%\^\&\*\(\)\_\+\-\=\[\]\{\}\;\'\:\"\\\|\,\.\<\>\/\?].*", self.entry
        ):
            self.suggestions.append("Your password should contain at least one special character.")

    def check_length(self):
        if len(self.entry) < 8:
            self.suggestions.append("Your password too short")

    def check_capital(self):
        if not re.match(r".*[A-Z].*", self.entry):
            self.suggestions.append("Your password should contain at least one capital letter.")

    def check_lower(self):
        if not re.match(r".*[a-z].*", self.entry):
            self.suggestions.append("Your password should contain at least one lowercase letter.")


def encrypt(password):
    return password[::-1]
