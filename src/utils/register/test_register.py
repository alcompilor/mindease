#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" unittest Register module."""

import unittest
from src.utils.register.register import Register
from src.utils.db_connection.db_connection import DBConnection


class TestRegister(unittest.TestCase):
    """Test Register."""

    def test_register_user(self):
        """Test register_user Function."""

        user = {
            'first_name': 'Jackson',
            'last_name': 'Reacher',
            'email': 'jackreacher@gmail.com',
            'password': 'pass1234',
            'birth': '1955.05.05',
            'gender': 'male'
        }

        conn = DBConnection()
        cursor = conn.cnx.cursor()
        param = (user['email'],)

        query = 'SELECT * FROM User WHERE email=%s'
        cursor.execute(query, param)
        row = cursor.fetchone()
        self.assertTrue(row is None or
            len(row) == 0)

        reg = Register(user)
        user_reg = reg.register_user()

        self.assertEqual(user_reg, {'registration_succeeded': True}, 'Registration failed')
