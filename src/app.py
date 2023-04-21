#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Flask module."""

import os
from pathlib import Path
from textwrap import dedent
from flask import Flask, render_template, request, flash
import bcrypt
from dotenv import load_dotenv
from src.validator import ValidateRegister
from src.utils.register.register import Register

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
def register_page():
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
        user.register_user()

        flash(dedent("""\
            Successfully registered.
            We will notify you once our platform launches!"""))

    data = {"doc_title": "Register | Mindease", "register_form": form}
    return render_template("register.html", data=data)


@app.route("/thankyou")  # TEMPORARY route
def comingsoon_page():
    """Route for coming soon page."""
    data = {"doc_title": "Thank You | Mindease"}
    return render_template("comingsoon.html", data=data)


def encrypt_password(password):
    """Encrypt registration password."""
    hashed_pwd = bcrypt.hashpw(password, bcrypt.gensalt(rounds=15))
    return hashed_pwd
