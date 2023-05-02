"""Journal Module."""

import mysql.connector
from src.utils.db_connection.db_connection import DBConnection


class Journal:
    """Journal class."""

    def __init__(self):
        """Initialize Journal object with provided data."""
        pass
        
        
    def create_journal(self, journal_content, journal_date,
                       journal_title, user_id):
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

            database.cursor.close()
            database.cnx.close()

            return {"journal_created": True}

        except mysql.connector.Error:
            return {"journal_created": False}

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
    