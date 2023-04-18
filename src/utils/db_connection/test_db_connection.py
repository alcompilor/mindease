import mysql.connector
import unittest


class test_db_connection(unittest.TestCase):
    
    def test_config_db_connection(self):

        self.cnx = mysql.connector.connect(
            database = 'mindease',
            host = '93.190.141.70',
            user = 'mindease_user',
            password = 'X3sh1sAvWa4NGWDw',
            auth_plugin='mysql_native_password'
        )

        self.cursor = self.cnx.cursor()
        query = 'SELECT VERSION()'
        self.cursor.execute(query)
        row = self.cursor.fetchone()

        self.assertIsNotNone(row, 'Connection Failed')
