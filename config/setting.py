import mysql.connector
from mysql.connector import Error


class DatabaseConfig:
    @staticmethod
    def get_connection():
        try:
            connection = mysql.connector.connect(
                host="localhost",       # Replace with your DB host
                user="root",            # Replace with your DB user
                password="sonam",    # Replace with your DB password
                database="quiz_system"  # Replace with your DB name
            )
            if connection.is_connected():
                print("Database connection established.")
                return connection
        except Error as e:
            print(f"Error connecting to database: {e}")
        return None
