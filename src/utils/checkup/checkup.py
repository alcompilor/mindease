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


    def fetch_checkup(self, checkup_id):
        """Fetches new checkup for the day from the database."""
        try:
            db = DBConnection()
            query = "SELECT * FROM checkup_answer WHERE checkup_id = %s ORDER BY id DESC LIMIT 1"
            db.cursor.execute(query, checkup_id)
            result = db.cursor.fetchone()
            
            todays_checkup = result[1] + 1
            if not result:
                checkup_id = 1
            
            if checkup_id > 30:
                checkup_id = 1
                db.cursor.execute()
                
            # Get the next checkup:
            query2 = ("SELECT * FROM checkup WHERE id = %s")
            db.cursor.execute(query2)
            
            """""    
            if result:
                last_checkup_id = result[0]
                next_checkup = (last_checkup_id % 30) +1
            else:
                next_checkup = 1
            return next_checkup
            """
        except mysql.connector.Error as e:
            print(f"Error: {e}")
        
        db.cursor.close()
        db.cnx.close()
    
        return {"Todays_checkup: " : todays_checkup}
    

    def fetch_latest_check(self, checkup_id):
        """Fetches the latest checkup answer for a specific checkup ID."""
        
        db = DBConnection()
        query = "SELECT * FROM checkup_answer WHERE checkup_id = %s ORDER BY id DESC LIMIT 1"
        db.cursor.execute(query, checkup_id)
        result = db.cursor.fetchone()
    
        return {"latest_checkup" : result}
    

    def check_answer(self, answer_id):
        """Check if the checkup answer with given ID was stored in the last 24 hours or more."""
        
        try:
            db = DBConnection()
            query = "SELECT created_at FROM checkup_answer WHERE id = %s"
            db.cursor.execute(query, answer_id)
            answer_date = datetime.datetime.strptime(self.cursor.fetchone()[0], "%Y-%m-%d %H:%M:%S.%f")
            success = True
        
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            success = False
        
        db.cursor.close()
        db.cnx.close()
        checked_answer = datetime.datetime.now() - answer_date >= datetime.timedelta(days=1)
        
        return {"checked_answer" : checked_answer}


    def register_checkup(self, checkup_id,user_id, answer, answer_date):
        """Registers a checkup answer for a specific checkup ID."""
        
        try:
            db = DBConnection()
            query = "INSERT INTO checkup_answer (checkup_id, user_id, answer, answer_date) VALUES (%s, %s, %s, %s)"
            data = (checkup_id,user_id, answer,answer_date)
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
        return {"answer_regsitered" : registered}