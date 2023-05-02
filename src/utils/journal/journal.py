"""Journal Module."""

import mysql.connector
from src.utils.db_connection.db_connection import DBConnection


class Journal:
    """Journal class."""

    def __init__(self, journal_content, journal_date,
                journal_title, user_id):
        """Initialize Journal object with provided data."""
        self.journal_content = journal_content
        self.journal_date = journal_date
        self.journal_title = journal_title
        self.user_id = user_id

    def create_journal(self, journal_content, journal_date,
                    journal_title, user_id, journal_id):
        """Create a journal."""
        try:
            database = DBConnection()
            query = "INSERT INTO Journal (user_id, " + \
                    "journal_title, journal_content, journal_date" + \
                    ") VALUES (%s, %s, %s, %s)"
            database.cursor.execute(query, (user_id,
                                    journal_title, journal_content,
                                    journal_date))
            database.cnx.commit()

            query = "SELECT journal_id, user_id, " + \
                    "journal_title, journal_content, journal_date " + \
                    "FROM Journal WHERE journal_id = %s"
            database.cursor.execute(query, (journal_id,))
            content = database.cursor.fetchone()

            database.cursor.close()
            database.cnx.close()

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return {"error": str(err)}

        return \
            {"journal_content": {
                "id": content[0], "user": content[1], "title": content[2],
                "content": content[3], "date": content[4]
            }} if content else None

    def get_all_journals(self):
        """Fetch all journals."""
        try:
            database = DBConnection()
            query = "SELECT journal_id, user_id, " + \
                    "journal_title, journal_content, journal_date " + \
                    "FROM Journal"
            database.cursor.execute(query)
            results = database.cursor.fetchall()
            journals = []
            for result in results:
                journals.append({"journal_content": {
                    "id": result[0], "user": result[1], "title": result[2],
                    "content": result[3], "date": result[4]
                }})
            database.cursor.close()
            database.cnx.close()

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return {"error": str(err)}

        return journals

    def search_journals(self, user_id, journal_date):
        """Fetch journals based on user_id and date."""
        try:
            database = DBConnection()
            query = "SELECT journal_id, user_id, " + \
                    "journal_title, journal_content, journal_date " + \
                    "FROM Journal WHERE user_id = %s AND journal_date = %s"
            database.cursor.execute(query, (user_id, journal_date))
            results = database.cursor.fetchall()
            journals = []
            for result in results:
                journals.append({"journal_content": {
                    "id": result[0], "user": result[1], "title": result[2],
                    "content": result[3], "date": result[4]
                }})
            database.cursor.close()
            database.cnx.close()

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return {"error": str(err)}

        return journals