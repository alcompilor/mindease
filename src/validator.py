#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Validator module."""
import datetime
from validate_email import validate_email
from wtforms import (
    Form,
    BooleanField,
    StringField,
    PasswordField,
    EmailField,
    SelectField,
    DateField,
    TextAreaField,
    IntegerRangeField,
    validators,
    ValidationError,
)
from src.utils.db_connection.db_connection import DBConnection


def validate_date_of_birth(form, field):  # pylint: disable=W0613
    """Validate minimum age."""
    date_of_birth = datetime.datetime.strptime(f"{field.data}", "%Y-%m-%d")
    today = datetime.date.today()

    age = (
        today.year
        - date_of_birth.year
        - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
    )

    if age < 13:
        raise ValidationError("You must be at least 13 years old")
    if age > 90:
        raise ValidationError("You must be at most 90 years old")


def validate_submission_date(form, field):  # pylint: disable=W0613
    """Validate submission date for journal."""
    fetched_date = datetime.datetime.strptime(f"{field.data}", "%Y-%m-%d")
    current_date = datetime.datetime.now().replace(
        hour=0, minute=0, second=0, microsecond=0
    )

    if fetched_date != current_date:
        raise ValidationError("An error occured: Submission date is invalid")


def validate_user_email(form, field):  # pylint: disable=W0613
    """Validate registered email."""
    email = field.data

    is_valid = validate_email(email, smtp_timeout=1)

    if is_valid is False:
        raise ValidationError(f"{email} does not appear to exist")


def validate_doctor_key_db(form, field):  # pylint: disable=W0613
    """Validate if doctor key exists in database."""
    query = "SELECT user_id FROM User WHERE doctor_key = %s;"
    data = field.data

    db_conn = DBConnection()
    db_conn.cursor.execute(query, (data,))

    result = db_conn.cursor.fetchone()

    db_conn.cursor.close()
    db_conn.cnx.close()

    if not result:
        raise ValidationError(
            "The patient's key you entered does not appear to exist"
        )


class ValidateRegister(Form):
    """Register Validator to validate client side register form."""

    first_name = StringField(
        "First Name",
        validators=[
            validators.Length(min=1, max=35, message="First Name is invalid"),
            validators.DataRequired(message="First Name is required"),
        ],
        id="first-name",
        render_kw={"placeholder": "John"},
    )

    last_name = StringField(
        "Last Name",
        validators=[
            validators.Length(min=1, max=35, message="Last Name is invalid"),
            validators.DataRequired(message="Last Name is required"),
        ],
        id="last-name",
        render_kw={"placeholder": "Smith"},
    )

    email = EmailField(
        "Email",
        validators=[
            validators.Length(min=1, max=254, message="Email is invalid"),
            validators.Email(message="Email is invalid"),
            validators.DataRequired(message="Email is required"),
            validate_user_email,
        ],
        id="email",
        render_kw={"placeholder": "john.smith@gmail.com"},
    )

    password = PasswordField(
        "New Password",
        validators=[
            validators.DataRequired(message="Password is required"),
            validators.EqualTo(
                "password_confirm", message="Passwords must match"
            ),
            validators.Regexp(
                r"(?=.*?[A-Z])", message="Missing uppercase letter"
            ),
            validators.Regexp(
                r"(?=.*?[a-z])", message="Missing lowercase letter"
            ),
            validators.Regexp(r"(?=.*?[0-9])", message="Missing digit"),
            validators.Regexp(
                r"(?=.*?[#?!@$%^&*-])", message="Missing special character"
            ),
            validators.Regexp(r".{8,}", message="Password is too short"),
        ],
        id="password",
        render_kw={"placeholder": "Enter a password"},
    )

    password_confirm = PasswordField(
        "Repeat Password",
        validators=[
            validators.DataRequired(
                message="Password confirmation sis required"
            )
        ],
        id="password-confirm",
        render_kw={"placeholder": "Re-enter password"},
    )

    gender = SelectField(
        "Gender",
        choices=[("male", "Male"), ("female", "Female")],
        validators=[validators.DataRequired(message="Gender is required")],
        id="gender",
    )

    birth = DateField(
        "Date of Birth",
        validators=[
            validators.DataRequired(message="Date of birth is required"),
            validate_date_of_birth,
        ],
        id="date-birth",
        format="%Y-%m-%d",
    )

    accept_tos = BooleanField(
        validators=[
            validators.DataRequired(
                message="You must accept terms & conditions"
            )
        ],
        id="tos",
    )


class ValidateLogin(Form):
    """Login Validator to validate client side login form."""

    email = EmailField(
        "Email",
        validators=[
            validators.Length(min=1, max=254, message="Email is invalid"),
            validators.Email(message="Email is invalid"),
            validators.DataRequired(message="Email is required"),
        ],
        id="email",
        render_kw={"placeholder": "Your email"},
    )

    password = PasswordField(
        "Password",
        validators=[
            validators.DataRequired(message="Password is required"),
            validators.Length(
                min=8,
                max=50,
                message="Password is between 8 and 50 characters",
            ),
        ],
        id="password",
        render_kw={"placeholder": "Your password"},
    )


class ValidateJournal(Form):
    """Journal Validator to validate client side new journal form."""

    title = StringField(
        "Title",
        validators=[
            validators.DataRequired(message="Journal Title is required"),
            validators.Length(
                min=1, max=30, message="Title is too long (>30 chars)"
            ),
        ],
        id="journal-title",
        render_kw={"placeholder": "A memory from my childhood"},
    )

    content = TextAreaField(
        "Content",
        validators=[
            validators.DataRequired(message="Journal Content is required"),
            validators.Length(
                min=1, max=540, message="Content is too long (>520 chars)"
            ),
        ],
        id="journal-content",
        render_kw={"placeholder": "When I was a child I...", "rows": "14"},
    )

    date_submitted = DateField(
        "Date",
        validators=[
            validators.DataRequired(
                message="An error has occured: Date couldn't be processed."
            ),
            validate_submission_date,
        ],
        id="journal-submission-date",
    )


class ValidateCheckup(Form):
    """Checkup Validator to validate client side new checkup range."""

    checkup_range = IntegerRangeField(
        "Range",
        validators=[
            validators.DataRequired(message="Checkup value is required"),
            validators.NumberRange(
                min=1, max=5, message="Checkup value is invalid"
            ),
        ],
        id="emoji",
    )


class ValidateDoctorKey(Form):
    """Docotor_key validator to ensure that a doctor using valid doctor_key."""

    doctor_key = StringField(
        validators=[
            validators.DataRequired(message="A Patient's key is required"),
            validate_doctor_key_db,
        ],
        id="doctor_key",
        render_kw={"placeholder": "Enter the patient's key"},
    )
