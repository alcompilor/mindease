#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Register Module."""

import time
import secrets

import mysql.connector
from src.utils.db_connection.db_connection import DBConnection


class Register:
    """Register Class."""

    def __init__(self, user):
        """Register Constructor."""
        self.first_name = user["first_name"]
        self.last_name = user["last_name"]
        self.email = user["email"]
        self.password = user["password"]
        self.birth = user["birth"]
        self.gender = user["gender"]
        self.doctor_key = self.generate_doctor_key()

    def generate_doctor_key(self):
        """Generate a doctor key for the user."""
        key_length = secrets.choice(range(15, 21))
        key = secrets.token_urlsafe(key_length)

        timestamp = str(int(time.time() * 1000))
        key = f"{key}{timestamp}"

        return key

    def register_user(self):
        """Register user function for Register class."""
        query = "INSERT INTO User \
            (first_name, last_name, email, \
            password, birth, gender, doctor_key) VALUES \
            (%s, %s, %s, %s, %s, %s, %s)"

        params = (
            self.first_name,
            self.last_name,
            self.email,
            self.password,
            self.birth,
            self.gender,
            self.doctor_key,
        )

        try:
            conn = DBConnection()

            conn.cursor.execute(query, params)
            conn.cnx.commit()

            conn.cursor.close()
            conn.cnx.close()

            return {"registration_succeeded": True}

        except mysql.connector.Error as err:
            print(f"error: {err}")
            return {"registration_succeeded": False}
