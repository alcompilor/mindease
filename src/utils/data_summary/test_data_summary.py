#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unittest DataSummary module."""

import unittest
from unittest.mock import MagicMock
from src.utils.data_summary.data_summary import DataSummary
from src.utils.db_connection.db_connection import DBConnection


class TestDataSummary(unittest.TestCase):
    """Test DataSummary class."""

    def setUp(self):
        """Unittest setup."""
        self.conn_mock = MagicMock(DBConnection())
        self.cursor_mock = MagicMock()
        self.conn_mock.cnx.cursor.return_value = self.cursor_mock

        self.email = "johndoe@email.com"
        self.data_summary = DataSummary()

    def test_get_id(self):
        user_id = self.data_summary.get_id(self.email)
        self.assertIsNotNone(user_id)

    def test_get_checkup_info(self):
        checkup_info = self.data_summary.get_checkup_info(self.email)
        self.assertIsNotNone(checkup_info)

    def test_get_data_summary(self):
        """Test get_data_summary function."""
        self.setUp()

        expected_checkups = [
            {
                "content": "Did you sleep well today?",
                "answer": None,
                "date": None,
            },
            {
                "content": "Did you start your day with a healthy "
                "breakfast today?",
                "answer": None,
                "date": None,
            },
            {
                "content": "Have you been drinking enough water lately?",
                "answer": None,
                "date": None,
            },
            {
                "content": "Did you get some fresh air today?",
                "answer": None,
                "date": None,
            },
            {
                "content": "Have you been feeling energized lately?",
                "answer": None,
                "date": None,
            },
            {
                "content": "Did you have a chance to do some exercise today?",
                "answer": None,
                "date": None,
            },
            {
                "content": "Are you feeling relaxed and calm today?",
                "answer": None,
                "date": None,
            },
            {
                "content": "Did you have a good night's sleep last night?",
                "answer": None,
                "date": None,
            },
            {
                "content": "Have you been taking breaks throughout the day to"
                " stretch or move around?",
                "answer": None,
                "date": None,
            },
            {
                "content": "Did you have a chance to spend time in nature today?",
                "answer": None,
                "date": None,
            },
            {
                "content": "Are you feeling well-rested today?",
                "answer": None,
                "date": None,
            },
            {
                "content": "Have you been able to manage stress effectively "
                "lately?",
                "answer": None,
                "date": None,
            },
            {
                "content": "Did you have a nutritious lunch today?",
                "answer": None,
                "date": None,
            },
            {
                "content": "Are you feeling productive and focused today?",
                "answer": None,
                "date": None,
            },
            {
                "content": "Did you take time to unwind and relax before bed "
                "last night?",
                "answer": None,
                "date": None,
            },
            {
                "content": "Are you feeling motivated and inspired today?",
                "answer": None,
                "date": None,
            },
            {
                "content": "Did you have a good workout or physical "
                "activity today?",
                "answer": None,
                "date": None,
            },
            {
                "content": "Are you feeling positive and optimistic today?",
                "answer": None,
                "date": None,
            },
            {
                "content": "Did you have a healthy snack today?",
                "answer": None,
                "date": None,
            },
            {
                "content": "Are you feeling alert and awake today?",
                "answer": None,
                "date": None,
            },
            {
                "content": "Did you take time to meditate or practice "
                "mindfulness today?",
                "answer": None,
                "date": None,
            },
            {
                "content": "Are you feeling physically strong today?",
                "answer": None,
                "date": None,
            },
            {
                "content": "Did you have a chance to do something you "
                "enjoy today?",
                "answer": None,
                "date": None,
            },
            {
                "content": "Are you feeling optimistic about your health "
                "and well-being?",
                "answer": None,
                "date": None,
            },
            {
                "content": "Did you have a nutritious dinner tonight?",
                "answer": None,
                "date": None,
            },
            {
                "content": "Are you feeling fulfilled and satisfied today?",
                "answer": None,
                "date": None,
            },
            {
                "content": "Did you take time to connect with loved ones today?",
                "answer": None,
                "date": None,
            },
            {
                "content": "Are you feeling confident and self-assured today?",
                "answer": None,
                "date": None,
            },
            {
                "content": "Did you have a chance to laugh and have fun today?",
                "answer": None,
                "date": None,
            },
            {
                "content": "Are you feeling grateful for your health and "
                "well-being today?",
                "answer": None,
                "date": None,
            },
        ]

        self.cursor_mock.fetchall.return_value = expected_checkups

        actual_result = self.data_summary.get_data_summary(self.email)

        expected_result = {
            "first_name": self.data_summary.first_name["first_name"],
            "last_name": self.data_summary.last_name["last_name"],
            "birth": self.data_summary.birth["birth"],
            "gender": self.data_summary.gender["gender"],
            "doctor_key": self.data_summary.doctor_key["doctor_key"],
            "checkups": {
                "checkups_sentences": [],
                "checkups_answers": [],
                "checkups_date": [],
            },
        }

        for element in expected_checkups:
            expected_result["checkups"]["checkups_sentences"].append(
                element["content"]
            )
            expected_result["checkups"]["checkups_answers"].append(
                element["answer"]
            )
            expected_result["checkups"]["checkups_date"].append(
                element["date"]
            )

        self.assertEqual(expected_result, actual_result, "Failed")
