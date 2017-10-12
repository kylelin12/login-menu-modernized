from flask import redirect, url_for, session, flash

# Hardcoded username/password
USERNAME = "DWROX"
PASSW = "nottrue"

# Success values
SUCCESS = 1
BAD_USER = -1
BAD_PASS = -2
BAD_USER_PASS = -3

# Function that determines if the login is successful
def auth_helper(user, passw):
    if user == USERNAME:
        if passw == PASSW:
            return SUCCESS
        else:
            return BAD_PASS
    else:
        if passw == PASSW:
            return BAD_USER
        else:
            return BAD_USER_PASS

# Function that flashes the right error message depending on the input value
def auth_flash(message):
    if message == -2:
        flash("Incorrect password")
    elif message == -1:
        flash("Incorrect username")
    elif message == -3:
        flash("Incorrect username and password")
    else:
        flash("Success")

# Function that helps redirection based on input
def auth_redirect(auth_success, username_i):
    if auth_success == SUCCESS:
        session['user_logged'] = username_i
        return redirect(url_for('welcome'))
    if auth_success == BAD_PASS:
        pass
    elif auth_success == BAD_USER:
        pass
    elif auth_success == BAD_USER_PASS:
        pass
    return redirect(url_for('home'))