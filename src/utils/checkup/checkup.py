"""Checkup integrated class."""

import mysql.connector
import datetime

from src.utils.db_connection.db_connection import DBConnection

class CheckUp:
    """Checkup class"""

    def __init__(self, db_file):
        self.conn = DBConnection
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()


    def fetch_checkup(self, date):
        """Fetches the checkup for a specific date from the database."""
        
        db = DBConnection()
        query = "SELECT * FROM checkup_answer WHERE date = ?"
        db.cursor.execute(query, date)
        result = db.cursor.fetchone()
        db.cursor.close()
        db.cnx.close()
        return {"Today's checkup: " : result[0] if result else None}
    

    def fetch_latest_check(self, checkup_id):
        """Fetches the latest checkup answer for a specific checkup ID."""
        
        db = DBConnection()
        query = "SELECT * FROM checkup_answer WHERE checkup_id = ? ORDER BY id DESC LIMIT 1"
        db.cursor.execute(query, checkup_id)
        result = db.cursor.fetchone()
        return {"The answer for the checkup is " : result}
    

    def check_answer(self, answer_id):
        """Check if the checkup answer with given ID was stored in the last 24 hours or more."""
        
        db = DBConnection()
        query = "SELECT created_at FROM checkup_answer WHERE id = ?"
        db.cursor.execute(query, answer_id)
        answer_date = datetime.datetime.strptime(self.cursor.fetchone()[0], "%Y-%m-%d %H:%M:%S.%f")
        db.cursor.close()
        db.cnx.close()
        return {datetime.datetime.now() - answer_date >= datetime.timedelta(days=1)}


    def register_checkup(self, checkup_id, answer):
        """Registers a checkup answer for a specific checkup ID."""
        
        try:
            db = DBConnection()
            query = "INSERT INTO checkup_answer (checkup_id, answer) VALUES (?, ?)"
            data = (checkup_id, answer)
            if answer < 1 or answer > 5:
                raise ValueError("Answer must be a number between 1 and 5.")
            db.cursor.execute(query, data)
            db.cnx.commit()
            registered = True
        
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            registered = False
        
        db.cursor.close()
        db.cnx.close()
        return {"Answer Regsitered" : registered}


"""""
def collect_checkup(self, user_id):
    db = DBConnection()
    cursor = db.cnx.cursor()
    query = ("SELECT * FROM checkup WHERE id = %s")
    checkup_id = 1
    cursor.execute(query, (checkup_id))
    checkup_data = cursor.fetchone()
    
    cursor.close()
    db.cnx.close()
    print(checkup_data)
"""""