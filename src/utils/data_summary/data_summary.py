#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""data_summary module."""
from src.utils.db_connection.db_connection import DBConnection
from src.utils.user.user import User

import mysql.connector


class DataSummary:
    """DataSummary class."""

    def __init__(self):
        """DATASUMMARY constructor."""
        self.conn = DBConnection()
        self.user = User()
        self.first_name = None
        self.last_name = None
        self.birth = None
        self.gender = None
        self.doctor_key = None

    def get_id(self, email):
        try:
            query = (
                'SELECT user_id FROM User WHERE email = %s;'
            )

            cursor = self.conn.cnx.cursor()
            cursor.execute(query, (email,))
            row = cursor.fetchone()
            self.conn.cnx.commit()

            cursor.close()

            return row
        except mysql.connector.Error as err:
            return err

    def get_checkup_info(self, email):
        try:
            query = (
                'SELECT c.checkup_content, ca.answer, ca.answer_date '
                'FROM User u '
                'LEFT JOIN Checkup c ON c.checkup_id = c.checkup_id '
                'LEFT JOIN Checkup_answer ca ON ca.user_id = u.user_id '
                'AND ca.checkup_id = c.checkup_id '
                'WHERE u.email = %s;'
            )

            cursor = self.conn.cnx.cursor()
            cursor.execute(query, (email,))
            rows = cursor.fetchall()
            cursor.close()

            return rows
        except mysql.connector.Error as err:
            return err

    def get_data_summary(self, email):
        """DATASUMMARY get_data_summary function."""
        uid = self.get_id(email)

        self.first_name = self.user.get_first_name(email)
        self.last_name = self.user.get_last_name(email)
        self.birth = self.user.get_birth(email)
        self.gender = self.user.get_gender(email)
        self.doctor_key = self.user.get_doctor_key(int(uid[0]))

        rows = self.get_checkup_info(email)

        result = {
            "first_name": self.first_name["first_name"],
            "last_name": self.last_name["last_name"],
            "birth": self.birth["birth"],
            "gender": self.gender["gender"],
            "doctor_key": self.doctor_key["doctor_key"],
            "checkups": {
                "checkups_sentences": [],
                "checkups_answers": [],
                "checkups_date": [],
            },
        }

        for checkup_row in rows:
            result["checkups"]["checkups_sentences"].append(checkup_row[0])
            result["checkups"]["checkups_answers"].append(checkup_row[1])
            result["checkups"]["checkups_date"].append(checkup_row[2])

        self.conn.cnx.close()

        return result
