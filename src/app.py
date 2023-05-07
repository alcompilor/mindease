#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Flask module."""

import os
from pathlib import Path
from textwrap import dedent
from datetime import datetime
import requests
from flask import Flask, render_template, request, flash, url_for, redirect, session
import bcrypt
from dotenv import load_dotenv
from src.utils.register.register import Register
from src.utils.login.login import Login
from src.utils.user.user import User
from src.utils.journal.journal import Journal
from src.utils.data_summary.data_summary import DataSummary
from src.utils.checkup.checkup import Checkup
from src.validator import (
    ValidateRegister,
    ValidateLogin,
    ValidateJournal,
    ValidateCheckup,
    ValidateDoctorKey,
)

load_dotenv()  # load .env

ROOT_DIR = Path(__file__).parent.parent  # getting root dir path
STATIC_DIR = (ROOT_DIR).joinpath("static")  # generating static dir path
TEMPLATES_DIR = (ROOT_DIR).joinpath("templates")  # generating templates dir path


app = Flask(
    __name__, static_folder=STATIC_DIR, template_folder=TEMPLATES_DIR
)  # init flask app
app.url_map.strict_slashes = False  # ignores trailing slash in routes

# assigning secret key for flask app
app.secret_key = os.getenv("APP_SECRET_KEY")


@app.route("/")  # homepage route
def home_page():
    """Route for home page."""
    data = {"doc_title": "Home | Mindease"}
    return render_template("index.html", data=data)


@app.route("/register", methods=["POST", "GET"])  # register route
def register():
    """Route for account registration page."""
    form = ValidateRegister(request.form)
    if request.method == "POST" and form.validate():
        hashed_pwd = encrypt_password(str.encode(form.password.data))

        user_data = {
            "first_name": form.first_name.data,
            "last_name": form.last_name.data,
            "email": form.email.data,
            "password": hashed_pwd,
            "birth": form.birth.data,
            "gender": form.gender.data,
        }

        user = Register(user_data)
        result = user.register_user()

        if result["registration_succeeded"]:
            flash(
                dedent(
                    """\
                    Successfully registered.
                    To continue, please login."""
                ),
                "success",
            )
        else:
            flash("Email already exists", "error")

    if session.get("user_id") is None:
        data = {"doc_title": "Register | Mindease", "register_form": form}
        return render_template("register.html", data=data)

    return redirect(url_for("myspace"))


@app.route("/login", methods=["GET", "POST"])  # login route
def login():
    """Route for login page."""
    form = ValidateLogin(request.form)
    if request.method == "POST" and form.validate():
        user_data = {
            "email": form.email.data,
            "password": form.password.data,
        }

        init_login = Login()
        result = init_login.login(user_data["email"], user_data["password"])

        if result["login_succeeded"]:
            user_id = load_user(user_data["email"])
            session["user_id"] = user_id
            session["user_email"] = user_data["email"]
            data_summary = DataSummary().get_data_summary(session.get("user_email"))
            session["data_summary"] = data_summary

            init_checkup = Checkup().check_answer(session["user_id"]["user_id"])
            new_checkup = init_checkup["new_checkup"]

            if new_checkup:
                return redirect(url_for("checkup"))
            return redirect(url_for("myspace"))

        if not result["login_succeeded"]:
            try:
                result["invalid_password"]  # pylint: disable=W0104

                flash("Password is incorrect", "error")
                return redirect(url_for("login"))

            except KeyError:
                flash("This email does not exist", "error")
                return redirect(url_for("login"))

    if session.get("user_id") is None:
        data = {"doc_title": "Login | Mindease", "login_form": form}
        return render_template("login.html", data=data)

    return redirect(url_for("myspace"))


@app.route("/logout")  # logout route
def logout():
    """Route to logout a user."""
    session.pop("user_id", None)
    session.pop("user_email", None)

    flash("You have been successfully logged out", "success")
    return redirect(url_for("login"))


@app.route("/checkup", methods=["GET", "POST"])  # checkup route
def checkup():
    """Route for user space."""
    init_checkup = Checkup()
    form = ValidateCheckup(request.form)
    if request.method == "POST" and form.validate():
        checkup_data = {
            "u_id": session["user_id"]["user_id"],
            "c_id": session["t_checkup"],
            "answer": form.checkup_range.data,
            "answer_date": datetime.today().date(),
        }

        init_checkup.register_checkup(
            checkup_data["c_id"],
            checkup_data["u_id"],
            checkup_data["answer"],
            checkup_data["answer_date"],
        )

        session.pop("t_checkup", None)

    user_id = session.get("user_id")

    if user_id is None:
        flash("You are not authenticated", "error")
        return redirect("/login")

    new_checkup = init_checkup.check_answer(session["user_id"]["user_id"])[
        "new_checkup"
    ]

    if not new_checkup:
        return redirect(url_for("myspace"))

    t_checkup = init_checkup.fetch_checkup(session["user_id"]["user_id"])
    session["t_checkup"] = t_checkup["todays_checkup"]["id"]

    data = {
        "doc_title": "Checkup | Mindease",
        "checkup_form": form,
        "checkup": t_checkup,
    }
    return render_template("checkup.html", data=data)


@app.route("/myspace")  # myspace route
def myspace():
    """Route for user space."""
    user_id = session.get("user_id")

    if user_id is None:
        flash("You are not authenticated", "error")
        return redirect("/login")

    init_checkup = Checkup().check_answer(session["user_id"]["user_id"])
    new_checkup = init_checkup["new_checkup"]

    if new_checkup:
        return redirect(url_for("checkup"))

    init_user = User(None, None, None, None, None, None, None, None)
    doctor_key = init_user.get_doctor_key(user_id["user_id"])

    assertion = get_assertion()

    data = {
        "doc_title": "My Space | Mindease",
        "assertion": assertion,
        "doctor_key": doctor_key,
    }
    return render_template("space-main.html", data=data)


# myspace/journals route
@app.route("/myspace/journals", methods=["GET", "POST"])
def journals():
    """Route for user journals."""
    user_id = session.get("user_id")
    journal = Journal()

    form = ValidateJournal(request.form)
    if request.method == "POST" and form.validate():
        journal_data = {
            "title": form.title.data,
            "content": form.content.data,
            "date": form.date_submitted.data,
            "user_id": session["user_id"]["user_id"],
        }

        result = journal.create_journal(
            journal_title=journal_data["title"],
            journal_content=journal_data["content"],
            journal_date=journal_data["date"],
            user_id=journal_data["user_id"],
        )

        if result["journal_created"]:
            flash("Journal has been saved", "success")
        else:
            flash("An error occured: Journal not saved", "error")

    if user_id is None:
        flash("You are not authenticated", "error")
        return redirect("/login")

    init_checkup = Checkup().check_answer(session["user_id"]["user_id"])
    new_checkup = init_checkup["new_checkup"]

    if new_checkup:
        return redirect(url_for("checkup"))

    if not request.args.get("q"):
        fetched_journals = journal.get_all_journals(session["user_id"]["user_id"])
    else:
        search_query = request.args.get("q")
        fetched_journals = journal.search_journals(
            session["user_id"]["user_id"], search_query
        )

    data = {
        "doc_title": "My Space - Journals | Mindease",
        "journal_form": form,
        "user_journals": fetched_journals,
    }
    return render_template("space-journals.html", data=data)


@app.route("/aboutus")  # aboutus route
def aboutus():
    """Route for about-us page."""
    data = {"doc_title": "About Us | Mindease"}
    return render_template("aboutus.html", data=data)


@app.route("/analysis", methods=["GET", "POST"])  # analysis (doctorform) route
def doctor_form():
    """Implement doctor_key validation and redirects to doctor_view route if valid."""
    form = ValidateDoctorKey(request.form)

    if request.method == "POST" and form.validate():
        session["doctor_key"] = form.doctor_key.data
        return redirect(url_for("doctor_view"))

    data = {"doc_title": "Psychologist Portal | Mindease", "doctor_form": form}
    return render_template("doctorform.html", data=data)


@app.route("/analysis/data", methods=["GET", "POST"])  # analysis/data route
def doctor_view():
    """Fetch patient records to be viewed by the doctor."""
    if session.get("doctor_key") is None:
        return redirect(url_for("doctor_form"))

    doctor_key = session["doctor_key"]

    user = User(None, None, None, None, None, None, None, None)
    user_id = user.get_user_id(None, doctor_key=doctor_key)
    user_email = user.get_email(user_id["user_id"])

    curr_month_year = datetime.today().strftime("%Y-%m")

    journal = Journal()
    fetched_journals = journal.search_journals(user_id["user_id"], curr_month_year)

    data_summary = DataSummary()
    data_summary_result = data_summary.get_data_summary(user_email["email"])

    user.update_doctor_key(doctor_key)
    session.pop("doctor_key", None)

    data = {
        "doc_title": "Psychologist View | Mindease",
        "journals": fetched_journals,
        "data_summary_result": data_summary_result,
    }

    return render_template("doctor-view.html", data=data)


def load_user(email):
    """Load user id from database based on user's email."""
    user = User(
        email=email,
        first_name=None,
        last_name=None,
        password=None,
        birth=None,
        gender=None,
        user_id=None,
        doctor_key=None,
    )

    return user.get_user_id(email, doctor_key=None)


def encrypt_password(password):
    """Encrypt/hash registration password."""
    hashed_pwd = bcrypt.hashpw(password, bcrypt.gensalt(rounds=15))
    return hashed_pwd


def get_assertion():
    """Fetch an assertion from an external api."""
    url = "https://www.affirmations.dev"

    response = requests.get(url, timeout=3)
    result = response.json()

    return result["affirmation"]

