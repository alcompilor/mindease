from src.utils.db_connection.db_connection import DBConnection
import mysql.connector


class Register:
    def __init__(self):
        pass

    def register_user(self, user):

        self.first_name = user['first_name']
        self.last_name = user['last_name']
        self.email = user['email']
        self.password = user['password']
        self.age = user['age']
        self.gender = user['gender']

        query = 'INSERT INTO User \
            (first_name, last_name, email, \
            password, age, gender) VALUES \
            (%s, %s, %s, %s, %s, %s)'

        params = (
            self.first_name, 
            self.last_name, 
            self.email, 
            self.password, 
            self.age, 
            self.gender
            )

        try:
            conn = DBConnection()

            conn.cursor.execute(query, params)
            conn.cnx.commit()
            return {'registration_succeeded': True}
            
        except mysql.connector.Error as err:
            print(f'error: {err}')
            return {'registration_succeeded': False}
