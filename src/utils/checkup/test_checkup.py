#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Unittest Checkup class."""
import unittest
from unittest.mock import MagicMock
from datetime import datetime, timedelta
from src.utils.checkup.checkup import Checkup
from src.utils.db_connection.db_connection import DBConnection


# pylint: disable=too-many-instance-attributes # pylint: disable=R0902
class TestCheckupClass(unittest.TestCase):
    """Tests checkup class."""

    def setUp(self):
        """Unittest setup."""
        self.checkup = Checkup()

        self.db_connection = MagicMock(spec=DBConnection)
        self.db_connection.cursor = MagicMock()
        self.db_connection.cursor.fetchone = MagicMock()
        self.db_connection.cursor.execute = MagicMock()
        self.db_connection.cursor.close = MagicMock()
        self.db_connection.cnx = MagicMock()
        self.db_connection.cnx.close = MagicMock()

    def test_fetch_checkup(self):
        """Test fetch_checkup function."""
        self.db_connection.cursor.fetchone.return_value = None
        self.db_connection.cursor.fetchone.side_effect = [
            (1, "Did you sleep well today?"),
            (2, "Question 2"),
            (3, "Question 3"),
            (4, "Question 4"),
            (5, "Question 5"),
            (6, "Question 6"),
            (7, "Question 7"),
            (8, "Question 8"),
            (9, "Question 9"),
            (10, "Question 10"),
            (11, "Question 11"),
            (12, "Question 12"),
            (13, "Question 13"),
            (14, "Question 14"),
            (15, "Question 15"),
            (16, "Question 16"),
            (17, "Question 17"),
            (18, "Question 18"),
            (19, "Question 19"),
            (20, "Question 20"),
            (21, "Question 21"),
            (22, "Question 22"),
            (23, "Question 23"),
            (24, "Question 24"),
            (25, "Question 25"),
            (26, "Question 26"),
            (27, "Question 27"),
            (28, "Question 28"),
            (29, "Question 29"),
            (30, "Question 30"),
            (1, "Question 1")
        ]
        DBConnection.return_value = self.db_connection
        result = self.checkup.fetch_checkup(1)
        self.assertEqual(result, {"todays_checkup": {"id": 1, "content": "Did you sleep well today?"}})

    def test_check_answe_with_answer_registered(self):
        """Test check_answer function."""
        self.db_connection.cursor.fetchone.return_value = ("2023-05-14",)
        DBConnection.return_value = self.db_connection
        result = self.checkup.check_answer(1)
        self.assertEqual(result, {"new_checkup": False})
    
    def test_check_answer_with_answer_not_registered(self):
        """Test1."""
        self.db_connection.cursor.fetchone.return_value = None
        DBConnection.retutn_value = self.db_connection
        result = self.checkup.check_answer(1)
        self.assertEqual(result, {"new_checkup": True})

    def test_register_checkup_with_registered_answer(self):
        """Test refister_checkup function."""
        self.db_connection.cursor.execute.return_value = None
        self.db_connection.cnx.commit.return_value = None
        DBConnection.return_value = self.db_connection

        result = self.checkup.register_checkup(1, 1, "Answer 1", datetime.now())

        self.assertEqual(result, {"answer_registered": True})

    def test_register_checkup_with_not_registered(self):
        """Test."""
        self.db_connection.cursor.execute.side_effect = [None, Exception("Database error")]
        DBConnection.return_value = self.db_connection
        result = self.checkup.register_checkup(1, 1, "4")


if __name__ == '__main__':
    unittest.main()
