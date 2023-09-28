def get_email_from_input():
    email = input('Please write your email :')
    if '@' in email:
        if '.' in email.split('@')[1]:
            return email
    else:
        return None