import re
from validate_email import validate_email

pass_reguex="^[a-zA-Z0-9_.-]+$"
user_reguex="^[a-zA-Z0-9_.-]+$"
email="/^\w+([\.-]?\w+)@\w+([\.-]?\w+)(\.\w{2,3})+$/"


def isEmailVaid(email):
    is_valid=validate_email(email)
    return is_valid

def isUsernameValid(user):
    if re.search(user_reguex,user):
        return True
    else: 
        return False

def isPasswordValid(password):
    if re.search(pass_reguex,password):
        return True
    else: 
        return False