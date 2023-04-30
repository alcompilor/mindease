#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Flask module."""

import os
from pathlib import Path
from textwrap import dedent
from flask import (Flask, render_template, request,
                   flash, url_for, redirect, session)
import bcrypt
from dotenv import load_dotenv
from src.validator import ValidateRegister, ValidateLogin
from src.utils.register.register import Register
from src.utils.login.login import Login
from src.utils.user.user import User

load_dotenv()  # load .env

ROOT_DIR = Path(__file__).parent.parent  # getting root dir path
STATIC_DIR = (ROOT_DIR).joinpath('static')  # generating static dir path
TEMPLATES_DIR = (ROOT_DIR).joinpath(
    'templates')  # generating templates dir path


app = Flask(__name__,
            static_folder=STATIC_DIR,
            template_folder=TEMPLATES_DIR)  # init flask app

# assigning secret key for flask app
app.secret_key = os.getenv('APP_SECRET_KEY')


@app.route("/")  # route
def home_page():
    """Route for home page."""
    data = {"doc_title": "Home | Mindease"}
    return render_template("index.html", data=data)


@app.route('/register', methods=['POST', 'GET'])  # route
def register():
    """Route for account registration page."""
    form = ValidateRegister(request.form)
    if request.method == 'POST' and form.validate():
        hashed_pwd = encrypt_password(str.encode(form.password.data))

        user_data = {'first_name': form.first_name.data,
                     'last_name': form.last_name.data,
                     'email': form.email.data,
                     'password': hashed_pwd,
                     'birth': form.birth.data,
                     'gender': form.gender.data
                     }

        user = Register(user_data)
        result = user.register_user()

        if result['registration_succeeded']:
            flash(dedent("""\
                    Successfully registered.
                    We will notify you once our platform launches!"""),
                  "success")
        else:
            flash("Email already exists", "error")

    if session.get('user_id') is None:
        data = {"doc_title": "Register | Mindease", "register_form": form}
        return render_template("register.html", data=data)

    return redirect(url_for('myspace'))


@app.route('/login', methods=['GET', 'POST'])  # route
def login():
    """Route for login page."""
    form = ValidateLogin(request.form)
    if request.method == 'POST' and form.validate():

        user_data = {'email': form.email.data,
                     'password': form.password.data,
                     }

        init_login = Login()
        result = init_login.login(user_data['email'], user_data['password'])

        if result['login_succeeded']:
            user_id = load_user(user_data['email'])
            session['user_id'] = user_id

            return redirect(url_for('myspace'))

        if not result['login_succeeded']:
            try:
                result['invalid_password']

                flash("Password is incorrect", "error")
                return redirect(url_for('login'))

            except KeyError:
                flash("This email does not exist", "error")
                return redirect(url_for('login'))

    if session.get('user_id') is None:
        data = {"doc_title": "Login | Mindease", "login_form": form}
        return render_template("login.html", data=data)

    return redirect(url_for('myspace'))


@app.route('/logout')  # route
def logout():
    """Route to logout a user."""
    session.pop('user_id', None)

    flash("You have been successfully logged out", "success")
    return redirect(url_for('login'))


@app.route('/checkup')  # route
def checkup():
    """Route for user space."""
    user_id = session.get('user_id')

    if user_id is None:
        flash('You are not authenticated', 'error')
        return redirect('/login')

    data = {}
    return render_template("checkup.html", data=data)


@app.route('/myspace')  # route
def myspace():
    """Route for user space."""
    user_id = session.get('user_id')

    if user_id is None:
        flash('You are not authenticated', 'error')
        return redirect('/login')

    data = {}
    return render_template("space.html", data=data)


@app.route('/aboutus')  # route
def aboutus():
    """Route for about-us page."""
    data = {}
    return render_template("aboutus.html", data=data)


def load_user(email):
    """Load user id from database based on email."""
    user = User(email=email,
                name=None,
                password=None,
                birth=None,
                gender=None,
                user_id=None,
                doctor_key=None
                )

    return user.get_user_id(email)


def encrypt_password(password):
    """Encrypt registration password."""
    hashed_pwd = bcrypt.hashpw(password, bcrypt.gensalt(rounds=15))
    return hashed_pwd
