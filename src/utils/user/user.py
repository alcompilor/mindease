"""User integrated Class."""

import time
import secrets

import mysql.connector

from src.utils.db_connection.db_connection import DBConnection


class User:
    """User Class."""

    def __init__(self):
        """Create a User object using the provided data."""

    def get_user_id(self, email=None, doctor_key=None):
        """Fetch user_id from table in the DB."""
        database = DBConnection()

        if doctor_key is None:
            query = "SELECT user_id FROM User WHERE email = %s"
            database.cursor.execute(query, (email,))
        elif email is None:
            query = "SELECT user_id FROM User WHERE doctor_key = %s"
            database.cursor.execute(query, (doctor_key,))

        result = database.cursor.fetchone()
        database.cursor.close()
        database.cnx.close()
        return {"user_id": result[0]} if result else None

    def get_first_name(self, email):
        """Fetch first_name from table in the DB."""
        database = DBConnection()
        query = "SELECT first_name FROM User WHERE email = %s"
        database.cursor.execute(query, (email,))
        result = database.cursor.fetchone()
        database.cursor.close()
        database.cnx.close()
        return {"first_name": result[0]} if result else None

    def get_last_name(self, email):
        """Fetch last_name from table in the DB."""
        database = DBConnection()
        query = "SELECT last_name FROM User WHERE email = %s"
        database.cursor.execute(query, (email,))
        result = database.cursor.fetchone()
        database.cursor.close()
        database.cnx.close()
        return {"last_name": result[0]} if result else None

    def get_birth(self, email):
        """Fetch age/birth from table in the DB."""
        database = DBConnection()
        query = "SELECT birth FROM User WHERE email = %s"
        database.cursor.execute(query, (email,))
        result = database.cursor.fetchone()
        database.cursor.close()
        database.cnx.close()
        return {"birth": result[0]} if result else None

    def get_email(self, user_id):
        """Fetch email from table in the DB."""
        database = DBConnection()
        query = "SELECT email FROM User WHERE user_id = %s"
        database.cursor.execute(query, (user_id,))
        result = database.cursor.fetchone()
        database.cursor.close()
        database.cnx.close()
        return {"email": result[0]} if result else None

    def get_password(self, email):
        """Fetch password from table in the DB."""
        database = DBConnection()
        query = "SELECT password FROM User WHERE email = %s"
        database.cursor.execute(query, (email,))
        result = database.cursor.fetchone()
        database.cursor.close()
        database.cnx.close()
        return {"password": result[0]} if result else None

    def get_gender(self, email):
        """Fetch gender of a user from table in the DB."""
        database = DBConnection()
        query = "SELECT gender FROM User WHERE email = %s"
        database.cursor.execute(query, (email,))
        result = database.cursor.fetchone()
        database.cursor.close()
        database.cnx.close()
        return {"gender": result[0]} if result else None

    def get_doctor_key(self, user_id):
        """Fetch doctor_key of a user from table in the DB."""
        database = DBConnection()
        query = "SELECT doctor_key FROM User WHERE user_id = %s"
        database.cursor.execute(query, (user_id,))
        result = database.cursor.fetchone()
        database.cursor.close()
        database.cnx.close()
        return {"doctor_key": result[0]} if result else None

    def update_first_name(self, new_first_name, email):
        """Update the first_name of a user in the DB."""
        query = "UPDATE User SET first_name = %s WHERE email = %s"
        data = (new_first_name, email)

        try:
            database = DBConnection()
            database.cursor.execute(query, data)
            database.cnx.commit()
            success = True

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            success = False

        database.cursor.close()
        database.cnx.close()

        return {"first_name_changed": success}

    def update_last_name(self, new_last_name, email):
        """Update the last_name of a user in the DB."""
        query = "UPDATE User SET last_name = %s WHERE email = %s"
        data = (new_last_name, email)

        try:
            database = DBConnection()
            database.cursor.execute(query, data)
            database.cnx.commit()
            success = True

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            success = False

        database.cursor.close()
        database.cnx.close()

        return {"last_name_changed": success}

    def update_email(self, new_email, email):
        """Update the email of a user in the DB."""
        query = "UPDATE User SET email = %s WHERE email = %s"
        data = (new_email, email)

        try:
            database = DBConnection()
            database.cursor.execute(query, data)
            database.cnx.commit()
            success = True

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            success = False

        database.cursor.close()
        database.cnx.close()

        return {"email_changed": success}

    def update_password(self, new_password, email):
        """Update the password of a user in the DB."""
        query = "UPDATE User SET password = %s WHERE email = %s"
        data = (new_password, email)

        try:
            database = DBConnection()
            database.cursor.execute(query, data)
            database.cnx.commit()
            success = True

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            success = False

        database.cursor.close()
        database.cnx.close()

        return {"password_changed": success}

    def update_doctor_key(self, doctor_key):
        """Update the doctor_key of a user in the DB."""
        key_length = secrets.choice(range(15, 21))
        key = secrets.token_urlsafe(key_length)

        timestamp = str(int(time.time() * 1000))
        key = f"{key}{timestamp}"

        query = "UPDATE User SET doctor_key = %s WHERE doctor_key = %s"
        data = (key, doctor_key)

        try:
            database = DBConnection()
            database.cursor.execute(query, data)
            database.cnx.commit()
            success = True

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            success = False

        database.cursor.close()
        database.cnx.close()

        return {"doctor_key_updated": success}

    def delete_user(self, email):
        """Delete a user from the DB."""
        query = "DELETE FROM User WHERE email = %s"
        data = (email,)

        try:
            database = DBConnection()
            database.cursor.execute(query, data)
            database.cnx.commit()
            success = True

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            success = False

        database.cursor.close()
        database.cnx.close()

        return {"user_deleted": success}
