#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Validator module."""

from wtforms import (Form, BooleanField, StringField, PasswordField,
                     EmailField, SelectField, DateField, validators)


class ValidateRegister(Form):
    """Register Validator to validate client side register form."""

    first_name = StringField('First Name', validators=[validators.Length(
        min=1, max=35), validators.DataRequired()], id="first-name")

    last_name = StringField('Last Name', validators=[validators.Length(
        min=1, max=35), validators.DataRequired()], id="last-name")

    email = EmailField('Email', validators=[validators.Length(
        min=1, max=254), validators.Email(), validators.DataRequired()],
        id="email")

    password = PasswordField('New Password', validators=[
        validators.DataRequired(),
        validators.EqualTo('password_confirm', message='Passwords must match')
    ], id="password")

    password_confirm = PasswordField('Repeat Password', validators=[
        validators.DataRequired()], id="password-confirm")

    gender = SelectField('Gender', choices=[('male', 'Male'),
                                            ('female', 'Female')],
                         validators=[validators.DataRequired()], id="gender")

    birth = DateField('Date of Birth',
                      validators=[validators.DataRequired()], id="date-birth")

    accept_tos = BooleanField(validators=[
                              validators.DataRequired()], id="tos")
