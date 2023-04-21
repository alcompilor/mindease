#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Validator module."""

from wtforms import (
    Form,
    BooleanField,
    StringField,
    PasswordField,
    EmailField,
    SelectField,
    DateField,
    validators,
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
            message="Date of birth is required")],
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
