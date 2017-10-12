from flask import session

# Function that pops 'user_logged' off of session if it is in session
def logout_helper():
    if 'user_logged' in session:
        session.pop('user_logged')