#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Register Module."""

import mysql.connector
from src.utils.db_connection.db_connection import DBConnection


class Register:
    """Register Class."""

    def __init__(self, user):
        """Register Constructor."""
        self.first_name = user['first_name']
        self.last_name = user['last_name']
        self.email = user['email']
        self.password = user['password']
        self.birth = user['birth']
        self.gender = user['gender']

    def register_user(self):
        """Register user function for Register class."""
        query = 'INSERT INTO User \
            (first_name, last_name, email, \
            password, birth, gender) VALUES \
            (%s, %s, %s, %s, %s, %s)'

        params = (
            self.first_name,
            self.last_name,
            self.email,
            self.password,
            self.birth,
            self.gender
        )

        try:
            conn = DBConnection()

            conn.cursor.execute(query, params)
            conn.cnx.commit()

            return {'registration_succeeded': True}

        except mysql.connector.Error as err:
            print(f'error: {err}')
            return {'registration_succeeded': False}

        conn.cursor.close()
        conn.cnx.close()
