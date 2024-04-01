import re

class Validation():
    def __init__(self):
        pass

    def is_correct_name(self, name):

        if not isinstance(name, str):
            return None
        if len(name.strip(),) < 2:
            return None
        if not all(c.isalpha() or c. isspace() or c in "-'." for c in name):
            return None
        return True
    # email pattern[a-zA-Z0-9-]
    def is_valid_email(self, email):
        pattern = r'^[\w\_#-]+@gmail+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    def is_valid_password(self, password):
        if not isinstance(password, str):
            return False
        if len(password) < 8:
            return False
        if not any(c.isdigit() for c in password):
            return False
        if not any(c.isupper() for c in password):
            return False
        if not re.search(r'^.*[!@#$%^&*()_+[\]{};:\'"|\\<>,./?].*$', password):
            return False
        return True

    def is_valid_element(self, element):
        if not isinstance(element, str):
            return False
        if not all(c is not None for c in element):
            return False
        if not all(c != ' ' for c in element.strip()) :
            return False
        if not any(c.isupper() for c in element):
            return False
        if not all(c.isalpha for c in element):
            return False
        if not len(element.strip()) >=1 and len(element.strip()) < 3  :
            return False
        return True
