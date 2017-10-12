from flask import session

# Function that determines if the login is successful
def logout_helper():
    if 'user_logged' in session:
        session.pop('user_logged')