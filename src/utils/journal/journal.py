"""Journal Module."""

import mysql.connector
from src.utils.db_connection.db_connection import DBConnection


class Journal:
    """Journal class."""

    def __init__(self, content=None, date=None, title=None, user_id=None):
        """Initialize Journal object with provided data."""
        self.content = content
        self.date = date
        self.title = title
        self.user_id = user_id

    def create_journal(
        self, journal_content, journal_date, journal_title, user_id
    ):
        """Create a journal."""
        try:
            database = DBConnection()
            query = (
                "INSERT INTO Journal (user_id, "
                + "journal_title, journal_content, journal_date"
                + ") VALUES (%s, %s, %s, %s)"
            )
            database.cursor.execute(
                query, (user_id, journal_title, journal_content, journal_date)
            )
            database.cnx.commit()

            database.cursor.close()
            database.cnx.close()

            return {"journal_created": True}

        except mysql.connector.Error:
            return {"journal_created": False}

    def get_all_journals(self, user_id):
        """Fetch all journals."""
        try:
            database = DBConnection()
            query = (
                "SELECT journal_id, user_id, "
                + "journal_title, journal_content, journal_date "
                + "FROM Journal "
                + "WHERE user_id = %s"
            )
            database.cursor.execute(query, (user_id,))
            results = database.cursor.fetchall()
            journals = []
            for result in results:
                journals.append(
                    {
                        "journal_content": {
                            "id": result[0],
                            "user": result[1],
                            "title": result[2],
                            "content": result[3],
                            "date": result[4],
                        }
                    }
                )
            database.cursor.close()
            database.cnx.close()

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return {"error": str(err)}

        return journals

    def search_journals(self, user_id, search_query):
        """Fetch journals based on user_id and date."""
        try:
            database = DBConnection()
            query = (
                "SELECT journal_id, user_id, "
                + "journal_title, journal_content, journal_date "
                + "FROM Journal WHERE user_id = %s AND "
                + "(journal_title LIKE %s OR journal_content LIKE %s OR "
                + "journal_date LIKE %s)"
            )
            wildcard_query = f"%{search_query}%"
            database.cursor.execute(
                query,
                (user_id, wildcard_query, wildcard_query, wildcard_query),
            )
            results = database.cursor.fetchall()
            journals = []
            for result in results:
                journals.append(
                    {
                        "journal_content": {
                            "id": result[0],
                            "user": result[1],
                            "title": result[2],
                            "content": result[3],
                            "date": result[4],
                        }
                    }
                )
            database.cursor.close()
            database.cnx.close()

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return {"error": str(err)}

        return journals
