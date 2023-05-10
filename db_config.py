#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""db_config module."""

from src.utils.db_connection.db_connection import DBConnection


def db_config():
    """db_config function."""
    conn = DBConnection()
    cursor = conn.cnx.cursor()

    cursor.execute("SHOW TABLES LIKE 'User';")
    user_exists = cursor.fetchone() is not None

    if user_exists:
        print("User table exists!")
    else:
        cursor.execute(
            "CREATE TABLE User (user_id int NOT NULL AUTO_INCREMENT, "
            + "first_name varchar(255) NOT NULL, "
            + "last_name varchar(255) NOT NULL, "
            + "email varchar(255) NOT NULL, "
            + "password varchar(255) NOT NULL, "
            + "birth date NOT NULL, "
            + "gender enum('male','female') NOT NULL, "
            + "doctor_key varchar(255) DEFAULT NULL, "
            + "PRIMARY KEY (user_id), "
            + "UNIQUE KEY email (email), "
            + "UNIQUE KEY doctor_key (doctor_key))"
        )

    cursor.execute("SHOW TABLES LIKE 'Journal';")
    journal_exists = cursor.fetchone() is not None

    if journal_exists:
        print("Journal table exists!")
    else:
        cursor.execute(
            "CREATE TABLE Journal ("
            "journal_id int NOT NULL AUTO_INCREMENT "
            + "user_id int NOT NULL, "
            + "journal_title varchar(255) NOT NULL, "
            + "journal_content text NOT NULL, "
            + "journal_date date NOT NULL, "
            + "PRIMARY KEY (journal_id), "
            + "KEY fk_user_id (user_id), "
            + "CONSTRAINT fk_user_id FOREIGN KEY (user_id) "
            + "REFERENCES User (user_id) ON DELETE CASCADE)"
        )

    cursor.execute("SHOW TABLES LIKE 'Checkup';")
    checkup_exists = cursor.fetchone() is not None

    if checkup_exists:
        print("Checkup table exists!")
    else:
        cursor.execute(
            "CREATE TABLE Checkup ("
            "checkup_id int NOT NULL AUTO_INCREMENT, "
            + "checkup_content varchar(255) NOT NULL, "
            + "PRIMARY KEY (checkup_id))"
        )

    cursor.execute("SHOW TABLES LIKE 'Checkup_answer';")
    checkup_answer_exists = cursor.fetchone() is not None

    if checkup_answer_exists:
        print("Checkup_answer table exists!")
    else:
        cursor.execute(
            "CREATE TABLE Checkup_answer ("
            "answer_id int NOT NULL AUTO_INCREMENT, "
            + "checkup_id int NOT NULL, "
            + "user_id int NOT NULL, "
            + "answer tinyint(1) DEFAULT NULL, "
            + "answer_date date DEFAULT NULL, "
            + "PRIMARY KEY (answer_id), "
            + "KEY fk_checkup_id (checkup_id), "
            + "KEY fk_user_id_checkup_answer (user_id), "
            + "CONSTRAINT fk_checkup_id FOREIGN KEY (checkup_id) "
            + "REFERENCES Checkup (checkup_id) ON DELETE CASCADE, "
            + "CONSTRAINT fk_user_id_checkup_answer FOREIGN KEY (user_id) "
            + "REFERENCES User (user_id) ON DELETE CASCADE)"
        )

    conn.cursor.close()
    conn.cnx.close()


if __name__ == "__main__":
    db_config()
