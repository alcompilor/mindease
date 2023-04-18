import mysql.connector


class db_connection:

    def config_db_connection(self):

        self.cnx = mysql.connector.connect(
            database = 'mindease',
            host = '93.190.141.70',
            user = 'mindease_user',
            password = 'X3sh1sAvWa4NGWDw',
            auth_plugin='mysql_native_password'
        )

        self.cursor = cnx.cursor()
        