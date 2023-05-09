#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""DBConnection module."""

import os
import mysql.connector  # pylint: disable=import-error
from dotenv import load_dotenv


class DBConnection:
    """DBConnection Class."""

    def __init__(self):
        """Init constructor for DBConnection class."""
        load_dotenv()

        self.cnx = mysql.connector.connect(
            database=os.getenv("DATABASE_NAME"),
            host=os.getenv("DATABASE_HOSTNAME"),
            user=os.getenv("DATABASE_USER"),
            password=os.getenv("DATABASE_PASSWORD"),
            auth_plugin="mysql_native_password",
        )

        self.cursor = self.cnx.cursor()
