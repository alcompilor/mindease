#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""unittest Register module."""

import unittest
from unittest.mock import MagicMock
from src.utils.register.register import Register
from src.utils.db_connection.db_connection import DBConnection


class TestRegister(unittest.TestCase):
    """Test Register."""

    def test_register_user(self):
        """Test register_user Function."""
        user = {
            "first_name": "Jackson",
            "last_name": "Reacher",
            "email": "new_user@gmail.com",
            "password": "Mohammed2000@",
            "birth": "1955.05.05",
            "gender": "male",
        }

        conn_mock = MagicMock(DBConnection())
        cursor_mock = MagicMock()
        cnx_mock = MagicMock()

        conn_mock.cnx.cursor = cursor_mock
        conn_mock.cnx = cnx_mock

        cursor_mock.fetchone.return_value = None

        with unittest.mock.patch(
            "src.utils.db_connection.db_connection.DBConnection",
            return_value=conn_mock,
        ):
            reg = Register(user)
            user_reg = reg.register_user()

        if user_reg.get("registration_succeeded") is True:
            self.assertTrue(True)
        else:
            self.assertFalse(True, "Registration failed")
