"""Checkup integrated class."""

from datetime import datetime
import mysql.connector
from src.utils.db_connection.db_connection import DBConnection


class Checkup:
    """Checkup class."""

    def fetch_checkup(self, user_id):
        """Fetch new checkup for the day from the database."""
        try:
            db_conn = DBConnection()
            cursor = db_conn.cnx.cursor()

            query = """SELECT checkup_id FROM Checkup_answer WHERE
             user_id = %s AND answer_date
              IN (SELECT MAX(answer_date) FROM Checkup_answer WHERE user_id = %s);"""

            query2 = "SELECT * FROM Checkup WHERE checkup_id = %s"

            cursor.execute(
                query,
                (
                    user_id,
                    user_id,
                ),
            )

            result = cursor.fetchone()

            if result is not None:
                checkup_id = result[0] + 1
            else:
                checkup_id = 1

            if checkup_id < 31:
                cursor.execute(query2, (checkup_id,))
            else:
                checkup_id = 1
                cursor.execute(query2, (checkup_id,))

            new_checkup = cursor.fetchone()

            cursor.close()
            db_conn.cnx.close()

            return {
                "todays_checkup": {
                    "id": new_checkup[0],
                    "content": new_checkup[1],
                }
            }

        except mysql.connector.Error as err:
            return err

    def check_answer(self, user_id):
        """Check if the checkup answer with given user_id
        was stored in the last 24 hours or more."""
        try:
            db_conn = DBConnection()
            cursor = db_conn.cnx.cursor()

            query = """SELECT answer_date FROM Checkup_answer WHERE
             user_id = %s AND answer_date = (SELECT MAX(answer_date)
              FROM Checkup_answer WHERE user_id = %s);"""

            cursor.execute(
                query,
                (
                    user_id,
                    user_id,
                ),
            )

            date = cursor.fetchone()

            cursor.close()
            db_conn.cnx.close()

            if date is not None:
                answer_date = datetime.strptime(
                    f"{date[0]}", "%Y-%m-%d"
                ).date()
                current_date = datetime.today().date()

                return {"new_checkup": (current_date > answer_date)}

            return {"new_checkup": True}

        except mysql.connector.Error as err:
            return err

    def register_checkup(self, checkup_id, user_id, answer, answer_date):
        """Register a checkup answer for a specific checkup ID."""
        try:
            db_conn = DBConnection()
            cursor = db_conn.cnx.cursor()

            query = """INSERT INTO Checkup_answer
             (checkup_id, user_id, answer, answer_date)
              VALUES (%s, %s, %s, %s)"""

            data = (checkup_id, user_id, answer, answer_date)

            cursor.execute(query, data)
            db_conn.cnx.commit()

            cursor.close()
            db_conn.cnx.close()

            return {"answer_registered": True}

        except mysql.connector.Error:
            return {"answer_registered": False}
