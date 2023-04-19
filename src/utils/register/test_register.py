#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" unittest Register module."""

import unittest
from src.utils.register.register import Register
from src.utils.db_connection.db_connection import DBConnection


class TestRegister(unittest.TestCase):
    """Test Register."""

    def test_register_user(self):
        """Test Register_user Function."""

        user = {
            'first_name': 'Mohammed',
            'last_name': 'Alkateb',
            'email': 'jackreachers@gmail.com',
            'password': 'pass1234',
            'age': 30,
            'gender': 'males'
        }

        conn = DBConnection()
        cursor = conn.cnx.cursor()
        param = (user['email'],)

        query = 'SELECT * FROM User WHERE email=%s'
        cursor.execute(query, param)
        row = cursor.fetchone()
        self.assertTrue(row is None or
            len(row) == 0)

        reg = Register()
        user_register = reg.register_user(user)

        self.assertEqual(user_register, {'registration_succeeded': True}, 'Registration failed')
