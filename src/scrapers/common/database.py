import mysql.connector
from src.scrapers.common.logger import get_logger

from config.settings import (DB_HOST, DB_NAME, DB_PORT, DB_USER, DB_PASSWORD)

logger = get_logger("Database")


class Database:
    def __init__(self):
        self.connection = None
        self.cursor = None


    def connect(self):
        logger.info("Connecting to MySQL database...")
        try:
            self.connection = mysql.connector.connect(
                host=DB_HOST,
                port=DB_PORT,
                database=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD
            )
            logger.info("Succesfully connected to MySQL Database.")
            self.cursor = self.connection.cursor()
        except Exception as e:
            logger.error(f"Failed to connect to MySQL database: {e}")            
        


    def get_cursor(self):
        return self.cursor
    
    def commit(self):
        logger.info("Transaction committed successfully.")
        self.connection.commit()

    def rollback(self):
        self.connection.rollback()

    def close(self):
        if self.cursor:
            self.cursor.close()
            logger.info("Closing MySQL database connection.")
            logger.inof("Connection closed.")

        if self.connection and self.connection.is_connected():
            self.connection.close()

        
        
    def is_connected(self):
        return (
            self.connection is not None
            and self.connection.is_connected()
        )