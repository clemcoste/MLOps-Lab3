def get_username_from_input():
    username = input("Please write your username :")
    if ' ' in username or len(username) == 0:
        print("The username is not valid")
        return None
    else:
        return username