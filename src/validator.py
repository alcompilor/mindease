#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Validator module."""

from wtforms import (Form, BooleanField, StringField, PasswordField,
                     EmailField, SelectField, DateField, validators)


class ValidateRegister(Form):
    """Register Validator to validate client side register form."""

    first_name = StringField('First Name', validators=[validators.Length(
        min=1, max=35), validators.DataRequired()])

    last_name = StringField('Last Name', validators=[validators.Length(
        min=1, max=35), validators.DataRequired()])

    email = EmailField('Email', validators=[validators.Length(
        min=1, max=254), validators.Email(), validators.DataRequired()])

    password = PasswordField('New Password', validators=[
        validators.DataRequired(),
        validators.EqualTo('password_confirm', message='Passwords must match')
    ])

    password_confirm = PasswordField('Repeat Password', validators=[
        validators.DataRequired()])

    gender = SelectField('Gender', choices=[('male', 'Male'),
                                            ('female', 'Female')],
                         validators=[validators.DataRequired()])

    birth = DateField('Date of Birth',
                      validators=[validators.DataRequired()])

    accept_tos = BooleanField(validators=[
                              validators.DataRequired()])
