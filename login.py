from flask import Flask, render_template, request, session, redirect, url_for, flash
from utils.auth_helper import auth_helper, auth_flash, auth_redirect
from utils.logout_helper import logout_helper
import os

login = Flask(__name__)
login.secret_key = os.urandom(32)

@login.route('/')
def home():
    # If the user is logged in, redirect to the welcome page
    if 'user_logged' in session:
        return redirect(url_for('welcome'))
    # Otherwise, return the login form
    else:
        return render_template('login_error.html')

@login.route('/auth', methods=['POST'])
def auth():
    # Sets local variables equal to the form inputs
    username_i = request.form['username-i']
    password_i = request.form['password-i']

    # Runs a helper function that returns 1, -1, -2, or -3.
    auth_success = auth_helper(username_i, password_i)

    # If the auth was not a success
    if auth_success is not 1:
        auth_flash(auth_success)

    # Redirect helper function
    return auth_redirect(auth_success, username_i)

@login.route('/welcome')
def welcome():
    # If the user is logged in, render the welcome page with the username variable equal to the username
    if 'user_logged' in session:
        return render_template('welcome.html', username=session['user_logged'])
    # Otherwise, redirect to the root/homepage
    else:
        return redirect(url_for('home'))

@login.route('/logout', methods=['POST'])
def logout():
    # Runs a helper function that pops 'user_logged' off of session.
    logout_helper()
    # Redirect to the root/homepage
    return redirect(url_for('home'))

if __name__ == '__main__':
    login.debug = True
    login.run()