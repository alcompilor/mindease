#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Flask module."""

from pathlib import Path
from flask import Flask, render_template
<<<<<<< HEAD
=======
import bcrypt
>>>>>>> 994f0a9a5af7581c3020529fad2ed7db9a53d7e6

ROOT_DIR = Path(__file__).parent.parent  # getting root dir path
STATIC_DIR = (ROOT_DIR).joinpath('static')  # generating static dir path
TEMPLATES_DIR = (ROOT_DIR).joinpath(
    'templates')  # generating templates dir path


app = Flask(__name__,
            static_folder=STATIC_DIR,
            template_folder=TEMPLATES_DIR)  # init flask app


@app.route("/")  # route
def home_page():
    """Route for home page."""
    data = {"doc_title": "Home | Mindease"}
    return render_template("index.html", data=data)


@app.route("/register")  # route
def register_page():
    """Route for account registration page."""
    data = {"doc_title": "Register | Mindease"}
    return render_template("register.html", data=data)


@app.route("/thankyou")  # TEMPORARY route
def comingsoon_page():
    """Route for coming soon page."""
    data = {"doc_title": "Thank You | Mindease"}
    return render_template("comingsoon.html", data=data)
<<<<<<< HEAD
=======


def encrypt_password(password):
    """Encrypt registration password"""
    hashed_pwd = bcrypt.hashpw(password, bcrypt.gensalt(rounds=15))
    return {'hashed_password': hashed_pwd}
>>>>>>> 994f0a9a5af7581c3020529fad2ed7db9a53d7e6
