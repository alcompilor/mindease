#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""unittest login module."""

import unittest
from unittest.mock import MagicMock
from src.utils.db_connection.db_connection import DBConnection
from src.utils.login.login import Login


class TestLogin(unittest.TestCase):
    """Test Login."""

    def setUp(self):
        """Unittest setup."""
        self.conn_mock = MagicMock(DBConnection())
        self.cursor_mock = MagicMock()
        self.conn_mock.cnx.cursor.return_value = self.cursor_mock

        self.login_instance = Login()

    def test_validate_password(self):
        """Test validate_password function."""
        self.setUp()
        email = "alkatebmohammed383@gmail.com"
        password = "Mohammed2001@"

        self.assertEqual(
            self.login_instance.validate_password(
                email, password.encode("utf-8")
            ),
            {"matches": True},
            {"matches": False},
        )

    def test_login(self):
        """Test login function."""
        email = "alkatebmohammed383@gmail.com"
        password = "Mohammed2001@"

        self.setUp()
        self.cursor_mock.fetchone.return_value = (email,)

        pwd_validation = self.login_instance.validate_password(
            email, password.encode("utf-8")
        )
        self.assertEqual(pwd_validation, {"matches": True})

        with unittest.mock.patch(
            "src.utils.db_connection.db_connection.DBConnection",
            return_value=self.conn_mock,
        ):
            result = self.login_instance.login(email, password)

        self.assertEqual(result, {"login_succeeded": True})
