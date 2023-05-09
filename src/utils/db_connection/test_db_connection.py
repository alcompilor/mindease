#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unittest DBConnection module."""

import unittest
from src.utils.db_connection.db_connection import DBConnection


class TestDBConnection(unittest.TestCase):
    """Test DBConnection."""

    def test_init(self):
        """Test DBConnection constructor."""
        database = DBConnection()
        cursor = database.cursor

        query = "SELECT VERSION()"
        cursor.execute(query)
        row = cursor.fetchone()

        self.assertIsNotNone(row, "Connection Failed")
