#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Flask module."""

import os
from pathlib import Path
from textwrap import dedent
from datetime import datetime
import requests
from flask import (
    Flask,
    render_template,
    request,
    flash,
    url_for,
    redirect,
    session,
)
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

# APP INIT SECTION #

load_dotenv()  # load .env

ROOT_DIR = Path(__file__).parent.parent  # getting root dir path
STATIC_DIR = (ROOT_DIR).joinpath("static")  # generating static dir path
TEMPLATES_DIR = (ROOT_DIR).joinpath(
    "templates"
)  # generating templates dir path


app = Flask(
    __name__, static_folder=STATIC_DIR, template_folder=TEMPLATES_DIR
)  # init flask app
app.url_map.strict_slashes = False  # ignores trailing slash in routes

# assigning secret key for flask app
app.secret_key = os.getenv("APP_SECRET_KEY")


# ROUTES SECTION #


@app.route("/")  # homepage route
def home_page():
    """Route for home page."""
    data = {"doc_title": "Home | Mindease"}
    return render_template("index.html", data=data)


@app.route("/register", methods=["POST", "GET"])  # register route
def register():
    """Route for account registration page."""
    if is_loggedin():
        return redirect(url_for("myspace"))

    form = ValidateRegister(request.form)  # init register form
    if request.method == "POST" and form.validate():
        hashed_pwd = encrypt_password(str.encode(form.password.data))

        user_data = {
            "first_name": form.first_name.data,
            "last_name": form.last_name.data,
            "email": form.email.data,
            "password": hashed_pwd,
            "birth": form.birth.data,
            "gender": form.gender.data,
        }  # data fetched from register form

        try_register(user_data)  # attempt to register user

    data = {"doc_title": "Register | Mindease", "register_form": form}
    return render_template("register.html", data=data)


@app.route("/login", methods=["GET", "POST"])  # login route
def login():
    """Route for login page."""
    if is_loggedin():
        return redirect(url_for("myspace"))

    form = ValidateLogin(request.form)  # init login form
    if request.method == "POST" and form.validate():
        user_data = {
            "email": form.email.data,
            "password": form.password.data,
        }  # data fetched from login form

        return try_login(user_data)  # attempt to login & return result

    data = {"doc_title": "Login | Mindease", "login_form": form}
    return render_template("login.html", data=data)


@app.route("/logout")  # logout route
def logout():
    """Route to logout a user."""
    session.clear()  # clear all session keys

    flash("You have been successfully logged out", "success")
    return redirect(url_for("login"))


@app.route("/checkup", methods=["GET", "POST"])  # checkup route
def checkup():
    """Route for user space."""
    if not is_loggedin():  # check if user is authenticated
        flash("You are not authenticated", "error")
        return redirect("/login")

    if not control_checkup():  # control if new checkup is required
        return redirect(url_for("myspace"))

    form = ValidateCheckup(request.form)
    if request.method == "POST" and form.validate():
        try_checkup(
            "register", data=form.checkup_range.data
        )  # register todays checkup data
        return redirect(url_for("myspace"))

    todays_checkup = try_checkup("display", data=None)  # fetch todays checkup

    data = {
        "doc_title": "Checkup | Mindease",
        "checkup_form": form,
        "checkup": todays_checkup,
    }
    return render_template("checkup.html", data=data)


@app.route("/myspace")  # myspace route
def myspace():
    """Route for user space."""
    if not is_loggedin():  # check if user is authenticated
        flash("You are not authenticated", "error")
        return redirect("/login")

    if control_checkup():  # control if new checkup is required
        return redirect(url_for("checkup"))

    doctor_key = fetch_doctor_key()  # fetch user doctor key
    assertion = get_assertion()  # fetch assertion from external API

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
    if not is_loggedin():  # check if user is authenticated
        flash("You are not authenticated", "error")
        return redirect("/login")

    if control_checkup():  # control if new checkup is required
        return redirect(url_for("myspace"))

    form = ValidateJournal(request.form)
    if request.method == "POST" and form.validate():
        journal_data = {
            "title": form.title.data,
            "content": form.content.data,
            "date": form.date_submitted.data,
            "user_id": session["user_id"]["user_id"],
        }

        try_journal(
            "register", journal_data, None
        )  # attempt to save a journal

    fetched_journals = try_journal(
        "display", None, request
    )  # attempt to fetch journals

    data = {
        "doc_title": "My Space - Journals | Mindease",
        "journal_form": form,
        "user_journals": fetched_journals,
    }
    return render_template("space-journals.html", data=data)


@app.route("/aboutus")  # about us route
def aboutus():
    """Route for about us page."""
    data = {"doc_title": "About Us | Mindease"}
    return render_template("aboutus.html", data=data)


@app.route("/analysis", methods=["GET", "POST"])  # analysis (doctorform) route
def doctor_form():
    """Route for psychologist portal (doctor form)."""
    form = ValidateDoctorKey(request.form)
    if request.method == "POST" and form.validate():
        session["doctor_key"] = form.doctor_key.data
        return redirect(url_for("doctor_view"))

    data = {"doc_title": "Psychologist Portal | Mindease", "doctor_form": form}
    return render_template("doctorform.html", data=data)


@app.route("/analysis/data", methods=["GET", "POST"])  # analysis/data route
def doctor_view():
    """Fetch patient records to be viewed by the doctor."""
    if (
        session.get("doctor_key") is None
    ):  # check if theres a valid doctor key in session
        return redirect(url_for("doctor_form"))

    doctor_key = session["doctor_key"]

    user = User()
    user_id = user.get_user_id(
        None, doctor_key=doctor_key
    )  # fetch user_id based on doctor_key

    user_email = user.get_email(
        user_id["user_id"]
    )  # fetch user email based on user_id

    curr_month_year = datetime.today().strftime("%Y-%m")

    journal = Journal()
    fetched_journals = journal.search_journals(
        user_id["user_id"], curr_month_year
    )  # fetch all journals based on "curr_month_year" variable
    data_summary = DataSummary()

    data_summary_result = data_summary.get_data_summary(
        user_email["email"]
    )  # fetch user data

    user.update_doctor_key(doctor_key)  # generate new doctor key to user
    session.pop("doctor_key", None)  # force doctor key session to expire

    data = {
        "doc_title": "Psychologist View | Mindease",
        "journals": fetched_journals,
        "data_summary_result": data_summary_result,
    }

    return render_template("doctor-view.html", data=data)


@app.errorhandler(404)
def page_not_found(err):
    """Handle 404 errors, custom page."""
    data = {"doc_title": "Page not found | Mindease", "e": err}
    return render_template("404.html", data=data), 404


# UTILS FUNCTIONS SECTION #


def load_user(email):
    """Load user id from database based on user's email."""
    user = User()

    return user.get_user_id(email, doctor_key=None)


def encrypt_password(password):
    """Encrypt/hash registration password."""
    hashed_pwd = bcrypt.hashpw(password, bcrypt.gensalt(rounds=15))
    return hashed_pwd


def get_assertion():
    """Fetch an assertion from an external api."""
    url = "https://www.affirmations.dev"

    response = requests.get(url, timeout=3)  # get req
    result = response.json()  # convert to json

    return result["affirmation"]


def is_loggedin():
    """Check wether a user is logged in or not."""
    if session.get("user_id") is None:
        return False
    return True


def fetch_doctor_key():
    """Fetch doctor key for a specific user."""
    init_user = User()
    doctor_key = init_user.get_doctor_key(session["user_id"]["user_id"])
    return doctor_key


def fetch_data_summary(email):
    """Fetch data summary for a specific user."""
    user_id = load_user(email)

    session["user_id"] = user_id
    session["user_email"] = email

    data_summary = DataSummary().get_data_summary(session.get("user_email"))

    session["data_summary"] = data_summary


def control_checkup():
    """Check if a new checkup is required."""
    init_checkup = Checkup().check_answer(session["user_id"]["user_id"])

    new_checkup = init_checkup["new_checkup"]

    if not new_checkup:
        return False
    return True


def try_journal(action, journal_data, j_request):
    """Attempt to display or register journals."""
    journal = Journal()  # init journal object

    match action:  # logic based on action type
        case "register":
            result = journal.create_journal(
                journal_title=journal_data["title"],
                journal_content=journal_data["content"],
                journal_date=journal_data["date"],
                user_id=journal_data["user_id"],
            )  # saves journal to db

            if result["journal_created"]:  # flash msg based on status
                return flash("Journal has been saved", "success")
            return flash("An error occured: Journal not saved", "error")

        case "display":
            if not j_request.args.get("q"):  # if it's NOT a search
                fetched_journals = journal.get_all_journals(
                    session["user_id"]["user_id"]
                )
                return fetched_journals

            search_query = j_request.args.get("q")  # if it's a search
            fetched_journals = journal.search_journals(
                session["user_id"]["user_id"], search_query
            )
            return fetched_journals


def try_checkup(action, data):
    """Attempt to display or register new checkup."""
    init_checkup = Checkup()  # init checkup object

    match action:  # logic based on action type
        case "register":
            checkup_data = {
                "u_id": session["user_id"]["user_id"],
                "c_id": session["t_checkup"],
                "answer": data,
                "answer_date": datetime.today().date(),
            }

            init_checkup.register_checkup(
                checkup_data["c_id"],
                checkup_data["u_id"],
                checkup_data["answer"],
                checkup_data["answer_date"],
            )  # saves checkup to db

            session.pop(
                "t_checkup", None
            )  # remove current checkup from session

        case "display":
            t_checkup = init_checkup.fetch_checkup(
                session["user_id"]["user_id"]
            )  # fetches new checkup
            session["t_checkup"] = t_checkup["todays_checkup"]["id"]
            return t_checkup


def try_login(user_data):
    """Attempt to login user."""
    init_login = Login()  # init login object
    result = init_login.login(
        user_data["email"], user_data["password"]
    )  # attempt login

    match result["login_succeeded"]:  # logic based on login status
        case True:  # if success
            fetch_data_summary(user_data["email"])

            if control_checkup():  # control if new checkup is required
                return redirect(url_for("checkup"))

            return redirect(url_for("myspace"))

        case False | None:  # if fail
            try:  # invalid password
                result["invalid_password"]  # pylint: disable=W0104

                flash("Password is incorrect", "error")
                return redirect(url_for("login"))

            except KeyError:  # invalid email
                flash("This email does not exist", "error")
                return redirect(url_for("login"))


def try_register(user_data):
    """Try to register a user."""
    init_register = Register(user_data)  # init register object w user data
    result = init_register.register_user()  # register user

    match result[
        "registration_succeeded"
    ]:  # flash msg based on register result
        case True:  # if success
            return flash(
                dedent(
                    """\
                    Successfully registered.
                    To continue, please login."""
                ),
                "success",
            )
        case False | None:  # if fail
            return flash("Email already exists", "error")
