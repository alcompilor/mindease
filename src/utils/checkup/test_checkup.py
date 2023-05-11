#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Unittest Checkup class."""
import unittest
from unittest.mock import patch
from datetime import datetime, timedelta
from unittest.mock import MagicMock
from src.utils.checkup.checkup import Checkup
from src.utils.db_connection.db_connection import DBConnection


# pylint: disable=too-many-instance-attributes # pylint: disable=R0902
class TestCheckupClass(unittest.TestCase):
    """Tests checkup class."""

    def setUp(self):
        """Unittest setup."""
        self.conn_mock = MagicMock(DBConnection)
        self.cursor_mock = MagicMock()
        self.conn_mock.cnx.cursor.return_value = self.cursor_mock
        self.checkup_instance = Checkup()

    def test_fetch_checkup(self):
        """Test fetch_checkup function."""
        self.setUp()
        user_id = 1
        query_result = (1, "How do you feel today?")
        self.cursor_mock.fetchone.return_value = None
        self.cursor_mock.execute.return_value = None
        self.cursor_mock.fetchone.return_value = query_result
        expected_output = {"todays_checkup": {"id": 1, "content": "How do you feel today?"}}
        result = self.checkup_instance.fetch_checkup(user_id)
        self.assertEqual(result, expected_output)

    def test_check_answer(self):
        """Test check_answer function."""
        self.setUp()
        user_id = 1
        query_result = (datetime.today().date() - timedelta(days=1),)
        self.cursor_mock.fetchone.return_value = query_result
        expected_output = {"new_checkup": True}
        result = self.checkup_instance.check_answer(user_id)
        self.assertEqual(result, expected_output)

    def test_register_checkup(self):
        """Test refister_checkup function."""
        self.setUp()
        checkup_id = 1
        user_id = 1
        answer = "Good"
        answer_date = datetime.today().date()
        self.cursor_mock.execute.return_value = None
        self.conn_mock.cnx.commit.return_value = None
        expected_output = {"answer_registerd": True}
        result = self.checkup_instance.register_checkup(checkup_id, user_id, answer, answer_date)
        self.assertEqual(result, expected_output)

    def test_error_on_query(self):
        """Test try 2"""
        self.cursor_mock.return_value = self.cursor_mock

    @patch('src.checkup.DBConnection')
    def test_fetch_checkup_2(self, mock_db_connection):
        """Test."""
        checkup = Checkup()
        mock_cursor = mock_db_connection.return_value.cnx.cursor.return_value
        mock_cursor.fetchone.return_value = (1, 'How do you feel today?')
        result = checkup.fetch_checkup(1)
        self.assertEqual(result, {"todays_checkup": {"id": 1, "content": "How is your day?"}})
    
    @patch('src.checkup.DBConnection')
    def test_check_answer_new_answer(self, mock_db_connection):
        """Test1."""
        checkup = Checkup()
        mock_cursor = mock_db_connection.return_value.cnx.cursor.return_value 
        mock_cursor.fetchone.return_value = None
        result = Checkup.check_answer(1)
        self.assertEqual(result, {"new_checkup": True})
        
    @patch('src.checkup.DBConnection')
    def test_check_answer_old_answer(self, mock_db_connection):
        """Try."""
        checkup = Checkup()
        mock_cursor = mock_db_connection.return_value.cnx.cursor.return_value
        mock_cursor.fetchone.return_value = ('2023-05-10',)
        result = checkup.check_answer(1)
        self.assertEqual(result, {"new_checkup": False})
    
    @patch('src.checkup.DBConnection')
    def test_register_checkup_num(self, mock_db_connection):
        """Test reg."""
        checkup = Checkup()
        mock_cursor = mock_db_connection.return_value.cnx.cursor.return_value
        mock_cursor.execute.return_value = None
        mock_db_connection.return_value.cnx.commit.return_value = None
        result = checkup.register_checkup(1, 1, 'test answer', datetime.now().date())
        self.assertEqual(result, {"answer_registered": True})


if __name__ == '__main__':
    unittest.main()
