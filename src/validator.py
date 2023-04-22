#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Validator module."""
import datetime

from wtforms import (
    Form,
    BooleanField,
    StringField,
    PasswordField,
    EmailField,
    SelectField,
    DateField,
    validators,
    ValidationError
)


def validate_date_of_birth(form, field):
    """Validate minimum age."""
    date_of_birth = datetime.datetime.strptime(f"{field.data}",
                                               '%Y-%m-%d')
    minimum_age_date = (datetime.datetime.now() -
                        datetime.timedelta(days=13*365))

    if date_of_birth > minimum_age_date:
        raise ValidationError("You must be at least 13 years old")


def get_min_year(date_type):
    """Return max/min date to show on register form."""
    if date_type == "max":
        return (datetime.datetime.now() -
                datetime.timedelta(days=13*365)).date()

    return (datetime.datetime.now() -
            datetime.timedelta(days=90*365)).date()


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
        ],
        id="email",
        render_kw={"placeholder": "john.smith@gmail.com"},
    )

    password = PasswordField(
        "New Password",
        validators=[
            validators.DataRequired(message="Password is required"),
            validators.EqualTo("password_confirm",
                               message="Passwords must match"),
            validators.Length(
                min=8, max=50,
                message="Password must be between 8 and 50 characters"
            ),
        ],
        id="password",
        render_kw={"placeholder": "Enter a password"},
    )

    password_confirm = PasswordField(
        "Repeat Password",
        validators=[
            validators.DataRequired(
                message="Password confirmation sis required")
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
        validators=[validators.DataRequired(
            message="Date of birth is required"),
            validate_date_of_birth, validators.NumberRange(
                max=f"{get_min_year('max')}", min=f"{get_min_year('min')}",
                message="Date of birth is invalid"
        )],
        id="date-birth",
        format="%Y-%m-%d",
    )

    accept_tos = BooleanField(
        validators=[
            validators.DataRequired(
                message="You must accept terms & conditions")
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
                min=8, max=50,
                message="Password is between 8 and 50 characters"
            ),
        ],
        id="password",
        render_kw={"placeholder": "Your password"},
    )
