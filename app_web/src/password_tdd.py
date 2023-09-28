import re

def get_password_from_input():
    password = input("Please select your password :")
    # Recherche caractère spécial
    list_special_char = re.compile(r'[!@#$%^&*()_+{}\[\]:;<>,.?~\\-]')
    if list_special_char.search(password) is not None and len(password) > 7 and re.search(r'\d', password) is not None and re.search(r'[a-zA-Z]',password) is not None:
        return password
    else:
        return None