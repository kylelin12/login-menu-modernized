from flask import Flask, render_template, request, session, redirect, url_for, flash
from utils.auth_helper import auth_helper, auth_flash, auth_redirect
from utils.logout_helper import logout_helper
import os

login = Flask(__name__)
login.secret_key = os.urandom(32)

@login.route('/')
def home():
    if 'user_logged' in session:
        return redirect(url_for('welcome'))
    else:
        return render_template('login_error.html')

@login.route('/auth', methods=['POST'])
def auth():
    username_i = request.form['username-i']
    password_i = request.form['password-i']

    auth_success = auth_helper(username_i, password_i)

    if auth_success is not 1:
        auth_flash(auth_success)

    return auth_redirect(auth_success, username_i)

@login.route('/welcome')
def welcome():
    if 'user_logged' in session:
        return render_template('welcome.html', username=session['user_logged'])
    else:
        return redirect(url_for('home'))

@login.route('/logout', methods=['POST'])
def logout():
    logout_helper()
    return redirect(url_for('home'))

if __name__ == '__main__':
    login.debug = True
    login.run()