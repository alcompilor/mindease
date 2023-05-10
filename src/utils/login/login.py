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

    def close_cursor(self, cursor):
        """Close cursor function."""
        cursor.close()

    def validate_password(self, email, password):
        """Validate password function."""
        query = "SELECT * FROM User WHERE email=%s LIMIT 1"
        cursor = self.conn.cnx.cursor()
        cursor.execute(query, (email,))
        row = cursor.fetchone()

        self.close_cursor(cursor)

        if row is None:
            return {"hashed_password_found": False}

        hashed_password = row[4]

        if bcrypt.checkpw(password, hashed_password.encode("utf-8")):
            return {"matches": True}

    def login(self, email, password):
        """Login function."""
        query = "SELECT email FROM User WHERE email=%s"
        cursor = self.conn.cnx.cursor()
        cursor.execute(query, (email,))
        row = cursor.fetchone()
        self.close_cursor(cursor)

        if row is not None:
            result = self.validate_password(email, password.encode("utf-8"))
            self.conn.cnx.close()
            if result["matches"] is True:
                return {"login_succeeded": True}
        self.conn.cnx.close()
