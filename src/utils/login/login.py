#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""login module."""

import bcrypt
from src.utils.db_connection.db_connection import DBConnection


class Login:
    """Login."""
    def __init__(self):
        """Login constructor."""
        self.conn = DBConnection()
        self.cursor = self.conn.cnx.cursor()

    def validate_password(self, email, password):
        """validate password function."""
        query = 'SELECT * FROM User WHERE email=%s LIMIT 1'
        self.cursor.execute(query, (email,))
        row = self.cursor.fetchone()

        if row is None:
            return {'hashed_password_found': False}

        hashed_password = row[4]

        if bcrypt.checkpw(password, hashed_password.encode('utf-8')):
            return {'matches': True}
        return {'matches': False}


    def login(self, email, password):
        """login function."""
        query = 'SELECT email FROM User WHERE email=%s'
        self.cursor.execute(query, (email,))
        row = self.cursor.fetchone()

        if row is not None:
            result = self.validate_password(email, password.encode('utf-8'))
            if result['matches'] is True:
                return {'login_succeeded': True}
            return {'login_succeeded': False, 'invalid_password': True}
        return {'login_succeeded': False, 'invalid_email': True}
