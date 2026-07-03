import mysql.connector

from config.settings import (DB_HOST, DB_NAME, DB_PORT, DB_USER, DB_PASSWORD)

class Database:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = mysql.connector.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )

        self.cursor = self.connection.cursor()


    def get_cursor(self):
        return self.cursor
    
    def commit(self):
        self.connection.commit()

    def rollback(self):
        self.connection.rollback()

    def close(self):
        if self.cursor:
            self.cursor.close()

        if self.connection and self.connection.is_connected():
            self.connection.close()
        
    def is_connected(self):
        return (
            self.connection is not None
            and self.connection.is_connected()
        )