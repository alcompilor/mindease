"""Unittest User Class"""

import unittest
import datetime

from unittest.mock import MagicMock

from src.utils.user.user import User, DBConnection


class TestUserClass(unittest.TestCase):
    """Tests User Class"""

    def setUp(self):
        """Method to setup data as placeholders for testing purposes."""

        self.email = "jacksonreacher@gmail.com"
<<<<<<< HEAD
        self.user_id = 40
        self.name = "Jackson"
        self.birth = datetime.date(1955, 5, 5)
        self.gender = "male"
        self.password = "pass1234"

        self.user = User(self.name, self.birth, self.email, self.password, self.gender, self.user_id)
=======
        self.user_id = 41
        self.first_name = "Jackson"
        self.last_name = "Reacher"
        self.birth = datetime.date(1955, 5, 5)
        self.gender = "male"
        self.password = "pass1234"
        self.doctor_key = "A43212DADD1321"

        self.user = User(self.first_name, self.last_name, self.birth, self.email, self.password, self.gender, self.user_id, self.doctor_key)
>>>>>>> f978cb6058741b491195f115164516c5aca3ea50

        self.db_connection = MagicMock(spec=DBConnection)
        self.db_connection.cursor = MagicMock()
        self.db_connection.cursor.fetchone = MagicMock()
        self.db_connection.cursor.close = MagicMock()
        self.db_connection.cnx = MagicMock()
        self.db_connection.cnx.close = MagicMock()

    def test_get_user_id(self):
        """Tests the retrieval of a user id."""

        self.db_connection.cursor.fetchone.return_value = self.user_id
        DBConnection.return_value = self.db_connection

        result = self.user.get_user_id(self.email)
        self.assertEqual(result, {"user_id": self.user_id})

<<<<<<< HEAD
    def test_get_name(self):
        """Tests the retrieval of a name that belongs to a user."""

        self.db_connection.cursor.fetchone.return_value = self.name
        DBConnection.return_value = self.db_connection

        result = self.user.get_name(self.email)
        self.assertEqual(result, {"name": self.name})
=======
    def test_get_first_name(self):
        """Tests the retrieval of a first_name that belongs to a user."""

        self.db_connection.cursor.fetchone.return_value = self.first_name
        DBConnection.return_value = self.db_connection

        result = self.user.get_first_name(self.email)
        self.assertEqual(result, {"first_name": self.first_name})

    def test_get_last_name(self):
        """Tests the retrieval of a last_name that belongs to a user."""

        self.db_connection.cursor.fetchone.return_value = self.last_name
        DBConnection.return_value = self.db_connection

        result = self.user.get_last_name(self.email)
        self.assertEqual(result, {"last_name": self.last_name})
>>>>>>> f978cb6058741b491195f115164516c5aca3ea50

    def test_get_birth(self):
        """Tests the retrieval of a users date of birth."""

        self.db_connection.cursor.fetchone.return_value = self.birth
        DBConnection.return_value = self.db_connection

        result = self.user.get_birth(self.email)
        self.assertEqual(result, {"birth": self.birth})

    def test_get_email(self):
        """Tests the retrieval of a users email."""

        self.db_connection.cursor.fetchone.return_value = self.email
        DBConnection.return_value = self.db_connection

        result = self.user.get_email(self.email)
        self.assertEqual(result, {"email": self.email})

    def test_get_password(self):
        """Tests the retrieval of a users password."""

        self.db_connection.cursor.fetchone.return_value = self.password
        DBConnection.return_value = self.db_connection

        result = self.user.get_password(self.email)
        self.assertEqual(result, {"password": self.password})

    def test_get_gender(self):
        """Tests the retrieval of a users gender."""

        self.db_connection.cursor.fetchone.return_value = self.gender
        DBConnection.return_value = self.db_connection

        result = self.user.get_gender(self.email)
        self.assertEqual(result, {"gender": self.gender})

<<<<<<< HEAD
    def test_update_name(self):
        """Tests the update of a users name."""

        new_name = "Jackson"
=======
    def test_get_doctor_key(self):
        """Tests the retrieval of a users doctor_key."""

        self.db_connection.cursor.fetchone.return_value = self.doctor_key
        DBConnection.return_value = self.db_connection

        result = self.user.get_doctor_key(self.user_id)
        self.assertEqual(result, {"doctor_key": self.doctor_key})

    def test_update_first_name(self):
        """Tests the update of a users first_name."""

        new_first_name = "Jackson"
>>>>>>> f978cb6058741b491195f115164516c5aca3ea50

        DBConnection.cursor = MagicMock()
        DBConnection.cursor.execute = MagicMock()
        DBConnection.cnx = MagicMock()
        DBConnection.cnx.commit = MagicMock()

<<<<<<< HEAD
        response = self.user.update_name(new_name, self.email)
        self.assertEqual(response, {"name_changed": True})
=======
        response = self.user.update_first_name(new_first_name, self.email)
        self.assertEqual(response, {"first_name_changed": True})

    def test_update_last_name(self):
        """Tests the update of a users last_name."""

        new_last_name = "Reacher"

        DBConnection.cursor = MagicMock()
        DBConnection.cursor.execute = MagicMock()
        DBConnection.cnx = MagicMock()
        DBConnection.cnx.commit = MagicMock()

        response = self.user.update_last_name(new_last_name, self.email)
        self.assertEqual(response, {"last_name_changed": True})
>>>>>>> f978cb6058741b491195f115164516c5aca3ea50

    def test_update_password(self):
        """Tests the update of a users password."""

        new_password = "pass1234"

        DBConnection.cursor = MagicMock()
        DBConnection.cursor.execute = MagicMock()
        DBConnection.cnx = MagicMock()
        DBConnection.cnx.commit = MagicMock()

        response = self.user.update_password(new_password, self.email)
        self.assertEqual(response, {"password_changed": True})

    def test_update_email(self):
        """Tests the update of a users email."""

        new_email = "jacksonreacher@gmail.com"

        DBConnection.cursor = MagicMock()
        DBConnection.cursor.execute = MagicMock()
        DBConnection.cnx = MagicMock()
        DBConnection.cnx.commit = MagicMock()

        response = self.user.update_email(new_email, self.email)
        self.assertEqual(response, {"email_changed": True})

<<<<<<< HEAD
=======
    def test_update_doctor_key(self):
        """Tests the update of a users doctor_key."""

        old_doctor_key = self.user.doctor_key

        DBConnection.cursor = MagicMock()
        DBConnection.cursor.execute = MagicMock()
        DBConnection.cnx = MagicMock()
        DBConnection.cnx.commit = MagicMock()

        response = self.user.update_doctor_key(old_doctor_key)
        self.assertEqual(response, {"doctor_key_updated": True})

>>>>>>> f978cb6058741b491195f115164516c5aca3ea50
    def test_delete_user(self):
        """Tests the deletion of a user."""

        self.db_connection.cursor.execute.return_value = None
        self.db_connection.cnx.commit.return_value = None
        DBConnection.return_value = self.db_connection

        result = self.user.delete_user(self.email)
        self.assertEqual(result, {"user_deleted": True})

if __name__ == '__main__':
    unittest.main()
    